%global gem_name activesupport

Name: rubygem-%{gem_name}
Epoch: 1
Version: 6.0.2.1
Release: 0%{?dist}
Summary: A support libraries and Ruby core extensions extracted from the Rails framework
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem


# ruby package has just soft dependency on rubygem({bigdecimal,json}), while
# ActiveSupport always requires them.
Requires: rubygem(bigdecimal)
Requires: rubygem(json)

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(builder)
# Reset theset do *runtime*, not buildtime!!!
Requires: rubygem(concurrent-ruby) >= 1.0
Requires: rubygem(connection_pool)
Requires: rubygem(dalli)
Requires: (rubygem(i18n) >= 0.7 with rubygem(i18n) < 2)
Requires: rubygem(minitest) >= 5.1
Requires: rubygem(rack)
Requires: rubygem(tzinfo) >= 1.1
Requires: rubygem(listen)
Requires: rubygem(redis)
Requires: memcached
BuildArch: noarch


%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

#%check
# *FORGET CHECKS until this can be ported to something sane!!!

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

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.3-1
- Update to Active Support 5.2.3.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2.1-1
- Update to Active Support 5.2.2.1.

* Mon Feb 04 2019 Vít Ondruch <vondruch@redhat.com> - 1:5.2.2-3
- Fix Range and BigDecimal compatibility with Ruby 2.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-1
- Update to Active Support 5.2.2.

* Wed Nov 14 2018 Vít Ondruch <vondruch@redhat.com> - 1:5.2.1-2
- Update I18n fallbacks configuration to be compatible with i18n 1.1.0.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-1
- Update to Active Support 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-1
- Update to Active Support 5.2.0.

* Mon Apr 16 2018 Vít Ondruch <vondruch@redhat.com> - 1:5.1.5-3
- Fix test suite issue caused by fix of CVE-2018-6914 in Ruby.

* Wed Feb 21 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-2
- Allow rubygem-i18n ~> 1.0
  https://github.com/rails/rails/pull/31991

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-1
- Update to Active Support 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Vít Ondruch <vondruch@redhat.com> - 1:5.1.4-2
- Fix MiniTest 5.11 compatibility.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-1
- Update to Active Support 5.1.4.

* Tue Aug 22 2017 Vít Ondruch <vondruch@redhat.com> - 1:5.1.3-2
- Explicitly require rubygem(json).
- Once again disable unstable test.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-1
- Update to Active Support 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-1
- Update to Active Support 5.1.2.
- Run tests that need memcached

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-1
- Update to Active Support 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-1
- Update to Active Support 5.0.2.

* Mon Feb 13 2017 Jun Aruga <jaruga@redhat.com> - 1:5.0.1-4
- Fix Fixnum/Bignum deprecated warning for Ruby 2.4.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jun Aruga <jaruga@redhat.com> - 1:5.0.1-2
- Fix Ruby 2.4.0 compatibility.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-1
- Update to Active Support 5.0.1.
  - Remove Patch0: rubygem-activesupport-5.0.0-Do-not-depend-on-Rails-git-repository-layout-in-Acti.patch; subsumed
- Fix warnings: Fixnum and Bignum are deprecated in Ruby trunk

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-1
- Update to Activesupport 5.0.0.1

* Wed Jul 27 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-2
- Fix missing epoch in -doc subpackage.

* Fri Jul 01 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActiveSupport 5.0.0.

* Fri Apr 08 2016 Vít Ondruch <vondruch@redhat.com> - 1:4.2.6-2
- Explicitly set rubygem(bigdecimal) dependency.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-1
- Update to activesupport 4.2.6

* Tue Mar 01 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-1
- Update to activesupport 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-1
- Update to activesupport 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-1
- Update to activesupport 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-1
- Update to activesupport 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-1
- Update to activesupport 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-1
- Update to activesupport 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-2
- Fix tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-1
- Update to activesupport 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-1
- Update to activesupport 4.2.0

* Tue Aug 19 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activesupport 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.4-1
- Update to ActiveSupport 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.1-1
- Update to ActiveSupport 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-1
- Update to ActiveSupport 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.3-1
- Update to ActiveSupport 4.0.3

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActiveSupport 4.0.2

* Fri Aug 09 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActiveSupport 4.0.1

* Fri Aug 09 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Fix: add minitest to requires

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActiveSupport 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to ActiveSupport 3.2.13.

* Fri Mar 01 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to ActiveSupport 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to ActiveSupport 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to ActiveSupport 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to ActiveSupport 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to ActiveSupport 3.2.7.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Update to ActiveSupport 3.2.6.
- Removed unneeded BuildRoot tag.
- Tests no longer fail with newer versions of Mocha, remove workaround.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveSupport 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveSupport 3.0.13.

* Wed Apr 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-5
- Add the bigdecimal dependency to gemspec.

* Fri Mar 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-4
- The CVE patch name now contains the CVE id.

* Mon Mar 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-3
- Patch for CVE-2012-1098

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActiveSupport 3.0.11.

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveSupport 3.0.10

* Fri Jul 01 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveSupport 3.0.9
- Changed %%define into %%global
- Removed unnecessary %%clean section

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-3
- Reverting accidental change adding a few gem flags

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-2
- Include fix for CVE-2011-2197

* Thu Mar 24 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Update to ActiveSupport 3.0.5
- Remove Rake dependnecy

* Mon Feb 14 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-4
- fix bad dates in the spec changelog

* Thu Feb 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-3
- include i18n runtime dependency

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- update to rails 3

* Wed Aug 25 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- bumped version

* Wed Aug 04 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8
- Added check section with rubygem-mocha dependency
- Added upsteam Rakefile and test suite to run tests

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Mon Sep 7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4 (bug 520843, CVE-2009-3009)

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.2.2-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Wed Nov 28 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-3
- Fix buildroot

* Tue Nov 13 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-2
- Install README and CHANGELOG in _docdir

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.4.4-1
- Initial package
