#!/bin/sh
# Uploads the built site (the repository root) to the web host over FTP with lftp.
# The host keeps the commit it was last uploaded from in .deployed-commit. When that commit is known, only the
# files that changed since then are uploaded (and removed files are deleted); otherwise the whole site is
# mirrored with several parallel connections.
# Usage (from the repository root): FTP_SERVER=host FTP_USERNAME=user FTP_PASSWORD=secret \
#   FTP_DIR=domains/miracle-mmo.com/public_html/wiki FTP_PROTOCOL=ftp source/tools/deploy_ftp.sh
set -eu
: "${FTP_SERVER:?}" "${FTP_USERNAME:?}" "${FTP_PASSWORD:?}"
dir=${FTP_DIR:-domains/miracle-mmo.com/public_html/wiki}
dir=${dir%/}
case "${FTP_PROTOCOL:-ftp}" in
  ftps) ssl="set ftp:ssl-force true; set ftp:ssl-protect-data true" ;;
  *) ssl="set ftp:ssl-allow false" ;;
esac
export LFTP_PASSWORD="$FTP_PASSWORD"
head=$(git rev-parse HEAD)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

ftp() {
  lftp -c "set net:max-retries 8; set net:reconnect-interval-base 5; set net:timeout 30; $ssl
open --env-password -u \"$FTP_USERNAME\" \"$FTP_SERVER\"
$1"
}

# Files that belong to the site: everything tracked except the sources, workflows and git files.
site() { grep -vE '^(source/|\.github/|\.git|\.game-commit$|\.deployed-commit$)' || true; }

old=$(ftp "cat \"$dir/.deployed-commit\"" 2>/dev/null | tr -d '[:space:]' || true)
if [ -n "$old" ] && git cat-file -e "$old^{commit}" 2>/dev/null || { [ -n "$old" ] && git fetch -q --depth=1 origin "$old" 2>/dev/null; }; then
  echo "Host has $old; uploading changes up to $head"
  {
    echo "cd \"$dir\""
    git diff --name-only --no-renames --diff-filter=D "$old" HEAD | site | while read -r f; do
      echo "rm -f \"$f\""
    done
    git diff --name-only --no-renames --diff-filter=ACMRT "$old" HEAD | site | while read -r f; do
      d=$(dirname "$f")
      [ "$d" = . ] && echo "put \"$f\"" || echo "mkdir -pf \"$d\"; put -O \"$d\" \"$f\""
    done
  } > "$tmp/script"
  echo "$(grep -c '^put\|; put' "$tmp/script" || true) files to upload, $(grep -c '^rm' "$tmp/script" || true) to delete"
  ftp "source \"$tmp/script\""
else
  echo "The host has no known upload commit; uploading the whole site"
  ftp "mkdir -pf \"$dir\"; mirror -R --parallel=8 --no-perms --verbose=1 \
-x '^\\.git' -x '^source/' -x '^\\.game-commit\$' -x '^\\.deployed-commit\$' . \"$dir\""
fi

echo "$head" > "$tmp/.deployed-commit"
ftp "put -O \"$dir\" \"$tmp/.deployed-commit\""
echo "Uploaded $head"
