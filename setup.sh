#! /bin/bash

set -e
if [[ $EUID -ne 0 ]]; then
    echo "This script requires superuser privileges"
    exit
fi

apt install python-pygments inkscape imagemagick
