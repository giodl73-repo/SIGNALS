# quest-rubric Variate — Round 7 (Round 3 against rubric v3)
**Date:** 2026-03-15
**Rubric:** v3 (C-01–C-14; adds C-14: contrast-in-Text — the "not: X but: Y" template embedded within the criterion Text field construction instruction, not only in preamble or structural framing)
**Target criterion:** C-14

**Round 3 design note:** Rounds 1–2 against rubric v3 explored failure-mode-first sequencing, aspirational-tier competitor framing, tier-as-failure-dimension lifecycle design, and Builder+Scrutineer role pairs targeting C-11/C-12/C-13. The scorecard pattern is consistent: C-10 partial every time. Contrast awareness lives in preamble or emerges structurally from failure-dimension design, but the "not: X but: Y" template never appears inside the Text field construction instruction. V-01 through V-04 from Round 2 all partially satisfy C-10 through earlier framing — none satisfy C-14 because none carry the contrast requirement into the per-criterion Text field instruction itself. This round targets exactly that gap. Three single-axis variations probe distinct mechanisms for embedding contrast in the Text field instruction; two combined variations close C-14 while preserving Round 2 coverage of C-11/C-12/C-13.

---

## Round 7 Variation Map

| Variation | Axis | C-14 probe | C-11/C-12/C-13 coverage | Notes |
|-----------|------|-----------|------------------------|-------|
| V-01 | Phrasing register (constitutive contrast) | Very strong — criterion Text is defined constitutively as a contrast statement; a Text without "not: X but: Y" is not a criterion Text by definition | C-12 partial (downstream consequence encouraged but not explicitly gated), C-11/C-13 not targeted | Single-axis; constitutive definition cannot be satisfied by adding a preamble; risk: constitutive framing is abstract and may produce syntactically compliant but semantically shallow contrast |
| V-02 | Output format (six-column contrast-pair table) | Very strong — explicit "Rejects" column in criteria table makes absent contrast a visible blank cell; blank cells are structural violations, not judgment calls | C-11/C-12/C-13 not targeted | Single-axis; contrast enforced by table structure, not instruction recall; risk: "Rejects" cells may be filled with generic negations rather than the specific rejected form |
| V-03 | Role sequence (Builder + Contrast Auditor) | Very strong — Contrast Auditor interrogates each Text field post-draft for "not: X but: Y" and issues per-criterion revision instructions; distinguishes contrast-in-preamble from contrast-in-Text | C-11/C-12/C-13 not targeted | Single-axis; post-draft review catches the exact gap — contrast framing present earlier in prompt but not carried into Text; risk: Auditor scope creep into non-contrast properties |
| V-04 | Role sequence + phrasing register (constitutive + Auditor) | Very strong — constitutive definition prevents contrast-absent Text during drafting; Auditor verifies compliance per criterion and issues targeted revisions | C-12 partial (downstream consequence named in constitutive definition), C-11/C-13 coverage moderate | Combined; two independent mechanisms targeting C-14 — generation-phase definition and post-draft verification; risk: redundant checks produce verbose output without adding criterion quality |
| V-05 | Inertia framing + output format (near-excellent reference + Rejects column) | Very strong — names the rubric that passes C-01–C-13 but fails C-14 (contrast in preamble, not in Text); Rejects column in table enforces contrast structurally per criterion | C-11 strong (near-excellent reference named before aspirational criteria), C-12 partial, C-13 partial | Combined; motivational framing (why C-14 matters vs. near-excellent competitor) + structural enforcement (table column); closes C-11 and C-14 simultaneously |

---

## V-01 — Phrasing Register (Constitutive Contrast)

**Axis:** Phrasing register
**Hypothesis:** Round 2 V-02 (criterion-as-argument) defined a criterion Text constitutively as "the argument" and a Pass condition as "the conclusion of that argument" — making C-12 compliance structural from first draft because a Text that only labels fails the constitutive definition. V-01 applies the same constitutive move to C-14: a criterion Text is not merely permitted to include contrast framing — it IS a contrast statement. A Text that names only the requirement without naming the rejected form is not a criterion Text; it is an assertion that happens to be correct. Contrast framing cannot be added by appending a preamble because the preamble does not modify the Text field's definition. The hypothesis is that constitutive definition produces C-14 compliance at a higher rate than instructional framing ("include not: X but: Y") because constitutive definitions cannot be satisfied by structural compliance elsewhere — the operator must satisfy them per criterion, in the Text field, or the Text field fails the definition.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

A criterion Text field has a constitutive definition:

**A criterion Text IS a contrast statement.** It names what the criterion requires AND names the form it rejects — "not [rejected form] but [required form]." A Text that states only what must be true without naming what is rejected has not built a criterion; it has labeled a preference. Preference labels can be transplanted to any rubric for any skill without losing content because they contain no specification of what they exclude. Contrast statements cannot be transplanted without revision because the rejected form is specific to this skill's failure modes.

The structure of the contrast is: **not [X] but [Y]** — where X is the specific form this criterion prohibits and Y is the form it requires. X and Y are not mere inversions of each other ("not absent but present"); X is a specific wrong answer that a real output might exhibit, and Y is the specific right answer that distinguishes passing from failing.

This definition is constitutive. A five-field structure whose Text satisfies it contains a criterion. One whose Text only states what must be true contains a preference assertion.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

Name the failure modes — what makes an output of this skill non-functional or misleading?
For each failure mode, name:
1. The specific wrong answer a real output might exhibit (this becomes X — the rejected form).
2. The specific right answer that distinguishes passing from failing (this becomes Y — the required form).

---

**Build the rubric.**

Write criteria satisfying the constitutive definition above. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — the contrast statement. Must encode "not [X] but [Y]" where X is the specific wrong form this criterion prohibits and Y is the specific right form it requires. A Text that names only Y without naming X fails the constitutive definition and must be rewritten before the next criterion is drafted.
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence — names the observable from the Text's contrast. Uses count thresholds, named fields, structural patterns, or explicit enumerations. No "is clear" or "adequately covers" as the sole criterion.

Before finalizing each criterion Text, apply the contrast check:

> "Does this Text name the specific wrong form X alongside the required form Y? Or does it name only Y? A Text that says 'criterion Text fields must include causal reasoning' fails the contrast check — it names Y but not X. A Text that says 'not [a Text that labels what must be true without naming what it rejects] but [a Text that states not: X but: Y in the Text field itself]' passes it."

If the Text names only Y: identify the specific wrong form X — the real output that would fail this criterion — and rewrite the Text to name it explicitly before naming Y.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. All three tiers required.

Essential: the contrast observable whose absence makes the output non-functional or misleading.
Recommended: pass condition tests a quality property — degree, precision, specificity — not just contrast presence.
Aspirational: goes beyond what essential and recommended require. Must not restate an essential.

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — invoke the constitutive definition: a criterion Text IS a contrast statement naming both the rejected form and the required form; a Text that names only the requirement is a preference assertion, not a criterion), then criteria ordered essential → recommended → aspirational, then scoring section.

---

## V-02 — Output Format (Six-Column Contrast-Pair Table)

**Axis:** Output format
**Hypothesis:** Round 1 V-02 (table-first format) demonstrated that a five-column criteria table enforces structural completeness (C-01) because blank cells are visually obvious violations that do not require judgment to detect. V-02 extends this mechanism to C-14 by adding a sixth column — "Rejects" — that forces each criterion to name the prohibited form alongside the required form in the Text. The key difference from prior contrast framing: a "Rejects" cell is not satisfied by preamble or framing; it must be filled per row, for each criterion individually, with the specific wrong form that criterion excludes. The hypothesis is that a visible, mandatory column produces C-14 compliance at a higher rate than instructional framing because the structural gap (blank cell) is detectable without reading the Text for contrast content — the format enforces what the instruction only encourages.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Inputs:** skill spec (required), sample outputs (optional).

**Analysis**

Read the skill spec. Identify:
- What the skill produces: artifact shape, required fields, content structure.
- Lifecycle phases: what each phase delivers.
- Failure modes: what makes an output of this skill non-functional?

For each failure mode, identify both:
1. **The wrong form** — the specific output pattern that fails. What does a real bad output look like?
2. **The right form** — the specific output pattern that passes. What distinguishes passing from failing?

---

**Criteria table**

Produce a criteria table. All six columns are required for every row. No cell may be blank, null, or "TBD."

| ID | Rejects | Text | Weight | Category | Pass condition |
|----|---------|------|--------|----------|----------------|

Column rules:

- **ID**: C-01, C-02, ... sequential.
- **Rejects**: name the specific wrong form this criterion prohibits — the real output pattern that fails. Not a generic negation ("not absent") but the specific answer a real output might exhibit that this criterion rules out. This is the X in "not X but Y." Without a Rejects entry, the Text field lacks contrast and cannot satisfy C-14.
- **Text**: one sentence encoding the contrast pair from the Rejects column: "not [Rejects] but [required form]." The Rejects column content must appear in or directly inform the Text's contrast framing. A Text whose contrast is not traceable to the Rejects entry is a structural mismatch and must be revised.
- **Weight**: `essential` | `recommended` | `aspirational`. Exactly 3-5 essential, 2-3 recommended, 1-2 aspirational.
- **Category**: `correctness` | `depth` | `format` | `coverage` | `behavior`.
- **Pass condition**: one auditable sentence using observable anchors (count thresholds, named fields, structural patterns, enumerations). No "is clear" or "adequately covers" as the sole criterion.

Essential criteria target behaviors whose absence makes the output non-functional.
Recommended criteria target the gap between passing and good — each pass condition tests a quality property, not just presence.
Aspirational criteria target the gap between good and excellent — each must go beyond what essential and recommended require.

---

**Scoring section**

After the criteria table, write:

```
composite = (essential_pass / N_e * 60)
          + (recommended_pass / N_r * 30)
          + (aspirational_pass / N_a * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter: `skill: quest-rubric`, `skill_target: {skill}`, `date: {today}`, `version: 1`

Body: purpose statement (2-3 sentences — state that each criterion's Text encodes "not [Rejects] but [required form]" because a criterion that names only what it requires cannot be distinguished from a criterion that accepts any reasonable form), then the criteria table (six columns, essential → recommended → aspirational ordering by weight), then the scoring section.

---

## V-03 — Role Sequence (Builder + Contrast Auditor)

**Axis:** Role sequence
**Hypothesis:** Round 2 V-05 (Builder + Scrutineer) demonstrated that calibrated post-draft interrogation of exactly the aspirational properties being tested produces reliable compliance because the Scrutineer's narrow scope generates precise revisions rather than generic improvement. V-03 applies the same two-role architecture to C-14 alone: the Builder drafts criteria without contrast constraints (exactly as prior rounds produced — adequate essential criteria with contrast possibly present in preamble), and the Contrast Auditor then interrogates each criterion's Text field specifically for "not: X but: Y" structure. The Auditor distinguishes the exact gap that C-14 targets: contrast framing present in earlier sections of the prompt (satisfying C-10 partially) but not carried into the individual criterion Text field instructions (failing C-14). The hypothesis is that a post-draft Auditor whose interrogation question is calibrated exactly to the C-14 gap — "does this Text field name what it rejects, or does it rely on earlier framing to supply the contrast context?" — produces higher C-14 compliance than generation-phase instructions, because the Auditor can detect preamble-reliance that the Builder cannot self-detect during drafting.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence: the Builder drafts the rubric, the Contrast Auditor interrogates every criterion's Text field for contrast structure and issues per-criterion revision instructions, and the Builder incorporates all required revisions. The final artifact reflects the post-revision state; Auditor notes do not appear in the output.

---

**BUILDER ROLE**

Read the skill spec. Extract:
1. What the skill produces — artifact type, required fields, structural shape.
2. Lifecycle phases — what each phase delivers.
3. At least 3 failure modes — what makes an output of this skill non-functional or misleading?

For each failure mode, draft one essential criterion with all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor — count thresholds, presence/absence of named fields, structural patterns, explicit enumerations. Phrases like "is clear", "seems appropriate", "adequately covers" are not observable anchors.

Draft 3-5 essential criteria. Then draft 2-3 recommended criteria (pass conditions test quality properties, not just presence) and 1-2 aspirational criteria (go beyond essential and recommended). Continue sequential C-NN numbering.

---

**CONTRAST AUDITOR ROLE**

The Contrast Auditor interrogates every criterion's Text field — essential, recommended, and aspirational — for a single structural property: does the Text name what this criterion rejects alongside what it requires?

For each criterion (C-01 through C-NN), apply the contrast diagnostic:

> "Does this Text encode 'not [X] but [Y]' — where X is the specific wrong form this criterion prohibits, and Y is the specific right form it requires? Or does this Text state only Y, relying on the preamble or an earlier section of the prompt to supply the contrast context?"

Evaluate the difference:
- **Preamble-reliant contrast** — the Text says "the rubric must have testable pass conditions" because an earlier section established that qualitative language is the problem. The Text names Y but not X. If the Text is read in isolation — stripped from the prompt — the rejected form (qualitative language) disappears. This is a C-14 failure.
- **Text-embedded contrast** — the Text says "not [qualitative language like 'is clear' or 'seems thorough'] but [observable anchors: count thresholds, named fields, structural patterns, or explicit enumerations]." The rejected form X is present in the Text field itself. Reading the Text in isolation, the contrast is intact. This is a C-14 pass.

For each criterion whose Text does not embed the contrast:

```
C-NN Text revision required:
  Current Text: [quote as drafted]
  Issue: the Text names the required form (Y) without naming the rejected form (X).
         Contrast is implied by earlier framing but not present in the Text field itself.
         Reading this Text in isolation, the rejected form disappears.
  Rejected form (X): [name the specific wrong answer a real output might exhibit —
                      not a generic negation, but the specific pattern this criterion
                      excludes. E.g., "qualitative-only language like 'is clear' or
                      'adequately covers'" not "the absence of observables."]
  Instruction: Rewrite the Text to encode: "not [X] but [Y]" — the rejected form
               named explicitly in the Text field, not supplied by context from
               earlier sections. The Pass condition does not change; only the Text
               is revised.
```

After all revision instructions are issued, the Builder rewrites the flagged criteria. The Auditor reviews the revisions once. If any rewritten Text still fails the contrast diagnostic (the rejected form is still absent or generic), the Auditor issues a second revision instruction.

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the Contrast Auditor's interrogation target: each criterion's Text field must embed "not: X but: Y" such that the contrast is intact when the Text is read in isolation, stripped from all preamble context), then criteria ordered essential → recommended → aspirational (Auditor revision notes omitted; revisions incorporated silently), then scoring section.

---

## V-04 — Role Sequence + Phrasing Register (Constitutive + Contrast Auditor)

**Axis:** Role sequence (Builder + Contrast Auditor) + phrasing register (constitutive contrast definition)
**Hypothesis:** V-01 (constitutive contrast definition) prevents contrast-absent Text fields during drafting — a Text without "not: X but: Y" fails the constitutive definition and must be rewritten before the next criterion is drafted. V-03 (Contrast Auditor) detects preamble-reliant contrast post-draft and issues targeted per-criterion revisions. Combined: the constitutive definition builds contrast into the generation-phase instruction, preventing most C-14 failures at source; the Auditor catches any that drift. The hypothesis is that the combination produces higher C-14 compliance than either mechanism alone because they address different failure modes: the constitutive definition prevents generation-phase omissions, and the Auditor detects cases where the operator satisfied the definition syntactically (X and Y are both named) but X is generic rather than specific — "not absent but present" rather than "not [specific wrong form] but [specific right form]." V-04 also carries moderate coverage of C-12 (Text-argues-before-Pass-concludes) because the constitutive Text definition establishes the causal downstream consequence as part of the contrast framing — the wrong form X must name the specific failure it causes, making the downstream consequence present in the Text by construction.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence. The Builder drafts the rubric using a constitutive definition of the criterion Text field. The Contrast Auditor reviews every criterion's Text field for contrast specificity and issues revision instructions for any Text whose contrast is generic. The Builder incorporates all revisions. The final artifact reflects the post-revision state; Auditor notes do not appear in the output.

---

**Constitutive definition (applies to both roles):**

A criterion Text field IS a contrast statement. It names both the rejected form (X) and the required form (Y): "not [X] but [Y]." X must be the specific wrong answer a real output might exhibit — not a generic negation. Y must be the specific right answer that distinguishes passing from failing. A Text that names only Y without naming X is not a criterion Text; it is a preference assertion. A Text that names X as a generic negation ("not absent" / "not qualitative") rather than a specific wrong form is a degraded contrast that fails to specify what it excludes precisely enough to be verifiable.

---

**BUILDER ROLE**

Read the skill spec. Extract:
1. What the skill produces — artifact type, required fields, structural shape.
2. Lifecycle phases — what each phase delivers.
3. At least 3 failure modes. For each failure mode, identify:
   - The specific wrong form (X): what does a real bad output look like for this failure?
   - The specific right form (Y): what distinguishes passing from failing?

Draft criteria using the constitutive definition. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence encoding "not [X] but [Y]" where X is the specific wrong form and Y is the specific right form. A Text that names only Y fails the constitutive definition — identify the specific wrong form X before proceeding to the next criterion.
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence — names the observable from the Text's contrast. Count thresholds, named fields, structural patterns, explicit enumerations. No "is clear" or "adequately covers" as sole criterion.

Draft 3-5 essential criteria, then 2-3 recommended (pass conditions test quality properties), then 1-2 aspirational (go beyond essential and recommended). Sequential C-NN numbering throughout.

---

**CONTRAST AUDITOR ROLE**

The Contrast Auditor interrogates every criterion's Text field against the constitutive definition. Specifically: is X a specific wrong form, or a generic negation?

For each criterion, apply the specificity diagnostic:

> "Is the rejected form X — the thing this criterion's Text names as excluded — specific enough that a real output exhibiting X could be identified by a third party? Or is X a generic negation that any reasonable observer would already know to avoid?"

Specificity test:
- **Generic X** (fails): "not qualitative language" / "not absent" / "not vague" — any evaluator familiar with rubric design already knows these are wrong forms; the Text adds no specification.
- **Specific X** (passes): "not pass conditions phrased as 'the output is clear and comprehensive'" / "not criterion Text fields that name only the requirement without naming the specific failure pattern they exclude" — specifies the exact wrong form, allows a third party to check whether an output exhibits it.

For each criterion whose X is generic:

```
C-NN Text specificity revision required:
  Current X: [quote the rejected form as stated]
  Issue: the rejected form is a generic negation, not a specific wrong answer.
         A third party cannot use this Text to identify an output that exhibits X —
         any evaluator would already exclude this form without the criterion's guidance.
  Specific wrong form: [name the exact pattern a real output might exhibit that this
                        criterion excludes — concrete enough to recognize in an artifact]
  Instruction: Rewrite the Text to name the specific wrong form: "not [specific
               wrong form] but [specific right form]." The Pass condition does not
               change; only X in the Text is made specific.
```

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — invoke the constitutive definition: a criterion Text IS a contrast statement encoding "not [specific wrong form] but [specific right form]"; a Text whose X is generic fails to specify what it excludes), then criteria ordered essential → recommended → aspirational (Auditor revision notes omitted), then scoring section.

---

## V-05 — Inertia Framing + Output Format (Near-Excellent Reference + Rejects Column)

**Axis:** Inertia framing (near-excellent reference that fails C-14) + output format (six-column contrast-pair table)
**Hypothesis:** Round 2 V-01 (aspirational-tier competitor) demonstrated that naming a near-excellent reference — a rubric that passes C-01 through C-08 but falls short on aspirational criteria — creates structural pressure toward the aspirational tier because the aspirational section must identify exactly what the near-excellent competitor lacks. V-05 names a more specific competitor: a rubric that passes all of C-01 through C-13 (including the Round 2 aspirational criteria — causal observables, contrast example in preamble, tier-grounded category diversity, reference anchor) but fails C-14 because its Text field construction instruction never requires "not: X but: Y." This competitor scores approximately 96–98 against the current rubric's formula; the delta to 100 is exclusively C-14. Combined with the six-column contrast-pair table from V-02, V-05 closes C-14 from two directions: the inertia framing motivates the requirement by naming the specific gap (contrast in preamble but not in Text), and the Rejects column enforces it structurally per criterion. The combination also covers C-11 (aspirational reference anchor) strongly because the near-excellent reference is named and described in detail before the aspirational section.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your rubric has a near-excellent competitor.

**The near-excellent competitor** is a rubric built in a prior round using the failure-mode-first tier-dimension design method. It has:
- Five or more criteria with all five fields complete and non-empty
- Pass conditions anchored in observable anchors — counts, named fields, structural patterns
- Essential criteria derived from failure mode analysis, traceable to the skill spec
- A composite formula and golden threshold stated explicitly
- Tier distribution within the 3-5 / 2-3 / 1-2 target ranges
- Three or more distinct categories across its criteria
- Tier design grounded in distinct failure dimensions, producing organic category diversity
- An aspirational section that names a near-excellent reference from a prior round

Against the current rubric's formula, the near-excellent competitor scores approximately 96. It passes every essential criterion, every recommended criterion, and aspirational criteria C-09 through C-13.

**Its single gap:** C-14. The near-excellent competitor's preamble establishes contrast framing — it names the vague rubric as the rejected competitor, it may include a "not: X but: Y" example in its introductory material. But its criterion Text field construction instruction never requires each individual Text field to encode "not: X but: Y." A builder following the near-excellent competitor's prompt will produce criterion Text fields that state what must be true without naming the specific form that is rejected — because the Text field instruction says "state what must be true," not "state not [rejected form] but [required form]." The contrast lives in the preamble, not in the criterion Text field instruction. A builder who reads only the Text field instruction — not the full preamble — produces contrast-absent criteria.

Your rubric must reach 100. The near-excellent competitor scores 96. The gap is C-14.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

Name at least 3 failure modes. For each failure mode, identify both:
1. **The specific wrong form (X)** — what a real bad output looks like.
2. **The specific right form (Y)** — what distinguishes passing from failing.

---

**Before writing aspirational criteria, name the reference:**

```
Reference: [Name the near-excellent competitor specifically — a prior-version rubric,
  a named method (e.g., "the failure-mode-first tier-dimension rubric built using
  V-03 + V-04 from Round 2"), or a rubric class described precisely enough to be
  recognized. Must be a specific artifact, not a hypothetical.]

Passes: C-01 through C-13 — five-field completeness, observable anchors, failure-mode
  derivation, formula + threshold, skill-specific criteria, tier distribution, category
  diversity, causal linkage in Text, contrast framing in preamble, tier-grounded
  organic diversity, aspirational reference anchor.

Fails: C-14 — the contrast template ("not: X but: Y") is not embedded within the
  criterion Text field construction instruction. The preamble establishes contrast
  framing but does not carry it into the per-criterion Text instruction. A builder
  following only the Text field instruction produces criteria that name Y without
  naming X.
```

---

**Criteria table**

Produce a criteria table. All six columns are required for every row. No cell may be blank, null, or "TBD."

| ID | Rejects | Text | Weight | Category | Pass condition |
|----|---------|------|--------|----------|----------------|

Column rules:

- **ID**: C-01, C-02, ... sequential.
- **Rejects**: the specific wrong form X — the pattern a real bad output would exhibit that this criterion excludes. Must be specific enough to recognize in an artifact. Generic negations ("not vague", "not absent") are not valid Rejects entries; they describe classes of badness that any evaluator already knows to avoid. The Rejects entry must name the specific form — e.g., "a criterion Text that states 'pass conditions must be testable' without naming what untestable pass conditions look like."
- **Text**: one sentence encoding the contrast: "not [Rejects] but [required form]." The Rejects column content must appear in or directly inform the Text's contrast framing. A Text whose contrast is not traceable to the Rejects entry is a structural mismatch and must be revised. This is the instruction the near-excellent competitor's Text field lacks — embedding "not [X]" in the Text itself, not only in the preamble.
- **Weight**: `essential` | `recommended` | `aspirational`. Exactly 3-5 essential, 2-3 recommended, 1-2 aspirational.
- **Category**: `correctness` | `depth` | `format` | `coverage` | `behavior`.
- **Pass condition**: one auditable sentence using observable anchors. No "is clear" or "adequately covers" as sole criterion.

---

**Aspirational criteria**

Write aspirational criteria that describe the exact dimension in which the named near-excellent reference falls short. Each aspirational criterion should name or implicitly reference what the near-excellent competitor lacks: "a rubric built without [aspirational property] [fails this specific way] because [mechanism]."

---

**Scoring section**

```
composite = (essential_pass / N_e * 60)
          + (recommended_pass / N_r * 30)
          + (aspirational_pass / N_a * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter: `skill: quest-rubric`, `skill_target: {skill}`, `date: {today}`, `version: 1`

Body: purpose statement (2-3 sentences — name the near-excellent competitor and state that the delta from 96 to 100 is C-14: the contrast template embedded in the criterion Text field instruction, not only in the preamble), then criteria table (six columns, essential → recommended → aspirational), then scoring section. The aspirational reference preamble (Reference / Passes / Fails) is retained in the artifact before the aspirational criteria rows.
