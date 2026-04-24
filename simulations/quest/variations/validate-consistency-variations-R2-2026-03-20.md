Done. Here's the summary:

---

## validate-consistency — Variations R2

**File**: `simulations/quest/variations/validate-consistency-variations-R2-2026-03-20.md`

### Variation map

| ID | Axis | New criteria hit | Projected score |
|----|------|-----------------|-----------------|
| **V-01** | Lifecycle: Phase 2→3 gate | C-13 only | ~104 |
| **V-02** | Inertia: INERTIA CHECK at classification | C-11 only | ~110 |
| **V-03** | Output: FINAL COUNT table with phase binding | C-12 (strongest) | ~110 |
| **V-04** | Combined: imperatives + gate + warning + named count | C-11 + C-12 + C-13 | 115 |
| **V-05** | Synthesis: Auditor/Skeptic + DA + gate + FINAL COUNT | C-11 + C-12 + C-13 | 115 |

### Key design decisions

- **V-01** is the minimal gate variation — single insertion into the V-02(R1) base. Deliberately leaves C-11 unaddressed to isolate the gate effect.
- **V-02** introduces the INERTIA CHECK as a distinct C-11 mechanism — fires at classification time (unlike Skeptic which is a standing role, and DA which is a post-hoc pass). Requires a paper citation to apply any drift pattern.
- **V-03** replaces the buried frontmatter instruction with a three-row FINAL COUNT table, each row naming its source phase. Impossible to estimate or leave stale.
- **V-04** is the step-list lineage (V-03 R1 was 100/100): adds Step 2G (gate), Step 7 INERTIA CHECK, and Step 9 named binding as natural insertions. No structural overhead.
- **V-05** is the synthesis: V-01(R1) Auditor/Skeptic + V-05(R1) DA block + Pass 1 Step C gate + FINAL COUNT. All three 100-point R1 mechanisms coexist with all three new v2 criteria.
d the DA epilogue |
| **V-03** | Output format (FINAL COUNT table with explicit phase binding) | A dedicated FINAL COUNT section at artifact close, with a three-row table that names the source phase for each frontmatter field, is the strongest possible C-12 fix: impossible to estimate, impossible to leave stale |
| **V-04** | Phrasing register (imperatives) + lifecycle (gate step) + inertia (warning) + output (named count) | V-03(R1) step-list is the most structurally minimal 100-point base; adding Step 2G gate (C-13), Step 7 INERTIA CHECK (C-11), and Step 9 named binding (C-12) adds all three new criteria with no structural complexity increase |
| **V-05** | Role sequence (Auditor/Skeptic) + DA block (C-11) + registry gate (C-13) + FINAL COUNT table (C-12) | Synthesis of the three 100-point R1 patterns: Skeptic's hard severity rule, DA's documented-rebuttal block, and a gate + FINAL COUNT for the two new coverage criteria |

---

## V-01: Lifecycle Emphasis — Phase 2→3 Completeness Gate

**Axis**: Lifecycle emphasis (Phase 2→3 boundary gate)
**Hypothesis**: An explicit "Phase 2 Gate" section — requiring the model to state total
quantities, MULTI count, and SINGLE count before Phase 3 begins — fixes C-13 in the
minimal possible way. Base is V-02(R1) which had the strongest Phase 2 structure. Only
new element is the gate section.

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

### 2C — Sweep: Boundary and Limit Claims

For every statement of the form "reduces to X in the limit Y" or "when Z=0, this becomes W":

| B-ID | Claim | Equation referenced | Testable by substitution? |
|------|-------|--------------------|-----------------------------|

### 2D — Sweep: Directional Claims

For every phrase like "positive feedback", "inverse relationship", "monotonically increasing",
"negatively correlated":

| D-ID | Claim | Location | Symbol / equation it applies to |
|------|-------|----------|----------------------------------|

---

## PHASE 2 GATE — REGISTRY CLOSED

Before Phase 3 begins, confirm Phase 2 is complete.

State:
- Total quantities registered (all rows in 2A): [n]
- Multi-location (Cross-check? = YES): [n]
- Single-location (Cross-check? = NO, unverifiable): [n]

Phase 2 is now closed. Do not add quantities during Phase 3.

If single-location count is 0 and the paper contains any numerical values at all,
stop and re-sweep Phase 2A. Almost all papers have quantities that appear only once.

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

quantities_checked = the "Total quantities registered" from the Phase 2 Gate.
p1_count and p2_count = count of P1 and P2 rows in the Phase 4 register.
Count after Phase 4 is complete. Do not carry forward from earlier.
```

---

## V-02: Inertia Framing — Embedded INERTIA CHECK at Severity Classification

**Axis**: Inertia framing (named inertia patterns with paper-support requirement, inline at
severity assignment)
**Hypothesis**: An INERTIA CHECK block that fires during Step 7 — listing the four common
drift patterns and requiring explicit paper support before applying any of them — is a
distinct C-11 mechanism from the Skeptic role (a standing instruction) and the DA epilogue
(a post-hoc review). It targets the moment of classification, when downgrading is most
likely to occur silently. Base is V-03(R1) step-list.

```
You are running /validate-consistency for: {{topic}}

Goal: find every place the paper contradicts itself — same quantity, different values;
equations that should agree but don't; limits that fail; signs that flip without explanation.

The primary competitor to this skill is inertia: the tendency to smooth over a discrepancy
with "probably rounding" or "the abstract simplifies." These explanations are sometimes
correct. This skill exists to ensure they are not simply assumed.

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

**Step 4.** For every pair of equations that describe the same thing (e.g., a dynamic
equation that should reduce to a static one at equilibrium): check whether they are
algebraically equivalent.

Output: a table with columns — C-ID | Eq A | Eq B | Why they must agree | Pass/Fail | If Fail: show the algebra

For any Fail row: do not write "they differ." Write the actual symbolic step that shows
the discrepancy.

**Step 5.** For every boundary condition or limit-case claim ("reduces to X when Y=0",
"approaches Z as t→∞"): substitute the condition into the equation and verify the claim.

Output: a table with columns — C-ID | Equation | Condition | Substitution you made | Holds? | If No: what you get instead

For every row: write the substitution. For a row with no claim to test, this step
produces the table with "none found."

**Step 6.** For every directional claim ("positive feedback", "inverse relationship",
"negatively correlated", "monotonically increasing"): check whether the sign is consistent
every time the quantity appears.

Output: a table with columns — C-ID | Claim | Where stated | Sign implied | Consistent with all other uses?

If the paper has no directional claims: write the table with "none found."

**Step 7.** Collect every Fail from steps 3–6 into an inconsistency register.

Before assigning each severity label, run the INERTIA CHECK:

> **INERTIA CHECK**
> The four common drift patterns that produce invalid downgrades are:
> 1. "Probably rounding" — valid only if the difference is within the paper's stated
>    measurement tolerance or is less than 1 unit in the last place.
> 2. "The abstract simplifies" — valid only if the paper contains an explicit disclaimer
>    that the abstract uses a simplified form.
> 3. "Different experiments / conditions" — valid only if the two sections explicitly
>    identify different experimental conditions that would cause the values to differ.
> 4. "Notation changed" — valid only if the paper defines both symbols somewhere.
>
> For each finding: state which pattern (if any) was considered. If you apply a pattern,
> cite the paper location that supports it. A pattern applied without paper support is not
> a valid basis for downgrading from P1.

After the INERTIA CHECK, assign severity:
- P1 if: the same quantity has two different numerical values, or two equations provably
  disagree. Reject condition at any peer-reviewed venue. Do not relabel P2 to soften it
  unless the INERTIA CHECK found explicit paper support.
- P2 if: the conflict is notational ambiguity or a qualitative inconsistency that does
  not numerically falsify a result.
- P3 if: rounding or presentation drift that does not affect the argument.

Output: a table with columns — I-ID | Type | What conflicts | Inertia check result | Severity | Fix required

If no inconsistencies: include the table with row "none found."

**Step 8.** Write three or more targeted fixes, ordered P1 → P2 → P3.
Each fix must: name the exact section/table/equation to change, and state the correct
value or form. "Verify which value is correct" is not a fix.

**Step 9.** Count from the outputs of named steps above:
- quantities_checked = total rows in Step 2 table
- p1_count = P1 rows in Step 7 table
- p2_count = P2 rows in Step 7 table

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write artifact flat into <path>/
Include frontmatter:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [count from Step 9]
  p2_count: [count from Step 9]
  quantities_checked: [count from Step 9]
```

---

## V-03: Output Format — FINAL COUNT Table with Named Phase Binding

**Axis**: Output format (dedicated FINAL COUNT section that names the source phase for each
frontmatter field)
**Hypothesis**: A FINAL COUNT table at artifact close — with one row per frontmatter field,
each naming the specific phase it is derived from — is the strongest possible C-12 fix.
The table format makes it impossible to estimate a value or leave one stale: every cell has
a named source. Base is V-01(R1) Auditor/Skeptic (strong role enforcement), only new element
is the FINAL COUNT table replacing the buried frontmatter instruction.

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

## PASS 1 — AUDITOR (extraction only, no verdicts)

### Step A — Quantity Registry

| Q-ID | Name | Value / Form | Location | Appears in N locations |
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

### Step B — Cross-Check Pairs

List every pair of registry entries that must agree:

| Pair-ID | Q-ID A | Q-ID B | Why they must agree |
|---------|--------|--------|---------------------|

---

## PASS 2 — SKEPTIC (verdicts only, no new extraction)

You are a journal reviewer who has seen every failure mode of sloppy papers.
Your prior is that inconsistencies exist until proven otherwise.
Work only from the registries built in Pass 1.

### 3A — Value Consistency

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: algebraic step showing divergence |
|------|------|------|-------------|-------------|---------------------------------------------|

SKEPTIC RULE for 3B: a FAIL verdict must include the symbolic step. "They differ" is not
a verdict — it is a placeholder. Show the algebra.

### 3C — Boundary / Limit Consistency

| C-ID | Equation | Condition | Holds? | Substitution used to verify |
|------|----------|-----------|--------|------------------------------|

SKEPTIC RULE for 3C: show the substitution. Work it out. A reader must be able to
verify your verdict without re-deriving.

### 3D — Sign / Direction Consistency

| C-ID | Claim | Location | Sign/direction | Consistent with all uses? |
|------|-------|----------|----------------|---------------------------|

If no directional claims exist, state: "No directional claims found — 3D not applicable."

---

## PHASE 4 — INCONSISTENCY REGISTER

Skeptic assembles the final register. Every FAIL from any 3x section gets one row.

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|

Severity rules — these are hard. The Skeptic does not negotiate them down:
- P1: Same quantity with different numerical values, or two equations that provably
  disagree. REJECT condition. No exceptions.
- P2: Ambiguous notation used for two different quantities, or conflicting qualitative
  claims that don't falsify a result.
- P3: Rounding inconsistency or presentation drift that doesn't affect the argument.

If no inconsistencies found: table is still present, with row: "none found".

---

## PHASE 5 — AMENDMENTS

Ordered P1 → P2 → P3. Each fix:
- Names the exact section/table/equation to change
- States the correct value or form to use
- Does not say "verify which is right" — that is not a fix

---

## FINAL COUNT

After Phase 4 is complete, fill this table. Do not estimate. Do not fill in advance.

| Frontmatter field | Derived from | Count |
|-------------------|-------------|-------|
| quantities_checked | Total rows in Pass 1 Step A registry | [n] |
| p1_count | P1 rows in Phase 4 register | [n] |
| p2_count | P2 rows in Phase 4 register | [n] |

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter using the FINAL COUNT table:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [from FINAL COUNT — Phase 4 P1 rows]
  p2_count: [from FINAL COUNT — Phase 4 P2 rows]
  quantities_checked: [from FINAL COUNT — Pass 1 Step A total]
```

---

## V-04: Combined — Imperatives + Gate + Inertia Warning + Named Count

**Axes**: Phrasing register (numbered imperatives) + lifecycle (Phase 2→3 gate step) +
inertia framing (INERTIA CHECK at classification) + output format (named count binding)
**Hypothesis**: V-03(R1) step-list is the most structurally minimal 100-point base from
Round 1. Adding Step 2G (gate with three counts — C-13), Step 7 INERTIA CHECK (C-11),
and Step 9 with explicit phase-name binding (C-12) adds all three new v2 criteria with no
structural complexity increase — each is a single step insertion at the natural position.

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

**Step 2G — Registry Gate.**
Before Step 3, confirm the registry is complete.

State:
- Total quantities registered: [n]
- MULTI quantities (will be cross-checked in steps 3–6): [n]
- SINGLE quantities (registered but unverifiable): [n]

If SINGLE count is 0 and the paper has any numerical values, the registry is incomplete.
Re-sweep Step 2 before continuing. SINGLE quantities exist in almost every paper.

**Step 3.** For every MULTI quantity: compare all its values across locations.
If they agree: PASS. If they disagree: FAIL.

Output: a table with columns — C-ID | Quantity | Location A | Value A | Location B | Value B | Pass/Fail

**Step 4.** For every pair of equations that describe the same thing (e.g., a dynamic
equation that should reduce to a static one at equilibrium): check whether they are
algebraically equivalent.

Output: a table with columns — C-ID | Eq A | Eq B | Why they must agree | Pass/Fail | If Fail: show the algebra

For any Fail row: do not write "they differ." Write the actual symbolic step that shows
the discrepancy.

**Step 5.** For every boundary condition or limit-case claim ("reduces to X when Y=0",
"approaches Z as t→∞"): substitute the condition into the equation and verify the claim.

Output: a table with columns — C-ID | Equation | Condition | Substitution you made | Holds? | If No: what you get instead

For every row: write the substitution. For a row with no claim to test, produce the table
with "none found."

**Step 6.** For every directional claim ("positive feedback", "inverse relationship",
"negatively correlated", "monotonically increasing"): check whether the sign is consistent
every time the quantity appears.

Output: a table with columns — C-ID | Claim | Where stated | Sign implied | Consistent with all other uses?

If the paper has no directional claims: write the table with "none found."

**Step 7.** Collect every Fail from steps 3–6 into an inconsistency register.

For each finding, run the INERTIA CHECK before assigning severity:

> **INERTIA CHECK** — Is this a genuine conflict or a drift pattern?
> The four patterns that produce invalid downgrades:
> 1. "Probably rounding" — valid only if the difference falls within the paper's stated
>    measurement tolerance.
> 2. "The abstract simplifies" — valid only if the paper contains an explicit simplification
>    disclaimer in the abstract or introduction.
> 3. "Different experiments / conditions" — valid only if the two sections explicitly
>    describe different experimental conditions.
> 4. "Notation changed" — valid only if both symbols are defined somewhere in the paper.
>
> State which pattern (if any) was considered and cite the paper location that supports it.
> A pattern applied without paper support is not a valid basis for downgrading from P1.

Then assign severity:
- P1 if: the same quantity has two different numerical values, or two equations provably
  disagree. Reject condition at any peer-reviewed venue. Do not relabel P2 unless the
  INERTIA CHECK found explicit paper support for a lesser classification.
- P2 if: the conflict is notational ambiguity or a qualitative inconsistency that does
  not numerically falsify a result.
- P3 if: rounding or presentation drift that does not affect the argument.

Output: a table with columns — I-ID | Type | What conflicts | Inertia check result | Severity | Fix required

If no inconsistencies: include the table with row "none found."

**Step 8.** Write three or more targeted fixes, ordered P1 → P2 → P3.
Each fix must: name the exact section/table/equation to change, and state the correct
value or form. "Verify which value is correct" is not a fix.

**Step 9 — Final Count.** Derive each value from the named step output, not from memory
or estimates:
- quantities_checked = total rows in the Step 2 table (confirmed in Step 2G tally)
- p1_count = P1 rows in the Step 7 table
- p2_count = P2 rows in the Step 7 table

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write artifact flat into <path>/
Include frontmatter:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [from Step 9 — Step 7 P1 rows]
  p2_count: [from Step 9 — Step 7 P2 rows]
  quantities_checked: [from Step 9 — Step 2G tally]
```

---

## V-05: Full Synthesis — Auditor/Skeptic + DA Block + Registry Gate + FINAL COUNT

**Axes**: Role sequence (Auditor/Skeptic two-pass) + inertia framing (Devil's Advocate
with documented rebuttal) + lifecycle (Pass 1 completeness gate) + output format
(FINAL COUNT table bound to named phase events)
**Hypothesis**: The three R1 100-point patterns (Skeptic hard-rule enforcement, DA
documented-rebuttal mechanism, and Step 9 count binding) can all coexist in one skill
body. Adding a Phase 2 Gate step (C-13) and a FINAL COUNT table (C-12) at the natural
structural positions produces a variation that targets all 13 criteria without adding
process complexity — each addition fits an existing phase boundary.

```
You are running /validate-consistency for: {{topic}}

Check that every numbered equation, claim, and quantitative result in a paper is
mutually consistent. Catches the class of error where the same quantity appears
with different values in different places, or where two equations that must agree
(e.g. a static limit and a dynamic equation at equilibrium) do not.

The primary competitor to this skill is inertia: the tendency to accept small
discrepancies as "probably rounding" or "just a simplified version for the abstract."
These explanations are almost always wrong. This skill exists to catch the cases
where they are wrong.

---

## PHASE 1 — SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: specify-spec, simulate-contract, simulate-argument.

---

## PASS 1 — AUDITOR (extraction only, no verdicts)

### Step A — Quantity Registry

| Q-ID | Name | Value / Form | Location | Appears in N locations |
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

### Step B — Cross-Check Pairs

List every pair of registry entries that must agree:

| Pair-ID | Q-ID A | Q-ID B | Why they must agree |
|---------|--------|--------|---------------------|

### Step C — Registry Gate

Before PASS 2 begins, confirm PASS 1 is complete.

State:
- Total quantities registered: [n]
- Multi-location (flagged for cross-check): [n]
- Single-location (unverifiable): [n]

If single-location count is 0 and the paper has any numerical values, re-sweep Step A
before continuing. PASS 2 does not begin until these three numbers are stated.

---

## PASS 2 — SKEPTIC (verdicts only, no new extraction)

You are a journal reviewer who has seen every failure mode of sloppy papers.
Your prior is that inconsistencies exist until proven otherwise.
Work only from the registries built in Pass 1.

### 3A — Value Consistency

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|

### 3B — Equation Consistency

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: algebraic step showing divergence |
|------|------|------|-------------|-------------|---------------------------------------------|

SKEPTIC RULE for 3B: a FAIL verdict must include the symbolic step. "They differ" is not
a verdict — it is a placeholder. Show the algebra.

### 3C — Boundary / Limit Consistency

| C-ID | Equation | Condition | Holds? | Substitution used to verify |
|------|----------|-----------|--------|------------------------------|

SKEPTIC RULE for 3C: show the substitution. Work it out. A reader must be able to
verify your verdict without re-deriving.

### 3D — Sign / Direction Consistency

| C-ID | Claim | Location | Sign/direction | Consistent with all uses? |
|------|-------|----------|----------------|---------------------------|

If no directional claims exist, state: "No directional claims found — 3D not applicable."

---

## PHASE 4 — INCONSISTENCY REGISTER

Skeptic assembles the final register. Every FAIL from any 3x section gets one row.

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|

Severity rules — these are hard. The Skeptic does not negotiate them down:
- P1: Same quantity with different numerical values, or two equations that provably
  disagree. REJECT condition. No exceptions.
- P2: Ambiguous notation used for two different quantities, or conflicting qualitative
  claims that don't falsify a result.
- P3: Rounding inconsistency or presentation drift that doesn't affect the argument.

If no inconsistencies found: table is still present, with row: "none found".

---

## PHASE 4B — DEVIL'S ADVOCATE REVIEW

For every P1 finding, list the most plausible author defense and then rebut or accept it.

The standard author defenses are:

1. "The abstract simplifies — the table is what counts."
2. "It's just rounding to different decimal places."
3. "These are different experiments / subsets / conditions."
4. "The notation changed between sections."

For each P1 finding:

**Finding [I-ID] — Devil's Advocate review**
Most plausible defense: [pick from the list above, or write a more specific one]
Rebuttal or acceptance:
- If REBUT: explain exactly why the defense fails (cite the specific paper location).
- If ACCEPT: downgrade the finding to P2 or P3 and explain why.

A finding that survives Devil's Advocate review stays at P1.
A finding that does not survive is downgraded. Document the downgrade — do not silently
remove it from the register.

If you find yourself accepting all defenses, that is a signal that inertia may be operating.
Re-examine whether the paper actually resolves the conflict somewhere you have not yet read,
or whether the acceptance is charitable guessing without paper support.

---

## PHASE 5 — AMENDMENTS

After Phase 4B, update severity assignments for any findings that were downgraded.
Then list fixes ordered P1 → P2 → P3.
Each fix: exact location + correct value or form. Not "verify which is right."

---

## FINAL COUNT

After Phase 4B is complete, fill this table. Do not estimate. Do not fill in advance.
If a finding was downgraded during Phase 4B, the counts below already reflect that change.

| Frontmatter field | Derived from | Count |
|-------------------|-------------|-------|
| quantities_checked | Total from Pass 1 Step C gate | [n] |
| p1_count | P1 rows in Phase 4 register, post Phase 4B | [n] |
| p2_count | P2 rows in Phase 4 register, post Phase 4B | [n] |

---

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter using the FINAL COUNT table:
  skill: validate-consistency
  topic: {{topic}}
  date: {{date}}
  p1_count: [from FINAL COUNT — Phase 4 post-4B P1 rows]
  p2_count: [from FINAL COUNT — Phase 4 post-4B P2 rows]
  quantities_checked: [from FINAL COUNT — Pass 1 Step C total]
```

---

## Rubric Coverage Projection (v2, 115 pts)

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|:----:|:----:|:----:|:----:|:----:|
| C-01 registry flagged | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 3A executed | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 register with severity | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 P1 not downgraded | 12 | PARTIAL (no structural guard) | PASS (inertia check) | PASS (Skeptic role) | PASS (inertia check) | PASS (DA block) |
| C-05 frontmatter correct | 12 | PASS | PASS | PASS | PASS | PASS |
| C-06 all four checks | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 amendments ordered | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 algebraic step on 3B fail | 10 | PASS | PASS | PASS | PASS | PASS |
| C-09 substitution in 3C | 5 | PASS | PASS | PASS | PASS | PASS |
| C-10 single-location annotated | 5 | PASS | PASS | PASS | PASS | PASS |
| C-11 structural P1 enforcement | 5 | MISS | PASS | PASS | PASS | PASS |
| C-12 count bound to named phase | 5 | PASS | PASS | PASS (strongest) | PASS | PASS (strongest) |
| C-13 completeness gate | 5 | PASS | MISS | MISS | PASS | PASS |
| **Projected total** | **115** | **~104** | **~110** | **~110** | **115** | **115** |

### Coverage rationale per new criterion

**C-11 (structural P1 enforcement)**:
- V-01: Phase 4 severity definitions only — a rule, not a mechanism. MISS.
- V-02: INERTIA CHECK block at Step 7 names the four drift patterns, requires paper citation to apply any of them. Named adversarial mechanism. PASS.
- V-03: Skeptic is a named adversarial role with hard severity mandate. "Does not negotiate" embedded at the role level. PASS.
- V-04: INERTIA CHECK identical to V-02. PASS.
- V-05: DA block in Phase 4B — named-defenses list + required rebuttal or documented acceptance. The inertia warning fires if all defenses are accepted. PASS.

**C-12 (count bound to named phase event)**:
- All five: explicit count section with named source phase. V-03 and V-05 use a three-row FINAL COUNT table making the binding unmissable. All PASS.

**C-13 (completeness gate before Phase 3)**:
- V-01: "Phase 2 Gate" section between Phase 2D and Phase 3. States all three numbers. PASS.
- V-02: No gate between Step 2 and Step 3. MISS.
- V-03: No gate — the Auditor completes extraction but PASS 2 begins without a count statement. MISS.
- V-04: Step 2G between Step 2 and Step 3. States all three numbers. PASS.
- V-05: Pass 1 Step C. States all three numbers. "PASS 2 does not begin until these three numbers are stated." PASS.

### Selection rationale for scoring run

| Target | Primary variation | Mechanism |
|--------|-------------------|-----------|
| C-11 miss in V-02 R1 / V-04 R1 | V-02 (R2), V-04 (R2) | INERTIA CHECK inline at classification |
| C-13 miss in all R1 | V-01, V-04, V-05 | Phase gate with required three-count statement |
| C-12 strengthen from buried instruction to bound table | V-03, V-05 | FINAL COUNT table with source-phase column |
| C-04 structural enforcement (R1 V-02 weakness) | V-03 inherits V-01(R1) Skeptic role; V-05 inherits DA block | Named adversarial role / DA mechanism |
