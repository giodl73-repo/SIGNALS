Reading the R20 excellence signals, I see two new behavioral patterns that map to distinct criteria:

- **Pattern 2** → C-23: `bridge_declared=true` as a machine-readable exit signal parameter that Stage 5 can gate on
- **Pattern 3** → C-24: STANCE enforcement note co-located with the table schema (not in preamble)

Pattern 1 (dual-gap closure as atomic unit) is a test-design observation, not a skill behavior — no criterion.

Denominator: 14 → 16. Each full pass drops from 0.71 to **0.625 pts**. Each partial: **0.31 pts**.

---

# prove-topic — Quest Rubric v20

**version**: 20
**skill**: prove-topic
**criteria-count**: Twenty-four (5 essential, 3 recommended, 16 aspirational)
**formula**: essential 60 pts + recommended 20 pts + aspirational 10 pts = 100 pts possible

---

## Scoring Formula

| Tier | Criteria | Points | Per Criterion |
|------|----------|--------|---------------|
| Essential | C-01 – C-05 | 60 pts total | 12 pts each |
| Recommended | C-06 – C-08 | 20 pts total | ~6.67 pts each |
| Aspirational | C-09 – C-24 | 10 pts total | **0.625 pts** full / **0.31 pts** partial |

Aspirational denominator: / 16.

---

## Essential Criteria

All five must pass. One FAIL eliminates the essential tier entirely.

---

### C-01 — Five-stage structure present and ordered

- **Weight**: essential
- **Category**: structure

**Pass condition**: The response contains exactly five named stages in order: Stage 1 (Hypothesis Formation), Stage 2 (Websearch Evidence), Stage 3 (Intelligence Evidence), Stage 4 (Analysis), Stage 5 (Synthesis). All five must be explicitly labeled. A response that collapses or reorders stages is a FAIL.

---

### C-02 — Named scout artifact cited before hypothesis formation

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Before the hypothesis stage begins, the response explicitly names a scout artifact (e.g., `{topic}-scout-record-{date}.md`) as the source that grounds the hypothesis. General knowledge used without referencing a named scout artifact is a FAIL. A vague "use your scout research" instruction without naming the file is a FAIL.

---

### C-03 — Progressive artifact writes — one per stage, not batched

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Each stage produces exactly one WRITE instruction followed by a confirmation signal before the next stage begins. All five writes batched at the end is a FAIL. A stage that produces output but defers the write is a FAIL. A stage that writes more than one artifact is a FAIL.

---

### C-04 — Minimum count thresholds enforced at each evidence stage

- **Weight**: essential
- **Category**: correctness

**Pass condition**: Stage 2 (websearch) gates on count >= 5; Stage 3 (intelligence) gates on count >= 3; Stage 4 (analysis) gates on count >= 3. Each gate must be explicit — a threshold stated as a requirement, not an aspiration. Proceeding without meeting the gate is a FAIL. Omitting the gate entirely is a FAIL.

---

### C-05 — Synthesis integrates evidence from all prior stages

- **Weight**: essential
- **Category**: correctness

**Pass condition**: The synthesize stage references output from Stages 2, 3, and 4 by count or label. A synthesis that re-derives conclusions without citing stage outputs is a FAIL. A synthesis present but disconnected from the evidence chain is a FAIL.

---

## Recommended Criteria

Strongly expected. Missing one caps the composite below 90.

---

### C-06 — Numeric confidence chain with delta tracking

- **Weight**: recommended
- **Category**: structure

**Pass condition**: A numeric 1–10 confidence chain is maintained across stages with named delta terms: `prior`, `s2_delta`, `s3_delta`, `s4_delta`, and a `chain_equation` that sums them to a `final` value. All terms must be explicitly named. A narrative confidence description without numeric deltas is a FAIL. A final score without a chain equation is a FAIL.

---

### C-07 — Counter-hypothesis tracked to resolution

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: Stage 1 names an explicit counter-hypothesis alongside the primary hypothesis. The counter-hypothesis must be explicitly resolved — confirmed or refuted — at Stage 4 or Stage 5 based on evidence gathered. A counter-hypothesis stated but never resolved is a FAIL. No counter-hypothesis stated is a FAIL.

---

### C-08 — Resume audit before execution

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: Before Stage 1 begins, the response audits whether a prior prove-topic artifact exists for this topic. If a prior artifact is found, execution resumes from the appropriate stage rather than restarting. The audit must be explicit — a named check, not an assumption. No audit present is a FAIL.

---

## Aspirational Criteria

Each full pass = **0.625 pts**. Each partial = **0.31 pts**. Total aspirational pool = 10 pts across 16 criteria.

---

### C-09 — Three named roles declared before Stage 1

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Before Stage 1 begins, exactly three named roles are declared with distinct functional descriptions (e.g., ROLE A — Hypothesis Architect, ROLE B — Evidence Collector, ROLE C — Analyst). Each role must be referenced at the stage where it operates. Unnamed or implicit roles are a FAIL. Fewer than three roles is a FAIL.

---

### C-10 — Three-point displacement loop

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Three displacement checkpoints must be present: (1) a displacement anchor established at Stage 3 with an explicit label (e.g., "ROLE 2 displacement anchor established"), (2) an `s4_displacement_verdict` computed at Stage 4, and (3) a `displacement_conclusion` drawn at Stage 5. All three must use these named constructs. Two of three present is a PARTIAL. Fewer than two is a FAIL.

---

### C-11 — Compound exit signals dual-value

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Each evidence stage exit signal carries at minimum `count + running_confidence` simultaneously. Stage 4 additionally carries `displacement_momentum_final`. All three stages must satisfy their compound requirement in both body text and parameter syntax. A Stage 4 exit that carries count + displacement_momentum_final but omits running_confidence is a PARTIAL if two of three stages pass. Missing compound signals in two or more stages is a FAIL.

---

### C-12 — Count-gated exit in signal

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: Each evidence stage exit signal includes an explicit count threshold gate in the parameter or body (e.g., `exit_gate: count >= 5 → proceed`). The gate must be machine-readable — a named field or explicit condition. Prose-only gating is a FAIL.

---

### C-13 — Live payload chaining

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: Each stage entry condition explicitly names the predecessor artifact by path and extracts values by field name (e.g., `read {topic}-prove-s2-{date}.md → extract running_confidence`). "Use the prior output" without field extraction is a FAIL. Missing artifact path citation is a FAIL.

---

### C-14 — Stage 5 dual-block structure

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Stage 5 contains exactly two named, delimited blocks: a synthesis block and a displacement verdict block. A single undifferentiated Stage 5 block is a FAIL. Missing either named block is a FAIL.

---

### C-15 — Artifact extraction tamper-resistance

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: Stage entry conditions read from the named artifact file on disk rather than relying on in-session memory. Each extraction cites the artifact path explicitly. Memory-only extraction without file path citation is a FAIL.

---

### C-16 — Three-block synthesis + displacement gate

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Stage 5 contains three named blocks: (1) evidence integration block, (2) confidence resolution block, (3) displacement verdict gate. Each block must be explicitly labeled. Missing any of the three blocks is a FAIL.

---

### C-17 — Dependency-driven block inversion

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: When the displacement gate yields a negative or inconclusive verdict, the block ordering in Stage 5 inverts — the displacement verdict block precedes the synthesis block. A fixed block ordering that ignores displacement outcome is a FAIL.

---

### C-18 — Multi-field inter-stage validation

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: Stage 3 entry extracts two independent fields from the Stage 2 artifact and cross-validates both against expected ranges or prior signals. Stage 4 entry extracts two independent fields from the Stage 3 artifact and cross-validates both. Single-field extraction at Stage 3 only is a PARTIAL. Single-field extraction at both stages is a FAIL.

---

### C-19 — Momentum trajectory as conclusion ceiling

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: The synthesis conclusion is explicitly bounded by momentum trajectory direction. If `displacement_momentum` is declining, the conclusion ceiling is stated as capped accordingly. An uncapped conclusion that ignores momentum direction is a FAIL. Momentum direction stated but not linked to conclusion ceiling is a PARTIAL.

---

### C-20 — Per-stage delta column + arc naming

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The confidence chain table includes a per-stage delta column showing the numeric delta at each stage. The overall confidence arc is named (e.g., "accelerating," "decelerating," "plateau-then-surge"). Missing the delta column is a FAIL. Delta column present but arc unnamed is a PARTIAL.

---

### C-21 — Stage 4 tri-value exit

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Stage 4 exit simultaneously carries all three values: `count`, `running_confidence`, and `displacement_momentum_final`. All three must appear in both the body text and the exit signal parameter syntax. Values present in body but absent from parameter syntax is a PARTIAL. Missing any of the three values entirely is a FAIL.

---

### C-22 — Per-row VERDICT SUPPORTED vocabulary

- **Weight**: aspirational
- **Category**: correctness

**Pass condition**: Each row in the THREE-STAGE DISPLACEMENT CHAIN table carries an explicit VERDICT (or STANCE) field using only: `SUPPORTED`, `PARTIALLY SUPPORTED`, or `NOT SUPPORTED`. Y/N or True/False shorthand is a FAIL. `chain_pattern` naming does not substitute for per-row VERDICT. Missing VERDICT column entirely is a FAIL.

---

### C-23 — bridge_declared=true as exit signal parameter *(new in v20)*

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: Stage 4 exit signal parameter includes `bridge_declared=true`, grounded in a CHAIN BRIDGE block in the Stage 4 body that explicitly names both `confidence_chain_final` and `displacement_chain_final`. Stage 5 entry conditions gate on `bridge_declared=true` (e.g., `prototype_complete(..., bridge_declared=true)`), making dual-chain convergence checkable by the receiving stage as a named invariant rather than a prose assertion. A CHAIN BRIDGE block present with `bridge_declared=true` in the parameter but without Stage 5 entry gating is a PARTIAL. No CHAIN BRIDGE block or no parameter flag is a FAIL.

---

### C-24 — STANCE enforcement note co-located with table schema *(new in v20)*

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The enforcement constraint for VERDICT/STANCE vocabulary (e.g., "Y/N shorthand = format error. chain_pattern names the arc; it does not substitute for STANCE.") appears directly beneath the THREE-STAGE DISPLACEMENT CHAIN table header or within the table schema definition — not in a preamble or separate rule section. Co-locating the constraint with the table it governs is required; placement in a distant rules section fails the co-location test even if the constraint text is otherwise correct. Enforcement note present but in preamble only is a PARTIAL. No enforcement note is a FAIL.

---

## Version History

| Version | Aspirational Count | Per-Pass Pts | Change |
|---------|--------------------|--------------|--------|
| v17 | 9 | — | C-01–C-17 established |
| v18 | 12 | 0.83 | Added C-18 (multi-field), C-19 (momentum ceiling), C-20 (delta column) |
| v19 | 14 | 0.71 | Added C-21 (tri-value exit), C-22 (VERDICT vocabulary); denominator 12 → 14 |
| v20 | 16 | 0.625 | Added C-23 (bridge_declared parameter), C-24 (co-located enforcement note); denominator 14 → 16 |

---

## Scoring Note (v20 baseline)

The denominator increase from 14 to 16 reduces each aspirational pass by ~0.085 pts relative to v19. V-05, the first variation to close C-23 (bridge_declared parameter + Stage 5 gate), also closes C-24 (enforcement note co-located) — 14 full passes + 1 partial (C-18) = 14 × 0.625 + 1 × 0.31 = **8.75 + 0.31 = 9.06 aspirational pts → total 89.06**. V-04 closes C-22 and C-24 but not C-23 → 13 full + 1 partial = 8.125 + 0.31 = **8.44 → 88.44**. V-05 breaks away from V-04 under v20, which is the correct structural outcome: the CHAIN BRIDGE block that makes chain convergence machine-checkable is categorically more expressive than value-listing alone.

**R21 ceiling**: C-18 remains PARTIAL across all variations. Stage 3 entry needs a second independent field extracted from the Stage 2 artifact. The candidate field is `s2_displacement_delta_sum` — present in Stage 2 body, independent of `running_confidence`, and meaningful for momentum validation. A Stage 3 entry that reads `running_confidence AND s2_displacement_delta_sum` and cross-validates both against the signal payload closes C-18 to PASS.
