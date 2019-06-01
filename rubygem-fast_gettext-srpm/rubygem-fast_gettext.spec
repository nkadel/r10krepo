%global gem_name fast_gettext

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 0%{?dist}
Summary: A simple, fast, memory-efficient and threadsafe implementation of GetText
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://rubygems.org/gems/fast_gettext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby(rubygems)
# List generated Requires explicitly
Requires:	rubygem(locale)

BuildArch: noarch

%description
FastGettext
===========
GetText but 12 x faster, 530 x less garbage, clean namespace (8 vs 26), simple and threadsafe!

It supports multiple backends (.mo, .po, .yml files, Database(ActiveRecord + any other), Chain, Loggers) and can easily be extended.

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
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/Readme.md

%changelog
* Sat Jun 1 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.15.7-0
- Initial setup
