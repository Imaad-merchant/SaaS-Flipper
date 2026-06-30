#!/usr/bin/env python3
"""grandfathered_scan.py — find legacy users underpaying relative to the value they extract.

Joins a billing export (who pays what) with a usage export (how much they use) and flags accounts
that are on a cheap/legacy price BUT in a high usage percentile — prime candidates to migrate to a
modern/value-based tier. Outputs the flagged list + the monthly revenue uplift if migrated.
Human-in-the-loop: this only IDENTIFIES + lets you draft outreach. It never changes billing.

CSV inputs (headers required):
  --billing : customer_id, price            (price = current monthly $)
  --usage   : customer_id, usage            (usage = any numeric value metric: API calls, seats, GB)

Example:
  python3 grandfathered_scan.py --billing billing.csv --usage usage.csv
  python3 grandfathered_scan.py --billing b.csv --usage u.csv --usage-pct 0.80 --target-price 49 --json
"""
import argparse
import csv
import json
import sys


def read_map(path, key, val, cast=float):
    out = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        cols = {(c or "").strip() for c in reader.fieldnames or []}
        if key not in cols or val not in cols:
            raise SystemExit(f"{path} must have headers '{key}' and '{val}' (got {reader.fieldnames})")
        for r in reader:
            cid = (r.get(key) or "").strip()
            if not cid:
                continue
            try:
                out[cid] = cast(r.get(val))
            except (TypeError, ValueError):
                continue
    return out


def percentile_rank(sorted_vals, x):
    """Fraction of values <= x (0..1)."""
    if not sorted_vals:
        return 0.0
    lo, hi = 0, len(sorted_vals)
    # count of values <= x
    count = 0
    for v in sorted_vals:
        if v <= x:
            count += 1
        else:
            break
    return count / len(sorted_vals)


def scan(billing, usage, usage_pct, legacy_price, target_price):
    common = [c for c in billing if c in usage]
    if not common:
        raise SystemExit("no overlapping customer_id between billing and usage")
    prices = [billing[c] for c in common]
    median_price = sorted(prices)[len(prices) // 2]
    if legacy_price is None:
        legacy_price = median_price  # "legacy/cheap" = at or below the median price
    if target_price is None:
        target_price = max(prices)  # migrate to the top existing tier by default

    usage_sorted = sorted(usage[c] for c in common)

    flagged = []
    for c in common:
        pr = percentile_rank(usage_sorted, usage[c])
        if billing[c] <= legacy_price and pr >= usage_pct:
            flagged.append({
                "customer_id": c,
                "current_price": round(billing[c], 2),
                "usage": usage[c],
                "usage_percentile": round(pr, 3),
                "suggested_price": round(target_price, 2),
                "monthly_uplift": round(max(0.0, target_price - billing[c]), 2),
            })
    flagged.sort(key=lambda x: (-x["usage_percentile"], x["current_price"]))
    total_uplift = round(sum(f["monthly_uplift"] for f in flagged), 2)
    return {
        "median_price": round(median_price, 2),
        "legacy_threshold": round(legacy_price, 2),
        "target_price": round(target_price, 2),
        "usage_percentile_cutoff": usage_pct,
        "accounts_scanned": len(common),
        "flagged_count": len(flagged),
        "total_monthly_uplift": total_uplift,
        "total_annual_uplift": round(total_uplift * 12, 2),
        "flagged": flagged,
    }


def render(d):
    L = ["", "Grandfathered-Account Pricing Scan", "=" * 50,
         f"Accounts scanned        : {d['accounts_scanned']}",
         f"'Legacy' price threshold: <= ${d['legacy_threshold']:,.2f} (median ${d['median_price']:,.2f})",
         f"Usage percentile cutoff : top {(1-d['usage_percentile_cutoff'])*100:.0f}% "
         f"(>= {d['usage_percentile_cutoff']*100:.0f}th pct)",
         f"Suggested target price  : ${d['target_price']:,.2f}",
         "",
         f"FLAGGED: {d['flagged_count']} underpaying power users", "-" * 50]
    if d["flagged"]:
        L.append(f"{'customer_id':<18}{'price':>8}{'usage':>10}{'pct':>7}{'→ target':>10}{'uplift':>9}")
        for f in d["flagged"]:
            L.append(f"{f['customer_id']:<18}${f['current_price']:>6.0f}{f['usage']:>10.0f}"
                     f"{f['usage_percentile']*100:>6.0f}%${f['suggested_price']:>8.0f}"
                     f"${f['monthly_uplift']:>7.0f}")
    else:
        L.append("  (none — no legacy users in a high usage percentile)")
    L += ["",
          f"Potential monthly uplift: ${d['total_monthly_uplift']:,.0f}  "
          f"(${d['total_annual_uplift']:,.0f}/yr) if migrated",
          "",
          "NEXT (human-in-the-loop): have Claude DRAFT a targeted, friendly migration email for these",
          "accounts — then YOU review and send. Do not auto-change billing.", ""]
    return "\n".join(L)


def build_parser():
    p = argparse.ArgumentParser(
        description="Flag legacy users underpaying vs. their usage; size the migration uplift.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--billing", required=True, help="CSV: customer_id, price")
    p.add_argument("--usage", required=True, help="CSV: customer_id, usage")
    p.add_argument("--usage-pct", type=float, default=0.80,
                   help="Usage percentile cutoff to count as a 'power user' (0..1)")
    p.add_argument("--legacy-price", type=float, default=None,
                   help="Price at/below which a user is 'legacy/cheap' (default: median price)")
    p.add_argument("--target-price", type=float, default=None,
                   help="Migration target price (default: top existing tier)")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    billing = read_map(args.billing, "customer_id", "price")
    usage = read_map(args.usage, "customer_id", "usage")
    d = scan(billing, usage, args.usage_pct, args.legacy_price, args.target_price)
    print(json.dumps(d, indent=2) if args.json else render(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
