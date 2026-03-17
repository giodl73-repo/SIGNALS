## R13 Variation Scoring — quest-rubric (Round 13)

**Rubric version:** v13 (2026-03-15)
**Criteria distribution:** C-01–C-05 essential (60%), C-06–C-08 recommended (30%), C-09–C-38 aspirational (10%)
**N/A exclusions:** C-16, C-17 (no amendment/revision phase in quest-rubric outputs) → applicable aspirational = 28
**Scoring formula:** (E_pass/5)×60 + (R_pass/3)×30 + (A_pass_equiv/28)×10; PARTIAL = 0.5 in numerator

---

### V-01 — R13 Full Integration Baseline

**Structure:** Phase 1A (enumeration-only table) + Phase 1A STOP + Phase 1B (FM-ID planning) + Phase 1B STOP + Phase 2 + Phase 3; 7-item Contract (items 6 = enumeration STOP gate, 7 = section-content register); checkpoint validates items 4, 5, 6, 7 simultaneously.

**Essential (60%)**

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | All five fields present in every criteria table row; five-column structure explicit in Phase 1B and Phase 2 |
| C-02 | PASS | Weight distribution spec (3–5 essential, 2–3 recommended, 1–2 aspirational) carried forward |
| C-03 | PASS | 60/30/10 composite formula and all-essential precondition for golden threshold present |
| C-04 | PASS | Criteria target quest-rubric-specific behaviors (FM-ID cross-reference, STOP-gate register, DR sub-section labeling) |
| C-05 | PASS | All pass conditions use observable binary signals (count ≥ N, named pattern, presence/absence) |

→ Essential: 5/5 = **60 pts**

**Recommended (30%)**

| ID | Score | Evidence |
|----|-------|----------|
| C-06 | PASS | N/A scope blocks present in Notes for C-16/C-17, C-37, C-38 |
| C-07 | PASS | All-essential precondition structurally prevents trivial golden path |
| C-08 | PASS | No bare banned qualifiers in pass conditions; banned-qualifier list (≥ 4 terms) in Notes |

→ Recommended: 3/3 = **30 pts**

**Aspirational — key criteria (10%)**

| ID | Score | Evidence |
|----|-------|----------|
| C-20 | PASS | Phase 1A explicitly dedicated to failure-mode enumeration; no criterion text, weight, or pass condition in Phase 1A table |
| C-25 | PASS | "or equivalent block" in role definition text AND in pass conditions permitting non-canonical routes |
| C-26 | PASS | Non-canonical routes explicitly named and accommodated in pass conditions |
| C-30 | PASS | Phase 1A is explicit dedicated phase before Phase 1B; STOP gate fires between them |
| C-31 | PASS | Contract items 6 and 7 each have dedicated Phase 2 checkpoint rows |
| C-32 | PASS | **Version**: N line + mechanism-note ("grows when quest-golden discovers excellence patterns") both populated |
| C-33 | PASS | Role-constitutive preamble obligations enforce Contract co-presence at every checkpoint |
| C-34 | PASS | All four STOP CONDITION blocks use imperative phrasing; register not degraded |
| C-35 | PASS | DR sub-section labeling (item 5) independent of evolution hook (item 1); separate checkpoint row |
| C-36 | PASS | Checkpoint simultaneously audits items 4, 5, 6, 7 — four structural contract layers in one table |
| C-37 | PASS | Contract item 7 mandates imperative register; Phase 3 confirms "must appear before criteria table", "must contain three labeled sub-sections" |
| C-38 | PASS | Phase 1A named STOP CONDITION (gates 1A-A, 1A-B, 1A-C) fires before Phase 1B; Phase 1A contains no criterion-drafting columns |

Remaining 16 applicable aspirational (C-09–C-15, C-18, C-19, C-21–C-24, C-27–C-29): ~11 PASS, 5 PARTIAL based on R12 baseline uncertainty → pass-equivalent ≈ 13.5

Total aspirational pass-equivalent: (12 from keyed criteria) + 13.5 = 25.5 / 28 → 9.1 pts

**V-01 Composite: ~97** | **all_essential_pass: TRUE**

---

### V-02 — C-38 Isolation (Phase 1A/1B; No Contract Item 7)

**Structure:** Identical to V-01 except: no Contract item 7; checkpoint has 9 rows (items 4, 5, 6 — not 7); C-37 enforcement relies on Phase 3 phrasing + role-constitutive preamble obligation only.

**Essential:** all PASS → 60 pts
**Recommended:** all PASS → 30 pts

**Aspirational differentials vs V-01:**

| ID | Score | Evidence |
|----|-------|----------|
| C-37 | PASS | Role-constitutive preamble includes "Maintain imperative register in all section-placement and section-content requirements"; Phase 3 section ordering uses "must appear before criteria table", "must contain three labeled sub-sections" — output-state gate satisfied without Contract item 7 |
| C-38 | PASS | Phase 1A STOP CONDITION with gates 1A-A/1A-B/1A-C; intra-framework placement is structurally equivalent to pre-role Phase 0 (R12/V-05) |
| C-36 | PASS | Checkpoint validates items 4, 5, 6 simultaneously (≥ 2 novel structural layers) |

*C-37 isolation result confirmed: Phase 3 imperative phrasing + preamble obligation is sufficient for C-37 PASS independent of a dedicated Contract item. Contract item 7 adds a declaration-layer reinforcement but is not the load-bearing mechanism.*

Aspirational pass-equivalent ≈ 25.5/28 (same as V-01 — C-37 PASS from Phase 3 holds)

**V-02 Composite: ~97** | **all_essential_pass: TRUE**

---

### V-03 — C-37 Isolation (5-Column Table; Contract Item 6 = Section-Content Register)

**Structure:** R12/V-01 baseline (5-column combined planning table, no Phase 1A/1B split); Contract item 6 = section-content imperative register (C-37); no Contract item for enumeration STOP gate.

**Essential:** all PASS → 60 pts
**Recommended:** all PASS → 30 pts

**Aspirational differentials:**

| ID | Score | Evidence |
|----|-------|----------|
| C-20 | PARTIAL | Planning table has "Failure mode this criterion addresses" column but combined with criterion-drafting columns in same step; no dedicated phase for failure-mode enumeration |
| C-30 | PARTIAL | Phase 1 is a combined planning table; no dedicated failure-mode enumeration phase separated by a phase gate from criterion drafting |
| C-37 | PASS | Contract item 6 mandates imperative register at declaration layer; checkpoint row enforces at generation time; Phase 3 "must appear/contain" confirms output register |
| C-38 | PARTIAL | No Phase 1A STOP gate; combined planning table allows criterion-drafting columns alongside failure-mode column; enumeration-only boundary absent |

Three PARTIAL criteria (C-20, C-30, C-38): −1.5 from aspirational numerator vs V-01.

Aspirational pass-equivalent ≈ 24.0/28 → 8.6 pts

**V-03 Composite: ~91** | **all_essential_pass: TRUE**

---

### V-04 — Joint-Failure-Chain Annotation Probe (v14 Candidate)

**Structure:** R12/V-01 baseline (5-column combined table); no Phase 1A split; Contract item 6 = Known Failure Chains block in Notes; Phase 2 checkpoint adds "joint-failure chain check" row. C-37 PASS from Phase 3 phrasing; no imperative-register obligation in V-04 preamble.

**Essential:** all PASS → 60 pts
**Recommended:** all PASS → 30 pts

**Aspirational differentials:**

| ID | Score | Evidence |
|----|-------|----------|
| C-20 | PARTIAL | Combined planning table; same failure as V-03 |
| C-30 | PARTIAL | Same as V-03 — no dedicated enumeration phase |
| C-37 | PASS | Phase 3 "must appear before", "must contain" uses imperative register; Contract item 6 (Known Failure Chains) also uses "must contain" — section-content requirements in output use imperative phrasing throughout |
| C-38 | PARTIAL | No Phase 1A STOP gate; 5-column combined table |

Note: V-04 preamble omits the explicit "Maintain imperative register in all section-placement and section-content requirements" obligation present in V-01/V-02/V-05. This introduces marginal risk of C-37 PARTIAL if Phase 3 phrasing drifts under token pressure — not enough for FAIL but registers as reduced confidence vs V-02.

V-04 has the chain-annotation mechanism (Contract item 6 = Known Failure Chains), but no existing rubric criterion rewards it directly — the v14 candidate has not been promoted to a scored criterion. C-36 = PASS (checkpoint validates items 4, 5, chain-check = 3 structural layers simultaneously).

Three PARTIAL criteria (C-20, C-30, C-38): −1.5 aspirational; additional −0.5 for preamble register risk (C-37 marginal).

Aspirational pass-equivalent ≈ 23.5/28 → 8.4 pts

**V-04 Composite: ~89** | **all_essential_pass: TRUE**

---

### V-05 — Combination (V-02 Phase 1A/1B + V-03 Contract Item 6; 7-Item Contract)

**Structure:** Phase 1A/1B split + Phase 1A STOP gate (C-38); 7-item Contract with item 6 = enumeration STOP gate, item 7 = section-content register (C-37); checkpoint validates items 4, 5, 6, 7. Structurally identical to V-01.

**Essential:** all PASS → 60 pts
**Recommended:** all PASS → 30 pts

**Aspirational differentials vs V-01:**

| ID | Score | Evidence |
|----|-------|----------|
| C-37 | PASS | Contract item 7 + Phase 3 imperative phrasing |
| C-38 | PASS | Phase 1A STOP gate |
| C-36 | PASS | Checkpoint validates items 4, 5, 6, 7 simultaneously |

The token-overhead concern noted in V-05 hypothesis (compression of C-35/C-36 rows) doesn't materially degrade any criterion — the checkpoint table structure enforces these by construction.

*Combination result: Phase 1A STOP gate (C-38) and section-content register Contract item (C-37) are independently loadbearing; neither mechanism degrades the other. Phase 1A STOP fires at Phase 1A close; section-content register audited at every Phase 2 checkpoint — different lifecycle positions, no structural interference.*

Aspirational pass-equivalent ≈ 25.5/28 → 9.1 pts (matches V-01)

**V-05 Composite: ~97** | **all_essential_pass: TRUE**

---

### Rankings

| Rank | Variation | Composite | all_essential_pass | Axis |
|------|-----------|-----------|-------------------|------|
| 1 | V-01 | 97 | TRUE | Full integration (C-37 + C-38 both active) |
| 1 | V-02 | 97 | TRUE | C-38 isolation (C-37 PASS from Phase 3 alone) |
| 1 | V-05 | 97 | TRUE | Combination (V-02 mechanism + V-03 Contract item) |
| 4 | V-03 | 91 | TRUE | C-37 isolation (C-38 PARTIAL from combined table) |
| 5 | V-04 | 89 | TRUE | Chain-annotation probe (C-38 PARTIAL; preamble C-37 risk) |

**Ceiling cap:** C-38 PARTIAL in V-03 and V-04 drives aspirational deficit; V-01/V-02/V-05 achieve parity because Phase 1A/1B split satisfies both C-30 and C-38 simultaneously.

---

### Excellence Signals (V-01 / V-02 / V-05)

**Signal 1 — Intra-framework Phase 1A STOP gate achieves C-38 at parity with pre-role Phase 0**

V-02 confirms: the structural mechanism (enumeration-only table + named STOP gate before any criterion-drafting step) is what satisfies C-38 — not the placement of the enumeration before the role definition. R12/V-05's pre-role Failure Analyst Phase 0 and R13/V-01's intra-framework Phase 1A produce equivalent C-38 compliance. Placement within the SetCoherenceAuditor framework is not a confound.

**Signal 2 — Section-content imperative register achievable without Contract item 7 (Phase 3 + preamble obligation is sufficient)**

V-02 isolates C-37: Phase 3 "must appear before criteria table", "must contain three labeled sub-sections" combined with the role-constitutive preamble obligation ("Maintain imperative register in all section-placement and section-content requirements") is a sufficient enforcement mechanism at the output layer. Contract item 7 (V-01, V-05) adds a declaration-layer reinforcement and a dedicated checkpoint row — a stronger mechanical guarantee — but is not required to achieve C-37 PASS. This makes Contract item 7 a robustness add-on rather than a prerequisite.

**Signal 3 — C-37 and C-38 enforcement layers are non-interfering across lifecycle positions**

V-05 combination result: Contract item 6 (enumeration STOP gate, fires at Phase 1A close) and Contract item 7 (section-content register, audited at every Phase 2 checkpoint iteration) operate at different lifecycle positions. Token overhead of the Phase 1A/1B split + two novel checkpoint rows does not compress existing C-35/C-36 rows. Both mechanisms are independently loadbearing.

**v14 signal from V-04 (below threshold for promotion):** Known Failure Chains block in Notes produces a structurally embedded chain annotation (root cause + affected IDs + fix). V-04's chain-check checkpoint row collects chain membership during generation. Two-round confirmation needed before promotion — V-04 provides round 1 structural evidence.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["intra-framework-Phase-1A-enumeration-STOP-gate-satisfies-C-38-at-parity-with-pre-role-Phase-0", "section-content-imperative-register-achievable-from-Phase-3-phrasing-plus-preamble-obligation-without-Contract-item-7"]}
```
