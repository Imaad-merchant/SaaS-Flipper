# The Master Playbook — the end-to-end flipping plan

This is the operating system. Every individual reference is a chapter; this is the whole book.
A flip moves through **5 stages with a hard decision gate between each**. Never advance a gate on
hope — advance on evidence. If a gate fails, you either renegotiate or walk. There is always
another deal.

```
 SOURCE → [Gate 1] → DILIGENCE → [Gate 2] → BUY → GROW (90d) → [Gate 3] → EXIT → RECYCLE
```

## Stage 0 — Set up (before you shop)
- Define your **buy-box** and **capital plan**: max purchase price + a reserve for the 90-day
  improvement + a cushion. Never spend your whole bankroll on the acquisition.
- Pick 1–2 niches you can understand and write content for.
- Stand up a deal pipeline tracker (Sourced → Screened → Diligence → Offer → Closed).
- **Detail:** `references/sourcing-and-marketplaces.md` (buy-box, capital discipline).

## Stage 1 — SOURCE
- Run the deal-flow system: marketplace alerts + off-market outreach to burnt-out solo founders.
- Apply the 30-second filter and the **Trap Filter** to kill bad deals fast (100 → 10).
- **Detail:** `references/sourcing-and-marketplaces.md`.

> **GATE 1 — Is there a wedge?** There must be an obvious, *fixable* reason it's underpriced
> (broken onboarding, no marketing, mispriced, ugly UI). No wedge → no flip → pass.

## Stage 2 — DILIGENCE & VALUE
- Demand the verified data room (Stripe/GA exports, P&L, churn cohorts, concentration, stack).
- Run `scripts/saas_metrics.py` (unit economics + SDE) and `scripts/valuation.py` (range).
- Build comps from live listings; write the **deal memo** (`templates/deal-memo.md`).
- **Detail:** `references/due-diligence.md`, `references/valuation-and-comparables.md`.

> **GATE 2 — Do the numbers verify and clear your hurdle?** Revenue is verified (not screenshots),
> churn/concentration acceptable, and the price leaves room for a profitable flip after the 90-day
> spend. Decide **BUY / PASS / COUNTER** with a number.

## Stage 3 — BUY (close cleanly)
- Agree price **and structure** (cash / earnout / seller financing — see `exit-and-resale.md`).
- Contingencies: verified Stripe access, code review, clean transfer of accounts/domains/keys.
- Get a transition-support window from the seller (e.g. 30 days).

## Stage 4 — GROW (the 90-day flip)
- Run the **30-Day Value-Extraction SOP**, then two more cycles of growth levers:
  audit & SDE → clean code + TTV <60s → retention email → re-anchor pricing/kill LTDs → relaunch.
- Fix Activation/Retention before pouring in traffic (AARRR). Apply "Different not Better" where
  the asset is thin/horizontal.
- **Track before/after on every metric** — the delta IS your resale pitch.
- Write the plan into `templates/flip-plan.md` (30/60/90, effort×impact, target exit multiple).
- **Detail:** `references/value-extraction-sop.md`, `references/growth-and-marketing.md`.

> **GATE 3 — Is it list-ready?** 3+ months of stable/growing verified MRR · churn down & proven ·
> owner-dependency removed (SOP written) · pricing migration complete. If not, keep improving or
> hold — don't list a fragile spike.

## Stage 5 — EXIT & RECYCLE
- Package the data room + SOP; pick the marketplace/broker; list at a comps-justified ask.
- Sell the **story and SOP**, not just the spreadsheet; cultivate multiple buyers; be willing to walk.
- After close: **recycle the capital** into Stage 0 with the lessons learned.
- **Detail:** `references/exit-and-resale.md`, `templates/exit-prospectus.md`.

## The portfolio mindset (this is a repeatable machine)
One flip is a project; a **system of flips** is the business. Run several assets at staggered
stages (one sourcing while another grows while a third lists) so capital and attention stay
deployed. Keep a written log of every deal's thesis, the lift you created, and the realized
return — your filters get sharper each cycle, and pattern recognition is the real edge.

## Risk rules (never break these)
1. **Verify revenue independently** — no live Stripe/analytics, no deal.
2. **Keep a reserve** — never spend the bankroll you need to actually grow the asset.
3. **Pass fast, often** — rejecting 99% is the job; one bad buy erases several good flips.
4. **No wedge, no buy** — if you can't name the lift, you're a holder, not a flipper.
5. **Document as you go** — the SOP you write during the flip is the asset you sell at exit.
