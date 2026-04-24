Reading the Round 4 scorecard carefully for patterns not yet captured in v4.

**New patterns detected:**

1. **V-02's gate completion artifact** — each phase closes with a model-written "PHASE N COMPLETE — [outcome summary]" line. This is structurally distinct from C-19 (ordering gate co-located at the constrained action). C-19 governs the *forward pointer* ("execute before Phase N"); this pattern governs the *completion record* — proof that the gate was satisfied, including what was established. The completion line also serves as a verifier for C-18 (V-02 evidence: "gate-completion line verifies disposition was selected").

2. **V-01's C-19 partial → V-02's fix** — V-01's gate scheme explicitly covered Sections 1–7 only; its output contract referenced "Sections 1–7" as the gated scope, leaving trailing optional sections (8 and 9) ungated. V-02 resolved this by assigning execute-before/after markers to all 9 phases including the trailing optional ones. This trailing-section gap is a distinct failure mode from C-19's general requirement, worth a dedicated criterion.

That yields **C-20** and **C-21**. Aspirational +10, total +10.

---

```markdown
# Rubric: prove-prototype (v5)

**Updated**: 2026-03-15
**Changes from v4**: Added C-20 and C-21 (Aspirational tier) derived from Round 4
scorecard patterns. C-20 captures the model-written gate completion artifact from
V-02's Phase Gates architecture: each gate-protected section closes with a
model-written line that records what was established, serving as structural proof
of gate passage (distinct from C-19's forward ordering pointer). C-21 captures the
trailing-section gate coverage gap exposed by V-01's C-19 partial: a gate scheme
that explicitly scopes itself to a subset of sections (e.g., "Sections 1–7") while
leaving trailing optional sections ungated does not satisfy C-19 or C-21. V-02's
full coverage of all 9 phases, including execute-after markers on phases 8 and 9,
is the pass-condition reference for C-21. Aspirational points raised from 30 to 40.
Total raised from 130 to 140.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-21 | 40 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **140** |

---

## Essential Criteria (60 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Hypothesis restated** — Output opens with an explicit restatement of the hypothesis being tested, before any description of what was built or what happened | correctness | essential | Hypothesis appears as the first substantive element; it must precede any prototype description or result |
| C-02 | **Prototype scope defined** — Output specifies what the prototype does and does not do, and states why the boundary does not invalidate the test | correctness | essential | At least two explicit exclusions are named; each exclusion is paired with a reason why the test remains valid without it |
| C-03 | **Measurement defined before building** — Output shows that success and failure criteria were established before construction, not retrofitted after results | correctness | essential | A "what to measure" section appears logically before the results section; success and failure conditions are stated explicitly |
| C-04 | **Actual vs. predicted reported** — Output explicitly compares what was predicted to happen with what actually happened | correctness | essential | Both a prediction and an observation are present; the delta (match or mismatch) is called out directly |
| C-05 | **Hypothesis verdict rendered** — Output states whether the hypothesis is confirmed, refuted, or inconclusive based on the measurements | correctness | essential | A verdict is stated in plain language; it follows from the evidence rather than being asserted without support |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Minimality justified** | depth | recommended | Output addresses at least one explicit trade-off: what was left out and why that omission still allows the hypothesis to be tested |
| C-07 | **Raw evidence included** | coverage | recommended | At least one concrete data point appears in the results section |
| C-08 | **Limitations and next step named** | depth | recommended | One limitation and one specific next step are stated |

---

## Aspirational Criteria (40 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |
| C-16 | **Counter-evidence question explicitly closed** — The output resolves whether any counter-interpretation exists, not just whether one was found | depth | aspirational | The counter-evidence section terminates with one of two explicit dispositions: (a) a named counter-interpretation with a grounded rebuttal, or (b) an explicit statement that no plausible counter-interpretation exists, with a reason. A missing counter-evidence section, or one that ends with the rebuttal case only and leaves the no-counter case unaddressed, does not pass |
| C-17 | **Rationale co-located with its anchor** — Each rationale element appears in the same structural unit as the item it explains | structure | aspirational | For every rationale required by the output — scope exclusion validity, delta explanation, verdict reasoning, counter-rebuttal — the rationale appears in the same table row, labeled pair, or immediately adjacent labeled element as its anchor item. A labeled-pair block (e.g., `**Why the delta is what it is**: [explanation]` in the same block as `**Delta**`) satisfies this criterion without requiring tabular format. A rationale that requires the reader to cross-reference a distant or generic section does not pass |
| C-18 | **Optional sections terminated with explicit binary disposition** — Any section that could be empty, skipped, or produce no findings must terminate with one of exactly two explicit dispositions: findings exist plus a substantive response, or findings absent plus an explicit reason | structure | aspirational | Every section whose content depends on what was found closes with one of the two permitted dispositions. Silence, a missing section, or a section structured to handle only the affirmative case does not pass. The disposition must appear as a terminal element of the section, not as a preamble or general instruction |
| C-19 | **Ordering gate co-located with the construction action** — Each temporal ordering requirement appears as an inline execution marker at the point where the constrained action occurs, not only in a separate structural-rules section or output contract | structure | aspirational | Every phase, section, or step that must precede a later action carries its own inline gate label (e.g., *Execute before Phase N*, *Establish before any build activity*) at the point of that action. A requirement stated only in a preamble or end-of-document contract, without a co-located inline marker, does not pass |
| C-20 | **Gate completion proven by model-written artifact** — Each gate-protected section closes with a model-written completion line that records what was established at that gate, providing structural proof of passage before the next section begins | structure | aspirational | Every gate-protected phase or section terminates with a labeled completion line (e.g., `PHASE N COMPLETE — [outcome summary]`) as the final element of that section, before the next section opens. The completion line must name what was established, not merely assert that the section is done. A gate that carries only a forward ordering marker (C-19) without a corresponding model-written completion record does not pass. A completion line that serves as the verifier for a binary disposition (C-18) satisfies both criteria simultaneously |
| C-21 | **Gate coverage is complete including trailing optional sections** — The gate scheme applies to every section in the output; no section is exempt because it is optional or positioned late in the sequence | structure | aspirational | Every section of the output — including optional trailing sections such as limitations, next steps, and replication path — carries an inline gate marker. A gate scheme that explicitly scopes its coverage to a named subset of sections (e.g., "Sections 1–7" or "Phases 1–7") while leaving subsequent sections ungated does not pass, even if all covered sections satisfy C-19. Execute-after markers (e.g., *Execute after Phase N gate is present in your output*) are a valid gate form for trailing sections |

---

## Excellence Criteria (10 points)

Derived from Round 1 scorecard patterns. These criteria distinguish outputs that
*enforce* their own completeness from outputs that merely permit it.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | **No sections left blank** — Every named section is populated with substantive content; no heading exists without a body | structure | excellence | Zero blank or placeholder sections; each heading is followed by content that directly addresses the section's purpose |
| C-12 | **Measurement ordering made explicit** — The temporal sequence is structurally visible; metric definition and success condition are explicitly positioned before any build or result content | structure | excellence | Section ordering or explicit labeling makes the temporal gate legible without inference |
| C-13 | **Delta computed, not co-reported** — The gap between predicted and actual is stated as its own labeled element, not merely co-located with two numbers | correctness | excellence | A dedicated delta element (column, field, or labeled sentence) states the gap explicitly; reader does not have to compute it |
| C-14 | **Verdict rationale is a distinct explanation** — The rationale explains *why* the evidence supports the verdict rather than restating the evidence | depth | excellence | A verdict rationale passage is present and distinct from the results section; it connects the observed delta to the verdict in at least one sentence of reasoning |
| C-15 | **Each scope exclusion answers the test-validity question** — For every excluded item, the output explains why the test remains valid without it | depth | excellence | Each exclusion entry answers "why does leaving this out still permit a valid test?"; bare labels or "it wasn't needed" do not pass |

---

## Scoring Guide

**Point weights**:
- Essential C-01–C-05: 12 pts each (60 total)
- Recommended C-06–C-08: 10 pts each (30 total)
- Aspirational C-09, C-10, C-16–C-21: 5 pts each (40 total)
- Excellence C-11–C-15: 2 pts each (10 total)
- **Total: 140 pts**

| Result | Credit |
|--------|--------|
| PASS | Full points |
| PARTIAL | ~half points |
| FAIL | 0 |
```

---

**Summary of new criteria:**

- **C-20** isolates the *completion side* of the gate pattern. C-19 covers the forward pointer ("execute before X"); C-20 covers the backward proof ("PHASE N COMPLETE — [outcome]"). They are independent: a variation can satisfy C-19 with inline markers and fail C-20 by omitting completion records, or vice versa.

- **C-21** closes the trailing-section loophole that produced V-01's partial. The failure mode is structural: a gate scheme that names its own coverage boundary ("Sections 1–7") is self-limiting. Execute-after markers are explicitly recognized as a valid gate form for sections that follow a prior gate, which is the V-02 pattern.
