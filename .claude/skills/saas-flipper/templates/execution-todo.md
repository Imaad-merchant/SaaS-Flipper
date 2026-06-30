# Execution To-Do — {{asset_name}}

The full step-by-step list, in order. Grouped by **cash-flow × complexity**, NOT calendar dates. Do
Quick-Wins first (they fund everything else), then Growth-Loops, then Exit-Prep. Check items off as you
go. Anything marked ✋ needs YOUR approval before execution (human-in-the-loop).

## 0. Baseline (do once, first)
- [ ] Get verified access: Stripe/analytics export, repo/codebase, hosting console
- [ ] Run `scripts/saas_metrics.py` and `scripts/scorecard.py` → record the starting numbers
- [ ] Run `scripts/cohort_churn.py` → note early vs late churn
- [ ] List every weekly task the founder did by hand (owner-dependency)

## 1. Quick-Wins — high cash impact, low complexity
- [ ] **Infra downsizing:** audit cloud bill; kill dead staging + heavy logs; move to a lean $5–10/mo tier
- [ ] **Kill/gate "forever free":** set a $19–$29/mo floor
- [ ] **Pricing re-anchor:** new tiers + anchor tier + charm pricing (model churn ≤ guardrail §C) ✋
- [ ] **Grandfathered migration:** `scripts/grandfathered_scan.py` → review flagged list → draft emails ✋
- [ ] Cancel overlapping/unused vendor subscriptions

## 2. Growth-Loops — compounding, medium complexity
- [ ] **Feature-gate the "Aha"** utility behind Pro
- [ ] **Onboarding:** TTV < 60s, signup → core value in < 3 clicks
- [ ] **Lifecycle email:** Day 1 tips → Day 3 features → Day 7 annual-discount upsell
- [ ] **One outbound channel:** ~25 personalized 1:1 touches/day (Claude drafts, you send) ✋
- [ ] **Apply the wedge:** ship the "different not better" positioning across site + onboarding
- [ ] (Optional) **Bolt-on scout:** `references/vop-telemetry.md` §4 → pipeline of cheap add-ons

## 3. Exit-Prep — package for resale
- [ ] 3+ months of stable/growing verified MRR; churn proven down (re-run scorecard)
- [ ] Write the **SOP** (how the business runs week to week) → kills owner-dependency
- [ ] Assemble the data room (verified metrics, P&L, transfer checklist — `references/closing-and-legal.md`)
- [ ] Generate the investor deck: `scripts/build_deck.py --content deck-content.json --out deal.pptx`
- [ ] List on Acquire.com / Microns.io at a comps-justified ask (`references/exit-and-resale.md`)

## Tracking — the resale story is the delta
| Metric | Start | Now | Target |
|--------|-------|-----|--------|
| MRR | | | |
| Churn (mo) | | | |
| Hosting $/mo | | | |
| TTV | | | |
| Rule of 40 | | | |
