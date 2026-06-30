#!/usr/bin/env python3
"""cohort_churn.py — Month-over-Month cohort retention heatmap from a subscription export.

Reads a CSV of subscriptions and builds a classic MoM retention heatmap (cohort = signup month,
columns = months since signup). Then classifies whether churn is EARLY (onboarding problem) or
LATE (long-term utility problem). Standard library only.

CSV columns (header required): customer_id, signup_date, churn_date
  - dates as YYYY-MM-DD or YYYY-MM
  - churn_date blank/empty = still active

Example:
  python3 cohort_churn.py --csv subs.csv
  python3 cohort_churn.py --csv subs.csv --max-offset 6 --json
"""
import argparse
import csv
import json
import sys
from datetime import datetime


def month_index(s):
    """Return an integer month index (year*12 + month-1) from 'YYYY-MM' or 'YYYY-MM-DD'."""
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            d = datetime.strptime(s, fmt)
            return d.year * 12 + (d.month - 1)
        except ValueError:
            continue
    raise ValueError(f"unrecognized date: {s!r}")


def label(idx):
    return f"{idx // 12:04d}-{idx % 12 + 1:02d}"


def load(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        required = {"customer_id", "signup_date"}
        if not required.issubset({(c or "").strip() for c in reader.fieldnames or []}):
            raise SystemExit(f"CSV must have headers: customer_id, signup_date, churn_date "
                             f"(got {reader.fieldnames})")
        for r in reader:
            su = month_index(r.get("signup_date"))
            if su is None:
                continue
            ch = month_index(r.get("churn_date"))
            rows.append((r.get("customer_id", "").strip(), su, ch))
    return rows


def build(rows, max_offset):
    if not rows:
        raise SystemExit("no usable rows in CSV")
    as_of = max(max(su, ch if ch is not None else su) for _, su, ch in rows)

    cohorts = {}  # signup_idx -> list of (su, ch)
    for _, su, ch in rows:
        cohorts.setdefault(su, []).append((su, ch))

    data = {"as_of": label(as_of), "cohorts": [], "max_offset": max_offset}
    # aggregate churn-by-offset to classify early vs late
    churn_at = {}   # offset -> churned count
    exposed_at = {}  # offset -> customers observed entering this offset

    for su in sorted(cohorts):
        members = cohorts[su]
        size = len(members)
        retention = []
        for m in range(max_offset + 1):
            if su + m > as_of:
                retention.append(None)  # future / unobserved
                continue
            active = 0
            for _, ch in members:
                if ch is None or ch > su + m:
                    active += 1
            retention.append(active / size if size else 0.0)
            # churn accounting between offset m-1 and m
            if m >= 1:
                churned_this_step = sum(
                    1 for _, ch in members if ch is not None and ch == su + m
                )
                churn_at[m] = churn_at.get(m, 0) + churned_this_step
                exposed_at[m] = exposed_at.get(m, 0) + size
        data["cohorts"].append({"cohort": label(su), "size": size, "retention": retention})

    # Early = offsets 1-2, Late = 3+. Compare churn rates.
    early_churn = sum(churn_at.get(m, 0) for m in (1, 2))
    early_exposed = sum(exposed_at.get(m, 0) for m in (1, 2)) or 1
    late_churn = sum(v for m, v in churn_at.items() if m >= 3)
    late_exposed = sum(v for m, v in exposed_at.items() if m >= 3) or 1
    early_rate = early_churn / early_exposed
    late_rate = late_churn / late_exposed
    if early_rate > late_rate * 1.3:
        verdict = "EARLY churn dominates → ONBOARDING problem (fix TTV / activation first)."
    elif late_rate > early_rate * 1.3:
        verdict = "LATE churn dominates → UTILITY problem (retention/value; expand the 'Aha')."
    else:
        verdict = "Churn is spread → mixed; fix onboarding AND long-term utility."
    data["early_churn_rate"] = round(early_rate, 4)
    data["late_churn_rate"] = round(late_rate, 4)
    data["verdict"] = verdict
    return data


def render(data):
    L = ["", f"MoM Cohort Retention Heatmap   (as of {data['as_of']})", "=" * 60]
    offsets = data["max_offset"]
    header = "Cohort   Size │ " + " ".join(f"M{m:<3d}" for m in range(offsets + 1))
    L.append(header)
    L.append("-" * len(header))
    for c in data["cohorts"]:
        cells = []
        for r in c["retention"]:
            cells.append("  . " if r is None else f"{r*100:3.0f}%")
        L.append(f"{c['cohort']}  {c['size']:>4d} │ " + " ".join(cells))
    L += ["",
          f"Early churn rate (M1–M2): {data['early_churn_rate']*100:.1f}%",
          f"Late churn rate  (M3+)  : {data['late_churn_rate']*100:.1f}%",
          "",
          f">>> {data['verdict']}", ""]
    return "\n".join(L)


def build_parser():
    p = argparse.ArgumentParser(
        description="MoM cohort retention heatmap + early/late churn diagnosis.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--csv", required=True, help="Path to subscriptions CSV "
                   "(customer_id, signup_date, churn_date)")
    p.add_argument("--max-offset", type=int, default=12, help="Months-since-signup columns")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    data = build(load(args.csv), args.max_offset)
    print(json.dumps(data, indent=2) if args.json else render(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
