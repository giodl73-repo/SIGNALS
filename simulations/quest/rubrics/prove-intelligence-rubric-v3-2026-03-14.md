Here is the complete updated rubric:

---

## prove-intelligence rubric v3

**Three new aspirational criteria** extracted from Round 2 excellence signals:

| ID | Pattern Source | What it enforces |
|----|---------------|-----------------|
| C-14 | V-01/V-04/V-05 (`blocking-warning-text-as-gate-mechanism`) | The insider gate must use a verbatim `WARNING: INSIDER GATE NOT MET` blocking block followed by a "do not proceed" instruction — a count field or verdict note is not a gate |
| C-15 | V-02/V-04/V-05 (`named-role-phase-separation-for-c12-durability`) | Structural separation (C-12) must be implemented with named roles or phases visible as distinct sections in the output artifact — in-block separation (excerpt then relevance in the same block) is invisible under model compression and does not pass |
| C-16 | V-03/V-05 (`ledger-lifecycle-tied-to-phase-exit-conditions`) | The falsification ledger must exist in at least two lifecycle states tied to phase exit conditions (e.g., draft at search completion and final at synthesis) — a ledger written only once at the end does not pass |

**Other changes:**
- Scoring formula denominator updated: `aspirational_pass / 8 * 10` (was `/ 5`)
- Three new failure modes added (FM-11, FM-12, FM-13) — one per new criterion

---

### The C-11 / C-12 / C-13 → C-14 / C-15 / C-16 relationship

Each new criterion is a refinement of its predecessor — it closes the gap that the predecessor leaves open:

| Predecessor | Gap it leaves | Refinement | How it closes it |
|-------------|--------------|------------|-----------------|
| C-11: gate must exist | Gate can be a count field that records the miss silently | C-14: gate must be blocking WARNING text | WARNING block + "do not proceed" prevents silent continuation |
| C-12: separation must be visible in structure | In-block ordering passes visually but collapses under compression | C-15: separation must use named roles or phases | Named sections leave a detectable structural gap when skipped |
| C-13: ledger must exist as named artifact | Single end-state ledger is written after verdict is already framed | C-16: ledger must have multiple phase-tied states | Initial state catches uncovered FCs before synthesis begins |

---

### Full aspirational table (v3)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Output identifies at least one internal contradiction | aspirational | depth | Named conflict (source A vs. source B disagree on X) resolved or flagged unresolved. "Mixed sources" without identifying specific conflict is a fail. |
| C-10 | Output recommends follow-up queries for evidence gaps | aspirational | behavior | At least two named queries, each with: what to query, where to look, which FC it addresses. Generic "more research" language is a fail. |
| C-11 | Insider advantage treated as a hard exit condition | aspirational | behavior | Gate enforced — zero-insider runs must surface an explicit warning. Count field alone without gatekeeping does not pass. |
| C-12 | Extraction and interpretation are structurally separated | aspirational | correctness | Extraction logged before any interpretation, relevance, or strength labeling. Single-pass format does not pass. |
| C-13 | Falsification ledger is a first-class named artifact | aspirational | coverage | Named table mapping every FC to sources and status. Per-source FC fields alone do not pass. |
| C-14 | Insider gate enforced by blocking WARNING text, not by a count field | aspirational | behavior | Verbatim `WARNING: INSIDER GATE NOT MET` block + explicit "do not proceed" instruction. Count-only field or verdict note does not pass. Distinction from C-11: C-11 requires a gate exist; C-14 requires it be implemented as blocking text. |
| C-15 | Structural separation implemented with named roles or phases, not in-block ordering | aspirational | correctness | Named roles (Archivist/Analyst) or named phases (Phase 2/Phase 3) visible as distinct sections. In-block ordering (excerpt field then relevance field in the same source block) does not pass. Distinction from C-12: C-12 requires separation be visible; C-15 requires it be via named roles or phases. |
| C-16 | Falsification ledger exists in multiple lifecycle states tied to phase exits | aspirational | coverage | At minimum: initial state (all FCs open, at search completion) and final state (at synthesis). Three-state lifecycle (draft / in-progress / final) is gold standard. Single end-state ledger does not pass. Distinction from C-13: C-13 requires a named ledger exist; C-16 requires multiple phase-tied states. |

---

### Scoring formula (v3)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

### New failure modes

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| FM-11 | C-14 | Run includes an insider count check (C-11 passes) but uses a count-only field or verdict note rather than blocking WARNING text — the gate records the miss but does not prevent the model from continuing as if the skill's value was delivered |
| FM-12 | C-15 | Skill uses in-block ordering (excerpt field precedes relevance field within the same source block) and claims separation — passes C-12 on visual inspection but fails when the model compresses or merges fields, because a merged block leaves no structural gap in the artifact |
| FM-13 | C-16 | A complete and accurate falsification ledger exists at synthesis (C-13 passes) but was written in a single pass at the end — uncovered FCs are only visible after the verdict is already written, removing the opportunity to redirect search before synthesis |

---

Written to `simulations/quest/rubrics/prove-intelligence-rubric-v3-2026-03-14.md`.
g C-08 fields without a gatekeeping check does not pass. |
| C-12 | Extraction and interpretation are structurally separated | aspirational | correctness | The output demonstrates role or phase separation: verbatim extraction from source files is completed and logged before any interpretation, relevance judgment, or strength labeling is applied. A single-pass format where the model excerpts and interprets simultaneously does not pass. The separation must be visible in the output structure (e.g., an extraction log precedes the analysis table, or two named roles are distinguished). |
| C-13 | Falsification ledger is a first-class named artifact | aspirational | coverage | The output includes a dedicated falsification ledger — a named table or section that maps every falsification criterion to: the source(s) that address it, and a per-criterion status (satisfies / violates / inconclusive / uncovered). A per-source FC field alone does not pass; the aggregate ledger must exist as its own artifact so that coverage gaps are visible without reading individual source entries. |
| C-14 | Insider gate enforced by blocking WARNING text, not by a count field | aspirational | behavior | The output or skill prompt uses verbatim blocking text — a visually distinct `WARNING: INSIDER GATE NOT MET` block followed by an explicit "do not proceed" instruction — as the gate mechanism when zero insider sources are found. A count field that reports zero, or a verdict note that documents the shortfall after the fact, is not a gate. The WARNING block must appear before the synthesis section and must instruct the model to pause or reclassify rather than continue. The distinction from C-11: C-11 requires a gate exist; C-14 requires the gate be implemented as blocking WARNING text. |
| C-15 | Structural separation implemented with named roles or phases, not in-block ordering | aspirational | correctness | The output's extraction-interpretation separation (C-12) is implemented using named structural units — named roles (e.g., Archivist / Analyst) or named phases (e.g., Phase 2: Extraction / Phase 3: Analysis) — that are visible as distinct sections in the output artifact. In-block ordering (excerpt field first, then relevance field, within the same source block) does not pass because merged blocks are invisible under model compression and structurally indistinguishable from single-pass output. Named sections leave a detectable absence when skipped. The distinction from C-12: C-12 requires separation be visible; C-15 requires it be implemented through named roles or phases. |
| C-16 | Falsification ledger exists in multiple lifecycle states tied to phase exits | aspirational | coverage | The falsification ledger exists in at least two distinct named states tied to phase exit conditions: an initial state (all FCs open, produced at end of search) and a final state (all FCs resolved or marked uncovered, produced at synthesis). A third in-progress state (updated incrementally during analysis) is the gold standard. A single ledger written once at the end does not pass regardless of completeness — the lifecycle states make coverage gaps visible at intermediate points, catching uncovered FCs before the verdict is written. The distinction from C-13: C-13 requires a named ledger artifact exist; C-16 requires the ledger to have multiple phase-tied states. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| FM-01 | C-01 | Source cited by paraphrase or label ("the feasibility spec") without a file path — happens when the model summarizes from memory rather than searching |
| FM-02 | C-02 | Source entry contains only the model's interpretation of a passage, no direct text — excerpts written from training knowledge rather than actual file content |
| FM-03 | C-03 | Relevance statement is generic ("this file is about the same topic") without connecting to the hypothesis claim or falsification criteria |
| FM-04 | C-04 | Strength labels present in the verdict section only, not per-source — model summarizes evidence quality globally but omits the per-entry label |
| FM-05 | C-05 | Verdict buried mid-document or phrased as a transition sentence rather than a dedicated closing section |
| FM-06 | C-07 | Model references the hypothesis document but does not cite specific falsification criteria — relevance stated at hypothesis level, not at criterion level |
| FM-07 | C-08 | All sources are design docs that are also publicly readable; no entry flagged as insider-only knowledge |
| FM-08 | C-11 | Insider flag fields are populated (C-08 passes) but no gate is enforced — run completes silently when all insider fields are "no", losing the skill's differentiation without any warning |
| FM-09 | C-12 | Model excerpts and interprets in the same pass — relevance and strength labels are written alongside the quote before extraction is complete, making fabricated excerpts indistinguishable from real ones in the output structure |
| FM-10 | C-13 | Per-source FC fields are present but no aggregate ledger exists — uncovered falsification criteria are invisible unless the reader scans every source entry individually |
| FM-11 | C-14 | Run includes an insider count check (C-11 passes) but uses a count-only field or verdict note rather than blocking WARNING text — the gate records the miss but does not prevent the model from continuing as if the skill's value was delivered |
| FM-12 | C-15 | Skill uses in-block ordering (excerpt field precedes relevance field within the same source block) and claims separation — passes C-12 on visual inspection but fails when the model compresses or merges fields, because a merged block leaves no structural gap in the artifact |
| FM-13 | C-16 | A complete and accurate falsification ledger exists at synthesis (C-13 passes) but was written in a single pass at the end — uncovered FCs are only visible after the verdict is already written, removing the opportunity to redirect search before synthesis |
