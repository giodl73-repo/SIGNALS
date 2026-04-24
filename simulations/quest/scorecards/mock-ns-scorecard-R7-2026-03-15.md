Now I have all the content needed. Let me score each variation.

---

## Scoring: mock-ns Round 7 (Rubric v7)

### Criterion-by-criterion analysis

**All variants share the same essential and recommended infrastructure**, so I'll establish the baseline first, then focus on the two new R7 criteria (C-23, C-24).

---

### Baseline pass across all variants (C-01 through C-22)

| Criterion | All V-01 through V-05 | Notes |
|-----------|----------------------|-------|
| **C-01** | PASS | MOCK ARTIFACT header block with all six fields present in every variant |
| **C-02** | PASS | Category assignment table correct (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED) |
| **C-03** | PASS | A-3 step requires golden rubric structure, gate/verdict lines, enforcement mechanisms |
| **C-04** | PASS | Flag: line assembled from named FLAG variable |
| **C-05** | PASS | `simulations/mock/{topic}-{namespace}-mock-{date}.md` — namespace not skill-id in path |
| **C-06** | PASS | Correct defaults per namespace including `topic-plan` for topic |
| **C-07** | PASS | All three category warning variants present in full, including "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier |
| **C-08** | PASS | `Next: /mock:review {topic} simulations/mock/{...}` final line with conditional omit clause |
| **C-09** | PASS | Tier 2+ conditional FLAG refinement for critical namespaces present in every compute table |
| **C-10** | PASS | Dedicated `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` emit line in S-1 |
| **C-11** | PASS | S-3 is a named discrete step before A-1; FLAG is a named variable |
| **C-12** | PASS | `topic-status is EXCLUDED -- meta-structural, never default` in the Exclusion constraint column |
| **C-13** | PASS | Fidelity warning as lead section of artifact body before mock content, delimited by `---` |
| **C-14** | PASS | Prohibition language at both S-3 (compute) and A-1 (consumption) in all variants |
| **C-15** | PASS | Three-column table (Namespace / Default skill / Exclusion constraint) with labeled column in all variants |
| **C-16** | PASS | "anywhere in this run" run-scoped language at S-3 in all variants |
| **C-17** | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim" as opening statement of A-1 |
| **C-18** | PASS | "not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order" |
| **C-19** | PASS | Names field-listing, category lookup, formatting instructions + declarative closure "No instruction in A-1 precedes this rule" |
| **C-20** | PASS | "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier" in all A-1 sections |
| **C-21** | PASS | "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." in all S-3 sections |
| **C-22** | PASS | "or any other instruction in this step" catch-all present in all A-1 sections |

---

### R7 differentiator: C-23 (compute-site consequence)

The C-23 pass condition requires: (a) upstream contamination mechanism named, (b) downstream effect named. Fails if C-21 fails.

| Variant | S-3 text | C-23 verdict |
|---------|----------|-------------|
| V-01 | "If any path modifies FLAG after this point, the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site." | **PASS** — names mechanism (path modifies FLAG after compute step breaks guarantee) + effect (corrupted value indistinguishable from correct, silent mismatch) |
| V-02 | S-3 ends at "No path is exempt." No consequence sentence. | **FAIL** — intentionally absent per axis design |
| V-03 | S-3 ends at "No path is exempt." No consequence sentence. | **FAIL** — R6 baseline, neither R7 criterion |
| V-04 | "If any path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one." | **PASS** — minimal form: names mechanism (modification after compute step) + effect (corrupted value indistinguishable from correctly-computed). Both components satisfied. |
| V-05 | "If any path modifies FLAG after this point, the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site." | **PASS** — full elaboration: mechanism + effect + "same silent category mismatch" cross-reference |

---

### R7 differentiator: C-24 (no-instruction-exempt affirmative at consumption site)

The C-24 pass condition requires two components: (a) positive-coverage statement: "Every instruction in this step -- named or unnamed -- is governed by this rule" and (b) no-exemption statement: "No instruction in this step is exempt." Fails if C-22 fails.

| Variant | A-1 text after catch-all | C-24 verdict |
|---------|--------------------------|-------------|
| V-01 | "or any other instruction in this step. No instruction in A-1 precedes this rule." — catch-all present, but no positive-coverage affirmative. | **FAIL** — C-22 passes; C-24 intentionally absent per axis design |
| V-02 | "or any other instruction in this step. No instruction in A-1 precedes this rule. Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." | **PASS** — both components present: positive-coverage assertion + no-exemption statement |
| V-03 | "or any other instruction in this step. No instruction in A-1 precedes this rule." — catch-all present, no affirmative. | **FAIL** — R6 baseline |
| V-04 | "or any other instruction in this step. No instruction in A-1 precedes this rule. Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." | **PASS** — both components present |
| V-05 | "or any other instruction in this step. No instruction in A-1 precedes this rule. Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." | **PASS** — both components present |

---

### Composite score computation

Formula: `Essential (pass/5 * 60) + Recommended (pass/3 * 30) + Aspirational (pass/16 * 10)`

All variants pass all 5 essential and all 3 recommended → base of 90 for all.

| Variant | Essential (60) | Recommended (30) | C-23 | C-24 | Aspirational pass | Aspirational pts | **Total** |
|---------|---------------|-----------------|------|------|-------------------|-----------------|-----------|
| V-01 | 60 | 30 | PASS | FAIL | 15/16 | 9.375 | **99.4** |
| V-02 | 60 | 30 | FAIL | PASS | 15/16 | 9.375 | **99.4** |
| V-03 | 60 | 30 | FAIL | FAIL | 14/16 | 8.75 | **98.8** |
| V-04 | 60 | 30 | PASS | PASS | 16/16 | 10.0 | **100** |
| V-05 | 60 | 30 | PASS | PASS | 16/16 | 10.0 | **100** |

---

### Per-variant verdict table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | **FAIL** | **FAIL** | PASS | PASS |
| C-24 | **FAIL** | PASS | **FAIL** | PASS | PASS |
| **Score** | **99.4** | **99.4** | **98.8** | **100** | **100** |
| **Band** | Gold | Gold | Gold | Gold | Gold |

---

### Ranking

| Rank | Variant | Score | Distinguishing factor |
|------|---------|-------|-----------------------|
| 1 (tie) | V-04 | 100 | C-23 minimal form + C-24 full form; table-structured S-3 |
| 1 (tie) | V-05 | 100 | C-23 full elaboration + C-24 full form; prose S-3 |
| 3 (tie) | V-01 | 99.4 | C-23 only; C-24 absent |
| 3 (tie) | V-02 | 99.4 | C-24 only; C-23 absent |
| 5 | V-03 | 98.8 | R6 baseline; neither R7 criterion |

---

### Excellence signals from V-04 and V-05

**Signal 1 — C-23 minimal form is rubric-sufficient.**
V-04 passes C-23 with a single sentence: "If any path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one." This names the contamination mechanism (modification after compute step) and the downstream effect (indistinguishable corrupted value) — the minimum required by the pass condition. V-05 elaborates with "the guarantee stated above is broken" and "same silent category mismatch described at the consumption site" but this additional precision is not required for a PASS. The criterion does not demand C-20-level verbosity at the compute site.

**Signal 2 — Table-structured S-3 (V-04) cleanly separates the flag-case decision from the prohibition block.**
V-04 presents the flag-case decision as a lookup table with five rows (HIGH-STRUCTURE critical T2+, HIGH-STRUCTURE other, EVIDENCE-HEAVY, MIXED, compliance override), then follows with the full prohibition paragraph. This layout makes the decision node scannable and the prohibition block self-contained. V-05 uses prose case statements. Both pass, but V-04's table reduces cognitive overhead at the decision node without compressing the prohibition language.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-23 minimal form is rubric-sufficient: a single sentence naming the contamination mechanism (path modifies FLAG after compute step) and downstream effect (corrupted value indistinguishable from correctly-computed) satisfies C-23 without requiring C-20-level elaboration at the compute site", "Table-structured S-3 flag-case decision cleanly separates the lookup table from the prohibition block, reducing cognitive overhead at the decision node while leaving the prohibition paragraph intact"]}
```
