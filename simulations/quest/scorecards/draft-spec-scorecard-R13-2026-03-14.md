Now I have everything needed to score all five variations. Let me evaluate systematically.

---

# Quest Score — `draft-spec` — Round 13 (Rubric v12)

**Evaluated**: 2026-03-15 | **Variations**: V-01 through V-05 | **Rubric**: v12 (37 criteria)

---

## Criterion Quick-Reference

| ID | Tier | Description |
|----|------|-------------|
| C-01..C-05 | Essential (12 pts each) | Scaffold, table presence, frontmatter |
| C-06..C-08 | Recommended (10 pts each) | PM Phase 3 role, contradiction scan, amendment list |
| C-09..C-35 | Aspirational | Fallback branches, gate tokens, traceability, depth rules |
| C-36 | Aspirational | [INERTIA-ANALYZED] Condition 1 names [STATUS-QUO-SNAPSHOT] |
| C-37 | Aspirational | [STATUS-QUO-SNAPSHOT] co-located structural fail rule |

**N/A rule**: C-36 and C-37 are inapplicable to templates without [STATUS-QUO-SNAPSHOT]. An inapplicable criterion cannot contribute to `aspirational_pass`. Fixed denominator = 29 for all variations.

---

## V-01 — Compressed Phase Headers

**Axis**: All phase headers replaced with single-line `→ BLOCKED:` / `→ BLOCKS:` inline gate statements. Gate tokens, invalidity rules, and structural blocks unchanged. No [STATUS-QUO-SNAPSHOT].

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | All five phases + FINDINGS in prescribed order |
| C-02 | **PASS** | 7-row [SCOUT-STATUS-TABLE] in Phase 0, before Phase 1 |
| C-03 | **PASS** | [PM-COVERAGE-TABLE] with Waiver Status column and C-03 waiver protocol |
| C-04 | **PASS** | FINDINGS has scan list (6 items) and structured findings table |
| C-05 | **PASS** | Frontmatter with all 6 fields: skill, topic, item, date, skill_version, input |
| C-06 | **PASS** | Phase 3: "PM: scan [PM-COVERAGE-TABLE] → fill each pre-assigned row" |
| C-07 | **PASS** | Contradiction scan with "Do not confirm 'none found' without naming the scan range" |
| C-08 | **PASS** | Phase 4: 2 enumerated amendment items |
| C-09 | **PASS** | Branch A ALL NOT FOUND with explicit HALT |
| C-10 | **PASS** | Cross-namespace signal table in Phase 1 with named Source artifact field |
| C-11 | **PASS** | Pre-printed signal row in Phase 1 AND Purpose section |
| C-12 | **PASS** | "PM: scan [PM-COVERAGE-TABLE] → fill..." inline in Phase 3 body |
| C-13 | **PASS** | Phase 3 Requirements: "Req ID \| Priority \| Spec Entry \| Status" — Status column per row |
| C-14 | **PASS** | Active inspection guard: "Do not confirm P0 coverage without naming scan range" |
| C-15 | **PASS** | "(location 1 of 2)" and "(location 2 of 2)" present |
| C-16 | **PASS** | All P0 assigned in Phase 1 before Architect prose in Phase 3 |
| C-17 | **PASS** | [PM-CONTRACT-SEAL] named; Phase 2: "→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above" |
| C-18 | **PASS** | Branch A has full blockquoted VERBATIM RESPONSE text |
| C-19 | **PASS** | Ordinal markers on the field itself ("Cross-namespace signal (location 1 of 2…)") |
| C-20 | **PASS** | "PM: scan `scout-requirements` → assign each P0 row → emit [PM-CONTRACT-SEAL]" |
| C-21 | **PASS** | [PM-CONTRACT-SEAL] INVALID IF without [PM-COVERAGE-TABLE] present |
| C-22 | **PASS** | [IG-REGISTER] and [ID-REGISTER] are separate named tables |
| C-23 | **PASS** | Responsible Role column in [IG-REGISTER] |
| C-24 | **PASS** | CASCADE TO co-located with unified role-source declaration |
| C-25 | **PASS** | Branch A and Branch B with independent VERBATIM blocks |
| C-26 | **PASS** | B-1, B-2, B-3, B-catch with distinct VERBATIM blocks + anti-blend instruction |
| C-27 | **PASS** | Imperative `→` binding form throughout role-phase instructions |
| C-28 | **PASS** | Phase 1 before Phase 2; inline gate dependency explicitly names [PM-CONTRACT-SEAL] |
| C-29 | **PASS** | "Each cell must begin with 'R-ID: [R-XX from [PM-COVERAGE-TABLE]]'" |
| C-30 | **PASS** | Condition 2: "INVALID IF any Elimination Path cell lacks a named R-ID" (per-cell check) |
| C-31 | **PASS** | Waiver propagation rule in Phase 1; Condition 2 exemption for "R-ID WAIVED" cells |
| C-32 | **PASS** | AMPLIFIED dual sub-slot template with `Risk:` and `R-ID:` named sub-slots |
| C-33 | **PASS** | Waiver Status column with COVERED / C-03 WAIVER enumerated values |
| C-34 | **PASS** | "Chain closed: [PM-COVERAGE-TABLE] … R-ID WAIVED … Condition 2 exemption" named in sequence |
| C-35 | **PASS** | "A cell with 'Risk:' populated and 'R-ID:' blank is a structural fail" |
| C-36 | **N/A** | No [STATUS-QUO-SNAPSHOT] — cannot evaluate; cannot contribute to aspirational_pass |
| C-37 | **N/A** | No [STATUS-QUO-SNAPSHOT] — cannot evaluate; cannot contribute to aspirational_pass |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 27/29 → 27/29 × 85 = **79.14 pts**  
**Composite: 169.1 / 175**

---

## V-02 — Inertia Framing (STATUS-QUO-SNAPSHOT + C-36 + C-37)

**Axis**: [STATUS-QUO-SNAPSHOT] added as first operation in Phase 2; each SQ-ID seeds one IG-ID; [INERTIA-ANALYZED] Condition 1 extended to name [STATUS-QUO-SNAPSHOT] (C-36); co-located structural fail rule for blank gap statements (C-37). Verbose REQUIRES/PRODUCES headers preserved.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 | **PASS** ×5 | All five phases + FINDINGS in order; 7-row table; Waiver protocol; scan list + table; frontmatter |
| C-06..C-08 | **PASS** ×3 | PM in Phase 3; contradiction scan with named range; 2 amendment items |
| C-09..C-35 | **PASS** ×27 | All aspirational base criteria satisfied (same structural elements, same gate tokens, full chain closure) |
| C-36 | **PASS** | [INERTIA-ANALYZED] Condition 1: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated" — [STATUS-QUO-SNAPSHOT] explicitly named |
| C-37 | **PASS** | [STATUS-QUO-SNAPSHOT] block: "A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap" — co-located with row definition, names the specific partial-population failure mode |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 29/29 → 85 pts  
**Composite: 175 / 175** ✓ Golden

---

## V-03 — Additive Coverage Columns

**Axis**: [PM-COVERAGE-TABLE] adds Coverage Evidence column; Phase 3 Requirements table adds Confidence column (HIGH/MEDIUM/LOW). Required columns (Waiver Status, Status) preserved. No [STATUS-QUO-SNAPSHOT].

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 | **PASS** ×5 | All sections present; 7-row table; Waiver protocol intact; scan list + table; frontmatter |
| C-06..C-08 | **PASS** ×3 | PM in Phase 3; contradiction scan; 2 amendment items |
| C-13 | **PASS** | Status column still present per row; Confidence is additive (does not replace Status) |
| C-33 | **PASS** | Waiver Status column still present; Coverage Evidence is additive (does not replace it) |
| C-09..C-35 | **PASS** ×27 | All base aspirational criteria satisfied |
| C-36 | **N/A** | No [STATUS-QUO-SNAPSHOT] |
| C-37 | **N/A** | No [STATUS-QUO-SNAPSHOT] |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 27/29 → 79.14 pts  
**Composite: 169.1 / 175**

---

## V-04 — Combined: STATUS-QUO-SNAPSHOT + Compressed Headers

**Axis**: V-02 inertia framing (C-36/C-37 satisfied) combined with V-01 compressed phase headers. Gate tokens and invalidity rules intact.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01..C-05 | **PASS** ×5 | All five phases in order; 7-row table; waiver protocol; scan list includes [STATUS-QUO-SNAPSHOT] verification item; frontmatter |
| C-06..C-08 | **PASS** ×3 | PM in Phase 3; contradiction scan; 2 amendment items |
| C-17 | **PASS** | Phase 2: "→ BLOCKED: Phase 2 begins after [PM-CONTRACT-SEAL] is present above. If absent, halt and state '[PM-CONTRACT-SEAL] missing — complete Phase 1 first.'" — compressed form still names dependency explicitly |
| C-28 | **PASS** | Phase 1 before Phase 2; inline gate statement enforces [PM-CONTRACT-SEAL] dependency computationally |
| C-34 | **PASS** | "Chain closed: … All three nodes named in sequence." |
| C-36 | **PASS** | [INERTIA-ANALYZED] Condition 1: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated" |
| C-37 | **PASS** | [STATUS-QUO-SNAPSHOT]: "A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap" — co-located structural fail rule |
| C-09..C-35 | **PASS** ×27 | All base aspirational criteria satisfied |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 29/29 → 85 pts  
**Composite: 175 / 175** ✓ Golden — **Primary Golden Candidate**

---

## V-05 — Combined: STATUS-QUO-SNAPSHOT + Strategy Inertia Scoping

**Axis**: V-02 inertia framing (C-36/C-37) PLUS Phase 1.5 (STRATEGY INERTIA SCOPING) where Strategy emits [STRATEGY-SCOPE-SEAL] gating [IG-REGISTER] authoring. Verbose headers. [STATUS-QUO-SNAPSHOT] moves to Phase 1.5.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | All five required phases present and in prescribed order: Phase 0 → Phase 1 (PM PRE-ASSIGNMENT) → Phase 1.5 sub-phase → Phase 2 (INERTIA ANALYSIS) → Phase 3 (GUIDED SECTIONS) → Phase 4 (AMENDMENTS) → FINDINGS. Phase 1.5 is additive; does not reorder or merge required phases |
| C-02..C-05 | **PASS** ×4 | 7-row table; waiver protocol; scan list names [STRATEGY-SCOPE-SEAL] + [STATUS-QUO-SNAPSHOT]; frontmatter |
| C-06..C-08 | **PASS** ×3 | PM in Phase 3; contradiction scan; 2 amendment items |
| C-17 | **PASS** | Phase 2 REQUIRES: "[PM-CONTRACT-SEAL] from Phase 1 AND [STRATEGY-SCOPE-SEAL] from Phase 1.5." [PM-CONTRACT-SEAL] still explicitly declared as REQUIRED |
| C-28 | **PASS** | PM pre-assignment (Phase 1) still precedes inertia analysis (Phase 2). [PM-CONTRACT-SEAL] gate dependency present. Phase 1.5 is between PM and inertia but does not precede PM |
| C-21 | **PASS** | [PM-CONTRACT-SEAL] INVALID IF rule still names [PM-COVERAGE-TABLE] |
| C-36 | **PASS** | [INERTIA-ANALYZED] Condition 1: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent from this phase block or any required row is unpopulated" |
| C-37 | **PASS** | [STATUS-QUO-SNAPSHOT] in Phase 1.5: "A row with a named status-quo alternative but a blank gap statement is a structural fail, not a content gap" — co-located |
| C-09..C-35 | **PASS** ×27 | All base aspirational criteria satisfied |

**Note — New structural patterns introduced but not yet codified in rubric v12:**
- [STRATEGY-SCOPE-SEAL] as a second named gate token gating Phase 2 (dual-token Phase 2 dependency not captured in any existing criterion)
- Phase 1.5 sub-phase pattern (named sub-phase between numbered phases, allowing Strategy role insertion without disrupting numbered phase ordering)
- [STRATEGY-SCOPE-SEAL] INVALID IF rule requires both [STATUS-QUO-SNAPSHOT] presence AND co-located structural fail rule verification — token invalidity cross-references a co-located structural rule

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 29/29 → 85 pts  
**Composite: 175 / 175** ✓ Golden

---

## Ranking

| Rank | Variation | Composite | All Essential | C-36 | C-37 | Notes |
|------|-----------|-----------|---------------|------|------|-------|
| 1 (tie) | **V-04** | **175/175** | YES | PASS | PASS | Primary golden candidate — inertia depth + compressed headers |
| 1 (tie) | **V-02** | **175/175** | YES | PASS | PASS | Single-axis C-36/C-37 target; cleanest isolated signal |
| 1 (tie) | **V-05** | **175/175** | YES | PASS | PASS | New structural patterns; seeds future criteria |
| 4 (tie) | V-01 | 169.1/175 | YES | N/A | N/A | Header compression confirmed criterion-neutral |
| 4 (tie) | V-03 | 169.1/175 | YES | N/A | N/A | Additive columns confirmed criterion-neutral |

---

## Excellence Signals — Top Variations (V-02, V-04, V-05)

**1. C-36/C-37 integration is the decisive separator** — The 5.86-point aspirational gap between the top tier (175) and the V-01/V-03 tier (169.1) is entirely attributable to [STATUS-QUO-SNAPSHOT] presence. Variations that don't introduce the snapshot block cannot score above 169.1 under rubric v12, regardless of all other structural quality.

**2. Compressed headers do not degrade any criterion (V-04 confirmation)** — V-04's 175 score confirms that C-17 and C-28 depend on gate token presence and dependency declaration, not on verbose REQUIRES/PRODUCES boilerplate. The compressed `→ BLOCKED:` form is fully criterion-equivalent.

**3. Additive columns are criterion-neutral (V-03 confirmation)** — Coverage Evidence and Confidence columns do not displace required structural elements. Both C-13 (Status column) and C-33 (Waiver Status column) pass when additive columns are present alongside them.

**4. Phase 1.5 sub-phase pattern is architecturally safe (V-05)** — Inserting a Strategy sub-phase between Phase 1 and Phase 2 does not violate C-01 (five required phases still in order), C-17 (Phase 2 still REQUIRES [PM-CONTRACT-SEAL]), or C-28 (PM still precedes inertia). The numbered phase ordering contract can accommodate named sub-phases between integers.

**5. [STRATEGY-SCOPE-SEAL] dual-token gate introduces new pattern (V-05)** — Phase 2 REQUIRES both [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL] — a multi-token dependency not captured in any existing criterion. This is the primary new pattern from R13; likely to seed C-38 in rubric v13.

---

## New Pattern Candidates from R13

| Pattern | Source | Description | Seeds |
|---------|--------|-------------|-------|
| Dual-token Phase gate | V-05 | Phase 2 blocks on two named tokens from two different prior phases | C-38 candidate |
| Named sub-phase between numbered phases | V-05 | Phase 1.5 as a Strategy scoping step; preserves numbered ordering contract while inserting a new role | C-39 candidate |
| Seal token references co-located structural rule | V-05 | [STRATEGY-SCOPE-SEAL] INVALID IF requires structural fail rule co-located with [STATUS-QUO-SNAPSHOT] | Depth criterion candidate |

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["dual-token Phase 2 gate: Phase 2 blocks on both [PM-CONTRACT-SEAL] and [STRATEGY-SCOPE-SEAL] — multi-token dependency not captured in any existing criterion", "named sub-phase between numbered phases: Phase 1.5 inserts Strategy scoping between Phase 1 and Phase 2 without violating numbered phase ordering contract", "seal token invalidity cross-references co-located structural rule: [STRATEGY-SCOPE-SEAL] INVALID IF requires structural fail rule present co-located with [STATUS-QUO-SNAPSHOT] row definition"]}
```
