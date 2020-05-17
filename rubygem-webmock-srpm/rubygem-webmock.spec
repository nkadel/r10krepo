# Generated from webmock-1.7.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webmock

Name: rubygem-%{gem_name}
Version: 3.5.1
#Release: 2%%{?dist}
Release: 0%{?dist}
Summary: Library for stubbing HTTP requests in Ruby
License: MIT
URL: http://github.com/bblimke/webmock
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby

BuildRequires: rubygem(addressable)
BuildRequires: rubygem(minitest)

# Runtime, not build time!!!!
Requires: rubygem(addressable)
Requires: rubygem(crack)
Requires: rubygem(hashdiff)
Requires: rubygem(minitest)

# Development dependencies
#Requires: rubygem(curb)
#Requires: rubygem(excon)
#Requires: rubygem(httpclient)
#Requires: rubygem(rack)
#Requires: rubygem(rspec)
#Requires: rubygem(test-unit)
#Requires: rubygem(typhoeus)
BuildArch: noarch

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

sed -i '/^#!\/usr\/bin\/env\ rake/ d' Rakefile
chmod -x Rakefile

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Disalbe the checks for now
#%check
#pushd .%{gem_instdir}
#ruby -e 'Dir.glob "./minitest/**/*.rb", &method(:require)'
#ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
#
## rubygem-{patron,em-http-request,http} are not in Fedora yet.
#sed -i '/patron/ s/^/#/' spec/spec_helper.rb
#sed -i '/em-http/ s/^/#/' spec/spec_helper.rb
#
## and we don't care about code quality, that's upstream business.
#rspec spec --exclude-pattern 'spec/{quality_spec.rb,acceptance/{patron,http_rb,em_http_request}/*}'
#
#popd
#%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/minitest
%{gem_instdir}/spec
%{gem_instdir}/test
%{gem_instdir}/webmock.gemspec

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Pavel Valena <pvalena@redhat.com> - 3.5.1-1
- Update to WebMock 3.5.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.3.2-1
- Updated to webmock 2.3.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Vít Ondruch <vondruch@redhat.com> - 1.21.0-1
- Updated to webmock 1.21.0.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Mo Morsi <mmorsi@redhat.com> - 1.17.1-1
- Update to version 1.17.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.9.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.9.0-1
- Updated to webmock 1.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.8.7-1
- Updated to webmock 1.8.7.

* Mon Feb 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.7.10-1
- Update to latest upstream release
- Build against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 03 2011 Mo Morsi <mmorsi@redhat.com> - 1.7.6-2
- Update to conform to guidelines

* Wed Sep 28 2011 Mo Morsi <mmorsi@redhat.com> - 1.7.6-1
- Initial package
