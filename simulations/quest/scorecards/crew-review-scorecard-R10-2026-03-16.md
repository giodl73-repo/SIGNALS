# crew-review -- Round 10 Scorecard

## Scoring Method

Essential: 5 x 12 = 60 max | Recommended: 6 x 10 = 60 max | Aspirational: 17 x 2.5 = 42.5 max | **Total max: 162.5**

PARTIAL = half points. Golden threshold: >= 80 with all essential passing.

---

## V-01 -- Lifecycle emphasis (direct triple-close)

**Design**: V-01 R9 + R3 per-slot coverage contract + 5-column criterion-check table through C-28.

### Essential (12 pts each)

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role selection grounded in .roles/ | PASS | L3 unconditional ERROR halts (absent/empty/malformed); L4 pool locked; zero invention |
| C-02 | Review matrix structure present | PASS | 6-column matrix (Slot, Role, Lens, Findings, Severity, Recommendation); superset passes |
| C-03 | Severity uses HIGH/MEDIUM/LOW only | PASS | Schema enum contract; NOT: freestyle labels; PHASE 4 validates before write |
| C-04 | Each role reviews from its own perspective | PASS | Lens column requires traceable to `lens.verify`; D2 anti-pattern exclusion prevents copy-paste |
| C-05 | Recommendations are concrete | PASS | Schema: "names (1) what to do and (2) where in the artifact"; NOT: generic directives |

**Essential subtotal: 60/60**

### Recommended (10 pts each)

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-06 | Depth flag respected | PASS | Standard 2-4 non-challenger roles; deep = all non-challenger; D1 documents selection reason |
| C-07 | Cross-role signal surfaced | PASS | R3 synthesis always present; per-slot coverage guarantees convergence/conflict/unique for every slot |
| C-08 | AMEND options listed | PASS | R4 AMEND section with 5 slot-numbered options |
| C-09 | Inertia-advocate leads as challenger | PASS | PHASE 2 CHALLENGE puts Slot 1 = all challenger roles first; null hypothesis 4-slot form required |
| C-10 | Finding specificity: named surface | PASS | Findings schema: "names a specific artifact surface"; NOT: abstract observations; PHASE 4 validates |
| C-14 | Registry ERROR halt | PASS | L3 explicit ERROR halts; "unconditional, no soft fallback"; covers absent/empty/malformed |

**Recommended subtotal: 60/60**

### Aspirational (2.5 pts each)

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-11 | Null hypothesis structured template | PASS | 4-slot form SLOT-A/B/C/D; all filled or escalated per C4 |
| C-12 | Per-role lens-lock declaration | PASS | Lens column required; one-sentence "As a [role], I care about [concern from lens.verify]"; anti-pattern excludes restatements |
| C-13 | Typed column contracts with per-row validation | PASS | Output schema table before execution; PHASE 4 validates all 6 cells before write |
| C-15 | Challenger bracket as named execution phase | PASS | PHASE 2 -- CHALLENGE at same heading level as PHASE 3 -- REVIEW |
| C-16 | Slot-level failure escalation | PASS | C4 escalation rule: each unfilled slot -> dedicated HIGH row; per-slot cardinality |
| C-17 | Challenger phase gate: formal exit condition | PASS | "Domain review does not begin until G1 transitions to CLOSED" explicit blocking statement |
| C-18 | Empty-slot escalation as separate matrix row | PASS | C4: "separate, dedicated matrix row"; "Do not embed..."; "Do not append..." |
| C-19 | Anti-pattern exclusion in typed column constraints | PASS | Lens, Findings, Slot, Severity, Recommendation, Role all carry NOT: exclusions |
| C-20 | Multi-condition gate closure with named states | PASS | G1 OPEN/CLOSED states; 4-condition closure predicate |
| C-21 | Anti-pattern exclusion in escalation rules | PASS | C4 names prohibited forms: "Do not embed as a sentence within...Findings cell"; "Do not append as a note" |
| C-22 | Slot-anchored matrix with numbered cross-references | PASS | Slot column present; R3 synthesis uses "Slot [N] converged/conflicts/is unique"; AMEND uses slot numbers |
| C-23 | Validation as named discrete execution phase | PASS | PHASE 4 -- VALIDATE at same heading level as PHASE 2 and PHASE 3 |
| C-24 | Criterion-check table embedded in VALIDATE phase | PASS | 17-row criterion-check table inside PHASE 4; all aspirational criteria with YES/NO/PARTIAL + evidence citations |
| C-25 | Exhaustive anti-pattern coverage across all schema columns | PASS | All 6 columns carry NOT: exclusions including Slot ("NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest") |
| C-26 | Criterion-check table is self-referentially complete | PASS | Table explicitly includes C-26, C-27, C-28 rows; "A table that stops at C-25 fails C-26 under v9" stated in table instructions |
| C-27 | Per-slot synthesis coverage contract | PASS | R3 text: "For every slot in the manifest...state exactly one of...Every slot must receive a verdict before synthesis is complete." Explicit per-slot contract replaces minimum-count from R9 |
| C-28 | VALIDATE phase criterion-failure remediation loop | PASS | 5-column table with "Remediation if NO" column; every row carries a specific return-to-phase instruction (e.g., C-27 row: "Return to PHASE 5 R3; write exactly one of 'Slot [N] converged...', 'conflicts with...', or 'is unique: ...' for each slot without a verdict") |

**Aspirational subtotal: 42.5/42.5**

**V-01 Total: 60 + 60 + 42.5 = 162.5/162.5**

---

## V-02 -- Output format (V-02 R9 + extended table)

**Design**: V-02 R9 per-slot R3 contract + criterion-check table extended to C-28 with 5-column format.

### Essential: PASS all 5 (60/60) -- same mechanisms as V-01
### Recommended: PASS all 6 (60/60) -- same mechanisms as V-01

### Aspirational

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-11 through C-25 | All | PASS | Identical mechanisms to V-01: 4-slot form, Lens column, PHASE 4 VALIDATE, G1 gate, all schema anti-patterns |
| C-26 | Self-referential completeness | PASS | Table instruction: "A table that stops at C-25 fails C-26 under v9"; C-26, C-27, C-28 rows present |
| C-27 | Per-slot synthesis coverage | PASS | R3 text carries the same explicit per-slot coverage contract as V-01 R10; "Every slot must receive a verdict. A synthesis that names one convergence and leaves other slots without a verdict does not satisfy this contract." |
| C-28 | Criterion-failure remediation loop | PASS | 5-column table with "Remediation if NO" column; per-row remediation instructions; C-28 row includes specific "Add 'Remediation if NO' column..." instruction |

**Aspirational subtotal: 42.5/42.5**

**V-02 Total: 60 + 60 + 42.5 = 162.5/162.5**

---

## V-03 -- Lifecycle variant (PHASE 3.5 SYNTHESIZE + Gate G2)

**Design**: New PHASE 3.5 -- SYNTHESIZE with G2 closure gate. Synthesis is a lifecycle phase, not a render step.

### Essential: PASS all 5 (60/60) -- same core mechanisms
### Recommended: PASS all 6 (60/60) -- same core mechanisms

### Aspirational

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-11 through C-25 | All | PASS | Same structural mechanisms; G1 gate, 4-slot form, Lens column, PHASE 4 VALIDATE, anti-patterns |
| C-26 | Self-referential completeness | PASS | Table covers ALL aspirational criteria through v9; C-26, C-27, C-28 rows present explicitly |
| C-27 | Per-slot synthesis coverage | PASS | G2 structural gate: "PHASE 4 does not begin until G2 transitions to CLOSED"; G2 closure predicate conditions 1-4 require every slot to have exactly one verdict; R3 renders directly from G2-guaranteed output. Structurally stronger than text contract -- gate prevents non-compliant output from reaching VALIDATE. C-27 criterion-check evidence: "G2 closed with N/N slots synthesized" |
| C-28 | Criterion-failure remediation loop | PASS | 5-column table with "Remediation if NO" column; C-27 row remediation: "Return to PHASE 3.5; G2 cannot close until every slot has a verdict -- address each missing slot" -- three-part structure: criterion (C-27), section (PHASE 3.5), required state (G2 closure) |

**Aspirational subtotal: 42.5/42.5**

**V-03 Total: 60 + 60 + 42.5 = 162.5/162.5**

**C-29 signal detected**: PHASE 3.5 -- SYNTHESIZE with G2 gate is architecturally distinct from all prior variations. The pattern: synthesis as a gated lifecycle phase with formal closure predicate. C-27 becomes a gate condition (structural enforcement) rather than a render contract (verification). This is the same elevation pattern applied in prior rounds: C-09 -> C-15 (challenger leads -> named phase), C-13 -> C-23 (visible validation -> named phase). C-27 -> C-29: per-slot contract -> gate-enforced synthesis phase.

---

## V-04 -- Lifecycle + Output format (dual synthesis enforcement)

**Design**: V-01 + V-02 merged; synthesis output contract in both schema section and R3 text.

### Essential: PASS all 5 (60/60)
### Recommended: PASS all 6 (60/60)

### Aspirational

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-11 through C-25 | All | PASS | All mechanisms present; identical to V-01/V-02 |
| C-26 | Self-referential completeness | PASS | C-26, C-27, C-28 rows present in 17-row table |
| C-27 | Per-slot synthesis coverage | PASS | Dual-location obligation: schema section declares contract "binding in both this schema declaration and in PHASE 5 R3"; R3 text repeats full per-slot contract. Two independent enforcement paths; no code path reaches RENDER without encountering the per-slot obligation |
| C-28 | Criterion-failure remediation loop | PASS | 5-column table with "Remediation if NO" column; all 17 rows carry specific return-to-phase instructions |

**Aspirational subtotal: 42.5/42.5**

**V-04 Total: 60 + 60 + 42.5 = 162.5/162.5**

---

## V-05 -- Three-axis (Lifecycle + Output format + Role sequence)

**Design**: V-04 + verbatim `expertise.relevance` quotes in manifest + L5 verification step.

### Essential: PASS all 5 (60/60)

**C-01 note**: V-05 adds L5 verification step: verbatim `expertise.relevance` quote must match registry file exactly or `ERROR: [role-name] verbatim quote mismatch -- manifest invalid. Halt.` This is C-01 beyond required: not just name-check but field-content verification.

### Recommended: PASS all 6 (60/60)

**C-06 note**: Verbatim quote + "selected because" 1-sentence mapping provides explicit selection evidence; strongest C-06 evidence in series.

### Aspirational

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-11 through C-25 | All | PASS | All V-04 mechanisms present; L5 verbatim quote verification adds to C-01/C-06 but does not change aspirational pass/fail |
| C-26 | Self-referential completeness | PASS | 17-row table including C-26, C-27, C-28 |
| C-27 | Per-slot synthesis coverage | PASS | Dual-location obligation: schema section ("binding in both this schema declaration and in PHASE 5 R3") + R3 text contract -- same as V-04 |
| C-28 | Criterion-failure remediation loop | PASS | 5-column table; every row has "Remediation if NO" with specific return-to-phase instruction |

**Aspirational subtotal: 42.5/42.5**

**V-05 Total: 60 + 60 + 42.5 = 162.5/162.5**

---

## Summary Table

| Variation | Axis | Essential | Recommended | Aspirational | Total | Golden? |
|-----------|------|-----------|-------------|--------------|-------|---------|
| V-01 | Lifecycle (per-slot R3 + 5-col table) | 60/60 | 60/60 | 42.5/42.5 | **162.5** | YES |
| V-02 | Output format (V-02 R9 base + table ext) | 60/60 | 60/60 | 42.5/42.5 | **162.5** | YES |
| V-03 | Lifecycle variant (PHASE 3.5 + G2) | 60/60 | 60/60 | 42.5/42.5 | **162.5** | YES |
| V-04 | Lifecycle + Output (dual synthesis) | 60/60 | 60/60 | 42.5/42.5 | **162.5** | YES |
| V-05 | Three-axis (+ verbatim quote + L5) | 60/60 | 60/60 | 42.5/42.5 | **162.5** | YES |

All five variations achieve the v9 perfect score. All essential criteria pass across all variations. The three R9 gaps (C-27 PARTIAL in V-01, C-26/C-28 FAIL in V-02) are closed by design in every R10 variation.

---

## Rank

All tied at 162.5. Within-rank ordering by structural depth and C-29 signal strength:

1. **V-05** -- three patterns coexist cleanly; verbatim quote + L5 verification is a new falsifiable selection chain pattern; strongest overall design
2. **V-04** -- dual-location synthesis obligation eliminates C-27 failure probability; simplest two-path design
3. **V-03** -- novel gate architecture (PHASE 3.5 + G2) is the strongest C-29 candidate; changes the fundamental nature of C-27 enforcement from verification to structural prevention
4. **V-01** -- clean direct triple-close; the single most targeted fix
5. **V-02** -- alternative base with same result; equivalent to V-01 from a different R9 starting point

---

## Excellence Signals

Patterns from the top-scoring variations that elevated R10 to 162.5:

**Pattern 1: 5-column criterion-check table with structural "Remediation if NO" column** (all R10 variations)
The remediation is a named structural column, not a footer instruction or a free-form note appended to the table. Every row carries a specific return-to-phase instruction. C-28 is satisfied at design level -- the table is not a static audit but a self-correcting execution loop by construction.

**Pattern 2: R3 per-slot coverage contract replacing minimum-count** (V-01, V-02, V-04, V-05)
Replacing "name at least one convergence or conflict" with "for every slot...state exactly one of...every slot must receive a verdict" closes the C-27 PARTIAL gap that persisted in V-01 R9. The force-function route (table-driven remediation) was not sufficient because the minimum-count R3 text remained technically present even when the table's C-27 row had been satisfied.

**Pattern 3: Dual-location synthesis obligation** (V-04, V-05)
Declaring the per-slot coverage contract in both the schema section AND in R3 text creates two independent enforcement paths. Neither schema-section-only nor R3-text-only has a code path that bypasses the obligation. This is the C-27 analog of how C-25 extended C-19: C-19 requires at least one column to carry an anti-pattern; C-25 requires exhaustive coverage. Dual-location synthesis is "exhaustive enforcement path coverage."

**Pattern 4: Synthesis as gate-enforced lifecycle phase (C-29 candidate)** (V-03 only)
PHASE 3.5 -- SYNTHESIZE with Gate G2 changes the architectural category of C-27 enforcement from *verification* (text contract checked in criterion-check table) to *prevention* (gate blocks VALIDATE from running until synthesis is complete). This mirrors the R2 elevation from C-09 (challenger leads) to C-15 (challenger as named phase) and the R6 elevation from C-13 (visible validation) to C-23 (validation as named phase). C-29 candidate: synthesis isolation as a gated lifecycle phase.

**Pattern 5: Verbatim expertise.relevance quote with L5 registry verification** (V-05 only)
Manifest entries for non-challenger slots must include the verbatim `expertise.relevance` text from the role file. L5 verifies the quote matches exactly before execution proceeds. This creates a falsifiable selection chain: role selection evidence is no longer a summary or paraphrase but a direct registry citation. Potential C-29/C-30 candidate: verbatim field citation as selection evidence proof.

---

```json
{"top_score": 162.5, "all_essential_pass": true, "new_patterns": ["5-column criterion-check table with structural Remediation-if-NO column satisfies C-28 at design level rather than via footer instruction", "dual-location synthesis obligation in schema section and R3 text eliminates C-27 failure probability via two independent enforcement paths", "PHASE 3.5 SYNTHESIZE with Gate G2 converts C-27 from verification contract to structural gate-enforced lifecycle phase -- C-29 candidate", "verbatim expertise.relevance quote in manifest with L5 registry verification creates falsifiable selection chain -- potential C-30 candidate"]}
```
