% VHOST-DEVICE-SOUND(1) Version 0.1.0 | rust-vmm/vhost-device

NAME
====

**vhost-device-sound** — vhost-user backend for a VirtIO SOUND device

SYNOPSIS
========

| **vhost-device-sound** **-s**|**\-\-socket-path** _path_ \[**-d**|**\-\-device** _spec_]
| **vhost-device-sound** \[**-h**|**\-\-help**]

DESCRIPTION
===========

This program is a vhost-user backend for a VirtIO SOUND device.
It provides SOUND access to various entities on the host; not
necessarily only those providing an SOUND interface themselves.

It is tested with QEMU's `-device vhost-user-sound-pci` but should work
with any virtual machine monitor (VMM) that supports vhost-user. See
*EXAMPLES* section below.

Options
-------

-h, \-\-help

:   Print help.

-s, \-\-socket=PATH

:   Location of the vhost-user Unix domain sockets.

-s, \-\-socket=PATH

:   audio backend to be used [null, pipewire, alsa]

EXAMPLES
========

The daemon should be started first:

```
host# vhost-device-sound --socket /tmp/snd.sock --backend null
```

The QEMU invocation needs to create a chardev socket the device can
use to communicate as well as share the guests memory over a memfd:

```
host# qemu-system \
   -chardev socket,path=/tmp/snd.sock,id=vsnd \
   -device vhost-user-snd-pci,chardev=vsnd,id=vsnd \
   -machine YOUR-MACHINE-OPTIONS,memory-backend=mem \
   -m 4096 \
   -object memory-backend-file,id=mem,size=4G,mem-path=/dev/shm,share=on \
   ...
```

ENVIRONMENT
===========

**RUST_LOG**

:   Logging level. Set to `debug` for maximum output.

BUGS
====

See GitHub Issues: <https://github.com/rust-vmm/vhost-device/issues>

AUTHORS
======

Dorinda Bassey <dbassey@redhat.com>
Matias Ezequiel Vara Larsen <mvaralar@redhat.com>
Manos Pitsidianakis <manos@pitsidianak.is>

SEE ALSO
========

**qemu(1)**
