Now I have full context. Writing the R7 variations.

---

# `/quest:variate` — topic-echo · Round 7

## Variation Design

R6 confirmed C-17 and C-18 as proven and introduced two new unproven criteria: C-19 (pre-write composability declaration) and C-20 (gate design integrity). R7 tests these two questions:

1. **C-19 timing strictness** — does the composability manifest need to *precede* the first written surprise, or does post-write declaration earn the criterion?
2. **C-20 mechanism** — can explicit gate-rationale documentation earn C-20, and does it matter whether the gate's origin is criterion-driven vs. rubric-driven?

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Base | V-05(R6) | V-03(R6) | V-05(R6) | V-05(R6) | V-04(R6) |
| Composability manifest | Post-write (timing shift) | None | Pre-write (pair list only, no inspection) | Pre-write + pair inspection | Pre-write + pair inspection |
| Gate rationale tags | None | Yes — NGT, Check B, CAT | None | Yes — NGT, Check B, CAT | Yes — NGT, PGT, CAT |
| C-19 prediction | FAIL (post-write) | FAIL (no manifest) | FAIL (no pair inspection) | PASS | PASS |
| C-20 prediction | PARTIAL | PASS | PARTIAL | PASS | FAIL (PGT reactive) |

**Predictions:**
- V-01: 99 — C-19 FAIL (manifest exists but post-write); C-20 PARTIAL (no rationale tags)
- V-02: 99 — C-20 PASS (rationale tags present, all gates criterion-motivated); C-19 FAIL (no manifest)
- V-03: 99 — C-19 FAIL (incomplete manifest — pair inspection absent); C-20 PARTIAL (no rationale tags)
- V-04: 100 — C-19 PASS + C-20 PASS (maximum compound, clean gate lineage)
- V-05: 99 — C-19 PASS; C-20 FAIL (PGT rationale documents reactive origin — rubric compliance, not criterion enforcement)

---

## V-01

**Axis**: Composability manifest timing — post-write declaration
**Hypothesis**: Moving the composability manifest to after surprises are written maintains C-17 PASS (mechanisms still reinforce) and C-18 PASS (gates still present) but fails C-19, which requires the manifest to *precede* the first written surprise. Post-write documentation of observed composability is distinct from pre-write commitment to composability. If C-19 PASS requires pre-write timing and V-01 fails it, this isolates timing as the operative C-19 requirement.

---

```
You are executing the /topic:echo skill for the Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

---

## WHO READS THIS

This echo is written for a stranger — a developer who has never seen this investigation, has no knowledge of the project, and must understand every surprise by reading this document alone. All decisions below serve this reader. Every mechanism below aims at one target: the stranger.

---

## RULES

**Rule 1 — Counterfactual gate**: Every surprise must fail the inertia test before inclusion. Ask: would a passive, attentive team tracking this feature normally have found this? If yes, cut it. Only findings that required active signal-gathering belong in an echo. The counterfactual mechanism explanation must name the specific reason passive observation fails — not a generic statement.

**Rule 2 — No hedge constructs**: These constructs are prohibited everywhere in the echo body:

| Prohibited | Replace with |
|-----------|-------------|
| may suggest | shows |
| appears to indicate | indicates |
| seems like | is |
| could mean | means |
| it is possible that | [state the finding directly] |
| might suggest | reveals |
| appears to | [direct verb] |
| we think | we found |

Every schema field is stated as a claim. "We assumed X" — claim. "We found Y" — claim. "This changes Z" — claim. No epistemic softening anywhere.

**Rule 3 — Word discipline**: Each surprise is stated within 120 words, measured from the first schema field through the last. The full echo is within 800 words. Count after writing each surprise before proceeding. Cut to the claim — overlong items are descriptions, not findings.

**Rule 4 — Field completeness**: Every schema field is required for every surprise. No N/A, no blank, no placeholder. If a field cannot be populated, the surprise is not ready.

---

## SCHEMA

Canonical field labels — exact, do not rename, applies to every surprise:

- **Source** [required — not N/A]: namespace, skill, or artifact where this surprise surfaced
- **We assumed** [required — not N/A]: stated as a claim — "We assumed X"
- **Found** [required — not N/A]: stated as a claim — "We found Y"
- **Why passive observation missed this** [required — not N/A]: the specific mechanism that makes active signal-gathering necessary — explained without project-internal shorthand
- **Design consequence** [required — not N/A]: stated as a claim — "This changes / requires / eliminates Z"

---

## EXECUTION

### Step 1 — Gather candidates

Read every signal artifact in the topic's namespace directories. Apply four culling filters:

1. Drop anything that was expected before gathering signals — confirmation is not a surprise
2. Drop anything untraceable to a specific signal — no source, no entry
3. Drop anything that could appear in a standard research summary or project brief unchanged
4. Drop anything the stranger cannot understand without project context — context dependence disqualifies

Apply Rule 1 now: for each candidate, ask "would a passive team have found this?" Cut anything that passes the inertia test. Retain 3–6 items that survive all four filters plus Rule 1.

### Step 2 — Name each surprise

Assign a specific, memorable label to each surviving candidate. The label must communicate the essence of the finding to the stranger — not a number, not "Surprise A", not a generic header. It must work when extracted out of context. If the label could label a different finding, it fails.

### Step 3 — Write each surprise

Apply the schema to each surprise. For each field:
- Populate before moving to the next field
- Write as a claim (Rule 2)
- The stranger reader is the target — no jargon, no unexplained acronyms, no implicit context

After writing each surprise, run the per-surprise gates in order:

**NGT — Newcomer Gate** [C-08 gate, runs first]:
Ask: can a new-hire who has never seen this project read only this surprise and understand what was found, why it matters, and why it was unexpected — without consulting any source signal?
- PASS: no project-internal vocabulary, no implicit context, no assumed background
- FAIL: any term or reference requires outside knowledge to decode

If NGT FAIL: rewrite before proceeding to Check A.

**Check A — Field and word count enforcement** [runs after NGT]:
1. Verify all five fields are populated — no N/A, no blank
2. Count words from **Source** through end of **Design consequence** — must be ≤ 120
3. Scan for prohibited constructs (Rule 2 list above) — must be zero
If any check fails: fix before writing the next surprise.

**Check B — Portability test** [C-14 gate, runs after Check A]:
Simulate extraction: imagine this surprise removed from the echo entirely and sent as a standalone note to a reader who has never seen this project. Ask:
1. Does it communicate what the finding is?
2. Does it communicate why it was unexpected?
3. Does it communicate what it means for the design?
4. Does it require reading any other surprise, any source signal, or any project background to make sense?
If any of 1–3 is missing, or if 4 is yes: rewrite before proceeding.

**CAT — Coupled Authority Test** [C-16 gate, runs after Check B]:
Run both tests as a single coupled gate:
- Test A: can the stranger understand this surprise without reading sources? (C-08 mechanism)
- Test B: is every sentence a direct claim — no prohibited constructs anywhere? (C-12 mechanism)
Both must pass. CAT FAIL on either test: revise before proceeding to the next surprise.

### Step 4 — Write patterns section (if applicable)

If any two surprises share a root cause, write a **Patterns** section identifying the shared dynamic by name. A single surprise set with no shared roots earns this by absence of counterexample.

### Step 5 — Field completion scan

Read every field of every surprise in sequence. Confirm: every field is populated with a claim-form value. Any blank or N/A: stop and fix.

### Step 6 — Label parity audit

For each canonical field name in the schema, read that field across all surprises in sequence. Every surprise must use the exact declared field label — character-identical. No renamed fields, no added fields, no omitted fields relative to the schema. Any divergence: correct before proceeding.

---

## POST-WRITE: COMPOSABILITY AUDIT

After all surprises are written and all per-surprise gates have passed, document the mechanism interactions:

**Active mechanisms in this variation**: Who reads this (stranger commitment) · Rule 1 (counterfactual gate) · Rule 2 (anti-hedge) · Rule 3 (word discipline) · Rule 4 (field completeness) · Schema manifest · NGT · Check A · Check B · CAT · Label parity audit

**Mechanism pair inspection**:
- Rule 1 + Rule 3: Rule 1 forces mechanism naming; Rule 3 constrains to claim form. Both serve the stranger reader. No conflict — Rule 3 compresses Rule 1's explanation, not removes it.
- NGT + Check B: NGT tests newcomer comprehension of vocabulary; Check B tests portability of the full unit. NGT is a prerequisite for Check B. Mutual reinforcement.
- NGT + CAT: NGT pre-validates CAT's stranger-accessibility component. No redundancy — NGT tests vocabulary; CAT tests the coupled claim+accessibility combination.
- Check B + CAT: Check B simulates extraction; CAT couples claim-voice with accessibility at the same moment. Reinforcing — a surprise that passes Check B portability with hedged voice still fails CAT.
- Rule 2 + CAT: Rule 2 provides construct-level enumeration; CAT applies it per-surprise as a coupled gate. Rule 2 is the enforcement depth; CAT is the coupling structure.
- Schema manifest + Label parity audit: Manifest declares canonical labels; audit verifies character-identical match post-write. Sequential relationship, no conflict.

Confirm: all mechanism pairs reinforce. If any conflict is found, resolve before submission.

---

## PRE-OUTPUT CHECKS

Before writing the final echo:

1. At least one surprise synthesizes two or more signals — cite both sources
2. Surprises span at least three distinct namespaces
3. A Patterns section is present if any two surprises share a root cause
4. Every surprise fails Rule 1 — a passive team would not have found it
5. Every "Why passive observation missed this" field names a specific mechanism — not "it was hidden" or "we didn't look"
6. A stranger with no project context understands every surprise without reading source signals
7. Zero prohibited constructs anywhere in the echo body
8. Every field is populated for every surprise — no N/A, no blank
9. Schema is identical across all surprises — same field names, same order

---

## OUTPUT FORMAT

Write the echo with this structure:

```
# Echo: {{topic}}
*Date: {{date}} · Signals gathered: {{namespace list}}*

## Surprises

### [Surprise name]
**Source**: ...
**We assumed**: We assumed ...
**Found**: We found ...
**Why passive observation missed this**: ...
**Design consequence**: This ...

[repeat for each surprise]

## Patterns
[if applicable]
```

The echo is institutional memory. Write it so the next team that walks this path finds what you learned, not what you expected.
```

---

## V-02

**Axis**: Gate rationale tags without composability manifest (C-20 alone, C-19 absent)
**Hypothesis**: V-03(R6) [C-18 PASS via NGT + Check B + CAT, no manifest] with explicit gate-design-rationale annotations on each per-surprise gate earns C-20 PASS: each gate names its enforced criterion and documents that removing C-20 from the rubric would not remove the gate. C-19 is absent (no manifest), testing whether C-20 is independent of C-19. If C-20 PASS + C-19 FAIL, this confirms C-19 and C-20 are orthogonal (as C-19 claims) and that gate rationale documentation is the operative C-20 mechanism.

---

```
You are executing the /topic:echo skill for the Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

---

## WHO READS THIS

This echo targets one reader: a stranger who has never seen this investigation, does not know the project vocabulary, and must understand every surprise by reading this document alone. Every mechanism below serves this reader without exception.

---

## RULES

**Rule 1 — Counterfactual gate**: Before a candidate enters the echo, it must fail the passive-observation test: would a vigilant team tracking this feature normally have surfaced this finding? If yes, cut it. The "Why passive observation missed this" field must name the specific mechanism — not a generic statement about hiddenness.

**Rule 2 — No hedge constructs**: Prohibited everywhere in the echo body:

| Prohibited | Replace with |
|-----------|-------------|
| may suggest | shows |
| appears to indicate | indicates |
| seems like | is |
| could mean | means |
| it is possible that | [direct claim] |
| might suggest | reveals |
| appears to | [direct verb] |
| we think | we found |

State every field as a direct claim. No epistemic softening. No qualifications. No uncertainty markers.

**Rule 3 — Word discipline**: Per-surprise ceiling: 120 words (measured from **Source** through end of **Design consequence**). Echo ceiling: 800 words. Count after writing each surprise. Cut to the claim — if you cannot say it in 120 words, you have not extracted the claim yet.

**Rule 4 — Field completeness**: All five schema fields must be populated for every surprise. No blank, no N/A, no placeholder. An unpopulated field means the surprise is not finished.

---

## SCHEMA

Schema contract — these field names apply to every surprise in this document. All are required. None are optional. None may be left N/A.

- **Source** [required — not N/A]
- **We assumed** [required — not N/A]
- **Found** [required — not N/A]
- **Why passive observation missed this** [required — not N/A]
- **Design consequence** [required — not N/A]

---

## EXECUTION

### Step 1 — Candidate selection

Read all signal artifacts for the topic. Apply:

1. Drop expected findings — confirmation does not belong in an echo
2. Drop untraceable items — no named source, no entry
3. Drop anything a standard project brief could contain unchanged
4. Apply Rule 1: drop anything a passive team would have found

Retain 3–6 survivors.

### Step 2 — Naming

Assign a specific, memorable label to each survivor. The label must communicate the finding to someone who has never seen the project. Generic labels ("Finding 3", "Surprise B") fail.

### Step 3 — Write each surprise using the schema

For each field, write a claim before moving to the next. After completing the surprise, run the per-surprise gate sequence:

---

**NGT — Newcomer Gate Test**

*Design rationale: This gate exists to enforce per-surprise newcomer accessibility (C-08). It was introduced as the primary mechanism for ensuring no surprise requires project-internal vocabulary or background knowledge to decode. This gate's motivation is C-08 enforcement. Removing C-20 from the rubric does not remove the motivation for NGT — C-08 still requires that a stranger can read any surprise without consulting source signals. NGT exists because the variation requires per-surprise accessibility enforcement, not because C-18 requires a named gate.*

Ask: can a new-hire reading only this surprise understand what was found, why it was unexpected, and why it matters — with no external context?
- PASS: every term is self-explanatory; no acronym requires decoding; no background knowledge is assumed
- FAIL: any term or reference requires outside knowledge

NGT FAIL → rewrite the surprise before proceeding.

---

**Check A — Structural enforcement gate**

1. All five fields populated (Rule 4)
2. Word count ≤ 120 from **Source** through end of **Design consequence** (Rule 3)
3. Zero prohibited constructs in the surprise body (Rule 2)

Any failure → fix before continuing.

---

**Check B — Portability gate**

*Design rationale: This gate exists to enforce per-surprise portability (C-14). It was introduced in V-05(R4) as the primary mechanism for verifying that each surprise stands alone as a self-contained institutional claim. This gate's motivation is C-14 enforcement — ensuring that any surprise extracted from the echo communicates its finding, unexpectedness, and design consequence without surrounding context. Removing C-20 from the rubric does not remove the motivation for Check B — C-14 still requires per-surprise portability. Check B exists because the variation requires deliberate portability enforcement, not because C-18 requires a named gate for C-14.*

Simulate extraction: this surprise is removed from the echo and sent as a standalone note to someone with no project context. Ask:
1. Does it communicate what was found?
2. Does it communicate why it was unexpected?
3. Does it communicate the design consequence?
4. Does it require any surrounding context, other surprises, or source signals to make sense?

1–3 must be yes. 4 must be no. Any failure → rewrite before proceeding.

---

**CAT — Coupled Authority Test**

*Design rationale: This gate exists to enforce per-surprise claim-authority coupling (C-16). It was introduced in V-04(R5)/V-05(R5) as the primary mechanism for ensuring each surprise passes both the stranger-accessibility test and the claim-voice test as a single coupled gate — neither independently, but as a unit. This gate's motivation is C-16 enforcement: a surprise can be stranger-accessible while still hedged, and can be claim-voiced while inaccessible; CAT requires both simultaneously. Removing C-20 from the rubric does not remove the motivation for CAT — C-16 still requires per-surprise coupled enforcement. CAT exists because the variation requires that accessibility and authority are verified together per surprise, not because C-18 requires a named gate for C-16.*

Run both tests as one gate — both must pass:
- Test A: can the stranger read this surprise and understand it completely without any external context? (C-08 mechanism applied per-surprise)
- Test B: does the surprise contain zero prohibited constructs — every sentence a direct claim? (C-12 mechanism applied per-surprise)

CAT FAIL on either test → revise before writing the next surprise.

---

### Step 4 — Patterns section

If any two surprises share a root cause, write a **Patterns** section naming the shared dynamic explicitly.

### Step 5 — Field completion scan

Scan every field of every surprise in sequence. Confirm every field holds a substantive, claim-form value. Any N/A or blank → stop and fix.

### Step 6 — Label parity audit

For each declared field name, read that field across all surprises in sequence. Confirm character-identical label in every position. Any renamed, added, or omitted field relative to the schema → correct before proceeding.

---

## PRE-OUTPUT CHECKS

1. At least one surprise synthesizes two or more distinct signals — both cited
2. Surprises span at least three distinct namespaces
3. Patterns section present if any two surprises share a root cause
4. Every surprise fails the inertia test (Rule 1)
5. Every "Why passive observation missed this" field names the specific mechanism
6. A stranger with no project context understands every surprise without source signals
7. Zero prohibited constructs in the echo body
8. Every field is populated — no N/A, no blank
9. Schema is identical across all surprises — same field names, same order

---

## OUTPUT FORMAT

```
# Echo: {{topic}}
*Date: {{date}} · Signals gathered: {{namespace list}}*

## Surprises

### [Surprise name]
**Source**: ...
**We assumed**: We assumed ...
**Found**: We found ...
**Why passive observation missed this**: ...
**Design consequence**: This ...

[repeat for each surprise]

## Patterns
[if applicable]
```

The echo is the signal that comes back from the investigation. Write what you did not expect to find.
```

---

## V-03

**Axis**: Composability manifest — mechanism listing without pair inspection
**Hypothesis**: A composability manifest that names all active mechanisms but does not inspect each mechanism pair (i.e., does not perform and declare the "does mechanism X degrade mechanism Y?" check for each pair) fails C-19. The pass condition for C-19 requires "inspects each mechanism pair" — listing is insufficient. If V-03 earns C-17 PASS (mechanisms actually compose, observable by inspection) but C-19 FAIL (manifest incomplete), this confirms that pair inspection is the operative requirement for C-19, not mere mechanism enumeration.

---

```
You are executing the /topic:echo skill for the Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

---

## WHO READS THIS

Every surprise in this echo is written for a stranger — a reader who has never encountered this investigation, does not know the project, and must understand every finding from this document alone. This reader guides every decision below.

---

## PRE-WRITE: MECHANISM INVENTORY

Before writing begins, declare all active enforcement mechanisms in this variation:

1. Stranger-reader commitment (newcomer orientation at all steps)
2. Rule 1 — counterfactual gate
3. Rule 2 — prohibited hedge constructs
4. Rule 3 — word discipline (120/800 word caps)
5. Rule 4 — field completeness
6. Schema manifest with canonical labels
7. NGT — Newcomer Gate Test (per-surprise)
8. Check A — structural enforcement (per-surprise)
9. Check B — portability test (per-surprise)
10. CAT — Coupled Authority Test (per-surprise)
11. Label parity audit (post-write)

These eleven mechanisms are active in this variation.

---

## RULES

**Rule 1 — Counterfactual gate**: Every surprise must pass the inertia test before inclusion. Ask: would a passive, attentive team normally have surfaced this finding? If yes, exclude it. The "Why passive observation missed this" field names the specific mechanism of concealment — not a generic statement.

**Rule 2 — No hedge constructs**: Prohibited everywhere in the echo body:

| Prohibited | Replace with |
|-----------|-------------|
| may suggest | shows |
| appears to indicate | indicates |
| seems like | is |
| could mean | means |
| it is possible that | [direct claim] |
| might suggest | reveals |
| appears to | [direct verb] |
| we think | we found |

Every sentence is a claim. Every field is a direct statement of fact.

**Rule 3 — Word discipline**: 120 words per surprise maximum (from **Source** through end of **Design consequence**). 800 words maximum for the full echo. Count after writing each surprise. Cut to the claim.

**Rule 4 — Field completeness**: All five schema fields are required for every surprise. No N/A. No blank. No placeholder.

---

## SCHEMA

Canonical field labels declared before writing (exact — do not rename across surprises):

- **Source** [required — not N/A]
- **We assumed** [required — not N/A]
- **Found** [required — not N/A]
- **Why passive observation missed this** [required — not N/A]
- **Design consequence** [required — not N/A]

---

## EXECUTION

### Step 1 — Candidate selection

Read all signal artifacts for the topic. Apply four filters:

1. Drop expected findings — echo is for surprises only
2. Drop untraceable items — every entry needs a named source
3. Drop anything a project brief could contain without alteration
4. Apply Rule 1: drop anything a passive team would have found normally

Retain 3–6 survivors.

### Step 2 — Naming

Give each survivor a specific, memorable label that communicates the finding to someone with no project context. Generic labels fail.

### Step 3 — Write each surprise

Populate all five schema fields as claims. After completing each surprise, run the per-surprise gate sequence in order:

**NGT — Newcomer Gate Test** [C-08 gate]

Can a new-hire reading only this surprise understand what was found, why it was unexpected, and why it matters — without any external reference?
- PASS: all terms are self-explanatory; no project-internal vocabulary
- FAIL: any term or context requires outside knowledge

NGT FAIL → rewrite before proceeding.

**Check A — Structural enforcement**

1. All five fields populated (Rule 4)
2. Word count ≤ 120 from **Source** through end of **Design consequence** (Rule 3)
3. Zero prohibited constructs in the body (Rule 2)

Any failure → fix before continuing.

**Check B — Portability test** [C-14 gate]

Simulate extraction: this surprise is sent as a standalone note to someone with no project context. Ask:
1. Does it communicate the finding?
2. Does it communicate why it was unexpected?
3. Does it communicate the design consequence?
4. Does it require any surrounding context to make sense?

1–3 must be yes. 4 must be no. Failure → rewrite before proceeding.

**CAT — Coupled Authority Test** [C-16 gate]

Run as one coupled gate:
- Test A: stranger reads this surprise and understands it completely without external context
- Test B: no prohibited constructs — every sentence a direct claim

Both must pass. Failure on either → revise before the next surprise.

### Step 4 — Patterns section

If any two surprises share a root cause, write a **Patterns** section naming the shared dynamic explicitly.

### Step 5 — Field completion scan

Read every field of every surprise in sequence. Confirm all fields are substantively populated. Any gap → stop and fix.

### Step 6 — Label parity audit

For each canonical field name, read that label across all surprises in sequence. Every surprise must use the exact declared label — character-identical. Any divergence → correct before proceeding.

---

## PRE-OUTPUT CHECKS

1. At least one surprise synthesizes two or more distinct signals — both cited
2. Surprises span at least three distinct namespaces
3. Patterns section present if any two surprises share a root cause
4. Every surprise fails the inertia test
5. Every "Why passive observation missed this" field names a specific mechanism
6. Stranger with no project context understands every surprise without source signals
7. Zero prohibited constructs in the echo body
8. Every field populated — no N/A, no blank
9. Schema identical across all surprises — same field names, same order

---

## OUTPUT FORMAT

```
# Echo: {{topic}}
*Date: {{date}} · Signals gathered: {{namespace list}}*

## Surprises

### [Surprise name]
**Source**: ...
**We assumed**: We assumed ...
**Found**: We found ...
**Why passive observation missed this**: ...
**Design consequence**: This ...

[repeat for each surprise]

## Patterns
[if applicable]
```

The echo is what the investigation returned that no one sent.
```

---

## V-04

**Axis**: V-05(R6) + gate-design-rationale tags on all three per-surprise gates (compound maximum)
**Hypothesis**: V-05(R6) already satisfies C-19 (composability manifest present as a pre-write step with full pair inspection). Adding explicit gate-design-rationale annotations — naming each gate's enforced criterion and documenting that removing C-20 from the rubric would not remove the gate — provides the evidence required for C-20 PASS. All three gates (NGT, Check B, CAT) have criterion-enforcement motivations predating any C-20 rubric requirement: NGT enforces C-08, Check B enforces C-14 (from V-05(R4) inception), CAT enforces C-16. This is the maximum compound variation targeting both C-19 and C-20.

---

```
You are executing the /topic:echo skill for the Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

---

## WHO READS THIS

This echo is written for a stranger — a developer who has never seen this investigation, has no project context, and must understand every surprise from this document alone. Every mechanism in this variation serves this reader without exception. The stranger is the single unifying target across all eleven enforcement mechanisms.

---

## PRE-WRITE: COMPOSABILITY MANIFEST

Before writing any surprise, perform this composability audit and declare the results.

**Active mechanisms in this variation** (11 total):

1. Stranger-reader commitment — orients all steps toward a single newcomer reader
2. Rule 1 — counterfactual gate — excludes passive-observation findings
3. Rule 2 — prohibited hedge constructs — enforces claim-only voice
4. Rule 3 — word discipline — 120-word per-surprise / 800-word echo caps
5. Rule 4 — field completeness — all five schema fields required, no N/A
6. Schema manifest — declares canonical labels before writing
7. NGT — Newcomer Gate Test — per-surprise accessibility check (C-08)
8. Check A — structural enforcement — per-surprise field/word/hedge check
9. Check B — Portability test — per-surprise standalone extraction test (C-14)
10. CAT — Coupled Authority Test — per-surprise stranger + claim coupled gate (C-16)
11. Label parity audit — post-write field-name uniformity verification

**Mechanism pair inspection** — for each pair, verify mutual reinforcement before writing begins:

- Stranger commitment + NGT: Both target same reader; stranger commitment frames all steps, NGT enforces per-surprise. Reinforcing.
- Stranger commitment + Check B: Check B simulates the stranger extracting the surprise. Direct expression of the commitment. Reinforcing.
- Rule 1 + Rule 3: Rule 1 requires naming a mechanism (information density); Rule 3 caps words (compression). Both together force a claim-form mechanism explanation. Reinforcing — Rule 3 does not prevent Rule 1 from earning credit; it compresses the explanation to its claim core.
- Rule 2 + Rule 3: Rule 2 eliminates hedging; Rule 3 eliminates elaboration. Both serve claim extraction. No conflict — different failure modes.
- Rule 2 + CAT: Rule 2 provides the construct-level prohibited list; CAT applies it as a per-surprise gate. Rule 2 is depth; CAT is coupling structure. Reinforcing.
- Rule 3 + Check A: Rule 3 sets the cap; Check A enforces the count per-surprise. Sequential, no conflict.
- Rule 4 + Check A: Rule 4 declares completeness requirement; Check A verifies it per-surprise. Sequential, no conflict.
- NGT + Check B: NGT tests vocabulary comprehension; Check B tests full portability of the surprise as a unit. NGT is a prerequisite for Check B — a surprise that fails NGT cannot pass Check B. Reinforcing.
- NGT + CAT: NGT pre-validates CAT's stranger-accessibility component at the vocabulary level. CAT then tests the coupled accessibility+authority unit. NGT makes CAT more reliable, not redundant. Reinforcing.
- Check B + CAT: Check B tests structural portability; CAT tests that portability is paired with authoritative voice. A surprise can pass Check B with hedged voice — CAT catches this. Sequential reinforcement, no conflict.
- Schema manifest + Label parity audit: Manifest declares canonical labels pre-write; audit verifies character-identical match post-write. Bookend relationship. No conflict.

**Composability declaration**: All eleven mechanisms reinforce each other toward the single stranger-reader target. No mechanism pair found to be in conflict. Writing may begin.

---

## RULES

**Rule 1 — Counterfactual gate**: Every item must fail the passive-observation test before inclusion. Ask: would a vigilant, attentive team tracking this feature in the normal course of work have surfaced this finding? If yes, it is not a surprise — cut it. The "Why passive observation missed this" field names the specific mechanism that made active signal-gathering necessary.

**Rule 2 — No hedge constructs**: Prohibited everywhere in the echo body:

| Prohibited | Replace with |
|-----------|-------------|
| may suggest | shows |
| appears to indicate | indicates |
| seems like | is |
| could mean | means |
| it is possible that | [state the finding directly] |
| might suggest | reveals |
| appears to | [direct verb] |
| we think | we found |

Every schema field is stated as a claim. The stranger needs direct statements they can act on.

**Rule 3 — Word discipline**: 120 words per surprise maximum (from **Source** through end of **Design consequence**). 800 words maximum for the full echo. Count after writing each surprise. If over 120: cut until you have a claim, not a description.

**Rule 4 — Field completeness**: All five schema fields are required for every surprise. No N/A. No blank. No placeholder text. An incomplete field means the surprise is not finished.

---

## SCHEMA

Canonical field labels — declared before writing, exact, applied identically to every surprise:

- **Source** [required — not N/A]
- **We assumed** [required — not N/A]
- **Found** [required — not N/A]
- **Why passive observation missed this** [required — not N/A]
- **Design consequence** [required — not N/A]

---

## EXECUTION

### Step 1 — Candidate selection

Read all signal artifacts for the topic across all namespaces. Apply:

1. Drop expected findings — the echo contains surprises only, not confirmations
2. Drop untraceable items — no named source, no entry
3. Drop anything a standard project brief or research summary could contain unchanged
4. Apply Rule 1: drop anything a vigilant team would have found through normal tracking

Retain 3–6 survivors.

### Step 2 — Naming

Assign a specific, memorable label to each survivor. The label must communicate the finding to the stranger without project context. It must work when extracted in isolation.

### Step 3 — Write each surprise

Populate all five schema fields as claims before moving to the next field. After completing each surprise, run the per-surprise gate sequence in order:

---

**NGT — Newcomer Gate Test**

*Design rationale: NGT enforces per-surprise newcomer accessibility (C-08). It was introduced as the primary enforcement mechanism for ensuring no surprise requires project-internal vocabulary or assumed background knowledge. This gate's motivation is C-08 enforcement — the variation requires that every surprise is comprehensible to a first-time reader, independent of any C-18 gating requirement. Test: remove C-20 from the rubric. NGT still exists because C-08 requires per-surprise accessibility enforcement and NGT is the designated mechanism for it.*

Ask: can a new-hire who has never seen this project read only this surprise and understand what was found, why it was unexpected, and why it matters — without any external context?
- PASS: every term is self-explanatory; no project-specific acronym requires decoding; no background assumption is relied upon
- FAIL: any term, reference, or context requires outside knowledge to decode

NGT FAIL → rewrite the surprise before proceeding to Check A.

---

**Check A — Structural enforcement gate**

1. All five fields populated — Rule 4
2. Word count from **Source** through end of **Design consequence** ≤ 120 — Rule 3
3. Zero prohibited constructs anywhere in the surprise body — Rule 2

Any failure → fix before continuing.

---

**Check B — Portability gate**

*Design rationale: Check B enforces per-surprise portability (C-14). It was introduced in V-05(R4) as the primary mechanism for verifying that each surprise is a self-contained institutional claim — not a portable observation but a portable claim that communicates its finding, unexpectedness, and design consequence independently. This gate's motivation is C-14 enforcement. The variation has required per-surprise portability verification since V-05(R4); Check B is the designated mechanism for it, predating any C-18 gating requirement. Test: remove C-20 from the rubric. Check B still exists because C-14 requires per-surprise portability enforcement and Check B is the designated mechanism for it.*

Simulate extraction: imagine this surprise removed from the echo entirely and shared as a standalone note with a reader who has never seen this project. Ask:
1. Does it communicate what was found?
2. Does it communicate why it was unexpected?
3. Does it communicate the design consequence?
4. Does it require reading any other surprise, any source signal, or any project background to make sense?

1–3 must be yes. 4 must be no. Any failure → rewrite before proceeding.

---

**CAT — Coupled Authority Test**

*Design rationale: CAT enforces per-surprise claim-authority coupling (C-16). It was introduced in V-04(R5)/V-05(R5) as the primary mechanism for ensuring each surprise passes both the stranger-accessibility test and the no-hedging test as a single coupled gate. The design insight: a surprise can be stranger-accessible while still hedged, or claim-voiced while requiring context — CAT requires both simultaneously per-surprise. This gate's motivation is C-16 enforcement. The variation has required coupled per-surprise authority enforcement since R5; CAT is the designated mechanism for it, predating any C-18 gating requirement. Test: remove C-20 from the rubric. CAT still exists because C-16 requires per-surprise coupled enforcement of accessibility and claim-voice.*

Run both tests as one coupled gate — both must pass:
- Test A: can the stranger read this surprise and understand it completely without consulting any external context? (stranger-reader commitment applied per-surprise)
- Test B: does the surprise contain zero prohibited constructs — every sentence a direct claim? (Rule 2 applied per-surprise)

CAT FAIL on either test → revise before writing the next surprise.

---

### Step 4 — Patterns section

If any two surprises share a root cause, write a **Patterns** section identifying the shared dynamic by name. A single surprise set with no shared roots earns this by default.

### Step 5 — Field completion scan

Read every field of every surprise in sequence. Confirm every field is populated with a substantive claim-form value. Any N/A or blank → stop and fix.

### Step 6 — Label parity audit

For each canonical field name in the schema declaration, read that field label across every surprise in sequence. Confirm character-identical match to the declared label. Any renamed, added, or omitted field → correct before proceeding.

---

## PRE-OUTPUT CHECKS

1. At least one surprise synthesizes two or more distinct signals — both sources cited
2. Surprises span at least three distinct namespaces
3. Patterns section present if any two surprises share a root cause
4. Every surprise fails Rule 1 — a passive team would not have found it
5. Every "Why passive observation missed this" field names a specific mechanism, not a generic description
6. A stranger with no project context understands every surprise without reading source signals
7. Zero prohibited constructs anywhere in the echo body
8. Every field populated for every surprise — no N/A, no blank
9. Schema identical across all surprises — field names character-identical, same order

---

## OUTPUT FORMAT

```
# Echo: {{topic}}
*Date: {{date}} · Signals gathered: {{namespace list}}*

## Surprises

### [Surprise name]
**Source**: ...
**We assumed**: We assumed ...
**Found**: We found ...
**Why passive observation missed this**: ...
**Design consequence**: This ...

[repeat for each surprise]

## Patterns
[if applicable]
```

The echo names what the investigation returned that no one predicted. Write it so the next team walks a shorter path.
```

---

## V-05

**Axis**: V-04(R6) PGT variant + honest gate rationale tags (C-20 stress test)
**Hypothesis**: V-04(R6) introduced PGT (Portability Gate) specifically to fill the C-14 gating gap that V-04(R5)'s emergent C-14 compliance left exposed — PGT's origin is rubric compliance (filling a C-18 requirement) rather than criterion enforcement (designing a C-14 gate from first principles). Adding explicit and *honest* gate rationale documentation to PGT — accurately documenting that PGT was installed to satisfy C-18's gating requirement for C-14 — fails C-20: the documented motivation is rubric compliance, and the pass condition requires that removing C-20 from the rubric would not remove the gate's motivation. C-19 PASS (manifest present). C-20 FAIL (PGT's rationale is rubric compliance). This confirms that retroactive documentation cannot earn C-20 when the gate's origin is reactive.

---

```
You are executing the /topic:echo skill for the Signal plugin.

Topic: {{topic}}
Arguments: {{args}}

---

## WHO READS THIS

This echo is written for a stranger who has never seen this investigation, does not know the project, and must understand every surprise from this document alone. All eleven enforcement mechanisms below serve this reader.

---

## PRE-WRITE: COMPOSABILITY MANIFEST

Before writing any surprise, perform this pre-write audit.

**Active mechanisms** (11 total):

1. Stranger-reader commitment
2. Rule 1 — counterfactual gate
3. Rule 2 — prohibited hedge constructs
4. Rule 3 — word discipline (120/800)
5. Rule 4 — field completeness
6. Schema manifest with canonical labels
7. NGT — Newcomer Gate Test (per-surprise, C-08)
8. Check A — structural enforcement (per-surprise)
9. PGT — Portability Gate (per-surprise, C-14)
10. CAT — Coupled Authority Test (per-surprise, C-16)
11. Label parity audit (post-write)

**Mechanism pair inspection**:

- Rule 1 + Rule 3: Rule 1 names mechanism of concealment; Rule 3 compresses to claim form. Reinforcing.
- Rule 2 + Rule 3: Different failure modes (hedging vs. elaboration). No conflict.
- Rule 2 + CAT: Rule 2 provides construct-level enumeration; CAT applies per-surprise. Reinforcing.
- NGT + PGT: NGT tests vocabulary comprehension; PGT tests structural portability. NGT is a prerequisite for PGT — stranger comprehension is a component of portability. Reinforcing.
- NGT + CAT: NGT pre-validates CAT's accessibility component. Reinforcing.
- PGT + CAT: PGT tests structural portability; CAT tests portability with authoritative voice. CAT adds claim-voice requirement to PGT's structural test. Sequential reinforcement.
- Rule 2 + PGT: Rule 2 enforces claim-voice; PGT tests portability. A surprise that passes PGT's structural questions while hedged still fails Rule 2 → PGT alone is insufficient for C-14; both must pass. Reinforcing — they address different failure modes.
- Schema manifest + Label parity audit: Manifest declares pre-write; audit verifies post-write. Sequential bookend, no conflict.
- Stranger commitment + NGT + PGT + CAT: All four target the same reader (stranger). Mutual reinforcement confirmed.

**Composability declaration**: All mechanism pairs reinforce. No conflicts found. Writing may begin.

---

## RULES

**Rule 1 — Counterfactual gate**: Every surprise must fail the passive-observation test. Ask: would a vigilant team tracking this feature have found this in normal work? If yes, cut it. "Why passive observation missed this" names the specific concealment mechanism.

**Rule 2 — No hedge constructs**: Prohibited everywhere in the echo body:

| Prohibited | Replace with |
|-----------|-------------|
| may suggest | shows |
| appears to indicate | indicates |
| seems like | is |
| could mean | means |
| it is possible that | [direct claim] |
| might suggest | reveals |
| appears to | [direct verb] |
| we think | we found |

Every field is a direct claim. No epistemic softening.

**Rule 3 — Word discipline**: 120 words per surprise maximum (from **Source** through end of **Design consequence**). 800 words maximum for the full echo.

**Rule 4 — Field completeness**: All five schema fields required for every surprise. No N/A, no blank, no placeholder.

---

## SCHEMA

Canonical field labels (declared before writing, exact, identical across all surprises):

- **Source** [required — not N/A]
- **We assumed** [required — not N/A]
- **Found** [required — not N/A]
- **Why passive observation missed this** [required — not N/A]
- **Design consequence** [required — not N/A]

---

## EXECUTION

### Step 1 — Candidate selection

Read all signal artifacts for the topic. Apply:

1. Drop expected findings
2. Drop untraceable items
3. Drop anything a project brief could contain unchanged
4. Apply Rule 1: drop anything a passive team would have found

Retain 3–6 survivors.

### Step 2 — Naming

Assign a specific, memorable label to each survivor. The name must communicate the finding to the stranger without context.

### Step 3 — Write each surprise

Populate all five schema fields as claims. After completing each surprise, run per-surprise gates in order:

---

**NGT — Newcomer Gate Test**

*Design rationale: NGT enforces per-surprise newcomer accessibility (C-08). It was introduced as the primary mechanism for ensuring no surprise requires project-internal vocabulary or background knowledge. This gate exists because the variation requires per-surprise C-08 enforcement. Test: remove C-20 from the rubric. NGT still exists — C-08 enforcement motivates it, not rubric compliance.*

Can a new-hire reading only this surprise understand what was found, why it was unexpected, and why it matters — without any external context?
- PASS: every term self-explanatory; no project vocabulary required
- FAIL: any term or context requires outside knowledge

NGT FAIL → rewrite before proceeding.

---

**Check A — Structural enforcement gate**

1. All five fields populated — Rule 4
2. Word count from **Source** through end of **Design consequence** ≤ 120 — Rule 3
3. Zero prohibited constructs in the surprise body — Rule 2

Any failure → fix before continuing.

---

**PGT — Portability Gate**

*Design rationale: PGT enforces per-surprise portability (C-14) as a named gate. It was introduced in V-04(R6) specifically to install an explicit C-14 gate that V-04(R5) lacked — V-04(R5)'s C-14 compliance was entirely emergent (no gate, compliance arose from four-mechanism convergence). PGT exists because C-18 requires a named per-surprise gate for every per-surprise criterion, and V-04(R5) had no named C-14 gate. The motivation for PGT is C-18 compliance — filling the gating gap. If C-20 were removed from the rubric, the pressure to document this distinction would disappear, but PGT's installation motivation remains: PGT was added to satisfy C-18's requirement for a named C-14 gate, not because the variation's C-14 enforcement philosophy demanded a new gate.*

Simulate extraction: this surprise is shared as a standalone note with a reader with no project context. Ask:
1. Does it communicate the finding?
2. Does it communicate why it was unexpected?
3. Does it communicate the design consequence?
4. Does it require surrounding context?

1–3 must be yes. 4 must be no. Any failure → rewrite before proceeding.

---

**CAT — Coupled Authority Test**

*Design rationale: CAT enforces per-surprise claim-authority coupling (C-16). It was introduced in V-04(R5)/V-05(R5) as the primary mechanism for coupled per-surprise verification of accessibility and claim-voice. This gate exists because C-16 requires per-surprise coupling — accessibility alone and claim-voice alone are insufficient. Test: remove C-20 from the rubric. CAT still exists — C-16 enforcement motivates it.*

Run as one coupled gate — both must pass:
- Test A: stranger understands this surprise completely without external context
- Test B: zero prohibited constructs — every sentence a direct claim

CAT FAIL on either test → revise before writing the next surprise.

---

### Step 4 — Patterns section

If any two surprises share a root cause, write a **Patterns** section naming the shared dynamic.

### Step 5 — Field completion scan

Confirm every field of every surprise is substantively populated. Any gap → stop and fix.

### Step 6 — Label parity audit

For each declared field name, confirm character-identical label across all surprises in sequence. Any divergence → correct.

---

## PRE-OUTPUT CHECKS

1. At least one surprise synthesizes two or more distinct signals — both cited
2. Surprises span at least three distinct namespaces
3. Patterns section present if any two surprises share a root cause
4. Every surprise fails the inertia test (Rule 1)
5. Every "Why passive observation missed this" names a specific mechanism
6. Stranger understands every surprise without source signals
7. Zero prohibited constructs in the echo body
8. Every field populated — no N/A, no blank
9. Schema identical across all surprises — same field names, same order

---

## OUTPUT FORMAT

```
# Echo: {{topic}}
*Date: {{date}} · Signals gathered: {{namespace list}}*

## Surprises

### [Surprise name]
**Source**: ...
**We assumed**: We assumed ...
**Found**: We found ...
**Why passive observation missed this**: ...
**Design consequence**: This ...

[repeat for each surprise]

## Patterns
[if applicable]
```

The echo is institutional memory for the team that walks this path next. Write what the signals returned that no one predicted.
```

---

## Summary Table

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Base** | V-05(R6) | V-03(R6) | V-05(R6) | V-05(R6) | V-04(R6) |
| **Composability manifest** | Post-write | Absent | Pre-write (list only) | Pre-write + pair inspection | Pre-write + pair inspection |
| **Gate rationale tags** | None | NGT + CheckB + CAT | None | NGT + CheckB + CAT | NGT + PGT + CAT |
| **PGT present** | No | No | No | No | Yes (reactive) |
| **C-17 prediction** | PASS | PASS | PASS | PASS | PASS |
| **C-18 prediction** | PASS | PASS | PASS | PASS | PASS |
| **C-19 prediction** | **FAIL** (post-write) | **FAIL** (no manifest) | **FAIL** (no pair inspection) | **PASS** | **PASS** |
| **C-20 prediction** | PARTIAL | **PASS** | PARTIAL | **PASS** | **FAIL** (PGT reactive) |
| **Score prediction** | 99 | 99 | 99 | **100** | 99 |

**Key questions R7 answers:**

1. C-19 timing: V-01 tests whether post-write placement fails C-19. If FAIL, timing is the operative requirement.
2. C-19 pair inspection: V-03 tests whether listing mechanisms without inspecting pairs fails C-19. If FAIL, pair inspection is required, not enumeration.
3. C-20 independence from C-19: V-02 tests whether C-20 PASS is achievable without a manifest. If PASS, C-19 and C-20 are confirmed orthogonal.
4. Maximum compound: V-04 tests the full C-19 + C-20 path. If 100/100, both new criteria are proven together.
5. Reactive gate ceiling: V-05 tests whether honest rationale documentation of a reactive gate fails C-20. If FAIL, motivation origin is the operative C-20 requirement — documentation cannot retroactively change it.
