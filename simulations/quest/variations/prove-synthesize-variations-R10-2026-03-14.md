## prove-synthesize — Variation Set R10

---

## V-01 — Single Axis: Role Sequence
**Hypothesis**: Sequential role execution (verdict-first ordering) produces clear synthesized output without requiring concurrent-reasoning specification.

```markdown
You are synthesizing investigation signals into a definitive answer for a hypothesis.

Work through three reasoning roles in this sequence:

**Step 1 — SYNTHESIST**
Read all investigation signals. Form a verdict: yes, no, or maybe. Assign confidence (0–100).
Identify the top 3 signals that most influenced your verdict. Note what each showed and
why it was decisive.

**Step 2 — ADVERSARY**
Challenge the verdict from Step 1. The challenge must be specific to this investigation.
Gate: reject any challenge that applies equally to every synthesis (e.g., "more data would
raise confidence"). A valid challenge names something structural about this evidence.

**Step 3 — ANALYST**
Review the ADVERSARY's challenge. If it identified a genuine gap, update the verdict or
confidence. Extract 2–4 principles from this investigation — transferable claims that apply
beyond this specific hypothesis. List open questions the investigation did not resolve.

---

## Output

Write a single document using this structure:

**Verdict — Confidence: [0-100]**
State yes, no, or maybe in the first sentence. Give the confidence score. Explain the basis
in 2–3 sentences.
Confidence scale: 0–24 = no basis; 25–49 = weak; 50–74 = moderate; 75–89 = strong;
90–100 = definitive.

**Key Evidence**
The three signals that most influenced the verdict. For each: name the signal, state what
it showed, and explain why it was decisive.

**Counter-Evidence**
What argues against the verdict. If the ADVERSARY raised a structural challenge, include it
here. State what would need to be true for the counter-evidence to overturn the verdict.

**Principles**
What this investigation tells us beyond this specific hypothesis. Each principle is a
transferable claim — something applicable to a different hypothesis in the same domain.

**Open Questions**
What the investigation did not resolve. List each as a question. Prioritize questions that
would change the verdict or confidence if answered.

---

## Completeness Check

Before finalizing, verify:
- The verdict is answerable without reading the underlying signals
- The top 3 signals are named and their influence explained
- At least one specific counter-evidence item is present
- Each principle is stated as a transferable claim
- Open questions are genuine questions, not restatements of the verdict

---

## Constraints

- The synthesis supersedes the individual investigation signals — it is the record
- Do not produce role-labeled headers in the output (no "SYNTHESIST:", "ADVERSARY:" sections)
- Output is prose paragraphs under each section header — not bullet lists

---

Hypothesis: {{hypothesis}}
Investigation signals: {{signals}}
```

---

## V-02 — Single Axis: Output Format
**Hypothesis**: Per-rank prose with explicit concurrent execution, dual-exemplar gate, slot-indexed self-containment check, and role-to-output closure attribution produces the highest-fidelity synthesis.

```markdown
You are synthesizing investigation signals for a hypothesis into a definitive answer.
The synthesis you produce supersedes the individual signals — it is the authoritative
record; the signal inventory is subordinate to it.

---

## Reasoning Roles

Three roles inform this synthesis: SYNTHESIST, ADVERSARY, and ANALYST. Roles run
concurrently in your reasoning; the output produced afterward is a single document, not
three labeled sections. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** integrates signals into a verdict, confidence score, and key evidence set.

**ADVERSARY** challenges the verdict and confidence on structural grounds.
Gate: the challenge must be specific to this investigation, not a generic hedge.
INVALID: "confidence could be higher with more data" — this applies to every synthesis
without exception and discloses nothing about this investigation.
VALID: "the three key signals all measure stated preference, not observed behavior — the
synthesis has no revealed-preference signal in key evidence" — this identifies something
structural and falsifiable about how this evidence was gathered.
Reject any challenge that cannot meet the specificity of the VALID example.

**ANALYST** reviews what the ADVERSARY raised, adjusts verdict or confidence if warranted,
extracts principles, and surfaces open questions. If the ADVERSARY raised a challenge that
was not resolved, it carries forward to open questions with the ADVERSARY as source.

---

## Output Structure

Write the synthesis as five prose paragraphs under these five section headers:

**Verdict — Confidence: [0-100]**
State yes, no, or maybe in the first sentence. Give the confidence score. Explain the
basis in 2–3 sentences.
Confidence scale: 0–24 = no basis; 25–49 = weak; 50–74 = moderate; 75–89 = strong;
90–100 = definitive.

**Key Evidence**
The three signals that most influenced the verdict. For each: name the signal, state what
it showed, and explain why it was decisive. One sentence per signal.

**Counter-Evidence**
What argues against the verdict. If the ADVERSARY raised a valid structural challenge, it
must appear here. State what would need to be true for the counter-evidence to overturn
the verdict.

**Principles**
What this investigation tells us beyond this specific hypothesis. State 2–4 transferable
claims — each should apply to a different hypothesis in the same domain.

**Open Questions**
What the investigation did not resolve. List each as a question. If the question was raised
by the ADVERSARY challenge, acknowledge that attribution.

---

## Self-Containment Check

Before outputting, verify that a reader who has not seen the investigation signals can
answer these five questions from the synthesis alone:

1. What is the verdict and why is the synthesizer confident at that level?
   → **verdict/confidence paragraph**
2. Which three signals drove the verdict and what did each show?
   → **key evidence paragraph**
3. What is the strongest argument against the verdict?
   → **counter-evidence paragraph**
4. What should a team take away that applies beyond this specific hypothesis?
   → **principles paragraph**
5. What remains unresolved, and what generated each open question?
   → **open questions paragraph**

If any question cannot be answered from the named paragraph, revise that paragraph before
outputting.

---

Hypothesis: {{hypothesis}}
Investigation signals: {{signals}}
```

---

## V-03 — Single Axis: Lifecycle Emphasis
**Hypothesis**: Framing synthesis as the lifecycle-closing event — with explicit phase attribution of signals — produces better-calibrated confidence scores by surfacing evidence gaps before verdict formation.

```markdown
You are synthesizing investigation signals into a definitive answer. Investigation proceeds
in phases; synthesis closes the lifecycle. The synthesis marks the point at which evidence
is sufficient to commit to a position — or to declare the hypothesis unresolved.

---

## Phase 1 — Signal Inventory

Before synthesizing, inventory the signals:

**Phase attribution**: For each signal, identify its investigation phase:
- Explore phase: qualitative, directional, hypothesis-forming
- Test phase: structured, quantified, hypothesis-testing
- Validate phase: confirmatory, cross-referenced, hypothesis-closing

**Signal role**: Mark each signal as primary (directly tests the hypothesis), supporting
(strengthens a primary signal), or contextual (relevant background, not directly probative).

**Phase coverage**: Does the signal set cover all three phases? A synthesis without
test-phase signals has a confidence ceiling of 49. A synthesis without validate-phase
signals has a ceiling of 74. All three phases present: no phase ceiling.

---

## Phase 2 — Synthesis

With inventory complete, synthesize:

**Verdict formation**: What do the primary signals say? If consistent, the verdict is
direct. If they conflict, the verdict must address the conflict explicitly.

**Confidence assignment**: Start from the phase ceiling. Lower within the ceiling if
primary signals are weak or conflicting.

**Adversarial check**: Challenge the verdict before committing. Is the phase coverage
assessment honest? Were any supporting signals misclassified as primary? Does a phase gap
explain a constraint on the verdict?

**Principle extraction**: What does this investigation's phase coverage tell us about
this hypothesis class? Some hypothesis classes reliably produce validate-phase signals;
others structurally cannot.

---

## Output

Write the synthesis as a single document:

**Verdict — Confidence: [0-100]**
State yes, no, or maybe. Give the confidence score. In one sentence, state which phase
ceiling applies and why (or state that no ceiling applies).

**Key Evidence**
The three most decisive signals. Note each signal's phase (explore/test/validate) and
explain why it was decisive.

**Counter-Evidence**
What argues against the verdict. Phase gaps count as counter-evidence when they constrain
the confidence ceiling. State what phase coverage would be required to remove each
constraint.

**Principles**
What this investigation tells us beyond this hypothesis. Include at least one principle
about what phase coverage is achievable for this hypothesis class.

**Open Questions**
What remains unresolved. Note whether each open question is a phase gap (a signal type
not gathered) or a content gap (signals conflict or are ambiguous within a phase).

---

## Constraints

- The synthesis supersedes the individual signals — the phase inventory is input, not output
- Do not reproduce the signal inventory in the output
- Phase labels in Key Evidence are the only lifecycle trace visible in the output document

---

Hypothesis: {{hypothesis}}
Investigation signals: {{signals}}
```

---

## V-04 — Combined: Concurrent Role Execution + Conversational Register
**Axes**: Role sequence (concurrent) + Phrasing register (direct/conversational)
**Hypothesis**: Concurrent role framing in plain imperative language reduces role-theater artifacts and produces tighter, less labored synthesis output.

```markdown
Synthesize the investigation signals into one definitive answer. Settle the hypothesis.
Give a verdict, defend it against a real challenge, and leave the reader with something
transferable.

---

## How to reason

Three roles are active at the same time as you work: SYNTHESIST, ADVERSARY, and ANALYST.
You don't run them in steps — they're concurrent in your reasoning. What you write is one
document that reflects all three. No labeled sections for each role.

**SYNTHESIST**: Pull the strongest signals. What is the answer, and why?

**ADVERSARY**: Push back. What is actually weak about the case?
Don't settle for a generic hedge — that tells the reader nothing.
Bad challenge: "more signals would increase confidence" — true of every synthesis, adds
nothing about this one.
Good challenge: "the two primary signals were gathered from the same participant pool —
corroboration is an illusion because the sources are not independent" — that is a real
structural problem with this evidence.
If the challenge doesn't clear the specificity bar of the good example, it doesn't belong
in the output.

**ANALYST**: Absorb what the ADVERSARY surfaced. Update the verdict or confidence if the
challenge was genuine. Extract the generalizable lesson. If the ADVERSARY raised something
you could not resolve, it goes into open questions — and the ADVERSARY gets credited as
the source.

---

## What to write

Five sections. Each is a prose paragraph.

**Verdict — Confidence: [0-100]**
First sentence: yes, no, or maybe, with the confidence score. Next 2–3 sentences: the
basis. Confidence: 0–24 = no basis; 25–49 = weak; 50–74 = moderate; 75–89 = strong;
90–100 = definitive.

**Key Evidence**
The three signals that drove the answer. One sentence each: name, what it showed, why it
mattered.

**Counter-Evidence**
The real arguments against. If the ADVERSARY landed a valid challenge, it goes here. Say
what it would take for the counter-evidence to flip the verdict.

**Principles**
2–4 things you would tell a team working a different hypothesis in the same space.
Transferable, specific — not a restatement of the verdict.

**Open Questions**
What is genuinely unresolved. If the ADVERSARY raised it and you did not resolve it, say
so. One question per line.

---

## Check before you output

Ask: could a reader who never saw the signals understand this synthesis completely?

- Can they get the verdict and confidence without digging further? → **verdict/confidence**
- Do they know which three signals mattered and why? → **key evidence**
- Do they know the strongest case against? → **counter-evidence**
- Do they have something transferable? → **principles**
- Do they know what is unresolved and where each question came from? → **open questions**

Revise any paragraph that fails its check.

---

This synthesis is the record. The individual signals are subordinate to it.

Hypothesis: {{hypothesis}}
Investigation signals: {{signals}}
```

---

## V-05 — Combined: Slot-Indexed Output + Inertia Framing
**Axes**: Output format (slot-indexed self-containment check) + Inertia framing (prior position + delta quantification)
**Hypothesis**: Grounding confidence scores in a named prior position and explicit delta makes the synthesis falsifiable — a reader can assess whether the investigation actually moved the needle or merely confirmed the prior.

```markdown
You are synthesizing investigation signals into a definitive answer for a hypothesis.
The synthesis resolves whether the hypothesis holds and states how far the evidence moved
from the prior default position — what a team would have believed before any investigation.

The synthesis supersedes the individual signals. It is the authoritative record; the signal
inventory is input, not output.

---

## Reasoning Roles

Three roles inform this synthesis simultaneously. Roles run concurrently in your reasoning;
the output is a single document, not three separate contributions.

**SYNTHESIST** integrates signals into a verdict and confidence. It identifies the prior
position and quantifies the delta the investigation produced.

**ADVERSARY** challenges the verdict at the gate. Apply this test to every proposed
challenge:
— REJECT if generic: "confidence could be higher with more data" — this applies to every
synthesis without exception and discloses nothing about this investigation.
— ACCEPT if structural: "the two primary signals were both collected post-intervention,
so the baseline delta cannot be computed from these signals" — this identifies something
falsifiable about how this specific evidence was gathered.
A challenge that cannot meet the ACCEPT bar does not belong in counter-evidence.

**ANALYST** updates based on valid ADVERSARY challenges, extracts principles, and closes
open questions. If the ADVERSARY raised a challenge that was not resolved, it carries
forward as an open question attributed to the ADVERSARY.

---

## Inertia Frame

Before writing the output, identify:

- **Prior**: What position would a team hold before any investigation? State in one sentence.
- **Delta**: How far did the investigation move the prior? Use the confidence scale as
  the unit: moving from 40 → 70 is a +30 delta.
- **Driver**: Which single signal produced the largest delta?

The inertia frame appears only inside the verdict/confidence paragraph. It is not a
separate section.

---

## Output Structure

Five prose paragraphs under these section headers:

**Verdict — Confidence: [0-100]**
State yes, no, or maybe. Give the confidence score. In the second and third sentences,
state the prior position and how far the investigation moved it (inertia frame). Identify
the signal that drove the largest move.
Confidence scale: 0–24 = no basis; 25–49 = weak; 50–74 = moderate; 75–89 = strong;
90–100 = definitive.

**Key Evidence**
The three signals that produced the most movement from the prior. For each: name the
signal, state what it showed, and characterize the movement it produced.

**Counter-Evidence**
What argues against the verdict or constrains movement from the prior. If the ADVERSARY's
challenge was accepted, it must appear here. State what evidence would be required to
reverse the movement — to push the position back toward the prior.

**Principles**
What this investigation tells us about hypothesis verification in this domain. 2–4
transferable claims. At least one principle should address what delta size is achievable
for this class of hypothesis.

**Open Questions**
What the investigation did not resolve. For each question, attribute its source: either
an unresolved ADVERSARY challenge (attribute to ADVERSARY) or an unexplored dimension not
covered by any signal.

---

## Self-Containment Check

Before outputting, verify that a reader who has not seen the signals can answer these
five questions from the synthesis alone:

1. What is the verdict, the confidence score, and how far did the investigation move the
   prior? → **verdict/confidence paragraph**
2. Which three signals produced the most movement and what did each show?
   → **key evidence paragraph**
3. What is the strongest argument against the verdict, and what would reverse it?
   → **counter-evidence paragraph**
4. What transferable claim about hypothesis verification can a team take away?
   → **principles paragraph**
5. What is unresolved, and which open questions came from the ADVERSARY?
   → **open questions paragraph**

If any question cannot be answered from the named paragraph, revise that paragraph before
outputting.

---

Hypothesis: {{hypothesis}}
Investigation signals: {{signals}}
```

---

## Variation Summary

| Var | Axis | Hypothesis | C-35 | C-36 | C-37 | C-38 | Predicted v10 |
|-----|------|-----------|------|------|------|------|--------------|
| V-01 | Role Sequence | Sequential is sufficient | FAIL | FAIL | FAIL | FAIL | ~119 |
| V-02 | Output Format | Per-rank prose + all v10 criteria | PASS | PASS | PASS | PASS | ~140 |
| V-03 | Lifecycle Emphasis | Phase-gated confidence calibration | FAIL | FAIL | FAIL | FAIL | ~90 |
| V-04 | Concurrent + Conversational | Plain register reduces role-theater | PASS | PASS† | PASS | PASS | ~133 |
| V-05 | Slot-Indexed + Inertia | Prior-delta grounding makes confidence falsifiable | PASS | PASS | PASS | PASS | ~140 |

†V-04's adversarial gate is embedded in an informal block rather than a labeled `Gate:` instruction — C-36 borderline depending on strict co-location reading.
