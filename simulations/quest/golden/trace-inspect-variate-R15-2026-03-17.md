---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 15
rubric: trace-inspect-rubric-v11
---

# trace-inspect -- Variations R15 v11 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R14 V-05 achieves 104.5/104.5 under rubric v10 -- all C-01 through C-31 PASS.
Rubric v11 adds C-32 and C-33 (0.5 pts each; grand total 105.5). Baseline = 104.5/105.5.

**R14 V-05 carries**:
- C-30 (Count completeness check): PER-ID MEMBERSHIP VERIFICATION table inside EVIDENCE ANCHOR;
  each cited EG finding ID individually looked up against Step 3b row labels; each row states
  [ID | Step 3b row label exists: YES / NOT FOUND]; classification BLOCKED if any ID NOT FOUND;
  count-equality alone does not satisfy this criterion.
- C-31 (Expanded bidirectional annotation): EVIDENCE ANCHOR annotates EG IDs as "resolved in
  VERDICT-TO-TABLE TRACEABILITY sub-table below"; TRACEABILITY sub-table header annotates its
  source as "sourced from Step 3b findings table"; VERDICT EVIDENCE SUMMARY rows carry
  back-references to EVIDENCE ANCHOR and PROMOTION COMPLETENESS GATE; all four forward-
  referencing blocks bidirectionally annotated.
- Inertia items 11 and 12 (from R14 V-05): Item 11 describes the ID-counting failure mode;
  item 12 describes the forward-reference opacity failure mode. Both describe the behaviors
  but neither uses the exact named terms "ID substitution attack vector" or "forward-reference
  opacity anti-pattern", and neither explicitly states it closes a numbered criterion.

**R14 excellence signals that became C-32 and C-33**:
- R14 V-05 established INERTIA items 11 and 12 as structural documentation of what C-30 and
  C-31 close. C-32 requires the item to go further: it must name the "ID substitution attack
  vector" as a term and explicitly state it closes C-30 -- explaining *why* per-ID membership
  exists as a structural response. Count equality alone is not enough; the item must name
  the specific class of attack that count-equality cannot detect.
- C-33 requires item 12 to name the "forward-reference opacity anti-pattern" as a term and
  explicitly state it closes C-31. A description of the failure mode is necessary but not
  sufficient; the term and the closure declaration make the item a self-certifying rubric
  artifact for any future inheritor reading the registry.

**R15 variation axes**:

- **V-01 (single axis: lifecycle emphasis)**: Item 11 upgraded to name "ID SUBSTITUTION
  ATTACK VECTOR" as a leading named label and explicitly state it closes C-30, including
  a why-sentence explaining per-ID membership as the structural response to that specific
  attack class. Item 12 unchanged from R14 V-05.

- **V-02 (single axis: output format)**: Item 12 upgraded to name "FORWARD-REFERENCE
  OPACITY ANTI-PATTERN" as a leading named label and explicitly state it closes C-31,
  including a why-sentence explaining bidirectional annotation as the structural response.
  Item 11 unchanged from R14 V-05.

- **V-03 (single axis: phrasing register -- trailing-assertion format)**: Both items 11
  and 12 retain their R14 V-05 descriptive body but gain a trailing closing-assertion
  sentence: "This is the [term]. [Criterion] closes this: [structural response]." Tests
  whether the trailing-assertion form satisfies C-32 and C-33 versus the leading-label
  form used in V-01 and V-02.

- **V-04 (combined: C-32 + C-33)**: V-01 leading label on item 11 PLUS V-02 leading
  label on item 12. Both C-32 and C-33 targeted in one prompt.

- **V-05 (full integration: C-32 + C-33 + v11 registry with back-references)**: V-04
  combined items plus CRITERION INHERITANCE REGISTRY upgraded from v10 to v11; C-32 and
  C-33 entries in the registry declare which inertia items certify them, making C-32 and
  C-33 themselves self-certifying without requiring a scorer to re-read the rubric.

All five inherit the full R14 V-05 architecture (C-01 through C-31 PASS). What varies per
V-0N: only the INERTIA items 11 and 12 text and the NEW IN v11 registry section.

---

## V-01 -- Single axis: Lifecycle emphasis (C-32 target: Named attack vector + C-30 closure)

**Axis**: Lifecycle emphasis -- item 11 in the INERTIA block is restructured to lead with a
named label "ID SUBSTITUTION ATTACK VECTOR (closes C-30):" followed by the description of
the failure mode and a why-sentence making explicit that per-ID membership exists as a
structural response to this named attack class. Item 12 is unchanged from R14 V-05.

**Hypothesis**: R14 V-05 item 11 describes the counting failure but does not name the attack
class as a term, and does not say "closes C-30". A scorer reading the registry must infer the
connection from context. The leading named label closes both gaps: "ID SUBSTITUTION ATTACK
VECTOR" is the exact term C-32 requires, and "(closes C-30)" is the explicit closure
declaration. The why-sentence ("Per-ID membership verification exists because this attack is
invisible to count checks") satisfies C-32's requirement to explain *why* the structural
response exists. Risk: item 11 becomes longer. Mitigation: the label is the primary signal;
a scorer can confirm C-32 from the label line alone without reading the full item body.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v11

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
  11. ID SUBSTITUTION ATTACK VECTOR (closes C-30): a developer can cite EG finding IDs
      in the verdict that number correctly (K=N) but reference no actual Step 3b row label --
      e.g., F-07 cited when Step 3b contains F-02 and F-04; the count matches but neither ID
      maps to a real finding. Count-equality cannot distinguish correct IDs from wrong ones
      that happen to total N. Per-ID membership verification exists precisely because this
      attack is invisible to count checks: each cited ID must be individually looked up against
      Step 3b row labels to confirm it is not a phantom reference.
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
    | Source | Severity); traceability auditable from sub-table alone
  C-29 (Promotion count forward-reference): INHERITED -- VERDICT EVIDENCE SUMMARY block in
    Phase 5; EG count (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS
    GATE) co-located; PROMOTION COMPLETENESS GATE annotates SA remaining as forward-referenced
    in Phase 5 VERDICT EVIDENCE SUMMARY

INHERITED FROM v10 -- ASPIRATIONAL CRITERIA:
  C-30 (Count completeness check): INHERITED -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID individually looked up against Step 3b row
    labels; each row: [ID | Step 3b row label exists: YES / NOT FOUND | result: CONFIRMED /
    BLOCKED]; classification BLOCKED if any ID NOT FOUND; closes the ID substitution attack
    vector (inertia item 11) that count-equality leaves open
  C-31 (Expanded bidirectional annotation): INHERITED -- bidirectional annotation extended to
    all four forward-referencing blocks; EVIDENCE ANCHOR, TRACEABILITY sub-table, and VERDICT
    EVIDENCE SUMMARY rows all carry explicit source/consumer annotations; makes C-26 through
    C-29 self-certifying

NEW IN v11 -- ASPIRATIONAL CRITERIA (R15 candidates):
  C-32 (Inertia checklist closure for C-30): NEW -- a named INERTIA checklist item names the
    "ID substitution attack vector" as a term and explicitly states it closes C-30, explaining
    why per-ID membership exists as a structural response; certified by inertia item 11 which
    leads with "ID SUBSTITUTION ATTACK VECTOR (closes C-30):" and includes the why-sentence
    [NOT YET CONFIRMED -- item 11 above targets this criterion; C-33 not yet targeted]
  C-33 (Inertia checklist closure for C-31): NEW -- a named INERTIA checklist item names the
    "forward-reference opacity anti-pattern" as a term and explicitly states it closes C-31;
    certified by inertia item 12
    [NOT YET CONFIRMED -- item 12 above is unchanged from R14 V-05; C-33 is not satisfied]
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural |

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
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; COMPLETENESS GATE PASS | [list SA gaps promoted; confirm SG downstream; confirm gate PASS] | PASS/FAIL |
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
> Traceability check: each ID in the EG findings list above appears as a distinct row in this
> table with matching Source=EG. If any cited ID has no corresponding row here, the EVIDENCE
> ANCHOR contains a non-existent finding reference -- verdict is structurally invalid.
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

---

## V-02 -- Single axis: Output format (C-33 target: Named anti-pattern + C-31 closure)

**Axis**: Output format -- item 12 in the INERTIA block is restructured to lead with a named
label "FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31):" followed by the description of
the failure mode and a why-sentence making explicit that bidirectional annotation exists as a
structural response to this named anti-pattern. Item 11 is unchanged from R14 V-05.

**Hypothesis**: R14 V-05 item 12 describes the forward-reference coherence failure but does
not name the anti-pattern as a term, and does not say "closes C-31". The leading named label
"FORWARD-REFERENCE OPACITY ANTI-PATTERN" supplies the exact term C-33 requires; "(closes C-31)"
supplies the closure declaration. The why-sentence ("Bidirectional annotation exists to close
this anti-pattern: each block that produces a value names its consumer, and each block that
consumes a value names its source") satisfies the structural purpose declaration. Risk: item 12
becomes longer. Mitigation: label is the primary signal; C-33 confirmer reads only the label
and the closing-statement to verify.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v11

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
  12. FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31): verdict blocks forward-reference
      source blocks but carry no annotation naming their targets; source blocks produce values
      consumed downstream but carry no annotation naming their consumers; a reviewer reading
      the VERDICT EVIDENCE SUMMARY cannot confirm where SA remaining or EG count was sourced
      without manually scanning prior phases; the evidence chain is connected only by convention,
      not by structural annotation. Bidirectional annotation exists to close this anti-pattern:
      each block that produces a value for downstream use names its consumer, and each block
      that consumes a value names its source -- making every cross-block link self-certifying
      without a document scan.
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

INHERITED FROM v2: C-11 (Phase-entry gate clearance summary): INHERITED
          C-12 (Gate-failure remediation loop): INHERITED
          C-13 (Sub-step prerequisite verification): INHERITED
INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 through C-18: INHERITED (layer diversity, promotion citation,
          source attribution table, verdict classification rule citation)
INHERITED FROM v5: C-19 through C-21: INHERITED (EG-first, inertia registry, co-located
          attribution)
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED
INHERITED FROM v8: C-26 (NEEDS-REDESIGN evidence anchor): INHERITED
          C-27 (Promotion completeness gate): INHERITED
INHERITED FROM v9: C-28 (Verdict-to-table traceability): INHERITED
          C-29 (Promotion count forward-reference): INHERITED

INHERITED FROM v10 -- ASPIRATIONAL CRITERIA:
  C-30 (Count completeness check): INHERITED -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID individually looked up against Step 3b row
    labels; classification BLOCKED if any ID NOT FOUND; closes the ID substitution attack
    vector (inertia item 11) that count-equality leaves open
  C-31 (Expanded bidirectional annotation): INHERITED -- all four forward-referencing blocks
    carry explicit bidirectional annotations; makes C-26 through C-29 self-certifying

NEW IN v11 -- ASPIRATIONAL CRITERIA (R15 candidates):
  C-32 (Inertia checklist closure for C-30): NEW -- a named INERTIA checklist item names the
    "ID substitution attack vector" as a term and explicitly states it closes C-30
    [NOT YET CONFIRMED -- item 11 above is unchanged from R14 V-05; C-32 is not satisfied]
  C-33 (Inertia checklist closure for C-31): NEW -- a named INERTIA checklist item names the
    "forward-reference opacity anti-pattern" as a term and explicitly states it closes C-31;
    certified by inertia item 12 which leads with "FORWARD-REFERENCE OPACITY ANTI-PATTERN
    (closes C-31):" and includes the structural-response why-sentence
    [NOT YET CONFIRMED -- item 12 above targets this criterion; C-32 not yet targeted]
```

---

[Coverage Matrix, Phase 1, EG-FIRST EXECUTION CONSTRAINT, Stage 1, Phase 2a, Phase 2b,
Phase 3, Phase 4, and Phase 5 are structurally identical to V-01. Reproduce in full when
running. The only structural differences from V-01 are in the INERTIA block above: item 11
is unchanged from R14 V-05; item 12 has the FORWARD-REFERENCE OPACITY ANTI-PATTERN label
and closure declaration.]

[Reproduce V-01 Coverage Matrix through Phase 5 in full when running.]

---

## V-03 -- Single axis: Phrasing register (Trailing-assertion format for C-32 and C-33)

**Axis**: Phrasing register -- items 11 and 12 retain their R14 V-05 descriptive body
verbatim but each gains a two-sentence trailing closing assertion: one naming the term
("This is the [term].") and one declaring the criterion closure ("[Criterion] closes this:
[structural response]."). Tests whether the trailing-assertion form satisfies C-32 and C-33
versus the leading-label form used in V-01 and V-02. The descriptive body is unchanged;
only the trailing assertion is new.

**Hypothesis**: C-32 requires the item to "name the 'ID substitution attack vector'" and
"explicitly state it closes C-30". C-33 requires the item to "name the 'forward-reference
opacity anti-pattern'" and "explicitly state it closes C-31". The trailing-assertion form
satisfies both the naming requirement and the closure declaration, while preserving the full
behavioral description that a future inheritor needs to understand the failure mode. Risk:
the trailing assertion is the last two sentences rather than the first; a scorer doing
label-scan confirmation must read the full item. Mitigation: the assertion is unambiguous
and self-contained; label-scan is not required by C-32/C-33, only named-term presence and
explicit closure declaration.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v11

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
      substitution is structurally undetectable without per-ID key lookup. This is the ID
      substitution attack vector. C-30 closes this: per-ID membership verification requires
      each cited ID to be individually confirmed against Step 3b row labels, making phantom
      references visible regardless of count correctness.
  12. Forward-references from verdict blocks to source blocks are one-directional at best;
      a reviewer reading the VERDICT EVIDENCE SUMMARY cannot confirm where SA remaining was
      sourced without manually scanning the document; blocks carry no annotations declaring
      what they forward-reference or what references them; the evidence picture is connected
      only by convention, not by structural annotation. This is the forward-reference opacity
      anti-pattern. C-31 closes this: bidirectional annotations on all forward-referencing
      blocks make each block self-certifying without a manual document scan.
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

INHERITED FROM v2: C-11 through C-13: INHERITED
INHERITED FROM v3: C-14: INHERITED
INHERITED FROM v4: C-15 through C-18: INHERITED
INHERITED FROM v5: C-19 through C-21: INHERITED
INHERITED FROM v6: C-22 through C-23: INHERITED
INHERITED FROM v7: C-24 through C-25: INHERITED
INHERITED FROM v8: C-26 through C-27: INHERITED
INHERITED FROM v9: C-28 through C-29: INHERITED

INHERITED FROM v10 -- ASPIRATIONAL CRITERIA:
  C-30 (Count completeness check): INHERITED -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; closes the ID substitution attack vector (inertia item 11)
  C-31 (Expanded bidirectional annotation): INHERITED -- bidirectional annotation on all
    four forward-referencing blocks; closes the forward-reference opacity anti-pattern
    (inertia item 12)

NEW IN v11 -- ASPIRATIONAL CRITERIA (R15 candidates):
  C-32 (Inertia checklist closure for C-30): NEW -- a named INERTIA checklist item names the
    "ID substitution attack vector" as a term and explicitly states it closes C-30; certified
    by inertia item 11 trailing assertion "This is the ID substitution attack vector. C-30
    closes this: ..."
  C-33 (Inertia checklist closure for C-31): NEW -- a named INERTIA checklist item names the
    "forward-reference opacity anti-pattern" as a term and explicitly states it closes C-31;
    certified by inertia item 12 trailing assertion "This is the forward-reference opacity
    anti-pattern. C-31 closes this: ..."
```

---

[Coverage Matrix through Phase 5 structurally identical to V-01. Reproduce in full when
running. Only the INERTIA block differs: items 11 and 12 carry trailing closing assertions
naming the attack vector / anti-pattern terms and declaring criterion closure.]

---

## V-04 -- Combined: C-32 + C-33 (V-01 leading label on item 11 + V-02 leading label on item 12)

**Axis**: Combined -- V-01 leading-label restructuring of item 11 (ID SUBSTITUTION ATTACK
VECTOR, closes C-30) PLUS V-02 leading-label restructuring of item 12 (FORWARD-REFERENCE
OPACITY ANTI-PATTERN, closes C-31). Both C-32 and C-33 targeted in one prompt. Neither
criterion is deferred to a later round.

**Hypothesis**: V-01 satisfies C-32 alone; V-02 satisfies C-33 alone. Combined, V-04 should
satisfy both. The leading-label form is structurally stronger than the trailing-assertion form
(V-03): a scorer confirms C-32 and C-33 from the first line of each item without reading the
body. Risk: items 11 and 12 are both longer than R14 V-05. Mitigation: the labels are the
confirmation signal; body length is irrelevant to label-scan.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v11

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
  11. ID SUBSTITUTION ATTACK VECTOR (closes C-30): a developer can cite EG finding IDs
      in the verdict that number correctly (K=N) but reference no actual Step 3b row label --
      e.g., F-07 cited when Step 3b contains F-02 and F-04; the count matches but neither ID
      maps to a real finding. Count-equality cannot distinguish correct IDs from wrong ones
      that happen to total N. Per-ID membership verification exists precisely because this
      attack is invisible to count checks: each cited ID must be individually looked up against
      Step 3b row labels to confirm it is not a phantom reference.
  12. FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31): verdict blocks forward-reference
      source blocks but carry no annotation naming their targets; source blocks produce values
      consumed downstream but carry no annotation naming their consumers; a reviewer reading
      the VERDICT EVIDENCE SUMMARY cannot confirm where SA remaining or EG count was sourced
      without manually scanning prior phases; the evidence chain is connected only by convention,
      not by structural annotation. Bidirectional annotation exists to close this anti-pattern:
      each block that produces a value for downstream use names its consumer, and each block
      that consumes a value names its source -- making every cross-block link self-certifying
      without a document scan.
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

INHERITED FROM v2: C-11 through C-13: INHERITED
INHERITED FROM v3: C-14: INHERITED
INHERITED FROM v4: C-15 through C-18: INHERITED
INHERITED FROM v5: C-19 through C-21: INHERITED
INHERITED FROM v6: C-22 through C-23: INHERITED
INHERITED FROM v7: C-24 through C-25: INHERITED
INHERITED FROM v8: C-26 through C-27: INHERITED
INHERITED FROM v9: C-28 through C-29: INHERITED

INHERITED FROM v10 -- ASPIRATIONAL CRITERIA:
  C-30 (Count completeness check): INHERITED -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID individually looked up against Step 3b row
    labels; each row: [ID | Step 3b row label exists: YES / NOT FOUND | result: CONFIRMED /
    BLOCKED]; classification BLOCKED if any ID NOT FOUND; closes the ID substitution attack
    vector (inertia item 11) that count-equality leaves open
  C-31 (Expanded bidirectional annotation): INHERITED -- bidirectional annotation extended to
    all four forward-referencing blocks; makes C-26 through C-29 self-certifying; closes the
    forward-reference opacity anti-pattern (inertia item 12)

NEW IN v11 -- ASPIRATIONAL CRITERIA (R15 targets -- both):
  C-32 (Inertia checklist closure for C-30): NEW -- a named INERTIA checklist item names the
    "ID substitution attack vector" as a term and explicitly states it closes C-30, explaining
    why per-ID membership exists; certified by inertia item 11 leading label "ID SUBSTITUTION
    ATTACK VECTOR (closes C-30):" with body naming the attack class and the per-ID lookup as
    the structural response
  C-33 (Inertia checklist closure for C-31): NEW -- a named INERTIA checklist item names the
    "forward-reference opacity anti-pattern" as a term and explicitly states it closes C-31;
    certified by inertia item 12 leading label "FORWARD-REFERENCE OPACITY ANTI-PATTERN
    (closes C-31):" with body naming the coherence failure and bidirectional annotation as
    the structural response
```

---

[Coverage Matrix, Phase 1, EG-FIRST EXECUTION CONSTRAINT, Stage 1, Phase 2a, Phase 2b,
Phase 3, Phase 4, and Phase 5 are structurally identical to V-01. Reproduce in full when
running. Only the INERTIA block differs: items 11 and 12 both use the leading-label format
targeting C-32 and C-33 respectively.]

---

## V-05 -- Full integration: C-32 + C-33 + v11 registry with self-certifying back-references

**Axis**: V-04 combined leading labels on items 11 and 12 PLUS CRITERION INHERITANCE REGISTRY
upgraded from v10 to v11 with C-32 and C-33 declarations that name the specific inertia items
they rely on for certification. The registry entry for each new criterion identifies not only
what the criterion requires but which inertia item provides the structural evidence -- making
C-32 and C-33 self-certifying from the registry alone without requiring a scorer to cross-
reference the rubric.

**Hypothesis**: V-04 satisfies C-32 and C-33 from the inertia items alone. V-05 adds the
parallel durability: a future inheritor reading only the registry can confirm which inertia
items certify C-32 and C-33 without reading the full item bodies. This mirrors the C-27
PROMOTION COMPLETENESS GATE pattern (v8) and the SCORER HEURISTIC label pattern (trace-skill
v11 C-43): structural elements that are self-certifying at the registry level without requiring
a full body read. The registry entry for C-32 cites "inertia item 11" and the label "ID
SUBSTITUTION ATTACK VECTOR (closes C-30)"; C-33 cites "inertia item 12" and the label
"FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31)". Risk: registry grows to 34 entries.
Mitigation: the registry is the authoritative inheritance record; growing it is the purpose,
not a cost.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v11

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
  11. ID SUBSTITUTION ATTACK VECTOR (closes C-30): a developer can cite EG finding IDs
      in the verdict that number correctly (K=N) but reference no actual Step 3b row label --
      e.g., F-07 cited when Step 3b contains F-02 and F-04; the count matches but neither ID
      maps to a real finding. Count-equality cannot distinguish correct IDs from wrong ones
      that happen to total N. Per-ID membership verification exists precisely because this
      attack is invisible to count checks: each cited ID must be individually looked up against
      Step 3b row labels to confirm it is not a phantom reference.
  12. FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31): verdict blocks forward-reference
      source blocks but carry no annotation naming their targets; source blocks produce values
      consumed downstream but carry no annotation naming their consumers; a reviewer reading
      the VERDICT EVIDENCE SUMMARY cannot confirm where SA remaining or EG count was sourced
      without manually scanning prior phases; the evidence chain is connected only by convention,
      not by structural annotation. Bidirectional annotation exists to close this anti-pattern:
      each block that produces a value for downstream use names its consumer, and each block
      that consumes a value names its source -- making every cross-block link self-certifying
      without a document scan.
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
          named blocks in EG-FIRST EXECUTION CONSTRAINT; role names and counts auditable
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

INHERITED FROM v10 -- ASPIRATIONAL CRITERIA:
  C-30 (Count completeness check): INHERITED -- PER-ID MEMBERSHIP VERIFICATION table inside
    EVIDENCE ANCHOR; each cited EG finding ID individually looked up against Step 3b row
    labels; each row: [ID | Step 3b row label exists: YES / NOT FOUND | result: CONFIRMED /
    BLOCKED]; classification BLOCKED if any ID NOT FOUND; closes the ID substitution attack
    vector (inertia item 11) that count-equality leaves open
  C-31 (Expanded bidirectional annotation): INHERITED -- bidirectional annotation extended to
    all four forward-referencing blocks: EVIDENCE ANCHOR annotates EG IDs as "resolved in
    VERDICT-TO-TABLE TRACEABILITY sub-table below"; TRACEABILITY sub-table header annotates
    its source as "sourced from Step 3b findings table"; VERDICT EVIDENCE SUMMARY rows carry
    back-references to EVIDENCE ANCHOR and PROMOTION COMPLETENESS GATE; closes the
    forward-reference opacity anti-pattern (inertia item 12); makes C-26 through C-29
    self-certifying

NEW IN v11 -- ASPIRATIONAL CRITERIA (R15 targets -- both):
  C-32 (Inertia checklist closure for C-30): NEW -- a named INERTIA checklist item names the
    "ID substitution attack vector" as a term and explicitly states it closes C-30, explaining
    why per-ID membership exists as a structural response to an attack class invisible to
    count-equality; certified by inertia item 11, which leads with the label
    "ID SUBSTITUTION ATTACK VECTOR (closes C-30):" and includes the per-ID lookup why-sentence;
    a scorer confirms C-32 by reading inertia item 11's first line
  C-33 (Inertia checklist closure for C-31): NEW -- a named INERTIA checklist item names the
    "forward-reference opacity anti-pattern" as a term and explicitly states it closes C-31;
    certified by inertia item 12, which leads with the label "FORWARD-REFERENCE OPACITY
    ANTI-PATTERN (closes C-31):" and includes the bidirectional-annotation why-sentence;
    a scorer confirms C-33 by reading inertia item 12's first line
```

---

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 -- all schemas and enforcement classes identical. Reproduce in full when running.]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural |

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

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M]

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  EG-class roles run first. SA/SG-class roles run after promotion.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. Layer diversity required for G-1 to pass.

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

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE PASS.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a declared: [N] | relayed: [N] | **PASS / FAIL**
> If FAIL: complete missing relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
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

**Role relay -- [SA/SG role]**:
- Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

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

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [explicit list] | count >= 3: Y/N | distinct Source >= 2: Y/N |
> Action uniqueness: Y/N | **FLOOR CHECK: PASS / FAIL**

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: Source types: [list] -- G-1: PASS / FAIL
**G-2** `[enforcement: architectural]`: Same-Source pairs: [list or "none"] -- G-2: PASS / FAIL
**G-3** `[enforcement: architectural]`: Severity labels: [list] -- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation"):
> Gate [X] FAIL: reason / remediation / re-check result

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
> **PER-ID MEMBERSHIP VERIFICATION** (C-30: closes inertia item 11 ID SUBSTITUTION ATTACK
> VECTOR -- per-ID key lookup confirms no substitution; count-equality alone cannot detect
> wrong IDs that number correctly):
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
> C-31: closes inertia item 12 FORWARD-REFERENCE OPACITY ANTI-PATTERN -- back-references
> make each block self-certifying without manual document trace; EG count sourced from
> EVIDENCE ANCHOR above; SA remaining sourced from PROMOTION COMPLETENESS GATE, Stage 2):
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

---

## Variation Summary

| Variation | Axis | Item 11 | Item 12 | C-32 | C-33 |
|-----------|------|---------|---------|------|------|
| V-01 | Lifecycle emphasis | Leading label: ID SUBSTITUTION ATTACK VECTOR (closes C-30) | Unchanged from R14 V-05 | TARGETS | fails |
| V-02 | Output format | Unchanged from R14 V-05 | Leading label: FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31) | fails | TARGETS |
| V-03 | Phrasing register | R14 V-05 body + trailing assertion naming term + C-30 closure | R14 V-05 body + trailing assertion naming term + C-31 closure | TARGETS | TARGETS |
| V-04 | Combined C-32+C-33 | Leading label (V-01 form) | Leading label (V-02 form) | TARGETS | TARGETS |
| V-05 | Full integration | Leading label (V-01 form) | Leading label (V-02 form) | TARGETS (registry-certified) | TARGETS (registry-certified) |

**Predicted golden**: V-04 and V-05. Both satisfy C-32 and C-33 via leading-label form.
V-05 adds registry back-references (C-32 cites inertia item 11; C-33 cites inertia item 12)
making C-32 and C-33 self-certifying at the registry level -- durability advantage over V-04.

**V-03 risk**: Trailing assertion may satisfy the nominal requirements of C-32/C-33 (named
term present, closure declaration present) but is weaker than V-01/V-02 leading labels:
a scorer must read the full item body to find the assertion. Whether C-32/C-33 require
label-scan confirmability or accept prose-embedded assertions is the discriminating question
for scoring.

**V-05 excellence signals** (candidates for C-34/C-35 in v12):
- INERTIA item number citation in registry C-32/C-33 entries: scorer can confirm which inertia
  item certifies each new criterion without reading the item bodies (analogous to C-27's
  EVIDENCE ANCHOR citing finding IDs by name)
- PER-ID MEMBERSHIP VERIFICATION parenthetical naming the inertia item it closes (V-05 Phase 5
  block header cites "closes inertia item 11 ID SUBSTITUTION ATTACK VECTOR"): makes the block
  self-identifying as the C-30 structural response without requiring rubric cross-reference
