Written to `simulations/quest/golden/crew-review-variate-R11-2026-03-16.md`.

---

## crew-review -- Variate R11

**Design target**: 172.5/172.5 under v10 (all 32 criteria PASS)

**Critical fix from R10**: V-03 R10's G2 said `"PHASE 4 does not begin until G2 transitions to CLOSED"` — wrong downstream target. C-32 mirrors C-17 exactly: G1 blocks domain review (PHASE 3), so G2 must block **AMEND** (the post-render command interface). All 5 R11 variations use `"AMEND does not begin until G2 transitions to CLOSED."` This closes both C-31 and C-32.

---

### Variation summary

| V | Axis | Key structural feature | C-31 | C-32 | Predicted |
|---|------|------------------------|------|------|-----------|
| V-01 | Lifecycle (direct integration) | PHASE 3.5 added to V-01/R10 canonical | PASS | PASS | **172.5** |
| V-02 | Output format | Synthesis output as typed 3-column schema (Slot \| Verdict Type \| Statement); G2 checks table row count | PASS | PASS | **172.5** |
| V-03 | Inertia framing | Slot 1 (inertia) must name its relationship to domain slots in G2 closure condition 1 | PASS | PASS | **172.5** |
| V-04 | Lifecycle + Output format | Synthesis contract in 3 locations: schema AMEND contract + G2 predicate + synthesis table row count | PASS | PASS | **172.5** |
| V-05 | Three-axis (+ Role sequence) | V-04 + verbatim `expertise.relevance` quotes + L5 registry verification; G2 note references L5-verified manifest | PASS | PASS | **172.5** |

### New excellence signals discovered

- **Pattern 6**: G2 downstream target correction (all) — AMEND, not VALIDATE
- **Pattern 7**: Typed synthesis schema parallel (V-02/V-04/V-05) — `C-33` candidate: schema discipline applied to every structured phase output
- **Pattern 8**: Inertia-synthesis anchor (V-03) — `C-33` candidate: Slot 1 synthesis verdict must name inertia implications, not just "unique"
- **Pattern 9**: Triple-location synthesis enforcement (V-04/V-05) — exhaustive enforcement path coverage principle
- **Pattern 10**: Verbatim field citation provenance chain (V-05) — registry → L5 verification → G2-verified synthesis
