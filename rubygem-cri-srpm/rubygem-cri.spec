%global gem_name cri

Name: rubygem-%{gem_name}
Version: 2.15.7
Release: 0%{?dist}
Summary: Puppet environment and module deployment
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://rubygems.org/gems/cri
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby(rubygems)

Requires:	rubygem(colored) = 1.2
Requires:	rubygem(cri) >= 2.15.1
Requires:	rubygem(cri) < 2.16
Requires:	rubygem(gettext-setup) >= 0.24
Requires:	rubygem(gettext-setup) < 1
Requires:	rubygem(log4r) = 1.1.10
Requires:	rubygem(multi_json) >= 1.10
Requires:	rubygem(multi_json) < 2
Requires:	rubygem(puppet_forge) >= 2.2
Requires:	rubygem(puppet_forge) < 2.3

BuildArch: noarch

%description
Cri provides a general purpose toolset for deploying Puppet environments and
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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_cache}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/test
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/NEWS.md
%doc %{gem_instdir}/README.md

%changelog
