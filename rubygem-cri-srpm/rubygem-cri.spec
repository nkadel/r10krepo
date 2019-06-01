%global gem_name cri

Name: rubygem-%{gem_name}
Version: 2.15.7
Release: 0%{?dist}
Summary: Colorize ruby gems
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://rubygems.org/gems/cri
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby(rubygems)

BuildArch: noarch

%description
>> puts "this is red".red
>> puts "this is red with a blue background (read: ugly_".red_on_blue
>> puts "this is red with an underline".red.underline
>> puts "this is really bold and really blue".bold.blue
>> logger.debug "this is really broken!".red_on_yellow    # in rails
>> puts color.red "This is red" # but this part is mostly untested

Windows users
  You will need the Win32 Console Ansi gem.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

Windows users
  You will need the Win32 Console Ansi gem.

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
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_cache}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/test
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/NEWS.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Jun 1 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 2.15.7-0
- Initial setup
