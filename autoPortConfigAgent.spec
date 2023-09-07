%define _rpmfilename %%{NAME}-%%{VERSION}.%%{ARCH}.rpm

Name:           autoPortConfigAgent
Version:        1.0.0
Release:        1%{?dist}
Summary:        Automatically configure ports based on mac or lldp information
BuildArch:	noarch

License:        GPL
URL:            https://github.com/aaronlott/autoPortConfigAgent
Source0:	      https://github.com/aaronlott/autoPortConfigAgent/archive/refs/tags/v%{version}.tar.gz

%description
Arista EOS Agent that will configure ports based on mac address or lldp information of the connected device


%prep
#%autosetup
%setup


%install
#%make_install
mkdir -p %{buildroot}/mnt/flash
install -m 600 autoPortConfigAgent.json %{buildroot}/mnt/flash/autoPortConfigAgent.json
install -m 755 autoPortConfigAgent.py %{buildroot}/mnt/flash/autoPortConfigAgent.py


%files
/mnt/flash/autoPortConfigAgent.py
/mnt/flash/autoPortConfigAgent.json
