`draft-proposal-rubric-v11-2026-03-15.md` written.

**What changed from v10:**

**C-36 — PREREQUISITE GATE extension for Phase 0 option anatomy contract verification**
Source: R10 V-01's gate item 9, which audited `PM FRAMING:` / `ARCHITECT VALIDATION:` anatomy contract presence in the gate. C-34 requires the anatomy contract to exist; C-36 requires the gate to include a binary making it machine-checkable at Phase 11 without Phase 0 scroll. Mirrors C-35 for the orthogonal Phase 0 contract.

**C-37 — PREREQUISITE GATE dual-contract coverage**
Source: The R10 discriminator finding that V-01 has the anatomy gate binary (C-36) but not the causal gate binary (C-35 FAIL), and V-02 has the causal gate binary (C-35) but not the anatomy gate binary (C-36 FAIL). Neither single-axis variation can satisfy C-37. A motivated R11 variation must combine C-33 + C-34 + C-35 + C-36 simultaneously.

**Denominator:** `/28` → `/30`. Each aspirational criterion = `0.333` points.

**Score projections under v11:**
| Variation | Aspirational pass | Composite |
|-----------|-------------------|-----------|
| R10 V-01 (C-34, C-36 pass; C-35, C-37 fail) | 27/30 | 99.00 |
| R10 V-02 strict (C-35 pass; C-32, C-34, C-36, C-37 fail) | 26/30 | 98.67 |
| R11 motivated (C-28–C-37 all pass) | 30/30 | 100.0 |

**Also clarified in v11:** C-32's pass condition now explicitly states that non-role typed fields such as DESCRIPTION placed before `PM FRAMING:` violate the "first typed field" requirement — closing the ambiguity exposed by R10 V-02's DESCRIPTION-first template.
