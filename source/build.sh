#!/bin/sh
# Rebuild the site from the server files and copy it to the repository root, which is what the web server serves.
# Usage: MIRACLE_SERVER=/path/to/Miracle-MMO ./build.sh   (defaults to ../../Miracle-MMO)
set -e
cd "$(dirname "$0")"
out=$(mktemp -d)
mkdocs build --strict --site-dir "$out"
cd ..
find . -mindepth 1 -maxdepth 1 ! -name ".*" ! -name source ! -name README.md -exec rm -rf {} +
cp -R "$out"/. .
rm -rf "$out"
