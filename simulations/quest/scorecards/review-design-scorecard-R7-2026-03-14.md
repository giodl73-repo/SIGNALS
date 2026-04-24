---

# Scorecard — review-design Round 7

## Rubric Summary (v7)

23 criteria: C-01–C-04 essential (60%), C-05–C-07 recommended (30%), C-08–C-23 aspirational (16 criteria × 0.625 pts, 10%).

All R7 variations are built on the R6-V05 baseline, which already carries C-21 (BLOCK 0), C-22 (4-column BLOCK 3 Synthesis), and C-23 (formal register). The R7 axes test three new F-IDs that have no corresponding criterion in v7 yet.

---

## Criterion Analysis — Summary

**All 5 variations PASS all 23 criteria.** The differentiators:

| Criterion | Differentiator | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|---------------|------|------|------|------|------|
| C-21 | BLOCK 0 + SHALL gate | PASS + F-13 | PASS (prose only) | PASS (prose only) | PASS + F-13 | PASS + F-13 |
| C-22 | 4-col BLOCK 3 | PASS | PASS + F-14 | PASS + F-15 | PASS + F-14 | PASS + F-14 + F-15 |
| C-23 | No calibration language | PASS (formal decl.) | PASS (imperative) | PASS (imperative) | PASS (formal decl.) | PASS (formal decl.) |

Key scoring notes:
- **C-21**: V-02/V-03 pass without F-13 — prose SHALL gate satisfies the pass condition. F-13 is additive (C-24 candidate).
- **C-22**: V-01 passes without F-14/F-15 — 4-column table form inherited from R6-V05 baseline satisfies C-22. F-14 and F-15 are additive.
- **C-23**: V-02/V-03 use imperative register ("Halt and restructure immediately," lowercase "must") — not calibration language. C-23 targets "aim for"/"try to ensure" phrasing specifically. PASS for all.

---

## Composite Scores

| Var | Essential | Recommended | Aspirational | **Total** |
|-----|-----------|-------------|--------------|----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

---

## Ranking

| Rank | Var | Score | Structural depth |
|------|-----|-------|-----------------|
| 1 | **V-05** | 100 | F-13 + F-14 + F-15; formal declarative register; R8 extraction source |
| 2 | **V-04** | 100 | F-13 + F-14; formal declarative; tests additivity |
| 3 | **V-01** | 100 | F-13 only; formal declarative; BLOCK 0 gate naming isolated |
| 4 | **V-02** | 100 | F-14 only; imperative register; introduces new constrained-vocabulary class |
| 5 | **V-03** | 100 | F-15 only; imperative register; narrowest failure surface |

---

## Excellence Signals (V-05)

1. **F-13 — Named halt on BLOCK 0 gate**: Every other lifecycle cross-block integrity gate had a named F-ID (F-09, F-10, F-12). The BLOCK 0→BLOCK 1 gate was the lone exception. F-13 closes the gap — same pattern as F-10, one stage earlier. Violations become precisely localizable (the exact uncatalogued signal phrase), rather than detectable only through prose comparison.

2. **F-14 — Constrained-vocabulary halt on BLOCK 3 Type column**: Introduces the fifth enforcement class: *categorical vocabulary integrity*. Prior classes: structural presence, content completeness, count parity, identity integrity. F-14 fires on any Type value outside {AGREE, SPLIT} — the last constrained-vocabulary column without a named halt (F-02 covers Sev, F-05 covers Re-run Scope).

3. **F-15 — Downstream reviewer identity verification BLOCK 3 vs BLOCK 1.5**: Extends F-10's identity-integrity pattern one stage downstream. F-10 catches orphaned experts at BLOCK 1.5 relative to BLOCK 1. F-15 catches phantom reviewers in the BLOCK 3 Reviewers column relative to BLOCK 1.5. Covers AGREE (each comma-separated name verified) and SPLIT (both A and B). Completes the full identity lifecycle chain from BLOCK 1 through BLOCK 3.

---

**v8 criterion candidates**: C-24 (F-13 named gate halt), C-25 (F-14 Type vocabulary), C-26 (F-15 downstream identity).

Scorecard written to `simulations/quest/scorecards/review-design-scorecard-R7-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-13: named halt on BLOCK 0 signal catalogue gate — converts prose SHALL constraint into a named enforcement event with precise F-ID; closes the last lifecycle cross-block integrity gate without a named halt (F-09 BLOCK 1→1.5 count, F-10 BLOCK 1→1.5 identity, F-12 BLOCK 2.5→BLOCK 5 count each had F-IDs; BLOCK 0→BLOCK 1 gate did not); V-02/V-03 pass C-21 with prose SHALL alone confirming F-13 is additive; C-24 candidate", "F-14: constrained-vocabulary halt on BLOCK 3 Type column — introduces fifth enforcement class (vocabulary integrity on categorical column); F-02 covers Sev {P1/P2/P3}, F-05 covers Re-run Scope (never full review), F-14 closes the last constrained-vocabulary column without a named halt: Type {AGREE/SPLIT}; V-01/V-03 pass C-22 without F-14 confirming aspirational; C-25 candidate", "F-15: downstream reviewer identity verification BLOCK 3 vs BLOCK 1.5 — extends F-10 identity-integrity pattern one lifecycle stage downstream; F-10 catches phantom experts at BLOCK 1.5 relative to BLOCK 1; F-15 catches phantom reviewers at BLOCK 3 relative to BLOCK 1.5; AGREE rows verify each comma-separated name, SPLIT rows verify both A and B names; V-01/V-02/V-04 pass without F-15 confirming aspirational; C-26 candidate"]}
```
| Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | BLOCK 2.5 explicitly positioned between BLOCK 2 and BLOCK 3; Status column distinguishes pyramid nominal from inverted; F-06 fires on inverted without Rationale row |

---

### C-09 | Expert Disagreement Analysis

All variations require SPLIT row synthesis via F-11. All use the 4-column BLOCK 3 form (Synthesis is a dedicated column).

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | F-11 declared in all registries; SPLIT row with empty Synthesis cell fires F-11; 4-column table makes blank Synthesis structurally detectable |

---

### C-10 | Structural Column Enforcement in Finding Tables

All variations use `Sev | Section | Finding` table format for BLOCK 2 per-reviewer findings.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Identical BLOCK 2 table structure across all |

---

### C-11 | Three-Field Expert Trace

All variations use `Signal detected | Expert added | Reason` as three distinct labeled table columns in BLOCK 1. F-03 and F-07 fire on empty cells.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Three-column domain expert table in all; F-03 on empty Signal detected, F-07 on empty Expert added or Reason |

---

### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block

All variations position BLOCK 2.5 as a discrete block explicitly between BLOCK 2 and BLOCK 3.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | BLOCK 2.5 header marks lifecycle position in all; `positioned between BLOCK 2 and BLOCK 3` present |

---

### C-13 | Expert Trace in Table Column Form

All variations use the three-column table form for domain expert selection.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | `| Signal detected | Expert added | Reason |` table in all |

---

### C-14 | Named Halt Conditions on Every Mandatory Block

All variations carry F-01 through F-12 from the R6-V05 baseline. Every mandatory block has at least one named F-ID.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | F-01–F-13; every mandatory block covered including F-08 on BLOCK 4, F-05+F-12 on BLOCK 5 |
| V-02 | **PASS** | F-01–F-12 + F-14; registry: "Halt and restructure immediately if any of F-01 through F-12 or F-14 fires" |
| V-03 | **PASS** | F-01–F-12 + F-15; same enumeration pattern |
| V-04 | **PASS** | F-01–F-13 + F-14; complete coverage |
| V-05 | **PASS** | F-01–F-13 + F-14 + F-15; most complete registry |

---

### C-15 | Roster Commitment Table Before Finding Generation

All variations include BLOCK 1.5 as a Markdown table positioned before BLOCK 2.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | `| Reviewer | Role | Source |` table present in all, positioned after BLOCK 1 before BLOCK 2 |

---

### C-16 | Source Column in Roster Commitment Table

All variations include a `Source` column (`Domain` / `Stock`) in BLOCK 1.5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Source column with Domain/Stock distinction in all BLOCK 1.5 tables |

---

### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)

All variations declare F-10 with exact-match trigger on BLOCK 1.5 Domain reviewer names vs. BLOCK 1 Expert added values.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | F-10 in all registries; BLOCK 1.5 gate explicitly checks Reviewer name must exactly match an Expert added value in BLOCK 1 |

---

### C-18 | Content-Completeness Halt on SPLIT Synthesis Field

All variations declare F-11 with the 4-column BLOCK 3 table making blank Synthesis cells structurally detectable.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | F-11 declared; formal: `An empty or absent Synthesis column cell is non-conformant under F-11` |
| V-02 | **PASS** | `F-11 fires on any SPLIT row with an empty Synthesis cell` |
| V-03 | **PASS** | Same as V-02 |
| V-04 | **PASS** | F-11 with formal language |
| V-05 | **PASS** | `fires on any SPLIT row with an empty Synthesis cell` |

---

### C-19 | Cross-Block Count-Parity for P1 Findings

All variations record `P1 count` at BLOCK 2.5 as anchor and enforce F-12 gate at BLOCK 5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | `P1 count = [n] SHALL be recorded` at BLOCK 2.5; F-12 fires if BLOCK 5 entry count < P1 count anchor |

---

### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form

All variations use `| P1 Finding | Section | Action | Re-run Scope |` 4-column table for BLOCK 5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Identical 4-column BLOCK 5 structure in all variations |

---

### C-21 | BLOCK 0 Pre-Scan Signal Catalogue

Requires: dedicated BLOCK 0 before BLOCK 1 + formal SHALL cross-block constraint. All 5 variations include BLOCK 0. V-01/V-04/V-05 additionally name F-13 on the gate; V-02/V-03 use prose SHALL without a named F-ID — prose SHALL is sufficient for C-21 pass.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | BLOCK 0 present; `Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation.` |
| V-02 | **PASS** | BLOCK 0 present; `Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue.` Prose SHALL satisfies C-21 pass condition without F-13. |
| V-03 | **PASS** | Same as V-02 — BLOCK 0 + prose SHALL gate, no F-13 |
| V-04 | **PASS** | BLOCK 0 + F-13; `F-13 is raised on any such violation — the violating row SHALL NOT be accepted until a matching Signal phrase is added` |
| V-05 | **PASS** | BLOCK 0 + F-13; strongest form: `block SHALL NOT be closed until all detected signals are recorded` |

Note: F-13 is additive to C-21 — converts prose SHALL into a named enforcement event. V-02/V-03 pass C-21 without it; F-13 is the C-24 candidate for R8.

---

### C-22 | BLOCK 3 Consensus in 4-Column Structural Table Form

All variations use a `Type | Issue | Reviewers | Synthesis` 4-column table for BLOCK 3. V-02 adds F-14 on Type (requires Type column); V-03 adds F-15 on Reviewers (requires Reviewers column).

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `| Type | Issue | Reviewers | Synthesis |` table; F-11 on Synthesis cell |
| V-02 | **PASS** | 4-column table with Type column; `Type: MUST contain exactly AGREE or SPLIT. Any other value fires F-14 — halt and correct the row before continuing.` |
| V-03 | **PASS** | 4-column table with Reviewers column; F-15 enforcement requires and depends on Reviewers column existence |
| V-04 | **PASS** | 4-column table; `Type SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14` |
| V-05 | **PASS** | 4-column table; both F-14 (Type) and F-15 (Reviewers) enforced against their respective columns |

---

### C-23 | Register Isolation for Formal Lifecycle Block Headers

Requires: no informal calibration language (aim, try, ideally, prefer, consider) in block headers or F-ID trigger clauses. All variations pass — none use calibration language in enforcement positions. V-01/V-04/V-05 use exclusively formal declarative vocabulary (SHALL/MUST/non-conformant); V-02/V-03 use imperative register (must/always required/Halt and restructure). Imperative is not calibration language — it signals mandatory constraint, not aspiration.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | Formal declarative throughout: `SHALL NOT be accepted until`, `is non-conformant under`, `MUST be populated`. No calibration language in any header or trigger. |
| V-02 | **PASS** | Imperative register: "Halt and restructure immediately," "always required," lowercase "must". No "aim for," "try to ensure," "ideally," or equivalent calibration phrasing in headers or F-ID triggers. |
| V-03 | **PASS** | Same imperative register as V-02; no calibration language |
| V-04 | **PASS** | Formal declarative: `SHALL NOT be accepted until`, `is non-conformant under F-14`; no calibration language |
| V-05 | **PASS** | Strongest formal register: `SHALL NOT be accepted until`, `MUST appear in`, `is non-conformant under`; no calibration language |

Register quality note (qualitative, not rubric-detectable): V-01/V-04/V-05 use exclusively formal modal vocabulary per C-23's vocabulary list. V-02/V-03 use imperative + lowercase modal — technically satisfies C-23 (no calibration language) but is qualitatively weaker than V-01/V-04/V-05.

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | essential | PASS | PASS | PASS | PASS | PASS |
| C-02 | essential | PASS | PASS | PASS | PASS | PASS |
| C-03 | essential | PASS | PASS | PASS | PASS | PASS |
| C-04 | essential | PASS | PASS | PASS | PASS | PASS |
| C-05 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-06 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-09 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-19 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-21 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-22 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-23 | aspirational | PASS | PASS | PASS | PASS | PASS |
| **Essential** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational** | 10 | 10 | 10 | 10 | 10 | 10 |
| **TOTAL** | 100 | **100** | **100** | **100** | **100** | **100** |

---

## Round 7 Ranking

All five variations score **100** on v7. This is the expected pattern: v7 was built from R6 excellence signals that the R6-V05 baseline already carries. All R7 variations build on that baseline and add axes (F-13, F-14, F-15) that the current rubric cannot yet distinguish.

| Rank | Var | Score | Structural depth |
|------|-----|-------|-----------------|
| 1 | V-05 | 100 | All three R7 axes: F-13 + F-14 + F-15; formal declarative register; R8 extraction source |
| 2 | V-04 | 100 | Two axes: F-13 + F-14; formal declarative register; tests F-13/F-14 additivity |
| 3 | V-01 | 100 | F-13 only; formal declarative register; isolates BLOCK 0 gate naming |
| 4 | V-02 | 100 | F-14 only; imperative register; introduces new constrained-vocabulary enforcement class |
| 5 | V-03 | 100 | F-15 only; imperative register; extends identity integrity downstream |

V-05 is qualitatively richest: only variation with all three new F-IDs and strongest register. V-02 and V-03 are weaker within the 100 tier — imperative register is a qualitative distinction not yet captured by any rubric criterion, and their single-axis scope is narrower. V-03 ranks lowest because F-15 addresses a narrower failure surface (phantom reviewer in consensus) than F-13 (gate integrity) or F-14 (new enforcement class).

---

## Excellence Signals (V-05 — top structural variation)

**F-13: Named halt on BLOCK 0 signal catalogue gate** — V-01/V-04/V-05 introduce F-13, converting the BLOCK 0→BLOCK 1 prose SHALL constraint into a named enforcement event. Before F-13, the BLOCK 0 gate was the only lifecycle cross-block integrity gate without a named halt: F-09 (BLOCK 1→BLOCK 1.5 count), F-10 (BLOCK 1→BLOCK 1.5 identity), and F-12 (BLOCK 2.5→BLOCK 5 count) all had named IDs. F-13 closes this gap — same pattern as F-10, one lifecycle stage earlier. A BLOCK 1 row that violates the BLOCK 0 gate can be precisely localized (the exact Signal detected value that failed the check), rather than detected only through prose comparison. V-02/V-03 pass C-21 without F-13, confirming F-13 is additive beyond the current rubric ceiling.

**F-14: Constrained-vocabulary halt on BLOCK 3 Type column** — V-02/V-04/V-05 introduce F-14 as a new enforcement class: categorical vocabulary integrity. Prior F-ID classes cover structural presence (F-01, F-04, F-08), content completeness (F-11), count parity (F-09, F-12), and identity integrity (F-10, F-13). F-14 is the first F-ID enforcing a closed vocabulary on a categorical column ({AGREE, SPLIT} only). The Type column is the last constrained-vocabulary column in the lifecycle without an equivalent halt — F-02 covers Sev vocabulary (P1/P2/P3), F-05 covers Re-run Scope ("never full review"), but no F-ID previously fired on an invalid Type value. V-01/V-03 pass C-22 without F-14, confirming F-14 is additive.

**F-15: Downstream reviewer identity verification BLOCK 3 vs BLOCK 1.5** — V-03/V-05 extend the F-10 identity-integrity pattern one lifecycle stage. F-10 catches phantom experts in BLOCK 1.5 relative to BLOCK 1 (Domain reviewer name has no BLOCK 1 Expert added match). F-15 catches phantom reviewers in BLOCK 3 relative to BLOCK 1.5 (Reviewers column name has no BLOCK 1.5 Reviewer match). Same structural failure class — entity referenced at block N has no canonical entry at block N-1 — now covers BLOCK 1 through BLOCK 3. For AGREE rows, each comma-separated name must verify against BLOCK 1.5; for SPLIT rows, both A and B names must verify. V-01/V-02/V-04 pass without F-15, confirming aspirational.

---

## v8 Criterion Candidates

**C-24 candidate | Named Halt on BLOCK 0 Signal Catalogue Gate (F-13)**
- V-01, V-04, V-05 name F-13 as the enforcement identifier for the BLOCK 0 prose SHALL gate
- V-02, V-03 pass C-21 without F-13 — confirms aspirational
- Pattern: closes the last lifecycle cross-block integrity gate without a named halt; same mechanism as F-10, one stage earlier
- C-24 pass condition: Output names F-13 (or equivalent ID) as a halt that fires when any Signal detected value in BLOCK 1 is absent from the BLOCK 0 catalogue; the halt must identify the violating signal phrase and require its addition to BLOCK 0 before the row is accepted

**C-25 candidate | Constrained-Vocabulary Halt on BLOCK 3 Type Column (F-14)**
- V-02, V-04, V-05 name F-14 for Type vocabulary enforcement
- V-01, V-03 pass C-22 without F-14 — confirms aspirational
- Pattern: fifth enforcement class (vocabulary integrity); prior classes cover presence, completeness, count parity, identity integrity
- C-25 pass condition: Output names F-14 (or equivalent) as a halt that fires when a Type cell in BLOCK 3 contains a value other than AGREE or SPLIT; halt must name the invalid value and require correction before the block closes

**C-26 candidate | Cross-Block Reviewer Identity Verification for BLOCK 3 (F-15)**
- V-03, V-05 name F-15 for phantom reviewer detection in BLOCK 3
- V-01, V-02, V-04 pass C-22 + C-17 without F-15 — confirms aspirational
- Pattern: extends F-10 identity integrity downstream; BLOCK 1→BLOCK 1.5 covered by F-10; BLOCK 1.5→BLOCK 3 now covered by F-15; full identity lifecycle chain complete
- C-26 pass condition: Output names F-15 (or equivalent) as a halt that fires when any reviewer name in BLOCK 3 Reviewers column has no matching Reviewer in BLOCK 1.5; AGREE rows: each comma-separated name verified; SPLIT rows: both A and B names verified; halt identifies the phantom name

---

## Scorecard Output

Written to `simulations/quest/scorecards/review-design-scorecard-R7-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-13: named halt on BLOCK 0 signal catalogue gate — converts prose SHALL constraint into a named enforcement event with precise F-ID; closes the last lifecycle cross-block integrity gate without a named halt (F-09 BLOCK 1→1.5 count, F-10 BLOCK 1→1.5 identity, F-12 BLOCK 2.5→BLOCK 5 count each had F-IDs; BLOCK 0→BLOCK 1 gate did not); V-02/V-03 pass C-21 with prose SHALL alone confirming F-13 is additive; C-24 candidate", "F-14: constrained-vocabulary halt on BLOCK 3 Type column — introduces fifth enforcement class (vocabulary integrity on categorical column); F-02 covers Sev {P1/P2/P3}, F-05 covers Re-run Scope (never full review), F-14 closes the last constrained-vocabulary column without a named halt: Type {AGREE/SPLIT}; V-01/V-03 pass C-22 without F-14 confirming aspirational; C-25 candidate", "F-15: downstream reviewer identity verification BLOCK 3 vs BLOCK 1.5 — extends F-10 identity-integrity pattern one lifecycle stage downstream; F-10 catches phantom experts at BLOCK 1.5 relative to BLOCK 1; F-15 catches phantom reviewers at BLOCK 3 relative to BLOCK 1.5; AGREE rows verify each comma-separated name, SPLIT rows verify both A and B names; V-01/V-02/V-04 pass without F-15 confirming aspirational; C-26 candidate"]}
```
