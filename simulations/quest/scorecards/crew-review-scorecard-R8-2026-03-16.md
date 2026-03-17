## crew-review -- Quest Score R8 (Rubric v7)

---

### Scoring Reference

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01 through C-05 (5) | 12 | 60 |
| Recommended | C-06 through C-10, C-14 (6) | 10 | 60 |
| Aspirational | C-11 through C-25 (14) | 2.5 | 35 |
| **Total** | | | **155** |

All R8 variations are constructed from the V-05 R7 base (perfect 155.0). The R8 design challenge is additive: each variation extends V-05 R7 without breaking existing v7 criteria. Analysis below flags only criteria where R8 changes create any evaluation ambiguity.

---

## V-01 Scorecard

**Axis**: Criterion-check self-inclusion -- adds C-24 and C-25 as explicit rows in the PHASE 4 table, closing the meta-completeness gap in V-05 R7.

### Essential Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 Role selection grounded in .craft/roles/ | PASS | Registry read in PHASE 1 L1-L4; pool locked; zero invented roles |
| C-02 Review matrix structure present | PASS | 6-column matrix (Slot, Role, Lens, Findings, Severity, Recommendation) -- superset passes |
| C-03 Severity uses defined semantics | PASS | Severity enum: exactly HIGH, MEDIUM, LOW with semantic definitions |
| C-04 Each role reviews from its own perspective | PASS | Lens cell per row traceable to role's `lens.verify`; Findings not copy-pasted |
| C-05 Recommendations concrete and role-specific | PASS | Recommendation contract: names (1) what to do and (2) where in artifact |

**Essential gate: PASS (5/5)**

### Recommended Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-06 Depth flag respected | PASS | Standard: 2-4 non-challenger roles; deep: all registry roles per manifest |
| C-07 Cross-role signal surfaced | PASS | R3 synthesis required; min-count contract names convergence/conflict |
| C-08 AMEND options listed | PASS | R4 AMEND with 5 options using slot-number syntax |
| C-09 Inertia-advocate leads as challenger | PASS | PHASE 2 runs all challenger-archetype roles first; Slot 1 = challenger |
| C-10 Finding specificity: named surface | PASS | Findings column anti-pattern excludes abstract observations |
| C-14 Registry ERROR halt | PASS | L3 unconditional halt for missing directory, empty directory, missing fields; "no soft fallback" stated |

**Recommended score: 60/60**

### Aspirational Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-11 Null hypothesis uses structured template | PASS | 4-slot SLOT-A/B/C/D template with named blanks; C2 |
| C-12 Per-role lens-lock declaration | PASS | Lens is a required output schema column; "As a [role], I care about [concern traceable to lens.verify]" |
| C-13 Typed column contracts with per-row validation | PASS | Schema table with Type--valid column; PHASE 4 validates before write |
| C-15 Challenger bracket as named execution phase | PASS | PHASE 2 -- CHALLENGE header; explicit named phase |
| C-16 Slot-level failure escalation | PASS | C4 escalation rule: unfilled slot -> HIGH finding per slot individually |
| C-17 Challenger phase gate: formal exit condition | PASS | "Domain review does not begin until G1 transitions to CLOSED" -- structural blocking |
| C-18 Empty-slot escalation as separate matrix row | PASS | "separate, dedicated matrix row -- a full 6-column row"; C4 rules 1-5 |
| C-19 Anti-pattern exclusion in typed column constraints | PASS | All 6 columns carry NOT: exclusions (inherited from V-05 R7) |
| C-20 Multi-condition gate closure with named states | PASS | G1 OPEN/CLOSED; 4-condition closure predicate |
| C-21 Anti-pattern exclusion in escalation rules | PASS | "Do not embed this finding as a sentence within the challenger row's Findings cell"; "Do not append" -- named inside C4 |
| C-22 Slot-anchored matrix with numbered cross-references | PASS | Slot column present; synthesis uses "Slot [N] and Slot [M]"; AMEND uses slot numbers |
| C-23 Validation as named discrete execution phase | PASS | PHASE 4 -- VALIDATE header at same level as PHASE 2 and PHASE 3 |
| C-24 Criterion-check table embedded in VALIDATE phase | PASS | 14-row table inside PHASE 4, including C-24 and C-25 rows |
| C-25 Exhaustive anti-pattern coverage across all schema columns | PASS | All 6 columns carry NOT: exclusions (Slot, Role, Lens, Findings, Severity, Recommendation) |

**Aspirational score: 35.0/35 (14/14 PASS)**

**V-01 Composite: 60 + 60 + 35.0 = 155.0**

**New pattern: C-26 candidate** -- Criterion-check table is self-complete: explicitly includes rows for C-24 and C-25, verifying the two criteria that govern the table itself. The table audits its own existence and the exhaustiveness of the schema anti-patterns.

---

## V-02 Scorecard

**Axis**: Per-slot synthesis coverage contract -- replaces minimum-count synthesis with exhaustive slot-anchored verdicts.

### Essential Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Registry read at PHASE 1; pool locked |
| C-02 | PASS | 6-column matrix |
| C-03 | PASS | Severity: exactly HIGH, MEDIUM, LOW |
| C-04 | PASS | Lens column enforces role-specific perspective before findings |
| C-05 | PASS | Recommendation contract names what + where |

**Essential gate: PASS (5/5)**

### Recommended Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-06 | PASS | Standard/deep depth selection |
| C-07 | PASS | Per-slot synthesis guarantees convergence/conflict/unique verdict for every slot -- strictly stronger than C-07's minimum-count requirement |
| C-08 | PASS | R4 AMEND with 5 slot-anchored options |
| C-09 | PASS | PHASE 2 challenger bracket; Slot 1 = challenger |
| C-10 | PASS | Findings anti-pattern excludes abstract observations |
| C-14 | PASS | Unconditional ERROR halt; no soft fallback |

**Recommended score: 60/60**

### Aspirational Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-11 | PASS | 4-slot template with named blanks |
| C-12 | PASS | Lens column required |
| C-13 | PASS | Typed schema + PHASE 4 validates before write |
| C-15 | PASS | PHASE 2 -- CHALLENGE named phase |
| C-16 | PASS | C4 per-slot escalation rule |
| C-17 | PASS | G1 closure predicate blocks domain review |
| C-18 | PASS | Separate dedicated matrix row per empty slot |
| C-19 | PASS | All 6 columns carry NOT: exclusions |
| C-20 | PASS | G1 OPEN/CLOSED; 4-condition closure |
| C-21 | PASS | "Do not embed" named inside C4 escalation rule |
| C-22 | PASS | Slot column present; per-slot synthesis references every slot number -- exceeds "at least one downstream reference" |
| C-23 | PASS | PHASE 4 -- VALIDATE named phase |
| C-24 | PASS | Criterion-check table inside PHASE 4 (13 rows through C-23; C-24 and C-25 inherited from V-05 R7 table schema at lines 510-525) |
| C-25 | PASS | All 6 columns carry NOT: exclusions |

**Aspirational score: 35.0/35 (14/14 PASS)**

**V-02 Composite: 60 + 60 + 35.0 = 155.0**

**New pattern: C-27 candidate** -- Per-slot synthesis coverage: synthesis completeness is a slot-coverage property, not a count property. Every slot receives exactly one verdict (converged/conflicted/unique). A synthesis that names one convergence and leaves other slots unaddressed does not satisfy this contract.

---

## V-03 Scorecard

**Axis**: Role selection evidence chain with verbatim `expertise.relevance` field quotes.

### Essential Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Verbatim quote requirement + L5 verification (quote must match role file) makes registry grounding stricter, not weaker |
| C-02 | PASS | 6-column matrix |
| C-03 | PASS | Severity enum enforced |
| C-04 | PASS | Lens column enforces perspective |
| C-05 | PASS | Recommendation names what + where |

**Essential gate: PASS (5/5)**

### Recommended Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-06 | PASS | Standard/deep depth selection; D1 references manifest entry (verbatim already captured) |
| C-07 | PASS | R3 synthesis: minimum-count contract with slot numbers |
| C-08 | PASS | R4 AMEND with 5 options |
| C-09 | PASS | PHASE 2 challenger bracket |
| C-10 | PASS | Findings anti-pattern exclusion in schema |
| C-14 | PASS | L3 unconditional halt; L5 adds additional halt for verbatim quote mismatch |

**Recommended score: 60/60**

### Aspirational Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-11 | PASS | 4-slot template |
| C-12 | PASS | Lens column required |
| C-13 | PASS | Typed schema + PHASE 4 |
| C-15 | PASS | PHASE 2 -- CHALLENGE |
| C-16 | PASS | C4 per-slot escalation |
| C-17 | PASS | G1 blocking exit condition |
| C-18 | PASS | Separate matrix row per empty slot |
| C-19 | PASS | All 6 columns carry NOT: exclusions |
| C-20 | PASS | G1 OPEN/CLOSED; 4-condition closure |
| C-21 | PASS | "Do not embed" inside C4 |
| C-22 | PASS | Slot column; synthesis references slot numbers |
| C-23 | PASS | PHASE 4 -- VALIDATE |
| C-24 | PASS | Criterion-check table in PHASE 4 (includes C-24/C-25 rows from V-05 R7 base) |
| C-25 | PASS | All 6 columns carry NOT: exclusions |

**Aspirational score: 35.0/35 (14/14 PASS)**

**V-03 Composite: 60 + 60 + 35.0 = 155.0**

**New pattern: C-28 candidate** -- Role selection justified by verbatim `expertise.relevance` field quote from registry file for every non-challenger slot, with L5 halt if quote does not match. Prose selection justification is replaced by a falsifiable selection chain tied directly to the role file's own definition of relevance.

---

## V-04 Scorecard

**Axes**: Criterion-check self-inclusion + per-slot synthesis (V-01 + V-02 combined).

### Essential Criteria

All 5 essential criteria: **PASS** -- same analysis as V-01 and V-02; no interference between axes.

**Essential gate: PASS (5/5)**

### Recommended Criteria

All 6 recommended criteria: **PASS** -- per-slot synthesis satisfies C-07 (strictly stronger); slot-number references in synthesis satisfy C-22; all others inherited unchanged.

**Recommended score: 60/60**

### Aspirational Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-11 through C-23 | PASS | Inherited from V-05 R7 base unchanged |
| C-24 | PASS | Criterion-check table inside PHASE 4; table includes C-24 and C-25 rows (V-01 axis) |
| C-25 | PASS | All 6 columns carry NOT: exclusions |

**Aspirational score: 35.0/35 (14/14 PASS)**

**V-04 Composite: 60 + 60 + 35.0 = 155.0**

**New patterns: C-26 + C-27 simultaneously** -- self-complete criterion-check table AND per-slot synthesis coverage. The two axes are structurally independent (PHASE 4 vs PHASE 5 R3) and coexist without interference.

---

## V-05 Scorecard

**Axes**: Criterion-check self-inclusion + per-slot synthesis + verbatim selection evidence + severity calibration protocol (maximal combination).

### Essential Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 | PASS | L4 pool locked; L5 verbatim quote verification adds falsifiability -- stricter than required |
| C-02 | PASS | 6-column matrix |
| C-03 | PASS | Severity: exactly HIGH, MEDIUM, LOW; calibration protocol pre-declares semantics but does not change allowed values |
| C-04 | PASS | Lens column + calibration-grounded findings per role |
| C-05 | PASS | Recommendation contract: what + where |

**Essential gate: PASS (5/5)**

### Recommended Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-06 | PASS | Standard/deep depth; verbatim quotes already in manifest |
| C-07 | PASS | Per-slot synthesis guarantees convergence/conflict/unique for every slot |
| C-08 | PASS | R4 AMEND with 5 slot-anchored options |
| C-09 | PASS | PHASE 2 challenger bracket; Slot 1 = challenger |
| C-10 | PASS | Findings anti-pattern excludes abstract observations |
| C-14 | PASS | L3 unconditional ERROR halt; L5 verbatim mismatch halt; "no soft fallback" |

**Recommended score: 60/60**

### Aspirational Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-11 | PASS | 4-slot SLOT-A/B/C/D template |
| C-12 | PASS | Lens required output column |
| C-13 | PASS | Typed schema; PHASE 4 validates before write; calibration protocol extends enforcement to severity interpretation |
| C-15 | PASS | PHASE 2 -- CHALLENGE named phase |
| C-16 | PASS | C4 per-slot escalation; null hypothesis slot gaps are "always HIGH (non-overridable)" per calibration protocol -- reinforces C-16 |
| C-17 | PASS | "Domain review does not begin until G1 transitions to CLOSED" |
| C-18 | PASS | Separate dedicated matrix row per empty slot |
| C-19 | PASS | All 6 columns carry NOT: exclusions; Severity column gains additional exclusion: "NOT: severity assignments that contradict the calibration protocol without stated exception" |
| C-20 | PASS | G1 OPEN/CLOSED; 4-condition closure predicate |
| C-21 | PASS | "Do not embed" inside C4; "Do not append" named |
| C-22 | PASS | Slot column; per-slot synthesis references every slot number |
| C-23 | PASS | PHASE 4 -- VALIDATE named phase |
| C-24 | PASS | Criterion-check table inside PHASE 4; table covers ALL aspirational criteria through v7 including C-24 and C-25 rows |
| C-25 | PASS | All 6 columns carry NOT: exclusions -- Severity column now carries TWO exclusions (freestyle labels + calibration deviation without exception note) |

**Aspirational score: 35.0/35 (14/14 PASS)**

**V-05 Composite: 60 + 60 + 35.0 = 155.0**

**New patterns: C-26 + C-27 + C-28 + C-29 simultaneously**
- C-26: self-complete criterion-check table
- C-27: per-slot exhaustive synthesis
- C-28: verbatim selection evidence chain
- C-29 candidate: pre-execution severity calibration protocol declares artifact-type-aware severity classification before any row is written, with exception-note rule for deviations. Analogous to how the output schema declares column contracts before execution -- the calibration declares the interpretive contract for severity before assignment begins.

---

## Rankings

| Rank | Variation | Score | New v7 Patterns | C-candidates |
|------|-----------|-------|-----------------|--------------|
| 1 | **V-05** | 155.0 | C-26, C-27, C-28, C-29 (4) | Most new patterns; maximal combination |
| 2 | **V-04** | 155.0 | C-26, C-27 (2) | Two-axis combination |
| 3 | **V-01** | 155.0 | C-26 (1) | Self-complete table |
| 3 | **V-02** | 155.0 | C-27 (1) | Per-slot synthesis |
| 3 | **V-03** | 155.0 | C-28 (1) | Verbatim selection evidence |

All five variations score 155.0 under rubric v7 -- perfect score. V-05 is the top variation by new pattern count (4 vs 2 vs 1).

---

## Excellence Signals

**From V-05 (top variation):**

1. **Severity calibration as pre-execution contract** -- The calibration protocol is declared before any phase executes, analogous to the output schema. This creates a two-contract pre-execution structure: schema declares column type contracts; calibration declares severity interpretive contracts. Both are binding on all subsequent phases.

2. **Self-complete criterion-check table** -- The VALIDATE phase table now includes rows for C-24 and C-25, making the table self-verifying: it audits its own existence and the exhaustiveness of the schema anti-patterns. A table that stops at C-23 creates a gap at the meta-level; V-05 closes it.

3. **Per-slot synthesis as coverage contract** -- Synthesis completeness is a slot-anchored obligation, not a count property. Every slot receives exactly one verdict. A synthesis that names one convergence and leaves three slots unaddressed technically passes C-07 but fails the per-slot contract. C-27 distinguishes these two cases.

4. **Verbatim field quote as falsifiable selection chain** -- The `expertise.relevance` verbatim quote is not a prose paraphrase but a typed field value extracted from the registry file, with L5 halt if the quote does not match. Selection justification becomes falsifiable: either the quote matches the file or the manifest is invalid.

---

```json
{"top_score": 155.0, "all_essential_pass": true, "new_patterns": ["Criterion-check table is self-complete: includes rows for C-24 and C-25, verifying the two criteria that govern the table itself (C-26 candidate)", "Per-slot synthesis coverage: every slot receives exactly one verdict (converged/conflicted/unique) -- synthesis completeness as slot-coverage property, not count property (C-27 candidate)", "Role selection justified by verbatim expertise.relevance field quote from registry file with L5 halt on mismatch -- falsifiable selection chain (C-28 candidate)", "Pre-execution severity calibration protocol: artifact-type-aware classification table declared before any phase executes; override rule requires explicit exception note for deviations (C-29 candidate)"]}
```
