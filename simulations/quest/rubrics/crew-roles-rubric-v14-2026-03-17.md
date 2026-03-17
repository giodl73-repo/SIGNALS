Good — that confirms the scorecard format. Now extracting the two new excellence patterns from R19 before writing.

**R19 excellence signals, extracted:**

**From V-02 (Axis-J) C-39 PARTIAL** — phase-number mismatch: the FRAME FILL PRE-ANCHOR CHECK had correct structure and explicit label but STEP 2 ≠ Phase 4. The rubric currently treats any phase-number deviation as a PARTIAL penalty even when structural position is demonstrably correct. No mechanism exists for a compressed skill to declare positional equivalence and earn PASS.

**From V-02 (Axis-J) C-40 PARTIAL** — same structural issue: NON-GENERIC REQUIREMENT block was fully formed (def + negative list + NON-GENERIC CHECK emission + EXIT GATE + back-ref using actual step name "STEP 1 NON-GENERIC CHECK") but STEP 1 ≠ Phase 2. Also reveals back-reference portability: citing the actual step name ("as validated at STEP 1 NON-GENERIC CHECK") is correct behavior under compression — the rubric must accept it.

**From V-02 (Axis-J) C-38 PASS** — the achieving variation added: (a) explicit PASS-branch routing ("proceed to remaining roles") and (b) explicit FAIL-branch routing ("revise file and re-check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS"). This self-routing pattern is not required by C-38 and should become C-43.

→ **C-42**: Canonical-phase positional equivalence under compression (closes V-02 C-39/C-40 phase-number gap)
→ **C-43**: Early anchor check self-routing branches (elevates V-02 C-38 PASS pattern)

Formula: 33 → 35 aspirational. `/35 * 10` = 0.286 pts each.

---

```markdown
# crew-roles rubric — v14

## Changes from v13

Two new aspirational criteria extracted from R19 variations V-01 (Axis-I: Phrasing
Register) and V-02 (Axis-J: Lifecycle Compression). Each closes a residual gap exposed
by the compressed-structure axis test.

**C-42 — CANONICAL-PHASE POSITIONAL EQUIVALENCE UNDER COMPRESSION** (from V-02 / Axis-J):
C-39 and C-40 reference canonical phase numbers ("Phase 4," "Phase 2") that become
mismatched when lifecycle compression merges or renumbers phases. V-02 demonstrated
that all structural elements of both checks can be present and correctly formed while
failing on phase-number matching alone — a mechanical penalty that does not reflect
correctness. Axis-J closes this by requiring that skills using lifecycle compression
satisfy one of two positional-equivalence conditions for C-39 and C-40: (a) an explicit
canonical-phase mapping table is declared in a structure header (e.g., "STEP 1 = canonical
Phase 1+2, STEP 2 = canonical Phase 3+4"), enabling phase-dependent criteria to be
evaluated by declared positional equivalents; or (b) the positional relationship is
unambiguously inferrable from step ordering — FRAME FILL PRE-ANCHOR CHECK fires
immediately after the inertia-advocate FRAME FILL block and before any remaining-roles
loop begins (C-39 position), and NON-GENERIC REQUIREMENT block appears within the same
step that constructs INERTIA BASELINE S-terms and G-terms (C-40 position). In both
cases, the Phase 7 back-reference must cite the actual step/phase name used at the
NON-GENERIC CHECK gate (e.g., "as validated at STEP 1 NON-GENERIC CHECK"), not the
canonical literal "Phase 2 NON-GENERIC CHECK." A compressed skill that meets one of
the two positional-equivalence conditions earns C-39 and C-40 PASS for phase placement;
a compressed skill that meets neither fails both for phase placement regardless of
content quality.

**C-43 — EARLY ANCHOR CHECK SELF-ROUTING BRANCHES** (from V-02 / Axis-J C-38 PASS):
C-38 requires EARLY INERTIA ANCHOR CHECK to emit an explicit PASS/FAIL label and block
Step 6.2. V-02 revealed an excellence pattern beyond C-38's current requirement: the
achieving variation emitted explicit dual-branch routing — PASS branch: "proceed to
remaining roles"; FAIL branch: "revise file and re-check before proceeding. Remaining
roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." This self-routing pattern
makes the gate fully self-contained: the executor reads the gate result and knows the
next action without consulting surrounding prose. C-43 requires that EARLY INERTIA
ANCHOR CHECK includes both routing branches in the gate text: PASS branch names the
continuation action ("proceed to remaining roles" or structural equivalent) and FAIL
branch names the remediation action and re-check obligation ("revise inertia-advocate
role and re-check before proceeding" or structural equivalent). A gate that emits the
PASS/FAIL label (satisfying C-38) but omits routing branches fails C-43. A gate that
includes one branch but not both earns C-43 PARTIAL.

**Formula updated**: `aspirational_pass / 35 * 10` (was `/33`). Each full pass = 0.286 pts.

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

### Aspirational (35)

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

---

## Scoring Key

| Rating | Weight |
|--------|--------|
| PASS   | 1.0    |
| PARTIAL | 0.5   |
| FAIL   | 0.0    |

**Formula**: `aspirational_pass / 35 * 10`
(Aspirational = C-09 through C-43, 35 criteria, 0.286 pts per full pass)

Essential (C-01–C-05) and Recommended (C-06–C-08) are pass/fail gates; they do not
contribute to the numeric score but gate scoring eligibility.

---

## Criterion Definitions for Close-Call Scoring (C-38–C-43)

| Criterion | PASS | PARTIAL | FAIL |
|-----------|------|---------|------|
| C-38 | Explicit "EARLY INERTIA ANCHOR CHECK: PASS/FAIL" label emitted + blocking statement present | Mechanism present and blocking, no explicit label | Absent |
| C-39 | Phase 4 canonical position (or positional equivalence per C-42) + explicit "FRAME FILL PRE-ANCHOR CHECK: PASS/FAIL" label | Mechanism present; one dimension off (wrong phase OR label missing, but not both) | Mechanism present but both phase wrong AND label missing; or position far off |
| C-40 | All four elements correct phase/position (or positional equivalence per C-42): NON-GENERIC REQUIREMENT block label + operational definition + negative-example list + NON-GENERIC CHECK PASS emission + EXIT GATE inclusion + Phase 7 back-ref citing actual step name | Content present (def + examples + back-ref) but missing block label or emission label, or phase wrong without C-42 resolution | Absent |
| C-41 | 6th LENS AUDIT item present per non-inertia role + CROSS-ROLE SPREAD CHECK in Phase 7 with PASS/FAIL emission | One of the two items present | Neither present |
| C-42 | Compressed skill: mapping table declared OR positional inference unambiguous; Phase 7 back-ref uses actual step name | Partial mapping declared (covers C-39 position but not C-40 or vice versa) | Compressed skill with no mapping and ambiguous ordering |
| C-43 | Both routing branches present in gate text (PASS: continue; FAIL: revise + re-check) | One branch present, one absent | Neither branch present (label only, no routing) |

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

---

## Version History

| Version | Change |
|---------|--------|
| v14 | +C-42 (canonical-phase positional equivalence under compression), +C-43 (early anchor check self-routing branches); formula → `/35 * 10` |
| v13 | +C-39 (FRAME FILL PRE-ANCHOR CHECK in Phase 4), +C-40 (NON-GENERIC REQUIREMENT block in Phase 2), +C-41 (6th LENS AUDIT item + CROSS-ROLE SPREAD CHECK); formula → `/33 * 10` |
| v12 | +C-38 (EARLY INERTIA ANCHOR CHECK in Phase 6.1); formula → `/30 * 10` |
| v11 | INERTIA BASELINE mechanism introduced (C-36, C-37) |
```

---

**Summary of additions:**

- **C-42** closes the phase-number portability gap exposed by V-02: a compressed skill earning PARTIAL on C-39/C-40 solely due to step renumbering now has a defined path to PASS via mapping declaration or unambiguous positional inference. The back-reference portability rule (cite actual step name, not canonical "Phase 2") is codified here rather than added to C-40, keeping C-40 focused on content requirements.

- **C-43** elevates the V-02 C-38 PASS pattern into a requirement: dual-branch self-routing (PASS → continue; FAIL → revise + re-check) makes gates executor-complete without prose consultation. The criterion is deliberately separate from C-38 so C-38 remains the baseline label requirement and C-43 layers the routing requirement on top — a skill can hold C-38 PASS while failing C-43.

- Formula moves to `/35 * 10` (0.286 pts each). A perfect score on the 29-criterion baseline plus C-38–C-43 all at PASS = 10.0.
