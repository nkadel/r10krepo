# Generated from r10k-3.9.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname r10k
%define version 3.9.1
%define release 0

Summary: Puppet environment and module deployment
Name: ruby-gems-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/puppetlabs/r10k
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby [">= 2.3.0"]
Requires: ruby-gems >= 2.0.14.1
Requires: ruby-gems-colored2 = 3.1.2
Requires: ruby-gems-cri = 2.15.10
Requires: ruby-gems-log4r = 1.1.10
Requires: ruby-gems-multi_json >= 1.10
Requires: ruby-gems-multi_json < 2
Requires: ruby-gems-puppet_forge >= 2.3.0
Requires: ruby-gems-puppet_forge < 2.4
Requires: ruby-gems-gettext-setup >= 0.24
Requires: ruby-gems-gettext-setup < 1
Requires: ruby-gems-fast_gettext >= 1.1.0
Requires: ruby-gems-fast_gettext < 1.2
Requires: ruby-gems-gettext >= 3.0.2
Requires: ruby-gems-gettext < 3.3.0
Requires: ruby-gems-rspec >= 3.1
Requires: ruby-gems-rspec < 4
Requires: ruby-gems-rake 
Requires: ruby-gems-yard >= 0.9.11
Requires: ruby-gems-yard < 0.10
Requires: ruby-gems-minitar >= 0.9.0
Requires: ruby-gems-minitar < 0.10
BuildRequires: ruby [">= 2.3.0"]
BuildRequires: ruby-gems >= 2.0.14.1
BuildArch: noarch
Provides: ruby(R10k) = %{version}

%define gemdir /home/nkadelgarcia/.gem/ruby
%define gembuilddir %{buildroot}%{gemdir}

%description
R10K provides a general purpose toolset for deploying Puppet environments
and modules.
It implements the Puppetfile format and provides a native implementation of
Puppet
dynamic environments.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/r10k
%{gemdir}/gems/r10k-3.9.1/
%{gemdir}/gems/r10k-3.9.1/path
%{gemdir}/gems/r10k-3.9.1/
%{gemdir}/gems/r10k-3.9.1/path
%{gemdir}/gems/r10k-3.9.1/
%{gemdir}/gems/r10k-3.9.1/path
%{gemdir}/gems/r10k-3.9.1/

%doc %{gemdir}/doc/r10k-3.9.1
%{gemdir}/cache/r10k-3.9.1.gem
%{gemdir}/specifications/r10k-3.9.1.gemspec

%changelog
