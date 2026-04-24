Written to `simulations/quest/variations/rhythm-rebuttal-variations-R12-2026-03-19.md`.

---

**R12 Variations — rhythm-rebuttal (Round 12)**

**Axes:**

| Axis | Criterion | What it isolates |
|------|-----------|-----------------|
| S | C-40 | Phase 2 carries canonical `Forward-annotation from Check 2c:` block alongside `Forward-annotation from Check 4 Part C:` |
| T | C-41 | Phase 7 Check 2c back-reference names Phase 2 as third upstream source (requires S) |
| U | C-42 | Phase 7 delegation repair blocks contain only the delegation line — no inline (a)/(b) follows |

**Predicted verdicts:**

| Variation | C-40 | C-41 | C-42 | Score |
|-----------|------|------|------|-------|
| V-01 (S) | PASS | FAIL | FAIL | 32/34 |
| V-02 (U) | FAIL | FAIL | PASS | 32/34 |
| V-03 (S+T) | PASS | PASS | FAIL | 33/34 |
| V-04 (S+U) | PASS | FAIL | PASS | 33/34 |
| V-05 (S+T+U) | PASS | PASS | PASS | 34/34 |

**Key design decisions:**

- Baseline is R11 V-05 with Phase 2 reduced to `Forward-annotation from Check 4 Part C:` only (C-40 absent). This scores 31/34 — passes C-09..C-39, fails C-40, C-41, C-42.
- Axis T cannot pass without Axis S (C-41 is conditional on C-40). V-03 demonstrates this is the natural coupling — naming Phase 2 as a source requires Phase 2 to actually carry the annotation.
- Axis U is independent: delegation-only works for Check 2c by delegating to Phase 5's canonical annotation regardless of whether Phase 2 has a Check 2c block. V-02 and V-04 isolate this.
- V-03 vs V-04 is the diagnostic contrast: V-03 shows full source graph without delegation minimality; V-04 shows delegation minimality with incomplete source graph.

**Excellence signals to watch for in V-05:** Phase 2 Check 2c block is a complete independently-actionable unit (gate label + unconditional failure condition + (a)/(b)). Phase 7 Check 2c back-reference names all three phases. Every Phase 7 `If FAIL` block ends at the delegation line — no (a)/(b) follows anywhere in Phase 7.
(which is self-contained regardless of whether Phase 2 has a Check 2c
block). C-42 can PASS when Axis S is absent, but the delegation points to two upstream sources
(Phase 5, Phase 6a) rather than three.

The V-03 vs V-04 contrast isolates the interaction: V-03 (S+T) shows that having the full
source graph (C-40+C-41) without delegation-only still creates dual repair surfaces; V-04
(S+U) shows that delegation-only with the expanded Phase 2 site (C-40) leaves the back-
reference source set incomplete (C-41 absent). V-05 closes both simultaneously.

**Excellence signals to watch for in V-05:**
1. Phase 2 carries two independently-labeled canonical blocks: "Forward-annotation from
   Check 2c:" (gate label + unconditional failure condition + (a)/(b)) followed by a separate
   "Forward-annotation from Check 4 Part C:" block.
2. Phase 7 Check 2c back-reference enumerates: "Phase 2 Forward-annotation from Check 2c
   warned..., Phase 5 Forward-annotation from Check 2c warned..., and Phase 6a entity-type
   referent column..." -- three sources, each named by canonical label.
3. Phase 7 Check 2c "If FAIL" repair block reads: back-reference sentence, then
   "Apply the Forward-annotation from Check 2c repair paths." -- nothing more. No (a)/(b)
   inline. Same minimal form for Check 4 Part C and Check 6b.

---

## Axis Rationales

**Axis S -- Phase 2 Check 2c annotation gap**: C-33 (R9) required Phase 2 to carry forward-
annotations for SHIFTED anti-deferral constraints (Check 4 Part C). C-39 (R11) required those
annotations to be canonical self-contained modules. Neither criterion required Phase 2 to
carry a Check 2c annotation, because Phase 2 was not recognized as a Check 2c decision point.
Phase 2 is where the author commits a P1-NC position AND names an evidence form -- making it
the earliest point at which Check 2c's entity-type requirement applies. Axis S adds a canonical
"Forward-annotation from Check 2c:" block to Phase 2's P1 pre-commitment section, making the
Check 2c constraint visible at the commitment decision point, not first at Phase 5 authoring.
Without Axis S, an author who names an evidence category at Phase 2 without a concrete entity
has no visibility into Check 2c's entity-type requirement until Phase 5.

**Axis T -- Phase 7 back-reference source-set update**: C-37 (R11) required Phase 7 back-
references to enumerate all upstream sources per gate. When Phase 7 Check 2c was established,
the known upstream sources were Phase 5 (MANUSCRIPT OUTCOME template annotation) and Phase 6a
(entity-type referent column). C-37 was satisfied by naming both. Axis S adds Phase 2 as a
third Check 2c annotation site. Axis T updates the Phase 7 Check 2c back-reference to reflect
this expanded source set. A variation that passes C-37 (names all previously-known sources)
fails C-41 (fails to name the new Phase 2 source) when the source set was established before
Axis S was in scope. C-41 closes the gap: after Axis S makes Phase 2 a Check 2c site, Axis T
ensures the back-reference reflects it.

**Axis U -- Phase 7 delegation minimality**: C-38 (R11) required Phase 7 to delegate to the
upstream annotation by label rather than restate paths independently. The delegation form
established in R11 reads "Apply the Forward-annotation repair paths:" followed by inline
(a)/(b). C-38 passes (delegation phrase exists, upstream annotation is named as authoritative)
but the inline (a)/(b) creates a second repair surface: the upstream annotation's (a)/(b) and
Phase 7's inline (a)/(b) are independent copies that can diverge on edit. Axis U removes the
inline content, making the delegation line the complete repair statement. Phase 7 becomes a
pure detection-and-delegation gate: it identifies the failure, names the upstream sources, and
delegates all repair to the upstream canonical annotations. The upstream annotations (C-39
compliant) are self-contained -- the author can find the failure condition and repair paths
there without returning to Phase 7.

---

## V-01 -- Phase 2 Check 2c Annotation (Axis S)

**Axis**: S only -- C-40 Phase 2 carries canonical "Forward-annotation from Check 2c:" block
**Hypothesis**: Phase 2 is the earliest point where the author commits a P1-NC position and
names an evidence form. Without a Check 2c annotation at Phase 2, the entity-type requirement
is invisible until Phase 5 authoring -- an author who writes "prior literature" at Phase 2
without naming Author Year has already failed Check 2c without knowing it. Adding a canonical
"Forward-annotation from Check 2c:" block to Phase 2 makes the entity-type requirement visible
at commitment time. Phase 7 back-reference is not updated (still names Phase 5 and Phase 6a
as two upstream sources -- C-41 absent). Phase 7 delegation blocks retain the delegation
phrase followed by inline (a)/(b) -- C-42 absent.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are structured as individually labeled
"Forward-annotation from Check X:" self-contained modules. Phase 2 carries two canonical
modules: "Forward-annotation from Check 2c:" makes the entity-type referent requirement
visible at the pre-commitment decision point; "Forward-annotation from Check 4 Part C:"
makes the anti-deferral requirement visible at the same point. Phase 7 back-references name
the two established upstream sources for Check 2c (Phase 5 and Phase 6a); Phase 2 as a Check
2c annotation site is not yet reflected in the back-reference source set. Phase 7 delegation
blocks carry the canonical delegation phrase followed by inline (a)/(b) repair paths.

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
  Back-reference: Phase 2 Forward-annotation from Check 4 Part C warned that PRESSURE-DRIVEN
  entries must commit REINSTATE or NO REINSTATE in Phase 6a before write -- an entry failing
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths:
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
  visible points.
  Apply the Forward-annotation repair paths:
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

## V-02 -- Phase 7 Delegation-Only Repair Blocks (Axis U)

**Axis**: U only -- C-42 Phase 7 "If FAIL" repair blocks contain only the delegation line
**Hypothesis**: R11 V-05 Phase 7 delegation blocks carry "Apply the Forward-annotation repair
paths:" followed by inline (a)/(b) content. C-38 passes (delegation phrase exists) but C-42
fails: two repair surfaces exist -- the upstream annotation's (a)/(b) and Phase 7's inline
(a)/(b) -- which can diverge on edit. Axis U removes the inline content, making the delegation
the complete repair statement. The upstream canonical annotations (Phase 5 Check 2c, Phase 5
Check 6b, Phase 6a Check 6b) are C-39-compliant self-contained modules; the author can find
the failure condition and repair paths there. Phase 7 becomes a detection-and-delegation gate
only. Phase 2 carries only canonical "Forward-annotation from Check 4 Part C:" (no Check 2c
annotation -- C-40 absent), so Phase 7 Check 2c back-reference names Phase 5 and Phase 6a
only (two sources -- C-41 absent).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are individually labeled "Forward-annotation from
Check X:" self-contained modules; Phase 2 carries a canonical "Forward-annotation from Check
4 Part C:" block. Phase 7 structural completion gate runs ten checks; each failing check's
repair block contains only the delegation line -- "Apply the Forward-annotation from Check X
repair paths." -- with no supplementary inline (a)/(b) content. The upstream canonical
annotation is the sole repair surface; Phase 7 detects and delegates rather than duplicating
repair instructions.

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
  Apply the Forward-annotation from Check 2c repair paths.

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
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths.

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
  visible points.
  Apply the Forward-annotation from Check 6b repair paths.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 -- Phase 2 Check 2c Annotation + Three-Source Back-Reference (Axes S+T)

**Axis**: S+T -- C-40 Phase 2 canonical Check 2c block + C-41 Phase 7 three-source enumeration
**Hypothesis**: Axis S makes Phase 2 the earliest Check 2c decision point by adding a canonical
"Forward-annotation from Check 2c:" block. Axis T updates Phase 7's Check 2c back-reference to
acknowledge Phase 2 as a named upstream source alongside Phase 5 and Phase 6a. An author
failing Check 2c learns they missed warnings at all three upstream phases -- not just the two
established sources. Phase 7 delegation blocks retain the canonical delegation phrase followed
by inline (a)/(b) -- C-42 absent: the delegation is a preamble to inline content, not the
complete repair statement.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are individually labeled "Forward-annotation from
Check X:" self-contained modules -- Phase 2 carries a canonical "Forward-annotation from
Check 2c:" block (making Phase 2 the earliest Check 2c decision point) alongside a canonical
"Forward-annotation from Check 4 Part C:" block. Phase 7 Check 2c back-reference enumerates
all three upstream annotation sources: Phase 2, Phase 5, and Phase 6a. Phase 7 delegation
blocks carry the canonical delegation phrase followed by inline (a)/(b) repair paths.

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
  Back-reference: Phase 2 Forward-annotation from Check 2c warned that a traceable instance
  was required at the pre-commitment decision point, Phase 5 Forward-annotation from Check 2c
  warned that entity-type specificity was required at authoring time, and Phase 6a entity-type
  referent column required the entity to be named during mid-workflow reconciliation -- an
  entry failing Check 2c missed that constraint at its earliest visible points.
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
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths:
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
  visible points.
  Apply the Forward-annotation repair paths:
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

## V-04 -- Phase 2 Check 2c Annotation + Delegation-Only (Axes S+U)

**Axis**: S+U -- C-40 Phase 2 canonical Check 2c block + C-42 delegation-only Phase 7 repair
**Hypothesis**: Axes S and U address independent gaps: S makes Phase 2 the earliest Check 2c
authoring-time decision point; U makes Phase 7 a pure detection-and-delegation gate. Combined,
Phase 2 exposes the entity-type constraint before any exchange is written, and Phase 7 does not
duplicate repair instructions. The back-reference source set is not updated: Phase 7 Check 2c
still names Phase 5 and Phase 6a as the two upstream sources (C-41 absent) -- Phase 2's
promotion to a Check 2c annotation site via Axis S is not yet reflected in the back-reference.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 carries two canonical modules: "Forward-annotation from Check 2c:"
makes the entity-type referent requirement visible at the pre-commitment decision point;
"Forward-annotation from Check 4 Part C:" makes the anti-deferral requirement visible at
the same point. Phase 7 structural completion gate runs ten checks; each failing check's
repair block contains only the delegation line -- the upstream canonical annotation is the
sole repair surface. Phase 7 Check 2c back-reference names the two established upstream
sources (Phase 5 and Phase 6a); Phase 2 as a third source is not yet named.

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
  Back-reference: Phase 5 Forward-annotation from Check 2c warned that entity-type specificity
  was required at authoring time, and Phase 6a entity-type referent column required the entity
  to be named during mid-workflow reconciliation -- an entry failing Check 2c missed that
  constraint at its earliest visible points.
  Apply the Forward-annotation from Check 2c repair paths.

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
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths.

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
  visible points.
  Apply the Forward-annotation from Check 6b repair paths.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 -- Full Integration (Axes S+T+U)

**Axis**: S+T+U -- C-40 Phase 2 Check 2c annotation + C-41 three-source back-reference +
C-42 delegation-only repair blocks
**Hypothesis**: Three structural gaps closed simultaneously. S makes Phase 2 the earliest
Check 2c annotation site -- the author sees the entity-type requirement at commitment time, not
first at Phase 5. T updates Phase 7's Check 2c back-reference to enumerate all three upstream
sources (Phase 2, Phase 5, Phase 6a) -- an author who fails Check 2c learns exactly which
three authoring phases warned them. U makes Phase 7 delegation blocks delegation-only -- no
inline (a)/(b) follows the delegation line; Phase 7 is a pure detection-and-delegation gate
that points to the upstream canonical annotations as the sole repair surface. The three phases
form a unified authority chain: Phase 2 commits (both gate constraints visible as canonical
modules), Phase 5 authors (both gate constraints visible), Phase 6a reconciles (Check 6b
constraint visible), Phase 7 detects failure and delegates to the upstream canonical
annotation -- one authoritative surface per constraint, no duplication.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 forward-annotations are individually labeled "Forward-annotation from
Check X:" self-contained modules -- Phase 2 carries a canonical "Forward-annotation from
Check 2c:" block (earliest Check 2c decision point) and a canonical "Forward-annotation from
Check 4 Part C:" block (earliest Check 4 Part C decision point). Phase 7 Check 2c back-
reference enumerates all three upstream sources by canonical label: Phase 2, Phase 5, and
Phase 6a. Every Phase 7 "If FAIL" repair block contains only the delegation line -- the
upstream canonical annotation is the sole repair surface; no inline (a)/(b) follows the
delegation. Phase 7 is a detection-and-delegation gate: it identifies the failure class,
names every upstream source that warned about it, and delegates all repair to the upstream
annotations.

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
  Back-reference: Phase 2 Forward-annotation from Check 2c warned that a traceable instance
  was required at the pre-commitment decision point, Phase 5 Forward-annotation from Check 2c
  warned that entity-type specificity was required at authoring time, and Phase 6a entity-type
  referent column required the entity to be named during mid-workflow reconciliation -- an
  entry failing Check 2c missed that constraint at its earliest visible points.
  Apply the Forward-annotation from Check 2c repair paths.

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
  Part C missed that constraint at its earliest visible point.
  Apply the Forward-annotation from Check 4 Part C repair paths.

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
  visible points.
  Apply the Forward-annotation from Check 6b repair paths.

All checks PASS -- proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```
