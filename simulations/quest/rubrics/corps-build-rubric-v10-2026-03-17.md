Reading the scorecard to extract the new excellence signals before writing.

The scorecard shows three R11 axes:
- **V-01**: Full PASS on C-11 via dedicated INVARIANTS block with named identifiers paired to enforcement codes + CO-EXTENSIVE DECLARATION (C-15 PARTIAL)
- **V-02**: Full PASS on C-15 via numbered COP-NN items referenced from phase bodies (C-11 PARTIAL)
- **V-03**: New SPECIALIZATION-GATE pattern — per-team comparison block, gate-verdict in ROLES-COMPLETE, and explicit AMEND re-run

V-01 and V-02 demonstrate full PASS on existing criteria. V-03 introduces three genuinely new structural patterns not covered by C-01 through C-33. Those become C-34, C-35, C-36.

```markdown
# corps-build Rubric — v10
**Updated**: 2026-03-17
**Based on**: Round 11 scorecard (V-01 through V-03)
**Changes from v9**: Added C-34, C-35, C-36 from R11 excellence signals; max updated 215 → 230; thresholds scaled.

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

**R11 pattern summary**: R11 revealed three structural innovations centered on specialization-gate auditing. C-34 (SPECIALIZATION-GATE per-team comparison block) introduces a named per-team gate in the WRITE-ROLES phase requiring a per-role comparison table distinguishing standard from specialized content across every role dimension, with an explicit gate-verdict (SPECIALIZATION-GATE: PASS|FAIL) that must resolve before advancing to the next team; this converts the specialization distinction from a write-time style constraint (C-07) into an auditable per-team comparison gate with a named verdict, making copy-from-standard violations detectable at build time rather than review time; V-03 demonstrated this with a named SPECIALIZATION-GATE block per team in Phase 7, and ROLES-COMPLETE including `all-specialization-gates-passed: YES`. C-35 (ROLES-COMPLETE specialization-gates attestation) extends the ROLES-COMPLETE terminal token to include an `all-specialization-gates-passed: YES|NO` field; NO is a recoverable in-phase state that triggers a named halt and per-team re-audit before ROLES-COMPLETE closes, mirroring the ROLES-WRITTEN NO-halt remediation cycle (C-31) at the specialization audit layer; this makes the specialization gate a closing condition of the entire WRITE-ROLES phase rather than a per-team check that could be silently skipped or left unresolved; V-03 demonstrated this with `all-specialization-gates-passed: YES` as a required field in ROLES-COMPLETE. C-36 (AMEND --area SPECIALIZATION-GATE re-run) requires that the AMEND --area repair chain explicitly re-run the SPECIALIZATION-GATE per team during Phase 7 re-execution rather than inheriting prior gate verdicts; this closes a gap where AMEND --area could regenerate roles that pass PROFILE-REDERIVE and IA-WRITTEN checks but silently regress specialization distinctness because the comparison gate was not re-evaluated; V-03 demonstrated this with AMEND --area explicitly naming the SPECIALIZATION-GATE per team in the Phase 7 re-run description, making specialization re-audit a named member of the AMEND chain alongside PROFILE-REDERIVE and ROLES-WRITTEN.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 28 | 5 | 140 |
| **Max** | | | **230** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 191
**PARTIAL pass**: composite >= 140 with all 5 essential passing — earn full pass with 2/3 recommended

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
| C-11 | **Named invariants block** — a dedicated INVARIANTS block names the structural constraints governing the build; each invariant identified by a distinct name (e.g., INVARIANT-PATH-ISOLATION), not embedded in prose; at least one invariant per major phase gate | structure | Prose-only constraint statements are PARTIAL; named block with distinct identifiers paired to enforcement codes is PASS |
| C-12 | **Auditable check-output** — verification steps emit literal, parseable check strings (e.g., `CROSS-REF: org.yaml slots: [n], files written: [n] -- MATCH`) rather than prose assertions | correctness | Silent or narrative compliance is PARTIAL; emitted literal check string is PASS |
| C-13 | **Named failure modes per criterion** — each aspirational criterion with a quality bar names at least one concrete failure mode — a specific wrong-path example, not generic prose — enabling testable failure detection | depth | Generic prose failure description is PARTIAL; named concrete example is PASS |
| C-14 | **Dedicated pre-step FAILURE MODES block** — a named FAILURE MODES section appears before the first phase step, listing concrete failure paths with named codes or labels; not embedded within phase bodies | structure | Inline failure notes scattered through phases are PARTIAL; dedicated named pre-step block is PASS |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — a dedicated section or block named CHECK-OUTPUT PROTOCOL (or equivalent) enumerates the check strings that must be emitted and their expected format; phase bodies reference this protocol by name | structure | Undifferentiated check strings without a named protocol section are PARTIAL; named protocol section with numbered items (e.g., COP-NN) referenced from phase bodies is PASS |
| C-16 | **Phase-exit guard tokens** — each phase boundary is named with a distinct exit token (e.g., PARSE-PASS, VALIDATE-PASS, PROFILE-GATE); subsequent phases name the required preceding token as their entry condition; chain is unbroken | structure | Unnamed phase transitions are PARTIAL; named token chain with no gaps is PASS |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — a named TRANSCRIPTION-RECEIPT block emits a VERBATIM\|REVISED verdict for each artifact written; receipt covers all artifacts, not a subset | correctness | Partial artifact coverage is PARTIAL; all-artifact receipt with per-artifact verdicts is PASS |
| C-18 | **BUILD-VERIFY single-purpose phase** — BUILD-VERIFY is declared to have exactly one responsibility; an EXCLUSION-MANIFEST table names what BUILD-VERIFY explicitly does not do | structure | Unscoped BUILD-VERIFY without exclusion manifest is PARTIAL; single-responsibility declaration + named exclusion manifest is PASS |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — REVISED verdict in TRANSCRIPTION-RECEIPT triggers a named in-phase remediation step (describe revision reason, confirm faithfulness to org.yaml) before advancing; REVISED is recoverable, not a silent pass | correctness | REVISED without in-phase remediation path is PARTIAL; named remediation step required for PASS |
| C-20 | **BUILD-VERIFY exclusion manifest** — a formal EXCLUSION-MANIFEST table is present within BUILD-VERIFY listing actions explicitly excluded from that phase, one row per excluded action | structure | Prose exclusion list is PARTIAL; formal named table is PASS |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — a named TRANSCRIPTION-CLEAR attestation confirms all artifacts have been re-audited and authorizes the next phase gate; emitted as a literal token, not inferred from individual receipts | correctness | Individual receipts without TRANSCRIPTION-CLEAR token are PARTIAL; explicit TRANSCRIPTION-CLEAR authorization token is PASS |
| C-22 | **IA failure mode contrast pair** — the WRITE-IA step includes an explicit FAIL/PASS contrast pair: one named example of generic IA content (FAIL) and one named example of team-domain-contextualized IA content (PASS); contrast pair is embedded in the phase body | depth | Single-example or prose-only guidance is PARTIAL; explicit FAIL/PASS contrast pair in phase body is PASS |
| C-23 | **Typed STRUCTURAL-ERROR code taxonomy** — all named violation codes follow a consistent typed prefix scheme (e.g., STRUCTURAL-ERROR:PATH-*, STRUCTURAL-ERROR:PROFILE-*); every violation in the catalog has a typed code; ad-hoc or untyped violation names fail | structure | Mixed typed/untyped codes are PARTIAL; fully typed consistent taxonomy is PASS |
| C-24 | **Premature-exit violation named as STRUCTURAL-ERROR** — premature phase exit (advancing without completing the required phase body) is named as a typed STRUCTURAL-ERROR code in the catalog; the code is referenced as an enforcement condition within the phase that can be exited prematurely | structure | Premature exit described in prose without a named catalog code is PARTIAL; named STRUCTURAL-ERROR code with in-phase enforcement reference is PASS |
| C-25 | **ENTRY-GATE bidirectional phase enforcement** — each phase names both its required entry token (predecessor gate) and its exit token (successor gate); ENTRY-GATE-FAIL is a named STRUCTURAL-ERROR triggered if a phase begins without its predecessor token; no phase in the chain is exempt | structure | Phases with entry token but no exit token (or vice versa) are PARTIAL; full bidirectional chain with ENTRY-GATE-FAIL enforcement is PASS |
| C-26 | **Pre-execution STRUCTURAL-ERROR-CATALOG** — the STRUCTURAL-ERROR-CATALOG is declared before all phase bodies; the catalog is complete at declaration time, not appended to during phase execution | structure | Catalog appended during execution or declared after any phase body is PARTIAL; pre-execution complete declaration is PASS |
| C-27 | **PROFILE-phase typed violation taxonomy** — the PROFILE phase includes a per-team STRUCTURAL-ERROR block enumerating PROFILE-specific violation codes (e.g., STRUCTURAL-ERROR:PROFILE-INCOMPLETE, STRUCTURAL-ERROR:PROFILE-STALE); codes reference the fields or conditions they enforce | structure | PROFILE violations described in prose or without typed codes are PARTIAL; per-team named block with STRUCTURAL-ERROR:PROFILE-* codes is PASS |
| C-28 | **ROLES-WRITTEN per-team field-completeness receipt** — ROLES-WRITTEN emits a per-team receipt with an explicit `standard-fields-complete: YES\|NO` verdict covering all five typed fields; receipt is emitted for every team before advancing, not as a summary after all teams | correctness | Summary-only receipt or omitted per-team receipt is PARTIAL; per-team receipt with field-completeness verdict is PASS |
| C-29 | **AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate** — AMEND --area triggers a named PROFILE-REDERIVE step that re-derives the full area profile before re-writing roles; PROFILE-REDERIVE-COMPLETE is a required gate before WRITE-IA; the repair chain does not skip PROFILE re-derivation | behavior | AMEND --area that rewrites roles without named PROFILE-REDERIVE gate is PARTIAL; named PROFILE-REDERIVE → PROFILE-REDERIVE-COMPLETE gate in chain is PASS |
| C-30 | **CATALOG-CLOSURE terminal attestation** — a named CATALOG-CLOSURE block closes the STRUCTURAL-ERROR-CATALOG; the block enumerates all catalog codes with their TRIGGERED\|NOT-TRIGGERED status; TRIGGERED codes require a `triggered-at` + `resolved-by` pair before CATALOG-CLOSURE emits | structure | Catalog that closes without per-code status attestation is PARTIAL; CATALOG-CLOSURE with full triggered/resolved accounting is PASS |
| C-31 | **ROLES-WRITTEN NO-halt remediation cycle** — a per-team `standard-fields-complete: NO` verdict in ROLES-WRITTEN triggers a named within-phase remediation loop: identify deficient fields → rewrite → re-emit receipt → confirm YES; the loop must confirm YES before advancing to the next team; NO is a recoverable in-phase state, not a silent halt | correctness | NO verdict without named remediation loop is PARTIAL; named loop with YES confirmation gate is PASS |
| C-32 | **AMEND-CHAIN-COMPLETE terminal token** — the AMEND --area repair chain emits a named terminal token AMEND-CHAIN-COMPLETE after all chain stages (PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY) pass; AMEND --area cannot return to the caller without AMEND-CHAIN-COMPLETE; the token records PROFILE-DELTA, files-regenerated, ROLES-WRITTEN-summary, and BUILD-VERIFY-summary | behavior | AMEND --area that completes without a named terminal token is PARTIAL; AMEND-CHAIN-COMPLETE with required summary fields is PASS |
| C-33 | **STRUCTURAL-ERROR-CATALOG declared as INVARIANTS contract** — the CATALOG-CLOSURE block or a co-located declaration explicitly states that the STRUCTURAL-ERROR-CATALOG constitutes the complete invariants contract for the build: all structural invariants are encoded as typed error codes, no invariant exists outside the catalog; CATALOG-CLOSURE CLEAN = invariants contract satisfied | structure | Catalog that does not declare its co-extensiveness with the invariants contract is PARTIAL; explicit co-extensive declaration bridging CATALOG-CLOSURE and the INVARIANTS concept is PASS |
| C-34 | **SPECIALIZATION-GATE per-team comparison block** — a named SPECIALIZATION-GATE block per team in the write-roles phase contains a per-role comparison table distinguishing standard from specialized content across every role dimension; the block emits an explicit gate-verdict (`SPECIALIZATION-GATE: PASS\|FAIL`); FAIL triggers named in-phase remediation before advancing to the next team | correctness | C-07 requires specialization distinction; C-34 requires it be audited per-team with a named comparison table and gate-verdict. Specialization gate without comparison table is PARTIAL; named comparison table + gate-verdict + named FAIL remediation path is PASS |
| C-35 | **ROLES-COMPLETE specialization-gates attestation** — the ROLES-COMPLETE terminal token includes an `all-specialization-gates-passed: YES\|NO` field; NO is a recoverable in-phase state that triggers a named halt and per-team re-audit before ROLES-COMPLETE closes; ROLES-COMPLETE may not be emitted with `all-specialization-gates-passed: NO` | correctness | ROLES-COMPLETE without specialization-gates field is PARTIAL; field present with NO-halt remediation path required before closure is PASS |
| C-36 | **AMEND --area SPECIALIZATION-GATE re-run** — the AMEND --area repair chain explicitly names a SPECIALIZATION-GATE re-run per team during Phase 7 re-execution; prior gate verdicts are not inherited from the previous build; specialization distinctness is re-audited as a named member of the AMEND chain alongside PROFILE-REDERIVE and ROLES-WRITTEN | behavior | AMEND --area that silently inherits prior SPECIALIZATION-GATE verdicts or omits specialization re-audit from the chain description is PARTIAL; explicit named SPECIALIZATION-GATE re-run in AMEND chain is PASS |
```
