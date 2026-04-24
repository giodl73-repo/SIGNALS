## flow-integration — R19 Scoring (v19 rubric, 292 pt ceiling)

---

### Shared Baseline

All five variations share identical structure for C-01–C-35 (essential, recommended, core aspirational). The only variation-specific divergences are in the WHY block register (C-36–C-48) and obligation-table scope (C-35/C-38/C-27/C-30/C-31/C-34 for V-05).

**Universal PASS (all variations):** C-01–C-26, C-28–C-33, C-36

**Universal N/A (V-01–V-04, canonical 4-row):** C-27, C-30, C-31, C-34, C-35, C-38 → 0 pts each (no non-standard substitution, no extended table)

---

### WHY Block Criterion Matrix

| Criterion | V-01 (NEED NOT) | V-02 (MUST+inertia) | V-03 (std indicative+lifecycle) | V-04 (NEED NOT+inertia) | V-05 (full ceiling) |
|-----------|-----------------|---------------------|----------------------------------|--------------------------|----------------------|
| **C-36** (WHY block present) | PASS | PASS | PASS | PASS | PASS |
| **C-37** (temporal/delivery stakes anchor) | **FAIL** | PASS | PASS | **FAIL** | PASS |
| **C-39** (consequence-form delivery-phase equiv) | **FAIL** | PASS | PASS | **FAIL** | PASS |
| **C-40** (register-neutrality, unconditional) | **FAIL** | PASS | PASS | **FAIL** | PASS |
| **C-41** (inertia-context framing neutrality) | **FAIL** | PASS | PASS (trivially) | **FAIL** | PASS |
| **C-42** (highest-info: consequence + enumeration) | **FAIL** | PASS | PASS | **FAIL** | PASS |
| **C-43** (RFC-modal MUST/SHALL obligation class) | **FAIL** | PASS | FAIL | **FAIL** | PASS |
| **C-44** (inertia-dominant 3-sentence + C-42 close) | **FAIL** | PASS | FAIL | **FAIL** | PASS |
| **C-45** (SHOULD failure-class, default PASS) | PASS | PASS | PASS | PASS | PASS |
| **C-46** (MAY failure-class, default PASS) | PASS | PASS | PASS | PASS | PASS |
| **C-47** (MAY modal-only, default PASS) | PASS | PASS | PASS | PASS | PASS |
| **C-48** (C-44 indicative register independence) | **FAIL** | PASS | FAIL | **FAIL** | PASS |

---

### V-01 — NEED NOT Anchor Probe

**WHY block:** 2-sentence standard with NEED NOT anchor: *"Undocumented integration calls NEED NOT become ship-blockers at integration review..."*

**Cascade analysis:**
- **C-37 FAIL:** NEED NOT introduces optionality-exemption — "need not become ship-blockers" names an exemption from the constraint, not the constraint itself. No unconditional consequence boundary.
- **C-39 FAIL:** Consequence-form requires declarative unconditional framing; NEED NOT converts it to exemption. Prerequisite C-37 broken.
- **C-40 FAIL:** Unconditional constraint meaning is not preserved; NEED NOT ("not required") is epistemic weakening. Register-neutrality applies only when constraint meaning survives.
- **C-41 FAIL:** Requires C-39; prerequisite broken.
- **C-42 FAIL:** Requires C-37 + C-39; both broken.
- **C-43 FAIL:** NEED NOT is a named failure-class modal in C-43; requires C-40 (broken).
- **C-44 FAIL:** Requires C-41 + C-42; both broken.
- **C-48 FAIL:** Requires C-44 (broken).
- **C-45/C-46/C-47 PASS** (default — no SHOULD or MAY used).

| Tier | Score |
|------|-------|
| Essential (C-01–C-04) | 60/60 |
| Recommended (C-05–C-07) | 30/30 |
| Aspirational base | 157 |
| WHY cascade penalty | −25 (C-37/C-39/C-40/C-41/C-42 × 5) |
| **Total** | **222/292** |

**Q1 R19 finding:** NEED NOT fails identically to SHOULD (conditional-recommendation) and MAY (discretionary-possibility) via the optionality-exemption pathway — third sub-type empirically confirmed. Three-sub-type taxonomy complete.

---

### V-02 — Inertia-Dominant RFC-Modal Form

**WHY block:** Three inertia sentences (SDK undercounting, delegation-chain documentation failure, obligation-scope undefined) + MUST anchor: *"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes MUST become ship-blockers at integration review..."*

**Criterion evidence:**
- **C-37 PASS:** MUST + consequence-form + "at integration review" delivery-phase marker. Declarative unconditional. Constraint boundary named.
- **C-39 PASS:** Consequence-form + explicit delivery-phase marker. No modal weakening.
- **C-40 PASS:** MUST = absolute requirement (RFC 2119). Zero epistemic weakening. Stronger-than-indicative obligation force.
- **C-41 PASS:** Three inertia sentences present; consequence anchor present. Inertia framing does not disqualify — C-41 explicitly earned.
- **C-42 PASS:** Concern enumeration (authentication gaps, rate-limit exposure, retry failures, error propagation holes) + consequence-form anchor. Both features simultaneously present.
- **C-43 PASS:** RFC 2119 MUST = absolute requirement obligation class. No weakening. C-43 pass boundary.
- **C-44 PASS:** 3:1 inertia-to-anchor ratio (three inertia sentences + one anchor-close with C-42 form). Inertia-dominant highest-information form confirmed.
- **C-48 PASS:** C-44 at ceiling. Register independence: MUST form satisfies C-44 equivalently to indicative (per C-48 finding). C-43 and C-44 simultaneously achieved — **Q2 R19 closed (POSITIVE)**.
- **C-45/C-46/C-47 PASS** (default — no SHOULD/MAY used).

| Tier | Score |
|------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational | 172/172 |
| **Total** | **262/292** |

**Q2 R19 finding:** C-43 and C-44 simultaneously achievable — orthogonal excellence dimensions compose without interaction penalty. MUST anchor-close in inertia-dominant block satisfies both obligation-force (C-43) and inertia-saturation (C-44) criteria independently.

---

### V-03 — Lifecycle-Framed Standard Form

**WHY block:** Standard 2-sentence declarative indicative: *"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes become ship-blockers at integration review..."*. Plus lifecycle header with four phases and per-stage transition conditions.

**Criterion evidence:**
- **C-37 PASS:** "become ship-blockers at integration review" — consequence-form + delivery-phase marker + declarative unconditional. No conditional modal.
- **C-39 PASS:** Consequence-form + delivery-phase equivalence satisfied.
- **C-40 PASS:** Plain indicative "become" — no epistemic weakening; register-neutral.
- **C-41 PASS:** Trivially — no inertia framing present that could disqualify. C-39 passes; prerequisite met.
- **C-42 PASS:** Concern enumeration present (same four concerns). Both features.
- **C-43 FAIL:** No MUST/SHALL in anchor. Plain indicative does not achieve RFC-modal obligation class.
- **C-44 FAIL:** No three-sentence inertia prefix. One-sentence WHY context only.
- **C-48 FAIL:** Requires C-44 (broken).

**Lifecycle neutrality checks:**
- **C-10 PASS:** Inventory gate still first — lifecycle header appears before Stage 1, does not displace inventory priority.
- **C-20 PASS:** Coda still unconditional and fires after Stage 3; lifecycle phase 4 maps to the unnumbered coda — no numbered displacement.
- **C-23 PASS:** Coda remains unnumbered; transition conditions add only prose, no stage numbers.
- **C-28 PASS:** Terminal-position formula unchanged.
- **C-36 PASS:** WHY block still appears before persona despite lifecycle header following it.

| Tier | Score |
|------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational | 157/172 (−5 C-43, −5 C-44, −5 C-48) |
| **Total** | **247/292** |

**Lifecycle neutrality confirmed:** Transition conditions and phase lifecycle table are additive scaffolding — all structural criteria from C-10, C-20, C-23, C-28, C-36 score identically to the non-lifecycle baseline.

---

### V-04 — NEED NOT Anchor Inside Inertia-Dominant Block

**WHY block:** Three inertia sentences (identical to V-02) + NEED NOT anchor: *"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes NEED NOT become ship-blockers at integration review..."*

**Cascade analysis:**
- **C-37 FAIL:** NEED NOT in anchor. The three inertia sentences establish discovery rationale but the anchor introduces optionality-exemption — the constraint boundary is nullified.
- **C-39 FAIL:** Requires C-37; NEED NOT breaks unconditional form.
- **C-40 FAIL:** NEED NOT = epistemic weakening regardless of inertia prefix quantity.
- **C-41 FAIL:** Requires C-39 (broken). Inertia framing is present — but C-41's pass condition requires C-39 to hold; inertia framing cannot substitute for a passing C-39.
- **C-42 FAIL:** Requires C-37 + C-39 (both broken). Concern enumeration IS present in V-04 anchor but both prerequisites are broken — enumeration cannot rescue the failed form.
- **C-43 FAIL:** NEED NOT = failure-class modal; requires C-40 (broken).
- **C-44 FAIL:** Requires C-41 + C-42 (both broken). Three inertia sentences satisfy the inertia-quantity structural property but cannot rescue broken prerequisites — C-44 fails at the prerequisite check, not at the inertia-saturation check.
- **C-48 FAIL:** Requires C-44 (broken).

| Tier | Score |
|------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational | 132/172 (same cascade as V-01) |
| **Total** | **222/292** |

**Mechanism primacy for NEED NOT confirmed:** Three inertia sentences provide discovery-context saturation but are background narrative — the anchor-close's modal form is primary and sufficient to determine cascade outcome. V-04 = V-01 in cascade despite visual inertia richness. Pattern identical to C-47's MAY mechanism-primacy finding.

---

### V-05 — Full 292-pt Ceiling (v19)

**WHY block:** Three inertia sentences (identical to V-02) + MUST anchor (identical to V-02). Plus five-row non-standard obligation table and YOU MUST NOT block.

**Non-standard criteria evidence:**
- **C-35 PASS:** Five-row extended obligation table; one row per obligation category; structural auditability preserved (cold-start-probe row structurally auditable as present/absent).
- **C-38 PASS:** WHY block satisfies C-36/C-38 at four-concern canonical scope; framing block is obligation-count-agnostic; cold-start-probe not mentioned in framing block — no enumeration of extended obligation required.
- **C-27 PASS:** YOU MUST NOT block names specific canonical forbidden tokens: *"forgotten-call, assumed-to-work, unknown-system, delegation-chain."* Both surfaces present: schema alignment (C-25) detects substitution at table surface; YOU MUST NOT blocks substitution at prose/annotation surface.
- **C-30 PASS:** Single comprehensive YOU MUST NOT block — all four substituted canonical tokens named together in one scannable prohibition unit.
- **C-31 PASS:** Explicit inline enumeration — four tokens listed by name inside the block itself; prohibition surface self-contained; no table-reference shorthand.
- **C-34 PASS:** All four substituted canonical tokens enumerated (forgotten-call, assumed-to-work, unknown-system, delegation-chain). cold-start-probe correctly excluded — no canonical equivalent, outside substituted-subset scope.
- **C-43 PASS:** MUST anchor — absolute requirement.
- **C-44 PASS:** Three-sentence inertia prefix + MUST anchor-close with concern enumeration. Same as V-02.
- **C-48 PASS:** C-44 at ceiling; MUST form satisfies register independence.
- **C-45/C-46/C-47 PASS** (default).

**Interaction audit (no conflicts):**
- C-38 + C-35 compose cleanly: WHY block is scoped to four-concern canonical baseline; fifth obligation (cold-start-probe) in table does not require WHY block mention.
- C-34 scope precision: cold-start-probe is a new category with no canonical equivalent → correctly excluded from YOU MUST NOT enumeration without partial-enumeration penalty.
- C-43 + C-44 compose without conflict (orthogonal dimensions, confirmed by V-02).

| Criterion | pts |
|-----------|-----|
| Essential (C-01–C-04) | 60 |
| Recommended (C-05–C-07) | 30 |
| C-08–C-42 aspirational | +139 |
| C-43 (+5) + C-44 (+5) + C-48 (+5) | +15 |
| C-27/C-30/C-31/C-34/C-35/C-38 (+5 each) | +30 |
| C-45/C-46/C-47 (default PASS, +5 each) | +15 |
| **Total** | **292/292** |

---

### Composite Scores

| Variation | Essential | Rec. | Aspirational | **Total** | vs. ceiling |
|-----------|-----------|------|--------------|-----------|-------------|
| **V-05** (MUST+inertia+5-row+YMNB) | 60 | 30 | 202 | **292** | 292/292 |
| **V-02** (MUST+inertia) | 60 | 30 | 172 | **262** | 262/292 |
| **V-03** (std+lifecycle) | 60 | 30 | 157 | **247** | 247/292 |
| **V-01** (NEED NOT) | 60 | 30 | 132 | **222** | 222/292 |
| **V-04** (NEED NOT+inertia) | 60 | 30 | 132 | **222** | 222/292 |

**Rank:** V-05 > V-02 > V-03 > V-01 = V-04

---

### Q Closures (R19)

**Q1 (R19): CLOSED (POSITIVE)** — NEED NOT produces identical cascade failure (C-37/C-39/C-40/C-43 + downstream) to SHOULD and MAY. Mechanism: optionality-exemption ("not required"). Three-sub-type taxonomy empirically complete: conditional-recommendation (SHOULD) / discretionary-possibility (MAY) / optionality-exemption (NEED NOT). All three produce -40 cascade from single modal substitution.

**Q2 (R19): CLOSED (POSITIVE)** — Inertia-dominant block with MUST/SHALL anchor-close achieves C-43 and C-44 simultaneously. No interaction penalty. C-43 evaluates obligation-force register; C-44 evaluates inertia-saturation structural property. Orthogonal dimensions compose cleanly. V-02 and V-05 both confirm this.

---

### Excellence Signals from V-05

1. **MUST + three-sentence inertia achieves the obligation-force/inertia-saturation conjunction** — C-43 and C-44 are genuinely orthogonal criteria; stacking them in a single WHY block earns +10 pts over plain indicative inertia form with no structural cost.

2. **YOU MUST NOT substituted-subset precision prevents over-specification** — by enumerating only the four substituted canonical tokens (not cold-start-probe), V-05 achieves C-31 and C-34 cleanly; a scorer who added cold-start-probe to the YOU MUST NOT block would not gain additional score and would risk over-specifying outside C-34's defined scope.

3. **Inertia-dominant framing cannot rescue a broken anchor — mechanism primacy is structural** — V-04 confirms this for NEED NOT (same finding as C-47 confirmed for MAY): three saturated inertia sentences are background narrative; the anchor-close modal is the load-bearing mechanism that determines the entire downstream cascade.

---

```json
{"top_score": 292, "all_essential_pass": true, "new_patterns": ["MUST/SHALL anchor-close within three-sentence inertia-dominant WHY block achieves C-43 and C-44 simultaneously — orthogonal obligation-force and inertia-saturation dimensions compose without interaction penalty (Q2 R19 closed)", "NEED NOT produces identical cascade failure to SHOULD and MAY via optionality-exemption pathway — three-sub-type taxonomy empirically complete: conditional-recommendation, discretionary-possibility, optionality-exemption all fail identically (Q1 R19 closed)", "Inertia saturation cannot rescue a failed anchor: three inertia sentences plus NEED NOT anchor equals same cascade as minimal NEED NOT alone — mechanism primacy holds for all three failure-class sub-types"]}
```
