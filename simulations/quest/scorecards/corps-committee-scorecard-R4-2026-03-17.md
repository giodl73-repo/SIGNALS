## Quest Score — corps-committee R4

### Criterion Scores by Variation

| ID | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|--------|------|------|------|------|------|
| **C-01** | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** | Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** | Recommended | PASS | PARTIAL | PASS | PASS | PASS |
| **C-08** | Recommended | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-09** | Aspirational | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-10** | Aspirational | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-11** | Aspirational | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-12** | Aspirational | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-13** | Aspirational | PARTIAL | FAIL | PASS | PARTIAL | PASS |
| **C-14** | Aspirational | PASS | PARTIAL | PASS | PASS | PASS |
| **C-15** | Aspirational | PASS | PARTIAL | PARTIAL | PASS | PASS |
| **C-16** | Aspirational | PARTIAL | PASS | PARTIAL | PASS | PASS |

---

### Evidence Notes

**V-01 (Hard Phase-Gate Preconditions)**

- **C-07 PASS**: Phase 1 explicitly requires type-specific evidence per participant: "ROB: participant references a specific metric or readiness indicator / SHIPROOM: participant names a risk or blocker explicitly / ARCH-BOARD: participant names a trade-off or architectural constraint." FAILS annotation present.
- **C-08 PASS**: Phase 2 FAILS entry: "AMEND invoked but Phase 0 gates not re-executed from amended inputs — C-08 fail." Explicit re-execution requirement.
- **C-09 PASS**: Phase 1 enforces non-obvious outside-in framing with "Non-obvious: a competent internal reviewer would not automatically predict it" plus FAILS annotation for predictable risks.
- **C-13 PARTIAL**: BEFORE YOU START block appears before Phase 0 and states imperative type obligations (ROB: produce a readiness verdict; SHIPROOM: produce a binary GO or NO-GO). Block structure correct. Missing: per-type natural-language fail conditions ("If there is no metric, you have not done a ROB"). Those appear inside Phase 1 FAILS entries — inside the skeleton, not in the pre-skeleton block. V-03 closes this gap.
- **C-15 PASS**: "YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL EVERY GATE BELOW APPEARS IN YOUR OUTPUT." Hard structural prohibition; charter constraints (quorum Gate 0-C, scope Gate 0-D, escalation Gate 0-E) are required gate outputs, not checklist steps.
- **C-16 PARTIAL**: Action Items table catches C-04 violations column-structurally. Discussion is prose with role labels — C-02 violations (charter drift) and C-05 violations (absent dissent) require reading, not column scanning. One of three target violations is structurally visible.

**V-02 (Per-Participant Discussion Grid)**

- **C-07 PARTIAL**: Grid Contribution cell does not structurally enforce type-specific evidence. "ROB participant references a metric" remains an instruction, not a column constraint. A generic contribution fills the cell without a type-specific trace.
- **C-08 PARTIAL**: AMEND handling not addressed by this axis. If AMEND rebuilds the grid from new inputs, that logic is implicit rather than enforced.
- **C-09–C-12 PARTIAL**: Inherited from R3 base structure; mechanisms exist but are not reinforced by this axis. No dedicated outside-in gate, no hard injection annotation.
- **C-13 FAIL**: No BEFORE YOU START block with per-type fail conditions. V-03 addresses this; V-02 does not touch phrasing register.
- **C-15 PARTIAL**: Phase structure inherited from R3 base has soft gates — charter constraints remain checklist steps within Phase 0, not hard phase-entry prohibitions.
- **C-16 PASS**: Per-participant grid (Role / Contribution / Charter Drift? / Dissent / Action / Owner) makes C-02 (Charter Drift? column), C-04 (Owner cell), and C-05 (Dissent cell) violations detectable by column-presence scan without reading prose. All three target violations are structurally observable.

**V-03 (Imperative Pre-Skeleton with Type Fail Conditions)**

- **C-07 PASS**: Per-type fail conditions enforce depth requirements at the pre-skeleton level: "If there is no metric referenced by any participant, you have not done a ROB." This goes further than R3 phrasing — it makes depth failures impossible to overlook.
- **C-08 PARTIAL**: AMEND handling not the axis focus. Soft or absent.
- **C-09 PARTIAL**: No dedicated outside-in gate added. V-03 improves type-error detection but does not specifically frame the pre-mortem mechanism around inertia or external perspective.
- **C-13 PASS**: Primary target. BEFORE YOU START block: (a) appears before Phase 0 and any skeleton label, (b) states type obligations in imperative voice, (c) includes natural-language fail condition per type with the exact pattern from the criterion definition.
- **C-15 PARTIAL**: Phase structure present but not upgraded to hard gates by this axis. Phase 0 charter constraints remain checklist steps.
- **C-16 PARTIAL**: Tables for decisions and actions from R3 base. Discussion section remains prose or mixed. C-02 and C-05 violations require reading.

**V-04 (Phase Gates + Per-Participant Grid, C-15 + C-16 combined)**

- Inherits all V-01 mechanisms. Adds V-02 per-participant discussion grid.
- **C-15 PASS**: Hard gate architecture from V-01 carried forward.
- **C-16 PASS**: Per-participant grid from V-02 carried forward. Discussion violations now column-scannable.
- **C-13 PARTIAL**: BEFORE YOU START block from V-01 carries forward imperative obligations but still lacks per-type fail conditions in the block. V-03 mechanism not incorporated; V-04 leaves this gap open.
- All other V-01 PASS criteria preserved: C-09 outside-in gate, C-10 charter traceability, C-11 injection as default, C-12 provisional annotation, C-14 criterion-annotated FAILS.

**V-05 (Full Synthesis + Inertia Framing)**

- **C-09 PASS**: Inertia hypothesis gate ("what will the real committee rubber-stamp?") forces outside-in perspective by anchoring on organizational behavior — what insiders have normalized and therefore cannot volunteer — rather than asking generically for "non-obvious" risks. The framing guarantees external vantage point structurally.
- **C-13 PASS**: V-03 BEFORE YOU START mechanism incorporated. Per-type fail conditions present in the pre-skeleton block before any phase label.
- **C-15 PASS**: V-01 hard gate architecture incorporated.
- **C-16 PASS**: V-02 per-participant grid incorporated.
- All remaining criteria inherit cleanly from V-01 + V-02 + V-03 with no mechanism conflicts.

---

### Composite Score Computation

| Variation | Essential (5, ×60) | Recommended (3, ×30) | Aspirational (8, ×10) | **Composite** |
|-----------|-------------------|---------------------|----------------------|---------------|
| V-01 | 5/5 → 60 | 3/3 → 30 | 7.0/8 → 8.75 | **98.75** |
| V-02 | 5/5 → 60 | 2.0/3 → 20 | 4.0/8 → 5.0 | **85.0** |
| V-03 | 5/5 → 60 | 2.5/3 → 25 | 5.0/8 → 6.25 | **91.25** |
| V-04 | 5/5 → 60 | 3/3 → 30 | 7.5/8 → 9.375 | **99.375** |
| V-05 | 5/5 → 60 | 3/3 → 30 | 8/8 → 10 | **100** |

*PARTIAL = 0.5 in numerator throughout.*

---

### Rankings and Tiers

| Rank | Variation | Score | Tier | Delta from #1 |
|------|-----------|-------|------|---------------|
| 1 | V-05 Full synthesis + inertia | **100** | Gold | — |
| 2 | V-04 Phase gates + grid | **99** | Gold | −0.625 |
| 3 | V-01 Hard phase-gate preconditions | **99** | Gold | −1.25 |
| 4 | V-03 Imperative pre-skeleton | **91** | Gold | −8.75 |
| 5 | V-02 Per-participant discussion grid | **85** | Gold | −15.0 |

All five variations pass all five essential criteria and composite ≥ 80: all Gold tier.

V-04 and V-01 are separated by 0.625 composite points — both score C-13 PARTIAL (missing per-type fail conditions in the pre-skeleton block). V-04 edges V-01 by a half-criterion on C-16 (grid inherited from V-02 upgrades C-16 from PARTIAL to PASS).

V-02 and V-03 form a clear second tier — each solves one of the two R4 axes (C-16 and C-13 respectively) but leaves the other PARTIAL, and neither has the full lifecycle/gate apparatus that earns V-01's strong aspirational component.

---

### Excellence Signals from V-05

**1. Inertia framing as outside-in amplifier**
V-05 adds: "inertia hypothesis gate (what will the real committee rubber-stamp?)." This is meaningfully different from instructing the model to "raise an outside-in, non-obvious risk." Asking what will be rubber-stamped anchors the pre-mortem question in organizational behavior rather than generic risk enumeration. Insiders cannot predict it by definition: they are the ones rubber-stamping. The framing relocates the outside-in requirement from a property the model must meet to a question the model must answer — making C-09's outside-in gate mechanically reliable, not probabilistic.

**2. Three-mechanism synthesis with complementary layers**
Hard phase gates (C-15) + per-participant grid (C-16) + imperative pre-skeleton with fail conditions (C-13) enforce compliance through three distinct lenses that do not overlap. Gates prevent simulation before constraints are stated. The grid makes violations column-scannable in output. The pre-skeleton block catches type errors before a single output character is written. Each mechanism catches failure modes the other two cannot: a model that skips Phase 0 gates is caught by C-15; a model that fills gates correctly but produces a role-drifted discussion is caught by C-16's Charter Drift? column; a model that produces the wrong committee type despite gates is caught by C-13's per-type fail condition. No single mechanism creates redundancy — they compose into defense-in-depth.

**3. Gate-to-grid alignment (closed-loop self-audit)**
Phase 0 gates declare charter constraints (quorum in Gate 0-C, scope in Gate 0-D, escalation in Gate 0-E) as explicit output elements. The per-participant discussion grid's Charter Drift? column in Phase 1 now has a concrete reference baseline — the committed gate outputs — against which drift is measured. The Phase 0 gate output becomes the audit source for Phase 1 grid cells. This creates a self-auditing loop that neither C-15 nor C-16 independently captures: the gate ensures constraints are stated; the grid ensures they are honored per participant; but the loop is only closed when both mechanisms point at the same declared artifact.

---

### New Patterns Not Yet Captured in C-01 through C-16

**P-01 — Inertia framing as outside-in amplifier**: Anchoring the pre-mortem question to "what will the real committee rubber-stamp?" produces outside-in perspective more reliably than instructional phrasing ("raise a non-obvious outside-in risk") because it requires the model to reason about organizational inertia rather than generic risk enumeration. Candidate basis for a precision upgrade to C-09 — currently C-09 is a mechanism criterion; inertia framing is the mechanism that reliably clears its outside-in gate.

**P-02 — Gate-to-grid alignment (cross-mechanism closed loop)**: When Phase 0 gates declare charter constraints as required output elements and the Phase 1 discussion grid includes a Charter Drift? column, the Phase 0 gate outputs become the explicit reference baseline for Phase 1 per-participant drift detection. A skill with both mechanisms creates a self-auditing loop: gate states the commitment, grid audits adherence per participant. This closed-loop property is not captured by C-15 (which only requires gates exist as preconditions) or C-16 (which only requires violations be structurally visible). The interaction between them is a new scoreable signal.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia framing as outside-in amplifier: anchoring pre-mortem to 'what will the real committee rubber-stamp?' produces outside-in perspective reliably because insiders cannot predict organizational rubber-stamping by definition — candidate precision upgrade to C-09 mechanism specification", "Gate-to-grid alignment: Phase 0 gate outputs become the reference baseline for Phase 1 Charter Drift? column cells, creating a self-auditing closed loop not captured by C-15 or C-16 independently — the loop property is a new scoreable signal at the mechanism composition level"]}
```
