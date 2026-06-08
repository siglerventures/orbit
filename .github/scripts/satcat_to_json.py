#!/usr/bin/env python3
"""Trim Celestrak SATCAT (CSV) to a compact NORAD-id -> {type, owner, launch} JSON.

Used by .github/workflows/update-tle.yml; the page loads data/satcat.json lazily
to enrich satellite info cards (object type, owner/country, launch date).
"""
import csv
import json
import sys


def main(src: str, dst: str) -> None:
    out = {}
    with open(src, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            nid = (row.get("NORAD_CAT_ID") or "").strip()
            if not nid:
                continue
            rec = {}
            owner = (row.get("OWNER") or "").strip()
            otype = (row.get("OBJECT_TYPE") or "").strip()
            launch = (row.get("LAUNCH_DATE") or "").strip()
            if otype:
                rec["t"] = otype
            if owner:
                rec["o"] = owner
            if launch:
                rec["l"] = launch
            if rec:
                out[nid] = rec
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print("satcat entries:", len(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
