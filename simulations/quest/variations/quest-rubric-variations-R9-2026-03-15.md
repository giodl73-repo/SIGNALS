Written to `simulations/quest/golden/quest-rubric-variate-v9-R09-2026-03-16.md`.

---

## quest-rubric R9 Batch 2 — V-01 through V-05

**Batch context:** Batch 1 (2026-03-15) used inertia-framing, output-format, lifecycle-emphasis. Batch 2 covers the two untouched axes plus a fresh inertia angle.

---

### V-01 — Role Sequence: Auditor Pre-Declaration *(single axis)*

**axis:** role-sequence
**hypothesis:** Inserts an `### AUDITOR-PRE [C-NN]` phase *before* the Author Phase. The Auditor reads the skill spec and declares per-position acceptance thresholds (PASS evidence / PARTIAL evidence / acceptance threshold boundary) before any criterion is drafted. The Author then writes each criterion with explicit `Auditor-Pre alignment` fields in INERTIA-RECORD and a `PARTIAL-CONDITION` field in CALIBRATION-PAIR grounded in the pre-declared threshold.

**Potential C-35 candidate:** per-position `### AUDITOR-PRE [C-NN]` block that makes the PARTIAL-credit boundary auditable before the criterion is written. If no new signal: post-hoc Auditor review is sufficient for C-23 compliance and pre-declaration is redundant.

**Structural additions over R8 V-05:**
- INVARIANT C (Auditor-Pre must precede Author Phase)
- Phase 0 skeleton includes `### AUDITOR-PRE [C-NN]` headings
- Auditor Pre-Declaration Gate before Author Phase
- CALIBRATION-PAIR gains `PARTIAL-CONDITION` field
- Auditor Phase Audit Table gains `Pre-Dec Alignment` column (YES/DRIFT)

---

### V-02 — Phrasing Register: Conversational Imperative *(single axis)*

**axis:** phrasing-register
**hypothesis:** All `CONSTRAINT:` / `INVARIANT A:` / `PRECONDITION for:` / `DEFINITION (most critical):` labels replaced with plain directive prose. "CONSTRAINT: DO NOT proceed" → "Don't continue until this is done." Rule A / Rule B instead of INVARIANT A / B. Structural contract is **identical** to R8 V-05 — same mechanisms, gates, heading patterns, formula guard.

**Regression probe:** C-27 (DISCRIMINATES-BETWEEN named structural blocks) and C-28 (DEPENDS_ON declarations) require scannable named blocks. If removing formal *label vocabulary* causes those blocks to lose their heading patterns (e.g., they become prose paragraphs without `###` headings), the scan detects the regression. If no regression: CONSTRAINT/INVARIANT vocabulary is navigational, not structural.

**Note:** CALIBRATION-PAIR STATUS-QUO field renamed `GENERIC` throughout (conversational field name); heading patterns like `### INERTIA-RECORD [C-NN]` are preserved because they are structural heading patterns from M-02, not label vocabulary.

---

### V-03 — Inertia Framing: Implicit/Unnamed Status-Quo *(single axis)*

**axis:** inertia-framing (minimal direction — removes named competitor block)
**hypothesis:** The prominent `**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."` block at the top is removed. The discrimination requirement is stated as a quality constraint only: "every pass condition must name something specific to this skill's output contract." INERTIA-RECORD and CALIBRATION-PAIR blocks are preserved but reference "a generic rubric" (implicit) rather than the named Status-Quo Rubric.

**Regression probe at C-02:** The named "THE STATUS-QUO RUBRIC" anchors the `STATUS-QUO` field to a concrete phrase. Without it, `GENERIC` fields may drift toward vague descriptions ("a rubric might say the output is organized") that lose their discrimination anchor. V-03 tests whether the named competitor is load-bearing for CALIBRATION-PAIR quality.

---

### V-04 — Role Sequence × Phrasing Register *(combination)*

**axes:** V-01 + V-02

**hypothesis:** Does the Auditor Pre-Declaration structural value depend on formal CONSTRAINT/INVARIANT vocabulary? In V-04, the `### AUDITOR-PRE [C-NN]` heading pattern is preserved (structural) but all surrounding prose is conversational. Tests: (1) does conversational register cause `### AUDITOR-PRE` blocks to lose their named heading structure? (2) does pre-declared acceptance still tighten PARTIAL-CONDITION quality when the gate language is plain directive prose?

---

### V-05 — Full Accumulation *(combination)*

**axes:** role-sequence × phrasing-register × inertia-framing (all three)

**hypothesis:** Hardest structural case: Auditor-First + conversational + unnamed Status-Quo competitor. Three compound tests:
1. Does Auditor Pre-Declaration compensate for loss of named-competitor anchoring (does `AUDITOR-PRE [C-NN]` PASS threshold serve the anchoring role that "clear, complete, well-formatted" normally provides)?
2. Does conversational register cause named-block heading patterns to degrade under compound variation?
3. Does a new compound signal emerge — specifically, the V-05 **convergence check**: does the Auditor Phase verify that the pre-declared PARTIAL boundary appears in CALIBRATION-PAIR without being mechanically copied from AUDITOR-PRE?

If compound signals emerge absent from V-01/V-02/V-03 individually → C-35 batch-2 candidates. If no compound signals → axes are independent.
