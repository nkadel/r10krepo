%global gem_name ruby-progressbar

Name:           rubygem-%{gem_name}
Version:        1.10.1
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Ruby/ProgressBar is a flexible text progress bar library
License:        MIT

URL:            https://github.com/jfelchner/ruby-progressbar
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildArch:      noarch

%description
Ruby/ProgressBar is an extremely flexible text progress bar library for Ruby.
The output can be customized with a flexible formatting system including:
percentage, bars of various formats, elapsed time and estimated time
remaining.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%{gem_instdir}/Rakefile


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabio Valentini <decathorpe@gmail.com> - 1.10.1-1
- Update to version 1.10.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.10.0-1
- Update to version 1.10.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.9.0-1
- Initial package

