---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 9
rubric: crew-check-rubric-v8-2026-03-17.md
---

# crew-check — Variate R9

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds).

Base for all variations: R8 V-05 (128/128 under v7 rubric). R9 adds three axes:

New criteria targeted in R9:
- C-28: SOLO convergence tier and disposition protocol (extends C-25)
  Gate 9 emits a SOLO FINDINGS table; each entry carries ESCALATE / DISMISS:rationale
  / ROLE-SPECIFIC disposition tag; SOLO tier has mandatory disposition path.
- C-29: Mid-run convergence snapshot gate (extends C-09/C-25)
  Gate 5.5 emits tier COUNTS (CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO) grouped
  by surface; early-abort halt fires if convergence count is zero before synthesis.
- C-30: Stage-aware RUN HEALTH certificate (extends C-21/C-26)
  RUN HEALTH includes Stage field (declared value) and a SCOPE DISTRIBUTION table with
  YES / ADVISORY / NO / DEPRECATED counts; both fields present in clean and failed variants.

Dependency chain (unchanged from v7, carried forward):
- C-28 extends C-25: SOLO tier requires convergence register in place.
- C-29 extends C-09 / C-25: mid-run snapshot requires named convergence tiers to count.
- C-30 extends C-21 / C-26: stage-aware certificate requires stage declared at G0.5.

Axes selected for R9:
- V-01: C-28 only — SOLO disposition protocol (mandatory Gate 9 SOLO FINDINGS table,
  disposition tags; FINDING CONVERGENCE CONTRACT updated to name disposition obligation)
- V-02: C-29 only — mid-run convergence snapshot (Gate 5.5 emits counts by tier;
  PRE-EXECUTION CONVERGENCE SNAPSHOT CONTRACT declares threshold and early-abort)
- V-03: C-30 only — stage-aware RUN HEALTH (SCOPE DISTRIBUTION table in both RUN
  HEALTH variants; Stage field in failed variant)
- V-04: C-28 + C-29 — SOLO disposition + snapshot counts combined
- V-05: C-28 + C-29 + C-30 — full three-axis integration

---

## V-01

**Axis**: C-28 — SOLO convergence tier and disposition protocol
**Hypothesis**: R8 V-05 names SOLO in the FINDING CONVERGENCE CONTRACT as "Normal
weight" with no downstream action requirement. Findings raised by exactly one role
enter Gate 9 prose and may influence the synthesis narrative without any obligation
to explain why only one lens detected them. V-01 R9 adds a mandatory Gate 9 SOLO
FINDINGS table that forces disposition of every SOLO finding before the run ends.
Each entry must carry one of three tags: ESCALATE (warrants deep review or additional
role), DISMISS:rationale (explainable noise with stated reason), or ROLE-SPECIFIC
(valid only from this lens; no cross-role action expected). Without this step, a
SOLO HIGH-severity finding and a SOLO LOW-severity finding are both silently absorbed
into synthesis prose — the mechanism that distinguishes "only one person saw this"
from "only the right person saw this" doesn't exist. The claim: when SOLO disposition
is mandatory, non-converging findings are either promoted toward re-review (ESCALATE)
or retired with an explanation (DISMISS / ROLE-SPECIFIC) — both outcomes more useful
than ambient inclusion.

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

Matrix sort: scope-grouped first (YES -> ADVISORY -> NO/DEPRECATED), then within each
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

| Tier          | Criteria                                                               | Readiness effect                           | Gate 9 obligation                              |
|---------------|------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------|
| CONFIRMED     | Same Surface, 2+ roles, ALL same Confidence tier, tier != LOW, YES-scope | HIGH-effective in Gate 7                  | Named in synthesis; no disposition required    |
| CONFIRMED-LOW | Same Surface, 2+ roles, ALL Confidence=LOW, YES-scope                  | Flagged for Gate 9; NOT HIGH-effective     | Enumerated in LOW findings table               |
| CORROBORATED  | Same Surface, 2+ roles, Confidence tiers differ, YES-scope             | Convergence signal; no automatic promotion | Named in synthesis                             |
| SOLO          | Surface cited by exactly 1 role (any scope group)                     | Normal weight                              | MANDATORY disposition in SOLO FINDINGS table   |

SOLO disposition tags (one required per SOLO finding at Gate 9):
| Tag                 | Meaning                                                                              |
|---------------------|--------------------------------------------------------------------------------------|
| ESCALATE            | Finding warrants additional reviewer or deep-mode re-run before verdict is final     |
| DISMISS:rationale   | Finding explainable as role-specific noise; rationale required                       |
| ROLE-SPECIFIC       | Finding valid only from this lens; no cross-role action expected; no further action  |

Convergence register computed over YES-scope rows. ADVISORY and NO rows excluded from
CONFIRMED / CORROBORATED / CONFIRMED-LOW tiers. SOLO applies to any scope group.

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
| G1            | `.roles/` absent or unreadable                                 | BLOCKING |
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
| `--amend rerun:G4d-{role}`  | G4d        | G4a-G4c       | Lens anchor + surface + severity verified                    |
| `--amend rerun:G4e-{role}`  | G4e        | G4a-G4d       | Lens anchor + surface + severity + location verified         |
| `--amend rerun:G4f-{role}`  | G4f        | G4a-G4e       | All prior sub-gates + IC-CHALLENGED verified                 |
| `--amend rerun:G4g-{role}`  | G4g        | G4a-G4f       | All prior sub-gates + confidence label verified              |
| `--amend rerun:G4h-{role}`  | G4h        | G4a-G4g       | All prior sub-gates verified                                 |

---

### REVIEWER PRIORITY MANIFEST

Read `.roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

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
-> To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING -- no gate proceeds until stage is declared)
```

Otherwise: state "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings receive STAGE-APPROPRIATE=DEPRECATED. Readiness will be
READY regardless of content. Run continues for informational record."

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .roles/ absent or unreadable.
-> To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
Stage: {{stage}}. Matrix: scope-grouped (YES->ADVISORY->NO), then severity DESC,
confidence DESC within group.
CONFIRMED (same surface + matching confidence tier != LOW, 2+ roles, YES-scope)
  treated as HIGH-effective in Gate 7.
SOLO findings require mandatory disposition at Gate 9 (ESCALATE / DISMISS:rationale
  / ROLE-SPECIFIC).
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
-> To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING -- no domain review proceeds until registry has >= 2 entries)
```

After populating: emit "Inertia registry locked. IC-01 through IC-[N] registered.
Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a -- Lens anchor*: "From the [role] perspective, this review examines [surface]."
On missing:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
-> To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING -- full role restart)
```

*G4b -- Surface finding*: Format:
`| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`
For DEPRECATED: STAGE-APPROPRIATE=DEPRECATED on all rows.
On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
-> To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c -- Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
-> To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d -- Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
-> To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a-G4c skipped)
```

*G4e -- IC-CHALLENGED column*: Every finding row must carry IC-CHALLENGED = IC-[N]
(comma-separated for multiple) or `none`. Absent column triggers SCOPED halt:
```
HALT [G4e-{role}]: IC-CHALLENGED column absent or unpopulated.
-> Role {role} excluded from matrix. Run continues.
-> To include: /crew-check {{artifact}} --amend rerun:G4e-{role}
  (skip-map: G4a-G4d skipped)
  (SCOPED -- EXCLUDED ROLES appendix will be appended)
```

*G4f -- Confidence validation*:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
-> To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a-G4e skipped)
```

*G4g -- Confidence column presence*:
```
HALT [G4g-{role}]: Confidence column absent -- row included as [DEFERRED].
-> Readiness verdict forced to CONDITIONAL.
-> To fix: /crew-check {{artifact}} --amend rerun:G4g-{role}
  (skip-map: G4a-G4f skipped; DEFERRED -- run continues)
```

*G4h -- STAGE-APPROPRIATE derivation*: Per ARTIFACT MATURITY STAGE CONTRACT.
Value must be in {YES, ADVISORY, NO, DEPRECATED}. On absent or invalid:
```
HALT [G4h-{role}]: STAGE-APPROPRIATE column absent or invalid -- row included as [DEFERRED].
-> Readiness verdict forced to CONDITIONAL.
-> To fix: /crew-check {{artifact}} --amend rerun:G4h-{role}
  (skip-map: G4a-G4g skipped; DEFERRED -- run continues)
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

After all domain roles complete, assemble the CHALLENGE RESPONSE MAP. For each IC-ID,
list every YES-scope finding row that cited it.

```
| IC-ID | Strength | Challenging Findings (Role -- Sev/Conf, STAGE-APPROPRIATE) | IC Status  |
|-------|----------|-------------------------------------------------------------|------------|
| IC-01 | H        | [pm -- HIGH/HIGH, YES], [architect -- MEDIUM/HIGH, YES]     | OVERCOME   |
| IC-02 | M        | [pm -- LOW/LOW, YES]                                        | CONTESTED  |
| IC-03 | H        | (none in YES scope)                                         | STANDING   |
```

IC Status (YES-scope findings only):
- OVERCOME: IC cited by >= 1 YES-scope finding at HIGH severity.
- CONTESTED: IC cited by YES-scope findings, none at HIGH severity.
- STANDING: IC cited by no YES-scope finding.

CONFIRMED findings (same surface + matching confidence tier != LOW, 2+ roles) that
challenge an IC in YES scope: mark IC as OVERCOME-CONFIRMED.

Emit CHALLENGE RESPONSE MAP before Gate 5.

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted**

Assemble all staged rows. Group by STAGE-APPROPRIATE first, then sort severity DESC,
confidence DESC within each group. Append [DEFERRED] to G4g/G4h-affected rows.

Group order:
1. YES group (severity DESC, confidence DESC) -- verdict input
2. ADVISORY group (severity DESC, confidence DESC) -- noted, not blocking
3. NO group -- STAGE-SCOPE EXCLUSIONS appendix
4. DEPRECATED group -- DEPRECATED-FINDINGS appendix
5. EXCLUDED ROLES appendix (SCOPED G4e halts)

Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

For non-DEPRECATED artifact: if zero YES-scope rows after G4:
```
HALT [G5]: Zero stage-appropriate findings for {{stage}} artifact.
-> To continue: /crew-check {{artifact}} --amend depth:deep
  Or: /crew-check {{artifact}} --amend stage:[correct-stage]
```

**Gate 5.5 — FINDING CONVERGENCE REGISTER** (YES-scope rows only)

Group YES-scope rows by Surface. For each Surface cited by 2+ YES-scope roles:
- All same confidence tier, tier != LOW: CONFIRMED.
- All same confidence tier, tier = LOW: CONFIRMED-LOW.
- Confidence tiers differ: CORROBORATED.
Surfaces cited by exactly 1 role (any scope): SOLO.

```
FINDING CONVERGENCE REGISTER (YES-scope):
| Surface   | Roles (Sev/Conf)                  | Tier          | IC Impact                  | Readiness Effect         |
|-----------|-----------------------------------|---------------|----------------------------|--------------------------|
| [surface] | [pm HIGH/HIGH],[arch HIGH/HIGH]   | CONFIRMED     | IC-01 -> OVERCOME-CONFIRMED| HIGH-effective           |
| [surface] | [pm MED/LOW],[arch MED/LOW]       | CONFIRMED-LOW | IC-02 -> CONTESTED (weak)  | Flagged for Gate 9       |
| [surface] | [pm HIGH/HIGH],[arch HIGH/MED]    | CORROBORATED  | none                       | Synthesis signal only    |
| [surface] | [pm MEDIUM/HIGH]                  | SOLO          | IC-03 -> none              | Disposition required G9  |
```

If no surface is cited by 2+ YES-scope roles: emit "No cross-role convergence detected.
All YES-scope findings are SOLO. Proceed to Gate 9 for mandatory SOLO disposition."

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  In-scope (STAGE-APPROPRIATE=YES):
    CONFIRMED (non-LOW, HIGH-effective): [N] surfaces -- [names]
    HIGH:    [N] findings
    MEDIUM:  [N] findings ([N] promoted via CONFIRMED)
    LOW:     [N] findings
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N] findings -- noted, not blocking
  Excluded (STAGE-APPROPRIATE=NO):       [N] findings -- below scope floor
  Deprecated:  [N] findings -- informational only
  Convergence: CONFIRMED-LOW [N], CORROBORATED [N], SOLO [N]
  Inertia: STANDING HIGH-strength ICs: [N]
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

For DEPRECATED artifact:
`READINESS: READY (artifact is DEPRECATED -- all findings informational; see appendix)`

For non-DEPRECATED, apply to STAGE-APPROPRIATE=YES rows only:
1. Any CONFIRMED (non-LOW) surface -> HIGH-effective -> BLOCKED.
2. Any YES-scope HIGH finding -> BLOCKED.
3. Any STANDING IC at HIGH strength -> BLOCKED (regardless of finding severity).
4. Any YES-scope MEDIUM finding (non-CONFIRMED or CONFIRMED-LOW), no HIGH or CONFIRMED
   or STANDING-HIGH -> CONDITIONAL.
5. Any DEFERRED row -> minimum CONDITIONAL.
6. Otherwise -> READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
Append attribution for each active blocker:
- `(confirmed evidence: [N] CONFIRMED surfaces treated as HIGH-effective)`
- `(inertia: IC-[N] STANDING at HIGH strength)`
- `(scope: {{stage}} -- [N] YES-scope findings; [N] ADVISORY; [N] excluded)`

**Gate 8 — Challenger: closing bracket and CHALLENGE RESPONSE MAP review**

Review the CHALLENGE RESPONSE MAP for each IC:
- OVERCOME or OVERCOME-CONFIRMED: acknowledge; name the finding(s) that overcame it.
- CONTESTED: name what additional evidence would make it OVERCOME.
- STANDING: explain why no YES-scope domain reviewer challenged this IC.

Note ADVISORY findings representing latent IC risk at next stage transition.
Revise readiness only if YES-scope or STANDING IC analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 — Cross-role synthesis and SOLO disposition**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface and its significance.

Then emit the mandatory Confidence=LOW enumeration:

```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
|------|---------|----------|---------------|-------------------|-----------------|
| ...  | ...     | ...      | ...           | ...               | ...             |
```

Then emit the mandatory SOLO FINDINGS table. Every SOLO finding from the convergence
register must appear here with a disposition tag. Omitting a SOLO finding or leaving
its disposition blank is a contract violation.

```
SOLO FINDINGS (mandatory disposition required):
| Role | Surface | Severity | Confidence | Finding summary | Disposition                  |
|------|---------|----------|------------|-----------------|------------------------------|
| ...  | ...     | ...      | ...        | ...             | ESCALATE | DISMISS:rationale | ROLE-SPECIFIC |
```

Disposition semantics:
- ESCALATE: warrants additional reviewer or `--amend add:{role}` before final verdict.
- DISMISS:rationale: explain why this finding is role-specific noise (rationale required).
- ROLE-SPECIFIC: valid only from this lens; no cross-role action expected.

If no SOLO findings: emit "No SOLO findings. All surfaces cited by 2+ roles."
State whether any CONFIRMED-LOW surface would change IC status or readiness verdict if
confidence could be elevated. Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a-G4h (all roles), G4.5,
                 G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  DEFERRED rows: 0
  CONFIRMED surfaces (non-LOW, HIGH-effective): [N]
  CONFIRMED-LOW (flagged): [N]
  SOLO findings (disposed): [N] (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])
  STANDING HIGH ICs: [N]
  YES-scope / ADVISORY / excluded: [N] / [N] / [N]
  Result:        Matrix complete. All contracts honored. SOLO disposition complete.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` -- add a specific reviewer
- `depth:deep` -- re-run with all roles
- `stage:{value}` -- change artifact maturity stage; restarts from Gate 0.5
- `rerun:{role}` -- full role restart from G4a
- `rerun:challenger` -- restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4h-{role}` -- re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` -- re-load `.roles/` and restart
- `halts` -- list all gates that fired in this run
- `halts:{gate-id}` -- show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT -- [N] gate(s) fired this run:
| Gate ID        | Trigger description                  | Tier     | Re-entry command                                        |
|----------------|--------------------------------------|----------|---------------------------------------------------------|
| [G0.5]         | Stage 'WIP' not in valid set         | BLOCKING | /crew-check {{artifact}} --amend stage:DRAFT            |
| [G4e-pm]       | IC-CHALLENGED column absent          | SCOPED   | /crew-check {{artifact}} --amend rerun:G4e-pm           |
```
Each entry is paste-ready. Re-entry command encodes minimum-restart routing per
SUB-GATE SKIP-MAP.

---

## V-02

**Axis**: C-29 -- Mid-run convergence snapshot gate with counts and early-abort
**Hypothesis**: R8 V-05 Gate 5.5 emits a surface-by-surface convergence register
as a table of individual rows. A reviewer can see which surfaces converge and how,
but must count rows to assess convergence density. More critically, Gate 5.5 does
not block: even when every finding is SOLO (zero cross-role agreement), execution
proceeds to Gate 9, which is contractually required to name ">= 1 cross-role
convergence or conflict" -- a requirement it cannot honestly satisfy. V-02 R9 adds
a PRE-EXECUTION CONVERGENCE SNAPSHOT CONTRACT that declares a count-level threshold
and an early-abort halt. Gate 5.5 is restructured: it emits tier counts first
(CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO), then the surface table, then
evaluates the early-abort condition. If zero cross-role signals exist (all SOLO),
Gate 5.5 halts with a named ID before synthesis, recommending `--amend depth:deep`
or `--amend add:{role}` to surface additional reviewers. The claim: when Gate 5.5
has count-level output and an early-abort path, the convergence checkpoint is a
genuine gate rather than an accumulation step -- synthesis runs only when there is
something to synthesize.

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

Matrix sort: scope-grouped first (YES -> ADVISORY -> NO/DEPRECATED), then within each
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
| SOLO         | Surface cited by exactly 1 role (any scope group)                     | Normal weight                              |

Convergence register computed over YES-scope rows. ADVISORY and NO rows excluded from
CONFIRMED / CORROBORATED / CONFIRMED-LOW tiers. SOLO applies to any scope group.

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after the last domain role review completes
and before Gate 6 (priority summary) and Gate 9 (synthesis).

Gate 5.5 must emit:
1. Tier counts: CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO as labeled fields.
2. Surface table: per-surface convergence detail (tier, roles, readiness effect).

Early-abort condition: if CONFIRMED count = 0 AND CORROBORATED count = 0
(all YES-scope findings are SOLO or CONFIRMED-LOW), Gate 5.5 emits HALT [G5.5]:

```
HALT [G5.5]: Zero cross-role convergence detected.
  CONFIRMED: 0, CORROBORATED: 0. All YES-scope findings are SOLO or CONFIRMED-LOW.
  Gate 9 synthesis cannot name a cross-role convergence from available evidence.
-> To continue with additional coverage:
   /crew-check {{artifact}} --amend depth:deep
   /crew-check {{artifact}} --amend add:{role}
-> To accept SOLO-only synthesis (waive convergence requirement):
   /crew-check {{artifact}} --amend waive:convergence
  (BLOCKING unless waived)
```

`--amend waive:convergence` restarts from Gate 9 with the note "Convergence waived:
synthesis proceeds with SOLO-only findings. Gate 9 cross-role convergence requirement
replaced by SOLO disposition requirement."

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
more IC-IDs (comma-separated) or `none`.
An absent IC-CHALLENGED column triggers HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: HALT REGISTRY

G0.5 appears before G1. G5.5 appears after G5 -- fires before Gate 6 and Gate 9.

| Halt ID       | Trigger condition                                                    | Tier     |
|---------------|----------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}  | BLOCKING |
| G1            | `.roles/` absent or unreadable                                 | BLOCKING |
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
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 does not fire for DEPRECATED artifacts.
G5.5 may be waived via `--amend waive:convergence`.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips         | Safe-skip prerequisite                                       |
|-----------------------------|------------|---------------|--------------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4b-{role}`  | G4b        | G4a           | Lens anchor verified                                         |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b      | Lens anchor + named surface verified                         |
| `--amend rerun:G4d-{role}`  | G4d        | G4a-G4c       | Lens anchor + surface + severity verified                    |
| `--amend rerun:G4e-{role}`  | G4e        | G4a-G4d       | Lens anchor + surface + severity + location verified         |
| `--amend rerun:G4f-{role}`  | G4f        | G4a-G4e       | All prior sub-gates + IC-CHALLENGED verified                 |
| `--amend rerun:G4g-{role}`  | G4g        | G4a-G4f       | All prior sub-gates + confidence label verified              |
| `--amend rerun:G4h-{role}`  | G4h        | G4a-G4g       | All prior sub-gates verified                                 |

---

### REVIEWER PRIORITY MANIFEST

Read `.roles/`. If absent: emit `HALT [G1]` (see HALT REGISTRY).

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
-> To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING -- no gate proceeds until stage is declared)
```

Otherwise: state "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings receive STAGE-APPROPRIATE=DEPRECATED. Readiness will be
READY regardless of content. Run continues for informational record."

**Gate 1 — Role registry load**

On failure:
```
HALT [G1]: .roles/ absent or unreadable.
-> To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active.
Severity: HIGH=3, MEDIUM=2, LOW=1.
Confidence: HIGH=3 (direct evidence), MEDIUM=2 (inferred), LOW=1 (speculative).
Stage: {{stage}}. Matrix: scope-grouped (YES->ADVISORY->NO), then severity DESC,
confidence DESC within group.
CONFIRMED (same surface + matching confidence tier != LOW, 2+ roles, YES-scope)
  treated as HIGH-effective in Gate 7.
Gate 5.5 convergence snapshot fires after all role reviews. Early-abort at G5.5 if
  CONFIRMED=0 and CORROBORATED=0.
STANDING IC at HIGH strength blocks readiness regardless of finding severity.
IC-CHALLENGED required on every finding row."

**Gate 3 — Challenger: opening bracket and inertia claim registration**

Inertia-advocate runs first. Populate the INERTIA CLAIM REGISTRY with >= 2 numbered
claims. For each: name the specific existing capability or argument. Assign Strength (H/M/L).
Note which claims are most relevant given `{{stage}}`.

On fewer than 2 claims:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
-> To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING)
```

Emit "Inertia registry locked. Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

For each role:

*G4a -- Lens anchor*: "From the [role] perspective, this review examines [surface]."
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
-> To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (BLOCKING)
```

*G4b -- Surface finding*: Format:
`| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
-> To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
  (skip-map: G4a skipped)
```

*G4c -- Severity validation*:
```
HALT [G4c-{role}]: Severity '{value}' not in calibration contract.
-> To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
  (skip-map: G4a, G4b skipped)
```

*G4d -- Recommendation completeness*:
```
HALT [G4d-{role}]: Recommendation missing location reference.
-> To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a-G4c skipped)
```

*G4e -- IC-CHALLENGED column*:
```
HALT [G4e-{role}]: IC-CHALLENGED column absent or unpopulated.
-> Role {role} excluded from matrix. Run continues.
-> To include: /crew-check {{artifact}} --amend rerun:G4e-{role}
  (SCOPED -- EXCLUDED ROLES appendix will be appended)
```

*G4f -- Confidence validation*:
```
HALT [G4f-{role}]: Confidence '{value}' not in calibration contract.
-> To continue: /crew-check {{artifact}} --amend rerun:G4f-{role}
  (skip-map: G4a-G4e skipped)
```

*G4g -- Confidence column presence*:
```
HALT [G4g-{role}]: Confidence column absent -- row included as [DEFERRED].
-> Readiness verdict forced to CONDITIONAL.
  (skip-map: G4a-G4f skipped; DEFERRED)
```

*G4h -- STAGE-APPROPRIATE derivation*:
```
HALT [G4h-{role}]: STAGE-APPROPRIATE column absent or invalid -- row included as [DEFERRED].
-> Readiness verdict forced to CONDITIONAL.
  (skip-map: G4a-G4g skipped; DEFERRED)
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

After all domain roles complete, assemble the CHALLENGE RESPONSE MAP.

```
| IC-ID | Strength | Challenging Findings (Role -- Sev/Conf, STAGE-APPROPRIATE) | IC Status  |
|-------|----------|-------------------------------------------------------------|------------|
```

IC Status: OVERCOME (>= 1 HIGH), CONTESTED (challenged, no HIGH), STANDING (unchallenged).
CONFIRMED challenges -> OVERCOME-CONFIRMED.
Emit before Gate 5.

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted**

Assemble rows. Group by STAGE-APPROPRIATE, then sort severity DESC, confidence DESC
within each group.

Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

If zero YES-scope rows (non-DEPRECATED):
```
HALT [G5]: Zero stage-appropriate findings.
-> /crew-check {{artifact}} --amend depth:deep
```

**Gate 5.5 — CONVERGENCE SNAPSHOT** (fires after Gate 5, before Gate 6)

Count convergence tiers across YES-scope rows. Emit counts first, then surface table.

```
CONVERGENCE SNAPSHOT (YES-scope):
  CONFIRMED:     [N] surfaces
  CONFIRMED-LOW: [N] surfaces
  CORROBORATED:  [N] surfaces
  SOLO:          [N] surfaces (any scope)
```

If CONFIRMED = 0 AND CORROBORATED = 0:
```
HALT [G5.5]: Zero cross-role convergence detected.
  CONFIRMED: 0, CORROBORATED: 0. All YES-scope findings are SOLO or CONFIRMED-LOW.
  Gate 9 cannot name a cross-role convergence from available evidence.
-> To continue: /crew-check {{artifact}} --amend depth:deep
-> Or: /crew-check {{artifact}} --amend add:{role}
-> Or waive: /crew-check {{artifact}} --amend waive:convergence
  (BLOCKING unless waived)
```

Then emit the surface detail table:
```
CONVERGENCE REGISTER:
| Surface   | Roles (Sev/Conf)                  | Tier          | IC Impact                  | Readiness Effect         |
|-----------|-----------------------------------|---------------|----------------------------|--------------------------|
| [surface] | [pm HIGH/HIGH],[arch HIGH/HIGH]   | CONFIRMED     | IC-01 -> OVERCOME-CONFIRMED| HIGH-effective           |
| [surface] | [pm MED/LOW],[arch MED/LOW]       | CONFIRMED-LOW | none                       | Flagged for Gate 9       |
| [surface] | [pm MEDIUM/HIGH]                  | SOLO          | none                       | Normal weight            |
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  In-scope (STAGE-APPROPRIATE=YES):
    CONFIRMED (non-LOW, HIGH-effective): [N] surfaces -- [names]
    HIGH:    [N] findings
    MEDIUM:  [N] findings ([N] promoted via CONFIRMED)
    LOW:     [N] findings
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N] findings
  Excluded (STAGE-APPROPRIATE=NO):       [N] findings
  Deprecated:  [N] findings
  Convergence snapshot: CONFIRMED [N], CONFIRMED-LOW [N], CORROBORATED [N], SOLO [N]
  Inertia: STANDING HIGH-strength ICs: [N]
  DEFERRED rows: [N]
```

**Gate 7 — Readiness verdict**

For DEPRECATED: `READINESS: READY (DEPRECATED -- informational only)`

For non-DEPRECATED, YES-scope rows only:
1. Any CONFIRMED (non-LOW) -> BLOCKED.
2. Any YES-scope HIGH -> BLOCKED.
3. Any STANDING IC at HIGH -> BLOCKED.
4. Any YES-scope MEDIUM (non-CONFIRMED or CONFIRMED-LOW), no blocking -> CONDITIONAL.
5. Any DEFERRED row -> minimum CONDITIONAL.
6. Otherwise -> READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Review CHALLENGE RESPONSE MAP. Note CONFIRMED convergence evidence vs STANDING ICs.
Note ADVISORY latent risk. Revise readiness only if YES-scope analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 — Cross-role synthesis**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface (if waived, describe SOLO
pattern). Then mandatory Confidence=LOW enumeration:

```
CONFIDENCE=LOW FINDINGS:
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
|------|---------|----------|---------------|-------------------|-----------------|
```

State whether CONFIRMED-LOW would change verdict if elevated. Reference role names.
No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a-G4h (all roles), G4.5,
                 G5, G5.5 (snapshot), G6, G7, G8, G9
  Halts fired:   0
  G5.5 waived:   NO
  SCOPED roles:  0
  DEFERRED rows: 0
  Convergence snapshot: CONFIRMED [N], CONFIRMED-LOW [N], CORROBORATED [N], SOLO [N]
  STANDING HIGH ICs: [N]
  YES-scope / ADVISORY / excluded: [N] / [N] / [N]
  Result:        Matrix complete. Convergence snapshot passed. All contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` -- add a specific reviewer
- `depth:deep` -- re-run with all roles
- `stage:{value}` -- change artifact maturity stage; restarts from Gate 0.5
- `waive:convergence` -- waive G5.5 early-abort; restarts from Gate 9 with SOLO-only note
- `rerun:{role}` -- full role restart from G4a
- `rerun:challenger` -- restart Gate 3
- `rerun:G4a-{role}` through `rerun:G4h-{role}` -- re-enter at named sub-gate
- `reload` -- re-load `.roles/` and restart
- `halts` -- list all gates that fired in this run

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT -- [N] gate(s) fired this run:
| Gate ID        | Trigger description                    | Tier     | Re-entry command                                          |
|----------------|----------------------------------------|----------|-----------------------------------------------------------|
| [G5.5]         | CONFIRMED=0, CORROBORATED=0            | BLOCKING | /crew-check {{artifact}} --amend depth:deep               |
| [G4e-pm]       | IC-CHALLENGED column absent            | SCOPED   | /crew-check {{artifact}} --amend rerun:G4e-pm             |
```

---

## V-03

**Axis**: C-30 -- Stage-aware RUN HEALTH certificate
**Hypothesis**: R8 V-05 RUN HEALTH (clean variant) includes `Stage: {{stage}}` and
a one-line scope summary: `YES-scope / ADVISORY / excluded: [N] / [N] / [N]`. But
the failed variant lists only halts and recovery commands -- no Stage field, no scope
distribution. A reviewer debugging a failed run cannot see what stage was declared or
how findings distributed across scope groups without re-reading the full transcript.
Additionally, "excluded" conflates NO-scope and DEPRECATED findings into one count,
hiding the distinction that is load-bearing for verdict derivation (NO = outside scope;
DEPRECATED = entire artifact retired). V-03 R9 extends RUN HEALTH in both variants:
the Stage field is present in clean and failed; a SCOPE DISTRIBUTION table (four
named columns: YES / ADVISORY / NO / DEPRECATED) replaces the one-line summary in
clean and is added to failed. The claim: when RUN HEALTH is a standalone diagnostic
artifact -- not dependent on transcript context to interpret -- reviewers can verify
scope calibration without re-executing the run.

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

Matrix sort: scope-grouped first (YES -> ADVISORY -> NO/DEPRECATED), then within each
scope group: severity DESC, confidence DESC.

Readiness: CONFIRMED surface treated as HIGH-effective in Gate 7 for YES-scope rows.

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
| SOLO         | Surface cited by exactly 1 role (any scope group)                     | Normal weight                              |

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

| IC-ID | Inertia Claim                                               | Strength |
|-------|-------------------------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                                 | [H/M/L]  |

IC-CHALLENGED: every finding row carries IC-CHALLENGED = IC-[N] or `none`.
Absent: HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT

RUN HEALTH emits a SCOPE DISTRIBUTION table in BOTH clean and failed variants.

SCOPE DISTRIBUTION format (structured table, not prose):
```
SCOPE DISTRIBUTION ({{stage}}):
| Group      | Count | Verdict contribution                |
|------------|-------|-------------------------------------|
| YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
| ADVISORY   | [N]   | Noted; not blocking                 |
| NO         | [N]   | Excluded (scope floor)              |
| DEPRECATED | [N]   | Informational only                  |
```

Stage field must carry the declared value (not a placeholder).
Both clean and failed variants must include Stage field and SCOPE DISTRIBUTION.

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                                    | Tier     |
|---------------|----------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}  | BLOCKING |
| G1            | `.roles/` absent or unreadable                                 | BLOCKING |
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
| `--amend rerun:G4d-{role}`  | G4d        | G4a-G4c       | Lens anchor + surface + severity verified                    |
| `--amend rerun:G4e-{role}`  | G4e        | G4a-G4d       | Lens anchor + surface + severity + location verified         |
| `--amend rerun:G4f-{role}`  | G4f        | G4a-G4e       | All prior + IC-CHALLENGED verified                           |
| `--amend rerun:G4g-{role}`  | G4g        | G4a-G4f       | All prior + confidence label verified                        |
| `--amend rerun:G4h-{role}`  | G4h        | G4a-G4g       | All prior verified                                           |

---

### REVIEWER PRIORITY MANIFEST

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

---

### EXECUTION

[Gates 0.5 through 4.5 identical to V-01, including IC registry and CHALLENGE RESPONSE MAP]

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted**

Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

Group order: YES -> ADVISORY -> NO -> DEPRECATED -> EXCLUDED ROLES.

**Gate 5.5 — FINDING CONVERGENCE REGISTER** (YES-scope rows only)

Same as R8 V-05 Gate 5.5.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  CONFIRMED (non-LOW, HIGH-effective): [N]
  HIGH: [N] / MEDIUM: [N] / LOW: [N] (YES-scope)
  ADVISORY: [N], NO: [N], DEPRECATED: [N]
  CONFIRMED-LOW: [N], CORROBORATED: [N], SOLO: [N]
  STANDING HIGH ICs: [N], DEFERRED: [N]
```

**Gate 7 — Readiness verdict** (same as R8 V-05)

**Gate 8 — Challenger: closing bracket** (same as R8 V-05)

**Gate 9 — Cross-role synthesis** (same as R8 V-05)

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a-G4h (all roles), G4.5,
                 G5, G5.5, G6, G7, G8, G9
  Halts fired:   0
  SCOPED roles:  0
  DEFERRED rows: 0
  SCOPE DISTRIBUTION ({{stage}}):
  | Group      | Count | Verdict contribution              |
  |------------|-------|-----------------------------------|
  | YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL |
  | ADVISORY   | [N]   | Noted; not blocking               |
  | NO         | [N]   | Excluded (scope floor)            |
  | DEPRECATED | [N]   | Informational only                |
  CONFIRMED (HIGH-effective): [N], CONFIRMED-LOW: [N], STANDING HIGH ICs: [N]
  Result:        Matrix complete. All contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Stage:         {{stage}}
  SCOPE DISTRIBUTION ({{stage}}):
  | Group      | Count | Verdict contribution              |
  |------------|-------|-----------------------------------|
  | YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL |
  | ADVISORY   | [N]   | Noted; not blocking               |
  | NO         | [N]   | Excluded (scope floor)            |
  | DEPRECATED | [N]   | Informational only                |
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

Same as R8 V-05 AMEND block, including `stage:{value}` and `rerun:challenger`.

---

## V-04

**Axis**: C-28 + C-29 -- SOLO disposition protocol + mid-run convergence snapshot
**Hypothesis**: V-01 makes non-converging findings first-class by requiring a Gate 9
SOLO FINDINGS table with mandatory disposition tags. V-02 makes the convergence
checkpoint load-bearing by adding tier counts at Gate 5.5 and an early-abort halt
when zero cross-role signals exist. V-04 combines both: a SOLO finding that triggers
the G5.5 early-abort path (all SOLO) must still be dispositioned in Gate 9 when the
run continues under `--amend waive:convergence`. The SOLO disposition requirement and
the convergence snapshot are complementary enforcement axes -- the snapshot tells you
whether convergence exists at all; the disposition contract tells you what to do with
everything that didn't converge. Without both, a SOLO-heavy run either aborts without
explanation (G5.5 blocks without waive) or proceeds to synthesis with non-converging
signals silently absorbed. With both, every SOLO finding has a mandatory exit path
(ESCALATE / DISMISS / ROLE-SPECIFIC) and the snapshot makes the SOLO-only condition
detectable before synthesis runs.

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

[Identical to V-01 / V-02 calibration contract]

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

Matrix sort: scope-grouped (YES -> ADVISORY -> NO/DEPRECATED), then severity DESC,
confidence DESC within group.
CONFIRMED treated as HIGH-effective in Gate 7 for YES-scope rows.
Invalid severity: HALT [G4c-{role}] BLOCKING.
Invalid confidence: HALT [G4f-{role}] BLOCKING.
Absent confidence: HALT [G4g-{role}] DEFERRED.

---

### PRE-EXECUTION: ARTIFACT MATURITY STAGE CONTRACT

[Identical to V-01/V-02/V-03]

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

| Tier          | Criteria                                                               | Readiness effect                           | Gate 9 obligation                              |
|---------------|------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------|
| CONFIRMED     | Same Surface, 2+ roles, ALL same Confidence tier, tier != LOW, YES-scope | HIGH-effective in Gate 7                  | Named in synthesis                             |
| CONFIRMED-LOW | Same Surface, 2+ roles, ALL Confidence=LOW, YES-scope                  | Flagged for Gate 9; NOT HIGH-effective     | Enumerated in LOW findings table               |
| CORROBORATED  | Same Surface, 2+ roles, Confidence tiers differ, YES-scope             | Convergence signal; no automatic promotion | Named in synthesis                             |
| SOLO          | Surface cited by exactly 1 role (any scope group)                     | Normal weight                              | MANDATORY disposition in SOLO FINDINGS table   |

SOLO disposition tags: ESCALATE / DISMISS:rationale / ROLE-SPECIFIC (one required per
SOLO finding at Gate 9).

Convergence register over YES-scope rows only.

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after all domain role reviews complete,
before Gate 6 and Gate 9.

Must emit: (1) tier counts as labeled fields; (2) surface table.

Early-abort: if CONFIRMED = 0 AND CORROBORATED = 0, emit HALT [G5.5] BLOCKING.
`--amend waive:convergence` allows Gate 9 to proceed with SOLO-only findings;
SOLO FINDINGS table (C-28 requirement) is mandatory under waive path.

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

[Identical to V-01/V-02]

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID       | Trigger condition                                                    | Tier     |
|---------------|----------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}  | BLOCKING |
| G1            | `.roles/` absent or unreadable                                 | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims                      | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding                          | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface                         | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract                       | BLOCKING |
| G4d-{role}    | Recommendation missing location reference                            | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated                           | SCOPED   |
| G4f-{role}    | Confidence `{value}` not in calibration contract                     | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row                            | DEFERRED |
| G4h-{role}    | STAGE-APPROPRIATE not in {YES, ADVISORY, NO, DEPRECATED}             | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)                 | BLOCKING |
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 waivable via `--amend waive:convergence`.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

[Identical to V-01/V-02 9-row skip-map]

---

### REVIEWER PRIORITY MANIFEST

[Identical structure to V-01/V-02/V-03]

---

### EXECUTION

**Gate 0.5 — Stage acknowledgment** (fires before Gate 1; identical to V-01)

**Gate 1 — Role registry load** (identical to V-01)

**Gate 2 — Calibration contract acknowledgment**

State: "Severity and confidence calibration contracts active. Severity: HIGH/MEDIUM/LOW.
Confidence: HIGH/MEDIUM/LOW. Stage: {{stage}}. Scope-grouped matrix, dual-axis sort.
CONFIRMED (same surface + matching confidence != LOW, 2+ YES-scope roles) = HIGH-effective.
Gate 5.5 convergence snapshot fires after all role reviews. Early-abort at G5.5 if
CONFIRMED=0 and CORROBORATED=0 (waivable).
SOLO findings require mandatory Gate 9 disposition (ESCALATE / DISMISS:rationale /
ROLE-SPECIFIC). STANDING IC at HIGH strength blocks. IC-CHALLENGED required per row."

**Gate 3 — Challenger: opening bracket and IC registration** (identical to V-01)

**Gate 4 — Domain reviewer loop** (G4a-G4h, 8-column schema; identical to V-01)

**Gate 4.5 — CHALLENGE RESPONSE MAP** (identical to V-01)

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted** (identical to V-01)

**Gate 5.5 — CONVERGENCE SNAPSHOT** (C-29 variant)

Emit tier counts first:

```
CONVERGENCE SNAPSHOT (YES-scope):
  CONFIRMED:     [N] surfaces
  CONFIRMED-LOW: [N] surfaces
  CORROBORATED:  [N] surfaces
  SOLO:          [N] surfaces (any scope)
```

If CONFIRMED = 0 AND CORROBORATED = 0:
```
HALT [G5.5]: Zero cross-role convergence.
  CONFIRMED: 0, CORROBORATED: 0.
-> /crew-check {{artifact}} --amend depth:deep
-> /crew-check {{artifact}} --amend add:{role}
-> /crew-check {{artifact}} --amend waive:convergence
  (BLOCKING unless waived -- if waived, Gate 9 SOLO FINDINGS table is mandatory)
```

Then emit convergence register surface table with IC Impact column.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  CONFIRMED (non-LOW, HIGH-effective): [N] surfaces
  YES-scope: HIGH [N] / MEDIUM [N] / LOW [N]
  ADVISORY: [N] / NO excluded: [N] / DEPRECATED: [N]
  Convergence: CONFIRMED-LOW [N], CORROBORATED [N], SOLO [N]
  Inertia: STANDING HIGH ICs: [N]
  DEFERRED: [N]
```

**Gate 7 — Readiness verdict** (identical to V-01; DEPRECATED = READY unconditionally)

**Gate 8 — Challenger: closing bracket** (identical to V-01)

**Gate 9 — Cross-role synthesis, SOLO disposition, and LOW enumeration**

2-4 sentences on CONFIRMED/CORROBORATED surfaces (or SOLO pattern if waived).

Mandatory Confidence=LOW enumeration:
```
CONFIDENCE=LOW FINDINGS:
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
```

Mandatory SOLO FINDINGS table (required whether or not G5.5 was waived):
```
SOLO FINDINGS (mandatory disposition):
| Role | Surface | Severity | Confidence | IC-CHALLENGED | Finding summary | Disposition                              |
|------|---------|----------|------------|---------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...           | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

If no SOLO findings: "No SOLO findings. All surfaces cited by 2+ YES-scope roles."
State CONFIRMED-LOW verdict impact if elevated. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a-G4h, G4.5, G5, G5.5 (snapshot), G6, G7, G8, G9
  Halts fired:   0
  G5.5 waived:   NO
  SCOPED roles:  0
  DEFERRED rows: 0
  CONFIRMED (HIGH-effective): [N], CONFIRMED-LOW: [N]
  CORROBORATED: [N], SOLO disposed: [N] (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])
  STANDING HIGH ICs: [N]
  YES-scope / ADVISORY / excluded: [N] / [N] / [N]
  Result:        Convergence snapshot passed. SOLO disposition complete. All contracts honored.
```

**Failed run:**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

Operations: `add:{role}`, `depth:deep`, `stage:{value}`, `waive:convergence`,
`rerun:{role}`, `rerun:challenger`, `rerun:G4a-{role}` through `rerun:G4h-{role}`,
`reload`, `halts`, `halts:{gate-id}`.

---

## V-05

**Axis**: C-28 + C-29 + C-30 -- Full three-axis integration
**Hypothesis**: V-01 adds mandatory SOLO disposition (C-28). V-02 adds counted
mid-run convergence snapshot with early-abort (C-29). V-03 adds stage-aware RUN
HEALTH with SCOPE DISTRIBUTION in both variants (C-30). V-05 combines all three
simultaneously on the R8 V-05 base. The integration test: do the three axes compose
without contract conflict? Each targets a different execution position -- Gate 9 (SOLO
disposition), Gate 5.5 (snapshot counts + abort), RUN HEALTH output (stage + scope
table). No two axes share a gate or enforcement path. C-30 depends on C-26 (Stage
field is only meaningful when G0.5 validated it). C-28 depends on C-25 (SOLO tier
requires convergence contract). C-29 depends on C-25 (snapshot counts tiers defined
in the convergence contract). All three dependencies are satisfied by R8 V-05's
pre-committed contracts. The claim: C-28, C-29, and C-30 are structurally independent
-- they occupy different positions in the execution sequence, enforce different fields,
and share no gate IDs -- and therefore compose additively with zero contract conflict.

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

Matrix sort: scope-grouped (YES -> ADVISORY -> NO/DEPRECATED), then severity DESC,
confidence DESC within group.
CONFIRMED (same surface + matching confidence != LOW, 2+ YES-scope roles) = HIGH-effective.
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

DEPRECATED: all rows STAGE-APPROPRIATE=DEPRECATED. Readiness always READY (informational).

---

### PRE-EXECUTION: FINDING CONVERGENCE CONTRACT

| Tier          | Criteria                                                               | Readiness effect                           | Gate 9 obligation                              |
|---------------|------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------|
| CONFIRMED     | Same Surface, 2+ roles, ALL same Confidence tier, tier != LOW, YES-scope | HIGH-effective in Gate 7                  | Named in synthesis                             |
| CONFIRMED-LOW | Same Surface, 2+ roles, ALL Confidence=LOW, YES-scope                  | Flagged for Gate 9; NOT HIGH-effective     | LOW findings table                             |
| CORROBORATED  | Same Surface, 2+ roles, Confidence tiers differ, YES-scope             | Convergence signal; no automatic promotion | Named in synthesis                             |
| SOLO          | Surface cited by exactly 1 role (any scope group)                     | Normal weight                              | MANDATORY disposition in SOLO FINDINGS table   |

SOLO disposition tags (one required per SOLO finding at Gate 9):
ESCALATE / DISMISS:rationale / ROLE-SPECIFIC

Convergence register over YES-scope rows only.

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after all domain roles complete,
before Gate 6 and Gate 9.

Must emit: (1) tier counts as labeled fields; (2) convergence register surface table.

Early-abort: CONFIRMED = 0 AND CORROBORATED = 0 -> HALT [G5.5] BLOCKING.
`--amend waive:convergence` allows Gate 9 with SOLO-only findings.
Under waive path, SOLO FINDINGS table (C-28 requirement) is mandatory.

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

| IC-ID | Inertia Claim                               | Strength |
|-------|---------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                 | [H/M/L]  |

IC-CHALLENGED: every finding row carries IC-CHALLENGED = IC-[N] or `none`.
Absent: HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT

RUN HEALTH emits Stage field (declared value) and SCOPE DISTRIBUTION table in BOTH
clean and failed variants.

SCOPE DISTRIBUTION format:
```
SCOPE DISTRIBUTION ({{stage}}):
| Group      | Count | Verdict contribution                |
|------------|-------|-------------------------------------|
| YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
| ADVISORY   | [N]   | Noted; not blocking                 |
| NO         | [N]   | Excluded (scope floor)              |
| DEPRECATED | [N]   | Informational only                  |
```

Stage field carries declared value. Both variants include Stage + SCOPE DISTRIBUTION.

---

### PRE-EXECUTION: HALT REGISTRY

G0.5 before all gates. G5.5 after G5, before Gate 6.

| Halt ID       | Trigger condition                                                    | Tier     |
|---------------|----------------------------------------------------------------------|----------|
| G0.5          | `{{stage}}` absent or not in {DRAFT, REVIEW, APPROVED, DEPRECATED}  | BLOCKING |
| G1            | `.roles/` absent or unreadable                                 | BLOCKING |
| G3a           | Challenger declares fewer than 2 inertia claims                      | BLOCKING |
| G4a-{role}    | Lens anchor not stated before first finding                          | BLOCKING |
| G4b-{role}    | Finding not tied to a named artifact surface                         | BLOCKING |
| G4c-{role}    | Severity `{value}` not in calibration contract                       | BLOCKING |
| G4d-{role}    | Recommendation missing location reference                            | BLOCKING |
| G4e-{role}    | IC-CHALLENGED column absent or unpopulated                           | SCOPED   |
| G4f-{role}    | Confidence `{value}` not in calibration contract                     | BLOCKING |
| G4g-{role}    | Confidence column absent from finding row                            | DEFERRED |
| G4h-{role}    | STAGE-APPROPRIATE not in {YES, ADVISORY, NO, DEPRECATED}             | DEFERRED |
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)                 | BLOCKING |
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 waivable. G5.5 does not fire for DEPRECATED artifacts.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

| Re-entry command            | Resumes at | Skips         | Safe-skip prerequisite                                       |
|-----------------------------|------------|---------------|--------------------------------------------------------------|
| `--amend rerun:{role}`      | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4a-{role}`  | G4a        | (nothing)     | Full role restart                                            |
| `--amend rerun:G4b-{role}`  | G4b        | G4a           | Lens anchor verified                                         |
| `--amend rerun:G4c-{role}`  | G4c        | G4a, G4b      | Lens anchor + named surface verified                         |
| `--amend rerun:G4d-{role}`  | G4d        | G4a-G4c       | Lens anchor + surface + severity verified                    |
| `--amend rerun:G4e-{role}`  | G4e        | G4a-G4d       | Lens anchor + surface + severity + location verified         |
| `--amend rerun:G4f-{role}`  | G4f        | G4a-G4e       | All prior + IC-CHALLENGED verified                           |
| `--amend rerun:G4g-{role}`  | G4g        | G4a-G4f       | All prior + confidence label verified                        |
| `--amend rerun:G4h-{role}`  | G4h        | G4a-G4g       | All prior verified                                           |

---

### REVIEWER PRIORITY MANIFEST

Read `.roles/`. If absent: emit `HALT [G1]`.

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

```
HALT [G0.5]: Stage absent or not recognized.
-> To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING)
```

Otherwise: "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings STAGE-APPROPRIATE=DEPRECATED. Readiness will be READY."

**Gate 1 — Role registry load**

```
HALT [G1]: .roles/ absent or unreadable.
-> To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 — Calibration contract acknowledgment**

State: "All pre-execution contracts active: severity/confidence calibration, artifact
maturity stage, finding convergence, convergence snapshot, inertia claim registry,
RUN HEALTH scope distribution.
Stage: {{stage}}. Scope-grouped matrix, dual-axis sort.
CONFIRMED (same surface + matching confidence != LOW, 2+ YES-scope roles) = HIGH-effective.
Gate 5.5 snapshot fires after all role reviews; early-abort if CONFIRMED=0, CORROBORATED=0.
SOLO findings require mandatory Gate 9 disposition (ESCALATE / DISMISS:rationale /
ROLE-SPECIFIC).
RUN HEALTH will emit Stage and SCOPE DISTRIBUTION in both clean and failed variants.
STANDING IC at HIGH strength blocks. IC-CHALLENGED required per row."

**Gate 3 — Challenger: opening bracket and IC registration**

Populate INERTIA CLAIM REGISTRY with >= 2 numbered ICs (IC-01, IC-02...). Name specific
existing capability or argument. Assign Strength (H/M/L). Note stage relevance.

On fewer than 2:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
-> To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING)
```

Emit "Inertia registry locked. Stage-scoped domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
Challenger)

*G4a -- Lens anchor*:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
-> /crew-check {{artifact}} --amend rerun:G4a-{role} (BLOCKING)
```

*G4b -- Surface finding*: Format:
`| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`
For DEPRECATED: STAGE-APPROPRIATE=DEPRECATED on all rows.
```
HALT [G4b-{role}]: Finding lacks named surface. (skip-map: G4a)
```

*G4c -- Severity*:
```
HALT [G4c-{role}]: Severity '{value}' not in contract. (skip-map: G4a, G4b)
```

*G4d -- Recommendation*:
```
HALT [G4d-{role}]: Recommendation missing location. (skip-map: G4a-G4c)
```

*G4e -- IC-CHALLENGED*:
```
HALT [G4e-{role}]: IC-CHALLENGED absent. Role excluded. (SCOPED)
-> /crew-check {{artifact}} --amend rerun:G4e-{role}
```

*G4f -- Confidence*:
```
HALT [G4f-{role}]: Confidence '{value}' not in contract. (skip-map: G4a-G4e)
```

*G4g -- Confidence presence*:
```
HALT [G4g-{role}]: Confidence absent -- [DEFERRED]. Readiness forced CONDITIONAL.
  (skip-map: G4a-G4f; DEFERRED)
```

*G4h -- STAGE-APPROPRIATE*:
```
HALT [G4h-{role}]: STAGE-APPROPRIATE absent or invalid -- [DEFERRED]. (skip-map: G4a-G4g)
```

**Gate 4.5 — CHALLENGE RESPONSE MAP**

```
| IC-ID | Strength | Challenging Findings (Role -- Sev/Conf, STAGE-APPROPRIATE) | IC Status             |
|-------|----------|-------------------------------------------------------------|-----------------------|
| IC-01 | H        | [pm HIGH/HIGH, YES], [arch MEDIUM/HIGH, YES]                | OVERCOME-CONFIRMED    |
| IC-02 | M        | [pm LOW/LOW, YES]                                           | CONTESTED             |
| IC-03 | H        | (none in YES scope)                                         | STANDING              |
```

IC Status: OVERCOME (>= 1 HIGH YES-scope), OVERCOME-CONFIRMED (CONFIRMED multi-role),
CONTESTED (challenged, no HIGH), STANDING (no YES-scope challenge).
Emit before Gate 5.

**Gate 5 — Matrix assembly: scope-grouped, dual-axis sorted**

Group order: YES -> ADVISORY -> NO -> DEPRECATED -> EXCLUDED ROLES.
Sort within each group: severity DESC, confidence DESC.
Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

Non-DEPRECATED zero YES-scope:
```
HALT [G5]: Zero stage-appropriate findings.
-> /crew-check {{artifact}} --amend depth:deep
   /crew-check {{artifact}} --amend stage:[correct]
```

**Gate 5.5 — CONVERGENCE SNAPSHOT** (C-29: counts + early-abort)

Emit counts first:
```
CONVERGENCE SNAPSHOT (YES-scope):
  CONFIRMED:     [N] surfaces
  CONFIRMED-LOW: [N] surfaces
  CORROBORATED:  [N] surfaces
  SOLO:          [N] surfaces (any scope)
```

Early-abort if CONFIRMED = 0 AND CORROBORATED = 0:
```
HALT [G5.5]: Zero cross-role convergence.
  CONFIRMED: 0, CORROBORATED: 0.
  Gate 9 cannot satisfy >= 1 cross-role convergence requirement.
-> /crew-check {{artifact}} --amend depth:deep
-> /crew-check {{artifact}} --amend add:{role}
-> /crew-check {{artifact}} --amend waive:convergence
  (BLOCKING -- waive path requires SOLO FINDINGS disposition at Gate 9)
```

Then emit convergence register surface table (YES-scope only):
```
CONVERGENCE REGISTER (YES-scope):
| Surface   | Roles (Sev/Conf)                  | Tier          | IC Impact                  | Readiness Effect              |
|-----------|-----------------------------------|---------------|----------------------------|-------------------------------|
| [surface] | [pm HIGH/HIGH],[arch HIGH/HIGH]   | CONFIRMED     | IC-01 -> OVERCOME-CONFIRMED| HIGH-effective                |
| [surface] | [pm MED/LOW],[arch MED/LOW]       | CONFIRMED-LOW | none                       | Flagged for Gate 9            |
| [surface] | [pm HIGH/HIGH],[arch HIGH/MED]    | CORROBORATED  | IC-02 -> CONTESTED         | Synthesis signal only         |
| [surface] | [pm MEDIUM/HIGH]                  | SOLO          | none                       | Disposition required at Gate 9|
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY (stage: {{stage}}):
  In-scope (STAGE-APPROPRIATE=YES):
    CONFIRMED (non-LOW, HIGH-effective): [N] surfaces -- [names]
    HIGH:    [N] findings
    MEDIUM:  [N] findings ([N] promoted via CONFIRMED)
    LOW:     [N] findings
  Advisory (STAGE-APPROPRIATE=ADVISORY): [N]
  Excluded (STAGE-APPROPRIATE=NO):       [N]
  Deprecated:  [N]
  Convergence snapshot: CONFIRMED [N], CONFIRMED-LOW [N], CORROBORATED [N], SOLO [N]
  Inertia: STANDING HIGH-strength ICs: [N]
  DEFERRED rows: [N]
  G5.5 waived: YES | NO
```

**Gate 7 — Readiness verdict**

DEPRECATED: `READINESS: READY (DEPRECATED -- informational only)`

Non-DEPRECATED, YES-scope rows only:
1. Any CONFIRMED (non-LOW) surface -> HIGH-effective -> BLOCKED.
2. Any YES-scope HIGH finding -> BLOCKED.
3. Any STANDING IC at HIGH strength -> BLOCKED.
4. Any YES-scope MEDIUM (non-CONFIRMED or CONFIRMED-LOW), no blockers -> CONDITIONAL.
5. Any DEFERRED row -> minimum CONDITIONAL.
6. Otherwise -> READY.

Emit: `READINESS: READY | CONDITIONAL | BLOCKED`
Append attributions: `(confirmed evidence: [N])`, `(inertia: IC-[N] STANDING HIGH)`,
`(scope: {{stage}} -- YES [N]; ADVISORY [N]; excluded [N])`

**Gate 8 — Challenger: closing bracket and CHALLENGE RESPONSE MAP review**

Review each IC:
- OVERCOME/OVERCOME-CONFIRMED: acknowledge; name evidence.
- CONTESTED: specify what additional evidence would make it OVERCOME.
- STANDING: explain absence of YES-scope challenge (scope gap, genuine absence, or advisory-only).

Note CONFIRMED convergence vs STANDING ICs. Note ADVISORY latent risk.
Revise readiness only if YES-scope or STANDING IC analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 — Cross-role synthesis, SOLO disposition, and LOW enumeration** (C-28)

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface (or SOLO pattern if waived).

Mandatory Confidence=LOW enumeration:
```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
|------|---------|----------|---------------|-------------------|-----------------|
| ...  | ...     | ...      | ...           | ...               | ...             |
```

Mandatory SOLO FINDINGS table (required on every run, including waive path):
```
SOLO FINDINGS (mandatory disposition):
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition                              |
|------|---------|----------|------------|---------------|-------------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...           | ...               | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

Disposition semantics:
- ESCALATE: warrants `--amend add:{role}` or `--amend depth:deep` before final verdict.
- DISMISS:rationale: role-specific noise; rationale required inline.
- ROLE-SPECIFIC: valid only from this lens; no cross-role action needed.

If no SOLO findings: "No SOLO findings. All surfaces cited by 2+ YES-scope roles."

State whether CONFIRMED-LOW would change IC status or readiness if elevated.
Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:** (C-30: Stage field + SCOPE DISTRIBUTION table)
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3 (IC registry), G4a-G4h (all roles), G4.5,
                 G5, G5.5 (snapshot), G6, G7, G8, G9
  Halts fired:   0
  G5.5 waived:   NO
  SCOPED roles:  0
  DEFERRED rows: 0
  SCOPE DISTRIBUTION ({{stage}}):
  | Group      | Count | Verdict contribution                |
  |------------|-------|-------------------------------------|
  | YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
  | ADVISORY   | [N]   | Noted; not blocking                 |
  | NO         | [N]   | Excluded (scope floor)              |
  | DEPRECATED | [N]   | Informational only                  |
  CONFIRMED (HIGH-effective): [N], CONFIRMED-LOW: [N], CORROBORATED: [N]
  SOLO disposed: [N] (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])
  STANDING HIGH ICs: [N]
  Result:        Matrix complete. All five contracts honored.
```

**Failed run:** (C-30: Stage + SCOPE DISTRIBUTION in failed variant too)
```
RUN HEALTH: [N] HALT(S) FIRED
  Stage:         {{stage}}
  SCOPE DISTRIBUTION ({{stage}}):
  | Group      | Count | Verdict contribution                |
  |------------|-------|-------------------------------------|
  | YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
  | ADVISORY   | [N]   | Noted; not blocking                 |
  | NO         | [N]   | Excluded (scope floor)              |
  | DEPRECATED | [N]   | Informational only                  |
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` -- add a specific reviewer
- `depth:deep` -- re-run with all roles
- `stage:{value}` -- change artifact maturity stage; restarts from Gate 0.5
- `waive:convergence` -- waive G5.5 early-abort; Gate 9 proceeds with SOLO-only note
  (SOLO FINDINGS table mandatory under waive path)
- `rerun:{role}` -- full role restart from G4a
- `rerun:challenger` -- restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4h-{role}` -- re-enter at named sub-gate
  (skip-map applies; state skipped sub-gates at re-entry)
- `reload` -- re-load `.roles/` and restart
- `halts` -- list all gates that fired in this run
- `halts:{gate-id}` -- show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT -- [N] gate(s) fired this run:
| Gate ID        | Trigger description                    | Tier     | Re-entry command                                          |
|----------------|----------------------------------------|----------|-----------------------------------------------------------|
| [G0.5]         | Stage 'WIP' not in valid set           | BLOCKING | /crew-check {{artifact}} --amend stage:DRAFT              |
| [G4e-pm]       | IC-CHALLENGED column absent            | SCOPED   | /crew-check {{artifact}} --amend rerun:G4e-pm             |
| [G5.5]         | CONFIRMED=0, CORROBORATED=0            | BLOCKING | /crew-check {{artifact}} --amend depth:deep               |
| [G4g-architect]| Confidence column absent               | DEFERRED | /crew-check {{artifact}} --amend rerun:G4g-architect      |
```
Each entry is paste-ready. Re-entry encodes minimum-restart routing per SUB-GATE SKIP-MAP.
