## signal-check rubric v20

**What was added (v19 -> v20):**

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-54 | Evidence trace field in VERDICT maps each blocking dimension to the exact inventory row number and artifact path (or explicit "not-represented-in-inventory" declaration for absent dimensions) — creating a closed structural loop from decision to source traversable without entering any preflight item body; absence declared at verdict level, not only within preflight item bodies; `evidence_trace` frontmatter enables automated cross-checks | evidence-trace-verdict | R20-EX-01 |
| C-55 | Named VERDICT section — a structured block separate from READINESS SUMMARY that declares the go/no-go recommendation, names blocking dimensions in a `blocking_dims` field, states the resolution condition, and is enumerated in all STANDING RULES Applies-to scopes that govern verdict-level output — creating a single-point decision artifact locatable without reading preflight item bodies or summary prose | verdict-section | R20-EX-02 |
| C-56 | Quality column in artifact inventory table — each artifact row annotated with a quality indicator using a named scale (e.g., HIGH / MED / LOW or equivalent) — distinguishing artifact presence from artifact quality and making per-artifact quality visible at the inventory level before entering any preflight item body | quality-column-inventory | R20-EX-03 |
| C-57 | Prior check field in each preflight dimension item — a structured field recording whether a previous signal check was performed for this topic and dimension, what the prior outcome was, and what has changed since — making check continuity and change-since-last-check visible at the dimension level without external lookup | prior-check-field | R20-EX-04 |

**Extraction rationale:**

**C-54** from V-05's live axis. V-05 adds an Evidence trace field to the VERDICT section that maps each blocking dimension declared in `blocking_dims` to the exact inventory row number from GATHER YOUR SIGNALS and the artifact path. For dimensions with no covering artifact, the Evidence trace writes "not-represented-in-inventory" — declaring absence at the verdict level, not only within the preflight item body. This creates four structural advances not present in V-01 through V-04: (1) closed verdict-to-source loop — the connection between decision and evidentiary basis is traversable at the VERDICT section level without entering any preflight item; (2) row number stability contract — row numbers in GATHER YOUR SIGNALS become functional, not cosmetic, because the Evidence trace cross-references them; (3) absence at verdict level — OPEN dimension closure status is visible without re-entering the dimension analysis section; (4) `evidence_trace` frontmatter — machine-readable cross-checks between `blocking_dims` and inventory row contents without prose parsing. V-01 carries a VERDICT section (Axis G) but no Evidence trace and fails C-54; this confirms C-55 is a precondition for C-54 but does not imply it. V-02 and V-03 carry neither verdict nor evidence trace. V-04 carries verdict block (Axis G) plus quality column (Axis H) but no evidence trace. Boundary confirmed: V-05 passes; V-01 through V-04 fail.

**C-55** from the R20 Axis G signal (V-01, V-04, V-05). Axis G introduces a named VERDICT section — a structured block separate from READINESS SUMMARY — that declares the go/no-go recommendation, names blocking dimensions in a `blocking_dims` field, states the condition for resolution, and is enumerated in the Applies-to scope of STANDING RULES constraints that govern verdict-level output (triggering C-16 compliance). An output whose READINESS SUMMARY contains dimensional status but no separate VERDICT section satisfies C-47 but not C-55: the go/no-go decision is embedded in prose and not addressable as a discrete block. C-55 requires C-12 (four dimensions structured with consistent labeling) as precondition; C-12 does not imply C-55. C-55 is a precondition for C-54; C-55 does not imply C-54. Boundary: variations carrying Axis G pass; variations without Axis G fail.

**C-56** from the R20 Axis H signal (V-02, V-04, V-05). Axis H introduces a Quality column in the artifact inventory table annotating each artifact row with a quality indicator (HIGH / MED / LOW or equivalent named scale), distinguishing artifact presence from artifact quality. V-01 and V-03 carry inventory tables without a Quality column and fail C-56. C-56 is independently testable from C-50: both are independent column additions to the artifact inventory table; neither implies the other. C-56 requires the artifact inventory section to be present as a structural precondition. Boundary: variations carrying Axis H pass; variations without Axis H fail.

**C-57** from the R20 Axis I signal (V-03, V-05). Axis I introduces a Prior check field in each preflight dimension item recording prior check performance, prior outcome, and change-since. V-01, V-02, and V-04 carry preflight dimension items without Prior check fields and fail C-57. C-57 is independently testable: the presence or absence of a Prior check field is structurally observable at the item level without verifying dimension analysis content. C-57 is independently testable from C-50 through C-56. Boundary: variations carrying Axis I pass (V-03, V-05); variations without Axis I fail (V-01, V-02, V-04).

**Round 20 scoring differential (post-extraction):**

| Var | Axis | C-54 | C-55 | C-56 | C-57 | Asp. | Composite |
|-----|------|------|------|------|------|------|-----------|
| V-01 | G | FAIL | PASS | FAIL | FAIL | 46/49 | 99.39 |
| V-02 | H | FAIL | FAIL | PASS | FAIL | 46/49 | 99.39 |
| V-03 | I | FAIL | FAIL | FAIL | PASS | 46/49 | 99.39 |
| V-04 | G+H | FAIL | PASS | PASS | FAIL | 47/49 | 99.59 |
| V-05 | G+H+I + live | PASS | PASS | PASS | PASS | 49/49 | **100.00** |

**Updated parameters:**
- Aspirational denominator: 45 -> **49**
- Formula: `composite = 90 + (aspirational_pass / 49) * 10`
- New subsumption links:
  - `C-12 <- C-55` (C-55 requires C-12; C-12 does not imply C-55)
  - `C-55 <- C-54` (C-54 requires C-55; C-55 does not imply C-54)
  - C-56 independently testable — requires artifact inventory section as structural precondition; independently testable from C-50
  - C-57 independently testable — requires preflight dimension items as structural precondition; independently testable from C-50 through C-56

---

## Criterion additions

| ID | Criterion | Source |
|----|-----------|--------|
| C-50 | The artifact inventory table includes a `Dims` column annotating each listed artifact with its covered check dimensions (C, Sq, St, Co), creating four structural advances: (1) inventory pre-analysis coverage scan — per-dimension coverage is visible before entering any preflight item, so a missing dimension abbreviation predicts OPEN without reading analysis; (2) per-item Dims prediction — each preflight dimension item opens with a prediction derived from the Dims column, creating a feedback loop between inventory and analysis; (3) Dims-driven Thin Coverage cross-item pattern — multi-dimension thin-coverage is detectable from inventory structure alone before STATUS analysis; (4) `dims_coverage` frontmatter — per-dimension artifact counts propagate into machine-readable metadata; an artifact inventory table without a Dims column satisfies the inventory presence requirement but not C-50: per-dimension coverage is not visible before entering the preflight items; C-50 is independently testable: the presence or absence of a Dims column in the inventory table is structurally observable without entering any preflight item or section body; boundary confirmed clean: V-01 through V-04 all use 5-column tables (without Dims column) and fail C-50; no combination of Axes D, E, or F implies C-50; C-50 is independently testable from C-51, C-52, and C-53 | R19-EX-01 |
| C-51 | The CROSS-ITEM PATTERNS section contains a structured pattern block — each cross-item pattern is labeled with a named header or identifier making the pattern type and its diagnostic scope recoverable from a section scan without reading the full pattern prose; an output whose CROSS-ITEM PATTERNS section uses unstructured prose without named pattern labels satisfies C-07 (section present) but not C-51: the reader must read the full section body to identify which patterns are addressed and what their diagnostic scope is; "every cross-item pattern" means each distinct pattern surfaced in the section, without exception; C-51 requires C-07 as a precondition; C-07 does not imply C-51; C-51 is independently testable from C-50, C-52, and C-53; boundary confirmed: variations carrying Axis D pass; variations without Axis D fail | R19-EX-02 |
| C-52 | The MISSING SIGNAL GUIDE entries are ordered by severity — most critical signal gaps (gaps that eliminate dimension coverage entirely, i.e., no artifact covers the dimension) listed before less critical gaps (gaps that thin but do not eliminate coverage) — making the highest-priority guidance immediately accessible without reading the full guide; an output whose MISSING SIGNAL GUIDE names each missing signal type (C-13) without severity ordering satisfies C-08 and C-13 but not C-52: the reader cannot identify priority without reading the full guide; C-52 requires C-08 and C-13 as preconditions; C-08 alone does not imply C-52; C-13 alone does not imply C-52; C-08 and C-13 together do not imply C-52 — severity ordering is independently checkable beyond their satisfaction; C-52 is independently testable from C-50, C-51, and C-53; boundary confirmed: variations carrying Axis E pass; variations without Axis E fail | R19-EX-03 |
| C-53 | STATUS vocabulary uses a five-state taxonomy — at minimum naming five distinct states that separately express: passing coverage, open analysis (artifacts present but analysis incomplete), thin coverage (artifacts present but below threshold), absent coverage (no artifacts covering the dimension), and not-applicable — rather than binary (PASS/FAIL) or three-state vocabulary; the five states enable finer-grained diagnostic resolution that is not expressible in sub-five-state vocabularies: distinguishing artifact absence from thin coverage and open analysis as separate diagnostic states; an output whose STATUS fields use binary or three-state vocabulary satisfies the status-presence requirements but not C-53: the distinctions between artifact absence, thin coverage, and open analysis are collapsed and the reader cannot determine which failure mode applies without reading the full dimension analysis; C-53 requires C-12 (four dimensions structured with consistent labeling) as a precondition; C-12 does not imply C-53; C-53 is independently testable from C-50, C-51, and C-52; boundary confirmed: variations carrying Axis F pass; variations without Axis F fail | R19-EX-04 |
| C-54 | The VERDICT section contains an Evidence trace field mapping each blocking dimension declared in `blocking_dims` to the exact inventory row number from GATHER YOUR SIGNALS and the artifact path (or an explicit "not-represented-in-inventory" declaration for dimensions with no covering artifact) — creating a closed structural loop from decision to source that is traversable without entering any preflight item body; an output whose VERDICT section names blocking dimensions without an Evidence trace field satisfies C-55 but not C-54: the connection between verdict and evidentiary basis requires entering preflight item bodies to establish; absence is declared at the verdict level in the Evidence trace — OPEN dimensions write "not-represented-in-inventory" in the Evidence trace rather than only within the preflight item body, making dimension closure status visible at the verdict level without re-entering analysis; the `evidence_trace` frontmatter field propagates this mapping into machine-readable metadata enabling automated cross-checks between `blocking_dims` and inventory row contents without prose parsing; inventory row numbers in GATHER YOUR SIGNALS are functional, not cosmetic — the Evidence trace cross-reference requires row numbers to match GATHER YOUR SIGNALS table assignments, establishing a row number stability contract; C-54 requires C-55 (VERDICT section) as precondition; C-55 does not imply C-54; C-54 is independently testable from C-50, C-51, C-52, C-53, C-56, and C-57; boundary confirmed: V-05 passes; V-01 through V-04 fail (V-01 and V-04 carry VERDICT without Evidence trace; V-02 and V-03 carry neither) | R20-EX-01 |
| C-55 | The output contains a named VERDICT section — a structured block separate from READINESS SUMMARY that declares the go/no-go recommendation, names blocking dimensions in a `blocking_dims` field, states the condition for recommendation resolution, and is enumerated in the Applies-to scope of all STANDING RULES constraints that govern verdict-level output — creating a single-point decision artifact that is locatable and parseable without reading preflight item bodies or READINESS SUMMARY prose; an output whose READINESS SUMMARY contains dimensional status information but no separate VERDICT section satisfies C-47 but not C-55: the go/no-go decision is embedded in summary prose and is not addressable as a discrete structural block; the `blocking_dims` frontmatter field propagates the verdict into machine-readable metadata; enumeration in STANDING RULES Applies-to fields (C-16) is required for full constraint governance: constraints that govern VERDICT output but omit it from their Applies-to scope violate C-16 without contradicting C-55 — C-16 and C-55 are jointly required for a fully governed VERDICT section; C-55 requires C-12 (four dimensions structured with consistent labeling) as precondition; C-12 does not imply C-55; C-55 is a precondition for C-54; C-55 does not imply C-54; C-55 is independently testable from C-56 and C-57; boundary confirmed: V-01, V-04, V-05 pass; V-02 and V-03 fail | R20-EX-02 |
| C-56 | The artifact inventory table includes a Quality column annotating each listed artifact row with a quality indicator using a named scale (e.g., HIGH / MED / LOW or equivalent) — distinguishing artifact presence from artifact quality and making per-artifact quality visible at the inventory level before entering any preflight item body; an output whose artifact inventory table lists artifacts without a Quality column satisfies the inventory presence requirement but not C-56: artifact quality requires reading preflight item bodies to determine; C-56 is independently testable from C-50 (Dims column): both are independent column additions to the artifact inventory table; presence of a Dims column does not imply a Quality column and presence of a Quality column does not imply a Dims column; the Quality column and Dims column together create a two-signal inventory: per-artifact dimensional coverage and per-artifact quality, both visible at inventory level before entering any preflight item; C-56 requires the artifact inventory section to be present as a structural precondition; C-56 is independently testable from C-54, C-55, and C-57; boundary confirmed: V-02, V-04, V-05 pass; V-01 and V-03 fail | R20-EX-03 |
| C-57 | Each preflight dimension item includes a Prior check field — a structured field recording whether a previous signal check was performed for this topic and dimension, what the prior outcome was, and what has changed since — making check continuity and change-since-last-check visible at the dimension level without external lookup or document search; an output whose preflight dimension items analyze current signals without a Prior check field satisfies the dimension analysis requirements but not C-57: check continuity and change detection require external memory or prior document retrieval; "each preflight dimension item" means all four dimension items (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE), without exception — a Prior check field present in some but not all dimension items fails C-57; C-57 is independently testable: the presence or absence of a Prior check field in preflight dimension items is structurally observable at the item level without verifying dimension analysis content; C-57 is independently testable from C-50, C-51, C-52, C-53, C-54, C-55, and C-56; boundary confirmed: V-03 and V-05 pass; V-01, V-02, and V-04 fail | R20-EX-04 |

## Updated parameters

- Aspirational count: 45 -> **49**
- Formula: `composite = 90 + (aspirational_pass / 49) * 10`
- C-50 independently testable — no precondition in established criterion chain
- C-51 requires C-07 as precondition; C-07 does not imply C-51
- C-52 requires C-08 and C-13 as preconditions; neither individually nor together imply C-52
- C-53 requires C-12 as precondition; C-12 does not imply C-53
- C-55 requires C-12 as precondition; C-12 does not imply C-55
- C-54 requires C-55 as precondition; C-55 does not imply C-54
- C-56 independently testable — requires artifact inventory section as structural precondition; independently testable from C-50
- C-57 independently testable — requires preflight dimension items as structural precondition; independently testable from C-50 through C-56

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
C-12 <- C-53  (C-53 requires C-12; C-12 does not imply C-53)
C-07 <- C-51  (C-51 requires C-07; C-07 does not imply C-51)
C-08 <- C-52  (C-52 requires C-08 and C-13; neither individually nor together imply C-52)
C-13 <- C-52
C-50  (independently testable -- no precondition in established criterion chain)
C-12 <- C-55  (C-55 requires C-12; C-12 does not imply C-55)
C-55 <- C-54  (C-54 requires C-55; C-55 does not imply C-54)
C-56  (independently testable -- requires artifact inventory section as structural precondition)
C-57  (independently testable -- requires preflight dimension items as structural precondition)
```
