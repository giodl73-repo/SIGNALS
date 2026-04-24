## listen-support — Quest Scorecard, Round 6

**Date:** 2026-03-15
**Rubric:** v6 (21 criteria, C-01–C-21; aspirational denominator = 13)
**Variations evaluated:** V-01 through V-05

---

### Scoring Framework Recap

| Tier | Criteria | Max pts | Per-pass value |
|------|----------|---------|----------------|
| Essential | C-01–C-05 | 60 | 12.0 each |
| Recommended | C-06–C-08 | 30 | 10.0 each |
| Aspirational | C-09–C-21 | 10 | 0.769 PASS / 0.385 PARTIAL |

Aspirational formula: `(pass_count + 0.5 × partial_count) / 13 × 10`

---

### Shared Baseline (all variations)

All R6 variations inherit the full R5 V-05 mechanism set. These criteria are evaluated identically across V-01 through V-05:

| Criterion | Evidence (structural) | Score |
|-----------|-----------------------|-------|
| C-01 Ticket inventory | Ticket inventory table present; all six fields required (T-ID, title, persona, volume, severity, phase) | PASS |
| C-02 Persona attribution | Named-role per ticket; multiple distinct personas across inventory | PASS |
| C-03 First-person body voice | PERFORMANCE MODE with explicit "I/my/we" mandate; prohibition on "the SRE / the user" | PASS |
| C-04 Gap analysis | Gap analysis section with T-NN cross-refs; doc/design/operational categories required | PASS |
| C-05 Volume/severity distribution | Non-trivial distribution enforced by CONSTRAINT MANIFEST (P0 <= 25%, high-vol <= 50%) | PASS |
| C-06 Ticket count 6–12 | Constraint Manifest target: 6 to 12 | PASS |
| C-07 Cross-persona coverage | >= 3 distinct personas, no single persona > 50%; enforced by Constraint Manifest | PASS |
| C-08 Gap actionability | >= 2 entries per gap category, each with named artifact/action | PASS |
| C-09 Theme clustering | Theme declaration in STEP 3 before inventory | PASS |
| C-10 Resolution paths | STEP 7B: triage owner, root cause category, resolution type for all high-vol/P0-P1 | PASS |
| C-11 Structural integrity | CONSTRAINT MANIFEST + VERIFICATION MANIFEST form closed loop; broken T-NN refs blocked | PASS |
| C-12 Role-phase compound coverage | STEP 3A Role-Phase Cross-Matrix + constraint: any role 3+ tickets must span 2+ phases | PASS |
| C-13 Phase-calibrated severity | Phase Map Table (STEP 2) prescribes P2/P3 for Phase 1, P0/P1 for Phase 3 | PASS |
| C-14 Phase-anchored body voice | Vocabulary matrix registers phase-differentiated (discovery P1, operational P3); body register enforced | PASS |
| C-15 Constraint declaration | CONSTRAINT MANIFEST (pre-generation targets) + VERIFICATION MANIFEST (post-generation numeric check) | PASS |
| C-16 Per-ticket commitment table | STEP 3B: one row per ticket with Cell/VM Row ID and committed opening phrase | PASS |
| C-17 Role-phase vocabulary matrix | VOCABULARY MATRIX / MANIFEST: 5 roles × 3 phases = 15 cells, each with register description + template phrase | PASS |

Essential: 5/5 → **60.0 pts**
Recommended: 3/3 → **30.0 pts**
Aspirational shared: C-09–C-17 = 9 PASS

---

### Variation-Specific Evaluation (C-18 through C-21)

#### V-01 — Output Format: Explicit C-20 ZERO-EXCEPTION Headline Rule

| C | Criterion | Evidence | Score |
|---|-----------|----------|-------|
| C-18 | Vocabulary linkage | Cell IDs in `*(Cell: XX-P#)*` on `##` line → 3-node chain (matrix cell → commitment row → body header) fully traceable by ID lookup. Headline placement makes node-3 unambiguous. | **PASS** |
| C-19 | Vocabulary pre-flight gate | Gate present before body generation; checks 4 items (matrix completeness, commitment completeness, phrase traceability, phase-register alignment). 4 >= 3 required. | **PASS** |
| C-20 | Headline-level ID annotation | ZERO-EXCEPTION rule stated in STEP 3B, STEP 4, and TABLE CHECK. Pattern `## T-NN — {Title} *(Cell: XX-P#)*` specified. C-20 VERIFICATION MANIFEST row present. Scorer reading only `##` lines sees Cell ID. | **PASS** |
| C-21 | Complete 5-item pre-flight | Gate explicitly checks 4 items; item (e) inter-role register differentiation absent. PRE-FLIGHT RESULT: ALL PASS covers only (1)–(4). | **FAIL** |

**Aspirational score:** (9 shared + C-18 PASS + C-19 PASS + C-20 PASS + C-21 FAIL) = 12/13 × 10 = **9.231**
**Composite: 60.0 + 30.0 + 9.231 = 99.23**

---

#### V-02 — Lifecycle: Letter-Labeled 5-Item Gate for C-21

| C | Criterion | Evidence | Score |
|---|-----------|----------|-------|
| C-18 | Vocabulary linkage | VM Row IDs present in commitment table (STEP 3B) and VOCABULARY MANIFEST. Body header cites ID — but ID is on a metadata subline (`- VM Row: VM-xxx-P#`), not on the `##` line. Three-node chain exists but node-3 requires reading the subline. C-18 partial: ID is present but not on the `##` line. | **PARTIAL** |
| C-19 | Vocabulary pre-flight gate | Gate stands alone before STEP 4 PERFORMANCE MODE. All 5 items (a)–(e) present with explicit individual PASS/FAIL state. GATE: OPEN/CLOSED declaration. Blocking structure confirmed. | **PASS** |
| C-20 | Headline-level ID annotation | VM Row IDs explicitly placed in metadata subline format (`- VM Row: ...`). STEP 4 body header template shows `## T-NN -- {Title}` on one line and VM Row ID on the next metadata subline. Scorer reading only `##` lines cannot see the VM Row ID. | **FAIL** |
| C-21 | Complete 5-item pre-flight | Letters (a)–(e) each named with individual PASS/FAIL state. Item (e) = "inter-role register differentiation" requires citing two roles in same phase with distinct register descriptions by VM Row ID. GATE: OPEN when all five PASS. Example citation format specified. | **PASS** |

**Aspirational score:** 9 shared PASS + C-18 PARTIAL + C-19 PASS + C-20 FAIL + C-21 PASS = (11 PASS + 0.5 PARTIAL) / 13 × 10 = (11 + 0.5) / 13 × 10 = **8.846**
**Composite: 60.0 + 30.0 + 8.846 = 98.85**

---

#### V-03 — Phrasing Register: Compliance Contract (C-20 + C-21 front-loaded)

| C | Criterion | Evidence | Score |
|---|-----------|----------|-------|
| C-18 | Vocabulary linkage | COMPLIANCE CONTRACT names the `*(VM: VM-xxx-P#)*` annotation on `##` line as the canonical format. Compliant header sample in contract shows VM Row ID inline. CONSTRAINT MANIFEST adds explicit C-20 row. Three-node chain complete with headline-level node-3. | **PASS** |
| C-19 | Vocabulary pre-flight gate | Gate uses letter labels (a)–(e); positioned before STEP 4. GATE: OPEN/CLOSED declaration. | **PASS** |
| C-20 | Headline-level ID annotation | COMPLIANCE CONTRACT at prompt header states: "The annotation is NOT permitted on any subline, bullet, or metadata row." Compliant body header sample: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. CONSTRAINT MANIFEST row: "Tickets with VM Row ID in ## headline (Compliance Contract C-20) = total". VERIFICATION MANIFEST has C-20 row. Prohibition redundantly anchored before any step. | **PASS** |
| C-21 | Complete 5-item pre-flight | COMPLIANCE CONTRACT states: "The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e) is named 'inter-role register differentiation'." Gate structure follows with items (a)–(e) individually labeled. VERIFICATION MANIFEST row: "Gate items (a)–(e) all PASS — C-21 = 5". | **PASS** |

**Aspirational score:** 13/13 × 10 = **10.0**
**Composite: 60.0 + 30.0 + 10.0 = 100.0**

---

#### V-04 — Combined: V-01 Explicit Headline Rule + V-02 Letter-Labeled Gate

| C | Criterion | Evidence | Score |
|---|-----------|----------|-------|
| C-18 | Vocabulary linkage | Cell IDs in `*(Cell: XX-P#)*` on `##` line (from V-01). STEP 6 body template: `## T-NN -- {Title} *(Cell: XX-P#)*`. Three-node chain fully traceable by ID lookup without subline reading. | **PASS** |
| C-19 | Vocabulary pre-flight gate | Letter-labeled (a)–(e) gate (from V-02) with GATE: OPEN/CLOSED, positioned before STEP 4 PERFORMANCE MODE. | **PASS** |
| C-20 | Headline-level ID annotation | V-01 ZERO-EXCEPTION rule in STEP 3B, STEP 4, and TABLE CHECK retained. V-02 letter-labeled gate does not change headline placement. C-20 check row in TABLE CHECK explicitly confirms `*(Cell: XX-P#)*` inline. VERIFICATION MANIFEST C-20 row. | **PASS** |
| C-21 | Complete 5-item pre-flight | V-02 letter-labeled (a)–(e) gate with individual PASS/FAIL per item. Item (e) = "inter-role register differentiation" explicitly named. GATE: OPEN only when all five PASS. VERIFICATION MANIFEST row: "Gate items (a)–(e) all PASS — C-21 = 5". | **PASS** |

**Aspirational score:** 13/13 × 10 = **10.0**
**Composite: 60.0 + 30.0 + 10.0 = 100.0**

---

#### V-05 — Full Synthesis (R5 V-05 Base + Explicit C-20 Rule + Letter-Labeled C-21 Gate)

| C | Criterion | Evidence | Score |
|---|-----------|----------|-------|
| C-18 | Vocabulary linkage | VM Row IDs in `##` headline annotation (`*(VM: VM-SRE-P1)*` style). STEP 3B states ID must appear in `##` headline "completing the C-20 three-node traceability chain." STEP 4 PERFORMANCE MODE reiterates headline placement. | **PASS** |
| C-19 | Vocabulary pre-flight gate | Standalone gate (a)–(e) with GATE: OPEN/CLOSED before STEP 4. Three distinct anchors that reference the gate: STEP 3B, STEP 4, and VERIFICATION MANIFEST. | **PASS** |
| C-20 | Headline-level ID annotation | ZERO-EXCEPTION prohibition stated twice (STEP 3B: "completing the C-20 three-node traceability chain" + STEP 4 reiteration). CONSTRAINT MANIFEST row: "Tickets with VM Row ID in ## headline annotation (C-20) = total". VERIFICATION MANIFEST row: `## headlines with *(VM: VM-xxx-P#)* inline — C-20 = total`. Maximum redundancy of enforcement. | **PASS** |
| C-21 | Complete 5-item pre-flight | R5 V-05 gate upgraded to letter-label formalism: items (a)–(e) individually named with binary PASS/FAIL. VERIFICATION MANIFEST has two C-21 rows: "Gate items (a)–(e) all PASS — C-21 = 5" and "Item (e) inter-role example explicitly cited = 1". | **PASS** |

**Aspirational score:** 13/13 × 10 = **10.0**
**Composite: 60.0 + 30.0 + 10.0 = 100.0**

---

### Consolidated Scorecard

| Var | C-01–C-08 | C-09–C-17 | C-18 | C-19 | C-20 | C-21 | Aspir | Composite | All Ess? |
|-----|-----------|-----------|------|------|------|------|-------|-----------|---------|
| V-01 | 9 PASS | 9 PASS | PASS | PASS | **PASS** | **FAIL** | 9.23 | **99.23** | YES |
| V-02 | 9 PASS | 9 PASS | **PARTIAL** | PASS | **FAIL** | PASS | 8.85 | **98.85** | YES |
| V-03 | 9 PASS | 9 PASS | PASS | PASS | PASS | PASS | 10.0 | **100.0** | YES |
| V-04 | 9 PASS | 9 PASS | PASS | PASS | PASS | PASS | 10.0 | **100.0** | YES |
| V-05 | 9 PASS | 9 PASS | PASS | PASS | PASS | PASS | 10.0 | **100.0** | YES |

**Ranking:** V-03 = V-04 = V-05 (100.0) > V-01 (99.23) > V-02 (98.85)

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — Front-loaded compliance contract (V-03)**
Placing C-20 and C-21 obligations in a `COMPLIANCE CONTRACT` block before any step — including before the Vocabulary Manifest — anchors both rules at the earliest reading position. The contract provides a compliant header sample (`## T-NN -- {Title} *(VM: VM-xxx-P#)*`) so the model has a visual reference before encountering STEP 3B. V-03 uniquely tests whether front-loading outperforms step-embedded instructions. The contract approach has a secondary advantage: it distinguishes the meta-obligation from the step-level execution, creating a two-layer structure where the contract specifies *what must be true* and the steps specify *how to achieve it*.

**Signal 2 — Dual-location subline prohibition (V-05)**
V-05 states the C-20 subline prohibition in two distinct positions (STEP 3B description + STEP 4 PERFORMANCE MODE body format), not just in the rule statement. The STEP 4 instruction explicitly names the prohibited pattern ("Not on a subline. Not on a metadata row.") even though STEP 3B already covered it. The VERIFICATION MANIFEST echoes C-20 with a count row that the model must fill in. This triple-anchor pattern — STEP 3B rule + STEP 4 repeat + VERIFICATION MANIFEST row — turns C-20 from a single instruction into a running obligation that the output must confirm explicitly.

**Signal 3 — Item (e) inter-role differentiation as a named, citeable gate item (V-02, V-03, V-04, V-05)**
All four composite-100 candidates and V-02 share the same structural pattern for C-21: item (e) is not merely present — it requires citing two specific VM Row IDs in the same phase with distinct register descriptions. The GATE declaration language (`GATE: OPEN -- (a)(b)(c)(d)(e) all PASS`) makes counting impossible to shortcut; a gate saying "ALL PASS" over four unnamed items is qualitatively different from one that names all five and shows evidence for (e). The citation requirement turns (e) from an assertion into evidence.

**Signal 4 — VERIFICATION MANIFEST as output-embedded audit trail (V-03, V-04, V-05)**
All top-scoring variations add explicit VERIFICATION MANIFEST rows for C-20 (count of `##` headlines with inline ID) and C-21 (gate items (a)–(e) all PASS + item (e) cited). The manifest rows mean the model's own output contains the scoring evidence — a scorer need not infer compliance from ticket bodies, they can read the VERIFICATION MANIFEST row directly. This is the same pattern that made C-15 robust in prior rounds: making compliance auditable by output inspection rather than inference.

---

### Pattern Summary for R7

The R6 differentiators converge on one principle: **make compliance evidence output-embedded, not just instruction-stated.** A ZERO-EXCEPTION rule in STEP 3B is an instruction; the same rule appearing as a VERIFICATION MANIFEST row that the model fills in is evidence. The move from V-01 (instruction only) to V-03/V-04/V-05 (instruction + manifest row + TABLE CHECK + VERIFICATION row) closes the gap because the output cannot claim compliance without producing the traceable evidence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Front-loaded compliance contract before all steps provides maximum-earliest obligation anchor with compliant format sample", "Dual-location subline prohibition (STEP 3B + STEP 4) turns a single rule into a running obligation reinforced at each generation site", "Item (e) inter-role differentiation requires explicit VM Row ID citation pair rather than assertion, making C-21 evidence-based not assertion-based", "VERIFICATION MANIFEST rows for C-20 and C-21 embed scoring evidence in the output itself, enabling audit by manifest inspection rather than body text inference"]}
```
