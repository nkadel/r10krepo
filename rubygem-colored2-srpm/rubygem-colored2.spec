%global gem_name colored2

Name: rubygem-%{gem_name}
Version: 3.1.2
Release: 0%{?dist}
Summary: color rubygem output
Group: Development/Languages
License: GPLv2+ or Artistic or MIT
URL: https://github.com/defunkt/colored2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)

Requires:	ruby >= 2.3.0
Requires:	ruby(rubygems)

# Development dependencies
#Requires:  rubytems(rake) >= 10.0
#Requires:  rubytems(rspec) >= 3.4
#Requires:  rubytems(codeclimate-test-reporter) >= 0

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}-%{release}

%description
This is a heavily modified fork of http://github.com/defunkt/colored
gem, with many sensible pull requests combined. Since the authors of
the original gem no longer support it, this might, perhaps, be
considered a good alternative. Simple gem that adds various color
methods to String class, and can be used as follows: require
'colored2' puts 'this is red'.red puts 'this is red with a yellow
background'.red.on.yellow puts 'this is red with and
italic'.red.italic puts 'this is green bold'.green.bold << ' and
regular'.green puts 'this is really bold blue on white but
reversed'.bold.blue.on.white.reversed puts 'this is regular, but
'.red! << 'this is red '.yellow! << ' and yellow.'.no_color! puts
('this is regular, but '.red! do 'this is red '.yellow! do ' and
yellow.'.no_color! end end)

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
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/README.md
%{gem_instdir}/LICENSE
%{gem_instdir}/spec

%changelog
