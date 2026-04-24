Scorecard written to `simulations/quest/scorecards/scout-inertia-scorecard-R18-2026-03-17.md`.

---

**Score Summary**

| V | R17 Base | C-55 | C-56 | R18 Score |
|---|----------|------|------|-----------|
| **V-04** | 46/46 | PASS | PASS | **10.00** |
| **V-05** | 46/46 | PASS | PASS | **10.00** |
| V-01 | 46/46 | PASS | FAIL | 9.79 |
| V-02 | 46/46 | PASS | FAIL | 9.79 |
| V-03 | 46/46 | FAIL | PASS | 9.79 |

**Top score: 10.00. All essential pass: true.**

Key finding: V-04 is the critical new result — it's a wholly different scaffold from R17 V-04 (domain-prefix vocabulary applied correctly, Q3/Q4 as standalone sections), so it carries no C-42/C-46 failures. V-03 gives C-56 in isolation for the first time, confirming lowercase artifact-name routing satisfies C-56.

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["C-55 and C-56 orthogonality experimentally verified in isolation: V-01/V-02 pass C-55 without C-56 (ordinal scaffold structurally excludes C-56); V-03 passes C-56 without C-55 (completion-action removed by design) -- neither criterion implies the other", "C-56 register-agnosticism confirmed: lowercase 'the Q3 section' (V-03) and all-caps 'THE Q3 SECTION' (V-04/V-05) satisfy C-56 identically -- criterion evaluates structural naming form (artifact-ID-as-section-reference), not case register", "C-55+C-56 combined form is register-agnostic across domain-prefix bracket-suffix register (V-04: INERTIA THREAT RULE [A-16]) and all-caps COMMAND register (V-05) -- register-agnosticism extends through the full C-53 to C-55+C-56 backward-routing chain"]}
```
nal scaffolds -- C-56 structurally unavailable, not a rubric failure.

**Register**: Register-agnostic. Lowercase `the Q3 section` (V-03) and all-caps `THE Q3 SECTION` (V-04/V-05) both satisfy.

---

### Variation-by-Variation Evaluation

---

#### V-01 -- C-55 on section-based scaffold (Section 1A/1B form)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-54 | PASS (carried) | R17 V-01 = 46/46; single change in R18 is gate body routing upgraded to completion-action form |
| **C-55** | **PASS** | `If Q3 shows N, return to Section 1A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows N, return to Section 1B (FM->TRIGGER BRIDGE) and complete the trigger mapping.` -- each clause delivers destination + class + task in a single self-contained instruction. Register lowercase; C-55 register-agnostic. |
| **C-56** | **FAIL** | Return target `Section 1A` is an ordinal label. C-56 applicability condition requires artifact-ID-based section names. V-01 primary section label is `SECTION 1A` not `Q3`. Author must mentally map `Q3 -> Section 1A`. C-56 structurally unavailable on this scaffold. |

**Score: 47/48 x 10 = 9.79**

---

#### V-02 -- C-55 on stage-based scaffold (Stage 2A/2B form)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-54 | PASS (carried) | R17 V-02 = 46/46; single change is gate body routing upgraded to completion-action form |
| **C-55** | **PASS** | `If Q3 shows N, return to Stage 2A (FM->ACTOR BRIDGE) and complete the actor mapping. If Q4 shows N, return to Stage 2B (FM->TRIGGER BRIDGE) and complete the trigger mapping.` -- structurally identical to V-01 with stage-based targets. Completion-action directive present for both artifacts. R18 minimum-viable C-55 reference. |
| **C-56** | **FAIL** | Return target `Stage 2A` is an ordinal label. Q3/Q4 are sub-sections within Stage 2, not standalone top-level sections. C-56 applicability condition not met. Structural necessity same as V-01. |

**Score: 47/48 x 10 = 9.79**

---

#### V-03 -- C-56 isolation test (artifact-name scaffold, no C-55)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | All essential templates present |
| C-34 through C-54 | PASS | Based on R17 V-05 scaffold (Q3/Q4 standalone top-level sections = 46/46 baseline). 3-segment gate heading satisfies C-50. Per-artifact `[BRIDGE Q3 COMMAND]`/`[BRIDGE Q4 COMMAND]` -> C-41 PASS. Return-target class annotations -> C-54 PASS. Bracket-label criteria carried from V-05. |
| **C-55** | **FAIL** | Gate body routing: `Return to the Q3 section (FM->ACTOR BRIDGE) if Q3 shows N; return to the Q4 section (FM->TRIGGER BRIDGE) if Q4 shows N.` -- no completion-action directive. Clause names destination + class only; author must read section heading to determine work required. C-55 isolation by design. |
| **C-56** | **PASS** | Return target `the Q3 section` uses artifact ID `Q3` as section reference. `Q3` appears in gate table row, conditional key (`if Q3 shows N`), and return target (`the Q3 section`) -- same base identifier. Q3/Q4 are standalone top-level sections whose primary label IS the artifact ID. Zero mapping overhead; applicability condition satisfied. Register lowercase; C-56 register-agnostic. |

**C-55/C-56 orthogonality confirmed in isolation**: V-03 passes C-56 without C-55. Combined with V-01/V-02 passing C-55 without C-56, R18 experimentally verifies independence.

**C-56 register-agnosticism confirmed**: lowercase `the Q3 section` satisfies C-56 identically to ALL-CAPS `THE Q3 SECTION` in V-04/V-05.

**Score: 47/48 x 10 = 9.79**

---

#### V-04 -- C-55 + C-56 combined in domain-prefix bracket-suffix register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Domain-prefix templates prescribe all five essential elements |
| C-34 | PASS | `INERTIA THREAT RULE [A-16]` at FM Inventory |
| C-35 | PASS | `INERTIA THREAT CITATION RULE [A-19]` at defeat conditions |
| C-36 | PASS | Seven distinct obligations including `INERTIA THREAT FAIL-FIRST RULE [A-31]`, `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `[BRIDGE Q3 COMMAND]`, `[BRIDGE Q4 COMMAND]`, `[BRIDGE COMPLETION COMMAND]` |
| **C-42** | **PASS** | `INERTIA THREAT FAIL-FIRST RULE [A-31]`, `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]` -- three bracket labels share `INERTIA THREAT` domain vocabulary threading |
| **C-46** | **PASS** | Compound domain-axis vocabulary: `INERTIA THREAT` (domain) + `RULE`/`CITATION RULE`/`FAIL-FIRST RULE` (structural-role axis) across three labels |
| C-41 | PASS | `[BRIDGE Q3 COMMAND]:` at Q3 section; `[BRIDGE Q4 COMMAND]:` at Q4 section -- per-artifact bracket commands at authoring points |
| C-43 through C-54 | PASS | Gate heading `BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?` satisfies C-50 (3-segment), C-43 (BOTH count), C-45 (Q3/Q4 IDs), C-49 (per-artifact class annotations). Gate body satisfies C-37, C-51, C-53, C-54 via `[BRIDGE COMPLETION COMMAND]: CONFIRM...` + annotated per-artifact routing. |
| **C-55** | **PASS** | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` -- completion-action directives present for both artifacts. Gate body form identical to R17 V-05; surrounding scaffold register differs. C-55 register-agnostic. |
| **C-56** | **PASS** | `THE Q3 SECTION` / `THE Q4 SECTION` -- artifact-name routing. Q3/Q4 are standalone top-level sections with artifact-ID primary labels. Conditional key `IF Q3 SHOWS N` and return target `THE Q3 SECTION` share base identifier `Q3`. Applicability condition satisfied. |

**Register-agnosticism of C-55+C-56 combined confirmed**: domain-prefix bracket-suffix register (V-04) and all-caps COMMAND register (V-05) produce identical scores on both new criteria. Register-agnosticism extends through the full C-53 -> C-54 -> C-55/C-56 backward-routing chain.

**Score: 48/48 x 10 = 10.00**

---

#### V-05 -- Reference form (R17 V-05 unchanged)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | All-caps COMMAND-register templates prescribe all five essential elements |
| C-34 through C-54 | PASS (carried) | R17 V-05 = 46/46; no changes in R18 -- carried as reference form |
| **C-55** | **PASS (criterion source)** | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` -- V-05 was the R16 excellence signal from which C-55 was extracted in v18. Carrying unchanged confirms criterion fidelity. |
| **C-56** | **PASS (criterion source)** | `THE Q3 SECTION` / `THE Q4 SECTION` -- artifact-name routing; R16 excellence signal from which C-56 was extracted in v18. Identifier isomorphism confirmed across gate table row, conditional key, and return target. |

**Score: 48/48 x 10 = 10.00**

---

### Composite Scores

| Variation | R17 Base | C-55 | C-56 | R18 Score | Notes |
|-----------|----------|------|------|-----------|-------|
| **V-04** | 46/46 | PASS | PASS | **48/48 = 10.00** | Domain-prefix register; C-55+C-56 combined; C-42/C-46 PASS |
| **V-05** | 46/46 | PASS | PASS | **48/48 = 10.00** | Reference form; criterion source for both C-55 and C-56 |
| V-01 | 46/46 | PASS | FAIL | 47/48 = 9.79 | Section-based ordinal scaffold; C-56 structurally unavailable |
| V-02 | 46/46 | PASS | FAIL | 47/48 = 9.79 | Stage-based ordinal scaffold; C-56 structurally unavailable |
| V-03 | 46/46 | FAIL | PASS | 47/48 = 9.79 | Artifact-name scaffold; C-56 isolation; no completion-action by design |

---

### Rankings

1. **V-04, V-05** -- 48/48 = 10.00 (tied)
2. **V-01, V-02, V-03** -- 47/48 = 9.79 (tied)

---

### C-55/C-56 Cross-Variation Analysis

| Question | Finding |
|----------|---------|
| Does C-55 require a specific verb or any task-naming directive? | Lowercase `complete` (V-01/V-02) and ALL-CAPS `COMPLETE` (V-04/V-05) both pass. C-55 register-agnostic. |
| Does C-55 require completion-action to appear after the class annotation? | All variations place task after `(FM->ACTOR BRIDGE)`. Most restrictive position interpretation uniformly satisfied. |
| Does C-56 require all-caps `THE Q3 SECTION` or is lowercase sufficient? | Lowercase (V-03) and all-caps (V-04/V-05) both pass. C-56 evaluates structural naming form, not case register. |
| Are C-55 and C-56 independently satisfiable? | Confirmed: V-01/V-02 pass C-55 without C-56; V-03 passes C-56 without C-55; V-04/V-05 pass both. Independence holds. |
| Does C-56 apply to ordinal scaffolds? | No. Ordinal scaffolds (Section 1A, Stage 2A) are outside C-56 scope by structural necessity. Applicability condition enforces this. |

---

### Excellence Signals (Top-Variation Patterns)

V-04 and V-05 tie at 10.00. No patterns from the top variations remain unformalized after v18.

**Key confirmations this round**:

1. **C-55/C-56 orthogonality experimentally verified**: Four conditions observed -- C-55 only (V-01/V-02), C-56 only (V-03), both (V-04/V-05), neither impossible by construction. Neither criterion implies the other.

2. **C-56 register-agnosticism confirmed**: Lowercase `the Q3 section` (V-03) and ALL-CAPS `THE Q3 SECTION` (V-04/V-05) satisfy C-56 identically. Register-agnosticism extends through the complete backward-routing criterion chain: C-53 (R16) -> C-54 (R17) -> C-55/C-56 (R18).

3. **C-55+C-56 combined form confirmed register-agnostic in domain-prefix register**: V-04 domain-prefix bracket-suffix notation with identical gate body form to V-05 produces the same score. Maximum-density routing clause is independent of surrounding document register.

No new unformalized excellence signals identified. v18 denominator saturation achieved at V-04/V-05 = 10.00.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["C-55 and C-56 orthogonality experimentally verified in isolation: V-01/V-02 pass C-55 without C-56 (ordinal scaffold structurally excludes C-56); V-03 passes C-56 without C-55 (completion-action removed by design) -- neither criterion implies the other", "C-56 register-agnosticism confirmed: lowercase 'the Q3 section' (V-03) and all-caps 'THE Q3 SECTION' (V-04/V-05) satisfy C-56 identically -- criterion evaluates structural naming form (artifact-ID-as-section-reference), not case register", "C-55+C-56 combined form is register-agnostic across domain-prefix bracket-suffix register (V-04: INERTIA THREAT RULE [A-16]) and all-caps COMMAND register (V-05) -- register-agnosticism extends through the full C-53 to C-55+C-56 backward-routing chain"]}
```
