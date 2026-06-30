#!/usr/bin/env python3
"""saas_metrics.py — core unit economics for a SaaS / micro-SaaS flip.

Computes MRR/ARR, gross margin, logo & revenue churn, LTV, CAC, LTV:CAC,
CAC payback, the Rule of 40, and SDE (with add-backs). Standard library only.

Examples
--------
  # Quick assessment of a target
  python3 saas_metrics.py --mrr 8000 --customers 200 --churned-customers 8 \
      --gross-margin 0.80 --new-customers 15 --marketing-spend 1500 \
      --growth-rate 0.06

  # SDE with add-backs
  python3 saas_metrics.py --mrr 8000 --net-profit 5200 --owner-salary 0 \
      --sde-addbacks 400 600 --json
"""
import argparse
import json
import sys


def pct(x):
    return f"{x * 100:.1f}%" if x is not None else "n/a"


def money(x):
    return f"${x:,.0f}" if x is not None else "n/a"


def compute(args):
    out = {}

    # --- Revenue ---
    mrr = args.mrr
    arr = mrr * 12 if mrr is not None else None
    out["mrr"] = mrr
    out["arr"] = arr

    # --- Churn ---
    logo_churn = None
    if args.customers and args.churned_customers is not None:
        logo_churn = args.churned_customers / args.customers
    rev_churn = None
    if mrr and args.churned_mrr is not None:
        rev_churn = args.churned_mrr / mrr
    out["logo_churn_monthly"] = logo_churn
    out["revenue_churn_monthly"] = rev_churn

    # --- ARPU ---
    arpu = None
    if mrr and args.customers:
        arpu = mrr / args.customers
    out["arpu_monthly"] = arpu

    # --- LTV ---
    # Lifetime (months) = 1 / monthly churn. Use revenue churn if given, else logo churn.
    churn_for_ltv = rev_churn if rev_churn else logo_churn
    ltv = None
    avg_lifetime_months = None
    if churn_for_ltv and arpu is not None:
        avg_lifetime_months = 1 / churn_for_ltv
        gross_margin = args.gross_margin if args.gross_margin is not None else 1.0
        ltv = arpu * avg_lifetime_months * gross_margin
    out["avg_lifetime_months"] = avg_lifetime_months
    out["ltv"] = ltv

    # --- CAC ---
    cac = None
    if args.marketing_spend is not None and args.new_customers:
        cac = args.marketing_spend / args.new_customers
    out["cac"] = cac

    # --- LTV:CAC and payback ---
    ltv_cac = (ltv / cac) if (ltv and cac) else None
    payback_months = None
    if cac and arpu:
        margin = args.gross_margin if args.gross_margin is not None else 1.0
        denom = arpu * margin
        payback_months = cac / denom if denom else None
    out["ltv_to_cac"] = ltv_cac
    out["cac_payback_months"] = payback_months

    # --- Rule of 40 ---
    rule_of_40 = None
    if args.growth_rate is not None and args.gross_margin is not None:
        # growth% (annualized if monthly given via --growth-is-monthly) + profit margin proxy
        g = args.growth_rate
        if args.growth_is_monthly:
            g = (1 + g) ** 12 - 1
        margin = args.profit_margin if args.profit_margin is not None else args.gross_margin
        rule_of_40 = (g + margin) * 100
    out["rule_of_40"] = rule_of_40

    # --- SDE ---
    sde_annual = None
    if args.net_profit is not None:
        monthly = args.net_profit
        monthly += args.owner_salary or 0
        monthly += sum(args.sde_addbacks or [])
        monthly -= args.normalized_costs or 0
        sde_annual = monthly * 12
    out["sde_annual"] = sde_annual

    return out


def render_table(o):
    rows = [
        ("MRR", money(o["mrr"])),
        ("ARR", money(o["arr"])),
        ("ARPU (monthly)", money(o["arpu_monthly"])),
        ("Logo churn (monthly)", pct(o["logo_churn_monthly"])),
        ("Revenue churn (monthly)", pct(o["revenue_churn_monthly"])),
        ("Avg lifetime (months)",
         f"{o['avg_lifetime_months']:.1f}" if o["avg_lifetime_months"] else "n/a"),
        ("LTV", money(o["ltv"])),
        ("CAC", money(o["cac"])),
        ("LTV:CAC",
         f"{o['ltv_to_cac']:.1f}x" if o["ltv_to_cac"] else "n/a"),
        ("CAC payback (months)",
         f"{o['cac_payback_months']:.1f}" if o["cac_payback_months"] else "n/a"),
        ("Rule of 40",
         f"{o['rule_of_40']:.0f}" if o["rule_of_40"] is not None else "n/a"),
        ("SDE (annual)", money(o["sde_annual"])),
    ]
    width = max(len(r[0]) for r in rows)
    lines = ["", "SaaS Unit Economics", "=" * (width + 18)]
    for k, v in rows:
        lines.append(f"{k.ljust(width)} : {v}")

    # Quick read-outs
    notes = []
    if o["ltv_to_cac"] is not None:
        if o["ltv_to_cac"] >= 3:
            notes.append("LTV:CAC >= 3x — healthy acquisition economics.")
        else:
            notes.append("LTV:CAC < 3x — acquisition may be unprofitable; verify CAC.")
    if o["logo_churn_monthly"] is not None:
        if o["logo_churn_monthly"] > 0.05:
            notes.append("Logo churn > 5%/mo — high for micro-SaaS; pressure the multiple down.")
        else:
            notes.append("Logo churn <= 5%/mo — acceptable for micro-SaaS.")
    if o["rule_of_40"] is not None:
        notes.append("Rule of 40 " + ("PASS" if o["rule_of_40"] >= 40 else "FAIL")
                     + f" ({o['rule_of_40']:.0f}).")
    if notes:
        lines.append("")
        lines.append("Read-out:")
        lines.extend("  - " + n for n in notes)
    lines.append("")
    return "\n".join(lines)


def build_parser():
    p = argparse.ArgumentParser(
        description="Compute SaaS unit economics for a flip assessment.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--mrr", type=float, help="Monthly recurring revenue ($)")
    p.add_argument("--customers", type=int, help="Total active customers")
    p.add_argument("--churned-customers", type=int,
                   help="Customers lost last month (for logo churn)")
    p.add_argument("--churned-mrr", type=float,
                   help="MRR lost last month (for revenue churn)")
    p.add_argument("--new-customers", type=int,
                   help="New customers acquired last month (for CAC)")
    p.add_argument("--marketing-spend", type=float,
                   help="Sales+marketing spend last month ($) (for CAC)")
    p.add_argument("--gross-margin", type=float,
                   help="Gross margin as a fraction, e.g. 0.80")
    p.add_argument("--profit-margin", type=float,
                   help="Profit margin fraction for Rule of 40 (defaults to gross margin)")
    p.add_argument("--growth-rate", type=float,
                   help="Revenue growth rate as a fraction (annual unless --growth-is-monthly)")
    p.add_argument("--growth-is-monthly", action="store_true",
                   help="Treat --growth-rate as monthly and annualize it")
    # SDE inputs
    p.add_argument("--net-profit", type=float,
                   help="Monthly net profit ($) (for SDE)")
    p.add_argument("--owner-salary", type=float, default=0,
                   help="Monthly owner salary/draw to add back ($)")
    p.add_argument("--sde-addbacks", type=float, nargs="*", default=[],
                   help="One-off/non-essential monthly costs to add back ($ ...)")
    p.add_argument("--normalized-costs", type=float, default=0,
                   help="Monthly cost the owner skipped but you WILL pay ($), subtracted")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.mrr is None and args.net_profit is None:
        build_parser().error("provide at least --mrr (and/or --net-profit for SDE)")
    o = compute(args)
    if args.json:
        print(json.dumps(o, indent=2))
    else:
        print(render_table(o))
    return 0


if __name__ == "__main__":
    sys.exit(main())
