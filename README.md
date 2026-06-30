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
| `references/financing-acquisitions.md` | Funding the buy: capital stack, seller financing, earnouts |
| `references/closing-and-legal.md` | LOI → APA → escrow, asset-transfer checklist, legal pitfalls |
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

## 🤝 Deal Structure, Financing & Closing
- [How to structure a SaaS acquisition deal (Acquire blog)](https://blog.acquire.com/how-to-structure-a-saas-acquisition-deal-that-makes-you-and-the-buyer-happy/) — cash/earnout/equity blends that close deals.
- [What is an Asset Purchase Agreement? (+ template) (Acquire)](https://blog.acquire.com/what-is-an-asset-purchase-agreement/) — the binding contract explained.
- [Technology & SaaS M&A legal guide (Acquisition Stars)](https://acquisitionstars.com/blog/technology-saas-ma-guide) — buyer/seller legal walkthrough.
- [Micro-SaaS funding when EBITDA < $500K (Distilled Funding)](https://www.distilledfunding.com/post/micro-saas-acquisitions-funding-options-when-ebitda-500k) — SBA, revenue-based, and the capital stack.
- [Seller notes, earnouts & SBA — building blocks of a deal (ClearlyAcquired)](https://www.clearlyacquired.com/blog/seller-notes-earnouts-and-sba-the-building-blocks-of-a-main-street-deal) — small-deal financing mechanics.
- [Escrow.com for safer startup acquisitions](https://www.escrow.com/partners/landing/microacquire) — how escrow protects both sides at close.

## 🚩 Due Diligence & Red Flags
- [8 red flags in SaaS due diligence (Acquire)](https://blog.acquire.com/8-red-flags-to-beware-of-when-doing-due-diligence-on-a-saas-startup/) — what to walk away from.
- [SaaS due diligence red flags that cut valuation in 2026 (ConsultEFC)](https://consultefc.com/saas-due-diligence-red-flags-valuation/) — current valuation-killers.
- [27-point SaaS due diligence checklist (The Ownix)](https://theownix.com/en/blog/saas-due-diligence-checklist-27-points) — a thorough buyer checklist.
- [Buy a $5K micro-SaaS and grow it — 2026 playbook (BuildMVPFast)](https://www.buildmvpfast.com/blog/buy-micro-saas-grow-acquisition-playbook-2026) — end-to-end small-deal walkthrough.

## 🎯 Differentiation & Positioning
- [Stop struggling with differentiation (edwinabl)](https://www.edwinabl.com/articles/stop-struggling-with-differentiation) — "different, not better" positioning.
- [Custom website vs template (Connective)](https://connectivewebdesign.com/blog/custom-website-vs-template) — when a UI facelift moves the needle.

## 📊 Valuation Data (benchmarks)
- [SaaS valuation multiples (Aventis Advisors)](https://aventis-advisors.com/saas-valuation-multiples/) — 543-deal dataset; median private SaaS ~4.5× revenue / ~23× EBITDA (skews to large deals — micro-SaaS clears lower, ~2–4× ARR). *Verified via deep research, 2026.*
- [Acquire.com biannual acquisition multiples report (Jan 2026)](https://blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026/) — marketplace-level multiples for small deals.

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
