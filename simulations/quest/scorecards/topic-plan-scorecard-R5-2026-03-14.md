Now I have everything needed. Let me score all 5 variations against the full C-01–C-23 rubric.

---

# `/quest:score` — topic-plan Round 5 (v5 rubric)

**Rubric**: v5 — C-01–C-23, 165 pts max
**Scoring formula**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 75)`
**Partial credit**: 0.5 pass per PARTIAL criterion

---

## Per-Criterion Evaluation

### Essential (C-01–C-05) — All variations

All five variations carry the essential mechanisms unchanged from Round 4.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy.md | PASS — Step 1 extracts 5 fields | PASS | PASS | PASS | PASS — enhanced: extracts unstated assumptions |
| C-02 Read signal artifacts | PASS — glob + read all | PASS | PASS | PASS | PASS |
| C-03 Delta not inventory | PASS — stop+name checkpoint at Step 3 | PASS — stop+name+contrast | PASS — explicit framing + stop+name | PASS — stop+name+contrast | PASS — stop+name, anchored to Step 1 commitments |
| C-04 Typed proposals | PASS — ADD/REMOVE/REPRIORITIZE table | PASS | PASS | PASS | PASS — adds inertia column |
| C-05 Confirmation gate | PASS — Step 8 YES gate, no auto-apply | PASS | PASS | PASS | PASS |

**Essential result**: 5/5 PASS in all variations → **60 pts each**

---

### Recommended (C-06–C-08) — All variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Evidence per change | PASS — Evidence col in proposals | PASS | PASS | PASS | PASS |
| C-07 Before/after diff | PASS — Step 7 diff table | PASS | PASS | PASS | PASS |
| C-08 All three change types | PASS — null rows for all types | PASS | PASS | PASS | PASS |

**Recommended result**: 3/3 PASS in all variations → **30 pts each**

---

### Aspirational (C-09–C-23) — Discriminator round

#### C-09 through C-20 (carried from Round 4)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Namespace gaps | PASS — Stage-Relative Status + Action Needed? | PASS | PASS | PASS | PASS — richer (Expected at stage? / Status / Gap? columns) |
| C-10 Conflicting signals | PASS — CF table + null row | PASS — prose null | PASS | PASS | PASS |
| C-11 Typed confirmation verb | PASS — "Reply YES" | PASS | PASS | PASS | PASS |
| C-12 Explicit no-change rows | PASS — verbatim ADD-0/REMOVE-0/REPRIORITIZE-0 | PASS | PASS — individually labeled | PASS | PASS |
| C-13 Inline evidence in diff | PASS — `[file.md — ≤10 word finding]` per row, no separate section | PASS — committed in checkpoint | PASS | PASS | PASS |
| C-14 Anti-inventory warning | **PARTIAL** — stop+name required but "plain inventory" label absent from prompt | **PARTIAL** — stop+name+contrast but label absent | **PASS** — "A plain inventory of signal files is not the delta" explicit in prompt | **PARTIAL** — stop+name+contrast, label absent | **PARTIAL** — stop+name, label absent |
| C-15 All 9 namespaces named | PASS — all 9 in table | PASS | PASS | PASS | PASS |
| C-16 Two-level traceability | PASS — Delta Finding col + Evidence col | PASS — committed in proposals checkpoint | PASS | PASS | PASS — enhanced: Delta Finding anchored to Step 1 commitments |
| C-17 Explicit no-conflicts | PASS — CF-00 verbatim row + "Do not omit this table" | PASS — prose statement + "Do not omit this section" | PASS — CF-00 verbatim row | PASS — CF-00 row | PASS |
| C-18 Structured delta format | PASS — "Strategy assumed [X] / Signal revealed [Y]" + F-00 stop condition | PASS | PASS | PASS | PASS |
| C-19 Diff Proposal ID column | PASS — Proposal col in Step 7 | PASS — committed in diff checkpoint | PASS | PASS | PASS |
| C-20 Delta Finding col in proposals | PASS — col present + null rows have "N/A" | PASS — committed in proposals checkpoint | PASS | PASS | PASS — inertia column adds causal depth requirement |

---

#### C-21 — Column-completeness declaration adjacent to each template

Rubric: explicit "The following columns are mandatory. Do not omit any column." sentence **adjacent** to each template definition (at minimum: proposals, diff, delta findings). Must appear in the prompt, not be inferred.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| **V-01** | Declaration present adjacent to ALL 6 structured tables: signal inventory (Step 2), delta findings (Step 3), namespace audit (Step 4), conflict table (Step 5), proposals (Step 6), diff (Step 7) | **PASS** |
| **V-02** | Declaration adjacent to proposals (Step 6) and diff (Step 7) only. Delta findings, signal inventory, namespace audit, conflict table — no adjacent declaration. The schema-commitment checkpoint replaces the declaration on those tables, but C-21 requires the sentence to appear adjacent, not be replaced by a checkpoint. | **PARTIAL** |
| **V-03** | No "The following columns are mandatory. Do not omit any column." sentence appears adjacent to any template anywhere in the prompt. Step 6 says only "All three types must appear" — insufficient per C-21's explicit sentence requirement. | **FAIL** |
| **V-04** | Upfront schema section has "Do not omit any ★ column" covering all tables globally. This is a blanket prohibition before execution, but C-21 requires adjacency at each template definition in the steps. The individual steps reference "Per schema (X)" without restating the prohibition. | **PARTIAL** |
| **V-05** | Declaration present adjacent to ALL 7 structured tables: Step 1 commitments, Steps 2–7. Same coverage as V-01, every table covered uniformly. | **PASS** |

---

#### C-22 — Active anti-pattern self-naming checkpoint at the delta step

Rubric: Prompt instructs the model to **stop and produce** the anti-pattern label as verifiable output before proceeding. Distinct from C-14 (prompt names the pattern).

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| **V-01** | Step 3: "Stop here. Write the name of the anti-pattern you are guarding against at this step." — single auditable checkpoint | **PASS** |
| **V-02** | Step 3: "Stop. Before building the findings table, produce: 1. Anti-pattern label: Name... Write the label. Do not omit this output." Step 6: schema-commitment statement before proposals. Step 7: schema-commitment statement before diff. — **3 independent auditable checkpoints** | **PASS** (strongest) |
| **V-03** | Step 3: "Stop here. Name the anti-pattern you are guarding against. Then proceed to the findings table." — single auditable checkpoint | **PASS** |
| **V-04** | Step 3: "Stop. Produce these two outputs: 1. Anti-pattern label: Name... (Write the label — do not skip.)" Step 6: schema confirmation statement. — **2 auditable checkpoints** | **PASS** |
| **V-05** | Step 3: "Stop here. Name the anti-pattern you are guarding against at this step. Then proceed to the findings table." — single checkpoint | **PASS** |

All PASS; quality varies: V-02 (3 checkpoints) > V-04 (2 checkpoints) > V-01/V-03/V-05 (1 checkpoint each).

---

#### C-23 — Pre-reproduced null-case templates for all mandatory null sections

Rubric: Every mandatory null section requires **(1) verbatim copy-paste text** + **(2) explicit "Do not omit" instruction**. Both required; either alone is insufficient.

Six conditions: (1) no signals, (2) all signals confirm / delta null, (3) no conflicts, (4) no ADD, (5) no REMOVE, (6) no REPRIORITIZE.

| Condition | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| (1) No signals | PASS — verbatim block + "Do not omit this output" | **PARTIAL** — quoted text but only "and stop", no "Do not omit" instruction | PASS — verbatim + "Do not omit this output" | **PARTIAL** — quoted text + "and stop", no "Do not omit" | PASS — verbatim + "Do not omit this output" |
| (2) Delta null | PASS — F-00 verbatim + "Do not omit this row" | PASS | PASS | PASS | PASS |
| (3) No conflicts | PASS — CF-00 verbatim + "Do not omit this table" | PASS — prose form + "Do not omit this section" | PASS — CF-00 verbatim + "Do not omit this table" | PASS | PASS |
| (4) No ADD | PASS — ADD-0 verbatim + "Do not omit any type row" | PASS | PASS — individually labeled section | PASS | PASS |
| (5) No REMOVE | PASS | PASS | PASS | PASS | PASS |
| (6) No REPRIORITIZE | PASS | PASS | PASS | PASS | PASS |

| Variation | Verdict | Note |
|-----------|---------|------|
| V-01 | **PASS** | All 6 covered with both requirements |
| V-02 | **PARTIAL** | 5/6 — no-signals case: verbatim text present but missing "Do not omit" instruction |
| V-03 | **PASS** | All 6, individually labeled with separate section headers |
| V-04 | **PARTIAL** | 5/6 — same gap as V-02 on no-signals case |
| V-05 | **PASS** | All 6 covered |

---

### Complete Aspirational Scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PARTIAL | PARTIAL | **PASS** | PARTIAL | PARTIAL |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | **PASS** | **PARTIAL** | **FAIL** | **PARTIAL** | **PASS** |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | **PASS** |
| **PASS count** | **14.5** | **13.5** | **14** | **13.5** | **14.5** |
| **Aspirational pts** | **72.5** | **67.5** | **70** | **67.5** | **72.5** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 72.5 | **162.5** |
| V-02 | 60 | 30 | 67.5 | **157.5** |
| V-03 | 60 | 30 | 70.0 | **160** |
| V-04 | 60 | 30 | 67.5 | **157.5** |
| V-05 | 60 | 30 | 72.5 | **162.5** |

---

## Rankings

| Rank | Variation | Score | Decisive factor |
|------|-----------|-------|-----------------|
| 1 (tie) | **V-05** | 162.5 | Full C-21/C-23 stack + inertia depth enriches C-16/C-20; PARTIAL only on C-14 |
| 1 (tie) | **V-01** | 162.5 | Full C-21/C-23 stack; PARTIAL only on C-14 |
| 3 | **V-03** | 160 | C-14 PASS (only variation with explicit "plain inventory" label) cancels against C-21 FAIL (no column declarations anywhere) |
| 4 (tie) | **V-02** | 157.5 | Strongest C-22 implementation (3 checkpoints) but loses pts on C-21 PARTIAL + C-23 PARTIAL |
| 4 (tie) | **V-04** | 157.5 | Schema-first priming is strong conceptually; C-21 and C-23 PARTIAL for same reasons as V-02 |

**Depth tiebreaker favors V-05**: V-05's inertia column and unstated-assumption extraction produce richer C-20/C-16 entries than V-01's equivalent mechanisms. Both score identically on the formula but V-05 generates more defensible outputs.

---

## Excellence Signals from Top Variation (V-05)

**Signal 1 — Uniform column-completeness declaration (C-21 pattern)**
Placing "The following columns are mandatory. Do not omit any column." adjacent to *every* table creates a structural baseline. The absence of the declaration on any table would become visible by contrast — the model has no ambiguous table to elide silently. Uniformity is the enforcement mechanism, not any single declaration.

**Signal 2 — Inertia column forces causal depth in proposals**
The "If unchanged: [gap that persists]" column in Step 6 makes mechanical Delta Finding fills structurally impossible. A model cannot put anything in the If-unchanged column without having traced the causal chain: assumption → gap → consequence. This is a depth-enforcement mechanism that works without adding instructions — the column shape does the work.

**Signal 3 — Unstated assumption extraction before signal reading**
Step 1's explicit "What it assumed without naming" row creates a pre-populated list of delta candidates before any signals are read. The model enters the delta step (Step 3) already holding concrete assumption targets rather than deriving them from signal accumulation alone. This makes C-03 more structurally self-enforcing.

**Note on C-14 residual gap (both V-01 and V-05)**: Neither variation explicitly names "plain inventory" in the prompt text — they require the model to name it (C-22 PASS) without planting the label (C-14 PARTIAL). V-03 resolves this cleanly ("A plain inventory of signal files is not the delta") at the cost of C-21. A Round 6 variation stacking V-03's C-14 mechanism with V-05's C-21/C-23 coverage would close the remaining 2.5-pt gap.

---

## Round 5 Meta-Pattern

R5 confirmed the enforcement-layer hypothesis: C-21 and C-23 coverage separated the leading variations from the pack, not C-22 (all five passed). The residual discriminator is C-14 (prompt labels the anti-pattern) vs. C-22 (model reproduces the label) — these two criteria pull in opposite directions across this round. V-03 optimized for C-14; V-01/V-05 optimized for C-21/C-23 at C-14's expense. A synthesis that achieves all three (C-14 PASS + C-21 PASS everywhere + C-23 PASS all 6) would score 165/165.

---

```json
{"top_score": 162.5, "all_essential_pass": true, "new_patterns": ["Inertia cost column in proposals forces causal depth — 'If unchanged' column makes mechanical Delta Finding fills structurally impossible by requiring consequence tracing", "Unstated assumption extraction in Step 1 creates a pre-populated delta candidate list before signal reading begins, making C-03 structurally self-enforcing"]}
```
