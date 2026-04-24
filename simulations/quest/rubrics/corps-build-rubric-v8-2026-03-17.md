Reading the R9 scorecard for `(++)` patterns across the five variations. The three axis innovations are:

- **V-01**: ROLES-WRITTEN per-team receipt — per-team `standard-fields-complete: YES/NO` check on all five fields within ROLES-WRITTEN, each team gets its own receipt before proceeding
- **V-02**: AMEND PROFILE-REDERIVE — `--area` triggers PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY chain with named PROFILE-REDERIVE-COMPLETE gate; AMEND --area cannot enter IA-WRITTEN without it
- **V-03**: CATALOG-CLOSURE attestation — named terminal block after STRUCTURAL-ERROR-CATALOG declaring the catalog exhaustively complete; closed-world guarantee for the error taxonomy

New criteria: **C-28** (per-team field-completeness receipt in ROLES-WRITTEN), **C-29** (AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate), **C-30** (CATALOG-CLOSURE terminal attestation).

Scoring: 19 aspirational → 22; max 185 → 200; golden 82.9% × 200 ≈ 166; partial 60.7% × 200 ≈ 121.

---

```markdown
# corps-build Rubric — v8
**Updated**: 2026-03-17
**Based on**: Round 9 scorecard (V-01 through V-05)
**Changes from v7**: Added C-28, C-29, C-30 from R9 excellence signals; max updated 185 → 200; thresholds scaled.

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

**R9 pattern summary**: R9 revealed three structural innovations that extend quality enforcement from phase-level to team-level granularity, from repair-option naming to full repair-chain gating, and from open-ended catalogs to closed-world attestation. C-28 (ROLES-WRITTEN per-team field-completeness receipt) requires the ROLES-WRITTEN phase to emit a named per-team receipt with `standard-fields-complete: YES/NO` verdict covering all five typed fields before moving to the next team — shifting verification from a single global count gate to a team-grained quality checkpoint; V-01/V-04/V-05 demonstrated this with per-team receipt emission that prevents partial-field teams from propagating forward while the global CROSS-REF count remains intact. C-29 (AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate) requires that the `--area` AMEND option name a complete re-derivation chain of PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE as a named phase-exit token; AMEND --area cannot enter IA-WRITTEN without PROFILE-REDERIVE-COMPLETE — elevating AMEND from a menu of named options to a gated re-derivation contract that mirrors the forward-pass phase structure; V-02/V-04/V-05 demonstrated this with PROFILE-REDERIVE-COMPLETE explicitly required before downstream repair continues. C-30 (CATALOG-CLOSURE terminal attestation) requires a named CATALOG-CLOSURE block or token following the STRUCTURAL-ERROR-CATALOG table that declares the catalog exhaustively complete — all codes that can occur in the build are listed, no undeclared structural errors exist; this converts the catalog from an open enumeration into a closed-world contract; V-03/V-05 demonstrated this with a dedicated attestation statement that bounds the error taxonomy and makes any runtime structural error either cataloged or a rubric violation.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 22 | 5 | 110 |
| **Max** | | | **200** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 166
**PARTIAL pass**: composite >= 121 with all 5 essential passing — earn full pass with 2/3 recommended

---

## Criteria

### Essential (12 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-01 | **Role file completeness** — total file count in summary equals count of files written in Step 2; gap identified and resolved before proceeding | correctness | PASS requires verification mechanism, not just count statement |
| C-02 | **org-chart.md with ASCII hierarchy** — uses `+--` / `\|` notation; all org.yaml names verbatim; nesting reflects group → team depth | format | Concrete example or INVARIANT declaration required for PASS |
| C-03 | **Inertia Advocate in every team** — one IA per team, no exceptions; enforced as a closure gate before moving to next team | correctness | "Mandatory" imperative + enforcement hook required |
| C-04 | **org.yaml structural fidelity** — files written only to subdirectories derived from org.yaml; path pattern `.roles/{area-slug}/{role-slug}.md` | correctness | Pre-write path validation required for PASS |
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
| C-10 | **Cross-reference integrity chart/roles** — explicit check statement: `Table Total = [n], files written = [n] — [MATCH \| MISMATCH]`; format is literal and auditable | correctness | Silent compliance is PARTIAL; emitted check string is PASS |
| C-11 | **Named invariants block** — a dedicated INVARIANTS block names the structural constraints governing the build; each invariant identified by a distinct name (e.g., INVARIANT-PATH-ISOLATION), not embedded in prose; at least one invariant per major phase gate | structure | Prose-only constraint statements are PARTIAL; named block with distinct identifiers is PASS |
| C-12 | **Auditable check-output** — verification steps emit literal, parseable check strings (e.g., `CROSS-REF: org.yaml slots: [n], files written: [n] -- MATCH`) rather than prose assertions | correctness | Silent or narrative compliance is PARTIAL; emitted literal check string is PASS |
| C-13 | **Named failure modes per criterion** — each aspirational criterion with a quality bar names at least one concrete failure mode — a specific wrong-path example, not generic prose — enabling testable failure detection | depth | Generic prose failure description is PARTIAL; named concrete example is PASS |
| C-14 | **Dedicated pre-step FAILURE MODES block** — a named FAILURE MODES section appears before the first phase step, listing concrete failure paths with named codes or labels; not embedded within phase bodies | structure | Inline failure notes scattered through phases are PARTIAL; dedicated named pre-step block is PASS |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — a dedicated section or block named CHECK-OUTPUT PROTOCOL (or equivalent) enumerates the check strings that must be emitted and their expected format; phase bodies reference this protocol by name | structure | Undifferentiated check strings without a named protocol section are PARTIAL; named protocol section referenced from phases is PASS |
| C-16 | **Phase-exit guard tokens** — each phase boundary is named with a distinct exit token (e.g., PARSE-PASS, VALIDATE-PASS, PROFILE-GATE); subsequent phases name the required preceding token as their entry condition; chain is unbroken | structure | Unnamed phase transitions are PARTIAL; named token chain with no gaps is PASS |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — a named TRANSCRIPTION-RECEIPT block emits a VERBATIM\|REVISED verdict for each artifact written; receipt covers all artifacts, not a subset | correctness | Partial artifact coverage is PARTIAL; all-artifact receipt with per-artifact verdicts is PASS |
| C-18 | **BUILD-VERIFY single-purpose phase** — BUILD-VERIFY is declared to have exactly one responsibility; an EXCLUSION-MANIFEST table names what BUILD-VERIFY explicitly does not do | structure | Unscoped BUILD-VERIFY without exclusion manifest is PARTIAL; single-responsibility declaration + named exclusion manifest is PASS |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — when TRANSCRIPTION-RECEIPT yields a REVISED verdict, a named remediation path (PATH-B) requires rewrite of the deviant artifact followed by re-emission of a new TRANSCRIPTION-RECEIPT before TRANSCRIPTION-CLEAR can be issued | correctness | REVISED verdict with no named remediation path is PARTIAL; named PATH-B with re-receipt requirement is PASS |
| C-20 | **BUILD-VERIFY exclusion manifest** — EXCLUSION-MANIFEST table lists at least five distinct categories of work excluded from BUILD-VERIFY, each with a named code (e.g., BV-FILE-WRITES, BV-COUNT-CHECKS); table is referenced from within the BUILD-VERIFY phase body | structure | Prose exclusion list without named codes is PARTIAL; coded table referenced from phase body is PASS |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — TRANSCRIPTION-CLEAR explicitly names all artifacts subject to re-audit; a statement that fewer than the total artifact count constitutes a structurally incomplete TRANSCRIPTION-CLEAR | correctness | TRANSCRIPTION-CLEAR without named artifact list or completeness assertion is PARTIAL; named all-artifact list with incompleteness declaration is PASS |
| C-22 | **IA failure mode contrast pair** — the Inertia Advocate criterion names a labeled FAIL example (transplantable generic phrase) alongside a labeled PASS example (team-domain-specific vocabulary); both examples are concrete, not described in prose | depth | Single-direction example or prose contrast is PARTIAL; labeled FAIL/PASS pair with concrete examples is PASS |
| C-23 | **Typed STRUCTURAL-ERROR code taxonomy** — structural error conditions are named with a typed code schema (e.g., STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT); codes appear in a catalog with Code, Phase, and Trigger columns; taxonomy covers at least two distinct phases | structure | Untyped error labels or single-phase coverage is PARTIAL; typed schema with multi-phase catalog table is PASS |
| C-24 | **Premature-exit violation named as STRUCTURAL-ERROR** — at least one premature-exit scenario (proceeding past a phase gate without the required exit token) is explicitly named as a STRUCTURAL-ERROR code in the catalog; the named code appears in the relevant phase body | correctness | Implicit or prose-described premature-exit violation without a catalog code is PARTIAL; named STRUCTURAL-ERROR code in catalog + phase body is PASS |
| C-25 | **ENTRY-GATE bidirectional phase enforcement** — each phase names both its exit token and the prior phase's exit token as its ENTRY-GATE; a named ENTRY-GATE-FAIL halt instruction is stated if the required prior token is absent; enforcement is bidirectional at every phase boundary | structure | Exit-only token chains without named ENTRY-GATE-FAIL instructions are PARTIAL; bidirectional enforcement with named halt at every boundary is PASS |
| C-26 | **Pre-execution STRUCTURAL-ERROR-CATALOG** — the full typed error catalog appears as a table before Phase 1; phase bodies reference catalog codes by name with a notation (e.g., `(catalog)`) indicating the code is pre-declared rather than inline-defined; no new codes are introduced within phase bodies | structure | Catalog embedded within phases or phase bodies redefining codes inline are PARTIAL; pre-execution table with phase bodies referencing by catalog notation is PASS |
| C-27 | **PROFILE-phase typed violation taxonomy** — the PROFILE phase contains a dedicated typed violations block listing named STRUCTURAL-ERROR codes for category-naming failure, lens-underived failure, and duplicate-lens failure; the block is organized as a table within the PROFILE phase body and includes enforcement conditions | structure | PROFILE violations described in prose without typed codes or dedicated block are PARTIAL; named typed violations table within PROFILE phase body is PASS |
| C-28 | **ROLES-WRITTEN per-team field-completeness receipt** — within the ROLES-WRITTEN phase, each team emits a named per-team receipt with a `standard-fields-complete: YES/NO` verdict covering all five typed fields before proceeding to the next team; global phase-complete is gated on all per-team receipts reaching YES; a single global count check without per-team receipts does not satisfy | correctness | Global post-hoc count check without per-team receipts is PARTIAL; per-team in-phase receipt with named YES/NO field verdict is PASS |
| C-29 | **AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate** — the `--area` AMEND option names a complete re-derivation chain of PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE as a named phase-exit token; AMEND --area cannot enter IA-WRITTEN without PROFILE-REDERIVE-COMPLETE; chain mirrors the forward-pass phase structure at the repair path | behavior | Naming only IA-WRITTEN re-run without upstream PROFILE re-derivation is PARTIAL; full named chain with PROFILE-REDERIVE-COMPLETE gate is PASS |
| C-30 | **CATALOG-CLOSURE terminal attestation** — a named CATALOG-CLOSURE block or terminal token follows the STRUCTURAL-ERROR-CATALOG table and declares the catalog exhaustively complete; the attestation states that all structural error codes that can occur in the build are listed and no undeclared structural errors can arise; this converts the catalog from an open enumeration into a closed-world contract | structure | Pre-execution catalog table without closure attestation is PARTIAL; named CATALOG-CLOSURE block with closed-world declaration is PASS |
```
