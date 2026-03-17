Now I have all the data I need. Let me score all 5 variations against rubric v8.

---

## mock-ns Round 8 -- Scorecard (rubric v8, max 120)

### Preamble Gate Text Per Variation

| Variate | S-0 Opening Sentence(s) | Count |
|---------|------------------------|-------|
| V-01 | "The TOPICS.md status line is the first output of this step. Write this line before any other operation begins." | 2 |
| V-02 | "This step's defining action is to emit first. Write the TOPICS.md status line before any other work begins." | 2 |
| V-03 | "This step emits first. Write the TOPICS.md status line before any other work begins. No other step may begin before this emission completes." | 3 |
| V-04 | "This step emits first and resolves the tier variable. Write the TOPICS.md status line before any other work begins." | 2 |
| V-05 | "This step emits first. Write the TOPICS.md status line before any other step begins." + terminal "Do not begin S-1 until the TOPICS.md status line above is written." | 2 |

---

### Shared Structure (C-01 -- C-26)

All 5 variations are structurally identical outside of the S-0 preamble gate. Criteria C-01 through C-26 evaluate shared components (A-1 header template, A-2 fidelity warning, A-3 body instruction, S-1 through S-3 step logic, CONSTRAINT block, tier-carry contract). Since R7 V-05 with the same shared structure scored 120/120 on all 26 prior criteria, all 5 R8 variations inherit that result.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-01 | Header 6 required fields | PASS | PASS | PASS | PASS | PASS | A-1: Skill, Topic, Category, Date, Status, Flag all present |
| C-02 | CATEGORY correctly assigned | PASS | PASS | PASS | PASS | PASS | S-2 registry identical across all |
| C-03 | FLAG correctly computed | PASS | PASS | PASS | PASS | PASS | S-3 5-row table with compliance override |
| C-04 | Fidelity warning present and matched | PASS | PASS | PASS | PASS | PASS | A-2 category-matched warning blocks all present |
| C-05 | Body is skill-specific | PASS | PASS | PASS | PASS | PASS | A-3 instructs skill-specific headings, tables, gate/verdict line |
| C-06 | S-1 emit lines: TOPICS.md + generating | PASS | PASS | PASS | PASS | PASS | TOPICS.md line in S-0, generating line in S-1, both specified |
| C-07 | Artifact written to correct path | PASS | PASS | PASS | PASS | PASS | A-4: namespace (not skill-id) in path |
| C-08 | Next-step line is final line | PASS | PASS | PASS | PASS | PASS | A-5 terminal emit instruction present |
| C-09 | Default topic-plan not topic-status | PASS | PASS | PASS | PASS | PASS | "topic-status EXCLUDED -- meta-structural, never default" in S-1 table |
| C-10 | Compliance override applied | PASS | PASS | PASS | PASS | PASS | Default pass -- no compliance tags in template inputs |
| C-11 | FLAG covers all 5 cases, critical namespaces named | PASS | PASS | PASS | PASS | PASS | 5-row table with trace-*, scout-feasibility, listen-* enumerated |
| C-12 | S-0 resolves tier before S-1 begins | PASS | PASS | PASS | PASS | PASS | S-0 and S-1 are separate labeled steps; tier emitted before skill selection |
| C-13 | Unrecognized skill-id halts with error | PASS | PASS | PASS | PASS | PASS | "emit error naming the skill-id and direct user to registry" in S-2 |
| C-14 | Assembly as 5 discrete named steps | PASS | PASS | PASS | PASS | PASS | A-1 through A-5 labeled, each single responsibility |
| C-15 | CONSTRAINT names 3+ op types | PASS | PASS | PASS | PASS | PASS | 5 op types named |
| C-16 | Wildcard patterns in FLAG table condition cell | PASS | PASS | PASS | PASS | PASS | "critical (trace-*, scout-feasibility, listen-*)" in condition column |
| C-17 | S-0 gate names S-1, prohibits early advancement | PASS | PASS | PASS | PASS | PASS | "Do not begin S-1 until the TOPICS.md status line above is emitted/written" |
| C-18 | Tier-carry handoff names S-2 and S-3 | PASS | PASS | PASS | PASS | PASS | "Carry the resolved tier into S-2 and S-3 before any further action" |
| C-19 | S-0 has both preamble gate and terminal gate | PASS | PASS | PASS | PASS | PASS | All 5 have preamble opening + terminal "Do not begin S-1" sentence |
| C-20 | Tier-carry in table column AND standalone sentence | PASS | PASS | PASS | PASS | PASS | Table "Carry into S-2 (category) and S-3 (flag)" + standalone sentence |
| C-21 | CONSTRAINT names 4+ op types including body generation | PASS | PASS | PASS | PASS | PASS | 5 types including "No artifact body construction or section assembly" |
| C-22 | FLAG table separates HS-critical tier=1 as distinct row | PASS | PASS | PASS | PASS | PASS | Dedicated row for critical tier=1 (flag: none) separate from non-critical |
| C-23 | Preamble gate is opening sentence of S-0 | PASS | PASS | PASS | PASS | PASS | Preamble comes before resolution bullets and CONSTRAINT block in all 5 |
| C-24 | CONSTRAINT names 5+ op types including artifact path | PASS | PASS | PASS | PASS | PASS | "No artifact path assembly or file output" present |
| C-25 | Two-sentence gate: declarative identity + imperative | PASS | PASS | PASS | PASS | PASS | Both sentence types present in correct order; type-coverage reading |
| C-26 | CONSTRAINT uses synonym vocabulary | PASS | PASS | PASS | PASS | PASS | Rubric explicitly endorses "No mock content generation" as synonym for "No mock generation" |

All 5 variations pass C-01 through C-26. Discriminators are C-27 and C-28 only.

---

### C-27 Evaluation: Count-Strict Two-Sentence Gate

**C-27 pass condition:** Exactly two sentences in the preamble gate -- no additional sentence of any type.

| Variate | Gate Text | Count | C-27 |
|---------|-----------|-------|------|
| V-01 | "The TOPICS.md status line is the first output of this step. Write this line before any other operation begins." | 2 | **PASS** |
| V-02 | "This step's defining action is to emit first. Write the TOPICS.md status line before any other work begins." | 2 | **PASS** |
| V-03 | "This step emits first. Write the TOPICS.md status line before any other work begins. No other step may begin before this emission completes." | **3** | **FAIL** -- enforcement sentence added after imperative; count-strict regardless of sentence content or position |
| V-04 | "This step emits first and resolves the tier variable. Write the TOPICS.md status line before any other work begins." | 2 | **PASS** |
| V-05 | "This step emits first. Write the TOPICS.md status line before any other step begins." | 2 | **PASS** |

**V-03 failure analysis:** The third sentence ("No other step may begin before this emission completes.") is functionally enforcement rationale -- it names the prohibited action and restates the gate. It is NOT expository elaboration like R7 V-03's "Its single obligation before advancing is to report TOPICS.md status." The hypothesis was testing whether C-27 is content-agnostic, and it is: enforcement value does not exempt a sentence from the count. Three sentences in the gate = FAIL regardless of sentence purpose. C-27 is confirmed content-agnostic.

---

### C-28 Evaluation: Step-Role Declarative (Grammatical Subject)

**C-28 pass condition:** Step as grammatical subject asserting its pipeline role -- not an artifact, abstraction, or output-position assertion.

| Variate | Declarative Sentence | Subject | C-28 |
|---------|---------------------|---------|------|
| V-01 | "The TOPICS.md status line is the first output of this step." | "The TOPICS.md status line" -- output artifact in nominative position; step appears only as oblique modifier "of this step" | **FAIL** -- passive construction promotes artifact to subject; distinct from R7 V-04's sequence-position form ("first observable output") but same C-28 failure mode |
| V-02 | "This step's defining action is to emit first." | "defining action" -- nominalization; "This step" is in genitive/possessive modifier position | **FAIL** -- head noun of subject phrase is an abstraction derived from the step; step is demoted to possessive modifier; a new C-28 failure mode not previously tested |
| V-03 | "This step emits first." | "This step" -- the pipeline step in nominative position | **PASS** -- minimal single-predicate form; step as agent of its own role |
| V-04 | "This step emits first and resolves the tier variable." | "This step" -- nominative, compound predicate | **PASS** -- step remains grammatical subject; compound predicate adds tier-resolve obligation but does not displace step from subject position |
| V-05 | "This step emits first." | "This step" -- nominative | **PASS** -- identical to R7 V-05 declarative form |

**V-01 failure analysis:** The passive construction ("is the first output of this step") elevates the artifact to grammatical subject. This is a new C-28 failure mode -- distinct from R7 V-04's active-voice output-sequence form ("The first observable output of this step is...") because here the artifact is nominative subject via passive construction rather than via output-position predicate. Both fail C-28 for the same underlying reason: the step is not the agent of its own identity assertion.

**V-02 failure analysis:** The possessive-nominal form ("This step's defining action is to emit first") demotes "step" to genitive modifier. The nominative subject is "defining action" -- a nominalization of the step's own role. This is a third distinct C-28 failure mode: neither artifact-subject (V-01) nor output-sequence-subject (R7 V-04) -- but subject-as-role-abstraction. The intent is correct (role-asserting language) but the syntactic structure fails.

**V-04 pass analysis:** "This step emits first and resolves the tier variable." The step is nominative subject; the compound predicate merges emit primacy with tier resolution. C-28 is satisfied because the step remains the agent. The compound predicate creates a new data point: multiple pipeline obligations can be merged into the declarative without displacing the step from subject position.

---

### Composite Scores

| ID | C-01--C-26 | C-27 | C-28 | Aspirational Failures | Score |
|----|-----------|------|------|----------------------|-------|
| V-01 | PASS (26/26) | PASS | **FAIL** | 1 × −2 | **118/120** |
| V-02 | PASS (26/26) | PASS | **FAIL** | 1 × −2 | **118/120** |
| V-03 | PASS (26/26) | **FAIL** | PASS | 1 × −2 | **118/120** |
| V-04 | PASS (26/26) | PASS | PASS | 0 | **120/120** |
| V-05 | PASS (26/26) | PASS | PASS | 0 | **120/120** |

---

### Ranking

| Rank | Variate | Score | Failure |
|------|---------|-------|---------|
| 1 (tie) | V-04 -- Compound-Predicate Declarative | 120/120 | none |
| 1 (tie) | V-05 -- Convergent: Symmetric Gate-Verb Pair | 120/120 | none |
| 3 (tie) | V-01 -- Passive-Voice Declarative | 118/120 | C-28 |
| 3 (tie) | V-02 -- Possessive-Nominal Subject | 118/120 | C-28 |
| 3 (tie) | V-03 -- Post-Imperative Enforcement Sentence | 118/120 | C-27 |

Predictions confirmed exactly. All 5 match the predicted C-27/C-28 outcomes from the golden file.

---

### Prediction Accuracy

| Variate | Predicted | Actual | Match |
|---------|-----------|--------|-------|
| V-01 | 118/120 (C-28 FAIL) | 118/120 (C-28 FAIL) | ✓ |
| V-02 | 118/120 (C-28 FAIL) | 118/120 (C-28 FAIL) | ✓ |
| V-03 | 118/120 (C-27 FAIL) | 118/120 (C-27 FAIL) | ✓ |
| V-04 | 120/120 | 120/120 | ✓ |
| V-05 | 120/120 | 120/120 | ✓ |

5/5 predictions correct.

---

### Excellence Signals (from V-04 and V-05)

**From V-04 -- Compound-predicate declarative is an acceptable dense form:**
The declarative "This step emits first and resolves the tier variable" passes both C-27 (2 sentences) and C-28 (step as subject). A compound predicate that bundles emit primacy with a second pipeline obligation does not dilute the identity assertion and does not displace the step from subject position. This establishes a new boundary: compound predicates are acceptable when the step remains nominative agent. A candidate C-29 emerges: single-predicate vs compound-predicate restriction (the current rubric does not penalize multi-obligation declaratives; if it should, V-04 is the canonical failing example).

**From V-05 -- Symmetric gate-verb pair creates auditable enforcement:**
Changing the preamble imperative from "before any other work begins" (R7 V-05) to "before any other step begins" (R8 V-05) aligns the scope unit with the pipeline model ("step" vs the undefined unit "work"). This creates a vocabulary mirror: preamble imperative ("before any other step begins") and terminal gate ("Do not begin S-1") both use "begin" as the enforcement action verb. An auditor can verify the enforcement pair by scanning for a single vocabulary item. A candidate C-29 emerges: preamble imperative and terminal gate share the action verb, making the enforcement pair auditable by vocabulary alignment alone.

**New C-28 failure taxonomy (from V-01 and V-02):**
R8 adds two new failure modes to the C-28 failure catalog:
- **Passive-voice artifact-subject** (V-01): artifact elevated to nominative position via passive construction; step demoted to oblique modifier
- **Possessive-nominal abstraction** (V-02): step demoted to genitive modifier; head noun is a role-abstraction derived from the step

This gives three confirmed C-28 failure modes: output-sequence declarative (R7 V-04), passive-voice artifact-subject (R8 V-01), possessive-nominal abstraction (R8 V-02). All fail for the same structural reason: the step is not the grammatical agent of its own role assertion.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Compound-predicate declarative with step as subject is an acceptable dense form -- step remains nominative agent even when multiple pipeline obligations are merged into the predicate; candidate C-29 restriction on single-predicate-only form", "Preamble imperative using 'step' as scope unit (not 'work') and sharing the action verb 'begin' with the terminal gate creates a symmetric enforcement pair auditable by vocabulary alignment alone; candidate C-29 excellence criterion"]}
```
