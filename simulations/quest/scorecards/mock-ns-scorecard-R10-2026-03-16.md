## Round 10 Score — mock-ns (rubric v10)

---

### Rubric Reference (key criteria for R10)

| ID | Test | Type | pts |
|----|------|------|-----|
| C-25 | Two-sentence gate: (1) declarative role-assertion, (2) imperative instruction — numbered order implies sequence | aspirational | 2 |
| C-28 | Step as grammatical subject of its own emission action | aspirational | 2 |
| C-29 | Step as direct nominative head of subject NP | aspirational | 2 |
| C-30 | No artifact in nominative position in **active voice** | aspirational | 2 |
| C-31 | Indicative mood — no deontic modal (must/shall/should/is required to) | aspirational | 2 |
| C-32 | C-18 (handoff) and C-20 (terminal sentence) satisfied by independent sentences | aspirational | 2 |

Max = 128. All C-01–C-10 essential/recommended criteria are unaffected by gate declarative syntax; all pass in every variation.

---

### V-01: "The TOPICS.md status line is emitted first by this step."

**Axis:** Passive voice — artifact as grammatical subject, step as by-agent.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-25 | **FAIL** | Sentence is an output-position claim about the artifact, not a role-declaration asserting the step's primacy. The step appears only as oblique by-agent. An identity sentence about the step would require the step in subject position. |
| C-28 | **FAIL** | Grammatical subject is "TOPICS.md status line" (artifact). Step appears as "by this step" — passive agent, not grammatical subject. |
| C-29 | **FAIL** | Subject NP head is "status line." Step is not the direct nominative head. |
| C-30 | **PASS** | C-30 targets artifact promotion "in active voice." This sentence is passive. Strict reading: C-30 does not fire on passive constructions. The passive-voice qualifier creates a gap — artifact is in nominative position but C-30's qualifier is not satisfied. |
| C-31 | **PASS** | "is emitted" is indicative passive. No modal of obligation present. |
| C-32 | **PASS** | "Carry the resolved tier..." (C-18) and "Do not begin S-1..." (C-20) are present as independent sentences. Not collapsed into the opener. |
| All other | **PASS** | No other variations from golden baseline. |

**Score: 122/128** (C-25 -2, C-28 -2, C-29 -2)

**Key finding:** C-30's "in active voice" qualifier creates a passive-voice blind spot. The rubric catches artifact-as-subject in active voice (C-30) but relies entirely on C-28 and C-29 for the passive case. A rubric note is warranted: passive promotion of an artifact to nominative position escapes C-30 but fails C-28 and C-29 independently.

---

### V-02: "This step will emit first."

**Axis:** Predictive-future "will" — temporal assertion vs deontic obligation.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-25 | **PASS** | "This step will emit first" asserts the step's role as the emitter. Predictive future is a temporal declaration about what the step does — a role-assertion in declarative form. Not prescriptive. |
| C-28 | **PASS** | "This step" is grammatical subject; "will emit first" is the predicate. Step is the agent of the emission action. |
| C-29 | **PASS** | "This step" is the direct nominative head of the subject NP. |
| C-30 | **PASS** | No artifact in nominative position. |
| C-31 | **PASS** | "will" is absent from C-31's enumerated deontic list (must/shall/should/is required to). The sentence is predictive-future, asserting the step will perform an action — temporal, not normative. No deontic loading. |
| C-32 | **PASS** | C-18 and C-20 satisfied by independent sentences downstream. |
| All other | **PASS** | No other deviations from golden baseline. |

**Score: 128/128**

**Critical discriminator on C-31:** The C-31 substitution test (replace modal with simple present; check if transformation reveals deontic intent) does NOT discriminate "will" from "must" — both yield "This step emits first" on replacement. However, C-31's primary test is enumeration-first: if the modal is not in the list (must/shall/should/is required to), the deontic test does not apply. "Will" is not listed. The sentence passes. The substitution test is a secondary probe, not the primary gate.

---

### V-03: "Emitting first is this step's defining action."

**Axis:** Gerundive-nominative — action phrase as grammatical subject, step demoted to genitive modifier in predicate.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-25 | **PASS** | Content reading: the sentence IS a role-declaration — emitting first is identified as this step's defining action, asserting the step's structural role. C-25 does not test subject position explicitly; it tests whether the assertion is a role-declaration vs prescription. PASS on content. |
| C-28 | **FAIL** | Grammatical subject is "Emitting first" (gerundive). The step appears only as genitive modifier "this step's" in the predicate. The step is not the agent performing emission in subject position. |
| C-29 | **FAIL** | Subject NP head is "Emitting" (gerundive nominalization). "This step" has moved to the predicate as a possessive modifier. Not the direct nominative head. Substitution test: replace subject NP with "It" → "It is this step's defining action" — "It" refers to the action (emitting first), not to the step. FAIL. |
| C-30 | **PASS** | "Emitting first" is an action, not an output artifact. No artifact promotion. |
| C-31 | **PASS** | Copula "is" is indicative. No modal. |
| C-32 | **PASS** | C-18 and C-20 satisfied by independent sentences. |
| All other | **PASS** | No other deviations. |

**Score: 124/128** (C-28 -2, C-29 -2)

**Structural note:** This is a new gerundive-subject failure mode distinct from R8 V-02's possessive-nominal ("This step's defining action is to emit first"). In R8: the nominalization is subject, step is possessive modifier of subject. Here: the action is subject, step is possessive modifier within the predicate. Both demote the step, but through different syntactic paths. C-28 and C-29 catch both.

---

### V-04: "Write the TOPICS.md status line before any other work begins. S-0 is the emit step."

**Axis:** Reversed sentence order — imperative first, declarative second.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-25 | **FAIL** | C-25's structure is numbered: "(1) a declarative identity sentence... and (2) an imperative instruction." Numbered ordering is prescriptive. V-04 places the imperative as sentence 1 and the declarative as sentence 2 — reversed. Both required sentence types are present, but the ordering requirement is violated. FAIL on ordering grounds. |
| C-28 | **PASS** | The declarative sentence "S-0 is the emit step" has "S-0" as grammatical subject, identity predicate. PASS. |
| C-29 | **PASS** | "S-0" is the direct nominative head. PASS. |
| C-30 | **PASS** | No artifact in active nominative position. |
| C-31 | **PASS** | "is" copula, indicative. No modal. |
| C-32 | **PASS** | C-18 and C-20 satisfied by independent sentences downstream. |
| All other | **PASS** | No other deviations from golden baseline. |

**Score: 126/128** (C-25 -2)

**Key finding:** The declarative sentence itself ("S-0 is the emit step") is a perfect identity predicate — it would score 128/128 in the standard gate position. Only the ordering of sentences within the gate triggers C-25. This reveals that C-25 is order-strict: declarative must precede imperative. A rubric note is warranted confirming this.

---

### V-05: "It is this step that emits first."

**Axis:** Cleft extraposition — dummy expletive "It" as formal subject, step as focused NP in relative clause.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-25 | **PASS** | Cleft construction is an identity assertion: "the entity that emits first = this step." Role content is present and declarative. PASS on content. |
| C-28 | **FAIL** | In the main clause, "It" is the formal grammatical subject (dummy expletive). "This step" is the focused constituent in the extraposed NP. Even though "this step" is the logical agent of "emits first" in the relative clause, the main clause grammatical subject is "It." C-28 requires the step as grammatical subject at the sentence level. Strict syntactic reading: FAIL. |
| C-29 | **FAIL** | Subject NP of main clause is "It" (dummy expletive). C-29 substitution test: replace subject NP with "It" — it IS already "It." "It" refers forward to the proposition "this step that emits first," not directly to the step. The step is not the direct nominative head. FAIL. |
| C-30 | **PASS** | No artifact in nominative position. |
| C-31 | **PASS** | Copula "is" is indicative. No modal. |
| C-32 | **PASS** | C-18 and C-20 satisfied by independent sentences. |
| All other | **PASS** | No other deviations. |

**Score: 124/128** (C-28 -2, C-29 -2)

**Structural note:** The cleft focuses "this step" pragmatically (it's the communicative focus) but demotes it grammatically. C-28 and C-29 are syntactic-surface tests; they catch the cleft because the dummy expletive "It" holds the surface subject position. This is consistent with the rubric's history of applying grammatical (not logical) subject tests. A rubric note clarifying that C-28 is syntactic-surface (not semantic-logical) would close the ambiguity.

---

### Ranking

| Rank | Variation | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-02 "This step will emit first." | **128/128** | none |
| 2 | V-04 "Write... S-0 is the emit step." (reversed order) | **126/128** | C-25 |
| 3 (tie) | V-03 Gerundive-nominative | **124/128** | C-28, C-29 |
| 3 (tie) | V-05 Cleft extraposition | **124/128** | C-28, C-29 |
| 5 | V-01 Passive artifact-as-subject | **122/128** | C-25, C-28, C-29 |

---

### Excellence Signals (from V-02, 128/128)

**E-01 — Predictive future is outside C-31's deontic scope.** "Will" is a temporal-future modal asserting the step's behavior as a factual prediction. C-31 enumerates its failure list (must/shall/should/is required to); "will" is absent. The enumeration is the primary gate; the substitution test is secondary. A gate declarative using "will emit" passes C-31 and also passes C-25, C-28, C-29 — it has the same grammatical structure as "emits first" with an added temporal marker.

**E-02 — The C-31 substitution test is insufficient as a standalone discriminator.** Replacing "will" with simple present yields "This step emits first" (fact) — the same transformation as replacing "must." The substitution test cannot distinguish predictive future from deontic obligation. This reveals that C-31 requires the enumeration check first; the substitution test cannot be applied blindly to any modal.

**E-03 (from V-04) — C-25 ordering is strict, not type-only.** The declarative sentence "S-0 is the emit step" in V-04 is individually perfect (passes C-28, C-29, C-30, C-31). Only its position (sentence 2 instead of sentence 1) triggers C-25. This confirms C-25's numbered structure encodes a strict ordering requirement: declarative must be the opening sentence of the gate.

---

### Open Questions Resolved by R10

| Question | Resolution |
|----------|-----------|
| Does C-30's "in active voice" qualifier create a passive-voice gap? | **Yes.** Passive artifact-as-subject escapes C-30 but is independently caught by C-28 and C-29. C-30 is active-voice-specific; passive requires no C-30 note on the rubric, but reviewers should know C-28/C-29 are the passive failure detectors. |
| Is predictive "will" inside or outside C-31's deontic scope? | **Outside.** "Will" is temporal-predictive, absent from the deontic enumeration. 128/128 achievable with predictive future. Rubric note needed: distinguish "will" (predictive) from the deontic list. |
| Is C-25's numbering order-strict or type-only? | **Order-strict.** Reversed gate fails C-25 even with both sentence types present. A rubric note confirming this settles the open question from V-04. |
| Is C-28 syntactic-surface or semantic-logical? | **Syntactic-surface.** Cleft form fails C-28 because the dummy expletive "It" holds the main-clause subject position. A rubric note clarifying this closes the V-05 ambiguity. |

---

```json
{"top_score": 128, "all_essential_pass": true, "new_patterns": ["Predictive future 'will' is outside C-31's deontic scope -- 'will' is absent from the enumerated failure list (must/shall/should/is required to) and makes a temporal assertion, not a normative prescription; a gate declarative using 'will emit' passes C-31 and achieves 128/128", "The C-31 substitution test (modal to simple present) is insufficient as a standalone discriminator -- it yields the same result for predictive 'will' and deontic 'must'; C-31 requires the enumeration check first, substitution test second", "C-25 ordering is strict: declarative sentence must be sentence 1, imperative sentence 2; reversed order fails C-25 even when both required sentence types are present", "C-28 is a syntactic-surface test: dummy expletive 'It' in cleft constructions fails C-28 because the step is not the main-clause grammatical subject, even though it is the logical agent in the embedded relative clause"]}
```
