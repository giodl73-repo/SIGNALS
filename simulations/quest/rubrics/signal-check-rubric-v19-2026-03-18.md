## signal-check rubric v19

**What was added (v18 -> v19):**

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-50 | Dims column in artifact inventory table — each artifact row annotated with its covered check dimensions (C/Sq/St/Co) — creating inventory pre-analysis coverage scan, per-item Dims prediction, Dims-driven Thin Coverage cross-item pattern, and `dims_coverage` frontmatter; makes per-dimension artifact coverage visible before entering any preflight item | dims-column-inventory | R19-EX-01 |
| C-51 | CROSS-ITEM PATTERNS section contains a structured, labeled pattern block — each cross-item pattern named with a header or identifier — making pattern types and diagnostic scope recoverable from a section scan without reading the full pattern prose | labeled-pattern-block | R19-EX-02 |
| C-52 | MISSING SIGNAL GUIDE entries are ordered by severity — most critical gaps (dimension coverage absent entirely) listed before less critical gaps (dimension coverage thin but present) — making the highest-priority guidance immediately accessible without reading the full guide | severity-ordered-guide | R19-EX-03 |
| C-53 | STATUS vocabulary uses a five-state taxonomy (e.g., PASS, OPEN, THIN, ABSENT, N/A or equivalent named states) rather than binary or three-state vocabulary, enabling finer-grained diagnostic resolution — distinguishing artifact absence, thin coverage, and open analysis as separate states | five-state-status | R19-EX-04 |

**Extraction rationale:**

**C-50** from V-05's live R19 axis. V-05 adds a sixth `Dims` column to the artifact inventory table annotating each artifact row with the check dimensions it covers (C, Sq, St, Co). This creates four structural advances not present in V-01 through V-04: (1) inventory pre-analysis coverage scan — per-dimension coverage visible before entering any preflight item; a missing dimension abbreviation predicts OPEN without reading analysis; (2) per-item Dims prediction — each preflight dimension item opens with a prediction derived from the Dims column, creating a structural feedback loop between inventory and analysis; (3) Dims-driven Thin Coverage cross-item pattern — multi-dimension thin-coverage detectable from inventory structure alone before STATUS analysis; (4) `dims_coverage` frontmatter — per-dimension artifact counts propagate into machine-readable metadata. Boundary confirmed clean: V-01 through V-04 all use 5-column tables and fail C-50. No combination of Axes D, E, or F implies C-50. C-50 is independently testable: presence or absence of the Dims column is structurally observable at the table level without entering any section body.

**C-51** from the R19 Axis D signal (V-01, V-04, V-05). Axis D introduces a structured, labeled pattern block in CROSS-ITEM PATTERNS: each pattern carries a named header or identifier, making pattern types and diagnostic scope recoverable from a section scan. V-02 and V-03 (Axes E and F only) carry unstructured CROSS-ITEM PATTERNS prose and fail C-51. C-51 requires C-07 (section present) as precondition; C-07 does not imply C-51. Boundary: variations carrying Axis D pass; variations without Axis D fail.

**C-52** from the R19 Axis E signal (V-02, V-04, V-05). Axis E introduces severity ordering in the MISSING SIGNAL GUIDE: critical gaps (dimension coverage eliminated) listed before thin-coverage gaps. V-01 and V-03 carry unordered guide entries and fail C-52. C-52 requires C-08 (section present) and C-13 (names each missing signal type) as preconditions; neither individually nor together imply C-52. Boundary: variations carrying Axis E pass; variations without Axis E fail.

**C-53** from the R19 Axis F signal (V-03, V-04, V-05). Axis F expands STATUS vocabulary from binary or three-state to a five-state taxonomy that distinguishes PASS, OPEN, THIN, ABSENT, and N/A (or equivalent named states). V-01 and V-02 use sub-five-state STATUS vocabulary and fail C-53. C-53 requires C-12 (four dimensions structured with consistent labeling) as precondition; C-12 does not imply C-53. Boundary: variations carrying Axis F pass; variations without Axis F fail.

**Round 19 scoring differential (post-extraction):**

| Var | Axis | C-50 | C-51 | C-52 | C-53 | Asp. | Composite |
|-----|------|------|------|------|------|------|-----------|
| V-01 | D | FAIL | PASS | FAIL | FAIL | 42/45 | 99.33 |
| V-02 | E | FAIL | FAIL | PASS | FAIL | 42/45 | 99.33 |
| V-03 | F | FAIL | FAIL | FAIL | PASS | 42/45 | 99.33 |
| V-04 | D+E | FAIL | PASS | PASS | FAIL | 43/45 | 99.56 |
| V-05 | D+E+F + live | PASS | PASS | PASS | PASS | 45/45 | **100.00** |

**Updated parameters:**
- Aspirational denominator: 41 -> **45**
- Formula: `composite = 90 + (aspirational_pass / 45) * 10`
- New subsumption links:
  - C-50 independently testable — no precondition in established chain
  - `C-07 <- C-51` (C-51 requires C-07; C-07 does not imply C-51)
  - `C-08 <- C-52` and `C-13 <- C-52` (C-52 requires C-08 and C-13; neither implies C-52)
  - `C-12 <- C-53` (C-53 requires C-12; C-12 does not imply C-53)

---

## Criterion additions

| ID | Criterion | Source |
|----|-----------|--------|
| C-50 | The artifact inventory table includes a `Dims` column annotating each listed artifact with its covered check dimensions (C, Sq, St, Co), creating four structural advances: (1) inventory pre-analysis coverage scan — per-dimension coverage is visible before entering any preflight item, so a missing dimension abbreviation predicts OPEN without reading analysis; (2) per-item Dims prediction — each preflight dimension item opens with a prediction derived from the Dims column, creating a feedback loop between inventory and analysis; (3) Dims-driven Thin Coverage cross-item pattern — multi-dimension thin-coverage is detectable from inventory structure alone before STATUS analysis; (4) `dims_coverage` frontmatter — per-dimension artifact counts propagate into machine-readable metadata; an artifact inventory table without a Dims column satisfies the inventory presence requirement but not C-50: per-dimension coverage is not visible before entering the preflight items; C-50 is independently testable: the presence or absence of a Dims column in the inventory table is structurally observable without entering any preflight item or section body; boundary confirmed clean: V-01 through V-04 all use 5-column tables (without Dims column) and fail C-50; no combination of Axes D, E, or F implies C-50; C-50 is independently testable from C-51, C-52, and C-53 | R19-EX-01 |
| C-51 | The CROSS-ITEM PATTERNS section contains a structured pattern block — each cross-item pattern is labeled with a named header or identifier making the pattern type and its diagnostic scope recoverable from a section scan without reading the full pattern prose; an output whose CROSS-ITEM PATTERNS section uses unstructured prose without named pattern labels satisfies C-07 (section present) but not C-51: the reader must read the full section body to identify which patterns are addressed and what their diagnostic scope is; "every cross-item pattern" means each distinct pattern surfaced in the section, without exception; C-51 requires C-07 as a precondition; C-07 does not imply C-51; C-51 is independently testable from C-50, C-52, and C-53; boundary confirmed: variations carrying Axis D pass; variations without Axis D fail | R19-EX-02 |
| C-52 | The MISSING SIGNAL GUIDE entries are ordered by severity — most critical signal gaps (gaps that eliminate dimension coverage entirely, i.e., no artifact covers the dimension) listed before less critical gaps (gaps that thin but do not eliminate coverage) — making the highest-priority guidance immediately accessible without reading the full guide; an output whose MISSING SIGNAL GUIDE names each missing signal type (C-13) without severity ordering satisfies C-08 and C-13 but not C-52: the reader cannot identify priority without reading the full guide; C-52 requires C-08 and C-13 as preconditions; C-08 alone does not imply C-52; C-13 alone does not imply C-52; C-08 and C-13 together do not imply C-52 — severity ordering is independently checkable beyond their satisfaction; C-52 is independently testable from C-50, C-51, and C-53; boundary confirmed: variations carrying Axis E pass; variations without Axis E fail | R19-EX-03 |
| C-53 | STATUS vocabulary uses a five-state taxonomy — at minimum naming five distinct states that separately express: passing coverage, open analysis (artifacts present but analysis incomplete), thin coverage (artifacts present but below threshold), absent coverage (no artifacts covering the dimension), and not-applicable — rather than binary (PASS/FAIL) or three-state vocabulary; the five states enable finer-grained diagnostic resolution that is not expressible in sub-five-state vocabularies: distinguishing artifact absence from thin coverage and open analysis as separate diagnostic states; an output whose STATUS fields use binary or three-state vocabulary satisfies the status-presence requirements but not C-53: the distinctions between artifact absence, thin coverage, and open analysis are collapsed and the reader cannot determine which failure mode applies without reading the full dimension analysis; C-53 requires C-12 (four dimensions structured with consistent labeling) as a precondition; C-12 does not imply C-53; C-53 is independently testable from C-50, C-51, and C-52; boundary confirmed: variations carrying Axis F pass; variations without Axis F fail | R19-EX-04 |

## Updated parameters

- Aspirational count: 41 -> **45**
- Formula: `composite = 90 + (aspirational_pass / 45) * 10`
- C-50 independently testable — no precondition in established criterion chain
- C-51 requires C-07 as precondition; C-07 does not imply C-51
- C-52 requires C-08 and C-13 as preconditions; neither individually nor together imply C-52
- C-53 requires C-12 as precondition; C-12 does not imply C-53

## Subsumption chains

```
C-20 <- C-22 <- C-24 <- C-26 <- C-29 <- C-33 <- C-36 <- C-38 <- C-40 <- C-42 <- C-43 <- C-44 <- C-46
                C-24 <- C-27 <- C-30
C-20 <- C-23 <- C-25
C-22 <- C-31
C-20 <- C-32
C-28  (independently testable -- heading-level existence assertion)
C-21 <- C-34 <- C-35
C-35 <- C-37  (C-37 requires C-35 as precondition; independently testable beyond it)
C-37 <- C-39  (C-39 requires C-37 as precondition; independently testable beyond it)
C-39 <- C-41  (C-41 requires C-39 as precondition; independently testable beyond it)
C-41 <- C-45  (C-45 requires C-41 as precondition; independently testable beyond it)
C-40 <- C-42  (C-42 requires C-40 as precondition; independently testable beyond it)
C-42 <- C-43  (C-43 requires C-42 as precondition; independently testable beyond it)
C-43 <- C-44  (C-44 requires C-43 as precondition; independently testable beyond it)
C-44 <- C-46  (C-46 requires C-44 as precondition; independently testable beyond it)
C-45 <- C-46  (C-46 requires C-45 as precondition; independently testable beyond it)
C-11 <- C-47  (C-47 requires C-11 as precondition; independently testable beyond it)
C-48  (independently testable -- no precondition in established chain)
C-18 <- C-49  (C-49 requires C-18, C-47, C-48 as preconditions; none imply C-49)
C-47 <- C-49  (C-49 requires C-47 as precondition; independently testable beyond it)
C-48 <- C-49  (C-49 requires C-48 as precondition; independently testable beyond it)
C-50  (independently testable -- no precondition in established chain)
C-07 <- C-51  (C-51 requires C-07 as precondition; independently testable beyond it)
C-08 <- C-52  (C-52 requires C-08 and C-13 as preconditions; neither implies C-52)
C-13 <- C-52  (C-52 requires C-13 as precondition; independently testable beyond it)
C-12 <- C-53  (C-53 requires C-12 as precondition; independently testable beyond it)
```

---

## Full Criterion Inventory

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-01 | *(essential — topic-signal file structure conformant)* | essential | — |
| C-02 | *(essential — four preflight dimensions present)* | essential | — |
| C-03 | *(essential — STANDING RULES section present)* | essential | — |
| C-04 | *(essential — artifact inventory table present)* | essential | — |
| C-05 | *(essential — output is not a raw checklist)* | essential | — |
| C-06 | READINESS SUMMARY section present | recommended-section | — |
| C-07 | CROSS-ITEM PATTERNS section present | recommended-section | — |
| C-08 | MISSING SIGNAL GUIDE section present | recommended-section | — |
| C-09 | Named STANDING RULES block present (block title present, not inline prose) | standing-rules-block | — |
| C-10 | STANDING RULES block contains Rule 1 (verbatim absence) and Rule 2 (no inference) as named, numbered rules | standing-rules-named | — |
| C-11 | READINESS SUMMARY uses pilot-briefing language — framing the verdict as a crew advisory rather than a pass/fail judgment | readiness-register | — |
| C-12 | Four dimensions (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE) structured with consistent labeling and formatting across all four preflight items | dimension-structure | — |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type explicitly rather than describing gaps in generic terms | guide-signal-names | — |
| C-14 | STANDING RULES block precedes all artifact inventory and all preflight dimension analysis in document order | standing-rules-precedence | — |
| C-15 | Each preflight dimension item specifies its required verbatim absence phrase — the exact text that must appear when no signal is present | verbatim-phrase-spec | — |
| C-16 | Every constraint in STANDING RULES explicitly enumerates all output locations it governs — no constraint applies to unstated locations by implication | constraint-enumeration | — |
| C-17 | Verbatim absence phrases are embedded at the point of use — present within each preflight dimension item, not only in STANDING RULES | verbatim-phrase-embedded | — |
| C-18 | Advisory register is carried structurally through framing vocabulary — pilot-briefing, coaching, and "team decides" language present in section headings, status fields, and summary prose, not only in isolated phrases | advisory-register | — |
| C-19 | Triple enforcement stack (Rules 1, 2, 3) declared as a unit with interdependency named — a note or block states that the three rules form a coordinated stack in which no layer substitutes for another and all three must pass for the output to be a valid health report | enforcement-stack | — |
| C-20 | Location-enumeration requirement expressed as a named meta-rule — the obligation to list all output locations appears as a titled rule within STANDING RULES, not as embedded prose | meta-rule-named | — |
| C-21 | Each rule is assigned a named failure class — the specific failure mode triggered by violating each rule is labeled (e.g., Phantom Signal, Silent Gap, Scope Escape) | failure-class | — |
| C-22 | Meta-rule includes a temporal activation gate — a condition specifying when the location-enumeration obligation activates (e.g., "at the time a new constraint is added") | activation-gate | — |
| C-23 | Meta-rule declares self-application — the body of the meta-rule states that the rule applies to itself, establishing that the meta-rule's own output locations must be enumerated | meta-rule-self-application | — |
| C-24 | Activation gate framed as a rule-validity condition — gate language states that a constraint added without location enumeration is not a valid constraint, rather than merely a violating one | gate-validity-framing | — |
| C-25 | Self-application declaration includes a proximate scope pointer — the self-application clause names the specific section or structural location where the meta-rule's own enumeration obligation is satisfied | self-application-scope | — |
| C-26 | Activation gate carries both obligation framing (what must be done) and validity framing (what is not valid if not done) — both registers co-present in the gate clause | gate-dual-register | — |
| C-27 | Validity condition uses rule-existence framing — gate clause states that a constraint not accompanied by location enumeration does not exist as a valid rule | validity-existence-framing | — |
| C-28 | Rule name encodes an existence assertion — the title of the meta-rule is phrased so that the rule's name alone asserts what must exist (e.g., "EVERY CONSTRAINT NAMES ITS LOCATIONS") | name-existence-assertion | — |
| C-29 | Dual register expressed as labeled sections with non-substitutability — the obligation and validity registers are placed under distinct labeled sub-headers or fields, and a statement declares that the two registers are not interchangeable | dual-register-labeled | — |
| C-30 | Validity condition uses rule-existence framing in a separate labeled field — the existence framing appears under its own label or heading, independently legible from the obligation framing | validity-field-labeled | — |
| C-31 | Temporal activation gate is placed under a labeled field — the gate condition appears under its own label or heading, independently legible from the meta-rule body | gate-field-labeled | — |
| C-32 | Location-enumeration meta-rule includes an explicit self-reference to its own position in document structure — the rule body names the section in which it resides as one of the locations enumerated under the meta-rule's own application | meta-rule-self-reference | — |
| C-33 | STANDING RULES block carries a named Rule 3 (scope-escape prevention) as a numbered, titled rule alongside Rule 1 and Rule 2 | rule-3-named | — |
| C-34 | Each named failure class includes a definition — a clause naming what makes the failure class distinct and what condition triggers it | failure-class-defined | — |
| C-35 | Each named failure class includes an example — a concrete instantiation of the failure mode at the artifact or dimension level | failure-class-example | — |
| C-36 | Rule 3 (scope-escape prevention) includes an explicit Applies-to declaration — a labeled field or clause naming all output locations to which Rule 3 applies | rule-3-applies-to | — |
| C-37 | Each named failure class includes a detection instruction — a clause specifying how to identify the failure mode in output | failure-class-detection | — |
| C-38 | Applies-to declarations carry location-specific scope — each Applies-to declaration distinguishes which parts of the named section are governed (e.g., "all STATUS fields" rather than "READINESS SUMMARY") | applies-to-scoped | — |
| C-39 | Each named failure class includes a prevention instruction — a clause specifying what structural commitment prevents the failure mode | failure-class-prevention | — |
| C-40 | Applies-to declarations include cross-section reach — at least one Applies-to declaration spans multiple named sections, and the cross-section scope is explicitly stated | applies-to-cross-section | — |
| C-41 | Each named failure class includes a recovery instruction — a clause specifying how to correct the output if the failure mode has already occurred | failure-class-recovery | — |
| C-42 | Applies-to declarations include field-level granularity — at least one Applies-to declaration names a specific field within a section (e.g., a specific column in a table) rather than a section as a whole | applies-to-field-level | — |
| C-43 | Applies-to declarations are consolidated under a labeled sub-structure within each rule — all location enumerations for a given rule appear under a single labeled Applies-to block rather than scattered through the rule body | applies-to-consolidated | — |
| C-44 | Applies-to sub-structure uses a tabular or list format — the location enumerations within each Applies-to block appear as a structured list or table rather than inline prose, making locations individually enumerable without parsing prose | applies-to-structured | — |
| C-45 | Each named failure class is expressed as a standalone labeled entry — definition, example, detection, prevention, and recovery appear as labeled sub-fields within a named failure-class block rather than as running prose under the rule body | failure-class-structured | — |
| C-46 | STANDING RULES block contains a dedicated FAILURE CLASS REGISTER — a named, labeled section or sub-section that consolidates all named failure classes as a registry, making the full failure vocabulary recoverable from the register heading without reading the individual rule bodies | failure-class-register | — |
| C-47 | The READINESS SUMMARY section includes a dimensional-status preamble — a structured block naming all four dimension statuses (CAUSAL GAP: [status], SEQUENCE: [status], STALENESS: [status], COHERENCE: [status]) before the pilot-briefing prose — so that the full STATUS picture is recoverable from the summary block alone without reading any preflight dimension items; an output satisfying C-11 by using pilot-briefing language in a prose-only READINESS SUMMARY satisfies C-11 but not C-47: the full STATUS picture requires reading the preflight items to recover all four dimension statuses; C-47 requires C-11 as a precondition; C-11 does not imply C-47; an output satisfying C-47 automatically satisfies C-11 (and therefore C-06); C-47 is independently testable from C-48 and C-49; boundary confirmed clean: V-01 through V-04 (R18) carry prose-only READINESS SUMMARY sections and all fail C-47; V-05 (R18) carries the four-line STATUS block before prose and passes | summary-status-preamble | R18-EX-01 |
| C-48 | Every section header in the output carries a section-function annotation — a bracketed or inline label naming the section's knowledge type and reader purpose (e.g., "[STANDING RULES -- Constraints that persist across all evaluations]", "[READINESS SUMMARY -- Synthesized advisory verdict accessible before reading preflight items]") — so that the output's lifecycle architecture and the epistemic role of each section are recoverable from a heading scan alone without reading any section body; an output whose sections are labeled only with section names without function annotations satisfies the section-presence requirements (C-06, C-07, C-08, C-09) but not C-48: the reader must enter each section body to determine its function; "every section header" means all named section headers present in the output, without exception; C-48 is independently testable and does not require any precondition among the established criterion chain; C-48 is independently testable from C-47 and C-49 | section-function-annotation | R18-EX-02 |
| C-49 | The output simultaneously expresses advisory register at three independent levels of structural granularity — (1) per-item coaching vocabulary in every preflight dimension (C-18), (2) per-section function annotations on every section header (C-48), and (3) per-summary dimensional-status preamble in READINESS SUMMARY (C-47) — making register drift structurally improbable because each level independently enforces the advisory register such that all three would have to fail simultaneously for register drift to occur; an output satisfying any two of the three levels satisfies those criteria individually but not C-49: the triple-vector saturation requires co-presence of all three vectors in the same output; an output satisfying C-18 and C-47 but lacking C-48 section-function annotations satisfies C-18 and C-47 but fails C-49; C-49 requires C-18, C-47, and C-48 as preconditions; C-18, C-47, and C-48 together do not imply C-49 (co-presence is independently checkable beyond their individual satisfaction); an output satisfying C-49 automatically satisfies C-18, C-47, and C-48 | advisory-register-saturation | R18-EX-03 |
| C-50 | The artifact inventory table includes a `Dims` column annotating each listed artifact with its covered check dimensions (C, Sq, St, Co), creating four structural advances: (1) inventory pre-analysis coverage scan — per-dimension coverage is visible before entering any preflight item, so a missing dimension abbreviation predicts OPEN without reading analysis; (2) per-item Dims prediction — each preflight dimension item opens with a prediction derived from the Dims column, creating a feedback loop between inventory and analysis; (3) Dims-driven Thin Coverage cross-item pattern — multi-dimension thin-coverage is detectable from inventory structure alone before STATUS analysis; (4) `dims_coverage` frontmatter — per-dimension artifact counts propagate into machine-readable metadata; an artifact inventory table without a Dims column satisfies the inventory presence requirement but not C-50: per-dimension coverage is not visible before entering the preflight items; C-50 is independently testable: the presence or absence of a Dims column in the inventory table is structurally observable without entering any preflight item or section body; boundary confirmed clean: V-01 through V-04 (R19) all use 5-column tables and fail C-50; no combination of Axes D, E, or F implies C-50; C-50 is independently testable from C-51, C-52, and C-53 | dims-column-inventory | R19-EX-01 |
| C-51 | The CROSS-ITEM PATTERNS section contains a structured pattern block — each cross-item pattern is labeled with a named header or identifier making the pattern type and its diagnostic scope recoverable from a section scan without reading the full pattern prose; an output whose CROSS-ITEM PATTERNS section uses unstructured prose without named pattern labels satisfies C-07 (section present) but not C-51: the reader must read the full section body to identify which patterns are addressed and what their diagnostic scope is; "every cross-item pattern" means each distinct pattern surfaced in the section, without exception; C-51 requires C-07 as a precondition; C-07 does not imply C-51; C-51 is independently testable from C-50, C-52, and C-53; boundary confirmed: variations carrying Axis D pass; variations without Axis D fail | labeled-pattern-block | R19-EX-02 |
| C-52 | The MISSING SIGNAL GUIDE entries are ordered by severity — most critical signal gaps (gaps that eliminate dimension coverage entirely, i.e., no artifact covers the dimension) listed before less critical gaps (gaps that thin but do not eliminate coverage) — making the highest-priority guidance immediately accessible without reading the full guide; an output whose MISSING SIGNAL GUIDE names each missing signal type (C-13) without severity ordering satisfies C-08 and C-13 but not C-52: the reader cannot identify priority without reading the full guide; C-52 requires C-08 and C-13 as preconditions; C-08 alone does not imply C-52; C-13 alone does not imply C-52; C-08 and C-13 together do not imply C-52 — severity ordering is independently checkable beyond their satisfaction; C-52 is independently testable from C-50, C-51, and C-53; boundary confirmed: variations carrying Axis E pass; variations without Axis E fail | severity-ordered-guide | R19-EX-03 |
| C-53 | STATUS vocabulary uses a five-state taxonomy — at minimum naming five distinct states that separately express: passing coverage, open analysis (artifacts present but analysis incomplete), thin coverage (artifacts present but below threshold), absent coverage (no artifacts covering the dimension), and not-applicable — rather than binary (PASS/FAIL) or three-state vocabulary; the five states enable finer-grained diagnostic resolution that is not expressible in sub-five-state vocabularies: distinguishing artifact absence from thin coverage and open analysis as separate states; an output whose STATUS fields use binary or three-state vocabulary satisfies the status-presence requirements but not C-53: the distinctions between artifact absence, thin coverage, and open analysis are collapsed; C-53 requires C-12 (four dimensions structured with consistent labeling) as a precondition; C-12 does not imply C-53; C-53 is independently testable from C-50, C-51, and C-52; boundary confirmed: variations carrying Axis F pass; variations without Axis F fail | five-state-status | R19-EX-04 |
