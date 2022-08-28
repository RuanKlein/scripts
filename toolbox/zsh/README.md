# zsh

Image to create containers with zsh installed.

## Build

Type:
```
$ podman build . --build-arg=FEDORA_VERSION=36 -t zsh
```

Set **FEDORA_VERSION** to your fedora version.

## Create toolbox

```
$ toolbox create -i zsh mybox
```