## Round 14 Scoring — mock-ns (rubric v14, max 142)

---

### Evaluation Framework

All five variations share identical structure (P-0, S-2, S-3, A-1–A-5). The only difference is the first sentence of S-1. Criteria C-01 through C-24, C-27, and C-32 are constant across all variations and pass per the R13 V-03 baseline (138/142 failing C-25+C-28 only). Differential scoring applies exclusively to the declarative-failure-mode criteria C-25, C-28–C-39.

---

### V-01 — Passive + agent-PP

**Sentence:** `The TOPICS.md status line is emitted by this step before any other step begins.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Shared structure |
| C-09–C-24 | PASS | Shared structure, per R13 baseline |
| C-25 | PASS | Declarative sentence; identifies step function via passive + agent-PP. Not an imperative, not an ordering gate. Passive form with explicit agent is distinct from possessor-NP failure (R12 V-03). |
| C-26 | PASS | "TOPICS.md status line" names the step output; per R13 baseline, this satisfies C-26. |
| C-27–C-28 | PASS | C-28 discriminator note: "Passivization passes: 'The TOPICS.md status line is emitted by this step.' Agent position satisfies the C-28 requirement for step agency." |
| C-29 | PASS | No possessive-nominal subject form |
| C-30 | PASS | Passive, not active-voice artifact-as-subject |
| C-31 | PASS | No modal-obligation |
| C-32 | PASS | Shared structure |
| **C-33** | **FAIL** | Passive artifact-as-subject form. C-33 pass condition: "no sentence describes emission using passive artifact-as-subject form." The artifact IS the main-clause subject. C-33 clarification confirms: "'The TOPICS.md status line is emitted by this step' (artifact = subject, step = agent) is still prohibited." |
| C-34 | PASS | No gerundive-as-subject |
| C-35 | PASS | Step is in a by-PP, not a relative clause. C-35 requires "step as grammatical agent in a subordinate (relative or other) clause" — by-PP is not a clause. Hypothesis misidentified C-35; correct criterion is C-33. |
| C-36–C-39 | PASS | No ordering predicate, possessive-NP, it-cleft, or wh-pseudo-cleft |

**Composite: 142 − 2 = 140/142**
Hypothesis: 140/142 ✓ (correct score; wrong criterion — C-33 not C-35)

---

### V-02 — Existential-there negation

**Sentence:** `There is no step that precedes this step's TOPICS.md status line emission.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-24 | PASS | Shared structure |
| **C-25** | **FAIL** | "There" is expletive with no referential content; "no step" is the nominal; step appears only as possessor in "this step's TOPICS.md status line emission." Not a declarative identity sentence for the step — a negative existential about ordering. C-25 requires a sentence that identifies "what the step is or does" from the step's perspective. |
| **C-28** | **FAIL** | Step is not the grammatical nominative subject. Appears as genitive possessor in the object phrase "this step's TOPICS.md status line emission." Neither the expletive "There" nor the nominal "no step" is the step itself in subject position. |
| C-29 | PASS | Possessive "this step's TOPICS.md status line emission" appears in object/relative-clause position, not as the main-clause subject NP. C-29 prohibits possessive-nominal **subject** form; the possessive here is in object position. |
| C-38 | PASS | Not an it-cleft. C-38 requires "It is [X] that [emits]..." form. V-02 is existential-there negation — structurally distinct. |
| C-39 | PASS | No wh-nominalization subject |
| C-30–C-37 | PASS | No matching failure forms |

**Composite: 142 − 4 = 138/142**
Hypothesis: 140/142 ✗ (two criteria fail, not one; no new C-40 needed)

---

### V-03 — Focus-particle fronting

**Sentence:** `Only this step emits the TOPICS.md status line before other steps act.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-24 | PASS | Shared structure |
| C-25 | PASS | Declarative sentence. "Only" is a focus-particle adverb scoped over the subject NP; it does not displace "this step" from nominative subject position. Step is the explicit grammatical subject. Identifies step's emission function. |
| C-26 | PASS | "TOPICS.md status line" names the step output |
| C-28 | PASS | Step as nominative subject; "emits" as main predicate in main clause |
| C-29–C-31 | PASS | No possessive-nominal, no artifact-as-subject, no modal-obligation |
| C-33–C-39 | PASS | No gerundive, no relative-clause agent, no ordering predicate, no possessive-NP abstraction, no it-cleft, no wh-pseudo-cleft |

**Composite: 142/142**
Hypothesis: 142/142 ✓

---

### V-04 — Modal-obligation

**Sentence:** `This step must emit the TOPICS.md status line before any other step may proceed.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-24 | PASS | Shared structure |
| C-25 | PASS | Declarative sentence; step is nominative subject; identifies emission function. Not imperative. Not an ordering-predicate sentence. |
| C-26 | PASS | "TOPICS.md status line" names the step output |
| C-28 | PASS | Step as nominative subject; "must emit" (modal + main verb) as predicate. Modal does not invalidate subject-predicate structure for C-28. |
| C-29–C-30 | PASS | No possessive-nominal, no artifact-as-subject |
| **C-31** | **FAIL** | "Must" is a modal-obligation form. C-31 pass condition: "no must, shall, should, or is required to in S-0 role declaration." The sentence IS the role-declaration sentence (satisfies C-25). C-31 therefore applies and fires. C-31 note: "A single word (must/shall/should) can trigger only C-31 if C-25/C-28 are otherwise satisfied" — exactly this case. |
| C-33–C-39 | PASS | No passive artifact-subject, no gerundive, no relative-clause agent, no ordering predicate, no possessive-NP, no it-cleft, no wh-pseudo-cleft |

**Composite: 142 − 2 = 140/142**
Hypothesis: 142/142 ✗ (C-31 fires; hypothesis missed modal-obligation trap)

---

### V-05 — Temporal-clause fronting (confirmed baseline)

**Sentence:** `Before any other step begins, this step emits the TOPICS.md status line.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-24 | PASS | Shared structure |
| C-25 | PASS | Declarative. "Before any other step begins" is fronted adverbial; main clause "this step emits the TOPICS.md status line" has step as subject, "emits" as predicate. |
| C-26 | PASS | "TOPICS.md status line" names step output |
| C-28 | PASS | Step as nominative subject in main clause; "emits" as main predicate |
| C-29–C-31 | PASS | No possessive-nominal, no artifact-as-subject, no modal |
| C-33–C-39 | PASS | None of the declarative failure forms present |
| **C-38** | PASS | No expletive it-cleft — confirmed |
| **C-39** | PASS | No wh-pseudo-cleft — confirmed |

**Composite: 142/142**
Hypothesis: 142/142 ✓

---

### Composite Scores

| Rank | Variation | Constraint sentence | Criteria failing | Score |
|------|-----------|---------------------|-----------------|-------|
| 1 | V-03 | "Only this step emits the TOPICS.md status line before other steps act." | none | **142/142** |
| 1 | V-05 | "Before any other step begins, this step emits the TOPICS.md status line." | none | **142/142** |
| 3 | V-01 | "The TOPICS.md status line is emitted by this step before any other step begins." | C-33 | **140/142** |
| 3 | V-04 | "This step must emit the TOPICS.md status line before any other step may proceed." | C-31 | **140/142** |
| 5 | V-02 | "There is no step that precedes this step's TOPICS.md status line emission." | C-25, C-28 | **138/142** |

---

### Excellence Signals (from V-03 and V-05)

**V-03 — Focus-particle fronting:**
"Only this step emits..." demonstrates that focus-particle adverbs scoped over the subject NP do not displace the subject's grammatical function. "This step" remains the explicit nominative subject; "emits" remains the main predicate. Focus particles are a confirmed safe positive form. This expands the positive set: temporal fronting (V-05) and focus-particle fronting (V-03) are both safe. The structural guarantee is that neither modifies the main clause subject-predicate relationship.

**V-05 — Temporal-clause fronting:**
Reconfirmed at 142/142 under v14. The two new criteria (C-38, C-39) do not fire. This is the primary positive anchor for R15.

---

### Hypothesis Accuracy Review

| Variation | Predicted | Actual | Result |
|-----------|-----------|--------|--------|
| V-01 | 140/142 (C-35) | 140/142 (C-33) | Score ✓ / Criterion ✗ |
| V-02 | 140/142 (C-38 ext or C-40) | 138/142 (C-25, C-28) | Score ✗ / Criterion ✗ |
| V-03 | 142/142 | 142/142 | ✓ |
| V-04 | 142/142 | 140/142 (C-31) | ✗ |
| V-05 | 142/142 | 142/142 | ✓ |

**V-04 is the critical correction:** modal "must" fires C-31 independently even when C-25 and C-28 pass. The hypothesis assumed modal-obligation in a declarative structure would be safe. It is not — C-31 is a standalone criterion targeting the wrong discourse register, not dependent on structural failure of C-25/C-28.

**V-01 correction:** C-35 requires step as agent in a relative clause ("TOPICS.md is the first artifact **this step emits**"). In V-01, step appears in a by-PP ("by this step"), which is not a clause. C-35 does not fire. C-33 fires: passive artifact-as-subject in S-0 emission description. These are structurally distinct failure modes.

**V-02 correction:** Existential-there negation is covered by C-25+C-28 without requiring a new criterion. C-38 extension or C-40 is not needed. The existential "there" fails C-25 (not a declarative identity sentence) and C-28 (step not nominative subject) — same failure chain as other confounded forms.

---

```json
{"top_score": 142, "all_essential_pass": true, "new_patterns": ["C-31 fires in isolation when modal 'must' is used even with C-25 and C-28 passing (V-04) — modal-obligation in declarative structure is a standalone single-criterion failure, not dependent on structural displacement", "Existential-there negation ('There is no step that precedes...') maps to C-25+C-28 failure chain without triggering new criterion; C-38 extension not needed for existential-there class", "Passive with agent-PP fires C-33 not C-35 — by-PP is not a subordinate clause; C-35 requires relative-clause agent; C-33 is the correct passive-artifact-subject criterion"]}
```
