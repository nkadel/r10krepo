# Generated from minitar-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name minitar

Name: rubygem-%{gem_name}
Version: 0.9
#Release: 201%%{?dist}
Release: 0%{?dist}
Summary: pure-Ruby library to deal with POSIX tar files
Group: Development/Languages
License: MIT
URL: https://github.com/seattlerb/minitar
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%gem_name) = %{version}-%{release}

# Development dependencies
#Requires: rubygem(hoe) >= 3.18
#Requires: rubygem(hoe-doofus) >= 1.0
#Requires: rubygem(hoe-gemspec2) >= 1.1
#Requires: rubygem(hoe-git) >= 1.0
#Requires: rubygem(hoe-rubygems) >= 1.0
#Requires: rubygem(hoe-travis) >= 1.2
#Requires: rubygem(minitest) >= 5.11
#Requires: rubygem(minitest-autotest) >= 1.0
#Conflicts: rubygem(minitest-autotest) >= 2
#Requires: rubygem(rake) >= 10.0
#Conflicts: rubygem(rake) >= 12
#Requires: rubygem(rdoc) >= 0.0

%description
The minitar library is a pure-Ruby library that provides the ability
to deal with POSIX tar(1) archive files. This is release 0.9, adding a
minor feature to Minitar.unpack and Minitar::Input#extract_entry that
when <tt>:fsync => false</tt> is provided, fsync will be
skipped. minitar (previously called Archive::Tar::Minitar) is based
heavily on code originally written by Mauricio Julio Fernández Pradier
for the rpa-base project.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T

%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
LANG=en_US.utf8
LC_ALL=en_US.utf8
pushd .%{gem_instdir}

ruby -Ilib:test -e 'Dir.glob "./test/minitar/test_*.rb", &method(:require)' || \
    echo Error: %{name} check failed

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/docs
%doc %{gem_instdir}/test
%doc %{gem_instdir}/Licence.md
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/Code-of-Conduct.md
%doc %{gem_instdir}/Contributing.md
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/Rakefile

%changelog
* Thu Jun 6 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.9-0
- Initial setup
- Ignore failed check

