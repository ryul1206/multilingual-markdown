#!/usr/bin/env python3
"""Pre-commit hook to run mmg validation on matched files."""

import subprocess
import sys


def main():
    """Run mmg validation on files passed by pre-commit."""
    # Get all file arguments
    files = sys.argv[1:] if len(sys.argv) > 1 else []

    if not files:
        print("No files to validate.")
        sys.exit(0)

    # Run mmg validation
    cmd = ["uv", "run", "mmg", "--validation-only"] + files

    try:
        result = subprocess.run(cmd, check=False)
        sys.exit(result.returncode)
    except FileNotFoundError:
        print("Error: 'uv' command not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
