---

# corps-build Rubric — v9
**Updated**: 2026-03-17
**Based on**: Round 10 scorecard (V-01 through V-05)
**Changes from v8**: Added C-31, C-32, C-33 from R10 excellence signals; max updated 200 → 215; thresholds scaled.

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

**R10 pattern summary**: R10 revealed three structural innovations that deepen R9's three axis criteria from declarations into gated contracts with defined continuations. C-31 (ROLES-WRITTEN NO-halt remediation cycle) extends C-28 by requiring that a per-team `standard-fields-complete: NO` verdict trigger a named within-phase remediation loop — rewrite deficient fields → re-emit per-team receipt → confirm YES before advancing to the next team — rather than leaving NO as an unspecified halt; this converts the receipt gate from a checkpoint that can strand a build into a gated remediation cycle with a defined resolution path; R10 V-04/V-05 demonstrated this with the named loop embedded in the ROLES-WRITTEN phase body, making NO a recoverable in-phase state. C-32 (AMEND-CHAIN-COMPLETE terminal token) extends C-29 by requiring that the AMEND --area repair chain (PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE) emit a named terminal token AMEND-CHAIN-COMPLETE after all three stages pass; AMEND --area cannot return to the caller without AMEND-CHAIN-COMPLETE — mirroring how BUILD-VERIFY-COMPLETE closes the forward pass and ensuring the repair chain has its own auditable closure signal rather than silently completing; R10 V-02/V-04/V-05 demonstrated AMEND-CHAIN-COMPLETE as a required exit from the repair chain. C-33 (STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract) resolves a persistent C-11 PARTIAL signal across all R10 variations by requiring that the CATALOG-CLOSURE block or a co-located declaration explicitly state that the STRUCTURAL-ERROR-CATALOG constitutes the complete invariants contract for the build — all structural invariants are encoded as typed error codes, no invariant exists outside the catalog; this elevates the catalog from an error taxonomy into a dual-function INVARIANTS contract, so a runtime structural error is either cataloged (covered by a named code) or a rubric violation (invariant not encoded); R10 V-03/V-05 demonstrated this with an explicit co-extensive declaration bridging CATALOG-CLOSURE and the INVARIANTS concept.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 25 | 5 | 125 |
| **Max** | | | **215** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 178
**PARTIAL pass**: composite >= 131 with all 5 essential passing — earn full pass with 2/3 recommended

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
| C-28 | **ROLES-WRITTEN per-team field-completeness receipt** — within the ROLES-WRITTEN phase, each team emits a named per-team receipt with a `standard-fields-complete: YES/NO` verdict covering all five typed fields before proceeding to the next team; global phase-complete is gated on all per-team receipts reaching YES | correctness | Global post-hoc count check without per-team receipts is PARTIAL; per-team in-phase receipt with named YES/NO field verdict is PASS |
| C-29 | **AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate** — the `--area` AMEND option names a complete re-derivation chain of PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE as a named phase-exit token; AMEND --area cannot enter IA-WRITTEN without PROFILE-REDERIVE-COMPLETE; chain mirrors the forward-pass phase structure at the repair path | behavior | Naming only IA-WRITTEN re-run without upstream PROFILE re-derivation is PARTIAL; full named chain with PROFILE-REDERIVE-COMPLETE gate is PASS |
| C-30 | **CATALOG-CLOSURE terminal attestation** — a named CATALOG-CLOSURE block or terminal token follows the STRUCTURAL-ERROR-CATALOG table and declares the catalog exhaustively complete; the attestation states that all structural error codes that can occur in the build are listed and no undeclared structural errors can arise | structure | Pre-execution catalog table without closure attestation is PARTIAL; named CATALOG-CLOSURE block with closed-world declaration is PASS |
| C-31 | **ROLES-WRITTEN NO-halt remediation cycle** — when a per-team receipt emits `standard-fields-complete: NO`, the ROLES-WRITTEN phase body defines a named within-phase remediation loop: rewrite deficient fields → re-emit per-team receipt → confirm YES before advancing to the next team; NO is a gated remediation trigger with a defined resolution path, not an unspecified halt; the loop is embedded in the ROLES-WRITTEN phase body, not deferred to AMEND | correctness | Per-team NO verdict with no named remediation path is PARTIAL; named within-phase remediation loop with re-receipt requirement and YES confirmation gate is PASS |
| C-32 | **AMEND-CHAIN-COMPLETE terminal token** — the AMEND --area repair chain (PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY with PROFILE-REDERIVE-COMPLETE) emits a named terminal token AMEND-CHAIN-COMPLETE after all three stages pass; AMEND --area cannot return to the caller without AMEND-CHAIN-COMPLETE; the token mirrors BUILD-VERIFY-COMPLETE for the forward pass and provides an auditable closure signal for the repair chain | behavior | AMEND chain completing without a named terminal token is PARTIAL; explicit AMEND-CHAIN-COMPLETE token required at chain exit before caller return is PASS |
| C-33 | **STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract** — the CATALOG-CLOSURE block or a co-located declaration explicitly states that the STRUCTURAL-ERROR-CATALOG constitutes the complete invariants contract for the build: all structural invariants are encoded as typed error codes, no invariant exists outside the catalog, and any runtime structural error is either cataloged (covered by a named code) or a rubric violation (invariant not encoded); this makes STRUCTURAL-ERROR-CATALOG and INVARIANTS co-extensive by declaration | structure | CATALOG-CLOSURE without explicit INVARIANTS contract declaration is PARTIAL; named co-extensive declaration bridging catalog and invariants contract is PASS |

---

Written to `simulations/quest/rubrics/corps-build-rubric-v9-2026-03-17.md`.

**Three new criteria extracted from R10:**

- **C-31** extends C-28: the per-team receipt gate now requires a named remediation loop when `standard-fields-complete: NO` — NO becomes a recoverable in-phase state, not a silent halt
- **C-32** extends C-29: the AMEND --area repair chain requires a terminal `AMEND-CHAIN-COMPLETE` token mirroring `BUILD-VERIFY-COMPLETE`, making the repair chain auditably closed
- **C-33** resolves the persistent C-11 PARTIAL: the `CATALOG-CLOSURE` block must declare `STRUCTURAL-ERROR-CATALOG` and INVARIANTS co-extensive — all invariants encoded as typed codes, no invariant outside the catalog

The C-11 PARTIAL signal that appeared across every R10 variation was the tell: top variations were already treating the catalog as the invariants contract but hadn't declared it formally. C-33 names that declaration as a first-class requirement.
