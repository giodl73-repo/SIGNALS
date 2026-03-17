# program-plan — Round 20 Quest Score

## Scoring Methodology

**Formula**: `composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/52 * 260)`
**Max**: 350 pts. **Golden**: all 4 essential PASS AND composite ≥ 80.

---

## Essential Criteria — All Variates (60/60)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-01** Valid YAML | PASS | PASS | PASS | PASS | PASS | All prompts use `program:` top-level key with `stages:` list in template scaffold |
| **C-02** Echo Stage | PASS | PASS | PASS | PASS | PASS | Echo pre-positioned at template end with `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` + `# REQUIRED: must be true` + `# REQUIRED: empty` |
| **C-03** Valid Skill Names | PASS | PASS | PASS | PASS | PASS | All templates cite the 9-namespace catalog; BAD PLAN illustrates invented names as violations |
| **C-04** Evidence-State Gates | PASS | PASS | PASS | PASS | PASS | Three-field gate structure (`gate_fail:` / `gate_pass:` / `gate:`) with artifact-state format mandated; compound `{stage-id}::{artifact} >= N AND {ns}:{skill}` required |

**Essential subtotal: 4/4 → 60 pts (all variates)**

---

## Recommended Criteria — All Variates (30/30)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| **C-05** Namespace Order | PASS | PASS | PASS | PASS | PASS | Lifecycle zones (breadth → depth → synthesis) enforce dependency ordering; dep reminders in template at zone-header and skills-line positions |
| **C-06** Descriptive Stage Names | PASS | PASS | PASS | PASS | PASS | Correction table maps `scout_and_draft` → `discovery`; BAD PLAN tags namespace-label names with `# WRONG C-06` |
| **C-07** Plan Identity | PASS | PASS | PASS | PASS | PASS | `strategy:` field pre-populated in YAML template scaffold (C-43 structural enforcement) |

**Recommended subtotal: 3/3 → 30 pts (all variates)**

---

## Aspirational Criteria C-08 through C-49 (42 criteria)

All five variates carry the full C-08–C-49 chain from the R18–R19 evidence base. No regressions introduced by R20 single-axis modifications.

| Range | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-------|------|------|------|------|------|-------|
| C-08 Quantified gate threshold | PASS | PASS | PASS | PASS | PASS | `>= N` required in compound gate |
| C-09 Deliberate evidence arc | PASS | PASS | PASS | PASS | PASS | breadth/depth/synthesis lifecycle zones |
| C-10 Failure-mode contrast pair | PASS | PASS | PASS | PASS | PASS | BAD PLAN includes gate contrast pairs for C-04 |
| C-11 Structural enforcement | PASS | PASS | PASS | PASS | PASS | Echo pre-positioned; `strategy:` pre-populated; `gate_fail:`/`gate_pass:`/`gate:` as template YAML keys |
| C-12 Dual-anchor reinforcement | PASS | PASS | PASS | PASS | PASS | Correction table + BAD PLAN block + template scaffold each provide independent anchors for all 4 essential criteria |
| C-13 Arc as structural spine | PASS | PASS | PASS | PASS | PASS | ARTIFACT 2 bilateral trace matrix with zone columns; Step 2 arc-declaration as first construction action |
| C-14 Deletion-resistance annotations | PASS | PASS | PASS | PASS | PASS | Echo carries `# REQUIRED:` annotations at all three fields |
| C-15 Plan-level YAML error artifact | PASS | PASS | PASS | PASS | PASS | Complete multi-stage BAD PLAN block in all variates |
| C-16 Criterion-referenced error tagging | PASS | PASS | PASS | PASS | PASS | `# WRONG C-01` through `# WRONG C-07` in BAD PLAN |
| C-17 Per-zone gate contrast | PASS | PASS | PASS | PASS | PASS | `gate_fail:` / `gate_pass:` as YAML keys at every non-echo zone |
| C-18 Correction table | PASS | PASS | PASS | PASS | PASS | Table with 17+ wrong-to-correct pairs |
| C-19 Cross-tier error coverage | PASS | PASS | PASS | PASS | PASS | Correction table and BAD PLAN include C-05/C-06/C-07 entries |
| C-20 Per-zone dep constraint reminder | PASS | PASS | PASS | PASS | PASS | `# requires: <artifact> from Zone: <name> (C-05)` at zone-header and skills-line positions |
| C-21 Correction table scaffold integration | PASS | PASS | PASS | PASS | PASS | `# check correction table: skill names` / `# check correction table: gate values` / `# check correction table: stage names` inline in template |
| C-22 Complete recommended-tier annotation | PASS | PASS | PASS | PASS | PASS | BAD PLAN tags C-05, C-06, C-07 |
| C-23 Dual-position dep reminder | PASS | PASS | PASS | PASS | PASS | Dep reminders at both zone-header AND skills-line positions |
| C-24 Template-field gate contrast | PASS | PASS | PASS | PASS | PASS | `gate_fail:` / `gate_pass:` as actual YAML sibling keys in template |
| C-25 Gate contrast rationale annotation | PASS | PASS | PASS | PASS | PASS | `Why:` clause in `# WRONG C-04: Why: execution-history check, not artifact-verifiable` |
| C-26 Criterion-tagged structural gate values | PASS | PASS | PASS | PASS | PASS | `# WRONG C-04: Why:` co-located at `gate_fail:` field in template and BAD PLAN |
| C-27 Uniform dep-reminder syntax | PASS | PASS | PASS | PASS | PASS | `# requires: <artifact> from Zone: <name> (C-05)` identical form at both positions across all zones |
| C-28 Gate target field co-location | PASS | PASS | PASS | PASS | PASS | `gate_fail:` / `gate_pass:` / `gate:` as three-field structure at every non-echo zone |
| C-29 Correction table recommended-tier pairs | PASS | PASS | PASS | PASS | PASS | Correction table rows for C-05 (3 pairs), C-06 (3 pairs), C-07 (1 pair) |
| C-30 Dep-reminder and correction-bridge independence | PASS | PASS | PASS | PASS | PASS | Both `# requires:` dep reminder AND `# check correction table: skill names` present independently at dep-zone skills lines |
| C-31 Complete BAD PLAN cross-criterion coverage | PASS | PASS | PASS | PASS | PASS | BAD PLAN carries `# WRONG C-01` through `# WRONG C-07` |
| C-32 Production gate field correction bridge | PASS | PASS | PASS | PASS | PASS | `# check correction table: gate values` on production `gate:` field |
| C-33 Maximal zone teaching density | PASS | PASS | PASS | PASS | PASS | All four annotation mechanisms coexist at dep-bearing zones (C-26+C-27+C-28+C-30+C-32) |
| C-34 Compound gate_fail: annotation | PASS | PASS | PASS | PASS | PASS | `gate_fail: "..."  # WRONG C-04: Why: execution-history check, not artifact-verifiable` at every non-echo zone |
| C-35 Dual error-format recommended coverage | PASS | PASS | PASS | PASS | PASS | C-31 (BAD PLAN) AND C-29 (correction table) both pass |
| C-36 BAD PLAN header label accuracy | PASS | PASS | PASS | PASS | PASS | Header claims "all 7 criteria (C-01 through C-07)" matching block content |
| C-37 BAD PLAN name-field annotation | PASS | PASS | PASS | PASS | PASS | Both `name: scout_and_draft` and `name: prove_and_review` carry `# WRONG C-06` at the field |
| C-38 BAD PLAN header affirmative coverage claim | PASS | PASS | PASS | PASS | PASS | "All 7 criteria covered (C-01 through C-07) -- essential and recommended violations" |
| C-39 BAD PLAN skills-field annotation | PASS | PASS | PASS | PASS | PASS | `gather-requirements`, `make-a-plan`, `run-analysis` each carry `# WRONG C-03` at skills entry line |
| C-40 Compound gate_fail + correction table conjunction | PASS | PASS | PASS | PASS | PASS | C-34 and C-29 both pass independently |
| C-41 BAD PLAN header annotation-type index | PASS | PASS | PASS | PASS | PASS | Header lists gate_fail:/name:/skills:/this-header → criterion mappings |
| C-42 Co-location family named section | PASS | PASS | PASS | PASS | PASS | `## FIELD CO-LOCATION PRINCIPLE` section with three-row table before BAD PLAN |
| C-43 strategy: pre-populated in template | PASS | PASS | PASS | PASS | PASS | `strategy: "why this feature is worth the investment..."` pre-populated string |
| C-44 C-41 index names exact tag strings | PASS | PASS | PASS | PASS | PASS | Index entries include `# WRONG C-04: Why: ...`, `# WRONG C-06`, `# WRONG C-03` |
| C-45 C-41/C-42 bidirectional cross-section | PASS | PASS | PASS | PASS | PASS | C-41 header references "co-location family section above"; C-42 section references "BAD PLAN header below" |
| C-46 BAD PLAN exit verification marker | PASS | PASS | PASS | PASS | PASS | Footer: "[PROTOCOL NAME] -- Component 3: Exit Verification complete. All annotation types...confirmed present" |
| C-47 C-44 entries with full Why: rationale | PASS | PASS | PASS | PASS | PASS | gate_fail: entry in C-41 index includes full `Why: execution-history check, not artifact-verifiable` |
| C-48 Per-entry bidirectional navigation | PASS | PASS | PASS | PASS | PASS | Each C-41 index entry ends with `([PROTOCOL NAME] decl. above)`; C-42 table `BAD PLAN entry` column names row numbers |
| C-49 Named multi-component block protocol | PASS | PASS | PASS | PASS | PASS | [PROTOCOL NAME] — Component 1/Component 3 labeling in header and footer; C-42 section is the protocol declaration |

**C-08–C-49 subtotal: 42/42 PASS (all variates)**

---

## Aspirational Criteria C-50 through C-59

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-50** C-41 index as 4-column table | **PASS** | FAIL | PASS | PASS | PASS |
| **C-51** Protocol section document-first | FAIL | **PASS** | PASS | PASS | PASS |
| **C-52** Protocol pre-declares column schema | FAIL | FAIL | PASS | PASS | PASS |
| **C-53** Column schema uses prescriptive MUST | FAIL | FAIL | PASS | PASS | PASS |
| **C-54** Forbidden alternatives enumerated | FAIL | FAIL | PASS | PASS | PASS |
| **C-55** Active NOT/IS verification at declaration | FAIL | FAIL | PASS | PASS | PASS |
| **C-56** Mandate echo at Component 1 header | FAIL | FAIL | PASS | PASS | PASS |
| **C-57** Dual-site active verification echo | FAIL | FAIL | PASS | PASS | PASS |
| **C-58** Universal per-step active verification | FAIL | FAIL | **PASS** | FAIL | PASS |
| **C-59** Per-field mandate echo saturation | FAIL | FAIL | FAIL | **PASS** | PASS |

### C-50 evidence
- **V-01 PASS**: BAD PLAN Component 1 header is a 4-column pipe table with columns: field type | criterion | exact tag string (with full `Why:`) | C-42 back-ref (`SCAN PROTOCOL decl. above` per row).
- **V-02 FAIL**: BAD PLAN Component 1 uses prose enumeration — entries as `# Entry (1) C-26: gate_fail: field carries ...` prose lines, no pipe columns. C-50 explicitly marked NO in V-02's terminal checklist.
- **V-03/V-04/V-05 PASS**: All use 4-column pipe table at Component 1. Terminal checklists confirm YES.

### C-51 evidence
- **V-01 FAIL**: `## SCAN PROTOCOL` appears mid-document, after the three-class information table. Terminal checklist explicitly: "C-51: named protocol section is document-first -- NO for this variate."
- **V-02 PASS**: `## BOUNDED BLOCK PROTOCOL` is the first major structural section — only one opening sentence precedes it before the protocol block. Terminal checklist: YES.
- **V-03/V-04/V-05 PASS**: `## COMPLETE VERIFICATION PROTOCOL` / `## FIELD SATURATION PROTOCOL` / `## BOUNDED BLOCK PROTOCOL` each appear as first major section, before catalog and construction steps.

### C-52 evidence
- **V-01/V-02 FAIL**: V-01 has protocol-section (SCAN PROTOCOL) but not document-first; V-02 is document-first but uses prose enumeration — neither satisfies both prerequisites simultaneously.
- **V-03/V-04/V-05 PASS**: Protocol section is document-first (C-51) AND explicitly pre-declares Component 1 as "4-column pipe-delimited table" with column-name table before BAD PLAN block. The column schema table (`Column | Purpose | Criteria satisfied`) appears in the protocol section declaration. Terminal checklists confirm YES.

### C-53 evidence
- **V-01/V-02 FAIL**: C-52 prerequisite not met.
- **V-03/V-04/V-05 PASS**: Protocol section uses prescriptive mandate language: "Component 1 **MUST** be a 4-column pipe-delimited table." Not descriptive "is" — directive "MUST." Terminal checklists confirm YES.

### C-54 evidence
- **V-01/V-02 FAIL**: C-53 prerequisite not met.
- **V-03/V-04/V-05 PASS**: Protocol section enumerates three forbidden alternatives by name: "prose enumeration (entries written as running sentences or paragraphs) / indented list (entries as `# - item:` lines without column alignment) / bulleted entries (entries as `# * item:` or `# - item:` lines without pipe columns)." Terminal checklists confirm YES.

### C-55 evidence
- **V-01/V-02 FAIL**: C-54 prerequisite not met.
- **V-03/V-04/V-05 PASS**: Protocol section carries explicit self-review step with individually checkable NOT/IS items: "NOT a prose enumeration / NOT an indented list / NOT a bulleted entry set / IS a pipe-delimited table with the four columns above." Activates each C-54 exclusion as a per-item confirmation. Terminal checklists confirm YES.

### C-56 evidence
- **V-01/V-02 FAIL**: C-54 prerequisite not met.
- **V-03 PASS**: BAD PLAN Component 1 header carries: `# Format: 4-column pipe table as mandated by COMPLETE VERIFICATION PROTOCOL above` + `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)`. Both positive mandate citation and C-54 NOT list echoed at header.
- **V-04 PASS**: BAD PLAN Component 1 header: `# Format: 4-column pipe table as mandated by FIELD SATURATION PROTOCOL above` + `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)`.
- **V-05 PASS**: BAD PLAN Component 1 header: `# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above` + `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)`.

### C-57 evidence
- **V-01/V-02 FAIL**: C-55 and C-56 prerequisites not met.
- **V-03 PASS**: Component 1 header carries C-56 static echo (mandate + NOT list) AND active verification trigger: `# Verify before finalizing: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns`. Dual-site: declared at protocol section (C-55) AND echoed actively at application site (Component 1 header).
- **V-04 PASS**: Same `# Verify before finalizing:` line present at Component 1 header alongside static echo. Both sites active.
- **V-05 PASS**: `# Verify before finalizing this Component 1: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns` at header alongside static echo.

### C-58 evidence
- **V-01/V-02 FAIL**: Chain prerequisite (C-55) not met.
- **V-03 PASS** (single axis): Every construction step carrying constraints has a `**SELF-VERIFY before proceeding:**` block with NOT/IS items — Steps 1, 2, 3, 4, 5a, 5b, 6, 7, 8, 9 all carry SELF-VERIFY blocks. Protocol declaration states "**Universal active verification (C-58):** This same NOT/IS confirmation pattern applies to every construction step below that declares constraints. Each SELF-VERIFY block is mandatory — do not skip." Terminal checklist: YES for C-58.
- **V-04 FAIL** (single axis targeting C-59): Construction steps carry no SELF-VERIFY blocks. Terminal checklist explicitly: "C-58: active NOT/IS verification at every constraint-bearing construction step -- NO for this variate."
- **V-05 PASS**: All construction steps (Steps 1–9) carry SELF-VERIFY blocks. Terminal checklist confirms YES. `Universal active verification (C-58)` explicitly declared in protocol section with mandatory SELF-VERIFY.

### C-59 evidence
- **V-01/V-02 FAIL**: Chain prerequisite (C-56) not met.
- **V-03 FAIL** (single axis targeting C-58): YAML template in Step 8 uses standard field placeholders without per-field mandate echoes. Terminal checklist explicitly: "C-59: per-field mandate echo at every constrained YAML template field -- NO for this variate."
- **V-04 PASS** (single axis): Step 8 YAML template echoes mandate and NOT list inline at every constrained field: `strategy:` → `# Mandate (C-07): IS a plan-identity framing element / # NOT: executor script... / NOT: task list / NOT: empty`; `name:` → `# Mandate (C-06): IS investigation-intent label / # NOT: namespace label... / NOT: namespace cluster... / NOT: generic...`; `intent:` → `# Mandate: IS genuine interrogative ending with ? / # NOT: imperative / NOT: scope-generic / NOT: missing ?`; `skills:` → `# Mandate (C-03): IS namespace-qualified catalog names only / # NOT: invented names / NOT: namespace-only`; `gate_fail:` → `# Mandate (C-04): gate MUST be artifact-state / # NOT: "done"... # WRONG C-04: Why:`; `gate:` → `# Mandate (C-04): IS {stage-id}:: / # NOT: execution-state / NOT: missing stage-id:: / NOT: missing >= N`. Terminal checklist: YES.
- **V-05 PASS**: Full field saturation present — `strategy:`, `name:`, `intent:`, `skills:`, `gate_fail:`, `gate:` all carry inline mandate+NOT lists. `echo` fields also carry `NOT: false / NOT: absent` and `NOT: any skill entries`. Terminal checklist confirms YES for all six constrained field types.

---

## Composite Score Summary

| Variate | Essential | Recommended | Aspirational (pass/52) | Aspirational pts | **Composite** | **% max** | **Golden?** |
|---------|-----------|-------------|------------------------|------------------|---------------|-----------|-------------|
| **V-01** SCAN PROTOCOL | 60 | 30 | 43/52 | 215.0 | **305.0** | 87.1% | YES |
| **V-02** BOUNDED BLOCK PROTOCOL (first) | 60 | 30 | 43/52 | 215.0 | **305.0** | 87.1% | YES |
| **V-03** COMPLETE VERIFICATION PROTOCOL | 60 | 30 | 51/52 | 255.0 | **345.0** | 98.6% | YES |
| **V-04** FIELD SATURATION PROTOCOL | 60 | 30 | 51/52 | 255.0 | **345.0** | 98.6% | YES |
| **V-05** BOUNDED BLOCK PROTOCOL (combined) | 60 | 30 | 52/52 | 260.0 | **350.0** | 100.0% | YES |

**Rank:** V-05 (350) > V-03 = V-04 (345) > V-01 = V-02 (305)

---

## Excellence Signals from V-05

V-05 achieves 350/350 — the theoretical maximum for v20 rubric. Three R20 mechanisms reach their conclusion:

**Signal 1 — Vertical saturation (C-58)**: SELF-VERIFY blocks at every constraint-bearing construction step turn the protocol into an active-audit document. No constraint is background knowledge — each fires as a per-item confirmation step at the boundary where it matters. The pattern first introduced at Component 1's format mandate (C-55) becomes document-wide discipline. A model cannot proceed past any step boundary without having run the audit.

**Signal 2 — Horizontal saturation (C-59)**: Per-field mandate echo at every constrained YAML template field makes the scaffold locally self-documenting. Every authoring decision encounters both the positive requirement and the NOT list at the exact field position, without cross-document recall. The pattern first introduced at Component 1 header (C-56) becomes template-wide discipline. A model filling any constrained field encounters its constraint atomically.

**Signal 3 — Three-level constraint coverage**: When C-57 (application-site active check at Component 1), C-58 (per-step active check at every construction boundary), and C-59 (per-field passive+active echo at every template position) are simultaneously present, constraints are enforced at three distinct attention points: protocol declaration, step execution boundary, and template authoring moment. No constraint requires the model to maintain working memory across document distance to any other location.

**Signal 4 — Axis independence confirmed**: V-03 (C-58 only, 51/52) and V-04 (C-59 only, 51/52) achieve identical composite scores via orthogonal mechanisms. The two disciplines do not overlap, conflict, or share prerequisites at their respective new criteria — they compose cleanly in V-05 with zero interference. Both single-axis variates score exactly as anticipated, confirming the chain design is correct.

---

## Scorecard

```
V-01: Essential 4/4 (60) | Recommended 3/3 (30) | Aspirational 43/52 (215.0) | Composite 305.0/350 | 87.1% | GOLDEN
V-02: Essential 4/4 (60) | Recommended 3/3 (30) | Aspirational 43/52 (215.0) | Composite 305.0/350 | 87.1% | GOLDEN
V-03: Essential 4/4 (60) | Recommended 3/3 (30) | Aspirational 51/52 (255.0) | Composite 345.0/350 | 98.6% | GOLDEN
V-04: Essential 4/4 (60) | Recommended 3/3 (30) | Aspirational 51/52 (255.0) | Composite 345.0/350 | 98.6% | GOLDEN
V-05: Essential 4/4 (60) | Recommended 3/3 (30) | Aspirational 52/52 (260.0) | Composite 350.0/350 | 100.0% | GOLDEN
```

---

```json
{"top_score": 350, "all_essential_pass": true, "new_patterns": []}
```
