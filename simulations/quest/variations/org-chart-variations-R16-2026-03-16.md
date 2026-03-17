Written to `simulations/quest/golden/org-chart-variate-R16-2026-03-17.md`.

---

## org-chart Variate -- Round 16

**Rubric:** v16 (C-45 new: CHECKPOINT-0 item (b) inline artifact enumeration)
**Baseline:** R15 V-01 passes C-45 (indented sub-list). R15 V-02 fails (pointer form).

**Three variation axes:**

| Axis | What it tests |
|------|--------------|
| **A** -- inline format shape | Numbered 1-4 list vs. compact single-line semicolons vs. baseline indented |
| **B** -- anti-pointer prohibition | Explicit named ban on "as listed above" form |
| **C** -- self-containment directive | Item (b) must be verifiable without cross-referencing any prior block |

---

### V-01 -- Axis A, form 2 (numbered sub-list)
Item (b) enumerates the four transitions as `1.` through `4.` entries. Ordinal gaps make incompleteness structurally visible -- a model that drops transition 3 breaks the 1-2-4 sequence.

### V-02 -- Axis A, form 3 (compact single-line)
All four transitions packed into a single semicolon-separated parenthetical on one line inside the checkbox body. Tests whether maximum compression still preserves inline enumeration, and whether the model drops artifact names or gate boundaries first when abbreviating.

### V-03 -- Axis B, form 2 (anti-pointer prohibition)
Same A-form-1 structure as R15 V-01, but adds an explicit prohibition inline: *"DO NOT write item (b) in pointer-reference form (e.g., 'as listed above' or 'as enumerated in the inventory block')"*. Closes the reversion path by naming the banned form before it's tried.

### V-04 -- Combined A-form-2 + B-form-2
Numbered list + anti-pointer prohibition. Two independent defenses: ordinal gaps catch incompleteness, explicit prohibition closes the reversion path.

### V-05 -- Combined A-form-2 + B-form-2 + C-form-2
Strongest form. Adds the self-containment directive: *"Item (b) MUST be self-contained -- the four transitions must be readable and verifiable at this checkpoint location without cross-referencing any prior block."* This closes a third failure path where the model writes a numbered list but prefixes it with a summary sentence that softly references the inventory ("as re-stated here from the block above"), technically satisfying anti-pointer while weakening independent verifiability.

**Predicted C-45 outcomes:**
- V-01 through V-05: all target PASS (all enumerate inline)
- V-02 is the compression stress test -- most likely to show a degraded form if the model treats single-line as "close enough to summarize"
- V-03/V-04/V-05: the prohibition sentence should prevent reversion even under output pressure

**Next deepening signal to watch for:** whether V-05's self-containment directive closes the "summary sentence softening" bypass, which would be the candidate signal for C-46.
