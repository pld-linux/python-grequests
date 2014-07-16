%define 	module	grequests
Summary:	gevent support for python-requests
Name:		python-%{module}
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/g/grequests/grequests-%{version}.tar.gz
# Source0-md5:	23186795cf69d127f5e90df665d25387
URL:		https://github.com/kennethreitz/grequests
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-requests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRequests allows you to use Requests with Gevent to make asyncronous
HTTP Requests easily.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build --build-base build-2 %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
