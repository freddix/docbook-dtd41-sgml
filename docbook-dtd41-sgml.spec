%define		ver	4.1
%define		sver	41
#
Summary:	DocBook - DTD for technical documentation
Name:		docbook-dtd%{sver}-sgml
Version:	1.0
Release:	22
Vendor:		OASIS
License:	Free
Group:		Applications/Publishing/SGML
URL:		http://www.oasis-open.org/docbook/
Source0:	http://www.oasis-open.org/docbook/sgml/%{ver}/docbk%{sver}.zip
# Source0-md5:	489f6ff2a2173eb1e14216c10533ede2
BuildRequires:	unzip
Requires(post,postun):	sgml-common
Requires:	sgmlparser
Requires:	sgml-common
Provides:	docbook-dtd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DocBook - DTD for technical documentation.

%prep
%setup -q -c
chmod 644 *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

install  *.dtd *.mod *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/

# install catalog (but filter out ISO entities)
grep -v 'ISO ' docbook.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/catalog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q /etc/sgml/sgml-docbook-%{ver}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc *.txt ChangeLog
%{_datadir}/sgml/docbook/*

