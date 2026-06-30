# PE Value-Creation Playbook — reframed for sub-$5k indie reality

The institutional private-equity playbook, stripped of corporate bloat and translated to a solo
operator flipping a sub-$5,000 micro-SaaS. **Keep** the metrics discipline, the pricing science, and
multiple arbitrage. **Drop** the 100-day committees, SDR/AE pods, Snowflake pipelines, and offshore
labor arbitrage — you don't have a team, you have you + Claude + contractors.

## The "Holy Trinity" metrics (audit every asset against these)
- **LTV : CAC ≥ 3×** — acquisition must pay back at least 3:1.
- **NRR > 100%** — existing customers should expand faster than they churn; under 100% is a *leaky
  bucket* flag (guardrail §A).
- **Rule of 40** — growth% + profit% ≥ 40. Below it, the asset is either not growing or not profitable
  enough; fix one before flipping.
Run `scripts/scorecard.py` to score these live and get lever recommendations.

## The levers, ranked by cash impact for a tiny asset

### 1. Pricing & packaging (fastest lever, do first)
- **Migrate grandfathered users** off legacy cheap plans — modern tiers or a **5–15% increase**.
  Model the churn hit against guardrail §C (max 5%); stage it if needed.
- **Value-based pricing** — price on a value metric (per seat / GB / transaction) so revenue grows as
  the customer grows.
- **Feature-gate the "Aha"** — lock the single highest-usage utility behind a Pro tier.
- **Kill "forever free"** — set a $19–$29/mo floor to filter for serious buyers.

### 2. Cost / margin (instant EBITDA on day one)
- **Infra downsizing** — indie apps over-provision Vercel/AWS/Supabase. Drop to a lean $5–10/mo tier,
  clean up heavy logs and dead staging envs. Pure margin on a low-revenue asset.
- **Vendor consolidation** — cut overlapping SaaS subscriptions the founder stacked up.

### 3. Distribution (validate one repeatable channel — solo scale)
- Not SDR pods. **You**, with Claude drafting: personalized 1:1 outbound to ~25 niche prospects/day on
  LinkedIn/X; re-engagement emails to churned/abandoned signups with a limited-time annual offer.
- Content clusters around long-tail buyer questions (compounds, AI-search friendly).

### 4. The wedge (from `competitor-study.md`)
"Different, not better" positioning is itself a value lever — it lifts conversion and defends the
multiple at exit.

## Multiple arbitrage & small bolt-ons (the financial trick, scaled down)
- Buy a tiny tool cheap (often **12–18× MRR** when distressed ≈ ~1–1.5× ARR), grow MRR and clean it up,
  resell at a healthy small-SaaS multiple (~**2–4× ARR**). The gain is revenue growth × multiple
  expansion.
- **Bolt-on**: if your asset lacks a feature, buying a tiny $500-MRR tool that already has it can be
  cheaper than building — and merging its revenue into a cleaner asset lifts the blended value.
  (No-go: never bolt on a dead-framework monolith — guardrail §D.)

## The exit framing
Turn a creative product into a **predictable little cash machine**: clean verified Stripe metrics, a
written SOP, low owner-dependency, a defensible wedge. The buyer is paying for predictability — package
it that way.
