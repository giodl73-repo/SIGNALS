## prove-interview — Variations V-01 through V-05 (Round 6)

---

## V-01 — Axis: Role Sequence (Skeptic-First Ordering)
**Hypothesis:** Starting with the skeptic establishes friction as the evidential baseline; subsequent subjects are explicitly measured against it, making C-23 evidential-function declarations and C-24 synthesis weighting fall out naturally from the sequencing logic itself.

---

```markdown
# /prove:interview — Stakeholder Interview Simulation

You are simulating stakeholder interviews for the feature topic: **{topic}**

Interview a minimum of two subjects. The sequence is deliberate and fixed:

**Required sequence order:**
1. Skeptic or friction-holder first — their objections become the evidential baseline
2. Neutral or evaluator second — they assess claims without prior commitment
3. Advocate or champion last (if present) — their support is weighed against the baseline

State the sequencing rationale in one sentence before the first subject card. Example:
> "Sequence: skeptic-first, so their friction is the evidential baseline all subsequent interviews are measured against."

---

## PRE-INTERVIEW SETUP

Before any interview begins, for EACH subject, write a Subject Card:

```
SUBJECT CARD — [Subject Name or Role]
Role / Title: [explicit]
Evidential Function: [what this subject's position DOES for the evidence structure — not who they are, but what structural job they perform. E.g., "establishes the friction floor that advocate claims must clear", "provides feasibility ground-truth from implementation experience", "challenge surface for surface-level objections"]
Vocabulary Signature: [2–3 role-specific terms this person uses — auditable against their answers]
Prior Knowledge: [what they know about this feature area]
Blind Spots: [what they have not seen, experienced, or been exposed to]
Disposition: [skeptic / neutral / advocate / undecided]
Epistemic Standing: [GROUNDED = direct operational experience | CONDITIONAL = informed but hasn't encountered the alternative | INFERRED = reasoning from adjacent domain]
```

Then write an Expectation Register for each subject — before the transcript starts:

```
EXPECTATION REGISTER — [Subject Name or Role]
Expected to say: [specific claim, concern, or objection you anticipate]
Expected to miss: [what they probably won't surface given their blind spots]
Expected to confirm: [what you expect them to validate based on their role]
```

Phase 1 complete when: every subject has a Subject Card AND an Expectation Register. Do not begin transcripts until this gate is passed.

---

## INTERVIEW TRANSCRIPTS

For each subject in sequence order:

**Format:**
- Questions probe the subject's declared role-specific concerns — not generic topics
- At least one follow-up question references a specific phrase from the subject's preceding answer: `triggered by: "[exact phrase from prior answer]"`
- Answers are written in the subject's distinct voice — vocabulary signature terms should appear naturally
- Each answer uses vocabulary from the subject's declared Vocabulary Signature at least once

**Moment Labeling (required within the transcript):**
When a notable moment occurs, label it inline:

```
SURPRISING (expected: [what the Expectation Register said], got: [what actually emerged])
CONFIRMING (validates: [which expectation was met])
INCONCLUSIVE (moment is notable but neither confirms nor surprises — name why)
```

At least one labeled moment per subject. Every notable moment must be labeled — do not leave interesting moments unlabeled.

Phase 2 complete when: every subject has a transcript with at least one follow-up anchored to a prior answer and at least one labeled moment. Do not begin extraction until this gate is passed.

---

## EVIDENCE EXTRACTION

After each transcript, extract evidence items in this format:

```
EVIDENCE ITEM [N]
Claim: [what the subject said or implied]
Signal Type: [adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation | contradiction]
Strength: [strong | moderate | weak]
Strength Rationale: [one sentence naming why — what made it reliable, hedged, or ambiguous]
Basis: [verbatim (quoted from transcript) | inferred (implied but not stated) | corroborated (consistent across subjects)]
Epistemic Standing of Source: [GROUNDED | CONDITIONAL | INFERRED — copied from Subject Card]
```

Phase 3 complete when: every subject has at least one evidence item with all fields populated.

---

## CROSS-INTERVIEW SYNTHESIS

Write a synthesis section after all transcripts and extractions.

The synthesis must:

1. **Name the evidential baseline** — state the skeptic's core objection as the baseline claim
2. **Track objection fate** — state whether the skeptic's objection *persisted*, *transformed*, or *was resolved* by the final interview. Trace its movement: do not merely say subjects "agreed" or "disagreed"
3. **Weight by epistemic standing** — for at least one evidence item, explicitly invoke its standing to adjust weight. Required form: `"[Subject]'s objection that [X] is CONDITIONAL — they have not experienced [Y]; treat as a risk to monitor, not a blocker"` or equivalent. Do not treat CONDITIONAL and GROUNDED evidence as equivalently weighted without acknowledgment
4. **Name convergences and contradictions** — at least one pattern (where subjects agree) and one tension (where they diverge)
5. **Composite signal** — one paragraph naming what the combined evidence says about the feature's readiness

Phase 4 complete when: synthesis names the baseline, tracks objection fate, invokes epistemic standing explicitly, and closes with a composite signal.

---

## SIMULATION FIDELITY NOTE

End with a brief meta-note:
- Name at least one specific basis for grounded claims (documented persona knowledge, domain context, or role convention)
- Name at least one constructed plausibility element (where you extrapolated beyond documented context)
- Name one concrete contrast in how two subjects sound different — cite a specific vocabulary choice, framing preference, or concern priority

---

**Topic:** {topic}
**Feature context (if provided):** {context}
```

---

## V-02 — Axis: Output Format (Structured Card + Table Format)
**Hypothesis:** Embedding all required fields as explicit table columns and named card sections forces population of C-13 (expectation register), C-22 (vocabulary signature), C-23 (evidential function), and C-18 (basis declaration) without relying on the author to remember them — the format is the checklist.

---

```markdown
# /prove:interview — Stakeholder Interview Simulation

Simulate persona-driven stakeholder interviews for: **{topic}**

The output follows a strict structural format. Every section header, every table column, and every labeled field is a required output — not a suggestion. Skipping a field is a rubric failure.

---

## SECTION 0 — SEQUENCE DECLARATION

State in one sentence why subjects appear in the given order. Name the sequencing logic:
> "Sequence: [logic — e.g., skeptic-first to surface objections before advocates; influence-map order; neutral-first to establish baseline]"

---

## SECTION 1 — SUBJECT CARDS

Write one card per subject. Minimum two subjects with meaningfully different roles.

| Field | Subject A | Subject B | Subject C (if present) |
|-------|-----------|-----------|----------------------|
| **Role / Title** | | | |
| **Evidential Function** | | | |
| **Vocabulary Signature** | (2–3 terms) | (2–3 terms) | (2–3 terms) |
| **Prior Knowledge** | | | |
| **Blind Spots** | | | |
| **Disposition** | skeptic / neutral / advocate / undecided | | |
| **Epistemic Standing** | GROUNDED / CONDITIONAL / INFERRED | | |

**Evidential Function field instructions:** Name what this subject's position *does* for the evidence structure — their structural job in the investigation. Not their role title. Not their disposition. Their contribution to the evidence chain. Examples:
- "Friction baseline: establishes the floor of objections all other interviews are measured against"
- "Feasibility probe: ground-truth from implementation realities the spec team has not encountered"
- "Challenge surface: tests whether advocate claims survive informed skepticism"

---

## SECTION 2 — EXPECTATION REGISTERS

Write one register per subject BEFORE any transcript begins.

| Expectation | Subject A | Subject B | Subject C |
|-------------|-----------|-----------|-----------|
| **Expected to say** | | | |
| **Expected to miss** | | | |
| **Expected to confirm** | | | |

Gate: Section 2 is complete when every cell is populated. Do not begin Section 3 until this table is complete.

---

## SECTION 3 — INTERVIEW TRANSCRIPTS

For each subject, run the interview in this structure:

**[Subject Role] Interview**

*Opening question:* [Question anchored to this subject's declared prior knowledge and concerns]

> **[Subject]:** [Answer in the subject's voice — vocabulary signature terms present]

*Follow-up:* `triggered by: "[exact phrase from prior answer]"` — [Follow-up question]

> **[Subject]:** [Answer]

*[Additional exchanges as needed — minimum one follow-up per subject]*

**Moment Labels (inline, immediately following the relevant answer):**
```
SURPRISING (expected: [from Expectation Register], got: [what emerged])
CONFIRMING (validates: [which register expectation])
INCONCLUSIVE (notable but unresolvable — reason: [why it fits neither category])
```

At least one label per subject. Label every notable moment — leave no interesting exchange unlabeled.

Gate: Section 3 complete when every subject has a transcript with a labeled moment and at least one follow-up containing `triggered by:`.

---

## SECTION 4 — EVIDENCE EXTRACTION TABLE

| # | Claim | Signal Type | Strength | Strength Rationale | Basis | Source Standing |
|---|-------|-------------|----------|--------------------|-------|-----------------|
| E-01 | | adoption risk / feasibility concern / requirement gap / scope signal / constraint / validation / contradiction | strong / moderate / weak | [why] | verbatim / inferred / corroborated | GROUNDED / CONDITIONAL / INFERRED |
| E-02 | | | | | | |

Minimum one row per subject. The `Source Standing` column is copied from the subject's Epistemic Standing field in Section 1.

Gate: Section 4 complete when every row has all columns populated.

---

## SECTION 5 — CROSS-INTERVIEW SYNTHESIS

### 5a. Evidential Baseline
State the skeptic subject's core objection as the baseline claim. One sentence.

### 5b. Objection Fate
Track the objection's movement across interviews. Did it *persist* (reached the final interview unchanged), *transform* (shifted in character), or *was it resolved* (closed by evidence or concession)?
Do not assert subjects "agreed" or "disagreed" — trace the objection's movement.

### 5c. Epistemic-Weighted Evidence
Select at least one evidence item where epistemic standing affects weight. Apply this formula:
> "[Item] from [Subject]: standing is [GROUNDED / CONDITIONAL / INFERRED] because [basis]. Weight: [full weight as blocker / risk to monitor / flag for future validation] — [one sentence explaining the adjustment]."

CONDITIONAL items are not blockers. INFERRED items flag future validation needs. GROUNDED items carry full evidential weight. Name this explicitly.

### 5d. Convergences and Contradictions
- Pattern (convergence): [what subjects agreed on]
- Tension (contradiction): [where they diverged — name the specific claims in conflict]

### 5e. Composite Signal
One paragraph. What does the combined evidence say about the feature's investigation status?

---

## SECTION 6 — META-NOTES

**Simulation Fidelity:** Name one grounded claim basis (documented knowledge, domain convention, or role-specific expertise), and one constructed plausibility element (extrapolated beyond documented context).

**Voice Divergence:** Name one concrete contrast between two subjects — cite a specific vocabulary choice, framing, or concern priority that distinguishes them. Generic statements ("they had different roles") fail.

---

**Topic:** {topic}
**Feature context (if provided):** {context}
```

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Gates with Completion Conditions)
**Hypothesis:** Making every phase transition conditional on explicit gate criteria prevents the common failure mode of rushing to synthesis before extraction is complete — and forces C-20 (phase completion gating) to be satisfied structurally rather than aspirationally.

---

```markdown
# /prove:interview — Stakeholder Interview Simulation

Topic: **{topic}**

This skill runs in five gated phases. Each phase ends with a completion gate. You must state the gate explicitly before moving to the next phase. Do not proceed if a gate condition is unmet — fill the gap first.

---

## PHASE 0: INVESTIGATION SETUP

**Purpose:** Establish the interview context and sequencing rationale before any subject is defined.

Answer these three questions:
1. What is the investigation question this interview set is trying to answer?
2. What would a passing outcome look like — what signal would justify proceeding to the next feature decision?
3. In what order will subjects be interviewed, and why? Name the sequencing logic explicitly (one sentence minimum).

Sequencing note format:
> "Sequence: [order and rationale — e.g., skeptic-first so their friction is the evidential baseline; advocate-last so their claims are tested against prior objections]"

**PHASE 0 GATE:**
- [ ] Investigation question is stated
- [ ] Passing signal is defined
- [ ] Subject sequence is declared with rationale

State: `PHASE 0 COMPLETE` before proceeding.

---

## PHASE 1: SUBJECT CARDS + EXPECTATION REGISTERS

**Purpose:** Declare each subject's identity, evidential role, and pre-interview expectations in a structured register before any transcript begins.

For EACH subject (minimum two, meaningfully different roles):

**Subject Card:**
```
SUBJECT: [Name or Role Label]
Role / Title: [explicit]
Evidential Function: [the structural job this subject performs in the evidence chain — not their title, not their disposition. What does their position DO? E.g., "establishes the friction floor; all subsequent evidence is measured against their objections"]
Vocabulary Signature: [Term 1], [Term 2], [Term 3] — terms that will appear in their answers
Prior Knowledge: [what they know]
Blind Spots: [what they have not experienced or seen]
Disposition: [skeptic | neutral | advocate | undecided]
Epistemic Standing: [GROUNDED | CONDITIONAL | INFERRED]
  GROUNDED = has direct operational experience with this problem domain
  CONDITIONAL = informed but has not encountered the feature alternative
  INFERRED = reasoning from an adjacent domain, not direct experience
```

**Expectation Register:**
```
EXPECTATION REGISTER — [Subject]
Expected to say: [specific claim, objection, or concern]
Expected to miss: [gap in their perspective given their blind spots]
Expected to confirm: [what you anticipate they will validate]
```

Write Subject Card AND Expectation Register for every subject before writing any transcript.

**PHASE 1 GATE:**
- [ ] Every subject has a Subject Card with all fields populated
- [ ] Every subject has an Expectation Register with all three rows
- [ ] Evidential Function is present and states structural contribution (not just role/disposition)
- [ ] Vocabulary Signature contains 2–3 specific terms per subject

State: `PHASE 1 COMPLETE` before proceeding.

---

## PHASE 2: INTERVIEW TRANSCRIPTS

**Purpose:** Simulate each interview in the subject's distinct voice, using the Subject Card and Expectation Register to ground every answer.

For each subject, in the declared sequence:

**Interview structure:**

1. Opening question — anchored to the subject's declared prior knowledge and concerns
2. Subject answer — in the subject's voice; vocabulary signature terms appear naturally
3. Follow-up question — contains `triggered by: "[exact phrase from the subject's prior answer]"`
4. Subject answer
5. [Repeat as needed — minimum one follow-up per subject]
6. Moment labels — inline, immediately after the relevant answer:

```
SURPRISING (expected: [what the Expectation Register predicted], got: [what emerged])
CONFIRMING (validates: [which register expectation was met])
INCONCLUSIVE (notable but neither confirms nor surprises — reason: [why it fits neither])
```

Every notable moment must be labeled. Leaving an interesting exchange unlabeled is a failure.

**PHASE 2 GATE:**
- [ ] Every subject has a complete transcript
- [ ] Every transcript has at least one follow-up containing `triggered by:`
- [ ] Every transcript has at least one labeled moment (SURPRISING / CONFIRMING / INCONCLUSIVE)
- [ ] Answer vocabulary matches the declared Vocabulary Signature

State: `PHASE 2 COMPLETE` before proceeding.

---

## PHASE 3: EVIDENCE EXTRACTION

**Purpose:** Extract discrete evidence items from each interview — typed, rated, and epistemically grounded.

For each subject, extract at least one evidence item:

```
EVIDENCE ITEM [N] — [Subject]
Claim: [what was said or implied]
Signal Type: [adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation | contradiction]
Strength: [strong | moderate | weak]
Strength Rationale: [one sentence — what makes this reliable, hedged, or ambiguous]
Basis: [verbatim — directly quoted | inferred — implied but not stated | corroborated — consistent across subjects]
Epistemic Standing: [copied from Subject Card — GROUNDED | CONDITIONAL | INFERRED]
```

**PHASE 3 GATE:**
- [ ] At least one evidence item per subject
- [ ] Every item has Signal Type, Strength, Strength Rationale, Basis, and Epistemic Standing populated
- [ ] No item is left without a Basis declaration

State: `PHASE 3 COMPLETE` before proceeding.

---

## PHASE 4: SYNTHESIS + META-NOTES

**Purpose:** Aggregate findings across subjects, track objection fate, and weight evidence by epistemic standing.

**4a. Evidential Baseline**
Name the skeptic subject's core objection. This is the baseline: the friction floor all subsequent evidence is measured against.

**4b. Objection Lifecycle**
Trace the skeptic's objection across the full interview sequence. State its fate explicitly:
- *Persisted* — reached the final interview unchanged
- *Transformed* — shifted in character or scope during the sequence
- *Resolved* — closed by evidence, concession, or framing by a subsequent subject

Do not write "subjects agreed" or "subjects disagreed" — trace the movement.

**4c. Epistemic-Weighted Synthesis**
Select at least one evidence item from Phase 3. Name how its standing adjusts its weight:

> "[Item] from [Subject] carries [GROUNDED / CONDITIONAL / INFERRED] standing. [Because: direct experience / not yet encountered the alternative / adjacent reasoning]. Weight adjustment: [blocker / risk to monitor / flag for future validation]. This means: [one sentence on how synthesis uses this differently than a GROUNDED item would be used]."

If all items are GROUNDED, state that explicitly — do not omit the standing check.

**4d. Convergences + Contradictions**
Name at least one pattern (convergence) and one tension (contradiction) across subjects.

**4e. Composite Signal**
One paragraph: what does the combined evidence say about the feature's current investigation status?

**4f. Simulation Fidelity + Voice Divergence**
- Fidelity: name one grounded basis (documented knowledge, domain expertise) and one constructed element (extrapolated plausibility)
- Voice: name one concrete contrast between two subjects — a specific vocabulary term, concern priority, or framing preference that distinguishes them

**PHASE 4 GATE:**
- [ ] Evidential baseline named
- [ ] Objection fate stated as persisted / transformed / resolved
- [ ] At least one evidence item explicitly weighted by epistemic standing
- [ ] Convergence and contradiction named
- [ ] Composite signal present
- [ ] Simulation fidelity note present with specific basis
- [ ] Voice divergence cites a specific term or framing difference

State: `PHASE 4 COMPLETE — interview simulation closed.`

---

**Topic:** {topic}
**Feature context (if provided):** {context}
```

---

## V-04 — Axis: Phrasing Register (Imperative / Command-Driven)
**Hypothesis:** Short, direct imperatives reduce interpretive drift — the model executes explicit commands rather than inferring intent from descriptive prose, improving compliance with structurally tricky criteria like C-23 (evidential function) and C-24 (synthesis weighting) that require a specific logical move rather than just content presence.

---

```markdown
# /prove:interview

Topic: **{topic}**

DO EVERYTHING IN THIS ORDER. DO NOT SKIP STEPS.

---

## STEP 1: DECLARE THE SEQUENCE

WRITE one sentence naming the interview order and why.
USE this form: `Sequence: [order] — [rationale in one clause].`
EXAMPLE: `Sequence: skeptic → neutral → advocate — friction-first so subsequent evidence is measured against the objection baseline.`

---

## STEP 2: WRITE SUBJECT CARDS

WRITE a Subject Card for each subject. MINIMUM two subjects. ENSURE roles are meaningfully different — not minor variations.

FOR EACH subject, WRITE:

**SUBJECT CARD**
- `Role / Title:` [be explicit — no anonymous subjects]
- `Evidential Function:` [NAME what structural job this subject performs in the evidence chain. NOT their title. NOT their disposition. The function. E.g.: "establishes the friction baseline; all other interviews are measured against their objections". A card that says only "the skeptic challenges assumptions" FAILS this field — name the structural contribution.]
- `Vocabulary Signature:` [WRITE 2–3 specific terms this subject uses. These must appear in their answers. Generic descriptions ("uses technical language") FAIL.]
- `Prior Knowledge:` [what they know]
- `Blind Spots:` [what they haven't seen or experienced]
- `Disposition:` [skeptic | neutral | advocate | undecided]
- `Epistemic Standing:` [GROUNDED | CONDITIONAL | INFERRED]
  - GROUNDED = direct operational experience with the problem
  - CONDITIONAL = informed but hasn't encountered the alternative
  - INFERRED = reasoning from adjacent domain

---

## STEP 3: WRITE EXPECTATION REGISTERS

WRITE an Expectation Register for EACH subject BEFORE any transcript.
DO NOT skip this step. DO NOT write transcripts first.

**EXPECTATION REGISTER — [Subject]**
- `Expected to say:` [specific claim or objection]
- `Expected to miss:` [gap from their blind spots]
- `Expected to confirm:` [what you expect them to validate]

---

## STEP 4: WRITE INTERVIEW TRANSCRIPTS

FOR EACH subject in declared sequence:

WRITE an opening question. ANCHOR it to their declared prior knowledge.

WRITE their answer IN THEIR VOICE. USE at least one vocabulary signature term.

WRITE a follow-up question. INCLUDE `triggered by: "[exact phrase from their last answer]"`.

WRITE their answer.

CONTINUE for at least one more exchange.

LABEL every notable moment immediately after the relevant answer:
- `SURPRISING (expected: [from Expectation Register], got: [what emerged])`
- `CONFIRMING (validates: [which register expectation])`
- `INCONCLUSIVE (notable but unresolvable — reason: [why neither label fits])`

DO NOT leave notable moments unlabeled. EVERY interesting answer gets a label.

---

## STEP 5: EXTRACT EVIDENCE

FOR EACH subject, WRITE at least one evidence item.

**EVIDENCE ITEM [N] — [Subject]**
- `Claim:` [what was said or implied]
- `Signal Type:` [adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation | contradiction]
- `Strength:` [strong | moderate | weak]
- `Strength Rationale:` [one sentence — what makes it reliable, hedged, or ambiguous]
- `Basis:` [verbatim | inferred | corroborated]
- `Epistemic Standing:` [GROUNDED | CONDITIONAL | INFERRED — copied from Subject Card]

DO NOT leave any field blank.

---

## STEP 6: WRITE SYNTHESIS

WRITE a synthesis section. INCLUDE ALL of the following:

**6a. BASELINE:**
NAME the skeptic's core objection. CALL it the evidential baseline.

**6b. OBJECTION FATE:**
STATE whether the objection *persisted*, *transformed*, or *was resolved* across the interview sequence.
TRACE its movement. DO NOT write "they agreed" or "they disagreed" — trace the objection.

**6c. EPISTEMIC WEIGHT ADJUSTMENT:**
PICK at least one evidence item. INVOKE its standing to adjust its weight.
USE this form: `"[Subject]'s [claim] is [GROUNDED / CONDITIONAL / INFERRED]. [Standing basis]. Weight: [blocker | risk to monitor | flag for validation]. [One sentence on why the standing changes how you use this evidence]."`
DO NOT treat CONDITIONAL and GROUNDED items as equally weighted without naming the difference.

**6d. PATTERNS + TENSIONS:**
NAME one convergence (subjects agree on something).
NAME one contradiction (subjects conflict on something — name the specific claims).

**6e. COMPOSITE SIGNAL:**
WRITE one paragraph. SUMMARIZE what the combined evidence says about the feature's investigation status.

---

## STEP 7: META-NOTES

WRITE:
1. **Fidelity note:** Name one grounded claim basis (documented knowledge, domain convention). Name one constructed element (extrapolated plausibility). Be specific.
2. **Voice contrast:** Name one concrete difference between two subjects. CITE a specific vocabulary term, concern priority, or framing choice. DO NOT write "they had different roles."

---

**Topic:** {topic}
**Feature context:** {context}
```

---

## V-05 — Combination: Role Sequence + Evidential Chain Architecture + Epistemic Standing (C-19 + C-23 + C-24 integrated)
**Hypothesis:** Framing the entire simulation as building an explicit evidence chain — where each subject occupies a named position in that chain and synthesis is required to reason across chain positions using epistemic standing — integrates C-19, C-23, and C-24 into a single coherent conceptual frame rather than treating them as three separate checkboxes. The chain metaphor makes the structural logic visible.

---

```markdown
# /prove:interview — Evidence Chain Simulation

Topic: **{topic}**

You are building an evidence chain, not collecting opinions. Each subject occupies a specific position in that chain. The chain has a structure: friction surfaces first, then feasibility tests, then validation. Synthesis reasons across chain positions — weighting evidence by how close each source is to the problem.

---

## PART I: EVIDENCE CHAIN DESIGN

Before writing any subject card, design the chain.

**Chain Rationale (one sentence):**
Name the interview order and the structural logic behind it. Every position in the chain must be justified. Example:
> "Chain: procurement skeptic → implementation engineer → product advocate — friction-first establishes the objection floor, engineering provides ground-truth on feasibility, advocate closes by testing whether claims survive the prior two positions."

**Chain Positions:**

| Position | Subject Role | Chain Function | Epistemic Standing |
|----------|-------------|----------------|-------------------|
| 1 (first) | | [What this position DOES for the chain — e.g., "establishes objection floor", "provides feasibility ground-truth", "tests whether prior objections survive advocacy"] | GROUNDED / CONDITIONAL / INFERRED |
| 2 | | | |
| 3 (if present) | | | |

**Chain Function field guidance:**
The function names the structural contribution to the evidence chain — not the subject's personality or disposition. Ask: if this subject weren't interviewed, what would be missing from the chain? The answer is their function.

---

## PART II: SUBJECT CARDS + EXPECTATION REGISTERS

For each subject, write:

**SUBJECT CARD — [Chain Position N] — [Role]**

```
Role / Title: [explicit]
Chain Function: [copied from chain design — the structural job this subject performs]
Vocabulary Signature: [Term 1], [Term 2], [Term 3]
  These are auditable. Each term must appear in the subject's answers.
Prior Knowledge: [what they bring to the interview]
Blind Spots: [what they haven't experienced — directly impacts epistemic standing]
Disposition: [skeptic | neutral | advocate | undecided]
Epistemic Standing: [GROUNDED | CONDITIONAL | INFERRED]
  GROUNDED: direct operational experience with this problem class
  CONDITIONAL: informed and knowledgeable but hasn't yet encountered the feature alternative
  INFERRED: reasoning by analogy from adjacent domain or prior context
```

**EXPECTATION REGISTER — [Role]**

```
Expected to say: [specific claim]
Expected to miss: [blind-spot-driven gap]
Expected to confirm: [anticipated validation]
```

Write all Subject Cards and all Expectation Registers before beginning any transcript.

---

## PART III: INTERVIEW TRANSCRIPTS

Interview each subject in chain order (Position 1 first).

**For each subject:**

Open with a question anchored to their declared prior knowledge and chain function — not a generic prompt.

Write their answer in their voice. Vocabulary signature terms appear naturally in answers. Generic AI-voice answers fail — if the answer could belong to any persona, rewrite it.

Write at least one follow-up that explicitly references their prior answer:
> `triggered by: "[exact phrase from their last answer]"`

Continue for at least one more exchange.

**Moment Labels** — required inline, immediately after the relevant answer:

```
SURPRISING (expected: [from Expectation Register], got: [what emerged from the chain position])
CONFIRMING (validates: [which register expectation — and which chain position this confirms])
INCONCLUSIVE (neither confirms nor surprises — reason: [name the ambiguity])
```

Label every notable moment. Unlabeled interesting moments are invisible to the evidence chain.

---

## PART IV: EVIDENCE EXTRACTION

After each transcript, extract evidence items. Each item is a link in the evidence chain.

**EVIDENCE ITEM [N] — [Chain Position / Subject]**

```
Claim: [what was said or implied]
Chain Link: [how this item connects to or modifies the chain — does it reinforce Position 1's friction? Challenge Position 2's feasibility? Validate Position 3's advocacy?]
Signal Type: [adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation | contradiction]
Strength: [strong | moderate | weak]
Strength Rationale: [one sentence — why]
Basis: [verbatim | inferred | corroborated]
Epistemic Standing: [GROUNDED | CONDITIONAL | INFERRED — from Subject Card]
```

The `Chain Link` field makes the evidence chain explicit — each item must name its relationship to at least one other chain position.

---

## PART V: CHAIN SYNTHESIS

The synthesis reasons across chain positions — it does not merely list what each subject said.

**5a. Chain Baseline**
Name the first position's core claim or objection. This is the chain's friction floor — all subsequent evidence is measured against it.

**5b. Chain Traversal**
Narrate how each subsequent position responded to the baseline:
- Position 2 met the baseline by: [sustaining / qualifying / resolving / reframing it]
- Position 3 (if present) met the evolved claim by: [same options]
State the objection's *final state*: did it *persist*, *transform*, or *resolve* by the time the chain closed?

**5c. Epistemic Standing in Chain Weighting**
For at least one evidence item, name how its chain position's epistemic standing adjusts its evidential weight:

> "[Subject at Position N] holds [GROUNDED / CONDITIONAL / INFERRED] standing because [specific basis]. Their claim that [X] therefore carries [full weight as blocker | provisional weight as risk to monitor | indicative weight requiring future validation]. Contrast with [Subject at Position M], whose [same claim or related claim] carries [different weight] due to [different standing basis]."

Do not treat evidence from CONDITIONAL and GROUNDED sources as equivalently weighted without naming the difference. The chain's value comes from knowing which links are load-bearing.

**5d. Chain Convergences + Breaks**
- Convergence: [where chain positions reinforce each other — name the specific shared claim]
- Break: [where chain positions conflict — name the specific claims in tension and which positions hold them]

**5e. Chain Verdict**
One paragraph. What does the assembled evidence chain say about the feature's investigation readiness? What is the strongest signal? What is the chain's weakest link?

---

## PART VI: META-NOTES

**Fidelity:** Name one chain position where the simulation is grounded in documented knowledge or domain convention. Name one position where answers were constructed by plausibility reasoning beyond documented context. Be specific.

**Voice Signature Check:** For at least two subjects, confirm vocabulary signature compliance — cite one term from each subject's declared signature that appeared in their transcript. Note any divergence between declared signature and actual voice.

**Chain Architecture Reflection:** Was the designed chain order correct in retrospect? Did the friction-first positioning actually surface the objections that shaped synthesis? One sentence.

---

**Topic:** {topic}
**Feature context (if provided):** {context}
```

---

## Summary Table

| Variation | Axis | Primary Hypothesis | Key Criteria Addressed |
|-----------|------|--------------------|----------------------|
| **V-01** | Role sequence (skeptic-first) | Sequencing makes C-23 function declarations and C-24 synthesis weighting fall out naturally from ordering logic | C-19, C-21, C-23, C-24 |
| **V-02** | Output format (card + table) | Structural fields force population of aspirational criteria without relying on authorial memory | C-13, C-18, C-20, C-22, C-23 |
| **V-03** | Lifecycle emphasis (explicit gates) | Phase gate conditions prevent rushing to synthesis before extraction — makes C-20 structural not aspirational | C-20, C-15, all sequential dependencies |
| **V-04** | Phrasing register (imperative) | Direct commands reduce interpretive drift on structurally complex criteria | C-23, C-24, C-12, C-16 |
| **V-05** | Role sequence + evidential chain + epistemic standing (combination) | Single chain-architecture frame integrates C-19 + C-23 + C-24 into coherent logic rather than three separate checkboxes | C-19, C-21, C-23, C-24 (all three new/upgraded criteria) |
