Written to `simulations/quest/variations/prove-publish-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — prove-publish

| ID | Axis | Core bet |
|----|------|----------|
| **V-01** | Role sequence: Skeptic Post-Review as dedicated standalone phase | C-15 is enforced most reliably when it is its own lifecycle phase with a named checklist. Pre-flight items become the checklist — closed loop from pre-work to post-work. |
| **V-02** | Output format: table-driven scaffold + Future Work loop table | Tabular output makes C-14 (scaffold before prose) and C-16 (B-NN anchor per FW row) machine-verifiable — a blank cell is structurally visible; an omitted sentence is not. |
| **V-03** | Lifecycle emphasis: novelty scaffold committed before Evidence is written | Pushing C-14 to before Evidence (not just before Findings prose) forces classification from raw artifacts — blocks rationalization drift at its source, before the author decides how to frame evidence. |
| **V-04** | Combined: forward declaration expanded to 6 non-negotiable rules | V-04 R2 scored 100/100 with 3 forward-declared rules. Adding C-14, C-15, C-16 as rules 4–6 at the prompt header extends the pattern to the full aspirational tier without new phases. |
| **V-05** | Combined: triple-Skeptic lifecycle — Pre / Mid / Post | Pre-Skeptic (C-12 + risk), Mid-Skeptic (C-13 + C-14), Post-Skeptic (C-15 only). Each role has exactly one job — the V-05 R2 isolation principle extended to R3's three new criteria. |

---

**Single-axis divergence:** V-01 isolates C-15 as a phase; V-02 enforces C-14 and C-16 via table columns; V-03 moves C-14 to the earliest possible lifecycle position (before Evidence).

**Combination divergence:** V-04 bets that forward declaration alone is sufficient — no structural changes needed, just add three more non-negotiable rules at the header. V-05 bets that role isolation produces the most structurally reliable execution, especially when session context grows long.

**The C-14 split:** V-01 inherits C-14 from a scaffold phase after Evidence; V-02 enforces it via a classification table with a locked sequence; V-03 pushes it before Evidence entirely; V-04 forward-declares it; V-05 delegates it to the Mid-Skeptic. Five distinct enforcement mechanisms for the same criterion — the R3 scorecard will show which produces the most reliable structural signal.
ed CITATION AUDIT block (C-13), Status Quo with concrete B-NN prior beliefs (C-12), and novelty tags on findings (C-11).

---

## V-01: Skeptic-Checklist-Spine

**Axis:** Role sequence — Skeptic Post-Review (C-15) is a dedicated phase that runs after paper
drafting and before panel review, with a structural checklist that maps to the pre-flight
commitments. The pre-flight items and the post-review items are the same list — closed loop.
**Hypothesis:** C-15 requires a "post-completion structural audit" with a named checklist,
pass/fail per item, and APPROVED/FLAG verdict — distinct from panel review. When the Skeptic
post-review is embedded inside a panel review phase (as in R2 V-04's SKEPTIC POST-REVIEW
sub-block), it can be abbreviated or collapsed into the panel critique. Extracting it as a
dedicated phase before panel review removes that ambiguity: the checklist runs first, APPROVED
is required before panel begins. The pre-flight items (Phase 2) become the checklist (Phase 6)
— the author committed to them at the start; the Skeptic verifies them at the end.
C-14 and C-16 are enforced via explicit template requirements inherited from R2 V-04 patterns.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight author + structural post-review), Lead Author (paper writer),
Domain Expert (substantive review), Practitioner (applicability review).

**Three non-negotiable rules:**
1. Status Quo section written by Skeptic before Lead Author writes a single section (C-12).
2. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13).
3. Novelty classification scaffold committed before any finding prose is written (C-14).

**Skeptic post-review rule (C-15):** After the paper is fully drafted, Skeptic runs a
named structural checklist and issues APPROVED or FLAG. This runs as its own phase, before
Domain Expert and Practitioner. It is not part of panel review.

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic:
- hypothesis, analysis, interview, websearch, synthesize

Disclose before proceeding:

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

**Output A: Pre-Flight Checklist** (this list becomes the Post-Review checklist in Phase 6)

```
SKEPTIC PRE-FLIGHT:
[ ] C1. Hypothesis verdict — Findings will resolve H-01 with an explicit committed sentence.
[ ] C2. Citation traceability — audit will pass (zero uncited claims) before Findings begins.
[ ] C3. Novelty scaffold — classification committed before any finding prose written.
[ ] C4. Synthesis quality — each finding answers "what does this mean?" not "what happened?".
[ ] C5. Principles actionability — each principle is a rule, not a vague statement.

Prediction: [most likely structural failure in this paper — one specific sentence]
Watch point: [section most at risk, with reason]
```

**Output B: Status Quo section (final text — inserted verbatim into paper)**

```
## Status Quo

Before this investigation began, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief 1 — what conventional understanding says]
- [B-02: Concrete prior belief 2 — what adjacent knowledge suggests]
- [B-03: Concrete prior belief 3 — the team's working assumption before hypothesis formed]

This investigation was motivated by: [gap or tension in the above that H-01 addresses].

Without this investigation, the default action would have been: [what team would have done
relying on these assumptions alone].
```

Minimum 2 concrete prior beliefs. Not background prose.
Lead Author reads both outputs before writing.

---

### Phase 3: Evidence (Before Findings)

Lead Author writes Evidence now — before Abstract, before Findings.

Citation format per claim:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For any uncitable claim: record separately, exclude from Evidence.
`UNCITABLE: [claim text] — no artifact source, moved to Limitations`

When Evidence is complete, output:

```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without citation anchor (must be 0 to proceed): [N]
Uncitable claims recorded for Limitations: [N]
Status: [PASS — proceed to novelty scaffold] or [BLOCKED — [N] uncited claims remain]
```

If BLOCKED: resolve before continuing. Do not proceed until Status: PASS.

---

### Phase 4: Novelty Classification Scaffold (Before Findings Prose)

With Evidence complete and audited, commit finding classifications now — before writing any
finding prose. This satisfies Rule 3 (C-14): the classification precedes the conclusion text.

Classification rules:
- BASELINE MATCH: finding confirms a prior belief from Status Quo (cite B-ID)
- NEW SIGNAL: finding challenges, extends, or contradicts a prior belief (cite B-ID),
  OR introduces something not anticipated in Status Quo (cite as "B-NONE")

```
NOVELTY CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
F-02: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
F-03: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
[Add F-04, F-05 as evidence supports]

NEW SIGNAL count: [N] of [N] findings.
```

If zero NEW SIGNAL:
```
SCAFFOLD FLAG: All classifications are BASELINE MATCH. No new signal identified.
Risk: synthesis may restate evidence rather than draw conclusions.
Proceeding — INERTIA FLAG will appear in Findings.
```

Classifications are set. To change after writing prose: state reclassification reason.

---

### Phase 5: Hypothesis Verdict

With Evidence audited and scaffold committed, state the verdict:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs that most directly support this verdict]
Full verdict sentence: "[One committed quotable sentence — no evasion accepted]"
```

Accepted: "The hypothesis was confirmed: E-03 and E-05 show that..."
Not accepted: "The evidence is mixed." / "The evidence suggests..." / "Further work is needed."

---

### Phase 6: Write the Paper

Lead Author writes all sections. Phase 2 Output B (Status Quo) and Phase 3 (Evidence)
are inserted verbatim — do not rewrite them.

**1. Abstract** (<200 words)
Written after the verdict is known. State: (a) question investigated, (b) method, (c) key
finding, (d) practical implication. Do not describe paper structure.
A reader who reads only this can state what was investigated, how, and what was found.

**2. Status Quo** (paste verbatim from Phase 2 Output B — do not edit)

**3. Hypothesis**
`H-01: [hypothesis text verbatim] (source: [file path])`
If the hypothesis was amended during investigation: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Why evidence was gathered this way.
Cold-start readable: define any domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 — all E-[N] items with citations)

Evidence complete marker (required):
```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**

HYPOTHESIS VERDICT from Phase 5 first (required):
```
HYPOTHESIS VERDICT
H-01: [text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[Committed sentence]"
```

Then findings using the scaffold from Phase 4 (do not reclassify without reason):
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" — not "what happened?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not derivable from the Status Quo baseline.
```
If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions. Paper validates the baseline.
Future Work should investigate: [gap in Status Quo assumptions].
```

**7. Principles**
Minimum 2 numbered action-oriented rules.
Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites its finding: `P-01 [from F-02]: ...`
Each tagged: `[EXTENDS BASELINE]` (refines a prior assumption) or `[REPLACES BASELINE]`
(contradicts a prior assumption).

**8. Limitations**
What the investigation did not cover. What cannot be concluded.
Uncitable claims from Phase 3: "The following claims had no artifact support: [items]."

**9. Future Work**
Minimum 2 specific investigable questions.
Required: at least one item explicitly names a B-NN gap from the Status Quo section (C-16).
```
FW-01 [closes B-NN gap]: Investigate whether [B-NN assumption] holds when [condition],
  using [specific method].
FW-02 [extends investigation]: [Additional question — may extend beyond Status Quo scope]
```
Failing form: "More research is needed on X."
The B-NN citation in at least one FW item is required.

---

### Phase 7: Skeptic Post-Review (Before Panel)

After the paper is fully drafted. Skeptic audits the paper against the pre-flight checklist
from Phase 2 Output A. Named output block — separate from Domain Expert and Practitioner.

```
SKEPTIC POST-REVIEW:
C1. Hypothesis verdict: [PASS — explicit committed verdict sentence present]
  or [FLAG — verdict sentence missing, evasive, or uncited]
C2. Citation traceability: [PASS — CITATION AUDIT block shows Status: PASS, zero uncited]
  or [FLAG — audit missing, or uncited claims found in Evidence]
C3. Novelty scaffold: [PASS — Phase 4 scaffold committed before Phase 6 finding prose]
  or [FLAG — scaffold absent, or classified after prose was written]
C4. Synthesis quality: [PASS — findings answer "what does this mean?", not raw data]
  or [FLAG — N findings restate evidence rather than drawing conclusions]
C5. Principles actionability: [PASS — all principles are action-oriented rules with finding citations]
  or [FLAG — N principles are vague summaries without rule form]

Pre-flight prediction outcome: [CONFIRMED — failure appeared as predicted]
  or [RESOLVED — watch point addressed in paper]
  or [STILL PRESENT — watch point not addressed: specify location]

Final verdict: [APPROVED] or [FLAG: items C-N failed — paper must be amended before output]
```

If FLAG: Lead Author amends flagged items. Skeptic re-issues verdict after amendments.
Panel review does not begin until verdict shows APPROVED.

---

### Phase 8: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy and domain correctness of Findings. Also assesses whether the
Status Quo baseline was accurately stated (not strawmanned or overstated).
One substantive critique or endorsement. Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Could a working team apply these without the full paper?
One substantive critique or endorsement. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique or endorsement] — Score: [N/10]
PRACTITIONER: [critique or endorsement] — Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT. Update Evidence complete marker.
If finding reclassified: state reason. Update scaffold in Phase 4 record.
If Future Work amended: confirm B-NN anchor still present in at least one FW item.
After amendments: Skeptic re-issues Post-Review verdict for any previously flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-02: Future-Work-Loop-Table

**Axis:** Output format — the finding classification and Future Work section use structured
tables; each table cell that can fail a rubric criterion becomes structurally visible and
non-skippable. A missing tag or missing B-NN citation is an empty cell; an omitted sentence
is not visible at all.
**Hypothesis:** V-02 R2's CITATION AUDIT block scored 100/100 on C-13 because the block is a
structured output the model cannot quietly omit — absence of the block is itself a visible
failure. This variation extends that principle to C-14 and C-16: a FINDING CLASSIFICATION
TABLE with a dedicated Classification and Baseline Anchor column makes pre-committed novelty
tags machine-verifiable (C-14), and a FUTURE WORK TABLE with a B-NN Anchor column makes the
Status Quo loop machine-verifiable (C-16). The hypothesis is that tabular output format is the
highest-reliability enforcement mechanism for criteria that require presence and sequence.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review),
Skeptic (structural post-review audit).

**Citation gate rule (C-13):** Findings section blocked until CITATION AUDIT block shows
zero uncited claims.
**Scaffold table rule (C-14):** Finding classifications committed in a table before any
finding prose is written. Reclassification after prose: state reason in the table.
**Future Work loop rule (C-16):** Each Future Work item declares its B-NN anchor or marks
"NET-NEW"; at least one must carry a B-NN anchor naming a gap from the Status Quo section.

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
| ID   | Prior Belief                            | Source of assumption            |
|------|-----------------------------------------|---------------------------------|
| B-01 | [Concrete prior assumption 1]           | [Common understanding / team]   |
| B-02 | [Concrete prior assumption 2]           | [Adjacent domain / prior art]   |
| B-03 | [Optional — concrete prior assumption]  | [Working hypothesis at start]   |

Investigation trigger: [gap or tension in the above that H-01 was designed to resolve]
Default action without investigation: [what team would have done relying on these]
```

Minimum 2 rows. Each belief must be concrete and stated, not background narrative.

---

### Phase 3: Evidence (Written Before Findings)

Lead Author writes Evidence first. Each claim on its own numbered line with citation.

`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims: record and exclude from Evidence.
`UNCITABLE: [claim text] — no source, moved to Limitations`

Citation audit (required before Phase 4):
```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without citation anchor (must be 0): [N]
Uncitable claims for Limitations: [N]
Status: [PASS — proceed to scaffold table] or [BLOCKED — [N] uncited claims remain]
```

Do not proceed to Phase 4 until Status: PASS.

---

### Phase 4: Finding Classification Table (Before Findings Prose)

Before writing any finding, fill the classification table.
Use only the artifact evidence loaded in Phase 1 and cited in Phase 3.

```
FINDING CLASSIFICATION TABLE:
| F-ID | Classification                | Baseline Anchor  | Evidence Basis |
|------|-------------------------------|------------------|----------------|
| F-01 | [BASELINE MATCH / NEW SIGNAL] | [B-ID or B-NONE] | [E-IDs]        |
| F-02 | [BASELINE MATCH / NEW SIGNAL] | [B-ID or B-NONE] | [E-IDs]        |
| F-03 | [BASELINE MATCH / NEW SIGNAL] | [B-ID or B-NONE] | [E-IDs]        |

NEW SIGNAL count: [N] of [N] total findings.
```

BASELINE MATCH = confirms the belief in that B-ID row.
NEW SIGNAL = challenges, extends, or contradicts that B-ID, or introduces B-NONE.

If NEW SIGNAL count is zero:
```
SCAFFOLD FLAG: All findings confirm prior assumptions.
Risk: paper is a baseline validation, not a new signal. Proceeding with INERTIA FLAG.
```

Classifications are locked. To change after writing prose: add a RECLASSIFICATION row:
```
| F-02 | RECLASSIFIED: BASELINE MATCH → NEW SIGNAL | Reason: [one sentence] | |
```

---

### Phase 5: Hypothesis Verdict

After Evidence audited, before writing all paper sections:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs most directly supporting this verdict]
Full verdict sentence: "[One quotable committed sentence — no evasions]"
```

Accepted: "The hypothesis was confirmed: E-03 and E-05 show that..."
Not accepted: "The evidence suggests..." / "The evidence is mixed."

---

### Phase 6: Write the Paper

All sections in order. Phase 2 (Status Quo table) and Phase 3 (Evidence) inserted verbatim.

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.)

**2. Status Quo** (formalize Phase 2 prior belief table as prose + embedded table)
```
## Status Quo

Before this investigation, the following was assumed:
[Prior Belief Table from Phase 2]

This investigation was motivated by: [trigger from Phase 2].
Without this investigation, the default action would have been: [Phase 2 default action].
```

**3. Hypothesis** (`H-01: [text] (source: [file path])`)

**4. Method**
Prove skills run. Artifacts produced. Why this approach was chosen.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 — E-[N] numbered items with citations)

Evidence complete marker (required):
```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored. [N] uncitable → Limitations.
```

**6. Findings**

HYPOTHESIS VERDICT from Phase 5 appears first.

Then findings, using the classification table from Phase 4:
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" — not "what happened?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If any NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not derivable from the Status Quo baseline.
```
If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirm prior assumptions. Paper validates the baseline.
Future Work should target: [specific gap in Status Quo beliefs].
```

**7. Principles**
Minimum 2 numbered action-oriented rules.
Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites its finding: `P-01 [from F-02]: ...`

**8. Limitations**
Scope boundaries. Uncitable claims from Phase 3 appear here.

**9. Future Work** — required table format (C-16 enforced by column)

```
FUTURE WORK TABLE:
| FW-ID | Question                                             | B-NN Anchor        | Method  |
|-------|------------------------------------------------------|--------------------|---------|
| FW-01 | [Specific investigable question]                     | [B-01 or B-02]     | [How]   |
| FW-02 | [Specific investigable question]                     | [B-ID or NET-NEW]  | [How]   |
```

Rules:
- Minimum 2 rows.
- At least one row must carry a B-NN anchor (not NET-NEW) — this is C-16.
- B-NN anchor form: "Investigate whether [B-NN assumption] holds when [condition], using [method]."
- NET-NEW is valid for questions that extend beyond the Status Quo baseline.
- Failing form: "More research is needed on X." — do not use.

---

### Phase 7: Skeptic Post-Review (Before Panel)

After paper is fully drafted. Skeptic audits the paper's structural commitments.
Separate output block — not part of Domain Expert or Practitioner critique.

```
SKEPTIC POST-REVIEW:
[ ] SQ-01. Status Quo present with ≥2 concrete B-NN prior beliefs, precedes Hypothesis: [PASS / FLAG]
[ ] SQ-02. Citation audit block shows Status: PASS, zero uncited claims: [PASS / FLAG]
[ ] SQ-03. Classification table committed before finding prose (Phase 4 before Phase 6): [PASS / FLAG]
[ ] SQ-04. Hypothesis verdict sentence is explicit and non-evasive: [PASS / FLAG]
[ ] SQ-05. Future Work table includes ≥1 row with a B-NN anchor (not NET-NEW): [PASS / FLAG — cite which FW-NN]

Final verdict: [APPROVED] or [FLAG: items SQ-NN failed — amend before output]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict after amendment.
Panel review does not begin until verdict shows APPROVED.

---

### Phase 8: Panel Review

**Domain Expert:** Evidence accuracy + Findings quality + Status Quo correctness. Score: [N/10]
**Practitioner:** Principles actionability. Score: [N/10]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT. Update Evidence complete marker.
If classification changed: add RECLASSIFICATION row to FINDING CLASSIFICATION TABLE.
If Future Work amended: verify B-NN anchor column still populated in ≥1 FW row.
After amendments: Skeptic re-issues Post-Review verdict for any flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-03: Pre-Evidence Scaffold

**Axis:** Lifecycle emphasis — novelty classification scaffold committed before the Evidence
section is written (not just before Findings prose). The author classifies each finding from
raw loaded artifacts before writing a single evidence claim.
**Hypothesis:** V-03 R2 moved classification before Findings prose — a significant C-14
improvement over R1. But the classification still followed Evidence writing, which allows
selection drift: authors unconsciously surface and frame evidence to support their pre-formed
sense of what the findings will be, then classify accordingly. Moving the scaffold to before
Evidence forces classification from raw artifacts alone (analysis findings, synthesis
conclusions, interview themes). If the author commits to "this finding is BASELINE MATCH or
NEW SIGNAL" before deciding how to present the evidence, the classification is harder to
rationalize post-hoc. This is the earliest possible C-14 intervention in the authoring
lifecycle and the strongest protection against evidence-framing drift.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review),
Skeptic (structural audit).

**Session order (strict):** Novelty scaffold committed from raw artifacts → Evidence written
and audited → Paper written → Skeptic Post-Review → Panel Review.

**Core rule (C-14):** The classification scaffold is produced from loaded artifacts before
the Evidence section is written. Evidence writing follows the scaffold — not the other way.
Reclassification is permitted only with an explicit stated reason.

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

If no hypothesis found: stop. Do not proceed.

---

### Phase 2: Prior Belief Inventory + Pre-Evidence Novelty Scaffold

Two outputs produced from raw artifact review — before writing any evidence claim.

**Output A: Prior Belief Inventory**

Based on the loaded artifacts (not on the investigation's conclusions), inventory what was
likely assumed before this investigation began.

```
PRIOR BELIEF INVENTORY:
B-01: [Concrete prior assumption 1]
B-02: [Concrete prior assumption 2]
B-03: [Optional — concrete prior assumption 3]

Investigation trigger: [gap or tension in the above that H-01 was designed to resolve]
```

Minimum 2 concrete prior beliefs. Not background prose or domain background.

**Output B: Pre-Evidence Novelty Classification Scaffold**

Review the loaded artifacts (analysis findings, synthesis outputs, interview themes,
websearch sources). For each distinct conclusion the artifacts support, classify now —
before writing any evidence claim. Use raw references, not yet E-IDs.

```
PRE-EVIDENCE NOVELTY SCAFFOLD:
[Based on artifact review only — not on how Evidence will be written]

F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Artifact basis: [analysis finding X / synthesis conclusion Y / raw quote Z]
F-02: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Artifact basis: [raw artifact reference]
F-03: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Artifact basis: [raw artifact reference]
[Add F-04, F-05 as artifacts support]

NEW SIGNAL count: [N] of [N] expected findings.
```

If zero NEW SIGNAL:
```
PRE-EVIDENCE FLAG: All expected findings are BASELINE MATCH.
Risk: investigation may not have produced new signals. Lead Author should consider
whether artifact scope was sufficient before writing Evidence.
```

Classifications are now committed. Evidence writing follows these commitments.
To reclassify: state reason explicitly before writing the affected finding.

---

### Phase 3: Evidence (After Scaffold, Before Findings)

Lead Author writes Evidence with the pre-evidence scaffold in mind.
Evidence should support — or honestly conflict with — the pre-committed classifications.

Citation format:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims: do not include in Evidence.
`UNCITABLE: [claim text] — no source, moved to Limitations`

When Evidence is complete:
```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without citation anchor (must be 0): [N]
Uncitable claims for Limitations: [N]
Status: [PASS — proceed to Findings] or [BLOCKED — [N] uncited claims remain]
```

Do not continue until Status: PASS.

If Evidence contradicts a pre-committed scaffold classification, note the conflict:
```
SCAFFOLD CONFLICT: F-XX pre-committed as [tag] but evidence weight suggests [alternative tag].
Reclassification reason: [one sentence explaining what changed]
Updated classification: [new tag — will appear in Findings]
```

---

### Phase 4: Hypothesis Verdict

With Evidence audited:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [2-3 E-IDs most directly supporting the verdict]
Full verdict sentence: "[One committed quotable sentence — no evasion accepted]"
```

Not accepted: "The evidence suggests..." / "Further investigation is needed."

---

### Phase 5: Write the Paper

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.)

**2. Status Quo** (formalize Phase 2 Output A prior belief inventory)
```
## Status Quo

Before this investigation, the following was assumed:
- [B-01 text]
- [B-02 text]
This investigation was motivated by: [trigger from Phase 2].
```
Minimum 2 concrete prior beliefs. Precedes Hypothesis.

**3. Hypothesis** (`H-01: [text] (source: [file path])`)

**4. Method**
Prove skills run. Artifacts produced. Why this approach was chosen.
Include: "A pre-evidence novelty scaffold was committed from artifacts before Evidence was
written, to prevent evidence-selection drift (see Phase 2 Output B)."
Cold-start readable: define any domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 — E-[N] numbered items with citations)

Evidence complete marker:
```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored. [N] uncitable → Limitations.
```

**6. Findings**

HYPOTHESIS VERDICT from Phase 4 appears first.

Then findings using the pre-evidence scaffold from Phase 2 Output B, with any reclassifications
from Phase 3 conflicts applied (reason stated):
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" — not "what happened?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If any NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not predictable from the Status Quo baseline.
```
If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions.
Future Work should investigate: [gap in B-01/B-02 assumptions].
```

**7. Principles**
Minimum 2 numbered action-oriented rules.
Form: "Always X", "When Y, do Z", "Prefer A over B."
Each cites its finding: `P-01 [from F-02]: ...`

**8. Limitations**
Scope boundaries. Uncitable claims from Phase 3. Any scaffold conflicts and their
reclassification reasons.

**9. Future Work**
Minimum 2 specific investigable questions.
Required: at least one names a B-NN gap from the Status Quo section (C-16).
```
FW-01 [addresses B-NN gap]: Investigate whether [B-NN assumption] holds when [condition],
  using [specific method].
FW-02 [extends investigation]: [Additional question — may extend beyond Status Quo scope]
```

---

### Phase 6: Skeptic Post-Review (Before Panel)

After paper is fully drafted. Named structural checklist + verdict.

```
SKEPTIC POST-REVIEW:
[ ] 1. Status Quo present with ≥2 concrete prior beliefs (B-NN format), precedes Hypothesis: [PASS / FLAG]
[ ] 2. Pre-evidence scaffold committed before Evidence section (Phase 2 Output B precedes Phase 3): [PASS / FLAG]
[ ] 3. Citation audit PASS with EVIDENCE COMPLETE marker present in paper: [PASS / FLAG]
[ ] 4. Hypothesis verdict is explicit and non-evasive (committed sentence present): [PASS / FLAG]
[ ] 5. At least one Future Work item names a specific B-NN gap from Status Quo: [PASS / FLAG — cite which FW-NN]

Final verdict: [APPROVED] or [FLAG: items N failed — amend before output]
```

If FLAG: Lead Author amends. Skeptic re-issues verdict after amendment.
Panel does not begin until verdict shows APPROVED.

---

### Phase 7: Panel Review

**Domain Expert:** Evidence accuracy + Status Quo baseline correctness + Findings quality.
One substantive critique or endorsement. Score: [N/10]

**Practitioner:** Principles actionability.
One substantive critique or endorsement. Score: [N/10]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 8: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT. Update Evidence complete marker.
If scaffold reclassified: update pre-evidence scaffold record with stated reason.
If Future Work amended: confirm B-NN anchor still present in ≥1 FW item.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-04: Forward-Declaration-v2

**Axis:** Combined — extends V-04 R2's forward declaration pattern; all three R3 aspirationals
(C-14, C-15, C-16) are declared as non-negotiable structural rules at the prompt header before
Phase 1, alongside the three R2 rules (C-11, C-12, C-13). Six non-negotiable rules total.
**Hypothesis:** V-04 R2 opened with "Three structural rules (non-negotiable):" naming C-11,
C-12, C-13 before Phase 1 and scored 100/100 on the v2 rubric. The forward declaration creates
a commitment at the highest possible scope — the model sees all constraints before reading a
phase. The R2 scorecard called this "the strongest intent signal" because declaring at the
header level makes constraints harder to ignore under context drift. Adding C-14, C-15, C-16
as rules 4–6 extends the pattern to the full aspirational tier. The risk is that 6 rules feels
mechanical; the counter-bet is that each rule maps to exactly one phase, and the declaration
serves as a cross-phase compliance checklist that survives long sessions.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight + Status Quo + post-review audit), Lead Author (paper writer),
Domain Expert (review), Practitioner (review).

**Six structural rules — all non-negotiable:**
1. Status Quo section produced by Skeptic before any paper section is written (C-12).
2. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13).
3. Every finding carries a BASELINE MATCH or NEW SIGNAL tag (C-11).
4. Novelty classification scaffold committed in a named block before any finding prose (C-14).
5. Skeptic Post-Review with ≥5-item structural checklist and APPROVED/FLAG verdict runs after
   paper is drafted, before panel review — structurally separate from Domain Expert and
   Practitioner critique (C-15).
6. At least one Future Work item names a specific B-NN gap from the Status Quo section (C-16).

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
Cannot publish: hypothesis artifact required. Run /prove:hypothesis first.
```

---

### Phase 2: Skeptic Pre-Flight + Status Quo (Rule 1)

Skeptic runs before Lead Author writes anything. Two outputs.

**Output A: Pre-Flight Checklist**

```
SKEPTIC PRE-FLIGHT:
[ ] H-01 hypothesis — will verify Findings resolves it with an explicit committed verdict.
[ ] Evidence traceability — citation audit will pass (zero uncited) before Findings begins.
[ ] Novelty scaffold — will verify scaffold committed before any finding prose.
[ ] Findings synthesis — will verify each finding answers "what does this mean?".
[ ] Principles actionability — will verify each principle is a rule, not a vague statement.

Prediction: [specific anticipated failure — one sentence citing an artifact]
Watch point: [section most at risk, with reason]
```

**Output B: Status Quo section (final version — inserted verbatim into paper)**

```
## Status Quo

Before this investigation began, a team in this area would likely have assumed:
- [B-01: Concrete prior belief 1]
- [B-02: Concrete prior belief 2]
- [B-03: Concrete prior belief 3]

This investigation was motivated by: [gap or tension in the above that H-01 addresses].

Without this investigation, the default action would have been: [what team would have done].
```

Minimum 2 concrete prior beliefs. Not background prose.
Lead Author reads both outputs before writing. Rule 1 satisfied.

---

### Phase 3: Evidence (Rule 2 — Findings Blocked Until CITATION AUDIT Passes)

Lead Author writes Evidence now — before Abstract, before Findings.

Citation format:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims:
`UNCITABLE: [claim text] — moved to Limitations`

Citation audit (Rule 2 — required):
```
CITATION AUDIT
Total evidence items: [N]
Items with citation anchor: [N]
Items without citation anchor (must be 0 to proceed): [N]
Uncitable claims moved to Limitations: [N]
Status: [PASS — Findings unlocked] or [BLOCKED — [N] uncited claims remain]
```

Do not proceed to Phase 4 until Status: PASS.

---

### Phase 4: Novelty Classification Scaffold (Rule 4 — Before Findings Prose)

With Evidence audited, commit classifications before writing any finding text.
This is the named block required by Rule 4 (C-14).

```
NOVELTY CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Evidence basis: [E-IDs]
F-02: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]
F-03: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]
[Add F-04, F-05 as evidence supports]

NEW SIGNAL count: [N] of [N] findings.
```

If zero NEW SIGNAL:
```
SCAFFOLD FLAG: All BASELINE MATCH. Investigation validated prior beliefs.
INERTIA FLAG will appear in Findings.
```

Rule 4 satisfied: scaffold committed. Reclassify after prose only with stated reason.

---

### Phase 5: Hypothesis Verdict

With Evidence audited and scaffold committed:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[One quotable committed sentence — no evasion accepted]"
```

Not accepted: "The evidence is mixed." / "Further investigation is needed."

---

### Phase 6: Write the Paper

Lead Author writes all sections. Phase 2 Output B (Status Quo) and Phase 3 (Evidence)
inserted verbatim — do not rewrite.

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.
Written as if it is the only thing a future researcher reads.)

**2. Status Quo** (paste verbatim from Phase 2 Output B — Rule 1 satisfied in paper)

**3. Hypothesis**
`H-01: [text] (source: [file path])`
If amended during investigation: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Why this approach was chosen.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 — E-[N] items with citations)

Evidence complete marker (required):
```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored. [N] uncitable → Limitations.
```

**6. Findings**

HYPOTHESIS VERDICT from Phase 5 appears first.

Then findings using scaffold from Phase 4 (Rules 3 + 4):
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" — not "what happened?"]

F-02 [NEW SIGNAL — contradicts B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not predictable from the Status Quo baseline.
```
If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions. Paper validates the baseline.
Future Work should investigate: [gap in Status Quo baseline].
```

**7. Principles**
Minimum 2 numbered rules. "Always X", "When Y, do Z", "Prefer A over B."
Each cites finding: `P-01 [from F-02]: ...`
Each tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`.

**8. Limitations**
What was not covered. Uncitable claims from Phase 3.

**9. Future Work** (Rule 6 — at least one item names a B-NN gap)
Minimum 2 specific investigable questions.
```
FW-01 [closes B-NN gap]: Investigate whether [B-NN assumption] holds when [condition],
  using [specific method].
FW-02 [extends investigation]: [Additional question]
```
At least one FW item must name a B-ID from the Status Quo section. Rule 6 requires this.
Failing form: "More research is needed on X."

---

### Phase 7: Skeptic Post-Review (Rule 5 — Before Panel)

After paper is fully drafted. Named structural checklist — separate from Domain Expert and
Practitioner. APPROVED or FLAG verdict required. Rule 5 (C-15) gate.

```
SKEPTIC POST-REVIEW:
[ ] 1. Status Quo: ≥2 concrete prior beliefs present (B-NN format), precedes Hypothesis: [PASS / FLAG]
[ ] 2. Citation audit: EVIDENCE COMPLETE marker present, Status: PASS, zero uncited: [PASS / FLAG]
[ ] 3. Novelty scaffold: Phase 4 block committed before Phase 6 finding prose: [PASS / FLAG]
[ ] 4. Hypothesis verdict: explicit committed sentence present, non-evasive form: [PASS / FLAG]
[ ] 5. Future Work: ≥1 item names a specific B-NN gap (names B-ID from Status Quo): [PASS / FLAG — cite which FW-NN]

Pre-flight prediction outcome: [CONFIRMED / RESOLVED / STILL PRESENT — one sentence]
Final verdict: [APPROVED] or [FLAG: items N failed — paper must be amended before panel]
```

If FLAG: Lead Author amends flagged items. Skeptic re-issues verdict after amendments.
Panel review (Phase 8) does not begin until verdict shows APPROVED.

---

### Phase 8: Panel Review

Runs after Skeptic Post-Review APPROVED.

**Domain Expert:**
Reviews Evidence accuracy and Findings quality. Also assesses Status Quo baseline
accuracy (were prior assumptions correctly stated?).
One substantive critique or endorsement. Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Could a working team apply these without the full paper?
One substantive critique or endorsement. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence amended: re-run CITATION AUDIT. Update Evidence complete marker.
If finding reclassified: update Phase 4 scaffold with reclassification reason.
If Future Work amended: confirm Rule 6 still satisfied (B-NN anchor in ≥1 FW item).
After amendments: Skeptic re-issues Post-Review verdict for any previously flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-05: Triple-Skeptic

**Axis:** Role sequence + lifecycle emphasis — three Skeptic roles at distinct lifecycle
gates, each with exactly one job and one output format:
- Pre-Skeptic: Status Quo + pre-flight risk naming (before authoring)
- Mid-Skeptic: Citation audit + novelty classification scaffold (after Evidence, before Findings)
- Post-Skeptic: Structural checklist + APPROVED/FLAG verdict (after paper complete, before panel)

**Hypothesis:** V-05 R2 had Pre-Skeptic + Post-Skeptic and scored the highest structural
isolation rating: "each Skeptic has exactly one job." The R2 Post-Skeptic handled citation
audit (C-13) + novelty scaffold (C-11/C-14 combined) — two jobs in one role. R3 adds C-15 as
a post-completion structural audit, which would make the Post-Skeptic three jobs. The
extension is to split: a Mid-Skeptic takes C-13 + C-14 (evidence-phase work), and the
Post-Skeptic is reserved exclusively for C-15 (paper-completion structural audit). Pre-Skeptic
remains unchanged (C-12 + risk naming). Each of three Skeptic instances has exactly one job.
The overhead is one additional role invocation; the benefit is that no role can collapse two
jobs into a single rushed output when context is long.

```
You are running /prove:publish for Signal.

Stock roles:
- Pre-Skeptic: Status Quo (C-12) + pre-flight risk naming (before authoring begins)
- Lead Author: Evidence section only
- Mid-Skeptic: Citation audit (C-13) + novelty classification scaffold (C-14)
- Lead Author: All remaining paper sections
- Post-Skeptic: Structural checklist + APPROVED/FLAG verdict (C-15) (before panel)
- Domain Expert, Practitioner: panel review (after Post-Skeptic APPROVED)

**Session order (strict):**
Pre-Skeptic → Lead Author writes Evidence → Mid-Skeptic → Lead Author writes paper →
Post-Skeptic → Panel Review.

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

If no hypothesis found: stop. Do not proceed.

---

### Phase 2: Pre-Skeptic

Pre-Skeptic's job: set the baseline and name the risks. Two outputs. Nothing else.

**Output A: Pre-Flight Checklist**

```
PRE-SKEPTIC PRE-FLIGHT:
[ ] H-01 hypothesis — Findings will resolve it with an explicit committed verdict sentence.
[ ] Evidence traceability — Mid-Skeptic citation audit will pass before Findings begins.
[ ] Novelty scaffold — Mid-Skeptic scaffold committed before Lead Author writes findings.
[ ] Findings synthesis — each finding will answer "what does this mean?" not "what happened?".
[ ] Principles actionability — each principle will be a rule, not a vague statement.

Prediction: [most likely failure in this paper — one specific sentence citing an artifact]
```

**Output B: Status Quo section (final text — inserted verbatim into paper)**

```
## Status Quo

Before this investigation, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief 1]
- [B-02: Concrete prior belief 2]
- [B-03: Optional — concrete prior belief 3]

This investigation was motivated by: [gap or tension in the above that H-01 addresses].

Without this investigation, the team would have: [default action relying on these assumptions].
```

Minimum 2 concrete prior beliefs. Not background prose.
Lead Author reads both outputs before writing anything.

---

### Phase 3: Lead Author — Evidence Section Only

Lead Author writes only the Evidence section. Stop after Evidence is complete.

Citation format:
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

For uncitable claims: record separately, do not include in Evidence.
`HOLD (uncitable): [claim text] — no artifact source`

Write all evidence items. Stop. Pass to Mid-Skeptic.

---

### Phase 4: Mid-Skeptic

Mid-Skeptic's job: audit citations and commit novelty scaffold. Two tasks. Nothing else.

**Task A: Citation Audit**

```
MID-SKEPTIC CITATION AUDIT:
Evidence items reviewed:
  E-01: [CITED — source: file.md, section/ID] or [UNCITED — move to Limitations]
  E-02: [CITED — source: file.md, section/ID] or [UNCITED — move to Limitations]
  [continue for all items]

Total: [N] | Cited: [N] | Uncited (must be 0): [N]
Status: [PASS] or [BLOCKED — [N] uncited items, listed above]
```

If BLOCKED: specify which items need citations. Lead Author must fix before Task B.
Do not proceed to Task B until Status: PASS.

**Task B: Novelty Classification Scaffold**

After citation audit PASS, produce the finding classification scaffold.
This scaffold commits to what each finding will be before Lead Author writes prose.

```
MID-SKEPTIC NOVELTY SCAFFOLD:
Status Quo baseline: B-01, B-02[, B-03] (from Phase 2 Output B)

Expected finding classifications:
F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Evidence basis: [E-IDs supporting this classification]
F-02: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]
F-03: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]

NEW SIGNAL count: [N] expected new signals out of [N] findings.
```

If zero NEW SIGNAL:
```
SCAFFOLD FLAG: All expected findings confirm prior assumptions.
Lead Author note: paper is a baseline validation. INERTIA FLAG will appear in Findings.
```

Lead Author uses this scaffold. Classifications are committed.
To reclassify when writing: state reason explicitly before the affected finding.

---

### Phase 5: Hypothesis Verdict

Lead Author commits to the verdict after Mid-Skeptic Task A PASS:

```
HYPOTHESIS VERDICT
H-01: [text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[One quotable committed sentence — no evasion]"
```

Not accepted: "The evidence is mixed." / "The evidence suggests..."

---

### Phase 6: Lead Author — Write All Remaining Sections

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.)

**2. Status Quo** (paste verbatim from Phase 2 Output B — do not edit)

**3. Hypothesis** (H-01 from Phase 5 verdict block + source path)

**4. Method**
Prove skills run. Artifacts produced. Why this approach was chosen. Cold-start readable.
Include: "Evidence was audited by Mid-Skeptic and a novelty scaffold committed before
Findings were written."
Define domain-specific terms on first use.

**5. Evidence** (paste from Phase 3, verified by Mid-Skeptic Task A)

Evidence complete marker:
```
EVIDENCE COMPLETE: Mid-Skeptic citation audit passed. [N] items anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**

HYPOTHESIS VERDICT from Phase 5 first.

Then findings using Mid-Skeptic novelty scaffold from Phase 4 Task B:
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" — not "what happened?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not predictable from the Status Quo baseline.
```
If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions.
Future Work target: [gap from Status Quo baseline].
```

**7. Principles**
Minimum 2 numbered action-oriented rules.
Each cites finding: `P-01 [from F-02]: ...`
Accepted forms: "Always X", "When Y, do Z", "Prefer A over B because..."

**8. Limitations**
Scope boundaries. HOLD (uncitable) claims from Phase 3 appear here.

**9. Future Work**
Minimum 2 specific investigable questions.
Required: at least one names a B-NN gap from the Status Quo section (C-16).
```
FW-01 [closes B-NN gap]: Investigate whether [B-NN assumption] holds when [condition],
  using [specific method].
FW-02 [extends investigation]: [Additional question — may go beyond Status Quo scope]
```

---

### Phase 7: Post-Skeptic (C-15 — Before Panel)

Post-Skeptic's job: structural checklist audit + verdict. Nothing else.
Runs after paper is complete, before Domain Expert and Practitioner.

```
POST-SKEPTIC STRUCTURAL AUDIT:
[ ] 1. Status Quo: ≥2 concrete prior beliefs (B-NN format), precedes Hypothesis: [PASS / FLAG]
[ ] 2. Evidence: Mid-Skeptic CITATION AUDIT Status: PASS, zero uncited,
        EVIDENCE COMPLETE marker present in paper: [PASS / FLAG]
[ ] 3. Novelty scaffold: Mid-Skeptic Phase 4 Task B committed before Phase 6 finding prose: [PASS / FLAG]
[ ] 4. Hypothesis verdict: explicit committed sentence, non-evasive form, before first finding: [PASS / FLAG]
[ ] 5. Future Work: ≥1 item names a specific B-NN gap from the Status Quo section
        (cites a B-ID, not generic): [PASS / FLAG — cite which FW-NN]

Pre-Skeptic prediction outcome: [CONFIRMED — failure appeared as predicted]
  or [RESOLVED — watch point addressed in paper]
  or [STILL PRESENT — watch point not addressed: specify location]

Final verdict: [APPROVED] or [FLAG: items N failed — Lead Author must amend before output]
```

If FLAG: Lead Author amends. Post-Skeptic re-audits flagged items after amendment.
Panel review does not begin until verdict shows APPROVED.

---

### Phase 8: Panel Review

Runs after Post-Skeptic APPROVED.

**Domain Expert:**
Reviews Evidence accuracy and Status Quo baseline correctness (prior assumptions correctly
stated?). One substantive critique or endorsement. Score: [N/10]

**Practitioner:**
Reviews Principles actionability.
One substantive critique or endorsement. Score: [N/10]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 9: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Post-Skeptic]
```

If Evidence amended: Mid-Skeptic re-runs CITATION AUDIT. Update EVIDENCE COMPLETE marker.
If finding reclassified: update Mid-Skeptic novelty scaffold record with stated reason.
If Future Work amended: confirm B-NN anchor still present in ≥1 FW item.
After amendment: Post-Skeptic re-audits any previously flagged items.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```
