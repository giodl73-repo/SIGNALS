Written to `simulations/quest/golden/crew-review-variate-R20-2026-03-17.md`.

---

# org-review -- Variate R20 (rubric v11)

**R20 design target**: All R19 variants predicted 225/225. R20 investigates three adversarial failure modes that survive R19's structural protections:

| Criterion | R19 approach | R20 failure mode addressed |
|-----------|-------------|---------------------------|
| **C-33** | PRE-REGISTRATION step + TYPED FIELD | Silent re-derivation of Applicability at step 10 ("inherits" in text but recalculates in practice) |
| **C-34** | Gap-check as numbered step + MANDATORY OPERATION | Domain list derived from reviewer findings instead of from SCOPE DECLARATION |
| **C-35** | PRIMACY DEVIATION CASE | NH table back-filled after prose intent formed (format satisfied, construction order reversed) |

---

## Variation axes

### V-01 -- C-33 Verbatim Inheritance Lock (single axis)
**Axis**: APPLICABILITY INHERITANCE PROTOCOL added to preamble. LENS COVERAGE TABLE Applicability column is a **verbatim-copy** operation from LENS APPLICABILITY PRE-REGISTRATION -- not re-derived at table-population time. Deviations require an explicit `INHERITANCE-DEVIATION-ALERT` (analogous to §7 VERBATIM ASSEMBLY PROHIBITION for gate ledger rows). Pre-registered value governs unless BRACKET CLOSING explicitly overrides.

**C-34** via numbered step 11. **C-35** via PRIMACY DEVIATION CASE. Predicted 225/225.

### V-02 -- C-34 Scope-Declaration Domain Anchor (single axis)
**Axis**: SCOPE DECLARATION (step 1) annotates every IN-SCOPE surface with a `| Surface | Domain | ... |` tag at declaration time. DOMAIN COVERAGE GAP-CHECK reads its input domain set from this annotated table only -- no post-review domain inference. Domain list is committed at step 1 and read-only for gap-check purposes. UNDECLARED-DOMAIN findings flagged in CROSS-ROLE SIGNALS.

**C-33** via PRE-REGISTRATION. **C-35** via PRIMACY DEVIATION CASE. Predicted 225/225.

### V-03 -- C-35 Two-Phase NH Table Construction (single axis)
**Axis**: NH DIMENSION COMPARISON TABLE uses a mandatory two-phase protocol. **Phase 1 (DIMENSION REGISTRATION)**: challenger commits dimension names, measurement basis, and scale before assigning any scores. **Phase 2 (VALUE ASSIGNMENT)**: fills A/B/C values and computes deltas. Phase 1 is immutable once Phase 2 begins -- the challenger cannot redefine what is measured to produce a desired score pattern. Prose follows Phase 2. CONSTRUCTION DEVIATION CASE for Phase 1 revision requests.

**C-33** via PRE-REGISTRATION. **C-34** via numbered step 11. Predicted 225/225.

### V-04 -- C-33 + C-34 (two-axis)
Combines V-01's APPLICABILITY INHERITANCE PROTOCOL with V-02's scope-declaration domain annotation. Both C-33 and C-34 enforced via chain-of-custody protocols rather than behavioral text alone. The two protocols are orthogonal (§11 governs Applicability; §9 governs domain source). **C-35** via PRIMACY DEVIATION CASE. Predicted 225/225.

### V-05 -- C-33 + C-34 + C-35 (three-axis)
All three: APPLICABILITY INHERITANCE PROTOCOL (V-01) + scope-declaration domain annotation (V-02) + two-phase NH table construction (V-03). Maximum chain-of-custody closure for all three new criteria simultaneously. Protocols are orthogonal; no interaction points. Predicted 225/225.

---

**Key structural additions in R20 vs R19:**

| Addition | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| APPLICABILITY INHERITANCE PROTOCOL (§10/§11) | yes | -- | -- | yes | yes |
| Scope domain annotation at step 1 (§9) | -- | yes | -- | yes | yes |
| Two-phase NH table construction (§3 Phase 1/2) | -- | -- | yes | -- | yes |
| INHERITANCE-DEVIATION-ALERT syntax | yes | -- | -- | yes | yes |
| UNDECLARED-DOMAIN flag | -- | yes | -- | yes | yes |
| NH-CONSTRUCTION-DEVIATION flag | -- | -- | yes | -- | yes |
