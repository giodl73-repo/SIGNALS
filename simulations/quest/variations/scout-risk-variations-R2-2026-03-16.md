Written to `simulations/quest/golden/scout-risk-variate-R2-2026-03-16.md`.

---

## scout-risk R2 — Five Variations

**R2 strategy**: All three new v2 aspirational criteria (C-11, C-12, C-13) have a structural enforcement gap in R1. Each single-axis variation isolates one mechanism to close exactly one gap.

| ID | Axis | Mechanism | New criterion targeted |
|----|------|-----------|------------------------|
| V-01 | Output format | IF-THEN likelihood syntax | C-12 (all likelihoods trigger-qualified) |
| V-02 | Phrasing register | Mitigation taxonomy + forbidden words | C-11 (zero-generic mitigations) |
| V-03 | Lifecycle emphasis | Mandatory interdependency section ≥2 pairs | C-13 (structured section) |
| V-04 | Output format + Phrasing register | IF-THEN + taxonomy | C-11 + C-12 |
| V-05 | Full integration | All three mechanisms + R1 V-05 base | C-11 + C-12 + C-13 |

### Key design decisions

**C-11 via taxonomy, not re-read**: V-02/V-05 require the model to select a mitigation type (Spike / Validate / Gate / Contract / Cut / Instrument) *before* writing the mitigation prose. Type selection at generation time makes "monitor closely" structurally impossible — a Spike needs a time box and a question, a Gate needs a criterion. R1's re-read gate caught generic text after the fact; taxonomy prevents it at the source.

**C-12 via IF-THEN token, not instruction**: V-01/V-05 require every likelihood to begin with "IF". This is a required syntactic token, not a quality instruction. "IF [condition], THEN this risk activates" cannot be produced alongside a bare probability label like "high" or "~30%". No re-check needed — the form enforces the content.

**C-13 via specificity smell-test**: V-03/V-05 add a rule that "if you find only 1 pairing, your risks are not specific enough — revise them." This indirectly raises risk quality across the whole register, not just the interdependency section.

### Projected scores (v2 rubric)

| ID | Score | Golden |
|----|-------|--------|
| V-01 | ~94 | YES |
| V-02 | ~94 | YES |
| V-03 | ~97 | YES |
| V-04 | ~97 | YES |
| V-05 | **~99** | YES |

All five project GOLDEN because R1's V-03 imperative base already handles all essential + recommended criteria. The R2 differentiation is entirely in aspirational scoring. C-10 (AMEND) remains PARTIAL on all base prompts — that ceiling requires a live AMEND directive to break.
