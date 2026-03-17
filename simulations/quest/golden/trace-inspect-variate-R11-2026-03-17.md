---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 11
rubric: trace-inspect-rubric-v7
---

# trace-inspect -- Variations v7 R11 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R10 V-05 achieves 101.5/101.5 under rubric v7 -- all C-01 through C-25 PASS.
v7 rubric is closed. R11 explores three structural patterns as hypothetical v8 candidates:

From R10 V-05 excellence signals, two cross-reference patterns passed as C-24 and C-25:
the EG-FIRST EXECUTION CONSTRAINT block cites the Coverage Matrix Enforcement class column
(C-24), and the VC-4 G-1 attribution row counts Phase 2a/2b membership against declared
blocks (C-25). Both are *backward linkage* patterns: a downstream element cites an upstream
declaration. R11 explores whether a *forward linkage* pattern produces analogous structural
value -- upstream declarations that cite the downstream element they are validated by.

**R11 hypothetical patterns (potential C-26, C-27, C-28)**:

- **C-26 candidate (lifecycle emphasis)**: Verdict NEEDS-REDESIGN threshold check explicitly
  cites EG finding IDs from Step 3b by name. Currently, the Verdict states "EG gaps exceed 3"
  as a prose assertion; a scorer must re-read the findings table to count. A NEEDS-REDESIGN
  EVIDENCE ANCHOR block cites the EG finding IDs and derives the count from them. This creates
  a forward linkage from Step 3b EG entries to the Verdict classification -- parallel to C-25's
  backward linkage from Verdict to PHASE 2a/2b MEMBERSHIP declarations.

- **C-27 candidate (output format)**: SA-TO-SG PROMOTION adds a PROMOTION COMPLETENESS GATE
  table that verifies: (promoted to SG count) + (remaining as SA count) = (Stage 1 SA relay
  count). Currently the promotion summary records the two counts but does not validate they
  sum correctly. A self-validating arithmetic check makes silent omission detectable at the
  promotion block itself rather than discovered at Verdict.

- **C-28 candidate (phrasing register)**: Every named invariant receives a consistent
  `[enforcement: X]` suffix at each occurrence throughout the prompt body -- not just at
  Coverage Matrix column declaration and EG-FIRST block. Currently `[enforcement: architectural]`
  appears on GATE CLEARANCE SUMMARY and Phase 2a header, and `[enforcement: instructional]`
  on Schema 2 label lock and channel taxonomy -- but label lock at SA-TO-SG PROMOTION,
  G-1/G-2/G-3 at Step 3c, and channel field requirement at Phase 4 do not consistently carry
  the suffix. Uniform per-occurrence annotation makes enforcement class a machine-checkable
  property of every invariant site in the prompt.

**R11 variation axes**:

- **V-01 (single axis: lifecycle emphasis)**: NEEDS-REDESIGN EVIDENCE ANCHOR block in Verdict
  cites EG finding IDs from Step 3b by name and derives EG count from the list.

- **V-02 (single axis: output format)**: SA-TO-SG PROMOTION gains PROMOTION COMPLETENESS GATE
  table with arithmetic self-check; mismatch is a named structural finding.

- **V-03 (single axis: phrasing register)**: Every named invariant at every occurrence in
  every phase block carries a consistent `[enforcement: X]` suffix -- no invariant without
  its class annotation at the point of use.

- **V-04 (combined: C-26 + C-27 candidates)**: Verdict evidence anchor + promotion completeness
  gate.

- **V-05 (combined: C-26 + C-27 + C-28 candidates)**: All three -- full R11 target.

All five inherit the full R10 V-05 architecture (C-01 through C-25 PASS). What varies per
V-0N: only the structural element listed above and in the CRITERION INHERITANCE REGISTRY
version update.

---

## V-01 -- Single axis: Lifecycle emphasis (C-26 candidate: Verdict evidence anchoring)

**Axis**: Lifecycle emphasis -- the Verdict NEEDS-REDESIGN classification adds a NEEDS-REDESIGN
EVIDENCE ANCHOR block that explicitly names the EG finding IDs from Step 3b and derives the
EG count from the named list. Instead of asserting "EG gaps exceed 3" as a prose claim, the
block reads: "EG findings in Step 3b: [F-NN, F-MM, ...]. EG count: N. Threshold: 3. N > 3:
[YES/NO]. Structural role gap indicated: [YES/NO -- cite finding IDs if YES]. Classification
fires: [YES/NO]."

**Hypothesis**: The current Verdict NEEDS-REDESIGN check is a prose assertion that requires a
scorer to re-read Step 3b and count EG entries. A block that names the IDs makes the count
derivable from the block alone -- EG count = |{F-NN, F-MM, ...}|. This creates a forward
linkage: Step 3b populates EG findings; the Verdict cites them by ID; the count is structural,
not re-derived. Parallel to C-25's backward linkage (VC-4 G-1 attribution row cites PHASE 2a/2b
MEMBERSHIP counts), C-26 is a forward linkage (Verdict cites Step 3b EG findings). Risk: the
EVIDENCE ANCHOR block adds four lines to the Verdict. Mitigation: it replaces a prose assertion
with a structured derivation, net no information added -- only structure.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v7

This skill body is version 7. The following criteria were established in prior versions and
are explicitly inherited here. A version that does not name a criterion in this registry has
dropped it. Dropping a criterion is a structural act, not a silent omission.

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the findings table at verdict time; count is re-derived
     each time and not anchored to named finding IDs
  Result: traces that pass or fail based on executor judgment, not structural evidence.
  This skill replaces judgment with a 4-phase lifecycle that produces auditable evidence.

INHERITED FROM v1 -- ESSENTIAL CRITERIA:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED CRITERIA:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL CRITERIA:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL CRITERIA:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL CRITERIA:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL CRITERIA:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

INHERITED FROM v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): INHERITED -- enforced via EG-FIRST EXECUTION
    CONSTRAINT block and EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally BLOCKED
    until PASS; [enforcement: architectural] per Coverage Matrix Schema 4 column
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED -- C-17 table
    embedded directly in VC-4 G-1 cross-role row; filling ledger and attribution are one
    operation; structural drift between ledger and attribution is impossible

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED -- enforced via "Enforcement class" column
    in Coverage Matrix; every schema row annotated as [architectural] or [instructional];
    [enforcement: X] inline suffix on every named invariant in schema description paragraphs;
    per-invariant class readable from Coverage Matrix without scanning the prompt body
  C-23 (Phase 2a/2b role membership enumerated): INHERITED -- enforced via PHASE 2a MEMBERSHIP
    and PHASE 2b MEMBERSHIP named blocks in EG-FIRST EXECUTION CONSTRAINT; each block lists
    role names explicitly with role count; membership auditable from the constraint block
    independently of the Role-Schema Binding Summary; count validated in VC-4 G-1 attribution

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED -- the structural invariant
    in EG-FIRST EXECUTION CONSTRAINT explicitly states "[enforcement: architectural -- see
    Coverage Matrix Schema 4 column]"; the constraint block and the Coverage Matrix column
    are mutually referencing; enforcement class is auditable from either element
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED -- VC-4 G-1 attribution
    row verifies Phase 2a role count in attribution = N from PHASE 2a MEMBERSHIP block and
    Phase 2b role count = M from PHASE 2b MEMBERSHIP block; count mismatch = membership
    inconsistency detectable in the compliance ledger

NEW IN v7 -- ASPIRATIONAL CRITERION (R11 candidate):
  C-26 (NEEDS-REDESIGN evidence anchor): NEW -- enforced via NEEDS-REDESIGN EVIDENCE ANCHOR
    block in Verdict; block names EG finding IDs from Step 3b explicitly; EG count is derived
    from the named list, not asserted as prose; forward linkage from Step 3b EG findings to
    Verdict classification; threshold check is self-auditing from the block alone
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1;
not structurally blocked.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA is a violation detectable in VC-2; not structurally blocked.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3; not structurally blocked.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears. See EG-FIRST EXECUTION CONSTRAINT
for the architectural gate governing SA-TO-SG PROMOTION.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment; role names must appear here explicitly and
are auditable without cross-referencing the binding table.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary;
  count mismatch = missing or misassigned role)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is structurally
  invalid at that point. Evidence-grounded promotion is architecturally enforced, not
  merely recommended. The enforcement class [architectural] is declared in the Coverage
  Matrix Enforcement class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses.
Stage 1 forces a systematic read of all three source layers before execution begins.

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role. A Setup that lists roles without schema binding declarations
is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here. SA/SG-only roles
deferred to Phase 2b. SA-TO-SG PROMOTION is structurally BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (required structural checkpoint -- SA-TO-SG PROMOTION is BLOCKED
> until this checkpoint passes):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names + count N]
> - EG-producing roles with completed relays above: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** (all Phase 2a roles relayed) / **FAIL** (relay missing for: [role])
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite**: EG-RELAY COMPLETE PASS (confirmed above). Promotion decisions may cite
observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here** (declared in EG-FIRST EXECUTION CONSTRAINT block).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output -- trace may not advance to Step 3c
> until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. Re-run FLOOR CHECK after correction.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.
Schema 5 output: gate results all PASS (unblocks Step 3d).

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block
> before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED.
Schema 5 output: Schema 3 channel taxonomy active (unblocks Phase 4).

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural
> block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; C-23 MEMBERSHIP counts validate attribution completeness | **G-1 SOURCE ATTRIBUTION TABLE** (this cell is not complete until the sub-table is filled): Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; after filling, verify: PHASE 2a role count in attribution = N from PHASE 2a MEMBERSHIP block; PHASE 2b role count = M from PHASE 2b MEMBERSHIP block; count mismatch = C-23 membership inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES (any P1 SA remaining) / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires above.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires above.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (C-27 candidate: Promotion completeness gate)

**Axis**: Output format -- SA-TO-SG PROMOTION block gains a PROMOTION COMPLETENESS GATE
table that validates: (SG from promotion count) + (SA remaining count) = (Stage 1 SA relay
count). The table has three columns: "Stage 1 SA count (from relay)", "Promoted to SG",
"Remaining as SA", and a fourth "Completeness check" column with the arithmetic verdict
(YES = sums match / MISMATCH = silent omission detected). A mismatch is a named structural
finding that must be resolved before Phase 2b begins.

**Hypothesis**: R10 V-05 records "SA remaining" and "SG from promotion" as separate counts
in the promotion summary but does not validate they sum to the original Stage 1 SA count.
A silent omission -- an SA gap that was neither promoted nor retained -- cannot be detected
from the current summary. The COMPLETENESS GATE makes such omissions immediately visible:
if promoted + remaining ≠ Stage 1 SA count, a gap was dropped. This creates a forward
linkage from Stage 1 relay (SA count declared there) to the promotion block (completeness
verified here). Risk: the arithmetic check adds one table to the promotion block. Mitigation:
the table reuses the three values already in the promotion summary; no new information is
required, only structure.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v7

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Silently drops SA gaps during promotion with no arithmetic check to detect the omission
  Result: traces that pass or fail based on executor judgment, not structural evidence.
  This skill replaces judgment with a 4-phase lifecycle that produces auditable evidence.

INHERITED FROM v1 -- ESSENTIAL CRITERIA:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED CRITERIA:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL CRITERIA:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL CRITERIA:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL CRITERIA:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL CRITERIA:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

INHERITED FROM v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): INHERITED
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED
  C-23 (Phase 2a/2b role membership enumerated): INHERITED

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

NEW IN v7 -- ASPIRATIONAL CRITERION (R11 candidate):
  C-27 (SA-TO-SG PROMOTION completeness gate): NEW -- enforced via PROMOTION COMPLETENESS
    GATE table in the SA-TO-SG PROMOTION block; table verifies promoted + remaining =
    Stage 1 SA relay count; arithmetic self-check; mismatch is a named structural finding
    requiring resolution before Phase 2b begins; silent gap omission is detectable from the
    promotion block without re-reading Stage 1
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1;
not structurally blocked.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA is a violation detectable in VC-2; not structurally blocked.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3; not structurally blocked.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears. See EG-FIRST EXECUTION CONSTRAINT
for the architectural gate governing SA-TO-SG PROMOTION.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment and is auditable without cross-referencing
the binding table.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary;
  count mismatch = missing or misassigned role)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is structurally
  invalid at that point. Evidence-grounded promotion is architecturally enforced, not
  merely recommended. The enforcement class [architectural] is declared in the Coverage
  Matrix Enforcement class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses.
Stage 1 forces a systematic read of all three source layers before execution begins.

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role. A Setup that lists roles without schema binding declarations
is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here. SA/SG-only roles
deferred to Phase 2b. SA-TO-SG PROMOTION is structurally BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (required structural checkpoint -- SA-TO-SG PROMOTION is BLOCKED
> until this checkpoint passes):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names + count N]
> - EG-producing roles with completed relays above: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** (all Phase 2a roles relayed) / **FAIL** (relay missing for: [role])
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite**: EG-RELAY COMPLETE PASS (confirmed above). Promotion decisions may cite
observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

> **PROMOTION COMPLETENESS GATE** (C-27: arithmetic self-check -- resolve MISMATCH before
> Phase 2b begins):
>
> | Stage 1 SA count (from relay) | Promoted to SG | Remaining as SA | Completeness check |
> |-------------------------------|----------------|-----------------|-------------------|
> | [count from [SA: ...] relay]  | [count]        | [count]         | promoted + remaining = Stage 1 SA count: YES / MISMATCH |
>
> If MISMATCH: one or more SA gaps were silently dropped. Identify the missing gap, classify
> it as PROMOTES TO SG-NN or REMAINS SA, and re-run the gate. Phase 2b is BLOCKED until
> the gate shows YES.

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here** (declared in EG-FIRST EXECUTION CONSTRAINT block).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output):
>
> - Finding IDs counted: [list all IDs explicitly]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block
> before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all PASS: "C-12 EXEMPTION APPLIES:
> all gates passed on first evaluation. No remediation loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED.
Schema 5 output: Schema 3 channel taxonomy active (unblocks Phase 4).

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural
> block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited; PROMOTION COMPLETENESS GATE YES | [list SA gaps promoted; confirm SG downstream; confirm gate YES] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; C-23 MEMBERSHIP counts validate attribution completeness | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; verify PHASE 2a/2b role counts against MEMBERSHIP blocks] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---
## V-03 -- Single axis: Phrasing register (C-28 candidate: Uniform per-occurrence enforcement annotation)

**Axis**: Phrasing register -- every named invariant at every phase of the prompt body carries
a consistent `[enforcement: architectural]` or `[enforcement: instructional]` suffix at the
point of use, not only at Coverage Matrix declaration and the EG-FIRST EXECUTION CONSTRAINT
block. Additions vs R10 V-05: G-1, G-2, G-3 invariant lines at Step 3c each gain their
suffix; the STEP 3b FLOOR CHECK gains `[enforcement: architectural]`; every Schema 5
prerequisite line at sub-step entry gains `[enforcement: architectural]`; the PHASE 2b
header gains `[enforcement: architectural]`; the EG-RELAY COMPLETE checkpoint gains its
suffix; the channel field requirement at Amend entries gains `[enforcement: instructional]`.

**Hypothesis**: R10 V-05 annotates enforcement class at the Coverage Matrix column (per
schema, once) and the EG-FIRST EXECUTION CONSTRAINT structural invariant (once). The suffix
also appears on GATE CLEARANCE SUMMARY, Phase 2a header, Schema 2 label lock, Schema 2
compliance field in relays, and Step 3d channel taxonomy. Missing from R10 V-05: the
individual G-1/G-2/G-3 lines at Step 3c, the FLOOR CHECK structural requirement, each
Schema 5 prerequisite verification line, the Phase 2b membership enforcement, and the
Amend channel field requirement. Uniform annotation makes the enforcement class of every
invariant machine-checkable at point of use: grep for `[enforcement:` returns the complete
inventory. Risk: eight to ten short annotations added. Mitigation: each is a parenthetical
suffix on an existing line; no new structure required.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v7

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine enforcement class at point of use; must return to Coverage Matrix
  Result: traces that pass or fail based on executor judgment, not structural evidence.
  This skill replaces judgment with a 4-phase lifecycle that produces auditable evidence.

INHERITED FROM v1 -- ESSENTIAL CRITERIA:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED CRITERIA:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL CRITERIA:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL CRITERIA:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL CRITERIA:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL CRITERIA:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

INHERITED FROM v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): INHERITED
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED
  C-23 (Phase 2a/2b role membership enumerated): INHERITED

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

NEW IN v7 -- ASPIRATIONAL CRITERION (R11 candidate):
  C-28 (Uniform per-occurrence enforcement annotation): NEW -- every named invariant at
    every occurrence in every phase block carries [enforcement: X]; G-1/G-2/G-3 individual
    lines at Step 3c, STEP 3b FLOOR CHECK, Schema 5 prerequisite lines, Phase 2b membership
    enforcement, EG-RELAY COMPLETE, and channel field at Amend entries all annotated;
    grep for [enforcement: produces the complete invariant inventory; no invariant site
    without its enforcement class at the point of use
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1;
not structurally blocked.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA is a violation detectable in VC-2; not structurally blocked.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3; not structurally blocked.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears. See EG-FIRST EXECUTION CONSTRAINT
for the architectural gate governing SA-TO-SG PROMOTION.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment and is auditable without cross-referencing
the binding table.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary;
  count mismatch = missing or misassigned role)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is structurally
  invalid at that point. Evidence-grounded promotion is architecturally enforced, not
  merely recommended. The enforcement class [architectural] is declared in the Coverage
  Matrix Enforcement class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses.
A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role. A Setup that lists roles without schema binding declarations
is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE** `[enforcement: architectural]`: Only PHASE 2a MEMBERSHIP
roles run here. SA/SG-only roles deferred to Phase 2b. SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** `[enforcement: architectural]` (required structural checkpoint --
> SA-TO-SG PROMOTION is BLOCKED until this checkpoint passes):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names + count N]
> - EG-producing roles with completed relays above: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS / FAIL**
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite** `[enforcement: architectural]`: EG-RELAY COMPLETE PASS (confirmed above).
Promotion decisions may cite observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2; not structurally blocked.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here** `[enforcement: architectural]` (declared in
EG-FIRST EXECUTION CONSTRAINT block; deviation is a membership violation detectable in VC-4).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite `[enforcement: architectural]`: Schema 1 declared in Coverage Matrix
(satisfied above). Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite `[enforcement: architectural]`: Step 3a complete (severity legend
defined above). Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** `[enforcement: architectural]` (required structural output --
> trace may not advance to Step 3c until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. Re-run FLOOR CHECK after correction.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite `[enforcement: architectural]`: Step 3b FLOOR CHECK PASS.
Schema 5 output: gate results all PASS (unblocks Step 3d).

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block
> before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED. Schema 5 output: Schema 3 channel taxonomy active (unblocks Phase 4).

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`; omission detectable
in VC-3 but not structurally blocked.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural
> block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality] `[enforcement: instructional]`
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] `[enforcement: instructional]`
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; C-23 MEMBERSHIP counts validate attribution completeness | **G-1 SOURCE ATTRIBUTION TABLE** (this cell is not complete until the sub-table is filled): Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; after filling, verify: PHASE 2a role count in attribution = N from PHASE 2a MEMBERSHIP block; PHASE 2b role count = M from PHASE 2b MEMBERSHIP block; count mismatch = C-23 membership block inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-26 + C-27 candidates (Verdict evidence anchor + Promotion completeness gate)

**Axis**: Lifecycle emphasis + output format. V-01's NEEDS-REDESIGN EVIDENCE ANCHOR block
combined with V-02's PROMOTION COMPLETENESS GATE table. No new element beyond V-01 and V-02.

**Hypothesis**: V-01 creates a forward linkage from Step 3b EG findings to the Verdict.
V-02 creates a forward linkage from Stage 1 SA relay to the SA-TO-SG PROMOTION block.
Together they give the prompt two self-auditing arithmetic paths: one at the promotion
boundary (Stage 1 SA count verified at promotion), one at the verdict boundary (Step 3b EG
list verified at classification). A scorer audits both from structural blocks without
re-reading source phases. V-04 tests whether the two patterns interact or conflict.
Expected: no conflict; combined score = V-01 + V-02 pts.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v7

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading findings table; silently drops SA gaps at promotion
  Result: traces that pass or fail based on executor judgment, not structural evidence.

INHERITED FROM v1..v7 -- all criteria C-01 through C-25: INHERITED (see V-01 registry for
  full list; abbreviated here for single-page legibility)

NEW IN v7 -- ASPIRATIONAL CRITERIA (R11 candidates):
  C-26 (NEEDS-REDESIGN evidence anchor): NEW -- NEEDS-REDESIGN EVIDENCE ANCHOR block in
    Verdict; EG finding IDs from Step 3b cited explicitly; EG count derived from the named
    list; threshold check self-auditing from the block; forward linkage Step 3b -> Verdict
  C-27 (SA-TO-SG PROMOTION completeness gate): NEW -- PROMOTION COMPLETENESS GATE table;
    arithmetic self-check: promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b;
    forward linkage Stage 1 SA relay -> promotion block
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b + FLOOR CHECK, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | instructional: channel field required; omissions detectable in VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY gates Step 3d; PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural: prerequisites gate each sub-step; transition sentences confirm completion |

**Schema 1** `[enforcement: instructional]`: {P1,P2,P3}. **Schema 2** `[enforcement: instructional]`:
{SA,SG,EG,QO}; label lock invariant `[enforcement: instructional]`. **Schema 3** `[enforcement:
instructional]`: channel field in every Amend entry. **Schema 4** `[enforcement: architectural]`:
GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement. **Schema 5**
`[enforcement: architectural]`: prerequisites and transition sentences gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | All gates PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

```
PHASE 2a MEMBERSHIP (EG-class roles):
  - [Role A] (EG-class) -- PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles):
  - [Role C] (SA/SG-class) -- PHASE 2b role count: [M]

Total roles: [N + M]

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE passes.
  The enforcement class [architectural] is declared in the Coverage Matrix Enforcement
  class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without Stage 1, a developer reads the spec once and guesses.
A valid Stage 1 reads only `{{skill_spec_path}}`.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Relay received: [SA], [SG], [EG], [layer diversity].

#### Phase 1 -- Setup

Confirmed input bindings: [topic], [scope_in], [scope_out], [roles], [spec_version].

Per-role schema binding:
```
[role: {{role_name}}]
  Schema 1 binding: [...] Schema 2 binding: [...]
  SA/SG gaps: [...] EG gaps expected: [...]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG original].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE** `[enforcement: architectural]`: PHASE 2a MEMBERSHIP roles only.
SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE.

**Role relay -- [EG-producing role]**:
- Received from: [...] | Received values: [...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels: [...] -- all from {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: [...] | Produced: [...] | EG gaps: [...]

> **EG-RELAY COMPLETE** (SA-TO-SG PROMOTION BLOCKED until PASS):
> PHASE 2a MEMBERSHIP declared: [list + count N] -- relays complete: YES/NO
> **EG-RELAY COMPLETE result: PASS / FAIL**

---

#### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: Gap: [...] -- Promotion: PROMOTES TO SG-NN / REMAINS SA -- Reason: [...]
```

> **PROMOTION COMPLETENESS GATE** (C-27: resolve MISMATCH before Phase 2b):
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |------------------|----------------|-----------------|-------------------|
> | [from relay]     | [count]        | [count]         | promoted + remaining = Stage 1 SA: YES / MISMATCH |
>
> MISMATCH: identify dropped gap, classify, re-run. Phase 2b BLOCKED.

Label lock `[enforcement: instructional]`: promoted gaps use SG; SA retention detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution

**PHASE 2b MEMBERSHIP roles only** (from EG-FIRST EXECUTION CONSTRAINT).

**Role relay -- [SA/SG-only role]**:
- Schema 2 compliance `[enforcement: instructional]`: Source labels: [...] -- YES/NO
- SA/SG gaps: [...] | Produced: [...] | EG gaps: [none]

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections: [list with WRITTEN status]

---

#### Phase 3 -- Findings

##### Step 3a

Schema 5 prerequisite: Schema 1 declared.

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log |

Schema 5 transition: Step 3a complete. Step 3b valid.

##### Step 3b

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (trace may not advance to Step 3c until PASS):
> Finding IDs: [...] | Row count: N (>= 3 required) | Source types: [...] (>= 2 required)
> Action-uniqueness: NO (PASS) / YES (FAIL) -- **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

##### Step 3c

Schema 5 prerequisite: FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: >=2 distinct Source types. Source types: [...] -- G-1: PASS/FAIL
**G-2** `[enforcement: architectural]`: No identical same-Source Actions. Pairs: [...] -- G-2: PASS/FAIL
**G-3** `[enforcement: architectural]`: All {P1,P2,P3}. Labels: [...] -- G-3: PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: [P/F] | G-2: [P/F] | G-3: [P/F] -- ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** (if any FAIL; else: "C-12 EXEMPTION APPLIES.")

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

##### Step 3d

Schema 5 prerequisite `[enforcement: architectural]`: ALL GATES CLEARED.
Channel taxonomy active `[enforcement: instructional]`: Amend entries include channel field.
Schema 5 transition: channel taxonomy active. Phase 4 valid.

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1/G-2/G-3: PASS -- ALL GATES CLEARED.

Amend entries (change): [finding], [source], [channel], [section changed], [change], [source confirmed].
Amend entries (dismissal): [finding], [reason], [channel], [source type confirmed].

---

### Verdict (Phase 5 -- Compliance Ledger)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS | [labels; FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All P1/P2/P3 | [severity values] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO used | [labels used] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | SG label; lock holds; EG-RELAY cited; PROMOTION GATE YES | [promotions; gate result] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; SG for promoted | [labels; lock confirmed] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 PASS/FAIL | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after gate summary PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 | G-1 verified; MEMBERSHIP counts validate | **G-1 SOURCE ATTRIBUTION TABLE**: Source / Phase / Role(s) / Finding IDs -- [one row per Source type; verify Phase 2a/2b counts vs MEMBERSHIP blocks] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3b after 3a | [evidence 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | 3c after FLOOR CHECK | [FLOOR CHECK cited] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | 3d after gate summary | [gate summary cited] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 after channel active | [channel + Phase 4 gate] | PASS/FAIL |

**VC-1..5 overall**: PASS / FAIL each

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION: P1 SA remaining: [count, IDs if >0] -- Fires: YES/NO
>
> NEEDS-REDESIGN: EG findings in Step 3b: [list IDs] -- EG count: [N] -- N > 3: YES/NO
> Structural role gap: YES (cite IDs) / NO -- Fires: YES (both) / NO
>
> USEFUL: fires when neither check fires.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [rule that fired; cite IDs from EVIDENCE ANCHOR]
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined: C-26 + C-27 + C-28 candidates (Full R11 target)

**Axis**: Lifecycle emphasis + output format + phrasing register. All three R11 single-axis
patterns combined: V-01's NEEDS-REDESIGN EVIDENCE ANCHOR, V-02's PROMOTION COMPLETENESS
GATE, and V-03's uniform per-occurrence `[enforcement: X]` annotation. Updated CRITERION
INHERITANCE REGISTRY lists all three as NEW in v7.

**Hypothesis**: V-04 achieves C-26 and C-27 with independent structural additions at two
lifecycle boundaries. V-05 adds V-03's annotation discipline (C-28), which propagates the
enforcement class to every invariant at every point of use -- including the two new blocks:
PROMOTION COMPLETENESS GATE is annotated `[enforcement: instructional]` (a MISMATCH is
a named finding, not a structural impossibility) and NEEDS-REDESIGN EVIDENCE ANCHOR is also
`[enforcement: instructional]` (the classification is required; the block makes it auditable
but does not mechanically enforce it). The uniform annotation in V-05 makes the enforcement
classes of C-26 and C-27 explicit at their point of use, creating a consistent annotation
surface across all R11 additions. A scorer checking C-28 can grep for `[enforcement:` and
find C-26 and C-27 blocks among the annotated inventory.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v7

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine enforcement class at point of use; must return to Coverage Matrix;
     enforcement class annotations are inconsistent across the prompt body
  7. Counts EG findings by re-reading findings table; silently drops SA gaps at promotion
     with no arithmetic check; neither omission is detectable without re-reading
  Result: traces that pass or fail based on executor judgment, not structural evidence.
  This skill replaces judgment with a 4-phase lifecycle that produces auditable evidence.

INHERITED FROM v1 -- ESSENTIAL CRITERIA:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED CRITERIA:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL CRITERIA:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL CRITERIA:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL CRITERIA:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL CRITERIA:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

INHERITED FROM v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): INHERITED -- EG-FIRST EXECUTION CONSTRAINT +
    EG-RELAY COMPLETE gate [enforcement: architectural]; SA-TO-SG PROMOTION BLOCKED until PASS
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED -- Coverage Matrix column; [enforcement: X]
    on every named invariant in schema descriptions
  C-23 (Phase 2a/2b role membership enumerated): INHERITED -- PHASE 2a/2b MEMBERSHIP blocks
    in EG-FIRST EXECUTION CONSTRAINT; count validated in VC-4 G-1

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED -- structural invariant states
    [enforcement: architectural -- see Coverage Matrix Schema 4 column]; mutual reference
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED -- VC-4 G-1 attribution
    row verifies Phase 2a/2b role counts against MEMBERSHIP blocks

NEW IN v7 -- ASPIRATIONAL CRITERIA (R11 candidates):
  C-26 (NEEDS-REDESIGN evidence anchor): NEW -- NEEDS-REDESIGN EVIDENCE ANCHOR block in
    Verdict [enforcement: instructional]; EG finding IDs from Step 3b cited; EG count derived
    from list; threshold check self-auditing; forward linkage Step 3b -> Verdict
  C-27 (SA-TO-SG PROMOTION completeness gate): NEW -- PROMOTION COMPLETENESS GATE table
    [enforcement: instructional]; promoted + remaining = Stage 1 SA count arithmetic check;
    MISMATCH blocks Phase 2b; forward linkage Stage 1 SA relay -> promotion block
  C-28 (Uniform per-occurrence enforcement annotation): NEW -- every named invariant at every
    occurrence carries [enforcement: X]; G-1/G-2/G-3 individual lines, STEP 3b FLOOR CHECK,
    Schema 5 prerequisite lines, Phase 2b membership, EG-RELAY COMPLETE, channel field at
    Amend, PROMOTION COMPLETENESS GATE, NEEDS-REDESIGN EVIDENCE ANCHOR all annotated;
    grep for [enforcement: returns the complete invariant inventory
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1;
not structurally blocked.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA is a violation detectable in VC-2; not structurally blocked.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3; not structurally blocked.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears. See EG-FIRST EXECUTION CONSTRAINT
for the architectural gate governing SA-TO-SG PROMOTION.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment; role names must appear here explicitly and
are auditable without cross-referencing the binding table.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary;
  count mismatch = missing or misassigned role)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is structurally
  invalid at that point. Evidence-grounded promotion is architecturally enforced, not
  merely recommended. The enforcement class [architectural] is declared in the Coverage
  Matrix Enforcement class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses.
Stage 1 forces a systematic read of all three source layers before execution begins.

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role. A Setup that lists roles without schema binding declarations
is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE** `[enforcement: architectural]`: Only PHASE 2a MEMBERSHIP
roles run here. SA/SG-only roles deferred to Phase 2b. SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** `[enforcement: architectural]` (required structural checkpoint --
> SA-TO-SG PROMOTION is BLOCKED until this checkpoint passes):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names + count N]
> - EG-producing roles with completed relays above: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS / FAIL**
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite** `[enforcement: architectural]`: EG-RELAY COMPLETE PASS (confirmed above).
Promotion decisions may cite observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

> **PROMOTION COMPLETENESS GATE** `[enforcement: instructional]` (C-27: arithmetic self-check
> -- mismatch is a named finding; resolve before Phase 2b begins):
>
> | Stage 1 SA count (from relay) | Promoted to SG | Remaining as SA | Completeness check |
> |-------------------------------|----------------|-----------------|-------------------|
> | [count from [SA: ...] relay]  | [count]        | [count]         | promoted + remaining = Stage 1 SA count: YES / MISMATCH |
>
> If MISMATCH: identify the dropped SA gap, classify it, re-run. Phase 2b blocked by
> this finding until gate shows YES.

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2; not structurally blocked.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here** `[enforcement: architectural]` (declared in
EG-FIRST EXECUTION CONSTRAINT block; deviation detectable in VC-4).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite `[enforcement: architectural]`: Schema 1 declared in Coverage Matrix
(satisfied above). Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite `[enforcement: architectural]`: Step 3a complete (severity legend
defined above). Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** `[enforcement: architectural]` (required structural output --
> trace may not advance to Step 3c until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. Re-run FLOOR CHECK after correction.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite `[enforcement: architectural]`: Step 3b FLOOR CHECK PASS.
Schema 5 output: gate results all PASS (unblocks Step 3d).

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block
> before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED. Schema 5 output: Schema 3 channel taxonomy active (unblocks Phase 4).

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`; omission detectable
in VC-3 but not structurally blocked.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural
> block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality] `[enforcement: instructional]`
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] `[enforcement: instructional]`
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited; PROMOTION COMPLETENESS GATE YES | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited; confirm gate YES] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; C-23 MEMBERSHIP counts validate attribution completeness | **G-1 SOURCE ATTRIBUTION TABLE** (this cell is not complete until the sub-table is filled): Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; after filling, verify: PHASE 2a role count in attribution = N from PHASE 2a MEMBERSHIP block; PHASE 2b role count = M from PHASE 2b MEMBERSHIP block; count mismatch = C-23 membership block inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** `[enforcement: instructional]` (C-26: derives verdict
> from named finding IDs; makes threshold check self-auditing; not a structural gate):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES (any P1 SA remaining) / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires above.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires above.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
