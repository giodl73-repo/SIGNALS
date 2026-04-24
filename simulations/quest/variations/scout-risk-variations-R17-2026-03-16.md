Written to `simulations/quest/golden/scout-risk-variate-R17-2026-03-17.md`.

---

## Scout-Risk — Round 17 Variations (Summary)

**Baseline:** R16 V-05 scores **172/174** on the v16 rubric. C-48 (structural independence) and C-49 (per-site citation) are already PASS. The only gap is **C-50** — Phase 0c has no explicit closure declaration sentence.

**The 3 variation axes:** `output format` (C-50 phrasing) · `lifecycle emphasis` (C-48 structural parity explicit) · `phrasing register` (C-49 fully-qualified citation name)

| Var | Axis | Phase 0c change | C-50 | Predicted score |
|-----|------|-----------------|------|-----------------|
| V-01 | Output format | "This taxonomy is closed." | PARTIAL | 173/174 |
| V-02 | Output format | "No violation category outside this list may be named at any prohibition site." | PARTIAL | 173/174 |
| V-03 | Output format | Both sentences (full two-part) | PASS | 174/174 |
| V-04 | Output format + Lifecycle | Full two-part + structural parity sentence ("equal structural weight to Phase 0") | PASS | 174/174 |
| V-05 | All three | Full two-part + parity + citations upgraded to `(Phase 0c Violation Taxonomy)` everywhere | PASS | 174/174 |

**Key design decisions:**
- V-01 and V-02 are deliberate isolation tests of C-50's two halves — they're expected to land at PARTIAL, not golden. This surfaces whether the rubric's "AND" compound is enforced or the stronger half alone suffices.
- V-03 is the safe reference implementation — minimal surgery on top of R16 V-05.
- V-04 makes C-48 self-evident by local inspection rather than inferred from document structure.
- V-05 is the maximum expression: every prohibition site cites the exact block name as declared in the phase heading, making C-49 verifiable character-by-character.
