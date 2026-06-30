# Guardrails — your investment rules (EDIT THIS)

The Operating Partner **loads this file at the start of every engagement** and applies these rules to
every judgement. Change the numbers to match your risk tolerance. If a value is blank, the documented
default is used.

> These are *your* rules, not the AI's opinion. When the AI gives a verdict it must cite the relevant
> rule here. When you change a number, the AI's recommendations change with it.

## A. Unit-economic hurdles (a deal/asset must clear these)
| Metric | Rule | Default | Your value |
|--------|------|---------|-----------|
| LTV : CAC | Minimum acceptable ratio | **≥ 3×** | 3× |
| Net Revenue Retention (NRR) | Below this → auto **"leaky bucket"** flag | **100%** | 100% |
| Rule of 40 | growth% + profit% must clear | **≥ 40** | 40 |
| Gross margin | Minimum for a "clean" SaaS | **75%** | 75% |
| Monthly logo churn | Above this is a red flag for micro-SaaS | **5%** | 5% |
| CAC payback | Maximum acceptable | **12 months** | 12 |

## B. Deal-size box (sub-$5k focus)
| Parameter | Default | Your value |
|-----------|---------|-----------|
| Max purchase price | **$5,000** | $5,000 |
| Min verified MRR to consider | **$100** | $100 |
| Improvement reserve to keep (on top of price) | **≥ 1× purchase price** | 1× |
| Min asking-price discount vs. fair value to "BUY" | **10%** | 10% |

## C. Pricing & change limits
- **Max acceptable churn from a price hike: 5%.** Model the hit before recommending any increase; if
  projected churn exceeds this, stage the increase or grandfather a cohort.
- **Floor price for a serious-buyer base:** $19–$29/mo (kill/hard-gate "forever free" tiers).
- **ARPU lens (decision rule):** prefer fewer, higher-paying niche customers. Evaluate every feature
  and pricing move by its effect on ARPU — 50 customers @ $100/mo beats 1,000 @ $5/mo.

## D. NO-GO zones (do not recommend, flag hard if present)
- Never recommend an **add-on/bolt-on acquisition** built on a **monolithic codebase in an
  unsupported/dead framework**.
- Walk on **unverifiable revenue** (no live Stripe/analytics access).
- Walk on **single-customer concentration > 30%** of revenue.
- Avoid **thin AI wrappers** with no custom workflow/UI moat (Trap Filter, see sourcing reference).
- No **irreversible writes** (billing changes, DB updates, email blasts) without explicit user approval.

## E. Operating philosophy
- **Minimum Sellable Product (MSP):** speed over perfection. If the software reliably solves a boring
  problem, don't burn months refactoring — fix monetization and distribution, then flip.
- **Different, not better:** win on a wedge (narrow ICP / workflow / monetization), never by
  out-building incumbents.
- **Human-in-the-loop:** the AI drafts and simulates; you approve before anything executes.
