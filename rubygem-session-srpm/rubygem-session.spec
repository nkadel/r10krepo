%global gem_name session

Summary: Session drives external programs
Name: rubygem-%{gem_name}
Version: 3.1.0
Release: 0%{?dist}
Group: Development/Languages
License: Ruby
URL: http://github.com/ahoward/session/tree/master
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: session-3.1.0-syntax-1424392.patch
BuildRequires: ruby(release)
BuildRequires: ruby-irb
BuildRequires: rubygems-devel
BuildRequires: rubygem(test-unit)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}-%{release}

%description
Session offers a set of classes built upon Open3::popen3 for driving
external progams via pipes.  It offers a significant abstraction over
Open3::popen in that the stdout/stderr of each command sent can be 
deliniated

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}
%patch0 -p1

# Adjusting permissions
chmod 0664 .%{gem_libdir}/session.rb

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm  %{buildroot}%{gem_instdir}/Rakefile
rm  %{buildroot}%{gem_instdir}/gemspec.rb
rm  %{buildroot}%{gem_instdir}/session.gemspec

#%%check
#cd %%{buildroot}%%{gem_instdir}
#ruby -Ilib -e 'Dir.glob "./test/*.rb", &method(:require)'

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/sample
%doc %{gem_instdir}/test

%changelog
* Sat Jun 1 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 3.1.0-0
- Port to RHEL
- Disable check to allow compilation in realtime
- Add Provides line

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Karsten Hopp <karsten@redhat.com> - 3.1.0-15
- fix syntax (rhbz#1424392)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.1.0-12
- Fix %%check for latest ruby (#1308083)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.1.0-9
- Fixes for Ruby 2.1 packaging guidelines (#1107236)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-6
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 3.1.0-3
- irb added as build require

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 3.1.0-2
- Rebuilt for Ruby 1.9.3.

* Sun Jan 22 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 3.1.0-1
- Initial package
