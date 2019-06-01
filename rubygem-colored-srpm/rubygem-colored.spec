%global gem_name colored

Name: rubygem-%{gem_name}
Version: 1.2
Release: 0%{?dist}
Summary: color rubygem output
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://github.com/defunkt/colored
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby >= 2.3.0
Requires:	ruby(rubygems)
Requires:	rubygem(colored) = 1.2
Requires:	rubygem(cri) >= 2.15.1
Requires:	rubygem(cri) < 2.16
Requires:	rubygem(gettext-setup) >= 0.24
Requires:	rubygem(gettext-setup) < 1
Requires:	rubygem(log4r) = 1.1.10
Requires:	rubygem(multi_json) >= 1.10
Requires:	rubygem(multi_json) < 2
Requires:	rubygem(puppet_forge) >= 2.2
Requires:	rubygem(puppet_forge) < 2.3

BuildArch: noarch

%description
cute.

  >> puts "this is red".red
  >> puts "this is red with a blue background (read: ugly)".red_on_blue
  >> puts "this is red with an underline".red.underline
  >> puts "this is really bold and really blue".bold.blue
  >> logger.debug "hey this is broken!".red_on_yellow     # in rails
  >> puts Color.red "This is red" # but this part is mostly untested

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

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
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/test
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/README

%changelog
