## Round 6 Scoring — mock-ns (Rubric v6)

---

### V-01 — Consumption-Side Catch-All

**Criterion-by-criterion:**

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | MOCK ARTIFACT header complete | PASS | All six fields present in correct order at header assembly |
| C-02 | Category assignment correct | PASS | CATEGORY lookup table covers all 27 skills correctly |
| C-03 | Mock body follows golden skill structure | PASS | A-3 explicitly requires golden rubric structure: sections, tables, gates, enforcement |
| C-04 | Automatic flag matches category | PASS | FLAG computed from CATEGORY in S-3, copied verbatim at A-1 |
| C-05 | Path convention correct | PASS | `simulations/mock/{topic}-{namespace}-mock-{date}.md` — no skill-id in path |
| C-06 | Representative skill default correct | PASS | Three-column table with correct defaults including `topic-plan` |
| C-07 | Fidelity warning complete | PASS | All three category variants fully specified; HIGH-STRUCTURE includes "REAL-REQUIRED at Tier 2+" qualifier |
| C-08 | Next-step invocation line | PASS | A-5 emits `Next: /mock:review {topic} {path}` |
| C-09 | Tier-conditional flag for critical namespaces | PASS | Case 1 distinguishes HIGH-STRUCTURE + critical + tier≥2 |
| C-10 | Dedicated TOPICS.md emit line | PASS | S-1 emits `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` as own line |
| C-11 | FLAG computed before header assembly | PASS | S-3 precedes A-1; FLAG is a named variable |
| C-12 | topic-status exclusion inline | PASS | Table row: `topic-status is EXCLUDED — meta-structural, never default` |
| C-13 | Fidelity warning in lead position | PASS | A-2 precedes A-3; delimited by `---` |
| C-14 | Prohibition at both sites | PASS | S-3: "FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run." A-1: "copy FLAG from S-3 verbatim. Do not rederive it." |
| C-15 | Structural exclusion column in default table | PASS | Three-column table with labeled "Exclusion constraint" column |
| C-16 | Run-scoped prohibition at compute site | PASS | "anywhere in this run … including paths that do not pass through prior steps in normal order" |
| C-17 | FLAG prohibition is first rule at A-1 | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim." opens A-1 |
| C-18 | Named execution path classes at compute site | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context" |
| C-19 | Anti-displacement closure at consumption site | PASS | Names field-listing, category lookup, formatting instructions + "No instruction in A-1 precedes this rule." |
| C-20 | Failure-consequence statement | PASS | "re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier" |
| C-21 | No-exemption affirmative closure at compute site | **FAIL** | S-3 has run-scoped prohibition and catch-all path clause but lacks both components of C-21: no "Every execution path that reaches A-1 carries the FLAG value emitted here" and no "No path is exempt." |
| C-22 | Catch-all instruction clause at consumption site | PASS | A-1: "before any field is listed, before any category lookup, before any formatting instruction, **or any other instruction in this step**" |

**Aspirational pass: 13/14**

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/14 × 10)
          = 60 + 30 + 9.29
          = 99.3
```

---

### V-02 — Compute-Site Affirmative Closure

**Criterion-by-criterion:**

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS × 8 | Same structure as V-01; all fields, table, path, warning, next-step present |
| C-09 | Tier-conditional flag | PASS | Case 1 present |
| C-10 | TOPICS.md dedicated emit | PASS | S-1 dedicated line |
| C-11 | FLAG computed before header | PASS | S-3 precedes A-1 |
| C-12 | topic-status exclusion inline | PASS | Three-column table; exclusion column populated |
| C-13 | Fidelity warning lead position | PASS | A-2 before A-3, delimited |
| C-14 | Prohibition at both sites | PASS | S-3 and A-1 both carry prohibition language |
| C-15 | Structural exclusion column | PASS | Three-column table with "Exclusion constraint" column |
| C-16 | Run-scoped prohibition | PASS | "including paths that do not pass through prior steps in normal order" |
| C-17 | FLAG prohibition first at A-1 | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim." |
| C-18 | Named path classes | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context" |
| C-19 | Anti-displacement closure | PASS | Three canonical types + "No instruction in A-1 precedes this rule." |
| C-20 | Failure-consequence statement | PASS | Inertia risk statement with mechanism + downstream impact |
| C-21 | No-exemption affirmative closure | PASS | S-3: "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." — both components present |
| C-22 | Catch-all instruction clause | **FAIL** | A-1 names field-listing, category lookup, formatting — stops there. No "or any other instruction in this step." C-19 passes but C-22 fails. |

**Aspirational pass: 13/14**

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/14 × 10)
          = 60 + 30 + 9.29
          = 99.3
```

---

### V-03 — R5 High-Water Baseline (Lifecycle Emphasis)

**Criterion-by-criterion:**

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS × 8 | All present; HIGH-STRUCTURE warning includes "REAL-REQUIRED at Tier 2+" qualifier |
| C-09 | Tier-conditional flag | PASS | S-3 Case 1 distinguishes critical + tier≥2 |
| C-10 | TOPICS.md dedicated emit | PASS | S-1 dedicated emit line |
| C-11 | FLAG computed before header | PASS | S-3 (in COMPUTE PHASE) precedes A-1 (in ASSEMBLY PHASE) |
| C-12 | topic-status exclusion inline | PASS | Prose note: "(topic-status is excluded as meta-structural; never use it as the mock-ns default...)" |
| C-13 | Fidelity warning lead position | PASS | A-2 positioned before A-3 body |
| C-14 | Prohibition at both sites | PASS | S-3: "Do not modify FLAG after this step." A-1: "RULE 1 — Do not compute a new FLAG value here." |
| C-15 | Structural exclusion column | **FAIL** | V-03 uses a list format (`namespace -> default`) with prose parenthetical note. No three-column table with a dedicated Exclusion column. C-12 passes; C-15 fails. |
| C-16 | Run-scoped prohibition | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order" |
| C-17 | FLAG prohibition first at A-1 | PASS | "RULE 1 — Do not compute a new FLAG value here." opens A-1 |
| C-18 | Named path classes | PASS | Same enumeration as V-01/V-02 |
| C-19 | Anti-displacement closure | PASS | Three canonical types + "No instruction in A-1 precedes this rule." |
| C-20 | Failure-consequence statement | PASS | "The failure cannot be caught by automated review because the header category and flag fields are not cross-checked by any downstream process..." — mechanism and invisibility both named |
| C-21 | No-exemption affirmative closure | **FAIL** | S-3 has run-scoped prohibition with path-class enumeration but no positive-obligation statement and no "No path is exempt." |
| C-22 | Catch-all instruction clause | **FAIL** | A-1: "before any field is listed, before any category lookup, before any formatting instruction in this step." — no "or any other instruction" clause. |

**Aspirational pass: 11/14** (fails C-15, C-21, C-22)

> **Note:** Predicted 12/14 in the variate document; actual is 11/14. The lifecycle-emphasis axis foregoes the three-column table structure in favor of an annotated list — C-15 deduction is real, not predicted.

```
Composite = (5/5 × 60) + (3/3 × 30) + (11/14 × 10)
          = 60 + 30 + 7.86
          = 97.9
```

---

### V-04 — Table-Structured Both (C-21 + C-22, Role Sequence + Output Format)

**Criterion-by-criterion:**

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS × 8 | Table-format inputs, dedicated TOPICS.md emit, three-category warning table (includes "REAL-REQUIRED at Tier 2+" row), next-step line present |
| C-09 | Tier-conditional flag | PASS | S-3 table: critical + tier≥2 row for HIGH-STRUCTURE |
| C-10 | TOPICS.md dedicated emit | PASS | S-1 dedicated emit line |
| C-11 | FLAG computed before header | PASS | S-3 compute table before A-1 header assembly |
| C-12 | topic-status exclusion inline | PASS | "Do NOT use topic-status (meta-structural, excl.)" in table |
| C-13 | Fidelity warning lead position | PASS | A-2: "Write as the lead section of the artifact body (before mock content, after ---)" |
| C-14 | Prohibition at both sites | PASS | S-3 prohibition line + A-1 first rule |
| C-15 | Structural exclusion column | PASS | Three-column table `Namespace | Default | Exclusion constraint` with dedicated column |
| C-16 | Run-scoped prohibition | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that bypass normal step order" |
| C-17 | FLAG prohibition first at A-1 | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim." opens A-1 |
| C-18 | Named path classes | PASS | Same path-class enumeration as prior variations |
| C-19 | Anti-displacement closure | PASS | Anti-displacement table names three canonical types + "No instruction in A-1 precedes this rule." |
| C-20 | Failure-consequence statement | PASS | "re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier." |
| C-21 | No-exemption affirmative closure | PASS | Visually isolated section: "Affirmative closure: Every execution path that reaches A-1 carries the FLAG value computed in this step. No path is exempt." — both components, standalone lines |
| C-22 | Catch-all instruction clause | PASS | Anti-displacement table row: `Any other instruction in A-1 | NO` — structurally enforced, not a prose tail clause |

**Aspirational pass: 14/14**

```
Composite = (5/5 × 60) + (3/3 × 30) + (14/14 × 10)
          = 60 + 30 + 10
          = 100
```

---

### V-05 — Full R6 Convergence

**Criterion-by-criterion:**

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS × 8 | All fields present; full fidelity warning text with "REAL-REQUIRED at Tier 2+" qualifier; next-step line |
| C-09 | Tier-conditional flag | PASS | Case 1 in S-3 |
| C-10 | TOPICS.md dedicated emit | PASS | S-1 dedicated emit |
| C-11 | FLAG computed before header | PASS | S-3 precedes A-1 |
| C-12 | topic-status exclusion inline | PASS | "topic-status is EXCLUDED — meta-structural, never default" in table column |
| C-13 | Fidelity warning lead position | PASS | A-2 before A-3 |
| C-14 | Prohibition at both sites | PASS | S-3: "FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run." A-1: "The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it." |
| C-15 | Structural exclusion column | PASS | Three-column table with "Exclusion constraint" column |
| C-16 | Run-scoped prohibition | PASS | "anywhere in this run … including paths that do not pass through prior steps in normal order" |
| C-17 | FLAG prohibition first at A-1 | PASS | "The first rule of this step is:" opens A-1 |
| C-18 | Named path classes | PASS | Full enumeration: step, conditional branch, fallback path, regeneration sequence, any other execution context |
| C-19 | Anti-displacement closure | PASS | Three types + "No instruction in A-1 precedes this rule." |
| C-20 | Failure-consequence statement | PASS | Full consequence chain: category mismatch → invisible to downstream tooling → corrupts trust tier → undetectable without manual inspection |
| C-21 | No-exemption affirmative closure | PASS | S-3: "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." — inline with prohibition, both components |
| C-22 | Catch-all instruction clause | PASS | A-1: "before any field is listed, before any category lookup, before any formatting instruction, **or any other instruction in this step**. No instruction in A-1 precedes this rule." |

**Aspirational pass: 14/14**

```
Composite = (5/5 × 60) + (3/3 × 30) + (14/14 × 10)
          = 60 + 30 + 10
          = 100
```

---

### Rankings

| Rank | Variation | Composite | Missing |
|------|-----------|-----------|---------|
| 1 | V-04 (table-structured both) | **100** | none |
| 1 | V-05 (full convergence prose) | **100** | none |
| 3 | V-01 (C-22 only) | 99.3 | C-21 |
| 3 | V-02 (C-21 only) | 99.3 | C-22 |
| 5 | V-03 (R5 baseline lifecycle) | 97.9 | C-15, C-21, C-22 |

All five variations pass all essential criteria. All five are Gold band (all essential pass + composite ≥ 80).

---

### V-03 Deduction Note

The predicted score for V-03 was 98.6 (12/14 aspirational). Actual is 97.9 (11/14). The lifecycle-emphasis axis chose a list format for namespace defaults rather than the three-column table used in V-01, V-02, V-04, and V-05. This loses C-15 (structural exclusion column), a criterion the R5 baseline had passed. The lifecycle framing (explicit `== COMPUTE PHASE ==` / `== ASSEMBLY PHASE ==` boundaries) is an improvement in phase clarity but does not offset the C-15 regression. The hypothesis that R5 C-01 through C-20 is "already sufficient" understates the C-15 cost of switching to list format.

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — C-21: Affirmative exhaustiveness as a positive fact (V-02, V-04, V-05)**
The highest-leverage innovation in v6. An enumeration of path classes — even with a catch-all — can be read as illustrative ("here are the main paths I thought of"). The affirmative closure converts this: "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." This is not a prohibition; it is a statement of fact about the system's invariant. An executor cannot interpret it as a suggestion.

**Signal 2 — C-22: Anti-displacement catch-all as exhaustive construction (V-01, V-04, V-05)**
Adding "or any other instruction in this step" after the three canonical types makes the anti-displacement coverage exhaustive by construction. Without it, a future or unrecognized instruction type (e.g., a compliance annotation or a templating directive not in the original design) could be processed before the FLAG prohibition without the executor recognizing the displacement risk. The catch-all forecloses this by making the coverage unconditional.

**Signal 3 — V-04 table row as structural enforcement (V-04 exclusive)**
V-04's anti-displacement table with a dedicated `Any other instruction in A-1 | NO` row is a presentation innovation that elevates C-22 beyond its prose form. A tail clause in a run-on sentence is syntactically skippable under execution pressure; a table row with a binary `NO` label in a column is structurally impossible to skip. This doesn't change the criterion's pass/fail outcome (both V-04 and V-05 pass C-22), but it reduces the probability that an executor under pressure skips the coverage on a fast read.

**Signal 4 — V-04 isolated affirmative closure (V-04 exclusive)**
V-04 separates the C-21 content as a visually distinct named assertion ("Affirmative closure: ... No path is exempt.") following the prohibition table, rather than embedding it as the last two sentences of the prohibition paragraph (V-02/V-05 style). The separation signals that the affirmative closure is not an afterthought to the prohibition — it is a standalone architectural claim. This visual structure reinforces the distinction between prohibitions (what must not happen) and invariants (what is always true).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-21 affirmative exhaustiveness: positions the no-exemption claim as a system invariant (Every path carries FLAG / No path is exempt) rather than as a tail clause of the prohibition enumeration — converts illustrative list to positive fact", "C-22 catch-all instruction clause: adds 'or any other instruction in this step' after the three canonical types, making anti-displacement coverage exhaustive by construction and immune to future instruction types not in the named list", "V-04 structural table row for C-22: elevates the catch-all instruction clause to a dedicated anti-displacement table row (Any other instruction in A-1 -- NO) making coverage structurally undeniable rather than syntactically skippable", "V-04 visually isolated affirmative closure: separates C-21 as a standalone named section after the prohibition table, signaling it is a system invariant rather than an addendum to the prohibition"]}
```
