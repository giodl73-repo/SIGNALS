Good — I have the format reference. Now I'll score all five variations.

---

## Round 6 Scorecard — topic-new

### Per-Variation Criterion Evaluation

---

#### V-01 — Minimal C-13 Fix

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry | PASS | Phase 2 provides template row |
| C-02 | Strategy at correct path | PASS | `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields | PASS | FIELD SCHEMA (§3.2) covers namespace, skill, item name, owner role, priority |
| C-04 | Valid priority vocabulary | PASS | `essential / recommended / optional only` |
| C-05 | At least one essential | PASS | Pre-write gate checkbox + COVERAGE SCHEMA threshold |
| C-06 | Multi-namespace | PASS | COVERAGE SCHEMA requires ≥ 2 namespaces |
| C-07 | Narrative rationale | PASS | §3.1 requires 2+ sentences |
| C-08 | Differentiated owner roles | PASS | COVERAGE SCHEMA "Distinct Stakeholder Refs ≥ 2 S-N values" enforces structurally |
| C-09 | Commit gate defined | PASS | §3.6 "Design commit is blocked until every listed signal exists. Name each one." |
| C-10 | Artifact naming convention | PASS | §3.3 "Artifact Naming Convention" is dedicated section with pattern + example |
| C-11 | Checkbox-gate before phase transition | PASS | §3.5 pre-write gate with 6 checkboxes |
| C-12 | Invalid vocabulary as operational consequence | PASS | Priority row: "Strategy unparseable as a commit gate" / "Team proceeds to commit with no defined stopping condition" |
| C-13 | Each aspirational criterion has dedicated section | PASS | §3.3 = C-10, §3.6 = C-09 — both are named section headings |
| C-14 | Consequence framing pervasive | PASS | Every FIELD SCHEMA and COVERAGE SCHEMA row carries Immediate Failure + Downstream Effect |
| C-15 | Stakeholder-risk opener | PASS | Phase 1 stakeholder fill-in table (immediate risk + downstream risk columns) as first output |
| C-16 | Every criterion enforced structurally | PASS | Section headers, table columns, checkbox gate — no criterion relies on prose alone |
| C-17 | Stakeholder-risk as active fill-in | PASS | Phase 1 produces fill-in table; S-N refs in FIELD SCHEMA trace back to it |
| C-18 | Constraints in named schemas with consequence columns | PASS | §3.2 FIELD SCHEMA + §3.4 COVERAGE SCHEMA — separate named, each with consequence columns |
| C-19 | FIELD SCHEMA Stakeholder traceability column | PASS | Dedicated "Stakeholder Ref" column in §3.2 FIELD SCHEMA; "Required — cite S-N" on owner role row |
| C-20 | Temporally layered consequence columns | PASS | "Immediate Failure" and "Downstream Effect" in both schemas |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 12/12
**Score**: 60 + 30 + 10 = **100** ✓ Golden

---

#### V-02 — Conversational Imperative Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry | PASS | Step 2 provides row template |
| C-02 | Strategy at correct path | PASS | `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields | PASS | Step 4 table covers all fields (6 rows including stakeholder ref as field row) |
| C-04 | Valid priority vocabulary | PASS | "essential or recommended or optional — nothing else" + explicit callout |
| C-05 | At least one essential | PASS | Step 6 checkbox "At least 1 signal will be essential" |
| C-06 | Multi-namespace | PASS | Step 6 checkbox "At least 2 different namespaces" |
| C-07 | Narrative rationale | PASS | Step 3 "minimum 2 sentences" |
| C-08 | Differentiated owner roles | PASS | Step 6 checkbox "At least 2 different S-N refs"; Step 4 Stakeholder Ref column |
| C-09 | Commit gate defined | PASS | Step 7 "Name the commit gate" — named step with explicit instruction |
| C-10 | Artifact naming convention | PASS | Step 5 "Know the naming pattern" — dedicated named step with pattern + example |
| C-11 | Checkbox-gate before phase transition | PASS | Step 6 with 7 checkboxes |
| C-12 | Invalid vocabulary as operational consequence | PASS | Step 4 priority row + explicit "On priority" callout: "strategy inert as a commit gate" |
| C-13 | Each aspirational criterion has dedicated section | PASS | Step 5 = C-10, Step 7 = C-09 — both are named sections |
| C-14 | Consequence framing pervasive | PASS | Step 4 table: every field row has "If you get it wrong immediately" + "What that causes downstream" |
| C-15 | Stakeholder-risk opener | PASS | Step 1 stakeholder fill-in table as explicit first output |
| C-16 | Every criterion enforced structurally | PASS | Named steps, table columns, checkboxes carry all criteria |
| C-17 | Stakeholder-risk as active fill-in | PASS | Step 1 is fill-in with "Do not move to Step 2 until table has ≥ 3 rows" |
| C-18 | Constraints in named schemas with consequence columns | **FAIL** | Step 4 = FIELD SCHEMA equivalent with consequence columns, but **no separate named COVERAGE SCHEMA table** — coverage constraints appear only as inline checkboxes in Step 6 without consequence columns |
| C-19 | FIELD SCHEMA Stakeholder traceability column | PASS | "Stakeholder Ref" column in Step 4 table; "Required — cite S-N" on owner role row |
| C-20 | Temporally layered consequence columns | PASS | Two temporal tiers in Step 4 FIELD SCHEMA |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 11/12
**Score**: 60 + 30 + (11/12 × 10) = 60 + 30 + 9.17 = **99.17** — Golden threshold met

---

#### V-03 — Lifecycle Emphasis (Six-Phase with Entry/Exit Gates)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry | PASS | Phase 2 provides row template |
| C-02 | Strategy at correct path | PASS | `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields | PASS | Phase 4 FIELD SCHEMA |
| C-04 | Valid priority vocabulary | PASS | "essential / recommended / optional only" |
| C-05 | At least one essential | PASS | Phase 6 pre-write gate + COVERAGE SCHEMA |
| C-06 | Multi-namespace | PASS | COVERAGE SCHEMA threshold ≥ 2 |
| C-07 | Narrative rationale | PASS | Phase 3 exit gate requires "≥ 2 sentences; decision context named" |
| C-08 | Differentiated owner roles | PASS | COVERAGE SCHEMA "Distinct Stakeholder Refs ≥ 2 distinct S-N values" |
| C-09 | Commit gate defined | PASS | Phase 6 "Commit Gate section: List item names of all essential signals" |
| C-10 | Artifact naming convention | PASS | Phase 5 "Artifact Naming Convention" is its own dedicated phase with exit gate |
| C-11 | Checkbox-gate before phase transition | PASS | Per-phase exit gates at every boundary + Phase 6 pre-write gate |
| C-12 | Invalid vocabulary as operational consequence | PASS | Phase 4 FIELD SCHEMA priority row: "Strategy unparseable as commit gate" / "no stopping condition" |
| C-13 | Each aspirational criterion has dedicated section | PASS | Phase 5 = C-10, Phase 6 Commit Gate section = C-09 |
| C-14 | Consequence framing pervasive | PASS | FIELD SCHEMA and COVERAGE SCHEMA both carry Immediate Failure + Downstream Effect for all rows |
| C-15 | Stakeholder-risk opener | PASS | Phase 1 "Stakeholder Enumeration" as first phase with fill-in table |
| C-16 | Every criterion enforced structurally | PASS | Phase entry/exit gates, table columns, section headers |
| C-17 | Stakeholder-risk as active fill-in | PASS | Phase 1 produces fill-in table; Phase 1 exit gate verifies ≥ 3 rows before advancing; owner roles must trace to table |
| C-18 | Constraints in named schemas with consequence columns | PASS | Phase 4 contains two explicitly named sub-sections: FIELD SCHEMA + COVERAGE SCHEMA, both with consequence columns |
| C-19 | FIELD SCHEMA Stakeholder traceability column | PASS | "Stakeholder Ref" column in Phase 4 FIELD SCHEMA; "Required — cite S-N" on owner role row |
| C-20 | Temporally layered consequence columns | PASS | "Immediate Failure" + "Downstream Effect" in both schemas |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 12/12
**Score**: 60 + 30 + 10 = **100** ✓ Golden

---

#### V-04 — C-13 Fix + Schema Compression (Minimal Surface Area)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry | PASS | "Output 1 — TOPICS.md" section |
| C-02 | Strategy at correct path | PASS | `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields | PASS | FIELD SCHEMA table |
| C-04 | Valid priority vocabulary | PASS | "essential / recommended / optional" |
| C-05 | At least one essential | PASS | GATE CHECKLIST checkbox + COVERAGE SCHEMA threshold |
| C-06 | Multi-namespace | PASS | COVERAGE SCHEMA "Namespaces ≥ 2" |
| C-07 | Narrative rationale | PASS | **RATIONALE** section "required, 2+ sentences" |
| C-08 | Differentiated owner roles | PASS | COVERAGE SCHEMA "Distinct S-N refs ≥ 2" enforces structurally |
| C-09 | Commit gate defined | PASS | **COMMIT GATE** bold heading — "Name the essential signals by item name" |
| C-10 | Artifact naming convention | PASS | **ARTIFACT NAMING CONVENTION** bold heading — pattern + example in compressed form |
| C-11 | Checkbox-gate before phase transition | PASS | **GATE CHECKLIST** with 7 checkboxes before SIGNAL PLAN |
| C-12 | Invalid vocabulary as operational consequence | PASS | Priority row: "Strategy unparseable" / "No commit gate; investigation never closes" |
| C-13 | Each aspirational criterion has dedicated section | PASS | `**ARTIFACT NAMING CONVENTION**` = C-10, `**COMMIT GATE**` = C-09 — both bold headings qualify as named sections |
| C-14 | Consequence framing pervasive | PASS | Every FIELD SCHEMA and COVERAGE SCHEMA row has Immediate Failure + Downstream Effect |
| C-15 | Stakeholder-risk opener | PASS | **STAKEHOLDERS** is first section "(fill as first step)" |
| C-16 | Every criterion enforced structurally | PASS | Bold section headers, table columns, checkbox gate |
| C-17 | Stakeholder-risk as active fill-in | PASS | Fill-in S-N rows; note that "rows with no citation are unauditable" — enforced as first step |
| C-18 | Constraints in named schemas with consequence columns | PASS | **FIELD SCHEMA** + **COVERAGE SCHEMA** are separate bold-heading sections with consequence columns |
| C-19 | FIELD SCHEMA Stakeholder traceability column | PASS | "Stakeholder Ref" column in FIELD SCHEMA; "Required: cite S-N" on owner role row |
| C-20 | Temporally layered consequence columns | PASS | "Immediate Failure" + "Downstream Effect" in both schemas |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 12/12
**Score**: 60 + 30 + 10 = **100** ✓ Golden

Key finding: **C-13 is satisfiable by a bold heading alone.** `**ARTIFACT NAMING CONVENTION**` + one pattern line + one example is sufficient. Section body length does not affect criterion compliance — the heading is the structural home.

---

#### V-05 — C-13 Fix + Inertia Framing + Lifecycle

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | TOPICS.md entry | PASS | Phase 2 provides row template |
| C-02 | Strategy at correct path | PASS | `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields | PASS | Phase 4 FIELD SCHEMA |
| C-04 | Valid priority vocabulary | PASS | "essential / recommended / optional only" |
| C-05 | At least one essential | PASS | Phase 7 pre-write gate + Phase 6 COVERAGE SCHEMA |
| C-06 | Multi-namespace | PASS | Phase 6 COVERAGE SCHEMA ≥ 2 namespaces |
| C-07 | Narrative rationale | PASS | Phase 3 "minimum 2 sentences" |
| C-08 | Differentiated owner roles | PASS | Phase 6 COVERAGE SCHEMA "≥ 2 distinct S-N values" |
| C-09 | Commit gate defined | PASS | Phase 8 "Commit Gate" — dedicated named phase |
| C-10 | Artifact naming convention | PASS | Phase 5 "Artifact Naming Convention" — dedicated named phase with pattern + example |
| C-11 | Checkbox-gate before phase transition | PASS | Phase 7 pre-write gate with 7 checkboxes |
| C-12 | Invalid vocabulary as operational consequence | PASS | Phase 4 FIELD SCHEMA priority row: "Strategy unparseable as a commit gate" / "Team commits without a stopping condition" |
| C-13 | Each aspirational criterion has dedicated section | PASS | Phase 5 heading = C-10, Phase 8 heading = C-09 |
| C-14 | Consequence framing pervasive | PASS | FIELD SCHEMA + COVERAGE SCHEMA consequence columns; PLUS inertia opener in every phase names the ambient failure state |
| C-15 | Stakeholder-risk opener | PASS | Phase 1 "Who Loses When We Decide Without Evidence" with fill-in table |
| C-16 | Every criterion enforced structurally | PASS | Phase headings, table columns, checklist gate |
| C-17 | Stakeholder-risk as active fill-in | PASS | Phase 1 fill-in table with S-N keys; uncited rows are explicitly "unauditable" |
| C-18 | Constraints in named schemas with consequence columns | PASS | Phase 4 = FIELD SCHEMA (named), Phase 6 = COVERAGE SCHEMA (named), each with consequence columns in separate phases |
| C-19 | FIELD SCHEMA Stakeholder traceability column | PASS | "Stakeholder Ref" column in Phase 4 FIELD SCHEMA; "Required — cite S-N" on owner role row |
| C-20 | Temporally layered consequence columns | PASS | "Immediate Failure" + "Downstream Effect" in Phase 4 and Phase 6 |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 12/12
**Score**: 60 + 30 + 10 = **100** ✓ Golden

---

### Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Minimal C-13 fix | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-03 Lifecycle emphasis | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-04 Schema compression | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-05 Inertia + lifecycle | 5/5 | 3/3 | 12/12 | **100** | YES |
| 5 | V-02 Conversational register | 5/5 | 3/3 | 11/12 | **99.17** | YES |

---

### The Single Discriminator: C-18

V-02 is the only variation that fails a criterion. The gap is structural: V-02's conversational step-by-step register collapses the COVERAGE SCHEMA into the pre-write checkbox list (Step 6). Coverage constraints are present but without a separate named table carrying consequence columns. C-18 requires two named schemas — V-02 delivers one.

The constraint is not about prose register. V-02 could have reached 100 if Step 6 had been preceded by a named `**COVERAGE SCHEMA**` table equivalent to §3.4 in V-01. The conversational phrasing of the checkboxes is not the problem — the missing schema table is.

**C-18 is a structural requirement that cannot be satisfied by a checklist alone.** The named table with consequence columns must exist as its own section, separate from the gate that cites it.

---

### Within the 100 cluster: structural differences

| Variation | C-13 mechanism | C-18 mechanism | Structural risk |
|-----------|---------------|----------------|-----------------|
| V-04 | Bold heading + 1 pattern line + 1 example | Bold headings for both schemas | Lowest — minimal surface, nothing to misread |
| V-01 | Named section (§3.3) with full prose body | Numbered sections (§3.2, §3.4) | Low |
| V-03 | Dedicated phase (Phase 5) with entry/exit gate | Sub-sections within Phase 4 | Low — exit gate adds extra enforcement |
| V-05 | Dedicated phase (Phase 5) with inertia opener | Separate phases (4 and 6) with inertia framing | Low — inertia framing adds motivational weight |

V-04's compression test resolves a design question: **the minimum viable form for a named section is a heading + one content line.** No prose body required. This matters for template density.

---

### Excellence Signals

**Pattern from R6 not yet captured in C-01–C-20:**

**Inertia opener** (V-05): Each phase begins by naming the default failure state the skill interrupts — "Without this step, teams do X and Y breaks." This is distinct from consequence columns (which state what breaks *if you violate a rule*). The inertia opener states what is *already broken before the skill runs*, making the value of each section viscerally clear before its constraints are stated. It is a motivational layer, not an enforcement layer — but it ensures models encounter the "why" before the "what," reducing rote compliance and increasing semantic uptake.

This pattern is most visible in V-05's Phase headers (e.g., "Without a stakeholders table, signal planning defaults to the PM's list of concerns...") and in the intro paragraph ("Without this skill, teams commit to feature designs based on whatever signals exist in memory..."). It doesn't change structural compliance, but it changes whether a model *understands* what it is doing when it follows the structure.

Candidate: **C-21 — Skill-level and phase-level inertia framing**: The prompt opens with a skill-level inertia statement (what teams do without the skill) and each major phase or section opens with a phase-level inertia statement (what happens at that phase boundary without the constraint). The inertia statement names the specific failure mode, not a generic "important" warning.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia opener: each skill and phase section begins by naming the ambient failure state the skill interrupts — what teams do without this step and what breaks as a result — before stating any constraints; motivational layer distinct from consequence columns which describe post-violation failure"]}
```
