## crew-check — Quest Score R9 (Rubric v8)

---

### Scoring Framework

**Base**: All variations carry R8 V-05 (128/128 under v7). New criteria in v8:

| ID | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----|------|------|------|------|------|
| C-28 | 2 | PASS | FAIL | FAIL | PASS | PASS |
| C-29 | 2 | FAIL | PASS | FAIL | PASS | PASS |
| C-30 | 2 | FAIL | FAIL | PASS | FAIL | PASS |

---

### Per-Variation Evidence

**V-01 (C-28 only)**

- **C-28 — PASS**: FINDING CONVERGENCE CONTRACT adds "Gate 9 obligation" column; SOLO row reads "MANDATORY disposition in SOLO FINDINGS table." Gate 9 emits the SOLO FINDINGS table (`ESCALATE / DISMISS:rationale / ROLE-SPECIFIC`), names omission a contract violation. Gate 2 acknowledgment includes SOLO disposition notice.
- **C-29 — FAIL**: No CONVERGENCE SNAPSHOT CONTRACT. Gate 5.5 emits the surface-level register from R8 V-05 only — no counts block, no early-abort HALT [G5.5], no waive path. Gate 5.5 accumulates but does not checkpoint.
- **C-30 — FAIL**: Clean RUN HEALTH has `Stage: {{stage}}` but scope summary is a one-liner (`YES-scope / ADVISORY / excluded: [N] / [N] / [N]`) that conflates NO and DEPRECATED. No SCOPE DISTRIBUTION table. Failed variant: no Stage field, no SCOPE DISTRIBUTION.

Score: 128 + 2 = **130/134**

---

**V-02 (C-29 only)**

- **C-28 — FAIL**: FINDING CONVERGENCE CONTRACT is a 4-column table (no "Gate 9 obligation" column). SOLO tier carries "Normal weight" — no mandatory disposition. Gate 9 emits only CONFIDENCE=LOW enumeration; no SOLO FINDINGS table.
- **C-29 — PASS**: PRE-EXECUTION CONVERGENCE SNAPSHOT CONTRACT declared. Gate 5.5 restructured: emits tier counts first (CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO), then surface table. HALT [G5.5] fires BLOCKING if CONFIRMED=0 AND CORROBORATED=0. `--amend waive:convergence` path defined. G5.5 added to HALT REGISTRY with "does not fire for DEPRECATED" note. Priority summary includes `Convergence snapshot:` counts line.
- **C-30 — FAIL**: Clean RUN HEALTH has `Stage: {{stage}}` and `G5.5 waived: NO` but scope remains as `YES-scope / ADVISORY / excluded: [N] / [N] / [N]` — no SCOPE DISTRIBUTION table, conflated NO+DEPRECATED. Failed variant: no Stage, no SCOPE DISTRIBUTION.

Score: 128 + 2 = **130/134**

---

**V-03 (C-30 only)**

- **C-28 — FAIL**: FINDING CONVERGENCE CONTRACT has no Gate 9 obligation column. Gates 0.5–8 delegated to V-01 via "[identical]" reference. Gate 9 is "[same as R8 V-05]" — no SOLO FINDINGS mandatory table.
- **C-29 — FAIL**: Gate 5.5 explicitly delegated: "Same as R8 V-05 Gate 5.5." No counts block, no early-abort, no CONVERGENCE SNAPSHOT CONTRACT.
- **C-30 — PASS**: PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT explicitly declared. Clean variant: `Stage: {{stage}}` field + full SCOPE DISTRIBUTION table (YES / ADVISORY / NO / DEPRECATED with counts and verdict contribution). Failed variant: `Stage: {{stage}}` field + SCOPE DISTRIBUTION table before recovery block. Both variants checked. NO and DEPRECATED are distinct rows, not conflated.

Score: 128 + 2 = **130/134**

---

**V-04 (C-28 + C-29)**

- **C-28 — PASS**: FINDING CONVERGENCE CONTRACT has Gate 9 obligation column; SOLO row = "MANDATORY disposition in SOLO FINDINGS table." Gate 9 emits SOLO FINDINGS table with IC-CHALLENGED column included (5 columns, not 4). Under waive path, SOLO FINDINGS table explicitly marked mandatory. Clean RUN HEALTH includes `SOLO disposed: [N] (ESCALATE: [N], DISMISS: [N], ROLE-SPECIFIC: [N])`.
- **C-29 — PASS**: CONVERGENCE SNAPSHOT CONTRACT declared. Gate 5.5 emits counts block then surface table. HALT [G5.5] BLOCKING with waive path. Waive path note explicitly names the C-28 dependency: "SOLO FINDINGS table (C-28 requirement) is mandatory under waive path." G5.5 in HALT REGISTRY. AMEND operations include `waive:convergence`.
- **C-30 — FAIL**: Clean RUN HEALTH has `Stage: {{stage}}` and `YES-scope / ADVISORY / excluded: [N] / [N] / [N]` — no SCOPE DISTRIBUTION table. Failed variant: no Stage, no SCOPE DISTRIBUTION. C-30 contract not declared.

Score: 128 + 4 = **132/134**

---

**V-05 (C-28 + C-29 + C-30)**

- **C-28 — PASS**: FINDING CONVERGENCE CONTRACT has Gate 9 obligation column. Gate 9 emits mandatory SOLO FINDINGS table with an 8-column schema: `Role | Surface | Severity | Confidence | IC-CHALLENGED | STAGE-APPROPRIATE | Finding summary | Disposition` — extending V-01/V-04's table with IC-CHALLENGED and STAGE-APPROPRIATE for full auditability. Disposition semantics restated inline. Waive path explicitly requires SOLO FINDINGS table. "No SOLO findings" exit if empty.
- **C-29 — PASS**: CONVERGENCE SNAPSHOT CONTRACT declared. Gate 5.5 emits CONVERGENCE SNAPSHOT counts block first, then CONVERGENCE REGISTER surface table with IC Impact column. HALT [G5.5] BLOCKING (CONFIRMED=0 AND CORROBORATED=0); waive path calls out "SOLO FINDINGS disposition at Gate 9" as the mandatory consequence. Gate 6 Priority summary includes `G5.5 waived: YES | NO`. HALT AUDIT example includes a [G5.5] entry. G5.5 DEPRECATED exemption noted.
- **C-30 — PASS**: PRE-EXECUTION: RUN HEALTH SCOPE DISTRIBUTION CONTRACT declared. Clean variant: `Stage: {{stage}}` + SCOPE DISTRIBUTION table (4 named rows). Failed variant: `Stage: {{stage}}` + SCOPE DISTRIBUTION table before recovery block — present in both. Gate 2 announces "RUN HEALTH will emit Stage and SCOPE DISTRIBUTION in both clean and failed variants." Result line: "All five contracts honored."

Score: 128 + 6 = **134/134**

---

### Rankings

| Variation | Score | Composite |
|-----------|-------|-----------|
| V-05 | 134/134 | 100.0% |
| V-04 | 132/134 | 98.5% |
| V-01 | 130/134 | 97.0% |
| V-02 | 130/134 | 97.0% |
| V-03 | 130/134 | 97.0% |

All 5 essential criteria inherited from R8 V-05 — PASS across all variations.

---

### Excellence Signals — V-05

**1. Waive path co-activates C-28 as a mutual enforcement contract**
V-04 introduced this pattern; V-05 solidifies it. The waive:convergence path is not a bypass — it substitutes Gate 9's cross-role convergence requirement with mandatory SOLO disposition. A run that cannot converge must explain every non-converging signal. The two criteria share a semantic seam: C-29 detects whether convergence exists; C-28 handles everything that didn't. Naming this relationship explicitly in the CONVERGENCE SNAPSHOT CONTRACT and in the waive path note makes the enforcement chain visible.

**2. SOLO FINDINGS table extended to 8-column schema including IC-CHALLENGED and STAGE-APPROPRIATE**
V-01 and V-04 emit SOLO FINDINGS with 5–6 columns. V-05 adds IC-CHALLENGED and STAGE-APPROPRIATE, making each SOLO disposition decision auditable against inertia impact and scope group. A SOLO finding tagged DISMISS is more defensible when the record shows it challenged no IC and fell in YES-scope; a SOLO finding tagged ESCALATE is more urgent when it is IC-CHALLENGED=IC-01 and STAGE-APPROPRIATE=YES.

**3. SCOPE DISTRIBUTION in the failed variant as standalone diagnostic**
V-03 established this for single-axis; V-05 carries it into the fully-integrated build. A reviewer debugging a multi-halt run can read the failed RUN HEALTH and see immediately what stage was declared and how findings distributed across YES/ADVISORY/NO/DEPRECATED — without re-executing or re-reading the transcript. The failed variant becomes a self-contained diagnostic artifact, not a pointer back to the run.

**4. Gate 2 unified contract acknowledgment enumerates all five active contracts by name**
V-05 Gate 2 names all active pre-execution contracts: "severity/confidence calibration, artifact maturity stage, finding convergence, convergence snapshot, inertia claim registry, RUN HEALTH scope distribution." No prior variation names all contracts in one acknowledgment. This creates an auditable "start of run" checkpoint that can be checked against the PRE-EXECUTION section headers, making omission detectable by inspection.

---

```json
{"top_score": 134, "all_essential_pass": true, "new_patterns": ["waive:convergence co-activates C-28 SOLO disposition as mutual enforcement — convergence abort and non-converging signal disposition share a semantic seam declared explicitly in the contract", "SOLO FINDINGS table extended to 8-column schema (adds IC-CHALLENGED + STAGE-APPROPRIATE) making each disposition decision auditable against inertia impact and scope group", "SCOPE DISTRIBUTION in failed RUN HEALTH variant enables scope debugging without transcript re-reading — failed cert is a standalone diagnostic artifact", "Gate 2 unified contract acknowledgment names all five active pre-execution contracts, creating an auditable start-of-run checkpoint detectable by inspection"]}
```
