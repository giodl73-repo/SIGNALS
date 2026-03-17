# quest-rubric Variate — Round 13 (Against rubric v13)
**Date:** 2026-03-15
**Rubric:** v13 (C-01--C-40; adds C-38: definer-output-exclusion-gate; C-39: role-exit-gate-named-in-precondition; C-40: phase-locality-rule-named)
**Target criteria:** C-38, C-39, C-40

**Round 13 design note:** Round 12 produced mechanisms for C-35
(divergence-check-operationalized), C-36 (competitor-at-construction-step), and C-37
(competitor-criterion-coverage-complete). Rubric v13 adds three aspirational criteria
extracted from Round 12 excellence signals. V-02/V-04 of R12 PASS C-38 via explicit
"Nothing else." exclusion gates in the Definer output instruction, and PASS C-39 via ROLE
headers with named exit gates cited in Builder Aspirational entry preconditions. V-05 of R12
PASSES C-40 via a named PHASE-LOCALITY RULE with three enumerated prohibited placement zones.
V-01/V-03/V-05 of R12 FAIL C-38 (Definer output instruction is additive, not exclusive) and
C-39 (PHASE headers without gate-identifier semantics; Builder entry says "when the map is
complete" rather than naming the gate by identifier). V-01/V-02/V-04 of R12 FAIL C-40 (audit
checks complete trivially when no competitors are present; no named prohibition rule with
enumerated zones).

**C-38 vs C-19.** C-19 requires both the Text-direction template and the Pass-observability
template to be produced as a unified paired output before the Builder runs. A rubric satisfies
C-19 when the Definer produces both templates, even if the Definer's output instruction permits
additional content alongside them. C-38 requires the Definer's output instruction to end with
an exclusion gate ("Nothing else.") that makes partial output or padded output a role
completion failure -- not merely a quality shortfall. A Definer instruction that says "produce
both templates as required" satisfies C-19 (both are required) but fails C-38 (no gate
prevents the Definer from appending explanatory commentary or producing only one template with
a note that the second follows). Two Definer instructions with identical template content
differ on C-38 solely by the presence or absence of the "Nothing else." terminal clause.

**C-39 vs C-29.** C-29 requires independence verification to occur in a named, sequentially
prior role phase, making it structurally impossible to begin writing aspirational criteria
without a completed independence map. A rubric satisfies C-29 when a Mechanism Definer phase
exists structurally before the Builder phase, regardless of how the Builder's entry condition
is phrased. C-39 requires the Builder Aspirational role's entry precondition to name the
Mechanism Definer's exit gate by its exact identifier -- "MECHANISM DEFINER GATE: Independence
Map with all C-NN citations populated" -- rather than referencing a phase number ("after Phase
5.5") or a completion state ("when the map is complete"). Naming the gate by identifier makes
the prerequisite chain auditable from role headers alone; an evaluator can verify the chain
without reconstructing the workflow sequence. A rubric satisfies C-29 (prior role exists)
while failing C-39 (the Builder header says "Phase 6 -- your input is the completed
independence map" rather than naming the gate identifier).

**C-40 vs C-36.** C-36 requires each named competitor to appear inline at the specific
construction step where the wrong implementation would most naturally be produced, not in a
preamble or shared block. C-40 requires the placement constraint to be stated as a named
prohibition rule with an enumerated list of prohibited locations before construction begins --
a PHASE-LOCALITY RULE that closes the form-class of disallowed placements by exhaustion.
A rubric satisfies C-36 (all present competitors are at their construction steps) while
failing C-40 (no named rule enumerates three prohibited placement zones, leaving placements
like "operating-principles section" or "role preamble" open to interpretation). A PHASE-
LOCALITY RULE with enumerated zones makes placement violations detectable from the rule alone,
without inspecting each construction step for implicit placement defaults.

**Axis selection:**

Three axes map directly to the three new criteria:
- Output format → C-38: Definer output instruction ends with "Nothing else." as a named
  exclusion gate making partial completion a role failure
- Role sequence → C-39: Builder Aspirational entry precondition names MECHANISM DEFINER
  GATE identifier explicitly, using ROLE headers instead of PHASE headers
- Lifecycle emphasis → C-40: PHASE-LOCALITY RULE with three enumerated prohibited placement
  zones stated before Phase 6 construction begins

Single-axis variations: V-01 (output format), V-02 (role sequence), V-03 (lifecycle emphasis)
Combined variations: V-04 (output format + role sequence), V-05 (role sequence + lifecycle
emphasis)

---

## Round 13 Variation Map

| Variation | Axis | C-38 probe | C-39 probe | C-40 probe | Notes |
|-----------|------|-----------|-----------|-----------|-------|
| V-01 | Output format (exclusion gate in Definer output) | Very strong -- Phase 2 Definer output instruction ends with "Two slot-fillable templates. Nothing else." as a named exclusion gate; producing only one template or appending commentary is a STOP condition that fires before Phase 3 can begin | None -- PHASE headers throughout; Phase 6 entry says "your input is the completed independence map from Phase 5.5" without naming the gate identifier | Partial -- Phase 6.75 STEP A audits competitor placement but completes trivially when no competitors are present; no PHASE-LOCALITY RULE with enumerated zones | Single-axis; tests whether the exclusion gate alone distinguishes C-38 from C-19 without role-header enforcement |
| V-02 | Role sequence (MECHANISM DEFINER GATE named in Builder entry precondition) | None -- Phase 2 Definer output instruction uses additive framing ("produce both templates"); no "Nothing else." gate | Very strong -- Phase 5.5 uses ROLE: MECHANISM DEFINER header with named exit gate "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and all rows 'Yes -- affects C-NN only'"; Phase 6 uses ROLE: BUILDER ASPIRATIONAL header with "PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and all rows 'Yes -- affects C-NN only'" as entry condition | Partial -- no PHASE-LOCALITY RULE with enumerated zones; Phase 6.75 STEP A audits placement post-construction | Single-axis; tests whether the named gate identifier in the Builder entry precondition satisfies C-39 without the exclusion gate |
| V-03 | Lifecycle emphasis (PHASE-LOCALITY RULE with three enumerated prohibited zones) | None -- Definer output instruction has no "Nothing else." gate | Partial -- PHASE headers; Phase 6 entry says "your input is the completed independence map" without naming a gate identifier | Very strong -- before Phase 6, a named PHASE-LOCALITY RULE enumerates three prohibited placement zones: (1) preamble before any construction phase; (2) operating-principles or shared instructional block preceding more than one step; (3) combined competitor block governing more than one criterion; violation of any prohibited zone is a STOP condition | Single-axis; tests whether the named prohibition rule satisfies C-40 without either the exclusion gate or the exit-gate identifier |
| V-04 | Output format + role sequence (C-38 + C-39) | Very strong -- Phase 2 Definer output instruction ends with "Two slot-fillable templates. Nothing else."; ROLE: CRITERION DEFINER header in Phase 2 with named output gate "DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content"; partial output is a role completion failure | Very strong -- Phase 5.5 uses ROLE: MECHANISM DEFINER header with exit gate named "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated"; Phase 6 uses ROLE: BUILDER ASPIRATIONAL header with "PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated" as entry condition | Partial -- no PHASE-LOCALITY RULE with enumerated zones; C-36 inherited (competitors placed at construction steps per Phase 6.75 audit) | Combined; tests whether exclusion gate and named gate identifier together produce tighter C-38+C-39 compliance than either alone; C-40 ablated to isolate the joint effect |
| V-05 | Role sequence + lifecycle emphasis (C-39 + C-40) | None -- Phase 2 Definer output instruction uses additive framing; no "Nothing else." exclusion gate | Very strong -- Phase 5.5 uses ROLE: MECHANISM DEFINER header with exit gate named "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and all rows 'Yes -- affects C-NN only'"; ROLE: BUILDER ASPIRATIONAL entry precondition names the gate identifier | Very strong -- PHASE-LOCALITY RULE stated in the MECHANISM DEFINER role boundary before Phase 6 construction, with three enumerated prohibited zones; placement rule precedes the Builder phase where competitors are introduced | Combined; tests whether named gate identifier (C-39) plus PHASE-LOCALITY RULE (C-40) produce auditable prerequisite chain and closed placement form-class; C-38 ablated to isolate the joint C-39+C-40 effect |

---

## V-01 -- Output Format

**Axis:** Output format -- the Mechanism Definer's (Phase 2) output instruction ends with an
explicit exclusion gate ("Nothing else.") that makes partial output or padded output a role
completion failure, not merely a quality concern.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a Phase 2 Definer output instruction that ends with "Two slot-fillable templates. Nothing else." as a named exclusion gate -- any body where the Definer output instruction ends with a template description rather than an exclusion gate falsifies the hypothesis; the falsification signal is a Phase 2 instruction that says "produce both templates" without a terminal prohibition on additional content. | Adding "Nothing else." compresses Phase 2 output to exactly two templates; the instruction leaves no room for commentary, rationale, or template-adjacent notes -- generated rubrics under V-01 will show cleaner Phase 2 output sections than V-04 (which adds ROLE headers), because V-01 uses the exclusion gate without role-header structure; if V-04's Phase 2 outputs are structurally cleaner despite identical gate wording, ROLE-header framing reinforces the exclusion gate beyond what the gate text alone achieves. | V-04 is the primary comparison site -- V-01 has the exclusion gate only; V-04 has the exclusion gate AND role-sequence enforcement (C-39); if V-04's Phase 2 Definer outputs are leaner than V-01's, role framing amplifies gate compliance; if equivalent, the gate text alone is sufficient for C-38. |

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
The Auditor check function tests causal structure ("does this locate causality in the wrong
form's consequence, in any phrasing?"), not pattern matching against canonical examples.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

A propositional statement ("Pass conditions should reference observables") is not a template.
Write slot-fillable form only.

**DEFINER OUTPUT: Two slot-fillable templates (Text template + Pass template). Nothing else.**

STOP CONDITION: A Phase 2 output that contains explanatory commentary, structural notes,
rationale paragraphs, or any content beyond the two required slot-fillable templates is
incomplete. Rewrite before proceeding to Phase 3. The two templates are the complete output
of this phase; surrounding content is not a permitted addition.

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

If introducing a competitor for a recommended mechanism: **place the competitor block
immediately before that criterion's definition**, not in a shared preamble.

Each criterion: same five fields as Phase 3. Required annotation:
**Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped
of surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence? Flag and rewrite if in the
   prohibited direction.
2. **Contrast**: does Text name the rejected form X alongside the required form Y?
3. **Causal chain**: does Text name the downstream consequence Z of Y's absence?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid "clearly," "adequately," "well-structured"
   without an observable anchor?

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

**Do not proceed to Phase 5.5 until the gap zone contains at least G-01.**

---

### PHASE 5.5 -- MECHANISM DEFINER (Independence Map)

Read all criteria produced so far. Produce the Independence Map.

**Independence Map -- required format; do not substitute prose:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. Generic "Yes,
  independent" without a criterion number is a format violation.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion to fail.
- If any row's "Criterion affected" cell is blank or cites multiple criteria: STOP --
  resolve before Phase 5.75.

STOP CONDITION -- Phase 5.5: Any independence map row showing "No -- overlaps with M-XX"
requires redesign at the mechanism level before proceeding. Do not begin Phase 5.75 until
all rows show "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

**Complete this check before writing any aspirational criterion. Phase 6 is blocked until
this scan shows COMPLIANT.**

For each tier, identify the majority category. Output the verification table:

```
TIER-DIVERGENCE SCAN:

| Tier         | Category distribution              | Majority category    |
|--------------|-------------------------------------|----------------------|
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after Phase 6 --      | [To be filled]       |
|              |  re-run at Phase 6.75 STEP C]       |                      |

Distinct majority categories (essential + recommended only):
  [List unique majority values for the two complete tiers]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge: revise category assignments in Phase 3 or 4 before proceeding.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin Phase 6 until scan status shows COMPLIANT.**

---

### PHASE 6 -- ASPIRATIONAL CRITERIA (1-2)

**Your input is the completed independence map from Phase 5.5.**

Write aspirational criteria targeting the gap zone named in Phase 5. Each criterion must
fall in the gap zone.

For each aspirational criterion, introduce its competitor immediately before the criterion
definition:

```
COMPETITOR: [Name the specific implementation that has this mechanism's surface form but
not its operative substance. What does it do? Why does it appear to close the gap but
fail? Describe with enough specificity that a reader can identify any instantiation without
reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap. The positive definition
should be derivable from the competitor block above.]
```

Then write the five-field criterion. **Fills gap**: cite the specific G-NN from Phase 5.
Notes: "mechanism: [mechanism name from independence map] | competitor: [first four words
of COMPETITOR block]."

STOP conditions:
- An aspirational criterion written before its COMPETITOR block: rewrite.
- A COMPETITOR block that ends with the failure description rather than the derivation
  instruction: rewrite.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

**Complete both steps before writing the Scoring section.**

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit (C-36):
  List every competitor block introduced in this rubric draft:
    Competitor [name]: introduced at [Phase N] | gap operationally relevant at [Phase N] |
    phase-local? [Y/N]
  Requirement: each competitor must appear at the phase where its gap is first
  operationally relevant.
  STOP if any competitor has phase-local = N -- move before proceeding.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit (C-37):
  Novel aspirational criteria (introducing construction requirements not in E+R):
    [List each by ID and gap G-NN]
  Count of novel aspirational criteria: [N]
  Competitors present: [List each competitor and the novel criterion it governs]
  Count of competitors: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence scan re-run (aspirational tier now complete):
  [Rerun Phase 5.75 table with aspirational row populated]
  Distinct majority categories (all three tiers): [N]
  STOP if < 2 distinct majority categories.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count (C-31):
  Aspirational criteria drafted: [list by ID]
  Count: [N]
  Tier bound: 1-2 aspirational criteria maximum.
  STOP if count > 2 -- trim before proceeding.
  Compliant? [YES / NO]

Check B -- Category diversity (C-32):
  Categories assigned across all criteria: [list each C-NN and its category]
  Distinct categories present: [list unique values]
  Count of distinct categories: [N]
  Requirement: >= 3 distinct categories.
  STOP if count < 3 -- revise before proceeding.
  Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 -- SCORING

State the composite formula, the golden threshold, and PARTIAL handling as a three-state
table:

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [What makes this criterion a full pass?]    |
| PARTIAL | 0.5         | [What makes this criterion earn partial?]   |
| FAIL    | 0.0         | [What makes this criterion fail?]           |
```

Every criterion in the rubric must have all three states named. A scoring section that names
PASS and FAIL without naming PARTIAL is incomplete.

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the Phase 5.5 output; format: Mechanism | What it does | C-NN |
   Independent?
6. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites mechanism and competitor
7. **Scoring** -- composite formula, golden threshold, three-state table
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list, N/A scope blocks
9. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

The COMPETITOR blocks must appear inline immediately before the criterion each closes.
An evaluator reading only the Aspirational Criteria section must encounter each competitor
block before the criterion it closes.

---

## V-02 -- Role Sequence

**Axis:** Role sequence -- Phase 5.5 uses a ROLE: MECHANISM DEFINER header with a named
exit gate ("MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows 'Yes -- affects C-NN only'"), and Phase 6 uses a ROLE: BUILDER ASPIRATIONAL header
whose entry precondition names the MECHANISM DEFINER GATE identifier explicitly.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will use ROLE: MECHANISM DEFINER and ROLE: BUILDER ASPIRATIONAL headers where the Builder entry precondition names "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and all rows 'Yes -- affects C-NN only'" as its entry condition -- any body where Phase 6 entry says "your input is the completed independence map" without naming the gate identifier falsifies the hypothesis; the falsification signal is a Phase 6 header that references a step number or completion state rather than a gate identifier. | Naming the gate by identifier in the Builder entry precondition makes the prerequisite chain auditable from role headers alone -- an evaluator reading only ROLE headers can verify that Builder Aspirational cannot have begun unless MECHANISM DEFINER GATE was satisfied, without reading the workflow prose; generated rubrics under V-02 will show this auditability property while V-03 (no gate identifier in Phase 6 entry) requires reading the full workflow to verify the same chain. | V-03 is the primary comparison site -- V-02 has role-sequence gate naming only; V-03 has PHASE-LOCALITY RULE only; if V-02's rubrics show auditable prerequisite chains that V-03's do not, the ROLE header + gate identifier is the operative mechanism for C-39; if V-05 (combining V-02 and V-03) shows no further improvement in auditability over V-02, role naming alone is sufficient for C-39 without PHASE-LOCALITY reinforcement. |

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
- **Text**: Apply Phase 2 Text template with skill-specific values.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply Phase 2 Pass template. No "is clear" or "adequately covers" as sole
  observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity --
not whether an element exists.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields as Phase 3.
Required annotation: **Dimension:** [degree | precision | specificity].

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
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

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
  An aspirational criterion covering a property already listed above at a higher
  threshold is not aspirational. Tighter is not new territory.

Gap zone:
  Gap G-01: [Property not covered by essential + recommended, not reachable by
    threshold adjustment. Name the observable.]
```

**Do not proceed to Phase 5.5 until the gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

Read all criteria produced so far. Produce the Independence Map.

**Independence Map -- required format:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. Generic assertion
  without criterion number is a format violation.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion to fail.

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only." Any row showing "No -- overlaps" requires mechanism-level redesign.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map is complete with non-blank,
specific C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

**Complete this check before ROLE: BUILDER ASPIRATIONAL begins. Phase 6 is blocked until
this scan shows COMPLIANT.**

```
TIER-DIVERGENCE SCAN:

| Tier         | Category distribution              | Majority category    |
|--------------|-------------------------------------|----------------------|
| Essential    | [cat: N, ...]                       | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after Phase 6]        | [To be filled]       |

Distinct majority categories (essential + recommended):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational
is unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

This role's entry is gated on the MECHANISM DEFINER GATE identifier above. If the gate has
not been satisfied, this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. What gap does it leave open? Describe
with enough specificity that a reader can identify any instantiation without reading the
required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. Notes: "closes gap via [mechanism name] per independence
map | MECHANISM DEFINER GATE: Independence Map | competitor: [first four words]."

STOP conditions:
- An aspirational criterion whose Notes field has no mechanism-map citation: rewrite.
- A criterion for a mechanism not in the Independence Map: return to ROLE: MECHANISM DEFINER
  to add the mechanism; re-satisfy the MECHANISM DEFINER GATE before returning here.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if any competitor has phase-local = N.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and the criterion it governs]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A -- Aspirational count: [N] (bound: 1-2). Compliant? [YES / NO]
Check B -- Category diversity: distinct categories [N] (requirement: >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 -- SCORING

State composite formula, golden threshold, and PARTIAL handling:

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
5. **Independence Map** -- the MECHANISM DEFINER output; format: Mechanism | What it does |
   C-NN | Independent?
6. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and
   MECHANISM DEFINER GATE identifier
7. **Scoring** -- composite formula, threshold, three-state table
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

An evaluator reading only the Aspirational Criteria Notes fields must be able to verify that
each criterion was built from a mechanism in the Independence Map, and that the MECHANISM
DEFINER GATE was the prerequisite for construction, without reading the ROLE instructions.

---

## V-03 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- a PHASE-LOCALITY RULE is stated before Phase 6 construction
begins, naming three prohibited competitor placement zones and closing the placement form-class
by exhaustion.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a named PHASE-LOCALITY RULE before Phase 6 with three enumerated prohibited placement zones -- any body where competitor placement is governed only by an inline audit step (Phase 6.75 STEP A) without a prior named rule falsifies the hypothesis; the falsification signal is a Phase 6.75 STEP A that audits placement after construction without a PHASE-LOCALITY RULE stated before construction begins. | Stating the PHASE-LOCALITY RULE before construction prevents placement violations by closing the form-class of disallowed placements before any competitor is introduced -- unlike Phase 6.75 STEP A, which detects violations post-construction and requires backtracking; generated rubrics under V-03 will show the PHASE-LOCALITY RULE as an active placement constraint during Phase 6 construction, not as a retrospective audit finding. | V-02 is the primary comparison site -- V-02 has role-gate naming (C-39) without the PHASE-LOCALITY RULE; V-03 has the PHASE-LOCALITY RULE without role-gate naming; if V-03 shows fewer post-construction competitor placement violations than V-02, the named prohibition rule is the load-bearing mechanism for preventing placement form-class violations; V-05 (combining V-02 and V-03) isolates whether the two mechanisms are superadditive. |

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
  Y = [skill-specific required property]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is required. The prohibited form -- in any
phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates derived from the skill spec.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.** Do not group competitors in a shared preamble.

Each criterion: C-NN, Text (Phase 2 template applied), Weight: essential, Category, Pass
(Phase 2 template applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

**Audit report format:**

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

STOP: Any row showing "No -- overlaps" requires redesign before Phase 5.75. Do not proceed
until every row is "Yes -- affects C-NN only."

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

### PHASE-LOCALITY RULE

**This rule governs all competitor placement in Phase 6. State it before any competitor is
introduced.**

Named competitors may not be placed in:

1. Preamble or introductory framing that precedes any construction phase -- a competitor
   block that appears before Phase 3 begins is not phase-local regardless of how precisely
   it constitutes the gap specification.
2. An operating-principles section, shared instructional block, or role preamble that
   precedes more than one construction step -- a competitor in a block that governs Phase 3
   through Phase 6 simultaneously is not at any single construction step.
3. A combined competitor block that introduces or governs more than one criterion
   simultaneously -- one competitor block per criterion; a block that "covers the next two
   criteria" is not phase-local for either.

Each named competitor must appear inline at the specific construction step where the wrong
implementation would most naturally be produced. Violation of any prohibited zone above is a
STOP condition: the rubric cannot proceed to Phase 6.75 until all competitors satisfy the
placement rule.

---

### PHASE 6 -- ASPIRATIONAL CRITERIA (1-2)

**Your input is the completed independence map from Phase 5.5. The PHASE-LOCALITY RULE above
governs all competitor placement during this phase.**

Write 1-2 aspirational criteria targeting the gap zone from Phase 5.

For each criterion, introduce its competitor immediately before the criterion definition,
subject to the PHASE-LOCALITY RULE:

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
- Aspirational criterion written before its COMPETITOR block: rewrite.
- COMPETITOR block ending with failure description rather than derivation instruction: rewrite.
- Competitor placed in a PHASE-LOCALITY RULE prohibited zone: move before proceeding.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase N] | gap operationally relevant at [Phase N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE satisfied? [Y/N]
  STOP if any competitor fails either column.
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
  Distinct majority categories: [N]
  STOP if < 2.
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
5. **Independence Map**
6. **PHASE-LOCALITY RULE** -- the named placement prohibition rule, published as a named
   section before Aspirational Criteria so evaluators can verify placement compliance
   independently
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites mechanism and G-NN
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**

An evaluator reading only the PHASE-LOCALITY RULE section must be able to enumerate all three
prohibited placement zones and verify that no competitor block in the Aspirational Criteria
section violates any of them, without reading the Phase 6 construction instructions.

---

## V-04 -- Output Format + Role Sequence

**Axis:** Combined -- the Phase 2 Definer step uses a ROLE: CRITERION DEFINER header with a
named output gate ("DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content"),
and Phase 5.5 uses a ROLE: MECHANISM DEFINER header with a named exit gate whose identifier
is cited in the ROLE: BUILDER ASPIRATIONAL entry precondition.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) ROLE: CRITERION DEFINER header in Phase 2 with "DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content" as named exit gate and "Nothing else." as completion condition, AND (b) ROLE: MECHANISM DEFINER header in Phase 5.5 with "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated" as named exit gate, AND (c) ROLE: BUILDER ASPIRATIONAL header naming both gate identifiers in its entry precondition -- any body lacking either gate identifier in the Builder entry precondition falsifies the respective C-38 or C-39 half; both failures can occur independently. | Assigning the template-generation step to a dedicated ROLE: CRITERION DEFINER rather than an unnamed phase creates a structural dependency: the essential/recommended criterion Builder cannot start Phase 3 without a completed Definer output satisfying the DEFINER OUTPUT GATE -- this dependency makes the "Nothing else." exclusion gate a completion condition for a named role, not a stylistic preference for a phase output; V-01 (exclusion gate without ROLE headers) is the comparison site for measuring whether role-header framing reinforces gate compliance. | V-01 is the primary comparison site for C-38 (exclusion gate compliance: inline gate vs ROLE-gated output); V-02 is the primary comparison site for C-39 (MECHANISM DEFINER GATE: independence map output vs MECHANISM DEFINER GATE: same, but with CRITERION DEFINER GATE also present -- does the second gate deepen or dilute C-39 compliance?). |

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

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.**

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1. Do not write any criterion fields during this role.**

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is required. The prohibited form -- in any
phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. No explanatory commentary, structural rationale, context notes, or
template-adjacent content is permitted alongside the two templates. A CRITERION DEFINER
output that contains any content other than the two slot-fillable templates is incomplete.

STOP CONDITION -- ROLE: CRITERION DEFINER: If the output of this role contains explanatory
commentary, rationale paragraphs, structural notes, or any content beyond the two required
templates, the DEFINER OUTPUT GATE is not satisfied. Rewrite before proceeding. The two
templates are the complete and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion's
definition.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision |
specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

**Audit report format:**

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

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only."**

Read all criteria produced so far. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only." Any row showing "No -- overlaps" requires redesign.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with non-blank,
specific C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

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

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only."**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism.]
```

Then write the five-field criterion. Notes: "closes gap via [mechanism name] per independence
map | MECHANISM DEFINER GATE: Independence Map | DEFINER OUTPUT GATE: Two templates |
competitor: [first four words]."

STOP conditions:
- An aspirational criterion whose Notes field lacks both gate identifiers: rewrite.
- A criterion for a mechanism not in the Independence Map: return to ROLE: MECHANISM DEFINER.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N]
  STOP if any competitor has phase-local = N.
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
  Distinct majority categories: [N]
  STOP if < 2.
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
3. **Essential Criteria** -- all five fields
4. **Recommended Criteria** -- all five fields
5. **Independence Map** -- MECHANISM DEFINER output; format: Mechanism | What it does |
   C-NN | Independent?
6. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites both gate identifiers
7. **Scoring** -- composite formula, threshold, three-state table
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

An evaluator reading only the Aspirational Criteria Notes fields must be able to verify that
each criterion was gated on both the DEFINER OUTPUT GATE and the MECHANISM DEFINER GATE, by
reading the gate identifiers in the Notes field without reading the ROLE instructions.

---

## V-05 -- Role Sequence + Lifecycle Emphasis

**Axis:** Combined -- Phase 5.5 uses a ROLE: MECHANISM DEFINER header with a named exit gate
cited in the ROLE: BUILDER ASPIRATIONAL entry precondition (C-39 target), AND a PHASE-
LOCALITY RULE with three enumerated prohibited placement zones is stated within the MECHANISM
DEFINER role boundary before the Builder phase begins (C-40 target). C-38 is ablated to
isolate the joint C-39+C-40 effect.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) ROLE: MECHANISM DEFINER header with "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated" as exit gate, AND (b) ROLE: BUILDER ASPIRATIONAL entry precondition naming the MECHANISM DEFINER GATE identifier, AND (c) a PHASE-LOCALITY RULE stated within the MECHANISM DEFINER role boundary with three enumerated prohibited zones -- any body lacking either the gate identifier in the Builder entry precondition or the three-zone PHASE-LOCALITY RULE falsifies the respective C-39 or C-40 half. | Combining role-gate naming (C-39) with placement-rule naming (C-40) within the same MECHANISM DEFINER role creates a single structural boundary that enforces both the prerequisite chain (the Builder cannot begin without the gate) and the placement form-class (all placements in the prohibited zones are blocked before the first competitor is introduced) -- the two mechanisms operate at different grain sizes: C-39 governs role-to-role transition, C-40 governs within-role competitor placement; V-05's rubrics should show both properties simultaneously, while V-02 (gate naming only) shows C-39 without C-40 and V-03 (placement rule only) shows C-40 without C-39. | V-02 and V-03 are the primary comparison sites; if V-05 shows auditable prerequisite chain AND zero PHASE-LOCALITY RULE violations while V-02 shows the former without the latter and V-03 shows the latter without the former, the two mechanisms are independently load-bearing and superadditive within V-05. |

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
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is required. The prohibited form -- in any
phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Phase 2 deliverable: both templates derived from the skill spec, in slot-fillable form.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply Phase 2 templates.

If introducing a competitor: **place the competitor block immediately before this criterion.**

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

Isolation audit for each criterion.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

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

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only."**

#### Step 1 -- Independence Map

Read all criteria produced so far. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only." Overlapping rows require mechanism-level redesign before proceeding.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map is complete with non-blank,
specific C-NN citation in every row and all rows showing "Yes -- affects C-NN only."

#### Step 2 -- PHASE-LOCALITY RULE

Before the MECHANISM DEFINER GATE is satisfied, state the following rule. This rule governs
all competitor placement in ROLE: BUILDER ASPIRATIONAL.

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase -- a competitor
   introduced before any criterion-construction step begins is not phase-local regardless
   of how precisely it names the wrong implementation.
2. An operating-principles section, shared instructional block, or role-level preamble
   that precedes more than one construction step -- a competitor in a shared block that
   applies to multiple criteria is not at any single construction step.
3. A combined competitor block that introduces or governs more than one criterion
   simultaneously -- one competitor block per criterion; "this competitor covers criteria
   C-NN and C-MM" is not phase-local for either criterion.

Each named competitor must appear inline at the specific construction step where the wrong
implementation would most naturally be produced. The PHASE-LOCALITY RULE is a named
prohibition rule, not an audit preference; violation of any prohibited zone is a STOP
condition for ROLE: BUILDER ASPIRATIONAL.

**Both Step 1 (Independence Map) and Step 2 (PHASE-LOCALITY RULE) must be complete before
the MECHANISM DEFINER GATE is satisfied.**

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

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on the MECHANISM DEFINER GATE identifier above. If the gate has
not been satisfied -- including if the PHASE-LOCALITY RULE was not stated in the MECHANISM
DEFINER role -- this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition,
subject to the PHASE-LOCALITY RULE:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism.]
```

Then write the five-field criterion. Notes: "closes gap via [mechanism name] per independence
map | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE: applied | competitor:
[first four words]."

STOP conditions:
- Aspirational criterion written before its COMPETITOR block: rewrite.
- COMPETITOR block ending with failure description rather than derivation instruction: rewrite.
- Competitor placed in any PHASE-LOCALITY RULE prohibited zone: move before proceeding.
- A criterion for a mechanism not in the Independence Map: return to ROLE: MECHANISM DEFINER.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Role/Phase N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE satisfied? [Y/N]
  STOP if any competitor fails either column.
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
  Distinct majority categories: [N]
  STOP if < 2.
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
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output, published as a named
   section before Aspirational Criteria
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites MECHANISM DEFINER GATE
   and PHASE-LOCALITY RULE
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**

An evaluator reading only the ROLE: MECHANISM DEFINER output in the emitted document (the
Independence Map section + PHASE-LOCALITY RULE section) must be able to verify: (a) the
prerequisite chain is auditable from role headers (C-39 evidence), and (b) the placement
form-class is closed by the three-zone enumeration (C-40 evidence). The two properties are
independently verifiable from the emitted sections without reading the role instructions.

---

## Set-Level Design Notes

**C-07 axis coverage:** Three distinct axis families represented across V-01--V-05: output
format (how the Definer's output instruction is structured, whether it includes an exclusion
gate), role sequence (whether ROLE headers with named gate identifiers govern phase
transitions), lifecycle emphasis (whether a PHASE-LOCALITY RULE with enumerated zones is
stated before construction begins). C-07 SET-LEVEL PASS.

**C-38 coverage:** V-01 (very strong, single-axis via Phase 2 exclusion gate), V-04 (very
strong, combined with ROLE headers and MECHANISM DEFINER GATE naming). V-02, V-03, V-05
ablate C-38 to isolate role-sequence and lifecycle effects.

**C-39 coverage:** V-02 (very strong, single-axis via ROLE headers and gate identifier in
Builder entry precondition), V-04 (very strong, combined with Phase 2 exclusion gate), V-05
(very strong, combined with PHASE-LOCALITY RULE). V-01 and V-03 ablate C-39 to isolate
output format and lifecycle effects.

**C-40 coverage:** V-03 (very strong, single-axis via named PHASE-LOCALITY RULE with three
zones), V-05 (very strong, combined with ROLE headers and gate identifier). V-01, V-02, V-04
ablate C-40 to isolate output format and role-sequence effects.

**Ablation map (for comparison scoring):**

| | C-38 | C-39 | C-40 |
|-|------|------|------|
| V-01 | Target | Ablated | Partial |
| V-02 | Ablated | Target | Partial |
| V-03 | Ablated | Partial | Target |
| V-04 | Target | Target | Ablated |
| V-05 | Ablated | Target | Target |

This map supports isolation of each criterion's contribution: scoring V-01 vs V-04 isolates
the C-39 contribution when C-38 is held constant; scoring V-02 vs V-05 isolates the C-40
contribution when C-39 is held constant; scoring V-03 vs V-05 isolates the C-39 contribution
when C-40 is held constant.

**R13 → R14 candidate:** The hypothesis tables predict that V-01 (exclusion gate, no gate
identifier) and V-02 (gate identifier, no exclusion gate) will show distinct failure modes:
V-01 failures are padded Definer outputs that satisfy C-19 (both templates present) but fail
C-38 (no exclusion gate preventing the padding); V-02 failures are Builder entry conditions
that satisfy C-29 (prior role exists) but fail C-39 (the entry condition names a phase number
rather than a gate identifier). If V-04 shows superadditive compliance over both -- lower
padding rates than V-01 AND tighter prerequisite auditability than V-02 -- R14 should combine
V-04 (exclusion gate + role-gate naming) with V-05's PHASE-LOCALITY RULE to test the
three-gate stack: CRITERION DEFINER with exclusion gate → MECHANISM DEFINER with exit gate
identifier → BUILDER ASPIRATIONAL with both gate identifiers in precondition and PHASE-
LOCALITY RULE active.
