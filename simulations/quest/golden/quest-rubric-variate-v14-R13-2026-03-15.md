# quest-rubric Variate — Round 13 (Against rubric v13 — C-41 and C-42)
**Date:** 2026-03-15
**Rubric:** v13 (C-01--C-42; adds C-41: named-audit-roles-bound-to-named-phase-spans; C-42: per-STOP-instance-consequence-chain-independent-named-blocks-with-sequential-gate)
**Target criteria:** C-41, C-42

**Round 13 design note:** Round 12 produced mechanisms for C-38 (Definer output exclusion gate),
C-39 (role exit gate named in Builder entry precondition), and C-40 (PHASE-LOCALITY RULE with
enumerated zones). Rubric v13 adds C-41 and C-42 extracted from R12 excellence signals. V-03
and V-04 of R12 PASS C-41 by binding named roles to named phase spans via ownership
declarations co-located with phase headings (Table Gatekeeper → Competing Implementations
construction phase; Table Architect → Phase C). V-05 of R12 FAILS C-41 because roles exist
but phase boundaries require per-step reading to resolve. V-03 and V-04 of R12 PASS C-42 by
producing structurally independent named blocks whose absence is a detectable heading-scan gap
before the next STOP. V-05 of R12 FAILS C-42 because Link 1/2/3 annotations are inline and
create no heading-scan gap when absent.

**C-41 vs C-17.** C-17 requires role/phase separation: named roles must be structurally
distinct from phase steps. A rubric satisfies C-17 when named roles exist as distinct
structural units, even if the role's phase boundaries require reading the instructions to
determine. C-41 requires that each named role is coupled to a named phase span via an explicit
ownership declaration co-located with the phase heading -- the declaration must name the span
and appear at or immediately after the heading label, making role compliance verifiable by
heading-label scan alone. Two rubrics that both name roles with distinct structural units differ
on C-41 solely by whether the ownership declaration is co-located with the heading (passes
C-41) or buried in the instructions (fails C-41 while satisfying C-17).

**C-42 vs C-15/C-19.** C-15 requires check outputs to be named section blocks detectable by
heading scan. C-19 requires both templates to be produced as a unified paired output before the
Builder runs. A rubric satisfies C-15 (check outputs are named blocks) and C-19 (both templates
present) while failing C-42 if STOP consequence chains are inline annotations that create no
heading-scan gap. C-42 extends the same named-block requirement to per-STOP-instance level:
each STOP's consequence chain must produce an independent named block with a sequential gate --
STOP N's block must appear before STOP N+1 is written. Two rubrics with identical named check
output sections differ on C-42 solely by whether STOP consequence chains produce independent
named blocks (passes C-42) or inline annotations like "Link 1/Link 2/Link 3" (fails C-42 while
satisfying C-15).

**Axis selection:**

Three axes map to the two new criteria:
- Lifecycle emphasis → C-41: ROLE heading labels include phase-span ownership declarations
  co-located with the heading, making role compliance verifiable by heading-label scan without
  reading instructions
- Output format → C-42: each STOP condition requires a named section block artifact; a
  sequential gate prevents STOP N+1 from being written until STOP N's block appears in the
  heading sequence
- Inertia framing → C-42: the wrong form (inline consequence annotations without named
  headings that create no heading-scan gap) is shown explicitly before the required form is
  defined

Single-axis variations: V-01 (lifecycle emphasis), V-02 (output format), V-03 (inertia
framing)
Combined variations: V-04 (lifecycle emphasis + output format), V-05 (role sequence + inertia
framing)

---

## Round 13 Variation Map

| Variation | Axis | C-41 probe | C-42 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis (phase-span ownership in ROLE heading label) | Very strong -- ROLE: MECHANISM DEFINER and ROLE: BUILDER ASPIRATIONAL headings each include a phase-span ownership declaration co-located with the heading; verifiable by heading scan without reading instructions | None -- STOP conditions remain as standard inline instructions; no named consequence blocks; no sequential gate | Single-axis; tests whether phase-span co-location in the heading alone satisfies C-41 without STOP block structuring |
| V-02 | Output format (named STOP consequence blocks with sequential gate) | None -- role headings use standard format without phase-span declarations; phase boundaries require reading instructions | Very strong -- STOP CONSEQUENCE FORMAT rule stated before first STOP; each STOP must produce a `### STOP CONSEQUENCE [N]:` named block before proceeding; sequential gate prevents STOP N+1 from being written until STOP N's block heading appears in the heading sequence | Single-axis; tests whether named block format + sequential gate alone satisfies C-42 without phase-span ownership |
| V-03 | Inertia framing (wrong-form STOP annotations shown before required form) | None -- role headings use standard format | Very strong -- before the first STOP consequence form is required, the wrong form (inline Link 1/Link 2/Link 3 annotations that create no heading-scan gap) is named and prohibited; the required form (independent named section block) is defined after the wrong form; sequential gate stated | Single-axis; tests whether explicit wrong-form inertia framing satisfies C-42 without lifecycle role emphasis |
| V-04 | Lifecycle emphasis + Output format (C-41 + C-42) | Very strong -- ROLE headings include phase-span ownership declarations (same mechanism as V-01) | Very strong -- STOP CONSEQUENCE FORMAT rule + sequential gate (same mechanism as V-02) | Combined; tests superadditivity: does C-41 compliance change when C-42 is also present? C-38/C-39/C-40 ablated |
| V-05 | Role sequence + Inertia framing (C-41 + C-42 via different mechanisms) | Very strong -- ROLE-PHASE REGISTRY produced before Phase 3; each role heading cites its registry entry by identifier; ownership verifiable from Registry + heading scan | Very strong -- inertia framing shows wrong form explicitly before required form; sequential gate stated (different framing mechanism from V-02/V-04) | Combined; different mechanisms than V-04 for both criteria; tests whether REGISTRY citation approach to C-41 is equivalent to or weaker than inline heading declaration |

---

## V-01 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- each named role heading includes a phase-span ownership
declaration co-located with the heading label, making role compliance verifiable by
heading-label scan without reading the role instructions.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain ROLE: MECHANISM DEFINER and ROLE: BUILDER ASPIRATIONAL headings that each include a phase-span ownership declaration co-located with the heading -- any body where the role's phase boundaries require reading the instructions to determine falsifies the hypothesis; the falsification signal is a role heading that names the role without naming its phase span in the heading label or immediately after it. | The phase-span ownership declaration in the heading creates a heading-label-readable contract: an evaluator scanning only headings can enumerate all roles and their phase spans without reading any instruction prose; generated rubrics under V-01 will show this scanability while baseline rubrics require reading instructions to reconstruct phase boundaries; if V-04 (which adds named STOP blocks) shows no further improvement in C-41 compliance over V-01, the heading declaration alone is sufficient for C-41 without STOP block reinforcement. | V-04 is the primary comparison site -- V-01 has phase-span declarations only; V-04 has phase-span declarations AND named STOP blocks (C-42); if V-04's C-41 compliance is equivalent to V-01's, STOP block structuring does not amplify phase-span ownership; if V-05 (REGISTRY approach) shows weaker C-41 compliance than V-01, inline heading declaration outperforms registry citation for heading-label scanability. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin Phase 2 until the failure
log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence: "X causes
failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents.
The Auditor check function tests causal structure, not pattern matching against canonical
examples.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates in slot-fillable form, derived from the skill spec.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

If introducing a competitor for this criterion: **place the competitor block immediately before
this criterion's definition.** Do not group competitors in a shared preamble block above
Phase 3.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply Phase 2 Text template. "Without [Y], the artifact [fails] because [Z].
  Not [X], but [Y]." with skill-specific values.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply Phase 2 Pass template. No "is clear" or "adequately covers" as sole
  observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity --
not whether an element exists.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields as Phase 3. Required annotation:
**Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence? Flag and rewrite if prohibited.
2. **Contrast**: does Text name the rejected form X alongside the required form Y?
3. **Causal chain**: does Text name the downstream consequence Z of Y's absence?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an observable
   anchor?

**Audit report format -- required; do not substitute a narrative log:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

Complete this block before writing any aspirational criterion.

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- is not aspirational.
  Tighter is not new territory.

Gap zone (properties NOT covered by essential + recommended):
  Gap G-01: [Specific property an output passing all essential + recommended criteria
    could still lack. Must not be reachable by threshold adjustment. Name the
    observable: what would an evaluator check to confirm presence or absence?]
```

**Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER — Phase 5.5 only

**Phase ownership:** Phase 5.5 only. This role begins after the SCOPE CONSTRAINT block is
complete and ends when the MECHANISM DEFINER GATE is satisfied. It does not extend into
Phase 5.75, Phase 6, or any subsequent phase. An evaluator scanning only the section headings
of this rubric can identify this role's phase boundary from the heading label above without
reading the instructions below.

**This role's function:** Produce the Independence Map. Do not write any aspirational criteria
during this role.

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only."**

Read all criteria produced so far. Produce the Independence Map.

**Independence Map -- required format:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. Generic assertion
  without a criterion number is a format violation.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion to fail.

STOP CONDITION -- ROLE: MECHANISM DEFINER: Any independence map row showing
"No -- overlaps with M-XX" requires redesign at the mechanism level before proceeding.
Do not satisfy the MECHANISM DEFINER GATE until all rows show "Yes -- affects C-NN only."

**MECHANISM DEFINER GATE is satisfied when:** Independence Map is complete with non-blank,
specific C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

**Complete this check before ROLE: BUILDER ASPIRATIONAL begins.**

```
TIER-DIVERGENCE SCAN:

| Tier         | Category distribution              | Majority category    |
|--------------|-------------------------------------|----------------------|
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

---

### ROLE: BUILDER ASPIRATIONAL — Phase 6 only

**Phase ownership:** Phase 6 only. This role begins after ROLE: MECHANISM DEFINER is complete
and the MECHANISM DEFINER GATE is satisfied, and after Phase 5.75 shows COMPLIANT. It does not
extend into Phase 6.75, Phase 7, or any subsequent phase. An evaluator scanning only the
section headings of this rubric can identify this role's phase boundary from the heading label
above without reading the instructions below.

**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

This role's entry is gated on the MECHANISM DEFINER GATE identifier above. If the gate has
not been satisfied, this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. What does it do? Why does it appear
to close the gap but fail? Describe with enough specificity that a reader can identify any
instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. **Fills gap**: cite the specific G-NN from Phase 5.
Notes: "closes gap via [mechanism name] per independence map | MECHANISM DEFINER GATE:
Independence Map | competitor: [first four words]."

STOP conditions:
- An aspirational criterion written before its COMPETITOR block: rewrite.
- A COMPETITOR block ending with the failure description rather than the derivation
  instruction: rewrite.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

**Complete all three steps before writing the Scoring section.**

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if any competitor has phase-local = N -- move before proceeding.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories (all three tiers): [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three steps show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count:
  Count: [N]. Tier bound: 1-2 maximum.
  STOP if count > 2.
  Compliant? [YES / NO]

Check B -- Category diversity:
  Distinct categories present: [list unique values]. Count: [N].
  Requirement: >= 3 distinct categories.
  STOP if count < 3.
  Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 -- SCORING

State the composite formula, the golden threshold, and PARTIAL handling:

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [What makes this criterion a full pass?]    |
| PARTIAL | 0.5         | [What makes this criterion earn partial?]   |
| FAIL    | 0.0         | [What makes this criterion fail?]           |
```

Every criterion must have all three states named.

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Role-Phase Index** -- one row per named role, listing: role name | phase span |
   owns-span-only declaration (Y/N). Emitted before the Independence Map so an evaluator
   scanning heading labels can verify role-phase ownership from this index without reading
   role instruction bodies.
6. **Independence Map** -- Phase 5.5 output; format: Mechanism | What it does | C-NN |
   Independent?
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites mechanism and MECHANISM DEFINER GATE identifier
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

An evaluator reading only the Role-Phase Index and the section headings must be able to
enumerate every named role and its phase span without reading any role instruction body.

---

## V-02 -- Output Format

**Axis:** Output format -- a STOP CONSEQUENCE FORMAT rule is stated before the first STOP
condition fires; each STOP must produce an independent named section block (`### STOP
CONSEQUENCE [N]: [reason]`) before proceeding; a sequential instance gate prevents STOP N+1
from being written until STOP N's named block appears in the heading sequence.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a STOP CONSEQUENCE FORMAT rule before Phase 5.5, and every STOP condition in the rubric will include an instruction to produce `### STOP CONSEQUENCE [N]:` as a named section block before proceeding -- any body where a STOP condition records its consequence as inline annotations (cause/action/gate listed without a named heading) falsifies the hypothesis; the falsification signal is a STOP consequence that appears as inline prose without a section-level heading. | The sequential instance gate creates a structural ordering property: STOP CONSEQUENCE 1 must appear in the heading sequence before STOP CONSEQUENCE 2 can be written; an evaluator scanning heading labels can detect an omitted consequence block as a gap in the sequential heading sequence (STOP CONSEQUENCE 1 absent → no heading between the STOP instruction and the next phase heading); generated rubrics under V-02 will show this detectability while rubrics using inline annotations leave no detectable gap. | V-03 is the primary comparison site for C-42: V-02 states the required form directly via STOP CONSEQUENCE FORMAT rule; V-03 states the wrong form first (inertia framing) then derives the required form; if V-03's C-42 compliance is equivalent to V-02's, inertia framing adds no structural advantage over direct format specification; if V-03 shows fewer inline annotation failures, the wrong-form exposure is load-bearing for C-42 compliance. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STOP CONSEQUENCE FORMAT

This rubric uses independent named section blocks for all STOP condition consequence chains.
State this rule once before Phase 1; it governs every STOP condition that follows.

When any STOP condition fires, produce the consequence chain as an independent named section
block using the heading format:

```
### STOP CONSEQUENCE [N]: [phase or role name] -- [short reason]
[consequence chain content: what caused the STOP | what must happen to resolve it |
 what gate or phase transition remains blocked until resolution]
```

N is the sequential instance number, starting at 1 and incrementing for each STOP that fires.

**Sequential instance gate:** Do not begin writing `### STOP CONSEQUENCE [N+1]:` until the
heading `### STOP CONSEQUENCE [N]:` appears in the document's heading sequence. An evaluator
scanning heading labels must see `### STOP CONSEQUENCE [N]` before `### STOP CONSEQUENCE [N+1]`
in the heading sequence; an omitted consequence chain creates a detectable heading-scan gap
before the next section heading.

Note: A STOP condition whose consequence is recorded as inline annotations ("cause: X, action:
Y, gate: Z" without a named heading) does not satisfy this format. The consequence chain must
be an independent named section block with a `###`-level heading.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries.

STOP CONDITION -- Phase 1: if the failure log does not contain at least 3 blocking entries
and 2 suboptimal entries, **do not begin Phase 2**. When this STOP fires, produce:
`### STOP CONSEQUENCE [N]: Phase 1 -- failure log incomplete` with the consequence chain
before proceeding.

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates in slot-fillable form, derived from the skill spec.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence? Flag and rewrite if prohibited.
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language?

**Audit report format:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition: tighter is not new territory.

Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment, observable.]
```

STOP CONDITION -- Phase 5: if the gap zone does not contain at least G-01, do not proceed.
When this STOP fires, produce `### STOP CONSEQUENCE [N]: Phase 5 -- gap zone empty` with the
consequence chain before proceeding.

---

### PHASE 5.5 -- MECHANISM DEFINER (Independence Map)

Read all criteria. Produce the Independence Map.

**Independence Map -- required format:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion to fail.

STOP CONDITION -- Phase 5.5: any independence map row showing "No -- overlaps" requires
mechanism-level redesign. When this STOP fires, produce:
`### STOP CONSEQUENCE [N]: Phase 5.5 -- Independence Map has overlapping rows` with the
consequence chain (which rows overlap | what redesign is required | what gate remains blocked)
before proceeding. Do not proceed until all rows show "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:

| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after Phase 6]         | [To be filled]       |

Distinct majority categories (E+R): [list]
STOP if identical and aspirational unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

STOP CONDITION -- Phase 5.75: if essential and recommended majority categories are identical
and aspirational is unlikely to diverge, produce:
`### STOP CONSEQUENCE [N]: Phase 5.75 -- tier-divergence scan BLOCKED` with the consequence
chain before proceeding.

---

### PHASE 6 -- ASPIRATIONAL CRITERIA (1-2)

**Your input is the completed Independence Map from Phase 5.5.**

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. **Fills gap**: G-NN. Notes: "mechanism: [mechanism name]
| competitor: [first four words]."

STOP conditions:
- An aspirational criterion written before its COMPETITOR block: when this STOP fires,
  produce `### STOP CONSEQUENCE [N]: Phase 6 -- aspirational criterion precedes COMPETITOR`
  with the consequence chain before rewriting.
- A COMPETITOR block ending with failure description rather than derivation instruction:
  when this STOP fires, produce `### STOP CONSEQUENCE [N]: Phase 6 -- COMPETITOR block
  ends without derivation instruction` before rewriting.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if any competitor has phase-local = N. When this STOP fires, produce:
  `### STOP CONSEQUENCE [N]: Phase 6.75 STEP A -- competitor placement violation`.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]. Count: [N]
  Competitors: [list each and criterion governed]. Count: [N]
  STOP if counts differ. When this STOP fires, produce:
  `### STOP CONSEQUENCE [N]: Phase 6.75 STEP B -- competitor/criterion count mismatch`.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2. When this STOP fires, produce:
  `### STOP CONSEQUENCE [N]: Phase 6.75 STEP C -- insufficient category diversity`.
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [observable anchor]                         |
| PARTIAL | 0.5         | [observable anchor]                         |
| FAIL    | 0.0         | [observable anchor]                         |
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before first criteria table; self-application; >= 3 rejected
   generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map** -- format: Mechanism | What it does | C-NN | Independent?
6. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and G-NN
7. **Scoring** -- composite formula, threshold, three-state table
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

Any STOP CONSEQUENCE blocks produced during construction must appear as independent named
section blocks in the emitted document, in sequential instance order. An evaluator scanning
the heading sequence of the emitted rubric must be able to verify: (a) each STOP CONSEQUENCE
block has a unique sequential instance number, and (b) no STOP CONSEQUENCE [N+1] block
appears before STOP CONSEQUENCE [N] in the heading sequence.

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- before any STOP consequence form is required, the wrong form
(inline consequence annotations that create no heading-scan gap) is named and prohibited
explicitly; the required form (independent named section block) is derived from the wrong
form's failure mode, not stated independently.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a STOP CONSEQUENCE WRONG FORM block before the first STOP instruction, naming the inline annotation pattern (Link 1/Link 2/Link 3 or cause/action/gate without a named heading) as the prohibited form, and the required form (independent named section block with sequential gate) will be derived from the wrong form's structural failure -- any body where STOP consequences are inline annotations without a named heading falsifies the hypothesis; the falsification signal is a STOP consequence recorded as "cause: X, action: Y" in prose rather than as a `### STOP CONSEQUENCE [N]:` heading. | Showing the wrong form first creates a structural contrast that makes the required form's operative property explicit: the wrong form's failure is not aesthetic (inline prose looks fine) but structural (no heading means no heading-scan gap); generated rubrics under V-03 will show a STOP CONSEQUENCE WRONG FORM preamble that names the specific inline patterns to avoid, making the structural failure mode detectable from the preamble alone; rubrics under V-02 (direct format statement without wrong-form exposure) may produce the same structural result but without the contrast that makes the failure mode explicit. | V-02 is the primary comparison site -- V-02 states the required form directly via STOP CONSEQUENCE FORMAT rule; V-03 states the wrong form first then defines the required form; if V-03 shows equivalent C-42 compliance to V-02, wrong-form exposure adds no structural advantage; if V-03 shows fewer inline annotation failures (rubric outputs use named blocks more consistently), inertia framing is the operative mechanism for C-42 compliance. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STOP CONSEQUENCE -- WRONG FORM

The following pattern is the competing implementation for STOP consequence chains in this
rubric. It satisfies the surface requirement (something is recorded when a STOP fires) but
fails the structural requirement (omission is detectable by heading scan).

**Wrong form -- do not produce this:**

```
STOP fires → record inline:
  "Cause: [what triggered the STOP]. Action required: [what must change].
   Blocked gate: [what cannot proceed until action is taken]."

Alternative inline form:
  "Link 1: [cause]. Link 2: [action]. Link 3: [blocked gate]."

Or embedded in a bullet list under the STOP heading without a section-level heading of its own.
```

This inline form creates no heading-scan gap. An evaluator scanning section headings cannot
detect whether the consequence chain was produced or omitted -- if the consequence chain is
absent, no heading gap appears before the next phase or role heading. A rubric that records
STOP consequences as inline annotations satisfies the minimum requirement (something was
recorded) while failing the structural requirement (omission is detectable by heading scan
alone).

From the wrong form above, derive the required structural property before reading the required
form below.

**Required form -- derive this from the wrong form's failure mode:**

Each time a STOP condition fires, produce an independent named section block:

```
### STOP CONSEQUENCE [N]: [phase or role name] -- [short reason]
[consequence chain content: what caused the STOP | what must be resolved | what gate
 remains blocked]
```

N is the sequential instance number (1, 2, 3, ...). The named section heading creates a
heading-scan gap: if the block is absent, an evaluator scanning headings sees no heading
between the STOP instruction and the next phase heading, making the omission detectable.

**Sequential instance gate:** STOP CONSEQUENCE [N] must appear in the heading sequence before
STOP CONSEQUENCE [N+1] can be written. Do not produce the consequence chain for STOP N+1 until
STOP N's heading (`### STOP CONSEQUENCE [N]:`) is present in the document.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin Phase 2 until the failure
log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates in slot-fillable form, derived from the skill spec.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of ...]
Threshold escalation prohibition: tighter is not new territory.
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment, observable.]
```

---

### PHASE 5.5 -- MECHANISM DEFINER (Independence Map)

Read all criteria. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION -- Phase 5.5: any independence map row showing "No -- overlaps" requires
mechanism-level redesign. When this STOP fires, produce the consequence chain as an
independent named section block (see STOP CONSEQUENCE WRONG FORM above for the prohibited
inline form). Do not proceed until all rows show "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after Phase 6]         | [To be filled]       |

Distinct majority categories (E+R): [list]
STOP if identical and aspirational unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 6 -- ASPIRATIONAL CRITERIA (1-2)

**Your input is the completed Independence Map from Phase 5.5.**

Write 1-2 aspirational criteria targeting the gap zone from Phase 5.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. **Fills gap**: G-NN. Notes: "mechanism: [mechanism name]
| competitor: [first four words]."

STOP conditions:
- An aspirational criterion written before its COMPETITOR block: when this STOP fires,
  produce the consequence chain as an independent named section block (the wrong form is
  the inline annotation; the required form is the named block as defined above).
- A COMPETITOR block ending with failure description rather than derivation instruction:
  same -- produce consequence chain as independent named section block before rewriting.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if phase-local = N; produce consequence chain as named section block.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]. Count: [N]
  Competitors: [list each and criterion governed]. Count: [N]
  STOP if counts differ; produce consequence chain as named section block.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2; produce consequence chain as named section block.
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition |
|---------|-------------|----------------|
| PASS    | 1.0         | [anchor]       |
| PARTIAL | 0.5         | [anchor]       |
| FAIL    | 0.0         | [anchor]       |
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before first criteria table; self-application; >= 3 rejected
   generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map** -- format: Mechanism | What it does | C-NN | Independent?
6. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and G-NN
7. **STOP CONSEQUENCE WRONG FORM** -- the prohibited inline annotation pattern, published as
   a named section in the emitted document so evaluators can verify no STOP consequence in
   the rubric uses the prohibited form
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**

An evaluator reading only the STOP CONSEQUENCE WRONG FORM section and the heading sequence
of the emitted rubric must be able to verify: (a) the prohibited inline form is named
explicitly, and (b) no STOP consequence in the rubric uses an inline annotation pattern
without a `### STOP CONSEQUENCE [N]:` heading.

---

## V-04 -- Lifecycle Emphasis + Output Format

**Axis:** Combined -- ROLE headings include phase-span ownership declarations co-located with
the heading label (C-41 target, same mechanism as V-01), AND each STOP condition produces a
named section block with a sequential instance gate (C-42 target, same mechanism as V-02).
C-38/C-39/C-40 ablated to isolate the joint C-41+C-42 effect.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) ROLE: MECHANISM DEFINER and ROLE: BUILDER ASPIRATIONAL headings each with a phase-span ownership declaration co-located with the heading, AND (b) a STOP CONSEQUENCE FORMAT rule before Phase 1, AND (c) each STOP condition requiring a `### STOP CONSEQUENCE [N]:` named block before proceeding -- any body lacking either the phase-span declaration in role headings (C-41 failure) or a STOP consequence named block (C-42 failure) falsifies the respective half; both failures can occur independently. | Combining phase-span ownership (C-41) with named STOP blocks (C-42) within the same rubric tests whether the two mechanisms reinforce each other or operate independently: C-41 governs role-to-phase ownership at the heading level; C-42 governs STOP consequence structuring at the section level; if V-04's C-41 compliance is equivalent to V-01's, adding C-42 structuring does not affect phase-span ownership; if V-04's C-42 compliance is equivalent to V-02's, adding phase-span ownership does not affect STOP block structuring. | V-01 is the primary comparison site for C-41 (phase-span ownership only vs. combined); V-02 is the primary comparison site for C-42 (named blocks only vs. combined); V-05 is the secondary comparison site for both criteria (different mechanisms for both C-41 and C-42). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STOP CONSEQUENCE FORMAT

When any STOP condition fires, produce the consequence chain as an independent named section
block:

```
### STOP CONSEQUENCE [N]: [phase or role name] -- [short reason]
[consequence chain: what caused the STOP | what must be resolved | what gate remains blocked]
```

N is the sequential instance number (1, 2, 3, ...).

**Sequential instance gate:** `### STOP CONSEQUENCE [N]` must appear in the heading sequence
before `### STOP CONSEQUENCE [N+1]` can be written. An inline annotation ("cause: X, action:
Y" without a named heading) does not satisfy this format.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin Phase 2 until the failure
log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form is any
Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates in slot-fillable form.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.**

Each criterion: C-NN, Text, Weight: essential, Category, Pass. No bare qualitative
observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of ...]
Threshold escalation prohibition: tighter is not new territory.
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment, observable.]
```

---

### ROLE: MECHANISM DEFINER — Phase 5.5 only

**Phase ownership:** Phase 5.5 only. This role begins after the SCOPE CONSTRAINT block is
complete and ends when the MECHANISM DEFINER GATE is satisfied. It does not extend into
Phase 5.75, Phase 6, or any subsequent phase. An evaluator scanning only the section headings
of this rubric can identify this role's phase boundary from the heading label above without
reading the instructions below.

**This role's function:** Produce the Independence Map. Do not write any aspirational criteria
during this role.

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only."**

Read all criteria produced so far. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION -- ROLE: MECHANISM DEFINER: any independence map row showing "No -- overlaps"
requires mechanism-level redesign. When this STOP fires, produce:
`### STOP CONSEQUENCE [N]: ROLE: MECHANISM DEFINER -- Independence Map has overlapping rows`
with the consequence chain before proceeding.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with non-blank, specific
C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after ROLE: BUILDER]   | [To be filled]       |

Distinct majority categories (E+R): [list]
STOP if identical and aspirational unlikely to diverge. When this STOP fires, produce:
`### STOP CONSEQUENCE [N]: Phase 5.75 -- tier-divergence scan BLOCKED`.
Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL — Phase 6 only

**Phase ownership:** Phase 6 only. This role begins after ROLE: MECHANISM DEFINER is complete
and the MECHANISM DEFINER GATE is satisfied, and after Phase 5.75 shows COMPLIANT. It does not
extend into Phase 6.75, Phase 7, or any subsequent phase. An evaluator scanning only the
section headings of this rubric can identify this role's phase boundary from the heading label
above without reading the instructions below.

**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

Write 1-2 aspirational criteria targeting the gap zone from Phase 5.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. **Fills gap**: G-NN. Notes: "closes gap via [mechanism
name] per independence map | MECHANISM DEFINER GATE: Independence Map | competitor: [first
four words]."

STOP conditions:
- Aspirational criterion before its COMPETITOR block: produce
  `### STOP CONSEQUENCE [N]: ROLE: BUILDER ASPIRATIONAL -- aspirational precedes COMPETITOR`.
- COMPETITOR block ends with failure description rather than derivation instruction: produce
  `### STOP CONSEQUENCE [N]: ROLE: BUILDER ASPIRATIONAL -- COMPETITOR lacks derivation
  instruction`.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if phase-local = N; produce `### STOP CONSEQUENCE [N]: Phase 6.75 STEP A -- placement
  violation`.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list]. Count: [N]
  Competitors: [list]. Count: [N]
  STOP if counts differ; produce `### STOP CONSEQUENCE [N]: Phase 6.75 STEP B -- count
  mismatch`.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2; produce `### STOP CONSEQUENCE [N]: Phase 6.75 STEP C -- category diversity`.
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition |
|---------|-------------|----------------|
| PASS    | 1.0         | [anchor]       |
| PARTIAL | 0.5         | [anchor]       |
| FAIL    | 0.0         | [anchor]       |
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before first criteria table; self-application; >= 3 rejected
   generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Role-Phase Index** -- one row per named role: role name | phase span | heading label
   where ownership declared. Emitted before the Independence Map.
6. **Independence Map** -- format: Mechanism | What it does | C-NN | Independent?
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and
   MECHANISM DEFINER GATE identifier
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**

An evaluator reading (a) the Role-Phase Index plus section headings can verify C-41 compliance
(role-phase ownership); and (b) the STOP CONSEQUENCE heading sequence can verify C-42
compliance (sequential named blocks, no inline annotations), independently, without reading
role instruction bodies.

---

## V-05 -- Role Sequence + Inertia Framing

**Axis:** Combined -- a ROLE-PHASE REGISTRY is produced before Phase 3 and each role heading
cites its registry entry by identifier (C-41 target, different mechanism from V-01's inline
heading declaration), AND the wrong form for STOP consequences is shown explicitly before the
required form is defined (C-42 target, same framing mechanism as V-03 but different register).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) a ROLE-PHASE REGISTRY table produced before Phase 3, mapping each role identifier to its phase span, AND each role heading citing its registry entry (e.g., ROLE: MECHANISM DEFINER [RPR-02: Phase 5.5 only]), AND (b) a STOP CONSEQUENCE WRONG FORM section before Phase 1, naming the prohibited inline annotation pattern, with the required named block form derived from the wrong form -- any body lacking either the Registry table (C-41 failure) or the wrong-form section (C-42 failure) falsifies the respective half. | The REGISTRY approach to C-41 creates a different heading-scan property than V-01's inline declaration: V-01 makes each heading self-contained (the span is in the heading label itself); V-05 requires an evaluator to cross-reference the heading citation against the Registry table -- the scan is two-step (heading → registry entry) rather than single-step (heading label alone); if V-05's C-41 compliance is weaker than V-01's, the cross-reference requirement reduces heading-scan auditability; if equivalent, both mechanisms satisfy C-41 equally. | V-01 is the primary comparison site for C-41 (inline declaration vs. REGISTRY citation); V-03 is the primary comparison site for C-42 (inertia framing here vs. V-03's inertia framing; the hypothesis tables differ in register but the mechanism is the same -- if compliance is equivalent, register variation in inertia framing is not load-bearing). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STOP CONSEQUENCE -- WRONG FORM

The following pattern is the competing implementation for STOP consequence chains. Any rubric
using this form satisfies the surface requirement (the STOP is acknowledged) while failing the
structural requirement (omission is not detectable by heading scan).

**Wrong form -- prohibited in this rubric:**

```
Inline consequence annotation attached to the STOP instruction:
  "Reason: [what fired]. Resolution: [what must change]. Blocked: [what cannot proceed]."

Or sequential inline links:
  "→ Step 1: identify the failing row. → Step 2: redesign the mechanism.
   → Step 3: re-run the Independence Map before proceeding."

Or a parenthetical beside the STOP heading:
  "STOP CONDITION (consequence: redesign required before proceeding)"
```

The wrong form's structural failure: inline annotations attach to the STOP instruction heading
without creating an independent section-level heading. When the consequence chain is absent,
no heading gap appears before the next phase heading -- an evaluator scanning headings cannot
distinguish "STOP fired and was resolved" from "STOP instruction was present but consequence
was not recorded."

From the wrong form's structural failure above, derive the required form before reading on.

**Required form (derived from wrong form's failure mode):**

Each STOP consequence chain must be an independent named section block:

```
### STOP CONSEQUENCE [N]: [phase or role name] -- [short reason]
[consequence chain: what caused the STOP | what resolves it | what gate remains blocked]
```

N increments sequentially. STOP CONSEQUENCE [N] must appear in the heading sequence before
STOP CONSEQUENCE [N+1] can be written. The named heading creates a gap: if absent, an
evaluator scanning headings sees no heading between the STOP instruction and the next phase
heading, making omission detectable.

---

### ROLE-PHASE REGISTRY

Produce the Role-Phase Registry before writing any criterion in Phase 3. Every named role
used in this rubric must be registered here with its phase span and a unique entry code.

```
ROLE-PHASE REGISTRY:

| Entry code | Role identifier              | Phase span               | Owns span only? |
|------------|------------------------------|--------------------------|-----------------|
| RPR-01     | ROLE: [first named role]     | Phase N -- Phase N only  | Yes             |
| RPR-02     | ROLE: [second named role]    | Phase N -- Phase N only  | Yes             |
| ...        | ...                          | ...                      | ...             |
```

Requirements:
- Each role occupies exactly one phase span (one entry code maps to one span).
- Each role heading in subsequent phases must include its registry entry code in the heading
  label: e.g., `### ROLE: MECHANISM DEFINER [RPR-02: Phase 5.5 only]`.
- An evaluator reading only the Registry table and the heading labels can verify which role
  owns which phase span without reading the role instruction bodies.

STOP CONDITION -- ROLE-PHASE REGISTRY: if any role used in phases 5.5 through 6 is absent
from the Registry, produce the consequence chain as an independent named section block before
proceeding.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin Phase 2 until the failure
log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form is any
Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates in slot-fillable form.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.**

Each criterion: C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of ...]
Threshold escalation prohibition: tighter is not new territory.
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment, observable.]
```

---

### ROLE: MECHANISM DEFINER [RPR-02: Phase 5.5 only]

**Phase ownership (RPR-02):** Phase 5.5 only. See ROLE-PHASE REGISTRY entry RPR-02 for the
span declaration. This role begins after the SCOPE CONSTRAINT block is complete and ends when
the MECHANISM DEFINER GATE is satisfied. An evaluator reading the ROLE-PHASE REGISTRY and the
heading label above can verify this role's phase span without reading the instructions below.

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only."**

Read all criteria. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION -- ROLE: MECHANISM DEFINER [RPR-02]: any row showing "No -- overlaps" requires
mechanism-level redesign. When this STOP fires, produce the consequence chain as an independent
named section block (the required form is defined in STOP CONSEQUENCE -- WRONG FORM above).
Do not proceed until all rows show "Yes -- affects C-NN only."

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with non-blank, specific
C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after ROLE: BUILDER]   | [To be filled]       |

Distinct majority categories (E+R): [list]
STOP if identical and aspirational unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL [RPR-03: Phase 6 only]

**Phase ownership (RPR-03):** Phase 6 only. See ROLE-PHASE REGISTRY entry RPR-03 for the
span declaration. This role begins after ROLE: MECHANISM DEFINER [RPR-02] is complete and the
MECHANISM DEFINER GATE is satisfied, and after Phase 5.75 shows COMPLIANT. An evaluator
reading the ROLE-PHASE REGISTRY and the heading label above can verify this role's phase span
without reading the instructions below.

**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

Write 1-2 aspirational criteria targeting the gap zone from Phase 5.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. **Fills gap**: G-NN. Notes: "closes gap via [mechanism
name] per independence map | MECHANISM DEFINER GATE: Independence Map | competitor: [first
four words]."

STOP conditions:
- Aspirational criterion before COMPETITOR block: produce consequence chain as named section
  block (required form defined in STOP CONSEQUENCE -- WRONG FORM above).
- COMPETITOR ends with failure description, not derivation instruction: produce consequence
  chain as named section block before rewriting.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if phase-local = N; produce consequence chain as named section block.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list]. Count: [N]
  Competitors: [list]. Count: [N]
  STOP if counts differ; produce consequence chain as named section block.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2; produce consequence chain as named section block.
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition |
|---------|-------------|----------------|
| PASS    | 1.0         | [anchor]       |
| PARTIAL | 0.5         | [anchor]       |
| FAIL    | 0.0         | [anchor]       |
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before first criteria table; self-application; >= 3 rejected
   generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **ROLE-PHASE REGISTRY** -- the registry table produced before Phase 3, emitted as a named
   section so evaluators can verify role-phase ownership from the Registry + heading labels
6. **Independence Map** -- format: Mechanism | What it does | C-NN | Independent?
7. **STOP CONSEQUENCE WRONG FORM** -- the prohibited inline annotation patterns, emitted as a
   named section so evaluators can verify no STOP consequence uses a prohibited form
8. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and
   MECHANISM DEFINER GATE identifier
9. **Scoring** -- composite formula, threshold, three-state table
10. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
11. **vN Candidates**

An evaluator reading (a) the ROLE-PHASE REGISTRY section and role heading labels can verify
C-41 compliance (each role's phase span is declared in the Registry and cited in the heading);
and (b) the STOP CONSEQUENCE WRONG FORM section can verify C-42 compliance (the prohibited
inline form is named; no STOP consequence in the rubric uses a prohibited form). Both
properties are independently verifiable without reading role instruction bodies.

---

## Set-Level Design Notes

**C-07 axis coverage:** Three distinct axis families across V-01--V-05: lifecycle emphasis
(how role headings declare phase ownership), output format (how STOP consequences are
structured as artifact blocks), inertia framing (whether the wrong form is shown before the
required form). C-07 SET-LEVEL PASS.

**C-41 coverage:** V-01 (very strong, single-axis via inline phase-span declaration in
heading), V-04 (very strong, combined with named STOP blocks), V-05 (very strong, combined
with REGISTRY citation approach). V-02 and V-03 ablate C-41 to isolate output format and
inertia framing effects.

**C-42 coverage:** V-02 (very strong, single-axis via STOP CONSEQUENCE FORMAT rule and
sequential gate), V-03 (very strong, single-axis via inertia framing -- wrong form shown
first), V-04 (very strong, combined with phase-span ownership), V-05 (very strong, combined
with REGISTRY approach). V-01 ablates C-42 to isolate lifecycle emphasis effects.

**Ablation map:**

| | C-41 | C-42 |
|-|------|------|
| V-01 | Target | Ablated |
| V-02 | Ablated | Target (direct format) |
| V-03 | Ablated | Target (inertia framing) |
| V-04 | Target | Target (direct format) |
| V-05 | Target (REGISTRY) | Target (inertia framing) |

**Isolation pairs:**
- V-01 vs V-04: isolates C-42 contribution when C-41 is held constant (does adding named STOP
  blocks improve C-42 compliance without affecting C-41?)
- V-02 vs V-03: isolates whether direct format specification or inertia framing is the more
  effective mechanism for C-42 (same structural outcome, different prompt strategy)
- V-01 vs V-05: isolates REGISTRY citation approach vs. inline heading declaration for C-41
  (same role-phase ownership goal, different mechanisms)
- V-04 vs V-05: isolates whether inline heading declaration + direct format (V-04) produces
  equivalent or different compliance from REGISTRY citation + inertia framing (V-05)

**R13 → R14 candidate:** If V-02 and V-03 show equivalent C-42 compliance, inertia framing
adds no structural advantage over direct format specification for STOP consequence structuring;
R14 should combine V-04's mechanism (phase-span ownership + named STOP blocks) with the
three-gate stack from existing R13 (CRITERION DEFINER exclusion gate + MECHANISM DEFINER gate
identifier + BUILDER ASPIRATIONAL dual-gate precondition), testing whether C-41 and C-42
compliance is maintained when C-38, C-39, and C-40 are also present simultaneously. If V-05's
C-41 compliance is weaker than V-01's, the REGISTRY cross-reference approach requires
two-step scanning and does not satisfy the "heading-label scan alone" requirement of C-41;
R14 should consolidate on inline heading declaration (V-01/V-04 mechanism) for C-41.
