# corps-chart Scoring — Round 6 (Rubric v5)

Only one variation to score this round: **V-01**.

---

## V-01 — Axis: Phrasing Register (Formal/Technical Imperative)

### Essential Criteria (60 pts, 12 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION with all four domain types | **PASS** | STEP 1 emits the block with closed vocabulary `(strategic) \| (operational) \| (advisory) \| (governance)`; "No role may be omitted. No domain type outside the four-word vocabulary is permitted." |
| C-02 | ASCII diagram with hierarchy and committees as distinct nodes | **PASS** | STEP 3: "Committees MUST appear as distinct labeled nodes — not embedded inside an area box." Minimum two hierarchy levels. Role names must match ROLE-NAME LOCK exactly. |
| C-03 | Headcount table with Decides and Escalates columns | **PASS** | STEP 4: "exactly these five columns: Area \| Headcount \| Key Roles \| Decides \| Escalates". VERIFY block states: "A merged Decision Scope column does not satisfy this step." |
| C-04 | Operating rhythm table with minimum three distinct rows | **PASS** | STEP 5: minimum three rows covering ROB + shiproom/gate + governance. "Do not merge two meetings into one row." |
| C-05 | Committee charters with all five required fields | **PASS** | STEP 6: all five fields listed; Quorum fraction format specified; Escalates must name a destination, not a residual clause. VERIFY enforces all five fields present per charter. |

**Essential: 5/5 PASS → 60/60 pts**

---

### Recommended Criteria (30 pts, 10 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Inertia assessment with verdict and pressure rating | **PASS** | STEP 2 has all four sub-sections in strict order. Verdict emits `FLAT-CASE-PRESSURE: [rating]` from closed set `Strong \| Moderate \| Weak \| Negligible \| Insufficient`. Declares exactly one of `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. RE-ASSESSMENT TRIGGER in verdict; "Revisit as the team grows" explicitly disqualified. |
| C-07 | ORG-ELEMENT REGISTER with all four categories | **PASS** | STEP 7: all four categories specified with content requirements. "No category may be empty or missing." |
| C-08 | Section order with all four phase gates present | **PASS** | All four required gates appear in exact order: ROLES COMPLETE → INERTIA COMPLETE → STRUCTURE COMPLETE → CHARTERS COMPLETE. Each appears between the correct steps. |

**Recommended: 3/3 PASS → 30/30 pts**

---

### Aspirational Criteria (10 pts, 1.11 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | STEP 9 produces Anti-Pattern Watch table with min 2 rows; every `Why It Applies Here` cell must open with `[element name] (cat-N) —`. VERIFY: "No cell names an org element without the typed citation prefix." |
| C-10 | Org Evolution Roadmap with two distinct trigger categories | **PASS** | STEP 8 Row 2 must come from a different category than Row 1 (headcount threshold). VERIFY: "Two headcount threshold rows do not satisfy this step." |
| C-11 | Inertia Rebuttal is role-grounded with concrete re-assessment trigger | **PASS** | STEP 2c ROLE UNDER PRESSURE requires "exactly one role from ROLE-NAME LOCK". OBSERVABLE BREAKDOWN requires "a current coordination failure — not a growth projection". Verdict RE-ASSESSMENT TRIGGER must be concrete; "Revisit as the team grows" explicitly disqualified. |
| C-12 | Role-name coherence across all document sections | **PASS** | ROLE-NAME LOCK states "No role name may appear in any downstream section... unless it appears in this lock list." Enforced in STEP 3 (diagram), STEP 5 (DRI/Owner), STEP 2b (How We Coordinate Today), STEP 2c (Rebuttal). |
| C-13 | ROLE-NAME LOCK block emitted after classification | **PASS** | STEP 1: "IMMEDIATELY AFTER the classification block, EMIT: ROLE-NAME LOCK" as numbered enumeration. Block appears before the first phase gate. Mechanism described: "downstream sections can be verified against a single named list." |
| C-14 | Inertia Rebuttal uses mandatory four-field case form | **PASS** | STEP 2c produces exact four-field form with all labels in order: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER. VERIFY block after the form excludes future-tense breakdowns. |
| C-15 | Anti-Pattern Watch uses schema-enforced CAT-N citation prefix | **PASS** | STEP 9 emits `CAT-N-CITATION-SCHEMA` block immediately before the table; enumerates valid cat-N codes; states mandatory `[element name] (cat-N) —` prefix. "No cell may name an org element without this typed prefix." |
| C-16 | Org Evolution Roadmap uses TRIGGER-TYPE VOCABULARY block | **PASS** | STEP 8 emits `TRIGGER-TYPE VOCABULARY` block immediately before the trigger table; enumerates four permitted Type values; states consecutive-row constraint explicitly. |
| C-17 | Anti-Pattern Watch section has a dedicated phase gate | **PASS** | `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===` appears after STEP 8 and before STEP 9, making Anti-Pattern Watch a structurally required section. |

**Aspirational: 9/9 PASS → 10/10 pts**

---

## Composite Score

| Tier | Score |
|------|-------|
| Essential (C-01–C-05) | 60/60 |
| Recommended (C-06–C-08) | 30/30 |
| Aspirational (C-09–C-17) | 10/10 |
| **Total** | **100/100** |

---

## Excellence Signals

**V-01 achieves a perfect score.** The phrasing-register hypothesis is confirmed: converting prose rules to `EMIT:` / `PRODUCE:` / `VERIFY:` command syntax closes the remaining gap between intent and mechanical checkability. Two new patterns emerge that are not yet named in the rubric:

**Pattern 1 — Inline VERIFY blocks as disqualification anchors.** V-01 places a `VERIFY:` block immediately after each `PRODUCE:` command that has a known failure mode. The VERIFY block names the exact disqualifying output ("A merged `Decision Scope` column does not satisfy this step", "Two headcount threshold rows do not satisfy this step", "As we scale... is not a valid breakdown"). This is a distinct mechanism from named vocabulary blocks (ROLE-NAME LOCK, TRIGGER-TYPE VOCABULARY, CAT-N-CITATION-SCHEMA): those enforce what must appear; VERIFY blocks enforce what must *not* appear. The pattern could be extracted as a rubric criterion: "every structural requirement with a known evasion mode has a corresponding VERIFY: block naming the disqualifying variant."

**Pattern 2 — Inner table type vocabulary for the Inertia Mechanism table.** Sub-section 2a applies the same named-enumeration principle to the mechanism `Type` column (`span-of-control / direct-comms / shared-context / single-DRI / low-coordination-cost`) that C-13 applies to roles and C-16 applies to trigger types. This extends the vocabulary-lock pattern into a third inner table. A v6 criterion could enforce that the mechanism table Type vocabulary is emitted as a named block (analogous to ROLE-NAME LOCK and TRIGGER-TYPE VOCABULARY) rather than inlined in prose, making it mechanically verifiable in the same way.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline VERIFY blocks immediately after each PRODUCE command name the exact disqualifying output variant, enforcing what must not appear rather than what must appear — a mechanism distinct from vocabulary-lock blocks and not yet captured as a named rubric pattern", "Inner table Type vocabulary for Inertia Mechanism table (sub-section 2a) applies the named-enumeration principle to a third inner table column but is inlined in prose rather than emitted as a named block — extractable as a v6 criterion requiring a MECHANISM-TYPE VOCABULARY block parallel to ROLE-NAME LOCK and TRIGGER-TYPE VOCABULARY"]}
```
