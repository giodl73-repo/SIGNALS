Simplified prompt looks clean. Now the full simplification report:

---

## Simplification Report — scout-stakeholders golden prompt

**Original (V-05 golden):** 2,752 words  
**Simplified:** 2,180 words  
**Removed:** 572 words (**20.8% reduction**)

---

### What was removed and why

| # | What | Words saved | Justification |
|---|------|-------------|---------------|
| 1 | `"Do not begin conflict analysis until Phase 1 is complete. Do not build the grid until Phase 2 is complete."` | 24 | Redundant with FAIL_INCOMPLETE_PHASE1/2 transition gates |
| 2 | `"Prose annotations are permitted alongside structural outputs but do not replace them."` | 17 | No criterion enforces this; clarification-only |
| 3 | Step 0b intro: tightened to `"Name each displaced workflow or tool before Phase 1."` | 6 | Shorter phrasing, same instruction |
| 4 | `"Assign three prefill-calibrated attributes per entry."` | 7 | Self-evident from 3-column table |
| 5 | Step 0b competitor template row | 18 | Column headers define structure; FAIL_NO_COMPETITOR_ENTRY enforces presence |
| 6 | Step 0c `"INERTIA FRAMING NOTE:"` label + `"Step 6b displacement-acknowledgment messages are checked against these requirements."` | 15 | Label is decoration; the sentence restates Step 6a Rule 4 |
| 7 | Step 0c template row | 20 | Downstream message requirement bullets define content; column headers define structure |
| 8 | Phase 1 template row | 13 | Column headers define structure |
| 9 | Step 2a-prefill Escalation Implication column | 22 | Guidance only; escalation behavior is enforced by Step 2a's escalation tier table and FAIL_NO_ESCALATION_PATH |
| 10 | Step 2a resolution + escalation template rows | 33 | Column headers define structure; FAIL codes enforce required fields |
| 11 | Step 2b + 2c template rows | 27 | Column headers define structure |
| 12 | Step 3c ROLE SEQUENCE NOTE middle sentence `"Temporal reliability is established before epistemic basis classification."` | 9 | Explanatory flair; zero behavioral implication |
| 13 | Step 3c Reliability Implication column → replaced with 2-line footer | Net −16 | CURRENT/STALE implications are guidance-only; EXPIRED obligation moved to explicit footer text (preserved C-49) |
| 14 | Step 3b ROLE SEQUENCE NOTE second sentence | 14 | Already stated in Step 3c |
| 15 | Step 3b Amendment Obligation column → replaced with 1-line footer | Net −16 | OBSERVED/INFERRED implications are guidance-only; ASSUMED obligation moved to explicit footer text (preserved C-23) |
| 16 | Phase 3 `"ASSUMED entries and EXPIRED Source Age entries are mandatory Step 8 amendment targets."` | 14 | Now carried in Steps 3b and 3c footers |
| 17 | Step 4a `When to Use` column | 9 | Range column already tells when to apply each band |
| 18 | Step 4b template row | 10 | Column headers + ordering rule define structure |
| 19 | Step 5a `"Update Phase 3 grid Engagement Window column with derived values."` | 13 | Implicit — grid has TBD marker, step produces the values |
| 20 | Step 5a, 5b template rows | 20 | Column headers define structure |
| 21 | Step 6a Rule 1 | 15 | Redundant — the table's `When to Use` column already implies correct application; FAIL codes enforce specifics |
| 22 | Step 6c `"Fallback may be used only when primary is explicitly unavailable. Document reason in Message cell."` | 20 | No FAIL code enforces fallback documentation |
| 23 | Step 6b opening 2-line prose about FAIL_RESPONSE_TRACK_ALIGNMENT | 22 | Already in Step 0c and Step 6a Rule 4; FAIL code is in the 6b fail list |
| 24 | Step 6d template row | 12 | Column headers define structure |
| 25 | Step 6e-priority Resource Implication column | 20 | Guidance-only; FAIL_UNCALIBRATED_PRIORITY only checks that the label is from the prefill |
| 26 | Step 7 template row | 9 | Column headers define structure |
| 27 | Step 8 eligible targets: compressed from 31-word list to `"any structural output in this prompt"` | 24 | Any structural output is eligible; enumeration adds no gate |
| 28 | Step 8 ASSUMED/EXPIRED obligation paragraphs: compressed | 11 | Same obligation, fewer words |
| 29 | Step 8b template rows | 12 | Column headers define structure |
| 30 | Step 9b `"OUTPUT FORMAT NOTE:"` label | 3 | Decoration |
| 31 | Step 9b `"Distinct from FAIL_NO_SYNTHESIS (C-32) and FAIL_SYNTHESIS_GAP (C-42): as defined above."` | 12 | Rubric meta-references; does no work in runtime prompt |
| 32 | `"— PM role"` from all Phase 3+ step sub-headers (Steps 3a–9b) | ~40 | Role established by Phase 3 phase header; no FAIL code checks sub-header role annotations |

---

### Essential criteria verified: ALL PASS

| Criterion | Key mechanism | Status |
|-----------|---------------|--------|
| C-01 (org state machine) | Step 0 table + `[STATE: ...]` output + FAIL_SILENT_INFERENCE | ✅ |
| C-51 (staleness before typology) | Step 3c ROLE SEQUENCE NOTE retained; Step 3b follow-up note retained | ✅ |
| C-54 (EXPIRED→ASSUMED pathway) | `"EXPIRED sources should be tentatively reclassified as ASSUMED in Step 3b if no refresh is available."` retained | ✅ |
| C-52 (Step 9b checksum matrix) | Full format spec, N/A reason codes, PASS/FAIL/N/A definitions all retained | ✅ |
| C-55 (column-pattern anomaly detection) | Step 9b matrix structure unchanged — column-pattern detection enabled by format | ✅ |
| C-53 (engagement obligations table) | Step 0c full table + bullets + Rule 4 in Step 6a + FAIL_RESPONSE_TRACK_ALIGNMENT in Step 6b | ✅ |
| C-23 (ASSUMED amendment obligation) | Step 3b footer + Step 8 mandatory paragraph | ✅ |
| C-49 (EXPIRED amendment obligation) | Step 3c footer + Step 8 mandatory paragraph | ✅ |
| C-48 (displacement-acknowledgment ordering) | Step 6a Rule 3 retained | ✅ |
| All FAIL codes from V-05 | All 40+ FAIL codes preserved or correctly chained via "as defined above" | ✅ |

**`all_essential_still_pass`: YES**

---

Simplified prompt written to `simulations/quest/golden/scout-stakeholders-golden-simplified-2026-03-15.md`.

```json
{"simplified_word_count": 2180, "original_word_count": 2752, "all_essential_still_pass": true}
```
