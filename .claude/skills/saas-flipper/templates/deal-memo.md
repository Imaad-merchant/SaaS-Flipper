# Deal Memo — {{business_name}}

**Date:** {{date}}  **Source:** {{marketplace / listing URL}}  **Asking:** {{asking_price}}

## Verdict
> **{{BUY / PASS / COUNTER}} @ {{recommended_offer}}**
>
> One-line rationale: {{...}}

## The asset in one line
{{What it does, for whom, and how it makes money.}}

## Key metrics (verified?)
| Metric | Value | Verified? | Note |
|--------|-------|-----------|------|
| MRR / ARR | | Stripe/GA? | |
| Logo churn (mo) | | | |
| Revenue churn (mo) | | | |
| NRR | | | |
| Gross margin | | | |
| LTV / CAC / LTV:CAC | | | |
| CAC payback | | | |
| SDE (annual) | | | |
| Traffic (organic %) | | | |
| Customer concentration | | | top account = __% |

_(Numbers from `scripts/saas_metrics.py` — paste the run.)_

## Valuation
- Multiple band applied: {{low}}–{{high}}× ARR, adjusted base {{x}}× (why: {{quality factors}}).
- Range: low {{}} / base {{}} / high {{}}  _(from `scripts/valuation.py`)_
- SDE cross-check: {{}}

## Comparables
| Comp | MRR/ARR | Price | Multiple | Churn | Growth | Source |
|------|---------|-------|----------|-------|--------|--------|
| | | | | | | |
_Median multiple: {{}}. Target positioned {{above/below}} median because {{}}._

## Trap Filter
- [ ] Thin AI wrapper / no custom UI
- [ ] Horizontal competition
- [ ] Pricing on the wrong axis (seat vs usage)
- [ ] LTD cash bomb
- [ ] Customer concentration >20–30%
- [ ] Fake / paid-only traffic

Result: {{clean / trips N rules — effect on offer}}

## Risks & missing data to request from seller
- {{...}}

## Recommended action
- Offer: {{number}} ({{structure: cash / earnout / seller financing}})
- Contingencies: {{verified Stripe access, code review, transfer terms}}
- If grown to {{target MRR}}, projected resale ≈ {{}} → est. gross flip gain {{}}.
