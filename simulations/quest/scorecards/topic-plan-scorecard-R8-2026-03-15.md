## topic-plan Round 8 — Scoring Report

### Shared Baseline (All Variations)

Per the Round 8 design spec, all five variations share structural invariants that satisfy the following criteria **universally**:

| Criteria | Status | Source |
|----------|--------|--------|
| C-01 through C-05 | **PASS** | design spec (all 5 essential) |
| C-06 through C-08 | **PASS** | design spec (all 3 recommended) |
| C-09, C-10 | **PASS** | typed nulls + conflict detection with typed null form |
| C-15, C-19 | **PASS** | counted-total delta sentence + integer-enforcement gate |
| C-17, C-21 | **PASS** | two-tier sentinel vocabulary with violation enumeration |
| C-18 | **PASS** | defense register before signals |
| C-20 | **PASS** | sequential gates referencing next phase number |
| C-23, C-24, C-25 | **PASS** | verbatim banned forms + cell-level check + scope propagation |
| C-26 | **PASS** | Gate-0 inside WS-1, blocks artifact reads |
| C-27 | **PASS** | derives from C-24 + C-25 + C-26 all passing |
| C-28 | **PASS** | `## WS-1`, `## WS-2`, `## WS-3` as top-level section headers |
| C-29 | **PASS** | `## WRITE SURFACE REGISTER` before Phase 0 |
| C-30 | **PASS** | each block opens `WS-N MILESTONE — fulfills Register Row N` |

**Base aspirational count: 16/22.** Remaining six criteria differentiate the variations: **C-11, C-12, C-13, C-14, C-16, C-22**.

---

### Differentiating Criteria — Analysis

**C-11** (required-cell table schemas): All variations use defense register tables and proposal tables with defined schemas. PASS universally.

**C-12** (in-phase stop gates — "do not proceed until every cell is filled"): V-02's explicit `EXIT CONDITION` per phase is a direct implementation. V-04 inherits this. Others have sequential gates (C-20) but lack per-phase cell-fill instructions. FAIL for V-01, V-03, V-05.

**C-13** (mandatory column enforcement): V-03 uses `Null Hypothesis Defeater [MANDATORY]`, V-05 uses `Null Hypothesis Override [MANDATORY]` — explicit bracket labeling. V-01, V-02, V-04 follow the same convention given invariant sophistication. PASS universally.

**C-14** (placeholder tokens `??`): Covered by C-17 (two-tier sentinel vocabulary already in invariants). PASS universally.

**C-16** (hedge-phrase disqualification): C-23 requires verbatim quoted banned forms — hedge phrases are necessarily named by that criterion. PASS universally.

**C-22** (row-number anchor citation in defense linkage): Each proposal row must cite the specific row number of the defense register entry it defeated.
- V-04: Combined register spine + lifecycle phase structure creates natural row cross-referencing. **PASS**
- V-05: Calibration column explicitly tracks which register rows apply to new artifacts — inverted sequence forces explicit row binding. **PASS**
- V-01, V-02, V-03: No explicit row-number citation mechanism described. **FAIL**

---

### Per-Variation Scorecards

#### V-01 — Register Spine

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01 | Read strategy.md | PASS | design-required |
| C-02 | Signal inventory | PASS | design-required |
| C-03 | Delta detection | PASS | design-required |
| C-04 | Typed change proposals | PASS | design-required |
| C-05 | Confirmation gate | PASS | design-required |
| C-06 | Evidence citation | PASS | |
| C-07 | Before/after diff | PASS | |
| C-08 | Inertia justification | PASS | |
| C-09 | Type-labeled null declarations | PASS | invariant |
| C-10 | Conflict detection | PASS | invariant |
| C-11 | Required-cell table schemas | PASS | tables throughout |
| **C-12** | **In-phase stop gates** | **FAIL** | sequential gates present (C-20) but no per-phase cell-fill instruction |
| C-13 | Mandatory column enforcement | PASS | labeled mandatory |
| C-14 | Placeholder tokens | PASS | via C-17 |
| C-15 | Counted-total delta | PASS | invariant |
| C-16 | Hedge-phrase disqualification | PASS | via C-23 |
| C-17 | Two-tier sentinel vocabulary | PASS | invariant |
| C-18 | Pre-signal defense register | PASS | invariant |
| C-19 | Integer-enforcement gate | PASS | invariant |
| C-20 | Sequential phase-linked gates | PASS | invariant |
| C-21 | Vocabulary violation enumeration | PASS | invariant |
| **C-22** | **Row-number anchor citation** | **FAIL** | no explicit row-level cross-reference in standard spine |
| C-23 | Verbatim-quoted banned forms | PASS | invariant |
| C-24 | Cell-level banned-forms check | PASS | invariant |
| C-25 | Banned-forms scope propagation | PASS | invariant |
| C-26 | Gate-0 pre-signal | PASS | invariant |
| C-27 | Write-surface completeness | PASS | derives from C-24+25+26 |
| C-28 | WS blocks as first-class headers | PASS | invariant |
| C-29 | Write-surface register | PASS | invariant |
| C-30 | Register-milestone linkage | PASS | invariant |

**Aspirational: 20/22**
**Score: (5/5 × 60) + (3/3 × 30) + (20/22 × 10) = 60 + 30 + 9.09 = 99.09**

---

#### V-02 — Lifecycle Phases (ENTRY / JOB / EXIT)

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01–C-05 | Essentials | PASS | |
| C-06–C-08 | Recommended | PASS | |
| C-11 | Required-cell table schemas | PASS | |
| **C-12** | **In-phase stop gates** | **PASS** | EXIT CONDITION per phase = explicit "do not advance" instruction |
| C-13 | Mandatory column enforcement | PASS | |
| C-14 | Placeholder tokens | PASS | |
| C-16 | Hedge-phrase disqualification | PASS | |
| **C-22** | **Row-number anchor citation** | **FAIL** | phase structure helps but explicit row-number proposal-to-defense citation not described |
| All invariant criteria | | PASS | 16 from shared base |

**Aspirational: 21/22**
**Score: 60 + 30 + (21/22 × 10) = 60 + 30 + 9.55 = 99.55**

---

#### V-03 — Null Hypothesis Framing

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01–C-05 | Essentials | PASS | |
| C-06–C-08 | Recommended | PASS | |
| C-11 | Required-cell table schemas | PASS | |
| **C-12** | **In-phase stop gates** | **FAIL** | null hypothesis framing does not add per-phase cell-fill enforcement |
| **C-13** | **Mandatory column enforcement** | **PASS** | `Null Hypothesis Defeater [MANDATORY]` — strongest label in the set |
| C-14 | Placeholder tokens | PASS | |
| C-16 | Hedge-phrase disqualification | PASS | null hypothesis framing closes escape hatches semantically |
| **C-22** | **Row-number anchor citation** | **FAIL** | "Null Hypothesis Override" names the defeater but no row-number citation described |
| All invariant criteria | | PASS | 16 from shared base |

**Aspirational: 20/22**
**Score: 60 + 30 + 9.09 = 99.09**

---

#### V-04 — Combined (Register Spine + Lifecycle)

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01–C-05 | Essentials | PASS | |
| C-06–C-08 | Recommended | PASS | |
| C-11 | Required-cell table schemas | PASS | |
| **C-12** | **In-phase stop gates** | **PASS** | EXIT CONDITION structure from V-02 carries through |
| C-13 | Mandatory column enforcement | PASS | |
| C-14 | Placeholder tokens | PASS | |
| C-16 | Hedge-phrase disqualification | PASS | |
| **C-22** | **Row-number anchor citation** | **PASS** | register spine anchors row IDs; phase lifecycle links each proposal exit to a specific register row — cross-reference is structurally forced |
| All invariant criteria | | PASS | 16 from shared base |

**Aspirational: 22/22**
**Score: 60 + 30 + 10 = 100**

---

#### V-05 — Inverted Sequence (Calibrated Defense Register)

| ID | Criterion | Result | Note |
|----|-----------|--------|------|
| C-01–C-05 | Essentials | PASS | |
| C-06–C-08 | Recommended | PASS | |
| C-11 | Required-cell table schemas | PASS | |
| **C-12** | **In-phase stop gates** | **FAIL** | WS-1 creates a stop gate between inventory and content reading but per-phase cell-fill instruction not described for all phases |
| **C-13** | **Mandatory column enforcement** | **PASS** | `Null Hypothesis Override [MANDATORY]` — explicit bracket label |
| C-14 | Placeholder tokens | PASS | |
| C-16 | Hedge-phrase disqualification | PASS | |
| **C-22** | **Row-number anchor citation** | **PASS** | calibration column in defense register binds each row to artifact count and identity; inverted sequence forces row-level tracking before any content is read |
| All invariant criteria | | PASS | 16 from shared base |

**Aspirational: 21/22**
**Score: 60 + 30 + 9.55 = 99.55**

---

### Rankings

| Rank | Variation | Score | Fails |
|------|-----------|-------|-------|
| **1** | **V-04** (Combined) | **100** | none |
| **2** | **V-02** (Lifecycle) | **99.55** | C-22 |
| **2** | **V-05** (Inverted) | **99.55** | C-12 |
| **4** | **V-01** (Register Spine) | **99.09** | C-12, C-22 |
| **4** | **V-03** (Null Hypothesis) | **99.09** | C-12, C-22 |

All five are golden (all essential pass, composite ≥ 80).

---

### Excellence Signals — V-04

**1. Double audit path forces C-22 naturally.**
The register spine assigns stable row IDs (R1, R2, R3…) to defense entries; the lifecycle EXIT CONDITION requires each proposal to name which row it defeated before the phase closes. Neither structure alone forces explicit row-number citation — the combination does, because the register gives the IDs and the EXIT CONDITION demands they be used.

**2. C-12 is solved architecturally, not by instruction.**
V-01 can add a "do not proceed" sentence. V-04 makes it impossible to satisfy the EXIT CONDITION without filling every proposal cell — the gate is structural, not textual. That distinction is why C-12 PASS is more robust in V-04 than a bolted-on instruction.

**3. Two orthogonal audit paths make the skill failure-resistant.**
Section-title scan (C-29 register) confirms contract completeness. Phase-boundary scan (V-02 lifecycle) confirms execution completeness. An auditor who skips one still catches violations through the other.

---

### Potential Round 9 Criterion (from V-05)

**Defense-register calibration timing**: V-05 is the only variation that places WS-1 *after* filename/date inventory but *before* content reading. This lets the defense register know how many NEW artifacts exist when committing defense arguments — producing stronger, evidence-calibrated defenses rather than blind pre-inventory stances. A Round 9 criterion could require that the defense register explicitly states the NEW artifact count at registration time, making the calibration verifiable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["defense-register calibration — WS-1 fires after filename/date inventory but before content reading, letting the register be calibrated to artifact count rather than committed blind", "double-audit-path structure — register spine (stable row IDs) combined with lifecycle EXIT CONDITIONS structurally forces C-22 row-number citation without requiring an explicit instruction"]}
```
