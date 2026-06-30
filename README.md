# SaaS Flipper 💸

A Claude Code **skill** that turns Claude into a **micro-PE Operating Partner** — it *leads* a
sub-$5,000 micro-SaaS acquisition end to end. It interviews you, studies competitors, judges flip
potential, builds the value-creation plan and execution to-do, and generates an investor PowerPoint.
It's **brutally honest**: it rates your ideas, pushes back, and does not rubber-stamp.

## What it does when activated (in order)

1. **Interviews you** one section at a time — business, goals, tech stack, then financials, pricing,
   product/tech-debt, GTM, automation.
2. **Studies competitors** live (G2, Product Hunt, AlternativeTo, pricing pages) and forms a
   **"different, not better"** positioning wedge.
3. **Resale-value plan** — concrete levers, each tied to a source playbook.
4. **Flip pros & cons** — an honest **BUY / PASS / COUNTER** scored against your guardrails.
5. **Step-by-step execution to-do** — ordered by cash-flow × complexity (Quick-Wins → Growth → Exit).
6. **Investor PowerPoint** — a real `.pptx` for partners/investors.

### How it thinks
- **Anti-sycophancy is a hard rule** — it rates ideas 🟢 Strong / 🟡 Mixed / 🔴 Kill it, with reasons.
- **Sourced judgement** — opinions come from the embedded playbooks + your `config/guardrails.md` +
  live competitor evidence, not freeform opinion. It cites what each verdict rests on.
- **Virtual Operating Partner** — runs telemetry (churn heatmaps, pricing scans, live scorecards) on
  your data exports, and uses live **MCP** tools (Stripe/Postgres/PostHog/AWS) when connected.
- **Human-in-the-loop** — it drafts and simulates writes (billing changes, migration emails) but
  **you approve** before anything executes.

## Quick start

The skill lives in [`.claude/skills/saas-flipper/`](.claude/skills/saas-flipper/) and loads
automatically in Claude Code. Try:

- *"Evaluate this micro-SaaS I'm thinking of buying — interview me."*
- *"Build me a value-creation plan and an investor deck for this $3.5k tool."*
- *"Is this a good flip? Be honest."*

**Set your rules first:** edit [`config/guardrails.md`](.claude/skills/saas-flipper/config/guardrails.md)
— hurdle rates, churn ceilings, ARPU lens, and no-go zones the Operating Partner must obey.

The helper scripts run standalone too (stdlib-only Python, no install — except the deck):

```bash
cd .claude/skills/saas-flipper/scripts
python3 saas_metrics.py       --help   # unit economics: MRR/ARR, churn, LTV, CAC, Rule of 40, SDE
python3 valuation.py          --help   # valuation range from multiples + flip target
python3 scorecard.py          --help   # live Rule-of-40 / LTV:CAC / NRR vs guardrails + levers
python3 cohort_churn.py       --help   # MoM retention heatmap; early (onboarding) vs late (utility) churn
python3 grandfathered_scan.py --help   # flag legacy underpayers vs usage; size the migration uplift
python3 build_deck.py         --help   # investor .pptx   (one-time:  pip install python-pptx)
```

## Install globally (use it in every project / the desktop app)

By default the skill only shows up when Claude Code is opened **at this repo's root**. To make
`/saas-flipper` available in **every** project — including the **desktop app** — install it into your
personal skills folder (`~/.claude/skills/`).

> ℹ️ The command is **`/saas-flipper`** — one word, hyphen, **no space**. (Typing `/saas flipper`
> with a space won't match.) The command name comes from the skill's folder name.

**One command** (from the repo root, after you've cloned/pulled this repo locally):

```bash
bash install-global.sh
```

**Or copy it manually:**

```bash
# macOS / Linux
mkdir -p ~/.claude/skills && cp -r .claude/skills/saas-flipper ~/.claude/skills/
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force ~/.claude/skills
Copy-Item -Recurse -Force .claude/skills/saas-flipper ~/.claude/skills/
```

**Then:** if `~/.claude/skills/` didn't already exist, **fully quit and reopen the desktop app** so it
picks up the new skills folder (existing skills hot-reload, but a brand-new top-level folder needs a
restart). Now type **`/saas-flipper`** in any project.

## What's inside

| Path | What it is |
|------|------------|
| `SKILL.md` | The Operating-Partner persona + 6-step activation flow |
| `config/guardrails.md` | **Your rules** (loaded first): hurdle rates, churn ceilings, ARPU lens, no-go zones |
| `references/intake-interview.md` | The one-section-at-a-time PE interview + sub-$5k vetting |
| `references/competitor-study.md` | Mandatory competitor research → "different, not better" wedge |
| `references/pe-value-creation.md` | PE value-creation playbook reframed for sub-$5k indie reality |
| `references/vop-telemetry.md` | The 5 Virtual-Operating-Partner capabilities + scripts + human-in-the-loop |
| `references/master-playbook.md` | The end-to-end pipeline — stages, decision gates, risk rules |
| `references/sourcing-and-marketplaces.md` | How + where to find deals + the **Trap Filter** |
| `references/due-diligence.md` | Numbers to demand, SDE add-backs, red/green flags |
| `references/valuation-and-comparables.md` | Multiples (~2–4× ARR; distressed buys 12–18× MRR) + comps |
| `references/value-extraction-sop.md` | Lean value extraction by cash-flow × complexity |
| `references/growth-and-marketing.md` | AARRR, TTV, pricing psychology, "Different not Better" |
| `references/financing-acquisitions.md` | Funding the buy: capital stack, seller financing, earnouts |
| `references/closing-and-legal.md` | LOI → APA → escrow, asset-transfer checklist, legal pitfalls |
| `references/exit-and-resale.md` | When/where/how to sell, data room, negotiation, deal structure |
| `scripts/saas_metrics.py` · `valuation.py` · `scorecard.py` | Unit economics, valuation, health scorecard |
| `scripts/cohort_churn.py` · `grandfathered_scan.py` | Telemetry: retention heatmap, legacy-underpayer scan |
| `scripts/build_deck.py` | Generates the investor `.pptx` (needs `python-pptx`) |
| `templates/` | interview/competitor-matrix, value-creation-playbook, execution-todo, deal-memo, exit-prospectus, sample deck JSON |

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
- **Value extraction by cash-flow × complexity** — lean Quick-Wins → Growth → Exit (no calendar bloat). → `references/value-extraction-sop.md`
- **"Different, not Better" transformation protocol** — workflow-over-LLM, vertical pivot, monetization pivot. → `references/growth-and-marketing.md` + `references/competitor-study.md`
- **Valuation bands** — ~2–4× ARR for sub-$1M micro-SaaS (up to 8× top-quartile) with quality adjustments. → `references/valuation-and-comparables.md` + `scripts/valuation.py`

### 🏛️ Operating-Partner frameworks (from user-provided PE playbooks)
Synthesized into the upgraded skill so Claude operates like an institutional partner, scaled to sub-$5k:
- **PE intake interview** — the one-section-at-a-time diagnostic. → `references/intake-interview.md`
- **PE value-creation playbook** — Holy-Trinity metrics (LTV/CAC>3×, NRR>100%, Rule of 40≥40), pricing/packaging levers, multiple arbitrage, small bolt-ons. → `references/pe-value-creation.md`
- **Virtual Operating Partner** — telemetry & action (cohort heatmap, grandfathered scan, live scorecard, add-on scouting, tech-debt audit), MCP-aware, human-in-the-loop. → `references/vop-telemetry.md`
- **Guardrails + human-in-the-loop** — user-set hurdle rates & no-go zones; draft/simulate, approve-to-execute. → `config/guardrails.md`

---

> ⚠️ **Not financial advice.** Flipping businesses carries real risk. Always verify a seller's
> revenue independently (insist on live Stripe/analytics access), do your own due diligence, and
> consult appropriate legal/financial professionals before closing a deal.
