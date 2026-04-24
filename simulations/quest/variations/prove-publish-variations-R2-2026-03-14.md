Written to `simulations/quest/variations/prove-publish-variations-R2-2026-03-14.md`.

---

### Round 2 Variations — prove-publish

| ID | Axis | Core bet |
|----|------|----------|
| **V-01** | Inertia framing: Status Quo as structural spine | Status Quo written by Skeptic before any paper section. All findings tagged against it. C-12 becomes an anchor, not an afterthought. |
| **V-02** | Lifecycle: citation audit as literal output gate | Evidence first, then a required CITATION AUDIT block (uncited = 0 to proceed). C-13 is a hard stop, not a guideline. |
| **V-03** | Output format: novelty-pre-classification | Finding classification committed before prose is written. Author declares BASELINE MATCH or NEW SIGNAL first; conclusion text follows. Forces C-11 to shape findings rather than decorate them. |
| **V-04** | Combined: V-01 excellence + all three R2 aspirationals | V-01's 96-point scaffold extended with Status Quo phase (C-12), citation audit gate (C-13), novelty tagging (C-11). All 13 criteria targeted in one prompt. |
| **V-05** | Role sequence: split Skeptic | Pre-Skeptic (Status Quo + pre-flight before authoring), Post-Skeptic (citation audit + novelty scaffold after Evidence). Separates baseline-setting from audit work — each Skeptic instance has exactly one job. |

**Key design choices for R2:**
- Every variation includes Status Quo, novelty tagging, and evidence-before-findings — the three R2 aspirationals are structural in all five, not optional
- V-01 and V-05 diverge on *who formalizes* the Status Quo: V-01's Skeptic writes the final section text; V-05's Pre-Skeptic writes a private pre-flight artifact the Lead Author formalizes
- V-02 is the purest single-axis: no new roles, just a hard lifecycle gate that was missing from R1 V-03
- V-04 is the ceiling bet: if V-01 was 96/100 before the R2 criteria existed, adding all three cleanly should complete coverage
keptic (citation audit + novelty classification scaffold after Evidence). Separates baseline-setting from audit work into distinct, non-overlapping jobs. |

**Design note:** V-01 and V-05 both involve a Skeptic establishing a Status Quo baseline, but
V-01's Skeptic writes the baseline as the final Status Quo section; V-05's Pre-Skeptic writes
a private pre-flight artifact that the Lead Author formalizes. V-02 is the purest single-axis:
no roles added, just a hard lifecycle gate on citations. V-04 is the integration bet — V-01
was 96/100 before C-11/C-12/C-13 existed; V-04 tests whether adding all three reaches the
rubric ceiling. V-03 is the most structurally novel: it inverts the usual write-then-tag
sequence into classify-then-write.

---

## V-01: Status-Quo-Spine

**Axis:** Inertia framing — Status Quo section written first, before any other paper content,
as the structural anchor against which all findings are measured
**Hypothesis:** Writing the Status Quo section before authoring begins forces the author to
commit to the prior belief baseline in concrete terms. This naturally produces BASELINE MATCH
vs NEW SIGNAL contrast in Findings (C-11), satisfies C-12 structurally (the section exists
because it was the first substantive output), and cold-orients future readers (C-10) because
it was written for an uninitiated reader from the start — not retrofitted. R1 V-01 scored 96
without any of these; this variation bets that anchoring everything to an upfront Status Quo
adds all three new aspirationals without disrupting the core.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (Status Quo author), Lead Author (paper writer), Domain Expert (review),
Practitioner (review).

**Spine rule:** The Status Quo section is the first substantive content produced in this
session. All findings will be measured against it. A finding is a BASELINE MATCH if it
confirms the Status Quo; it is a NEW SIGNAL if it challenges, extends, or contradicts it.

---

### Phase 1: Artifact Load

Read all prove artifacts for the topic under `simulations/prove/`:
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

If no hypothesis artifact found: stop. Output:
```
Cannot publish: no hypothesis artifact at simulations/prove/hypothesis/*.
Run /prove:hypothesis first or supply hypothesis text.
```

---

### Phase 2: Status Quo (Written Before Everything Else)

The Skeptic writes the Status Quo section now — before the Lead Author writes a single word.
This is not a draft; it is the final text that will appear verbatim in the paper.

```
## Status Quo

Before this investigation began, a team working in this area would likely have assumed:
- [B-01: Prior belief 1 — what conventional understanding says about this topic]
- [B-02: Prior belief 2 — what adjacent domain knowledge suggests]
- [B-03: Prior belief 3 — the team's default working assumption before the hypothesis formed]

The investigation was motivated by: [gap, tension, or uncertainty in the above that the
hypothesis was designed to resolve].

Without this investigation, the default action would have been: [what the team would have
done relying on the above assumptions alone].
```

Minimum 2 prior beliefs. Each must be a concrete stated assumption, not background prose.
This section must appear in the final paper before the Hypothesis section.

The Lead Author reads the Status Quo section before writing anything.

---

### Phase 3: Write the Paper

Lead Author writes all sections. The Status Quo section from Phase 2 is inserted verbatim
at position 2 (after Abstract, before Hypothesis). Do not edit it.

**Required sections (in this order):**

**1. Abstract** (<200 words)
Write it as the only thing a future researcher may read: (a) question investigated,
(b) method, (c) key finding, (d) practical implication. Do not describe structure.
A reader who reads only this can state what was investigated, how, and what was found.

**2. Status Quo** (paste verbatim from Phase 2 — do not edit)

**3. Hypothesis**
`H-01: [hypothesis text verbatim from artifact] (source: [file path])`
If the hypothesis was amended during investigation: state original and final form.

**4. Method**
Which prove skills ran. What artifacts were produced. Why evidence was gathered this way.
Cold-start readable: define any domain-specific terms on first use.

**5. Evidence**
Every claim cites a named artifact:
`- E-[N]: [claim] [source: file-path.md, section or item ID]`
Uncitable claims go to Limitations, not here. Record them:
`UNCITABLE: [claim] — moved to Limitations, no artifact source`
Minimum 3 cited claims.

**6. Findings**

HYPOTHESIS VERDICT: [Confirmed | Refuted | Partially confirmed under X but not Y]
Rationale: [One sentence citing specific evidence items by E-ID.]

For each finding, classify it against the Status Quo baseline before writing the conclusion:

```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion — judgment, pattern, or causal claim answering "what does this mean?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

Tag rules:
- BASELINE MATCH: finding confirms an assumption listed in Status Quo (cite B-ID)
- NEW SIGNAL: finding challenges, extends, or contradicts a Status Quo assumption (cite B-ID)
  or introduces something not in Status Quo at all (cite as "not in prior baseline")

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not derivable from the Status Quo baseline.
```

If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions. This paper validates the baseline.
Future work should target: [gap where Status Quo assumptions may not hold].
```

**7. Principles**
Minimum 2 numbered rules. Action-oriented: "Always X", "When Y, do Z", "Prefer A over B."
Each cites its finding: `P-01 [from F-02]: ...`
Each is tagged: `[EXTENDS BASELINE]` (refines a prior assumption) or
`[REPLACES BASELINE]` (contradicts a prior assumption).

**8. Limitations**
What this investigation did not cover. What cannot be concluded.
Uncitable claims from Evidence appear here: "These observations lacked artifact support:
[UNCITABLE items]."

**9. Future Work**
Minimum 2 specific investigable questions. At least one targets a gap in the Status Quo
assumptions. Specific enough that a team could start without further clarification.
Failing form: "More research is needed on X."
Passing form: "Investigate whether [B-01 assumption] holds when [condition changed],
using [specific method]."

---

### Phase 4: Panel Review

**Domain Expert:**
Assesses domain accuracy of Evidence and Findings. Also assesses whether the Status Quo
baseline is accurately stated (not strawmanned or overstated).
One substantive critique or endorsement. Score: [N/10 domain accuracy]

**Practitioner:**
Assesses whether principles are actionable by a working team without reading the full paper.
One substantive critique or endorsement. Score: [N/10 practical applicability]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 5: Amend

```
AMENDMENT A-01: [Section] — [What changed] — [Triggered by: user / Domain Expert / Practitioner]
```

After amendments, re-run the Findings novelty check: confirm all findings still carry
BASELINE MATCH or NEW SIGNAL tags consistent with the Status Quo section.

---

### Output

Write the paper to: `simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-02: Citation-Gate

**Axis:** Lifecycle emphasis — citation audit is a required output block, not a guideline;
the Findings section is locked until the audit shows zero uncited claims
**Hypothesis:** R1 V-03 (evidence-first) scored 59/100 — it enforced the right lifecycle
order but failed as a single-axis experiment that dropped coverage elsewhere. V-02 takes
the R1 V-03 insight (cite-before-conclude) and integrates it into a full-coverage prompt
that keeps all essential criteria while making the citation audit a mandatory, machine-verifiable
gate. C-13 becomes not just a guideline but a literal output block that either passes or
stops the session. The bet: a hard stop at Evidence that requires a passing audit report
before Findings unlocks is the strongest possible C-13 enforcement — and V-01 R1 proved
all essentials can coexist with strong lifecycle enforcement.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review).

**Citation gate rule:** The Findings section may not begin until a CITATION AUDIT block
appears in the output showing zero uncited claims. This is a hard stop enforced by structure —
if the audit block is missing or shows uncited claims > 0, the paper is incomplete.

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

If no hypothesis found: stop. Do not proceed without a stated hypothesis.

---

### Phase 2: Evidence Section (Written Before All Other Sections)

Write the Evidence section now — before Abstract, before Findings, before all other sections.

Citation format (required for every claim):
`E-[N]: [claim text] [source: file-path.md, section or item ID]`

Number every evidence item E-01, E-02, ... These IDs will be referenced in the Verdict
and Findings sections.

For any claim you cannot cite: do not include in Evidence. Record it:
`UNCITABLE (moved to Limitations): [claim text — no source available]`

When Evidence is complete, output the citation audit:

```
CITATION AUDIT
Evidence items total: [N]
Items with citation anchor: [N]
Items without citation anchor: [must be 0]
Uncitable claims recorded for Limitations: [N]
Status: [PASS — proceed to Findings] or [BLOCKED — [N] uncited claims remain]
```

If Status is BLOCKED: fix citations or move claims to Limitations.
Do not move to Phase 3 until the citation audit shows Status: PASS.

---

### Phase 3: Hypothesis Verdict

With Evidence complete and audited, state the verdict before writing any finding:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [Cite 2-3 E-IDs that most directly support this verdict]
Full verdict sentence: "[One quotable sentence: 'The hypothesis was confirmed: E-03 and
E-05 demonstrate that...' — no evasions accepted]"
```

Accepted verdict forms:
- "The hypothesis was confirmed: [evidence basis citing E-IDs]."
- "The hypothesis was refuted because [evidence basis citing E-IDs]."
- "Partially confirmed under [condition X] (E-01, E-04) but not under [condition Y] (E-02)."
Not accepted: "The evidence is mixed." / "Further investigation is needed."

---

### Phase 4: Write All Paper Sections

Write sections in this order. Evidence (from Phase 2) and Verdict (from Phase 3) are inserted
at their positions — do not rewrite them.

**1. Abstract** (<200 words)
Written now that the verdict is known. State: question, method, key finding, implication.
Do not describe paper structure. A reader who reads only this can act on it.

**2. Status Quo**
What the team believed before this investigation. Minimum 2 concrete prior assumptions:
`- [B-01: prior belief]`
`- [B-02: prior belief]`
State what the default action would have been without this investigation.
This section precedes the Hypothesis.

**3. Hypothesis** (from Phase 3 verdict block — H-01 text + source path)

**4. Method**
Prove skills run. Artifacts produced. Why evidence was gathered this way.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (paste from Phase 2 — all E-[N] items with citations)

Evidence complete marker (required):
```
EVIDENCE COMPLETE: Citation audit passed. [N] items, all anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**
The HYPOTHESIS VERDICT from Phase 3 appears first.

Then findings as interpreted conclusions:
```
F-01 [BASELINE MATCH / NEW SIGNAL]: [conclusion answering "what does this mean?", not "what happened?"]
F-02 [BASELINE MATCH / NEW SIGNAL]: [conclusion]
F-03 [BASELINE MATCH / NEW SIGNAL]: [conclusion]
```

BASELINE MATCH = confirms a prior assumption from Status Quo.
NEW SIGNAL = challenges or extends it.
Minimum 3 findings. At least one NEW SIGNAL if evidence supports it.

**7. Principles**
Minimum 2 numbered action-oriented rules.
Form: "Always X", "When Y, do Z", "Prefer A over B because..."
Each cites its finding: `P-01 [from F-02]: ...`

**8. Limitations**
What the investigation did not cover. Include uncitable claims from Phase 2:
"The following observations were noted but could not be supported by available artifacts:
[UNCITABLE items]."

**9. Future Work**
Minimum 2 specific investigable questions.
Form: "Investigate whether X holds when Y, using method Z."
Failing form: "More research is needed."

---

### Phase 5: Panel Review

**Domain Expert:**
Critiques Evidence accuracy and Findings quality.
One substantive critique or endorsement. Score: [N/10]

**Practitioner:**
Critiques Principles actionability.
One substantive critique or endorsement. Score: [N/10]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 6: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner]
```

If Evidence is amended: re-run CITATION AUDIT and update the Evidence complete marker.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-03: Novelty-Pre-Classification

**Axis:** Output format — each finding is classified BASELINE MATCH or NEW SIGNAL before
its conclusion text is written; classification commits first, prose follows
**Hypothesis:** C-11 (findings classified by novelty) is aspirational because in most prompts
it is appended after findings are written. Pre-classifying each finding before writing its
conclusion inverts this: the author must decide "is this new?" before deciding what to say.
This prevents the drift where a finding sounds novel but is actually a Status Quo restatement
dressed in conclusion language. If the author must commit to BASELINE MATCH or NEW SIGNAL
first, BASELINE MATCH findings will be written more honestly as confirmations rather than
disguised as discoveries. C-04 (synthesis quality) should also improve: the classification
forces interpretation mode before writing each finding.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author (paper writer), Domain Expert (review), Practitioner (review).

**Novelty-first rule:** Before writing any finding, the Lead Author declares its novelty
classification (BASELINE MATCH or NEW SIGNAL). The classification is committed first; the
finding text then follows that classification. Reclassification after writing the finding
is not permitted without stating a reason. If all findings are BASELINE MATCH, the paper
is flagged before panel review.

---

### Phase 1: Artifact Load

Read all prove artifacts under `simulations/prove/` for the topic:
- hypothesis, analysis, interview, websearch, synthesize

Disclose before proceeding:

```
Artifacts loaded:
- hypothesis: [file path or "not found"] (H-01: "[text excerpt]")
- analysis: [file path, N findings noted]
- interview: [file path or "not found"]
- websearch: [file path or "not found"]
- synthesize: [file path or "not found"]
```

If no hypothesis found: stop. Supply hypothesis before proceeding.

---

### Phase 2: Prior Belief Inventory

Before writing the paper, inventory what was assumed before this investigation.
This becomes the Status Quo section.

```
PRIOR BELIEF INVENTORY:
B-01: [concrete prior assumption about this topic]
B-02: [concrete prior assumption]
B-03: [optional — additional assumption]

Investigation trigger: "This investigation was motivated by: [gap or tension in the above
that H-01 was designed to resolve]."
```

---

### Phase 3: Hypothesis Verdict

State the verdict before Findings classification begins:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Rationale: [One sentence citing named artifacts or evidence items]
```

No evasive forms accepted. The verdict is a commit, not a hedge.

---

### Phase 4: Findings Classification Scaffold (Before Prose)

For each finding the investigation supports, classify before writing any conclusion text.
This phase produces the classification scaffold. Prose follows in Phase 5.

Classification instructions:
- BASELINE MATCH: this finding confirms one or more of the prior beliefs from Phase 2
  (cite which: B-01, B-02, etc.)
- NEW SIGNAL: this finding challenges, extends, or contradicts a prior belief (cite which)
  OR introduces something the prior belief inventory did not anticipate (cite as B-NONE)

```
FINDING CLASSIFICATION SCAFFOLD:
F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / introduces B-NONE]
F-02: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / introduces B-NONE]
F-03: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / introduces B-NONE]
[Add F-04, F-05 if evidence supports]
```

NEW SIGNAL check: if all classifications are BASELINE MATCH, output:
```
NEW SIGNAL CHECK: Zero new signals found. All findings confirm prior assumptions.
Risk: C-04 — are these synthesized conclusions or data restatements?
Proceeding with INERTIA FLAG in Findings section.
```

At least one NEW SIGNAL is expected for a paper to claim investigation value. The author
may proceed with all BASELINE MATCH but must acknowledge this explicitly.

---

### Phase 5: Write the Paper

Write all sections. Classifications from Phase 4 are embedded in Findings — do not change
them without stating a reclassification reason.

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.)

**2. Status Quo** (formalize the Phase 2 prior belief inventory)
```
## Status Quo
Before this investigation, the following was assumed:
- [B-01 text]
- [B-02 text]
This investigation was motivated by: [trigger from Phase 2].
```
Minimum 2 prior beliefs. Concrete assumptions, not background prose.

**3. Hypothesis** (H-01 from Phase 3 verdict block + source file path)

**4. Method**
Prove skills run. Artifacts produced. Why this approach. Cold-start readable.
Define domain-specific terms on first use.

**5. Evidence**
Numbered cited claims:
`E-[N]: [claim] [source: file-path.md, section or item ID]`
Uncitable claims moved to Limitations.
Minimum 3 cited claims.

**6. Findings**
The HYPOTHESIS VERDICT line from Phase 3 appears first.

Then findings, using the classification scaffold from Phase 4:
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" not "what happened?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If any NEW SIGNAL finding is present:
```
CONTRIBUTION: F-[xx] is this paper's primary contribution — not predictable from
the Status Quo baseline.
```

If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions. Future work should investigate:
[gap in B-01/B-02 assumptions].
```

**7. Principles**
Minimum 2 numbered rules. Action-oriented form required.
Each cites its finding: `P-01 [from F-02]: ...`
Tag each: [EXTENDS BASELINE] or [REPLACES BASELINE].

**8. Limitations**
What was not covered. What cannot be concluded.
Uncitable claims from Evidence phase appear here.

**9. Future Work**
Minimum 2 specific investigable questions, specific enough to start.

---

### Phase 6: Panel Review

**Novelty Audit** (Lead Author self-check before panel):
```
NOVELTY AUDIT:
Total findings: [N]
BASELINE MATCH: [N]
NEW SIGNAL: [N]
Primary contribution: [F-xx or "none — baseline validation only"]
```

**Domain Expert:**
Assesses domain accuracy and whether the Status Quo baseline is correctly stated.
Score: [N/10]

**Practitioner:**
Assesses principles actionability.
Score: [N/10]

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 7: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner]
```

If a finding classification is amended, state the reclassification reason explicitly.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-04: Full Integration (V-01 Excellence + R2 Aspirationals)

**Axis:** Combined — V-01 R1 excellence signals (artifact disclosure, Skeptic pre-flight,
forced verdict sentence, uncitable-claim routing) + all three R2 aspirationals as structural
phases: Status Quo (C-12), citation audit gate (C-13), novelty tagging (C-11)
**Hypothesis:** V-01 scored 96/100 without C-11/C-12/C-13 (which didn't exist in R1 rubric).
If V-01's scaffold is correct, adding C-12 (Status Quo as Phase 2), C-13 (citation audit gate
before Findings), and C-11 (novelty tag on every finding) should reach the R2 rubric ceiling.
The risk is over-engineering — too many phases may produce a prompt that is structurally
complete but too complex to follow reliably. The counter-bet: each R2 addition maps cleanly
to a discrete phase that already exists in V-01's structure. Status Quo extends the Skeptic
pre-flight. Citation audit extends the Evidence section gate. Novelty tagging extends the
Findings format. None require new phases — they extend existing ones.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight + post-evidence audit), Lead Author (paper writer),
Domain Expert (review), Practitioner (review).

**Three structural rules (non-negotiable):**
1. Status Quo section produced by Skeptic before any paper section is written (C-12).
2. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13).
3. Every finding carries a BASELINE MATCH or NEW SIGNAL tag (C-11).

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

If hypothesis not found: stop. Output:
```
Cannot publish: hypothesis artifact required at simulations/prove/hypothesis/*.
Run /prove:hypothesis first.
```

---

### Phase 2: Skeptic Pre-Flight

Skeptic runs before the Lead Author writes a single section.

**Part A: Pre-flight checklist**
```
SKEPTIC PRE-FLIGHT:
[ ] H-01 hypothesis — will verify Findings resolves it with an explicit verdict sentence.
[ ] Evidence traceability — will flag any claim without a named artifact citation.
[ ] Findings synthesis quality — will verify each finding answers "what does this mean?"
[ ] Principles actionability — will verify each principle is a rule, not a vague summary.
[ ] New signal check — will verify at least one finding diverges from Status Quo.

Prediction: [specific anticipated failure given the artifacts loaded — one sentence]
Watch point: [one section most at risk, with reason]
```

**Part B: Status Quo section (final version — inserted verbatim into paper)**
```
## Status Quo
Before this investigation began, a team in this area would likely have assumed:
- [B-01: Assumption 1 — what conventional understanding says]
- [B-02: Assumption 2 — what adjacent domain knowledge suggests]
- [B-03: Assumption 3 — the team's prior working assumption]

This investigation was motivated by: [gap or tension in the above that H-01 addresses].

Without this investigation, the default action would have been: [what team would have done
relying on these assumptions alone].
```

Minimum 2 concrete assumptions. This text is final — Lead Author does not edit it.

The Lead Author reads both parts before writing.

---

### Phase 3: Evidence (Written Before Findings)

Lead Author writes the Evidence section now, before Abstract and before Findings.

Citation format:
`E-[N]: [claim] [source: file-path.md, section or item ID]`

For any claim that cannot be cited:
`UNCITABLE: [claim text] — moved to Limitations`

When Evidence is complete, output the citation audit:

```
CITATION AUDIT
Total evidence items: [N]
Items with citation anchor: [N]
Items without citation anchor: [must be 0 to proceed]
Uncitable claims moved to Limitations: [N]
Status: [PASS — Findings unlocked] or [BLOCKED — [N] uncited claims remain]
```

Do not proceed to Phase 4 until Status shows PASS.

---

### Phase 4: Hypothesis Verdict

With Evidence audited, commit to the verdict before writing Findings:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [cite E-IDs that most directly support the verdict]
Full verdict sentence: "[One quotable sentence: 'The hypothesis was confirmed: E-03 and
E-05 show that...']"
```

Not accepted: "The evidence is mixed." / "Further investigation is needed." The verdict
is a commit with evidence basis, not a hedge.

---

### Phase 5: Write the Paper

Lead Author writes all sections. Phase 2 Part B (Status Quo) and Phase 3 (Evidence) are
inserted verbatim — do not rewrite them.

**1. Abstract** (<200 words)
Written now that the verdict is known. State: question, method, key finding, implication.
Not structure. Written as if it is the only thing a future researcher reads.

**2. Status Quo** (paste verbatim from Phase 2 Part B)

**3. Hypothesis**
`H-01: [text] (source: [file path])`
If hypothesis was amended during investigation: state original and final form.

**4. Method**
Prove skills run. Artifacts produced. Why this approach was chosen.
Cold-start readable: define domain-specific terms on first use.

**5. Evidence** (paste from Phase 3 — E-[N] numbered items with citations)

Evidence complete marker (required):
```
EVIDENCE COMPLETE: Citation audit passed. [N] items anchored.
[N] uncitable claims moved to Limitations.
```

**6. Findings**
HYPOTHESIS VERDICT from Phase 4 appears first.

Then findings as interpreted conclusions. Each carries a novelty tag:

```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion answering "what does this mean?" not "what happened?"]

F-02 [NEW SIGNAL — contradicts B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

Tag rules:
- BASELINE MATCH: confirms an assumption from Status Quo (cite B-ID)
- NEW SIGNAL: challenges, extends, or contradicts a Status Quo assumption (cite B-ID)
  OR introduces something not in Status Quo (cite as "not in prior baseline")

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not predictable from the Status Quo baseline.
```

If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions. This paper validates the baseline.
Future work should investigate: [the gap the Skeptic's Status Quo baseline identified].
```

**7. Principles**
Minimum 2. Numbered. Action-oriented: "Always X", "When Y, do Z", "Prefer A over B."
Each cites its finding: `P-01 [from F-02]: ...`
Each tagged: `[EXTENDS BASELINE]` or `[REPLACES BASELINE]`.

**8. Limitations**
What was not covered. What cannot be concluded.
Uncitable claims from Phase 3: "The following claims lacked artifact support: [items]."

**9. Future Work**
Minimum 2 specific investigable questions. At least one targets a gap in the Status Quo
baseline. Specific enough to start without clarification.

---

### Phase 6: Panel Review

**Domain Expert:**
Reviews Evidence accuracy and Findings quality. Also reviews Status Quo accuracy
(were the prior assumptions correctly stated?).
One substantive critique or endorsement. Score: [N/10 domain accuracy]

**Practitioner:**
Reviews Principles actionability. Could a working team apply these without the full paper?
One substantive critique or endorsement. Score: [N/10 practical applicability]

**Skeptic Post-Review:**
```
SKEPTIC POST-REVIEW:
Pre-flight items resolved: [N/5]
Citation audit: [PASS / fail reason]
New signal count: [N findings tagged NEW SIGNAL]
Prediction outcome: [CONFIRMED / RESOLVED / STILL PRESENT — one sentence]
Overall: [APPROVED / FLAG: reason]
```

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 7: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

If Evidence is amended: re-run citation audit. Update Evidence complete marker.
If findings are reclassified: state reclassification reason explicitly.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-05: Dual-Skeptic (Split Intervention)

**Axis:** Role sequence — two distinct Skeptic interventions at different lifecycle gates:
Pre-Skeptic (before authoring: Status Quo + pre-flight risk), Post-Skeptic (after Evidence:
citation audit + novelty classification scaffold for Lead Author)
**Hypothesis:** In V-01 R1, the Skeptic ran pre-flight and then appeared in panel review —
a pre-flight risk namer and a post-completion reviewer. Neither instance audited citations
or classified finding novelty. Splitting the Skeptic into two role invocations at different
lifecycle gates separates the cognitive load: Pre-Skeptic sets up the baseline (C-12),
Post-Skeptic performs the audit (C-13) and stages the novelty classification for the author
(C-11). The Lead Author writes between these two interventions. This design prevents the dual
role from becoming ambiguous — each Skeptic instance has exactly one job and one output
format. V-04 handles all three R2 aspirationals in a single Skeptic instance; V-05 bets that
splitting produces cleaner execution with less role-drift between baseline-setting and auditing.

```
You are running /prove:publish for Signal.

Stock roles: Pre-Skeptic (baseline + pre-flight), Lead Author (Evidence + paper body),
Post-Skeptic (citation audit + novelty staging), Domain Expert (review), Practitioner (review).

**Session order:** Pre-Skeptic → Lead Author writes Evidence → Post-Skeptic →
Lead Author writes remaining sections → Panel Review.

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

If no hypothesis: stop. Do not proceed.

---

### Phase 2: Pre-Skeptic

Pre-Skeptic runs first. Two outputs.

**Output A: Pre-Flight Checklist**
```
PRE-SKEPTIC PRE-FLIGHT:
[ ] H-01 hypothesis — will verify Findings resolves it with an explicit verdict sentence.
[ ] Evidence traceability — will verify citation audit passes before Findings begins.
[ ] Findings synthesis — will verify each finding is a conclusion, not a data restatement.
[ ] Principles actionability — will verify each principle is a rule, not a vague statement.
[ ] New signal — will verify at least one finding diverges from the baseline.

Prediction: [most likely failure point in this paper — one specific sentence]
```

**Output B: Status Quo Section (final version, inserted verbatim into paper)**
```
## Status Quo
Before this investigation, a team working in this area would likely have assumed:
- [B-01: Concrete prior belief 1]
- [B-02: Concrete prior belief 2]
- [B-03: Optional assumption 3]

This investigation was motivated by: [gap or tension that H-01 was designed to resolve].

Without investigating H-01, the team would have: [stated default action].
```

Minimum 2 concrete prior beliefs. Not background prose.
This is the final Status Quo text — Lead Author inserts it verbatim. Do not edit.

Lead Author reads both outputs before writing.

---

### Phase 3: Lead Author — Evidence Section Only

Lead Author writes only the Evidence section now. Stop after Evidence is complete.

Citation format:
`E-[N]: [claim] [source: file-path.md, section or item ID]`

For any claim that cannot be cited: record separately and do not include in Evidence:
`HOLD (uncitable): [claim] — no artifact source available`

Write all evidence items. Stop. Pass to Post-Skeptic.

---

### Phase 4: Post-Skeptic

Post-Skeptic performs two tasks on the Evidence from Phase 3.

**Task A: Citation Audit**
```
POST-SKEPTIC CITATION AUDIT:
Evidence items reviewed:
  E-01: [CITED — source: file.md] or [UNCITED — move to Limitations]
  E-02: [CITED — source: file.md] or [UNCITED — move to Limitations]
  [continue for all items]
Total: [N] | Cited: [N] | Uncited (must be 0): [N]
Status: [PASS] or [BLOCKED — [N] uncited items, listed above]
```

If BLOCKED: specify which items need citations. Lead Author must fix before Phase 5.

**Task B: Novelty Classification Scaffold**
Review the artifacts and produce the finding classification for the Lead Author.
The scaffold commits to what each finding will be before the Lead Author writes it.

```
POST-SKEPTIC NOVELTY SCAFFOLD:
Status Quo baseline: B-01, B-02[, B-03] (from Phase 2)

Expected finding classifications:
F-01: [BASELINE MATCH — confirms B-XX] or [NEW SIGNAL — challenges B-XX / B-NONE]
  Evidence basis: [E-IDs supporting this classification]
F-02: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]
F-03: [BASELINE MATCH / NEW SIGNAL]
  Evidence basis: [E-IDs]

NEW SIGNAL CHECK: [N] expected new signals out of [N] findings.
If 0: "All expected findings confirm prior assumptions — flag for scope reconsideration."
```

The Lead Author uses this scaffold. Classifications are set. To reclassify: state reason.

---

### Phase 5: Hypothesis Verdict

Lead Author commits to the verdict after Evidence is audited:

```
HYPOTHESIS VERDICT
H-01: [text] (source: [file path])
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [E-IDs]
Full verdict sentence: "[Quotable committed sentence]"
```

---

### Phase 6: Lead Author — Write All Remaining Sections

**1. Abstract** (<200 words: question, method, key finding, implication. Not structure.)

**2. Status Quo** (paste verbatim from Phase 2 Output B)

**3. Hypothesis** (from Phase 5 verdict block — H-01 text + source path)

**4. Method** (Skills run, artifacts produced, why this approach. Cold-start readable.)

**5. Evidence** (paste from Phase 3, verified by Post-Skeptic audit)

Evidence complete marker:
```
EVIDENCE COMPLETE: Post-Skeptic citation audit passed. [N] items.
[N] uncitable claims moved to Limitations.
```

**6. Findings**
HYPOTHESIS VERDICT from Phase 5 first.

Then findings using the Post-Skeptic novelty scaffold from Phase 4:
```
F-01 [BASELINE MATCH — confirms B-01]:
[conclusion — judgment, pattern, or causal claim answering "what does this mean?"]

F-02 [NEW SIGNAL — challenges B-02]:
[conclusion]

F-03 [BASELINE MATCH — confirms B-01]:
[conclusion]
```

If at least one NEW SIGNAL:
```
CONTRIBUTION: F-[xx] is the primary contribution — not predictable from Status Quo.
```

If all BASELINE MATCH:
```
INERTIA FLAG: All findings confirmed prior assumptions.
Future work target: [gap from Status Quo baseline].
```

**7. Principles**
Minimum 2 numbered action-oriented rules.
Each cites its finding: `P-01 [from F-02]: ...`
Accepted forms: "Always X", "When Y, do Z", "Prefer A over B because..."

**8. Limitations**
Scope boundaries. Uncitable claims from Phase 3 appear here.

**9. Future Work**
Minimum 2 specific investigable questions. At least one targets a gap from the Status Quo.

---

### Phase 7: Panel Review

**Domain Expert:**
Reviews Evidence accuracy and Status Quo baseline correctness.
One substantive critique or endorsement. Score: [N/10]

**Practitioner:**
Reviews Principles actionability.
One substantive critique or endorsement. Score: [N/10]

**Pre-Skeptic Check-In:**
```
PRE-SKEPTIC FINAL:
Pre-flight items resolved: [N/5]
Prediction outcome: [CONFIRMED / RESOLVED / STILL PRESENT — one sentence]
```

```
DOMAIN EXPERT: [critique] — Score: [N/10]
PRACTITIONER: [critique] — Score: [N/10]
```

---

### Phase 8: Amend

```
AMENDMENT A-01: [Section] — [Change] — [Triggered by: user / Domain Expert / Practitioner / Pre-Skeptic]
```

If Evidence is amended: re-run Post-Skeptic citation audit. Update Evidence complete marker.
If finding classification changes: state reclassification reason. Update novelty scaffold.

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```
