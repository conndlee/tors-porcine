#!/usr/bin/env bash
# Build the LaTeX PDF and Word manuscript from the same sources.
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"

# Explicit environment variables and make arguments take priority.
has_override() {
    local name="$1"
    shift
    [[ -n "${!name:-}" ]] && return 0
    local argument
    for argument in "$@"; do
        [[ "$argument" == "$name="* ]] && return 0
    done
    return 1
}

# Reuse the existing local toolchain when no system installation is available.
if ! has_override TECTONIC "$@" && ! command -v tectonic >/dev/null 2>&1; then
    if [[ ! -x /tmp/tors-latex/bin/tectonic ]]; then
        printf 'Missing Tectonic. Install it or pass TECTONIC=/path/to/tectonic.\n' >&2
        exit 1
    fi
    export PATH="/tmp/tors-latex/bin:$PATH"
    export XDG_CACHE_HOME="${XDG_CACHE_HOME:-/tmp/tors-tex-cache}"
    export TECTONIC=tectonic
    if [[ -d /tmp/tors-tex-extras/biblatex-ieee-1.3c ]]; then
        export TECTONIC="tectonic -Z search-path=/tmp/tors-tex-extras/biblatex-ieee-1.3c"
    fi
    printf 'Using the local Tectonic toolchain in /tmp/tors-latex.\n'
fi

if ! command -v biber >/dev/null 2>&1 && [[ -x /tmp/tors-biber/biber ]]; then
    export PATH="/tmp/tors-biber:$PATH"
fi

if ! has_override PANDOC "$@" && ! command -v pandoc >/dev/null 2>&1; then
    for candidate in /tmp/pandoc-*/bin/pandoc; do
        if [[ -x "$candidate" ]]; then
            export PANDOC="$candidate"
            break
        fi
    done
    if [[ -z "${PANDOC:-}" ]]; then
        printf 'Missing Pandoc. Install it or pass PANDOC=/path/to/pandoc.\n' >&2
        exit 1
    fi
fi

make -C "$repo_root" all "$@"
