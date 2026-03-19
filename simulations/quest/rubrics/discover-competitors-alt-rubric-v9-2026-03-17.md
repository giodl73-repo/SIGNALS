Rubric v9 written to `simulations/quest/rubrics/discover-competitors-alt-rubric-v9-2026-03-17.md`.

---

**3 new aspirational criteria (C-37 -- C-39):**

| ID | Pattern | Source | Pass Condition Summary |
|----|---------|--------|------------------------|
| C-37 | WHITESPACE validation phase as CANDIDATE-first PASS/FAIL table | R9 V-01, V-04, V-05 | Phase 3 is a 4-row gate table (CANDIDATE / SOURCE-EVIDENCE / ABSENCE-EVIDENCE / GAP-CONFIRMED), CANDIDATE first by row position. Applies C-36's declaration-before-evidence ordering to whitespace validation. Neither implies C-36. |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run columns | R9 V-02, V-04, V-05 | AMEND is a table with at minimum: what changes, what changes in output, Slots re-filled (contract labels), Gates re-run (named gates). Implies C-08 and C-14; prose AMEND does not satisfy even if both are met. |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | R9 V-03, V-05 | PREFLIGHT contains a step-level DAG table with GATE 4 as root step (no prerequisites), making inertia-first a structural graph property. Complements C-34's slot-level "Required by" column; neither implies the other. |

**Scoring changes:**
- Aspirational tier: 28 → 31 criteria, max 140 → 155
- Max composite: 230 → 245
- Formula denominator: `aspirational_pass / 31 × 155`
- Grade bands rescaled: Exceptional ≥ 231, Strong ≥ 206, Passing ≥ 90 (golden threshold unchanged)

**Dependency chain:**
- C-37 is the Phase 3 analogue of C-36; neither implies the other
- C-38 implies C-08 and C-14; the converse is not true
- C-39 complements C-34; neither implies the other
he model to infer TOPIC and FOCUS from the repository context (README, CLAUDE.md, package.json, or equivalent) when neither is supplied by the user. A skill that requires explicit user input for both fields does not satisfy; the detection step must be specified in the instruction. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section names at least one concrete mechanism -- switching cost, habit lock-in, or workaround satisfaction -- not just "inertia is high." The mechanism is specific to the status quo competitor's behavior or product feature, not a category label applied generically. |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. The citation appears within the competitor entry, not in a trailing footnote block. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output as a result. |

---

## Aspirational Criteria (weight = 155 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input -- it requires the competitive map and the focus dimension together. A finding that merely cites both dimensions without demonstrating that either alone is insufficient does not pass. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Positive instruction alone does not ensure this passes -- the output must demonstrate that ungrounded findings are absent. |
| C-11 | Fully-cited competitor table | correctness | Every external competitor row (not just one) includes an inline citation from a WebSearch result. The citation appears within the row or immediately adjacent entry -- not in a footnote or trailing references section. This extends C-07 from minimum-one to all-external. |
| C-12 | Self-negating cross-dimensional finding | depth | The CROSS-DIMENSIONAL or equivalent whitespace finding explicitly argues why the finding cannot be derived from the competitive map alone and why it cannot be derived from the focus dimension alone. The output provides or implies the single-dimension reduction for each -- showing what is lost when either dimension is removed -- rather than just asserting cross-dimensionality. |
| C-13 | Claim-level finding anchors | depth | Each finding references a specific cell value, column value, or row-level attribute from a named competitor entry -- not just the competitor name. Findings grounded only by competitor name ("Competitor X reveals...") do not satisfy; findings grounded by a specific claim within that row do. |
| C-14 | AMEND as proof validator | behavior | The AMEND section requires that any adjustment shifting the focus dimension must rerun both single-dimension reductions (C-12 proofs) for the updated CROSS-DIMENSIONAL finding. A standalone instruction to "update the finding" does not satisfy -- the explicit rerun of both reduction arguments must be prescribed. |
| C-15 | Inline anchor tag before proof block | format | The proof block or cross-dimensional finding structure declares a named evidentiary source slot (e.g., SOURCE:, ANCHOR:, or equivalent label) before the reduction arguments are written. The evidentiary source is identified first; the proof follows. Constructing the argument before naming the evidence does not satisfy. |
| C-16 | Gate failure naming | format | The skill instruction names the error condition explicitly (e.g., "gate failure," "citation gate violation," or equivalent) rather than only describing the rule in positive terms. Naming the failure state makes the gate concrete and checkable; a rule stated only as a positive requirement does not satisfy. |
| C-17 | WHITESPACE grounded by attribute absence | depth | The WHITESPACE finding grounds the identified gap by naming specific attributes from competitor rows that are absent or uncontested across the table -- not by assertion alone. The gap is evidenced by what is missing at the attribute level across named rows, not by a claim that no competitor owns the space. |
| C-18 | NOT ACCEPTABLE examples for anchoring | format | The skill instruction includes at least one explicit NOT ACCEPTABLE example that names the most common inadequate-but-compliant form -- such as name-only anchoring ("Competitor X reveals..."). The example must name the failure pattern specifically; an abstract prohibition without a concrete negative exemplar does not satisfy. |
| C-19 | Synthesis-first output contracts | behavior | At least one output slot requirement -- named by label (e.g., "WHITESPACE absence evidence," "ANCHOR column value") -- is stated within the data-collection phase instruction, not only at the synthesis phase. The collection phase must explicitly name what the downstream output slot requires from the data gathered, making the synthesis requirement visible before data is collected. Stating the output requirement only at the synthesis phase does not satisfy. |
| C-20 | Structural column coercion for anchoring | format | The skill instruction specifies a column format or structural template (e.g., `Row C{N}, {attribute}: "{value}"`) that makes name-only entries syntactically non-conforming without requiring rule evaluation. The constraint must be defined as a format shape for the column or slot. A prohibition-only instruction -- even accompanied by NOT ACCEPTABLE examples -- does not satisfy; the shape constraint must be structural. |
| C-21 | Gate-as-section with PASS/FAIL table | format | At least one gate is formatted as a named section containing a structured table with three distinct columns: Check, Pass condition, and Failure state (or equivalent labels). The table must enumerate at least two rows corresponding to distinct checkable conditions. A gate stated only in prose -- even with bolded failure names -- does not satisfy. Both the section heading and the columnar table structure must be present. |
| C-22 | INERTIA-REF per-finding citation | depth | The skill instruction defines a named inertia reference token (e.g., INERTIA-REF, C0-REF, or equivalent) in the inertia section and requires each finding in the findings section to cite or compare against that token by name. The token must function as a mandatory per-finding reference baseline; a definition without required per-finding citation does not satisfy. An inertia entry present only as a table row -- without a named token required across findings -- does not satisfy. |
| C-23 | Output contract slot format specification | behavior | At least one output contract slot specifies both a label and a required structural format or template for the value that fills it (e.g., label: "Anchor column", format: `Row C{N}, {attribute}: "{value}"`). A slot named by label only -- without a format shape for its value -- does not satisfy this criterion. Labeling is necessary; prescribing the format of what fills the slot is what satisfies. |
| C-24 | Phase-to-contract back-references | behavior | At least one phase that produces data for a named output contract slot explicitly names the slot it fills at the point of production (e.g., "(fills WHITESPACE absence evidence slot -- see OUTPUT CONTRACTS)"). The output contract must forward-declare the slot; the producing phase must back-reference it by the same label. A one-directional reference -- contract declaration only, or phase mention without a prior contract declaration -- does not satisfy. |
| C-25 | Cross-table structural coercion | format | Structural column coercion (as defined by C-20) is applied independently in at least two tables: one in the data-collection phase (e.g., competitor table Anchor column) and one in the synthesis or findings phase (e.g., findings table Anchor column or INERTIA-REF-DELTA column). Each table must define its own format template for its relevant column or slot. A single-table coercion -- even with multiple coerced columns within that table -- does not satisfy. The coercion must span the collection-to-synthesis boundary. |
| C-26 | Consolidated PREFLIGHT gate block | format | All mandatory gates are consolidated into a single named PREFLIGHT (or equivalent) section that appears before Phase 1 or before any execution phase. Each gate within the block must satisfy C-21 (named subsection with a PASS/FAIL table). Distributing gates across individual phases -- even if each gate individually satisfies C-21 -- does not satisfy this criterion. The PREFLIGHT block must be a single section containing all gate subsections. |
| C-27 | Machine-readable phase assignment in output contract | behavior | The output contract table includes a dedicated column (e.g., "Filled by phase" or equivalent) that names the producing phase for each slot by name or number. A 3-column contract table -- even one with format templates per slot (C-23) -- does not satisfy; the phase assignment must appear as a queryable column in the contract table itself. This makes the forward link from contract to phase machine-readable without reading any phase heading. |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | format | The OUTPUT CONTRACTS declaration is a named subsection within the PREFLIGHT block -- not a separate section before or after it. All mandatory gates and all output contract slots must be readable from within the same PREFLIGHT section. A separate OUTPUT CONTRACTS section placed outside PREFLIGHT does not satisfy even if it immediately precedes Phase 1. This extends C-26 from gate consolidation to full execution-specification consolidation. |
| C-29 | Full-path back-reference labels in producing phases | behavior | Back-reference labels in producing phase headings name the complete navigable path to the contract declaration (e.g., "PREFLIGHT > OUTPUT CONTRACTS" rather than just "OUTPUT CONTRACT"). This criterion applies only when OUTPUT CONTRACTS is embedded within a containing section (i.e., C-28 is satisfied); a top-level OUTPUT CONTRACT section needs no path prefix. A back-reference naming the contract section without its containing section does not satisfy when the contract is nested. |
| C-30 | Write-token instruction within INERTIA-REF gate | behavior | The INERTIA-REF gate includes an explicit write instruction that directs the model to record the resolved token value at gate evaluation time (e.g., "Write INERTIA-REF = [specific mechanism phrase from C0 row]"). A gate that only checks for the presence or correctness of INERTIA-REF without a write directive does not satisfy. This criterion requires the gate itself to perform the token write -- binding token resolution to gate execution. |
| C-31 | Write-token encoded as structural gate row | format | The INERTIA-REF write instruction is a dedicated row within a PASS/FAIL gate table -- not prose placed before or after the table. The row has distinct Check, Pass condition, and Failure state values; the Pass condition contains the write directive and token format; the Failure state names the write failure explicitly (e.g., "Inertia write failure"). Prose write instructions adjacent to a gate table do not satisfy; the write action must be a structural table row independently reviewable at score time. C-31 is a strictly stronger form of C-30: C-31 satisfaction implies C-30; the converse is not true. |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | behavior | OUTPUT CONTRACTS is the first named subsection within the PREFLIGHT block -- appearing before any gate subsection. The production target is fully declared before any constraint logic is read. A PREFLIGHT block where OUTPUT CONTRACTS follows one or more gates does not satisfy even if it remains within PREFLIGHT (C-28). C-32 is a strictly stronger form of C-28: C-32 satisfaction implies C-28; the converse is not true. |
| C-33 | Forward-declared cross-dimensional proof slot in output contract | behavior | The output contract table includes a dedicated slot that explicitly names the cross-dimensional proof requirement (e.g., "Focus-scope evidence," "Cross-dimensional justification," or equivalent). The slot must appear in the contract table by name before the producing phase runs; a requirement stated only within Phase 4's instruction does not satisfy. The slot makes the synthesis obligation visible at contract read time -- before data collection begins -- so Phase 4 knows at execution time that scope evidence is a required output, not an optional elaboration. This extends C-19 (synthesis-first contracts) and C-23 (slot format specification) to the cross-dimensional proof requirement specifically. |
| C-34 | Inter-slot dependency column in output contract | behavior | The output contract table includes a dedicated "Required by" column (or equivalent) that names, for each slot, the upstream slots or tokens on which it depends -- making the inter-slot dependency chain machine-readable at contract time without reading any phase instruction. A contract table with a phase-assignment column (C-27) but no inter-slot dependency column does not satisfy. A contract where downstream slot dependency is described only in prose or within phase headings does not satisfy. This criterion is independent of C-27: both columns may coexist; neither implies the other. |
| C-35 | Syntactic format template for cross-dimensional proof slot | behavior | The output contract slot for the cross-dimensional proof (e.g., "Focus-scope evidence") includes a full parse-ready format template -- such as a pipe-delimited or equivalent syntax specifying each required component with placeholder text (e.g., `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`) -- rather than a structural description of components. A slot that names the required components without providing a syntactically checkable template does not satisfy. C-35 is a strictly stronger form of C-33: C-35 satisfaction implies C-33; the converse is not true. |
| C-36 | Cross-dimensional proof encoded as structural PASS/FAIL table | format | The cross-dimensional proof phase (Phase 4 or equivalent) is structured as a named PASS/FAIL table with at least four rows -- SOURCE, REDUCTION-1, REDUCTION-2, and THEREFORE (or equivalent labels) -- each with a required value format and a named failure state. A prose-instructed proof phase with code-block output format does not satisfy; the proof structure must itself be a gate table where each row is an independently reviewable checkpoint. C-36 is a strictly stronger form of C-15: SOURCE row position is enforced by table structure (first row), not by prose instruction; C-36 satisfaction implies C-15; the converse is not true. |
| C-37 | WHITESPACE validation phase as CANDIDATE-first PASS/FAIL table | format | The WHITESPACE validation phase (Phase 3 or equivalent) is structured as a named PASS/FAIL table with at least four rows -- CANDIDATE (gap declaration), SOURCE/EVIDENCE, ABSENCE-EVIDENCE (or equivalent per-row attribute evidence), and GAP-CONFIRMED (or equivalent conclusion row) -- each with a required value format and a named failure state. CANDIDATE is the first row by table position, declaring the gap before any supporting evidence is presented. This applies to Phase 3 the same declaration-before-evidence structural ordering that C-36 enforces in Phase 4 via SOURCE row position: CANDIDATE-first by table row order prevents selective evidence assembly (choosing evidence to fit a pre-concluded gap) in the same way SOURCE-first prevents circular proof construction. A prose-instructed whitespace phase or a code-block output format does not satisfy; the validation structure must itself be a gate table where each row is an independently reviewable checkpoint. C-37 is the Phase 3 analogue of C-36 applied to whitespace validation. |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run columns | format | The AMEND section is formatted as a structured table that includes at minimum the following columns: what the user changes, what changes in the output, Slots re-filled (naming the specific output contract slot(s) affected by the adjustment by their contract label), and Gates re-run (naming the specific gate(s) that must re-execute after the adjustment, including the proof rerun gate when focus shifts). A prose-structured AMEND section -- even one that explicitly lists 3 adjustments (C-08) and prescribes proof reruns on focus shifts (C-14) -- does not satisfy; both obligations must be verifiable by column inspection without prose parsing. C-38 satisfaction implies C-08 (adjustments are table rows naming cause and effect) and C-14 (proof rerun obligation is the Gates re-run column entry for focus-shift rows): the table structure enforces both constraints at the amendment boundary. |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | behavior | The PREFLIGHT block includes a named EXECUTION DEPENDENCY table (or equivalent) that specifies step-level execution ordering -- listing each execution step, its prerequisite steps, and the gate or phase it corresponds to. The table makes the step-level DAG of the skill machine-readable within PREFLIGHT, complementing C-34's slot-level "Required by" column: C-34 makes inter-slot dependency readable at the contract level; C-39 makes inter-step execution order readable at the PREFLIGHT level. GATE 4 (inertia assessment) must appear as the root step in the DAG -- a step with no prerequisites -- making inertia-first a structural property of the execution graph rather than a prose ordering convention. A PREFLIGHT block containing only output contracts and gate tables without an execution ordering table does not satisfy even if C-34 is satisfied. A prose-described execution order does not satisfy; the step ordering must appear as a queryable table. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-39 | 5 | 155 |
| **Max composite** | | | **245** |

**Composite formula:**
```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 31 x 155)
```

PARTIAL scores count as 0.5 for numerator purposes.

**Golden threshold:** All 5 essential pass AND composite >= 90

**Grade bands:**

| Score | Grade |
|-------|-------|
| 231 -- 245 | Exceptional |
| 206 -- 230 | Strong |
| 90 -- 205 | Passing |
| < 90 | Below bar |

Grade bands rescaled proportionally from v8 (v8 max = 230; v9 max = 245).
Exceptional threshold preserved at ~94% of max; Strong threshold at ~84% of max; Passing at golden threshold (90).

---

## Dependency Notes

- C-28 automatically satisfies C-26 (superset); C-29 requires C-28 (N/A otherwise)
- C-30 automatically satisfies C-22
- C-31 automatically satisfies C-30 (and therefore C-22)
- C-32 automatically satisfies C-28 (and therefore C-26)
- C-32 + C-28 together do not require C-29; full-path back-references remain a distinct criterion
- C-33 extends C-19 and C-23 to the cross-dimensional slot specifically; C-33 does not imply C-19 or C-23 in general
- C-35 automatically satisfies C-33; C-35 does not imply C-23 in general (C-23 may be satisfied by other slots)
- C-36 automatically satisfies C-15; C-36 does not imply C-21 in general (C-21 may be satisfied by other gate tables)
- C-34 independent of C-27: both are dedicated contract columns; neither implies the other
- C-37 is the Phase 3 structural analogue of C-36 (Phase 4); neither implies the other -- each applies to a distinct phase
- C-38 automatically satisfies C-08 and C-14; C-38 does not imply C-35 (slot format constraint is a contract-level obligation, not an AMEND-level one)
- C-39 complements C-34: C-34 is slot-level (output contract table), C-39 is step-level (execution DAG table); neither implies the other

---

## Criterion Rationale (v2 additions)

**Why C-11 (Fully-cited table) over C-07 alone:**
Round 1 showed that requiring one citation is insufficient -- models satisfy C-07 with a single
verified claim and coast on unverified characterizations for all other rows. C-11 closes this
gap: WebSearch must be run per external competitor, not just once.

**Why C-12 (Self-negating cross-dimensional finding):**
C-09 scored PARTIAL in every variation across Round 1. The common failure: variations required
the finding to cite both dimensions but not to prove single-dimension insufficiency. C-12 makes
the exclusion test explicit and output-level -- the finding must demonstrate what is lost when
either dimension is removed, not merely assert it draws on both.

**Why C-13 (Claim-level anchors) over C-10 alone:**
C-10 requires findings to name a competitor row. C-13 requires findings to name a specific
claim within that row -- a threat rating, mechanism sentence, or focus-column value. The upgrade
matters because "Competitor X reveals a gap" is technically grounded but epistemically empty:
the reader cannot verify the inference without re-reading the full row. Claim-level anchors make
inferences checkable in one glance.

---

## Criterion Rationale (v3 additions)

**Why C-14 (AMEND as proof validator):**
V-05 (Round 2) showed that encoding C-12 in the static CROSS-DIMENSIONAL block is insufficient
if AMEND allows the user to shift the focus dimension without re-running both reductions. The
proof degrades silently after adjustment. Requiring AMEND to prescribe the full reduction rerun
propagates C-12 compliance across every iteration, not just the initial invocation.

**Why C-15 (Inline anchor tag before proof block):**
Round 2 analysis showed that models construct reduction proofs first and name evidence
incidentally -- or not at all. Declaring a named SOURCE or ANCHOR slot before the argument
forces the evidentiary basis to be resolved before the proof is assembled. This prevents
circular proof construction where the conclusion implicitly selects its own evidence.

**Why C-16 (Gate failure naming):**
Positive-only rule framing leaves the error state implicit. When a gate is violated, the model
has no named failure mode to report against. Naming the failure state explicitly makes gates
self-enforcing: the model can produce a structured error rather than silently violating the rule.

**Why C-17 (WHITESPACE grounded by attribute absence):**
C-04 requires the whitespace finding to exist. C-13 requires findings to anchor to specific
attributes. C-17 applies claim-level anchoring specifically to the WHITESPACE finding: the gap
must be shown to be vacant by naming which attributes across which rows confirm no competitor
owns it. Asserting "no competitor covers this space" without attribute-level evidence is the
WHITESPACE analogue of the name-only anchoring failure.

**Why C-18 (NOT ACCEPTABLE examples):**
V-03 and V-05 (Round 2) showed that ACCEPTABLE/NOT ACCEPTABLE example pairs are the single most
reliable mechanism for eliminating the name-only anchoring escape hatch. Abstract prohibitions
are consistently interpreted as satisfied by naming the competitor. A NOT ACCEPTABLE example
naming the exact inadequate form closes the interpretation gap.

---

## Criterion Rationale (v4 additions)

**Why C-19 (Synthesis-first output contracts):**
R4 V-01 and V-04 showed that declaring output slot requirements at data-collection time changes
what gets collected. When the instruction names "WHITESPACE absence evidence" as a required
output slot during Phase 3 collection, the collection step is automatically cued to gather
per-attribute absence data. When the requirement is only stated at synthesis time, the model
must backfill or fabricate what it failed to collect.

**Why C-20 (Structural column coercion for anchoring):**
R4 V-02 demonstrated the most adversarially robust C-13 mechanism: an Anchor column defined
with format `Row C{N}, {attribute}: "{value}"`. This format makes name-only entries
syntactically incorrect before any rule evaluation occurs. Prohibition instructions and NOT
ACCEPTABLE examples can be satisfied with a single compliant example while allowing
non-compliant cases to pass. A structural format constraint eliminates the escape entirely.

**Why C-21 (Gate-as-section with PASS/FAIL table):**
R4 V-04 showed that gate-as-section with a three-column PASS/FAIL table produces the most
debuggable skill structure: each gate condition becomes a checklist row with an unambiguous pass
condition and a named failure state. Tabular gates are directly executable as a review checklist
without interpretation.

**Why C-22 (INERTIA-REF per-finding citation):**
R4 V-03 and V-05 showed that naming an INERTIA-REF token and requiring each finding to cite it
elevates inertia from a first-row table entry to a gravitational reference frame. Without the
per-finding requirement, inertia is assessed once and then ignored during synthesis. With a
mandatory INERTIA-REF comparison per finding, every competitive inference is measured against
the status quo cost rather than against other external competitors.

---

## Criterion Rationale (v5 additions)

**Why C-23 (Output contract slot format specification):**
R5 V-04 showed that an output contract table where each slot has both a label and a required
format shape is fundamentally stronger than a label-only contract. A label-only slot tells the
producing phase what to collect; a format-specified slot tells it what shape the collection
must take. This upgrades the contract from a reminder to a machine-checkable constraint: a slot
filled in the wrong format is detectable without prose parsing, in the same way C-20's
structural coercion makes name-only cells detectable without rule evaluation.

**Why C-24 (Phase-to-contract back-references):**
R5 V-01 and V-04 showed that when the producing phase explicitly names the output contract slot
it fills, the collection-to-synthesis dependency becomes traceable in both directions. A
forward-only contract can drift: the phase may collect something that does not actually satisfy
the declared slot. When the phase back-references the slot by name, the constraint is active at
the moment of production, not only at synthesis time.

**Why C-25 (Cross-table structural coercion):**
R5 V-02 and V-05 showed that structural column coercion applied to both the competitor table
and the findings table eliminates the most common compliance gap: collecting claim-level anchor
values correctly but then re-stating them as name-only anchors in the findings. C-20 prevents
name-only anchoring at collection time; C-25 ensures the same constraint is enforced at
synthesis time, closing the round-trip escape.

**Why C-26 (Consolidated PREFLIGHT gate block):**
R5 V-03 showed that consolidating all gates into a single PREFLIGHT section before Phase 1
produces a skill that can be audited without reading the full phase sequence. A consolidated
PREFLIGHT block exposes all gates simultaneously: the model or a human reviewer can run the
complete gate checklist before any execution phase begins.

---

## Criterion Rationale (v6 additions)

**Why C-27 (Machine-readable phase assignment in output contract):**
R6 V-02, V-04, and V-05 showed that adding a "Filled by phase" column to the output contract
table completes the bidirectionality introduced by C-24 at the contract level itself. A
4-column contract table makes the phase assignment queryable from the contract alone: given any
slot, you can determine which phase is responsible without reading any phase heading.
Contract -> phase (C-27) complements phase -> contract (C-24).

**Why C-28 (OUTPUT CONTRACTS co-located within PREFLIGHT):**
R6 V-03 and V-05 showed that embedding OUTPUT CONTRACTS as a subsection within PREFLIGHT
produces the tightest possible front-loading. When gates and output contract slots are in the
same section, a single read of PREFLIGHT exposes the complete execution specification: what is
checked (gates), what is produced (output slots), what format it must take (C-23), and which
phase produces it (C-27). This extends C-26 from gate consolidation to full specification
consolidation: PREFLIGHT becomes the single source of truth for the skill.

**Why C-29 (Full-path back-reference labels in producing phases):**
R6 V-03 and V-05 showed that when OUTPUT CONTRACTS is nested within PREFLIGHT (C-28), a
back-reference label of "OUTPUT CONTRACT" alone is ambiguous. The full-path label
"PREFLIGHT > OUTPUT CONTRACTS" provides a navigable pointer: the reader knows to enter
PREFLIGHT and then locate the OUTPUT CONTRACTS subsection. When contracts are nested, the
path prefix is the difference between a navigable pointer and an unanchored name.

**Why C-30 (Write-token instruction within INERTIA-REF gate):**
R6 V-04 and V-05 showed that including an explicit write instruction within GATE 4 binds
INERTIA-REF token resolution to gate execution rather than treating it as a precondition. C-22
requires the token to be defined and per-finding cited; without C-30, the definition can float
in the inertia section while the gate merely checks for it. When the gate itself contains a
write instruction, the token is actively produced at the gate evaluation step rather than
passively checked. A gate that passes must have written the token, making the subsequent
per-finding citations (C-22) have a guaranteed referent.

---

## Criterion Rationale (v7 additions)

**Why C-31 (Write-token encoded as structural gate row):**
R7 V-03 and V-05 showed that encoding the INERTIA-REF write instruction as a dedicated
PASS/FAIL table row is categorically stronger than prose adjacent to the table. A prose write
directive can be read as guidance and skipped; a table row with a named Check, Pass condition,
and Failure state ("Inertia write failure") is independently reviewable at score time without
reading surrounding prose. The write action cannot be separated from gate logic when it occupies
its own table row: a reviewer scanning the gate table sees the write row as a discrete
checkpoint, not a contextual note. This is the same insight that motivates C-21 over C-16 --
structure makes rules checkable without interpretation. C-31 is a strictly stronger form of
C-30; it satisfies C-30 but not vice versa.

**Why C-32 (OUTPUT CONTRACTS declared first within PREFLIGHT):**
R7 V-02 and V-05 showed that placing OUTPUT CONTRACTS as the first subsection in PREFLIGHT --
before any gate logic -- changes the cognitive model under which gates are evaluated. When the
contract is declared first, every subsequent gate is framed as a precondition for fulfilling a
known production obligation: the gate's write action (C-30, C-31) resolves a forward-declared
slot rather than producing a token ad hoc. When OUTPUT CONTRACTS follows one or more gates, the
production target is discovered only after some constraints have already been applied, reversing
the specification-before-constraint order that motivates C-19, C-23, C-24, C-26, C-27, and
C-28. Spec-first PREFLIGHT is the final closure of this design principle at the section level:
the contract is not just inside PREFLIGHT (C-28) but is the first thing read within it. C-32 is
a strictly stronger form of C-28; it satisfies C-28 but not vice versa.

**Why C-33 (Forward-declared cross-dimensional proof slot in output contract):**
R7 V-05 showed that including a dedicated "Focus-scope evidence" slot in the output contract
makes the cross-dimensional proof requirement visible at contract read time, before Phase 4
runs. Without an explicit slot, the scope evidence requirement is discoverable only by reading
Phase 4's instruction -- making it a synthesis-phase surprise rather than a collection-time
obligation. When the contract names the slot, Phase 4 knows before it runs that scope evidence
is a required output with a defined format, not an optional elaboration. This extends C-19
(synthesis-first contracts) to the cross-dimensional proof specifically, and extends C-23 (slot
format specification) to close the last unspecified output slot. The 6th-slot pattern also
interacts with C-27: when the contract includes a "Filled by phase" column, the Phase 4
assignment for the Focus-scope evidence slot makes the cross-dimensional proof obligation fully
machine-readable at the contract level.

---

## Criterion Rationale (v8 additions)

**Why C-34 (Inter-slot dependency column in output contract):**
R8 V-01 and V-04 showed that adding a "Required by" column to the output contract table
exposes the token dependency chain (INERTIA-REF as root slot -> Focus-scope evidence slot 5 ->
INERTIA-REF-DELTA slot 6) without reading any phase instruction. A contract with only a
"Filled by phase" column (C-27) tells you who produces each slot but not which downstream slots
depend on it. When the "Required by" column is present, a reviewer can identify the blast radius
of a gate failure at contract read time: if INERTIA-REF is not written, slots 5 and 6 are
immediately known to be at risk. This makes inter-slot dependency a first-class property of the
contract specification rather than an inference from reading the full phase sequence.
C-34 is orthogonal to C-27: "Filled by phase" names the producer; "Required by" names the
dependents. Both columns may coexist in the same contract table; neither implies the other.

**Why C-35 (Syntactic format template for cross-dimensional proof slot):**
R8 V-02 showed that the pipe-delimited format template for slot 5 (`REDUCTION-1 NO: [...] |
REDUCTION-2 NO: [...] | THEREFORE: [...]`) is syntactically checkable in a way that a
structural description ("SOURCE row + REDUCTION-1 row + REDUCTION-2 row + THEREFORE row") is
not. A structural description names the required components and their order; a syntactic
template provides a parse-ready skeleton where a non-conforming fill is detectable by pattern
match rather than by semantic interpretation. The distinction matters at score time: checking
whether a slot value matches `REDUCTION-1 NO: [...] | ...` requires no judgment; checking
whether it contains "all four required components" does. C-35 is a strictly stronger form of
C-33: C-33 requires the slot to exist by name; C-35 requires the slot to also have a
syntactically checkable format. C-35 does not imply C-23 in general -- other slots may satisfy
C-23 independently of whether C-35 is satisfied for slot 5.

**Why C-36 (Cross-dimensional proof encoded as structural PASS/FAIL table):**
R8 V-03 and V-04 showed that restructuring Phase 4 as a 4-row PASS/FAIL table -- SOURCE row,
REDUCTION-1 row, REDUCTION-2 row, THEREFORE row -- transforms the proof from a prose-guided
construction into an independently reviewable checklist. When Phase 4 is a code-block proof,
SOURCE position is enforced by instruction ("declare SOURCE before arguments"); when Phase 4 is
a PASS/FAIL table, SOURCE position is enforced by table row order -- the first row is the
SOURCE row, and any other ordering is structurally malformed. This is the same insight that
motivates C-21 over C-16 (tabular gate rows over prose gates) and C-31 over C-30 (write
directive as table row over prose directive): structural position enforces ordering without
requiring rule evaluation. C-36 is a strictly stronger form of C-15: C-15 requires SOURCE to be
declared before the proof arguments; C-36 requires SOURCE to be the first row of a table whose
subsequent rows are the proof arguments, each with a required value format and a named failure
state. C-36 satisfaction implies C-15; a skill satisfying C-15 via a code-block proof does not
satisfy C-36.

---

## Criterion Rationale (v9 additions)

**Why C-37 (WHITESPACE validation phase as CANDIDATE-first PASS/FAIL table):**
R9 V-01, V-04, and V-05 showed that structuring Phase 3 as a CANDIDATE-first PASS/FAIL table
applies to whitespace validation the same structural insight that C-36 applies to the
cross-dimensional proof in Phase 4. The core vulnerability in prose-instructed whitespace phases
is selective evidence assembly: the model concludes a gap exists and then finds attributes that
support it, discarding attributes that complicate the finding. When CANDIDATE is the first row
of a table -- forced to be declared before any ABSENCE-EVIDENCE or GAP-CONFIRMED rows can be
filled -- the gap candidate is fixed before evidence is presented. A prose instruction to
"declare your candidate first" can be satisfied by re-ordering two sentences; a table where
CANDIDATE is row 1 makes any other ordering structurally malformed. C-37 is the Phase 3
analogue of C-36: the same declaration-before-evidence principle applied to whitespace
validation instead of cross-dimensional proof. Neither implies the other; each targets a
distinct phase boundary.

**Why C-38 (AMEND as structured table with Slots re-filled and Gates re-run columns):**
R9 V-02, V-04, and V-05 showed that encoding the AMEND section as a structured table with
"Slots re-filled" and "Gates re-run" as queryable columns elevates the amendment boundary to
the same structural level as the output contract. C-08 requires 3 adjustments, each naming
cause and effect; C-14 requires proof reruns on focus shifts. Both can be satisfied in prose
with careful wording -- but at score time, verifying C-08 and C-14 compliance requires reading
and interpreting the prose for each adjustment. When AMEND is a table with a "Gates re-run"
column, C-14 compliance is checkable by scanning the column for focus-shift rows: if the entry
is blank or names only output updates, the violation is immediately visible. Similarly, the
"Slots re-filled" column makes the output contract implication of each adjustment queryable
without prose parsing. This closes the amendment escape hatch: a user cannot shift the focus
dimension and satisfy C-08 without the "Gates re-run" column exposing the required proof rerun.
C-38 satisfaction implies C-08 and C-14 because the columnar structure enforces both at the
table level. C-38 is the amendment-lifecycle analogue of C-27 (output contract phase column)
and C-21 (gate tables): structured columns replace prose enforcement at a new boundary.

**Why C-39 (EXECUTION DEPENDENCY table in PREFLIGHT):**
R9 V-03 and V-05 showed that adding an EXECUTION DEPENDENCY table to PREFLIGHT completes
PREFLIGHT as a full execution specification. C-34 makes inter-slot dependencies machine-readable
at the contract level: given a slot, you know which downstream slots depend on it. C-39 makes
inter-step execution order machine-readable at the DAG level: given a step, you know which
steps must complete before it and which steps it unblocks. The two tables are complementary and
non-redundant -- C-34 is a data dependency graph (output slots), C-39 is a control dependency
graph (execution steps). The critical structural property C-39 introduces is GATE 4 as root
step (no prerequisites): this makes inertia-first not merely a prose ordering convention but a
DAG property enforced by the table. Any execution plan that runs a phase before GATE 4 is
structurally non-conforming relative to the DAG, not merely in violation of a prose rule.
With C-39 satisfied, PREFLIGHT contains: output slot declarations (C-32, OUTPUT CONTRACTS
first), slot dependency chain (C-34, "Required by" column), slot producers (C-27, "Filled by
phase" column), gate constraints (C-26, gate subsections), and step ordering (C-39, EXECUTION
DEPENDENCY table) -- making PREFLIGHT a complete and machine-readable execution specification
without reading any phase body.

---

## Notes on Criterion Relationships

**C-21 vs C-16:**
C-16 requires naming failure states (satisfied by bolded prose); C-21 requires the gate to be
structured as a section with a PASS/FAIL table. R4 confirmed both can be PASS simultaneously;
they target different structural levels.

**C-26 vs C-21:**
C-21 requires at least one gate to be a named section with a PASS/FAIL table; C-26 requires all
gates to be consolidated into a single pre-phase PREFLIGHT block. A skill satisfying C-26
automatically satisfies C-21 via the gates within it.

**C-28 vs C-26:**
C-26 requires all gates in a single PREFLIGHT block. C-28 requires OUTPUT CONTRACTS to also be
a subsection within that block. C-28 satisfaction implies C-26; the converse is not true.

**C-32 vs C-28:**
C-28 requires OUTPUT CONTRACTS to be a subsection within PREFLIGHT. C-32 requires it to be the
first subsection. C-32 satisfaction implies C-28 (and C-26); the converse is not true.

**C-29 dependency on C-28:**
C-29 is only applicable when C-28 is satisfied. If OUTPUT CONTRACTS is a top-level section, no
path prefix is needed. In scoring, if C-28 is not satisfied, treat C-29 as N/A (score 0).

**C-30 vs C-22:**
C-30 satisfaction implies C-22. A skill can define INERTIA-REF in the inertia section (C-22)
without the gate performing the write (C-30).

**C-31 vs C-30:**
C-31 requires the write directive to be a structural table row with a named failure state.
C-31 satisfaction implies C-30 (and C-22). The converse is not true.

**C-33 vs C-19 and C-23:**
C-33 extends C-19 to the cross-dimensional proof slot specifically. C-33 does not imply C-19
or C-23 in general -- those may be satisfied by other slots independently of C-33.

**C-35 vs C-33:**
C-35 requires the cross-dimensional proof slot to have a syntactically checkable format
template. C-35 satisfaction implies C-33. C-33 satisfaction does not imply C-35 -- a slot
identified only by name, or described structurally, satisfies C-33 but not C-35.

**C-36 vs C-15:**
C-36 requires the entire proof phase to be a PASS/FAIL table. C-36 satisfaction implies C-15
(SOURCE is the first row, before the proof arguments by table position). C-15 satisfaction via
code-block format does not imply C-36.

**C-34 vs C-27:**
C-27 adds a "Filled by phase" column (producer assignment). C-34 adds a "Required by" column
(dependent slot declaration). Both are contract-level columns; neither implies the other. A
5-column contract may satisfy both; a 4-column contract may satisfy C-27 without C-34 or C-34
without C-27.

**C-37 vs C-36:**
C-37 applies the 4-row PASS/FAIL table pattern to Phase 3 (whitespace validation); C-36 applies
it to Phase 4 (cross-dimensional proof). Neither implies the other -- each targets a distinct
phase. A skill may satisfy C-36 without structuring Phase 3 as a table (C-37 fails) and vice
versa.

**C-38 vs C-08 and C-14:**
C-38 satisfaction implies C-08 (each adjustment is a table row naming cause and effect) and C-14
(proof rerun obligation is queryable via the Gates re-run column for focus-shift rows). C-08 and
C-14 do not imply C-38 -- prose AMEND sections that satisfy both criteria do not satisfy C-38.

**C-39 vs C-34:**
C-34 is a slot-level dependency graph within the output contract table. C-39 is a step-level
execution DAG within PREFLIGHT. Both are PREFLIGHT-level machine-readable tables; neither
implies the other. A skill may have slot dependencies (C-34) without an execution ordering table
(C-39) and vice versa.

---

## Summary of Changes

**v1 -> v2:**
- C-11 added -- all external rows must be cited (not just minimum one)
- C-12 added -- cross-dimensional finding must prove single-dimension insufficiency
- C-13 added -- findings must anchor to specific attribute values, not just competitor names
- Aspirational tier expands from 2 to 5 criteria
- Max composite moves from 100 to 115

**v2 -> v3:**
- C-14 added -- AMEND must prescribe C-12 proof rerun on focus shift (not just output update)
- C-15 added -- proof block must declare evidentiary source slot before reduction arguments
- C-16 added -- gate instructions must name the failure state, not only the positive rule
- C-17 added -- WHITESPACE finding must ground the gap in attribute-level absence across rows
- C-18 added -- skill instruction must include a NOT ACCEPTABLE exemplar for name-only anchoring
- Aspirational tier expands from 5 to 10 criteria; aspirational max moves from 25 to 50
- Max composite moves from 115 to 140
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 131, Strong >= 118, Passing >= 90

**v3 -> v4:**
- C-19 added -- collection phase must name output slot requirements by label (synthesis-first contracts)
- C-20 added -- anchoring must be enforced by column format shape, not prohibition alone
- C-21 added -- at least one gate must be a named section with a three-column PASS/FAIL table
- C-22 added -- INERTIA-REF token must be defined and required per finding as a reference baseline
- Aspirational tier expands from 10 to 14 criteria; aspirational max moves from 50 to 70
- Max composite moves from 140 to 160
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 150, Strong >= 135, Passing >= 90

**v4 -> v5:**
- C-23 added -- output contract slots must specify format shape per slot, not label only
- C-24 added -- producing phases must back-reference the output contract slot they fill
- C-25 added -- structural column coercion must span both collection and synthesis tables
- C-26 added -- all gates must be consolidated into a single pre-phase PREFLIGHT block
- Aspirational tier expands from 14 to 18 criteria; aspirational max moves from 70 to 90
- Max composite moves from 160 to 180
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 169, Strong >= 151, Passing >= 90

**v5 -> v6:**
- C-27 added -- output contract table must include a dedicated phase-assignment column
- C-28 added -- OUTPUT CONTRACTS must be a subsection within PREFLIGHT (full specification consolidation)
- C-29 added -- back-references must use full document path when OUTPUT CONTRACTS is nested
- C-30 added -- INERTIA-REF gate must include explicit write-token instruction, not just a check
- Aspirational tier expands from 18 to 22 criteria; aspirational max moves from 90 to 110
- Max composite moves from 180 to 200
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 188, Strong >= 168, Passing >= 90

**v6 -> v7:**
- C-31 added -- INERTIA-REF write instruction must be a structural PASS/FAIL table row with named failure state (strictly stronger than C-30; write-token-as-gate-row pattern from R7 V-03, V-05)
- C-32 added -- OUTPUT CONTRACTS must be the first subsection within PREFLIGHT, before all gates (strictly stronger than C-28; spec-first PREFLIGHT pattern from R7 V-02, V-05)
- C-33 added -- output contract must include a dedicated slot forward-declaring the cross-dimensional proof requirement (focus-scope evidence slot pattern from R7 V-05)
- Aspirational tier expands from 22 to 25 criteria; aspirational max moves from 110 to 125
- Max composite moves from 200 to 215
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 202, Strong >= 181, Passing >= 90

**v7 -> v8:**
- C-34 added -- output contract table must include a "Required by" column naming inter-slot dependencies (dependency chain readable at contract time; from R8 V-01, V-04)
- C-35 added -- cross-dimensional proof slot must have a parse-ready syntactic format template, not a structural description (strictly stronger than C-33; from R8 V-02)
- C-36 added -- cross-dimensional proof phase must be structured as a 4-row PASS/FAIL table with named failure states per row (strictly stronger than C-15; from R8 V-03, V-04)
- Aspirational tier expands from 25 to 28 criteria; aspirational max moves from 125 to 140
- Max composite moves from 215 to 230
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 216, Strong >= 194, Passing >= 90

**v8 -> v9:**
- C-37 added -- WHITESPACE validation phase must be a CANDIDATE-first 4-row PASS/FAIL table (Phase 3 structural analogue of C-36; CANDIDATE-first by row order prevents selective evidence assembly; from R9 V-01, V-04, V-05)
- C-38 added -- AMEND must be a structured table with Slots re-filled and Gates re-run as queryable columns (implies C-08 and C-14; amendment-lifecycle analogue of C-27 and C-21; from R9 V-02, V-04, V-05)
- C-39 added -- PREFLIGHT must include an EXECUTION DEPENDENCY table with GATE 4 as root step, making inertia-first a structural DAG property rather than a prose convention (complements C-34's slot-level dependency column; from R9 V-03, V-05)
- Aspirational tier expands from 28 to 31 criteria; aspirational max moves from 140 to 155
- Max composite moves from 230 to 245
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 231, Strong >= 206, Passing >= 90
