Written to `simulations/quest/variations/prove-publish-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — prove-publish

| ID | Axis | Core bet |
|----|------|----------|
| **V-01** | Role sequence: PF-NN antecedent trace fields | C-17 is not structurally verified when symmetry is claimed by design. Emitting `PF-01`–`PF-05` IDs in the pre-flight and requiring `[Pre-flight antecedent: PF-NN]` per post-review item makes the trace one verifiable field, not a reader comparison. |
| **V-02** | Output format: paper NON-NEGOTIABLES block + FW table Status column | C-20 targets the paper document, not the prompt. C-18 needs a Status column (B-NN ANCHOR / NET-NEW) -- a blank cell is visible without reading the anchor value. Both enforced by output template additions only, no new phases. |
| **V-03** | Lifecycle emphasis: SCAFFOLD AUDIT as required Findings subsection | C-19 fails when SCAFFOLD CONFLICT entries are optional annotations. Promoting the conflict mechanism to a required subsection with a slot per finding makes every reclassification compulsory by structure. A missing slot is a blank, not an absent sentence. |
| **V-04** | Combined: 8-rule forward declaration + paper STRUCTURAL COMMITMENTS mirrors prompt | Rules 7 (C-17) and 8 (C-20) extend V-04 R3's pattern to the full R4 aspirational tier. C-20's paper-level requirement is satisfied by mirroring the 8 prompt rules into a PAPER STRUCTURAL COMMITMENTS block -- the prompt header and the paper header are the same list, two uses. |
| **V-05** | Combined: quad-criterion distribution to single owners | Pre-Skeptic owns C-20, Mid-Skeptic owns C-19, Post-Skeptic owns C-17, Lead Author owns C-18. V-05 R3's single-job isolation extended to all four new criteria without structural changes to the triple-Skeptic architecture. |

---

**Single-axis divergence:** V-01 isolates C-17 via ID-based trace fields; V-02 enforces C-20 as a paper output block and C-18 via Status column; V-03 makes C-19 structural through required subsection slots.

**Combination divergence:** V-04 mirrors the prompt's 8 rules into the paper header -- the document self-audits from its first line. V-05 distributes all four new criteria to single owners, the minimum structural change that achieves coverage without role overlap.

**The C-20 surface problem:** R3 non-negotiables live in the prompt header. C-20 requires them in the paper document before the Abstract. V-02 adds a PAPER NON-NEGOTIABLES block to the output template. V-04 mirrors 8 rules into a PAPER STRUCTURAL COMMITMENTS block. V-05 delegates the block to Pre-Skeptic as a named output -- the declaration precedes the investigation, satisfying C-20's requirement that it cannot be retrofitted after the paper is written.
d antecedent fields); V-02 enforces C-20 in the paper output and C-18 via table Status column; V-03 makes C-19 a compulsory Findings subsection rather than an optional annotation.

**Combination divergence:** V-04 extends the forward-declaration pattern to 8 rules and mirrors them into the paper body -- the first R4 variation where the paper's own opening block is an enforcement mechanism for C-20. V-05 distributes the four new criteria to single owners without changing the triple-Skeptic architecture -- each role adds exactly one new responsibility to what it already held in R3.

**The C-20 problem:** R3 variations put non-negotiables in the prompt header. C-20 requires them in the paper document header -- "before Abstract or as the first visible element." This is a different enforcement surface. V-02, V-04, and V-05 each address it differently: V-02 adds a paper-level NON-NEGOTIABLES block as part of the output template; V-04 mirrors the 8 prompt rules into a paper STRUCTURAL COMMITMENTS block; V-05 delegates the block to Pre-Skeptic as a named output before Lead Author writes anything.

---

## V-01: Checklist-Symmetry-Chain

**Axis:** Role sequence -- pre-flight checklist items emit named IDs (PF-01 through PF-05),
and the Skeptic post-review template contains an explicit "Pre-flight antecedent: PF-NN" field
per checklist item. Symmetry is enforced by named reference, not reader judgment.
**Hypothesis:** C-17 requires that at least 3 post-review checklist items have a corresponding
pre-work antecedent. The failure mode is that symmetry exists as a design claim ("these are
the same items") but is not structurally verifiable -- a reviewer must compare two blocks
manually. When the pre-flight output assigns IDs and the post-review template cites those IDs,
the trace is one field per item. A missing PF-NN citation is a blank field. A present-but-wrong
citation fails a simple ID check. This variation also adds C-18, C-19, C-20 via direct
template additions to the phases that already own the relevant structure.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight author + structural post-review), Lead Author (paper writer),
Domain Expert (substantive review), Practitioner (applicability review).

**Four non-negotiable rules:**
1. Status Quo section written by Skeptic before Lead Author writes a single section (C-12).
2. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13).
3. Novelty classification scaffold committed before any finding prose is written (C-14).
4. Skeptic post-review runs after paper draft, before panel review; each checklist item names
   its pre-flight antecedent by PF-NN ID (C-15, C-17).

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic:
- hypothesis, analysis, interview, websearch, synthesize

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path] or [not found]
```

If hypothesis not found: stop.
```
Cannot publish: no hypothesis artifact at simulations/prove/hypothesis/*.
Run /prove:hypothesis first.
```

---

### Phase 2: Skeptic Pre-Flight

Skeptic runs before Lead Author writes anything. Two outputs.

**Output A: Pre-Flight Checklist** (items receive IDs -- these IDs are reused in Phase 7)

```
SKEPTIC PRE-FLIGHT:
PF-01. Hypothesis verdict -- Findings will resolve H-01 with an explicit committed sentence.
PF-02. Citation traceability -- CITATION AUDIT will show zero uncited claims before Findings.
PF-03. Novelty scaffold -- classification committed before any finding prose written.
PF-04. Synthesis quality -- each finding answers "what does this mean?" not "what happened?".
PF-05. Principles actionability -- each principle is a rule, not a vague statement.

Prediction: [most likely structural failure -- one specific sentence]
Watch point: [section most at risk, with reason]
```

IDs PF-01 through PF-05 are declared. Phase 7 will trace each post-review item to one of these.

**Output B: Status Quo section (final text -- inserted verbatim into paper)**

```
## Status Quo

Before this investigation began, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief 1]
- [B-02: Concrete prior belief 2]
- [B-03: Concrete prior belief 3]

This investigation was motivated by: [gap or tension in the above].

Without this investigation, the default action would have been: [what team would have done].
```

Minimum 2 concrete prior beliefs (B-01, B-02 minimum). Not background prose.
Lead Author reads both outputs before writing.

---

### Phase 3: Evidence (Before Findings)

Lead Author writes Evidence before Abstract, before Findings.

Citation format:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For any uncitable claim:
`UNCITABLE: [claim text] -- no artifact source, moved to Limitations`

When Evidence is complete:
```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without citation anchor (must be 0 to proceed): [N]
Uncitable claims recorded for Limitations: [N]
Status: [PASS -- proceed to novelty scaffold] or [BLOCKED -- [N] uncited claims remain]
```

If BLOCKED: resolve before continuing.

---

### Phase 4: Novelty Classification Scaffold (Before Findings Prose)

With Evidence complete and audited:

```
NOVELTY CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH -- confirms B-XX] or [NEW SIGNAL -- challenges B-XX / B-NONE]
F-02: [BASELINE MATCH -- confirms B-XX] or [NEW SIGNAL -- challenges B-XX / B-NONE]
F-03: [BASELINE MATCH -- confirms B-XX] or [NEW SIGNAL -- challenges B-XX / B-NONE]
[Add F-04, F-05 as evidence supports]

NEW SIGNAL count: [N] of [N] findings.
```

If zero NEW SIGNAL:
```
SCAFFOLD FLAG: All classifications are BASELINE MATCH. No new signal identified.
Risk: synthesis may restate evidence rather than draw conclusions.
Proceeding -- INERTIA FLAG will appear in Findings.
```

---

### Phase 5: Hypothesis Verdict

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs]
Full verdict sentence: "[One committed quotable sentence]"
```

Accepted: "The hypothesis was confirmed: E-03 and E-05 show that..."
Not accepted: "The evidence is mixed." / "The evidence suggests..." / "Further work is needed."

---

### Phase 6: Write the Paper

Paper opens with a NON-NEGOTIABLES BLOCK before the Abstract. This is the first visible
element of the document. A reviewer can check these without reading any section content.

```
NON-NEGOTIABLES
1. All 8 sections present: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings,
   Principles, Limitations, Future Work.
2. CITATION AUDIT block present in Evidence section with Status: PASS and zero uncited items.
3. SCAFFOLD AUDIT present in Findings: every finding classified; any reclassification has
   a stated reason.
4. Skeptic Post-Review APPROVED verdict present before Domain Expert and Practitioner.
5. Future Work table present with B-NN Anchor and Status columns; at least one row carries
   Status: B-NN ANCHOR naming a gap from the Status Quo section.
```

**1. Abstract** (<200 words)
State: (a) question investigated, (b) method, (c) key finding, (d) practical implication.
Do not describe paper structure. Written after verdict is known.

**2. Status Quo** (paste verbatim from Phase 2 Output B)

**3. Hypothesis**
`H-01: [hypothesis text] (source: [file path])`
If amended: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Why evidence was gathered this way.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 -- all E-[N] items with citations)

```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**

Hypothesis verdict first (required):
```
HYPOTHESIS VERDICT
H-01: [text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[Committed sentence]"
```

SCAFFOLD AUDIT subsection (required, before finding prose):
```
SCAFFOLD AUDIT
F-01: [pre-committed classification] -- [CONFIRMED]
  or CONFLICT:
    Finding ID: F-01
    Original classification: [BASELINE MATCH / NEW SIGNAL -- B-XX]
    Revised classification: [new form]
    Reason: [what evidence showed that contradicted the pre-committed tag]

F-02: [pre-committed classification] -- [CONFIRMED]
  or CONFLICT: [4 fields]

[Continue for all findings in Phase 4 scaffold]

ATTESTATION (if no conflicts): All [N] pre-committed classifications confirmed. No changes.
```

Finding prose using Phase 4 scaffold (do not reclassify without SCAFFOLD AUDIT entry):
```
F-01 [BASELINE MATCH -- confirms B-01]:
[conclusion answering "what does this mean?" -- not "what happened?"]

F-02 [NEW SIGNAL -- challenges B-02]:
[conclusion]
```

CONTRIBUTION or INERTIA FLAG as appropriate.

**7. Principles**
Minimum 2 numbered rules. Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites finding: `P-01 [from F-02]: ...`
Tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`

**8. Limitations**
What the investigation did not cover. Uncitable claims from Phase 3.

**9. Future Work**

Required table format:

| Item  | Question                                      | B-NN Anchor              | Status       |
|-------|-----------------------------------------------|--------------------------|--------------|
| FW-01 | [Investigable question, specific enough start]| [B-NN from Status Quo]   | B-NN ANCHOR  |
| FW-02 | [Additional question]                         | --                       | NET-NEW      |

Column rules:
- Status must be "B-NN ANCHOR" or "NET-NEW" -- blank Status = structural failure.
- At least one row must carry Status: B-NN ANCHOR.
- NET-NEW rows need no anchor but must be marked explicitly.

---

### Phase 7: Skeptic Post-Review (Before Panel)

After paper is fully drafted. Skeptic audits against Phase 2 Output A.
Each checklist item names its pre-flight antecedent by PF-NN ID.

```
SKEPTIC POST-REVIEW:
Item 1 -- Hypothesis verdict [Pre-flight antecedent: PF-01]:
  [PASS -- explicit committed verdict sentence present]
  or [FLAG -- verdict sentence missing, evasive, or uncited]

Item 2 -- Citation traceability [Pre-flight antecedent: PF-02]:
  [PASS -- CITATION AUDIT block shows Status: PASS, zero uncited]
  or [FLAG -- audit missing or uncited claims in Evidence]

Item 3 -- Novelty scaffold [Pre-flight antecedent: PF-03]:
  [PASS -- Phase 4 scaffold committed before Phase 6 prose; SCAFFOLD AUDIT present in Findings]
  or [FLAG -- scaffold absent, or SCAFFOLD AUDIT missing, or CONFLICT entry incomplete]

Item 4 -- Synthesis quality [Pre-flight antecedent: PF-04]:
  [PASS -- findings answer "what does this mean?" not raw data]
  or [FLAG -- N findings restate evidence rather than drawing conclusions]

Item 5 -- Principles actionability [Pre-flight antecedent: PF-05]:
  [PASS -- all principles action-oriented rules with finding citations]
  or [FLAG -- N principles vague or uncited]

Antecedent trace check: Items 1-5 each cite a PF-NN antecedent.
C-17 minimum: at least 3 items cite a PF-NN from Phase 2 Output A. Result: [N of 5].

Pre-flight prediction outcome: [CONFIRMED] or [RESOLVED] or [STILL PRESENT -- location]

Final verdict: [APPROVED] or [FLAG: items N failed -- paper must be amended]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict. Panel does not begin until APPROVED.

---

### Phase 8: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy and domain correctness of Findings. Assesses Status Quo accuracy.
One substantive critique or endorsement. Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. One substantive critique or endorsement.
Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement] -- Score: [N/10]
PRACTITIONER: [critique or endorsement] -- Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT.
If finding reclassified: state reason; add SCAFFOLD AUDIT entry with all 4 conflict fields.
If Future Work amended: confirm at least one FW row still has Status: B-NN ANCHOR.
After amendments: Skeptic re-issues Post-Review verdict for any previously flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-02: Structural-Visibility-Table

**Axis:** Output format -- the paper opens with a PAPER NON-NEGOTIABLES block before the
Abstract (C-20); the Future Work table adds a Status column where blank = structural failure
(C-18). Both enforce compliance through structure visible without reading prose.
**Hypothesis:** R3 V-02 demonstrated that a FUTURE WORK TABLE with a B-NN Anchor column makes
C-16 machine-verifiable. The R4 insight is that C-18 requires a dedicated Status column
(B-NN ANCHOR / NET-NEW) that makes the classification explicit per row, not inferrable from
anchor presence alone. A blank Status cell is visible without reading the anchor cell value.
C-20 is a paper-level requirement: the document must declare its structural non-negotiables
before any section content. Adding a PAPER NON-NEGOTIABLES block as the first element of the
paper output template enforces C-20 without adding a new lifecycle phase -- it is a required
section in the paper output, not an additional prompt step.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review),
Skeptic (structural post-review audit).

**Three non-negotiable rules (prompt scope):**
1. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13).
2. Finding classifications committed in a table before any finding prose is written (C-14).
3. Future Work section uses a table with B-NN Anchor and Status columns; at least one row
   carries Status: B-NN ANCHOR naming a gap from the Status Quo section (C-16, C-18).

**Paper-level requirement:** The paper output opens with a PAPER NON-NEGOTIABLES block
before the Abstract. This block is not a section -- it is a pre-section compliance
declaration. A reviewer can check it without reading any section content (C-20).

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic:
- hypothesis, analysis, interview, websearch, synthesize

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path] or [not found]
```

If no hypothesis found: stop. Do not proceed without a stated hypothesis.

---

### Phase 2: Prior Belief Table

Before writing any paper section, build the prior belief table.
This becomes the Status Quo section.

```
PRIOR BELIEF TABLE:
| ID   | Prior belief (concrete assumption before investigation) | Source of assumption |
|------|--------------------------------------------------------|----------------------|
| B-01 | [concrete prior belief]                                | [intuition / paper / convention] |
| B-02 | [concrete prior belief]                                | [source] |
| B-03 | [optional]                                             | [source] |

Default action (without this investigation): [what team would have done]
Motivated by: [gap or tension H-01 addresses]
```

Minimum 2 rows. Not background prose.

---

### Phase 3: Evidence

Lead Author writes Evidence before Abstract, before Findings.

`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims:
`UNCITABLE: [claim text] -- no artifact source, will appear in Limitations`

```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without anchor (must be 0 to proceed): [N]
Uncitable claims for Limitations: [N]
Status: [PASS -- proceed to Phase 4] or [BLOCKED -- [N] uncited claims remain]
```

Do not proceed to Phase 4 until Status: PASS.

---

### Phase 4: Finding Classification Table (Before Findings Prose)

With Evidence complete and CITATION AUDIT passed. Commit the finding classification table
before writing any finding prose. To reclassify after prose: add a RECLASSIFICATION ROW.
Reclassification without a reason row fails C-14.

```
FINDING CLASSIFICATION TABLE:
| F-ID | Evidence basis (E-IDs) | Classification            | Baseline Anchor |
|------|------------------------|---------------------------|-----------------|
| F-01 | [E-NN, E-NN]          | BASELINE MATCH            | B-NN            |
| F-02 | [E-NN]                | NEW SIGNAL                | B-NONE          |
| F-03 | [E-NN, E-NN]          | BASELINE MATCH            | B-NN            |
```

RECLASSIFICATION ROW (if needed after prose):
```
RECLASSIFICATION: F-NN
  Original: [BASELINE MATCH / NEW SIGNAL -- B-XX]
  Revised: [new form]
  Reason: [what evidence or prose writing revealed]
```

NEW SIGNAL count: [N] of [N].

---

### Phase 5: Hypothesis Verdict

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs]
Full verdict sentence: "[Committed -- no hedging accepted]"
```

Not accepted: "The evidence is mixed." / "The evidence suggests..." / "Further work is needed."

---

### Phase 6: Write the Paper

**Paper output starts with this block -- before the Abstract, before any section heading:**

```
PAPER NON-NEGOTIABLES
This paper satisfies the following requirements. Verify without reading sections:

1. All 8 sections present: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings,
   Principles, Limitations, Future Work.
2. CITATION AUDIT block in Evidence section with Status: PASS and zero uncited claims.
3. FINDING CLASSIFICATION TABLE present with Classification and Baseline Anchor columns.
   Any reclassification after prose has a RECLASSIFICATION ROW with a stated reason.
4. HYPOTHESIS VERDICT block at start of Findings with explicit committed verdict sentence.
5. FUTURE WORK TABLE present with B-NN Anchor and Status columns; at least one row carries
   Status: B-NN ANCHOR naming a gap from the Status Quo section.
6. Skeptic Post-Review APPROVED verdict present before Domain Expert and Practitioner.
```

**1. Abstract** (<200 words)
State: (a) question, (b) method, (c) key finding, (d) practical implication. Not structure.
Written after verdict is known.

**2. Status Quo** (paste Phase 2 Prior Belief Table, formatted as prose with B-IDs)

**3. Hypothesis**
`H-01: [hypothesis text] (source: [file path])`
If amended during investigation: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Why evidence was gathered this way.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (all E-[N] items from Phase 3)

```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored. [N] claims in Limitations.
```

**6. Findings**

Hypothesis verdict first (required). Then findings using Phase 4 classification table:
```
F-01 [BASELINE MATCH -- confirms B-01]:
[conclusion -- "what does this mean?"]

F-02 [NEW SIGNAL -- challenges B-02]:
[conclusion]
```

If reclassification from table: RECLASSIFICATION ROW required.
CONTRIBUTION or INERTIA FLAG as appropriate.

**7. Principles**
Minimum 2 numbered rules. Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites finding: `P-01 [from F-02]: ...`
Tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`

**8. Limitations**
What the investigation did not cover. Uncitable claims from Phase 3.

**9. Future Work**

Required format -- table with three columns:

| Item  | Question                                      | B-NN Anchor            | Status      |
|-------|-----------------------------------------------|------------------------|-------------|
| FW-01 | [Investigable question, specific enough start]| [B-NN from Status Quo] | B-NN ANCHOR |
| FW-02 | [Additional question]                         | --                     | NET-NEW     |

Column rules:
- Status must be "B-NN ANCHOR" or "NET-NEW" -- no blank Status cells.
- At least one row must carry Status: B-NN ANCHOR.
- A blank Status cell is a structural failure visible without reading the question text.

---

### Phase 7: Skeptic Post-Review (Before Panel)

After paper is fully drafted.

```
SKEPTIC POST-REVIEW:
SQ-01. PAPER NON-NEGOTIABLES block present before Abstract:
  [PASS -- block present as first visible element with 6 verifiable items]
  or [FLAG -- block absent, positioned after Abstract, or items are generic statements]

SQ-02. CITATION AUDIT in Evidence, Status: PASS:
  [PASS -- present, zero uncited claims]
  or [FLAG -- audit missing or uncited claims]

SQ-03. Finding Classification Table committed before finding prose:
  [PASS -- table present; reclassifications have RECLASSIFICATION ROW with reason]
  or [FLAG -- table absent or reclassification without reason]

SQ-04. Hypothesis verdict explicit committed sentence:
  [PASS -- quotable sentence with evidence basis]
  or [FLAG -- evasive, hedged, or uncited]

SQ-05. Future Work table with Status column, at least one B-NN ANCHOR row:
  [PASS -- table present; no blank Status cells; at least one B-NN ANCHOR row]
  or [FLAG -- table absent, blank Status cells, or zero B-NN ANCHOR rows]

Final verdict: [APPROVED] or [FLAG: items SQ-NN failed -- amend before output]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict. Panel does not begin until APPROVED.

---

### Phase 8: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy, Findings correctness, Status Quo for strawmanning.
Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement] -- Score: [N/10]
PRACTITIONER: [critique or endorsement] -- Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT.
If finding reclassified: add RECLASSIFICATION ROW with reason.
If Future Work amended: confirm at least one row retains Status: B-NN ANCHOR.
After amendments: Skeptic re-issues verdict for flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-03: Scaffold-Audit-Section

**Axis:** Lifecycle emphasis -- the SCAFFOLD CONFLICT mechanism is promoted from an inline
annotation to a required Findings subsection: SCAFFOLD AUDIT. Every finding appears in the
audit: either CONFIRMED (no change) or CONFLICT (4 required fields). The subsection must
appear before any finding prose. A paper where SCAFFOLD AUDIT is absent fails C-14 and C-19
without reading further.
**Hypothesis:** C-19 fails when SCAFFOLD CONFLICT entries are optional -- the author can
silently reclassify by simply not writing a conflict entry, and a reviewer must compare the
scaffold table against the findings prose to detect the omission. When SCAFFOLD AUDIT is a
required subsection with a slot for every finding, the audit is compulsory by structure:
every finding slot exists regardless of whether there was a conflict. A missing slot is
visible. The four required conflict fields (finding ID, original, revised, reason) are
named elements in the slot, not free-form prose. A slot with only 3 of 4 fields is
structurally incomplete in a way that a missing sentence in prose never is.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review),
Skeptic (structural post-review audit).

**Three non-negotiable rules:**
1. Status Quo section with concrete B-NN prior beliefs written before any paper section (C-12).
2. CITATION AUDIT block must show Status: PASS before findings are written (C-13).
3. Novelty classification scaffold committed from artifact summaries before Evidence is
   written; any post-evidence reclassification requires a SCAFFOLD AUDIT entry with
   4 required fields (C-14, C-19).

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic.

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path] or [not found]
```

If hypothesis not found: stop.

---

### Phase 2: Prior Belief Inventory + Pre-Evidence Scaffold

**Output A: Prior Belief Inventory** (becomes Status Quo section)

```
PRIOR BELIEF INVENTORY:
B-01: [Concrete prior belief] -- [why this was believed]
B-02: [Concrete prior belief] -- [why this was believed]
B-03: [Optional] -- [why]

Gap motivating investigation: [specific tension H-01 targets]
Default action without investigation: [what team would have done]
```

Minimum 2 beliefs. Each must be confirmable or refutable.

**Output B: Pre-Evidence Novelty Classification Scaffold**

From artifact summaries loaded in Phase 1 only -- before writing any evidence claim:

```
PRE-EVIDENCE NOVELTY CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH -- pre-committed to confirm B-XX]
      or [NEW SIGNAL -- pre-committed to challenge B-XX / B-NONE]
      Artifact basis (file names and section IDs only -- no evidence claims yet): [refs]

F-02: [BASELINE MATCH / NEW SIGNAL]
      Artifact basis: [refs]

F-03: [BASELINE MATCH / NEW SIGNAL]
      Artifact basis: [refs]

Pre-committed NEW SIGNAL count: [N] of [N].
Note: classifications committed from artifact summaries only. Evidence writing follows.
Any reclassification after Evidence requires a SCAFFOLD AUDIT entry with 4 fields.
Silent reclassification is not allowed.
```

---

### Phase 3: Evidence

Lead Author writes evidence claims with citations:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims:
`UNCITABLE: [claim] -- no artifact source, routed to Limitations`

```
CITATION AUDIT
Evidence items total: [N]
Items with anchor: [N]
Items without anchor (must be 0): [N]
Uncitable claims in Limitations: [N]
Status: [PASS -- proceed to Phase 4] or [BLOCKED -- [N] uncited claims, must resolve]
```

Do not continue until Status: PASS.

---

### Phase 4: Hypothesis Verdict

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs]
Full verdict sentence: "[Committed -- no hedging accepted]"
```

Not accepted: "The evidence suggests..." / "Further investigation is needed."

---

### Phase 5: Write the Paper

**1. Abstract** (<200 words)
State: (a) question, (b) method, (c) key finding, (d) practical implication. Not structure.
Written after verdict is known.

**2. Status Quo** (paste Phase 2 Output A verbatim, formatted with B-IDs)

**3. Hypothesis**
`H-01: [text] (source: [file path])`
If amended: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Evidence collection rationale.
Include: "Novelty classification scaffold committed from artifact summaries before Evidence
was written. Any classification that changed after Evidence was gathered is documented in the
SCAFFOLD AUDIT in Section 6."
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (all E-[N] items from Phase 3)

```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored. [N] claims in Limitations.
```

**6. Findings**

Hypothesis verdict first (required).

**SCAFFOLD AUDIT** (required subsection -- must appear before any finding prose):

One slot per finding from Phase 2 Output B. Each slot must be filled.
No finding may be silently reclassified -- either CONFIRMED or CONFLICT entry required.

```
SCAFFOLD AUDIT:

F-01 -- Pre-committed: BASELINE MATCH -- B-01
  Status: CONFIRMED -- evidence supports pre-committed classification.
  [or]
  Status: CONFLICT
    Finding ID: F-01
    Original classification: BASELINE MATCH -- confirms B-01
    Revised classification: NEW SIGNAL -- challenges B-01
    Reason: [what evidence showed that contradicted the pre-committed tag]

F-02 -- Pre-committed: NEW SIGNAL -- B-NONE
  Status: CONFIRMED
  [or]
  Status: CONFLICT
    Finding ID: F-02
    Original classification: [original]
    Revised classification: [revised]
    Reason: [reason]

[Slot for each finding in Phase 2 Output B]

ATTESTATION: [N] findings -- [N] confirmed, [N] reclassified (each has CONFLICT entry above).
```

If all confirmed: "SCAFFOLD AUDIT: [N] findings -- all classifications confirmed. No changes."

Finding prose (uses final classifications from SCAFFOLD AUDIT):
```
F-01 [BASELINE MATCH -- confirms B-01]:
[conclusion -- "what does this mean?"]

F-02 [NEW SIGNAL -- challenges B-02]:
[conclusion]
```

CONTRIBUTION or INERTIA FLAG as appropriate.

**7. Principles**
Minimum 2 numbered rules. Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites finding: `P-01 [from F-02]: ...`
Tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`

**8. Limitations**
What the investigation did not cover. Uncitable claims from Phase 3.

**9. Future Work**
Minimum 2 specific investigable questions.
Required: at least one item explicitly names a B-NN gap from the Status Quo section.
```
FW-01 [addresses B-NN gap]:
  Question: [investigable]
  B-NN anchor: [B-ID from Status Quo] -- [gap or assumption to investigate]
  Method: [specific approach]

FW-02 [extends investigation]:
  Question: [investigable]
  Anchor: NET-NEW -- [not tied to a Status Quo gap]
```

---

### Phase 6: Skeptic Post-Review (Before Panel)

After paper is fully drafted.

```
SKEPTIC POST-REVIEW:
1. SCAFFOLD AUDIT present in Findings before finding prose:
   [PASS -- subsection present; every pre-committed finding has a CONFIRMED or CONFLICT slot;
   all CONFLICT slots have all 4 required fields: finding ID, original, revised, reason]
   or [FLAG -- subsection absent / finding slot missing / CONFLICT slot missing a field]

2. Citation traceability:
   [PASS -- EVIDENCE COMPLETE marker with zero uncited claims]
   or [FLAG -- marker missing or uncited claims in Evidence]

3. Hypothesis verdict explicit:
   [PASS -- committed sentence with evidence basis]
   or [FLAG -- evasive, hedged, or no evidence basis]

4. Synthesis quality:
   [PASS -- findings answer "what does this mean?"]
   or [FLAG -- N findings restate evidence rather than draw conclusions]

5. Future Work has B-NN anchor:
   [PASS -- at least one FW item names a B-NN gap from Status Quo]
   or [FLAG -- no FW item references a B-ID from Status Quo]

Final verdict: [APPROVED] or [FLAG: items N failed -- amend before output]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict. Panel does not begin until APPROVED.

---

### Phase 7: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy, Findings correctness, Status Quo accuracy. Assesses whether
SCAFFOLD AUDIT conflicts were reasonably resolved.
Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement, including scaffold conflict assessment] -- Score: [N/10]
PRACTITIONER: [critique or endorsement] -- Score: [N/10]
```

---

### Phase 8: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If finding reclassified: add CONFLICT slot in SCAFFOLD AUDIT with all 4 fields.
If Evidence amended: re-run CITATION AUDIT.
If Future Work amended: confirm at least one FW item names a B-NN gap.
After amendments: Skeptic re-issues verdict for flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-04: Document-Header-Declaration

**Axis:** Combined -- 8-rule forward declaration at prompt header (C-17 and C-20 added as
Rules 7-8) + the paper output opens with a PAPER STRUCTURAL COMMITMENTS block that restates
the same rules in verifiable document form. The prompt header declares intent; the paper
header declares compliance. They are the same list, two uses -- header-level symmetry.
**Hypothesis:** V-04 R3 established that 6 rules at the prompt header -- covering C-11 through
C-16 -- creates a cross-phase compliance checklist that survives long sessions. R4 adds
C-17 (checklist symmetry) and C-20 (paper-level non-negotiables) as Rules 7 and 8.
C-20 is unusual: it targets the paper document, not the prompt. The V-04 R4 bet is that
the same mechanism that makes prompt-level rules effective also works at the paper level --
if the paper opens with a block that a reviewer can scan without reading any section, it
front-loads verification for any reader, not just the author. The 8 rules in the prompt and
the PAPER STRUCTURAL COMMITMENTS block are the same list: the document is a self-auditing
artifact from its first visible line.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight author + post-review), Lead Author (paper writer),
Domain Expert (substantive review), Practitioner (applicability review).

**Eight non-negotiable rules (prompt scope -- each maps to exactly one phase):**

1. Status Quo section with at least 2 concrete B-NN prior beliefs -- written by Skeptic
   before Lead Author writes any section [Phase 2 -> C-12]
2. CITATION AUDIT block with zero uncited claims before Findings begins [Phase 3 -> C-13]
3. Every finding carries BASELINE MATCH or NEW SIGNAL tag -- committed in scaffold
   before finding prose [Phase 4 -> C-11, C-14]
4. Novelty scaffold committed before finding prose -- in a named block after citation audit
   [Phase 4 -> C-14]
5. Skeptic Post-Review with 5+ item structural checklist and APPROVED/FLAG verdict runs
   after paper draft, before panel review [Phase 7 -> C-15]
6. At least one Future Work item names a specific B-NN gap from the Status Quo section
   [Phase 6 paragraph 9 -> C-16]
7. Skeptic Post-Review checklist items each name a pre-flight antecedent by PF-NN ID;
   at least 3 items must trace to a Phase 2 commitment [Phase 7 -> C-17]
8. Paper output opens with a PAPER STRUCTURAL COMMITMENTS block before the Abstract,
   listing Rules 1-8 in verifiable form [Phase 6 -> C-20]

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic.

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path] or [not found]
```

If hypothesis not found: stop.

---

### Phase 2: Skeptic Pre-Flight

Two outputs. Skeptic runs before Lead Author writes anything.

**Output A: Pre-Flight Checklist with PF-NN IDs** (Phase 7 will cite these by ID)

```
SKEPTIC PRE-FLIGHT:
PF-01. Hypothesis verdict -- explicit committed sentence in Findings.
PF-02. Citation traceability -- CITATION AUDIT Status: PASS.
PF-03. Novelty scaffold -- all findings tagged before prose.
PF-04. Synthesis quality -- findings answer "what does this mean?".
PF-05. Principles actionability -- numbered rules with finding citations.

Prediction: [most likely structural failure -- one specific sentence]
Watch point: [section most at risk, with reason]
```

**Output B: Status Quo section (final text -- inserted verbatim into paper)**

```
## Status Quo

Before this investigation began, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief 1]
- [B-02: Concrete prior belief 2]
- [B-03: Optional]

Motivated by: [gap H-01 targets]
Default action without investigation: [what team would have done]
```

Minimum 2 beliefs. Not background prose. Lead Author reads both before writing.

---

### Phase 3: Evidence

Lead Author writes Evidence before Abstract, before Findings.
Rule 2 requires Status: PASS before Phase 4.

`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims:
`UNCITABLE: [claim] -- no artifact source, moved to Limitations`

```
CITATION AUDIT
Evidence items total: [N]
Items with anchor: [N]
Items without anchor (must be 0): [N]
Uncitable claims in Limitations: [N]
Status: [PASS -- Findings unlocked] or [BLOCKED -- resolve before proceeding]
```

Rule 2 satisfied when Status: PASS.

---

### Phase 4: Novelty Classification Scaffold

With citation audit passed. Commit before writing finding prose.
Rules 3 and 4 require this block named and sequenced before Phase 6 finding prose.

```
NOVELTY CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH -- confirms B-XX] or [NEW SIGNAL -- challenges B-XX / B-NONE]
F-02: [BASELINE MATCH / NEW SIGNAL]
F-03: [BASELINE MATCH / NEW SIGNAL]

NEW SIGNAL count: [N] of [N].
Rule 3 satisfied: all findings tagged.
Rule 4 satisfied: scaffold committed before finding prose.
```

If zero NEW SIGNAL:
```
SCAFFOLD FLAG: All BASELINE MATCH. INERTIA FLAG will appear in Findings.
```

---

### Phase 5: Hypothesis Verdict

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[Committed -- Rule 1 requires this verbatim in Findings]"
```

---

### Phase 6: Write the Paper

**Rule 8: Paper opens with PAPER STRUCTURAL COMMITMENTS block as first visible element.**

```
PAPER STRUCTURAL COMMITMENTS
Verify without reading section content:

1. Status Quo section present with at least 2 labeled prior beliefs (B-01, B-02...).
2. Evidence section contains CITATION AUDIT block with Status: PASS and zero uncited claims.
3. Findings section contains novelty tags on every finding (BASELINE MATCH / NEW SIGNAL).
4. Novelty scaffold committed in a named block before finding prose -- see Phase 4.
5. Skeptic Post-Review appears after paper draft, before Domain Expert and Practitioner;
   APPROVED verdict present.
6. Future Work contains at least one item naming a B-NN gap from the Status Quo section.
7. Skeptic Post-Review checklist items each cite a PF-NN antecedent from pre-flight.
8. This block appears before the Abstract as the first visible element of the document.

Each commitment is verifiable by scanning structure. A reviewer may reject if any is absent.
```

**1. Abstract** (<200 words)
State: (a) question, (b) method, (c) key finding, (d) practical implication. Not structure.

**2. Status Quo** (paste Phase 2 Output B verbatim)

**3. Hypothesis**
`H-01: [text] (source: [file path])`

**4. Method**
Prove skills run. Artifacts produced. Evidence collection rationale.
Cold-start readable: define terms on first use.

**5. Evidence** (all E-[N] items from Phase 3)

```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored.
```

**6. Findings**

Hypothesis verdict (required -- paste Phase 5 Full verdict sentence verbatim):
```
HYPOTHESIS VERDICT
[paste Phase 5 block]
```

Finding prose using scaffold from Phase 4:
```
F-01 [BASELINE MATCH -- confirms B-01]:
[conclusion -- "what does this mean?"]

F-02 [NEW SIGNAL -- challenges B-02]:
[conclusion]
```

If reclassification from scaffold: state reason explicitly.
CONTRIBUTION or INERTIA FLAG as appropriate.

**7. Principles**
Minimum 2 numbered rules. Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites finding: `P-01 [from F-02]: ...`
Tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`

**8. Limitations**
What the investigation did not cover. Uncitable claims from Phase 3.

**9. Future Work** (Rule 6 requires at least one B-NN anchor)

```
FW-01 [closes B-NN gap -- Rule 6]:
  Question: [specific enough to start]
  B-NN anchor: [B-ID from Status Quo] -- [assumption to investigate]
  Method: [specific approach]

FW-02 [extends investigation]:
  Question: [specific]
  Anchor: NET-NEW
```

---

### Phase 7: Skeptic Post-Review (Before Panel)

Rules 5, 7 require this phase before Domain Expert and Practitioner.
Rule 7 requires each item to cite a PF-NN antecedent from Phase 2 Output A.

```
SKEPTIC POST-REVIEW:
Item 1 [Pre-flight antecedent: PF-01 -- Hypothesis verdict]:
  [PASS -- Commitment #1 in PAPER STRUCTURAL COMMITMENTS satisfied; verdict sentence present]
  or [FLAG -- sentence missing or hedged]

Item 2 [Pre-flight antecedent: PF-02 -- Citation traceability]:
  [PASS -- Commitment #2 satisfied; CITATION AUDIT Status: PASS]
  or [FLAG -- audit absent or uncited claims]

Item 3 [Pre-flight antecedent: PF-03 -- Novelty scaffold]:
  [PASS -- Commitments #3 and #4 satisfied; scaffold named in Phase 4; tags on findings]
  or [FLAG -- tags absent or scaffold produced after prose]

Item 4 [Pre-flight antecedent: PF-04 -- Synthesis quality]:
  [PASS -- findings answer "what does this mean?"]
  or [FLAG -- N findings restate evidence]

Item 5 [Pre-flight antecedent: PF-05 -- Principles actionability]:
  [PASS -- numbered rules with finding citations]
  or [FLAG -- N principles vague or uncited]

Rule 7 trace check: 5 items -- all 5 cite PF-NN antecedents from Phase 2 Output A.
C-17 minimum (3 of 5 traceable): [N of 5 traceable].

PAPER STRUCTURAL COMMITMENTS check (Rule 8):
  [PASS -- block present before Abstract; 8 verifiable items; no generic statements]
  or [FLAG -- block absent, positioned after Abstract, or contains generic statements]

Pre-flight prediction outcome: [CONFIRMED / RESOLVED / STILL PRESENT -- location]

Final verdict: [APPROVED] or [FLAG: items N failed -- amend before output]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict. Panel does not begin until APPROVED.

---

### Phase 8: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy, Findings correctness, Status Quo accuracy.
Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement] -- Score: [N/10]
PRACTITIONER: [critique or endorsement] -- Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT. Update PAPER STRUCTURAL COMMITMENTS #2 if needed.
If finding reclassified: state reason. Update scaffold and PAPER STRUCTURAL COMMITMENTS #3.
If Future Work amended: confirm B-NN anchor still present. Update PAPER STRUCTURAL COMMITMENTS #6.
After amendments: Skeptic re-issues verdict for flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-05: Quad-Criterion-Distribution

**Axis:** Combined -- each of C-17, C-18, C-19, C-20 gets exactly one named structural owner,
extending V-05 R3's single-job role isolation to all four R4 criteria. Pre-Skeptic writes
the paper NON-NEGOTIABLES block (C-20). Mid-Skeptic produces the scaffold with a provisional
classification column and flags conflicts (C-19). Post-Skeptic traces each checklist item
to its pre-flight antecedent by ID (C-17). Lead Author owns FW table format with Status
column (C-18). No criterion is owned by a role that has competing responsibilities.
**Hypothesis:** R3 V-05 demonstrated that single-job role isolation prevents criteria from
being abbreviated or collapsed when sessions run long. The R4 insight: C-17, C-18, C-19,
and C-20 each represent a different structural surface. Distributing one criterion per role
means no single role carries competing surface responsibilities. The Pre-Skeptic produces
the paper header block before knowing what the paper will say -- the declaration precedes
the work, which is the structural requirement of C-20. The Post-Skeptic's only new job is
the antecedent trace per checklist item -- no other role can quietly drop it.

```
You are running /prove:publish for Signal.

Stock roles:
- Pre-Skeptic: paper NON-NEGOTIABLES block (C-20) + Status Quo (C-12) + risk naming
- Lead Author: writes paper content; owns Future Work table format with Status column (C-18)
- Mid-Skeptic: citation audit (C-13) + novelty scaffold with provisional column +
  conflict detection (C-14, C-19)
- Post-Skeptic: structural checklist with PF-NN antecedent trace per item (C-15, C-17)
- Domain Expert: substantive review of evidence and findings
- Practitioner: applicability review of principles

Each role has exactly one criterion-responsibility per R4 criterion. No R4 criterion
is owned by a role that has other R4 responsibilities.

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic.

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path] or [not found]
```

If hypothesis not found: stop.

---

### Phase 2: Pre-Skeptic

Pre-Skeptic runs before Lead Author writes anything. Three outputs.

**Output A: Paper NON-NEGOTIABLES Block** (C-20 -- written now, inserted verbatim as first
visible element of the paper in Phase 6)

```
PAPER NON-NEGOTIABLES
[Pre-Skeptic writes this block before any paper section exists. Lead Author inserts it
verbatim as the paper's first element in Phase 6.]

Verify without reading section content:

N-01. CITATION AUDIT block in Evidence -- Status: PASS, zero uncited claims.
N-02. SCAFFOLD AUDIT in Findings -- every finding confirmed or CONFLICT-documented (4 fields).
N-03. HYPOTHESIS VERDICT block at start of Findings -- explicit committed sentence, E-IDs.
N-04. Future Work uses a table with B-NN Anchor and Status columns; at least one row
      carries Status: B-NN ANCHOR naming a gap from the Status Quo section.
N-05. Post-Skeptic APPROVED verdict present; checklist items each cite a PF-NN antecedent.

Pre-Skeptic declares these before any investigation is written. These are the Post-Skeptic's
verification items. No new criteria will be introduced at post-review.
```

**Output B: Pre-Flight Checklist with PF-NN IDs** (Post-Skeptic cites these in Phase 7)

```
PRE-SKEPTIC PRE-FLIGHT:
PF-01. Hypothesis verdict -- explicit committed sentence.
PF-02. Citation traceability -- CITATION AUDIT Status: PASS.
PF-03. Novelty scaffold -- Mid-Skeptic produces; Lead Author uses.
PF-04. Synthesis quality -- findings answer "what does this mean?".
PF-05. Principles actionability -- numbered rules with finding citations.

Prediction: [most likely structural failure -- one specific sentence]
Watch point: [section most at risk, with reason]
```

**Output C: Status Quo section (final text -- inserted verbatim into paper)**

```
## Status Quo

Before this investigation began, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief]
- [B-02: Concrete prior belief]
- [B-03: Optional]

Gap motivating investigation: [gap H-01 targets]
Default action without investigation: [what team would have done]
```

Minimum 2 beliefs. Not background prose. Lead Author reads all three outputs before writing.

---

### Phase 3: Lead Author -- Evidence

Lead Author writes evidence claims before Abstract, before Findings.

`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims:
`UNCITABLE: [claim] -- no artifact source, will appear in Limitations`

Evidence writing is complete when all claims are entered. Mid-Skeptic audits next.

---

### Phase 4: Mid-Skeptic -- Citation Audit + Scaffold (C-13, C-14, C-19)

Two tasks. Mid-Skeptic does not write finding prose.

**Task A: Citation Audit (C-13)**

```
CITATION AUDIT (Mid-Skeptic):
E-01: [CITED -- source: file.md, section] or [UNCITED -- move to Limitations]
E-02: [CITED] or [UNCITED]
...
E-[N]: [CITED] or [UNCITED]

Total: [N] | Cited: [N] | Uncited (must be 0): [N]
Status: [PASS -- Task B unlocked] or [BLOCKED -- [N] items need citations]
```

If BLOCKED: specify which items. Lead Author fixes. Mid-Skeptic re-runs Task A.

**Task B: Novelty Scaffold with Provisional Classification Column (C-14, C-19)**

After Task A PASS. Classifications committed from evidence items only, before any finding prose.

```
MID-SKEPTIC NOVELTY SCAFFOLD:
| F-ID | Evidence basis (E-IDs) | Provisional classification | Baseline anchor |
|------|------------------------|---------------------------|-----------------|
| F-01 | [E-NN, E-NN]          | BASELINE MATCH -- B-01    | B-01            |
| F-02 | [E-NN]                | NEW SIGNAL -- B-NONE      | B-NONE          |
| F-03 | [E-NN, E-NN]          | BASELINE MATCH -- B-02    | B-02            |

Basis: evidence items above only. No finding prose exists.
These classifications are provisional. Lead Author uses them in Phase 6.
If evidence gathered DURING WRITING contradicts a provisional classification:
Lead Author must file a SCAFFOLD CONFLICT entry in SCAFFOLD AUDIT (Phase 6).
Provisional classifications may not be silently changed.

NEW SIGNAL count: [N] of [N].
```

---

### Phase 5: Hypothesis Verdict

Lead Author states verdict after Mid-Skeptic scaffold is complete.

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[Committed -- N-03 requires this verbatim in Findings]"
```

Not accepted: "The evidence is mixed." / "The evidence suggests..." / "Further work is needed."

---

### Phase 6: Lead Author -- Write the Paper

Lead Author inserts all Pre-Skeptic outputs verbatim where specified.

**Paper opens with Phase 2 Output A (NON-NEGOTIABLES block) -- first visible element:**

[Insert Phase 2 Output A verbatim]

**1. Abstract** (<200 words)
State: (a) question, (b) method, (c) key finding, (d) practical implication. Not structure.

**2. Status Quo** (insert Phase 2 Output C verbatim)

**3. Hypothesis**
`H-01: [text] (source: [file path])`

**4. Method**
Prove skills run. Artifacts produced. Evidence collection rationale.
Include: "Evidence was audited by Mid-Skeptic (Task A). Novelty scaffold committed by
Mid-Skeptic (Task B) before Findings were written. Any classification change from the
provisional scaffold is documented in SCAFFOLD AUDIT in Section 6."
Cold-start readable: define terms on first use.

**5. Evidence** (all E-[N] items from Phase 3, as verified in Mid-Skeptic Task A)

```
EVIDENCE COMPLETE: Mid-Skeptic citation audit passed. [N] items anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**

Insert Phase 5 Hypothesis verdict first.

**SCAFFOLD AUDIT** (required, before finding prose -- satisfies N-02):

For each finding in the Mid-Skeptic scaffold:
```
SCAFFOLD AUDIT:
F-01 -- Provisional: BASELINE MATCH -- B-01 -- Status: CONFIRMED
F-02 -- Provisional: NEW SIGNAL -- B-NONE -- Status: CONFIRMED
F-03 -- Provisional: BASELINE MATCH -- B-02 -- Status: CONFLICT
  SCAFFOLD CONFLICT F-03:
    Finding ID: F-03
    Original classification: BASELINE MATCH -- confirms B-02
    Revised classification: NEW SIGNAL -- challenges B-02
    Reason: [what evidence showed during writing that contradicted Mid-Skeptic provisional tag]

ATTESTATION: [N] findings -- [N] confirmed, [N] reclassified with CONFLICT entries.
```

Finding prose using final classifications from SCAFFOLD AUDIT:
```
F-01 [BASELINE MATCH -- confirms B-01]:
[conclusion -- "what does this mean?"]

F-02 [NEW SIGNAL -- challenges B-02]:
[conclusion]
```

CONTRIBUTION or INERTIA FLAG as appropriate.

**7. Principles**
Minimum 2 numbered rules. Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites finding: `P-01 [from F-02]: ...`
Tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`

**8. Limitations**
What the investigation did not cover. Uncitable claims from Phase 3.

**9. Future Work** (Lead Author owns C-18 -- table with Status column required)

N-04 requires a table with B-NN Anchor and Status columns.
A blank Status cell is a structural failure visible without reading the content.

| Item  | Question                                      | B-NN Anchor              | Status      |
|-------|-----------------------------------------------|--------------------------|-------------|
| FW-01 | [specific investigable question]              | [B-ID from Status Quo]   | B-NN ANCHOR |
| FW-02 | [additional question]                         | --                       | NET-NEW     |

Rules:
- Status must be "B-NN ANCHOR" or "NET-NEW" -- blank = structural failure.
- At least one row must carry Status: B-NN ANCHOR.
- NET-NEW rows must be explicitly marked.

---

### Phase 7: Post-Skeptic -- Structural Checklist with Antecedent Trace (C-15, C-17)

Post-Skeptic's job: structural checklist audit + PF-NN antecedent trace. Nothing else.
Each item names the PF-NN antecedent it verifies. Symmetry is declared, not assumed.

```
POST-SKEPTIC STRUCTURAL AUDIT:

Item 1 [Pre-flight antecedent: PF-01 -- Hypothesis verdict]:
  [PASS -- N-03 satisfied; committed sentence verbatim in Findings]
  or [FLAG -- absent or hedged]

Item 2 [Pre-flight antecedent: PF-02 -- Citation traceability]:
  [PASS -- N-01 satisfied; EVIDENCE COMPLETE with Mid-Skeptic audit PASS]
  or [FLAG -- marker absent or uncited items in Evidence]

Item 3 [Pre-flight antecedent: PF-03 -- Novelty scaffold]:
  [PASS -- Mid-Skeptic scaffold present; SCAFFOLD AUDIT in Findings; N-02 satisfied;
  all CONFLICT entries have 4 required fields]
  or [FLAG -- scaffold absent, SCAFFOLD AUDIT missing, or CONFLICT entry incomplete]

Item 4 [Pre-flight antecedent: PF-04 -- Synthesis quality]:
  [PASS -- findings answer "what does this mean?"]
  or [FLAG -- N findings restate evidence]

Item 5 [Pre-flight antecedent: PF-05 -- Principles actionability]:
  [PASS -- all principles numbered rules with finding citations]
  or [FLAG -- N principles vague or uncited]

Antecedent trace check:
  All 5 items cite PF-NN antecedents from Phase 2 Output B.
  C-17 minimum (3 of 5 traceable): [N of 5 traceable].

NON-NEGOTIABLES block check (Phase 2 Output A):
  N-01 CITATION AUDIT: [PASS / FLAG]
  N-02 SCAFFOLD AUDIT: [PASS / FLAG]
  N-03 HYPOTHESIS VERDICT: [PASS / FLAG]
  N-04 Future Work table with Status column, at least one B-NN ANCHOR: [PASS / FLAG]
  N-05 Post-Skeptic APPROVED: [pending -- verdict below]

Pre-flight prediction outcome: [CONFIRMED / RESOLVED / STILL PRESENT -- location]

Final verdict: [APPROVED] or [FLAG: items N failed -- amend before output]
```

If FLAG: Lead Author amends. Post-Skeptic re-issues verdict. Panel does not begin until APPROVED.

---

### Phase 8: Panel Review

Runs after Post-Skeptic APPROVED.

**Domain Expert:**
Reviews Evidence accuracy, Findings correctness, Status Quo accuracy. Assesses whether
SCAFFOLD CONFLICT entries were reasonably resolved.
Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement, including scaffold conflict assessment] -- Score: [N/10]
PRACTITIONER: [critique or endorsement] -- Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Post-Skeptic]
```

If Evidence amended: Mid-Skeptic re-runs Task A for affected items. Update EVIDENCE COMPLETE.
If finding reclassified: Lead Author adds SCAFFOLD CONFLICT entry in SCAFFOLD AUDIT with all 4 fields.
If Future Work amended: confirm at least one row retains Status: B-NN ANCHOR.
After amendments: Post-Skeptic re-issues verdict for flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```
