# 📦 Toolbox

More informations about toolbox [here](https://github.com/containers/toolbox).

## Using Fedora image (default)

Type:
```
podman build . --build-arg=JAVA_VERSION=11 --no-cache -t fedora
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version

## Create toolbox

```
toolbox create -i <image> <container> 
```
