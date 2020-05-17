%global gem_name puppet_forge

Name: rubygem-%{gem_name}
Version: 2.3.1
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

Requires: rubygem(faraday) >= 0.9.0
Conflicts: rubygem(faraday) = 0.13.1
Conflicts: rubygem(faraday) >= 0.15.0
Requires: rubygem(faraday_middleware) >= 0.0.0
Conflicts: rubygem(faraday_middleware) >= 0.13.0
Requires: rubygem(gettext-setup) >= 0.11
Requires: rubygem(minitar) >= 0
Requires: rubygem(semantic_puppet) >= 1.0

# Development dependencies
#Requires: rubygem(cane) >= 0
#Requires: rubygem(pry-byebug) >= 0
#Requires: rubygem(rake) >= 0
#Requires: rubygem(rspec) >= 3.0
#Requires: rubygem(simplecov) >= 0
#Requires: rubygem(yard) >= 0

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
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/Rakefile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/locales
%{gem_instdir}/spec
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODEOWNERS
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md

%changelog
* Sun Jun 2 2019 Nico Kadel-Garcia <nkadel@gmai..com> - 2.2.9-0
- Create initial setup
