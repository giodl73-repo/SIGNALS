Written to `simulations/quest/golden/mock-ns-variate-R10-2026-03-16.md`.

---

## Round 10 Variations -- mock-ns (rubric v10)

Five single-axis variations, all targeting unexplored declarative failure modes beyond what R9 confirmed.

| Variation | Gate Declarative | Axis | Predicted Failures | Score |
|-----------|-----------------|------|-------------------|-------|
| **V-01** | `The TOPICS.md status line is emitted first by this step.` | Passive voice | C-25?, C-28, C-29 (C-30 may PASS -- passive not active) | 122-124/128 |
| **V-02** | `This step will emit first.` | Predictive future "will" | None OR C-25+C-28+C-31 | **122 or 128/128** |
| **V-03** | `Emitting first is this step's defining action.` | Gerundive-nominative | C-28, C-29 | 122-124/128 |
| **V-04** | `Write the TOPICS.md status line before any other work begins. S-0 is the emit step.` | Reversed sentence order | C-25 (ordering) | 126/128 |
| **V-05** | `It is this step that emits first.` | Cleft extraposition | C-29, C-28? | 124-126/128 |

**Key open questions this round resolves:**

1. **V-01** -- Does C-30's "in active voice" qualifier create a passive-voice gap? Passive artifact-as-subject escapes C-30 but fails C-28/C-29 -- tests whether the rubric needs a passive-voice note on C-30.

2. **V-02** -- Is predictive "will" inside or outside C-31's deontic scope? "Will" is absent from C-31's list (must/shall/should/is required to), but the substitution test doesn't discriminate between "will" and "must." Genuinely uncertain outcome.

3. **V-03** -- Gerundive-nominative as a new C-29 failure mode (distinct from R8's possessive-nominal). Tests whether C-25 passes on role-assertion content when the step is syntactically absent from subject position.

4. **V-04** -- Tests whether C-25's `(1)...(2)...` numbering enforces ordering or is type-only. A passing score here means reversed-order gates are valid -- rubric needs a note either way.

5. **V-05** -- Cleft extraposition: "It" is the surface subject, "this step" is the focused constituent. Tests whether C-28's "grammatical subject" is syntactic-surface or semantic-logical.
