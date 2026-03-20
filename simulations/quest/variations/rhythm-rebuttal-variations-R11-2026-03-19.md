Written to `simulations/quest/variations/rhythm-rebuttal-variations-R11-2026-03-19.md`.

---

**R11 Variations — V-01 through V-05**

**Axes:**
| Axis | What it tests |
|------|--------------|
| P (C-37) | Complete enumeration — Phase 7 back-refs name ALL upstream sources per gate |
| Q (C-38) | Canonical delegation — Phase 7 says "Apply the Forward-annotation repair paths:" rather than "Apply the repair paths:" |
| R (C-39) | Self-contained modules — Phase 2 and Phase 6a use individually labeled "Forward-annotation from Check X:" blocks |

**Predicted verdicts:**

| Variation | C-37 | C-38 | C-39 | Predicted |
|-----------|------|------|------|-----------|
| V-01 (P) | PASS | FAIL | FAIL | 29/31 |
| V-02 (Q) | FAIL | PASS | FAIL | 29/31 |
| V-03 (R) | FAIL | FAIL | PASS | 29/31 |
| V-04 (P+Q) | PASS | PASS | FAIL | 30/31 |
| V-05 (P+Q+R) | PASS | PASS | PASS | 31/31 |

**Key axis interaction (C-37 × C-39):** When Axis R adds a canonical `Forward-annotation from Check 2c:` block to Phase 2, Phase 2 becomes a third named upstream source for Check 2c. V-05's Check 2c back-reference therefore enumerates three sources — Phase 2, Phase 5, and Phase 6a — while V-01/V-04 (C-39 absent, Phase 2 in bullet format) only enumerate two. V-03 (C-39 only) adds Phase 2 as a canonical source but its back-reference still names only one, failing C-37.

**Excellence signals to watch for in V-05:**
1. Check 2c back-reference names three upstream phases (Phase 2 as new source from C-39)
2. Check 6b back-reference uses canonical labels: "Phase 6a Forward-annotation from Check 6b warned... and Phase 5 Forward-annotation from Check 6b warned..."
3. Phase 2 blocks are referable by name from Phase 7 — "Apply the Phase 2 repair paths:" becomes "Apply the Forward-annotation from Check 4 Part C repair paths:"
nstrates this three-source back-reference; V-01 and V-04 (C-39 absent, Phase 2 uses
bullet format) need only name Phase 5 and Phase 6a. The interaction is testable: V-03 (C-39
only) passes on module format but its back-reference still names only one source.

---

## Axis Rationales

**Axis P -- back-reference completeness gap**: C-34 (R9) requires a back-reference to exist
in Phase 7 when a gate failure class was forward-annotated upstream. An executor who fails
Check 6b sees a back-reference to Phase 6a. But Check 6b was ALSO forward-annotated in Phase
5 -- the executor who read Phase 6a but not Phase 5 still missed a warning. C-37 requires the
back-reference to name every upstream annotation that warned about this constraint, converting
"you missed a warning" into "you missed warnings at Phase 6a AND Phase 5." For Check 2c, the
interaction with C-39 adds Phase 2 as a third source in V-05.

**Axis Q -- repair delegation gap**: C-35 (R9) requires (a)/(b) repair paths in upstream
annotations. C-32 (R9) requires (a)/(b) in Phase 7 gate checks. When both surfaces carry
(a)/(b), they are independent copies that can diverge on edit. Axis Q requires Phase 7 to
name the upstream annotation as the authoritative repair source by its canonical label --
"Apply the Forward-annotation repair paths:" -- rather than restating the paths. Phase 7 then
delegates rather than duplicates. R10 V-05 already does this for Check 2c and Check 4 Part C;
the single-axis gap is Check 6b, which uses "Apply the repair paths:" without naming the
upstream annotation.

**Axis R -- upstream module completeness gap**: C-33 (R9) requires gate failure conditions
to be forward-annotated in upstream phases. C-35 (R9) adds (a)/(b) repair paths to those
upstream annotations. But neither criterion requires each gate's annotation to be an
independently labeled, self-contained unit. R10 V-05 Phase 5 uses canonical "Forward-annotation
from Check X:" blocks and passes C-39. Phase 2 uses a bullet list under a shared heading; Phase
6a uses a non-canonical heading ("Forward-annotation -- Check 6b failure condition with repair
paths:"). Axis R restructures Phase 2 and Phase 6a into canonical "Forward-annotation from
Check X:" modules matching the Phase 5 format, making each block independently actionable and
referable by label from Phase 7.

---

## V-01 -- Complete Back-Reference Enumeration (Axis P)

**Axis**: P only -- C-37 complete enumeration of all upstream sources in Phase 7 back-references
**Hypothesis**: When a Phase 7 gate failure class was forward-annotated from multiple upstream
phases, naming only one upstream source in the back-reference leaves the second warning
unaccounted. An executor who failed Check 6b learns they missed the Phase 6a annotation but
not the Phase 5 annotation. Adding complete enumeration -- naming both Phase 6a AND Phase 5
for Check 6b, and Phase 5 AND Phase 6a for Check 2c -- gives the executor the full breadth of
where they failed to catch the constraint. Phase 7 repair blocks do not delegate by label
(C-38 absent; "Apply the repair paths:" without naming upstream annotation). Phase 2 uses
bullet-list format under shared heading (C-39 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; downstream Phase 7 gate constraints are forward-annotated at
the Phase 2 commitment surface with labeled (a)/(b) repair paths. Phase 3.5 audits ambiguous
type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows carry forward
as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1 no-change entries
carries a separately labeled Forward-annotation for each applicable Phase 7 gate check, each
with embedded (a)/(b) repair paths. The amendment pass validates FLAGGED exchanges first,
audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to
REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM
CHANGE -- then checks for unflagged failures; Phase 6a carries an entity-type referent column
and a forward-annotated Check 6b annotation with (a)/(b) repair paths. Phase 7 structural
completion gate runs ten checks; each failing check whose constraint class was forward-
annotated from multiple upstream phases includes an explicit back-reference naming EVERY
upstream phase that warned about the constraint.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints with repair paths**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper
>   or author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with study-design basis. Location alone fails.
>   Repair paths if entity is not yet named:
>   (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>       paper location (statistical), named principle + study-design basis (methodological).
>   (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>       defensible -- an unresolved entity at commitment time will fail Check 2c at write time.
>
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision must be recorded in Phase 6a before write. Deferral fails
>   Part C regardless of how clearly the decision is stated in the cover letter.
>   Repair paths if a PRESSURE-DRIVEN shift occurs in Phase 6a:
>   (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with
>       the evidence category and specific instance in Phase 6a.
>   (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>       the scientific claim: state NO REINSTATE with a one-sentence description of the
>       specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

Correct Phase 3 table before proceeding if any assignment looks wrong.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

Correct Phase 3 table before proceeding. All P2/P3 assignments require entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. These rows carry forward
as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism causing over-explanation] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure causing over-concession] |
| F-03 | [R-NN] | too brief | [structural reason this concern gets under-addressed] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies -- no-change requires valid evidence form category AND
specific traceable instance; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."
  methodological: "We agree that [aspect]. [Scientific justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent (Author Year + locator for
  literature; statistic + paper location for statistical; named principle + study-design
  basis for methodological)]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 P1-NC pre-commitment and Phase 6a pre-commitment table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition with repair paths**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- it is faster to fix here where both artifacts are visible.

- P1 pre-commitment audit with entity-type referent column, SHIFTED classification, and
  decision closure:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7:
  - Prior literature: the cited paper or author (Author Year) -- not a section of this ms
  - Statistical result: the specific statistic and its paper location
  - Methodological argument: the named inferential principle and its study-design basis
  An entry with an empty or location-only entity-type referent fails Phase 6a. The referent
  must be present here -- it cannot be inserted at Phase 7 Check 2c as a last-second addition.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical weight without specific new scientific
    evidence. Decision required: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: author encountered specific named evidence not anticipated in Phase 2.
    Decision required: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority):
1. [R-NN] -- too defensive: [rewrite AUTHOR RESPONDS opening]
2. [R-NN] -- concedes too much: [what to hold; why the concession went too far]
3. [R-NN] -- too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write -- fix the failing check and re-run before proceeding.

**Check 1 -- Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern in Phase 3 with no exchange written: write the missing exchange in severity
      order before proceeding.
  (b) Two concerns merged into one REVIEWER SAID block: split into separate exchanges,
      each with its own REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be "[Section N]: [specific change]" or "No change -- [rationale]".
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME is a placeholder: write section + change description.
  (b) Outcome genuinely unresolved: use Phase 2 pre-commitments as baseline and record.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form anywhere: revise to introduce prior literature, methodological argument,
      or statistical result before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator (literature); named statistic + location (statistical); named principle
+ study-design basis (methodological).
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 Forward-annotation from Check 2c warned that entity-type specificity
  was required at authoring time, and Phase 6a entity-type referent column required the entity
  to be named during mid-workflow reconciliation -- an entry failing Check 2c missed that
  constraint at its earliest visible points.
  Apply the Forward-annotation repair paths:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Apply Forward-annotation path (b) --
      reclassify to CHANGE if no specific instance exists.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed: add parenthetical R-ID references to each change claim.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation for each.
  (b) Count mismatch: identify unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but note absent: write the re-examination note.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 forward-annotation warned that PRESSURE-DRIVEN entries must commit
  REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing Part C missed that
  constraint at its earliest visible point. Apply the Phase 2 repair paths:
  (a) Original RULE-1 evidence remains scientifically valid: state REINSTATE with the evidence
      category and specific instance. Record in Phase 6a before proceeding.
  (b) Change improved a non-scientific dimension: state NO REINSTATE with a one-sentence
      description of the specific improvement achieved.

**Check 5 -- Frontmatter integer verification**:
Compute from Phase 5 outcomes:
- reviewer_count: distinct reviewers in Phase 3
- concerns_addressed: total R-IDs in Phase 3
- manuscript_changes: R-IDs with CHANGE MANUSCRIPT OUTCOME
- no_change_responses: R-IDs with no-change MANUSCRIPT OUTCOME
CHECK: all four are integers, manuscript_changes + no_change_responses = concerns_addressed
-- PASS / FAIL
If FAIL:
  (a) String placeholders: replace each with the computed integer.
  (b) Inconsistent totals: recount from Phase 5 and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (updated in 6a) must include at least one parenthetical
R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted: add parenthetical reference.
  (b) No R-ID maps to the claim: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME (not "No change").
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  Back-reference: Phase 6a forward-annotation warned that Paragraph 1 change claims
  referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME, and Phase 5
  Forward-annotation from Check 6b warned of this constraint at the moment of authoring the
  MANUSCRIPT OUTCOME -- an entry failing Check 6b missed that constraint at its earliest
  visible points.
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 -- Phase 7 Canonical Delegation (Axis Q)

**Axis**: Q only -- C-38 Phase 7 repair blocks delegate to upstream annotation by canonical label
**Hypothesis**: R10 V-05 passes C-38 for Check 2c ("Apply the Forward-annotation repair paths:")
and Check 4 Part C ("Apply the Phase 2 repair paths:") but fails for Check 6b, which says
"Apply the repair paths:" without naming the upstream annotation. The single-axis addition is
completing the delegation pattern for Check 6b. Phase 7 back-references name only one upstream
source per check (C-37 absent). Phase 2 uses bullet-list format (C-39 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; downstream Phase 7 gate constraints are forward-annotated at
the Phase 2 commitment surface with labeled (a)/(b) repair paths. Phase 3.5 audits ambiguous
type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows carry forward
as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1 no-change entries
carries a separately labeled Forward-annotation for each applicable Phase 7 gate check, each
with embedded (a)/(b) repair paths. The amendment pass validates FLAGGED exchanges first,
audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to
REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM
CHANGE -- then checks for unflagged failures; Phase 6a carries an entity-type referent column
and a forward-annotated Check 6b annotation with (a)/(b) repair paths. Phase 7 structural
completion gate runs ten checks; every failing check's repair protocol names the upstream
Forward-annotation as the authoritative repair source by its canonical label rather than
restating (a)/(b) paths independently.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints with repair paths**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper
>   or author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with study-design basis. Location alone fails.
>   Repair paths if entity is not yet named:
>   (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>       paper location (statistical), named principle + study-design basis (methodological).
>   (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>       defensible -- an unresolved entity at commitment time will fail Check 2c at write time.
>
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision must be recorded in Phase 6a before write. Deferral fails
>   Part C regardless of how clearly the decision is stated in the cover letter.
>   Repair paths if a PRESSURE-DRIVEN shift occurs in Phase 6a:
>   (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with
>       the evidence category and specific instance in Phase 6a.
>   (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>       the scientific claim: state NO REINSTATE with a one-sentence description of the
>       specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data.] We have updated [location]."
  methodological: "We agree that [aspect]. [Justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added analysis / explained constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 P1-NC pre-commitment and Phase 6a pre-commitment table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition with repair paths**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- it is faster to fix here where both artifacts are visible.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7.
  An entry with empty or location-only referent fails Phase 6a. Cannot insert at Phase 7.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.
  SHIFTED: classify and re-examine:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED first, then unflagged.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED take priority):
1. [R-NN] -- too defensive: [rewrite]
2. [R-NN] -- concedes too much: [what to hold]
3. [R-NN] -- too brief: [what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) missing exchange: write it. (b) merged: split.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) placeholder: write it. (b) unresolved: use Phase 2 baseline.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL: (a) move from AUTHOR RESPONDS. (b) revise to introduce valid form.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 Forward-annotation from Check 2c warned that entity-type specificity
  was required at authoring time -- an entry failing Check 2c missed that constraint at its
  earliest visible point.
  Apply the Forward-annotation repair paths:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Apply Forward-annotation path (b) --
      reclassify to CHANGE if no specific instance exists.

**Check 3 -- Cover letter structure**:
CHECK: PASS / FAIL
If FAIL: (a) malformed: add R-ID references. (b) missing: draft from Phase 2 + Phase 5.

**Check 4 -- Forecast validation + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: CHECK: [n FLAGGED] vs [n validated rows] -- PASS / FAIL
Part B: CHECK: [n SHIFTED] vs [n classified + re-examined] -- PASS / FAIL
Part C: CHECK: [n PRESSURE-DRIVEN] vs [n with binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 forward-annotation warned that PRESSURE-DRIVEN entries must commit
  REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing Part C missed that
  constraint at its earliest visible point. Apply the Phase 2 repair paths:
  (a) Original RULE-1 evidence remains scientifically valid: state REINSTATE with category
      and specific instance. Record in Phase 6a.
  (b) Change improved a non-scientific dimension: state NO REINSTATE with one-sentence
      description of the specific improvement achieved.

**Check 5 -- Frontmatter integer verification**:
CHECK: all four values are integers, manuscript_changes + no_change_responses = concerns_addressed
If FAIL: (a) replace placeholders. (b) recount and correct.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID references -- PASS / FAIL per claim
If FAIL: (a) R-ID omitted: add. (b) no R-ID: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type -- PASS / FAIL
If FAIL:
  Back-reference: Phase 6a forward-annotation warned that Paragraph 1 change claims
  referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME -- an entry failing
  Check 6b missed that constraint at its earliest visible point.
  Apply the Forward-annotation repair paths:
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 -- Self-Contained Upstream Modules (Axis R)

**Axis**: R only -- C-39 Phase 2 and Phase 6a blocks restructured as individually labeled
"Forward-annotation from Check X:" self-contained modules
**Hypothesis**: Phase 5 already uses canonical "Forward-annotation from Check X:" blocks that
pass C-39. Phase 2 uses a bullet list under a shared "Forward-annotation -- downstream gate
constraints" heading. Phase 6a uses "Forward-annotation -- Check 6b failure condition with
repair paths:" (non-canonical dash form). Restructuring both into canonical "Forward-annotation
from Check X:" modules -- each with gate label, unconditional failure condition, and (a)/(b)
repair paths -- makes each block independently actionable without consulting Phase 7. Phase 7
back-references name only one upstream source per check (C-37 absent). Phase 7 repair blocks
do not use canonical delegation (C-38 absent; Check 6b says "Apply the repair paths:").

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are structured as individually labeled
"Forward-annotation from Check X:" modules -- one per applicable gate constraint -- each
containing the gate label, an unconditional failure condition, and (a)/(b) repair paths as a
self-contained unit the author can act on without consulting Phase 7. Phase 3.5 audits
ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows carry
forward as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1 no-change
entries carries the same canonical module format for each applicable Phase 7 gate check.
The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED
classification, closes PRESSURE-DRIVEN entries; Phase 6a carries an entity-type referent
column and a "Forward-annotation from Check 6b:" module with (a)/(b) repair paths. Phase 7
runs ten checks before write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation from Check 2c**: A P1 no-change evidence instance must name a
> concrete entity -- cited paper or author (Author Year, not a section of this manuscript),
> specific statistic with paper location, or named methodological principle with study-design
> basis. A location reference alone (App. B, section 3.2, Table 4) fails Check 2c even when
> the evidence category label is correctly named.
> Repair paths:
> (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>     paper location (statistical), named principle + study-design basis (methodological).
> (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>     defensible -- an unresolved entity at commitment time will fail Check 2c at write time.

> **Forward-annotation from Check 4 Part C**: If this pre-commitment is later SHIFTED to
> PRESSURE-DRIVEN in Phase 6a, a binding decision (REINSTATE or NO REINSTATE with a one-
> sentence rationale) must be recorded in Phase 6a before write. Deferring the decision to
> the cover letter fails Part C regardless of how clearly it appears there.
> Repair paths (if PRESSURE-DRIVEN shift occurs in Phase 6a):
> (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with the
>     evidence category and specific instance in Phase 6a.
> (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>     the scientific claim: state NO REINSTATE with a one-sentence description of the
>     specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data.] We have updated [location]."
  methodological: "We agree that [aspect]. [Justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added analysis / explained constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 P1-NC pre-commitment and Phase 6a pre-commitment table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation from Check 6b**: A Paragraph 1 change claim asserting "we changed X
> in response to R-NN" while R-NN's Phase 5 MANUSCRIPT OUTCOME is "No change" is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain, and
> Check 6b will block the write.
> Repair paths:
> (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>     it incorrectly -- the claim is accurate, the record is wrong.
> (b) Revise Paragraph 1 to remove or rephrase the false change claim -- the manuscript
>     record is correct and the cover letter overstated.
> Resolve before filling the audit table -- it is faster to fix here where both artifacts
> are simultaneously visible.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7.
  An entry with empty or location-only referent fails Phase 6a. Cannot insert at Phase 7.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.
  SHIFTED: classify and re-examine:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED first, then unflagged.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED take priority):
1. [R-NN] -- too defensive: [rewrite]
2. [R-NN] -- concedes too much: [what to hold]
3. [R-NN] -- too brief: [what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) missing exchange: write it. (b) merged: split.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) placeholder: write it. (b) unresolved: use Phase 2 baseline.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL: (a) move from AUTHOR RESPONDS. (b) revise to introduce valid form.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 Forward-annotation from Check 2c warned that entity-type specificity
  was required at authoring time -- an entry failing Check 2c missed that constraint at its
  earliest visible point.
  Apply the Forward-annotation repair paths:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Apply Forward-annotation path (b) --
      reclassify to CHANGE if no specific instance exists.

**Check 3 -- Cover letter structure**:
CHECK: PASS / FAIL
If FAIL: (a) malformed: add R-ID references. (b) missing: draft from Phase 2 + Phase 5.

**Check 4 -- Forecast validation + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: CHECK: [n FLAGGED] vs [n validated rows] -- PASS / FAIL
Part B: CHECK: [n SHIFTED] vs [n classified + re-examined] -- PASS / FAIL
Part C: CHECK: [n PRESSURE-DRIVEN] vs [n with binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 Forward-annotation from Check 4 Part C warned that PRESSURE-DRIVEN
  entries must commit REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing
  Part C missed that constraint at its earliest visible point. Apply the Phase 2 repair paths:
  (a) Original RULE-1 evidence remains scientifically valid: state REINSTATE with category
      and specific instance. Record in Phase 6a.
  (b) Change improved a non-scientific dimension: state NO REINSTATE with one-sentence
      description of the specific improvement achieved.

**Check 5 -- Frontmatter integer verification**:
CHECK: all four values are integers, manuscript_changes + no_change_responses = concerns_addressed
If FAIL: (a) replace placeholders. (b) recount and correct.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID references -- PASS / FAIL per claim
If FAIL: (a) R-ID omitted: add. (b) no R-ID: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type -- PASS / FAIL
If FAIL:
  Back-reference: Phase 6a forward-annotation warned that Paragraph 1 change claims
  referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME -- an entry failing
  Check 6b missed that constraint at its earliest visible point.
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 -- Complete Enumeration + Canonical Delegation (Axes P+Q)

**Axis**: P+Q -- C-37 complete enumeration + C-38 canonical delegation in Phase 7
**Hypothesis**: Combining complete back-reference enumeration (all upstream sources named per
gate) with canonical repair delegation ("Apply the Forward-annotation repair paths:") closes
two independent gaps in Phase 7. An executor who fails Check 6b sees: the full list of
upstream phases that warned (C-37) AND a delegation to the upstream annotation as the
authoritative repair source rather than standalone instructions (C-38). Phase 2 remains in
bullet-list format and Phase 6a uses non-canonical label (C-39 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; downstream Phase 7 gate constraints are forward-annotated at
the Phase 2 commitment surface with labeled (a)/(b) repair paths. Phase 3.5 audits ambiguous
type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows carry forward
as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1 no-change entries
carries a separately labeled Forward-annotation for each applicable Phase 7 gate check, each
with embedded (a)/(b) repair paths. The amendment pass validates FLAGGED exchanges first,
audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to
REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM
CHANGE -- then checks for unflagged failures; Phase 6a carries an entity-type referent column
and a forward-annotated Check 6b annotation with (a)/(b) repair paths. Phase 7 structural
completion gate runs ten checks; each failing check includes a back-reference enumerating
ALL upstream annotation sources that warned about this constraint, and each repair protocol
delegates to the upstream Forward-annotation by canonical label rather than restating paths.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints with repair paths**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper
>   or author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with study-design basis. Location alone fails.
>   Repair paths if entity is not yet named:
>   (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>       paper location (statistical), named principle + study-design basis (methodological).
>   (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>       defensible -- an unresolved entity at commitment time will fail Check 2c at write time.
>
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision must be recorded in Phase 6a before write. Deferral fails
>   Part C regardless of how clearly the decision is stated in the cover letter.
>   Repair paths if a PRESSURE-DRIVEN shift occurs in Phase 6a:
>   (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with
>       the evidence category and specific instance in Phase 6a.
>   (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>       the scientific claim: state NO REINSTATE with a one-sentence description of the
>       specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data.] We have updated [location]."
  methodological: "We agree that [aspect]. [Justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added analysis / explained constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 P1-NC pre-commitment and Phase 6a pre-commitment table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition with repair paths**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- it is faster to fix here where both artifacts are visible.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7.
  An entry with empty or location-only referent fails Phase 6a. Cannot insert at Phase 7.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.
  SHIFTED: classify and re-examine:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED first, then unflagged.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED take priority):
1. [R-NN] -- too defensive: [rewrite]
2. [R-NN] -- concedes too much: [what to hold]
3. [R-NN] -- too brief: [what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) missing exchange: write it. (b) merged: split.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL: (a) placeholder: write it. (b) unresolved: use Phase 2 baseline.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL: (a) move from AUTHOR RESPONDS. (b) revise to introduce valid form.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 Forward-annotation from Check 2c warned that entity-type specificity
  was required at authoring time, and Phase 6a entity-type referent column required the entity
  to be named during mid-workflow reconciliation -- an entry failing Check 2c missed that
  constraint at its earliest visible points.
  Apply the Forward-annotation repair paths:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Apply Forward-annotation path (b) --
      reclassify to CHANGE if no specific instance exists.

**Check 3 -- Cover letter structure**:
CHECK: PASS / FAIL
If FAIL: (a) malformed: add R-ID references. (b) missing: draft from Phase 2 + Phase 5.

**Check 4 -- Forecast validation + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: CHECK: [n FLAGGED] vs [n validated rows] -- PASS / FAIL
Part B: CHECK: [n SHIFTED] vs [n classified + re-examined] -- PASS / FAIL
Part C: CHECK: [n PRESSURE-DRIVEN] vs [n with binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 forward-annotation warned that PRESSURE-DRIVEN entries must commit
  REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing Part C missed that
  constraint at its earliest visible point. Apply the Phase 2 repair paths:
  (a) Original RULE-1 evidence remains scientifically valid: state REINSTATE with category
      and specific instance. Record in Phase 6a.
  (b) Change improved a non-scientific dimension: state NO REINSTATE with one-sentence
      description of the specific improvement achieved.

**Check 5 -- Frontmatter integer verification**:
CHECK: all four values are integers, manuscript_changes + no_change_responses = concerns_addressed
If FAIL: (a) replace placeholders. (b) recount and correct.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID references -- PASS / FAIL per claim
If FAIL: (a) R-ID omitted: add. (b) no R-ID: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type -- PASS / FAIL
If FAIL:
  Back-reference: Phase 6a forward-annotation warned that Paragraph 1 change claims
  referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME, and Phase 5
  Forward-annotation from Check 6b warned of this constraint at the moment of authoring the
  MANUSCRIPT OUTCOME -- an entry failing Check 6b missed that constraint at its earliest
  visible points.
  Apply the Forward-annotation repair paths:
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 -- Full Integration (Axes P+Q+R)

**Axis**: P+Q+R -- complete enumeration + canonical delegation + self-contained modules
**Hypothesis**: The three axes address three structurally distinct gaps in the constraint
propagation chain. P ensures Phase 7 back-references name EVERY upstream warning source --
including Phase 2 as a new source for Check 2c when Axis R adds the canonical Phase 2 module,
making V-05's Check 2c back-reference enumerate three sources (Phase 2, Phase 5, Phase 6a)
rather than two. Q converts Phase 7 repair blocks from independent instruction sets into named
cross-references delegating to the upstream annotation as authoritative. R restructures Phase 2
and Phase 6a annotations into canonical "Forward-annotation from Check X:" modules, making
each independently resolvable: the author encounters the gate label, the unconditional failure
condition, and the (a)/(b) repair paths as a complete unit at the decision point without
reaching Phase 7. Together: every constraint is visible as a labeled module at the authoring
phase, every module is cross-referenced by label from Phase 7, and Phase 7 delegates rather
than duplicates, creating a unified authority chain across all three enforcement surfaces.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are structured as individually labeled
"Forward-annotation from Check X:" self-contained modules -- each containing the gate label,
an unconditional failure condition, and (a)/(b) repair paths as a complete independently-
resolvable unit. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3
severity assignments. Forecast rows carry forward as flags into exchange headers; Phase 5
MANUSCRIPT OUTCOME template carries the same canonical module format for each applicable
Phase 7 gate check. The amendment pass validates FLAGGED exchanges first, audits P1
pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to REINSTATE /
NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE -- then
checks for unflagged failures; Phase 6a carries an entity-type referent column and a
"Forward-annotation from Check 6b:" module with (a)/(b) repair paths. Phase 7 structural
completion gate runs ten checks; each failing check includes a back-reference enumerating
all upstream annotation sources (Phase 2, Phase 5, Phase 6a where applicable), names each
source by its canonical label, and delegates repair to the upstream Forward-annotation as
the authoritative source rather than restating paths.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default -- the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia -- use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia -- do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error.
Violation: academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:
  REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT OUTCOME
Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them. SHIFTED entries in Phase 6a require
classification; PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation from Check 2c**: A P1 no-change evidence instance must name a
> concrete entity -- cited paper or author (Author Year, not a section of this manuscript),
> specific statistic with paper location, or named methodological principle with study-design
> basis. A location reference alone (App. B, section 3.2, Table 4) fails Check 2c even when
> the evidence category label is correctly named.
> Repair paths:
> (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>     paper location (statistical), named principle + study-design basis (methodological).
> (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>     defensible -- an unresolved entity at commitment time will fail Check 2c at write time.

> **Forward-annotation from Check 4 Part C**: If this pre-commitment is later SHIFTED to
> PRESSURE-DRIVEN in Phase 6a, a binding decision (REINSTATE or NO REINSTATE with a one-
> sentence rationale) must be recorded in Phase 6a before write. Deferring the decision to
> the cover letter fails Part C regardless of how clearly it appears there.
> Repair paths (if PRESSURE-DRIVEN shift occurs in Phase 6a):
> (a) If the original RULE-1 evidence remains scientifically valid: state REINSTATE with the
>     evidence category and specific instance in Phase 6a.
> (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>     the scientific claim: state NO REINSTATE with a one-sentence description of the
>     specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

If none: "All P1 concerns will be addressed with manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide (verify scope/framing/methodological in Phase 3.5):

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" -- factual = paper error; framing = reviewer misread |
| methodological | Existing experiment or analysis design is flawed | "Scope" -- methodological = current work wrong; scope = wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" -- scope = paper doesn't claim this; methodological = tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" -- framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" -- statistical = analysis layer; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback for no scientific content impact |

Severity: P1 (blocks) / P2 (moderate) / P3 (editorial). Sort P1 first, then P2, then P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment:
  R-[NN] typed [type] not [most likely alternative] because:
  [specific distinguishing reason -- not a restatement of the type definition]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment:
  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: "| FLAGGED: [F-0N] [predicted failure mode -- resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data.] We have updated [location]."
  methodological: "We agree that [aspect]. [Justification or fix.] N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact claim]. The reviewer may be reading this as
                  [misread]. We have added [clarifying language] to N."
  statistical:    "[Added analysis / explained constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent (Author Year + locator for
  literature; statistic + paper location for statistical; named principle + study-design
  basis for methodological)]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement.
  > Repair paths:
  > (a) Add the specific traceable instance: Author Year + locator (literature), named
  >     statistic + paper location (statistical), named principle + study-design basis
  >     (methodological).
  > (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
  >     Phase 2 Forward-annotation from Check 2c pre-commitment and Phase 6a table accordingly.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction.
  > Repair paths:
  > (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
  >     incorrectly in this exchange.
  > (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this
  >     R-ID before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation from Check 6b**: A Paragraph 1 change claim asserting "we changed X
> in response to R-NN" while R-NN's Phase 5 MANUSCRIPT OUTCOME is "No change" is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain, and
> Check 6b will block the write.
> Repair paths:
> (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>     it incorrectly -- the claim is accurate, the record is wrong.
> (b) Revise Paragraph 1 to remove or rephrase the false change claim -- the manuscript
>     record is correct and the cover letter overstated.
> Resolve before filling the audit table -- it is faster to fix here where both artifacts
> are simultaneously visible.

- P1 pre-commitment audit with entity-type referent column, SHIFTED classification, and
  decision closure:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column** -- fill during reconciliation, not at Phase 7:
  - Prior literature: the cited paper or author (Author Year) -- not a section of this ms
  - Statistical result: the specific statistic and its paper location
  - Methodological argument: the named inferential principle and its study-design basis
  An entry with an empty or location-only entity-type referent fails Phase 6a. The referent
  must be present here -- it cannot be inserted at Phase 7 Check 2c as a last-second addition.

  HELD: pre-committed no-change maintained; named evidence form and instance used in Phase 5.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical weight without specific new scientific
    evidence. Decision required: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: author encountered specific named evidence not anticipated in Phase 2.
    Decision required: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority):
1. [R-NN] -- too defensive: [rewrite AUTHOR RESPONDS opening]
2. [R-NN] -- concedes too much: [what to hold; why the concession went too far]
3. [R-NN] -- too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write -- fix the failing check and re-run before proceeding.

**Check 1 -- Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Concern in Phase 3 with no exchange written: write the missing exchange in severity
      order before proceeding.
  (b) Two concerns merged into one REVIEWER SAID block: split into separate exchanges,
      each with its own REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME.

**Check 2a -- Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be "[Section N]: [specific change]" or "No change -- [rationale]".
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Change made but MANUSCRIPT OUTCOME is a placeholder: write section + change description.
  (b) Outcome genuinely unresolved: use Phase 2 pre-commitments as baseline and record.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form anywhere: revise to introduce prior literature, methodological argument,
      or statistical result before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator (literature); named statistic + location (statistical); named principle
+ study-design basis (methodological).
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 2 Forward-annotation from Check 2c warned that entity-type specificity
  was required at the pre-commitment decision point, Phase 5 Forward-annotation from Check 2c
  warned of the same constraint at authoring time, and Phase 6a entity-type referent column
  required the entity to be named during mid-workflow reconciliation -- an entry failing Check
  2c missed that constraint at its earliest visible points.
  Apply the Forward-annotation repair paths:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Apply Forward-annotation path (b) --
      reclassify to CHANGE if no specific instance exists.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed: add parenthetical R-ID references to each change claim.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation for each.
  (b) Count mismatch: identify unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but note absent: write the re-examination note.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 Forward-annotation from Check 4 Part C warned that PRESSURE-DRIVEN
  entries must commit REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing
  Part C missed that constraint at its earliest visible point. Apply the Phase 2 repair paths:
  (a) Original RULE-1 evidence remains scientifically valid: state REINSTATE with the evidence
      category and specific instance. Record in Phase 6a before proceeding.
  (b) Change improved a non-scientific dimension: state NO REINSTATE with a one-sentence
      description of the specific improvement achieved.

**Check 5 -- Frontmatter integer verification**:
Compute from Phase 5 outcomes:
- reviewer_count: distinct reviewers in Phase 3
- concerns_addressed: total R-IDs in Phase 3
- manuscript_changes: R-IDs with CHANGE MANUSCRIPT OUTCOME
- no_change_responses: R-IDs with no-change MANUSCRIPT OUTCOME
CHECK: all four are integers, manuscript_changes + no_change_responses = concerns_addressed
-- PASS / FAIL
If FAIL:
  (a) String placeholders: replace each with the computed integer.
  (b) Inconsistent totals: recount from Phase 5 and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (updated in 6a) must include at least one parenthetical
R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted: add parenthetical reference.
  (b) No R-ID maps to the claim: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME (not "No change").
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  Back-reference: Phase 6a Forward-annotation from Check 6b warned that Paragraph 1 change
  claims referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME, and Phase 5
  Forward-annotation from Check 6b warned of this constraint at the moment of authoring the
  MANUSCRIPT OUTCOME -- an entry failing Check 6b missed that constraint at its earliest
  visible points. Apply the Forward-annotation repair paths:
  (a) Change was actually made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly:
      correct the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```
