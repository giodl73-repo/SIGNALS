# org-review Variations — Round 1
Generated: 2026-03-15
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-2026-03-15.md

---

## V-01 — Role Sequence: Inertia-First

**Variation axis**: Role sequence — challenger role runs before product and technical roles
**Hypothesis**: Forcing the inertia-advocate to run first, before PM or architect have framed the artifact positively, sets a null-hypothesis baseline that subsequent reviewers must actively depart from. This increases C-03 perspective fidelity by preventing the PM from anchoring the framing before the challenger speaks.

---

You are running `org-review` on the artifact provided below.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to identify available reviewers. You will see role files including `pm.md`, `architect.md`, and `inertia-advocate.md`. Do not invent roles — all reviewers must come from this directory.

- **Standard depth** (default): Select the roles most relevant to the artifact type. For a spec artifact: architect + inertia-advocate. For a proposal artifact: pm + inertia-advocate. For a feasibility artifact: architect + pm. State which roles you selected and why.
- **`--depth deep`**: Include every role found in `.craft/roles/signal/`. State the total count.

**Step 2 — Inertia Gate (runs first, always)**

Before any other reviewer speaks, the `inertia-advocate` reviews the artifact. This is not optional. The inertia-advocate plays the role of the status quo and argues the case for doing nothing.

Apply the inertia-advocate's lens from its role file:
- Verify: What is the team doing today instead of this? Is the workaround actually worse? Has anyone talked to non-adopters?
- Simplify: The inertia case is HIGH threat. Name what the team does today before naming anything else.
- Expertise: switching cost quantification, null hypothesis construction, adoption friction modeling.

Produce the inertia-advocate's review entry with all four fields:
- **Role**: inertia-advocate
- **Findings**: What the null hypothesis is; whether the artifact addresses it; specific gaps
- **Severity**: HIGH / MEDIUM / LOW — calibrate to how well the artifact addresses inertia
- **Recommendation**: What the artifact must add or change to survive the inertia test

Also include at least one **Verify Question** from the inertia-advocate's lens.

**Step 3 — Remaining Reviewers**

After the inertia gate, apply each remaining selected role in sequence. For each role:

1. Read the role's `lens.verify`, `lens.simplify`, and `expertise` fields from its `.craft/roles/signal/` file.
2. Do NOT echo the inertia-advocate's framing — this role has its own orientation. A PM finding addresses decision/commitment concerns. An architect finding addresses feasibility/boundary/complexity concerns.
3. Produce a review entry with all four fields: **Role**, **Findings**, **Severity**, **Recommendation**.
4. Include at least one **Verify Question** from that role's verify lens.
5. Apply the simplify lens: what could be removed, collapsed, or clarified from this role's perspective?

Use consistent severity vocabulary across all reviewers: HIGH / MEDIUM / LOW. Not all findings may share the same level — if they do, re-examine.

**Step 4 — Synthesis**

After all reviewer entries, produce a **Cross-Role Summary** section:
- Where do reviewers agree?
- Where do they diverge or contradict each other? Name the conflict explicitly if one exists.
- Which artifact areas are most at risk?
- What is the overall signal: ready / conditional / blocked?

**Artifact to review:**

{{artifact}}

---

## V-02 — Output Format: Strict Markdown Table

**Variation axis**: Output format — all review entries rendered as a single markdown table with enforced column headers
**Hypothesis**: A mandatory table format makes C-02 (field completeness) structurally impossible to fail — missing a cell is visually obvious. It also makes C-04 (severity non-uniformity) scannable at a glance. The constraint forces brevity per finding, which may compress nuance but eliminates structural gaps.

---

You are running `org-review` on the artifact provided below.

**Step 1 — Mode Declaration**

State which depth mode is active:
- **Standard** (default): Select reviewers from `.craft/roles/signal/` whose expertise is most relevant to this artifact type. Name the selected roles and your selection rationale in one sentence each.
- **`--depth deep`**: Include every role found in `.craft/roles/signal/`. State the total count before the table.

All roles must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Review Matrix Table**

Produce a single markdown table with these exact columns:

| Role | Findings | Severity | Recommendation | Verify Question |

Rules:
- One row per reviewer. No empty cells. No merged cells.
- **Role**: the role name exactly as it appears in the `.craft/roles/signal/` filename (e.g., `pm`, `architect`, `inertia-advocate`).
- **Findings**: 2–4 sentences from that role's specific orientation. PM findings address decision/inertia/commitment. Architect findings address feasibility/boundary/complexity. Inertia-advocate findings stress-test the null hypothesis. Findings must not echo each other across rows.
- **Severity**: one of HIGH / MEDIUM / LOW. Not every row may share the same level — calibrate to the actual risk each role sees. If all rows show the same severity, re-examine.
- **Recommendation**: one concrete action the artifact author should take, framed from this role's expertise.
- **Verify Question**: one question this reviewer would ask before accepting the artifact. Drawn from the role's `lens.verify` list.

**Step 3 — Simplify Column (append after table)**

After the table, produce a second smaller table:

| Role | Simplify Observation |

One row per reviewer. Apply each role's `lens.simplify` principles to name one thing in the artifact that could be removed, collapsed, or clarified.

**Step 4 — Cross-Role Summary**

Below both tables, write a summary paragraph (5–8 sentences) that:
- Identifies the highest-severity finding across all reviewers
- Names any cross-role conflict (two reviewers recommending incompatible actions)
- States which areas of the artifact are most at risk
- Gives a single overall disposition: **ready** / **conditional** / **blocked**

**Artifact to review:**

{{artifact}}

---

## V-03 — Inertia Framing: Null Hypothesis as Universal Gate

**Variation axis**: Inertia framing — every reviewer (not just the inertia-advocate) must explicitly state their stance on the null hypothesis before giving findings
**Hypothesis**: Requiring all roles to answer "what is the inertia case here and does this artifact defeat it?" before giving role-specific findings forces genuine divergence (C-03): the PM's answer to that question looks different from the architect's answer, which looks different from the inertia-advocate's answer. This prevents echo-chamber convergence by anchoring every review on a shared question that each role answers differently.

---

You are running `org-review` on the artifact provided below.

**The null hypothesis for every review**: the team does nothing. They keep their current workflow. They do not adopt this feature, spec, or proposal. The artifact's job is to defeat this hypothesis. Every reviewer's job is to assess how well it does.

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to identify available reviewers.
- **Standard** (default): Select the 2–3 roles most relevant to the artifact type based on each role's `expertise.relevance` field. State your selection.
- **`--depth deep`**: Use all roles in `.craft/roles/signal/`. State the total count.

All roles must come from `.craft/roles/signal/`.

**Step 2 — Per-Role Review**

For each selected role, structure the review in three parts:

**Part A — Null Hypothesis Stance**
From this role's specific orientation, state: does the artifact defeat the null hypothesis? Answer from the role's frame only:
- PM frame: Is the evidence strong enough to justify building over doing nothing? Is the inertia case named and addressed?
- Architect frame: Is the technical complexity actually justified by the problem? Could the workaround be extended more cheaply?
- Inertia-advocate frame: What is the team doing today, and is this genuinely better?

Each role's Part A answer must be substantively different from the others — they see the null hypothesis from different angles.

**Part B — Role Findings**
2–4 findings from this role's expertise, drawn from its `lens.verify` and `expertise.depth` fields. Do not repeat Part A. Do not echo other roles' framing.

**Part C — Severity + Recommendation**
- **Severity**: HIGH / MEDIUM / LOW for this role's primary finding. Calibrate independently — do not copy another role's severity.
- **Recommendation**: One concrete action, framed from this role's expertise.
- **Verify Question**: One question from this role's `lens.verify` list.

**Step 3 — Null Hypothesis Verdict**

After all reviewer entries, produce a **Null Hypothesis Verdict** section:
- State the overall null hypothesis threat level: HIGH / MEDIUM / LOW
- Name the evidence that defeats the null hypothesis (if present)
- Name the gap that leaves the null hypothesis alive (if present)
- State overall disposition: **defeats null** / **partial** / **does not defeat null**

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Formal Register + Explicit Lifecycle Phases

**Variation axes**: Phrasing register (formal/technical) + lifecycle emphasis (explicit bounded phases)
**Hypothesis**: Formal technical register combined with explicit phase labels (Selection, Review, Synthesis) treats org-review as a bounded operation with observable state transitions. This reduces conversational drift and makes the depth-flag behavior (C-05) explicit at the phase boundary rather than implicit in the reviewer count.

---

You are executing the `org-review` skill. This skill distributes an artifact to a set of organizational reviewers drawn from the role registry at `.craft/roles/signal/`. Each reviewer applies their designated lens — verify, simplify, expertise — and returns a structured finding. The output is a review matrix suitable for decision-making.

**Phase 1: Reviewer Selection**

Input: `.craft/roles/signal/` directory
Depth parameter: `{{depth}}` (values: `standard` | `deep`)

Procedure:
1. Enumerate all role files in `.craft/roles/signal/`.
2. If depth = `standard`: apply the relevance filter — for each role, read its `expertise.relevance` field and select only those roles whose stated relevance matches the artifact type. Minimum selection: 2 roles. Document selection rationale.
3. If depth = `deep`: include all enumerated roles without filtering. Document total count.

Constraint: No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`. If a desired reviewer does not exist in the registry, that reviewer is omitted.

Output: A reviewer manifest listing selected role names, archetypes, and selection basis.

**Phase 2: Review Execution**

For each reviewer in the manifest, execute the following procedure in order:

2a. Load the role file from `.craft/roles/signal/{role}.md`.
2b. Extract: `orientation.frame`, `lens.verify`, `lens.simplify`, `expertise.depth`.
2c. Apply the orientation frame to the artifact. The reviewer's frame is their interpretive filter — it determines which artifact properties are salient. A product-archetype reviewer attends to decision sufficiency. A technical-archetype reviewer attends to boundary correctness. A challenger-archetype reviewer attends to null hypothesis validity.
2d. Generate findings from this frame. Findings must not duplicate the framing of another reviewer. Cross-role finding homogeneity is a defect.
2e. Classify findings by severity using the scale: HIGH (blocks commitment) / MEDIUM (conditions commitment) / LOW (advisory). Severity is a function of the finding's impact on the artifact's primary purpose.
2f. Formulate a recommendation: one concrete, scoped action the artifact author must take.
2g. Formulate a verify question: one question from `lens.verify` that this reviewer would require answered before accepting the artifact.
2h. Apply the simplify lens: name one element the artifact should remove or collapse, drawn from `lens.simplify`.

Output per reviewer:
```
### Reviewer: {role} ({archetype})
**Findings**: {findings — 2-4 sentences, frame-specific}
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: {action}
**Verify Question**: {question}
**Simplify**: {observation}
```

**Phase 3: Synthesis**

After all reviewer entries are complete, execute synthesis:

3a. Identify the highest-severity finding across all reviewers.
3b. Identify any cross-role conflict: two reviewers whose recommendations are incompatible with each other. If a conflict exists, name the roles in tension and state the decision required to resolve it.
3c. Identify areas of reviewer agreement.
3d. Compute overall disposition:
  - `READY`: all critical findings addressed; HIGH findings are zero or resolved
  - `CONDITIONAL`: MEDIUM findings remain; HIGH findings are zero or advisory
  - `BLOCKED`: one or more HIGH findings are unresolved

Output: A synthesis section with conflict map, agreement areas, and disposition.

**Artifact to review:**

{{artifact}}

---

## V-05 — Combination: Parallel Independent Reviews + Structured Prose

**Variation axes**: Role sequence (parallel/blind) + output format (structured prose sections, not table)
**Hypothesis**: Framing each reviewer as operating independently — without access to other reviewers' findings — prevents the most common C-03 failure mode: sequential reviewers reading the first reviewer's framing and echoing it. Structured prose (rather than table or list) gives each reviewer room to develop findings in their own voice, making perspective divergence observable rather than merely asserted.

---

You are running `org-review`. Each reviewer in this org-review has been given only the artifact — they have not seen each other's work. They are operating in parallel, from their own desk, with their own concerns. Your job is to faithfully render what each reviewer would produce independently.

**Setup — Role Registry**

Read `.craft/roles/signal/` to enumerate available reviewers.

Depth mode:
- **Standard**: Select reviewers whose `expertise.relevance` matches the artifact type. You are selecting a focused review panel — pick reviewers who would genuinely care about this artifact's content. State who you selected and why in one sentence per role.
- **`--depth deep`**: Include all roles in `.craft/roles/signal/`. State the count. On a deep run, every desk gets the artifact.

**Review Format**

For each reviewer, produce a self-contained section with this structure:

---
**[Role name] — [Role archetype]**

*Independent review — this reviewer has not seen other reviews.*

[Opening sentence that establishes what this reviewer is looking for, in their own voice and frame. The PM opens with a decision question. The architect opens with a technical boundary question. The inertia-advocate opens with the status-quo case. These opening frames must be substantively different from each other — they cannot all start from the same concern.]

[2–4 findings paragraphs, each grounded in this role's lens. Do not cross-reference or allude to other reviewers' concerns. Stay in this role's frame entirely.]

**Severity**: HIGH / MEDIUM / LOW — with one sentence of justification.

**Recommendation**: One concrete action, in this role's voice.

**Verify Question**: One question this reviewer would ask the artifact's author, drawn from their `lens.verify` list.

**If I could simplify one thing**: One observation from this role's `lens.simplify` principles.

---

[Repeat for each selected reviewer]

**Cross-Role Debrief**

After all independent reviews are complete, produce a debrief section written from a synthesis perspective (not from any individual role):

- **Where reviewers aligned** (same concern, same severity)
- **Where reviewers diverged** (different framing, different severity, different recommendation)
- **Explicit conflict** (if any): two reviewers whose recommendations are incompatible — name the roles, name the tension, name the decision
- **Areas of the artifact not covered** by any reviewer
- **Overall disposition**: ready / conditional / blocked — with the primary reason

The debrief should read as a genuine synthesis, not a repetition of findings. It should add information the individual reviews do not contain.

**Artifact to review:**

{{artifact}}
