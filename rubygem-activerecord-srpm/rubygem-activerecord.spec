# Generated from activerecord-1.15.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord

Name: rubygem-%{gem_name}
Epoch: 1
Version: 5.2.2
#Release: 4%%{?dist}
Release: 0%{?dist}
Summary: Object-relational mapper framework (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/rails/rails.git
# cd rails/activerecord/
# git checkout v5.2.2 && tar czvf activerecord-5.2.2-tests.tgz test/
Source1: activerecord-%{version}-tests.tgz

# Backport upstream patches for Ruby 2.6 compatibility
# https://github.com/rails/rails/pull/34858
# https://github.com/rails/rails/commit/6ea356e9781e7696c48a3f9fc3ecbb0ddda5f198
Patch0: rubygem-activerecord-5.2.2-fix-Ruby26-compatibility.patch
Patch1: rubygem-activerecord-5.2.2-fix-Ruby26-compatibility-tests.patch

# Database dump/load reuires the executable.
%if 0%{?fedora} > 0 || 0%{?rhel} > 7
Suggests: %{_bindir}/sqlite3
%endif
BuildRequires: rubygems-devel
BuildRequires: rubygem(bcrypt)
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activemodel)   = %{version}
BuildRequires: rubygem(builder)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(arel)
BuildRequires: rubygem(rack)
BuildRequires: %{_bindir}/sqlite3
BuildArch: noarch

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties database
tables and classes together for business objects, like Customer or
Subscription, that can find, save, and destroy themselves without resorting to
manual SQL.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p2

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

tar xzvf %{SOURCE1}

cat %{PATCH1} | patch -p2 -F 0

# Tests are broken on Fedora
# https://github.com/rails/rails/pull/34436
sed -i '/^\s*def test_too_many_binds$/ a skip' \
  test/cases/bind_parameter_test.rb
# https://github.com/rails/rails/issues/25774#issuecomment-445031789
sed -i '/^\s*def test_preloading_has_many_through_with_implicit_source$/ a skip' \
  test/cases/associations/eager_test.rb
sed -i '/^\s*def test_eager_habtm_with_association_inheritance$/ a skip' \
  test/cases/associations/eager_test.rb

ruby -Itest:lib <<EOF
  test_files = Dir.glob( "./test/cases/**/*_test.rb" )
  test_files.reject! { |x| x =~ %r|/adapters/| }

  # Only test sqlite3 backend
  test_files += Dir.glob("./test/cases/adapters/sqlite3/*_test.rb")

  test_files.sort.each { |f| require f }
EOF

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/examples

%changelog
* Thu Feb 07 2019 Vít Ondruch <vondruch@redhat.com> - 1:5.2.2-4
- Drop unnecessary erubis dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-2
- Fix Ruby 2.6 compatibility

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-1
- Update to Active Record 5.2.2.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-1
- Update to Active Record 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-1
- Update to Active Record 5.2.0.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-1
- Update to Active Record 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-1
- Update to Active Record 5.1.4.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-1
- Update to Active Record 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-1
- Update to Active Record 5.1.2.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-1
- Update to Active Record 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-1
- Update to Active Record 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Vít Ondruch <vondruch@redhat.com> - 1:5.0.1-2
- Fix unstable ReflectionTest#test_read_attribute_names test.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-1
- Update to Active Record 5.0.1.
- Fix warnings: Fixnum and Bignum are deprecated in Ruby trunk

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-1
- Update to Activerecord 5.0.0.1

* Thu Jul 07 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActiveRecord 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-1
- Update to activerecord 4.2.6

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-1
- Update to activerecord 4.2.5.2
- Add sqlite3 executable to BR

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-1
- Update to activerecord 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-1
- Update to activerecord 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-1
- Update to activerecord 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-1
- Update to activerecord 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-1
- Update to activerecord 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-1
- Update to activerecord 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-1
- Update to activerecord 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activerecord 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to activerecord 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.1-1
- Update to ActiveRecord 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Apr 11 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-1
- Update to ActiveRecord 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.3-1
- Update to ActiveRecord 4.0.3

* Wed Dec 11 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-2
- Enable tests
- Patch for new sqlite

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActiveRecord 4.0.2
- Disable tests

* Thu Nov 21 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-2
- Fix: this shouldn't be scl spec

* Mon Nov 11 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActiveRecord 4.0.1

* Fri Oct 04 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Convert to scl

* Thu Aug 01 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActiveRecord 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to ActiveRecord 3.2.13.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to ActiveRecord 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to ActiveRecord 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to ActiveRecord 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to ActiveRecord 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to ActiveRecord 3.2.7.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Thu Jul 19 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-1
- Update to ActiveRecord 3.2.6.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveRecord 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveRecord 3.0.13.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActionRecord 3.0.11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveRecord 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveRecord 3.0.9

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActiveRecord 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Wed Sep 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-4
- Updated postgres fix to resolve security issue

* Mon Aug 16 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-3
- Included postgres fix (patch also pushed upstream, see rails issue tracker)

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Updated patch0 to correctly parse sqlite3 version

* Wed Aug 04 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Fri Sep 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4
- Enable check

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.2.2-1
- New upstream version
- Fixed rpmlint errors zero-length files and script-without-shebang

* Thu Nov 20 2008 David Lutterkort <lutter@redhat.com> - 2.1.1-2
- Do not mark lib/ as doc

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.15.6-1
- New version

* Wed Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-2
- Fix buildroot
- Properly mark docs in geminstdir

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-1
- Initial package