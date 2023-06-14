#!/bin/bash

set -e

install_from_git() {
    repo_url=$1
    repo_name=$2
    cmake_options=$3

    echo "Cloning and installing $repo_name from $repo_url"
    
    git clone $repo_url
    cd $repo_name
    mkdir build
    cd build
    if [ -z "$cmake_options" ]
    then
      cmake ..
    else
      cmake $cmake_options ..
    fi
    make
    sudo make install
    cd /app/installed
}

install_re2() {
    echo "Cloning and installing re2"
    
    git clone https://github.com/google/re2.git
    cd re2
    make
    make test
    sudo make install
    make testinstall
}

update_paths() {
    echo "Updating PKG_CONFIG_PATH and LD_LIBRARY_PATH"
    
    export PKG_CONFIG_PATH=/usr/local/lib64/pkgconfig:$PKG_CONFIG_PATH
    export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH
    cp -r /usr/local/lib64/pkgconfig/ /usr/local/lib/
}

install_python_packages() {
    echo "Installing python packages"
    
    sudo dnf install -y re2-devel
    pip install pybind11
    pip install google-re2
}

mkdir -p /app/installed

cd /app/installed

install_from_git "https://github.com/abseil/abseil-cpp.git" "abseil-cpp"
install_from_git "https://github.com/google/googletest.git" "googletest"
install_from_git "https://github.com/google/benchmark.git" "benchmark" "-DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON"
update_paths
install_re2
install_python_packages

echo "Cleaning up specific installation directories"
rm -rf /app/installed/abseil-cpp
rm -rf /app/installed/googletest
rm -rf /app/installed/benchmark
rm -rf /app/installed/re2
