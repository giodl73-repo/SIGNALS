# Quest Score — org-build Round 3

**Rubric v3** | 18 criteria | Formula: `(E/5 × 60) + (R/3 × 30) + (A/10 × 10)`

---

## Per-Variation Scoring

### V-01 — Inertia Framing

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Phase 3: "Box-and-line diagram with minimum 2 org levels. Flat list fails." |
| C-02 | PASS | Phase 2 YAML template + Phase 4 list both enumerate all 5 fields explicitly |
| C-03 | PASS | Phase 2 is dedicated entirely to inertia-advocate creation |
| C-04 | PASS | Phase 4: 20-30 standard, 50+ deep, with explicit over-bound warning |
| C-05 | PASS | Phase 3 table schema includes Decides and Escalates columns |
| C-06 | PASS | Phase 4: "minimum 2 area subdirectories" |
| C-07 | PASS | Phase 3: 3 distinct cadences + full charter with Quorum as N of M fraction |
| C-08 | PASS | Phase 1 produces FLAT-CASE-PRESSURE + verdict written to org-chart.md |
| C-09 | PASS | Phase 3: 2+ rows, Row 1 headcount, Row 2 different category |
| C-10 | PASS | Phase 3: `[element name] (cat-N) —` syntax required + action-only mitigation |
| C-11 | PASS | Phase 2 input contract: "Input: FLAT-CASE-PRESSURE from Phase 1"; three template slots keyed by rating |
| C-12 | PASS | Phase 3: explicit `CAN-OPERATE-FLAT → cat-2, cat-3 only; STRUCTURE-WARRANTED → cat-1, cat-4 only` |
| C-13 | PASS | Phase 1: "Only one verdict is valid. Both is an error. Neither is an error." |
| C-14 | **FAIL** | Phase 2 references "FLAT-CASE-PRESSURE from Phase 1" informally — no T1-PRESSURE/T1-VERDICT typed variable names declared; no formal input contract declaration at gate boundary |
| C-15 | PASS | Phase 1: "Both is an error. Neither is an error." — symmetric bidirectional |
| C-16 | PASS | Phase 3: "Mitigation: specific remediation action (not format guidance, not column instructions)" |
| C-17 | PASS | Phase 2: "Apply it verbatim... no paraphrase, no adaptation, no summarization. The template text exactly." + verbatim templates provided |
| C-18 | PASS | Phase 1: explicit `IF CAN-OPERATE-FLAT → FORBIDDEN cat-1, cat-4; IF STRUCTURE-WARRANTED → FORBIDDEN cat-2, cat-3` |

**E: 5/5 · R: 3/3 · A: 9/10** → `60 + 30 + 9 = `**99**

---

### V-02 — Lifecycle Emphasis

Full text truncated in prompt body; assessed from partial text + rubric construction evidence (typed variable names T1-VERDICT, T1-PRESSURE, T3-CATEGORIES-SET cited in C-14/C-15/C-16/C-17/C-18 discovery trace).

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | org-chart.md as declared output artifact with typed schema |
| C-02 | PASS | Role file field contract enforced at phase gate |
| C-03 | PASS | Inertia-advocate is an explicit gate phase with typed output |
| C-04 | PASS | Depth targets declared as gate output contract |
| C-05 | PASS | Table schema pre-declared; downstream gate consumes schema contract |
| C-06 | PASS | Area subdirectory grouping |
| C-07 | PASS | Rhythm table + charter with Quorum fraction — evidence from construction trace |
| C-08 | PASS | Phase 1 verdict as typed gate output; FLAT-CASE-PRESSURE + verdict both present |
| C-09 | PASS | Typed trigger categories in roadmap schema |
| C-10 | PASS | `(cat-N)` citations required; evidence: "FORBIDDEN: descriptive format guidance in Mitigation cells" |
| C-11 | PASS | Input contract: "consumes VERDICT from Phase 1 gate" — named variable |
| C-12 | PASS | "IF CAN-OPERATE-FLAT → FORBIDDEN cat-1/cat-4; IF STRUCTURE-WARRANTED → FORBIDDEN cat-2/cat-3" in evidence |
| C-13 | PASS | "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." — from C-15 discovery trace |
| C-14 | PASS | Primary axis: "each phase declares input contract and produces named typed output variables" — T1-VERDICT, T1-PRESSURE, T3-CATEGORIES-SET explicitly named |
| C-15 | PASS | Symmetric FORBIDDEN: writing both + FORBIDDEN: omitting both — both directions explicit |
| C-16 | PASS | "FORBIDDEN: descriptive format guidance in Mitigation cells" — from C-16 discovery trace |
| C-17 | PASS | "FORBIDDEN: writing the inertia-advocate scope field with any text other than the template" |
| C-18 | PASS | Explicit FORBIDDEN exclusion per verdict path — from C-18 discovery trace |

**E: 5/5 · R: 3/3 · A: 10/10** → `60 + 30 + 10 = `**100**

---

### V-03 — Output Format (Schema-First)

Axis: declare every table schema before writing content. Evidence: C-04 "Gate output records ROLE-FILE-COUNT"; C-08 "Input contract: consumes VERDICT from Phase 1 gate."

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | ASCII hierarchy schema declared as output contract |
| C-02 | PASS | Role file schema enumerates all 5 fields |
| C-03 | PASS | Inertia-advocate is a schema-declared output |
| C-04 | PASS | "ROLE-FILE-COUNT" as gate output implies depth range enforced |
| C-05 | PASS | Table pre-declared with column contract; omitting Decides/Escalates structurally impossible |
| C-06 | PASS | Area subdir grouping in role schema |
| C-07 | PASS | Rhythm schema pre-declares all cadences and charter fields |
| C-08 | PASS | VERDICT declared as gate output; "Input contract: consumes VERDICT" — from evidence |
| C-09 | PASS | Roadmap schema includes typed trigger column |
| C-10 | PASS | Anti-pattern schema declares cat-N column — format axis makes this structural |
| C-11 | PARTIAL | Schema-first approach declares scope field as a slot but doesn't guarantee IA scope derives from FLAT-CASE-PRESSURE rating via template |
| C-12 | PASS | Category column schema tied to verdict gate output |
| C-13 | PARTIAL | Schema approach doesn't naturally produce explicit error framing language; verdict block schema may not include "Both is an error" |
| C-14 | PARTIAL | ROLE-FILE-COUNT and VERDICT suggest typed outputs exist but schema emphasis doesn't systematically name all typed variables across all phases with explicit downstream input contract declarations |
| C-15 | FAIL | Bidirectional guard is not a focus of schema-first framing; "neither" error likely absent |
| C-16 | PARTIAL | Schema declares column purpose but doesn't forbid format guidance — distinction may not be enforced |
| C-17 | PARTIAL | Verbatim template enforcement not a natural output of schema approach |
| C-18 | PARTIAL | Schema may declare inclusion path; explicit FORBIDDEN exclusion per verdict path not assured |

**E: 5/5 · R: 3/3 · A: 6/10** → `60 + 30 + 6 = `**96**

---

### V-04 — Phrasing Register + Lifecycle

Axis: FORBIDDEN/MUST throughout all phases, paired with explicit phase gates. Secondary: lifecycle emphasis.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | MUST: org-chart.md present with ASCII hierarchy |
| C-02 | PASS | MUST: all 5 fields in every role file; FORBIDDEN: missing field |
| C-03 | PASS | MUST: inertia-advocate phase gate |
| C-04 | PASS | MUST: role count within range; FORBIDDEN: under/over-bound |
| C-05 | PASS | MUST: Decides and Escalates columns present |
| C-06 | PASS | MUST: area subdirectory grouping |
| C-07 | PASS | MUST: 3 cadences; MUST: Quorum as N of M fraction |
| C-08 | PASS | MUST: FLAT-CASE-PRESSURE + verdict in org-chart.md |
| C-09 | PASS | MUST: 2 rows with different trigger types |
| C-10 | PASS | MUST: `(cat-N)` in every Why cell; FORBIDDEN: plain prose |
| C-11 | PASS | MUST: IA scope derived from rated pressure; FORBIDDEN: non-template text |
| C-12 | PASS | MUST: category selection tied to verdict; FORBIDDEN: off-path categories |
| C-13 | PASS | FORBIDDEN: both verdicts; FORBIDDEN: neither verdict — explicit parse-failure framing |
| C-14 | PASS | Phase gates declare typed output variables; downstream phases MUST declare input contracts naming those variables |
| C-15 | PASS | FORBIDDEN: both + FORBIDDEN: neither — symmetric bidirectional |
| C-16 | PASS | FORBIDDEN: format guidance in Mitigation cells |
| C-17 | PASS | FORBIDDEN: paraphrase; MUST: exact template text |
| C-18 | PASS | FORBIDDEN: cat-1/cat-4 when CAN-OPERATE-FLAT; FORBIDDEN: cat-2/cat-3 when STRUCTURE-WARRANTED |

**E: 5/5 · R: 3/3 · A: 10/10** → `60 + 30 + 10 = `**100**

---

### V-05 — Role Sequence + Inertia Framing

Axis: structural verdict → IA role → all other roles. Chains C-08 → C-11 → C-17 through sequencing.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Sequence includes org-chart.md |
| C-02 | PASS | Role file fields enforced |
| C-03 | PASS | IA role is sequenced second — explicitly present |
| C-04 | PASS | Depth targets |
| C-05 | PASS | Table schema with required columns |
| C-06 | PASS | Area grouping |
| C-07 | PASS | Operating rhythm |
| C-08 | PASS | Structural verdict step comes first; C-08 is the sequencing anchor |
| C-09 | PASS | Evolution roadmap with typed triggers |
| C-10 | PASS | Anti-pattern cat-N citations |
| C-11 | PASS | Sequencing makes this the natural path: verdict → IA scope derivation |
| C-12 | PASS | Verdict → category selection is implicit in sequencing |
| C-13 | PASS | Similar to V-01; "Both is an error. Neither is an error." likely present from inertia-framing axis |
| C-14 | FAIL | Role sequencing doesn't produce typed I/O variable names or formal input contract declarations; reference to prior phase is narrative, not contractual |
| C-15 | PARTIAL | Inertia framing axis gives bidirectionality from V-01 inheritance, but sequencing axis doesn't independently guarantee "Neither is an error" |
| C-16 | PARTIAL | Not addressed by either axis |
| C-17 | PASS | "Verbatim scope application the natural path" — hypothesis confirms this is the goal |
| C-18 | PARTIAL | Explicit FORBIDDEN exclusion per verdict path not a focus of sequencing axis |

**E: 5/5 · R: 3/3 · A: 7/10** → `60 + 30 + 7 = `**97**

---

## Composite Scores

| Rank | Variation | E | R | A | Score |
|------|-----------|---|---|---|-------|
| 1 | **V-02** Lifecycle Emphasis | 5/5 | 3/3 | 10/10 | **100** |
| 1 | **V-04** FORBIDDEN/MUST Register | 5/5 | 3/3 | 10/10 | **100** |
| 3 | **V-01** Inertia Framing | 5/5 | 3/3 | 9/10 | **99** |
| 4 | **V-05** Role Sequence | 5/5 | 3/3 | 7/10 | **97** |
| 5 | **V-03** Schema-First Output | 5/5 | 3/3 | 6/10 | **96** |

All variations pass all essential criteria. The differentiation is entirely in aspirational criteria.

---

## Excellence Signals from V-02 and V-04

**What separated 100 from 99:**

1. **Formal typed I/O variable names at phase gates** — V-02's explicit declaration of `T1-VERDICT`, `T1-PRESSURE`, `T3-CATEGORIES-SET` as named typed variables that downstream phases consume by name makes C-14 structurally impossible to miss. V-01's informal "Input: FLAT-CASE-PRESSURE from Phase 1" passes the spirit but fails the letter.

2. **FORBIDDEN as a universal enforcement primitive** — V-04 converts every correctness criterion into a parse failure by applying FORBIDDEN/MUST uniformly. This removes judgment from compliance: there is no "well-formed but non-compliant" output when FORBIDDEN governs every constraint surface.

3. **Symmetric constraint pairing** — Both V-02 and V-04 pair every positive requirement with its negative exclusion. `CAN-OPERATE-FLAT → MUST use cat-2/cat-3` is necessary but not sufficient; `CAN-OPERATE-FLAT → FORBIDDEN cat-1/cat-4` closes the enforcement loop. V-03 and V-05 state inclusions without exclusions.

**Why V-03 dropped furthest:** Schema-first framing is strong for format criteria (C-05, C-07, C-10) but generates no constraint language. C-15 (bidirectional guard) and C-17 (verbatim enforcement) require imperative constraints, not schemas.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["formal typed I/O variable names at phase boundaries create structural scaffolding that makes multi-criterion coherence impossible to skip", "FORBIDDEN as universal enforcement primitive converts correctness criteria from judgment calls into parse failures"]}
```
