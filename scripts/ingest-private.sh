#!/bin/bash
# Can be scheduled locally; Miniflux credentials and private data stay local.
set -euo pipefail
umask 077
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec 9>"${XDG_RUNTIME_DIR:-/tmp}/future-ingest-${UID}.lock"
flock -n 9 || exit 0
python3 "$script_dir/ingestion.py" miniflux --days 7 "$@"
