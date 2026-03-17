# Quest Score — `draft-spec` — Round 10 (Rubric v10)

---

## V-01 — Axis: C-30 Gate Token Column-Content Check (Minimal Base)

### Essential (5/5 → 60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | All five sections present in order (Phase 3: Purpose→Requirements→Design→Constraints→Open Questions) |
| C-02 | **PASS** | [SCOUT-STATUS-TABLE] with 7 artifact rows in Phase 0 before any EXECUTE content |
| C-03 | **PASS** | [PM-COVERAGE-TABLE] in Phase 1 with "P0 coverage count: {n}/{n} assigned" and C-03 waiver path |
| C-04 | **PASS** | Phase 4 [FINDINGS-TABLE] + explicit "Finding claim:" required |
| C-05 | **PASS** | Frontmatter block present with all required fields; `{topic}-spec-{date}.md` naming |

### Recommended (3/3 → 30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Requirements, Design, Constraints all have named secondary role annotations inline |
| C-07 | **PASS** | Contradiction scan names R-ID pairs by format (e.g., "R-06 vs R-10"); Phase 4 self-review surfaces unresolved pairs |
| C-08 | **PASS** | Phase 5 INVALID IF fewer than 2 items; format requires section + finding ID + specific change |

### Aspirational (13/24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Branch A (ALL NOT FOUND) + Branch B (requirements absent) both present as named conditionals with HALT |
| C-10 | PASS | Cross-namespace signal table in Phase 1 names source artifact + spec impact |
| C-11 | **FAIL** | Purpose says "Name the strongest non-requirements signal…" — prose instruction only, no pre-printed row in template |
| C-12 | PASS | Role annotations inline in Requirements, Design, Constraints sections |
| C-13 | PASS | Requirements table in Phase 3 maps each R-ID to named Spec Entry column |
| C-14 | PASS | Contradiction scan names source ("all P0 rows in scout-requirements"), provides "R-XX vs R-YY" format, states scan scope |
| C-15 | **FAIL** | Cross-namespace signal at only 1 structural location (Phase 1 table); Purpose has prose instruction not pre-printed row |
| C-16 | PASS | PM pre-assigns each R-ID to section + entry name before prose writing; Architect fills pre-assigned rows |
| C-17 | PASS | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE], [SELF-REVIEW-SEAL] all present; downstream phases name gate artifacts |
| C-18 | PASS | Branch A has demarcated VERBATIM RESPONSE block; Branch B has VERBATIM RESPONSE block |
| C-19 | **FAIL** | No ordinal markers on multi-instance fields; cross-namespace signal has no "location 1 of 2 / 2 of 2" labels |
| C-20 | **FAIL** | No unified role+source declaration; contradiction scan names source but no role; no imperative "PM: scan X → confirm Y" form |
| C-21 | PASS | [PM-CONTRACT-SEAL] INVALID IF without [PM-COVERAGE-TABLE]; [INERTIA-ANALYZED] INVALID IF conditions not met — both are explicit invalidity rules |
| C-22 | **FAIL** | Single merged [INERTIA-TABLE] — not split into [IG-REGISTER]/[ID-REGISTER] |
| C-23 | **FAIL** | [INERTIA-TABLE] columns: IG-ID / Hypothesis / Elimination Path / Risk Signal / Mitigation Required / Verdict — no Responsible Role column |
| C-24 | **FAIL** | No CASCADE TO annotations on any unified declaration |
| C-25 | PASS | Branch A + Branch B both named with dedicated VERBATIM RESPONSE blocks |
| C-26 | **FAIL** | Branch B has single VERBATIM block — no per-artifact sub-conditions B-1/B-2/B-3/B-4, no anti-blend instruction |
| C-27 | **FAIL** | No imperative actor-action-output role-phase instructions; no "PM: scan X → fill Y" form |
| C-28 | PASS | Phase 1 produces [PM-CONTRACT-SEAL]; Phase 2 REQUIRES [PM-CONTRACT-SEAL] — structural ordering enforced |
| C-29 | PASS | Elimination Path format: "R-ID: [R-XX from [PM-COVERAGE-TABLE]] —" required; generic descriptions fail |
| C-30 | PASS | [INERTIA-ANALYZED] names Condition 1 (table presence) + Condition 2 (column-level R-ID); "Meeting Condition 1 without Condition 2 renders this token invalid" |
| C-31 | **FAIL** | Waiver handling is behavioral note only ("Mark the cell 'R-ID WAIVED'…"); no structural propagation rule declared in Phase 1; no Waiver Status column in [PM-COVERAGE-TABLE]; no explicit chain closure beyond exemption note |
| C-32 | **FAIL** | AMPLIFIED format is prose instruction: "the cell must also name the specific risk dimension… before the R-ID reference" — no pre-printed labeled sub-slots in template |

**V-01 Composite: 60 + 30 + (13/24 × 85) = 90 + 46.0 = 136.0**
Golden: YES (all essential pass; composite 136 ≥ 85)

---

## V-02 — Axis: C-32 AMPLIFIED Dual Sub-Slot (on V-01 base)

All V-01 criteria carry forward identically. Only difference: AMPLIFIED row template.

### Essential/Recommended: 5/5 + 3/3 (same as V-01)

### Aspirational delta from V-01:

| ID | Result | Evidence |
|----|--------|----------|
| C-32 | **PASS** | [INERTIA-TABLE] template pre-prints two labeled sub-slots as a code block: `Risk: [feasibility constraint or compliance gap...]` and `R-ID: [R-XX from [PM-COVERAGE-TABLE]...]`; "A combined prose statement… does not satisfy"; "Each sub-slot is structurally required — a cell with only 'Risk:' populated and 'R-ID:' blank is a structural fail" |

All other aspirational criteria unchanged: C-31 still FAIL (behavioral note waiver, no structural propagation rule).

**V-02 Aspirational: 14/24**
**V-02 Composite: 60 + 30 + (14/24 × 85) = 90 + 49.6 = 139.6**
Golden: YES

---

## V-03 — Axis: C-31 Waiver Propagation Structural Rule (on V-01 base)

All V-01 criteria carry forward identically. Only difference: waiver handling in Phase 1 + [PM-COVERAGE-TABLE] + [INERTIA-ANALYZED].

### Essential/Recommended: 5/5 + 3/3 (same as V-01)

### Aspirational delta from V-01:

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | **PASS** | Phase 1 declares "**Waiver propagation rule (structural):**" — named structural rule covering all affected IG-IDs without per-row judgment; [PM-COVERAGE-TABLE] adds Waiver Status column with "COVERED / C-03 WAIVER"; [INERTIA-ANALYZED] closes chain: "Chain closed: [PM-COVERAGE-TABLE] waiver → 'R-ID WAIVED' cell marker in [INERTIA-TABLE] → explicit Condition 2 exemption here" |
| C-32 | **FAIL** | AMPLIFIED format remains combined prose: "AMPLIFIED: [risk dimension from scout-feasibility or scout-compliance] — R-ID: [R-XX from [PM-COVERAGE-TABLE]] — [reason]" — single unlabeled statement, no pre-printed sub-slots |

**V-03 Aspirational: 14/24**
**V-03 Composite: 60 + 30 + (14/24 × 85) = 90 + 49.6 = 139.6**
Golden: YES

---

## V-04 — C-30+C-31+C-32 Combined (R9 V-04 base: split registers, C-22/C-23/C-26/C-27)

### Essential (5/5 → 60 pts) — all PASS, same as V-01

### Recommended (3/3 → 30 pts) — all PASS, same as V-01

### Aspirational (20/24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Branch A + Branch B both present |
| C-10 | PASS | Cross-namespace signal table in Phase 1 with source artifact |
| C-11 | **FAIL** | Purpose in Phase 3 says "Name the strongest non-requirements signal influencing this purpose statement and its source artifact" — prose instruction, no pre-printed named row |
| C-12 | PASS | "Strategy inline verdict (Requirements): PASS / FINDING" inline in section 2; same for Design and Constraints |
| C-13 | PASS | Requirements table maps each R-ID to Spec Entry with COVERED/WAIVED status |
| C-14 | PASS | "Do not confirm 'none found' without reviewing the requirements artifact. State which rows were inspected." — named inspection prohibition + source |
| C-15 | **FAIL** | Cross-namespace signal only in Phase 1 table; Purpose section has prose instruction not pre-printed row; 1 location, not 2 |
| C-16 | PASS | "PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE]" pre-assigns before prose writing |
| C-17 | PASS | Four named gate tokens; downstream phases name prerequisites |
| C-18 | PASS | Both Branch A and Branch B have VERBATIM RESPONSE blocks |
| C-19 | **FAIL** | No ordinal location markers; cross-namespace signal has no "location 1 of 2" labels |
| C-20 | PASS | "PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE]" — role (PM) + data source (requirements artifact) + output in single structural block |
| C-21 | PASS | All four gate tokens have explicit INVALID IF invalidity rules |
| C-22 | PASS | [IG-REGISTER] (Guards) and [ID-REGISTER] (Defeats) are structurally separate tables; row counts must match |
| C-23 | PASS | [IG-REGISTER] has "Responsible Role" column in table definition; "Responsible Role blank = structural fail" |
| C-24 | **FAIL** | No CASCADE TO annotations on unified declarations; axis map explicitly notes "no C-24" |
| C-25 | PASS | Branch A + Branch B with dedicated VERBATIM RESPONSE blocks |
| C-26 | PASS | B-1/B-2/B-3/B-4 sub-conditions each with VERBATIM RESPONSE block; "Do not blend sub-condition copy; emit the matching block verbatim" |
| C-27 | PASS | "PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE]"; "PM: scan `scout-feasibility` AND `scout-compliance` → record risk level → populate [IG-REGISTER] and [ID-REGISTER]" — both actor-action-output imperative |
| C-28 | PASS | Phase 1 produces [PM-CONTRACT-SEAL]; Phase 2 REQUIRES [PM-CONTRACT-SEAL] |
| C-29 | PASS | "STANDARD Elimination Path: 'R-XX (from [PM-COVERAGE-TABLE]):…'" required; AMPLIFIED format requires R-ID sub-slot |
| C-30 | PASS | [INERTIA-ANALYZED] Condition 1 (register integrity) + Condition 2 (column-level R-ID); WAIVED exemption via explicit marker only |
| C-31 | PASS | Structural waiver propagation rule declared in Phase 1; Waiver Status column in [PM-COVERAGE-TABLE]; chain closure in [INERTIA-ANALYZED]: "Chain closed: [PM-COVERAGE-TABLE] waiver → [IG-REGISTER] 'R-ID WAIVED' marker → Condition 2 exemption here" |
| C-32 | PASS | [IG-REGISTER] AMPLIFIED rows carry pre-printed sub-slots as code block: `Risk: [feasibility constraint…]` / `R-ID: [R-XX from [PM-COVERAGE-TABLE]…]`; "A combined single-line statement does not satisfy C-32" |

**V-04 Aspirational: 20/24** (C-11, C-15, C-19, C-24 fail)
**V-04 Composite: 60 + 30 + (20/24 × 85) = 90 + 70.8 = 160.8**
Golden: YES

---

## V-05 — Full Combination — Target 175/175

### Essential (5/5 → 60 pts) — all PASS

### Recommended (3/3 → 30 pts) — all PASS

### Aspirational (24/24 → 85 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Branch A + Branch B as named conditionals with HALT |
| C-10 | PASS | [CNS-SLOT-1-OF-2] in Phase 1 names source artifact + spec impact |
| C-11 | PASS | Purpose section (Phase 4) has pre-printed named row: `| [CNS-SLOT-2-OF-2] Cross-namespace signal, location 2 of 2 | [name artifact + 1-sentence signal…] |` — structurally present; blank is immediately visible |
| C-12 | PASS | "Strategy inline verdict (Requirements):", "Strategy inline verdict (Design):", "Compliance inline verdict:" all inline within respective section blocks |
| C-13 | PASS | Requirements table maps each R-ID to Spec Entry name by row; per-row Status column |
| C-14 | PASS | [CONTRADICTION-SCAN] with "Do not confirm 'none found' without reviewing the requirements artifact. State which rows were inspected." — named source + prohibition on default |
| C-15 | PASS | [CNS-SLOT-1-OF-2] in Phase 1 + [CNS-SLOT-2-OF-2] pre-printed in Purpose section = two structurally independent locations; "location 1 of 2 / 2 of 2" labels confirm deliberate design |
| C-16 | PASS | "PM: scan requirements → enumerate all P0 → fill [PM-COVERAGE-TABLE]. CASCADE TO: [IG-REGISTER] Elimination Paths" — PM pre-assigns before Architect writes |
| C-17 | PASS | Four gate tokens; [PM-CONTRACT-SEAL] names all four prerequisites; Phase 2 REQUIRES names [PM-CONTRACT-SEAL]; Phase 4 REQUIRES names [STRATEGY-SEAL] + [PM-CONTRACT-SEAL] + [INERTIA-ANALYZED] |
| C-18 | PASS | Branch A VERBATIM RESPONSE block; Branch B per-sub-condition VERBATIM blocks |
| C-19 | PASS | [CNS-SLOT-1-OF-2] labeled "location 1 of 2"; [CNS-SLOT-2-OF-2] labeled "location 2 of 2" with count denominator; completeness verifiable by counting labeled instances |
| C-20 | PASS | "PM: scan `{topic}-requirements-{date}.md` → enumerate all P0 requirements → fill [PM-COVERAGE-TABLE]. CASCADE TO: [IG-REGISTER]…" — role (PM) + named source artifact + output in single structural block |
| C-21 | PASS | All four gate tokens have explicit INVALID IF rules with prerequisite evidence conditions |
| C-22 | PASS | [IG-REGISTER] and [ID-REGISTER] are separate tables with "row count must equal" cross-check |
| C-23 | PASS | [IG-REGISTER] has Responsible Role column in table definition |
| C-24 | PASS | Multiple CASCADE TO annotations co-located with unified declarations: CASCADE TO [IG-REGISTER], CASCADE TO Purpose [CNS-SLOT-2-OF-2], CASCADE TO Open Questions, CASCADE TO Design and Constraints, CASCADE TO Design IG-ID mitigation table |
| C-25 | PASS | Branch A + Branch B both named with VERBATIM RESPONSE blocks |
| C-26 | PASS | B-1/B-2/B-3/B-4 each with VERBATIM RESPONSE; "Do not blend sub-condition copy; emit the matching block verbatim" |
| C-27 | PASS | Multiple imperative actor-action-output instructions: "PM: scan X → enumerate Y → fill Z", "Strategy: inspect X → validate Y → record Z", "Compliance: inspect X against Y → validate Z → record W" |
| C-28 | PASS | Phase 1 produces [PM-CONTRACT-SEAL]; Phase 2 REQUIRES [PM-CONTRACT-SEAL] from Phase 1 |
| C-29 | PASS | STANDARD: "R-XX (from [PM-COVERAGE-TABLE]):…"; AMPLIFIED: R-ID sub-slot required independently; WAIVED: explicit marker required |
| C-30 | PASS | [INERTIA-ANALYZED] Condition 2: "INVALID IF any Elimination Path cell in [IG-REGISTER] lacks a named R-ID AND does not carry an explicit 'R-ID WAIVED' marker… For AMPLIFIED rows: Condition 2 checks the 'R-ID:' sub-slot specifically" |
| C-31 | PASS | Structural propagation rule in Phase 1 with Waiver Status column; [INERTIA-ANALYZED] chain closure: "[PM-COVERAGE-TABLE] 'C-03 WAIVER' → [IG-REGISTER] 'R-ID WAIVED' marker → Condition 2 exemption here. A template that carries 'R-ID WAIVED' in cells but omits the Condition 2 exemption rule fails chain closure" |
| C-32 | PASS | [IG-REGISTER] AMPLIFIED format: pre-printed code block with `Risk: [...]` and `R-ID: [...]` as independently labeled sub-slots; "A prose instruction… without pre-printed sub-slot labels does not satisfy"; "C-29 requires both elements — C-32 requires them as independently labeled sub-slots" |

**V-05 Aspirational: 24/24 — perfect**
**V-05 Composite: 60 + 30 + (24/24 × 85) = 175/175**
Golden: YES

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** | Golden |
|-----------|-----------|-------------|--------------|---------------|--------|
| V-01 | 5/5 (60) | 3/3 (30) | 13/24 (46.0) | **136.0** | YES |
| V-02 | 5/5 (60) | 3/3 (30) | 14/24 (49.6) | **139.6** | YES |
| V-03 | 5/5 (60) | 3/3 (30) | 14/24 (49.6) | **139.6** | YES |
| V-04 | 5/5 (60) | 3/3 (30) | 20/24 (70.8) | **160.8** | YES |
| **V-05** | **5/5 (60)** | **3/3 (30)** | **24/24 (85)** | **175** | **YES** |

V-02 and V-03 are tied: each adds exactly one R10 criterion to the V-01 base. V-04 produces the large jump (+20 pts) by combining all three R10 criteria with the full R9 V-04 base (split registers, imperative phrasing, Branch B sub-conditions, C-20). V-05 adds the final 4 missing criteria (C-11, C-15, C-19, C-24) from the R9 V-05 ordinal-slot + CASCADE TO architecture.

---

## Excellence Signals (from V-05)

**1. Waiver chain declared as a structural rule, not a behavioral note.**
V-03/V-04/V-05 all declare a named "**Waiver propagation rule (structural):**" in Phase 1 with a Waiver Status column in [PM-COVERAGE-TABLE]. This makes C-31 pass. V-01/V-02 use behavioral notes ("Mark the cell…") — which feel equivalent but fail the structural-rule test. The key distinction: the rule must be a template-level declaration, not a fill-in instruction.

**2. Pre-printed code-block sub-slots distinguish structural format from prose instruction.**
V-02/V-04/V-05 use a code block with `Risk: [...]` and `R-ID: [...]` on separate lines as the AMPLIFIED template. V-01/V-03 use inline combined-prose or single-statement formats. Even when both elements are present, a single-line combined statement fails C-32 — the structural separation is the criterion, not element presence.

**3. Ordinal-labeled slots make multi-instance completeness verifiable by counting.**
V-05's [CNS-SLOT-1-OF-2] / [CNS-SLOT-2-OF-2] pattern with "location 1 of 2" labels satisfies C-11, C-15, and C-19 simultaneously. The ordinal suffix is not decoration — it is the mechanism by which a reviewer can verify completeness without searching prose. No V-01–V-04 achieves this.

**4. CASCADE TO annotations close the semantic gap between output and consumer.**
V-05's "CASCADE TO: [IG-REGISTER] Elimination Paths in Phase 2 (R-IDs must be drawn from this table)" co-located with the unified PM declaration makes the dependency explicit in the same structural block. V-04 has the unified declarations (C-20 passes) but omits the CASCADE TO (C-24 fails) — the annotation is what binds the declaration to its downstream.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["Waiver chain must be declared as a named structural rule in Phase 1 with a Waiver Status column — a behavioral note with equivalent semantics fails C-31 even when WAIVED markers appear in cells", "AMPLIFIED dual sub-slot format requires pre-printed code-block labels in the table template — a combined single-line statement naming both elements fails C-32 regardless of content equivalence", "Column-level R-ID gate token check (C-30) integrates as a named Condition 2 without disturbing any other gate token criteria and composes cleanly with split-register architecture"]}
```
