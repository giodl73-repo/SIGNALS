`prove-publish-rubric-v4` written. Here is the complete updated rubric:

---

**prove-publish-rubric-v4** written to `simulations/quest/rubrics/prove-publish-rubric-v4-2026-03-14.md`.

---

## What changed

**Four new aspirational criteria from R3 excellence signals:**

| ID | Name | Source | Key distinction |
|----|------|--------|-----------------|
| C-17 | Checklist symmetry -- pre-flight mirrors post-review | V-01 R3 defining axis | C-15 checks a post-review checklist exists; C-17 checks the checklist items *are the same ones* the author committed to at pre-flight -- one list, two uses, making surprise impossible |
| C-18 | Future Work table with machine-visible B-NN anchor column | V-02 R3 defining axis | C-16 checks at least one FW item names a B-NN gap; C-18 checks the requirement is enforced by table column structure -- a blank cell is structurally visible in a way a missing sentence never is |
| C-19 | Scaffold conflict mechanism documents classification drift | V-03 R3 defining axis | C-14 checks novelty tags were committed before prose; C-19 checks that when evidence *contradicts* the pre-committed classification, the conflict is named and a reclassification reason documented -- audit trail of where prior conception diverged from evidence |
| C-20 | Non-negotiable rules forward-declared at document header | V-04 R3 defining axis | No prior criterion captures this -- structural non-negotiables listed at the top of the document let a reviewer reject without reading the body; front-loads verification to the first visible line |

**Aspirational lifecycle coverage after v4:**

```
Pre-work gates    : C-12 (Status Quo first) -> C-13 (citation audit gate) -> C-14 (classify before prose)
                  : C-20 (non-negotiables declared at header before any section)
In-paper structure: C-09 (principles traced) + C-10 (cold-start readable) + C-11 (novelty tags)
                  : C-18 (table columns enforce loop criteria)
Post-completion   : C-15 (Skeptic checklist + verdict) -> C-17 (checklist mirrors pre-flight)
Forward loop      : C-16 (Future Work -> Status Quo gap) + C-18 (column makes it machine-visible)
Conflict audit    : C-19 (classification drift named and documented)
```

**Scoring:** aspirational pool expands 16 -> 24 pts (12 x 2), max total **114**. Golden threshold unchanged at >= 80 with all 5 essential passing.

---

## Design Notes

The R3 insight that distinguishes v4 from v3: v3 established *that* pre-work gates and verification loops must exist. v4 establishes *how* they must be structured -- via symmetry (C-17), table enforcement (C-18), conflict documentation (C-19), and header declaration (C-20). The difference is between requiring a gate and requiring a gate that cannot be quietly bypassed.

---

## Essential Criteria (weight: 60 -- must all pass)

**C-01** All 8 sections present | **C-02** Hypothesis explicitly resolved | **C-03** Evidence traceable | **C-04** Findings synthesized | **C-05** Principles extractable *(unchanged from v3)*

---

## Recommended Criteria (weight: 30 -- improve quality)

**C-06** Panel review, 2+ named roles | **C-07** Abstract standalone-useful | **C-08** Future Work concrete *(unchanged from v3)*

---

## Aspirational Criteria (weight: 24 -- raise the bar)

*(C-09 through C-16 unchanged from v3)*

### C-17 - Pre-flight checklist mirrors post-review checklist
- **Category**: process | **Weight**: aspirational (2 pts)
- **Source**: V-01 R3 defining axis
- **Text**: The checklist used by the Skeptic in post-completion review (C-15) contains the same structural commitments the author made at investigation start. One list, two uses: the author's pre-work promises are the Skeptic's verification items.
- **Pass condition**: C-15 must pass first. At least 3 Skeptic checklist items must have a corresponding pre-work antecedent. Papers where the Skeptic's checklist and pre-work setup share no items fail even if both blocks are formally present.

### C-18 - Future Work table with machine-visible B-NN anchor column
- **Category**: process | **Weight**: aspirational (2 pts)
- **Source**: V-02 R3 defining axis
- **Text**: The Future Work section is structured as a table with an explicit column for B-NN anchor citations. A blank anchor cell is structurally visible as a compliance gap -- it cannot be overlooked the way a missing sentence can.
- **Pass condition**: C-16 must pass first. The Future Work section uses a table with a dedicated B-NN anchor field per item. At least one row carries a B-NN citation. Rows with no anchor must be explicitly marked NET-NEW.

### C-19 - Scaffold conflict mechanism documents classification drift
- **Category**: process | **Weight**: aspirational (2 pts)
- **Source**: V-03 R3 defining axis
- **Text**: When evidence contradicts a novelty classification pre-committed in the scaffold (C-14), the paper contains an explicit SCAFFOLD CONFLICT entry: (a) finding ID, (b) original classification, (c) revised classification, (d) reason for change.
- **Pass condition**: C-14 must pass first. Either (a) at least one SCAFFOLD CONFLICT entry with all four fields if any classification changed, or (b) explicit attestation that all pre-committed classifications were confirmed with no changes. Silent reclassifications fail.

### C-20 - Non-negotiable structural rules forward-declared at document header
- **Category**: process | **Weight**: aspirational (2 pts)
- **Source**: V-04 R3 defining axis
- **Text**: Before any section content, the document declares the structural non-negotiables the finished paper must satisfy. A reviewer can scan this list and reject without reading the body if any declared requirement is visibly absent.
- **Pass condition**: A header block before the first content section names at least 3 verifiable structural non-negotiables. Generic quality statements do not count. Must be positioned before Abstract or as the first visible element.

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 24)
```

**Maximum score**: 114 | **Golden threshold**: all 5 essential pass + composite >= 80

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, 3 tiers |
| v2 | 2026-03-14 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational pool 5 x 2 pts |
| v3 | 2026-03-14 | Added C-14, C-15, C-16 from R2 excellence signals; aspirational pool 8 x 2 pts = 16 pts |
| v4 | 2026-03-14 | Added C-17, C-18, C-19, C-20 from R3 excellence signals; aspirational pool 12 x 2 pts = 24 pts |
area is complex") fail.

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

## Aspirational Criteria (weight: 24 -- raise the bar)

Each aspirational criterion is worth 2 pts. All 12 passing = 24 pts. Max total score is 114.

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
- **Source**: V-05 R1 excellence signal -- BASELINE MATCH vs NEW SIGNAL tagging (R1 scorecard C-04)
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
  otherwise have to infer (R1 scorecard C-10)
- **Text**: The paper includes a Status Quo section (or equivalent subsection) that explicitly
  records what the team believed about this topic before the investigation began. This makes the
  paper's contribution legible by contrast -- a reader can see exactly what changed.
- **Pass condition**: A Status Quo section or "Prior Belief" block is present that contains at
  least two concrete prior beliefs or assumptions held at investigation start. The section must
  precede the Hypothesis. Generic "background" text with no stated beliefs fails.

### C-13 - Citation audit precedes Findings
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-03 R1 excellence signal -- "Citation-audited before Findings begins" -- strongest
  single enforcement of C-03 across all variations (R1 scorecard C-03)
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
- **Source**: V-03 R2 defining axis -- "Classification scaffold committed BEFORE prose: forces
  the author to decide 'is this new?' before deciding what to say -- the strongest C-04
  enforcement of any variation" (R2 scorecard V-03 C-04)
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
- **Source**: V-04 R2 excellence -- Skeptic Post-Review with 5-item checklist, prediction
  outcome, APPROVED/FLAG verdict (R2 scorecard V-04 C-06)
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
- **Source**: V-04 R2 excellence -- "At least one [future work item] targets a gap in the Status
  Quo baseline" (R2 scorecard V-04 C-08)
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
- **Source**: V-01 R3 defining axis -- "pre-flight checklist items (Phase 2 Output A) become
  the post-review checklist (Phase 7) -- closed-loop design that creates self-auditing
  symmetry. The author's pre-work commitments and the Skeptic's post-completion verification
  are the same list." (R3 scorecard V-01)
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
- **Source**: V-02 R3 defining axis -- "FUTURE WORK TABLE with dedicated B-NN Anchor column
  makes C-16 machine-verifiable. Absence of a column entry is structurally visible in a way
  that a missing sentence never is." (R3 scorecard V-02)
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
- **Source**: V-03 R3 defining axis -- "The SCAFFOLD CONFLICT mechanism is a new contribution:
  when evidence contradicts the pre-committed classification, the conflict is named and a
  reclassification reason required, creating a visible audit trail of where the author's prior
  conception diverged from evidence." (R3 scorecard V-03)
- **Text**: When evidence gathered during the investigation contradicts a novelty classification
  that was pre-committed in the scaffold (C-14), the paper contains an explicit SCAFFOLD
  CONFLICT entry documenting: (a) the finding ID, (b) the original classification, (c) the
  revised classification, and (d) the reason for the change. This creates an audit trail of
  where the author's prior conception diverged from evidence. Papers where all pre-committed
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
- **Source**: V-04 R3 defining axis -- "Forward Declaration header block makes all gate
  violations visible before reading body. Non-negotiable rules listed at the header let a
  reviewer reject the paper without reading further." (R3 scorecard V-04)
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

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 24)
```

**Maximum score**: 114 (scores above 100 indicate papers that exceed all structural requirements;
114 means every gate, verification pattern, and loop closure was satisfied)
**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band       | Score              | Meaning                              |
|------------|--------------------|--------------------------------------|
| Golden     | >= 80, all E pass  | Publishable -- institutional memory  |
| Passing    | >= 60, all E pass  | Usable with gaps                     |
| Needs work | Any essential fail | Not yet a paper                      |
| Failing    | < 40               | Restart recommended                  |

---

## Version History

| Version | Date       | Changes                                                                                                       |
|---------|------------|---------------------------------------------------------------------------------------------------------------|
| v1      | 2026-03-14 | Initial rubric -- 10 criteria, 3 tiers                                                                        |
| v2      | 2026-03-14 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational pool redistributed to 5 x 2 pts              |
| v3      | 2026-03-14 | Added C-14, C-15, C-16 from R2 excellence signals; aspirational pool expanded to 8 x 2 pts = 16 pts          |
| v4      | 2026-03-14 | Added C-17, C-18, C-19, C-20 from R3 excellence signals; aspirational pool expanded to 12 x 2 pts = 24 pts  |
