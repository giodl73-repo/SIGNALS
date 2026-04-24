R6 variations written. Here's what was generated:

**The R6 problem**: R5 V-05 already scores 16/16 against v6 (C-23/C-24 were distilled from R5). R6 targets three latent failure modes that persist despite a perfect score:

| Variation | Axis | Innovation |
|-----------|------|------------|
| **V-01** | Axis D: P1 no-change evidence gate | Phase 7 Check 2b — P1 no-change MANUSCRIPT OUTCOME must name a valid RULE-1 evidence form by category; a "well-supported" rationale fails where "prior literature (Smith 2023)" passes |
| **V-02** | Axis E: Cover letter traceability | Phase 6a requires R-ID references in each Paragraph 1 change claim; Phase 7 Check 6 blocks vague cover letter claims at write time |
| **V-03** | Axis F: SHIFTED classification | Phase 6a SHIFTED entries classified PRESSURE-DRIVEN (re-examine if original no-change is still valid) or EVIDENCE-DRIVEN (re-examine if Paragraph 2 still claims this as a disagreement); Phase 7 Check 4 Part B blocks unclosed SHIFTED entries |
| **V-04** | D+E combined | Evidence gate + traceability |
| **V-05** | D+E+F full integration | All three axes — evidence enforced at write time, cover letter linked to R-IDs, position drift examined by type |

**What changed structurally from R5**: All five maintain the complete R5 V-05 baseline (A+B+C). R6 axes target the gap between "criterion specified" and "criterion enforced at the artifact boundary" — the same class of gap that generated C-24 in R5, now applied to P1 evidence quality (D), cover letter precision (E), and SHIFTED pre-commitment closure (F).
ase 7 Check 2 verifies MANUSCRIPT OUTCOMEs are filled in but not whether P1 no-change rationales name valid evidence. An author can write "No change — the approach is standard in the field" (appeal to precedent, invalid evidence form per RULE-1) and pass Check 2. Check 2b targets this gap: each P1 "No change" MANUSCRIPT OUTCOME must explicitly name at least one of the three valid RULE-1 evidence forms by category label (prior literature, methodological argument, statistical result). A rationale that names only invalid forms fails regardless of phrasing quality. This moves C-03 enforcement from declarative guidance into the mechanical gate that prevents artifact write — the same place as C-24.

**Axis E — Cover letter Paragraph 1 change claim traceability**: Phase 6a reconciliation updates Paragraph 1 to "reflect changes actually made" but doesn't enforce that each named change links to specific R-IDs. An author writes "We significantly strengthened the discussion" without naming which concerns drove the change. Axis E adds a traceability requirement: each Paragraph 1 change claim must include parenthetical R-ID references (e.g., "We revised the discussion of limitations (R-04, R-07)"). An unnamed change is detectable as vague. Phase 7 Check 6 verifies all Paragraph 1 claims have at least one R-ID reference before write — cover letter vagueness becomes a structural gate failure, not an editorial observation.

**Axis F — SHIFTED pre-commitment classification and re-examination**: Phase 6a records HELD/SHIFTED for P1-NC pre-commitments, requiring "state whether the shift was correct and why" for SHIFTED entries. But "correct" is not operationalized — an author can write "the reviewer's argument was compelling" without examining whether the original no-change position was valid. Axis F classifies each SHIFTED entry as PRESSURE-DRIVEN (author conceded under argument weight without new scientific evidence — original no-change position may still be valid) or EVIDENCE-DRIVEN (author encountered specific evidence in Phase 5 that genuinely changed the assessment). Each classification triggers a distinct re-examination protocol: PRESSURE-DRIVEN entries require checking whether RULE-1 valid evidence still supports no-change and whether the change was warranted; EVIDENCE-DRIVEN entries require checking whether cover letter Paragraph 2 accurately reflects the resolved disagreement. Phase 7 extends Check 4 or adds Check 6 to verify all SHIFTED entries have a classification and a closed re-examination before write.

---

## V-01 — P1 No-Change Evidence Form Verification Gate

**Axis**: Phase 7 Check 2b — P1 no-change rationale must name a valid evidence form by category (single axis D)
**Hypothesis**: RULE-1 names valid evidence forms and RULE-1 is applied at P1 writing time, but Phase 7 Check 2 only verifies that MANUSCRIPT OUTCOMEs are non-empty. An author who writes "No change — this finding is well-supported by the literature" satisfies Check 2 (non-empty), satisfies RULE-2 (one paragraph), but may be using an appeal to precedent (invalid form) rather than citing a specific prior work (valid form). The distinction is invisible at Check 2. Check 2b adds one mechanical test: does the P1 no-change rationale name prior literature, methodological argument, or statistical result by category or by named instance? A rationale that names only restatement or precedent fails regardless of phrasing length or quality. This closes the last gap between "C-03 declared in RULE-1" and "C-03 enforced at write time."

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. A type audit between decomposition and forecast eliminates
misclassification before it propagates. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments,
then checks for unflagged failures. Phase 7 structural completion gate verifies count-based
integrity including P1 no-change evidence form presence before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category):
  - Prior literature: cite specific prior work that validates the original approach or finding
  - Methodological argument: demonstrate that the reviewer's proposed alternative is inferior
    given the study design, population, or research question of this paper
  - Statistical result: show quantitatively that the data support the original claim

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails
the artifact — editors treat it as a non-response. A P1 no-change backed by at least one
valid evidence form (named by category) is acceptable; a P1 no-change backed only by
restatement or precedent is not. Phase 7 Check 2b enforces this mechanically before write.

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
in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS strategy in Phase 5.
Forecast flags from Phase 4 appear in the exchange header — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions — P1 no-change positions — are committed before Phase 5 drafting pressure can
erode them.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (must be a valid form from RULE-1 — prior literature, methodological argument,
or statistical result):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [one sentence naming the specific valid evidence form by category, not a restatement]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result (power analysis, Appendix B) showed 80% power at N=120 for
  the primary outcome.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

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
- **P1**: blocks acceptance — RULE-1 applies; any no-change response must name at least one
  valid evidence form by category; check Phase 2 P1-NC pre-commitments before drafting Phase 5
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

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

--- P1 CONCERNS (RULE-1 applies — no-change requires named valid evidence form; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological):

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
[Section + specific change. Or: No change — [rationale naming at least one valid RULE-1
evidence form by category if P1; RULE-2 applies to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Pre-committed evidence form | Phase 5 outcome | HELD / SHIFTED |
  |-------|----------------------------|-----------------|----------------|

  HELD: pre-committed no-change was maintained; named evidence form used in Phase 5
  SHIFTED: position changed during drafting — state whether the shift was correct and why

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

**Check 2b — P1 no-change evidence form presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale that says only "the approach is standard" or "the finding
is well-supported" without naming the evidence category fails this check.
CHECK: list each P1 no-change R-ID and its evidence form category — PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the specific evidence form before
proceeding. Do not advance to artifact write with an unnamed P1 no-change rationale.

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named) and Paragraph 2
(areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 — Forecast validation coverage**:
Every FLAGGED exchange from Phase 5 (every exchange header with "FLAGGED: [F-0N]")
must appear as a validated row in Phase 6b (with ACCURATE / MISSED / OVERSTATED result).
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] — PASS / FAIL
If FAIL: identify unvalidated FLAGGED exchanges and add Phase 6b rows before proceeding.

**Check 5 — Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table (= REVIEWER SAID count after Check 1)
- manuscript_changes: R-IDs with MANUSCRIPT OUTCOME = section + change
- no_change_responses: R-IDs with MANUSCRIPT OUTCOME = No change
CHECK: all four values are integers, sum is consistent — PASS / FAIL
If FAIL: recompute from Phase 5 outcomes and correct frontmatter values.

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 — Cover Letter Paragraph 1 Traceability

**Axis**: Phase 6a traceability requirement + Phase 7 Check 6 (single axis E)
**Hypothesis**: Phase 6a currently updates Paragraph 1 to "reflect changes actually made"
but does not enforce that each named change links to specific R-IDs. An author who writes
"We substantially revised the methodology section" satisfies Phase 6a without naming R-03
or R-09 (the methodological concerns that drove the change). After a Phase 6a update, the
cover letter can still contain untraced claims — a vague Paragraph 1 that passes every
current check. Axis E adds a traceability requirement: each Paragraph 1 change claim must
include parenthetical R-ID references. An unnamed change is detectable as vague and cannot
pass Phase 7. Phase 7 Check 6 verifies all claims have at least one R-ID reference before
write, making cover letter vagueness a structural gate failure rather than an editorial
observation that survives to submission.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. A type audit between decomposition and forecast eliminates
misclassification before it propagates. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments,
then checks for unflagged failures. Phase 6a reconciliation requires each Paragraph 1 change
claim to trace to at least one R-ID. Phase 7 structural completion gate verifies traceability
and count-based integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one):
  - Prior literature: cite specific prior work that validates the original approach or finding
  - Methodological argument: demonstrate that the reviewer's proposed alternative is inferior
    given the study design, population, or research question of this paper
  - Statistical result: show quantitatively that the data support the original claim

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails
the artifact — editors treat it as a non-response.

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
in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS strategy in Phase 5.
Forecast flags from Phase 4 appear in the exchange header — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions — P1 no-change positions — are committed before Phase 5 drafting pressure can
erode them.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (must be a valid form from RULE-1):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [one sentence naming the specific valid evidence form by category, not a restatement]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result (power analysis, Appendix B) showed 80% power at N=120 for
  the primary outcome.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

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
- **P1**: blocks acceptance — RULE-1 applies; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

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

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological):

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
[Section + specific change. Or: No change — [rationale citing at least one valid RULE-1
evidence form if P1; RULE-2 applies to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references for at least one concern that drove the change:
  Format: "We [change description] (R-NN)" or "We [change] (R-NN, R-NN)"
  A change claim without an R-ID reference is vague and will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Pre-committed evidence form | Phase 5 outcome | HELD / SHIFTED |
  |-------|----------------------------|-----------------|----------------|

  HELD: pre-committed no-change was maintained; named evidence form used in Phase 5
  SHIFTED: position changed during drafting — state whether the shift was correct and why

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

**Check 2 — Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME in Phase 5 must be either "[Section N]: [specific change]" or
"No change — [rationale]". No placeholder, deferred, or TBD outcomes.
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL
If FAIL: identify unresolved outcomes and complete them before proceeding.

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named with R-ID references)
and Paragraph 2 (areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 — Forecast validation coverage**:
Every FLAGGED exchange from Phase 5 must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] — PASS / FAIL
If FAIL: identify unvalidated FLAGGED exchanges and add Phase 6b rows before proceeding.

**Check 5 — Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table
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

## V-03 — SHIFTED Pre-Commitment Classification Protocol

**Axis**: Phase 6a SHIFTED classification + re-examination protocol (single axis F)
**Hypothesis**: Phase 6a currently records SHIFTED pre-commitments with "state whether
the shift was correct and why." This produces a logged observation but not a closed loop.
An author writes "the reviewer's argument was compelling" and the SHIFTED entry is satisfied.
But "compelling" is not a category. Two meaningfully different kinds of SHIFTED exist:
PRESSURE-DRIVEN (the author yielded under rhetorical or emotional weight without encountering
specific new scientific evidence — the original no-change position may still be scientifically
correct) and EVIDENCE-DRIVEN (the author encountered a specific new datum, calculation, or
argument in Phase 5 that genuinely changed the assessment — the change is likely correct).
These two types require different re-examination actions. PRESSURE-DRIVEN requires checking
whether RULE-1 valid evidence still supports the original no-change position — if it does,
the shift may have been wrong and should be reconsidered. EVIDENCE-DRIVEN requires checking
whether cover letter Paragraph 2 (disagreement framing) accurately reflects the resolved
position — if the concern was named as a standing disagreement and the shift resolved it,
Paragraph 2 must be updated. Phase 7 extends Check 4 to verify all SHIFTED entries are
classified and re-examined before write, preventing a SHIFTED event from remaining an
unexamined observation in the completed artifact.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. A type audit between decomposition and forecast eliminates
misclassification before it propagates. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments
with SHIFTED classification and type-specific re-examination, then checks for unflagged
failures. Phase 7 structural completion gate verifies SHIFTED entries are closed and
count-based integrity holds before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one):
  - Prior literature: cite specific prior work that validates the original approach or finding
  - Methodological argument: demonstrate that the reviewer's proposed alternative is inferior
    given the study design, population, or research question of this paper
  - Statistical result: show quantitatively that the data support the original claim

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails
the artifact — editors treat it as a non-response.

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
in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS strategy in Phase 5.
Forecast flags from Phase 4 appear in the exchange header — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions — P1 no-change positions — are committed before Phase 5 drafting pressure can
erode them.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (must be a valid form from RULE-1):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [one sentence naming the specific valid evidence form by category, not a restatement]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result (power analysis, Appendix B) showed 80% power at N=120 for
  the primary outcome.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.
SHIFTED entries require classification and re-examination — see Phase 6a protocol.

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
- **P1**: blocks acceptance — RULE-1 applies; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

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

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism
(not just a concern property). These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific mechanism that will cause over-explanation] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — no-change requires valid evidence form; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template:

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
[Section + specific change. Or: No change — [rationale citing at least one valid RULE-1
evidence form if P1; RULE-2 applies to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification:

  | P1-NC | Pre-committed evidence form | Phase 5 outcome | HELD / SHIFTED | Classification | Re-examination |
  |-------|----------------------------|-----------------|----------------|----------------|----------------|

  HELD: pre-committed no-change was maintained; named evidence form used in Phase 5.
  No re-examination required.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Re-examination required: Does RULE-1 valid evidence (prior literature, methodological
    argument, or statistical result) still support the original no-change position? If yes —
    state whether to restore the no-change; if the change was made on pressure alone, consider
    whether the position should be reinstated. If no — the change was correct; confirm the
    Phase 5 outcome stands.

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 (a named result,
    calculation, or argument not anticipated in Phase 2) that genuinely changed the assessment.
    Re-examination required: Does cover letter Paragraph 2 accurately reflect the resolved
    disagreement? If this concern was listed as a standing disagreement and the shift resolved
    it, update Paragraph 2 to remove or revise that disagreement claim.

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
PASS if counts match. FAIL if Phase 5 has fewer blocks than Phase 3 R-IDs.
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] — PASS / FAIL

**Check 2 — Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME in Phase 5 must be either "[Section N]: [specific change]" or
"No change — [rationale]". No placeholder, deferred, or TBD outcomes.
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 and Paragraph 2 (or explicit none).
CHECK: PASS / FAIL

**Check 4 — Forecast validation coverage + SHIFTED closure**:
Part A: Every FLAGGED exchange must appear as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] — PASS / FAIL
Part B: Every SHIFTED entry in Phase 6a pre-commitment audit must have a classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note. An entry with
classification only and no re-examination outcome fails Part B.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] — PASS / FAIL
If either part fails: complete the missing classification or re-examination before proceeding.

**Check 5 — Frontmatter integer verification**:
Compute actual values from Phase 5 outcomes:
- reviewer_count: total distinct reviewers in Phase 3 table
- concerns_addressed: total R-IDs in Phase 3 table
- manuscript_changes: R-IDs with MANUSCRIPT OUTCOME = section + change
- no_change_responses: R-IDs with MANUSCRIPT OUTCOME = No change
CHECK: all four values are integers, sum is consistent — PASS / FAIL

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 — Evidence Gate + Traceability (D+E)

**Axes**: P1 no-change evidence form verification in Phase 7 (D) + Cover letter Paragraph 1
traceability (E)
**Hypothesis**: D and E close two adjacent vagueness gaps that remain in R5 V-05. Axis D
targets the MANUSCRIPT OUTCOME layer: a P1 no-change rationale that names no valid evidence
form passes every prior check but would fail editorial review. Check 2b enforces that P1
no-change rationales name at least one valid RULE-1 evidence form category before write.
Axis E targets the cover letter layer: a Paragraph 1 change claim that names no R-ID is
vague — the connection between the stated revision and the reviewer concerns that drove it
is invisible to the editorial office. Check 6 enforces that all Paragraph 1 claims have
at least one R-ID reference. Together D+E make vagueness at two artifact surfaces (the
MANUSCRIPT OUTCOME and the cover letter) structurally detectable and blocking — both at the
same Phase 7 gate that already enforces C-24.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. A type audit between decomposition and forecast eliminates
misclassification before it propagates. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments,
then checks for unflagged failures. Phase 6a reconciliation requires each Paragraph 1 change
claim to trace to at least one R-ID. Phase 7 structural completion gate verifies P1 no-change
evidence form presence, cover letter traceability, and count-based integrity before artifact write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category):
  - Prior literature: cite specific prior work that validates the original approach or finding
  - Methodological argument: demonstrate that the reviewer's proposed alternative is inferior
    given the study design, population, or research question of this paper
  - Statistical result: show quantitatively that the data support the original claim

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails
the artifact. Phase 7 Check 2b enforces evidence form presence mechanically before write.

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
atomicity. The type assigned in Phase 3 (and verified in Phase 3.5) determines the AUTHOR
RESPONDS strategy in Phase 5. Forecast flags from Phase 4 appear in the exchange header.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and anticipated
evidence form (must be a valid form from RULE-1 — named by category):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [one sentence naming the specific valid evidence form by category, not a restatement]

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a for HELD / SHIFTED outcomes.

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
- **P1**: blocks acceptance — RULE-1 applies; no-change requires named valid evidence form;
  check Phase 2 P1-NC pre-commitments before drafting Phase 5 response
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

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

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only. The trigger column must name a causal mechanism. These rows carry forward as flags.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [specific mechanism that will cause over-explanation] |
| F-02 | [R-NN] | concedes too much | [reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [structural reason this concern gets under-addressed] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — no-change requires named valid evidence form; see Phase 2 P1-NC) ---
--- P2 CONCERNS (address or explain) ---
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
evidence form by category if P1; RULE-2 applies to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit:

  | P1-NC | Pre-committed evidence form | Phase 5 outcome | HELD / SHIFTED |
  |-------|----------------------------|-----------------|----------------|

  HELD: pre-committed no-change was maintained; named evidence form used in Phase 5
  SHIFTED: position changed — state whether the shift was correct and why

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges:
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | | | |
| F-02 | | | | |
| F-03 | | | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen**:
1. [R-NN] — too defensive
2. [R-NN] — concedes too much
3. [R-NN] — too brief

---

## PHASE 7 -- STRUCTURAL COMPLETION GATE

All checks must PASS before writing. Any FAIL stops the write.

**Check 1 — Decomposition completeness**:
CHECK: [n REVIEWER SAID blocks in Phase 5] vs [n R-IDs in Phase 3] — PASS / FAIL

**Check 2a — Outcome resolution completeness**:
Every MANUSCRIPT OUTCOME must be resolved (not placeholder/TBD).
CHECK: [n resolved MANUSCRIPT OUTCOMEs] vs [n R-IDs] — PASS / FAIL

**Check 2b — P1 no-change evidence form presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale using only invalid forms (restatement, precedent) fails.
CHECK: list each P1 no-change R-ID and its named evidence form category — PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the evidence form before proceeding.

**Check 3 — Cover letter structure**:
Paragraph 1 and Paragraph 2 present and structurally correct.
CHECK: PASS / FAIL

**Check 4 — Forecast validation coverage**:
Every FLAGGED exchange appears as a validated row in Phase 6b.
CHECK: [n FLAGGED exchange headers] vs [n validated rows in Phase 6b] — PASS / FAIL

**Check 5 — Frontmatter integer verification**:
Compute: reviewer_count, concerns_addressed, manuscript_changes, no_change_responses.
CHECK: all integers, sum consistent — PASS / FAIL

**Check 6 — Cover letter Paragraph 1 traceability**:
Every change claim in Paragraph 1 includes at least one parenthetical R-ID reference.
CHECK: list each Paragraph 1 claim and its R-ID reference(s) — PASS / FAIL per claim
If FAIL: add R-ID references to untraced claims. If no R-ID maps to the claim, remove or
rephrase — a claim with no R-ID origin is not a reviewer-driven revision.

All checks PASS — proceed to artifact write.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 — Full Integration (D+E+F)

**Axes**: Evidence form gate (D) + cover letter traceability (E) + SHIFTED classification (F)
**Hypothesis**: All three R6 axes at maximum coverage. Check 2b (D) verifies P1 no-change
rationales name a valid RULE-1 evidence form category — the last remaining gap between
RULE-1's declarative taxonomy and mechanical enforcement at write time. Check 6 (E) verifies
every Paragraph 1 change claim is traceable to at least one R-ID — cover letter vagueness
becomes a structural gate failure. The SHIFTED classification protocol (F) closes the loop
on P1-NC pre-commitment drift: PRESSURE-DRIVEN shifts trigger re-examination of whether the
original no-change position was valid; EVIDENCE-DRIVEN shifts trigger cover letter Paragraph 2
re-examination to ensure resolved disagreements are no longer listed. Phase 7 Check 4 Part B
verifies all SHIFTED entries are classified and re-examined. Together: evidence quality
enforced at write time (D), cover letter linked to reviewer concerns (E), position drift
examined by type rather than just logged (F). Each axis is independently effective; combined
they close the three vagueness gaps that remain in R5 V-05 despite a 16/16 score.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules are declared before
any work begins, each with a violation consequence. RULE-1 carries an explicit evidence
quality taxonomy: valid forms that overcome inertia (prior literature, methodological
argument, statistical result) and invalid forms that do not (restatement, appeal to
precedent). Phase 2 commits to both the revision narrative and any anticipated P1 no-change
positions before decomposition. A type audit between decomposition and forecast eliminates
misclassification before it propagates. Forecast rows carry forward as flags into exchange
headers. The amendment pass validates FLAGGED exchanges first, audits P1 pre-commitments
with SHIFTED classification and type-specific re-examination, then checks for unflagged
failures. Phase 6a reconciliation requires each Paragraph 1 change claim to trace to at
least one R-ID. Phase 7 structural completion gate verifies P1 no-change evidence form
presence, cover letter traceability, SHIFTED closure, and count-based integrity before write.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

Valid evidence forms (each overcomes inertia — use at least one; name the category):
  - Prior literature: cite specific prior work that validates the original approach or finding
  - Methodological argument: demonstrate that the reviewer's proposed alternative is inferior
    given the study design, population, or research question of this paper
  - Statistical result: show quantitatively that the data support the original claim

Invalid evidence forms (do NOT overcome inertia — do not use alone):
  - Restatement: repeating the original claim in different words, even if accurate
  - Appeal to authority or precedent: noting other reviewers did not raise this concern,
    or that the paper passed prior review, or that the claim appears in other published work

Violation: a P1 exchange with no-change supported only by invalid evidence forms fails
the artifact — editors treat it as a non-response. Phase 7 Check 2b enforces evidence form
presence mechanically: no P1 no-change MANUSCRIPT OUTCOME advances to write without naming
a valid evidence form category.

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
in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS strategy in Phase 5.
Forecast flags from Phase 4 appear in the exchange header — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER + P1 PRE-COMMITMENT (BEFORE DECOMPOSITION)

Write the cover letter and pre-commit to any anticipated P1 no-change decisions before
decomposing or responding to any concern. Commitment anchor: the hardest individual
decisions — P1 no-change positions — are committed before Phase 5 drafting pressure can
erode them. SHIFTED outcomes in Phase 6a require classification and re-examination.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

**P1 No-Change Pre-Commitment** (complete before Phase 3 decomposition):
For each P1 concern anticipated to result in no-change, name the concern and the anticipated
evidence form (must be a valid form from RULE-1 — named by category):

  P1-NC: [anticipated concern summary] — anticipated no-change because:
  [one sentence naming the specific valid evidence form by category — prior literature,
  methodological argument, or statistical result — not a restatement of the original claim]

  Example: P1-NC: Reviewer 1 challenge to sample size adequacy — anticipated no-change
  because: statistical result (power analysis, Appendix B) showed 80% power at N=120 for
  the primary outcome.

If no P1 no-change decisions are anticipated: "All P1 concerns will be addressed with
manuscript changes."

These pre-commitments are audited in Phase 6a. SHIFTED entries require classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and type-specific re-examination — see Phase 6a.

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
- **P1**: blocks acceptance — RULE-1 applies; any no-change response must name at least one
  valid evidence form by category; check Phase 2 P1-NC pre-commitments before drafting
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

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

--- P1 CONCERNS (RULE-1 applies — no-change requires named valid evidence form; see Phase 2 P1-NC pre-commitments) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological):

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
[Section + specific change. Or: No change — [rationale naming at least one valid RULE-1
evidence form by category if P1 (prior literature / methodological argument / statistical
result); RULE-2 applies to all no-change; RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation + P1 pre-commitment audit**:
Compare Phase 2 cover letter and P1-NC pre-commitments against Phase 5 outcomes.
- Update Paragraph 1 to reflect changes actually made. Each named change must include
  parenthetical R-ID references: "We [change] (R-NN)" or "We [change] (R-NN, R-NN)".
  An unnamed change claim will fail Phase 7 Check 6.
- Update Paragraph 2 for any shift in disagreement framing.
- P1 pre-commitment audit with SHIFTED classification:

  | P1-NC | Pre-committed evidence form | Phase 5 outcome | HELD / SHIFTED | Classification | Re-examination |
  |-------|----------------------------|-----------------|----------------|----------------|----------------|

  HELD: pre-committed no-change was maintained; named evidence form used in Phase 5.
  No re-examination required.

  SHIFTED: position changed during drafting. Classify and re-examine:

    PRESSURE-DRIVEN: author yielded under rhetorical or emotional argument weight without
    encountering specific new scientific evidence. The original no-change position may still
    be scientifically correct.
    Re-examination required: Does RULE-1 valid evidence (prior literature, methodological
    argument, or statistical result) still support the original no-change position? If yes —
    consider whether the change was warranted or whether the position should be reinstated.
    If no — the change was correct; confirm the Phase 5 outcome stands.

    EVIDENCE-DRIVEN: author encountered specific evidence in Phase 5 that genuinely changed
    the assessment. Re-examination required: Does cover letter Paragraph 2 accurately reflect
    the resolved disagreement? If this concern was named as a standing disagreement and the
    shift resolved it, update Paragraph 2 to remove or revise the disagreement claim.

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

**Check 2b — P1 no-change evidence form presence**:
For every P1 MANUSCRIPT OUTCOME that is "No change," verify the rationale names at least
one valid RULE-1 evidence form by category (prior literature / methodological argument /
statistical result). A rationale that says only "the approach is standard" or "the finding
is well-supported" without naming the evidence category fails this check.
CHECK: list each P1 no-change R-ID and its evidence form category — PASS / FAIL per entry
If FAIL: rewrite the MANUSCRIPT OUTCOME rationale to name the specific evidence form before
proceeding. A P1 no-change rationale using only invalid forms (restatement, precedent) is
not acceptable regardless of how it is phrased.

**Check 3 — Cover letter structure**:
Phase 2 (updated in 6a) contains exactly Paragraph 1 (3-4 changes named with R-ID references)
and Paragraph 2 (areas of disagreement named, or explicit statement that none exist).
CHECK: PASS / FAIL
If FAIL: identify which paragraph is missing or malformed and repair before proceeding.

**Check 4 — Forecast validation coverage + SHIFTED closure**:
Part A: Every FLAGGED exchange from Phase 5 must appear as a validated row in Phase 6b
(with ACCURATE / MISSED / OVERSTATED result).
CHECK: [n FLAGGED exchange headers in Phase 5] vs [n validated rows in Phase 6b] — PASS / FAIL
Part B: Every SHIFTED entry in the Phase 6a pre-commitment audit must have a classification
(PRESSURE-DRIVEN or EVIDENCE-DRIVEN) and a completed re-examination note. An entry with
only classification and no re-examination outcome fails Part B.
CHECK: [n SHIFTED entries] vs [n classified + re-examined entries] — PASS / FAIL
If either part fails: complete the missing validation or re-examination before proceeding.

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

## Variation Comparison

| Dimension | V-01 (Axis D) | V-02 (Axis E) | V-03 (Axis F) | V-04 (D+E) | V-05 (D+E+F) |
|-----------|--------------|--------------|--------------|-----------|-------------|
| RULE-1 evidence taxonomy (A) | Yes | Yes | Yes | Yes | Yes |
| P1-NC pre-commitment in Phase 2 (B) | Yes | Yes | Yes | Yes | Yes |
| Phase 7 five-check gate baseline (C) | Yes | Yes | Yes | Yes | Yes |
| Phase 7 Check 2b — P1 no-change evidence form (D) | Yes | No | No | Yes | Yes |
| Phase 6a Paragraph 1 traceability requirement (E) | No | Yes | No | Yes | Yes |
| Phase 7 Check 6 — traceability (E) | No | Yes | No | Yes | Yes |
| Phase 6a SHIFTED classification + re-examination (F) | No | No | Yes | No | Yes |
| Phase 7 Check 4 Part B — SHIFTED closure (F) | No | No | Yes | No | Yes |
| Total Phase 7 checks | 6 (2a+2b) | 6 | 5 | 7 (2a+2b+6) | 7 (2a+2b+4B+6) |
| P1 no-change enforcement surface | RULE-1 + pre-commit + gate | RULE-1 + pre-commit | RULE-1 + pre-commit | RULE-1 + pre-commit + gate | RULE-1 + pre-commit + gate |
| Cover letter vagueness detectable | No | Yes — Check 6 | No | Yes — Check 6 | Yes — Check 6 |
| SHIFTED drift examined by type | No | No | Yes — classification | No | Yes — classification |
| Phases | 7 + 3.5 | 7 + 3.5 | 7 + 3.5 | 7 + 3.5 | 7 + 3.5 |

## What changed from R5

All five R6 variations maintain the complete R5 V-05 architecture (RULE-N block with
violation consequences, Phase 2 P1-NC pre-commitment, Phase 3.5 type audit, forecast
FLAGGED carry-forward, FLAGGED-first Phase 6b, Phase 7 five-check gate). The R6 axes
target the gap between "every criterion specified" and "every criterion enforced at the
artifact boundary":

- **Axis D** closes the gap between RULE-1's declarative evidence taxonomy and Phase 7's
  enforcement: Check 2 passes a well-phrased invalid-evidence rationale; Check 2b does not.
- **Axis E** closes the gap between Phase 6a's reconciliation instruction and traceability:
  "update Paragraph 1 to reflect actual changes" produces vague claims; Check 6 does not allow them.
- **Axis F** closes the gap between Phase 6a's SHIFTED logging and its interpretation: "state
  whether the shift was correct and why" is an unstructured prompt; PRESSURE-DRIVEN / EVIDENCE-DRIVEN
  classification is a binary that triggers a defined re-examination action.
