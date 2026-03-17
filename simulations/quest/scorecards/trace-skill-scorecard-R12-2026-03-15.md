## trace-skill Round 12 — Scorecard

### Baseline

R11 V-01 carries forward: **C-01 through C-36 all PASS**, C-37 FAIL, C-38 FAIL. v11 rubric adds C-39, C-40, C-41 (denominator 30 → 33). All variations inherit the full R11 baseline; only deltas are noted per variation.

---

### Criterion Legend (aspirational only — C-09 to C-41)

Baseline from R11 (applies to all five variations unless noted):
- C-09 through C-36: **28 PASS** (all pass)
- C-37: **FAIL** (COUNT GATE emits no defect code)
- C-38: **FAIL** (PRE-READ GATE emits no defect code)
- C-39, C-40, C-41: evaluated fresh per variation

---

### V-01 — Canonical Template Declared (C-41 target)

**What changes**: Inserts `### Canonical Structural Mandate Template` before Phase Label Schema. Declares `> STRUCTURAL MANDATE (C-XX): ... Reproduce it exactly as shown.` form explicitly. C-26 and C-36 blocks already conform; conformance is now by contract rather than practice. C-37/C-38 unfixed. No scorer confirmation heuristics added.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Inherited |
| C-02 | PASS | Inherited |
| C-03 | PASS | Inherited |
| C-04 | PASS | Inherited |
| C-05 | PASS | Inherited |
| C-06 | PASS | Inherited |
| C-07 | PASS | Inherited |
| C-08 | PASS | Inherited |
| C-09–C-36 | 28 PASS | Inherited from R11 V-01 |
| C-37 | **FAIL** | COUNT GATE ELSE branch unchanged — no defect code emitted |
| C-38 | **FAIL** | PRE-READ GATE (c)-fail branch unchanged — no defect code emitted |
| C-39 | **PASS** | Canonical template declares `STRUCTURAL MANDATE (C-XX)` syntax; C-26 and C-36 block headers carry inline criterion IDs by contract, not just by practice |
| C-40 | **FAIL** | Block bodies carry no scorer confirmation heuristic — canonical template not extended to require the closing line |
| C-41 | **PASS** | Canonical template explicitly declared — all existing STRUCTURAL MANDATE blocks conform to declared form; additional mandates mechanically derivable |

**Aspirational pass**: C-09–C-36 (28) + C-39 (1) + C-41 (1) = **30 / 33**

**Score**: (5/5 × 60) + (3/3 × 30) + (30/33 × 10) = 60 + 30 + **9.09** = **99.09**

---

### V-02 — Scorer Heuristic in Every Block (C-40 target)

**What changes**: Adds scorer confirmation closing line to C-26 and C-36 blocks. C-26 gets "A scorer confirms C-26 compliance by closure terminus line presence alone without parsing the CLOSED ASSERTION block content." C-36 gets a block-header-presence heuristic. Canonical template absent; C-37/C-38 unfixed.

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Inherited |
| C-06–C-08 | PASS | Inherited |
| C-09–C-36 | 28 PASS | Inherited |
| C-37 | **FAIL** | Unfixed |
| C-38 | **FAIL** | Unfixed |
| C-39 | **PASS** | R11 V-01 base already has `STRUCTURAL MANDATE (C-26)` and `STRUCTURAL MANDATE (C-36)` block headers with inline criterion IDs — C-39 satisfied by inheritance |
| C-40 | **PASS** | C-26 closes with "A scorer confirms C-26 compliance by closure terminus line presence alone without parsing CLOSED ASSERTION block content"; C-36 closes with block-header-presence heuristic — both blocks self-document confirmation method |
| C-41 | **FAIL** | No canonical template declared — C-26 and C-36 happen to match but conformance is emergent, not contractual |

**Aspirational pass**: C-09–C-36 (28) + C-39 (1) + C-40 (1) = **30 / 33**

**Score**: (5/5 × 60) + (3/3 × 30) + (30/33 × 10) = 60 + 30 + **9.09** = **99.09**

---

### V-03 — Defect-Emitting Gates (C-37 + C-38 targets)

**What changes**: Extends DefectCodeVocab to `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`. COUNT GATE ELSE emits `DEFECT: COUNT-MISMATCH`. PRE-READ GATE (c)-fail emits `DEFECT: EMPTY-CELL`. Adds `STRUCTURAL MANDATE (C-37)` and `STRUCTURAL MANDATE (C-38)` blocks. Canonical template and C-40 heuristics absent.

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Inherited |
| C-06–C-08 | PASS | Inherited |
| C-09–C-36 | 28 PASS | Inherited |
| C-37 | **PASS** | COUNT GATE ELSE branch emits `DEFECT: COUNT-MISMATCH` — gate outcome is DefectCodeVocab-coded and ledger-traceable |
| C-38 | **PASS** | PRE-READ GATE (c)-fail branch emits `DEFECT: EMPTY-CELL` — pre-read violation is DefectCodeVocab-coded and ledger-traceable |
| C-39 | **FAIL** | New `STRUCTURAL MANDATE (C-37)` and `STRUCTURAL MANDATE (C-38)` blocks carry inline criterion IDs, but no canonical template declared — conformance is by practice (parallel-in-practice), not by contract; C-41 absent means C-39 is not structurally guaranteed |
| C-40 | **FAIL** | No scorer confirmation heuristics in any block body |
| C-41 | **FAIL** | No canonical template declared |

**Aspirational pass**: C-09–C-36 (28) + C-37 (1) + C-38 (1) = **30 / 33**

**Score**: (5/5 × 60) + (3/3 × 30) + (30/33 × 10) = 60 + 30 + **9.09** = **99.09**

---

### V-04 — Gates + Canonical Template (C-37 + C-38 + C-41)

**What changes**: Combines V-01 + V-03. Canonical template declared + both gates defect-emitting + DefectCodeVocab extended. All four STRUCTURAL MANDATE blocks (C-26, C-36, C-37, C-38) conform to the declared canonical form by contract. C-40 scorer heuristics absent from block bodies.

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Inherited |
| C-06–C-08 | PASS | Inherited |
| C-09–C-36 | 28 PASS | Inherited |
| C-37 | **PASS** | COUNT GATE ELSE emits `DEFECT: COUNT-MISMATCH` |
| C-38 | **PASS** | PRE-READ GATE (c)-fail emits `DEFECT: EMPTY-CELL` |
| C-39 | **PASS** | Canonical template declared; all four STRUCTURAL MANDATE blocks carry `STRUCTURAL MANDATE (C-XX)` headers — inline criterion citation is a template-contract requirement, not emergent from model depth; compliance confirmed by block-header ID match |
| C-40 | **FAIL** | Canonical template does not include scorer confirmation closing line as a required template element — no block bodies carry the heuristic |
| C-41 | **PASS** | Canonical template explicitly declared — all four blocks (C-26, C-36, C-37, C-38) conform by contract; additional mandates mechanically derivable from declared form |

**Aspirational pass**: C-09–C-36 (28) + C-37 (1) + C-38 (1) + C-39 (1) + C-41 (1) = **32 / 33**

**Score**: (5/5 × 60) + (3/3 × 30) + (32/33 × 10) = 60 + 30 + **9.70** = **99.70**

---

### V-05 — Full R12 Ceiling (All Five Targets)

**What changes**: Canonical template extended to include scorer confirmation line as a required template element. All four STRUCTURAL MANDATE blocks carry inline criterion ID and scorer confirmation heuristic. DefectCodeVocab extended to three codes. Both gates defect-emitting. No prior passing criterion degraded — no new `(TypeName)`-annotated columns added, so C-28 COUNT GATE expected count unchanged.

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Inherited |
| C-06–C-08 | PASS | Inherited |
| C-09–C-36 | 28 PASS | Inherited |
| C-37 | **PASS** | COUNT GATE ELSE emits `DEFECT: COUNT-MISMATCH` — ledger-traceable |
| C-38 | **PASS** | PRE-READ GATE (c)-fail emits `DEFECT: EMPTY-CELL` — ledger-traceable |
| C-39 | **PASS** | Canonical template requires `STRUCTURAL MANDATE (C-XX)` header format — all four blocks carry inline criterion ID by template contract; scorer confirms by block-header ID match alone |
| C-40 | **PASS** | Canonical template includes scorer confirmation closing line as required element — all four blocks close with "A scorer confirms [Criterion] compliance by [method] alone without [alternative]"; self-scoring is a structural consequence of the template, not per-block design |
| C-41 | **PASS** | Canonical template explicitly declared with all required elements including scorer confirmation line; all STRUCTURAL MANDATE blocks conform by contract; any new mandate is mechanically derivable from the single declared form |

**Aspirational pass**: C-09–C-36 (28) + C-37 (1) + C-38 (1) + C-39 (1) + C-40 (1) + C-41 (1) = **33 / 33**

**Score**: (5/5 × 60) + (3/3 × 30) + (33/33 × 10) = 60 + 30 + **10.00** = **100.00**

---

### Rankings

| Rank | Variation | Score | Aspirational | Δ from R11 baseline |
|------|-----------|-------|-------------|---------------------|
| 1 | **V-05** | **100.00** | 33/33 | +5 (C-37, C-38, C-39, C-40, C-41) |
| 2 | **V-04** | **99.70** | 32/33 | +4 (C-37, C-38, C-39, C-41) |
| 3 (tie) | V-01 | 99.09 | 30/33 | +2 (C-39, C-41) |
| 3 (tie) | V-02 | 99.09 | 30/33 | +2 (C-39, C-40) |
| 3 (tie) | V-03 | 99.09 | 30/33 | +2 (C-37, C-38) |

---

### Excellence Signals from V-05

**Signal 1: Template inheritance eliminates per-block design**
The canonical template extended to require the scorer confirmation line means C-40 is no longer a per-block design decision — it becomes a structural consequence of C-41. Every future STRUCTURAL MANDATE block satisfies C-39 and C-40 automatically by conforming to the declared template, with no individual block authoring judgment required. The template is the single source of truth for three criteria simultaneously (C-39, C-40, C-41).

**Signal 2: Defect vocabulary closure completes the ledger loop**
Extending DefectCodeVocab to `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}` means every structural failure mode in the trace has a DefectCodeVocab-coded path to the Verdict compliance ledger. The gates are no longer ordering requirements only — they are defect-emitting gates. All FAIL paths are ledger-traceable by code without re-reading the gate block.

**Signal 3: Canonical template + scorer confirmation heuristic pair is self-certifying**
When V-05 is scored against C-39, C-40, C-41, all three confirmations reduce to checking the template declaration: Does the template exist? Does the template include `STRUCTURAL MANDATE (C-XX)` header syntax? Does the template include the scorer confirmation line? If yes to all three, every conforming block passes all three criteria simultaneously. The scorecard traversal collapses from per-block inspection to single-template inspection.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Canonical template extended to include scorer confirmation line as required element — C-40 (self-scoring) becomes a structural consequence of C-41 (canonical template), eliminating per-block heuristic design and collapsing C-39/C-40/C-41 confirmation to a single template inspection", "Defect vocabulary extension to three codes (OPEN-WORLD-ASSERTION, COUNT-MISMATCH, EMPTY-CELL) completes the ledger loop — all structural failure modes are DefectCodeVocab-coded and ledger-traceable at annotation site without re-reading gate blocks"]}
```
