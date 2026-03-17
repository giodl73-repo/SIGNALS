## Round 8 Scorecard — topic-new (v7 rubric)

> **Scoring note**: Only V-01 contains a complete prompt in this scoring request. V-02 (Output format), V-03 (Phrasing register), V-04 (Lifecycle + Inertia framing), and V-05 (Output format + Role sequence + Inertia framing) are named as axes but no prompt bodies were provided. Scoring covers V-01 in full; V-02–V-05 entries are marked **NOT SCORED** with axis notation.

---

## V-01 — Lifecycle Emphasis

**Axis**: Three-column pipeline overview table (Purpose + Produces + Exit Gate) declaring all exit gate conditions before any phase body. Hypothesis: maximum architectural clarity for C-24; pre-declared artifact shapes may also improve C-02 and C-10 compliance.

---

### Essential Criteria (5 of 5 = 60/60)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | **PASS** | Phase 2 explicitly appends a row to `simulations/TOPICS.md` with topic name, `status=active`, and strategy path. Phase 2 exit gate enforces all three fields. |
| C-02 | Strategy file at correct path | **PASS** | Phases 3, 5, 7, and 8 all target `simulations/{topic}/strategy.md`. No flat path or inline variant. |
| C-03 | All five signal fields present | **PASS** | Phase 7 signal plan table columns: Namespace, Skill, Item Name, Owner Role, Stakeholder Ref, Priority. All five required fields present (Stakeholder Ref is additive). |
| C-04 | Priority values are valid | **PASS** | F-05: "Must be exactly: `essential` / `recommended` / `optional` — no substitutions." Consequence stated. Enforced by Phase 6 pre-write gate and Phase 7 exit gate, both citing F-05 by ID. |
| C-05 | At least one essential signal | **PASS** | COV-01 threshold ">=1 row where priority = essential" enforced by Phase 6 (entry gate to Phase 7) and Phase 7 exit gate. |

**Essential subtotal: 5/5 → 60 pts**

---

### Recommended Criteria (3 of 3 = 30/30)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Signal set spans multiple namespaces | **PASS** | COV-02 threshold ">= 2 distinct namespaces" enforced in Phase 6 and Phase 7 exit gates citing COV-02 by ID. |
| C-07 | Strategy includes a narrative rationale | **PASS** | Phase 3 writes a dedicated `## Rationale` section with a ">= 2 sentences" exit gate requirement that names the specific design decision. |
| C-08 | Owner roles are differentiated | **PASS** | COV-03 threshold ">= 2 distinct S-N refs" structurally enforced. Role differentiation derives from the Phase 1 fill-in table, not a late checklist. |

**Recommended subtotal: 3/3 → 30 pts**

---

### Aspirational Criteria (17 of 17 = 10/10)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Strategy defines a commit gate | **PASS** | Phase 8 is fully dedicated to writing the Commit Gate section with explicit "gate condition stated explicitly" exit requirement. |
| C-10 | Artifact naming convention present | **PASS** | Phase 5 is a dedicated phase writing `## Artifact Naming Convention` with pattern and at least one parameterized example. Phase 5 exit gate enforces both. |
| C-11 | Checkbox-gate before phase transition | **PASS** | Every phase carries a named exit gate with checkbox items. No phase advances silently. |
| C-12 | Invalid vocabulary framed as operational consequence | **PASS** | F-05: "Strategy unparseable as commit gate" (Immediate) + "Team commits without a defined stopping condition" (Downstream). Consequence framing, not style note. |
| C-13 | Each aspirational criterion has a dedicated section | **PASS** | Phase 5 is the naming convention section. Phase 8 is the commit gate section. Both are independent phases with headers, not inline notes. |
| C-14 | Consequence framing applied pervasively | **PASS** | Every F-0N and COV-0N row carries both Immediate Failure and Downstream Effect columns. No constraint without a stated failure mode. |
| C-15 | Prompt opens with stakeholder-risk enumeration | **PASS** | Phase 1 header: "WHO BEARS THE RISK if this topic's strategy is wrong?" Executes before any artifact writing. |
| C-16 | Every criterion enforced by structural mechanism | **PASS** | Schema tables, fill-in templates, checkbox gates, and column constraints enforce all criteria. No criterion is prose-only. |
| C-17 | Stakeholder-risk section is active fill-in output | **PASS** | Phase 1 is a fill-in table (S-01…S-N rows) required as first output. F-04 traces every Owner Role to an S-N row from that table — role differentiation is derived, not asserted. |
| C-18 | Constraints partitioned into named schemas with consequence columns | **PASS** | FIELD SCHEMA (F-01–F-05) and COVERAGE SCHEMA (COV-01–COV-03) are separate named tables. Both carry Immediate Failure and Downstream Effect columns. Gates cite by row ID. |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | **PASS** | F-04 field rule: "Must reference a specific S-N row from the Phase 1 Stakeholders table." Signal plan table includes a dedicated "Stakeholder Ref" column, making traceability auditable at row level. |
| C-20 | Consequence columns are temporally layered | **PASS** | FIELD SCHEMA and COVERAGE SCHEMA both split consequences into "Immediate Failure" and "Downstream Effect" — two temporal tiers present in both schemas. |
| C-21 | Per-phase exit gates at every phase boundary | **PASS** | Phases 1 through 8 each have their own named exit gate block. Phase 7 exit gate explicitly states "Do not advance to Phase 8 until all exit gate items are checked." |
| C-22 | Stakeholder fill-in minimum row count gate | **PASS** | Phase 1 exit gate: ">= 3 rows filled; all four columns populated." Quantified threshold present; degenerate one-row table cannot pass. |
| **C-23** | Schema constraints carry row-level identifiers for gate citation | **PASS** | F-01–F-05 and COV-01–COV-03 are stable row IDs. Phase 6 exit gate cites each by ID: "F-01: All planned namespaces…", "F-02: All planned skills…", etc. Phase 7 exit gate repeats this citation. A gate citing "F-01 through F-05" cannot drift from the schema definition. |
| **C-24** | Pipeline declares all exit gates in a summary table before phase content | **PASS** | PIPELINE OVERVIEW table is placed before Phase 1 with the instruction "Read this entire table before executing Phase 1. All exit gate conditions are declared here." The Exit Gate column carries specific gate conditions for all 8 phases architecturally. Phases then carry inline gates as a second layer. Dual-layer structure: overview declaration + inline gate per phase. |
| **C-25** | Commit Gate occupies a dedicated phase separate from signal plan production | **PASS** | Phase 7 = signal plan rows. Phase 8 = Commit Gate (declared as "a dedicated phase separate from signal plan production" in the phase header). Phase 7 exit gate verifies all signal rows before the model advances to Phase 8. The V-02 failure mode (entry-only gate leaving post-production boundary ungated) is architecturally impossible: Phase 7 has its own exit gate, Phase 8 has its own entry/exit. PIPELINE OVERVIEW makes this separation visible before execution begins. |

**Aspirational subtotal: 17/17 → 10 pts**

---

### V-01 Composite Score

```
composite = (5/5 × 60) + (3/3 × 30) + (17/17 × 10)
          = 60 + 30 + 10
          = 100 / 100
```

---

## V-02 — Output Format

**Axis**: Output format variation.
**Score**: NOT SCORED — prompt body not provided.

---

## V-03 — Phrasing Register

**Axis**: Phrasing register variation.
**Score**: NOT SCORED — prompt body not provided.

---

## V-04 — Lifecycle + Inertia Framing

**Axes**: Lifecycle emphasis + Inertia framing combination.
**Score**: NOT SCORED — prompt body not provided.

---

## V-05 — Output Format + Role Sequence + Inertia Framing

**Axes**: Output format + Role sequence + Inertia framing (three-axis combination).
**Score**: NOT SCORED — prompt body not provided.

---

## Rankings

| Rank | Variation | Composite | Essential | Rec | Asp |
|------|-----------|-----------|-----------|-----|-----|
| 1 | V-01 | **100** | 5/5 | 3/3 | 17/17 |
| — | V-02 | — | — | — | — |
| — | V-03 | — | — | — | — |
| — | V-04 | — | — | — | — |
| — | V-05 | — | — | — | — |

V-01 is the first variation in the topic-new series to achieve a perfect score under any rubric version.

---

## Excellence Signals — V-01

Three new patterns explain why V-01 satisfies all R7 criteria where prior rounds could not:

**E-1: Three-column pipeline overview table as architectural declaration layer (→ C-24)**
The PIPELINE OVERVIEW table carries Purpose, Produces, and Exit Gate for all eight phases before the model reads any phase body. The instruction "Read this entire table before executing Phase 1. All exit gate conditions are declared here" makes exit gate review possible without entering phase content. The "Produces" column additionally pre-declares the artifact shape of each phase, which locks C-02 and C-10 to the overview rather than relying on per-phase instruction. Prior rounds satisfied C-21 via inline-only gates; V-01's dual-layer structure (overview + inline) makes gate omission structurally impossible at the architectural level before execution begins.

**E-2: Schema row IDs (F-N, COV-N) as mechanical coupling between constraint definitions and gate citations (→ C-23)**
Naming each schema row F-01–F-05 and COV-01–COV-03 transforms gate checkpoints from paraphrased rules into citations by canonical ID. The Phase 6 exit gate reads "F-01: All planned namespaces are in the allowed set" — not a restatement of the rule, but a pointer to it. A model cannot satisfy Phase 6 for F-01 while holding a different definition of F-01 than the one in FIELD SCHEMA. Prior rounds satisfied C-18 with named schemas but did not add row IDs, leaving the possibility of semantic drift between schema definition and gate checkpoint.

**E-3: Commit Gate as a named dedicated phase following signal plan production (→ C-25)**
Phase 7 (Signal Plan) and Phase 8 (Commit Gate) are separated in both the PIPELINE OVERVIEW and the phase body. Phase 7 carries an exit gate that verifies all signal rows; only then does the model advance to Phase 8. This means Phase 7 has an entry gate (Phase 6's exit) and an exit gate (Phase 7's own), eliminating the V-02 failure mode where signal production and commit gate naming shared one phase, leaving the post-production boundary ungated. The Phase 8 header text "This is a dedicated phase separate from signal plan production" names the structural invariant explicitly.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Three-column pipeline overview table (Purpose + Produces + Exit Gate) before any phase body creates an architectural declaration layer satisfying C-24 with dual-layer enforcement", "Schema row IDs (F-N, COV-N) mechanically couple constraint definitions to gate citations, preventing semantic drift between schema and gate checkpoint", "Commit Gate isolated as Phase 8 separate from Phase 7 signal plan production gives Phase 7 both an entry gate and an exit gate, structurally eliminating the post-production ungated boundary failure mode"]}
```
