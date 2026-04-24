## mock-ns Round 11 Scoring (rubric v11, max 132)

---

### Scoring Framework

| Weight | Criteria | Each | Max |
|--------|----------|------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-34 | 2 | 52 |
| **Total** | | | **132** |

---

### Essential Criteria — All Variations

All five variations share identical structure from P-0 through A-5. Essential criteria are common.

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 (6-field header) | **PASS** | A-1 assembles skill, topic, category, date, status, flag — all 6 present |
| C-02 (CATEGORY correct) | **PASS** | mock-ns is HIGH-STRUCTURE; S-2 assigns correctly from canonical registry |
| C-03 (FLAG correct) | **PASS** | S-3 computes from CATEGORY + tier with all 4 cases + compliance override |
| C-04 (fidelity warning) | **PASS** | A-2 emits category-matched HIGH-STRUCTURE warning block |
| C-05 (skill-specific body) | **PASS** | A-3 generates mock body; namespace/skill identifiable from structure alone |

**Essential total: 50/50 — all_essential_pass: true**

---

### Recommended Criteria — All Variations

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-06 (setup emit lines) | **PASS** | S-0 emits TOPICS.md status line; S-1 emits generating line; S-0 precedes S-1 |
| C-07 (write confirmation) | **PASS** | A-4 writes to `simulations/mock/{topic}-{namespace}-mock-{date}.md` |
| C-08 (next-step line) | **PASS** | A-5 emits `Next: /mock:review {topic} ...` as final line |

**Recommended total: 30/30**

---

### Aspirational Criteria — Common Scoring

These criteria are identical across all variations (no gate declarative dependence).

| C | Status | Note |
|---|--------|------|
| C-09 | PASS | S-1 table: topic-plan default, topic-status EXCLUDED |
| C-10 | PASS | Default pass — no compliance tags scenario; override rule present |
| C-11 | PASS | S-3 covers all 5 flag cases functionally; cases 1+2 may collapse per C-11 |
| C-12 | PASS | S-0 is a discrete labeled step; tier resolved before S-1 begins |
| C-13 | PASS | S-2 assignment structure produces undefined CATEGORY on unrecognized skill-id; spec-implied halt |
| C-14 | PASS | 10 labeled steps (S-0, P-0, S-1–S-3, A-1–A-5); A-1 through A-5 are the 5 assembly steps |
| C-15 | PASS | S-0 prohibits advancement: "Do not begin S-1 until the TOPICS.md status line is written" + carry constraint |
| C-16 | PASS | `trace-*`, `scout-feasibility`, `listen-*` appear directly in S-3 Case 1 match expression |
| C-17 | PASS | "Do not begin S-1 until the TOPICS.md status line is written" — names S-1, names the precondition |
| C-18 | PASS | "Carry the resolved tier value into S-1" — S-1 is the pipeline entry; S-2 and S-3 consume implicitly via resolved variable |
| C-19 | PASS | Preamble gate (sentences 1–2 at S-0 opening) + terminal gate ("Do not begin S-1…") — both present |
| C-20 | PASS | Carry sentence in S-0 terminal position naming downstream consumer; FLAG immutability chain table in S-3 encodes tier dependence |
| C-21 | PASS | S-0 advancement prohibition covers: tier resolution, skill lookup, category assignment, mock generation — 4 operations named |
| C-22 | PASS | S-3 Case 1 and Case 2 are distinct cases; HS critical tier≥2 and HS other are structurally separated |
| C-23 | PASS | Gate declarative (sentence 1) is the absolute first content of S-0 in all variations |
| C-24 | PASS | S-0 prohibition chain closes all production phases including artifact output (S-0 ends before A-4) |
| C-26 | PASS | Case-expression vocabulary in S-3 uses distinct terminology per condition row |
| C-27 | PASS | All variations have exactly two sentences in the preamble gate; additional S-0 content is separated and non-gate |
| C-31 | PASS | All gate declaratives use indicative or copular mood; no deontic modal present |
| C-32 | PASS | Tier-carry in S-0 terminal position (C-18) and FLAG immutability table in S-3 (C-20) are structurally independent |
| C-33 | PASS all | No passive constructions in any gate declarative; confirmed below per variation |

**Common aspirational total: 21 criteria × 2 = 42 pts**

---

### Gate Declarative Analysis — Per Variation

Each variation differs only in sentence 1 of the S-0 two-sentence gate. Criteria C-25, C-28, C-29, C-30, C-33, C-34 are gate-sensitive.

---

#### V-01 — "TOPICS.md is the first artifact this step emits."

Active-voice artifact nominative. Tests C-30 vs C-33 non-overlapping scope.

| C | Result | Evidence |
|---|--------|---------|
| C-25 | **FAIL** | Sentence asserts a property of the artifact (being first), not the step's role. Step appears only as agent inside the embedded relative clause "this step emits" — not as main-clause subject. Not a role-declaration. |
| C-27 | PASS | Exactly two sentences in gate pair |
| C-28 | **FAIL** | "TOPICS.md" is grammatical subject. Step is embedded agent in relative clause. Step does not assert its own functional role. |
| C-29 | **FAIL** | Substitution: "It is the first artifact this step emits" — "It" refers to TOPICS.md, not to the step. Step is not nominative head. |
| C-30 | **FAIL** | Artifact "TOPICS.md" is in active nominative subject position. |
| C-31 | PASS | "emits" in embedded clause is indicative; no deontic modal in main clause |
| C-33 | **PASS** | Active-voice construction, not passive. C-33 targets passive constructions only. **Key finding: C-30 and C-33 are non-overlapping detectors.** |
| C-34 | PASS | No gerundive subject; "TOPICS.md" is a noun, not an action-nominalization. |

**Gate failures: C-25, C-28, C-29, C-30 (−8 pts)**
**Score: 132 − 8 = 124/132**

---

#### V-02 — "What S-0 emits first is the TOPICS.md status line."

Wh-cleft with step as embedded agent. Tests C-28/C-29 syntactic threshold + C-34 boundary.

| C | Result | Evidence |
|---|--------|---------|
| C-25 | PASS | Content reading: wh-cleft asserts what S-0's first output is, identifying S-0 as the first emitter. Role-assertion in cleft form. C-25 is content-based (confirmed R9 V-01). |
| C-27 | PASS | Exactly two sentences |
| C-28 | **FAIL** | Main-clause grammatical subject is "What S-0 emits first" (nominalized free relative). S-0 is logical agent inside the relative clause but not main-clause grammatical subject. C-28 is a syntactic-surface test. |
| C-29 | **FAIL** | Substitution: "It is the TOPICS.md status line" — "It" refers to the action-content (the thing first emitted), not to S-0 directly. The wh-word is the nominative head, not S-0. |
| C-30 | PASS | "TOPICS.md status line" is the predicate nominal (post-copular), not the nominative subject. |
| C-31 | PASS | Indicative "emits" in embedded clause; no deontic modal |
| C-33 | PASS | Active-voice wh-cleft, not passive |
| C-34 | **PASS** | "What S-0 emits first" is a wh-nominalized free relative, not a gerundive ("-ing") construction. Critically: S-0 appears inside the subject as embedded agent, NOT as predicate-possessive modifier. C-34's trigger is predicate-possessive displacement of the step ("this step's X"). In V-02, the step is displaced to embedded-agent inside the subject clause — a structurally distinct displacement. C-34 does not fire. |

**Gate failures: C-28, C-29 (−4 pts)**
**Score: 132 − 4 = 128/132**

---

#### V-03 — "To emit the TOPICS.md status line first is this step's role."

Infinitival subject. Tests C-34 scope: gerundive-specific vs action-nominalization-general.

| C | Result | Evidence |
|---|--------|---------|
| C-25 | PASS | Content: explicitly declares the step's role. Role-assertion in infinitival form. |
| C-27 | PASS | Exactly two sentences |
| C-28 | **FAIL** | "To emit the TOPICS.md status line first" (infinitive clause) is the grammatical subject. The step appears only as "this step's" — a genitive modifier in the predicate. Step is not the grammatical subject asserting its own emission. |
| C-29 | **FAIL** | Substitution: "It is this step's role" — "It" refers to the infinitival action (emitting), not to the step. Step is predicate-possessive. |
| C-30 | PASS | "TOPICS.md status line" is inside the infinitive as direct object of "emit" — not the main-clause nominative subject. |
| C-31 | PASS | Copula "is" in indicative; infinitive is non-finite (no deontic modal) |
| C-33 | PASS | Not a passive construction |
| C-34 | **FAIL** | The pass condition for C-34 is: "gerundive phrase OR action-nominalization derived from the step's behavior as grammatical subject, with the step appearing only as predicate-possessive modifier." Both conditions are fully met: (1) "To emit first" is an infinitival action-nominalization derived from the step's behavior; (2) the step appears as predicate-possessive "this step's role." The determining condition is the predicate-possessive displacement, not the gerundive morpheme. C-34 fires. Resolves the C-34 scope question: the criterion covers infinitival action-nominalizations when the step is predicate-possessive — not just gerundive "-ing" forms. |

**Gate failures: C-28, C-29, C-34 (−6 pts)**
**Score: 132 − 6 = 126/132**

---

#### V-04 — "The emit step, S-0, runs before all other steps produce any output."

Appositional step identifier. Tests C-29 identifier-strict vs referential.

| C | Result | Evidence |
|---|--------|---------|
| C-25 | PASS | Declarative with step-referent subject; temporal ordering role-assertion. |
| C-27 | PASS | Exactly two sentences |
| C-28 | PASS | Subject NP "The emit step, S-0" refers to the step; the subject performs the ordering action "runs before all other steps." The step (via the NP) is agent of its own pipeline role. |
| C-29 | **FAIL** | C-29 requires "the step itself as the direct nominative HEAD of the subject noun phrase." The NP head is "step" (common noun), not "S-0" (the step identifier). "S-0" occupies appositive position within the NP — it is a renaming constituent, not the head. Substitution test confirms referential identity ("It" refers to the step), but C-29 is a HEAD-position test, not a referential test. Rubric history favors the strict reading: each criterion closes a specific structural gap; the appositive construction is a new gap the appositive identifier does not close. |
| C-30 | PASS | No artifact in nominative subject position |
| C-31 | PASS | "runs" is indicative |
| C-33 | PASS | Not passive |
| C-34 | PASS | No gerundive or infinitival action-nominalization as subject; "The emit step" is a common noun |

**Gate failures: C-29 (−2 pts)**
**Score: 132 − 2 = 130/132**

---

#### V-05 — "S-0 emits the TOPICS.md status line before any other output."

Transitive-object form. Predicted canonical positive.

| C | Result | Evidence |
|---|--------|---------|
| C-25 | PASS | "S-0" is the subject; sentence asserts S-0's role as first emitter. Declarative. |
| C-27 | PASS | Exactly two sentences |
| C-28 | PASS | "S-0" is the direct grammatical subject performing the emission action "emits." Step as agent of its own role, in indicative form. |
| C-29 | PASS | Substitution: "It emits the TOPICS.md status line before any other output" — "It" refers directly to S-0. S-0 is the direct nominative head of the subject NP. No appositive, no genitive, no abstraction. |
| C-30 | PASS | "TOPICS.md status line" is the direct object (post-verbal accusative), not the nominative subject. Active-voice artifact promotion criterion does not fire. |
| C-31 | PASS | "emits" is simple present indicative |
| C-33 | PASS | Active transitive construction; artifact is in object position. Not passive. Passive artifact-as-subject criterion does not fire. Both C-30 and C-33 satisfied by placing artifact in object position. |
| C-34 | PASS | "S-0" is the grammatical subject — a step identifier, not an action-nominalization. No gerundive, no infinitival clause in subject position. |

**Gate failures: none**
**Score: 132/132**

---

### Composite Scores and Ranking

| Rank | Var | Gate Declarative | Score | Gate Failures |
|------|-----|-----------------|-------|---------------|
| 1 | **V-05** | "S-0 emits the TOPICS.md status line before any other output." | **132/132** | none |
| 2 | **V-04** | "The emit step, S-0, runs before all other steps produce any output." | **130/132** | C-29 |
| 3 | **V-02** | "What S-0 emits first is the TOPICS.md status line." | **128/132** | C-28, C-29 |
| 4 | **V-03** | "To emit the TOPICS.md status line first is this step's role." | **126/132** | C-28, C-29, C-34 |
| 5 | **V-01** | "TOPICS.md is the first artifact this step emits." | **124/132** | C-25, C-28, C-29, C-30 |

---

### Excellence Signals — V-05

**Step identifier as direct nominative NP head.** "S-0" occupies the subject position as the head of the NP with no intermediary (no common-noun head, no appositive structure, no possessive, no wh-clause). This simultaneously satisfies C-25 (role-declaration), C-28 (step as grammatical subject of its own emission), and C-29 (step as direct nominative head).

**Artifact as transitive direct object.** Placing the artifact name after a transitive emission verb ("emits the TOPICS.md status line") removes it from all subject-position tests: C-30 (no active-voice nominative artifact) and C-33 (no passive-voice nominative artifact) are both satisfied in a single structural choice.

**Single construction resolves five criteria.** V-05's subject-verb-object structure satisfies C-28, C-29, C-30, C-33, and C-34 simultaneously — not by avoiding the artifact, but by giving it the grammatically correct role (direct object, not subject). This is the canonical form for gates that name the artifact explicitly.

**Temporal adjunct encodes ordering without subject displacement.** "before any other output" expresses the step's first-mover role as an adjunct, not by making "first output" the subject. The ordering claim stays in the predicate; the step stays in the subject.

---

### Open Questions Resolved by R11

| Question | Resolution | Method |
|----------|-----------|--------|
| Is C-33 passive-only? | **CONFIRMED passive-only.** V-01's active-voice artifact nominative triggers C-30, not C-33. The two criteria cover non-overlapping voice constructions of the same failure mode. | V-01: C-30 FAIL, C-33 PASS |
| Does C-34 cover wh-nominalization? | **CONFIRMED gerundive-specific for wh-cleft.** Step-as-embedded-agent inside a wh-subject does not displace the step to predicate-possessive; C-34 does not fire. | V-02: C-34 PASS |
| Does C-34 cover infinitival subjects? | **CONFIRMED: C-34 fires.** Trigger is predicate-possessive demotion of the step, not gerundive morphology. Infinitival subject + "this step's role" in predicate satisfies both C-34 conditions. | V-03: C-34 FAIL (126/132) |
| Is C-29 identifier-strict? | **CONFIRMED identifier-strict.** Common-noun NP head "step" with S-0 as appositive fails C-29; the identifier must occupy the direct NP head position. | V-04: C-29 FAIL (130/132) |
| Transitive-object form canonical? | **CONFIRMED 132/132.** Subject = step identifier, verb = transitive emission verb, object = artifact. Canonical safe gate pattern. | V-05 |

---

### New Patterns for v12 Rubric

**Pattern 1: C-34 predicate-possessive trigger confirmed.** C-34 fires for any action-nominalization (gerundive OR infinitival) as grammatical subject when the step is displaced to predicate-possessive modifier ("this step's X"). C-34 does NOT fire when the step appears as embedded agent inside the subject clause (wh-cleft form) — the predicate-possessive displacement is the discriminating condition, not the nominalization morpheme. Rubric update needed: C-34 description should add infinitival form as a named example, and add a discriminator note clarifying that wh-cleft displacement (step as embedded agent) escapes C-34.

**Pattern 2: Transitive-object is the canonical artifact-naming gate form.** "S-0 emits [artifact] before any other output" satisfies C-28, C-29, C-30, C-33, and C-34 in a single structural choice. No prior round had named this constructive positive explicitly. Candidate for a design rule note in the rubric.

**Pattern 3: C-29 appositive failure confirmed.** "The emit step, S-0" — common-noun NP head with identifier as appositive — fails C-29 because the identifier does not occupy the direct NP head position. Rubric update: add C-29 discriminator note stating appositional identifiers do not satisfy the direct-nominative-head requirement; only when the step identifier is the NP head (e.g., "S-0 emits..." or "This step emits...") does C-29 pass.

---

```json
{"top_score": 132, "all_essential_pass": true, "new_patterns": ["C-34 predicate-possessive trigger: fires for infinitival action-nominalization subjects when step is predicate-possessive ('this step's role'); does not fire for wh-cleft subjects where step is embedded agent inside the subject clause — predicate-possessive displacement is the discriminating condition, not gerundive morphology", "transitive-object canonical form: step-identifier as subject + transitive emission verb + artifact as direct object satisfies C-28, C-29, C-30, C-33, C-34 simultaneously — canonical safe gate pattern for gates naming the artifact explicitly", "C-29 appositive failure confirmed: common-noun NP head with step identifier as appositive ('The emit step, S-0') fails C-29 — identifier must occupy the direct NP head position, not an appositive slot"]}
```
