# Sourcing & Marketplaces — where to find deals + the Trap Filter

## The arbitrage thesis
You are not building the next Salesforce. You are buying **digital real estate**: a tool
doing ~$200/mo bought for a ~$3,000 flat fee (≈15× MRR), optimizing its presentation and
pricing, bumping it to ~$600/mo, and flipping it for ~$10,000 inside 90 days. The edge is
"engineer brain" sellers — great code, terrible distribution. You buy the distribution gap.

## Where the liquidity is

| Marketplace | Best for | Why it matters |
|-------------|----------|----------------|
| **Acquire.com** | The default. Deals up to mid-7-figures. | Gold standard, 500k+ verified buyers; integrates Stripe + Google Analytics for **verified** metrics. |
| **Microns.io** | Micro-exits under $100k. | Tailor-made for small, high-velocity developer deals; zero-commission. |
| **TrustMRR** | Verifying revenue. | All MRR strictly verified via **live Stripe/LemonSqueezy API** — kills fake-screenshot fraud. |
| **Flippa** | Open liquidity, pre-revenue, side projects. | The OG open marketplace for apps/SaaS/digital assets; widest selection, lowest signal — dig. |

Also scan: indie founder communities (Indie Hackers, X/Twitter "build in public"), and
direct outreach to founders of stalled tools (cold DM the "I'm burnt out" posts).

## How to actually FIND good deals (deal flow is a system, not luck)

Good flips come from **volume + filters**, not from finding one perfect listing. Build a funnel.

### The screening funnel (100 → 10 → 3 → 1)
1. **100 raw listings** — cast wide across all four marketplaces weekly.
2. **→ 10 worth a look** — pass the 30-second filter: recurring revenue, in a niche you can
   understand, not an obvious trap, priced in your capital range.
3. **→ 3 worth diligence** — request verified Stripe/GA; run `scripts/saas_metrics.py`; check
   the Trap Filter; eyeball churn and concentration.
4. **→ 1 to offer** — full deal memo, comps, and a number.

Expect to reject ~99%. The discipline is in passing fast, not falling in love.

### Your buy-box (define it before you shop)
Write down and filter hard on:
- **Price range:** what you can pay AND fund the 90-day improvement on (keep reserve).
- **Revenue floor:** e.g. >$300–500 MRR verified (below that, signal is too noisy).
- **Business model:** recurring (card-on-file), not LTD-propped or one-off.
- **Niche:** something you can understand and write content for; prefer narrow/unsexy B2B.
- **The wedge:** there must be an obvious, fixable reason it's underpriced (broken onboarding,
  no marketing, ugly UI, mispriced) — that gap *is* your profit. No gap = no flip.

### Search filters to apply on each marketplace
Profitable · recurring revenue · age >12 months (survived the novelty) · low/declining ask
relative to MRR · solo founder ("engineer brain", burnt out) · organic traffic present.

### Deal-flow cadence (run it weekly)
- **Set alerts** on Acquire.com / Flippa / Microns for your buy-box; check TrustMRR for verified-MRR drops.
- **Mine "build in public" / "I'm shutting down / burnt out" posts** on X and Indie Hackers — the
  best deals are *off-market*. Cold-DM stalled founders; you'll face zero auction competition.
- **Track everything** in a simple pipeline (Sourced → Screened → Diligence → Offer → Closed).
- **Off-market beats on-market:** auctions bid prices up; a tired solo founder you reached
  directly will often sell at a great multiple just to be free of it.

## The Trap Filter — when to walk away

Flag a listing as a **TRAP** (lean PASS, or counter hard) if **any** of these hit:

1. **Thin AI wrapper.** It's a generic OpenAI/Anthropic wrapper with **zero custom UI system**
   or proprietary workflow — no moat, trivially cloned, margin-squeezed by model providers.
2. **Horizontal competition.** It competes broadly (generic coding assistant, generic image
   generator, generic "AI writer") against funded incumbents. No wedge.
3. **Pricing on the wrong axis.** Per-seat pricing in a market shifting to **usage-based**
   billing (or vice-versa) — revenue model is structurally mispriced.
4. **LTD cash bomb.** Revenue is propped up by **lifetime deals** — the "MRR" is an illusion;
   those users cost money forever and never renew.
5. **Single-customer concentration.** One customer is >20–30% of revenue — one churn = collapse.
6. **Fake or rented traffic.** Spikey, paid, or referral-bot traffic with no organic baseline.

A trap isn't always a no — sometimes it's a *cheaper* counter. But never pay a clean multiple
for a trap asset.

## Green-light signals (the opposite)
- Verified Stripe MRR, flat or growing, low logo churn (<3–5%/mo for micro-SaaS).
- A **narrow, unsexy ICP** (logistics, municipal compliance, franchise supply chain).
- Organic/SEO traffic with long-tail intent — distribution you can compound.
- A real workflow or integration moat, not just a model call.
- Owner-dependency that is *fixable* (undocumented but simple), so you can de-risk and relist.
