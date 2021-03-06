Summary:	Fast (incremental) CVS->* conversion
Name:		fromcvs
Version:	0.1
Release:	3
License:	GPL
Group:		Development
Source0:	http://ww2.fs.ei.tum.de/~corecode/hg/fromcvs/archive/tip.tar.bz2?/%{name}.tbz2
# Source0-md5:	65a791705a1f6a7b5fd718c1af76695e
Patch0:		ruby19.patch
URL:		http://ww2.fs.ei.tum.de/~corecode/hg/fromcvs/
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.272
BuildRequires:	ruby
BuildRequires:	sed >= 4.0
Requires:	ruby >= 1.8.5
Requires:	ruby-rbtree
Requires:	ruby-rcsparse
# for db/commitset - not packaged
#Suggests:	sqlite3-ruby
# for togit
Suggests:	git-core >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fromcvs is designed to sync to different target SCM; at the moment
there is a hg and git destination available.

%prep
%setup -qc
mv %{name}-*/* .
%if "%{pld_release}" != "ac"
%patch0 -p1
%endif

# setup shebang
%{__sed} -i -e '1i#!%{__ruby}' to*.rb
chmod a+rx to*.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_vendorlibdir}}
install -p togit.rb $RPM_BUILD_ROOT%{_bindir}/togit
install -p tohg.rb $RPM_BUILD_ROOT%{_bindir}/tohg
install -p todb.rb $RPM_BUILD_ROOT%{_bindir}/todb
cp -p fromcvs.rb tagexpander.rb $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/todb
%attr(755,root,root) %{_bindir}/togit
%attr(755,root,root) %{_bindir}/tohg
%{ruby_vendorlibdir}/fromcvs.rb
%{ruby_vendorlibdir}/tagexpander.rb
