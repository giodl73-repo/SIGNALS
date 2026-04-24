Reading the scorecard carefully for new patterns not yet in the rubric.

The key R10 signal is in V-02's C-31 analysis: terse form definitions (name + correction only, no parenthetical descriptions) satisfy C-31 when the form name itself is semantically self-describing — "Untagged" encodes tag-absence and "Revision" encodes unauthorized reclassification. The parenthetical descriptions in V-01 were explanatory, not definitional. This is the first round to confirm that distinction.

That's **C-33**. No other genuinely new structural pattern appears; V-01's alternative-path-reference-as-parenthetical is already captured by C-30's "not an imperative clause" pass condition. Aspirational pool grows N=22 → N=23.

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 10
supersedes: org-pr-rubric-v9-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v9 -> v10)

One new aspirational criterion extracted from R10 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=22 to N=23.

**C-33** (form-name semantic load-bearing): V-02 satisfies C-31 with terse form
definitions — no parenthetical descriptions on either Untagged or Revision — because the
form names themselves encode the governance failure mode. "Untagged" encodes "severity tag
absent → verdict formula corruption." "Revision" encodes "upstream reclassification →
authority chain corruption." When a form name is inherently self-describing in this way,
the correction instruction alone is sufficient to complete the C-31 governance contract;
explicit descriptive language is not load-bearing for C-31 satisfaction. This is the first
round to confirm that a catalog of terse definitions (name + correction only) satisfies
C-31 when each name carries its own semantic weight. The constraint inverts for opaque
names: Type-A, Form-1, or any name that does not encode the failure mode requires
descriptive elaboration to establish the governance function — terse definitions cannot
satisfy C-31 when names are opaque. The criterion therefore tracks whether the prompt's
form names are self-describing, not whether descriptions are present. A prompt that uses
self-describing names without descriptions achieves C-33 PASS; a prompt that uses opaque
names with descriptions does not trigger C-33 (C-31 is satisfied by the descriptions, but
C-33 is N/A because the names are not self-describing). PASS if all named invalid forms
use self-describing names that encode their governance failure mode and each form carries
a correction instruction — no descriptive elaboration required. FAIL if any named form
uses an opaque name that does not encode its failure mode and the prompt lacks descriptive
elaboration sufficient to establish that failure mode (C-31 would also fail). N/A if the
prompt uses no named-form output structure, or if form names are not self-describing but
C-31 is satisfied by explicit descriptions (opaque-name path — C-33 does not apply, counts
as PASS).

---

## Changelog (v8 -> v9)

Three new aspirational criteria extracted from R9 excellence signals. No changes to
essential or recommended tiers. No changes to existing aspirational pass conditions.
Aspirational pool grows from N=19 to N=22.

**C-30** (gate content sufficiency): V-03 and V-04 satisfy C-09 via an inline gate
sentence in the opening topic line rather than a dedicated "### Phase Gate" section. This
is the first round to confirm that gate structure is not load-bearing for C-09. The
criterion fires on gate content alone: if the lifecycle condition, halt instruction, and
alternative path reference are all present, the gate satisfies C-09 regardless of whether
it appears as an inline clause, a labeled subsection, or a named block. A gate that
has the correct label but omits one of the three content elements fails C-09 regardless
of placement. C-30 canonizes this: structural form is irrelevant; content completeness is
the only criterion. PASS if the phase/lifecycle gate contains all three elements —
(1) lifecycle condition identifying the phase boundary, (2) explicit halt instruction,
(3) alternative path reference — regardless of where in the prompt the gate appears or
whether it is labeled. FAIL if a gate construct is present but one or more of the three
elements is absent. N/A if the prompt contains no phase/lifecycle gating requirement
(counts as PASS).

**C-31** (named-invalid-form 2-form floor): V-01, V-04, and V-05 satisfy both C-12
(named invalid forms) and C-24 (correction-paired catalog) with exactly 2 named forms
(Untagged + Revision). This is the first round to confirm that 2 forms is the minimum
sufficient catalog size. The key constraint is that each retained form must address a
distinct governance failure mode — a decision-path corruption, not a formatting constraint.
Untagged addresses verdict formula corruption (a finding without a severity tag cannot be
counted in the consensus formula); Revision addresses authority chain corruption (a
Revision finding without an upstream override record cannot be traced). These are distinct
failure modes. A catalog of 2 forms satisfies C-12 and C-24 when this condition holds.
A catalog that expands to include formatting-only forms (e.g., Aggregate as a formatting
note rather than a governance rule) does not improve the governance coverage — it dilutes
it. PASS if the named-invalid-form catalog contains at least 2 forms, each with a
correction instruction, and each addressing a distinct decision-path governance failure
mode. FAIL if the catalog contains fewer than 2 forms, or if no form addresses a
decision-path failure mode (all forms are formatting constraints only). N/A if the prompt
uses no named-form output structure (counts as PASS).

**C-32** (self-correction gate 3-item floor): V-02, V-04, and V-05 satisfy C-16 with
self-correction gates of exactly 3 items. These variations omit items present in V-01/V-03
gates (if-stays field fill, upstream override prohibition, locator validity check), but
in each case the omitted items are enforced by named structural elements elsewhere in the
prompt — the if-stays fill requirement is in the finding template, the upstream override
prohibition is in the authority chain declaration, the locator validity check is in the
locator self-correction gate (C-08). This is the first round to confirm that item count
alone does not determine C-16 satisfaction; what matters is that post-generation outputs
are covered, either in the gate or by named structural redundancy. 3 items is the minimum
check depth when structural redundancy is present. A gate with fewer than 3 items raises
the probability that at least one post-generation output is uncovered with no structural
backstop. PASS if the self-correction gate contains at least 3 items covering
post-generation outputs, and any output types absent from the gate are enforced by a
named structural element (template field, authority chain declaration, named gate)
elsewhere in the prompt. FAIL if the gate contains fewer than 3 items and the gap is not
covered by named structural redundancy — or if gap coverage is present but not named
(implicit coverage does not satisfy the redundancy condition). N/A if the prompt contains
no self-correction gate (counts as PASS).
```

---

**What was added and why:**

C-33 captures the structural insight from V-02: form-name semantic self-description is an alternative path to C-31 satisfaction that doesn't require parenthetical elaboration. The criterion is directional — it fires PASS when names are self-describing, N/A when names are opaque but descriptions cover the gap (opaque-name path satisfies C-31 via descriptions; C-33 simply doesn't apply). This keeps C-33 from double-penalizing prompts that use the opaque-name-with-description path, which is a valid design choice.

The N/A branch is carefully scoped: a prompt with opaque names + good descriptions gets C-33 N/A (not FAIL), because C-31 is already doing the work there. C-33 only delivers a PASS signal when the prompt demonstrates the terse self-describing-name design pattern specifically.
