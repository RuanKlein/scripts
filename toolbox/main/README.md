# main

My main image to create containers with web development tools and other tools. 

## Build main image

### Using 'base' fedora image

Type:
```
$ podman build . \
    --build-arg=JAVA_VERSION=11 \
    --no-cache \
    -t main
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version

### Using Arch base

```
$ podman build . \
    -f Containerfile-arch \
    --no-cache \
    --build-arg=JAVA_VERSION=11 \
    --build-arg=LANGUAGE=en_US.UTF-8 \
    --build-arg=USER=$USER \
    -t main
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version
- **LANGUAGE (optional)**: locale configuration

## Create toolbox

```
toolbox create -i main mybox
```