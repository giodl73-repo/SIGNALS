Generated `topic-plan-variate-R7-2026-03-15-new.md` with 5 complete variations targeting **C-27 (write-surface enforcement completeness)**.

---

## Round 7 — Design axis summary

**New criterion: C-27** — tests whether all three point-of-production blocking mechanisms are present *and architecturally placed* at their write surfaces simultaneously:

| Write surface | What C-27 requires |
|--------------|-------------------|
| WS-1 (Gate 0) | Read-barrier declaration *before Phase 0 actions* naming Gate 0 |
| WS-2 (Schema E/F boundary) | *Labeled block at the boundary* — not buried in Phase 5 instructions |
| WS-3 (null templates) | Banned-forms check *inside each template* — not in a gate condition |

---

## Variation axes

| V | Axis | C-27 mechanism |
|---|------|----------------|
| **V-01** | Role sequence | PRE-COMMIT BLOCK names Gate 0 before Phase 0; SCHEMA BOUNDARY BLOCK as labeled header between Schema D and E; inline WS-3 CHECK in each null template |
| **V-02** | Output format | Three `WS-N BLOCK` first-class section headers at each write surface — structurally visible in any outline view |
| **V-03** | Lifecycle emphasis | WRITE SURFACE REGISTER declared upfront + `[WS-N MILESTONE]` annotations at each lifecycle site |
| **V-04** | Phrasing + inertia framing | Short imperatives with `WHY:` motivations at each enforcement site; NO CHANGE as opening premise |
| **V-05** | Combined | WRITE-SURFACE ARCHITECTURE block declared as governing contract before all schemas; each lifecycle enforcement site references it by name |

**Predicted winner: V-05.** The architecture block before any phase makes C-27 the governing contract, not a checklist item. The WSA-2 labeled block sits between Schema D and Schema E in the *schema section* — the model cannot fill Schema E without crossing it.

**Key discriminator:** WSA-2 placement. Variations where the cell-level check is in Phase 5 instructions (not in the pre-committed schemas section at the Schema D/E boundary) satisfy C-24 individually but miss C-27's "fires at its write surface" requirement.
