## Round 9 Scorecard — topic-open (v7)

**Base**: R8 V-05 — passes C-01 through C-30 (all v7 criteria) plus R8 prospective C-31 through C-34.
**Rubric**: v7, denominator 22 aspirational. Scoring formula: Essential (5) × 60% + Recommended (3) × 30% + Aspirational (22) × 10%.

---

### Criteria Reference

| Tier | IDs | Weight | Max points |
|------|-----|--------|-----------|
| Essential | C-01–C-05 | 60% | 60 |
| Recommended | C-06–C-08 | 30% | 30 |
| Aspirational | C-09–C-30 | 10% | 10 |

---

### V-01 — Multi-Phase Exit Gates

**Essential (C-01–C-05)**: All PASS. Inherited from R8 V-05 base; V-01 does not modify essential output structure.
- C-01 PASS: ROW TEMPLATE + TOPICS.md append instruction fully present.
- C-02 PASS: `simulations/{topic}/strategy.md` path instruction explicit.
- C-03 PASS: Five-field schema defined, Phase 2 gate enforces completeness.
- C-04 PASS: VOCABULARY LOCK at top of skill; Phase 2 gate item uses exact-string-match language.
- C-05 PASS: Phase 2 gate COV-01 checks for >= 1 essential row.

**Recommended (C-06–C-08)**: All PASS. Phase 2 exit gate carries COV-02 (namespaces), COV-03 (owner roles), and rationale check. None affected by V-01's axis.

**Aspirational (C-09–C-30)**: All PASS.
- C-11 PASS: VOCABULARY LOCK is a standalone block before all phase instructions.
- C-12 PASS: Phase 5 self-check present (C-01 through C-05 with AMEND blocks).
- C-25 PASS: All Phase 2 gate items and Phase 1 exit gate item cite tool + what it checks (two-slot citation).
- C-26 PASS: Phase 4 ordering instructions carry inline if/if; no delegation to tables.
- C-27 PASS: All five phase decision tables present.
- C-28 PASS: DECISION TABLE SCHEMA declares uniform Path/Action/Consequence grammar before Phase 1.
- C-29 PASS: Gate checklist items at Phase 1, 2, 3, 4 all name tool + enforcement mechanism.
- C-30 PASS: Phase 4 if/if instructions are self-contained; no "see Phase X Decision" delegation.
- C-31 PASS: Phase 5 AMEND blocks use uniform `AMEND — {CONDITION NAME}` labels for all five essential criteria.
- C-32 PASS: Phase 2 GATE FAILURE names return phase, repair action, re-run condition.
- C-33 PASS: Recovery Path column present in all five DEFAULTS rows.
- C-34 PASS: DEFAULTS Recovery Path and Phase 5 AMEND blocks carry independent repair procedures.

**Prospective assessment**:
- C-35 (multi-phase gate completeness): **PASS** — Phase 1 terminal gate, Phase 3 and Phase 4 return-to-repair gates, each with GATE FAILURE routing. Gate coverage is now uniform across all four procedural phases.
- C-36 (Phase 5 covers C-01–C-08): **FAIL** — Phase 5 self-check covers only C-01 through C-05; C-06/C-07/C-08 have no AMEND blocks.
- C-37 (worked example in schema): **FAIL** — FIELD SCHEMA is abstract only; no concrete example row; no example COMMIT GATE.

**Score: 100/100** (5/5 essential, 3/3 recommended, 22/22 aspirational)
**Prospective coverage: 1/3** (C-35 only)

---

### V-02 — Extended Phase 5 Self-Check

**Essential (C-01–C-05)**: All PASS. No change to essential output structure vs base.

**Recommended (C-06–C-08)**: All PASS. Phase 2 exit gate coverage unchanged; additionally all three now have Phase 5 AMEND blocks.

**Aspirational (C-09–C-30)**: All PASS.
- C-12: PASS — Phase 5 now covers C-01 through C-08 (all essential + all recommended) with named AMEND blocks. The self-check is a uniform repair protocol across all eight criteria.
- All other aspirational criteria carry over from base without regression. V-02 does not add phases, does not modify phase decision tables, does not touch DEFAULTS or VOCABULARY LOCK.

**Prospective assessment**:
- C-35: **FAIL** — No Phase 1/3/4 exit gates added; only Phase 2 has gate + GATE FAILURE routing.
- C-36: **PASS** — Phase 5 covers C-01 through C-08 with `AMEND — {CONDITION NAME}` blocks using the same uniform format established for essential criteria. C-06 AMEND → "MONOCULTURE NAMESPACE", C-07 AMEND → "THIN RATIONALE", C-08 AMEND → "DEGENERATE OWNERSHIP".
- C-37: **FAIL** — No worked example in FIELD SCHEMA or Phase 3.

**Score: 100/100**
**Prospective coverage: 1/3** (C-36 only)

---

### V-03 — Worked Example in FIELD SCHEMA

**Essential (C-01–C-05)**: All PASS. Worked examples are additive; they do not modify instruction logic.

**Recommended (C-06–C-08)**: All PASS. No change to Phase 2 gate structure.

**Aspirational (C-09–C-30)**: All PASS.
- C-10: PASS — The example row in FIELD SCHEMA uses `my-topic-competitors-2026-01-15.md`, which correctly demonstrates the `{topic}-{signal}-{date}.md` pattern. The example COMMIT GATE lists two item names matching that pattern exactly. Neither example uses abstract placeholders for field values.
- All other aspirational criteria carry over from base. V-03 does not add phase gates, does not modify decision tables, does not modify VOCABULARY LOCK.

**Prospective assessment**:
- C-35: **FAIL** — No multi-phase exit gates.
- C-36: **FAIL** — Phase 5 covers only C-01 through C-05.
- C-37: **PASS** — FIELD SCHEMA contains a concrete filled-in example row with `essential` / `scout` / `scout-competitors` / `my-topic-competitors-2026-01-15.md` / `Product Manager`. Phase 3 template is followed by an example COMMIT GATE listing two essential signals by exact item name. Both examples use fixed, readable values without abstract placeholders.

**Score: 100/100**
**Prospective coverage: 1/3** (C-37 only)

---

### V-04 — V-01 + V-02 (Multi-Phase Gates + Extended Self-Check)

**Essential (C-01–C-05)**: All PASS. Both axes are additive to different parts of the skill; no interaction modifies essential output path.

**Recommended (C-06–C-08)**: All PASS. Phase 2 gate unchanged; Phase 5 now adds AMEND blocks for C-06/C-07/C-08.

**Aspirational (C-09–C-30)**: All PASS.
- C-12: PASS — Phase 5 covers C-01 through C-08. The self-check is comprehensive.
- C-29: PASS — Phase 1, 2, 3, 4 exit gate items all carry two-slot tool citations.
- C-35 target: Four phases have gates. Phase 5 has AMEND blocks covering all eight criteria. The repair graph is complete: every phase has a routing instruction for failure.
- No regression from combining axes. V-01 gates sit at the end of Phase 1/3/4 instruction bodies; V-02 AMEND blocks sit at the end of Phase 5. They occupy different positions in the skill body and do not interact.

**Prospective assessment**:
- C-35: **PASS** — Phase 1 terminal gate, Phase 3 and 4 return-to-repair gates, all with GATE FAILURE routing.
- C-36: **PASS** — Phase 5 covers all eight criteria with uniform AMEND blocks.
- C-37: **FAIL** — No worked example in FIELD SCHEMA or Phase 3.

**Composition finding**: V-01 and V-02 compose without regression. Phase-level gate routing and post-write criterion coverage are structurally independent — they close different failure modes (phase-exit routing vs criterion-level audit coverage). Neither axis creates redundancy with the other.

**Score: 100/100**
**Prospective coverage: 2/3** (C-35 + C-36)

---

### V-05 — Full Integration (V-01 + V-02 + V-03)

**Essential (C-01–C-05)**: All PASS. All three axes additive; no axis modifies essential output path.

**Recommended (C-06–C-08)**: All PASS. Phase 2 gate unchanged; Phase 5 AMEND blocks added for C-06/C-07/C-08.

**Aspirational (C-09–C-30)**: All PASS.
- C-10: PASS — Example row in FIELD SCHEMA and example COMMIT GATE both demonstrate correct `{topic}-{signal}-{date}.md` format with concrete values.
- C-12: PASS — Phase 5 covers C-01 through C-08 comprehensively.
- C-28: PASS — DECISION TABLE SCHEMA declares uniform column grammar; all five phase tables use it; the example rows in FIELD SCHEMA and Phase 3 do not introduce any new table grammar.
- C-29: PASS — All phase exit gate items carry tool + mechanism.
- C-35 target: All four procedural phases have exit gates with GATE FAILURE routing.
- C-36 target: Phase 5 AMEND covers all eight criteria.
- C-37 target: FIELD SCHEMA has example row; Phase 3 has example COMMIT GATE.

**Composition check — Phase 3 example vs Phase 3 exit gate checklist (the specific adjacency concern noted in the R9 axis description)**:

In V-05, Phase 3 body reads: (1) isolation instruction + if/if, (2) template with abstract placeholders, (3) example COMMIT GATE with concrete values, (4) tool-consequence note, (5) Phase 3 Exit Gate checklist. The example (item 3) demonstrates structural format; the exit gate (item 5) confirms the current-instance gate was executed correctly. These are two different operations: the example is a reference artifact for construction; the gate is a confirmation instrument for the produced output. A model reading Phase 3 can use the example to validate its gate's format before the exit gate confirms the gate exists and is complete. **No conflict; complementary functions.**

**Score: 100/100**
**Prospective coverage: 3/3** (C-35 + C-36 + C-37)

---

### Rankings

| Rank | Variation | Score | Prospective |
|------|-----------|-------|-------------|
| 1 | V-05 | 100/100 | 3/3 (C-35 + C-36 + C-37) |
| 2 | V-04 | 100/100 | 2/3 (C-35 + C-36) |
| 3 | V-01 | 100/100 | 1/3 (C-35) |
| 3 | V-02 | 100/100 | 1/3 (C-36) |
| 3 | V-03 | 100/100 | 1/3 (C-37) |

All five variations pass the v7 rubric at 100/100. Differentiation is entirely in prospective criterion coverage. V-05 is the clear top variation — it is the only one to demonstrate all three prospective axes and confirm they compose without regression.

---

### Excellence Signals from V-05

**Signal 1 — Full-phase gate grammar (C-35)**
V-05 demonstrates that a model executing this skill encounters no phase boundary without a routing instruction for failure. Phase 1 is terminal (stop + redirect options given). Phases 2/3/4 are return-to-repair (return phase named, repair action specified, re-run condition given). Phase 5 does not exit — it is the audit layer. The gate grammar is now spatially uniform: every procedural phase body ends with an Exit Gate checklist and a GATE FAILURE line. A model does not need to know which phase has gate coverage — all of them do.

**Signal 2 — Phase 5 as a full-criteria audit surface (C-36)**
V-05 extends Phase 5 from an essential-only check to a complete eight-criteria audit with uniform AMEND labels. The structural insight: Phase 2's exit gate is a pre-write verification (confirms the table is ready before files are flushed); Phase 5 is a post-write audit (confirms the actual files match what was intended). These are different verification moments for the same criteria — a table that passes Phase 2 can be degraded during Phase 3/4 work. Phase 5 covering C-06/C-07/C-08 closes the window between Phase 2 gate and file write. The AMEND blocks follow the exact same `AMEND — {CONDITION NAME}` format as C-01 through C-05, making Phase 5 a uniform repair protocol with no formatting variance across all eight criteria.

**Signal 3 — Example as a pre-construction reference channel (C-37)**
V-05 adds a concrete example row to FIELD SCHEMA and a concrete example COMMIT GATE to Phase 3. The structural insight: F-04 naming errors are the most consequential schema errors (they make signals invisible to discovery with no error), but FIELD SCHEMA defines the pattern abstractly. A concrete example row provides a second verification channel at schema-read time — before Phase 4 gate, before Phase 5 AMEND, before `topic-scanner` fails silently. The example is explicitly labeled as replaceable (`my-topic` → actual slug, `2026-01-15` → today's date), so it instructs without being prescriptive.

**Signal 4 — Phase 3 example and Phase 3 exit gate are complementary, not redundant**
The Phase 3 body now contains both an example COMMIT GATE (concrete format demonstration) and a Phase 3 Exit Gate checklist (current-instance execution confirmation). These serve different functions at the same phase: the example shows what a correctly populated gate looks like; the gate checklist confirms the gate was written as a standalone heading with all essential signals listed. A model uses the example to construct correctly, then uses the gate to confirm. No redundancy — two verification operations on the same phase output with different inputs (the example reads a reference artifact; the gate reads the model's produced output).

---

### Prospective Criteria Promoted

All three R9 prospective criteria are confirmed by the isolation experiments:

**C-35** — Multi-phase gate completeness: Every procedural phase (1–4) has a formal exit gate checklist and GATE FAILURE routing. Phase 1's GATE FAILURE is terminal (stop + redirect to `/topic-plan` or new slug); Phases 2–4 are return-to-repair (return phase named + repair action + re-run condition).

**C-36** — Phase 5 covers all eight criteria: Post-generation self-check includes C-06, C-07, and C-08 with `AMEND — {CONDITION NAME}` blocks in the same uniform format as C-01 through C-05. Phase 5 is a complete repair protocol, not an essential-only audit.

**C-37** — Worked example in schema: FIELD SCHEMA contains a concrete filled-in example row demonstrating all five fields with a valid `{topic}-{signal}-{date}.md` item name. Phase 3 COMMIT GATE template is followed by an example with at least two essential signals listed by exact item name. Neither example uses abstract placeholders for field values.

Denominator advances from 22 → 25.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 3 example COMMIT GATE and Phase 3 exit gate checklist are complementary not redundant — the example provides a reference artifact for construction-time format validation; the gate confirms current-instance execution correctness; two verification operations at the same phase serve different functions and compose without conflict", "Full-phase gate grammar closes all phase boundaries — every procedural phase body ends with an exit gate checklist and a GATE FAILURE routing instruction; Phase 1 is terminal, Phases 2/3/4 are return-to-repair; a model encounters no phase transition without knowing exactly what to do if the transition condition is not met"]}
```
