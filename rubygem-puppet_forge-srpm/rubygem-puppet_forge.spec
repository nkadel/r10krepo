%global gem_name puppet_forge

Name: rubygem-%{gem_name}
Version: 2.2.9
Release: 0%{?dist}
Summary: Access and manipulate the Puppet Forge API from Ruby.
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://rubygems.org/gems/%{gem_name}
Source0:http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)
Requires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}-%{release}

%description
# Puppet Forge
Access and manipulate the [Puppet Forge API](https://forgeapi.puppetlabs.com)
from Ruby.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c  -T
%gem_install -n %{SOURCE0}


%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


#%check
#pushd .%{gem_instdir}
#rspec spec
#popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/locales
%{gem_instdir}/spec
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/MAINTAINERS
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Sun Jun 2 2019 Nico Kadel-Garcia <nkadel@gmai..com> - 2.2.9-0
- Create initial setup
