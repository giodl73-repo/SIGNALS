Now I have everything needed to score. Let me work through each variation systematically.

---

## Round 9 Scoring — `topic-report` (Rubric v9)

### Scoring Basis

All five variations share the same neutral base. They satisfy **C-01 through C-27** (5 essential + 3 recommended + 19 aspirational) identically. The only discriminators are **C-28**, **C-29**, and **C-30** — the three v9-new axes tested in pairwise and triple combinations.

**Composite formula (v9):**
```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/22 × 10)
```

---

### Per-Criterion Evaluation

#### Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Artifact written and path echoed | PASS | PASS | PASS | PASS | PASS |
| C-02 | Progress table with accurate counts | PASS | PASS | PASS | PASS | PASS |
| C-03 | Open signals listed with owners | PASS | PASS | PASS | PASS | PASS |
| C-04 | Readiness statement calibrated | PASS | PASS | PASS | PASS | PASS |
| C-05 | Recommended next step present | PASS | PASS | PASS | PASS | PASS |

**Evidence**: All variations include PHASE 1 DISCOVER → PHASE 2 PRE-COMPUTATION → SLOT 1–4 write sequence → PHASE 4 CONFIRM with path echo. Identical structural coverage across all five specs.

**Essential pass: 5/5 for all variations.**

---

#### Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | `--format teams` produces compact ASCII card | PASS | PASS | PASS | PASS | PASS |
| C-07 | Content matches topic-status output | PASS | PASS | PASS | PASS | PASS |
| C-08 | Open signals include signal type and namespace | PASS | PASS | PASS | PASS | PASS |

**Evidence**: Branch B in all variations carries the full four-section ASCII card template (`+--[ TOPIC REPORT ]`, `PROGRESS`, `OPEN SIGNALS`, `READINESS`/`NEXT STEP`) with 40-line / 80-char constraints. SLOT 2 enumerates `{namespace}/{skill-type}` per open signal.

**Recommended pass: 3/3 for all variations.**

---

#### Aspirational Criteria C-09 through C-27 — All Variations (Shared Base)

All five variations carry the full R8 neutral base, which passes every criterion in this range. Brief evidence:

| ID | Pass Condition Met | Evidence Location |
|----|-------------------|-------------------|
| C-09 | Readiness sentence names BLOCKERS | `{names from LOCKED BLOCKERS list}` in SLOT 3 write instruction |
| C-10 | Backtick, `<`, `>` explicitly named | `[RULE G-8 VERIFICATION]: Prohibited characters named by character: backtick (\`), less-than (<), greater-than (>)` |
| C-11 | BLOCKERS pre-computation block | Step 2b emits `BLOCKERS:` block before any write phase |
| C-12 | Teams card passes character-level scan | ASCII-only template: `+ - |` borders; no markdown syntax in card body |
| C-13 | COMPLETENESS / EXCLUSIVITY named separately | `G-7a COMPLETENESS` and `G-7b EXCLUSIVITY` as distinct invariant labels in Step 2c and at write point |
| C-14 | Branch sealing instruction | `[RULE BRANCH-SEAL]` at dispatch point and `[RULE BRANCH-SEAL-B]` at Branch B entry — dual-position isolation |
| C-15 | BLOCKERS LOCK directive | Step 2d: standalone "The BLOCKERS list from step 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase." |
| C-16 | In-render verification scan | `G-7a COMPLETENESS SCAN` + `G-7b EXCLUSIVITY SCAN` steps execute before readiness sentence in both Branch A and Branch B |
| C-17 | Rules co-located at governed positions | `[RULE SLOT1-SOURCE]` at SLOT 1, `[RULE SLOT2-SOURCE]` at SLOT 2, `[RULE G-7a/G-7b]` at SLOT 3, `[RULE G-9 INERTIA]` at SLOT 4 |
| C-18 | Three-layer co-location at write point | SLOT 3 carries DECLARE (`[RULE G-7a/G-7b]`) + ANCHOR (LOCKED BLOCKERS reference) + VERIFY (scan steps) at the same structural position |
| C-19 | Contract label chaining (register → annotation → scan header) | `G-7a`/`G-7b` assigned in register, propagated to `[RULE G-7a COMPLETENESS]`/`[RULE G-7b EXCLUSIVITY]` annotations and `G-7a COMPLETENESS SCAN`/`G-7b EXCLUSIVITY SCAN` headers |
| C-20 | Worked example in each `[RULE]` annotation | Correct/violation pairs embedded at SLOT 3 rules (both G-7a and G-7b) and at SLOT 4 `[RULE G-9 INERTIA]` |
| C-21 | Inertia framing at NEXT STEP | `[RULE G-9 INERTIA]` present at SLOT 4; stall cost clause `"Leaving this open holds the topic at Not Ready."` in both correct example and write instruction |
| C-22 | Explicit THREE-LAYER WRITE POINT header (Branch A) | `=== THREE-LAYER WRITE POINT ===` header with LAYER 1/2/3 enumeration at SLOT 3 in Branch A |
| C-23 | Criterion-tagged violation in `[RULE]` | SLOT 4 violation text ends with `(... -- C-21 violation)` in all variations (V-01/V-02/V-04 carry the compound `G-9 INERTIA / C-21 violation`; V-03/V-05 carry `C-21 violation` alone — C-23 passes regardless since C-21 criterion ID is present) |
| C-24 | Contract label chaining for single-position invariants | `G-9 INERTIA` assigned in register; propagated to `[RULE G-9 INERTIA]` annotation at SLOT 4 — two-level chain (register → annotation) appropriate for single-position invariant |
| C-25 | Branch B independent THREE-LAYER header | `=== THREE-LAYER WRITE POINT (BRANCH B) ===` with LAYER 1/2/3 enumeration present in all five Branch B sections |
| C-26 | Dual-chain co-presence at governed annotation slot | `[RULE G-9 INERTIA]` (register-path) co-present with `(... -- C-21 violation)` (rubric-path) at the same SLOT 4 annotation across all variations |
| C-27 | Dual-branch three-layer closure | Both C-22 (Branch A header) and C-25 (Branch B header) present — neither execution path requires cross-branch lookup |

**Aspirational C-09–C-27 pass: 19/19 for all variations.**

---

#### Aspirational Criteria C-28, C-29, C-30 — Discriminator Evaluation

**C-28 — Dual-identifier violation example**
*Pass condition*: Violation text at SLOT 4 carries both the register label (G-9 INERTIA) and the rubric criterion ID (C-21) as a single compound fragment.

| Variation | Violation text | Result |
|-----------|---------------|--------|
| V-01 (A+B) | `(no stall cost -- G-9 INERTIA / C-21 violation)` — both identifiers present as one fragment | **PASS** |
| V-02 (A+C) | `(no stall cost -- G-9 INERTIA / C-21 violation)` — both identifiers present as one fragment | **PASS** |
| V-03 (B+C) | `(no stall cost -- C-21 violation)` — C-21 only; G-9 INERTIA absent from violation text | **FAIL** |
| V-04 (A+B+C) | `(no stall cost -- G-9 INERTIA / C-21 violation)` — both identifiers present as one fragment | **PASS** |
| V-05 (neutral) | `(no stall cost -- C-21 violation)` — C-21 only; G-9 INERTIA absent from violation text | **FAIL** |

---

**C-29 — Explicit named recovery directive in Branch B header**
*Pass condition*: Branch B THREE-LAYER header contains an explicit recovery instruction naming both the recovery action and the prohibited alternative.

| Variation | Branch B THREE-LAYER header content | Result |
|-----------|-------------------------------------|--------|
| V-01 (A+B) | Includes `Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.` | **PASS** |
| V-02 (A+C) | Ends at `LAYER 3 VERIFY` with no Recovery line | **FAIL** |
| V-03 (B+C) | Includes `Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.` | **PASS** |
| V-04 (A+B+C) | Includes `Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.` | **PASS** |
| V-05 (neutral) | Ends at `LAYER 3 VERIFY` with no Recovery line | **FAIL** |

*Note*: The Branch A THREE-LAYER header carries `Recovery: If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding.` in all five variations — this is the pre-existing recovery note for the main path (satisfies C-22 recovery intent) but does not satisfy C-29, which specifically requires the recovery directive within the Branch B header.

---

**C-30 — Slot-indexed contract register**
*Pass condition*: Each register entry carries a `[SLOT n]` or `[PHASE n]` forward annotation naming the governed output position.

| Variation | Register format | Result |
|-----------|----------------|--------|
| V-01 (A+B) | `G-1: ...`, `G-2: ...`, ..., `G-9 INERTIA: ...` — no slot annotations | **FAIL** |
| V-02 (A+C) | `G-1 [PHASE 4]: ...`, `G-2 [SLOT 1]: ...`, `G-3 [SLOT 2]: ...`, `G-4 [SLOT 3]: ...`, `G-5 [SLOT 4]: ...`, `G-6 [BRANCH B]: ...`, `G-7 [SLOT 3]: ...` with sub-entries `G-7a COMPLETENESS [SLOT 3]`, `G-7b EXCLUSIVITY [SLOT 3]`, `G-8 [BRANCH B]: ...`, `G-9 INERTIA [SLOT 4]: ...` — all entries indexed | **PASS** |
| V-03 (B+C) | Same slot-indexed format as V-02 | **PASS** |
| V-04 (A+B+C) | Same slot-indexed format as V-02 | **PASS** |
| V-05 (neutral) | `G-1: ...` through `G-9 INERTIA: ...` — no slot annotations | **FAIL** |

---

### Consolidated Criterion Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 Essential | P | P | P | P | P |
| C-02 Essential | P | P | P | P | P |
| C-03 Essential | P | P | P | P | P |
| C-04 Essential | P | P | P | P | P |
| C-05 Essential | P | P | P | P | P |
| C-06 Recommended | P | P | P | P | P |
| C-07 Recommended | P | P | P | P | P |
| C-08 Recommended | P | P | P | P | P |
| C-09 Aspirational | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | P | P |
| C-19 | P | P | P | P | P |
| C-20 | P | P | P | P | P |
| C-21 | P | P | P | P | P |
| C-22 | P | P | P | P | P |
| C-23 | P | P | P | P | P |
| C-24 | P | P | P | P | P |
| C-25 | P | P | P | P | P |
| C-26 | P | P | P | P | P |
| C-27 | P | P | P | P | P |
| **C-28** | **P** | **P** | **F** | **P** | **F** |
| **C-29** | **P** | **F** | **P** | **P** | **F** |
| **C-30** | **F** | **P** | **P** | **P** | **F** |
| **Aspirational total** | **21/22** | **21/22** | **21/22** | **22/22** | **19/22** |

---

### Composite Score Computation

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/22 × 10)

V-01: (5/5 × 60) + (3/3 × 30) + (21/22 × 10) = 60 + 30 + 9.545 = 99.5
V-02: (5/5 × 60) + (3/3 × 30) + (21/22 × 10) = 60 + 30 + 9.545 = 99.5
V-03: (5/5 × 60) + (3/3 × 30) + (21/22 × 10) = 60 + 30 + 9.545 = 99.5
V-04: (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10.000 = 100.0
V-05: (5/5 × 60) + (3/3 × 30) + (19/22 × 10) = 60 + 30 + 8.636 = 98.6
```

*Note on V-05 prediction*: The variations document predicts V-05 = 95.5. The composite formula yields **98.6**. The prediction appears to have used a non-composite formula (likely `aspirational_pass/22 × 100` applied only to the aspirational component in isolation, yielding 86.4, or a denominator mismatch). The composite formula is authoritative — 98.6 is correct.

---

### Ranking

| Rank | Variation | Axes | Asp | Score | Delta |
|------|-----------|------|-----|-------|-------|
| 1 | **V-04** | A+B+C | 22/22 | **100.0** | — |
| 2 | **V-01** | A+B | 21/22 | **99.5** | −0.5 (C-30) |
| 2 | **V-02** | A+C | 21/22 | **99.5** | −0.5 (C-29) |
| 2 | **V-03** | B+C | 21/22 | **99.5** | −0.5 (C-28) |
| 5 | **V-05** | neutral | 19/22 | **98.6** | −1.4 |

V-01, V-02, V-03 are rubric-level tied. No v9 criterion distinguishes them from each other — the three R9 new criteria are mutually orthogonal at this scoring level, exactly as predicted.

---

### Prediction Accuracy

| Variation | Predicted asp | Actual asp | Predicted score | Actual score | Match? |
|-----------|--------------|------------|----------------|--------------|--------|
| V-01 | 21/22 | 21/22 | 99.5 | 99.5 | **Confirmed** |
| V-02 | 21/22 | 21/22 | 99.5 | 99.5 | **Confirmed** |
| V-03 | 21/22 | 21/22 | 99.5 | 99.5 | **Confirmed** |
| V-04 | 22/22 | 22/22 | 100.0 | 100.0 | **Confirmed** |
| V-05 | 19/22 | 19/22 | 95.5 (predicted) | **98.6** | Asp count correct; composite differs — formula error in prediction |

All aspirational pass-counts are confirmed. V-05 composite diverges from prediction due to a formula mismatch in the prediction document; the composite formula gives 98.6.

---

### Excellence Signals from V-04

V-04 is the sole ceiling variation. Three patterns distinguish it from each pairwise competitor:

**Pattern 1 — Compound violation fragment as single recovery entry point (C-28)**
V-04 SLOT 4 violation text: `(no stall cost -- G-9 INERTIA / C-21 violation)`. V-03 carries `(no stall cost -- C-21 violation)`. The compound form places both the register label and the rubric criterion ID into one text fragment, collapsing two-hop recovery (violation text → C-21 criterion → register lookup for G-9) to one hop (violation text → both chains simultaneously). A model encountering wrong NEXT STEP output reaches the contract register and rubric invariant without a second scan. V-03 lacks this: its recovery path from bad output requires a separate register lookup to reach G-9 INERTIA.

**Pattern 2 — Procedural recovery instruction at Branch B entry (C-29)**
V-04 Branch B THREE-LAYER header includes: `Recovery: re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A.` V-02 lacks this. The recovery directive converts the structural property of Branch B self-containment (C-25: no cross-branch lookup required) into a procedural instruction encountered before any enforcement layer, naming both the recovery action and the prohibition. The distinction: C-25 makes cross-branch lookup unnecessary; C-29 makes the recovery procedure explicit at branch entry, before attention degrades across the LAYER 1/2/3 sequence.

**Pattern 3 — Slot-indexed register as forward execution map (C-30)**
V-04 CONTRACT REGISTER: every entry carries a `[SLOT n]` or `[PHASE n]` annotation (`G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, `G-1 [PHASE 4]`, etc.). V-01 carries the same register without slot annotations. The forward indexing enables a model to plan its execution arc at register-read time — before encountering any write point. This is directionally orthogonal to C-19/C-24 backward traceability (annotation → register) and to C-28 backward recovery (bad output → invariant). Axis C closes the one failure mode the other two axes do not address: incomplete planning before generation starts.

**Orthogonality confirmation**: All three mechanisms fire at structurally separate moments in the generation arc — Axis A at output-slot recovery (after wrong output), Axis B at branch-entry (before enforcement layers), Axis C at register-read (before any output slot). The pairwise combinations each leave one arc moment uncovered.

---

### R9 Finding

Predictions confirmed. The three R9 pairwise combinations (V-01, V-02, V-03) all score 99.5, confirming that C-28, C-29, and C-30 remain mutually orthogonal at the pairwise level — no criterion in C-28/C-29/C-30 implies or preconditions any of the others. V-04 (ceiling) scores 100.0, confirming the R8 V-05 22/22 design is stable.

**Candidate C-31 watch**: V-03 (B+C) is the asymmetric case — the only pairwise combination lacking the dual-identifier violation. If live runs show elevated SLOT 4 inertia errors for V-03 relative to V-01 and V-02 at identical 99.5 rubric scores, the finding names a C-31 candidate: *violation-text single-hop recovery rate for NEXT STEP errors is not substitutable by early-arc mechanisms (register forward indexing + Branch B recovery directive)*. V-02 (A+C) is the second watch: absence of C-29 exposes Branch B generation-flow errors that neither the dual-identifier nor slot indexing addresses.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["compound violation fragment as single-hop recovery entry point: violation text carrying both register label (G-9 INERTIA) and criterion ID (C-21) in one fragment collapses two-hop backward recovery to one, independent of early-arc mechanisms", "procedural recovery directive at Branch B entry converts C-25 structural self-containment into an explicit instruction naming recovery action and prohibited alternative before enforcement layers are encountered", "slot-indexed contract register creates forward execution map orthogonal to annotation-to-register backward chaining: a model reads its full execution arc from the register before encountering any write point"]}
```
