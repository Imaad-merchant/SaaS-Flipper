# Virtual Operating Partner — telemetry & action capabilities

Turn the LLM into a virtual operating partner: **you provide capital + decisions; Claude runs the
telemetry, flags the leaks, and drafts the optimization playbooks.** Each capability works **today** on
a CSV / export via a committed script, and uses **live MCP** (Stripe, Postgres, PostHog/Mixpanel, AWS,
repo access) when those tools are connected.

> **Access model (hard rule):** read-only analysis by default. Any **write** — billing-tier change, DB
> update, email dispatch — requires **explicit user approval**. Claude's job is to read → isolate →
> simulate → *draft the execution script*, then stop and ask. A bad regex on a billing table can
> trigger mass cancellations. Never auto-execute.

## 1. Cohort & churn matrix
- **Goal:** find *where* users leave — early (onboarding problem) vs late (utility problem).
- **Live MCP:** query Stripe subscription/invoice events or the subscriptions table.
- **Offline:** `python3 scripts/cohort_churn.py --csv subs.csv` → MoM retention heatmap + early/late
  churn read. (CSV: `customer_id, signup_date, churn_date` — churn_date blank = still active.)

## 2. Grandfathered-account pricing scanner
- **Goal:** find users drastically underpaying vs. the value they extract.
- **Live MCP:** cross-ref billing tier with usage logs.
- **Offline:** `python3 scripts/grandfathered_scan.py --billing billing.csv --usage usage.csv` → flags
  e.g. "legacy $19/mo plan, top-5% usage," suggests a target tier, and lists accounts so you can have
  Claude **draft** (not send) a targeted migration email. Approve before any send.

## 3. Live Rule-of-40 / health scorecard
- **Goal:** know the asset's financial health + exit-multiple trajectory at a glance.
- **Live MCP:** pull live revenue growth + opex (cloud, APIs, contractors).
- **Offline:** `python3 scripts/scorecard.py --mrr ... --growth ... --margin ...` → Rule of 40, LTV:CAC,
  NRR vs `config/guardrails.md`, with lever recommendations when a metric misses (cut nodes, raise price).

## 4. Competitive intel & add-on scouter
- **Goal:** build a pipeline of cheap bolt-on targets and track rivals.
- **Tooling:** WebSearch/WebFetch over Product Hunt / AlternativeTo / GitHub for abandoned or solo-dev
  micro-SaaS in-niche; evaluate tech-stack fit (guardrail §D); **draft** cold acquisition outreach.
  (See also `competitor-study.md` for the positioning side.)

## 5. Tech-debt & OSS-license audit
- **Goal:** quantify cleanup cost and protect IP before you buy or sell.
- **Live MCP / repo access:** review source + dependencies → map architectural bottlenecks, flag
  restrictive licenses (GPL/AGPL) that threaten a sale, estimate dev-hours to clean up.
- **Offline:** ask the user for the dependency manifest (package.json / requirements.txt) and review it.

## Degradation rule
If a needed MCP tool or repo isn't connected, **say what you'd pull and why**, then fall back to the
offline script or ask the user to paste the export. Never pretend to have data you can't see.
