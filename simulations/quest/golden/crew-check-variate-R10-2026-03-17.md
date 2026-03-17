---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 10
rubric: crew-check-rubric-v9-2026-03-17.md
---

# crew-check — Variate R10

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Base for all variations: R9 V-05 (full C-28 + C-29 + C-30 integration under v8 rubric).
R10 adds four axes extracted from the v9 rubric excellence signals:

New criteria targeted in R10:
- C-31: waive:convergence mutual enforcement contract (extends C-28 / C-29)
  CONVERGENCE SNAPSHOT CONTRACT explicitly names mandatory SOLO FINDINGS disposition
  as the consequence of waive:convergence; waive path note repeats the enforcement
  seam; a run under waive:convergence with zero SOLO findings emits a declared exit,
  not a silent skip.
- C-32: SOLO FINDINGS extended schema (IC-CHALLENGED + STAGE-APPROPRIATE) (extends C-28)
  SOLO FINDINGS table extended to 8-column schema adding IC-CHALLENGED and
  STAGE-APPROPRIATE; each disposition decision auditable against inertia impact and
  scope group; schema declared in PRE-EXECUTION; empty case declared explicitly.
- C-33: Failed RUN HEALTH as standalone diagnostic artifact (extends C-21 / C-30)
  Failed RUN HEALTH places Stage field and complete SCOPE DISTRIBUTION table (all
  four rows with resolved counts) before the recovery block; readable as standalone
  diagnostic without referencing clean cert or run transcript; NO and DEPRECATED
  are distinct rows.
- C-34: Gate 2 unified contract acknowledgment (extends C-13)
  Gate 2 emits a single numbered enumeration of all active pre-execution contracts
  by name; creating an auditable start-of-run checkpoint detectable by comparison
  with PRE-EXECUTION section headers.

Dependency chain:
- C-31 extends C-28 / C-29: mutual enforcement requires both SOLO tier (C-28) and
  convergence snapshot gate (C-29) in place; C-31 is the declared relationship between them.
- C-32 extends C-28: extended schema requires SOLO tier and disposition protocol in place.
- C-33 extends C-21 / C-30: standalone diagnostic structure requires failed variant (C-21)
  and Stage + SCOPE DISTRIBUTION fields (C-30) in place.
- C-34 extends C-13 (prompt inputs as template variables): unified acknowledgment
  requires named pre-execution contracts to enumerate.

Axes selected for R10:
- V-01: C-31 only -- waive:convergence mutual enforcement (CONVERGENCE SNAPSHOT CONTRACT
  updated to declare mutual enforcement seam; Gate 5.5 waive path note strengthened;
  Gate 9 declared empty exit under waive path)
- V-02: C-32 only -- SOLO FINDINGS extended schema (new PRE-EXECUTION SOLO FINDINGS
  SCHEMA CONTRACT; 8-column table at Gate 9; declared empty exit)
- V-03: C-33 only -- failed RUN HEALTH as standalone diagnostic (Stage + SCOPE DISTRIBUTION
  repositioned before recovery block; all four rows distinct; self-contained)
- V-04: C-31 + C-32 -- mutual enforcement + extended schema combined
- V-05: C-31 + C-32 + C-33 + C-34 -- full four-axis integration

---

## V-01

**Axis**: C-31 -- waive:convergence mutual enforcement contract
**Hypothesis**: R9 V-05 CONVERGENCE SNAPSHOT CONTRACT states "Under waive path, SOLO
FINDINGS table (C-28 requirement) is mandatory" -- a correct assertion that exists in
one location. But the FINDING CONVERGENCE CONTRACT (which defines the SOLO tier and
its Gate 9 obligation) does not name waive:convergence as the activating condition, and
the CONVERGENCE SNAPSHOT CONTRACT does not name SOLO FINDINGS disposition as the
explicitly declared substitute for the convergence requirement it is waiving. A reviewer
inspecting the two contracts can observe that both exist, but cannot verify from the
contract text alone that waive:convergence and SOLO disposition are linked by design
rather than by convention. V-01 R10 restructures the CONVERGENCE SNAPSHOT CONTRACT
to add a "MUTUAL ENFORCEMENT DECLARATION" block that names mandatory SOLO FINDINGS
disposition (FINDING CONVERGENCE CONTRACT, SOLO tier Gate 9 obligation) as the explicit
enforcement substitute for waive:convergence, repeats the link in the Gate 5.5 waive
path note, and adds a declared "No SOLO findings" exit requirement for the empty case
under waive path. The claim: when the enforcement seam between waive:convergence and
SOLO disposition is declared in the contract text and visible at both the contract layer
and the execution layer, a reviewer can verify by inspection that no run using
waive:convergence exits without either a populated SOLO FINDINGS table or a declared
empty exit.

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

**MUTUAL ENFORCEMENT DECLARATION (C-31):**
`--amend waive:convergence` does not waive accountability. It substitutes Gate 5.5
convergence enforcement with mandatory Gate 9 SOLO FINDINGS disposition (FINDING
CONVERGENCE CONTRACT, SOLO tier Gate 9 obligation). The enforcement chain under
waive:convergence is: Gate 5.5 convergence requirement -> waived; SOLO FINDINGS
disposition requirement (Gate 9) -> activated as mandatory substitute. A run proceeding
under waive:convergence MUST emit the SOLO FINDINGS table at Gate 9. If no SOLO findings
exist under waive path, a declared exit is required: "No SOLO findings under
waive:convergence. Convergence substitute satisfied (declared empty exit)." Silent
skip is a contract violation.

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
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)                 | BLOCKING |
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 waivable via `--amend waive:convergence`. See MUTUAL ENFORCEMENT DECLARATION.
G5.5 does not fire for DEPRECATED artifacts.

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

Read `.craft/roles/`. If absent: emit `HALT [G1]`.

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 -- Stage acknowledgment** (fires before Gate 1)

```
HALT [G0.5]: Stage absent or not recognized.
-> To continue: /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED]
  (BLOCKING)
```

Otherwise: "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings STAGE-APPROPRIATE=DEPRECATED. Readiness will be READY."

**Gate 1 -- Role registry load**

```
HALT [G1]: .craft/roles/ absent or unreadable.
-> To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING)
```

**Gate 2 -- Calibration contract acknowledgment**

State: "All pre-execution contracts active: severity/confidence calibration, artifact
maturity stage, finding convergence, convergence snapshot (with mutual enforcement
declaration), inertia claim registry, RUN HEALTH scope distribution.
Stage: {{stage}}. Scope-grouped matrix, dual-axis sort.
CONFIRMED (same surface + matching confidence != LOW, 2+ YES-scope roles) = HIGH-effective.
Gate 5.5 snapshot fires after all role reviews; early-abort if CONFIRMED=0, CORROBORATED=0.
waive:convergence activates mandatory SOLO FINDINGS disposition as enforcement substitute
per MUTUAL ENFORCEMENT DECLARATION; declared empty exit required if no SOLO findings.
SOLO findings require mandatory Gate 9 disposition (ESCALATE / DISMISS:rationale /
ROLE-SPECIFIC).
RUN HEALTH will emit Stage and SCOPE DISTRIBUTION in both clean and failed variants.
STANDING IC at HIGH strength blocks. IC-CHALLENGED required per row."

**Gate 3 -- Challenger: opening bracket and IC registration**

Populate INERTIA CLAIM REGISTRY with >= 2 numbered ICs (IC-01, IC-02...). Name specific
existing capability or argument. Assign Strength (H/M/L). Note stage relevance.

On fewer than 2:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims.
-> To continue: /crew-check {{artifact}} --amend rerun:challenger
  (BLOCKING)
```

Emit "Inertia registry locked. Stage-scoped domain review proceeds."

**Gate 4 -- Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing
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

**Gate 4.5 -- CHALLENGE RESPONSE MAP**

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

**Gate 5 -- Matrix assembly: scope-grouped, dual-axis sorted**

Group order: YES -> ADVISORY -> NO -> DEPRECATED -> EXCLUDED ROLES.
Sort within each group: severity DESC, confidence DESC.
Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

Non-DEPRECATED zero YES-scope:
```
HALT [G5]: Zero stage-appropriate findings.
-> /crew-check {{artifact}} --amend depth:deep
   /crew-check {{artifact}} --amend stage:[correct]
```

**Gate 5.5 -- CONVERGENCE SNAPSHOT** (C-29: counts + early-abort)

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
  (BLOCKING -- waive:convergence activates FINDING CONVERGENCE CONTRACT SOLO tier
   disposition as mandatory enforcement substitute per MUTUAL ENFORCEMENT DECLARATION;
   SOLO FINDINGS table required at Gate 9; declared empty exit required if no SOLO
   findings; convergence is substituted, not waived)
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

**Gate 6 -- Priority summary**

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

**Gate 7 -- Readiness verdict**

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

**Gate 8 -- Challenger: closing bracket and CHALLENGE RESPONSE MAP review**

Review each IC:
- OVERCOME/OVERCOME-CONFIRMED: acknowledge; name evidence.
- CONTESTED: specify what additional evidence would make it OVERCOME.
- STANDING: explain absence of YES-scope challenge.

Note CONFIRMED convergence vs STANDING ICs. Note ADVISORY latent risk.
Revise readiness only if YES-scope or STANDING IC analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 -- Cross-role synthesis, SOLO disposition, and LOW enumeration**

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
| Role | Surface | Severity | Confidence | Finding summary | Disposition                              |
|------|---------|----------|------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

Disposition semantics:
- ESCALATE: warrants `--amend add:{role}` or `--amend depth:deep` before final verdict.
- DISMISS:rationale: role-specific noise; rationale required inline.
- ROLE-SPECIFIC: valid only from this lens; no cross-role action needed.

Empty case (C-31 mutual enforcement declared exit):
- If no SOLO findings and waive:convergence NOT invoked: emit "No SOLO findings.
  All surfaces cited by 2+ roles."
- If no SOLO findings and waive:convergence WAS invoked: emit "No SOLO findings
  under waive:convergence. Convergence substitute satisfied (declared empty exit)."
  Do not silently skip.

State whether CONFIRMED-LOW would change IC status or readiness if elevated.
Reference role names. No new findings.

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
  Result:        Matrix complete. All contracts honored.
```

**Failed run:**
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
- `waive:convergence` -- waive G5.5 early-abort; activates mandatory SOLO FINDINGS
  disposition as enforcement substitute per MUTUAL ENFORCEMENT DECLARATION; declared
  empty exit required if no SOLO findings
- `rerun:{role}` -- full role restart from G4a
- `rerun:challenger` -- restart Gate 3 (re-register inertia claims)
- `rerun:G4a-{role}` through `rerun:G4h-{role}` -- re-enter at named sub-gate
- `reload` -- re-load `.craft/roles/` and restart
- `halts` -- list all gates that fired in this run
- `halts:{gate-id}` -- show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT -- [N] gate(s) fired this run:
| Gate ID        | Trigger description                    | Tier     | Re-entry command                                          |
|----------------|----------------------------------------|----------|-----------------------------------------------------------|
| [G5.5]         | CONFIRMED=0, CORROBORATED=0            | BLOCKING | /crew-check {{artifact}} --amend waive:convergence        |
```
Each entry is paste-ready. Re-entry encodes minimum-restart routing per SUB-GATE SKIP-MAP.

---

## V-02

**Axis**: C-32 -- SOLO FINDINGS extended schema (IC-CHALLENGED + STAGE-APPROPRIATE)
**Hypothesis**: R9 V-05 SOLO FINDINGS table carries six columns: Role, Surface, Severity,
Confidence, Finding summary, Disposition. The Disposition column records the decision
(ESCALATE / DISMISS:rationale / ROLE-SPECIFIC), but the two evidence columns that make
that decision auditable are absent. A DISMISS disposition on a finding that challenges
IC-01 (HIGH strength) is indistinguishable in the table from one that challenges nothing
-- without IC-CHALLENGED, a reviewer cannot verify whether a dismissed SOLO finding was
IC-neutral. Similarly, an ESCALATE disposition on a NO-scoped finding looks urgent
without STAGE-APPROPRIATE revealing it was excluded from the verdict. V-02 R10 extends
the SOLO FINDINGS table to an 8-column schema by adding IC-CHALLENGED and
STAGE-APPROPRIATE, declares this schema in a new PRE-EXECUTION SOLO FINDINGS SCHEMA
CONTRACT, and adds a declared empty-case exit path. The claim: when IC-CHALLENGED and
STAGE-APPROPRIATE are present in every SOLO finding row, each disposition decision is
auditable against both inertia impact (was the finding IC-neutral, contested, or
directly challenging a standing claim?) and scope group (was the finding in-scope,
advisory, or below the stage floor?). A reviewer can confirm a DISMISS is defensible
or flag an ESCALATE as scope-mismatched from the table alone, without cross-referencing
finding rows.

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
Under waive path, SOLO FINDINGS table is mandatory.

---

### PRE-EXECUTION: SOLO FINDINGS SCHEMA CONTRACT (C-32)

The SOLO FINDINGS table uses an 8-column schema declared here. This schema is required
on every run; the table must be emitted at Gate 9 regardless of SOLO count.

**8-column schema:**
```
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition |
```

Column definitions:
- `IC-CHALLENGED`: carry forward from finding row IC-CHALLENGED column (IC-[N] or `none`).
  Surfaces which IC-IDs the SOLO finding challenges, making disposition auditable against
  inertia impact.
- `STAGE-APPROPRIATE`: carry forward from finding row (YES / ADVISORY / NO / DEPRECATED).
  Surfaces scope group, making an ESCALATE on a NO-scoped finding identifiable by
  inspection.
- `Disposition`: ESCALATE | DISMISS:rationale | ROLE-SPECIFIC (one required per row).

**Empty-case declared exit:**
If zero SOLO findings exist, emit:
"No SOLO findings. All surfaces cited by 2+ roles. SOLO FINDINGS table: empty (declared)."
Do not omit the table section. The declared exit is required; silent skip is a contract
violation.

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

Read `.craft/roles/`. If absent: emit `HALT [G1]`.

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 -- Stage acknowledgment**

```
HALT [G0.5]: Stage absent or not recognized.
-> /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED] (BLOCKING)
```

Otherwise: "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings STAGE-APPROPRIATE=DEPRECATED. Readiness will be READY."

**Gate 1 -- Role registry load**

```
HALT [G1]: .craft/roles/ absent or unreadable.
-> /crew-check {{artifact}} --amend reload (BLOCKING)
```

**Gate 2 -- Calibration contract acknowledgment**

State: "All pre-execution contracts active: severity/confidence calibration, artifact
maturity stage, finding convergence, convergence snapshot, inertia claim registry,
SOLO FINDINGS schema (8-column: Role/Surface/Severity/Confidence/IC-CHALLENGED/
STAGE-APPROPRIATE/Finding summary/Disposition), RUN HEALTH scope distribution.
Stage: {{stage}}. Scope-grouped matrix, dual-axis sort.
CONFIRMED = HIGH-effective. Gate 5.5 snapshot fires after all role reviews.
SOLO FINDINGS table uses 8-column schema per PRE-EXECUTION; IC-CHALLENGED and
STAGE-APPROPRIATE required per row; declared empty exit required if no SOLO findings.
STANDING IC at HIGH strength blocks. IC-CHALLENGED required per finding row."

**Gate 3 -- Challenger: opening bracket and IC registration**

Populate INERTIA CLAIM REGISTRY >= 2 ICs. Assign Strength (H/M/L). Note stage relevance.

On fewer than 2:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims. (BLOCKING)
-> /crew-check {{artifact}} --amend rerun:challenger
```

Emit "Inertia registry locked. Stage-scoped domain review proceeds."

**Gate 4 -- Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order)

*G4a* through *G4h* -- same sub-gate protocol as V-01.

**Gate 4.5 -- CHALLENGE RESPONSE MAP** -- same as V-01.

**Gate 5 -- Matrix assembly** -- same as V-01.

**Gate 5.5 -- CONVERGENCE SNAPSHOT** -- same as V-01 (counts + early-abort).

**Gate 6 -- Priority summary** -- same as V-01.

**Gate 7 -- Readiness verdict** -- same as V-01.

**Gate 8 -- Challenger: closing bracket** -- same as V-01.

**Gate 9 -- Cross-role synthesis, SOLO disposition (8-column schema), and LOW enumeration**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface.

Mandatory Confidence=LOW enumeration -- same as V-01.

Mandatory SOLO FINDINGS table (8-column schema per SOLO FINDINGS SCHEMA CONTRACT):
```
SOLO FINDINGS (mandatory disposition -- 8-column schema):
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition                              |
|------|---------|----------|------------|---------------|-------------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...           | ...               | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

Column population rules:
- IC-CHALLENGED: copy from finding row; enables auditing disposition against inertia impact.
- STAGE-APPROPRIATE: copy from finding row; enables auditing disposition against scope group.
- Disposition: one tag required per row with rationale for DISMISS.

Empty case:
If zero SOLO findings: emit "No SOLO findings. All surfaces cited by 2+ roles.
SOLO FINDINGS table: empty (declared)."

State whether CONFIRMED-LOW would change IC status if elevated. Reference role names.
No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a-G4h (all roles), G4.5, G5, G5.5, G6, G7, G8, G9
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
  CONFIRMED: [N], CONFIRMED-LOW: [N], CORROBORATED: [N]
  SOLO disposed: [N] (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])
  SOLO schema: 8-column (IC-CHALLENGED + STAGE-APPROPRIATE present on all rows)
  STANDING HIGH ICs: [N]
  Result:        Matrix complete. All contracts honored.
```

**Failed run:**
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

Same operations as V-01. waive:convergence note: "SOLO FINDINGS table mandatory under
waive path; 8-column schema (IC-CHALLENGED + STAGE-APPROPRIATE) required; declared
empty exit required if no SOLO findings."

---

## V-03

**Axis**: C-33 -- Failed RUN HEALTH as standalone diagnostic artifact
**Hypothesis**: R9 V-05 failed RUN HEALTH includes Stage field and SCOPE DISTRIBUTION
table, satisfying C-30. However, Stage and SCOPE DISTRIBUTION appear inside the recovery
block structure -- Stage precedes recovery, but SCOPE DISTRIBUTION is embedded as part
of the same block, meaning a reviewer reading top-to-bottom encounters recovery items
before they have the full scope picture. To answer "how did findings distribute?" a
reviewer must either pre-scan the block or read through recovery instructions to find
SCOPE DISTRIBUTION. V-03 R10 restructures the failed RUN HEALTH variant: Stage field
and SCOPE DISTRIBUTION table (all four rows -- YES / ADVISORY / NO / DEPRECATED --
with resolved counts and NO and DEPRECATED as distinct rows) appear as a complete
diagnostic header before any recovery content. The recovery block begins only after
SCOPE DISTRIBUTION closes. This restructuring is declared in the RUN HEALTH SCOPE
DISTRIBUTION CONTRACT, which adds "In the failed variant, Stage + SCOPE DISTRIBUTION
precede recovery items. SCOPE DISTRIBUTION includes all four rows as distinct entries."
The claim: when the failed cert opens with Stage + SCOPE DISTRIBUTION, a reviewer
can determine what stage was declared and how findings distributed across YES/ADVISORY/
NO/DEPRECATED before reading a single recovery instruction -- making the failed cert a
self-contained diagnostic that does not require the clean cert or run transcript for
scope interpretation.

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

SOLO disposition tags: ESCALATE / DISMISS:rationale / ROLE-SPECIFIC

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after all domain roles complete,
before Gate 6 and Gate 9.

Must emit: (1) tier counts as labeled fields; (2) convergence register surface table.

Early-abort: CONFIRMED = 0 AND CORROBORATED = 0 -> HALT [G5.5] BLOCKING.
`--amend waive:convergence` allows Gate 9 with SOLO-only findings.
Under waive path, SOLO FINDINGS table is mandatory.

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

| IC-ID | Inertia Claim                               | Strength |
|-------|---------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                 | [H/M/L]  |

IC-CHALLENGED: every finding row carries IC-CHALLENGED = IC-[N] or `none`.
Absent: HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT (C-33 extended)

RUN HEALTH emits Stage field (declared value) and SCOPE DISTRIBUTION table in BOTH
clean and failed variants.

**Diagnostic positioning requirement (C-33):**
In the failed variant, Stage field and SCOPE DISTRIBUTION table are the first content
block, appearing before any recovery items. A reviewer must be able to read Stage +
SCOPE DISTRIBUTION without encountering recovery instructions first. Recovery items
begin only after SCOPE DISTRIBUTION closes.

**SCOPE DISTRIBUTION schema:**
```
SCOPE DISTRIBUTION ({{stage}}):
| Group      | Count | Verdict contribution                |
|------------|-------|-------------------------------------|
| YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
| ADVISORY   | [N]   | Noted; not blocking                 |
| NO         | [N]   | Excluded (scope floor)              |
| DEPRECATED | [N]   | Informational only                  |
```

All four rows are required as distinct entries. NO and DEPRECATED are not conflated.
Counts must be resolved values (not placeholders) before RUN HEALTH is emitted.

---

### PRE-EXECUTION: HALT REGISTRY

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
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)                 | BLOCKING |
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 waivable. G5.5 does not fire for DEPRECATED artifacts.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

Same as V-01.

---

### REVIEWER PRIORITY MANIFEST

Same as V-01.

---

### EXECUTION

Gates 0.5 through 9 are identical to V-01 except RUN HEALTH below.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a-G4h (all roles), G4.5, G5, G5.5, G6, G7, G8, G9
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
  Result:        Matrix complete. All contracts honored.
```

**Failed run (C-33: Stage + SCOPE DISTRIBUTION as standalone diagnostic header, before recovery):**
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
  [Stage + SCOPE DISTRIBUTION complete -- diagnostic header above is self-contained]
  Recovery (paste and execute in order):
  1. [gate-id] [trigger description]
     -> /crew-check {{artifact}} --amend [operation]
  After all fixes: /crew-check {{artifact}} --stage {{stage}}
```

Note: Stage and SCOPE DISTRIBUTION appear before recovery items in the failed variant.
A reviewer can determine stage and scope distribution without reading recovery content.
Reading the failed cert does not require cross-referencing the clean cert or run transcript.

---

### AMEND

Same as V-01.

---

## V-04

**Axis**: C-31 + C-32 -- Mutual enforcement + extended SOLO schema combined
**Hypothesis**: V-01 adds the MUTUAL ENFORCEMENT DECLARATION to CONVERGENCE SNAPSHOT
CONTRACT (C-31). V-02 adds the 8-column SOLO FINDINGS schema with IC-CHALLENGED and
STAGE-APPROPRIATE (C-32). V-04 combines both. The integration test: do C-31 and C-32
compose without conflict? C-31 targets the CONVERGENCE SNAPSHOT CONTRACT (contract text
layer) and the Gate 5.5 waive path note (execution layer). C-32 targets the SOLO FINDINGS
SCHEMA CONTRACT (pre-execution schema declaration) and the Gate 9 table format (execution
layer). The two share one surface: the SOLO FINDINGS table. C-31 governs the contractual
condition under which the table is required (waive:convergence activates it as enforcement
substitute) and the declared empty exit. C-32 governs what columns the table must carry
(IC-CHALLENGED + STAGE-APPROPRIATE). Both requirements apply to the same table without
conflict: a waive-path run must emit an 8-column SOLO FINDINGS table with declared empty
exit. The declared empty exit under V-01 ("No SOLO findings under waive:convergence.
Convergence substitute satisfied (declared empty exit).") and the declared empty exit
under V-02 ("SOLO FINDINGS table: empty (declared).") merge into a single unified
declaration. The claim: C-31 and C-32 are contractually independent (different enforcement
paths, different pre-execution sections), share the SOLO FINDINGS table as their
enforcement surface, and compose additively -- the combined prompt satisfies both
criteria simultaneously without introducing any gate conflict.

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

SOLO disposition tags: ESCALATE / DISMISS:rationale / ROLE-SPECIFIC
Convergence register over YES-scope rows only.

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after all domain roles complete,
before Gate 6 and Gate 9.

Must emit: (1) tier counts as labeled fields; (2) convergence register surface table.

Early-abort: CONFIRMED = 0 AND CORROBORATED = 0 -> HALT [G5.5] BLOCKING.

**MUTUAL ENFORCEMENT DECLARATION (C-31):**
`--amend waive:convergence` does not waive accountability. It substitutes Gate 5.5
convergence enforcement with mandatory Gate 9 SOLO FINDINGS disposition (FINDING
CONVERGENCE CONTRACT, SOLO tier Gate 9 obligation; 8-column schema per SOLO FINDINGS
SCHEMA CONTRACT). The enforcement chain: Gate 5.5 convergence requirement -> waived;
SOLO FINDINGS disposition (Gate 9, 8-column) -> activated as mandatory substitute.
A run under waive:convergence MUST emit the 8-column SOLO FINDINGS table at Gate 9.
If no SOLO findings exist under waive path, emit the unified declared exit:
"No SOLO findings under waive:convergence. Convergence substitute satisfied (declared
empty exit). SOLO FINDINGS table: empty (declared)."
Silent skip is a contract violation under both C-31 and C-32.

---

### PRE-EXECUTION: SOLO FINDINGS SCHEMA CONTRACT (C-32)

The SOLO FINDINGS table uses an 8-column schema declared here. Required on every run.

**8-column schema:**
```
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition |
```

- `IC-CHALLENGED`: carry forward from finding row (IC-[N] or `none`).
- `STAGE-APPROPRIATE`: carry forward from finding row (YES / ADVISORY / NO / DEPRECATED).
- `Disposition`: ESCALATE | DISMISS:rationale | ROLE-SPECIFIC (one required per row).

**Empty-case declared exit (unified with C-31 mutual enforcement):**
If zero SOLO findings:
- Standard run: "No SOLO findings. All surfaces cited by 2+ roles. SOLO FINDINGS table:
  empty (declared)."
- waive:convergence run: "No SOLO findings under waive:convergence. Convergence substitute
  satisfied (declared empty exit). SOLO FINDINGS table: empty (declared)."

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

---

### PRE-EXECUTION: HALT REGISTRY

Same as V-01 (G0.5 through G5.5).

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

Same as V-01.

---

### REVIEWER PRIORITY MANIFEST

Same as V-01.

---

### EXECUTION

Gates 0.5 through 8 are identical to V-01 except Gate 2 and Gate 9.

**Gate 2 -- Calibration contract acknowledgment**

State: "All pre-execution contracts active: severity/confidence calibration, artifact
maturity stage, finding convergence, convergence snapshot (with mutual enforcement
declaration), SOLO FINDINGS schema (8-column: IC-CHALLENGED + STAGE-APPROPRIATE),
inertia claim registry, RUN HEALTH scope distribution.
Stage: {{stage}}. Scope-grouped matrix, dual-axis sort. CONFIRMED = HIGH-effective.
Gate 5.5 snapshot fires after all role reviews; early-abort if CONFIRMED=0, CORROBORATED=0.
waive:convergence activates mandatory 8-column SOLO FINDINGS table as enforcement
substitute; unified declared empty exit required if no SOLO findings.
STANDING IC at HIGH strength blocks. IC-CHALLENGED required per row."

**Gate 9 -- Cross-role synthesis, SOLO disposition (8-column), and LOW enumeration**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface (or SOLO pattern if waived).

Mandatory Confidence=LOW enumeration -- same as V-01.

Mandatory SOLO FINDINGS table (8-column schema -- IC-CHALLENGED + STAGE-APPROPRIATE):
```
SOLO FINDINGS (mandatory disposition -- 8-column schema):
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition                              |
|------|---------|----------|------------|---------------|-------------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...           | ...               | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

Empty case (unified C-31 + C-32 declared exit):
- Standard: "No SOLO findings. All surfaces cited by 2+ roles. SOLO FINDINGS table:
  empty (declared)."
- waive:convergence: "No SOLO findings under waive:convergence. Convergence substitute
  satisfied (declared empty exit). SOLO FINDINGS table: empty (declared)."

State whether CONFIRMED-LOW would change IC status if elevated. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2, G3, G4a-G4h (all roles), G4.5, G5, G5.5, G6, G7, G8, G9
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
  CONFIRMED: [N], CONFIRMED-LOW: [N], CORROBORATED: [N]
  SOLO disposed: [N] -- 8-column schema (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])
  STANDING HIGH ICs: [N]
  Result:        Matrix complete. All contracts honored.
```

**Failed run:**
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

Same as V-01, with waive:convergence note updated:
"waive:convergence activates mandatory 8-column SOLO FINDINGS table (IC-CHALLENGED +
STAGE-APPROPRIATE) as enforcement substitute per MUTUAL ENFORCEMENT DECLARATION;
unified declared empty exit required if no SOLO findings."

---

## V-05

**Axis**: C-31 + C-32 + C-33 + C-34 -- Full four-axis integration
**Hypothesis**: V-01 adds explicit waive:convergence mutual enforcement (C-31). V-02
adds IC-CHALLENGED + STAGE-APPROPRIATE to the SOLO FINDINGS table (C-32). V-03
restructures the failed RUN HEALTH as a standalone diagnostic with Stage + SCOPE
DISTRIBUTION before recovery (C-33). V-05 adds all three plus C-34: Gate 2 unified
contract acknowledgment. C-34 requires Gate 2 to emit a single numbered enumeration of
all active pre-execution contracts by name, creating an auditable start-of-run checkpoint.
A reviewer can open Gate 2, read the enumeration, compare it against PRE-EXECUTION
section headers, and detect any contract declared in PRE-EXECUTION but absent from the
Gate 2 list. The four axes target different execution positions: CONVERGENCE SNAPSHOT
CONTRACT text (C-31), SOLO FINDINGS table schema (C-32), failed RUN HEALTH layout (C-33),
Gate 2 acknowledgment format (C-34). No two axes share a gate. The integration test:
does adding Gate 2 enumeration conflict with any of the three axes from V-01-V-03?
C-34 touches only Gate 2 -- it adds structure to an acknowledgment block that currently
emits prose. C-31, C-32, C-33 each touch different sections (CONVERGENCE SNAPSHOT
CONTRACT, SOLO FINDINGS SCHEMA CONTRACT, RUN HEALTH). The claim: all four compose
without conflict, and the resulting prompt satisfies C-31 through C-34 simultaneously
on the R9 V-05 base.

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

SOLO disposition tags: ESCALATE / DISMISS:rationale / ROLE-SPECIFIC
Convergence register over YES-scope rows only.

---

### PRE-EXECUTION: CONVERGENCE SNAPSHOT CONTRACT

Gate 5.5 fires as a named mid-run checkpoint after all domain roles complete,
before Gate 6 and Gate 9.

Must emit: (1) tier counts as labeled fields; (2) convergence register surface table.

Early-abort: CONFIRMED = 0 AND CORROBORATED = 0 -> HALT [G5.5] BLOCKING.

**MUTUAL ENFORCEMENT DECLARATION (C-31):**
`--amend waive:convergence` does not waive accountability. It substitutes Gate 5.5
convergence enforcement with mandatory Gate 9 SOLO FINDINGS disposition (FINDING
CONVERGENCE CONTRACT, SOLO tier Gate 9 obligation; 8-column schema per SOLO FINDINGS
SCHEMA CONTRACT). The enforcement chain: Gate 5.5 convergence requirement -> waived;
SOLO FINDINGS disposition (Gate 9, 8-column) -> activated as mandatory substitute.
A run under waive:convergence MUST emit the 8-column SOLO FINDINGS table at Gate 9.
If no SOLO findings exist under waive path, emit the unified declared exit:
"No SOLO findings under waive:convergence. Convergence substitute satisfied (declared
empty exit). SOLO FINDINGS table: empty (declared)."
Silent skip is a contract violation.

---

### PRE-EXECUTION: SOLO FINDINGS SCHEMA CONTRACT (C-32)

The SOLO FINDINGS table uses an 8-column schema declared here. Required on every run.

**8-column schema:**
```
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition |
```

- `IC-CHALLENGED`: carry forward from finding row (IC-[N] or `none`). Enables auditing
  disposition against inertia impact.
- `STAGE-APPROPRIATE`: carry forward from finding row (YES / ADVISORY / NO / DEPRECATED).
  Enables auditing disposition against scope group.
- `Disposition`: ESCALATE | DISMISS:rationale | ROLE-SPECIFIC (one required per row).

**Empty-case declared exit (unified C-31 + C-32):**
- Standard: "No SOLO findings. All surfaces cited by 2+ roles. SOLO FINDINGS table:
  empty (declared)."
- waive:convergence: "No SOLO findings under waive:convergence. Convergence substitute
  satisfied (declared empty exit). SOLO FINDINGS table: empty (declared)."

---

### PRE-EXECUTION: INERTIA CLAIM REGISTRY

| IC-ID | Inertia Claim                               | Strength |
|-------|---------------------------------------------|----------|
| IC-01 | [to be populated at Gate 3]                 | [H/M/L]  |
| IC-02 | [to be populated at Gate 3]                 | [H/M/L]  |

IC-CHALLENGED: every finding row carries IC-CHALLENGED = IC-[N] or `none`.
Absent: HALT [G4e-{role}] SCOPED.

---

### PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT (C-33 extended)

RUN HEALTH emits Stage field (declared value) and SCOPE DISTRIBUTION table in BOTH
clean and failed variants.

**Diagnostic positioning requirement (C-33):**
In the failed variant, Stage field and SCOPE DISTRIBUTION table are the first content
block, appearing before any recovery items. Recovery items begin only after SCOPE
DISTRIBUTION closes.

**SCOPE DISTRIBUTION schema:**
```
SCOPE DISTRIBUTION ({{stage}}):
| Group      | Count | Verdict contribution                |
|------------|-------|-------------------------------------|
| YES        | [N]   | Evaluated for BLOCKED/CONDITIONAL   |
| ADVISORY   | [N]   | Noted; not blocking                 |
| NO         | [N]   | Excluded (scope floor)              |
| DEPRECATED | [N]   | Informational only                  |
```

All four rows required as distinct entries. NO and DEPRECATED are not conflated.
Counts must be resolved before RUN HEALTH is emitted.

---

### PRE-EXECUTION: HALT REGISTRY

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
| G5            | Zero STAGE-APPROPRIATE=YES findings (non-DEPRECATED)                 | BLOCKING |
| G5.5          | Zero cross-role convergence (CONFIRMED=0 AND CORROBORATED=0)         | BLOCKING |

G5.5 waivable via `--amend waive:convergence`. See MUTUAL ENFORCEMENT DECLARATION.
G5.5 does not fire for DEPRECATED artifacts.

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

Read `.craft/roles/`. If absent: emit `HALT [G1]`.

| Priority | Slot        | Role Name      | Basis                          |
|----------|-------------|----------------|--------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]    | Inertia-advocate: always first |
| 2        | DOMAIN-1    | [ROLE_NAME]    | [reason]                       |
| 3+       | DOMAIN-2..N | [ROLE_NAME...] | [reason]                       |
| N (fixed)| CHALLENGER  | [ROLE_NAME]    | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with rationale. State total role count.

---

### EXECUTION

**Gate 0.5 -- Stage acknowledgment**

```
HALT [G0.5]: Stage absent or not recognized.
-> /crew-check {{artifact}} --amend stage:[DRAFT|REVIEW|APPROVED|DEPRECATED] (BLOCKING)
```

Otherwise: "Artifact maturity stage: {{stage}}. Scope calibration locked."
If DEPRECATED: "All findings STAGE-APPROPRIATE=DEPRECATED. Readiness will be READY."

**Gate 1 -- Role registry load**

```
HALT [G1]: .craft/roles/ absent or unreadable.
-> /crew-check {{artifact}} --amend reload (BLOCKING)
```

**Gate 2 -- Unified contract acknowledgment (C-34)**

Emit a single numbered enumeration of all active pre-execution contracts by name.
Any contract declared in PRE-EXECUTION but absent from this list is detectable by
comparing the two locations.

```
Pre-execution contracts active (all seven):
1. SEVERITY AND CONFIDENCE CALIBRATION CONTRACT
2. ARTIFACT MATURITY STAGE CONTRACT
3. FINDING CONVERGENCE CONTRACT
4. CONVERGENCE SNAPSHOT CONTRACT (includes MUTUAL ENFORCEMENT DECLARATION)
5. SOLO FINDINGS SCHEMA CONTRACT (8-column: IC-CHALLENGED + STAGE-APPROPRIATE)
6. INERTIA CLAIM REGISTRY
7. RUN HEALTH SCOPE DISTRIBUTION CONTRACT (includes diagnostic positioning requirement)

Stage: {{stage}}. Scope-grouped matrix (YES -> ADVISORY -> NO/DEPRECATED), dual-axis sort.
CONFIRMED (same surface + matching confidence != LOW, 2+ YES-scope roles) = HIGH-effective.
Gate 5.5 snapshot fires after all role reviews; early-abort if CONFIRMED=0, CORROBORATED=0.
waive:convergence activates mandatory 8-column SOLO FINDINGS table as enforcement
substitute per contract 4; unified declared empty exit required if no SOLO findings.
SOLO FINDINGS table uses 8-column schema per contract 5; IC-CHALLENGED + STAGE-APPROPRIATE
required on all rows; declared empty exit required.
RUN HEALTH failed variant: Stage + SCOPE DISTRIBUTION precede recovery per contract 7.
STANDING IC at HIGH strength blocks. IC-CHALLENGED required per finding row.
```

**Gate 3 -- Challenger: opening bracket and IC registration**

Populate INERTIA CLAIM REGISTRY >= 2 ICs (IC-01, IC-02...). Assign Strength (H/M/L).
Note stage relevance.

On fewer than 2:
```
HALT [G3a]: Challenger produced fewer than 2 inertia claims. (BLOCKING)
-> /crew-check {{artifact}} --amend rerun:challenger
```

Emit "Inertia registry locked. Stage-scoped domain review proceeds."

**Gate 4 -- Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order)

*G4a -- Lens anchor*:
```
HALT [G4a-{role}]: Lens anchor not stated. -> /crew-check {{artifact}} --amend rerun:G4a-{role} (BLOCKING)
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

**Gate 4.5 -- CHALLENGE RESPONSE MAP**

```
| IC-ID | Strength | Challenging Findings (Role -- Sev/Conf, STAGE-APPROPRIATE) | IC Status             |
|-------|----------|-------------------------------------------------------------|-----------------------|
| IC-01 | H        | [pm HIGH/HIGH, YES], [arch MEDIUM/HIGH, YES]                | OVERCOME-CONFIRMED    |
| IC-02 | M        | [pm LOW/LOW, YES]                                           | CONTESTED             |
| IC-03 | H        | (none in YES scope)                                         | STANDING              |
```

IC Status: OVERCOME, OVERCOME-CONFIRMED, CONTESTED, STANDING. Emit before Gate 5.

**Gate 5 -- Matrix assembly: scope-grouped, dual-axis sorted**

Group order: YES -> ADVISORY -> NO -> DEPRECATED -> EXCLUDED ROLES.
Sort within each group: severity DESC, confidence DESC.
Schema: `| Role | Finding | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Recommendation |`

```
HALT [G5]: Zero stage-appropriate findings.
-> /crew-check {{artifact}} --amend depth:deep
   /crew-check {{artifact}} --amend stage:[correct]
```

**Gate 5.5 -- CONVERGENCE SNAPSHOT** (counts + early-abort + mutual enforcement waive path)

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
-> /crew-check {{artifact}} --amend depth:deep
-> /crew-check {{artifact}} --amend add:{role}
-> /crew-check {{artifact}} --amend waive:convergence
  (BLOCKING -- waive:convergence activates FINDING CONVERGENCE CONTRACT SOLO tier
   disposition as mandatory enforcement substitute per MUTUAL ENFORCEMENT DECLARATION;
   8-column SOLO FINDINGS table required at Gate 9 per SOLO FINDINGS SCHEMA CONTRACT;
   unified declared empty exit required if no SOLO findings; convergence is substituted,
   not waived)
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

**Gate 6 -- Priority summary**

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

**Gate 7 -- Readiness verdict**

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

**Gate 8 -- Challenger: closing bracket and CHALLENGE RESPONSE MAP review**

Review each IC:
- OVERCOME/OVERCOME-CONFIRMED: acknowledge; name evidence.
- CONTESTED: specify additional evidence needed.
- STANDING: explain absence of YES-scope challenge.

Note CONFIRMED convergence vs STANDING ICs. Note ADVISORY latent risk.
Revise readiness only if YES-scope or STANDING IC analysis warrants.
Emit: "Inertia, convergence, and stage assessment complete."

**Gate 9 -- Cross-role synthesis, SOLO disposition (8-column), and LOW enumeration**

2-4 sentences naming >= 1 CONFIRMED or CORROBORATED surface (or SOLO pattern if waived).

Mandatory Confidence=LOW enumeration:
```
CONFIDENCE=LOW FINDINGS (require independent verification before action):
| Role | Surface | Severity | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary |
|------|---------|----------|---------------|-------------------|-----------------|
| ...  | ...     | ...      | ...           | ...               | ...             |
```

Mandatory SOLO FINDINGS table (8-column schema -- IC-CHALLENGED + STAGE-APPROPRIATE):
```
SOLO FINDINGS (mandatory disposition -- 8-column schema):
| Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition                              |
|------|---------|----------|------------|---------------|-------------------|-----------------|------------------------------------------|
| ...  | ...     | ...      | ...        | ...           | ...               | ...             | ESCALATE|DISMISS:rationale|ROLE-SPECIFIC |
```

Disposition semantics:
- ESCALATE: warrants `--amend add:{role}` or `--amend depth:deep` before final verdict.
- DISMISS:rationale: role-specific noise; rationale required inline.
- ROLE-SPECIFIC: valid only from this lens; no cross-role action needed.

Empty case (unified C-31 + C-32):
- Standard: "No SOLO findings. All surfaces cited by 2+ roles. SOLO FINDINGS table:
  empty (declared)."
- waive:convergence: "No SOLO findings under waive:convergence. Convergence substitute
  satisfied (declared empty exit). SOLO FINDINGS table: empty (declared)."

State whether CONFIRMED-LOW would change IC status or readiness if elevated.
Reference role names. No new findings.

---

### RUN HEALTH

**Clean run:**
```
RUN HEALTH: PASS
  Stage:         {{stage}}
  Gates checked: G0.5, G1, G2 (unified enumeration), G3, G4a-G4h (all roles), G4.5,
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
  CONFIRMED: [N], CONFIRMED-LOW: [N], CORROBORATED: [N]
  SOLO disposed: [N] -- 8-column (IC-CHALLENGED + STAGE-APPROPRIATE present; ESCALATE: [N],
    DISMISS: [N], ROLE-SPECIFIC: [N])
  STANDING HIGH ICs: [N]
  Contracts acknowledged at Gate 2: 7/7
  Result:        Matrix complete. All contracts honored.
```

**Failed run (C-33: Stage + SCOPE DISTRIBUTION as standalone diagnostic header, before recovery):**
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
  [Stage + SCOPE DISTRIBUTION complete -- diagnostic header above is self-contained]
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
- `waive:convergence` -- waive G5.5 early-abort; activates mandatory 8-column SOLO
  FINDINGS table as enforcement substitute per MUTUAL ENFORCEMENT DECLARATION; unified
  declared empty exit required if no SOLO findings
- `rerun:{role}` -- full role restart from G4a
- `rerun:challenger` -- restart Gate 3
- `rerun:G4a-{role}` through `rerun:G4h-{role}` -- re-enter at named sub-gate
- `reload` -- re-load `.craft/roles/` and restart
- `halts` -- list all gates that fired in this run
- `halts:{gate-id}` -- show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT -- [N] gate(s) fired this run:
| Gate ID        | Trigger description                    | Tier     | Re-entry command                                          |
|----------------|----------------------------------------|----------|-----------------------------------------------------------|
| [G0.5]         | Stage 'WIP' not in valid set           | BLOCKING | /crew-check {{artifact}} --amend stage:DRAFT              |
| [G4e-pm]       | IC-CHALLENGED column absent            | SCOPED   | /crew-check {{artifact}} --amend rerun:G4e-pm             |
| [G5.5]         | CONFIRMED=0, CORROBORATED=0            | BLOCKING | /crew-check {{artifact}} --amend waive:convergence        |
| [G4g-architect]| Confidence column absent               | DEFERRED | /crew-check {{artifact}} --amend rerun:G4g-architect      |
```
Each entry is paste-ready. Re-entry encodes minimum-restart routing per SUB-GATE SKIP-MAP.
