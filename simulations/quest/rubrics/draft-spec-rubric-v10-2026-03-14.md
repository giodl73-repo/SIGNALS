Here is the complete updated rubric:

---

# Rubric — `draft-spec` — v10

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 24 | 85 |
| **Total** | **32** | **175** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/24 * 85)
```

---

## What changed from v9 to v10

| | v9 | v10 |
|-|----|----|
| Version | v9 | v10 |
| Source rounds | R1–R8 | R1–R9 |
| Aspirational count | 21 | 24 |
| Total criteria | 29 | 32 |
| Composite formula denominator | 21 | 24 |

**Three new aspirational criteria from R9:**

---

### C-30 — Inertia gate token validates column-level R-ID population (depth)

The `[INERTIA-ANALYZED]` gate token extends its structural invalidity rule beyond table-presence checking to column-content checking: the token is explicitly declared invalid if any non-waived Elimination Path cell lacks a named R-ID. Rows whose corresponding requirement was waived in `[PM-COVERAGE-TABLE]` are exempted only when the cell carries an explicit `"R-ID WAIVED"` marker — absence of the marker is not an implicit exemption. A gate token invalidity rule that checks only for table presence (C-21 level) without checking R-ID population does not satisfy. Requires C-29. Upgrades C-21 in the inertia domain. Enables C-31.

Source signal: V-02 — "[INERTIA-ANALYZED] invalidity rule updated to check R-ID population."

---

### C-31 — Waiver propagation from PM-COVERAGE-TABLE to IG-REGISTER (depth)

Requirements that carry a C-03 waiver in `[PM-COVERAGE-TABLE]` generate corresponding `"R-ID WAIVED"` markers in the `[IG-REGISTER]` Elimination Path cells for every inertia row that would otherwise reference those requirements. The waiver propagation must be declared as a structural rule in the template — a behavioral note ("handle waivers appropriately") does not satisfy. The `[INERTIA-ANALYZED]` gate token invalidity rule (C-30) must explicitly exempt WAIVED-marked rows from the R-ID population check, closing the traceability chain: PM-COVERAGE-TABLE waiver → IG-REGISTER cell marker → gate token exemption. A template that carries `"R-ID WAIVED"` in cells but omits the gate-token exemption rule satisfies the propagation step but fails the chain closure. Requires C-29 and C-30.

Source signal: V-02 — "C-03 WAIVER rows carry 'R-ID WAIVED'."

---

### C-32 — AMPLIFIED Elimination Path dual sub-slot structural format (structure)

When a row's Risk Signal is AMPLIFIED, the Elimination Path cell is structured in the template as two explicitly labeled sub-slots — one for the risk dimension (e.g., `"Risk: [feasibility constraint or compliance gap]"`) and one for the requirement ID (e.g., `"R-ID: [R-XX from [PM-COVERAGE-TABLE]]"`) — pre-printed so that their independent population is structurally required. A prose instruction to "name both the risk dimension and R-ID" without pre-printed sub-slot labels does not satisfy. A combined prose format containing both elements in a single unlabeled statement does not satisfy. C-29 requires both elements — C-32 requires them as independently labeled structural slots. Upgrades C-29 at the structural format level — C-29 can pass without C-32.

Source signal: V-02 — "AMPLIFIED rows: risk dimension + R-ID both required" with two-field format; V-03's column-format approach demonstrated the structural-separation instinct even while failing C-29 on letter.

---

The three new criteria form a coherent sub-chain: C-29 (require R-IDs in cells) → C-30 (gate token enforces R-ID population) → C-31 (waivers propagate and are exempted). C-32 is an orthogonal structural upgrade to C-29's AMPLIFIED-row requirement. The max score stays at 175; the denominator in the aspirational formula moves from 21 to 24.
