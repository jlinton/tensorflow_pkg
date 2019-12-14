%global pypi_name tensorflow
%global debug_package %{nil}

Name:           tensorflow
Version:        2.0
Release:        2.0%{?dist}
Summary:        A framework used for deep learning


License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND FSFUL AND MIT AND MPL-2.0 AND OpenSSL AND Python-2.0
URL:            https://www.tensorflow.org/
Source0:        https://github.com/jlinton/tensorflow/archive/36ec840f8c5e504e4fe187bdb802918f621603d6.tar.gz
Patch0:         Config-tensorflow.patch
Patch1:         adding_python_bin_path.patch

BuildRequires:  python-devel
BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  python
BuildRequires:  gcc-c++
BuildRequires:  python3-six
BuildRequires:  python3-pip
BuildRequires:  bazel
#BuildRequires:  python3-keras-applications
#BuildRequires:  python3-keras-preprocessing
BuildRequires:  numpy
BuildRequires:  python3-numpy
#BuildRequires:  python-google-apputils
BuildRequires:  python3-google-apputils
BuildRequires:  protobuf
BuildRequires:  python3-protobuf
BuildRequires:  python2-enum34
#BuildRequires:  python2-astor
BuildRequires:  python3-termcolor
BuildRequires:  python3-werkzeug
BuildRequires:  python3-markdown
BuildRequires:  python3-setuptools
BuildRequires:  python2-backports
#BuildRequires:  python2-futures
#BuildRequires:  python2-absl-py


Provides:       python3-tensorflow
Provides:       python3-tensorflow-cpu

Requires:       numpy >= 1.16.1
Requires:       python3-pip
Requires:       python3-protobuf >= 3.6.1
#Requires:       python-enum34 >= 1.1.6
#Requires:       python3-astor >= 0.6.0
Requires:       python3-termcolor >= 1.1.0
Requires:       python3-werkzeug >= 0.11.15
Requires:       python3-markdown >= 2.6.8
#Requires:       python-backports
#Requires:       python3-futures
#Requires:       python3-absl-py
#Requires:       python3-keras-applications >= 1.0.6
#Requires:       python3-keras-preprocessing
Requires:       python3-gast >= 0.2


%description
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python-%{pypi_name}}
Provides:       python3-tensorflow
Provides:       python3-tensorflow-cpu

Requires:       numpy >= 1.16.1
Requires:       python3-pip
Requires:       python3-protobuf >= 3.6.1
#Requires:       python-enum34 >= 1.1.6
#Requires:       python3-astor >= 0.6.0
Requires:       python3-termcolor >= 1.1.0
Requires:       python3-werkzeug >= 0.11.15
Requires:       python3-markdown >= 2.6.8
#Requires:       python-backports
#Requires:       python3-futures
#Requires:       python3-absl-py
#Requires:       python3-keras-applications >= 1.0.6
#Requires:       python3-keras-preprocessing
Requires:       python3-gast >= 0.2

%description -n python3-%{pypi_name}
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.


%prep
%setup -n tensorflow-36ec840f8c5e504e4fe187bdb802918f621603d6
%patch0 -p0
%patch1 -p0


%build
yes | pip install --user --upgrade pip
yes | pip install --user wheel mock
sed -i "s/\/local\/lib64/\/lib64/g" .tf_configure.bazelrc 
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg



%install
pip install --root=%{buildroot} /tmp/tensorflow_pkg/tensorflow-%{version}.0-cp37-cp37m-linux_$(uname -m).whl
rm -rf %{buildroot}/usr/lib/python3.7/site-packages/gast-0.2.2.dist-info
rm -rf %{buildroot}/usr/lib/python3.7/site-packages/gast
rm -rf %{buildroot}/usr/lib64/python3.7/site-packages/grpc
rm -rf %{buildroot}/usr/lib64/python3.7/site-packages/grpcio-1.19.0.dist-info
rm -rf %{buildroot}/usr/lib/python3.7/site-packages/backports.weakref-1.0.post1.dist-info
rm -rf %{buildroot}/usr/lib/python3.7/site-packages/backports
mv %{buildroot}/%{python_sitearch}/%{pypi_name}-%{version}.0.dist-info %{buildroot}/%{python_sitelib}/%{pypi_name}-%{version}.dist-info



%files -n  python3-%{pypi_name}
#%{python_sitelib}/%{pypi_name}
%{python_sitelib}/tensorboard
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
%{python_sitelib}/tensorflow_estimator
%{python_sitelib}/tensorflow_estimator-2.0.1.dist-info
#%{_bindir}/freeze_graph
%{_bindir}/tensorboard
%{_bindir}/estimator_ckpt_converter
%{_bindir}/saved_model_cli
%{_bindir}/tf_upgrade_v2
%{_bindir}/tflite_convert
%{_bindir}/toco
%{_bindir}/toco_from_protos



%changelog

