Written to `simulations/quest/rubrics/scout-inertia-rubric-v19-2026-03-17.md`.

**v18 → v19 summary**

| # | Criterion | Source signal | Key distinction |
|---|-----------|---------------|-----------------|
| A-44 | **Verification-action register in bridge completion status table column label** | R18 V-01: BUILT → VERIFIED in status table column (second of three co-located register changes) | A-43 requires the gate heading interrogative to use VERIFIED; A-44 additionally requires the same register in the gate's artifact-status column label — column says "VERIFIED?" not "BUILT?" |
| A-45 | **Verification-action register in bridge completion command directive** | R18 V-01: BUILT → VERIFIED in command body (third of three co-located register changes) | A-43 requires the heading verb; A-45 additionally requires the command directive label/body to use verification-action vocabulary — "[BRIDGE VERIFICATION COMMAND]" not "[BRIDGE COMPLETION COMMAND]" |

**Ceiling: 270 → 280**

**Three-point gate register coherence**: A-43 (heading) + A-44 (status column) + A-45 (command directive) — when all three are satisfied, no sub-element of the gate uses completion-state vocabulary that contradicts the verification-action intent.

**New implication chains:**
- `A-45 implies A-43 implies A-39 ... implies A-12`
- `A-45 implies A-25 implies A-22 implies A-12`
- `A-44 implies A-43 implies A-39 ... implies A-12`
- `A-44 implies A-22 implies A-12`
