Written to `simulations/quest/golden/prove-program-golden-2026-03-15.md`.

**What's in the golden document:**

- **Frontmatter** — R7, v6 rubric, 160/160, GOLDEN
- **Prompt body** — simplified V-02 verbatim (1,163 words, 24.8% below the variation base)
- **What made it golden** — five patterns:
  1. Inertia gate at Phase 0 — names prove-topic as the specific competitor, enumerates acceptable gap types, FAIL on generic statements
  2. Atomic conjunction gate (GATE-1) — hypothesis distinctness AND falsification as a single boolean, no partial credit
  3. Per-block citation contract (E-02 INPUT) — anti-pointer prohibition travels with the consumer block, not a global preamble
  4. Calibration gate (GATE-CAL) — enforces distinct confidence values, not just presence
  5. Minimum viable surface — all 22 criteria survive in 1,163 words with no tables, no role overhead
- **Rubric summary** — all 22 criteria (C-01–C-22) with tier, description, and points
riment type unavailable in prove-topic.

**Inertia gap:** [one sentence naming the specific prove-topic limitation]

**GATE-0:** The gap statement names a specific capability prove-topic lacks. If prove-topic is sufficient for this question, stop here and use it.

**FAIL:** Gap statement is generic ("more flexibility needed", "broader scope") rather than naming the specific limitation.

---

### Phase 1 -- Hypothesis

State a single, testable belief before naming or planning any experiment. The hypothesis must be in positive form.

**Hypothesis:** [one sentence, positive form]

**Falsification:** [the specific evidence that would cause you to reject this hypothesis -- concrete, not a vague qualifier]

---

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction

Both must be TRUE. Partial satisfaction is FAIL.

**Condition A -- Hypothesis distinctness:** Hypothesis differs from the research question in specificity or framing. A restatement in different words fails.
Condition A: TRUE / FALSE -- [in what way does the hypothesis differ?]

**Condition B -- Falsification present:** A falsification criterion is explicitly stated as a concrete piece of evidence that would cause rejection.
Condition B: TRUE / FALSE -- [what is the stated falsification criterion?]

**GATE-1 result: PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

**FAIL:** Hypothesis is a restatement of the question, or falsification criterion is absent. Return to Phase 1. Rewrite and re-evaluate GATE-1.

---

### Phase 1B -- Experiment Plan

**E-01:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [E-02 / synthesis]. Closes gap? -- Yes / No.

**E-02:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [synthesis]. Closes gap? -- Yes / No.

**Plan rules:**
- At least 2 distinct types required. No two experiments may share the same type.
- At least one experiment must close the inertia gap (Closes gap? = Yes).
- Every output label must be filled.

**GATE-P:** Confirm: (a) >=2 distinct types; (b) at least one Closes gap? = Yes; (c) every output label filled.

**FAIL:** Fewer than 2 distinct types, no experiment closes the gap, or any output label missing.

---

### Experiment E-01 -- [Type]

**Entry condition:** GATE-P PASS confirmed.

**INPUT:** Hypothesis -- [verbatim hypothesis from Phase 1] | Inertia gap -- [verbatim gap from Phase 0]

[One sentence: how hypothesis and inertia gap together scope what this experiment seeks.]

[Execute experiment.]

**E-01 output:** [labeled finding -- write this precisely; E-02 will embed it verbatim]

**Contract delivery:** output label = "[plan label]" -- consumed by: [E-02 / synthesis] -- delivered? Yes / No

**FAIL:** Contract delivery line absent or output label does not match Phase 1B plan.

**EXPERIMENT 1 COMPLETE.** Summary: [one line]. -> Consumed by: [E-02 / synthesis].

---

### Experiment E-02 -- [Type]

**Entry condition:** EXPERIMENT 1 COMPLETE confirmed.

**FAIL:** E-02 content written without EXPERIMENT 1 COMPLETE marker present.

**INPUT -- citation contract (local to this block):** This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding in full below. The following pointer forms are PROHIBITED in this INPUT section: "see above", "per E-01", "as found in E-01", or any paraphrase. Embed verbatim:

[exact text from E-01's labeled output -- quoted in full, not described or summarized]

[One sentence: how E-01's finding constrains or refocuses this experiment.]

[Execute experiment.]

**E-02 output:** [labeled finding]

**Contract delivery:** output label = "[plan label]" -- consumed by: synthesis -- delivered? Yes / No

**FAIL:** Contract delivery line absent or output label mismatch.

**EXPERIMENT 2 COMPLETE.** Summary: [one line]. -> Consumed by: synthesis.

---

[For each additional experiment: begin with entry condition confirming prior COMPLETE marker; INPUT section must contain the citation contract clause and verbatim content of the consumed output; execute; write labeled output; write contract delivery line; write EXPERIMENT N COMPLETE marker. The citation contract is written locally in each consumer experiment's INPUT section -- not in a shared global note.]

**ALL EXPERIMENTS COMPLETE.** -> Synthesis receives all labeled outputs.

---

### Feed-Forward Audit

**E-01 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- [E-02 / synthesis]
**E-02 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- synthesis

Populate from contract delivery lines only.

**FAIL:** Any audit entry contradicts the corresponding contract delivery line.

---

### Findings

>=2 labeled findings required. Evidence basis required per finding.

**F-01:** [finding text] -- Source: E-01 -- Confidence: high / medium / low -- Evidence basis: [basis]

**F-02:** [finding text] -- Source: E-02 -- Confidence: high / medium / low -- Evidence basis: [basis]

**FAIL:** Fewer than 2 findings, or evidence basis absent from any finding.

---

### GATE-CAL -- Confidence Calibration Check

Pass condition: >=2 distinct confidence values. All findings rated the same level = FAIL.

Distinct confidence values in findings: [e.g., "high (F-01), medium (F-02)"]
Count of distinct values: [N]
At least 2 distinct values? YES / NO

**GATE-CAL result: PASS / FAIL**

**FAIL:** All findings carry the same confidence level. Return to Findings. Examine each evidence basis independently. Differentiate confidence assignments. Re-evaluate GATE-CAL.

---

### Synthesis

**[Confirm GATE-CAL PASS before writing this section.]**

**What we thought:** [verbatim hypothesis from Phase 1]

**What we actually learned:** [confirm, refine, or refute -- must differ from hypothesis text; answer the research question]

**Inertia gap closure:** Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.

**Cross-namespace routing:** Which Signal artifact downstream should receive these findings? [draft spec / scout brief / topic plan / topic story]

**FAIL:** "What we actually learned" copies the hypothesis verbatim, or inertia gap closure verdict absent.

---

### Principles

Write at least 2 labeled, actionable principles abstracted from the findings. Each must state a specific guideline (when X, do Y -- or always Z). No generic truisms. Each must cite its source finding.

**P-01:** [When X, do Y] -- Source: F-NN

**P-02:** [When X, do Y] -- Source: F-NN

**FAIL:** Fewer than 2 principles, any principle is a generic truism, or any source finding missing.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
```
skill: prove-program
topic: {{topic}}
date: {{date}}
hypothesis: [one line]
inertia_gap: [one line]
experiment_types: [list]
findings_count: [N]
principles_count: [N]
inertia_gap_closed: true / false
```

---

## What Made It Golden

Five patterns distinguish the golden prompt from early-round baselines:

**1. Inertia gate at Phase 0.** Every run must name the specific prove-topic capability that is insufficient before a single experiment is designed. Acceptable gap types are enumerated (cross-namespace scope, external domain, multi-hypothesis, custom experiment type). Generic gap statements ("more flexibility") are a named FAIL. This prevents prove-program from being invoked when prove-topic would suffice — the inertia competitor is always named.

**2. Atomic conjunction gate (GATE-1).** Hypothesis distinctness and falsification presence are enforced as a single conjunction before the experiment plan. Two boolean conditions, one PASS line, no partial credit. A hypothesis that restates the research question fails Condition A even if a falsification criterion is present. This prevents the common failure mode of treating hypothesis + falsification as a checklist rather than a paired commitment.

**3. Per-block citation contract (E-02 INPUT).** Each consumer experiment carries its own inline anti-pointer prohibition identifying the upstream source by name. Pointer forms ("see above", "per E-01") are explicitly PROHIBITED in that block's INPUT section. The contract clause travels with the consumer, not with a global preamble. This forces verbatim embedding of upstream findings rather than reference drift.

**4. Calibration gate before synthesis (GATE-CAL).** A named gate enforces that confidence levels across findings are not all identical. The FAIL condition names the uniform-label pattern explicitly. Presence of confidence labels (C-07) does not imply differentiation — GATE-CAL tests differentiation independently.

**5. Minimum viable prompt surface.** The golden prompt is the simplification of V-02 (pure prose, no tables) — 1,163 words reduced from the 1,547-word variation base (24.8%). All 22 rubric criteria survive at PASS with no tables, no role overhead, no RFC bureaucracy. The lean format is easier to follow in production; the density comes from precision, not length.

---

## Final Rubric Criteria Summary

**Rubric:** prove-program-rubric-v6-2026-03-15.md | **Score ceiling:** 160/160

| Tier | # | Criterion | Pts |
|------|---|-----------|-----|
| Essential | C-01 | Hypothesis pre-commitment before first experiment | 12 |
| Essential | C-02 | Experiment plan >=2 distinct types with rationale | 12 |
| Essential | C-03 | Feed-forward: later experiment cites specific finding from earlier | 12 |
| Essential | C-04 | Synthesis contrast: original hypothesis + "what we actually learned" (must differ) | 12 |
| Essential | C-05 | Qx.md format at correct path (>=4 labeled sections) | 12 |
| Recommended | C-06 | Principles >=2, labeled, actionable, sourced to findings | 10 |
| Recommended | C-07 | Confidence levels per finding (>=2 distinct findings) | 10 |
| Recommended | C-08 | Flexibility beyond prove-topic: specific limitation named, program structure addresses it | 10 |
| Aspirational | C-09 | Inertia gap verdict in synthesis | 5 |
| Aspirational | C-10 | Cross-namespace routing in synthesis | 5 |
| Aspirational | C-11 | Feed-Forward Audit Ledger | 5 |
| Aspirational | C-12 | Locked hypothesis values carried verbatim into experiments | 5 |
| Aspirational | C-13 | Contract delivery lines per experiment | 5 |
| Aspirational | C-14 | Per-experiment entry condition gate | 5 |
| Aspirational | C-15 | EXPERIMENT N COMPLETE markers | 5 |
| Aspirational | C-16 | ALL EXPERIMENTS COMPLETE marker before synthesis | 5 |
| Aspirational | C-17 | Artifact frontmatter with required fields | 5 |
| Aspirational | C-18 | Phase-boundary gates >=2 named | 5 |
| Aspirational | C-19 | >=3 inline FAIL conditions in template | 5 |
| Aspirational | C-20 | Atomic conjunction gate: hypothesis polarity AND falsification, two conditions, single PASS line | 5 |
| Aspirational | C-21 | Calibration gate: confidence non-uniformity enforced before synthesis, named FAIL condition | 5 |
| Aspirational | C-22 | Per-consumer-block embedded citation contract, not global preamble | 5 |
| | | **Total** | **160** |
