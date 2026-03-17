Now I have the rubric and all 5 variations. Scoring all variations against rubric v1.

---

# /quest:score — org-chart — Round 1

**Skill:** org-chart | **Rubric:** v1 | **Variations:** V-01 through V-05 (R1, 2026-03-16)

---

## Criterion Reference

| ID | Tier | Weight | What It Tests |
|----|------|--------|---------------|
| C-01 | Essential | 12 | Inertia Assessment — 4 sub-sections, mechanism table >=2 rows with closed Type vocab, `FLAT-CASE-PRESSURE:` line, VERDICT, concrete re-assessment trigger |
| C-02 | Essential | 12 | Roles block opens output — `ROLES-LOADED:` or `ROLES-NOTE:` before all other content |
| C-03 | Essential | 12 | ASCII org diagram with >=2 levels, committees as distinct nodes, role names from roles block |
| C-04 | Essential | 12 | Operating rhythm >=3 distinct rows covering ROB, shiproom, governance |
| C-05 | Essential | 12 | Committee charters — all 5 fields: Purpose, Membership, Decides, Escalates, Quorum (N-of-M fraction) |
| C-06 | Recommended | 10 | Headcount table with **split** Decides/Escalates columns (not merged Decision Scope), >=2 area rows, annotated roles |
| C-07 | Recommended | 10 | All 4 phase gates present in order |
| C-08 | Recommended | 10 | `ROLE-TYPE-CLASSIFICATION:` block immediately after roles, closed-set types, three-tier order |
| C-09 | Aspirational | 5 | ORG-ELEMENT REGISTER (4 categories) + Anti-Pattern Watch with cat-N typed citations |
| C-10 | Aspirational | 5 | Org Evolution Roadmap — 2 triggers from distinct categories |

---

## V-01 — Inertia Framing: Status-Quo Defense Before VERDICT

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | FAIL | Has a 4-part inertia section (status-quo description, defense, threshold, VERDICT) but missing the `FLAT-CASE-PRESSURE:` line, the mechanism table with closed Type vocabulary, and the `Case for Staying Flat` / `How We Coordinate Today` / `Rebuttal` sub-section names required by the rubric |
| C-02 | FAIL | Roles INPUT section appears **after** the inertia gate — rubric requires output opens with `ROLES-LOADED:` or `ROLES-NOTE:` |
| C-03 | PARTIAL | Diagram instructions present (>=2 levels, committees as distinct nodes) but no propagation rule enforcing that node labels match roles declared in the roles block — invented roles could slip through |
| C-04 | PASS | Explicit >=3 row requirement with ROB, shiproom, and governance as named entries |
| C-05 | FAIL | No committee charters section in the prompt at all |
| C-06 | FAIL | Headcount table template is `Area | Headcount | Key Roles` — no Decides or Escalates columns |
| C-07 | FAIL | No phase gate lines |
| C-08 | FAIL | No ROLE-TYPE-CLASSIFICATION block |
| C-09 | FAIL | Not present |
| C-10 | FAIL | Not present |

**Essential passes:** 1 (C-04)
**Recommended passes:** 0
**Aspirational passes:** 0
**Composite:** (1/5 × 60) + (0/3 × 30) + (0/2 × 10) = **12**

---

## V-02 — Output Format: Section Scaffolds with Required Slots

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | FAIL | Section 1 scaffold has coordination mode, threshold, current position, VERDICT, reasoning, re-assessment trigger — but missing `FLAT-CASE-PRESSURE:` line and mechanism table with closed Type vocabulary |
| C-02 | FAIL | Section 1 is Inertia Assessment; roles appear in Section 2 — does not open with `ROLES-LOADED:` |
| C-03 | PARTIAL | Section 2 has diagram requirements (>=2 levels, committees as separate node) but no explicit propagation rule from roles block to node labels |
| C-04 | PASS | Section 4 pre-labels ROB, shiproom, governance rows — forces three distinct rows |
| C-05 | FAIL | Section 5 charters have only 4 fields (Purpose, Membership, Decides, Escalates) — missing Quorum with N-of-M fraction |
| C-06 | FAIL | Section 3 table template uses `Decision Scope` — a single merged column; rubric explicitly requires split Decides and Escalates columns |
| C-07 | FAIL | No phase gate lines |
| C-08 | FAIL | No ROLE-TYPE-CLASSIFICATION block |
| C-09 | FAIL | Not present |
| C-10 | FAIL | Not present |

**Essential passes:** 1 (C-04)
**Recommended passes:** 0
**Aspirational passes:** 0
**Composite:** (1/5 × 60) + (0/3 × 30) + (0/2 × 10) = **12**

---

## V-03 — Role Sequence: Roles-First with Propagation Rule

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | FAIL | Step 2 inertia has informal mechanisms, coordination failures, threshold, VERDICT — but missing `FLAT-CASE-PRESSURE:` line and mechanism table with closed Type vocabulary |
| C-02 | PASS | Step 1 is roles-first, produces `ROLES-LOADED` table before any other output; propagation rule enforces role names appear in >=2 downstream sections |
| C-03 | PASS | Step 3 requires >=2 levels, distinct committee nodes, and explicitly states "every named node must use a role name from Step 1's ROLES-LOADED table" — closes the invented-roles gap |
| C-04 | PASS | Step 5 requires ROB, shiproom, governance as 3 distinct entries |
| C-05 | FAIL | Step 6 charters have Purpose, Membership, Decides, Escalates — missing Quorum field entirely |
| C-06 | FAIL | Step 4 headcount uses `Decision Scope` column — not split |
| C-07 | FAIL | No phase gate lines |
| C-08 | FAIL | No ROLE-TYPE-CLASSIFICATION block |
| C-09 | FAIL | Not present |
| C-10 | FAIL | Not present |

**Essential passes:** 3 (C-02, C-03, C-04)
**Recommended passes:** 0
**Aspirational passes:** 0
**Composite:** (3/5 × 60) + (0/3 × 30) + (0/2 × 10) = **36**

---

## V-04 — Phrasing Register + Inertia Framing: DO/DO NOT with Hard Gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | FAIL | Inertia section has all 5 named elements (coordination mode, status-quo defense, threshold, VERDICT as discrete field, reasoning) but missing `FLAT-CASE-PRESSURE:` line and mechanism table with closed Type vocabulary |
| C-02 | PASS | "DO check .craft/roles/ before writing anything" — roles block is first; DO NOT invent contradicting roles |
| C-03 | PASS | DO draw ASCII hierarchy >=2 levels, committees as distinct nodes, DO NOT produce flat list; DO reference roles from ROLES-LOADED (implicit in phrasing) |
| C-04 | PASS | DO include minimum 3 distinct rows, DO NOT combine, DO NOT produce rhythm with only ROB |
| C-05 | FAIL | Charters have Purpose, Membership, Decides/Escalates — missing Quorum field with N-of-M fraction |
| C-06 | FAIL | Headcount template uses `Decision Scope` — not split Decides/Escalates |
| C-07 | FAIL | Section ordering enforced by prose, not the specific phase gate line format |
| C-08 | FAIL | No ROLE-TYPE-CLASSIFICATION block |
| C-09 | FAIL | Not present |
| C-10 | FAIL | Not present |

**Essential passes:** 3 (C-02, C-03, C-04)
**Recommended passes:** 0
**Aspirational passes:** 0
**Composite:** (3/5 × 60) + (0/3 × 30) + (0/2 × 10) = **36**

---

## V-05 — Lifecycle Emphasis + Output Format: Five-Phase Sequence with Phase-Complete Conditions

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | FAIL | Phase 2 has Status-quo defense, Coordination failures, Flat-team threshold, VERDICT, Re-assessment trigger with concrete requirement enforced by checklist — but missing `FLAT-CASE-PRESSURE:` line and mechanism table with closed Type vocabulary |
| C-02 | PASS | Phase 1 is roles-first; propagation contract requires role names in >=2 downstream sections |
| C-03 | PASS | Phase 3 requires >=2 levels, distinct committee nodes, role names from Phase 1; phase-complete condition enforces diagram completeness |
| C-04 | PASS | Phase 4 requires ROB, shiproom, governance as 3 distinct rows; phase-complete condition verifies each row is present separately |
| C-05 | FAIL | Phase 5 charters have Purpose, Membership, Decides, Escalates with checklist enforcement — but Quorum field with N-of-M fraction is entirely absent |
| C-06 | **PASS** | Phase 3 headcount template explicitly uses separate `Decides | Escalates` columns; note "Decides and Escalates split satisfies C-08" |
| C-07 | FAIL | No formal `=== [PHASE GATE: ...] ===` lines in the required format |
| C-08 | FAIL | No ROLE-TYPE-CLASSIFICATION block |
| C-09 | FAIL | Not present |
| C-10 | FAIL | Not present |

**Essential passes:** 3 (C-02, C-03, C-04)
**Recommended passes:** 1 (C-06)
**Aspirational passes:** 0
**Composite:** (3/5 × 60) + (1/3 × 30) + (0/2 × 10) = 36 + 10 = **46**

---

## Score Summary

| Rank | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite |
|------|-----------|------|------|------|------|------|------|------|------|------|------|-----------|
| 1 | V-05 | FAIL | PASS | PASS | PASS | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | **46** |
| 2 | V-03 | FAIL | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **36** |
| 2 | V-04 | FAIL | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **36** |
| 4 | V-01 | FAIL | FAIL | PARTIAL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **12** |
| 4 | V-02 | FAIL | FAIL | PARTIAL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **12** |

**Golden threshold:** NOT MET by any variation (requires all 5 essential pass AND composite >= 80)

---

## Excellence Signals (from V-05)

1. **Split Decides/Escalates in headcount** — V-05 is the only variation to use a two-column `Decides | Escalates` format in the headcount table. All others used the single `Decision Scope` column, which fails C-06.
2. **Phase-complete checklists** — explicit `- [ ]` checklist items at the end of each phase prevent partial outputs from being accepted silently. Especially effective for the re-assessment trigger specificity (not just "when the team grows").
3. **Propagation contract** — stating "role names from Phase 1 must appear in at least two of: org diagram, headcount Key Roles, committee membership, rhythm DRI/Owner" closes the gap where roles vanish after the opening block.

---

## Systemic Gaps (fail across ALL variations)

**C-01 — FLAT-CASE-PRESSURE line + mechanism table with closed vocabulary**
Every variation has an inertia section but none implements:
- The 4-sub-section naming (Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT)
- A typed mechanism table with closed Type vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
- The `FLAT-CASE-PRESSURE: [rating] — [justification]` line as a gate-opener for VERDICT
- The flat-case-closed separator with row count

**C-05 — Quorum field (N-of-M fraction)**
Every variation has charters but none includes the Quorum field. The N-of-M fraction format (`Quorum: N of M member roles required for binding decisions`) is missing from all five prompts.

**C-07 / C-08 — Phase gates and ROLE-TYPE-CLASSIFICATION**
None of the variations include the specific `=== [PHASE GATE: ...] ===` format lines or the `ROLE-TYPE-CLASSIFICATION:` block with the three-tier order constraint. These were in the rubric but not in any variation's prompt design.

---

## Verdict

All variations are **Failing** band (composite < 60, >=2 essential fails). V-05 is the clear leader at 46. The next iteration must address the two universal misses (C-01 mechanism table + FLAT-CASE-PRESSURE; C-05 Quorum field) to have a chance at the golden threshold.

```json
{"top_score": 46, "all_essential_pass": false, "new_patterns": ["split-decides-escalates-headcount", "phase-complete-checklists", "propagation-contract-roles"]}
```
