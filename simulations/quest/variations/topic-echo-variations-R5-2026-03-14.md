Here are the 5 complete R5 variations:

---

## R5 Summary

| # | Axis | Target | Key mechanism |
|---|------|--------|---------------|
| **V-01** | Schema name-lock + label parity audit | C-15 | Canonical manifest pre-write; post-write label-only cross-surprise scan |
| **V-02** | Per-surprise Coupled Authority Test | C-16 | After each surprise: stranger-accessibility AND claim-voice tested as a single coupled unit |
| **V-03** | Tabular schema format | C-15 (structural) | Row headers enforce uniform field names by construction — drift impossible |
| **V-04** | V-04(R4) + schema name-lock + Coupled Authority Test | C-15 + C-16 | Minimum addition to proven 100/100 baseline |
| **V-05** | V-05(R4) + schema name-lock + Coupled Authority Test | All criteria | Maximum-mechanism combination |

---

**Design logic:**

**C-15 gap in V-04(R4):** The existing field completion scan checks content population, not field-name identity. An author who writes "Design consequence" instead of "Design impact" passes C-13 but fails C-15. V-01 closes this with a manifest + label-only scan. V-03 tests whether a table format forecloses the problem structurally (row headers can't diverge between columns).

**C-16 gap in V-04(R4):** The per-surprise checks are sequential: stranger → word count → prohibited constructs. C-16 requires both to hold *simultaneously* for the extracted unit. A hedged surprise can pass the structural portability test while failing as an institutional claim. V-02's Coupled Authority Test collapses both checks into one pass — both tests A and B must hold for the same extracted block.

**Key risk for V-03:** The tabular format is the structural C-15 bet, but C-10's "Why passive observation missed this" field is information-dense — table cells may be too constrained for the mechanism explanation, which could degrade C-10 while achieving C-15.

**Predicted winner:** V-04(R5). It is the minimum addition to a proven baseline, with both new mechanisms orienting toward the same newcomer-stranger reader as the existing four.
not N/A]` labels and field completion scan both target field *population*, not field-*name identity*. If an author writes "Design consequence" instead of "Design impact" across all surprises — populating every field — C-13 PASS is unaffected but C-15 fails. The schema name-lock mechanism targets this gap: it publishes the canonical label set once before writing and audits labels specifically (not content) in a cross-surprise scan.

**Key structural bet in V-02**: V-04(R4)'s per-surprise checks apply tests sequentially (read as stranger → count words → check prohibited constructs). C-16 requires the *coupling*: a surprise that is stranger-accessible but stated in hedged voice is not an institutional claim. A surprise that uses claim voice but requires project context is not a portable claim. The Coupled Authority Test makes this joint requirement explicit at the per-surprise level.

**Key structural bet in V-03**: Table row headers are schema field names. In a row-based table, the field label appears once (as a row header) and applies identically to every column (every surprise). An author cannot rename "Design impact" in Surprise 2 without renaming it for all surprises, because it is a row header. C-15 would be earned without an explicit audit step. The risk: table cells constrain word count; the 120-word per-column cap is harder to enforce in prose cells, and the "Why passive observation missed this" field may be too information-dense for a table cell.

**V-04 prediction**: 100/100 + C-15 PASS + C-16 PASS. Both mechanisms are additive to the V-04(R4) structure without conflicting with existing rules.

**V-05 prediction**: 100/100 + C-15 PASS + C-16 PASS. Seven mechanisms, same single reader. No friction predicted.

---

## V-01 — Single axis: Schema name-lock + label parity audit (C-15)

**Axis**: Before writing, declare a canonical field-name manifest with exact labels. After writing all surprises, run a label parity audit that reads only the bold field labels (not content) across all surprises in sequence and confirms character-identical match to the manifest.

**Hypothesis**: C-15 requires field names to be identical across all surprises — not just populated (C-13), but named identically. V-04(R4)'s inline template and completion scan target content population. A schema name-lock step (explicit canonical manifest pre-write) plus a label-only cross-surprise audit (reading only bold labels, not content) addresses field-name identity as a separate verification step. If V-04(R4)'s template already prevents label drift implicitly (same template = same names), the audit confirms it at zero cost. If an author renames a field while populating all content, the audit catches it where C-13's completion scan would not.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — fully documented, uniformly named, no field left empty, no field label changed.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once — before they start their own investigation of the same path.**

They need: what surprised the team, why it mattered for the design, and what they would have missed without active signal-gathering. Every rule below serves this reader.

---

### Schema manifest — declare before writing

Before writing any surprise, write the following into the artifact:

```markdown
## Schema manifest

Canonical field labels applied to every surprise in this document (exact — do not rename):
- **Source**
- **Expected**
- **Found**
- **Design impact**
- **Why passive observation missed this**

All fields required. None optional. None N/A. Applied in this order, with these exact labels, to every surprise.
```

This manifest is a contract. Any reader scanning "Design impact" across the full surprise set will find that label in the same position every time. No surprise in this document may use a synonym, abbreviation, or alternate label for any field.

---

### Four rules that govern this echo

**Rule 1 — The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering — relying only on initial strategy, standard planning, and normal development feedback — have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

A surprise a passive team would find anyway is planning documentation, not institutional memory.

**Rule 2 — Claim-only voice**

Every surprise is stated as a claim the author stands behind. Prohibited from all entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

The stranger needs claims. If you cannot assert it, drop it.

**Rule 3 — 120 words per surprise body**

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. Under 800 words total. If the stranger cannot absorb a surprise in a single reading, it has not been synthesized.

**Rule 4 — Every field populated**

Every schema field is required for every surprise. No field may be absent, blank, or marked N/A. If you cannot populate a field, the surprise is not ready to write. Confirm it further or drop it.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise:
1. Apply Rule 1: could a passive team have discovered this?
2. Ask: can the stranger understand this without reading the source?

Record both verdicts. Do not write yet.

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without reading the source artifact.
5. Keep 3–6 surprises.

---

### Step 3 — Name for the stranger

Assign a specific named label before writing. Content-specific, memorable, self-explanatory without project context. Not "Finding 3." Something specific to what this investigation found, that the stranger will remember after reading once.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Apply the schema manifest exactly. Use the five canonical field labels, in order, for every surprise — no variation:

```markdown
## {Named Label}

**Source** [required — not N/A]:
{namespace/skill where this surfaced}

**Expected** [required — not N/A]:
{stated as a claim: "We assumed X"}

**Found** [required — not N/A]:
{stated as a claim: "X is Y / X is false / the constraint is Z"}

**Design impact** [required — not N/A]:
{stated as a claim: "This changes / confirms / invalidates..."}

**Why passive observation missed this** [required — not N/A]:
{what specific signal or method surfaced it, and why planning or normal feedback would not have — explained for the stranger, not the team}
```

After writing each surprise: read it as the stranger. Count words from `**Source**` through end of `**Why passive observation missed this**`. If > 120: cut until you have a claim, not a description. Check for prohibited constructs. Verify all five fields are populated. Move to the next only when all checks pass.

---

### Step 5 — Label parity audit

After writing all surprises, run the cross-surprise label parity audit.

Read only the bold-formatted field labels (not the content) in each surprise, in sequence:

1. List the five canonical labels from the schema manifest: Source / Expected / Found / Design impact / Why passive observation missed this.
2. For each canonical label, read the corresponding bold label in every surprise in sequence.
3. Confirm: every surprise uses that exact canonical label — same spelling, same capitalization, same order.

Any label that deviates from the canonical manifest — renamed, abbreviated, reordered, or missing — must be corrected to match the manifest before publishing.

This audit checks names only. It is separate from the field completion scan, which checks content.

---

### Step 6 — Field completion scan

After the label audit, scan field-by-field for content completeness:

For each canonical field (Source / Expected / Found / Design impact / Why passive observation missed this):
- Read that field for every surprise in sequence.
- Verify it is populated with substantive content — not N/A, not blank, not "see above."

Any field that fails: fill it or drop the surprise.

---

### Step 7 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest appears in the artifact before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order — no renamed, abbreviated, reordered, or missing labels
- [ ] A reader scanning "Design impact" across all surprises finds that label in the same position every time

**Stranger utility:**
- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] Every "Why passive observation missed this" is explained without team-internal shorthand

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo's institutional value depends on its structure being readable across time and context. Uniform field labels mean a future reader can scan any field across the full set without re-learning the schema.

---

## V-02 — Single axis: Per-surprise Coupled Authority Test (C-16)

**Axis**: After writing each surprise, extract it as a standalone unit and run a Coupled Authority Test — a single pass that tests stranger-accessibility AND claim-voice simultaneously for that unit. Both must hold together; passing one while failing the other fails the test.

**Hypothesis**: C-16 requires each surprise to individually carry both stranger-reader authority and no-hedging authority as a coupled property. V-04(R4)'s per-surprise checks apply tests sequentially (read as stranger → count words → check prohibited constructs). C-16 requires the *coupling*: a surprise that is stranger-accessible but stated in hedged voice is not an institutional claim. The Coupled Authority Test collapses the two checks into one: the author extracts the surprise as a unit, then asks both A and B about that unit in a single pass. The coupling is the mechanism. Risk: this structurally overlaps with V-05(R4)'s Check A + Check B. The distinction is that C-16 explicitly tests the coupling — both properties must hold for the same extracted unit simultaneously, not as independent document-level sweeps.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of institutional claims — each one authoritative in voice and complete in context, for any reader, in any setting, without preparation.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once.** Individual surprises will also be extracted — cited in design briefs, onboarding documents, and postmortems by people who will never see the full echo.

Every surprise must function as an authoritative institutional claim when extracted: complete in context, direct in voice, actionable without surrounding information. A surprise that requires context to be understood is not portable. A surprise that hedges its finding is not a claim.

---

### Four rules that govern this echo

**Rule 1 — The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering — relying only on initial strategy, standard planning, and normal development feedback — have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

**Rule 2 — Claim-only voice**

Every surprise is stated as a claim. Prohibited from all entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

**Rule 3 — 120 words per surprise body + 800 total**

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. Under 800 words total.

**Rule 4 — Every field populated**

Every schema field is required for every surprise. No field may be absent, blank, or marked N/A. If you cannot populate a field, drop the surprise or confirm it further.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise:
1. Apply Rule 1: could a passive team have discovered this?
2. Ask: can the stranger understand this without reading the source? Can it stand alone when extracted?

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without reading the source artifact.
5. Keep 3–6 surprises.

---

### Step 3 — Name for the stranger

Assign a specific named label before writing. Content-specific, memorable, self-explanatory without project context. The stranger will encounter this name out of context — it must work alone.

---

### Step 4 — Write each surprise, then run the Coupled Authority Test

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise uses this schema — applied identically across every entry. Each field is required:

```markdown
## {Named Label}

**Source** [required — not N/A]:
{namespace/skill where this surfaced}

**Expected** [required — not N/A]:
{stated as a claim: "We assumed X"}

**Found** [required — not N/A]:
{stated as a claim: "X is Y / X is false / the constraint is Z"}

**Design impact** [required — not N/A]:
{stated as a claim: "This changes / confirms / invalidates..."}

**Why passive observation missed this** [required — not N/A]:
{what specific signal or method surfaced it, and why planning would not have — explained without project-internal shorthand}
```

**After writing each surprise — before the next — run the Coupled Authority Test:**

> Extract this surprise as a standalone block. A reader who has never seen this project reads only this section.
>
> **Test A — Institutional claim**: Is every sentence in this surprise a direct statement of fact or consequence? Zero hedge constructs. Zero uncertainty language. The reader receives a claim, not an observation.
>
> **Test B — Stranger authority**: Does this extracted unit — standing alone — communicate all three of the following without any outside context?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> **The test passes only when A and B hold simultaneously for the extracted unit.**
>
> A stranger-accessible but hedged surprise FAILS — it is a portable observation, not a portable claim.
> A claim-voiced but context-dependent surprise FAILS — it is a claim the stranger cannot use.
> Both must hold together for the same extracted unit.

If either test fails: revise until both pass for the extracted unit. Count words from `**Source**` through end of `**Why passive observation missed this**`. If > 120: cut. Write the next surprise only after the Coupled Authority Test passes.

---

### Step 5 — Field completion scan

After all surprises are written, scan field by field:

For each field name (Source / Expected / Found / Design impact / Why passive observation missed this): read that field for every surprise in sequence. Verify: populated, substantive, not N/A. Any failure: fill or drop.

---

### Step 6 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank
- [ ] Schema is identical across all surprises — no missing or extra fields

**Coupled authority:**
- [ ] Every surprise passes the Coupled Authority Test — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes Test B structurally while remaining hedged in voice

**Stranger utility:**
- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] "Why passive observation missed this" is explained without team-internal shorthand

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

An institutional claim is both authoritative and portable. The Coupled Authority Test confirms both hold together — for each surprise, as a unit.

---

## V-03 — Single axis: Tabular schema format (C-15 via structural enforcement)

**Axis**: Surprises are written as a Markdown table where each column is a surprise and each row is a schema field. Field names appear as row headers — applied uniformly to every column by construction.

**Hypothesis**: C-15 requires field names to be identical across all surprises. In a column-per-surprise table, field names are row headers — they appear once and apply to every column simultaneously. An author cannot rename "Design impact" in Surprise 2 without renaming it for all surprises, because it is a row header, not a field within a surprise. C-15 is earned structurally, without an explicit audit step. Secondary test: does constrained cell width increase compression pressure (C-11) and reduce hedging opportunity (C-12)? Risk: table cells may be too short to populate the "Why passive observation missed this" field with the mechanism explanation required for C-10. If C-10 degrades, the format fails on a more foundational criterion than C-15.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — one table, each column a complete institutional claim.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once — before they start their own investigation of the same path.**

They need: what surprised the team, why it mattered for the design, and what they would have missed without active signal-gathering. Every rule below serves this reader.

---

### Four rules that govern this echo

**Rule 1 — The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering — relying only on initial strategy, standard planning, and normal development feedback — have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

**Rule 2 — Claim-only voice**

Every cell is stated as a claim. Prohibited from all cells:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

**Rule 3 — 120 words per column**

Each surprise column (all cells from Source through Why passive observation missed this, combined) is capped at 120 words. Under 800 words total across all columns. Constrained cells force claim extraction.

**Rule 4 — Every cell populated**

Every cell in the table is required. No cell may be absent, blank, or marked N/A. If you cannot populate a cell, the surprise is not ready to write.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise:
1. Apply Rule 1: could a passive team have discovered this?
2. Ask: can the stranger read only this column and understand the finding without any outside context?

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without outside context.
5. Keep 3–5 surprises. (Table width constrains the readable range.)

---

### Step 3 — Name each column

Assign a specific named label for each surprise before writing. Content-specific, memorable, self-explanatory without project context. These become the column headers.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Write one table. Each column is one surprise. Row headers are the field names — they apply identically to every column by construction.

```markdown
| | **{Named Label 1}** | **{Named Label 2}** | **{Named Label 3}** |
|---|---|---|---|
| **Source** | {namespace/skill} | {namespace/skill} | {namespace/skill} |
| **Expected** | We assumed X | We assumed X | We assumed X |
| **Found** | X is Y | X is Y | X is Y |
| **Design impact** | This changes... | This changes... | This changes... |
| **Why passive observation missed this** | {mechanism — for the stranger, no shorthand} | {mechanism} | {mechanism} |
```

After writing each column: count all cell words in that column (all five cells combined). If > 120: cut. Check all cells for prohibited constructs. Verify all five cells are populated. Move to the next column only when all checks pass.

---

### Step 5 — Column review

After writing all columns, read each row across the full table:

For each row header (Source / Expected / Found / Design impact / Why passive observation missed this):
- Read every cell in that row in sequence.
- Verify: every cell is populated, substantive, not N/A.
- Verify: the row header label applies correctly to every cell in that row — no cell is misaligned.

Any cell that fails: fill it or drop the column.

---

### Step 6 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every column fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any cell
- [ ] Every "Found" cell is a statement of fact

**Length (Rule 3):**
- [ ] Every column is at or under 120 words (combined across all five cells)
- [ ] Total table is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every cell is populated — no N/A, no blank

**Schema uniformity:**
- [ ] Row headers are declared once and applied to every column — the format guarantees this by construction; confirm no header row was modified after initial declaration

**Stranger utility:**
- [ ] A stranger reads any single column and understands the surprise without reading other columns or source signals
- [ ] Every "Why passive observation missed this" cell is explained without team-internal shorthand

**Structural:**
- [ ] Every column has a specific named header
- [ ] Every Source cell names the namespace + skill
- [ ] Every Expected cell states the prior assumption
- [ ] At least one column synthesizes two or more signals — name both in the Source cell
- [ ] Surprises span at least three distinct namespaces
- [ ] Add a **Patterns** section below the table if two or more columns share a root cause

---

The table format makes the schema its own enforcement mechanism. Row headers cannot diverge between columns. Any reader can scan any field across all surprises in one pass without re-reading the schema.

---

## V-04 — Combination: V-04(R4) + schema name-lock + Coupled Authority Test (C-15 + C-16)

**Axes**: Full V-04(R4) (counterfactual gate + claim-only voice + 120-word cap + newcomer framing + every field populated) plus schema name-lock from V-01 (C-15 mechanism) plus Coupled Authority Test from V-02 (C-16 mechanism). Minimum addition to the proven 100/100 baseline.

**Hypothesis**: V-04(R4) scored 100/100 on all proven criteria. C-15 and C-16 are unproven. The schema name-lock adds one pre-write manifest and one post-write label scan. The Coupled Authority Test adds one per-surprise coupled check. Risk: two new steps on top of an already-comprehensive variation may create friction for C-01 or C-11. Mitigation: both mechanisms orient toward the same newcomer-stranger reader, so they reinforce the four existing mechanisms rather than conflict with them. If both compose without friction, V-04(R5) earns 100/100 on all proven criteria plus C-15 and C-16.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — for the next team that walks this path. Fully documented, uniformly structured, authoritative in voice.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once — before they start their own investigation of the same path.** Individual surprises will also be extracted and cited in contexts where the rest of the echo is unavailable.

Every surprise must work in two modes: as part of the echo, and as a standalone portable institutional claim. Every rule below serves this reader in both modes.

---

### Schema manifest — declare before writing

Before writing any surprise, write the following into the artifact:

```markdown
## Schema manifest

Canonical field labels applied to every surprise in this document (exact — do not rename):
- **Source**
- **Expected**
- **Found**
- **Design impact**
- **Why passive observation missed this**

All fields required. None optional. None N/A. Applied in this order, with these exact labels, to every surprise.
```

This is a contract. No surprise in this document may use a synonym, abbreviation, or alternate label for any field.

---

### Four rules that govern this echo

**Rule 1 — The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering — relying only on initial strategy, standard planning, and normal development feedback — have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

A surprise a passive team would find anyway is planning documentation, not institutional memory.

**Rule 2 — Claim-only voice**

Every surprise is stated as a claim the author stands behind. Prohibited from all entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

The stranger needs claims. If you cannot assert it, drop it.

**Rule 3 — 120 words per surprise body**

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. Under 800 words total. If the stranger cannot absorb a surprise in a single reading, it has not been synthesized.

**Rule 4 — Every field populated**

Every schema field is required for every surprise. No field may be absent, blank, or marked N/A. If you cannot populate a field, the surprise is not ready to write. Confirm it further or drop it.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise:
1. Apply Rule 1: could a passive team have discovered this?
2. Ask: can the stranger understand this without reading the source? Can it stand alone when extracted?

Record both verdicts. Do not write yet.

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without reading the source artifact.
5. Keep 3–6 surprises.

---

### Step 3 — Name for the stranger

Assign a specific named label before writing. Content-specific, memorable, self-explanatory without project context. Not "Finding 3." Something specific to what this investigation found, that the stranger will remember after reading once.

---

### Step 4 — Write each surprise, then run two checks

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise uses the schema manifest exactly — five canonical fields, in order, each required:

```markdown
## {Named Label}

**Source** [required — not N/A]:
{namespace/skill where this surfaced}

**Expected** [required — not N/A]:
{stated as a claim: "We assumed X"}

**Found** [required — not N/A]:
{stated as a claim: "X is Y / X is false / the constraint is Z"}

**Design impact** [required — not N/A]:
{stated as a claim: "This changes / confirms / invalidates..."}

**Why passive observation missed this** [required — not N/A]:
{what specific signal or method surfaced it, and why planning or normal feedback would not have — explained for the stranger, not the team}
```

**After writing each surprise — before the next — run two checks:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Check B — Coupled Authority Test:**
> Extract this surprise as a standalone block. A reader who has never seen this project reads only this section.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language.
>
> **Test B — Stranger authority**: Does the extracted unit communicate all three of the following without outside context?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> Both must hold simultaneously. A stranger-accessible but hedged surprise FAILS. A claim-voiced but context-dependent surprise FAILS.

If either mechanical check or the Coupled Authority Test fails: revise. Write the next surprise only after all checks pass.

---

### Step 5 — Label parity audit

After all surprises are written, run the cross-surprise label parity audit.

For each of the five canonical labels (Source / Expected / Found / Design impact / Why passive observation missed this):
1. Read the bold label in every surprise in sequence.
2. Confirm: every surprise uses that exact canonical label — same spelling, same capitalization, same order.

Any label that deviates: correct to match the manifest. This audit checks names only; it is separate from the field completion scan.

---

### Step 6 — Field completion scan

After the label audit, scan field-by-field for content completeness:

For each canonical field: read that field for every surprise in sequence. Verify: populated, substantive, not N/A. Any failure: fill or drop.

---

### Step 7 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest appears in the artifact before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order — no renamed, abbreviated, or reordered labels

**Coupled authority:**
- [ ] Every surprise passes the Coupled Authority Test — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes structural portability while remaining hedged in voice

**Stranger utility:**
- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] Every "Why passive observation missed this" is explained without team-internal shorthand

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is institutional memory. Uniform structure makes it scannable. Coupled authority makes every surprise extractable. Complete documentation is part of the trust it earns.

---

## V-05 — Full convergence: V-05(R4) + schema name-lock + Coupled Authority Test (all seven mechanisms)

**Axes**: Full V-05(R4) (counterfactual gate + claim-only voice + 120-word cap + newcomer framing + every field populated + Check B portability test) plus schema name-lock from V-01 (C-15 mechanism) plus Coupled Authority Test as Check C from V-02 (C-16 mechanism). Maximum-mechanism combination.

**Hypothesis**: V-05(R4) scored 100/100. This variation adds two mechanisms: schema name-lock (one pre-write manifest, one post-write label scan) and the Coupled Authority Test (one per-surprise coupled check). Seven mechanisms total. Risk: each additional mechanism must share the same reader orientation to compose without friction. Predicted: the newcomer stranger is the single unifying reader for all seven mechanisms — schema name-lock and the Coupled Authority Test both orient toward the same stranger. If composition holds, V-05(R5) earns 100/100 on all proven criteria plus C-15 and C-16. If friction appears, it will show as C-01 degradation (over-complexity in culling) or C-11 violation (over-writing to satisfy multiple checks).

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of portable, fully documented institutional claims — for the next team that walks this path.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once.** Individual surprises will also be extracted from this echo — cited in design briefs, onboarding documents, and postmortems by people who will never see the full echo.

Every surprise must work in two modes: as part of the echo, and as a standalone portable institutional claim. Every rule below serves this reader in both modes.

---

### Schema manifest — declare before writing

Before writing any surprise, write the following into the artifact:

```markdown
## Schema manifest

Canonical field labels applied to every surprise in this document (exact — do not rename):
- **Source**
- **Expected**
- **Found**
- **Design impact**
- **Why passive observation missed this**

All fields required. None optional. None N/A. Applied in this order, with these exact labels, to every surprise.
```

This is a public contract. Any reader scanning "Design impact" across the full surprise set will find that label in the same position every time. No surprise in this document may use a synonym, abbreviation, or alternate label for any field.

---

### Four rules that govern this echo

**Rule 1 — The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering — relying only on initial strategy, standard planning, and normal development feedback — have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

**Rule 2 — Claim-only voice**

Every surprise is stated as a claim. Prohibited from all entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

**Rule 3 — 120 words per surprise body + 800 total**

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. Under 800 words total. If the stranger cannot absorb a surprise in a single reading, it has not been synthesized.

**Rule 4 — Every field populated**

Every schema field is required for every surprise. No field may be absent, blank, or marked N/A. If you cannot populate a field, drop the surprise or confirm it further.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise:
1. Apply Rule 1: could a passive team have discovered this?
2. Ask: can the stranger understand this without reading the source? Can it stand alone when extracted from this echo?

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without reading the source artifact.
5. Keep 3–6 surprises.

---

### Step 3 — Name for the stranger

Assign a specific named label before writing. Content-specific, memorable, self-explanatory without project context. The stranger will encounter this name out of context — it must work alone.

---

### Step 4 — Write each surprise, then run three checks

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise uses the schema manifest exactly — five canonical fields, in order, each required:

```markdown
## {Named Label}

**Source** [required — not N/A]:
{namespace/skill where this surfaced}

**Expected** [required — not N/A]:
{stated as a claim: "We assumed X"}

**Found** [required — not N/A]:
{stated as a claim: "X is Y / X is false / the constraint is Z"}

**Design impact** [required — not N/A]:
{stated as a claim: "This changes / confirms / invalidates..."}

**Why passive observation missed this** [required — not N/A]:
{what specific signal or method surfaced it, and why planning would not have — explained without project-internal shorthand}
```

**After writing each surprise — before the next — run three checks:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Check B — Portability test:**
> Imagine this surprise extracted from the echo. A reader who has never seen this project reads only this section.
>
> Does it communicate all three?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> Does it require reading any other surprise, any source signal, or any project background?

If any of the three is absent or context-dependent: revise. Write the next surprise only after Check B passes.

**Check C — Coupled Authority Test:**
> The extracted unit passes Check B structurally. Now apply the authority test to the same unit.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language. The reader receives a claim, not an observation.
>
> **Test B — Claim authority**: Does every sentence commit to the finding? No qualification, hedging, or softening of what the signal revealed.
>
> A surprise that passes Check B (structural portability) while remaining hedged in voice FAILS Check C. Structural completeness and claim authority must hold for the same extracted unit.

Write the next surprise only after Checks A, B, and C all pass.

---

### Step 5 — Label parity audit

After all surprises are written, run the cross-surprise label parity audit.

For each of the five canonical labels (Source / Expected / Found / Design impact / Why passive observation missed this):
1. Read the bold label in every surprise in sequence.
2. Confirm: every surprise uses that exact canonical label — same spelling, same capitalization, same order.

Any label that deviates: correct to match the manifest. This audit checks names only.

---

### Step 6 — Field completion scan

After the label audit, scan field-by-field for content completeness:

For each canonical field: read that field for every surprise in sequence. Verify: populated, substantive, not N/A. Any failure: fill or drop.

---

### Step 7 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest appears in the artifact before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order — no renamed, abbreviated, or reordered labels

**Portability (Check B):**
- [ ] Every surprise passes the portability test — finding, expectation, and design consequence are self-contained
- [ ] No surprise depends on context from other surprises or source signals to make sense

**Coupled authority (Check C):**
- [ ] Every surprise passes the Coupled Authority Test — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes Check B structurally while remaining hedged in voice

**Stranger utility:**
- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] "Why passive observation missed this" is explained without team-internal shorthand

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo makes the investigation portable. Each surprise is a self-contained institutional claim — complete in structure, authoritative in voice, readable by any stranger. Its value does not diminish when extracted.
