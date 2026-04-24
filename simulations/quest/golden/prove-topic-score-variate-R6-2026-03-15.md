---
skill: quest-score
skill_target: prove-topic
round: R6
date: 2026-03-15
rubric: prove-topic-rubric-v6-2026-03-15.md
variations_scored: [V-01, V-02, V-03, V-04, V-05]
top_score: 136
max_score: 136
all_essential_pass: true
rubric_ceiling_hit: true
new_patterns:
  - "Campaign-outcome named as distinct handoff boolean — incumbent_defense_closed: [true if all null] independent of co_activation_confirmed, enabling point-in-chain audit without dual-lock inference"
  - "Role-structural origin of dual attestation — two blocking roles each producing one attestation field makes C-22 drift-resistant by construction rather than by instruction"
---

# prove-topic — Round R6 Score Sheet (Rubric v6)

## Rubric Structure

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01 to C-05 | 10 | 50 |
| Recommended | C-06 to C-08 | 10 | 30 |
| Aspirational | C-09 to C-22 | 4 | 56 |
| **Total** | | | **136** |

Golden threshold: 80 (= essential + recommended exactly).
Round 6 primary targets: C-20 (per-stage tally), C-21 (co-activation in handoff), C-22 (invariant-registry as distinct gate field).

---

## V-01 — Role Sequence

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All stages ran | 10 | PASS | ROLE A → ROLE B → S1–S5 in fixed sequence; forward-only enforced by blocking roles |
| C-02 | Scout loaded | 10 | PASS | ROLE B searches scout path, records slug+path; GATE S blocks on found artifact |
| C-03 | Progressive artifacts | 10 | PASS | Each stage writes named artifact via explicit Write instruction |
| C-04 | Terminal output usable | 10 | PASS | Synthesis has: Invariant Compliance Check, CE State, ATOMIC DUAL-LOCK, Findings, CE Register, Thin-Evidence, Confidence, Handoff |
| C-05 | Artifact paths prefixed | 10 | PASS | Every Write instruction names full path `simulations/prove/{topic}/{topic}-{stage}-{date}.md` |
| C-06 | Stage order enforced | 10 | PASS | "All roles and stages execute in fixed sequence. No step may be skipped or reordered." STOP on GATE S fail |
| C-07 | Scout handoff explicit | 10 | PASS | GATE S records `scout_anchor: [slug]`; hypothesis frontmatter requires `scout_anchor: [slug from ROLE B]` |
| C-08 | Synthesis → topic-story | 10 | PASS | Handoff has `next: topic-story` with named artifact path |
| C-09 | Thin-evidence propagates | 4 | PASS | Stage 4 THIN flag → synthesis Thin-Evidence Note qualifies confidence |
| C-10 | Progress narrated | 4 | PASS | Each stage ends with prose Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Claim: [one-line]. Advancing to Stage 2." |
| C-11 | Hypothesis hard-gated | 4 | PASS | GATE S requires both fields; explicit STOP if either fails; Stage 1 follows GATE S pass only |
| C-12 | Comparator at session open | 4 | PASS | `status_quo_comparator` in ROLE A; referenced in every counter-evidence section at S2–S4 |
| C-13 | Per-artifact path enforcement | 4 | PASS | Every Write instruction names full path; no prefix-only shorthand |
| C-14 | Counter-evidence unconditional | 4 | PASS | "Counter-Evidence Register (MANDATORY)" with fallback "If all null: recorded in ATOMIC DUAL-LOCK block above." |
| C-15 | Gate clearance in hypothesis | 4 | PASS | `gate_s_cleared: true` in hypothesis frontmatter as mandatory field |
| C-16 | Null CE triggers escalation | 4 | PASS | LOCK 1: "Promotion to topic-story blocked until adversarial review complete or explicitly deferred with written justification." |
| C-17 | Confidence mechanically capped | 4 | PASS | "CE-score = -2 (pre-committed formula — not a synthesis judgment). Confidence cannot be rated HIGH while null-CE escalation is active." |
| C-18 | Null CE doubly locked | 4 | PASS | ATOMIC DUAL-LOCK: "one trigger, both locks fire simultaneously... Both locks active. Partial activation is a format error." |
| C-19 | Protocol pre-committed | 4 | PASS | ROLE A: `registry_note: "Both invariants are on record. Cannot be modified after this point."` — invariant language before Stage 0 |
| C-20 | Per-stage null tally | 4 | PASS | S2: "Running tally: 1 null. 2 evidence stages remain (S3, S4)... Both were registered in ROLE A before this stage opened." S3/S4 carry forward count with protocol reference |
| C-21 | Co-activation in handoff | 4 | PASS | Handoff: `co_activation_confirmed: [must equal dual_lock_fired]` as explicit integrity constraint |
| C-22 | Registry as distinct gate field | 4 | PASS | GATE S and hypothesis frontmatter both carry `gate_s_cleared: true` (ROLE B) and `invariant_registry_confirmed: true` (ROLE A) as structurally distinct fields |

**V-01: 136/136 — all essential PASS**

---

## V-02 — Output Format (cumulative table)

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All stages ran | 10 | PASS | Stage 0–5 in fixed sequence; "Do not fill forward" constraint on table |
| C-02 | Scout loaded | 10 | PASS | Stage 0 records slug+path; GATE S requires both `gate_s_cleared` and `invariant_registry_confirmed` |
| C-03 | Progressive artifacts | 10 | PASS | Named Write instruction per stage |
| C-04 | Terminal output usable | 10 | PASS | Synthesis: pasted NULL-TALLY TABLE, CE State, ATOMIC DUAL-LOCK, Findings, CE Register, Thin-Evidence, Confidence, Handoff |
| C-05 | Artifact paths prefixed | 10 | PASS | All Write instructions use full `{topic}-{stage}-{date}.md` path |
| C-06 | Stage order enforced | 10 | PASS | "Five stages in fixed sequence." Table row fill constraint: "Do not fill forward." |
| C-07 | Scout handoff explicit | 10 | PASS | GATE S `scout_anchor`; hypothesis frontmatter `scout_anchor: [slug from GATE S]` |
| C-08 | Synthesis → topic-story | 10 | PASS | Handoff `next: topic-story` with artifact path |
| C-09 | Thin-evidence propagates | 4 | PASS | Stage 4 THIN flag → synthesis Thin-Evidence section; confidence qualified |
| C-10 | Progress narrated | 4 | PASS | Prose confirms: "Artifact written: {topic}-websearch-{date}.md. S2 tally row updated." |
| C-11 | Hypothesis hard-gated | 4 | PASS | "Both fields required before Stage 1 opens." — forward-condition blocking Stage 1 |
| C-12 | Comparator at session open | 4 | PASS | `status_quo_comparator` in CAMPAIGN OPEN; referenced per-stage in counter-evidence sections |
| C-13 | Per-artifact path enforcement | 4 | PASS | Full path per Write instruction |
| C-14 | Counter-evidence unconditional | 4 | PASS | "Counter-Evidence Register (MANDATORY)" with null fallback |
| C-15 | Gate clearance in hypothesis | 4 | PASS | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | Null CE triggers escalation | 4 | PASS | LOCK 1 blocks promotion |
| C-17 | Confidence mechanically capped | 4 | PASS | `cap_applied: true`; CE-score = -2; "Confidence ceiling: MEDIUM. HIGH not available." |
| C-18 | Null CE doubly locked | 4 | PASS | ATOMIC DUAL-LOCK: "Both locks activate from this single entry. Partial activation is a format error." |
| C-19 | Protocol pre-committed | 4 | PASS | CAMPAIGN OPEN: "Session-level invariants. Cannot be modified after this point." |
| C-20 | Per-stage null tally | 4 | PASS | NULL-TALLY TABLE `Running Null Count` column; each null-result note instructs per-row update with pre-committed obligation reference: "pre-committed at campaign open, not assignable at synthesis" |
| C-21 | Co-activation in handoff | 4 | PASS | Handoff: `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-22 | Registry as distinct gate field | 4 | PASS | GATE S: `gate_s_cleared: true` + `invariant_registry_confirmed: true ← distinct from gate_s_cleared; two separate attestations` — both required |

**V-02: 136/136 — all essential PASS**

---

## V-03 — Lifecycle Emphasis (STAGE ENTER / STAGE EXIT)

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All stages ran | 10 | PASS | Stage 0–5 with STAGE ENTER/EXIT blocks; entry conditions require prior stage completion |
| C-02 | Scout loaded | 10 | PASS | Stage 0 GATE S; STAGE 0 EXIT records both `gate_s_cleared` and `invariant_registry_confirmed` |
| C-03 | Progressive artifacts | 10 | PASS | STAGE EXIT records `artifact_written` per stage |
| C-04 | Terminal output usable | 10 | PASS | Stage 5 synthesis fully populated via STAGE ENTER carry-forward |
| C-05 | Artifact paths prefixed | 10 | PASS | All Write instructions and EXIT blocks name full `{topic}-{stage}-{date}.md` paths |
| C-06 | Stage order enforced | 10 | PASS | STAGE ENTER entry conditions require prior EXIT confirmed; Stage 1 entry requires gate_s_cleared AND invariant_registry_confirmed |
| C-07 | Scout handoff explicit | 10 | PASS | GATE S `scout_anchor`; hypothesis frontmatter `scout_anchor: [from Stage 0]` |
| C-08 | Synthesis → topic-story | 10 | PASS | STAGE 5 EXIT (= Handoff): `next: topic-story` |
| C-09 | Thin-evidence propagates | 4 | PASS | Stage 4 EXIT `thin_evidence_flag`; carry-forward into Stage 5 ENTER; synthesis qualifies confidence |
| C-10 | Progress narrated | 4 | PASS | STAGE EXIT Confirm at each stage: "Stage N complete. CE: [found/null]. Tally: [N]. Advancing to Stage N+1." |
| C-11 | Hypothesis hard-gated | 4 | PASS | STAGE 1 ENTER: "Entry condition: Stage 0 EXIT confirmed with gate_s_cleared = true AND invariant_registry_confirmed = true." |
| C-12 | Comparator at session open | 4 | PASS | `status_quo_comparator` in SESSION INVARIANT REGISTRY; carried in STAGE ENTER blocks |
| C-13 | Per-artifact path enforcement | 4 | PASS | Write instructions and STAGE EXIT `artifact_written` both name full paths |
| C-14 | Counter-evidence unconditional | 4 | PASS | CE Register MANDATORY; null fallback in DUAL-LOCK block |
| C-15 | Gate clearance in hypothesis | 4 | PASS | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | Null CE triggers escalation | 4 | PASS | LOCK 1 blocks promotion |
| C-17 | Confidence mechanically capped | 4 | PASS | "CE-score = -2 (locked formula — not a synthesis judgment). Confidence ceiling: MEDIUM. HIGH not available." |
| C-18 | Null CE doubly locked | 4 | PASS | ATOMIC DUAL-LOCK: "one trigger, both locks fire simultaneously... Both locks active. Partial activation is a format error." |
| C-19 | Protocol pre-committed | 4 | PASS | SESSION INVARIANT REGISTRY: "binding for the full session — cannot be modified or bypassed" — the exact exemplar language |
| C-20 | Per-stage null tally | 4 | PASS | STAGE EXIT tally field + running-count language: "Running tally: 1 null. 2 evidence stages remain (S3, S4) as pre-committed obligations... locked session invariants — not decisions pending synthesis." |
| C-21 | Co-activation in handoff | 4 | PASS | STAGE 5 EXIT: `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-22 | Registry as distinct gate field | 4 | PASS | GATE S exit block: `gate_s_cleared: true` + `invariant_registry_confirmed: true ← distinct from gate_s_cleared; traces Session Invariant Registry` — both required before STAGE 0 EXIT |

**V-03: 136/136 — all essential PASS**

---

## V-04 — Phrasing Register + Inertia Framing

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All stages ran | 10 | PASS | Stage 0–5 in sequence; "Don't guess forward" on scout fail |
| C-02 | Scout loaded | 10 | PASS | Stage 0 searches scout; GATE S requires both fields before Stage 1 |
| C-03 | Progressive artifacts | 10 | PASS | Write instruction per stage |
| C-04 | Terminal output usable | 10 | PASS | Synthesis: incumbent defense tally, ATOMIC DUAL-LOCK, Findings, Incumbent defense record, Thin-evidence, Confidence, Handoff |
| C-05 | Artifact paths prefixed | 10 | PASS | All Write instructions name `{topic}-{stage}-{date}.md` |
| C-06 | Stage order enforced | 10 | PASS | "These are locked at campaign open. They carry through every stage." Stop instruction on scout fail |
| C-07 | Scout handoff explicit | 10 | PASS | Stage 0 records slug; hypothesis frontmatter `scout_anchor: [from Stage 0 — named, not paraphrased]` |
| C-08 | Synthesis → topic-story | 10 | PASS | "Handoff to topic-story" section with `next: topic-story` |
| C-09 | Thin-evidence propagates | 4 | PASS | Stage 4 THIN flag → synthesis thin-evidence note with confidence qualification |
| C-10 | Progress narrated | 4 | PASS | Prose confirms per stage: "Web search written: {topic}-websearch-{date}.md — moving to internal signals." |
| C-11 | Hypothesis hard-gated | 4 | PASS | GATE S: "Before Stage 1 opens, confirm: gate_s_cleared: true... invariant_registry_confirmed: true. If you can't find a scout record, stop here." |
| C-12 | Comparator at session open | 4 | PASS | `incumbent` in OPENING DECLARATIONS before Stage 0; referenced at every stage as "defend the incumbent" |
| C-13 | Per-artifact path enforcement | 4 | PASS | Full path per Write instruction |
| C-14 | Counter-evidence unconditional | 4 | PASS | "Incumbent defense record (MANDATORY)" with null fallback |
| C-15 | Gate clearance in hypothesis | 4 | PASS | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | Null CE triggers escalation | 4 | PASS | LOCK 1: "[reviewer_type] is tasked... Topic-story is blocked until this challenge is addressed or explicitly deferred." |
| C-17 | Confidence mechanically capped | 4 | PASS | "CE-score = -2. Ceiling: MEDIUM. HIGH is off the table while the challenge is open." |
| C-18 | Null CE doubly locked | 4 | PASS | ATOMIC DUAL-LOCK: "Both active. One trigger. Partial activation would mean the incumbent got a half-defense." |
| C-19 | Protocol pre-committed | 4 | PASS | "Null-evidence commitments (locked here — not decisions for later)... Both consequences are pre-registered. If they fire, you execute — you don't decide." `invariant_registry_confirmed: true` |
| C-20 | Per-stage null tally | 4 | PASS | S2: "Running tally: 1 null. The incumbent is still owed a defense at S3 and S4... Both were locked at opening — not my call now." S3: "[N] null... not a judgment I'm making at synthesis." S4: "[N] null. All stages complete... Both obligations are paid at synthesis, not negotiated." |
| C-21 | Co-activation in handoff | 4 | PASS | Handoff: `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-22 | Registry as distinct gate field | 4 | PASS | Hypothesis frontmatter: `gate_s_cleared: true` + `invariant_registry_confirmed: true ← separate: confirms opening declarations active`; GATE S requires both |

**V-04: 136/136 — all essential PASS**

---

## V-05 — Combined (Role Sequence + Output Format + Inertia)

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All stages ran | 10 | PASS | ROLE A → ROLE B → S1–S5 in fixed sequence; two-phase blocking chain |
| C-02 | Scout loaded | 10 | PASS | ROLE B searches and records; GATE S requires both fields; explicit STOP on fail |
| C-03 | Progressive artifacts | 10 | PASS | Write instruction per stage; table row update confirms stage completion |
| C-04 | Terminal output usable | 10 | PASS | Synthesis: ROLE A Invariant Compliance, pasted INCUMBENT-DEFENSE TABLE, CE State, ATOMIC DUAL-LOCK, Findings, CE Register, Thin-Evidence, Confidence, Handoff |
| C-05 | Artifact paths prefixed | 10 | PASS | All Write instructions name full paths |
| C-06 | Stage order enforced | 10 | PASS | "ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true." Sequential blocking |
| C-07 | Scout handoff explicit | 10 | PASS | ROLE B `scout_anchor`; hypothesis frontmatter `scout_anchor: [from ROLE B]` |
| C-08 | Synthesis → topic-story | 10 | PASS | Handoff `next: topic-story` with artifact path |
| C-09 | Thin-evidence propagates | 4 | PASS | Stage 4 THIN flag → synthesis qualifies confidence |
| C-10 | Progress narrated | 4 | PASS | Prose Confirm per stage; table row update noted in confirm |
| C-11 | Hypothesis hard-gated | 4 | PASS | "ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true." ROLE B complete required before Stage 1 |
| C-12 | Comparator at session open | 4 | PASS | `incumbent` in ROLE A before any stage; referenced in INCUMBENT-DEFENSE TABLE and per-stage sections |
| C-13 | Per-artifact path enforcement | 4 | PASS | Full path per Write instruction |
| C-14 | Counter-evidence unconditional | 4 | PASS | "Incumbent Defense Register (MANDATORY)" with null fallback |
| C-15 | Gate clearance in hypothesis | 4 | PASS | `gate_s_cleared: true ← ROLE B output` in hypothesis frontmatter |
| C-16 | Null CE triggers escalation | 4 | PASS | LOCK 1 blocks promotion to topic-story |
| C-17 | Confidence mechanically capped | 4 | PASS | `cap_applied: true`; CE-score = -2; "Ceiling: MEDIUM. HIGH not available while challenge is open." |
| C-18 | Null CE doubly locked | 4 | PASS | ATOMIC DUAL-LOCK: "Both locks activate from this single entry. Partial activation is a format error." |
| C-19 | Protocol pre-committed | 4 | PASS | ROLE A: `invariant_registry_confirmed: true`. `registry_note: "Locked. Cannot be modified after ROLE A."` |
| C-20 | Per-stage null tally | 4 | PASS | INCUMBENT-DEFENSE TABLE `Running Null Count` column + per-row update instructions with "Pre-committed in ROLE A — not a synthesis decision" framing |
| C-21 | Co-activation in handoff | 4 | PASS | Handoff: `co_activation_confirmed: [must equal dual_lock_fired]` + `incumbent_defense_closed: [true if all null, false if any found]` |
| C-22 | Registry as distinct gate field | 4 | PASS | Hypothesis frontmatter: `gate_s_cleared: true ← ROLE B output` + `invariant_registry_confirmed: true ← ROLE A output (distinct field)` — structurally distinct because they originate from different blocking roles |

**V-05: 136/136 — all essential PASS**

---

## Summary Table

| Var | Essential (50) | Recommended (30) | Aspirational (56) | Total (136) | All Essential |
|-----|---------------|-----------------|------------------|-------------|---------------|
| V-01 | 50 | 30 | 56 | **136** | YES |
| V-02 | 50 | 30 | 56 | **136** | YES |
| V-03 | 50 | 30 | 56 | **136** | YES |
| V-04 | 50 | 30 | 56 | **136** | YES |
| V-05 | 50 | 30 | 56 | **136** | YES |

**Rubric ceiling hit.** All five variations score 136/136. Round 6's engineering goal — close C-20, C-21, C-22 simultaneously in a single prompt — succeeded across every axis tested. Every variation that explicitly targeted all three new criteria earned full PASS on all three.

---

## Ranking

**Rank 1 (tied)**: V-01, V-02, V-03, V-04, V-05 — all 136/136

**Differentiation by structural robustness** (scores equal; axes independent?):

| Var | C-20 source | C-21 source | C-22 source | Axes independent |
|-----|-------------|-------------|-------------|-----------------|
| V-01 | Role-exit null note | Handoff field | Two-role structure | Partial — C-20 and C-22 share role-exit architecture |
| V-02 | Table row | Handoff field | Two-field GATE S | Mostly — table distinct from gate |
| V-03 | STAGE EXIT gate | STAGE 5 EXIT | GATE S two-field | Partial — all three share lifecycle block |
| V-04 | Per-stage null note | Handoff field | Two-field GATE S | Partial — C-20 and C-22 use different mechanisms |
| **V-05** | **Table row (V-02 axis)** | **Table echo (combined)** | **Two-role (V-01 axis)** | **Yes — distinct source per criterion** |

**V-05 is the structural robustness winner**: C-20 arises from the table, C-22 arises from the role separation, C-21 arises from the table echo into the Handoff. Removing any single axis eliminates exactly one criterion's structural origin. No other variation has this property.

---

## Excellence Signals

### Signal 1 (V-05) — Campaign-closure boolean as distinct handoff field

```
incumbent_defense_closed: [true if all null, false if any found]
```

This is separate from and complementary to `co_activation_confirmed`. It names the campaign's null-CE outcome as a first-class boolean — not derivable from dual-lock state inference. A downstream skill (topic-story) reads `incumbent_defense_closed: true` directly without reasoning about whether co-activation fired. Audit without replay.

**Candidate C-23**: The handoff includes a campaign-level outcome boolean (`incumbent_defense_closed`, `null_ce_campaign: true`, or equivalent) that names the null-CE state independently of `co_activation_confirmed`. A handoff carrying only `co_activation_confirmed` and `dual_lock_fired` satisfies C-21 but not C-23. The boolean must be readable without inferring from the dual-lock block.

### Signal 2 (V-01, V-05) — Role-structural origin of dual attestation

When the invariant registry and scout load are produced by two separate blocking roles, the hypothesis frontmatter's two fields (`gate_s_cleared` from ROLE B, `invariant_registry_confirmed` from ROLE A) arise from the architecture — not from a special "add a second field" instruction. Any refactoring that merges the two roles into one would visibly collapse two fields to one, making the regression observable. C-22 becomes drift-resistant by construction.

**Implication**: Single-role variations that add `invariant_registry_confirmed` as a side note on GATE S pass C-22 today but are less robust than two-role variations. The field's origin is not traceable from the artifact — only from the session structure.

---

## v6 Severity Stack — Final Status

| Criterion | Role | R6 status |
|-----------|------|-----------|
| C-14 | Recording | All PASS (established R2) |
| C-16 | Escalation | All PASS (established R3) |
| C-17 | Consequence | All PASS (established R3) |
| C-18 | Co-activation | All PASS (established R4) |
| C-19 | Pre-commitment | All PASS (established R4) |
| C-20 | Accumulation | All PASS (closed R6) |
| C-21 | Handoff echo | All PASS (closed R6) |
| C-22 | Registry trace | All PASS (closed R6) |

The full 8-criterion null-CE closure chain is now achievable in a single prompt. Round 6 confirms that per-stage accumulation (C-20), handoff echo (C-21), and registry trace (C-22) are not in tension with each other or with the v5 stack — all eight fire simultaneously in all five variations.

---

## Round 7 Direction

The rubric ceiling (136/136) has been hit by all variations. Two paths forward:

**Path A — C-23**: Elevate the `incumbent_defense_closed` pattern to a criterion. The handoff carries a named campaign-outcome boolean independent of `co_activation_confirmed`. Max rises to 140. Tests whether downstream skill consumers need a dedicated campaign-state field beyond the dual-lock echo.

**Path B — Adversarial axis**: Introduce variations where Stage N explicitly *finds* counter-evidence and verify that C-20's tally logic, C-18's dual-lock, and C-21's handoff echo correctly suppress activation when CE is present. All R6 variations were scored on the null-CE path; the found-CE path has not been exercised as a primary axis.

**Recommended**: Path A (C-23) first — clean escalation from one new excellence signal. Path B as a follow-on to stress-test the non-null path.
