---

## program-plan Scorecard — Round 1

**Trace artifact**: placeholder (no golden file) — scores are prompt-predictive.

### Criterion Scores

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Valid YAML | PASS | PASS | PASS | PASS | PASS |
| C-02 | Echo contract | PASS | PASS | PASS | PASS | PASS |
| C-03 | Valid skills | FAIL | FAIL | FAIL | **PASS** | FAIL |
| C-04 | Non-trivial gates | FAIL | PASS | PASS | PASS | PASS |
| C-05 | Dependency order | FAIL | PASS | PASS | PASS | PASS |
| C-06 | Meaningful groupings | FAIL | PASS | PASS | PASS | PASS |
| C-07 | Gates ref artifacts | FAIL | PASS | PASS | PASS | PASS |
| C-08 | Descriptive names | PASS | PASS | PASS | PASS | PASS |
| C-09 | Strategic arc pacing | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| C-10 | Quantified gates | FAIL | FAIL | FAIL | **PASS** | **PASS** |

### Composite Scores

| Rank | Variation | Essential | Recommended | Aspirational | **Total** | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 | V-04 Role-Aware + Quantified Gates | 60 | 30 | 5 | **95** | **YES** |
| 2 | V-05 Inertia Contrast + Arc Strategy | 48 | 30 | 10 | **88** | NO |
| 3 | V-03 Phase-First | 48 | 30 | 5 | **83** | NO |
| 4 | V-02 Conversational/Imperative | 48 | 30 | 0 | **78** | NO |
| 5 | V-01 Schema-First (truncated) | 24 | 10 | 0 | **34** | NO |

### Key Findings

**V-04 is golden (95/100, all essential pass).** The decisive differentiator: it's the only variation that enumerates all 47 valid skill names inline — the sole reason V-03, V-05, and V-02 fail C-03 despite scoring >=80 composite.

**C-03 is the gating blocker for R1.** Four of five variations reference "the catalog" without listing it. One enumeration line in V-04 is worth 12 essential points.

**V-04's gap is C-09.** Actor-ordering implies breadth→depth→synthesis but doesn't require the model to argue the arc strategy. Adding V-03's or V-05's arc framing to V-04 would push a combined variation to 100.

**V-05's inertia framing** achieves the highest aspirational score (2/2, both C-09 and C-10) — more argued gates, required strategy statement — but the missing catalog kills it. This is the most promising R2 base: V-05 body + V-04's skill enumeration.

### Excellence Signals

- Enumerate valid skills by namespace inline — removes hallucination risk at the source (C-03)
- Actor-role framing grounds gate writing in concrete workflow transitions (C-07, C-05)
- Embed quantified gate syntax example directly in the requirement text (C-10)

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["enumerate all valid skill names inline to anchor against hallucination", "actor-role framing before gate-writing produces artifact-grounded transitions without extra instruction", "embed quantified gate syntax example in requirement text to drive machine-checkable output"]}
```
isk remains |
| C-04 | Gates non-trivial | PASS | Step 4: "Empty, vague, or trivial gate strings ('done', 'ready') are not acceptable" |
| C-05 | Dependency-ordered | PASS | Explicit: "scout before draft, draft before review/prove, review/prove before listen and metrics" |
| C-06 | Meaningful groupings | PASS | Step 3: coherent phase coaching with examples (discovery, design-validation, evidence-gathering) |
| C-07 | Gates reference artifacts | PASS | Step 4: "Reference specific artifact types by name" + example ">=2 scout artifacts present" |
| C-08 | Descriptive stage names | PASS | Stage name examples given: discovery, design-validation, evidence-gathering, synthesis |
| C-09 | Strategic arc pacing | FAIL | Breadth/depth ordering implied by dependency rule but arc strategy not required or framed |
| C-10 | Quantified gates | FAIL | One example given (">=2 scout artifacts") but not required; output may omit quantification |

```
Essential:    C-01 [P] C-02 [P] C-03 [F] C-04 [P] C-05 [P]
              Pass count: 4 / 5   -> 4 * 12 = 48 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [F] C-10 [F]
              Pass count: 0 / 2   -> 0 * 5  =  0 pts (of 10)

Composite score: 78 / 100
Golden: all essential pass NO  AND composite >= 80 NO  ->  [ ] YES  [X] NO
```

---

## V-03 — Phase-First

**Axis**: Lifecycle emphasis (evidence arc phases named before YAML)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Valid YAML structure | PASS | Step 5 produces program.yaml with specified fields |
| C-02 | Echo stage contract | PASS | Phase 5 defined as "Echo (auto, no skills): always present, always last" -- unambiguous |
| C-03 | All skills valid | FAIL | Valid namespaces listed; individual skill names not enumerated -- same hallucination risk |
| C-04 | Gates non-trivial | PASS | Gate defined per phase with artifact references; structure prevents trivial gates |
| C-05 | Dependency-ordered | PASS | Dependency rule explicit: "review skill that reads draft-spec cannot appear before draft stage" |
| C-06 | Meaningful groupings | PASS | 5-phase arc structure (breadth, design, depth, synthesis, echo) enforces cohesive grouping |
| C-07 | Gates reference artifacts | PASS | Step 4: "reference artifact types produced by prior phase by name" with example |
| C-08 | Descriptive stage names | PASS | Phase labels defined as arc phase names -- breadth-signals, design-draft, depth-signals, synthesis |
| C-09 | Strategic arc pacing | PASS | Entire structure IS the evidence arc: breadth -> design -> depth -> synthesis -> echo |
| C-10 | Quantified gates | FAIL | "at least one depth signal from Phase 3" -- non-zero but not a count threshold; no >= N syntax |

```
Essential:    C-01 [P] C-02 [P] C-03 [F] C-04 [P] C-05 [P]
              Pass count: 4 / 5   -> 4 * 12 = 48 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [F]
              Pass count: 1 / 2   -> 1 * 5  =  5 pts (of 10)

Composite score: 83 / 100
Golden: all essential pass NO  AND composite >= 80 YES  ->  [ ] YES  [X] NO
```

---

## V-04 — Role-Aware + Quantified Gates

**Axes**: Role sequence (who acts per stage) + quantified gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Valid YAML structure | PASS | Step 5 produces YAML with all required fields; format explicit |
| C-02 | Echo stage contract | PASS | Step 5: "final stage is `echo` with `skills: []` and `auto: true`" -- exact contract text |
| C-03 | All skills valid | PASS | Full per-namespace enumeration in step 3: all 47 skills listed by name as authoritative catalog |
| C-04 | Gates non-trivial | PASS | Step 4: "Never uses vague terms: 'done', 'ready', 'complete' are not valid gates" |
| C-05 | Dependency-ordered | PASS | Actor-ordering (PM scout -> Architect draft -> Team review/prove -> Dev flow/trace -> Team listen/metrics) enforces layer dependency |
| C-06 | Meaningful groupings | PASS | "Group actor-phases into 3-6 stages" -- each actor group = coherent phase; step 6 flags empty actor groups |
| C-07 | Gates reference artifacts | PASS | Step 4 names artifact types directly: "scout-feasibility artifact", "scout-spec artifact and draft-spec artifact both present" |
| C-08 | Descriptive stage names | PASS | Actor-role labels are inherently descriptive; no generic names possible under actor-framing |
| C-09 | Strategic arc pacing | FAIL | Evidence arc implied by actor sequence but not framed as strategy; no required arc narrative |
| C-10 | Quantified gates | PASS | Explicit: "specifies a minimum count: '>=2 scout artifacts present'" required in step 4 |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [F] C-10 [P]
              Pass count: 1 / 2   -> 1 * 5  =  5 pts (of 10)

Composite score: 95 / 100
Golden: all essential pass YES  AND composite >= 80 YES  ->  [X] YES  [ ] NO
```

---

## V-05 — Inertia Contrast + Evidence Arc Strategy

**Axes**: Inertia framing (contrast against naive baseline) + evidence arc strategy

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Valid YAML structure | PASS | Step 7 explicit YAML instruction with required fields |
| C-02 | Echo stage contract | PASS | Step 6: "final stage is always `echo` with `skills: []` and `auto: true`" -- exact contract |
| C-03 | All skills valid | FAIL | "Do not invent skills not in the catalog" but no catalog enumeration; hallucination risk persists |
| C-04 | Gates non-trivial | PASS | "'done' or 'ready' is not an argument -- it is a placeholder; replace it" -- explicit rejection |
| C-05 | Dependency-ordered | PASS | Explicit rule: "scout before draft, draft before review/prove, review/prove before listen and metrics" |
| C-06 | Meaningful groupings | PASS | "3-6 stages, each with a name that communicates the arc phase intent" -- not generic, not skill names |
| C-07 | Gates reference artifacts | PASS | "Reference artifact types by name" appears twice; gates framed as arguments requiring artifact evidence |
| C-08 | Descriptive stage names | PASS | Examples: landscape, architecture, validation, evidence, synthesis -- explicitly not generic |
| C-09 | Strategic arc pacing | PASS | Inertia framing forces arc justification; step 8 requires post-YAML strategy statement |
| C-10 | Quantified gates | PASS | Explicit: "at least one gate must specify a quantified threshold (e.g., >=3 scout signals present and draft-spec artifact produced)" |

```
Essential:    C-01 [P] C-02 [P] C-03 [F] C-04 [P] C-05 [P]
              Pass count: 4 / 5   -> 4 * 12 = 48 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P]
              Pass count: 2 / 2   -> 2 * 5  = 10 pts (of 10)

Composite score: 88 / 100
Golden: all essential pass NO  AND composite >= 80 YES  ->  [ ] YES  [X] NO
```

---

## Rankings

| Rank | Variation | Score | Golden | C-03 note |
|------|-----------|-------|--------|-----------|
| 1 | V-04 Role-Aware + Quantified Gates | **95** | **YES** | skill list enumerated in body |
| 2 | V-05 Inertia Contrast + Arc Strategy | 88 | NO | catalog referenced, not listed |
| 3 | V-03 Phase-First | 83 | NO | catalog referenced, not listed |
| 4 | V-02 Conversational/Imperative | 78 | NO | catalog referenced, not listed |
| 5 | V-01 Schema-First (truncated) | 34 | NO | catalog not visible |

**The C-03 blocker**: V-03, V-04, and V-05 all score >=80 composite and pass all other
criteria. Only V-04 clears C-03 by embedding the full skill name catalog inline. This is the
structural differentiator between golden and non-golden at this score tier.

---

## Excellence Signals (from V-04)

1. **Enumerate valid skills by namespace inline** -- embedding the complete 47-skill list in
   the instruction removes ambiguity and anchors the model against hallucination (C-03 pass).
   All other variations reference "the catalog" without listing it, leaving a gap.

2. **Actor-role framing before gate writing** -- "who acts in this stage?" before "what must
   exist to advance?" grounds transitions in concrete workflow logic. Actor boundaries produce
   natural, artifact-grounded gate conditions without requiring the model to invent them.

3. **Quantified gate example embedded in the requirement** -- not just "write quantified gates"
   but showing the exact syntax (`>=2 scout artifacts present`) in the instruction increases
   the probability the model produces machine-checkable gate text (C-10 pass).

---

## Observations for Next Round

- **C-03 is the gating deficiency** across V-02, V-03, V-05. The fix is simple: add the
  47-skill catalog enumeration to any variation that wants to score golden.
- **C-09 is V-04's remaining gap**: actor-ordering implies breadth->depth->synthesis but does
  not require the model to name or argue the arc strategy. A two-sentence arc framing (as in
  V-03 or V-05) would push V-04 to 100.
- **V-05's inertia framing** produces the highest aspirational score (2/2) and the most
  argued gates -- but the C-03 miss keeps it from golden. Inertia framing + catalog
  enumeration would be the most powerful combined variation for R2.
- **V-01 truncation**: the prompt body was not captured in the variations file. Full V-01
  text should be recovered before R2 comparison.
