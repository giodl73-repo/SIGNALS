Reading the scorecard variations carefully before writing the new criteria.

**Extraction pass:**

V-01 through V-03 each demonstrate full PASS on an *existing* criterion (C-11, C-15, C-36 respectively) by closing R11 gaps — not new structure. V-04 and V-05 introduce the genuinely new patterns:

- **V-04**: INVARIANTS entries carry `cop: [COP-07, COP-09]` pointers; COP-NN items carry `invariant: INVARIANT-SPECIALIZATION-DISTINCTNESS` annotations — bidirectional cross-layer traceability. Not covered by any existing criterion.
- **V-05**: CO-EXTENSIVE DECLARATION explicitly enumerates all three layers (CATALOG + INVARIANTS + COP-NN) as independently attesting the same properties. C-33 covers the two-layer contract; the three-layer extension is new.

That yields **C-37** and **C-38**. Two new criteria, not three — the round count varies.

---

```markdown
# corps-build Rubric — v11
**Updated**: 2026-03-17
**Based on**: Round 12 scorecard (V-01 through V-05)
**Changes from v10**: Added C-37, C-38 from R12 excellence signals; max updated 230 → 240; thresholds scaled.

---

## What Changed

| Version | Change | Source |
|---------|--------|--------|
| v1 → v2 | Added C-11 (named invariants block), C-12 (auditable check-output), C-13 (named failure modes per criterion) | R3 excellence signals |
| v2 → v3 | Added C-14 (dedicated pre-step FAILURE MODES block), C-15 (named CHECK-OUTPUT PROTOCOL section) | R4 excellence signals |
| v3 → v4 | Added C-16 (phase-exit guard tokens), C-17 (per-artifact TRANSCRIPTION-RECEIPT), C-18 (BUILD-VERIFY single-purpose phase) | R5 excellence signals |
| v4 → v5 | Added C-19 (TRANSCRIPTION-RECEIPT in-phase remediation), C-20 (BUILD-VERIFY exclusion manifest), C-21 (TRANSCRIPTION-CLEAR all-artifact re-audit) | R6 excellence signals |
| v5 → v6 | Added C-22 (IA failure mode contrast pair), C-23 (typed STRUCTURAL-ERROR code taxonomy), C-24 (premature-exit violation named as STRUCTURAL-ERROR) | R7 excellence signals |
| v6 → v7 | Added C-25 (ENTRY-GATE bidirectional phase enforcement), C-26 (pre-execution STRUCTURAL-ERROR-CATALOG), C-27 (PROFILE-phase typed violation taxonomy) | R8 excellence signals |
| v7 → v8 | Added C-28 (ROLES-WRITTEN per-team field-completeness receipt), C-29 (AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate), C-30 (CATALOG-CLOSURE terminal attestation) | R9 excellence signals |
| v8 → v9 | Added C-31 (ROLES-WRITTEN NO-halt remediation cycle), C-32 (AMEND-CHAIN-COMPLETE terminal token), C-33 (STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract) | R10 excellence signals |
| v9 → v10 | Added C-34 (SPECIALIZATION-GATE per-team comparison block), C-35 (ROLES-COMPLETE specialization-gates attestation), C-36 (AMEND --area SPECIALIZATION-GATE re-run) | R11 excellence signals |
| v10 → v11 | Added C-37 (INVARIANTS-to-COP bidirectional pointer), C-38 (three-layer CO-EXTENSIVE DECLARATION) | R12 excellence signals |

**R11 pattern summary**: R11 revealed three structural innovations centered on specialization-gate auditing. C-34 (SPECIALIZATION-GATE per-team comparison block) introduces a named per-team gate in the WRITE-ROLES phase requiring a per-role comparison table distinguishing standard from specialized content across every role dimension, with an explicit gate-verdict (SPECIALIZATION-GATE: PASS|FAIL) that must resolve before advancing to the next team; this converts the specialization distinction from a write-time style constraint (C-07) into an auditable per-team comparison gate with a named verdict, making copy-from-standard violations detectable at build time rather than review time; V-03 demonstrated this with a named SPECIALIZATION-GATE block per team in Phase 7, and ROLES-COMPLETE including `all-specialization-gates-passed: YES`. C-35 (ROLES-COMPLETE specialization-gates attestation) extends the ROLES-COMPLETE terminal token to include an `all-specialization-gates-passed: YES|NO` field; NO is a recoverable in-phase state that triggers a named halt and per-team re-audit before ROLES-COMPLETE closes, mirroring the ROLES-WRITTEN NO-halt remediation cycle (C-31) at the specialization audit layer; this makes the specialization gate a closing condition of the entire WRITE-ROLES phase rather than a per-team check that could be silently skipped or left unresolved; V-03 demonstrated this with `all-specialization-gates-passed: YES` as a required field in ROLES-COMPLETE. C-36 (AMEND --area SPECIALIZATION-GATE re-run) requires that the AMEND --area repair chain explicitly re-run the SPECIALIZATION-GATE per team during Phase 7 re-execution rather than inheriting prior gate verdicts; this closes a gap where AMEND --area could regenerate roles that pass PROFILE-REDERIVE and IA-WRITTEN checks but silently regress specialization distinctness because the comparison gate was not re-evaluated; V-03 demonstrated this with AMEND --area explicitly naming the SPECIALIZATION-GATE per team in the Phase 7 re-run description, making specialization re-audit a named member of the AMEND chain alongside PROFILE-REDERIVE and ROLES-WRITTEN.

**R12 pattern summary**: R12 revealed two structural innovations centered on cross-layer traceability and co-extensive contract depth. V-01 through V-03 demonstrated full PASS on existing C-11, C-15, and C-36 respectively by closing R11 gaps — adding `INVARIANT-SPECIALIZATION-DISTINCTNESS` to the INVARIANTS block (V-01), adding specialization-aware COP-07 and COP-09 items to the COP-NN section (V-02), and adding the `specialization-gate-rerun: { per-team: [...] }` field to AMEND-CHAIN-COMPLETE (V-03); these three variations validated that each enforcement layer can independently reach PASS on specialization coverage without introducing new structural requirements. V-04 and V-05 then demonstrated the structural innovations that become C-37 and C-38.

C-37 (INVARIANTS-to-COP bidirectional pointer) introduces cross-layer traceability between the INVARIANTS block and COP-NN protocol items: each INVARIANTS entry carries a `cop:` pointer field naming the COP-NN items that enforce it, and each COP-NN item carries an `invariant:` annotation naming its source invariant; this bidirectional mapping makes the protocol and invariant layers mutually verifiable at inspection time without requiring the reader to manually resolve which protocol steps enforce which invariants; prior to V-04, INVARIANTS entries and COP-NN items were independently specified and only coincidentally consistent — a reviewer could not verify consistency between the two layers without reading both sections in full and performing the mapping manually; V-04 demonstrated this with `INVARIANT-SPECIALIZATION-DISTINCTNESS` carrying `cop: [COP-07, COP-09]` and COP-07/COP-09 each annotated with `invariant: INVARIANT-SPECIALIZATION-DISTINCTNESS`; V-05 carried this forward as part of the full three-layer synthesis. An INVARIANTS block that lacks `cop:` pointer fields, or a COP-NN section whose items lack `invariant:` annotations, is PARTIAL even if both layers are individually complete.

C-38 (three-layer CO-EXTENSIVE DECLARATION) extends the CO-EXTENSIVE DECLARATION from the two-layer contract established by C-33 (STRUCTURAL-ERROR-CATALOG + INVARIANTS block) to a three-layer contract that explicitly enumerates STRUCTURAL-ERROR-CATALOG (catalog layer), INVARIANTS block (invariant layer), and COP-NN (protocol layer) as all three independently attesting the same structural properties; the declaration must name all three layers and assert that adding any new structural property requires entries in all three; a CO-EXTENSIVE DECLARATION that names only CATALOG and INVARIANTS while omitting COP-NN achieves C-33 PASS but fails C-38; V-05 demonstrated this with CO-EXTENSIVE DECLARATION explicitly extending to COP-NN as a third verification mechanism alongside INVARIANTS and CATALOG, and with all three layers independently verifying the same specialization distinctness property through their respective typed entries (CATALOG: SPECIALIZATION-COPY-VIOLATION error code; INVARIANTS: INVARIANT-SPECIALIZATION-DISTINCTNESS with `cop:` pointer; COP-NN: COP-07 = specialization-gate verdict + COP-09 = terminal attestation field, both annotated with invariant name). A declaration naming all three layers without asserting the "all three required for any new property" rule is PARTIAL.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 30 | 5 | 150 |
| **Max** | | | **240** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 201
**PARTIAL pass**: composite >= 150 with all 5 essential passing — earn full pass with 2/3 recommended

---

## Criteria

### Essential (12 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-01 | **Role file completeness** — total file count in summary equals count of files written in Step 2; gap identified and resolved before proceeding | correctness | PASS requires verification mechanism, not just count statement |
| C-02 | **org-chart.md with ASCII hierarchy** — uses `+--` / `\|` notation; all org.yaml names verbatim; nesting reflects group → team depth | format | Concrete example or INVARIANT declaration required for PASS |
| C-03 | **Inertia Advocate in every team** — one IA per team, no exceptions; enforced as a closure gate before moving to next team | correctness | "Mandatory" imperative + enforcement hook required |
| C-04 | **org.yaml structural fidelity** — files written only to subdirectories derived from org.yaml; path pattern `.craft/roles/{area-slug}/{role-slug}.md` | correctness | Pre-write path validation required for PASS |
| C-05 | **Role file typed fields present** — all five fields (`title`, `role-type`, `area`, `lens`, `expertise`) present with substantive bodies | coverage | Example files or field descriptions with quality bar required |

---

### Recommended (10 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-06 | **Headcount by group table + levels** — table includes group, standard count, specialized count, IA count, total, and Levels column | depth | Column structure must be explicit; IA count column required for PASS |
| C-07 | **Standard vs specialized distinction** — `role-type` in frontmatter; write sequence orders standard → specialized → IA | correctness | Sequence must be stated; specialized distinctness must be enforced (not copyable from standard) |
| C-08 | **AMEND section with three options** — close with named repair options: specific area regeneration, level-term update, group-node addition | behavior | Area regeneration option should reference invariant re-checks |

---

### Aspirational (5 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-09 | **Inertia Advocate team-contextualized** — IA lens and expertise drawn from this team's declared domain vocabulary; generic resistance language fails | depth | Named failure mode earns full PASS (see C-13) |
| C-10 | **Build plan declared before execution** — before any write phase, skill declares the intended artifact list, phase sequence, and termination conditions; no implicit phases; reader can predict all outputs before execution begins | structure | Partial enumeration (missing artifact types or phases) is PARTIAL |
| C-11 | **Named INVARIANTS block** — dedicated INVARIANTS section names each structural property as a numbered invariant with paired enforcement code (`STRUCTURAL-ERROR:XXX`); invariants referenced by name from phase bodies where they apply; includes `INVARIANT-SPECIALIZATION-DISTINCTNESS` entry | enforcement | CO-EXTENSIVE DECLARATION required for PASS; INVARIANTS block without specialization entry is PARTIAL |
| C-12 | **Auditable check-output** — CHECK-OUTPUT section structured with named items after each major phase; correctness verifiable by reviewer without re-running phase | auditability | Prose summary without named items is PARTIAL |
| C-13 | **Named failure modes per criterion** — each key criterion has at least one named failure mode describing what a failing response looks like; named failure modes enable detection, not just prevention | depth | Generic "may fail" language without named mode is PARTIAL |
| C-14 | **Dedicated pre-step FAILURE MODES block** — pre-step FAILURE MODES block exists before any complex phase; block names at least two distinct failure modes with type codes before phase execution begins | enforcement | Inline failure notes without dedicated block is PARTIAL |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section (COP-NN)** — dedicated COP-NN numbered items section exists as post-phase protocol; each check step numbered and named; specialization-aware items present: COP-07 = SPECIALIZATION-GATE gate-verdict per team, COP-09 = ROLES-COMPLETE `all-specialization-gates-passed` field check | auditability | COP-NN section without specialization items (COP-07/COP-09) is PARTIAL |
| C-16 | **Phase-exit guard tokens** — named token required to advance from each phase; token absent = phase not exited; forward reference in next phase confirms token from prior phase | enforcement | Implied completion without named token is PARTIAL |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — each written artifact generates a named TRANSCRIPTION-RECEIPT listing fields written, field count, and path written to; receipt confirms transcription was faithful | auditability | Count statement without named RECEIPT structure is PARTIAL |
| C-18 | **BUILD-VERIFY single-purpose phase** — BUILD-VERIFY phase exists as its own named phase separate from write phases; single purpose (verify, not extend); no write operations within BUILD-VERIFY | structure | BUILD-VERIFY merged with write phase is PARTIAL |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — when TRANSCRIPTION-RECEIPT flags a discrepancy, a named remediation step exists within the phase; remediation re-writes the artifact and generates a new receipt; phase does not advance until all receipts clear | enforcement | Remediation deferred to next phase is PARTIAL |
| C-20 | **BUILD-VERIFY exclusion manifest** — BUILD-VERIFY includes explicit named list of files excluded from verification with stated reason; prevents silent under-counting | auditability | Unexplained exclusion or missing exclusion list is PARTIAL |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — at BUILD-VERIFY, each artifact receipt re-checked against written file; TRANSCRIPTION-CLEAR token issued only after all receipts confirm; missing or mismatched receipts halt BUILD-VERIFY | enforcement | TRANSCRIPTION-CLEAR without per-artifact check is PARTIAL |
| C-22 | **IA failure mode contrast pair** — named contrast pair distinguishes valid IA (team-domain language, unique lens) from invalid IA (generic resistance language, copied from standard template); both positive and negative exemplars named | depth | Single exemplar without contrast is PARTIAL |
| C-23 | **Typed STRUCTURAL-ERROR code taxonomy** — STRUCTURAL-ERROR codes use a typed taxonomy with at least three distinct types distinguishing structural class (e.g., MISSING-ARTIFACT vs PREMATURE-EXIT vs COPY-VIOLATION); all CATALOG codes draw from named types | structure | Untyped error codes or fewer than three types is PARTIAL |
| C-24 | **Premature-exit violation named as STRUCTURAL-ERROR** — premature phase exit (advancing without required token) named as a specific STRUCTURAL-ERROR code in CATALOG; code identifies it as a distinct violation class; referenced from ENTRY-GATE enforcement | enforcement | Generic error without named code is PARTIAL |
| C-25 | **ENTRY-GATE bidirectional phase enforcement** — each phase entry gate checks both (a) prior phase exit token present AND (b) current phase not previously completed; bidirectional check prevents both phase skipping and re-entry without explicit AMEND | enforcement | Unidirectional gate (prior token check only) is PARTIAL |
| C-26 | **Pre-execution STRUCTURAL-ERROR-CATALOG** — STRUCTURAL-ERROR-CATALOG declared before any phase executes; catalog lists all known error codes with types and descriptions; phase execution references CATALOG by name for error reporting | structure | CATALOG declared mid-execution or post-hoc is PARTIAL |
| C-27 | **PROFILE-phase typed violation taxonomy** — PROFILE phase includes typed violation taxonomy specific to profile derivation failures (e.g., MISSING-FIELD, INVALID-AREA-SLUG, DOMAIN-MISMATCH); violations reported against named taxonomy codes | depth | Prose error reporting without typed taxonomy is PARTIAL |
| C-28 | **ROLES-WRITTEN per-team field-completeness receipt** — ROLES-WRITTEN token per team includes field-completeness receipt listing each role, each field, and PRESENT\|MISSING status; receipt is a named data structure, not a prose summary | auditability | Prose summary without named per-field receipt is PARTIAL |
| C-29 | **AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate** — `AMEND --area` triggers full chain re-derivation for the named area: PROFILE-REDERIVE gate resolves before ROLES-WRITTEN begins; TRANSCRIPTION-RECEIPTS re-issued; chain completes before AMEND-CHAIN-COMPLETE | enforcement | AMEND that skips PROFILE-REDERIVE is PARTIAL |
| C-30 | **CATALOG-CLOSURE terminal attestation** — CATALOG-CLOSURE token attests at build close that all STRUCTURAL-ERROR codes referenced during the build are accounted for in CATALOG; unresolved codes halt CATALOG-CLOSURE | enforcement | CATALOG-CLOSURE without per-code reconciliation is PARTIAL |
| C-31 | **ROLES-WRITTEN NO-halt remediation cycle** — when ROLES-WRITTEN token cannot resolve (field-completeness receipt shows MISSING), named NO-halt remediation cycle triggers: identify missing fields, re-write affected roles, re-issue receipts; cycle continues until all receipts clear | enforcement | Missing-field halt without named remediation cycle is PARTIAL |
| C-32 | **AMEND-CHAIN-COMPLETE terminal token** — AMEND-CHAIN-COMPLETE token closes the AMEND repair chain as a named data structure with required fields (`area-amended:`, `profile-rederived:`, `roles-rewritten:`, `specialization-gate-rerun:`); token absent or any required field missing fails | enforcement | Prose AMEND summary without named token structure is PARTIAL |
| C-33 | **STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract** — STRUCTURAL-ERROR-CATALOG is the enforcement layer of the INVARIANTS contract; each invariant entry has a `catalog:` pointer to its corresponding CATALOG error code; CO-EXTENSIVE DECLARATION asserts CATALOG and INVARIANTS block co-extensively cover the same structural properties | enforcement | CATALOG and INVARIANTS present but without co-extensive linkage is PARTIAL |
| C-34 | **SPECIALIZATION-GATE per-team comparison block** — WRITE-ROLES phase includes per-team SPECIALIZATION-GATE block with per-role comparison table distinguishing standard from specialized content across every role dimension; gate-verdict (SPECIALIZATION-GATE: PASS\|FAIL) issued per team; FAIL halts advance to next team | enforcement | Specialization check without named gate-verdict per team is PARTIAL |
| C-35 | **ROLES-COMPLETE specialization-gates attestation** — ROLES-COMPLETE terminal token includes `all-specialization-gates-passed: YES\|NO` field; NO triggers named halt and per-team re-audit before ROLES-COMPLETE closes; token does not resolve until field reads YES | enforcement | ROLES-COMPLETE without specialization attestation field is PARTIAL |
| C-36 | **AMEND --area SPECIALIZATION-GATE re-run** — AMEND --area repair chain explicitly re-runs SPECIALIZATION-GATE per team during Phase 7 re-execution; prior gate verdicts discarded, not inherited; AMEND-CHAIN-COMPLETE token includes required `specialization-gate-rerun: { per-team: [...] }` field enumerating per-team re-run results | enforcement | AMEND that names SPECIALIZATION-GATE parenthetically without `specialization-gate-rerun:` field in AMEND-CHAIN-COMPLETE is PARTIAL |
| C-37 | **INVARIANTS-to-COP bidirectional pointer** — each INVARIANTS block entry includes a `cop:` pointer field naming the COP-NN items that enforce it; each COP-NN item includes an `invariant:` annotation naming its source invariant; bidirectional mapping makes protocol and invariant layers mutually verifiable at inspection time without manual cross-referencing | auditability | INVARIANTS entries without `cop:` pointers, or COP-NN items without `invariant:` annotations, is PARTIAL; one direction only is PARTIAL |
| C-38 | **Three-layer CO-EXTENSIVE DECLARATION** — CO-EXTENSIVE DECLARATION explicitly enumerates all three enforcement layers: STRUCTURAL-ERROR-CATALOG (catalog layer), INVARIANTS block (invariant layer), and COP-NN (protocol layer); declaration asserts all three independently attest the same structural properties and that any new structural property requires entries in all three layers | enforcement | CO-EXTENSIVE DECLARATION naming only CATALOG + INVARIANTS (two-layer) achieves C-33 PASS but fails C-38; all three layers named without the "all three required for new properties" assertion is PARTIAL |
```

---

**Summary of changes from v10 → v11:**

| Item | v10 | v11 |
|------|-----|-----|
| New criteria | — | C-37, C-38 |
| Aspirational count | 28 | 30 |
| Max score | 230 | 240 |
| Golden threshold | 191 | 201 |
| PARTIAL threshold | 140 | 150 |

The threshold increments (+10 each) match the value of the two new aspirational criteria both at PASS — they are achievable, so the thresholds scale to expect them.
