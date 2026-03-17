## program-plan Scorecard — Round 3

**Rubric**: v3 (135 pts) | **Golden threshold**: 108 | **Date**: 2026-03-14

---

### V-01 — Explicit Contrast Opener (C-14)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 instructs `program.yaml` with `topic`, `stages`, echo; echo has `auto: true` |
| C-02 | Echo stage contract | **PASS** | Step 6: "Final stage is always `echo` with `skills: []` and `auto: true`. No other stage may be named `echo`." |
| C-03 | All referenced skills valid | **PASS** | Complete 47-skill catalog listed inline by namespace |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 explicitly bans "Done", "ready", "complete"; requires artifact threshold |
| C-05 | Skills ordered by dependency | **PASS** | Arc layer mapping (Step 3) enforces Breadth→Design→Depth→Synthesis |
| C-06 | Stages group meaningfully | **PASS** | Step 5 instructs 3-6 stages reflecting arc intent, not namespace categories |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires `scout-feasibility`, `draft-spec` naming; examples demonstrate specific artifact types |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples: `discovery`, `design`, `validation`, `synthesis` |
| C-09 | Strategic pacing | **PASS** | Explicit arc layers Breadth→Design→Depth→Synthesis with layer-output-feeds-layer-input logic |
| C-10 | Gates quantified | **PASS** | `>=N` threshold required in Step 4 for every gate |
| C-11 | Skill catalog grounded inline | **PASS** | All 47 skills listed inline, not by reference |
| C-12 | Actor-role framing for gates | **PASS** | Required format: "[Delivering actor] hands off to [Receiving actor]" |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N artifact_type` syntax embedded inside Step 4 gate-writing instruction |
| C-14 | Naive-competitor framing | **PASS** | "This variation defeats that failure mode specifically by two structural choices: (1) actor-layer assignment, (2) unified handoff+threshold gate template." Failure mode named + structural choices named. |
| C-15 | Why-this-position column | **FAIL** | Column present with "Why this position" header; entries provide position rationale ("Landscape signals establish what is worth building") but contain no "what breaks if moved earlier" reasoning. R2 V-05 table inherited unchanged — same gap. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Single format string in Step 4: `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"` — all three elements co-located |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what the gates are protecting against — specifically, what happens if any gate is removed" |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [F] C-16 [P] C-17 [P]
              Pass count: 8 / 9   -> 8 * 5  = 40 pts (of 45)

Composite score: 130 / 135

Golden: all essential pass AND composite >= 108  ->  [X] YES
```

---

### V-02 — Causal Actor Table (C-15)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Same YAML step as V-01 |
| C-02 | Echo stage contract | **PASS** | Step 6 identical |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layers enforce sequence |
| C-06 | Stages group meaningfully | **PASS** | Step 5 same instruction |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires specific artifact type names |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples provided |
| C-09 | Strategic pacing | **PASS** | Arc layer structure with layer-feeds-layer rationale |
| C-10 | Gates quantified | **PASS** | `>=N` threshold required |
| C-11 | Skill catalog grounded inline | **PASS** | 47-skill inline listing |
| C-12 | Actor-role framing | **PASS** | Handoff format with named actors |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` inside Step 4 |
| C-14 | Naive-competitor framing | **FAIL** | "The competitor you are designing against is unsequenced skill execution." Names a specific failure mode but provides no "this variation defeats that by [structural choice]" statement. The contrast is implied not explicit — the rubric requires naming the structural choice that defeats it. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this position — and what breaks if moved earlier." Entries include full consequence chains: "Moved later: design is anchored in the author's assumptions rather than validated landscape signals; review critiques a design targeting the wrong problem; prove investigates a hypothesis without market grounding." Per-actor causal reasoning present. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Format string in Step 4 with actor + `>=N` + artifact |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what happens if any gate is removed" |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [F] C-15 [P] C-16 [P] C-17 [P]
              Pass count: 8 / 9   -> 8 * 5  = 40 pts (of 45)

Composite score: 130 / 135

Golden: all essential pass AND composite >= 108  ->  [X] YES
```

---

### V-03 — C-14 + C-15 Minimal Form

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 instruction present |
| C-02 | Echo stage contract | **PASS** | Step 6 explicit |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layer mapping enforces order |
| C-06 | Stages group meaningfully | **PASS** | Step 5 same |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires artifact naming |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples |
| C-09 | Strategic pacing | **PASS** | Breadth→Design→Depth→Synthesis arc with layer-output logic |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | 47-skill inline listing |
| C-12 | Actor-role framing | **PASS** | Handoff format |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | "This variation defeats that by two mechanisms: actor-layer assignment that grounds every stage in a workflow transition, and a required handoff+threshold gate format that forces artifact naming and role transitions simultaneously." Failure mode named (namespace-sorted skills, "ready"/"complete" gates); structural choices named. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this position (what breaks if moved earlier)." PM entry: "No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem." Architect entry: "Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation." Each entry has position rationale + "what breaks if moved" consequence. Compact form is sufficient. *Resolves R3-H02: compact notes pass C-15.* |
| C-16 | Unified handoff+threshold gate template | **PASS** | Format string in Step 4 with all three elements |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what happens if any gate is removed" |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P]
              Pass count: 9 / 9   -> 9 * 5  = 45 pts (of 45)

Composite score: 135 / 135

Golden: all essential pass AND composite >= 108  ->  [X] YES
```

---

### V-04 — C-14 + C-15 Role-Pedagogy Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 |
| C-02 | Echo stage contract | **PASS** | Step 6 |
| C-03 | All referenced skills valid | **PASS** | Inline catalog |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layers |
| C-06 | Stages group meaningfully | **PASS** | Step 5 |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 |
| C-08 | Stage names descriptive | **PASS** | Step 5 |
| C-09 | Strategic pacing | **PASS** | Arc structure + layer rationale |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | 47-skill listing |
| C-12 | Actor-role framing | **PASS** | Handoff format |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | "This variation breaks that pattern by requiring two things a skill list cannot satisfy: a causal actor ordering with per-actor justification explaining what breaks if the actor moves, and a gate format that exposes the handoff — who delivers what to whom at what threshold." Failure mode: "a program plan that is secretly a skill list." Structural choices named. *Resolves R3-H01: "defeats" not required; "breaks that pattern by requiring" passes.* |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this actor cannot run earlier." Full prose paragraphs per actor. PM: "Every other actor needs something from scout: the Architect needs landscape context to anchor the design..." Maximum causal depth. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4: "all three elements must appear together" with format string |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what happens if any gate is removed" |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P]
              Pass count: 9 / 9   -> 9 * 5  = 45 pts (of 45)

Composite score: 135 / 135

Golden: all essential pass AND composite >= 108  ->  [X] YES
```

---

### V-05 — Full Synthesis Maximum

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 |
| C-02 | Echo stage contract | **PASS** | Step 6 |
| C-03 | All referenced skills valid | **PASS** | Inline catalog |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 |
| C-05 | Skills ordered by dependency | **PASS** | Arc layers |
| C-06 | Stages group meaningfully | **PASS** | Step 5 |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 |
| C-08 | Stage names descriptive | **PASS** | Step 5 |
| C-09 | Strategic pacing | **PASS** | Full arc structure with per-layer output-input chain |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | 47-skill listing |
| C-12 | Actor-role framing | **PASS** | Handoff format |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` embedded in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | "This variation defeats that failure mode specifically by two structural choices enforced before any skill is placed: (1) an actor-layer assignment table with per-actor causal justification..., and (2) a required handoff+threshold gate template that forces three co-located elements." Explicit failure mode + both structural choices named. Strongest form. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this position and what breaks if moved earlier." Multi-sentence entries per actor. PM: "Moved later: design is anchored in the author's assumptions... review critiques a design targeting the wrong problem... prove investigates a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously." Maximum causal depth + gate consequence reasoning. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4: "all three elements must appear together" — actor + `>=N` + artifact in one format string |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "specifically, what happens if any gate is removed" |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P]
              Pass count: 9 / 9   -> 9 * 5  = 45 pts (of 45)

Composite score: 135 / 135

Golden: all essential pass AND composite >= 108  ->  [X] YES
```

---

### Final Ranking

| Rank | ID | Score | Golden | C-14 | C-15 | Notes |
|------|----|-------|--------|------|------|-------|
| 1 | V-03 | **135/135** | YES | P | P | Minimal form — proves compact entries sufficient |
| 1 | V-04 | **135/135** | YES | P | P | Role-pedagogy register — alternative C-14 phrasing passes |
| 1 | V-05 | **135/135** | YES | P | P | Full synthesis — maximum causal depth |
| 4 | V-01 | **130/135** | YES | P | F | C-15 fails: no "what breaks if moved" in table entries |
| 4 | V-02 | **130/135** | YES | F | P | C-14 fails: implicit contrast only, no structural choice named |

---

### Hypotheses Resolved

**R3-H01 (C-14 phrasing)**: RESOLVED — "defeats" is not required. V-04's "breaks that pattern by requiring" passes C-14. The criterion requires naming the failure mode AND the structural choice; the verb form is flexible.

**R3-H02 (C-15 depth)**: RESOLVED — Compact "what breaks if moved" notes pass. V-03's one-sentence consequence entries ("Moved later: design targets an unvalidated problem") satisfy C-15. Prose depth is not required.

**R3-H03 (density regression)**: RESOLVED — Adding C-14 + C-15 caused no regression in prior criteria. V-03, V-04, V-05 all score 135. Instruction density is not a problem.

**R3-H04 (R2 V-05 C-15 failure cause)**: RESOLVED — V-01 inherits R2 V-05's table and fails C-15 again. The gap is absence of "what breaks if moved" reasoning, not entry depth. V-01's entries are slightly richer than R2's ("nothing downstream can start without them") but still lack consequence reasoning. The "if moved" clause is what distinguishes pass from fail.

---

### Excellence Signals (New Patterns)

1. **Compact consequence clause is sufficient for C-15** — A single sentence naming one consequence of displacement ("Moved later: design targets an unvalidated problem") passes C-15. Prose paragraphs are not required. Minimum form = position rationale + one consequence-of-displacement sentence.

2. **C-14 phrasing is verb-agnostic** — Any explicit contrast form naming failure mode + structural choice passes: "defeats that by," "breaks that pattern by requiring," and "defeats that failure mode specifically by" are all equivalent. The criterion is structural (presence of both elements), not lexical (specific verb).

3. **V-03 is the efficient frontier** — Minimum form of both C-14 and C-15 achieves the ceiling score (135/135) with lower instruction density than V-04/V-05. V-03 is the recommended canonical form going forward.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["compact consequence clause sufficient for C-15: one sentence naming displacement consequence passes without prose depth", "C-14 phrasing is verb-agnostic: any explicit contrast naming failure mode + structural choice passes regardless of verb form", "V-03 minimal form reaches ceiling score — compact implementation of both C-14 and C-15 is the efficient frontier"]}
```
