---
skill: quest-variate
skill_target: mock-ns
date: 2026-03-15
round: 2
rubric_version: v2
status: VARIATE
---

# Variate: mock-ns (Round 2)

**Skill**: quest-variate
**Target skill**: mock-ns
**Round**: 2
**Date**: 2026-03-15
**Rubric**: quest-rubric-mock-ns-v2-2026-03-15.md

---

## SPREAD-DESIGN PLAN

Round 2 targets the three new aspirational criteria introduced in v2. Round 1 established
reliable coverage of C-01 through C-10 in the best variations (V-01, V-03, V-04 from R1).
Round 2 builds on that foundation and drives C-11, C-12, and C-13 to pass.

**Key v2 gap analysis:**

- **C-11** (flag computed before header): R1 V-03 introduced "Write it now. Do not defer it."
  but did not create a discrete named step with a named variable. The flag was still
  effectively computed inline during Step 6 (write header). C-11 requires the flag to be
  resolved to a named value in a prior step, then referenced by name in the header block.
  Fix: lifecycle-emphasis axis — "Compute FLAG" as its own named step, header references FLAG.

- **C-12** (topic-status exclusion inline with default table): R1 V-01 and V-03 carried
  exclusion language, but in V-01 it was a note below the table, and in V-03 it was a
  separate "Do NOT use" line after the table. C-12 requires the exclusion note to be *inside*
  the table row itself — same visual context as the affirmative defaults. Fix: output-format
  or phrasing-register axis with an inline exclusion column or annotated row.

- **C-13** (warning as lead section with `---` delimiters): R1 V-04 came closest — it
  wrote the warning before the mock body with `---` delimiters. C-13 requires the warning
  to be a *framing section* that establishes epistemological context before content begins.
  "Before the mock body" is necessary but not sufficient; the section framing and `---`
  separation are required. Fix: output-format axis — warning block is Section 1 of the
  artifact body with explicit framing header.

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | lifecycle-emphasis | C-11: flag resolved as named var before header assembly | C-11, C-09 | PASS on C-11 -- flag variable named in step, header references it |
| V-02 | output-format | C-13: warning block as lead section with delimiters | C-13, C-07 | PASS on C-13 -- warning is Section 1 of artifact body, not inline note |
| V-03 | phrasing-register | C-12: inline exclusion row in default table with DO NOT | C-12, C-06 | PASS on C-12 -- exclusion in same table cell as affirmative default |
| V-04 | lifecycle-emphasis + output-format | Combine V-01 flag-first with V-02 warning-led body | C-11, C-13, C-09 | PASS on C-11 + C-13 simultaneously |
| V-05 | phrasing-register + inertia-framing | Combine V-03 exclusion gate with why-framing for C-12 stickiness | C-12, C-07, C-04 | PASS on C-12; C-07 richer because inertia framing explains cost of wrong flag |

---

## V-01 — Flag-First Sequencing

**axis:** lifecycle-emphasis
**hypothesis:** Resolving the flag value into a named variable (FLAG) in a dedicated
procedural step that *completes before the header-assembly step begins* increases C-11
pass rate because the flag is never computed inline during header construction. In R1
V-03, "Write it now" positioned the flag instruction before the header step but did not
produce a named intermediate value -- the model still resolved category-to-flag during
header writing. Naming the output of the flag step (FLAG = {value}) and instructing the
header step to reference FLAG by name breaks the coupling. Failure condition: if C-11
still fails because "Step 3 sets FLAG but Step 4 re-derives it inline" the named variable
framing is insufficient and a harder gate (emit FLAG before header) is needed.

---

You are executing `/mock:ns`.

Generate a mock artifact for a single namespace. Single-pass, no prompts, no coverage
summary table.

**Inputs**
- `{topic}` -- required
- `{namespace}` -- one of: scout | draft | review | flow | trace | prove | listen | program | topic
- `--skill {skill-id}` -- optional; overrides namespace default
- `--tier 1|2|3` -- optional; default 1

---

**Step 1 -- Read TOPICS.md**

Check for `simulations/TOPICS.md`. If found, read the entry for `{topic}`:
- Tier classification (if present; else default to `--tier` value or 1)
- Compliance tags (if present; else none)

Emit one progress line:

```
> TOPICS.md: {found -- topic {topic} registered, tier: {N}, compliance: {none | list} | not found -- proceeding with defaults}
```

**Step 2 -- Select skill**

If `--skill {skill-id}` was provided: use that skill.
Otherwise, use the namespace default:

| Namespace | Default skill | Exclusion note |
|-----------|--------------|----------------|
| scout     | scout-feasibility | |
| draft     | draft-spec | |
| review    | review-design | |
| flow      | flow-resilience | |
| trace     | trace-request | |
| prove     | prove-hypothesis | |
| listen    | listen-support | |
| program   | program-plan | |
| topic     | topic-plan | Do NOT use topic-status -- excluded as meta-structural (reports coverage rather than generating a signal) |

Emit:

```
> Skill: {skill-id} ({selected by --skill flag | namespace default})
```

**Step 3 -- Assign category**

Match `{skill-id}` against the category table:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

If the skill does not appear in any category row, assign HIGH-STRUCTURE and note the assumption.

**Step 4 -- Compute FLAG**

Resolve the flag value *now*, before writing any artifact content. Assign it to FLAG.

```
HIGH-STRUCTURE (non-critical namespace):
  FLAG = none (structural coverage reliable)

HIGH-STRUCTURE (critical namespace: trace-*, scout-feasibility, listen-*):
  FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY:
  FLAG = REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)

MIXED:
  FLAG = REVIEW-FOR-PLAUSIBILITY

Compliance override (if TOPICS.md has compliance tags AND namespace is
scout-compliance or trace-permissions):
  FLAG = REAL-REQUIRED (compliance-sensitive)
```

Emit:

```
> FLAG: {FLAG value}
```

This step is complete when FLAG is emitted. Do not modify FLAG after this point.

**Step 5 -- Declare artifact path**

```
simulations/mock/{topic}-{namespace}-mock-{date}.md
```

The middle segment is `{namespace}` (the namespace argument). The skill-id does NOT
appear in the filename. Date is YYYY-MM-DD.

Emit:

```
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

**Step 6 -- Write header block**

Write the header block. Use FLAG from Step 4 in the Flag field. Do not re-derive it.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category from Step 3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from Step 4}
```

No fields may be omitted. No fields may be reordered. The Flag value is the value
emitted in Step 4, verbatim.

**Step 7 -- Write fidelity warning**

Immediately after the header block, write the category-appropriate fidelity warning.
The complete block for each category:

HIGH-STRUCTURE:
```
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
mechanisms are reliable. Content is synthetically generated but structurally
representative. Adequate for structural planning and coverage orientation at Tier 1.
REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
```

EVIDENCE-HEAVY:
```
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct but
evidentially fabricated. Do not use this output to draw conclusions about {topic}. The
sections are right; the contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.
```

MIXED:
```
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
mechanisms) are reliable. Specific claims (competitor names, market data, research
findings) may be partially accurate or partially fabricated. Review for plausibility
before accepting coverage.
```

**Step 8 -- Write mock body**

Generate the mock body following the *exact golden structure* of `{skill-id}`:

- Use section headings specific to `{skill-id}` (not generic headings)
- Reproduce every required structural element: tables where the skill produces tables,
  gate lines where the skill produces verdicts, role cards where the skill uses roles,
  named-output lists where the skill produces those
- Place enforcement mechanisms in the positions the skill places them
- Fill with synthetic but structurally representative content

A reader familiar with `{skill-id}` must be able to identify which skill was mocked
from the structure alone.

**Step 9 -- Write next-step line**

Last line of the artifact:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session to regenerate a thin namespace.

**Step 10 -- Write file**

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 -- Warning-Led Body

**axis:** output-format
**hypothesis:** Structuring the artifact so the fidelity warning block is a formal
lead *section* of the artifact body -- delimited by `---` on both sides, appearing
before any skill-specific content -- increases C-13 pass rate and eliminates C-07
partial scores. R1 V-04 wrote the warning before the mock body with `---` delimiters
but framed it as "write this before the mock body" (an instruction about position,
not a structural property). C-13 requires the warning to be an organizing concept:
Section 1 of the artifact, establishing what can and cannot be trusted before the
reader encounters any content. Making the warning a named section (FIDELITY CONTEXT)
forces the delimiter structure and prevents the warning from migrating into the body or
being compressed to a single line. Failure condition: if the section header for
FIDELITY CONTEXT is omitted and the delimiter structure collapses, C-13 still fails
despite correct intent.

---

You are executing `/mock:ns`. Generate a single-namespace mock artifact.
Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional),
`--tier 1|2|3` (default 1).

---

**Setup**

Read `simulations/TOPICS.md`. Extract tier and compliance tags for `{topic}` if found.
Emit: `> TOPICS.md: {found -- tier: {N}, compliance: {none|list} | not found -- defaults apply}`.

Resolve skill: use `--skill {skill-id}` if provided, otherwise the namespace default:

```
scout    -> scout-feasibility
draft    -> draft-spec
review   -> review-design
flow     -> flow-resilience
trace    -> trace-request
prove    -> prove-hypothesis
listen   -> listen-support
program  -> program-plan
topic    -> topic-plan  [NOT topic-status -- excluded as meta-structural]
```

Classify skill by category:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

Determine flag:

| Category | Namespace type | Flag |
|----------|---------------|------|
| HIGH-STRUCTURE | non-critical | `none (structural coverage reliable)` |
| HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | any | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | any | `REVIEW-FOR-PLAUSIBILITY` |
| Compliance override | scout-compliance or trace-permissions, compliance tags active | `REAL-REQUIRED (compliance-sensitive)` |

Artifact path: `simulations/mock/{topic}-{namespace}-mock-{date}.md`
(`{namespace}` segment -- not `{skill-id}` -- in the filename).

---

**Artifact structure**

The artifact has three sections in this order:

1. MOCK ARTIFACT header block
2. FIDELITY CONTEXT section (fidelity warning)
3. MOCK BODY section (skill-specific content)

**Section 1 -- MOCK ARTIFACT header block**

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Date: {date}
Status: MOCK (awaiting review)
Flag: {flag}
```

All seven fields required. No omissions. No reordering.

**Section 2 -- FIDELITY CONTEXT**

This section establishes what can and cannot be trusted before the reader encounters
any skill content. It is the first section of the artifact body, separated from the
header and from the mock body by `---` delimiters.

```
---
## FIDELITY CONTEXT

{Write the complete fidelity warning for the assigned category:}

[If EVIDENCE-HEAVY:]
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct but
evidentially fabricated. Do not use this output to draw conclusions about {topic}. The
sections are right; the contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.

[If MIXED:]
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
mechanisms) are reliable. Specific claims (competitor names, market data, research
findings) may be partially accurate (well-known facts) or partially fabricated (recent,
proprietary, or domain-specific claims). Review for plausibility before accepting
coverage.

[If HIGH-STRUCTURE:]
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
mechanisms are reliable. Content is synthetically generated but structurally
representative. Adequate for structural planning and coverage orientation at Tier 1.
REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---
```

Write this section in full. Do not truncate the warning. Do not move it after the mock
body.

**Section 3 -- MOCK BODY**

After the FIDELITY CONTEXT section, generate the skill-specific mock content.

Follow the golden structural pattern of `{skill-id}` exactly:
- Use `{skill-id}`-specific section headings (not generic ones like "Overview" or "Findings")
- Reproduce every required structural element: tables, gate lines, verdicts, role cards,
  named-output lists, numeric rubrics
- Populate with synthetic but plausible content (realistic column names, representative
  row counts, values that fit the topic context)

A reader who has run `{skill-id}` before must recognize the structure.

**Closing line**

Last line of the artifact:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if invoked from within a `/mock:review` session to regenerate a thin namespace.

**Write file**

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit:

```
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- Inline Exclusion Row

**axis:** phrasing-register
**hypothesis:** Embedding the topic-status exclusion directly in the default-skill table
as a third column -- "Exclusion note" -- increases C-12 pass rate because the exclusion
appears in the same visual and cognitive context as the affirmative default. In R1, V-01
placed the exclusion as a paragraph below the table ("Note: topic-status is excluded..."),
and V-03 placed it as a separate "Do NOT use topic-status" line after the table. Both
keep the exclusion in proximity but not in-line. C-12 requires the exclusion language to
be in the same section as the default table -- inline is stronger than a footnote because
it cannot be skipped during a fast scan. The DO NOT phrasing ("Do NOT use topic-status")
is preserved from R1 V-03 because it was identified as the minimum acceptable strength
per the rubric's own pass condition. Failure condition: if the third column is omitted in
model output (table rendered without exclusion column), C-12 still fails because the
exclusion is absent from the inline context.

---

Execute `/mock:ns`.
Accept: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional),
`--tier 1|2|3` (optional, default 1).

**DO NOT SKIP ANY STEP.**

---

**Step 1. Read TOPICS.md.**

Look for `simulations/TOPICS.md`. Read tier and compliance tags for `{topic}` if found.
Emit one line: `> TOPICS.md: {result}`.

---

**Step 2. Select the skill.**

Use `--skill {skill-id}` if provided.
If not provided, select from the default table below. The table has three columns. Read
all three before selecting.

| Namespace | Default skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility | |
| draft     | draft-spec | |
| review    | review-design | |
| flow      | flow-resilience | |
| trace     | trace-request | |
| prove     | prove-hypothesis | |
| listen    | listen-support | |
| program   | program-plan | |
| topic     | topic-plan | Do NOT use topic-status. It is excluded as meta-structural: it reports on existing signal coverage rather than generating a new signal, so it cannot advance topic readiness. |

The Exclusion column contains hard constraints. Any value in that column overrides the
default.

Emit: `> Skill: {skill-id} ({--skill flag | namespace default})`

---

**Step 3. Assign the category.**

Match `{skill-id}` against the category table:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | everything else |

---

**Step 4. Compute the flag.**

Write the FLAG value now. Do not defer. Do not compute it again during header assembly.

| Category | Namespace type | FLAG |
|----------|---------------|------|
| HIGH-STRUCTURE | non-critical | `none (structural coverage reliable)` |
| HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | any | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | any | `REVIEW-FOR-PLAUSIBILITY` |

Compliance override: if TOPICS.md shows compliance tags AND namespace is `scout-compliance`
or `trace-permissions`: `REAL-REQUIRED (compliance-sensitive)`.

Emit: `> FLAG: {FLAG value}`

---

**Step 5. Declare the artifact path.**

```
simulations/mock/{topic}-{namespace}-mock-{date}.md
```

`{namespace}` = the namespace argument. NOT `{skill-id}`. Date = YYYY-MM-DD.
Emit: `> Artifact path: {path}`

---

**Step 6. Write the header block.**

Write these seven lines in this order. Include all seven. The Flag value is the FLAG
emitted in Step 4 -- copy it exactly, do not rederive.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from Step 4}
```

---

**Step 7. Write the fidelity warning.**

Write the complete warning for `{category}`:

HIGH-STRUCTURE:
```
NOTE: HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms are
reliable. Content is synthetically generated but structurally representative.
Adequate for Tier 1 structural planning. REAL-REQUIRED at Tier 2+ for critical
namespaces (trace, scout-feasibility, listen).
```

EVIDENCE-HEAVY:
```
WARNING: EVIDENCE-HEAVY mock. Content is structurally correct but evidentially
fabricated. Do not use for evidence-based decisions about {topic}. Real {skill-id}
run required.
```

MIXED:
```
CAUTION: MIXED mock. Tables and gates are reliable. Specific claims may be fabricated.
Review for plausibility before accepting coverage.
```

---

**Step 8. Write the mock body.**

Generate the body using the golden structure of `{skill-id}`.
Use skill-specific section headings. Include every required table, gate, verdict, or
role card. Fill with synthetic but structurally sound content.
Do NOT write generic prose where the skill produces structured output.

---

**Step 9. Write the next-step line.**

Last line of the artifact, always:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

**Step 10. Write the file.**

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-04 (Combined) -- Flag-First + Warning-Led Body

**axes:** lifecycle-emphasis + output-format
**hypothesis:** Combining V-01's named FLAG variable (resolved before header assembly)
with V-02's FIDELITY CONTEXT lead section (delimited, before mock body) targets C-11
and C-13 simultaneously, without adding competing complexity. The two changes operate
at different points in the procedure: FLAG computation happens in setup (before the
artifact begins); FIDELITY CONTEXT positioning happens in artifact structure (first
body section). They do not interfere. The combination predicts: C-11 passes because
FLAG is named and emitted before the header step; C-13 passes because FIDELITY CONTEXT
is the structural lead with `---` delimiters; C-07 passes because the full warning text
is required in FIDELITY CONTEXT; C-09 passes because the FLAG step's critical-namespace
branch includes the Tier 2+ qualifier. Failure condition: if the model collapses the
FLAG emit and the header into a single step (treating "emit FLAG" as equivalent to
"write the Flag: field"), C-11 will still fail. The named variable must survive as a
distinct procedural output.

---

You are executing `/mock:ns`. Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional),
`--tier 1|2|3` (default 1).

---

### SETUP PHASE

**S-1 -- Read TOPICS.md**

Check `simulations/TOPICS.md`. If found, read: tier for `{topic}`, compliance tags.
Emit: `> TOPICS.md: {found -- topic {topic}, tier: {N}, compliance: {none|list} | not found -- defaults apply}`.

**S-2 -- Select skill**

Use `--skill {skill-id}` if provided. Otherwise use the namespace default:

| Namespace | Default skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility | |
| draft     | draft-spec | |
| review    | review-design | |
| flow      | flow-resilience | |
| trace     | trace-request | |
| prove     | prove-hypothesis | |
| listen    | listen-support | |
| program   | program-plan | |
| topic     | topic-plan | Do NOT use topic-status -- excluded as meta-structural |

Emit: `> Skill: {skill-id} ({source})`

**S-3 -- Assign category**

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

**S-4 -- Compute FLAG**

Resolve FLAG to a concrete value in this step. The header-assembly step (A-1) will
copy FLAG verbatim -- it will not compute it.

```
If HIGH-STRUCTURE AND namespace NOT in {trace-*, scout-feasibility, listen-*}:
  FLAG = none (structural coverage reliable)

If HIGH-STRUCTURE AND namespace in {trace-*, scout-feasibility, listen-*}:
  FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

If EVIDENCE-HEAVY:
  FLAG = REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)

If MIXED:
  FLAG = REVIEW-FOR-PLAUSIBILITY

Compliance override (TOPICS.md has compliance tags AND namespace is
scout-compliance or trace-permissions):
  FLAG = REAL-REQUIRED (compliance-sensitive)
```

Emit: `> FLAG: {FLAG value}`

FLAG is now resolved. Do not re-evaluate or modify it after this emit.

**S-5 -- Declare artifact path**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

Use `{namespace}` (the argument). Not `{skill-id}`. Date = YYYY-MM-DD.
Emit: `> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

### ARTIFACT PHASE

The artifact has three sections, in order: HEADER, FIDELITY CONTEXT, MOCK BODY.

**A-1 -- HEADER**

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4}
```

Copy FLAG from S-4 verbatim. Do not rederive.

**A-2 -- FIDELITY CONTEXT section**

This is the first section of the artifact body. It frames what can be trusted and what
cannot, before the reader encounters any skill-specific content.

```
---
## FIDELITY CONTEXT

[Write the complete warning for the category assigned in S-3:]

HIGH-STRUCTURE:
NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
mechanisms are reliable. Content is synthetically generated but structurally
representative. Adequate for structural planning and coverage orientation at Tier 1.
REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

EVIDENCE-HEAVY:
WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally correct
but evidentially fabricated. Do not use this output to draw conclusions about {topic}.
The sections are right; the contents are invented. A real {skill-id} run is required
before any evidence-based decision can be made from this namespace.

MIXED:
CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
mechanisms) are reliable. Specific claims (competitor names, market data, research
findings) may be partially accurate or partially fabricated. Review for plausibility
before accepting coverage.

---
```

Write the complete warning text. Do not truncate. Do not move this section after A-3.

**A-3 -- MOCK BODY**

Generate the skill-specific content after the FIDELITY CONTEXT section.

- Use section headings specific to `{skill-id}` (not generic headings)
- Reproduce every required structural element the skill produces: tables, gate lines,
  verdicts, role cards, named-output lists, numeric rubrics
- Fill with synthetic but plausible content

A reader who has run `{skill-id}` before must recognize the structure without being
told the skill name.

**A-4 -- Closing line**

Last line of the artifact:

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

### WRITE

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-05 (Combined) -- Inline Exclusion + Inertia Framing

**axes:** phrasing-register + inertia-framing
**hypothesis:** Combining V-03's inline exclusion table (DO NOT use topic-status, with
reason) with inertia framing in the fidelity warning increases C-12 stickiness and
makes C-07 semantically richer. The inertia framing mechanism: each category's warning
names the cost of treating the mock as coverage without a real run -- specifically what
decision would be made incorrectly if the artifact were trusted beyond its category
grade. For EVIDENCE-HEAVY, the cost is accepting fabricated evidence as real; for MIXED,
the cost is treating uncertain specific claims as confirmed; for HIGH-STRUCTURE, the
cost is skipping a real run at Tier 2+ when structure-only coverage is insufficient for
commit-level decisions. This framing targets a residual C-07 partial pattern from R1:
the HIGH-STRUCTURE warning was sometimes truncated to "adequate for Tier 1" without the
"REAL-REQUIRED at Tier 2+" qualifier. Adding the inertia cost makes the Tier 2+
escalation feel like a natural consequence of the evidence gap, not an appended rule.
For C-12: the inertia framing extends V-03's inline exclusion by explaining *why*
topic-status cannot advance readiness (its cost when substituted for topic-plan is
zero new signal, which defeats the purpose of running /mock:ns). Failure condition: if
the inertia framing lengthens the warning to the point that the model truncates it,
C-07 partial scores worsen instead of improving.

---

You are executing `/mock:ns`. Generate a mock artifact for a single namespace.
Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}` (optional),
`--tier 1|2|3` (default 1).

---

**Step 1. Read TOPICS.md.**

Check `simulations/TOPICS.md`. Read tier and compliance tags for `{topic}` if found.

Emit: `> TOPICS.md: {found -- topic {topic}, tier: {N}, compliance: {none|list} | not found -- defaults apply}`

---

**Step 2. Select the skill.**

Use `--skill {skill-id}` if provided.
If not provided, read the full default table below, including the Exclusion column:

| Namespace | Default skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility | |
| draft     | draft-spec | |
| review    | review-design | |
| flow      | flow-resilience | |
| trace     | trace-request | |
| prove     | prove-hypothesis | |
| listen    | listen-support | |
| program   | program-plan | |
| topic     | topic-plan | Do NOT use topic-status. Inertia cost: topic-status reports existing coverage -- it produces zero new signal. Substituting topic-status for topic-plan means the mock run generates no forward readiness signal, defeating the purpose of /mock:ns. |

The Exclusion column is a hard constraint. A value in that column means the listed skill
cannot be the default under any circumstance, regardless of topic context.

Emit: `> Skill: {skill-id} ({source})`

---

**Step 3. Assign the category.**

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

---

**Step 4. Compute FLAG.**

Compute now. Do not defer.

| Category | Namespace type | FLAG |
|----------|---------------|------|
| HIGH-STRUCTURE | non-critical | `none (structural coverage reliable)` |
| HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | any | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | any | `REVIEW-FOR-PLAUSIBILITY` |
| Compliance override | scout-compliance or trace-permissions + compliance tags active | `REAL-REQUIRED (compliance-sensitive)` |

Emit: `> FLAG: {FLAG value}`

---

**Step 5. Declare artifact path.**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

`{namespace}` in the filename. Not `{skill-id}`. Date = YYYY-MM-DD.
Emit: `> Artifact path: {path}`

---

**Step 6. Write the header block.**

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from Step 4}
```

Copy FLAG from Step 4 verbatim.

---

**Step 7. Write the fidelity warning.**

Write the complete warning for the category. Each warning names what is reliable,
what is not, and the cost of treating the mock as coverage beyond its grade.

HIGH-STRUCTURE:
```
---
NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative.

What you can trust: section headings, table structures, gate positions, verdict format.
What you cannot trust: specific values, thresholds, named entities -- these are synthetic.

Adequate for Tier 1 structural planning and coverage orientation. Inertia risk at
Tier 2+: structural coverage alone is insufficient for commit-level decisions on
critical namespaces (trace, scout-feasibility, listen). Accepting this mock at Tier 2+
without a real run means making a commit decision without actual evidence -- structure
shows the shape of the answer; a real run shows the answer.
REAL-REQUIRED at Tier 2+ for critical namespaces.
---
```

EVIDENCE-HEAVY:
```
---
WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
evidentially fabricated.

What you can trust: section headings, required sections, output format, structural
completeness of the mock.
What you cannot trust: any specific claim, finding, data point, or conclusion -- these
are invented.

Inertia risk: treating this mock as evidence coverage means making decisions from
fabricated data. The cost is not just uncertainty -- it is false confidence. A real
{skill-id} run is required before any evidence-based decision can be made from this
namespace.
---
```

MIXED:
```
---
CAUTION: This is a MIXED mock. Some elements are reliable; others are not.

What you can trust: structural elements -- tables, gates, enforcement mechanisms,
output format.
What you cannot trust: specific claims -- competitor names, market figures, research
findings, domain-specific assertions. These may be partially accurate (well-known
facts) or partially fabricated (recent, proprietary, or domain-specific).

Inertia risk: accepting specific claims without review means treating partially
fabricated content as confirmed. Review all specific claims for plausibility before
accepting this namespace as coverage.
---
```

---

**Step 8. Write the mock body.**

Generate skill-specific content following the golden structure of `{skill-id}`:

- `{skill-id}`-specific section headings
- Every required structural element: tables, gates, verdicts, role cards, named outputs
- Synthetic but plausible content

A reader familiar with `{skill-id}` must recognize the structure from the output alone.

---

**Step 9. Write the next-step line.**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if invoked from within a `/mock:review` session.

---

**Step 10. Write the file.**

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## Variation Map Summary

| V | Axes | C-11 | C-12 | C-13 | What changed | Hypothesis |
|---|------|------|------|------|--------------|------------|
| V-01 | lifecycle-emphasis | target | carry | carry | FLAG computed as named step (S-4), emitted before header; header copies FLAG verbatim | C-11 passes -- flag value resolved at lowest cognitive load point before header assembly |
| V-02 | output-format | carry | carry | target | Fidelity warning is FIDELITY CONTEXT section with `---` delimiters, positioned as Section 2 of artifact (before mock body) | C-13 passes -- warning is a structural lead section, not inline note |
| V-03 | phrasing-register | carry | target | carry | Default skill table has inline Exclusion column; topic-status row contains DO NOT + reason | C-12 passes -- exclusion language in same table cell as affirmative default |
| V-04 | lifecycle-emphasis + output-format | target | carry | target | V-01 FLAG-first sequencing combined with V-02 FIDELITY CONTEXT lead section | C-11 + C-13 both pass; C-09 carried by FLAG step's critical-namespace branch |
| V-05 | phrasing-register + inertia-framing | carry | target | carry | V-03 inline exclusion combined with inertia-cost language in fidelity warning and exclusion row | C-12 passes with stronger framing; C-07 HIGH-STRUCTURE warning no longer truncated (cost of Tier 2+ inertia explicit) |

**Top combination candidate for Round 3:**
V-01 (FLAG-first) + V-02 (FIDELITY CONTEXT) + V-03 (inline exclusion table) as a
three-axis combination -- if all three single-axis variations pass their target criteria
independently, the combination should deliver C-11 + C-12 + C-13 together. The risk is
prompt length: V-03's three-column table adds width, V-02's FIDELITY CONTEXT adds
section depth, and V-01's dedicated FLAG step adds a setup step. If the combination
exceeds comfortable prompt length, V-04 (already two-axis) can be extended with V-03's
table instead of creating a new variation.
