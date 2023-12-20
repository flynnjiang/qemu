Name:           kemu
Version:        8.2.0-rc4
Release:        1%{?dist}
Summary:        KEMU

License:        GPL3.0+
URL:            https://www.kylinos.cn
Source0:        %{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: bison
BuildRequires: flex
BuildRequires: zlib-devel
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: libselinux-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libaio-devel
BuildRequires: python3-devel

# --enable-linux-io-uring
BuildRequires: liburing-devel

# --enable-libnfs
BuildRequires: libnfs-devel

# --enable-virglrenderer
BuildRequires: virglrenderer-devel

#Requires:       

%description
Kemu


%package img
Summary: QEMU
Conflicts: qemu-img
Provides: qemu-img
%description img

%ifarch x86_64
%global targets x86_64-softmmu
%package system-x86
Summary: QEMU
Conflicts: qemu-system-x86
Provides: qemu-system-x86
%description system-x86
%files system-x86
%{_bindir}/qemu-system-x86_64
%endif

%ifarch aarch64
%global targets aarch64-softmmu
%package system-aarch64
Summary: QEMU
Conflicts: qemu-system-aarch64
Provides: qemu-system-aarch64
%description system-aarch64
%files system-aarch64
%{_bindir}/qemu-system-aarch64
%endif

%prep
%autosetup


%build
%global firmwaredirs "%{_datadir}/qemu-firmware:%{_datadir}/ipxe/qemu:%{_datadir}/seavgabios:%{_datadir}/seabios"
meson subprojects download keycodemapdb && \
./configure \
        --extra-cflags="%{optflags}" \
        --extra-ldflags="%{build_ldflags}" \
        --prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
        --datadir="%{_datadir}" \
        --docdir="%{_docdir}" \
	--includedir="%{_includedir}"
        --libdir="%{_libdir}" \
        --libexecdir="%{_libexecdir}" \
	--localdir="%{_prefix}/share/locale"
        --localstatedir="%{_localstatedir}" \
        --sysconfdir="%{_sysconfdir}" \
	--mandir="%{_mandir}"
        --interp-prefix=%{_prefix}/qemu-%M \
        --firmwarepath="%firmwaredirs" \
        --with-pkgversion="qemu-%{version}-%{release}" \
	--disable-install-blobs \
	--disable-strip \
	--disable-download  \
	--disable-containers \
	--target-list="%targets" \
	--without-default-features	\
	--disable-af-xdp		\
	--enable-alsa			\
	--disable-attr			\
	--disable-auth-pam		\
	--disable-avx2			\
	--disable-avx512bw		\
	--disable-avx512f		\
	--disable-blkio			\
	--disable-bochs			\
	--disable-bpf			\
	--disable-brlapi		\
	--enable-bzip2			\
	--disable-canokey		\
	--disable-cap-ng		\
	--disable-capstone		\
	--disable-cloop			\
	--disable-cocoa			\
	--disable-colo-proxy		\
	--disable-coreaudio		\
	--disable-crypto-afalg		\
	--disable-curl			\
	--disable-curses		\
	--disable-dbus-display		\
	--disable-dmg			\
	--disable-docs			\
	--disable-dsound		\
	--disable-fuse			\
	--disable-fuse-lseek		\
	--disable-gcrypt		\
	--enable-gettext		\
	--enable-gio			\
	--disable-glusterfs		\
	--enable-gnutls			\
	--enable-gtk			\
	--enable-gtk-clipboard		\
	--enable-guest-agent		\
	--disable-guest-agent-msi	\
	--disable-hv-balloon		\
	--disable-hvf			\
	--enable-iconv			\
	--disable-jack			\
	--enable-keyring		\
	--enable-kvm			\
	--enable-l2tpv3			\
	--disable-libdaxctl		\
	--enable-libdw			\
	--enable-libiscsi		\
	--disable-libkeyutils		\
	--enable-libnfs			\
	--disable-libpmem		\
	--disable-libssh		\
	--disable-libudev		\
	--disable-libusb		\
	--disable-libvduse		\
	--enable-linux-aio		\
	--enable-linux-io-uring		\
	--disable-live-block-migration	\
	--disable-lzfse			\
	--disable-lzo			\
	--disable-malloc-trim		\
	--disable-membarrier		\
	--enable-modules		\
	--disable-mpath			\
	--disable-multiprocess		\
	--disable-netmap		\
	--disable-nettle		\
	--enable-numa			\
	--disable-nvmm			\
	--enable-opengl			\
	--enable-oss			\
	--enable-pa			\
	--disable-parallels		\
	--enable-pipewire		\
	--enable-pixman			\
	--disable-plugins		\
	--enable-png			\
	--disable-pvrdma		\
	--enable-qcow1			\
	--disable-qed			\
	--disable-qga-vss		\
	--disable-rbd			\
	--enable-rdma			\
	--disable-replication		\
	--disable-rutabaga-gfx		\
	--enable-sdl			\
	--disable-sdl-image		\
	--enable-seccomp		\
	--enable-selinux		\
	--disable-slirp			\
	--disable-slirp-smbd		\
	--enable-smartcard		\
	--disable-snappy		\
	--disable-sndio			\
	--disable-sparse		\
	--enable-spice			\
	--enable-spice-protocol		\
	--disable-stack-protector	\
	--disable-tcg			\
	--enable-tools			\
	--enable-tpm			\
	--disable-u2f			\
	--enable-usb-redir		\
	--disable-vde			\
	--enable-vdi			\
	--disable-vduse-blk-export	\
	--disable-vfio-user-server	\
	--enable-vhdx			\
	--enable-vhost-crypto		\
	--enable-vhost-kernel		\
	--enable-vhost-net		\
	--enable-vhost-user		\
	--enable-vhost-user-blk-server	\
	--enable-vhost-vdpa		\
	--enable-virglrenderer		\
	--disable-virtfs		\
	--disable-virtfs-proxy-helper	\
	--disable-vmdk			\
	--disable-vmnet			\
	--enable-vnc			\
	--enable-vnc-jpeg		\
	--enable-vnc-sasl		\
	--disable-vpc			\
	--disable-vte			\
	--disable-vvfat			\
	--disable-werror		\
	--disable-whpx			\
	--disable-xen			\
	--disable-xen-pci-passthrough	\
	--disable-xkbcommon		\
	--enable-zstd			\
	--enable-system			\
	--disable-user			\
	--disable-linux-user		\
	--disable-bsd-user		\
	--disable-pie			\


%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING COPYING.LIB LICENSE
%doc %{_docdir}/qemu
%{_bindir}/qemu-edid
%{_bindir}/qemu-ga
%{_bindir}/qemu-pr-helper
%{_bindir}/qemu-trace-stap
%{_libdir}/qemu/accel-qtest-x86_64.so
%{_libdir}/qemu/audio-alsa.so
%{_libdir}/qemu/audio-oss.so
%{_libdir}/qemu/audio-pa.so
%{_libdir}/qemu/audio-pipewire.so
%{_libdir}/qemu/audio-sdl.so
%{_libdir}/qemu/audio-spice.so
%{_libdir}/qemu/block-iscsi.so
%{_libdir}/qemu/block-nfs.so
%{_libdir}/qemu/chardev-spice.so
%{_libdir}/qemu/hw-display-qxl.so
%{_libdir}/qemu/hw-display-virtio-gpu-gl.so
%{_libdir}/qemu/hw-display-virtio-gpu-pci-gl.so
%{_libdir}/qemu/hw-display-virtio-gpu-pci.so
%{_libdir}/qemu/hw-display-virtio-gpu.so
%{_libdir}/qemu/hw-display-virtio-vga-gl.so
%{_libdir}/qemu/hw-display-virtio-vga.so
%{_libdir}/qemu/hw-s390x-virtio-gpu-ccw.so
%{_libdir}/qemu/hw-usb-redirect.so
%{_libdir}/qemu/hw-usb-smartcard.so
%{_libdir}/qemu/ui-egl-headless.so
%{_libdir}/qemu/ui-gtk.so
%{_libdir}/qemu/ui-opengl.so
%{_libdir}/qemu/ui-sdl.so
%{_libdir}/qemu/ui-spice-app.so
%{_libdir}/qemu/ui-spice-core.so
%{_libexecdir}/qemu-bridge-helper
%{_libexecdir}/vhost-user-gpu
%{_datadir}/applications/qemu.desktop
%{_datadir}/icons/
%{_datadir}/locale/bg/LC_MESSAGES/qemu.mo
%{_datadir}/locale/de_DE/LC_MESSAGES/qemu.mo
%{_datadir}/locale/fr_FR/LC_MESSAGES/qemu.mo
%{_datadir}/locale/hu/LC_MESSAGES/qemu.mo
%{_datadir}/locale/it/LC_MESSAGES/qemu.mo
%{_datadir}/locale/sv/LC_MESSAGES/qemu.mo
%{_datadir}/locale/tr/LC_MESSAGES/qemu.mo
%{_datadir}/locale/uk/LC_MESSAGES/qemu.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/qemu.mo
%{_mandir}/man1/qemu-img.1.gz
%{_mandir}/man1/qemu-storage-daemon.1.gz
%{_mandir}/man1/qemu-trace-stap.1.gz
%{_mandir}/man1/qemu.1.gz
%{_mandir}/man7/qemu-block-drivers.7.gz
%{_mandir}/man7/qemu-cpu-models.7.gz
%{_mandir}/man7/qemu-ga-ref.7.gz
%{_mandir}/man7/qemu-qmp-ref.7.gz
%{_mandir}/man7/qemu-storage-daemon-qmp-ref.7.gz
%{_mandir}/man8/qemu-ga.8.gz
%{_mandir}/man8/qemu-nbd.8.gz
%{_mandir}/man8/qemu-pr-helper.8.gz
%{_datadir}/qemu/QEMU,cgthree.bin
%{_datadir}/qemu/QEMU,tcx.bin
%{_datadir}/qemu/bamboo.dtb
%{_datadir}/qemu/bios-256k.bin
%{_datadir}/qemu/bios-microvm.bin
%{_datadir}/qemu/bios.bin
%{_datadir}/qemu/canyonlands.dtb
%{_datadir}/qemu/edk2-aarch64-code.fd
%{_datadir}/qemu/edk2-arm-code.fd
%{_datadir}/qemu/edk2-arm-vars.fd
%{_datadir}/qemu/edk2-i386-code.fd
%{_datadir}/qemu/edk2-i386-secure-code.fd
%{_datadir}/qemu/edk2-i386-vars.fd
%{_datadir}/qemu/edk2-licenses.txt
%{_datadir}/qemu/edk2-x86_64-code.fd
%{_datadir}/qemu/edk2-x86_64-secure-code.fd
%{_datadir}/qemu/efi-e1000.rom
%{_datadir}/qemu/efi-e1000e.rom
%{_datadir}/qemu/efi-eepro100.rom
%{_datadir}/qemu/efi-ne2k_pci.rom
%{_datadir}/qemu/efi-pcnet.rom
%{_datadir}/qemu/efi-rtl8139.rom
%{_datadir}/qemu/efi-virtio.rom
%{_datadir}/qemu/efi-vmxnet3.rom
%{_datadir}/qemu/firmware/50-edk2-i386-secure.json
%{_datadir}/qemu/firmware/50-edk2-x86_64-secure.json
%{_datadir}/qemu/firmware/60-edk2-aarch64.json
%{_datadir}/qemu/firmware/60-edk2-arm.json
%{_datadir}/qemu/firmware/60-edk2-i386.json
%{_datadir}/qemu/firmware/60-edk2-x86_64.json
%{_datadir}/qemu/hppa-firmware.img
%{_datadir}/qemu/keymaps/
%{_datadir}/qemu/kvmvapic.bin
%{_datadir}/qemu/linuxboot.bin
%{_datadir}/qemu/linuxboot_dma.bin
%{_datadir}/qemu/multiboot.bin
%{_datadir}/qemu/multiboot_dma.bin
%{_datadir}/qemu/npcm7xx_bootrom.bin
%{_datadir}/qemu/openbios-ppc
%{_datadir}/qemu/openbios-sparc32
%{_datadir}/qemu/openbios-sparc64
%{_datadir}/qemu/opensbi-riscv32-generic-fw_dynamic.bin
%{_datadir}/qemu/opensbi-riscv64-generic-fw_dynamic.bin
%{_datadir}/qemu/palcode-clipper
%{_datadir}/qemu/petalogix-ml605.dtb
%{_datadir}/qemu/petalogix-s3adsp1800.dtb
%{_datadir}/qemu/pvh.bin
%{_datadir}/qemu/pxe-e1000.rom
%{_datadir}/qemu/pxe-eepro100.rom
%{_datadir}/qemu/pxe-ne2k_pci.rom
%{_datadir}/qemu/pxe-pcnet.rom
%{_datadir}/qemu/pxe-rtl8139.rom
%{_datadir}/qemu/pxe-virtio.rom
%{_datadir}/qemu/qboot.rom
%{_datadir}/qemu/qemu-nsis.bmp
%{_datadir}/qemu/qemu_vga.ndrv
%{_datadir}/qemu/s390-ccw.img
%{_datadir}/qemu/s390-netboot.img
%{_datadir}/qemu/skiboot.lid
%{_datadir}/qemu/slof.bin
%{_datadir}/qemu/trace-events-all
%{_datadir}/qemu/u-boot-sam460-20100605.bin
%{_datadir}/qemu/u-boot.e500
%{_datadir}/qemu/vgabios-ati.bin
%{_datadir}/qemu/vgabios-bochs-display.bin
%{_datadir}/qemu/vgabios-cirrus.bin
%{_datadir}/qemu/vgabios-qxl.bin
%{_datadir}/qemu/vgabios-ramfb.bin
%{_datadir}/qemu/vgabios-stdvga.bin
%{_datadir}/qemu/vgabios-virtio.bin
%{_datadir}/qemu/vgabios-vmware.bin
%{_datadir}/qemu/vgabios.bin
%{_datadir}/qemu/vhost-user/50-qemu-gpu.json
%{_datadir}/qemu/vof-nvram.bin
%{_datadir}/qemu/vof.bin
%{_datadir}/systemtap/tapset/qemu-system-x86_64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-x86_64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-x86_64.stp

%files img
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd
%{_bindir}/qemu-storage-daemon

%changelog
* Wed Dec 20 2023 Feng Jiang <jiangfeng@kylinos.cn>
- Initial.
