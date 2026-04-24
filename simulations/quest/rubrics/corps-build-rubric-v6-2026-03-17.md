Reading the Round 7 scorecard evidence notes for patterns that went beyond what v5 criteria reward — the `(++)` signals are in the "highest fidelity" and "adds beyond PASS" language in the evidence notes:

- **C-20 evidence**: V-03/V-05 produce "typed EXCLUSION-MANIFEST table with error codes per excluded type (highest fidelity)" — C-20 only requires a named exclusion list; the typed code-per-item form is not yet captured.
- **C-19 evidence**: V-03/V-05 add "STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT as a named error for emitting CHART-WRITTEN before TRANSCRIPTION-CLEAR" — C-19 only requires a prose gate statement; the named violation token is not yet captured.
- **C-09/C-13 evidence**: V-05 provides "category-naming failure (e.g., 'the existing pipeline architecture' vs 'the event-resequencing buffer...') plus transplantable lens example" — a before/after contrast pair that makes the failure mode testable, beyond the single named example both criteria require.

Three new criteria: **C-22** (IA failure mode contrast pair), **C-23** (typed STRUCTURAL-ERROR code taxonomy), **C-24** (premature-exit violation named as STRUCTURAL-ERROR).

Scoring: 13 aspirational → 16; 65 → 80; max 155 → 170; golden 82.9% × 170 ≈ 141; partial 85/140 × 170 ≈ 103.

---

```markdown
# corps-build Rubric — v6
**Updated**: 2026-03-17
**Based on**: Round 7 scorecard (V-01 through V-05)
**Changes from v5**: Added C-22, C-23, C-24 from R7 excellence signals; max updated 155 → 170; thresholds scaled.

---

## What Changed

| Version | Change | Source |
|---------|--------|--------|
| v1 → v2 | Added C-11 (named invariants block), C-12 (auditable check-output), C-13 (named failure modes per criterion) | R3 excellence signals |
| v2 → v3 | Added C-14 (dedicated pre-step FAILURE MODES block), C-15 (named CHECK-OUTPUT PROTOCOL section) | R4 excellence signals |
| v3 → v4 | Added C-16 (phase-exit guard tokens), C-17 (per-artifact TRANSCRIPTION-RECEIPT), C-18 (BUILD-VERIFY single-purpose phase) | R5 excellence signals |
| v4 → v5 | Added C-19 (TRANSCRIPTION-RECEIPT in-phase remediation), C-20 (BUILD-VERIFY exclusion manifest), C-21 (TRANSCRIPTION-CLEAR all-artifact re-audit) | R6 excellence signals |
| v5 → v6 | Added C-22 (IA failure mode contrast pair), C-23 (typed STRUCTURAL-ERROR code taxonomy), C-24 (premature-exit violation named as STRUCTURAL-ERROR) | R7 excellence signals |

**R7 pattern summary**: R7 revealed three structural innovations that advance constraint enforcement from prose-based to code-based and add contrast-driven clarity to failure mode specification. C-22 (IA failure mode contrast pair) requires named IA failure modes to include a before/after contrast — transplantable generic phrasing alongside domain-derived specific phrasing — making the failure mode testable rather than abstract; V-05 demonstrated this with "the existing pipeline architecture" (transplantable, FAIL) vs. "the event-resequencing buffer that preserves order during backpressure" (domain-derived, PASS). C-23 (typed STRUCTURAL-ERROR code taxonomy) requires each structural constraint to be identified by a unique named string token organized as a typed taxonomy table, elevating invariants, exclusions, and gate violations from prose lists to grep-detectable codes; V-03/V-05 achieved this with entries like STRUCTURAL-ERROR:PHASE-2-FILE-WRITE and BV-FILE-WRITE forming a machine-matchable catalog. C-24 (premature-exit violation named as STRUCTURAL-ERROR) requires the premature phase-exit condition — emitting a phase-complete token before the required re-audit completes — to carry an explicit named STRUCTURAL-ERROR token rather than only a prose gate statement; V-03/V-05 demonstrated this with STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT, converting the gate declaration into a detectable error signal.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 16 | 5 | 80 |
| **Max** | | | **170** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 141
**PARTIAL pass**: composite >= 103 with all 5 essential passing — earn full pass with 2/3 recommended

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
| C-11 | **Named invariants block** — a dedicated INVARIANTS (or equivalent) block naming structural rules as machine-checkable conditions; each invariant is yes/no against output, not descriptive prose | structure | Prose restatement of rules is PARTIAL; named enumerable block is PASS |
| C-12 | **Auditable check-output** — check steps emit literal, parseable output strings rather than prose assertions; output format is consistent and machine-readable across all check steps | correctness | Prose-only or inconsistent check output is PARTIAL; literal format with named fields is PASS |
| C-13 | **Named failure modes per criterion** — each essential and recommended criterion has a named, concrete failure mode example; category-only descriptions ("may fail if not followed") are PARTIAL | depth | Named concrete example required for PASS; category label alone fails |
| C-14 | **Dedicated pre-step FAILURE MODES block** — each phase opens with a dedicated FAILURE MODES block before phase content begins; block names prohibitive conditions as discrete entries | structure | Absent or prose-embedded failure modes are PARTIAL; dedicated block at phase entry is PASS |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — check steps are organized under a named CHECK-OUTPUT PROTOCOL section; section defines expected output shape for each resolution path (e.g., PATH-A / PATH-B) | structure | Inline checks without a named protocol section are PARTIAL; named section with output shapes is PASS |
| C-16 | **Phase-exit guard tokens** — each phase closes with an explicit named guard token that must evaluate to YES before the next phase begins; prose-only phase close is PARTIAL | correctness | Named guard token (e.g., ROLES-COMPLETE, IA-PHASE-COMPLETE) required for PASS |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — each artifact (A, B, C) receives an individual verdict (VERBATIM or REVISED) in the TRANSCRIPTION-CLEAR step; a single combined receipt covering all three is PARTIAL | correctness | Three individually named receipts required for PASS |
| C-18 | **BUILD-VERIFY single-purpose phase** — BUILD-VERIFY does only verification; no file writes, no AMEND generation, no structural outputs; single-purpose scope is declared by the phase | behavior | Dual-purpose behavior fails; scope declaration required for PASS |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — a REVISED verdict triggers an immediate rewrite and updated receipt within the same phase; the phase cannot close with any REVISED verdict outstanding | correctness | Remediation loop described but without an explicit cannot-close gate is PARTIAL; gate stated is PASS |
| C-20 | **BUILD-VERIFY exclusion manifest** — BUILD-VERIFY has an explicit named list of what the phase must NOT do; scope is defined by enumerated prohibition, not only by purpose statement | behavior | Purpose-statement-only scope is PARTIAL; named exclusion list is PASS |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — a dedicated re-audit step confirms all three artifacts individually (A, B, C) in one pass, including those already VERBATIM before any rewrite; PATH-B exit token cannot emit until all three are confirmed VERBATIM | correctness | Re-audit covering only rewritten artifacts is PARTIAL; all-three individual confirmation is PASS |
| C-22 | **IA failure mode contrast pair** — the named IA failure mode includes an explicit before/after contrast: a transplantable (generic) phrasing example and a domain-derived (specific) phrasing example named side by side; a single named failure mode without a contrast pair is PARTIAL; a contrast pair showing both the wrong and correct form is PASS | depth | Extends C-09 and C-13; contrast pair makes the domain-derivation requirement testable rather than abstract; e.g., "the existing pipeline architecture" (transplantable, FAIL) vs. "the event-resequencing buffer that preserves order during backpressure" (domain-derived, PASS) |
| C-23 | **Typed STRUCTURAL-ERROR code taxonomy** — structural constraints (invariants, exclusions, gate violations) are represented as a typed taxonomy with a unique named string token per violation type (e.g., STRUCTURAL-ERROR:PHASE-2-FILE-WRITE, BV-FILE-WRITE); each code is grep-detectable in output; prose-only constraint enumeration without typed codes is PARTIAL; typed code taxonomy organized as a named table is PASS | structure | Extends C-11, C-14, C-20; the taxonomy form means every violation has a string identity, enabling output validation by name-match rather than by prose interpretation |
| C-24 | **Premature-exit violation named as STRUCTURAL-ERROR** — the premature phase-exit condition (emitting a phase-complete token before the required re-audit or remediation step finishes) is identified by an explicit named STRUCTURAL-ERROR token (e.g., STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT); a prose gate statement without a named violation token is PARTIAL; named premature-exit error token is PASS | correctness | Extends C-19; converts the gate declaration into a detectable error signal — violation presence is confirmed by string-match against the named code, not by prose interpretation of whether the gate was respected |
```
