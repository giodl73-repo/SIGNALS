Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v12-variate-R12-2026-03-15.md`.

---

# flow-lifecycle — Round 12 Variations (Rubric v12)

## What changed from R11 → R12

R11 cracked C-40 and C-41 as signals. R12 now targets them with structural precision.

**Key distinction from R11 probes:**

| R11 field | What it probed | What R12 adds instead |
|-----------|---------------|----------------------|
| `Bottleneck Ref: B-NN` in EX blocks | Exception→B-NN direction | `Role Ref: R-ID` — Exception→Role direction (C-40) |
| `Prior phase blocked bottleneck: B-ID` | B-NN phase-boundary continuity | `Prior phase: PHASE N` — Phase→Phase sequence (C-41) |

Both new fields **coexist** with the R11 fields — not replacements.

## Variation Table

| ID | Axis | Key change | C-40 hypothesis | C-41 hypothesis |
|----|------|-----------|-----------------|-----------------|
| **V-01** | D only | `Role Ref: R-ID` in EX blocks, one direction | Minimum for C-40 if single-direction sufficient | Not probed |
| **V-02** | D + E | Role Ref + registry gate fourth check (Role→Exception closure) | Minimum for C-40 if bidirectional required | Not probed |
| **V-03** | F only | `Prior phase: PHASE N` in PHASE ENTRY CONTRACT | Not probed | Minimum for C-41 in isolation |
| **V-04** | D + F | Role Ref + Prior phase, no gate closure | C-40 if single-direction | C-41 independently |
| **V-05** | D + E + F | Full bidirectional Role Ref + Prior phase | Maximum — both directions | Sequential linkage confirmed |

## Architecture summary (V-05 is the ceiling)

V-05 activates a **seven-artifact cross-reference system**:

```
INCUMBENT BASELINE (IM-IDs)
  ↓ Baseline→B-NN (C-34)
B-NN blocks ← Phase→B-NN (C-37) ← PHASE EXIT GATE (Blocked bottleneck)
  ↑↓ SLA↔B-NN (C-14/C-16)
SLA ANALYSIS
  
ROLE SEQUENCE SCHEDULE (R-IDs)
  ↓ Role→B-NN (C-39 Condition B) via B-NN Cause field
  ↓ Role→Exception (C-40 gate check) ← EX blocks (Role Ref: R-ID)
                                               ↕ Exception→Role (C-40 block)

PHASE ENTRY CONTRACT (Prior phase: PHASE N)
  ↔ Phase→Phase (C-41)
PHASE ENTRY CONTRACT (Prior phase blocked bottleneck: B-ID)
  ↔ Phase-boundary B-NN continuity (R11)
```

Every artifact is reachable from every other via at most two string comparisons.
