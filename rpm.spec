%define release %(/bin/date +"%Y%m%d.%H%M")

Name:    lua-resty-hmac
Version: 0.03
Release: 1%{?dist}
Summary: HMAC functions for ngx_lua and LuaJIT
License: BSD
Source0: %{name}.tar.gz
Group:   Openresty/Lua
URL:     https://github.com/Mjolkhare/lua-resty-hmac

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: lua-resty-string >= 0.12

%description
 HMAC functions for ngx_lua and LuaJIT

%if %{?GBRANCH:1}%{!?GBRANCH:0} && %{?GCOMMIT:1}%{!?GCOMMIT:0}
It was built from repo: %{url}
Branch: %{GBRANCH}
Commit: %{GCOMMIT}
%endif

%prep
%setup -q -n %{name}

%install
install -d -m 0755 %{buildroot}/usr/share/lua/5.1/nginx/resty
cp -aR resty/*.lua %{buildroot}/usr/share/lua/5.1/nginx/resty

%files
%dir /usr/share/lua/5.1/nginx/resty
/usr/share/lua/5.1/nginx/resty/*.lua

%changelog
