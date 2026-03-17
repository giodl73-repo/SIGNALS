Now I have everything I need to score all five variations. Let me evaluate each against all 29 criteria.

---

# /quest:score — `draft-spec` — Round 9 (Rubric v9)

**Rubric**: v9 | **Variations**: V-01 through V-05 | **Date**: 2026-03-15

---

## Scoring Legend

- **PASS** — criterion met as written
- **PARTIAL** — partially met; scored as fail (aspirational are binary)
- **FAIL** — criterion not met

---

## V-01 — C-28 PM-Before-Inertia Gate (Minimal Base)

Base: REQUIRES/PRODUCES/BLOCKS syntax, merged [INERTIA-TABLE], Branch B single-block, no C-22/C-23/C-27/C-29.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-01** | Guided section structure preserved | **PASS** | Phase 3: Purpose → Requirements → Design → Constraints → Open Questions in order |
| **C-02** | Scout artifact status table present | **PASS** | [SCOUT-STATUS-TABLE] in Phase 0, 7 rows |
| **C-03** | P0 requirement coverage | **PASS** | [PM-COVERAGE-TABLE] with per-row assignment, explicit waiver clause |
| **C-04** | Self-review findings present | **PASS** | Phase 4 [FINDINGS-TABLE] + finding claim + [SELF-REVIEW-SEAL] |
| **C-05** | Artifact frontmatter complete | **PASS** | All fields: skill, topic, item, date, skill_version, input |
| **C-06** | Secondary role validation | **PASS** | Inline validations in Requirements, Design (Strategy), Constraints (Compliance) |
| **C-07** | Contradiction detection | **PASS** | Contradiction scan in Phase 1 with R-ID pair format |
| **C-08** | Actionable amendment list | **PASS** | Phase 5 with Section/Finding/Change format, min 2 items |
| **C-09** | No-scout fallback documented | **PASS** | Branch A named conditional in Phase 0 |
| **C-10** | Cross-namespace coherence | **PASS** | Cross-namespace signal table in Phase 1 with source artifact + spec impact |
| **C-11** | Pre-printed cross-namespace column | **FAIL** | Phase 1 has table but Purpose section has only prose instruction ("Name the strongest..."); no pre-printed column in Purpose or Design |
| **C-12** | Role annotations inline | **PASS** | "Secondary role validation (Requirements): [role name] — PASS / FINDING" inline within each section |
| **C-13** | Per-row P0 status column | **PASS** | Requirements table has Spec Entry column with "exact name from [PM-COVERAGE-TABLE]" |
| **C-14** | Active inspection guard | **PASS** | Contradiction scan requires "none found after scanning R-01 through R-{n}" format |
| **C-15** | Cross-namespace signal in two locations | **FAIL** | Only one structural location (Phase 1 table); Purpose instruction is prose, not a pre-printed field |
| **C-16** | PM-first coverage pre-assignment | **PASS** | Phase 1 pre-assigns rows before Phase 3 prose writing; gate blocks writing until pre-assignment done |
| **C-17** | Named progression gate token | **PASS** | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL] all blocking |
| **C-18** | Scripted verbatim fallback | **PASS** | Branch A and Branch B both have VERBATIM RESPONSE blocks with scripted copy |
| **C-19** | Ordinal location markers | **FAIL** | No "location 1 of 2 / 2 of 2" markers; cross-namespace field only in one location |
| **C-20** | Unified role-and-source declaration | **FAIL** | REQUIRES/PRODUCES/BLOCKS syntax — no instruction combining named role + named source in single directive |
| **C-21** | Gate token proof-of-work validity rule | **PASS** | [PM-CONTRACT-SEAL]: "INVALID IF emitted without [PM-COVERAGE-TABLE] present"; proof-of-work language present |
| **C-22** | Split inertia registers | **FAIL** | Single merged [INERTIA-TABLE] — explicitly minimal base |
| **C-23** | Responsible Role column | **FAIL** | [INERTIA-TABLE] columns: IG-ID / Hypothesis / Elimination Path / Risk Signal / Mitigation Required / Verdict — no role column |
| **C-24** | CASCADE TO annotations | **FAIL** | No CASCADE TO annotations present |
| **C-25** | Two-branch fallback with VERBATIM blocks | **PASS** | Branch A (all NOT FOUND) and Branch B (requirements absent, others loaded) both with VERBATIM RESPONSE |
| **C-26** | Per-artifact Branch B sub-conditionals | **FAIL** | Single Branch B block, no B-1/B-2/B-3/B-4 sub-conditions |
| **C-27** | Imperative phrasing register | **FAIL** | Declarative REQUIRES/PRODUCES/BLOCKS syntax only; criterion explicitly states this does not satisfy |
| **C-28** | PM pre-assignment before inertia | **PASS** | Phase 2 REQUIRES header names "[PM-CONTRACT-SEAL] from Phase 1 — if absent, halt"; structural gate enforces ordering |
| **C-29** | Elimination Paths reference R-IDs | **FAIL** | Intentionally absent; Elimination Path column: "[why it fails to satisfy the spec need]" — no R-ID requirement |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 11/21 → 44.5 pts

**V-01 Composite: 134.5 / 175**

---

## V-02 — C-29 Elimination Path Inline R-ID Slots (on V-01 base)

Base: V-01 + mandatory "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" sub-slot in each Elimination Path cell. AMPLIFIED rows require risk dimension + R-ID both.

All V-01 criteria carry forward unchanged. Changes:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-29** | Elimination Paths reference R-IDs | **PASS** | Elimination Path format: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]"; AMPLIFIED rows: risk dimension + R-ID both required; "A generic functional description without a named R-ID does not satisfy"; [INERTIA-ANALYZED] invalidity rule updated to check R-ID population; C-03 WAIVER rows carry "R-ID WAIVED" |

All other criteria: unchanged from V-01. C-11/C-15/C-19/C-20/C-22/C-23/C-24/C-26/C-27 all still FAIL (minimal base).

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 12/21 → 48.6 pts

**V-02 Composite: 138.6 / 175**

---

## V-03 — C-29 Separate "Req Closed" Column Format (on V-01 base)

Base: V-01 + dedicated "Req Closed (from [PM-COVERAGE-TABLE])" column in [INERTIA-TABLE]. Elimination Path carries functional prose; R-IDs go in the separate column.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-29** | Elimination Paths reference R-IDs | **FAIL** | C-29 requires "Each **Elimination Path cell**...names at least one specific requirement ID." V-03 places R-IDs in a separate "Req Closed" column — the Elimination Path cell itself has only functional prose ("functional reason...no R-IDs here"). Strict criterion text requires the R-ID in the Elimination Path cell. AMPLIFIED rows: V-03 puts risk dimension in Elimination Path (correct) but R-ID in separate column (fails AMPLIFIED dual requirement in Elimination Path cell). Column-format traceability is structurally stronger for visibility but does not satisfy the specific cell-level requirement |

All other criteria: identical to V-01.

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 11/21 → 44.5 pts

**V-03 Composite: 134.5 / 175**

> **V-03 = V-01 score.** The column format isolates traceability visually but fails C-29 on letter — the criterion names the Elimination Path cell as the required location. V-02's inline sub-slot is the stronger format for satisfying C-29.

---

## V-04 — C-28+C-29 Combined (R8 V-04 base: split registers, C-22/C-23/C-26/C-27; no C-24)

Full R8 V-04 base preserved: split [IG-REGISTER]/[ID-REGISTER], Responsible Role column, Branch B B-1 through B-4 sub-conditions with anti-blend, imperative phrasing. Added: C-28 gate + C-29 R-IDs. Missing: C-24 CASCADE TO.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-01** | Guided section structure | **PASS** | Phase 4: 5 sections in order |
| **C-02** | Scout artifact status table | **PASS** | Phase 0 [SCOUT-STATUS-TABLE] |
| **C-03** | P0 requirement coverage | **PASS** | [PM-COVERAGE-TABLE] in Phase 1, waiver clause |
| **C-04** | Self-review findings | **PASS** | Phase 5 [FINDINGS-TABLE] + finding claim |
| **C-05** | Frontmatter complete | **PASS** | All fields present |
| **C-06** | Secondary role validation | **PASS** | Strategy and Compliance inline verdicts in sections |
| **C-07** | Contradiction detection | **PASS** | [CONTRADICTION-SCAN] with "Do not confirm 'none found' without reviewing" guard |
| **C-08** | Actionable amendment list | **PASS** | Phase 6, min 2 items, Section/Finding/Change format |
| **C-09** | No-scout fallback | **PASS** | Branch A VERBATIM RESPONSE |
| **C-10** | Cross-namespace coherence | **PASS** | [CNS-SLOT-1-OF-2] in Phase 1 + [CNS-SLOT-2-OF-2] in Purpose — named source artifact |
| **C-11** | Pre-printed cross-namespace column | **PASS** | "[CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal]" as a named row in the Purpose table — omission is visually immediate |
| **C-12** | Role annotations inline | **PASS** | "Strategy inline verdict (Requirements/Design): PASS / FINDING" embedded within sections; "Compliance inline verdict" in Constraints |
| **C-13** | Per-row P0 status column | **PASS** | Requirements table with Spec Entry + Status per row |
| **C-14** | Active inspection guard | **PASS** | [CONTRADICTION-SCAN]: "Do not confirm 'none found' without reviewing the requirements artifact. State which rows were inspected." |
| **C-15** | Cross-namespace signal in two locations | **PASS** | [CNS-SLOT-1-OF-2] in Phase 1 and [CNS-SLOT-2-OF-2] in Purpose — structurally independent locations |
| **C-16** | PM-first coverage pre-assignment | **PASS** | "**PM: scan `{topic}-requirements-{date}.md` → enumerate P0 requirements → fill [PM-COVERAGE-TABLE].**" pre-assigns before prose writing |
| **C-17** | Named progression gate token | **PASS** | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [STRATEGY-SEAL], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL] |
| **C-18** | Scripted verbatim fallback | **PASS** | Branch A + Branch B B-1 through B-4 each with VERBATIM RESPONSE |
| **C-19** | Ordinal location markers | **PASS** | "[CNS-SLOT-1-OF-2]" labels "location 1 of 2"; "[CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2" — ordinal denominators present |
| **C-20** | Unified role-and-source declaration | **PASS** | "**PM: scan `{topic}-requirements-{date}.md` → enumerate P0 requirements → fill [PM-COVERAGE-TABLE].**" — names PM (role) + named source artifact + output in single directive; satisfies "Role X inspects Source Y before confirming Z" form |
| **C-21** | Gate token proof-of-work validity rule | **PASS** | [PM-CONTRACT-SEAL]: "INVALID IF emitted without ALL of the following...Proof-of-work: presence certifies all three outputs present and non-empty"; [INERTIA-ANALYZED], [STRATEGY-SEAL] also have invalidity rules |
| **C-22** | Split inertia registers | **PASS** | [IG-REGISTER] (hypothesis + Elimination Path) and [ID-REGISTER] (defeat + risk + verdict) are separate tables |
| **C-23** | Responsible Role column | **PASS** | [IG-REGISTER] includes "Responsible Role" column |
| **C-24** | CASCADE TO annotations | **FAIL** | PM directives do not carry "CASCADE TO:" annotation — no explicit downstream phase named in unified declarations |
| **C-25** | Two-branch fallback | **PASS** | Branch A + Branch B present with VERBATIM blocks |
| **C-26** | Per-artifact Branch B sub-conditionals | **PASS** | B-1 (feasibility only), B-2 (compliance only), B-3 (both), B-4 (market/positioning); "Do not blend sub-condition copy; emit the matching block verbatim" anti-blend instruction co-located |
| **C-27** | Imperative phrasing register | **PASS** | "**PM: scan [source] → [action] → fill [target].**" form used in Phase 1, Phase 2, Phase 3 — actor-action-output binding; at least two instances |
| **C-28** | PM pre-assignment before inertia | **PASS** | Phase 2 REQUIRES header: "REQUIRES: [PM-CONTRACT-SEAL] from Phase 1 — if absent, halt" |
| **C-29** | Elimination Paths reference R-IDs | **PASS** | [IG-REGISTER] Elimination Path format: "R-XX (from [PM-COVERAGE-TABLE]): [reason]"; AMPLIFIED: "AMPLIFIED: [risk dimension] — R-XX: [reason]"; "A generic elimination without a named R-ID is a structural fail for that row" |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 20/21 → 80.95 pts

**V-04 Composite: 171.0 / 175**

Single miss: C-24 (CASCADE TO absent from unified declarations).

---

## V-05 — Full Combination (Target 175/175)

V-04 base + CASCADE TO annotations co-located on all unified role-source declarations.

All V-04 criteria carry forward. Change:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-24** | CASCADE TO annotations on unified declarations | **PASS** | "**PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE].** CASCADE TO: [IG-REGISTER] Elimination Paths in Phase 2 (R-IDs must be drawn from this table)." — co-located annotation on the same structural line; similarly on [CNS-SLOT-1-OF-2] directive: "CASCADE TO: Purpose section [CNS-SLOT-2-OF-2] in Phase 4 (must match content)"; [CONTRADICTION-SCAN] directive: "CASCADE TO: Open Questions in Phase 4 if unresolved pairs found"; [IG-REGISTER] directive: "CASCADE TO: Design section IG-ID mitigation table in Phase 4" |

**All 29 criteria: PASS**

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 21/21 → 85 pts

**V-05 Composite: 175 / 175**

---

## Composite Score Summary

| Variation | Essential | Recommended | Asp Pass | Asp Pts | **Total** | Golden? |
|-----------|-----------|-------------|----------|---------|-----------|---------|
| V-01 | 60 (5/5) | 30 (3/3) | 11/21 | 44.5 | **134.5** | No |
| V-02 | 60 (5/5) | 30 (3/3) | 12/21 | 48.6 | **138.6** | No |
| V-03 | 60 (5/5) | 30 (3/3) | 11/21 | 44.5 | **134.5** | No |
| V-04 | 60 (5/5) | 30 (3/3) | 20/21 | 81.0 | **171.0** | No |
| V-05 | 60 (5/5) | 30 (3/3) | 21/21 | 85.0 | **175.0** | **YES** |

**Golden threshold**: all essential pass AND composite >= 85. V-05 is the sole golden variation.

---

## Rank

1. **V-05** — 175.0 (all 29 criteria)
2. **V-04** — 171.0 (C-24 miss only)
3. **V-02** — 138.6 (C-28 + C-29 on minimal base; still missing 9 aspirational)
4. **V-01** — 134.5 (C-28 only; C-29 absent)
4. **V-03** — 134.5 (C-28 only; C-29 column format fails strict cell requirement)

---

## Criteria Gap Map (V-01 to V-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Pre-printed CNS column in Purpose/Design | FAIL | FAIL | FAIL | PASS | PASS |
| C-15 CNS in two locations | FAIL | FAIL | FAIL | PASS | PASS |
| C-19 Ordinal location markers | FAIL | FAIL | FAIL | PASS | PASS |
| C-20 Unified role-and-source declaration | FAIL | FAIL | FAIL | PASS | PASS |
| C-22 Split inertia registers | FAIL | FAIL | FAIL | PASS | PASS |
| C-23 Responsible Role column | FAIL | FAIL | FAIL | PASS | PASS |
| C-24 CASCADE TO annotations | FAIL | FAIL | FAIL | FAIL | PASS |
| C-26 Branch B sub-conditionals | FAIL | FAIL | FAIL | PASS | PASS |
| C-27 Imperative phrasing | FAIL | FAIL | FAIL | PASS | PASS |
| C-28 PM before inertia gate | PASS | PASS | PASS | PASS | PASS |
| C-29 Elimination Path R-IDs | FAIL | PASS | FAIL | PASS | PASS |

---

## Excellence Signals (from V-05)

**Signal 1 — PM-first gate dependency closes the C-28/C-29 loop**: The [PM-CONTRACT-SEAL] in Phase 2's REQUIRES header is not just positional ordering — it makes the R-IDs available at inertia-write time. This creates a verifiable closed loop: PM assigns R-IDs in Phase 1 → gate token certifies assignment is complete → Phase 2 Elimination Paths draw from the now-available table. Without C-28, C-29 would require the model to self-reference IDs that may not yet be structured; with C-28, the IDs are contractually present.

**Signal 2 — CASCADE TO annotation as downstream chain documentation**: V-05's imperative directives carry a "CASCADE TO:" annotation naming the exact downstream structural element that consumes the output. This makes the data flow a first-class documented contract rather than an implied connection. The annotation is co-located on the same directive line, not in a separate section — the reader does not need to trace the document to know where the output lands.

**Signal 3 — V-03 column format is structurally visible but fails the cell-level criterion**: V-03 demonstrates that a dedicated "Req Closed" column is visually superior for detecting omissions (blank cell vs. missing sub-slot in prose), but C-29 names the Elimination Path cell as the required location. The better design may be V-02's inline sub-slot — it satisfies the criterion AND keeps all elimination reasoning co-located in one cell. V-03 is a valid hypothesis that identified an ergonomic tradeoff, not a scoring win.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["PM-first gate dependency ([PM-CONTRACT-SEAL] in Phase 2 REQUIRES header) closes the C-28/C-29 loop by making pre-assigned R-IDs structurally available at inertia-write time", "CASCADE TO annotations co-located on unified role-source directives document the downstream data chain as a first-class structural contract"]}
```
