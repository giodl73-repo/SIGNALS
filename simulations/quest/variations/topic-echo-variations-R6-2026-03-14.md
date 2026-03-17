Here are the 5 complete R6 variations:

---

## R6 Summary

| # | Axis | Target | Key mechanism |
|---|------|--------|---------------|
| **V-01** | Named Newcomer Gate (NGT) on V-04(R5) | C-18 partial | NGT as discrete named per-surprise gate for C-08 |
| **V-02** | Composability Manifest on V-04(R5) | C-17 | Pre-write mechanism conflict audit declared before writing |
| **V-03** | NGT on V-05(R5) base | C-18 PASS | V-05(R5) already has Check B (C-14 gate) + Check C/CAT (C-16 gate); NGT adds the missing C-08 gate |
| **V-04** | V-04(R5) + composability manifest + NGT + PGT | C-17 + C-18 | Full four-gate structure from V-04(R5) baseline |
| **V-05** | V-05(R5) + composability manifest + NGT | C-17 + C-18 | Maximum mechanism; Check B already is the PGT; NGT completes the three-gate set |

---

**Design logic:**

**C-18 gap assessment before R6:**
- V-04(R5): FAIL — only CAT present as a per-surprise named gate (C-16 covered; C-08 and C-14 ungated)
- V-05(R5): PARTIAL — Check B (named, discrete) covers C-14; Check C/CAT covers C-16; C-08 has no per-surprise gate

**C-17 gap assessment:** Neither V-04 nor V-05 (R5) was explicitly audited. R5 observed composability; R6 tests whether *declaring* it via a manifest earns the criterion or whether output-level evidence is required.

**The critical test (V-03):** Adding NGT to V-05(R5) should complete the three-gate set. V-03 is the minimum-addition path to C-18 PASS — if confirmed, it proves that the three named discrete per-surprise gates (NGT, Check B, Check C) satisfy C-18's pass condition.

**Predicted winners:** V-04 and V-05. V-05 has the cleaner mechanism lineage — Check B was already a named portability gate, so the PGT is not a new concept, just a new label. The composability manifest in both V-04 and V-05 makes the absence of mutual degradation deliberate rather than assumed.
as a named C-14 gate — named, discrete, explicit. Check C (CAT) functions as a named C-16 gate. C-08 still has no per-surprise named gate. V-05(R5) earns C-18 = PARTIAL (two of three gates present).

**V-03 as the critical test:** V-05(R5) + NGT = all three per-surprise gates present. This is the minimum-addition test for C-18 PASS from the V-05(R5) baseline. If C-18's pass condition is satisfied by three named discrete per-surprise gates, V-03 confirms it.

**V-04 as the alternative path:** V-04(R5) has only the CAT. Adding the composability manifest (C-17), the NGT (C-08 gate), and a new PGT (C-14 gate) achieves the same goal from the V-04(R5) baseline. The PGT is distinct from V-05's Check B — it frames the gate as an explicit C-14 enforcement step rather than as a structural portability check.

**Composability risk for V-04:** Four per-surprise gates (Check A + NGT + PGT + CAT) may create friction for C-11 (120-word cap) or C-01 (surprise focus), since authors may over-explain to satisfy multiple gate requirements. The composability manifest in V-04 should detect this risk before writing.

**Predicted winner:** V-05. It is the minimum addition to a proven maximum-mechanism baseline. The NGT inserts cleanly between Check A and Check B without conflicting with any existing mechanism. The composability manifest adds one pre-write step that documents what R5 already established observationally.

---

## V-01 — Single axis: Named Newcomer Gate (NGT) for C-08

**Axis**: After writing each surprise, before the CAT, run the Named Newcomer Gate (NGT) — a discrete named step that tests newcomer accessibility per surprise. The NGT is separate from the CAT: the NGT tests comprehensibility (can a stranger understand this?), while the CAT tests coupling of accessibility and claim-voice simultaneously.

**Hypothesis**: V-04(R5) earns C-08 PASS via a document-level commitment ("Who reads this"). C-18 requires per-surprise named gates — not document-level commitment — for C-08, C-14, and C-16. Adding the NGT installs a named per-surprise gate for C-08, advancing C-18 from FAIL (zero per-surprise C-08 gate) to PARTIAL (one of three per-surprise gates present: NGT for C-08, CAT for C-16, C-14 still ungated). If C-18's pass condition requires all three gates simultaneously, PARTIAL. If a single gate addition earns partial credit, this variation surfaces that boundary.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — fully documented, uniformly named, no field left empty, no field label changed.

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
{what specific signal or method surfaced it, and why planning or normal feedback would not have — explained for the stranger, not the team}
```

**After writing each surprise — before the next — run three checks in sequence:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Newcomer Gate (NGT) — C-08:**
> Extract just this surprise's text. A new-hire with no project history reads only this block.
>
> Can they understand — without any external context, project background, or access to source signals:
> 1. What the team found?
> 2. Why it was unexpected?
> 3. What it means for the design?
>
> If any answer is NO — the surprise uses unexplained jargon, project-internal shorthand, or implicit team context the newcomer lacks — rewrite before proceeding.
>
> The NGT passes only when a newcomer can absorb the surprise without preparation. Structural completeness (Check A) is not sufficient: a surprise can populate all five fields while burying its meaning behind acronyms only the team knows.

**Coupled Authority Test (CAT) — C-16:**
> Extract this surprise as a standalone block. A reader who has never seen this project reads only this section.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language.
>
> **Test B — Stranger authority**: Does the extracted unit communicate all three of the following without outside context?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> **The CAT passes only when A and B hold simultaneously for the extracted unit.**
>
> A stranger-accessible but hedged surprise FAILS — it is a portable observation, not a portable claim.
> A claim-voiced but context-dependent surprise FAILS — it is a claim the stranger cannot use.
> Both must hold together.

If any check fails: revise. Write the next surprise only after Check A, the NGT, and the CAT all pass.

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
- [ ] Every "Why passive observation missed this" explains the mechanism to a newcomer

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

**Newcomer accessibility (NGT):**
- [ ] Every surprise passed the NGT — a new-hire with no project history can absorb each surprise without preparation
- [ ] No surprise relies on unexplained jargon, project-internal shorthand, or implicit context

**Coupled authority (CAT):**
- [ ] Every surprise passes the CAT — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes structural portability while remaining hedged in voice

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" field states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The NGT and CAT serve the same reader but at different levels. The NGT tests comprehensibility: can the stranger parse this surprise at all? The CAT tests authority: does the stranger receive a claim or an observation? Both must pass before the next surprise is written.

---

## V-02 — Single axis: Composability Manifest for C-17

**Axis**: Before writing any surprise, run an explicit composability audit — a named pre-write step that lists every enforcement mechanism, names its target criterion, and checks each mechanism pair for structural conflict. The result is documented in the artifact before the schema manifest. If a conflict is detected, it is resolved before writing begins.

**Hypothesis**: V-04(R5) was found in R5 to compose cleanly — all eight mechanisms orient toward the same stranger reader with no structural conflict. But this was observed from output, not declared pre-write. C-17 asks whether mechanisms reinforce each other without mutual degradation. An explicit composability manifest makes the absence of conflict deliberate (named, documented, audited) rather than assumed. If C-17's pass condition is satisfied by declared composability, the manifest earns it. If C-17 requires the absence of conflict to be demonstrable from output structure rather than declared, the manifest alone may be insufficient. This tests the boundary.

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

### Composability manifest — declare before writing

Before writing any surprise, audit all enforcement mechanisms in this variation for structural compatibility. Write the following into the artifact as the first section:

```markdown
## Composability manifest

Active enforcement mechanisms in this variation:

| # | Mechanism | Target criterion |
|---|-----------|-----------------|
| 1 | Counterfactual gate — Rule 1 | C-10 |
| 2 | Claim-only voice table — Rule 2 | C-12 |
| 3 | 120-word cap per surprise — Rule 3 | C-11 |
| 4 | [required — not N/A] field labels — Rule 4 | C-13 |
| 5 | Who reads this commitment | C-08 |
| 6 | Schema manifest + label parity audit | C-15 |
| 7 | CAT per surprise | C-16 |

Conflict check:
- Mechanism 1 vs Mechanism 3: [reinforce / conflict — reason]
- Mechanism 1 vs Mechanism 5: [reinforce / conflict — reason]
- Mechanism 2 vs Mechanism 7: [reinforce / conflict — reason]
- Mechanism 5 vs Mechanism 7: [reinforce / conflict — reason]
- Mechanism 6 vs Mechanism 3: [reinforce / conflict — reason]
- [check every pair that could plausibly interact]

Composability declaration: [All mechanisms reinforce each other — no mechanism achieves one criterion while degrading another's enforcement path in this variation.] OR [Conflict detected between Mechanism X and Mechanism Y: [description]. Resolution: [resolution]. Declaration pending resolution.]
```

Fill every row. Check every plausible pair. Do not begin writing until the composability declaration is complete. If a conflict is detected, resolve it before writing any surprise and document the resolution.

---

### Schema manifest — declare after composability manifest

After completing the composability manifest, write the following into the artifact:

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

**Coupled Authority Test (CAT):**
> Extract this surprise as a standalone block. A reader who has never seen this project reads only this section.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language.
>
> **Test B — Stranger authority**: Does the extracted unit communicate all three of the following without outside context?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> **The CAT passes only when A and B hold simultaneously for the extracted unit.**

If either check fails: revise. Write the next surprise only after Check A and the CAT both pass.

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

### Step 7 — Composability confirmation

After writing all surprises, return to the composability manifest. Confirm: did any mechanism create structural friction during writing that was not detected pre-write? If yes, update the manifest's conflict check and add the resolution. The composability declaration must accurately reflect the variation as executed, not just as planned.

---

### Step 8 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest appears in the artifact after the composability manifest and before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order — no renamed, abbreviated, or reordered labels

**Composability:**
- [ ] Composability manifest is present and complete before all surprises
- [ ] Every mechanism pair has been checked
- [ ] Composability declaration is present and accurate
- [ ] No post-write friction detected that was not declared and resolved

**Coupled authority (CAT):**
- [ ] Every surprise passes the CAT — claim-voice and stranger-accessibility hold simultaneously for the extracted unit

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" field states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The composability manifest is not a formality. It is the author's declaration that no mechanism in this variation achieves one criterion by degrading another. The post-write confirmation closes the loop: the manifest is accurate to execution, not just to intent.

---

## V-03 — Single axis: NGT on V-05(R5) base (C-18 completion)

**Axis**: V-05(R5) has Check B (named portability gate for C-14) and Check C (CAT, named gate for C-16). Adding the Named Newcomer Gate (NGT) as a discrete step between Check A and Check B installs the missing per-surprise C-08 gate — completing the three-gate set required for C-18 PASS.

**Hypothesis**: C-18 requires all three per-surprise criteria (C-08, C-14, C-16) to be enforced via named gates that run as discrete steps. V-05(R5) is already PARTIAL (two of three gates: Check B for C-14, Check C/CAT for C-16). Adding the NGT between Check A and Check B completes the three-gate set. If C-18's pass condition is "all three per-surprise criteria have named, discrete gates," V-03 earns C-18 PASS. The NGT must be meaningfully distinct from Check B's portability test: the NGT tests whether a newcomer can parse the surprise (comprehensibility), while Check B tests whether the surprise stands alone structurally (self-containment). The gates overlap in spirit but target different failure modes — newcomer failure is jargon/implicit-context; portability failure is missing structural component.

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

This is a public contract. No surprise in this document may use a synonym, abbreviation, or alternate label for any field.

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

### Step 4 — Write each surprise, then run four checks

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

**After writing each surprise — before the next — run four checks in sequence:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Newcomer Gate (NGT) — C-08:**
> Extract just this surprise's text. A new-hire with no project history reads only this block.
>
> Can they understand — without any external context, project background, or access to source signals:
> 1. What the team found?
> 2. Why it was unexpected?
> 3. What it means for the design?
>
> If any answer is NO — the surprise uses unexplained jargon, project-internal shorthand, or implicit team context the newcomer lacks — rewrite before proceeding.
>
> The NGT is distinct from Check B: the NGT tests comprehensibility (can the stranger parse this?), not structural completeness (are all three components present?). A surprise can be structurally complete while using terminology only the team understands. The NGT catches what Check B does not.

**Check B — Portability Gate (PGT) — C-14:**
> Imagine this surprise extracted from the echo. A reader who has never seen this project reads only this section.
>
> Does it communicate all three independently:
> 1. What the finding is
> 2. Why it was unexpected (what did the team expect instead?)
> 3. Why it matters for design
>
> Does it require reading any other surprise, any source signal, or any project background to make sense?
>
> If any of the three is absent or context-dependent: revise. This gate passes only when the surprise is structurally self-contained.

**Check C — Coupled Authority Test (CAT) — C-16:**
> The extracted unit passes Check B structurally. Now apply the authority test to the same unit.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language. The reader receives a claim, not an observation.
>
> **Test B — Claim authority**: Does every sentence commit to the finding? No qualification, hedging, or softening of what the signal revealed.
>
> A surprise that passes Check B (structural portability) while remaining hedged in voice FAILS Check C. Structural completeness and claim authority must hold for the same extracted unit.

Write the next surprise only after Checks A, NGT, B, and C all pass.

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
- [ ] Every "Why passive observation missed this" explains the mechanism to a newcomer

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

**Newcomer accessibility (NGT):**
- [ ] Every surprise passed the NGT — a new-hire with no project history can absorb each surprise without preparation
- [ ] No surprise relies on unexplained jargon, project-internal shorthand, or implicit context

**Portability (Check B — PGT):**
- [ ] Every surprise passes Check B — finding, expectation, and design consequence are self-contained
- [ ] No surprise depends on context from other surprises or source signals to make sense

**Coupled authority (Check C — CAT):**
- [ ] Every surprise passes the CAT — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes Check B structurally while remaining hedged in voice

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" field states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

Three gates, three failure modes. The NGT catches jargon and implicit context. Check B catches missing structural components. The CAT catches hedged voice. A surprise must survive all three to earn its place.

---

## V-04 — Combination: V-04(R5) + composability manifest + NGT + PGT (C-17 + C-18)

**Axes**: Full V-04(R5) (Rules 1-4 + schema manifest + label parity audit + CAT) plus the composability manifest from V-02 (C-17 mechanism) plus the Named Newcomer Gate from V-01 (C-08 gate) plus a new Named Portability Gate (PGT, C-14 gate). Full three-gate per-surprise structure: NGT (C-08), PGT (C-14), CAT (C-16).

**Hypothesis**: V-04(R5) scores 100/100 + C-15 + C-16 PASS. It earns C-18 = FAIL (only CAT present as a per-surprise gate). Adding the composability manifest earns C-17 PASS (declared, documented). Adding the NGT installs the C-08 gate. Adding the PGT installs the C-14 gate. The three-gate set completes C-18. Risk: four per-surprise checks (Check A + NGT + PGT + CAT) may create friction for C-11 — the composability manifest should detect this risk pre-write. If the composability declaration finds no conflict (all gates orient toward the same stranger reader), V-04(R6) earns 100/100 + C-15 + C-16 + C-17 + C-18.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — for the next team that walks this path. Fully documented, uniformly structured, authoritative in voice, deliberate in enforcement.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once — before they start their own investigation of the same path.** Individual surprises will also be extracted and cited in contexts where the rest of the echo is unavailable.

Every surprise must work in two modes: as part of the echo, and as a standalone portable institutional claim. Every rule below serves this reader in both modes.

---

### Composability manifest — declare before writing

Before writing any surprise, audit all enforcement mechanisms for structural compatibility. Write the following into the artifact as the first section:

```markdown
## Composability manifest

Active enforcement mechanisms in this variation:

| # | Mechanism | Target criterion |
|---|-----------|-----------------|
| 1 | Counterfactual gate — Rule 1 | C-10 |
| 2 | Claim-only voice table — Rule 2 | C-12 |
| 3 | 120-word cap per surprise — Rule 3 | C-11 |
| 4 | [required — not N/A] field labels — Rule 4 | C-13 |
| 5 | Who reads this commitment | C-08 |
| 6 | Schema manifest + label parity audit | C-15 |
| 7 | NGT per surprise | C-08 (per-surprise gate) |
| 8 | PGT per surprise | C-14 (per-surprise gate) |
| 9 | CAT per surprise | C-16 (per-surprise gate) |

Conflict check:
- Mechanisms 5, 7, 8, 9: all test the same stranger reader. Reinforce. No conflict.
- Mechanism 3 vs Mechanisms 7, 8, 9: word cap may constrain explanation depth per surprise. Check: do per-surprise gate requirements cause authors to over-write? Gates require YES/NO decisions, not additional prose — no structural conflict.
- Mechanism 6 vs Mechanisms 7, 8, 9: schema uniformity and per-surprise gates target independent properties. No conflict.
- Mechanism 2 vs Mechanisms 7, 8, 9: prohibited-constructs enforcement and gate decisions reinforce — gates test the same voice property Rule 2 enforces. No conflict.

Composability declaration: All mechanisms reinforce each other — no mechanism achieves one criterion while degrading another's enforcement path in this variation.
```

If any conflict is detected: resolve before writing. Update the declaration.

---

### Schema manifest — declare after composability manifest

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

### Step 4 — Write each surprise, then run four gates

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

**After writing each surprise — before the next — run four gates in sequence:**

**Gate 1 — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Gate 2 — Newcomer Gate (NGT) — C-08:**
> Extract just this surprise's text. A new-hire with no project history reads only this block.
>
> Can they understand — without any external context:
> 1. What the team found?
> 2. Why it was unexpected?
> 3. What it means for the design?
>
> If any answer is NO — unexplained jargon, project-internal shorthand, or implicit context — rewrite before proceeding. This gate passes only when a newcomer can absorb the surprise without preparation.

**Gate 3 — Portability Gate (PGT) — C-14:**
> Copy this surprise's five fields as a standalone block. A reader who has never seen this investigation reads only these fields.
>
> Does the block communicate independently:
> 1. What was found?
> 2. Why it was unexpected (what did the team expect instead)?
> 3. What it means for the design?
>
> Does it require any context from other surprises, source signals, or project background?
>
> This gate passes only when all three are present and no external context is required. A surprise may pass the NGT (newcomer can parse the words) while failing the PGT (structural component missing). Both gates must pass.

**Gate 4 — Coupled Authority Test (CAT) — C-16:**
> The extracted unit passes Gate 3 structurally and Gate 2 in accessibility. Now apply the authority test.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language.
>
> **Test B — Stranger authority**: Does the extracted unit communicate the finding, its unexpectedness, and its design consequence — all three — without outside context?
>
> **Both must hold simultaneously.** A stranger-accessible but hedged surprise FAILS. A claim-voiced but context-dependent surprise FAILS.

Write the next surprise only after all four gates pass.

---

### Step 5 — Label parity audit

After all surprises are written, run the cross-surprise label parity audit.

For each of the five canonical labels (Source / Expected / Found / Design impact / Why passive observation missed this):
1. Read the bold label in every surprise in sequence.
2. Confirm: every surprise uses that exact canonical label — same spelling, same capitalization, same order.

Any label that deviates: correct to match the manifest.

---

### Step 6 — Field completion scan

After the label audit, scan field-by-field for content completeness:

For each canonical field: read that field for every surprise in sequence. Verify: populated, substantive, not N/A. Any failure: fill or drop.

---

### Step 7 — Composability confirmation

After writing all surprises, review the composability manifest. Did any gate create friction during writing that was not anticipated? If yes, update the conflict check and resolution. The composability declaration must reflect execution, not just intent.

---

### Step 8 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest present before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order

**Composability:**
- [ ] Composability manifest present and complete
- [ ] Composability declaration accurate to execution
- [ ] No unresolved conflicts detected

**Gates:**
- [ ] Every surprise passed Gate 2 (NGT) — newcomer can absorb without preparation
- [ ] Every surprise passed Gate 3 (PGT) — structurally self-contained, no external context required
- [ ] Every surprise passed Gate 4 (CAT) — claim-voice and stranger-accessibility hold simultaneously

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" field states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

Four gates, one reader. The composability manifest declared them compatible before writing. The gates enforce it surprise by surprise. Deliberate gating means no criterion can fail silently.

---

## V-05 — Full convergence: V-05(R5) + composability manifest + NGT (all mechanisms)

**Axes**: Full V-05(R5) (Rules 1-4 + schema manifest + label parity audit + Check A + Check B portability test + Check C/CAT) plus the composability manifest from V-02 (C-17 mechanism) plus the Named Newcomer Gate from V-01 (C-08 gate). Check B already functions as the named C-14 gate (Portability Gate). Check C already functions as the named C-16 gate (CAT). The NGT completes the three-gate set.

**Hypothesis**: V-05(R5) scores 100/100 + C-15 + C-16 PASS and earns C-18 PARTIAL (Check B covers C-14, Check C/CAT covers C-16, C-08 ungated). Adding the NGT completes C-18 — all three per-surprise criteria now have named discrete gates. Adding the composability manifest earns C-17 PASS. If both additions compose without friction with V-05(R5)'s existing seven mechanisms, V-05(R6) earns 100/100 + C-15 + C-16 + C-17 + C-18. The NGT inserts between Check A and Check B — structurally: mechanical gate, then accessibility gate, then structural-portability gate, then authority gate.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of portable, fully documented institutional claims — for the next team that walks this path. Deliberate in enforcement at every step.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once.** Individual surprises will also be extracted from this echo — cited in design briefs, onboarding documents, and postmortems by people who will never see the full echo.

Every surprise must work in two modes: as part of the echo, and as a standalone portable institutional claim. Every rule below serves this reader in both modes.

---

### Composability manifest — declare before writing

Before writing any surprise, audit all enforcement mechanisms for structural compatibility. Write the following into the artifact as the first section:

```markdown
## Composability manifest

Active enforcement mechanisms in this variation:

| # | Mechanism | Target criterion |
|---|-----------|-----------------|
| 1 | Counterfactual gate — Rule 1 | C-10 |
| 2 | Claim-only voice table — Rule 2 | C-12 |
| 3 | 120-word cap per surprise — Rule 3 | C-11 |
| 4 | [required — not N/A] field labels — Rule 4 | C-13 |
| 5 | Who reads this commitment | C-08 |
| 6 | Schema manifest + label parity audit | C-15 |
| 7 | NGT per surprise | C-08 (per-surprise gate) |
| 8 | Check B — portability test per surprise | C-14 (per-surprise gate) |
| 9 | Check C — CAT per surprise | C-16 (per-surprise gate) |

Conflict check:
- Mechanisms 5, 7, 8, 9: all test the same newcomer-stranger reader. Reinforce. No conflict.
- Mechanism 7 (NGT) vs Mechanism 8 (Check B): NGT tests comprehensibility; Check B tests structural self-containment. Adjacent but non-overlapping failure modes. Reinforce — a surprise passing the NGT but failing Check B reveals a distinct gap.
- Mechanism 3 vs Mechanisms 7, 8, 9: gates require YES/NO decisions, not prose additions. Word cap is not degraded. No conflict.
- Mechanism 6 vs Mechanisms 7, 8, 9: label uniformity and per-surprise gates target independent properties. No conflict.
- Mechanism 2 vs Mechanism 9 (CAT): Rule 2 prevents prohibited constructs document-wide; CAT tests claim-voice per-surprise as a coupled gate. Reinforce — CAT catches per-surprise failures that a document-level scan might miss between surprises.

Composability declaration: All mechanisms reinforce each other — no mechanism achieves one criterion while degrading another's enforcement path in this variation.
```

If any conflict is detected: resolve before writing. Update the declaration.

---

### Schema manifest — declare after composability manifest

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

This is a public contract. No surprise in this document may use a synonym, abbreviation, or alternate label for any field.

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

### Step 4 — Write each surprise, then run four checks

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

**After writing each surprise — before the next — run four checks in sequence:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated and use the canonical labels from the manifest. If any field is missing or mislabeled: correct before proceeding.

**Newcomer Gate (NGT) — C-08:**
> Extract just this surprise's text. A new-hire with no project history reads only this block.
>
> Can they understand — without any external context, project background, or access to source signals:
> 1. What the team found?
> 2. Why it was unexpected?
> 3. What it means for the design?
>
> If any answer is NO — unexplained jargon, project-internal shorthand, or implicit context — rewrite before proceeding.
>
> The NGT tests comprehensibility. Check B tests structural completeness. These are distinct gates: a surprise can be parseable (NGT passes) while missing the "why it was unexpected" component (Check B fails), or can be structurally complete (Check B passes) while using team-internal terminology (NGT fails).

**Check B — Portability Gate (PGT) — C-14:**
> Imagine this surprise extracted from the echo. A reader who has never seen this project reads only this section.
>
> Does it communicate all three independently:
> 1. What the finding is
> 2. Why it was unexpected (what did the team expect instead?)
> 3. Why it matters for design
>
> Does it require reading any other surprise, any source signal, or any project background?
>
> If any of the three is absent or context-dependent: revise. Write the next surprise only after Check B passes.

**Check C — Coupled Authority Test (CAT) — C-16:**
> The extracted unit passed the NGT (newcomer comprehensibility) and Check B (structural portability). Now apply the authority test to the same unit.
>
> **Test A — Institutional claim**: Is every sentence a direct statement? Zero hedge constructs. Zero uncertainty language. The reader receives a claim, not an observation.
>
> **Test B — Claim authority**: Does every sentence commit to the finding? No qualification, hedging, or softening of what the signal revealed.
>
> A surprise that passes Check B while remaining hedged in voice FAILS Check C. Structural completeness and claim authority must hold for the same extracted unit.

Write the next surprise only after Checks A, NGT, B, and C all pass.

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

### Step 7 — Composability confirmation

After writing all surprises, return to the composability manifest. Did any check create unexpected friction during writing? If yes, update the conflict check and resolution. The composability declaration must reflect execution, not just intent.

---

### Step 8 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank

**Schema uniformity (label parity):**
- [ ] Schema manifest present before all surprises
- [ ] Every surprise uses the five canonical field labels in the declared order — no renamed, abbreviated, or reordered labels

**Composability:**
- [ ] Composability manifest present, complete, and accurate to execution
- [ ] All mechanism pairs checked; composability declaration present

**Newcomer accessibility (NGT):**
- [ ] Every surprise passed the NGT — newcomer can absorb without preparation
- [ ] No surprise relies on unexplained jargon, project-internal shorthand, or implicit context

**Portability (Check B — PGT):**
- [ ] Every surprise passes Check B — finding, expectation, and design consequence are self-contained
- [ ] No surprise depends on context from other surprises or source signals

**Coupled authority (Check C — CAT):**
- [ ] Every surprise passes Check C — claim-voice and stranger-accessibility hold simultaneously for the extracted unit
- [ ] No surprise passes Check B structurally while remaining hedged in voice

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" field states the prior assumption
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

Four checks. One reader. The composability manifest declared them compatible before writing. Each check enforces a distinct failure mode: Check A catches mechanical errors, the NGT catches comprehensibility gaps, Check B catches structural incompleteness, Check C catches hedged voice. A surprise that passes all four has no remaining failure surface.
