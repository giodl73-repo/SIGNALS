Written to `simulations/quest/golden/topic-echo-variate-R7-2026-03-16.md`.

---

## Round 7 Variations Summary

**Design context**: v7 rubric added two new criteria — C-21 (Enforcement Pipeline Staging) and C-22 (Synthesis Verdict Commitment). All five variations build on the R6 best state (C-01..C-20 active).

---

### V-01 — Pipeline Staging Axis (C-21)
**Single axis**: Lifecycle emphasis — three distinct pipeline positions with named failure classes.
- **PRE-GATE** (Step 1b): namespace diversity check before any entry validation. Failure class: *collection-level monoculture* — invisible per-entry, only visible across the full candidate set.
- **ENTRY-GATE** (Step 3): existing multi-stage epistemic gate, now labeled by position.
- **POST-GATE** (Step 6b): exhaustive N*(N-1)/2 pairwise redundancy check. Failure class: *degree-variant pairs* — each passes individually, redundancy only detectable across entries.

**Hypothesis**: The model has a structural map of which pipeline position runs which check and why no other position could catch the same failure — C-21 PASS condition met explicitly.

---

### V-02 — Synthesis Verdict Commitment Axis (C-22)
**Single axis**: Output format — binary verdict contracts in all verdict-bearing synthesis sections.
- **Step 1c** (new): signal coverage meta-reflection — COMPLETE | INCOMPLETE; hedged FAIL list; no-verdict = INCOMPLETE by default.
- **Step 8**: cross-signal synthesis ends with ECHOES PRESENT | ECHOES ABSENT; ≥3 hedged-language forms explicitly named as FAIL.

**Hypothesis**: Every synthesis section resolves to a binary state unconditionally — the model cannot produce a compliant output without committing to COMPLETE or ECHOES PRESENT rather than "appears sufficient."

---

### V-03 — Phrasing Register Axis (embedded directive)
**Single axis**: Replace formal declaration blocks with inline `[PRE-GATE]` / `[POST-GATE]` / `[ENTRY-GATE]` position callouts embedded in step instructions. Same structural constraints as V-01 but via direct imperatives: "Check X now. Failure class: Y. Cannot be caught at Z."

**Hypothesis**: Tests whether pipeline staging (C-21) survives register change — whether a model executing terse directives applies the same structural discipline as one executing formal declaration blocks.

---

### V-04 — Combination: C-21 + C-22
**Both new criteria simultaneously**. PRE-GATE and POST-GATE from V-01 + verdict commitment blocks in Steps 1c and 8 from V-02.

**Hypothesis**: C-21 and C-22 are orthogonal — pipeline position (when checks run) vs. verdict form (what terminal states are valid). No interaction; scores additively.

---

### V-05 — Full Combination with Inertia Framing
**C-21 + C-22 + inertia framing**. Adds a **Belief Inventory** (Step 1d) — the pre-investigation assumption set as the "Competitor Set." Each surprise must defeat a named Competitor Belief. The echo verdict becomes **COMPETITOR BELIEFS DEFEATED / SURVIVE** rather than ECHOES PRESENT/ABSENT.

**Hypothesis**: Naming the Competitor Set explicitly reinforces C-21 (PRE-GATE becomes a belief-inventory anchor), C-22 (verdict = competitor defeated or not), C-10 (delta tracing is automatic: old belief = competitor, correction = the defeat), and C-15 (correction register is structurally embedded via "Competitor Belief" field in every entry). The inertia frame is the only axis here that affects multiple criteria simultaneously.
