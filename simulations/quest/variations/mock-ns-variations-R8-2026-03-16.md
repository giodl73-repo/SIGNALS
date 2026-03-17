Written to `simulations/quest/golden/mock-ns-variate-R8-2026-03-16.md`.

---

## Round 8 -- 5 Variations (rubric v8, targeting C-27 + C-28)

**Variation axes selected:**

| Variate | Axis | C-27 | C-28 | Predicted |
|---------|------|------|------|-----------|
| V-01 | Passive-voice declarative | PASS | FAIL | 118/120 |
| V-02 | Possessive-nominal subject | PASS | FAIL | 118/120 |
| V-03 | Post-imperative enforcement sentence | FAIL | PASS | 118/120 |
| V-04 | Compound-predicate declarative | PASS | PASS | 120/120 |
| V-05 | Convergent: symmetric gate-verb pair | PASS | PASS | 120/120 |

---

**V-01 (Passive-Voice Declarative):** `"The TOPICS.md status line is the first output of this step."` -- artifact in nominative position via passive construction; step is oblique modifier. Distinct from R7 V-04's sequence-position form ("first observable output") -- here the passive makes the artifact the agent of emission. C-28 FAIL, C-27 PASS.

**V-02 (Possessive-Nominal Subject):** `"This step's defining action is to emit first."` -- head noun is "defining action" (nominalization of the step's role); "this step" is demoted to genitive modifier. New C-28 failure mode not previously tested: nominal-derivation vs artifact-primacy vs output-sequence.

**V-03 (Post-Imperative Enforcement Sentence):** `"This step emits first. Write the TOPICS.md status line before any other work begins. No other step may begin before this emission completes."` -- third sentence added after the imperative as enforcement rationale (not elaboration between the pair, as in R7 V-03). Confirms C-27 is content-agnostic and position-agnostic: count = 3 fails regardless of where the third sentence sits.

**V-04 (Compound-Predicate Declarative):** `"This step emits first and resolves the tier variable."` -- step as nominative subject retained; compound predicate merges emit primacy with tier resolution. New territory: either an acceptable dense form (120/120) or the seed of a new C-29 restriction (declarative should be single-predicate, emit-only).

**V-05 (Convergent -- Symmetric Gate-Verb Pair):** `"This step emits first. Write the TOPICS.md status line before any other step begins."` + terminal `"Do not begin S-1 until the TOPICS.md status line is written."` -- imperative changes "work" → "step" (pipeline-unit framing); preamble and terminal now share "begin" as action verb. Candidate C-29: preamble imperative and terminal gate share action verb, making the enforcement pair auditable by vocabulary alone.
