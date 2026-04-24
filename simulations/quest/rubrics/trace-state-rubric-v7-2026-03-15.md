Scanning V-01 and V-02 evidence for structural patterns not yet mapped to a criterion slot.

**New signals from Round 8:**

1. **V-01 C-17 + V-02 C-17 (both variate) "at least 15 transition rows total" / "(15 operations total)"** — both variates declare a cross-pass aggregate floor alongside the per-pass floor; C-17 covers per-pass completeness but says nothing about whole-artifact aggregate completeness; the aggregate floor appears independently in two different format styles, making it a robust structural pattern.

2. **V-01 C-18 `"ID is not null"`, `"record exists"`, `"amount field is populated"` explicitly disqualified** — three patterns named in enumerated form; C-18 requires one named disqualifying example, but these three form a typed exclusion list — testable against a set rather than by inference from a single representative.

Mapped to: **C-26**, **C-27**. Aspirational pool grows from 17 to 19; cap and any-5 threshold unchanged.

---

## trace-state rubric (v23) — outer quest rubric v7

**5 essential + 3 recommended + 19 aspirational (cap 5) = 27 criteria**

### Essential (all must pass, 60 pts)

| ID | Criterion |
|----|-----------|
| C-01 | State Transition Completeness — every operation shows starting state, operation, ending state |
| C-02 | Precondition + Postcondition per operation (explicit, even if "none") |
| C-03 | Two+ domain-meaningful invariants declared and checked after every operation |
| C-04 | At least one labeled defect: type, triggering operation, reason |
| C-05 | Domain plausibility — states/ops recognizable in Sales / CS / Finance |

### Recommended (30 pts)

| ID | Criterion |
|----|-----------|
| C-06 | Consistent trace format — uniform table or numbered steps throughout |
| C-07 | Non-trivial invariants — encode real business rules, not generic structural ones |
| C-08 | Race condition analysis — one concurrent interleaving with conflict or resolution named |

### Aspirational (10 pts — 2 pts each, any 5 of 19)

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

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

### Scoring notes for v23

- **C-11** is earned only when criterion IDs appear as *field labels or inline annotations inside the output format itself*, not merely in section headings or surrounding prose.
- **C-12** requires *both* orderings explicitly described; naming one interleaving and noting "the reverse is symmetric" does not qualify.
- **C-13** requires a visible cross-reference (e.g., row ref, stage ref, or explicit linkage note) between a trace row and a declared invariant — derivation must be traceable, not implied.
- **C-14** is distinct from C-11: C-11 requires IDs to be *present* in the output; C-14 requires the schema structure itself to make criterion satisfaction *unavoidable at write time* — a cell cannot be filled without satisfying the criterion.
- **C-15** requires an actual filled row (not an empty template) with placeholder anchors (`…`, `[value]`, or equivalent) in every column; a blank schema skeleton does not qualify.
- **C-16** requires the constraint to be *named and declared* as a rule, not merely implied by format instructions; "prose is permitted if brief" disqualifies.
- **C-17** requires an explicit numeric floor (e.g., "minimum 5 rows", "at least 3 operations") declared inside the format spec itself; a qualitative instruction like "be thorough" does not qualify. C-17 covers per-pass completeness; C-26 covers cross-pass aggregate completeness — both may be earned independently.
- **C-18** requires a named *disqualifying* example — a pattern explicitly called out as insufficient (e.g., "not 'ID is not null'"); framing invariants as "role-specific" without naming what fails the bar does not qualify.
- **C-19** is distinct from C-16: C-16 requires the ban to be declared; C-19 requires the declared rule to carry an explicit consequence ("invalidates the artifact", "disqualifies the submission") — a prohibition without a stated consequence does not qualify.
- **C-20** is distinct from C-18: C-18 requires a negative model (what is disqualified); C-20 requires a positive model (what is accepted); a format that names only disqualifying patterns without a qualifying counterpart does not satisfy C-20. Naming a role category ("Finance-relevant") without a concrete positive example does not qualify.
- **C-21** requires the anti-lazy-copy constraint to be *declared inside the race condition section* (or its instructions); a general "no repetition" rule elsewhere in the prompt does not qualify. The ban must be specific to the ordering description task (e.g., "describe each ordering independently", "do not write 'same as above'").
- **C-22** requires the nil-value instruction to appear *at the field or column level* — co-located with the field it governs (e.g., "Preconditions [write `none` if genuinely absent]"); a general preamble note about empty cells does not qualify. The instruction must cover at least one field where absence is a legitimate outcome.
- **C-23** is distinct from C-19: C-19 requires a consequence at the artifact level; C-23 requires a consequence scoped to an individual section. A section that references the artifact-level rule (e.g., "see above") does not qualify — the section must declare its own consequence. One qualifying section is sufficient.
- **C-24** requires the guard to appear *co-located with the example row itself* (e.g., immediately preceding or following it, or as an annotation on the row); a general instruction elsewhere in the prompt that examples are illustrative does not qualify. The guard must name the specific example row it governs.
- **C-25** requires a *named aggregation structure* (a section, register, or table with a distinct heading) that spans at least two domain passes, with at least one cross-pass derivation reference (e.g., "Pass 1 R2") visible in the output format. An instruction to "reuse invariants across passes" without a named structure does not qualify. C-13 and C-25 may both be earned on the same output if single-trace derivation linkage and cross-domain aggregation are both present.
- **C-26** requires an explicit numeric total across all passes (e.g., "15 total", "at least 15 rows across all passes") declared inside the format spec; a per-pass floor alone (C-17) does not qualify. C-17 and C-26 may both be earned on the same output if both per-pass and aggregate floors are present.
- **C-27** requires at least two named disqualifying patterns in a visible list structure; a single named example — even a well-chosen one — satisfies C-18 but not C-27. The patterns must be explicitly named (quoted or cited), not described categorically (e.g., "structural patterns" does not qualify). C-18 and C-27 may both be earned on the same output.
- **C-09** and **C-10** remain at their v17 definitions; no scoring change.
