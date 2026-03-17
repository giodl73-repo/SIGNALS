## Quest Score — corps-chart (Round 8)

### Variation Scoring

---

#### V-01 — UPFRONT FORMAT CONTRACT (single axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION with closed vocabulary | PASS | Uses exact closed set: (strategic) / (operational) / (advisory) / (governance) |
| C-02 | ASCII diagram with committee nodes | PASS | Explicit: "Committees appear as distinct labeled nodes — not embedded in an area box" |
| C-03 | Headcount table five columns, separate Decides/Escalates | PASS | FORMAT CONTRACT schema (1) names all five columns; NOTE disqualifies "Decision Scope" |
| C-04 | Rhythm table ≥3 distinct rows | PASS | Schema (2) requires ROB, shiproom/gate, governance; "Two meetings must not be merged" |
| C-05 | Charter five fields with Quorum fraction form | PASS | Schema (3) specifies `[N] of [M]`; NOTE disqualifies denominator-free form |
| C-06 | Inertia Assessment with FLAT-CASE-PRESSURE + verdict | PASS | All four sub-sections structured; rating from closed set; concrete trigger required |
| C-07 | ORG-ELEMENT REGISTER all four categories | PASS | All four cat-N categories required per schema (4) |
| C-08 | Section order with all four phase gates | PASS | All four gates listed in SECTION ORDER in correct sequence |
| C-09 | Anti-Pattern Watch typed cat-N citations | PASS | Schema (5) specifies `[element name] (cat-N) —` prefix; explicit NOTE on invalid form |
| C-10 | Org Evolution Roadmap two distinct trigger categories | PASS | "Row 2: a different category… DO NOT use two headcount thresholds" |
| C-11 | Rebuttal role-grounded with concrete trigger | PARTIAL | Re-assessment trigger required in VERDICT; Rebuttal does not mandate naming a specific role |
| C-12 | Role-name coherence across all sections | PARTIAL | Diagram instruction covers naming; DRI/Owner says "where possible" — not strict for all sections |
| C-13 | ROLE-NAME LOCK block after classification | FAIL | No ROLE-NAME LOCK block present |
| C-14 | Rebuttal uses four-field form | FAIL | No four-field form; sub-section 3 is prose-only |
| C-15 | CAT-N-CITATION-SCHEMA block before Anti-Pattern Watch | FAIL | Cat-N format declared in FORMAT CONTRACT at top, not as a named block immediately before the table |
| C-16 | TRIGGER-TYPE VOCABULARY block for Roadmap | FAIL | No TRIGGER-TYPE VOCABULARY block; trigger categories prose-only |
| C-17 | 5th phase gate (ORG-EVOLUTION → ANTI-PATTERN) | FAIL | Section order lists only four gates |
| C-18 | VERIFY blocks for three known evasion modes | FAIL | FORMAT CONTRACT flags invalid forms but no VERIFY blocks at PRODUCE commands |
| C-19 | MECHANISM-TYPE VOCABULARY block for mechanism table | FAIL | Type vocabulary inline in prose, not a named block |
| C-20 | UPFRONT FORMAT CONTRACT with all five schemas | PASS | Full FORMAT CONTRACT block pre-declares all five schemas before first phase gate |
| C-21 | ROLE-NAME LOCK with inline CHECKs at every use site | FAIL | No ROLE-NAME LOCK |
| C-22 | Vocabulary-lock + VERIFY co-deployed for every governed table | FAIL | No vocabulary-lock blocks; no VERIFY blocks at PRODUCE commands |

**Aspirational score**: 3 PASS × 0.714 + 2 PARTIAL × 0.36 = 2.14 + 0.72 = **2.86**
**Total: 60 + 30 + 2.86 = 92.86**

---

#### V-02 — ROLE-NAME LOCK with Inline CHECKs (single axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION closed vocabulary | PASS | Assigns `(strategic) / (operational) / (advisory) / (governance)` |
| C-02 | ASCII diagram with committee nodes | PASS | Explicit requirement |
| C-03 | Headcount table five columns | PASS | "Five columns required. DO NOT merge Decides and Escalates" |
| C-04 | Rhythm table ≥3 rows | PASS | "Minimum three rows: ROB, shiproom or gate meeting, governance meeting" |
| C-05 | Charter five fields with Quorum fraction | PASS | `[N] of [M] member roles required` specified |
| C-06 | Inertia Assessment structure | PASS | Full four sub-sections; FLAT-CASE-PRESSURE from closed set |
| C-07 | ORG-ELEMENT REGISTER | PASS | All four categories required |
| C-08 | Section order four phase gates | PASS | All four gates in SECTION ORDER |
| C-09 | Anti-Pattern Watch typed citations | PASS | `[element name] (cat-N) — [one sentence]` required |
| C-10 | Roadmap two distinct trigger categories | PASS | "DO NOT use two headcount thresholds" |
| C-11 | Rebuttal role-grounded | PARTIAL | CHECK constrains names used, but does not mandate naming a specific role as the failure point |
| C-12 | Role-name coherence all sections | PASS | ROLE-NAME LOCK + CHECKs at diagram, Key Roles, DRI/Owner, Membership/Decides, Rebuttal |
| C-13 | ROLE-NAME LOCK block | PASS | Named block emitted immediately after ROLE-TYPE-CLASSIFICATION |
| C-14 | Rebuttal four-field form | FAIL | No four-field form; Rebuttal is prose with a CHECK |
| C-15 | CAT-N-CITATION-SCHEMA block | FAIL | Cat-N format stated in ANTI-PATTERN WATCH prose, no named schema block |
| C-16 | TRIGGER-TYPE VOCABULARY block | FAIL | No vocabulary block for roadmap |
| C-17 | 5th phase gate | FAIL | Four gates only |
| C-18 | VERIFY blocks for three evasion modes | FAIL | No VERIFY blocks |
| C-19 | MECHANISM-TYPE VOCABULARY block | FAIL | No named vocabulary block; Type values listed inline |
| C-20 | UPFRONT FORMAT CONTRACT | FAIL | No FORMAT CONTRACT |
| C-21 | ROLE-NAME LOCK with inline CHECKs at every use site | PARTIAL | CHECKs at diagram, Key Roles, DRI/Owner, Membership/Decides, and Rebuttal; but no ROLE UNDER PRESSURE field (four-field form absent), leaving the specific Inertia sub-section role-selection gap open |
| C-22 | Vocabulary-lock + VERIFY co-deployment | FAIL | No vocabulary-lock blocks; no VERIFY blocks |

**Aspirational score**: 4 PASS × 0.714 + 2 PARTIAL × 0.36 = 2.86 + 0.72 = **3.58**
**Total: 60 + 30 + 3.58 = 93.58**

---

#### V-03 — Vocabulary-Lock + VERIFY Co-Deployment (single axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION closed vocabulary | PASS | Correct closed set |
| C-02 | ASCII diagram | PASS | Committees as distinct nodes |
| C-03 | Headcount five columns | PASS | Five columns; VERIFY disqualifies merged column |
| C-04 | Rhythm table ≥3 rows | PASS | Three required rows |
| C-05 | Charter five fields Quorum fraction | PASS | Fraction form; VERIFY disqualifies short form |
| C-06 | Inertia Assessment | PASS | All sub-sections; MECHANISM-TYPE VOCABULARY; FLAT-CASE-PRESSURE from closed set |
| C-07 | ORG-ELEMENT REGISTER | PASS | All four categories |
| C-08 | Four phase gates in order | PASS | All four present |
| C-09 | Anti-Pattern Watch typed citations | PASS | CAT-N-CITATION-SCHEMA block + VERIFY |
| C-10 | Roadmap two distinct trigger categories | PASS | TRIGGER-TYPE VOCABULARY + VERIFY blocks |
| C-11 | Rebuttal role-grounded | PARTIAL | VERIFY blocks prevent future-tense prose; but no mandate to name a specific role from ROLES-LOADED |
| C-12 | Role-name coherence all sections | PARTIAL | Diagram covered; DRI/Owner not explicitly locked |
| C-13 | ROLE-NAME LOCK block | FAIL | No ROLE-NAME LOCK |
| C-14 | Rebuttal four-field form | FAIL | No four-field form |
| C-15 | CAT-N-CITATION-SCHEMA block | PASS | Named block immediately before Anti-Pattern Watch table |
| C-16 | TRIGGER-TYPE VOCABULARY block | PASS | Named block before trigger table; no-consecutive-same-type constraint stated |
| C-17 | 5th phase gate | FAIL | Section order has four gates only |
| C-18 | VERIFY blocks for three evasion modes | PASS | VERIFY at headcount (merged column), roadmap (duplicate threshold), Rebuttal (future-tense) |
| C-19 | MECHANISM-TYPE VOCABULARY block | PASS | Named block before mechanism table |
| C-20 | UPFRONT FORMAT CONTRACT | FAIL | No FORMAT CONTRACT |
| C-21 | ROLE-NAME LOCK with inline CHECKs | FAIL | No ROLE-NAME LOCK |
| C-22 | Vocabulary-lock + VERIFY co-deployment | PASS | All four pairings: mechanism type, trigger type, cat-N citation, Quorum fraction |

**Aspirational score**: 7 PASS × 0.714 + 2 PARTIAL × 0.36 = 5.00 + 0.72 = **5.72**
**Total: 60 + 30 + 5.72 = 95.72**

---

#### V-04 — FORMAT CONTRACT + Vocabulary-Lock/VERIFY Pairs

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION closed vocabulary | PASS | Correct closed set |
| C-02 | ASCII diagram | PASS | Committees as distinct nodes |
| C-03 | Headcount five columns | PASS | FORMAT CONTRACT schema (1) + VERIFY |
| C-04 | Rhythm table ≥3 rows | PASS | Schema (2) + three-row minimum |
| C-05 | Charter five fields Quorum fraction | PASS | Schema (3) + VERIFY disqualifies short form |
| C-06 | Inertia Assessment | PASS | All sub-sections; MECHANISM-TYPE VOCABULARY; FLAT-CASE-PRESSURE from closed set |
| C-07 | ORG-ELEMENT REGISTER | PASS | All four categories per schema (4) |
| C-08 | Four phase gates in order | PASS | All four present |
| C-09 | Anti-Pattern Watch typed citations | PASS | FORMAT CONTRACT schema (5) + CAT-N-CITATION-SCHEMA + VERIFY |
| C-10 | Roadmap two distinct trigger categories | PASS | TRIGGER-TYPE VOCABULARY + VERIFY |
| C-11 | Rebuttal role-grounded | PARTIAL | VERIFY blocks prevent future-tense; no mandatory role-naming in Rebuttal |
| C-12 | Role-name coherence all sections | PARTIAL | "Role names from ROLES-LOADED only" for diagram; no strict lock on rhythm/charter sections |
| C-13 | ROLE-NAME LOCK block | FAIL | No ROLE-NAME LOCK |
| C-14 | Rebuttal four-field form | FAIL | No four-field form |
| C-15 | CAT-N-CITATION-SCHEMA block | PASS | Named block before Anti-Pattern Watch; FORMAT CONTRACT schema (5) provides redundant reference |
| C-16 | TRIGGER-TYPE VOCABULARY block | PASS | Named block before trigger table |
| C-17 | 5th phase gate | PASS | `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===` present |
| C-18 | VERIFY blocks for three evasion modes | PASS | VERIFY at headcount, roadmap, Rebuttal |
| C-19 | MECHANISM-TYPE VOCABULARY block | PASS | Named block before mechanism table |
| C-20 | UPFRONT FORMAT CONTRACT | PASS | All five schemas pre-declared before first STEP |
| C-21 | ROLE-NAME LOCK with inline CHECKs | FAIL | No ROLE-NAME LOCK |
| C-22 | Vocabulary-lock + VERIFY co-deployment | PASS | All four pairings present |

**Aspirational score**: 9 PASS × 0.714 + 2 PARTIAL × 0.36 = 6.43 + 0.72 = **7.15**
**Total: 60 + 30 + 7.15 = 97.15**

---

#### V-05 — Full Integration

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION closed vocabulary | PASS | Correct closed set in STEP 2 |
| C-02 | ASCII diagram | PASS | STEP 5: committees as distinct nodes; CHECK on role names |
| C-03 | Headcount five columns | PASS | FORMAT CONTRACT schema (1) + VERIFY at STEP 6 + CHECK on Key Roles |
| C-04 | Rhythm table ≥3 rows | PASS | Schema (2) + STEP 7 minimum three rows |
| C-05 | Charter five fields Quorum fraction | PASS | Schema (3) + VERIFY at STEP 8 |
| C-06 | Inertia Assessment | PASS | All sub-sections; MECHANISM-TYPE VOCABULARY; FLAT-CASE-PRESSURE from closed set |
| C-07 | ORG-ELEMENT REGISTER | PASS | All four categories required per schema (4), STEP 9 |
| C-08 | Four phase gates in order | PASS | All four present in correct sequence |
| C-09 | Anti-Pattern Watch typed citations | PASS | FORMAT CONTRACT schema (5) + CAT-N-CITATION-SCHEMA + VERIFY at STEP 11 |
| C-10 | Roadmap two distinct trigger categories | PASS | TRIGGER-TYPE VOCABULARY + VERIFY at STEP 10 |
| C-11 | Rebuttal role-grounded with concrete trigger | PASS | Four-field form: ROLE UNDER PRESSURE names one role from LOCK list; OBSERVABLE BREAKDOWN requires current failure; RE-ASSESSMENT TRIGGER is concrete |
| C-12 | Role-name coherence across all sections | PASS | ROLE-NAME LOCK + CHECKs at diagram (STEP 5), Key Roles (STEP 6), DRI/Owner (STEP 7), Membership/Decides (STEP 8), Rebuttal (STEP 4 sub-section 3) |
| C-13 | ROLE-NAME LOCK block | PASS | STEP 3 emits named block immediately after ROLE-TYPE-CLASSIFICATION |
| C-14 | Rebuttal four-field form | PASS | Mandatory form with ROLE UNDER PRESSURE, OBSERVABLE BREAKDOWN, WHY EXISTING MECHANISMS FAIL, RE-ASSESSMENT TRIGGER |
| C-15 | CAT-N-CITATION-SCHEMA block | PASS | Named block before Anti-Pattern Watch table at STEP 11 |
| C-16 | TRIGGER-TYPE VOCABULARY block | PASS | Named block before trigger table at STEP 10 |
| C-17 | 5th phase gate | PASS | `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===` in SECTION ORDER |
| C-18 | VERIFY blocks for three evasion modes | PASS | VERIFY at headcount (STEP 6), roadmap (STEP 10), Rebuttal (four-field form VERIFY) |
| C-19 | MECHANISM-TYPE VOCABULARY block | PASS | Named block before mechanism table in STEP 4 |
| C-20 | UPFRONT FORMAT CONTRACT all five schemas | PASS | All five schemas declared before STEP 1 |
| C-21 | ROLE-NAME LOCK with inline CHECKs at every use site | PASS | CHECKs at STEP 4 Rebuttal (including ROLE UNDER PRESSURE), STEP 5 diagram, STEP 6 Key Roles, STEP 7 DRI/Owner, STEP 8 Membership/Decides |
| C-22 | Vocabulary-lock + VERIFY co-deployment | PASS | All four pairings: mechanism type (STEP 4), headcount VERIFY (STEP 6), Quorum VERIFY (STEP 8), trigger type (STEP 10), cat-N citation (STEP 11) |

**Aspirational score**: 14 PASS × 0.714 = **10.00**
**Total: 60 + 30 + 10.00 = 100.00**

---

### Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Full Integration | **100.0** | Yes |
| 2 | V-04 FORMAT CONTRACT + Vocab/VERIFY | **97.2** | Yes |
| 3 | V-03 Vocab/VERIFY Co-Deployment | **95.7** | Yes |
| 4 | V-02 ROLE-NAME LOCK + CHECKs | **93.6** | Yes |
| 5 | V-01 FORMAT CONTRACT only | **92.9** | Yes |

### Excellence Signals from V-05

**1. STEP-numbered procedural structure converts specification into execution trace.**
The skill body uses STEP 1 through STEP 11 as explicit execution units rather than named sections. This creates a sequential run-protocol where each step is a discrete checkpoint — the model cannot skip forward without visibly violating the step sequence. Phase gates enforce section boundaries at four points, but numbered steps enforce ordering within each phase.

**2. ROLE-NAME LOCK block carries a preemptive forward-reference to all downstream CHECK locations.**
The LOCK block in STEP 3 contains: "CHECK: before writing any role name in the Diagram, Headcount Key Roles, Rhythm Table DRI/Owner, Charter Membership/Decides, or Inertia sub-sections — verify it is in this list." This forward-reference inside the lock creates a two-layer check: the lock is the authority, and the lock itself reminds the model where it will be enforced. Each subsequent CHECK can then reference "the ROLE-NAME LOCK list above" without restating the full list.

**3. VERDICT cross-references the four-field form output rather than duplicating it.**
"Re-assessment trigger from the four-field form applies here — do not repeat unless it differs" prevents Rebuttal–VERDICT divergence by making the VERDICT a consumer of the Rebuttal's structured output. This ties two sections together through an explicit cross-section reference, eliminating the failure mode where the VERDICT re-assessment trigger contradicts or weakens the Rebuttal trigger.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["STEP-numbered procedural structure converts skill body from declarative specification to sequential execution trace — each step is a discrete checkpoint that makes section skipping a visible protocol violation", "ROLE-NAME LOCK block carries a preemptive forward-reference enumerating all downstream CHECK locations — creates a two-layer check where the lock is the authority and the lock itself activates its own enforcement at every use site", "VERDICT cross-references four-field Rebuttal output rather than re-stating the trigger — explicit consumer-of-prior-output pattern prevents cross-section divergence between Rebuttal and VERDICT"]}
```
