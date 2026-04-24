## Round 1 Scorecard — quest-variate

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-04 Phase gates (lifecycle emphasis) | **90** | NO |
| 2 | V-02 Fenced blocks (output format) | **90** | NO |
| 3 | V-03 Direct imperative (phrasing register) | **88** | NO |
| 4 | V-05 Critic-first (role sequence) | **85** | NO |
| 5 | V-01 Generator-then-critic (role sequence) | **40** | NO |

**Verdict: REJECT** — essential fails on C-01 and C-02.

---

**Root cause — V-01 structural corruption:**

The file was assembled with V-01's beginning dropped. What survived (lines 19–38) is the lower half of a complete body — Steps 1–4 and Constraints are sound — but the section header `## V-01`, the axes table column headers, and the inline `**Axis:**`/`**Hypothesis:**` block are all missing. The fragment `"or persona governs the run |"` is a dangling table row. This is a file-write truncation, not a content failure.

The V-01 design (generate → label → critique → output) is the cleanest process formulation in the set. If the body were complete, V-01 ranks 1–2 alongside V-04.

---

**Essential criteria:**
- C-01: **FAIL** (V-01 truncated)
- C-02: **FAIL** (V-01 no inline label block)
- C-03: **PASS** (all single-axis)
- C-04: **PASS** (5 variations present)

**Recommended:** 3/3 pass (C-05, C-06, C-07 all pass)

**Composite: 65**

---

**Top variation: V-04** — encodes axis-drift prevention as a structural stop condition, not an instruction. Phase 2's explicit single-axis check before proceeding is the only variation that mechanically prevents its own failure mode.

**Excellence signals:**
1. Stop conditions encode constraint, not instruction
2. Phase 1 forces hypothesis commitment before token spend
3. Explicit rewrite trigger in Phase 2 (not just a warning)

```json
{"top_score": 90, "all_essential_pass": false, "new_patterns": ["stop-conditions-encode-single-axis-invariant-structurally", "phase-gate-forces-hypothesis-commitment-before-generation"]}
```
Aspirational pass: 1/2**

```
Composite = (2/4 * 60) + (3/3 * 30) + (1/2 * 10) = 30 + 30 + 5 = 65
```

**Verdict: REJECT** -- C-01 and C-02 fail. Output is not usable as-is.

---

### Root cause

V-01 is a structural corruption, not a content failure. The body at lines 19-38 of the variations file is the lower half of a complete variation -- it contains Steps 1-4 and Constraints, which are sound. But the top of V-01 (the section header `## V-01`, the axes table with column headers, and the inline `**Axis:**`/`**Hypothesis:**` block) is missing. The fragment `"or persona governs the run |"` is a dangling table row from what should have been the role-sequence column in the axes table.

This is not a model failure during generation -- it is a file-write truncation: the variation file was assembled with V-01's beginning dropped.

**The actual V-01 skill body design is valid.** The generate-then-label-critique-output pattern is the cleanest process formulation in the set. If the body were complete, V-01 would rank 1-2 alongside V-04.

---

### Per-variation detail

**V-01 -- Role sequence (generator-then-critic)**
- C-01: FAIL -- body starts mid-table; `## V-01` header absent; axes table head truncated
- C-02: FAIL -- no inline `**Axis:**`/`**Hypothesis:**` block; only in index table
- C-03: PASS -- role sequence, single axis; distinct from V-05 (generator-first vs critic-first)
- C-05: PASS -- "prevents diff-leak failures" is specific and observable
- C-06: PASS -- generate-then-critique ordering is a real design choice
- C-09: FAIL -- intended as baseline but truncated body cannot anchor comparisons

**V-02 -- Output format (table index + fenced blocks)**
- C-01: PASS -- complete: SkillSpec input spec, index table, per-variation fenced block structure, axes list, rules
- C-02: PASS -- `**Axis:**` and `**Hypothesis:**` present inline
- C-03: PASS -- output format only
- C-05: PASS -- "reducing partial-body failures compared to prose-delimited output" is a specific, falsifiable comparison
- C-06: PASS -- fenced block + index is a genuine structural forcing function

**V-03 -- Phrasing register (direct imperative)**
- C-01: PASS -- complete: imperative framing, per-variation steps, label format, falsifiability guidance
- C-02: PASS -- inline labels present
- C-03: PASS -- phrasing register only
- C-05: PASS -- "model mirrors the register of the prompt" is an observable behavioral prediction
- C-06: PASS -- stripping all meta-commentary is a deliberate, non-trivial design choice

**V-04 -- Lifecycle emphasis (phase gates with stop conditions)**
- C-01: PASS -- complete 3-phase structure with Phase 1 (axis selection), Phase 2 (generation + check), Phase 3 (output)
- C-02: PASS -- inline labels present
- C-03: PASS -- lifecycle emphasis only
- C-05: PASS -- "reduces axis drift...each gate forces single-axis check before proceeding" is precise and falsifiable
- C-06: PASS -- explicit stop conditions between phases is a meaningfully distinct structural choice; no other variation does this

**V-05 -- Role sequence (critic-first)**
- C-01: PASS -- complete 4-step body (Analyze, Assign and hypothesize, Generate, Output)
- C-02: PASS -- inline labels present
- C-03: PASS -- role sequence only; critic-first is architecturally distinct from generator-first (V-01)
- C-05: PARTIAL PASS -- "more discriminating set of variations" is directionally specific but not crisply falsifiable; mechanism stated (critic's prior narrows hypothesis space) saves it
- C-06: PASS -- critic-first is a genuine design inversion; practitioner would consciously choose this

---

### Top variation: V-04 (phase gates with stop conditions)

V-04 wins by design principle: it encodes the #3 rubric failure mode (axis drift) as a structural impossibility, not a polite instruction. The stop conditions between phases mean a model cannot proceed from axis-selection to body-generation without writing a complete hypothesis -- and cannot proceed from generation to output without running a single-axis check. No other variation structurally prevents its own failure mode.

V-02 is a close second. Its fenced block format mechanically prevents partial bodies (C-01 fail mode) for the same reason -- the model must close the fence before moving on.

### Excellence signals from V-04

1. **Stop conditions encode constraint, not instruction** -- phase gates prevent axis drift structurally by requiring a single-axis check as a gate condition, not as a reminder. More reliable than instruction-based approaches.
2. **Phase 1 forces hypothesis commitment before token spend** -- requiring all 5 axis assignments and hypotheses before any body is written prevents drift into generation before the design space is mapped.
3. **Phase 2 rewrite trigger is explicit** -- "If two axes changed, stop and rewrite before continuing" gives the model a clear recovery path, not just a warning.

---

```json
{"top_score": 90, "all_essential_pass": false, "new_patterns": ["stop-conditions-encode-single-axis-invariant-structurally", "phase-gate-forces-hypothesis-commitment-before-generation"]}
```
