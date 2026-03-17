---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 14
rubric: trace-inspect-rubric-v10
---

# trace-inspect -- Variations R14 v10 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R13 V-05 achieves 103.5/103.5 under rubric v9 -- all C-01 through C-29 PASS.
Rubric v10 adds C-30 and C-31 (0.5 pts each; grand total 104.5). Baseline = 103.5/104.5.

**R13 V-05 carries**:
- C-26 (NEEDS-REDESIGN EVIDENCE ANCHOR): Phase 5 enumerates EG finding IDs from Step 3b;
  EG count derived from the named list.
- C-27 (PROMOTION COMPLETENESS GATE): arithmetic closure in SA-TO-SG PROMOTION;
  promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b.
- C-28 (VERDICT-TO-TABLE TRACEABILITY): per-ID resolution sub-table inside EVIDENCE ANCHOR;
  each cited EG finding ID resolved to its Step 3b row (Finding excerpt | Source | Severity).
- C-29 (PROMOTION COUNT FORWARD-REFERENCE): VERDICT EVIDENCE SUMMARY block in Phase 5
  co-locates EG count (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS
  GATE); both classification inputs present at verdict time without re-reading prior phases.
- COUNT COMPLETENESS CHECK (count-equality variant): Step 3b EG row count = EVIDENCE ANCHOR
  list length; K=N confirms sub-table is complete. NOTE: this count-check detects omission
  (fewer cited IDs than Step 3b EG rows) but NOT substitution (wrong IDs that number correctly).

**R13 excellence signals that became C-30 and C-31**:
- V-03 in R13 (COUNT RECONCILIATION CHECK) establishes that count-equality is insufficient:
  a scorer can confirm K=N while F-07 in the EVIDENCE ANCHOR corresponds to no actual Step 3b
  row -- IDs that number correctly but do not match real row labels. C-30 requires per-ID key
  existence verification: each cited ID cross-checked against Step 3b row labels individually.
- V-05 in R13 introduced ONE bidirectional annotation on the PROMOTION COMPLETENESS GATE
  ("SA remaining certified: R -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY").
  C-31 expands this pattern to ALL forward-referencing blocks: EVIDENCE ANCHOR annotates its
  EG IDs as resolved in the TRACEABILITY sub-table; the TRACEABILITY sub-table annotates its
  source as Step 3b; the VERDICT EVIDENCE SUMMARY back-references both source blocks. Every
  forward-reference and back-reference is explicit, making C-26 through C-29 self-certifying.

**R14 variation axes**:

- **V-01 (single axis: lifecycle emphasis)**: Upgrade the COUNT COMPLETENESS CHECK from
  count-equality to per-ID membership verification. The EVIDENCE ANCHOR block gains a
  PER-ID MEMBERSHIP VERIFICATION table: one row per cited EG ID; each row states whether
  that ID exists as an actual Step 3b row label. Classification BLOCKED if any ID has
  NO. Scorer confirms C-30 from the membership table alone; count equality is insufficient.

- **V-02 (single axis: output format)**: EXPANDED BIDIRECTIONAL ANNOTATION. All four
  forward-referencing blocks in the trace carry explicit inline annotations: the EVIDENCE
  ANCHOR marks its EG ID list as "resolved in VERDICT-TO-TABLE TRACEABILITY sub-table";
  the TRACEABILITY sub-table header marks its source as "sourced from Step 3b findings
  table"; the VERDICT EVIDENCE SUMMARY rows carry back-reference annotations to their
  source blocks. Combined with the existing PROMOTION COMPLETENESS GATE annotation
  (inherited from C-29), all cross-block references are bidirectional.

- **V-03 (single axis: phrasing register -- alternative C-30 mechanism)**: Inline
  membership check within the EVIDENCE ANCHOR EG findings list. Instead of a separate
  PER-ID MEMBERSHIP VERIFICATION table, each cited EG ID in the NEEDS-REDESIGN check
  list is formatted as `[F-NN] (Step 3b row label: confirmed / NOT FOUND)`. If any ID
  has NOT FOUND, classification is BLOCKED inline. Tests whether inline per-ID notation
  satisfies C-30 without a dedicated membership table block.

- **V-04 (combined: C-30 + C-31)**: V-01 PER-ID MEMBERSHIP VERIFICATION table PLUS
  V-02 expanded bidirectional annotations. Both criteria targeted in one prompt.

- **V-05 (full integration: C-30 + C-31 + expanded inertia)**: V-04 combined axes plus
  inertia block extended with items 11 and 12 naming the ID-substitution attack vector
  (C-30) and the missing back-reference coherence pattern (C-31).

All five inherit the full R13 V-05 architecture (C-01 through C-29 PASS). What varies per
V-0N: only the structural element listed above and in the CRITERION INHERITANCE REGISTRY
version update.

---

## V-01 -- Single axis: Lifecycle emphasis (C-30 target: Per-ID membership verification)

**Axis**: Lifecycle emphasis -- the NEEDS-REDESIGN EVIDENCE ANCHOR block in Phase 5 replaces
the count-equality COUNT COMPLETENESS CHECK with a PER-ID MEMBERSHIP VERIFICATION table. For
each EG finding ID cited in the EVIDENCE ANCHOR list, a membership row confirms whether that
ID exists as an actual Step 3b row label (YES / NOT FOUND). Classification is BLOCKED if any
cited ID has NOT FOUND. A scorer reading this block can confirm per-ID membership without
re-reading Step 3b; the membership table is the verification record.

**Hypothesis**: R13 V-05's count-equality check (K=N) detects ID omission but not ID
substitution. A model citing F-07 when Step 3b has F-02 passes the count check if K=N. The
PER-ID MEMBERSHIP VERIFICATION table closes this: each ID is individually looked up against
Step 3b row labels. F-07 has no row label in Step 3b, so its membership row reads NOT FOUND
and classification is BLOCKED. Risk: one table row per cited EG ID; adds N rows. Mitigation:
the table is a lookup record, not new content -- each row is a single YES/NOT FOUND assertion.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v10

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     a model writing "F-07" when Step 3b has no F-07 row produces a structurally invalid
     verdict that passes a count-equality check undetected
  9. Omits EG findings from the verdict citation that inconveniently complicate the verdict
     narrative; cherry-picks IDs that fit the classification; count validated against Step 3b
     but individual keys never confirmed as actual row labels
  10. Reads the verdict without SA remaining count; must retrieve it from Stage 2 separately;
      verdict and promotion data are disconnected with no structural link
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
  C-19 (EG-first structural role ordering): INHERITED -- EG-FIRST EXECUTION CONSTRAINT
    block + EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally BLOCKED until PASS;
    [enforcement: architectural] per Coverage Matrix Schema 4 column
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED -- C-17 table
    embedded in VC-4 G-1 cross-role row

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED -- "Enforcement class" column in Coverage
    Matrix; [enforcement: X] inline suffix on every named invariant
  C-23 (Phase 2a/2b role membership enumerated): INHERITED -- PHASE 2a/2b MEMBERSHIP named
    blocks in EG-FIRST EXECUTION CONSTRAINT; role names and counts auditable from the block

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED -- EG-FIRST EXECUTION
    CONSTRAINT states "[enforcement: architectural -- see Coverage Matrix Schema 4 column]"
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED -- VC-4 G-1 attribution
    row verifies Phase 2a/2b role counts match MEMBERSHIP block declarations

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- EVIDENCE ANCHOR enumerates EG IDs;
    count derived from named list; forward linkage Step 3b -> Verdict
  C-27 (Promotion completeness gate): INHERITED -- arithmetic closure in SA-TO-SG PROMOTION;
    promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b

INHERITED FROM v9 -- ASPIRATIONAL CRITERIA:
  C-28 (Verdict-to-table traceability): INHERITED -- VERDICT-TO-TABLE TRACEABILITY sub-table
    in EVIDENCE ANCHOR; each cited EG finding ID resolved to its Step 3b row (Finding excerpt
    | Source | Severity); traceability auditable from sub-table alone
  C-29 (Promotion count forward-reference): INHERITED -- VERDICT EVIDENCE SUMMARY block in
    Phase 5; EG count (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS
    GATE) co-located; both classification inputs present at verdict time without re-read of
    prior phases; PROMOTION COMPLETENESS GATE annotates SA remaining as forward-referenced

NEW IN v10 -- ASPIRATIONAL CRITERION (R14 candidate):
  C-30 (Count completeness check): NEW -- enforced via PER-ID MEMBERSHIP VERIFICATION table
    inside NEEDS-REDESIGN EVIDENCE ANCHOR; each cited EG finding ID individually looked up
    against Step 3b row labels; each row states [ID | Step 3b row label exists: YES / NOT
    FOUND]; classification BLOCKED if any ID has NOT FOUND; count-equality alone does not
    satisfy this criterion (substitution attack: wrong IDs that number correctly pass K=N
    but fail per-ID lookup)
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only.
P1 blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA after promotion is a violation detectable in VC-2.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Phase 1 -- Setup: Role-Schema Binding Summary

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

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  EG-class roles run first. SA/SG-class roles run after promotion.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete -- layer diversity is required for G-1 to pass.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here. SA-TO-SG PROMOTION
is structurally BLOCKED `[enforcement: architectural]` until EG-RELAY COMPLETE passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (SA-TO-SG PROMOTION is BLOCKED until this PASSES):
>
> - PHASE 2a MEMBERSHIP declared: [list role names + count N]
> - EG-producing roles with completed relays: [list]
> - All PHASE 2a roles relayed: YES / NO
> - **EG-RELAY COMPLETE result: PASS / FAIL**
> - If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

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

> **PROMOTION COMPLETENESS GATE** (arithmetic closure -- validates no gap was silently dropped):
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N from Stage 1] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining certified: R** -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY.
> If MISMATCH: Phase 2b is structurally BLOCKED. Reconcile the missing gap before continuing.

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2.

---

### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here.**

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

### Phase 3 -- Findings

Phase 3 is valid if and only if sub-steps run in the order declared by Schema 5.

#### Step 3a -- Severity Legend Declaration

Prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

#### Step 3b -- Findings Table

Prerequisite: Step 3a complete (severity legend defined above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (trace may not advance to Step 3c until PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
> - **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

#### Step 3c -- Enforcement Gates

Prerequisite: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list] -- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action.
- Same-Source pairs examined: [list or "no same-Source pairs"] -- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list] -- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required before Step 3d):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation:
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added or text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

#### Step 3d -- Channel Taxonomy Activation

Prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must include
`[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`] | [source: `{{source}}`] | [remediation channel: spec/invocation/artifact/quality]
- [section or field changed: ] | [change: ] | [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`] | [reason: ] | [remediation channel: spec/invocation/artifact/quality]
- [source type confirmed: YES / NO]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; PROMOTION COMPLETENESS GATE PASS | [list SA gaps promoted; confirm SG downstream; confirm gate PASS] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; MEMBERSHIP counts validate attribution | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; verify Phase 2a count = N from MEMBERSHIP block; Phase 2b count = M; mismatch = membership inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | Step 3b valid only after 3a complete | [confirm 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to its Step 3b row):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> Traceability check: each ID in the EG findings list above appears as a distinct row in this
> table with matching Source=EG. If any cited ID has no corresponding row here, the EVIDENCE
> ANCHOR contains a non-existent finding reference -- verdict is structurally invalid.
>
> **PER-ID MEMBERSHIP VERIFICATION** (C-30: each cited ID cross-checked against Step 3b row labels):
>
> | Cited ID | Step 3b row label exists | Membership result |
> |----------|--------------------------|------------------|
> | [F-NN] | YES / NOT FOUND | CONFIRMED / BLOCKED |
> | [F-MM] | YES / NOT FOUND | CONFIRMED / BLOCKED |
>
> Membership check: every cited ID above must have a confirmed row label in Step 3b.
> If any ID has NOT FOUND: the EVIDENCE ANCHOR cites a non-existent finding key.
> Classification is BLOCKED until all cited IDs resolve to actual Step 3b row labels.
> COUNT COMPLETENESS CHECK PASS: all [N] cited IDs confirmed as actual Step 3b row keys.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived (EG: named list; SA: arithmetic closure).
> No re-read of prior phases required to verify the classification inputs.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (C-31 target: Expanded bidirectional annotation)

**Axis**: Output format -- all forward-referencing blocks in the trace carry explicit inline
bidirectional annotations. The EVIDENCE ANCHOR block annotates its EG finding IDs list as
"resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below". The TRACEABILITY sub-table header
annotates its source as "sourced from Step 3b findings table". The VERDICT EVIDENCE SUMMARY
rows carry back-reference annotations: EG count row annotates its source as the EVIDENCE
ANCHOR; SA remaining row annotates its source as the PROMOTION COMPLETENESS GATE. Combined
with the existing PROMOTION COMPLETENESS GATE annotation (C-29 inherited), all four
forward-referencing blocks now have both a forward and backward annotation.

**Hypothesis**: R13 V-05's single annotation on the PROMOTION COMPLETENESS GATE ("SA remaining
certified: R -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY") established the
bidirectional pattern. C-31 extends it: a reviewer can confirm any criterion (C-26 through
C-29) from the annotation alone without re-tracing the document. The EVIDENCE ANCHOR states
where its EG IDs are resolved; the TRACEABILITY sub-table states where its content comes from;
the VERDICT EVIDENCE SUMMARY back-references both its sources. Each block is self-certifying.
Risk: four annotation lines added across Phase 5. Mitigation: annotations are one-line
suffixes, not new content -- they add no computation, only navigation metadata.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v10

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     IDs may be fabricated or mis-remembered with no structural check
  9. Omits EG findings from the verdict citation that inconveniently complicate the verdict
     narrative; cherry-picks IDs; count validated but individual keys not confirmed
  10. Reads verdict without SA remaining count; must retrieve it from Stage 2 separately;
      verdict and promotion data are disconnected
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED
  C-27 (Promotion completeness gate): INHERITED

INHERITED FROM v9 -- ASPIRATIONAL CRITERIA:
  C-28 (Verdict-to-table traceability): INHERITED
  C-29 (Promotion count forward-reference): INHERITED -- PROMOTION COMPLETENESS GATE
    annotates SA remaining as forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY;
    single bidirectional annotation established in R13 V-02/V-05

NEW IN v10 -- ASPIRATIONAL CRITERION (R14 candidate):
  C-31 (Expanded bidirectional annotation): NEW -- bidirectional annotation extended to all
    forward-referencing blocks: EVIDENCE ANCHOR annotates EG IDs as "resolved in
    VERDICT-TO-TABLE TRACEABILITY sub-table below"; TRACEABILITY sub-table header annotates
    its source as "sourced from Step 3b findings table"; VERDICT EVIDENCE SUMMARY EG count
    row annotates its source as "NEEDS-REDESIGN EVIDENCE ANCHOR list above"; VERDICT EVIDENCE
    SUMMARY SA remaining row annotates its source as "PROMOTION COMPLETENESS GATE (Stage 2)";
    all four forward-referencing blocks now self-certifying without document re-trace
```

---

[Coverage Matrix, Phase 1, EG-FIRST EXECUTION CONSTRAINT, Stage 1, Phase 2a, Phase 2b,
Phase 3, and Phase 4 are structurally identical to V-01. Reproduce in full when running.]

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 -- all schemas and enforcement classes identical.]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3}.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO}. Label lock enforced.
**Schema 3** `[enforcement: instructional]`: channel field in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: gate advancement structurally blocked.
**Schema 5** `[enforcement: architectural]`: named prerequisites gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

### Phase 1 -- Setup: Role-Schema Binding Summary

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA], [SG original].

#### EG-FIRST EXECUTION CONSTRAINT

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class)
  PHASE 2b role count: [M]

Total roles: [N + M]
Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
```

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

### Phase 2a -- EG-First Execution

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`.

**Role relay -- [EG-producing role]**:
- Received from: | Received values: | Schema 2 compliance `[enforcement: instructional]`: [list] -- {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: | Produced: | EG gaps: [list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a declared: [N] | relayed: [N] | **PASS / FAIL**

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA | Reason: [one sentence]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining certified: R** -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY.
> If MISMATCH: Phase 2b BLOCKED. Reconcile before continuing.

Label lock `[enforcement: instructional]`: promoted gaps must use SG label downstream.

### Phase 2b -- SA/SG-Only Role Execution

**Role relay -- [SA/SG role]**: Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections written: [list each required section -- WRITTEN]

### Phase 3 -- Findings

#### Step 3a -- Severity Legend

| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

#### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [list all IDs] | count >= 3: Y/N |
> distinct Source types >= 2: Y/N | Action uniqueness: Y/N | **FLOOR CHECK: PASS/FAIL**

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: Source types: [list] -- PASS/FAIL
**G-2** `[enforcement: architectural]`: Same-Source pairs: [list or "none"] -- PASS/FAIL
**G-3** `[enforcement: architectural]`: Severity labels: [list] -- PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation")

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active `[enforcement: instructional]`. Phase 4 valid to begin.

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS | G-2: PASS | G-3: PASS -- Phase 4 valid to begin.

[Amend entries: finding / source / remediation channel / change or dismissal / source confirmed]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

[Compliance ledger VC-1 through VC-5 identical to V-01 -- reproduce in full when running.]

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | P1/P2/P3 + FLOOR CHECK PASS | [labels; FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | P1/P2/P3 in Amend | [severity values] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted=SG; GATE PASS | [promoted gaps; SG confirmed; gate] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in every entry | [channels listed] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 -- C-21 | G-1; MEMBERSHIP counts | **G-1 SOURCE ATTRIBUTION TABLE**: Source/Phase/Role(s)/Finding IDs | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy | [activation + PHASE 4 gate] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs;
> C-31: EG finding IDs below resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b (resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below):
>   [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row;
> C-31 back-reference: sourced from Step 3b findings table above):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> COUNT COMPLETENESS CHECK: Step 3b EG rows: [K] | sub-table rows: [N] | K = N: COMPLETE / INCOMPLETE
>
> Traceability confirmed: each cited ID resolves to a Step 3b row AND K = N.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5;
> C-31 back-references: EG count sourced from EVIDENCE ANCHOR above; SA remaining sourced
> from PROMOTION COMPLETENESS GATE, Stage 2):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count (forward-referenced from EVIDENCE ANCHOR above) | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining (forward-referenced from PROMOTION COMPLETENESS GATE) | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived (EG: named list; SA: arithmetic closure).
> All four forward-referencing cross-block links now bidirectional (C-31 PASS):
>   PROMOTION COMPLETENESS GATE -> VERDICT EVIDENCE SUMMARY (and back)
>   EVIDENCE ANCHOR -> VERDICT-TO-TABLE TRACEABILITY sub-table (and back)

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Phrasing register (C-30 alternative: inline per-ID membership notation)

**Axis**: Phrasing register -- instead of a separate PER-ID MEMBERSHIP VERIFICATION table
block, the membership check is embedded inline within the EVIDENCE ANCHOR EG findings list
itself. Each cited EG finding ID is formatted as `[F-NN] (Step 3b row label: confirmed)` or
`[F-NN] (Step 3b row label: NOT FOUND -- BLOCKED)`. If any ID has NOT FOUND, the line emits
a classification BLOCKED signal inline. No separate block is required; per-ID verification
is co-located with the citation at the point of use.

**Hypothesis**: C-28's VERDICT-TO-TABLE TRACEABILITY sub-table resolves each ID to its row
content (Finding excerpt, Source, Severity). C-30 requires confirming each ID exists as a
row KEY -- membership, not content. The inline notation makes this confirmation at citation
time rather than in a downstream verification block. Risk: inline notation is less auditable
than a dedicated table -- a scorer must read each line rather than scan a structured block.
Mitigation: the notation is explicit per-ID (NOT just a count assertion), so the per-ID
membership requirement of C-30 is satisfied. This variation tests whether inline phrasing
satisfies C-30 or whether a dedicated table block is required for auditability.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v10

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     IDs may be fabricated or mis-remembered with no structural check
  9. Omits EG findings from the verdict citation that inconveniently complicate the verdict;
     cherry-picks IDs; count may match but individual keys not confirmed as actual row labels
  10. Reads verdict without SA remaining count; must retrieve it from Stage 2 separately
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED
  C-27 (Promotion completeness gate): INHERITED

INHERITED FROM v9 -- ASPIRATIONAL CRITERIA:
  C-28 (Verdict-to-table traceability): INHERITED
  C-29 (Promotion count forward-reference): INHERITED

NEW IN v10 -- ASPIRATIONAL CRITERION (R14 candidate -- inline mechanism for C-30):
  C-30 (Count completeness check -- inline variant): CANDIDATE -- per-ID membership
    verification embedded inline within EVIDENCE ANCHOR EG findings list; each cited ID
    formatted as "[F-NN] (Step 3b row label: confirmed)" or "[F-NN] (Step 3b row label:
    NOT FOUND -- BLOCKED)"; classification BLOCKED inline if any ID has NOT FOUND; tests
    whether inline phrasing satisfies C-30 without a dedicated membership table block
```

---

[Coverage Matrix, Phase 1, Stage 1, Phase 2, Phase 3, Phase 4 identical to V-01.]

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 -- reproduce in full when running.]

| Schema | Content | Enforcement class |
|--------|---------|-------------------|
| Schema 1 -- Severity Vocabulary | P1/P2/P3 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA/SG/EG/QO | instructional |
| Schema 3 -- Channel Taxonomy | spec/invocation/artifact/quality | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a->3b->3c->3d | architectural |

[Schema descriptions and sub-step prerequisite table: same as V-01.]

### Phase 1 -- Setup

[Same structure as V-01: confirmed bindings, per-role schema binding blocks, EG-FIRST
EXECUTION CONSTRAINT with PHASE 2a/2b MEMBERSHIP declarations.]

### Stage 1 -- Source-Layer Audit

[Same as V-01.]

### Phase 2a -- EG-First Execution / EG-RELAY COMPLETE / SA-TO-SG PROMOTION with PROMOTION
COMPLETENESS GATE / Phase 2b

[Same as V-01 through end of Phase 2b including PROMOTION COMPLETENESS GATE with annotation:
"SA remaining certified: R -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY."]

### Phase 3 -- Findings (Steps 3a, 3b, 3c, 3d)

[Same as V-01.]

### Phase 4 -- Amend

[Same as V-01.]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid.

[Compliance ledger VC-1 through VC-5 identical to V-01.]

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b (per-ID membership verification inline -- C-30 candidate):
>   - [F-NN] (Step 3b row label: confirmed)
>   - [F-MM] (Step 3b row label: confirmed)
>   - [F-PP] (Step 3b row label: confirmed)
>   [If any ID has "NOT FOUND": classification BLOCKED -- that ID is not an actual Step 3b
>   row label; reconcile the EVIDENCE ANCHOR before proceeding.]
> - EG count (derived from confirmed list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> COUNT COMPLETENESS CHECK: Step 3b EG rows: [K] | cited IDs above (all confirmed): [N]
> K = N: COMPLETE / K != N: INCOMPLETE -- classification BLOCKED until reconciled.
>
> Traceability confirmed: each cited ID resolves to a Step 3b row AND K = N.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived. No re-read of prior phases required.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: Lifecycle emphasis + Output format (C-30 + C-31 targets)

**Axis**: V-01's PER-ID MEMBERSHIP VERIFICATION table (per-ID key existence lookup, C-30)
PLUS V-02's EXPANDED BIDIRECTIONAL ANNOTATION on all forward-referencing blocks (C-31). Both
criteria targeted in one prompt. No prior criterion degraded.

**Hypothesis**: C-30 and C-31 operate on distinct structural elements. C-30 adds a membership
lookup table inside the EVIDENCE ANCHOR block; C-31 adds inline annotations to four cross-block
references. They can coexist: the EVIDENCE ANCHOR block already has the TRACEABILITY sub-table
(C-28) and will gain the PER-ID MEMBERSHIP VERIFICATION table (C-30); the bidirectional
annotations (C-31) are one-line suffixes on existing block headers and rows. Together, Phase 5
becomes fully self-certifying: every fact cited in the verdict is individually verified (C-30)
and every cross-block reference is navigable in both directions (C-31). No re-read of any prior
phase is required to confirm C-26 through C-30.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v10

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     IDs may be fabricated or mis-remembered with no structural check
  9. Omits EG findings from the verdict citation; cherry-picks IDs; count may match but
     individual keys never confirmed as actual Step 3b row labels (substitution undetected)
  10. Reads verdict without SA remaining count; must retrieve from Stage 2 separately;
      forward-references are one-directional; blocks are not self-certifying
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED -- EG-FIRST
          EXECUTION CONSTRAINT + EG-RELAY COMPLETE gate; [enforcement: architectural]
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- EVIDENCE ANCHOR enumerates EG IDs;
    count derived from named list; forward linkage Step 3b -> Verdict
  C-27 (Promotion completeness gate): INHERITED -- arithmetic closure in SA-TO-SG PROMOTION;
    MISMATCH blocks Phase 2b

INHERITED FROM v9 -- ASPIRATIONAL CRITERIA:
  C-28 (Verdict-to-table traceability): INHERITED -- VERDICT-TO-TABLE TRACEABILITY sub-table;
    each cited EG ID resolved to Step 3b row (Finding excerpt | Source | Severity)
  C-29 (Promotion count forward-reference): INHERITED -- VERDICT EVIDENCE SUMMARY co-locates
    EG count + SA remaining; PROMOTION COMPLETENESS GATE annotated as forward-referenced

NEW IN v10 -- ASPIRATIONAL CRITERIA (R14 targets -- both):
  C-30 (Count completeness check): NEW -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID looked up against Step 3b row labels; each
    row: [ID | Step 3b row label exists: YES / NOT FOUND | result: CONFIRMED / BLOCKED];
    classification BLOCKED if any ID NOT FOUND; closes substitution attack vector
  C-31 (Expanded bidirectional annotation): NEW -- bidirectional annotations on all four
    forward-referencing blocks: EVIDENCE ANCHOR annotates EG IDs as "resolved in
    VERDICT-TO-TABLE TRACEABILITY sub-table below"; TRACEABILITY sub-table header annotates
    its source as "sourced from Step 3b findings table"; VERDICT EVIDENCE SUMMARY rows carry
    back-references to EVIDENCE ANCHOR and PROMOTION COMPLETENESS GATE; combined with the
    existing PROMOTION COMPLETENESS GATE -> VERDICT EVIDENCE SUMMARY annotation (C-29),
    all four forward-referencing blocks are now self-certifying
```

---

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 -- all schemas and enforcement classes identical. Reproduce in full when running.]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3}.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO}. Label lock enforced.
**Schema 3** `[enforcement: instructional]`: channel field in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: gate advancement structurally blocked.
**Schema 5** `[enforcement: architectural]`: named prerequisites gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

### Phase 1 -- Setup: Role-Schema Binding Summary

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA], [SG original].

#### EG-FIRST EXECUTION CONSTRAINT

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only)
  PHASE 2b role count: [M]

Total roles: [N + M]
Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
```

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

### Phase 2a -- EG-First Execution

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`.

**Role relay -- [EG-producing role]**:
- Received from: | Received values: | Schema 2 compliance `[enforcement: instructional]`: [list] -- {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: | Produced: | EG gaps: [list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a declared: [N] | relayed: [N] | **PASS / FAIL**

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA | Reason: [one sentence]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining certified: R** -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY.
> If MISMATCH: Phase 2b BLOCKED. Reconcile before continuing.

Label lock `[enforcement: instructional]`: promoted gaps must use SG label downstream.

### Phase 2b -- SA/SG-Only Role Execution

**Role relay -- [SA/SG role]**: Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections written: [list each required section -- WRITTEN]

### Phase 3 -- Findings

#### Step 3a -- Severity Legend

| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

#### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [list all IDs] | count >= 3: Y/N |
> distinct Source types >= 2: Y/N | Action uniqueness: Y/N | **FLOOR CHECK: PASS/FAIL**

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: Source types: [list] -- PASS/FAIL
**G-2** `[enforcement: architectural]`: Same-Source pairs: [list or "none"] -- PASS/FAIL
**G-3** `[enforcement: architectural]`: Severity labels: [list] -- PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL -- ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation")

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active `[enforcement: instructional]`. Phase 4 valid to begin.

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS | G-2: PASS | G-3: PASS -- Phase 4 valid to begin.

[Amend entries: finding / source / remediation channel / change or dismissal / source confirmed]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | P1/P2/P3 + FLOOR CHECK PASS | [labels; FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | P1/P2/P3 in all Amend entries | [severity values] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted=SG; GATE PASS | [promoted gaps; SG confirmed; gate] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in every entry | [channels listed] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 -- C-21 | G-1; MEMBERSHIP counts | **G-1 SOURCE ATTRIBUTION TABLE**: Source/Phase/Role(s)/Finding IDs [per Source type; verify Phase 2a count = N; Phase 2b count = M] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy | [activation + PHASE 4 gate] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs;
> C-31: EG finding IDs below resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b (resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below):
>   [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row;
> C-31 back-reference: sourced from Step 3b findings table above):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> **PER-ID MEMBERSHIP VERIFICATION** (C-30: each cited ID cross-checked against Step 3b row labels):
>
> | Cited ID | Step 3b row label exists | Membership result |
> |----------|--------------------------|------------------|
> | [F-NN] | YES / NOT FOUND | CONFIRMED / BLOCKED |
> | [F-MM] | YES / NOT FOUND | CONFIRMED / BLOCKED |
>
> Membership check: all [N] cited IDs must show YES. If any ID has NOT FOUND: the EVIDENCE
> ANCHOR cites a non-existent finding key. Classification BLOCKED until reconciled.
> COUNT COMPLETENESS CHECK PASS: all [N] cited IDs confirmed as actual Step 3b row keys.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5;
> C-31 back-references: EG count sourced from EVIDENCE ANCHOR above; SA remaining sourced
> from PROMOTION COMPLETENESS GATE, Stage 2):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count (forward-referenced from EVIDENCE ANCHOR above) | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining (forward-referenced from PROMOTION COMPLETENESS GATE) | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived (EG: named list; SA: arithmetic closure).
> All four forward-referencing cross-block links now bidirectional (C-31 PASS):
>   PROMOTION COMPLETENESS GATE -> VERDICT EVIDENCE SUMMARY (and back)
>   EVIDENCE ANCHOR -> VERDICT-TO-TABLE TRACEABILITY sub-table (and back)

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Full integration: C-30 + C-31 + expanded inertia framing

**Axis**: V-04 combined axes (C-30 PER-ID MEMBERSHIP VERIFICATION + C-31 expanded bidirectional
annotation) plus inertia framing extended with items 11 and 12 naming both new failure modes
explicitly. Item 11 names the ID-substitution attack vector that C-30 closes: a developer can
write correct-looking IDs that pass count-equality but reference no actual Step 3b row label.
Item 12 names the forward-reference coherence gap that C-31 closes: a developer reviewing
the verdict must manually trace the document to confirm where each structural value originated,
because no block declares its source or its consumers.

**Hypothesis**: V-04 produces structural completeness for C-30 and C-31. The inertia extension
makes the failure modes these criteria address visible as explicit behaviors the skill corrects.
A developer reading the registry understands not only what the skill produces (the inheritance
chain) but what specific judgment failures it replaces (the inertia items). Items 11 and 12
sharpen this: ID substitution is a distinct class of error from cherry-picking (item 9), and
forward-reference opacity is a distinct class of error from verdict disconnection (item 10).
Risk: registry length increases to 12 items. Mitigation: each item names a precise failure
mode; the registry is not a list of vague complaints but a specification of what judgment
each structural element replaces.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v10

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     IDs may be fabricated or mis-remembered with no structural check
  9. Omits EG findings from the verdict citation that inconveniently complicate the verdict
     narrative; cherry-picks IDs that fit the classification; a count-equality check may
     pass while a subset of EG findings is silently excluded
  10. Reads the verdict without SA remaining count; must retrieve it from Stage 2 separately;
      verdict and promotion data are in different sections with no structural link
  11. Cites EG finding IDs by key without verifying each key exists as an actual Step 3b row
      label; count-equality passes when IDs number correctly but reference wrong rows (e.g.,
      F-07 cited when Step 3b contains F-02 and F-04 -- counts match but IDs are wrong); the
      substitution is structurally undetectable without per-ID key lookup
  12. Forward-references from verdict blocks to source blocks are one-directional at best;
      a reviewer reading the VERDICT EVIDENCE SUMMARY cannot confirm where SA remaining was
      sourced without manually scanning the document; blocks carry no annotations declaring
      what they forward-reference or what references them; the evidence picture is connected
      only by convention, not by structural annotation
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED -- EG-FIRST
          EXECUTION CONSTRAINT + EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally
          BLOCKED until PASS; [enforcement: architectural] per Coverage Matrix Schema 4 column
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED -- C-17 table
          embedded in VC-4 G-1 cross-role row
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED -- "Enforcement class"
          column in Coverage Matrix; [enforcement: X] inline suffix on every named invariant
          C-23 (Phase 2a/2b role membership enumerated): INHERITED -- PHASE 2a/2b MEMBERSHIP
          named blocks in EG-FIRST EXECUTION CONSTRAINT; counts auditable from the block
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED --
          "[enforcement: architectural -- see Coverage Matrix Schema 4 column]"
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED -- VC-4 G-1
          attribution row verifies Phase 2a/2b role counts match MEMBERSHIP block declarations

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- EVIDENCE ANCHOR enumerates EG IDs;
    count derived from named list; forward linkage Step 3b -> Verdict
  C-27 (Promotion completeness gate): INHERITED -- arithmetic closure in SA-TO-SG PROMOTION;
    promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b

INHERITED FROM v9 -- ASPIRATIONAL CRITERIA:
  C-28 (Verdict-to-table traceability): INHERITED -- VERDICT-TO-TABLE TRACEABILITY sub-table
    in EVIDENCE ANCHOR; each cited EG finding ID resolved to its Step 3b row (Finding excerpt
    | Source | Severity); traceability auditable from sub-table alone without re-reading Step 3b
  C-29 (Promotion count forward-reference): INHERITED -- VERDICT EVIDENCE SUMMARY block in
    Phase 5; EG count (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS
    GATE) co-located; PROMOTION COMPLETENESS GATE annotates SA remaining as forward-referenced
    in Phase 5 VERDICT EVIDENCE SUMMARY (bidirectional annotation origin)

NEW IN v10 -- ASPIRATIONAL CRITERIA (R14 targets -- both):
  C-30 (Count completeness check): NEW -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID individually looked up against Step 3b row
    labels; each row: [ID | Step 3b row label exists: YES / NOT FOUND | result: CONFIRMED /
    BLOCKED]; classification BLOCKED if any ID NOT FOUND; closes the substitution attack
    vector (inertia item 11) that count-equality leaves open
  C-31 (Expanded bidirectional annotation): NEW -- bidirectional annotation extended to all
    four forward-referencing blocks: EVIDENCE ANCHOR annotates EG IDs as "resolved in
    VERDICT-TO-TABLE TRACEABILITY sub-table below"; TRACEABILITY sub-table header annotates
    its source as "sourced from Step 3b findings table"; VERDICT EVIDENCE SUMMARY rows carry
    back-references to EVIDENCE ANCHOR and PROMOTION COMPLETENESS GATE; closes the
    forward-reference coherence gap (inertia item 12) where blocks are structurally connected
    only by convention and not by explicit annotation; makes C-26 through C-29 self-certifying
```

---

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 -- all schemas and enforcement classes identical. Reproduce in full when running.]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3}. P1 blocks usefulness.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO}. Label lock: promoted SA -> SG.
**Schema 3** `[enforcement: instructional]`: channel field required in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: GATE CLEARANCE SUMMARY blocks advancement.
**Schema 5** `[enforcement: architectural]`: named prerequisites gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

---

### Phase 1 -- Setup: Role-Schema Binding Summary

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA], [SG original].

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M]
Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
  EG-class roles run first. SA/SG-class roles run after promotion.
```

---

### Stage 1 -- Source-Layer Audit

A Stage 1 where all gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE PASS.

**Role relay -- [EG-producing role]**:
- Received from: | Received values: | Schema 2 compliance `[enforcement: instructional]`: Source labels: [list] -- {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: | Produced: | EG gaps: [EG-NN list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a declared: [N] | relayed: [N] | **PASS / FAIL**
> If FAIL: complete missing relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA
Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining certified: R** -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY.
> If MISMATCH: Phase 2b BLOCKED. Reconcile before continuing.

Label lock `[enforcement: instructional]`: promoted gaps must use SG label downstream.

---

### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG role]**: Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections written: [list each required section -- WRITTEN]

---

### Phase 3 -- Findings

#### Step 3a -- Severity Legend Declaration

| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

#### Step 3b -- Findings Table

Prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [list all IDs explicitly] | count >= 3: Y/N |
> distinct Source types >= 2: Y/N | Action uniqueness: Y/N | **FLOOR CHECK: PASS/FAIL**
> If FAIL: add findings. Re-run after correction.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: Source types: [list] -- G-1: PASS/FAIL
**G-2** `[enforcement: architectural]`: Same-Source pairs: [list or "none"] -- G-2: PASS/FAIL
**G-3** `[enforcement: architectural]`: Severity labels: [list] -- G-3: PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation"):
> Gate [X] FAIL: reason / remediation action / re-check result

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active `[enforcement: instructional]`. Phase 4 valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS | G-2: PASS | G-3: PASS -- Phase 4 valid to begin.

[Amend entries: finding / source / remediation channel: spec-invocation-artifact-quality /
change or dismissal / source confirmed]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend P1/P2/P3 declared | [legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS | [labels; FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result + labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | P1/P2/P3 in all Amend entries | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels | [all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted=SG; COMPLETENESS GATE PASS | [promoted gaps; SG confirmed; gate PASS] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in every entry | [channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 results | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; MEMBERSHIP counts | **G-1 SOURCE ATTRIBUTION TABLE**: Source/Phase/Role(s)/Finding IDs [per Source type; verify Phase 2a count = N from MEMBERSHIP block; Phase 2b = M; mismatch = inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy | [activation + PHASE 4 gate summary] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs;
> C-31: EG finding IDs below resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b (resolved in VERDICT-TO-TABLE TRACEABILITY sub-table below;
>   membership verified in PER-ID MEMBERSHIP VERIFICATION table below):
>   [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row;
> C-31 back-reference: sourced from Step 3b findings table above):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> Traceability check: each cited ID appears as a distinct row with Source=EG. If any cited
> ID has no row here, the EVIDENCE ANCHOR is structurally invalid.
>
> **PER-ID MEMBERSHIP VERIFICATION** (C-30: closes inertia item 11 -- per-ID key lookup
> confirms no substitution; count-equality alone cannot detect wrong IDs that number correctly):
>
> | Cited ID | Step 3b row label exists | Membership result |
> |----------|--------------------------|------------------|
> | [F-NN] | YES / NOT FOUND | CONFIRMED / BLOCKED |
> | [F-MM] | YES / NOT FOUND | CONFIRMED / BLOCKED |
>
> Membership check: all [N] cited IDs must have YES. If any ID has NOT FOUND: EVIDENCE
> ANCHOR cites a non-existent finding key. Classification BLOCKED until reconciled.
> COUNT COMPLETENESS CHECK PASS: all [N] cited IDs confirmed as actual Step 3b row keys.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5;
> C-31: closes inertia item 12 -- back-references make each block self-certifying without
> manual document trace; EG count sourced from EVIDENCE ANCHOR above; SA remaining sourced
> from PROMOTION COMPLETENESS GATE, Stage 2):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count (forward-referenced from EVIDENCE ANCHOR above) | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining (forward-referenced from PROMOTION COMPLETENESS GATE) | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived (EG: named list; SA: arithmetic closure).
> All four forward-referencing cross-block links now bidirectional (C-31 PASS):
>   PROMOTION COMPLETENESS GATE -> VERDICT EVIDENCE SUMMARY (and back) [C-29 origin + C-31 ext]
>   EVIDENCE ANCHOR -> VERDICT-TO-TABLE TRACEABILITY sub-table (and back) [C-31 new]
>   VERDICT EVIDENCE SUMMARY -> EVIDENCE ANCHOR (and back) [C-31 new]
>   VERDICT EVIDENCE SUMMARY -> PROMOTION COMPLETENESS GATE (and back) [C-31 new]

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
