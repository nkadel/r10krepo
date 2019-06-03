# Generated from fast_gettext-0.5.13.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fast_gettext

Name: rubygem-%{gem_name}
Version: 1.2.0
#Release: 7%%{?dist}
Release: 0%{?dist}
Summary: A simple, fast, memory-efficient and threadsafe implementation of GetText
# fast_gettext is MIT. However the files in lib/vendor directory
# are LGPL, BSD or Ruby licensed.
# https://github.com/grosser/fast_gettext/issues/50
License: MIT and (BSD or Ruby) and (LGPLv2+ or BSD or Ruby)
URL: https://github.com/grosser/fast_gettext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/grosser/fast_gettext.git && cd fast_gettext
# git checkout v1.2.0 && tar czvf fast_gettext-1.2.0-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}-%{release}

%description
A simple, fast, memory-efficient and threadsafe implementation of GetText.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

chmod a+x %{buildroot}%{gem_libdir}/fast_gettext/vendor/string.rb


%check
pushd .%{gem_instdir}

tar xzf %{SOURCE1}

# Do not use bundler, since it tries to install unnecessary gems.
sed -i -e 's/bundle exec //' spec/fast_gettext/vendor/iconv_spec.rb
sed -i -e 's/bundle exec //' spec/fast_gettext/vendor/string_spec.rb

LANG=C.UTF-8 rspec spec

popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/Readme.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-6
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Vít Ondruch <vondruch@redhat.com> - 1.2.0-1
- Update to fast_gettext 1.2.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Vít Ondruch <vondruch@redhat.com> - 0.9.2-1
- Update to fast_gettext 0.9.2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 0.8.1-1
- Update to fast_gettext 0.8.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.1-1
- Update to fast_gettext 0.7.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to fast_gettext 0.7.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.1-1
- Update to fast_gettext 6.1.

* Mon Aug 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.13-1
- Initial package
