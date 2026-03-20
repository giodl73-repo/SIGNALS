## /quest:score — rhythm-track R1

### Scoring Method

No trace artifact available. Evaluating each variation as a **prompt design**: will this design reliably produce output that passes each criterion? Scale: PASS / PARTIAL (structurally present but relies on model compliance without mechanical enforcement) / FAIL.

Point weights: Essential 12 pts each (60 total), Recommended 10 pts each (30 total), Aspirational 5 pts each (10 total). PARTIAL = 0.5 × full credit.

---

## V-01 — Table-Based Verification

**Axis**: Output format — Phase 3 as a multi-column table instead of free-form blocks.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Phase 2 table with explicit D-ID rows, "Every edge from Phase 1 becomes one row." |
| C-02 | PASS | Phase 3 verification TABLE, "No row may be skipped. If a paper cannot be read, mark every cell 'UNREADABLE'." |
| C-03 | PARTIAL | "Count your P1 rows now. This count must appear verbatim in Phase 5 and in the artifact frontmatter." Instruction present but no reconciliation table — model must manually track from Phase 4 to Phase 5, count drift still possible. |
| C-04 | PASS | "BROKEN requires at least one P1 violation; PARTIAL requires at least one P2 gap and no P1; SOUND requires no P1 and no P2." |
| C-05 | PASS | All six frontmatter fields listed explicitly. |
| C-06 | PASS | Four transfer types defined with descriptions, column required in table. |
| C-07 | PASS | "[Name the paper, name the section, state the exact change]" + "if they can't make the change from Fix 1 alone, the fix is too generic." |
| C-08 | PASS | "List D-IDs that must be resolved before the next paper in the track can be submitted. State 'none' only when P1 = 0 and P2 = 0." |
| C-09 | PASS | IMPLICITLY column value + "IMPLICIT citation note: add a one-sentence note on whether implicit use is sufficient for a reviewer." |
| C-10 | PASS | "Modification justified?" column with YES/NO/N/A and column-rule explanation. |

**Essential**: 4.5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (4.5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **94**
**all_essential_pass**: FALSE (C-03 PARTIAL)

---

## V-02 — Lifecycle Emphasis: Hard Gates + Reconciliation

**Axis**: Pre-flight checklist gate at Phase 1, block count at Phase 3, explicit reconciliation step before Phase 5.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Phase 2 table with D-ID rows, "Total dependencies: [n]" count recorded. |
| C-02 | PASS | "Pre-phase check: Confirm you have the count from Phase 2. You must produce exactly that many blocks." + "Blocks written: [n] — must equal Total dependencies from Phase 2." |
| C-03 | PASS | Explicit reconciliation step: "Recount every P1 row in this table: P1 count = [n]... These exact numbers go into Phase 5 and the artifact frontmatter." Structural enforcement, not just instruction. |
| C-04 | PASS | "Integrity derivation (show your work): P1 violations = [n] -> [BROKEN if >0, else continue]." Derivation made visible. |
| C-05 | PASS | All frontmatter fields listed. |
| C-06 | PASS | Transfer types referenced; definitions available. |
| C-07 | PASS | "(a) the paper, (b) the section, (c) the exact change." Edge case handled: "If P1 violations = 0, Fix 1 addresses the highest-severity P2 gap. State this explicitly." |
| C-08 | PASS | "D-IDs blocking submission: [list or 'none']." |
| C-09 | PASS | "Cited? YES / NO / IMPLICITLY" + "Implicit note: [if IMPLICITLY: is implicit use sufficient for a reviewer?]" in block template. |
| C-10 | PASS | "Mod. justified? YES / NO / N/A" in block template. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**
**all_essential_pass**: TRUE

---

## V-03 — Conversational Auditor Voice

**Axis**: Phrasing register — question-answer framing, imperative commands → direct questions.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Step 2 table with D-ID rows. |
| C-02 | PASS | Step 3 question-answer per D-ID, "Work through every D-ID. Do not skip any." |
| C-03 | PARTIAL | "Before moving on: count your P1 rows. Write the number here. You'll need it again." Writing inline is stronger than V-01's instruction, but still no structural count enforcement table. Count drift between Step 4 and Step 5 still possible. |
| C-04 | PASS | "(BROKEN if any P1; PARTIAL if P2 but no P1; SOUND if neither)" inline in the health block. |
| C-05 | PASS | Frontmatter fields listed. |
| C-06 | PASS | Transfer type options listed with descriptions. |
| C-07 | PASS | Template: "In [paper], section [§X.Y]: [exactly what to change]" + "specific enough that a co-author can act on it without reading this report first." |
| C-08 | PASS | "What must be fixed before the next paper in the track can be submitted? [List the D-IDs, or 'nothing — track is ready']." |
| C-09 | PASS | "(YES — named explicitly / IMPLICITLY — uses the result but doesn't name it)" + "would a reviewer expect an explicit citation here, or is implicit use acceptable?" Richer question framing. |
| C-10 | PASS | "If MODIFIED: does the paper explain why it changed the form? (YES / NO / NOT ADDRESSED)" — "NOT ADDRESSED" is more nuanced than N/A (surfacing when the paper neither confirms nor denies justification). |

**Essential**: 4.5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (4.5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **94**
**all_essential_pass**: FALSE (C-03 PARTIAL)

---

## V-04 — Combined: Table-First + Hard Gates

**Axes**: Output format (table) + Lifecycle emphasis (gates, reconciliation).

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Phase 2 table, "One row per dependency edge. Complete all cells before proceeding." + "Row count checkpoint: Total dependency rows = [n]." |
| C-02 | PASS | Phase 3 verification TABLE + "Completeness check: Count rows filled = [n]. Must equal Phase 2 row count." Two structural checkpoints. |
| C-03 | PASS | Reconciliation TABLE in Phase 4 with explicit P1/P2/P3 row counts + "Copy these exact numbers into Phase 5 and the frontmatter. Do not recount." Strongest structural enforcement across all variations. |
| C-04 | PASS | Explicit IF-THEN derivation: "IF P1 violations > 0 THEN BROKEN; ELSE IF P2 gaps > 0 THEN PARTIAL; ELSE SOUND → Track integrity: [derive]." |
| C-05 | PASS | Frontmatter fields listed. |
| C-06 | PASS | Four transfer types defined with descriptions, column required. |
| C-07 | PASS | "exact change — specific enough to act on without reading this report" + edge case: "Fix 1 (P1 or highest-severity P2 if P1 = 0)" explicitly handled. |
| C-08 | PASS | "D-IDs that must be resolved: [list or 'none — track is ready']." |
| C-09 | PASS | "Implicit note" as a dedicated column in Phase 3 table alongside IMPLICITLY value. |
| C-10 | PASS | "Mod. justified?" column with YES/NO/N/A. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**
**all_essential_pass**: TRUE

---

## V-05 — Two-Pass (Mapper + Skeptic) + Formal Register

**Axes**: Role sequence (adversarial second pass) + Formal register.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | M-2 Dependency Map table with D-ID rows. |
| C-02 | PASS | M-3 verification blocks per D-ID (Mapper) + Skeptic review blocks per D-ID + Final Register table — three layers covering every dependency. |
| C-03 | PASS | "P1 count: [n] — record this number exactly." in Final Register. The Skeptic pass also improves P1 identification accuracy: SATISFIED verdicts are actively challenged, reducing the risk of missed P1s that inflate the count. |
| C-04 | PASS | Explicit BROKEN/PARTIAL/SOUND rules with conditions. Plus: "Skeptic escalations (Mapper SATISFIED -> Skeptic VIOLATED/PARTIAL): [list D-IDs or 'none']" — unprecedented traceability of verdict changes. |
| C-05 | PASS | Frontmatter fields listed. |
| C-06 | PASS | Transfer types listed in M-2. |
| C-07 | PASS | "(1) paper, (2) section, (3) exact change required." AND: "If an amendment requires coordinated changes across multiple papers (e.g., a P1 violation where both source and target must change), list all affected locations." Only variation to address multi-paper fixes. |
| C-08 | PASS | Critical path in Track Health section + Skeptic escalations field identifies which D-IDs changed severity. |
| C-09 | PASS | "Cited? YES / NO / IMPLICITLY" in both Mapper and Skeptic blocks. Challenge B ("Is the source paper cited in related work but absent from sections where the structural result should actually appear?") directly operationalizes the IMPLICIT case. |
| C-10 | PASS | "Mod justified? YES / NO / N/A" in M-3. Challenge C ("Does the target paper use different variable names or notation? If so, is the equivalence stated explicitly?") specifically targets unjustified MODIFIED cases in Skeptic pass. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**
**all_essential_pass**: TRUE

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Score | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 4.5/5 | 3/3 | 2/2 | 94 | NO |
| V-02 | 5/5 | 3/3 | 2/2 | 100 | YES |
| V-03 | 4.5/5 | 3/3 | 2/2 | 94 | NO |
| V-04 | 5/5 | 3/3 | 2/2 | 100 | YES |
| V-05 | 5/5 | 3/3 | 2/2 | 100 | YES |

**Ranked**: V-04 = V-02 = V-05 (100) > V-01 = V-03 (94)

**What separated 100 from 94**: C-03 (P1 count enforcement). V-01 and V-03 instruct the model to count but provide no structural mechanism to verify the count transfers correctly from Phase 4 to Phase 5. The reconciliation step (V-02) and reconciliation table (V-04) eliminate this failure mode mechanically.

**Best overall design**: V-04 — it combines the widest set of structural defenses: table format prevents row skipping, row-count checkpoint locks Phase 2 completeness, Phase 3 completeness check locks Phase 3 coverage, and the reconciliation table locks the P1/P2/P3 counts before they enter Phase 5 or frontmatter.

**Most distinctive contribution**: V-05 — the Skeptic's three named challenge probes (silent divergence, citation-without-use, terminology drift) operationalize the hardest-to-catch failure mode: P1 violations hidden behind a correct-looking citation. The escalation tracker and multi-paper AMEND guidance are unique.

---

## Excellence Signals

Patterns from top-scoring variations that produced the score improvements:

1. **Reconciliation table with explicit copy instruction** (V-04): A dedicated count table at the end of Phase 4 listing P1/P2/P3 row counts, with "Copy these exact numbers... Do not recount" — removes the need for the model to recount and eliminates inter-phase drift.

2. **Layered completeness checkpoints** (V-04): Three independent structural checks (Phase 2 row count, Phase 3 row count, Phase 4 reconciliation) rather than a single reminder — each layer catches failures the previous one might miss.

3. **Named Skeptic challenge probes** (V-05): Replacing a generic "check again" instruction with three specific adversarial probes (silent divergence, citation-without-use, terminology drift) gives the Skeptic pass clear targets and prevents it from rubber-stamping Mapper verdicts.

4. **Multi-paper AMEND guidance** (V-05): Explicitly noting that a P1 violation may require coordinated changes across both source and target papers — most single-paper AMEND templates would miss this, producing incomplete fixes.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Reconciliation table with explicit copy instruction (Copy these exact numbers, Do not recount) mechanically prevents P1 count drift between Phase 4 and Phase 5 without relying on model memory", "Layered completeness checkpoints at Phase 2 row count, Phase 3 completeness check, and Phase 4 reconciliation table provide structural defense against skipped dependencies across three independent gates", "Named Skeptic challenge probes (silent divergence, citation-without-use, terminology drift) operationalize adversarial verification — replacing generic re-check with specific failure-mode targets that surface P1 violations single-pass audits normalize away", "Multi-paper AMEND guidance for coordinated P1 fixes (where both source and target must change) prevents incomplete fix prescriptions for the hardest violation class"]}
```
