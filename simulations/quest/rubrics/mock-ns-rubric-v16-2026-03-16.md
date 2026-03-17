`simulations/quest/rubrics/mock-ns-rubric-v16-2026-03-17.md` written.

---

## v16 summary

**Two new criteria, max 146 → 150 (35 aspirational × 2 = 70).**

### C-42 — C-28 step-scope displacement (R15 V-01)
> "Only this step emits the TOPICS.md status line" — grammatically correct form, in S-1 not S-0.

C-28 requires the emission sentence within S-0 or its gates. When S-0 is absent (collapsed into S-1), no emission sentence can satisfy C-28 regardless of grammatical correctness. The sentence is in the wrong step scope. C-42 names this as the twelfth declarative-placement failure mode: grammatical form is necessary but not sufficient — step scope is independently required. The two criteria co-fire when a correctly-formed emission sentence appears outside S-0.

**Failure chain: C-28, C-42 → varies** (in V-01, C-28 already fails from S-0 absence; C-42 adds named displacement)

### C-43 — C-32 lifecycle-annotation closing-position displacement (R15 V-02)
> V-02 boundary: supplementation (annotation follows terminal sentence) → C-32 passes; replacement (annotation eliminates terminal sentence) → C-32 fails, C-43 fires.

Lifecycle exit-state blocks interact with C-32 in two ways. Supplementation: annotation follows the terminal sentence; C-32 passes (sentence is still present as discrete prose). Replacement: annotation takes the structural position of the terminal sentence, eliminating it; C-32 fails and C-43 fires. Evaluators must check for the sentence as a discrete prose item, not merely whether it is the absolute final token.

**Failure chain: C-32, C-43 → 148/150**

### Discriminator notes updated

| Criterion | New note |
|-----------|---------|
| C-28 | R15: Step-scope boundary confirmed — grammatical form + correct step scope both required. Emission sentence in S-1 (S-0 absent) fails C-28, fires C-42. R15 V-01 canonical. |
| C-32 | R15: Lifecycle annotation interaction. Supplementation (annotation follows sentence) → pass. Replacement (annotation eliminates sentence) → fail + C-43 fires. R15 V-02 boundary. |

### R15 under v16

| Variation | Fails | Score |
|-----------|-------|-------|
| V-01 decision table (no S-0) | C-12, C-13, C-15–C-28/C-32 (S-0 dependent), C-42 | 118/150 |
| V-02 lifecycle annotations (supplementation) | — | 150/150 |
| V-02 lifecycle annotations (replacement) | C-32, C-43 | 148/150 |
