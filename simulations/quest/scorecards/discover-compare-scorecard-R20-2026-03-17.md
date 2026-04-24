## discover-compare R20 — Scoring Results

**Rubric:** v17 | **Denominator:** /33 (full for all variations)

---

### Per-Variation Scores

| Variation | Axis | C-39 | C-40 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| **V-01** | C-39 asymmetric recall (Override uses literal) | **FAIL** | PASS | **99.70** | No |
| **V-02** | C-40 minimal BRANCH-RULE (no equivalence sets) | PASS | **PASS** | **100.00** | Yes |
| **V-03** | C-39 timing failure (declaration inside AMEND phase) | **FAIL** | PASS | **99.70** | No |
| **V-04** | C-39 form-neutral token name (`PATH-HALT`) | PASS | PASS | **100.00** | Yes |
| **V-05** | C-40 partial declaration (DEVIATION-MARKER only) | PASS | **FAIL** | **99.70** | No |

**Ranking:** V-02 = V-04 (100.00) > V-01 = V-03 = V-05 (99.70)

---

### Discrimination Results (all confirmed as projected)

- **V-01** — C-37 PASS / C-39 FAIL simultaneously confirmed. One literal path triggers "one or more paths omit token reference." Resolved-value uniformity (C-37) and encoding discipline (C-39) are orthogonal.
- **V-02** — Minimal BRANCH-RULE without equivalence sets: C-40 PASS confirmed. Equivalence set enumeration is a visibility property, not a gate condition.
- **V-03** — Declaration inside AMEND phase: C-39 FAIL despite correct token-name recall at all three paths. The two C-39 conditions (timing + recall) are independently required.
- **V-04** — `PATH-HALT` token name: C-39 PASS confirmed. The rubric's "e.g., AMEND-HALT" is illustrative; any named token satisfying declaration-before-use architecture passes.
- **V-05** — Partial BRANCH-RULE: C-38 PASS + C-40 FAIL simultaneously achievable. The two criteria are independently scored.

Zero projection errors across all five discrimination questions.

---

### Excellence Signals

1. **Minimal declaration is sufficient for C-40** — naming both elements (`[DEVIATION-MARKER] + [POSITIONAL-VOCAB]`) without enumerating equivalence sets satisfies the pairing contract. The pass gate is structural naming, not form-completeness.
2. **C-39 is form-neutral on token name** — any declared-before-AMEND token recalled consistently at all three paths passes, regardless of whether the name matches the rubric example.
3. **C-39's two conditions fail independently** — timing (before-AMEND placement) and encoding (token-name recall) are each separately required and separately detectable.
4. **C-37/C-39 discriminate orthogonal failure modes** — resolved-value uniformity and encoding discipline are independent properties; a literal value matching the token's resolved string satisfies one and fails the other.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["c39-form-neutral-token-name: any declared-before-AMEND token name satisfies C-39 architecture; rubric example is illustrative", "c40-minimal-declaration-sufficient: BRANCH-RULE naming both elements without equivalence sets satisfies C-40; equivalence sets are visibility-only", "c39-two-independent-conditions: timing (before-AMEND) and token-name recall are independently required; each detectable without the other", "c39-c37-asymmetric-recall: literal-identical-to-resolved-value satisfies C-37 (resolved uniform) but fails C-39 (encoding not token-name)", "c40-c38-partial-declaration: C-38 PASS + C-40 FAIL simultaneously achievable when declaration names only one of two required elements"]}
```
 contains only DEVIATION branch (engineering/general) -- no exec branch |
| C-31 | PASS | `DECISION MATRIX precedes RECOMMENDATION` -- positionally descriptive vocabulary |
| C-32 | PASS | `ROUTING: deviation from BODY ORDER only` -- scope declaration present |
| C-33 | PASS | `BODY-ORDER-LAYER: active` token present as standalone declaration |
| C-34 | PASS | Mini-ledger in fenced-code block form -- separable from halt instruction text |
| C-35 | PASS | All three halt instructions resolve to "any of the above tokens is absent" -- positional reference language |
| C-36 | PASS | `DEVIATION: if REG = engineering or general...` -- deviation marker at branch-instruction level |
| C-37 | PASS | All three resolved halt phrases identical: "any of the above tokens is absent" (Override literal = Add-C/Weight resolved value) |
| C-38 | PASS | `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION` -- marker + positional vocab in same line |
| **C-39** | **FAIL** | Declaration present before AMEND (`AMEND-HALT: "any of the above tokens is absent"`). Add-C and Weight paths use `{AMEND-HALT}`. Override path uses literal "any of the above tokens is absent" -- not token-name recall. "Declaration present but one or more paths omit the token reference = C-39 FAIL." |
| C-40 | PASS | `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: / OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes / before / follows / after}]` -- both elements named with equivalence sets |

**Score computation:**
- Denominator: /33 (full -- AMEND-HALT declared before AMEND + BRANCH-RULE present)
- C-39: FAIL (Override path uses literal, not token-name recall)
- All others: PASS (32/33)
- Essential: 4/4 = 60.00
- Recommended: 3/3 = 30.00
- Aspirational: 32/33 x 10 = 9.70

**V-01 Composite: 99.70** | Golden: No

---

#### V-02 — C-40 minimal declaration: BRANCH-RULE without equivalence sets

**Essential Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | All four dimensions for both options covered |
| C-02 | PASS | Separate INERT-A/B with independent FAULT directives |
| C-03 | PASS | 4x4 matrix with Option 0 column |
| C-04 | PASS | Explicit recommendation slot |

**Recommended Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Build/no-build gate surfaced on dual HIGH inertia |
| C-06 | PASS | RISK-B differentiation enforced |
| C-07 | PASS | Three concrete AMEND paths |

**Aspirational Criteria:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-08 | PASS | Option 0 named column in matrix |
| C-09 | PASS | REG token declared; register-calibrated framing |
| C-10 | PASS | Matrix assembled from LEDGER GATE tokens |
| C-11 | PASS | Dual-polarity FAULT at each inertia site |
| C-12 | PASS | ANCHOR[0] in dedicated block before analysis |
| C-13 | PASS | Verbatim anchor recall + no-paraphrase mandate co-located |
| C-14 | PASS | FAULT: label co-located with TOKEN RECALL |
| C-15 | PASS | REG declared before ANCHOR[0] |
| C-16 | PASS | Blocking HALT instruction present |
| C-17 | PASS | Pure directive output |
| C-18 | PASS | Dual-polarity FAULT in single line |
| C-19 | PASS | AMEND paths self-contained with inline TOKEN RECALL + FAULT |
| C-20 | PASS | Path-scoped TOKEN RECALL -- no over-recall |
| C-21 | PASS | Dual-polarity FAULT propagates to all AMEND paths |
| C-22 | PASS | Phase structure via token positioning and dividers |
| C-23 | PASS | RECOMMENDATION before DECISION MATRIX |
| C-24 | PASS | Mini-ledger at each AMEND path |
| C-25 | PASS | BODY ORDER + deviation routing handle both registers |
| C-26 | PASS | Exec-safe body section order |
| C-27 | PASS | Routing block after LEDGER GATE |
| C-28 | PASS | BODY ORDER and routing block structurally isolated |
| C-29 | PASS | BODY ORDER unconditional directive |
| C-30 | PASS | Routing block deviation-only (no exec branch) |
| C-31 | PASS | Positional vocabulary in branch instruction |
| C-32 | PASS | `ROUTING: deviation from BODY ORDER only` scope declaration |
| C-33 | PASS | `BODY-ORDER-LAYER: active` token present |
| C-34 | PASS | Mini-ledger in separable fenced-code block form |
| C-35 | PASS | All three halt instructions use positional reference ("any of the above tokens is absent") |
| C-36 | PASS | DEVIATION: marker at branch-instruction level |
| C-37 | PASS | Identical halt phrase across all three AMEND paths |
| C-38 | PASS | Deviation marker + positional vocab paired in same directive line |
| C-39 | PASS | `AMEND-HALT: "any of the above tokens is absent"` declared before "AMEND:" header; all three paths recall `{AMEND-HALT}` -- timing met, token-name recall met at all three paths |
| **C-40** | **PASS** | `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]` -- both required elements named; equivalence sets absent. C-40 pass condition: "Declaration present and branch satisfies both named elements = pass." Equivalence set enumeration is a visibility enhancement, not a gate requirement. Routing line carries DEVIATION: + "precedes" -- both named elements satisfied. |

**Score computation:**
- Denominator: /33 (full)
- All criteria: PASS (33/33)
- Essential: 4/4 = 60.00
- Recommended: 3/3 = 30.00
- Aspirational: 33/33 x 10 = 10.00

**V-02 Composite: 100.00** | Golden: Yes (confirmed -- minimal BRANCH-RULE without equivalence sets satisfies C-40)

---

#### V-03 — C-39 declaration timing failure: AMEND-HALT inside AMEND phase

**Essential Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | All four dimensions for both options covered |
| C-02 | PASS | Separate INERT-A/B with independent FAULT directives |
| C-03 | PASS | 4x4 matrix with Option 0 column |
| C-04 | PASS | Explicit recommendation slot |

**Recommended Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Build/no-build gate on dual HIGH inertia |
| C-06 | PASS | RISK-B differentiation enforced |
| C-07 | PASS | Three concrete AMEND paths |

**Aspirational Criteria:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-08 | PASS | Option 0 named column |
| C-09 | PASS | REG token; register framing |
| C-10 | PASS | Matrix from LEDGER GATE tokens |
| C-11 | PASS | Dual-polarity FAULT at each inertia site |
| C-12 | PASS | ANCHOR[0] in dedicated pre-analysis block |
| C-13 | PASS | Verbatim recall + no-paraphrase co-located |
| C-14 | PASS | FAULT: co-located with TOKEN RECALL |
| C-15 | PASS | REG before ANCHOR[0] |
| C-16 | PASS | Blocking HALT |
| C-17 | PASS | Pure directive output |
| C-18 | PASS | Dual-polarity FAULT single line |
| C-19 | PASS | AMEND paths self-contained |
| C-20 | PASS | Path-scoped TOKEN RECALL |
| C-21 | PASS | Dual-polarity FAULT in all AMEND paths |
| C-22 | PASS | Phase structure via token positioning |
| C-23 | PASS | RECOMMENDATION before DECISION MATRIX |
| C-24 | PASS | Mini-ledger at each AMEND path |
| C-25 | PASS | BODY ORDER + deviation routing |
| C-26 | PASS | Exec-safe body order |
| C-27 | PASS | Routing block after LEDGER GATE |
| C-28 | PASS | BODY ORDER and routing block isolated |
| C-29 | PASS | BODY ORDER unconditional |
| C-30 | PASS | Routing block deviation-only |
| C-31 | PASS | Positional vocabulary in branch |
| C-32 | PASS | Deviation-only scope declaration |
| C-33 | PASS | `BODY-ORDER-LAYER: active` present |
| C-34 | PASS | Mini-ledger in separable block form |
| C-35 | PASS | All halt instructions use positional reference (via `{AMEND-HALT}` token recall resolving to "any of the above tokens is absent") |
| C-36 | PASS | DEVIATION: marker at branch level |
| C-37 | PASS | All three resolved halt phrases identical |
| C-38 | PASS | Deviation marker + positional vocab paired in same line |
| **C-39** | **FAIL** | Token recall correct at all three paths (`{AMEND-HALT}` used uniformly -- condition-2 met). Declaration line: `AMEND-HALT: "any of the above tokens is absent"` appears immediately after `AMEND:` header -- inside the AMEND phase, not before it. "Before the AMEND phase" timing condition independently required -- condition-1 failed. C-39 FAIL: timing gate unmet despite correct token-name encoding at all three paths. |
| C-40 | PASS | BRANCH-RULE with full form + equivalence sets before ROUTING block -- both elements named |

**Score computation:**
- Denominator: /33 (full -- AMEND-HALT declared + BRANCH-RULE present)
- C-39: FAIL (declaration inside AMEND phase; timing condition unmet)
- All others: PASS (32/33)
- Essential: 4/4 = 60.00
- Recommended: 3/3 = 30.00
- Aspirational: 32/33 x 10 = 9.70

**V-03 Composite: 99.70** | Golden: No

---

#### V-04 — C-39 form-neutral token name: PATH-HALT instead of AMEND-HALT

**Essential Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | All four dimensions for both options |
| C-02 | PASS | Independent INERT-A/B with dual-polarity FAULT |
| C-03 | PASS | 4x4 matrix with Option 0 column |
| C-04 | PASS | Explicit recommendation slot |

**Recommended Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Build/no-build gate on dual HIGH inertia |
| C-06 | PASS | RISK-B differentiation |
| C-07 | PASS | Three concrete AMEND paths |

**Aspirational Criteria:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-08 | PASS | Option 0 named column |
| C-09 | PASS | REG declared; register framing |
| C-10 | PASS | Matrix from LEDGER GATE tokens |
| C-11 | PASS | Dual-polarity FAULT at each inertia site |
| C-12 | PASS | ANCHOR[0] in dedicated pre-analysis block |
| C-13 | PASS | Verbatim recall + no-paraphrase co-located |
| C-14 | PASS | FAULT: co-located with TOKEN RECALL |
| C-15 | PASS | REG before ANCHOR[0] |
| C-16 | PASS | Blocking HALT |
| C-17 | PASS | Pure directive output |
| C-18 | PASS | Dual-polarity FAULT single line |
| C-19 | PASS | AMEND paths self-contained |
| C-20 | PASS | Path-scoped TOKEN RECALL -- no over-recall |
| C-21 | PASS | Dual-polarity FAULT in all AMEND paths |
| C-22 | PASS | Phase structure via token positioning |
| C-23 | PASS | RECOMMENDATION before DECISION MATRIX |
| C-24 | PASS | Mini-ledger at each AMEND path |
| C-25 | PASS | BODY ORDER + deviation routing |
| C-26 | PASS | Exec-safe body order |
| C-27 | PASS | Routing block after LEDGER GATE |
| C-28 | PASS | BODY ORDER and routing block isolated |
| C-29 | PASS | BODY ORDER unconditional |
| C-30 | PASS | Routing block deviation-only |
| C-31 | PASS | Positional vocabulary in branch instruction |
| C-32 | PASS | Deviation-only scope declaration |
| C-33 | PASS | `BODY-ORDER-LAYER: active` present |
| C-34 | PASS | Mini-ledger in separable fenced-code block form |
| C-35 | PASS | All halt instructions use positional reference via `{PATH-HALT}` recall ("any of the above tokens is absent") |
| C-36 | PASS | DEVIATION: marker at branch level |
| C-37 | PASS | All three resolved halt phrases identical |
| C-38 | PASS | Deviation marker + positional vocab paired in same line |
| C-39 | PASS | `PATH-HALT: "any of the above tokens is absent"` declared before "AMEND:" header. All three paths recall `{PATH-HALT}`. Both conditions met: timing (before AMEND) and token-name recall (all three paths). Form-neutral: rubric "e.g., AMEND-HALT" is illustrative -- any named token satisfies declaration-before-use architecture. |
| C-40 | PASS | BRANCH-RULE with full form + equivalence sets -- both elements named before ROUTING block |

**Score computation:**
- Denominator: /33 (full)
- All criteria: PASS (33/33)
- Essential: 4/4 = 60.00
- Recommended: 3/3 = 30.00
- Aspirational: 33/33 x 10 = 10.00

**V-04 Composite: 100.00** | Golden: Yes (confirmed -- alternative token name `PATH-HALT` satisfies C-39 declaration architecture)

---

#### V-05 — C-40 partial declaration: BRANCH-RULE names only DEVIATION-MARKER

**Essential Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | All four dimensions for both options |
| C-02 | PASS | Independent INERT-A/B with dual-polarity FAULT |
| C-03 | PASS | 4x4 matrix with Option 0 column |
| C-04 | PASS | Explicit recommendation slot |

**Recommended Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Build/no-build gate on dual HIGH inertia |
| C-06 | PASS | RISK-B differentiation |
| C-07 | PASS | Three concrete AMEND paths |

**Aspirational Criteria:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-08 | PASS | Option 0 named column |
| C-09 | PASS | REG declared; register framing |
| C-10 | PASS | Matrix from LEDGER GATE tokens |
| C-11 | PASS | Dual-polarity FAULT at each inertia site |
| C-12 | PASS | ANCHOR[0] in dedicated pre-analysis block |
| C-13 | PASS | Verbatim recall + no-paraphrase co-located |
| C-14 | PASS | FAULT: co-located with TOKEN RECALL |
| C-15 | PASS | REG before ANCHOR[0] |
| C-16 | PASS | Blocking HALT |
| C-17 | PASS | Pure directive output |
| C-18 | PASS | Dual-polarity FAULT single line |
| C-19 | PASS | AMEND paths self-contained |
| C-20 | PASS | Path-scoped TOKEN RECALL |
| C-21 | PASS | Dual-polarity FAULT in all AMEND paths |
| C-22 | PASS | Phase structure via token positioning |
| C-23 | PASS | RECOMMENDATION before DECISION MATRIX |
| C-24 | PASS | Mini-ledger at each AMEND path |
| C-25 | PASS | BODY ORDER + deviation routing |
| C-26 | PASS | Exec-safe body order |
| C-27 | PASS | Routing block after LEDGER GATE |
| C-28 | PASS | BODY ORDER and routing block isolated |
| C-29 | PASS | BODY ORDER unconditional |
| C-30 | PASS | Routing block deviation-only |
| C-31 | PASS | Positional vocabulary in branch instruction |
| C-32 | PASS | Deviation-only scope declaration |
| C-33 | PASS | `BODY-ORDER-LAYER: active` present |
| C-34 | PASS | Mini-ledger in separable fenced-code block form |
| C-35 | PASS | All halt instructions use positional reference (`{AMEND-HALT}` resolves to "any of the above tokens is absent") |
| C-36 | PASS | DEVIATION: marker at branch level |
| C-37 | PASS | All three halt phrases identical across AMEND paths |
| C-38 | PASS | `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION` -- both deviation marker + positional vocab present in routing line |
| C-39 | PASS | `AMEND-HALT: "any of the above tokens is absent"` declared before "AMEND:" header; all three paths recall `{AMEND-HALT}` -- both conditions met |
| **C-40** | **FAIL** | `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER]` -- POSITIONAL-VOCAB absent from declaration. C-40 requires "naming both required elements as a structural rule." Declaration names only one element; "both required elements" gate not satisfied. C-38 PASS (line-level coexistence by inspection) and C-40 FAIL (incomplete declaration) are simultaneously achievable -- independently scored criteria. |

**Score computation:**
- Denominator: /33 (full -- AMEND-HALT declared + BRANCH-RULE present even if incomplete)
- C-40: FAIL (declaration names only [DEVIATION-MARKER], not both elements)
- All others: PASS (32/33)
- Essential: 4/4 = 60.00
- Recommended: 3/3 = 30.00
- Aspirational: 32/33 x 10 = 9.70

**V-05 Composite: 99.70** | Golden: No

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 60.00 | 30.00 | 9.70 (32/33) | **99.70** | No |
| V-02 | 60.00 | 30.00 | 10.00 (33/33) | **100.00** | Yes |
| V-03 | 60.00 | 30.00 | 9.70 (32/33) | **99.70** | No |
| V-04 | 60.00 | 30.00 | 10.00 (33/33) | **100.00** | Yes |
| V-05 | 60.00 | 30.00 | 9.70 (32/33) | **99.70** | No |

**Ranking:** V-02 = V-04 (100.00) > V-01 = V-03 = V-05 (99.70)

---

### Discrimination Verification

| Discrimination Question | Expected | Confirmed |
|------------------------|----------|-----------|
| V-01: C-37 PASS when 2 paths use `{AMEND-HALT}` and 1 uses identical literal? | Yes | YES -- C-37 measures resolved-value uniformity, not encoding form |
| V-01: C-39 FAIL on single non-recall path ("one or more" clause)? | Yes | YES -- Override path literal triggers C-39 FAIL |
| V-02: Minimal BRANCH-RULE without equivalence sets satisfies C-40? | PASS | YES -- equivalence sets are visibility enhancement only, not pass gate |
| V-03: C-39 FAIL when declaration placed inside AMEND phase? | Yes | YES -- before-phase timing condition independently required |
| V-03: C-37 PASS when all three paths use `{AMEND-HALT}` recall? | Yes | YES -- resolved-value uniformity met via token recall |
| V-04: `{PATH-HALT}` alternative token name satisfies C-39? | PASS | YES -- "e.g., AMEND-HALT" in rubric is illustrative; mechanism is declaration-before-use architecture |
| V-05: C-38 PASS + C-40 FAIL simultaneously achievable? | Yes | YES -- line-level coexistence (C-38) and declaration completeness (C-40) independently scored |

All five discrimination questions confirmed as expected. Zero projection errors.

---

### Excellence Signals from Top-Scoring Variations (V-02, V-04)

**Signal 1 -- C-40 pass gate is declaration-names-both-elements, not enumeration-completeness** (V-02)
The minimal form `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]` satisfies C-40 without equivalence sets. The pass gate is structural: declare the pairing contract naming both required elements before the routing block fires. Equivalence sets (`{DEVIATION: | OVERRIDE:}`, `{precedes | before | follows | after}`) make form-neutrality visible without rubric cross-reference -- a documentation quality property, not a mechanism gate. Stripping to minimal form: C-40 PASS confirmed.

**Signal 2 -- C-39 token-name is form-neutral; declaration-before-use architecture is the gate** (V-04)
`PATH-HALT: "any of the above tokens is absent"` satisfies C-39 identically to `AMEND-HALT`. The rubric uses "e.g., AMEND-HALT" as illustrative. The actual mechanism: declare a named token before the AMEND block opens; recall it by that exact name at each path. Any valid identifier satisfies the architecture. Alternate names (`PATH-HALT`, `GATE-HALT`, etc.) are fully C-39-compliant provided they are declared before AMEND and recalled at every path.

**Signal 3 -- C-37 and C-39 are independently scored on orthogonal dimensions** (V-01 discrimination)
C-37 measures resolved-value uniformity -- same string at execution. C-39 measures encoding discipline -- declaration-before-use with token-name recall. A path using the literal value (not `{AMEND-HALT}`) satisfies C-37 (resolved string matches) while failing C-39 (token name not used). These are not redundant criteria -- they discriminate orthogonal failure modes and cannot be collapsed.

**Signal 4 -- C-39's two conditions are independently required** (V-03 discrimination)
C-39 has two independently required conditions: (1) declaration placed before the AMEND phase opens, and (2) token-name recall at each path. V-03 shows condition-2 fully met (all three paths use `{AMEND-HALT}`) while condition-1 fails (declaration placed after "AMEND:" header). The failure is architectural -- a declaration inside the AMEND phase cannot serve as a pre-phase anchor even when recall encoding is correct.

---

### New Patterns (R20 additions to watch list)

| Pattern | Rule |
|---------|------|
| `c39-form-neutral-token-name` | C-39 architecture satisfied by any named token -- `PATH-HALT`, `AMEND-HALT`, or equivalent; rubric example is illustrative; mechanism is declaration-before-use, not name conformance; confirmed R20 V-04 |
| `c40-minimal-declaration-sufficient` | BRANCH-RULE naming both elements without equivalence set enumeration satisfies C-40; equivalence sets enhance visibility but are not a gate condition; confirmed R20 V-02 |
| `c39-two-independent-conditions` | C-39 has two independently required conditions: (a) declaration before AMEND phase opens, (b) token-name recall at every path; V-03 shows condition-b met while condition-a fails -- both separately required and separately detectable |
| `c39-c37-asymmetric-recall` | When one path uses literal value (identical to resolved token value) and others use token-name recall: C-37 PASS (resolved-value uniform), C-39 FAIL (encoding not uniform); confirmed R20 V-01 |
| `c40-c38-partial-declaration` | C-38 PASS (coexistence by inspection) and C-40 FAIL (declaration names only one element) are simultaneously achievable; C-40 not co-scored with C-38; confirmed R20 V-05 |
