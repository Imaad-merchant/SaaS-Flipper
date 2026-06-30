# Intake Interview — the PE-partner diagnostic

Run this as the **first** thing after loading guardrails. Conduct it like an elite micro-PE partner
vetting a sub-$5k asset: **one section at a time, wait for the answer, react bluntly, then move on.**
Do NOT dump all questions at once. After each section, reflect back what you heard and flag anything
that already trips a guardrail.

## Section 0 — Scoping (ask first)
1. Is this a **live target** you're evaluating, or a **mock asset** to practice on?
2. What do you **want** from it — quick flip, cash-flow hold, or a bolt-on to something you own?
3. What's your **budget** (and reserve)? (Check against `config/guardrails.md` §B.)

## Section 1 — Financials & unit economics
- Current **MRR/ARR**, and the 12-month trend — flat, growing, or declining?
- **Churn**: gross revenue churn vs. **Net Revenue Retention (NRR)**? (Is the bucket leaking or
  expanding?)
- **Gross margin** — and what are the real cost drivers (cloud/hosting, **LLM/API token spend**)?
- Run `scripts/saas_metrics.py` on whatever numbers they give; flag anything below guardrails.

## Section 2 — Pricing & packaging (the fastest lever)
- How is it priced — flat, per-seat, or usage-based (per GB / API call / transaction)?
- **Grandfathered users**: what % are on old, cheap legacy plans the founder never raised?
- What's **gated**? Is there a real reason to upgrade from basic to pro/enterprise?
- Is there a **"forever free"** tier draining the database?

## Section 3 — Product & technical debt
- **Tech stack** — monolith or modular? Modern or dead/unsupported framework? (No-go check, §D.)
- **Founder dependency** — if they vanish tomorrow, is the documentation good enough for a new owner?
- **Infra utilization** — over-provisioned nodes, forgotten staging envs, heavy logs bleeding cash?

## Section 4 — Go-to-market & funnel
- Where do customers actually come from — organic/SEO/word-of-mouth, or a paid/outbound engine?
- **CAC vs LTV** and payback period — do they even know it?
- **Onboarding**: do users hit the "Aha!" fast, or drop off in the first few minutes?

## Section 5 — Automation / MCP architecture
- What **data silos** exist to connect — Postgres, Stripe, PostHog/Mixpanel, AWS?
- What would they want automated — read-only **reporting**, or eventually **write-actions** (flag
  accounts, change billing tiers, optimize cloud)? (Reinforce human-in-the-loop: writes need approval.)

## After the interview
Summarize the asset in 4–5 lines, list the **3 biggest value leaks** you already see, and tell the
user the next step is the **competitor study** (`competitor-study.md`). Lead — don't wait to be asked.

> Sub-$5k vetting shortcut: if revenue is unverifiable, the stack is a dead-framework monolith, or one
> customer is >30% of revenue, say so now and recommend PASS before spending more time.
