#!/bin/bash

set -euo pipefail

# This script automates the absurdly convoluted process of building a website
# out of LaTeX source using Lwarp. A container image with TeXLive installed is
# used to compile and build the site, which is then copied out of the container
# and placed in the docs/ directory as a tar archive.

texlive="/usr/local/texlive/2024/bin/x86_64-linux"

# Inside the TeXLive container with the source latex mounted, we perform all
# necessary compilation and archive the HTML and CSS as a tarball
podman run -i -v ./src:/app/src:z --name texbuild --env-merge PATH=${PATH},":$texlive" localhost/texlive-2024 \
bash -- <<-BUILD
  mkdir -p /app/dist
  cp -r /app/src/* /app/dist

  cd /app/dist

  lualatex index.tex
  lwarpmk print
  lwarpmk htmlindex
  lwarpmk html
  lwarpmk limages
  lwarpmk html

  # lwarpmk runs asynchronously for some reason, need to identify better fix
  sleep 2

  tar -cvf site.tar *.html *.css
  tar -r -f site.tar index-images
BUILD

# Remove the existing contents of the docs directory and replace with new site
# contents from the tarball.
rm -rf docs/*

podman cp texbuild:/app/dist/site.tar ./docs
podman rm texbuild

# In docs directory
cd ./docs/
tar -xvf site.tar

rm site.tar
