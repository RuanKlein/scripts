# base

Base image to create others images with some tools pre installed.

## Build

Type:
```
$ podman build . \
    --build-arg=FEDORA_VERSION=$(rpm -E %fedora) \
    --build-arg=LANGPACK=en \
    --build-arg=GLIBC_LANGPACK=en \
    -t base
```

Args:
- **FEDORA_VERSION (optional)**: Fedora version. "Latest" is default.
- **LANGPACK (optional)**: Langpack locale. "en" is default.
- **GLIBC_LANGPACK (optional)**: Langpack for glibc. "en" is default.

## Create toolbox

```
toolbox create -i base mybox
```
