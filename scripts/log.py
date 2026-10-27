#!/usr/bin/env python3
"""Contribution log generator.

Appends a timestamped entry to the daily contributions log.
Used by the local automation and the CI workflow.
"""
from __future__ import annotations

import datetime as dt
import pathlib
import sys

LOG = pathlib.Path(__file__).resolve().parent / "daily-contributions.txt"


def entry(now: dt.datetime | None = None) -> str:
    now = now or dt.datetime.now(dt.timezone.utc)
    return f"{now:%Y-%m-%d %H:%M:%S} UTC  contribution recorded"


def append(text: str, path: pathlib.Path = LOG) -> None:
    with path.open("a", encoding="utf-8") as fh:
        fh.write(text + "\n")


def main(argv: list[str]) -> int:
    text = entry()
    append(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
