# Valuation & Comparables

## The multiples (the durable method)

Micro-SaaS trades on a multiple of recurring revenue or SDE.

### ⚠️ Reality check — keep micro-SaaS multiples grounded (verified, 2026)
The "8–10× ARR" figure you'll hear quoted is a **larger-deal / top-quartile** number, not a default.
Specialist M&A data (Aventis Advisors, 543 deals since 2015) puts the **median private SaaS at
~4.5× revenue** (top quartile >8.1×, median ~23× EBITDA) — and that dataset skews toward $50M+
transactions. **Genuinely sub-$1M micro-SaaS on marketplaces realistically clears ~2–4× ARR.**
Treat the high end of any band as reserved for assets that are larger, fast-growing, profitable, and
low-churn — most flips are not that. Underwriting at 2–4× keeps you from overpaying. *(Source:
[Aventis Advisors — SaaS valuation multiples](https://aventis-advisors.com/saas-valuation-multiples/).)*

The market has also shifted **growth-first → profitability-first** (public-SaaS median growth ~12%,
EBITDA margins ~9–10% as of Q4 2025): buyers now pay up for **margin, low churn, and retention**, not
growth alone. Weight those factors heaviest when positioning a multiple.

### Working bands
- **ARR multiple:** micro-SaaS typically **~2×–4× ARR**; up to **~8×** only for exceptional
  (fast-growing, profitable, low-churn, defensible) assets. The often-cited 3–10× is the *broad* SaaS
  band — anchor to the low half for small deals.
- **MRR multiple:** **~24×–48× MRR** at 2–4× ARR (same thing, monthly). Distressed/underoptimized
  assets are often *acquired* far cheaper (12–18× MRR) — that gap is the flip.
- **SDE multiple:** small owner-operated deals quoted as **~2×–4× SDE** (annual).

> These are *bands*, not constants — they move with the market and skew with deal size. Before quoting
> a live number, `WebSearch`/`WebFetch` current Acquire.com / Flippa / Microns listings for the asset's
> size and niche, and adjust. The band above is the prior; comps are the evidence.
>
> **Do NOT rely on these refuted rules of thumb:** "≥40% ARR growth commands 7–10× while <20% gets
> 3–5×," and "Rule-of-40 score drives the multiple at ~1.1× per 10 points." Adversarial verification
> of 2026 data refuted both as deterministic rules. Growth, margin, and Rule-of-40 *inform* where in
> the band you land — they are not a formula. Always confirm against live comps.

### What moves the multiple

| Pushes multiple UP (toward 10× / 36×) | Pushes multiple DOWN (toward 3× / 12×) |
|---------------------------------------|----------------------------------------|
| Low churn (<3%/mo), high NRR (>100%)  | High churn, negative NRR |
| Growing MRR, organic acquisition      | Flat/declining MRR, paid-only traffic |
| Clean modern stack, documented, tested | Tech debt, fragile infra, undocumented |
| Low owner-dependency, real SOPs        | Owner is the product / does everything |
| Defensible niche / workflow moat       | Thin AI wrapper, horizontal, commodity |
| Diversified customers                  | One customer = most of revenue |
| Real recurring (card-on-file)          | LTD-propped or one-off revenue |

## Worked arbitrage example (the whole game in one line)
A tool at **$200/mo** ($2,400 ARR). Bought for **~$3,000** (≈15× MRR — cheap because
distribution is broken). Over 90 days you fix onboarding, re-anchor pricing, and add a content
funnel → **$600/mo** ($7,200 ARR). Relisted clean at a healthy multiple → **~$10,000**.
~3.3× on capital in a quarter. The value wasn't built; it was *unlocked*.

## Building comparables (do this every assessment)
1. Pull 5–10 **sold or listed** comps from Acquire.com / Flippa / Microns.io / TrustMRR in the
   same niche and revenue band (use `WebSearch`/`WebFetch` — these are live).
2. For each comp record: MRR/ARR, asking (or sold) price, implied multiple, churn, growth, age.
3. **Normalize** — strip LTD-inflated numbers, adjust for verified vs. claimed revenue.
4. Compute the comp-set median and range. Position the target relative to it using the
   up/down table above.
5. Cross-check the comp-derived number against `scripts/valuation.py` output. If they diverge,
   explain why (the target is better/worse than the median comp on which axis).

## Output
Feed the chosen multiple band and SDE/ARR into `scripts/valuation.py` to get a **low / base /
high** range, then state a single recommended offer (usually base, discounted for any red flags
or trap-filter hits). Put the comps table and the math in `templates/deal-memo.md`.
