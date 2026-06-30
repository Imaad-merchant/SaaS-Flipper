# Due Diligence — what to demand, SDE, red & green flags

> Rule zero: **screenshots are not evidence.** Insist on verified exports. If the seller
> won't connect Stripe/GA (or share read-only access), discount the offer or walk.

## The data room you must request

**Financials**
- Profit & Loss statement, trailing 12–24 months (monthly granularity).
- **Stripe / LemonSqueezy / Paddle export** — raw, not a dashboard screenshot.
- MRR/ARR breakdown by plan; new vs. expansion vs. churned MRR per month.
- All costs: hosting, APIs (esp. LLM token spend), tools, contractors, ad spend.

**Customers & churn**
- Churn **cohorts** (logo churn AND revenue/dollar churn), monthly.
- Customer concentration: revenue from top 1/5/10 accounts.
- Net Revenue Retention (NRR) if any expansion exists.

**Traffic & acquisition**
- Google Analytics / Plausible export: sources, organic vs. paid, trend.
- Where signups actually come from (attribution), and CAC by channel.

**Product & ops**
- Tech stack + third-party dependencies + infrastructure footprint.
- Code access / repo walkthrough; outstanding tech debt and security issues.
- Support load: tickets/month, time per ticket, who answers them.
- SOPs: what does the owner personally do each week? (owner-dependency).

## SDE — Seller's Discretionary Earnings
Micro-SaaS is usually priced on **SDE** (what the business really earns for an owner-operator),
not raw profit. Compute:

```
SDE = Net Profit
    + Owner's salary / draw
    + One-off / non-recurring costs (one-time contractor builds, legal setup)
    + Non-essential or personal expenses run through the business
    + Add-backs you will not incur (tools you already own, etc.)
    - Any normalized cost the owner was NOT paying but you will (e.g. real hosting/support)
```
The add-backs are where value is created or hidden — interrogate every line. Use
`scripts/saas_metrics.py --sde-addbacks` to total them.

## Red flags (discount or walk)
- **Declining MRR** or churn trending up over the last 3–6 months.
- **Customer concentration** >20–30% in one account.
- **LTD cash bomb** — lifetime deals inflating the headline number.
- **Fake / paid traffic** with no organic baseline; referral spam.
- **Hidden tech debt** — out-of-date packages, no tests, fragile single-server setup,
  undocumented one-person knowledge.
- **Margin erosion** — LLM/API costs scaling with usage faster than revenue.
- Seller won't verify revenue or give code access.

## Green flags (pay up / move fast)
- Verified, flat-to-growing Stripe MRR; low logo churn; positive or neutral NRR.
- Clean, transparent costs and healthy gross margin (80%+ typical for SaaS).
- Organic/SEO traffic you can compound.
- Clear, *fixable* owner-dependency (you can document and de-risk it pre-resale).
- A workflow/integration moat, not a thin model wrapper.
