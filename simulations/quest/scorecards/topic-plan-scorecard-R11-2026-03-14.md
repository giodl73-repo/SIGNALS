## Round 11 Scoring — topic:plan (v10 rubric, 235 pts)

---

### Scoring Matrix

**Essential (C-01–C-05)**

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Reads strategy.md | PASS | PASS | PASS | PASS | PASS |
| C-02 | Reads signal artifacts | PASS | PASS | PASS | PASS | PASS |
| C-03 | Identifies delta not inventory | PASS | PASS | PASS | PASS | PASS |
| C-04 | Proposes typed changes | PASS | PASS | PASS | PASS | PASS |
| C-05 | Confirmation gate | PASS | PASS | PASS | PASS | PASS |

All five: **5/5 essential pass → 60 pts**

---

**Recommended (C-06–C-08)**

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Signal evidence per change | PASS | PASS | PASS | PASS | PASS |
| C-07 | Before/after diff | PASS | PASS | PASS | PASS | PASS |
| C-08 | All three change types | PASS | PASS | PASS | PASS | PASS |

All five: **3/3 recommended → 30 pts**

---

**Aspirational (C-09–C-37)**

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|-----------|------|------|------|------|------|---------------|
| C-09 | Namespace coverage gaps | PASS | PASS | PASS | PASS | PASS | All 9 namespaces by name, stage-relative status column |
| C-10 | Conflicting signals | PASS | PASS | PASS | PASS | PASS | Conflict Audit table with null case CF-00 in all |
| C-11 | Typed confirmation verb | PASS | PASS | PASS | PASS | PASS | "Reply **YES**" in all |
| C-12 | Explicit no-change rows | PASS | PASS | PASS | PASS | PASS | ADD-0, REMOVE-0, REPRIORITIZE-0 null rows verbatim |
| C-13 | Inline evidence brackets in diff | PASS | PASS | PASS | PASS | PASS | `[file.md — ≤10 word finding]` in diff schema + commitment |
| C-14 | Anti-inventory warning at delta step | PASS | PASS | PASS | PASS | PASS | "Write the name of the anti-pattern" instruction; V-03/V-04/V-05 additionally provide labeled PASS/FAIL exhibit |
| C-15 | All 9 namespaces in gap audit | PASS | PASS | PASS | PASS | PASS | scout/draft/review/flow/trace/prove/listen/program/topic enumerated |
| C-16 | Two-level traceability chain | PASS | PASS | PASS | PASS | PASS | Delta Finding column + Evidence column in proposals = proposal→finding→artifact |
| C-17 | Absence declared at conflict audit | PASS | PASS | PASS | PASS | PASS | CF-00 null row + "Do not omit this table" |
| C-18 | Structured delta format per finding | PASS | PASS | PASS | PASS | PASS | "Strategy assumed [X] / Signal revealed [Y]" format + F-00 null case |
| C-19 | Diff Proposal ID cross-reference | PASS | PASS | PASS | PASS | PASS | "Proposal" column in diff table linking to ADD-N / REPRIORITIZE-N |
| C-20 | Delta Finding column in proposals | PASS | PASS | PASS | PASS | PASS | Column present for all types; null rows carry "Delta Finding: N/A" |
| C-21 | Column-completeness declarations | PASS | PASS | PASS | PASS | PASS | "The following columns are mandatory. Do not omit any column." at delta, proposals, and diff steps |
| C-22 | Active anti-pattern self-naming | PASS | PASS | PASS | PASS | PASS | "Stop. Before building the findings table, write the name of the anti-pattern" |
| C-23 | Pre-reproduced null-case templates | PASS | PASS | PASS | PASS | PASS | No-signals, delta F-00, CF-00, ADD-0/REMOVE-0/REPRIORITIZE-0 all with "Do not omit" |
| C-24 | Unstated assumption extraction | PASS | PASS | PASS | PASS | PASS | Step 2 "Assumption Archaeologist — Extract phase" with explicit scan |
| C-25 | Inertia cost column | PASS | PASS | PASS | PASS | PASS | V-01/V-03/V-04: "If unchanged"; V-02/V-05: "Status quo retains" (same function, stronger framing) |
| C-26 | Schema-first priming | PASS | PASS | PASS | PASS | PASS | Output Schema declared before Step 0/1 for all; before any file read |
| C-27 | Cascade commitment checkpoints | PASS | PASS | PASS | PASS | PASS | Verbatim schema statements at proposals step AND diff step in all |
| C-28 | Named role + scan dimensions | PASS | PASS | PASS | PASS | PASS | "Assumption Archaeologist" role + 5 explicit dimensions (a–e) |
| C-29 | Back-fill column | PASS | PASS | PASS | PASS | PASS | "[pending]" → Contradicted/Supported/No signal coverage adjudication in Step 3b |
| C-30 | Forward-reasoning columns | PASS | PASS | PASS | PASS | PASS | "Why this matters for delta detection" + "Delta candidate? [yes/no; update to yes—F-NN]" |
| C-31 | Proposal decision-gate framing | PASS | PASS | PASS | PASS | PASS | "a row that cannot name a specific degradation is a preference, not a decision" in all |
| C-32 | Reversibility taxonomy | PASS | PASS | PASS | PASS | PASS | Three-value enum: (1)/(2)/(3); prose-prohibition in CONTRACT Rule 1 |
| C-33 | Assumption table in upfront schema | PASS | PASS | PASS | PASS | PASS | All 5 columns in Output Schema block before Step 1 |
| C-34 | Enumerated columns at both sites | PASS | PASS | PASS | PASS | PASS | CONTRACT Rule 1 lists valid values; commitment checkpoints cite "Rule 1" + values |
| C-35 | Columns independently populated | PASS | PASS | PASS | PASS | PASS | Rule 2 decision-question + fail examples (row key, restatement, pointer) in all |
| C-36 | Named pre-schema rule block | PASS | PASS | PASS | PASS | PASS | "COLUMN CONTRACT" block precedes Output Schema in all; numbered Rule 1/2; checkpoints cite "Rule 1" |
| C-37 | Operationalized independence test | **PARTIAL** | **PARTIAL** | PASS | PASS | PASS | See detail below |

---

**C-37 Evidence Detail — the deciding criterion**

| Variation | Decision-question | Fail examples | Pass examples | Verdict |
|-----------|------------------|---------------|---------------|---------|
| V-01 | ✓ in CONTRACT Rule 2 and column header | ✓ 3 explicit: row key / restatement / pointer | ✗ only implicit ("phrase from strategy.md") | **PARTIAL** |
| V-02 | ✓ same as V-01 | ✓ 3 explicit | ✗ only implicit | **PARTIAL** |
| V-03 | ✓ in CONTRACT Rule 2 | ✓ 4 explicit + labeled FAIL rows in Step 2 | ✓ 3 explicit: "teams run scout before draft" / "signal count threshold never defined" / "the phrase 'gather evidence first'" | **PASS** |
| V-04 | ✓ in CONTRACT Rule 2 | ✓ same as V-03 | ✓ same as V-03; Step 2 explicitly references "PASS/FAIL exhibit from COLUMN CONTRACT" | **PASS** |
| V-05 | ✓ in CONTRACT Rule 2 | ✓ same as V-03 | ✓ same as V-03 | **PASS** |

C-37 requires *explicit* pass examples embedded in the column definition. V-01/V-02 describe what a passing cell looks like in general terms but provide no concrete example values. V-03/V-04/V-05 provide labeled, quoted pass examples that are traceable to strategy.md format — symmetric with the fail examples.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational (pass count) | Composite |
|-----------|-----------|-------------|---------------------------|-----------|
| V-01 | 60 (5/5) | 30 (3/3) | 142.5 (28.5/29 — C-37 PARTIAL) | **232.5** |
| V-02 | 60 (5/5) | 30 (3/3) | 142.5 (28.5/29 — C-37 PARTIAL) | **232.5** |
| V-03 | 60 (5/5) | 30 (3/3) | 145 (29/29) | **235** |
| V-04 | 60 (5/5) | 30 (3/3) | 145 (29/29) | **235** |
| V-05 | 60 (5/5) | 30 (3/3) | 145 (29/29) | **235** |

**Formula applied:** `(5/5 × 60) + (3/3 × 30) + (aspirational_pass/29 × 145)` where PARTIAL = 0.5 pass

---

### Ranking

| Rank | Variations | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-03, V-04, V-05 (tied) | 235/235 | ✓ |
| 2 | V-01, V-02 (tied) | 232.5/235 | ✓ |

All five variations clear the golden threshold (≥ 140, all essential pass).

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — Symmetric PASS/FAIL exhibits at the delta anti-pattern checkpoint (V-03/V-04/V-05)**
The Step 4 checkpoint in V-03 adds a labeled exhibit table immediately before the findings table:
```
| PASS — this is a delta    | "F-01: Strategy assumed scout signals suffice / Signal revealed draft completes without scout" |
| FAIL — this is inventory  | "S-01 covers namespace coverage" or "we have 3 signals in scout"                             |
```
This extends the C-22 mechanism (model produces the anti-pattern label) into a *bidirectional* discrimination exhibit. C-14 requires the prompt to name the failure mode; C-22 requires the model to reproduce it. Neither requires a concrete passing delta example. The exhibit shows what a correct finding structurally looks like — blocking both inventory rows that restate signal metadata AND inventory rows that list signal counts. The PASS row forces the model to hold the correct format in working memory before generating findings.

**Signal 2 — Pre-read hypothesis commitment (V-01/V-04/V-05)**
Step 0 runs before any file read. The model commits to predictions (H-01: predicted assumption, expected signal direction, expected delta). Delta Findings gain a "Hypothesis match" column: *H-N confirmed* or *Surprise — not hypothesized*. A delta finding that matches no prior hypothesis is flagged as highest-value. This makes the delta step falsifiable: the model cannot retroactively claim it "anticipated" a gap when no H-row matches. Surprise findings expose genuine blindspots — assumptions the hypothesis generation failed to anticipate, which are categorically more valuable than confirmed ones. No existing criterion targets pre-execution prediction commitment or surprise-flagging.

**Signal 3 — Status-quo framing with Inertia Cost Audit table (V-02/V-05)**
V-02 reframes the opening premise: the current strategy is the status quo; each proposal is a challenger. "If unchanged" becomes "Status quo retains" — inverting the column from passive (what degrades) to adversarial (what the status quo keeps and why that retention eventually fails). The Inertia Cost Audit table (Step 7a) forces a signal-level ranking *before* proposals are built: for each signal, what is the current strategy's position and what does it cost to retain it? This separates the audit step from the proposal step — inertia cost is evaluated at the signal level, not only at the proposal level. C-25 and C-31 measure column existence and disqualification framing; neither measures signal-level pre-proposal inertia analysis.

**Signal 4 — 4-rule COLUMN CONTRACT with evidence provenance and null completeness (V-05)**
V-05 elevates two constraints from per-step instructions to pre-schema binding rules:
- **Rule 3 (evidence provenance)**: evidence cells must trace to artifact filenames, not to other output columns or to strategy.md
- **Rule 4 (null-case completeness)**: every mandatory section has a verbatim null template; skipping when null fails the rule regardless of other output

Both constraints previously appeared as per-step instructions encountered under context pressure. Elevating to CONTRACT rules means they are encountered once, before any schema column, as part of the binding architectural layer. Rule 3 specifically closes a gap in C-16: the two-level chain (proposal → delta → artifact) can be structurally present but broken if the Evidence cell points to a delta finding row rather than a signal file. Rule 4 extends C-23 (which requires the templates) by making the binding explicit at the architectural level.

---

### Why V-01 and V-02 are PARTIAL on C-37 despite having the decision-question

The gap is exhibit symmetry, not the test itself. Both V-01 and V-02 embed the decision-question ("Can I fill this cell without reading the source document?") in the column header — satisfying the core C-37 mechanism. What they lack is an *explicit, labeled pass example* showing what a correct cell looks like (e.g., `"teams run scout before draft" — specific phrase from strategy.md`). The fail examples establish a recognition scaffold for known shortcuts (row key, restatement, pointer). But without a paired pass example, a novel shortcut that doesn't resemble any of the three named failure modes can still satisfy the column definition while violating its intent. The pass example shows what *correct* looks like, not just what *incorrect* looks like — completing the bidirectional discrimination.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["Pre-read hypothesis commitment table (Step 0 before any file read) with Hypothesis match column in Delta Findings — scores findings as confirmed vs. surprise, making the delta step falsifiable and surfacing genuine blindspots that the hypothesis generation missed", "Symmetric PASS/FAIL exhibit at the delta anti-pattern checkpoint — adds a labeled two-row exhibit (PASS: a correct delta finding / FAIL: an inventory row) immediately before the findings table, extending C-22 from label-reproduction to bidirectional discrimination between structurally correct and structurally incorrect outputs", "Inertia Cost Audit as a pre-proposal signal-level table — evaluates every signal against the current strategy before proposals are built, separating signal-level inertia analysis from proposal-level inertia cost framing (C-25/C-31 measure the proposals column; this measures the signal layer)", "4-rule COLUMN CONTRACT elevating evidence provenance (cells must trace to artifact filenames, not output columns) and null-case completeness to pre-schema binding architecture — closes the C-16 chain where an Evidence cell points to another output column instead of a signal artifact"]}
```
