# review-design — Round 14 Scorecard
**Rubric version**: v13 (C-01 through C-42, denominator 35)
**Date**: 2026-03-15

---

## Baseline Inheritance

All five variations carry the full R13 V-01 baseline: BLOCK 0 through BLOCK 5 with F-01 through F-27 declared, all C-01 through C-40 satisfied. The R14 task is to encode C-41 (BLOCK 5 Section leftmost) and C-42 (F-28 cross-block section verification). The axis experiment is **where** C-42 enforcement lives: inline at BLOCK 5 (V-01), upstream dedicated registry (V-02/V-04/V-05), or inline pre-check enumeration (V-03).

---

## Criterion-by-Criterion Evaluation

### Essential (C-01 through C-04) — 60 pts at full pass

| # | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-01 | All 6 stock disciplines present | PASS | PASS | PASS | PASS | PASS |
| C-02 | Severity tag on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 | Domain expert auto-selection justified | PASS | PASS | PASS | PASS | PASS |
| C-04 | Consensus block present | PASS | PASS | PASS | PASS | PASS |

All variants: **4/4 essential pass** → 60.00 pts each.

---

### Recommended (C-05 through C-07) — 30 pts at full pass

| # | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-05 | Unique catches surfaced | PASS | PASS | PASS | PASS | PASS |
| C-06 | Amend pathway described | PASS | PASS | PASS | PASS | PASS |
| C-07 | Finding traceability to design section | PASS | PASS | PASS | PASS | PASS |

All variants: **3/3 recommended pass** → 30.00 pts each.

---

### Aspirational (C-08 through C-42) — 10 pts at full pass, ~0.286 pts/criterion

**Shared pass (C-08 through C-36, C-38 through C-42):**

All five variations inherit from R13 V-01 baseline. The following criteria pass uniformly:

| Criteria | Evidence | All 5 |
|----------|----------|-------|
| C-08 | BLOCK 2.5 pyramid gate with Status + Rationale column | PASS |
| C-09 | F-11 fires on empty SPLIT Synthesis cell | PASS |
| C-10 | BLOCK 2 findings in Markdown table with Sev + Section columns | PASS |
| C-11 | Three-field expert trace: Signal detected / Expert added / Reason | PASS |
| C-12 | BLOCK 2.5 as dedicated lifecycle block between findings and consensus | PASS |
| C-13 | Expert trace in table column form | PASS |
| C-14 | Named F-IDs on every mandatory block; F-01 through F-27 present | PASS |
| C-15 | BLOCK 1.5 roster commitment table before any finding block | PASS |
| C-16 | Source column (Stock/Domain) in BLOCK 1.5 | PASS |
| C-17 | F-10 fires when Domain reviewer in BLOCK 1.5 has no BLOCK 1 name match | PASS |
| C-18 | F-11 content-completeness halt on SPLIT Synthesis | PASS |
| C-19 | F-12 cross-block P1 count parity (BLOCK 2.5 anchor → BLOCK 5 row count) | PASS |
| C-20 | BLOCK 5 in 4-column+ Markdown table form | PASS |
| C-21 | BLOCK 0 pre-scan catalogue with formal SHALL constraint | PASS |
| C-22 | BLOCK 3 consensus in 4-column table (Issue/Type/Reviewers/Synthesis) | PASS |
| C-23 | Formal modal vocabulary in all block headers and F-ID triggers | PASS |
| C-24 | F-16 fires when BLOCK 4 Reviewer cell has no BLOCK 1.5 match | PASS |
| C-25 | F-17 fires when BLOCK 5 Re-run Scope names non-roster reviewer | PASS |
| C-26 | F-18 bidirectional BLOCK 0 ↔ BLOCK 1 disposal completeness | PASS |
| C-27 | F-19 fires when pyramid inversion Rationale cell empty | PASS |
| C-28 | BLOCK 4 in 3-column structural table form | PASS |
| C-29 | F-21 fires when BLOCK 0 No-Expert-Needed Reason cell empty | PASS |
| C-30 | F-22 fires when Domain reviewer in BLOCK 1.5 has no BLOCK 2 finding table | PASS |
| C-31 | F-23 fires when BLOCK 3 Issue cell empty | PASS |
| C-32 | F-24 fires when BLOCK 5 Action cell empty or placeholder | PASS |
| C-33 | F-25 fires when BLOCK 4 Finding cell empty | PASS |
| C-34 | F-26 fires when BLOCK 5 Section cell empty or placeholder | PASS |
| C-35 | F-27 fires when BLOCK 2 P1 row has empty Section cell | PASS |
| C-36 | BLOCK 2 Section column is leftmost (`Section \| Sev \| Finding`) | PASS |
| C-38 | BLOCK 0 Amendment Cost column (High/Medium/Low) | PASS |
| C-39 | BLOCK 5 Priority Rank column present | PASS |
| C-40 | PRESERVATION PRINCIPLE inertia framing declared before amend table | PASS |
| C-41 | BLOCK 5 Section column is leftmost (`Section \| Priority Rank \| P1 Finding \| Action \| Re-run Scope`) | PASS |
| C-42 | F-28 fires when BLOCK 5 Section value absent from BLOCK 2 P1 Section values | PASS |

**Evidence for C-41 and C-42 (new this round):**

- All 5 variations produce BLOCK 5 with column order `Section | Priority Rank | P1 Finding | Action | Re-run Scope` — Section leftmost before Priority Rank and P1 Finding. C-41: **PASS all**.
- All 5 declare F-28: V-01 fires against BLOCK 2 P1 rows directly; V-02/V-04/V-05 fire against BLOCK 2.7 registry; V-03 fires against inline pre-check enumeration. All three placement strategies satisfy C-42's pass condition (named halt + stated trigger + localizable mismatch identification). C-42: **PASS all**.

---

**The sole differentiator — C-37:**

| # | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-37 | Named halt conditions include inline corrective action specification | **PASS** | FAIL | FAIL | FAIL | FAIL |

**C-37 Evidence:**

- **V-01 PASS**: Cell-level corrective action specificity maintained throughout. Representative halts: F-07 `"Populate the Reason cell with the specific content signal that warrants this expert. Halt."` — names target cell; F-02 `"Replace the non-standard tag with P1, P2, or P3 before continuing. Halt."` — names replacement values; F-28 `"Correct the Section value to match a BLOCK 2 P1 Section, or add the P1 finding to BLOCK 2 before continuing. Halt."` — names both resolution paths with block specificity. F-19 `"Populate it before continuing. Halt."` — anaphoric "it" refers to "Rationale cell" in trigger clause; passes by the R13 V-01 precedent.

- **V-02 FAIL**: F-19 `"Populate. Halt."` — bare one-word corrective action without naming target cell or content type. C-37 requires complete coverage; a single bare halt fails the criterion regardless of how specific other halts are.

- **V-03 FAIL**: F-06 `"Populate. Halt."` and F-19 `"Populate. Halt."` — both the primary pyramid halt and the inversion rationale halt use bare shorthand. Two bare halts compound the failure.

- **V-04 FAIL**: F-19 `"Populate. Halt."` — same bare shorthand pattern. F-06 names the cell (`"Populate the Rationale cell. Halt."`) but F-19 does not.

- **V-05 FAIL**: Uses "CONSTRAINT VIOLATED:" declarative prefix but F-07 `"Populate. Halt."`, F-19 `"Populate. Halt."`, F-11 `"Populate. Halt."`, F-25 `"populate. Halt."` — four bare halts. The declarative framing elevates structural clarity but does not substitute for corrective action specificity.

**C-37 pattern note**: C-37 is confirmed as the decisive differentiator for the third consecutive round (R12 introduced it, R13 made it active, R14 maintains it). V-01 is the only variation that consistently specifies what to populate, with what content, in which cell.

---

### Aspirational Pass Counts

| Variation | Aspirational Pass | Aspirational Score |
|-----------|------------------|--------------------|
| V-01 | 35 / 35 | 10.00 |
| V-02 | 34 / 35 | 9.71 |
| V-03 | 34 / 35 | 9.71 |
| V-04 | 34 / 35 | 9.71 |
| V-05 | 34 / 35 | 9.71 |

---

## Composite Scores

```
composite = (essential_pass / 4 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 35 × 10)
```

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.00 | 30.00 | 10.00 | **100.00** |
| V-02 | 60.00 | 30.00 | 9.71 | **99.71** |
| V-03 | 60.00 | 30.00 | 9.71 | **99.71** |
| V-04 | 60.00 | 30.00 | 9.71 | **99.71** |
| V-05 | 60.00 | 30.00 | 9.71 | **99.71** |

---

## Ranking

| Rank | Variation | Score | Delta from Leader |
|------|-----------|-------|-------------------|
| 1 | **V-01** | 100.00 | — |
| 2 | V-02 | 99.71 | −0.29 |
| 2 | V-03 | 99.71 | −0.29 |
| 2 | V-04 | 99.71 | −0.29 |
| 2 | V-05 | 99.71 | −0.29 |

**Sub-ranking V-02/V-03/V-04/V-05 by structural richness (score-equivalent, ordered by new-pattern density):**

1. **V-05** — introduces Elevation Record + "CONSTRAINT VIOLATED:" register + BLOCK 2.7 + F-28/F-29/F-30: most new structural surface of any variation this round
2. **V-04** — BLOCK 2.7 + derivation formula continuity + F-28/F-29/F-30: three cross-block verification chains
3. **V-02** — BLOCK 2.7 + F-28/F-29/F-30: dedicated upstream registry with both integrity gates
4. **V-03** — inline pre-check enumeration + F-28: lowest structural footprint among the four; no new F-IDs beyond F-28

---

## Excellence Signals (V-01)

**Signal 1 — C-37 compliance maintained through F-28 addition.** V-01's F-28 corrective action demonstrates the cell-level specificity pattern applied to the new cross-block halt class: `"Correct the Section value to match a BLOCK 2 P1 Section, or add the P1 finding to BLOCK 2 before continuing. Halt."` Two resolution paths are named with explicit block-level references. This is the first F-ID in BLOCK 5 to offer a bidirectional repair choice: fix the consumer (BLOCK 5 Section reference) OR expand the source (BLOCK 2 P1 rows). The same bidirectional repair class is present in F-13/F-18 for BLOCK 0 ↔ BLOCK 1, now extended to BLOCK 2 ↔ BLOCK 5.

**Signal 2 — Inline F-28 sufficiency confirmed.** V-01 places F-28 at BLOCK 5 firing directly against BLOCK 2 P1 rows, with no upstream registry block. The 100.00 score confirms that the enforcement placement experiment (V-01 inline vs. V-02/V-04/V-05 upstream registry) resolves in favor of inline for compliance equivalence. A dedicated registry block adds structural depth (enabling F-29/F-30) but is not required for C-42 pass.

---

## New Structural Patterns (Round 14 — R15 Criterion Candidates)

These patterns appear in runner-up variations and are candidates for R15 rubric encoding. They do not affect R14 scores but represent the structural frontier opened by the C-42 axis.

**Pattern 1 — F-29: Registry outbound integrity gate** (V-02, V-04, V-05)
BLOCK 2.7 can contain a spurious entry: a Section value in the registry with no matching P1 row in BLOCK 2. A spurious registry entry is propagated to BLOCK 5 as a valid Section value, bypassing F-28. F-29 closes this gap by firing when any BLOCK 2.7 entry has no BLOCK 2 P1 source. This is a new enforcement class: **downstream consumer protection through upstream source integrity**. F-28 protects BLOCK 5 from invalid references; F-29 protects BLOCK 2.7 from invalid entries before BLOCK 5 ever consults it.

**Pattern 2 — F-30: Referenced block mandatory halt** (V-02, V-04, V-05)
When BLOCK 5 F-28 references BLOCK 2.7, the absence of BLOCK 2.7 makes the reference structurally unsatisfiable. F-30 fires when BLOCK 2.7 is absent, making the registry block mandatory rather than optional. This generalizes to a new enforcement class: **referenced-block existence must be separately halted** when a later block depends on it. Prior F-IDs fire on content absence within a present block; F-30 fires on the absence of a block referenced by a later block's F-ID.

**Pattern 3 — BLOCK 3 P1 Elevation Record with BLOCK 5 Consensus Elevation Rule** (V-05)
V-05 adds a second table to BLOCK 3 that classifies every P1 finding as ELEVATED (in a BLOCK 3 AGREE row) or BASELINE (not in any AGREE row). BLOCK 5 then enforces an ordering rule: all ELEVATED P1 findings receive lower rank integers than all BASELINE findings. This makes Priority Rank partially deterministic and independently verifiable: a BASELINE finding ranked above any ELEVATED finding is a structural violation detectable without computing the derivation formula. The Elevation Record introduces a **pre-classification gate** before BLOCK 5 that converts a derivation input (consensus status) into a discrete categorical label, enabling rank integrity enforcement at the category level.

---

## Outcome Classification

| Variation | All Essential Pass | Composite ≥ 80 | Outcome |
|-----------|--------------------|----------------|---------|
| V-01 | ✓ | ✓ (100.00) | **Golden** |
| V-02 | ✓ | ✓ (99.71) | **Golden** |
| V-03 | ✓ | ✓ (99.71) | **Golden** |
| V-04 | ✓ | ✓ (99.71) | **Golden** |
| V-05 | ✓ | ✓ (99.71) | **Golden** |

All five variations are Golden. The round is saturated on essential and recommended criteria; C-37 is the single active differentiator.

---

## Round Summary

R14 settles the C-42 enforcement placement question: inline named halt at BLOCK 5 (V-01), upstream dedicated registry (V-02/V-04/V-05), and inline pre-check enumeration (V-03) all satisfy C-42 at identical rubric score. The axis experiment produced no compliance differential — C-42 is placement-agnostic. The structural value of BLOCK 2.7 is not C-42 compliance but the two new enforcement classes it enables (F-29, F-30) that protect the registry's integrity before BLOCK 5 consults it. These are R15 candidates. C-37 remains the leading differentiator for the third consecutive round.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["F-29 registry outbound integrity gate: BLOCK 2.7 entries must have matching BLOCK 2 P1 rows; spurious registry entries produce valid F-28-passing BLOCK 5 rows that reference sections the review never flagged", "F-30 referenced-block mandatory halt: when BLOCK 5 F-28 references BLOCK 2.7, the registry block absence must be separately halted — extends F-ID enforcement to block-level dependency existence, not just content presence", "BLOCK 3 P1 Elevation Record pre-classifies findings as ELEVATED or BASELINE before BLOCK 5 rank ordering, making Priority Rank verifiable at the category level independent of the derivation formula"]}
```
