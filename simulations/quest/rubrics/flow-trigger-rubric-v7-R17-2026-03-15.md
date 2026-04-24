# Flow-Trigger Skill — Round 17 Variations (Rubric v13)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v13 (C-01 through C-38, denominator /31 aspirational)
**Date**: 2026-03-15

---

## Variation Design Notes

R16 saturated v13 in V-05 (100.00, all 31 aspirational criteria). Three structural patterns
were formalized: C-36 (gate integrity audit with per-slot EMITTED/MANIFEST-GAP in Role 5),
C-37 (BUDGET_GATE as named emitted key with CHAIN-LINK-3 cross-block readback), and C-38
(14-slot simulation manifest as canonical completeness registry replacing separate chain/gate
integrity sections). R17 targets the next structural tier.

**New signal candidates for R17:**

**Signal A — Gate passage key chain** *(V-01 axis)*: C-36 detects *absent* GATE-STATE
blocks. C-37 formalizes one specific key readback (budget gate). Neither mechanism addresses
whether an *emitted* GATE-STATE block carries evidence for *why* it closed — any role can
emit GATE-STATE-N→M with Status=CLOSED and no upstream key reference. V-01 extends C-37's
pattern to all seven transitions: each GATE-STATE block carries a `PASSAGE_KEY` field that
reads a named key from the preceding CHAIN-LINK. An emitted GATE-STATE with no PASSAGE_KEY
is a structural gap (PASSAGE-KEY-GAP) distinct from artifact absence (MANIFEST-GAP). Role 5
audits both dimensions.

**Signal B — Ownership registry and OWNER-MISMATCH audit** *(V-02 axis)*: C-36 detects
absent artifacts; C-38 drives COLUMN-GAP from MANIFEST-GAP. Neither detects an artifact
emitted by the *wrong role* — CHAIN-LINK-3 produced by Pathology Analyst, GATE-STATE-3→4
carrying `Owner: PCR Analyst`. V-02 declares a header-level Ownership Registry (14 rows:
artifact + expected owner). Role 5's manifest verification gains a second dimension: for each
EMITTED slot, compare the declared Owner field against the registry. A mismatch is a named
`OWNER-MISMATCH: [artifact] (declared: [role], expected: [role])`.

**Signal C — Manifest derivation proof** *(V-03 axis)*: C-38 formalizes the 14-slot manifest
but the denominator "/14" is a hardcoded constant — not structurally derived. If the simulation
were extended (e.g., a new role inserted between Role 2 and Role 3), the manifest would need
manual updating. V-03 adds a derivation proof at manifest header: `ROLE_COUNT=7 → 7
CHAIN-LINK slots; GATE_COUNT=ROLE_COUNT-1 transitions + 2 bookend gates = 7 GATE-STATE slots;
TOTAL=14`. Role 5 verifies the arithmetic before slot verification. A manifest with a
hardcoded "/14" that is not derived from role/gate counts satisfies C-38 but fails this signal.

**Variation axes (3 single-axis, then 2 combined):**

- V-01: **Role sequence** — gate passage key chain (each role declares PASSAGE_KEY before GATE-STATE transition)
- V-02: **Output format** — header ownership registry table + OWNER-MISMATCH dimension in Role 5 manifest audit
- V-03: **Lifecycle emphasis** — manifest derivation proof as named header phase with explicit arithmetic
- V-04: **Combined** — role sequence + output format (passage keys + ownership registry + dual-dimension audit)
- V-05: **Combined** — all three + inertia framing (explicit status-quo failure analysis opening each new structural section)

---

## V-01 — Role Sequence: Gate Passage Key Chain

**Axis**: Role sequence — each CHAIN-LINK-emitting role also declares a `PASSAGE_KEY`
annotation immediately before the GATE-STATE that follows it. The PASSAGE_KEY names the
specific key(s) from that CHAIN-LINK that certify gate passage. The GATE-STATE reads those
keys back in a `PASSAGE_KEY` field. Role 5 audits all 7 GATE-STATE slots for both presence
(MANIFEST-GAP if absent, C-38) and passage key population (PASSAGE-KEY-GAP if emitted but
unpopulated or carrying no named key reference).

**Hypothesis**: C-37 closes the self-attestation gap at one gate (budget). V-01 generalizes
this: every gate transition has a named upstream key that justifies it. A gate that closes
without citing evidence is structurally distinguishable from a gate that reads a key from its
upstream CHAIN-LINK. The two gap types (absent artifact vs. unjustified closure) are
independently auditable by Role 5, producing a finer-grained completeness protocol than
MANIFEST-GAP alone.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating
which automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts and passage key readbacks at every transition.
Complete all blocks in order. Do not begin a block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change:        {{change}}
Power Platform environment: {{environment_name}}  <- specific named environment required
Solution layer:            {{solution_layer}}      <- specific named solution required
```

**Simulation Manifest** — declared at header; Role 5 verifies all 14 artifact slots plus
7 passage key slots (21 verification points total).

```
SIMULATION MANIFEST
Chain-link slots  (7): CHAIN-LINK-0, CHAIN-LINK-1, CHAIN-LINK-PCR,
                        CHAIN-LINK-2, CHAIN-LINK-3, CHAIN-LINK-4, CHAIN-LINK-4B
Gate-state slots  (7): GATE-STATE-0→1, GATE-STATE-1→PCR, GATE-STATE-PCR→2,
                        GATE-STATE-2→3, GATE-STATE-3→4, GATE-STATE-4→4B, GATE-STATE-4B→5
Passage-key slots (7): one per GATE-STATE — each must carry a named key readback
                        from the immediately preceding CHAIN-LINK
```

---

### Role 0 — Inertia Analyst (Prosecution Theories + Forward Mesh)

**Mandate**: Produce the Failure Mode Catalog and CHAIN-LINK-0. This is the sole output of
this role. No involvement in threat cataloging, trigger table, budget, pathology, or audit.

For this triggering change, produce three prosecution theory entries:

| Charge | Why this change creates this risk | Predicted TC-2 cascade signatures | Predicted TC-3 side-effect signatures |
|--------|----------------------------------|-----------------------------------|---------------------------------------|
| IF-Storm | [why — specific to this change] | [anticipated chains, or "none anticipated"] | [anticipated side effects, or "none anticipated"] |
| IF-Missing | [why] | [anticipated absent paths, or "none anticipated"] | [anticipated absent side effects, or "none anticipated"] |
| IF-Circular | [why] | [anticipated re-entrant chains, or "none anticipated"] | [anticipated circular side effects, or "none anticipated"] |

Emit **CHAIN-LINK-0** verbatim immediately after:

```
CHAIN-LINK-0 (owner: Inertia Analyst)
ENV={{environment_name}} | LAYER={{solution_layer}}
MESH_STORM=[RISK | NO-RISK]
MESH_MISSING=[RISK | NO-RISK]
MESH_CIRCULAR=[RISK | NO-RISK]
STORM_TC2_PRED=[n] | STORM_TC3_PRED=[n]
MISSING_TC2_PRED=[n] | MISSING_TC3_PRED=[n]
CIRCULAR_TC2_PRED=[n] | CIRCULAR_TC3_PRED=[n]
```

Passage key declaration (emit immediately after CHAIN-LINK-0, before GATE-STATE):

```
GATE_PASSAGE_KEY-0→1:
  Justifying keys: CHAIN-LINK-0.MESH_STORM, CHAIN-LINK-0.MESH_MISSING, CHAIN-LINK-0.MESH_CIRCULAR
  Passage condition: all three MESH_* keys emitted and prosecution table complete
```

Emit **GATE-STATE-0→1** verbatim:

```
GATE-STATE-0→1:
  Owner: Inertia Analyst
  PASSAGE_KEY: [read CHAIN-LINK-0.MESH_STORM=<val>, CHAIN-LINK-0.MESH_MISSING=<val>, CHAIN-LINK-0.MESH_CIRCULAR=<val>]
  Condition: Prosecution theory table complete; CHAIN-LINK-0 emitted with all MESH_* keys
  Status: [OPEN | CLOSED]
```

⛔ **Gate 0→1**: GATE-STATE-0→1 Status=CLOSED AND PASSAGE_KEY populated before Role 1 begins.

---

### Role 1 — Threat Cataloger

**Mandate**: Produce TC-1, TC-2, TC-3, Mesh Completeness Check, and CHAIN-LINK-1. Read
CHAIN-LINK-0 prediction counts to know how many prosecution theories require confirmation.

**TC-1 — Candidate Trigger Conditions**

| Automation | Trigger condition | Evaluates? YES/NO | IF-* annotation | Notes |
|-----------|-------------------|-------------------|-----------------|-------|
| [name] | [condition] | YES or NO only | IF-Storm/Missing/Circular/none — required; blank not acceptable | [boundary condition or N/A] |

**TC-2 — Cascade Paths** *(IF-* annotation required on every row; "IF-none" is the explicit null)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none | Confirmed: [detail] OR ⚠ Not confirmed: [reason] — read CHAIN-LINK-0 pred keys | [notes] |

**TC-3 — Side-Effect Scope** *(IF-* annotation required on every row)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none | Confirmed: [detail] OR ⚠ Not confirmed: [reason] | YES or NO |

**Mesh Completeness Check**

| Charge | TC-1 count | TC-2 count | TC-3 count | Status |
|--------|-----------|-----------|-----------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "⚠ [charge] orphaned — [explanation of why no TC evidence for this change]."

Emit **CHAIN-LINK-1** verbatim:

```
CHAIN-LINK-1 (owner: Threat Cataloger)
TC1=[n] | TC2=[n] | TC3=[n]
STORM_TC1=[n] | STORM_TC2=[n] | STORM_TC3=[n]
MISSING_TC1=[n] | MISSING_TC2=[n] | MISSING_TC3=[n]
CIRCULAR_TC1=[n] | CIRCULAR_TC2=[n] | CIRCULAR_TC3=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
PRED_CONFIRMED=[n] | PRED_FLAGGED=[n]
```

Passage key declaration:

```
GATE_PASSAGE_KEY-1→PCR:
  Justifying keys: CHAIN-LINK-1.TC1, CHAIN-LINK-1.MESH_STORM, CHAIN-LINK-1.MESH_MISSING, CHAIN-LINK-1.MESH_CIRCULAR
  Passage condition: TC-1/TC-2/TC-3 complete with IF-* annotations; mesh check complete; CHAIN-LINK-1 emitted
```

Emit **GATE-STATE-1→PCR** verbatim:

```
GATE-STATE-1→PCR:
  Owner: Threat Cataloger
  PASSAGE_KEY: [read CHAIN-LINK-1.TC1=<n>, CHAIN-LINK-1.MESH_STORM=<val>, CHAIN-LINK-1.MESH_MISSING=<val>, CHAIN-LINK-1.MESH_CIRCULAR=<val>]
  Condition: CHAIN-LINK-1 emitted; all mesh statuses declared
  Status: [OPEN | CLOSED]
```

⛔ **Gate 1→PCR**: GATE-STATE-1→PCR Status=CLOSED AND PASSAGE_KEY populated before PCR Analyst begins.

---

### PCR Analyst — Prosecution Closure Report

**Independence declaration**: PCR Analyst is explicitly distinct from (1) Inertia Analyst
(prediction author), (2) Registry Analyst, (3) Pathology Analyst (verdict producer), (4)
Remediation Coverage Analyst / Phase 4B, and (5) Audit Analyst. Reads CHAIN-LINK-0 and
CHAIN-LINK-1 as black-box inputs. CHAIN-LINK-PCR is the first independent terminal artifact.

For each charge, read prediction counts from CHAIN-LINK-0 and confirmation counts from
CHAIN-LINK-1 to assess prosecution closure:

**IF-Storm closure**: CHAIN-LINK-0.STORM_TC2_PRED=[n], STORM_TC3_PRED=[n] vs.
CHAIN-LINK-1.STORM_TC2=[n], STORM_TC3=[n] — [assessment]; silent gaps = preds - confirmed - flagged

**IF-Missing closure**: [same pattern]

**IF-Circular closure**: [same pattern]

Emit **CHAIN-LINK-PCR** verbatim:

```
CHAIN-LINK-PCR (owner: PCR Analyst — first independent terminal artifact)
PCR_STORM=[CLOSED | INDETERMINATE | NULL]  (read: CHAIN-LINK-0.STORM_TC2_PRED+STORM_TC3_PRED vs CHAIN-LINK-1.STORM_TC2+STORM_TC3)
PCR_MISSING=[CLOSED | INDETERMINATE | NULL]
PCR_CIRCULAR=[CLOSED | INDETERMINATE | NULL]
SILENT_GAPS_STORM=[n] | SILENT_GAPS_MISSING=[n] | SILENT_GAPS_CIRCULAR=[n]
```

Passage key declaration:

```
GATE_PASSAGE_KEY-PCR→2:
  Justifying keys: CHAIN-LINK-PCR.PCR_STORM, CHAIN-LINK-PCR.PCR_MISSING, CHAIN-LINK-PCR.PCR_CIRCULAR
  Passage condition: all three PCR_* verdict keys emitted
```

Emit **GATE-STATE-PCR→2** verbatim:

```
GATE-STATE-PCR→2:
  Owner: PCR Analyst
  PASSAGE_KEY: [read CHAIN-LINK-PCR.PCR_STORM=<val>, CHAIN-LINK-PCR.PCR_MISSING=<val>, CHAIN-LINK-PCR.PCR_CIRCULAR=<val>]
  Condition: CHAIN-LINK-PCR emitted with all three PCR_* keys
  Status: [OPEN | CLOSED]
```

⛔ **Gate PCR→2**: GATE-STATE-PCR→2 Status=CLOSED AND PASSAGE_KEY populated before Role 2 begins.

---

### Role 2 — Registry Analyst

**Mandate**: Trigger table and CHAIN-LINK-2. Does not evaluate pathology.

**Trigger Table** *(read: CHAIN-LINK-1.TC1=[n] to verify condition count)*:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int for YES; -- for NO] | [name] | [TC-1 ref] | YES or NO only | [inputs] | [outputs] | [TC-3 ref or "none"] |

Emit **CHAIN-LINK-2** verbatim:

```
CHAIN-LINK-2 (owner: Registry Analyst)
M=[count YES rows with at least one non-"none" side effect]
N=[count all YES rows]
NON_FIRING=[count NO rows]
BUDGET_GATE=[TRIGGERED | WAIVED]
  (TRIGGERED if M >= 3 AND at least one non-"none" Side Effects entry; WAIVED otherwise)
```

Passage key declaration:

```
GATE_PASSAGE_KEY-2→3:
  Justifying keys: CHAIN-LINK-2.M, CHAIN-LINK-2.N, CHAIN-LINK-2.BUDGET_GATE
  Passage condition: trigger table complete; M, N, BUDGET_GATE keys emitted
```

Emit **GATE-STATE-2→3** verbatim:

```
GATE-STATE-2→3:
  Owner: Registry Analyst
  PASSAGE_KEY: [read CHAIN-LINK-2.M=<val>, CHAIN-LINK-2.N=<val>, CHAIN-LINK-2.BUDGET_GATE=<val>]
  Condition: CHAIN-LINK-2 emitted with M, N, NON_FIRING, BUDGET_GATE
  Status: [OPEN | CLOSED]
```

⛔ **Gate 2→3**: GATE-STATE-2→3 Status=CLOSED AND PASSAGE_KEY populated before Role 3 begins.

---

### Role 3 — Budget Analyst

**Mandate**: Read CHAIN-LINK-2.BUDGET_GATE — do not re-evaluate the gate condition.

```
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated by Role 3
```

If WAIVED: emit `Budget Gate: WAIVED — M=[read CHAIN-LINK-2.M], condition not met.`

If TRIGGERED, produce:
1. Per-automation action count (one line per automation with side effects):
   `[Name]: [Dataverse] + [connector] + [child flows] = [total] requests/invocation`
   No aggregate without per-automation intermediate arithmetic.
2. Total API requests: [sum]
3. Power Platform daily limit: [specific number for this license tier]
4. Budget consumed: [%]
5. Run duration: [X to Y] seconds — specific span required; hedged ranges not acceptable

Emit **CHAIN-LINK-3** verbatim:

```
CHAIN-LINK-3 (owner: Budget Analyst)
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated by Role 3
TOTAL_REQ=[n | N/A] | DAILY_LIMIT=[n | N/A] | BUDGET_PCT=[pct | N/A] | DURATION=[X to Y s | N/A]
```

Passage key declaration:

```
GATE_PASSAGE_KEY-3→4:
  Justifying keys: CHAIN-LINK-3.TRIGGERED (provenance: read from CHAIN-LINK-2.BUDGET_GATE)
  Passage condition: budget section complete or WAIVED; TRIGGERED carries key readback from CHAIN-LINK-2
```

Emit **GATE-STATE-3→4** verbatim:

```
GATE-STATE-3→4:
  Owner: Budget Analyst
  PASSAGE_KEY: [read CHAIN-LINK-3.TRIGGERED=<val> (from CHAIN-LINK-2.BUDGET_GATE), CHAIN-LINK-3.BUDGET_PCT=<val>]
  Condition: CHAIN-LINK-3 emitted; TRIGGERED carries key readback annotation
  Status: [OPEN | CLOSED]
```

⛔ **Gate 3→4**: GATE-STATE-3→4 Status=CLOSED AND PASSAGE_KEY carries CHAIN-LINK-3.TRIGGERED readback before Role 4 begins.

---

### Role 4 — Pathology Analyst

**Mandate**: Assess all three pathology types. Verdict keyword first on its own line.
Three-layer remediation required for every DETECTED or INDETERMINATE verdict.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Storm entries (read: CHAIN-LINK-1.STORM_TC2=[n]): [cite]
- TC-3 IF-Storm entries (read: CHAIN-LINK-1.STORM_TC3=[n]): [cite]
- Registry M=[read CHAIN-LINK-2.M], N=[read CHAIN-LINK-2.N]
- PCR closure (read: CHAIN-LINK-PCR.PCR_STORM=[val]): [note]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism — name it, not the feature area]
- Layer 2 — Catalog entry: TC-[type], entry [#] from Role 1
- Layer 3 — Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-1 IF-Missing annotations (read: CHAIN-LINK-1.MISSING_TC1=[n]): [cite]
- TC-3 IF-Missing entries (read: CHAIN-LINK-1.MISSING_TC3=[n]): [cite]
- PCR closure (read: CHAIN-LINK-PCR.PCR_MISSING=[val]): [note]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Circular entries (read: CHAIN-LINK-1.CIRCULAR_TC2=[n]): [cite]
- TC-1 IF-Circular annotations (read: CHAIN-LINK-1.CIRCULAR_TC1=[n]): [cite]
- PCR closure (read: CHAIN-LINK-PCR.PCR_CIRCULAR=[val]): [note]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Circular

Emit **CHAIN-LINK-4** verbatim:

```
CHAIN-LINK-4 (owner: Pathology Analyst)
STORM=[DETECTED | NOT_DETECTED | INDETERMINATE]
MISSING=[DETECTED | NOT_DETECTED | INDETERMINATE]
CIRCULAR=[DETECTED | NOT_DETECTED | INDETERMINATE]
REM_PROVIDED=[n] | REM_REQUIRED=[count of DETECTED+INDETERMINATE verdicts]
```

Passage key declaration:

```
GATE_PASSAGE_KEY-4→4B:
  Justifying keys: CHAIN-LINK-4.STORM, CHAIN-LINK-4.MISSING, CHAIN-LINK-4.CIRCULAR
  Passage condition: all three verdict keys emitted; REM_REQUIRED computed
```

Emit **GATE-STATE-4→4B** verbatim:

```
GATE-STATE-4→4B:
  Owner: Pathology Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4.STORM=<val>, CHAIN-LINK-4.MISSING=<val>, CHAIN-LINK-4.CIRCULAR=<val>]
  Entry condition: all pathology subsections complete with verdict-first structure; CHAIN-LINK-4 emitted
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B (Remediation Coverage Analyst) — distinct from Role 4
```

⛔ **Gate 4→4B**: GATE-STATE-4→4B Status=CLOSED AND PASSAGE_KEY carries all three CHAIN-LINK-4 verdict keys before Phase 4B begins.

---

### Phase 4B — Remediation Coverage Analyst

**Independence declaration**: Remediation Coverage Analyst is distinct from Role 4 (verdict
producer) and Role 5 (Audit Analyst). Reads CHAIN-LINK-4 as a black-box input.
CHAIN-LINK-4B is the second independent terminal artifact.

For each charge with DETECTED or INDETERMINATE verdict (read from CHAIN-LINK-4):

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage |
|--------|-------------------------------------|-----------------|---------|---------|---------|----------|
| IF-Storm | [read CHAIN-LINK-4.STORM] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED / ORPHANED |

If ORPHANED: "⚠ CHARGE [label] ORPHANED — [reason]."

Emit **CHAIN-LINK-4B** verbatim:

```
CHAIN-LINK-4B (owner: Remediation Coverage Analyst — second independent terminal artifact)
REM_STORM=[COVERED | ORPHANED | N/A]   (read: CHAIN-LINK-4.STORM=<val>)
REM_MISSING=[COVERED | ORPHANED | N/A]  (read: CHAIN-LINK-4.MISSING=<val>)
REM_CIRCULAR=[COVERED | ORPHANED | N/A] (read: CHAIN-LINK-4.CIRCULAR=<val>)
ORPHANED_COUNT=[n] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all orphans acknowledged; NO otherwise]
```

Passage key declaration:

```
GATE_PASSAGE_KEY-4B→5:
  Justifying keys: CHAIN-LINK-4B.REM_STORM, CHAIN-LINK-4B.REM_MISSING, CHAIN-LINK-4B.REM_CIRCULAR
  Passage condition: coverage table complete; all orphaned charges flagged; CHAIN-LINK-4B.GATE_PASS declared
```

Emit **GATE-STATE-4B→5** verbatim:

```
GATE-STATE-4B→5:
  Owner: Remediation Coverage Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4B.REM_STORM=<val>, CHAIN-LINK-4B.REM_MISSING=<val>, CHAIN-LINK-4B.REM_CIRCULAR=<val>]
  Exit condition: CHAIN-LINK-4B emitted; GATE_PASS declared; all orphans acknowledged
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 (Audit Analyst) — distinct from Phase 4B
```

⛔ **Gate 4B→5**: GATE-STATE-4B→5 Status=CLOSED AND PASSAGE_KEY carries all three CHAIN-LINK-4B REM_* keys before Role 5 begins.

---

### Role 5 — Audit Analyst

**Independence declaration**: Role 5 (Audit Analyst) is distinct from (1) PCR Analyst
(prediction closure owner — distinct from Inertia Analyst), (2) Remediation Coverage Analyst
/ Phase 4B, and (3) Role 4 / Pathology Analyst (verdict producer). Reads all prior CHAIN-LINK
and GATE-STATE blocks as black-box inputs. Does not re-evaluate any upstream decision.

**Simulation Manifest Verification** — 21-slot audit

For each of the 14 artifact slots:
- EMITTED: block is present
- MANIFEST-GAP: `MANIFEST-GAP: [artifact] (expected owner: [owner], verifies: [condition], not emitted)`

For each of the 7 GATE-STATE slots that are EMITTED, additionally verify passage key:
- PASSAGE_KEY_POPULATED: PASSAGE_KEY field carries named key readbacks from preceding CHAIN-LINK
- PASSAGE-KEY-GAP: `PASSAGE-KEY-GAP: [gate] (expected readback from: [CHAIN-LINK-N keys], field absent or contains no named key reference)`

| Manifest slot | Presence | Passage key (gate slots only) |
|--------------|----------|-------------------------------|
| CHAIN-LINK-0 | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-1 | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-PCR | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-2 | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-3 | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-4 | EMITTED / MANIFEST-GAP | — |
| CHAIN-LINK-4B | EMITTED / MANIFEST-GAP | — |
| GATE-STATE-0→1 | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-1→PCR | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-PCR→2 | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-2→3 | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-3→4 | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-4→4B | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |
| GATE-STATE-4B→5 | EMITTED / MANIFEST-GAP | PASSAGE_KEY_POPULATED / PASSAGE-KEY-GAP |

Any MANIFEST-GAP drives a COLUMN-GAP in the certificate (the column sourced from that
CHAIN-LINK → `COLUMN-GAP: [column] for all rows — [CHAIN-LINK-N] absent`).

Emit this block verbatim with all values filled in:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from (1) PCR Analyst (prediction closure owner — distinct from
  Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4 / Pathology
  Analyst (verdict producer). Does not evaluate evidence, modify verdicts, or add analysis.
Manifest: canonical completeness check — replaces separate chain/gate integrity sections.

| Charge      | TC-1 annotation                                           | TC-2/TC-3 annotation                                                   | Forward mesh (PCR)                                               | Adjudication verdict                             | Remedy on record                                                |
|-------------|-----------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------|
| IF-Storm    | [n] <- named key ref: CHAIN-LINK-1.STORM_TC1             | TC2=[n], TC3=[n] <- named key refs: CHAIN-LINK-1.STORM_TC2, .STORM_TC3 | [val] <- named key ref: CHAIN-LINK-PCR.PCR_STORM                | [verdict] <- named key ref: CHAIN-LINK-4.STORM   | [val] <- named key ref: CHAIN-LINK-4B.REM_STORM                |
| IF-Missing  | [n] <- named key ref: CHAIN-LINK-1.MISSING_TC1           | TC2=[n], TC3=[n] <- named key refs: CHAIN-LINK-1.MISSING_TC2, .MISSING_TC3 | [val] <- named key ref: CHAIN-LINK-PCR.PCR_MISSING          | [verdict] <- named key ref: CHAIN-LINK-4.MISSING | [val] <- named key ref: CHAIN-LINK-4B.REM_MISSING              |
| IF-Circular | [n] <- named key ref: CHAIN-LINK-1.CIRCULAR_TC1          | TC2=[n], TC3=[n] <- named key refs: CHAIN-LINK-1.CIRCULAR_TC2, .CIRCULAR_TC3 | [val] <- named key ref: CHAIN-LINK-PCR.PCR_CIRCULAR       | [verdict] <- named key ref: CHAIN-LINK-4.CIRCULAR| [val] <- named key ref: CHAIN-LINK-4B.REM_CIRCULAR             |

Scoring dimensions:
  Manifest verification (canonical completeness check): all 14 slots EMITTED = PASS; any MANIFEST-GAP = FAIL
  Passage key audit: all 7 GATE-STATE slots PASSAGE_KEY_POPULATED = PASS; any PASSAGE-KEY-GAP = FAIL
  Budget gate key readback: CHAIN-LINK-3.TRIGGERED read from CHAIN-LINK-2.BUDGET_GATE (not self-evaluated)
  PCR independence: CHAIN-LINK-PCR owner (PCR Analyst) distinct from Inertia Analyst (prediction author)
  Full-column key refs: all five certificate columns carry named key refs; absent CHAIN-LINK → COLUMN-GAP

⚠ Audit flags: [list any MANIFEST-GAP, PASSAGE-KEY-GAP, or COLUMN-GAP; "none" if all 21 slots pass]
```

---
## V-02 — Output Format: Ownership Registry and OWNER-MISMATCH Audit

**Axis**: Output format — a header-level Ownership Registry table declares the expected owner
for each of the 14 simulation artifacts. Role 5's manifest verification gains a second audit
dimension: presence (MANIFEST-GAP, C-38) plus ownership (OWNER-MISMATCH for emitted artifacts
whose Owner field does not match the registry). The registry is structural — every artifact
has one expected owner, and Role 5 reports discrepancies without needing to reason about intent.

**Hypothesis**: C-36 detects absent gate artifacts. C-38 drives COLUMN-GAP from MANIFEST-GAP.
Neither detects an artifact emitted under the wrong authority — CHAIN-LINK-3 produced by
Pathology Analyst passes all presence checks. An Ownership Registry closes this: role
contamination becomes structurally detectable, named, and independently auditable.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating
which automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts and a header-level Ownership Registry. Complete
all blocks in order. Do not begin a block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change:         {{change}}
Power Platform environment: {{environment_name}}
Solution layer:             {{solution_layer}}
```

**Ownership Registry** — declared at header; Role 5 verifies Owner fields of all emitted
artifacts against this table.

| Artifact | Expected Owner |
|----------|---------------|
| CHAIN-LINK-0 | Inertia Analyst |
| CHAIN-LINK-1 | Threat Cataloger |
| CHAIN-LINK-PCR | PCR Analyst |
| CHAIN-LINK-2 | Registry Analyst |
| CHAIN-LINK-3 | Budget Analyst |
| CHAIN-LINK-4 | Pathology Analyst |
| CHAIN-LINK-4B | Remediation Coverage Analyst |
| GATE-STATE-0->1 | Inertia Analyst |
| GATE-STATE-1->PCR | Threat Cataloger |
| GATE-STATE-PCR->2 | PCR Analyst |
| GATE-STATE-2->3 | Registry Analyst |
| GATE-STATE-3->4 | Budget Analyst |
| GATE-STATE-4->4B | Pathology Analyst |
| GATE-STATE-4B->5 | Remediation Coverage Analyst |

**Simulation Manifest** — declared at header; Role 5 verifies all 14 slots.

```
SIMULATION MANIFEST
Chain-link slots (7): CHAIN-LINK-0, CHAIN-LINK-1, CHAIN-LINK-PCR,
                       CHAIN-LINK-2, CHAIN-LINK-3, CHAIN-LINK-4, CHAIN-LINK-4B
Gate-state slots (7): GATE-STATE-0->1, GATE-STATE-1->PCR, GATE-STATE-PCR->2,
                       GATE-STATE-2->3, GATE-STATE-3->4, GATE-STATE-4->4B, GATE-STATE-4B->5
```

---

### Role 0 — Inertia Analyst

**Mandate**: Prosecution Theories and CHAIN-LINK-0. No downstream involvement.

| Charge | Why this change creates this risk | Predicted TC-2 | Predicted TC-3 |
|--------|----------------------------------|----------------|----------------|
| IF-Storm | [why] | [anticipated chains or "none anticipated"] | [side effects or "none anticipated"] |
| IF-Missing | [why] | [absent paths or "none anticipated"] | [absent effects or "none anticipated"] |
| IF-Circular | [why] | [re-entrant chains or "none anticipated"] | [circular effects or "none anticipated"] |

Emit CHAIN-LINK-0:

```
CHAIN-LINK-0 (owner: Inertia Analyst)
ENV={{environment_name}} | LAYER={{solution_layer}}
MESH_STORM=[RISK|NO-RISK] | MESH_MISSING=[RISK|NO-RISK] | MESH_CIRCULAR=[RISK|NO-RISK]
STORM_TC2_PRED=[n] | STORM_TC3_PRED=[n]
MISSING_TC2_PRED=[n] | MISSING_TC3_PRED=[n]
CIRCULAR_TC2_PRED=[n] | CIRCULAR_TC3_PRED=[n]
```

Emit GATE-STATE-0->1:

```
GATE-STATE-0->1:
  Owner: Inertia Analyst
  Condition: prosecution table complete; CHAIN-LINK-0 emitted
  Status: [OPEN | CLOSED]
```

Gate 0->1: Status=CLOSED before Role 1 begins.

---

### Role 1 — Threat Cataloger

TC-1, TC-2, TC-3, Mesh Completeness Check, and CHAIN-LINK-1.

TC-1: Automation | Condition | YES/NO | IF-* annotation (required; "IF-none" is the null) | Notes

TC-2: # | Cascade chain | IF-* label | Prosecution status (Confirmed / Not confirmed) | Notes

TC-3: # | Side effect | IF-* label | Prosecution status | Reversible?

Mesh Completeness Check: IF-Storm [TC-1 n, TC-2 n, TC-3 n, COMPLETE/ORPHANED]; same for IF-Missing, IF-Circular.

Emit CHAIN-LINK-1:

```
CHAIN-LINK-1 (owner: Threat Cataloger)
TC1=[n] | TC2=[n] | TC3=[n]
STORM_TC1=[n] | STORM_TC2=[n] | STORM_TC3=[n]
MISSING_TC1=[n] | MISSING_TC2=[n] | MISSING_TC3=[n]
CIRCULAR_TC1=[n] | CIRCULAR_TC2=[n] | CIRCULAR_TC3=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
PRED_CONFIRMED=[n] | PRED_FLAGGED=[n]
```

Emit GATE-STATE-1->PCR:

```
GATE-STATE-1->PCR:
  Owner: Threat Cataloger
  Condition: TC-1/TC-2/TC-3 complete; IF-* on every row; mesh check; CHAIN-LINK-1 emitted
  Status: [OPEN | CLOSED]
```

Gate 1->PCR: Status=CLOSED before PCR Analyst begins.

---

### PCR Analyst — Prosecution Closure Report

**Independence declaration**: Explicitly distinct from (1) Inertia Analyst (prediction author),
(2) Registry Analyst, (3) Pathology Analyst, (4) Remediation Coverage Analyst / Phase 4B,
(5) Audit Analyst. CHAIN-LINK-PCR is the first independent terminal artifact.

Emit CHAIN-LINK-PCR:

```
CHAIN-LINK-PCR (owner: PCR Analyst — first independent terminal artifact)
PCR_STORM=[CLOSED|INDETERMINATE|NULL]   (read: CHAIN-LINK-0.STORM_*_PRED vs CHAIN-LINK-1.STORM_*)
PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
SILENT_GAPS_STORM=[n] | SILENT_GAPS_MISSING=[n] | SILENT_GAPS_CIRCULAR=[n]
```

Emit GATE-STATE-PCR->2:

```
GATE-STATE-PCR->2:
  Owner: PCR Analyst
  Condition: CHAIN-LINK-PCR emitted with all PCR_* keys
  Status: [OPEN | CLOSED]
```

Gate PCR->2: Status=CLOSED before Role 2 begins.

---

### Role 2 — Registry Analyst

Trigger table (read CHAIN-LINK-1.TC1=[n] to verify count):

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int or --] | [name] | [ref] | YES or NO | [in] | [out] | [ref or "none"] |

Emit CHAIN-LINK-2:

```
CHAIN-LINK-2 (owner: Registry Analyst)
M=[n] | N=[n] | NON_FIRING=[n]
BUDGET_GATE=[TRIGGERED|WAIVED]
```

Emit GATE-STATE-2->3:

```
GATE-STATE-2->3:
  Owner: Registry Analyst
  Condition: trigger table complete; CHAIN-LINK-2 with M, N, BUDGET_GATE
  Status: [OPEN | CLOSED]
```

Gate 2->3: Status=CLOSED before Role 3 begins.

---

### Role 3 — Budget Analyst

Read CHAIN-LINK-2.BUDGET_GATE — do not re-evaluate.

```
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated
```

If WAIVED: "Budget Gate: WAIVED — M=[read CHAIN-LINK-2.M]."

If TRIGGERED: per-automation action count + total requests + daily limit + budget % + run duration (X to Y seconds, specific span required).

Emit CHAIN-LINK-3:

```
CHAIN-LINK-3 (owner: Budget Analyst)
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback
TOTAL_REQ=[n|N/A] | DAILY_LIMIT=[n|N/A] | BUDGET_PCT=[pct|N/A] | DURATION=[X to Y s|N/A]
```

Emit GATE-STATE-3->4:

```
GATE-STATE-3->4:
  Owner: Budget Analyst
  Condition: CHAIN-LINK-3 emitted; TRIGGERED carries key readback from CHAIN-LINK-2.BUDGET_GATE
  Status: [OPEN | CLOSED]
```

Gate 3->4: Status=CLOSED before Role 4 begins.

---

### Role 4 — Pathology Analyst

Verdict keyword first on its own line. Three-layer remediation for DETECTED or INDETERMINATE.

**Trigger Storm (IF-Storm)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 IF-Storm (CHAIN-LINK-1.STORM_TC2); M/N (CHAIN-LINK-2); PCR_STORM (CHAIN-LINK-PCR)
Remediation if applicable: Layer 1 (construct); Layer 2 (TC entry); Layer 3 (IF-Storm closed)

**Missing Trigger (IF-Missing)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-3 IF-Missing (CHAIN-LINK-1.MISSING_TC3); TC-1 annotations; PCR_MISSING (CHAIN-LINK-PCR)
Remediation if applicable: Layer 1; Layer 2; Layer 3 (IF-Missing closed)

**Circular Trigger (IF-Circular)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 IF-Circular (CHAIN-LINK-1.CIRCULAR_TC2); TC-1 annotations; PCR_CIRCULAR (CHAIN-LINK-PCR)
Remediation if applicable: Layer 1; Layer 2; Layer 3 (IF-Circular closed)

Emit CHAIN-LINK-4:

```
CHAIN-LINK-4 (owner: Pathology Analyst)
STORM=[verdict] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[n] | REM_REQUIRED=[n]
```

Emit GATE-STATE-4->4B:

```
GATE-STATE-4->4B:
  Owner: Pathology Analyst
  Entry condition: all three pathology subsections complete; CHAIN-LINK-4 emitted
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B (Remediation Coverage Analyst) — distinct from Role 4
```

Gate 4->4B: Status=CLOSED before Phase 4B begins.

---

### Phase 4B — Remediation Coverage Analyst

**Independence declaration**: Distinct from Role 4 and Role 5. Reads CHAIN-LINK-4 as black-box.
CHAIN-LINK-4B is the second independent terminal artifact.

| Charge | Verdict (read CHAIN-LINK-4) | Remedy? | L1? | L2? | L3? | Coverage |
|--------|----------------------------|---------|-----|-----|-----|----------|
| IF-Storm | [read CHAIN-LINK-4.STORM] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |

Emit CHAIN-LINK-4B:

```
CHAIN-LINK-4B (owner: Remediation Coverage Analyst — second independent terminal artifact)
REM_STORM=[COVERED|ORPHANED|N/A]   (read: CHAIN-LINK-4.STORM)
REM_MISSING=[COVERED|ORPHANED|N/A]  (read: CHAIN-LINK-4.MISSING)
REM_CIRCULAR=[COVERED|ORPHANED|N/A] (read: CHAIN-LINK-4.CIRCULAR)
ORPHANED_COUNT=[n] | GATE_PASS=[YES|NO]
```

Emit GATE-STATE-4B->5:

```
GATE-STATE-4B->5:
  Owner: Remediation Coverage Analyst
  Exit condition: CHAIN-LINK-4B emitted; GATE_PASS declared; orphans acknowledged
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 (Audit Analyst) — distinct from Phase 4B
```

Gate 4B->5: Status=CLOSED before Role 5 begins.

---

### Role 5 — Audit Analyst

**Independence declaration**: Distinct from (1) PCR Analyst (prediction closure owner —
distinct from Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4
/ Pathology Analyst (verdict producer). Does not re-evaluate any upstream decision.

**Simulation Manifest Verification** — 14-slot audit with Ownership Registry cross-check

For each slot:
- EMITTED or MANIFEST-GAP: `MANIFEST-GAP: [artifact] (expected owner: [from registry], not emitted)`
- For EMITTED slots: OWNER_VERIFIED or OWNER-MISMATCH: `OWNER-MISMATCH: [artifact] (declared: [owner in block], expected: [owner in registry])`

| Manifest slot | Presence | Owner verification |
|--------------|----------|--------------------|
| CHAIN-LINK-0 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-1 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-PCR | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-2 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-3 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-4 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| CHAIN-LINK-4B | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-0->1 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-1->PCR | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-PCR->2 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-2->3 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-3->4 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-4->4B | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |
| GATE-STATE-4B->5 | EMITTED / MANIFEST-GAP | OWNER_VERIFIED / OWNER-MISMATCH |

Any MANIFEST-GAP drives a COLUMN-GAP in the certificate.

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from (1) PCR Analyst (prediction closure owner — distinct from
  Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4 / Pathology
  Analyst (verdict producer).
Manifest: canonical completeness check (replaces separate chain/gate integrity sections).
Ownership Registry: declared at simulation header — all 14 artifacts cross-checked.

| Charge      | TC-1 annotation                           | TC-2/TC-3 annotation                                     | Forward mesh (PCR)                         | Adjudication verdict                   | Remedy on record                          |
|-------------|-------------------------------------------|----------------------------------------------------------|---------------------------------------------|----------------------------------------|-------------------------------------------|
| IF-Storm    | [n] <- key ref: CHAIN-LINK-1.STORM_TC1   | TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.STORM_TC2,.STORM_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_STORM | [val] <- key ref: CHAIN-LINK-4.STORM  | [val] <- key ref: CHAIN-LINK-4B.REM_STORM |
| IF-Missing  | [n] <- key ref: CHAIN-LINK-1.MISSING_TC1 | TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.MISSING_TC2,.MISSING_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_MISSING | [val] <- key ref: CHAIN-LINK-4.MISSING | [val] <- key ref: CHAIN-LINK-4B.REM_MISSING |
| IF-Circular | [n] <- key ref: CHAIN-LINK-1.CIRCULAR_TC1| TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.CIRCULAR_TC2,.CIRCULAR_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR | [val] <- key ref: CHAIN-LINK-4.CIRCULAR | [val] <- key ref: CHAIN-LINK-4B.REM_CIRCULAR |

Scoring dimensions:
  Manifest verification: all 14 slots EMITTED = PASS; any MANIFEST-GAP = FAIL
  Ownership audit: all emitted slots OWNER_VERIFIED = PASS; any OWNER-MISMATCH = FAIL
  Budget gate key readback: CHAIN-LINK-3.TRIGGERED read from CHAIN-LINK-2.BUDGET_GATE
  PCR independence: CHAIN-LINK-PCR owner (PCR Analyst) distinct from Inertia Analyst
  Full-column key refs: all five columns carry named key refs; absent CHAIN-LINK -> COLUMN-GAP

Audit flags: [list any MANIFEST-GAP, OWNER-MISMATCH, or COLUMN-GAP; "none" if all pass]
```

---
## V-03 — Lifecycle Emphasis: Manifest Derivation Proof

**Axis**: Lifecycle emphasis — the simulation manifest carries a derivation proof declaring
why there are 14 slots, not just that there are 14. The proof is a named lifecycle header
phase: Role_Count=7 named roles each produce one CHAIN-LINK, so 7 chain-link slots;
Gate_Count=7 named transitions between the 8 lifecycle phases, so 7 gate-state slots;
Total=14. Role 5 verifies the arithmetic before proceeding to slot verification. A manifest
with a hardcoded "/14" that is not derived from role/gate counts satisfies C-38 but fails
the derivation proof criterion.

**Hypothesis**: C-38 formalizes the manifest as the completeness source but the denominator
is implicit — if the simulation were extended with a new role, the manifest would need manual
updating with no structural indicator that the count changed. A derivation proof makes the
manifest self-validating: the number of slots is a theorem from the role/gate declaration,
not a constant. Role 5 can detect a manifest whose denominator doesn't match the declared
role and gate counts — a manifest misconfiguration becomes a named audit failure.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating
which automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts and a manifest derivation proof. Complete all
blocks in order. Do not begin a block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change:         {{change}}
Power Platform environment: {{environment_name}}
Solution layer:             {{solution_layer}}
```

**Simulation Manifest with Derivation Proof** — declared at header; Role 5 verifies
derivation arithmetic, then verifies all 14 slots.

```
SIMULATION MANIFEST — DERIVATION PROOF
Declared roles (7):
  1. Inertia Analyst      -> CHAIN-LINK-0
  2. Threat Cataloger     -> CHAIN-LINK-1
  3. PCR Analyst          -> CHAIN-LINK-PCR
  4. Registry Analyst     -> CHAIN-LINK-2
  5. Budget Analyst       -> CHAIN-LINK-3
  6. Pathology Analyst    -> CHAIN-LINK-4
  7. Remediation Coverage Analyst -> CHAIN-LINK-4B
CHAIN_LINK_SLOTS = ROLE_COUNT = 7

Declared gate transitions (7):
  1. 0->1       (Inertia Analyst -> Threat Cataloger)
  2. 1->PCR     (Threat Cataloger -> PCR Analyst)
  3. PCR->2     (PCR Analyst -> Registry Analyst)
  4. 2->3       (Registry Analyst -> Budget Analyst)
  5. 3->4       (Budget Analyst -> Pathology Analyst)
  6. 4->4B      (Pathology Analyst -> Remediation Coverage Analyst)
  7. 4B->5      (Remediation Coverage Analyst -> Audit Analyst)
GATE_STATE_SLOTS = GATE_COUNT = 7

TOTAL_SLOTS = CHAIN_LINK_SLOTS + GATE_STATE_SLOTS = 7 + 7 = 14
MANIFEST_DENOMINATOR = /14

Chain-link slots: CHAIN-LINK-0, CHAIN-LINK-1, CHAIN-LINK-PCR,
                  CHAIN-LINK-2, CHAIN-LINK-3, CHAIN-LINK-4, CHAIN-LINK-4B
Gate-state slots: GATE-STATE-0->1, GATE-STATE-1->PCR, GATE-STATE-PCR->2,
                  GATE-STATE-2->3, GATE-STATE-3->4, GATE-STATE-4->4B, GATE-STATE-4B->5
```

Role 5 must verify: ROLE_COUNT=7, GATE_COUNT=7, TOTAL_SLOTS=14 before proceeding
to slot verification. A DERIVATION-MISMATCH occurs if the manifest denominator does
not equal ROLE_COUNT + GATE_COUNT.

---

### Role 0 — Inertia Analyst

**Mandate**: Prosecution Theories and CHAIN-LINK-0. No downstream involvement.

| Charge | Why this change creates this risk | Predicted TC-2 | Predicted TC-3 |
|--------|----------------------------------|----------------|----------------|
| IF-Storm | [why] | [chains or "none anticipated"] | [side effects or "none anticipated"] |
| IF-Missing | [why] | [absent paths or "none anticipated"] | [absent effects or "none anticipated"] |
| IF-Circular | [why] | [re-entrant chains or "none anticipated"] | [circular effects or "none anticipated"] |

Emit CHAIN-LINK-0:

```
CHAIN-LINK-0 (owner: Inertia Analyst)
ENV={{environment_name}} | LAYER={{solution_layer}}
MESH_STORM=[RISK|NO-RISK] | MESH_MISSING=[RISK|NO-RISK] | MESH_CIRCULAR=[RISK|NO-RISK]
STORM_TC2_PRED=[n] | STORM_TC3_PRED=[n]
MISSING_TC2_PRED=[n] | MISSING_TC3_PRED=[n]
CIRCULAR_TC2_PRED=[n] | CIRCULAR_TC3_PRED=[n]
```

Emit GATE-STATE-0->1:

```
GATE-STATE-0->1:
  Owner: Inertia Analyst
  Condition: prosecution table complete; CHAIN-LINK-0 emitted (slot 1 of 7 chain-links filled)
  Status: [OPEN | CLOSED]
```

Gate 0->1: Status=CLOSED before Role 1 begins.

---

### Role 1 — Threat Cataloger

TC-1, TC-2, TC-3, Mesh Completeness Check, and CHAIN-LINK-1.

TC-1: Automation | Condition | YES/NO | IF-* annotation (required) | Notes

TC-2: # | Cascade chain | IF-* label | Prosecution status | Notes

TC-3: # | Side effect | IF-* label | Prosecution status | Reversible?

Mesh Completeness Check: IF-Storm/Missing/Circular each with TC-1/TC-2/TC-3 counts and COMPLETE/ORPHANED status.

Emit CHAIN-LINK-1:

```
CHAIN-LINK-1 (owner: Threat Cataloger)
TC1=[n] | TC2=[n] | TC3=[n]
STORM_TC1=[n] | STORM_TC2=[n] | STORM_TC3=[n]
MISSING_TC1=[n] | MISSING_TC2=[n] | MISSING_TC3=[n]
CIRCULAR_TC1=[n] | CIRCULAR_TC2=[n] | CIRCULAR_TC3=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
PRED_CONFIRMED=[n] | PRED_FLAGGED=[n]
```

Emit GATE-STATE-1->PCR:

```
GATE-STATE-1->PCR:
  Owner: Threat Cataloger
  Condition: TC sections complete; IF-* on every row; mesh check; CHAIN-LINK-1 emitted (slot 2/7)
  Status: [OPEN | CLOSED]
```

Gate 1->PCR: Status=CLOSED before PCR Analyst begins.

---

### PCR Analyst — Prosecution Closure Report

**Independence declaration**: Distinct from (1) Inertia Analyst (prediction author),
(2) Registry Analyst, (3) Pathology Analyst, (4) Remediation Coverage Analyst / Phase 4B,
(5) Audit Analyst. CHAIN-LINK-PCR is the first independent terminal artifact.

Emit CHAIN-LINK-PCR:

```
CHAIN-LINK-PCR (owner: PCR Analyst — first independent terminal artifact)
PCR_STORM=[CLOSED|INDETERMINATE|NULL]   (read: CHAIN-LINK-0.STORM_*_PRED vs CHAIN-LINK-1.STORM_*)
PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
SILENT_GAPS_STORM=[n] | SILENT_GAPS_MISSING=[n] | SILENT_GAPS_CIRCULAR=[n]
```

Emit GATE-STATE-PCR->2:

```
GATE-STATE-PCR->2:
  Owner: PCR Analyst
  Condition: CHAIN-LINK-PCR emitted with all PCR_* keys (slot 3/7 chain-links filled)
  Status: [OPEN | CLOSED]
```

Gate PCR->2: Status=CLOSED before Role 2 begins.

---

### Role 2 — Registry Analyst

Trigger table; then CHAIN-LINK-2.

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int or --] | [name] | [ref] | YES or NO | [in] | [out] | [ref or "none"] |

Emit CHAIN-LINK-2:

```
CHAIN-LINK-2 (owner: Registry Analyst)
M=[n] | N=[n] | NON_FIRING=[n]
BUDGET_GATE=[TRIGGERED|WAIVED]
```

Emit GATE-STATE-2->3:

```
GATE-STATE-2->3:
  Owner: Registry Analyst
  Condition: trigger table complete; CHAIN-LINK-2 emitted with M, N, BUDGET_GATE (slot 4/7)
  Status: [OPEN | CLOSED]
```

Gate 2->3: Status=CLOSED before Role 3 begins.

---

### Role 3 — Budget Analyst

Read CHAIN-LINK-2.BUDGET_GATE — key readback, not self-evaluated.

If WAIVED: "Budget Gate: WAIVED — M=[read CHAIN-LINK-2.M]."

If TRIGGERED: per-automation action count + total + limit + % + duration (X to Y seconds).

Emit CHAIN-LINK-3:

```
CHAIN-LINK-3 (owner: Budget Analyst)
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated
TOTAL_REQ=[n|N/A] | DAILY_LIMIT=[n|N/A] | BUDGET_PCT=[pct|N/A] | DURATION=[X to Y s|N/A]
```

Emit GATE-STATE-3->4:

```
GATE-STATE-3->4:
  Owner: Budget Analyst
  Condition: CHAIN-LINK-3 emitted; TRIGGERED carries key readback (slot 5/7)
  Status: [OPEN | CLOSED]
```

Gate 3->4: Status=CLOSED before Role 4 begins.

---

### Role 4 — Pathology Analyst

Verdict first on its own line. Three-layer remediation for DETECTED or INDETERMINATE.

**Trigger Storm (IF-Storm)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 (CHAIN-LINK-1.STORM_TC2); M/N (CHAIN-LINK-2); PCR_STORM (CHAIN-LINK-PCR)
Remediation: Layer 1 (construct); Layer 2 (TC entry); Layer 3 (IF-Storm closed)

**Missing Trigger (IF-Missing)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-3 (CHAIN-LINK-1.MISSING_TC3); TC-1 annotations; PCR_MISSING (CHAIN-LINK-PCR)
Remediation: Layer 1; Layer 2; Layer 3 (IF-Missing closed)

**Circular Trigger (IF-Circular)**
VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 (CHAIN-LINK-1.CIRCULAR_TC2); TC-1 annotations; PCR_CIRCULAR (CHAIN-LINK-PCR)
Remediation: Layer 1; Layer 2; Layer 3 (IF-Circular closed)

Emit CHAIN-LINK-4:

```
CHAIN-LINK-4 (owner: Pathology Analyst)
STORM=[verdict] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[n] | REM_REQUIRED=[n]
```

Emit GATE-STATE-4->4B:

```
GATE-STATE-4->4B:
  Owner: Pathology Analyst
  Entry condition: all three pathology verdicts; CHAIN-LINK-4 emitted (slot 6/7)
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B (Remediation Coverage Analyst) — distinct from Role 4
```

Gate 4->4B: Status=CLOSED before Phase 4B begins.

---

### Phase 4B — Remediation Coverage Analyst

**Independence declaration**: Distinct from Role 4 and Role 5. Reads CHAIN-LINK-4 as black-box.
CHAIN-LINK-4B is the second independent terminal artifact.

| Charge | Verdict (read CHAIN-LINK-4) | Remedy? | L1? | L2? | L3? | Coverage |
|--------|----------------------------|---------|-----|-----|-----|----------|
| IF-Storm | [read CHAIN-LINK-4.STORM] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES/NO | YES/NO | YES/NO | YES/NO | COVERED/ORPHANED |

Emit CHAIN-LINK-4B:

```
CHAIN-LINK-4B (owner: Remediation Coverage Analyst — second independent terminal artifact)
REM_STORM=[COVERED|ORPHANED|N/A]   (read: CHAIN-LINK-4.STORM)
REM_MISSING=[COVERED|ORPHANED|N/A]  (read: CHAIN-LINK-4.MISSING)
REM_CIRCULAR=[COVERED|ORPHANED|N/A] (read: CHAIN-LINK-4.CIRCULAR)
ORPHANED_COUNT=[n] | GATE_PASS=[YES|NO]
```

Emit GATE-STATE-4B->5:

```
GATE-STATE-4B->5:
  Owner: Remediation Coverage Analyst
  Exit condition: CHAIN-LINK-4B emitted; GATE_PASS declared; orphans acknowledged (slot 7/7)
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 (Audit Analyst) — distinct from Phase 4B
```

Gate 4B->5: Status=CLOSED before Role 5 begins.

---

### Role 5 — Audit Analyst

**Independence declaration**: Distinct from (1) PCR Analyst (prediction closure owner —
distinct from Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4
/ Pathology Analyst (verdict producer). Does not re-evaluate any upstream decision.

**Derivation Proof Verification** — verify before slot verification:

```
DERIVATION VERIFICATION (owner: Audit Analyst)
ROLE_COUNT_DECLARED=7 | CHAIN_LINK_SLOTS_DERIVED=7 (= ROLE_COUNT)
GATE_COUNT_DECLARED=7 | GATE_STATE_SLOTS_DERIVED=7 (= GATE_COUNT)
TOTAL_SLOTS_DERIVED=14 (= CHAIN_LINK_SLOTS + GATE_STATE_SLOTS)
MANIFEST_DENOMINATOR_DECLARED=/14
DERIVATION_CHECK=[PASS — derived total matches declared denominator | DERIVATION-MISMATCH — [detail]]
```

**Simulation Manifest Verification** — 14-slot audit (proceed only after derivation PASS)

For each slot: EMITTED or MANIFEST-GAP: `MANIFEST-GAP: [artifact] (expected owner: [owner], verifies: [condition], not emitted)`

| Manifest slot | Status |
|--------------|--------|
| CHAIN-LINK-0 | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-1 | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-PCR | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-2 | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-3 | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-4 | EMITTED / MANIFEST-GAP |
| CHAIN-LINK-4B | EMITTED / MANIFEST-GAP |
| GATE-STATE-0->1 | EMITTED / MANIFEST-GAP |
| GATE-STATE-1->PCR | EMITTED / MANIFEST-GAP |
| GATE-STATE-PCR->2 | EMITTED / MANIFEST-GAP |
| GATE-STATE-2->3 | EMITTED / MANIFEST-GAP |
| GATE-STATE-3->4 | EMITTED / MANIFEST-GAP |
| GATE-STATE-4->4B | EMITTED / MANIFEST-GAP |
| GATE-STATE-4B->5 | EMITTED / MANIFEST-GAP |

Any MANIFEST-GAP drives a COLUMN-GAP in the certificate.

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from (1) PCR Analyst (prediction closure owner — distinct from
  Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4 / Pathology
  Analyst (verdict producer).
Manifest: canonical completeness check (replaces separate chain/gate integrity sections).
Derivation proof: ROLE_COUNT=7, GATE_COUNT=7, TOTAL=14 — manifest denominator structurally derived.

| Charge      | TC-1 annotation                           | TC-2/TC-3 annotation                                     | Forward mesh (PCR)                         | Adjudication verdict                   | Remedy on record                          |
|-------------|-------------------------------------------|----------------------------------------------------------|---------------------------------------------|----------------------------------------|-------------------------------------------|
| IF-Storm    | [n] <- key ref: CHAIN-LINK-1.STORM_TC1   | TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.STORM_TC2,.STORM_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_STORM | [val] <- key ref: CHAIN-LINK-4.STORM  | [val] <- key ref: CHAIN-LINK-4B.REM_STORM |
| IF-Missing  | [n] <- key ref: CHAIN-LINK-1.MISSING_TC1 | TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.MISSING_TC2,.MISSING_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_MISSING | [val] <- key ref: CHAIN-LINK-4.MISSING | [val] <- key ref: CHAIN-LINK-4B.REM_MISSING |
| IF-Circular | [n] <- key ref: CHAIN-LINK-1.CIRCULAR_TC1| TC2=[n],TC3=[n] <- key refs: CHAIN-LINK-1.CIRCULAR_TC2,.CIRCULAR_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR | [val] <- key ref: CHAIN-LINK-4.CIRCULAR | [val] <- key ref: CHAIN-LINK-4B.REM_CIRCULAR |

Scoring dimensions:
  Derivation proof: ROLE_COUNT=7, GATE_COUNT=7, TOTAL=14 verified before slot check = PASS; DERIVATION-MISMATCH = FAIL
  Manifest verification: all 14 slots EMITTED = PASS; any MANIFEST-GAP = FAIL
  Budget gate key readback: CHAIN-LINK-3.TRIGGERED read from CHAIN-LINK-2.BUDGET_GATE
  PCR independence: CHAIN-LINK-PCR owner (PCR Analyst) distinct from Inertia Analyst
  Full-column key refs: all five columns carry named key refs; absent CHAIN-LINK -> COLUMN-GAP

Audit flags: [list any DERIVATION-MISMATCH, MANIFEST-GAP, or COLUMN-GAP; "none" if all pass]
```

---
## V-04 — Combined: Role Sequence + Output Format (Passage Keys + Ownership Registry)

**Axes**: Role sequence (V-01 gate passage key chain) + Output format (V-02 ownership registry
and OWNER-MISMATCH). Role 5 now performs a three-dimensional manifest audit: (1) presence
(MANIFEST-GAP for absent artifacts, C-38), (2) passage key population (PASSAGE-KEY-GAP for
emitted GATE-STATE blocks without a named key readback, V-01), and (3) ownership match
(OWNER-MISMATCH for emitted artifacts whose Owner field disagrees with the registry, V-02).

**Hypothesis**: V-01 and V-02 target independent structural gaps — V-01 closes the evidence
gap at gate transitions (a gate can close without citing justification); V-02 closes the
authority gap at every artifact (a block can claim the wrong owner without detection). Neither
depends on the other. Combining them gives Role 5 a richer audit surface: a simulation that
passes presence + passage key checks can still fail on ownership, and vice versa.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating
which automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts, passage key readbacks at every transition, and
a header-level Ownership Registry. Complete all blocks in order.

**Scenario boundary:**

```
Triggering change:         {{change}}
Power Platform environment: {{environment_name}}
Solution layer:             {{solution_layer}}
```

**Ownership Registry** — declared at header; Role 5 verifies Owner fields against this.

| Artifact | Expected Owner |
|----------|---------------|
| CHAIN-LINK-0 | Inertia Analyst |
| CHAIN-LINK-1 | Threat Cataloger |
| CHAIN-LINK-PCR | PCR Analyst |
| CHAIN-LINK-2 | Registry Analyst |
| CHAIN-LINK-3 | Budget Analyst |
| CHAIN-LINK-4 | Pathology Analyst |
| CHAIN-LINK-4B | Remediation Coverage Analyst |
| GATE-STATE-0->1 | Inertia Analyst |
| GATE-STATE-1->PCR | Threat Cataloger |
| GATE-STATE-PCR->2 | PCR Analyst |
| GATE-STATE-2->3 | Registry Analyst |
| GATE-STATE-3->4 | Budget Analyst |
| GATE-STATE-4->4B | Pathology Analyst |
| GATE-STATE-4B->5 | Remediation Coverage Analyst |

**Simulation Manifest** — declared at header; Role 5 verifies all 14 artifact slots plus
7 passage key slots (21 verification points).

```
SIMULATION MANIFEST
Chain-link slots (7): CHAIN-LINK-0, CHAIN-LINK-1, CHAIN-LINK-PCR,
                       CHAIN-LINK-2, CHAIN-LINK-3, CHAIN-LINK-4, CHAIN-LINK-4B
Gate-state slots (7): GATE-STATE-0->1, GATE-STATE-1->PCR, GATE-STATE-PCR->2,
                       GATE-STATE-2->3, GATE-STATE-3->4, GATE-STATE-4->4B, GATE-STATE-4B->5
Passage-key slots (7): one PASSAGE_KEY per GATE-STATE — each reads named key(s)
                        from the immediately preceding CHAIN-LINK
```

---

### Role 0 — Inertia Analyst

Prosecution Theories and CHAIN-LINK-0. No downstream involvement.

| Charge | Why this risk | Predicted TC-2 | Predicted TC-3 |
|--------|--------------|----------------|----------------|
| IF-Storm | [why] | [or "none anticipated"] | [or "none anticipated"] |
| IF-Missing | [why] | [or "none anticipated"] | [or "none anticipated"] |
| IF-Circular | [why] | [or "none anticipated"] | [or "none anticipated"] |

Emit CHAIN-LINK-0:

```
CHAIN-LINK-0 (owner: Inertia Analyst)
ENV={{environment_name}} | LAYER={{solution_layer}}
MESH_STORM=[RISK|NO-RISK] | MESH_MISSING=[RISK|NO-RISK] | MESH_CIRCULAR=[RISK|NO-RISK]
STORM_TC2_PRED=[n] | STORM_TC3_PRED=[n]
MISSING_TC2_PRED=[n] | MISSING_TC3_PRED=[n]
CIRCULAR_TC2_PRED=[n] | CIRCULAR_TC3_PRED=[n]
```

Emit GATE-STATE-0->1:

```
GATE-STATE-0->1:
  Owner: Inertia Analyst
  PASSAGE_KEY: [read CHAIN-LINK-0.MESH_STORM=<val>, CHAIN-LINK-0.MESH_MISSING=<val>, CHAIN-LINK-0.MESH_CIRCULAR=<val>]
  Condition: prosecution table complete; CHAIN-LINK-0 emitted with all MESH_* keys
  Status: [OPEN | CLOSED]
```

Gate 0->1: Status=CLOSED AND PASSAGE_KEY populated before Role 1 begins.

---

### Role 1 — Threat Cataloger

TC-1, TC-2, TC-3, Mesh Completeness Check, and CHAIN-LINK-1.

TC-1: Automation | Condition | YES/NO | IF-* annotation (required; IF-none is the null) | Notes

TC-2: # | Cascade chain | IF-* label | Prosecution status (Confirmed/Not confirmed) | Notes

TC-3: # | Side effect | IF-* label | Prosecution status | Reversible?

Mesh Completeness Check: IF-Storm/Missing/Circular [TC-1 n, TC-2 n, TC-3 n, COMPLETE/ORPHANED].

Emit CHAIN-LINK-1:

```
CHAIN-LINK-1 (owner: Threat Cataloger)
TC1=[n] | TC2=[n] | TC3=[n]
STORM_TC1=[n] | STORM_TC2=[n] | STORM_TC3=[n]
MISSING_TC1=[n] | MISSING_TC2=[n] | MISSING_TC3=[n]
CIRCULAR_TC1=[n] | CIRCULAR_TC2=[n] | CIRCULAR_TC3=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
PRED_CONFIRMED=[n] | PRED_FLAGGED=[n]
```

Emit GATE-STATE-1->PCR:

```
GATE-STATE-1->PCR:
  Owner: Threat Cataloger
  PASSAGE_KEY: [read CHAIN-LINK-1.TC1=<n>, CHAIN-LINK-1.MESH_STORM=<val>, CHAIN-LINK-1.MESH_MISSING=<val>, CHAIN-LINK-1.MESH_CIRCULAR=<val>]
  Condition: TC sections complete; IF-* on every row; mesh check; CHAIN-LINK-1 emitted
  Status: [OPEN | CLOSED]
```

Gate 1->PCR: Status=CLOSED AND PASSAGE_KEY populated before PCR Analyst begins.

---

### PCR Analyst — Prosecution Closure Report

**Independence declaration**: Distinct from (1) Inertia Analyst (prediction author),
(2) Registry Analyst, (3) Pathology Analyst, (4) Remediation Coverage Analyst / Phase 4B,
(5) Audit Analyst. CHAIN-LINK-PCR is the first independent terminal artifact.

Emit CHAIN-LINK-PCR:

```
CHAIN-LINK-PCR (owner: PCR Analyst — first independent terminal artifact)
PCR_STORM=[CLOSED|INDETERMINATE|NULL]   (read: CHAIN-LINK-0 vs CHAIN-LINK-1 prediction/confirmation counts)
PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
SILENT_GAPS_STORM=[n] | SILENT_GAPS_MISSING=[n] | SILENT_GAPS_CIRCULAR=[n]
```

Emit GATE-STATE-PCR->2:

```
GATE-STATE-PCR->2:
  Owner: PCR Analyst
  PASSAGE_KEY: [read CHAIN-LINK-PCR.PCR_STORM=<val>, CHAIN-LINK-PCR.PCR_MISSING=<val>, CHAIN-LINK-PCR.PCR_CIRCULAR=<val>]
  Condition: CHAIN-LINK-PCR emitted with all three PCR_* keys
  Status: [OPEN | CLOSED]
```

Gate PCR->2: Status=CLOSED AND PASSAGE_KEY populated before Role 2 begins.

---

### Role 2 — Registry Analyst

Trigger table; then CHAIN-LINK-2.

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int or --] | [name] | [ref] | YES or NO | [in] | [out] | [ref or "none"] |

Emit CHAIN-LINK-2:

```
CHAIN-LINK-2 (owner: Registry Analyst)
M=[n] | N=[n] | NON_FIRING=[n]
BUDGET_GATE=[TRIGGERED|WAIVED]
```

Emit GATE-STATE-2->3:

```
GATE-STATE-2->3:
  Owner: Registry Analyst
  PASSAGE_KEY: [read CHAIN-LINK-2.M=<val>, CHAIN-LINK-2.N=<val>, CHAIN-LINK-2.BUDGET_GATE=<val>]
  Condition: trigger table complete; CHAIN-LINK-2 emitted with M, N, BUDGET_GATE
  Status: [OPEN | CLOSED]
```

Gate 2->3: Status=CLOSED AND PASSAGE_KEY populated before Role 3 begins.

---

### Role 3 — Budget Analyst

Read CHAIN-LINK-2.BUDGET_GATE — key readback, not self-evaluated.

If WAIVED: emit waiver. If TRIGGERED: per-automation breakdown + total + limit + % + duration.

Emit CHAIN-LINK-3:

```
CHAIN-LINK-3 (owner: Budget Analyst)
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated
TOTAL_REQ=[n|N/A] | DAILY_LIMIT=[n|N/A] | BUDGET_PCT=[pct|N/A] | DURATION=[X to Y s|N/A]
```

Emit GATE-STATE-3->4:

```
GATE-STATE-3->4:
  Owner: Budget Analyst
  PASSAGE_KEY: [read CHAIN-LINK-3.TRIGGERED=<val> (from CHAIN-LINK-2.BUDGET_GATE), CHAIN-LINK-3.BUDGET_PCT=<val>]
  Condition: CHAIN-LINK-3 emitted; TRIGGERED carries key readback
  Status: [OPEN | CLOSED]
```

Gate 3->4: Status=CLOSED AND PASSAGE_KEY populated before Role 4 begins.

---

### Role 4 — Pathology Analyst

Verdict first on its own line. Three-layer remediation for DETECTED or INDETERMINATE.

**Trigger Storm**: VERDICT first; Evidence (TC-2 CHAIN-LINK-1, M/N CHAIN-LINK-2, PCR_STORM CHAIN-LINK-PCR); Remediation (L1 construct, L2 TC entry, L3 IF-Storm closed)

**Missing Trigger**: VERDICT first; Evidence (TC-3/TC-1 CHAIN-LINK-1, PCR_MISSING); Remediation (L1, L2, L3 IF-Missing closed)

**Circular Trigger**: VERDICT first; Evidence (TC-2/TC-1 CHAIN-LINK-1, PCR_CIRCULAR); Remediation (L1, L2, L3 IF-Circular closed)

Emit CHAIN-LINK-4:

```
CHAIN-LINK-4 (owner: Pathology Analyst)
STORM=[verdict] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[n] | REM_REQUIRED=[n]
```

Emit GATE-STATE-4->4B:

```
GATE-STATE-4->4B:
  Owner: Pathology Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4.STORM=<val>, CHAIN-LINK-4.MISSING=<val>, CHAIN-LINK-4.CIRCULAR=<val>]
  Entry condition: all three pathology verdicts present; CHAIN-LINK-4 emitted
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B (Remediation Coverage Analyst) — distinct from Role 4
```

Gate 4->4B: Status=CLOSED AND PASSAGE_KEY populated before Phase 4B begins.

---

### Phase 4B — Remediation Coverage Analyst

**Independence declaration**: Distinct from Role 4 and Role 5. Black-box read of CHAIN-LINK-4.
CHAIN-LINK-4B is the second independent terminal artifact.

Coverage table: Charge | Verdict (read CHAIN-LINK-4) | Remedy? | L1? | L2? | L3? | COVERED/ORPHANED

Emit CHAIN-LINK-4B:

```
CHAIN-LINK-4B (owner: Remediation Coverage Analyst — second independent terminal artifact)
REM_STORM=[COVERED|ORPHANED|N/A]   (read: CHAIN-LINK-4.STORM)
REM_MISSING=[COVERED|ORPHANED|N/A]  (read: CHAIN-LINK-4.MISSING)
REM_CIRCULAR=[COVERED|ORPHANED|N/A] (read: CHAIN-LINK-4.CIRCULAR)
ORPHANED_COUNT=[n] | GATE_PASS=[YES|NO]
```

Emit GATE-STATE-4B->5:

```
GATE-STATE-4B->5:
  Owner: Remediation Coverage Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4B.REM_STORM=<val>, CHAIN-LINK-4B.REM_MISSING=<val>, CHAIN-LINK-4B.REM_CIRCULAR=<val>]
  Exit condition: CHAIN-LINK-4B emitted; GATE_PASS declared; orphans acknowledged
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 — distinct from Phase 4B
```

Gate 4B->5: Status=CLOSED AND PASSAGE_KEY populated before Role 5 begins.

---

### Role 5 — Audit Analyst

**Independence declaration**: Distinct from (1) PCR Analyst (prediction closure owner —
distinct from Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4
/ Pathology Analyst (verdict producer).

**Simulation Manifest Verification** — 21-slot audit (14 presence + 7 passage key)
plus Ownership Registry cross-check on all emitted artifacts.

For each slot:
- Presence: EMITTED or MANIFEST-GAP
- Ownership (EMITTED only): OWNER_VERIFIED or OWNER-MISMATCH: `OWNER-MISMATCH: [artifact] (declared: [role], expected: [role from registry])`
- Passage key (GATE-STATE EMITTED only): PASSAGE_KEY_POPULATED or PASSAGE-KEY-GAP

| Manifest slot | Presence | Owner | Passage key |
|--------------|----------|-------|-------------|
| CHAIN-LINK-0 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-1 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-PCR | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-2 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-3 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-4 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-4B | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| GATE-STATE-0->1 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-1->PCR | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-PCR->2 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-2->3 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-3->4 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-4->4B | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-4B->5 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |

Any MANIFEST-GAP drives a COLUMN-GAP in the certificate.

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from (1) PCR Analyst (prediction closure owner — distinct from
  Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4 / Pathology
  Analyst (verdict producer).
Manifest: canonical completeness check (replaces separate chain/gate integrity sections).
Ownership Registry: declared at simulation header — all 14 artifacts cross-checked.

| Charge      | TC-1 annotation                           | TC-2/TC-3 annotation                                     | Forward mesh (PCR)                         | Adjudication verdict                   | Remedy on record                          |
|-------------|-------------------------------------------|----------------------------------------------------------|---------------------------------------------|----------------------------------------|-------------------------------------------|
| IF-Storm    | [n] <- key ref: CHAIN-LINK-1.STORM_TC1   | TC2=[n],TC3=[n] <- key refs: .STORM_TC2,.STORM_TC3       | [val] <- key ref: CHAIN-LINK-PCR.PCR_STORM | [val] <- key ref: CHAIN-LINK-4.STORM  | [val] <- key ref: CHAIN-LINK-4B.REM_STORM |
| IF-Missing  | [n] <- key ref: CHAIN-LINK-1.MISSING_TC1 | TC2=[n],TC3=[n] <- key refs: .MISSING_TC2,.MISSING_TC3   | [val] <- key ref: CHAIN-LINK-PCR.PCR_MISSING| [val] <- key ref: CHAIN-LINK-4.MISSING| [val] <- key ref: CHAIN-LINK-4B.REM_MISSING|
| IF-Circular | [n] <- key ref: CHAIN-LINK-1.CIRCULAR_TC1| TC2=[n],TC3=[n] <- key refs: .CIRCULAR_TC2,.CIRCULAR_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR| [val] <- key ref: CHAIN-LINK-4.CIRCULAR| [val] <- key ref: CHAIN-LINK-4B.REM_CIRCULAR|

Scoring dimensions:
  Manifest verification: all 14 slots EMITTED = PASS; any MANIFEST-GAP = FAIL
  Ownership audit: all emitted slots OWNER_VERIFIED = PASS; any OWNER-MISMATCH = FAIL
  Passage key audit: all 7 GATE-STATE slots PASSAGE_KEY_POPULATED = PASS; any PASSAGE-KEY-GAP = FAIL
  Budget gate key readback: CHAIN-LINK-3.TRIGGERED read from CHAIN-LINK-2.BUDGET_GATE
  PCR independence: CHAIN-LINK-PCR owner (PCR Analyst) distinct from Inertia Analyst
  Full-column key refs: all five columns carry named key refs; absent CHAIN-LINK -> COLUMN-GAP

Audit flags: [list any MANIFEST-GAP, OWNER-MISMATCH, PASSAGE-KEY-GAP, or COLUMN-GAP; "none" if all pass]
```

---

## V-05 — Combined: All Three + Inertia Framing

**Axes**: Role sequence (V-01) + Output format (V-02) + Lifecycle emphasis (V-03) + Inertia
framing. Each new structural section carries an explicit note on what the status-quo design
misses — making the inertia cost visible at the point where the structural gap would otherwise
be silent.

**Inertia framing convention**: each new structural element opens with a brief *(Status quo:
[what the un-augmented design leaves undetectable])* declaration. This registers the gap
before the mechanism that closes it, so the role of each new protocol is traceable to a
specific failure mode rather than appearing as arbitrary overhead.

**Hypothesis**: Combining all three structural signals plus inertia framing produces the
highest-conformance single prompt: passage key chain closes unjustified gate closures;
ownership registry closes role contamination; manifest derivation proof closes implicit
denominator drift; inertia framing makes each closure's value legible. The four mechanisms
are orthogonal — each closes a gap the others leave open.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating
which automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts, passage key readbacks at every transition, a
header-level Ownership Registry, and a manifest derivation proof. Complete all blocks in order.

**Scenario boundary:**

```
Triggering change:         {{change}}
Power Platform environment: {{environment_name}}
Solution layer:             {{solution_layer}}
```

**Ownership Registry** — *(Status quo: absent; without this, an artifact emitted under the
wrong role authority passes all manifest presence checks with no audit flag.)*

| Artifact | Expected Owner |
|----------|---------------|
| CHAIN-LINK-0 | Inertia Analyst |
| CHAIN-LINK-1 | Threat Cataloger |
| CHAIN-LINK-PCR | PCR Analyst |
| CHAIN-LINK-2 | Registry Analyst |
| CHAIN-LINK-3 | Budget Analyst |
| CHAIN-LINK-4 | Pathology Analyst |
| CHAIN-LINK-4B | Remediation Coverage Analyst |
| GATE-STATE-0->1 | Inertia Analyst |
| GATE-STATE-1->PCR | Threat Cataloger |
| GATE-STATE-PCR->2 | PCR Analyst |
| GATE-STATE-2->3 | Registry Analyst |
| GATE-STATE-3->4 | Budget Analyst |
| GATE-STATE-4->4B | Pathology Analyst |
| GATE-STATE-4B->5 | Remediation Coverage Analyst |

**Simulation Manifest with Derivation Proof** — *(Status quo: denominator hardcoded; without
derivation proof, a manifest with a wrong slot count is undetectable until Role 5 lists gaps.)*

```
SIMULATION MANIFEST — DERIVATION PROOF
Declared roles (7): Inertia Analyst, Threat Cataloger, PCR Analyst, Registry Analyst,
                    Budget Analyst, Pathology Analyst, Remediation Coverage Analyst
CHAIN_LINK_SLOTS = ROLE_COUNT = 7

Declared gate transitions (7): 0->1, 1->PCR, PCR->2, 2->3, 3->4, 4->4B, 4B->5
GATE_STATE_SLOTS = GATE_COUNT = 7

TOTAL_SLOTS = 7 + 7 = 14
MANIFEST_DENOMINATOR = /14

Chain-link slots: CHAIN-LINK-0, CHAIN-LINK-1, CHAIN-LINK-PCR,
                  CHAIN-LINK-2, CHAIN-LINK-3, CHAIN-LINK-4, CHAIN-LINK-4B
Gate-state slots: GATE-STATE-0->1, GATE-STATE-1->PCR, GATE-STATE-PCR->2,
                  GATE-STATE-2->3, GATE-STATE-3->4, GATE-STATE-4->4B, GATE-STATE-4B->5
Passage-key slots: one per GATE-STATE — named key readback from preceding CHAIN-LINK
                   (Status quo: absent; without passage keys, a gate closes without citing
                   the upstream key that justified it — unjustified closure is undetectable)
```

---

### Role 0 — Inertia Analyst

Prosecution Theories and CHAIN-LINK-0. No downstream involvement.

| Charge | Why this risk | Predicted TC-2 | Predicted TC-3 |
|--------|--------------|----------------|----------------|
| IF-Storm | [why] | [or "none anticipated"] | [or "none anticipated"] |
| IF-Missing | [why] | [or "none anticipated"] | [or "none anticipated"] |
| IF-Circular | [why] | [or "none anticipated"] | [or "none anticipated"] |

Emit CHAIN-LINK-0:

```
CHAIN-LINK-0 (owner: Inertia Analyst)
ENV={{environment_name}} | LAYER={{solution_layer}}
MESH_STORM=[RISK|NO-RISK] | MESH_MISSING=[RISK|NO-RISK] | MESH_CIRCULAR=[RISK|NO-RISK]
STORM_TC2_PRED=[n] | STORM_TC3_PRED=[n]
MISSING_TC2_PRED=[n] | MISSING_TC3_PRED=[n]
CIRCULAR_TC2_PRED=[n] | CIRCULAR_TC3_PRED=[n]
```

*(Status quo: GATE-STATE-0->1 with no PASSAGE_KEY; gate closure asserts passage with no
evidence citation — any value of MESH_* satisfies the gate without Role 5 detecting the gap.)*

Emit GATE-STATE-0->1:

```
GATE-STATE-0->1:
  Owner: Inertia Analyst
  PASSAGE_KEY: [read CHAIN-LINK-0.MESH_STORM=<val>, CHAIN-LINK-0.MESH_MISSING=<val>, CHAIN-LINK-0.MESH_CIRCULAR=<val>]
  Condition: prosecution table complete; CHAIN-LINK-0 emitted with all MESH_* keys
  Status: [OPEN | CLOSED]
```

Gate 0->1: Status=CLOSED AND PASSAGE_KEY populated before Role 1 begins.

---

### Role 1 — Threat Cataloger

TC-1, TC-2, TC-3, Mesh Completeness Check, and CHAIN-LINK-1.

TC-1: Automation | Condition | YES/NO | IF-* annotation (required; IF-none is the null) | Notes

TC-2: # | Cascade chain | IF-* label | Prosecution status (Confirmed/Not confirmed) | Notes

TC-3: # | Side effect | IF-* label | Prosecution status | Reversible?

Mesh Completeness Check: IF-Storm/Missing/Circular [TC-1 n, TC-2 n, TC-3 n, COMPLETE/ORPHANED].

Emit CHAIN-LINK-1:

```
CHAIN-LINK-1 (owner: Threat Cataloger)
TC1=[n] | TC2=[n] | TC3=[n]
STORM_TC1=[n] | STORM_TC2=[n] | STORM_TC3=[n]
MISSING_TC1=[n] | MISSING_TC2=[n] | MISSING_TC3=[n]
CIRCULAR_TC1=[n] | CIRCULAR_TC2=[n] | CIRCULAR_TC3=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
PRED_CONFIRMED=[n] | PRED_FLAGGED=[n]
```

Emit GATE-STATE-1->PCR:

```
GATE-STATE-1->PCR:
  Owner: Threat Cataloger
  PASSAGE_KEY: [read CHAIN-LINK-1.TC1=<n>, CHAIN-LINK-1.MESH_STORM=<val>, CHAIN-LINK-1.MESH_MISSING=<val>, CHAIN-LINK-1.MESH_CIRCULAR=<val>]
  Condition: TC sections complete; IF-* on every row; mesh check; CHAIN-LINK-1 emitted
  Status: [OPEN | CLOSED]
```

Gate 1->PCR: Status=CLOSED AND PASSAGE_KEY populated before PCR Analyst begins.

---

### PCR Analyst — Prosecution Closure Report

**Independence declaration**: Distinct from (1) Inertia Analyst (prediction author),
(2) Registry Analyst, (3) Pathology Analyst, (4) Remediation Coverage Analyst / Phase 4B,
(5) Audit Analyst. CHAIN-LINK-PCR is the first independent terminal artifact.

Emit CHAIN-LINK-PCR:

```
CHAIN-LINK-PCR (owner: PCR Analyst — first independent terminal artifact)
PCR_STORM=[CLOSED|INDETERMINATE|NULL]   (read: CHAIN-LINK-0 vs CHAIN-LINK-1 prediction/confirmation counts)
PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
SILENT_GAPS_STORM=[n] | SILENT_GAPS_MISSING=[n] | SILENT_GAPS_CIRCULAR=[n]
```

Emit GATE-STATE-PCR->2:

```
GATE-STATE-PCR->2:
  Owner: PCR Analyst
  PASSAGE_KEY: [read CHAIN-LINK-PCR.PCR_STORM=<val>, CHAIN-LINK-PCR.PCR_MISSING=<val>, CHAIN-LINK-PCR.PCR_CIRCULAR=<val>]
  Condition: CHAIN-LINK-PCR emitted with all PCR_* keys
  Status: [OPEN | CLOSED]
```

Gate PCR->2: Status=CLOSED AND PASSAGE_KEY populated before Role 2 begins.

---

### Role 2 — Registry Analyst

Trigger table; then CHAIN-LINK-2.

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int or --] | [name] | [ref] | YES or NO | [in] | [out] | [ref or "none"] |

Emit CHAIN-LINK-2:

```
CHAIN-LINK-2 (owner: Registry Analyst)
M=[n] | N=[n] | NON_FIRING=[n]
BUDGET_GATE=[TRIGGERED|WAIVED]
```

Emit GATE-STATE-2->3:

```
GATE-STATE-2->3:
  Owner: Registry Analyst
  PASSAGE_KEY: [read CHAIN-LINK-2.M=<val>, CHAIN-LINK-2.N=<val>, CHAIN-LINK-2.BUDGET_GATE=<val>]
  Condition: trigger table complete; CHAIN-LINK-2 emitted with M, N, BUDGET_GATE
  Status: [OPEN | CLOSED]
```

Gate 2->3: Status=CLOSED AND PASSAGE_KEY populated before Role 3 begins.

---

### Role 3 — Budget Analyst

*(Status quo: TRIGGERED re-evaluated by Role 3 independently; budget gate self-attestation
gap — Role 3 can contradict CHAIN-LINK-2.BUDGET_GATE without a detectable key-level
discrepancy. C-37 closes this; V-05 inherits C-37.)*

Read CHAIN-LINK-2.BUDGET_GATE — key readback, not self-evaluated.

If WAIVED: emit waiver. If TRIGGERED: per-automation breakdown + total + limit + % + duration.

Emit CHAIN-LINK-3:

```
CHAIN-LINK-3 (owner: Budget Analyst)
TRIGGERED=[read CHAIN-LINK-2.BUDGET_GATE=<val>]  <- key readback; not self-evaluated by Role 3
TOTAL_REQ=[n|N/A] | DAILY_LIMIT=[n|N/A] | BUDGET_PCT=[pct|N/A] | DURATION=[X to Y s|N/A]
```

Emit GATE-STATE-3->4:

```
GATE-STATE-3->4:
  Owner: Budget Analyst
  PASSAGE_KEY: [read CHAIN-LINK-3.TRIGGERED=<val> (provenance: CHAIN-LINK-2.BUDGET_GATE), CHAIN-LINK-3.BUDGET_PCT=<val>]
  Condition: CHAIN-LINK-3 emitted; TRIGGERED carries key readback from CHAIN-LINK-2.BUDGET_GATE
  Status: [OPEN | CLOSED]
```

Gate 3->4: Status=CLOSED AND PASSAGE_KEY populated before Role 4 begins.

---

### Role 4 — Pathology Analyst

Verdict first on its own line. Three-layer remediation for DETECTED or INDETERMINATE.

**Trigger Storm**: VERDICT; Evidence (CHAIN-LINK-1.STORM_TC2, CHAIN-LINK-2 M/N, CHAIN-LINK-PCR.PCR_STORM); Remediation L1/L2/L3

**Missing Trigger**: VERDICT; Evidence (CHAIN-LINK-1.MISSING_TC3/TC1, CHAIN-LINK-PCR.PCR_MISSING); Remediation L1/L2/L3

**Circular Trigger**: VERDICT; Evidence (CHAIN-LINK-1.CIRCULAR_TC2/TC1, CHAIN-LINK-PCR.PCR_CIRCULAR); Remediation L1/L2/L3

Emit CHAIN-LINK-4:

```
CHAIN-LINK-4 (owner: Pathology Analyst)
STORM=[verdict] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[n] | REM_REQUIRED=[n]
```

Emit GATE-STATE-4->4B:

```
GATE-STATE-4->4B:
  Owner: Pathology Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4.STORM=<val>, CHAIN-LINK-4.MISSING=<val>, CHAIN-LINK-4.CIRCULAR=<val>]
  Entry condition: all three pathology verdicts present; CHAIN-LINK-4 emitted
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B — distinct from Role 4
```

Gate 4->4B: Status=CLOSED AND PASSAGE_KEY populated before Phase 4B begins.

---

### Phase 4B — Remediation Coverage Analyst

**Independence declaration**: Distinct from Role 4 and Role 5. Black-box read of CHAIN-LINK-4.
CHAIN-LINK-4B is the second independent terminal artifact.

Coverage table: Charge | Verdict (CHAIN-LINK-4) | Remedy? | L1? | L2? | L3? | COVERED/ORPHANED

Emit CHAIN-LINK-4B:

```
CHAIN-LINK-4B (owner: Remediation Coverage Analyst — second independent terminal artifact)
REM_STORM=[COVERED|ORPHANED|N/A]   (read: CHAIN-LINK-4.STORM)
REM_MISSING=[COVERED|ORPHANED|N/A]  (read: CHAIN-LINK-4.MISSING)
REM_CIRCULAR=[COVERED|ORPHANED|N/A] (read: CHAIN-LINK-4.CIRCULAR)
ORPHANED_COUNT=[n] | GATE_PASS=[YES|NO]
```

Emit GATE-STATE-4B->5:

```
GATE-STATE-4B->5:
  Owner: Remediation Coverage Analyst
  PASSAGE_KEY: [read CHAIN-LINK-4B.REM_STORM=<val>, CHAIN-LINK-4B.REM_MISSING=<val>, CHAIN-LINK-4B.REM_CIRCULAR=<val>]
  Exit condition: CHAIN-LINK-4B emitted; GATE_PASS declared; orphans acknowledged
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 (Audit Analyst) — distinct from Phase 4B
```

Gate 4B->5: Status=CLOSED AND PASSAGE_KEY populated before Role 5 begins.

---

### Role 5 — Audit Analyst

**Independence declaration**: Distinct from (1) PCR Analyst (prediction closure owner —
distinct from Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4
/ Pathology Analyst (verdict producer). Does not re-evaluate any upstream decision.

**Derivation Proof Verification** — verify first:

```
DERIVATION VERIFICATION (owner: Audit Analyst)
ROLE_COUNT_DECLARED=7 | CHAIN_LINK_SLOTS_DERIVED=7
GATE_COUNT_DECLARED=7 | GATE_STATE_SLOTS_DERIVED=7
TOTAL_SLOTS_DERIVED=14 | MANIFEST_DENOMINATOR_DECLARED=/14
DERIVATION_CHECK=[PASS | DERIVATION-MISMATCH: detail]
```

**Simulation Manifest Verification** — 21-slot audit + Ownership Registry cross-check
(proceed only after DERIVATION_CHECK=PASS)

*(Status quo without ownership audit: role contamination — e.g., CHAIN-LINK-3 produced
by Pathology Analyst — passes all presence and passage key checks. OWNER-MISMATCH closes this.)*
*(Status quo without passage key audit: unjustified gate closure — gate emitted with
Status=CLOSED but no named key from upstream CHAIN-LINK cited. PASSAGE-KEY-GAP closes this.)*

| Slot | Presence | Owner | Passage key |
|------|----------|-------|-------------|
| CHAIN-LINK-0 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-1 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-PCR | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-2 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-3 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-4 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| CHAIN-LINK-4B | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | — |
| GATE-STATE-0->1 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-1->PCR | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-PCR->2 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-2->3 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-3->4 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-4->4B | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |
| GATE-STATE-4B->5 | EMITTED/MANIFEST-GAP | OWNER_VERIFIED/OWNER-MISMATCH | POPULATED/PASSAGE-KEY-GAP |

Any MANIFEST-GAP drives a COLUMN-GAP in the certificate.

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from (1) PCR Analyst (prediction closure owner — distinct from
  Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B, (3) Role 4 / Pathology
  Analyst (verdict producer).
Manifest: canonical completeness check (replaces separate chain/gate integrity sections).
  Derivation proof: ROLE_COUNT=7, GATE_COUNT=7, TOTAL=14 — denominator structurally derived.
  Ownership Registry: header-declared — all 14 artifacts cross-checked against expected owner.
  Passage key audit: all 7 gate-state slots verified for named key readback from preceding CHAIN-LINK.

| Charge      | TC-1 annotation                           | TC-2/TC-3 annotation                                     | Forward mesh (PCR)                         | Adjudication verdict                   | Remedy on record                          |
|-------------|-------------------------------------------|----------------------------------------------------------|---------------------------------------------|----------------------------------------|-------------------------------------------|
| IF-Storm    | [n] <- key ref: CHAIN-LINK-1.STORM_TC1   | TC2=[n],TC3=[n] <- key refs: .STORM_TC2,.STORM_TC3       | [val] <- key ref: CHAIN-LINK-PCR.PCR_STORM | [val] <- key ref: CHAIN-LINK-4.STORM  | [val] <- key ref: CHAIN-LINK-4B.REM_STORM |
| IF-Missing  | [n] <- key ref: CHAIN-LINK-1.MISSING_TC1 | TC2=[n],TC3=[n] <- key refs: .MISSING_TC2,.MISSING_TC3   | [val] <- key ref: CHAIN-LINK-PCR.PCR_MISSING| [val] <- key ref: CHAIN-LINK-4.MISSING| [val] <- key ref: CHAIN-LINK-4B.REM_MISSING|
| IF-Circular | [n] <- key ref: CHAIN-LINK-1.CIRCULAR_TC1| TC2=[n],TC3=[n] <- key refs: .CIRCULAR_TC2,.CIRCULAR_TC3 | [val] <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR| [val] <- key ref: CHAIN-LINK-4.CIRCULAR| [val] <- key ref: CHAIN-LINK-4B.REM_CIRCULAR|

Scoring dimensions:
  Derivation proof: ROLE_COUNT=7, GATE_COUNT=7, TOTAL=14 verified = PASS; DERIVATION-MISMATCH = FAIL
  Manifest verification: all 14 slots EMITTED = PASS; any MANIFEST-GAP = FAIL
  Ownership audit: all emitted slots OWNER_VERIFIED = PASS; any OWNER-MISMATCH = FAIL
  Passage key audit: all 7 GATE-STATE slots PASSAGE_KEY_POPULATED = PASS; any PASSAGE-KEY-GAP = FAIL
  Budget gate key readback: CHAIN-LINK-3.TRIGGERED read from CHAIN-LINK-2.BUDGET_GATE
  PCR independence: CHAIN-LINK-PCR owner (PCR Analyst) distinct from Inertia Analyst
  Full-column key refs: all five columns carry named key refs; absent CHAIN-LINK -> COLUMN-GAP

Audit flags: [list any DERIVATION-MISMATCH, MANIFEST-GAP, OWNER-MISMATCH, PASSAGE-KEY-GAP, or COLUMN-GAP; "none" if all pass]
```

---

## Variation Summary

| Variation | Axis | New Signal Targeted | Gap Closed |
|-----------|------|--------------------|----|
| V-01 | Role sequence | Gate passage key chain | GATE-STATE blocks close without citing upstream key — PASSAGE-KEY-GAP closes this |
| V-02 | Output format | Ownership Registry + OWNER-MISMATCH | Artifacts emitted under wrong role authority — ownership audit closes this |
| V-03 | Lifecycle emphasis | Manifest derivation proof | Manifest denominator hardcoded — derivation proof makes it structurally derived |
| V-04 | Role sequence + output format | Passage keys + ownership registry | Both unjustified gate closure and role contamination — dual-dimension audit |
| V-05 | All three + inertia framing | All signals + status-quo cost visible | All three gaps closed; inertia framing makes each mechanism's value legible at the point of use |

**Predicted v14 extraction candidates (not scored under v13):**

| Candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39 (gate passage key chain) | PASS* | FAIL | FAIL | PASS* | PASS* |
| C-40 (ownership registry + OWNER-MISMATCH) | FAIL | PASS* | FAIL | PASS* | PASS* |
| C-41 (manifest derivation proof) | FAIL | FAIL | PASS* | FAIL | PASS* |

*Not scored under v13. Listed for v14 extraction evidence only.
