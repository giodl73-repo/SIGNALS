---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 6
rubric: crew-check-rubric-v5-2026-03-17.md
---

# crew-check — Variate R6

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v5 floor (all variations must hold):
- Essential: C-01 role source, C-02 matrix structure, C-03 perspective fidelity, C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational: C-09 cross-role synthesis, C-10 AMEND responsiveness, C-11 lens-anchoring step,
  C-12 severity calibration contract, C-13 challenger-first, C-14 readiness-gate framing,
  C-15 severity-sorted output, C-16 hard-halt execution gate, C-17 named halt identifier system,
  C-18 AMEND gate-audit sub-command, C-19 self-routing halt messages, C-20 executable audit output

Design intent for R6: All five variations hold the R5 v5 floor (C-01 through C-20 present in all).
R5 V-01, V-03, V-05 contained the three new structural patterns incidentally or as a single axis.
R6 makes each a load-bearing pre-committed preamble contract — not a behavioral side-effect.
Single-axis variations isolate each deepened pattern; V-04 and V-05 combine them.

Axes selected for R6:
- V-01: Sub-gate skip-map as pre-committed preamble contract (minimum-restart routing formalized)
- V-02: Run health certificate (success-conditioned output structured in BOTH directions)
- V-03: Three-tier halt scope: BLOCKING / SCOPED / DEFERRED
- V-04: Skip-map + three-tier halts (axes 1 + 3: per-tier minimum-restart semantics)
- V-05: Full R6 integration (skip-map + health certificate + three-tier + tier-routed re-entry)

---

## V-01

**Axis**: Sub-gate skip-map as pre-committed preamble contract
**Hypothesis**: R5 V-01 deepened C-19 by embedding sub-gate-precise re-entry commands
(`--amend rerun:G4c-{role}` instead of `--amend rerun:{role}`) and describing skip semantics
inline at each sub-gate. The skip property was stated in prose but not pre-committed as a
structural contract. V-01 R6 formalizes it: a SUB-GATE SKIP-MAP table is declared before any
gate executes, enumerating each re-entry entry point, which sub-gates it skips, and the
prerequisite condition that makes skipping safe. The claim: when skip semantics are pre-committed
in a named table rather than described inline, (a) the model cannot silently re-execute already-
passing sub-gates, (b) auditors can verify minimum-restart behavior by checking the skip-map
before examining output, and (c) AMEND routing commands are fully specified by the pre-committed
table alone — no gate-level prose is required to understand what a re-entry command does.

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

All halt conditions are declared before execution. Halt messages in output MUST match this
registry verbatim. `{role}` = role file name without extension. `{value}` = the invalid value
received.

| Halt ID        | Trigger condition                          | Tier     |
|----------------|--------------------------------------------|----------|
| G1             | `.craft/roles/` absent or unreadable       | BLOCKING |
| G4a-{role}     | Lens anchor not stated before first finding| BLOCKING |
| G4b-{role}     | Finding not tied to a named artifact surface | BLOCKING |
| G4c-{role}     | Severity `{value}` not in calibration contract | BLOCKING |
| G4d-{role}     | Recommendation missing location reference  | BLOCKING |
| G5             | Zero findings produced across all roles    | BLOCKING |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

For any `--amend rerun:G4x-{role}` command, the skip-map governs which sub-gates are
re-executed and which are skipped. Skipping is safe only when the prerequisite condition
was verified in the prior run.

| Re-entry command        | Resumes at | Skips              | Prerequisite for safe skip                             |
|-------------------------|------------|--------------------|--------------------------------------------------------|
| `--amend rerun:{role}`  | G4a        | (nothing)          | Full role re-execution from lens anchor                |
| `--amend rerun:G4a-{role}` | G4a     | (nothing)          | Full role re-execution from lens anchor                |
| `--amend rerun:G4b-{role}` | G4b     | G4a                | Lens anchor verified in prior run                      |
| `--amend rerun:G4c-{role}` | G4c     | G4a, G4b           | Lens anchor + named artifact surface verified          |
| `--amend rerun:G4d-{role}` | G4d     | G4a, G4b, G4c      | Lens anchor + surface + severity all verified          |

At re-entry time, state which sub-gates are being skipped and cite the prerequisite condition.
Do not silently re-execute a passing sub-gate — the skip-map is a constraint, not a suggestion.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

Assign slots:

| Priority | Slot       | Role Name          | Basis                          |
|----------|------------|--------------------|--------------------------------|
| 1        | CHALLENGER | [ROLE_NAME]        | Inertia-advocate: always first |
| 2        | DOMAIN-1   | [ROLE_NAME]        | [reason]                       |
| 3+       | DOMAIN-2..N| [ROLE_NAME...]     | [reason]                       |
| N (last) | CHALLENGER | [ROLE_NAME]        | Bracket close: always last     |

Challenger occupies first and last slots (fixed). `deep`: all roles. `standard`: relevant roles
with selection rationale.

---

### EXECUTION

**Gate 1 — Role registry load**

You are not ready to select reviewers until `.craft/roles/` is confirmed readable and non-empty.

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active. HIGH=3, MEDIUM=2, LOW=1. No other values permitted."

You are not ready to run any reviewer until this contract is acknowledged.

**Gate 3 — Challenger: opening bracket**

Inertia-advocate reviews first. State what the team does today without `{{artifact}}` and why
that is acceptable. Name >= 2 specific status-quo strengths. This gate produces the null hypothesis
framing, not findings. Emit: "Status quo registered. Domain review proceeds."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing Challenger)

For each role:

*G4a — Lens anchor*: State the role's lens in one sentence before any finding. Format:
"From the [role] perspective, this review examines [specific surface of {{artifact}}]."

On missing lens anchor:
```
HALT [G4a-{role}]: Lens anchor not stated before first finding.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
  (full role restart — no sub-gates skipped)
```

*G4b — Surface finding*: Every finding row must name a specific artifact surface (field, section,
behavior, schema element). Format: `| Role | Finding | Artifact Surface | Severity | Recommendation |`

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
  (skip-map: G4a + G4b skipped — lens anchor and surface verified in prior run)
```

*G4d — Recommendation completeness*: Every recommendation must include a location reference.
On missing location:
```
HALT [G4d-{role}]: Recommendation missing location reference.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (skip-map: G4a + G4b + G4c skipped — lens anchor, surface, severity all verified)
```

**Gate 5 — Matrix assembly and severity sort**

Assemble all staged rows. Sort descending by severity score (HIGH=3 first). Within severity tier:
Challenger rows before domain rows.

If zero findings from all roles:
```
HALT [G5]: Zero findings produced across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:   [N] findings — [top finding brief]
  MEDIUM: [N] findings
  LOW:    [N] findings
```

**Gate 7 — Readiness verdict**

Apply: any HIGH = BLOCKED. Any MEDIUM, no HIGH = CONDITIONAL. All LOW or none = READY.
Emit: `READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate reviews last. Given the domain findings, does the status quo hold? Name the
strongest counter-evidence from the domain review. Revise readiness recommendation if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. Name >= 1 cross-role convergence or conflict. Reference role names. No new findings.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a (no sub-gates skipped)
- `rerun:G4a-{role}` through `rerun:G4d-{role}` — re-enter at named sub-gate (skip-map applies; state skipped sub-gates at re-entry)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID       | Trigger description                 | Re-entry command                              |
|---------------|-------------------------------------|-----------------------------------------------|
| [G4c-pm]      | Severity 'CRITICAL' not in contract | /crew-check {{artifact}} --amend rerun:G4c-pm |
```
Each entry is paste-ready. The Re-entry command encodes minimum-restart routing per the
SUB-GATE SKIP-MAP — using it directly is equivalent to consulting the skip-map manually.

---

## V-02

**Axis**: Run health certificate — success-conditioned output structured in both directions
**Hypothesis**: R5 V-05 introduced the success-conditioned RECOVERY BLOCK: present on failure,
absent on success. The signal was asymmetric — failure was named and structured (RECOVERY BLOCK),
but success was signaled only by absence. V-02 R6 makes both directions structurally named: on a
clean run, a RUN HEALTH CERTIFICATE section appears, enumerating all gates PASS and confirming
zero halts. On a failed run, the same section becomes the RECOVERY BLOCK. The section heading
itself encodes run state: `RUN HEALTH: PASS` vs `RUN HEALTH: [N] HALT(S) FIRED`. The claim:
when both clean and failed runs produce a named output section at the same structural position,
(a) users always know where to look for run status regardless of outcome, (b) the clean signal
is as legible as the failure signal, and (c) the output contract is symmetric — no "absence"
semantics required to interpret the result.

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

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW permitted. Any other value triggers HALT [G4c-{role}].

---

### PRE-EXECUTION: HALT REGISTRY

| Halt ID        | Trigger condition                              |
|----------------|------------------------------------------------|
| G1             | `.craft/roles/` absent or unreadable           |
| G4a-{role}     | Lens anchor not stated before first finding    |
| G4b-{role}     | Finding not tied to a named artifact surface   |
| G4c-{role}     | Severity `{value}` not in calibration contract |
| G4d-{role}     | Recommendation missing location reference      |
| G5             | Zero findings produced across all roles        |

---

### PRE-EXECUTION: RUN HEALTH CONTRACT

After all gates complete, emit a RUN HEALTH section at a fixed position (after Gate 9, before
AMEND). The section heading and content depend on run outcome:

**Clean run (zero halts fired):**
```
RUN HEALTH: PASS
  Gates checked: G1, G2, G4a through G4d (all roles), G5
  Halts fired:   0
  Result:        Matrix complete. Proceed to readiness verdict.
```

**Failed run (>= 1 halt fired):**
```
RUN HEALTH: [N] HALT(S) FIRED
  Recovery (paste and execute in order):

  1. [G4a-pm] Lens anchor not stated
     → /crew-check {{artifact}} --amend rerun:G4a-pm

  2. [G4c-inertia-advocate] Severity 'BLOCKER' not in contract
     → /crew-check {{artifact}} --amend rerun:G4c-inertia-advocate

  After all fixes: /crew-check {{artifact}}
```

The RUN HEALTH section always appears. Its heading encodes run state. On failure it is also the
recovery procedure. No separate RECOVERY BLOCK — the health certificate serves both functions.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: `HALT [G1]: .craft/roles/ absent. → /crew-check {{artifact}} --amend reload`

| Priority | Slot       | Role Name          | Basis                          |
|----------|------------|--------------------|--------------------------------|
| 1        | CHALLENGER | [ROLE_NAME]        | Inertia-advocate: always first |
| 2        | DOMAIN-1   | [ROLE_NAME]        | [reason]                       |
| 3+       | DOMAIN-2..N| [ROLE_NAME...]     | [reason]                       |
| N (last) | CHALLENGER | [ROLE_NAME]        | Bracket close: always last     |

---

### EXECUTION

**Gate 1 — Role registry load**

You are not ready to select reviewers until `.craft/roles/` is confirmed readable.

On failure:
```
HALT [G1]: .craft/roles/ absent or unreadable.
→ To continue: /crew-check {{artifact}} --amend reload
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active." You are not ready to run reviewers until stated.

**Gate 3 — Challenger: opening bracket**

Inertia-advocate first. State what the team does today without `{{artifact}}` and why acceptable.
Name >= 2 status-quo strengths. Emit: "Status quo registered."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing Challenger)

For each role:

*G4a — Lens anchor* (required before any finding):
"From the [role] perspective, this review examines [specific surface of {{artifact}}]."

On missing:
```
HALT [G4a-{role}]: Lens anchor not stated.
→ To continue: /crew-check {{artifact}} --amend rerun:G4a-{role}
```

*G4b — Surface finding*: Every finding must name a specific artifact surface.
`| Role | Finding | Artifact Surface | Severity | Recommendation |`

On missing surface:
```
HALT [G4b-{role}]: Finding lacks named artifact surface.
→ To continue: /crew-check {{artifact}} --amend rerun:G4b-{role}
```

*G4c — Severity validation*: All labels must be HIGH / MEDIUM / LOW.
On invalid:
```
HALT [G4c-{role}]: Severity '{value}' not in contract.
→ To continue: /crew-check {{artifact}} --amend rerun:G4c-{role}
```

*G4d — Recommendation completeness*: Every recommendation must include a location reference.
On missing:
```
HALT [G4d-{role}]: Recommendation missing location.
→ To continue: /crew-check {{artifact}} --amend rerun:G4d-{role}
```

**Gate 5 — Matrix assembly and severity sort**

Assemble staged rows. Sort HIGH first (score 3→2→1). Challenger rows before domain within tier.

On zero findings:
```
HALT [G5]: Zero findings across all roles.
→ To continue: /crew-check {{artifact}} --amend depth:deep
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:   [N] findings — [top finding brief]
  MEDIUM: [N] findings
  LOW:    [N] findings
```

**Gate 7 — Readiness verdict**

Apply: any HIGH = BLOCKED. Any MEDIUM, no HIGH = CONDITIONAL. All LOW or none = READY.
`READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate reviews last. Does status quo hold given domain findings? Revise verdict
if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. >= 1 cross-role convergence or conflict named. No new findings.

**Gate 10 — RUN HEALTH section**

Emit the RUN HEALTH section per the RUN HEALTH CONTRACT. This is the final named section
before AMEND. On a clean run: certificate format. On failure: numbered recovery procedure format.
The section always appears at this position regardless of run outcome.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — re-run a specific role from G4a
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired in this run
- `halts:{gate-id}` — show single halt registry entry by ID

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] gate(s) fired this run:
| Gate ID   | Trigger description              | Re-entry command                           |
|-----------|----------------------------------|--------------------------------------------|
| [halt-id] | [trigger]                        | /crew-check {{artifact}} --amend rerun:... |
```
Each entry is paste-ready.

---

## V-03

**Axis**: Three-tier halt scope — BLOCKING / SCOPED / DEFERRED
**Hypothesis**: R5 V-03 introduced BLOCKING (run-level full stop) vs SCOPED (row-level skip, run
continues with partial matrix). Both tiers require re-run to resolve. V-03 R6 introduces a third
tier: DEFERRED. A DEFERRED halt does not stop the run and does not exclude the row — the finding
is included in the matrix with a [DEFERRED] tag, and the run completes. However, any DEFERRED
finding forces READINESS to CONDITIONAL regardless of severity. The three-tier model addresses
a real failure scope question: some validation issues are run-blockers (no output makes sense),
some are row-specific (other rows are valid and useful), and some are advisory flags that should
be visible in the output without stopping anything. The DEFERRED tier captures that third case:
"this finding has a validation concern, but the matrix is still useful as-is."

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

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW permitted.

---

### PRE-EXECUTION: HALT REGISTRY

Three halt tiers govern failure behavior. Tier determines what happens to the run.

**BLOCKING** — run-level full stop. No output produced after halt point. Must resolve before
any output is useful.

**SCOPED** — row-level skip. The failing role's row is excluded from the matrix; all other
rows proceed. Run completes with partial matrix. Excluded rows appear below the matrix as
`[EXCLUDED: {role} — {halt-id}]`.

**DEFERRED** — finding-level flag. Row is included in the matrix, tagged `[DEFERRED]`. Run
completes. Any DEFERRED row forces READINESS to CONDITIONAL regardless of other findings.
Deferred findings appear in priority summary with their own count.

| Halt ID        | Trigger condition                              | Tier     |
|----------------|------------------------------------------------|----------|
| G1             | `.craft/roles/` absent or unreadable           | BLOCKING |
| G4a-{role}     | Lens anchor not stated before first finding    | BLOCKING |
| G4b-{role}     | Finding not tied to a named artifact surface   | SCOPED   |
| G4c-{role}     | Severity `{value}` not in calibration contract | SCOPED   |
| G4d-{role}     | Recommendation missing location reference      | DEFERRED |
| G5             | Zero findings across all roles                 | BLOCKING |

Tier rationale: G4a (no lens) and G1 (no roles) invalidate the entire run or row — BLOCKING.
G4b (no surface) and G4c (bad severity) make the row structurally invalid but leave others useful
— SCOPED. G4d (missing location) is a completeness issue that doesn't invalidate the finding
itself — DEFERRED with conditional result.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: HALT [G1] per registry.

| Priority | Slot       | Role Name          | Basis                          |
|----------|------------|--------------------|--------------------------------|
| 1        | CHALLENGER | [ROLE_NAME]        | Inertia-advocate: always first |
| 2        | DOMAIN-1   | [ROLE_NAME]        | [reason]                       |
| 3+       | DOMAIN-2..N| [ROLE_NAME...]     | [reason]                       |
| N (last) | CHALLENGER | [ROLE_NAME]        | Bracket close: always last     |

---

### EXECUTION

**Gate 1 — Role registry load** [BLOCKING]

You are not ready to select reviewers until `.craft/roles/` is confirmed readable.

On failure:
```
HALT [G1] BLOCKING: .craft/roles/ absent or unreadable. Run cannot continue.
→ Fix and: /crew-check {{artifact}} --amend reload
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active." Required before any reviewer runs.

**Gate 3 — Challenger: opening bracket**

Inertia-advocate first. State what team does today without `{{artifact}}` and why acceptable.
>= 2 status-quo strengths. Emit: "Status quo registered."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing Challenger)

For each role:

*G4a — Lens anchor* [BLOCKING for this role]: State role lens before any finding.

On missing:
```
HALT [G4a-{role}] BLOCKING: Lens anchor not stated. Role excluded.
→ Row excluded from matrix. Fix and: /crew-check {{artifact}} --amend rerun:{role}
```

*G4b — Surface finding* [SCOPED]: Every finding must name a specific artifact surface.

On missing surface:
```
HALT [G4b-{role}] SCOPED: Finding lacks named artifact surface. Row excluded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4b-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
```
Exclude this role's rows. Continue to next role.

*G4c — Severity validation* [SCOPED]: All labels must be HIGH / MEDIUM / LOW.

On invalid:
```
HALT [G4c-{role}] SCOPED: Severity '{value}' not in contract. Row excluded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4c-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
```
Exclude this role's rows. Continue to next role.

*G4d — Recommendation completeness* [DEFERRED]: Every recommendation must include a location.

On missing location:
```
HALT [G4d-{role}] DEFERRED: Recommendation missing location. Row included with flag.
→ Row tagged [DEFERRED]. Run continues. Result will be CONDITIONAL.
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
```
Include row in matrix with `[DEFERRED]` tag.

**Gate 5 — Matrix assembly and severity sort**

Assemble staged rows (excluding SCOPED rows). Sort HIGH first. Within tier: Challenger before
domain. DEFERRED rows included; display their [DEFERRED] tag.

On zero rows after exclusions:
```
HALT [G5] BLOCKING: No valid rows remain after exclusions. Run cannot continue.
→ /crew-check {{artifact}} --amend depth:deep
```

If excluded rows exist, append below matrix:
```
EXCLUDED ROWS (SCOPED halts):
  [EXCLUDED: {role} — {halt-id}]: [brief trigger description]
  → /crew-check {{artifact}} --amend rerun:{role}
```

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:     [N] findings
  MEDIUM:   [N] findings
  LOW:      [N] findings
  DEFERRED: [N] findings (recommendation location missing — forces CONDITIONAL)
  EXCLUDED: [N] rows (SCOPED halts — rows omitted from matrix)
```

**Gate 7 — Readiness verdict**

Apply: any HIGH = BLOCKED. Any DEFERRED or MEDIUM (no HIGH) = CONDITIONAL. All LOW or none = READY.

Note: DEFERRED rows force CONDITIONAL regardless of their finding severity. A run with only LOW
findings but one DEFERRED row is CONDITIONAL, not READY.

`READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate last. Does status quo hold given domain findings (including any excluded rows)?
Note excluded rows by name. Revise readiness if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. >= 1 cross-role convergence or conflict. Reference roles by name. Note if
any excluded rows represent a gap in the synthesis. No new findings.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — re-run a specific role from G4a
- `reload` — re-load `.craft/roles/` and restart
- `halts` — list all gates that fired, separated by tier

HALT AUDIT format (`--amend halts`) — tier-separated:
```
HALT AUDIT — [N] total: [B] BLOCKING, [S] SCOPED, [D] DEFERRED

BLOCKING (must resolve before run can complete):
  none

SCOPED (rows excluded; run is otherwise complete):
  G4c-inertia-advocate | Severity 'CRITICAL' invalid
  → /crew-check {{artifact}} --amend rerun:inertia-advocate

DEFERRED (rows included with flag; forces CONDITIONAL):
  G4d-pm | Recommendation missing location
  → /crew-check {{artifact}} --amend rerun:pm
```
Each entry is paste-ready. Tier classification tells the user whether the issue stopped the run,
removed a row, or only conditioned the result.

---

## V-04

**Axis**: Skip-map + three-tier halts (axes 1 + 3 combined)
**Hypothesis**: V-01 R6 pre-commits sub-gate skip semantics as a named table. V-03 R6
pre-commits halt tier scope as a named registry. Combining them produces a per-tier skip-map:
BLOCKING halts (G4a, G1) require full-role or full-run restart — no sub-gates to skip.
SCOPED halts (G4b, G4c) exclude the row and require rerun from G4a (the whole role must
re-run for the row to be valid). DEFERRED halts (G4d) require only G4d rerun — the lens,
surface, and severity are already verified, so the skip-map applies fully. The claim:
per-tier re-entry semantics are more precise than a single skip-map because they encode
not just which sub-gates are safe to skip but whether skipping is possible at all for this
tier. A SCOPED halt means the row was thrown away — there is nothing to resume from.

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

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW permitted.

---

### PRE-EXECUTION: HALT REGISTRY WITH TIER AND RE-ENTRY

Each halt condition carries: trigger, tier (scope of effect), and re-entry semantics derived
from tier + SUB-GATE SKIP-MAP below.

| Halt ID        | Trigger                                        | Tier     | Re-entry semantics                              |
|----------------|------------------------------------------------|----------|-------------------------------------------------|
| G1             | `.craft/roles/` absent or unreadable           | BLOCKING | Full restart: `--amend reload`                  |
| G4a-{role}     | Lens anchor not stated before first finding    | BLOCKING | Full role restart: `--amend rerun:{role}`        |
| G4b-{role}     | Finding not tied to a named artifact surface   | SCOPED   | Row re-execution: `--amend rerun:{role}` (from G4a — row was discarded) |
| G4c-{role}     | Severity `{value}` not in calibration contract | SCOPED   | Row re-execution: `--amend rerun:{role}` (from G4a — row was discarded) |
| G4d-{role}     | Recommendation missing location reference      | DEFERRED | Sub-gate re-entry: `--amend rerun:G4d-{role}` (skip G4a–G4c per skip-map) |
| G5             | Zero findings across all roles                 | BLOCKING | Full restart: `--amend depth:deep`              |

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

The skip-map applies only to DEFERRED tier halts. SCOPED tier halts discard the row;
re-execution must start from G4a because prior sub-gate results no longer exist.

| Re-entry command           | Applies to tier | Resumes at | Skips               | Prerequisite                                    |
|----------------------------|-----------------|------------|---------------------|-------------------------------------------------|
| `--amend rerun:{role}`     | BLOCKING, SCOPED| G4a        | (nothing)           | Full role restart                               |
| `--amend rerun:G4d-{role}` | DEFERRED only   | G4d        | G4a, G4b, G4c       | Lens anchor + surface + severity verified in prior run |

SCOPED halts cannot use sub-gate precision because the row state was discarded at halt time.
DEFERRED halts can use sub-gate precision because the row was included with a flag — prior
sub-gate results are preserved in the output.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: HALT [G1] per registry.

| Priority | Slot       | Role Name          | Basis                          |
|----------|------------|--------------------|--------------------------------|
| 1        | CHALLENGER | [ROLE_NAME]        | Inertia-advocate: always first |
| 2        | DOMAIN-1   | [ROLE_NAME]        | [reason]                       |
| 3+       | DOMAIN-2..N| [ROLE_NAME...]     | [reason]                       |
| N (last) | CHALLENGER | [ROLE_NAME]        | Bracket close: always last     |

---

### EXECUTION

**Gate 1 — Role registry load** [BLOCKING]

On failure:
```
HALT [G1] BLOCKING: .craft/roles/ absent or unreadable. Run cannot continue.
→ To continue: /crew-check {{artifact}} --amend reload
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active." Required before any reviewer.

**Gate 3 — Challenger: opening bracket**

Inertia-advocate first. State status quo and why acceptable. >= 2 strengths.

**Gate 4 — Domain reviewer loop**

For each role in REVIEWER PRIORITY MANIFEST order (excluding closing Challenger):

*G4a — Lens anchor* [BLOCKING]:
State role lens before any finding: "From the [role] perspective, this review examines [surface]."

On missing:
```
HALT [G4a-{role}] BLOCKING: Lens anchor not stated.
→ To continue: /crew-check {{artifact}} --amend rerun:{role}
  (full role restart — no skip-map applies to BLOCKING tier)
```

*G4b — Surface finding* [SCOPED]:
Every finding must name a specific artifact surface.

On missing surface:
```
HALT [G4b-{role}] SCOPED: Finding lacks named surface. Row discarded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4b-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
  (full role restart from G4a — row state discarded, skip-map does not apply)
```

*G4c — Severity validation* [SCOPED]:
All labels must match calibration contract.

On invalid value:
```
HALT [G4c-{role}] SCOPED: Severity '{value}' not in contract. Row discarded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4c-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
  (full role restart from G4a — row state discarded, skip-map does not apply)
```

*G4d — Recommendation completeness* [DEFERRED]:
Every recommendation must include a location reference.

On missing location:
```
HALT [G4d-{role}] DEFERRED: Recommendation missing location. Row included with flag.
→ Row tagged [DEFERRED]. Run continues. Result will be CONDITIONAL.
→ To resolve: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (sub-gate re-entry per skip-map — G4a, G4b, G4c skipped; row state preserved)
```

**Gate 5 — Matrix assembly and sort**

Assemble staged rows (excluding SCOPED rows). Sort HIGH first. DEFERRED rows included with tag.
If excluded rows exist, append `EXCLUDED ROWS` list below matrix with re-entry commands.

On zero valid rows: HALT [G5] BLOCKING.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:     [N] findings
  MEDIUM:   [N] findings
  LOW:      [N] findings
  DEFERRED: [N] rows (location missing — CONDITIONAL)
  EXCLUDED: [N] rows (row-level failures)
```

**Gate 7 — Readiness verdict**

Any HIGH = BLOCKED. Any DEFERRED or MEDIUM (no HIGH) = CONDITIONAL. All LOW or none = READY.
`READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate last. Reflect on domain findings including any excluded rows. Revise if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. >= 1 cross-role convergence or conflict named. No new findings.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a (for BLOCKING or SCOPED halts)
- `rerun:G4d-{role}` — sub-gate re-entry at G4d (for DEFERRED halts only; skips G4a–G4c)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — tier-separated halt audit
- `halts:{gate-id}` — single halt entry with tier and re-entry semantics

HALT AUDIT format (`--amend halts`):
```
HALT AUDIT — [N] total: [B] BLOCKING, [S] SCOPED, [D] DEFERRED

BLOCKING:
  (none)

SCOPED (row discarded — restart from G4a):
  G4c-pm | Severity 'CRITICAL' invalid
  → /crew-check {{artifact}} --amend rerun:pm

DEFERRED (row flagged — sub-gate re-entry available):
  G4d-architect | Recommendation missing location
  → /crew-check {{artifact}} --amend rerun:G4d-architect
```
Tier column tells the user whether skip-map applies to the re-entry command.

---

## V-05

**Axis**: Full R6 integration — skip-map + health certificate + three-tier + tier-routed re-entry
**Hypothesis**: V-01 formalizes the skip-map as a preamble contract. V-02 structures clean-run
output as a RUN HEALTH CERTIFICATE. V-03 introduces three halt tiers. V-04 combines skip-map
with three tiers to produce per-tier re-entry semantics. V-05 integrates all four: the HALT
REGISTRY declares tier + re-entry semantics before execution; the SUB-GATE SKIP-MAP governs
per-tier minimum-restart behavior; the RUN HEALTH CONTRACT names the output section in both
directions (certificate on clean, numbered recovery on failure). The structural claim: when
all three pre-committed contracts are declared before any gate fires, the model holds a complete
map of failure space before encountering any failure — the combination eliminates the need
for any gate-level prose to explain halt behavior, skip behavior, or recovery behavior.
All three are derivable from the pre-execution preamble alone.

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

| Label  | Score | Operational meaning                        |
|--------|-------|--------------------------------------------|
| HIGH   | 3     | Blocks commit or ship decision             |
| MEDIUM | 2     | Conditions ship; must have resolution plan |
| LOW    | 1     | Advisory; proceed with awareness           |

Only HIGH / MEDIUM / LOW permitted.

---

### PRE-EXECUTION: HALT REGISTRY

Three tiers govern failure scope. Tier is part of every halt message.

| Halt ID        | Trigger                                        | Tier     |
|----------------|------------------------------------------------|----------|
| G1             | `.craft/roles/` absent or unreadable           | BLOCKING |
| G4a-{role}     | Lens anchor not stated before first finding    | BLOCKING |
| G4b-{role}     | Finding not tied to a named artifact surface   | SCOPED   |
| G4c-{role}     | Severity `{value}` not in calibration contract | SCOPED   |
| G4d-{role}     | Recommendation missing location reference      | DEFERRED |
| G5             | Zero findings across all roles                 | BLOCKING |

**BLOCKING**: Run-level full stop. No output past halt point. Must resolve before any output
is useful.

**SCOPED**: Row-level skip. Failing role's rows excluded from matrix; all other rows proceed.
Run completes with partial matrix.

**DEFERRED**: Finding-level flag. Row included with `[DEFERRED]` tag. Run completes.
Any DEFERRED row forces READINESS to CONDITIONAL.

---

### PRE-EXECUTION: SUB-GATE SKIP-MAP

Minimum-restart re-entry semantics per tier. SCOPED halts discard the row state — no skip
is safe because the row must be reconstructed from scratch. DEFERRED halts preserve the row
state — sub-gate re-entry is safe.

| Tier     | Re-entry command              | Resumes at | Skips               | Safety basis                                  |
|----------|-------------------------------|------------|---------------------|-----------------------------------------------|
| BLOCKING | `--amend rerun:{role}`        | G4a        | (nothing)           | Row or run state was not produced              |
| SCOPED   | `--amend rerun:{role}`        | G4a        | (nothing)           | Row state was discarded at halt time           |
| DEFERRED | `--amend rerun:G4d-{role}`    | G4d        | G4a, G4b, G4c       | Lens + surface + severity verified; row in output |

No SCOPED or BLOCKING halt may use sub-gate precision — prior row state was discarded or never
produced. Only DEFERRED halts earn sub-gate re-entry because their row is present in the output.

---

### PRE-EXECUTION: RUN HEALTH CONTRACT

After Gate 9, emit the RUN HEALTH section at a fixed position before AMEND.

**Clean run (zero halts across all tiers):**
```
RUN HEALTH: PASS
  Gates: G1 PASS, G2 PASS, G4a–G4d (all roles) PASS, G5 PASS
  Halts fired: 0
  Result: Matrix complete. Proceed to readiness verdict.
```

**Failed run (>= 1 halt of any tier):**
```
RUN HEALTH: [B] BLOCKING / [S] SCOPED / [D] DEFERRED
  Recovery (paste and execute — BLOCKING before SCOPED before DEFERRED):

  BLOCKING (must resolve first):
    1. [G4a-pm] Lens anchor not stated
       → /crew-check {{artifact}} --amend rerun:pm

  SCOPED (row excluded — row restart):
    2. [G4c-inertia-advocate] Severity 'BLOCKER' invalid
       → /crew-check {{artifact}} --amend rerun:inertia-advocate

  DEFERRED (row flagged — sub-gate re-entry available):
    3. [G4d-architect] Recommendation missing location
       → /crew-check {{artifact}} --amend rerun:G4d-architect

  After all fixes: /crew-check {{artifact}}
```

Tier ordering in the recovery block: BLOCKING items first (they prevent a complete run),
then SCOPED (they limit matrix coverage), then DEFERRED (they condition the verdict). The
user works top-to-bottom; completing the list and re-running will produce a clean run.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/`. If absent: HALT [G1] per HALT REGISTRY.

| Priority | Slot       | Role Name          | Basis                          |
|----------|------------|--------------------|--------------------------------|
| 1        | CHALLENGER | [ROLE_NAME]        | Inertia-advocate: always first |
| 2        | DOMAIN-1   | [ROLE_NAME]        | [reason]                       |
| 3+       | DOMAIN-2..N| [ROLE_NAME...]     | [reason]                       |
| N (last) | CHALLENGER | [ROLE_NAME]        | Bracket close: always last     |

`deep`: all roles. `standard`: relevant roles with selection rationale.

---

### EXECUTION

**Gate 1 — Role registry load** [BLOCKING]

You are not ready to select reviewers until `.craft/roles/` is readable and non-empty.

On failure:
```
HALT [G1] BLOCKING: .craft/roles/ absent or unreadable. Run cannot continue.
→ To continue: /crew-check {{artifact}} --amend reload
  (BLOCKING tier — no skip-map applies; full restart required)
```

**Gate 2 — Severity contract acknowledgment**

State: "Severity calibration contract active." Required before any reviewer runs.

**Gate 3 — Challenger: opening bracket**

Inertia-advocate first. State what team does today and why acceptable without `{{artifact}}`.
>= 2 status-quo strengths. Emit: "Status quo registered."

**Gate 4 — Domain reviewer loop** (REVIEWER PRIORITY MANIFEST order, excluding closing Challenger)

For each role:

*G4a — Lens anchor* [BLOCKING]: State role lens before any finding.

On missing:
```
HALT [G4a-{role}] BLOCKING: Lens anchor not stated.
→ To continue: /crew-check {{artifact}} --amend rerun:{role}
  (BLOCKING tier — full role restart; no sub-gate skip applies)
```

*G4b — Surface finding* [SCOPED]: Every finding must name a specific artifact surface.

On missing surface:
```
HALT [G4b-{role}] SCOPED: Finding lacks named artifact surface. Row discarded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4b-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
  (SCOPED tier — row state discarded; full role restart from G4a required)
```

*G4c — Severity validation* [SCOPED]: Labels must be HIGH / MEDIUM / LOW.

On invalid:
```
HALT [G4c-{role}] SCOPED: Severity '{value}' not in contract. Row discarded, run continues.
→ Row excluded: [EXCLUDED: {role} — G4c-{role}]
→ To resolve: /crew-check {{artifact}} --amend rerun:{role}
  (SCOPED tier — row state discarded; full role restart from G4a required)
```

*G4d — Recommendation completeness* [DEFERRED]: Recommendations must include a location reference.

On missing location:
```
HALT [G4d-{role}] DEFERRED: Recommendation missing location. Row included with flag.
→ Row tagged [DEFERRED]. Run continues. Result will be CONDITIONAL.
→ To resolve: /crew-check {{artifact}} --amend rerun:G4d-{role}
  (DEFERRED tier — row preserved in output; sub-gate re-entry skips G4a, G4b, G4c)
```

**Gate 5 — Matrix assembly and sort**

Assemble staged rows (excluding SCOPED rows). Sort HIGH first. DEFERRED rows included with tag.

If excluded rows exist:
```
EXCLUDED ROWS:
  [EXCLUDED: {role} — {halt-id}]: [brief trigger]
  → /crew-check {{artifact}} --amend rerun:{role}
```

On zero valid rows: HALT [G5] BLOCKING.

**Gate 6 — Priority summary**

```
PRIORITY SUMMARY:
  HIGH:     [N] findings
  MEDIUM:   [N] findings
  LOW:      [N] findings
  DEFERRED: [N] rows (forces CONDITIONAL)
  EXCLUDED: [N] rows (SCOPED halts)
```

**Gate 7 — Readiness verdict**

Any HIGH = BLOCKED. Any DEFERRED or MEDIUM (no HIGH) = CONDITIONAL. All LOW or none = READY.
`READINESS: READY | CONDITIONAL | BLOCKED`

**Gate 8 — Challenger: closing bracket**

Inertia-advocate last. Reflect on domain findings and any excluded rows. Revise if warranted.

**Gate 9 — Cross-role synthesis**

2-4 sentences. >= 1 cross-role convergence or conflict. Note excluded row gaps. No new findings.

**Gate 10 — RUN HEALTH section**

Emit the RUN HEALTH section per RUN HEALTH CONTRACT. This is the terminal named section
before AMEND. Certificate format on clean run. Tier-ordered numbered recovery procedure
on failure. Section always appears at this position.

---

### AMEND

```
/crew-check {{artifact}} --amend [operation]
```

Operations:
- `add:{role}` — add a specific reviewer
- `depth:deep` — re-run with all roles
- `rerun:{role}` — full role restart from G4a (BLOCKING or SCOPED tier)
- `rerun:G4d-{role}` — sub-gate re-entry at G4d (DEFERRED tier only; G4a–G4c skipped)
- `reload` — re-load `.craft/roles/` and restart
- `halts` — tier-separated halt audit (see RUN HEALTH section for equivalent)
- `halts:{gate-id}` — single halt entry with tier, trigger, and re-entry command

HALT AUDIT format (`--amend halts`) — mirrors RUN HEALTH failure format:
```
HALT AUDIT — [N] total: [B] BLOCKING, [S] SCOPED, [D] DEFERRED

BLOCKING (must resolve first — full restart):
  (none)

SCOPED (rows excluded — full role restart from G4a):
  G4c-inertia-advocate | Severity 'BLOCKER' invalid
  → /crew-check {{artifact}} --amend rerun:inertia-advocate

DEFERRED (rows flagged — sub-gate re-entry at G4d):
  G4d-architect | Recommendation missing location
  → /crew-check {{artifact}} --amend rerun:G4d-architect
```
Audit format is identical to the RUN HEALTH failure block, ensuring any path to recovery
(inline halt message, RUN HEALTH section, or `--amend halts` query) leads to the same
tier-ordered, paste-ready command list.
