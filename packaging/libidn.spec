Name:       libidn
Summary:    Internationalized Domain Name support library
Version:    1.15
Release:    6
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://www.gnu.org/software/libidn/
Source0:    http://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
Source1001: packaging/libidn.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  autoconf

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.



%package devel
Summary:    Development files for the libidn library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   glibc-devel

%description devel
This package includes header files and libraries necessary for
developing programs which use the GNU libidn library.



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%configure --disable-static \
    --disable-csharp \
    --disable-java \
    --with-pic

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 

rm -f $RPM_BUILD_ROOT/%_infodir/dir
rm -f %{buildroot}%{_libdir}/libidn.la
rm -f  $RPM_BUILD_ROOT%_infodir/libidn-components.png
rm -f %{buildroot}%{_bindir}/idn
%find_lang libidn

%remove_docs 

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libidn.lang
%manifest libidn.manifest
%defattr(-,root,root,-)
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/idna.el
%{_datadir}/emacs/site-lisp/punycode.el
%{_libdir}/libidn.so.*

%files devel
%manifest libidn.manifest
%defattr(-,root,root,-)
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libidn.pc

