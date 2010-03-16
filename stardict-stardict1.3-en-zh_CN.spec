%define	version	2.4.2
%define release %mkrel 6
%define dict_format_version	2.4.2

Summary:	StarDict 1.3 dictionary (English -> Simplified Chinese) converted to StarDict 2
Name:		stardict-stardict1.3-en-zh_CN
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-stardict1.3-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
This package contains StarDict 1.3 dictionary (English -> Simplified Chinese)
database converted into StarDict 2 format.

%prep
%setup -q -n stardict-stardict1.3-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


