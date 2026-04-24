Written to `simulations/quest/variations/rhythm-rebuttal-variations-R10-2026-03-19.md`.

---

**R10 Variations Summary**

| Variation | Axis | C-34 | C-35 | C-36 | Predicted |
|-----------|------|------|------|------|-----------|
| V-01 | M only | Phase 7 repair blocks name upstream annotation | -- | -- | 26/28 |
| V-02 | N only | -- | Upstream annotations carry (a)/(b) repair paths | -- | 26/28 |
| V-03 | O only | -- | -- | Phase 5 has separately labeled Forward-annotation per gate | 26/28 |
| V-04 | M+N | Back-references in Phase 7 | (a)/(b) in upstream annotations | -- | 27/28 |
| V-05 | M+N+O | Back-references in Phase 7 | (a)/(b) in upstream annotations | Separate labeled per gate + (a)/(b) | 28/28 |

**The three axis distinctions:**
- **M**: Closes the Phase 7 accountability loop — the "If FAIL" repair block names the specific upstream annotation the author missed, converting gate detection into a learning signal
- **N**: Makes upstream annotations self-contained — adds (a)/(b) repair paths to Phase 2 and Phase 5 annotations so resolution is possible at the decision point without waiting for Phase 7
- **O**: Prevents partial annotation gaps — replaces combined "Check 2c and Check 6b warning:" block with two independently labeled `Forward-annotation from Check X:` blocks in the Phase 5 template slot, making each gate's failure class structurally independent
uote so
  the author can resolve the failure at the decision point without waiting for Phase 7
- O prevents partial annotation gaps per artifact -- C-33 required forward-annotations per phase;
  C-36 requires ALL applicable Phase 7 gates to be separately labeled in the same upstream
  artifact template slot, catching the case where Check 2c is annotated in Phase 5 but Check 6b
  is not (or vice versa)

---

## Axis Rationales

**Axis M -- back-reference accountability gap**: C-33 (R9) requires upstream forward-annotations
to exist. When a Phase 7 check fails, the executor receives a repair instruction. But the repair
instruction does not point back to the upstream annotation that warned about this constraint.
An executor who failed Check 2c cannot tell whether they read and ignored the Phase 5
forward-annotation, or whether the annotation was absent. C-34 closes this loop: each Phase 7
"If FAIL:" repair block includes a back-reference sentence naming the upstream phase and the
specific annotation that warned about this constraint class. The sentence follows the canonical
form: "Phase X forward-annotation warned that [specific constraint] -- an entry failing this
check missed that constraint at its earliest visible point." An executor who reads the
back-reference can compare the Phase 7 failure to the upstream annotation they saw (or missed)
during authoring, converting detection into a learning signal.

**Axis N -- repair-path propagation gap**: C-32 (R9) embeds (a)/(b) repair paths in Phase 7
gate checks. C-33 (R9) surfaces failure conditions in upstream phases. Together: the failure
is detectable at authoring time (C-33) AND the repair structure exists at gate time (C-32).
But the repair structure appears only in Phase 7 -- after the draft is complete. An executor
reading the Phase 5 forward-annotation "Check 2c: entity-type referent required" has the
failure condition but not the repair options. If they want to know what to do, they must
consult Phase 7. C-35 propagates the (a)/(b) repair paths into the upstream annotation
blockquote itself. The annotation becomes self-contained: the author sees both what will fail
and what the repair options are at the moment of authoring. Resolution is possible at the
decision point without reaching Phase 7.

**Axis O -- multi-gate annotation coverage gap**: C-33 (R9) requires forward-annotations per
phase. A Phase 5 MANUSCRIPT OUTCOME entry is checked by multiple Phase 7 gates -- both Check
2c (entity-type specificity) and Check 6b (cover-letter/outcome consistency) apply to the same
MANUSCRIPT OUTCOME entry. A combined "Check 2c and Check 6b warning:" block mentions both
constraints but presents them as a single annotation. An executor who skims the block may treat
it as one gate, not two independent failure classes with independent repair actions. C-36 requires
each applicable gate to have its own separately labeled "Forward-annotation from Check X:" block
in the same template slot. Two independently labeled annotations make the structural independence
visible: each gate can independently block the write, each has its own failure condition, and
each will require its own repair.

---

## V-01 -- Phase 7 Gate Back-References (Axis M)

**Axis**: M only -- C-34 back-reference accountability in Phase 7 repair blocks
**Hypothesis**: Adding an explicit back-reference sentence within each Phase 7 "If FAIL:" block
-- naming the upstream phase and annotation that warned about the constraint -- closes the
accountability loop. An executor who fails Check 2c, Check 4 Part C, or Check 6b sees exactly
which upstream annotation they encountered (or missed) during authoring. This adds no new
authoring-time information; it adds repair-time learning signal only. Phase 5 uses combined
annotation format (C-36 absent). Upstream annotations have no (a)/(b) repair paths (C-35 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance; downstream
Phase 7 gate constraints are forward-annotated at the Phase 2 commitment surface. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows
carry forward as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1
no-change entries carries forward-annotated failure conditions from Check 2c and Check 6b.
The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED
classification -- PRESSURE-DRIVEN entries close to REINSTATE / NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE -- then checks for unflagged failures;
Phase 6a carries an entity-type referent column and a forward-annotated Check 6b failure
condition. Phase 7 structural completion gate runs ten checks; each failing check whose
constraint class was forward-annotated upstream includes an explicit back-reference naming
the upstream phase and annotation that warned about the failure.

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
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces instance specificity.
A P1 no-change rationale naming a valid category but no traceable instance fails Check 2c --
the category label alone does not satisfy RULE-1 at editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless
of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response concedes that the scope challenge has merit
and invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: combative or dismissive phrasing is a professional failure that may cause
rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange produces a single REVIEWER SAID block quoting multiple
distinct concerns -- the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change -- rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to REINSTATE or NO
REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints visible now**:
> - Check 2c (entity-type): the evidence instance you name must be a concrete entity -- a
>   cited paper or author (Author Year, not a section of this manuscript), a specific
>   statistic with its paper location, or a named methodological principle with its
>   study-design basis. A location reference alone ("App. B", "3.2", "Table 4") fails Check
>   2c even when the category label is correctly named.
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision (REINSTATE or NO REINSTATE with a one-sentence rationale)
>   must be recorded in Phase 6a before write. The decision cannot be deferred to the cover
>   letter -- deferral fails Part C regardless of how clearly it is stated there.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1)
  showed adequacy before data collection began.
  Entity: App. B Table B1 power analysis result (N=120, power=0.80) -- NOT "App. B alone".

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (2.1,
  single observation per participant) makes that framework inapplicable by structural assumption.
  Entity: Chen 2018 panel-data independence assumption (named principle) -- NOT "2.1 alone".

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

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

Before writing any exchange, produce a structured failure forecast. Specific predictions
only -- generic statements do not count. These rows carry forward as flags into Phase 5 headers.

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
  "No change -- [evidence category: named entity-type referent (Author Year N for literature;
  statistic + paper location for statistical; named principle + study-design basis for
  methodological)]"
  Check 2c and Check 6b warning: naming only a location (N, App. C) without a named entity
  fails Check 2c. If Paragraph 1 currently claims a change citing this R-ID, that claim will
  fail Check 6b -- update Paragraph 1 or reconsider the no-change decision before continuing.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction -- the cover letter asserts a change the manuscript does not contain.
> Resolve it now, during Phase 6a reconciliation:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- Check 6b will catch it in Phase 7, but it is faster to fix
> here where both Paragraph 1 and Phase 5 outcomes are visible simultaneously.

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

  SHIFTED: classify and re-examine:
    PRESSURE-DRIVEN: author yielded under rhetorical weight without specific new scientific
    evidence. Decision required: REINSTATE or NO REINSTATE with one-sentence rationale.
    EVIDENCE-DRIVEN: author encountered specific named evidence in Phase 5.
    Decision required: CONFIRM CHANGE: [specific evidence]. Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

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
  (b) Outcome genuinely unresolved: use Phase 2 pre-commitments as baseline and record
      a no-change rationale or commit to a change before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category.
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move the category
      name into the MANUSCRIPT OUTCOME rationale before proceeding.
  (b) No valid form anywhere in the exchange: revise to introduce prior literature,
      methodological argument, or statistical result before proceeding.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify a specific traceable instance:
Author Year + locator (literature); named statistic + location (statistical); named principle
+ study-design basis (methodological).
"Prior literature supports our approach" -- fails (category present, no instance).
"Prior literature (Jones 2019, 3.2) validates this approach in equivalent populations"
-- passes (category + entity + locator).
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 MANUSCRIPT OUTCOME annotation warned that entity-type specificity
  was required at authoring time, and Phase 6a entity-type referent column required the entity
  to be named during mid-workflow reconciliation -- an entry failing Check 2c missed that
  constraint at its earliest visible points.
  (a) Specific entity exists in exchange body but absent from MANUSCRIPT OUTCOME: move the
      named entity into the MANUSCRIPT OUTCOME rationale. Update Phase 6a entity-type referent
      column to reflect the correction.
  (b) No concrete entity named anywhere: revise the exchange to name a specific entity.
      A location reference alone without a named entity does not satisfy this check.

**Check 3 -- Cover letter structure**:
Phase 2 (updated in 6a) contains Paragraph 1 (3-4 changes with R-ID references) and
Paragraph 2 (disagreement framing or explicit statement of none).
CHECK: PASS / FAIL
If FAIL:
  (a) Paragraph present but malformed (changes lack R-ID references): add parenthetical
      R-ID references to each change claim before proceeding.
  (b) Paragraph missing entirely: draft from Phase 2 pre-commitments and Phase 5 outcomes.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b FLAGGED validation for each.
  (b) Validation entries written but count mismatches: identify unvalidated row and add it.

Part B: Every SHIFTED entry must have classification and completed re-examination note.
CHECK: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED entries with no classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but re-examination note absent: write the note for each classified entry.

Part C: Every PRESSURE-DRIVEN entry must have REINSTATE or NO REINSTATE with rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 forward-annotation warned that PRESSURE-DRIVEN entries must commit
  REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing Part C missed that
  constraint at its earliest visible point.
  (a) PRESSURE-DRIVEN with re-examination note but no binary decision: state REINSTATE or
      NO REINSTATE with a one-sentence rationale naming what holds or was conceded.
  (b) EVIDENCE-DRIVEN without CONFIRM CHANGE: name the specific evidence and record CONFIRM
      CHANGE with a one-sentence evidence statement before proceeding.

**Check 5 -- Frontmatter integer verification**:
Compute from Phase 5 outcomes:
- reviewer_count: distinct reviewers in Phase 3
- concerns_addressed: total R-IDs in Phase 3
- manuscript_changes: R-IDs with CHANGE MANUSCRIPT OUTCOME
- no_change_responses: R-IDs with no-change MANUSCRIPT OUTCOME
CHECK: all four are integers, manuscript_changes + no_change_responses = concerns_addressed
-- PASS / FAIL
If FAIL:
  (a) String placeholders in frontmatter: replace each with the computed integer.
  (b) Inconsistent totals: recount from Phase 5 outcomes and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (updated in 6a) must include at least one parenthetical
R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but was omitted from parenthetical: add it before proceeding.
  (b) No R-ID maps to the claim: remove or rephrase to reflect a reviewer-driven change.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME (not "No change"). A claim asserting "we changed X in response
to R-NN" while R-NN records no-change is a structural contradiction.
CHECK: list each Paragraph 1 claim, R-ID references, and each R-ID MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
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
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 -- Upstream Annotations with (a)/(b) Repair Paths (Axis N)

**Axis**: N only -- C-35 (a)/(b) repair paths embedded in Phase 2 and Phase 5 upstream annotations
**Hypothesis**: An upstream annotation that states the failure condition but not the repair options
is a warning, not a resolution surface. Adding labeled (a)/(b) repair paths to each upstream
annotation makes the annotation self-contained: the author sees what will fail AND what to do
about it at the authoring decision point. Phase 6a already carries (a)/(b) in the Check 6b
annotation; this variation adds (a)/(b) to Phase 2 and Phase 5 annotations as well.
Phase 5 still uses combined annotation format (C-36 absent). Phase 7 has no back-references
(C-34 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; each forward-annotated gate constraint at the Phase 2
commitment surface carries labeled (a)/(b) repair paths within the annotation blockquote
so the author can resolve failures at commitment time without waiting for Phase 7. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows
carry forward as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1
no-change entries carries failure conditions from Check 2c and Check 6b, each with embedded
(a)/(b) repair paths. The amendment pass validates FLAGGED exchanges first, audits P1
pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN entries close to REINSTATE /
NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE -- then
checks for unflagged failures; Phase 6a carries an entity-type referent column and a
forward-annotated Check 6b annotation with (a)/(b) repair paths. Phase 7 structural completion
gate verifies all constraints before write.

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
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces instance specificity.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office will return it for revision.

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
decomposing or responding to any concern.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints with repair paths**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper
>   or author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with its study-design basis. A location
>   reference alone fails Check 2c.
>   Repair paths if entity is not yet named at Phase 2:
>   (a) Name the concrete entity now: Author Year + section or table locator (literature),
>       named statistic + paper location (statistical), named principle + study-design basis
>       (methodological).
>   (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>       defensible -- an unresolved entity at commitment time will fail Check 2c at write time.
>
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision must be recorded in Phase 6a before write. Deferral fails
>   Part C regardless of how clearly the decision is stated in the cover letter.
>   Repair paths if a PRESSURE-DRIVEN shift occurs in Phase 6a:
>   (a) If the original RULE-1 evidence remains scientifically valid after Phase 5 exchange:
>       state REINSTATE with the evidence category and specific instance in Phase 6a.
>   (b) If the change improved clarity, presentation, or reduced ambiguity without affecting
>       the scientific claim: state NO REINSTATE with a one-sentence description of the
>       specific non-scientific improvement achieved.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1).

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (2.1)
  makes that framework inapplicable by structural assumption.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type: factual / methodological / scope / framing / statistical / presentation
(verify scope/framing/methodological in Phase 3.5)
Severity: P1 / P2 / P3. Sort P1, P2, P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological:
  R-[NN] typed [type] not [alternative] because: [specific distinguishing reason]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3:
  R-[NN] assigned [P2/P3] not P1 because: [specific paper-based or venue-based reason]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [mechanism] |
| F-02 | [R-NN] | concedes too much | [pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

--- P1 CONCERNS (RULE-1) --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[FLAGGED: [F-0N] if applicable]

**REVIEWER SAID:** > "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  [type-specific template]

**MANUSCRIPT OUTCOME:**
[Section + change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent]"

  Check 2c repair paths if entity-type referent is missing or is a location-only reference:
  (a) Add the specific traceable instance: Author Year + section locator (literature), named
      statistic + paper location (statistical), named principle + study-design basis
      (methodological).
  (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
      Phase 2 P1-NC pre-commitment and Phase 6a pre-commitment table accordingly.

  Check 6b repair paths if Paragraph 1 currently claims a change citing this R-ID:
  (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was actually made but recorded
      incorrectly in this exchange.
  (b) Revise Paragraph 1 to remove or rephrase the claim asserting a change against this R-ID
      before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition with repair paths**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction. Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and Phase 5 recorded
>       it incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.
> Do not carry this forward -- it is faster to fix here where both artifacts are visible.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column**: Prior literature: Author Year. Statistical: statistic +
  paper location. Methodological: named principle + study-design basis.
  Location-only entry fails Phase 6a. Referent must be present here, not inserted at Phase 7.

  HELD: no-change maintained; evidence form and instance in Phase 5.
  SHIFTED -- classify:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE + one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE + evidence sentence. Update Paragraph 2 if needed.

**6b. Forecast validation**: FLAGGED first, then unflagged.
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing. Any FAIL stops the write.

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Missing exchange: write it before proceeding.
  (b) Merged concerns: split into separate exchanges before proceeding.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Placeholder outcome: write section + change before proceeding.
  (b) Unresolved outcome: use Phase 2 baseline and record before proceeding.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form: revise to introduce one.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it and update
      the Phase 6a entity-type referent column to reflect the correction.
  (b) No concrete entity named: revise to name one. Phase 5 annotation carried repair paths
      (a)/(b) for this constraint -- apply them before proceeding.

**Check 3 -- Cover letter structure**:
CHECK: Paragraph 1 (changes with R-IDs) and Paragraph 2 (disagreement or none) -- PASS / FAIL
If FAIL:
  (a) Malformed paragraph: add R-ID references.
  (b) Missing paragraph: draft from Phase 2 and Phase 5.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: [n FLAGGED headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails:
  (a) Forecast rows without validation: complete Phase 6b validation.
  (b) Count mismatch: identify unvalidated row and add it.

Part B: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails:
  (a) SHIFTED without classification: apply PRESSURE-DRIVEN or EVIDENCE-DRIVEN.
  (b) Classified but no re-examination note: write the note.

Part C: [n PRESSURE-DRIVEN] vs [n with REINSTATE or NO REINSTATE + rationale] -- PASS / FAIL
If Part C fails:
  (a) PRESSURE-DRIVEN with re-examination but no binary decision: state REINSTATE or NO
      REINSTATE + rationale. Phase 2 annotation carried repair paths (a)/(b) for this case.
  (b) EVIDENCE-DRIVEN without CONFIRM CHANGE: name evidence and record CONFIRM CHANGE.

**Check 5 -- Frontmatter integer verification**:
CHECK: reviewer_count, concerns_addressed, manuscript_changes, no_change_responses -- PASS / FAIL
If FAIL:
  (a) String placeholders: replace with computed integers.
  (b) Inconsistent totals: recount from Phase 5 and correct all four values.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but omitted: add parenthetical reference.
  (b) No R-ID maps to claim: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  (a) Change was made but Phase 5 records no change incorrectly: correct MANUSCRIPT OUTCOME.
  (b) Change was not made: revise Paragraph 1. Phase 6a annotation and Phase 5 Check 6b
      repair paths both apply -- use the applicable path before proceeding.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 -- Multi-Gate Annotation Coverage Per Artifact (Axis O)

**Axis**: O only -- C-36 separately labeled Forward-annotation per Phase 7 gate in Phase 5 template
**Hypothesis**: A combined "Check 2c and Check 6b warning:" block presents two independent failure
classes as one annotation. An executor who skims the combined block may treat it as one gate.
Separating each gate into its own labeled "Forward-annotation from Check X:" block makes the
independence structural: two independent labeled annotations, each capable of independent failure,
each demanding its own resolution. Phase 2 annotations have no (a)/(b) repair paths (C-35 absent).
Phase 7 has no back-references (C-34 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition, naming evidence by category AND specific instance; downstream
Phase 7 gate constraints are forward-annotated at the Phase 2 commitment surface. Phase 3.5
audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity assignments. Forecast rows
carry forward as flags into exchange headers; Phase 5 MANUSCRIPT OUTCOME template for P1
no-change entries carries a separately labeled Forward-annotation for each applicable Phase 7
gate check -- Check 2c and Check 6b each have their own labeled block in the same template
slot so neither failure class is invisible during authoring. The amendment pass validates
FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED classification -- PRESSURE-
DRIVEN entries close to REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN
entries record CONFIRM CHANGE -- then checks for unflagged failures; Phase 6a carries an
entity-type referent column and a forward-annotated Check 6b failure condition. Phase 7
structural completion gate verifies all constraints before write.

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
  - Appeal to authority or precedent

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office returns it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop. Violation: academic misconduct.

**RULE-8 (Exchange format rule)**: REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT
OUTCOME in every exchange. Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure can erode them.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints visible now**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper
>   or author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with study-design basis. Location alone fails.
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision (REINSTATE or NO REINSTATE with a one-sentence rationale)
>   must be recorded in Phase 6a before write. Deferral to the cover letter fails Part C.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1).

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (2.1)
  makes that framework inapplicable by structural assumption.

If none: "All P1 concerns will be addressed with manuscript changes."

---

## PHASE 3 -- CONCERN DECOMPOSITION

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type: factual / methodological / scope / framing / statistical / presentation
Severity: P1 / P2 / P3. Sort P1, P2, P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological:
  R-[NN] typed [type] not [alternative] because: [specific distinguishing reason]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3:
  R-[NN] assigned [P2/P3] not P1 because: [specific paper-based or venue-based reason]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [mechanism] |
| F-02 | [R-NN] | concedes too much | [pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

--- P1 CONCERNS --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[FLAGGED: [F-0N] if applicable]

**REVIEWER SAID:** > "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  [type-specific template]

**MANUSCRIPT OUTCOME:**
[Section + specific change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent (Author Year + locator for
  literature; statistic + paper location for statistical; named principle + study-design
  basis for methodological)]"

  > **Forward-annotation from Check 2c**: A P1 no-change rationale naming a valid evidence
  > category without a specific traceable instance fails Check 2c -- naming a location alone
  > (section N, App. C) without the cited paper or author, specific statistic, or named
  > principle does not satisfy the entity-type referent requirement. Resolve before
  > continuing past this exchange.

  > **Forward-annotation from Check 6b**: If Paragraph 1 currently claims a change citing
  > this R-ID, that claim will fail Check 6b -- a cover letter asserting "we changed X in
  > response to R-NN" paired with a No-change MANUSCRIPT OUTCOME is a structural contradiction
  > that Check 6b will detect and block. Resolve: update Paragraph 1 or reconsider the
  > no-change decision before continuing past this exchange.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition**:
> Before filling the audit table, scan Paragraph 1 for any change claim that references an
> R-ID whose Phase 5 MANUSCRIPT OUTCOME is "No change." Each such claim is a structural
> contradiction. Resolve it now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was actually made and recorded incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  **Entity-type referent column**: fill during reconciliation, not at Phase 7.
  Prior literature: Author Year. Statistical: statistic + paper location.
  Methodological: named principle + study-design basis. Location-only entry fails Phase 6a.

  HELD: no-change maintained; evidence form and instance in Phase 5.
  SHIFTED -- classify:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE + rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE + evidence sentence. Update Paragraph 2 if needed.

**6b. Forecast validation**: FLAGGED first, then unflagged.
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing. Any FAIL stops the write.

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Missing exchange: write it.
  (b) Merged concerns: split into separate exchanges.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Placeholder: write section + change.
  (b) Unresolved: use Phase 2 baseline and record.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form: revise to introduce one.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it. Update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. The Phase 5 Forward-annotation from
      Check 2c warned of this requirement at authoring time.

**Check 3 -- Cover letter structure**:
CHECK: Paragraph 1 (changes with R-IDs) and Paragraph 2 (disagreement or none) -- PASS / FAIL
If FAIL:
  (a) Malformed: add R-ID references.
  (b) Missing: draft from Phase 2 and Phase 5.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: [n FLAGGED headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails: (a) complete validation. (b) identify unvalidated row.

Part B: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails: (a) classify. (b) write re-examination note.

Part C: [n PRESSURE-DRIVEN] vs [n with REINSTATE or NO REINSTATE + rationale] -- PASS / FAIL
If Part C fails:
  (a) No binary decision: state REINSTATE or NO REINSTATE with one-sentence rationale.
  (b) EVIDENCE-DRIVEN without CONFIRM CHANGE: name evidence and record it.

**Check 5 -- Frontmatter integer verification**:
CHECK: reviewer_count, concerns_addressed, manuscript_changes, no_change_responses -- PASS / FAIL
If FAIL:
  (a) String placeholders: replace with integers.
  (b) Inconsistent totals: recount and correct.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but omitted: add parenthetical.
  (b) No R-ID maps: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each referenced R-ID resolves
to a CHANGE MANUSCRIPT OUTCOME.
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  (a) Change was made but Phase 5 records no change incorrectly: correct MANUSCRIPT OUTCOME.
  (b) Change was not made: revise Paragraph 1. The Phase 5 Forward-annotation from Check 6b
      warned of this constraint at the moment of authoring the MANUSCRIPT OUTCOME.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 -- Back-References + Upstream Repair Paths (Axes M+N)

**Axis**: M+N combined -- C-34 Phase 7 back-references + C-35 upstream (a)/(b) repair paths
**Hypothesis**: M and N address the same failure window from opposite ends. M closes the
accountability loop at Phase 7 (executor learns which upstream annotation they missed). N closes
the repair gap at authoring time (executor resolves the failure at the decision point using
embedded repair paths). Together they create a complete cycle: upstream annotation carries repair
options at authoring time; Phase 7 back-reference names the annotation at gate time. Phase 5 still
uses combined annotation format (C-36 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; each forward-annotated gate constraint at the Phase 2
commitment surface carries labeled (a)/(b) repair paths so the author can resolve failures
at commitment time. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3
severity assignments. Forecast rows carry forward as flags into exchange headers; Phase 5
MANUSCRIPT OUTCOME template for P1 no-change entries carries failure conditions from Check 2c
and Check 6b, each with embedded (a)/(b) repair paths. The amendment pass validates FLAGGED
exchanges first, audits P1 pre-commitments with SHIFTED classification -- PRESSURE-DRIVEN
entries close to REINSTATE / NO REINSTATE with a named rationale; EVIDENCE-DRIVEN entries
record CONFIRM CHANGE -- then checks for unflagged failures; Phase 6a carries an entity-type
referent column and a forward-annotated Check 6b annotation with (a)/(b) repair paths. Phase 7
structural completion gate runs ten checks; each failing check whose constraint class was
forward-annotated upstream includes an explicit back-reference naming the upstream annotation
that warned about the failure, completing the accountability loop at gate time.

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
  - Appeal to authority or precedent

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Check 2b enforces category presence; Check 2c enforces instance specificity.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: 2-3 sentences max. Violation: invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: may cause rejection.

**RULE-5 (Decomposition rule)**: One concern = one exchange.
Violation: editorial office returns it.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: fail validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop. Violation: academic misconduct.

**RULE-8 (Exchange format rule)**: REVIEWER SAID / AUTHOR RESPONDS [stance] / MANUSCRIPT
OUTCOME in every exchange. Violation: structurally incomplete -- rewrite.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: review artifact or reviewer comments. Read: original paper if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern.

**Paragraph 1**: Name 3-4 changes this revision will make.
**Paragraph 2**: Name areas of respectful disagreement. If none: state explicitly.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):

> **Forward-annotation -- downstream Phase 7 gate constraints with repair paths**:
> - Check 2c (entity-type): the evidence instance must be a concrete entity -- cited paper or
>   author (Author Year, not a section of this manuscript), specific statistic with paper
>   location, or named methodological principle with study-design basis. Location alone fails.
>   Repair paths if entity is not yet named:
>   (a) Name the concrete entity now: Author Year + locator (literature), named statistic +
>       paper location (statistical), named principle + study-design basis (methodological).
>   (b) If no concrete entity can be named at Phase 2, reconsider whether this P1-NC is
>       defensible -- an unresolved entity will fail Check 2c at write time.
>
> - Check 4 Part C (anti-deferral): if this pre-commitment is later SHIFTED to PRESSURE-DRIVEN
>   in Phase 6a, a binary decision must be recorded in Phase 6a before write. Deferral fails
>   Part C.
>   Repair paths if a PRESSURE-DRIVEN shift occurs in Phase 6a:
>   (a) If the original RULE-1 evidence remains scientifically valid after Phase 5 exchange:
>       state REINSTATE with the evidence category and specific instance in Phase 6a.
>   (b) If the change improved clarity or presentation without affecting the scientific claim:
>       state NO REINSTATE with a one-sentence description of the specific improvement.

For each P1 concern anticipated to result in no-change:

  P1-NC: [anticipated concern summary] -- anticipated no-change because:
  [evidence category: specific traceable instance -- one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1).

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (2.1)
  makes that framework inapplicable by structural assumption.

If none: "All P1 concerns will be addressed with manuscript changes."

---

## PHASE 3 -- CONCERN DECOMPOSITION

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type: factual / methodological / scope / framing / statistical / presentation
Severity: P1 / P2 / P3. Sort P1, P2, P3.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological:
  R-[NN] typed [type] not [alternative] because: [specific distinguishing reason]

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3:
  R-[NN] assigned [P2/P3] not P1 because: [specific paper-based or venue-based reason]

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [mechanism] |
| F-02 | [R-NN] | concedes too much | [pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

--- P1 CONCERNS (RULE-1) --- P2 CONCERNS --- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [summary]**
[FLAGGED: [F-0N] if applicable]

**REVIEWER SAID:** > "[exact quote]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  [type-specific template]

**MANUSCRIPT OUTCOME:**
[Section + change.]
[Or for P1 no-change:
  "No change -- [evidence category: named entity-type referent]"

  Check 2c repair paths if entity-type referent is missing or location-only:
  (a) Add the specific traceable instance: Author Year + locator (literature), named statistic
      + paper location (statistical), named principle + study-design basis (methodological).
  (b) If no specific instance exists, reclassify MANUSCRIPT OUTCOME to CHANGE and update
      Phase 2 P1-NC and Phase 6a pre-commitment table accordingly.

  Check 6b repair paths if Paragraph 1 claims a change for this R-ID:
  (a) Correct this MANUSCRIPT OUTCOME to CHANGE if the change was made but recorded incorrectly.
  (b) Revise Paragraph 1 to remove or rephrase the false change claim.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with parenthetical R-ID references for each named change.
- Update Paragraph 2 for any shift in disagreement framing.

> **Forward-annotation -- Check 6b failure condition with repair paths**:
> Scan Paragraph 1 for any change claim referencing an R-ID whose Phase 5 MANUSCRIPT OUTCOME
> is "No change." Resolve now:
>   (a) Correct the MANUSCRIPT OUTCOME if the change was made and Phase 5 recorded incorrectly.
>   (b) Revise Paragraph 1 to remove or rephrase the false change claim.

- P1 pre-commitment audit:

  | P1-NC | Evidence category | Entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|-------------------|----------------------|-----------------|----------------|----------------|----------|-----------|

  Entity-type referent: Author Year (literature); statistic + location (statistical); named
  principle + study-design basis (methodological). Location-only entry fails Phase 6a.

  HELD: no-change maintained; evidence form and instance in Phase 5.
  SHIFTED -- classify:
    PRESSURE-DRIVEN: REINSTATE or NO REINSTATE + one-sentence rationale.
    EVIDENCE-DRIVEN: CONFIRM CHANGE + evidence sentence. Update Paragraph 2 if needed.

**6b. Forecast validation**: FLAGGED first, then unflagged.
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] -- too defensive
2. [R-NN] -- concedes too much
3. [R-NN] -- too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing. Any FAIL stops the write.

**Check 1 -- Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] -- PASS / FAIL
If FAIL:
  (a) Missing exchange: write it.
  (b) Merged concerns: split.

**Check 2a -- Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] -- PASS / FAIL
If FAIL:
  (a) Placeholder: write section + change.
  (b) Unresolved: use Phase 2 baseline.

**Check 2b -- P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category -- PASS / FAIL per entry
If FAIL:
  (a) Valid form in AUTHOR RESPONDS but absent from MANUSCRIPT OUTCOME: move it.
  (b) No valid form: revise to introduce one.

**Check 2c -- P1 no-change evidence specificity (traceable instance present)**:
CHECK: list each P1 no-change R-ID, its evidence category, and named traceable instance
-- PASS / FAIL per entry
If FAIL:
  Back-reference: Phase 5 MANUSCRIPT OUTCOME annotation warned that entity-type specificity
  was required at authoring time, and Phase 6a entity-type referent column required the entity
  to be present during reconciliation -- an entry failing Check 2c missed that constraint at
  its earliest visible points. Phase 5 repair paths (a)/(b) apply:
  (a) Specific entity in exchange body but absent from MANUSCRIPT OUTCOME: move it. Update
      Phase 6a entity-type referent column.
  (b) No concrete entity named: revise to name one. Reclassify to CHANGE if no instance exists.

**Check 3 -- Cover letter structure**:
CHECK: Paragraph 1 (changes with R-IDs) and Paragraph 2 (disagreement or none) -- PASS / FAIL
If FAIL:
  (a) Malformed: add R-ID references.
  (b) Missing: draft from Phase 2 and Phase 5.

**Check 4 -- Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: [n FLAGGED headers] vs [n validated rows in Phase 6b] -- PASS / FAIL
If Part A fails: (a) complete validation. (b) identify unvalidated row.

Part B: [n SHIFTED entries] vs [n classified + re-examined] -- PASS / FAIL
If Part B fails: (a) classify. (b) write re-examination note.

Part C: [n PRESSURE-DRIVEN] vs [n with REINSTATE or NO REINSTATE + rationale] -- PASS / FAIL
If Part C fails:
  Back-reference: Phase 2 forward-annotation warned that PRESSURE-DRIVEN entries must commit
  REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing Part C missed that
  constraint at its earliest visible point. Phase 2 repair paths (a)/(b) apply:
  (a) Original RULE-1 evidence remains valid: state REINSTATE + evidence sentence in Phase 6a.
  (b) Change improved non-scientific dimension: state NO REINSTATE + improvement description.

**Check 5 -- Frontmatter integer verification**:
CHECK: reviewer_count, concerns_addressed, manuscript_changes, no_change_responses -- PASS / FAIL
If FAIL:
  (a) String placeholders: replace with integers.
  (b) Inconsistent totals: recount and correct.

**Check 6 -- Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) -- PASS / FAIL per claim
If FAIL:
  (a) R-ID exists but omitted: add parenthetical.
  (b) No R-ID maps: remove or rephrase.

**Check 6b -- Cover letter claim-outcome consistency**:
CHECK: list each Paragraph 1 claim, R-ID references, and MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) -- PASS / FAIL per claim
If FAIL:
  Back-reference: Phase 6a forward-annotation warned that Paragraph 1 change claims
  referencing an R-ID must resolve to a CHANGE MANUSCRIPT OUTCOME -- an entry failing
  Check 6b missed that constraint at its earliest visible point. Phase 6a repair paths
  (a)/(b) and Phase 5 Check 6b repair paths both apply:
  (a) Change was made but Phase 5 records no change incorrectly: correct MANUSCRIPT OUTCOME.
  (b) Change was not made: revise Paragraph 1 to remove the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 -- Full Integration (Axes M+N+O)

**Axis**: M+N+O -- back-references in Phase 7 + (a)/(b) in upstream annotations + separate labeled
Forward-annotation per gate in Phase 5
**Hypothesis**: The three axes address three structurally distinct gaps in the accountability and
repair chain. M closes the Phase 7 accountability loop: the executor knows which upstream
annotation they missed. N makes each upstream annotation self-contained: the executor can resolve
the failure at the decision point with embedded repair paths. O prevents partial annotation gaps:
every applicable Phase 7 gate has its own labeled Forward-annotation in Phase 5 with independent
failure condition and repair paths. Together they create full constraint visibility from authoring
through gate time, with repair options at every enforcement surface.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition; each forward-annotated gate constraint at the Phase 2
commitment surface carries labeled (a)/(b) repair paths so the author can resolve failures
at commitment time. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3
severity assignments. Forecast rows carry forward as flags into exchange headers; Phase 5
MANUSCRIPT OUTCOME template for P1 no-change entries carries a separately labeled
Forward-annotation for EACH applicable Phase 7 gate check -- Check 2c and Check 6b each have
their own labeled block in the same template slot, each with embedded (a)/(b) repair paths.
The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED
classification -- PRESSURE-DRIVEN entries close to REINSTATE / NO REINSTATE with a named
rationale; EVIDENCE-DRIVEN entries record CONFIRM CHANGE -- then checks for unflagged failures;
Phase 6a carries an entity-type referent column and a forward-annotated Check 6b annotation
with (a)/(b) repair paths. Phase 7 structural completion gate runs ten checks; each failing
check whose constraint class was forward-annotated upstream includes an explicit back-reference
naming the upstream phase and annotation that warned about the failure.

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
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
If none: "All reviewer concerns have been addressed with manuscript changes."

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

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy -- no-change because:
  statistical result -- power analysis (80% power at N=120, primary outcome, App. B Table B1)
  showed adequacy before data collection began.
  Entity: App. B Table B1 power analysis result (N=120, power=0.80) -- NOT "App. B alone".

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework -- no-change because:
  methodological argument -- Chen 2018 assumes panel data; cross-sectional design (2.1,
  single observation per participant) makes that framework inapplicable by structural assumption.
  Entity: Chen 2018 panel-data independence assumption (named principle) -- NOT "2.1 alone".

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
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

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
  constraint at its earliest visible points. Apply the Forward-annotation repair paths:
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
  visible points. Apply the repair paths:
  (a) Change was made but Phase 5 MANUSCRIPT OUTCOME records no change incorrectly: correct
      the MANUSCRIPT OUTCOME for that R-ID before proceeding.
  (b) Change was not made: revise Paragraph 1 to remove or rephrase the false claim.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```
