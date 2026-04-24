Written to `simulations/quest/golden/topic-report-golden-2026-03-14.md`.

---

## Round 6 Variations — `topic-report`

**Base**: R5 V-04 (12/14 under v6, misses C-21 + C-22). All 5 variations build on the full C-01–C-20 foundation.

---

### V-01 — Single axis: C-21 inertia framing only

**Hypothesis**: Adding `[RULE NEXT-CONCRETE C-21]` stall-cost clause to the NEXT STEP slot converts a label into a commitment without a named recovery header. Tests whether C-21 alone is the primary reliability gain from R5 V-05.

Key addition to V-04(R5):
```
[RULE NEXT-CONCRETE C-21]: State the concrete action, then the stall cost of deferring it.
  correct: "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready."
  form: "{skill} ({ns}). Leaving this open {readiness consequence}."
```

**Expected**: 13/14 — misses C-22 (no explicit THREE-LAYER header)

---

### V-02 — Single axis: C-22 explicit THREE-LAYER header only

**Hypothesis**: The named recovery checklist at the write point reduces attention-degradation failures independent of inertia framing. If live-run variance decreases with the header alone, C-22 is an autonomous reliability property.

Key addition to V-04(R5) at SLOT 3:
```
=== THREE-LAYER WRITE POINT ===
LAYER 1 DECLARE  -- [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] govern the readiness sentence.
LAYER 2 ANCHOR   -- The LOCKED BLOCKERS list from Phase 2 (step 2b, frozen by 2d) is the canonical name set.
LAYER 3 VERIFY   -- Execute G-7a and G-7b SCAN immediately below before writing.
Recovery: re-read this header if attention has degraded.
```

NEXT STEP has no stall-cost clause — labels skill only.

**Expected**: 13/14 — misses C-21 (no stall cost at NEXT STEP)

---

### V-03 — Single axis: Inertia propagated to READINESS sentence

**Hypothesis**: C-21 requires inertia at NEXT STEP. What if the readiness sentence itself encodes persistence cost — "Not ready -- missing X; topic stays here until resolved"? Tests whether broader inertia anchoring is signal or noise. Live-run risk: G-04 calibration failure if BLOCKERS is empty.

Key pattern:
```
[RULE G-7a COMPLETENESS]: Every LOCKED BLOCKERS name must appear. The sentence communicates that the topic remains blocked until resolved.
  correct: "Not ready -- missing prove/analysis (prove) and review/design (review); topic stays here until both are resolved."
  violation: "Not ready -- missing prove/analysis (prove)." (omits review/design and persistence framing)
```

Carries both C-21 (NEXT STEP stall cost) and C-22 (THREE-LAYER header).

**Expected**: 14/14 — watch G-04 calibration when BLOCKERS is none

---

### V-04 — Combined C-21 + C-22 — R6 minimal golden candidate

**Hypothesis**: Both C-21 and C-22 slot into V-04(R5) at zero new mechanism. C-21 is a one-clause addition to `[RULE NEXT-CONCRETE]`. C-22 is the `=== THREE-LAYER WRITE POINT ===` header block inserted at SLOT 3 entry. No new phases, no new contract labels, no Branch B structural change.

The full structure: CONTRACT REGISTER (G-1–G-8) → PHASE 1 DISCOVER (CHECKPOINT) → PHASE 2 PRE-COMPUTATION (2b BLOCKERS, 2c G-7a/G-7b guarantees, 2d LOCK) → PHASE 3 WRITE:
- Branch A: SLOT 1 table / SLOT 2 open signals / **SLOT 3 with THREE-LAYER header + G-7a/G-7b [RULE] + worked examples + scan** / **SLOT 4 with stall-cost clause**
- Branch B: sealed, G-8 verification, 4 sections, scan before READINESS, **NEXT line with stall cost**
→ PHASE 4 CONFIRM.

**Expected**: 14/14 = 100 — GOLDEN

---

### V-05 — Ceiling: G-9 contract label + Branch B own THREE-LAYER header + inertia propagation

**Hypothesis**: Three independent extensions beyond V-04(R6):
1. **G-9 INERTIA** contract label — makes the stall-cost invariant chain-traceable at register → `[RULE G-9 INERTIA]` annotation → NEXT STEP output, matching the G-7a/G-7b pattern. Inertia framing is no longer an unnamed annotation; it's a first-class contract guarantee.
2. **Branch B THREE-LAYER header** — Branch B SECTION 3 gets its own `=== THREE-LAYER WRITE POINT (BRANCH B) ===`. If `--format teams` is the primary failure mode in live runs, this provides an independent recovery point without cross-branch lookup.
3. **Inertia at READINESS** (from V-03 pattern) — readiness sentence includes persistence framing. Combined with G-9, inertia is now present at two output positions with a contract label governing both.

**Expected**: 14/14 = 100 — ceiling. New patterns are R7 discriminator candidates if live-run variance data supports promotion.

---

### Discriminator table

| Mechanism | V-01 | V-02 | V-03 | V-04 | V-05 | Gap |
|-----------|------|------|------|------|------|-----|
| C-21 inertia at NEXT STEP | YES | NO | YES | YES | YES | — |
| C-22 THREE-LAYER header (Branch A) | NO | YES | YES | YES | YES | — |
| Inertia at READINESS sentence | NO | NO | YES | NO | YES | R7 candidate |
| G-9 stall-cost contract label | NO | NO | NO | NO | YES | R7 candidate |
| Branch B own THREE-LAYER header | NO | NO | NO | NO | YES | R7 candidate |
| **Score under v6** | **13/14** | **13/14** | **14/14** | **14/14** | **14/14** | |

V-01 and V-02 discriminate C-21 vs C-22 in isolation. V-03 tests propagation risk. V-04 is the minimal golden. V-05 populates the R7 candidate pool.
