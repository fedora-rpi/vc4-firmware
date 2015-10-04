%global _binaries_in_noarch_packages_terminate_build 0

%global commit 6785329266e889552b7a142563cb66d743b25610
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vc4-firmware
Version:        0
Release:        1.20151001git%{shortcommit}%{?dist}
Summary:        VideoCore 4 GPU firmware and bootloaders

Group:          System Environment/Kernel
# Has an usage restriction (1. in license)
License:        Redistributable, no modification permitted with exception
URL:            https://github.com/raspberrypi/firmware
Source0:        https://github.com/raspberrypi/firmware/archive/%{commit}/firmware-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Pre-compiled binaries of the Raspberry Pi bootloader/GPU firmware.


%prep
%setup -q -n firmware-%{commit}


%build


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
tar -C boot --exclude 'kernel*' --exclude 'COPYING*' --exclude 'LICENCE*' -cf - . |
        tar xf - -C %{buildroot}%{_datadir}/%{name}


%files
%{_datadir}/%{name}
%license boot/LICENCE.broadcom


%changelog
* Sun Oct 04 2015 Lubomir Rintel <lkundrak@v3.sk> - 0-1.20151001git6785329
- Initial packaging
