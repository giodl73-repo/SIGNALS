**Scorecard written.** Summary:

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-05 Tight Combined | **100.0** | YES |
| 2 | V-02 / V-03 / V-04 | **95.0** | YES |
| 5 | V-01 Verbatim-Copy Seal | **92.8** | YES |

All five are Golden. Projections matched actuals exactly — the single-axis isolation design held.

**Key findings:**

- **C-13**: The verbatim instruction must be in the recall directive itself, not a preamble (`do not paraphrase` co-located with the token slot). V-01's preamble-only instruction worked; V-02's `recall` without `exact sentence` was PARTIAL.
- **C-14**: `SCORING DEFECT:` / `VIOLATION:` structurally adjacent to TOKEN RECALL = PASS. Free sentence inside the same section but not paired to a recall step = FAIL.
- **C-15**: Phase 0A → 0B ordering with explicit "commit before anchor" instruction is sufficient — no ledger required.
- **C-16**: The word HALT / "do not proceed" as the operative instruction is the discriminating element.

**V-05 is the recommended prompt.** Four excellence signals identified: precondition chain ordering, verbatim constraint at point of use, HALT gate scope covering Phase 0 tokens, and AMEND propagating all patterns forward.
| FAIL | PASS |
| C-14 failure class co-located | FAIL | PASS | FAIL | FAIL | PASS |
| C-15 register before anchor | FAIL | FAIL | PASS | FAIL | PASS |
| C-16 blocking ledger gate | FAIL | FAIL | FAIL | PASS | PASS |

---

### Scoring Worksheet

| Variation | Essential (4) | Recommended (3) | Aspirational (/9) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60 | 3/3 = 30 | 2.5/9 = 2.78 | **92.78** | YES |
| V-02 | 4/4 = 60 | 3/3 = 30 | 4.5/9 = 5.00 | **95.00** | YES |
| V-03 | 4/4 = 60 | 3/3 = 30 | 4.5/9 = 5.00 | **95.00** | YES |
| V-04 | 4/4 = 60 | 3/3 = 30 | 4.5/9 = 5.00 | **95.00** | YES |
| V-05 | 4/4 = 60 | 3/3 = 30 | 9/9 = 10.00 | **100.00** | YES |

*Partial counts as 0.5. Aspirational normalized: passed * 10 / 9.*

---

### Criterion Evidence Notes

**C-11 partials (V-01, V-03, V-04)**
- V-01: "Compare against ANCHOR[0] only — not against Option B" — directional instruction; no named failure class
- V-03: Same pattern as V-01 in each inertia section
- V-04: "Do not reference Option B at this step" — directional framing, no named failure class

**C-13 partial (V-02)**
- TOKEN RECALL present: `ANCHOR[0] = {recall the anchor sentence from above}` — but "recall" does not mandate verbatim reproduction; no "exact sentence" or "do not paraphrase" instruction

**C-09 pass (V-03, V-05)**
- V-03: REG token applied to all phase labels; TOKEN RECALL `REG:` at recommendation; audience handled in primary flow, not only in AMEND
- V-05: Same plus REG label overrides in matrix and Phase 8 TOKEN RECALL for both REG and ANCHOR[0]

**C-10 pass (V-04, V-05)**
- V-04: 9-token HALT GATE; matrix assembled by explicit token reference; "Assemble from HALT GATE tokens" with column cells labeled by token name
- V-05: 10-token LEDGER GATE (includes REG and ANCHOR[0]); same assembly pattern; gate scope covers Phase 0

**C-16 pass (V-04, V-05)**
- V-04: "HALT — If any token is marked absent, do not proceed to Step 6" — explicit blocking instruction
- V-05: "HALT — do not proceed to Phase 6 if any token is absent" — same operative word

**C-13 pass (V-01, V-05)**
- V-01: "copy this exact sentence — not a paraphrase, not a reference to 'the anchor.' Verbatim copy only." in preamble + inline copy placeholder
- V-05: TOKEN RECALL: `{reproduce exact sentence from Phase 0 — do not paraphrase}` — verbatim constraint embedded in the recall directive itself at point of use

**C-14 pass (V-02, V-05)**
- V-02: `SCORING DEFECT:` label immediately after TOKEN RECALL — named failure class co-located at point of use
- V-05: `VIOLATION:` label immediately after TOKEN RECALL with "is an error" — same pattern; tighter because "VIOLATION" is a harder class name

**C-15 pass (V-03, V-05)**
- V-03: Phase 0A (REG) before Phase 0B (ANCHOR[0]); "commit register before anchor" ordering stated in Part B header
- V-05: Same; additionally, Phase 0 print statement confirms REG and ANCHOR[0] committed before Phase 1 begins; Phase 0A label explicitly says "commit first, before anchor"

---

### Rankings

| Rank | Variation | Composite | New C-13 | New C-14 | New C-15 | New C-16 |
|------|-----------|-----------|----------|----------|----------|----------|
| 1 | V-05 Tight Combined | 100.0 | PASS | PASS | PASS | PASS |
| 2 | V-02 Co-located Failure Class | 95.0 | PARTIAL | PASS | FAIL | FAIL |
| 2 | V-03 Register-Prime | 95.0 | FAIL | FAIL | PASS | FAIL |
| 2 | V-04 Halt-Gate Ledger | 95.0 | FAIL | FAIL | FAIL | PASS |
| 5 | V-01 Verbatim-Copy Seal | 92.8 | PASS | FAIL | FAIL | FAIL |

---

### Projection Accuracy

Projected vs actual composites:

| Variation | Projected | Actual | Match |
|-----------|-----------|--------|-------|
| V-01 | ~93 | 92.78 | YES |
| V-02 | ~95 | 95.00 | YES |
| V-03 | ~95 | 95.00 | YES |
| V-04 | ~95 | 95.00 | YES |
| V-05 | 100 | 100.00 | YES |

All criterion-level projections matched exactly. Single-axis isolation design confirmed: each V-0x (1-4) passed exactly its target criterion and no others among the new four.

---

### Key Discriminating Results

**V-01 vs V-02 on C-13**: PASS vs PARTIAL confirmed. "copy this exact sentence — not a paraphrase... Verbatim copy only." (V-01) is sufficient for C-13. "recall the anchor sentence" (V-02) without "exact sentence" or "do not paraphrase" is not — model may paraphrase. **Verbatim instruction is the load-bearing element.**

**V-02 vs V-01-R2 on C-14**: V-02 `SCORING DEFECT:` immediately after TOKEN RECALL = PASS. R2 V-01 placed "is an error" as a free sentence (not co-located with a TOKEN RECALL step). **Structural adjacency to TOKEN RECALL is required for C-14.**

**V-03 on C-15**: Phase 0A → Phase 0B ordering with explicit "commit before anchor" instruction and REG TOKEN RECALL at recommendation = PASS. C-15 does not require a token ledger — the two-part Phase 0 structure alone is sufficient.

**V-04 on C-16**: "HALT — If any token is marked absent, do not proceed" = PASS. R2 V-02 used "Do not assemble the matrix with gaps" = FAIL (status confirmed by R2 scoring). **The explicit HALT/do-not-proceed blocking word is the discriminating element for C-16.**

---

### Excellence Signals from V-05

**1. Phase-ordered commitment as a precondition chain.**
REG → ANCHOR[0] → analysis phases. Each phase requires the prior to be committed. The anchor sentence is written in the declared register because register was committed first. Structural, not instructional.

**2. Verbatim constraint co-located with TOKEN RECALL directive.**
`TOKEN RECALL: {reproduce exact sentence — do not paraphrase}` — the no-paraphrase rule is inside the recall directive at the point where drift would occur. V-01 placed the verbatim instruction in a preamble; V-05 binds it to the token slot.

**3. VIOLATION immediately after TOKEN RECALL.**
The failure class names itself at the token it guards. No path through the inertia phase exists that doesn't encounter both the recall step and its violation label in sequence.

**4. HALT gate scope covers Phase 0 tokens.**
REG and ANCHOR[0] are in the 10-token ledger alongside analysis tokens. The HALT that enforces matrix assembly also enforces Phase 0 commitment. Single gate covers the full dependency chain.

**5. AMEND propagates the patterns forward.**
Option C in AMEND explicitly requires TOKEN RECALL of ANCHOR[0] verbatim + VIOLATION prohibition for INERT-C. The structural patterns survive prompt extension.

---

### Recommended Prompt: V-05

V-05 is the recommended prompt for `discover-compare`. All 16 criteria pass; all four structural enforcement patterns from R3 are present; AMEND propagates the patterns to any added option. Composite 100 / Golden.
