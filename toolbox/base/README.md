# base

Base image to create others images with some tools pre installed.

## Build

Type:
```
podman build . --build-arg=FEDORA_VERSION=$(rpm -E %fedora) -t base
```

## Create toolbox

```
toolbox create -i base mybox
```
