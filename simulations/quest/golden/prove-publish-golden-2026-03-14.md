Written to `simulations/quest/golden/prove-publish-golden-2026-03-14.md`.

**prove-publish quest complete.**

- **Winning variation:** V-01: Checklist-Symmetry-Chain (114/114, tied with V-05)
- **Simplified prompt:** 1,349 words (20% reduction, all 5 essential preserved)
- **Golden document:** frontmatter + verbatim prompt body + 5 distinguishing patterns + v5 rubric summary

The five patterns that made it golden:
1. **PF-NN ID system** -- symmetry becomes a field check, not a reader comparison
2. **SCAFFOLD AUDIT subsection** with per-finding slots -- missing slot is a blank, not an absent sentence
3. **NON-NEGOTIABLES BLOCK** in paper before Abstract -- paper-level, not prompt-level enforcement
4. **Four rules in prompt header** with criterion tags -- visible before Phase 1
5. **FW Status column** as binary classification separate from anchor content
ion with per-finding slots.**
Every finding in the Phase 4 scaffold gets a slot in the Findings SCAFFOLD AUDIT. A missing
slot is a visible blank, not an absent sentence. The ATTESTATION line closes both paths:
conflict-present (CONFLICT entry with 4 fields) and no-change (explicit confirmation).
This makes C-14 and C-19 structurally indistinguishable from enforcement.

**3. NON-NEGOTIABLES BLOCK in the paper before the Abstract.**
The paper's first visible element is a 5-item compliance checklist a reviewer can check
without reading any section. C-20 requires paper-level declaration, not prompt-level rules.
Added to the Phase 6 paper template -- no new phase, no structural cost.

**4. Four non-negotiable rules in the prompt header with explicit criterion tags.**
The prompt opens with four rules tagged (C-12), (C-13), (C-14), (C-15/C-17). Every role
reads them before Phase 1. Non-negotiables are not buried in phase instructions.

**5. FW Status column as a binary classification distinct from anchor content.**
The Future Work table requires a Status column (`B-NN ANCHOR` or `NET-NEW`). A blank Status
cell is a structural failure visible without reading the B-NN Anchor cell. At least one
`B-NN ANCHOR` row required, closing the Status Quo forward loop (C-16, C-18).

---

## Prompt Body

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

| Item  | Question                                       | B-NN Anchor             | Status       |
|-------|------------------------------------------------|-------------------------|--------------|
| FW-01 | [Investigable question, specific enough start] | [B-NN from Status Quo]  | B-NN ANCHOR  |
| FW-02 | [Additional question]                          | --                      | NET-NEW      |

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

## Final Rubric Criteria Summary (v5)

### Essential (60 pts -- all must pass)

| ID | Name | Pass condition |
|----|------|----------------|
| C-01 | All 8 sections present | Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work -- distinct headers |
| C-02 | Hypothesis explicitly resolved | Committed verdict sentence in Findings; hedged outcome without verdict fails |
| C-03 | Evidence is traceable | Zero uncited claims; CITATION AUDIT Status: PASS gate before Findings |
| C-04 | Findings are synthesized | Each finding answers "what does this mean?" -- at least 2 interpretive conclusions |
| C-05 | Principles are extractable | Minimum 2 numbered actionable rules with finding citations |

### Recommended (30 pts)

| ID | Name |
|----|------|
| C-06 | Panel review with 2+ named expert roles |
| C-07 | Abstract standalone (<200 words, 4 elements) |
| C-08 | Future Work minimum 2 rows, at least 1 B-NN ANCHOR |
| C-09 | Principles cross-referenced to findings |
| C-10 | Cold-start readable (domain terms defined on first use) |

### Aspirational (34 pts -- v5 expansion from v4's 24)

| ID | Name | What it checks beyond the predecessor |
|----|------|----------------------------------------|
| C-11 | Findings classified by novelty | BASELINE MATCH / NEW SIGNAL column per finding |
| C-12 | Status Quo prior beliefs | Skeptic writes before Lead Author; minimum 2 B-NN beliefs |
| C-13 | Citation audit precedes Findings | Hard gate -- Status: PASS required to proceed |
| C-14 | Novelty scaffold pre-committed | Phase 4 scaffold from evidence only, before prose |
| C-15 | Skeptic post-review structured | Per-item PASS/FLAG; APPROVED required before panel |
| C-16 | Future Work closes Status Quo loop | At least one FW row anchors a B-NN from Status Quo |
| C-17 | Pre-flight mirrors post-review | Symmetry by design (Phase 2 checklist matches Phase 7 items) |
| C-18 | FW table machine-visible anchor column | B-NN Anchor column present; blank = structural failure |
| C-19 | Scaffold conflict mechanism | SCAFFOLD CONFLICT with 4 fields; mechanism exists |
| C-20 | Non-negotiables forward-declared | NON-NEGOTIABLES block in paper before Abstract |
| C-21 | Non-negotiables produced by non-author role | Pre-Skeptic produces block in Phase 2 before any prose |
| C-22 | SCAFFOLD AUDIT per-finding slots | One slot per finding; missing slot is blank |
| C-23 | PF-NN antecedent ID field | Each post-review item cites `[Pre-flight antecedent: PF-NN]` -- field check |
| C-24 | FW Status column binary classification | Separate Status column; blank visible without reading anchor |
| C-25 | Role separation: scaffold by Mid-Skeptic | Different role commits scaffold; bypassing requires named role failure |

**Max score: 124. Golden threshold: >= 80 with all 5 essential passing.**
