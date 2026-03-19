# discover-competitors-alt — Round 9 Scorecard

## Rubric Version: v9 (C-26 added, 18 aspirational criteria)

---

## Criterion Reference Map

| Tier | IDs | Weight |
|------|-----|--------|
| Essential | C-01–C-05 | 12 pts each |
| Recommended | C-06–C-08 | 10 pts each |
| Aspirational | C-09–C-26 | 0.556 pts each |

---

## V-01 — REQUIRED OUTPUTS blocks replace completion conditions

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | GATE-2 explicitly places `## C0` before any competitor row; structural ordering enforced |
| C-02 | PASS | Competitive map template requires ≥3 named external competitors with HIGH/MEDIUM/LOW |
| C-03 | PASS | "row 0 = C0" declared in GATE-2 required outputs |
| C-04 | WHITESPACE finding with its own labeled block in GATE-3 required outputs | PASS |
| C-05 | PASS | GATE-1 reads repo context; no user prompting required |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "mechanism must tie to a real C0 behavior or feature" in GATE-2; generic inertia fails by spec |
| C-07 | PASS | "min 1 inline WebSearch citation" in GATE-2 required outputs |
| C-08 | PASS | GATE-4 requires ≥3 AMEND rows; each entry pairs input change with named output effect |

**Recommended: 3/3 → 30 pts**

### Aspirational (max 10 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | GATE-3: "If FOCUS ACTIVE: gap must require both competitive map and focus lens; show intersection" |
| C-10 | PASS | GATE-3 required outputs: "each references a named competitor row by table label" |
| C-11 | PASS | TOKEN appears in GATE-3 findings (`vs [TOKEN]:`) and GATE-4 every stability verdict |
| C-12 | PASS | GATE-4 stability verdict cells address TOKEN stability; C-08 passes |
| C-13 | PASS | GATE-0 declares `TOKEN: [domain-adaptive identifier]` as a copyable token |
| C-14 | PASS | "every Stability verdict cell names TOKEN" — GATE-4 required outputs, no per-entry exceptions |
| C-15 | PASS | GATE-0 is unconditional first gate; TOKEN declared before GATE-2 prose by design |
| C-16 | PASS | GATE-4: "every Evidence cell contains reasoning distinct from verdict — 'Stable.' alone fails" |
| C-17 | PASS | "must include at least one DOMAIN-TERMS term" in TOKEN construction rule |
| C-18 | PASS | GATE-0 required outputs: DOMAIN-TERMS on its own closed line before TOKEN |
| C-19 | PASS | GATE-0 is unconditional, no focus detection precedes it; TOKEN is the second line of output |
| C-20 | PASS | GATE-4 enumerates all four: "Input change, Output effect, Stability verdict, Evidence" by name |
| C-21 | PASS | GATE-0 header: `[UNCONDITIONAL — GATE-1 is the first conditional operation]` — both conditions met |
| C-22 | PASS | All four AMEND component names are domain-neutral; no product-specific renaming |
| C-23 | PASS | Manifest table enumerates all 5 gates with execution-mode labels before any gate runs |
| C-24 | PASS | Manifest uses pipe-and-hyphen table outside code fence |
| C-25 | PASS | Completion conditions removed; REQUIRED OUTPUTS blocks are sole output spec; TOKEN appears in each gate's block |
| C-26 | PASS | Each gate carries `**Required outputs:**` as a labeled block; TOKEN appears by declared value within each block; no gate defers TOKEN to completion condition only (they're absent) |

**Aspirational: 18/18 → 10 pts**

**V-01 Composite: 60 + 30 + 10 = 100**

---

## V-02 — REQUIRED OUTPUTS as native markdown tables

### Essential: 5/5 → 60 pts *(same structural guarantees as V-01)*

### Recommended: 3/3 → 30 pts *(same)*

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-24 | PASS | Same as V-01; table format doesn't remove any criterion evidence |
| C-25 | PASS | REQUIRED OUTPUTS table has explicit `TOKEN required?` column = Yes; token named by value in each gate's table |
| C-26 | PASS | Table format is the strongest form of "structurally separable artifact" — `**Required outputs:**` table is extractable by heading; TOKEN appears in `TOKEN required?` column within the block. Table format adds explicit column for token requirement, improving clarity over numbered list |

**Note on completion condition retention in GATE-0:** V-02 retains "Completion condition:" at GATE-0's end alongside the REQUIRED OUTPUTS table. C-26 is satisfied by the presence of the dedicated block — the completion condition adds redundancy but doesn't disqualify the block.

**Aspirational: 18/18 → 10 pts**

**V-02 Composite: 60 + 30 + 10 = 100**

---

## V-03 — REQUIRED OUTPUTS blocks trailing (after body prose)

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-24 | PASS | Same structural properties; position within gate body doesn't affect these criteria |
| C-25 | PASS | REQUIRED OUTPUTS blocks still exist in each gate; TOKEN appears within them |
| C-26 | **FAIL** | C-26 requires the block be "extractable without reading the gate's instructional prose." Trailing placement structurally couples the block to preceding body prose: (1) the gate's body prose naturally defines the execution context that the block's required-output items assume; (2) a reader extracting the trailing block in isolation encounters items like "TOKEN appears by declared value in: C0 section label, `vs [TOKEN]` column header" — these references derive meaning from the body prose preceding them. A leading block can be read as a standalone contract before any prose context is ingested; a trailing block cannot. The operative failure: the block is structurally positioned as a summary artifact, not a contract artifact, making it extractable only after reading the body. |

**Aspirational: 17/18 → 17 × 0.556 = 9.444 pts**

**V-03 Composite: 60 + 30 + 9.444 = 99.444**

---

## V-04 — Lean gate bodies; REQUIRED OUTPUTS dominant

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Cross-dimensional whitespace still required by GATE-3 REQUIRED OUTPUTS when FOCUS ACTIVE |
| C-10 | PASS | REQUIRED OUTPUTS block still mandates findings reference named competitor rows |
| C-11–C-24 | PASS | Lean body prose reduces instructional text but doesn't remove criterion-satisfying content from REQUIRED OUTPUTS blocks |
| C-25 | PASS | Minimal body prose means REQUIRED OUTPUTS blocks bear maximum weight as output spec; TOKEN named in each |
| C-26 | PASS | Lean design maximizes structural dominance of blocks — with one-sentence body prose, REQUIRED OUTPUTS is clearly the gate's primary content; extraction without reading prose is trivially satisfied when prose is a single sentence |

**Note:** V-04's lean-body design is the most favorable form for C-26 extractability. Reduced prose eliminates the semantic dependency concern that causes V-03's failure — there is no body context to depend on.

**Aspirational: 18/18 → 10 pts**

**V-04 Composite: 60 + 30 + 10 = 100**

---

## V-05 — Table blocks + manifest column + completion conditions retained

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-24 | PASS | Combined design preserves all prior criterion evidence |
| C-25 | PASS | Triple-source declaration (REQUIRED OUTPUTS table + manifest "Required outputs" column + completion conditions) makes TOKEN's required-output status verifiable from three independent locations |
| C-26 | PASS | REQUIRED OUTPUTS tables are present and labeled per gate; TOKEN appears in each block. Retaining completion conditions does not disqualify the blocks — C-26 is satisfied by the *presence* of dedicated blocks, not by the *absence* of other output specifications. No conflicting specification risk: completion conditions and blocks declare the same TOKEN requirement; redundancy is robustness, not conflict |

**Aspirational: 18/18 → 10 pts**

**V-05 Composite: 60 + 30 + 10 = 100**

---

## Composite Scores & Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 (tie) | V-01 | 60 | 30 | 10.000 (18/18) | **100** | Yes |
| 1 (tie) | V-02 | 60 | 30 | 10.000 (18/18) | **100** | Yes |
| 1 (tie) | V-04 | 60 | 30 | 10.000 (18/18) | **100** | Yes |
| 1 (tie) | V-05 | 60 | 30 | 10.000 (18/18) | **100** | Yes |
| 5 | V-03 | 60 | 30 | 9.444 (17/18) | **99.444** | Yes* |

*V-03 exceeds the 80 composite and passes all 5 essential — technically golden by threshold, but the structural defect in C-26 represents a real design flaw.

---

## C-26 Decisive Question Resolution

**Does trailing REQUIRED OUTPUTS position fail C-26?**

**Answer: Yes, trailing position fails C-26.**

The criterion's operative test is "extractable without reading the gate's instructional prose." Leading blocks serve as forward contracts — a reader encounters the block first, understands the required outputs, then reads the body as implementation detail. Trailing blocks serve as summaries — the body prose establishes the execution context, and the block retrospectively enumerates what the prose has already described. A reader extracting a trailing block encounters items that implicitly reference the body above them (e.g., "TOKEN appears in the C0 section label, `vs [TOKEN]` column header" — these locations are defined in the body prose). The block is not structurally prior to the prose; it structurally depends on it.

**Position matters for C-26. Leading or standalone placement is required.**

---

## Excellence Signals from Top-Scoring Variations

**V-01** establishes the cleanest C-25/C-26 form: removing completion conditions eliminates the ambiguity about which artifact constitutes the "output specification." With REQUIRED OUTPUTS blocks as the sole spec, C-25 and C-26 are satisfied at maximum clarity — there is no competing output-spec artifact.

**V-02** demonstrates that table format provides an explicit structural affordance for C-26: a `TOKEN required?` column makes the block's TOKEN-requirement contract machine-readable. This is the highest-fidelity form of "dedicated, explicitly labeled REQUIRED OUTPUTS block."

**V-04** demonstrates that lean body prose inverts the prose-to-block ratio, making REQUIRED OUTPUTS the gate's dominant content. This eliminates the structural dependency concern at its root: with minimal body prose, there is no prose context for the block to depend on.

**V-05** demonstrates that triple-source TOKEN declaration (block + manifest column + completion condition) adds structural resilience without scoring cost. Redundancy is robustness when all sources declare the same required element.

**Shared pattern across all 100-point variations:** REQUIRED OUTPUTS blocks function as first-class structural contracts, not appendices or summaries. Leading placement (V-01, V-02), minimal surrounding prose (V-04), and multi-source corroboration (V-05) all reinforce this contract-first architecture.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Leading REQUIRED OUTPUTS blocks function as forward contracts — position before body prose is structurally required for C-26 extractability; trailing placement fails even when blocks are present and labeled", "Removing completion conditions (V-01) eliminates output-spec ambiguity and makes REQUIRED OUTPUTS blocks unambiguously the sole output contract for C-25 and C-26", "Table format for REQUIRED OUTPUTS blocks adds explicit TOKEN-required column, making the contract machine-readable and maximally extractable", "Lean gate bodies (V-04) eliminate prose-dependency risk for C-26 by minimizing the context a trailing reader would need to supply from body prose"]}
```
