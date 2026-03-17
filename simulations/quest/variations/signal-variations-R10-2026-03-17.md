Written to `simulations/quest/golden/signal-variate-R10-2026-03-17.md`.

---

## R10 Variate -- /signal (Round 10)

**Goal**: Confirm independence of C-31, C-32, C-33 by single-axis isolation.

**Axis matrix**:

| V | Axis | C-31 labeled count | C-32 named DNT | C-33 full Check 3 enum | Predicted |
|---|------|--------------------|----------------|------------------------|-----------|
| V-01 | M | PASS | FAIL | FAIL | 99.20 |
| V-02 | N | FAIL | PASS | FAIL | 99.20 |
| V-03 | O | FAIL | FAIL | PASS | 99.20 |
| V-04 | M+N | PASS | PASS | FAIL | 99.60 |
| V-05 | M+N+O | PASS | PASS | PASS | 100.00 |

**What varies per variation** (all other R9 V-05 mechanisms preserved):

- **C-31** (Axis M): transcription gate count formula and BARE gate Check 2 — `8 scout + 4 draft + ... + 4 org = 61` (labeled) vs `8+4+4+7+7+9+3+2+6+4+3+4 = 61` (anonymous)
- **C-32** (Axis N): `DOMAIN NOUN TABLE` section — present as named formal lookup vs absent (nouns inline only in catalog footers)
- **C-33** (Axis O): FULL gate Check 3 — full 12-name sequence `scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org` vs first+last anchors only `(First section: scout. Last section: org.)`

V-05 is structurally identical to R9 V-05 and should confirm 100.00. If V-01/V-02/V-03 each score 99.20 (not 99.60 or some other value), the three criteria are independent with no interaction effects.
