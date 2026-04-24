---
skill: quest-variate
skill_target: mock-ns
date: 2026-03-15
round: 3
rubric_version: v3
status: VARIATE
---

# Variate: mock-ns (Round 3)

**Skill**: quest-variate
**Target skill**: mock-ns
**Round**: 3
**Date**: 2026-03-15
**Rubric**: quest-rubric-mock-ns-v3-2026-03-15.md

---

## SPREAD-DESIGN PLAN

Round 3 targets C-14 and C-15, the two new aspirational criteria in v3. The foundation
from R2's best performers is stable and carried forward in all variations:

- C-09: tier-conditional flag (from R2 V-01 onward)
- C-10: dedicated TOPICS.md emit line (from R1 V-01 onward)
- C-11: FLAG as named step before header assembly (from R2 V-01 onward)
- C-12: topic-status exclusion inline with default table (from R2 V-03 onward)
- C-13: FIDELITY CONTEXT as lead section with `---` delimiters (from R2 V-04)
- C-15: Exclusion as dedicated structural table column (from R2 V-01 onward)

**Key v3 gap analysis:**

- **C-14** (dual-point FLAG immutability): R2 V-04 passes cleanly: "FLAG is now resolved.
  Do not re-evaluate or modify it after this emit." (compute site) + "Copy FLAG from S-4
  verbatim. Do not rederive." (header site). R2 V-03 has the compute-site prohibition
  phrased as a forward reference ("Do not compute it again during header assembly") rather
  than an at-site finality declaration -- the rubric requires prohibition language *at both
  sites*, which means each site declares its own constraint, not one site pointing ahead.
  R2 V-01 passes C-14 but fails C-13 (no FIDELITY CONTEXT section), scoring 6/7. R2 V-02
  fails C-11 (no named FLAG variable) and therefore auto-fails C-14. Round 3 builds
  variations where C-14 is satisfied by progressively stronger mechanisms: structural gate
  (V-01), procedural lock block (V-02), MUST NOT modal register (V-03), and combinations.

- **C-15** (structural exclusion column): Already present in R2 V-01, V-03, V-04, V-05
  via three-column Exclusion table. R2 V-02 fails (uses `[NOT topic-status]` bracket
  annotation in prose list). Round 3 carries the three-column table in all variations;
  V-02 adopts it to close the only remaining C-15 gap.

**R3 target: all five variations pass C-14 and C-15 simultaneously, with full C-13
carrythrough. Round 3 is a stability round -- not opening new axes but hardening the dual
criteria and testing three distinct enforcement mechanisms for C-14.**

| Plan | Axis | Target | Hypothesis |
|------|------|--------|------------|
| V-01 | lifecycle-emphasis | C-14 via structural site-boundary gate | Declaring FLAG final at end of compute step + prohibiting rederivation at start of header step creates dual-point enforcement that matches C-14 pass condition exactly |
| V-02 | output-format | C-14 via FLAG RESOLUTION BLOCK with STATUS: LOCKED | Visual lock structure is harder to overlook than inline prose prohibition; also fixes R2 V-02's C-15 gap |
| V-03 | phrasing-register | C-14 via MUST NOT at both sites | Stronger modal register elevates prohibition from advisory to mandatory at both compute and header assembly sites |
| V-04 | lifecycle-emphasis + phrasing-register | C-14 maximum enforcement | Structural gate from V-01 + MUST NOT register from V-03 -- two orthogonal enforcement mechanisms at the same two sites |
| V-05 | output-format + inertia-framing | C-14 via lock block + richer fidelity framing | FLAG RESOLUTION BLOCK from V-02 + inertia-cost language in FIDELITY CONTEXT (extending R2 V-05) |

---

## V-01 -- FLAG Site-Boundary Gate

**axis:** lifecycle-emphasis
**hypothesis:** Declaring FLAG final *at the close of the compute step* (not just
"before header assembly" but as an explicit closing declaration of the compute step
itself) and then prohibiting re-derivation *at the open of the header assembly step*
(not just "copy from Step N" but as the opening rule of that step) creates a structural
gate between the two lifecycle phases. R2 V-01 had both sites but the compute-site
declaration was a trailing statement rather than a closing gate. R2 V-04's compute-site
language ("FLAG is now resolved. Do not re-evaluate or modify it after this emit.") is
close to the gate pattern -- V-01 R3 makes this the close of S-4 rather than a trailing
note. The header step's opening rule ("FLAG was computed in S-4 and is final. Do not
re-derive it here.") frames the prohibition as the entry condition of the step, not an
afterthought. This structural positioning is more resistant to collapse than inline prose.
Predicted: C-14 PASS because both sites have explicit, site-local prohibition language.
C-13 PASS because FIDELITY CONTEXT lead section carried from R2 V-04. C-15 PASS via
three-column table. C-11 PASS via named FLAG step. Failure condition: if the model
merges S-4 and A-1 into a single operation, C-11 and C-14 both fail -- watch for that
collapse pattern in scoring.

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

### SETUP PHASE

**S-1 -- Read TOPICS.md**

Check `simulations/TOPICS.md`. If found, read the entry for `{topic}`: tier
classification (if present; else default to `--tier` value or 1), compliance tags
(if present; else none).

Emit one dedicated progress line:

```
> TOPICS.md: {found -- topic {topic} registered, tier: {N}, compliance: {none | list} | not found -- proceeding with defaults}
```

**S-2 -- Select skill**

Use `--skill {skill-id}` if provided. Otherwise use the namespace default from the
table below. The table has three columns -- read all three before selecting.

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
| topic     | topic-plan | Do NOT use topic-status. Hard exclusion: meta-structural (reports existing coverage rather than generating a new signal; cannot advance topic readiness). |

The Exclusion column contains hard constraints. Any value in that column overrides the
default under all circumstances.

Emit: `> Skill: {skill-id} ({--skill flag | namespace default})`

**S-3 -- Assign category**

Match `{skill-id}` against the category table:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

If the skill does not appear in any row, assign HIGH-STRUCTURE and note the assumption.

**S-4 -- Compute FLAG**

This step resolves FLAG to a named concrete value. It ends by declaring FLAG final.
The header assembly step (A-1) will copy FLAG from this step -- it will not compute it.

```
If HIGH-STRUCTURE AND namespace NOT in {trace-*, scout-feasibility, listen-*}:
  FLAG = none (structural coverage reliable)

If HIGH-STRUCTURE AND namespace IN {trace-*, scout-feasibility, listen-*}:
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

**Step S-4 is now complete. FLAG is final. Do not modify FLAG after this emit.
Do not re-evaluate or re-derive FLAG in any subsequent step.**

**S-5 -- Declare artifact path**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

Use `{namespace}` (the argument). NOT `{skill-id}`. Date = YYYY-MM-DD.

Emit: `> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

### ARTIFACT PHASE

The artifact has three sections in this order: HEADER, FIDELITY CONTEXT, MOCK BODY.

**A-1 -- HEADER**

FLAG was computed and finalized in S-4. Do not re-derive it here. The first rule of
this step is: copy FLAG from S-4 verbatim.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 -- copy verbatim, do not rederive}
```

No fields may be omitted. No fields may be reordered.

**A-2 -- FIDELITY CONTEXT section**

This is the first section of the artifact body. It frames what can and cannot be
trusted before the reader encounters any skill-specific content. Delimited by `---`
on both sides; the `---` delimiters appear before the section heading and after the
warning block.

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

Write the complete warning text. Do not truncate. Do not position this section after
the mock body.

**A-3 -- MOCK BODY**

Generate the skill-specific content after the FIDELITY CONTEXT section.

- Use section headings specific to `{skill-id}` (not generic headings)
- Reproduce every required structural element: tables, gate lines, verdicts, role
  cards, named-output lists, numeric rubrics
- Fill with synthetic but structurally representative content

A reader who has run `{skill-id}` before must recognize the structure.

**A-4 -- Closing line**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

### WRITE

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-02 -- FLAG RESOLUTION BLOCK

**axis:** output-format
**hypothesis:** Rendering the FLAG computation as a delimited procedural block --
explicitly opened, resolved, and closed with a STATUS: LOCKED marker -- makes FLAG
immutability structurally visible rather than prose-embedded. The block boundary
establishes a hard structural fence: the FLAG value inside the block cannot be
changed after the "STATUS: LOCKED" line closes it, and the header assembly step
references "the FLAG RESOLUTION BLOCK" as an external artifact rather than running
inline logic. This format change targets C-14's mechanism: the rubric requires
explicit prohibition language at both sites; the RESOLUTION BLOCK provides the
compute-site prohibition structurally (STATUS: LOCKED closes the block), and the
header step provides the consumption-site prohibition explicitly ("Do not compute a
new flag value. Copy the locked value from the FLAG RESOLUTION BLOCK verbatim.").
Secondary target: this variation also fixes the C-15 gap in R2 V-02, which used a
bracket annotation `[NOT topic-status]` in a prose list; this variation uses the
same three-column Exclusion table as R2 V-01 and V-04. Failure condition: if the
model renders the block as prose rather than a structured block, the visual lock is
lost and C-14 depends on whether the inline prohibition text is still present.

---

You are executing `/mock:ns`. Generate a single-namespace mock artifact.
Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}`
(optional), `--tier 1|2|3` (default 1).

---

**Setup**

Read `simulations/TOPICS.md`. Extract tier and compliance tags for `{topic}` if found.
Emit one dedicated line:
`> TOPICS.md: {found -- topic {topic}, tier: {N}, compliance: {none|list} | not found -- defaults apply}`

Resolve skill: use `--skill {skill-id}` if provided, otherwise the namespace default:

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
| topic     | topic-plan | Do NOT use topic-status -- excluded as meta-structural (reports coverage; generates no new signal; cannot advance readiness) |

Emit: `> Skill: {skill-id} ({source})`

Classify skill by category:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

---

**FLAG RESOLUTION BLOCK**

Perform the following resolution inside the block. Once the block closes, FLAG is
final and MUST NOT be recomputed anywhere in this run.

```
--- FLAG RESOLUTION ---
Inputs:
  category: {category from classification step}
  namespace: {namespace}
  compliance: {tags from TOPICS.md, or none}

Resolution:
  If HIGH-STRUCTURE AND namespace NOT in {trace-*, scout-feasibility, listen-*}:
    FLAG = none (structural coverage reliable)

  If HIGH-STRUCTURE AND namespace IN {trace-*, scout-feasibility, listen-*}:
    FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

  If EVIDENCE-HEAVY:
    FLAG = REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)

  If MIXED:
    FLAG = REVIEW-FOR-PLAUSIBILITY

  Compliance override (compliance tags active AND namespace is
  scout-compliance or trace-permissions):
    FLAG = REAL-REQUIRED (compliance-sensitive)

Result: FLAG = {resolved value}
STATUS: LOCKED -- do not modify FLAG after this line.
--- END FLAG RESOLUTION ---
```

Emit: `> FLAG: {FLAG value}`

---

**Artifact path**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

(`{namespace}` segment -- NOT `{skill-id}`; date = YYYY-MM-DD)

Emit: `> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

**Artifact structure**

The artifact has three ordered sections: HEADER, FIDELITY CONTEXT, MOCK BODY.

**Section 1 -- MOCK ARTIFACT header**

Retrieve FLAG from the FLAG RESOLUTION BLOCK above. Do not compute a new flag value
here. Do not re-derive it. Copy the locked value verbatim from the FLAG RESOLUTION
BLOCK.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG -- copy from FLAG RESOLUTION BLOCK, do not rederive}
```

All fields required. No omissions. No reordering.

**Section 2 -- FIDELITY CONTEXT**

This section is the first body section of the artifact. It appears immediately after
the MOCK ARTIFACT header block and before any skill-specific content. Delimited by
`---` on both sides.

```
---
## FIDELITY CONTEXT

HIGH-STRUCTURE:
NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative.
Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
namespaces (trace, scout-feasibility, listen).

EVIDENCE-HEAVY:
WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
evidentially fabricated. Do not use for evidence-based decisions about {topic}.
Sections are right; contents are invented. A real {skill-id} run is required before
any evidence-based decision can be made from this namespace.

MIXED:
CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
may be partially accurate or partially fabricated. Review for plausibility before
accepting coverage.

---
```

Write the complete warning for the assigned category. Do not truncate. Do not
position this section after the mock body.

**Section 3 -- MOCK BODY**

Generate skill-specific content following the golden structure of `{skill-id}`:

- Use `{skill-id}`-specific section headings (not generic headings)
- Reproduce every required structural element: tables, gates, verdicts, role cards,
  named-output lists
- Synthetic but structurally representative content

A reader familiar with `{skill-id}` must recognize the structure from the output alone.

**Closing line**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

**Write file**

Write the complete artifact to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-03 -- MUST NOT Prohibition Register

**axis:** phrasing-register
**hypothesis:** Upgrading the prohibition modal register from advisory ("do not
rederive") to mandatory ("MUST NOT rederive") at both the compute site and the header
assembly site tests whether stronger modal phrasing meaningfully increases C-14 pass
rate. The rubric pass condition uses "do not modify FLAG after this point" and "copy
it exactly, do not rederive" as exemplars -- these are advisory imperatives. MUST NOT
is a stronger modal: it marks the action as prohibited rather than discouraged.
This variation applies MUST NOT at both C-14 sites: "FLAG is final. MUST NOT modify
after this emit. MUST NOT re-derive FLAG in any subsequent step." (compute site) and
"MUST NOT re-derive FLAG here. Copy verbatim from the step above." (header site).
The FIDELITY CONTEXT lead section (C-13) and three-column Exclusion table (C-15) are
carried forward. The exclusion row itself also adopts MUST NOT ("MUST NOT use
topic-status") to maintain register consistency and test C-15 stability under the
same phrasing pattern. Failure condition: if MUST NOT triggers refusal or if the
model treats it as unusual syntax and skips the step, a softer register re-run is
needed.

---

Execute `/mock:ns`.
Accept: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}`
(optional), `--tier 1|2|3` (optional, default 1).

**DO NOT SKIP ANY STEP.**

---

**Step 1. Read TOPICS.md.**

Look for `simulations/TOPICS.md`. Read tier and compliance tags for `{topic}` if
found. Emit one dedicated line: `> TOPICS.md: {result}`.

---

**Step 2. Select the skill.**

Use `--skill {skill-id}` if provided.
If not provided, read the full default table below, including the Exclusion column,
before selecting.

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
| topic     | topic-plan | MUST NOT use topic-status. Hard exclusion: meta-structural (reports existing coverage; generates no new signal). MUST NOT be used as default under any circumstance. |

The Exclusion column contains hard constraints that override the default.

Emit: `> Skill: {skill-id} ({--skill flag | namespace default})`

---

**Step 3. Assign the category.**

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

---

**Step 4. Compute FLAG.**

This is a named, discrete step. Compute FLAG now. Use the result in Step 6.

| Category | Namespace type | FLAG |
|----------|---------------|------|
| HIGH-STRUCTURE | non-critical | `none (structural coverage reliable)` |
| HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| EVIDENCE-HEAVY | any | `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` |
| MIXED | any | `REVIEW-FOR-PLAUSIBILITY` |
| Compliance override | scout-compliance or trace-permissions + compliance tags | `REAL-REQUIRED (compliance-sensitive)` |

Emit: `> FLAG: {FLAG value}`

**FLAG is final. MUST NOT modify FLAG after this emit.
MUST NOT re-derive FLAG in any subsequent step, including header assembly.**

---

**Step 5. Declare artifact path.**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

`{namespace}` in filename. MUST NOT use `{skill-id}` in filename. Date = YYYY-MM-DD.
Emit: `> Artifact path: {path}`

---

**Step 6. Write the header block.**

FLAG was computed in Step 4 and is final. MUST NOT re-derive FLAG here.
Copy it verbatim from Step 4. Write these seven lines in this order. MUST NOT omit
any field.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category from Step 3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from Step 4 -- copy verbatim, MUST NOT rederive}
```

---

**Step 7. Write the FIDELITY CONTEXT section.**

This is the first section of the artifact body, before any mock body content.
Delimited by `---` on both sides.

```
---
## FIDELITY CONTEXT

HIGH-STRUCTURE:
NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative.
Adequate for Tier 1 structural planning. REAL-REQUIRED at Tier 2+ for critical
namespaces (trace, scout-feasibility, listen).

EVIDENCE-HEAVY:
WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
evidentially fabricated. MUST NOT use for evidence-based decisions about {topic}.
Sections are right; contents are invented. Real {skill-id} run required.

MIXED:
CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
be fabricated. Review for plausibility before accepting coverage.

---
```

Write the complete warning for the assigned category. MUST NOT truncate.
MUST NOT position this section after the mock body.

---

**Step 8. Write the mock body.**

Generate the body using the golden structure of `{skill-id}`.
Use skill-specific headings. Include every required table, gate, verdict, role card.
MUST NOT write generic prose where the skill produces structured output.

---

**Step 9. Write the next-step line.**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

**Step 10. Write the file.**

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-04 (Combined) -- Structural Gate + MUST NOT

**axes:** lifecycle-emphasis + phrasing-register
**hypothesis:** Combining V-01's structural site-boundary gate (FLAG declared final at
the *close* of the compute step; re-derivation prohibited at the *open* of the header
step) with V-03's MUST NOT modal register creates the maximum C-14 enforcement possible
in a single prompt. The two axes operate at different layers: lifecycle-emphasis
controls *where* in the procedure the prohibition appears (step boundaries are the
highest-salience positions); phrasing-register controls *how strong* the prohibition
reads at each site. Together they produce a pattern where: (a) the compute step ends
with a named gate declaration using MUST NOT; (b) the header step opens with the same
MUST NOT prohibition that names the source step explicitly. The FIDELITY CONTEXT lead
section (C-13) and three-column Exclusion table (C-15) are carried forward from R2 V-04.
This variation predicts: C-14 PASS at maximum confidence -- dual MUST NOT gates, one
closing compute and one opening header. C-11, C-13, C-15 stable carry. Failure
condition: if the procedural density of step boundaries + MUST NOT language causes the
model to truncate earlier sections (C-10, S-1 emit), the gain in C-14 comes at the cost
of setup step reliability.

---

You are executing `/mock:ns`. Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}`
(optional), `--tier 1|2|3` (default 1).

---

### SETUP PHASE

**S-1 -- Read TOPICS.md**

Check `simulations/TOPICS.md`. If found, read: tier for `{topic}`, compliance tags.
Emit one dedicated line:
`> TOPICS.md: {found -- topic {topic}, tier: {N}, compliance: {none|list} | not found -- defaults apply}`

**S-2 -- Select skill**

Use `--skill {skill-id}` if provided. Otherwise use the namespace default. Read all
three columns of the table before selecting.

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
| topic     | topic-plan | MUST NOT use topic-status -- hard exclusion: meta-structural. Reports coverage; generates no new signal. MUST NOT be used as topic default. |

The Exclusion column is a hard constraint.

Emit: `> Skill: {skill-id} ({source})`

**S-3 -- Assign category**

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

**S-4 -- Compute FLAG**

Resolve FLAG in this step. This step ends with a gate declaration.

```
If HIGH-STRUCTURE AND namespace NOT in {trace-*, scout-feasibility, listen-*}:
  FLAG = none (structural coverage reliable)

If HIGH-STRUCTURE AND namespace IN {trace-*, scout-feasibility, listen-*}:
  FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

If EVIDENCE-HEAVY:
  FLAG = REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)

If MIXED:
  FLAG = REVIEW-FOR-PLAUSIBILITY

Compliance override (compliance tags active AND namespace is
scout-compliance or trace-permissions):
  FLAG = REAL-REQUIRED (compliance-sensitive)
```

Emit: `> FLAG: {FLAG value}`

**-- S-4 GATE -- FLAG IS FINAL. MUST NOT modify FLAG after this emit.
MUST NOT re-evaluate or re-derive FLAG in any step that follows. --**

**S-5 -- Declare artifact path**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

Use `{namespace}`. MUST NOT use `{skill-id}`. Date = YYYY-MM-DD.
Emit: `> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

### ARTIFACT PHASE

The artifact has three sections in this order: HEADER, FIDELITY CONTEXT, MOCK BODY.

**A-1 -- HEADER**

**-- A-1 GATE -- MUST NOT re-derive FLAG here. FLAG was finalized in S-4.
Copy it verbatim from the S-4 emit. --**

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 -- copy verbatim, MUST NOT rederive}
```

No fields may be omitted. No fields may be reordered.

**A-2 -- FIDELITY CONTEXT section**

This is the first section of the artifact body, establishing what can and cannot be
trusted before any skill-specific content is encountered. Delimited by `---` on both
sides.

```
---
## FIDELITY CONTEXT

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

Write the complete warning. MUST NOT truncate. MUST NOT move this section after A-3.

**A-3 -- MOCK BODY**

Generate skill-specific content after the FIDELITY CONTEXT section.

- `{skill-id}`-specific section headings (not generic)
- Every required structural element: tables, gates, verdicts, role cards, named outputs
- Synthetic but structurally representative content

A reader who has run `{skill-id}` before must recognize the structure.

**A-4 -- Closing line**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

### WRITE

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## V-05 (Combined) -- FLAG RESOLUTION BLOCK + FIDELITY CONTEXT + Inertia Framing

**axes:** output-format + inertia-framing
**hypothesis:** R2 V-05 established that inertia framing (naming the cost of treating
the mock as real coverage) strengthens C-07 and makes the Tier 2+ escalation feel like
a natural consequence rather than an appended rule. V-05 R3 extends this by combining
three elements: V-02's FLAG RESOLUTION BLOCK (structural lock for C-14), R2 V-04's
FIDELITY CONTEXT lead section (C-13), and R2 V-05's inertia-cost language inside both
the fidelity warning and the exclusion row. The inertia framing for the exclusion row
names the cost of substituting topic-status for topic-plan: "zero new signal, zero
readiness advance" -- making the exclusion feel like a cost-consequence rule rather
than a syntactic prohibition. The FIDELITY CONTEXT warnings include the "what you
cannot trust / inertia risk" pattern from R2 V-05's HIGH-STRUCTURE warning, which
showed that naming the cost of a Tier-2+ commit decision without a real run produced
a richer, non-truncated warning. V-05 R3 is therefore the highest-depth variation:
FLAG structurally locked (C-14 via RESOLUTION BLOCK), warning structurally framed
(C-13 via FIDELITY CONTEXT), exclusion structurally positioned (C-15 via Exclusion
column) and semantically grounded (inertia-cost). Failure condition: prompt length.
If the inertia framing causes the model to front-load the fidelity section and truncate
the mock body (C-03), the depth of C-07 is purchased at the cost of C-03 quality.

---

You are executing `/mock:ns`. Generate a mock artifact for a single namespace.
Single-pass. No prompts. No coverage summary table.

**Inputs**: `{topic}` (required), `{namespace}` (required), `--skill {skill-id}`
(optional), `--tier 1|2|3` (default 1).

---

**Setup**

Read `simulations/TOPICS.md`. Extract tier and compliance tags for `{topic}` if found.

Emit one dedicated line:
`> TOPICS.md: {found -- topic {topic}, tier: {N}, compliance: {none|list} | not found -- defaults apply}`

Resolve skill: use `--skill {skill-id}` if provided, otherwise the namespace default:

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
| topic     | topic-plan | Do NOT use topic-status. Inertia cost: topic-status reports existing signal coverage -- it produces zero new signal and cannot advance topic readiness. Substituting topic-status for topic-plan means the /mock:ns run generates no forward readiness signal, defeating its purpose. |

Emit: `> Skill: {skill-id} ({source})`

Classify skill by category:

| Category | Skills |
|----------|--------|
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, prove-analysis, prove-synthesize, prove-publish, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |
| HIGH-STRUCTURE | all other skills |

---

**FLAG RESOLUTION BLOCK**

Resolve FLAG inside this block. The block closes with STATUS: LOCKED. After the block
closes, FLAG is final and MUST NOT be recomputed anywhere in this run.

```
--- FLAG RESOLUTION ---
Inputs:
  category: {category from classification}
  namespace: {namespace}
  compliance: {tags from TOPICS.md, or none}

Resolution:
  If HIGH-STRUCTURE AND namespace NOT in {trace-*, scout-feasibility, listen-*}:
    FLAG = none (structural coverage reliable)

  If HIGH-STRUCTURE AND namespace IN {trace-*, scout-feasibility, listen-*}:
    FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

  If EVIDENCE-HEAVY:
    FLAG = REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)

  If MIXED:
    FLAG = REVIEW-FOR-PLAUSIBILITY

  Compliance override (compliance tags active AND namespace is
  scout-compliance or trace-permissions):
    FLAG = REAL-REQUIRED (compliance-sensitive)

Result: FLAG = {resolved value}
STATUS: LOCKED -- do not modify FLAG after this line.
--- END FLAG RESOLUTION ---
```

Emit: `> FLAG: {FLAG value}`

---

**Artifact path**

`simulations/mock/{topic}-{namespace}-mock-{date}.md`

(`{namespace}` segment -- NOT `{skill-id}`; date = YYYY-MM-DD)

Emit: `> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

**Artifact structure**

Three ordered sections: HEADER, FIDELITY CONTEXT, MOCK BODY.

**Section 1 -- MOCK ARTIFACT header**

Retrieve FLAG from the FLAG RESOLUTION BLOCK above. Do not compute a new flag value
here. Do not re-derive it. Copy the locked value verbatim.

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG -- copy from FLAG RESOLUTION BLOCK, do not rederive}
```

All fields required. No omissions. No reordering.

**Section 2 -- FIDELITY CONTEXT**

This section frames reliability before the reader encounters any mock content. It is
the first body section of the artifact, delimited by `---` on both sides. Each warning
names: what can be trusted, what cannot be trusted, and the inertia risk of treating
the mock as coverage beyond its category grade.

```
---
## FIDELITY CONTEXT

HIGH-STRUCTURE:
NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
are reliable. Content is synthetically generated but structurally representative.

What you can trust: section headings, table structures, gate positions, verdict format.
What you cannot trust: specific values, thresholds, named entities -- these are
synthetic.

Adequate for Tier 1 structural planning. Inertia risk at Tier 2+: structural coverage
alone is insufficient for commit-level decisions on critical namespaces (trace,
scout-feasibility, listen). Accepting this mock at Tier 2+ without a real run means
making a commit decision on structure without evidence -- structure shows the shape of
the answer; a real run shows the answer. REAL-REQUIRED at Tier 2+ for critical
namespaces.

EVIDENCE-HEAVY:
WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
evidentially fabricated.

What you can trust: section headings, required sections, output format, structural
completeness.
What you cannot trust: any specific claim, finding, data point, or conclusion --
these are invented.

Inertia risk: treating this mock as evidence coverage means making decisions from
fabricated data. The cost is not uncertainty -- it is false confidence. A real
{skill-id} run is required before any evidence-based decision can be made.

MIXED:
CAUTION: This is a MIXED mock. Some elements are reliable; others are not.

What you can trust: structural elements -- tables, gates, enforcement mechanisms.
What you cannot trust: specific claims -- competitor names, market figures, research
findings. These may be partially accurate (well-known facts) or partially fabricated
(recent or domain-specific).

Inertia risk: accepting specific claims without review means treating partially
fabricated content as confirmed. Review all specific claims for plausibility before
accepting this namespace as coverage.

---
```

Write the complete warning for the assigned category. Do not truncate. Do not
position this section after the mock body.

**Section 3 -- MOCK BODY**

Generate skill-specific content following the golden structure of `{skill-id}`:

- `{skill-id}`-specific section headings
- Every required structural element: tables, gates, verdicts, role cards, named outputs
- Synthetic but plausible content

A reader familiar with `{skill-id}` must recognize the structure from the output alone.

**Closing line**

```
Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

Omit only if called from within a `/mock:review` session.

---

**Write file**

Write to `simulations/mock/{topic}-{namespace}-mock-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`

---

## Variation Map Summary

| V | Axes | C-14 mechanism | C-15 | C-13 | What changed from R2 |
|---|------|----------------|------|------|----------------------|
| V-01 | lifecycle-emphasis | Structural site-boundary gate: S-4 closes with "FLAG IS FINAL"; A-1 opens with "FLAG was finalized in S-4. Do not re-derive it here." | 3-col Exclusion table | FIDELITY CONTEXT section | R2 V-01 lacked C-13; R3 V-01 adds it. Compute-site declaration now closes S-4 rather than being a trailing note |
| V-02 | output-format | FLAG RESOLUTION BLOCK with STATUS: LOCKED close; header step says "Do not compute a new flag value. Copy from FLAG RESOLUTION BLOCK verbatim." | 3-col Exclusion table | FIDELITY CONTEXT section | R2 V-02 failed C-11 and C-15; R3 V-02 fixes both and adds RESOLUTION BLOCK for C-14 |
| V-03 | phrasing-register | MUST NOT at compute site: "MUST NOT modify after this emit. MUST NOT re-derive in any subsequent step." MUST NOT at header site: "MUST NOT re-derive FLAG here." | 3-col Exclusion table with MUST NOT | FIDELITY CONTEXT section | Upgrades R2 V-03 compute-site prohibition from advisory to mandatory at both sites |
| V-04 | lifecycle-emphasis + phrasing-register | Structural gate from V-01 + MUST NOT from V-03 at both sites: S-4 GATE + A-1 GATE, both using MUST NOT | 3-col Exclusion table with MUST NOT | FIDELITY CONTEXT section | Combines V-01 and V-03; highest-enforcement C-14 variation |
| V-05 | output-format + inertia-framing | FLAG RESOLUTION BLOCK from V-02 + inertia-cost language in exclusion row and fidelity warnings | 3-col Exclusion table with inertia cost | FIDELITY CONTEXT with inertia framing | Extends R2 V-05 inertia framing into the RESOLUTION BLOCK format |

**Top combination candidate for Round 4:**
V-04 structure (lifecycle gates + MUST NOT) merged with V-05 inertia framing in
FIDELITY CONTEXT -- the full three-axis combination. If V-01, V-03, and V-05 each
independently pass C-14, a round-4 variation that combines all three axes should
produce the most stable and richly-grounded prompt. The risk is length: V-04 is
already the longest single variation, and V-05's inertia framing adds depth to
every fidelity section. A round-4 editorial pass trimming redundancy without losing
the structural gates would be the natural next step.
