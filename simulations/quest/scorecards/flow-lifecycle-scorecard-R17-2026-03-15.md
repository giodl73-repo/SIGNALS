---

## flow-lifecycle — Round 17 Scoring (rubric v17, C-50 + C-51)

**Scoring basis:** Denominator 51. Floor invariant (C-01 through C-49) holds for all five variations. The only discriminating criteria are C-50, C-51, and C-48 (which V-03 weakens to PARTIAL by dissolving enforcement vocabulary into prose). PARTIAL = 0.5 points.

---

### Per-Criterion Discriminator Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| **C-01 through C-49 (floor)** | PASS | PASS | PASS* | PASS | PASS |
| **C-48** (per-field inline token) | PASS | PASS | **PARTIAL** | PASS | PASS |
| **C-50** (pre-table Protocol block) | FAIL | **PASS** | FAIL | PARTIAL | **PASS** |
| **C-51** (leading-clause token) | **PASS** | FAIL | FAIL | PARTIAL | **PASS** |

*V-03 holds C-48 in the floor count but scores PARTIAL (parenthetical prose guidance does not carry discrete inline tokens); all other floor criteria hold.

---

### Per-Variation Scoring

#### V-01 — Output Format: Leading-Clause Enforcement Tokens

| Block | Assessment |
|-------|-----------|
| Essential C-01–C-05 | PASS: all five essential criteria carried from floor |
| Recommended C-06–C-08 | PASS |
| Aspirational C-09–C-49 | PASS: full R16 V-05 floor invariant |
| **C-50** (pre-table Protocol block) | **FAIL** — no pre-table FM-ID Protocol block; C-48 field-cell tokens are the single enforcement layer; D-16 (missing section-entry block) remains open |
| **C-51** (leading-clause token) | **PASS** — every SQ Declaration field cell opens with "does not count; Mandatory -- [Field]:" as its first expression; D-15 structurally blocked; truncation cannot displace the qualifying token |

**Composite: 50/51** — D-15 closed, D-16 open. Single-layer defense at the cell level.

---

#### V-02 — Inertia Framing: Pre-Table FM-ID Protocol Block

| Block | Assessment |
|-------|-----------|
| Essential C-01–C-05 | PASS |
| Recommended C-06–C-08 | PASS |
| Aspirational C-09–C-49 | PASS: full floor |
| **C-50** (pre-table Protocol block) | **PASS** — named FM-ID PROTOCOL section appears before the SQ Declaration table; covers all four fields with specific "does not count" language for each; establishes section-entry encounter independent of field cells; D-16 structurally blocked |
| **C-51** (leading-clause token) | **FAIL** — tokens present per-field at C-48 floor level but in trailing position ("FM-01 -- first failure mode: ... does not count" rather than "does not count; Mandatory -- FM-01:"); D-15 (trailing-position truncation) remains open |

**Composite: 50/51** — D-16 closed, D-15 open. Single-layer defense at the section-entry level.

---

#### V-03 — Phrasing Register: Descriptive Prose Dissolves Enforcement

| Block | Assessment |
|-------|-----------|
| Essential C-01–C-05 | PASS |
| Recommended C-06–C-08 | PASS |
| Aspirational C-09–C-47 | PASS: floor |
| **C-48** (per-field inline token) | **PARTIAL** — parenthetical guidance embedded in prose descriptions ("Try to be specific... rather than naming only the department") is not a discrete inline token; "does not count" vocabulary is absent as a standalone expression; AC-23 would score PARTIAL because the fail condition is only inferrable from the instructional positive, not stated directly |
| **C-50** (pre-table Protocol block) | **FAIL** — no pre-table Protocol block; section header is descriptive ("Before beginning the lifecycle trace, describe..."); D-16 open |
| **C-51** (leading-clause token) | **FAIL** — no field cell begins with enforcement vocabulary; all cells open with field name and descriptive instruction; D-15 open |

**Composite: 48.5/51** — documents both failure modes (D-15 and D-16) and validates C-49 mutual-audit design principle by negative example: when enforcement vocabulary is dissolved into prose, the practitioner reads content instructions and infers fail conditions rather than encountering them directly.

---

#### V-04 — Role Sequence + Lifecycle Emphasis: Phase-First Framing Dilutes SQ Block

| Block | Assessment |
|-------|-----------|
| Essential C-01–C-05 | PASS |
| Recommended C-06–C-08 | PASS |
| Aspirational C-09–C-49 | PASS: floor |
| **C-50** (pre-table Protocol block) | **PARTIAL** — FM-ID NOTE block exists before the SQ Declaration table, but covers only failure mode fields (FM-01, FM-02) with "does not count" language; Incumbent Process and Inertia Driver fields are not covered by the Protocol block; AC-24 would score PARTIAL ("a note that covers only failure mode fields is PARTIAL, not PASS") |
| **C-51** (leading-clause token) | **PARTIAL** — FM-01 and FM-02 field cells carry "does not count; Mandatory --" leading tokens; Incumbent Process and Inertia Driver cells carry trailing tokens ("...does not count; Mandatory" at end); AC-25 would score PARTIAL ("all four fields must have leading tokens for PASS") |

**Composite: 50/51** — Phase-first framing concentrates attention on failure mode fields as "critical" while treating Incumbent Process and Inertia Driver as contextual, producing asymmetric coverage that leaves exactly the fields the author considers secondary without leading-clause protection. Discrimination is visible in AC-24 and AC-25 PARTIAL rows.

---

#### V-05 — Full Dual-Encounter Defense-in-Depth

| Block | Assessment |
|-------|-----------|
| Essential C-01–C-05 | PASS |
| Recommended C-06–C-08 | PASS |
| Aspirational C-09–C-49 | PASS: full floor |
| **C-50** (pre-table Protocol block) | **PASS** — named FM-ID PROTOCOL section before the SQ Declaration table; governs all four fields uniformly (Incumbent Process, FM-01, FM-02, Inertia Driver); each field has a dedicated bullet naming what "does not count"; block closes with production instruction ("Author the STATUS-QUO PROCESS DECLARATION completely before proceeding to STEP 0A"); AC-24 PASS |
| **C-51** (leading-clause token) | **PASS** — every field cell begins with "does not count; Mandatory -- [Field]: [description]"; qualifying token is the first expression in every cell; D-15 structurally blocked because token cannot be truncated or scrolled past; AC-25 PASS |

**Composite: 51/51** — D-14 closed (per-field token present, C-48), D-15 closed (leading-clause position, C-51), D-16 closed (Protocol block at section entry, C-50). The two encounter points are structurally independent: an author who skips the Protocol block still encounters the leading-clause token as the first expression in each field; an author who skips directly to cell fill encounters the token before any content instruction. Both defenses must be actively bypassed simultaneously to defeat enforcement.

---

### Composite Scores and Ranking

| Rank | Variation | Score | C-50 | C-51 | Key Discriminator |
|------|-----------|-------|:----:|:----:|-------------------|
| **1** | **V-05** | **51/51 (100%)** | PASS | PASS | Both encounter points operational; D-14+D-15+D-16 all closed |
| **2 (tied)** | V-01 | 50/51 (98%) | FAIL | PASS | D-15 closed; D-16 open |
| **2 (tied)** | V-02 | 50/51 (98%) | PASS | FAIL | D-16 closed; D-15 open |
| **2 (tied)** | V-04 | 50/51 (98%) | PARTIAL | PARTIAL | Both failure modes half-closed; phase-first framing dilutes uniform coverage |
| **5** | V-03 | 48.5/51 (95%) | FAIL | FAIL | Both failure modes open; C-48 weakened to PARTIAL |

**Within the three-way tie (V-01, V-02, V-04):** Each achieves 50/51 by different means. V-01 and V-02 close one distinct failure mode fully while leaving the other structurally open — these are orthogonal single-layer defenses. V-04 achieves the same score arithmetically but through partial coverage on both — neither failure mode is fully closed. V-04 is architecturally weaker despite identical raw score because its partials are field-asymmetric: the fields the author perceived as "contextual" (Incumbent Process, Inertia Driver) received neither Protocol block coverage nor leading-clause tokens, while the fields perceived as "critical" (FM-01, FM-02) received both. This asymmetry would be invisible to a practitioner filling the prompt — the two unprotected fields carry no enforcement signal at section entry or as a leading clause.

---

### Excellence Signals from V-05

**Signal E-01: Dual-encounter independence is the structural property, not additive redundancy.** V-05's two enforcement layers are not redundant backups for the same signal — they operate at different moments in the authoring sequence. The Protocol block fires at section entry (before any cell is open). The leading-clause token fires at cell-fill time (when the practitioner decides what to write). A practitioner who reads the Protocol block conceptually primes the cell-fill expectation; a practitioner who skips directly to cell fill encounters the constraint as the first expression in the cell before any content instruction. The combination cannot be passively bypassed because the two encounter moments are separated in time and activity — one requires skipping an entire named section, the other requires ignoring the first clause of every cell. Only active effort defeats both.

**Signal E-02: Protocol block must govern ALL fields uniformly.** V-04 shows the failure mode when a Protocol block covers only "important" fields: the author's cognitive framing of field priority determines which fields receive section-entry defense. The fix is not to make the block longer — it is to structure the block as a per-field enumeration that names every SQ Declaration field explicitly. V-05's Protocol block has a dedicated bullet for each of the four fields, making it structurally impossible to read the block and not encounter Incumbent Process and Inertia Driver constraints alongside FM-01 and FM-02. Uniform field coverage in the Protocol block is a necessary condition for C-50 PASS; field-selective coverage is the exact failure mode C-50 was designed to block.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-encounter independence: Protocol block fires at section entry and leading-clause token fires at cell-fill time — the two enforcement points operate at structurally different moments in the authoring sequence and cannot both be passively bypassed simultaneously", "Protocol block must enumerate every SQ Declaration field by name — field-selective coverage (failure modes only) leaves the fields the author perceives as contextual without section-entry defense, producing asymmetric enforcement invisible to the practitioner"]}
```
