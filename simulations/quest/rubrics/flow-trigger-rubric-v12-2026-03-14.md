`simulations/quest/rubrics/flow-trigger-rubric-v12-2026-03-15.md` written.

---

**What was extracted and why:**

| Criterion | Source | Structural property |
|-----------|--------|---------------------|
| **C-33** | V-01 axis | Gates transition from prose pre-conditions to named `GATE-STATE` blocks with keyed fields; absent gate block is detectable by Role 5 (gate gap), not inferred from phase order |
| **C-34** | V-02 axis | All five certificate columns carry `<- named key ref: CHAIN-LINK-N.KEY` annotations; absent CHAIN-LINK produces a named `COLUMN-GAP` in the specific column, not just a chain integrity list entry |
| **C-35** | V-03 axis | PCR Analyst extracted from Inertia Analyst as a fourth independent terminal artifact owner; independence declaration names prediction-authorship as the self-attestation boundary being closed |

**Denominator**: /25 → /28.

**R15 scores under v12**: V-01/V-02/V-03 each earn exactly one new criterion → 26/28 → composite **99.29**. V-04 (combined V-01+V-02) earns two → 27/28 → **99.64**. V-05 (all three + triple-entity Role 5) earns all → 28/28 → **100.00** — second consecutive perfect score, now on a harder rubric.

**R14 retroactive impact**: All five R14 variations score 0 on C-33/C-34/C-35 — none have gate artifact blocks, full-column key refs, or PCR independence. R14 V-05 drops from 100.00 (v11) to 98.93 (v12), correctly reflecting that the ceiling moved.
