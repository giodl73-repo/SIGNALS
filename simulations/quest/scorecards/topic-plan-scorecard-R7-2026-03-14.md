## Round 7 Scoring — topic-plan (v6 rubric, C-01–C-27)

---

### V-01 — Cognitive Role Sequence

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Read strategy | PASS | Step 1a Stated-Field Extractor role reads strategy.md explicitly |
| C-02 | Read signals | PASS | Step 2 globs and reads every artifact |
| C-03 | Delta not inventory | PASS | Step 3: "Stop. Before building the findings table, write the name of the anti-pattern you are guarding against." |
| C-04 | Typed proposals | PASS | Step 6 table with ADD/REMOVE/REPRIORITIZE typed rows |
| C-05 | Confirm gate | PASS | Step 8: "Reply YES to apply" |
| C-06 | Evidence per change | PASS | Step 6 Evidence col |
| C-07 | Before/after diff | PASS | Step 7 diff table |
| C-08 | All three types | PASS | Step 6 verbatim null rows for all three types |
| C-09 | Namespace gaps | PASS | Step 4 enumerates all 9 by name with Stage-Relative Status |
| C-10 | Conflicting signals | PASS | Step 5 with verbatim null-case row |
| C-11 | Typed confirmation verb | PASS | Step 8 YES |
| C-12 | Explicit no-change rows | PASS | ADD-0 / REMOVE-0 / REPRIORITIZE-0 verbatim null rows |
| C-13 | Inline evidence in diff | PASS | Step 7 Evidence col `[file.md — ≤10 word finding]` format |
| C-14 | Anti-inventory warning | PASS | Step 3 instructs model to name the anti-pattern before proceeding |
| C-15 | All 9 namespaces named | PASS | Step 4 table enumerates all 9 |
| C-16 | Two-level traceability | PASS | Step 6 Delta Finding col + Evidence col; Assumption root in Step 3 |
| C-17 | Explicit no-conflicts | PASS | Step 5 CF-00 null row verbatim |
| C-18 | Structured delta format | PASS | Step 3 "Strategy assumed / Signal revealed" format + F-00 null case |
| C-19 | Diff Proposal ID col | PASS | Step 7 Proposal col |
| C-20 | Delta Finding col | PASS | Step 6 Delta Finding with N/A null rows |
| C-21 | Column-completeness declaration | PASS | "The following columns are mandatory. Do not omit any column." at every template |
| C-22 | Anti-pattern checkpoint | PASS | Step 3: "Stop. Before building the findings table, write the name. Do not proceed until you have written the label." |
| C-23 | Pre-reproduced null templates | PASS | All 6 null outcomes with verbatim text + "Do not omit" |
| C-24 | Unstated-assumption extraction | PASS | Step 1b Assumption Archaeologist role; systematic scan (a-e); Assumption ID table; "Contradicted by a signal?" back-fill col |
| C-25 | Inertia cost column | PASS | Step 6 "If unchanged" col with explicit requirement to name gap that persists |
| C-26 | Schema-first priming | **PARTIAL** | Per-table declarations only; no upfront consolidated ★ schema block before Step 1 |
| C-27 | Cascade checkpoints | **PARTIAL** | Step 3 anti-pattern checkpoint only; no schema-commitment checkpoints at proposals/diff |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 17 PASS + 2 × 0.5 = 18.0 / 19 → 18/19 × 95 = **90.0 pts**  
**V-01 Total: 180.0**

---

### V-02 — Conversational Decision Register

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Read strategy | PASS | Step 1 reads strategy.md for both stated fields and unstated assumptions |
| C-02 | Read signals | PASS | Step 2 globs and reads all artifacts |
| C-03 | Delta not inventory | PASS | Step 3: "Before you build the findings table, write the name of the failure mode you are guarding against." |
| C-04 | Typed proposals | PASS | Step 6 typed table |
| C-05 | Confirm gate | PASS | Step 8 YES |
| C-06 | Evidence per change | PASS | Step 6 Evidence col |
| C-07 | Before/after diff | PASS | Step 7 |
| C-08 | All three types | PASS | Verbatim null rows |
| C-09 | Namespace gaps | PASS | Step 4 all 9 by name |
| C-10 | Conflicting signals | PASS | Step 5 with CF-00 null |
| C-11 | Typed confirmation verb | PASS | YES |
| C-12 | Explicit no-change rows | PASS | Verbatim null rows |
| C-13 | Inline evidence in diff | PASS | Step 7 Evidence col |
| C-14 | Anti-inventory warning | PASS | Step 3 names the failure mode explicitly |
| C-15 | All 9 namespaces named | PASS | Step 4 |
| C-16 | Two-level traceability | PASS | Delta Finding + Evidence cols |
| C-17 | Explicit no-conflicts | PASS | CF-00 verbatim |
| C-18 | Structured delta format | PASS | "Strategy assumed / Signal revealed" + F-00 null |
| C-19 | Diff Proposal ID col | PASS | Step 7 Proposal col |
| C-20 | Delta Finding col | PASS | Step 6 with N/A null rows |
| C-21 | Column-completeness declaration | PASS | Upfront table: "All column sets above are mandatory. If a table is missing any of its key columns, the output is incomplete." |
| C-22 | Anti-pattern checkpoint | PASS | Step 3 instructs model to write the failure mode name — verifiable in output |
| C-23 | Pre-reproduced null templates | PASS | All null outcomes with "Do not omit" |
| C-24 | Unstated-assumption extraction | PASS | Step 1 Unstated assumptions section; "Why this matters for delta detection" col; last col is delta-candidate reasoning |
| C-25 | Inertia cost column | PASS | "If unchanged" col + Step 6 purpose framing: "A proposal that can't answer the second question is a preference, not a decision." |
| C-26 | Schema-first priming | PASS | Upfront output-shape table before Step 1: "Before you read a single file, review this output shape." All six tables with key columns declared mandatory |
| C-27 | Cascade checkpoints | **PARTIAL** | Step 3 anti-pattern checkpoint only; no schema-commitment verbatim statements at proposals/diff |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 18 PASS + 1 × 0.5 = 18.5 / 19 → 18.5/19 × 95 = **92.5 pts**  
**V-02 Total: 182.5**

---

### V-03 — Reversibility Dimension

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Read strategy | PASS | Step 1 reads strategy.md; "What it assumed without naming" row mandatory |
| C-02 | Read signals | PASS | Step 2 globs and reads |
| C-03 | Delta not inventory | PASS | Step 3: "Stop here. Name the anti-pattern you are guarding against at this step." |
| C-04 | Typed proposals | PASS | Step 6 typed table |
| C-05 | Confirm gate | PASS | Step 8 YES |
| C-06 | Evidence per change | PASS | Step 6 Evidence col |
| C-07 | Before/after diff | PASS | Step 7 |
| C-08 | All three types | PASS | Verbatim null rows for all three |
| C-09 | Namespace gaps | PASS | Step 4 all 9 by name |
| C-10 | Conflicting signals | PASS | Step 5 with CF-00 null |
| C-11 | Typed confirmation verb | PASS | YES |
| C-12 | Explicit no-change rows | PASS | Verbatim null rows |
| C-13 | Inline evidence in diff | PASS | Step 7 + checkpoint commits to it |
| C-14 | Anti-inventory warning | PASS | Step 3 names the anti-pattern |
| C-15 | All 9 namespaces named | PASS | Step 4 |
| C-16 | Two-level traceability | PASS | Delta Finding + Evidence cols |
| C-17 | Explicit no-conflicts | PASS | CF-00 verbatim |
| C-18 | Structured delta format | PASS | "Strategy assumed / Signal revealed" + F-00 null |
| C-19 | Diff Proposal ID col | PASS | Step 7 Proposal col, committed in Step 7 verbatim checkpoint |
| C-20 | Delta Finding col | PASS | Step 6 Delta Finding, committed in Step 6 verbatim checkpoint |
| C-21 | Column-completeness declaration | PASS | Per-table "mandatory. Do not omit" + checkpoints at proposals and diff |
| C-22 | Anti-pattern checkpoint | PASS | Step 3 stop+name + Step 6 verbatim schema statement + Step 7 verbatim schema statement |
| C-23 | Pre-reproduced null templates | PASS | All null outcomes with verbatim + "Do not omit" |
| C-24 | Unstated-assumption extraction | PASS | Step 1 "What it assumed without naming" row (mandatory); R6 V-05 mechanism |
| C-25 | Inertia cost column | PASS | "If unchanged" + Reversibility cols; three-value taxonomy distinguishes trajectory from current state |
| C-26 | Schema-first priming | **PARTIAL** | Per-table + proposals/diff checkpoints but no upfront consolidated ★ schema block before Step 1 |
| C-27 | Cascade checkpoints | PASS | Step 3 stop+name + Step 6 verbatim schema statement + Step 7 verbatim schema statement |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 18 PASS + 1 × 0.5 = 18.5 / 19 → 18.5/19 × 95 = **92.5 pts**  
**V-03 Total: 182.5**

---

### V-04 — Role Sequence + Schema-First Priming

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Read strategy | PASS | Step 1a Stated-Field Extractor role |
| C-02 | Read signals | PASS | Step 2 globs and reads |
| C-03 | Delta not inventory | PASS | Step 3: stop + produce anti-pattern label + delta definition (IS vs IS NOT) |
| C-04 | Typed proposals | PASS | Step 6 typed table |
| C-05 | Confirm gate | PASS | Step 8 YES |
| C-06 | Evidence per change | PASS | Step 6 Evidence col |
| C-07 | Before/after diff | PASS | Step 7 |
| C-08 | All three types | PASS | Verbatim null rows |
| C-09 | Namespace gaps | PASS | Step 4 all 9 by name |
| C-10 | Conflicting signals | PASS | Step 5 with CF-00 null |
| C-11 | Typed confirmation verb | PASS | YES |
| C-12 | Explicit no-change rows | PASS | Verbatim null rows |
| C-13 | Inline evidence in diff | PASS | Step 7 + diff checkpoint |
| C-14 | Anti-inventory warning | PASS | Step 3 stop+name+contrast |
| C-15 | All 9 namespaces named | PASS | Step 4 |
| C-16 | Two-level traceability | PASS | Delta Finding + Evidence cols; Assumption root in delta table |
| C-17 | Explicit no-conflicts | PASS | CF-00 verbatim |
| C-18 | Structured delta format | PASS | Structured delta format + F-00 null |
| C-19 | Diff Proposal ID col | PASS | Step 7 Proposal col, committed at Step 7 checkpoint |
| C-20 | Delta Finding col | PASS | Step 6 Delta Finding, committed at Step 6 checkpoint |
| C-21 | Column-completeness declaration | PASS | Upfront ★ schema + per-table "mandatory. Do not omit." |
| C-22 | Anti-pattern checkpoint | PASS | Step 3 stop+name+contrast (both label AND definition); Step 6 verbatim checkpoint; Step 7 verbatim checkpoint |
| C-23 | Pre-reproduced null templates | PASS | All null outcomes with verbatim + "Do not omit" |
| C-24 | Unstated-assumption extraction | PASS | Step 1b Assumption Archaeologist role; Likelihood column forces prioritization; systematic scan (a-e) |
| C-25 | Inertia cost column | PASS | "If unchanged" col + committed at Step 6 checkpoint: "If unchanged ★" in schema statement |
| C-26 | Schema-first priming | PASS | Upfront ★ schema block lists all 6 tables with all mandatory columns before Step 1a; "Do not omit any ★ column. A table missing any ★ column fails schema validation." |
| C-27 | Cascade checkpoints | PASS | Step 3 (stop+name+contrast) + Step 6 verbatim schema commitment + Step 7 verbatim schema commitment = 3 independent auditable points |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 19/19 PASS → 95 pts  
**V-04 Total: 185.0**

---

### V-05 — Full Stack

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Read strategy | PASS | Step 1a Stated-Field Extractor role |
| C-02 | Read signals | PASS | Step 2 globs and reads |
| C-03 | Delta not inventory | PASS | Step 3: stop + anti-pattern label + IS/IS NOT delta definition; back-fill Contradicted? col after Step 3 |
| C-04 | Typed proposals | PASS | Step 6 typed table |
| C-05 | Confirm gate | PASS | Step 8 YES |
| C-06 | Evidence per change | PASS | Step 6 Evidence col |
| C-07 | Before/after diff | PASS | Step 7 |
| C-08 | All three types | PASS | Verbatim null rows; Step 6 checkpoint names them explicitly |
| C-09 | Namespace gaps | PASS | Step 4 all 9 by name |
| C-10 | Conflicting signals | PASS | Step 5 with CF-00 null |
| C-11 | Typed confirmation verb | PASS | YES |
| C-12 | Explicit no-change rows | PASS | Verbatim null rows committed by name in Step 6 checkpoint |
| C-13 | Inline evidence in diff | PASS | Step 7 + checkpoint commits to it |
| C-14 | Anti-inventory warning | PASS | Step 3 stop+name+contrast |
| C-15 | All 9 namespaces named | PASS | Step 4 |
| C-16 | Two-level traceability | PASS | Delta Finding + Evidence cols + schema-level traceability obligation with hop notation |
| C-17 | Explicit no-conflicts | PASS | CF-00 verbatim |
| C-18 | Structured delta format | PASS | Structured delta format + F-00 null; back-fill Contradicted? col enforces Step 3 → Step 1b return |
| C-19 | Diff Proposal ID col | PASS | Step 7 Proposal col "entry point into full traceability chain" — committed at Step 7 checkpoint |
| C-20 | Delta Finding col | PASS | Step 6 Delta Finding; committed at Step 6 checkpoint alongside null-row names |
| C-21 | Column-completeness declaration | PASS | Upfront ★ schema + per-table "mandatory. Do not omit." |
| C-22 | Anti-pattern checkpoint | PASS | Step 3 (stop+name+contrast) + Step 6 (schema+null-rows double-commit) + Step 7 (schema+traceability) = 3 points |
| C-23 | Pre-reproduced null templates | PASS | All null outcomes verbatim + "Do not omit"; null-row names explicitly committed in Step 6 checkpoint |
| C-24 | Unstated-assumption extraction | PASS | Step 1b Assumption Archaeologist role; Likelihood col; Contradicted? deferred-fill col; explicit back-fill obligation in Step 3 |
| C-25 | Inertia cost column | PASS | "If unchanged" + Reversibility cols + committed at Step 6 checkpoint: "If unchanged ★ (specific degradation — not 'nothing changes'), Reversibility ★" |
| C-26 | Schema-first priming | PASS | Upfront ★ schema with Reversibility ★ in Proposals + Traceability obligation statement, all before Step 1a |
| C-27 | Cascade checkpoints | PASS | Step 3 (stop+name+contrast) + Step 6 (commits schema AND null-row names simultaneously = double weight) + Step 7 (commits schema + traceability chain entry point) |

**Essential**: 5/5 = 60 pts  
**Recommended**: 3/3 = 30 pts  
**Aspirational**: 19/19 PASS → 95 pts  
**V-05 Total: 185.0**

---

### Score Summary

| Variation | Essential | Recommended | Aspirational | Total | All Essential |
|-----------|-----------|-------------|-------------|-------|---------------|
| V-01 | 60 | 30 | 90.0 (18/19) | **180.0** | YES |
| V-02 | 60 | 30 | 92.5 (18.5/19) | **182.5** | YES |
| V-03 | 60 | 30 | 92.5 (18.5/19) | **182.5** | YES |
| V-04 | 60 | 30 | 95.0 (19/19) | **185.0** | YES |
| V-05 | 60 | 30 | 95.0 (19/19) | **185.0** | YES |

**Ranking**: V-04 = V-05 (185) > V-02 = V-03 (182.5) > V-01 (180)

V-01 and V-02 are the deliberate partial-enforcement isolations; their depth-layer improvements (role sequence, conversational register) achieve full C-24/C-25 credit but the enforcement gaps (C-26 or C-27 partial) hold them below the ceiling. V-03's single partial is C-26 only — it achieved C-27 through the Step 3+6+7 checkpoint cascade, so it ties V-02 despite a different partial. V-04 and V-05 close all gaps; V-05 carries richer implementations across every v6 criterion.

---

### Excellence Signals from V-05

**1. Reversibility as a trajectory claim, not a current-state synonym**

The three-value taxonomy (*Reversible at same cost / Gets harder / Becomes impossible*) forces the model to classify the *direction of change* of a gap over time, not just its current existence. "Gets harder" and "Becomes impossible" cannot be pattern-matched from the delta finding — they require reasoning about what happens to the gap if no action is taken. This converts C-25's "If unchanged" column from a restatement of the finding to a time-pressure commitment. Round 8 candidate: this could become C-28 with a specific pass condition requiring at least one non-"Reversible" classification with a named causal mechanism.

**2. Deferred back-fill column in the assumption table creates bidirectional audit**

Step 1b's "Contradicted?" column is explicitly left blank at Step 1 and filled in Step 3. This creates a named obligation that runs in both directions: the finding table references the assumption (Assumption root A-NN), and the assumption table is updated to record which findings contradicted it. A reviewer can audit the chain starting from either table. V-04 has the Assumption Archaeologist role and Likelihood column but lacks the explicit back-fill column — this is V-05's strongest C-24 mechanism and the most auditable form of assumption-to-finding linkage seen across all rounds.

**3. Schema-level traceability obligation with hop-by-hop notation**

V-05's upfront schema block includes: *"Every Proposal row must be traceable from the diff (Proposal ID) → to the proposal table (Delta Finding) → to the findings table (Finding ID) → to the assumption table (Assumption root). A Proposal row with a missing Delta Finding column, or a Finding row with a missing Assumption root column, breaks the traceability chain."* This converts the three-level chain from a structurally available path (present since C-16/C-19/C-20) to a named schema violation if any hop is missing. The hop notation (→) makes the chain navigable from the diff backward — entry point is the Proposal column in the diff table, not the assumption table. Round 8 candidate: explicit chain-break language in the schema could become C-28.

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["Reversibility taxonomy (Reversible at same cost / Gets harder / Becomes impossible) converts the inertia column from current-state description to a trajectory claim — the model must reason about time pressure, not pattern-match from the delta finding", "Deferred back-fill column in assumption table (Contradicted? filled in Step 3, not Step 1) creates bidirectional audit — chain is auditable from assumption forward to finding and from finding back to assumption", "Schema-level traceability obligation with hop-by-hop notation (diff Proposal → Delta Finding → Finding ID → Assumption root) makes chain breaks schema violations rather than structural omissions — entry point navigable from any hop"]}
```
