%global gem_name gettext-setup

Name: rubygem-%{gem_name}
Version: 0.30
Release: 0%{?dist}
Summary: Setup i18n for Ruby projects
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://rubygems.org/gems/gettext-setup
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby(rubygems)
# List generated Requires explicitly
Requires:	rubygem(gettext) >= 3.0.2
Requires:	rubygem(locale)

BuildArch: noarch

%description
This is a simple gem to set up i18n for Ruby projects (including [Sinatra](http://www.sinatrarb.com/) web apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a different locale in their browser preferences, and we support the user's preferred locale, strings and data formatting will be customized for that locale.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
This is a simple gem to set up i18n for Ruby projects (including [Sinatra](http://www.sinatrarb.com/) web apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a different locale in their browser preferences, and we support the user's preferred locale, strings and data formatting will be customized for that locale.

%prep
%setup -q -c  -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/spec
%{gem_instdir}/locales
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sat Jun 1 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.15.7-0
- Initial setup
