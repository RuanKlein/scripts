# toolbox scripts

Useful scripts to use with toolbox.

## container_exec

This script maps any binaries from a container to the host, via symlinks. This helps maintain compatibility with host resources with binaries in a container, like desktop shortcut, nautilus or dolphin plugins, and others.

### Install

Type:
```
sudo install -m0755 container_exec /usr/local/bin/container_exec
```

#### Configuration

Set your container name to use with container_exec:
```
echo your_container_name > ~/.container_name
```

### How to use

For example, to map `code` binary from container to host, type:

```
sudo ln -s /usr/local/bin/container_exec /usr/local/bin/code
```

Assuming the Visual Studio Code is installed in the container, the `container_exec` calls `code` from container, or if is executed from inside the container, the binary will be called normally.

```
# From host or container
code ~/path/to/my/project # this works!
```

Both ways work correctly. Also, parameters are sent to binary as well.

Another example, to execute `unrar` from host:

```
sudo ln -s /usr/local/bin/container_exec /usr/local/bin/unrar
unrar help
```