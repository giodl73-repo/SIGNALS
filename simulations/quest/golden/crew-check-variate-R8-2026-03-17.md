---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 8
rubric: crew-check-rubric-v7-2026-03-17.md
---

# crew-check — Variate R8

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds).

Rubric v7 floor (all variations must hold):
- Essential: C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability,
  C-08 severity calibration consistency
- Aspirational v6: C-09 through C-23 (cross-role synthesis, AMEND, lens-anchoring,
  severity calibration contract, challenger-first, readiness-gate, severity-sorted output,
  hard-halt gates, named halt IDs, gate-audit sub-command, self-routing halts,
  executable audit output, run health certificate, three-tier halt scope, pre-committed skip-map)

New criteria targeted in R8:
- C-24: Dual-axis calibration contract (confidence scale pre-committed alongside severity,
  in matrix schema, as sort key, as readiness modifier)
- C-25: Named convergence tier register (CORROBORATED/CONFIRMED with formal distinguishing
  criteria, Confidence=LOW findings separately enumerated)
- C-26: Artifact maturity stage pre-condition (G0.5 fires BLOCKING before G1 on absent/
  unrecognized stage; G0.5 appears in HALT REGISTRY before G1 entry)
- C-27: Stage-scoped matrix and readiness filter (STAGE-APPROPRIATE with 4 values including
  DEPRECATED; scope-grouped matrix; Gate 7 reads only YES-scope rows; DEPRECATED=automatic
  READY; `--amend stage:{value}` in AMEND block)

Design intent for R8: R7 introduced the three axes (inertia framing, confidence tier,
lifecycle stage) but each with gaps against the v7 rubric. V-01 tightens C-24 by making
confidence a pre-committed contract with equal structural weight to severity. V-02 tightens
C-25 by formalizing the CONFIRMED/CORROBORATED distinction on confidence alignment (not
just role count) and explicitly enumerating Confidence=LOW findings. V-03 tightens C-26+C-27
by adding DEPRECATED as the fourth STAGE-APPROPRIATE value, scope-grouping the matrix before
severity sort, and adding `--amend stage:{value}`. V-04 and V-05 combine axes.

Axes selected for R8:
- V-01: C-24 only — dual-axis calibration (confidence scale pre-committed with named tiers,
  in matrix schema, as secondary sort key; CONFIRMED findings at Confidence=HIGH treated as
  HIGH-effective in readiness verdict)
- V-02: C-25 only — named convergence tier register (CORROBORATED=same surface 2+ roles;
  CONFIRMED=same surface + matching confidence tier 2+ roles; Confidence=LOW separately
  enumerated at Gate 9; presupposes C-24)
- V-03: C-26+C-27 combined — stage pre-condition (G0.5 before G1 in HALT REGISTRY) plus
  stage-scoped matrix (four STAGE-APPROPRIATE values, scope-grouped matrix, Gate 7 reads
  YES only, DEPRECATED=READY, `--amend stage:{value}`)
- V-04: C-24 + C-25 — full dual-axis calibration + named convergence register
- V-05: C-24 + C-25 + C-26 + C-27 + IC-CHALLENGED — full integration of all four new
  criteria plus R7 inertia framing (IC-CHALLENGED column, INERTIA CLAIM REGISTRY,
  CHALLENGE RESPONSE MAP)

---

## V-01

**Axis**: C-24 — Dual-axis calibration contract
**Hypothesis**: C-12 (severity calibration contract, part of the v6 floor) locks severity
values before reviewers run. Findings within a severity tier are unordered — a HIGH finding
based on direct artifact text and a HIGH finding based on speculation receive identical weight
in the readiness verdict. V-01 R8 extends the pre-execution calibration contract to include
a confidence scale with equal structural rigor: named tiers, operational criteria, and
consequences locked before Gate 1. Confidence appears in every finding row, governs the
secondary sort axis (severity DESC, confidence DESC within tier), and feeds the readiness
verdict: findings at MEDIUM severity with Confidence=HIGH are CONFIRMED and treated as
HIGH-effective in Gate 7. The claim: when confidence is pre-committed with the same formal
weight as severity, reviewers distinguish "what might be wrong" from "what is evidenced to
be wrong" — and the readiness verdict reflects that distinction mechanically.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
```

Acknowledge injected values before executing any gate.

---

### PRE-EXECUTION: SEVERITY AND CONFIDENCE CALIBRATION CONTRACT

Lock both scales before any reviewer runs. Both appear in every finding row.
No values outside these tables are permitted.

**Severity scale:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence scale:**
| Label  | Score | Operational meaning                                                       |
|--------|-------|---------------------------------------------------------------------------|
| HIGH   | 3     | Directly evidenced: cited text, field, or schema element in artifact      |
| MEDIUM | 2     | Inferred from structural pattern or omission; no direct citation possible |
| LOW    | 1     | Speculative or risk-based; no direct artifact evidence exists             |

Matrix sort: severity DESC (primary), confidence DESC within severity tier (secondary).

Readiness treatment: a finding at MEDIUM severity with Confidence=HIGH is a CONFIRMED
finding — treated as HIGH-effective in Gate 7 (confidence eliminates evidential uncertainty
that normally makes MEDIUM conditional).

Invalid severity label: HALT [G4c-{role}] BLOCKING.
Invalid confidence label: HALT [G4f-{role}] BLOCKING.
Absent confidence column: HALT [G4g-{role}] DEFERRED.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4f-{role}    | Confidence `{value}` not in calibration contract    | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row           | DEFERRED |
| G5            | Zero findings produced across all roles             | BLOCKING |

BLOCKING: full stop. No output beyond the halt message.
SCOPED: triggering role excluded from matrix; run continues for remaining roles.
DEFERRED: finding row included with [DEFERRED] tag; readiness verdict forced to CONDITIONAL.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                               |
|-----------------------------|------------|-------------------|------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified in prior run                    |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + named surface verified                 |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified            |
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4d           | Lens anchor + surface + severity + location verified |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f           | All prior sub-gates verified                         |

At re-entry time, state which sub-gates are being skipped and cite the prerequisite.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with selection rationale.
State total role count before Gate 3.

---

### EXECUTION

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING — no output follows)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
No other values permitted for either scale.
Matrix sort: severity DESC, confidence DESC within tier.
CONFIRMED (Severity=MEDIUM, Confidence=HIGH) treated as HIGH-effective in readiness verdict."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate runs first. State what the team does today without `{{artifact}}` and
why that is acceptable. Name >= 2 specific status-quo strengths.
Emit: "Status quo registered. Domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor* (required before any finding):
"From the [role] perspective, this review examines [specific surface of {{artifact}}]."
On missing:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart; no sub-gates skipped)
```

*G4b — Surface finding*: Every finding must name a specific artifact surface.
Format: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped — lens anchor verified in prior run)
```

*G4c — Severity validation*: On first invalid severity label:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*: Every recommendation must include a location
reference (section name, field, or line reference in `{{artifact}}`). On missing:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4f — Confidence validation*: On first invalid confidence label:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a–G4d skipped)
```

*G4g — Confidence column presence*: Every finding row must carry a populated Confidence
value. A row with absent or blank Confidence triggers G4g DEFERRED:
```
HALT [G4g-{role}]: Confidence column absent from finding row — row included as [DEFERRED].
→ Readiness verdict will be forced to CONDITIONAL for this run.
→ To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a–G4f skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly: severity-confidence sort**

Assemble all staged finding rows. Sort: severity DESC (primary), confidence DESC
(secondary within severity tier). Append [DEFERRED] to G4g-affected rows.

Schema: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`

If zero findings from all non-excluded roles:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:   [N] findings ([N] Confidence=HIGH, [N] MEDIUM, [N] LOW)
  MEDIUM: [N] findings
    └ CONFIRMED (Severity=MEDIUM, Confidence=HIGH): [N] — treated as HIGH-effective
  LOW:    [N] findings
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. Any HIGH-severity finding → BLOCKED.
2. Any CONFIRMED finding (Severity=MEDIUM, Confidence=HIGH) → HIGH-effective → BLOCKED.
3. Any MEDIUM finding (Confidence=MEDIUM or LOW), no HIGH or CONFIRMED → CONDITIONAL.
4. Any DEFERRED row → minimum CONDITIONAL.
5. All LOW or none of the above → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
If CONFIRMED findings contributed: append
`(confirmed evidence: [N] MEDIUM-severity Confidence=HIGH findings treated as HIGH-effective)`

**Gate 8 — Challenger: closing bracket**

Does the status quo hold? Name the strongest counter-evidence from the matrix. Note
whether any Confidence=HIGH findings directly refute the status-quo position stated at
Gate 3. Revise readiness recommendation if warranted.
Emit: "Inertia assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 cross-role convergence or conflict. Enumerate all Confidence=LOW
findings and state whether each warrants independent verification before acting on it.
Reference role names. No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run.

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3, G4a–G4g (all roles), G5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  CONFIRMED findings (HIGH-effective): [N]
  Result:        Matrix complete. Severity and confidence contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a
- `rerun:G4a-{role}` through `rerun:G4g-{role}` — re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID        | Trigger description                       | Tier     | Re-entry command                                     |
|----------------|-------------------------------------------|----------|------------------------------------------------------|
| [G4f-architect]| Confidence 'CERTAIN' not in contract      | BLOCKING | /crew-check {{artifact}} --amend rerun:G4f-architect |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.

---

## V-02

**Axis**: C-25 — Named convergence tier register (presupposes C-24)
**Hypothesis**: V-01 R8 makes confidence a pre-committed dimension. But agreement between
roles remains unlabeled: two roles citing the same surface with different confidence tiers,
and two roles citing the same surface with identical confidence tiers, both appear as
un-differentiated convergence in Gate 9 prose. V-02 R8 adds a PRE-EXECUTION FINDING
CONVERGENCE CONTRACT that formalizes exactly two convergence tiers with distinguishing
criteria. CORROBORATED requires only surface agreement across 2+ roles. CONFIRMED requires
surface agreement AND matching confidence tier across all citing roles. The distinction is
load-bearing: CONFIRMED findings at non-LOW confidence are HIGH-effective in Gate 7;
CORROBORATED are synthesis signals only. Separately, all Confidence=LOW findings — whether
CONFIRMED-LOW or SOLO — are enumerated at Gate 9 for cross-role verification before
action. The claim: when convergence levels are operationally defined before execution,
the synthesis gate emits a register rather than a narrative — agreement strength is as
mechanical as severity.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
```

Acknowledge injected values before executing any gate.

---

### PRE-EXECUTION: SEVERITY AND CONFIDENCE CALIBRATION CONTRACT

**Severity scale:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence scale:**
| Label  | Score | Operational meaning                                                       |
|--------|-------|---------------------------------------------------------------------------|
| HIGH   | 3     | Directly evidenced: cited text, field, or schema element in artifact      |
| MEDIUM | 2     | Inferred from structural pattern or omission; no direct citation possible |
| LOW    | 1     | Speculative or risk-based; no direct artifact evidence exists             |

Matrix sort: severity DESC (primary), confidence DESC within tier (secondary).

Invalid severity: HALT [G4c-{role}] BLOCKING.
Invalid confidence: HALT [G4f-{role}] BLOCKING.
Absent confidence: HALT [G4g-{role}] DEFERRED.

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

After the matrix (Gate 5.5), a FINDING CONVERGENCE REGISTER is emitted. Convergence is
defined per Surface value: two findings converge when they cite the same Surface from
different roles.

Tier assignment:
| Tier         | Criteria                                                           | Readiness effect                         |
|--------------|--------------------------------------------------------------------|------------------------------------------|
| CONFIRMED    | Same Surface, 2+ roles, ALL citing roles share the same Confidence tier, tier != LOW | HIGH-effective in Gate 7  |
| CONFIRMED-LOW| Same Surface, 2+ roles, ALL citing roles share Confidence=LOW      | Flagged for verification; NOT HIGH-effective |
| CORROBORATED | Same Surface, 2+ roles, Confidence tiers differ across citing roles | Convergence signal noted in Gate 9 only |
| SOLO         | Surface cited by exactly 1 role                                    | Normal weight                            |

Distinguishing criterion between CONFIRMED and CORROBORATED: confidence alignment.
CONFIRMED means roles not only agree on the problem surface but on the evidential basis
for the finding — making the combined finding stronger than any individual role's finding.
CORROBORATED means roles identify the same surface but from different evidential positions —
agreement on problem but not on certainty.

CONFIRMED findings at non-LOW confidence: treated as HIGH-effective in Gate 7 (convergent
direct evidence eliminates the uncertainty that normally makes MEDIUM severity conditional).
CONFIRMED-LOW: NOT HIGH-effective. Enumerated separately at Gate 9 for verification.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4f-{role}    | Confidence `{value}` not in calibration contract    | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row           | DEFERRED |
| G5            | Zero findings produced across all roles             | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                               |
|-----------------------------|------------|-------------------|------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified                                 |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + named surface verified                 |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified            |
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4d           | Lens anchor + surface + severity + location verified |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f           | All prior sub-gates verified                         |

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING — no output follows)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
Convergence tiers: CONFIRMED (same surface + matching confidence tier != LOW, 2+ roles)
  treated as HIGH-effective in Gate 7.
CORROBORATED (same surface, differing confidence tiers, 2+ roles) synthesis signal only.
CONFIRMED-LOW (same surface + matching LOW confidence, 2+ roles) flagged at Gate 9."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate runs first. State what the team does today without `{{artifact}}` and
why acceptable. Name >= 2 specific status-quo strengths.
Emit: "Status quo registered. Domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor*: "From the [role] perspective, this review examines [surface]."
On missing:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart)
```

*G4b — Surface finding*: Format: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c — Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4f — Confidence validation*:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a–G4d skipped)
```

*G4g — Confidence column presence*:
```
HALT [G4g-{role}]: Confidence column absent — row included as [DEFERRED].
→ Readiness verdict forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a–G4f skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly: severity-confidence sort**

Sort: severity DESC (primary), confidence DESC (secondary within tier).
Append [DEFERRED] to G4g-affected rows.
Schema: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`

If zero findings:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 5.5 — FINDING CONVERGENCE REGISTER**

Group rows by Surface value. For each Surface cited by 2+ roles:
1. Check if all citing roles used the same Confidence tier.
   - Same tier, tier != LOW: assign CONFIRMED.
   - Same tier, tier = LOW: assign CONFIRMED-LOW.
   - Tiers differ: assign CORROBORATED.

```
FINDING CONVERGENCE REGISTER:
| Surface         | Roles (Confidence tiers)           | Tier          | Readiness Effect              |
|-----------------|------------------------------------|---------------|-------------------------------|
| [artifact field]| [pm: HIGH], [architect: HIGH]      | CONFIRMED     | HIGH-effective in Gate 7      |
| [other surface] | [pm: LOW], [architect: LOW]        | CONFIRMED-LOW | Flagged for Gate 9 enumeration|
| [third surface] | [pm: HIGH], [architect: MEDIUM]    | CORROBORATED  | Synthesis signal only         |
```

If no surface is cited by 2+ roles: emit "No convergence detected — all findings SOLO."
CONFIRMED-LOW findings are NOT HIGH-effective. They appear in the Gate 9 enumeration.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  CONFIRMED (non-LOW, HIGH-effective): [N] surfaces — [names]
  HIGH:    [N] findings
  MEDIUM:  [N] findings ([N] promoted to HIGH-effective via CONFIRMED)
  LOW:     [N] findings
  CORROBORATED surfaces: [N]
  CONFIRMED-LOW (requires Gate 9 verification): [N] surfaces
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. Any CONFIRMED (non-LOW) surface → HIGH-effective → BLOCKED.
2. Any HIGH finding → BLOCKED.
3. Any MEDIUM finding (non-CONFIRMED or CONFIRMED-LOW), no HIGH → CONDITIONAL.
4. Any DEFERRED row → minimum CONDITIONAL.
5. All LOW or none of the above → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
If CONFIRMED findings contributed: append
`(convergence: [N] CONFIRMED surfaces treated as HIGH-effective)`

**Gate 8 — Challenger: closing bracket**

Does the status quo hold? Name the strongest CONFIRMED counter-evidence. Note if any
CORROBORATED finding represents emerging signal that one more role would promote to
CONFIRMED. Revise readiness if warranted.
Emit: "Convergence assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface and its significance.
Then emit the mandatory Confidence=LOW enumeration:

```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | Finding summary |
|------|---------|----------|-----------------|
| ...  | ...     | ...      | ...             |
```

If no Confidence=LOW findings: emit "No Confidence=LOW findings. All findings are
directly evidenced or inferred from structure."
Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3, G4a–G4g (all roles), G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  CONFIRMED surfaces (non-LOW, HIGH-effective): [N]
  CONFIRMED-LOW (flagged): [N]
  CORROBORATED surfaces: [N]
  Result:        Matrix and convergence register complete. Both calibration contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a
- `rerun:G4a-{role}` through `rerun:G4g-{role}` — re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID     | Trigger description                  | Tier     | Re-entry command                                |
|-------------|--------------------------------------|----------|-------------------------------------------------|
| [G4g-pm]    | Confidence column absent from row    | DEFERRED | /crew-check {{artifact}} --amend rerun:G4g-pm   |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.

---

## V-03

**Axis**: C-26 + C-27 — Stage pre-condition and stage-scoped matrix with DEPRECATED value
**Hypothesis**: R7 V-03 introduced G0.5 before G1 and three STAGE-APPROPRIATE values
(YES/ADVISORY/NO). Two gaps remain against the v7 rubric: (1) DEPRECATED is not a formal
STAGE-APPROPRIATE value — retired artifacts fall through to the NO column with no automatic
READY guarantee; (2) the matrix sorts by severity only, so ADVISORY and NO rows appear
interspersed with YES rows; (3) `--amend stage:{value}` is absent from the AMEND block.
V-03 R8 closes all three. DEPRECATED is added as the fourth STAGE-APPROPRIATE label;
all rows for a DEPRECATED artifact receive DEPRECATED unconditionally and the readiness
verdict is READY without reading any finding. The matrix is scope-grouped before severity
sort: YES rows first, then ADVISORY, then NO (STAGE-SCOPE EXCLUSIONS appendix), then
DEPRECATED rows (DEPRECATED-FINDINGS appendix). Gate 7 reads only YES-scope rows for
non-DEPRECATED artifacts. `--amend stage:{value}` restarts from Gate 0.5. The claim:
when DEPRECATED is a formal label and the matrix is scope-grouped, a reviewer running
against a retired artifact cannot accidentally BLOCK it — the structure enforces
DEPRECATED = READY before any finding is evaluated.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
{{stage}}: [DRAFT | REVIEW | APPROVED | DEPRECATED]
```

Acknowledge injected values before executing any gate. If `{{stage}}` is absent or not
in the valid set, halt at Gate 0.5 before proceeding.

---

### PRE-EXECUTION: SEVERITY CALIBRATION CONTRACT

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW are valid. Any other value: HALT [G4c-{role}] BLOCKING.

---

### PRE-EXECUTION: ARTIFACT MATURITY STAGE CONTRACT

`{{stage}}` determines which finding rows contribute to the readiness verdict.

| Stage      | STAGE-APPROPRIATE=YES     | STAGE-APPROPRIATE=ADVISORY | STAGE-APPROPRIATE=NO  | STAGE-APPROPRIATE=DEPRECATED |
|------------|---------------------------|----------------------------|-----------------------|------------------------------|
| DRAFT      | HIGH, MEDIUM              | LOW                        | (none)                | N/A                          |
| REVIEW     | HIGH, MEDIUM              | LOW                        | (none)                | N/A                          |
| APPROVED   | HIGH (regression only)    | MEDIUM (calibration gap)   | LOW (polish-only)     | N/A                          |
| DEPRECATED | N/A                       | N/A                        | N/A                   | All findings (automatic)     |

STAGE-APPROPRIATE derivation per finding row:
- Compare finding Severity to stage profile for `{{stage}}`.
- DEPRECATED artifact: all rows receive STAGE-APPROPRIATE=DEPRECATED unconditionally.

DEPRECATED readiness rule: READINESS is always READY for DEPRECATED artifacts. No
YES-scope rows exist by definition; the verdict requires no finding evaluation.
All finding rows appear in the DEPRECATED-FINDINGS informational appendix.

Matrix grouping order: DEPRECATED group (informational) → YES group → ADVISORY group
→ NO group (exclusions appendix). Within each group: severity DESC.

Readiness verdict reads ONLY STAGE-APPROPRIATE=YES rows.
ADVISORY rows: appear in matrix, do not contribute to BLOCKED or CONDITIONAL.
NO rows: listed in STAGE-SCOPE EXCLUSIONS appendix, excluded from matrix body.

---

### PRE-EXECUTION: HALT REGISTRY

G0.5 appears before G1. G0.5 fires before G1 — no other gate proceeds until stage is
declared and recognized.

| Halt ID       | Trigger condition                                                | Tier     |
|---------------|------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED} | BLOCKING |
| G1            | `.craft/roles/` absent or unreadable                             | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding                      | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface                     | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract                   | BLOCKING |
| G4d-{role}    | Recommendation missing location reference                        | BLOCKING |
| G4h-{role}    | STAGE-APPROPRIATE column absent or not in {YES,ADVISORY,NO,DEPRECATED} | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED artifact)    | BLOCKING |

G5 does not fire for DEPRECATED artifacts (READY is unconditional; no YES-scope exists).

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips         | Safe-skip prerequisite                    |
|-----------------------------|------------|---------------|-------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)     | Full role restart                         |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)     | Full role restart                         |
| `--amend rerun:G4b-{role}`  | G4b        | G4a           | Lens anchor verified                      |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b      | Lens anchor + named surface verified      |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c       | Lens anchor + surface + severity verified |
| `--amend rerun:G4h-{role}`  | G4h        | G4a–G4d       | All prior sub-gates verified              |

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 — Stage acknowledgment** (fires before Gate 1)

If `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}:
```
HALT [G0.5]: Stage absent or not recognized.
→ To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING — no gate proceeds until stage is declared)
```

Otherwise: state "Artifact maturity stage: {{stage}}. Scope calibration locked per
ARTIFACT MATURITY STAGE CONTRACT. STAGE-APPROPRIATE values loaded for {{stage}}."

If {{stage}} = DEPRECATED: additionally state "Artifact is DEPRECATED. All findings
will receive STAGE-APPROPRIATE=DEPRECATED. Readiness verdict will be READY regardless
of finding content. Run continues for informational record."

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active. HIGH=3, MEDIUM=2, LOW=1.
Stage: {{stage}}. Scope grouping: YES → ADVISORY → NO (→ DEPRECATED if stage=DEPRECATED)."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate runs first. State what the team does today without `{{artifact}}` and
why acceptable. Name >= 2 status-quo strengths. Note which are most relevant given
`{{stage}}` (e.g., APPROVED stage centers inertia on regression risk; DEPRECATED stage
names what replaced the artifact).
Emit: "Status quo registered. Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor*:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart)
```

*G4b — Surface finding*: Format:
`| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | Recommendation |`
For DEPRECATED artifacts: STAGE-APPROPRIATE=DEPRECATED on all rows.
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c — Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4h — STAGE-APPROPRIATE derivation*: Derive STAGE-APPROPRIATE per CONTRACT for
`{{stage}}`. Value must be in {YES, ADVISORY, NO, DEPRECATED}. On absent or invalid:
```
HALT [G4h-{role}]: STAGE-APPROPRIATE column absent or invalid — row included as [DEFERRED].
→ Readiness verdict forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4h-{role}
  (skip-map: G4a–G4d skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly: scope-grouped, severity-sorted**

Assemble all staged rows. Group by STAGE-APPROPRIATE first, then sort severity DESC
within each group. Append [DEFERRED] to G4h-affected rows.

Group order in output:
1. YES group (severity DESC) — contributes to readiness verdict
2. ADVISORY group (severity DESC) — noted, not blocking
3. NO group — listed in STAGE-SCOPE EXCLUSIONS appendix only
4. DEPRECATED group — listed in DEPRECATED-FINDINGS appendix only

Schema: `| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | Recommendation |`

For non-DEPRECATED artifact: if zero YES-scope rows after G4:
```
HALT [G5]: Zero stage-appropriate findings for {{stage}} artifact.
→ All reviewers produced findings outside YES scope for this stage.
→ To continue: /crew-check {{artifact}} --amend depth:deep
  Or verify: /crew-check {{artifact}} --amend stage:[correct-stage]
```

STAGE-SCOPE EXCLUSIONS appendix (STAGE-APPROPRIATE=NO rows):
```
STAGE-SCOPE EXCLUSIONS (STAGE-APPROPRIATE=NO — excluded from verdict):
- [role] on [surface]: [brief description] — outside YES scope for {{stage}}
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  In-scope (STAGE-APPROPRIATE=YES):
    HIGH:   [N] findings
    MEDIUM: [N] findings
    LOW:    [N] findings
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N] findings — noted, not blocking
  Excluded (STAGE-APPROPRIATE=NO):       [N] findings — below scope floor
  Deprecated (STAGE-APPROPRIATE=DEPRECATED): [N] findings — informational
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

For DEPRECATED artifact:
`READINESS: READY (artifact is DEPRECATED — all findings informational; see DEPRECATED-FINDINGS appendix)`

For non-DEPRECATED, apply to STAGE-APPROPRIATE=YES rows only:
1. Any YES-scope HIGH → BLOCKED.
2. Any YES-scope MEDIUM, no YES-scope HIGH → CONDITIONAL.
3. Any DEFERRED row → minimum CONDITIONAL.
4. Otherwise → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
Append: `(scope: {{stage}} — [N] YES-scope findings evaluated; [N] ADVISORY; [N] NO excluded)`

**Gate 8 — Challenger: closing bracket**

Does the status quo hold given the stage-scoped matrix? Note whether ADVISORY findings
represent latent risks worth escalating before the next stage transition. For DEPRECATED:
confirm no ADVISORY finding warrants a patch or fork before full retirement. Revise
readiness only if YES-scope analysis warrants.
Emit: "Stage-scoped inertia assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 cross-role convergence on YES-scope findings. Note if any
ADVISORY finding has cross-role corroboration that warrants scope promotion at next
review cycle. Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a–G4h (all roles), G5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  YES-scope findings: [N]
  ADVISORY findings:  [N]
  NO-excluded:        [N]
  Result:        Stage-scoped matrix complete. Scope and severity contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `stage:{value}` — change artifact maturity stage; restarts from Gate 0.5
- `rerun:{role}` — full role restart from G4a
- `rerun:G4a-{role}` through `rerun:G4h-{role}` — re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID   | Trigger description                | Tier     | Re-entry command                                  |
|-----------|------------------------------------|----------|---------------------------------------------------|
| [G0.5]    | Stage 'WIP' not in valid set       | BLOCKING | /crew-check {{artifact}} --amend stage:DRAFT      |
| [G4h-pm]  | STAGE-APPROPRIATE column absent    | DEFERRED | /crew-check {{artifact}} --amend rerun:G4h-pm     |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.

---

## V-04

**Axis**: C-24 + C-25 — Full dual-axis calibration + named convergence tier register
**Hypothesis**: V-01 R8 establishes confidence as a pre-committed dimension with formal
tiers and operational meanings — the score sort and the CONFIRMED readiness promotion both
flow from it. V-02 R8 establishes named convergence tiers where the distinguishing criterion
between CONFIRMED and CORROBORATED is confidence tier alignment. V-04 combines both: the
confidence scale (C-24) feeds directly into convergence tier derivation (C-25) — CONFIRMED
requires same surface AND same confidence tier across citing roles. The CONFIRMED-LOW tier
exists only because confidence has a LOW value; without C-24, C-25's tier distinction
collapses. The claim: when C-24 and C-25 are active simultaneously, the matrix contains
dual-axis sort order (severity DESC, confidence DESC), a convergence register with
mechanically-derived CONFIRMED/CORROBORATED/CONFIRMED-LOW tiers, HIGH-effective promotion
for CONFIRMED non-LOW findings, and a separately enumerated Confidence=LOW list — a complete
evidence-quality picture with no editorial step between the pre-committed contracts and the
readiness verdict.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
```

Acknowledge injected values before executing any gate.

---

### PRE-EXECUTION: SEVERITY AND CONFIDENCE CALIBRATION CONTRACT

**Severity scale:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence scale:**
| Label  | Score | Operational meaning                                                       |
|--------|-------|---------------------------------------------------------------------------|
| HIGH   | 3     | Directly evidenced: cited text, field, or schema element in artifact      |
| MEDIUM | 2     | Inferred from structural pattern or omission; no direct citation possible |
| LOW    | 1     | Speculative or risk-based; no direct artifact evidence exists             |

Matrix sort: severity DESC (primary), confidence DESC within severity tier (secondary).

Readiness treatment: CONFIRMED surface (same surface + matching confidence tier != LOW,
2+ roles) treated as HIGH-effective in Gate 7 (convergent direct evidence eliminates
the uncertainty that makes MEDIUM severity conditional).

Invalid severity: HALT [G4c-{role}] BLOCKING.
Invalid confidence: HALT [G4f-{role}] BLOCKING.
Absent confidence: HALT [G4g-{role}] DEFERRED.

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

After the matrix (Gate 5.5), a FINDING CONVERGENCE REGISTER is emitted.

| Tier         | Criteria                                                           | Readiness effect                          |
|--------------|--------------------------------------------------------------------|-------------------------------------------|
| CONFIRMED    | Same Surface, 2+ roles, ALL citing roles share same Confidence tier, tier != LOW | HIGH-effective in Gate 7  |
| CONFIRMED-LOW| Same Surface, 2+ roles, ALL citing roles share Confidence=LOW      | Flagged for Gate 9; NOT HIGH-effective    |
| CORROBORATED | Same Surface, 2+ roles, Confidence tiers differ across citing roles | Synthesis signal; no automatic promotion |
| SOLO         | Surface cited by exactly 1 role                                    | Normal weight                             |

Distinguishing criterion: confidence alignment. CONFIRMED = roles agree on surface AND
evidential basis. CORROBORATED = roles agree on surface but bring different evidential
positions. CONFIRMED-LOW = roles agree on surface AND evidential weakness.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4f-{role}    | Confidence `{value}` not in calibration contract    | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row           | DEFERRED |
| G5            | Zero findings produced across all roles             | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                               |
|-----------------------------|------------|-------------------|------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart                                    |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified                                 |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + named surface verified                 |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified            |
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4d           | Lens anchor + surface + severity + location verified |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f           | All prior sub-gates verified                         |

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
Matrix sort: severity DESC, confidence DESC within tier.
Convergence tiers: CONFIRMED (same surface + matching confidence tier != LOW, 2+ roles)
  treated as HIGH-effective in Gate 7.
CORROBORATED (same surface, differing confidence, 2+ roles): synthesis signal only.
CONFIRMED-LOW (same surface + matching LOW, 2+ roles): flagged for Gate 9 verification."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate runs first. State what the team does today without `{{artifact}}` and
why acceptable. Name >= 2 specific status-quo strengths.
Emit: "Status quo registered. Domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor*: "From the [role] perspective, this review examines [surface]."
On missing:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart)
```

*G4b — Surface finding*: Format:
`| Role | Finding | Surface | Severity | Confidence | Recommendation |`
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c — Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4f — Confidence validation*:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a–G4d skipped)
```

*G4g — Confidence column presence*:
```
HALT [G4g-{role}]: Confidence column absent — row included as [DEFERRED].
→ Readiness verdict forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a–G4f skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly: severity-confidence sort**

Sort: severity DESC (primary), confidence DESC (secondary).
Append [DEFERRED] to G4g-affected rows.
Schema: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`

If zero findings:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 5.5 — FINDING CONVERGENCE REGISTER**

Group rows by Surface. For each Surface cited by 2+ roles:
1. Check confidence tier across all citing rows.
   - All same tier, tier != LOW: CONFIRMED.
   - All same tier, tier = LOW: CONFIRMED-LOW.
   - Tiers differ: CORROBORATED.

```
FINDING CONVERGENCE REGISTER:
| Surface       | Roles (Severity / Confidence)              | Tier          | Readiness Effect            |
|---------------|--------------------------------------------|---------------|-----------------------------|
| [surface]     | [pm: HIGH/HIGH], [arch: MEDIUM/HIGH]       | CONFIRMED     | HIGH-effective in Gate 7    |
| [surface]     | [pm: MEDIUM/LOW], [arch: LOW/LOW]          | CONFIRMED-LOW | Flagged for Gate 9          |
| [surface]     | [pm: HIGH/HIGH], [arch: HIGH/MEDIUM]       | CORROBORATED  | Synthesis signal only       |
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  CONFIRMED (non-LOW, HIGH-effective): [N] surfaces — [names]
  HIGH:    [N] findings
  MEDIUM:  [N] findings ([N] promoted to HIGH-effective via CONFIRMED)
  LOW:     [N] findings
  CORROBORATED:  [N] surfaces
  CONFIRMED-LOW: [N] surfaces (flagged; verification required before action)
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. Any CONFIRMED (non-LOW) surface → HIGH-effective → BLOCKED.
2. Any HIGH finding → BLOCKED.
3. Any MEDIUM finding (non-CONFIRMED or CONFIRMED-LOW), no HIGH → CONDITIONAL.
4. Any DEFERRED row → minimum CONDITIONAL.
5. CONFIRMED-LOW surfaces do not block independently; they are flagged at Gate 9.
6. All LOW or none → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
If CONFIRMED contributed: append
`(convergence: [N] CONFIRMED surfaces treated as HIGH-effective)`

**Gate 8 — Challenger: closing bracket**

Does the status quo hold? Name strongest CONFIRMED counter-evidence. Note if any
CORROBORATED finding would become CONFIRMED with one more role at the same confidence
tier. Note if CONFIRMED-LOW findings would change verdict if confidence could be elevated.
Emit: "Convergence and inertia assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface and its significance. Then
emit the mandatory Confidence=LOW enumeration:

```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | Finding summary |
|------|---------|----------|-----------------|
| ...  | ...     | ...      | ...             |
```

State whether any CONFIRMED-LOW surface would change readiness verdict if confidence
could be elevated. Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3, G4a–G4g (all roles), G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  CONFIRMED surfaces (non-LOW, HIGH-effective): [N]
  CONFIRMED-LOW (flagged): [N]
  CORROBORATED surfaces: [N]
  Result:        Dual-axis calibration and convergence register complete.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a
- `rerun:G4a-{role}` through `rerun:G4g-{role}` — re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID        | Trigger description                  | Tier     | Re-entry command                                     |
|----------------|--------------------------------------|----------|------------------------------------------------------|
| [G4f-architect]| Confidence 'CERTAIN' not in contract | BLOCKING | /crew-check {{artifact}} --amend rerun:G4f-architect |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.

---

## V-05

**Axis**: C-24 + C-25 + C-26 + C-27 + IC-CHALLENGED — Full integration
**Hypothesis**: V-04 unifies C-24 and C-25 into a clean calibration-plus-convergence
chain. V-03 introduces C-26+C-27 for stage-scoped readiness. R7 V-01 established the
IC-CHALLENGED architecture (INERTIA CLAIM REGISTRY, CHALLENGE RESPONSE MAP). V-05 R8
combines all five structures: finding rows carry Severity, Confidence, IC-CHALLENGED,
and STAGE-APPROPRIATE; the FINDING CONVERGENCE REGISTER uses confidence-matching for
CONFIRMED and CORROBORATED; G0.5 fires before G1; the matrix is scope-grouped then
dual-axis sorted; Confidence=LOW findings are enumerated at Gate 9; DEPRECATED is a
formal fourth value yielding automatic READY; `--amend stage:{value}` is a first-class
operation; STANDING HIGH-strength ICs block. Four independent mechanical signals
(scope, severity, confidence, inertia) each pre-committed in their own contract section,
each enforceable independently of prose context. The claim: when all four new criteria
compose with IC framing, the review produces a definitive readiness answer without
editorial aggregation at any gate.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
{{stage}}: [DRAFT | REVIEW | APPROVED | DEPRECATED]
```

Acknowledge injected values before executing any gate. If `{{stage}}` is absent or not
in the valid set, halt at Gate 0.5 before proceeding.

---

### PRE-EXECUTION: SEVERITY AND CONFIDENCE CALIBRATION CONTRACT

**Severity scale:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence scale:**
| Label  | Score | Operational meaning                                                       |
|--------|-------|---------------------------------------------------------------------------|
| HIGH   | 3     | Directly evidenced: cited text, field, or schema element in artifact      |
| MEDIUM | 2     | Inferred from structural pattern or omission; no direct citation possible |
| LOW    | 1     | Speculative or risk-based; no direct artifact evidence exists             |

Matrix sort: scope-grouped first (YES → ADVISORY → NO/DEPRECATED), then within each
scope group: severity DESC, confidence DESC.

Readiness: CONFIRMED surface (same surface + matching confidence tier != LOW, 2+ roles)
treated as HIGH-effective in Gate 7 for YES-scope rows.

Invalid severity: HALT [G4c-{role}] BLOCKING.
Invalid confidence: HALT [G4f-{role}] BLOCKING.
Absent confidence: HALT [G4g-{role}] DEFERRED.

---

### PRE-EXECUTION: ARTIFACT MATURITY STAGE CONTRACT

| Stage      | STAGE-APPROPRIATE=YES     | STAGE-APPROPRIATE=ADVISORY | STAGE-APPROPRIATE=NO  | STAGE-APPROPRIATE=DEPRECATED |
|------------|---------------------------|----------------------------|-----------------------|------------------------------|
| DRAFT      | HIGH, MEDIUM              | LOW                        | (none)                | N/A                          |
| REVIEW     | HIGH, MEDIUM              | LOW                        | (none)                | N/A                          |
| APPROVED   | HIGH (regression only)    | MEDIUM (calibration gap)   | LOW (polish-only)     | N/A                          |
| DEPRECATED | N/A                       | N/A                        | N/A                   | All findings (automatic)     |

DEPRECATED artifact: all rows receive STAGE-APPROPRIATE=DEPRECATED unconditionally.
Readiness for DEPRECATED is always READY (informational appendix only).

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

| Tier         | Criteria                                                               | Readiness effect                           |
|--------------|------------------------------------------------------------------------|--------------------------------------------|
| CONFIRMED    | Same Surface, 2+ roles, ALL same Confidence tier, tier != LOW, YES-scope | HIGH-effective in Gate 7                  |
| CONFIRMED-LOW| Same Surface, 2+ roles, ALL Confidence=LOW, YES-scope                  | Flagged for Gate 9; NOT HIGH-effective     |
| CORROBORATED | Same Surface, 2+ roles, Confidence tiers differ, YES-scope             | Convergence signal; no automatic promotion |
| SOLO         | Surface cited by exactly 1 role                                        | Normal weight                              |

Convergence register is computed over YES-scope rows only. ADVISORY and NO rows are
excluded from the convergence register (they do not contribute to verdict).

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

Challenger's opening pass populates this registry. Claims numbered IC-01, IC-02, etc.

| IC-ID | Inertia Claim (why not building {{artifact}} is acceptable) | Strength |
|-------|-------------------------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                                 | [H/M/L]  |
| ...   | ...                                                         | ...      |

Strength: H = fully replaces the proposed value; M = partially covers it; L = weak substitute.

IC-CHALLENGED derivation contract: every finding row carries IC-CHALLENGED = one or
more IC-IDs (comma-separated) or `none` (finding does not challenge any registered IC).
An absent IC-CHALLENGED column triggers HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: HALT REGISTRY

G0.5 appears before G1 — fires before all other gates. No gate proceeds until stage
is declared and recognized.

| Halt ID       | Trigger condition                                                    | Tier     |
|---------------|----------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}  | BLOCKING |
| G1            | `.craft/roles/` absent or unreadable                                 | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims                      | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding                          | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface                         | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract                       | BLOCKING |
| G4d-{role}    | Recommendation missing location reference                            | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated                           | SCOPED   |
| G4f-{role}    | Confidence `{value}` not in calibration contract                     | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row                            | DEFERRED |
| G4h-{role}    | STAGE-APPROPRIATE not in {YES, ADVISORY, NO, DEPRECATED}             | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED artifact)        | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips         | Safe-skip prerequisite                                       |
|-----------------------------|------------|---------------|--------------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4b-{role}`  | G4b        | G4a           | Lens anchor verified                                         |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b      | Lens anchor + named surface verified                         |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c       | Lens anchor + surface + severity verified                    |
| `--amend rerun:G4e-{role}`  | G4e        | G4a–G4d       | Lens anchor + surface + severity + location verified         |
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4e       | All prior sub-gates + IC-CHALLENGED verified                 |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f       | All prior sub-gates + confidence label verified              |
| `--amend rerun:G4h-{role}`  | G4h        | G4a–G4g       | All prior sub-gates verified                                 |

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 — Stage acknowledgment** (fires before Gate 1)

If `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}:
```
HALT [G0.5]: Stage absent or not recognized.
→ To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING — no gate proceeds until stage is declared)
```

Otherwise: state "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings receive STAGE-APPROPRIATE=DEPRECATED. Readiness will be
READY regardless of content. Run continues for informational record."

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
Stage: {{stage}}. Matrix: scope-grouped (YES→ADVISORY→NO), then severity DESC,
confidence DESC within group.
CONFIRMED (same surface + matching confidence tier != LOW, 2+ roles, YES-scope)
  treated as HIGH-effective in Gate 7.
STANDING IC at HIGH strength blocks readiness regardless of finding severity.
IC-CHALLENGED required on every finding row."

**Gate 3 — Challenger: opening bracket and inertia claim registration**

Inertia-advocate runs first. Populate the INERTIA CLAIM REGISTRY with >= 2 numbered
claims (IC-01, IC-02, ...). For each: name the specific existing capability, process,
or argument that makes `{{artifact}}` unnecessary or low-priority. Assign Strength
(H/M/L). Note which claims are most relevant given `{{stage}}`.

On fewer than 2 claims:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
→ To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING — no domain review proceeds until registry has >= 2 entries)
```

After populating: emit "Inertia registry locked. IC-01 through IC-[N] registered.
Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor*: "From the [role] perspective, this review examines [surface]."
On missing:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart)
```

*G4b — Surface finding*: Format:
`| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`
For DEPRECATED: STAGE-APPROPRIATE=DEPRECATED on all rows.
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c — Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4e — IC-CHALLENGED column*: Every finding row must carry IC-CHALLENGED = IC-[N]
(comma-separated for multiple) or `none`. Absent column triggers SCOPED halt:
```
HALT [G4e-{role}]: IC-CHALLENGED column absent or unpopulated.
→ Role {role} excluded from matrix. Run continues.
→ To include: /crew-check {{artifact}} --amend rerun:G4e-{role}
  (skip-map: G4a–G4d skipped)
  (SCOPED — EXCLUDED ROLES appendix will be appended)
```

*G4f — Confidence validation*:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a–G4e skipped)
```

*G4g — Confidence column presence*:
```
HALT [G4g-{role}]: Confidence column absent — row included as [DEFERRED].
→ Readiness verdict forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a–G4f skipped; DEFERRED — run continues)
```

*G4h — STAGE-APPROPRIATE derivation*: Per ARTIFACT MATURITY STAGE CONTRACT.
Value must be in {YES, ADVISORY, NO, DEPRECATED}. On absent or invalid:
```
HALT [G4h-{role}]: STAGE-APPROPRIATE column absent or invalid — row included as [DEFERRED].
→ Readiness verdict forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4h-{role}
  (skip-map: G4a–G4g skipped; DEFERRED — run continues)
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

After all domain roles complete, assemble the CHALLENGE RESPONSE MAP. For each IC-ID,
list every YES-scope finding row that cited it.

```
| IC-ID | Strength | Challenging Findings (Role — Sev/Conf, STAGE-APPROPRIATE) | IC Status  |
|-------|----------|-------------------------------------------------------------|------------|
| IC-01 | H        | [pm — HIGH/HIGH, YES], [architect — MEDIUM/HIGH, YES]       | OVERCOME   |
| IC-02 | M        | [pm — LOW/LOW, YES]                                         | CONTESTED  |
| IC-03 | H        | (none in YES scope)                                         | STANDING   |
```

IC Status (YES-scope findings only):
- OVERCOME: IC cited by >= 1 YES-scope finding at HIGH severity.
- CONTESTED: IC cited by YES-scope findings, none at HIGH severity.
- STANDING: IC cited by no YES-scope finding.

CONFIRMED findings (same surface + matching confidence tier != LOW, 2+ roles) that
challenge an IC in YES scope: mark IC as OVERCOME-CONFIRMED — convergent direct evidence
eliminates the claim without editorial judgement.

Emit CHALLENGE RESPONSE MAP before Gate 5.

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted**

Assemble all staged rows. Group by STAGE-APPROPRIATE first, then sort severity DESC,
confidence DESC within each group. Append [DEFERRED] to G4g/G4h-affected rows.

Group order:
1. YES group (severity DESC, confidence DESC) — verdict input
2. ADVISORY group (severity DESC, confidence DESC) — noted, not blocking
3. NO group — STAGE-SCOPE EXCLUSIONS appendix
4. DEPRECATED group — DEPRECATED-FINDINGS appendix
5. EXCLUDED ROLES appendix (SCOPED G4e halts)

Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

For non-DEPRECATED artifact: if zero YES-scope rows after G4:
```
HALT [G5]: Zero stage-appropriate findings for {{stage}} artifact.
→ To continue: /crew-check {{artifact}} --amend depth:deep
  Or: /crew-check {{artifact}} --amend stage:[correct-stage]
```

**Gate 5.5 — FINDING CONVERGENCE REGISTER** (YES-scope rows only)

Group YES-scope rows by Surface. For each Surface cited by 2+ YES-scope roles:
- All same confidence tier, tier != LOW: CONFIRMED.
- All same confidence tier, tier = LOW: CONFIRMED-LOW.
- Confidence tiers differ: CORROBORATED.

```
FINDING CONVERGENCE REGISTER (YES-scope):
| Surface   | Roles (Sev/Conf)                  | Tier          | IC Impact                 | Readiness Effect         |
|-----------|-----------------------------------|---------------|---------------------------|--------------------------|
| [surface] | [pm HIGH/HIGH],[arch HIGH/HIGH]   | CONFIRMED     | IC-01 -> OVERCOME-CONFIRMED| HIGH-effective           |
| [surface] | [pm MED/LOW],[arch MED/LOW]       | CONFIRMED-LOW | IC-02 -> CONTESTED (weak) | Flagged for Gate 9       |
| [surface] | [pm HIGH/HIGH],[arch HIGH/MED]    | CORROBORATED  | none                      | Synthesis signal only    |
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  In-scope (STAGE-APPROPRIATE=YES):
    CONFIRMED (non-LOW, HIGH-effective): [N] surfaces — [names]
    HIGH:    [N] findings
    MEDIUM:  [N] findings ([N] promoted via CONFIRMED)
    LOW:     [N] findings
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N] findings — noted, not blocking
  Excluded (STAGE-APPROPRIATE=NO):       [N] findings — below scope floor
  Deprecated:  [N] findings — informational only
  Convergence: CONFIRMED-LOW [N], CORROBORATED [N]
  Inertia: STANDING HIGH-strength ICs: [N]
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

For DEPRECATED artifact:
`READINESS: READY (artifact is DEPRECATED — all findings informational; see appendix)`

For non-DEPRECATED, apply to STAGE-APPROPRIATE=YES rows only:
1. Any CONFIRMED (non-LOW) surface → HIGH-effective → BLOCKED.
2. Any YES-scope HIGH finding → BLOCKED.
3. Any STANDING IC at HIGH strength → BLOCKED (regardless of finding severity).
4. Any YES-scope MEDIUM finding (non-CONFIRMED or CONFIRMED-LOW), no HIGH or CONFIRMED
   or STANDING-HIGH → CONDITIONAL.
5. Any DEFERRED row → minimum CONDITIONAL.
6. Otherwise → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
Append attribution for each active blocker:
- `(confirmed evidence: [N] CONFIRMED surfaces treated as HIGH-effective)`
- `(inertia: IC-[N] STANDING at HIGH strength)`
- `(scope: {{stage}} — [N] YES-scope findings; [N] ADVISORY; [N] excluded)`

**Gate 8 — Challenger: closing bracket and CHALLENGE RESPONSE MAP review**

Review the CHALLENGE RESPONSE MAP for each IC:
- OVERCOME or OVERCOME-CONFIRMED: acknowledge; name the finding(s) that overcame it.
- CONTESTED: name what additional evidence (surface, severity, confidence tier) would
  make it OVERCOME.
- STANDING: explain why no YES-scope domain reviewer challenged this IC — is it a scope
  gap, a genuine absence, or an ADVISORY-only signal?

Note whether any CONFIRMED finding's convergence evidence makes a STANDING IC
demonstrably OVERCOME. Note ADVISORY findings representing latent IC risk at next
stage transition. Revise readiness only if YES-scope or STANDING IC analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface and its significance. Then
emit the mandatory Confidence=LOW enumeration:

```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
|------|---------|----------|---------------|-------------------|-----------------|
| ...  | ...     | ...      | ...           | ...               | ...             |
```

State whether any CONFIRMED-LOW surface would change IC status or readiness verdict if
confidence could be elevated. Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a–G4h (all roles), G4.5,
                 G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  DEFERRED rows: 0
  CONFIRMED surfaces (non-LOW, HIGH-effective): [N]
  CONFIRMED-LOW (flagged): [N]
  STANDING HIGH ICs: [N]
  YES-scope / ADVISORY / excluded: [N] / [N] / [N]
  Result:        Matrix complete. All four contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `stage:{value}` — change artifact maturity stage; restarts from Gate 0.5
- `rerun:{role}` — full role restart from G4a
- `rerun:challenger` — restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4h-{role}` — re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID        | Trigger description                  | Tier     | Re-entry command                                        |
|----------------|--------------------------------------|----------|---------------------------------------------------------|
| [G0.5]         | Stage 'WIP' not in valid set         | BLOCKING | /crew-check {{artifact}} --amend stage:DRAFT            |
| [G4e-pm]       | IC-CHALLENGED column absent          | SCOPED   | /crew-check {{artifact}} --amend rerun:G4e-pm           |
| [G4g-architect]| Confidence column absent             | DEFERRED | /crew-check {{artifact}} --amend rerun:G4g-architect    |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.
