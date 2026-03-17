Here are the 5 complete variations for Round 7.

---

## V-01 — Role Sequence: Finance → Operations → Commerce
**Axis**: Single — role sequence (Finance-first)
**Hypothesis**: Finance-first breaks natural order (Ops → Finance → Commerce). Operations must cite Finance's pre-declared PO SLA as the immutable contract from a non-adjacent predecessor; Commerce must cite [A-04] (Finance boundary checks) even though [A-07] (Operations) immediately precedes it — maximally stressing the non-adjacent citation chain.

**Scenario**: Retail procurement pipeline — PO creation/AP accrual (Finance) → goods receipt/WMS update (Operations) → catalog availability sync (Commerce)

**Key structural moves**:
- [A-01] declares PO-to-availability staleness SLA before any stage; immutability append per SC-5
- [A-02] INCUMBENT BASELINE (manual AP/receiving process) anchors the `Fall back to [A-02] if [condition]` formula in [A-12]
- [A-05] PHASE GATE 1 and [A-08] PHASE GATE 2 are first-class registry rows in the ARTIFACT REGISTRY table (C-25)
- Commerce's `Citing:` line must name [A-04] explicitly because it is non-adjacent (C-26)
- [A-12] requires the exact formula structure; loose prose citation fails (C-27)

---

## V-02 — Output Format: Table-based blocks (Operations → Commerce → Finance)
**Axis**: Single — output format (markdown table per stage and boundary block)
**Hypothesis**: Rendering stage blocks as `Field | Value | Notes` tables and boundary blocks as `Field | Value` tables makes column presence machine-verifiable — C-12, C-21, and SC-2 compliance reduces to "does column exist + is it populated." Natural order is Ops → Finance → Commerce; Commerce before Finance is non-natural, forcing Finance to cite Commerce's accumulated elapsed.

**Scenario**: E-commerce returns pipeline — return authorization/OMS reversal (Operations) → platform inventory restock/availability (Commerce) → credit memo/GL reversal (Finance)

**Key structural moves**:
- SC-7 explicitly prohibits labeled field lists; tables are the only acceptable format
- Finance is last and must cite [A-04] (Operations, non-adjacent) alongside [A-07] (Commerce)
- Phase gate artifacts [A-05] and [A-08] appear as registry rows; gates include a table-format audit of boundary blocks

---

## V-03 — Phrasing Register: Conversational/guiding (Commerce → Finance → Operations)
**Axis**: Single — phrasing register (conversational "Here is what you need to produce...")
**Hypothesis**: Conversational tone can enforce all 27 criteria as reliably as formal/imperative phrasing if constraint identifiers (PR-x instead of SC-x) are maintained and inline callbacks are preserved. Commerce-first (canonical R6 non-natural ordering) with a different domain provides a new citation stress test.

**Scenario**: Vendor marketplace payment clearing — invoice submission/payment auth (Commerce) → AP ledger/bank settlement (Finance) → vendor portal update/fulfillment release (Operations)

**Key structural moves**:
- PROTOCOL RULES section uses plain-English descriptions but assigns PR-x identifiers that are referenced inline
- The guiding voice ("Think of the boundary block as a gate you have to pass through") enforces SC-2 semantics without formal prohibition language
- `Fall back to [A-02] if [condition]` formula preserved verbatim in [A-12] instructions despite conversational register elsewhere

---

## V-04 — Role Sequence + Inertia Framing (Operations → Commerce → Finance)
**Axes**: Combined — non-natural ordering (Commerce before Finance) + prominently featured manual incumbent
**Hypothesis**: Foregrounding REPLEN_TRACKER.xlsx as the named incumbent and requiring SC-7 (every role must reference it substantively) makes the C-27 recovery formula and C-15 closure more structurally demanding — not just the recovery role but every role must engage with the manual baseline.

**Scenario**: Store replenishment sync — DC pick/dispatch (Operations) → store receiving/POS availability (Commerce) → GL inventory cost posting (Finance)

**Key structural moves**:
- [A-02] INCUMBENT BASELINE describes REPLEN_TRACKER with concrete failure modes before any role
- SC-7 requires substantive REPLEN_TRACKER mention in every role, not just [A-12]
- [A-13] TRADE-OFF ANALYSIS must compare against REPLEN_TRACKER's twice-daily cadence explicitly
- Finance cites [A-04] (Operations, two roles prior) as a non-adjacent predecessor

---

## V-05 — Lifecycle Emphasis + Output Format: Risk score column (Finance → Operations → Commerce)
**Axes**: Combined — extra-explicit lifecycle with phase risk summaries + `Risk score: 1–5` column in boundary checks
**Hypothesis**: Adding an ordinal risk score column (derived from the SC-5 table: freshness verdict × error handling quality) extends the binary C-21 verdict into a risk-weighted gate, allows [A-12] to order recovery prescriptions by urgency, and provides a richer phase gate audit trail (C-23/C-25) than a binary tick-list.

**Scenario**: Procurement-to-POS pricing pipeline — vendor cost feed/price model (Finance) → store distribution/label print (Operations) → POS price activation/e-commerce sync (Commerce)

**Key structural moves**:
- SC-5 defines a precise risk-score formula (1–5) derived from freshness × error handling — no judgment required
- Phase gates [A-05] and [A-08] include a `Highest risk score in this role: N at [boundary]` row; next role's Citing line must acknowledge it
- Finance-first + Commerce-last is maximally non-natural; Commerce must cite [A-04] (Finance, non-adjacent) explicitly
- [A-12] sorts prescriptions by risk score descending; Risk 4–5 items require time-to-recover estimates

---

All five variations are written to the rubric file at `simulations/quest/rubrics/flow-dataflow-rubric-v7-R7-2026-03-14.md`. Each satisfies the full 27-criterion rubric: the ARTIFACT REGISTRY pre-registers phase gate artifacts as first-class rows (C-25), the role ordering is designed so at least one downstream role must cite a non-adjacent predecessor with an explicit `Citing:` line (C-26), and the recovery role instructions specify the `Fall back to [A-02] if [condition]` formula as a structural requirement rather than an example (C-27).
