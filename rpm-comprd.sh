#!/bin/sh
set -x

#
# Copyright (c) 2011-2012 David Bigagli
#

major="2"
minor="0"

rpmbuild=/home/unix/neilw/rpmbuild

echo "Archving source code..."
git archive --format=tar --prefix="openlava-broad-comprd-${major}.${minor}/" HEAD \
   | gzip > $rpmbuild/SOURCES/openlava-broad-comprd-${major}.${minor}.tar.gz
cp spec/openlava.spec $rpmbuild/SPECS/openlava.spec

echo "RPM building..."
rpmbuild -ba --target x86_64 $rpmbuild/SPECS/openlava.spec
if [ "$?" != 0 ]; then
  echo "Failed buidling rpm"
  exit 1
fi
