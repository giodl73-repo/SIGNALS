Reading the scorecard evidence before drafting new criteria.

**Round 11 signals not yet mapped:**

**Signal → C-32** (from V-01 C-02 evidence): `"Write \`none\` if genuinely absent — never leave these blank"` — the phrase *"never leave these blank"* is a distinct structural element separate from the nil-value token: C-22 prescribes what to write when absent; this prohibits blank cells outright, closing the loophole where a generator interprets "write `none` if absent" as permission to leave blank when content is present. Explicit anti-blank mandate co-located at the field level, independent of the nil-value instruction.

**Signal → C-33** (from V-02 C-02 field label): `Preconditions [C-02a — write "none" if genuinely absent]` — the nil-value instruction is embedded *within the sub-criterion annotation* rather than at the parent field column header or in a preamble. C-22 is satisfied by parent-field co-location; C-33 requires the nil-value instruction to appear at sub-element granularity. Achieves maximum specificity: absence acknowledgment is governed independently per sub-element.

Aspirational pool grows from 23 to 25. Cap and any-5 threshold unchanged.

---

## trace-state rubric (v26) — outer quest rubric v10

**5 essential + 3 recommended + 25 aspirational (cap 5) = 33 criteria**

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

### Aspirational (10 pts — 2 pts each, any 5 of 25)

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

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

### Scoring notes for v26

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
- **C-30** is distinct from C-11: C-11 requires IDs to be present in field labels; C-30 requires the label to also carry a behavioral directive within the same annotation — ID alone does not qualify.
- **C-31** is distinct from C-11 and C-14: C-11 requires IDs present; C-14 requires schema-level write-time enforcement; C-31 requires the criterion to be *decomposed into labeled sub-elements* — the parent ID applied to a single column does not qualify.
- **C-32** is distinct from C-22: C-22 prescribes what to write when absent; C-32 prohibits blank cells outright. Both may be earned independently. A prompt that carries "write `none` if absent" (C-22) but omits "never leave blank" (C-32) satisfies C-22 only. A prompt with both satisfies both.
- **C-33** is distinct from C-22 and C-31: C-22 requires nil-value instruction at field level (parent column satisfies); C-31 requires sub-element decomposition (decomposition alone, without nil-value content, satisfies); C-33 requires the nil-value instruction to appear *within* the sub-criterion annotation itself — the most granular possible placement. A parent field annotation with a nil-value instruction satisfies C-22 but not C-33.
