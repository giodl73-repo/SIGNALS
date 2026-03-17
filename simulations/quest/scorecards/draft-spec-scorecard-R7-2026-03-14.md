## Round 7 — `draft-spec` Scorecard

---

### Rubric Reference (v7)

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01–C-05 | 60 |
| Recommended | C-06–C-08 | 30 |
| Aspirational | C-09–C-25 | 85 |
| **Total** | **25** | **175** |

Golden threshold: all 5 essential pass AND composite ≥ 85.

---

## V-01 — C-25 Two-Branch Fallback (Minimal Base)

**Base**: merged [INERTIA-TABLE], no C-22/C-23/C-24. Branch A + Branch B each with own `VERBATIM RESPONSE:` block.

### Essential (5/5 — 60 pts)

| ID | Pass | Evidence |
|----|------|----------|
| C-01 | PASS | Phase 3 contains Purpose → Requirements → Design → Constraints → Open Questions in prescribed order |
| C-02 | PASS | [SCOUT-STATUS-TABLE] with 7 rows in Phase 0, before any EXECUTE content |
| C-03 | PASS | [PM-COVERAGE-TABLE] pre-assigns P0 rows; "C-03 WAIVER stated here" clause present; coverage count `{n}/{n}` |
| C-04 | PASS | Phase 4 has [FINDINGS-TABLE] + "Finding claim: [explicit scan outcome — never absent or empty]" |
| C-05 | PASS | `{topic}-spec-{date}.md` naming; frontmatter lists skill, topic, item, date, skill_version, input |

### Recommended (3/3 — 30 pts)

| ID | Pass | Evidence |
|----|------|----------|
| C-06 | PASS | Strategy invoked in Phase 2 with PASS/FINDING table; Compliance and Strategy invoked inline within Phase 3 sections |
| C-07 | PASS | [CONTRADICTION-SCAN]: "name 'R-XX vs R-YY' after scanning all rows, or 'none found after scanning R-01 through R-{n}'" — R-ID format required |
| C-08 | PASS | Phase 5: "INVALID IF list contains fewer than 2 items or any item is vague (must name section + finding ID + specific change)" |

### Aspirational (13/17)

| ID | Pass | Evidence |
|----|------|----------|
| C-09 | PASS | Branch A (all NOT FOUND) and Branch B (requirements absent, others loaded) both documented as named conditionals |
| C-10 | PASS | [CNS-SLOT-1-OF-2] requires naming a specific non-requirements artifact as "Source artifact" |
| C-11 | PASS | [CNS-SLOT-2-OF-2] pre-printed as labeled row in Purpose table; C-11 fires note if unfilled |
| C-12 | PASS | PM inline in Purpose; PM inline in Requirements; Strategy inline in Design; Compliance inline in Constraints — each within its section block |
| C-13 | PASS | Requirements table: `Req ID \| Requirement Text \| Priority \| Spec Entry \| Status` — per-row Status column |
| C-14 | PASS | [CONTRADICTION-SCAN] names scan source "R-01 through R-{n}" before confirming absence; PM declarations name source artifact for each enumeration |
| C-15 | PASS | CNS-SLOT appears in Phase 1 (location 1 of 2) and Phase 3 Purpose (location 2 of 2) — structurally independent |
| C-16 | PASS | [PM-COVERAGE-TABLE] in Phase 1 pre-assigns P0 rows before Phase 3 writing; Architect "RECEIVES [PM-COVERAGE-TABLE] and fills pre-assigned rows" |
| C-17 | PASS | Five named gate tokens: [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL]; downstream phases name each |
| C-18 | PASS | Branch A VERBATIM RESPONSE: complete pre-written copy; Branch B VERBATIM RESPONSE: complete pre-written copy; HALT instruction present |
| C-19 | PASS | [CNS-SLOT-1-OF-2] labeled "location 1 of 2"; [CNS-SLOT-2-OF-2] labeled "location 2 of 2" — ordinal with stated denominator |
| C-20 | PASS | Phase 0B: "**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each IG-ID risk signal PRODUCES [INERTIA-TABLE].**" — role + sources + action + output in one declaration |
| C-21 | PASS | [INERTIA-ANALYZED]: "INVALID IF emitted without [INERTIA-TABLE] present in this phase block with all IG-ID rows fully populated" — invalidity declared; presence certifies prerequisite evidence |
| C-22 | **FAIL** | Phase 0B uses merged [INERTIA-TABLE] (single table with IG-ID, Hypothesis, Elimination, Risk, Mitigation, Verdict) — not separate IG-REGISTER and ID-REGISTER |
| C-23 | **FAIL** | No Responsible Role column in [INERTIA-TABLE] |
| C-24 | **FAIL** | No CASCADE TO: annotations on any unified declaration |
| C-25 | PASS | "Fallback Branch A — ALL rows NOT FOUND" and "Fallback Branch B — requirements NOT FOUND but others LOADED" — structurally distinct named headers, each with own `VERBATIM RESPONSE:` blockquote |

**Composite V-01**: (5/5 × 60) + (3/3 × 30) + (13/17 × 85) = 60 + 30 + **65.0** = **155**

---

## V-02 — C-25 Expanded Branch B (4 Sub-conditionals)

**Base**: same as V-01 structure (merged [INERTIA-TABLE], no C-22/C-23/C-24). Branch B expanded into 4 artifact-specific sub-conditions (B-1 through B-4), each with its own `VERBATIM RESPONSE:` block.

### Essential (5/5 — 60 pts)
Identical to V-01. All five PASS.

### Recommended (3/3 — 30 pts)
Identical to V-01. All three PASS.

### Aspirational (13/17)

| ID | Pass | Evidence |
|----|------|----------|
| C-09–C-21 | PASS (all 13) | Structurally identical to V-01 in all these axes |
| C-18 | PASS | Branch A has VERBATIM; Branch B has 4 sub-conditionals each with own VERBATIM RESPONSE: block; "HALT on any Branch B sub-condition...Do not blend sub-condition copy; emit the matching block verbatim" |
| C-22 | **FAIL** | Merged [INERTIA-TABLE], same as V-01 |
| C-23 | **FAIL** | No Responsible Role column |
| C-24 | **FAIL** | No CASCADE TO: annotations |
| C-25 | PASS | Branch A + Branch B (with 4 named sub-conditions) both have distinct VERBATIM RESPONSE: blocks; branch conditions structurally demarcated |

**Note on C-25**: V-02 satisfies C-25 (two-branch structure with distinct VERBATIM blocks) but the sub-conditional specificity within Branch B does not yet have a rubric criterion — it's a potential v8 signal (see Excellence Signals below).

**Composite V-02**: (5/5 × 60) + (3/3 × 30) + (13/17 × 85) = 60 + 30 + **65.0** = **155**

---

## V-03 — Phrasing Register: Concise Imperative (+ C-25 carried)

**Base**: all structural elements from parallel-register designs preserved; REQUIRES/PRODUCES/BLOCKS headers replaced with imperative voice ("**PM: scan X → fill Y**", "Confirm [token] is in the document"). Has [IG-REGISTER] + [ID-REGISTER] as separate tables. Has Responsible Role in [IG-REGISTER]. No CASCADE TO:.

### Essential (5/5 — 60 pts)

| ID | Pass | Evidence |
|----|------|----------|
| C-01 | PASS | GUIDED SECTIONS contains all five in order; SECTION ORDER declared |
| C-02 | PASS | [SCOUT-STATUS-TABLE] in INTAKE (Step 1), before INERTIA CHECK |
| C-03 | PASS | [PM-COVERAGE-TABLE] with row-level assignment; "C-03 waiver stated here" fallback |
| C-04 | PASS | [FINDINGS-TABLE] + "Finding claim: [explicit scan outcome — must reference sections scanned]" |
| C-05 | PASS | Frontmatter fields all present; naming convention preserved |

### Recommended (3/3 — 30 pts)

| ID | Pass | Evidence |
|----|------|----------|
| C-06 | PASS | Strategy inline in Design; Compliance inline in Constraints; PM invocations in Purpose and Requirements |
| C-07 | PASS | [CONTRADICTION-SCAN]: "name 'R-XX vs R-YY' or 'none found after scanning R-01 through R-{n}'" |
| C-08 | PASS | AMEND: "Produce at least 2 specific, actionable amendments. Each must name a section, a finding ID, and the exact change." |

### Aspirational (16/17)

| ID | Pass | Evidence |
|----|------|----------|
| C-09 | PASS | *Branch A — all seven NOT FOUND* and *Branch B — requirements NOT FOUND but others LOADED* — named, italicized branch labels |
| C-10 | PASS | [CNS-SLOT-1-OF-2] requires "Source artifact: [name the specific loaded artifact]" |
| C-11 | PASS | [CNS-SLOT-2-OF-2] pre-printed row in Purpose table; "Cross-namespace signal, location 2 of 2" label; "> [CNS-SLOT-2-OF-2] blank = C-11 fires" |
| C-12 | PASS | Purpose: "**PM: verify [CNS-SLOT-1-OF-2] → place...→ produce [CNS-SLOT-2-OF-2].**" inline in section. Requirements: "**PM: confirm...**" inline. Design: "**Strategy: validate...**" inline. Constraints: "**Compliance: validate...**" inline — all embedded within content blocks |
| C-13 | PASS | Requirements: `Req ID \| Requirement Text \| Priority \| Spec Entry \| Status` |
| C-14 | PASS | Contradiction: "name 'R-XX vs R-YY' or 'none found after scanning R-01 through R-{n}'" names scan source; PM: "scan all rows in `{topic}-requirements-{date}.md`" explicit source |
| C-15 | PASS | [CNS-SLOT-1-OF-2] in PM PRE-ASSIGNMENT + [CNS-SLOT-2-OF-2] in Purpose — two structurally independent locations |
| C-16 | PASS | PM PRE-ASSIGNMENT block before GUIDED SECTIONS; "Before writing the five sections, PM assigns each P0 requirement" |
| C-17 | PASS | [INERTIA-ANALYZED], [PM-CONTRACT-SEAL], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL] — each confirmed by "Confirm [X] is in the document. If not, stop." |
| C-18 | PASS | Branch A and Branch B VERBATIM RESPONSE: blocks with complete copy; "Stop here until user responds/confirms" |
| C-19 | PASS | [CNS-SLOT-1-OF-2] = "location 1 of 2", [CNS-SLOT-2-OF-2] = "location 2 of 2" — stated denominator |
| C-20 | PASS | Concise imperative form still unifies role + source: "**PM: scan `{topic}-requirements-{date}.md` → fill [PM-COVERAGE-TABLE].**" names both in one declaration; satisfies C-20's "single parseable instruction" requirement |
| C-21 | PASS | [INERTIA-ANALYZED]: "INVALID if: either register is missing; any IG-XX Responsible Role cell is blank; any ID-XX Confirming Role does not match its paired IG-XX; row counts differ; any AMPLIFIED row's Artifact Trigger is generic" — invalidity rule referencing prerequisite register evidence |
| C-22 | PASS | [IG-REGISTER] and [ID-REGISTER] are separate distinct tables in INERTIA CHECK; row-count equivalence rule enforced |
| C-23 | PASS | [IG-REGISTER]: `\| IG-ID \| Default to Block \| Artifact Trigger \| Risk \| Responsible Role \| Mitigation Location \|`; [ID-REGISTER]: `\| ID-ID \| Paired IG \| Defeat Condition \| Confirmation Evidence \| Confirming Role \|`; "Confirming Role does not match its paired IG-XX" = invalidity condition |
| C-24 | **FAIL** | No CASCADE TO: annotations. Concise imperative register deliberately excludes them. |
| C-25 | PASS | *Branch A* and *Branch B* with distinct VERBATIM RESPONSE: blockquotes; branch conditions named and structurally demarcated |

**Register test result**: V-03 reaches 16/17 aspirational (missing only C-24) using entirely concise imperative phrasing. The REQUIRES/PRODUCES/BLOCKS boilerplate is **not load-bearing** for any C-09 through C-23, C-25 criterion — confirmed.

**Composite V-03**: (5/5 × 60) + (3/3 × 30) + (16/17 × 85) = 60 + 30 + **80.0** = **170**

---

## V-04 — C-25 + C-22 (Two-Branch + Parallel Registers, no C-23/C-24)

**Base**: REQUIRES/PRODUCES/BLOCKS format. [IG-REGISTER] and [ID-REGISTER] as distinct tables **but no Responsible Role column**. Branch A + Branch B VERBATIM blocks.

### Essential (5/5 — 60 pts)
All five PASS (identical structure to other variations).

### Recommended (3/3 — 30 pts)
All three PASS.

### Aspirational (15/17)

| ID | Pass | Evidence |
|----|------|----------|
| C-09–C-21 | PASS (all 13) | Same structure as V-01 for all non-register criteria |
| C-22 | PASS | [IG-REGISTER]: `\| IG-ID \| Guard: Default to Block \| Named Artifact Trigger \| Risk Signal \| Mitigation Location \|`; [ID-REGISTER]: `\| ID-ID \| Guards \| Defeat Condition \| Confirmation Evidence \|`; row-count rule enforced; INVALID condition references both registers |
| C-23 | **FAIL** | [IG-REGISTER] has no Responsible Role column; [ID-REGISTER] has no Confirming Role. The axis explicitly excludes C-23. |
| C-24 | **FAIL** | No CASCADE TO: annotations |
| C-25 | PASS | Branch A + Branch B both with named headers and distinct VERBATIM RESPONSE: blockquotes; HALT instructions present |

**Composite V-04**: (5/5 × 60) + (3/3 × 30) + (15/17 × 85) = 60 + 30 + **75.0** = **165**

---

## V-05 — Full Combination: C-22 + C-23 + C-24 + C-25 (Target 175/175)

**Base**: All four axes explicit. [IG-REGISTER] with Responsible Role + [ID-REGISTER] with Confirming Role (cross-matched). CASCADE TO: on every unified declaration. Branch A + Branch B VERBATIM blocks.

### Essential (5/5 — 60 pts)
All five PASS.

### Recommended (3/3 — 30 pts)
All three PASS.

### Aspirational (17/17 — 85 pts)

| ID | Pass | Evidence |
|----|------|----------|
| C-09 | PASS | Branch A (all NOT FOUND) and Branch B (requirements absent) — named conditional branches |
| C-10 | PASS | [CNS-SLOT-1-OF-2] "Source artifact: [name the specific loaded artifact]" |
| C-11 | PASS | `[CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2` pre-printed row in Purpose table; "> If [CNS-SLOT-2-OF-2] is blank, C-11 fires from this location" |
| C-12 | PASS | Inline within each Phase 3 section: Purpose has PM inline, Requirements has PM inline, Design has Strategy inline (with CASCADE reference), Constraints has Compliance inline |
| C-13 | PASS | Requirements per-row table with Spec Entry + Status columns |
| C-14 | PASS | [CONTRADICTION-SCAN] names scan source; PM declarations name source artifacts explicitly; AMPLIFIED invalidity rule in [INERTIA-ANALYZED] names "Named Artifact Trigger must address the named threshold dimension" |
| C-15 | PASS | [CNS-SLOT-1-OF-2] in Phase 1 (location 1 of 2) + [CNS-SLOT-2-OF-2] in Phase 3 Purpose (location 2 of 2) — CASCADE TO: explicitly declares both addresses |
| C-16 | PASS | [PM-COVERAGE-TABLE] in Phase 1 pre-assigns before Phase 3; CASCADE TO: "single instantiation; Architect receives [PM-COVERAGE-TABLE] as a pre-filled contract" |
| C-17 | PASS | Five gate tokens; each downstream phase states BLOCKS condition; Output summary lists all five |
| C-18 | PASS | Branch A and Branch B each have complete pre-written VERBATIM RESPONSE: copy; "HALT" + "Do not compose an alternative response; emit the text above verbatim" |
| C-19 | PASS | [CNS-SLOT-1-OF-2] = "location 1 of 2"; [CNS-SLOT-2-OF-2] = "location 2 of 2"; CASCADE TO: itself states "Completeness verifiable by counting labeled instances (1 of 2 + 2 of 2)" |
| C-20 | PASS | Phase 0B: "**PM INSPECTS `scout-feasibility` AND `scout-compliance` REQUIRES both artifacts (if LOADED) TO ASSESS each inertia guard and defeat PRODUCES [IG-REGISTER] and [ID-REGISTER].**" — single declaration, role + sources + action + outputs |
| C-21 | PASS | [INERTIA-ANALYZED]: "INVALID IF emitted without BOTH [IG-REGISTER] and [ID-REGISTER]...All IG-XX rows fully populated including Responsible Role (not blank)...Confirming Role in each ID-XX matches Responsible Role in paired IG-XX...pair-balanced in this block" — invalidity rule names all prerequisite evidence forms; "certifies [IG-REGISTER] and [ID-REGISTER] are structurally complete, role-bound, and pair-balanced" |
| C-22 | PASS | [IG-REGISTER] + [ID-REGISTER] as separate named tables; "[ID-REGISTER] must have exactly as many rows as IG-REGISTER" enforced |
| C-23 | PASS | [IG-REGISTER]: `\| IG-ID \| Guard: Default to Block \| Named Artifact Trigger \| Risk Signal \| **Responsible Role** \| Mitigation Location \|`; [ID-REGISTER]: `\| ... \| **Confirming Role** \|`; invalidity condition: "Confirming Role must match Responsible Role in paired IG-XX"; IG/ID role binding is a closed-loop structural check |
| C-24 | PASS | CASCADE TO: present on every unified declaration: Phase 0B → "single instantiation"; Phase 1 CNS-SLOT → "location 1 of 2 → location 2 of 2: Phase 3 Purpose"; Phase 2 Strategy → "location 1 of 2 → location 2 of 2: Phase 3 Design inline"; Phase 3 Purpose → "completing the cascade declared in Phase 1"; Phase 4 scan checklist explicitly audits: "Cascade completeness: CNS-SLOT location 1 of 2 (Phase 1) and location 2 of 2 (Purpose) both filled; Strategy location 1 of 2 (Phase 2) and location 2 of 2 (Design inline) both filled" |
| C-25 | PASS | "Fallback Branch A — ALL rows NOT FOUND" with VERBATIM RESPONSE: blockquote + HALT; "Fallback Branch B — requirements NOT FOUND but at least one other artifact LOADED" with distinct VERBATIM RESPONSE: blockquote + HALT; Output summary: "Branch conditions structurally distinct" |

**Composite V-05**: (5/5 × 60) + (3/3 × 30) + (17/17 × 85) = 60 + 30 + **85** = **175** ✓ Target achieved.

---

## Final Rankings

| Rank | Variation | Essential | Recommended | Aspirational | **Composite** |
|------|-----------|-----------|-------------|--------------|---------------|
| 1 | **V-05** | 5/5 (60) | 3/3 (30) | 17/17 (85) | **175** |
| 2 | **V-03** | 5/5 (60) | 3/3 (30) | 16/17 (80) | **170** |
| 3 | **V-04** | 5/5 (60) | 3/3 (30) | 15/17 (75) | **165** |
| 4 | **V-01** | 5/5 (60) | 3/3 (30) | 13/17 (65) | **155** |
| 4 | **V-02** | 5/5 (60) | 3/3 (30) | 13/17 (65) | **155** |

All essential criteria pass in every variation. Golden threshold (all 5 essential + composite ≥ 85) achieved by all five variations.

---

## Excellence Signals

**From V-05 (top scorer — C-24 the differentiating axis):**

- **Cascade completeness as a named self-review audit item**: V-05's Phase 4 scan checklist explicitly lists each cascade chain by its address pair ("CNS-SLOT location 1 of 2 (Phase 1) and location 2 of 2 (Purpose) both filled") and the Output summary declares "All CASCADE TO: denominators verified." This converts cascade completeness from a structural implication into an explicitly audited property. Current criteria require cascade declarations (C-24) and ordinal labels (C-19) but no criterion requires the self-review phase to name each cascade chain by address and confirm its closure. Potential **v8 criterion**: "Phase 4 scan checklist names each required cascade chain by its origin–destination address pair and requires affirmative evidence that both locations are filled."

**From V-02 (Branch B sub-conditionals):**

- **Artifact-specific verbatim copy within Branch B**: V-02's B-1 through B-4 sub-conditions each name the specific available artifact type(s) in their VERBATIM RESPONSE: text ("I have feasibility and compliance signals..." / "I have a feasibility assessment..." / "I have a compliance scan..."). The current C-25 pass condition requires only structurally named Branch A and Branch B with distinct VERBATIM blocks — generic "some signals" language satisfies it. V-02 demonstrates that naming the specific artifact type in the verbatim copy makes the response materially more model-ready. Potential **v8 criterion**: "Branch B verbatim copy names the specific artifact type(s) present (by role: feasibility, compliance, market, etc.) rather than using generic 'some signals' language; each sub-condition produces artifact-aware copy."

**From V-03 (register test result):**

- **REQUIRES/PRODUCES/BLOCKS syntax is not load-bearing for C-09–C-23, C-25**: V-03 reaches 170/175 using pure concise imperative phrasing. The one miss (C-24) was deliberate exclusion, not a consequence of phrasing. This confirms that future simplification of the formal boilerplate register carries no structural cost for any currently-scored criterion.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["V-05 Phase 4 scan checklist names each cascade chain by its address pair (origin location N of M → destination location M of M) and requires confirmatory evidence per chain — cascade completeness is explicitly audited rather than implied; potential v8 criterion: self-review scan must enumerate each CASCADE TO: chain by name and confirm both ends are filled", "V-02 Branch B sub-conditionals provide artifact-specific verbatim copy naming the exact available artifact type(s) (feasibility+compliance / feasibility-only / compliance-only / other signals) rather than generic 'some signals' language — each sub-condition has its own VERBATIM RESPONSE: block; potential v8 criterion: Branch B copy names the specific artifact type(s) present by role"]}
```
