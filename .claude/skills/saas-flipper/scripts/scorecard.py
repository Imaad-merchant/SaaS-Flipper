#!/usr/bin/env python3
"""scorecard.py — live financial-health scorecard vs. your guardrails, with lever recommendations.

Scores the "Holy Trinity" (Rule of 40, LTV:CAC, NRR) plus margin/churn against the thresholds in
config/guardrails.md, marks PASS/FAIL, and recommends a concrete lever for each miss. Standard
library only. Defaults match config/guardrails.md; override with flags if your guardrails differ.

Example:
  python3 scorecard.py --mrr 600 --growth 0.06 --growth-is-monthly --margin 0.82 \
      --ltv 800 --cac 100 --nrr 0.97
"""
import argparse
import json
import sys


def annualize(g, monthly):
    return (1 + g) ** 12 - 1 if monthly else g


def compute(a):
    rows = []
    recs = []

    # Rule of 40
    if a.growth is not None and a.margin is not None:
        g = annualize(a.growth, a.growth_is_monthly)
        ro40 = (g + a.margin) * 100
        ok = ro40 >= a.t_rule40
        rows.append(("Rule of 40", f"{ro40:.0f}", f">= {a.t_rule40:.0f}", ok))
        if not ok:
            recs.append("Rule of 40 below target → raise prices (margin) or fix activation/growth; "
                        "cut redundant cloud nodes to lift EBITDA%.")
    # LTV:CAC
    if a.ltv is not None and a.cac:
        ratio = a.ltv / a.cac
        ok = ratio >= a.t_ltv_cac
        rows.append(("LTV : CAC", f"{ratio:.1f}x", f">= {a.t_ltv_cac:.1f}x", ok))
        if not ok:
            recs.append("LTV:CAC below hurdle → lower CAC (lean to organic/outbound) or raise LTV "
                        "(reduce churn, raise ARPU).")
    # NRR
    if a.nrr is not None:
        ok = a.nrr * 100 >= a.t_nrr
        rows.append(("Net Revenue Retention", f"{a.nrr*100:.0f}%", f">= {a.t_nrr:.0f}%", ok))
        if not ok:
            recs.append("NRR under 100% = LEAKY BUCKET → add expansion (usage tiers, seats), cut "
                        "logo churn before spending on acquisition.")
    # Gross margin
    if a.margin is not None:
        ok = a.margin * 100 >= a.t_margin
        rows.append(("Gross margin", f"{a.margin*100:.0f}%", f">= {a.t_margin:.0f}%", ok))
        if not ok:
            recs.append("Margin below target → audit cloud/API spend (downsize over-provisioned "
                        "infra, cap LLM token usage).")
    # Churn
    if a.churn is not None:
        ok = a.churn * 100 <= a.t_churn
        rows.append(("Monthly logo churn", f"{a.churn*100:.1f}%", f"<= {a.t_churn:.0f}%", ok))
        if not ok:
            recs.append("Churn above ceiling → onboarding/TTV fix + retention email; run "
                        "cohort_churn.py to localize early vs late churn.")

    if not rows:
        raise SystemExit("provide at least one metric (e.g. --growth + --margin for Rule of 40)")

    passes = sum(1 for *_, ok in rows if ok)
    health = round(100 * passes / len(rows))
    return {
        "mrr": a.mrr, "arr": (a.mrr * 12 if a.mrr is not None else None),
        "metrics": [{"name": n, "value": v, "target": t, "pass": ok} for n, v, t, ok in rows],
        "passed": passes, "total": len(rows), "health_score": health,
        "recommended_levers": recs,
    }


def render(d):
    L = ["", "SaaS Health Scorecard (vs. guardrails)", "=" * 52]
    if d["mrr"] is not None:
        L.append(f"MRR ${d['mrr']:,.0f}  |  ARR ${d['arr']:,.0f}")
        L.append("")
    L.append(f"{'Metric':<24}{'Value':>10}{'Target':>12}   Verdict")
    L.append("-" * 60)
    for m in d["metrics"]:
        L.append(f"{m['name']:<24}{m['value']:>10}{m['target']:>12}   "
                 f"{'✅ PASS' if m['pass'] else '🔴 FAIL'}")
    L += ["", f"Health: {d['passed']}/{d['total']} metrics pass  ({d['health_score']}%)"]
    if d["recommended_levers"]:
        L += ["", "Recommended levers:"]
        L += [f"  - {r}" for r in d["recommended_levers"]]
    L.append("")
    return "\n".join(L)


def build_parser():
    p = argparse.ArgumentParser(
        description="Score Rule of 40 / LTV:CAC / NRR / margin / churn vs. guardrails + recommend levers.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--mrr", type=float, help="Monthly recurring revenue ($), for context")
    p.add_argument("--growth", type=float, help="Revenue growth as a fraction (annual unless --growth-is-monthly)")
    p.add_argument("--growth-is-monthly", action="store_true", help="Treat --growth as monthly")
    p.add_argument("--margin", type=float, help="Gross/profit margin fraction, e.g. 0.82")
    p.add_argument("--ltv", type=float, help="Lifetime value ($)")
    p.add_argument("--cac", type=float, help="Customer acquisition cost ($)")
    p.add_argument("--nrr", type=float, help="Net revenue retention fraction, e.g. 1.05")
    p.add_argument("--churn", type=float, help="Monthly logo churn fraction, e.g. 0.04")
    # Guardrail thresholds (defaults mirror config/guardrails.md)
    p.add_argument("--t-rule40", type=float, default=40, help="Rule of 40 target")
    p.add_argument("--t-ltv-cac", type=float, default=3.0, help="LTV:CAC hurdle")
    p.add_argument("--t-nrr", type=float, default=100, help="NRR target (percent)")
    p.add_argument("--t-margin", type=float, default=75, help="Gross margin target (percent)")
    p.add_argument("--t-churn", type=float, default=5, help="Max monthly churn (percent)")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    d = compute(args)
    print(json.dumps(d, indent=2) if args.json else render(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
