The file is complete. Here is the full simplification output:

---

## Simplified Prompt Body

**Topic: `{topic}`**

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural commitment is named, formal, and auditable from output. This is the correction register: what the team believed, what the signals proved wrong, and what the next team must inherit as tested knowledge -- with every provenance claim traceable to the artifact that generated it.

*(full body written to `simulations/quest/golden/topic-echo-variate-R20-QU5-simplified-2026-03-16.md`)*

---

## Simplification Report

### What was removed and why

| # | Location | Removed | Words |
|---|----------|---------|-------|
| 1 | Opening | "This is not a summary. This is not a list of findings." | 14 |
| 2 | GATE-TOKEN-REGISTRY post-table | GT-04 rationale paragraph ("a derived gate token... scan-dependent, not diff-detectable") | 55 |
| 3 | TOKEN CONTENT REQUIREMENT intro | "This requirement applies to all four gate tokens..." | 19 |
| 4 | TCR GT-01 | Failure note (covered by MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX) | 14 |
| 5 | GATE-INDEPENDENCE-ENFORCED | Negative restatement ("A combined token carrying...non-conforming") | 18 |
| 6 | GATE-INDEPENDENCE-ENFORCED | Specific name example redundant with Step 7 note | 18 |
| 7 | MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX | "A MANIFEST-COMPLETE token that states..." failure sentence (covered by GT-01 format) | 19 |
| 8 | BC-COVERAGE-RECORD F-BCR-4 | Passing example ("PB-01 through PB-12... passes") | 12 |
| 9 | Step 9 intro | Rationale paragraph explaining WHY the check exists | 32 |
| 10 | Step 7 closing | "These two tokens are at the same step boundary..." paragraph | 32 |
| 11 | ARTIFACT STRUCTURE | Quest-variate AXIS A/B/C meta-annotation Note block | 57 |
| 12-14 | Section headings | [AXIS A/B/C -- C-61/62/63] tracking labels | 23 |
| 15 | Step 8 | "Apply all active declarations:" + 2 bullet lines before protocol | 32 |
| 16 | Phase Handover Schema | "Six required rows, fixed field names:" redundant intro | 6 |
| 17 | EF function decl | "Does not execute any downstream step." (covered by Phase scope) | 7 |
| 18 | BC function decl | Sub-phases enumeration (covered by BC-STEP1-PROTOCOL) | 11 |
| 19 | Step 8 | Self-certifying example token with placeholder CIT-IDs | 50 |
| 20 | Step 9 | "If all rows show MATCH..." + inline token example (→ reference to TCR) | 30 |
| 21 | TCR GT-04 | "A token emitted when any row is MISMATCH..." (covered by protocol HARD GATE) | 15 |
| 22 | ARTIFACT STRUCTURE item 26 | Traversal-free note clause (satisfied by Step 9 note, not by structure list pointer) | 20 |
| 23-25 | GATE-INDEPENDENCE, MANIFEST-TOKEN, MANIFEST-ROW sections | Prose tightening: co-location qualifier, verbose self-certify phrasing, manifest name | 37 |

### Essential criteria verification

| Criterion | Status | Preserved by |
|-----------|--------|-------------|
| E-01: Three roles at exclusive phase boundaries | **PASS** | All three function declarations intact; phase scope fields unchanged |
| E-02: Structural commitments named and auditable | **PASS** | All schema tables, registry, protocol blocks intact |
| E-03: Gate tokens present and self-certifying | **PASS** | TCR format specs for all 4 tokens (GT-01..GT-04) intact |
| E-04: PHASE-HANDOVER tables at all 7 exits | **PASS** | Phase Handover Schema + Steps 0-6 instruction intact |
| E-05: Correction register structure | **PASS** | ARTIFACT STRUCTURE items 1-22 intact |
| C-61: GT-04 in GATE-TOKEN-REGISTRY | **PASS** | Table entry unchanged |
| C-62: TCR comprehensive for all 4 tokens | **PASS** | GT-04 format spec intact |
| C-63: Traversal-free note in Step 9 | **PASS** | Verification note intact, only AXIS label stripped |

```json
{"simplified_word_count": 1943, "original_word_count": 2446, "all_essential_still_pass": true}
```
