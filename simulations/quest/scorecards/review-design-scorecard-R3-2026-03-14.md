Scorecard written. Summary:

**R3 Results — `review-design`**

| Var | Score | C-13 | C-14 | Outcome |
|-----|-------|------|------|---------|
| V-01 | **98.57** | FAIL (labeled prose) | PASS | Golden |
| V-02 | **98.57** | PASS | FAIL (no F-IDs) | Golden |
| V-03 | **100** | PASS | PASS | Golden |
| V-04 | **100** | PASS | PASS | Golden |
| V-05 | **100** | PASS | PASS | Golden |

**All four design bets confirmed:**
- V-01 = V-02 = 98.57 — C-13 and C-14 are independent failure modes, 1.43 pts each
- V-01 vs V-03 delta = 1.43 — C-13 isolated precisely
- V-03 = V-04 = 100 — gate language is qualitative, not rubric-detectable
- V-04 = V-05 = 100 — F-09/BLOCK 1.5 is additive quality, not required for C-14 pass

**Three new patterns for R4:**
1. F-ID failures are precisely localizable — single F-08 addition was the only gap
2. C-13 and C-14 are orthogonal — table form and named F-IDs cannot substitute for each other
3. BLOCK 1.5 (roster commitment before finding generation) is a new enforcement tier: proactive prevention vs. reactive halt — candidate for C-15

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-13 and C-14 are orthogonal — labeled-prose-with-F-IDs and table-form-without-F-IDs each fail exactly one criterion and score identically, confirming neither mechanism substitutes for the other", "F-ID failures are precisely localizable — a single targeted addition (F-08 for unique catches) is sufficient to close the last C-14 gap without other structural changes", "roster commitment table before finding generation (BLOCK 1.5) converts reactive F-01 halt into proactive pre-condition verification — a new enforcement tier beyond named halt conditions"]}
```
ASS | `Sev` column + F-02 halt |

All PASS — unchanged from R2.

---

#### C-03 | Domain Expert Auto-Selection Justified

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Code block: `Signal detected:` / `Expert added:` / `Reason:` — all three labeled, F-03/F-07 halt on empty |
| V-02 | PASS | Domain expert table; "Every row must have all three cells populated before proceeding to BLOCK 2" |
| V-03 | PASS | Domain expert table + F-03 (Signal detected empty) + F-07 (Expert added or Reason empty) |
| V-04 | PASS | Domain expert table + F-03 + F-07 + Gate confirmation before BLOCK 2 |
| V-05 | PASS | Domain expert table + F-03 + F-07 + BLOCK 1.5 roster verification |

All PASS — unchanged from R2.

---

#### C-04 | Consensus Block Present

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "Do not omit this block — F-04 fires on omission regardless of review content" |
| V-02 | PASS | "This block is always required" |
| V-03 | PASS | F-04 halt; "Never omit this block — F-04 fires on omission" |
| V-04 | PASS | F-04 + Gate: "This block is mandatory. F-04 fires on omission regardless of review content." |
| V-05 | PASS | F-04 + explicit gate instruction |

All PASS — unchanged from R2.

---

#### C-05 | Unique Catches Surfaced

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 4 present; F-08 fires on omission; "If none: write `No unique catches.`" |
| V-02 | PASS | BLOCK 4 table present; "This block is always required"; `UNIQUE | none | —` fallback row |
| V-03 | PASS | BLOCK 4 present; F-08 halt; `UNIQUE | none | —` fallback row |
| V-04 | PASS | BLOCK 4 table + F-08 + Gate: "This block is mandatory. F-08 fires on omission even when catches are empty." |
| V-05 | PASS | BLOCK 4 table + F-08 + explicit gate instruction |

All PASS — F-08 reinforces what was already structurally present as BLOCK 4.

---

#### C-06 | Amend Pathway Described

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 5: `Re-run: [reviewer name(s)] on [section scope only]`; F-05 fires on full-review scope |
| V-02 | PASS | BLOCK 5: "Scope is per-section only — never 'full review'" |
| V-03 | PASS | F-05 halt + "An amend scoped to 'full review' fires F-05 — halt and re-scope" |
| V-04 | PASS | F-05 + Gate: "Re-run must name specific section — 'full review' fires F-05" |
| V-05 | PASS | F-05 + explicit halt instruction |

All PASS — unchanged from R2.

---

#### C-07 | Finding Traceability to Design Section

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `Section` column; "P1 rows: Section always required. P2 rows: Section required for >= 50%" |
| V-02 | PASS | `Section` column contracts: P1 always, >= 50% P2 |
| V-03 | PASS | `Section` column + same P1/50%-P2 rules |
| V-04 | PASS | `Section` column + explicit rules + Gate confirmation |
| V-05 | PASS | `Section` column + same rules |

All PASS — unchanged from R2.

---

#### C-08 | Severity Distribution Sanity

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 2.5: explicit P1/P2/P3 count; F-06 fires if inverted without rationale |
| V-02 | PASS | BLOCK 2.5 table with `Status` column; Rationale row required if inverted; "Do not proceed to BLOCK 3 until Status column is complete" |
| V-03 | PASS | BLOCK 2.5 table + F-06 halt |
| V-04 | PASS | BLOCK 2.5 table + F-06 + Gate: "Status column must be fully populated. Rationale row must be present if any Status cell reads `inverted`." |
| V-05 | PASS | BLOCK 2.5 table + F-06 + Gate instruction |

All PASS — all R3 variations carry forward the R2 fix.

---

#### C-09 | Expert Disagreement Analysis

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 3: `SPLIT:...Synthesis: [1-3 sentences on the design tension]` |
| V-02 | PASS | Table row: `SPLIT | [decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.]` |
| V-03 | PASS | BLOCK 3: `A: [pos] / B: [pos] | Synthesis: [1-3 sent.]` |
| V-04 | PASS | Table row with structured synthesis field |
| V-05 | PASS | Same table row format |

All PASS — unchanged from R2.

---

#### C-10 | Structural Column Enforcement in Finding Tables

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `| Sev | Section | Finding |` table in BLOCK 2 |
| V-02 | PASS | `| Sev | Section | Finding |` in every reviewer block; "no block may be rendered as prose bullets" |
| V-03 | PASS | `| Sev | Section | Finding |` table + F-02 |
| V-04 | PASS | `| Sev | Section | Finding |` + "no finding may appear as prose-only" |
| V-05 | PASS | Same table form |

All PASS — R2 baseline requirement.

---

#### C-11 | Three-Field Expert Trace

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Code block with three distinct labeled fields: `Signal detected:` / `Expert added:` / `Reason:` — all required, F-03/F-07 enforce non-empty |
| V-02 | PASS | Domain expert table: `Signal detected | Expert added | Reason` columns |
| V-03 | PASS | Domain expert table: three-column form + F-03/F-07 halts |
| V-04 | PASS | Domain expert table + F-03/F-07 + Gate verification |
| V-05 | PASS | Domain expert table + F-03/F-07 |

All PASS — C-11 satisfied by labeled prose (V-01) or table form (V-02–V-05). Table form is qualitatively stronger; C-13 adds the next level.

---

#### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 2.5 is a discrete named block positioned between BLOCK 2 and BLOCK 3 with explicit count format and pyramid check |
| V-02 | PASS | "This block must appear between BLOCK 2 and BLOCK 3." Status column gate. |
| V-03 | PASS | BLOCK 2.5 positioned between BLOCK 2 and BLOCK 3; F-06 enforces it |
| V-04 | PASS | BLOCK 2.5 with positioning statement + Gate: "Do not begin BLOCK 3 without completing this block" |
| V-05 | PASS | BLOCK 2.5 with F-06; positioned between BLOCK 2 and BLOCK 3 |

All PASS — all R3 variations carry BLOCK 2.5 from R2.

---

#### C-13 | Expert Trace in Table Column Form

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | Expert trace is a code block with labeled prose fields (`Signal detected: [...]` / `Expert added: [...]` / `Reason: [...]`). Three labeled fields → C-11 PASS. No table → C-13 FAIL by design. |
| V-02 | PASS | Domain expert table with `Signal detected | Expert added | Reason` columns — table column form |
| V-03 | PASS | Domain expert table: `| Signal detected | Expert added | Reason |` — table column form |
| V-04 | PASS | Domain expert table with same three columns |
| V-05 | PASS | Domain expert table with same three columns |

V-01 FAIL by design — isolates C-13 from C-14.

---

#### C-14 | Named Halt Conditions on Every Mandatory Block

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | F-01–F-08 cover all mandatory blocks: BLOCK 1 (F-03/F-07), BLOCK 2 (F-01/F-02), BLOCK 2.5 (F-06), BLOCK 3 (F-04), BLOCK 4 (F-08), BLOCK 5 (F-05) |
| V-02 | **FAIL** | No F-IDs anywhere. Column contracts say "format error" without named identifiers. Gate language uses "correct it before moving on" — not a named halt condition. C-14 FAIL by design. |
| V-03 | PASS | F-01–F-08 present; every block from BLOCK 1 through BLOCK 5 has at least one named F-ID |
| V-04 | PASS | F-01–F-08 on all blocks + explicit "Gate:" labels at each block boundary naming the F-IDs |
| V-05 | PASS | F-01–F-09; F-09 adds BLOCK 1.5 coverage — strongest coverage (9 named halt conditions) |

V-02 FAIL by design — isolates C-14 from C-13.

---

### Composite Scores

Formula: `essential_pass/4 × 60 + recommended_pass/3 × 30 + aspirational_pass/7 × 10`
PARTIAL = 0.5 for scoring.

| Var | C-01 | C-02 | C-03 | C-04 | Essential (×60) | C-05 | C-06 | C-07 | Recommended (×30) | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Aspirational (×10) | **Composite** | All Essential? | Outcome |
|-----|------|------|------|------|-----------------|------|------|------|-------------------|------|------|------|------|------|------|------|--------------------|---------------|----------------|---------|
| V-01 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | P | **F** | P | 6/7 → 8.57 | **98.57** | Yes | **Golden** |
| V-02 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | P | P | **F** | 6/7 → 8.57 | **98.57** | Yes | **Golden** |
| V-03 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | P | P | P | 7/7 → 10 | **100** | Yes | **Golden** |
| V-04 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | P | P | P | 7/7 → 10 | **100** | Yes | **Golden** |
| V-05 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | P | P | P | P | P | P | P | 7/7 → 10 | **100** | Yes | **Golden** |

`P = PASS, F = FAIL`

---

### Ranking

| Rank | Variation | Score | Outcome | Tiebreaker |
|------|-----------|-------|---------|------------|
| 1 | V-05 (lifecycle + inertia + format) | 100 | Golden | 9 F-IDs + BLOCK 1.5 roster commitment — deepest enforcement stack; prevents reviewer drift before BLOCK 2 begins |
| 2 | V-04 (format + inertia) | 100 | Golden | 8 F-IDs + expert table + explicit "Gate:" transitions at every block — full enforcement without extra lifecycle block overhead |
| 3 | V-03 (inertia, minimal fix) | 100 | Golden | Minimum viable change: single F-08 addition closes C-14 entirely — validates precise failure localization |
| 4 | V-02 (all-table, no F-IDs) | 98.57 | Golden | Table structure everywhere; C-14 FAIL confirms F-IDs are not replaceable by table structure alone |
| 4 | V-01 (F-IDs, labeled prose) | 98.57 | Golden | Complete F-ID registry; C-13 FAIL confirms table columns are not replaceable by labeled prose alone |

---

### Design Bet Resolution

| Bet | Result | Finding |
|-----|--------|---------|
| V-01 vs V-02 score identical? | **Confirmed — both 98.57** | C-13 and C-14 are independent failure modes worth exactly 1.43 pts each; missing either one produces the same composite |
| V-01 vs V-03 delta exactly 1.43? | **Confirmed — 98.57 vs 100** | C-13 is isolated: expert table vs. labeled prose is the only structural difference |
| V-03 vs V-04 both score 100? | **Confirmed — both 100** | Explicit "Gate: do not proceed" language produces no rubric score lift — qualitative enforcement depth only |
| V-04 vs V-05 both score 100? | **Confirmed — both 100** | BLOCK 1.5 and F-09 are additive quality; C-14 pass condition covers canonical structural blocks — BLOCK 1.5 is not in that list, so F-09 is surplus enforcement, not rubric-necessary |

All four design bets resolved in the predicted direction.

---

### Key Findings

**R3 rubric ceiling reached by three variations.** V-03, V-04, and V-05 all score 100. The minimum winning form is V-03: extend R2 V-05 with F-08 only. V-04 and V-05 demonstrate that additional structural investment (gate language, coverage block) is qualitatively stronger without producing measurable score lift.

**C-13 and C-14 are orthogonal enforcement axes.** The V-01/V-02 symmetric miss confirms that labeled-prose-with-F-IDs and table-form-without-F-IDs each fail exactly one criterion and produce identical scores. Neither mechanism substitutes for the other.

**F-08 was the only R2 gap.** The hypothesis that R2 V-05 required only F-08 to close C-14 is confirmed. All other blocks already had named halt conditions — the unique catches block was the sole missing coverage point.

**BLOCK 1.5 as qualitative pattern.** V-05's coverage verification block prevents reviewer drop mid-output proactively, where F-01 catches it reactively. This proactive-vs-reactive distinction is a real quality dimension not yet captured in rubric criteria. Candidate for C-15 in R4.

---

### Excellence Signals

**From V-03 (minimal winning form):**
1. **F-ID failures are precisely localizable.** Adding a single named halt condition (F-08) to a prompt that already passes C-14 on all other blocks closes the criterion with zero other changes. C-14 is compositional — each block's coverage is independent, and gaps can be fixed surgically.

**From V-04 (strongest combined without extra lifecycle block):**
2. **Gate language at block transitions is qualitatively superior even at equal rubric score.** The "Gate: [condition]. Do not begin [NEXT BLOCK] without [verification]." pattern produces a sequencing contract that named F-IDs alone do not — F-IDs halt reactively after a violation; gate transitions prevent the skip from occurring. The rubric does not yet distinguish these enforcement tiers.

**From V-05 (deepest enforcement stack):**
3. **A roster commitment table (BLOCK 1.5) separates expert selection from finding generation as a named lifecycle boundary.** Forcing a reviewer list before BLOCK 2 makes the omission of any scheduled reviewer an explicit F-01 fire rather than a silent drop. The pattern extends the C-14 halt mechanism backward one step — not just catching violations, but making the pre-condition for each block's work explicit and verifiable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-13 and C-14 are orthogonal — labeled-prose-with-F-IDs and table-form-without-F-IDs each fail exactly one criterion and score identically, confirming neither mechanism substitutes for the other", "F-ID failures are precisely localizable — a single targeted addition (F-08 for unique catches) is sufficient to close the last C-14 gap without other structural changes", "roster commitment table before finding generation (BLOCK 1.5) converts reactive F-01 halt into proactive pre-condition verification — a new enforcement tier beyond named halt conditions"]}
```
