---
name: topic-story
description: Editorial synthesis of all signals into a coherent narrative with recommendation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*` and read every artifact found. Read
`simulations/{topic}/strategy.md` if present.

---

### Step 2 -- Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence -- the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each artifact, in reading order:

```
- `{artifact-name}`: {key finding most relevant to S0, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

After all entries:

```
Hypothesis at S3: [evolved claim, one sentence]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: which stances drove this; reference at least one artifact name]
```

**Anti-stagnation check**: If S3 = S0, explain. **Reconciliation check**: CONFIRMED +
unresolved CONTRADICTS = QUALIFIED. Do not build the reconciliation table until the ledger
is complete.

---

### Step 2a -- Vector-verdict reconciliation table

Immediately after the net mutation vector, build the reconciliation table. One row per
ledger entry. Four columns: Signal, Verdict type, Consistent?, Verify.

```
| Signal | Verdict type | Consistent? | Verify |
|--------|-------------|-------------|--------|
| {artifact-name} | CONFIRMS -- {dimension} | YES | {section}, {entry-type} |
| {artifact-name} | MODIFIES toward {dimension} | YES | {section}, {entry-type} |
| {artifact-name} | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) | {section}, {entry-type} |
| {artifact-name} | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT | {section}, {entry-type} |
```

The Verify column names two things: the section a reader would check and the entry type
within it. Both must be present per cell.

After the table:

```
Reconciliation: Vector is consistent -- [one sentence: verdict distribution justification].
```

OR if a CONFLICT row forced a revision:

```
Reconciliation: Vector revised from [X] to [Y] -- [the CONFLICT entry that forced it].
```

---

### Step 2b -- INERTIA-CLAIM

Name the status-quo competitor before writing CONDITIONS-PRECOMMIT.

```
INERTIA-CLAIM: [one sentence: the specific default path the team would have taken without
  investigation -- named precisely, not generically. Self-contained.]
```

Appears in Beat 1 (entering default), Beat 2 (foil per signal), and Beat 4.5 CHAIN-AUDIT
(quoted verbatim in the weakest-justification-link sentence).

---

### Step 2c -- CONDITIONS-PRECOMMIT

Commit pointer values for both conditions sites before writing any conditions clause.

```
CONDITIONS-PRECOMMIT:
- Site 1 (Beat 4.5 Conditions line)
    Pre-committed section:    [section a reader checks to confirm the condition]
    Pre-committed field-type: [entry type within that section]
- Site 2 (AUTHOR-CONDITIONS in Beat 5)
    Pre-committed section:    [section a reader checks to confirm the condition]
    Pre-committed field-type: [entry type within that section]
```

All four fields must be real values before writing Beat 4.5. Update this block first if a
conditions clause changes direction.

---

### Step 3 -- State the verdict

```
## Verdict

**{PROCEED | PAUSE | PIVOT | ABANDON}** -- [one sentence: the core directive, defeating
the INERTIA-CLAIM. Committed before any evidence beat. Defended in Beat 5.]
```

---

### Step 4 -- Write the justification beats

**Beat 1 -- What we set out to understand**
One to three sentences. The question and S0. Name the INERTIA-CLAIM as the entering
default: "The default going in was [INERTIA-CLAIM]. The investigation asked whether it held."

**Beat 2 -- What each signal revealed**
For each ledger entry, one editorial sentence -- what the finding means for the INERTIA-CLAIM.
Does this signal support or challenge the default path? Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open with: "Across [N] signals, the hypothesis was [vector] -- consistent with the stated
verdict." The reconciliation table validates this claim.

**Anchor citation rule**: Every non-trivial claim names its source:
`(anchored: {artifact-name}, {stance})`.

For any cross-signal tension:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason]
     OR: UNRESOLVED because [what signal would resolve it]
```

Every Conflict verdict carries a because-clause. Any CONFLICT row in the reconciliation
table must appear as a Conflict/Verdict entry here.

**Falsifiability check**: Does any single entry carry the Beat 3 conclusion alone? Revisit
if yes.

**Beat 4 -- What remains uncertain (structured risk register)**

Three tiers, completed before writing Beat 4.5.

**Tier 1 -- Gap catalog**

```
Gap [{ID}]: [testable question -- not a vague category]
  Risk tier: BLOCKING | MAJOR | MINOR
  Blocking rationale: [if BLOCKING: why this must close before the verdict can hold;
    if MAJOR/MINOR: bounded scope, one sentence]
  Most exposed finding: [ledger entry whose claim depends on closing this gap]
```

Label gaps G-01, G-02, etc. At least one gap must be BLOCKING or MAJOR.

**Tier 2 -- Critical-path analysis**

```
Critical path: [G-XX] -> [G-XX]
  Rationale: [one sentence per dependency edge]
```

If no dependencies: "No critical-path dependencies: all gaps are independently closeable."

**Tier 3 -- Resolution sequencing**

```
Resolution [{G-ID}]:
  Priority: BLOCKING | MAJOR | MINOR
  Next signal: {namespace}/{skill} -- [expected finding type]
  Prerequisite: [G-ID or "none"]
```

**Beat 4.5 -- Derivation chain**

Six elements, each on its own line. No placeholders.

```
Anchored claim: "[exact S3 claim from Beat 3, verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence, verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: why the vector
  licenses this verb; must match the Verdict section]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: what would have to
  be true for the adjacent verb to apply; may reference a Beat 4 gap tier]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why this value maps
  to the recommendation verb; may reference a Beat 4 gap tier label]
CHAIN-AUDIT (justification): The first sentence must state the pre-committed verdict verbatim:
  "Stated verdict: {VERB}." For each link, state ADEQUATE or INADEQUATE for {VERB} with a
  reason that references the stated verdict explicitly:
    S0 -> ledger: ADEQUATE | INADEQUATE -- [reason referencing {VERB} vs INERTIA-CLAIM]
    ledger -> S3 ([vector]): ADEQUATE | INADEQUATE -- [reason]
    S3 -> {verb}: ADEQUATE | INADEQUATE -- [reason]
    Conditions ({category}={value}) -> Beat 5: ADEQUATE | INADEQUATE -- [reason; may name
      a BLOCKING gap as the source of any INADEQUATE rating]
  Weakest-justification-link sentence (REQUIRED FORMAT):
    "Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
    is most contestable here because {specific artifact name or vector property; if a BLOCKING
    gap is the most exposed dependency, name it}."
  The INERTIA-CLAIM text must be quoted verbatim. Referencing "the inertia position" without
  the actual claim text does not satisfy this requirement.
```

**Conditions line format:** Count, ratio, or threshold with comparator. No bare adjectives.
The `(verify: ...)` must match Site 1 in CONDITIONS-PRECOMMIT.
The Recommendation verb must match the Verdict section. Fix Verdict section if they diverge.

Do not write Beat 5 until all six elements are consistent.

**Beat 5 -- Recommendation**

**Sub-step A -- CHALLENGER**

The CHALLENGER argues the INERTIA-CLAIM should stand. Must cite a specific element.

```
CHALLENGER-CLAIM: [adjacent verb] -- [specific element supporting the INERTIA-CLAIM:
  ledger entry by name, Beat 4 gap ID, or declared vector property]
```

Optional CHALLENGER paragraph (up to four sentences referencing the named element).

**Sub-step B -- AUTHOR**

```
AUTHOR-RULING: [one sentence: why the element the CHALLENGER cited does not save the
  INERTIA-CLAIM; reference that element directly]
AUTHOR-CONDITIONS: {category} = {value} (verify: {section}, {field-type}) -- [one sentence:
  why this value resolves in favor of {VERB} over the adjacent verb and the INERTIA-CLAIM]
```

The `(verify: ...)` pointer must match Site 2 in CONDITIONS-PRECOMMIT.

Optional AUTHOR paragraph (up to four sentences).

**Multi-site five-field compliance record**
*(run after Sub-step B, before recommendation paragraph)*:

```
*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language statement of what the conditions clause requires -- NOT a
    copy of the clause itself; one sentence explaining what must be true]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]:
              "(verify: {section}, {field-type})"
  VERIFIED:   [satisfied / not-yet-satisfied] -- [one sentence: name the specific evidence
    -- ledger entry, reconciliation row, or gap tier -- that confirms or fails to confirm
    the condition]
  MATCH:      Pre-committed: ({section}, {field-type}) vs
              Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]  [or: MISMATCH -- state discrepancy; revise PRECOMMIT]

Site 2 -- AUTHOR-CONDITIONS:
  CONDITION:  [plain-language requirement, one sentence; not a copy of the clause]
  LOCATION:   Beat 5 / AUTHOR-CONDITIONS
  VALUE:      TRANSCRIBED FROM [Beat 5 > AUTHOR-CONDITIONS > verify field]:
              "(verify: {section}, {field-type})"
  VERIFIED:   [satisfied / not-yet-satisfied] -- [one sentence: basis]
  MATCH:      Pre-committed: ({section}, {field-type}) vs
              Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]  [or: MISMATCH -- state discrepancy; revise PRECOMMIT]
```

Field requirements:
- CONDITION: plain-language restatement, not a copy of the clause.
- VALUE: verbatim `(verify: ...)` text with TRANSCRIBED FROM attribution.
- VERIFIED: names the basis explicitly. "satisfied" without a basis sentence fails C-39.
- MATCH: states both pre-committed and transcribed values side by side, then declares Status.

**Named-rival compliance check**:

```
NAMED-RIVAL CHECK:
  INERTIA-CLAIM declared: [YES -- quote the exact INERTIA-CLAIM text]
  Weakest-link sentence: [copy full sentence from CHAIN-AUDIT]
  Rival appears quoted: [YES / NO]
  Status: PASS | FAIL
```

Do not write the recommendation paragraph until all ten compliance-record fields are present,
both MATCH statuses show MATCH, and the NAMED-RIVAL CHECK shows PASS.

**Recommendation paragraph**

One of: **proceed**, **pause**, **pivot**, **abandon** (must match Verdict section exactly).
Full directive: what to do, under what conditions, with what scope. Names what the investigation
established over the INERTIA-CLAIM. May reference gap-tier closure conditions from Beat 4
Tier 3. Does not repeat labeled claims.

---

**Voice**: Six mechanisms are simultaneously active. The reconciliation table (C-30) validates
the vector claim in Beat 3; every CONFLICT row must appear as a Conflict/Verdict entry. The
structured risk register (Beat 4) gives the CHALLENGER/AUTHOR exchange a richer citation
vocabulary: gap IDs and tier labels are available for the CHALLENGER-CLAIM and AUTHOR-RULING.
The INERTIA-CLAIM shadows the entire artifact: Beat 1 names it as the entering default, Beat 2
measures each signal against it, and Beat 4.5 quotes it in the weakest-link sentence because
the case for {VERB} is only auditable when the rival is named and the weakest link is identified
in relation to that specific rival. The CHAIN-AUDIT uses formal-imperative instruction: the
quoted-rival requirement is a template constraint, not a suggestion. The five-field compliance
record makes conditions verification self-confirming: CONDITION restates the requirement,
VERIFIED names what was found and why it confirms it -- a reader never needs to navigate.
The ceiling is 227.5 because C-10 requires a story-forward opening; this artifact opens with
a verdict. Every other mechanism is active.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]

## Vector-Verdict Reconciliation
| Signal | Verdict type | Consistent? | Verify |
|--------|-------------|-------------|--------|
...
**Reconciliation**: [consistency sentence or revision note]

## INERTIA-CLAIM
[specific default path, one sentence, self-contained]

## CONDITIONS-PRECOMMIT
- Site 1 (Beat 4.5): Pre-committed section: [section] / Pre-committed field-type: [field-type]
- Site 2 (AUTHOR-CONDITIONS): Pre-committed section: [section] / Pre-committed field-type: [field-type]

## Verdict
**PROCEED | PAUSE | PIVOT | ABANDON** -- [one-sentence directive defeating INERTIA-CLAIM]

## Story

### Beat 1 -- What we set out to understand
[question + S0 + INERTIA-CLAIM as entering default]

### Beat 2 -- What each signal revealed
[per-signal editorial sentence read against INERTIA-CLAIM]

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector] -- consistent with the stated verdict.
[anchored claims] [Conflict / Verdict entries, including any CONFLICT reconciliation rows]

### Beat 4 -- What remains uncertain

**Tier 1 -- Gap catalog**
Gap [G-01]: [testable question]
  Risk tier: BLOCKING
  Blocking rationale: [...]
  Most exposed finding: [ledger entry]
...

**Tier 2 -- Critical-path analysis**
Critical path: [G-01] -> [G-02] / Rationale: [dependency sentence]

**Tier 3 -- Resolution sequencing**
Resolution [G-01]: Priority: BLOCKING / Next signal: {namespace}/{skill} -- [...] / Prerequisite: none
...

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} -- [mechanism sentence]
Recommendation verb: {VERB} -- [licensing sentence]
Adjacent verb: {ADJACENT-VERB} -- [contestation claim; may reference gap tier]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why value maps]
CHAIN-AUDIT (justification): Stated verdict: {VERB}.
  S0 -> ledger: ADEQUATE -- [reason, refs {VERB} vs INERTIA-CLAIM];
  ledger -> S3 ([vector]): ADEQUATE -- [reason]; S3 -> {verb}: ADEQUATE -- [reason];
  Conditions -> Beat 5: ADEQUATE -- [reason; may name BLOCKING gap].
  Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
  is most contestable here because {artifact or property; name BLOCKING gap if most exposed}.

### Beat 5 -- Recommendation

**CHALLENGER-CLAIM**: [adjacent verb] -- [specific element: ledger entry, gap ID, or vector property]
[Optional CHALLENGER paragraph]

**AUTHOR-RULING**: [ruling-out claim referencing same element]
**AUTHOR-CONDITIONS**: {category} = {value} (verify: {section}, {field-type}) -- [why]
[Optional AUTHOR paragraph]

*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language requirement, not a copy]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis: ledger entry, reconciliation row, or gap tier]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

Site 2 -- AUTHOR-CONDITIONS:
  CONDITION:  [plain-language requirement]
  LOCATION:   Beat 5 / AUTHOR-CONDITIONS
  VALUE:      TRANSCRIBED FROM [Beat 5 > AUTHOR-CONDITIONS > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

NAMED-RIVAL CHECK:
  INERTIA-CLAIM declared: YES -- "[exact INERTIA-CLAIM text]"
  Weakest-link sentence: "Weakest justification link: [{link}] -- the case for {VERB} over '{INERTIA-CLAIM}' is most contestable here because {artifact}."
  Rival appears quoted: YES
  Status: PASS

**PROCEED | PAUSE | PIVOT | ABANDON** -- [full directive paragraph; defeats INERTIA-CLAIM;
may reference gap-tier closure conditions from Tier 3]
```