#!/usr/bin/env python
"""claude-run.py: Call claude --print via shell redirection, bypassing ARG_MAX limits.

Usage: python tools/claude-run.py <prompt_file> <output_file>

Uses bash shell redirection `claude --print < file > outfile` which works correctly
in relay subprocess contexts where Python subprocess stdin parameter may not behave
as expected (MSYS2/Windows detached process environment).
"""
import sys
import os
import subprocess

def main():
    if len(sys.argv) < 3:
        print("Usage: python claude-run.py <prompt_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    prompt_file = os.path.abspath(sys.argv[1])
    output_file = os.path.abspath(sys.argv[2])

    # Use bash shell redirection -- most reliable across subprocess environments
    # `claude --print < file > outfile` lets the shell handle stdin/stdout
    cmd = f'claude --print < "{prompt_file}" > "{output_file}"'
    result = subprocess.run(
        ['bash', '-c', cmd],
        capture_output=True,
        text=True,
        timeout=600,
        cwd=os.getcwd()
    )

    if result.returncode != 0 and (not os.path.exists(output_file) or os.path.getsize(output_file) == 0):
        sys.stderr.write(f"claude --print failed (exit {result.returncode})\n")
        sys.stderr.write(f"stderr: {result.stderr[:500]}\n")
        sys.exit(result.returncode or 1)

if __name__ == '__main__':
    main()
