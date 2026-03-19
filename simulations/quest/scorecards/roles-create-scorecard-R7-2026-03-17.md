---

# roles-create R7 -- Scorecard

**Rubric version:** v6 | **Scoring:** `5 Essential @ 12pt + 2 Recommended @ 15pt + 14 Aspirational @ 0.714pt`

---

## Per-Criterion Results

### Essential + Recommended: all PASS across all variations (baseline inherited from R6 V-05)

### Aspirational: C-08 through C-17 all PASS across all variations

---

### C-18 / C-19 / C-20 / C-21 — the R7 discrimination layer

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-18 Bidirectional tracing | **P** | **P** | **P** | **F** | P |
| C-19 Thin phases | **P** | **P** | **F** | **P** | P |
| C-20 Thin checklist items | **F** | **P** | F(auto) | **P** | P |
| C-21 Every active block declared | F(auto) | **F** | F(auto) | **P** | P |
| **Aspirational passed** | **12/14** | **13/14** | **11/14** | **13/14** | **14/14** |

---

### Key Evidence

**V-01 (adversarial):** Phases are thin single-line CONTRACT citations (C-19=P). Bidirectional annotation intact (C-18=P). But AUDIT-CHECKLIST criterion B enumerates every field name, register rule, and anti-pattern in ~92 words — restating the CONTRACT: FIELD-REGISTER content verbatim in the declaration layer. Items C, D, E, F, G similarly fat. C-20=**FAIL**. C-21 auto-fails via prerequisite.

**V-02 (missing block):** All checklist items thin (C-20=P). Bidirectional intact (C-18=P). But item F (COLUMN-HEADER) is absent from the pre-declaration. Phase 4 cites `Apply CONTRACT: COLUMN-HEADER` and Gate 4b [F] fires — but no declaration item pre-announced it. C-21=**FAIL**. Demonstrates that thin format ≠ complete coverage.

**V-03 (cascade):** Phase 3 and 4 restate CONTRACT rules inline after citing them. C-19=**FAIL** → C-20 and C-21 auto-fail via prerequisite chain. C-18 survives (bidirectional annotation is independent).

**V-04 (forward-only):** All phases thin, all checklist items thin, all active blocks declared. But gates use bare labels (`Gate 0`, `Gate 3a`) with no `[letter]` suffixes — backward direction absent. C-18=**FAIL** only.

**V-05 (ceiling):** AUDIT-CHECKLIST header explicitly states "Items name the CONTRACT block and validation scope only -- no rule enumeration." All 8 items thin. Item F present. Full bidirectional annotation. All 14 aspirational criteria pass.

---

## Composite Scores

| Variation | Score |
|-----------|-------|
| V-05 Full-Seven-Criteria | **100** |
| V-02 Thin+Bidi+MissingBlock | **99.29** |
| V-04 ForwardOnly+Thin+Complete | **99.29** |
| V-01 Thin+Bidi+FatChecklist | **98.57** |
| V-03 FatPhases+Bidi | **97.86** |

**Rubric separation confirmed:** V-02 and V-04 tie at 99.29 (C-21 and C-18 equally weighted). V-01 at 98.57 (C-20 auto-costs C-21 = two criteria). V-03 at 97.86 (C-19 cascade = three criteria). V-05 sole 100.

---

## Excellence Signals from V-05

1. **Three-location rule:** each invariant lives in exactly three places — CONTRACT block (defined), phase step (cited), audit item (referenced by name). Nowhere else.
2. **Complete pre-declaration:** every CONTRACT block cited by a content-producing phase has at least one AUDIT-CHECKLIST item. No unannounced gates.
3. **C-20 and C-21 are orthogonal:** thin item format (C-20) and complete item inventory (C-21) require distinct structural commitments — satisfying one does not imply the other.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["thin declaration layer -- each AUDIT-CHECKLIST item names the CONTRACT block and validation scope only; no rule content in the declaration; invariant appears in exactly three locations: CONTRACT block (defined), phase step (cited), audit item (referenced by name)", "complete pre-declaration coverage -- every CONTRACT block cited by a content-producing phase must have at least one AUDIT-CHECKLIST item; a check that fires without pre-declaration is an unannounced gate (C-21 fail)", "C-20 and C-21 are independently satisfiable -- thin format (C-20) and complete inventory (C-21) require distinct structural commitments; passing one does not imply the other"]}
```
block.

| Variation | Phase 3 structure | Phase 4 structure | Verdict |
|-----------|------------------|------------------|---------|
| V-01 | `Apply CONTRACT: FIELD-REGISTER.` only -- no inline restatement | `Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.` only | **PASS** |
| V-02 | `Apply CONTRACT: FIELD-REGISTER.` only | `Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.` only | **PASS** |
| V-03 | `Apply CONTRACT: FIELD-REGISTER.` THEN "Field-by-field guidance (from CONTRACT: FIELD-REGISTER, restated here for execution clarity):" + full inline archetype/frame/serves/lens rules with GOOD/BAD examples | `Apply CONTRACT: COLUMN-HEADER for table column headers.` THEN full FAIL/PASS examples and generic-header rule restated inline | **FAIL** |
| V-04 | `Apply CONTRACT: FIELD-REGISTER.` only | `Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.` only | **PASS** |
| V-05 | `Apply CONTRACT: FIELD-REGISTER.` only | `Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.` only | **PASS** |

**V-03 evidence:** Phase 3 announces "Field-by-field guidance (from CONTRACT: FIELD-REGISTER, restated here for execution clarity):" then reproduces each field rule with GOOD/BAD examples -- identical to the CONTRACT block content. Phase 4 similarly restates all FAIL/PASS column header examples and the generic-header rule inline. C-19 requires the phase step to be a single-line citation. V-03 fails; the cascade pulls C-20 and C-21 down automatically.

---

#### C-20: AUDIT-CHECKLIST items are thin CONTRACT references, not rule enumerations

Pass condition: each AUDIT-CHECKLIST criterion entry names the CONTRACT block and validation scope only -- no reproduction of rules within that block.

| Variation | Criterion B format | Other items | Verdict |
|-----------|-------------------|-------------|---------|
| V-01 | **Fat:** "Frontmatter fields: name, version, archetype (checked against existing roles in the area -- `craft` for technical/builder areas, `process` for governance/ops areas), orientation.frame (first-person observational, not starting 'This role...' or third-person), orientation.serves (names a specific beneficiary, not 'Serves the team' or self-description), lens.verify (min 4 boolean items each naming a specific artifact/state/config answerable yes/no), lens.simplify, expertise.depth (domain-specific, not genre description), expertise.relevance, scope, collaborates_with, artifacts, workflow" -- C, D, E, F, G also enumerate specific rules | Fat throughout | **FAIL** |
| V-02 | Thin: "FIELD-REGISTER compliance -- frontmatter field completeness" | C="FIELD-REGISTER compliance -- orientation.frame register", D="FIELD-REGISTER compliance -- orientation.serves beneficiary naming", E="FIELD-REGISTER compliance -- lens.verify sharpness and count", G="INPUT-ROUTING-RULES compliance -- input classification and resolution", H="INERTIA-ADVOCATE-TEMPLATE compliance -- companion file completeness" | Thin throughout | **PASS** |
| V-03 | Thin: "FIELD-REGISTER compliance -- frontmatter field completeness" | Thin throughout | **FAIL** (auto from C-19=F) |
| V-04 | Thin: "FIELD-REGISTER compliance -- frontmatter field completeness" | Thin throughout | **PASS** |
| V-05 | Thin: "FIELD-REGISTER compliance -- frontmatter field completeness" | Thin throughout; header explicitly states "Items name the CONTRACT block and validation scope only -- no rule enumeration" | **PASS** |

**V-01 evidence (primary adversarial):** Criterion B is ~92 words enumerating every field name, archetype tier mapping rule, register constraint, anti-pattern condition, and item-count minimum -- restating the entire CONTRACT: FIELD-REGISTER content in the declaration layer. Items C, D, E, F, G similarly enumerate specific rules inline rather than naming the CONTRACT block and scope. The no-restatement principle is satisfied at the execution layer (phases are thin, C-19=P) but violated at the declaration layer. C-20 = FAIL. This is the primary R7 adversarial target: bidirectional tracing and thin phases together do not prevent fat declaration items.

**V-03 auto-fail:** C-20 implies C-19 (prerequisite). Since C-19 = F for V-03, C-20 is auto-fail regardless of actual checklist item format.

---

#### C-21: Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item

Pass condition: every CONTRACT block cited by a content-producing phase has at least one corresponding item in the pre-declared AUDIT-CHECKLIST. C-21 implies C-20; if C-20 fails, C-21 auto-fails.

| Variation | Item F in checklist | Phase 4 cites COLUMN-HEADER | Verdict |
|-----------|--------------------|-----------------------------|---------|
| V-01 | YES (fat item F present) | YES (Gate 4b [F]) | **FAIL** (auto from C-20=F) |
| V-02 | **NO** -- AUDIT-CHECKLIST has items A, B, C, D, E, G, H; item F structurally absent; variation notes: "*CONTRACT: COLUMN-HEADER is cited in Phase 4 and gated at Gate 4b [F], but no checklist item declares it.*" | YES (Gate 4b [F]) | **FAIL** |
| V-03 | YES (item F: "COLUMN-HEADER compliance -- body table column headers") | YES (Gate 4b [F]) | **FAIL** (auto from C-20=F) |
| V-04 | YES (item F: "COLUMN-HEADER compliance -- body table column headers") | YES (Gate 4b) | **PASS** |
| V-05 | YES (item F: "COLUMN-HEADER compliance -- body table column headers") | YES (Gate 4b [F]) | **PASS** |

**V-02 evidence (C-21 single-axis failure):** All present checklist items are thin and correctly formatted (C-20=P). But item F is absent from the pre-declaration. Phase 4 cites `Apply CONTRACT: COLUMN-HEADER` and Gate 4b [F] fires in execution. The gate has a `[letter]` suffix -- but there is no declaration item for it to cite back to. The COLUMN-HEADER check is active and executes but was never announced. An unannounced gate = C-21 fail. Demonstrates that C-20 and C-21 are independently satisfiable: thin format alone does not guarantee complete coverage.

---

### Full Aspirational Summary

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-08 | P | P | P | P | P |
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | P | P |
| C-18 | **P** | **P** | **P** | **F** | P |
| C-19 | **P** | **P** | **F** | **P** | P |
| C-20 | **F** | **P** | F(auto) | **P** | P |
| C-21 | F(auto) | **F** | F(auto) | **P** | P |
| **Passed** | **12/14** | **13/14** | **11/14** | **13/14** | **14/14** |

---

## Composite Scores

| Variation | Essential (max 60) | Recommended (max 30) | Aspirational (max 10) | Composite |
|-----------|-------------------|---------------------|----------------------|-----------|
| V-01 Thin+Bidi+FatChecklist | 5/5 x 60 = **60** | 2/2 x 30 = **30** | 12/14 x 10 = **8.57** | **98.57** |
| V-02 Thin+Bidi+MissingBlock | 5/5 x 60 = **60** | 2/2 x 30 = **30** | 13/14 x 10 = **9.29** | **99.29** |
| V-03 FatPhases+Bidi | 5/5 x 60 = **60** | 2/2 x 30 = **30** | 11/14 x 10 = **7.86** | **97.86** |
| V-04 ForwardOnly+Thin+Complete | 5/5 x 60 = **60** | 2/2 x 30 = **30** | 13/14 x 10 = **9.29** | **99.29** |
| V-05 Full-Seven-Criteria | 5/5 x 60 = **60** | 2/2 x 30 = **30** | 14/14 x 10 = **10.00** | **100** |

---

## Rankings

| Rank | Variation | Score | Delta | Failing Criteria |
|------|-----------|-------|-------|-----------------|
| 1 | V-05 Full-Seven-Criteria | **100** | -- | none |
| 2 | V-02 Thin+Bidi+MissingBlock | **99.29** | -0.71 | C-21 |
| 2 | V-04 ForwardOnly+Thin+Complete | **99.29** | -0.71 | C-18 |
| 4 | V-01 Thin+Bidi+FatChecklist | **98.57** | -1.43 | C-20 + C-21(auto) |
| 5 | V-03 FatPhases+Bidi | **97.86** | -2.14 | C-19 + C-20(auto) + C-21(auto) |

**Rubric separation check passed:**
- V-02 and V-04 tie at 99.29 -- confirms C-21 and C-18 are equally weighted single-criterion failures (0.71pt each).
- V-01 at 98.57 is lower than both -- C-20 failure auto-costs C-21 as well; two criteria for one structural defect (1.43pt).
- V-03 at 97.86 is lowest -- C-19 cascade costs three criteria (C-19 + C-20 auto + C-21 auto = 2.14pt).
- V-05 is the sole 100.

**Key R7 finding confirmed:** C-20 and C-21 are orthogonal. Thin checklist item format (C-20) is necessary but not sufficient for C-21 -- a skill with perfectly thin items still fails C-21 if it omits one phase-cited CONTRACT block (V-02). C-18 and C-21 fail independently at the same score cost (V-04 and V-02 tie), confirming they measure distinct structural commitments.

---

## Excellence Signals from V-05

**Three patterns that make V-05 the sole ceiling under v6:**

1. **Thin declaration layer -- CONTRACT block name + scope only.** Each AUDIT-CHECKLIST item names the CONTRACT block and validation scope only: "FIELD-REGISTER compliance -- frontmatter field completeness." No rule content appears in the declaration. Each invariant lives in exactly three locations: defined in the CONTRACT block, cited in the phase step, referenced by name in the audit item. V-05 makes this explicit in the checklist header: "Items name the CONTRACT block and validation scope only -- no rule enumeration."

2. **Complete pre-declaration coverage -- every active block announced.** Every CONTRACT block cited by a content-producing phase (FIELD-REGISTER at Phase 3, COLUMN-HEADER at Phase 4, INPUT-ROUTING-RULES at Phase 0, INERTIA-ADVOCATE-TEMPLATE at Phase 2) has at least one corresponding AUDIT-CHECKLIST item (B/C/D/E, F, G, H respectively). No check fires without first being declared. The pre-declared obligation set is a superset of all active checks -- no unannounced gates.

3. **C-20 and C-21 are independently satisfiable.** V-01 shows thin execution phases do not prevent fat declaration items (C-20 fails despite C-18+C-19 passing). V-02 shows thin declaration items do not guarantee complete coverage (C-21 fails despite C-20 passing). V-05 satisfies both through distinct structural commitments: thin item format (C-20) and complete item inventory (C-21). Each requires its own discipline.

---

## Score History (updated through R7)

| Variation axis | v2(R3) | v3(R4) | v4(R5) | v5(R6 act.) | v6(R7 act.) | C-20 | C-21 |
|----------------|--------|--------|--------|-------------|-------------|------|------|
| Fat Phases + Bidirectional (-> V-03 R7) | 100 | 100 | 98 | 99.17 | 97.86 | F(auto) | F(auto) |
| Decl-to-Gate / Missing coverage (-> V-02 R7) | 100 | 100 | 98 | 99.17 | 99.29 | P | **F** |
| Fat Checklist adversarial (new R7 V-01) | -- | -- | -- | -- | 98.57 | **F** | F(auto) |
| Forward-Only annotation (new R7 V-04) | -- | -- | -- | -- | 99.29 | P | P |
| Full-criteria ceiling (V-05 all rounds) | 100 | 100 | 100 | 100 | **100** | P | P |

_Each round adds one discriminating layer. R7 adds C-20 (declaration-layer thin items) and C-21 (active-block coverage completeness). The cascade structure (C-21 implies C-20 implies C-19) means a single execution-layer defect still costs three criteria. Declaration-layer defects (C-20, C-21) cost independently of each other and of C-18._

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["thin declaration layer -- each AUDIT-CHECKLIST item names the CONTRACT block and validation scope only; no rule content in the declaration; invariant appears in exactly three locations: CONTRACT block (defined), phase step (cited), audit item (referenced by name)", "complete pre-declaration coverage -- every CONTRACT block cited by a content-producing phase must have at least one AUDIT-CHECKLIST item; a check that fires without pre-declaration is an unannounced gate (C-21 fail)", "C-20 and C-21 are independently satisfiable -- thin format (C-20) and complete inventory (C-21) require distinct structural commitments; passing one does not imply the other"]}
```
