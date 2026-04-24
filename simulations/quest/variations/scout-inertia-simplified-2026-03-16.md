## Simplification Analysis

### Step 1: Identify dead weight

| Phrase/Sentence | Verdict | Reason |
|---|---|---|
| "Here are the 5 complete variations for R20, written to `simulations/quest/golden/...`" | **CUT** | Pure status preamble — no rubric work |
| `## R20 Summary`, `## Variations` headings | **CUT** | Structural scaffolding, content stands without them |
| `---` separators | **CUT** | Formatting only |
| **Design confirmation** paragraph (R19 already demonstrates... pattern's stability) | **CUT** | Historical context — the table + invariant already show what positions are covered; this adds no new structural content |
| "three rule labels" in A-47 description | **CUT** | Already stated in A-46; pure repetition |
| "Every rule label follows the fully normalized three-part schema" | **CONDENSE** | → "Rule labels follow" (same claim, 6 fewer words) |
| "Key structural invariant satisfied in all 5" | **CONDENSE** | → "Invariant (all 5)" |
| "The single-axis choices isolate... The combined forms test..." (30 words) | **CONDENSE** | The table's Axis column already contains this; keep as a 16-word mapping line |

### Step 2: Simplified prompt body

---

**New criteria**: A-46 (bracket-suffix criterion-ID in all three rule labels) + A-47 (RULE as normalized structural noun)

| # | Axis | Domain | Schema | Gate verb | Cardinality | Predicted |
|---|------|--------|--------|-----------|-------------|-----------|
| V-01 | Single-axis phrasing register | INERTIA THREAT | SECTION flat | VERIFIED | EACH | 290/290 |
| V-02 | Single-axis inertia framing (adversarial FAIL-FIRST) | STATUS QUO | SECTION flat | VERIFIED | ALL | 290/290 |
| V-03 | Single-axis lifecycle emphasis | DEFAULT OPTION | STAGE nested | VERIFIED | BOTH | 290/290 |
| V-04 | Combined: domain + schema | INCUMBENT | STAGE nested | CONFIRMED | EACH | 290/290 |
| V-05 | Combined: domain + schema + verb (max normalization) | STATUS QUO | STAGE nested | VALIDATED | ALL | 290/290 |

**Invariant (all 5)**: Rule labels follow `[AXIS-SUBJECT] [DESCRIPTOR] RULE [CRITERION-ID]` at all three positions (A-16 source, A-19 citation, A-31 fail-first), satisfying A-42 + A-46 + A-47.

Single-axis: V-01 vs V-02 (phrasing register), V-01 vs V-03 (lifecycle). Combined: V-04 (INCUMBENT/STAGE), V-05 (STATUS QUO/STAGE/VALIDATED).

---

### Step 3: Essential criteria check

| Criterion | Original coverage | Simplified coverage | Passes? |
|---|---|---|---|
| A-46 bracket-suffix criterion-ID in all three positions | New criteria line + invariant | New criteria line + invariant | YES |
| A-47 RULE as normalized structural noun | New criteria line + invariant | New criteria line + invariant | YES |
| A-42 domain prefix | Invariant paragraph | Invariant paragraph | YES |
| All three positions A-16/A-19/A-31 | Invariant paragraph | Invariant paragraph | YES |
| Axis isolation pattern (single vs combined) | Last paragraph | Condensed last line | YES |
| 5 variations with full parameters | Table | Table (unchanged) | YES |
| 290/290 predicted scores | Table | Table (unchanged) | YES |

### Step 4: Report

**Removed (90 words, 42%):**
- Status preamble: *"Here are the 5 complete variations for R20, written to..."* — pure output acknowledgment
- Design confirmation paragraph (41 words): historical R19/R20 comparison context already implied by the table
- Section headings + separators (3 words)
- Redundant phrase "three rule labels" from A-47 (already in A-46 description)
- Verbose invariant label condensed from 7 words to 3
- Final paragraph condensed from 30 words to 16 — axis mapping is already latent in the table's Axis column; the condensed version preserves the V-01→V-02 comparison signal without the filler prose

**Retained (123 words):**
- All 5 table rows with all 6 columns — structural evidence
- New criteria line — names both new criteria explicitly
- Invariant paragraph — names schema, positions, criteria IDs
- Axis isolation line — preserves comparison pairs and combined-form targets

```json
{"simplified_word_count": 123, "original_word_count": 213, "all_essential_still_pass": true}
```
