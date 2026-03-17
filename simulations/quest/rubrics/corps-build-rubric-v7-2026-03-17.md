Reading the R8 scorecard evidence notes for `(++)` patterns — the three new axes are V-01 (ENTRY-GATE bidirectional enforcement), V-02 (pre-execution STRUCTURAL-ERROR-CATALOG table), and V-03 (PROFILE-phase typed violation taxonomy). Each achieved PASS on all 24 v6 criteria and introduced a distinct structural innovation not yet rewarded.

New criteria: **C-25** (ENTRY-GATE bidirectional phase enforcement), **C-26** (pre-execution STRUCTURAL-ERROR-CATALOG), **C-27** (PROFILE-phase typed violation taxonomy).

Scoring: 16 aspirational → 19; 80 → 95; max 170 → 185; golden 82.9% × 185 ≈ 153; partial 60.7% × 185 ≈ 112.

---

```markdown
# corps-build Rubric — v7
**Updated**: 2026-03-17
**Based on**: Round 8 scorecard (V-01 through V-05)
**Changes from v6**: Added C-25, C-26, C-27 from R8 excellence signals; max updated 170 → 185; thresholds scaled.

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

**R8 pattern summary**: R8 revealed three structural innovations that extend constraint enforcement from single-directional to bidirectional, from inline to pre-declared, and from partial to full phase coverage. C-25 (ENTRY-GATE bidirectional phase enforcement) requires each phase start to name the prior required exit token with a named ENTRY-GATE-FAIL halt instruction if absent — creating bidirectional boundary enforcement where both phase exit and phase entry are explicitly named; V-01/V-04/V-05 demonstrated this with constructs like `ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS`, converting unidirectional exit-only chains into fully bounded corridors. C-26 (pre-execution STRUCTURAL-ERROR-CATALOG) requires an upfront typed catalog table listing all structural error codes with Code, Phase, and Trigger columns before Phase 1, so phase bodies reference codes by catalog name rather than re-defining inline; V-02 achieved the highest fidelity form, organizing all 13 codes into a single auditable pre-execution table with phase bodies annotating `(catalog)` on each reference — elevating the code system from distributed inline tokens to a pre-execution contract. C-27 (PROFILE-phase typed violation taxonomy) extends the typed code system from downstream phases to the upstream PROFILE derivation phase, requiring named STRUCTURAL-ERROR codes for category naming failure (STRUCTURAL-ERROR:PROFILE-CATEGORY), lens-underived failure (STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED), and duplicate-lens failure (STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS), organized as a dedicated typed violations table within Phase 5; V-03/V-05 demonstrated this, with V-03 additionally adding a labeled FAIL/PASS contrast pair within PROFILE that mirrors the C-22 IA contrast structure at the upstream derivation source, creating end-to-end contrast coverage from derivation through write.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 19 | 5 | 95 |
| **Max** | | | **185** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 153
**PARTIAL pass**: composite >= 112 with all 5 essential passing — earn full pass with 2/3 recommended

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
| C-10 | **Cross-reference integrity chart/roles** — explicit check statement: `Table Total = [n], files written = [n] — [MATCH \| MISMATCH]`; format is literal and auditable | correctness | Silent compliance is PARTIAL; emitted check string is PASS |
| C-11 | **Named invariants block** — a dedicated INVARIANTS block names the structural constraints governing the build; each invariant identified by a distinct name (e.g., INVARIANT-PATH-ISOLATION), not embedded in prose; at least one invariant per major phase gate | structure | Prose-only constraint statements are PARTIAL; named block with distinct identifiers is PASS |
| C-12 | **Auditable check-output** — verification steps emit literal, parseable check strings (e.g., `CROSS-REF: org.yaml slots: [n], files written: [n] -- MATCH`) rather than prose assertions | correctness | Silent or narrative compliance is PARTIAL; emitted literal check string is PASS |
| C-13 | **Named failure modes per criterion** — each aspirational criterion with a quality bar names at least one concrete failure mode — a specific wrong-path example, not generic prose — enabling testable failure detection | depth | Generic prose failure description is PARTIAL; named concrete example is PASS |
| C-14 | **Dedicated pre-step FAILURE MODES block** — each phase with constraint-bearing operations opens with a dedicated FAILURE MODES section listing what can go wrong in that phase; inline failure mentions without a dedicated block are PARTIAL | structure | Block must be labeled and appear before the phase body; trailing failure notes are PARTIAL |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — a dedicated CHECK-OUTPUT PROTOCOL (or equivalent labeled section) names the expected output format and check strings for the phase's verification steps, distinct from the phase body | structure | Verification steps embedded in phase prose without a named protocol section are PARTIAL |
| C-16 | **Phase-exit guard tokens** — each phase closes by emitting a named exit token (e.g., PARSE-PASS, VALIDATE-PASS, ROLES-COMPLETE); downstream phases name the required token; absence halts execution | correctness | Token names must be unique and non-generic; generic "complete" labels are PARTIAL |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — each file written within a phase emits a named TRANSCRIPTION-RECEIPT confirming successful write; receipts are referenced by BUILD-VERIFY as evidence of completeness | correctness | Batch-level receipts without per-artifact resolution are PARTIAL |
| C-18 | **BUILD-VERIFY single-purpose phase** — a dedicated BUILD-VERIFY phase exists solely for cross-checking all written artifacts; it does not produce new role files; its sole output is a completeness report and exit token | structure | Verification steps embedded in a write phase without a dedicated BUILD-VERIFY are PARTIAL |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — if a TRANSCRIPTION-RECEIPT is absent or fails within the phase, the phase provides an inline remediation path before proceeding; remediation must complete before the phase-exit token is emitted | correctness | Deferral to a later phase without inline remediation is PARTIAL |
| C-20 | **BUILD-VERIFY exclusion manifest** — BUILD-VERIFY emits a named EXCLUSION-MANIFEST listing files excluded from verification with the reason; typed table format with error codes per excluded type earns full PASS | depth | Prose-only exclusion list is PARTIAL; typed table with error codes per item is PASS |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — after any remediation, a TRANSCRIPTION-CLEAR re-audit step confirms all receipts are present before the BUILD-VERIFY-COMPLETE token is emitted; skipping re-audit after remediation is a structural error | correctness | Remediation without subsequent re-audit before token emission is PARTIAL |
| C-22 | **IA failure mode contrast pair** — the WRITE-IA step includes a labeled contrast pair — one transplantable generic phrasing example (FAIL) and one domain-derived specific phrasing example (PASS) — making the failure mode testable rather than abstract | depth | Single named failure mode without contrast is PARTIAL; labeled FAIL/PASS contrast pair is PASS |
| C-23 | **Typed STRUCTURAL-ERROR code taxonomy** — structural constraint violations are identified by unique named tokens (STRUCTURAL-ERROR:*) organized as a typed taxonomy; at minimum, codes cover phase-write violations, exclusion violations, and gate violations | structure | Inline codes without taxonomy structure are PARTIAL; organized typed table is PASS |
| C-24 | **Premature-exit violation named as STRUCTURAL-ERROR** — the premature phase-exit condition — emitting a phase-complete token before the required re-audit completes — carries an explicit STRUCTURAL-ERROR token (e.g., STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT), converting the gate declaration into a detectable error signal | correctness | Prose-only gate statement without named STRUCTURAL-ERROR token is PARTIAL |
| C-25 | **ENTRY-GATE bidirectional phase enforcement** — each phase start names the required prior exit token with a named ENTRY-GATE-FAIL halt instruction if absent (e.g., `ENTRY-GATE-FAIL: VALIDATE requires PARSE-PASS`); both phase exit and phase entry are explicitly named, creating bidirectional boundary enforcement | structure | Exit-only enforcement without named entry gates is PARTIAL; bidirectional named gates on all phases is PASS |
| C-26 | **Pre-execution STRUCTURAL-ERROR-CATALOG** — an upfront typed catalog table listing all structural error codes with Code, Phase, and Trigger columns appears before Phase 1; phase bodies reference codes by catalog name rather than re-defining inline | structure | Inline-only codes without a pre-execution catalog are PARTIAL; pre-execution catalog with phase bodies annotating references is PASS |
| C-27 | **PROFILE-phase typed violation taxonomy** — the PROFILE derivation phase carries its own typed STRUCTURAL-ERROR codes (at minimum STRUCTURAL-ERROR:PROFILE-CATEGORY, STRUCTURAL-ERROR:PROFILE-LENS-UNDERIVED, STRUCTURAL-ERROR:PROFILE-DUPLICATE-LENS) organized as a dedicated typed violations table; PROFILE gate closure conditions name specific STRUCTURAL-ERROR codes as required-absent for exit | depth | PROFILE with prose-only failure modes is PARTIAL; dedicated typed violations table with gate conditions is PASS; additionally adding a labeled FAIL/PASS contrast pair within PROFILE earns highest fidelity |
```
