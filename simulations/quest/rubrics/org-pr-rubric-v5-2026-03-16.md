Reading the scorecard carefully to extract the R4 excellence signals before writing the new criteria.

The four signals are:

1. **Locator self-correction gate** — clarifies C-08 (existing recommended): `if NO → rewrite → include` branch is the gate; prohibition alone is not
2. **Verdict hardening pair** — C-11 + C-14 must co-occur; one without the other leaves a decision space gap → **C-19**
3. **Priority table as composition mechanism** — prose rules don't scale past 2 axes; table with governance-domain labels scales to N → **C-20**
4. **Authority-inertia reconciliation** — if-stays projections from lower-authority roles must be declared compounding cost, not counter-findings → **C-21**
5. **Conflict resolution column** (unsealed C-07 gap / R5 hypothesis) — authority chain already resolves conflicts mechanically; wiring it back as a Resolution column closes C-07 → **C-22**

C-08 pass condition tightens (tier stays recommended). Aspirational pool: 8 → 12.

---

```markdown
---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 5
supersedes: org-pr-rubric-v4-2026-03-16.md
---

# Scoring Rubric — org-pr

**Skill**: org-pr  
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Changelog (v4 -> v5)

Four new aspirational criteria extracted from R4 excellence signals. One existing recommended
criterion (C-08) has its pass condition tightened; no tier change.

**C-08 pass condition tightened**: R4 confirmed that declaring invalidity is not a gate —
the `if locator invalid → rewrite → include` branch instruction is the gate. Prompts that
prohibit invalid locators without providing the branch have scored PARTIAL in every round.
Pass condition now requires the explicit branch; prohibition alone scores PARTIAL.

**C-19** (verdict hardening pair): Formula lock (C-11) and escape closure (C-14) must
co-occur. A locked formula combined with unspecified escape still permits a P1 + Go claim
— the formula is closed but the decision space is not. R4 V-04 reached PARTIAL on both;
V-05 was the first to PASS both in the same prompt. PASS requires both a formula lock
instruction AND an explicit escape closure instruction present together. PARTIAL if only one
is present.

**C-20** (priority table as composition mechanism): When N≥3 axes are composed, prose
conflict rules produce ambiguous precedence chains — a rule for axis A over B and B over C
does not mechanically handle A vs. C under a novel constraint. The R4 excellence signal is
the table structure (axis / governance domain / yields-to): it assigns each axis a
non-overlapping governance domain and makes tiebreakers deterministic at any N. PASS
requires a table when 3+ axes are present. Prose conflict rules with 3+ axes score PARTIAL.
N/A for prompts with fewer than 3 axes (counts as PASS).

**C-21** (authority-inertia reconciliation rule): Without an explicit reconciliation
statement, a lower-authority role's if-stays projection reads as a counter-finding against
the upstream constraint — destabilizing the authority sequence. The R4 excellence signal:
"inertia framing describes the compounding cost of an upstream finding going unresolved, not
a reclassification of the finding." This declaration resolves the three-way tension between
authority chain, inertia framing, and finding format. PASS requires this declaration or
equivalent. N/A if no inertia axis (counts as PASS).

**C-22** (conflict resolution column — R5 hypothesis): All four rounds of C-07 are PARTIAL
because the conflict table names who disagrees on what surface but provides no resolution
instruction. The authority chain already resolves conflicts mechanically: the role with the
higher authority position in the declared sequence governs. C-22 tracks whether the conflict
output template is wired to this mechanism — a "Resolution" column or field populated by
authority position. This is the R5 hypothesis for closing C-07. PASS requires the conflict
output template to include a resolution field with authority-position logic. N/A if no
conflict analysis is instructed (counts as PASS).

Aspirational pool grows from N=8 to N=12. No changes to essential or recommended tiers
beyond C-08 pass condition.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 12

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Multi-role coverage | coverage | 2+ labeled sections from defined role set, each with a finding |
| C-02 | P1/P2/P3 on every finding | correctness | Zero untagged findings |
| C-03 | File-based role selection rationale | correctness | Each role's inclusion tied to specific changed files |
| C-04 | Explicit go/no-go recommendation | correctness | Labeled verdict block, derivable from findings |
| C-05 | Per-role structure / no bleeding | format | Each section opens with role-name heading; sections cannot bleed |

---

## Recommended Criteria (weight: 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Projection-aware consensus | correctness | Consensus block includes projection (future-state impact) in the ALIGNED/DIVERGENT call; not just current-state summary |
| C-07 | Conflict analysis | correctness | Named conflict table with disagreeing roles, disputed surface, and resolution; PARTIAL if table present but resolution omitted |
| C-08 | Locator self-correction gate | correctness | Explicit `if locator invalid → rewrite → include` branch instruction; prohibition without the branch scores PARTIAL |
| C-09 | Phase/lifecycle gating | correctness | Review instruction gated to phase or lifecycle state of the feature (e.g., pre-merge, pre-deploy) |
| C-10 | Downstream risk field | format | Each finding includes an explicit downstream risk or cascading effect field |

---

## Aspirational Criteria (weight: 10 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-11 | Formula lock | correctness | Verdict formula explicitly closed: no override or modification path permitted |
| C-12 | Named invalid forms | correctness | Invalid locator or finding forms named with examples, not just prohibited |
| C-13 | Inertia / if-stays framing | format | Each finding includes an if-stays projection describing what happens if the finding goes unresolved |
| C-14 | Verdict escape closure | correctness | All escape paths from the verdict explicitly named and closed |
| C-15 | Projection convergence call | correctness | Consensus block contains explicit ALIGNED or DIVERGENT call on projection direction across roles |
| C-16 | Self-correction gate pre-commit | correctness | Pre-commit self-check instruction embedded; model instructed to verify all criteria before output |
| C-17 | Role authority sequence declaration | correctness | Review order declared with explicit authority rationale: blocking roles (security, schema) sequenced before advisory roles (DX, docs), principle stated |
| C-18 | Axis conflict resolution rule | correctness | Explicit tiebreaker rule stating which axis governs when two axes conflict; N/A for single-axis prompts (counts as PASS) |
| C-19 | Verdict hardening pair | correctness | Formula lock (C-11) and escape closure (C-14) both present in same prompt; one present without the other scores PARTIAL |
| C-20 | Priority table as composition mechanism | format | When 3+ axes present: conflict resolution expressed as table (axis / governance domain / yields-to), not prose; prose rules at N≥3 score PARTIAL; N/A for fewer than 3 axes (counts as PASS) |
| C-21 | Authority-inertia reconciliation rule | correctness | Explicit declaration that lower-authority if-stays projections describe compounding cost of upstream findings, not counter-findings; N/A if no inertia axis (counts as PASS) |
| C-22 | Conflict resolution column | correctness | Conflict output template includes a resolution field populated by authority position (higher-authority role governs); N/A if no conflict analysis instructed (counts as PASS) |
```

---

**What changed and why:**

| Change | Reason |
|--------|--------|
| C-08 tightened | Branch instruction is the gate; prohibition alone has been PARTIAL in every round |
| C-19 (verdict hardening pair) | R4 V-04/V-05 showed one without the other leaves a gap; they behave as a logical unit |
| C-20 (priority table) | Prose rules at N≥3 produce implicit A→B→C chains; table with governance domains is the only structure that scales mechanically |
| C-21 (authority-inertia reconciliation) | Without it, if-stays projections from lower roles read as counter-findings; the reconciliation declaration is what makes inertia + authority-chain composition stable |
| C-22 (conflict resolution column) | Direct R5 hypothesis for closing the four-round C-07 PARTIAL; authority chain already has the answer — wiring it to the output template is all that is needed |
