| V-05 | 50/50 | 33.75/33.75 | 10.0/10 | **100** | C-25 PASS via FRAME CONFIRM + gate CHECK 5/6 |

**Ranking:** V-03 = V-05 (100) > V-01 = V-02 = V-04 (99.7)

---

## Excellence Signals from V-05

**ES-1 — Three-handle annotation with ROW-ID MISMATCH as fourth independent failure mode**

V-01 introduced `[Q: Q1 — vocab: {CS-N} — {term}]` and CHECK 5 validates Q-number, row-id, and term. V-05 extends CHECK 6 with a fourth distinct flag: `[ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]`. This makes row-ID binding independently detectable from term binding — a question can carry the correct term but cite the wrong row (e.g., CS-2 instead of CS-1 for the same term appearing in two positions). V-01's three failure modes cannot catch this; V-05's four failure modes can.

**ES-2 — Source-phrase forensic citation makes row identifiers cross-verifiable**

V-01's replacement format uses `{new-row-id} confirmed in Phase 1 {bucket-name} bucket` — a re-assertion that cannot be verified without returning to Phase 1. V-05's format uses `Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"` — the quoted source phrase must exist verbatim in Phase 1 output. A fabricated row ID cannot produce a matching source phrase; the citation is forensic rather than inferential. CHECK 7 validates that the row identifier can be found in Phase 1 output, closing the fabrication path.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["three-handle annotation binding carries Q-number + row-ID + term as independently flaggable dimensions; verification gate CHECK exposes ROW-ID MISMATCH as a fourth failure mode separate from TERM MISMATCH — a question can carry the correct term but cite the wrong row, which three-failure-mode gates cannot detect", "source-phrase forensic citation in replacement records quotes the verbatim Phase 1 source phrase alongside the row identifier, making the row verifiable by inspection against Phase 1 output; bucket-name re-assertion cannot be cross-checked and permits fabricated row identifiers to pass unchallenged"]}
```
