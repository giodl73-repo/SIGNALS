
# Variate: mock-ns (Round 1)

**Skill**: quest-variate
**Target skill**: mock-ns
**Round**: 1
**Date**: 2026-03-15
**Rubric**: quest-rubric-mock-ns-v1-2026-03-15.md

---

## SPREAD-DESIGN PLAN

Single-axis variation for Round 1. Three axes selected.

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | Lifecycle emphasis — explicit phases | C-10 weak in baseline (no TOPICS.md narration) | C-10, C-06 | PASS on C-10 |
| V-02 | Lifecycle emphasis — compressed/output-forward | C-03 risk: compressed setup may skip skill-structure detail | C-03, C-07 | PARTIAL on C-10 |
| V-03 | Phrasing register — imperative commands | C-04 failure (Flag absent): imperative sequence prevents omission | C-01, C-04, C-05 | PASS on C-04 |
| V-04 | Output format — fidelity-warning leads body | C-07 weak when warning is afterthought; leading it locks the structure | C-07, C-02 | PASS on C-07 |
| V-05 | Path construction — filename declared first | C-05 failure (skill-id in path): declaring path before header prevents the trap | C-05, C-01 | PASS on C-05 |

---

## V-01 — Lifecycle Explicit

**Axis**: Lifecycle emphasis — all four phases labeled and fully narrated
**Hypothesis**: Explicit phase boundaries and detailed setup narration ensure TOPICS.md consultation is visible (C-10) and representative skill default is unambiguous (C-06). Phases reduce the chance of skipping Flag or fidelity warning.

---

You are executing `/mock:ns`.

Generate a mock artifact for a single namespace. Single-pass, no prompts, no coverage summary table.

**Inputs**
- `{topic}` — required
- `{namespace}` — one of: scout | draft | review | flow | trace | prove | listen | program | topic
- `--skill {skill-id}` — optional; overrides the namespace default
- `--tier 1|2|3` — optional; default 1

---

### PHASE 1 — SETUP

**Step 1.1 — Read TOPICS.md**

Check for `simulations/TOPICS.md` in the workspace.

- If found: read the topic entry for `{topic}`. Extract: tier classification (if present), compliance tags (if present), any prior namespace signals listed.
- If not found or topic not registered: proceed with defaults. Do not prompt the user.

Emit a single progress line:

```
> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {none|list} | not found — proceeding with defaults}
```

**Step 1.2 — Select skill**

Determine which skill to mock:

- If `--skill {skill-id}` was provided: use that skill.
- Otherwise, use the namespace default from this table:

| Namespace | Default skill |
|-----------|--------------|
| scout | scout-feasibility |
| draft | draft-spec |
| review | review-design |
| flow | flow-resilience |
| trace | trace-request |
| prove | prove-hypothesis |
| listen | listen-support |
| program | program-plan |
| topic | topic-plan |

Note: `topic-status` is excluded as the default for the `topic` namespace because it is meta-structural (reports on existing coverage rather than generating a signal). Use `topic-plan` instead.

Emit a progress line:

```
> Skill: {skill-id} ({selected by --skill flag | namespace default})
```

**Step 1.3 — Assign category**

Look up the skill in the category table:

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market, scout-positioning, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-request, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger, flow-integration, program-plan, topic-plan, topic-story, topic-echo, topic-report |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

If the skill does not appear in any row, assign HIGH-STRUCTURE and note the assumption.

**Step 1.4 — Determine flag**

Assign the flag value from the category and tier:

- **HIGH-STRUCTURE, non-critical namespace**: `none (structural coverage reliable)`
- **HIGH-STRUCTURE, critical namespace** (trace-*, scout-feasibility, listen-*), **any tier**: `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)`
- **EVIDENCE-HEAVY**: `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)`
- **MIXED**: `REVIEW-FOR-PLAUSIBILITY`

If compliance tags were found in TOPICS.md for this topic and the namespace is `scout-compliance` or `trace-permissions`: override flag to `REAL-REQUIRED (compliance-sensitive)`.

**Step 1.5 — Construct artifact path**

```
simulations/mock/{topic}-{namespace}-mock-{date}.md
```

The `{namespace}` segment is the namespace argument, not the skill-id. Date is today's date in YYYY-MM-DD format.

Emit:

```
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

### PHASE 2 — EXECUTE

Write the mock artifact. Begin with the MOCK ARTIFACT header block immediately after any frontmatter. The header block must be exactly this structure, in this order:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag value from Step 1.4}
```

No fields may be omitted. No fields may be reordered.

**Fidelity warning**

Immediately after the header block, write the category-appropriate fidelity warning:

For HIGH-STRUCTURE:
```
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement mechanisms are
reliable. Content is synthetically generated but structurally representative. Adequate for
structural planning and coverage orientation at Tier 1. REAL-REQUIRED at Tier 2+ for critical
namespaces (trace, scout-feasibility, listen).
```

For EVIDENCE-HEAVY:
```
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct but
evidentially fabricated. Do not use this output to draw conclusions about {topic}. The
sections are right; the contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.
```

For MIXED:
```
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement mechanisms)
are reliable. Specific claims (competitor names, market data, research findings) may be
partially accurate or partially fabricated. Review for plausibility before accepting coverage.
```

**Mock body**

Generate the mock body following the **exact golden structure** of `{skill-id}`. This means:

- Use the correct section headings for that skill (not generic headings)
- Include every required structural element: tables where the skill produces tables, gate lines where the skill produces a verdict, role cards where the skill uses roles, named-output lists where the skill produces those
- Place enforcement mechanisms (gates, verdicts, confidence levels, severity labels) in the positions the skill places them
- Generate synthetic but structurally representative content — realistic column names, representative row counts, plausible values

A reader familiar with the real `{skill-id}` output must be able to identify which skill was mocked from the structure alone. Generic prose without skill-specific structure fails this standard.

---

### PHASE 3 — FINDINGS

The mock artifact is the output. No additional interpretation.

Final line of the artifact:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit this line only if the skill was called from within an active `/mock:review` session to regenerate a thin namespace.

---

### PHASE 4 — AMEND

Not applicable for mock-ns. Regenerate with `--skill {different-skill-id}` if the output is structurally thin for the intended purpose.

---

### WRITE

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.

Emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 — Compressed / Output-Forward

**Axis**: Lifecycle emphasis — setup compressed into a single lookup block; output generation leads
**Hypothesis**: Removing phase narration and going straight to output construction reduces cognitive overhead and keeps the model focused on C-03 (skill-structure fidelity). Risk: C-10 (TOPICS.md visibility) may be PARTIAL if the setup check is too brief.

---

You are executing `/mock:ns`. Inputs: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional), `--tier 1|2|3` (default 1).

**Quick setup (single pass before writing)**

1. Check `simulations/TOPICS.md` for `{topic}`. Read tier and compliance tags if present.
2. Skill: use `--skill` if provided, else the default for `{namespace}`:
   scout=scout-feasibility, draft=draft-spec, review=review-design, flow=flow-resilience,
   trace=trace-request, prove=prove-hypothesis, listen=listen-support, program=program-plan,
   topic=topic-plan.
3. Category:
   - EVIDENCE-HEAVY if skill is in: prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption
   - MIXED if skill is in: scout-competitors, prove-hypothesis, review-customers, review-users
   - HIGH-STRUCTURE for all others
4. Flag:
   - HIGH-STRUCTURE: `none (structural coverage reliable)` — add `; REAL-REQUIRED at Tier 2+` if the skill is trace-*, scout-feasibility, or listen-*
   - EVIDENCE-HEAVY: `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)`
   - MIXED: `REVIEW-FOR-PLAUSIBILITY`
5. Path: `simulations/mock/{topic}-{namespace}-mock-{date}.md` — use namespace, not skill-id.

Emit:
```
> Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {N})...
```

**Write the artifact**

Open with the MOCK ARTIFACT header block (no fields omitted, in this exact order):

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag}
```

Then write the fidelity warning:

- HIGH-STRUCTURE: `NOTE: HIGH-STRUCTURE mock. Structure and enforcement mechanisms are reliable. Content synthetically generated. Adequate for Tier 1 structural planning.`
- EVIDENCE-HEAVY: `WARNING: EVIDENCE-HEAVY mock. Content is structurally correct but evidentially fabricated. Real {skill-id} run required for any evidence-based decision.`
- MIXED: `CAUTION: MIXED mock. Tables and gates are reliable. Specific claims may be fabricated. Review for plausibility.`

Then write the mock body. Follow the golden structural pattern for `{skill-id}` exactly:

- Use `{skill-id}`-specific section headings (not generic ones)
- Reproduce every required table, gate line, verdict, role card, or named-output list the skill produces
- Fill with synthetic but structurally sound content

End the artifact with:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md` and emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 — Imperative Register

**Axis**: Phrasing register — every instruction is a direct command verb; no descriptive framing
**Hypothesis**: Short imperative sentences prevent omissions. The Flag line failure (C-04) happens when the model skips it because it is described as optional or buried in prose. Making every step a command verb forces sequential completion.

---

Execute `/mock:ns`. Accept: `{topic}`, `{namespace}`, optional `--skill {skill-id}`, optional `--tier 1|2|3` (default 1).

**DO THIS IN ORDER. DO NOT SKIP A STEP.**

**Step 1. Read TOPICS.md.**
Look for `simulations/TOPICS.md`. Read tier and compliance tags for `{topic}` if found. Emit one line: `> TOPICS.md: {result}`.

**Step 2. Select the skill.**
Use `--skill {skill-id}` if provided.
If not provided, select from:

| Namespace | Skill |
|-----------|-------|
| scout | scout-feasibility |
| draft | draft-spec |
| review | review-design |
| flow | flow-resilience |
| trace | trace-request |
| prove | prove-hypothesis |
| listen | listen-support |
| program | program-plan |
| topic | topic-plan |

Do NOT use topic-status as the topic default. topic-status is excluded.

**Step 3. Assign the category.**
Match `{skill-id}` against the table:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | everything else |

**Step 4. Write the Flag line value.**
Write it now. Do not defer it.

- HIGH-STRUCTURE (not critical): `none (structural coverage reliable)`
- HIGH-STRUCTURE (critical: trace-*, scout-feasibility, listen-*): `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)`
- EVIDENCE-HEAVY: `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)`
- MIXED: `REVIEW-FOR-PLAUSIBILITY`
- Override: if TOPICS.md shows compliance tags AND namespace is scout-compliance or trace-permissions: `REAL-REQUIRED (compliance-sensitive)`

**Step 5. Declare the artifact path.**
Write the path before generating any content:
`simulations/mock/{topic}-{namespace}-mock-{date}.md`
Use `{namespace}`, not `{skill-id}`. Use YYYY-MM-DD date. Emit: `> Artifact path: {path}`.

**Step 6. Write the header block.**
Write these six lines in this order. Include all six. Do not skip any.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag from Step 4}
```

**Step 7. Write the fidelity warning.**
Select the warning for `{category}`:

HIGH-STRUCTURE:
```
NOTE: HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms are reliable.
Content is synthetically generated but structurally representative. Adequate for Tier 1
structural planning. REAL-REQUIRED at Tier 2+ for critical namespaces.
```

EVIDENCE-HEAVY:
```
WARNING: EVIDENCE-HEAVY mock. Content is structurally correct but evidentially fabricated.
Do not use for evidence-based decisions about {topic}. Real {skill-id} run required.
```

MIXED:
```
CAUTION: MIXED mock. Tables and gates are reliable. Specific claims may be fabricated.
Review for plausibility before accepting coverage.
```

**Step 8. Write the mock body.**
Generate the body using the golden structure of `{skill-id}`.
Use skill-specific section headings. Include every required table, gate, verdict, or role card.
Fill with synthetic content. Do not write generic prose where the skill produces structured output.

**Step 9. Write the next-step line.**
Last line of the artifact, always:
`Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md`
Omit only if called from within a `/mock:review` session.

**Step 10. Write the file.**
Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-04 — Fidelity-Forward

**Axis**: Output format — fidelity warning block leads the mock body; category is the organizing concept
**Hypothesis**: When fidelity warning is the first thing written after the header, the model locks the category early and cannot drift. C-07 (warning block present) always passes. The warning also primes the correct body structure for the category.

---

You are executing `/mock:ns`. Generate a single-namespace mock artifact. Single-pass. No prompts.

**Inputs**: `{topic}`, `{namespace}`, `--skill {skill-id}` (optional), `--tier 1|2|3` (default 1).

**Setup**

Check `simulations/TOPICS.md`. If found, read: tier, compliance tags, existing signals for `{topic}`. Emit `> TOPICS.md: {result}`.

Resolve the skill to mock:

- `--skill {skill-id}` if provided, else namespace default:
  `scout→scout-feasibility, draft→draft-spec, review→review-design, flow→flow-resilience, trace→trace-request, prove→prove-hypothesis, listen→listen-support, program→program-plan, topic→topic-plan`

Classify the skill:

| Category | When |
|----------|------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

The category drives everything that follows. Lock it before writing.

**Artifact construction**

The artifact path is `simulations/mock/{topic}-{namespace}-mock-{date}.md`. The `{namespace}` segment is the namespace argument. The skill-id does not appear in the filename.

Begin the artifact with the MOCK ARTIFACT header block:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag}
```

Flag values by category:

| Category | Flag |
|----------|------|
| HIGH-STRUCTURE (non-critical) | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | `REVIEW-FOR-PLAUSIBILITY` |
| Compliance override | `REAL-REQUIRED (compliance-sensitive)` — if TOPICS.md has compliance tags and namespace is scout-compliance or trace-permissions |

**Fidelity warning — write this before the mock body**

The category determines the warning. Write the complete block for the assigned category:

If EVIDENCE-HEAVY:
```
---
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct but
evidentially fabricated. Do not use this output to draw conclusions about {topic}. The
sections are right; the contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.
---
```

If MIXED:
```
---
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement mechanisms)
are reliable. Specific claims (competitor names, market data, research findings) may be
partially accurate (well-known facts) or partially fabricated (recent, proprietary, or
domain-specific claims). Review for plausibility before accepting coverage.
---
```

If HIGH-STRUCTURE:
```
---
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative. Adequate
for structural planning and coverage orientation at Tier 1. REAL-REQUIRED at Tier 2+ for
critical namespaces (trace, scout-feasibility, listen).
---
```

**Mock body**

After the fidelity warning, generate the mock body. The body must follow the golden structural pattern of `{skill-id}`:

- Use the section headings specific to `{skill-id}` (not generic headings like "Overview" or "Findings")
- Reproduce every structural element the skill produces: tables, gate lines, verdicts, role cards, named-output lists, numeric rubrics, decision trees
- Populate with synthetic but plausible content — realistic column names, representative rows, values that fit the topic context

The body structure must be recognizable to someone who has run `{skill-id}` before. "Recognizable" means: correct section count, correct element types, correct gate/verdict positions.

**Closing**

Last line of the artifact:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if this skill run was invoked from within a `/mock:review` session to regenerate a thin namespace.

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`. Emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
> Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 — Path-First

**Axis**: Path construction — artifact filename is the first declared output; all other elements derive from it
**Hypothesis**: C-05 failures (skill-id embedded in filename) happen when the filename is constructed late, after the skill-id is already prominent in working memory. Declaring the path first — before the header block — anchors the correct `{namespace}` segment early and prevents skill-id contamination of the path.

---

You are executing `/mock:ns`. Inputs: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional), `--tier 1|2|3` (default 1).

**Declare the artifact path first.**

Before any content generation, construct and emit the artifact path:

```
Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Rules:
- The middle segment is `{namespace}` — the namespace argument you received (scout, draft, review, flow, trace, prove, listen, program, or topic).
- The skill-id does NOT appear in the path. It goes in the header block only.
- Date is YYYY-MM-DD.

Hold this path. Every subsequent reference to the artifact uses this path verbatim.

**Setup**

1. Check `simulations/TOPICS.md`. Read tier and compliance tags for `{topic}` if found. Emit: `> TOPICS.md: {result}`.

2. Resolve skill: use `--skill {skill-id}` if provided. Otherwise use the namespace default:

| Namespace | Default skill |
|-----------|--------------|
| scout | scout-feasibility |
| draft | draft-spec |
| review | review-design |
| flow | flow-resilience |
| trace | trace-request |
| prove | prove-hypothesis |
| listen | listen-support |
| program | program-plan |
| topic | topic-plan |

3. Classify skill:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | everything else |

4. Determine flag:

| Category | Skill type | Flag |
|----------|-----------|------|
| HIGH-STRUCTURE | non-critical | `none (structural coverage reliable)` |
| HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | any | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | any | `REVIEW-FOR-PLAUSIBILITY` |

Compliance override: if TOPICS.md shows compliance tags AND namespace is scout-compliance or trace-permissions: `REAL-REQUIRED (compliance-sensitive)`.

**Write the artifact to the declared path**

Begin with the MOCK ARTIFACT header block (all six fields, in order):

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag}
```

Then write the fidelity warning for the assigned category:

- HIGH-STRUCTURE: `NOTE: HIGH-STRUCTURE mock. Structure and enforcement mechanisms are reliable. Content synthetically generated. Adequate for Tier 1 structural planning. REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).`
- EVIDENCE-HEAVY: `WARNING: EVIDENCE-HEAVY mock. Content is structurally correct but evidentially fabricated. Real {skill-id} run required before any evidence-based decision.`
- MIXED: `CAUTION: MIXED mock. Tables and gates reliable. Specific claims may be fabricated. Review for plausibility.`

Then write the mock body following the golden structure of `{skill-id}`:
- Skill-specific section headings
- All required structural elements (tables, gates, verdicts, role cards, named outputs)
- Synthetic but structurally representative content

Close with:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

(Use the path you declared at the top. Do not reconstruct it.)

Write the artifact. Emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```
