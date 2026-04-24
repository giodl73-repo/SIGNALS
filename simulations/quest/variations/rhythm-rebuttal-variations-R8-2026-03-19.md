R8 variations written to `simulations/quest/variations/rhythm-rebuttal-variations-R8-2026-03-19.md`.

**What was generated:**

| Variation | Axis | Core change from R7 V-05 |
|-----------|------|--------------------------|
| V-01 | G only | Check 2c entity-type resolution: "prior literature" must name a paper/author; "statistical result" a statistic/test; "methodological argument" a named principle — location references without entity names fail |
| V-02 | H only | PRESSURE-DRIVEN splits REINSTATE/NO REINSTATE (not REINSTATE/CONFIRM CHANGE); EVIDENCE-DRIVEN now also requires CONFIRM CHANGE + named evidence sentence; both before write, not deferred |
| V-03 | I only | New Check 6b: Paragraph 1 change claims whose traced R-ID has a no-change MANUSCRIPT OUTCOME are structural contradictions — write-blocking |
| V-04 | G+H | Entity-type resolution + updated SHIFTED decision protocol |
| V-05 | G+H+I | Full integration — 10 Phase 7 checks |

**The three structural distinctions from R7:**
- G refines "traceable instance" → entity-type requirement (§3.2 alone fails; "Jones 2019" passes)
- H resolves the CONFIRM CHANGE ambiguity (PRESSURE-DRIVEN now uses NO REINSTATE; EVIDENCE-DRIVEN owns CONFIRM CHANGE)
- I is the only check that cross-references cover letter claims against Phase 5 outcome types — no prior check can detect this contradiction class
ral contradiction detectable only at this gate |
| **V-04** | G+H combined | Entity-type resolution + REINSTATE/NO REINSTATE + EVIDENCE-DRIVEN CONFIRM CHANGE |
| **V-05** | G+H+I full integration | All three axes |

**What changed structurally from R7**: All five maintain the complete R7 V-05 baseline (A+B+C+D+E+F+G+H+I as defined in R7). R8 axes refine the *precision* of existing gates and add one new consistency gate:

- **G refinement**: Check 2c already required a "traceable instance" (R7). C-28 sharpens the definition: the instance must be of the entity type the category implies — a paper/author for literature, a statistic/test for statistical, a named principle for methodological. A location reference (§3.2) without a named entity fails the *new* framing even if it passed R7's Check 2c.
- **H refinement**: The REINSTATE/CONFIRM CHANGE binary (R7) conflated "keep the change for non-scientific reasons" (PRESSURE-DRIVEN CONFIRM CHANGE) with "confirm the change was driven by evidence" (EVIDENCE-DRIVEN). C-29 separates these cleanly: PRESSURE-DRIVEN closes to REINSTATE or NO REINSTATE; EVIDENCE-DRIVEN requires its own CONFIRM CHANGE with a named evidence sentence. Both are now required before write.
- **I addition**: Check 6b is structurally novel — no prior criterion cross-references the cover letter's change claims against Phase 5 outcomes for semantic consistency. Check 6 confirms traceability; Check 6b confirms that what is traced is a change, not a non-response. The contradiction class it detects (cover letter says "changed" while MANUSCRIPT OUTCOME says "no change") is invisible to all prior checks.

---

## Axis Rationales

**Axis G — entity-type resolution gap**: Check 2c (C-25 → R7 G) requires a "traceable instance."
The phrase is correct but under-specified. An author writes: "No change — prior literature
(§3.2 of this manuscript) establishes the measurement approach." §3.2 is a locator but refers
to the author's own text, not a cited work. It passes R7's "Author Year, §Section" template
loosely interpreted. C-28 closes this by requiring the instance to be of the *entity type* the
category implies — prior literature resolves to a *cited paper or author*, not a self-citation
or section reference. The same logic applies: "statistical result (our model fit indices)" is
a description; "statistical result (RMSEA=.047, 90% CI [.031, .062], Table 4)" is a specific
statistic. "Methodological argument (our cross-sectional design)" restates the design; "the
independence assumption in Chen 2018 requires longitudinal measurement invariance not available
in cross-sectional data" names a specific methodological principle. The entity-type check is
the gate between "location present" and "evidence entity named."

**Axis H — REINSTATE/NO REINSTATE and EVIDENCE-DRIVEN decision gap**: R7 H introduced the
PRESSURE-DRIVEN binary as REINSTATE / CONFIRM CHANGE. The problem: "CONFIRM CHANGE" is
semantically ambiguous when applied to a PRESSURE-DRIVEN entry — it could mean "the change is
confirmed because the pressure was right" or "the change is confirmed even though it was
pressure-driven." C-29 resolves the ambiguity by renaming the non-reinstate outcome NO REINSTATE
— signaling that the author chose not to reverse the change made under pressure, while the
EVIDENCE-DRIVEN path takes ownership of CONFIRM CHANGE with a precise meaning: "we encountered
specific evidence that justified the change." The second half of C-29 closes the gap where
EVIDENCE-DRIVEN entries had no required decision in R7 — they only needed a Paragraph 2 audit.
C-29 requires EVIDENCE-DRIVEN entries to also record a named binary outcome (CONFIRM CHANGE +
the specific evidence) before write. The timing constraint — "cannot defer to cover letter" —
is a write-blocking constraint: the decision is recorded in Phase 6a, not summarized later.

**Axis I — cover letter / outcome consistency gap**: Check 6 (C-26 → R7) verifies R-IDs
present in Paragraph 1 claims. A claim with R-IDs passes Check 6. But Check 6 does not inspect
what the R-ID's MANUSCRIPT OUTCOME is. An author writes: "We revised the analysis of variance
structure in §3.2 in response to Reviewer 2 (R-07)." R-07's MANUSCRIPT OUTCOME is: "No change —
prior literature (Jones 2019) establishes that the original structure is appropriate." The cover
letter claims a change; Phase 5 records no change for that concern. Check 6 sees R-07 in
parentheses and passes. Check 6b sees that R-07's outcome is no-change and fails — because the
cover letter's assertion is false. This is a structural contradiction with a specific failure
mode: the author drafted the cover letter before finalizing exchanges, or updated exchanges
without updating Paragraph 1. Check 6b makes this class of contradiction detectable and
write-blocking.

---

## V-01 — Entity-Type Resolution in Check 2c

**Axis**: Axis G — C-28 entity-type resolution (single axis)
**Hypothesis**: Check 2c (R7) requires a "traceable instance." C-28 refines what "traceable"
means by requiring the instance to be of the entity type the evidence category implies. A
location reference without a named entity (§3.2, Appendix C without a statistic) satisfies
R7's phrasing but fails C-28's entity-type gate. This variation introduces the three entity-type
mappings — literature → paper/author; statistical → statistic/test; methodological → principle —
into RULE-1, Phase 2 pre-commitment examples, Phase 5 MANUSCRIPT OUTCOME annotations, and
Check 2c. All other R7 V-05 content is preserved.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Each valid form requires a category name AND a concrete referent of the
corresponding entity type — a cited paper or author (literature), a named statistic or
test (statistical), a specific methodological principle (methodological). Phase 2 commits
to both the revision narrative and any anticipated P1 no-change positions before
decomposition. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3
severity assignments. Forecast rows carry forward as flags into exchange headers. The
amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED
classification, then checks for unflagged failures. Phase 6a reconciliation requires each
Paragraph 1 change claim to trace to at least one R-ID. Phase 7 structural completion gate
verifies P1 no-change evidence entity-type resolution, cover letter traceability, SHIFTED
closure, and count-based integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category AND
a concrete referent of the corresponding entity type):
  - Prior literature: name a specific cited paper or author that validates the original
    approach or finding. Entity type: Author Year (e.g., Jones 2019) or paper title.
    A field description or self-citation does not satisfy this entity type.
  - Methodological argument: name a specific methodological principle that demonstrates
    the reviewer's proposed alternative is inferior given this study's design, population,
    or research question. Entity type: a named principle (e.g., "independence assumption
    in panel designs"). A restatement of the study design does not satisfy this entity type.
  - Statistical result: name a specific statistic or test that shows the data support the
    original claim. Entity type: a specific statistic with location (e.g., F(2,118)=14.3,
    Appendix C) or a named test with its result (e.g., paired t-test, p<.001, Table 2).
    A description of what the data show does not satisfy this entity type.

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces entity-type
resolution. A category label without a concrete referent of the corresponding entity type
fails Check 2c — a location reference (§3.2) without a named entity (paper, author,
statistic, or principle) does not satisfy RULE-1 at editorial submission standard.

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
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (verified in Phase 3.5; severity verified in Phase 3.6) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to a named binary decision.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 — named by category AND concrete referent of the
corresponding entity type):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [evidence category: entity-type referent — one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result — power analysis (80% power at N=120, primary outcome,
  Appendix B Table B1) showed adequacy before data collection began.
  [Entity type: specific statistic with location. NOT "our power was sufficient."]

  Example: P1-NC: Reviewer 3 request to adopt Chen 2018 framework — anticipated no-change
  because: methodological argument — the independence assumption in Chen 2018 requires
  longitudinal measurement invariance, which is unavailable in cross-sectional designs (§2.1).
  [Entity type: named methodological principle. NOT "our design is different from Chen 2018."]

  Example: P1-NC: Reviewer 2 challenge to construct validity — anticipated no-change
  because: prior literature — Jones and Park 2021 validated this construct measure in
  equivalent adult populations.
  [Entity type: specific cited paper. NOT "prior work supports our construct."]

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.
SHIFTED entries require classification. PRESSURE-DRIVEN entries require a named binary
decision (REINSTATE / CONFIRM CHANGE) — see Phase 6a protocol.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; no-change requires valid evidence form category
  AND entity-type referent; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial — fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

Example:
  R-03 typed scope not methodological because: reviewer requests new population-level
  replication; the existing study design is not questioned.

  R-07 typed framing not factual because: §2.3 states the claim correctly; the reviewer
  reads the abstract shorthand as a stronger universality claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance —
  not a restatement of the severity tier definition]

Valid: "R-05 assigned P2 not P1 because: the journal's author guidelines state secondary
outcome reporting requirements are non-blocking for desk review; R-05 concerns a sensitivity
analysis on the secondary outcome (§4.3, Table 3) and the primary outcome analysis is complete
and unreported."

Invalid: "R-05 assigned P2 not P1 because: this is a moderate concern." (Restates definition.)

Invalid: "R-05 assigned P2 not P1 because: the reviewer asked about sensitivity analysis."
(Describes the concern, does not state why it does not block acceptance.)

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism
(not just a concern property). These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism — reviewer tone, P1 inertia pressure, ambiguous claim — that will cause over-explanation] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed — buried, overlap, deferred] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row. The flag
appears in the exchange header and keeps the prediction visible during drafting.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form category AND
entity-type referent; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5; severity verified in Phase 3.6 for P2/P3):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale naming the valid RULE-1 evidence
form by category AND a concrete referent of the corresponding entity type (cited paper or
author / specific statistic or test / named methodological principle) if P1; RULE-2 applies
to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification and decision closure:

  | P1-NC | Evidence category + entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: pre-committed no-change was maintained; named evidence form and entity-type referent
  used in Phase 5. No re-examination required.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Decision required (choose one and state a one-sentence rationale):
      REINSTATE: [name the specific RULE-1 evidence category and entity-type referent that
      was valid before Phase 5 and remains valid — the change should be reversed]
      CONFIRM CHANGE: [name the specific non-scientific improvement achieved by the change
      (clarity, presentation, reduced ambiguity) — confirm the scientific claim is unaffected]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Re-examination required: Does cover letter Paragraph 2 accurately reflect the resolved
    disagreement? If this concern was listed as a standing disagreement and the shift resolved
    it, update Paragraph 2 to remove or revise the disagreement claim.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges (from Phase 4 forecast rows):
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority; add unflagged
failures as needed to reach three):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write — fix the failing check and re-run before proceeding.

**Check 1 — Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
PASS if counts match. FAIL if Phase 5 has fewer REVIEWER SAID blocks than Phase 3 R-IDs.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] — PASS / FAIL
If FAIL: identify missing R-IDs and write the missing exchanges before proceeding.

**Check 2a — Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME in Phase 5 must be either "[Section N]: [specific change]" or
"No change — [rationale]". No placeholder, deferred, or TBD outcomes.
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL
If FAIL: identify unresolved outcomes and complete them before proceeding.

**Check 2b — P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale using only invalid forms (restatement, precedent) fails.
CHECK: list each P1 no-change R-ID and its named evidence form category — PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the evidence form before proceeding.

**Check 2c — P1 no-change evidence entity-type resolution**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify the rationale names a concrete
referent of the entity type corresponding to the valid category:
  - Prior literature must resolve to a specific cited paper or author (Author Year or title).
    A field description ("prior work on this topic"), a self-citation (§3.2 of this paper),
    or a general claim ("the literature supports this") fails this check.
  - Statistical result must resolve to a specific statistic or named test with its result.
    A description ("the data support the original claim") or location without a value
    ("see Appendix C") fails this check.
  - Methodological argument must resolve to a specific named methodological principle.
    A restatement of the study design ("our cross-sectional design precludes this") fails;
    naming the assumption violated by the reviewer's alternative passes.
"Prior literature supports the approach" — fails (category present, no entity-type referent).
"Prior literature (Jones 2019) demonstrates this measurement approach is validated in
equivalent populations" — passes (cited paper named).
CHECK: list each P1 no-change R-ID, its evidence category, and its entity-type referent
— PASS / FAIL per entry
If FAIL: add the entity-type referent to the MANUSCRIPT OUTCOME rationale before proceeding.

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named with R-ID references)
and Paragraph 2 (areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 — Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange from Phase 5 must appear as a validated row in Phase 6b
(with ACCURATE / MISSED / OVERSTATED result).
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] — PASS / FAIL
Part B: Every SHIFTED entry in the Phase 6a pre-commitment audit must have a classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note. An entry with
only classification and no re-examination outcome fails Part B.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] — PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry from Phase 6a must have a named binary decision
(REINSTATE or CONFIRM CHANGE) with a one-sentence rationale. An entry with classification
and a re-examination note but no named binary decision fails Part C. "Considered" alone fails.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary decision + rationale] — PASS / FAIL
If any part fails: complete the missing element before proceeding.

**Check 5 — Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table (= REVIEWER SAID count after Check 1)
- manuscript_changes: R-IDs with MANUSCRIPT OUTCOME = section + change
- no_change_responses: R-IDs with MANUSCRIPT OUTCOME = No change
CHECK: all four values are integers, sum is consistent — PASS / FAIL
If FAIL: recompute from Phase 5 outcomes and correct frontmatter values.

**Check 6 — Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (Phase 2, updated in 6a) must include at least one
parenthetical R-ID reference. A claim with no R-ID reference is vague and fails this check.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) — PASS / FAIL per claim
If FAIL: add R-ID references to untraced claims. If no R-ID maps to the claim, the claim
names a change not driven by any reviewer concern — remove or rephrase before proceeding.

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 — REINSTATE/NO REINSTATE + EVIDENCE-DRIVEN CONFIRM CHANGE

**Axis**: Axis H — C-29 SHIFTED decision gate (single axis)
**Hypothesis**: R7 H introduced PRESSURE-DRIVEN REINSTATE/CONFIRM CHANGE. Two gaps remained.
First: "CONFIRM CHANGE" for PRESSURE-DRIVEN entries is semantically ambiguous — it reads as
"the change is confirmed" without distinguishing whether the confirmation is pressure-driven or
evidence-driven. Renaming the non-reinstate PRESSURE-DRIVEN outcome to NO REINSTATE clarifies:
the author chose not to reverse a change made under pressure, which is a different decision
from "the change is confirmed by evidence." Second: EVIDENCE-DRIVEN entries in R7 had no
required named decision — only a Paragraph 2 consistency check. C-29 requires EVIDENCE-DRIVEN
entries to also record CONFIRM CHANGE + the specific evidence encountered. Both decisions must
be recorded in Phase 6a before write — they cannot be deferred to the cover letter.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. Phase 3.5 audits ambiguous type assignments. Phase 3.6
audits P2/P3 severity assignments. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments
with SHIFTED classification — PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE
with a named rationale; EVIDENCE-DRIVEN entries close to CONFIRM CHANGE with the specific
evidence named; both decisions recorded before write — then checks for unflagged failures.
Phase 6a reconciliation requires each Paragraph 1 change claim to trace to at least one
R-ID. Phase 7 structural completion gate verifies SHIFTED decision closure for both
PRESSURE-DRIVEN and EVIDENCE-DRIVEN entries, cover letter traceability, and count-based
integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces traceable instance.

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
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (verified in Phase 3.5; severity verified in Phase 3.6) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification and a named binary decision recorded before write —
PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE; EVIDENCE-DRIVEN entries close
to CONFIRM CHANGE.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 — named by category and specific traceable instance):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [evidence category: specific instance — one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result — power analysis (80% power at N=120, primary outcome,
  Appendix B Table B1) showed adequacy before data collection began.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes. SHIFTED entries
require classification and a named binary decision recorded before write — PRESSURE-DRIVEN
close to REINSTATE or NO REINSTATE; EVIDENCE-DRIVEN close to CONFIRM CHANGE. Neither
decision may be deferred to the cover letter.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; no-change requires valid evidence form category
  AND specific traceable instance; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial — fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance —
  not a restatement of the severity tier definition]

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism.
These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism — reviewer tone, P1 inertia pressure, ambiguous claim] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form category AND
specific traceable instance; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."
  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."
  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale naming at least one valid RULE-1
evidence form category and specific traceable instance if P1; RULE-2 applies; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)". An unnamed change claim fails Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification and named binary decision:

  | P1-NC | Evidence category + instance | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: no re-examination required.

  SHIFTED: classify and record a named binary decision before proceeding — cannot defer
  to cover letter:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Decision required — choose one, state a one-sentence rationale, record before write:
      REINSTATE: [name the specific RULE-1 evidence category and instance that was valid
      before Phase 5 and remains valid — the change should be reversed; one sentence stating
      the evidence and the reversal decision]
      NO REINSTATE: [name the specific non-scientific benefit the change achieves even though
      it was made under pressure — clarity, reduced ambiguity, presentation quality; confirm
      the scientific claim is unaffected; one sentence]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Decision required — record before write:
      CONFIRM CHANGE: [name the specific evidence encountered that justified the change —
      one sentence naming the result, calculation, or argument; not a summary of the concern]

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges (from Phase 4 forecast rows):
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen**:
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write — fix the failing check and re-run before proceeding.

**Check 1 — Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] — PASS / FAIL

**Check 2a — Outcome resolution completeness**:
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL

**Check 2b — P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category — PASS / FAIL per entry

**Check 2c — P1 no-change evidence specificity (traceable instance present)**:
Each P1 no-change MANUSCRIPT OUTCOME that passed Check 2b names a specific traceable instance:
prior literature (Author Year, §N), methodological argument (named inferential claim + design
basis), statistical result (specific statistic + location). Category alone fails.
CHECK: list each P1 no-change R-ID, its category, and its traceable instance — PASS / FAIL per entry

**Check 3 — Cover letter structure**:
CHECK: PASS / FAIL

**Check 4 — Forecast validation coverage + SHIFTED decision closure**:
Part A: Every FLAGGED exchange appears as a validated row in Phase 6b.
CHECK: [n FLAGGED headers] vs [n validated rows] — PASS / FAIL
Part B: Every SHIFTED entry has classification and re-examination.
CHECK: [n SHIFTED] vs [n classified + re-examined] — PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry has a named binary decision (REINSTATE or NO REINSTATE)
with a one-sentence rationale. Every EVIDENCE-DRIVEN entry has CONFIRM CHANGE with a
one-sentence rationale naming the specific evidence encountered. Both decisions must be
recorded in Phase 6a before write — deferring to the cover letter fails Part C.
"Considered" alone fails. "Re-examined" alone fails. A decision name without a rationale
sentence fails.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with REINSTATE or NO REINSTATE + rationale] — PASS / FAIL
CHECK: [n EVIDENCE-DRIVEN entries] vs [n with CONFIRM CHANGE + named evidence] — PASS / FAIL
If any part fails: complete before proceeding.

**Check 5 — Frontmatter integer verification**:
CHECK: all four values integers, sum consistent — PASS / FAIL

**Check 6 — Cover letter Paragraph 1 traceability**:
CHECK: list each Paragraph 1 claim and its R-ID reference(s) — PASS / FAIL per claim

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 — Cover Letter Claim–Outcome Consistency Gate (Check 6b)

**Axis**: Axis I — C-30 Check 6b (single axis)
**Hypothesis**: Check 6 (C-26 → R7) requires R-ID references in each Paragraph 1 change claim.
A claim with a traced R-ID passes Check 6. But Check 6 does not verify that the traced R-ID's
MANUSCRIPT OUTCOME is a change. An author who drafts Paragraph 1 before finalizing exchanges —
or who updates exchanges without updating the cover letter — can produce a structurally
consistent-looking artifact where the cover letter says "we revised X in response to R-N" while
R-N's MANUSCRIPT OUTCOME says "No change." This contradiction is invisible to Checks 1-6 and
Check 2b/2c (which only audit P1 no-change quality). Check 6b introduces a cross-reference gate:
every R-ID cited in a Paragraph 1 change claim must resolve to a CHANGE MANUSCRIPT OUTCOME.
The gate is write-blocking: a cover letter asserting a change traced to a no-change outcome
cannot proceed to artifact write.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. Phase 3.5 audits ambiguous type assignments. Phase 3.6
audits P2/P3 severity assignments. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments
with SHIFTED classification, then checks for unflagged failures. Phase 6a reconciliation
requires each Paragraph 1 change claim to trace to at least one R-ID. Phase 7 structural
completion gate verifies count-based integrity, P1 no-change evidence quality, cover letter
traceability, and — after traceability — cover letter claim–outcome consistency: every R-ID
cited in a Paragraph 1 change claim must resolve to a CHANGE MANUSCRIPT OUTCOME, not a
no-change outcome.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category AND
a specific traceable instance within the category):
  - Prior literature: cite a specific work (Author Year, §Section or Table N)
  - Methodological argument: name the specific inferential claim and its study-design basis
  - Statistical result: name the statistic and its paper location (e.g., F(2,118)=14.3, App. C)

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces traceable instance.

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
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity. The type assigned in Phase 3 (verified in Phase 3.5; severity verified in Phase
3.6) determines the AUTHOR RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear
in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification; PRESSURE-DRIVEN entries close to a named binary decision.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 — named by category AND specific traceable instance):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [evidence category: specific instance — one sentence]

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.
SHIFTED entries require classification and re-examination.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; no-change requires valid evidence form category
  AND specific traceable instance; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial — fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance —
  not a restatement of the severity tier definition]

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism.
These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [name the structural reason] |

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form category AND
specific traceable instance; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."
  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."
  scope:          [2-3 sentences. RULE-3.]
  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."
  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"
  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale naming valid RULE-1 evidence form
category AND specific traceable instance if P1; RULE-2 applies; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)". An unnamed change claim fails Check 6.
  A change claim with an R-ID that traces to a no-change outcome fails Check 6b.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification:

  | P1-NC | Evidence category + instance | Phase 5 outcome | HELD / SHIFTED | Classification | Re-examination |
  |-------|------------------------------|-----------------|----------------|----------------|----------------|

  HELD: no re-examination required.

  SHIFTED: classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence.
    Decision required (choose one and state a one-sentence rationale):
      REINSTATE: [name the specific RULE-1 evidence that was valid before Phase 5 and remains
      valid — the change should be reversed]
      CONFIRM CHANGE: [name the specific non-scientific improvement achieved — confirm the
      scientific claim is unaffected]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 that genuinely changed
    the assessment.
    Re-examination required: Does Paragraph 2 accurately reflect the resolved disagreement?
    Update Paragraph 2 if needed.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges:
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen**:
1. [R-NN] — too defensive
2. [R-NN] — concedes too much
3. [R-NN] — too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write — fix the failing check and re-run before proceeding.

**Check 1 — Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks] vs [n R-IDs in Phase 3] — PASS / FAIL

**Check 2a — Outcome resolution completeness**:
CHECK: [n resolved OUTCOMEs] vs [n R-IDs] — PASS / FAIL

**Check 2b — P1 no-change evidence form category presence**:
CHECK: list each P1 no-change R-ID and its named evidence form category — PASS / FAIL per entry

**Check 2c — P1 no-change evidence specificity (traceable instance present)**:
Each P1 no-change MANUSCRIPT OUTCOME that passed Check 2b names a specific traceable instance:
prior literature (Author Year, §N), methodological argument (named inferential claim + design
basis), statistical result (specific statistic + location). Category alone fails.
CHECK: list each P1 no-change R-ID, its category, and its traceable instance — PASS / FAIL per entry

**Check 3 — Cover letter structure**:
CHECK: PASS / FAIL

**Check 4 — Forecast validation coverage + SHIFTED closure + PRESSURE-DRIVEN decision**:
Part A: Every FLAGGED exchange appears as a validated row in Phase 6b.
CHECK: [n FLAGGED headers] vs [n validated rows] — PASS / FAIL
Part B: Every SHIFTED entry has classification and re-examination.
CHECK: [n SHIFTED] vs [n classified + re-examined] — PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry has a named binary decision (REINSTATE or CONFIRM CHANGE)
with a one-sentence rationale.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with named binary + rationale] — PASS / FAIL

**Check 5 — Frontmatter integer verification**:
CHECK: all four values integers, sum consistent — PASS / FAIL

**Check 6 — Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 must include at least one parenthetical R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) — PASS / FAIL per claim
If FAIL: add R-IDs or remove untraced claims before proceeding.

**Check 6b — Cover letter Paragraph 1 claim–outcome consistency**:
For every Paragraph 1 change claim that passed Check 6, verify each traced R-ID has a CHANGE
MANUSCRIPT OUTCOME (section + specific change) in Phase 5. An R-ID with a "No change"
MANUSCRIPT OUTCOME cannot support a cover letter claim that asserts a change was made.
A cover letter asserting "we changed X in response to R-N" while R-N's MANUSCRIPT OUTCOME
is "No change" is a structural contradiction — the cover letter claims a change the manuscript
does not contain.
CHECK: list each Paragraph 1 claim, its R-ID(s), and each R-ID's MANUSCRIPT OUTCOME type
(CHANGE or NO CHANGE) — PASS if all traced R-IDs have CHANGE outcomes; FAIL if any R-ID
has a no-change outcome
If FAIL: either (a) correct the MANUSCRIPT OUTCOME for R-N if the change was actually made
but recorded incorrectly; or (b) revise Paragraph 1 to remove or rephrase the false claim.
Do not proceed to write with any Paragraph 1 claim whose traced R-ID has a no-change outcome.

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 — Entity-Type Resolution + REINSTATE/NO REINSTATE + EVIDENCE-DRIVEN CONFIRM CHANGE (G+H)

**Axes**: Axis G (C-28 entity-type resolution) + Axis H (C-29 REINSTATE/NO REINSTATE + EVIDENCE-DRIVEN CONFIRM CHANGE)
**Hypothesis**: G and H refine two parallel commitment gates. Axis G refines Check 2c: the
existing "traceable instance" requirement is sharpened to entity-type resolution — each evidence
category must resolve to the corresponding entity type, not a location reference that omits the
entity name. Axis H refines the SHIFTED decision protocol: PRESSURE-DRIVEN uses REINSTATE/NO
REINSTATE (removing the ambiguous CONFIRM CHANGE from that path) and EVIDENCE-DRIVEN now also
requires a named outcome (CONFIRM CHANGE + specific evidence). Together G+H close two vagueness
surfaces that remain in R7 V-05: "traceable instance without entity name" in Check 2c, and
"EVIDENCE-DRIVEN with no named decision" in Phase 6a.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Each valid form requires a category name AND a concrete referent of the
corresponding entity type — a cited paper or author (literature), a named statistic or
test (statistical), a specific methodological principle (methodological). Phase 2 commits
to both the revision narrative and any anticipated P1 no-change positions before
decomposition. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity
assignments. Forecast rows carry forward as flags into exchange headers. The amendment pass
validates FLAGGED exchanges first, audits P1 pre-commitments with SHIFTED classification —
PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE with a named rationale; EVIDENCE-
DRIVEN entries close to CONFIRM CHANGE with the specific evidence named; both decisions
recorded before write — then checks for unflagged failures. Phase 6a reconciliation requires
each Paragraph 1 change claim to trace to at least one R-ID. Phase 7 structural completion
gate verifies P1 no-change evidence entity-type resolution, SHIFTED decision closure for both
PRESSURE-DRIVEN and EVIDENCE-DRIVEN entries, cover letter traceability, and count-based
integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category AND
a concrete referent of the corresponding entity type):
  - Prior literature: name a specific cited paper or author (entity type: Author Year or title).
    A field description or self-citation does not satisfy this entity type.
  - Methodological argument: name a specific methodological principle (entity type: named
    principle). A restatement of the study design does not satisfy this entity type.
  - Statistical result: name a specific statistic or test with its result (entity type: e.g.,
    F(2,118)=14.3, App. C or paired t-test, p<.001, Table 2). A description of the data does
    not satisfy this entity type.

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces entity-type
resolution. A P1 no-change rationale naming a category but providing no entity-type referent
fails Check 2c — the category label alone does not meet editorial submission standard.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max.
Violation: a no-change response longer than 1 paragraph reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max.
Violation: a multi-paragraph scope response concedes the challenge has merit.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
Violation: combative or dismissive phrasing may cause rejection independent of merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns.
Violation: a merged exchange will be returned by the editorial office.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers.
Violation: non-integer values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any block missing any part is structurally incomplete and must be rewritten.
RULE-5 and RULE-8 enforce atomicity. Type verified in Phase 3.5; severity verified in Phase
3.6. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: hardest decisions committed
before Phase 5 drafting pressure. SHIFTED entries require classification and a named binary
decision — PRESSURE-DRIVEN close to REINSTATE or NO REINSTATE; EVIDENCE-DRIVEN close to
CONFIRM CHANGE; both recorded before write.

**Paragraph 1**: Name 3-4 changes this revision will make.

**Paragraph 2**: Name areas of respectful disagreement, or state none exist.

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
Name the concern and the anticipated evidence form (category AND entity-type referent):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [evidence category: entity-type referent — one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result — power analysis (80% power at N=120, App. B Table B1).
  [Entity type: specific statistic with location.]

  Example: P1-NC: Reviewer 2 request to adopt Chen 2018 framework — anticipated no-change
  because: methodological argument — the independence assumption in Chen 2018 requires
  longitudinal measurement invariance unavailable in cross-sectional designs (§2.1).
  [Entity type: named methodological principle.]

If none anticipated: "All P1 concerns will be addressed with manuscript changes."

SHIFTED PRESSURE-DRIVEN entries: REINSTATE or NO REINSTATE.
SHIFTED EVIDENCE-DRIVEN entries: CONFIRM CHANGE + named evidence.
Neither decision deferred to cover letter.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |

Type assignment guide — verified in Phase 3.5:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake | "Framing" — factual = paper error; framing = reviewer error |
| methodological | Existing design is flawed | "Scope" — methodological = current work wrong; scope = wants new work |
| scope | Requests new experiments or extensions | "Methodological" — scope = paper doesn't claim this |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis | "Methodological" — statistical = analysis; methodological = design |
| presentation | Clarity, structure, notation, language | Safe fallback, no scientific content impact |

Severity:
- **P1**: no-change requires category AND entity-type referent; check Phase 2 P1-NC
- **P2**: verified in Phase 3.6 before forecast
- **P3**: verified in Phase 3.6 before forecast

Sort: P1 first, P2, P3. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every scope, framing, or methodological assignment, state one sentence:

  R-[NN] typed [type] not [alternative] because: [specific distinguishing reason]

Correct Phase 3 if any assignment is wrong. Only these three types require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every P2 or P3 assignment, state one sentence:

  R-[NN] assigned [P2/P3] not P1 because: [specific paper-based reason, not tier definition]

Correct Phase 3 if any assignment is wrong. All P2/P3 require entries; P1 requires none.

---

## PHASE 4 -- WEAKNESS FORECAST

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure] |
| F-03 | [R-NN] | too brief | [structural reason] |

Forecast rows carry forward as flags into Phase 5 exchange headers.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (no-change requires category AND entity-type referent; see Phase 2 P1-NC) ---
--- P2 CONCERNS (severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:** > "[quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
  factual / methodological / scope / framing / statistical / presentation [see template]

**MANUSCRIPT OUTCOME:**
[Section + change. Or: No change — [category: entity-type referent (cited paper or author /
specific statistic or test / named principle) if P1; RULE-2; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 with actual changes; each claim includes parenthetical R-ID references.
  An untraced claim fails Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Evidence category + entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: no re-examination required.

  SHIFTED: classify and record a named binary decision before write:

    PRESSURE-DRIVEN:
      REINSTATE: [name the RULE-1 evidence category and entity-type referent that was valid
      before Phase 5 and remains valid — state the reversal decision; one sentence]
      NO REINSTATE: [name the specific non-scientific benefit achieved by the change — confirm
      scientific claim is unaffected; one sentence]

    EVIDENCE-DRIVEN:
      CONFIRM CHANGE: [name the specific evidence encountered that justified the change —
      one sentence naming the result, calculation, or argument; not a summary]

**6b. Forecast validation**: FLAGGED first, then unflagged.

| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|

Unflagged failures: name any quality failure not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED priority):
1. [R-NN] — too defensive
2. [R-NN] — concedes too much
3. [R-NN] — too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

All checks must PASS before writing. Any FAIL stops the write.

**Check 1**: [n REVIEWER SAID] vs [n R-IDs] — PASS / FAIL

**Check 2a**: [n resolved OUTCOMEs] vs [n R-IDs] — PASS / FAIL

**Check 2b**: List each P1 no-change R-ID and its evidence form category — PASS / FAIL per entry

**Check 2c — P1 no-change evidence entity-type resolution**:
Each P1 no-change MANUSCRIPT OUTCOME that passed Check 2b must name a concrete referent of
the corresponding entity type:
  - Prior literature: specific cited paper or author (Author Year or title)
  - Statistical result: specific statistic or named test with its result
  - Methodological argument: specific named methodological principle
A location reference without an entity name fails. A category label alone fails.
CHECK: list each P1 no-change R-ID, its evidence category, and its entity-type referent
— PASS / FAIL per entry

**Check 3**: Cover letter structure — PASS / FAIL

**Check 4 — Forecast validation + SHIFTED decision closure**:
Part A: [n FLAGGED headers] vs [n validated rows in 6b] — PASS / FAIL
Part B: [n SHIFTED] vs [n classified + re-examined] — PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry has REINSTATE or NO REINSTATE + one-sentence rationale.
Every EVIDENCE-DRIVEN entry has CONFIRM CHANGE + named evidence sentence. Both recorded
before write — not deferred to cover letter.
CHECK: [n PRESSURE-DRIVEN] vs [n with REINSTATE or NO REINSTATE + rationale] — PASS / FAIL
CHECK: [n EVIDENCE-DRIVEN] vs [n with CONFIRM CHANGE + named evidence] — PASS / FAIL

**Check 5**: Frontmatter integers — PASS / FAIL

**Check 6**: [n Paragraph 1 claims] vs [n with R-ID references] — PASS / FAIL per claim

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 — Full Integration (G+H+I)

**Axes**: Entity-type resolution (G) + REINSTATE/NO REINSTATE + EVIDENCE-DRIVEN CONFIRM CHANGE (H) + Check 6b claim–outcome consistency (I)
**Hypothesis**: All three R8 axes at maximum coverage. Axis G (C-28) refines Check 2c:
evidence categories must resolve to entity-type referents — cited paper/author for literature,
statistic/test for statistical, named principle for methodological. Axis H (C-29) refines the
SHIFTED decision protocol: PRESSURE-DRIVEN uses REINSTATE/NO REINSTATE; EVIDENCE-DRIVEN uses
CONFIRM CHANGE; both recorded before write, not deferred to the cover letter. Axis I (C-30)
adds Check 6b: every R-ID cited in a Paragraph 1 change claim must resolve to a CHANGE
MANUSCRIPT OUTCOME — a claim traced to a no-change R-ID is a structural contradiction
detectable only at this gate. Each axis is independently effective; combined they close the
three output-quality gaps that remain in R7 V-05 despite a 22/22 score.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Each valid form requires a category name AND a concrete referent of the
corresponding entity type — a cited paper or author (literature), a named statistic or
test (statistical), a specific methodological principle (methodological). Phase 2 commits
to both the revision narrative and any anticipated P1 no-change positions before
decomposition. Phase 3.5 audits ambiguous type assignments. Phase 3.6 audits P2/P3 severity
assignments — for each downgraded concern, one sentence states the specific paper-based
reason it does not block acceptance. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments
with SHIFTED classification — PRESSURE-DRIVEN entries close to REINSTATE or NO REINSTATE
with a named rationale; EVIDENCE-DRIVEN entries close to CONFIRM CHANGE with the specific
evidence named; both decisions recorded before write — then checks for unflagged failures.
Phase 6a reconciliation requires each Paragraph 1 change claim to trace to at least one
R-ID. Phase 7 structural completion gate verifies P1 no-change evidence entity-type
resolution, SHIFTED decision closure for all classified entries, cover letter traceability,
cover letter claim–outcome consistency (each traced R-ID resolves to a CHANGE outcome), and
count-based integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category AND
a concrete referent of the corresponding entity type):
  - Prior literature: name a specific cited paper or author (Author Year or title).
    Entity type: cited paper or author. Field descriptions and self-citations fail.
  - Methodological argument: name a specific methodological principle. Entity type: named
    principle. Restatements of study design fail.
  - Statistical result: name a specific statistic or test with its result (e.g., F(2,118)=14.3,
    App. C). Entity type: specific statistic or test. Descriptions of what the data show fail.

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails the
artifact. Phase 7 Check 2b enforces category presence; Check 2c enforces entity-type
resolution. A P1 no-change rationale naming a valid category without a concrete entity-type
referent fails Check 2c — the category label alone does not meet editorial submission standard.

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
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (verified in Phase 3.5; severity verified in Phase 3.6) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions are committed before Phase 5 drafting pressure can erode them. SHIFTED entries
in Phase 6a require classification and a named binary decision recorded before write.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (valid form from RULE-1 — named by category AND entity-type referent):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [evidence category: entity-type referent — one sentence]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result — power analysis (80% power at N=120, App. B Table B1).
  [Entity: specific statistic with location, not "power was sufficient."]

  Example: P1-NC: Reviewer 2 request to adopt Chen 2018 framework — anticipated no-change
  because: methodological argument — the independence assumption in Chen 2018 requires
  longitudinal measurement invariance unavailable in this cross-sectional design (§2.1).
  [Entity: named methodological principle, not "our design is different."]

  Example: P1-NC: Reviewer 3 challenge to construct validity — anticipated no-change
  because: prior literature — Jones and Park 2021 validated this measure in equivalent adult
  populations.
  [Entity: specific cited paper, not "prior work supports our construct."]

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a. SHIFTED PRESSURE-DRIVEN entries close to
REINSTATE or NO REINSTATE; SHIFTED EVIDENCE-DRIVEN entries close to CONFIRM CHANGE with
specific evidence named. Both decisions are recorded before write — cannot defer to cover
letter.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; no-change requires valid evidence form category
  AND entity-type referent; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain; assignment verified in Phase 3.6 before forecast
- **P3**: editorial — fix or note briefly; assignment verified in Phase 3.6 before forecast

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

Example:
  R-03 typed scope not methodological because: reviewer requests new population-level
  replication; the existing study design is not questioned.

  R-07 typed framing not factual because: §2.3 states the claim correctly; the reviewer
  reads the abstract shorthand as a stronger universality claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 3.6 -- SEVERITY DOWNGRADE AUDIT

For every concern assigned P2 or P3, verify the assignment before writing the forecast.
State one sentence per assignment:

  R-[NN] assigned [P2/P3] not P1 because:
  [specific paper-based or venue-based reason this concern does not block acceptance —
  not a restatement of the severity tier definition]

Valid: "R-05 assigned P2 not P1 because: the journal's author guidelines state secondary
outcome reporting requirements are non-blocking for desk review; R-05 concerns a sensitivity
analysis on the secondary outcome (§4.3, Table 3) and the primary outcome analysis is
complete."

Invalid: "R-05 assigned P2 not P1 because: this is a moderate concern." (Restates definition.)

If any severity assignment looks wrong on audit, correct the Phase 3 table before proceeding.
All P2 and P3 assignments require audit entries. P1 assignments require no entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism
(not just a concern property). These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism — reviewer tone, P1 inertia pressure, ambiguous claim] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form category AND
entity-type referent; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain; severity justified in Phase 3.6) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5; severity verified in Phase 3.6 for P2/P3):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale naming the valid RULE-1 evidence
form by category AND a concrete referent of the corresponding entity type (cited paper or
author / specific statistic or test / named methodological principle) if P1; RULE-2 applies
to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim fails Check 6. A change claim whose R-ID traces to a no-change
  MANUSCRIPT OUTCOME fails Check 6b.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification and named binary decision:

  | P1-NC | Evidence category + entity-type referent | Phase 5 outcome | HELD / SHIFTED | Classification | Decision | Rationale |
  |-------|------------------------------------------|-----------------|----------------|----------------|----------|-----------|

  HELD: pre-committed no-change maintained; entity-type referent used in Phase 5.
  No re-examination required.

  SHIFTED: classify and record a named binary decision before write — cannot defer to cover
  letter:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Decision required — choose one, state a one-sentence rationale, record before write:
      REINSTATE: [name the specific RULE-1 evidence category and entity-type referent that
      was valid before Phase 5 and remains valid — state that the change should be reversed;
      one sentence naming both the evidence and the reversal decision]
      NO REINSTATE: [name the specific non-scientific benefit the change achieves under
      pressure — clarity, reduced ambiguity, presentation quality; confirm the scientific
      claim is unaffected; one sentence]

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Decision required — record before write:
      CONFIRM CHANGE: [name the specific evidence encountered that justified the change —
      one sentence naming the result, calculation, or argument; not a summary of the concern]
      Also: Does cover letter Paragraph 2 accurately reflect the resolved disagreement?
      Update Paragraph 2 if this concern was listed as a standing disagreement.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges (from Phase 4 forecast rows):
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority; add unflagged
failures as needed to reach three):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

Run all checks before writing the artifact. Each check must PASS. Any FAIL stops
the write — fix the failing check and re-run before proceeding.

**Check 1 — Decomposition completeness**:
Count REVIEWER SAID blocks in Phase 5. Count R-ID entries in Phase 3 table.
PASS if counts match. FAIL if Phase 5 has fewer REVIEWER SAID blocks than Phase 3 R-IDs.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] — PASS / FAIL
If FAIL: identify missing R-IDs and write the missing exchanges before proceeding.

**Check 2a — Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME in Phase 5 must be either "[Section N]: [specific change]" or
"No change — [rationale]". No placeholder, deferred, or TBD outcomes.
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL
If FAIL: identify unresolved outcomes and complete them before proceeding.

**Check 2b — P1 no-change evidence form category presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale using only invalid forms (restatement, precedent) fails.
CHECK: list each P1 no-change R-ID and its named evidence form category — PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the evidence form before proceeding.

**Check 2c — P1 no-change evidence entity-type resolution**:
For every P1 MANUSCRIPT OUTCOME that passed Check 2b, verify the rationale names a concrete
referent of the entity type corresponding to the valid category:
  - Prior literature must resolve to a specific cited paper or author (Author Year or title).
    Field descriptions, self-citations, and general claims ("prior work supports") fail.
  - Statistical result must resolve to a specific statistic or named test with its result.
    Descriptions ("data support the claim") and locations without values fail.
  - Methodological argument must resolve to a specific named methodological principle.
    Study design restatements and conclusions without a named principle fail.
"Prior literature supports our approach" — fails (category present, no entity-type referent).
"Prior literature — Jones and Park 2021 validated this measure in equivalent populations"
— passes (specific cited paper named).
"Statistical result (paired t-test, p<.001, Table 2)" — passes (specific test with result).
"Methodological argument — the independence assumption in Chen 2018 requires panel data
unavailable here" — passes (specific named principle).
CHECK: list each P1 no-change R-ID, its evidence category, and its entity-type referent
— PASS / FAIL per entry
If FAIL: add the entity-type referent to the MANUSCRIPT OUTCOME rationale before proceeding.

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named with R-ID references)
and Paragraph 2 (areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 — Forecast validation coverage + SHIFTED decision closure**:
Part A: Every FLAGGED exchange from Phase 5 must appear as a validated row in Phase 6b
(with ACCURATE / MISSED / OVERSTATED result).
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] — PASS / FAIL
Part B: Every SHIFTED entry in the Phase 6a pre-commitment audit must have a classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note. An entry with
only classification and no decision fails Part B.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] — PASS / FAIL
Part C: Every PRESSURE-DRIVEN entry must have a named binary decision (REINSTATE or NO
REINSTATE) with a one-sentence rationale. Every EVIDENCE-DRIVEN entry must have CONFIRM
CHANGE with a one-sentence rationale naming the specific evidence encountered. Both decisions
must be recorded in Phase 6a — deferring to the cover letter fails Part C. "Considered" alone
fails. A decision name without a rationale sentence fails.
CHECK: [n PRESSURE-DRIVEN entries] vs [n with REINSTATE or NO REINSTATE + rationale] — PASS / FAIL
CHECK: [n EVIDENCE-DRIVEN entries] vs [n with CONFIRM CHANGE + named evidence] — PASS / FAIL
If any part fails: complete the missing element before proceeding.

**Check 5 — Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table (= REVIEWER SAID count after Check 1)
- manuscript_changes: R-IDs with MANUSCRIPT OUTCOME = section + change
- no_change_responses: R-IDs with MANUSCRIPT OUTCOME = No change
CHECK: all four values are integers, sum is consistent — PASS / FAIL
If FAIL: recompute from Phase 5 outcomes and correct frontmatter values.

**Check 6 — Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 (Phase 2, updated in 6a) must include at least one
parenthetical R-ID reference. A claim with no R-ID reference is vague and fails this check.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) — PASS / FAIL per claim
If FAIL: add R-ID references to untraced claims. If no R-ID maps to the claim, remove or
rephrase before proceeding.

**Check 6b — Cover letter Paragraph 1 claim–outcome consistency**:
For every Paragraph 1 change claim that passed Check 6 (R-ID reference present), verify
each referenced R-ID has a CHANGE MANUSCRIPT OUTCOME (section + specific change) in Phase 5.
A change claim whose traced R-ID has a "No change" MANUSCRIPT OUTCOME is a structural
contradiction: the cover letter asserts a change the manuscript does not contain. This is
the only check that cross-references the cover letter's change assertions against Phase 5
outcomes — no prior check can detect this divergence class.
CHECK: list each Paragraph 1 claim, its R-ID reference(s), and each R-ID's MANUSCRIPT OUTCOME
type (CHANGE or NO CHANGE) — PASS if all traced R-IDs have CHANGE outcomes; FAIL if any has
a no-change outcome
If FAIL: either (a) correct the MANUSCRIPT OUTCOME for the R-ID if the change was actually
made but recorded incorrectly in Phase 5; or (b) revise Paragraph 1 to remove or rephrase
the false claim. Do not proceed to write with any Paragraph 1 change claim whose traced R-ID
resolves to a no-change outcome.

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## Variation Comparison

| Dimension | V-01 (Axis G) | V-02 (Axis H) | V-03 (Axis I) | V-04 (G+H) | V-05 (G+H+I) |
|-----------|--------------|--------------|--------------|-----------|-------------|
| R7 V-05 baseline (A through I as in R7) | Yes | Yes | Yes | Yes | Yes |
| Check 2c — entity-type resolution (G) | Yes | No | No | Yes | Yes |
| RULE-1 entity-type referent language (G) | Yes | No | No | Yes | Yes |
| PRESSURE-DRIVEN: REINSTATE / NO REINSTATE (H) | No | Yes | No | Yes | Yes |
| EVIDENCE-DRIVEN: CONFIRM CHANGE required (H) | No | Yes | No | Yes | Yes |
| Check 4 Part C — both binaries + timing constraint (H) | No | Yes | No | Yes | Yes |
| Check 6b — claim–outcome consistency (I) | No | No | Yes | No | Yes |
| P1 no-change traceability level | entity-type referent | traceable instance | traceable instance | entity-type referent | entity-type referent |
| PRESSURE-DRIVEN outcome vocabulary | REINSTATE / CONFIRM CHANGE (R7) | REINSTATE / NO REINSTATE | REINSTATE / CONFIRM CHANGE (R7) | REINSTATE / NO REINSTATE | REINSTATE / NO REINSTATE |
| EVIDENCE-DRIVEN outcome | Paragraph 2 audit only | CONFIRM CHANGE + named evidence | Paragraph 2 audit only | CONFIRM CHANGE + named evidence | CONFIRM CHANGE + named evidence |
| Cover letter / Phase 5 consistency gate | No | No | Check 6b | No | Check 6b |
| Total Phase 7 checks | 8 (2a+2b+2c+3+4A+4B+4C+5+6) | 9 (adds 4C dual-type) | 9 (adds 6b) | 9 (2c+4C dual-type) | 10 (2c+4C dual-type+6b) |
| Phases | 7 + 3.5 + 3.6 | 7 + 3.5 + 3.6 | 7 + 3.5 + 3.6 | 7 + 3.5 + 3.6 | 7 + 3.5 + 3.6 |

## What changed from R7

All five R8 variations maintain the complete R7 V-05 architecture (RULE-N block with violation
consequences, Phase 2 P1-NC pre-commitment with instance requirement, Phase 3.5 type audit,
Phase 3.6 severity downgrade audit, forecast FLAGGED carry-forward, FLAGGED-first Phase 6b,
Phase 7 nine-check gate including Check 2b, Check 2c, Check 4 Part C, and Check 6). The R8
axes refine the precision of two existing gates and add one new consistency gate:

- **Axis G** closes the gap between "traceable instance present" (R7 Check 2c) and "entity-type
  referent named" — a location reference (§3.2) or description ("data support") satisfies R7's
  "traceable instance" loosely interpreted but fails C-28's entity-type check, which requires
  the instance to be of the type the category implies. The three entity types — cited paper/author,
  statistic/test, named methodological principle — make the gate mechanical: either the entity-type
  referent appears by name, or Check 2c fails.

- **Axis H** closes two gaps simultaneously: (1) PRESSURE-DRIVEN vocabulary precision — REINSTATE/
  CONFIRM CHANGE conflated "keep the change on non-scientific grounds" with "confirm the change was
  driven by evidence"; REINSTATE/NO REINSTATE separates the author's structural position (did not
  reverse the pressure-driven change) from the evidence question (does RULE-1 evidence still support
  the original position); (2) EVIDENCE-DRIVEN decision requirement — R7 required only a Paragraph 2
  consistency audit; C-29 requires EVIDENCE-DRIVEN entries to also close to a named outcome (CONFIRM
  CHANGE + specific evidence named), making EVIDENCE-DRIVEN as structurally committed as PRESSURE-
  DRIVEN.

- **Axis I** (Check 6b) is structurally novel — no prior criterion cross-references the cover
  letter's change assertions against Phase 5 MANUSCRIPT OUTCOMEs. The contradiction it detects
  (cover letter claims "changed X via R-N" while R-N records "No change") is invisible to all
  nine prior checks: Check 6 only verifies the R-ID is present, not what outcome it records;
  Checks 2b/2c only audit P1 no-change quality, not whether no-change R-IDs are cited as changes.
  Check 6b is the first and only gate that enforces semantic consistency between the cover letter's
  claims and the manuscript's actual changes.
