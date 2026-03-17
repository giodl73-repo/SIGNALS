Now I have the full v14 rubric and the complete R20 scorecard. Two new criteria to add:

- **C-44**: System-wide EXIT GATE self-routing (from V-02/V-04/V-05, Axis-M)
- **C-45**: BASELINE PROPAGATION MAP as upfront assignment contract (from V-03/V-05, Axis-N)

Formula: 35 → 37 aspirational. `/37 * 10` = 0.270 pts each.

```markdown
# crew-roles rubric — v15

## Changes from v14

Two new aspirational criteria extracted from R20 variations V-02/V-04/V-05 (Axis-M:
Full Self-Routing Gates) and V-03/V-05 (Axis-N: Baseline Propagation Map). Each closes
a structural gap not addressed by any existing criterion.

**C-44 — SYSTEM-WIDE EXIT GATE SELF-ROUTING** (from V-02, V-04, V-05 / Axis-M):
C-43 requires dual-branch routing (PASS→continue; FAIL→remediate) in EARLY INERTIA
ANCHOR CHECK only. R20 demonstrated that the same self-routing pattern can and should
apply to every blocking gate in the prompt: the four step EXIT GATEs (STEP 1–4 or
structural equivalent), SCOPE AUDIT, PERSPECTIVE AUDIT, INERTIA ANCHOR CHECK, and
CROSS-ROLE SPREAD CHECK. In V-02/V-04/V-05, every one of these gates emits a PASS
branch naming the continuation action and a FAIL branch naming the remediation action
and the re-check obligation. An executor can resolve any gate result to its next action
without reading surrounding prose — the prompt is executor-complete at every structural
boundary. C-44 requires this pattern at each of the following gates: (1) all STEP EXIT
GATEs (every phase boundary); (2) SCOPE AUDIT; (3) PERSPECTIVE AUDIT; (4) INERTIA
ANCHOR CHECK; (5) CROSS-ROLE SPREAD CHECK. C-43 remains the baseline for EARLY INERTIA
ANCHOR CHECK; C-44 is satisfied independently of C-43. A prompt in which fewer than all
five named gate types carry both routing branches earns C-44 PARTIAL proportional to
the fraction covered; a prompt in which none of the five carry routing branches (beyond
EARLY INERTIA ANCHOR CHECK) fails C-44.

**C-45 — BASELINE PROPAGATION MAP AS UPFRONT ASSIGNMENT CONTRACT** (from V-03, V-05 /
Axis-N):
C-41 requires CROSS-ROLE SPREAD CHECK to verify that at least one non-inertia role
references an INERTIA BASELINE term verbatim and to emit a PASS/FAIL [N of M] count.
R20 revealed a stronger pattern: constructing a BASELINE PROPAGATION MAP at the end of
STEP 1 / Phase 2 (immediately after G-terms are defined) that pre-commits each
non-inertia role to a named S/G term before any frame fill or role authoring begins. The
PROPAGATION MAP is a table of the form: Role | Assigned Term (S/G label + phrase). Once
declared, LENS AUDIT item 6 shifts from open-ended scan ("does any role reference a
baseline term?") to conformance verification ("does this role carry its assigned term
per the PROPAGATION MAP?"), and CROSS-ROLE SPREAD CHECK shifts from binary gate to
per-role accountability report — listing every satisfying role by name in the PASS
emission and every failing role by name in the FAIL emission. STEP 1 EXIT GATE (or
Phase 2 gate) includes BASELINE PROPAGATION MAP complete as a stated exit condition.
WRITE REMAINING ROLES instruction includes "include the PROPAGATION MAP assigned term
verbatim in lens.verify" as an explicit constraint. C-45 requires: (a) BASELINE
PROPAGATION MAP table present at Phase 2 / STEP 1 with a Role column and an Assigned
Term column; (b) LENS AUDIT item 6 references the MAP assignment by label+phrase (not
just "an INERTIA BASELINE term"); (c) CROSS-ROLE SPREAD CHECK emits per-role PASS/FAIL
against the MAP (not just aggregate N of M); (d) STEP 1 / Phase 2 EXIT GATE states MAP
completeness as an exit condition. Absence of the PROPAGATION MAP fails C-45. A MAP
present but not referenced in LENS AUDIT item 6 or CROSS-ROLE SPREAD CHECK earns C-45
PARTIAL.

**Formula updated**: `aspirational_pass / 37 * 10` (was `/35`). Each full pass = 0.270 pts.

---

## Criteria (full table)

### Essential (5)
| ID | Criterion |
|----|-----------|
| C-01 | All 5 required role fields present (`name`, `orientation`, `lens`, `simplify`, `collaborates_with`) |
| C-02 | Inertia-advocate role present with `orientation: status-quo advocate` |
| C-03 | Output path is `.craft/roles/{domain}/` |
| C-04 | Role content is domain-specific (no generic placeholders) |
| C-05 | Minimum 3 roles in the role-set |

### Recommended (3)
| ID | Criterion |
|----|-----------|
| C-06 | `lens.verify` items are actionable (each item is a testable check, not a description) |
| C-07 | `collaborates_with` references resolve to named roles in the same role-set |
| C-08 | Perspective diversity: roles represent distinct functional or stakeholder viewpoints |

### Aspirational (37)

#### Phase 1 — Input Inventory
| ID | Criterion |
|----|-----------|
| C-09 | INPUT INVENTORY table present with Row-ID, Source, and Excerpt columns; minimum 5 rows; explicit exit gate before Phase 2 |
| C-10 | Sole-citation rule stated: "This table is the sole citation source for INERTIA BASELINE — no field may cite the convergence summary" (or structural equivalent) |
| C-11 | Phase 1 exit gate states: "Do not proceed to Phase 2 until at least 5 rows are present" (or structural equivalent with explicit threshold) |

#### Phase 2 — Inertia Baseline Construction
| ID | Criterion |
|----|-----------|
| C-12 | INERTIA BASELINE S-terms labeled in `S{N}: "{exact phrase}"` format; minimum S1–S3 |
| C-13 | INERTIA BASELINE G-terms labeled in `G{N}: "{exact phrase}"` format; minimum G1–G3 |
| C-14 | Candidate roster table present with S/G label column; inertia-advocate assigned to defend named S-terms (e.g., "defends S1 (and S2, S3)") |
| C-40 | NON-GENERIC REQUIREMENT block present in Phase 2 (or the structural phase/step that constructs INERTIA BASELINE): operational definition of the form "a phrase is non-generic if and only if it contains at least one noun or verb specific to this domain…"; negative-example list (e.g., "easy to use," "works well," "is fast"); NON-GENERIC CHECK gate with explicit "NON-GENERIC CHECK: PASS" emission when all terms pass; Phase 2 EXIT GATE includes NON-GENERIC CHECK; Phase 7 INERTIA ANCHOR CHECK back-references this check by its actual name. Absence of NON-GENERIC REQUIREMENT block or failure of any term at NON-GENERIC CHECK is a blocking error. |

#### Phase 3 — Frame Fill
| ID | Criterion |
|----|-----------|
| C-15 | Frame fill: all five role fields drafted; each field includes `Phase 1 source: {row-id} = "{verbatim phrase}"` citation |
| C-39 | FRAME FILL PRE-ANCHOR CHECK fires after the inertia-advocate FRAME FILL block and before Phase 5 or Phase 6 begins (Phase 4 canonical position); verifies that the inertia-advocate's `lens.verify` draft contains at least one label-prefixed verbatim S-term from INERTIA BASELINE in "S{N}: {phrase}" format; emits explicit "FRAME FILL PRE-ANCHOR CHECK: PASS / FAIL" label; FAIL halts Phase 4 and requires FRAME FILL revision before continuing. Advancing past the inertia-advocate FRAME FILL without FRAME FILL PRE-ANCHOR CHECK PASS is a blocking error. |

#### Phase 4 — Planning Table
| ID | Criterion |
|----|-----------|
| C-16 | Planning table present with columns: Role, Scope, Perspective, Planned-Vocab-Term, Gap/Strength |
| C-17 | Scope audit present: "Fewer than 2 — expand or reassign, then re-count. Two or more — proceed" (or structural equivalent with explicit threshold and consequence) |
| C-18 | Perspective audit present: "Fewer than 3 — add roles or reassign. Three or more — proceed" (or structural equivalent) |

#### Phase 5 — Role Authoring
| ID | Criterion |
|----|-----------|
| C-19 | Inertia-advocate written first; step explicitly labeled (e.g., "Step 6.1 — Write the inertia-advocate first") |
| C-20 | Step 6.1 (or equivalent) emits "INERTIA-ADVOCATE WRITTEN: {path}" after writing the inertia-advocate role file |
| C-38 | EARLY INERTIA ANCHOR CHECK present in Phase 6.1 (or the step immediately after inertia-advocate role is written): explicit "EARLY INERTIA ANCHOR CHECK: PASS / FAIL" label emitted; FAIL blocks Step 6.2 (or equivalent remaining-roles step); PASS required before proceeding. |
| C-21 | LENS AUDIT block present for each non-inertia-advocate role with all 6 check items (see C-22–C-25 and C-41 for items 1–5 and 6) |
| C-22 | LENS AUDIT item 1: "Is verify[1] domain-specific? Yes / No + evidence" |
| C-23 | LENS AUDIT item 2: "Is verify[2] domain-specific? Yes / No + evidence" |
| C-24 | LENS AUDIT item 3: "Is simplify[1] a concrete cut rule? Yes / No + evidence" |
| C-25 | LENS AUDIT item 4: "Does Planned-Vocab-Term appear verbatim in this role? Yes / No + location" |
| C-41 | LENS AUDIT item 6 present for every non-inertia-advocate role: "references INERTIA BASELINE term (S or G label + phrase from Phase 2)? Yes / No + which term." Phase 7 CROSS-ROLE SPREAD CHECK requires at least one non-inertia-advocate role to reference an INERTIA BASELINE term (label + phrase) verbatim; emits "CROSS-ROLE SPREAD CHECK: PASS or FAIL [N of M non-inertia roles reference a baseline term]." ROLE-REPLACE re-evaluation includes CROSS-ROLE SPREAD CHECK. A role-set in which only the inertia-advocate references INERTIA BASELINE terms fails CROSS-ROLE SPREAD CHECK. |

#### Phase 6 — Phase 7 Verification Checks
| ID | Criterion |
|----|-----------|
| C-26 | Check 1: All required fields present in every written role file; "Emit per file: PASS or FAIL [missing field]" |
| C-27 | Check 2: Inertia-advocate orientation = "status-quo advocate"; emit PASS or FAIL |
| C-28 | Check 3A: Scope spread across all roles ≥ 2; emit PASS or FAIL |
| C-29 | Check 3B: ROLE-REPLACE sub-procedure defined and fires when scope spread < 2 |
| C-30 | Check 4A: All roles from the planning table are written; emit PASS or FAIL per missing role |
| C-31 | Check 4B: Each Planned-Vocab-Term appears verbatim in its assigned role; ROLE-REPLACE fires on mismatch |
| C-32 | Check 5A: Written role fields match the frame fill for each role; emit PASS or FAIL per discrepancy |
| C-33 | Check 5B: All citations in written roles are verifiable against the INPUT INVENTORY table; emit per violation |
| C-34 | Check 6: No generic placeholders remain in any written role field; emit PASS or FAIL |
| C-35 | Check 7: All role files are at the correct output path `.craft/roles/{domain}/`; emit PASS or FAIL |
| C-36 | Check 8: Perspective spread across all roles ≥ 3; emit PASS or FAIL |
| C-37 | INERTIA ANCHOR CHECK: re-reads the inertia-advocate role file and verifies at least one label-prefixed verbatim S-term from INERTIA BASELINE is present in `lens.verify`; emits explicit "INERTIA ANCHOR CHECK: PASS or FAIL"; FAIL is a blocking error at Phase 7 |

#### New in v14
| ID | Criterion |
|----|-----------|
| C-42 | CANONICAL-PHASE POSITIONAL EQUIVALENCE UNDER COMPRESSION: A skill using lifecycle compression (phases merged or renumbered) earns C-39 and C-40 PASS for phase placement if it satisfies at least one of: (a) an explicit canonical-phase mapping table is declared in a structure header mapping compressed steps to canonical phases; or (b) positional relationship is unambiguously inferrable from step ordering — FRAME FILL PRE-ANCHOR CHECK fires immediately after the inertia-advocate FRAME FILL block and before the remaining-roles loop, AND NON-GENERIC REQUIREMENT block appears in the same step that constructs INERTIA BASELINE S-terms and G-terms. In either case, the Phase 7 INERTIA ANCHOR CHECK back-reference must cite the actual step/phase name used at the NON-GENERIC CHECK gate (not the canonical literal "Phase 2 NON-GENERIC CHECK"). A compressed skill satisfying neither condition fails C-39 and C-40 for phase placement regardless of content quality. |
| C-43 | EARLY ANCHOR CHECK SELF-ROUTING BRANCHES: EARLY INERTIA ANCHOR CHECK (C-38 gate) includes explicit dual-branch routing in the gate text — PASS branch names the continuation action ("proceed to remaining roles" or structural equivalent) and FAIL branch names the remediation action and re-check obligation ("revise inertia-advocate role and re-check before proceeding" or structural equivalent). Both branches must appear in the gate text; the gate is self-routing without consulting surrounding prose. A gate that emits PASS/FAIL label only (satisfying C-38) but omits both routing branches fails C-43. A gate with one branch but not both earns C-43 PARTIAL. |

#### New in v15
| ID | Criterion |
|----|-----------|
| C-44 | SYSTEM-WIDE EXIT GATE SELF-ROUTING: Every blocking gate in the prompt emits explicit dual-branch routing — a PASS branch naming the continuation action and a FAIL branch naming the remediation action and re-check obligation — so an executor can resolve any gate result to its next action without consulting surrounding prose. The five gate types that must each carry both branches are: (1) all STEP EXIT GATEs (every phase-boundary gate, STEP 1–N); (2) SCOPE AUDIT; (3) PERSPECTIVE AUDIT; (4) INERTIA ANCHOR CHECK; (5) CROSS-ROLE SPREAD CHECK. C-43 is the baseline for EARLY INERTIA ANCHOR CHECK; C-44 is evaluated independently across the remaining five gate types. A prompt in which all five named gate types carry both PASS and FAIL routing branches earns C-44 PASS. A prompt in which at least one but fewer than all five carry both branches earns C-44 PARTIAL. A prompt in which none of the five carry routing branches (only EARLY INERTIA ANCHOR CHECK qualifies via C-43) fails C-44. |
| C-45 | BASELINE PROPAGATION MAP AS UPFRONT ASSIGNMENT CONTRACT: A BASELINE PROPAGATION MAP table (columns: Role, Assigned Term [S/G label + phrase]) is constructed at the end of Phase 2 / STEP 1, immediately after G-terms are defined, pre-committing each non-inertia role to a specific INERTIA BASELINE term before any frame fill or role authoring begins. Four structural requirements must all be present: (a) BASELINE PROPAGATION MAP table present at Phase 2 / STEP 1 with a Role column and an Assigned Term column covering every non-inertia role; (b) LENS AUDIT item 6 references the MAP assignment by label+phrase in the form "references INERTIA BASELINE term per PROPAGATION MAP assignment ({label}: {phrase}): YES/NO + which term" — not just "references an INERTIA BASELINE term"; (c) CROSS-ROLE SPREAD CHECK emits per-role conformance results against the MAP (listing each satisfying role by name in the PASS emission and each failing role by name in the FAIL emission), rather than an aggregate N-of-M count only; (d) STEP 1 / Phase 2 EXIT GATE states BASELINE PROPAGATION MAP completeness (every non-inertia role assigned) as an explicit exit condition. Absence of the PROPAGATION MAP fails C-45. A MAP present but not referenced in LENS AUDIT item 6 or CROSS-ROLE SPREAD CHECK earns C-45 PARTIAL. |

---

## Scoring Key

| Rating | Weight |
|--------|--------|
| PASS   | 1.0    |
| PARTIAL | 0.5   |
| FAIL   | 0.0    |

**Formula**: `aspirational_pass / 37 * 10`
(Aspirational = C-09 through C-45, 37 criteria, 0.270 pts per full pass)

Essential (C-01–C-05) and Recommended (C-06–C-08) are pass/fail gates; they do not
contribute to the numeric score but gate scoring eligibility.

---

## Criterion Definitions for Close-Call Scoring (C-38–C-45)

| Criterion | PASS | PARTIAL | FAIL |
|-----------|------|---------|------|
| C-38 | Explicit "EARLY INERTIA ANCHOR CHECK: PASS/FAIL" label emitted + blocking statement present | Mechanism present and blocking, no explicit label | Absent |
| C-39 | Phase 4 canonical position (or positional equivalence per C-42) + explicit "FRAME FILL PRE-ANCHOR CHECK: PASS/FAIL" label | Mechanism present; one dimension off (wrong phase OR label missing, but not both) | Mechanism present but both phase wrong AND label missing; or position far off |
| C-40 | All four elements correct phase/position (or positional equivalence per C-42): NON-GENERIC REQUIREMENT block label + operational definition + negative-example list + NON-GENERIC CHECK PASS emission + EXIT GATE inclusion + Phase 7 back-ref citing actual step name | Content present (def + examples + back-ref) but missing block label or emission label, or phase wrong without C-42 resolution | Absent |
| C-41 | 6th LENS AUDIT item present per non-inertia role + CROSS-ROLE SPREAD CHECK in Phase 7 with PASS/FAIL emission | One of the two items present | Neither present |
| C-42 | Compressed skill: mapping table declared OR positional inference unambiguous; Phase 7 back-ref uses actual step name | Partial mapping declared (covers C-39 position but not C-40 or vice versa) | Compressed skill with no mapping and ambiguous ordering |
| C-43 | Both routing branches present in gate text (PASS: continue; FAIL: revise + re-check) | One branch present, one absent | Neither branch present (label only, no routing) |
| C-44 | All 5 named gate types carry explicit PASS→continuation and FAIL→remediation+re-check branches | At least 1 but fewer than 5 gate types carry both branches | None of the 5 named gate types carry routing branches |
| C-45 | PROPAGATION MAP table present at Phase 2; LENS AUDIT item 6 uses MAP conformance formulation; CROSS-ROLE SPREAD CHECK emits per-role results; Phase 2 EXIT GATE states MAP completeness | MAP present but missing 1–2 of the three downstream requirements (LENS AUDIT ref, per-role CHECK, EXIT GATE condition) | MAP absent |

---

## Risk Register

| Risk | Closed by |
|------|-----------|
| Risk-1: Phase 2 generic phrase ambiguity | C-40 |
| Risk-2: Inertia baseline not propagated into lens.verify | C-37 |
| Risk-3: Intra-Phase-6 cascade revision after full role commit | C-39 |
| Risk-4: Definitional ambiguity — "easy to use" passes as domain-specific | C-40 |
| Risk-5: Baseline silo — terms confined to inertia-advocate role only | C-41 |
| Risk-6: Phase-number mismatch under lifecycle compression invalidates correct mechanisms | C-42 |
| Risk-7: Ambiguous gate consequence — executor must infer next action from prose | C-43 |
| Risk-8: Executor-incomplete prompt — gate routing ambiguity beyond EARLY INERTIA ANCHOR CHECK | C-44 |
| Risk-9: Post-hoc cascade revision from baseline term omission — all roles written before any carry a baseline term | C-45 |

---

## Version History

| Version | Change |
|---------|--------|
| v15 | +C-44 (system-wide exit gate self-routing), +C-45 (baseline propagation map as upfront assignment contract); formula → `/37 * 10` |
| v14 | +C-42 (canonical-phase positional equivalence under compression), +C-43 (early anchor check self-routing branches); formula → `/35 * 10` |
| v13 | +C-39 (FRAME FILL PRE-ANCHOR CHECK in Phase 4), +C-40 (NON-GENERIC REQUIREMENT block in Phase 2), +C-41 (6th LENS AUDIT item + CROSS-ROLE SPREAD CHECK); formula → `/33 * 10` |
| v12 | +C-38 (EARLY INERTIA ANCHOR CHECK in Phase 6.1); formula → `/30 * 10` |
| v11 | INERTIA BASELINE mechanism introduced (C-36, C-37) |
```
