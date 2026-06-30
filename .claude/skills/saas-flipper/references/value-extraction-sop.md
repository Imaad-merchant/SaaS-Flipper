# Value Extraction — organized by cash-flow × complexity (sub-$5k lean)

The repeatable playbook to unlock the value an "engineer brain" founder left on the table, then relist
at a higher multiple. For a sub-$5k asset, **forget the calendar** — there is no "100-day plan" and no
team. Order work by **immediate cash-flow impact vs. complexity**, and obey the **Minimum Sellable
Product** rule: if the software reliably solves a boring problem, don't burn months refactoring — fix
monetization and distribution, then flip.

## Step 0 — Baseline (do once, first)
- Extract every dependency, API integration, and infra cost. Watch **LLM/API token spend** — it scales
  with usage and silently eats margin.
- Run `scripts/saas_metrics.py` and `scripts/scorecard.py` to baseline the metrics so you can **prove
  the lift** at resale. Recompute **SDE** with real (not seller-claimed) costs.
- Map owner-dependency: list everything the founder did by hand each week.

## Quick-Wins — high cash impact, low complexity (do these now)
- **Infra downsizing:** indie apps over-provision Vercel/AWS/Supabase. Drop to a lean $5–10/mo tier,
  kill heavy logs and dead staging envs. Instant margin on a low-revenue asset. *(VOP: `cohort_churn`
  not needed here; check the cloud bill.)*
- **"Anti-Free" pivot:** delete or hard-gate any "forever free" tier draining the DB. Set a **$19–$29/mo
  floor** to filter for serious buyers.
- **Pricing re-anchor:** shift entry tiers to market rate; add a high anchor tier so the standard tier
  reads cheap; charm pricing ($49 not $50). Model the churn hit against guardrail §C (≤5%).
- **Grandfathered migration:** run `scripts/grandfathered_scan.py`, then **draft** (not send) targeted
  emails moving underpayers to a value-based tier. Approve before sending.

## Growth-Loops — compounding, variable complexity
- **Feature-gate the "Aha":** lock the single highest-usage utility behind Pro. (Find it via usage logs.)
- **Crush onboarding friction:** target **TTV < 60s**, signup → core value in **< 3 clicks**. Most
  indie apps die in Activation, not Acquisition.
- **Retention lifecycle email** (Loops/Resend): Day 1 quick-win tips → Day 3 feature highlights → Day 7
  soft annual-discount upsell. Retention lifts the multiple more than new signups.
- **One repeatable channel (solo scale):** Claude drafts ~25 personalized 1:1 outbound touches/day on
  LinkedIn/X to a niche list; re-engagement emails to churned/abandoned signups.
- **The wedge:** apply the "different, not better" positioning from `competitor-study.md`.

## Exit-Prep — package for resale
- Relaunch publicly (changelog / build-in-public).
- Assemble the data room: **verified Stripe metrics** + a written **SOP** so the buyer inherits a
  turnkey, low-owner-dependency asset. List per `exit-and-resale.md`.

> The resale pitch *is* the delta. Track before/after on everything you touch: "TTV 4 min → 40s, churn
> 7% → 3%, MRR $200 → $600, hosting $40 → $8, fully documented." That delta justifies the new multiple.
