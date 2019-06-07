# Generated from connection_pool-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name connection_pool

Name: rubygem-%{gem_name}
Version: 2.2.0
#Release: 2%{?dist}
Release: 0.1%{?dist}
Summary: Generic connection pool for Ruby
Group: Development/Languages
License: MIT
URL: https://github.com/mperham/connection_pool
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Increase version number for RHEL
#BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest) > 5
BuildArch: noarch
Provides: rubygem(%gem_name) = %{version}-%{release}

%description
Generic connection pool for Ruby.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
  ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changes.md
%{gem_libdir}
%{gem_spec}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/connection_pool.gemspec
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Gemfile


%changelog
* Sat Dec 19 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.2.0-2
- trivial fixes in spec

* Tue Sep 29 2015 Ilya Gradina <ilya.gradina@gmail.com> - 2.2.0-1
- Initial package
