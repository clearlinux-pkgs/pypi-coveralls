#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-coveralls
Version  : 3.3.1
Release  : 14
URL      : https://files.pythonhosted.org/packages/c2/c5/6b8254092117fa366b022fbee9434224483ba38e0bbf36e80836bf10692a/coveralls-3.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c2/c5/6b8254092117fa366b022fbee9434224483ba38e0bbf36e80836bf10692a/coveralls-3.3.1.tar.gz
Summary  : Show coverage stats online via coveralls.io
Group    : Development/Tools
License  : MIT
Requires: pypi-coveralls-bin = %{version}-%{release}
Requires: pypi-coveralls-license = %{version}-%{release}
Requires: pypi-coveralls-python = %{version}-%{release}
Requires: pypi-coveralls-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(docopt)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Coveralls for Python
====================
:Test Status:
.. image:: https://img.shields.io/circleci/project/github/TheKevJames/coveralls-python/master.svg?style=flat-square&label=CircleCI
:target: https://circleci.com/gh/TheKevJames/coveralls-python

%package bin
Summary: bin components for the pypi-coveralls package.
Group: Binaries
Requires: pypi-coveralls-license = %{version}-%{release}

%description bin
bin components for the pypi-coveralls package.


%package license
Summary: license components for the pypi-coveralls package.
Group: Default

%description license
license components for the pypi-coveralls package.


%package python
Summary: python components for the pypi-coveralls package.
Group: Default
Requires: pypi-coveralls-python3 = %{version}-%{release}

%description python
python components for the pypi-coveralls package.


%package python3
Summary: python3 components for the pypi-coveralls package.
Group: Default
Requires: python3-core
Provides: pypi(coveralls)
Requires: pypi(coverage)
Requires: pypi(docopt)
Requires: pypi(requests)

%description python3
python3 components for the pypi-coveralls package.


%prep
%setup -q -n coveralls-3.3.1
cd %{_builddir}/coveralls-3.3.1
pushd ..
cp -a coveralls-3.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672265296
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . coverage
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . coverage
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-coveralls
cp %{_builddir}/coveralls-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-coveralls/75628b5484e52ada20d833093ea3980fe24c5fc4 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} coverage
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coveralls

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-coveralls/75628b5484e52ada20d833093ea3980fe24c5fc4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
