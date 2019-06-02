# Generated from multi_json-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_json


Summary: A gem to provide swappable JSON backends
Name: rubygem-%{gem_name}
Version: 1.7.1
#Release: 1%%{?dist}
Release: 0%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/multi_json
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(json)
BuildRequires: rubygem(json_pure)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# OkJson is allowed to be bundled:
# https://fedorahosted.org/fpc/ticket/113
Provides: bundled(okjson) = 20110719

%description
A gem to provide swappable JSON backends utilizing Yajl::Ruby, the JSON gem,
JSON pure, or a vendored version of okjson.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# simplecov gem is not available in Fedora so remove its usage
sed -i '1,+8 s/^/#/' spec/helper.rb

# oj is not available on Fedora.
sed -i '123,131 s/^/#/' spec/multi_json_spec.rb
sed -i '49,57 s/^/#/' spec/multi_json_spec.rb
sed -i 's/ oj / /' spec/multi_json_spec.rb

# ruby-yajl is not available on Fedora yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=823351
sed -i 's/ yajl//' spec/multi_json_spec.rb

# Prevents "invalid byte sequence in US-ASCII" testsuite error.
# https://github.com/intridea/multi_json/issues/104
LANG=en_US.utf8 rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec


%changelog
* Wed Mar 20 2013 Vít Ondruch <vondruch@redhat.com> - 1.7.1-1
- Update to multi_json 1.7.1.

* Tue Feb 26 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.6-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.6-1
- Update to multi_json 1.3.6.
- Switch to rubygem(rspec) from rubygem(rspec-core).

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.3-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-3
- Removed useless shebang.

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-2
- Review fixes.

* Fri Jul 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-1
- Initial package
