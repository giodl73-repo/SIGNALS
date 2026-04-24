```markdown
# Rubric: prove-prototype (v6)

**Updated**: 2026-03-15
**Changes from v5**: Added C-22, C-23, and C-24 (Aspirational tier) derived from
Round 5 excellence signals. C-22 captures the completion-line-as-audit-by-scan
pattern from V-04: completion lines that carry substantive result values (not merely
"section done" assertions) create a cross-phase audit path — a reader can verify
phase outcomes by scanning completion lines alone without reading phase bodies.
C-23 captures the role-attribution-as-contamination-guard pattern from V-01/V-05:
role labels that carry explicit prohibitions detect in-order but out-of-role content
(e.g., EVALUATOR writing build description), a failure class that phase-gate ordering
alone cannot detect. C-24 captures the lifecycle-container-as-second-detection-level
pattern from V-04: a named lifecycle container structure (e.g., DEFINE / RUN /
EVALUATE) catches lifecycle inversions at the document-structure level before any
phase-level inspection is required, providing a second independent detection surface.
Aspirational points raised from 40 to 70. Total raised from 140 to 170.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-24 | 70 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **170** |

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

## Aspirational Criteria (70 points)

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
| C-22 | **Completion lines carry substantive result values enabling audit-by-scan** — Each model-written completion line encodes the actual outcome values established at that gate (e.g., the measured result, the delta, the calibration reading), not merely an assertion that the phase is done | structure | aspirational | Every completion line contains at least one substantive result value drawn from the phase body — a number, a verdict word, a named finding, or an explicit null — such that a reader who scans only the completion lines can reconstruct the full outcome chain without reading the phase bodies. A completion line that says only `PHASE N COMPLETE` or paraphrases the phase heading without embedding a result value does not pass. C-22 extends C-20: a completion line that satisfies C-22 automatically satisfies C-20, but not vice versa |
| C-23 | **Role labels carry explicit prohibitions that guard against in-order, out-of-role contamination** — Each named role in a role-sequenced output includes a stated prohibition identifying content that role must not produce, preventing a role from writing content that belongs to a different role even when that content would appear in the correct phase position | structure | aspirational | Every role label (e.g., BUILDER, EVALUATOR, ANALYST) is accompanied by at least one explicit prohibition (e.g., *must not interpret results*, *must not restate build description*). The prohibition must name the content type being excluded, not merely instruct the role to stay focused. A role sequence that assigns phases correctly but omits role-level prohibitions does not pass, because phase-gate ordering cannot detect content written by the correct phase but the wrong role |
| C-24 | **Lifecycle containers provide a second detection level for structural inversions** — The output is organized within named lifecycle containers (e.g., DEFINE / RUN / EVALUATE) that correspond to the scientific method stages, so that lifecycle inversions are detectable at the document-structure level before any phase-level or role-level inspection | structure | aspirational | The output declares at least two named lifecycle containers that map onto distinct stages of the experimental method (setup, execution, analysis). Each container encloses only phases that belong to its stage. A container whose enclosed phases span multiple lifecycle stages does not pass. The containers must be structural boundaries (labeled sections or blocks), not merely thematic labels in prose. When present, lifecycle containers serve as a first-pass inversion detector independent of C-19, C-20, and C-23 |

---

## Excellence Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | **Failure mode named** | depth | excellence | A specific way the prototype could have succeeded accidentally — without the hypothesis being true — is identified and assessed |
| C-12 | **Effect size estimated** | depth | excellence | The result is quantified in a way that allows comparison: not just "it worked" but how much, how fast, how often, or under what conditions |
| C-13 | **Boundary condition tested** | coverage | excellence | At least one test at or beyond the claimed operating boundary is reported |
| C-14 | **Negative result treated as informative** | behavior | excellence | If the hypothesis is refuted or inconclusive, the output explains what was learned rather than treating the result as a failure to report |
| C-15 | **Next hypothesis named** | behavior | excellence | The output states what question the prototype result makes worth investigating next |
```

---

**What changed:**

- **C-22** (completion-line-as-audit-by-scan): Extends C-20 by requiring completion lines to embed actual result values. A reader scanning only completion lines must be able to reconstruct the full outcome chain. C-22 is a strict superset of C-20 — any line that passes C-22 automatically passes C-20.

- **C-23** (role-attribution-as-contamination-guard): Role labels must carry explicit prohibitions naming the content type each role must not produce. Phase-gate ordering is blind to a role that writes the right content for its phase but wrong content for its role; only role-level prohibitions catch this.

- **C-24** (lifecycle-container-as-second-detection-level): Named lifecycle containers (DEFINE / RUN / EVALUATE or equivalent) act as a coarser detection surface that catches structural inversions before any phase or role inspection. Distinct from C-19/C-20 in that it operates at document structure, not at individual phase boundaries.

**Point totals**: Aspirational 40 → 70, Total 140 → 170.
