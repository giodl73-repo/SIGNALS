---

## signal-check Round 19 Scorecard

**All five variations: 100.00 composite (41/41 aspirational, 5/5 essential)**

| Var | Axis | Asp. | Composite | Rank |
|-----|------|------|-----------|------|
| V-01 | D (structured pattern block) | 41/41 | 100.00 | T-1 |
| V-02 | E (severity-ordered guide) | 41/41 | 100.00 | T-1 |
| V-03 | F (5-state STATUS) | 41/41 | 100.00 | T-1 |
| V-04 | D+E | 41/41 | 100.00 | T-1 |
| V-05 | D+E+F + live axis | 41/41 | 100.00 | **T-1 (excellence leader)** |

---

### Why all five tie at 100.00

All five share the complete R18 V-05 baseline, which already achieves the C-46 ceiling on STANDING RULES, section-function annotations (C-48), dimensional-status preamble (C-47), and triple-vector saturation (C-49). The R19 axes target three untouched sections — CROSS-ITEM PATTERNS (Axis D), MISSING SIGNAL GUIDE (Axis E), and STATUS vocabulary (Axis F) — none of which map to any existing C-09 through C-49 criterion. No scoring differential is possible under v18.

---

### Excellence signals (V-05, C-50 candidate)

V-05 introduces the live R19 axis: a `Dims` column in the artifact inventory table annotating each artifact with its covered check dimensions (C/Sq/St/Co). This creates four structural advances not present in V-01 through V-04:

1. **Inventory pre-analysis coverage scan** — per-dimension coverage visible before entering any preflight item; a missing dimension abbreviation predicts OPEN without reading analysis
2. **Per-item Dims prediction** — each preflight item opens with a prediction derived from the Dims column, creating a feedback loop between inventory and analysis
3. **Dims-driven Thin Coverage pattern** — cross-item gap detectable from inventory structure alone, before STATUS analysis
4. **`dims_coverage` frontmatter** — per-dimension artifact counts propagate into machine-readable metadata

**C-50 boundary confirmed clean**: V-01 through V-04 all use 5-column tables and fail C-50. No combination of axes D+E+F implies C-50.

---

### v19 rubric extraction

Four candidates: **C-50** (Dims column, confirmed), **C-51** (labeled pattern block), **C-52** (severity-ordered guide), **C-53** (5-state STATUS). Aspirational denominator will grow from 41 to 42–45 depending on which are extracted.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["inventory pre-analysis coverage scan via Dims column makes per-dimension artifact coverage visible before entering any preflight item", "per-item Dims prediction ties expected STATUS to inventory column count before reading artifact content creating structural feedback loop", "Dims-driven Thin Coverage cross-item pattern detects multi-dimension thin-coverage from inventory structure without requiring per-item STATUS analysis", "dims_coverage frontmatter propagates per-dimension artifact counts into machine-readable metadata"]}
```
ister carried through preflight items, readiness summary, and guide sections.

---

### Recommended (C-06 to C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Readiness summary section present | PASS | PASS | PASS | PASS | PASS |
| C-07 | CROSS-ITEM PATTERNS section present | PASS | PASS | PASS | PASS | PASS |
| C-08 | MISSING SIGNAL GUIDE section present | PASS | PASS | PASS | PASS | PASS |

---

### Aspirational (C-09 to C-49) -- all five PASS all 41

#### C-09 to C-16: Core structure

| ID | Criterion summary | All five |
|----|-------------------|----------|
| C-09 | Named STANDING RULES block present | PASS |
| C-10 | STANDING RULES contains Rule 1 and Rule 2 | PASS |
| C-11 | Readiness summary uses pilot-briefing language | PASS |
| C-12 | Four dimensions structured with consistent labeling | PASS |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type | PASS |
| C-14 | STANDING RULES block precedes all inventory and analysis | PASS |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS |
| C-16 | Every constraint explicitly enumerates all output locations it governs | PASS |

Evidence: All five carry full STANDING RULES block with Rule 1, Rule 2, Rule 3, each with Applies-to declarations. Scan index table lists all four required verbatim absence phrases. Per-dimension blocks embed required absence phrases at point of use.

#### C-17 to C-19: Advisory register and enforcement stack

| ID | Criterion summary | All five |
|----|-------------------|----------|
| C-17 | Verbatim absence phrases embedded at point of use | PASS |
| C-18 | Advisory register carried structurally through framing vocabulary | PASS |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | PASS |

Evidence:
- C-17: Each dimension block contains "Required verbatim absence phrase for this item:" with exact required text.
- C-18: Pilot-briefing language, coaching register, "team decides" framing embedded in section headings and status fields.
- C-19: ENFORCEMENT STACK NOTE: "Rules 1, 2, and 3 form a coordinated enforcement stack... No layer substitutes for another... All three must pass for the output to be a valid health report."

#### C-20 to C-32: Meta-rule and activation gate chain

| ID | Criterion summary | All five |
|----|-------------------|----------|
| C-20 | Location-enumeration requirement as named meta-rule | PASS |
| C-21 | Each rule assigned a named failure class | PASS |
| C-22 | Meta-rule includes temporal activation gate | PASS |
| C-23 | Meta-rule self-application declared in rule body | PASS |
| C-24 | Activation gate framed as rule-validity condition | PASS |
| C-25 | Body self-application includes proximate scope pointer | PASS |
| C-26 | Activation gate carries both obligation and validity framing | PASS |
| C-27 | Validity condition uses rule-existence framing | PASS |
| C-28 | Rule name encodes existence assertion | PASS |
| C-29 | Dual register expressed as labeled sections with non-substitutability | PASS |
| C-30 | Step-up disclaimer before existence framing | PASS |
| C-31 | Temporal gate expressed as "at rule-creation time" | PASS |
| C-32 | Location annotation covers rules not yet written | PASS |

Evidence (identical across all five):
- C-28: "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" in rule heading
- C-26/C-29: "Obligation: ... Existence condition: ..." labeled sections
- C-30: "Not operative understates the condition"
- C-31: "Scope must be discharged at rule-creation time, not retroactively"
- C-32: "any rule added in the future"
- C-23/C-25: "This requirement self-applies: Rule 3 itself declares its scope below"
- C-24/C-27: "does not exist as an active rule"

#### C-33 to C-46: Reader position and consulting directory chain

| ID | Criterion summary | All five |
|----|-------------------|----------|
| C-33 | Non-substitutability assigns distinct function to each register | PASS |
| C-34 | Each rule heading encodes failure class | PASS |
| C-35 | Failure class in top-level rule heading | PASS |
| C-36 | Reader-position named explicitly in function framing | PASS |
| C-37 | ENFORCEMENT STACK NOTE collapses to forward-references | PASS |
| C-38 | Each rule names its own reader position | PASS |
| C-39 | NOTE reduced to pure interdependency statement | PASS |
| C-40 | Per-rule reader positions surfaced as consulting directory | PASS |
| C-41 | NOTE attributes failure-mode ownership to top-level headings | PASS |
| C-42 | Consulting directory carries completeness assertion | PASS |
| C-43 | Completeness assertion uses all-roles claim form | PASS |
| C-44 | All-roles claim includes embedded count qualifier | PASS |
| C-45 | NOTE attribution extended with parenthetical heading index | PASS |
| C-46 | Dual count consistency between count qualifier and heading index | PASS |

Evidence (identical across all five):
- C-33/C-36: "the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost"
- C-34/C-35: "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:", "Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:", "Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:"
- C-37: NOTE reads "failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" -- forward-reference only, no "prevents..." prose
- C-38: Rule 1 names "A committing engineer checking for missing absence declarations"; Rule 2 names "A skill-reference consumer disambiguating a reference"
- C-39: NOTE contains only interdependency statement; no "Rule 1 prevents X" prose
- C-40/C-42/C-43/C-44: "All 3 reader roles for this block are listed above." -- all-roles claim with embedded count
- C-41/C-45: "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" heading index in NOTE
- C-46: Count = 3 in all-roles claim; entries = 3 in heading index; numerically consistent

#### C-47 to C-49: Triple-vector advisory register (R18 criteria)

| ID | Criterion summary | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-------------------|------|------|------|------|------|
| C-47 | READINESS SUMMARY includes dimensional-status preamble | PASS | PASS | PASS | PASS | PASS |
| C-48 | Every section header carries section-function annotation | PASS | PASS | PASS | PASS | PASS |
| C-49 | Triple-vector advisory register saturation | PASS | PASS | PASS | PASS | PASS |

Evidence:
- C-47: All five READINESS SUMMARY sections open with structured STATUS block (CAUSAL GAP: [...] / SEQUENCE: [...] / STALENESS: [...] / COHERENCE: [...]) before pilot-briefing prose. V-03/V-05 use 5-state placeholders; V-01/V-02/V-04 use 3-state. Both forms satisfy C-47.
- C-48: All seven section headers in all five variations carry bracketed [FUNCTION:...] or inline annotations naming knowledge type and reader purpose.
- C-49: C-18 PASS + C-47 PASS + C-48 PASS for all five; co-presence confirmed at three independent structural levels.

---

## R19 Axis Differences (scoring-neutral; extraction context)

These differences are not captured by any C-09 through C-49 criterion. They constitute the R19 candidate pool for v19 extraction.

| Axis | What changed | Variations |
|------|-------------|------------|
| D | CROSS-ITEM PATTERNS uses labeled block (Pattern / Items implicated / Root cause / Single action) instead of prose; null form is also a labeled block; pattern components recoverable from format scan without reading prose | V-01, V-04, V-05 |
| E | MISSING SIGNAL GUIDE opens with explicit ordering declaration; OPEN before FLAG; CAUSAL GAP before SEQUENCE before STALENESS before COHERENCE within tier; ordering invariant | V-02, V-04, V-05 |
| F | STATUS uses 5-state vocabulary (OK-STRONG / OK-WEAK / FLAG / OPEN); per-dimension OK-STRONG/OK-WEAK criteria defined inline within each preflight item; epistemic confidence visible from status line without reading Basis | V-03, V-05 |
| Live (C-50) | Inventory includes 6th column `Dims` (C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE); pre-analysis coverage scan; per-item Dims prediction; Thin Coverage pattern; `dims_coverage` frontmatter | V-05 only |

**C-50 boundary confirmation:**

| Var | Axes | Dims column | C-50 |
|-----|------|-------------|------|
| V-01 | D | Absent (5-col table) | FAIL |
| V-02 | E | Absent (5-col table) | FAIL |
| V-03 | F | Absent (5-col table) | FAIL |
| V-04 | D+E | Absent (5-col table) | FAIL |
| V-05 | D+E+F+live | Present (6-col, Dims annotated) | PASS |

Boundary confirmed clean. C-50 independently testable from axes D, E, F; independently testable from C-47, C-48, C-49. No combination of D+E+F implies C-50.

---

## Aspirational Pass Counts

| Var | Asp. pass | Composite |
|-----|-----------|-----------|
| V-01 | 41/41 | 100.00 |
| V-02 | 41/41 | 100.00 |
| V-03 | 41/41 | 100.00 |
| V-04 | 41/41 | 100.00 |
| V-05 | 41/41 | 100.00 |

---

## Excellence Signals

**Top variation**: V-05 (D+E+F + live R19 axis). All five tie at 100.00 under v18. V-05 is the excellence leader on the C-50 candidate axis.

**Pattern 1 -- Inventory pre-analysis coverage scan (C-50 candidate)**

V-05 adds a `Dims` column to the artifact inventory table annotating each artifact with the check dimensions it addresses (C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE). Before entering any preflight item, V-05 instructs a pre-analysis coverage scan: "note which dimension abbreviations appear in the Dims column and which do not. A missing abbreviation predicts OPEN; a single-row abbreviation predicts OK-WEAK at best." Per-dimension artifact coverage is visible from the inventory before any analysis section is entered. Boundary confirmed clean: V-01 through V-04 all use 5-column tables and fail C-50.

**Pattern 2 -- Per-item Dims prediction**

Each preflight item in V-05 opens with a "Dims prediction:" block tying the expected STATUS to the inventory Dims column: e.g., "Dims prediction: count rows with C in the Dims column. 0 rows predicts OPEN; 1 row predicts OK-WEAK at best; 2+ rows may support OK-STRONG if mechanism is traced." The inventory scan generates a coverage prediction that narrows per-item analysis scope. A structural feedback loop is established: inventory informs analysis, analysis confirms or corrects the Dims prediction.

**Pattern 3 -- Dims-driven cross-item pattern detection**

V-05 extends CROSS-ITEM PATTERNS with a Dims-driven detection rule: "Also scan the Dims column: if 3+ dimensions have only one artifact each, that is a 'Thin Coverage' pattern distinct from individual dimension gaps." The Thin Coverage pattern has its own labeled block form and single action. A cross-dimension gap is visible from inventory structure rather than requiring all four items to be STATUS-analyzed first.

**Pattern 4 -- Machine-readable dims_coverage frontmatter**

V-05 adds a `dims_coverage` block to the artifact frontmatter recording per-dimension artifact counts (causal_gap: N, sequence: N, staleness: N, coherence: N). The Dims column annotation propagates into machine-readable metadata, making per-dimension coverage queryable across /signal:check artifacts without reading any inventory table.

---

## v19 Rubric Extraction Candidates

| Candidate | Axis | Description |
|-----------|------|-------------|
| C-50 | Live | Artifact inventory includes a dimension-coverage column (Dims) mapping each artifact to its covered check dimensions (C/Sq/St/Co), making per-dimension artifact coverage visible from the inventory scan before any preflight item is entered; independently testable from C-47, C-48, C-49; no precondition in established chain; boundary confirmed clean (V-01 through V-04 FAIL; V-05 PASS) |
| C-51 (candidate) | D | CROSS-ITEM PATTERNS uses labeled block format (Pattern / Items implicated / Root cause / Single action); null-pattern form is also a labeled block; prose-only patterns satisfy C-07 but not C-51; pattern components recoverable from format scan without reading prose |
| C-52 (candidate) | E | MISSING SIGNAL GUIDE opens with explicit ordering declaration and orders items by severity (OPEN before FLAG) and within tier by dimension order (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE); most-blocking gap always appears first; ordering is invariant |
| C-53 (candidate) | F | STATUS uses 5-state vocabulary (OK-STRONG / OK-WEAK / FLAG / OPEN); per-dimension OK-STRONG/OK-WEAK criteria defined inline within each preflight item; epistemic confidence (single vs. multi-artifact coverage) visible from status line alone without reading Basis field |

Next rubric version: **v19**
- Aspirational denominator: 42 (C-50 only) to 45 (C-50 through C-53)
- C-50: no precondition in established chain
- C-51: requires C-07 as precondition; C-07 does not imply C-51
- C-52: requires C-08 as precondition; C-08 does not imply C-52
- C-53: requires C-02 as precondition; C-02 does not imply C-53

---

## Composite Calculation (v18)

```
composite = 90 + (aspirational_pass / 41) * 10

V-01: 90 + (41/41) * 10 = 100.00
V-02: 90 + (41/41) * 10 = 100.00
V-03: 90 + (41/41) * 10 = 100.00
V-04: 90 + (41/41) * 10 = 100.00
V-05: 90 + (41/41) * 10 = 100.00
```

All five golden (all essential pass, composite >= 80).

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["inventory pre-analysis coverage scan via Dims column makes per-dimension artifact coverage visible before entering any preflight item", "per-item Dims prediction ties expected STATUS to inventory column count before reading artifact content creating structural feedback loop", "Dims-driven Thin Coverage cross-item pattern detects multi-dimension thin-coverage from inventory structure without requiring per-item STATUS analysis", "dims_coverage frontmatter propagates per-dimension artifact counts into machine-readable metadata"]}
```
