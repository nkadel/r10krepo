# Generated from addressable-2.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name addressable

Name: rubygem-%{gem_name}
Version: 2.5.2
Release: 5%{?dist}
Summary: URI Implementation
License: ASL 2.0
URL: https://github.com/sporkmonger/addressable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(public_suffix)
BuildRequires: rubygem(rspec-its)
BuildRequires: rubygem(idn)
#BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(launchy)
#BuildRequires: rubygem(json_pure)
#BuildRequires: rubygem(yard)
#BuildRequires: rubygem(simplecov)
#BuildRequires: rubygem(bundler)
#BuildRequires: rubygem(rspec-core)
BuildArch: noarch
Patch0: no-rack-mount.patch
Patch1: fix_addressable_tests.patch

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for URI and URL templates.

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

# Revert f1d5855162c48d06eb1907871909d5859b9a7d3c (rack-mount)
%patch0
# Comment out failing tests
%patch1

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

%check
pushd .%{gem_instdir}
# Manually revert f1d5855162c48d06eb1907871909d5859b9a7d3c
rm spec/addressable/rack_mount_compat_spec.rb

# Drop Bundler dependency.
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb

# We don't care about code coverage.
sed -i '/^begin$/,/^end$/ s/^/#/' spec/spec_helper.rb

# Remove tests failing because of missing internet connection
rm spec/addressable/net_http_compat_spec.rb

rspec spec/
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Shawn Starr <shawn.starr@fedoraproject.org> - 2.5.2-1
- Spec changes from František Zatloukal <fzatlouk@redhat.com>
- New upstream release
- Add BuildRequires: rubygem(idn)
- Drop a lot of Build dependencies, kudos to vondruch@redhat.com
- Fix test fails in mock
- Comment out failing tests
- Add BuildRequires: rubygem(bundler)
- Switched rspec-its to rspec-core
- Re-Enable testing suite
- add no-rack-mount.patch to fix tests
- Regenerate spec with gem2rpm

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Shawn Starr <spstarr@fedoraproject.org> - 2.3.8-1
- New upstream release, fix some build changes

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.6-5
- Fix it harder

* Wed Apr 23 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.6-4
- Disable test 'Addressable::URI when parsed from 'http://example.com' should have a
  different hash from http://EXAMPLE.com' fails on koji but not in mock

* Wed Apr 23 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.6-3
- Disable GNU idn ruby bindings fallback to pure, rubygem-idn is dead upstream

* Wed Apr 23 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.6-2
- minor build issue..

* Wed Apr 23 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.6-1
- New upstream release

* Fri Feb 07 2014 Shawn Starr <shawn.starr@rogers.com> - 2.3.5-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Josef Stribny <jstribny@redhat.com> - 2.3.2-5
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 19 2013 Shawn Starr <shawn.starr@rogers.com> - 2.3.2-4
- Changes in rubygem rspec packaging, adjust build dependencies accordingly

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Shawn Starr <shawn.starr@rogers.com> - 2.3.2-2
- Fix build issue disable one test due to DNS lookup not available on koji mock builders

* Thu Aug 23 2012 Shawn Starr <shawn.starr@rogers.com> - 2.3.2-1
- Bump to latest upstream
- Fix spec test due to namespace/classname conflict

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Shawn Starr <shawn.starr@rogers.com> - 2.2.6-3
- Remove patch passes all tests now.

* Sun Nov 06 2011 Shawn Starr <shawn.starr@rogers.com> - 2.2.6-2
- Fix up package from bugzilla reviews

* Tue Jul 19 2011 Shawn Starr <shawn.starr@rogers.com> - 2.2.6-1
- Bump to latest upstream
- Overhall spec, split -doc packaging 
- Fix loader path to idn.so extension

* Thu Apr 01 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 2.1.1-1
- Initial package
