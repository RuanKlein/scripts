# 📦 Toolbox

This directory contains the my **Containerfiles** for some cases of use to use with OSTree based system, like Fedora Silverblue/Kinoite.

More informations about toolbox [here](https://github.com/containers/toolbox).

## Using Fedora image

Type:
```
podman build . -f Containerfile-fedora --build-arg=LANGPACK=en --build-arg=GLIBC_LANGPACK=en --build-arg=JAVA_VERSION=11 --no-cache -t fedora
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version
- **LANGPACK (optional)**: Langpack locale.
- **GLIBC_LANGPACK (optional)**: Langpack for glibc.

## Using Arch image

```
podman build . -f Containerfile-arch --no-cache --build-arg=JAVA_VERSION=11 --build-arg=LANGUAGE=en_US.UTF-8 -t arch
```

Args:
- **JAVA_VERSION (optional)**: OpenJDK version
- **LANGUAGE (optional)**: locale configuration

## Create toolbox

```
toolbox create -i <image> <container> 
```