# Generated from concurrent-ruby-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name concurrent-ruby

Name: rubygem-%{gem_name}
Version: 1.0.5
Release: 0%{?dist}
Summary: Modern concurrency tools for Ruby
License: MIT
URL: http://www.concurrent-ruby.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby-concurrency/concurrent-ruby.git && cd concurrent-ruby
# git checkout v1.0.5 && tar czvf concurrent-ruby-1.0.5-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
# Avoid sporadic test failures due to wrong object_id formatting.
# https://github.com/ruby-concurrency/concurrent-ruby/pull/651
Patch1: concurrent-ruby-1.0.5-fix-inspect-output.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(timecop)
BuildArch: noarch

%description
Modern concurrency tools including agents, futures, promises, thread pools,
actors, supervisors, and more.

Inspired by Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch1 -p1

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
tar xzf %{SOURCE1}

# -edge is not part of this gem.
sed -i '/require.*concurrent-edge/ s/^/#/' spec/spec_helper.rb

# We don't have the C extension. It would need to come from concurrent-ruby-ext
# and that would lead to cicrular dependency.
sed -i '/allow_c_extensions?/,/^      end/ s/^/#/' spec/concurrent/atomic/atomic_reference_spec.rb

# Exclude the -edge test cases.
rspec -rspec_helper \
  --exclude-pattern 'spec/concurrent/{actor_spec.rb,channel_spec.rb,lazy_register_spec.rb,channel/**/*,atomic/atomic_markable_reference_spec.rb,edge/**/*}' \
  spec

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Vít Ondruch <vondruch@redhat.com> - 1.0.5-1
- Update to Concurrent Ruby 1.0.5.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Vít Ondruch <vondruch@redhat.com> - 1.0.4-1
- Update to Concurrent Ruby 1.0.4.

* Mon Jul 04 2016 Vít Ondruch <vondruch@redhat.com> - 1.0.2-1
- Update to Concurrent Ruby 1.0.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Vít Ondruch <vondruch@redhat.com> - 1.0.0-1
- Initial package
