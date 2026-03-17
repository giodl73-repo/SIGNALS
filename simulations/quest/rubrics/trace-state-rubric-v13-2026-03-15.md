Here is the complete updated rubric (v13 / inner v29).

---

## Changes from v12 → v13

**Two new aspirational criteria extracted from R14 excellence signals:**

### C-38 — Step-label criterion-instruction fusion
**Source**: V-02 earns C-11 *partially* ("IDs appear in step headers but not field-level annotations — step format has no table columns") and *fails* C-30 ("step labels carry IDs but no behavioral directive at column level"). Together these notes reveal the achievable ceiling for step-block format: a step label or within-block field annotation that carries both a criterion ID **and** a behavioral directive. This is the step-block-format analog of C-30.

Key distinctions:
- A step label carrying only a criterion ID (V-02's partial C-11) does not qualify
- Achieving C-30 in a tabular format does not cross-satisfy C-38
- C-30 and C-38 are format-specific analogs — they do not cross-satisfy

### C-39 — Step-block disqualification-condition fusion
**Source**: V-02 deliberately omits C-34 and C-36; the scorecard shows no attempt to carry disqualification-condition annotations at the step-field level. The deliberate-absence pattern exposes the parallel ceiling: a step label or within-block field annotation that carries both a criterion ID **and** the specific pattern that *fails* the criterion. The step-block-format analog of C-34.

Key distinctions:
- C-38 and C-39 are orthogonal axes of the same annotation (a single label can satisfy both)
- Achieving C-34 in a tabular format does not cross-satisfy C-39
- A step label carrying only a criterion ID does not qualify

**Pool: 29 → 31 aspirationals (C-09–C-39). Aspirational point value: 50/31 ≈ 1.61 pts each.**

The scoring notes section adds C-38 and C-39 entries and updates several prior notes (C-14, C-15, C-17, C-22, C-30, C-31, C-32, C-33, C-34) to explicitly state that those criteria apply to tabular formats and direct scorers to C-38/C-39 for step-block equivalents.
.61 pts each.**

---

## Design Rationale

**Essential (50 pts)** — the five things that make a trace-state output useful at all:
- C-01: every operation expressed as a named before/after state triple
- C-02: preconditions + postconditions per operation (not just "what happened" but "why it was allowed")
- C-03: domain-meaningful invariants named and checked (the thing a state machine analysis is hunting for)
- C-04: at least one labeled defect (the deliverable — no finding = no signal)
- C-05: domain grounding (Sales / CS / Finance vocabulary — otherwise it's a toy example)

**Recommended (not scored separately — see scoring):**
- C-06: Consistent trace format — uniform table or numbered steps throughout
- C-07: Non-trivial invariants — encode real business rules, not generic structural ones
- C-08: Race condition analysis — one concurrent interleaving with conflict or resolution named

**Aspirational (50 pts — any of 31, each ≈ 1.61 pts):**
- C-09 through C-39: see full aspirationals list below (accumulated from R1–R14 excellence signals)

---

## Scoring

- 5 essential criteria × 10 pts = **50 pts**
- 31 aspirationals (C-09–C-39): each = 50/31 ≈ **1.61 pts**, total max 50 pts
- **Total max = 100 | Golden threshold = 80**

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

## Essential Criteria

| ID | Criterion |
|----|-----------|
| C-01 | State Transition Completeness — every operation shows starting state, operation, ending state |
| C-02 | Precondition + Postcondition per operation (explicit, even if "none") |
| C-03 | Two+ domain-meaningful invariants declared and checked after every operation |
| C-04 | At least one labeled defect: type, triggering operation, reason |
| C-05 | Domain plausibility — states/ops recognizable in Sales / CS / Finance |

**Pass condition for essentials**: all five must pass. A single essential failure disqualifies
the artifact from the golden threshold regardless of composite score.

---

## Recommended Criteria

| ID | Criterion |
|----|-----------|
| C-06 | Consistent trace format — uniform table or numbered steps throughout |
| C-07 | Non-trivial invariants — encode real business rules, not generic structural ones |
| C-08 | Race condition analysis — one concurrent interleaving with conflict or resolution named |

---

## Aspirational Criteria

| ID | Criterion |
|----|-----------|
| C-09 | Negative path trace — one rejected operation with all four elements (invalid state, blocked op, unchanged state, named error) |
| C-10 | Reachability annotation — every omitted transition listed with rationale; silent omissions do not qualify |
| C-11 | Inline criterion anchoring — output format embeds rubric criterion IDs at individual elements (e.g., field labels carry IDs like `C-01a`, `C-03: never skip`), making satisfaction auditable at the element level without cross-referencing |
| C-12 | Symmetric interleaving — race condition section describes both orderings (A→B **and** B→A) for at least one concurrent operation pair, surfacing asymmetric conflict outcomes that single-direction analysis misses |
| C-13 | Invariant derivation pipeline — forward trace rows are cross-referenced as invariant candidates with explicit linkage, showing how observed business transitions generate declared invariants rather than declaring invariants independently |
| C-14 | Schema-level write-time enforcement — column headers or schema slots embed criterion IDs such that filling any cell mechanically satisfies the criterion; rubric compliance becomes structurally unavoidable, not instruction-dependent |
| C-15 | Example row with placeholder syntax — the output format includes at least one filled example row with `…` anchors showing exactly what belongs in each cell, eliminating schema ambiguity before generation begins |
| C-16 | Hard no-prose-substitution constraint — a named ban on prose fallback (e.g., "no prose substitutions") is declared as a hard rule, preventing narrative format from evading structural criteria |
| C-17 | Quantified trace floor — the output format schema declares an explicit minimum row count for the state transition table (e.g., "minimum 5 rows"), making trace completeness measurable at generation time rather than qualitative |
| C-18 | Named anti-example for invariant triviality — the invariant section names at least one disqualifying pattern (e.g., "not 'ID is not null'"), making the non-triviality requirement testable by exclusion rather than by inference from role framing alone |
| C-19 | Artifact invalidation clause — at least one hard constraint explicitly states that violation *invalidates* the artifact (not merely violates instructions), creating a consequence mechanism that distinguishes enforcement from instruction |
| C-20 | Named qualifying example for invariant scope — the invariant section names at least one positive qualifying example (a pattern explicitly cited as acceptable, e.g., "Invoice amount must remain positive after creation"), complementing any disqualifying example with a positive model of what a valid domain invariant looks like |
| C-21 | Anti-lazy-copy constraint in race section — a named ban on cross-referencing between ordering descriptions (e.g., "do not write 'same as above'") is declared in the race condition section, requiring each ordering to be independently and fully described rather than expressed by reference to the other |
| C-22 | Nil-value acknowledgment syntax — optional or potentially-absent fields carry an explicit nil-value instruction (e.g., "write `none` if genuinely absent") rather than leaving blanks unmarked, making intentional absence distinguishable from omission at generation time |
| C-23 | Section-level invalidation clause — at least one section (distinct from the whole artifact) declares its own scoped invalidation consequence for non-compliance (e.g., "Silent omissions invalidate this section"), creating section-granular enforcement independent of the artifact-level rule in C-19 |
| C-24 | Anti-literal-copy guard on example rows — the example row carries an explicit instruction preventing it from being reproduced verbatim in the output (e.g., "do not include in output"), ensuring the template serves as a reference anchor without polluting generation with literal copy |
| C-25 | Cross-domain invariant aggregation register — a named consolidated structure (e.g., "Invariant Register") aggregates invariants from all domain passes with explicit cross-pass derivation linkage (e.g., `Derived From: Pass 1 R2, Pass 2 R1`), making multi-domain synthesis traceable rather than per-domain isolated |
| C-26 | Cross-pass aggregate trace floor — the output format schema declares an explicit numeric floor for total transition rows across ALL domain passes (e.g., "at least 15 transition rows total"), making whole-artifact trace completeness measurable at the aggregate level independently of any per-pass floor |
| C-27 | Enumerated invariant exclusion list — the invariant section names at least two disqualifying patterns in a visible list structure (e.g., `"ID is not null"`, `"record exists"`, `"amount field is populated"`), forming a typed exclusion set that makes the non-triviality bar testable against an enumeration rather than by inference from a single example |
| C-28 | Named concurrent-operation pair — the race condition section explicitly names both concurrent operations involved in the interleaving (e.g., `Operations: X and Y`, `Op A: ___ / Op B: ___`), making the interleaving's source unambiguous; naming only the conflict outcome or only one operation does not qualify |
| C-29 | Active mutation-verification instruction — the negative path section declares an explicit instruction to actively verify state immutability after a rejected operation (e.g., "confirm no mutation occurred", "verify starting state is unchanged"), going beyond passive representation of the pre-operation state as a column value; an output that merely records unchanged state without an active-verification directive does not qualify |
| C-30 | Criterion-instruction fusion in field labels — at least one field label embeds both a criterion ID and a brief behavioral directive co-located within the same annotation (e.g., `[C-03: minimum 2 per pass — never skip]`, `[C-06: uniform format throughout]`), making the compliance requirement self-documenting at the schema level without external cross-reference; a label carrying only an ID (e.g., `[C-03]`) does not qualify |
| C-31 | Sub-criterion element decomposition — at least one multi-element criterion is decomposed into individually labeled sub-element annotations within the output schema (e.g., `Defect type [C-04a]`, `Triggering operation [C-04b]`, `Reason [C-04c]`; or `[C-09a]`–`[C-09d]`), making each element independently satisfiable and auditable; a field carrying only the parent criterion ID (e.g., `[C-04]`) does not qualify |
| C-32 | Mandatory-fill prohibition on absence-eligible fields — at least one field or column where absence is a legitimate outcome carries an explicit anti-blank instruction (e.g., "never leave blank", "must always be filled") in addition to any nil-value token, prohibiting blank cells outright rather than merely prescribing the absence token; a nil-value instruction alone (C-22) without an explicit anti-blank prohibition does not qualify; a general "be thorough" instruction does not qualify |
| C-33 | Sub-element nil-value annotation — a nil-value instruction is embedded within a sub-criterion annotation rather than at the parent field column header or in a preamble (e.g., `Preconditions [C-02a — write "none" if genuinely absent]`), making absence acknowledgment granular to each sub-element independently; a nil-value instruction co-located only at the parent field level satisfies C-22 but does not qualify for C-33; a preamble-level nil-value instruction does not qualify regardless of how specifically it references the field |
| C-34 | Disqualification-condition fusion in field labels — at least one field label embeds the criterion ID co-located with the specific negative test: the exact pattern that *fails* the criterion (e.g., `[C-17: qualitative 'be thorough' does not satisfy]`, `[C-28: naming only the conflict outcome does not qualify]`). C-30 and C-34 are orthogonal axes of the same label; a single annotation can satisfy both if it carries a directive *and* a disqualification condition. A general prohibition without a named failing pattern does not qualify |
| C-35 | Section-label criterion-consequence fusion — the section heading itself (not body prose) carries a criterion ID + conditional consequence clause (e.g., `[C-17: if fewer than 5 blocks...]`), making enforcement visible at structural navigation level before any field in the section is read. Distinct from C-23 (invalidation clause anywhere in section prose) and C-19 (artifact-level clause anywhere in hard constraints); a body-level invalidation sentence satisfies C-23 but not C-35 |
| C-36 | Disqualification-condition fusion on structural-format field labels — at least one field label whose criterion prescribes a structural output format embeds the criterion ID co-located with the specific failing format pattern (e.g., `[C-01b: disqualifies if description written instead of state name]`, `[C-01c: disqualifies if verb phrase used instead of noun phrase]`). Extends C-34 from value-content and quantitative fields to structural output-format fields: any criterion that names a correct format has a corresponding disqualifying format expressible in its label. A C-34-qualifying disqualification condition on a quantitative or identifier field does not satisfy C-36 |
| C-37 | Section-label criterion-consequence fusion at domain-pass heading tier — the `### Pass N` heading (or equivalent domain-pass heading) itself carries a criterion ID + conditional consequence clause (e.g., `[C-05: if states and operations are not recognizable in the CS domain, C-05 fails]`), making enforcement visible at the domain entry point before any section heading, column header, or cell in the pass is read. Distinct from C-35, which covers sub-section headings (invariant registers, defect logs, etc.); a C-35-qualifying annotation on a sub-section heading does not satisfy C-37. Achieving C-37 does not retroactively satisfy C-35 unless a sub-section heading also independently carries a qualifying annotation |
| C-38 | Step-label criterion-instruction fusion — in a non-tabular (step-block) output format, at least one step label or within-block field annotation carries both a criterion ID and a behavioral directive co-located within the same annotation (e.g., `State name [C-01: noun-phrase only — never write a description]:`). This is the step-block-format analog of C-30, which applies to column and field labels in tabular formats. A step label carrying only a criterion ID (partially satisfying C-11 in step format) does not qualify; achieving C-30 in a tabular format does not satisfy C-38; C-30 and C-38 are format-specific analogs and do not cross-satisfy |
| C-39 | Step-block disqualification-condition fusion — in a non-tabular (step-block) output format, at least one step label or within-block field annotation carries both a criterion ID and the specific pattern that *fails* the criterion co-located within the same annotation (e.g., `State name [C-01: disqualifies if description written instead of noun-phrase state name]:`). This is the step-block-format analog of C-34. C-38 and C-39 are orthogonal axes of the same step-level annotation: a single annotation can satisfy both if it carries a behavioral directive *and* a disqualification condition. Achieving C-34 in a tabular format does not satisfy C-39; a step label carrying only a criterion ID does not qualify |

---

## Scoring Notes for v29

- **C-11** is earned only when criterion IDs appear as *field labels or inline annotations inside the output format itself*, not merely in section headings or surrounding prose. In a step-block format, "inside the output format" means within step labels or step-field annotations, not only in the section heading that introduces the step block. A step-block format that places IDs only in section headings earns neither C-11 nor C-38.
- **C-12** requires *both* orderings explicitly described; naming one interleaving and noting "the reverse is symmetric" does not qualify.
- **C-13** requires a visible cross-reference (e.g., row ref, stage ref, or explicit linkage note) between a trace row and a declared invariant — derivation must be traceable, not implied.
- **C-14** is distinct from C-11: C-11 requires IDs to be *present* in the output; C-14 requires the schema structure itself to make criterion satisfaction *unavoidable at write time* — a cell cannot be filled without satisfying the criterion. C-14 applies to tabular formats only; a step-block format cannot satisfy C-14 because it has no column headers.
- **C-15** requires an actual filled row (not an empty template) with placeholder anchors (`…`, `[value]`, or equivalent) in every column; a blank schema skeleton does not qualify. In step-block format, a filled example step block with placeholder anchors in every step-field satisfies C-15.
- **C-16** requires the constraint to be *named and declared* as a rule, not merely implied by format instructions; "prose is permitted if brief" disqualifies.
- **C-17** requires an explicit numeric floor (e.g., "minimum 5 rows", "at least 3 operations") declared inside the format spec itself; a qualitative instruction like "be thorough" does not qualify. In step-block format, a step-count floor (e.g., "minimum 5 step blocks per pass") satisfies C-17. C-17 covers per-pass completeness; C-26 covers cross-pass aggregate completeness — both may be earned independently.
- **C-18** requires a named *disqualifying* example — a pattern explicitly called out as insufficient (e.g., "not 'ID is not null'"); framing invariants as "role-specific" without naming what fails the bar does not qualify.
- **C-19** is distinct from C-16: C-16 requires the ban to be declared; C-19 requires the declared rule to carry an explicit consequence ("invalidates the artifact", "disqualifies the submission") — a prohibition without a stated consequence does not qualify.
- **C-20** is distinct from C-18: C-18 requires a negative model (what is disqualified); C-20 requires a positive model (what is accepted); a format that names only disqualifying patterns without a qualifying counterpart does not satisfy C-20. Naming a role category ("Finance-relevant") without a concrete positive example does not qualify.
- **C-21** requires the anti-lazy-copy constraint to be *declared inside the race condition section* (or its instructions); a general "no repetition" rule elsewhere in the prompt does not qualify. The ban must be specific to the ordering description task (e.g., "describe each ordering independently", "do not write 'same as above'").
- **C-22** requires the nil-value instruction to appear *at the field or column level* — co-located with the field it governs (e.g., "Preconditions [write `none` if genuinely absent]"); a general preamble note about empty cells does not qualify. The instruction must cover at least one field where absence is a legitimate outcome. In step-block format, a step-field-level nil-value instruction satisfies C-22.
- **C-30** is distinct from C-11: C-11 requires IDs to be present in field labels; C-30 requires the label to also carry a behavioral directive within the same annotation — ID alone does not qualify. C-30 applies to tabular-format field labels and column headers; for step-block format, see C-38.
- **C-31** is distinct from C-11 and C-14: C-11 requires IDs present; C-14 requires schema-level write-time enforcement; C-31 requires the criterion to be *decomposed into labeled sub-elements* — the parent ID applied to a single column does not qualify. C-31 applies to tabular formats; a step-block format that cannot produce column-level decomposition cannot satisfy C-31.
- **C-32** is distinct from C-22: C-22 prescribes what to write when absent; C-32 prohibits blank cells outright. Both may be earned independently. C-32 applies to tabular-format columns; for step-block format equivalents, see C-38 (directive fusion) or use prose-guard language within step-field annotations.
- **C-33** is distinct from C-22 and C-31: C-22 requires nil-value instruction at field level (parent column satisfies); C-31 requires sub-element decomposition; C-33 requires the nil-value instruction to appear *within* the sub-criterion annotation itself — the most granular possible placement. C-33 applies to tabular-format sub-criterion annotations.
- **C-34** is distinct from C-30: C-30 requires a behavioral directive (what to do); C-34 requires a disqualification condition (the exact pattern that fails). Both are orthogonal axes of the same label. C-34 applies to tabular-format field labels; for step-block format, see C-39.
- **C-35** is distinct from C-23 and C-19: C-23 requires an invalidation clause anywhere in section *body prose*; C-19 requires a consequence clause anywhere in artifact-level hard constraints; C-35 requires the consequence to appear *in the section heading itself*. A body sentence even adjacent to the heading does not satisfy C-35.
- **C-36** is distinct from C-34: C-34 covers value-content fields (quantitative floors, identifier naming patterns, behavioral outcomes); C-36 covers structural output-format fields (state naming convention, phrase-type requirements such as noun vs. verb phrase). A disqualification condition on a quantitative floor field satisfies C-34 but not C-36.
- **C-37** is distinct from C-35: C-35 covers sub-section headings (invariant registers, defect logs, race condition sections); C-37 requires the annotation to appear on the `### Pass N` domain-pass heading, the highest structural navigation node below the artifact title. A C-35-qualifying annotation on any heading below the Pass-N tier does not satisfy C-37.
- **C-38** is the step-block-format analog of C-30. It requires (a) a non-tabular step-block output format AND (b) a step label or step-field annotation carrying both a criterion ID and a behavioral directive. A tabular format earning C-30 does not satisfy C-38; a step-block format with C-11 partial credit (IDs in step headers only) does not satisfy C-38; both C-30 and C-38 may be earned in the same artifact only if the artifact contains both a tabular section and a step-block section, each independently qualifying.
- **C-39** is the step-block-format analog of C-34. It requires (a) a non-tabular step-block output format AND (b) a step label or step-field annotation carrying both a criterion ID and the specific failing pattern. C-38 and C-39 are orthogonal axes of the same step-level annotation: a single annotation can satisfy both by carrying a directive and a disqualification condition. A tabular format earning C-34 does not satisfy C-39.
