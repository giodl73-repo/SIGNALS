# signal-check Scorecard — R3

## Scoring Summary

| V | Essential | Recommended | Aspirational | Composite | Gold? |
|---|-----------|-------------|--------------|-----------|-------|
| V-01 | 5/5 | 3/3 | 6/8 (C-09–C-14) | **97.5** | YES |
| V-02 | 5/5 | 3/3 | 6/8 (C-09–C-13 + C-15) | **97.5** | YES |
| V-03 | 5/5 | 3/3 | 6/8 (C-09–C-13 + C-16) | **97.5** | YES |
| V-04 | 5/5 | 3/3 | 7/8 (C-09–C-14 + C-16) | **98.75** | YES |
| V-05 | 5/5 | 3/3 | 8/8 (all) | **100** | YES |

All five gold. Scores match expected exactly.

---

## Key Findings by Criterion

**C-14 (named preamble block):** Passes V-01, V-04, V-05. Fails V-02 (REQUIRED ABSENCE PHRASES table is not a named governance block) and V-03 (distributed constraints are not a consolidated preamble — these are structurally orthogonal).

**C-15 (verbatim phrases per dimension):** Passes V-02 and V-05 only. V-01/V-03/V-04 all fail — structural guidance ("write the absence explicitly") without exact required wording does not satisfy C-15 regardless of how well-framed or well-located the constraint is.

**C-16 (location enumeration):** Passes V-03, V-04, V-05. Fails V-01 ("throughout this output" = generic scope) and V-02 ("applies to this entire output" = generic scope). Named locations, not generic scope, is the threshold.

## Research Question Answers

1. **C-14 alone (V-01):** Improves over per-section reminders but doesn't eliminate drift — no verbatim forms, no propagation scope.
2. **C-15 alone (V-02):** Narrows absence drift via phrase table, but table-lookup dependency remains; embedding at point of use (V-05) is more reliable.
3. **Distributed vs. preamble C-16 (V-03 vs. V-04):** C-16 compliance is equivalent either way — the structural difference is C-14 consolidation, not C-16 propagation.
4. **C-15 over V-04 (V-04 vs. V-05):** Adds 1.25 points. Structural absence obligations + full location scope (V-04) vs. exact required wording per dimension (V-05) — the empirical compliance gap remains untested without execution data.

## Excellence Signals

- Triple enforcement stack (C-14 + C-15 + C-16) addresses three independent failure modes; each is necessary, none substitutes for another
- Verbatim phrases at point of use (V-05) outperform pre-analysis reference tables (V-02) — removes table-lookup dependency
- C-14 and C-16 are structurally orthogonal: consolidation ≠ enumeration
- Preflight/pilot framing in V-05 carries the advisory register structurally, not just declaratively

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verbatim-phrase-at-point-of-use outperforms reference-table for C-15 compliance", "C-14 and C-16 are structurally orthogonal — consolidation and enumeration are independent mechanisms", "triple enforcement stack addresses three distinct failure modes; no two layers substitute for the third"]}
```
 — generic scope. Rule 2: "anywhere in this output" — generic scope. Neither rule lists specific governed locations |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8 (C-09 thru C-14; fail C-15, C-16)
**Composite:** 60 + 30 + 7.5 = **97.5** | **Gold: YES**

---

## V-02: Verbatim Absence Phrase Table (97.5)

**Axis:** C-15 alone — verbatim phrase table, no named block

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All four dimensions present | PASS | All four present |
| C-02 | SEQUENCE grounded in artifact dates | PASS | "Classify artifacts as discovery/commitment. Compare dates." |
| C-03 | COHERENCE names specific signal pairs | PASS | '"Signals seem aligned" without named pairs does not pass' |
| C-04 | CAUSAL GAP states mechanism or names absence | PASS | Required absence phrase (b) provided verbatim |
| C-05 | Advisory/coaching register | PASS | "Coaching check -- not a gate. Advisory throughout." |
| C-06 | STALENESS named concrete threshold | PASS | "Name the threshold first: For {topic}'s domain..." |
| C-07 | Every flagged issue has next action | PASS | Action fields required for FLAG/OPEN |
| C-08 | Readiness summary before dimension analysis | PASS | READINESS SUMMARY section present |
| C-09 | Cross-dimension patterns named | PASS | CROSS-DIMENSION PATTERNS section present |
| C-10 | Missing signals by namespace + skill | PASS | MISSING SIGNAL GUIDE with /namespace:skill |
| C-11 | All skill refs use /namespace:skill format | PASS | SKILL REFERENCE FORMAT declared at top; per-dimension action fields enforce it |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | PASS | MISSING SIGNAL GUIDE terminal section present |
| C-13 | Absent evidence declared explicitly | PASS | REQUIRED ABSENCE PHRASES table + "phrase is required; blank does not pass" per dimension |
| C-14 | Named STANDING RULES block precedes inventory | **FAIL** | REQUIRED ABSENCE PHRASES table and SKILL REFERENCE FORMAT block are not a named governance preamble; neither constitutes a STANDING RULES equivalent per C-14 pass condition |
| C-15 | Each dimension specifies verbatim absence phrases | PASS | REQUIRED ABSENCE PHRASES table provides exact wording for all four dimensions |
| C-16 | Every constraint enumerates all output locations | **FAIL** | SKILL REFERENCE FORMAT: "(applies to this entire output)" — generic scope. REQUIRED ABSENCE PHRASES table has no location enumeration. Neither constraint names specific governed locations |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8 (C-09 thru C-13 + C-15; fail C-14, C-16)
**Composite:** 60 + 30 + 7.5 = **97.5** | **Gold: YES**

---

## V-03: Per-Constraint Location Enumeration (97.5)

**Axis:** C-16 alone — distributed location enumeration, no named block, no verbatim phrases

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All four dimensions present | PASS | All four present |
| C-02 | SEQUENCE grounded in artifact dates | PASS | Artifact classification with date comparison required |
| C-03 | COHERENCE names specific signal pairs | PASS | "Named pairs required — 'signals seem aligned' without names does not pass" |
| C-04 | CAUSAL GAP states mechanism or names absence | PASS | Option (b) "No mechanism evidence found. The causal gap is open." specified |
| C-05 | Advisory/coaching register | PASS | "Coaching check -- not a gate. Nothing here produces a verdict that blocks you." |
| C-06 | STALENESS named concrete threshold | PASS | "Name the threshold: For {topic}'s domain, signals older than [N] days..." |
| C-07 | Every flagged issue has next action | PASS | Action fields required for FLAG/OPEN |
| C-08 | Readiness summary before dimension analysis | PASS | READINESS SUMMARY section |
| C-09 | Cross-dimension patterns named | PASS | CROSS-DIMENSION PATTERNS section |
| C-10 | Missing signals by namespace + skill | PASS | MISSING SIGNAL GUIDE with /namespace:skill |
| C-11 | All skill refs use /namespace:skill format | PASS | SKILL FORMAT constraint distributed with full location enumeration ensures consistent enforcement |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | PASS | MISSING SIGNAL GUIDE terminal section present |
| C-13 | Absent evidence declared explicitly | PASS | ABSENCE constraint distributed with full location enumeration; explicit absence language at each dimension |
| C-14 | Named STANDING RULES block precedes inventory | **FAIL** | No named preamble block; constraints distributed per-section. Design notes confirm: "C-14 requires a single named preamble block consolidating system-wide constraints before any inventory. V-03 distributes constraints per section with cross-references." |
| C-15 | Each dimension specifies verbatim absence phrases | **FAIL** | Absence phrases present (e.g., "No discovery artifacts found -- ordering cannot be established.") but characterized as structural guidance; no table or explicit "required verbatim phrase" framing per dimension |
| C-16 | Every constraint enumerates all output locations | PASS | SKILL FORMAT constraint: "applies to this section AND to all action fields in DIMENSION ANALYSIS, to CROSS-DIMENSION PATTERNS, and to MISSING SIGNAL GUIDE". ABSENCE constraint: same. Each subsequent declaration references "same scope as declared at [prior location]." All governed locations named explicitly. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 6/8 (C-09 thru C-13 + C-16; fail C-14, C-15)
**Composite:** 60 + 30 + 7.5 = **97.5** | **Gold: YES**

---

## V-04: STANDING RULES with Full Location Enumeration (98.75)

**Axis:** C-14 + C-16 combined — named block with explicit location enumeration, no verbatim phrases

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All four dimensions present | PASS | All four present |
| C-02 | SEQUENCE grounded in artifact dates | PASS | Artifact classification with date comparison |
| C-03 | COHERENCE names specific signal pairs | PASS | '"Signals seem aligned" without named pairs does not pass' |
| C-04 | CAUSAL GAP states mechanism or names absence | PASS | Option (b) "No mechanism evidence found. The causal gap is open." specified in CAUSAL GAP section |
| C-05 | Advisory/coaching register | PASS | "Coaching check -- not a gate. Surfaces inconsistencies so you can decide. Nothing here overrides your judgment." |
| C-06 | STALENESS named concrete threshold | PASS | "Name the threshold first: For {topic}'s domain..." |
| C-07 | Every flagged issue has next action | PASS | Action fields required for FLAG/OPEN |
| C-08 | Readiness summary before dimension analysis | PASS | READINESS SUMMARY section placed first |
| C-09 | Cross-dimension patterns named | PASS | CROSS-DIMENSION PATTERNS section with examples; Rule 1 applied |
| C-10 | Missing signals by namespace + skill | PASS | MISSING SIGNAL GUIDE with /namespace:skill; Rule 2 applied |
| C-11 | All skill refs use /namespace:skill format | PASS | Rule 2 with full location enumeration ensures enforcement across all output locations |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | PASS | MISSING SIGNAL GUIDE terminal section with Rule 1 and Rule 2 applied |
| C-13 | Absent evidence declared explicitly | PASS | Rule 1 with location enumeration: "Blank or hedged findings in any of these locations do not pass" |
| C-14 | Named STANDING RULES block precedes inventory | PASS | "STANDING RULES — These rules govern every section of this output. No section is exempt." before ARTIFACT INVENTORY |
| C-15 | Each dimension specifies verbatim absence phrases | **FAIL** | Rule 1 declares "write the absence explicitly" — structural obligation only. No exact required phrases per dimension. Design notes: "Both rules...declare structural absence obligations without specifying exact required wording per dimension." |
| C-16 | Every constraint enumerates all output locations | PASS | Rule 1 "Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS Finding, COHERENCE Finding, cross-dimension patterns, and MISSING SIGNAL GUIDE. Blank or hedged findings in any of these locations do not pass." Rule 2 likewise enumerates all governed locations. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 7/8 (C-09 thru C-14 + C-16; fail C-15 only)
**Composite:** 60 + 30 + 8.75 = **98.75** | **Gold: YES**

---

## V-05: Full v3 Canonical Stack (100)

**Axis:** C-14 + C-15 + C-16 on R2 V-05 base

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All four dimensions present | PASS | All four present (Item 1–4 structure) |
| C-02 | SEQUENCE grounded in artifact dates | PASS | Classify artifacts with dates; compare; forms (a)/(b)/(c) require dating |
| C-03 | COHERENCE names specific signal pairs | PASS | Named pair structure: "[Artifact A, date] and [Artifact B, date] both say [X]"; required absence phrase when no pair |
| C-04 | CAUSAL GAP states mechanism or names absence | PASS | Required verbatim phrase: "No mechanism evidence found -- the causal gap is open." |
| C-05 | Advisory/coaching register | PASS | "preflight check...does not decide whether to fly — it makes sure the pilot sees everything before they decide. Nothing here blocks you." |
| C-06 | STALENESS named concrete threshold | PASS | "First, name the threshold: For {topic}'s domain: signals older than [N] days are stale because [reason]." |
| C-07 | Every flagged issue has next action | PASS | Action (What you can do) field for each item; required for FLAG/OPEN |
| C-08 | Readiness summary before dimension analysis | PASS | READINESS SUMMARY section, "write last — place first in final artifact" |
| C-09 | Cross-dimension patterns named | PASS | CROSS-ITEM PATTERNS section with examples; Rule 1 "if no pattern exists, write 'No cross-item pattern found.'" |
| C-10 | Missing signals by namespace + skill | PASS | MISSING SIGNAL GUIDE with /namespace:skill + examples per gap type |
| C-11 | All skill refs use /namespace:skill format | PASS | Rule 2 with full location enumeration: "Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE." |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | PASS | MISSING SIGNAL GUIDE with examples and Rule 1 applied; both per-item actions and guide present |
| C-13 | Absent evidence declared explicitly | PASS | Rule 1 with location enumeration + required verbatim phrases per dimension = double enforcement |
| C-14 | Named STANDING RULES block precedes inventory | PASS | "STANDING RULES — The following rules apply to every section of this output, without exception." before GATHER YOUR SIGNALS |
| C-15 | Each dimension specifies verbatim absence phrases | PASS | Each dimension has "Required verbatim absence phrase for this item:" with exact wording: CAUSAL GAP ("No mechanism evidence found -- the causal gap is open."), SEQUENCE ("No discovery artifacts found -- ordering cannot be established."), STALENESS ("No dated artifacts found -- staleness cannot be assessed."), COHERENCE ("Only one artifact exists for {topic} -- no comparable pair available to assess coherence.") |
| C-16 | Every constraint enumerates all output locations | PASS | Rule 1: "Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE. Blank or hedged findings in any of those locations do not pass." Rule 2: identical enumeration. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 8/8 (all)
**Composite:** 60 + 30 + 10 = **100** | **Gold: YES**

---

## Criterion Pass Rate Across All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Pass Rate |
|----|------|------|------|------|------|-----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-02 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-03 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-04 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-05 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-06 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-07 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-08 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-09 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-10 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-11 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-12 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-13 | PASS | PASS | PASS | PASS | PASS | 5/5 |
| C-14 | PASS | FAIL | FAIL | PASS | PASS | 3/5 |
| C-15 | FAIL | PASS | FAIL | FAIL | PASS | 2/5 |
| C-16 | FAIL | FAIL | PASS | PASS | PASS | 3/5 |

---

## Excellence Signals (from V-05)

**EX-R3-01 — Triple enforcement stack:**
C-14 (named preamble block) + C-15 (verbatim phrases at point of use) + C-16 (location enumeration) address three distinct failure modes: structural frame, exact wording, and propagation scope. Each layer is independently necessary; the presence of two does not substitute for the third.

**EX-R3-02 — Verbatim phrases at point of use outperform reference tables:**
V-05 places required verbatim phrases directly at each dimension ("Required verbatim absence phrase for this item:"). V-02 places them in a pre-analysis table (REQUIRED ABSENCE PHRASES). The table approach satisfies C-15 structurally but relies on the model referring back — embedding at the point of use removes that dependency.

**EX-R3-03 — Location enumeration is a prerequisite for constraint propagation:**
V-01 and V-02 both have named blocks or phrase tables but fail C-16 because their constraints use generic scope ("throughout this output", "anywhere in this output"). These variations may drift in practice despite strong structural framing. V-04 and V-05 pass C-16 because every constraint names each governed location by role, making violation visible.

**EX-R3-04 — C-14 and C-16 are structurally orthogonal:**
V-03 satisfies C-16 without C-14 (distributed enumeration, no named preamble). V-01 satisfies C-14 without C-16 (named preamble, generic scope). V-04 satisfies both — the named block provides the enforcement frame; location enumeration closes the propagation gap. They are complementary, not redundant.

**EX-R3-05 — Preflight framing (V-05) reinforces advisory register:**
The "pilot/preflight checklist" metaphor in V-05 makes the advisory intent structural, not just declarative. The framing carries C-05 compliance into every section by analogy — the checklist does not decide whether to fly. This is the clearest expression of the advisory register across all five variations.

---

## Research Question Answers (R3)

**Q1: Does C-14 alone improve absence compliance over per-section reminders?**
V-01 (C-14 only) passes C-13 and C-04 — absence declarations are structurally enforced. The named STANDING RULES block establishes an enforcement frame before evidence is encountered. However, without verbatim phrases (C-15), there is drift risk under minimal-inventory conditions. C-14 alone improves compliance over per-section reminders but does not eliminate absence drift.

**Q2: Does C-15 alone close absence drift without a named preamble block?**
V-02 (C-15 only) passes C-13 via the REQUIRED ABSENCE PHRASES table. The table provides exact wording but requires the model to refer back to it from each dimension. Without C-14's enforcement frame and C-16's propagation scope, the table is a reference, not a constraint. C-15 alone narrows absence drift but the table-lookup dependency remains — embedding phrases at point of use (V-05) is more reliable.

**Q3: Does distributed C-16 (V-03) propagate constraints as effectively as preamble C-16 (V-04)?**
Both V-03 and V-04 pass C-16 and achieve the same aspirational count (6/8 vs. 7/8 — the difference is C-14, not C-16). V-03 satisfies C-16 through distributed enumeration; V-04 satisfies it through preamble enumeration. Constraint propagation appears equivalent for C-16 purposes. However, V-03 lacks C-14's consolidation benefit: the enforcement frame is fragmented. The distinction matters for gap visibility, not for C-16 compliance.

**Q4: What does C-15 add when C-14 + C-16 are already present (V-04 vs. V-05)?**
V-04 → V-05: the only change is adding required verbatim phrases per dimension. V-04 has structural absence obligations with full location scope; V-05 adds exact required wording at each dimension's point of use. The composite moves from 98.75 to 100. C-15 adds 1.25 points. The practical question (whether verbatim forms produce more consistent absence declarations than structural guidance + full location scope) is the remaining open empirical claim — R3 isolates the design difference but cannot confirm compliance rates without execution data.

---

## Trace Artifact

No trace artifact available. Scoring derived from skill instruction text only.
