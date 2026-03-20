---

# validate-consistency — Variations R1

5 complete variations written to `simulations/quest/variations/validate-consistency-variations-R1-2026-03-20.md`.

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Role sequence | Two-pass Auditor → Skeptic split prevents P1 downgrading (C-04) via explicit role separation |
| **V-02** | Lifecycle emphasis | Heavy Phase 2 with mandatory single-location annotation fixes C-01 and C-10 before Phase 3 runs |
| **V-03** | Phrasing register | Numbered imperative step-list with no optional paths makes C-06 omission structurally harder |
| **V-04** | Lifecycle + Output format | Prose audit memo per finding makes algebraic steps (C-08) and substitution steps (C-09) the natural output form; explicit count step fixes stale frontmatter (C-05) |
| **V-05** | Role sequence + Inertia framing | Devil's Advocate epilogue forces explicit rebuttal of author defenses — P1 downgrading must be documented, not silent |

## Key design decisions

- **V-01** introduces a hard Skeptic rule: "They differ" is not a verdict. This directly attacks the C-08 miss pattern.
- **V-02** adds a Phase 2E completeness gate — if single-location count is 0 on a paper with numbers, re-sweep is mandatory. This is the most direct fix for C-10.
- **V-03** is the most structurally minimal: no phases, no headers, just numbered imperatives. Bets that removing optional framing removes the option to skip.
- **V-04** trades the Phase 4 table for a prose `Finding I-01` block that forces the model to write both conflicting values in a sentence — the format makes accurate frontmatter counting a natural last step.
- **V-05** surfaces inertia explicitly as the named competitor and gives it a named list of defenses to rebut — makes charitable downgrading visible rather than implicit.
Value / Form | Location | Appears in N locations |
|------|------|-------------|----------|------------------------|
| Q-01 | [quantity] | [value or form] | §2, Eq. 3 | 1 — single-location (unverifiable) |
| Q-02 | [quantity] | [value or form] | §4, Table 1 | 2+ — flag for cross-check |

Record ALL quantities, including those that appear only once.
Mark single-location quantities explicitly — do not omit them.

Also record:
- All equations with explicit LHS and RHS
- All numerical values in text, tables, and abstract
- All boundary conditions and limit-case claims
- All directional claims (positive feedback, inverse correlation, etc.)

### Step C — Cross-Check Pairs

List every pair of registry entries that must agree:

| Pair-ID | Q-ID A | Q-ID B | Why they must agree |
|---------|--------|--------|---------------------|

---

## PASS 2 — SKEPTIC (verdicts only, no new extraction)

You are a journal reviewer who has seen every failure mode of sloppy papers.
Your prior is that inconsistencies exist until proven otherwise.
Work only from the registries built in Pass 1.

### 3A — Value Consistency

For every pair flagged in the registry: do the values agree?

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency

For every equation pair in the cross-check list: are they algebraically equivalent?

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: algebraic step showing divergence |
|------|------|------|-------------|-------------|---------------------------------------------|

SKEPTIC RULE for 3B: a FAIL verdict must include the symbolic step. "They differ" is not
a verdict — it is a placeholder. Show the algebra.

### 3C — Boundary / Limit Consistency

For every boundary condition or limit-case claim:

| C-ID | Equation | Condition | Holds? | Substitution used to verify |
|------|----------|-----------|--------|------------------------------|

SKEPTIC RULE for 3C: show the substitution. "Setting dR/dt=0 in Eq. 7 gives..." — work
it out. A reader must be able to verify your verdict without re-deriving.

### 3D — Sign / Direction Consistency

For every directional claim in the registry:

| C-ID | Claim | Location | Sign/direction | Consistent with all uses? |
|------|-------|----------|----------------|---------------------------|

If no directional claims exist, state: "No directional claims found — 3D not applicable."

---

## PHASE 4 — INCONSISTENCY REGISTER

Skeptic assembles the final register. Every FAIL from any 3x section gets one row.

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|

Severity rules — these are hard. The Skeptic does not negotiate them down:
- P1: Same quantity with different numerical values in different locations, OR two
  equations that provably disagree. REJECT condition. No exceptions.
- P2: Ambiguous notation used for two different quantities, inconsistent units, or
  conflicting qualitative claims that don't falsify a result.
- P3: Rounding inconsistency or presentation drift that doesn't affect the argument.

If no inconsistencies found: table is still present, with row: "none found".

---

## PHASE 5 — AMENDMENTS

Ordered P1 → P2 → P3. Each fix:
- Names the exact section/table/equation to change
- States the correct value or form to use
- Does not say "verify which is right" — that is not a fix

1. [P1 fix]
2. [P2 fix, if any]
3. [P3 fix, if any]

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: validate-consistency, topic: {{topic}}, date: {{date}},
p1_count: [n], p2_count: [n], quantities_checked: [n]

p1_count and p2_count must match the actual count of rows in the register.
Count them after Phase 4 is complete — do not carry forward from earlier.
```

---

## V-02: Lifecycle Emphasis

**Axis**: Lifecycle emphasis (Phase 2 expanded)
**Hypothesis**: Making Phase 2 the heaviest, most explicit phase — with mandatory single-location annotation — forces both C-01 (complete flagging) and C-10 (single-location visibility) by front-loading the completeness burden before any checking begins.

```
You are running /validate-consistency for: {{topic}}

Check that every numbered equation, claim, and quantitative result in a paper is
mutually consistent. Catches the class of error where the same quantity appears
with different values in different places, or where two equations that must agree
(e.g. a static limit and a dynamic equation at equilibrium) do not.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: specify-spec, simulate-contract, simulate-argument.

---

## PHASE 2 — COMPLETE QUANTITY REGISTRY

This phase is the foundation of everything that follows. A weak registry produces
a weak consistency check. Do not rush it.

### 2A — Sweep: Numerical Values

Scan every section, every table, every figure caption, and the abstract.
For each numerical value found, create a row:

| Q-ID | Name / Symbol | Value | Location | Also appears at | Cross-check? |
|------|--------------|-------|----------|-----------------|--------------|
| Q-01 | MAPE | 7.4% | §3 Table 1 | Abstract | YES — 2 locations |
| Q-02 | n (sample size) | 450 | §2 | nowhere else | NO — single-location, unverifiable |

Rules:
- If a quantity appears in 2+ locations: mark Cross-check? = YES
- If a quantity appears in only 1 location: mark Cross-check? = NO and annotate
  "single-location — cannot cross-check"
- Do not omit single-location quantities. The registry must be complete.

### 2B — Sweep: Equations

For every numbered equation, record:

| E-ID | Equation # | LHS | RHS | Any other equation describing same quantity? |
|------|-----------|-----|-----|----------------------------------------------|
| E-01 | Eq. 3 | R_static | formula | Eq. 7 (dynamic, should reduce to Eq. 3 at equilibrium) |

### 2C — Sweep: Boundary and Limit Claims

For every statement of the form "reduces to X in the limit Y" or "when Z=0, this becomes W":

| B-ID | Claim | Equation referenced | Testable by substitution? |
|------|-------|--------------------|-----------------------------|

### 2D — Sweep: Directional Claims

For every phrase like "positive feedback", "inverse relationship", "monotonically increasing",
"negatively correlated":

| D-ID | Claim | Location | Symbol / equation it applies to |
|------|-------|----------|----------------------------------|

### 2E — Registry Completeness Check

Before proceeding to Phase 3, count:
- Total quantities registered: [n]
- Multi-location (will be cross-checked): [n]
- Single-location (unverifiable — registered but cannot be checked): [n]

If single-location count is 0 and the paper has any numerical values at all,
stop and re-sweep Phase 2A. Almost all papers have at least some quantities
that only appear once.

---

## PHASE 3 — CONSISTENCY CHECKS

Use only the registry from Phase 2. Do not add new quantities here.

### 3A — Value Consistency
Cross-check every Q-ID marked YES in Phase 2A.

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency
For every pair flagged in Phase 2B.

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: what diverges |
|------|------|------|-------------|-------------|------------------------|

For any FAIL row: show the algebraic step. Do not write "they differ".

### 3C — Boundary / Limit Consistency
For every item in Phase 2C.

| C-ID | Equation | Boundary condition | Holds? | Substitution: what you computed |
|------|----------|-------------------|--------|----------------------------------|

Show the substitution for every row, pass or fail.

### 3D — Sign / Direction Consistency
For every item in Phase 2D. If Phase 2D is empty, write:
"Phase 2D: no directional claims found — 3D not applicable."

| C-ID | Claim | Location | Consistent across all uses? |
|------|-------|----------|-----------------------------|

---

## PHASE 4 — INCONSISTENCY REGISTER

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|
| I-01 | Value | ... | P1 — reject condition | ... |

Severity:
- P1: Different values for the same quantity, or two equations that provably disagree
- P2: Ambiguous notation or conflicting qualitative claims without numerical falsification
- P3: Rounding or presentation inconsistency

If none: include the table with row "none found".

---

## PHASE 5 — AMENDMENTS

Ordered P1 → P2 → P3. One entry per severity level that has findings.
Each entry: exact location to change + correct value or form.

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: validate-consistency, topic: {{topic}}, date: {{date}},
p1_count: [n], p2_count: [n], quantities_checked: [n]

quantities_checked = the total from Phase 2E (all registered quantities, not just
the ones that were cross-checkable).
```

---

## V-03: Phrasing Register (Imperative Step-List)

**Axis**: Phrasing register
**Hypothesis**: A numbered imperative step-list with no optional paths removes the model's ability to silently skip a section. Every step is a required action with a concrete output. This targets C-06 (missing 3D) and C-08 (missing algebraic step) by making omission structurally harder than execution.

```
You are running /validate-consistency for: {{topic}}

Goal: find every place the paper contradicts itself — same quantity, different values;
equations that should agree but don't; limits that fail; signs that flip without explanation.

Do each step below. Do not skip steps. If a step yields no findings, write the output
anyway and state "none found."

---

**Step 1.** Read the paper for {{topic}} and any prior signals (specify-spec,
simulate-contract, simulate-argument).

**Step 2.** List every quantity (number, symbol, equation) the paper states.
For each one: write down where it appears. If it appears in more than one place,
mark it MULTI. If it appears only once, mark it SINGLE.

Output: a table with columns — Q-ID | Name | Value/Form | Location | Multi or Single

**Step 3.** For every MULTI quantity: compare all its values across locations.
If they agree: PASS. If they disagree: FAIL.

Output: a table with columns — C-ID | Quantity | Location A | Value A | Location B | Value B | Pass/Fail

**Step 4.** For every pair of equations that describe the same thing (e.g., a
dynamic equation that should reduce to a static one at equilibrium): check whether
they are algebraically equivalent.

Output: a table with columns — C-ID | Eq A | Eq B | Why they must agree | Pass/Fail | If Fail: show the algebra

For any Fail row: do not write "they differ." Write the actual symbolic step that
shows the discrepancy.

**Step 5.** For every boundary condition or limit-case claim ("reduces to X when Y=0",
"approaches Z as t→∞"): substitute the condition into the equation and verify the claim.

Output: a table with columns — C-ID | Equation | Condition | Substitution you made | Holds? | If No: what you get instead

For every row: write the substitution. For a row with no claim to test, this step
produces the table with "none found."

**Step 6.** For every directional claim ("positive feedback", "inverse relationship",
"negatively correlated", "monotonically increasing"): check whether the sign is
consistent every time the quantity appears.

Output: a table with columns — C-ID | Claim | Where stated | Sign implied | Consistent with all other uses?

If the paper has no directional claims: write the table with "none found."

**Step 7.** Collect every Fail from steps 3–6 into an inconsistency register.
Assign severity:

- P1 if: the same quantity has two different numerical values, or two equations
  provably disagree. This is a reject condition at any peer-reviewed venue. Do not
  relabel it P2 to soften it.
- P2 if: the conflict is notational ambiguity or a qualitative inconsistency that
  doesn't numerically falsify a result.
- P3 if: rounding or presentation drift that doesn't affect the argument.

Output: a table with columns — I-ID | Type | What conflicts | Severity | Fix required

If no inconsistencies: include the table with row "none found."

**Step 8.** Write three or more targeted fixes, ordered P1 → P2 → P3.
Each fix must: name the exact section/table/equation to change, and state the
correct value or form. "Verify which value is correct" is not a fix.

**Step 9.** Count: total quantities registered in step 2. Count: P1 entries in step 7.
Count: P2 entries in step 7.

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write artifact flat into <path>/
Include frontmatter:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [count from step 9]
  p2_count: [count from step 9]
  quantities_checked: [count from step 9]
```

---

## V-04: Lifecycle Emphasis + Output Format

**Axis**: Lifecycle emphasis (Phase 4 expanded) + Output format (prose audit memo for findings)
**Hypothesis**: Replacing the Phase 4 table with a structured prose memo for each finding forces the model to state both conflicting values in full sentences, making C-08 (algebraic step) and C-09 (substitution step) natural outputs. Accurate frontmatter counts (C-05) are enforced by a final explicit count step.

```
You are running /validate-consistency for: {{topic}}

Check that every numbered equation, claim, and quantitative result in a paper is
mutually consistent. Catches the class of error where the same quantity appears
with different values in different places, or where two equations that must agree
do not.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: specify-spec, simulate-contract, simulate-argument.

---

## PHASE 2 — QUANTITY REGISTRY

Extract every named quantity, equation, and quantitative result.

| Q-ID | Name | Value / Form | Location | Cross-check? |
|------|------|-------------|----------|--------------|

Flag any quantity that appears in more than one location for cross-checking.
Mark quantities that appear only once as "single-location — cannot cross-check."

Also register equations (LHS/RHS), boundary conditions, and directional claims.

---

## PHASE 3 — CONSISTENCY CHECKS

### 3A — Value Consistency

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: algebraic step |
|------|------|------|-------------|-------------|-------------------------|

### 3C — Boundary / Limit Consistency

| C-ID | Equation | Condition | Holds? | Substitution made |
|------|----------|-----------|--------|-------------------|

### 3D — Sign / Direction Consistency

| C-ID | Claim | Location | Consistent? |
|------|-------|----------|-------------|

If any section has no applicable checks, write: "[section] — none applicable."

---

## PHASE 4 — AUDIT MEMO

Do not use a table here. For each inconsistency found, write a short prose finding:

**Finding I-01 [SEVERITY]**
Quantity: [name]
Conflict: [Location A] states [Value A]. [Location B] states [Value B]. These cannot
both be correct.
[For 3B FAIL: include the algebraic step here. E.g.: "Eq. 3 gives R = A/B.
Setting dR/dt=0 in Eq. 7 gives R = A/(B+C), which equals Eq. 3 only when C=0.
The paper does not state C=0, so the forms disagree."]
[For 3C FAIL: include the substitution. E.g.: "Setting t→∞ in Eq. 5 gives
lim = k/(1-r). For r=1.2 (Table 3), this is negative, contradicting the claim
of positive steady-state in §4."]
Severity: P1 — reject condition / P2 — ambiguity / P3 — presentation drift
Action: [specific location and specific correction]

Write one such block per inconsistency. If no inconsistencies: write
"No inconsistencies found across [n] quantities checked."

---

## PHASE 4B — SEVERITY COUNTS

After writing all findings, count:
- P1 findings: [n]
- P2 findings: [n]
- Total quantities checked (from Phase 2 registry): [n]

These numbers go directly into the frontmatter. Do not estimate them.

---

## PHASE 5 — AMENDMENTS

Ordered P1 → P2 → P3. Each fix:
- Names the exact location (section, table, equation number)
- States the correct value or form
- Does not defer to the author to "decide which is right"

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter using counts from Phase 4B:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [from Phase 4B]
  p2_count: [from Phase 4B]
  quantities_checked: [from Phase 4B]
```

---

## V-05: Role Sequence + Inertia Framing

**Axis**: Role sequence + Inertia framing
**Hypothesis**: Adding an explicit Devil's Advocate pass that lists common author defenses for each finding, followed by a mandatory rebuttal or acceptance, makes P1 downgrading (C-04) structurally visible. The inertia framing surfaces the natural drift toward author charity — the primary competitor to rigorous consistency checking.

```
You are running /validate-consistency for: {{topic}}

Check that every numbered equation, claim, and quantitative result in a paper is
mutually consistent. Catches the class of error where the same quantity appears
with different values in different places, or where two equations that must agree
do not.

The primary competitor to this skill is inertia: the tendency to accept small
discrepancies as "probably rounding" or "just a simplified version for the abstract."
These explanations are almost always wrong. This skill exists to catch the cases
where they are wrong.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: specify-spec, simulate-contract, simulate-argument.

---

## PHASE 2 — QUANTITY REGISTRY

| Q-ID | Name | Value / Form | Location | Cross-check? |
|------|------|-------------|----------|--------------|

Flag multi-location quantities for cross-checking.
Include single-location quantities with note "single-location — cannot cross-check."

Also register equations, boundary conditions, and directional claims.

---

## PHASE 3 — CONSISTENCY CHECKS

### 3A — Value Consistency

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: what diverges |
|------|------|------|-------------|-------------|------------------------|

For any FAIL: show the algebraic step.

### 3C — Boundary / Limit Consistency

| C-ID | Equation | Boundary condition | Holds? | Substitution made |
|------|----------|-------------------|--------|-------------------|

For every row: show the substitution.

### 3D — Sign / Direction Consistency

| C-ID | Claim | Location | Consistent? |
|------|-------|----------|-------------|

If no directional claims: "3D — none applicable."

---

## PHASE 4 — INCONSISTENCY REGISTER

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|

Severity:
- P1: Same quantity with different numerical values, or two equations that provably
  disagree — reject condition
- P2: Notational ambiguity or qualitative inconsistency without numerical falsification
- P3: Rounding or presentation drift

If no inconsistencies: table with row "none found."

---

## PHASE 4B — DEVIL'S ADVOCATE REVIEW

For every P1 finding, list the most plausible author defense and then rebut or accept it.

The standard author defenses are:

1. "The abstract simplifies — the table is what counts."
2. "It's just rounding to different decimal places."
3. "These are different experiments / subsets / conditions."
4. "The notation changed between sections."

For each P1 finding in the register:

**Finding [I-ID] — Devil's Advocate review**
Most plausible defense: [pick the most applicable defense from the list above, or
write a more specific one if the paper warrants it]
Rebuttal or acceptance:
- If REBUT: explain exactly why the defense fails (e.g., "The abstract states
  n=450 in the same sentence that references Table 1, ruling out defense 3.")
- If ACCEPT: downgrade the finding to P2 or P3 and explain why.

A finding that survives Devil's Advocate review stays at P1.
A finding that does not survive is downgraded. Document the downgrade — do not
silently remove it.

Note: if you find yourself accepting all defenses, that is a signal that inertia
may be operating. Re-examine whether the paper actually resolves the conflict
somewhere you haven't read yet, or whether the acceptance is charitable guessing.

---

## PHASE 5 — AMENDMENTS

After Devil's Advocate review, update severity assignments if any changed.
Then list fixes ordered P1 → P2 → P3.
Each fix: exact location + correct value or form. Not "verify which is right."

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter: skill: validate-consistency, topic: {{topic}}, date: {{date}},
p1_count: [final count after Phase 4B], p2_count: [final count after Phase 4B],
quantities_checked: [n]

Use post-Phase-4B counts. If a finding was downgraded from P1 to P2 during
Devil's Advocate review, that changes both p1_count and p2_count.
```

---

## Selection Rationale

| Failure mode targeted | Primary variation | Mechanism |
|-----------------------|-------------------|-----------|
| C-01: incomplete flagging | V-02 | Phase 2 completeness check gate |
| C-04: P1 downgraded to P2 | V-01, V-05 | Skeptic role / Devil's Advocate rebuttal |
| C-05: stale frontmatter counts | V-04 | Phase 4B explicit count step |
| C-06: missing 3D section | V-03 | No optional sections in step-list |
| C-08: missing algebraic step | V-01, V-04 | Skeptic rule / prose finding format |
| C-09: missing substitution step | V-02, V-04 | Phase 2C + prose finding format |
| C-10: silent single-location omission | V-02, V-03 | Registry annotation mandate |
