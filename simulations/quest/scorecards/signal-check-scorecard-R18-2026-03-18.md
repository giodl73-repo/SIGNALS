Scorecard written. Now the required JSON block:

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Dimensional-status preamble in READINESS SUMMARY -- a four-line structured block naming all four dimension statuses before pilot-briefing prose, making the full STATUS picture recoverable from the summary block alone without reading preflight items (C-47 candidate; requires C-11; C-11 does not imply C-47; boundary confirmed clean across V-01 to V-04)", "Section-function annotations on every section header make lifecycle architecture surface-readable from a heading scan alone -- each section's knowledge type and reader purpose visible before reading the body (independently testable structural element, C-48 candidate)", "Triple-vector advisory register -- coaching vocabulary per-item (A), FUNCTION annotations per-section (C), and dimensional-status preamble per-summary (live axis) simultaneously express advisory register at three levels of granularity, making register drift structurally improbable (compound saturation pattern from V-05)"]}
```

---

**Round 18 summary:**

- All 5 variations: **100.00** (rubric v17 ceiling, 38/38 aspirational)
- All essential: **5/5 PASS** across all variations
- **C-47 candidate extracted** from V-05's live R18 axis: dimensional-status preamble in READINESS SUMMARY
- Rubric v18 additions: C-47 (denominator 38 → 39, formula `composite = 90 + (aspirational_pass / 39) * 10`)
TANDING RULES contains Rule 1 and Rule 2 | PASS | Rule 1 -- Absence Drift and Rule 2 -- Reference Ambiguity both present |
| C-14 | STANDING RULES precedes all inventory and analysis | PASS | Appears before GATHER YOUR SIGNALS, READINESS SUMMARY, THE PREFLIGHT CHECK |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS | All four dimensions carry "Required verbatim absence phrase for this item:" with exact phrases |
| C-16 | Every constraint enumerates all output locations | PASS | Rule 1: 7 locations; Rule 2: 7 locations; Rule 3: "all Rule declarations... including Rule 3 itself and any rule added in the future" |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | Phrases embedded inline within each dimension item's instruction block, not only in a reference table |
| C-19 | Triple enforcement stack declared as unit | PASS | "Rules 1, 2, and 3 form a coordinated enforcement stack... No layer substitutes for another; the three rules address independent failure modes." |
| C-20 | Location-enumeration requirement as named meta-rule | PASS | Rule 3 "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" governs all rule declarations including itself |
| C-21 | Each rule assigned a named failure class | PASS | Absence Drift / Reference Ambiguity / Constraint Scope Gaps |
| C-22 | Meta-rule includes temporal activation gate | PASS | "Scope must be discharged at rule-creation time, not retroactively." |
| C-23 | Meta-rule self-application declared in rule body | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| C-24 | Activation gate framed as validity condition | PASS | "a Rule that has not declared its scope does not exist as an active rule" |
| C-25 | Body self-application includes proximate scope pointer | PASS | "Rule 3 itself declares its scope below" -- "below" is the proximate pointer |
| C-26 | Dual-register enforcement (obligation + validity) | PASS | Obligation: "every Rule... must declare all output locations"; Existence condition: "does not exist as an active rule" |
| C-27 | Validity condition uses rule-existence framing | PASS | "A rule without scope has no force, no scope, and no standing. It does not exist as an active rule." |
| C-28 | Rule name encodes existence assertion in heading | PASS | "Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:" |
| C-29 | Dual register as structurally labeled sections with non-substitutability | PASS | "Obligation:" and "Existence condition:" labels; "These two registers are not substitutes: the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost." |
| C-30 | Step-up disclaimer before existence framing | PASS | "'Not operative' understates the condition -- an inoperative rule is still a declared object with suspended force." |
| C-31 | Temporal gate as "at rule-creation time" | PASS | "scope must be discharged at rule-creation time, not retroactively" |
| C-32 | Forward-scope Applies-to | PASS | "including Rule 3 itself and any rule added in the future" |
| C-33 | Non-substitutability assigns distinct function description to each register | PASS | "the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost" -- action-spec vs. loss-model |
| C-34 | Each rule heading encodes failure class | PASS | "Rule 1 -- Absence Drift:", "Rule 2 -- Reference Ambiguity:", "Rule 3 -- Constraint Scope Gaps:" |
| C-35 | Failure class in top-level rule heading | PASS | "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:", "Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:", "Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:" |
| C-36 | Reader-position named explicitly in function framing | PASS | "the obligation tells a committing engineer reading for what to fix; the existence condition tells a reviewer reading for what is already lost" |
| C-37 | ENFORCEMENT STACK NOTE collapses inline labels to forward-references | PASS | "failure class encoded in each rule's heading above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" |
| C-38 | Each rule names its own reader position | PASS | Rule 1: "A committing engineer checking for missing absence declarations consults this rule"; Rule 2: "A skill-reference consumer disambiguating a reference consults this rule"; Rule 3: committing engineer / reviewer |
| C-39 | NOTE reduced to pure interdependency statement | PASS | NOTE contains only stack declaration, forward-reference with parenthetical index, non-substitutability. No "Rule 1 prevents X" prose. |
| C-40 | Per-rule reader positions surfaced as consulting directory | PASS | "Consulting Directory:" routes committing engineers / skill-reference consumers / committing engineers and reviewers to Rule 1 / Rule 2 / Rule 3 |
| C-41 | Pure interdependency NOTE attributes failure-mode ownership to headings | PASS | "failure class encoded in each rule's heading above" -- ownership attribution makes omission of prevents-prose self-explaining |
| C-42 | Consulting directory carries explicit completeness assertion | PASS | "All 3 reader roles for this block are listed above." |
| C-43 | Completeness assertion uses all-roles claim form | PASS | "All 3 reader roles for this block are listed above." -- direct proposition, not count-annotation |
| C-44 | All-roles claim includes embedded count qualifier | PASS | "All **3** reader roles for this block are listed above." -- count "3" embedded as qualifier |
| C-45 | Failure-mode ownership attribution extended with parenthetical heading index | PASS | "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" -- 3 entries |
| C-46 | Dual count consistency: C-44 count and C-45 entry count numerically consistent | PASS | C-44 count = 3; C-45 parenthetical entries = 3 -- independently cross-checkable |

**Aspirational subtotal from STANDING RULES (C-09 to C-46): 38/38 PASS for all five variations.**

---

## V-01 Detail — Phrasing register: coaching/conversational (single-axis A)

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE present in order |
| C-02 | PASS | "STATUS: OK \| FLAG \| OPEN" in each dimension item |
| C-03 | PASS | "Think of this as a preflight check. The checklist does not decide whether to fly -- it makes sure the pilot sees everything before they decide. Nothing here blocks you from proceeding." |
| C-04 | PASS | "Frame as pilot briefing -- not a verdict. The team decides." |
| C-05 | PASS | "Why this matters:", "What the inventory shows:", "What the team can do:" -- coaching vocabulary structurally present in every dimension item; advisory register not only declared but enacted through framing vocabulary |

**Essential: 5/5 PASS**

### Recommended: 3/3 PASS (all sections present)

### Aspirational

C-09 to C-46: 38/38 PASS (STANDING RULES common trace above).

**C-18 confirmation**: "Why this matters:", "What the inventory shows:", "What the team can do:" -- coaching vocabulary is the structural vehicle for advisory register throughout all four dimension items. Not only the header disclaimer. PASS.

**Aspirational: 38/38 PASS**

### New R18 axis

- **C-47**: FAIL -- READINESS SUMMARY is prose-only; no structured per-dimension STATUS block before prose.
- **Axis A independence confirmed**: coaching vocabulary present in V-01, absent from V-02 and V-03 -- independently testable.

**V-01 Composite: 100.00**

---

## V-02 Detail — Output format: leading scan index table (single-axis B)

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Four items in order |
| C-02 | PASS | STATUS field with OK / FLAG / OPEN in each item |
| C-03 | PASS | "Think of this as a preflight check... Nothing here blocks you from proceeding." |
| C-04 | PASS | "Frame as pilot briefing -- not a verdict. The team decides." |
| C-05 | PASS | "THE PREFLIGHT CHECK" structural header; scan index table is a structural advisory-register artifact; "What we're checking:" inspection-framed advisory vocabulary per item |

**Essential: 5/5 PASS**

### Recommended: 3/3 PASS

### Aspirational

C-09 to C-46: 38/38 PASS.

**C-15 + C-17 dual-location**: Absence phrases in the scan index table (upfront reference) AND inline within each item body ("Required verbatim absence phrase for this item:"). Both the table path (upfront lookup) and the inline path (at point of use) are simultaneously satisfied. C-17 does not depend on the table -- the inline embedding is independently present.

**C-18**: "THE PREFLIGHT CHECK" header, STATUS fields, and scan table structure carry advisory register structurally; "What we're checking:" is inspection-framed advisory vocabulary. PASS.

**Aspirational: 38/38 PASS**

### New R18 axis

- **C-47**: FAIL -- no dimensional-status preamble in READINESS SUMMARY.
- **Axis B independence confirmed**: scan table is structurally detectable from THE PREFLIGHT CHECK heading area; V-01 and V-03 carry no such table.

**V-02 Composite: 100.00**

---

## V-03 Detail — Lifecycle emphasis: section-function annotations (single-axis C)

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Four items in order |
| C-02 | PASS | STATUS field with OK / FLAG / OPEN |
| C-03 | PASS | "Think of this as a preflight check... Nothing here blocks you from proceeding." |
| C-04 | PASS | FUNCTION annotation: "[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail... Does not decide; frames what the team is walking into.]" Plus prose: "Frame as pilot briefing -- not a verdict." |
| C-05 | PASS | FUNCTION annotations on every section header make lifecycle function structurally visible: GATHER YOUR SIGNALS annotated as inventory-build; READINESS SUMMARY as pilot briefing; THE PREFLIGHT CHECK as four-dimension analysis ordered by difficulty; CROSS-ITEM PATTERNS as root-cause synthesis; MISSING SIGNAL GUIDE as actionable gap map; ARTIFACT as ground-truth persistence |

**Essential: 5/5 PASS**

### Recommended: 3/3 PASS

### Aspirational

C-09 to C-46: 38/38 PASS.

**C-18**: FUNCTION annotations carry the advisory register structurally at the section level -- "[FUNCTION: Build the artifact inventory... If no artifacts exist, the run stops here -- health cannot be assessed without a ground truth.]" on GATHER YOUR SIGNALS makes the advisory constraint visible before reading the body. "[FUNCTION: Root-cause synthesis... If all items are OK, this section confirms no pattern exists -- it does not silently pass.]" on CROSS-ITEM PATTERNS carries the Rule 1 advisory intent structurally in the heading. PASS.

**Aspirational: 38/38 PASS**

### New R18 axis

- **C-47**: FAIL -- no dimensional-status preamble in READINESS SUMMARY.
- **Axis C independence confirmed**: FUNCTION annotations present in V-03, absent from V-01 and V-02; lifecycle architecture recoverable from heading scan alone.

**V-03 Composite: 100.00**

---

## V-04 Detail — Combined A+B: coaching register + scan index table

### Essential: 5/5 PASS

Coaching vocabulary (A) and scan index table (B) both present; advisory register carried through two independent structural vectors. "Frame as pilot briefing -- not a verdict. The team decides." present. All four items in order.

### Recommended: 3/3 PASS

### Aspirational

C-09 to C-46: 38/38 PASS.

**C-18**: Two independent structural vectors: per-item coaching labels AND scan index table structure. Neither is required for the other; both carry advisory register structurally.

**C-15 + C-17**: Dual-location absence phrases (table + inline) confirmed, same as V-02.

**Aspirational: 38/38 PASS**

### New R18 axis

- **C-47**: FAIL -- READINESS SUMMARY is prose-only: "2-4 sentences: overall signal health... Frame as pilot briefing -- not a verdict." No structured STATUS block.
- **A+B independence from C-47 confirmed**: Neither coaching vocabulary nor scan table nor their combination introduces a dimensional-status preamble. C-47 boundary confirmed clean across A, B, and A+B.

**V-04 Composite: 100.00**

---

## V-05 Detail — Combined A+B+C + live R18 axis: dimensional-status preamble

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Four items in order |
| C-02 | PASS | STATUS values present: in per-item fields AND in dimensional-status preamble |
| C-03 | PASS | "Think of this as a preflight check... Nothing here blocks you from proceeding. It exists so you know what you know before you commit." |
| C-04 | PASS | FUNCTION annotation: "The team decides whether to proceed."; prose: "Frame as pilot briefing -- not a verdict. The team decides." |
| C-05 | PASS | Three simultaneous structural vectors: (1) coaching vocabulary per-item; (2) FUNCTION annotations per-section; (3) dimensional-status preamble in READINESS SUMMARY. Advisory register redundantly expressed at item, section, and summary level. |

**Essential: 5/5 PASS**

### Recommended: 3/3 PASS

### Aspirational

C-09 to C-46: 38/38 PASS.

**C-11 confirmation**: READINESS SUMMARY opens with dimensional-status preamble, then the 2-4 sentence pilot briefing follows: "2-4 sentences: overall signal health for {topic}... Frame as pilot briefing -- not a verdict. The team decides." The preamble is additive -- it precedes the prose without replacing it. C-11 satisfied by the prose section. PASS.

**C-18**: Three structural vectors simultaneously carry advisory register: coaching labels (A), FUNCTION annotations (C), dimensional-status preamble (live R18 axis). Advisory register is structurally pervasive at three levels of granularity. PASS.

**C-15 + C-17 + preamble extension**: Absence phrases in scan table (B), inline per item, AND Rule 1 explicitly governs preamble fields: "write the following for each dimension: CAUSAL GAP: OPEN | SEQUENCE: OPEN | STALENESS: OPEN | COHERENCE: OPEN" when no artifacts exist. Three-location Rule 1 coverage.

**Dimensional-status preamble structural form:**
```
Dimensional status:
  CAUSAL GAP:  [OK / FLAG / OPEN]
  SEQUENCE:    [OK / FLAG / OPEN]
  STALENESS:   [OK / FLAG / OPEN]
  COHERENCE:   [OK / FLAG / OPEN]
```
Preamble presence/absence is independently detectable from READINESS SUMMARY structure without reading prose. STATUS back-pointer annotations at each preflight item's STATUS field (`<- use this value for CAUSAL GAP in the dimensional-status preamble`) close the loop from analysis to summary.

**Aspirational: 38/38 PASS**

### New R18 axis

| Axis | Result | Evidence |
|------|--------|----------|
| C-47 (dimensional-status preamble) | PASS* | READINESS SUMMARY opens with four-line structured STATUS block before pilot-briefing prose; full dimension health recoverable from summary block alone |
| Axis A (coaching vocabulary) | PASS | Same as V-01 |
| Axis B (scan index table) | PASS | Same as V-02 |
| Axis C (FUNCTION annotations) | PASS | Same as V-03 |

*C-47 is a candidate criterion for rubric v18; not yet part of the rubric.

**V-05 Composite: 100.00**

---

## Excellence Signals

All five variations reach the rubric v17 ceiling (100.00). V-05 is the top-complexity variation. The following patterns are candidates for rubric v18.

### Pattern 1: Dimensional-status preamble in READINESS SUMMARY (C-47 candidate)

V-05's READINESS SUMMARY opens with a four-line structured block naming all four dimension statuses before pilot-briefing prose. The full STATUS picture is recoverable from the summary block without reading preflight items. V-01 through V-04 all satisfy C-11 via prose; none carry the preamble. C-47 boundary is confirmed clean across all single-axis designs and the A+B combination.

V-05 additional detail: Rule 1 extended to govern preamble fields; STATUS back-pointer annotations at each dimension's STATUS field connect analysis to summary; empty-inventory case produces four explicit OPEN values before the absence phrase.

### Pattern 2: Section-function annotations (C-48 candidate)

V-03 and V-05 carry `[FUNCTION: ...]` on every section header, naming each section's knowledge type and reader purpose. Lifecycle architecture recoverable from heading scan alone. Independently testable: present in V-03/V-05, absent from V-01/V-02/V-04.

### Pattern 3: Triple-vector advisory register (compound structural finding)

V-05 achieves advisory register saturation through three simultaneous structural vectors: per-item coaching vocabulary (A), per-section FUNCTION annotations (C), and per-summary dimensional-status preamble (live R18 axis). No single axis produces all three coverage levels. V-05's compound form makes advisory register structurally improbable to lose through drift.

---

## C-47 Candidate Specification

**Source**: V-05, live R18 axis.

**Proposed criterion**: READINESS SUMMARY opens with a dimensional-status preamble -- a structured per-dimension STATUS block naming all four dimensions (CAUSAL GAP / SEQUENCE / STALENESS / COHERENCE) with their final OK/FLAG/OPEN values, placed before the pilot-briefing prose -- so that a reader scanning the READINESS SUMMARY block recovers the full four-dimension STATUS picture without reading the preflight check items; presence/absence is independently testable from the READINESS SUMMARY structure (detectable without reading prose); C-47 requires C-11 as a precondition; C-11 does not imply C-47; an output satisfying C-47 automatically satisfies C-11.

**Precondition**: C-11
**Boundary evidence**: V-01 through V-04 satisfy C-11, fail C-47 -- boundary confirmed across single-axis and combined (A+B) designs.

---

## Round Summary

| Round | Top score | All essential | New criteria extracted |
|-------|-----------|---------------|----------------------|
| R18 | 100.00 | YES (all 5) | C-47 candidate (dimensional-status preamble in READINESS SUMMARY) |
