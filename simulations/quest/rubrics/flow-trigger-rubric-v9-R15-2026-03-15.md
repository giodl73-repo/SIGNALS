# Flow-Trigger Skill — Round 15 Variations (Rubric v11)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v11 (C-01 through C-32, denominator /25 aspirational)
**Date**: 2026-03-15

---

## Variation Design Notes

R14 V-05 scores 100.00 under v11 — the first variation to achieve all 25 aspirational criteria.
The terminal architecture is: seven-link verbatim chain, Phase 4B as independent terminal artifact
with bidirectional gate conditions, dual-entity Role 5 independence (distinct from Role 4 AND
Phase 4B), and CHAIN-LINK-4B carrying REM_* keys referenced in the certificate schema by name.

R15 does not optimize against v11 (already saturated). Instead, R15 probes the *next generation*
of structural gaps by varying three new axes that V-05 does not yet formalize:

**Gap 1 — Gate artifacts are described, not emitted.** V-05 uses ⛔ gate notation (prose
pre-conditions). The named "Gate 4→4B" and "Gate 4B→5" appear in C-30's definition but are
never emitted as machine-readable artifacts. A missing gate block cannot be detected by Role 5's
chain integrity section.

**Gap 2 — Four of five certificate columns carry no key-ref annotation.** C-32 adds
`<- named key ref` to the Remedy on record column only. The other four columns (TC-1, TC-2/TC-3,
Forward mesh, Pathology verdict) can silently produce values without reading a named key from
an upstream CHAIN-LINK. An absent CHAIN-LINK-1 does not produce a column gap — only a chain
integrity list failure.

**Gap 3 — PCR remains a Role 0 Phase 2 re-entry, not an independent terminal artifact.**
V-05 has three terminal artifact owners: Inertia Analyst (FMC forward mesh), Phase 4B
(remediation coverage), Audit Analyst (certificate). The PCR is still produced by the same
analyst who wrote the predictions. A PCR Analyst role that reads CHAIN-LINK-0 and CHAIN-LINK-1
as black-box inputs — with an independence declaration identical to Phase 4B's — closes this
self-attestation gap.

**New signal candidates for R16:**

| Gap | Candidate Criterion | Description |
|-----|--------------------|----|
| G-1 | C-33 | Gate formalization — named gate transitions emit machine-readable GATE-STATE blocks; chain integrity section checks gate artifacts alongside CHAIN-LINK blocks |
| G-2 | C-34 | Full-column schema key references — every certificate column has an inline `<- named key ref` annotation; absent CHAIN-LINK produces a column-specific named gap, not just a chain integrity failure |
| G-3 | C-35 | PCR as fourth independent terminal artifact — PCR Analyst declared distinct from Inertia Analyst; independence declaration at role definition AND in certificate header; four-owner terminal architecture |

**Variation axes (3 single-axis, 2 combined):**

- V-01: **Gate formalization** — gates emit GATE-STATE blocks; Gate 4→4B and Gate 4B→5 are
  named machine-readable artifacts; Role 5 chain integrity checks gate blocks
- V-02: **Full-column key references** — all five certificate columns carry `<- named key ref`
  annotations; absent chain link produces named column gap in specific column
- V-03: **PCR as independent role** — PCR Analyst extracted from Inertia Analyst; four-owner
  terminal architecture; PCR Analyst independence declaration at role definition
- V-04: **Combined (V-01 + V-02)** — gate formalization + full-column key references; gate
  blocks auditable in chain integrity section
- V-05: **Combined (V-01 + V-02 + V-03 + triple-entity Role 5)** — four-owner terminal
  architecture + gate formalization + full-column key refs + Role 5 names three upstream
  terminal artifact owners in independence declaration

**R14 retroactive scores under v11 (reference):**

| Variation | Composite |
|-----------|-----------|
| V-01–V-03 | 99.20 |
| V-04 | 99.40 |
| V-05 | 100.00 (ceiling) |

---

## V-01 — Gate Formalization

**Axis**: Gate formalization — every ⛔ gate emits a machine-readable GATE-STATE block
immediately after its condition description. Gate 4→4B and Gate 4B→5 are named structural
artifacts with explicit condition text, ownership, and status fields. Role 5's chain integrity
section checks gate artifacts as auditable chain items alongside the seven CHAIN-LINK blocks.

**Hypothesis**: C-30 requires "named Gate N→4B (entry condition)" and "named Gate 4B→5 (exit
condition)" as structural properties. In V-05, these are in ⛔ prose — they describe what must
be true but do not emit an artifact Role 5 can verify. A GATE-STATE block makes gate passage
a machine-readable fact. A missing GATE-STATE block is detectable (gap), not inferred
(satisfied because output appeared). Gate formalization is the structural escalation of C-30:
from named gate *conditions* to named gate *artifacts*.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating which
automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture plus named gate-state artifacts. Every structural transition emits either a
CHAIN-LINK block (data) or a GATE-STATE block (passage). Failure modes are formal charges.
Complete all blocks in order. Do not begin a block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change: {{change}}
Power Platform environment: {{environment_name}}    <- specific named environment only; "default" / "current" not acceptable
Solution layer: {{solution_layer}}                   <- specific named solution only; ambiguous labels not acceptable
```

---

### Role 0 — Prosecution Analyst / Inertia Analyst (Phase 1: Charges + Prosecution Theory)

**Accountability**: File the three formal charges and state prosecution theories. No involvement
in TC cataloging, trigger table, budget, or adjudication. Produces CHAIN-LINK-0.

| Charge | Why this change creates this risk | Expected TC-2 evidence chains | Expected TC-3 side-effect evidence |
|--------|----------------------------------|-------------------------------|-------------------------------------|
| IF-Storm | [why] <- specific to this change | [anticipated chains — or "none anticipated"] <- blank is not valid | [anticipated excess side effects — or "none anticipated"] |
| IF-Missing | [why] <- specific to this change | [anticipated absent paths — or "none anticipated"] | [anticipated missing side effects — or "none anticipated"] |
| IF-Circular | [why] <- specific to this change | [anticipated re-entrant chains — or "none anticipated"] | [anticipated circular side effects — or "none anticipated"] |

Caption (emit verbatim — CHAIN-LINK-0; downstream blocks read these keys by name):
```
CHAIN-LINK-0: ENV={{environment_name}} | LAYER={{solution_layer}}
STORM_TC2_PRED=[count] | STORM_TC3_PRED=[count]
MISSING_TC2_PRED=[count] | MISSING_TC3_PRED=[count]
CIRCULAR_TC2_PRED=[count] | CIRCULAR_TC3_PRED=[count]
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-0):
```
GATE-STATE-0→1:
  Owner: Prosecution Analyst
  Condition: Charges table complete with no blank cells AND CHAIN-LINK-0 emitted
  Status: [OPEN — condition not yet met | CLOSED — condition satisfied]
```

⛔ **Gate 0→1**: GATE-STATE-0→1 must show Status=CLOSED before Role 1 begins.

---

### Role 1 — Investigating Analyst (Threat Cataloger)

**Input**: Read CHAIN-LINK-0 prediction counts to know how many prosecution theories require
confirmation or rebuttal per charge.

**TC-1 — Candidate Trigger Conditions**

| Automation name | Trigger condition | Evaluates? | IF-* annotation | Notes |
|----------------|-------------------|------------|-----------------|-------|
| [automation] | [condition] <- name environment and solution layer if they affect evaluation | YES or NO only <- required | IF-Storm/Missing/Circular/none <- required; annotate where evaluation drives a charge risk; blank not acceptable | [boundary condition or "N/A"] <- required |

**TC-2 — Cascade Paths** *(read: CHAIN-LINK-0.STORM_TC2_PRED, MISSING_TC2_PRED,
CIRCULAR_TC2_PRED for fulfillment counts)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none <- required | Confirmed: [match] OR ⚠ Not confirmed: [reason] OR Not in prosecution scope <- one of three; read CHAIN-LINK-0 pred counts <- required | [notes] |

**TC-3 — Side-Effect Scope** *(read: CHAIN-LINK-0.STORM_TC3_PRED, MISSING_TC3_PRED,
CIRCULAR_TC3_PRED)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none <- required | same three-option rule; read CHAIN-LINK-0 <- required | YES or NO only <- required |

**Mesh Completeness Check**

| Charge | TC-1 | TC-2 | TC-3 | Status |
|--------|------|------|------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "⚠ [charge] orphaned: [explanation]."

Caption (emit verbatim — CHAIN-LINK-1; downstream blocks read these keys by name):
```
CHAIN-LINK-1: TC1=[N] | TC2=[N] | TC3=[N]
STORM_TC2_CONF=[n] | STORM_TC2_FLAG=[n] | STORM_TC3_CONF=[n] | STORM_TC3_FLAG=[n]
MISSING_TC2_CONF=[n] | MISSING_TC2_FLAG=[n] | MISSING_TC3_CONF=[n] | MISSING_TC3_FLAG=[n]
CIRCULAR_TC2_CONF=[n] | CIRCULAR_TC2_FLAG=[n] | CIRCULAR_TC3_CONF=[n] | CIRCULAR_TC3_FLAG=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-1):
```
GATE-STATE-1→PCR:
  Owner: Investigating Analyst
  Condition: TC-1/TC-2/TC-3 complete; IF-* annotations on every row; Mesh check complete; CHAIN-LINK-1 emitted
  Status: [OPEN | CLOSED]
```

⛔ **Gate 1→PCR**: GATE-STATE-1→PCR must show Status=CLOSED before PCR phase begins.

---

### Role 0 — Prosecution Analyst (Phase 2: Prosecution Closure Report)

**Input**: Read CHAIN-LINK-0 (predictions); read CHAIN-LINK-1 (confirmations and flags) by key name.

Caption (emit verbatim — CHAIN-LINK-PCR):
```
CHAIN-LINK-PCR (owner: Prosecution Analyst):
  Source: CHAIN-LINK-0 predictions vs CHAIN-LINK-1 actuals
  IF-Storm:    preds=[CHAIN-LINK-0.STORM_TC2_PRED + STORM_TC3_PRED] | conf=[CHAIN-LINK-1.STORM_TC2_CONF + STORM_TC3_CONF] | flagged=[CHAIN-LINK-1.STORM_TC2_FLAG + STORM_TC3_FLAG] | silent-gaps=[preds-conf-flagged] | PCR_STORM=[CLOSED|INDETERMINATE|NULL]
  IF-Missing:  preds=[CHAIN-LINK-0.MISSING_TC2_PRED + MISSING_TC3_PRED] | conf=[...CHAIN-LINK-1...] | flagged=[...] | silent-gaps=[...] | PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
  IF-Circular: preds=[CHAIN-LINK-0.CIRCULAR_TC2_PRED + CIRCULAR_TC3_PRED] | conf=[...CHAIN-LINK-1...] | flagged=[...] | silent-gaps=[...] | PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-PCR):
```
GATE-STATE-PCR→2:
  Owner: Prosecution Analyst
  Condition: CHAIN-LINK-PCR emitted with all three PCR_* values filled
  Status: [OPEN | CLOSED]
```

⛔ **Gate PCR→2**: GATE-STATE-PCR→2 must show Status=CLOSED before Role 2 begins.

---

### Role 2 — Registry Analyst

**Input**: Read TC-1 conditions from Role 1; read TC-3 side effects from Role 1.

**Trigger Table** *(read: CHAIN-LINK-1.TC1=[N] to verify condition count)*:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [consecutive int for YES; -- for NO] <- required | [name] | [TC-1 entry name] <- required | YES or NO only <- required | [inputs] | [outputs] | [TC-3 description or "none" if TC-3 confirms none] <- required |

Caption (emit verbatim — CHAIN-LINK-2):
```
CHAIN-LINK-2: FIRING=[N YES rows] | NON_FIRING=[N NO rows] | FIRES_VALID=[YES — all cells YES or NO | NO — invalid: [list]]
```

Registry Summary (emit verbatim):
```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of YES rows with at least one non-"none" side effect]
N = [count of all YES rows]
Non-firing = [count of NO rows]
```

Gate artifact (emit verbatim immediately after Registry Summary):
```
GATE-STATE-2→3:
  Owner: Registry Analyst
  Condition: CHAIN-LINK-2 emitted AND Registry Summary present with M, N, Non-firing
  Status: [OPEN | CLOSED]
```

⛔ **Gate 2→3**: GATE-STATE-2→3 must show Status=CLOSED before Role 3 begins.

---

### Role 3 — Budget Analyst

**Input**: Read M from Registry Summary (CHAIN-LINK-2.M); read FIRES_VALID from CHAIN-LINK-2.

Gate condition: M >= 3 AND at least one non-"none" side effect. If not met:
"Budget Gate: NOT TRIGGERED — M=[value], reason=[condition not met]."

If triggered:

| Automation | Dataverse actions | Connector actions | Child flow invocations | Total requests/invocation |
|-----------|------------------|------------------|----------------------|--------------------------|
| [name] | [n] | [n] | [n] | [sum] <- per-automation intermediate required |

1. Total API requests: [sum]
2. Platform daily limit: [specific number]
3. Budget consumed: [%]
4. Run duration: [X to Y] seconds

Caption (emit verbatim — CHAIN-LINK-3):
```
CHAIN-LINK-3: TRIGGERED=[YES|NO] | M=[value] | TOTAL_REQ=[count] | BUDGET_PCT=[pct]% | DURATION=[X to Y]s
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-3):
```
GATE-STATE-3→4:
  Owner: Budget Analyst
  Condition: CHAIN-LINK-3 emitted (budget section complete OR NOT TRIGGERED waiver present)
  Status: [OPEN | CLOSED]
```

⛔ **Gate 3→4**: GATE-STATE-3→4 must show Status=CLOSED before Role 4 begins.

---

### Role 4 — Adjudicator (Pathology Analyst)

**Input**: Read IF-* evidence from CHAIN-LINK-1; read PCR status from CHAIN-LINK-PCR by key name;
read M, N from Registry Summary; read CHAIN-LINK-3. Role 4 does not produce CHAIN-LINK-4B
(that belongs to Phase 4B) and does not produce the certificate (that belongs to Role 5).

Each subsection opens with its verdict keyword on its own line before evidence.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Storm entries: [cite by chain description]
- TC-3 IF-Storm entries: [cite by side-effect description]
- Registry M=[from Registry Summary], N=[from Registry Summary]
- CHAIN-LINK-PCR.PCR_STORM=[value] — [note silent gaps if any]

Remediation (required if DETECTED or INDETERMINATE; absence will produce an ORPHANED flag in Phase 4B that Role 5 will read from CHAIN-LINK-4B):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-1 IF-Missing annotations: [cite]
- TC-2 IF-Missing entries: [cite]
- TC-3 IF-Missing entries: [cite]
- CHAIN-LINK-PCR.PCR_MISSING=[value] — [description]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Circular entries: [cite]
- TC-1 IF-Circular annotations: [cite]
- CHAIN-LINK-PCR.PCR_CIRCULAR=[value] — [description]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Circular

Caption (emit verbatim — CHAIN-LINK-4; Phase 4B reads STORM, MISSING, CIRCULAR verdict keys):
```
CHAIN-LINK-4: STORM=[DETECTED|NOT DETECTED|INDETERMINATE] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[count with three-layer remediation] | REM_REQUIRED=[count of DETECTED+INDETERMINATE]
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-4 — this is the bidirectional entry gate for Phase 4B):
```
GATE-STATE-4→4B:
  Owner: Phase 4B (Remediation Coverage Gate) declares entry
  Entry condition: All three pathology subsections present with verdict-first structure AND CHAIN-LINK-4 emitted with REM_PROVIDED and REM_REQUIRED
  Status: [OPEN | CLOSED]
  Processing authority: Phase 4B — distinct from Role 4
```

⛔ **Gate 4→4B**: GATE-STATE-4→4B must show Status=CLOSED before Phase 4B begins.

---

### Phase 4B — Charges Closed Review (Remediation Coverage Gate)

**Role declaration**: This phase is a distinct structural artifact — not part of Role 4 and not
part of Role 5. It reads CHAIN-LINK-4 as a black-box input. It does not re-evaluate verdicts
and does not add analysis. Processing authority: Phase 4B only.

**Input**: Read CHAIN-LINK-4.STORM, MISSING, CIRCULAR verdict keys; read
CHAIN-LINK-4.REM_PROVIDED vs REM_REQUIRED. Read Role 4 pathology subsections to verify
three-layer completeness per IF-*.

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage status |
|--------|-------------------------------------|-----------------|----------|----------|----------|-----------------|
| IF-Storm | [read CHAIN-LINK-4.STORM] <- required; read from caption, do not re-derive | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |

For any ORPHANED charge:
"⚠ CHARGE [IF-label] ORPHANED — verdict is [DETECTED/INDETERMINATE] and [no remedy on record /
Layer [1|2|3] absent]. Acknowledgment required: [reason or resolution]."

Caption (emit verbatim — CHAIN-LINK-4B; Role 5 certificate schema references REM_STORM,
REM_MISSING, REM_CIRCULAR by key name):
```
CHAIN-LINK-4B: REM_STORM=[COVERED|ORPHANED] | REM_MISSING=[COVERED|ORPHANED] | REM_CIRCULAR=[COVERED|ORPHANED]
ORPHANED_COUNT=[count or 0] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all orphans acknowledged; NO otherwise]
```

Gate artifact (emit verbatim immediately after CHAIN-LINK-4B — this is the bidirectional exit gate from Phase 4B):
```
GATE-STATE-4B→5:
  Owner: Phase 4B (Remediation Coverage Gate) declares exit
  Exit condition: Coverage gate table complete; all ORPHANED charges flagged and acknowledged; CHAIN-LINK-4B emitted with GATE_PASS declared
  Status: [OPEN | CLOSED]
  Processing authority handoff: Role 5 — distinct from Phase 4B
```

⛔ **Gate 4B→5**: GATE-STATE-4B→5 must show Status=CLOSED before Role 5 begins.

---

### Role 5 — Independent Audit Analyst

**Role declaration**: Independent Audit Analyst is explicitly distinct from Role 4 (verdict
producer) and Phase 4B (remediation coverage gate). Does not evaluate evidence, modify verdicts,
or add analysis. Reads all prior CHAIN-LINK and GATE-STATE blocks as auditable inputs. Audits,
cites, and flags only. This boundary is declared, not inferred from behavior.

**Input references** (read each block by key name — if any CHAIN-LINK is absent, the certificate
schema has a named reference gap; if any GATE-STATE is absent, report gate gap):
- `CHAIN-LINK-0.*` — prosecution theory prediction counts
- `CHAIN-LINK-1.*` — TC annotation and confirmation counts + mesh status
- `CHAIN-LINK-PCR.*` — prosecution closure status per charge
- `CHAIN-LINK-2.*` — trigger table filing counts
- `CHAIN-LINK-3.*` — budget gate result
- `CHAIN-LINK-4.*` — adjudication verdicts
- `CHAIN-LINK-4B.*` — charges closed status per charge ← read REM_STORM, REM_MISSING, REM_CIRCULAR by key name; if absent, Remedy column = CHAIN-GAP for all rows
- `GATE-STATE-4→4B.*` — entry gate artifact for Phase 4B ← if absent, Phase 4B provenance unverifiable
- `GATE-STATE-4B→5.*` — exit gate artifact from Phase 4B ← if absent, Phase 4B closure unverifiable

Emit this block verbatim with all values filled in:

```
MESH CLOSURE CERTIFICATE (owner: Independent Audit Analyst)
Role declaration: distinct from Role 4 (verdict producer) and Phase 4B (remediation gate). Does not evaluate evidence, modify verdicts, or add analysis.
Chain links read: CHAIN-LINK-0 | CHAIN-LINK-1 | CHAIN-LINK-PCR | CHAIN-LINK-2 | CHAIN-LINK-3 | CHAIN-LINK-4 | CHAIN-LINK-4B
Gate artifacts read: GATE-STATE-4→4B | GATE-STATE-4B→5

| Charge      | TC-1 ann. (C-22)                                    | TC-2/TC-3 ann. (C-20)                                                      | Forward mesh (C-21)                                                             | Adjudication verdict (C-18)                          | Remedy on record (C-27)                                                          | Certificate |
|-------------|-----------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|-------------|
| IF-Storm    | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC1=[n])        | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC2=[n] + STORM_TC3=[n])              | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_STORM=[status], silent-gaps=[n])       | PASS/FAIL (read: CHAIN-LINK-4.STORM=[verdict])       | PASS/FAIL (read: CHAIN-LINK-4B.REM_STORM=[COVERED|ORPHANED]) <- named key ref   | PASS/FAIL   |
| IF-Missing  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC1=[n])      | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC2=[n] + MISSING_TC3=[n])          | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_MISSING=[status], silent-gaps=[n])     | PASS/FAIL (read: CHAIN-LINK-4.MISSING=[verdict])     | PASS/FAIL (read: CHAIN-LINK-4B.REM_MISSING=[COVERED|ORPHANED]) <- named key ref | PASS/FAIL   |
| IF-Circular | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC1=[n])     | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC2=[n] + CIRCULAR_TC3=[n])        | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_CIRCULAR=[status], silent-gaps=[n])    | PASS/FAIL (read: CHAIN-LINK-4.CIRCULAR=[verdict])    | PASS/FAIL (read: CHAIN-LINK-4B.REM_CIRCULAR=[COVERED|ORPHANED]) <- named key ref| PASS/FAIL   |

Scoring per dimension:
- TC-1 annotation PASS: CHAIN-LINK-1 TC1 count > 0
- TC-2/TC-3 annotation PASS: CHAIN-LINK-1 TC2 + TC3 count > 0
- Forward mesh PASS: CHAIN-LINK-PCR silent-gaps = 0; N-A if NULL
- Adjudication verdict PASS: CHAIN-LINK-4 verdict keyword present
- Remedy on record PASS: CHAIN-LINK-4B.[charge]_REM = COVERED; FAIL if ORPHANED or CHAIN-LINK-4B absent

Chain integrity:
  CHAIN-LINK-0 present: [YES/NO]
  CHAIN-LINK-1 present: [YES/NO]
  CHAIN-LINK-PCR present: [YES/NO]
  CHAIN-LINK-2 present: [YES/NO]
  CHAIN-LINK-3 present: [YES/NO]
  CHAIN-LINK-4 present: [YES/NO]
  CHAIN-LINK-4B present: [YES/NO]  <- named reference required; if NO, Remedy column = CHAIN-GAP for all rows
  Chain complete: [YES if all seven present; NO — first missing link: [name]]

Gate integrity:
  GATE-STATE-4→4B present: [YES/NO]  <- if NO, Phase 4B entry provenance unverifiable
  GATE-STATE-4B→5 present: [YES/NO]  <- if NO, Phase 4B exit provenance unverifiable
  Gates complete: [YES if both present; NO — missing gate: [name]]

⚠ Audit flags: [fill in for any FAIL, chain gap, or gate gap; "none" if all rows PASS in all dimensions]

Overall certificate: [PASS if all rows PASS in all five dimensions, chain complete, and gates complete; FAIL otherwise]
```

---

## V-02 — Full-Column Schema Key References

**Axis**: Full-column schema key references — every column in the certificate schema carries an
inline `<- named key ref: [CHAIN-LINK-N.KEY]` annotation. An absent CHAIN-LINK produces a
named column gap in the specific column that reads it — not just a chain integrity list failure.
Column gaps are named in the audit flags section as "COLUMN-GAP: [column name] for all rows —
[CHAIN-LINK] absent."

**Hypothesis**: C-32 extends verbatim-chain key references to the Remedy column only. The other
four columns (TC-1, TC-2/TC-3, Forward mesh, Adjudication verdict) read their values from
CHAIN-LINK-1, CHAIN-LINK-PCR, CHAIN-LINK-4 but carry no `<- named key ref` annotation. This
means an absent CHAIN-LINK-1 does not produce a named column gap — it produces only a chain
integrity list failure, which is a structural audit, not a schema-level enforcement. Full-column
key references elevate the entire schema from "verified by chain integrity audit" to
"schema-enforced by named key reference." Every column gap is schema-detectable, not just
chain-integrity-detectable.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating which
automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture where the certificate schema references every upstream key by name. An absent
CHAIN-LINK produces a named column gap in the specific certificate column that reads it. Failure
modes are formal charges. Complete all blocks in order. Do not begin a block until its gate
pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change: {{change}}
Power Platform environment: {{environment_name}}    <- specific named environment only; "default" / "current" not acceptable
Solution layer: {{solution_layer}}                   <- specific named solution only; ambiguous labels not acceptable
```

---

### Role 0 — Prosecution Analyst / Inertia Analyst (Phase 1: Charges + Prosecution Theory)

**Accountability**: File the three formal charges and state prosecution theories. No involvement
in TC cataloging, trigger table, budget, or adjudication. Produces CHAIN-LINK-0.

| Charge | Why this change creates this risk | Expected TC-2 evidence chains | Expected TC-3 side-effect evidence |
|--------|----------------------------------|-------------------------------|-------------------------------------|
| IF-Storm | [why] <- specific to this change | [anticipated chains — or "none anticipated"] | [anticipated excess side effects — or "none anticipated"] |
| IF-Missing | [why] <- specific to this change | [anticipated absent paths — or "none anticipated"] | [anticipated missing side effects — or "none anticipated"] |
| IF-Circular | [why] <- specific to this change | [anticipated re-entrant chains — or "none anticipated"] | [anticipated circular side effects — or "none anticipated"] |

Caption (emit verbatim — CHAIN-LINK-0):
```
CHAIN-LINK-0: ENV={{environment_name}} | LAYER={{solution_layer}}
STORM_TC2_PRED=[count] | STORM_TC3_PRED=[count]
MISSING_TC2_PRED=[count] | MISSING_TC3_PRED=[count]
CIRCULAR_TC2_PRED=[count] | CIRCULAR_TC3_PRED=[count]
```

⛔ **Gate 0→1**: Charges table complete; CHAIN-LINK-0 emitted.

---

### Role 1 — Investigating Analyst (Threat Cataloger)

**Input**: Read CHAIN-LINK-0 prediction counts by key name.

**TC-1 — Candidate Trigger Conditions**

| Automation name | Trigger condition | Evaluates? | IF-* annotation | Notes |
|----------------|-------------------|------------|-----------------|-------|
| [automation] | [condition] <- name environment and solution layer if they affect evaluation | YES or NO only <- required | IF-Storm/Missing/Circular/none <- required; blank not acceptable | [boundary condition or "N/A"] <- required |

**TC-2 — Cascade Paths** *(read: CHAIN-LINK-0.STORM_TC2_PRED, MISSING_TC2_PRED,
CIRCULAR_TC2_PRED)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none <- required | Confirmed: [match] OR ⚠ Not confirmed: [reason] OR Not in prosecution scope <- one of three | [notes] |

**TC-3 — Side-Effect Scope** *(read: CHAIN-LINK-0.STORM_TC3_PRED, MISSING_TC3_PRED,
CIRCULAR_TC3_PRED)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none <- required | same three-option rule | YES or NO only <- required |

**Mesh Completeness Check**

| Charge | TC-1 | TC-2 | TC-3 | Status |
|--------|------|------|------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "⚠ [charge] orphaned: [explanation]."

Caption (emit verbatim — CHAIN-LINK-1; the certificate schema reads STORM_TC1, STORM_TC2,
STORM_TC3 (and equivalents for MISSING, CIRCULAR) by key name from this block — an absent
CHAIN-LINK-1 produces COLUMN-GAP in TC-1 annotation and TC-2/TC-3 annotation columns):
```
CHAIN-LINK-1: TC1=[N] | TC2=[N] | TC3=[N]
STORM_TC2_CONF=[n] | STORM_TC2_FLAG=[n] | STORM_TC3_CONF=[n] | STORM_TC3_FLAG=[n]
MISSING_TC2_CONF=[n] | MISSING_TC2_FLAG=[n] | MISSING_TC3_CONF=[n] | MISSING_TC3_FLAG=[n]
CIRCULAR_TC2_CONF=[n] | CIRCULAR_TC2_FLAG=[n] | CIRCULAR_TC3_CONF=[n] | CIRCULAR_TC3_FLAG=[n]
STORM_TC1=[n] | MISSING_TC1=[n] | CIRCULAR_TC1=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
```

⛔ **Gate 1→PCR**: TC-1/TC-2/TC-3 complete; IF-* annotations on every row; Mesh check complete;
CHAIN-LINK-1 emitted.

---

### Role 0 — Prosecution Analyst (Phase 2: Prosecution Closure Report)

**Input**: Read CHAIN-LINK-0 (predictions); read CHAIN-LINK-1 (confirmations and flags) by key name.

Caption (emit verbatim — CHAIN-LINK-PCR; the certificate schema reads PCR_STORM, PCR_MISSING,
PCR_CIRCULAR by key name from this block — an absent CHAIN-LINK-PCR produces COLUMN-GAP in
the Forward mesh column):
```
CHAIN-LINK-PCR (owner: Prosecution Analyst):
  Source: CHAIN-LINK-0 predictions vs CHAIN-LINK-1 actuals
  IF-Storm:    preds=[CHAIN-LINK-0.STORM_TC2_PRED + STORM_TC3_PRED] | conf=[CHAIN-LINK-1.STORM_TC2_CONF + STORM_TC3_CONF] | flagged=[CHAIN-LINK-1.STORM_TC2_FLAG + STORM_TC3_FLAG] | silent-gaps=[preds-conf-flagged] | PCR_STORM=[CLOSED|INDETERMINATE|NULL]
  IF-Missing:  preds=[CHAIN-LINK-0.MISSING_TC2_PRED + MISSING_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
  IF-Circular: preds=[CHAIN-LINK-0.CIRCULAR_TC2_PRED + CIRCULAR_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
```

⛔ **Gate PCR→2**: CHAIN-LINK-PCR emitted with all three PCR_* values.

---

### Role 2 — Registry Analyst

**Input**: Read TC-1 from Role 1; read TC-3 from Role 1.

**Trigger Table**:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [consecutive int for YES; -- for NO] <- required | [name] | [TC-1 entry name] <- required | YES or NO only <- required | [inputs] | [outputs] | [TC-3 description or "none"] <- required |

Caption (emit verbatim — CHAIN-LINK-2):
```
CHAIN-LINK-2: FIRING=[N YES rows] | NON_FIRING=[N NO rows] | FIRES_VALID=[YES | NO — invalid: [list]]
```

Registry Summary (emit verbatim):
```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of YES rows with at least one non-"none" side effect]
N = [count of all YES rows]
Non-firing = [count of NO rows]
```

⛔ **Gate 2→3**: CHAIN-LINK-2 emitted; Registry Summary present.

---

### Role 3 — Budget Analyst

**Input**: Read M from Registry Summary; read FIRES_VALID from CHAIN-LINK-2.

Gate: M >= 3 AND at least one non-"none" side effect. If not met:
"Budget Gate: NOT TRIGGERED — M=[value], reason=[condition not met]."

If triggered:

| Automation | Dataverse actions | Connector actions | Child flow invocations | Total requests/invocation |
|-----------|------------------|------------------|----------------------|--------------------------|
| [name] | [n] | [n] | [n] | [sum] <- per-automation intermediate required |

1. Total API requests: [sum]
2. Platform daily limit: [specific number]
3. Budget consumed: [%]
4. Run duration: [X to Y] seconds

Caption (emit verbatim — CHAIN-LINK-3):
```
CHAIN-LINK-3: TRIGGERED=[YES|NO] | M=[value] | TOTAL_REQ=[count] | BUDGET_PCT=[pct]% | DURATION=[X to Y]s
```

⛔ **Gate 3→4**: CHAIN-LINK-3 emitted.

---

### Role 4 — Adjudicator (Pathology Analyst)

**Input**: Read CHAIN-LINK-1, CHAIN-LINK-PCR, CHAIN-LINK-3 by key name. Role 4 does not produce
CHAIN-LINK-4B and does not produce the certificate.

Each subsection opens with its verdict keyword on its own line before evidence.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Storm entries: [cite]
- TC-3 IF-Storm entries: [cite]
- Registry M=[value], N=[value]
- CHAIN-LINK-PCR.PCR_STORM=[value] — [note silent gaps]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-1 IF-Missing annotations: [cite]
- TC-2 IF-Missing entries: [cite]
- TC-3 IF-Missing entries: [cite]
- CHAIN-LINK-PCR.PCR_MISSING=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence:
- TC-2 IF-Circular entries: [cite]
- TC-1 IF-Circular annotations: [cite]
- CHAIN-LINK-PCR.PCR_CIRCULAR=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#]
- Layer 3 — Failure mode closed: IF-Circular

Caption (emit verbatim — CHAIN-LINK-4; the certificate schema reads STORM, MISSING, CIRCULAR
verdict keys by name — an absent CHAIN-LINK-4 produces COLUMN-GAP in the Adjudication verdict
column):
```
CHAIN-LINK-4: STORM=[DETECTED|NOT DETECTED|INDETERMINATE] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[count with three-layer remediation] | REM_REQUIRED=[count of DETECTED+INDETERMINATE]
```

⛔ **Gate 4→4B**: All three subsections present with verdict-first structure; CHAIN-LINK-4 emitted.

---

### Phase 4B — Charges Closed Review (Remediation Coverage Gate)

**Role declaration**: Distinct structural artifact — not part of Role 4, not part of Role 5.
Reads CHAIN-LINK-4 as black-box input. Does not re-evaluate verdicts. Processing authority:
Phase 4B only.

**Input**: Read CHAIN-LINK-4.STORM, MISSING, CIRCULAR by key name; read REM_PROVIDED vs
REM_REQUIRED. Read Role 4 subsections to verify three-layer completeness per IF-*.

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage status |
|--------|-------------------------------------|-----------------|----------|----------|----------|-----------------|
| IF-Storm | [read CHAIN-LINK-4.STORM] <- required | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |

For any ORPHANED charge:
"⚠ CHARGE [IF-label] ORPHANED — verdict is [DETECTED/INDETERMINATE] and [no remedy on record /
Layer [1|2|3] absent]. Acknowledgment required: [reason or resolution]."

Caption (emit verbatim — CHAIN-LINK-4B; the certificate schema reads REM_STORM, REM_MISSING,
REM_CIRCULAR by key name from this block — an absent CHAIN-LINK-4B produces COLUMN-GAP in the
Remedy on record column for all rows):
```
CHAIN-LINK-4B: REM_STORM=[COVERED|ORPHANED] | REM_MISSING=[COVERED|ORPHANED] | REM_CIRCULAR=[COVERED|ORPHANED]
ORPHANED_COUNT=[count or 0] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all orphans acknowledged; NO otherwise]
```

⛔ **Gate 4B→5**: Coverage table complete; all ORPHANED charges flagged and acknowledged;
CHAIN-LINK-4B emitted with GATE_PASS declared before Role 5 begins.

---

### Role 5 — Independent Audit Analyst

**Role declaration**: Independent Audit Analyst is explicitly distinct from Role 4 (verdict
producer) and Phase 4B (remediation coverage gate). Does not evaluate evidence, modify verdicts,
or add analysis. Reads all prior CHAIN-LINK blocks by key name. Audits, cites, and flags only.
This boundary is declared, not inferred from behavior.

**Input references** (read each block by key name — an absent CHAIN-LINK produces a COLUMN-GAP
in the specific column that reads it, named in audit flags):
- `CHAIN-LINK-0.*` — prediction counts
- `CHAIN-LINK-1.*` — TC counts + mesh status ← TC-1 annotation column and TC-2/TC-3 column
- `CHAIN-LINK-PCR.*` — PCR closure status ← Forward mesh column
- `CHAIN-LINK-2.*` — firing counts
- `CHAIN-LINK-3.*` — budget result
- `CHAIN-LINK-4.*` — verdicts ← Adjudication verdict column
- `CHAIN-LINK-4B.*` — remediation coverage ← Remedy on record column

Emit this block verbatim with all values filled in:

```
MESH CLOSURE CERTIFICATE (owner: Independent Audit Analyst)
Role declaration: distinct from Role 4 (verdict producer) and Phase 4B (remediation gate). Does not evaluate evidence, modify verdicts, or add analysis.
Chain links read: CHAIN-LINK-0 | CHAIN-LINK-1 | CHAIN-LINK-PCR | CHAIN-LINK-2 | CHAIN-LINK-3 | CHAIN-LINK-4 | CHAIN-LINK-4B

| Charge      | TC-1 ann. (C-22)                                                                     | TC-2/TC-3 ann. (C-20)                                                                                | Forward mesh (C-21)                                                                                          | Adjudication verdict (C-18)                                               | Remedy on record (C-27)                                                                          | Certificate |
|-------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| IF-Storm    | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC1=[n]) <- named key ref: CHAIN-LINK-1.STORM_TC1 | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC2=[n] + STORM_TC3=[n]) <- named key refs: CHAIN-LINK-1.STORM_TC2, STORM_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_STORM=[status], silent-gaps=[n]) <- named key ref: CHAIN-LINK-PCR.PCR_STORM | PASS/FAIL (read: CHAIN-LINK-4.STORM=[verdict]) <- named key ref: CHAIN-LINK-4.STORM | PASS/FAIL (read: CHAIN-LINK-4B.REM_STORM=[COVERED|ORPHANED]) <- named key ref: CHAIN-LINK-4B.REM_STORM | PASS/FAIL   |
| IF-Missing  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC1=[n]) <- named key ref: CHAIN-LINK-1.MISSING_TC1 | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC2=[n] + MISSING_TC3=[n]) <- named key refs: CHAIN-LINK-1.MISSING_TC2, MISSING_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_MISSING=[status]) <- named key ref: CHAIN-LINK-PCR.PCR_MISSING | PASS/FAIL (read: CHAIN-LINK-4.MISSING=[verdict]) <- named key ref: CHAIN-LINK-4.MISSING | PASS/FAIL (read: CHAIN-LINK-4B.REM_MISSING=[COVERED|ORPHANED]) <- named key ref: CHAIN-LINK-4B.REM_MISSING | PASS/FAIL   |
| IF-Circular | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC1=[n]) <- named key ref: CHAIN-LINK-1.CIRCULAR_TC1 | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC2=[n] + CIRCULAR_TC3=[n]) <- named key refs: CHAIN-LINK-1.CIRCULAR_TC2, CIRCULAR_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_CIRCULAR=[status]) <- named key ref: CHAIN-LINK-PCR.PCR_CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4.CIRCULAR=[verdict]) <- named key ref: CHAIN-LINK-4.CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4B.REM_CIRCULAR=[COVERED|ORPHANED]) <- named key ref: CHAIN-LINK-4B.REM_CIRCULAR | PASS/FAIL   |

Scoring per dimension:
- TC-1 annotation PASS: CHAIN-LINK-1.STORM_TC1 (or equiv) > 0; if CHAIN-LINK-1 absent: COLUMN-GAP for TC-1 column
- TC-2/TC-3 annotation PASS: CHAIN-LINK-1.TC2 + TC3 > 0; if CHAIN-LINK-1 absent: COLUMN-GAP for TC-2/TC-3 column
- Forward mesh PASS: CHAIN-LINK-PCR.silent-gaps = 0; N-A if NULL; if CHAIN-LINK-PCR absent: COLUMN-GAP for Forward mesh column
- Adjudication verdict PASS: CHAIN-LINK-4 verdict keyword present; if CHAIN-LINK-4 absent: COLUMN-GAP for Adjudication verdict column
- Remedy on record PASS: CHAIN-LINK-4B.REM_* = COVERED; if CHAIN-LINK-4B absent: COLUMN-GAP for Remedy column (all rows)

Chain integrity:
  CHAIN-LINK-0 present: [YES/NO]
  CHAIN-LINK-1 present: [YES/NO]  <- if NO: COLUMN-GAP: TC-1 annotation, TC-2/TC-3 annotation for all rows
  CHAIN-LINK-PCR present: [YES/NO]  <- if NO: COLUMN-GAP: Forward mesh for all rows
  CHAIN-LINK-2 present: [YES/NO]
  CHAIN-LINK-3 present: [YES/NO]
  CHAIN-LINK-4 present: [YES/NO]  <- if NO: COLUMN-GAP: Adjudication verdict for all rows
  CHAIN-LINK-4B present: [YES/NO]  <- if NO: COLUMN-GAP: Remedy on record for all rows
  Chain complete: [YES if all seven present; NO — first missing link: [name], producing column gap: [column name]]

⚠ Audit flags: [fill in for any FAIL or COLUMN-GAP; "none" if all rows PASS in all dimensions]
  COLUMN-GAP format: "COLUMN-GAP: [column name] for all rows — [CHAIN-LINK-N] absent"

Overall certificate: [PASS if all rows PASS in all five dimensions and chain complete; FAIL otherwise]
```

---
## V-03 -- PCR as Fourth Independent Terminal Artifact

**Axis**: PCR as independent terminal artifact -- Role 0 Phase 2 is extracted into a named role:
"PCR Analyst," distinct from the Inertia Analyst (who wrote the predictions), from Role 4
(verdict producer), and from Phase 4B (remediation coverage gate). Creates a four-owner terminal
architecture: Inertia Analyst owns the forward mesh, PCR Analyst owns prediction closure, Phase
4B owns remediation coverage, Audit Analyst owns the certificate.

**Hypothesis**: Phase 4B was extracted from Role 4 because the verdict producer cannot
self-certify remediation coverage. By strict analogy, the Inertia Analyst cannot independently
verify prediction fulfillment -- they wrote the predictions. A PCR Analyst who reads
CHAIN-LINK-0 and CHAIN-LINK-1 as black-box inputs provides genuine independent verification.
This is the Phase 4B extraction pattern applied to the prediction closure dimension.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating which
automations fire when a record changes. This simulation uses a four-owner terminal architecture:
every terminal artifact (PCR, Remediation Coverage Gate, Mesh Closure Certificate) is owned by
a role distinct from the role that produced the data being checked. Failure modes are formal
charges. Complete all blocks in order. Do not begin a block until its gate pre-condition is
satisfied.

**Scenario boundary:**

```
Triggering change: {{change}}
Power Platform environment: {{environment_name}}    <- specific named environment only; "default" / "current" not acceptable
Solution layer: {{solution_layer}}                   <- specific named solution only; ambiguous labels not acceptable
```

---

### Role 0 -- Inertia Analyst (Phase 1: Charges + Forward Mesh)

**Accountability**: File the three formal charges and state prosecution theories. No involvement
in TC cataloging, trigger table, budget, adjudication, or prediction closure. Prediction closure
belongs to PCR Analyst independently. Produces CHAIN-LINK-0.

| Charge | Why this change creates this risk | Expected TC-2 evidence chains | Expected TC-3 side-effect evidence |
|--------|----------------------------------|-------------------------------|-------------------------------------|
| IF-Storm | [why] <- specific to this change | [anticipated chains -- or "none anticipated"] | [anticipated excess side effects -- or "none anticipated"] |
| IF-Missing | [why] <- specific to this change | [anticipated absent paths -- or "none anticipated"] | [anticipated missing side effects -- or "none anticipated"] |
| IF-Circular | [why] <- specific to this change | [anticipated re-entrant chains -- or "none anticipated"] | [anticipated circular side effects -- or "none anticipated"] |

Caption (emit verbatim -- CHAIN-LINK-0):
```
CHAIN-LINK-0: ENV={{environment_name}} | LAYER={{solution_layer}}
STORM_TC2_PRED=[count] | STORM_TC3_PRED=[count]
MISSING_TC2_PRED=[count] | MISSING_TC3_PRED=[count]
CIRCULAR_TC2_PRED=[count] | CIRCULAR_TC3_PRED=[count]
```

Gate 0->1: Charges table complete; CHAIN-LINK-0 emitted.

---

### Role 1 -- Investigating Analyst (Threat Cataloger)

**Input**: Read CHAIN-LINK-0 prediction counts by key name.

**TC-1 -- Candidate Trigger Conditions**

| Automation name | Trigger condition | Evaluates? | IF-* annotation | Notes |
|----------------|-------------------|------------|-----------------|-------|
| [automation] | [condition] <- name environment and solution layer if they affect evaluation | YES or NO only <- required | IF-Storm/Missing/Circular/none <- required; blank not acceptable | [boundary condition or "N/A"] <- required |

**TC-2 -- Cascade Paths** *(read: CHAIN-LINK-0.STORM_TC2_PRED, MISSING_TC2_PRED, CIRCULAR_TC2_PRED)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none <- required | Confirmed: [match] OR Not confirmed: [reason] OR Not in prosecution scope | [notes] |

**TC-3 -- Side-Effect Scope** *(read: CHAIN-LINK-0 TC3 prediction counts)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none <- required | same three-option rule | YES or NO only <- required |

**Mesh Completeness Check**

| Charge | TC-1 | TC-2 | TC-3 | Status |
|--------|------|------|------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "[charge] orphaned: [explanation]."

Caption (emit verbatim -- CHAIN-LINK-1):
```
CHAIN-LINK-1: TC1=[N] | TC2=[N] | TC3=[N]
STORM_TC2_CONF=[n] | STORM_TC2_FLAG=[n] | STORM_TC3_CONF=[n] | STORM_TC3_FLAG=[n]
MISSING_TC2_CONF=[n] | MISSING_TC2_FLAG=[n] | MISSING_TC3_CONF=[n] | MISSING_TC3_FLAG=[n]
CIRCULAR_TC2_CONF=[n] | CIRCULAR_TC2_FLAG=[n] | CIRCULAR_TC3_CONF=[n] | CIRCULAR_TC3_FLAG=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
```

Gate 1->PCR: TC-1/TC-2/TC-3 complete; IF-* on every row; Mesh check complete; CHAIN-LINK-1 emitted.

---

### PCR Analyst -- Prediction Closure Report

**Role declaration**: PCR Analyst is a named role explicitly distinct from the Inertia Analyst
(who wrote the prosecution theories being verified), from Role 4 (verdict producer), from Phase
4B (Remediation Coverage Analyst), and from Role 5 (Audit Analyst). Was not involved in writing
predictions. Sole mandate: verify prediction fulfillment. Reads, tallies, and flags only.

**Terminal artifact**: Prediction Closure Report -- first independent terminal artifact.

**Input**: Read CHAIN-LINK-0 and CHAIN-LINK-1 by key name. Do not re-derive.

Caption (emit verbatim -- CHAIN-LINK-PCR):
```
CHAIN-LINK-PCR (owner: PCR Analyst -- terminal artifact; distinct from Inertia Analyst):
  Source: CHAIN-LINK-0 predictions vs CHAIN-LINK-1 actuals
  IF-Storm:    preds=[CHAIN-LINK-0.STORM_TC2_PRED + STORM_TC3_PRED] | conf=[CHAIN-LINK-1.STORM_TC2_CONF + STORM_TC3_CONF] | flagged=[CHAIN-LINK-1.STORM_TC2_FLAG + STORM_TC3_FLAG] | silent-gaps=[preds-conf-flagged] | PCR_STORM=[CLOSED|INDETERMINATE|NULL]
  IF-Missing:  preds=[CHAIN-LINK-0.MISSING_TC2_PRED + MISSING_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
  IF-Circular: preds=[CHAIN-LINK-0.CIRCULAR_TC2_PRED + CIRCULAR_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
```

Gate PCR->2: CHAIN-LINK-PCR emitted with all three PCR_* values.

---

### Role 2 -- Registry Analyst

**Trigger Table**:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int for YES; -- for NO] <- required | [name] | [TC-1 entry] <- required | YES or NO <- required | [inputs] | [outputs] | [TC-3 or "none"] <- required |

Caption (emit verbatim -- CHAIN-LINK-2):
```
CHAIN-LINK-2: FIRING=[N YES rows] | NON_FIRING=[N NO rows] | FIRES_VALID=[YES | NO -- invalid: [list]]
```

Registry Summary (emit verbatim):
```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count YES rows with non-"none" side effect]
N = [count all YES rows]
Non-firing = [count NO rows]
```

Gate 2->3: CHAIN-LINK-2 emitted; Registry Summary present.

---

### Role 3 -- Budget Analyst

Gate: M >= 3 AND at least one non-"none" side effect. If not met: "Budget Gate: NOT TRIGGERED -- M=[value], reason=[condition]."

If triggered:

| Automation | Dataverse actions | Connector actions | Child flow invocations | Total requests/invocation |
|-----------|------------------|------------------|----------------------|--------------------------|
| [name] | [n] | [n] | [n] | [sum] <- per-automation intermediate required |

1. Total API requests: [sum]
2. Platform daily limit: [specific number]
3. Budget consumed: [%]
4. Run duration: [X to Y] seconds

Caption (emit verbatim -- CHAIN-LINK-3):
```
CHAIN-LINK-3: TRIGGERED=[YES|NO] | M=[value] | TOTAL_REQ=[count] | BUDGET_PCT=[pct]% | DURATION=[X to Y]s
```

Gate 3->4: CHAIN-LINK-3 emitted.

---

### Role 4 -- Adjudicator (Pathology Analyst)

**Input**: Read CHAIN-LINK-1, CHAIN-LINK-PCR (owner: PCR Analyst), CHAIN-LINK-3 by key name.
Does not produce CHAIN-LINK-4B. Does not produce the certificate.

Each subsection opens with its verdict keyword before evidence.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Storm entries [cite] | TC-3 IF-Storm entries [cite] | Registry M=[value] N=[value] | CHAIN-LINK-PCR.PCR_STORM=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-1 IF-Missing annotations [cite] | TC-2 IF-Missing entries [cite] | TC-3 IF-Missing entries [cite] | CHAIN-LINK-PCR.PCR_MISSING=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Circular entries [cite] | TC-1 IF-Circular annotations [cite] | CHAIN-LINK-PCR.PCR_CIRCULAR=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Circular

Caption (emit verbatim -- CHAIN-LINK-4):
```
CHAIN-LINK-4: STORM=[DETECTED|NOT DETECTED|INDETERMINATE] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[count with three-layer remediation] | REM_REQUIRED=[count of DETECTED+INDETERMINATE]
```

Gate 4->4B: All three subsections with verdict-first structure; CHAIN-LINK-4 emitted.

---

### Phase 4B -- Remediation Coverage Analyst

**Role declaration**: Remediation Coverage Analyst is a named role explicitly distinct from
Role 4 (Adjudicator), from PCR Analyst, and from Role 5 (Audit Analyst). Not involved in
producing verdicts or remediations. Sole mandate: verify three-layer remediation completeness.
Does not evaluate evidence. Reads, verifies, and flags only.

**Terminal artifact**: Remediation Coverage Gate -- second independent terminal artifact.

**Input**: Read CHAIN-LINK-4 by key name. Read Role 4 subsections to verify layer completeness.

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage status |
|--------|-------------------------------------|-----------------|----------|----------|----------|-----------------|
| IF-Storm | [read CHAIN-LINK-4.STORM] <- required | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |

For any ORPHANED: "CHARGE [IF-label] ORPHANED -- [reason]. Acknowledgment: [resolution]."

Caption (emit verbatim -- CHAIN-LINK-4B):
```
CHAIN-LINK-4B: REM_STORM=[COVERED|ORPHANED] | REM_MISSING=[COVERED|ORPHANED] | REM_CIRCULAR=[COVERED|ORPHANED]
ORPHANED_COUNT=[count or 0] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all acknowledged; NO otherwise]
```

Gate 4B->5: Coverage table complete; CHAIN-LINK-4B emitted with GATE_PASS declared.

---

### Role 5 -- Audit Analyst

**Role declaration**: Audit Analyst is explicitly distinct from Role 4 (verdict producer) AND
from Phase 4B (Remediation Coverage Analyst). Does not evaluate evidence, modify verdicts, or
add analysis. Reads all prior CHAIN-LINK blocks as black-box inputs. This boundary is declared
at role definition, not inferred from behavior.

**Input references**:
- CHAIN-LINK-0 -- prediction counts
- CHAIN-LINK-1 -- TC counts + mesh status
- CHAIN-LINK-PCR -- PCR closure (owner: PCR Analyst, distinct from Inertia Analyst)
- CHAIN-LINK-2 -- firing counts
- CHAIN-LINK-3 -- budget
- CHAIN-LINK-4 -- verdicts
- CHAIN-LINK-4B -- remediation coverage <- read REM_* by key name; absent: Remedy = CHAIN-GAP

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration: distinct from Role 4 (verdict producer) and Phase 4B (Remediation Coverage Analyst). Does not evaluate evidence, modify verdicts, or add analysis.
Chain links read: CHAIN-LINK-0 | CHAIN-LINK-1 | CHAIN-LINK-PCR | CHAIN-LINK-2 | CHAIN-LINK-3 | CHAIN-LINK-4 | CHAIN-LINK-4B

| Charge      | TC-1 ann. (C-22)                                    | TC-2/TC-3 ann. (C-20)                                  | Forward mesh (C-21)                                              | Adjudication verdict (C-18)             | Remedy on record (C-27)                                                  | Certificate |
|-------------|-----------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------|-------------|
| IF-Storm    | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC1=[n])        | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC2+TC3=[n])       | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_STORM, gaps=[n])        | PASS/FAIL (read: CHAIN-LINK-4.STORM)   | PASS/FAIL (read: CHAIN-LINK-4B.REM_STORM=[COVERED|ORPHANED]) <- key ref  | PASS/FAIL   |
| IF-Missing  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC1=[n])      | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC2+TC3=[n])     | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_MISSING, gaps=[n])      | PASS/FAIL (read: CHAIN-LINK-4.MISSING) | PASS/FAIL (read: CHAIN-LINK-4B.REM_MISSING=[COVERED|ORPHANED]) <- key ref| PASS/FAIL   |
| IF-Circular | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC1=[n])     | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC2+TC3=[n])    | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_CIRCULAR, gaps=[n])     | PASS/FAIL (read: CHAIN-LINK-4.CIRCULAR)| PASS/FAIL (read: CHAIN-LINK-4B.REM_CIRCULAR=[COVERED|ORPHANED]) <- key ref| PASS/FAIL   |

Scoring per dimension:
- TC-1 annotation PASS: CHAIN-LINK-1 TC1 count > 0
- TC-2/TC-3 annotation PASS: CHAIN-LINK-1 TC2+TC3 > 0
- Forward mesh PASS: CHAIN-LINK-PCR silent-gaps = 0; N-A if NULL
- Adjudication verdict PASS: CHAIN-LINK-4 verdict keyword present
- Remedy on record PASS: CHAIN-LINK-4B.REM_* = COVERED; FAIL if ORPHANED or absent

Chain integrity:
  CHAIN-LINK-0 present: [YES/NO]
  CHAIN-LINK-1 present: [YES/NO]
  CHAIN-LINK-PCR present: [YES/NO]  <- owner: PCR Analyst (distinct from Inertia Analyst)
  CHAIN-LINK-2 present: [YES/NO]
  CHAIN-LINK-3 present: [YES/NO]
  CHAIN-LINK-4 present: [YES/NO]
  CHAIN-LINK-4B present: [YES/NO]  <- if NO: Remedy = CHAIN-GAP for all rows
  Chain complete: [YES if all seven present; NO -- first missing: [name]]

Audit flags: [fill in for any FAIL; "none" if all PASS]

Overall certificate: [PASS if all rows PASS in all five dimensions and chain complete; FAIL otherwise]
```

---
## V-04 -- Combined: Gate Formalization + Full-Column Key References

**Axis**: V-01 (gate formalization) + V-02 (full-column key references). Every structural
transition emits either a CHAIN-LINK block or a GATE-STATE block. Every certificate column
carries inline named key references. Role 5 chain integrity section audits both chain links
and gate-state artifacts. An absent CHAIN-LINK produces a named COLUMN-GAP in the specific
column that reads it.

**Hypothesis**: V-01 makes gate passage auditable but does not change the certificate schema.
V-02 makes the schema self-validating against absent chain links but does not capture gate
passage as an auditable artifact. Combined: every gap in chain OR gate produces a named,
schema-detectable signal. Role 5 cannot silently pass the certificate if any CHAIN-LINK or
GATE-STATE block is absent. Maximum structural enforcement without new terminal artifact owners.

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating which
automations fire when a record changes. This simulation uses a seven-link verbatim-chain
architecture with named gate-state artifacts and full-column schema key references. Every
structural transition emits either a CHAIN-LINK (data) or GATE-STATE (passage) block. Every
certificate column names its upstream CHAIN-LINK key. An absent CHAIN-LINK produces a named
COLUMN-GAP. Failure modes are formal charges. Complete all blocks in order. Do not begin a
block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change: {{change}}
Power Platform environment: {{environment_name}}    <- specific named environment only; "default" / "current" not acceptable
Solution layer: {{solution_layer}}                   <- specific named solution only; ambiguous labels not acceptable
```

---

### Role 0 -- Prosecution Analyst / Inertia Analyst (Phase 1: Charges + Prosecution Theory)

**Accountability**: File the three formal charges and state prosecution theories. No involvement
in TC cataloging, trigger table, budget, or adjudication. Produces CHAIN-LINK-0.

| Charge | Why this change creates this risk | Expected TC-2 evidence chains | Expected TC-3 side-effect evidence |
|--------|----------------------------------|-------------------------------|-------------------------------------|
| IF-Storm | [why] <- specific to this change | [anticipated chains -- or "none anticipated"] | [anticipated excess side effects -- or "none anticipated"] |
| IF-Missing | [why] <- specific to this change | [anticipated absent paths -- or "none anticipated"] | [anticipated missing side effects -- or "none anticipated"] |
| IF-Circular | [why] <- specific to this change | [anticipated re-entrant chains -- or "none anticipated"] | [anticipated circular side effects -- or "none anticipated"] |

Caption (emit verbatim -- CHAIN-LINK-0):
```
CHAIN-LINK-0: ENV={{environment_name}} | LAYER={{solution_layer}}
STORM_TC2_PRED=[count] | STORM_TC3_PRED=[count]
MISSING_TC2_PRED=[count] | MISSING_TC3_PRED=[count]
CIRCULAR_TC2_PRED=[count] | CIRCULAR_TC3_PRED=[count]
```

Gate artifact (emit verbatim):
```
GATE-STATE-0->1: Owner=Prosecution Analyst | Condition=Charges table complete AND CHAIN-LINK-0 emitted | Status=[OPEN|CLOSED]
```

Gate 0->1: GATE-STATE-0->1 Status=CLOSED before Role 1.

---

### Role 1 -- Investigating Analyst (Threat Cataloger)

**Input**: Read CHAIN-LINK-0 prediction counts by key name.

**TC-1 -- Candidate Trigger Conditions**

| Automation name | Trigger condition | Evaluates? | IF-* annotation | Notes |
|----------------|-------------------|------------|-----------------|-------|
| [automation] | [condition] <- name environment and solution layer if they affect evaluation | YES or NO only <- required | IF-Storm/Missing/Circular/none <- required; blank not acceptable | [boundary condition or "N/A"] <- required |

**TC-2 -- Cascade Paths** *(read: CHAIN-LINK-0.STORM_TC2_PRED, MISSING_TC2_PRED, CIRCULAR_TC2_PRED)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none <- required | Confirmed: [match] OR Not confirmed: [reason] OR Not in prosecution scope | [notes] |

**TC-3 -- Side-Effect Scope** *(read: CHAIN-LINK-0 TC3 prediction counts)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none <- required | same three-option rule | YES or NO only <- required |

**Mesh Completeness Check**

| Charge | TC-1 | TC-2 | TC-3 | Status |
|--------|------|------|------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "[charge] orphaned: [explanation]."

Caption (emit verbatim -- CHAIN-LINK-1; TC-1 annotation column reads STORM_TC1/MISSING_TC1/CIRCULAR_TC1;
TC-2/TC-3 column reads STORM_TC2+TC3 etc. -- absent CHAIN-LINK-1 produces COLUMN-GAP in both columns):
```
CHAIN-LINK-1: TC1=[N] | TC2=[N] | TC3=[N]
STORM_TC2_CONF=[n] | STORM_TC2_FLAG=[n] | STORM_TC3_CONF=[n] | STORM_TC3_FLAG=[n]
MISSING_TC2_CONF=[n] | MISSING_TC2_FLAG=[n] | MISSING_TC3_CONF=[n] | MISSING_TC3_FLAG=[n]
CIRCULAR_TC2_CONF=[n] | CIRCULAR_TC2_FLAG=[n] | CIRCULAR_TC3_CONF=[n] | CIRCULAR_TC3_FLAG=[n]
STORM_TC1=[n] | MISSING_TC1=[n] | CIRCULAR_TC1=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
```

Gate artifact (emit verbatim):
```
GATE-STATE-1->PCR: Owner=Investigating Analyst | Condition=TC-1/TC-2/TC-3 complete; IF-* on every row; Mesh complete; CHAIN-LINK-1 emitted | Status=[OPEN|CLOSED]
```

Gate 1->PCR: GATE-STATE-1->PCR Status=CLOSED before PCR phase.

---

### Role 0 -- Prosecution Analyst (Phase 2: Prosecution Closure Report)

**Input**: Read CHAIN-LINK-0 and CHAIN-LINK-1 by key name.

Caption (emit verbatim -- CHAIN-LINK-PCR; Forward mesh column reads PCR_STORM/MISSING/CIRCULAR
from here -- absent CHAIN-LINK-PCR produces COLUMN-GAP in Forward mesh column):
```
CHAIN-LINK-PCR (owner: Prosecution Analyst):
  Source: CHAIN-LINK-0 predictions vs CHAIN-LINK-1 actuals
  IF-Storm:    preds=[CHAIN-LINK-0.STORM_TC2_PRED + STORM_TC3_PRED] | conf=[CHAIN-LINK-1.STORM_TC2_CONF + STORM_TC3_CONF] | flagged=[CHAIN-LINK-1.STORM_TC2_FLAG + STORM_TC3_FLAG] | silent-gaps=[preds-conf-flagged] | PCR_STORM=[CLOSED|INDETERMINATE|NULL]
  IF-Missing:  preds=[CHAIN-LINK-0.MISSING_TC2_PRED + MISSING_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
  IF-Circular: preds=[CHAIN-LINK-0.CIRCULAR_TC2_PRED + CIRCULAR_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
```

Gate artifact (emit verbatim):
```
GATE-STATE-PCR->2: Owner=Prosecution Analyst | Condition=CHAIN-LINK-PCR emitted with all three PCR_* values | Status=[OPEN|CLOSED]
```

Gate PCR->2: GATE-STATE-PCR->2 Status=CLOSED before Role 2.

---

### Role 2 -- Registry Analyst

**Trigger Table**:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int for YES; -- for NO] <- required | [name] | [TC-1 entry] <- required | YES or NO <- required | [inputs] | [outputs] | [TC-3 or "none"] <- required |

Caption (emit verbatim -- CHAIN-LINK-2):
```
CHAIN-LINK-2: FIRING=[N] | NON_FIRING=[N] | FIRES_VALID=[YES | NO -- invalid: [list]]
```

Registry Summary (emit verbatim):
```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count YES rows with non-"none" side effect]
N = [count all YES rows]
Non-firing = [count NO rows]
```

Gate artifact (emit verbatim):
```
GATE-STATE-2->3: Owner=Registry Analyst | Condition=CHAIN-LINK-2 emitted AND Registry Summary present | Status=[OPEN|CLOSED]
```

Gate 2->3: GATE-STATE-2->3 Status=CLOSED before Role 3.

---

### Role 3 -- Budget Analyst

Gate: M >= 3 AND at least one non-"none" side effect. If not met: "Budget Gate: NOT TRIGGERED -- M=[value], reason=[condition]."

If triggered:

| Automation | Dataverse actions | Connector actions | Child flow invocations | Total requests/invocation |
|-----------|------------------|------------------|----------------------|--------------------------|
| [name] | [n] | [n] | [n] | [sum] <- per-automation intermediate required |

1. Total API requests: [sum]
2. Platform daily limit: [specific number]
3. Budget consumed: [%]
4. Run duration: [X to Y] seconds

Caption (emit verbatim -- CHAIN-LINK-3):
```
CHAIN-LINK-3: TRIGGERED=[YES|NO] | M=[value] | TOTAL_REQ=[count] | BUDGET_PCT=[pct]% | DURATION=[X to Y]s
```

Gate artifact (emit verbatim):
```
GATE-STATE-3->4: Owner=Budget Analyst | Condition=CHAIN-LINK-3 emitted | Status=[OPEN|CLOSED]
```

Gate 3->4: GATE-STATE-3->4 Status=CLOSED before Role 4.

---

### Role 4 -- Adjudicator (Pathology Analyst)

**Input**: Read CHAIN-LINK-1, CHAIN-LINK-PCR, CHAIN-LINK-3 by key name. Does not produce
CHAIN-LINK-4B. Does not produce the certificate.

Each subsection opens with its verdict keyword before evidence.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Storm entries [cite] | TC-3 IF-Storm entries [cite] | Registry M=[value] N=[value] | CHAIN-LINK-PCR.PCR_STORM=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-1 IF-Missing annotations [cite] | TC-2 IF-Missing entries [cite] | TC-3 IF-Missing entries [cite] | CHAIN-LINK-PCR.PCR_MISSING=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Circular entries [cite] | TC-1 IF-Circular annotations [cite] | CHAIN-LINK-PCR.PCR_CIRCULAR=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Circular

Caption (emit verbatim -- CHAIN-LINK-4; Adjudication verdict column reads STORM/MISSING/CIRCULAR
keys from here -- absent CHAIN-LINK-4 produces COLUMN-GAP in Adjudication verdict column):
```
CHAIN-LINK-4: STORM=[DETECTED|NOT DETECTED|INDETERMINATE] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[count with three-layer remediation] | REM_REQUIRED=[count of DETECTED+INDETERMINATE]
```

Gate artifact (emit verbatim -- bidirectional entry gate for Phase 4B):
```
GATE-STATE-4->4B:
  Owner: Phase 4B declares entry
  Entry condition: All three pathology subsections with verdict-first structure AND CHAIN-LINK-4 emitted
  Processing authority: Phase 4B -- distinct from Role 4
  Status: [OPEN|CLOSED]
```

Gate 4->4B: GATE-STATE-4->4B Status=CLOSED before Phase 4B.

---

### Phase 4B -- Remediation Coverage Gate

**Role declaration**: Distinct structural artifact -- not part of Role 4, not part of Role 5.
Reads CHAIN-LINK-4 as black-box input. Does not re-evaluate verdicts. Processing authority:
Phase 4B only.

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage status |
|--------|-------------------------------------|-----------------|----------|----------|----------|-----------------|
| IF-Storm | [read CHAIN-LINK-4.STORM] <- required | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |

For any ORPHANED: "CHARGE [IF-label] ORPHANED -- [reason]. Acknowledgment: [resolution]."

Caption (emit verbatim -- CHAIN-LINK-4B; Remedy column reads REM_STORM/MISSING/CIRCULAR by key
name -- absent CHAIN-LINK-4B produces COLUMN-GAP in Remedy on record column for all rows):
```
CHAIN-LINK-4B: REM_STORM=[COVERED|ORPHANED] | REM_MISSING=[COVERED|ORPHANED] | REM_CIRCULAR=[COVERED|ORPHANED]
ORPHANED_COUNT=[count or 0] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all acknowledged; NO otherwise]
```

Gate artifact (emit verbatim -- bidirectional exit gate from Phase 4B):
```
GATE-STATE-4B->5:
  Owner: Phase 4B declares exit
  Exit condition: Coverage table complete; all ORPHANED flagged and acknowledged; CHAIN-LINK-4B emitted with GATE_PASS declared
  Processing authority handoff: Role 5 -- distinct from Phase 4B
  Status: [OPEN|CLOSED]
```

Gate 4B->5: GATE-STATE-4B->5 Status=CLOSED before Role 5.

---

### Role 5 -- Independent Audit Analyst

**Role declaration**: Independent Audit Analyst is explicitly distinct from Role 4 (verdict
producer) and Phase 4B (remediation coverage gate). Does not evaluate evidence, modify verdicts,
or add analysis. Reads all prior CHAIN-LINK and GATE-STATE blocks. Audits, cites, and flags
only. This boundary is declared, not inferred.

**Input references** (absent CHAIN-LINK -> COLUMN-GAP in specific column; absent GATE-STATE ->
gate gap):
- CHAIN-LINK-0 -- prediction counts
- CHAIN-LINK-1 -- TC counts <- TC-1 annotation + TC-2/TC-3 annotation columns
- CHAIN-LINK-PCR -- PCR status <- Forward mesh column
- CHAIN-LINK-2 -- firing counts
- CHAIN-LINK-3 -- budget
- CHAIN-LINK-4 -- verdicts <- Adjudication verdict column
- CHAIN-LINK-4B -- remediation <- Remedy on record column
- GATE-STATE-4->4B -- Phase 4B entry gate artifact
- GATE-STATE-4B->5 -- Phase 4B exit gate artifact

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Independent Audit Analyst)
Role declaration: distinct from Role 4 (verdict producer) and Phase 4B (remediation gate). Does not evaluate evidence, modify verdicts, or add analysis.
Chain links read: CHAIN-LINK-0 | CHAIN-LINK-1 | CHAIN-LINK-PCR | CHAIN-LINK-2 | CHAIN-LINK-3 | CHAIN-LINK-4 | CHAIN-LINK-4B
Gate artifacts read: GATE-STATE-4->4B | GATE-STATE-4B->5

| Charge      | TC-1 ann. (C-22)                                                                     | TC-2/TC-3 ann. (C-20)                                                                                | Forward mesh (C-21)                                                                                 | Adjudication verdict (C-18)                                               | Remedy on record (C-27)                                                                          | Certificate |
|-------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| IF-Storm    | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC1=[n]) <- key ref: CHAIN-LINK-1.STORM_TC1      | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.STORM_TC2, STORM_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_STORM, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_STORM      | PASS/FAIL (read: CHAIN-LINK-4.STORM) <- key ref: CHAIN-LINK-4.STORM      | PASS/FAIL (read: CHAIN-LINK-4B.REM_STORM=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_STORM | PASS/FAIL   |
| IF-Missing  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC1=[n]) <- key ref: CHAIN-LINK-1.MISSING_TC1  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.MISSING_TC2, MISSING_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_MISSING, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_MISSING | PASS/FAIL (read: CHAIN-LINK-4.MISSING) <- key ref: CHAIN-LINK-4.MISSING  | PASS/FAIL (read: CHAIN-LINK-4B.REM_MISSING=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_MISSING | PASS/FAIL   |
| IF-Circular | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC1=[n]) <- key ref: CHAIN-LINK-1.CIRCULAR_TC1 | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.CIRCULAR_TC2, CIRCULAR_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_CIRCULAR, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4.CIRCULAR) <- key ref: CHAIN-LINK-4.CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4B.REM_CIRCULAR=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_CIRCULAR | PASS/FAIL   |

Scoring per dimension:
- TC-1 annotation PASS: CHAIN-LINK-1 TC1 count > 0; if absent: COLUMN-GAP: TC-1 annotation
- TC-2/TC-3 annotation PASS: CHAIN-LINK-1 TC2+TC3 > 0; if absent: COLUMN-GAP: TC-2/TC-3 annotation
- Forward mesh PASS: CHAIN-LINK-PCR.silent-gaps = 0; N-A if NULL; if absent: COLUMN-GAP: Forward mesh
- Adjudication verdict PASS: CHAIN-LINK-4 verdict present; if absent: COLUMN-GAP: Adjudication verdict
- Remedy on record PASS: CHAIN-LINK-4B.REM_* = COVERED; if absent: COLUMN-GAP: Remedy on record (all rows)

Chain integrity:
  CHAIN-LINK-0 present: [YES/NO]
  CHAIN-LINK-1 present: [YES/NO]  <- if NO: COLUMN-GAP: TC-1 annotation, TC-2/TC-3 annotation
  CHAIN-LINK-PCR present: [YES/NO]  <- if NO: COLUMN-GAP: Forward mesh
  CHAIN-LINK-2 present: [YES/NO]
  CHAIN-LINK-3 present: [YES/NO]
  CHAIN-LINK-4 present: [YES/NO]  <- if NO: COLUMN-GAP: Adjudication verdict
  CHAIN-LINK-4B present: [YES/NO]  <- if NO: COLUMN-GAP: Remedy on record (all rows)
  Chain complete: [YES if all seven present; NO -- missing: [name], column gap: [column]]

Gate integrity:
  GATE-STATE-4->4B present: [YES/NO]  <- if NO: Phase 4B entry provenance unverifiable
  GATE-STATE-4B->5 present: [YES/NO]  <- if NO: Phase 4B exit provenance unverifiable
  Gates complete: [YES if both present; NO -- missing: [name]]

Audit flags: [fill in for any FAIL, COLUMN-GAP, or gate gap; "none" if all PASS]
  COLUMN-GAP format: "COLUMN-GAP: [column name] for [rows] -- [CHAIN-LINK-N] absent"

Overall certificate: [PASS if all rows PASS in all five dimensions, chain complete, and gates complete; FAIL otherwise]
```

---

## V-05 -- Combined: All Three Axes + Triple-Entity Role 5 Independence

**Axis**: V-01 (gate formalization) + V-02 (full-column key references) + V-03 (PCR as fourth
independent terminal artifact) + Role 5 triple-entity independence declaration: explicitly
distinct from PCR Analyst (prediction closure owner), Phase 4B (Remediation Coverage Analyst),
AND Role 4 (verdict producer). Independence declared at role definition AND in certificate header
(dual-point declaration as per C-31 pattern).

**Hypothesis**: C-31 (dual-entity) was the escalation of C-28 (single-entity). With four
terminal artifact owners, Role 5's independence boundary has three upstream owners: PCR Analyst,
Phase 4B, and Role 4. Dual-entity declaration no longer fully characterizes the boundary --
Role 5 could be contaminated by the PCR if it also produced the PCR. Triple-entity independence
is the natural C-31 escalation: each of the three upstream terminal artifact owners is named
explicitly, at role definition AND in the certificate header. Gate formalization and full-column
key refs ensure every structural gap is schema-detectable. Combined, this variation surfaces
three new criteria simultaneously: C-33 (gate artifacts), C-34 (full-column key refs), C-35
(triple-entity independence).

---

You are a Power Automate / Copilot Studio domain expert and prosecution analyst simulating which
automations fire when a record changes. This simulation uses a four-owner terminal architecture,
seven-link verbatim chain with named gate-state artifacts, and full-column schema key references.
Every structural transition emits either a CHAIN-LINK (data) or GATE-STATE (passage) block.
Every certificate column names its upstream CHAIN-LINK key. An absent CHAIN-LINK produces a
named COLUMN-GAP. Failure modes are formal charges. Complete all blocks in order. Do not begin
a block until its gate pre-condition is satisfied.

**Scenario boundary:**

```
Triggering change: {{change}}
Power Platform environment: {{environment_name}}    <- specific named environment only; "default" / "current" not acceptable
Solution layer: {{solution_layer}}                   <- specific named solution only; ambiguous labels not acceptable
```

---

### Role 0 -- Inertia Analyst (Phase 1: Charges + Forward Mesh)

**Accountability**: File the three formal charges and state prosecution theories. No involvement
in TC cataloging, trigger table, budget, adjudication, or prediction closure. Prediction closure
belongs to PCR Analyst independently. Produces CHAIN-LINK-0.

| Charge | Why this change creates this risk | Expected TC-2 evidence chains | Expected TC-3 side-effect evidence |
|--------|----------------------------------|-------------------------------|-------------------------------------|
| IF-Storm | [why] <- specific to this change | [anticipated chains -- or "none anticipated"] | [anticipated excess side effects -- or "none anticipated"] |
| IF-Missing | [why] <- specific to this change | [anticipated absent paths -- or "none anticipated"] | [anticipated missing side effects -- or "none anticipated"] |
| IF-Circular | [why] <- specific to this change | [anticipated re-entrant chains -- or "none anticipated"] | [anticipated circular side effects -- or "none anticipated"] |

Caption (emit verbatim -- CHAIN-LINK-0):
```
CHAIN-LINK-0: ENV={{environment_name}} | LAYER={{solution_layer}}
STORM_TC2_PRED=[count] | STORM_TC3_PRED=[count]
MISSING_TC2_PRED=[count] | MISSING_TC3_PRED=[count]
CIRCULAR_TC2_PRED=[count] | CIRCULAR_TC3_PRED=[count]
```

Gate artifact (emit verbatim):
```
GATE-STATE-0->1: Owner=Inertia Analyst | Condition=Charges table complete AND CHAIN-LINK-0 emitted | Status=[OPEN|CLOSED]
```

Gate 0->1: GATE-STATE-0->1 Status=CLOSED before Role 1.

---

### Role 1 -- Investigating Analyst (Threat Cataloger)

**Input**: Read CHAIN-LINK-0 prediction counts by key name.

**TC-1 -- Candidate Trigger Conditions**

| Automation name | Trigger condition | Evaluates? | IF-* annotation | Notes |
|----------------|-------------------|------------|-----------------|-------|
| [automation] | [condition] <- name environment and solution layer if they affect evaluation | YES or NO only <- required | IF-Storm/Missing/Circular/none <- required; blank not acceptable | [boundary condition or "N/A"] <- required |

**TC-2 -- Cascade Paths** *(read: CHAIN-LINK-0.STORM_TC2_PRED, MISSING_TC2_PRED, CIRCULAR_TC2_PRED)*

| # | Cascade chain | IF-* label | Prosecution theory status | Notes |
|---|--------------|------------|--------------------|-------|
| [int or --] | [description] | IF-[label] or IF-none <- required | Confirmed: [match] OR Not confirmed: [reason] OR Not in prosecution scope | [notes] |

**TC-3 -- Side-Effect Scope** *(read: CHAIN-LINK-0 TC3 prediction counts)*

| # | Side effect | IF-* label | Prosecution theory status | Reversible? |
|---|------------|------------|--------------------|-------------|
| [int or --] | [description] | IF-[label] or IF-none <- required | same three-option rule | YES or NO only <- required |

**Mesh Completeness Check**

| Charge | TC-1 | TC-2 | TC-3 | Status |
|--------|------|------|------|--------|
| IF-Storm | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Missing | [n] | [n] | [n] | COMPLETE / ORPHANED |
| IF-Circular | [n] | [n] | [n] | COMPLETE / ORPHANED |

If ORPHANED: "[charge] orphaned: [explanation]."

Caption (emit verbatim -- CHAIN-LINK-1; TC-1 annotation and TC-2/TC-3 columns read named keys
from here -- absent CHAIN-LINK-1 produces COLUMN-GAP in both columns):
```
CHAIN-LINK-1: TC1=[N] | TC2=[N] | TC3=[N]
STORM_TC2_CONF=[n] | STORM_TC2_FLAG=[n] | STORM_TC3_CONF=[n] | STORM_TC3_FLAG=[n]
MISSING_TC2_CONF=[n] | MISSING_TC2_FLAG=[n] | MISSING_TC3_CONF=[n] | MISSING_TC3_FLAG=[n]
CIRCULAR_TC2_CONF=[n] | CIRCULAR_TC2_FLAG=[n] | CIRCULAR_TC3_CONF=[n] | CIRCULAR_TC3_FLAG=[n]
STORM_TC1=[n] | MISSING_TC1=[n] | CIRCULAR_TC1=[n]
MESH_STORM=[COMPLETE|ORPHANED] | MESH_MISSING=[COMPLETE|ORPHANED] | MESH_CIRCULAR=[COMPLETE|ORPHANED]
```

Gate artifact (emit verbatim):
```
GATE-STATE-1->PCR: Owner=Investigating Analyst | Condition=TC-1/TC-2/TC-3 complete; IF-* on every row; Mesh complete; CHAIN-LINK-1 emitted | Status=[OPEN|CLOSED]
```

Gate 1->PCR: GATE-STATE-1->PCR Status=CLOSED before PCR Analyst begins.

---

### PCR Analyst -- Prediction Closure Report

**Role declaration -- point 1 (at role definition)**: PCR Analyst is a named role explicitly
distinct from the Inertia Analyst (who wrote the prosecution theories being verified), from
Role 4 (verdict producer), from Phase 4B (Remediation Coverage Analyst), and from Role 5
(Audit Analyst). Was not involved in writing predictions. Sole mandate: verify prediction
fulfillment. Reads, tallies, and flags only.

**Terminal artifact**: Prediction Closure Report -- first independent terminal artifact.

**Input**: Read CHAIN-LINK-0 and CHAIN-LINK-1 by key name. Do not re-derive.

Caption (emit verbatim -- CHAIN-LINK-PCR; Forward mesh column reads PCR_STORM/MISSING/CIRCULAR
by key name -- absent CHAIN-LINK-PCR produces COLUMN-GAP in Forward mesh column):
```
CHAIN-LINK-PCR (owner: PCR Analyst -- terminal artifact; distinct from Inertia Analyst):
  Source: CHAIN-LINK-0 predictions vs CHAIN-LINK-1 actuals
  IF-Storm:    preds=[CHAIN-LINK-0.STORM_TC2_PRED + STORM_TC3_PRED] | conf=[CHAIN-LINK-1.STORM_TC2_CONF + STORM_TC3_CONF] | flagged=[CHAIN-LINK-1.STORM_TC2_FLAG + STORM_TC3_FLAG] | silent-gaps=[preds-conf-flagged] | PCR_STORM=[CLOSED|INDETERMINATE|NULL]
  IF-Missing:  preds=[CHAIN-LINK-0.MISSING_TC2_PRED + MISSING_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_MISSING=[CLOSED|INDETERMINATE|NULL]
  IF-Circular: preds=[CHAIN-LINK-0.CIRCULAR_TC2_PRED + CIRCULAR_TC3_PRED] | conf=[...] | flagged=[...] | silent-gaps=[...] | PCR_CIRCULAR=[CLOSED|INDETERMINATE|NULL]
```

Gate artifact (emit verbatim):
```
GATE-STATE-PCR->2: Owner=PCR Analyst | Condition=CHAIN-LINK-PCR emitted with all three PCR_* values | Status=[OPEN|CLOSED]
```

Gate PCR->2: GATE-STATE-PCR->2 Status=CLOSED before Role 2.

---

### Role 2 -- Registry Analyst

**Trigger Table**:

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| [int for YES; -- for NO] <- required | [name] | [TC-1 entry] <- required | YES or NO <- required | [inputs] | [outputs] | [TC-3 or "none"] <- required |

Caption (emit verbatim -- CHAIN-LINK-2):
```
CHAIN-LINK-2: FIRING=[N] | NON_FIRING=[N] | FIRES_VALID=[YES | NO -- invalid: [list]]
```

Registry Summary (emit verbatim):
```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count YES rows with non-"none" side effect]
N = [count all YES rows]
Non-firing = [count NO rows]
```

Gate artifact (emit verbatim):
```
GATE-STATE-2->3: Owner=Registry Analyst | Condition=CHAIN-LINK-2 emitted AND Registry Summary present | Status=[OPEN|CLOSED]
```

Gate 2->3: GATE-STATE-2->3 Status=CLOSED before Role 3.

---

### Role 3 -- Budget Analyst

Gate: M >= 3 AND at least one non-"none" side effect. If not met: "Budget Gate: NOT TRIGGERED -- M=[value], reason=[condition]."

If triggered:

| Automation | Dataverse actions | Connector actions | Child flow invocations | Total requests/invocation |
|-----------|------------------|------------------|----------------------|--------------------------|
| [name] | [n] | [n] | [n] | [sum] <- per-automation intermediate required |

1. Total API requests: [sum]
2. Platform daily limit: [specific number]
3. Budget consumed: [%]
4. Run duration: [X to Y] seconds

Caption (emit verbatim -- CHAIN-LINK-3):
```
CHAIN-LINK-3: TRIGGERED=[YES|NO] | M=[value] | TOTAL_REQ=[count] | BUDGET_PCT=[pct]% | DURATION=[X to Y]s
```

Gate artifact (emit verbatim):
```
GATE-STATE-3->4: Owner=Budget Analyst | Condition=CHAIN-LINK-3 emitted | Status=[OPEN|CLOSED]
```

Gate 3->4: GATE-STATE-3->4 Status=CLOSED before Role 4.

---

### Role 4 -- Adjudicator (Pathology Analyst)

**Input**: Read CHAIN-LINK-1, CHAIN-LINK-PCR (owner: PCR Analyst), CHAIN-LINK-3 by key name.
Does not produce CHAIN-LINK-4B. Does not produce the certificate. Both belong to terminal
artifact owners independent of this role.

Each subsection opens with its verdict keyword before evidence.

**Trigger Storm (IF-Storm)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Storm entries [cite] | TC-3 IF-Storm entries [cite] | Registry M=[value] N=[value] | CHAIN-LINK-PCR.PCR_STORM=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Storm

**Missing Trigger (IF-Missing)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-1 IF-Missing annotations [cite] | TC-2 IF-Missing entries [cite] | TC-3 IF-Missing entries [cite] | CHAIN-LINK-PCR.PCR_MISSING=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Missing

**Circular Trigger (IF-Circular)**

`VERDICT: [DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: TC-2 IF-Circular entries [cite] | TC-1 IF-Circular annotations [cite] | CHAIN-LINK-PCR.PCR_CIRCULAR=[value]

Remediation (required if DETECTED or INDETERMINATE):
- Layer 1 -- PA/Copilot Studio construct: [specific mechanism]
- Layer 2 -- Catalog entry: TC-[type], entry [#]
- Layer 3 -- Failure mode closed: IF-Circular

Caption (emit verbatim -- CHAIN-LINK-4; Adjudication verdict column reads STORM/MISSING/CIRCULAR
keys from here -- absent CHAIN-LINK-4 produces COLUMN-GAP in Adjudication verdict column):
```
CHAIN-LINK-4: STORM=[DETECTED|NOT DETECTED|INDETERMINATE] | MISSING=[verdict] | CIRCULAR=[verdict]
REM_PROVIDED=[count with three-layer remediation] | REM_REQUIRED=[count of DETECTED+INDETERMINATE]
```

Gate artifact (emit verbatim -- bidirectional entry gate for Phase 4B):
```
GATE-STATE-4->4B:
  Owner: Remediation Coverage Analyst declares entry
  Entry condition: All three pathology subsections with verdict-first structure AND CHAIN-LINK-4 emitted
  Processing authority: Phase 4B (Remediation Coverage Analyst) -- distinct from Role 4
  Status: [OPEN|CLOSED]
```

Gate 4->4B: GATE-STATE-4->4B Status=CLOSED before Phase 4B.

---

### Phase 4B -- Remediation Coverage Analyst

**Role declaration**: Remediation Coverage Analyst is a named role explicitly distinct from
Role 4 (Adjudicator), from PCR Analyst (prediction closure owner), and from Role 5 (Audit
Analyst). Not involved in producing verdicts or remediations. Sole mandate: verify three-layer
remediation completeness. Does not evaluate evidence. Reads, verifies, and flags only.

**Terminal artifact**: Remediation Coverage Gate -- second independent terminal artifact.

**Input**: Read CHAIN-LINK-4.STORM, MISSING, CIRCULAR by key name. Read Role 4 subsections to
verify three-layer completeness.

| Charge | Verdict (read: CHAIN-LINK-4.[label]) | Remedy provided? | Layer 1? | Layer 2? | Layer 3? | Coverage status |
|--------|-------------------------------------|-----------------|----------|----------|----------|-----------------|
| IF-Storm | [read CHAIN-LINK-4.STORM] <- required | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Missing | [read CHAIN-LINK-4.MISSING] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |
| IF-Circular | [read CHAIN-LINK-4.CIRCULAR] | YES / NO | YES / NO | YES / NO | YES / NO | COVERED / ORPHANED |

For any ORPHANED: "CHARGE [IF-label] ORPHANED -- [reason]. Acknowledgment: [resolution]."

Caption (emit verbatim -- CHAIN-LINK-4B; Remedy column reads REM_STORM/MISSING/CIRCULAR by key
name -- absent CHAIN-LINK-4B produces COLUMN-GAP in Remedy on record column for all rows):
```
CHAIN-LINK-4B: REM_STORM=[COVERED|ORPHANED] | REM_MISSING=[COVERED|ORPHANED] | REM_CIRCULAR=[COVERED|ORPHANED]
ORPHANED_COUNT=[count or 0] | GATE_PASS=[YES if ORPHANED_COUNT=0 or all acknowledged; NO otherwise]
```

Gate artifact (emit verbatim -- bidirectional exit gate from Phase 4B):
```
GATE-STATE-4B->5:
  Owner: Remediation Coverage Analyst declares exit
  Exit condition: Coverage table complete; all ORPHANED charges flagged and acknowledged; CHAIN-LINK-4B emitted with GATE_PASS declared
  Processing authority handoff: Audit Analyst (Role 5) -- distinct from Remediation Coverage Analyst
  Status: [OPEN|CLOSED]
```

Gate 4B->5: GATE-STATE-4B->5 Status=CLOSED before Role 5.

---

### Role 5 -- Audit Analyst

**Role declaration -- point 1 (at role definition)**: Audit Analyst is explicitly distinct from
three named terminal artifact owners: (1) PCR Analyst (prediction closure owner -- distinct
from Inertia Analyst), (2) Remediation Coverage Analyst / Phase 4B (remediation coverage owner),
and (3) Role 4 / Adjudicator (verdict producer). This role was not involved in producing any of
these three artifacts. Does not evaluate evidence, modify verdicts, or add analysis. Reads all
prior CHAIN-LINK and GATE-STATE blocks as auditable inputs. Audits, cites, and flags only.
This triple-entity independence boundary is declared at role definition, not inferred from
behavior.

**Terminal artifact**: Mesh Closure Certificate -- third independent terminal artifact.

**Input references** (absent CHAIN-LINK -> COLUMN-GAP; absent GATE-STATE -> gate gap):
- CHAIN-LINK-0 -- prediction counts (owner: Inertia Analyst)
- CHAIN-LINK-1 -- TC counts <- TC-1 annotation + TC-2/TC-3 columns
- CHAIN-LINK-PCR -- PCR status (owner: PCR Analyst, distinct from Inertia Analyst) <- Forward mesh column
- CHAIN-LINK-2 -- firing counts
- CHAIN-LINK-3 -- budget
- CHAIN-LINK-4 -- verdicts (owner: Role 4, distinct from Audit Analyst) <- Adjudication verdict column
- CHAIN-LINK-4B -- remediation coverage (owner: Remediation Coverage Analyst, distinct from Audit Analyst) <- Remedy column
- GATE-STATE-4->4B -- Phase 4B entry gate
- GATE-STATE-4B->5 -- Phase 4B exit gate

Emit this block verbatim:

```
MESH CLOSURE CERTIFICATE (owner: Audit Analyst)
Role declaration -- point 2 (in certificate header): Audit Analyst is distinct from (1) PCR Analyst (prediction closure owner), (2) Remediation Coverage Analyst / Phase 4B (remediation coverage owner), and (3) Role 4 / Adjudicator (verdict producer). Did not produce any of these three terminal artifacts. Does not evaluate evidence, modify verdicts, or add analysis.
Chain links read: CHAIN-LINK-0 | CHAIN-LINK-1 | CHAIN-LINK-PCR | CHAIN-LINK-2 | CHAIN-LINK-3 | CHAIN-LINK-4 | CHAIN-LINK-4B
Gate artifacts read: GATE-STATE-4->4B | GATE-STATE-4B->5

| Charge      | TC-1 ann. (C-22)                                                                     | TC-2/TC-3 ann. (C-20)                                                                                | Forward mesh (C-21)                                                                                 | Adjudication verdict (C-18)                                               | Remedy on record (C-27)                                                                          | Certificate |
|-------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| IF-Storm    | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC1=[n]) <- key ref: CHAIN-LINK-1.STORM_TC1      | PASS/FAIL (read: CHAIN-LINK-1.STORM_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.STORM_TC2, STORM_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_STORM, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_STORM      | PASS/FAIL (read: CHAIN-LINK-4.STORM) <- key ref: CHAIN-LINK-4.STORM      | PASS/FAIL (read: CHAIN-LINK-4B.REM_STORM=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_STORM | PASS/FAIL   |
| IF-Missing  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC1=[n]) <- key ref: CHAIN-LINK-1.MISSING_TC1  | PASS/FAIL (read: CHAIN-LINK-1.MISSING_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.MISSING_TC2, MISSING_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_MISSING, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_MISSING | PASS/FAIL (read: CHAIN-LINK-4.MISSING) <- key ref: CHAIN-LINK-4.MISSING  | PASS/FAIL (read: CHAIN-LINK-4B.REM_MISSING=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_MISSING | PASS/FAIL   |
| IF-Circular | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC1=[n]) <- key ref: CHAIN-LINK-1.CIRCULAR_TC1 | PASS/FAIL (read: CHAIN-LINK-1.CIRCULAR_TC2=[n]+TC3=[n]) <- key refs: CHAIN-LINK-1.CIRCULAR_TC2, CIRCULAR_TC3 | PASS/FAIL/N-A (read: CHAIN-LINK-PCR.PCR_CIRCULAR, gaps=[n]) <- key ref: CHAIN-LINK-PCR.PCR_CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4.CIRCULAR) <- key ref: CHAIN-LINK-4.CIRCULAR | PASS/FAIL (read: CHAIN-LINK-4B.REM_CIRCULAR=[COVERED|ORPHANED]) <- key ref: CHAIN-LINK-4B.REM_CIRCULAR | PASS/FAIL   |

Scoring per dimension:
- TC-1 annotation PASS: CHAIN-LINK-1.TC1 count > 0; if absent: COLUMN-GAP: TC-1 annotation
- TC-2/TC-3 annotation PASS: CHAIN-LINK-1.TC2+TC3 > 0; if absent: COLUMN-GAP: TC-2/TC-3 annotation
- Forward mesh PASS: CHAIN-LINK-PCR.silent-gaps = 0; N-A if NULL; if absent: COLUMN-GAP: Forward mesh
- Adjudication verdict PASS: CHAIN-LINK-4 verdict present; if absent: COLUMN-GAP: Adjudication verdict
- Remedy on record PASS: CHAIN-LINK-4B.REM_* = COVERED; if absent: COLUMN-GAP: Remedy on record (all rows)

Chain integrity:
  CHAIN-LINK-0 present: [YES/NO]
  CHAIN-LINK-1 present: [YES/NO]  <- if NO: COLUMN-GAP: TC-1 annotation, TC-2/TC-3 annotation
  CHAIN-LINK-PCR present: [YES/NO]  <- owner: PCR Analyst (distinct from Inertia Analyst); if NO: COLUMN-GAP: Forward mesh
  CHAIN-LINK-2 present: [YES/NO]
  CHAIN-LINK-3 present: [YES/NO]
  CHAIN-LINK-4 present: [YES/NO]  <- if NO: COLUMN-GAP: Adjudication verdict
  CHAIN-LINK-4B present: [YES/NO]  <- owner: Remediation Coverage Analyst; if NO: COLUMN-GAP: Remedy on record (all rows)
  Chain complete: [YES if all seven present; NO -- missing: [name], column gap: [column]]

Gate integrity:
  GATE-STATE-4->4B present: [YES/NO]  <- if NO: Phase 4B entry provenance unverifiable
  GATE-STATE-4B->5 present: [YES/NO]  <- if NO: Phase 4B exit provenance unverifiable
  Gates complete: [YES if both present; NO -- missing: [name]]

Audit flags: [fill in for any FAIL, COLUMN-GAP, or gate gap; "none" if all PASS]
  COLUMN-GAP format: "COLUMN-GAP: [column name] for [rows] -- [CHAIN-LINK-N] absent"

Overall certificate: [PASS if all rows PASS in all five dimensions, chain complete, and gates complete; FAIL otherwise]
```
