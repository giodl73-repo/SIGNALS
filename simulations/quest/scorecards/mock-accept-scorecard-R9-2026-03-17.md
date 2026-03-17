## mock-accept — Round 9 Scorecard

**Rubric:** v9 (25 aspirational; denominator 25 when C-09 present)
**Baseline:** R8 V-01 — 25/25 = 100.0 (sole golden)
**Round axis:** Three structural questions C-33 opens but doesn't mandate

---

### Criterion Matrix

All five variations carry the same structure for Essential, Recommended, and Aspirational C-09 through C-29 — all inherited cleanly from R8 V-01. The table below focuses on full evidence for axis criteria and confirms passes on remaining criteria by cluster.

#### Essential — C-01 to C-05 (all variations)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Artifact-as-subject in auto-flag rules | PASS | PASS | PASS | PASS | PASS |
| C-02 Forbidden triad completeness | PASS | PASS | PASS | PASS | PASS |
| C-03 CANARY ASSERTION + SUPPRESSED branch | PASS | PASS | PASS | PASS | PASS |
| C-04 Single Write block | PASS | PASS | PASS | PASS | PASS |
| C-05 Slot 1 / Slot 2 separation, paraphrase named | PASS | PASS | PASS | PASS | PASS |

Evidence cluster: STANDING RULE with exact PASS/FAIL forms, HALT + Delete + Rewrite three-step; auto-flag output templates use artifact-as-subject form throughout; STEP 7 has structurally separated Slot 1 (Reason Code) and Slot 2 (Coverage Basis) with "paraphrase is a violation in both slots" named; STEP 9 writes all four sections in ONE Write call; CANARY ASSERTION with `___` blank + CANARY SUPPRESSED branch in STEP 6.

#### Recommended — C-06 to C-08 (all variations)

| ID | All V-01..V-05 |
|----|---------------|
| C-06 Entity-naming in roles | PASS — `Required artifact citation: "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]"` in STEP 3 and STEP 4; CONSTRAINT + HALT |
| C-07 Named accumulators + empty-list acknowledgment | PASS — `Arch-blocked: []` initialized; VERDICT-ECHO per REAL-REQUIRED; `Arch-blocked: none` if empty; mirrored for Strategy-blocked |
| C-08 5-field REAL-REQUIRED template + VERDICT-ECHO | PASS — trigger condition / SQ / Artifact state / Verdict / Reason / Cost-of-MOCK / Required action; VERDICT-ECHO named |

#### Aspirational — C-09 to C-29 (all variations — bulk pass)

All five variations carry the complete R8 V-01 structure unchanged for these criteria. Evidence summary:

| Range | Status | Evidence basis |
|-------|--------|----------------|
| C-09 Artifact-as-subject grammar | PASS ×5 | STANDING RULE at top; all auto-flag and role templates enforce artifact-as-subject form throughout |
| C-10 Tier sourcing | PASS ×5 | STEP 1 CONSTRAINT: exact format `"Tier: N (source: TOPICS.md \| --tier \| default)"` with source label; HALT if absent |
| C-11 Inline completeness gate | PASS ×5 | GATE A (count = 9), GATE B (partition sums to 9), GATE C (count = 9 - auto-flagged), GATE D (count = GATE C MOCK-ACCEPTED); all named with count assertions and HALT |
| C-12 Reason-code enforcement at point of use | PASS ×5 | CONSTRAINT co-located at Verdict and Reason fields in STEP 3 and STEP 4; not preamble-only |
| C-13 Phase exit assertions | PASS ×5 | "Do not proceed to STEP N until GATE X is written" at GATE A, B, C, D, E-COST, E, F |
| C-14 Blank-line failure signal | PASS ×5 | `___` blanks throughout all fill-in sites; no `[bracket]` notation |
| C-15 Forbidden-form enumeration | PASS ×5 | STANDING RULE enumerates: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…" |
| C-16 Written-gate blocking language | PASS ×5 | All phase exit gates include "Do not proceed to STEP N until GATE X is written" |
| C-17 Named gate registry | PASS ×5 | GATE A, B, C, D, E-COST, E, F — stable sequential IDs referenceable across phases |
| C-18 Adjacent framed CONSTRAINT co-location | PASS ×5 | Every constrained field followed by indented standalone `CONSTRAINT:` block |
| C-19 Universal blank-slot enforcement | PASS ×5 | Auto-flag output templates and CANARY ASSERTION all use `___` blanks |
| C-20 Halt-on-violation instruction | PASS ×5 | STANDING RULE: "HALT. Delete the violating line. Rewrite in PASS form." — explicit stop action |
| C-21 Per-section CONSTRAINT in review Write block | PASS ×5 | STEP 9 has CONSTRAINT + HALT for each of the 4 sections (Coverage, Structural records, Risk, Next Steps) |
| C-22 Slot 1 paraphrase violation examples | PASS ×5 | STEP 7 Slot 1 revert-on-violation: `"sufficient coverage"` and `"domain realistic"` as concrete quoted examples |
| C-23 Three-step halt sequence | PASS ×5 | STANDING RULE: `HALT. Delete the violating line. Rewrite in PASS form.` — three atomic imperatives |
| C-24 Gate-to-section traceability in GATE F | PASS ×5 | GATE F: "All four sections confirmed: Coverage / Structural records / Risk / Next Steps" — named by stable IDs |
| C-25 Slot 2 paraphrase violation examples | PASS ×5 | SLOT 2 VIOLATION TABLE with 3 quoted near-miss forms in STEP 7 |
| C-26 Halt co-location at each CONSTRAINT site | PASS ×5 | Every CONSTRAINT block throughout all phases has an adjacent `HALT.` instruction |
| C-27 GATE F as standalone dedicated numbered step | PASS ×5 | STEP 10 is a separate dedicated step; GATE F fires after the STEP 9 Write call returns |
| C-28 Slot 2 violation table | PASS ×5 | SLOT 2 VIOLATION TABLE: two-column `Quoted near-miss form \| Violation type` in STEP 7 |
| C-29 Cost-of-MOCK field in evaluation record | PASS ×5 | Cost-of-MOCK field in STEP 3 and STEP 4 with constrained format: `"Without real data for [namespace], [specific type] remains unvalidated by production evidence at Tier [N]."` |

#### Aspirational — Axis Criteria C-30 to C-33 (per-variation)

##### C-30 — DEFAULT DECISION POSITION as pre-phase inertia anchor

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Prose-form DEFAULT DECISION POSITION block before STEP 1; "MOCK-ACCEPTED is an earned escape requiring a named positive argument against inertia"; STEP 3 header references DEFAULT DECISION POSITION | PASS |
| V-02 | Same prose-form DEFAULT DECISION POSITION as R8 V-01; identical C-30 satisfaction | PASS |
| V-03 | DECISION SCOREBOARD before STEP 1: `REAL-REQUIRED: 9 (all namespaces begin here — this is inertia)` / `MOCK-ACCEPTED: 0 (nothing earned yet)`; "MOCK-ACCEPTED is earned against named evidence"; "This scoreboard governs STEP 3 and STEP 4"; STEP 3 header references "DECISION SCOREBOARD applies" | PASS — named block before STEP 1 declaring REAL-REQUIRED as default with earned-against-inertia framing |
| V-04 | Same prose-form DEFAULT DECISION POSITION as R8 V-01 | PASS |
| V-05 | DECISION SCOREBOARD identical to V-03; adds "GATE E-COST verifies the final register split matches the phase-gate totals" in preamble | PASS |

##### C-31 — INERTIA LEDGER at phase gates

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | INERTIA LEDGER — ARCHITECT PHASE EXIT at GATE C (still at REAL-REQUIRED / earned MOCK-ACCEPTED; sum constraint + HALT); INERTIA LEDGER — STRATEGY PHASE EXIT at GATE D | PASS |
| V-02 | Same as V-01; no change to GATE C or GATE D structure | PASS |
| V-03 | INERTIA LEDGER blocks present at both gates; V-03 adds DECISION SCOREBOARD UPDATE and DECISION SCOREBOARD FINAL alongside — these augment but do not replace the INERTIA LEDGER blocks | PASS |
| V-04 | Same as V-01; no change to gate blocks | PASS |
| V-05 | INERTIA LEDGER blocks present at both gates; DECISION SCOREBOARD UPDATE at GATE C and DECISION SCOREBOARD FINAL at GATE D add numeric movement tracking; sum constraint `REAL-REQUIRED + MOCK-ACCEPTED = 9` added at GATE D | PASS |

##### C-32 — MOCK COST REGISTER as dedicated post-evaluation step

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | STEP 5 dedicated step; COST REGISTER ASSERTION count; GATE E-COST; table with Phase cell constraint; positioned after GATE D before STATUS WRITEBACK | PASS |
| V-02 | STEP 5 identical to V-01 for table structure; GATE E-COST enhanced with per-phase assertions but register step itself is still dedicated with COST REGISTER ASSERTION | PASS |
| V-03 | STEP 5 uses Namespace \| Phase \| Cost-of-MOCK (same as R8 V-01); GATE E-COST same as R8 V-01 (total count only) | PASS |
| V-04 | STEP 5 dedicated; Phase-first table; enhanced GATE E-COST | PASS |
| V-05 | STEP 5 dedicated; Phase-first table; enhanced GATE E-COST | PASS |

##### C-33 — COST REGISTER phase-dimension column

| Variation | Table format | Cross-verification mechanism | Verdict |
|-----------|-------------|------------------------------|---------|
| V-01 | `Phase \| Namespace \| Cost-of-MOCK` (Phase-first); Phase cell constrained to exactly "Architect" or "Strategy"; Architect rows before Strategy rows by explicit instruction | Phase column present; Phase-first grouping makes per-phase count scannable by consecutive rows; C-33's column inspection property satisfied and improved | PASS |
| V-02 | `Namespace \| Phase \| Cost-of-MOCK` (same as R8 V-01); Phase cell constrained | Phase column present (R8 V-01 form); GATE E-COST adds three-line assertion: total rows / Architect rows vs GATE C INERTIA LEDGER / Strategy rows vs GATE D INERTIA LEDGER — cross-verification made mandatory, not just possible | PASS |
| V-03 | `Namespace \| Phase \| Cost-of-MOCK` (same as R8 V-01); Phase cell constrained | Phase column present; same cross-verification path as R8 V-01 | PASS |
| V-04 | `Phase \| Namespace \| Cost-of-MOCK` (Phase-first; Architect rows before Strategy rows); GATE E-COST three-line per-phase assertion | Phase-first grouping + mandatory per-phase verification — strongest C-33 expression of single-axis variations | PASS |
| V-05 | `Phase \| Namespace \| Cost-of-MOCK` (Phase-first; Architect rows before Strategy rows); GATE E-COST three-line per-phase assertion | Phase-first grouping + mandatory per-phase verification + scoreboard traces movement from initial state declaration through GATE E-COST confirmation | PASS |

---

### Composite Scores

All five variations carry C-09 → denominator = 25.

| Variation | Asp passes | Asp score (×10) | Essential all pass | Recommended all pass | Total |
|-----------|------------|-----------------|-------------------|---------------------|-------|
| **V-01** | 25/25 | 10.0 | Yes | Yes | **100.0** |
| **V-02** | 25/25 | 10.0 | Yes | Yes | **100.0** |
| **V-03** | 25/25 | 10.0 | Yes | Yes | **100.0** |
| **V-04** | 25/25 | 10.0 | Yes | Yes | **100.0** |
| **V-05** | 25/25 | 10.0 | Yes | Yes | **100.0** |

**All five variations: 100.0. R9 confirms the v9 rubric ceiling is stable at 25/25.**

---

### Ranking

All five are co-golden at 100.0. Rank order reflects structural completeness of the audit chain, not score difference:

1. **V-05** — Full integration: Phase-first + numeric scoreboard + GATE E-COST phase-split. Complete audit chain: inertia declared numerically → tracked at each gate → aggregated by phase in register → verified at GATE E-COST against both INERTIA LEDGER values. Adds FINAL sum constraint (REAL-REQUIRED + MOCK-ACCEPTED = 9) at GATE D.
2. **V-04** — Phase-first + GATE E-COST phase-split. Register column order makes phase grouping scan-countable; GATE E-COST makes the count mandatory. C-33's cross-verification path is closed.
3. **V-02** — GATE E-COST phase-split only. Converts C-33's structural possibility into a mandatory per-phase verification without changing column order.
4. **V-01** — Phase-first column only. Grouping by Phase-first makes per-phase row count readable by scan. Column order preference proved not to affect any criterion.
5. **V-03** — Numeric scoreboard only. DECISION SCOREBOARD satisfies C-30 equally to prose form. Adds FINAL sum constraint at GATE D but does not close the GATE E-COST per-phase verification gap.

**R9 answers:**
1. C-33 does not require column ordering. Phase-first (V-01) and Namespace-first (R8 V-01) both pass. Column order is a presentation preference.
2. GATE E-COST per-phase split (V-02) converts C-33 cross-verification from possible to required. This is a distinct quality improvement not yet encoded as a criterion.
3. Numeric scoreboard (V-03) satisfies C-30 as fully as prose form and adds observable inertia movement tracking — but the form is not mandated by any existing criterion.

---

### Excellence Signals from V-05

**Pattern 1 — Phase-first register grouping as scan-countable phase audit**
V-05 orders `Phase | Namespace | Cost-of-MOCK` with Architect rows before Strategy rows by explicit HALT-backed instruction. The phase-split count becomes verifiable by reading consecutive rows rather than filtering a middle column. C-33 requires the Phase column; V-05 adds row ordering that makes the count trivially scannable without parsing.

**Pattern 2 — GATE E-COST per-phase verification closing the C-33 audit loop**
V-05's GATE E-COST fires three assertions: total row count, Architect rows vs GATE C INERTIA LEDGER count, Strategy rows vs GATE D INERTIA LEDGER count — each with HALT if mismatch. C-33 makes column inspection possible; this gate makes it required. Structural possibility becomes mandatory verification without adding a new step.

**Pattern 3 — Numeric scoreboard with live gate-exit updates and FINAL sum constraint**
V-05's DECISION SCOREBOARD (REAL-REQUIRED: 9, MOCK-ACCEPTED: 0) is not a static prose declaration — it updates at GATE C and fires a constrained FINAL (REAL-REQUIRED + MOCK-ACCEPTED = 9) at GATE D. The evaluator can read inertia state as a live counter rather than inferring it from prose. The FINAL sum constraint makes the evaluation phase self-closing: a mis-routed namespace surfaces immediately rather than at writeback.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase-first row ordering in COST REGISTER with explicit Architect-before-Strategy instruction makes per-phase row count scan-countable by consecutive rows rather than column filtering", "GATE E-COST per-phase split assertions (Architect rows vs GATE C INERTIA LEDGER; Strategy rows vs GATE D INERTIA LEDGER) convert C-33 structural cross-verification possibility into mandatory verification with HALT on mismatch", "Numeric DECISION SCOREBOARD with live phase-gate updates (GATE C update + GATE D FINAL with REAL-REQUIRED + MOCK-ACCEPTED = 9 sum constraint) makes inertia movement observable as a running counter throughout evaluation rather than a prose declaration"]}
```
