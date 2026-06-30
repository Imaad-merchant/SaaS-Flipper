#!/usr/bin/env python3
"""valuation.py — value a SaaS / micro-SaaS for acquisition or resale.

Produces a low / base / high valuation range from revenue multiples (with an
optional SDE cross-check), adjusts the multiple for quality factors, shows
sensitivity to the multiple, and computes an implied flip target. Stdlib only.

Default bands (grounded in 2026 micro-SaaS reality — confirm against live comps):
  ARR multiple : 2x - 8x    (base 3x; sub-$1M micro-SaaS clears ~2-4x, 8x is top-quartile)
  SDE multiple : 2x - 4x    (annual, owner-operated)
Note: the often-quoted "8-10x ARR" is a larger-deal/top-quartile figure (median private
SaaS ~4.5x revenue per Aventis Advisors, a dataset that skews to $50M+ deals), NOT a
default for small flips. Anchor low; let quality factors earn the way up.

Examples
--------
  python3 valuation.py --mrr 8000 --churn 0.04 --growth 0.06
  python3 valuation.py --arr 96000 --sde 62000 --asking 250000 --json
"""
import argparse
import json
import sys


def money(x):
    return f"${x:,.0f}" if x is not None else "n/a"


def quality_adjustment(args):
    """Return (delta_multiplier, reasons[]) nudging the base multiple up/down.

    Each factor shifts the base ARR multiple by a small amount. Clamped later.
    """
    delta = 0.0
    reasons = []
    if args.churn is not None:
        if args.churn <= 0.03:
            delta += 1.0
            reasons.append(f"low churn {args.churn*100:.0f}%/mo (+1.0)")
        elif args.churn >= 0.07:
            delta -= 1.5
            reasons.append(f"high churn {args.churn*100:.0f}%/mo (-1.5)")
    if args.growth is not None:
        if args.growth >= 0.05:
            delta += 1.0
            reasons.append(f"growth {args.growth*100:.0f}%/mo (+1.0)")
        elif args.growth < 0:
            delta -= 2.0
            reasons.append(f"declining revenue (-2.0)")
    if args.nrr is not None:
        if args.nrr >= 1.0:
            delta += 0.5
            reasons.append(f"NRR {args.nrr*100:.0f}% (+0.5)")
        elif args.nrr < 0.9:
            delta -= 0.5
            reasons.append(f"NRR {args.nrr*100:.0f}% (-0.5)")
    if args.owner_dependent:
        delta -= 1.0
        reasons.append("high owner-dependency (-1.0)")
    if args.trap:
        delta -= 2.0
        reasons.append("trips Trap Filter (-2.0)")
    if args.moat:
        delta += 1.0
        reasons.append("defensible niche/workflow moat (+1.0)")
    return delta, reasons


def compute(args):
    # Resolve ARR from arr or mrr.
    arr = args.arr
    if arr is None and args.mrr is not None:
        arr = args.mrr * 12
    if arr is None and args.sde is None:
        raise ValueError("need --arr, --mrr, or --sde")

    lo_m, base_m, hi_m = args.mult_low, args.mult_base, args.mult_high

    delta, reasons = quality_adjustment(args)
    adj_base = base_m + delta
    # Keep the adjusted base inside the band.
    adj_base = max(lo_m, min(hi_m, adj_base))

    out = {
        "arr": arr,
        "mrr": (arr / 12) if arr is not None else None,
        "multiple_band": {"low": lo_m, "base": base_m, "high": hi_m},
        "quality_delta": round(delta, 2),
        "quality_reasons": reasons,
        "adjusted_base_multiple": round(adj_base, 2),
    }

    # Revenue-multiple valuation.
    if arr is not None:
        out["valuation_arr"] = {
            "low": arr * lo_m,
            "base": arr * adj_base,
            "high": arr * hi_m,
        }
        # Sensitivity table across the band.
        steps = []
        m = lo_m
        while m <= hi_m + 1e-9:
            steps.append({"multiple": round(m, 1), "value": round(arr * m)})
            m += max(0.5, (hi_m - lo_m) / 7)
        out["sensitivity"] = steps

    # SDE cross-check.
    if args.sde is not None:
        out["valuation_sde"] = {
            "low": args.sde * args.sde_mult_low,
            "base": args.sde * ((args.sde_mult_low + args.sde_mult_high) / 2),
            "high": args.sde * args.sde_mult_high,
        }

    # Asking-price verdict.
    if args.asking is not None and arr is not None:
        base_val = out["valuation_arr"]["base"]
        ratio = args.asking / base_val if base_val else None
        out["asking"] = args.asking
        out["asking_implied_arr_multiple"] = round(args.asking / arr, 2)
        if ratio is not None:
            if ratio <= 0.9:
                verdict = "BUY — asking is at/below fair value."
            elif ratio <= 1.15:
                verdict = "COUNTER — asking is near fair value; negotiate down."
            else:
                verdict = "PASS / hard COUNTER — asking is well above fair value."
            out["verdict"] = verdict
            out["asking_vs_base_ratio"] = round(ratio, 2)

    # Flip target: if you can move revenue to --target-mrr, value at adjusted base.
    if args.target_mrr is not None:
        target_arr = args.target_mrr * 12
        out["flip_target"] = {
            "target_mrr": args.target_mrr,
            "target_arr": target_arr,
            "projected_resale_base": target_arr * adj_base,
        }
        if args.asking is not None:
            gross = out["flip_target"]["projected_resale_base"] - args.asking
            out["flip_target"]["projected_gross_gain_over_asking"] = gross

    return out


def render(o):
    L = ["", "SaaS Valuation", "=" * 40]
    if o.get("arr") is not None:
        L.append(f"ARR                     : {money(o['arr'])}  (MRR {money(o['mrr'])})")
    band = o["multiple_band"]
    L.append(f"Multiple band (ARR)     : {band['low']}x - {band['high']}x (base {band['base']}x)")
    if o["quality_reasons"]:
        L.append(f"Quality adjustment      : {o['quality_delta']:+.1f}x  "
                 f"-> adjusted base {o['adjusted_base_multiple']}x")
        for r in o["quality_reasons"]:
            L.append(f"    - {r}")
    else:
        L.append(f"Adjusted base multiple  : {o['adjusted_base_multiple']}x")

    if "valuation_arr" in o:
        v = o["valuation_arr"]
        L += ["", "Valuation (revenue multiple):",
              f"    Low   ({band['low']}x)  : {money(v['low'])}",
              f"    Base  ({o['adjusted_base_multiple']}x) : {money(v['base'])}",
              f"    High  ({band['high']}x) : {money(v['high'])}"]
    if "valuation_sde" in o:
        s = o["valuation_sde"]
        L += ["", "Cross-check (SDE multiple):",
              f"    Low   : {money(s['low'])}",
              f"    Base  : {money(s['base'])}",
              f"    High  : {money(s['high'])}"]
    if "verdict" in o:
        L += ["", "Asking price:",
              f"    Asking                : {money(o['asking'])} "
              f"({o['asking_implied_arr_multiple']}x ARR)",
              f"    Asking / base value   : {o['asking_vs_base_ratio']}x",
              f"    >>> {o['verdict']}"]
    if "flip_target" in o:
        f = o["flip_target"]
        L += ["", "Flip target:",
              f"    If grown to MRR {money(f['target_mrr'])} (ARR {money(f['target_arr'])})",
              f"    Projected resale (base): {money(f['projected_resale_base'])}"]
        if "projected_gross_gain_over_asking" in f:
            L.append(f"    Gross gain over asking : "
                     f"{money(f['projected_gross_gain_over_asking'])}")
    L.append("")
    L.append("NOTE: micro-SaaS clears ~2-4x ARR; 8x+ is top-quartile. Confirm against live comps.")
    L.append("")
    return "\n".join(L)


def build_parser():
    p = argparse.ArgumentParser(
        description="Value a SaaS for acquisition or resale (multiples + sensitivity).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--arr", type=float, help="Annual recurring revenue ($)")
    p.add_argument("--mrr", type=float, help="Monthly recurring revenue ($) (ARR = MRR*12)")
    p.add_argument("--sde", type=float, help="Annual SDE ($) for cross-check valuation")
    p.add_argument("--asking", type=float, help="Seller's asking price ($) for a verdict")
    # Multiple band (ARR).
    p.add_argument("--mult-low", type=float, default=2.0, help="Low ARR multiple")
    p.add_argument("--mult-base", type=float, default=3.0, help="Base ARR multiple")
    p.add_argument("--mult-high", type=float, default=8.0, help="High ARR multiple")
    # SDE band.
    p.add_argument("--sde-mult-low", type=float, default=2.0, help="Low SDE multiple")
    p.add_argument("--sde-mult-high", type=float, default=4.0, help="High SDE multiple")
    # Quality factors.
    p.add_argument("--churn", type=float, help="Monthly churn fraction, e.g. 0.04")
    p.add_argument("--growth", type=float, help="Monthly growth fraction, e.g. 0.06 (neg = decline)")
    p.add_argument("--nrr", type=float, help="Net revenue retention fraction, e.g. 1.05")
    p.add_argument("--owner-dependent", action="store_true", help="High owner-dependency")
    p.add_argument("--trap", action="store_true", help="Trips the Trap Filter")
    p.add_argument("--moat", action="store_true", help="Has a defensible niche/workflow moat")
    # Flip projection.
    p.add_argument("--target-mrr", type=float, help="MRR you expect to reach post-flip")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        o = compute(args)
    except ValueError as e:
        build_parser().error(str(e))
    if args.json:
        print(json.dumps(o, indent=2))
    else:
        print(render(o))
    return 0


if __name__ == "__main__":
    sys.exit(main())
