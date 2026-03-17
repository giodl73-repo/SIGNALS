---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 20
rubric: v18
---

# Variations -- topic-story (Round 20)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: R19 tested C-37 achievability and three structural axes. Two new criteria
were extracted from R19 outputs: C-38 (named-rival weakest-link identification, from V-02 R19)
and C-39 (audit-record satisfaction basis, from V-05 R19). R20 rotates to these two new
criteria as the primary test axes.

**State from R19 (scored against v17, 220 pts):**

- V-01 R19: Verdict-first, C-37 pass (explanatory register), minimal compliance, no INERTIA-CLAIM. ~202.5.
- V-02 R19: Verdict-first, C-37 pass (formal register), INERTIA-CLAIM, named-rival weakest-link. ~202.5. [Source of C-38]
- V-03 R19: Story-forward, C-37 fail, structured risk register. ~205.
- V-04 R19: Verdict-first, C-37 pass (explanatory register), INERTIA-CLAIM. ~202.5.
- V-05 R19: All mechanisms (explanatory register, INERTIA-CLAIM, risk register, C-30, five-field compliance). ~217.5. [Source of C-39]

**Why V-04/V-05 R19 fail C-38**: The rubric confirms that V-01/04/05 R19 pass C-37 without
naming a rival. V-04 and V-05 both carry an INERTIA-CLAIM structural element, but their
CHAIN-AUDIT instructions use explanatory register -- describing the purpose of naming the
rival rather than demanding a specific quoted-name format. The conversational framing produced
weakest-link sentences that referenced the inertia position without quoting the INERTIA-CLAIM
verbatim. V-02's formal-imperative instruction -- "identifying the link where the case for
{VERB} over the INERTIA-CLAIM ("{INERTIA-CLAIM}") is most contestable" -- required the
quoted claim text, which is what C-38 captures. R20 V-02 and V-04 use formal-imperative
framing for the weakest-link instruction specifically to produce the quoted-rival form.

**R20 axis selection:**

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| C-39 isolation: five-field VERIFIED | V-01 | C-39 is achievable without C-38 or INERTIA-CLAIM; the VERIFIED field adds independently to a standard verdict-first artifact |
| C-38 isolation: explicit named-rival, formal | V-02 | C-38 requires formal-imperative CHAIN-AUDIT instruction with quoted INERTIA-CLAIM; achievable without C-39 |
| Story-forward + C-39 | V-03 | C-39 is architecture-neutral; story-forward artifacts can achieve the VERIFIED field |
| C-38 + C-39 combined, minimal | V-04 | Both new criteria are additive and non-interfering at the minimal compliance level |
| Full ceiling: C-38 + C-39 + C-30 + risk register | V-05 | Full verdict-first ceiling 227.5 with all mechanisms active |

**R20 isolation design:**

| Variation | C-10 | C-12 | C-27 | C-30 | C-36/C-39 | C-37 | C-38 | Register |
|-----------|------|------|------|------|-----------|------|------|----------|
| V-01 | FAIL | PASS | PASS-just | absent | 5-field (C-39) | PASS | FAIL | formal |
| V-02 | FAIL | PASS | PASS-just | absent | 4-field (C-36 only) | PASS | PASS | formal |
| V-03 | PASS | FAIL | PASS-disc | absent | 5-field (C-39) | FAIL | FAIL | formal |
| V-04 | FAIL | PASS | PASS-just | absent | 5-field (C-39) | PASS | PASS | formal |
| V-05 | FAIL | PASS | PASS-just | PASS | 5-field (C-39) | PASS | PASS | formal |

**Expected scores (v18, 230 pts, verdict-first ceiling 227.5):**

| Variation | Expected | Key FAILs |
|-----------|----------|-----------|
| V-01 | ~207.5 | C-10, C-30, C-38 |
| V-02 | ~207.5 | C-10, C-30, C-39 |
| V-03 | ~210 | C-12, C-37, C-38 |
| V-04 | ~212.5 | C-10, C-30 |
| V-05 | ~227.5 | C-10 only |

**C-38 note for R20**: C-38 is independent of C-39. V-02 demonstrates C-38 without five-field
compliance; V-01 demonstrates C-39 without a named rival. The combination (V-04) tests
additivity. V-05 tests full ceiling with both.

**C-39 note for R20**: The VERIFIED field is the operative condition -- "satisfied" must be
followed by a basis sentence naming the ledger entry, reconciliation row, or gap tier that
confirms the condition. The CONDITION field must be a plain-language restatement, not a copy
of the clause. V-01/V-03 isolate this; V-04/V-05 embed it in combination.

---

## V-01

**Variation axis**: C-39 isolation -- five-field compliance record (CONDITION/LOCATION/VALUE/
VERIFIED/MATCH) added to the standard verdict-first artifact. No INERTIA-CLAIM structural
element (C-38 unavailable). All other mechanisms from V-01 R18/R19 preserved: C-37
justification-audit CHAIN-AUDIT, formal register, minimal compliance (no C-30).

**Hypothesis**: C-39 is achievable without C-38 or a named rival. The VERIFIED field -- the
satisfaction basis stating what was found and why it confirms the condition -- can be added
to any verdict-first artifact that already carries a CONDITIONS-PRECOMMIT block and a
MATCH-CHECK. V-01 R19 scored ~202.5 under v17. Under v18 (230 pts), adding C-39 should
yield ~207.5. If V-01 achieves C-39 while failing C-38, independence is confirmed.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*` and read every artifact found. If
`simulations/{topic}/strategy.md` exists, read that too.

You now have the full evidence set. Everything in the story flows from what you just read.

---

### Step 2 -- Hypothesis mutation ledger

Before you write the story, track how your hypothesis changed as you read.

Begin with the working hypothesis -- the specific claim the team entered with, stated as
something that could be proved wrong. Write it in one sentence.

**Working hypothesis (S0)**: [the specific entering claim as a falsifiable assertion]

For each artifact you read, write one entry in the order you encountered it:

```
- `{artifact-name}`: {key finding most relevant to S0, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

After all entries, close the ledger:

```
Hypothesis at S3: [the working hypothesis after all stances are applied, one sentence]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: which stances, on which dimension, drove this classification; reference at
least one ledger entry by artifact name]
```

**Anti-stagnation check**: If S3 is identical to S0, say why explicitly.

**Reconciliation check**: If the net vector says CONFIRMED but there are unresolved
CONTRADICTS entries, revise the vector to QUALIFIED before continuing.

Do not write the story beats until the ledger is complete and both checks are done.

---

### Step 2b -- CONDITIONS-PRECOMMIT

Before you write any conditions clause, decide what the conditions will point to.

There are exactly two conditions sites in this artifact: the Conditions line in Beat 4.5,
and the AUTHOR-CONDITIONS line in Beat 5. Each will carry a pointer of the form
`(verify: {section}, {field-type})`. Commit those pointers now, before writing the
conditions clauses, so you can verify consistency afterward.

```
CONDITIONS-PRECOMMIT:
- Site 1 (Beat 4.5 Conditions line)
    Pre-committed section:    [the section a reader would check to confirm the condition]
    Pre-committed field-type: [the entry type within that section]
- Site 2 (AUTHOR-CONDITIONS in Beat 5)
    Pre-committed section:    [the section a reader would check to confirm the condition]
    Pre-committed field-type: [the entry type within that section]
```

All four fields must have real values before you write Beat 4.5. If your conditions clause
changes direction during writing, update the CONDITIONS-PRECOMMIT block first, then write
the revised clause.

---

### Step 3 -- Write the verdict headline

This story opens with the recommendation. You state your verdict before showing any evidence.

```
## Verdict

**{PROCEED | PAUSE | PIVOT | ABANDON}** -- [one sentence stating the core directive.
This commits the recommendation before any evidence is shown. Beat 5 defends it.]
```

The verb you write here is the anchor for everything that follows. Beat 4.5 must carry the
same verb. Beat 5 defends this specific verb against the adjacent alternative.

---

### Step 4 -- Write the justification beats

The beats are not a discovery arc. They are a justification chain for the verdict you
already stated. Write each one as evidence in support of that conclusion.

**Beat 1 -- What we set out to understand**
One to three sentences. State the original question and S0. Name the default position the
team would have taken if no investigation had occurred.

**Beat 2 -- What each signal revealed** *(draws from the ledger)*
For each ledger entry, write one editorial sentence beyond the raw finding -- what the
finding means as evidence for the stated verdict. Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
This is the cross-signal synthesis, not a summary. Open with:
"Across [N] signals, the hypothesis was [vector] -- consistent with the stated verdict."

**Anchor citation rule**: Every non-trivial claim in Beat 3 must name the ledger entry
that licenses it: `(anchored: {artifact-name}, {stance})`.

For any place where two signals point in different directions:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [the dimension they disagree on]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every verdict in a Conflict block carries a because-clause. No bare verdicts.

**Falsifiability test**: Before closing Beat 3, check whether any single ledger entry alone
contains your Beat 3 conclusion. If one entry could carry the synthesis by itself, you
haven't synthesized -- you've excerpted. Revisit if so.

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} -- [one sentence: expected finding type]
```

**Beat 4.5 -- Derivation chain** *(written after CONDITIONS-PRECOMMIT is filled)*

Six elements, each on its own line. No placeholders.

```
Anchored claim: "[exact S3 claim from Beat 3, copied verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence, verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: why the vector
  licenses this verb; must match the verb in the Verdict section]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: the specific claim that
  would have to be true for this alternative verb to apply instead]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why this value maps to
  the recommendation verb rather than the adjacent one]
CHAIN-AUDIT (justification): The first sentence must state the pre-committed verdict verbatim:
  "Stated verdict: {VERB}." For each derivation link, evaluate ADEQUATE or INADEQUATE for the
  stated conclusion -- a reason must reference {VERB}, not just describe the link. Links:
  S0 -> ledger: [ADEQUATE/INADEQUATE -- reason referencing {VERB}]; ledger -> S3 ([vector]):
  [ADEQUATE/INADEQUATE -- reason]; S3 -> {verb}: [ADEQUATE/INADEQUATE -- reason]; Conditions
  ({category}={value}) -> Beat 5 ruling: [ADEQUATE/INADEQUATE -- reason]. Close with:
  "Weakest justification link: [{link-name}] -- {specific artifact or vector property that
  makes this link the most contestable step in the case for {VERB}}."
```

**Conditions line format:**
- Count: `CONTRADICTS count = 0`
- Ratio: `readiness distribution = 7/9 CONFIRMS`
- Threshold with comparator: `gap-closure cost < 1 sprint`

Prohibited: adjectives without a reference value.

The `(verify: {section}, {field-type})` in the Conditions line must match the pre-committed
value for Site 1 in CONDITIONS-PRECOMMIT.

The Recommendation verb in Beat 4.5 must match the verb in the Verdict section. If they
diverge, revise the Verdict section first.

Do not write Beat 5 until all six elements are consistent.

**Beat 5 -- Recommendation**

**Sub-step A -- CHALLENGER**

The CHALLENGER argues that the stated verdict is the wrong call, citing specific evidence.

```
CHALLENGER-CLAIM: [adjacent verb] -- [one sentence citing the specific evidence-state element
  -- a ledger entry by artifact name, a Beat 4 Gap, or a declared vector property -- that
  the CHALLENGER claims overrides the stated verdict]
```

Optional CHALLENGER paragraph (up to four sentences referencing the named element).

**Sub-step B -- AUTHOR**

```
AUTHOR-RULING: [one sentence: the ruling-out claim -- references the same element the
  CHALLENGER named and explains why the current evidence state resolves in favor of the
  stated verdict]
AUTHOR-CONDITIONS: {category} = {value} (verify: {section}, {field-type}) -- [one sentence:
  why this value maps to the stated verb, not the adjacent one named by the CHALLENGER]
```

The `(verify: ...)` pointer in AUTHOR-CONDITIONS must match the pre-committed value for
Site 2 in CONDITIONS-PRECOMMIT.

Optional AUTHOR paragraph (up to four sentences).

**Multi-site five-field compliance record**
*(run after Sub-step B, before the recommendation paragraph)*:

Complete all ten fields. Do not combine sites or skip fields.

```
*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language statement of what the conditions clause requires -- NOT a
    copy of the clause itself; one sentence explaining what must be true]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]:
              "(verify: {section}, {field-type})"
  VERIFIED:   [satisfied / not-yet-satisfied] -- [one sentence: name the specific evidence
    -- a ledger entry by artifact name, a reconciliation row, or a Beat 4 gap -- that
    confirms or fails to confirm the condition]
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
- CONDITION: a plain-language restatement, not a copy of the clause. If the two sentences
  would be identical, rewrite CONDITION in different words.
- VALUE: the verbatim `(verify: ...)` pointer, with TRANSCRIBED FROM attribution -- copied
  from the source location, not re-derived from memory.
- VERIFIED: names the basis explicitly. "satisfied" without a basis sentence fails C-39.
- MATCH: states both pre-committed and transcribed values side by side, then declares Status.

Do not write the recommendation paragraph until all ten fields are present and both MATCH
statuses show MATCH.

**Recommendation paragraph**

One of: **proceed**, **pause**, **pivot**, **abandon** (must match Verdict section exactly).
Full directive: what to do, under what conditions, with what scope. Does not repeat the
labeled claims from the CHALLENGER/AUTHOR exchange.

---

**Voice**: You opened with a verdict. Every beat that follows is justification. The
CHAIN-AUDIT checks whether each derivation step earns the conclusion you already stated --
not how you discovered it. "Stated verdict: {VERB}" is the anchor; ADEQUATE means this step
genuinely supports {VERB}, INADEQUATE means a reasonable person could accept this step and
still doubt {VERB}. The weakest justification link is where the verdict is most vulnerable.
The five-field compliance record makes the verification self-contained: CONDITION restates
what must be true, VERIFIED names what was found and why it confirms that requirement. The
recommendation paragraph is directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]

## CONDITIONS-PRECOMMIT
- Site 1 (Beat 4.5): Pre-committed section: [section] / Pre-committed field-type: [field-type]
- Site 2 (AUTHOR-CONDITIONS): Pre-committed section: [section] / Pre-committed field-type: [field-type]

## Verdict
**PROCEED | PAUSE | PIVOT | ABANDON** -- [one-sentence directive]

## Story

### Beat 1 -- What we set out to understand
...

### Beat 2 -- What each signal revealed
...

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector] -- consistent with the stated verdict.
[anchored claims] [Conflict / Verdict entries]

### Beat 4 -- What remains uncertain
Gap: [unknown]
Most exposed finding: [ledger entry]
Next signal: {namespace}/{skill} -- [expected finding]

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} -- [mechanism sentence]
Recommendation verb: {VERB} -- [licensing sentence]
Adjacent verb: {ADJACENT-VERB} -- [contestation claim]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why value maps]
CHAIN-AUDIT (justification): Stated verdict: {VERB}. S0 -> ledger: ADEQUATE -- [reason,
  refs {VERB}]; ledger -> S3 ([vector]): ADEQUATE -- [reason, refs {VERB}];
  S3 -> {verb}: ADEQUATE -- [reason, refs {VERB}]; Conditions -> Beat 5: ADEQUATE --
  [reason, refs {VERB}]. Weakest justification link: [{link-name}] -- {artifact or property}.

### Beat 5 -- Recommendation

**CHALLENGER-CLAIM**: [adjacent verb] -- [specific element]
[Optional CHALLENGER paragraph]

**AUTHOR-RULING**: [ruling-out claim]
**AUTHOR-CONDITIONS**: {category} = {value} (verify: {section}, {field-type}) -- [why]
[Optional AUTHOR paragraph]

*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language requirement, not a copy of the clause]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis: ledger entry or Beat 4 gap]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

Site 2 -- AUTHOR-CONDITIONS:
  CONDITION:  [plain-language requirement]
  LOCATION:   Beat 5 / AUTHOR-CONDITIONS
  VALUE:      TRANSCRIBED FROM [Beat 5 > AUTHOR-CONDITIONS > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

**PROCEED | PAUSE | PIVOT | ABANDON** -- [full directive paragraph]
```

---

## V-02

**Variation axis**: C-38 isolation -- named-rival weakest-link identification with formal-
imperative CHAIN-AUDIT instruction. INERTIA-CLAIM declared as structural element before
writing the verdict. The weakest-link sentence must quote the INERTIA-CLAIM text explicitly.
Standard four-field MATCH-CHECK compliance (no VERIFIED field; C-39 absent). All other
mechanisms from V-02 R19: verdict-first, C-37 justification framing, minimal compliance,
no C-30.

**Hypothesis**: C-38 requires two conditions: (1) an INERTIA-CLAIM declared as a named
structural element, and (2) a formal-imperative CHAIN-AUDIT instruction that demands the
quoted-claim form in the weakest-link sentence. V-02 R19 sourced C-38 with this combination.
V-04/V-05 R19 failed C-38 despite carrying an INERTIA-CLAIM because their explanatory-register
CHAIN-AUDIT instructions produced weakest-link sentences that referenced the inertia position
without quoting it. V-02 R20 preserves the formal-imperative register from V-02 R19 and
strengthens the quoted-rival requirement with an explicit format spec and a named-rival
compliance check. If V-02 achieves C-38 while failing C-39 (four-field audit), independence
of C-38 from C-39 is confirmed.

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
Hypothesis at S3: [one sentence -- working hypothesis after all stances]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: which stances, on which dimension; reference at least one artifact name]
```

**Anti-stagnation check**: If S3 = S0, explain why explicitly.
**Reconciliation check**: CONFIRMED with unresolved CONTRADICTS -> revise to QUALIFIED.

Do not begin the story beats until the ledger is complete.

---

### Step 2b -- INERTIA-CLAIM declaration

Before writing CONDITIONS-PRECOMMIT, declare the status-quo competitor.

```
INERTIA-CLAIM: [one sentence: the specific default path or "skip" position the team would
  have maintained if no investigation had occurred. Not "do nothing" -- name the actual
  path: "continue on {path X} under the assumption that {condition}." This claim must be
  self-contained: a reader who has not read the signals should understand what the team
  was defaulting to.]
```

The INERTIA-CLAIM is referenced in three places: Beat 1 (the entering default), Beat 2
(each signal evaluated against it), and Beat 4.5 CHAIN-AUDIT (the named rival in the
weakest-justification-link sentence, quoted verbatim).

---

### Step 2c -- CONDITIONS-PRECOMMIT

Before writing any conditions clause, commit the pointer values for both conditions sites.

```
CONDITIONS-PRECOMMIT:
- Site 1 (Beat 4.5 Conditions line)
    Pre-committed section:    [section a reader checks to confirm the condition]
    Pre-committed field-type: [entry type within that section]
- Site 2 (AUTHOR-CONDITIONS in Beat 5)
    Pre-committed section:    [section a reader checks to confirm the condition]
    Pre-committed field-type: [entry type within that section]
```

All four fields must be real values before writing Beat 4.5. If a conditions clause
changes direction during writing, revise this block first.

---

### Step 3 -- Write the verdict headline

```
## Verdict

**{PROCEED | PAUSE | PIVOT | ABANDON}** -- [one sentence: the core directive. This commits
the recommendation before any evidence is shown. It defeats the INERTIA-CLAIM. Beat 5
defends it.]
```

---

### Step 4 -- Write the justification beats

**Beat 1 -- What we set out to understand**
One to three sentences. The original question and S0. Reference the INERTIA-CLAIM as the
entering default: "The entering default was [INERTIA-CLAIM]. The investigation asked whether
that default was warranted."

**Beat 2 -- What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence -- what the finding means for the INERTIA-CLAIM.
Does this signal support continuing with the inertia position, or does it challenge it?
Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open with: "Across [N] signals, the hypothesis was [vector] -- consistent with the stated
verdict."

**Anchor citation rule**: Every non-trivial claim cites the licensing ledger entry:
`(anchored: {artifact-name}, {stance})`.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every Conflict verdict carries a because-clause.

**Falsifiability test**: Does any single entry carry the Beat 3 conclusion alone? Revisit
if yes.

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [ledger entry whose claim cannot be confirmed without this]
Next signal: {namespace}/{skill} -- [one sentence: expected finding type]
```

**Beat 4.5 -- Derivation chain** *(written after CONDITIONS-PRECOMMIT is complete)*

Six elements, each on its own line. No placeholders.

```
Anchored claim: "[exact S3 claim from Beat 3, copied verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence, verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: why the vector
  licenses this verb; must match the Verdict section]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: what would have to
  be true for the adjacent verb to apply instead]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why this value maps
  to the recommendation verb rather than the adjacent one]
CHAIN-AUDIT (justification): The first sentence must state the pre-committed verdict verbatim:
  "Stated verdict: {VERB}." For each link, state ADEQUATE or INADEQUATE for the stated verdict
  with a reason that references {VERB} explicitly:
    S0 -> ledger: ADEQUATE | INADEQUATE -- [reason referencing {VERB} vs INERTIA-CLAIM]
    ledger -> S3 ([vector]): ADEQUATE | INADEQUATE -- [reason]
    S3 -> {verb}: ADEQUATE | INADEQUATE -- [reason]
    Conditions ({category}={value}) -> Beat 5: ADEQUATE | INADEQUATE -- [reason]
  Close with the weakest-justification-link sentence. This sentence MUST name the INERTIA-CLAIM
  verbatim in this exact form:
    "Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
    is most contestable here because {specific artifact name or vector property}."
  The INERTIA-CLAIM text must appear quoted in that sentence. Referencing "the inertia position"
  or "the default" without quoting the actual INERTIA-CLAIM sentence is not sufficient.
```

**Conditions line format:**
- Count: `CONTRADICTS count = 0`
- Ratio: `readiness distribution = 7/9 CONFIRMS`
- Threshold with comparator: `gap-closure cost < 1 sprint`

Prohibited: adjectives without a reference value.

The `(verify: {section}, {field-type})` in Conditions must match Site 1 in CONDITIONS-PRECOMMIT.
The Recommendation verb must match the Verdict section. Fix Verdict section if they diverge.

Do not write Beat 5 until all six elements are consistent.

**Beat 5 -- Recommendation**

**Sub-step A -- CHALLENGER**

The CHALLENGER argues that the stated verdict is wrong and the INERTIA-CLAIM is defensible:

```
CHALLENGER-CLAIM: [adjacent verb] -- [one sentence: the specific evidence-state element --
  a ledger entry by artifact name, a Beat 4 Gap, or a declared vector property -- that the
  CHALLENGER claims makes the INERTIA-CLAIM defensible against the stated verdict]
```

Optional CHALLENGER paragraph (up to four sentences).

**Sub-step B -- AUTHOR**

```
AUTHOR-RULING: [one sentence: references the same element the CHALLENGER named and states
  why the current evidence state defeats the INERTIA-CLAIM in favor of the stated verdict]
AUTHOR-CONDITIONS: {category} = {value} (verify: {section}, {field-type}) -- [one sentence:
  why this value maps to the stated verb, not the adjacent one]
```

The `(verify: ...)` pointer must match Site 2 in CONDITIONS-PRECOMMIT.

Optional AUTHOR paragraph (up to four sentences).

**Multi-site compliance audit record with MATCH-CHECK**
*(run after Sub-step B, before the recommendation paragraph)*:

Two layers. Complete them in sequence.

**Layer 1 -- Transcription** *(copy from source; do not re-derive)*:

```
Transcription:
  Site 1 (Beat 4.5): TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]: "{exact text}"
  Site 2 (AUTHOR-CONDITIONS): TRANSCRIBED FROM [Beat 5 > AUTHOR-CONDITIONS > verify field]: "{exact text}"
```

**Layer 2 -- MATCH-CHECK**:

```
MATCH-CHECK:
  Site 1: Pre-committed ({section}, {field-type}) vs Transcribed ("{exact text from Layer 1}")
          Status: MATCH [checkmark]  [or: MISMATCH -- state discrepancy; revise PRECOMMIT]
  Site 2: Pre-committed ({section}, {field-type}) vs Transcribed ("{exact text from Layer 1}")
          Status: MATCH [checkmark]  [or: MISMATCH -- state discrepancy; revise PRECOMMIT]
```

After both checks pass:

```
*Multi-site compliance [pre-committed + transcribed]: Beat 4.5 (verify: {section}, {field-type}) MATCH [checkmark] | AUTHOR-CONDITIONS (verify: {section}, {field-type}) MATCH [checkmark]*
```

**Named-rival compliance check** *(run before the recommendation paragraph)*:

```
NAMED-RIVAL CHECK:
  INERTIA-CLAIM declared: [YES -- quote the exact text from the INERTIA-CLAIM block]
  Weakest-link sentence: [copy the full "Weakest justification link:" sentence from CHAIN-AUDIT]
  Rival appears quoted: [YES / NO -- confirm '{INERTIA-CLAIM}' text appears quoted in sentence]
  Status: PASS | FAIL
```

Do not write the recommendation paragraph if either the MATCH-CHECK or NAMED-RIVAL CHECK fails.

**Recommendation paragraph**

One of: **proceed**, **pause**, **pivot**, **abandon** (must match Verdict section exactly).
Full directive: what to do, under what conditions, with what scope. Names what the
investigation established over the INERTIA-CLAIM. Does not repeat labeled claims.

---

**Voice**: The INERTIA-CLAIM is the named rival this verdict defeats. It appears in Beat 1 as
the entering default, in Beat 2 as the foil each signal is measured against, and in Beat 4.5
as the named alternative in the weakest-justification-link sentence. The CHAIN-AUDIT does not
trace how you discovered the conclusion -- it asks whether each derivation step earns the
conclusion you already committed. The weakest link is where the case for {VERB} over the
specific rival is most contestable: naming the rival explicitly, quoted, makes the comparison
auditable. The compliance record confirms pointer values were planned before writing.
The recommendation paragraph is directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]

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
[per-signal editorial sentence evaluated against INERTIA-CLAIM]

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector] -- consistent with the stated verdict.
[anchored claims] [Conflict / Verdict entries]

### Beat 4 -- What remains uncertain
Gap: [unknown] / Most exposed finding: [entry] / Next signal: {namespace}/{skill} -- [finding]

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} -- [mechanism sentence]
Recommendation verb: {VERB} -- [licensing sentence]
Adjacent verb: {ADJACENT-VERB} -- [contestation claim]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why value maps]
CHAIN-AUDIT (justification): Stated verdict: {VERB}.
  S0 -> ledger: ADEQUATE -- [reason, refs {VERB} vs INERTIA-CLAIM];
  ledger -> S3 ([vector]): ADEQUATE -- [reason]; S3 -> {verb}: ADEQUATE -- [reason];
  Conditions -> Beat 5: ADEQUATE -- [reason].
  Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
  is most contestable here because {artifact or vector property}.

### Beat 5 -- Recommendation

**CHALLENGER-CLAIM**: [adjacent verb] -- [element supporting INERTIA-CLAIM]
[Optional CHALLENGER paragraph]

**AUTHOR-RULING**: [ruling-out claim defeating INERTIA-CLAIM]
**AUTHOR-CONDITIONS**: {category} = {value} (verify: {section}, {field-type}) -- [why]
[Optional AUTHOR paragraph]

Transcription:
  Site 1 (Beat 4.5): TRANSCRIBED FROM [...]: "{exact text}"
  Site 2 (AUTHOR-CONDITIONS): TRANSCRIBED FROM [...]: "{exact text}"

MATCH-CHECK:
  Site 1: Pre-committed ({section}, {field-type}) vs Transcribed ("{exact text}") -- Status: MATCH [checkmark]
  Site 2: Pre-committed ({section}, {field-type}) vs Transcribed ("{exact text}") -- Status: MATCH [checkmark]

*Multi-site compliance [pre-committed + transcribed]: Beat 4.5 (verify: {section}, {field-type}) MATCH [checkmark] | AUTHOR-CONDITIONS (verify: {section}, {field-type}) MATCH [checkmark]*

NAMED-RIVAL CHECK:
  INERTIA-CLAIM declared: YES -- "[exact INERTIA-CLAIM text]"
  Weakest-link sentence: "Weakest justification link: [{link}] -- the case for {VERB} over '{INERTIA-CLAIM}' is most contestable here because {artifact}."
  Rival appears quoted: YES
  Status: PASS

**PROCEED | PAUSE | PIVOT | ABANDON** -- [full directive paragraph]
```

---

## V-03

**Variation axis**: Story-forward architecture + C-39 (five-field compliance). Tests whether
C-39 is architecture-neutral. The VERIFIED field is added to a story-forward artifact that
uses discovery-path CHAIN-AUDIT framing. No INERTIA-CLAIM structural element. No verdict-first
architecture. C-12, C-37, and C-38 are all unavailable. C-39 is the sole new criterion tested.

**Hypothesis**: C-39 has no architecture restriction per the rubric. A story-forward artifact
can achieve the VERIFIED field (satisfaction basis in the compliance record) without a verdict
stated before evidence, without C-37 justification-audit framing, and without an INERTIA-CLAIM.
If V-03 achieves C-39 at a score of ~210 (story-forward base ~205 from V-03 R19 + 5 for C-39),
architecture-neutrality of C-39 is confirmed. If V-03 fails C-39, the VERIFIED field may be
operationally coupled to the verdict-first compliance flow in a way the rubric does not capture.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found. Read
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
Hypothesis at S3: [working hypothesis after all stances applied, one sentence]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: which stances, on which dimension, drove this; reference at least one artifact name]
```

**Anti-stagnation check**: If S3 = S0, explain explicitly.
**Reconciliation check**: CONFIRMED with unresolved CONTRADICTS -> QUALIFIED.

Do not begin the story beats until the ledger is complete.

---

### Step 2b -- CONDITIONS-PRECOMMIT

Commit pointer values for both conditions sites before writing any conditions clause.

```
CONDITIONS-PRECOMMIT:
- Site 1 (Beat 4.5 Conditions line)
    Pre-committed section:    [section where the condition value will be verified]
    Pre-committed field-type: [entry type within that section]
- Site 2 (AUTHOR-CONDITIONS in Beat 5)
    Pre-committed section:    [section where the condition value will be verified]
    Pre-committed field-type: [entry type within that section]
```

All four fields must have real values before writing Beat 4.5. If a conditions clause
changes direction, update this block first.

---

### Step 3 -- Write the story beats

This story opens with context. The recommendation appears at the end, after the evidence.

**Beat 1 -- What we set out to understand**
One to three sentences. The original question and S0. Name the entering default: what the
team expected to confirm, and why. Name the status-quo path the team would have taken
without investigation.

**Beat 2 -- What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding. What does this signal mean
as evidence? Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open with: "Across [N] signals, the hypothesis was [vector]."

**Anchor citation rule**: Every non-trivial claim names its source:
`(anchored: {artifact-name}, {stance})`.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would provide the missing evidence]
```

Every Conflict verdict carries a because-clause.

**Falsifiability test**: Does any single entry carry the Beat 3 conclusion alone? Revisit
if yes.

**Beat 4 -- What remains uncertain (structured risk register)**

Three tiers, all completed before writing Beat 4.5.

**Tier 1 -- Gap catalog**

```
Gap [{ID}]: [testable question -- not a vague category]
  Risk tier: BLOCKING | MAJOR | MINOR
  Blocking rationale: [if BLOCKING: why this must close before the recommendation can hold;
    if MAJOR/MINOR: bounded scope of the risk, one sentence]
  Most exposed finding: [ledger entry whose claim depends on closing this gap]
```

Label gaps G-01, G-02, etc. At least one gap must be BLOCKING or MAJOR; if all gaps are
MINOR, justify the absence of higher-tier gaps explicitly.

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
  Prerequisite: [G-ID of prerequisite, or "none"]
```

**Beat 4.5 -- Derivation chain** *(written after CONDITIONS-PRECOMMIT is complete)*

Six elements, each on its own line. No placeholders.

```
Anchored claim: "[exact S3 claim from Beat 3, copied verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence, verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: why the vector
  licenses this verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: specific contestation
  claim; may reference a specific Beat 4 gap tier]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why this value maps
  to the recommendation verb; may reference a Beat 4 gap tier label]
CHAIN-AUDIT: S0 -> {N} ledger entries -> S3 ([vector]) -> {verb} -> Conditions
  ({category}={value}) -> Beat 5 ruling. Enumerate every link in this chain. Name the
  weakest link: the step most dependent on a single ledger entry. Name that entry. If a
  BLOCKING gap is the most exposed dependency, name it as the source of the weakest link's
  vulnerability. [Note: this is discovery-path framing. Do NOT open with "Stated verdict:"
  and do NOT evaluate ADEQUATE/INADEQUATE per link. C-37 is unavailable for this artifact.]
```

**Conditions line format:**
- Count, ratio, or threshold with comparator. No bare adjectives.

The `(verify: ...)` pointer must match Site 1 in CONDITIONS-PRECOMMIT.

Do not write Beat 5 until all six derivation chain elements are consistent.

**Beat 5 -- Recommendation**

**Sub-step A -- CHALLENGER**

The CHALLENGER must cite a specific Beat 4 risk-register entry:

```
CHALLENGER-CLAIM: [adjacent verb] -- [one sentence citing a specific gap ID (e.g., "G-01,
  a BLOCKING gap in...") or tier-labeled gap property that overrides the recommendation verb]
```

Optional CHALLENGER paragraph (up to four sentences).

**Sub-step B -- AUTHOR**

```
AUTHOR-RULING: [one sentence: references the same gap entry cited by CHALLENGER; explains
  why the current tier assignment or critical-path position resolves in favor of the verb]
AUTHOR-CONDITIONS: {category} = {value} (verify: {section}, {field-type}) -- [one sentence:
  why this value maps to this verb, not the adjacent one]
```

The `(verify: ...)` pointer must match Site 2 in CONDITIONS-PRECOMMIT.

Optional AUTHOR paragraph (up to four sentences).

**Multi-site five-field compliance record**
*(run after Sub-step B, before the recommendation paragraph)*:

```
*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language statement of what the conditions clause requires -- NOT a
    copy of the clause itself; one sentence]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]:
              "(verify: {section}, {field-type})"
  VERIFIED:   [satisfied / not-yet-satisfied] -- [one sentence: name the specific evidence
    -- a ledger entry by artifact name, reconciliation row, or gap tier -- that confirms
    or fails to confirm the condition]
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

Do not write the recommendation paragraph until all ten fields are present and both MATCH
statuses show MATCH.

**Recommendation paragraph**

One of: **proceed**, **pause**, **pivot**, **abandon**. Full directive: what to do, under
what conditions, with what scope. May reference gap-tier resolution conditions. Does not
repeat labeled claims.

---

**Voice**: This story opens with context and builds toward a recommendation. The discovery
arc is genuine -- Beat 1 states what was unknown, Beat 2 traces what each signal added, Beat
3 synthesizes what they say together, Beat 4 names what is still uncertain. The CHAIN-AUDIT
enumerates the derivation path rather than justifying a pre-stated conclusion. The five-field
compliance record makes the conditions verification self-contained: CONDITION states what must
be true, VERIFIED names what was found and why it confirms or fails to confirm that requirement.
The recommendation is directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]

## CONDITIONS-PRECOMMIT
- Site 1 (Beat 4.5): Pre-committed section: [section] / Pre-committed field-type: [field-type]
- Site 2 (AUTHOR-CONDITIONS): Pre-committed section: [section] / Pre-committed field-type: [field-type]

## Story

### Beat 1 -- What we set out to understand
[question + S0 + entering default + status-quo path]

### Beat 2 -- What each signal revealed
[per-signal editorial sentence]

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector].
[anchored claims] [Conflict / Verdict entries]

### Beat 4 -- What remains uncertain

**Tier 1 -- Gap catalog**
Gap [G-01]: [testable question]
  Risk tier: BLOCKING
  Blocking rationale: [...]
  Most exposed finding: [ledger entry]
...

**Tier 2 -- Critical-path analysis**
Critical path: [G-01] -> [G-02] / Rationale: [dependency]

**Tier 3 -- Resolution sequencing**
Resolution [G-01]: Priority: BLOCKING / Next signal: {namespace}/{skill} -- [...] / Prerequisite: none
...

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} -- [mechanism sentence]
Recommendation verb: {VERB} -- [licensing sentence]
Adjacent verb: {ADJACENT-VERB} -- [contestation claim; may reference gap tier]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why value maps]
CHAIN-AUDIT: S0 -> {N} entries -> S3 ([vector]) -> {verb} -> Conditions -> Beat 5.
  Weakest link: [{link-name}, dependent on {artifact}; {BLOCKING gap if applicable}]

### Beat 5 -- Recommendation

**CHALLENGER-CLAIM**: [adjacent verb] -- [{G-ID}, a {tier} gap in...]
[Optional CHALLENGER paragraph]

**AUTHOR-RULING**: [gap-entry ruling]
**AUTHOR-CONDITIONS**: {category} = {value} (verify: {section}, {field-type}) -- [why]
[Optional AUTHOR paragraph]

*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language requirement]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis: ledger entry or gap tier]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

Site 2 -- AUTHOR-CONDITIONS:
  CONDITION:  [plain-language requirement]
  LOCATION:   Beat 5 / AUTHOR-CONDITIONS
  VALUE:      TRANSCRIBED FROM [Beat 5 > AUTHOR-CONDITIONS > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis]
  MATCH:      Pre-committed: ({section}, {field-type}) vs Transcribed: "(verify: {section}, {field-type})"
              Status: MATCH [checkmark]

**PROCEED | PAUSE | PIVOT | ABANDON** -- [full directive paragraph; may reference gap-tier closure]
```

---

## V-04

**Variation axes**: C-38 + C-39 combined, minimal compliance. Verdict-first with INERTIA-CLAIM
structural element (enables C-38). Five-field compliance record with VERIFIED field (C-39).
Formal-imperative CHAIN-AUDIT instruction with quoted-rival weakest-link (C-38). No C-30
reconciliation table. Tests additivity: can both new criteria be achieved simultaneously
without the reconciliation table or structured risk register?

**Hypothesis**: C-38 and C-39 are structurally independent -- C-38 operates at the derivation-
chain audit layer, C-39 operates at the compliance record layer. They do not share a dependency
that would cause interference when both are active. V-04 R20 combines the C-38 mechanism from
V-02 (INERTIA-CLAIM + formal CHAIN-AUDIT weakest-link) with the C-39 mechanism from V-01
(five-field compliance with VERIFIED). Keeping C-30 absent ensures the score increase from
V-02 or V-01 baselines comes only from the new criterion addition: ~202.5 + 5 (C-38) + 5
(C-39) = ~212.5. If V-04 matches that expectation, both criteria are confirmed additive.

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
Hypothesis at S3: [one sentence -- working hypothesis after all stances]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: which stances, on which dimension; reference at least one artifact name]
```

**Anti-stagnation check**: If S3 = S0, explain why explicitly.
**Reconciliation check**: CONFIRMED with unresolved CONTRADICTS -> QUALIFIED.

Do not begin the story beats until the ledger is complete.

---

### Step 2b -- INERTIA-CLAIM declaration

Before writing CONDITIONS-PRECOMMIT, declare the status-quo competitor.

```
INERTIA-CLAIM: [one sentence: the specific default path the team would have maintained
  without investigation. Named precisely: "continue on {path X} under the assumption that
  {condition}." Self-contained: a reader who has not seen the signals should understand
  what was being defaulted to.]
```

The INERTIA-CLAIM appears in Beat 1 (entering default), Beat 2 (foil for per-signal
evaluation), and Beat 4.5 CHAIN-AUDIT (quoted verbatim in the weakest-justification-link
sentence).

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

### Step 3 -- Write the verdict headline

```
## Verdict

**{PROCEED | PAUSE | PIVOT | ABANDON}** -- [one sentence: the core directive. Commits the
recommendation before any evidence is shown. Defeats the INERTIA-CLAIM. Beat 5 defends it.]
```

---

### Step 4 -- Write the justification beats

**Beat 1 -- What we set out to understand**
One to three sentences. The original question and S0. Reference the INERTIA-CLAIM as the
entering default: "The entering default was [INERTIA-CLAIM]. The investigation asked whether
that default was warranted."

**Beat 2 -- What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence -- what the finding means for the INERTIA-CLAIM.
Does this signal support continuing with the inertia position, or does it challenge it?
Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open with: "Across [N] signals, the hypothesis was [vector] -- consistent with the stated
verdict."

**Anchor citation rule**: Every non-trivial claim cites the licensing ledger entry:
`(anchored: {artifact-name}, {stance})`.

For every tension between stances:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension of disagreement]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every Conflict verdict carries a because-clause.

**Falsifiability test**: Does any single entry carry the Beat 3 conclusion alone? Revisit if yes.

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [ledger entry whose claim cannot be confirmed without this]
Next signal: {namespace}/{skill} -- [one sentence: expected finding type]
```

**Beat 4.5 -- Derivation chain** *(written after CONDITIONS-PRECOMMIT is complete)*

Six elements, each on its own line. No placeholders.

```
Anchored claim: "[exact S3 claim from Beat 3, copied verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence, verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: why the vector
  licenses this verb; must match the Verdict section]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: what would have to
  be true for the adjacent verb to apply instead]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why this value maps
  to the recommendation verb rather than the adjacent one]
CHAIN-AUDIT (justification): The first sentence must state the pre-committed verdict verbatim:
  "Stated verdict: {VERB}." For each link, state ADEQUATE or INADEQUATE for {VERB} with a
  reason referencing the stated verdict explicitly:
    S0 -> ledger: ADEQUATE | INADEQUATE -- [reason referencing {VERB} vs INERTIA-CLAIM]
    ledger -> S3 ([vector]): ADEQUATE | INADEQUATE -- [reason]
    S3 -> {verb}: ADEQUATE | INADEQUATE -- [reason]
    Conditions ({category}={value}) -> Beat 5: ADEQUATE | INADEQUATE -- [reason]
  Weakest-justification-link sentence (REQUIRED FORMAT):
    "Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
    is most contestable here because {specific artifact name or vector property}."
  The INERTIA-CLAIM text must be quoted verbatim. "The inertia position" or "the default"
  without the actual claim text does not satisfy this requirement.
```

**Conditions line format:**
- Count: `CONTRADICTS count = 0`
- Ratio: `readiness distribution = 7/9 CONFIRMS`
- Threshold with comparator: `gap-closure cost < 1 sprint`

Prohibited: adjectives without a reference value.

The `(verify: ...)` in Conditions must match Site 1 in CONDITIONS-PRECOMMIT.
The Recommendation verb must match the Verdict section. Fix Verdict section if they diverge.

Do not write Beat 5 until all six elements are consistent.

**Beat 5 -- Recommendation**

**Sub-step A -- CHALLENGER**

The CHALLENGER argues the stated verdict is wrong and the INERTIA-CLAIM is defensible:

```
CHALLENGER-CLAIM: [adjacent verb] -- [one sentence: the specific evidence-state element --
  a ledger entry by artifact name, a Beat 4 Gap, or a declared vector property -- that
  makes the INERTIA-CLAIM defensible against the stated verdict]
```

Optional CHALLENGER paragraph (up to four sentences).

**Sub-step B -- AUTHOR**

```
AUTHOR-RULING: [one sentence: references the same element the CHALLENGER named; states
  why the current evidence state defeats the INERTIA-CLAIM in favor of the stated verdict]
AUTHOR-CONDITIONS: {category} = {value} (verify: {section}, {field-type}) -- [one sentence:
  why this value maps to the stated verb, not the adjacent one]
```

The `(verify: ...)` pointer must match Site 2 in CONDITIONS-PRECOMMIT.

Optional AUTHOR paragraph (up to four sentences).

**Multi-site five-field compliance record**
*(run after Sub-step B, before the recommendation paragraph)*:

```
*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language statement of what the conditions clause requires -- NOT a
    copy of the clause itself; one sentence explaining what must be true]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]:
              "(verify: {section}, {field-type})"
  VERIFIED:   [satisfied / not-yet-satisfied] -- [one sentence: name the specific evidence
    -- a ledger entry by artifact name, or a Beat 4 gap -- that confirms the condition]
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

Do not write the recommendation paragraph if either the five-field compliance or the
NAMED-RIVAL CHECK fails.

**Recommendation paragraph**

One of: **proceed**, **pause**, **pivot**, **abandon** (must match Verdict section exactly).
Full directive: what to do, under what conditions, with what scope. Names what the
investigation established over the INERTIA-CLAIM. Does not repeat labeled claims.

---

**Voice**: Two independent mechanisms are active simultaneously. The CHAIN-AUDIT names the
inertia rival explicitly in the weakest-link sentence -- this is not a rhetorical device but
a structural requirement that makes the comparison auditable. The five-field compliance record
makes conditions verification self-contained: CONDITION restates what must be true, VERIFIED
names what was found and why it confirms that requirement. Neither mechanism depends on the
other: the named-rival test operates at the derivation-chain layer, the VERIFIED test operates
at the compliance record layer. The recommendation paragraph is directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]

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
[per-signal editorial sentence against INERTIA-CLAIM]

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector] -- consistent with the stated verdict.
[anchored claims] [Conflict / Verdict entries]

### Beat 4 -- What remains uncertain
Gap: [unknown] / Most exposed finding: [entry] / Next signal: {namespace}/{skill} -- [finding]

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim]" (anchored: {artifact-name}, {stance})
Net vector: {vector} -- [mechanism sentence]
Recommendation verb: {VERB} -- [licensing sentence]
Adjacent verb: {ADJACENT-VERB} -- [contestation claim]
Conditions: {category} = {value} (verify: {section}, {field-type}) -- [why value maps]
CHAIN-AUDIT (justification): Stated verdict: {VERB}.
  S0 -> ledger: ADEQUATE -- [reason, refs {VERB}]; ledger -> S3 ([vector]): ADEQUATE --
  [reason]; S3 -> {verb}: ADEQUATE -- [reason]; Conditions -> Beat 5: ADEQUATE -- [reason].
  Weakest justification link: [{link-name}] -- the case for {VERB} over '{INERTIA-CLAIM}'
  is most contestable here because {artifact or vector property}.

### Beat 5 -- Recommendation

**CHALLENGER-CLAIM**: [adjacent verb] -- [element supporting INERTIA-CLAIM]
[Optional CHALLENGER paragraph]

**AUTHOR-RULING**: [ruling-out claim defeating INERTIA-CLAIM]
**AUTHOR-CONDITIONS**: {category} = {value} (verify: {section}, {field-type}) -- [why]
[Optional AUTHOR paragraph]

*Compliance record*

Site 1 -- Beat 4.5 Conditions:
  CONDITION:  [plain-language requirement, not a copy]
  LOCATION:   Beat 4.5 / Conditions line
  VALUE:      TRANSCRIBED FROM [Beat 4.5 > Conditions line > verify field]: "(verify: {section}, {field-type})"
  VERIFIED:   satisfied -- [basis: ledger entry or Beat 4 gap]
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

**PROCEED | PAUSE | PIVOT | ABANDON** -- [full directive paragraph]
```

---

## V-05

**Variation axes**: Full ceiling -- C-38 + C-39 + C-30 + structured risk register (Beat 4) +
all compliance mechanisms. Verdict-first with INERTIA-CLAIM. Formal-imperative CHAIN-AUDIT
with quoted-rival weakest-link (C-38). Five-field compliance record with VERIFIED (C-39).
Vector-verdict reconciliation table (C-30). Three-tier risk register in Beat 4. Target: ~227.5
(verdict-first ceiling under v18: 230 - 2.5 for C-10).

**Hypothesis**: V-05 R19 scored ~217.5 under v17 (C-10 was the only miss). Under v18, V-05
R19 achieves C-39 (source of the criterion) but fails C-38 (explanatory register diluted the
quoted-rival format in the weakest-link sentence). V-05 R20 replaces the explanatory CHAIN-AUDIT
instruction with a formal-imperative instruction that requires the exact quoted-rival format.
All other mechanisms from V-05 R19 are preserved: reconciliation table, INERTIA-CLAIM, risk
register, five-field compliance, justification-audit framing. If V-05 R20 achieves ~227.5,
C-38 is register-dependent (formal instruction required) and all six active mechanisms are
simultaneously non-interfering.

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
