%global srcname p1_stun
# Erlang packages don't seem to ship debug files, as the build process does not generate them
%global debug_package %{nil}


Name: erlang-%{srcname}
Version: 1.0.7
Release: %mkrel 2
Group:   Development/Erlang
Summary: STUN and TURN library for Erlang / Elixir
# The license changed after 0.9.0 to ASL 2.0, and should be updated.
License: GPLv2
URL: https://github.com/processone/stun/
Source0: https://github.com/processone/stun/archive/%{version}.tar.gz

Requires: erlang-erts
Requires: erlang-p1_tls
Requires: erlang-p1_utils
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: erlang-p1_tls
BuildRequires: erlang-p1_utils


%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.


%prep
%autosetup -n stun-%{version}


%build
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/include

install -pm644 ebin/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin/
install -pm644 include/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/include/


%files
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.7-2.mga6
+ Revision: 1067866
- New version 1.0.7

* Fri May 06 2016 neoclust <neoclust> 0.9.0-2.mga6
+ Revision: 1009925
- imported package erlang-p1_stun

