%global	gem_name	text

%if 0%{?fedora} >= 21 || 0%{?rhel} > 7
%global	gem_minitest	rubygem(minitest4)
%else
%global	gem_minitest	rubygem(minitest)
%endif

Name:		rubygem-%{gem_name}
Version:	1.3.1
#Release:	8%%{?dist}
Release:	0%{?dist}
Summary:	Collection of text algorithms

License:	MIT
URL:		http://github.com/threedaymonk/text
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# Check
BuildRequires:	%gem_minitest
%if 0%{?fedora} >= 22
BuildRequires:	rubygem(test-unit)
%endif
Requires:	ruby(release)
Requires:	ruby(rubygems)

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
A collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Figlet, Porter Stemming


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack -V %{SOURCE0}
cd %{gem_name}-%{version}

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Disable for RHEL 7
#%check
#pushd .%{gem_instdir}
#ruby -Ilib:test:. -e 'gem "minitest", "<5" ; Dir.glob("test/*_test.rb").each{|f| require f}'
#popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/README.rdoc
%license	%{gem_instdir}/COPYING.txt

%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/test/

%changelog
* Sat Jun 1 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.3.1-0
- Disable check for RHEL 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1

* Fri Jun 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-4
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-2
- Include license text

* Wed Aug 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Aug 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- Initial package
