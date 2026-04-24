## corps-scan R3 — Quest Score

**Rubric**: v3, 130 pts | **Golden threshold**: 80 pts + all essential passing

---

## Per-Variation Scoring

All 5 variations score **130/130**. R3 design goal achieved — C-13/C-14/C-15/C-16 are structural invariants.

### Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (40) | Total | All-E Pass | Golden |
|-----------|---------------|------------------|-------------------|-------|------------|--------|
| V-01 Role Sequence | 60 | 30 | 40 | **130** | Yes | Yes |
| V-02 Signal Schema | 60 | 30 | 40 | **130** | Yes | Yes |
| V-03 Formal Reqs | 60 | 30 | 40 | **130** | Yes | Yes |
| V-04 Pre-Check+Debt | 60 | 30 | 40 | **130** | Yes | Yes |
| V-05 Phase Gates | 60 | 30 | 40 | **130** | Yes | Yes |

---

### Ranking (within 130/130 ceiling)

1. **V-04** — Pre-check names 7 criteria by ID (highest). C-16 pre-scheduled as a pre-check item before amends are written — only variation anticipating amend compliance at declaration time. C-14 self-labeled by criterion ID. Directly fixes R2's only miss.
2. **V-01** — Role-sequence enforcement makes compliance structurally impossible to bypass. No scan or YAML work can begin until Compliance Officer role completes.
3. **V-03** — Highest C-15 depth (8 numbered requirements named). Novel forward-reference C-13 form.
4. **V-05** — Distributed per-phase compliance is new architecture. C-14 self-labeled.
5. **V-02** — Most compact format. C-13 as standalone labeled item (weakest form but still PASS).

---

### Excellence Signals (from V-04)

**P-1: C-16 pre-scheduled in pre-check** — commits to debt framing before amends are written; new in R3.
**P-2: Criterion ID as checklist item header** — "[ ] C-12...", "[ ] C-16..." makes rubric-to-output mapping auditable without the rubric document.
**P-3: C-14 self-labeled in artifact** — post-write block states "C-14 dual-bracket: ...Both present." The artifact names the criterion it satisfies.
**P-4: Role-sequence as mechanical enforcement (V-01)** — structural ordering beats instruction-level compliance.

---

Scorecard written to `simulations/quest/scorecards/corps-scan-scorecard-R3-2026-03-16.md`.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["C-16 pre-scheduled as pre-check item before amend section: model commits to debt framing at declaration time before amends are written", "criterion ID as compliance item header: rubric IDs used as primary checklist key making rubric-to-output mapping explicit and auditable", "C-14 self-labeled by criterion ID in post-write artifact: compliance artifact names the criterion it satisfies without consulting the rubric", "role-sequence mechanical enforcement: Compliance Officer role structurally prevents scan or YAML work until compliance pre-check completes"]}
```
attern inside a compliance checklist |
| C-14 | Dual-stage YAML bracketing | **PASS** | Pre-YAML: Role 3 "Pre-YAML compliance note (required before YAML block)" with explicit statement. Post-YAML: Role 3 "Post-write checklist" with STATUS columns. Both present |
| C-15 | Rubric criteria embedded in skill | **PASS** | Role 1 pre-check names criteria by ID: C-12 (Item 1), C-13 (Item 2), C-05 (Item 3), C-11 (Item 4), C-04 (Item 5). 5 criteria explicitly labeled |
| C-16 | Debt-framed amend options | **PASS** | All 3 amend options carry "Debt if skipped:" framing. AMEND-A: pivot mode misalignment propagates to all downstream governance artifacts. AMEND-B: exec office name propagation through corps-rob/committee. AMEND-C: review routing ambiguity named |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5+5+5+5+5 = 130/130**

---

### V-02 — Signal-Schema Mapping Table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Step 2 produces full YAML block; schema is the sole YAML authority |
| C-02 | Team areas derived from repo | **PASS** | Schema rule: "No team area appears in the YAML that is not in the schema." Schema-to-YAML traceability enforced by column reference |
| C-03 | Group structure present | **PASS** | Group container with `type: [division|tribe|pillar]` in YAML template |
| C-04 | Standard roles per team | **PASS** | R1 (maps to C-04): "Every team area row in the schema lists 2+ named roles." Schema "Proposed roles" column enforces this |
| C-05 | Does not write .roles/ | **PASS** | Opening line: "No `.roles/` files will be written." R2 (maps to C-05): "No `.roles/` files, role file content, or role-creation instructions anywhere in this output." |
| C-06 | Pivot mode declared with rationale | **PASS** | After schema: "Pivot mode: [...] / Rationale: [one sentence citing a specific schema row]" |
| C-07 | Exec office placeholder present | **PASS** | R3 (maps to C-07): "An exec-office section is present in the org.yaml." YAML template includes exec-office |
| C-08 | Amend options listed | **PASS** | Step 3 has AMEND-A/B/C with specific commands; all debt-framed |
| C-09 | Detection rationale per area | **PASS** | Schema "Detection evidence" column: "one sentence: why this maps to a team area." YAML template: `# schema-signal: [repo signal from schema row]` |
| C-10 | Inertia Advocate noted | **PASS** | After schema: "Inertia Advocate: corps-build adds this role to each team's role files automatically." YAML: `# Inertia Advocate: auto-added by corps-build` |
| C-11 | Pre-YAML scan inventory listed | **PASS** | R4 (maps to C-11): "The Signal-to-YAML Schema is a distinct artifact that appears before the YAML block." Schema in Step 1 precedes YAML in Step 2 |
| C-12 | Draft boundary front-loaded | **PASS** | "**DRAFT-ONLY: This output is a draft org.yaml for human review. No `.roles/` files will be written.**" appears before schema and YAML |
| C-13 | Self-referential compliance check | **PASS** | "Self-referential confirmation: The draft-only statement is line 1 of this response. STATUS: CONFIRMED -- constraint precedes all schema, inventory, and YAML content." Named item with STATUS: CONFIRMED; the model can only write CONFIRMED after the draft-only statement is above it |
| C-14 | Dual-stage YAML bracketing | **PASS** | Pre-YAML: "Pre-YAML constraint note (required immediately before the YAML block)" with explicit statement. Post-YAML: "POST-YAML CHECK -- signal-schema compliance" with full verification table |
| C-15 | Rubric criteria embedded in skill | **PASS** | Requirements section maps R1->C-04, R2->C-05, R3->C-07, R4->C-11, R5->C-12. 5 criteria named with explicit parenthetical mapping |
| C-16 | Debt-framed amend options | **PASS** | All 3 amend options carry "Debt if skipped:" framing. AMEND-A: misalignment propagation to all corps-* artifacts. AMEND-B: exec name to governance templates. AMEND-C: schema signal misclustering and affected downstream step named |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5+5+5+5+5 = 130/130**

---

### V-03 — Phrasing Register: Formal Numbered Requirements

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Section 3 produces complete YAML; pre-YAML compliance statement required immediately before block |
| C-02 | Team areas derived from repo | **PASS** | "All team area names trace to the Signal Inventory." Section 1 produces repo-grounded inventory; traceability enforced in Section 3 |
| C-03 | Group structure present | **PASS** | Group container with `type: [division|tribe|pillar]` in YAML template |
| C-04 | Standard roles per team | **PASS** | Requirement 4 (maps to C-04): "Every team area in the YAML lists at least 2 named roles. Generic placeholders fail." |
| C-05 | Does not write .roles/ | **PASS** | DECLARATION at top + Requirement 2 (maps to C-05): "This output does not write `.roles/` files, does not include role file content, and does not instruct the user to create role files." |
| C-06 | Pivot mode declared with rationale | **PASS** | Section 2: "Pivot mode: [mode] / Rationale: [one sentence from Signal Inventory] / Alternatives considered: [...]" |
| C-07 | Exec office placeholder present | **PASS** | Requirement 5 (maps to C-07): "The org.yaml contains an exec-office section, even if the name is a placeholder." YAML template enforces it |
| C-08 | Amend options listed | **PASS** | Section 4 has AMEND-A/B/C with commands; "Non-compliance consequence" framing per option |
| C-09 | Detection rationale per area | **PASS** | Requirement 6 (maps to C-09): "At least half of the detected team areas include a comment or annotation naming the specific repo signal." `# detected from:` in YAML |
| C-10 | Inertia Advocate noted | **PASS** | Requirement 7 (maps to C-10): "The output notes that corps-build will auto-add an Inertia Advocate role." Section 1 inventory note confirms |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Requirement 3 (maps to C-11): "A repo signal inventory, distinct from the YAML block, must appear before the YAML block begins." Section 1 produces it; STATUS check follows inventory |
| C-12 | Draft boundary front-loaded | **PASS** | DECLARATION appears as the very first line. Requirement 1 self-confirms: "Satisfied by: The DECLARATION block above, which is line 1 of this output. STATUS: CONFIRMED." |
| C-13 | Self-referential compliance check | **PASS** | Two-part pattern: "Verification: This line IS the declaration required by Requirement 1 below" (forward reference) followed by Requirement 1: "STATUS: CONFIRMED -- see DECLARATION at line 1." Model cannot confirm Requirement 1 without having written the DECLARATION above it |
| C-14 | Dual-stage YAML bracketing | **PASS** | Pre-YAML: Section 3 "Pre-YAML compliance statement (required): 'Producing org.yaml draft. Requirements 2, 4, 5, 6 active. No .roles/ content.'" Post-YAML: "Requirements Status -- post-YAML" table confirming R2/R4/R5/R6 |
| C-15 | Rubric criteria embedded in skill | **PASS** | 8 numbered requirements map explicitly to rubric criteria: R1->C-04, R2->C-05, R3->C-11, R4->C-04, R5->C-07, R6->C-09, R7->C-10, R8->C-16. Highest criterion-count of all variations |
| C-16 | Debt-framed amend options | **PASS** | "Non-compliance consequence:" per amend option (equivalent to "Debt if skipped:"). All 3 options name downstream failure. Requirement 8 STATUS check at end of Section 4 confirms satisfaction |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5+5+5+5+5 = 130/130**

---

### V-04 — Ceiling Variant: Compliance Pre-Check + Debt-Framed Amends

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Step 2 produces complete YAML; post-write checklist verifies all structural elements |
| C-02 | Team areas derived from repo | **PASS** | "Traceability rule: every team area name must match a 'Team area candidate' cell in the Signal Table." Post-write checklist item 1 confirms |
| C-03 | Group structure present | **PASS** | Post-write checklist: "At least one group container above teams STATUS: [CONFIRMED / FAIL]" |
| C-04 | Standard roles per team | **PASS** | Pre-check C-04: "Every team area I draft will list at least 2 named roles. I will not use generic placeholders." Post-write checklist confirms |
| C-05 | Does not write .roles/ | **PASS** | Pre-check C-05: "I will not write .roles/ files, include role file content, or instruct the user to create role files at any point in this output." Final gate confirms |
| C-06 | Pivot mode declared with rationale | **PASS** | Signal Table section: "Pivot mode: [...] / Rationale: [one sentence citing a specific table row]" |
| C-07 | Exec office placeholder present | **PASS** | Pre-check C-07: "I will include an exec-office section in the YAML even if the name is a placeholder." Signal Table includes exec inference field |
| C-08 | Amend options listed | **PASS** | Step 3 has AMEND-A/B/C with commands; all debt-framed; Every option must name debt (instruction in Step 3 header) |
| C-09 | Detection rationale per area | **PASS** | Signal Table "Detection note" column; YAML `# signal: [table row reference]`; post-write checklist: "# signal: comment on at least half the team areas" |
| C-10 | Inertia Advocate noted | **PASS** | Signal Table: "Inertia Advocate: corps-build auto-adds this role to each team's role files." YAML: `# Inertia Advocate: auto-added by corps-build -- expect it in role files` |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Pre-check C-11: "I will produce a Repo Signal Table as a distinct section that appears before the YAML block. The table is not the YAML. It precedes the YAML." Step 1 before Step 2 |
| C-12 | Draft boundary front-loaded | **PASS** | Pre-check C-12: draft-only statement is the first substantive content, confirmed in pre-check before scan, inventory, or YAML begins |
| C-13 | Self-referential compliance check | **PASS** | Pre-check C-13: "The draft-only statement named in C-12 above appears before any YAML in this response. This item confirms that the previous item is satisfied. STATUS: CONFIRMED." C-13 explicitly confirms C-12 by reference; the inter-item dependency is named |
| C-14 | Dual-stage YAML bracketing | **PASS** | Pre-YAML: "Pre-YAML traceability statement (required immediately before YAML block)". Post-YAML: "POST-WRITE CHECKLIST" with explicit self-label: "C-14 dual-bracket: Pre-YAML statement: CONFIRMED. Post-write checklist: above. Both present." Only variation to name C-14 by criterion ID in the artifact that satisfies it |
| C-15 | Rubric criteria embedded in skill | **PASS** | Pre-check names 7 criteria by ID: C-12, C-13, C-05, C-11, C-04, C-07, C-16. Highest ID-count of all variations. Only variation to include C-16 as a pre-check item |
| C-16 | Debt-framed amend options | **PASS** | Pre-check C-16 pre-schedules debt framing before amends are written ("STATUS: SCHEDULED"). All 3 amend options carry "Debt if skipped:" framing with named downstream propagation paths |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5+5+5+5+5 = 130/130**

---

### V-05 — Distributed Compliance: Per-Phase Entry + Exit Gates

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Phase 3 YAML Draft produces complete block; Phase 3 EXIT CHECK verifies all elements |
| C-02 | Team areas derived from repo | **PASS** | Phase 3 ENTRY CHECK: "All team names will trace to Phase 1 signal table rows. STATUS: CONFIRMED." Phase 3 EXIT CHECK confirms every name matches Phase 1 |
| C-03 | Group structure present | **PASS** | Group container with `type: [division|tribe|pillar]` in template; Phase 3 EXIT CHECK: "At least one group container above teams" |
| C-04 | Standard roles per team | **PASS** | Phase 3 ENTRY CHECK: "C-04 NAMED ROLES: Every team area will have 2+ specific named roles STATUS: CONFIRMED." Phase 3 EXIT CHECK confirms |
| C-05 | Does not write .roles/ | **PASS** | DRAFT-ONLY BOUNDARY at top. Phase 3 ENTRY CHECK: "C-05 ROLE FILES: I confirm I will not write .roles/ files STATUS: CONFIRMED." Phase 4 EXIT CHECK: "no .roles/ content in any phase STATUS: CONFIRMED" |
| C-06 | Pivot mode declared with rationale | **PASS** | Phase 2: "Pivot mode: [mode] / Rationale: [one sentence citing at least one specific Phase 1 signal table row]." Phase 2 EXIT CHECK confirms pivot declared with rationale |
| C-07 | Exec office placeholder present | **PASS** | Phase 3 ENTRY CHECK: "C-07 EXEC OFFICE: exec-office section will be present in the YAML STATUS: CONFIRMED." YAML template enforces it |
| C-08 | Amend options listed | **PASS** | Phase 4 has AMEND-A/B/C with commands; Phase 4 EXIT CHECK: "3 amend options written -- each actionable with a named command STATUS: CONFIRMED" |
| C-09 | Detection rationale per area | **PASS** | YAML: `# detected from: [Phase 1 signal row]`. Phase 3 EXIT CHECK: "# detected from: comment on at least half the team areas" |
| C-10 | Inertia Advocate noted | **PASS** | Phase 2: "Inertia Advocate note: corps-build auto-adds Inertia Advocate...must be explicitly considered." YAML: `# Inertia Advocate: added automatically by corps-build` |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Phase 1 produces signal table. Phase 1 EXIT CHECK: "Signal table is a distinct section -- it is not the YAML. No YAML written in Phase 1. STATUS: CONFIRMED." |
| C-12 | Draft boundary front-loaded | **PASS** | "**DRAFT-ONLY BOUNDARY: This output is a draft org.yaml for human review...No `.roles/` files will be written.**" appears as first line before all phase descriptions |
| C-13 | Self-referential compliance check | **PASS** | Phase 3 ENTRY CHECK: "C-12 DRAFT BOUNDARY: Draft-only boundary is line 1 of this output STATUS: CONFIRMED." Checklist item confirms C-12 at point of entering YAML phase; model can only write CONFIRMED if boundary is above it |
| C-14 | Dual-stage YAML bracketing | **PASS** | Phase 3 ENTRY CHECK (pre-YAML) + Phase 3 EXIT CHECK (post-YAML). EXIT CHECK self-labels: "C-14 dual-bracket: Phase 3 ENTRY CHECK (pre-YAML). Phase 3 EXIT CHECK (post-YAML). Both present." |
| C-15 | Rubric criteria embedded in skill | **PASS** | Phase 3 ENTRY CHECK names criteria by ID: C-12, C-05, C-04, C-07. Phase 4 ENTRY CHECK names C-16 intent. 4+ criteria named by ID; each phase check names its governed criterion |
| C-16 | Debt-framed amend options | **PASS** | Phase 4 ENTRY CHECK: "Amend options will be debt-framed: at least 2 options name downstream debt STATUS: CONFIRMED." Phase 4 EXIT CHECK confirms. All 3 options carry "Debt if skipped:" framing |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5+5+5+5+5 = 130/130**

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (40) | Total | All-E Pass | Golden |
|-----------|---------------|------------------|-------------------|-------|------------|--------|
| V-01 | 60 | 30 | 40 | **130** | Yes | Yes |
| V-02 | 60 | 30 | 40 | **130** | Yes | Yes |
| V-03 | 60 | 30 | 40 | **130** | Yes | Yes |
| V-04 | 60 | 30 | 40 | **130** | Yes | Yes |
| V-05 | 60 | 30 | 40 | **130** | Yes | Yes |

**All 5 variations score 130/130. R3 design goal achieved: C-13/C-14/C-15/C-16 are structural invariants.**

---

## Ranking

All variations tie at ceiling. Differentiation on structural robustness and pattern strength:

1. **V-04** -- *Top* -- Pre-check names 7 criteria by ID (highest ID-count). C-16 pre-scheduled as a pre-check item before amends are written -- only variation that anticipates amend compliance at declaration time. C-14 self-labeled by criterion ID in post-write checklist. Directly combines R2's proven pre-check architecture with R2's debt-framing form. Final gate summarizes all compliance states.

2. **V-01** -- *Strong* -- Role-sequence enforcement makes compliance structurally impossible to bypass: Compliance Officer must complete before Archaeologist, Archaeologist before Drafter. No YAML work can begin without satisfying C-13 and C-11. Strongest mechanical ordering guarantee.

3. **V-03** -- *Strong* -- Highest C-15 depth (8 numbered requirements, most criteria named of any variation). Novel C-13 form: forward-reference "Verification: This line IS the declaration required by Requirement 1 below" before the requirement appears. Completion Statement in Section 5 summarizes all 8 requirement statuses.

4. **V-05** -- *Solid* -- Distributed per-phase compliance is a new architectural pattern: entry+exit per phase spreads verification across the lifecycle. C-14 self-labeled. Suitable for multi-artifact skills where front-loading all compliance would be premature.

5. **V-02** -- *Solid* -- Most compact format. Single schema artifact serves as both inventory and YAML authority. Self-referential item is a standalone labeled statement rather than a formal checklist item -- satisfies C-13 but is the weakest form of the pattern.

---

## Excellence Signals (from top scorer V-04)

**Pattern 1: C-16 pre-scheduled as pre-check obligation** -- V-04 is the only variation to add debt framing as a pre-check item ("STATUS: SCHEDULED") before the amend section is written. The model commits to downstream debt framing at declaration time, before it knows what the amends will say. Anticipating a later section's compliance requirement in the pre-check is new in R3.

**Pattern 2: Criterion ID as compliance item header** -- V-04 uses rubric IDs as primary item identifiers in the pre-check: "[ ] C-12 DRAFT BOUNDARY...", "[ ] C-13 SELF-REFERENTIAL...", etc. R2's V-04 named behaviors; R3 V-04 names criteria directly. Makes the rubric-to-output mapping explicit and auditable without consulting the rubric document.

**Pattern 3: C-14 self-labeled by criterion ID in the artifact** -- V-04 and V-05 both state "C-14 dual-bracket" by name in the post-write verification. A compliance artifact that names the criterion it satisfies is self-documenting. Scoring an artifact becomes possible by reading the artifact alone.

**Pattern 4: Role-sequence mechanical enforcement (V-01)** -- Assigning compliance work to a named role (Compliance Officer) in strict sequence makes certain criteria structurally unskippable. Different from pre-check: role ordering enforces sequence at structure level, not instruction level. No instruction can accidentally skip Role 1 because Role 2 cannot begin until Role 1 is complete.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["C-16 pre-scheduled as pre-check item before amend section: model commits to debt framing at declaration time before amends are written", "criterion ID as compliance item header: rubric IDs used as primary checklist key making rubric-to-output mapping explicit and auditable", "C-14 self-labeled by criterion ID in post-write artifact: compliance artifact names the criterion it satisfies without consulting the rubric", "role-sequence mechanical enforcement: Compliance Officer role structurally prevents scan or YAML work until compliance pre-check completes"]}
```
