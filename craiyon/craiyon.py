#!/usr/bin/env python3

import sys
import base64
import os
import requests

args = sys.argv[1:]

if len(args) < 1:
    print(f"Usage: {sys.argv[0]} <text> [output_dir]")
    sys.exit(0)

try:
    text = args[0]
    output_dir = os.path.abspath(args[1] if len(args) > 1 else os.getcwd())

    print(f"Generating images with '{text}' ...")

    response = requests.post(
        "https://backend.craiyon.com/generate", json={"prompt": text})

    data = response.json()

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for index, image in enumerate(data["images"]):
        image_index = index + 1

        output_file = f"{text.replace(' ', '_')}_{image_index}.jpg"

        decoded_image = base64.b64decode(image)

        print(f"Writing image file #{image_index} ...")
        with open(f"{output_dir}/{output_file}", "wb") as file:
            file.write(decoded_image)

except Exception as e:
    print(f"Error: {str(e)}")
