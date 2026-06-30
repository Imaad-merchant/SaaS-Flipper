# SaaS Flipper 💸

A Claude Code **skill** that turns Claude into a world-class micro-SaaS arbitrage operator —
helping you **buy under-optimized SaaS businesses cheap, grow them in ~90 days, and resell them
for a higher multiple.**

It does three things:

1. **Assess** a target — analyzes the numbers (MRR/ARR, churn, margins, SDE, unit economics),
   builds comparables from live marketplace data, runs a "trap filter," and gives a
   **BUY / PASS / COUNTER** verdict with a number.
2. **Grow & flip** — runs a proven 30-day value-extraction SOP plus live niche research and hands
   you a prioritized 30/60/90 plan with a target exit multiple.
3. **Exit & resale** — tells you when to sell, where to list, how to package the data room/SOP,
   and how to structure and negotiate the deal.

## Quick start

The skill lives in [`.claude/skills/saas-flipper/`](.claude/skills/saas-flipper/) and loads
automatically in Claude Code when you ask flipping questions. Try:

- *"Should I buy a SaaS doing $8k MRR, 4% monthly churn, 80% margin, asking $250k?"*
- *"What's this micro-SaaS worth? Find me comparables."*
- *"I just bought this tool — build me a 30-day flip plan."*
- *"How and when should I exit and resell this SaaS?"*

The helper scripts run standalone too (stdlib-only Python, no install):

```bash
cd .claude/skills/saas-flipper/scripts
python3 saas_metrics.py --help     # MRR/ARR, churn, LTV, CAC, payback, Rule of 40, SDE
python3 valuation.py   --help      # valuation range from multiples + sensitivity + flip target
```

## What's inside

| Path | What it is |
|------|------------|
| `SKILL.md` | The persona + 3-phase workflow router |
| `references/master-playbook.md` | **The end-to-end plan** — 5 stages, decision gates, risk rules |
| `references/sourcing-and-marketplaces.md` | How + where to find deals (deal-flow system) + the **Trap Filter** |
| `references/due-diligence.md` | Numbers to demand, SDE add-backs, red/green flags |
| `references/valuation-and-comparables.md` | Multiples (3–10× ARR / 12–36× MRR) + building comps |
| `references/value-extraction-sop.md` | The day-by-day 30-day flip playbook |
| `references/growth-and-marketing.md` | AARRR, TTV, pricing psychology, "Different not Better" |
| `references/exit-and-resale.md` | When/where/how to sell, data room, negotiation, deal structure |
| `scripts/saas_metrics.py` · `scripts/valuation.py` | The calculators |
| `templates/` | `deal-memo.md`, `flip-plan.md`, `exit-prospectus.md` output templates |

---

# 📚 Resource Library

Every source that informs this skill, organized by category. The skill also fetches several of
these **live at runtime** for current multiples, comps, and tactics.

## 🎥 Video Playbooks
- [Flipping SaaS — walkthrough](https://www.youtube.com/watch?v=eSTtk_EXbAQ&t=740s) — end-to-end flip walkthrough.
- [Micro-SaaS / flipping playlist](https://www.youtube.com/watch?v=pFhVQo0YPyw&list=PLwcQbu9cKWclSZ5X1D2BFr3t4jBzpiSoi) — multi-part series on building and flipping micro-SaaS.
- [Flipping SaaS — strategy](https://www.youtube.com/watch?v=plrni3IBEyI) — how flippers source and grow assets.
- [SaaS acquisition / growth](http://www.youtube.com/watch?v=jAIontNGgWA) — acquisition and growth tactics.
- [SaaS flipping deep-dive](http://www.youtube.com/watch?v=QsugcuSBYV4) — additional operator perspective.

## 🏪 Marketplaces & Liquidity (where deals trade)
- [Acquire.com](https://acquire.com) — gold standard; 500k+ verified buyers; Stripe + Google Analytics verified metrics.
- [Microns.io](https://microns.io) — micro-exits under $100k; zero-commission, high-velocity developer platform.
- [TrustMRR](https://trustmrr.com) — MRR verified via live Stripe/LemonSqueezy API (kills fake-screenshot fraud).
- [Flippa](https://flippa.com) — the OG open marketplace for apps, SaaS, and pre-revenue digital assets.

## 📈 Flipping Strategy & Economics
- [How to flip a SaaS (Acquire blog)](https://blog.acquire.com/how-to-flip-a-saas-acquire/) — the canonical flip walkthrough from the biggest marketplace.
- [Make more money flipping micro-SaaS than building them (Medium)](https://medium.com/@urano10/how-to-make-more-money-flipping-micro-saas-than-building-them-137805122813) — the arbitrage thesis and economics.
- [The business of SaaS (Stripe Atlas)](https://stripe.com/guides/atlas/business-of-saas) — fundamentals: metrics, retention, pricing, growth.
- [What is micro-SaaS & how to build one in 2026 (netmaxims)](https://netmaxims.com/blog/what-is-micro-saas-and-how-to-build-one-successfully-in-2026/) — current micro-SaaS landscape.

## 🚀 Marketing & Growth
- [SaaS marketing strategy (Leadfeeder)](https://www.leadfeeder.com/blog/marketing-strategy/saas-marketing/) — acquisition and demand-gen playbooks.
- [SaaS marketing (Paddle)](https://www.paddle.com/resources/saas-marketing) — pricing, funnels, and growth from a SaaS payments leader.
- [SaaS product strategy framework (ProductLed)](https://productled.com/blog/saas-product-strategy-framework) — product-led growth, activation, and TTV.

## 🎯 Differentiation & Positioning
- [Stop struggling with differentiation (edwinabl)](https://www.edwinabl.com/articles/stop-struggling-with-differentiation) — "different, not better" positioning.
- [Custom website vs template (Connective)](https://connectivewebdesign.com/blog/custom-website-vs-template) — when a UI facelift moves the needle.

## 🌐 Market & Industry Trends
- [Platform consolidation 2026 — SaaS stack reduction & AI (Vantagepoint)](https://vantagepoint.io/blog/sf/insights/platform-consolidation-2026-saas-stack-reduction-ai) — where the market is heading.
- [SaaS industry monitor (BetterCloud)](https://www.bettercloud.com/monitor/saas-industry/) — ongoing industry data and benchmarks.

## 🧠 Embedded Frameworks
These operator frameworks are encoded directly into the skill's reference files so Claude applies
them automatically:
- **The Trap Filter** — when an asset is a structural trap (thin AI wrapper, horizontal, mispriced, LTD bomb). → `references/sourcing-and-marketplaces.md`
- **The 30-Day Value-Extraction SOP** — the day-by-day flip playbook. → `references/value-extraction-sop.md`
- **"Different, not Better" transformation protocol** — workflow-over-LLM, vertical pivot, monetization pivot. → `references/growth-and-marketing.md`
- **Valuation bands** — 3–10× ARR / 12–36× MRR with quality adjustments. → `references/valuation-and-comparables.md` + `scripts/valuation.py`

---

> ⚠️ **Not financial advice.** Flipping businesses carries real risk. Always verify a seller's
> revenue independently (insist on live Stripe/analytics access), do your own due diligence, and
> consult appropriate legal/financial professionals before closing a deal.
