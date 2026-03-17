**prove-publish-rubric-v5** written to `simulations/quest/rubrics/prove-publish-rubric-v5-2026-03-14.md`.

---

## What changed

**Five new aspirational criteria from R4 excellence signals:**

| ID | Name | Source | Key distinction |
|----|------|--------|-----------------|
| C-21 | Non-negotiables block produced by a non-author role before investigation begins | V-05 R4 defining axis | C-20 checks the block exists at header; C-21 checks a different role produced it in Phase 2 -- before any evidence or prose -- making retroactive alignment impossible |
| C-22 | SCAFFOLD AUDIT subsection with per-finding slots | V-05/V-03 R4 defining axis | C-19 checks a conflict mechanism exists; C-22 checks it is a required subsection with one slot per finding -- a missing slot is a blank, not an absent sentence |
| C-23 | PF-NN antecedent ID field makes C-17 machine-verifiable | V-01 R4 defining axis | C-17 checks pre-flight symmetry by reader comparison; C-23 checks each post-review item carries a named "[Pre-flight antecedent: PF-NN]" field -- symmetry is a field check, not a claim |
| C-24 | FW Status column as binary classification distinct from anchor content | V-02/V-05 R4 defining axis | C-18 checks the FW table has a B-NN anchor column; C-24 checks a separate Status column classifies each row -- blank Status cell is visible without reading anchor content |
| C-25 | Role separation: scaffold produced by Mid-Skeptic, prose written by Lead Author | V-05 R4 defining axis | C-14 checks classification precedes prose; C-25 checks a different named role committed the scaffold -- bypassing C-14 or C-19 now requires a named role to explicitly fail a named sole responsibility |

**Aspirational lifecycle coverage after v5:**

```
Pre-work gates    : C-12 -> C-13 -> C-14 -> C-20 -> C-21 (non-author role, Phase 2) -> C-25 (Mid-Skeptic scaffold)
In-paper structure: C-09 + C-10 + C-11 + C-18 (anchor column) + C-24 (Status column separate)
Post-completion   : C-15 -> C-17 -> C-23 (PF-NN ID field, field-level check)
Forward loop      : C-16 + C-18 + C-24
Conflict audit    : C-19 + C-22 (per-finding slots + ATTESTATION required)
```

**Scoring:** aspirational pool expands 24 -> 34 pts (17 x 2), max total **124**.

---

## Design Notes

The R4 progression: v4 established *how* gates must be structured (symmetry, table enforcement, conflict documentation, header declaration). v5 establishes *who* and *when* -- structural guarantees only hold when role separation prevents the author from producing their own verification artifacts, and when structural slots (not prose requirements) enforce completeness. A SCAFFOLD AUDIT row cannot be quietly omitted; a missing row is a visible blank. A Pre-Skeptic-produced NON-NEGOTIABLES block cannot be retrofitted because it was written before the paper existed.

v4: gates cannot be quietly bypassed. v5: bypassing a gate requires an explicit named failure by a named role -- the audit trail captures not just drift but *who* caused it.
ict audit    : C-19 (scaffold conflict mechanism) + C-22 (per-finding slots enforce it)
```

**Scoring:** aspirational pool expands 24 -> 34 pts (17 x 2), max total **124**. Golden threshold unchanged at >= 80 with all 5 essential passing.

---

## Design Notes

The R4 insight that distinguishes v5 from v4: v4 established *how* gates and loops must be structured (symmetry, table enforcement, conflict documentation, header declaration). v5 establishes *who* and *when* -- the structural guarantees only hold when role separation prevents the author from producing their own verification artifacts, and when structural slots (not prose requirements) enforce completeness. A SCAFFOLD AUDIT row is not a sentence that could be omitted; a missing row is a visible blank. A Pre-Skeptic-produced NON-NEGOTIABLES block cannot be retrofitted to match what the paper ended up saying, because it was written before the paper existed.

The R4 progression: v4 criteria require that gates cannot be quietly bypassed. v5 criteria require that bypassing a gate requires an explicit named failure by a named role -- the audit trail does not just capture drift, it captures *who* caused it.

---

## Essential Criteria (weight: 60 -- must all pass)

### C-01 - All 8 sections present
- **Category**: format
- **Weight**: essential (12 pts)
- **Text**: The paper contains all 8 required sections: Abstract, Status Quo, Hypothesis, Evidence,
  Findings, Principles, Limitations, Future Work. No section may be absent or merged into another.
- **Pass condition**: All 8 sections are present with distinct headers. A paper missing any
  section fails this criterion regardless of content quality.

### C-02 - Hypothesis explicitly resolved
- **Category**: rigor
- **Weight**: essential (12 pts)
- **Text**: The paper states a clear hypothesis at the start and explicitly resolves it in the
  Findings or Conclusions -- accepted, rejected, or qualified with specific evidence cited.
- **Pass condition**: The hypothesis is stated as a falsifiable claim. The Findings section
  explicitly accepts, rejects, or qualifies it with a committed sentence. Hedged outcomes
  ("further research is needed") without a verdict fail.

### C-03 - Evidence is traceable
- **Category**: rigor
- **Weight**: essential (12 pts)
- **Text**: Every factual claim in Findings and Principles is traceable to a specific evidence
  source cited in the Evidence section. No finding is asserted without a cited basis.
- **Pass condition**: All evidence items are cited with enough specificity to locate the source.
  Findings that rest on uncited assertions fail. A citation audit block confirming zero uncited
  claims is the strongest form of compliance.

### C-04 - Findings are synthesized
- **Category**: depth
- **Weight**: essential (12 pts)
- **Text**: The Findings section synthesizes what the evidence means, not merely what it says.
  Each finding is a conclusion ("what does this mean?"), not a data summary ("what happened?").
- **Pass condition**: At least two findings are interpretive conclusions that go beyond restating
  evidence. A findings section that merely lists data points without synthesis fails.

### C-05 - Principles are extractable
- **Category**: utility
- **Weight**: essential (12 pts)
- **Text**: The Principles section contains numbered, actionable guidance directly extractable
  from the findings -- phrased as rules ("Always X", "When Y, do Z", "Prefer A over B because").
- **Pass condition**: At least two principles are present, numbered, and phrased as actionable
  rules. Generic observations ("quality matters", "this area is complex") fail.

---

## Recommended Criteria (weight: 30 -- improve quality)

### C-06 - Panel review with named expert roles
- **Category**: coverage
- **Weight**: recommended
- **Text**: The paper includes a simplified panel review section where at least two named expert
  roles (e.g. domain expert, skeptic, practitioner) provide critique, identify gaps, or assign
  a score.
- **Pass condition**: A review block is present with at least two distinct named reviewer
  perspectives. Each reviewer provides at least one substantive critique or endorsement, not
  just a score.

### C-07 - Abstract is standalone-useful
- **Category**: format
- **Weight**: recommended
- **Text**: The Abstract alone is sufficient for a reader to decide whether the paper is relevant
  to their question. It names the topic, the hypothesis, the method, and the key finding in
  under 200 words.
- **Pass condition**: A reader who reads only the Abstract can state: (a) what question was
  investigated, (b) how it was investigated, and (c) what was found. An abstract that merely
  describes structure ("this paper covers...") fails.

### C-08 - Future Work identifies concrete next questions
- **Category**: coverage
- **Weight**: recommended
- **Text**: The Future Work section lists specific, actionable next investigations -- not generic
  statements like "more research is needed."
- **Pass condition**: At least two future work items are phrased as investigable questions or
  proposed experiments, with enough specificity that a team could start them without further
  clarification.

---

## Aspirational Criteria (weight: 34 -- raise the bar)

Each aspirational criterion is worth 2 pts. All 17 passing = 34 pts. Max total score is 124.

### C-09 - Principles cross-referenced to findings
- **Category**: depth
- **Weight**: aspirational (2 pts)
- **Text**: Each principle in the Principles section is explicitly linked to the finding(s) that
  produced it (e.g. "Principle 1 [from F-02, F-05]: ..."). This creates a traceable chain from
  evidence to findings to principles.
- **Pass condition**: Every principle has at least one finding reference. Papers with unnumbered
  findings or unlinked principles fail.

### C-10 - New-team cold-start readability
- **Category**: behavior
- **Weight**: aspirational (2 pts)
- **Text**: The paper is self-contained enough that a team member with no prior context on this
  topic could read it and act on the principles without consulting the underlying investigation
  artifacts.
- **Pass condition**: The paper defines all domain-specific terms it uses, provides enough method
  context to understand why evidence was collected the way it was, and the Limitations section is
  honest about what the paper does not cover. Evaluated by attempting a cold read and checking
  for undefined jargon or unexplained jumps.

### C-11 - Findings classified by novelty
- **Category**: depth
- **Weight**: aspirational (2 pts)
- **Source**: V-05 R1 excellence signal -- BASELINE MATCH vs NEW SIGNAL tagging
- **Text**: Each finding is labeled to distinguish whether it confirms a prior belief
  (BASELINE MATCH) or challenges/extends it (NEW SIGNAL). This forces the author to
  explicitly identify what the investigation actually changed about the team's understanding.
- **Pass condition**: Every numbered finding carries a novelty tag. At least one finding is
  labeled NEW SIGNAL. Papers where all findings merely restate what was already believed fail
  this criterion even if synthesis quality is otherwise high.

### C-12 - Status Quo section documents prior belief baseline
- **Category**: coverage
- **Weight**: aspirational (2 pts)
- **Source**: V-05 R1 excellence signal -- Status Quo section gives new readers context they'd
  otherwise have to infer
- **Text**: The paper includes a Status Quo section (or equivalent subsection) that explicitly
  records what the team believed about this topic before the investigation began. This makes the
  paper's contribution legible by contrast -- a reader can see exactly what changed.
- **Pass condition**: A Status Quo section or "Prior Belief" block is present that contains at
  least two concrete prior beliefs or assumptions held at investigation start. The section must
  precede the Hypothesis. Generic "background" text with no stated beliefs fails.

### C-13 - Citation audit precedes Findings
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-03 R1 excellence signal -- "Citation-audited before Findings begins"
- **Text**: The paper demonstrates (or its prompt enforces) that all Evidence citations were
  verified complete before any Findings were written. This prevents rationalization drift --
  the tendency to write conclusions first and then backfill evidence to fit them.
- **Pass condition**: The paper includes an explicit audit note, completion gate, or structural
  ordering that demonstrates evidence was locked before conclusions were drawn. Acceptable
  forms: a pre-Findings evidence checklist, an "Evidence complete as of [date/artifact]"
  marker, or a method description that names citation audit as a lifecycle step. Papers with
  no evidence of this ordering fail even if C-03 passes.

### C-14 - Novelty scaffold pre-committed before findings prose
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-03 R2 defining axis -- "Classification scaffold committed BEFORE prose"
- **Text**: The novelty classification (BASELINE MATCH / NEW SIGNAL) for each finding is
  committed as a structured scaffold before any finding prose is written. This inverts the
  default authoring sequence -- labels precede prose -- preventing the author from rationalizing
  novelty after the fact.
- **Pass condition**: The paper includes a finding scaffold (or its prompt enforces one) where
  each finding's novelty tag is assigned before the finding is written out. Acceptable forms:
  a pre-prose classification table, a numbered scaffold with tags committed before body text,
  or a method note that names "classify before write" as a required step. C-11 passing (tags
  present) is necessary but not sufficient -- C-14 requires evidence the classification came
  first.

### C-15 - Skeptic post-review with structured checklist
- **Category**: coverage
- **Weight**: aspirational (2 pts)
- **Source**: V-04 R2 excellence -- Skeptic Post-Review with 5-item checklist and APPROVED/FLAG verdict
- **Text**: After the paper is drafted, a named Skeptic reviewer conducts a structured
  post-completion audit against a checklist of the paper's structural commitments and issues
  an explicit APPROVED or FLAG verdict. This is distinct from the panel review (C-06) -- the
  Skeptic role specifically verifies that all structural promises made at the start of the
  investigation were kept in the final paper.
- **Pass condition**: A Skeptic post-review block is present (beyond the 2+ roles counted for
  C-06) with: (a) a named checklist of at least 3 structural items checked, (b) an explicit
  pass/fail per item, and (c) a final APPROVED or FLAG verdict. Reviewers who only provide
  commentary without a structured checklist fail this criterion.

### C-16 - Future Work closes the Status Quo loop
- **Category**: depth
- **Weight**: aspirational (2 pts)
- **Source**: V-04 R2 excellence -- "At least one [future work item] targets a gap in the Status Quo baseline"
- **Text**: At least one item in the Future Work section explicitly targets a gap, assumption,
  or prior belief identified in the Status Quo section. This creates a self-reinforcing
  investigation cycle: each paper's Future Work seeds the Status Quo of the next investigation.
- **Pass condition**: At least one future work item names a specific prior belief (B-NN) or
  Status Quo gap from the paper's own Status Quo section and proposes to investigate it
  further. Generic future questions with no connection to the Status Quo baseline fail. C-12
  passing (Status Quo section present) is required for this criterion to be evaluated; papers
  without C-12 automatically fail C-16.

### C-17 - Pre-flight checklist mirrors post-review checklist
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-01 R3 defining axis -- closed-loop design, author pre-work commitments = Skeptic verification items
- **Text**: The checklist used by the Skeptic in post-completion review (C-15) contains the
  same structural commitments the author made at investigation start. One list, two uses: the
  author's pre-work promises are the Skeptic's verification items. This prevents the Skeptic
  from introducing new criteria the author was never told to satisfy, and prevents the author
  from making pre-work commitments that are never verified.
- **Pass condition**: C-15 must pass first. The Skeptic's checklist items can be traced back to
  commitments, outputs, or gates the author was required to produce at investigation start --
  not criteria invented post-hoc. At least 3 checklist items must have a corresponding
  pre-work antecedent. Papers where the Skeptic's checklist and the pre-work setup share no
  items fail even if both blocks are formally present.

### C-18 - Future Work table with machine-visible B-NN anchor column
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-02 R3 defining axis -- FUTURE WORK TABLE with dedicated B-NN Anchor column makes C-16 machine-verifiable
- **Text**: The Future Work section is structured as a table with an explicit column for B-NN
  anchor citations. Each row must declare its B-NN anchor or explicitly mark "NET-NEW". A
  blank anchor cell is structurally visible as a compliance gap -- it cannot be overlooked the
  way a missing sentence can. This enforces C-16 via structure rather than prose requirement.
- **Pass condition**: C-16 must pass first. The Future Work section uses a table (or equivalent
  structured format) with a dedicated B-NN anchor field per item. At least one row carries a
  B-NN citation. Rows with no anchor must be explicitly marked NET-NEW. A prose list of future
  work items with no anchor column fails even if C-16 passes.

### C-19 - Scaffold conflict mechanism documents classification drift
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-03 R3 defining axis -- SCAFFOLD CONFLICT mechanism creates visible audit trail of where prior conception diverged from evidence
- **Text**: When evidence gathered during the investigation contradicts a novelty classification
  that was pre-committed in the scaffold (C-14), the paper contains an explicit SCAFFOLD
  CONFLICT entry documenting: (a) the finding ID, (b) the original classification, (c) the
  revised classification, and (d) the reason for the change. Papers where all pre-committed
  classifications remain unchanged in a complex investigation are also suspect -- absence of
  any conflicts may indicate the scaffold was not genuinely pre-committed.
- **Pass condition**: C-14 must pass first. The paper either (a) contains at least one
  SCAFFOLD CONFLICT entry with all four required fields if any classification changed, or (b)
  includes an explicit attestation that all pre-committed classifications were confirmed by
  evidence with no changes required. Reclassifications with no stated reason fail. Papers that
  silently change classifications from the scaffold without a conflict entry fail.

### C-20 - Non-negotiable structural rules forward-declared at document header
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-04 R3 defining axis -- Forward Declaration header block makes all gate violations visible before reading body
- **Text**: The paper (or its authoring prompt) declares at the top -- before any section
  content -- the structural non-negotiables that the finished paper must satisfy. A reviewer
  can scan this list and, if any declared requirement is visibly absent, reject the paper
  without reading the body. This front-loads verification and eliminates the failure mode
  where a paper passes a superficial read because problems are buried in later sections.
- **Pass condition**: A header block is present before the first content section that names at
  least 3 structural non-negotiables for this paper (e.g., "CITATION AUDIT block with zero
  uncited claims must appear before Findings begins"). Each non-negotiable is phrased as a
  verifiable condition, not a goal. Generic quality statements ("the paper should be clear")
  do not count. The block must be positioned before Abstract or as the first visible element
  of the document.

### C-21 - Non-negotiables block produced by a non-author role before investigation begins
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-05 R4 defining axis -- Pre-Skeptic writes C-20 block in Phase 2 before any evidence or prose exists
- **Text**: The NON-NEGOTIABLES block required by C-20 is produced by a role other than the
  Lead Author, in Phase 2 (before any evidence has been gathered and before any paper prose
  has been written). A block produced by a non-author role before the paper exists cannot be
  retrofitted to match what the paper ended up saying -- the author has no future-knowledge of
  the paper's content to exploit when producing the block. This is the enforcement distinction
  between declaring non-negotiables and locking non-negotiables.
- **Pass condition**: C-20 must pass first. The NON-NEGOTIABLES block is attributed to a named
  non-author role (e.g., Pre-Skeptic, Compliance Auditor) and is dated or sequenced to Phase 2
  -- before Evidence gathering begins. A block produced by the Lead Author during paper writing,
  even if positioned at the document header, fails C-21. Papers with no phase attribution for
  the NON-NEGOTIABLES block fail unless another structural marker confirms pre-investigation
  production.

### C-22 - SCAFFOLD AUDIT subsection with per-finding slots
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-05/V-03 R4 defining axis -- SCAFFOLD AUDIT required subsection where a missing slot is a blank, not an absent sentence
- **Text**: The conflict mechanism required by C-19 is implemented as a SCAFFOLD AUDIT
  subsection with one dedicated slot per finding -- either CONFIRMED or CONFLICT (with four
  fields). A missing slot is structurally visible as a blank; it cannot go unnoticed the way
  an absent sentence can. The subsection also provides a mandatory ATTESTATION closing when
  all classifications are confirmed, closing the no-change path of C-19 via a required output,
  not an optional statement.
- **Pass condition**: C-19 must pass first. The Findings section contains a SCAFFOLD AUDIT
  subsection before finding prose. Each finding has a dedicated slot: either "F-NN:
  CONFIRMED" or "F-NN: CONFLICT -- Original: [...] / Revised: [...] / Reason: [...]". If
  all findings are confirmed, a closing ATTESTATION line is required: "ATTESTATION: All [N]
  pre-committed classifications confirmed. No changes." Papers where the audit is present
  as prose commentary rather than per-finding slots fail. Papers where the ATTESTATION is
  absent when no conflicts exist fail.

### C-23 - PF-NN antecedent ID field makes C-17 machine-verifiable
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-01 R4 defining axis -- "[Pre-flight antecedent: PF-NN]" field per post-review item transforms symmetry from reader comparison to field-level check
- **Text**: Each item in the Skeptic's post-review checklist (C-15) carries a named field
  "[Pre-flight antecedent: PF-NN]" that cites a specific pre-flight commitment produced in
  Phase 2. This transforms the C-17 symmetry check from a reader comparison across two blocks
  into a field-level verification: if the PF-NN field is blank or cites a non-existent
  pre-flight item, C-17 fails structurally without requiring any cross-document analysis.
- **Pass condition**: C-17 must pass first. Every post-review checklist item (from C-15) carries
  a "[Pre-flight antecedent: PF-NN]" field. At least 3 fields cite a PF-NN ID from the Phase 2
  pre-flight output. A blank field on any item is a structural failure. Papers where symmetry
  is claimed in prose ("these items correspond to the Phase 2 commitments") without per-item
  IDs fail C-23 even if they pass C-17.

### C-24 - FW Status column as binary classification distinct from anchor content
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-02/V-05 R4 defining axis -- Status column (B-NN ANCHOR or NET-NEW) is a separate field from anchor content; blank Status cell is visible without reading anchor
- **Text**: The Future Work table required by C-18 contains a dedicated Status column that
  classifies each row as either "B-NN ANCHOR" or "NET-NEW", separate from the B-NN anchor
  citation field. A blank Status cell is a compliance failure visible without reading any other
  field -- a reviewer does not need to examine the anchor content to detect a missing
  classification. This enforces C-16 and C-18 via orthogonal structural slots, not via a
  single combined field.
- **Pass condition**: C-18 must pass first. The Future Work table contains both a B-NN Anchor
  column AND a separate Status column. Status values are restricted to "B-NN ANCHOR" or
  "NET-NEW". A blank Status cell is explicitly documented as a structural failure. Papers where
  anchor classification is inferred from anchor content (e.g., "a row with no anchor is NET-NEW
  by implication") fail C-24 -- the Status column must be an explicit, independent field.

### C-25 - Role separation: scaffold produced by Mid-Skeptic, prose written by Lead Author
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-05 R4 defining axis -- role separation makes C-14 and C-19 enforcement structurally independent; bypassing requires named role to fail a named sole responsibility
- **Text**: The novelty classification scaffold required by C-14 is committed by a named role
  other than the Lead Author (e.g., Mid-Skeptic) before the Lead Author writes any finding
  prose. When scaffold producer and prose writer are different named roles, the Lead Author's
  only path when findings diverge from the scaffold is to file a SCAFFOLD CONFLICT entry.
  Bypassing it requires the Mid-Skeptic to fail a named sole responsibility -- the failure is
  attributable, not anonymous.
- **Pass condition**: C-14 must pass first. The novelty scaffold is attributed to a named role
  distinct from the Lead Author, and the scaffold is produced before any finding prose exists.
  The Lead Author is explicitly barred from modifying the scaffold without a SCAFFOLD CONFLICT
  entry. Papers where a single role both produces the scaffold and writes the prose fail C-25,
  even if C-14 passes. Papers with no role attribution for the scaffold fail.

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 34)
```

**Maximum score**: 124 (scores above 100 indicate papers that exceed all structural requirements;
124 means every gate, verification pattern, loop closure, role separation, and machine-verifiable
enforcement was satisfied)
**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band       | Score              | Meaning                              |
|------------|--------------------|--------------------------------------|
| Golden     | >= 80, all E pass  | Publishable -- institutional memory  |
| Passing    | >= 60, all E pass  | Usable with gaps                     |
| Needs work | Any essential fail | Not yet a paper                      |
| Failing    | < 40               | Restart recommended                  |

---

## Version History

| Version | Date       | Changes                                                                                                                       |
|---------|------------|-------------------------------------------------------------------------------------------------------------------------------|
| v1      | 2026-03-14 | Initial rubric -- 10 criteria, 3 tiers                                                                                        |
| v2      | 2026-03-14 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational pool redistributed to 5 x 2 pts                              |
| v3      | 2026-03-14 | Added C-14, C-15, C-16 from R2 excellence signals; aspirational pool expanded to 8 x 2 pts = 16 pts                          |
| v4      | 2026-03-14 | Added C-17, C-18, C-19, C-20 from R3 excellence signals; aspirational pool expanded to 12 x 2 pts = 24 pts; max 114          |
| v5      | 2026-03-14 | Added C-21, C-22, C-23, C-24, C-25 from R4 excellence signals; aspirational pool expanded to 17 x 2 pts = 34 pts; max 124   |
