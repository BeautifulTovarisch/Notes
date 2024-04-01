#!/bin/bash

set -euo pipefail

tex=$(buildah from scratch)
mnt=$(buildah mount $tex)

buildah config \
  --workingdir='/app' \
  $tex

dnf install -y --installroot $mnt \
  --release 39 \
  --setopt=install_weak_depts=False \
  tar \
  bash \
  coreutils \
  perl-core \
  poppler-utils \
  ghostscript

buildah copy $tex 'texlive.profile' '/app'

# Install TeXLive and packages
buildah run $tex bash -- <<-TEX
curl -L -o install-tl-unx.tar.gz https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar xvf install-tl-unx.tar.gz

cd /app/install-tl-2024*
perl ./install-tl --no-interaction -profile /app/texlive.profile

echo 'export PATH=$PATH:/usr/local/texlive/2024/bin/x86_64-linux' >> ~/.bashrc

# Install base packages
/usr/local/texlive/2024/bin/x86_64-linux/tlmgr install lwarp \
luatex \
fontspec \
float \
xindy \
pdfcrop \
ifptex \
etoolbox \
verifycommand \
xpatch \
catchfile \
newunicodechar \
upquote \
comment \
microtype \
xifthen \
newfloat \
xstring \
environ \
printlen \
cleveref \
ifmtarg \
capt-of \
filehook \
svn-prov \
pgf \
pgfplots \
amsmath \
standalone \
xcolor \
bibtex \
algorithms \
algorithmicx
TEX
