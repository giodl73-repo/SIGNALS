I have all 5 variations fully read. Now scoring.

---

## corps-pr — Round 9 Scorecard

### Criterion Evaluation

---

#### V-01 — Inertia Framing

**Essential (target: 5/5)**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | "Read org.yaml. Extract: All defined roles and their domain scope" |
| C-02 | PASS | ROUTING SUMMARY block with "one line per role naming the files that triggered it" |
| C-03 | PASS | Findings table per role in Step 5b |
| C-04 | PASS | Step 7 GO / GO WITH CONDITIONS / NO-GO |
| C-05 | PASS | Domain-Lens Gate rule with binary test ("Would only this role raise this?") and rewrite consequence |

**Recommended (target: 3/3)**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | IA activated first from org.yaml |
| C-07 | PASS | "[Role name] total: [N] findings — [x] P1, [y] P2, [z] P3" |
| C-08 | PASS | AMEND SCOPE DISCLOSURE block with template slots (a)–(d) |

**Aspirational (target: 24/24)**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Step 6: "Identify the architectural mechanism that explains the divergence — not the difference in perspective" |
| C-10 | PASS | GO WITH CONDITIONS names "(b) which role must confirm resolution before merge" |
| C-11 | PASS | IA sequenced first (Step 4 before Step 5); cost ledger provides reference baseline for technical roles |
| C-12 | PASS | "structural or code-level reason one role sees higher risk" named in consensus |
| C-13 | PASS | Enumerated ban list with 4 explicit surface forms |
| C-14 | PASS | Step 5b C-31 requirement: Description must name IA cost position AND disagreeing mechanism |
| C-15 | PASS | Binary test + "revise before including" rewrite consequence |
| C-16 | PASS | AMEND SCOPE DISCLOSURE is a named template block, not prose instruction |
| C-17 | PASS | "status quo's budget authority... not to list risks — it is to state what the current system costs" |
| C-18 | **FAIL** | Numbered STEPs without formal named phases; no entry/exit conditions labeled as such |
| C-19 | PASS | Cost ledger with named rows + columns; Budget verdict + Budget strength terminal fields |
| C-20 | **FAIL** | No pipeline declaration; "in routing order, after the IA" is not a declared entry condition |
| C-21 | PASS | Net Direction per row; "Conclusion must cite which rows drove it" |
| C-22 | **FAIL** | No C1/C2 dual-clause sub-conditions |
| C-23 | **FAIL** | No IA READ RECEIPT block |
| C-24 | PASS | Named-field table with Domain-Lens Gate column |
| C-25 | PASS | Three-clause formula, "each clause appears on its own line with no other label or value on the same line" |
| C-26 | **FAIL** | No C1 RESULT / C2 RESULT output lines |
| C-27 | PASS | PRE-COMMITMENT block is labeled, appears before findings, closes with [PRE-COMMITMENT SEALED] |
| C-28 | PASS | "Each clause appears on its own line with no other label or value on the same line" |
| C-29 | PASS | "[PRE-COMMITMENT SEALED] must appear as a distinct output line... No PR diff file, function, or line reference may appear before this token" |
| C-30 | **FAIL** | No pipeline declaration → no Phase C exit condition to name PRE-COMMITMENT as gate item |
| C-31 | PASS | IA counterpoint required inside Description field of a specific finding, with example and negative examples |
| C-32 | **FAIL** | No READ RECEIPT → no cross-reference for fields (d) and (e) |

**Aspirational: 17/24**  
**Score: (5/5 × 60) + (3/3 × 30) + (17/24 × 10) = 60 + 30 + 7.08 = 97.08**

---

#### V-02 — Lifecycle Emphasis

**Essential: 5/5**  
All pass. C-05: "Domain-Lens Gate: ask for each finding — 'Would only this role raise this given their domain?' Revise until the test passes."

**Recommended (target: 3/3)**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | IA activated first from org.yaml |
| C-07 | PASS | "[Role]: [N] findings — [x] P1, [y] P2, [z] P3" |
| C-08 | **FAIL** | No AMEND mode handling anywhere in V-02 |

**Aspirational**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase D: "Name the architectural mechanism that explains the divergence" |
| C-10 | PASS | GO WITH CONDITIONS with "(a) resolution required and (b) named role responsible" |
| C-11 | PASS | Phase B runs before Phase C; IA section is explicit reference baseline |
| C-12 | PASS | "structural or code-level reason — not a perspective difference" |
| C-13 | PASS | 5-item enumerated ban list |
| C-14 | PASS | Phase C exit: "at least one finding per role contains an IA counterpoint in its body text" |
| C-15 | PASS | Binary test + rewrite consequence; "Revise until the test passes" |
| C-16 | **FAIL** | No AMEND mode → no structured AMEND disclosure block exists |
| C-17 | PASS | "budget authority position: what does the current system cost to maintain?" |
| C-18 | PASS | PIPELINE DECLARATION with Phases A–D, each with Entry/Exit/Gates; domain-lens is Phase C exit gate |
| C-19 | PASS | Named-row × named-column cost ledger; Budget verdict + Budget strength |
| C-20 | PASS | Phase C entry: "C1: Phase B pre-flight checklist... C2: Per-role IA read prerequisite — before each role generates findings: The role cites specific Phase B content" |
| C-21 | PASS | Net Direction per row; Conclusion derives from WORSE/BETTER row list |
| C-22 | PASS | Two independently auditable sub-conditions with separate C1/C2 RESULT output lines declared |
| C-23 | PASS | Per-role IA READ RECEIPT block appears before findings (lines 391–405) |
| C-24 | PASS | Named-field findings table with Domain-Lens Gate column |
| C-25 | PASS | "Each labeled clause on its own line, independently retrievable by line-scan. No two clauses share a line." |
| C-26 | **FAIL** | C2 RESULT appears after PRE-COMMITMENT but **before** READ RECEIPT; C-26 requires it after READ RECEIPT |
| C-27 | PASS | PRE-COMMITMENT block with [PRE-COMMITMENT SEALED] seal token, precedes findings |
| C-28 | PASS | "No two clauses share a line. No clause is embedded in prose" |
| C-29 | PASS | [PRE-COMMITMENT SEALED] token as distinct closing line before any diff content |
| C-30 | PASS | Phase B exit check: "PRE-COMMITMENT blocks precede findings tables (C-30 gate item)"; Phase C exit also names it |
| C-31 | PASS | "IA Counterpoint in finding body (C-31): at least one finding's Description field must contain the IA's cost position AND this role's disagreeing mechanism in the same text" |
| C-32 | PASS | READ RECEIPT fields (d) and (e) use "see PRE-COMMITMENT block — (d/e)" cross-reference syntax |

**Aspirational: 22/24** (fails C-16, C-26)  
**Score: (5/5 × 60) + (2/3 × 30) + (22/24 × 10) = 60 + 20 + 9.17 = 89.17**

---

#### V-03 — Output Format

**Essential: 5/5**  
All pass. Domain-Lens Gate rule includes binary test and "revise it to name the domain-specific mechanism" rewrite consequence.

**Recommended: 3/3**  
All pass. AMEND CHECK box-template with named fields (a)–(d). Role summary line template. IA activated from org.yaml.

**Aspirational**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | CONSENSUS BLOCK: "Mechanism: [structural or code-level reason — not a perspective label — naming the specific component, guard, or path]" |
| C-10 | PASS | "RECOMMENDATION: GO WITH CONDITIONS / 1. [What must be resolved] — sign-off: [Role responsible]" |
| C-11 | PASS | "IA REVIEW BLOCK: Produce this block before any technical role section" |
| C-12 | PASS | Mechanism explanation required; "structural or code-level reason" |
| C-13 | PASS | 5-item enumerated ban list as "Prohibited explanation forms" |
| C-14 | PASS | "IA Counterpoint rule (C-31): At least one finding in this role's table must contain an IA counterpoint inside the Description field" |
| C-15 | PASS | Binary test + rewrite consequence; example shows domain-specific mechanism replacement |
| C-16 | PASS | AMEND CHECK uses box-border template with named field slots (a)–(d) |
| C-17 | PASS | "Inertia Advocate is the status quo's budget authority" with cost ledger |
| C-18 | **FAIL** | Sections (IA REVIEW BLOCK, TECHNICAL ROLE BLOCK TEMPLATE, etc.) are not named phases with entry/exit conditions |
| C-19 | PASS | IA COST LEDGER template with named rows and columns; Budget verdict + Budget strength |
| C-20 | **FAIL** | No pipeline declaration with phase entry conditions |
| C-21 | PASS | Net Direction column in ledger; Budget verdict derived from WORSE/BETTER rows |
| C-22 | **FAIL** | No C1/C2 sub-conditions |
| C-23 | PASS | "[Role Name] — IA READ RECEIPT" block precedes findings table |
| C-24 | PASS | Named-field findings table with Domain-Lens Gate column |
| C-25 | PASS | "Each clause on its own line. No two clauses share a line" |
| C-26 | **FAIL** | No C1 RESULT / C2 RESULT output lines |
| C-27 | PASS | PRE-COMMITMENT block closes with [PRE-COMMITMENT SEALED]; precedes diff references |
| C-28 | PASS | "Each clause on its own line. No two clauses share a line" |
| C-29 | PASS | "[PRE-COMMITMENT SEALED] is a required output line. It closes the block." |
| C-30 | **FAIL** | No phase gate pipeline → no Phase C exit condition to name PRE-COMMITMENT as gate item |
| C-31 | PASS | "The counterpoint names: (i) the IA's specific cost position... and (ii) the architectural mechanism... Both (i) and (ii) appear in the same Description cell." With compliant example. |
| C-32 | PASS | READ RECEIPT template has "(d) Cost row most relevant: see PRE-COMMITMENT block — (d) [row name]" and "(e) Initial position: see PRE-COMMITMENT block — (e) committed above" |

**Aspirational: 19/24** (fails C-18, C-20, C-22, C-26, C-30)  
**Score: (5/5 × 60) + (3/3 × 30) + (19/24 × 10) = 60 + 30 + 7.92 = 97.92**

---

#### V-04 — Phase Gates + Inertia Framing (Combined)

**Essential: 5/5**  
All pass. C-05: "per finding, test 'Would only this role raise this given their domain?' Revise until the test passes."

**Recommended: 3/3**  
All pass. AMEND SCOPE DISCLOSURE block with template slots. Per-role summary. IA from org.yaml.

**Aspirational**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase D: "State the architectural mechanism — a structural, code-level reason one role rates higher. Name the component, guard, path, or interface." |
| C-10 | PASS | "Condition 1: [what] — confirmed by: [role]" |
| C-11 | PASS | Phase B before Phase C in pipeline declaration; IA ledger is the baseline technical roles pre-commit against |
| C-12 | PASS | "structural, code-level reason" naming mechanism required |
| C-13 | PASS | 6-item enumerated ban list |
| C-14 | PASS | "IA Counterpoint — finding body placement (C-31): at least one finding's Description field must contain both (i) the IA's cost verdict... and (ii) the architectural mechanism" — named Phase C exit condition |
| C-15 | PASS | Binary test + rewrite; "Write 'Passed' only after the test is applied" |
| C-16 | PASS | AMEND SCOPE DISCLOSURE is a named template block with fields (a)–(d) |
| C-17 | PASS | "The IA holds a budget authority position. Their output is a cost ledger and a three-clause verdict, not a list of concerns." |
| C-18 | PASS | Phases A–D with explicit "Entry condition" and "Exit conditions" labels; domain-lens gate in Phase C exit |
| C-19 | PASS | Cost ledger with named rows + columns; Budget verdict + Budget strength terminal fields |
| C-20 | PASS | Phase C C1: "Before Phase C begins, verify: [ ] Cost ledger has maintenance burden and incident exposure rows..." — IA phase completion declared as pre-flight entry gate |
| C-21 | PASS | Net Direction per row; "verdict explicitly derived from the named row directions" |
| C-22 | PASS | "two independently auditable sub-conditions: C1 (pre-flight checklist)... C2 (per-role IA read prerequisite)" with separate output lines |
| C-23 | PASS | "Step C.3 — IA READ RECEIPT" block appears between PRE-COMMITMENT and Findings |
| C-24 | PASS | Named-field findings table with Domain-Lens Gate column |
| C-25 | PASS | "Output on exactly three lines. Each label at line start, nothing else on that line." |
| C-26 | **FAIL** | C2 RESULT (Step C.2) appears after PRE-COMMITMENT but **before** READ RECEIPT (Step C.3); C-26 requires C2 RESULT after READ RECEIPT |
| C-27 | PASS | PRE-COMMITMENT block with [PRE-COMMITMENT SEALED] seal token precedes diff content |
| C-28 | PASS | "Each label at line start, nothing else on that line" |
| C-29 | PASS | [PRE-COMMITMENT SEALED] explicit seal line closes PRE-COMMITMENT block |
| C-30 | PASS | Phase B exit: "PRE-COMMITMENT blocks for Phase C precede all diff content ← named Phase B exit gate for C-30 compliance; absence of PRE-COMMITMENT blocks is a Phase B exit violation, not merely a format issue" |
| C-31 | PASS | Named Phase C exit condition: "A role section where the IA counterpoint appears only as a section-level element outside all finding cells fails this Phase C exit condition." |
| C-32 | PASS | Phase C exit: "All READ RECEIPTs complete with (d) and (e) present or cross-referenced"; receipt template shows "see PRE-COMMITMENT block — (d/e)" syntax |

**Aspirational: 23/24** (fails C-26 only — ordering gap)  
**Score: (5/5 × 60) + (3/3 × 30) + (23/24 × 10) = 60 + 30 + 9.58 = 99.58**

---

#### V-05 — All Axes Combined (Maximum Structure)

**Essential: 5/5**  
All pass. C-05: binary test + rewrite consequence; "Apply this test before writing each finding."

**Recommended: 3/3**  
All pass. PRE-RUN AMEND CHECK box template with named fields. Per-role summary. IA from org.yaml.

**Aspirational**

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase D: "Name the architectural mechanism explaining the divergence. This is a code-level, structural, or interface-level reason — not a framing difference" |
| C-10 | PASS | "Sign-off required from: [Role name]" per condition |
| C-11 | PASS | PIPELINE DECLARATION: Phase B (IA) before Phase C; IA ledger is the baseline |
| C-12 | PASS | "code-level, structural, or interface-level reason... Name the component, guard, path, or interface" |
| C-13 | PASS | 7-item enumerated ban list with rewrite trigger instruction |
| C-14 | PASS | Phase C exit gate per role: "At least one finding's Description contains IA counterpoint with both (i) IA cost position and (ii) disagreeing mechanism" |
| C-15 | PASS | "Test: 'Would only this role raise this finding given their domain scope?' If any generic reviewer could write the same sentence, revise before including." |
| C-16 | PASS | AMEND SCOPE DISCLOSURE is a box-template with named field slots (a)–(d) |
| C-17 | PASS | "Output a cost ledger and a three-clause verdict. Do not list concerns. Frame as tradeoffs with explicit cost terms." |
| C-18 | PASS | PIPELINE DECLARATION with box-format table showing all four phases with Entry/Exit/Gates; domain-lens gate in Phase C exit |
| C-19 | PASS | Cost ledger (B.1), Budget verdict (B.2), Budget strength (B.3) |
| C-20 | PASS | PIPELINE DECLARATION Phase C entry: "C1 pre-flight Phase B exit checklist (ALL CLEAR required) / C2 per-role IA read prerequisite (verified per role)" |
| C-21 | PASS | Net Direction column per row; "Conclusion must cite which rows drove it" |
| C-22 | PASS | C.0 pre-flight + per-role C.2 sequence; "A BLOCKED result halts Phase C." |
| C-23 | PASS | "C.3 — IA READ RECEIPT" block appears before findings table |
| C-24 | PASS | Named-field findings table with Domain-Lens Gate column |
| C-25 | PASS | "Three clauses. Each on its own output line. No clause shares its line with another label or value. Each label appears at line start." |
| C-26 | **FAIL** | C2 RESULT (C.2) appears after PRE-COMMITMENT but **before** READ RECEIPT (C.3); C-26 requires C2 RESULT after READ RECEIPT |
| C-27 | PASS | "[PRE-COMMITMENT SEALED] is a required output line. It closes the block. All PR diff references follow after this line." |
| C-28 | PASS | "No clause shares its line with another label or value. Each label appears at line start." |
| C-29 | PASS | "[PRE-COMMITMENT SEALED]" as required output line closing the block before any diff content |
| C-30 | PASS | Phase B exit gate: "PRE-COMMITMENT blocks precede findings tables ← compliance item; absence is a Phase B exit violation"; also in PIPELINE DECLARATION Phase B exit |
| C-31 | PASS | Extensive specification: both (i) and (ii) required in same Description cell; compliant example provided; four non-compliant forms enumerated and prohibited |
| C-32 | PASS | Dual-form compliance explicitly declared: "cross-reference form: 'see PRE-COMMITMENT block — (d/e) [value]'" OR "Inline restatement: write the value directly in the receipt" |

**Aspirational: 23/24** (fails C-26 only — same ordering gap as V-04)  
**Score: (5/5 × 60) + (3/3 × 30) + (23/24 × 10) = 60 + 30 + 9.58 = 99.58**

---

### Score Summary

| Rank | Variation | Essential | Recommended | Aspirational | **Composite** |
|------|-----------|-----------|-------------|-------------|-------------|
| 1 (tie) | **V-04** Phase gates + IA framing | 5/5 = 60 | 3/3 = 30 | 23/24 = 9.58 | **99.58** |
| 1 (tie) | **V-05** All axes | 5/5 = 60 | 3/3 = 30 | 23/24 = 9.58 | **99.58** |
| 3 | V-03 Output format | 5/5 = 60 | 3/3 = 30 | 19/24 = 7.92 | **97.92** |
| 4 | V-01 Inertia framing | 5/5 = 60 | 3/3 = 30 | 17/24 = 7.08 | **97.08** |
| 5 | V-02 Lifecycle emphasis | 5/5 = 60 | 2/3 = 20 | 22/24 = 9.17 | **89.17** |

---

### Tiebreaker: V-04 vs V-05

Both score 99.58. V-05 edges V-04 on documentation robustness:

1. **C-31 non-compliant form enumeration** — V-05 explicitly lists four non-compliant C-31 forms (section-level anchor, section footer, trailing bullet, introductory paragraph). This makes false-positive compliance visible and eliminates the ambiguity that caused R8 PARTIAL scores. V-04 names only one non-compliant form ("not a separate 'IA Position:' block... not a section header... not a trailing bullet").

2. **Per-role Phase C exit gate checklist** — V-05 provides a per-role exit checklist at C.5 with 6 named items, making it impossible to advance past a role section without all conditions met. V-04 combines all role exit conditions at the phase level, reducing per-role enforcement granularity.

3. **C-32 dual-form compliance explicitly named** — V-05 names both acceptable forms ("cross-reference form" and "Inline restatement") as variant labels, not just describes them. This prevents a model from rejecting a valid restatement for not matching the cross-reference exact syntax.

**Golden: V-05**

---

### Universal Gap: C-26 Ordering

All three variations implementing C1/C2 (V-02, V-04, V-05) place C2 RESULT **after PRE-COMMITMENT but before READ RECEIPT**. C-26 requires C2 RESULT to appear **after the IA READ RECEIPT**. The intent of C-26 is for C2 RESULT to confirm the receipt is complete and fully cites Phase B content. The current ordering has C2 verify the PRE-COMMITMENT block instead, then produces the READ RECEIPT as a downstream artifact.

**R10 hypothesis**: Move C2 RESULT to appear after the READ RECEIPT block (making C2 a receipt completeness confirmation rather than a PRE-COMMITMENT verification), and produce a separate PRE-COMMITMENT verification step (C.1b or C2-pre) immediately after the PRE-COMMITMENT seal. This closes C-26 while retaining the pre-commitment timing evidence.

---

### Excellence Signals from V-05 (top variation)

**1. C-31 non-compliant form enumeration as a phase gate item**  
V-05 specifies 4 non-compliant C-31 forms by description, not just by label. This converts C-31 from "must have IA counterpoint in body text" to a checklist with named failure modes — making false positives into named gate violations rather than judgment calls.

**2. Per-role Phase C exit gate as a recurring checklist**  
V-05 closes each role section with a 6-item checklist `[ ]`. This enforces C-31 and C-32 at the role level before the model proceeds to the next role, preventing silent skips. Prior variations checked these at the phase level only.

**3. C-32 dual-form compliance with explicit form labels**  
V-05 names the two acceptable forms as "cross-reference form" and "Inline restatement" rather than describing them in prose. This makes compliance checkable by form recognition rather than content parsing.

---

```json
{"top_score": 99.58, "all_essential_pass": true, "new_patterns": ["C-31 non-compliant form enumeration as named gate items", "per-role Phase C exit gate checklist enforces C-31 and C-32 before role section closes", "C-32 dual-form compliance (cross-reference or inline restatement) explicitly named as variant labels"]}
```
