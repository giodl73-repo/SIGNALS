## prove-topic — Round 10 Scoring

### Rubric Reference: v9 (max 168, golden ≥ 80)

All five R10 variations are built explicitly on the full v9 stack (C-01 through C-30). I evaluate each against all 30 criteria, then rank by R10 axis coverage.

---

## V-01 — CE Verdict Ownership

**R10 axis**: `s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict` as OWNED FIELDs; CE VERDICT OWNERSHIP TABLE at CAMPAIGN OPEN; `null_tally_final` derivation formula references three named fields.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All stages present | PASS | CAMPAIGN OPEN, ROLE A/B, GATE S, Stages 1–5 |
| C-02 Scout artifact loaded | PASS | ROLE B loads `{topic}-scout-record-{date}.md` |
| C-03 Progressive artifact writes | PASS | Write instruction at each stage |
| C-04 Synthesis readiness signal | PASS | "Evidence brief ready for topic-story." |
| C-05 Artifact naming consistent | PASS | `{topic}-[type]-{date}.md` in every write instruction |
| C-06 Stage order enforced | PASS | Forward-only; gate blocks re-entry |
| C-07 Scout handoff explicit | PASS | `scout_anchor` in hypothesis frontmatter |
| C-08 Synthesis signals topic-story | PASS | `next: topic-story` in handoff |
| C-09 Thin-evidence propagates | PASS | Null CE acknowledged; CE section mandatory with fallback |
| C-10 Progress narrated per stage | PASS | Confirm lines with prose at every stage |
| C-11 Hypothesis hard-gated | PASS | GATE S blocks Stage 1 if either field false/missing |
| C-12 Comparator anchored at open | PASS | `status_quo_comparator` at CAMPAIGN OPEN |
| C-13 Per-artifact path enforcement | PASS | Full `{topic}-[type]-{date}.md` on each write instruction |
| C-14 CE unconditionally required | PASS | MANDATORY SECTION with null fallback |
| C-15 Gate clearance in artifact | PASS | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 Null CE triggers escalation | PASS | Adversarial review required, SESSION INVARIANT A execution |
| C-17 Confidence mechanically capped | PASS | `ce_score = -2`, `HIGH blocked` |
| C-18 Null CE doubly locked | PASS | ATOMIC DUAL-LOCK; `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-19 Protocol pre-committed | PASS | SESSION INVARIANTs A, B, C with "cannot be modified or bypassed" |
| C-20 Per-stage null tally | PASS | NULL TALLY NOTE + running count + protocol reference at Stages 2, 3 |
| C-21 Co-activation in handoff | PASS | `co_activation_confirmed` in handoff section |
| C-22 Invariant registry confirmed | PASS | `invariant_registry_confirmed: true` in hypothesis frontmatter; ROLE A sole source |
| C-23 Campaign-outcome boolean | PASS | `incumbent_defense_closed` independent of co_activation |
| C-24 Role-structural dual attestation | PASS | ROLE A owns `invariant_registry_confirmed`; ROLE B owns `gate_s_cleared` |
| C-25 Inline derivation annotations | PASS | All 9 handoff fields carry `[derived from: X]` |
| C-26 Schema pre-committed | PASS | PRE-COMMITTED HANDOFF SCHEMA table at CAMPAIGN OPEN, compliance check at synthesis |
| C-27 Independence chain on `incumbent_defense_closed` | PASS | `positive_derivation` + `independence_chain` on field |
| C-28 Symmetric chain on both lock fields | PASS | `co_activation_confirmed` also carries `positive_derivation` + `independence_chain` |
| C-29 Per-stage schema integrity counts | PASS | SCHEMA INTEGRITY NOTE (9/9, 0 additions/omissions) at Stages 2, 3, 4 |
| C-30 Annotation rule as session invariant | PASS | SESSION INVARIANT C with invariant language at CAMPAIGN OPEN |

**V-01 composite: 168/168 — Golden** (R10 axis: adds CE verdict field chain beyond v9 ceiling)

---

## V-02 — Counter-Hypothesis Closure

**R10 axis**: `counter_hypothesis:` field at Stage 1; COUNTER-HYPOTHESIS RESOLUTION section at Stage 5 with REFUTED / PARTIALLY REFUTED / OPEN RISK verdict; OPEN RISK reduces confidence one tier.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All stages present |
| C-02 | PASS | ROLE B scout load |
| C-03 | PASS | Progressive writes |
| C-04 | PASS | "Evidence brief ready for topic-story." |
| C-05 | PASS | Per-instruction path naming |
| C-06 | PASS | Forward-only gate |
| C-07 | PASS | `scout_anchor` in frontmatter |
| C-08 | PASS | `next: topic-story` in handoff |
| C-09 | PASS | Null CE mandatory section with fallback |
| C-10 | PASS | Per-stage Confirm prose |
| C-11 | PASS | GATE S hard block |
| C-12 | PASS | `status_quo_comparator` at CAMPAIGN OPEN |
| C-13 | PASS | Full path on each write instruction |
| C-14 | PASS | MANDATORY SECTION, null fallback explicit |
| C-15 | PASS | `gate_s_cleared` in hypothesis frontmatter |
| C-16 | PASS | SESSION INVARIANT A execution on null |
| C-17 | PASS | CE-score = -2 cap |
| C-18 | PASS | ATOMIC DUAL-LOCK, `co_activation_confirmed` parity check |
| C-19 | PASS | SESSION INVARIANTs A, B, C with invariant language |
| C-20 | PASS | NULL TALLY NOTE + running count at Stages 2, 3 |
| C-21 | PASS | `co_activation_confirmed` in handoff |
| C-22 | PASS | `invariant_registry_confirmed` in frontmatter, ROLE A sole source |
| C-23 | PASS | `incumbent_defense_closed` independent boolean |
| C-24 | PASS | Structural role separation |
| C-25 | PASS | All 9 handoff fields labeled |
| C-26 | PASS | PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN |
| C-27 | PASS | `incumbent_defense_closed` has `positive_derivation` + `independence_chain` |
| C-28 | PASS | `co_activation_confirmed` also has `positive_derivation` + `independence_chain` |
| C-29 | PASS | SCHEMA INTEGRITY NOTE (9/9, 0 additions/omissions) at Stages 2, 3, 4 |
| C-30 | PASS | SESSION INVARIANT C at CAMPAIGN OPEN with invariant language |

**V-02 composite: 168/168 — Golden** (R10 axis: adds counter-hypothesis lifecycle closure)

---

## V-03 — Null Tally Chain Echo

**R10 axis**: NULL TALLY CHAIN RULE at CAMPAIGN OPEN; Stage 5 ATOMIC DUAL-LOCK includes NULL TALLY CHAIN block reconstructing per-stage accumulation order (S2→N, S3→N, S4→N=null_tally_final); chain terminal value cross-checked against Stage 4.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Full v9 structure present; ROLE A/B, GATE S, stages 1–5 |
| C-09 | PASS | Null CE mandatory with fallback; tally chain echoes all stages |
| C-10 | PASS | Per-stage Confirm prose + tally chain forward-reference |
| C-11 | PASS | GATE S hard block |
| C-12 | PASS | `status_quo_comparator` at CAMPAIGN OPEN |
| C-13 | PASS | Full `{topic}-[type]-{date}.md` per write instruction |
| C-14 | PASS | MANDATORY SECTION, null fallback |
| C-15 | PASS | `gate_s_cleared` in hypothesis frontmatter |
| C-16 | PASS | SESSION INVARIANT A execution |
| C-17 | PASS | CE-score = -2 cap |
| C-18 | PASS | ATOMIC DUAL-LOCK with format error guard |
| C-19 | PASS | SESSION INVARIANTs A, B, C at CAMPAIGN OPEN |
| C-20 | PASS | NULL TALLY NOTE + running count + tally chain forward note at Stages 2, 3 |
| C-21 | PASS | `co_activation_confirmed` in handoff |
| C-22 | PASS | `invariant_registry_confirmed` in hypothesis frontmatter; ROLE A sole source |
| C-23 | PASS | `incumbent_defense_closed` independent boolean |
| C-24 | PASS | Structural role separation |
| C-25 | PASS | All 9 handoff fields carry derivation labels; `null_tally_final` labels reference tally chain |
| C-26 | PASS | PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN; compliance check at synthesis |
| C-27 | PASS | `incumbent_defense_closed` has `positive_derivation` + `independence_chain` |
| C-28 | PASS | `co_activation_confirmed` has `positive_derivation` + `independence_chain` |
| C-29 | PASS | SCHEMA INTEGRITY NOTE at Stages 2, 3, 4 |
| C-30 | PASS | SESSION INVARIANT C at CAMPAIGN OPEN |

**V-03 composite: 168/168 — Golden** (R10 axis: adds null tally accumulation chain in terminal artifact)

---

## V-04 — CE Verdict Ownership + Counter-Hypothesis Closure

**R10 axes combined**: CE VERDICT OWNERSHIP TABLE (V-01) + COUNTER-HYPOTHESIS CLOSURE RULE (V-02). Both locked at CAMPAIGN OPEN; both discharged at Stage 4 (verdict fields) and Stage 5 (hypothesis resolution).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Full v9 structure; dual-axis CAMPAIGN OPEN with both tables |
| C-09 | PASS | Null CE mandatory; CE section + escalation |
| C-10 | PASS | Per-stage Confirm with counter-hypothesis tracking note |
| C-11 | PASS | GATE S hard block |
| C-12 | PASS | `status_quo_comparator` at CAMPAIGN OPEN |
| C-13 | PASS | Full path on each write instruction |
| C-14 | PASS | MANDATORY SECTION, null fallback |
| C-15 | PASS | `gate_s_cleared` in hypothesis frontmatter |
| C-16 | PASS | SESSION INVARIANT A execution |
| C-17 | PASS | CE-score = -2 cap |
| C-18 | PASS | ATOMIC DUAL-LOCK with format error guard |
| C-19 | PASS | SESSION INVARIANTs A, B, C with invariant language |
| C-20 | PASS | NULL TALLY NOTE + running count at Stages 2, 3 |
| C-21 | PASS | `co_activation_confirmed` in handoff |
| C-22 | PASS | `invariant_registry_confirmed` in frontmatter; ROLE A scope updated to include both rules |
| C-23 | PASS | `incumbent_defense_closed` independent boolean |
| C-24 | PASS | Structural role separation |
| C-25 | PASS | All 9 handoff fields labeled; `null_tally_final` references CE VERDICT OWNERSHIP TABLE formula |
| C-26 | PASS | PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN; compliance check |
| C-27 | PASS | `incumbent_defense_closed` has `positive_derivation` + `independence_chain` |
| C-28 | PASS | `co_activation_confirmed` has `positive_derivation` + `independence_chain` |
| C-29 | PASS | SCHEMA INTEGRITY NOTE at Stages 2, 3, 4 |
| C-30 | PASS | SESSION INVARIANT C at CAMPAIGN OPEN |

**V-04 composite: 168/168 — Golden** (R10 axes: CE verdict ownership chain + hypothesis lifecycle closure)

---

## V-05 — All Four R10 Axes Combined

**R10 axes combined**: CE VERDICT OWNERSHIP TABLE + COUNTER-HYPOTHESIS CLOSURE RULE + NULL TALLY CHAIN RULE + schema compliance cross-reference (synthesis `schema_compliance_confirmed` cites per-stage SCHEMA INTEGRITY NOTEs by stage). `schema_compliance_confirmed` self-declared as field 9.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All stages present; ROLE A/B locked before any stage |
| C-02 | PASS | ROLE B loads named scout artifact |
| C-03 | PASS | Progressive writes across 5 stages |
| C-04 | PASS | "Evidence brief ready for topic-story." |
| C-05 | PASS | `{topic}-[type]-{date}.md` at every write instruction |
| C-06 | PASS | Forward-only; "Do not modify after this point" |
| C-07 | PASS | `scout_anchor` in hypothesis frontmatter |
| C-08 | PASS | `next: topic-story` in handoff |
| C-09 | PASS | Null CE propagates to mandatory synthesis section |
| C-10 | PASS | Per-stage Confirm prose with CE status, schema status, counter-hypothesis status |
| C-11 | PASS | GATE S: "If either field is false or missing: STOP." |
| C-12 | PASS | `status_quo_comparator` at CAMPAIGN OPEN; referenced at Stage 2 |
| C-13 | PASS | Full path naming per write instruction throughout |
| C-14 | PASS | MANDATORY SECTION unconditionally required; null fallback explicit |
| C-15 | PASS | `gate_s_cleared: true` in hypothesis frontmatter; ROLE B sole source |
| C-16 | PASS | SESSION INVARIANT A execution on null CE |
| C-17 | PASS | `CE-score = -2 (all-null formula). Maximum claim: MEDIUM. HIGH blocked.` |
| C-18 | PASS | ATOMIC DUAL-LOCK; `co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]` |
| C-19 | PASS | SESSION INVARIANTs A, B, C all with "cannot be modified or bypassed at synthesis" |
| C-20 | PASS | NULL TALLY NOTE + running count + protocol reference at Stages 2, 3 |
| C-21 | PASS | `co_activation_confirmed` with `[derived from: dual_lock_fired]` in handoff |
| C-22 | PASS | `invariant_registry_confirmed: true` in hypothesis frontmatter; ROLE A scope covers all 5 rules |
| C-23 | PASS | `incumbent_defense_closed` independent of co_activation; own derivation chain |
| C-24 | PASS | ROLE A and ROLE B each structural sole producer of exactly one attestation field |
| C-25 | PASS | All 9 handoff fields carry `[derived from: X]`; `schema_compliance_confirmed` adds `collection_phase_chain:` |
| C-26 | PASS | PRE-COMMITTED HANDOFF SCHEMA; `schema_compliance_confirmed` self-registered as field 9; compliance check at synthesis |
| C-27 | PASS | `incumbent_defense_closed` carries `positive_derivation:` + `independence_chain:` |
| C-28 | PASS | `co_activation_confirmed` carries `positive_derivation:` + `independence_chain:`; Note in ATOMIC DUAL-LOCK confirms parallel consumer relationship |
| C-29 | PASS | SCHEMA INTEGRITY NOTE (Stage 2), SCHEMA INTEGRITY NOTE (Stage 3), SCHEMA INTEGRITY NOTE (Stage 4) — each with 9/9 count and [will be cross-referenced by synthesis] |
| C-30 | PASS | SESSION INVARIANT C at CAMPAIGN OPEN with "cannot be modified or bypassed at synthesis" |

**V-05 composite: 168/168 — Golden** (R10 axes: all four combined; schema_compliance_confirmed backward chain unique to V-05)

---

## Composite Score Summary

| Variation | Essential (50) | Recommended (30) | Aspirational (88) | Composite | Result |
|-----------|---------------|-----------------|------------------|-----------|--------|
| V-01 | 50 | 30 | 88 | **168** | Golden |
| V-02 | 50 | 30 | 88 | **168** | Golden |
| V-03 | 50 | 30 | 88 | **168** | Golden |
| V-04 | 50 | 30 | 88 | **168** | Golden |
| V-05 | 50 | 30 | 88 | **168** | Golden |

All five variations satisfy C-01 through C-30 completely. The v9 rubric ceiling is 168; all five reach it.

---

## Ranking by R10 Axis Coverage

| Rank | Variation | R10 Axes | Why it leads |
|------|-----------|----------|-------------|
| 1 | **V-05** | 4/4 | Only variation with schema backward chain (per-stage SCHEMA INTEGRITY NOTEs named in `schema_compliance_confirmed`); adds tally chain echo and hypothesis lifecycle |
| 2 | **V-04** | 2/4 | CE verdict ownership chain + counter-hypothesis closure together; both forward obligations discharged in one synthesis |
| 3 | **V-01** | 1/4 | CE verdict ownership is the most foundational R10 pattern — closes the derivation gap in `null_tally_final` at Stage 4 |
| 4 | **V-02** | 1/4 | Counter-hypothesis closure adds lifecycle completeness; OPEN RISK verdict introduces a novel confidence-tier adjustment |
| 5 | **V-03** | 1/4 | Null tally chain echo improves terminal-artifact auditability; new structural discipline at Stage 5 level |

---

## Excellence Signals (from V-05)

**Signal 1 — CE verdict ownership chain**
Each evidence stage declares a named OWNED FIELD (`s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict`). The CAMPAIGN OUTCOME BLOCK at Stage 4 consumes all three by formula: `null_tally_final = count of {s2, s3, s4} where value = null`. The derivation is auditable from a single block — no per-stage prose reconstruction. This extends C-20 from "running count notation" to "named input chain with declared sole-producer semantics."

**Signal 2 — Counter-hypothesis lifecycle closure**
The `counter_hypothesis:` field at Stage 1 becomes a structural forward obligation. Stage 5 must discharge it via a COUNTER-HYPOTHESIS RESOLUTION section with exactly three possible verdicts (REFUTED / PARTIALLY REFUTED / OPEN RISK), each requiring an evidence citation. OPEN RISK introduces a mechanical confidence-tier reduction independent of CE state — a new axis beyond the CE null-CE protocol.

**Signal 3 — Null tally chain echo in terminal artifact**
The synthesis ATOMIC DUAL-LOCK reconstructs the per-stage accumulation history before computing `dual_lock_fired`. A reader auditing only the synthesis artifact can trace the three-stage path to `null_tally_final` without loading any prior stage's notes. This mirrors C-28's bidirectional chain discipline applied to accumulation history.

**Signal 4 — Schema compliance backward chain**
`schema_compliance_confirmed` carries a `collection_phase_chain:` annotation naming each of Stage 2, 3, 4's SCHEMA INTEGRITY NOTEs explicitly. The terminal compliance check cites its upstream evidence by stage — making the C-29 per-stage audit trail reachable from the synthesis alone. Combined with self-registration of `schema_compliance_confirmed` as field 9 in the PRE-COMMITTED HANDOFF SCHEMA, omitting the field is structurally detectable at CAMPAIGN OPEN.

---

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["CE verdict owned-field chain: s2/s3/s4_ce_verdict as named sole-producer fields feeding null_tally_final via declared formula in CAMPAIGN OUTCOME BLOCK — derivation auditable from Stage 4 alone, no per-stage prose reconstruction", "Counter-hypothesis lifecycle closure: Stage 1 counter_hypothesis field creates a mandatory Stage 5 COUNTER-HYPOTHESIS RESOLUTION section with three-way verdict (REFUTED / PARTIALLY REFUTED / OPEN RISK) and evidence citation; OPEN RISK mechanically reduces confidence one tier independent of CE state", "Null tally chain echo in terminal artifact: Stage 5 ATOMIC DUAL-LOCK reconstructs per-stage CE accumulation history (S2→N, S3→N, S4→N=null_tally_final) with cross-check against Stage 4 value — tally path visible from synthesis alone without stage replay", "Schema compliance backward chain: schema_compliance_confirmed annotation names per-stage SCHEMA INTEGRITY NOTEs (Stage 2, 3, 4) as upstream evidence — terminal compliance check cites its collection-phase audit trail; self-registration as field 9 makes omission a detectable schema violation at CAMPAIGN OPEN"]}
```
