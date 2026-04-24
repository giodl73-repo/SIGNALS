## roles-create R2 — Scoring

**Rubric:** v2 (12 criteria) | **Point values:** Essential 12pt each, Recommended 15pt each, Aspirational 2pt each, PARTIAL = 50%

---

### Per-Variation Scores

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Score |
|----|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | P | P | P | P | P | P | P | **P** | **P** | **P** | PA | PA | **98** |
| V-02 | P | P | P | P | P | P | P | P | P | PA | **P** | PA | **98** |
| V-03 | P | P | P | P | P | P | P | P | P | PA | P | **P** | **99** |
| V-04 | P | P | P | P | P | P | P | PA | P | P | PA | P | **98** |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | **100** |

Bold = improvement over R1 retroactive baseline. All variations Golden (all essential pass + composite ≥ 80).

---

### Rankings

| Rank | Variation | Score | Key Strength | Gap |
|------|-----------|-------|--------------|-----|
| 1 | **V-05: Full Integration v2** | **100** | All three R2 gaps mechanical: named-prohibition HOLD + fill-in template + FAIL/PASS contract | — |
| 2 | **V-03: Interactive-Hold-Protocol** | **99** | Named-prohibition HOLD (C-12 PASS); inherits V-05 R1 C-08/C-09/C-11 | C-10 PARTIAL: designer flags as risk; no FAIL/PASS table |
| 3 | **V-01/V-02/V-04** | **98** | Each fixes one axis cleanly | PARTIAL on the other two axes |

---

### Key Scoring Decisions

**V-01 C-08/C-09: PASS (upgraded from R1)** — R2 V-01 adds "check existing roles in the area; match their archetype value" and "must name a beneficiary, not describe the role itself" — neither guard was in R1 V-01. +4 over R1 retroactive.

**V-03 C-10: PARTIAL** — Single-line "domain-named column headers (not generic 'Entity / Purpose')" constraint without a FAIL/PASS table. Designer risk note explicitly flags C-10 as unchanged from R1 gap. V-03 R1 failed C-10. Scored conservatively.

**V-04 C-08: PARTIAL** — AMEND block reviews archetype post-write but no generation-time "check existing roles" instruction. Same structural gap as R1 V-04.

**C-11 PASS threshold** — Requires explicit enumeration of all 12 fields. V-03 Phase 2 lists all 12 by name → PASS. V-05 provides fill-in template → PASS. V-02/V-04 describe content but omit scope, collaborates_with, artifacts, workflow → PARTIAL.

---

### Excellence Signals (R2)

1. **Named-prohibition interactive hold** (V-03/V-05): "Do not generate after one or two answers" / "Do not produce draft mid-conversation" — categorical prohibitions, not positive instructions. V-03 and V-05 independently arrive at the same three-rule set, both pass C-12. Pattern confirmed.

2. **Fill-in template for companion file** (V-02/V-05): Complete parameterized template with `{area}` slots removes the generation decision — model fills slots instead of deciding what "complete" means. Resolves the C-11 failure mode where a convincing-looking file omits required fields.

3. **Column header FAIL/PASS contract** (V-01/V-04/V-05): Explicit domain-concrete FAIL/PASS example table makes C-10 a pre-write checkable rule. Single-line constraint (V-03) depends on inference and scores PARTIAL.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named-prohibition interactive hold: explicit 'Do not generate after one or two answers' and 'Do not produce draft mid-conversation' rules make C-12 a hard constraint — positive wait instructions leave rationalization room; named prohibitions close it", "fill-in template for companion file: complete parameterized inertia-advocate template with {area} slots eliminates the generation decision — the model fills slots instead of deciding what complete means, removing the partial-file output path", "column header FAIL/PASS contract: explicit domain-concrete FAIL and PASS example table makes C-10 a pre-write checkable rule rather than a stylistic inference from a single-line constraint"]}
```
raft/roles/{area}/inertia-advocate.md" and Step 5 write order explicit. |
| C-02 | All required frontmatter fields present | PASS | 12 | Step 3 enumerates all fields by name. Complete template in Step 2 for companion shows field shape. |
| C-03 | Mode detection routes correctly | PASS | 12 | Three modes in Step 1. "Do not generate any content until all three are answered" for interactive path. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | "Build domain-specific content for every field. No placeholder text." with per-field guidance. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Step 2 ABSENT branch: complete companion template generated. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | "4+ boolean checks; each names a specific artifact or system state." Carried from R1 V-02. |
| C-07 | Body includes domain specializations table | PASS | 15 | Step 4: "domain-named column headers (not 'Entity / Purpose')" requirement. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | "match area's established pattern; check existing roles first" — check-existing instruction present. Carried from R1 V-02. |
| C-09 | Orientation register matches audience | PASS | 2 | "receiver-directed; name the beneficiary explicitly" in Step 3. Carried from R1 V-02. |
| C-10 | Body table uses domain-named column headers | PARTIAL | 1 | Step 4: "domain-named column headers (not 'Entity / Purpose')" — one-line instruction only. Inertia companion template models domain-named headers ("Existing {area} Pattern / Dependent Roles / Migration Effort / Rollback Available") but no FAIL/PASS example table for the main role. Less mechanical than V-01/V-04/V-05. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Primary axis. Complete parameterized template in Step 2 with all 12 required fields pre-populated and {area} slots throughout. Body section with displacement cost table included. Fill-in-slots format eliminates partial-file path. |
| C-12 | Interactive mode holds for all inputs | PARTIAL | 1 | "Do not generate any content until all three are answered." Explicit but no named prohibitions. Same language as R1 V-02 which failed C-12. |
| **Total** | | | **98** | All 5 essential: PASS |

---

### V-03: Interactive-Hold-Protocol

Primary axis: C-12 (explicit HOLD with named prohibitions). Non-interactive paths stated to be "identical to V-05 R1" which passed C-08, C-09, C-11. C-10 addressed via single-line constraint (same level as V-05 R1) but designer flags as unchanged from R1 gap — scored PARTIAL.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5: write order for inertia-advocate and main role. Both paths to .roles/{area}/. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 enumerates all required fields by name with descriptions. Complete field list present. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1: three-mode gate with explicit phase output ({area}, {subrole}, {orientation seed}). |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Phase 3: "Generate domain-specific content for every field. No generic language." |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 ABSENT: "Generate a complete inertia-advocate role file with: - All required frontmatter fields: name, version, archetype, orientation (frame + serves), lens (verify + simplify), expertise (depth + relevance), scope, collaborates_with, artifacts, workflow." All 12 fields enumerated. Write instruction present. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Phase 3: "4+ boolean checks; each references a specific artifact, state, config, or command; each answerable yes/no about a real system." Identical to V-05 R1. |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4: "Domain specializations table: domain-named column headers (not generic 'Entity / Purpose')." Required element in body. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | Phase 3: "archetype -- check existing roles in {area}; match their archetype value." Check-existing instruction present. Inherited from V-05 R1 which passed C-08. |
| C-09 | Orientation register matches audience | PASS | 2 | Phase 3: "orientation.serves -- third-person recipient; name the beneficiary explicitly; must not be a self-description of the role." Beneficiary guard present. Inherited from V-05 R1 which passed C-09. |
| C-10 | Body table uses domain-named column headers | PARTIAL | 1 | Phase 4: "domain-named column headers (not generic 'Entity / Purpose')" — single-line constraint, no FAIL/PASS example table. Designer risk note explicitly flags C-10 as "unchanged from R1 gaps" for V-03. V-03 R1 failed C-10. Without the FAIL/PASS example table present in V-01/V-04/V-05, the instruction depends on model inference. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Phase 2 enumerates all 12 required frontmatter fields by name. Content guidance per key field. Body with displacement cost table and "domain-named column headers" required. Write instruction present. All 12 fields explicitly named reduces omission risk to low. Consistent with R1 V-03 which passed C-11. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | Primary axis. Phase 1 INTERACTIVE: three named prohibitions: "Do not proceed after receiving only question 1 or question 2." / "Do not generate a draft, stub, or partial role mid-conversation." / "Proceed to Phase 2 only when all three values have been received." Named prohibitions make hold a hard constraint. |
| **Total** | | | **99** | All 5 essential: PASS |

---

### V-04: Register-with-Domain-Examples

Primary axis: C-09/C-10 (conversational register + per-field domain examples + column header contract with FAIL/PASS table). Also adds interactive hold prohibition. C-08 remains PARTIAL: no archetype generation instruction, only AMEND review. C-11 addressed in prose without template or field enumeration.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | "Write the companion file to .roles/{area}/inertia-advocate.md" and main role write instruction present. |
| C-02 | All required frontmatter fields present | PASS | 12 | Conversational enumeration: "The frontmatter has: name, version ('1.0'), archetype, orientation (frame and serves), lens (verify and simplify), expertise (depth and relevance), scope, collaborates_with, artifacts, workflow." — complete list. |
| C-03 | Mode detection routes correctly | PASS | 12 | Three modes described in second-person paragraphs. Clear routing for each case. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Per-field domain-concrete examples model what specificity means: healthcare gives HIPAA/FHIR R4 examples, backend gives API contract versioning/idempotency key examples, finance gives GAAP/GL examples. Positive examples constrain more reliably than anti-generic instructions. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | "create a complete companion role file -- not a note or suggestion." Explicit prohibition against note/suggestion path. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Per-field boolean check examples: "Is PHI encrypted at rest using an approved algorithm before HIPAA Security Rule compliance review?" vs "Avoid: 'Check audit logging', 'Review security posture'." Domain-concrete good/bad examples. |
| C-07 | Body includes domain specializations table | PASS | 15 | "Body section -- column header contract" requires at least one structured table. |
| C-08 | Archetype calibrated to area tier | PARTIAL | 1 | No archetype generation instruction in conversational body. AMEND block says "Whether the archetype matches the area's established pattern, with a reason" — post-write review only. Without a generation-time instruction to check existing roles, C-08 compliance depends on model judgment. R1 V-04 was PARTIAL for same reason. |
| C-09 | Orientation register matches audience | PASS | 2 | Primary axis sub-component. "Writing orientation.frame" section with domain-concrete first-person examples per domain. "Writing orientation.serves" section names beneficiary examples explicitly: "Compliance officers who must certify..." / "Controllers and auditors who rely on...". Pass condition mechanically satisfied. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | "Body section -- column header contract" with explicit FAIL/PASS example table across 5 domains (healthcare, backend/CLI, finance, discovery, governance). Identical quality to V-01. |
| C-11 | Inertia-advocate companion file generated | PARTIAL | 1 | "create a complete companion role file -- not a note or suggestion" with content guidance for orientation.frame, serves, verify questions, expertise.depth, and displacement cost table. No template; fields lens.simplify, scope, collaborates_with, artifacts, workflow not explicitly listed. Field omission risk remains. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | "Do not draft any content after one or two answers. Only begin writing when all three values are confirmed." Named prohibition present. Slightly less explicit than V-03's three-rule set but passes the condition. |
| **Total** | | | **98** | All 5 essential: PASS |

---

### V-05: Full Integration v2

Primary axis: All three R2 gaps (C-10, C-11, C-12) addressed mechanically in a 6-phase lifecycle. Phase 1 HOLD adds named prohibitions. Phase 2 adds complete fill-in template. Phase 4 adds FAIL/PASS column header table. All R1 criteria maintained.

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5 write order: inertia-advocate first (if generated), then .roles/{area}/{subrole}.md. Both paths explicit. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 template shows every field with register labels and format contracts. All 12 required fields present. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1 standalone gate with exact three-mode classification and "Output of Phase 1: {area}, {subrole}, {orientation seed}." |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Phase 3: per-field REGISTER labels with domain-concrete "Good:" and "Bad:" examples for frame, serves, verify, expertise.depth. Healthcare/backend/finance examples per field. Strongest C-04 of all R2 variations. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 ABSENT: complete fill-in template generates the companion file unconditionally. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Phase 3: inline "Good:" and "Bad:" examples per verify slot. "Good: 'Is the HIPAA audit log exported in FHIR-compliant format before submission?' Bad: 'Check audit log configuration.'" |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4 requires domain specializations table as required body element 2. |
| C-08 | Archetype calibrated to area tier | PASS | 2 | Phase 3: "Check existing roles in this area first -- use their archetype value." with craft/process categorization and area examples. |
| C-09 | Orientation register matches audience | PASS | 2 | Phase 3: explicit REGISTER labels ("REGISTER: first-person observational" for frame; "REGISTER: third-person recipient. Must name a beneficiary. Rule: serves names a beneficiary — not a description of the role itself.") with "Good:" and "Bad:" examples per field. Strongest C-09 guard of all R2 variations. |
| C-10 | Body table uses domain-named column headers | PASS | 2 | Phase 4: full FAIL/PASS table with domain examples across 5 domain pairs. "Rule: column headers must name domain constructs -- not generic categories." Explicit contract with failure examples. |
| C-11 | Inertia-advocate companion file generated | PASS | 2 | Phase 2: complete parameterized template with all fields pre-populated and {area} slots throughout. Body included. Write instruction present. Fill-in format eliminates partial-file output path. |
| C-12 | Interactive mode holds for all inputs | PASS | 2 | Phase 1 INTERACTIVE: named prohibitions: "Do not generate any role content after receiving only one or two answers." / "Do not produce a draft, stub, or partial frontmatter mid-conversation." / "Proceed to Phase 2 only when all three values are confirmed." |
| **Total** | | | **100** | All 5 essential: PASS |

---

## Rankings

| Rank | Variation | Score /100 | Band | Distinctive Strength |
|------|-----------|-----------|------|----------------------|
| 1 | **V-05: Full Integration v2** | **100** | Golden | All three R2 gaps mechanical: named-prohibition HOLD (Phase 1) + fill-in template (Phase 2) + FAIL/PASS column header contract (Phase 4). Strongest C-04 and C-09. |
| 2 | **V-03: Interactive-Hold-Protocol** | **99** | Golden | Named-prohibition HOLD makes C-12 binary. Inherits V-05 R1 quality for C-08/C-09/C-11. C-10 PARTIAL: one-line constraint without FAIL/PASS table; designer flags as risk. |
| 3 | **V-01: Column-Header-Contract** | **98** | Golden | R2 adds check-existing-roles (C-08 PASS) and beneficiary guard (C-09 PASS) over R1. FAIL/PASS table makes C-10 mechanical. C-11/C-12 addressed in prose only. |
| 3 | **V-02: Companion-Generation-Explicit** | **98** | Golden | Fill-in template makes C-11 most reliable of single-axis variations. C-10 PARTIAL (one-line only). C-12 PARTIAL (instruction without named prohibitions). |
| 3 | **V-04: Register-with-Domain-Examples** | **98** | Golden | Per-field domain examples make C-04/C-09 strongest in conversational format. FAIL/PASS table makes C-10 mechanical. C-08 PARTIAL (no archetype generation instruction). C-11 PARTIAL (no template). |

All five variations pass all 5 essential criteria. All five are Golden (>= 80 composite, all essential pass).

---

## Key Scoring Decisions

**V-03 C-10: PARTIAL** — Phase 4 says "domain-named column headers (not generic 'Entity / Purpose')" — single-line constraint, same level as V-05 R1 Phase 4. V-05 R1 passed C-10 with this instruction, but the designer's own risk note for V-03 explicitly flags C-10 as "unchanged from R1 gaps." V-03 R1 failed C-10. Without the FAIL/PASS example table present in V-01/V-04/V-05, the instruction depends on model inference. Scored PARTIAL as the reliable read.

**V-01 C-08/C-09: PASS (upgraded from R1)** — R2 V-01 adds "check existing roles in the area; match their archetype value" (C-08) and "must name a beneficiary, not describe the role itself" (C-09) to the field generation section. Neither guard was present in R1 V-01. C-08 pass condition literally says "Checking existing roles in the area and aligning to their pattern = pass." V-01 R2 satisfies this. 2-point improvement over R1 v2-retroactive baseline.

**V-04 C-08: PARTIAL** — No archetype generation instruction in the conversational body. AMEND block flags archetype calibration as a post-write review item but does not instruct the model to check existing roles before generating. AMEND review does not equal generation-time calibration. R1 V-04 was PARTIAL for the same structural reason.

**V-02/V-04 C-11: PARTIAL vs V-03/V-05 C-11: PASS** — The dividing line is explicit field enumeration. V-03 Phase 2 lists all 12 required fields by name ("name, version, archetype, orientation (frame + serves), lens (verify + simplify), expertise (depth + relevance), scope, collaborates_with, artifacts, workflow"). V-05 provides a fill-in template. V-02/V-04 describe content but do not enumerate all 12 fields — scope, collaborates_with, artifacts, workflow omission risk remains.

**Three-way tie at 98** — V-01/V-02/V-04 each fix different gaps as their primary axis and remain PARTIAL on the others. No cross-axis spillover gives any single variation the edge among these three.

---

## v2 Score Delta (R1 retroactive vs R2)

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| R1 v2 retroactive | ~94 | ~98 | ~91 | ~96 | 100 |
| R2 v2 score | 98 | 98 | 99 | 98 | 100 |
| Delta | +4 | 0 | +8 | +2 | 0 |

V-03 shows the largest gain (+8): named-prohibition HOLD (C-12 FAIL→PASS) plus strong C-11 from the Phase 2 field enumeration. V-01 gains +4 from C-08/C-09 upgrades and C-10 primary-axis pass. V-02 and V-05 are stable — their R1 patterns were already well-positioned on their respective axes.

---

## Excellence Signals from V-05 R2

1. **Named-prohibition HOLD is the minimal gate for C-12 — positive instruction is not enough.** V-05 R1 said "Wait for answers before proceeding." V-05 R2 adds "Do not generate any role content after receiving only one or two answers" and "Do not produce a draft, stub, or partial frontmatter mid-conversation." The prohibitions make the constraint categorical. V-03 R2 independently arrived at the same three-rule set and also passes C-12, confirming the pattern: positive instruction (wait) leaves room for rationalization; named prohibition (do not draft after two answers) does not.

2. **Fill-in template for companion file removes the generation decision entirely.** V-02 R1 and V-03 R1 both said "generate a complete companion file" and failed C-11. V-02 R2 and V-05 R2 both provide a complete parameterized template with {area} slots. The model fills slots rather than deciding what "complete" means. This pattern resolves the category of C-11 failure where the model generates a convincing-looking file with missing fields. Template = slots to fill; instruction = decision to make.

3. **FAIL/PASS example tables for column headers are more effective than single-line constraints.** V-05 R1 had "Column names should reflect the domain, not generic 'Entity / Purpose'" — one sentence. V-05 R1 passed C-10 but the rubric notes it was incidental. V-05 R2 and V-01 R2 add a full FAIL/PASS table with 5+ domain-specific PASS examples. V-03 R2 keeps the one-line constraint and scores PARTIAL on C-10 (designer flags as risk). The FAIL/PASS table makes C-10 a pre-write checkable rule rather than a stylistic inference.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named-prohibition interactive hold: explicit 'Do not generate after one or two answers' and 'Do not produce draft mid-conversation' rules make C-12 a hard constraint — positive wait instructions leave rationalization room; named prohibitions close it", "fill-in template for companion file: complete parameterized inertia-advocate template with {area} slots eliminates the generation decision — the model fills slots instead of deciding what complete means, removing the partial-file output path", "column header FAIL/PASS contract: explicit domain-concrete FAIL and PASS example table makes C-10 a pre-write checkable rule rather than a stylistic inference from a single-line constraint"]}
```
