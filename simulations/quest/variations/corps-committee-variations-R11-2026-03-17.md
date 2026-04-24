| INERTIA-FINDING-1 | v1 (4 tokens) | [GATE-CLEARED / NOT-CLEARED] | [YES: pre-mortem / dissent row [name] / decision # -- or NO] | [N/A or specific justification] | CONSUMED / NOT-APPLICABLE / DROPPED |
| INERTIA-FINDING-2 | v1 | [GATE STATUS] | [YES: [element] / NO] | [N/A or justification] | CONSUMED / NOT-APPLICABLE / DROPPED |
| INERTIA-FINDING-3 | v1 | [GATE STATUS] | [YES: [element] / NO] | [N/A or justification] | CONSUMED / NOT-APPLICABLE / DROPPED |
| INERTIA-FINDING-4 | v1 | [GATE STATUS] | [YES: [element] / NO] | [N/A or justification] | CONSUMED / NOT-APPLICABLE / DROPPED |

Manifest reconciliation:
  B3-COMMIT MANIFEST current version token count: 4.
  Tokens in this table: [N]. Must equal 4. Count mismatch = unreported token; halt and add.

Cross-reference with Phase 1 TOKEN TRACE MANIFEST:
  GATE-CLEARED in Phase 1 AND DROPPED here = gate-cleared dropout (highest severity).
  NOT-CLEARED in Phase 1 AND CONSUMED here = token appeared without clearing gate; verify label.

STATUS assignment rules (apply in order):
  1. IF CONSUMED column = YES with a cited element: STATUS = CONSUMED.
  2. IF CONSUMED column = NO AND justification is valid (specific constraint cited): STATUS = NOT-APPLICABLE.
  3. IF CONSUMED column = NO AND justification is empty or invalid: STATUS = DROPPED.
  4. A token cannot simultaneously be CONSUMED and NOT-APPLICABLE.

DROPPED REPAIR RULE: Return to Phase 2 (pre-mortem or dissent rows). Add the missing
  token citation. Re-run this table. All DROPPED must become CONSUMED before delivery.

NOT-APPLICABLE AUDIT RULE: For each NOT-APPLICABLE row, confirm the justification
  references an exact Phase 0 charter entry. Vague justifications are invalidated to DROPPED.

### Next Steps
[Follow-up meetings, escalations, or dependencies. Re-entry triggers if verdict is not APPROVED / GO / ACCEPTED.]

PHASE-2-COMMIT: All sections present. TOKEN TRACE CONFIRMATION complete.
  Manifest count reconciliation confirmed (table count = B3 manifest count).
  All tokens: CONSUMED or NOT-APPLICABLE (justified). Zero DROPPED rows.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## AMEND Handling

### AMEND ROUTING TABLE

Amendment scope is determined by which pre-execution block manifests the amendment
invalidates -- not by which phases are affected downstream.

| Amendment Type | Block Manifests Invalidated | Re-COMMIT Required Before Phase Resume |
|---------------|----------------------------|----------------------------------------|
| Participant composition change | B2 (tier rows), B4 (Challenger) | B2-RECOMMIT MANIFEST + B4-RECOMMIT MANIFEST before Phase 0 resumes |
| Committee type change | B1 (vocabulary), B2 (STANCE tokens reference B1) | B1-RECOMMIT MANIFEST + B2-RECOMMIT MANIFEST before Phase 0 resumes |
| Scope change | Phase 0 charter section only | No block RECOMMIT required; charter section re-declared |
| New agenda item | Phase 1 only | No block RECOMMIT required |
| Challenger role removed | B4 | B4-RECOMMIT MANIFEST before Phase 0 resumes |
| Inertia finding correction | B3; B2 (if T1 citation label changes); B4 (if NORM label changes) | B3-RECOMMIT MANIFEST; B2-RECOMMIT MANIFEST and B4-RECOMMIT MANIFEST if affected; before Phase 0 resumes |

### AMEND-AFFECTED SITES (emit before any re-execution begins)

List every output element rendered stale by the amendment, by structural reference
and the specific manifest token affected. Amendment impact must be visible at the
artifact layer before a single phase re-executes.

Format:
```
AMEND-AFFECTED SITES:
Amendment: [describe the change precisely]
Amendment type: [from AMEND ROUTING TABLE above]
Block manifests invalidated: [list blocks + current version]

Stale output elements:
  [block or phase + section] -- [element name] -- STALE: [affected manifest token or assignment] -- Re-run: [action required]
```

Example (participant added):
```
AMEND-AFFECTED SITES:
Amendment: Add [role] as a new participant.
Amendment type: Participant composition change.
Block manifests invalidated: B2 v1 (missing new participant row), B4 v1 (Challenger may change).

Stale output elements:
  B2-COMMIT MANIFEST v1 -- participant roster -- STALE: new participant row absent -- Re-run B2; emit B2-RECOMMIT MANIFEST v2
  B4-COMMIT MANIFEST v1 -- CHALLENGER-ROLE -- STALE: new T1 candidate may qualify; re-designation required -- Re-run B4; emit B4-RECOMMIT MANIFEST v2
  Phase 0 Attendee List -- row count -- STALE: derived from stale B2 manifest -- Re-run Phase 0
  Phase 1 Discussion Grid -- new participant voice absent -- STALE -- Re-run Phase 1
  Phase 2 Dissenting Opinions -- new participant row absent -- STALE -- Re-run Phase 2
  Phase 2 TOKEN TRACE CONFIRMATION -- dissent row count changed -- STALE -- Re-run CONFIRMATION
```

### Re-COMMIT Cycle with Manifest Update (C-34 + C-35)

After AMEND-AFFECTED SITES is complete:

STEP 1: Re-run each invalidated pre-execution block in routing order.

STEP 2: Each re-executed block emits a versioned RECOMMIT MANIFEST (v2 or higher).
  The RECOMMIT MANIFEST includes a delta annotation.

  B1-RECOMMIT MANIFEST v2 (if type changed):
    Delta from v1: Type: [old] → [new]. Tokens changed: [removed tokens], [added tokens].
    Full sealed tokens:
      | Token | Type | Status |
      |-------|------|--------|
      | [new token set] | outcome vocab | SEALED v2 |
    ENFORCE: Phase 0 may NOT resume until this manifest is present.

  B3-RECOMMIT MANIFEST v2 (if findings corrected):
    Delta from v1:
      Modified findings: [INERTIA-FINDING-N changed from "[old anchor]" to "[new anchor]"]
      Token count: v1: 4, v2: [N] (must still equal TOKEN TRACE CONFIRMATION row count).
    Full INERTIA RECORD: [all tokens with updated values]
    INVARIANT: downstream sites that cited the changed token must be re-validated.
    ENFORCE: B2 and B4 must re-check their T1 citation and NORM obligation against this manifest v2.

  B2-RECOMMIT MANIFEST v2:
    Delta from v1:
      ADDED rows: [list new participants + tier]
      REMOVED rows: [list removed participants]
      MODIFIED rows: [list changed tier or STANCE assignments]
    Full manifest (all rows including changed):
      | Participant | Role | Tier | STANCE-from-B1 | Inertia Citation | Row Status |
      |-------------|------|------|----------------|-----------------|------------|
      | [all rows] | ... | SEALED v2 |
    Tier count: T1: [N], T2: [N], T3: [N]. Manifest version: v2.
    ENFORCE: Phase 0 may NOT resume until this manifest is present.

  B4-RECOMMIT MANIFEST v2:
    Delta from v1:
      Challenger changed: [YES / NO]
      Updated CHALLENGER-ROLE: [new role or "unchanged"]
      Updated CHALLENGER-NORM: [new INERTIA-FINDING-N or "unchanged"]
      Rationale updated: [YES / NO]
    Full manifest:
      | Token | Value | Source Manifest |
      |-------|-------|-----------------|
      | CHALLENGER-ROLE | [value] | B2-RECOMMIT MANIFEST v2 |
      | CHALLENGER-TIER | T1 | B2-RECOMMIT MANIFEST v2 |
      | CHALLENGER-RATIONALE | [value] | (committed here) |
      | CHALLENGER-NORM | [value] | B3 manifest (current version) |
    Manifest version: v2. ENFORCE: Phase 0 may NOT resume until this manifest is present.

STEP 3: Phase entry checks verify RECOMMIT MANIFESTS, not original COMMIT MANIFESTS.

  Phase 0 re-entry check (post-amendment):
    B1 manifest (current version) present? [YES / HALT if B1 was re-run]
    B2 manifest (current version) present? [YES / HALT if B2 was re-run]
    B3 manifest (current version) present? [YES / HALT if B3 was re-run]
    B4 manifest (current version) present? [YES / HALT if B4 was re-run]
    Cross-manifest consistency with current versions:
      B4 CHALLENGER-ROLE in B2 current manifest as T1? [YES / HALT]
      B4 CHALLENGER-NORM in B3 current manifest? [YES / HALT]
    All required RECOMMIT MANIFESTS present and consistent? [YES -- resume / HALT]

  The test (C-34): can Phase 0 resume without the upstream RECOMMIT MANIFEST?
  If yes, the block was re-executed but not re-sealed with a manifest -- the amendment
  closed the execution loop but not the availability-and-content loop. HALT.

STEP 4: Resume phases from the first affected phase.

STEP 5: TOKEN TRACE CONFIRMATION must be re-run whenever B3 manifest or dissent rows
  are affected. On re-run:
  - Reconcile against B3 manifest CURRENT VERSION token count (not v1 count if B3 changed).
  - Any token whose prior status was CONSUMED must be re-confirmed in updated output.
  - A formerly CONSUMED token absent after re-execution = DROPPED (repair required).
  - NOT-APPLICABLE justifications that reference scope constraints changed by the amendment
    must be re-validated against the updated Phase 0 charter.
  - Deliver updated minutes only after zero DROPPED rows confirmed in re-run CONFIRMATION.
```

---

## R11 Variation Design Notes

### What each variation isolates or combines

| Variation | New mechanism | Gap from R10 it closes | What it does NOT close |
|-----------|--------------|------------------------|------------------------|
| V-01 | Re-COMMIT cycle after AMEND | R10 V-03 gap: AMEND routing declared, no re-COMMIT closing the loop | Manifest (no token enumeration in seals); three-way CONFIRMATION status |
| V-02 | COMMIT seal token manifest | R10 V-01/V-02 gap: COMMIT seals exist, no manifest for reconciliation | Re-COMMIT cycle (amendments don't update manifests); three-way status |
| V-03 | CONSUMED / NOT-APPLICABLE / DROPPED | R10 CONFIRMATION only detects presence vs complete absence | Manifest (three-way status assumed but manifest reconciliation is weak without C-35); re-COMMIT cycle |
| V-04 | C-34 + C-35 | Re-COMMIT cycle + manifest as linked pair — amendments produce delta-annotated manifests | Three-way CONFIRMATION status (still CONFIRMED / DROPOUT in V-04) |
| V-05 | C-34 + C-35 + C-36 + R10 full | All three new structural properties; closed audit loop | (intended as the aspirational full-integration candidate) |

### Single-axis discriminators expected at scoring

V-01 vs V-02 vs V-03 should each score differently on C-34/C-35/C-36:
- V-01: PASS C-34, FAIL C-35 (no manifest), FAIL C-36 (binary status, no manifest to reconcile against)
- V-02: FAIL C-34 (manifest exists but no re-COMMIT requirement after AMEND), PASS C-35, FAIL C-36 (binary status)
- V-03: FAIL C-34 (no re-COMMIT), FAIL C-35 (no manifest, C-36 reconciliation weak), PASS C-36 (three-way status present but without manifest the audit is incomplete)
- V-04: PASS C-34, PASS C-35, FAIL C-36 (still CONFIRMED/DROPOUT)
- V-05: PASS C-34, PASS C-35, PASS C-36
