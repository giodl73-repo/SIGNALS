## Quest Score — corps-chart Round 7

### Rubric Domain-Type Note

C-01 checks for domain types `(strategic) / (operational) / (advisory) / (governance)`. All five R7 variations use `Engineering / PM / Design / Operations / Research / Other`. This is a vocabulary mismatch — C-01 **FAIL** across all variations.

---

## Per-Variation Scoring

### V-01 — MECHANISM-TYPE VOCABULARY (single axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION (strategic/operational/advisory/governance) | **FAIL** | Uses Engineering/PM/Operations/etc. — wrong closed vocabulary |
| C-02 | ASCII diagram, committees as distinct nodes | **PASS** | "draw ASCII hierarchy… committees as distinct labeled nodes — not embedded in one area" |
| C-03 | Headcount table — 5 columns, Decides/Escalates separate | **PASS** | Explicit `Area | Headcount | Key Roles | Decides | Escalates`; Key Roles annotated |
| C-04 | Operating rhythm — min 3 rows | **PASS** | ROB + shiproom + governance explicitly required |
| C-05 | Committee charters — all 5 fields, Quorum fraction | **PASS** | All 5 fields; `Quorum: [N] of [M] member roles` format stated |
| C-06 | Inertia assessment — FLAT-CASE-PRESSURE + verdict | **PASS** | All 4 sub-sections, pressure line, closed-set rating, declaration, concrete trigger |
| C-07 | ORG-ELEMENT REGISTER — 4 categories | **PASS** | All 4 cat-N categories present |
| C-08 | Section order — all 4 phase gates | **PASS** | All 4 gates in correct sequence |
| C-09 | Anti-Pattern Watch — typed cat-N citations | **PASS** | "Every 'Why It Applies Here' cell MUST open with [element name] (cat-N)" + "cat-N codes must match categories in ORG-ELEMENT REGISTER" |
| C-10 | Org Evolution — two distinct trigger categories | **PASS** | Row 1 headcount threshold; Row 2 "different category (workload signal, structural symptom, or milestone event)" |
| C-11 | Rebuttal role-grounded, concrete re-assessment trigger | **FAIL** | Rebuttal only says "reference a specific observable" — no requirement to name a role from ROLES-LOADED |
| C-12 | Role-name coherence full document | **PARTIAL** | Diagram enforced; DRI/Owner says "where possible" (not required); no lock |
| C-13 | ROLE-NAME LOCK block after classification | **FAIL** | Not present |
| C-14 | Four-field Rebuttal form | **FAIL** | Not present |
| C-15 | CAT-N-CITATION-SCHEMA block | **FAIL** | Not present |
| C-16 | TRIGGER-TYPE VOCABULARY block | **FAIL** | Not present |
| C-17 | 5th phase gate before Anti-Pattern Watch | **FAIL** | Not present |
| C-18 | VERIFY blocks for all high-risk PRODUCE commands | **FAIL** | Not present |
| C-19 | MECHANISM-TYPE VOCABULARY block | **PASS** | Full named block with 4 permitted types and "no row may use a Type value outside this list" |

**Score**: Essential 48 + Recommended 30 + Aspirational (C-09 + C-10 + C-12 partial + C-19 = 0.91×3 + 0.45) = **81.2**

---

### V-02 — VERIFY Blocks (single axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION vocabulary | **FAIL** | Engineering/PM vocabulary |
| C-02 | ASCII diagram | **PASS** | "Draw an ASCII hierarchy… committees as distinct labeled nodes. Role names must match ROLES-LOADED" |
| C-03 | Headcount table — 5 columns | **PASS** | 5 columns stated; VERIFY disqualifies merged Decision Scope column |
| C-04 | Operating rhythm — min 3 rows | **PASS** | ✓ |
| C-05 | Committee charters — 5 fields, Quorum fraction | **PASS** | Quorum VERIFY: short form "without denominator M does not satisfy" |
| C-06 | Inertia assessment | **PASS** | All 4 sub-sections, FLAT-CASE-PRESSURE, declaration, trigger |
| C-07 | ORG-ELEMENT REGISTER | **PASS** | All 4 categories |
| C-08 | 4 phase gates in order | **PASS** | ✓ |
| C-09 | Anti-Pattern Watch — typed cat-N | **PASS** | VERIFY block: "cell that names an org element without the (cat-N) typed citation prefix does not satisfy this criterion for that row" |
| C-10 | Org Evolution — distinct trigger categories | **PASS** | VERIFY: "Two rows that are both headcount threshold triggers do not satisfy this step" |
| C-11 | Rebuttal role-grounded | **FAIL** | No role-from-ROLES-LOADED requirement in Rebuttal |
| C-12 | Role-name coherence full document | **PARTIAL** | Diagram role check; DRI/Owner not enforced |
| C-13 | ROLE-NAME LOCK block | **FAIL** | Not present |
| C-14 | Four-field Rebuttal form | **FAIL** | Not present |
| C-15 | CAT-N-CITATION-SCHEMA block | **FAIL** | Not present |
| C-16 | TRIGGER-TYPE VOCABULARY block | **FAIL** | Inline type names in VERIFY but no named `TRIGGER-TYPE VOCABULARY` block before the table |
| C-17 | 5th phase gate | **FAIL** | Not present |
| C-18 | VERIFY blocks — all 3 required | **PASS** | Headcount (merged column) ✓ · Org Evolution (duplicate threshold) ✓ · Rebuttal (future-tense "As we scale…") ✓; also Quorum and Anti-Pattern bonus |
| C-19 | MECHANISM-TYPE VOCABULARY block | **FAIL** | Inline vocabulary mention only — no named `MECHANISM-TYPE VOCABULARY` block before mechanism table |

**Score**: Essential 48 + Recommended 30 + Aspirational (C-09 + C-10 + C-12 partial + C-18 = 0.91×3 + 0.45) = **81.2**

---

### V-03 — CAT-N-CITATION-SCHEMA + TRIGGER-TYPE VOCABULARY Pair

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION vocabulary | **FAIL** | Engineering/PM vocabulary |
| C-02 | ASCII diagram | **PASS** | ✓ |
| C-03 | Headcount table — 5 columns | **PASS** | "DO NOT merge Decides and Escalates into a single Decision Scope column" |
| C-04 | Operating rhythm | **PASS** | ✓ |
| C-05 | Committee charters | **PASS** | Quorum fraction format stated |
| C-06 | Inertia assessment | **PASS** | ✓ |
| C-07 | ORG-ELEMENT REGISTER | **PASS** | All 4 categories |
| C-08 | 4 phase gates in order | **PASS** | ✓ |
| C-09 | Anti-Pattern Watch — typed cat-N | **PASS** | CAT-N-CITATION-SCHEMA block present; "A cell that names an org element without (cat-N) prefix does not satisfy this schema" |
| C-10 | Org Evolution — distinct trigger categories | **PASS** | TRIGGER-TYPE VOCABULARY block; Row 1 headcount threshold, Row 2 different Type |
| C-11 | Rebuttal role-grounded | **FAIL** | "Reference a specific observable" but no role-from-ROLES-LOADED requirement |
| C-12 | Role-name coherence full document | **PARTIAL** | Diagram enforced; no ROLE-NAME LOCK for other sections |
| C-13 | ROLE-NAME LOCK block | **FAIL** | Not present |
| C-14 | Four-field Rebuttal form | **FAIL** | Not present |
| C-15 | CAT-N-CITATION-SCHEMA block | **PASS** | Full named block with valid cat-N enumeration and mandatory format statement before Anti-Pattern Watch table |
| C-16 | TRIGGER-TYPE VOCABULARY block | **PASS** | Full named block with 4 permitted Types and "No two consecutive rows may share the same Type value" before trigger table |
| C-17 | 5th phase gate | **FAIL** | Not present |
| C-18 | VERIFY blocks | **FAIL** | Not present |
| C-19 | MECHANISM-TYPE VOCABULARY block | **FAIL** | Inline only: "Type values from closed vocabulary: Channel / Informal Role / Recurring Cadence / Shared Artifact" — no named block |

**Score**: Essential 48 + Recommended 30 + Aspirational (C-09 + C-10 + C-12 partial + C-15 + C-16 = 0.91×4 + 0.45) = **83.1**

---

### V-04 — 5th Phase Gate + Vocabulary-Lock Trilogy

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION vocabulary | **FAIL** | Engineering/PM vocabulary |
| C-02 | ASCII diagram | **PASS** | ✓ |
| C-03 | Headcount table — 5 columns | **PASS** | "Produce: Area | Headcount | Key Roles | Decides | Escalates. Five columns required." |
| C-04 | Operating rhythm | **PASS** | ✓ |
| C-05 | Committee charters | **PASS** | Quorum fraction format stated |
| C-06 | Inertia assessment | **PASS** | All 4 sub-sections, FLAT-CASE-PRESSURE, closed-set rating, declaration, concrete trigger |
| C-07 | ORG-ELEMENT REGISTER | **PASS** | All 4 categories; "DO NOT proceed until all four are populated" |
| C-08 | 4 phase gates in order | **PASS** | All 4 original gates present (plus 5th) |
| C-09 | Anti-Pattern Watch — typed cat-N | **PASS** | CAT-N-CITATION-SCHEMA block present with full enumeration |
| C-10 | Org Evolution — distinct trigger categories | **PASS** | TRIGGER-TYPE VOCABULARY block; Row 1 headcount threshold, Row 2 different Type |
| C-11 | Rebuttal role-grounded | **FAIL** | No role-from-ROLES-LOADED requirement in Rebuttal sub-section |
| C-12 | Role-name coherence full document | **PARTIAL** | "Names from ROLES-LOADED" for diagram only; other sections not enforced via lock |
| C-13 | ROLE-NAME LOCK block | **FAIL** | Not present |
| C-14 | Four-field Rebuttal form | **FAIL** | Not present |
| C-15 | CAT-N-CITATION-SCHEMA block | **PASS** | Full named block before Anti-Pattern Watch ✓ |
| C-16 | TRIGGER-TYPE VOCABULARY block | **PASS** | Full named block before trigger table ✓ |
| C-17 | 5th phase gate before Anti-Pattern Watch | **PASS** | `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===` present with "DO NOT begin Anti-Pattern Watch until this gate line is present" |
| C-18 | VERIFY blocks | **FAIL** | Not present |
| C-19 | MECHANISM-TYPE VOCABULARY block | **PASS** | Full named block with 4 permitted Types before mechanism table ✓ |

**Score**: Essential 48 + Recommended 30 + Aspirational (C-09 + C-10 + C-12 partial + C-15 + C-16 + C-17 + C-19 = 0.91×6 + 0.45) = **83.9**

---

### V-05 — Full Integration

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION vocabulary | **FAIL** | Engineering/PM/Design/Operations/Research/Other — wrong vocabulary |
| C-02 | ASCII diagram | **PASS** | "Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes — not embedded in any area box. ROLE-NAME LOCK check: every role name in the diagram must appear in the ROLE-NAME LOCK list." |
| C-03 | Headcount table — 5 columns | **PASS** | UPFRONT FORMAT CONTRACT declares 5-column schema; VERIFY block disqualifies Decision Scope merge |
| C-04 | Operating rhythm | **PASS** | ✓ |
| C-05 | Committee charters | **PASS** | Charter schema in UPFRONT FORMAT CONTRACT includes Quorum fraction format; VERIFY: "short form … does NOT satisfy this schema" |
| C-06 | Inertia assessment | **PASS** | All 4 sub-sections; FLAT-CASE-PRESSURE; closed-set rating; declaration; re-assessment trigger via four-field form |
| C-07 | ORG-ELEMENT REGISTER | **PASS** | All 4 categories; "DO NOT proceed to Org Evolution Roadmap until all four are populated" |
| C-08 | 4 phase gates in order | **PASS** | All 4 original gates present (+ 5th) ✓ |
| C-09 | Anti-Pattern Watch — typed cat-N | **PASS** | CAT-N-CITATION-SCHEMA block + VERIFY for un-typed citation per row |
| C-10 | Org Evolution — distinct trigger categories | **PASS** | TRIGGER-TYPE VOCABULARY block + VERIFY: "Two rows that are both headcount threshold triggers do not satisfy this step" |
| C-11 | Rebuttal role-grounded, concrete re-assessment trigger | **PASS** | Four-field form: `ROLE UNDER PRESSURE: [name exactly one role from ROLE-NAME LOCK]` + `OBSERVABLE BREAKDOWN: [current failure — not future growth risk]` + `RE-ASSESSMENT TRIGGER: [concrete measurable threshold]`; VERIFY: future-tense fails |
| C-12 | Role-name coherence full document | **PASS** | ROLE-NAME LOCK with inline CHECK at diagram, Rhythm Table DRI/Owner, Charter Membership/Decides, Inertia sub-sections (ROLE UNDER PRESSURE bound to lock) |
| C-13 | ROLE-NAME LOCK block after classification | **PASS** | Full named block immediately after ROLE-TYPE-CLASSIFICATION; "complete set of permitted references for this document"; appears before first phase gate |
| C-14 | Four-field Rebuttal form | **PASS** | All 4 field labels in order: `ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER`; VERIFY disqualifies future-tense OBSERVABLE BREAKDOWN |
| C-15 | CAT-N-CITATION-SCHEMA block | **PASS** | Full named block before Anti-Pattern Watch; enumerates valid codes; mandatory prefix format stated; disqualification rule stated |
| C-16 | TRIGGER-TYPE VOCABULARY block | **PASS** | Full named block before trigger table; 4 permitted Types; "No two consecutive rows may share the same Type value" |
| C-17 | 5th phase gate before Anti-Pattern Watch | **PASS** | `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`; "DO NOT begin Anti-Pattern Watch until this gate line is present" |
| C-18 | VERIFY blocks — all required | **PASS** | Headcount (merged column) ✓ · Org Evolution (duplicate threshold) ✓ · Rebuttal (future-tense) ✓ · Charter Quorum (short form) ✓ · Anti-Pattern (un-typed citation) ✓ |
| C-19 | MECHANISM-TYPE VOCABULARY block | **PASS** | Full named block before mechanism table; 4 permitted Types; "No row may use a Type value outside this list" |

**Score**: Essential 48 + Recommended 30 + Aspirational (11 × 0.91 = 10.01 → capped at 10) = **88.0**

---

## Rankings

| Rank | Variation | Score | Aspirational passes |
|------|-----------|-------|---------------------|
| 1 | **V-05** Full Integration | **88.0** | 11/11 |
| 2 | **V-04** 5th Gate + Vocab Trilogy | **83.9** | 6.5/11 (6 + 1 partial) |
| 3 | **V-03** CAT-N + TRIGGER-TYPE Pair | **83.1** | 4.5/11 (4 + 1 partial) |
| 4 | **V-01** MECHANISM-TYPE VOCABULARY | **81.2** | 3.5/11 (3 + 1 partial) |
| 4 | **V-02** VERIFY Blocks | **81.2** | 3.5/11 (3 + 1 partial) |

All variations: `all_essential_pass = false` (C-01 fails due to vocabulary mismatch across all).

---

## Excellence Signals from V-05

**Pattern 1 — Upfront TABLE SCHEMAS block as forward-declared contract**
All five table schemas are consolidated in one block before the first STEP. This eliminates the failure mode where the model produces the correct *structure* while misremembering a column name because the schema was prose-embedded 1,500 tokens earlier. The schema becomes a lookup reference, not a recall requirement.

**Pattern 2 — ROLE-NAME LOCK as document-spanning active contract, not one-time enumeration**
Unlike a list that the model reads and forgets, V-05's ROLE-NAME LOCK includes inline `CHECK:` reminders at every downstream section (diagram, rhythm table DRI/Owner, charter Membership/Decides, Inertia sub-sections). This converts role-coherence from a "read it at the top, hope it holds" discipline into a per-section mechanical check.

**Pattern 3 — Vocabulary lock + VERIFY block as complementary, non-redundant pair**
Vocabulary locks prevent wrong-type values (e.g., "Tool" in the mechanism table). VERIFY blocks prevent right-type-but-wrong-structure evasions (e.g., a valid "headcount threshold" row 1 paired with another "headcount threshold" row 2, or a structurally correct charter where Quorum omits the denominator M). The two mechanisms target different failure modes and stack without redundancy.

**Pattern 4 — Four-field Rebuttal form makes role-grounding a syntactic precondition**
By placing `ROLE UNDER PRESSURE` as the first field with a VERIFY block on `OBSERVABLE BREAKDOWN`, V-05 makes it impossible to write the breakdown prose without first naming the role. The form structure eliminates the compliance gap that exists when role-grounding is requested only via prose instruction ("name a specific role").

**Pattern 5 — 5th phase gate converts optional section into structurally required section**
A missing Anti-Pattern Watch section without a gate is a silent skip — the output looks complete. A missing gate after the Org Evolution Roadmap is a visible structural violation. The gate shifts the failure from "section absent" (hard to catch in a long document) to "gate absent" (syntactically absent at the sequence level).

---

```json
{"top_score": 88, "all_essential_pass": false, "new_patterns": ["Upfront TABLE SCHEMAS block pre-declares all five table column schemas before any section begins, converting schema recall into schema lookup", "ROLE-NAME LOCK with inline CHECK reminders at each downstream section converts role-coherence from one-time read to per-section mechanical check", "Vocabulary lock + VERIFY block pairing covers complementary failure modes: wrong-type values vs. right-type-but-wrong-structure evasions", "Four-field Rebuttal form makes role-grounding a syntactic precondition — ROLE UNDER PRESSURE must be named before OBSERVABLE BREAKDOWN prose can begin", "5th structural phase gate converts Anti-Pattern Watch from a silently-skippable section into a structurally visible required section"]}
```
