## discover-competitors-alt — Round 10 Scoring

### Scoring Framework
- **Essential** (C-01–C-05): 12 pts each, 60 pts max
- **Recommended** (C-06–C-08): 10 pts each, 30 pts max
- **Aspirational** (C-09–C-29): 0.476 pts each, 10 pts max (21 criteria)
- Formula: `(E/5×60) + (R/3×30) + (A/21×10)`

---

## Per-Criterion Analysis — All Variations

### Essential Criteria

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | All: C0 section before competitor rows in GATE-2 |
| C-02 | PASS | PASS | PASS | PASS | PASS | All: ≥3 named competitors with HIGH/MEDIUM/LOW required in GATE-2 |
| C-03 | PASS | PASS | PASS | PASS | PASS | All: C0 at row 0 in competitive map template |
| C-04 | PASS | PASS | PASS | PASS | PASS | All: WHITESPACE with specific named dimension required in GATE-3 |
| C-05 | PASS | PASS | PASS | PASS | PASS | All: "Infer domain, competitors, market from repo context — do not ask the user" |

**Essential: 5/5 all variations → 60 pts each**

### Recommended Criteria

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-06 | PASS | PASS | PASS | PASS | PASS | All: TOKEN mechanism with named type (switching cost \| habit lock-in \| workaround satisfaction) → specific C0 behavior |
| C-07 | PASS | PASS | PASS | PASS | PASS | All: "≥1 inline WebSearch citation within a competitor entry" required in GATE-2 |
| C-08 | PASS | PASS | PASS | PASS | PASS | All: AMEND schema with ≥3 entries; Input change and Output effect both named per row |

**Recommended: 3/3 all variations → 30 pts each**

### Aspirational Criteria

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Cross-dimensional whitespace required when FOCUS ACTIVE; both dimensions structurally required |
| C-10 | PASS | PASS | PASS | PASS | PASS | "each references a named competitor row by table label" — findings grounded by contract |
| C-11 | PASS | PASS | PASS | PASS | PASS | TOKEN propagates to `vs [TOKEN]:` lines, `[TOKEN] exposure:` field, competitive map column |
| C-12 | PASS | PASS | PASS | PASS | PASS | Stability verdict cell in every AMEND row; C-08 passes |
| C-13 | PASS | PASS | PASS | PASS | PASS | TOKEN declared as copyable identifier; generic placeholder alone explicitly fails |
| C-14 | PASS | PASS | PASS | PASS | PASS | Stability verdict in every AMEND data row — per-row enforcement |
| C-15 | PASS | PASS | PASS | PASS | PASS | GATE-0 declares TOKEN before GATE-2 (C0 description); temporal ordering enforced |
| C-16 | PASS | PASS | PASS | PASS | PASS | Separate Evidence column "distinct from verdict text"; "Stable." alone explicitly fails |
| C-17 | PASS | PASS | PASS | PASS | PASS | GATE-0 requires domain-adaptive token; generic placeholder alone explicitly fails |
| C-18 | PASS | PASS | PASS | PASS | PASS | DOMAIN-TERMS closed on its own line before TOKEN — separate artifact requirement explicit |
| C-19 | PASS | PASS | PASS | PASS | PASS | GATE-0 unconditional and first; no focus detection, headers, or branching before it |
| C-20 | PASS | PASS | PASS | PASS | PASS | All four components named in schema: Input change, Output effect, Stability verdict, Evidence |
| C-21 | PASS | PASS | PASS | PASS | PASS | All: GATE-0 labeled unconditional AND GATE-1 named as first conditional operation |
| C-22 | PASS | PASS | PASS | PASS | PASS | All four schema labels domain-neutral; naive reader can match each to function |
| C-23 | PASS | PASS | PASS | PASS | PASS | All 5 gates enumerated with UNCONDITIONAL/CONDITIONAL labels in manifest before GATE-0 executes |
| C-24 | PASS | PASS | PASS | PASS | PASS | Manifest is native pipe-and-hyphen table in all 5 variations |
| C-25 | PASS | PASS | PASS | PASS | PASS | TOKEN named in REQUIRED OUTPUTS block of every gate — declared as required output by value |
| C-26 | PASS | PASS | PASS | PASS | PASS | Every gate has `**REQUIRED OUTPUTS:**` heading with structured block extractable in isolation |
| C-27 | PASS | PASS | PASS | PASS | PASS | No completion conditions in any gate across all variations; REQUIRED OUTPUTS is sole spec |
| C-28 | PASS | PASS | PASS | PASS | PASS | Every gate's REQUIRED OUTPUTS block is native pipe-and-hyphen table outside code fences |
| **C-29** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** | **Decisive criterion — see analysis below** |

---

### C-29 Decisive Analysis

**C-29 test:** "explicitly declares TOKEN as required **by its committed value** — making TOKEN's required status machine-verifiable from the block alone."

**V-01 / V-03** — Column header: `TOKEN required?`

The column uses the abstract word "TOKEN," not the committed identifier (e.g., SIGNAL-LOCK). A reader consulting only the table can confirm *TOKEN* is required, but cannot confirm the specific committed identifier is required without consulting GATE-0. The Yes cells say "TOKEN by declared value" but that's row-cell content, not the column header.

C-29 says "by its committed value" — the declaration must use the committed value itself. Generic "TOKEN required?" satisfies C-28 (it's a native table with a TOKEN-marking column) but fails C-29 because the column header does not carry the committed identifier. **FAIL.**

**V-02 / V-04 / V-05** — Column header: `[TOKEN] required?` with explicit bracket-notation substitution instruction

After GATE-0 declares `TOKEN: SIGNAL-LOCK`, the model substitutes the committed value into all subsequent column headers, producing `SIGNAL-LOCK required?`. This makes the committed identifier machine-verifiable from each gate's table without reading body prose.

GATE-0's own table retains `[TOKEN] required?` literally — this is the declaration gate itself, where the commitment happens in the row ("Yes — declared value becomes the substituted column header in all subsequent gates"). This is a legitimate special case: the committed value is being established, not consumed.

C-29 passes for GATE-1 through GATE-4 (committed value in header); GATE-0 marks TOKEN as the required declaration output. **PASS.**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (A/21) | Composite |
|-----------|-----------|-------------|---------------------|-----------|
| V-01 | 60 | 30 | 20/21 = 9.524 | **99.524** |
| V-02 | 60 | 30 | 21/21 = 10.000 | **100.000** |
| V-03 | 60 | 30 | 20/21 = 9.524 | **99.524** |
| V-04 | 60 | 30 | 21/21 = 10.000 | **100.000** |
| V-05 | 60 | 30 | 21/21 = 10.000 | **100.000** |

**Ranking:** V-02 = V-04 = V-05 = **100** > V-01 = V-03 = **99.524**

---

## Excellence Signals

**Top-scoring variations: V-02, V-04, V-05**

The decisive pattern separating 100 from 99.524:

**Signal 1 — Declared-value column header via bracket-notation substitution (C-29)**
Generic `TOKEN required?` satisfies C-28 (native table) but not C-29 (by committed value). The `[TOKEN] required?` placeholder — with an explicit instruction to substitute the committed value in all post-GATE-0 gates — produces `SIGNAL-LOCK required?` at execution time. This makes the committed identifier machine-verifiable from the table column header alone, satisfying C-29's "by its committed value" requirement. Bracket substitution is the minimal mechanism that achieves this without hardcoding domain-specific values in the skill template.

**Signal 2 — 3-col REQUIRED OUTPUTS with Format column (V-04, V-05 vs V-02)**
V-04 and V-05 add `Output | Format | [TOKEN] required?` structure — the Format column specifies per-row output format (what the output looks like, not just what it is). This doesn't add new criterion passes at the current rubric level but creates a structurally richer per-gate output contract. This is an emergent quality pattern — a candidate for R11 criterion C-30 ("REQUIRED OUTPUTS table includes per-row Format column specifying expected output format").

**Signal 3 — Manifest-level TOKEN column (V-05 vs V-04)**
V-05 adds "Required outputs (TOKEN)" as a column to the EXECUTION PLAN manifest, establishing the cross-gate TOKEN contract at the architecture level. Each manifest row specifies TOKEN's required form for that gate. This dual-layer declaration (manifest contract + per-gate table detail) creates a redundant but resilient TOKEN commitment — a candidate for R11 criterion C-30/C-31 ("Manifest declares per-gate TOKEN output contract as a dedicated manifest column").

**R10 decisive learning:** The boundary between C-28 (native table) and C-29 (by committed value) is resolved. C-29 requires the actual committed identifier in the column header — generic "TOKEN required?" satisfies structural form but not semantic specificity. Bracket-notation substitution is the rubric-correct pattern.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["3-col REQUIRED OUTPUTS tables with Format column providing per-row output format specification alongside content requirement and TOKEN-required marker — structural enhancement beyond 2-col baseline; candidate for C-30", "Manifest-level Required-outputs-TOKEN column declaring the per-gate TOKEN contract at the architecture level — dual-layer declaration with per-gate tables; candidate for C-31"]}
```
