# discover-competitors-alt — Round 7 Scoring

## Rubric Orientation

R7 adds **C-23** (15th aspirational criterion): a pre-execution gate manifest enumerating *all* gates with execution-mode labels as a standalone artifact before GATE-0 runs. C-21's inline bracket alone satisfied "pre-phase declaration" in R6; C-23 requires the full sequence in one consultable artifact. This is the sole scoring-relevant change from R6.

**C-19 / C-23 compatibility note:** C-19 prohibits "section headers, focus detection, auto-detect, conditional branching" before TOKEN. The EXECUTION PLAN manifest is a structural declaration, not an operational section doing analysis — all examples C-19 lists (focus detection, conditional branching, auto-detect) are processing operations. A manifest satisfies C-23 without violating C-19 under this reading. The rubric authors confirm V-01 predicts 100, making this the intended interpretation.

---

## Variation Scoring

### V-01 — Full gate bodies + standalone EXECUTION PLAN markdown table

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | GATE-2 opens with `## C0 — [product name]` before any competitor row. |
| C-02 | PASS | "Minimum 3 named external competitors" with HIGH/MEDIUM/LOW required in GATE-2 table. |
| C-03 | PASS | `row 0 = C0` is the explicit GATE-2 completion condition. |
| C-04 | PASS | GATE-3 requires a labeled whitespace finding with a specific uncontested dimension. |
| C-05 | PASS | GATE-1 reads repo context; "Do not ask the user for topic, competitor names, or market category." |
| C-06 | PASS | C0 template: `[TOKEN]: [mechanism type] → [Specific description tied to a real behavior or feature]`. Generic labels explicitly excluded. |
| C-07 | PASS | GATE-2: "Run a WebSearch… at least one external row: inline citation in the Source cell." |
| C-08 | PASS | GATE-4 AMEND table has Input change + Output effect columns with "which gate or section specifically shifts." |
| C-09 | PASS | GATE-3 FOCUS=ACTIVE path: "the gap must be uncontested across both the competitive dimension and the focus dimension simultaneously." |
| C-10 | PASS | Every finding: "reference at least one named competitor row by its table label." Grounding test stated explicitly. |
| C-11 | PASS | GATE-3: "TOKEN must appear by its declared value in at least one `vs [TOKEN]` line across the finding set." |
| C-12 | PASS | GATE-4 Stability verdict column: "addresses whether TOKEN is affected… required in every row." |
| C-13 | PASS | GATE-0 produces `TOKEN: [identifier]` as portable label. Role descriptions explicitly excluded. |
| C-14 | PASS | "Every row fills all four cells with a verdict." Minimum 3 rows. |
| C-15 | PASS | TOKEN declared in GATE-0 before GATE-2 C0 prose begins. Manifest precedes TOKEN but is structural, not C0 prose. |
| C-16 | PASS | Evidence column explicitly distinct from verdict: "reasoning distinct from the verdict. 'Stable.' alone fails." |
| C-17 | PASS | TOKEN "must include at least one term from the DOMAIN-TERMS line. Generic placeholder alone does not satisfy." |
| C-18 | PASS | GATE-0 template forces `DOMAIN-TERMS:` written and closed on its own line before `TOKEN:`. |
| C-19 | PASS | GATE-0 is unconditional; TOKEN is GATE-0's first output. Manifest is structural declaration, not conditional operation. |
| C-20 | PASS | GATE-4 column headers: "Input change, Output effect, Stability verdict, Evidence" — all four named. |
| C-21 | PASS | Double-declared: manifest table (`GATE-0 = UNCONDITIONAL | GATE-1 = CONDITIONAL (first)`) + bracket header `[unconditional — GATE-1 is the first conditional operation]`. |
| C-22 | PASS | Column headers are domain-neutral. Naive reader can map each to rubric-standard function without context. |
| C-23 | PASS | Markdown table under "EXECUTION PLAN" heading enumerates all 5 gates (GATE-0 through GATE-4) with UNCONDITIONAL/CONDITIONAL labels. Appears before any gate executes. Consultable without reading gate bodies. |

**Essential:** 5/5 · **Recommended:** 3/3 · **Aspirational:** 15/15
**Composite: 60 + 30 + 10 = 100**

---

### V-02 — Manifest-centric: full manifest table, compact gate bodies

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | C0 section before competitor rows required by gate structure. |
| C-02 | PASS | Competitive map gate requires 3+ named competitors with threat levels. |
| C-03 | PASS | C0 at row 0 required. |
| C-04 | PASS | Whitespace finding gate present. |
| C-05 | PASS | Repo-context inference required; no prompting. |
| C-06 | PASS | C0 inertia section requires mechanism tied to a real behavior or feature. |
| C-07 | PASS | WebSearch + inline citation required. |
| C-08 | PASS | AMEND with input-output pairs. |
| C-09 | PASS | FOCUS-ACTIVE whitespace requires cross-dimensional gap. |
| C-10 | PASS | Findings grounded to competitor rows by label. |
| C-11 | PASS | TOKEN appears in downstream findings. |
| C-12 | PASS | Stability verdict in AMEND. |
| C-13 | PASS | TOKEN portable identifier declared. |
| C-14 | PASS | Every AMEND row addresses stability. |
| C-15 | PASS | TOKEN before C0 mechanism prose. |
| C-16 | PASS | Verdict + evidence required. |
| C-17 | PASS | Domain-adaptive TOKEN with DOMAIN-TERMS term. |
| C-18 | PASS | DOMAIN-TERMS artifact committed before TOKEN. |
| C-19 | PASS | GATE-0 unconditional; TOKEN is GATE-0's first output. |
| C-20 | PASS | All four schema components named in AMEND column headers. |
| C-21 | PASS | Manifest carries both conditions: GATE-0 = UNCONDITIONAL, GATE-1 = CONDITIONAL (first). Compact gate bodies rely on manifest for this; double-declaration absent but manifest is sufficient per rubric wording. |
| C-22 | PASS | Domain-neutral column headers; no product-specific renaming. |
| C-23 | PASS | Full manifest table enumerates all gates with execution-mode labels before any gate executes. Rubric summary explicitly confirms "R6 V-02/V-05's manifest tables would have passed C-23." |

**Essential:** 5/5 · **Recommended:** 3/3 · **Aspirational:** 15/15
**Composite: 60 + 30 + 10 = 100**

---

### V-03 — Manifest as code-fence pipe-delimited block

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01–C-05 | PASS (all) | Same gate operations as V-01; all essential behaviors preserved. |
| C-06–C-08 | PASS (all) | Gate bodies identical to V-01 per axis description. |
| C-09–C-22 | PASS (all) | All aspirational criteria C-09 through C-22: same gate architecture as V-01; no structural differences affecting these criteria. |
| C-21 | PASS | Code-fence manifest still declares GATE-0 = UNCONDITIONAL, GATE-1 = first conditional. |
| C-23 | PARTIAL | Rubric requires "table or equivalent." A code-fenced pipe-aligned block is functionally tabular and renders as a table in many contexts — the "or equivalent" clause appears designed for this case. However, the criterion's operative test ("any gate's execution mode can be verified by consulting the manifest") is satisfied. Scored PARTIAL because the variation was explicitly constructed to test this boundary and the rubric authors flag it as "at risk." The "or equivalent" clause supports PASS but the deliberate uncertainty warrants the hedge. |

**Essential:** 5/5 · **Recommended:** 3/3 · **Aspirational:** 14.5/15 (C-23 = 0.5)
**Composite: 60 + 30 + (14.5/15 × 10) = 60 + 30 + 9.667 = 99.667**

---

### V-04 — Full manifest + TOKEN required by declared value in every gate output field

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01–C-05 | PASS (all) | Manifest table (V-01 format) + standard gate operations. |
| C-06–C-08 | PASS (all) | Inertia mechanism anchored; WebSearch citation required; AMEND with input-output pairs. |
| C-09–C-10 | PASS | Findings grounded to competitor rows; whitespace cross-dimensional. |
| C-11 | PASS | Maximized: TOKEN mandated in every gate output field — column headers, every finding `vs [TOKEN]` line, whitespace `[TOKEN] exposure:` label, AMEND verdict column. Propagation is structural, not incidental. |
| C-12–C-22 | PASS (all) | All aspirational criteria met; TOKEN propagation maximization does not introduce new failure modes for any structural criterion. |
| C-23 | PASS | Manifest table (V-01 format) enumerates all 5 gates with UNCONDITIONAL/CONDITIONAL labels before any gate executes. |

**Essential:** 5/5 · **Recommended:** 3/3 · **Aspirational:** 15/15
**Composite: 60 + 30 + 10 = 100**

*Note on C-11 quality:* Per-gate TOKEN mandates produce formulaic repetition risk in output quality, but C-11 only requires TOKEN to appear by name in at least one downstream finding. V-04 easily satisfies the structural requirement; whether richer or formulaic is a quality question outside the rubric's scope.

---

### V-05 — EXECUTION CONTRACT heading + bracket mode annotations + TOKEN propagation + pre-AMEND schema table

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01–C-05 | PASS (all) | Full manifest; standard gate structure. |
| C-06–C-08 | PASS (all) | Inertia mechanism; WebSearch citation; AMEND present. |
| C-09–C-19 | PASS (all) | Architecture satisfies all upstream aspirational criteria. |
| C-20 | PASS | Pre-AMEND schema declaration table explicitly enumerates all four required components with rubric-standard names before the data table. Stronger than column headers alone: a reader consulting only the schema declaration can identify all four components. |
| C-21 | PASS | Gate bracket annotations include execution-mode labels + manifest double-declares both C-21 conditions. |
| C-22 | PASS | Pre-AMEND schema uses rubric-standard names (not domain-specific renamings). Naive-reader consultability is explicit design goal per axis description. |
| C-23 | PASS | "EXECUTION CONTRACT" heading with full manifest table. Heading label is stronger standalone-artifact signal (per axis description) but the criterion tests content, not heading name. PASS either way; the heading strengthens the signal without being required. |

**Essential:** 5/5 · **Recommended:** 3/3 · **Aspirational:** 15/15
**Composite: 60 + 30 + 10 = 100**

*Note on C-20/C-22:* The pre-AMEND schema declaration table makes these criteria more robustly satisfied than column headers alone — it creates an explicit consultable schema contract before any data rows appear.

---

## Rankings

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 (tied) | V-01 | 100 | Full manifest + full gate bodies + double C-21 declaration |
| 1 (tied) | V-02 | 100 | Manifest-centric; minimal gate bodies sufficient |
| 1 (tied) | V-04 | 100 | TOKEN propagation maximized across all gate output fields |
| 1 (tied) | V-05 | 100 | Pre-AMEND schema table + EXECUTION CONTRACT + bracket annotations |
| 5 | V-03 | 99.667 | C-23 PARTIAL: code-fence pipe-aligned block at "table or equivalent" boundary |

---

## Excellence Signals

**Signal 1 — Manifest as standalone consultable contract (C-23 unlock):**
The winning pattern is an explicit `EXECUTION PLAN` or `EXECUTION CONTRACT` table — placed before GATE-0 executes — that enumerates every gate with its execution-mode label. The manifest is architecturally prior to execution; gate bodies provide operational detail but the contract is readable without them. This is structurally distinct from C-21's inline bracket, which declares the boundary of one gate, not the full execution sequence.

**Signal 2 — Double-declaration for structural redundancy (V-01, V-05):**
Declaring C-21's conditions in both the manifest table and the GATE-0 bracket header provides two independent structural signals for the same fact. The manifest satisfies C-23; the bracket reinforces C-21 without depending on the manifest being parsed. Neither alone is required, but together they eliminate interpretive ambiguity about gate-boundary semantics.

**Signal 3 — Pre-AMEND schema declaration as explicit consultability artifact (V-05):**
A dedicated schema table before the AMEND data table makes C-20/C-22 consultability structural rather than incidental. Column headers alone require reading the data table to understand the schema; a separate schema declaration creates a named contract. For naive-reader consultability (C-22), this eliminates reliance on reader inference.

**Signal 4 — Manifest + compact gate bodies are co-equal (V-02 parity):**
V-02 demonstrates that full gate bodies are not required for top scores. When the manifest carries the structural contract, gate bodies can be reduced to minimum viable instructions. The consultable contract lives in the manifest; verbosity in gate bodies adds operational clarity but zero structural scoring value.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-execution gate manifest as standalone consultable artifact enumerates all gates with execution-mode labels before GATE-0 runs", "Double-declaration of C-21 conditions across manifest table and gate bracket header provides redundant structural signals", "Pre-AMEND schema declaration table creates explicit consultability contract distinct from column headers"]}
```
