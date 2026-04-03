#!/usr/bin/env bash
# find-tools.sh -- sourced by other scripts to locate ffmpeg/ffprobe/jq
# Sets FFMPEG, FFPROBE, JQ variables

WINGET_PKG="/c/Users/giodl/AppData/Local/Microsoft/WinGet/Packages"

if [[ -z "${FFMPEG:-}" ]]; then
  if command -v ffmpeg &>/dev/null; then
    FFMPEG="ffmpeg"
  elif [[ -d "$WINGET_PKG" ]]; then
    FFMPEG="$(find "$WINGET_PKG" -name "ffmpeg.exe" -path "*/bin/*" 2>/dev/null | head -1)"
  fi
fi

if [[ -z "${FFPROBE:-}" ]]; then
  if command -v ffprobe &>/dev/null; then
    FFPROBE="ffprobe"
  elif [[ -n "${FFMPEG:-}" ]]; then
    FFPROBE="$(dirname "$FFMPEG")/ffprobe.exe"
  fi
fi

if [[ -z "${JQ:-}" ]]; then
  if command -v jq &>/dev/null; then
    JQ="jq"
  elif [[ -d "$WINGET_PKG" ]]; then
    JQ="$(find "$WINGET_PKG" -name "jq.exe" 2>/dev/null | head -1)"
  fi
fi

# Export for subprocesses
export FFMPEG="${FFMPEG:-}"
export FFPROBE="${FFPROBE:-}"
export JQ="${JQ:-jq}"

if [[ -z "$FFMPEG" ]]; then
  echo "ERROR: ffmpeg not found. Install with: winget install Gyan.FFmpeg" >&2
  exit 1
fi
