Done. Here's what was written:

---

**`trace-state-variate-R20-2026-03-15.md`** — 1278 lines, 5 complete runnable variations

**`trace-state-rubric-v19-2026-03-15.md`** — scoring round rubric (no new pool; v19 = v18 criteria + R20 scoring guidance)

---

### What changed per variation

| Variant | R19 → R20 change | Target |
|---------|------------------|--------|
| **V-01** | Added C12 constraint requiring IS-NOT/IS canonical contrast in EPOCH-CLUSTER remediation body; added C12 acknowledgment to GATE A and GATE D | C-54 |
| **V-02** | Carried unchanged — C-54 already present in R19 | — |
| **V-03** | Extended C11 to require IS-NOT/IS canonical contrast in ECL-4 step body; updated ECL-4 instruction to require "IS NOT an [epoch-label] finding; IS a [structural-role] finding" | C-54 (step-block path) |
| **V-04** | Extended C12 to require IS-NOT/IS contrast per domain + structural roles on both sides of Finance→Sales handoff; added per-domain C-54 remediation templates and C-55 inter-domain handoff form to EPOCH-CLUSTER ANALYSIS | C-54 + C-55 |
| **V-05** | Extended C13 to require IS-NOT/IS contrast per domain + structural roles at **both** handoff boundaries (Finance→Sales and Sales→CS); added three per-domain C-54 remediations and two C-55 handoff forms | C-54 + C-55 both boundaries |

The key structural distinction in V-04/V-05: C-55 requires naming roles **on both sides** of each handoff. The R19 EPOCH-CLUSTER named the handoff in epoch-label terms ("Finance APPROVAL→Sales ADVANCE"); R20 requires "Finance Gate-boundary→Sales Entry-boundary structural mismatch IS the handoff intervention."
