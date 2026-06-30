# Valuation & Comparables

## The multiples (the durable method)

Micro-SaaS trades on a multiple of recurring revenue or SDE:

- **ARR multiple:** typically **3×–10× ARR**.
- **MRR multiple:** typically **12×–36× MRR** (the same band expressed monthly).
- **SDE multiple:** small owner-operated deals often quoted as **~2×–4× SDE** (annual).

> These are *bands*, not constants — they move with the market. Before quoting a live number,
> `WebSearch`/`WebFetch` current Acquire.com / Flippa / Microns listings for the asset's size
> and niche, and adjust. The band above is the prior; comps are the evidence.

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
