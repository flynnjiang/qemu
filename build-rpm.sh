#!/bin/sh

SUDO=
if [ `id -u` -ne 0 ]; then
	SUDO=sudo
fi

TOPDIR=$PWD/rpmbuild

SPEC_FILE=`ls -1 $TOPDIR/SPECS/*.spec 2>/dev/null | head -1`
if [ -z "$SPEC_FILE" ]; then
    echo "RPM spec file was not found in $TOPDIR/SPECS/."
    exit 1
fi

if ! dnf builddep --help >/dev/null 2>&1; then
       $SUDO dnf -y install dnf-plugins-core
fi

# Install build dependencies
if ! $SUDO dnf -y builddep $SPEC_FILE; then
	exit 1
fi

if ! command -v git >/dev/null; then
	$SUDO dnf -y install git
fi

if ! command -v meson >/dev/null; then
	$SUDO dnf -y install meson
fi

if ! command -v rpmspec >/dev/null; then
	$SUDO dnf -y install rpm-build
fi

SRC_PKG=`rpmspec -P $SPEC_FILE 2>/dev/null | grep "^Source0:" | cut -c 9- | xargs basename`
SRC_DIR=`basename $SRC_PKG .tar.xz`

# QEMU specific: download subprojects
#SUBPROJECTS="libvfio-user keycodemapdb berkeley-softfloat-3 berkeley-testfloat-3"
#if ! meson subprojects download keycodemapdb; then
#	exit 1
#fi

mkdir -p $TOPDIR/SOURCES
#git archive -v --prefix=$SRC_DIR/ -o $TOPDIR/SOURCES/$SRC_PKG HEAD
tar --exclude=.git --exclude=rpmbuild --xform="s/^\.\//$SRC_DIR\//" -cvjf $TOPDIR/SOURCES/$SRC_PKG .
if [ $? -ne 0 ]; then
    echo "Create $SRC_PKG failed."
    exit 1
fi

rpmbuild --define="_topdir $TOPDIR" -ba --without check $SPEC_FILE
