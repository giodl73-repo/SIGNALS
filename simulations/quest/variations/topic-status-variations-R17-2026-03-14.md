---

## Variations: `topic:status` -- Round 17
**Rubric:** v16 (max 295) | **Date:** 2026-03-15

---

### Design Context

R16's V-03 was contaminated: it applied a readiness-first template reordering axis alongside the C-48 ablation, causing C-12 and C-20 failures unrelated to C-48 (−10 pts contamination). R17's primary purpose is a clean C-48 isolation. V-01, V-02, V-04, V-05 carry identical structure to their R16 counterparts.

**Predicted score map under v16:**

| Variant | C-47 | C-48 | C-12 | C-20 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 295/295   |
| V-02    | FAIL | PASS | PASS | PASS | 290/295   |
| V-03    | PASS | FAIL | PASS | PASS | 290/295   |
| V-04    | PASS | PASS | PASS | PASS | 295/295   |
| V-05    | PASS | PASS | PASS | PASS | 295/295   |

V-02 and V-03 score symmetrically at 290 — confirming C-47 ⊥ C-48.

---

### V-01: Minimum delta — full-stack baseline (execution-prose)
**Axis:** Identical to R16 V-01. Three-element labeled ADVERSARY CHAIN preamble (C-47 PASS). PHASE 1 ADVERSARY: / DEFEAT CONDITION: block (C-48 PASS). All 48 criteria satisfied. Expected: **295/295**.

---

### V-02: Single axis — C-47 withheld
**Axis:** Identical to R16 V-02 (clean isolation confirmed). Preamble ADVERSARY CHAIN block in running prose naming all three adversaries — no `P1-ADVERSARY:` / `P2-ADVERSARY:` / `P3-ADVERSARY:` labeled entries. PHASE 1 execution body carries full three-part adversary block (C-48 PASS). Expected: **290/295** (C-47 FAIL only).

---

### V-03: Single axis — C-48 withheld (redesigned, no contamination)
**Axis:** PHASE 1 execution body carries no `ADVERSARY:` / `DEFEAT CONDITION:`. Preamble ADVERSARY CHAIN carries `P2-ADVERSARY:` and `P3-ADVERSARY:` labeled sub-entries (two-element labeled chain — C-47 PASS; label count tracks chain length, two labels when C-48 absent). **No template reordering** — LAYER 1 STRUCTURAL (COMMIT RISK REGISTER) remains first, [LAYER 2] retains PER-SIGNAL COMMITMENT ASSERTION vocabulary. Only structural difference from V-01: removal of PHASE 1 adversary block + removal of P1-ADVERSARY: preamble entry. Expected: **290/295** (C-48 FAIL only, no contamination).

---

### V-04: Combination — Lifecycle GUARD contract form
**Axis:** Identical to R16 V-04. Phase contract boxes (INPUT / GUARD / OUTPUT) with adversary+defeat-condition prose appended below each phase box. C-47+C-48 PASS. Tests form-agnosticism. Expected: **295/295**.

---

### V-05: Combination — Elevated titled adversary-declaration blocks
**Axis:** Identical to R16 V-05. All three phases receive `+-- PHASE N ADVERSARY DECLARATION --+` titled boxes with `ADVERSARY:` / `TRIGGER:` / `DEFEAT CONDITION:` fields. Three-element labeled preamble ADVERSARY CHAIN. Tests form-agnosticism across a third execution style. Expected: **295/295**.

---

**Key design result:** V-03 is the sole redesign. The C-48 contamination is eliminated by applying zero additional axes — only remove the PHASE 1 adversary block and the corresponding P1-ADVERSARY: preamble label. The symmetric V-02/V-03 delta of 0 under v16 proves C-47 and C-48 are independently observable.

File written to `simulations/quest/rubrics/topic-status-rubric-v16-variate-R17-2026-03-15.md`.
