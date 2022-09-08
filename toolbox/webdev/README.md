# webdev

My image to create containers with web development tools. 

## Build webdev image

### Using 'base' fedora image

Type:
```
podman build . --build-arg=JAVA_VERSION=11 --no-cache -t webdev 
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version

### Using Arch base

```
podman build . -f Containerfile-arch --no-cache --build-arg=JAVA_VERSION=11 --build-arg=LANGUAGE=en_US.UTF-8 --build-arg=USER=$USER -t webdev
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version
- **LANGUAGE (optional)**: locale configuration
- **USER (required)**: Home username 

## Create toolbox

```
toolbox create -i webdev mybox
```