#
# Conditional build:
%bcond_without	doc             # don't build doc
%bcond_without	tests   # do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

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
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-gevent
Requires:	python-libs
Requires:	python-requests
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-gevent
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRequests allows you to use Requests with Gevent to make asyncronous
HTTP Requests easily.

%package -n python3-%{module}
Summary:	gevent support for python-requests
Group:		Libraries/Python
Requires:	python3-libs
Requires:	python3-requests

%description -n python3-%{module}
GRequests allows you to use Requests with Gevent to make asyncronous
HTTP Requests easily.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}*.py*
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
