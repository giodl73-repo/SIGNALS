Rubric written to `simulations/quest/rubrics/trace-inspect-rubric-2026-03-17.md`.

**Structure summary:**

**Essential (5)** — all must pass for the trace to be useful:
- **C-01** Phase completeness — all 4 phases present and structurally closed
- **C-02** Artifact produced — hand-compiled file written with all required sections
- **C-03** Schema 1 + 2 compliance — only {P1/P2/P3} severity, {SA/SG/EG/QO} source, label lock invariant holds
- **C-04** Enforcement gates checked — G-1/G-2/G-3 at Step 3c, no gate skipped or advanced past a FAIL
- **C-05** Verdict classified — USEFUL/NEEDS-REDESIGN/NEEDS-SPEC-REVISION with rationale consistent with gap inventory

**Recommended (3):**
- **C-06** SA-TO-SG promotion evaluated per gap
- **C-07** Per-role relays with all required fields including Schema 2 compliance
- **C-08** Findings table depth (>=3 findings, >=2 source types, distinct Actions)

**Aspirational (2):**
- **C-09** Full VC compliance ledger with specific observed values
- **C-10** Schema 5 sub-step transition sentences explicit
d input bindings and per-role schema binding blocks; Phase 2 (Execute) runs at least one role relay; Phase 3 (Findings) runs all four sub-steps in order (3a -> 3b -> 3c -> 3d); Phase 4 (Amend) produces at least one change or dismissal entry. A trace missing any phase, or a phase present but producing no required output, fails. |
| C-02 | **Artifact produced** | essential | correctness | Phase 2 (Execute) writes a hand-compiled artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md` (or equivalent declared path). The artifact contains every section the skill's artifact contract requires. An Execute phase that produces role relays without a written artifact fails. |
| C-03 | **Schema 1 + Schema 2 compliance** | essential | correctness | Every severity label used anywhere in the trace is from {P1, P2, P3}. Every Source label used anywhere in the trace is from {SA, SG, EG, QO}. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION. Any label outside these sets, or a promoted gap retaining SA, is a structural violation and fails this criterion. |
| C-04 | **Enforcement gates checked** | essential | behavior | Step 3c records an explicit PASS or FAIL result for each of G-1, G-2, and G-3. G-1: >= 2 distinct Source types in Step 3b table. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A trace where any gate is omitted, implicitly assumed to pass, or advanced past despite a FAIL result fails this criterion. |
| C-05 | **Verdict present and classified** | essential | correctness | Phase 5 (or Verdict section) delivers one of three classifications: USEFUL, NEEDS-REDESIGN, or NEEDS-SPEC-REVISION, with the decision rationale. The classification follows the defined rules: NEEDS-SPEC-REVISION if any P1 SA gap remains SA after promotion; NEEDS-REDESIGN if EG gaps exceed 3 and indicate a structural role gap; USEFUL otherwise. A trace ending without a verdict, or with a verdict that contradicts the gap inventory, fails. |

---

## Recommended Criteria

> Output is better with these. Failing one degrades quality but does not make the trace useless.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|---------------|
| C-06 | **SA-TO-SG promotion evaluated** | recommended | depth | Every SA gap from the Stage 1 relay is evaluated at the SA-TO-SG PROMOTION lifecycle event. Each gap records PROMOTES TO SG or REMAINS SA with a one-sentence reason. The post-promotion inventory states SA remaining count and SG from promotion count. A trace with SA gaps that skip this evaluation, or where all SA gaps silently disappear without a promotion record, fails this criterion. |
| C-07 | **Per-role relays complete** | recommended | coverage | Each role in the execution sequence has a relay in Phase 2 with all required fields: Received from, Received values, Schema 2 compliance (Source labels used and YES/NO conformance), SA/SG gaps affecting this role, Produced (artifact content added), EG gaps encountered. A relay missing the "Schema 2 compliance" field, or a relay summarized as "role ran normally" without field-level detail, fails this criterion. |
| C-08 | **Findings table depth** | recommended | depth | The Step 3b findings table contains >= 3 distinct findings covering at least 2 different Source types. Each finding has a distinct Action (not a restatement of the finding). A table with only spec-layer (SA) findings or only execution-layer (EG) findings, or with Action cells that repeat the Finding text verbatim, fails this criterion. |

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|---------------|
| C-09 | **Compliance ledger populated** | aspirational | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results -- it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transitions explicit** | aspirational | behavior | Each of the four Phase 3 sub-steps (3a, 3b, 3c, 3d) states its Schema 5 prerequisite and its Schema 5 transition sentence confirming the prerequisite was satisfied before the sub-step began. A trace that runs sub-steps without recording the transition (e.g., jumps from Step 3a directly to Step 3b content without stating "Step 3a complete, Step 3b is valid to begin") fails this criterion. |

---

## Scoring Summary

| Tier | Criteria | Points available |
|------|----------|-----------------|
| Essential (all must pass) | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07, C-08 | 30 |
| Aspirational | C-09, C-10 | 10 |

**Composite** = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Patterns to Watch

| Pattern | Likely criterion violated |
|---------|--------------------------|
| Phases present but artifact file not written | C-02 |
| Severity labels like "high/medium/low" or "critical" used | C-03 |
| Source labels like "spec gap" or "runtime" used | C-03 |
| Phase 4 entered with a G-1 FAIL still active | C-04 |
| Verdict states USEFUL despite unresolved P1 SA gaps | C-05 |
| SA gaps listed in Stage 1 but SA-TO-SG evaluation skipped | C-06 |
| Role relays present but missing Schema 2 compliance field | C-07 |
| Findings table has all SA findings, no EG or SG | C-07, C-08 |
| Compliance ledger rows say "as expected" without specifics | C-09 |
| Sub-steps run without transition sentences | C-10 |
