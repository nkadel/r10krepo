%global gem_name r10k

Name: rubygem-%{gem_name}
Version: 3.2.0
Release: 0%{?dist}
Summary: Puppet environment and module deployment
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://github.com/halostatue/r10k
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby >= 2.3.0
Requires:	ruby(rubygems)
# Allow compilation to deduce Requires
#Requires:	rubygem(colored) = 1.2
#Requires:	rubygem(cri) >= 2.15.1
#Requires:	rubygem(cri) < 2.16
#Requires:	rubygem(gettext-setup) >= 0.24
#Requires:	rubygem(gettext-setup) < 1
#Requires:	rubygem(log4r) = 1.1.10
#Requires:	rubygem(multi_json) >= 1.10
#Requires:	rubygem(multi_json) < 2
#Requires:	rubygem(puppet_forge) >= 2.2
#Requires:	rubygem(puppet_forge) < 2.3

BuildArch: noarch

%description
R10k provides a general purpose toolset for deploying Puppet environments and
modules. It implements the [Puppetfile](doc/puppetfile.mkd) format and provides a native
implementation of Puppet [dynamic environments][workflow].

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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Fix shebangs.
sed -i 's|^#!.*|#!/usr/bin/ruby|' %{buildroot}%{gem_instdir}/bin/*

    # Disable chck until further notice
#%if ! 0%{?bootstrap}
#%check
#pushd .%{gem_instdir}
#rspec spec
#popd
#%endif

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_cache}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/azure-pipelines.yml
%{gem_instdir}/bin
%{gem_instdir}/locales
%{gem_instdir}/docker
%{gem_instdir}/integration
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/r10k.yaml.example
%doc %{gem_instdir}/CHANGELOG.mkd
%doc %{gem_instdir}/CONTRIBUTING.mkd
%doc %{gem_instdir}/MAINTAINERS
%doc %{gem_instdir}/README.mkd

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc/
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
