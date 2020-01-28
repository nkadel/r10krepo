# Generated from zeitwerk-2.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name zeitwerk

Name: rubygem-%{gem_name}
Version: 2.2.1
Release: 1%{?dist}
Summary: Efficient and thread-safe constant autoloader
License: MIT
URL: https://github.com/fxn/zeitwerk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not included in packaged gem
# git clone https://github.com/fxn/zeitwerk.git --no-checkout
# cd zeitwerk && git archive -v -o zeitwerk-2.2.1-tests.txz v2.2.1 test
Source2: %{gem_name}-%{version}-tests.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-reporters)
BuildArch: noarch

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, preloading,
reloading, and eager loading.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b2

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# focus gem is not needed for tests
sed -i '/require..minitest.focus./ s/^/#/' test/test_helper.rb

ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Oct 16 2019 Pavel Valena <pvalena@redhat.com> - 2.2.1-1
- Update to zeitwerk 2.2.1.

* Tue Sep 24 2019 Pavel Valena <pvalena@redhat.com> - 2.1.10-1
- Initial package
