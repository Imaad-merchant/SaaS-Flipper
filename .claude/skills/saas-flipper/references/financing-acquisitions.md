# Financing Acquisitions — fund the buy without draining your bankroll

The pros rarely pay 100% cash from their own pocket. They build a **capital stack** — a blend of
sources — so they can do more deals and keep a reserve for the 90-day improvement. (Risk Rule #2:
never spend the money you need to actually grow the asset.)

## The capital stack (combine, don't pick one)
| Source | Typical role | Notes |
|--------|--------------|-------|
| **Your cash** | The down payment + improvement reserve | Keep a cushion; don't go all-in. |
| **Seller financing** | 25–30% down, remainder paid over time w/ interest | The workhorse of small deals — see below. |
| **Earnout** | Defer part of price, paid on the asset hitting targets | Bridges valuation gaps; aligns risk. |
| **SBA loan** | Larger, cash-flowing deals (US) | Cheap but slow + paperwork; needs real EBITDA. |
| **Revenue-based financing** | Fast, repaid as a % of revenue | Alternative lenders win on speed for micro deals. |
| **Investor capital / holdco** | Scaling to a portfolio | Raise once you have a track record. |

> Smart acquirers use a **capital stack, not one silver bullet.** Typical micro-SaaS pricing is
> **~2×–4× EBITDA/SDE** (or ~2–4× ARR) — small enough that seller financing + your cash often closes
> it with no bank involved.

## Seller financing (your best friend on the buy side)
- Buyer pays a portion upfront in cash — **typically 25–30%** — and pays the rest as a **note** with
  interest over time.
- Makes deals possible when you can't (or don't want to) finance the full amount, and **bridges a
  valuation gap** between what the seller wants and what you'll pay today.
- Win-win: you pay less interest than a bank loan and preserve cash for growth; the seller gets a
  higher effective price plus interest, and stays mildly incentivized for a clean handover.
- **Negotiation lever:** offering seller financing can *increase* the price the seller accepts,
  because you've de-risked their side — use it to win competitive deals or shave the cash price.

## Earnouts (bridge the gap, share the risk)
- Part of the price is paid later, contingent on performance after close.
- **Customer-Retention Earnout** fits SaaS perfectly: payment tied to keeping a defined % of the
  customer base over a set period — directly hedges the churn risk you're underwriting.
- Keep earnout **targets inside your control**, **cap the term**, and define measurement precisely so
  it can't be gamed by either side.

## Buy-side structuring principles
1. **Minimize cash out of pocket, maximize reserve.** Down payment + improvement budget + cushion.
2. **Push risk onto the future** with seller notes and earnouts when the asset is unproven to you.
3. **Use a holdback** (10–15% in escrow, 60–90 days) so a post-close churn cliff or hidden cost comes
   out of the seller's proceeds, not your pocket.
4. **Model the full cost**, not just the sticker: price + transfer costs + the 90-day improvement
   spend + your time. The flip only works if projected resale clears all of it with margin
   (`scripts/valuation.py --target-mrr` projects this).
