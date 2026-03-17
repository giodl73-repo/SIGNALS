## Round 19 Scoring — `draft-spec` v17 Rubric

**Formula**: `(E/5×60) + (R/3×30) + (A/39×85)` — fixed denominator 39

---

## V-01 — Post-Hoc Architect Role Sequence

**N/A cluster**: C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47 (no STATUS-QUO, no Phase 1.5)

### Essential (5/5)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 0–4 present in order; HANDOFF note between Phase 2 and Phase 3 does not affect numbered phase ordering |
| C-02 | PASS | [SCOUT-STATUS-TABLE] with 7 artifact rows in Phase 0 |
| C-03 | PASS | [PM-COVERAGE-TABLE] with Waiver Status column, enumerated COVERED / C-03 WAIVER values |
| C-04 | PASS | [IG-REGISTER] and [ID-REGISTER] both present in Phase 2; "Minimum 2 IG-ID rows required" |
| C-05 | PASS | Phase 3 has 1. PURPOSE, 2. REQUIREMENTS, 3. DESIGN, 4. CONSTRAINTS, 5. OPEN QUESTIONS in prescribed order |

### Recommended (3/3)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 | PASS | Branch A, B-1, B-2, B-3, B-catch all named |
| C-07 | PASS | Each named branch contains a blockquoted VERBATIM RESPONSE block |
| C-08 | PASS | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE] all defined with INVALID IF rules |

### Aspirational (27 pass / 4 fail / 8 N/A)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 | PASS | Waiver Status declared as structural element inside [PM-COVERAGE-TABLE] definition |
| C-10 | PASS | "C-03 WAIVER rows propagate to [IG-REGISTER] as: Elimination Path = 'R-ID WAIVED (no requirements artifact)'" |
| C-11 | PASS | Condition 1 and Condition 2 declared as distinct named invalidity paths in [INERTIA-ANALYZED] |
| C-12 | PASS | "Meeting Condition 1 without Condition 2 is invalid: structural completeness alone does not permit [INERTIA-ANALYZED] to be emitted." |
| C-13 | PASS | "Waiver chain closure — all three nodes named in sequence: (1)...(2)...(3)..." |
| C-14 | PASS | AMPLIFIED threshold names Condition A and Condition B as explicit trigger conditions |
| C-15 | PASS | Dual sub-slot format: "Risk: [risk narrative] / R-ID: [R-XX...]" |
| C-16 | PASS | "Partial-population structural fail: a cell in which one sub-slot is populated while the other is blank is a structural fail, not a content gap." |
| C-17 | PASS | [PM-CONTRACT-SEAL] names both [PM-COVERAGE-TABLE] absent and no R-IDs assigned; "Both structural dependencies must be satisfied" |
| C-18 | PASS | "→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL]." present at Phase 2 entry |
| C-19 | PASS | HANDOFF line and Phase 3 preamble both state "requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED]" |
| C-20 | PASS | [SPEC-DRAFT-COMPLETE] INVALID IF rules name [PM-CONTRACT-SEAL] and [INERTIA-ANALYZED] by token name |
| C-21 | PASS | "Cross-namespace signal (location 1 of 2):" at Phase 1 |
| C-22 | PASS | "(location 2 of 2)" marker in Phase 3 Purpose section |
| C-23 | PASS | "INVALID IF scout-requirements is LOADED but cross-namespace signal is absent at location 1 of 2 (Phase 1) or location 2 of 2 (Phase 3 Purpose section)." |
| C-24 | PASS | "scan R-01 through R-{n} → flag contradictions" with named range |
| C-25 | PASS | "Do not confirm 'none found' without naming the scan source and range." |
| C-26 | PASS | "P0 coverage count: State the count of P0 requirements carried forward before any section prose" |
| C-27 | PASS | All directives use "PM: scan `scout-requirements` →" or equivalent actor→action→output with `→` binding |
| C-28 | PASS | [PM-CONTRACT-SEAL] emitted at Phase 1 exit; Phase 2 computationally blocked on it |
| C-29 | PASS | FINDINGS has 6 named scan items (Scan 1–Scan 6) |
| C-30 | PASS | Finding table names coverage gap, contradiction, complexity hotspot, OQ register |
| C-31 | PASS | "Jointly list at minimum 2 amendments. Each amendment names the target section." |
| C-32 | PASS | "Standard Elimination Path format: R-ID: [R-XX from [PM-COVERAGE-TABLE]]" |
| C-33 | PASS | "C-03 WAIVER rows: R-ID WAIVED (no requirements artifact)" named separately |
| C-34 | PASS | "[INERTIA-ANALYZED] Condition 2 exemption: cells marked 'R-ID WAIVED' are exempt from the per-cell R-ID check." |
| C-35 | PASS | "CASCADE TO: [IG-REGISTER] in Phase 2...; cross-namespace signal row in Phase 3 Purpose section (location 2 of 2)." co-located with Phase 1 directive |
| C-36 | N/A | No [STATUS-QUO-SNAPSHOT] |
| C-37 | N/A | No [STATUS-QUO-SNAPSHOT] |
| C-38 | N/A | No Phase 1.5 |
| C-39 | N/A | No Phase 1.5 |
| C-40 | N/A | No fractional sub-phase |
| C-41 | **FAIL** | No ENTER/EXIT blocks at numbered phase boundaries — phase body contains entry-condition prose (HANDOFF) but no structural ENTER/EXIT elements |
| C-42 | **FAIL** | No second-person transitional frame; preamble uses third-person ("PM leads phases 0 through 2..."), no "you will", "you are entering" across phases |
| C-43 | **FAIL** | No `→ ROLE:` markers at numbered phase entry points; HANDOFF prose is not a structural ROLE marker at a numbered phase boundary |
| C-44 | **FAIL** | No ENTER/EXIT blocks to form a chain |
| C-45 | N/A | No [STATUS-QUO-SNAPSHOT] |
| C-46 | N/A | No [STATUS-QUO-SNAPSHOT] |
| C-47 | N/A | No fractional sub-phase |

**Composite**: (5/5 × 60) + (3/3 × 30) + (27/39 × 85) = 60 + 30 + **58.85** = **148.85**

---

## V-02 — Numbered Checklist Format

**N/A cluster**: C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47

### Essential (5/5)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase headers "PHASE 0" through "PHASE 4" present in order under numbered items 1–5; outer numbering (1=Phase 0, 2=Phase 1...) doesn't affect criterion — all five required phases present in order |
| C-02 | PASS | [SCOUT-STATUS-TABLE] rows 1.1.1–1.1.7 = 7 artifact rows in Phase 0 block |
| C-03 | PASS | [PM-COVERAGE-TABLE] with Waiver Status column; values enumerated at 2.2.1/2.2.2 |
| C-04 | PASS | [IG-REGISTER] at 3.1, [ID-REGISTER] at 3.6, min 2 rows stated |
| C-05 | PASS | 4.4.1 PURPOSE, 4.4.2 REQUIREMENTS, 4.4.3 DESIGN, 4.4.4 CONSTRAINTS, 4.4.5 OPEN QUESTIONS — five labeled sections in prescribed order; numbered labels satisfy "five guided sections" identically to prose labels |

### Recommended (3/3)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 | PASS | 1.2.1 Branch A, 1.2.2 Branch B-1, 1.2.3 Branch B-2, 1.2.4 Branch B-3, 1.2.5 Branch B-catch |
| C-07 | PASS | Each branch item has "> VERBATIM RESPONSE:" blockquote |
| C-08 | PASS | [PM-CONTRACT-SEAL] at 2.5, [INERTIA-ANALYZED] at 3.7, [SPEC-DRAFT-COMPLETE] at 4.5; all have INVALID IF rules |

### Aspirational (27 pass / 4 fail / 8 N/A)

All C-09 through C-35 pass on same grounds as V-01 (content identical, surface format changed). Key checks:

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 | PASS | Waiver Status enumerated values declared at 2.2.1–2.2.2 within [PM-COVERAGE-TABLE] block |
| C-11 | PASS | 3.7.1 = Condition 1, 3.7.2 = Condition 2 — distinct numbered items |
| C-12 | PASS | 3.7.3: "Meeting Condition 1 without Condition 2 is invalid." |
| C-13 | PASS | 3.7.5: "(1)... (2)... (3)..." three nodes in sequence |
| C-17 | PASS | 2.5.1 and 2.5.2 name both dependencies; 2.5.3 confirms both required |
| C-18 | PASS | 2.6: "→ BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL]." and repeated at 3.0 |
| C-19 | PASS | 3.8: "→ BLOCKED: Phase 3 requires [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED]." |
| C-27 | PASS | 2.1: "PM: scan `scout-requirements` → extract R-IDs..." retains actor→action→output form |
| C-29 | PASS | 6.1.1–6.1.6 = 6 named scan items |
| C-36–C-40 | N/A | No STATUS-QUO-SNAPSHOT, no Phase 1.5 |
| C-41 | **FAIL** | No ENTER/EXIT blocks at numbered phase boundaries |
| C-42 | **FAIL** | No second-person frame; preamble is task-directive, not transitional orientation |
| C-43 | **FAIL** | No `→ ROLE:` markers at phase entries |
| C-44 | **FAIL** | No ENTER/EXIT chain |
| C-45–C-47 | N/A | |

**Composite**: (5/5 × 60) + (3/3 × 30) + (27/39 × 85) = 60 + 30 + 58.85 = **148.85**

---

## V-03 — MUST/SHALL Modal Register

**N/A cluster**: C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47

### Essential (5/5)

All five phases present in order; all five required blocks present. PASS on C-01 through C-05.

### Recommended (3/3)

All fallback branches present with VERBATIM RESPONSE blocks; all three gate tokens defined. PASS on C-06 through C-08.

### Aspirational (27 pass / 4 fail / 8 N/A)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-27 | PASS | "PM: MUST scan `scout-requirements` -> extract all R-IDs..." — actor label and `->` binding preserved throughout; modal wrapper wraps the directive without replacing actor or binding. Hypothesis states "actor→action `→` binding preserved" |
| C-18 | PASS | "Phase 2 SHALL NOT begin until [PM-CONTRACT-SEAL] is present." — C-18 accepts "or equivalent"; SHALL NOT form is equivalent to BLOCKED declaration |
| C-19 | PASS | "Phase 3 SHALL NOT begin until [PM-CONTRACT-SEAL] AND [INERTIA-ANALYZED] are both present." — names both tokens |
| C-12 | PASS | "Condition 1 satisfied WITHOUT Condition 2 SHALL constitute an invalid state: structural completeness alone SHALL NOT permit [INERTIA-ANALYZED] to be emitted." — MUST/SHALL form of the explicit statement |
| C-42 | **FAIL** | MUST/SHALL modal register is orthogonal to second-person transitional frame; no "you will", "you are entering" anywhere; C-42 requires orientation prose, not compliance directives |
| C-41 | **FAIL** | No ENTER/EXIT ceremony |
| C-43 | **FAIL** | No ROLE markers |
| C-44 | **FAIL** | No chained ENTER/EXIT |

All C-09–C-35 (excluding C-36–C-47 N/A) pass on same grounds as V-01. 27/39 aspirational pass.

**Composite**: (5/5 × 60) + (3/3 × 30) + (27/39 × 85) = 60 + 30 + 58.85 = **148.85**

---

## V-04 — Competition-First Inertia Framing + [STATUS-QUO-SNAPSHOT]

**N/A cluster**: C-38, C-39, C-40, C-47 (no Phase 1.5)
**Active extension cluster**: C-36, C-37, C-45, C-46

### Essential (5/5)

All five phases in order; [SCOUT-STATUS-TABLE] 7 rows; [PM-COVERAGE-TABLE] with Waiver Status; [IG-REGISTER] + [ID-REGISTER] in Phase 2; five Phase 3 sections. PASS C-01–C-05.

### Recommended (3/3)

PASS C-06–C-08.

### Aspirational (31 pass / 4 fail / 4 N/A)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-36 | PASS | "[INERTIA-ANALYZED] Condition 1: INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated." — explicitly names [STATUS-QUO-SNAPSHOT] in Condition 1 invalidity rule |
| C-37 | PASS | "[STATUS-QUO-SNAPSHOT] Structural fail rule: A row with a named Alternative but a blank Gap statement is a structural fail, not a content gap." — co-located with [STATUS-QUO-SNAPSHOT] row definition |
| C-38 | N/A | No Phase 1.5 |
| C-39 | N/A | No Phase 1.5 |
| C-40 | N/A | No fractional sub-phase |
| C-41 | **FAIL** | No ENTER/EXIT ceremony |
| C-42 | **FAIL** | No second-person frame; preamble is third-person "competition-first inertia pattern" orientation |
| C-43 | **FAIL** | No `→ ROLE:` markers at phase entries |
| C-44 | **FAIL** | No chained ENTER/EXIT |
| C-45 | PASS | Dual-form structural fail rule: "A row with a named Alternative but a blank Gap statement is a structural fail, not a content gap. **Do not leave Gap blank when Alternative is populated.**" — negative declaration (first sentence) + positive directive (second sentence) co-located in [STATUS-QUO-SNAPSHOT] block |
| C-46 | PASS | "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent **from this phase block**..." — "from this phase block" scope qualifier present in [INERTIA-ANALYZED] Condition 1 |
| C-47 | N/A | No fractional sub-phase |

C-09–C-35 all pass as in V-01 (27) + C-36 + C-37 + C-45 + C-46 = **31 aspirational pass**.

**Composite**: (5/5 × 60) + (3/3 × 30) + (31/39 × 85) = 60 + 30 + **67.56** = **157.56**

---

## V-05 — Full Five-Cluster Extension (Compliance Lead Phase 1.5)

**No N/A criteria** — all five extension clusters active.

### Essential (5/5)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | PHASE 0, 1, 2, 3, 4 all present in order; Phase 1.5 is fractional sub-phase between Phase 1 and Phase 2 — does not merge, replace, or reorder any required numbered phase |
| C-02 | PASS | [SCOUT-STATUS-TABLE] with 7 artifact rows in Phase 0 |
| C-03 | PASS | [PM-COVERAGE-TABLE] with Waiver Status column, COVERED / C-03 WAIVER enumeration |
| C-04 | PASS | [IG-REGISTER] and [ID-REGISTER] in Phase 2; "Minimum 2 IG-ID rows required" |
| C-05 | PASS | Five sections in Phase 3: 1. PURPOSE, 2. REQUIREMENTS, 3. DESIGN, 4. CONSTRAINTS, 5. OPEN QUESTIONS |

### Recommended (3/3)

PASS C-06–C-08.

### Aspirational (39 pass / 0 fail / 0 N/A)

**C-09 through C-35**: All pass on identical grounds as prior variations.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-36 | PASS | "[INERTIA-ANALYZED] Condition 1: INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block, or any required row is unpopulated." |
| C-37 | PASS | [STATUS-QUO-SNAPSHOT] block contains: "Structural fail rule: A row with a named Alternative but a blank Gap statement is a structural fail, not a content gap. Do not leave Gap blank when Alternative is populated." |
| C-38 | PASS | "ENTER Phase 2: [PM-CONTRACT-SEAL] from Phase 1 AND [COMPLIANCE-SCOPE-SEAL] from Phase 1.5 must both be present. → BLOCKED: Phase 2 requires [PM-CONTRACT-SEAL] AND [COMPLIANCE-SCOPE-SEAL]." — two named tokens from two distinct prior phases in Phase 2 REQUIRES |
| C-39 | PASS | "PHASE 1.5 — COMPLIANCE INERTIA SCOPING [GATE: COMPLIANCE-SCOPE-SEAL] / → ROLE: Compliance Lead" — header names ordinal (1.5) and role scope (COMPLIANCE INERTIA SCOPING); emits [COMPLIANCE-SCOPE-SEAL]; all five C-01 phases remain in prescribed order |
| C-40 | PASS | "[COMPLIANCE-SCOPE-SEAL] INVALID IF the structural fail rule — 'a row with a named Alternative but a blank Gap statement is a structural fail, not a content gap' — is absent from within the [STATUS-QUO-SNAPSHOT] block definition." — names the target block ([STATUS-QUO-SNAPSHOT]) AND the specific co-located rule as a precondition |
| C-41 | PASS | All five numbered phases carry formal ENTER and EXIT blocks at phase boundary level: Phase 0 ENTER (no preconditions) / EXIT ([SCOUT-STATUS-TABLE] complete); Phase 1 ENTER ([SCOUT-STATUS-TABLE] from Phase 0) / EXIT ([PM-CONTRACT-SEAL]); Phase 2 ENTER (both tokens) / EXIT ([INERTIA-ANALYZED]); Phase 3 ENTER (both tokens) / EXIT ([SPEC-DRAFT-COMPLETE]); Phase 4 ENTER ([SPEC-DRAFT-COMPLETE]) / EXIT (amendment list) |
| C-42 | PASS | Second-person frame appears across all phases: "You are beginning Phase 0. Your goal is...", "You are now entering Phase 1. Your goal is...", "You are now entering Phase 1.5. Your goal is...", "You are now entering Phase 2. Your goal is...", "You are now entering Phase 3. Your goal is...", "You are now in Phase 4. Your goal is...", "You have completed the spec draft." — multiple phases, not single preamble. All actor→action directives retain "PM: scan..." form (C-27 compliance preserved) |
| C-43 | PASS | Phase 0: `→ ROLE: PM`; Phase 1: `→ ROLE: PM`; Phase 2: `→ ROLE: PM + Compliance Lead` (two roles named); Phase 3: `→ ROLE: Architect + PM`; Phase 4: `→ ROLE: PM + Architect` — markers as dedicated structural elements at phase entry, consistent with phase body directives |
| C-44 | PASS | Unbroken named chain: Phase 0 EXIT [SCOUT-STATUS-TABLE] → Phase 1 ENTER [SCOUT-STATUS-TABLE]; Phase 1 EXIT [PM-CONTRACT-SEAL] → Phase 2 ENTER [PM-CONTRACT-SEAL]; Phase 2 EXIT [INERTIA-ANALYZED] → Phase 3 ENTER [INERTIA-ANALYZED]; Phase 3 EXIT [SPEC-DRAFT-COMPLETE] → Phase 4 ENTER [SPEC-DRAFT-COMPLETE]; Phase 4 EXIT "amendment list" named in same structural position |
| C-45 | PASS | "A row with a named Alternative but a blank Gap statement is a structural fail, not a content gap. **Do not leave Gap blank when Alternative is populated.**" — negative + positive, co-located |
| C-46 | PASS | "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent **from this phase block**..." — scope qualifier present |
| C-47 | PASS | "ENTER Phase 2: [PM-CONTRACT-SEAL] from Phase 1 AND [COMPLIANCE-SCOPE-SEAL] from Phase 1.5 must both be present." — ENTER block names Phase 1's EXIT token AND Phase 1.5's EXIT token; chain unbroken; declaration in ENTER block itself (not only in C-38 gate dependency header) |

**Composite**: (5/5 × 60) + (3/3 × 30) + (39/39 × 85) = 60 + 30 + **85.00** = **175.00**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational (pass/fail/N/A) | Composite |
|-----------|-----------|-------------|------------------------------|-----------|
| V-01 | 5/5 (60) | 3/3 (30) | 27/4/8 (58.85) | **148.85** |
| V-02 | 5/5 (60) | 3/3 (30) | 27/4/8 (58.85) | **148.85** |
| V-03 | 5/5 (60) | 3/3 (30) | 27/4/8 (58.85) | **148.85** |
| V-04 | 5/5 (60) | 3/3 (30) | 31/4/4 (67.56) | **157.56** |
| V-05 | 5/5 (60) | 3/3 (30) | 39/0/0 (85.00) | **175.00** |

**Rank**: V-05 > V-04 > V-01 = V-02 = V-03

All predicted scores confirmed exactly. All variations pass the golden threshold (all 5 essential + composite ≥ 85).

---

## Excellence Signals (V-05)

V-05 achieves 175/175 — the second perfect score in the series (R17 V-01 being the first). The new axis in R19 is Compliance Lead Phase 1.5 vs. Strategy Lead in R18. Five signals to examine:

**E-1: Compliance Lead Phase 1.5 is structurally indistinguishable from Strategy Lead Phase 1.5 for C-38/C-39/C-40/C-47 scoring.**
The fractional sub-phase extension cluster evaluates on anatomy — named ordinal in header, role scope in header, emitted gate token, cross-block rule reference in gate invalidity — not on which role inhabits the sub-phase. Compliance Lead and Strategy Lead produce identical scoring against all four criteria. The role identity is transparent to the rubric.

**E-2: C-40 fires on role-agnostic cross-block rule dependency.**
[COMPLIANCE-SCOPE-SEAL]'s INVALID IF cross-references the [STATUS-QUO-SNAPSHOT] structural fail rule identically to [STRATEGY-SCOPE-SEAL] in R18. The criterion cares about the named cross-block dependency pattern, not the name of the gate token making the reference.

**E-3: HANDOFF TO ARCHITECT prose (V-01) is invisible to all criteria.**
An explicit "HANDOFF TO ARCHITECT" statement at the Phase 2/Phase 3 boundary changes no evaluation. C-43 requires `→ ROLE:` markers as dedicated structural elements at *numbered phase entries*, not prose transition statements between phases. V-01's handoff note confirmed the boundary between actor-labeling prose and structural ROLE markers is cleanly defined.

**E-4: Numbered checklist format (V-02) satisfies C-05 identically to prose sections.**
`4.4.1 PURPOSE` through `4.4.5 OPEN QUESTIONS` satisfies "five guided sections in prescribed order" regardless of whether sections are introduced by numbered items or prose labels. The criterion is section-presence and ordering, not surface formatting.

**E-5: MUST/SHALL modal register (V-03) satisfies C-27 and C-18 without conflict.**
Modal wrappers ("PM: MUST scan `scout-requirements` →") preserve the actor→action→output form with `→` binding, satisfying C-27. "Phase 2 SHALL NOT begin until [PM-CONTRACT-SEAL] is present" satisfies C-18's "or equivalent" condition. The register change is orthogonal to structural governance criteria; it conflicts only with C-42 (which requires second-person orientation prose, not compliance directives).

**Disposition of all five signals**: All confirmatory. No signal represents a structural gap without an existing criterion. The rubric correctly evaluates role-agnostic fractional sub-phases, format-agnostic section naming, and register-agnostic directive forms as written.

---

## Rubric Stability Assessment

R19 is the third consecutive round where V-05 (full five-cluster extension) achieves 175/175. The variation space explored across R17, R18, R19 includes: Strategy Lead Phase 1.5, Architecture-First scoping, Compliance Lead Phase 1.5; table-dominant format, second-person frame, role-sequence variation, numbered checklist, MUST/SHALL modal. No variation has introduced a structural pattern that exposes a criterion gap. The rubric remains stable at 47 criteria.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
