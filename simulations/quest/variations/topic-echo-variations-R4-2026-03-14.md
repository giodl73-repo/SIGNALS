Written to `simulations/quest/variations/topic-echo-variations-R4-2026-03-14.md`.

---

## topic-echo Variations R4 — Summary

| # | Axis | Target | Key mechanism |
|---|------|--------|---------------|
| **V-01** | Per-field inline `[required — not N/A]` labels | C-13 | Enforcement at write-time per field, not post-write |
| **V-02** | Portability extraction test per surprise | C-14 | Author simulates extraction after each entry before proceeding |
| **V-03** | Schema contract declaration + cross-surprise uniformity audit | C-13 (alt) | Pre-write declaration + post-write field-scan — structurally distinct from V-01 |
| **V-04** | R3-V-05 + Rule 4 (every field populated) | C-08+C-10+C-11+C-12+C-13 | Minimum addition to proven 100/100 baseline |
| **V-05** | V-04 (R4) + portability test | All six aspirational mechanisms | Check A (mechanical) + Check B (portability) per surprise |

**Design logic for R4:**

- R3 achieved 100/100 with V-05, then the rubric added C-13 and C-14. R4 tests whether those two criteria require new explicit enforcement or whether the R3 baseline already delivers them.
- **V-01 vs V-03** is a mechanism comparison for C-13 — inline labeling vs contract declaration. If both earn PASS, either mechanism works. If one fails, the winning mechanism is the required ingredient for V-04.
- **V-02** tests whether C-14 can be enforced as an explicit step rather than emerging from four-mechanism convergence.
- **V-04** is the predicted gap-closer — minimum addition to the proven baseline.
- **V-05** risk is six-mechanism friction showing as essential criteria degradation. The expected mitigation is that all six mechanisms again point at the same reader (the newcomer stranger), just as R3's four-mechanism convergence was friction-free for the same reason.
via per-field inline "required" labeling — the mechanism identified in R3's excellence signals
- V-02: C-14 via an explicit per-surprise portability isolation test — making the emergent quality explicit
- V-03: C-13 via a different mechanism (schema contract declaration + post-write uniformity audit) — tests whether V-01's inline labeling or V-03's structural audit is operationally superior

**Two combination variations** test convergence:
- V-04: R3-V-05 + C-13 enforcement only — minimum addition to close the remaining gap
- V-05: R3-V-05 + C-13 + explicit C-14 — full six-mechanism convergence

**Key structural bet in V-03**: V-01 enforces C-13 by annotating each field at write-time. V-03 enforces it by declaring a schema contract before writing and auditing field-by-field after. These are architecturally distinct. If V-01 and V-03 both earn C-13 PASS, either mechanism suffices. If one fails, the winning mechanism is operationally required for C-13 and should be incorporated into V-04.

**Key structural bet in V-02**: The v3 rubric characterizes C-14 as emergent from four converging mechanisms. An explicit portability test makes it an authorial step, not an emergent property. The risk: the test may add complexity without adding output quality (if R3-V-05 already achieved it implicitly). The gain: a repeatable enforcement mechanism any author can apply deliberately.

**V-04 prediction**: 100/100 + C-13 PASS. Rule 4 adds the explicit per-field "required — not N/A" label to the five-field R3-V-05 schema. The four existing mechanisms are unchanged. If the mechanisms compose cleanly, V-04 scores 100 on the v2 criteria and earns C-13.

**V-05 risk**: Six mechanisms. The portability test in V-05 is a per-surprise step that runs immediately after writing each entry and before the next. It adds one explicit test per item. If friction appears, it will show as reduced essential criteria scores or word-count violations (authors hedging rather than claiming, or over-writing to cover portability). If it composes cleanly, it converts C-14 from emergent to deliberate.

---

## V-01 — Single axis: Per-field completion enforcement (C-13)

**Axis**: Every schema field is labeled "required — not N/A" inline at the point of writing, plus a post-write field-scan step.

**Hypothesis**: C-13's operative mechanism is labeling each field as required at the moment the author reaches it — before they can proceed to the next field. A post-write checklist is weaker than inline enforcement because it operates after the decision. If per-field inline labeling earns C-13 PASS, it is the primary mechanism and should be carried into combination variations.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — each item fully documented, no field left empty.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

List candidate surprises. Do not filter yet.

---

### Step 2 — Cull

- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear in a standard research summary, retrospective, or findings doc.
- Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a **specific named label** to each surviving surprise before writing its body. Content-specific, memorable, not generic. "The Phantom Dependency" passes. "Finding 2" fails. "The Edge Case" fails — make it specific to what this investigation found.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

The schema below is your template. Each field is labeled with its requirement. Apply this schema identically to every surprise.

```markdown
## {Named Label}

**Source** [required — not N/A]:
{namespace/skill where this surfaced}

**Expected** [required — not N/A]:
{what the team assumed — "We assumed X"}

**Found** [required — not N/A]:
{what the signal revealed}

**Design impact** [required — not N/A]:
{how this changes, challenges, or confirms the direction — one sentence minimum}
```

When you reach each field, populate it before moving to the next. If you reach a field you cannot populate, the surprise is not ready. Drop it or confirm it more fully before writing.

---

### Step 5 — Field completion scan

After writing all surprises, scan the document field-by-field:

For each field name (Source / Expected / Found / Design impact):
- Read that field for every surprise in sequence.
- Verify it is populated with substantive content — not N/A, not blank, not "see above."
- Confirm the same field appears in every surprise — no surprise has fields another lacks.

If any field fails either check: fill it or drop the surprise. Do not publish an incomplete entry.

---

### Step 6 — Quality checks

- [ ] Every schema field is populated for every surprise — no missing fields, no N/A
- [ ] Schema is identical across all surprises — no variation in field names or count
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell states the prior assumption ("We assumed X")
- [ ] Every "Design impact" is stated explicitly, not implied
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Document under 800 words
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is only as strong as its weakest field. A gap in any cell is a gap in the institutional record.

---

## V-02 — Single axis: Portability extraction test per surprise (C-14)

**Axis**: After writing each surprise, the author extracts it and applies an isolation test before proceeding to the next.

**Hypothesis**: C-14 requires each surprise to stand alone as a self-contained institutional claim. The operative mechanism is an explicit extraction simulation — pulling the surprise out of context and verifying the finding, expectation, and design consequence are all self-contained. R3-V-05 achieved C-14 emergently via four converging mechanisms. This variation tests whether an explicit per-surprise portability test produces C-14 PASS on its own, and whether it is a reproducible enforcement mechanism independent of the four-mechanism convergence.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of portable institutional claims — each one complete enough to be useful anywhere, to anyone.

---

### What "portable" means

This echo will outlive its context. Surprises from this investigation will be cited in design briefs, onboarding documents, and postmortems by people who never saw the source signals and will not read the full echo.

Every surprise must work as a standalone claim: the finding, why it was unexpected, and why it matters for design — all present, requiring nothing outside itself.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

List candidate surprises. For each, ask: "If I extracted this as a single entry and sent it to a new-hire, could they understand it without any context?"

---

### Step 2 — Cull

- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear in a standard research summary.
- Drop anything that depends on surrounding context to make sense — if understanding it requires reading the rest of the echo or the source signals, it is not portable.
- Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a **specific named label** before writing. The name must communicate the finding to someone who has never seen the investigation. "The Phantom Dependency" passes. "Finding 3" fails. "The Onboarding Problem" fails — make it specific to what this investigation found.

---

### Step 4 — Write each surprise, then test it

`simulations/{topic}/{topic}-echo-{date}.md`

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {what the team assumed — "We assumed X"}
**Found**: {what the signal revealed}
**Design impact**: {how this changes, challenges, or confirms the direction — one sentence minimum}
```

**After writing each surprise, run the portability test before writing the next:**

> Extract this surprise — just this section. Read it as someone who:
> - Was not on this team
> - Has not read the source signals
> - Will use this finding in a new context (onboarding, design brief, postmortem)
>
> Does it communicate all three?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> Does it require reading any other surprise or any project background to make sense?

If any of the three is absent, or if understanding requires outside context: revise until all three are self-contained, or drop the surprise. Write the next surprise only after the portability test passes.

---

### Step 5 — Quality checks

- [ ] Every surprise passes the portability test — the finding, expectation, and design consequence are self-contained
- [ ] No surprise depends on reading another surprise or the source signals to make sense
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated ("We assumed X")
- [ ] Every "Design impact" is stated, not implied
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Document under 800 words
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

Each surprise is a self-contained institutional claim. Its value is not diminished by extraction.

---

## V-03 — Single axis: Schema declaration contract + cross-surprise uniformity audit (C-13)

**Axis**: The schema is declared as an explicit contract before writing any surprise. A cross-surprise uniformity audit is run after all surprises are written.

**Hypothesis**: V-01 enforces C-13 by annotating each field inline at write-time. V-03 tests a structurally distinct mechanism: the schema is declared once as a contract before writing, and uniformity is verified across all surprises in a post-write cross-surprise scan. If both V-01 and V-03 earn C-13 PASS, either mechanism suffices. If V-03 earns PARTIAL where V-01 earns PASS, inline per-field enforcement is operationally superior to declaration + audit. The structural audit in V-03 additionally enforces cross-surprise consistency in a way V-01's inline mechanism may not.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of surprises — documented uniformly and completely.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

List candidate surprises. Do not filter yet.

---

### Step 2 — Cull

- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear in a standard research summary, retrospective, or findings doc.
- Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a **specific named label** before writing. Content-specific, memorable. "The Invisible Constraint" passes. "Finding 2" fails.

---

### Step 4 — Declare the schema contract

Before writing any surprise, write this section into the artifact:

```markdown
## Schema contract

Fields applied to every surprise (all required — none optional, none N/A):
- **Source**: namespace + skill name
- **Expected**: prior assumption stated as "We assumed X"
- **Found**: what the signal revealed
- **Design impact**: explicit consequence for the design direction

This schema is applied identically to every surprise in this document.
No field may be absent, blank, or N/A. No surprise may deviate from this structure.
```

This is a public commitment. You are declaring to any reader what every surprise will contain.

---

### Step 5 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

For each surprise, apply the declared schema exactly:

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {We assumed X}
**Found**: {what the signal revealed}
**Design impact**: {explicit consequence — one sentence minimum}
```

Do not add fields. Do not remove fields. Do not leave any field blank.

---

### Step 6 — Uniformity audit

After writing all surprises, run the cross-surprise uniformity audit:

1. List the field names from your schema contract (Source / Expected / Found / Design impact).
2. For each field name: read that field in Surprise 1, then Surprise 2, then every surprise in sequence.
3. Confirm each field is: populated (not blank, not N/A, not "see above") in every surprise.
4. Confirm: the same field names appear in every surprise — no surprise has fields others lack.

Any field that fails either check: fill it or drop the surprise.

---

### Step 7 — Quality checks

- [ ] Schema contract section appears in the artifact before all surprises
- [ ] Every field declared in the schema is populated for every surprise
- [ ] Schema is identical across all surprises — no missing or extra fields
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell states the prior assumption ("We assumed X")
- [ ] Every "Design impact" is stated explicitly
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Document under 800 words
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

A uniform schema makes the echo scannable. A reader can compare any single field across all surprises in one pass. Gaps break the scan and break the trust.

---

## V-04 — Combination: R3-V-05 base + C-13 enforcement (C-08+C-10+C-11+C-12+C-13)

**Axes**: Full four-mechanism convergence from R3-V-05 (counterfactual gate + claim-only voice + per-item cap + newcomer framing) plus Rule 4 (every field populated — not N/A).

**Hypothesis**: R3-V-05 achieved 100/100 on the v2 rubric. C-13 was then codified as aspirational based on V-04's enforcement pattern (per-field "not N/A" requirement). This variation adds Rule 4 to the R3-V-05 structure as a fifth mechanism, applying inline "required — not N/A" labels to every schema field and adding a field-scan step. The four existing mechanisms are unchanged. If Rule 4 composes without friction, V-04 (R4) should score 100/100 on v2 criteria and earn C-13 PASS on the v3 criteria.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — for the next team that walks this path. Fully documented, no field left empty.

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

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. If the stranger who reads this once cannot absorb a surprise in a single reading, it is too long. Under 800 words total.

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

Each surprise uses this schema — applied identically to every entry. Each field is required:

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

**After writing each surprise**: read it as the stranger. Count words from `**Source**` through end of `**Why passive observation missed this**`. If > 120: cut until you have a claim, not a description. Check for prohibited constructs. Verify all five fields are populated. Move to the next only when all checks pass.

---

### Step 5 — Field completion scan

After writing all surprises, scan field by field:

For each field name (Source / Expected / Found / Design impact / Why passive observation missed this):
- Read that field for every surprise in sequence.
- Verify: populated, substantive, not N/A, not blank.
- If any field fails: fill it or drop the surprise.

---

### Step 6 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell is populated and explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank
- [ ] Schema is identical across all surprises — no missing or extra fields

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

The echo is institutional memory. Complete documentation is part of the trust it earns.

---

## V-05 — Full convergence: R3-V-05 + C-13 + explicit portability test (all six aspirational mechanisms)

**Axes**: V-04 (R4)'s five mechanisms (counterfactual gate + claim-only voice + per-item cap + newcomer framing + every field populated) plus an explicit per-surprise portability extraction test.

**Hypothesis**: V-04 (R4) should earn C-13 PASS while maintaining 100/100 on v2 criteria. C-14 was achieved emergently in R3-V-05 but not as an explicit execution step. This variation adds the portability extraction test from V-02 as a sixth mechanism. The risk: six mechanisms may degrade C-01 or C-04 if they create execution friction. The gain: C-14 becomes a deliberate authorial step, not an emergent consequence, making it reproducible. If V-05 scores 100/100 and earns both C-13 and C-14 without friction, the six mechanisms compose — and the portability test is confirmed as a mechanically enforceable supplement to the four-mechanism convergence.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A set of portable, fully documented institutional claims — for the next team that walks this path.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once.** Individual surprises will also be extracted from this echo — cited in design briefs, onboarding documents, and postmortems by people who will never see the full echo.

Every surprise must work in two modes: as part of the echo, and as a standalone portable claim.

Every rule below serves this reader in both modes.

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

Every schema field is required for every surprise. No field may be absent, blank, or N/A. If you cannot populate a field, drop the surprise or confirm it further.

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

### Step 4 — Write each surprise, then run the portability test

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

**After writing each surprise — before the next — run two checks:**

**Check A — Mechanical (Rules 2, 3, 4):**
- Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words. If not: cut.
- Zero prohibited constructs anywhere in the body. If any: rewrite.
- All five fields are populated — none is N/A or blank. If any is missing: confirm further or drop.

**Check B — Portability test:**
> Imagine this surprise extracted from the echo. A reader who has never seen this project reads only this section.
>
> Does it communicate all three?
> 1. What the finding is
> 2. Why it was unexpected
> 3. Why it matters for design
>
> Does it require reading any other surprise, any source signal, or any project background?

If any of the three is absent or context-dependent: revise. Write the next surprise only after both checks pass.

---

### Step 5 — Field completion scan

After all surprises are written, scan field by field:

For each field name (Source / Expected / Found / Design impact / Why passive observation missed this): read that field for every surprise in sequence. Verify: populated, substantive, not N/A. Any failure: fill or drop.

---

### Step 6 — Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell is populated and explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Schema completeness (Rule 4):**
- [ ] Every field is populated for every surprise — no N/A, no blank
- [ ] Schema is identical across all surprises — no missing or extra fields

**Portability:**
- [ ] Every surprise passes the portability test — finding, expectation, and design consequence are self-contained
- [ ] No surprise depends on context from other surprises or source signals to make sense

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

The echo makes the investigation portable. Each surprise is a self-contained institutional claim. Its value does not diminish when extracted.
