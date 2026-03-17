---

# Rubric -- topic-plan (v5)

Three new aspirational criteria extracted from Round 4. All three operate at the **enforcement layer** — the gap between "the instruction is present" and "the model cannot deviate from it."

---

## New criteria: C-21, C-22, C-23

**C-21 — Explicit column-completeness declaration adjacent to each template** | format

Each template definition (proposals, diff, delta findings) is accompanied by an explicit sentence: "The following columns are mandatory. Do not omit any column." The declaration must appear in the prompt, not be inferable from context. A template that defines its columns without this prohibition allows models to silently elide columns when compressing output. Defining columns (which C-19/C-20 require) is a different act from prohibiting their omission.

**C-22 — Active anti-pattern self-naming checkpoint at the delta step** | depth

The prompt instructs the model to stop and *produce* the anti-pattern label as output before proceeding — e.g., "Stop here and name the anti-pattern you are guarding against." This is distinct from C-14 (prompt names the pattern): C-22 requires the model to demonstrate awareness by reproducing the name in its output. The checkpoint is verifiable — a reviewer auditing a response can confirm C-22 by checking whether the label appears; they cannot confirm C-14 without reading the prompt. A prompt that names the anti-pattern in instructions (C-14 pass) without requiring the model to reproduce it is a fail for C-22.

**C-23 — Pre-reproduced null-case templates for all mandatory null sections** | format

Every mandatory null-case section (no-conflicts row, empty-type proposal rows) provides verbatim copy-paste text accompanied by an explicit "Do not omit this table/section" instruction. A prompt that instructs null rows (C-12/C-17 pass) without supplying exact text is a fail for C-23. The "Do not omit" instruction closes the omission path that verbatim text alone cannot close; both components required.

---

## Updated totals

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 15 | 75 |
| **Total** | **23** | **165** |

Composite formula updated: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 75)`

---

**Meta-pattern behind all three:** C-21, C-22, and C-23 share the same layer — *constraint explicitness*. C-21 makes column completeness a named rule. C-22 makes anti-pattern awareness a verifiable output. C-23 makes null-case form a copy-paste act. In each case the behavior was already instructed (by C-19/C-20, C-14, C-12/C-17); what changed is the enforcement surface — moving from "the model should infer this matters" to "the model cannot skip this without producing a visible deviation." The v1→v5 progression mirrors a general pattern: early criteria define *what* to do; later criteria define how to make the *what* structurally unignorable.
