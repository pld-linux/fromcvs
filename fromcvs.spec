Summary:	Fast (incremental) CVS->* conversion
Name:		fromcvs
Version:	0.1
Release:	1
License:	GPL
Group:		Development
Source0:	http://ww2.fs.ei.tum.de/~corecode/hg/fromcvs/archive/tip.tar.bz2#/%{name}.tbz2
# Source0-md5:	65a791705a1f6a7b5fd718c1af76695e
URL:		http://ww2.fs.ei.tum.de/~corecode/hg/fromcvs/
Requires:	ruby >= 1.8.5
Requires:	ruby-rbtree
Requires:	ruby-rcsparse
Requires:	sqlite3-ruby
Suggests:	git-core >= 1.5
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Fromcvs is designed to sync to different target SCM; at the moment
there is a hg and git destination available.

%prep
%setup -qc
mv %{name}-*/* .

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
