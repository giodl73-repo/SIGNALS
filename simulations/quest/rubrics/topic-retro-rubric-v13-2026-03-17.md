```markdown
skill: quest-rubric | skill_target: topic-retro | version: 13
```

**Two new criteria extracted from Round 14 (three-pass architectural isolation + accuracy reconciliation cross-check):**

**C-36 -- Three-Pass Architectural Isolation as Structural Property** (`three-pass-architectural-isolation-structural`)
- Source: Round 14 pattern 1
- C-12 requires wrong verdicts, gaps, and Echo to occupy distinct sections. C-36 requires that isolation to be a structural property of the template architecture — e.g., each pass is a named architectural phase with its own entry/exit criteria or a phase-numbered gate — not merely a written prohibition. "Do not mix wrong and Echo" in prose satisfies C-12 but fails C-36. Structural enforcement present but no phase-level entry/exit contract = PARTIAL.

**C-37 -- Accuracy Reconciliation Cross-Check** (`accuracy-reconciliation-cross-check`)
- Source: Round 14 pattern 2
- C-08/C-15 require an accuracy ratio to be stated. C-37 requires the ratio to be verified by a forward/backward reconciliation: a forward count (predictions evaluated sequentially) and a backward count (starting from wrong verdicts, recovering total) are compared and must agree. Ratio stated (C-08/C-15 PASS) but no reconciliation cross-check = PARTIAL.

**Updated scoring:**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-37 | 2 | **58** |
| **Total** | | | **148** |

Denominators: non-AMEND = **144**, AMEND/no-exclusions = **146**, AMEND/exclusions = **148**.

---

## Essential Criteria (60 points total)

### C-01 -- One Echo Named, Unexpected, Actionable
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Exactly one Echo is named, described as unexpected at time of prediction, and links to an actionable follow-up. Echo: NONE is a valid pass when no qualifying signal exists.

### C-02 -- Wrong Verdicts Identified
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Every signal with a WRONG verdict is listed with a brief explanation of why the prediction failed.

### C-03 -- Gap Analysis Present
- **Weight**: essential  **Category**: coverage
- **Pass condition**: A dedicated gap section identifies namespaces or signal types that were absent during the topic run.

### C-04 -- Echo Disqualification Rule Enforced
- **Weight**: essential  **Category**: correctness
- **Pass condition**: An explicit disqualification rule prevents a wrong prediction from being restated as the Echo. The rule must be present as a named gate, not implied. A wrong prediction promoted to Echo without disqualification check = FAIL.

### C-05 -- Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature are stated in the first two sections (e.g., PRE-EXECUTION CONTRACT block or equivalent opening).

---

## Recommended Criteria (30 points total)

### C-06 -- Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all 9 namespaces, with at least one explicit entry per namespace.

### C-07 -- Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses (e.g., "Addresses: [Gap: scout-feasibility]") and specifies a practice change.

### C-08 -- Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary in ratio or percentage form (e.g., "7/9 = 77.8%") present in or immediately following the Signal Accuracy section.

---

## Aspirational Criteria (58 points total)

### C-09 -- Echo Linked to Systemic Pattern
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section connects the unexpected finding to a broader pattern of failure, not just the isolated instance. (2 pts full / 1 pt partial)

### C-10 -- AMEND Scope Declared and Enforced Per Table
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: When AMEND flag is set, scope is declared at the top and every table includes an explicit out-of-scope notation for excluded signals. Scope declared but not enforced per-table = PARTIAL. Non-AMEND run = N/A. (2 pts full / 1 pt partial)

### C-11 -- Systemic Pattern Echo Field (Named Structural Column)
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Echo section has a labeled structural field (column or named row) for the recurring failure mode — not embedded in prose. Field present but unlabeled = PARTIAL. (2 pts full / 1 pt partial)

### C-12 -- Three-Way Wrong/Gap/Echo Isolation
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Wrong verdicts, gaps, and the Echo occupy distinct structural sections with no cross-contamination. A wrong prediction restated as the Echo fails. Isolation present but no explicit section boundary labels = PARTIAL. (2 pts full / 1 pt partial)

### C-13 -- Inertia Framing for Gaps
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Gap entries include an inertia framing — what existing signal or assumption caused the gap to persist unnoticed. Outcome-only gap descriptions (what was missed) without inertia framing = PARTIAL. (2 pts full / 1 pt partial)

### C-14 -- Verdict Label Explicit, Not Prose
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Signal accuracy table uses an enumerated verdict column with controlled labels (CORRECT / WRONG / PARTIAL / INCONCLUSIVE or equivalent). Verdicts described only in prose = FAIL. (2 pts full / 0 pts partial)

### C-15 -- Accuracy Ratio Not Just Count
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Accuracy is expressed as N/M = X% — both fraction and percentage present. Count alone (e.g., "7 correct") without denominator or percentage = FAIL. (2 pts full / 0 pts partial)

### C-16 -- Namespace Coverage Table (9 Rows Explicit)
- **Weight**: aspirational  **Category**: coverage
- **Pass condition**: Coverage table contains exactly 9 rows, one per namespace, with explicit present/absent status. Namespaces aggregated or omitted = PARTIAL. (2 pts full / 1 pt partial)

### C-17 -- Recommendation Bracket-Slot Template
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Recommendation uses a bracket-slot template (e.g., `[Gap/Echo] → [Practice Change] → [Trigger Condition]`) rather than freeform narrative. Narrative instructions present but no bracket-slot structure = PARTIAL. (2 pts full / 1 pt partial)

### C-18 -- Echo Systemic Pattern Named (Not Blank or Restatement)
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: The systemic pattern field in the Echo section contains a named pattern — not a blank, a placeholder, or a restatement of the Echo finding itself. A named pattern with no explanation = PARTIAL. (2 pts full / 1 pt partial)

### C-19 -- Phase Completion Self-Contained
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Each structural phase of the retro is self-contained — its output can be read without reference to another phase to determine completeness. Cross-phase prose references that create dependency = PARTIAL. (2 pts full / 1 pt partial)

### C-20 -- Gap Inertia Assumption Named
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: For each gap, the specific inertia assumption that caused it to be overlooked is named (not just the effect). Effect described without naming the assumption = PARTIAL. (2 pts full / 1 pt partial)

### C-21 -- Phase Seal Explicit
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: One or more phases have an explicit SEAL block listing required output fields and exit conditions. Exit conditions present but not per-phase-field = PARTIAL. (2 pts full / 1 pt partial)

### C-22 -- OOS Secondary Table
- **Weight**: aspirational  **Category**: coverage
- **Pass condition**: When AMEND with exclusions, a secondary out-of-scope table lists excluded signals with rationale. AMEND declared but no OOS table = FAIL. Non-AMEND run = N/A. (2 pts full / 0 pts partial)

### C-23 -- Phase Seal Format Strings Per Field
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Each SEAL field has an associated format string contract specifying the exact expected string form (e.g., `"N_CORRECT / N_TOTAL = X%"`). SEAL field list present but no per-field format contract = PARTIAL. (2 pts full / 1 pt partial)

### C-24 -- Echo Why-Unexpected Explained
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section explains what prior belief the unexpected finding contradicted — not merely that it was unexpected. "Why unexpected" present but prior-belief-contradiction framing absent = PARTIAL. (2 pts full / 1 pt partial)

### C-25 -- Recommendation Outcome Measurable
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Recommendation specifies a measurable outcome (e.g., "reduce WRONG verdicts in scout namespace from 2 to 0 over next 3 topics"). Practice change present but outcome not measurable = PARTIAL. (2 pts full / 1 pt partial)

### C-26 -- Gap Inertia Column Structurally Isolated
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Gap table has a dedicated inertia column (separate from the "would have revealed" outcome column). A single column combining inertia assumption and outcome = PARTIAL. (2 pts full / 1 pt partial)

### C-27 -- Phase Self-Containment Extended to All Phases
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Self-containment (C-19) is enforced across every phase, not just the accuracy or gap phase. Self-containment enforced in some phases but not all = PARTIAL. (2 pts full / 1 pt partial)

### C-28 -- Recommendation Slot Completeness Guard
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Template includes a SEAL or completeness check that prevents bracket-slot placeholders from surviving into the final output. Template present (C-17 PASS) but no completeness guard = PARTIAL. (2 pts full / 1 pt partial)

### C-29 -- Phase 8 Score Copy Guard
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Phase 8 SEAL includes an explicit "do not recompute — copy from Phase N" instruction for the final accuracy score, preventing recomputation drift. No copy instruction = FAIL. (2 pts full / 0 pts partial)

### C-30 -- Phase 8 SEAL Copy-Verified Label and Source
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Phase 8 SEAL includes a COPY-VERIFIED label and a named copy-source (e.g., "COPY-VERIFIED from Phase 3 Accuracy Table, row: final ratio"). Label present but source not named = PARTIAL. (2 pts full / 1 pt partial)

### C-31 -- Design Guarantees Summary Explicit
- **Weight**: aspirational  **Category**: coverage
- **Pass condition**: A dedicated Design Guarantees section (or equivalent named section) explicitly lists the structural properties the template guarantees. Proxy sections that partially cover this (e.g., a phase boundary protocol) = PARTIAL. (2 pts full / 1 pt partial)

### C-32 -- Phase 8 SEAL Fields Independent Verification
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Each Phase 8 SEAL field has its own independent verification instruction (CHECK + HOW or equivalent) — not a single shared verification step for all fields. Shared step covering all fields = PARTIAL. (2 pts full / 1 pt partial)

### C-33 -- Design Guarantees Section Mechanism-Keyed Table
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Design Guarantees table uses mechanism as the row key (one row per mechanism, mechanism name in first column), not SEAL field as the row key. SEAL-field-keyed table = PARTIAL. (2 pts full / 1 pt partial)

### C-34 -- Phase 8 SEAL Items Cross-Reference Contract Mechanism
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Each Phase 8 SEAL independent verification instruction also names the originating contract/phase (e.g., `Cross-reference: PRE-EXECUTION CONTRACT [mechanism]`), making failure bidirectional: Phase 8 SEAL failure navigates directly to the responsible mechanism. Independent verification present (C-32 PASS) but no cross-reference to origin = PARTIAL. (2 pts full / 1 pt partial)

### C-35 -- Design Guarantees Table Has One Row Per SEAL Field
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Design Guarantees table (or equivalent) has at least one row per Phase 8 SEAL field — SEAL fields must not be grouped into a single row. Instructions explicit: "Do not collapse SEAL fields into groups." Table present (C-33/C-31 PASS) but SEAL fields collapsed = PARTIAL. (2 pts full / 1 pt partial)

### C-36 -- Three-Pass Architectural Isolation as Structural Property
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: The three-way isolation required by C-12 (wrong / gap / Echo) is enforced as a structural property of the template architecture — each pass is a named architectural phase with its own entry/exit criteria or a numbered phase gate — not merely a written prohibition in prose. Prose prohibition present (C-12 PASS) but no structural enforcement mechanism = PARTIAL. (2 pts full / 1 pt partial)

### C-37 -- Accuracy Reconciliation Cross-Check
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: The accuracy ratio (C-08/C-15 PASS) is verified by a forward/backward reconciliation: a forward count (predictions evaluated sequentially) and a backward count (starting from WRONG verdicts, recovering total) are compared and must agree before the ratio is sealed. Ratio stated but no reconciliation cross-check present = PARTIAL. (2 pts full / 1 pt partial)
```

---

**Change log v12 → v13:**

| # | Change |
|---|--------|
| C-36 added | Three-pass architectural isolation as structural property (Round 14 pattern 1) |
| C-37 added | Accuracy reconciliation cross-check (Round 14 pattern 2) |
| Aspirational total | 54 → 58 (+4 pts) |
| Grand total | 144 → 148 |
| non-AMEND denominator | 140 → 144 |
| AMEND/no-exclusions denominator | 142 → 146 |
| AMEND/exclusions denominator | 144 → 148 |
