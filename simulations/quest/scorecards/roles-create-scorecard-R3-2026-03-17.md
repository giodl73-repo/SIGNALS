## roles-create R3 — Scoring

**Rubric:** v2 | **Round:** R3 | **Top score:** 100

---

### Per-Variation Scores

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Score |
|----|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |

**R3 confirmed the rubric ceiling hypothesis.** All five variations score 100 on v2. The three mechanics from R2 V-05 (named-prohibition HOLD + fill-in companion template + FAIL/PASS column header contract) are stable enough that every R3 architectural variation inherits them cleanly.

---

### R2 → R3 Delta

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| R2 v2 score | 98 | 98 | 99 | 98 | 100 |
| R3 v2 score | 100 | 100 | 100 | 100 | 100 |
| Delta | +2 | +2 | +1 | +2 | 0 |

V-01/V-02/V-04 each close their last R2 PARTIAL criterion. V-03 closes C-10 (FAIL/PASS table added). V-05 stable at 100.

---

### Rankings (by architectural robustness, not score)

| Rank | Variation | Score | Why |
|------|-----------|-------|-----|
| 1 | **V-03: Pre-Write Audit** | 100 | Fix-in-place loop. Every rubric criterion mapped to an explicit YES/NO gate before writing. Audit item [H] verifies companion file fields. Audit item [G] retroactively confirms Phase 1 HOLD. Store-then-write: no file exists until post-audit. |
| 2 | **V-05: Separation-of-Contracts** | 100 | Contracts independently consultable at any phase. "Categorical prohibitions, not preferences" is uniquely strong framing for C-12. Third FAIL example in COLUMN HEADER. Archetype anti-pattern explicitly named. |
| 3 | **V-02: Template-First** | 100 | Both output file shapes established before execution instructions. Reduces late-phase field omission risk under token pressure. |
| 4 | **V-04: Ambiguous-Input Routing** | 100 | Only variation with explicit INVALID path for malformed inputs. Prevents C-01/C-03 failures outside the three clean modes. |
| 5 | **V-01: Constraint-Minimal** | 100 | Shortest prompt. Proves mechanics alone satisfy v2. Highest adversarial risk: no Good/Bad examples for novel domains. |

---

### Excellence Signals (R3)

1. **Pre-write self-certification phase (V-03)** — A mandatory audit phase between generation and write converts AMEND from post-hoc correction into pre-commit validation. Every criterion gets an explicit YES/NO. If NO, fix before writing. The file on disk is always the post-audit version. No wrong file exists to amend — only a draft that is fixed before it becomes a file. Candidate for v3 required structure.

2. **Categorical prohibitions framing (V-05)** — "These are categorical prohibitions, not preferences." No other variation in any round uses this framing. Positive instructions ("wait for all three") leave room for rationalization. Named prohibitions close that path. Categorical framing closes it further by denying preference status entirely. Should propagate to any prompt where a constraint must be unconditional.

3. **Explicit invalid-input routing phase (V-04)** — Three clean modes don't cover the full input space. A pre-detection phase with deterministic rules for BARE AREA, EXTRA COLONS, VAGUE PHRASE, and EMPTY prevents silent misclassification. Not tested by v2, but a real production failure path. The rubric needs adversarial input cases to discriminate among v3 variations.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-write self-certification phase: mandatory YES/NO audit against each rubric criterion before writing converts AMEND from post-hoc correction into pre-commit fix-in-place validation -- the file on disk is always the post-audit version", "categorical prohibitions framing: labeling hard constraints as 'categorical prohibitions, not preferences' is the strongest register for behavioral rules -- closes rationalization space that positive wait-instructions leave open", "explicit invalid-input routing phase: a dedicated phase before mode detection with deterministic rules for malformed inputs (bare area, extra colons, vague phrases, empty) prevents C-01/C-03 failures on inputs outside the three clean modes"]}
```
 REFERENCE block before any execution instruction.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Step 4 writes in order: `.roles/{area}/inertia-advocate.md` (if generated in Step 2) then `.roles/{area}/{subrole}.md`. Paths explicit. |
| C-02 | All required frontmatter fields present | PASS | 12 | Template B in REFERENCE block contains all 12 fields with register annotations. Model sees complete output shape before reading any execution instruction. |
| C-03 | Mode detection routes correctly | PASS | 12 | Step 1 three-mode gate. INTERACTIVE: "Do not generate any content after receiving only one or two answers" / "Do not produce a draft, stub, or partial frontmatter mid-conversation" / "Proceed only when all three are confirmed." |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Template B: "Every {placeholder} must be replaced with content specific to the named domain. Verify: no placeholder text remains in the written output." Step 3 reinforces. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Step 2 ABSENT: generates Template A (complete fill-in with all fields), announces "No inertia-advocate in '{area}' -- generating companion file first." |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Template B: "boolean check naming a specific artifact, state, or config; min 4." Register annotation in each slot. |
| C-07 | Body includes domain specializations table | PASS | 15 | Template B body section includes domain specializations table with domain-named column header guidance and FAIL/PASS examples. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | Template B: "check existing roles in the area first; use their archetype." Step 3 references Template B. Check-existing instruction survives template-first reordering. |
| C-09 | Orientation register matches audience | PASS | 2 | Template B: frame = "first-person observational: how this role perceives its domain"; serves = "third-person recipient -- who benefits; must name a beneficiary, not describe the role itself." Register distinction from template position: model sees it before executing Step 3. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | Template B body: "domain-named column headers -- not 'Entity / Purpose'" + five PASS examples + "Generic headers (Entity, Item, Area, Purpose, Description, Notes, Impact) = FAIL." Strong. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Template A is a complete fill-in with all 12 frontmatter fields, {area} slots throughout, and body section including displacement cost table. Template-first position means the model encounters the full shape before any execution step. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | Step 1 INTERACTIVE: three named prohibitions matching the R2 V-05 pattern. Categorical. |
| **Total** | | | **100** | All 5 essential: PASS |

Architectural note: Template-first may be most robust under token pressure -- both output file shapes are established in working context before any behavioral instruction is processed.

---

#### V-03: Pre-Write Audit

Axis: Phase 6 mandatory self-check (8 audit items, one per rubric dimension) inserted before writing.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 7 writes correct paths. Audit item [A]: "Does `.roles/{area}/{subrole}.md` exist as the output path? (not current dir, not simulations/)" -- path compliance is an explicit pre-write checkpoint. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 template + audit item [B]: "Does the main role frontmatter contain all 12 fields: name, version, archetype, orientation.frame, orientation.serves, lens.verify (list), lens.simplify (list), expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, workflow?" All 12 named. Fix-in-place if NO. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1 three-mode gate with three named prohibitions. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Phase 3 field annotations. Audit items [C][D][E] explicitly verify domain specificity of frame, serves, and verify items against register requirements before writing. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 generates complete companion file (store-then-write pattern). Audit item [H] verifies it. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Phase 3: "4+ boolean checks; each names a specific artifact, state, config, or command; each answerable yes/no." Audit item [E]: "Does each lens.verify item reference a specific artifact, state, or config (not 'Check X' or 'Review Y' without concrete conditions)?" Fix-in-place if NO. |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4 requires domain table with FAIL/PASS examples. Audit item [F] covers column header compliance (which implies table presence). |
| C-08 | Archetype calibrated to area tier | PASS | 2 | Phase 3: "check existing roles in {area}; match their archetype value" + craft/process categorization with area examples. Audit item [B] includes archetype in the 12-field check, confirming it was set. |
| C-09 | Orientation register matches audience | PASS | 2 | Phase 3 annotations for frame/serves. Audit items [C] and [D] are explicit YES/NO checks: [C] "Is orientation.frame written in first-person observational register (not 'This role monitors...' or 'Reviews X for the team.')?"; [D] "Does orientation.serves name a specific beneficiary (not 'Serves the team' or a self-description of the role)?" Fix-in-place before write. Strongest C-09 enforcement of all R3 variations. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | Phase 4 FAIL/PASS table. Audit item [F]: "Do the domain specializations table column headers use domain vocabulary (not 'Entity', 'Item', 'Purpose', 'Description', 'Notes')?" Fix-in-place if NO. Pre-write enforcement is architecturally stronger than AMEND-only correction. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Phase 2 complete template with store-then-write. Audit item [H]: "If inertia-advocate was generated: does its file include all 12 required frontmatter fields with {area} values substituted (not literal {area})?" Only variation that audits the companion file's field completeness explicitly before writing. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | Phase 1 three named prohibitions. Audit item [G]: "If interactive mode: were all three inputs (area, subrole, orientation seed) confirmed before any content was generated?" Audit retroactively verifies the hold was honored -- catches cases where Phase 1 was bypassed. |
| **Total** | | | **100** | All 5 essential: PASS |

Architectural note: Only variation with an explicit fix-in-place loop. Every rubric criterion has a corresponding audit gate. Audit item [H] audits companion file field completeness. Audit item [G] catches Phase 1 HOLD violations retroactively. Store-then-write pattern (Phases 2-5 generate, Phase 6 audits, Phase 7 writes) means no file exists until post-audit.

---

#### V-04: Ambiguous-Input Routing

Axis: Phase 0 before mode detection handles edge-case inputs with deterministic resolution rules.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5 writes correct paths. Phase 0 EXTRA COLONS rule ("use the first two tokens only") prevents path construction from malformed input. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 template with all fields; Good/Bad examples for key fields. Complete. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 0 resolves edge cases before Phase 1 mode detection. BARE AREA -> INTERACTIVE (correct, not description). EMPTY -> INTERACTIVE (correct). EXTRA COLONS -> NAME-ONLY with first two tokens (correct, prevents silent misclassification). VAGUE PHRASE -> clarifying question rather than silent misclassification. Phase 1 then handles clean inputs cleanly. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Phase 3 Good/Bad examples per field (same quality as R2 V-04 which passed). Healthcare/backend/finance domain examples anchor each field. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 complete fill-in template. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Phase 3 Good/Bad examples: "Is PHI encrypted at rest using an approved algorithm before HIPAA Security Rule compliance review?" vs "Check audit log configuration." |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4 FAIL/PASS table with 5 domain examples. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | Phase 3: "check existing roles in {area}; match their archetype value; craft = technical/builder areas | process = governance/ops areas." Explicit check-existing instruction with tier examples. |
| C-09 | Orientation register matches audience | PASS | 2 | Phase 3 Good/Bad examples: Good "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval" vs Bad "Reviews healthcare compliance for the team." Named beneficiary examples per domain. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | Phase 4 FAIL/PASS table (identical to V-01/V-03). |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Phase 2 complete fill-in template with {area} slots. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | Phase 1 INTERACTIVE: three named prohibitions. Phase 0 routes BARE AREA and EMPTY to INTERACTIVE, ensuring the hold also triggers for under-specified inputs. |
| **Total** | | | **100** | All 5 essential: PASS |

Architectural note: Only variation that handles malformed inputs before mode detection. Phase 0 is the only explicit INVALID path among all five R3 variations. Prevents C-01 failures from misclassified input shapes that the v2 rubric does not stress-test.

---

#### V-05: Separation-of-Contracts

Axis: All behavioral contracts grouped at prompt head (INTERACTIVE HOLD, FIELD REGISTER, COLUMN HEADER, INERTIA-ADVOCATE TEMPLATE). Execution phases reference contracts by name.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5 writes in order: `.roles/{area}/inertia-advocate.md` (if generated) then `.roles/{area}/{subrole}.md`. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 template has all 12 fields. CONTRACT: FIELD REGISTER covers key fields with Good/Anti-pattern. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1: NAME-ONLY and DESCRIPTION proceed immediately. INTERACTIVE: "Apply CONTRACT: INTERACTIVE HOLD before proceeding." Contract contains all three prohibitions plus the three questions. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | CONTRACT: FIELD REGISTER provides Good example and Anti-pattern for orientation.frame, orientation.serves, lens.verify, expertise.depth, and archetype. Separately consultable throughout execution. Strongest domain-specificity guidance for fields not covered by Phase 4 examples. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2: ABSENT -> "Apply CONTRACT: INERTIA-ADVOCATE TEMPLATE. Substitute all {area} slots." Write instruction explicit. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | CONTRACT: FIELD REGISTER: lens.verify = "Boolean check naming specific artifact | 'Is the idempotency key validated server-side before the transaction commits?'" -- concrete example in contract. |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4 applies CONTRACT: COLUMN HEADER; domain table required. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | CONTRACT: FIELD REGISTER: archetype row -- "Check existing roles in the area first; use their value | Applying craft/process without checking." Anti-pattern named explicitly as "Applying craft/process without checking" -- strongest archetype guard of all R3 variations. |
| C-09 | Orientation register matches audience | PASS | 2 | CONTRACT: FIELD REGISTER has Good/Anti-pattern for both frame and serves. Frame anti-pattern: "Reviews API compliance for the team." Serves anti-pattern: "Serves the team by reviewing APIs." Register distinction is independently consultable throughout execution. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | CONTRACT: COLUMN HEADER: three FAIL rows (adds "Area / Value / Consideration" not in other variations) + five domain PASS rows + rule: "generic headers ('Entity', 'Item', 'Purpose', 'Description') = FAIL regardless of what the rows contain." Most complete FAIL taxonomy of all R3 variations. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | CONTRACT: INERTIA-ADVOCATE TEMPLATE: complete fill-in with all 12 fields, {area} slots throughout, body section. Phase 2 references contract by name. "Do not leave literal {area} in the written file." Explicit substitution guard. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | CONTRACT: INTERACTIVE HOLD: "these are categorical prohibitions, not preferences" -- only variation to frame the HOLD constraints as categorical prohibitions explicitly. Three named prohibitions; framing uniquely strong. |
| **Total** | | | **100** | All 5 essential: PASS |

Architectural note: CONTRACTS section makes every rule independently consultable at any phase without re-reading phase text. CONTRACT: COLUMN HEADER is the only one to include a third FAIL example ("Area / Value / Consideration"). "Categorical prohibitions" framing for C-12 is unique across all rounds.

---

### Rankings

Since all five variations score 100 on v2, ranking is by architectural robustness: resistance to adversarial input, token pressure, and domains outside the training examples.

| Rank | Variation | Score | Architectural Strength | Risk |
|------|-----------|-------|------------------------|------|
| 1 | **V-03: Pre-Write Audit** | **100** | Fix-in-place loop. Every rubric criterion mapped to an explicit audit gate. Audit item [H] audits companion file field completeness. Audit item [G] retroactively verifies Phase 1 HOLD. Store-then-write means no file exists until post-audit. | Added phase increases token overhead; audit items could be skimmed under extreme compression. |
| 2 | **V-05: Separation-of-Contracts** | **100** | Contracts independently consultable throughout execution. "Categorical prohibitions" framing for C-12. Third FAIL example in COLUMN HEADER. Anti-pattern "Applying craft/process without checking" for archetype. | Cross-reference structure fragments context vs inline embedding; phases are thin and could be ambiguous without the contracts. |
| 3 | **V-02: Template-First** | **100** | Both output file shapes established in context before execution instructions. Reduces late-phase field omission risk under token pressure. Good/Bad examples retained. | Template-first doesn't help if model skips back-reference under pressure; redundancy between REFERENCE section and execution steps. |
| 4 | **V-04: Ambiguous-Input Routing** | **100** | Only variation with explicit INVALID path for malformed inputs. Phase 0 prevents silent misclassification. Good/Bad examples per field. | Phase 0 adds overhead for clean inputs; VAGUE PHRASE trigger ("shorter than 6 words") may over-fire on terse natural descriptions. |
| 5 | **V-01: Constraint-Minimal** | **100** | Shortest prompt; all mechanics present. Proves mechanics alone satisfy v2. | No Good/Bad examples; novel domains rely more on model judgment. C-04/C-09 highest-risk under adversarial conditions. |

---

### Key Scoring Decisions

**All five score 100 on v2** -- R3 confirmed the rubric ceiling hypothesis. The three mechanics from R2 V-05 (named-prohibition HOLD, fill-in companion template, FAIL/PASS column header contract) are present in every R3 variation. v2 has no criterion that discriminates architectural patterns from mechanical ones.

**V-01 C-04/C-09: PASS** -- Template annotations ("FIRST-PERSON OBSERVATIONAL: not a job description", "THIRD-PERSON RECIPIENT: must not describe the role itself", "specific regulations, systems, tools, or patterns -- not genre names") are sufficient to satisfy the pass condition. The pass condition requires domain-specific content, not Good/Bad examples. The annotations prohibit generic content explicitly.

**V-03 audit items vs AMEND** -- Pre-write audit converts every rubric criterion from a post-write review item into a pre-commit YES/NO checkpoint. Does not change the v2 score (all criteria already pass) but is architecturally significant: issues that in other variations reach the file are caught and fixed before writing.

**V-04 Phase 0 routing** -- BARE AREA -> INTERACTIVE is the correct handling (not DESCRIPTION, which would silently generate a role with no subrole name). EXTRA COLONS rule ("use first two tokens") is deterministic and correct. Both prevent C-01 failure paths that v2 does not test explicitly.

**V-05 "categorical prohibitions" framing** -- No other variation in any round uses this framing. Aligns the prompt's register with what the constraint actually is. Positive instructions ("wait for all three") leave room for rationalization; named prohibitions close that; "categorical prohibitions, not preferences" closes it further by denying preference status entirely.

---

### R2 -> R3 Delta

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| R2 v2 score | 98 | 98 | 99 | 98 | 100 |
| R3 v2 score | 100 | 100 | 100 | 100 | 100 |
| Delta | +2 | +2 | +1 | +2 | 0 |

V-01/V-02/V-04 each gain +2 by closing their remaining R2 PARTIAL criteria. V-03 gains +1 (C-10 PARTIAL -> PASS via added FAIL/PASS table). V-05 was already at 100 -- stable.

---

### Excellence Signals (R3)

1. **Pre-write self-certification is a new phase archetype** (V-03): Inserting a mandatory audit phase between content generation and file write converts AMEND from post-hoc correction into pre-commit validation. Audit items map one-to-one with rubric criteria. Fix-in-place loop means the file on disk is always the post-audit version. This pattern is stronger than AMEND because it happens before the artifact exists -- no wrong file to correct, only a draft that gets fixed before it is written. Candidate for v3 required structure.

2. **Categorical prohibitions are the correct register for hard constraints** (V-05): "These are categorical prohibitions, not preferences" is the only explicit meta-label for constraint strength across all rounds. Positive instructions ("wait for all three") leave room for rationalization. Named prohibitions ("do not generate after two answers") close that path. Categorical framing closes it further by denying preference status entirely. Should be propagated to any prompt where a constraint must be unconditional.

3. **Malformed-input routing requires a phase before mode detection** (V-04): Three clean modes (NAME-ONLY, DESCRIPTION, INTERACTIVE) do not cover the full input space. A dedicated pre-detection phase with deterministic resolution rules is necessary to prevent silent misclassification. Not tested by v2 but a real production failure path. The rubric needs adversarial input cases to discriminate among variations.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-write self-certification phase: mandatory YES/NO audit against each rubric criterion before writing converts AMEND from post-hoc correction into pre-commit fix-in-place validation -- the file on disk is always the post-audit version", "categorical prohibitions framing: labeling hard constraints as 'categorical prohibitions, not preferences' is the strongest register for behavioral rules -- closes rationalization space that positive wait-instructions leave open", "explicit invalid-input routing phase: a dedicated phase before mode detection with deterministic rules for malformed inputs (bare area, extra colons, vague phrases, empty) prevents C-01/C-03 failures on inputs outside the three clean modes"]}
```
