# Closing & Legal — from handshake to keys-in-hand

Stage 3 (BUY) and Stage 5 (EXIT) both run through this. A clean close protects you from fraud and
from inheriting someone else's liabilities. On platforms like Acquire.com the standard window from
**LOI signed → funds released is 30–60 days** for a clean deal (longer with earnouts/seller notes).

## The closing sequence
1. **LOI (Letter of Intent)** — *non-binding* terms: price, structure, what's included, and an
   **exclusivity/diligence window** (typically 30 days) during which the seller stops shopping.
   Use the marketplace template or your own. Signing the LOI starts the clock.
2. **Confirmatory due diligence** — verify everything claimed (see `due-diligence.md`). This is your
   window to re-trade or walk if the data doesn't match the pitch.
3. **APA (Asset Purchase Agreement)** — the *binding* contract. Unlike the LOI, these obligations are
   enforceable. Covers assets included, price & structure, reps & warranties, indemnification,
   non-compete, and transition support.
4. **Escrow** — once the APA is signed, route money + assets through an escrow service (e.g.
   Escrow.com). **Buyer wires funds → seller transfers assets → both confirm → escrow releases.**
   Neither side can run off with the asset or the cash. Always use escrow; never wire direct to a
   stranger.
5. **Transfer & confirm** — execute the transfer checklist below, both sides confirm in escrow, funds
   release, transition-support window begins.

## Asset-transfer checklist (put this IN the APA)
- [ ] Source code + repo ownership (GitHub/GitLab org transfer)
- [ ] Domain(s) + DNS + registrar transfer
- [ ] Stripe / payment processor account or clean customer-payment migration
- [ ] Customer list, database, and any PII (with a lawful basis to transfer)
- [ ] Hosting / infra accounts (AWS/Vercel/etc.) and **all API keys rotated to you**
- [ ] Third-party SaaS subscriptions and integrations
- [ ] Email / support inboxes, help-desk, docs
- [ ] Social / marketing accounts, ad accounts, analytics
- [ ] Trademarks, brand assets, content/IP
- [ ] The written **SOP** (how the business is run)

## Reps, warranties & protections to insist on
- **Reps & warranties:** seller affirms revenue is accurate, code is theirs, no undisclosed
  liabilities/litigation, customers are real and paying.
- **Indemnification:** seller covers losses from breaches of those reps (cap + survival period).
- **Holdback / escrow holdback:** retain a slice (e.g. 10–15%) for 60–90 days against
  post-close surprises (churn cliff, undisclosed costs).
- **Non-compete:** seller can't rebuild the same thing and poach your customers.
- **Transition support:** a defined window (e.g. 30 days) of seller help, in writing.

## Legal pitfalls that bite buyers
- **Wiring before escrow confirms transfer** — the classic fraud. Don't.
- **Stock vs. asset purchase** — for micro-SaaS, prefer an **asset purchase** so you don't inherit the
  entity's hidden liabilities/tax history.
- **Personal data transfer** without a lawful basis (GDPR/CCPA) — confirm the customer data can
  legally move to you.
- **Untransferable dependencies** — a critical API/account tied to the seller's identity that can't
  be reassigned. Verify transferability *before* the APA.
- **Hardcoded seller credentials** — rotate every key/secret on day one.

> Use marketplace templates as a starting point, but for anything beyond a few-thousand-dollar deal,
> have an M&A-savvy lawyer review the APA. It's cheap insurance against an expensive surprise.
