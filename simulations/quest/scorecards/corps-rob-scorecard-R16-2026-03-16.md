# corps-rob R16 — Scorecard

## Scoring Framework

| Parameter | Value |
|-----------|-------|
| Max composite (v16) | 290 |
| Aspirational pool | 40 × 5 = 200 |
| Essential + Recommended | 90 (5 essential × 6 + 3 recommended × 20) |
| R15 V-05 base under v16 | 285/290 (1 persistent gap = 5 pts) |

---

## Criterion-by-Criterion Scoring

### Essential Criteria (C-01 to C-05) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-01 | Stage identity and labeling | PASS | PASS | PASS | PASS | PASS | `## Stage: [stage-name]` header template present in all |
| C-02 | Role-loaded perspective | PASS | PASS | PASS | PASS | PASS | `ROLE: [name] \| Frame: [...] \| Lens: [...]` field + findings cite Via from lens |
| C-03 | ROB document format compliance | PASS | PASS | PASS | PASS | PASS | Labeled findings table, verdict table, TPM Go/No-Go, Mission Cascade all templated |
| C-04 | Actionable findings 2× per stage | PASS | PASS | PASS | PASS | PASS | Findings section mandates "minimum 2 findings per stage; severity must vary" |
| C-05 | Go/No-Go in TPM stage | PASS | PASS | PASS | PASS | PASS | `### Go/No-Go` with `GO / NO-GO / GO WITH CONDITIONS` in TPM section |

**All essential: PASS across all variations.**

---

### Recommended Criteria (C-06 to C-08) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-06 | Cross-stage coherence | PASS | PASS | PASS | PASS | PASS | CARRY FORWARD blocks + FINDING LEDGER + Dual-Direction Traceability ensure ≥2 cross-stage references structurally |
| C-07 | Structured risk register in TPM | PASS | PASS | PASS | PASS | PASS | Risk Register table with title/severity/likelihood/mitigation/Inertia Link/status; ≥3 rows, ≥1 HIGH, ≥2 distinct Status values |
| C-08 | Exec-office cascade tracing | PASS | PASS | PASS | PASS | PASS | SPIRE stage Mission Cascade table: `\| S-Office Mission \| Program \| Artifact/Topic \| Alignment \|`; named mission required |

**All recommended: PASS across all variations.**

---

### Aspirational Criteria — Scoring Notes (C-09 to C-48)

For brevity, criteria with identical status across all 5 variations (all PASS or all FAIL) are grouped. Variation-specific delta notes follow.

#### C-09 through C-39 — Carried from R15 V-05 Base

| ID | Criterion | All V-01–V-05 | Evidence note |
|----|-----------|---------------|---------------|
| C-09 | Inter-stage blocker detection | PASS | BLOCKER record format present in all; `BLOCKER: [upstream] [LID] blocks [downstream]: [impact]`; min 1 per run instructed |
| C-10 | Cross-cutting theme elevation | PASS | CROSS-CUTTING THEMES section in all; document-level `## Cross-Cutting Theme:` header with stage sources and severity escalation |
| C-11 | Conditional verdict itemization | PASS | RULE CONDITIONAL-ITEM: numbered items (1) what, (2) owner by role, (3) LID driving condition |
| C-12 | Finding severity discrimination | PASS | "severity must vary" instruction in findings template; calibration block ensures spread |
| C-13 | Risk register status lifecycle | PASS | Status column (OPEN / WATCH / MITIGATED) in risk register template; ≥2 distinct values required |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR) before findings in every stage |
| C-15 | Risk register update protocol | PASS | Risk Register Update Protocol table with Trigger Events / Owner Role / Revisit Cadence in TPM section |
| C-16 | Role-lens pre-declaration | PASS | `ROLE LENS: [what this role most fears for this specific topic...]` in Calibration Block; topic-specific requirement stated |
| C-17 | Pre-commitment enforcement audit | PASS | POST-STAGE AUDIT SUITE: CALIBRATION AUDIT is the enforcement audit section with named pre-commitments checked |
| C-18 | Universal per-stage triage note | PASS | `### Triage Note` with HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR in every stage template unconditionally |
| C-19 | Zero-deviation explicit declaration | PASS | RULE ZERO-STATE: "Silence is not clean — explicit zero-state required"; VIOLATIONS: NONE / GAPS: NONE / `(a) NONE` per-condition enumeration |
| C-20 | Enforcement audit structured table | PASS | CALIBRATION AUDIT has `\| Stage \| HIGH DRIVER \| LOW ANCHOR \| DISTRIBUTION FACTOR \| Honored \| Deviation \|` table |
| C-21 | Named triage field vocabulary | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR labeled fields in Triage Note template |
| C-22 | Post-stage role-concern gap scan | PASS | `### ROLE CONCERN AUDIT` section in POST-STAGE AUDIT SUITE; ROLE CONCERN GAPS zero-state instructed |
| C-23 | Post-stage triage note gap scan | PASS | `### TRIAGE NOTE AUDIT` section in POST-STAGE AUDIT SUITE; TRIAGE NOTE GAPS zero-state instructed |
| C-24 | Multi-type post-stage audit suite | PASS | Three independent sections: CALIBRATION AUDIT / ROLE CONCERN AUDIT / TRIAGE NOTE AUDIT — distinct scopes |
| C-25 | Triage note field-level compliance | PASS | TRIAGE NOTE AUDIT checks three failure conditions: (a) absent section, (b) missing named field, (c) placeholder content |
| C-26 | Named audit rule with anti-patterns | PASS | RULE AUDIT-SUITE with Anti-pattern-1 (merged section) and Anti-pattern-2 (same dimension × 3); C-24 passes |
| C-27 | Gap-scan absence as format error | PASS | ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT headers carry `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` |
| C-28 | Named field-level audit schema | PASS | TRIAGE NOTE AUDIT SCHEMA declared with labeled `(a)/(b)/(c)` indices; appears as named artifact in preamble |
| C-29 | Enumerated condition zero-state | PASS | TRIAGE NOTE AUDIT RESULT block: `(a) NONE`, `(b) NONE`, `(c) NONE` — per-condition enumeration, not aggregate |
| C-30 | Preamble schema with named reference | PASS | TRIAGE NOTE AUDIT SCHEMA declared before Stage 1; TRIAGE NOTE AUDIT section says `[preamble declaration applies]` |
| C-31 | Rule citation anchors in section headers | PASS | ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT headers: `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` — compliance constraint inline |
| C-32 | Carry-forward structural artifact | PASS | Per-stage `### Carry Forward [RULE CARRY-FORWARD applies]` block with `\| From Stage \| LID \| Summary \| Inertia ID \| Action \|`; CARRY: NONE zero-state |
| C-33 | Synthesis non-audit declaration | PASS | RULE SYNTHESIS: "NOT an audit section. Does NOT count toward RULE AUDIT-SUITE." in both glossary and SYNTHESIS template |
| C-34 | Conditional item vs condition enum disambiguation | PASS | RULE CONDITIONAL-ITEM annotation: `[governs conditional verdicts — distinct from RULE CONDITION-ENUM]` with full disambiguation text |
| C-35 | Audit table additive-not-replacement | PASS | RULE AUDIT-TABLE: "Additive constraint: The table is a new layer above an existing artifact. Adding the table does NOT void RULE CONDITION-ENUM." |
| C-36 | Synthesis positive-artifact subsection schema | PASS | RULE SYNTHESIS enumerates 5 required subsections: BLOCKERS / CROSS-CUTTING THEMES SUMMARY / RESIDUAL OPEN ITEMS / DUAL-DIRECTION CHECK / INERTIA PRESSURE SUMMARY; "absence of any is VIOLATION-13" |
| C-37 | Dual illustrative baseline examples | PASS | IB-01 (Technical Displacement) and IB-02 (Organizational Adoption) — structurally distinct fields; IB-01 lacks Urgency Gradient; IB-02 adds it |
| C-38 | Carry forward inertia-ID baseline attribution column | PASS | RULE CARRY-FORWARD: "Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A"; present in CARRY FORWARD table schema |
| C-39 | IB-02 urgency gradient cascade constraint | PASS | RULE IB-URGENCY-CASCADE with 3 declared cascade constraints: Go/No-Go MUST cite IB-02; Risk Register MUST include delay-compounding entry; Inertia Pressure Summary MUST name compounding path |

*Note on C-39 in V-01/V-04/V-05*: RULE IB-REVISION integration adds the revision-triggered cascade path ("declared initially or revised per RULE IB-REVISION") to RULE IB-URGENCY-CASCADE. C-39 was already PASS before this enhancement; the addition enriches the cascade declaration but does not change the pass verdict.

#### C-40 to C-48 — Carried Criteria + New v16 Criteria

| ID | Criterion | All V-01–V-05 | Evidence note |
|----|-----------|---------------|---------------|
| C-40 | Named rule glossary exclusivity declaration | PASS | "This glossary is the **exclusive locus** for named format rule declarations... Named-rule requirements **cannot be satisfied by inline rule declarations** in stage templates or section bodies." |
| C-41 | RULE AUDIT-TABLE named anti-pattern | PASS | RULE AUDIT-TABLE: "Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's per-condition enumeration" — labeled, cites voided criterion |
| C-42 | Glossary exclusivity named-criterion enumeration | PASS | "The 2 protected criteria are: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference)... and **C-34** (Conditional Item vs Condition Enum Disambiguation)" — two criteria named by label |
| C-43 | Criterion enumeration label-plus-description pairing | PASS | Both C-30 and C-34 enumerated as label+parenthetical description pairs; substantive descriptions present |
| C-44 | AUDIT RESULT block independence declaration | PASS | RULE AUDIT-INDEPENDENCE condition (2): "When AUDIT TABLE is absent: AUDIT RESULT block... is still required. Mandatory status is not derived from RULE AUDIT-TABLE." — satisfies "or equivalent" path |
| C-45 | Exclusivity declaration protected-count annotation | PASS | "**Exactly 2 criteria require glossary scope** — any addition of a third glossary-scope criterion requires an explicit count update." Count-fixing language present; count matches enumeration |
| C-46 | RULE AUDIT-TABLE bidirectional condition enumeration | PASS | RULE AUDIT-INDEPENDENCE: two enumerated branches — (1) when AUDIT TABLE is present: AUDIT RESULT preserved beneath; (2) when AUDIT TABLE is absent: AUDIT RESULT still required — satisfies via factored path |
| C-47 | RULE AUDIT-INDEPENDENCE named-rule decomposition | PASS | RULE AUDIT-TABLE retains only ordering constraint and anti-pattern; RULE AUDIT-INDEPENDENCE is structurally separate and owns the independence declaration; non-overlapping scopes |
| C-48 | RULE AUDIT-INDEPENDENCE escalation-boundary annotation | PASS | RULE AUDIT-INDEPENDENCE Rule field: "A single 'mandatory regardless of table presence' clause satisfies C-44 but not C-46 — only explicit enumeration of both branches as separate numbered items satisfies C-46. C-44 is the single-clause form; C-46 is the two-branch enumerated form." — all three elements present |

**C-45 invariant check (V-02/V-04/V-05)**: Adding RULE BLOCKER-PROTOCOL, RULE IB-REVISION, or RULE STAGE-HANDOFF to the glossary does not create new criteria that "require glossary scope" in the rubric sense. The count of 2 refers to rubric criteria whose satisfaction requires glossary-level declaration (C-30 and C-34). No new rubric criterion imposes that constraint on these new rules. "Exactly 2" remains accurate. C-45 PASS in all variations.

---

#### Persistent Gap Criterion — All Variations

| Hypothesis | New Rule | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| H-A | RULE IB-REVISION | Present | Absent | Absent | Present | Present |
| H-B | RULE BLOCKER-PROTOCOL | Absent | Present | Absent | Present | Present |
| H-C | RULE STAGE-HANDOFF | Absent | Absent | Present | Absent | Present |

**Gap criterion verdict — all variations: FAIL (persistent)**

Cross-checking against all 40 aspirational criteria: RULE IB-REVISION, RULE BLOCKER-PROTOCOL, and RULE STAGE-HANDOFF do not map to any current rubric criterion. No existing criterion requires:
- A named rule for in-run baseline revision (RULE IB-REVISION)
- A named rule for blocker protocol at the glossary tier (RULE BLOCKER-PROTOCOL)
- A structural EXIT-to-ENTRY chain binding rule (RULE STAGE-HANDOFF)

The persistent gap lies outside H-A, H-B, and H-C.

---

## Composite Scores

| Variation | Essential + Recommended | Aspirational (39/40 × 5) | Total |
|-----------|------------------------|--------------------------|-------|
| V-01 | 90 | 195 | **285/290** |
| V-02 | 90 | 195 | **285/290** |
| V-03 | 90 | 195 | **285/290** |
| V-04 | 90 | 195 | **285/290** |
| V-05 | 90 | 195 | **285/290** |

**All variations tie at 285/290.** No variation resolves the persistent gap.

---

## Ranking

All five variations rank equally at 285/290. V-05 carries the most architectural content (all three new rules, VIOLATION-14 + VIOLATION-15, full cascade integration) and provides the strongest diagnostic: if V-05 = 285, the gap is definitively outside all three hypotheses.

**Diagnostic conclusion**: H-A (RULE IB-REVISION), H-B (RULE BLOCKER-PROTOCOL), and H-C (RULE STAGE-HANDOFF) are all eliminated as sources of the persistent gap. R17 must probe a different space.

**Candidate R17 hypotheses** (outside current probe space):
- Named anti-pattern on RULE PHASE-GATE (parallel to C-41 applied to phase gate generic language)
- Named anti-pattern on RULE FINDING-LEDGER (parallel to C-41 applied to the ledger initialization requirement)
- Named anti-pattern on RULE INERTIA-BASELINE (parallel to C-26/C-41 applied to baseline-without-concern raising)
- VIOLATION TAXONOMY structural declaration (annotated taxonomy vs. bare list)
- RULE ZERO-STATE expanded with schema for zero-state confirmation protocols

---

## Excellence Signals

No variation improved the score over the R16 base. No new excellence signals are extractable from score-differential analysis.

**Structural observations from V-05** (most complete variation, diagnostic saturation point):
1. The three new rules (RULE IB-REVISION / RULE BLOCKER-PROTOCOL / RULE STAGE-HANDOFF) integrate cleanly without breaking any existing criterion — the glossary accommodates additional named rules without invalidating C-45's count or C-40's exclusivity logic.
2. RULE BLOCKER-PROTOCOL's promotion from inline section to named rule parallels the structural elevation pattern seen in C-26 (RULE AUDIT-SUITE) and C-41 (RULE AUDIT-TABLE anti-pattern) — this pattern is architecturally sound even if it doesn't resolve the current gap.
3. RULE STAGE-HANDOFF's EXIT-to-ENTRY chain binding is a novel structural constraint class not represented elsewhere in the rubric — it may be relevant when a future criterion targets stage-boundary formalism rather than cross-stage content.

---

```json
{"top_score": 285, "all_essential_pass": true, "new_patterns": []}
```
