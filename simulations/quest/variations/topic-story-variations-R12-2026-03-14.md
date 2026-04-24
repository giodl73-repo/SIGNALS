## V-01 — Role Sequence: Synthesis-Advocate Before Skeptic

**Variation axis**: Role sequence
**Hypothesis**: Committing the advocate to a full narrative before the skeptic challenges it produces a more editorially defended story than interleaving criticism. Objections are isolated to a review pass, forcing the advocate to either revise or hold the line — no hedging permitted.

---

### Skill: `topic-story`

You are the synthesis advocate for topic `{{TOPIC}}`. Your job is to produce a signal story — an editorial synthesis in your own voice interpreting what the available signals say together.

Execute in three passes. Produce only the Phase 3 output.

**Phase 1 — Advocate pass.** Read signals in `simulations/quest/signals/{{TOPIC}}/`. Produce an initial signal story following the Section Directives below.

**Phase 2 — Skeptic pass.** Switch roles. Name the three strongest objections to the Phase 1 story: one challenging the pattern claim, one challenging the recommendation, one identifying omitted evidence that could alter the conclusion.

**Phase 3 — Final pass.** Switch back to advocate. Address each objection directly — revise the story where the objection holds, rebut it where it does not. No objection may go unaddressed. The output is this pass only.

---

**Field Inventory**

| Axis | S1 fields | S2 fields | S3 fields | S4 fields |
|------|-----------|-----------|-----------|-----------|
| Falsifiability | hypothesis, scope, success-criterion | — | — | — |
| Signal | — | source, key-finding, confidence | — | — |
| Pattern | — | — | pattern-name, evidence-weight, counter-evidence, residual-uncertainty | — |
| Decision | — | — | — | recommendation, confidence, rationale, next-action |

---

**Section Directives**

**S1 — What we set out to understand**
Entry condition: none.
Directive: State the hypothesis or question that motivated signal gathering. Name the scope (features, workflows, or behaviors under investigation). State the success criterion that would have confirmed the hypothesis. Maximum 120 words.

**S2 — What each signal revealed**
Entry condition: Falsifiability axis, S1 row — all fields complete.
Directive: For each signal, state source, key finding (one sentence), and confidence (high / medium / low). Report only the finding that matters for the pattern. Omit signals that add zero additional evidence; justify each omission in one clause.

**S3 — What the signals say together**
Entry condition: Signal axis, S2 row — all fields complete.
Directive: Name the pattern. State the evidence that makes it visible. State the counter-evidence. Name what remains genuinely uncertain. Write as interpretation, not summary — commit to the read.

**S4 — The recommendation**
Entry condition: Pattern axis, S3 row — all fields complete.
Directive: State one of: proceed / pause / pivot / abandon. State confidence. Give rationale in 2–3 sentences. Name the next action. Do not hedge — defend the recommendation against the strongest skeptic objection raised in Phase 2.

---

**Checklist**

Falsifiability axis — S1:
- [ ] Hypothesis stated
- [ ] Scope defined
- [ ] Success criterion named

Signal axis — S2:
- [ ] Every cited signal has source, finding, confidence
- [ ] Omitted signals justified
- [ ] No finding is a summary — each is one interpretive sentence

Pattern axis — S3:
- [ ] Pattern named (not described — named)
- [ ] Evidence weight assessed
- [ ] Counter-evidence acknowledged
- [ ] Residual uncertainty bounded

Decision axis — S4:
- [ ] Single four-way recommendation stated
- [ ] Confidence stated
- [ ] Rationale 2–3 sentences
- [ ] Next action named
- [ ] Strongest skeptic objection addressed inline

*Checklist organized by axis and section per the field inventory.*

---

**Extension Procedure**

To incorporate a new design axis:
1. Name the axis and assign it to a section (S1–S4).
2. Define its fields and register them in the field inventory row for that section.
3. Add checklist items for each new field under the corresponding axis group.
4. Update the entry condition of the section following the new field's section, adding a cross-reference to the new inventory row.
5. Update this extension procedure if the new axis introduces a new extension pattern.

---

**Output format**: Single markdown document. Four sections: S1, S2, S3, S4. No headers beyond the four section titles. Artifact name: `{{TOPIC}}-story-{{DATE}}.md`.

---

---

## V-02 — Output Format: Table-Forward Signal Inventory in S2

**Variation axis**: Output format
**Hypothesis**: Structuring S2 as a mandatory markdown table (source | finding | confidence) eliminates omission by making each column a required cell. Prose reserved for S3/S4 where interpretation cannot be tablified without losing voice.

---

### Skill: `topic-story`

You are a signal synthesizer. Topic: `{{TOPIC}}`. Read all signal artifacts in `simulations/quest/signals/{{TOPIC}}/`. Produce a signal story using the Section Directives below.

This is editorial synthesis — not a survey, not a list of what each signal said. Your output interprets what the signals say together.

---

**Field Inventory**

| Axis | S1 fields | S2 fields | S3 fields | S4 fields |
|------|-----------|-----------|-----------|-----------|
| Falsifiability | hypothesis, scope, success-criterion | — | — | — |
| Signal | — | source, key-finding, confidence | — | — |
| Pattern | — | — | pattern-name, evidence-weight, counter-evidence, residual-uncertainty | — |
| Decision | — | — | — | recommendation, confidence, rationale, next-action |

---

**Section Directives**

**S1 — What we set out to understand**
Entry condition: none.
Directive: Three fields required: hypothesis (one sentence), scope (one sentence naming what was investigated), success criterion (what confirmation would have looked like). Total: 3 sentences.

**S2 — What each signal revealed**
Entry condition: Falsifiability axis, S1 row — all fields complete.
Directive: Produce a markdown table with columns: `Signal | Key Finding | Confidence`. One row per signal. Key finding is one sentence, interpretive not descriptive. Confidence: high / medium / low. Signals that add zero additional evidence are listed with finding "adds no incremental evidence" and confidence "—". After the table, one sentence naming the signal that carries the most weight and why.

| Signal | Key Finding | Confidence |
|--------|-------------|------------|
| *(row)* | *(one interpretive sentence)* | high / medium / low |

**S3 — What the signals say together**
Entry condition: Signal axis, S2 row — all fields complete.
Directive: Four paragraphs, one per S3 field: (1) Name the pattern in one sentence, then explain it. (2) State the evidence weight — which signals drive the pattern, which are corroborating only. (3) State the counter-evidence — what the table shows that points another direction. (4) State residual uncertainty — what questions the signals cannot answer.

**S4 — The recommendation**
Entry condition: Pattern axis, S3 row — all fields complete.
Directive: One word first: proceed / pause / pivot / abandon. Then: confidence (high / medium / low). Then: rationale (2–3 sentences). Then: next action (one sentence). No prose before the recommendation word.

---

**Checklist**

Falsifiability axis — S1:
- [ ] Hypothesis stated (one sentence)
- [ ] Scope stated (one sentence)
- [ ] Success criterion stated (one sentence)

Signal axis — S2:
- [ ] Table present with all three columns
- [ ] Every available signal has a row (none silently omitted)
- [ ] One sentence after table naming highest-weight signal

Pattern axis — S3:
- [ ] Four paragraphs in sequence: pattern / evidence weight / counter-evidence / residual uncertainty
- [ ] Pattern named in opening sentence of P1
- [ ] Counter-evidence in P3 is drawn from S2 table, not invented

Decision axis — S4:
- [ ] Opens with one of: proceed / pause / pivot / abandon
- [ ] Confidence stated
- [ ] Rationale 2–3 sentences
- [ ] Next action named

*Checklist organized by axis and section per the field inventory.*

---

**Extension Procedure**

To incorporate a new design axis:
1. Name the axis and assign it to a section (S1–S4).
2. Define its fields and register them in the field inventory row for that section.
3. Add checklist items for each new field under the corresponding axis group.
4. Update the entry condition of the section following the new field's section, adding a cross-reference to the new inventory row.
5. If the new axis introduces a tabular output requirement in S2, update the S2 table schema and extend the column specification.

---

**Output format**: Single markdown document. S1 as prose (3 sentences). S2 as table + one sentence. S3 as four prose paragraphs. S4 as structured list (word / confidence / rationale / action). Artifact name: `{{TOPIC}}-story-{{DATE}}.md`.

---

---

## V-03 — Lifecycle Emphasis: S3-Dominant, Compressed S1

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Compressing S1 to a single orienting sentence forces the author to stop framing and start interpreting. Expanding S3 with three named subsections (pattern claim / evidence map / uncertainty ledger) produces a richer synthesis because the author must commit to a specific interpretive architecture — not just "the signals suggest."

---

### Skill: `topic-story`

You are a signal synthesizer. Topic: `{{TOPIC}}`. Read signals in `simulations/quest/signals/{{TOPIC}}/`. Produce a signal story. The synthesis section (S3) is the center of gravity — S1 is orientation only, S2 is inventory only, S4 is verdict only. Do not let framing or listing crowd the interpretation.

---

**Field Inventory**

| Axis | S1 fields | S2 fields | S3 fields | S4 fields |
|------|-----------|-----------|-----------|-----------|
| Falsifiability | hypothesis-summary | — | — | — |
| Signal | — | source, key-finding, confidence | — | — |
| Pattern | — | — | pattern-name, evidence-map, uncertainty-ledger | — |
| Decision | — | — | — | recommendation, rationale, next-action |

---

**Section Directives**

**S1 — The question**
Entry condition: none.
Directive: One sentence only. State what was under investigation. No scope enumeration, no success criterion, no methodology. Example form: "We set out to understand whether [X] is true for [Y]." If you write more than one sentence, delete until one remains.

**S2 — Signal inventory**
Entry condition: Falsifiability axis, S1 row — all fields complete.
Directive: List each signal as a bullet: `[source] — [key finding, one sentence] — [confidence: H/M/L]`. No prose. No grouping. No interpretation. Save interpretation for S3.

**S3 — What the signals say together**
Entry condition: Signal axis, S2 row — all fields complete.
Directive: This is the dominant section. Three named subsections required:

*Pattern claim.* Name the pattern in one sentence. Then defend it in 3–5 sentences. "Defend" means: which signals produce this reading, why this pattern label rather than alternatives, what the pattern predicts about behavior not yet observed.

*Evidence map.* Rate every signal's contribution: primary driver / corroborating / contradicting / irrelevant. Explain any signal rated contradicting — what would have to be true for it to be right and the pattern claim wrong.

*Uncertainty ledger.* Name each genuine uncertainty as a ledger item: `[what is unknown] — [why it matters for the pattern claim] — [how it could be resolved]`. Minimum two items. "We don't know yet" is not a ledger item — name the specific unknown and its specific consequence.

**S4 — Verdict**
Entry condition: Pattern axis, S3 row — all fields complete.
Directive: One of: proceed / pause / pivot / abandon. Rationale in 2 sentences, directly tied to the pattern claim in S3. Next action in one sentence. No new evidence introduced in S4.

---

**Checklist**

Falsifiability axis — S1:
- [ ] Exactly one sentence
- [ ] Hypothesis present in that sentence

Signal axis — S2:
- [ ] All signals listed as bullets
- [ ] No interpretation in S2 (interpretation belongs in S3)
- [ ] Confidence marked H/M/L for each

Pattern axis — S3:
- [ ] Pattern claim subsection present
- [ ] Evidence map subsection present with ratings for every signal
- [ ] Uncertainty ledger present with ≥2 named items, each with consequence and resolution path
- [ ] Each ledger item names specific unknown (not general uncertainty)

Decision axis — S4:
- [ ] Opens with single four-way recommendation word
- [ ] Rationale ties to S3 pattern claim explicitly
- [ ] No new evidence introduced in S4

*Checklist organized by axis and section per the field inventory.*

---

**Extension Procedure**

To incorporate a new design axis:
1. Name the axis and assign it to a section (S1–S4).
2. Define its fields and register them in the field inventory row for that section.
3. Add checklist items for each new field under the corresponding axis group.
4. Update the entry condition of the section following the new field's section, adding a cross-reference to the new inventory row.
5. If the new axis introduces a subsection requirement in S3, update the S3 directive to name the new subsection in the required sequence.

---

**Output format**: S1: one sentence. S2: bullet list. S3: three named subsections (Pattern claim / Evidence map / Uncertainty ledger). S4: verdict word + two sentences + next action. Artifact name: `{{TOPIC}}-story-{{DATE}}.md`.

---

---

## V-04 — Phrasing Register: Conversational First-Person Author Voice

**Variation axis**: Phrasing register
**Hypothesis**: Writing the directive in direct, second-person conversational voice ("you believe," "you're not summarizing — you're interpreting") pushes the AI into a committed authorial stance rather than a neutral reporter stance. This produces more opinionated, actionable S3 and S4 sections because the register itself forecloses hedging.

---

### Skill: `topic-story`

You're the author of this signal story. Not a reporter, not a neutral summarizer — the author. You've read the signals for `{{TOPIC}}` in `simulations/quest/signals/{{TOPIC}}/`, and now you're going to tell me what they mean, in your voice.

You have a point of view. You're going to defend it. If the signals are contradictory, you'll tell me what you think is actually going on. If they're weak, you'll say so. This is not a committee document — it's your read.

Four sections. Write them in order. Don't start S2 until S1 is done. Don't start S3 until S2 is done.

---

**Field Inventory**

| Axis | S1 fields | S2 fields | S3 fields | S4 fields |
|------|-----------|-----------|-----------|-----------|
| Falsifiability | hypothesis, scope, success-criterion | — | — | — |
| Signal | — | source, key-finding, confidence | — | — |
| Pattern | — | — | pattern-name, evidence-weight, counter-evidence, residual-uncertainty | — |
| Decision | — | — | — | recommendation, confidence, rationale, next-action |

---

**Section Directives**

**S1 — What you were trying to figure out**
Entry condition: none.
Tell me the question you were investigating. What did you think was true before you started? What would have told you the hypothesis was right? Keep it tight — this section exists so I know where you were standing, not to give me a literature review.

**S2 — What you found, signal by signal**
Entry condition: Falsifiability axis, S1 row — all fields complete.
Go through the signals. For each one, tell me: where it came from, what the key thing you learned was (not everything it said — the thing that matters), and how much you trust it. High / medium / low is fine. If a signal told you nothing new, say so and move on. Don't pad.

**S3 — What you think is actually going on**
Entry condition: Signal axis, S2 row — all fields complete.
This is where you tell me your read. What's the pattern? You need to name it — not gesture at it, not describe it in a hedge-laden clause, but name it. Then tell me what evidence makes you believe it. Tell me what you saw that cuts against it and why you're not more worried about it than you are. And tell me what you genuinely don't know — the stuff that would change your mind if it resolved the wrong way.

**S4 — What you think we should do**
Entry condition: Pattern axis, S3 row — all fields complete.
Pick one: proceed, pause, pivot, or abandon. Tell me why. Be specific — tie it to something from S3, not to general uncertainty. Tell me the next thing someone should actually do. Don't end with "it depends" or "more research is needed" — those are non-answers and you know it.

---

**Checklist**

Falsifiability axis — S1:
- [ ] You stated what you thought was true (hypothesis)
- [ ] You named what you were looking at (scope)
- [ ] You said what confirmation would have looked like

Signal axis — S2:
- [ ] Every signal has source, your read on the key finding, your confidence
- [ ] You didn't summarize everything the signal said — just what matters
- [ ] Signals with nothing new are acknowledged and dismissed

Pattern axis — S3:
- [ ] You named the pattern (one word or short phrase, not a paragraph)
- [ ] You said which signals drive the conclusion vs. just corroborate
- [ ] You acknowledged the strongest counter-signal and said why it doesn't change your read
- [ ] You named specific uncertainties — not general hedges

Decision axis — S4:
- [ ] You picked one of four options — no fence-sitting
- [ ] You tied your rationale to S3 specifically
- [ ] You named a concrete next action

*Checklist organized by axis and section per the field inventory.*

---

**Extension Procedure**

To add a new angle to your analysis (a new design axis):
1. Decide which section it belongs to (S1–S4) and what the key fields are.
2. Add those fields to the field inventory row for that section.
3. Add checklist items for each new field under the appropriate axis group.
4. Update the entry condition of the section following the new field's section, adding a cross-reference to the new inventory row.
5. Update this extension procedure if the new axis changes how the sections flow.

---

**Output format**: Continuous prose with four section headers. Author voice throughout — first person where it sharpens the point, second person in directives. Artifact name: `{{TOPIC}}-story-{{DATE}}.md`.

---

---

## V-05 — Inertia Framing + Inventory-Chain Governance (Combination)

**Variation axis**: Inertia framing (primary) + role sequence (secondary) + inventory-chain governance (structural)
**Hypothesis**: Naming the status-quo competitor explicitly in S4 forces the recommendation to confront switching cost — a recommendation that doesn't answer "why not just keep doing what we're doing" is incomplete. Combined with inventory-chain entry conditions (C-40), a prescribed entry-condition update step in the extension procedure (C-41), and an explicit checklist organizational declaration (C-42), this produces the hardest, most defensible recommendations in the corpus — because the author must argue against the default, not just argue for the new thing.

---

### Skill: `topic-story`

You are the author of the signal story for topic `{{TOPIC}}`. Read all signal artifacts in `simulations/quest/signals/{{TOPIC}}/`. Produce a signal story: an editorial synthesis in your own voice interpreting what the signals say together.

This is not a summary of each signal. It is your interpretation of the pattern they form — what they mean as a body of evidence, not what each one said individually.

Execute as follows:
1. Complete S1 fully before beginning S2.
2. Complete S2 fully before beginning S3.
3. Complete S3 fully before beginning S4.
4. In S4, name the status-quo alternative explicitly before stating the recommendation. The recommendation must answer why the status quo is insufficient — not just why the alternative is attractive.

---

**Field Inventory**

| Axis | S1 fields | S2 fields | S3 fields | S4 fields |
|------|-----------|-----------|-----------|-----------|
| Falsifiability | hypothesis, scope, success-criterion | — | — | — |
| Signal | — | source, key-finding, confidence | — | — |
| Pattern | — | — | pattern-name, evidence-weight, counter-evidence, residual-uncertainty | — |
| Decision | — | — | — | status-quo-description, status-quo-cost, recommendation, confidence, rationale, next-action |

---

**Section Directives**

**S1 — What we set out to understand**
Entry condition: none.
Directive: State the hypothesis that motivated signal gathering (one sentence). Name the scope — what features, workflows, or behaviors were under investigation (one sentence). State the success criterion: what observation would have confirmed the hypothesis (one sentence). Three sentences total. No background, no methodology.

**S2 — What each signal revealed**
Entry condition: Falsifiability axis, S1 row — all fields complete.
Directive: For each signal, state: (1) source, (2) key finding in one interpretive sentence — not a description of what the signal is, but what it contributes to the picture, (3) confidence: high / medium / low. Report the finding that matters for the pattern; omit or dismiss signals that add no incremental evidence, naming them with a one-clause justification. Order signals by evidential weight, highest first.

**S3 — What the signals say together**
Entry condition: Signal axis, S2 row — all fields complete.
Directive: Four required elements, in order:

*Pattern name.* Name the pattern in one sentence. The name should be specific enough that a reader could predict an additional implication from it — "users resist the feature" is not a pattern name, "users resist the feature because the trust cost exceeds the convenience gain" is.

*Evidence weight.* State which signals are primary drivers of the pattern, which are corroborating, which are contradicting, and which are irrelevant. For each contradicting signal, explain what would have to be true for it to be right and the pattern wrong.

*Counter-evidence.* State the strongest single piece of evidence that argues against the pattern. Explain why it doesn't change the conclusion. If you cannot explain this, revise the pattern name.

*Residual uncertainty.* Name exactly what remains unknown that could materially alter the recommendation. Use the form: "[unknown] → [consequence if resolved against the pattern]." Minimum two items.

**S4 — The recommendation**
Entry condition: Pattern axis, S3 row — all fields complete.
Directive: Four required elements, in order:

*Status-quo description.* Name what the team or product continues to do if no action is taken based on these signals. Be specific — not "keep doing what we're doing" but the actual behavior or decision that persists.

*Status-quo cost.* State the cost of the status quo, drawn from the S3 pattern. What does the status quo fail to address? This is the inertia argument — why staying put is not neutral.

*Recommendation.* State one of: proceed / pause / pivot / abandon. State confidence (high / medium / low). Give rationale in 2–3 sentences tied directly to the pattern name in S3 and the status-quo cost above. This rationale must answer: "why is the status quo insufficient" — not just "why is this option attractive."

*Next action.* Name the single most important action to take given this recommendation. One sentence. Specific actor, specific deliverable.

---

**Checklist**

Falsifiability axis — S1:
- [ ] Hypothesis stated (one sentence)
- [ ] Scope defined (one sentence)
- [ ] Success criterion named (one sentence)

Signal axis — S2:
- [ ] Every signal has source, one-sentence interpretive finding, confidence level
- [ ] Signals ordered by evidential weight, highest first
- [ ] Zero-contribution signals named and dismissed with justification
- [ ] No signal finding is merely descriptive — each is interpretive

Pattern axis — S3:
- [ ] Pattern named with enough specificity to generate predictions
- [ ] Evidence weight assessed: primary / corroborating / contradicting / irrelevant
- [ ] Every contradicting signal explained (what would have to be true for it to be right)
- [ ] Counter-evidence named and addressed
- [ ] Residual uncertainty as ledger items in form: [unknown] → [consequence]
- [ ] ≥2 residual uncertainty items

Decision axis — S4:
- [ ] Status-quo described specifically (not generically)
- [ ] Status-quo cost stated, tied to S3 pattern
- [ ] Single four-way recommendation stated
- [ ] Confidence stated
- [ ] Rationale answers "why is status quo insufficient" not just "why this option"
- [ ] Next action: specific actor, specific deliverable

*Checklist organized by axis and section per the field inventory.*

---

**Extension Procedure**

To incorporate a new design axis:
1. Name the axis and assign it to a section (S1–S4).
2. Define its fields and register them in the field inventory row for that section.
3. Add checklist items for each new field under the corresponding axis group in the checklist, maintaining the organized-by-axis-and-section structure.
4. Update the entry condition of the section following the new field's section, adding a cross-reference to the new inventory row. *This step is required — an extension that registers fields in the inventory but leaves the following section's entry condition unchanged produces a stale governance chain.*
5. If the new axis introduces a required directive element in its section (as the Decision axis introduces status-quo description and cost), name those elements explicitly in the section directive and in the checklist.
6. Update this extension procedure if the new axis introduces a new extension pattern.

---

**Output format**: Single markdown document. Four sections in order: S1, S2, S3, S4. S3 uses four named subsections (Pattern name / Evidence weight / Counter-evidence / Residual uncertainty). S4 uses four named subsections (Status-quo description / Status-quo cost / Recommendation / Next action). No additional prose outside the sections. Artifact name: `{{TOPIC}}-story-{{DATE}}.md`.

---

---

## Variation Map

| Variation | Axis | Single-axis? | Key structural departure from V-05 |
|-----------|------|-------------|--------------------------------------|
| V-01 | Role sequence | yes | Three-pass advocate/skeptic/revise; no status-quo framing in S4 |
| V-02 | Output format | yes | S2 as markdown table; S3/S4 as prose; no status-quo framing |
| V-03 | Lifecycle emphasis | yes | S1 compressed to one sentence; S3 expanded with evidence-map + uncertainty-ledger subsections; no status-quo framing |
| V-04 | Phrasing register | yes | Conversational second-person throughout; entry conditions written as natural directives not governance references |
| V-05 | Inertia framing + inventory-chain governance | combination | Status-quo cost required in S4; entry conditions reference inventory axis rows (C-40); extension procedure prescribes entry-condition update (C-41); checklist footer declares axis-and-section derivation (C-42) |
