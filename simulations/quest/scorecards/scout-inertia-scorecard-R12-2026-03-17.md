## scout-inertia — Quest Score R12 (rubric v12)

**Date**: 2026-03-17
**Rubric**: v12 — 32 aspirational criteria, denominator 32
**New criteria**: C-34 through C-40 (7 criteria formalized from R11 excellence signals)
**Scoring**: 100 essential base + aspirational_pass/32 × 120 bonus = 220 ceiling

---

## Essential Criteria — All Variations

All five variations are scaffold templates. Each supplies the structural sections required by C-01 through C-05:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Workaround mapped | PASS | PASS | PASS | PASS | PASS |
| C-02 Switching costs quantified | PASS | PASS | PASS | PASS | PASS |
| C-03 Threat score HIGH | PASS | PASS | PASS | PASS | PASS |
| C-04 "Why inertia loses" | PASS | PASS | PASS | PASS | PASS |
| C-05 Failure mode inventory | PASS | PASS | PASS | PASS | PASS |

**All essential criteria pass for all five variations. Essential base: 100/100.**

---

## Aspirational Criteria — C-06 through C-33

R11 confirmed 25/25 aspirational pass for all five variation templates under v11. All R12 variations preserve every R11-satisfying structural element: FAIL-FIRST ordering, FM-[N] primary key system, Q3/Q4 bridge architecture, bridge gate with completion check, Stage 5B placement of citation integrity rule, COMMAND directives on each section, and C-NN: prefixed checklist. **C-06 through C-33: PASS for all five variations.**

---

## New Aspirational Criteria — C-34 through C-40 (Detailed)

### C-34 — Primary Key Rule Label

Bracket-enclosed rule label at FM-[N] assignment directive in Stage 1.

| Variation | Label form | Evidence | Score |
|-----------|-----------|----------|-------|
| V-01 | `[A-16 PRIMARY KEY RULE]` | Bracket-prefix, Stage 1 table header | **PASS** |
| V-02 | `STATUS QUO LOCK RULE [A-16]` | Bracket-suffix; R11 confirmed bracket-suffix satisfies C-34 | **PASS** |
| V-03 | `[A-16 PRIMARY KEY RULE]` | Bracket-prefix, Stage 1 table header | **PASS** |
| V-04 | `[A-16 PRIMARY KEY RULE]` | Bracket-prefix, Section 1 | **PASS** |
| V-05 | `[A-16 PRIMARY KEY RULE]` | Bracket-prefix, Stage 1 | **PASS** |

---

### C-35 — Citation Integrity Rule Label

Bracket-enclosed rule label at or before Stage 5B defeat conditions table.

| Variation | Label form | Placement | Score |
|-----------|-----------|-----------|-------|
| V-01 | `[A-19 CITATION INTEGRITY RULE]` | Section 5, immediately before DC table | **PASS** |
| V-02 | `STATUS QUO CITATION RULE [A-19]` | Section 5 (WHERE THE UNNAMED COMPETITOR LOSES), before DC table | **PASS** |
| V-03 | `[A-19 CITATION INTEGRITY RULE]` | Stage 5B, before DC table | **PASS** |
| V-04 | `[A-19 CITATION INTEGRITY RULE]` | Section 6 (Defeat Conditions), before DC table | **PASS** |
| V-05 | `[A-19 CITATION INTEGRITY RULE]` | Stage 5B, before DC table | **PASS** |

---

### C-36 — Minimum Bracket-Label Count (≥3)

Three or more distinct bracket-labeled obligations in the scaffold.

| Variation | Bracket elements | Count | Score |
|-----------|----------------|-------|-------|
| V-01 | `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` + `[BRIDGE COMPLETION COMMAND]` | 3 | **PASS** |
| V-02 | `STATUS QUO LOCK RULE [A-16]` + `STATUS QUO CITATION RULE [A-19]` + `[STATUS QUO BRIDGE COMMAND]` | 3 | **PASS** |
| V-03 | `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` + `[BRIDGE COMPLETION COMMAND]` | 3 | **PASS** |
| V-04 | `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` + `[BRIDGE GATE COMMAND]` | 3 | **PASS** |
| V-05 | `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` + `[BRIDGE COMPLETION COMMAND]` + `[BRIDGE Q3 COMMAND]` + `[BRIDGE Q4 COMMAND]` | 5 | **PASS** |

**V-02 note**: The two bracket-suffix elements (`[A-16]`, `[A-19]`) are bracket-enclosed at the ID level; regex `\[A-16` matches in either prefix or suffix position. The third element `[STATUS QUO BRIDGE COMMAND]` is bracket-prefix. C-36 counts "distinct bracket-labeled obligations" without specifying prefix-only — and the rubric evaluator notes confirm "any three distinct bracket-labeled obligations pass." PASS is warranted.

**V-05 note**: Five bracket elements far exceeds the 3-minimum. No ambiguity.

---

### C-37 — Completion Command Inside Gate Block

`[BRACKET COMMAND]` must appear in the gate block body, not in the heading text.

| Variation | Gate heading | Command location | Score |
|-----------|-------------|-----------------|-------|
| V-01 | "BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS POPULATED?" | `[BRIDGE COMPLETION COMMAND]` in block body | **PASS** |
| V-02 | "STATUS QUO BRIDGE -- FULLY MAPPED?" | `[STATUS QUO BRIDGE COMMAND]` in block body | **PASS** |
| V-03 | "STAGE 2 BRIDGE GATE -- ALL ARTIFACTS POPULATED?" | `[BRIDGE COMPLETION COMMAND]` in block body | **PASS** |
| V-04 | "BRIDGE COMPLETION CHECK -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" | `[BRIDGE GATE COMMAND]` in block body | **PASS** |
| V-05 | "PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" | `[BRIDGE COMPLETION COMMAND]` in block body | **PASS** |

All five place the bracket command as the first line of the gate block body, cleanly separated from the heading. The command is independently labelable and does not appear embedded in heading text.

---

### C-38 — FAIL-FIRST Domain Subtitle

FAIL-FIRST heading must carry structural role marker + inertia-domain vocabulary subtitle.

| Variation | Full heading | Structural marker | Domain subtitle | Domain check | Score |
|-----------|-------------|-------------------|-----------------|--------------|-------|
| V-01 | "FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR" | FAIL-FIRST DECLARATION | NAMING THE UNNAMED COMPETITOR | Names the unnamed competitor — core inertia framing | **PASS** |
| V-02 | "FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR'S FAILURE SURFACE" | FAIL-FIRST DECLARATION | THE UNNAMED COMPETITOR'S FAILURE SURFACE | Competitor + failure surface — inertia domain | **PASS** |
| V-03 | "FAIL-FIRST DECLARATION -- THE WORKAROUND FAILURE INVENTORY" | FAIL-FIRST DECLARATION | THE WORKAROUND FAILURE INVENTORY | Failure inventory is the analytical artifact of this skill | **PASS** |
| V-04 | "FAIL-FIRST DECLARATION -- DEFEAT CONDITION PREREQUISITES: WHERE THE WORKAROUND BREAKS" | FAIL-FIRST DECLARATION | DEFEAT CONDITION PREREQUISITES: WHERE THE WORKAROUND BREAKS | Compound: defeat conditions + workaround breakage — both inertia-domain | **PASS** |
| V-05 | "FAIL-FIRST DECLARATION -- NAMING THE DEFAULT COMPETITOR: STRUCTURAL WEAKNESSES" | FAIL-FIRST DECLARATION | NAMING THE DEFAULT COMPETITOR: STRUCTURAL WEAKNESSES | Names default competitor and its structural weaknesses | **PASS** |

**V-04 compound subtitle note**: "DEFEAT CONDITION PREREQUISITES: WHERE THE WORKAROUND BREAKS" uses two inertia-domain phrases joined by colon — defeat conditions as the functional role, workaround breakage as the content domain. A reader encountering the subtitle alone immediately recognizes scout-inertia context. Evaluator note: "given the subtitle alone, could a reader identify this section as part of a scout-inertia analysis?" — yes. PASS.

---

### C-39 — Binary-Question Gate Heading

Gate heading must be Yes/No-answerable without reading the block body.

| Variation | Gate heading | Question form | Score |
|-----------|-------------|--------------|-------|
| V-01 | "BRIDGE COMPLETION GATE -- ALL BRIDGE ARTIFACTS POPULATED?" | Artifact-inventory question, explicit "?" | **PASS** |
| V-02 | "STATUS QUO BRIDGE -- FULLY MAPPED?" | Short-form binary question, independently answerable | **PASS** |
| V-03 | "STAGE 2 BRIDGE GATE -- ALL ARTIFACTS POPULATED?" | Minimal artifact question, explicit "?" | **PASS** |
| V-04 | "BRIDGE COMPLETION CHECK -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" | Explicit-count binary question | **PASS** |
| V-05 | "PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" | Imperative prefix + binary question; "ALL BRIDGES COMPLETE?" is independently Yes/No | **PASS** |

**V-02 short-form note**: "FULLY MAPPED?" is the shortest gate question tested. Context from the heading prefix "STATUS QUO BRIDGE" supplies the subject; the question is Yes/No answerable within the heading scope. PASS.

**V-05 compound note**: "PASS BEFORE ADVANCING" is an imperative instruction; "ALL BRIDGES COMPLETE?" is the decision question. The evaluator rule is: can the heading be answered Yes or No without reading the body? "ALL BRIDGES COMPLETE?" is independently answerable — Yes (proceed) or No (return). The imperative prefix reinforces but does not replace the decision question. PASS.

---

### C-40 — Criterion-ID Prefixes on Checklist Items

Every trailing completeness checklist item must carry C-NN: prefix.

| Variation | Checklist section | Item prefix coverage | Score |
|-----------|-----------------|---------------------|-------|
| V-01 | Section 6 | C-01: C-02: C-03: C-04: C-05: — all five essential criteria prefixed | **PASS** |
| V-02 | Completeness Verification | C-01: C-02: C-03: C-04: C-05: — confirmed in artifact; domain vocabulary in section names does not contaminate checklist items | **PASS** |
| V-03 | Stage 6 | C-01: C-02: C-03: C-04: C-05: — stage lifecycle vocabulary does not bleed into checklist text | **PASS** |
| V-04 | Section 7 | C-01: C-02: C-03: C-04: C-05: — numbered section format, all items prefixed | **PASS** |
| V-05 | Stage 6 | C-01: C-02: C-03: C-04: C-05: — maximum-density scaffold preserves clean prefix format | **PASS** |

**C-40 vocabulary contamination check**: V-02 uses competitor-vocabulary section names ("WHERE THE UNNAMED COMPETITOR BREAKS", "WHERE THE UNNAMED COMPETITOR LOSES") throughout, but the completeness verification checklist retains neutral C-NN: prefixes. Domain vocabulary in stage names does not contaminate checklist item text. PASS confirmed.

---

## Per-Variation Composite Scores

### V-01 — Phrasing Register axis

- Essential: 5/5 ✓
- C-06 through C-33: 28/28 ✓
- C-34: PASS | C-35: PASS | C-36: PASS | C-37: PASS | C-38: PASS | C-39: PASS | C-40: PASS
- New criteria: 7/7 ✓
- **Aspirational total: 32/32**
- **Composite: 220/220**

### V-02 — Inertia Framing axis

- Essential: 5/5 ✓
- C-06 through C-33: 28/28 ✓
- C-34: PASS (bracket-suffix, R11-confirmed) | C-35: PASS | C-36: PASS (2 bracket-suffix + 1 bracket-prefix command = 3) | C-37: PASS | C-38: PASS | C-39: PASS ("FULLY MAPPED?" independently answerable) | C-40: PASS (no vocabulary contamination)
- New criteria: 7/7 ✓
- **Aspirational total: 32/32**
- **Composite: 220/220**

### V-03 — Lifecycle Emphasis axis

- Essential: 5/5 ✓
- C-06 through C-33: 28/28 ✓
- C-34: PASS | C-35: PASS | C-36: PASS | C-37: PASS | C-38: PASS ("THE WORKAROUND FAILURE INVENTORY" — artifact of this skill, inertia-domain) | C-39: PASS ("ALL ARTIFACTS POPULATED?" — binary) | C-40: PASS
- New criteria: 7/7 ✓
- **Aspirational total: 32/32**
- **Composite: 220/220**

### V-04 — Output Format axis

- Essential: 5/5 ✓
- C-06 through C-33: 28/28 ✓
- C-34: PASS | C-35: PASS | C-36: PASS | C-37: PASS | C-38: PASS (compound dual-phrase subtitle — both halves inertia-domain) | C-39: PASS ("HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" — explicit count + binary) | C-40: PASS
- New criteria: 7/7 ✓
- **Aspirational total: 32/32**
- **Composite: 220/220**

### V-05 — All Axes combined

- Essential: 5/5 ✓
- C-06 through C-33: 28/28 ✓
- C-34: PASS | C-35: PASS | C-36: PASS (5 bracket elements — highest count of any variation) | C-37: PASS | C-38: PASS ("NAMING THE DEFAULT COMPETITOR: STRUCTURAL WEAKNESSES" — competitor identity + analytical focus) | C-39: PASS ("PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" — imperative prefix + binary question) | C-40: PASS
- New criteria: 7/7 ✓
- **Aspirational total: 32/32**
- **Composite: 220/220**

---

## Rankings

| Rank | Variation | Aspirational | Composite | Notes |
|------|-----------|-------------|-----------|-------|
| 1 (tie) | V-01 | 32/32 | 220 | Canonical bracket-prefix form; COMMAND phrasing throughout |
| 1 (tie) | V-02 | 32/32 | 220 | Bracket-suffix stress test resolved; first confirmation of bracket-suffix satisfying C-36 |
| 1 (tie) | V-03 | 32/32 | 220 | Lifecycle emphasis; "THE WORKAROUND FAILURE INVENTORY" confirms artifact-noun subtitle |
| 1 (tie) | V-04 | 32/32 | 220 | Compound FAIL-FIRST subtitle; explicit-count gate heading |
| 1 (tie) | V-05 | 32/32 | 220 | Maximum bracket density (5 elements); imperative+question gate confirmed |

**All five variations achieve 32/32 aspirational under v12. First clean sweep of C-34 through C-40.**

---

## Excellence Signals

R12's design succeeded: all seven new criteria fire simultaneously across all five variations. Three structural patterns emerge that go beyond what C-34 through C-40 already codify and are candidates for v13 criteria:

**1. Compound FAIL-FIRST subtitle with dual inertia-domain phrases (V-04)**
"DEFEAT CONDITION PREREQUISITES: WHERE THE WORKAROUND BREAKS" demonstrates that a FAIL-FIRST subtitle can carry two inertia-domain phrases joined by colon — a functional-role phrase naming what follows and a domain-action phrase naming the analytical operation — without ambiguity. This is richer than single-noun subtitles ("NAMING THE UNNAMED COMPETITOR") because it simultaneously positions the section's role in the skill lifecycle and names the content in domain terms. C-38 passes on any inertia-domain subtitle, but the compound form provides additional navigation value.

**2. Imperative prefix + binary question compound gate heading (V-05)**
"PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" demonstrates that a gate heading can carry two distinct elements: a gating-action imperative ("PASS BEFORE ADVANCING") that names the consequence of the decision, plus a binary question ("ALL BRIDGES COMPLETE?") that names the decision itself. The compound form is richer than either element alone — the imperative connects the gate to the lifecycle flow, and the binary question identifies the pass criterion. C-39 passes on the binary-question form alone; the imperative prefix adds a lifecycle-anchor element not yet required by any criterion.

**3. Over-minimum bracket density compounds audit coverage (V-05)**
V-05 carries five bracket-labeled elements versus the three-minimum required by C-36. By extending bracket directives to the bridge sub-sections ([BRIDGE Q3 COMMAND], [BRIDGE Q4 COMMAND]), the scaffold creates audit checkpoints at every structural obligation — not just the three canonical lifecycle poles (primary key, citation integrity, gate command). The practical effect: every directive in the scaffold is independently labelable and cross-referenceable by its bracket tag. C-36 requires three as a floor; the five-element pattern in V-05 suggests a richer principle that may be worth formalizing: bracket-labeled directives on every gated action, not just the minimum set.

---

## Scorecard Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Essential (all 5) | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| C-06 to C-33 (prior) | 28/28 | 28/28 | 28/28 | 28/28 | 28/28 |
| **C-34** Primary Key Rule Label | PASS | PASS | PASS | PASS | PASS |
| **C-35** Citation Integrity Rule Label | PASS | PASS | PASS | PASS | PASS |
| **C-36** Min 3 Bracket Labels | PASS | PASS | PASS | PASS | PASS |
| **C-37** Completion Command in Body | PASS | PASS | PASS | PASS | PASS |
| **C-38** FAIL-FIRST Domain Subtitle | PASS | PASS | PASS | PASS | PASS |
| **C-39** Binary-Question Gate | PASS | PASS | PASS | PASS | PASS |
| **C-40** C-NN: Checklist Prefixes | PASS | PASS | PASS | PASS | PASS |
| **Aspirational Total** | **32/32** | **32/32** | **32/32** | **32/32** | **32/32** |
| **Composite Score** | **220** | **220** | **220** | **220** | **220** |

---

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["compound FAIL-FIRST subtitle with dual inertia-domain phrases — functional-role phrase plus domain-action phrase joined by colon, richer than single-noun subtitles while satisfying C-38", "imperative prefix plus binary question compound gate heading — gating-action imperative names the lifecycle consequence while the binary question names the pass criterion, both elements coexist without violating C-39", "over-minimum bracket density extends audit coverage to every gated action — five bracket elements versus the three-minimum in C-36 by labeling bridge sub-section directives, establishing that bracket-labeled commands belong on every structural obligation not just the canonical three"]}
```
