## Scorecard: review-users Round 3

### Rubric Version
v3 — 15 criteria: 5 essential (60 pts), 3 recommended (30 pts), 7 aspirational (10 pts)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

---

### Per-Variation Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 — All 5 personas present (essential) | PASS | PASS | PASS | PASS | PASS |
| C-02 — Each persona scores 1–5 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-03 — Each persona quotes exact text (essential) | PASS | PASS | PASS | PASS | PASS |
| C-04 — Cross-persona synthesis present (essential) | PASS | PASS | PASS | PASS | PASS |
| C-05 — Aggregate score computed (essential) | PASS | PASS | PASS | PASS | PASS |
| C-06 — First-person voice per persona (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-07 — Role-specific vs universal friction distinguished (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-08 — Persona conflicts identified (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-09 — Friction typed with contrast block (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-10 — Amend loop triggered correctly (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-11 — Score table pre-committed (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-12 — Named-character grounding (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-13 — Inertia fields per persona (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-14 — Pre-walkthrough workaround field (aspirational) | PASS | PASS | PASS | **FAIL** | PASS |
| C-15 — Inline friction tags in first-person sentences (aspirational) | PASS | PASS | PASS | PASS | PASS |
| **Composite** | **100** | **100** | **100** | **99** | **100** |
| **Golden** | YES | YES | YES | YES | YES |

All 5 variations are Golden. All essential criteria pass in every variation.

---

### Criterion-Level Evidence

#### C-09 — All variations PASS under v3

v3 raised the pass bar to require a correct/wrong contrast block (not just inline tag instructions). All five variations provide this block:

- **V-01, V-03**: Global contrast block in the PERSONA WALKTHROUGHS preamble — same placement as R2 V-01/V-04/V-05, which earned PASS under the stricter v3 condition because the contrast block is present.
- **V-02**: Per-section contrast block — a role-appropriate correct/wrong pair inside each persona section instruction line. Strongest structural enforcement (model sees the mechanic at every persona boundary, not just at the top). Same strength as V-05.
- **V-04**: Global contrast block with two correct examples and one wrong example — stronger than V-01/V-03's single correct example.
- **V-05**: Per-section contrast blocks with three correct examples per persona. Strongest of all.

The R2 failure modes (V-02/V-03 PARTIAL — mechanic stated without contrast examples) are fixed in every R3 variation.

#### C-14 — FAIL in V-04

C-14 pass condition: *"each persona section includes a named 'What [Name] does today instead:' field before the walkthrough narrative begins."* The criterion explicitly fails persona sections that **omit this field**.

V-04 moves the workaround entirely into the SCORE SUMMARY TABLE column. The per-persona sections contain no `**Current workaround — what [Name] does today instead:**` field — they only say "Reference [Name]'s current workaround from the SCORE SUMMARY TABLE." This satisfies the criterion's intent (workaround is accessible) but fails its pass condition (the per-persona field is omitted from persona sections).

V-01, V-02, V-03, V-05 all include the named field inside each persona section. PASS.

#### C-14 — ordering note for V-02 and V-03

V-02 and V-03 place the workaround field **after** the scenario brief but before the walkthrough. The criterion requires "before the walkthrough narrative begins" — not "before the scenario brief." Both pass. The ordering is less optimal than V-01/V-05's workaround-first approach (which places the comparison baseline before the character grounding), but it satisfies the criterion.

#### C-10 — All variations PASS

C-10 pass condition is binary: explicit amend proposal with re-scoring when sub-3 score exists. All five variations provide this. V-03 and V-05 go further with a named-workaround slot in the amend template; V-01, V-02, V-04 ground proposals in "Loses to current process." All meet the pass threshold.

---

### Ranking

| Rank | Variation | Composite | Golden | Key differentiator |
|------|-----------|-----------|--------|---------------------|
| 1 (tie) | **V-01** | **100** | YES | Workaround-first ordering — C-14 field before scenario brief |
| 1 (tie) | **V-02** | **100** | YES | Per-section contrast blocks — C-09 enforcement at every persona boundary |
| 1 (tie) | **V-03** | **100** | YES | Amend template with named workaround slot — strongest C-10 actionability |
| 1 (tie) | **V-05** | **100** | YES | All four R3 mechanisms combined — workaround-first + per-section blocks + amend template + table column |
| 5 | **V-04** | **99** | YES | C-14 FAIL: workaround in table only, per-persona field absent |

V-04 scores 99 (6/7 aspirationals: 60 + 30 + 6/7×10 = 98.57 → 99). Its structural bet — pre-commit via table column, reference from persona sections — satisfies the criterion's intent but not its letter.

---

### Why the Four-Way Tie at 100

All four top variations independently satisfy all 15 criteria. This is expected: each was designed to fix a specific gap while preserving R2 V-05's full foundation. R3 had no remaining essential or recommended gaps — only aspirational gaps — and each variation closes all aspirational criteria through different structural mechanisms:

- **V-01** closes C-14 by ordering the field first (before the scenario brief), making the comparison baseline the most recent thing written when the walkthrough begins.
- **V-02** closes C-09 with per-section enforcement, preventing drift across long multi-persona output.
- **V-03** closes C-10 actionability by templating the workaround as a required amend-slot input.
- **V-05** applies all three, plus V-04's table-column pre-commitment.

The rubric criteria are structurally compatible — no variation had to trade one criterion for another.

---

### Excellence Signals

**Signal 1 — Workaround-first ordering creates a comparison cascade (V-01, V-05)**

Placing the workaround field before the scenario brief means the model writes the comparison baseline before inhabiting the character. The order becomes: *who they are without the feature* → *what they face today* → *what they do step-by-step*. When the narrative begins, the alternative is the most recent reference. This is a general prompt-engineering principle: establish the comparison object before establishing the context, not after.

**Signal 2 — Per-section contrast blocks prevent rule decay in long outputs (V-02, V-05)**

R2's global contrast block appeared once in the PERSONA WALKTHROUGHS preamble. By persona 4 or 5, a model generating a long output may drift to sub-section typing because the rule is far behind in context. V-02 embeds a role-appropriate correct/wrong example inside each persona section instruction. The rule is visible at every persona boundary. This is an instance of a broader pattern: structural rules that apply repeatedly across a long output must be repeated at each application site, not just stated once at the top.

**Signal 3 — Named workaround slot in amend template changes the argument type (V-03, V-05)**

When the amend loop instructs "copy the character's 'What [Name] does today instead:' field here verbatim," the model must explicitly state what it is trying to displace before proposing a change. This transforms the amend from "add more explanation to this section" (abstract usability patch) to "this proposed change makes [specific workaround] unnecessary because [mechanism]" (workaround-replacement argument). The template field changes the type of reasoning the model performs, not just the format of the output.

---

### Round Summary

| Metric | Value |
|--------|-------|
| Variations scored | 5 |
| Golden | 5 (all) |
| Top composite | 100 |
| All essential pass | YES |
| Failing essential criteria | None |
| Failing aspirational criteria | C-14 in V-04 only |
| Best C-09 enforcement | V-02, V-05 (per-section contrast blocks) |
| Best C-10 actionability | V-03, V-05 (named workaround slot in amend template) |
| Best C-14 structure | V-01, V-05 (workaround-first, before scenario brief) |
| New pattern count | 3 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["workaround-first ordering (field before scenario brief) creates a comparison cascade — establishing the alternative before the character grounding means the baseline is the most recent reference when narrative begins; a general principle: establish the comparison object before the context, not after", "per-section contrast blocks prevent rule decay in long multi-persona outputs — rules that apply repeatedly across many sections must be restated at each application site; a global preamble rule is too far away by persona 4 or 5", "named workaround slot in amend template changes the argument type from abstract usability patch to workaround-replacement argument — requiring the model to copy the workaround verbatim before proposing a change transforms 'add more detail' into 'this change makes [specific workaround] unnecessary because [mechanism]'"]}
```
