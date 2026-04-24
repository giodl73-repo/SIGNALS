Now I have all five variates fully read. Let me score them.

---

# Scorecard — campaign-evidence (Round 13)

## Rubric Framework (v13)

- **Essential** (60 pts): C-01 through C-04 — 4 criteria × 15 pts
- **Recommended** (30 pts): C-05 through C-07 — 3 criteria × 10 pts
- **Aspirational** (10 pts): C-08 through C-34 — 27 criteria, proportional

---

## Per-Variation Scoring

### V-01 — Role Sequence (Provenance Activation at Handoff Boundary)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Multi-stage campaign (5 stages) | PASS | 5 named stages declared in sequence; "Role passes to" at each boundary |
| C-02 | Evidence before hypothesis | PASS | SEQUENCING RULE enforced; S3 blocked behind S2 exit gate |
| C-03 | Hypotheses with falsification conditions | PASS | FALSIFICATION RULE at S3/S5; exit gate verifies non-blank conditions |
| C-04 | Self-contained output | PASS | OUTPUT ASSEMBLY section; brief header + stage outputs + synthesis + audit table |
| C-05 | Source attribution per claim | PASS | ATTRIBUTION RULE with stage labels [web]/[intel]/[hypothesis]/[analysis]/[synthesis]; 70%+ requirement stated |
| C-06 | Synthesis distinguishes consensus from conflict | PASS | Stage 5 explicitly requires separate "Consensus findings" and "Conflicts" sections |
| C-07 | Calibrated confidence levels | PASS | CALIBRATION RULE anti-uniformity guard: "If all ratings are identical, CALIBRATION fails" |
| C-08 | Gaps and open questions | PASS | Stage 5 output step 4: "Gaps and open questions" |
| C-09 | Decision readiness signal | PASS | Stage 5 step 5: decision readiness; output assembly requires it |
| C-10 | Hypotheses post-evidence | PASS | SEQUENCING RULE; named principle encoded in rule declaration |
| C-11 | Anti-uniformity guard | PASS | Explicit anti-uniformity guard in CALIBRATION RULE with "If all ratings are identical, CALIBRATION fails" |
| C-12 | Decision readiness one sentence | PASS | "one sentence naming posture and, if not ready, the specific gap" — compressed by design |
| C-13 | Named rules invoked at point of use | PASS | Rules named in preamble (ATTRIBUTION, CALIBRATION, etc.); invoked by identifier at each stage |
| C-14 | Hypothesis reordering rationale stated | PASS | SEQUENCING RULE includes: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis" |
| C-15 | Sequencing formalized as named rule | PASS | SEQUENCING RULE is a peer-tier named rule referenceable by identifier |
| C-16 | Zero-gap rule invocation | PASS | 5 rules × 5 stages = 25 cells; all handled (positive or explicit negative) |
| C-17 | Coverage map prospective | PASS | Coverage Map in preamble: "finalized before Stage 1 begins and cannot be modified" |
| C-18 | All rules peer tier | PASS | "all five rules are peers; no rule is primary"; explicit peer declaration |
| C-19 | Coverage map immutability declared | PASS | "immutable — sealed at preamble; cannot be modified after execution begins" |
| C-20 | Rule scope inline in declaration | PASS | Every rule has `[invoked at: S1(+), S2(+), ...]` inline annotation within rule body |
| C-21 | Interrogative invocation at critical rules | PASS | All invocations use `[ Yes / No ]` binary form |
| C-22 | Universal binary invocation | PASS | Every applicable stage invocation uses `[ Yes / No ]`; non-applicable use explicit `[ No -- reason ]` |
| C-23 | Stage-indexed invocation trail | PASS | `[S1 of 5]`, `[S2 of 5]`, ... suffix on every invocation |
| C-24 | Per-stage entry/exit conditions | PASS | Explicit ENTRY GATE and EXIT GATE tables at every stage |
| C-25 | Gate record as output artifact | PASS | OUTPUT ASSEMBLY step 2 includes "Filled gate record"; pre-templated blank in preamble |
| C-26 | Consolidated audit table with derivable count | PASS | Output assembly includes audit table; delivery gate: "confirm count equals 25 (5 rules × 5 stages)" — derivable |
| C-27 | Gate record pre-templated blank in preamble | PASS | Gate Record Template with blank `[ ]` cells in GOVERNANCE PREAMBLE |
| C-28 | Sequencing as machine-verifiable column | **FAIL** | No evidence table with Stage column; SEQUENCING enforced via narrative order and invocation tags only — not sort-verifiable |
| C-29 | Extensible without static updates | PASS | "Adding a new peer rule propagates automatically through the coverage map and checksum; no static integers require manual update" |
| C-30 | Named handoff actors with transfer declarations | PASS | Every boundary has "Role passes to: Stage N — Role Name" + artifact enumeration |
| C-31 | Negative invocation at non-applicable stages | PASS | Every non-applicable cell has explicit negative: "CALIBRATION [S1 of 5]: Applicable at evidence collection? [ No — confidence governs analysis ]" |
| C-32 | Role access scope per stage | PASS | Role Roster table with "Authorized Reads" column; note explicitly says "access scope only — provenance activation occurs at handoff, not here" |
| C-33 | Derivable checksum pre-declared | PASS | "25 artifacts = 15 positive + 10 negative (5 rules × 5 stages)... updates automatically if rules or stages are added" |
| C-34 | Artifact provenance tags in scope-restricted stages | PASS | PROVENANCE RULE activated at handoff S2-to-S3, S3-to-S4, S4-to-S5; every claim in S3/S4/S5 requires `[source: Stage N — Artifact Name]`; exit gates verify |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 26/27

```
composite = (4/4 × 60) + (3/3 × 30) + (26/27 × 10)
          = 60 + 30 + 9.63
          = 99.63
```

**Score: 99.63 / 100**

---

### V-02 — Output Format (Stage-Indexed Evidence Table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Multi-stage campaign (5 stages) | PASS | 5 named stages; "Role passes to" at each boundary |
| C-02 | Evidence before hypothesis | PASS | SEQUENCING RULE enforced; S3 entry gate requires S2 exit-Pass and both S1+S2 rows in Evidence Table |
| C-03 | Hypotheses with falsification conditions | PASS | Hypotheses Table has Falsification-Condition column; non-blank required at S3 exit gate |
| C-04 | Self-contained output | PASS | OUTPUT ASSEMBLY produces coherent Master Evidence Table + Hypotheses Table + Synthesis Table + audit |
| C-05 | Source attribution per claim | PASS | Stage column in every Evidence Table row; 70%+ requirement; unlabeled rows are attribution violations |
| C-06 | Synthesis distinguishes consensus from conflict | PASS | Synthesis Table distinguishes Consensus vs Conflict row types |
| C-07 | Calibrated confidence levels | PASS | Anti-uniformity guard as column constraint: "if min(Confidence) = max(Confidence) across S4/S5 rows, CALIBRATION fails" |
| C-08 | Gaps and open questions | PASS | Gap row type in Synthesis Table |
| C-09 | Decision readiness signal | PASS | Decision-Readiness row type in Synthesis Table |
| C-10 | Hypotheses post-evidence | PASS | SEQUENCING RULE + Stage column sort-verifiable |
| C-11 | Anti-uniformity guard | PASS | Column-level constraint: if min=max across Confidence values, CALIBRATION fails |
| C-12 | Decision readiness one sentence | PASS | "Decision-Readiness row present (one sentence)" — one row, one sentence |
| C-13 | Named rules invoked at point of use | PASS | Rules named in preamble; invoked by name in per-stage invocation tables |
| C-14 | Hypothesis reordering rationale | PASS | "Named principle: 'A hypothesis anchored before evidence gathering is a bias, not a hypothesis.' This principle is the reason the Stage column exists." |
| C-15 | Sequencing as named rule | PASS | SEQUENCING RULE named; principle explicitly encoded as named rule |
| C-16 | Zero-gap invocation coverage | PASS | 25-cell coverage map; all cells addressed in per-stage invocation tables |
| C-17 | Coverage map prospective | PASS | Coverage Map in preamble: "sealed"; stage execution blocked until preamble finalized |
| C-18 | All rules peer tier | PASS | "all five rules are peers; no rule is primary"; explicit peer declaration |
| C-19 | Coverage map immutability | PASS | "This map is sealed. Columns cannot be added or removed after any stage executes." |
| C-20 | Rule scope inline in declaration | PASS | Every rule has `[invoked at: S1(+), ...]` inline annotation |
| C-21 | Interrogative invocation at critical rules | PASS | Per-stage invocation tables use questions: "Are all S1 rows labeled...?" |
| C-22 | Universal binary invocation | PASS | All applicable invocations use `[ Yes / No ]`; non-applicable carry `[ No ]` in table |
| C-23 | Stage-indexed trail | PASS | `[S1]`, `[S2]` suffixes in invocation tables |
| C-24 | Per-stage entry/exit conditions | PASS | Entry gate and exit gate at every stage |
| C-25 | Gate record as output artifact | PASS | Output assembly step 3: "Filled gate record"; blank template pre-instantiated in preamble |
| C-26 | Audit table with derivable count | PASS | Output assembly step 7: "25 rows (one per coverage map cell)"; "Derivable from table dimensions" |
| C-27 | Gate record pre-templated blank | PASS | Gate Record Template in preamble with blank cells |
| C-28 | Sequencing as machine-verifiable column | **PASS** | Evidence Table has Stage column; "sort the stage column; any hypothesis row appearing before evidence rows is a structural violation"; grounded-in constraint: hypothesis rows (Stage=S3) may only reference Source-Stage in {S1,S2} |
| C-29 | Extensible without static updates | PASS | "Adding a new peer rule adds a row to the coverage map and a column to the invocation audit table. No static integer requires manual update." |
| C-30 | Named handoff actors | PASS | "Role passes to: Stage N — Role Name" at each boundary |
| C-31 | Negative invocation at non-applicable stages | PASS | Invocation tables include explicit N/A rows with "Not applicable at..." statements |
| C-32 | Role access scope per stage | PASS | Role Roster with "Authorized Source-Stage Values" column |
| C-33 | Derivable checksum | PASS | "25 artifacts = 15 positive + 10 negative. Derivable from table dimensions." |
| C-34 | Artifact provenance tags | PASS | Source-Stage and Source-Artifact columns in Hypotheses Table; PROVENANCE RULE as column-constraint verification |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 27/27

```
composite = (4/4 × 60) + (3/3 × 30) + (27/27 × 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100**

---

### V-03 — Lifecycle Emphasis (Dual-Phase Interrogatives)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Multi-stage campaign | PASS | 5 named stages; "Role passes to" at each boundary |
| C-02 | Evidence before hypothesis | PASS | SEQUENCING RULE with dual-phase; S3 blocked behind S2 exit |
| C-03 | Hypotheses with falsification conditions | PASS | FALSIFICATION RULE dual-phase at S3/S5; pre/post verification for falsification conditions |
| C-04 | Self-contained output | PASS | OUTPUT ASSEMBLY includes all sections in narrative format |
| C-05 | Source attribution | PASS | ATTRIBUTION RULE invoked at all 5 stages via dual-phase |
| C-06 | Consensus/conflict separation | PASS | Stage 5 requires separate consensus and conflicts sections |
| C-07 | Calibrated confidence | PASS | Anti-uniformity guard: "if all findings carry the same confidence level, calibration is insufficient, regardless of whether the level is High, Medium, or Low" |
| C-08 | Gaps surfaced | PASS | Stage 5 output step 4: gaps and open questions |
| C-09 | Decision readiness signal | PASS | Stage 5 step 5: one-sentence decision readiness |
| C-10 | Hypotheses post-evidence | PASS | SEQUENCING RULE with dual-phase pre/post verification |
| C-11 | Anti-uniformity guard | PASS | Explicit guard in CALIBRATION RULE |
| C-12 | One-sentence decision readiness | PASS | "5. Decision readiness: one sentence naming posture" |
| C-13 | Named rules at point of use | PASS | Rules named in preamble; invoked by name with dual-phase labels at every stage |
| C-14 | Reordering rationale | PASS | Named principle in SEQUENCING RULE: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis" |
| C-15 | Sequencing as named rule | PASS | SEQUENCING RULE is named and peer-tier |
| C-16 | Zero-gap invocation | PASS | Every rule invoked at every stage (40 total artifacts = 30 dual-phase + 10 negative); all cells covered |
| C-17 | Coverage map prospective | PASS | Dual-Phase Coverage Map in preamble: "Finalized before Stage 1 begins. Immutable after execution starts." |
| C-18 | All rules peer tier | PASS | "all five rules are peers; no rule is primary" |
| C-19 | Coverage map immutability | PASS | "Immutable after execution starts" |
| C-20 | Rule scope inline | PASS | Every rule has `[invoked at: ...]` and `[dual-phase: ...]` inline annotations |
| C-21 | Interrogative invocation at critical rules | PASS | All applicable invocations use interrogative form: "Will X hold? [Yes/No]" and "Does X hold? [Yes/No]" — surpasses C-21 requirement |
| C-22 | Universal binary invocation | PASS | Every applicable invocation uses `[ Yes / No ]`; non-applicable use `[ No ]` |
| C-23 | Stage-indexed trail | PASS | `[Stage 1 of 5, PRE-EXECUTION]`, `[Stage 1 of 5, POST-EXECUTION]` suffixes on every invocation |
| C-24 | Per-stage entry/exit conditions | PASS | Entry gate and exit gate at every stage |
| C-25 | Gate record as output artifact | PASS | Output assembly step 3: "Filled gate record"; pre-templated in preamble |
| C-26 | Audit table derivable count | PASS | "Count rows... Must equal 40"; formula: "(15 × 2) + (10 × 1) = 40" — derivable from map dimensions |
| C-27 | Gate record pre-templated blank | PASS | Gate Record Template with blank cells in preamble |
| C-28 | Sequencing as machine-verifiable column | **FAIL** | No Evidence Table with Stage column; SEQUENCING verified via interrogative invocations only — not sort-verifiable by column value |
| C-29 | Extensible without static updates | PASS | "Coverage map auto-extends when a new peer rule is added. Invocation checksum updates accordingly." |
| C-30 | Named handoff actors | PASS | "Role passes to: Stage N — Role Name" at each boundary |
| C-31 | Negative invocation at non-applicable stages | PASS | Every non-applicable cell has explicit single-phase negative: "CALIBRATION [S1 of 5]: Not applicable at evidence collection... [ No ]" |
| C-32 | Role access scope per stage | PASS | Role Roster and Access Scopes table |
| C-33 | Derivable checksum | PASS | "Invocation checksum: 40 invocation artifacts = 30 dual-phase answers + 10 negative checks, derived from: (15 positive × 2) + (10 negative × 1)" |
| C-34 | Artifact provenance tags | PASS | PROVENANCE RULE dual-phase at S3/S4/S5; exit gates verify `[source: Stage N — Artifact Name]` |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 26/27

```
composite = (4/4 × 60) + (3/3 × 30) + (26/27 × 10)
          = 60 + 30 + 9.63
          = 99.63
```

**Score: 99.63 / 100**

---

### V-04 — Phrasing Register (RFC SHALL/MUST)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Multi-stage campaign | PASS | 5 named stages with "HANDOFF: Role passes to" at each boundary |
| C-02 | Evidence before hypothesis | PASS | REQ-SEQ-01: "SHALL complete evidence stages (S1, S2) before declaring any hypothesis (S3)" |
| C-03 | Hypotheses with falsification conditions | PASS | REQ-FAL-01: "SHALL include an explicit falsification condition with each hypothesis" |
| C-04 | Self-contained output | PASS | OUTPUT ASSEMBLY REQUIREMENTS section specifies all required sections |
| C-05 | Source attribution | PASS | REQ-ATTR-01: "SHALL label every material claim with its source stage; 70%+ of material claims MUST carry stage labels" |
| C-06 | Consensus/conflict separation | PASS | Stage 5 REQ-EXIT-S5a: "Consensus and conflict explicitly separated"; output assembly requires this section |
| C-07 | Calibrated confidence | PASS | REQ-CAL-01: "SHALL NOT assign uniform confidence ratings; if uniform ratings are produced, the executor MUST regenerate" |
| C-08 | Gaps surfaced | PASS | Stage 5 requires gaps section; REQ-EXIT-S5c: "Gaps section present" |
| C-09 | Decision readiness signal | PASS | REQ-EXIT-S5d: "Decision readiness stated in exactly one sentence" |
| C-10 | Hypotheses post-evidence | PASS | REQ-SEQ-01 enforces this; named principle encoded |
| C-11 | Anti-uniformity guard | PASS | REQ-CAL-01: "executor SHALL NOT assign uniform confidence ratings to all findings" — explicit prohibition |
| C-12 | One-sentence decision readiness | PASS | REQ-EXIT-S5d: "exactly one sentence"; also "executor SHALL NOT produce a multi-paragraph decision readiness section" |
| C-13 | Named rules at point of use | PASS | REQ-ATTR-01, REQ-CAL-01, REQ-FAL-01, REQ-SEQ-01, REQ-PROV-01 declared in preamble; invoked by identifier at each stage |
| C-14 | Reordering rationale | PASS | REQ-SEQ-01: "Named principle: 'A hypothesis anchored before evidence gathering is a bias, not a hypothesis.' This principle SHALL be encoded as a named rule (REQ-SEQ-01)" |
| C-15 | Sequencing as named rule | PASS | REQ-SEQ-01 is a numbered named requirement, explicitly declared as referenceable by identifier |
| C-16 | Zero-gap invocation | PASS | 25-cell coverage map; all cells addressed at every stage |
| C-17 | Coverage map prospective | PASS | Coverage Map "sealed before Stage 1"; "The executor SHALL NOT modify it" |
| C-18 | All rules peer tier | PASS | "all five rules are peers; no rule is primary"; REQ-level peer declaration |
| C-19 | Coverage map immutability | PASS | "sealed before Stage 1; The executor SHALL NOT modify it" |
| C-20 | Rule scope inline | PASS | Every requirement has `[applies at: S1, S2, ...]` inline annotation within the requirement body |
| C-21 | Interrogative invocation at critical rules | PASS | All invocations use binary questions: "All S1 findings SHALL carry `[web]` label. All labeled? [ Yes / No ]" |
| C-22 | Universal binary invocation | PASS | Every applicable invocation uses `[ Yes / No ]`; non-applicable use `[ N/A ]` |
| C-23 | Stage-indexed trail | PASS | `[S1 of 5]`, `[S2 of 5]`, ... suffixes on all invocations |
| C-24 | Per-stage entry/exit conditions | PASS | Explicit entry gates and exit gates with SHALL conditions at every stage |
| C-25 | Gate record as output artifact | PASS | Output assembly step 3: "Filled gate record (required)"; pre-templated in preamble |
| C-26 | Audit table derivable count | PASS | "25 rows (one per coverage map cell)"; "derived from 5 req × 5 stages" |
| C-27 | Gate record pre-templated blank | PASS | Gate Record Template in preamble with `[ ]` blank cells |
| C-28 | Sequencing as machine-verifiable column | **FAIL** | No evidence table with Stage column; REQ-SEQ-01 enforced via invocation tags and narrative order only — not sort-verifiable |
| C-29 | Extensible without static updates | PASS | "Adding a new peer requirement SHALL propagate automatically through the coverage map. The executor SHALL NOT require manual updates to static integers." |
| C-30 | Named handoff actors | PASS | "HANDOFF: Role passes to Stage N — Role Name" at each boundary |
| C-31 | Negative invocation at non-applicable stages | PASS | Explicit N/A invocations: "REQ-CAL-01 [S1 of 5]: N/A — REQ-CAL-01 SHALL NOT be invoked at evidence collection. [ N/A ]" |
| C-32 | Role access scope per stage | PASS | Role Roster with "Access Scope" column and explicit "SHALL NOT access" statements |
| C-33 | Derivable checksum | PASS | "SHALL count: 15. N/A count: 10. Total invocation artifacts: 25 (derived from 5 req × 5 stages)." |
| C-34 | Artifact provenance tags | PASS | REQ-PROV-01: "SHALL include a provenance tag `[source: Stage N — Artifact Name]`" at S3/S4/S5; exit gates verify |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 26/27

```
composite = (4/4 × 60) + (3/3 × 30) + (26/27 × 10)
          = 60 + 30 + 9.63
          = 99.63
```

**Score: 99.63 / 100**

---

### V-05 — Combination (Table-First + Dual-Phase + Provenance Activation at Handoff)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Multi-stage campaign | PASS | 5 named stages; explicit "Role passes to" handoff declarations |
| C-02 | Evidence before hypothesis | PASS | SEQUENCING RULE dual-phase; Stage column in Evidence Table makes ordering sort-verifiable |
| C-03 | Hypotheses with falsification conditions | PASS | Hypotheses Table Falsification-Condition column; non-blank required; verified pre/post at S3/S5 |
| C-04 | Self-contained output | PASS | OUTPUT ASSEMBLY produces coherent brief with all tables and synthesis narrative |
| C-05 | Source attribution | PASS | Stage column in Evidence Table; 70%+ requirement; unlabeled rows = attribution violations |
| C-06 | Consensus/conflict separation | PASS | Synthesis rows distinguished as Consensus vs Conflict row types in Evidence Table |
| C-07 | Calibrated confidence | PASS | Confidence column constraint: "min(Confidence) MUST NOT equal max(Confidence) across rows. Uniform Confidence values fail this rule." |
| C-08 | Gaps surfaced | PASS | Gap row type in Evidence Table at Stage 5 |
| C-09 | Decision readiness signal | PASS | Decision-Readiness row type: "exactly one row; value is one sentence naming posture and specific gap if not ready" |
| C-10 | Hypotheses post-evidence | PASS | SEQUENCING RULE dual-phase + Stage column; both interrogative and sort-verifiable |
| C-11 | Anti-uniformity guard | PASS | Explicit: "min(Confidence) MUST NOT equal max(Confidence) across rows" |
| C-12 | One-sentence decision readiness | PASS | "exactly one row; value is one sentence" — Decision-Readiness row type enforces compression |
| C-13 | Named rules at point of use | PASS | All five rules named in preamble; invoked by name at every applicable stage with PRE/POST labels |
| C-14 | Reordering rationale | PASS | Named principle in SEQUENCING RULE: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis" |
| C-15 | Sequencing as named rule | PASS | SEQUENCING RULE is a named peer-tier rule with identifier |
| C-16 | Zero-gap invocation | PASS | 40-artifact checksum covers all 25 cells (15 dual-phase × 2 + 10 negative × 1) |
| C-17 | Coverage map prospective | PASS | Dual-Phase Coverage Map in preamble: "Immutable — cannot be modified after execution starts" |
| C-18 | All rules peer tier | PASS | "all five rules are peers; no rule is primary"; explicit peer declaration |
| C-19 | Coverage map immutability | PASS | "Immutable — cannot be modified after execution starts" |
| C-20 | Rule scope inline | PASS | Every rule has `[invoked at: ...]` and `[dual-phase at: ...]` inline annotations within rule body |
| C-21 | Interrogative invocation at critical rules | PASS | All applicable invocations are dual-phase interrogatives: "Will X hold? [Yes/No]" + "Does X hold? [Yes/No]" — exceeds C-21 minimum |
| C-22 | Universal binary invocation | PASS | All applicable invocations use `[ Yes / No ]` (both PRE and POST); non-applicable use `[ No ]` |
| C-23 | Stage-indexed trail | PASS | `[Stage 1 of 5]` / `[S1, PRE]` / `[S1, POST]` suffixes on all invocations — phase-labeled and stage-indexed |
| C-24 | Per-stage entry/exit conditions | PASS | Entry gate and exit gate with Pass/Fail cells at every stage |
| C-25 | Gate record as output artifact | PASS | Output assembly step 3: "Filled gate record"; pre-templated blank in preamble; includes PROVENANCE activation check in S3/S4/S5 entry conditions |
| C-26 | Audit table derivable count | PASS | "40 rows (one per dual-phase answer + negative)"; checksum: "derived from (positive count × 2) + (negative count × 1)" — fully derivable |
| C-27 | Gate record pre-templated blank | PASS | Gate Record Template in preamble with blank cells including PROVENANCE activation status |
| C-28 | Sequencing as machine-verifiable column | **PASS** | Evidence Table has Stage column; "sort by Stage column; no S3 row should have Source-Stage outside {S1, S2}"; Hypothesis rows (Stage=S3) constrained to Source-Stage in {S1,S2} |
| C-29 | Extensible without static updates | PASS | "Adding a peer rule extends the coverage map automatically. No static integer requires manual update." |
| C-30 | Named handoff actors | PASS | "Role passes to: Stage N — Role Name" + artifact enumeration + PROVENANCE activation at S2-S3, S3-S4, S4-S5 handoffs |
| C-31 | Negative invocation at non-applicable stages | PASS | Every non-applicable cell carries explicit negative: "CALIBRATION [S1]: Not applicable at evidence collection. [ No ]" |
| C-32 | Role access scope per stage | PASS | Role Roster with "Authorized Source-Stage Values" column; note that provenance activation is at handoff, not here |
| C-33 | Derivable checksum | PASS | "Checksum: 40 invocation artifacts = 30 dual-phase answers + 10 negative checks, derived from (positive count × 2) + (negative count × 1). Derivable from map; no static integer stored independently." |
| C-34 | Artifact provenance tags | PASS | Source-Stage and Source-Artifact columns in both Evidence Table and Hypotheses Table; PROVENANCE activated at each handoff boundary with explicit structural enforcement |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 27/27

```
composite = (4/4 × 60) + (3/3 × 30) + (27/27 × 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100**

---

## Final Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Score | C-28 |
|------|-----------|-----------|-------------|--------------|-------|------|
| 1 | **V-05** — Combination | 4/4 | 3/3 | 27/27 | **100** | PASS |
| 1 | **V-02** — Output Format | 4/4 | 3/3 | 27/27 | **100** | PASS |
| 3 | **V-01** — Role Sequence | 4/4 | 3/3 | 26/27 | **99.63** | FAIL |
| 3 | **V-03** — Lifecycle Emphasis | 4/4 | 3/3 | 26/27 | **99.63** | FAIL |
| 3 | **V-04** — Phrasing Register | 4/4 | 3/3 | 26/27 | **99.63** | FAIL |

---

## Single Discriminator: C-28

C-28 (sequencing compliance encoded as machine-verifiable column value) is the only criterion that separates variates in R13. V-01, V-03, and V-04 each enforce SEQUENCING through invocation tags or binary interrogatives — but none provides a Stage column in a structured table that makes a hypothesis-before-evidence violation detectable by sort. V-02 and V-05 both implement the Master Evidence Table with a Stage column and explicitly state that hypothesis rows (Stage=S3) may only reference Source-Stage in {S1, S2}, making a violation detectable without prose interpretation.

C-28 is entirely a structural format decision: it cannot be satisfied by adding invocation phrasing to a narrative format.

---

## Within the 100 Cluster: Structural Guarantee Differences

| Variation | C-28 mechanism | Signal 1 (dual-phase) | Signal 2 (handoff provenance) | Structural risk |
|-----------|---------------|----------------------|-------------------------------|-----------------|
| V-05 | Stage column + sort constraint | PRESENT (40-artifact checksum) | PRESENT (explicit activation at handoff) | Lowest |
| V-02 | Stage column + sort constraint | Absent (single-phase) | Absent (charter declaration) | Low |

V-05 scores identically to V-02 in the v13 rubric but implements two additional structural mechanisms that are candidates for C-36 and C-37 in v14. Both close compliance gaps not currently measured: dual-phase makes intent-execution gaps visible in the invocation trail; handoff-boundary provenance activation makes the provenance rule live at the transfer event rather than in a static charter. V-05 is the predicted golden candidate.

---

## Excellence Signals (from V-05)

**Signal 1 — Dual-phase invocation splits every compliance event into a commitment and a verification:**
The PRE-EXECUTION check records intent before execution begins; the POST-EXECUTION check records whether intent was realized. A discrepancy (PRE=Yes, POST=No) is an intent-execution gap that requires no content interpretation — it is two rows in the audit table that disagree. This also changes the artifact count from 25 to 40, making any missing PRE/POST pair detectable as a count mismatch before the audit table is scanned.

**Signal 2 — Handoff-boundary provenance activation converts a charter obligation into a live enforcement event:**
Moving the PROVENANCE RULE activation from the role roster (a static declaration consulted once) to the handoff block (an active transfer event that must be completed before the next stage opens) means a scope-restricted role that begins execution without a completed handoff block structurally lacks an activated provenance rule. The gap is visible at the boundary before the first claim is produced, not discovered at audit after claims have been made.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-phase invocation splits each applicable compliance event into a PRE-EXECUTION commitment and a POST-EXECUTION verification — a PRE=Yes followed by POST=No is an intent-execution gap visible as two-row disagreement in the audit trail, detectable without content interpretation; dual-phase also raises the checksum from 25 to 40 artifacts, making any missing PRE/POST pair a count mismatch before scanning", "Handoff-boundary provenance activation converts a static role-charter declaration into a live enforcement event — when PROVENANCE is not activated in the role roster but is activated exclusively at the handoff block, a scope-restricted role that begins execution without a completed handoff block structurally lacks an activated provenance rule, making the gap visible at the boundary before the first claim is produced rather than discovered at audit after claims exist"]}
```
