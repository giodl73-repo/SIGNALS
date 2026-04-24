Scanning the scorecard evidence strings for structural patterns not yet mapped to a criterion slot.

**New signals from Round 5:**

1. **V-02 C-02 "(write `none` only if genuinely absent)"** — optional fields carry an explicit nil-value instruction that distinguishes intentional absence from omission; no existing criterion captures the nil-acknowledgment pattern (C-16 bans prose substitutions; this is orthogonal — it governs absent values, not filled ones).

2. **V-02 C-08 "explicit 'Do not write same as above' ban"** — a named anti-lazy-copy constraint inside the race condition section forces each ordering to be independently described; C-12 requires both orderings to be present but says nothing about whether one may be expressed by reference to the other; this closes that gap.

3. **V-02 C-07 "gives Finance qualifying examples ('Invoice amount must remain positive after creation')"** — the invariant section names a positive qualifying example, not just a disqualifying one; C-18 captures the negative model; the complementary positive model is structurally distinct and not yet mapped.

Mapped to: **C-20**, **C-21**, **C-22**. Aspirational pool grows from 11 to 14; cap and any-5 threshold unchanged.

---

## trace-state rubric (v21) — outer quest rubric v5

**5 essential + 3 recommended + 14 aspirational (cap 5) = 22 criteria**

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

### Aspirational (10 pts — 2 pts each, any 5 of 14)

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

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

### Scoring notes for v21

- **C-11** is earned only when criterion IDs appear as *field labels or inline annotations inside the output format itself*, not merely in section headings or surrounding prose.
- **C-12** requires *both* orderings explicitly described; naming one interleaving and noting "the reverse is symmetric" does not qualify.
- **C-13** requires a visible cross-reference (e.g., row ref, stage ref, or explicit linkage note) between a trace row and a declared invariant — derivation must be traceable, not implied.
- **C-14** is distinct from C-11: C-11 requires IDs to be *present* in the output; C-14 requires the schema structure itself to make criterion satisfaction *unavoidable at write time* — a cell cannot be filled without satisfying the criterion.
- **C-15** requires an actual filled row (not an empty template) with placeholder anchors (`…`, `[value]`, or equivalent) in every column; a blank schema skeleton does not qualify.
- **C-16** requires the constraint to be *named and declared* as a rule, not merely implied by format instructions; "prose is permitted if brief" disqualifies.
- **C-17** requires an explicit numeric floor (e.g., "minimum 5 rows", "at least 3 operations") declared inside the format spec itself; a qualitative instruction like "be thorough" does not qualify.
- **C-18** requires a named *disqualifying* example — a pattern explicitly called out as insufficient (e.g., "not 'ID is not null'"); framing invariants as "role-specific" without naming what fails the bar does not qualify.
- **C-19** is distinct from C-16: C-16 requires the ban to be declared; C-19 requires the declared rule to carry an explicit consequence ("invalidates the artifact", "disqualifies the submission") — a prohibition without a stated consequence does not qualify.
- **C-20** is distinct from C-18: C-18 requires a negative model (what is disqualified); C-20 requires a positive model (what is accepted); a format that names only disqualifying patterns without a qualifying counterpart does not satisfy C-20. Naming a role category ("Finance-relevant") without a concrete positive example does not qualify.
- **C-21** requires the anti-lazy-copy constraint to be *declared inside the race condition section* (or its instructions); a general "no repetition" rule elsewhere in the prompt does not qualify. The ban must be specific to the ordering description task (e.g., "describe each ordering independently", "do not write 'same as above'").
- **C-22** requires the nil-value instruction to appear *at the field or column level* — co-located with the field it governs (e.g., "Preconditions [write `none` if genuinely absent]"); a general preamble note about empty cells does not qualify. The instruction must cover at least one field where absence is a legitimate outcome.
- **C-09** and **C-10** remain at their v17 definitions; no scoring change.
- **Aspirational cap**: score min(earned × 2, 10). A perfect output scoring all 14 aspirational criteria still earns 10 aspirational points.
