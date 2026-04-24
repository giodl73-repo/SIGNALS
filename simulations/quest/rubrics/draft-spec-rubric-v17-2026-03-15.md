---
skill: quest:score
rubric_for: draft-spec
version: v17
date: 2026-03-15
source_rounds: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17
---

# Rubric — `draft-spec` — v17

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 39 | 85 |
| **Total** | **47** | **175** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/39 * 85)
```

---

## What changed from v16 to v17

| | v16 | v17 |
|-|----|-----|
| Version | v16 | v17 |
| Source rounds | R1–R16 | R1–R17 |
| Aspirational count | 39 | 39 |
| Total criteria | 47 | 47 |
| Composite formula denominator | 39 | 39 |

**No new criteria from R17.**

R17 ran five variations (V-01 through V-05) against the v16 rubric. V-01 (full extension, all clusters) scored 175/175 — the first perfect score in the draft-spec series. All five excellence signals from R17 map to existing structure or scoring mechanics; none represents a structural gap without a criterion.

| Excellence signal | Disposition |
|-------------------|-------------|
| E-1: C-47 closes the final Phase 1.5 → Phase 2 chain gap | Confirms C-47 (v16) — not a new gap |
| E-2: Five extension clusters are independently stackable | Rubric design property — not a template criterion |
| E-3: N/A ceiling loss scores lower than partial cluster failure | Mathematical property of the fixed-denominator formula — not a template criterion |
| E-4: C-43 (ROLE markers) independent of C-41 (ENTER/EXIT ceremony) | Validates existing dependency graph — both criteria independently scoreable as designed |
| E-5: Essential-only floor (64.36) definitively below golden threshold (85) | Threshold calibration validation — not a template criterion |

**R17 JSON `new_patterns` disposition:**

| Pattern | Disposition |
|---------|-------------|
| Multi-input ENTER block (C-47) closes Phase 1.5 → Phase 2 chain gap | C-47 already in v16 |
| N/A ceiling loss < partial cluster failure (scoring asymmetry) | Mathematical property — not a template criterion |
| All five extension clusters independently composable | Rubric design property — not a template criterion |
| Essential-only floor well below golden threshold | Threshold calibration validation — not a template criterion |

**Why V-01's perfect score matters:** A 175/175 score against all five variation profiles (full extension, no ceremony, no Phase 1.5, no SQS + no Phase 1.5, essential-only) confirms the rubric's criterion set is complete for the current variation space. The N/A/FAIL asymmetry (E-3) and cluster independence (E-2) are correct-by-design properties, not gaps. The rubric is stable at 47 criteria until a new structural pattern appears in a future variation that no existing criterion addresses.

---

## N/A Rules

**C-36, C-37, C-45, C-46**: Inapplicable to templates without [STATUS-QUO-SNAPSHOT]. Cannot contribute to `aspirational_pass`. Fixed denominator = 39 for all variations.

**C-38, C-39, C-40, C-47**: Inapplicable to templates without a named fractional sub-phase emitting a second pre-Phase-2 gate token. Cannot contribute to `aspirational_pass`. Fixed denominator = 39 for all variations.

**C-41, C-42, C-43, C-44**: Applicable to all templates. No N/A condition.

A template satisfying none of the extension patterns (no [STATUS-QUO-SNAPSHOT], no Phase 1.5, no ENTER/EXIT ceremony, no second-person frame, no ROLE markers) achieves at most 27/39 aspirational points. A template with ENTER/EXIT ceremony and chained notation but no other extension clusters achieves at most 29/39. A 39/39 template combines all five extension clusters.

---

## Essential Criteria (60 pts total)

### C-01 — Five required numbered phases in prescribed order (12 pts)

The spec template contains all five required numbered phases — Phase 0, Phase 1 (PM PRE-ASSIGNMENT), Phase 2 (INERTIA ANALYSIS), Phase 3 (REQUIREMENTS), Phase 4 (AMENDMENTS) — present in that prescribed order. A template with missing phases, merged phases, or reordered phases does not satisfy. Fractional sub-phases (e.g., Phase 1.5) between numbered phases do not affect evaluation; C-01 passes when the five required numbered phases are in prescribed order regardless of sub-phases between them.

---

### C-02 — [SCOUT-STATUS-TABLE] with seven artifact rows in Phase 0 (12 pts)

A [SCOUT-STATUS-TABLE] block appears in Phase 0 and contains at minimum 7 rows covering the expected scout artifact types. Each row names the artifact type and a status field. A table with fewer rows, with catch-all rows substituting for individual artifact entries, or placed outside Phase 0 does not satisfy.

---

### C-03 — [PM-COVERAGE-TABLE] with required columns including Waiver Status (12 pts)

A [PM-COVERAGE-TABLE] block is present and includes a dedicated Waiver Status column with explicitly enumerated values (e.g., `"COVERED"` / `"C-03 WAIVER"`). A table without the Waiver Status column, or that handles waivers through inline prose notation, does not satisfy. This criterion is the upstream structural dependency for C-33, C-31, and C-10.

---

### C-04 — [IG-REGISTER] and [ID-REGISTER] in Phase 2 with minimum 2 IG-IDs (12 pts)

[IG-REGISTER] (inertia gaps) and [ID-REGISTER] (inertia decisions) are both present in Phase 2. [IG-REGISTER] contains at minimum 2 IG-ID rows. A template with only one register, or with an [IG-REGISTER] containing fewer than 2 IG-ID rows, does not satisfy.

---

### C-05 — Five guided sections in Phase 3 in prescribed order (12 pts)

Phase 3 (REQUIREMENTS) contains all five guided sections in their prescribed order. A Phase 3 section with missing sections, merged sections, or reordered sections does not satisfy.

---

## Recommended Criteria (30 pts total)

### C-06 — Fallback branches A, B-1/B-2/B-3, B-catch present in Phase 0 (10 pts)

Phase 0 contains a structured fallback tree with Branch A (ALL NOT FOUND), Branch B sub-branches B-1, B-2, B-3 (per-artifact conditionals), and a B-catch branch. All named branches must be present. A fallback structure missing any named branch does not satisfy.

---

### C-07 — VERBATIM RESPONSE blocks in each named fallback branch (10 pts)

Each named fallback branch (A, B-1, B-2, B-3, B-catch) contains a blockquoted VERBATIM RESPONSE block with complete scripted text. A fallback branch with paraphrase instructions, fill-in-blank templates, or a pointer to another block's response does not satisfy. Every named branch must have its own independent VERBATIM block.

---

### C-08 — All three gate tokens present ([PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE]) (10 pts)

The template defines all three named gate tokens: [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], and [SPEC-DRAFT-COMPLETE]. Each token must be named and defined with at minimum one INVALID IF invalidity rule. A template with anonymous gate concepts, placeholder token names, or fewer than three defined named tokens does not satisfy. Additional gate tokens (e.g., [STRATEGY-SCOPE-SEAL]) are additive and do not affect this criterion.

---

## Aspirational Criteria (85 pts total)

### C-09 — Waiver Status column named as structural element in [PM-COVERAGE-TABLE] (structure)

The Waiver Status column is declared as a named structural element in the [PM-COVERAGE-TABLE] block definition — not only referenced in surrounding prose or in a separate waiver protocol block. The column definition must appear within the [PM-COVERAGE-TABLE] structural definition itself. Requires C-03.

---

### C-10 — Waiver propagation rule named: C-03 WAIVER → "R-ID WAIVED" cell (traceability)

An explicit waiver propagation rule is declared: rows marked "C-03 WAIVER" in [PM-COVERAGE-TABLE] must propagate their waived status as an "R-ID WAIVED" cell marker in the corresponding [IG-REGISTER] Elimination Path cell. The rule must be named — a general instruction to "note waivers" without the named cell-marker propagation format does not satisfy.

---

### C-11 — [INERTIA-ANALYZED] Condition 1 and Condition 2 as distinct named invalidity paths (governance)

The [INERTIA-ANALYZED] gate token declares Condition 1 and Condition 2 as two structurally distinct named invalidity paths, each with its own named check. A token with a single combined invalidity rule covering both conditions does not satisfy. The named separation enables independent evaluation of structural completeness (Condition 1) and per-cell proof-of-work (Condition 2).

---

### C-12 — "Meeting Condition 1 without Condition 2 = invalid" stated explicitly (governance)

The [INERTIA-ANALYZED] gate token explicitly states that satisfying Condition 1 without also satisfying Condition 2 is an invalidity state — the token cannot be emitted on structural completeness alone. This declaration must appear in the token definition as a named rule, not implied by the conditions' enumeration.

---

### C-13 — Waiver chain closure: all three nodes named in sequence (traceability)

A named chain closure declaration co-located with [INERTIA-ANALYZED] names all three waiver traceability nodes in sequence: (1) [PM-COVERAGE-TABLE] WAIVER source, (2) "R-ID WAIVED" cell marker in [IG-REGISTER], (3) Condition 2 exemption in [INERTIA-ANALYZED]. A declaration that names only two nodes, or names all three in separate non-sequential statements, does not satisfy. Requires C-11 and C-10.

---

### C-14 — Risk amplification threshold named with two trigger conditions (depth)

The template names an AMPLIFIED row type in [IG-REGISTER] with an explicit amplification threshold declaring the two conditions that trigger AMPLIFIED status. A general "high-risk rows" annotation without a named threshold with two explicitly enumerated trigger conditions does not satisfy.

---

### C-15 — AMPLIFIED sub-slot format with two required named fields (depth)

AMPLIFIED Elimination Path cells use a pre-printed dual sub-slot template with named sub-slots — `Risk:` and `R-ID:` — each on its own line. A free-text Elimination Path field, a single combined label, or a field that requires the PM to manually format the sub-slots does not satisfy. Requires C-14.

---

### C-16 — Partial-population structural fail rule for AMPLIFIED sub-slots (depth)

An explicit partial-population structural fail rule is declared co-located with the AMPLIFIED sub-slot definition: a cell in which one or more sub-slots are populated while at least one other sub-slot is blank is a structural fail, not a content gap. A general completeness instruction without naming partial population as a structural-level failure does not satisfy. Requires C-15.

---

### C-17 — [PM-CONTRACT-SEAL] INVALID IF names both structural dependencies (governance)

The [PM-CONTRACT-SEAL] INVALID IF rule explicitly names both of its structural dependencies as invalidity conditions. A token with an INVALID IF rule naming only one structural dependency does not satisfy. Both dependencies must be named in the token definition itself — naming them only in surrounding prose does not satisfy.

---

### C-18 — Phase 2 blocked statement names [PM-CONTRACT-SEAL] as required (governance)

Phase 2 contains an explicit blocked statement declaring that Phase 2 cannot begin without [PM-CONTRACT-SEAL]: "→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL]" or equivalent. A Phase 2 section that references the token only in surrounding prose without a dedicated blocked/REQUIRES declaration does not satisfy. Requires C-17.

---

### C-19 — Phase 3 blocked statement names both [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED] (governance)

Phase 3 contains an explicit blocked statement naming both [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED] as required: "Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED]" or equivalent. A Phase 3 blocked statement naming only one of the two tokens does not satisfy.

---

### C-20 — [SPEC-DRAFT-COMPLETE] INVALID IF names missing seal dependencies by token name (governance)

The [SPEC-DRAFT-COMPLETE] INVALID IF rule explicitly names the upstream seal dependencies as invalidity conditions, referencing each by token name. An invalidity rule that references seals only by description or refers generically to "prior phases incomplete" without naming tokens does not satisfy.

---

### C-21 — Cross-namespace signal at Phase 1 (location 1 of 2) explicitly marked (traceability)

Phase 1 contains the cross-namespace signal row marked as "(location 1 of 2)". The ordinal marker must appear on the signal row or field itself — not only in the section header or surrounding prose. A cross-namespace signal row without the "(location 1 of 2)" marker does not satisfy.

---

### C-22 — Cross-namespace signal at Phase 3 Purpose section (location 2 of 2) explicitly marked (traceability)

The Phase 3 Purpose section contains the cross-namespace signal row marked as "(location 2 of 2)". The ordinal marker must appear on the signal row or field itself. A cross-namespace signal in Phase 3 without the "(location 2 of 2)" marker does not satisfy. Requires C-21.

---

### C-23 — [SPEC-DRAFT-COMPLETE] INVALID IF cross-namespace signal absent at both locations when artifact LOADED (governance)

[SPEC-DRAFT-COMPLETE]'s INVALID IF rule includes a condition for when the cross-namespace artifact is LOADED but the signal is absent at both named locations. "INVALID IF cross-namespace artifact is LOADED but the signal is absent at location 1 or location 2" or equivalent must be declared as a named invalidity condition. A token that validates signal presence only at one location, or only in aggregate, does not satisfy. Requires C-21 and C-22.

---

### C-24 — Contradiction scan with named range (R-01 through R-{n}) (depth)

Phase 3 contains a contradiction scan instruction naming the scan range as "R-01 through R-{n}" or an equivalent named range format. A contradiction check instruction without a named scan range does not satisfy. The range format enables traceability of what was scanned.

---

### C-25 — Active inspection guard in Phase 3 Requirements (depth)

Phase 3 includes an active inspection guard — an instruction prohibiting confirmation of "none found" without naming the scan source and range. "Do not confirm 'none found' without naming scan range" or equivalent anti-passive-confirmation constraint must be declared as a named rule. A general completeness instruction without this guard does not satisfy.

---

### C-26 — P0 coverage count confirmed in Phase 3 Requirements before narrative (structure)

Phase 3 includes an explicit P0 coverage count confirmation before any narrative prose: the number of P0 requirements carried forward is stated as a structural element. A Phase 3 section that proceeds to narrative without an explicit count confirmation does not satisfy.

---

### C-27 — Actor→action directives retain "PM: scan `scout-requirements` →" form (clarity)

All actor→action directives use the concise actor→action→output form with `→` binding throughout the template. Instructions using the descriptive "The PM should..." form or passive constructions in directive positions do not satisfy. Gate tokens and REQUIRES/PRODUCES headers are not subject to this criterion.

---

### C-28 — PM pre-assignment computationally precedes inertia analysis (Phase 1 before Phase 2) (ordering)

[PM-CONTRACT-SEAL] is emitted at Phase 1 exit and Phase 2 requires [PM-CONTRACT-SEAL] to begin — the ordering is computationally enforced, not merely prescribed by document structure. A template in which Phase 1 precedes Phase 2 in document order without the gate dependency does not satisfy. Requires C-17.

---

### C-29 — FINDINGS section with self-review scan list (minimum 6 named items) (structure)

The FINDINGS section contains a self-review scan list with at minimum 6 named scan items. Each item must be named — "scan for X" with X specified. A FINDINGS section with a generic "review all sections" instruction or fewer than 6 named items does not satisfy. Requires C-04.

---

### C-30 — Finding table with named finding types (coverage gaps, contradictions, complexity hotspots, OQ register) (structure)

The findings table in the FINDINGS section names at minimum these four finding types as defined column values or row types: coverage gaps, contradictions, complexity hotspots, open question (OQ) register entries. A findings table with generic "finding" rows without named type taxonomy does not satisfy. Requires C-04.

---

### C-31 — Phase 4 amendments specify minimum 2 items with section reference (structure)

Phase 4 (AMENDMENTS) contains at minimum 2 amendment items, each with an explicit section reference naming the section to be amended. An amendment list with fewer than 2 items, or with items that do not name the target section, does not satisfy.

---

### C-32 — Elimination Path format names "R-ID: [R-XX]" structure explicitly (traceability)

The Elimination Path field template in [IG-REGISTER] names the required format explicitly — "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" or equivalent named format — in the field definition or column header. A field with a free-text placeholder without a named format requirement does not satisfy.

---

### C-33 — C-03 WAIVER elimination path format named ("R-ID WAIVED (no requirements artifact)…") (traceability)

The Elimination Path field template includes a named format for C-03 WAIVER rows: "R-ID WAIVED (no requirements artifact)" or equivalent named marker format. The waiver elimination path format must be named separately from the standard R-ID format — a generic "see waiver" note does not satisfy. Requires C-32 and C-10.

---

### C-34 — [INERTIA-ANALYZED] INVALID IF phrases Condition 2 exemption for "R-ID WAIVED" cells (governance)

[INERTIA-ANALYZED] Condition 2 includes an explicit named exemption for "R-ID WAIVED" cells: cells marked "R-ID WAIVED" are exempt from the per-cell R-ID population check of Condition 2. The exemption must be named in the token's Condition 2 definition — a waiver notation in Phase 1 without a corresponding Condition 2 exemption in the token definition does not satisfy. Requires C-11.

---

### C-35 — CASCADE TO annotation in Phase 1 naming downstream consumers of [PM-COVERAGE-TABLE] (traceability)

Phase 1 includes a CASCADE TO annotation naming the downstream blocks that receive the PM's pre-assignments from [PM-COVERAGE-TABLE]: at minimum [IG-REGISTER] in Phase 2 and the cross-namespace signal row. The annotation must be co-located with the Phase 1 PM assignment directive — a general note about downstream use elsewhere in the template does not satisfy.

---

### C-36 — [INERTIA-ANALYZED] Condition 1 extended to [STATUS-QUO-SNAPSHOT] presence (depth)

The [INERTIA-ANALYZED] gate token's Condition 1 invalidity rule explicitly names [STATUS-QUO-SNAPSHOT] as a required presence check alongside [IG-REGISTER] and [ID-REGISTER]: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated." A gate token whose Condition 1 names only [IG-REGISTER] and [ID-REGISTER] without [STATUS-QUO-SNAPSHOT] does not satisfy, even if the template elsewhere defines [STATUS-QUO-SNAPSHOT] as required. The extension must appear as a named structural element in the token's invalidity rules — a surrounding prose note that the snapshot must be present does not satisfy. Without C-36, a gate token designed for the two-register model can pass Condition 1 while silently ignoring [STATUS-QUO-SNAPSHOT] absence; C-36 closes that gap at the token definition level. Applicable only to template variants that introduce the status-quo-first inertia pattern; a template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. Requires C-30.

Source signal: R13 V-02 — [INERTIA-ANALYZED] Condition 1 extended to: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated."

---

### C-37 — [STATUS-QUO-SNAPSHOT] row structural fail rule (depth)

The [STATUS-QUO-SNAPSHOT] block includes an explicit structural fail rule co-located with the row definition: a row with a named status-quo alternative but a blank gap statement is declared a structural fail, not a content gap. The rule must name the fail condition explicitly — a general completeness instruction ("all fields required") without naming the named-alternative-plus-blank-gap-statement pattern as a structural-level failure does not satisfy. A template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. C-36 can pass without C-37.

Source signal: R13 V-02 note — "A row with a named alternative but a blank gap statement is a structural fail" declared co-located with the [STATUS-QUO-SNAPSHOT] row definition.

---

### C-38 — Multi-token Phase 2 gate with dual named dependencies (governance)

Phase 2 declares REQUIRES for two named gate tokens from two distinct prior phases — specifically [PM-CONTRACT-SEAL] from Phase 1 AND a second named gate token (e.g., [STRATEGY-SCOPE-SEAL]) from a fractional sub-phase or additional phase that precedes Phase 2. Both tokens must be named explicitly in Phase 2's REQUIRES header or preamble: "Phase 2 begins after [PM-CONTRACT-SEAL] is present AND [STRATEGY-SCOPE-SEAL] is present" or the compressed equivalent ("→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]"). A Phase 2 REQUIRES declaration naming only [PM-CONTRACT-SEAL] does not satisfy; a second token named only in surrounding prose or in the second token's own definition without a corresponding Phase 2 REQUIRES does not satisfy. The pattern captures the case where a Strategy scoping step — or any equivalent pre-Phase-2 role insertion — is computationally enforced at the Phase 2 gate level, not merely noted as a prerequisite. Applicable only to templates that introduce a pre-Phase-2 role emitting its own named gate token; a template with no second pre-Phase-2 seal cannot be evaluated against this criterion. Requires C-17 and C-28.

Source signal: R13 V-05 — Phase 2 REQUIRES: "[PM-CONTRACT-SEAL] from Phase 1 AND [STRATEGY-SCOPE-SEAL] from Phase 1.5" — two named tokens from two distinct prior phases declared jointly in Phase 2's gate dependency.

---

### C-39 — Named fractional sub-phase between numbered phases with role and seal (structure)

The template includes at least one named fractional sub-phase (e.g., Phase 1.5) inserted between two consecutive numbered phases. Three conditions must all be satisfied: (1) all five required numbered phases from C-01 remain present in prescribed order — Phase 1.5 does not merge, replace, or reorder any required phase; (2) the sub-phase carries a descriptive header naming both its ordinal position and its role scope (e.g., "Phase 1.5 — STRATEGY INERTIA SCOPING"); (3) the sub-phase emits at minimum one named gate token. A new role inserted via a renamed or renumbered required phase does not satisfy. An unnumbered section between phases with no ordinal label does not satisfy. A sub-phase with a descriptive header but no emitted gate token does not satisfy. The numbered phase ordering contract of C-01 and the fractional sub-phase anatomy of C-39 are evaluated independently — C-01 passes when the five required phases are in order regardless of sub-phases between them; C-39 passes when a fractional sub-phase satisfies all three conditions. Requires C-01.

Source signal: R13 V-05 — Phase 1.5 (STRATEGY INERTIA SCOPING) inserted between Phase 1 and Phase 2; header names both ordinal (1.5) and role scope (STRATEGY INERTIA SCOPING); sub-phase emits [STRATEGY-SCOPE-SEAL]; all five C-01 phases remain in prescribed order unaffected.

---

### C-40 — Gate token invalidity rule cross-references co-located structural rule by name (depth)

A named gate token's INVALID IF rule explicitly names a co-located structural rule — defined within another block in the same template — as a required presence precondition: the token is invalid not only if the target block is absent, but if the named structural rule is absent from within that block. The cross-reference must identify both the target block and the specific rule it must contain (e.g., "[STRATEGY-SCOPE-SEAL] INVALID IF the [STATUS-QUO-SNAPSHOT] structural fail rule is absent from the [STATUS-QUO-SNAPSHOT] block definition"). A token that requires only block presence without naming the co-located rule as a precondition does not satisfy — C-36 covers block presence at Condition 1; C-40 captures the deeper dependency where the seal's validity requires a specific enforcement rule to be verifiably defined within another block. This pattern formalizes cross-block structural rule dependencies at the token-definition level: a seal that enforces structural correctness in a dependent block can only be validly emitted if that block's structural rule is actually present in the template. Applicable only to templates where a gate token's invalidity logic names a co-located structural rule in another block as a precondition. Requires C-37.

Source signal: R13 V-05 — [STRATEGY-SCOPE-SEAL] INVALID IF rule requires [STATUS-QUO-SNAPSHOT] presence AND the co-located structural fail rule co-located with the [STATUS-QUO-SNAPSHOT] row definition — the seal's invalidity logic names the C-37 structural rule as a precondition by reference, not merely the block containing it.

---

### C-41 — Phase ENTER/EXIT ceremony blocks at all numbered phase boundaries (structure)

Each of the five numbered phases (0 through 4) includes a formal ENTER block and a formal EXIT block at the phase boundary level. The ENTER block declares the precondition state — gate tokens required, artifacts loaded, or conditions that must be true — for the phase to begin. The EXIT block names the gate token emitted by this phase and any downstream cascade effects. Both blocks must appear at the phase boundary level as structurally labeled elements — not embedded in phase body prose, not implied by a REQUIRES header alone, not defined only in the gate token's own definition elsewhere in the template. A phase with an entry-condition sentence in the body prose but no structural ENTER block does not satisfy. A phase with an EXIT note in a gate token definition elsewhere but no EXIT block co-located at the phase boundary does not satisfy. The pattern formalizes phase transition computability: any processing agent can verify phase entry and exit conditions without parsing phase body content. Fractional sub-phases (C-39) may carry ENTER/EXIT blocks but are not evaluated by C-41; C-41 is evaluated against the five numbered phases only. Requires C-01.

Source signal: R14 V-01, V-04 — each of the five numbered phases (0, 1, 2, 3, 4) carries a formal ENTER block declaring required preconditions and an EXIT block naming the emitted gate token; phase transitions are fully computable from the ENTER/EXIT blocks without parsing phase body content.

---

### C-42 — Second-person transitional frame with preserved actor-directive separation (style)

Explanatory and transitional prose uses second-person frame — "you will", "your goal is", "you are now entering" — while actor→action directives retain the labeled third-person imperative form: "PM: scan `scout-requirements` →", "PM: assign...", "Architect: draft...". The two registers must be structurally distinct: second-person prose appears in explanatory framing, phase purpose statements, and transitional preambles; actor→action directives appear as their own labeled directive lines. Three conditions must all be satisfied: (1) second-person framing appears in multiple named phases, not confined to a single phase or preamble; (2) no actor→action directive uses second-person frame — C-27 compliance is a hard precondition; (3) the second-person frame is used for explanation and orientation, not to replace the actor-directive structure. A template that applies second-person frame to actor→action directives — replacing "PM: scan..." with "you will scan..." — does not satisfy and also fails C-27. A template that uses second-person frame only in a single section introduction or frontmatter note without recurring use across phase transitions does not satisfy. Requires C-27.

Source signal: R14 V-02, V-05 — second-person framing ("you will now...", "your goal is...", "you are entering...") used in phase purpose statements and transitional prose across multiple phases while all actor→action directives retain "PM: scan `scout-requirements` →" and equivalent labeled imperative forms throughout.

---

### C-43 — Explicit ROLE markers at numbered phase entry points naming active actors (governance)

Each numbered phase includes at minimum one → ROLE: [ACTOR] marker — or equivalent labeled role assignment element — appearing at phase entry before any phase body content, explicitly naming the role or roles active in that phase. Four conditions must be satisfied: (1) Phase 1 carries a single-actor marker (e.g., → ROLE: PM); (2) Phase 2 carries a multi-actor marker naming at least two roles (e.g., → ROLE: PM + ARCHITECT); (3) the markers appear as dedicated labeled structural elements at phase entry — not named only through actor→action directive labels embedded in the phase body, not defined only in a roles legend outside phase boundaries; (4) role assignments at the marker level are consistent with actor→action directives in the phase body — a marker naming only PM in a phase where the body names Architect directives does not satisfy. A template that identifies role assignments exclusively through actor→action directive labels ("PM: scan...", "Architect: draft...") without dedicated entry-level ROLE markers does not satisfy. Fractional sub-phases (C-39) may carry ROLE markers but are not evaluated by C-43. Requires C-01.

Source signal: R14 V-03 — → ROLE: PM marker at Phase 1 entry; → ROLE: PM + ARCHITECT at Phase 2 entry; role identities and prescribed phase ordering unaffected; structural ROLE markers appear at phase boundaries as distinct labeled elements consistent with phase body actor→action directives.

---

### C-44 — Chained ENTER/EXIT phase transition notation (structure)

The ENTER and EXIT blocks across all five numbered phases form an unbroken transition chain: each phase's ENTER precondition is exactly the artifact or token named in the prior phase's EXIT output, making the full phase sequence readable as a single transition graph without parsing phase body content. Three conditions must be satisfied: (1) each numbered phase's ENTER block names a precondition that matches — by name — the token or artifact declared in the preceding phase's EXIT block; (2) the chain is unbroken from Phase 0 through Phase 4 — a gap at any phase boundary does not satisfy; (3) a terminal phase whose EXIT produces an artifact rather than a gate token (e.g., Phase 4 producing an amendment list) still names the artifact in the EXIT block in the same structural position as prior phases name gate tokens, and Phase 4's named artifact appears as the precondition in Phase 4's own ENTER block. A template with ENTER/EXIT blocks at all five phase boundaries that do not cross-reference each other's named outputs and inputs does not satisfy — independent per-phase declarations without chained naming form a set of isolated blocks, not a computable transition graph. Requires C-41.

Source signal: R15 V-01 — Phase 0 (file access→table complete), Phase 1 (table complete→PM-CONTRACT-SEAL), Phase 2 (PM-CONTRACT-SEAL→INERTIA-ANALYZED), Phase 3 (both tokens→SPEC-DRAFT-COMPLETE), Phase 4 (SPEC-DRAFT-COMPLETE→amendment list); the EXIT of each phase is the ENTER precondition of the next, forming an unbroken named chain; Phase 4 EXIT names the artifact output ("amendment list") in the same structural position as prior phases name gate tokens.

---

### C-45 — Structural fail rule stated in dual form: negative declaration plus positive counterpart instruction (depth)

A structural fail rule co-located with the block it governs is declared in both negative form and positive form at the same structural location. The negative form names the fail condition ("A row with X but blank Y is a structural fail, not a content gap"). The positive form names the required behavior as an actionable directive ("Do not leave Y blank when X is populated" or equivalent). Both forms must appear co-located — a negative fail declaration in the block definition and a positive instruction placed elsewhere in the template does not satisfy. The dual form ensures the rule is both a compliance gate (negative) and an actionable directive (positive), making it self-contained and executable by a processing agent reading only the block definition. A structural fail rule stated only in negative form, or only in positive form, does not satisfy. Applicable only to templates containing the structural fail rule patterns governed by C-37. Requires C-37.

Source signal: R15 V-02 — [STATUS-QUO-SNAPSHOT] structural fail rule declared as: "A row with a named alternative but a blank Gap statement is a structural fail, not a content gap. Do not leave Gap blank when Alternative is populated." — negative fail declaration and positive directive co-located in the same structural element.

---

### C-46 — Invalidity rule scoped to "this phase block" for block presence checks (governance)

An invalidity rule that checks for block presence — "INVALID IF [BLOCK-NAME] is absent" — scopes the presence check to "this phase block" or an equivalent named scope: "INVALID IF [BLOCK-NAME] is absent from this phase block." The scoped phrasing closes a gap in presence-only rules: without scope qualification, a block defined elsewhere in the document could pass the check while failing to appear in the required phase location. Three conditions must be satisfied: (1) the INVALID IF rule names the target block by name; (2) the rule includes an explicit scope qualifier ("from this phase block", "within Phase N", or equivalent) naming where the block must appear; (3) the scope qualifier is part of the INVALID IF rule text itself — not a note in surrounding prose or a phase header that implies the scope. A gate token invalidity rule that checks for block presence without scope qualification does not satisfy, even if the phase structure makes the intended scope inferrable. Applicable only to templates where [INERTIA-ANALYZED] Condition 1 names block presence checks against blocks that could hypothetically be defined outside Phase 2; a template with globally unique block names that cannot drift in scope cannot be evaluated against this criterion. Requires C-36.

Source signal: R15 V-02 — [INERTIA-ANALYZED] Condition 1 phrased as "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated" — "from this phase block" scope qualifier prevents the presence check from being satisfied by a block defined outside Phase 2.

---

### C-47 — Multi-input ENTER block absorbs fractional sub-phase EXIT tokens into the named chain (structure)

When a named fractional sub-phase (C-39) sits between two consecutive numbered phases and carries its own ENTER/EXIT ceremony, the next numbered phase's ENTER block names gate tokens from ALL immediate predecessor phases — both the preceding numbered phase AND the fractional sub-phase — not only the numbered phase's token. Three conditions must be satisfied: (1) the ENTER block of the numbered phase following the fractional sub-phase names gate tokens from both the prior numbered phase and the fractional sub-phase by name, matching their respective EXIT block outputs; (2) the C-44 chain remains unbroken — no immediate predecessor EXIT token is unnamed in the successor ENTER block; (3) the multi-input ENTER declaration appears in the ENTER block itself as a named list of preconditions, not only in the gate dependency header (C-38) or the fractional sub-phase's own EXIT block. A Phase 2 ENTER block that names only the prior numbered phase's EXIT token (e.g., [PM-CONTRACT-SEAL]) while a Phase 1.5 has also emitted a gate token (e.g., [STRATEGY-SCOPE-SEAL]) does not satisfy — the chain is broken at the Phase 2 ENTER boundary because an immediate predecessor EXIT is absent from the absorption list. C-38 requires the gate dependency declaration; C-44 requires the five numbered phases to form a named chain; C-47 closes the gap where a fractional sub-phase's EXIT token is present in the gate dependency (C-38) but absent from the ENTER block's named chain (C-44). A template without a fractional sub-phase carrying ENTER/EXIT ceremony cannot be evaluated against this criterion. Requires C-44 and C-39.

Source signal: R16 V-05 — Phase 2 ENTER names both Phase 1 EXIT ([PM-CONTRACT-SEAL]) and Phase 1.5 EXIT ([STRATEGY-SCOPE-SEAL]); the five numbered phases' ENTER/EXIT chain remains unbroken because the Phase 2 ENTER block accumulates prior EXIT tokens from all feed sources including fractional sub-phases; C-44 scored PASS for the numbered phase chain, C-47 captures the additional requirement that fractional sub-phase EXIT tokens are explicitly absorbed into the ENTER block's named precondition list.
