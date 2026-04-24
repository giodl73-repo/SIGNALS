Done. Two new criteria extracted from the R15 scorecard and written to `simulations/quest/rubrics/topic-story-rubric-v15-2026-03-15.md`.

---

**What changed v14 → v15**

| | v14 | v15 |
|--|-----|-----|
| Source rounds | R1–R14 | R1–R15 |
| Aspirational count | 32 | 34 |
| Total criteria | 39 | 41 |
| Composite denominator | 32 | 34 |

**C-40 — Verdict as literal first line** (format, aspirational)
Sourced from V-02 C-01 evidence: "First line of output (before any section heading)." V-01 satisfies the essential C-01 floor — verdict in the opening paragraph or section. V-02 enforces the ceiling: nothing above the verdict, including structural labels. An output that passes C-01 but places the verdict after "ROLE 2: AUTHOR" fails C-40. C-01 remains the gate; C-40 is the tighter discipline.

**C-41 — Pattern necessity test** (depth, aspirational)
Sourced from V-02 C-03 evidence: "must require at least two signals to be true." C-03 (essential) says the claim must reference what signals show *together* that neither shows alone — ruling out single-signal claims. C-41 adds the necessity direction: remove either referenced signal and the claim must become false or unprovable. This rules out claims that borrow vocabulary from two signals but derive their logical force from one. Co-presence (C-03) is the gate; necessity (C-41) is the test that separates genuine conjunction from decorative co-citation.
 the output. A verdict that passes C-01 (appears in the opening section) but appears after even a structural heading ("## ANALYST BRIEF" or "ROLE 2: AUTHOR") fails. First line means topmost line.

**C-41 — Pattern necessity test** — BLOCK P passes a necessity test: the claim is false or unprovable if either signal it references were removed. A claim that references two signals but is supportable by either alone fails — "Signal A shows X and Signal B shows Y, therefore Z" fails if Z follows from X alone or Y alone. Each referenced signal must be a load-bearing premise for the claim.

---

```markdown
# Quest Rubric — `topic-story` v15

**Version:** v15
**Source rounds:** R1–R15
**Rubric version history:**
- v14 → v15: +2 aspirational criteria (C-40, C-41); N_aspirational 32 → 34
- v13 → v14: +1 aspirational criterion (C-39); N_aspirational 31 → 32
- v12 → v13: +3 aspirational criteria (C-36, C-37, C-38); N_aspirational 28 → 31
- v11 → v12: +3 aspirational criteria (C-33, C-34, C-35); N_aspirational 25 → 28
- v10 → v11: +3 aspirational criteria (C-30, C-31, C-32); N_aspirational 22 → 25
- v9 → v10: +2 aspirational criteria (C-28, C-29); N_aspirational 20 → 22

**What changed from v14 to v15:**

| | v14 | v15 |
|--|-----|-----|
| Version | v14 | v15 |
| Source rounds | R1–R14 | R1–R15 |
| Aspirational count | 32 | 34 |
| Total criteria | 39 | 41 |
| Composite formula denominator | 32 | 34 |

**New aspirational criteria from R15 (V-02 excellence signals):**

| C | Name | Axis | Category |
|---|------|------|----------|
| C-40 | Verdict as literal first line | V-02 | format |
| C-41 | Pattern necessity test | V-02 | depth |

---

## Essential Criteria

Output is not usable if any essential criterion fails.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Bottom Line Up Front** | correctness | essential | The recommendation or verdict appears in the opening paragraph or first named section — not buried at the end. A story that builds to a conclusion fails. A story where the first substantive sentence is hedging or context-setting fails. |
| C-02 | **Labeled sections present** | format | essential | The story contains the five named beats: *What we set out to understand / What the signals revealed / What the signals say together / What remains uncertain / The recommendation*. Any beat missing or renamed beyond recognition fails. |
| C-03 | **Cross-signal synthesis present** | correctness | essential | Beat 3 states a claim that references what two or more signals show *together* that no single signal shows alone. A sentence that could be derived from reading any single artifact fails. Restating artifact summaries side by side fails. |
| C-04 | **Pattern, not summary** | depth | essential | The synthesis claim names a relationship, tension, or gap across signals — not a collection of findings. A sentence equivalent to "Signal A said X and Signal B said Y" fails. The pattern must name a synthetic claim (e.g., "users want X but the technical cost is Y — the gap is the risk"). Restating individual findings side by side fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Signal coverage is grounded** | coverage | recommended | At least three distinct signal namespaces or artifact types are referenced to show what evidence base the story draws from. Not exhaustive enumeration — enough to make the synthesis credible. Fewer than three identifiable signal sources fails. |
| C-06 | **Uncertainty is specific** | depth | recommended | The "what remains uncertain" section names at least one specific open question that, if resolved, would change the recommendation. Generic hedges such as "more research may be needed" without naming what research or what it would change fail. |
| C-07 | **Recommendation proportionality** | correctness | recommended | The recommendation weight is consistent with the evidence described. Strong positive signals → proceed; mixed → pause; conflicting → pivot; weak or negative → abandon. A proceed recommendation following a story of conflicts and gaps fails; an abandon recommendation following a story of strong positive signals fails. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Narrative arc** | behavior | aspirational | The story has a discernible arc: intent (what we set out to learn), evidence building (signals adding up), resolution (recommendation). A reader unfamiliar with the topic can follow the reasoning from intent to recommendation without consulting the underlying signals. A flat list of findings with a tacked-on recommendation fails. |
| C-09 | **Delta surfacing** | depth | aspirational | At least one explicit "we expected X but found Y" or equivalent contrastive statement appears. The story calls out where the signals surprised or contradicted initial assumptions. Absence of any contrastive or discovery framing fails. Discovery language that requires inference from surrounding context — rather than a stated contrast — fails. |
| C-10 | **Pre-composition pattern artifact** | depth | aspirational | The cross-signal pattern is stated as a discrete, labeled claim that stands independently of the narrative prose — a named sentence or block (e.g., "The pattern: ...") that could be read without the surrounding story. The pattern must not exist only as an inference embedded in flowing text. This signals the pattern was identified analytically before writing, not arrived at during composition. Absence of a discrete pattern statement fails. |
| C-11 | **Pattern-to-recommendation traceability** | correctness | aspirational | The recommendation is visibly derived from the named cross-signal pattern. The story contains an explicit logical bridge: the pattern is cited as the stated reason for the recommendation verb chosen. A reader can identify the sentence or passage where the pattern produces the recommendation. Recommendation and pattern that are both present but not explicitly connected fail. |
| C-12 | **Decision-cost annotated uncertainty** | depth | aspirational | Each uncertainty item explicitly states what resolving it would change about the recommendation: whether the verb would shift and in which direction (e.g., "if X resolves to Y, this moves from pause to proceed"). General "this matters for the decision" framing without a stated direction fails. Uncertainty items with no decision-cost annotation fail. |
| C-13 | **Accountability-addressed recommendation** | correctness | aspirational | The recommendation beat names or clearly addresses the decision context — who is making the decision and under what constraint. A recommendation stated as a finding ("the signals suggest X") rather than a decision ("a team lead deciding Y should Z") fails. A recommendation with no named or implied decision-maker role fails. |
| C-14 | **Pattern block self-sufficiency** | depth | aspirational | The pre-composition pattern block (C-10) is self-contained: it conveys the full cross-signal claim without requiring the surrounding narrative to be read. Forward references ("as shown below"), backward references ("the above signals"), or incomplete claims that resolve only in the prose around the block all fail. |
| C-15 | **Signal-to-beat attribution** | correctness | aspirational | Each claim in Beat 2 is traceable to a named signal type or artifact. A beat that describes what "signals revealed" without naming the signal source for each revelation fails. Generic attribution ("the research showed") without a signal-type anchor fails. |
| C-16 | **Beat 3 opens with pattern block** | format | aspirational | Beat 3 ("What the signals say together") opens with the pre-composition pattern block verbatim or by reference — not with narrative setup. A beat that buries the pattern in prose after an introductory paragraph fails. The pattern must appear at or immediately after the beat header. |
| C-17 | **Explicit bridge sentence** | correctness | aspirational | The story contains a sentence that explicitly connects the analytical pattern to the recommendation verb — not implied by proximity. "Because the pattern shows X, the recommendation is Y" or equivalent. A reader must not have to infer the connection. |
| C-18 | **Uncertainty items are countable** | format | aspirational | Beat 4 lists discrete uncertainty items — numbered or bulleted — rather than presenting uncertainty as continuous prose. A single paragraph of hedging without discrete enumerable items fails. |
| C-19 | **Recommendation is a verb phrase** | correctness | aspirational | The recommendation is stated as an actionable verb phrase: proceed, pause, pivot, abandon, or an equivalent directive. Noun-form conclusions ("the recommendation is caution") fail. Adjective-form conclusions ("this is promising") fail. |
| C-20 | **Delta in Beat 2, not Beat 3** | behavior | aspirational | The contrastive "expected vs. found" signal (C-09) appears in Beat 2 (evidence revelation), not Beat 3 (synthesis). Surprises are evidence-layer observations; the synthesis layer interprets what they mean together. A story where the only contrastive statement appears in the synthesis beat fails. |
| C-21 | **Uncertainty items reference specific signals** | depth | aspirational | Each uncertainty item in Beat 4 names which signal namespace or artifact type would resolve it. "Further research is needed" fails. "A prove:prototype run on X would resolve whether Y" passes. Items with no named resolution path fail. |
| C-22 | **Pattern block uses consistent terminology** | correctness | aspirational | The terminology in BLOCK P matches the terminology used throughout the narrative. A pattern block that introduces terms not used elsewhere, or a narrative that drifts from terms established in the pattern block, fails. The block sets the vocabulary; the narrative inherits it. |
| C-23 | **Beat 5 opens with recommendation verb** | format | aspirational | The recommendation beat opens with the recommendation verb or directive in the first sentence — not with a restatement of the situation or a pivot word ("However," "Despite this,"). The beat signals the decision immediately. |
| C-24 | **No orphaned signals** | coverage | aspirational | Every signal namespace or artifact type mentioned in Beat 2 contributes to the synthesis in Beat 3. A signal cited in evidence but absent from synthesis is orphaned. Orphaned signals indicate coverage inflation rather than genuine synthesis. |
| C-25 | **Bridge sentence bidirectionality** | correctness | aspirational | The explicit bridge sentence (C-17) is traversable in both directions: the recommendation follows from the pattern, and the pattern is the specific reason for the recommendation verb chosen (not another pattern). A bridge that would justify multiple different recommendation verbs equally fails. |
| C-26 | **Beat 1 contains no hedging** | correctness | aspirational | The opening beat states the recommendation without qualifications, caveats, or uncertainty in the first sentence. Hedges belong in Beat 4. An opening sentence of the form "While results are mixed, the recommendation is X" fails — the hedge must be removed to Beat 4 or the opening sentence rewritten. |
| C-27 | **Uncertainty items are ranked or prioritized** | depth | aspirational | Beat 4 signals which uncertainty item, if resolved, would most change the recommendation. A flat list with no ordering fails. Ranking can be explicit ("most important:") or by placement (leading item = highest decision cost). |
| C-28 | **BLOCK D present and explicit** | depth | aspirational | A discrete, labeled delta block ("BLOCK D" or equivalent) appears in the artifact, containing at least one "Expected [X]. Found [Y]." statement. Delta framing embedded only in prose without a named block fails. |
| C-29 | **BLOCK B present and explicit** | correctness | aspirational | A discrete, labeled bridge block ("BLOCK B" or equivalent) appears in the artifact, containing the sentence that connects BLOCK P to the recommendation verb. A bridge that exists only as flowing prose without a named block fails. |
| C-30 | **BLOCK P single-sentence discipline** | depth | aspirational | BLOCK P is a single sentence. A multi-sentence pattern block fails — if the claim requires multiple sentences, it has not been distilled to a true synthetic claim. The sentence may be long; it must be one. |
| C-31 | **BLOCK B directional precision** | correctness | aspirational | BLOCK B names the specific recommendation verb it produces and no other. "The pattern suggests we should be careful" fails — "careful" is not a verb from the permitted set. The bridge must produce exactly one of: proceed, pause, pivot, abandon, or a domain-equivalent directive. |
| C-32 | **LEDGER present and exhaustive** | coverage | aspirational | A named LEDGER section lists every signal artifact drawn on in the story. Signals referenced in prose but absent from the LEDGER fail. The LEDGER is the closed set from which all narrative claims derive. |
| C-33 | **BLOCK P independence from LEDGER order** | depth | aspirational | BLOCK P does not name signals in the order they appear in the LEDGER. The pattern is a synthetic claim derived from signal relationships, not a progression through the evidence list. A pattern block that reads as "Signal 1 shows A; Signal 2 shows B; therefore C" fails — the pattern must name the relationship, not the sequence. |
| C-34 | **LEDGER entries carry claim weight** | coverage | aspirational | Each LEDGER entry states what the artifact contributes to the story — not just its name or type. A LEDGER that lists "scout:feasibility, prove:prototype, listen:adoption" without stating what each contributes fails. Each entry must carry a one-phrase claim summary. |
| C-35 | **BLOCK B cites BLOCK P by reference** | correctness | aspirational | BLOCK B explicitly references BLOCK P — by name, by quote, or by "the pattern above" — before stating the recommendation verb. A bridge that states the recommendation without anchoring to the named pattern block fails. The citation makes the derivation chain auditable. |
| C-36 | **Narrative-ledger closed-world constraint** | correctness | aspirational | The narrative may only draw on findings present in the LEDGER. Any claim in Beats 2–5 that cannot be traced to a LEDGER entry fails. The LEDGER is bidirectionally closed: it must be exhaustive (C-32) and the narrative must not exceed it. Introducing a finding in the narrative that was not captured in the LEDGER fails, even if the finding is accurate. |
| C-37 | **Pre-composition blocks as first-class output sections** | depth | aspirational | BLOCK D, BLOCK P, BLOCK B, and LEDGER appear as named, labeled output sections of the final artifact — not as internal working notes, scratchpad content, or commentary. A prompt that treats these blocks as process steps rather than deliverable sections fails. A reader reviewing the artifact must be able to locate and audit each block without inference. |
| C-38 | **BLOCK B verbatim restatement in Beat 5** | correctness | aspirational | BLOCK B appears verbatim in Beat 5. Paraphrasing, summarizing, or condensing BLOCK B in the narrative beat fails. The bridge sentence that connects pattern to recommendation verb must be identical in the block and in the beat — no interpretive drift between the analytical artifact and its narrative expression. |
| C-39 | **Analyst/Author role sequence** | depth | aspirational | Pre-composition work (BLOCK D, BLOCK P, BLOCK B, LEDGER) is completed by an explicitly named analyst role before any narrative authoring begins. The analyst role and author role are sequenced — the analyst's completed blocks are the input to the author, not a parallel activity. A prompt that directs a single pass where blocks are built and narrative is written simultaneously fails. A prompt that names two distinct roles and sequences them — analyst completes, then author writes — passes. |
| C-40 | **Verdict as literal first line** | format | aspirational | The verdict appears as the first line of output — before any heading, section label, role label, or preamble text. Nothing appears above it. A verdict that passes C-01 (appears in the opening section) but appears after a structural label ("## ANALYST BRIEF", "ROLE 2: AUTHOR", or any heading at any level) fails. First line means topmost line of the output, with zero lines above it. This is an aspirational refinement of C-01 — C-01 establishes the floor (opening paragraph or section); C-40 enforces the ceiling (literal first line). |
| C-41 | **Pattern necessity test** | depth | aspirational | BLOCK P passes a necessity test: the claim is false or unprovable if either signal it references were removed. A claim that references two signals but is supportable by either alone fails — the claim must be logically dependent on the conjunction of both signals. Each referenced signal must function as a load-bearing premise. "Signal A shows X and Signal B shows Y, therefore Z" fails if Z follows from X alone or Y alone. The test: remove each referenced signal in turn — if the claim survives either removal, the pattern is not genuinely cross-signal and must be rewritten. |
```

---

**Summary of change:**

| | v14 | v15 |
|--|-----|-----|
| Source rounds | R1–R14 | R1–R15 |
| Aspirational count | 32 | 34 |
| Total criteria | 39 | 41 |
| Composite denominator | 32 | 34 |

**C-40** captures a placement discipline that V-02 enforces and V-01 does not: the verdict precedes all structure, not just all narrative. In V-01, the verdict callout comes first within the narrative but could follow a role label. V-02's "first line of output (before any section heading)" closes that gap. C-01 remains the essential floor (opening paragraph or section); C-40 is the aspirational ceiling (literal first line).

**C-41** upgrades the cross-signal synthesis test from co-presence to logical necessity. C-03 (essential) establishes that synthesis must transcend any single signal — the claim must reference what signals show *together* that neither shows alone. C-41 adds the necessity direction: the claim must be false if either referenced signal is removed. Co-presence (C-03) rules out single-signal claims; necessity (C-41) rules out claims that borrow the vocabulary of two signals but derive their force from one. The two criteria work at different levels: C-03 is the gate, C-41 is the test that separates genuine conjunction from decorative co-citation.
