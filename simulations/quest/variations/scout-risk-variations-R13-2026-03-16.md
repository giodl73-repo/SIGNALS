Written to `simulations/quest/golden/scout-risk-variate-R13-2026-03-17.md`.

---

## Scout-Risk R13 — V-01 through V-05

**Baseline**: R11 V-05 scores ~142/148 on v12 rubric. Three gaps:
- C-35 PARTIAL — Phase 0a exists but never explicitly named as a "role-activation gate" blocking downstream phases
- C-36 FAIL — No HIGH-seed step; Phase 2b operates as gap-discovery rather than seed-confirmation
- C-37 FAIL — Table 2 column schema defined inline in Phase 2; no pre-population field list declared before Table 1 (inertia row) is written

---

### V-01 — C-35 only (Lifecycle emphasis: Phase 0a as role-activation gate)
**Axis**: Adds explicit precondition contract language to Phase 0a header and AMEND check — names Phase 0 through Phase 4 as role-activating phases blocked until Phase 0a confirms scope. Minimal structural change; tests whether phrasing alone closes C-35.
**Expected**: ~144/148 (C-35 PASS; C-36, C-37 unchanged)

### V-02 — C-36 only (Role sequence: HIGH-seed sub-phase)
**Axis**: Inserts Phase 1b between Phase 1 (inertia) and Phase 2 (expansion). Phase 1b seeds exactly one HIGH row per active dimension before any MEDIUM/LOW row exists. Phase 2 expands around seeds. Phase 2b shifts from gap-discovery to seed-confirmation framing.
**Expected**: ~144/148 (C-36 PASS; C-35, C-37 unchanged)

### V-03 — C-37 only (Output format: Phase 0b schema pre-declaration)
**Axis**: Inserts Phase 0b between Phase 0 (taxonomy) and Phase 1 (inertia). Declares the Table 2 base schema as a named field list and defines Table 1 as a named extension to that schema (substituting Likelihood with three inertia-specific fields). Both Table 1 and Table 2 explicitly reference Phase 0b — field parity becomes a structural precondition rather than a retrospective check.
**Expected**: ~144/148 (C-37 PASS; C-35, C-36 unchanged)

### V-04 — C-35 + C-36 (Lifecycle emphasis + Role sequence)
**Axis**: Combines V-01's explicit role-activation gate with V-02's Phase 1b HIGH-seed. Key interaction: Phase 0a confirmed scope feeds directly into Phase 1b's seed dimension set — the seed step is intrinsically AMEND-aware without additional wiring.
**Expected**: ~146/148 (C-35 + C-36 PASS; C-37 unchanged)

### V-05 — C-35 + C-36 + C-37 (Full combination)
**Axis**: All three preconditions compose in sequence — scope confirmed (Phase 0a) → schema declared (Phase 0b) → HIGH seeds placed (Phase 1b) → expansion begins (Phase 2). Each precondition is a closed output; every downstream phase inherits all three. AMEND check updated to name Phase 0b as a blocked phase, making the full precondition chain explicit.
**Expected**: 148/148
