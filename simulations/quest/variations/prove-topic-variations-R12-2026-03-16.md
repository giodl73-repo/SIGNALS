Written to `simulations/quest/golden/prove-topic-variate-R12-2026-03-16-v14.md`.

---

## Round 12 — 5 Variations

**R12 thesis**: R11 V-05 achieved C-09 via a conviction ladder. This round tests whether simpler mechanisms are sufficient.

| Var | Axis | C-09 mechanism | Predicted score |
|-----|------|----------------|-----------------|
| V-01 | per_claim_synthesis_table | Required THIN EVIDENCE IMPACT TABLE at synthesis with "Source Stage + Specific Claim + Confidence" columns | ~95-100 |
| V-02 | named_hypothesis_claims | CLAIM INDEX at Stage 1 gives THIN flags precise targets; per-claim table cannot be vague | 100 |
| V-03 | inline_weakens_annotation | "weakens: [claim]" in every THIN flag at discovery; synthesis copies verbatim | 100 |
| V-04 | named_claims + inline_weakens | CLAIM IDs committed at Stage 1 + THIN flags annotated with CLAIM-N; tightest possible chain | 100 |
| V-05 | full integration | All three axes + scout gate + full paths + per-stage gate emits | 100 |

**Key finding if scoring confirms predictions**: The conviction ladder, PRE-STAGE COMMITMENT BLOCK, HANDOFF-exclusive synthesis, and four-ceiling ordering from R11 V-05 are all unnecessary for v14. The minimum for C-09 full pass is: (1) named claims at hypothesis stage, (2) "weakens: CLAIM-N" in THIN flags, (3) per-claim confidence table at synthesis referencing source stage.

V-01 is the ablation probe — testing whether even the CLAIM INDEX is needed, or whether a well-structured synthesis table with clear column instructions is enough on its own.
