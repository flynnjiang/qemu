#!/bin/sh

SUDO=
if [ $(id -u) -ne 0 ]; then
	SUDO=sudo

	if ! command -v fakeroot >/dev/null; then
		$SUDO apt-get -y install fakeroot
	fi
fi

# Install build dependencies
$SUDO env DEBIAN_FRONTEND=noninteractive apt-get -y build-dep .
if [ $? -ne 0 ]; then
	exit 1
fi

# QEMU need git to download submodules and subprojects
if ! command -v git >/dev/null; then
	$SUDO apt-get -y install git
fi

ARGS=
if [ `dpkg-architecture -q DEB_BUILD_ARCH` = "amd64" ]; then
	ARGS="$ARGS -b"
else
	ARGS="$ARGS -B"
fi
ARGS="$ARGS -uc -us"
ARGS="$ARGS -nc -tc"

if ! dpkg-buildpackage $ARGS; then
	echo "-_-! Build failed!"
	exit 1
fi

echo "^_^ Build successfully!"
