Name: hunspell-nr
Summary: Southern Ndebele hunspell dictionaries
%define upstreamid 20060120
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://downloads.translate.org.za/spellchecker/ndebele/myspell-nr_ZA-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Southern Ndebele hunspell dictionaries.

%prep
%setup -q -c -n hunspell-nr

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_nr_ZA.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060120-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060120-2
- mysteriously, upstream tarball no longer matches our tarball

* Tue Sep 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060120-1
- initial version
