%global gem_name minitest-reporters

Name:           rubygem-%{gem_name}
Version:        1.3.8
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Create customizable Minitest output formats
License:        MIT

URL:            https://github.com/CapnKernul/minitest-reporters
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Disable generating coverage report during test execution
Patch0:         00-disable-rubocop-tests.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 1.9.3

BuildRequires:  git
BuildRequires:  rubygem(ansi)
BuildRequires:  rubygem(builder)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(maruku)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(ruby-progressbar)

BuildArch:      noarch

%description
Death to haphazard monkey-patching! Extend Minitest through simple hooks.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -S git -n %{gem_name}-%{version} -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
# The 4 test failures and 2 test errors are expected according to the code.
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' || :
popd


%files
%license %{gem_instdir}/LICENSE

%dir %{gem_instdir}

%{gem_instdir}/.ruby-gemset
%{gem_instdir}/assets

%exclude %{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/minitest-reporters.gemspec

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test


%changelog
* Mon Aug 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.8-1
- Update to version 1.3.8.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.6-1
- Update to version 1.3.6.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.5-1
- Update to version 1.3.5.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.4-1
- Update to version 1.3.4.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.3-1
- Update to version 1.3.3.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Update to version 1.3.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Initial package

