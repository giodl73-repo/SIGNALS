---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 7
rubric: crew-check-rubric-v6-2026-03-17.md
---

# crew-check — Variate R7

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v6 floor (all variations must hold):
- Essential: C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability,
  C-08 severity calibration consistency
- Aspirational: C-09 cross-role synthesis, C-10 AMEND responsiveness,
  C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first,
  C-14 readiness-gate framing, C-15 severity-sorted output, C-16 hard-halt execution gate,
  C-17 named halt identifier system, C-18 AMEND gate-audit sub-command,
  C-19 self-routing halt messages, C-20 executable audit output,
  C-21 run health certificate (always-emit), C-22 three-tier halt scope,
  C-23 pre-committed skip-map

Design intent for R7: All five variations hold the R6 v6 floor (C-01 through C-23 present
in all). R6 closed the halt/audit progression: run health certificate (C-21), three-tier
halt scope (C-22), pre-committed skip-map (C-23). R7 moves to the review architecture
itself — how the challenger's inertia claims connect structurally to domain findings,
how finding confidence is calibrated independently of severity, and how artifact maturity
stages scope which findings count toward readiness.

Axes selected for R7:
- V-01: Inertia framing — challenger bracket with pre-registered INERTIA CLAIM REGISTRY
  and CHALLENGE RESPONSE MAP (IC-IDs link challenger claims to domain findings)
- V-02: Output format — per-finding confidence tier and FINDING CONVERGENCE REGISTER
  (CORROBORATED/CONFIRMED tags derived mechanically from cross-role agreement)
- V-03: Lifecycle emphasis — artifact maturity stage pre-registration with scope
  calibration table (STAGE-APPROPRIATE column gates readiness contribution)
- V-04: Inertia framing + output format (V-01 + V-02: IC challenge map + confidence tier;
  CONFIRMED findings that challenge an IC make that IC OVERCOME unconditionally)
- V-05: Inertia framing + lifecycle emphasis (V-01 + V-03: IC challenge map + maturity
  stage; STANDING ICs on STAGE-APPROPRIATE=ADVISORY dimensions do not block)

---

## V-01

**Axis**: Inertia framing — challenger bracket with INERTIA CLAIM REGISTRY and
CHALLENGE RESPONSE MAP
**Hypothesis**: C-13 covers challenger-first sequencing and Gate 8 has always had a
closing challenger pass, but neither were structurally load-bearing. The challenger named
status-quo strengths in prose; domain findings had no obligation to address them; the
closing Challenger assessed "does the status quo hold?" without a formal accounting of
which claims were challenged and which were not. V-01 R7 formalizes the entire bracket:
the challenger's opening pass pre-registers numbered inertia claims (IC-01, IC-02...)
in a named table; every domain finding row carries an IC-CHALLENGED column citing which
claim(s) it addresses; a CHALLENGE RESPONSE MAP section assembles the claim-to-finding
mapping after Gate 4; and the closing Challenger assesses each IC as OVERCOME,
CONTESTED, or STANDING. A STANDING claim at HIGH strength conditions the readiness
verdict directly — no editorial judgement required. The claim: when the challenger's
authority is pre-committed and mechanically auditable, the review answers "did we
overcome inertia?" rather than "did we find problems?"

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
```

Acknowledge injected values before executing any gate.

---

### PRE-EXECUTION: SEVERITY CALIBRATION CONTRACT

Lock this severity scale before any reviewer runs.

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW are valid labels. Any other value triggers HALT [G4c-{role}].

---

### PRE-EXECUTION: HALT REGISTRY

All halt conditions declared before execution. Halt messages MUST match this registry
verbatim. `{role}` = role file name without extension. `{value}` = invalid value received.

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims     | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated          | SCOPED   |
| G5            | Zero findings produced across all roles             | BLOCKING |

SCOPED halts: the triggering role is excluded from the matrix; the run continues for
remaining roles; excluded roles are listed in the EXCLUDED ROLES appendix.
BLOCKING halts: full stop. No output beyond the halt message.
DEFERRED halts: finding row included in matrix with [DEFERRED] tag; readiness verdict
is forced to CONDITIONAL regardless of finding severity.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

For `--amend rerun:G4x-{role}` commands, the skip-map governs which sub-gates are
re-executed and which are skipped. Skipping is safe only when the prerequisite condition
was verified in the prior run.

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                         |
|-----------------------------|------------|-------------------|------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart from lens anchor             |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart from lens anchor             |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified in prior run              |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + named surface verified           |
| `--amend rerun:G4d-{role}`  | G4d        | G4a, G4b, G4c     | Lens anchor + surface + severity verified      |
| `--amend rerun:G4e-{role}`  | G4e        | G4a–G4d           | All four prior sub-gates verified              |

At re-entry time, state which sub-gates are being skipped and cite the prerequisite
condition. Do not silently re-execute a passing sub-gate.

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

The challenger's opening pass populates this registry. Claims are numbered IC-01, IC-02,
etc. Each claim names a specific status-quo capability or process that reduces the value
of `{{artifact}}`. The registry is used by the CHALLENGE RESPONSE MAP after Gate 4 and
by the closing Challenger at Gate 8.

| IC-ID | Inertia Claim (why not building {{artifact}} is acceptable) | Strength |
|-------|-------------------------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                                 | [H/M/L]  |
| ...   | ...                                                         | ...      |

Strength: H = the claim fully replaces the proposed value; M = the claim partially covers
it; L = the claim is a weak substitute.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

| Priority | Slot        | Role Name     | Basis                           |
|----------|-------------|---------------|---------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]   | Inertia-advocate: always first  |
| 2        | DOMAIN-1    | [ROLE_NAME]   | [reason]                        |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]   | Bracket close: always last      |

Challenger occupies first and last slots (fixed). `deep`: all roles. `standard`: relevant
roles with selection rationale. State total role count.

---

### EXECUTION

**Gate 1 — Role registry load**

You are not ready to select reviewers until `.craft/roles/` is confirmed readable and
non-empty.

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING — no output follows)
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active. HIGH=3, MEDIUM=2, LOW=1. No other values
permitted." You are not ready to run any reviewer until this is stated.

**Gate 3 — Challenger: opening bracket and inertia claim registration**

Inertia-advocate runs first. Populate the INERTIA CLAIM REGISTRY with >= 2 numbered
claims (IC-01, IC-02, ...). For each: name the specific existing capability, process, or
argument that makes `{{artifact}}` unnecessary or low-priority. Assign Strength (H/M/L).

On fewer than 2 claims:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
→ To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING — no domain review follows until registry has >= 2 entries)
```

After populating: emit "Inertia registry locked. IC-01 through IC-[N] registered.
Domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor* (required before any finding):
"From the [role] perspective, this review examines [specific surface of {{artifact}}]."

On missing lens anchor:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING — full role restart; no sub-gates skipped)
```

*G4b — Surface finding*: Every finding must name a specific artifact surface.
Format: `| Role | Finding | Surface | Severity | IC-CHALLENGED | Recommendation |`

On finding lacking named surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped — lens anchor verified in prior run)
```

*G4c — Severity validation*: Verify all severity labels against the calibration contract.
On first invalid value:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped — lens anchor and surface verified)
```

*G4d — Recommendation completeness*: Every recommendation must include a location
reference (section name, field, or line reference in `{{artifact}}`).
On missing location:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped — lens anchor, surface, severity verified)
```

*G4e — IC-CHALLENGED column*: Every finding row must carry an IC-CHALLENGED value:
either `IC-01`, `IC-02` (or comma-separated list for multiple), or `none` (finding is
novel, does not challenge any registered inertia claim). An empty or absent IC-CHALLENGED
column triggers HALT [G4e-{role}] (SCOPED — role excluded, run continues).

On missing IC-CHALLENGED:
```
HALT [G4e-{role}]: IC-CHALLENGED column absent or unpopulated.
→ Role {role} excluded from matrix. Run continues.
→ To include: /crew-check {{artifact}} --amend rerun:G4e-{role}
  (skip-map: G4a–G4d skipped — all prior sub-gates verified)
  (SCOPED — EXCLUDED ROLES appendix will be appended)
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

After all domain roles complete, assemble the CHALLENGE RESPONSE MAP. For each IC-ID
from the INERTIA CLAIM REGISTRY, list every finding row that cited it. If no finding
cites an IC, the cell is empty.

```
| IC-ID | Strength | Challenging Findings (Role — Severity) | IC Status  |
|-------|----------|----------------------------------------|------------|
| IC-01 | H        | [pm — HIGH], [architect — MEDIUM]      | OVERCOME   |
| IC-02 | M        | [pm — LOW]                             | CONTESTED  |
| IC-03 | H        | (none)                                 | STANDING   |
```

IC Status derivation:
- OVERCOME: IC is cited by >= 1 finding at HIGH severity.
- CONTESTED: IC is cited by findings, but none at HIGH severity.
- STANDING: IC is cited by no domain finding.

Emit the CHALLENGE RESPONSE MAP before Gate 5.

**Gate 5 — Matrix assembly and severity sort**

Assemble all staged finding rows. Sort descending by severity score (HIGH=3 first).
Within severity tier: challenger rows before domain rows.

Schema: `| Role | Finding | Surface | Severity | IC-CHALLENGED | Recommendation |`

If zero findings from all non-excluded roles:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

Append EXCLUDED ROLES section if any G4e SCOPED halts fired:
```
EXCLUDED ROLES (SCOPED halt — G4e):
- {role}: IC-CHALLENGED column absent. Re-run with: /crew-check {{artifact}} --amend rerun:G4e-{role}
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:   [N] findings
  MEDIUM: [N] findings
  LOW:    [N] findings
  STANDING ICs at HIGH strength: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. Any HIGH-severity finding → contributes BLOCKED.
2. Any MEDIUM-severity finding, no HIGH → contributes CONDITIONAL.
3. Any STANDING IC at HIGH strength (from CHALLENGE RESPONSE MAP) → contributes
   BLOCKED, regardless of domain finding severity.
4. All LOW or none, no STANDING HIGH ICs → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
If STANDING HIGH ICs contributed: append `(inertia: IC-[N] STANDING at HIGH strength)`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate reviews the CHALLENGE RESPONSE MAP. For each IC:
- OVERCOME: acknowledge. Name the finding(s) that overcome it.
- CONTESTED: name what additional evidence would make it OVERCOME.
- STANDING: explain why no domain reviewer challenged this IC and whether that is a
  scope gap or a genuine absence.

Revise readiness recommendation only if STANDING IC analysis changes the Gate 7 verdict.
Emit: "Inertia assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 cross-role convergence or conflict. Reference role names.
Identify >= 1 finding that is `none` for IC-CHALLENGED — and name whether it changes the
readiness picture independently of the inertia assessment. No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run. Heading encodes run state.

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3 (IC registry), G4a–G4e (all roles), G4.5, G5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  Result:        Matrix complete.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     → /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}}
```

The RUN HEALTH section always appears at this position. Its heading encodes run state.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a
- `rerun:challenger` — restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4e-{role}` — re-enter at named sub-gate (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID       | Trigger description                 | Tier    | Re-entry command                              |
|---------------|-------------------------------------|---------|-----------------------------------------------|
| [G4c-pm]      | Severity 'CRITICAL' not in contract | BLOCKING| /crew-check {{artifact}} --amend rerun:G4c-pm |
```
Each entry is paste-ready. The Re-entry command encodes minimum-restart routing per the
SUB-GATE SKIP-MAP — using it directly is equivalent to consulting the skip-map manually.

---

## V-02

**Axis**: Output format — per-finding confidence tier and FINDING CONVERGENCE REGISTER
**Hypothesis**: Severity tells you how bad the finding is if true. Confidence tells you
how likely it is to be true. Prior variations assign severity per a calibrated contract
(C-12) but leave confidence entirely editorial — a HIGH finding from a speculative
inference and a HIGH finding directly cited from artifact text receive the same weight.
V-02 R7 extends the calibration contract to include a CONFIDENCE tier (HIGH = directly
evidenced in artifact text; MEDIUM = inferred from structural pattern; LOW = speculative
or risk-based). Confidence appears as a column in every finding row. The matrix sorts
severity DESC, then confidence DESC within tier. After the matrix, a FINDING CONVERGENCE
REGISTER identifies findings that overlap in surface across 2+ roles: CORROBORATED (2
roles) or CONFIRMED (3+ roles). CONFIRMED findings are promoted to PRIORITY-1 in the
readiness assessment regardless of individual severity. The claim: when both confidence
and convergence are pre-committed and mechanical, the matrix becomes a prioritization
instrument rather than a severity-sorted list.

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

Lock both scales before any reviewer runs.

**Severity scale:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence scale:**
| Label  | Score | Operational meaning                                              |
|--------|-------|------------------------------------------------------------------|
| HIGH   | 3     | Finding is directly evidenced: cited text, field, or schema element present in artifact |
| MEDIUM | 2     | Finding is inferred from structural pattern or omission          |
| LOW    | 1     | Finding is speculative or risk-based; no direct artifact evidence|

Invalid severity label triggers HALT [G4c-{role}]. Invalid confidence label triggers
HALT [G4f-{role}]. Both are BLOCKING.

Matrix sort: severity DESC (primary), confidence DESC (secondary within severity tier).

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

DEFERRED halts: the finding row is included in the matrix with a [DEFERRED] tag; the run
continues; the readiness verdict is forced to CONDITIONAL regardless of severity scores.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                         |
|-----------------------------|------------|-------------------|------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                              |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart                              |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified in prior run              |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + named surface verified           |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified      |
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4d           | Lens anchor + surface + severity + location verified |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f           | All prior sub-gates verified                   |

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

After the matrix, a FINDING CONVERGENCE REGISTER is produced. Two findings overlap if
they cite the same `Surface` value from different roles. Overlap classification:

| Tag         | Condition                                              | Effect                                   |
|-------------|--------------------------------------------------------|------------------------------------------|
| CONFIRMED   | Same surface cited by >= 3 roles                       | Promoted to PRIORITY-1 in Gate 7 summary |
| CORROBORATED| Same surface cited by exactly 2 roles                  | Noted as convergence signal in Gate 9    |
| SOLO        | Surface cited by exactly 1 role                        | No convergence tag; normal weight        |

CONFIRMED findings are treated as HIGH-effective in the readiness verdict regardless of
their individual severity labels.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

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

State: "Severity and confidence calibration contracts active. Severity: HIGH=3, MEDIUM=2,
LOW=1. Confidence: HIGH=3, MEDIUM=2, LOW=1. No other values permitted for either scale."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate runs first. State what the team does today without `{{artifact}}` and
why that is acceptable. Name >= 2 specific status-quo strengths. Emit: "Status quo
registered. Domain review proceeds."

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

*G4b — Surface finding*: Every finding must name a specific artifact surface.
Format: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`

On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c — Severity validation*: On first invalid severity label:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d — Recommendation completeness*: Every recommendation must include a location
reference.
On missing:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a–G4c skipped)
```

*G4f — Confidence validation*: Verify all confidence labels against the calibration
contract. On first invalid value:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a–G4d skipped)
```

*G4g — Confidence column presence*: Every finding row must carry a populated Confidence
value. A row with an absent or blank Confidence column triggers G4g DEFERRED:
```
HALT [G4g-{role}]: Confidence column absent from finding row — row included as [DEFERRED].
→ Readiness verdict will be forced to CONDITIONAL for this run.
→ To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a–G4f skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly: severity-confidence sort**

Assemble all staged rows. Sort: severity DESC (primary), confidence DESC (secondary).
Append [DEFERRED] tag to any G4g-affected rows.

Schema: `| Role | Finding | Surface | Severity | Confidence | Recommendation |`

If zero findings:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 5.5 — FINDING CONVERGENCE REGISTER**

Group rows by Surface value. For each surface cited by 2+ roles, emit:

```
FINDING CONVERGENCE REGISTER:
| Surface         | Roles Citing     | Tag          | Highest Severity | Action            |
|-----------------|------------------|--------------|------------------|-------------------|
| [artifact field]| [role1], [role2] | CORROBORATED | HIGH             | Convergence noted |
| [other surface] | [r1],[r2],[r3]   | CONFIRMED    | MEDIUM           | PRIORITY-1 promoted|
```

CONFIRMED surfaces are PRIORITY-1 in Gate 6 regardless of severity label.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  PRIORITY-1 (CONFIRMED surfaces): [N] findings — [surface(s)]
  HIGH:   [N] findings
  MEDIUM: [N] findings
  LOW:    [N] findings
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. Any CONFIRMED surface → treated as HIGH-effective (BLOCKED if finding is otherwise
   MEDIUM or lower; CONDITIONAL if finding was already HIGH).
2. Any HIGH severity finding → BLOCKED.
3. Any MEDIUM finding, no HIGH or CONFIRMED → CONDITIONAL.
4. Any DEFERRED row → minimum CONDITIONAL.
5. All LOW or none of the above → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Given the matrix and FINDING CONVERGENCE REGISTER: does the status quo hold? Name the
strongest counter-evidence. Note whether any CONFIRMED finding directly undermines a
previously named status-quo strength. Revise readiness recommendation if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 CORROBORATED or CONFIRMED convergence. Name >= 1 finding with
Confidence=LOW that deserves independent verification before acting. Reference role names.
No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run.

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3, G4a–G4g (all roles), G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  Result:        Matrix complete. Confidence and convergence contracts honored.
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
- `rerun:G4a-{role}` through `rerun:G4g-{role}` — re-enter at named sub-gate (skip-map applies; state skipped sub-gates)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID        | Trigger description                       | Tier     | Re-entry command                               |
|----------------|-------------------------------------------|----------|------------------------------------------------|
| [G4f-architect]| Confidence 'CERTAIN' not in contract      | BLOCKING | /crew-check {{artifact}} --amend rerun:G4f-architect |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per SUB-GATE
SKIP-MAP.

---

## V-03

**Axis**: Lifecycle emphasis — artifact maturity stage pre-registration with scope
calibration table and STAGE-APPROPRIATE column
**Hypothesis**: Prior variations review any artifact at the same level of rigor regardless
of where it sits in its lifecycle. A DRAFT skill prompt reviewed with APPROVED-level
expectations produces noise (cosmetic findings block); an APPROVED skill reviewed with
DRAFT tolerance misses regressions. V-03 R7 introduces an ARTIFACT MATURITY STAGE
CONTRACT pre-committed before execution. The reviewer declares the artifact's maturity
stage (DRAFT / REVIEW / APPROVED / DEPRECATED); the contract maps each stage to an
expected severity profile and a scope limitation rule. Each finding row carries a
STAGE-APPROPRIATE column (YES / ADVISORY / NO) derived by comparing the finding's
severity against the stage profile. Only STAGE-APPROPRIATE=YES findings contribute to
the readiness verdict; ADVISORY findings are surfaced but do not block; NO findings are
demoted to informational and excluded from the verdict. The claim: when review scope is
calibrated to artifact context, findings carry weight proportional to their lifecycle
relevance — not just their logical severity.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
{{stage}}: [DRAFT | REVIEW | APPROVED | DEPRECATED]
```

Acknowledge injected values before executing any gate. If `{{stage}}` is not provided,
halt at Gate 0.5 and request it before continuing.

---

### PRE-EXECUTION: SEVERITY CALIBRATION CONTRACT

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW are valid. Any other value triggers HALT [G4c-{role}].

---

### PRE-EXECUTION: ARTIFACT MATURITY STAGE CONTRACT

Lock this contract before Gate 1. `{{stage}}` determines which finding severities are
STAGE-APPROPRIATE for the readiness verdict.

| Stage      | STAGE-APPROPRIATE=YES         | STAGE-APPROPRIATE=ADVISORY | STAGE-APPROPRIATE=NO             |
|------------|-------------------------------|----------------------------|----------------------------------|
| DRAFT      | HIGH, MEDIUM                  | LOW                        | (none — all severities relevant) |
| REVIEW     | HIGH, MEDIUM                  | LOW                        | (none)                           |
| APPROVED   | HIGH (regression)             | MEDIUM (calibration gap)   | LOW (polish-only)                |
| DEPRECATED | (none — artifact being retired)| HIGH, MEDIUM              | (all findings advisory)          |

STAGE-APPROPRIATE derivation rule (applied per finding row):
- Compare finding's Severity to the stage profile above.
- YES = severity is in the YES column for `{{stage}}`.
- ADVISORY = severity is in the ADVISORY column.
- NO = severity is in the NO column.

For DEPRECATED artifacts: all findings are STAGE-APPROPRIATE=ADVISORY; readiness verdict
is always READY with informational appendix.

Readiness verdict reads only STAGE-APPROPRIATE=YES rows. ADVISORY rows appear in the
matrix but do not contribute to BLOCKED or CONDITIONAL. NO rows are listed in a
STAGE-SCOPE EXCLUSIONS appendix.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G0.5          | `{{stage}}` not provided or not in valid set        | BLOCKING |
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4h-{role}    | STAGE-APPROPRIATE column absent or invalid value    | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)| BLOCKING |

G5 for non-DEPRECATED artifacts fires only when zero YES-scope findings exist (LOW-only
findings on an APPROVED artifact are all STAGE-APPROPRIATE=NO or ADVISORY and do not
constitute a valid review pass).

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                         |
|-----------------------------|------------|-------------------|------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                              |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)         | Full role restart                              |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified                           |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + surface verified                 |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified      |
| `--amend rerun:G4h-{role}`  | G4h        | G4a–G4d           | All prior sub-gates verified                   |

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 — Stage acknowledgment**

If `{{stage}}` is absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}:
```
HALT [G0.5]: Stage not provided or not in valid set.
→ To continue: /crew-check {{artifact}} --stage [DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING — no gate proceeds until stage is declared)
```

Otherwise: state "Artifact maturity stage: {{stage}}. Scope calibration active per
ARTIFACT MATURITY STAGE CONTRACT." Read the YES / ADVISORY / NO scope columns for
`{{stage}}` and hold them for G4h enforcement.

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active. HIGH=3, MEDIUM=2, LOW=1."

**Gate 3 — Challenger: opening bracket**

Inertia-advocate first. State what the team does today without `{{artifact}}` and why
acceptable. Name >= 2 status-quo strengths. Note which are most relevant given
`{{stage}}` (e.g., for APPROVED stage, inertia argument centers on regression risk).
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

*G4b — Surface finding*: Every finding must name a specific artifact surface.
Format: `| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | Recommendation |`

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

*G4h — STAGE-APPROPRIATE derivation*: For each finding row, derive STAGE-APPROPRIATE
value per the ARTIFACT MATURITY STAGE CONTRACT for `{{stage}}`. A row with an absent or
invalid STAGE-APPROPRIATE value triggers HALT [G4h-{role}] (DEFERRED):
```
HALT [G4h-{role}]: STAGE-APPROPRIATE column absent or invalid — row included as [DEFERRED].
→ Readiness verdict will be forced to CONDITIONAL.
→ To fix: /crew-check {{artifact}} --amend rerun:G4h-{role}
  (skip-map: G4a–G4d skipped; DEFERRED — run continues)
```

**Gate 5 — Matrix assembly and severity sort**

Assemble all staged rows. Sort descending by severity score. Within tier: challenger rows
before domain rows. Append [DEFERRED] tag to G4h-affected rows.

Schema: `| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | Recommendation |`

If zero STAGE-APPROPRIATE=YES findings for non-DEPRECATED artifact:
```
HALT [G5]: Zero stage-appropriate findings for {{stage}} artifact.
→ Reviewers produced findings outside the scope profile for this stage.
→ To continue: /crew-check {{artifact}} --amend depth:deep
  Or verify that {{stage}} is correctly declared.
```

Append STAGE-SCOPE EXCLUSIONS if any STAGE-APPROPRIATE=NO rows exist:
```
STAGE-SCOPE EXCLUSIONS (STAGE-APPROPRIATE=NO — not counted in verdict):
- [role] finding on [surface]: [brief description] — below scope floor for {{stage}} stage
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
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

Apply to STAGE-APPROPRIATE=YES rows only:
1. Any YES-scoped HIGH → BLOCKED.
2. Any YES-scoped MEDIUM, no YES-scoped HIGH → CONDITIONAL.
3. Any DEFERRED row → minimum CONDITIONAL.
4. DEPRECATED artifact: always READY with advisory appendix.
5. Otherwise → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
Append: `(scope: {{stage}} — [N] findings excluded from verdict)`

**Gate 8 — Challenger: closing bracket**

Given the stage-scoped matrix: does the status quo hold? Specifically address whether any
STAGE-APPROPRIATE=ADVISORY findings represent latent risks worth escalating before the
next lifecycle stage transition. Revise readiness if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 cross-role convergence or conflict on in-scope findings. Note
whether any STAGE-APPROPRIATE=ADVISORY findings have cross-role corroboration that
warrants stage promotion. Reference role names. No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run.

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a–G4h (all roles), G5, G6, G7, G8, G9
  Halts fired:   0
  DEFERRED rows: 0
  Excluded rows: [N] (STAGE-APPROPRIATE=NO)
  Result:        Stage-scoped matrix complete.
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
- `stage:{value}` — change artifact maturity stage declaration (restarts from Gate 0.5)
- `rerun:{role}` — full role restart from G4a
- `rerun:G4a-{role}` through `rerun:G4h-{role}` — re-enter at named sub-gate (skip-map applies)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID        | Trigger description                       | Tier     | Re-entry command                                     |
|----------------|-------------------------------------------|----------|------------------------------------------------------|
| [G4h-pm]       | STAGE-APPROPRIATE column absent           | DEFERRED | /crew-check {{artifact}} --amend rerun:G4h-pm        |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per SUB-GATE
SKIP-MAP.

---

## V-04

**Axis**: Inertia framing + output format (V-01 + V-02)
**Hypothesis**: V-01 makes domain findings accountable to registered inertia claims via
IC-CHALLENGED. V-02 makes findings accountable to calibrated confidence via CONFIDENCE
and the FINDING CONVERGENCE REGISTER. V-04 combines both: finding rows carry both
IC-CHALLENGED and CONFIDENCE columns; the FINDING CONVERGENCE REGISTER is extended to
cross-reference IC challenges — a CONFIRMED surface (3+ roles) that challenges an IC
makes that IC OVERCOME unconditionally, regardless of individual finding severity. The
claim: when convergence evidence can mechanically resolve inertia claims, the review
produces a definitive answer rather than a recommendation — CONFIRMED-OVERCOME ICs
require no editorial judgement to close.

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

**Severity:**
| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

**Confidence:**
| Label  | Score | Operational meaning                                              |
|--------|-------|------------------------------------------------------------------|
| HIGH   | 3     | Directly evidenced in artifact text, field, or schema element    |
| MEDIUM | 2     | Inferred from structural pattern or omission                     |
| LOW    | 1     | Speculative or risk-based; no direct artifact evidence           |

Invalid severity triggers HALT [G4c-{role}] BLOCKING. Invalid confidence triggers
HALT [G4f-{role}] BLOCKING. Absent confidence triggers HALT [G4g-{role}] DEFERRED.
Matrix sort: severity DESC, confidence DESC within tier.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                   | Tier     |
|---------------|-----------------------------------------------------|----------|
| G1            | `.craft/roles/` absent or unreadable                | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims     | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding         | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface        | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract      | BLOCKING |
| G4d-{role}    | Recommendation missing location reference           | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated          | SCOPED   |
| G4f-{role}    | Confidence `{value}` not in calibration contract    | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row           | DEFERRED |
| G5            | Zero findings produced across all roles             | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                              |
|-----------------------------|------------|-------------------|-----------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                                   |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified                                |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + surface verified                      |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified           |
| `--amend rerun:G4e-{role}`  | G4e        | G4a–G4d           | Lens anchor + surface + severity + location verified|
| `--amend rerun:G4f-{role}`  | G4f        | G4a–G4d           | Same as G4e (parallel sub-gate)                     |
| `--amend rerun:G4g-{role}`  | G4g        | G4a–G4f           | All prior sub-gates verified                        |

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

Populated by challenger at Gate 3. IC-IDs numbered IC-01, IC-02, ...

| IC-ID | Inertia Claim                                        | Strength |
|-------|------------------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                          | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                          | [H/M/L]  |

---

### PRE-EXECUTION: FINDING CONVERGENCE AND IC-RESOLUTION CONTRACT

After the matrix, the FINDING CONVERGENCE REGISTER maps surfaces to IC challenges:

| Surface convergence | IC-CHALLENGED | Convergence tag | IC Resolution effect                          |
|---------------------|---------------|-----------------|-----------------------------------------------|
| 3+ roles            | an IC-ID      | CONFIRMED       | IC is OVERCOME unconditionally                |
| 2 roles             | an IC-ID      | CORROBORATED    | IC status per CHALLENGE RESPONSE MAP severity |
| 1 role              | an IC-ID      | SOLO            | IC status per CHALLENGE RESPONSE MAP severity |
| any                 | none          | (tag only)      | No IC effect; convergence noted in Gate 9     |

CONFIRMED surfaces that cite an IC override the CHALLENGE RESPONSE MAP IC Status
derivation — the IC becomes OVERCOME regardless of individual finding severity.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

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

State: "Severity contract active (HIGH=3, MEDIUM=2, LOW=1). Confidence contract active
(HIGH=3, MEDIUM=2, LOW=1). No other values permitted for either scale."

**Gate 3 — Challenger: opening bracket and inertia claim registration**

Inertia-advocate runs first. Populate INERTIA CLAIM REGISTRY with >= 2 IC-IDs. For each:
name the specific existing capability that makes `{{artifact}}` unnecessary. Assign
Strength (H/M/L). On fewer than 2:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
→ To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING)
```
After: emit "Inertia registry locked. IC-01 through IC-[N] registered."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor* | BLOCKING on missing
*G4b — Surface finding*: Format: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | Recommendation |`
*G4c — Severity validation* | BLOCKING on invalid value
*G4d — Recommendation completeness* | BLOCKING on missing location
*G4e — IC-CHALLENGED column*: SCOPED on absent/unpopulated (role excluded, run continues)
*G4f — Confidence validation*: BLOCKING on invalid value
*G4g — Confidence column presence*: DEFERRED on absent (row tagged, verdict forced CONDITIONAL)

All halt messages embed re-entry commands per skip-map:
```
HALT [G4x-{role}]: [trigger].
→ To continue: /crew-check {{artifact}} --amend rerun:G4x-{role}
  (skip-map: [prior sub-gates] skipped — [prerequisite])
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

Assemble per V-01 logic. Then run the FINDING CONVERGENCE AND IC-RESOLUTION CONTRACT:
for any CONFIRMED surface (3+ roles) that cites an IC, override that IC's status to
OVERCOME unconditionally.

```
CHALLENGE RESPONSE MAP:
| IC-ID | Strength | Challenging Findings (Role — Sev — Conf) | Convergence Override | IC Status  |
|-------|----------|------------------------------------------|----------------------|------------|
| IC-01 | H        | [pm — HIGH — HIGH], [arch — HIGH — MED]  | CONFIRMED (3 roles)  | OVERCOME   |
| IC-02 | M        | [pm — LOW — LOW]                         | SOLO                 | CONTESTED  |
| IC-03 | H        | (none)                                   | —                    | STANDING   |
```

**Gate 5 — Matrix assembly: severity-confidence sort**

Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | Recommendation |`

Sort: severity DESC, confidence DESC within tier. Append [DEFERRED] and EXCLUDED ROLES
appendix as appropriate.

If zero findings: HALT [G5] BLOCKING.

**Gate 5.5 — FINDING CONVERGENCE REGISTER**

```
FINDING CONVERGENCE REGISTER:
| Surface    | Roles Citing | Tag          | IC-CHALLENGED | Convergence Effect             |
|------------|--------------|--------------|---------------|--------------------------------|
| [surface]  | [r1,r2,r3]   | CONFIRMED    | IC-01         | IC-01 OVERCOME unconditionally |
| [surface2] | [r1,r2]      | CORROBORATED | none          | Cross-role signal in Gate 9    |
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  CONFIRMED-OVERCOME ICs: [N] (resolved by convergence)
  STANDING ICs at HIGH strength: [N]
  HIGH:   [N] findings
  MEDIUM: [N] findings
  LOW:    [N] findings
  DEFERRED / SCOPED: [N]
```

**Gate 7 — Readiness verdict**

Apply:
1. STANDING IC at HIGH strength (not CONFIRMED-OVERCOME) → BLOCKED.
2. CONFIRMED surface finding → HIGH-effective → BLOCKED if IC-CHALLENGED=none; resolved
   via IC-OVERCOME otherwise.
3. Any remaining HIGH → BLOCKED.
4. Any remaining MEDIUM, no BLOCKED → CONDITIONAL.
5. DEFERRED → minimum CONDITIONAL.
6. Otherwise → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Review CHALLENGE RESPONSE MAP and FINDING CONVERGENCE REGISTER. Assess each IC. For
CONFIRMED-OVERCOME ICs: acknowledge resolution by convergence. For STANDING ICs: assess
whether CONFIDENCE of unchallenging findings reveals a scope gap. Revise readiness if
warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name CONFIRMED-OVERCOME IC(s). Name any STANDING IC with
Confidence=LOW-only challenges (suggesting scope gap, not absence of evidence). Reference
role names. No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run.

**Clean run:**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G3 (IC registry), G4a–G4g (all roles), G4.5, G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  DEFERRED rows: 0
  ICs OVERCOME by convergence: [N]
  Result:        Matrix complete. IC and convergence contracts honored.
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
- `add:{role}` / `depth:deep` / `reload` / `halts` / `halts:{gate-id}` — same as V-01
- `rerun:{role}` — full restart from G4a
- `rerun:challenger` — restart Gate 3 (re-register IC claims)
- `rerun:G4a-{role}` through `rerun:G4g-{role}` — named sub-gate re-entry (skip-map applies)

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID    | Trigger                       | Tier    | Re-entry command                             |
|------------|-------------------------------|---------|----------------------------------------------|
| [G4e-pm]   | IC-CHALLENGED column absent   | SCOPED  | /crew-check {{artifact}} --amend rerun:G4e-pm|
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per skip-map.

---

## V-05

**Axis**: Inertia framing + lifecycle emphasis (V-01 + V-03)
**Hypothesis**: V-01 connects domain findings to registered inertia claims via IC-IDs.
V-03 connects finding severity to artifact maturity via STAGE-APPROPRIATE scope. V-05
combines both: finding rows carry IC-CHALLENGED and STAGE-APPROPRIATE columns; the
CHALLENGE RESPONSE MAP cross-references stage scope — a STANDING IC whose
IC-CHALLENGED=none findings are all STAGE-APPROPRIATE=ADVISORY or NO does not block
readiness, because the unchallenged claim is outside the current review scope. The claim:
when inertia authority and lifecycle scope are both pre-committed, the review can
distinguish "this IC was not challenged because no evidence exists" (genuinely STANDING —
blocks) from "this IC was not challenged because the scope excluded the relevant finding
class" (stage-scoped STANDING — informational only). This prevents APPROVED artifacts
from being blocked by DRAFT-tier concerns that happen to align with registered ICs.

---

You are running `/crew-check`.

Inputs:
```
{{artifact}}: [artifact name or path]
{{depth}}: [standard | deep]
{{stage}}: [DRAFT | REVIEW | APPROVED | DEPRECATED]
```

Acknowledge injected values before executing any gate. If `{{stage}}` not provided,
halt at Gate 0.5 before continuing.

---

### PRE-EXECUTION: SEVERITY CALIBRATION CONTRACT

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW are valid. Any other value triggers HALT [G4c-{role}] BLOCKING.

---

### PRE-EXECUTION: ARTIFACT MATURITY STAGE CONTRACT

| Stage      | STAGE-APPROPRIATE=YES | STAGE-APPROPRIATE=ADVISORY | STAGE-APPROPRIATE=NO             |
|------------|-----------------------|----------------------------|----------------------------------|
| DRAFT      | HIGH, MEDIUM          | LOW                        | (none)                           |
| REVIEW     | HIGH, MEDIUM          | LOW                        | (none)                           |
| APPROVED   | HIGH                  | MEDIUM                     | LOW                              |
| DEPRECATED | (none)                | HIGH, MEDIUM               | LOW                              |

Readiness verdict reads only STAGE-APPROPRIATE=YES rows. ADVISORY rows are surfaced but
do not block. NO rows are listed in STAGE-SCOPE EXCLUSIONS appendix.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                              | Tier     |
|---------------|----------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` not provided or not in valid set                   | BLOCKING |
| G1            | `.craft/roles/` absent or unreadable                           | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims                | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding                    | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface                   | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract                 | BLOCKING |
| G4d-{role}    | Recommendation missing location reference                      | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated                     | SCOPED   |
| G4h-{role}    | STAGE-APPROPRIATE column absent or invalid value               | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED artifact)  | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips             | Safe-skip prerequisite                              |
|-----------------------------|------------|-------------------|-----------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)         | Full role restart                                   |
| `--amend rerun:G4b-{role}`  | G4b        | G4a               | Lens anchor verified                                |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b          | Lens anchor + surface verified                      |
| `--amend rerun:G4d-{role}`  | G4d        | G4a–G4c           | Lens anchor + surface + severity verified           |
| `--amend rerun:G4e-{role}`  | G4e        | G4a–G4d           | All four prior sub-gates verified                   |
| `--amend rerun:G4h-{role}`  | G4h        | G4a–G4d           | Same prerequisite as G4e (parallel sub-gate)        |

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

Populated by challenger at Gate 3. IC-IDs numbered IC-01, IC-02, ...

| IC-ID | Inertia Claim                           | Strength |
|-------|------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]              | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]              | [H/M/L]  |

---

### PRE-EXECUTION: STAGE-SCOPED IC RESOLUTION CONTRACT

After the CHALLENGE RESPONSE MAP, IC Status is qualified by stage scope:

| IC Status (raw) | Challenge finding STAGE-APPROPRIATE values | Stage-qualified IC Status |
|-----------------|---------------------------------------------|---------------------------|
| STANDING        | No challenges at any scope                  | STANDING-GENUINE (blocks) |
| STANDING        | All challenges are ADVISORY or NO scope     | STANDING-SCOPED (advisory)|
| CONTESTED       | All challenges ADVISORY or NO scope         | CONTESTED-SCOPED (advisory)|
| CONTESTED       | Any challenge is YES scope                  | CONTESTED (standard)      |
| OVERCOME        | Any challenge is YES scope + HIGH severity  | OVERCOME (resolved)       |

STANDING-GENUINE ICs at HIGH strength contribute BLOCKED to the readiness verdict.
STANDING-SCOPED ICs at HIGH strength are listed in the priority summary as stage-excluded
— they do not block the current stage verdict but are flagged for the next stage review.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 — Stage acknowledgment**

If `{{stage}}` absent or invalid:
```
HALT [G0.5]: Stage not provided or not in valid set.
→ To continue: /crew-check {{artifact}} --stage [DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING)
```
Otherwise: state "Stage: {{stage}}. Scope calibration active. IC resolution will apply
STAGE-SCOPED IC RESOLUTION CONTRACT."

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active. HIGH=3, MEDIUM=2, LOW=1."

**Gate 3 — Challenger: opening bracket and inertia claim registration**

Inertia-advocate first. Populate INERTIA CLAIM REGISTRY with >= 2 IC-IDs. For each:
name the specific existing capability. Assign Strength (H/M/L). Note which ICs are most
relevant to the current lifecycle stage (e.g., for APPROVED stage, IC claims about
regression prevention carry more weight than workflow-productivity claims).

On fewer than 2 claims:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
→ To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING)
```
After: emit "Inertia registry locked. IC-01 through IC-[N] registered.
Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a — Lens anchor* | BLOCKING on missing
*G4b — Surface finding*:
Format: `| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | IC-CHALLENGED | Recommendation |`

*G4c — Severity validation* | BLOCKING on invalid
*G4d — Recommendation completeness* | BLOCKING on missing location
*G4e — IC-CHALLENGED column*: SCOPED on absent/unpopulated (role excluded)
*G4h — STAGE-APPROPRIATE derivation*: DEFERRED on absent/invalid (row tagged)

All halt messages embed re-entry commands per skip-map:
```
HALT [G4x-{role}]: [trigger].
→ To continue: /crew-check {{artifact}} --amend rerun:G4x-{role}
  (skip-map: [skipped gates] — [prerequisite]; [tier note])
```

**Gate 4.5 — CHALLENGE RESPONSE MAP with stage-scoped IC resolution**

For each IC-ID, collect all findings that cite it. Then apply STAGE-SCOPED IC RESOLUTION
CONTRACT: for each IC, check whether the challenging findings are YES-scope, ADVISORY,
or NO-scope per ARTIFACT MATURITY STAGE CONTRACT.

```
CHALLENGE RESPONSE MAP:
| IC-ID | Strength | Challenging Findings (Role — Sev — Stage-Appropriate) | Stage-Qualified IC Status |
|-------|----------|-------------------------------------------------------|---------------------------|
| IC-01 | H        | [pm — MEDIUM — YES], [arch — HIGH — YES]              | OVERCOME                  |
| IC-02 | H        | [pm — HIGH — ADVISORY]                                | STANDING-SCOPED           |
| IC-03 | M        | (none)                                                | STANDING-GENUINE          |
```

**Gate 5 — Matrix assembly and sort**

Schema: `| Role | Finding | Surface | Severity | STAGE-APPROPRIATE | IC-CHALLENGED | Recommendation |`

Sort: severity DESC. Within tier: YES-scope rows before ADVISORY rows before NO-scope
rows. Append [DEFERRED] and EXCLUDED ROLES appendix as appropriate.

If zero STAGE-APPROPRIATE=YES findings for non-DEPRECATED artifact: HALT [G5] BLOCKING.

Append STAGE-SCOPE EXCLUSIONS if any STAGE-APPROPRIATE=NO rows exist.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  STANDING-GENUINE ICs at HIGH strength: [N] (blocks readiness)
  STANDING-SCOPED ICs at HIGH strength:  [N] (advisory — flagged for next stage)
  In-scope HIGH:   [N] | MEDIUM: [N] | LOW: [N]
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N]
  Excluded (STAGE-APPROPRIATE=NO):       [N]
  DEFERRED / SCOPED: [N]
```

**Gate 7 — Readiness verdict**

Apply in order:
1. Any STANDING-GENUINE IC at HIGH strength → BLOCKED.
2. Any YES-scope HIGH finding → BLOCKED.
3. Any YES-scope MEDIUM, no BLOCKED → CONDITIONAL.
4. DEFERRED → minimum CONDITIONAL.
5. DEPRECATED artifact → always READY with advisory appendix.
6. Otherwise → READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
If STANDING-SCOPED contributed: append `(N ICs STANDING-SCOPED — flagged for next stage)`

**Gate 8 — Challenger: closing bracket**

Review the CHALLENGE RESPONSE MAP with stage-qualified IC statuses. For each
STANDING-SCOPED IC: explain which scope limitation prevented challenge and what finding
class would resolve it at the next lifecycle stage. For STANDING-GENUINE ICs: assess
whether the absence of challenges reveals a scope gap (reviewer set too narrow) or a
genuine status-quo strength. Revise readiness only if stage-qualification changes the
verdict.

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name any STANDING-GENUINE ICs and the roles that had opportunity but did
not challenge them. Name any STANDING-SCOPED ICs and note the stage transition at which
they become load-bearing. Reference role names. No new findings.

---

### RUN HEALTH

Emitted after Gate 9 on every run.

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a–G4h (all roles), G4.5, G5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  DEFERRED rows: 0
  STANDING-GENUINE ICs: [N] | STANDING-SCOPED ICs: [N]
  Result:        Stage-scoped IC-accountable matrix complete.
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
- `add:{role}` / `depth:deep` / `reload` / `halts` / `halts:{gate-id}` — standard
- `stage:{value}` — change maturity stage (restarts from Gate 0.5)
- `rerun:{role}` — full restart from G4a
- `rerun:challenger` — restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4h-{role}` — named sub-gate re-entry (skip-map applies)

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID    | Trigger                           | Tier    | Re-entry command                                   |
|------------|-----------------------------------|---------|----------------------------------------------------|
| [G4e-pm]   | IC-CHALLENGED column absent       | SCOPED  | /crew-check {{artifact}} --amend rerun:G4e-pm      |
| [G4h-arch] | STAGE-APPROPRIATE column absent   | DEFERRED| /crew-check {{artifact}} --amend rerun:G4h-arch    |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per skip-map.
