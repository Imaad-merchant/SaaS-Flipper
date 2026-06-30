# The 30-Day Value-Extraction SOP

The repeatable playbook to run the moment you acquire (or get the keys to) an asset. Goal:
unlock the trapped value an "engineer brain" founder left on the table, then relist at a higher
multiple. Each block is sequential; don't skip the audit.

## Days 1–5 — Audit the stack & SDE
- Extract every third-party dependency, API integration, and infrastructure cost. Special
  attention to **LLM/API token spend** — it scales with usage and silently eats margin.
- Recompute **SDE** with real (not seller-claimed) costs; find the add-backs and the leaks.
- Map owner-dependency: list everything the previous owner did by hand each week.
- Baseline the metrics (run `scripts/saas_metrics.py`) so you can prove the lift at resale.

## Days 6–15 — Clean code & core user flow
- Upgrade out-of-date packages; optimize the worst database queries; remove dead code.
- Apply a standard, clean UI layer (e.g. Tailwind/React/Next.js component system) — buyers and
  users both pay for "looks maintained."
- **Crush onboarding friction.** Target **Time-to-Value (TTV) under 60 seconds** and signup →
  core "Aha!" in **under 3 clicks**. This is the single highest-ROI fix; most indie apps die in
  Activation, not Acquisition.

## Days 16–20 — Retention email automation
- Plug in automated lifecycle email (Loops, Resend, or ActiveCampaign).
- Minimum sequence: **Day 1** quick-win tips → **Day 3** feature highlights → **Day 7** soft
  upsell / annual-discount offer. Retention compounds the multiple more than new signups do.

## Days 21–25 — Optimize tiers & pricing
- **Re-anchor the pricing page.** Shift entry tiers up to market rate; add a high enterprise
  **anchor** tier on the left so the standard tier reads cheap; use **charm pricing** ($49 not $50).
- **Kill LTDs and grandfathered/unmonetized legacy tiers.** Transition everyone toward clean
  monthly/annual recurring. (The Bannerbear lesson: raising $9→$49 *lowered* churn — low prices
  attract high-support bargain hunters; serious users want a sustainable price.)
- Where the asset is a thin/horizontal AI tool, apply the **"Different not Better"** pivot from
  `growth-and-marketing.md` (vertical ICP + usage/outcome-based pricing) before relaunch.

## Days 26–30+ — Relaunch & resale prep
- Relaunch publicly (changelog, "build in public" post, Product Hunt if warranted).
- Assemble the resale package: **transparent Stripe metrics** + a written **SOP document** so the
  next buyer inherits a turnkey, low-owner-dependency asset.
- List on Acquire.com / Microns.io. A clean data room + SOP commands a **premium multiple** — see
  `exit-and-resale.md`.

> Track the before/after of every metric you touch. The resale pitch *is* the delta: "TTV 4 min →
> 40s, churn 7% → 3%, MRR $200 → $600, fully documented." That delta is what justifies the new multiple.
