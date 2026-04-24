## Round 11 — draft-proposal Scorecard

**Rubric v11 · /30 denominator · All 5 variations: Golden**

| Rank | Variation | Designed Fails | Aspirational | Score |
|------|-----------|----------------|--------------|-------|
| 1 | V-05 Inertia + motivated | none | 30/30 | **100.00** |
| 2 | V-03 Split-gate lifecycle | C-37 | 29/30 | **99.67** |
| 2 | V-04 Conversational register | C-25 | 29/30 | **99.67** |
| 4 | V-01 Architect-first | C-34, C-36, C-37 | 27/30 | **99.00** |
| 4 | V-02 Compact tables PM-first | C-33, C-35, C-37 | 27/30 | **99.00** |

**Prediction table correction**: The round summary predicted 99.33 for V-01 and V-02. The per-variation hypotheses are authoritative: both have 3-failure designs (27/30 = 9.00 pts), not 2. Actual score is 99.00 for each.

---

**Key discriminator findings:**

- **C-37 appears in 3 of 5 failure sets** — confirmed R11 discriminator. Any variation supplying only one Phase 0 contract also supplies only one gate binary and automatically fails C-37 via cascade (V-01, V-02). V-03 is the structurally interesting case: both contracts present, both gate binaries exist, C-37 fails purely from sub-section separation — co-presence violated without any content missing.

- **Cascade invariant:** 1 absent Phase 0 contract → exactly 3 failures (contract criterion + gate binary criterion + C-37). Deterministic under v11.

- **V-04 confirms register orthogonality again:** Conversational phrasing affects zero structural criteria through R11.

**Excellence signals from V-05:** (1) Dual-contract gate completeness — both Phase 0 contract binaries co-present in a single gate block, minimal-scroll auditability. (2) Inertia-first narrative coherence — the causal chain formula is *earned* by the document's framing rather than bolted on. (3) Frontline T-GUARD × dual-contract gate — closed enforcement loop with no escape path.

**No new v12 criterion warranted** from split-gate finding; C-37's "same gate block" language already covers the V-03 failure mode.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["dual-contract gate completeness: both Phase 0 contract binaries co-present in same undivided gate block creates minimal-scroll auditability model", "split-gate fragmentation failure: sub-section separation of contract binaries within gate passes C-35/C-36 individually but breaks C-37 co-presence — adding structure can violate conjunction requirements", "cascade invariant: 1 absent Phase 0 contract causes exactly 3 aspirational failures (contract + gate binary + C-37) — motivated variations must supply both contracts to escape cascade"]}
```
