---

# flow-throttle — Round 12 Score Report (v12 Rubric, 178-point max)

## Variation Scores

### V-01 — Phase 4 Alternative Evaluation-Type Subtitle ("Remediation Registry and Throttle Budget Corrections")

**Axis:** C-36 subtitle-text inertness test. Phase 0 carries "Inertia Baseline" (confirmed R11 form). Phase 4 carries "Remediation Registry and Throttle Budget Corrections."

| Criterion block | Verdict | Evidence |
|---|---|---|
| C-01–C-13 (content criteria) | PASS | Full phase structure present: TABLE 1 (Phase 1), TABLE 2–4 (Phase 2), TABLE 5–7 (Phase 3), TABLE 8–10 (Phase 4). All analytical dimensions present. |
| C-14–C-16 (gate/barrier mechanisms) | PASS | GATE 1, GATE 2, GATE 3 all explicitly declared with block conditions. |
| C-17–C-32 (pre-barrier container + barrier heading) | PASS | PRE-EVALUATION ASSERTIONS block present before Round 2 barrier. Round 2 heading carries evaluation-type subtitle. Container header carries ASSERTIONS mechanism-type, positional qualifier, boundary-event phrase with round cross-reference. Full chain passes. |
| C-33 (Pre-Analysis Inertia Frame) | PASS | `### PHASE 0 — Inertia Baseline` appears as a structurally distinct section before Phase 1. |
| C-34 (Phase-Anchor Tabular Encoding) | PASS | Phase 1 carries TABLE 1; Phase 4 carries TABLE 8, TABLE 9, TABLE 10. Both anchor phases tabular. |
| C-35 (Pre-Analysis Baseline Heading Subtitle) | **PASS** | `### PHASE 0 — Inertia Baseline` — dash-separated subtitle "Inertia Baseline" names the content class. Confirmed R11 form; inertness axis not tested here. |
| C-36 (Phase-4 Anchor Heading Evaluation-Type Subtitle) | **PASS** | `### PHASE 4 — Remediation Registry and Throttle Budget Corrections` — "Remediation Registry" names an output class. The rubric explicitly lists "Remediation Registry" and "Throttle Budget Corrections" as conforming subtitle examples. Subtitle names an output class, not operations. |

**Score: 178 / 178**

---

### V-02 — Phase 4 Operation-Description Subtitle ("Synthesis and Validation") — Fail C-36

**Axis:** C-36 failure boundary. Phase 0 carries "Inertia Baseline" (C-35 PASS). Phase 4 carries "Synthesis and Validation."

| Criterion block | Verdict | Evidence |
|---|---|---|
| C-01–C-13 | PASS | Full phase structure and tabular content present across all phases. |
| C-14–C-16 | PASS | All three gate declarations present with block conditions. |
| C-17–C-32 | PASS | PRE-EVALUATION ASSERTIONS container intact. Round 2 heading carries evaluation-type subtitle. Full barrier-container chain passes. |
| C-33 | PASS | `### PHASE 0 — Inertia Baseline` structurally distinct before Phase 1. |
| C-34 | PASS | Phase 1: TABLE 1 present. Phase 4: TABLE 8, TABLE 9, TABLE 10 present. Anchor encoding intact. |
| C-35 | **PASS** | `### PHASE 0 — Inertia Baseline` — subtitle present and names content class. |
| C-36 | **FAIL** | `### PHASE 4 — Synthesis and Validation` — "Synthesis and Validation" describes the phase's operations (what it does), not an output or synthesis class (what it produces). The heading is structurally present but carries no class declaration. Fails the evaluation-type requirement: the subtitle must name an output class, not list operations. This is the Phase 4 analog of `### PHASE 0` failing C-35. |

**Score: 175 / 178** (−3 via C-36)

---

### V-03 — Phase 0 Plain Ordinal Heading, No Content-Type Subtitle — Fail C-35

**Axis:** C-35 failure boundary. Phase 0 carries `### PHASE 0` only. Phase 4 carries "Capacity Synthesis and PA Validation" (confirmed R11 V-04 form, C-36 PASS).

| Criterion block | Verdict | Evidence |
|---|---|---|
| C-01–C-13 | PASS | Full analysis content present in all phases. TABLE 1 through TABLE 10 complete. |
| C-14–C-16 | PASS | GATE 1, GATE 2, GATE 3 declared with block conditions. |
| C-17–C-32 | PASS | PRE-EVALUATION ASSERTIONS container present. Barrier heading carries evaluation-type subtitle. Full chain intact. |
| C-33 | PASS | `### PHASE 0` section appears before Phase 1 and establishes current-state context (construct stack, active limits, baseline failure point present in section body). C-33 requires structural existence and current-state content — the section satisfies both conditions. Heading subtitle is a C-35 requirement, not a C-33 requirement. |
| C-34 | PASS | Phase 1: TABLE 1 present. Phase 4: TABLE 8, TABLE 9, TABLE 10 present. |
| C-35 | **FAIL** | `### PHASE 0` carries only the ordinal label — no dash-separated subtitle naming the baseline content class. A reader cannot determine from the heading alone whether the section contains an inertia baseline, a system inventory, a load snapshot, or other pre-analysis content. C-35 requires the heading to carry a subtitle that names the content class. |
| C-36 | **PASS** | `### PHASE 4 — Capacity Synthesis and PA Validation` — confirmed R11 V-04 evaluation-type subtitle. "Capacity Synthesis and PA Validation" names an output class. |

**Score: 175 / 178** (−3 via C-35)

---

### V-04 — Combination: Role Sequence + Phase 0 "Current-State Inventory" + Phase 4 "Throttle Budget Corrections"

**Axes:** (1) Analyst/verifier role sequence — inertness test for heading-structure criteria. (2) Phase 0 subtitle "Current-State Inventory" — C-35 text-inertness test. (3) Phase 4 subtitle "Throttle Budget Corrections" — C-36 text-inertness test.

| Criterion block | Verdict | Evidence |
|---|---|---|
| C-01–C-13 | PASS | Full tabular analysis content present. Analyst framing in Phase 1 (arithmetic emphasis on request contribution column) and verifier framing in Round 2 (entitlement documentation source check) are content-layer additions that do not remove any required analysis dimension. |
| C-14–C-16 | PASS | GATE 1, GATE 2, GATE 3 all declared. Block conditions present. |
| C-17–C-32 | PASS | Round 2 renamed "Entitlement Verification" — evaluation-type subtitle is role-matched ("Entitlement Verification" names an evaluation class; C-32 is subtitle-text-inert per R10 confirmation). PRE-EVALUATION ASSERTIONS container present with full structural chain. Role persona assignment at barrier (`*Role: Platform entitlement verifier.*`) is below the container/heading layer — inert to all C-17–C-32 criteria. |
| C-33 | PASS | `### PHASE 0 — Current-State Inventory` structurally distinct before Phase 1. Section body names construct inventory, active limit profile, scenario parameters, first-break point — satisfies current-state context requirement. |
| C-34 | PASS | Phase 1: TABLE 1 present (analyst explicitly required arithmetic in every row). Phase 4: TABLE 8, TABLE 9, TABLE 10 present. |
| C-35 | **PASS** | `### PHASE 0 — Current-State Inventory` — subtitle "Current-State Inventory" names the content class of the pre-analysis section. Different text from "Inertia Baseline" (R11) — this variation tests C-35 text-inertness. "Current-State Inventory" is a content-class declaration: a reader knows the section contains a system state inventory without reading the body. |
| C-36 | **PASS** | `### PHASE 4 — Throttle Budget Corrections` — "Throttle Budget Corrections" is an explicitly listed pass example in the C-36 rubric text. Names an output class (the corrections to the throttle budget register). Role-sequence assignment does not interact with Phase 4 heading text. |

**Score: 178 / 178**

---

### V-05 — Combination: Phase 0 Plain Heading (Fail C-35) + Phase 4 Operation-Description Subtitle (Fail C-36)

**Axes:** Double-failure floor test. Phase 0: `### PHASE 0` (C-35 FAIL). Phase 4: `### PHASE 4 — Synthesis and Validation` (C-36 FAIL).

| Criterion block | Verdict | Evidence |
|---|---|---|
| C-01–C-13 | PASS | Full analysis content present. TABLE 1–TABLE 10 present. Phase structure intact. |
| C-14–C-16 | PASS | All three gates declared. |
| C-17–C-32 | PASS | PRE-EVALUATION ASSERTIONS container present. Round 2 heading carries evaluation-type subtitle ("Structural Precision Pass"). Full barrier-container chain intact. |
| C-33 | PASS | `### PHASE 0` section present before Phase 1 with current-state content in the body (construct stack, limits, baseline failure point). C-33 is satisfied by section existence and current-state content; heading subtitle is not a C-33 requirement. |
| C-34 | PASS | Phase 1: TABLE 1. Phase 4: TABLE 8, TABLE 9, TABLE 10. Anchor tabular encoding present. |
| C-35 | **FAIL** | `### PHASE 0` — no content-type subtitle. Same failure as V-03. Heading is a structural placeholder; content class not self-documented. |
| C-36 | **FAIL** | `### PHASE 4 — Synthesis and Validation` — operation-description subtitle; same failure as V-02. Lists operations performed (synthesis, validation), not an output class produced. |

**Score: 172 / 178** (−3 via C-35, −3 via C-36)

---

## Rankings

| Rank | Variation | Score | C-35 | C-36 | Delta |
|------|-----------|-------|------|------|-------|
| 1 (tie) | V-01 | 178/178 | PASS | PASS | — |
| 1 (tie) | V-04 | 178/178 | PASS | PASS | — |
| 3 (tie) | V-02 | 175/178 | PASS | FAIL | −3 |
| 3 (tie) | V-03 | 175/178 | FAIL | PASS | −3 |
| 5 | V-05 | 172/178 | FAIL | FAIL | −6 |

**Score spread confirmed: 178 / 175 / 175 / 178 / 172** — matches all five predictions exactly.

---

## Excellence Signals (from V-01 and V-04, both 178/178)

**Signal 1 — C-36 is subtitle-text-inert for evaluation-type subtitles.** V-01 uses "Remediation Registry and Throttle Budget Corrections" and V-04 uses "Throttle Budget Corrections" — both distinct from R11 V-04's "Capacity Synthesis and PA Validation" — and both pass C-36. The pass condition is form-based (ordinal + dash-separated output-class name), not phrase-specific. Any subtitle naming an output class satisfies C-36. This mirrors the C-32 text-inertness pattern confirmed in R10.

**Signal 2 — C-35 is subtitle-text-inert.** V-04 uses "Current-State Inventory" rather than the R11 forms "Inertia Baseline" / "Baseline Snapshot." The criterion requires a content-class declaration on the Phase 0 heading — not a specific phrase. "Current-State Inventory" names the content class; it passes on form, not on match to a prior example.

**Signal 3 — C-35 and C-36 independence is structurally confirmed, not just conjectured.** V-02 (fail C-36, pass C-35) and V-03 (fail C-35, pass C-36) both score 175. V-05 (fail both) scores 172. The arithmetic is exact: each criterion contributes exactly 3 points, independently, with no interaction. This closes the two-criterion independence proof: neither heading position's subtitle requirement conditions the other.

**Signal 4 — Role-sequence is inert at the heading-structure layer.** V-04's analyst/verifier persona structure scores identically to V-01's domain-expert framing on all heading-structure criteria. Persona assignment propagates through content framing (Round 1 arithmetic emphasis, Round 2 documentation sourcing) but does not reach Phase 0 or Phase 4 heading structure. The heading-subtitle layer is persona-invariant.

---

```json
{"top_score": 178, "all_essential_pass": true, "new_patterns": ["C-36 subtitle-text inertness confirmed: any evaluation-type output-class subtitle satisfies C-36 regardless of specific phrasing — the R11 form is not canonical", "C-35 and C-36 independence structurally proved: each contributes exactly 3 points independently, V-02=V-03=175 and V-05=172 close the proof"]}
```
