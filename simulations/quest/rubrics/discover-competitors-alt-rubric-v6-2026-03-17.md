Rubric v6 written to `simulations/quest/rubrics/discover-competitors-alt-rubric-v6-2026-03-17.md`.

---

**4 new aspirational criteria (C-27 -- C-30):**

| ID | Pattern | Source | Pass Condition |
|----|---------|--------|----------------|
| C-27 | Machine-readable phase assignment in output contract | V-02, V-04, V-05 | Output contract table has a dedicated "Filled by phase" column — makes the contract->phase link queryable without reading any phase heading; 3-column contract does not satisfy |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | V-03, V-05 | OUTPUT CONTRACTS is a named subsection inside PREFLIGHT — not a separate section before or after it; extends C-26 from gate consolidation to full execution-specification consolidation |
| C-29 | Full-path back-reference labels in producing phases | V-03, V-05 | Phase headings use "PREFLIGHT > OUTPUT CONTRACTS" (full path) not just "OUTPUT CONTRACT"; only applicable when C-28 is satisfied; if C-28 fails, score C-29 as 0 |
| C-30 | Write-token instruction within INERTIA-REF gate | V-04, V-05 | The INERTIA-REF gate includes an explicit write directive ("Write INERTIA-REF = ...") at gate evaluation time — checking for the token's presence does not satisfy; binds token resolution to gate execution |

**Scoring changes:**
- Aspirational tier: 18 → 22 criteria, max 90 → 110
- Max composite: 180 → 200
- Formula denominator: `aspirational_pass / 22 × 110`
- Grade bands rescaled: Exceptional ≥ 188, Strong ≥ 168, Passing ≥ 90 (golden threshold unchanged)

**Dependency notes:**
- C-28 automatically satisfies C-26 (superset); C-29 requires C-28 (N/A otherwise); C-30 automatically satisfies C-22
Topic domain is inferred from repo context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply the domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section names at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — not just "inertia is high." The mechanism is specific to the status quo competitor's behavior or product feature, not a category label applied generically. |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. The citation appears within the competitor entry, not in a trailing footnote block. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output as a result. |

---

## Aspirational Criteria (weight = 110 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires the competitive map and the focus dimension together. A finding that merely cites both dimensions without demonstrating that either alone is insufficient does not pass. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Positive instruction alone does not ensure this passes — the output must demonstrate that ungrounded findings are absent. |
| C-11 | Fully-cited competitor table | correctness | Every external competitor row (not just one) includes an inline citation from a WebSearch result. The citation appears within the row or immediately adjacent entry — not in a footnote or trailing references section. This extends C-07 from minimum-one to all-external. |
| C-12 | Self-negating cross-dimensional finding | depth | The CROSS-DIMENSIONAL or equivalent whitespace finding explicitly argues why the finding cannot be derived from the competitive map alone and why it cannot be derived from the focus dimension alone. The output provides or implies the single-dimension reduction for each — showing what is lost when either dimension is removed — rather than just asserting cross-dimensionality. |
| C-13 | Claim-level finding anchors | depth | Each finding references a specific cell value, column value, or row-level attribute from a named competitor entry — not just the competitor name. For example: citing Competitor X's specific threat rating, mechanism sentence, or focus-column value as the evidentiary basis. Findings grounded only by competitor name ("Competitor X reveals...") do not satisfy; findings grounded by a specific claim within that row do. |
| C-14 | AMEND as proof validator | behavior | The AMEND section requires that any adjustment shifting the focus dimension must rerun both single-dimension reductions (C-12 proofs) for the updated CROSS-DIMENSIONAL finding. A standalone instruction to "update the finding" does not satisfy — the explicit rerun of both reduction arguments must be prescribed. |
| C-15 | Inline anchor tag before proof block | format | The proof block or cross-dimensional finding structure declares a named evidentiary source slot (e.g., SOURCE:, ANCHOR:, or equivalent label) before the reduction arguments are written. The evidentiary source is identified first; the proof follows. Constructing the argument before naming the evidence does not satisfy. |
| C-16 | Gate failure naming | format | The skill instruction names the error condition explicitly (e.g., "gate failure," "citation gate violation," or equivalent) rather than only describing the rule in positive terms. Naming the failure state makes the gate concrete and checkable; a rule stated only as a positive requirement does not satisfy. |
| C-17 | WHITESPACE grounded by attribute absence | depth | The WHITESPACE finding grounds the identified gap by naming specific attributes from competitor rows that are absent or uncontested across the table — not by assertion alone. The gap is evidenced by what is missing at the attribute level across named rows, not by a claim that no competitor owns the space. |
| C-18 | NOT ACCEPTABLE examples for anchoring | format | The skill instruction includes at least one explicit NOT ACCEPTABLE example that names the most common inadequate-but-compliant form — such as name-only anchoring ("Competitor X reveals..."). The example must name the failure pattern specifically; an abstract prohibition without a concrete negative exemplar does not satisfy. |
| C-19 | Synthesis-first output contracts | behavior | At least one output slot requirement — named by label (e.g., "WHITESPACE absence evidence," "ANCHOR column value") — is stated within the data-collection phase instruction, not only at the synthesis phase. The collection phase must explicitly name what the downstream output slot requires from the data gathered, making the synthesis requirement visible before data is collected. Stating the output requirement only at the synthesis phase does not satisfy. |
| C-20 | Structural column coercion for anchoring | format | The skill instruction specifies a column format or structural template (e.g., `Row C{N}, {attribute}: "{value}"`) that makes name-only entries syntactically non-conforming without requiring rule evaluation. The constraint must be defined as a format shape for the column or slot. A prohibition-only instruction — even accompanied by NOT ACCEPTABLE examples — does not satisfy; the shape constraint must be structural. |
| C-21 | Gate-as-section with PASS/FAIL table | format | At least one gate is formatted as a named section containing a structured table with three distinct columns: Check, Pass condition, and Failure state (or equivalent labels). The table must enumerate at least two rows corresponding to distinct checkable conditions. A gate stated only in prose — even with bolded failure names — does not satisfy. Both the section heading and the columnar table structure must be present. |
| C-22 | INERTIA-REF per-finding citation | depth | The skill instruction defines a named inertia reference token (e.g., INERTIA-REF, C0-REF, or equivalent) in the inertia section and requires each finding in the findings section to cite or compare against that token by name. The token must function as a mandatory per-finding reference baseline; a definition without required per-finding citation does not satisfy. An inertia entry present only as a table row — without a named token required across findings — does not satisfy. |
| C-23 | Output contract slot format specification | behavior | At least one output contract slot specifies both a label and a required structural format or template for the value that fills it (e.g., label: "Anchor column", format: `Row C{N}, {attribute}: "{value}"`). A slot named by label only — without a format shape for its value — does not satisfy this criterion. Labeling is necessary; prescribing the format of what fills the slot is what satisfies. |
| C-24 | Phase-to-contract back-references | behavior | At least one phase that produces data for a named output contract slot explicitly names the slot it fills at the point of production (e.g., "(fills WHITESPACE absence evidence slot — see OUTPUT CONTRACTS)" or "fills Anchor slot — OUTPUT CONTRACT"). The output contract must forward-declare the slot; the producing phase must back-reference it by the same label. A one-directional reference — contract declaration only, or phase mention without a prior contract declaration — does not satisfy. |
| C-25 | Cross-table structural coercion | format | Structural column coercion (as defined by C-20) is applied independently in at least two tables: one in the data-collection phase (e.g., competitor table Anchor column) and one in the synthesis or findings phase (e.g., findings table Anchor column or INERTIA-REF-DELTA column). Each table must define its own format template for its relevant column or slot. A single-table coercion — even with multiple coerced columns within that table — does not satisfy. The coercion must span the collection-to-synthesis boundary. |
| C-26 | Consolidated PREFLIGHT gate block | format | All mandatory gates are consolidated into a single named PREFLIGHT (or equivalent) section that appears before Phase 1 or before any execution phase. Each gate within the block must satisfy C-21 (named subsection with a PASS/FAIL table). Distributing gates across individual phases — even if each gate individually satisfies C-21 — does not satisfy this criterion. The PREFLIGHT block must be a single section containing all gate subsections. |
| C-27 | Machine-readable phase assignment in output contract | behavior | The output contract table includes a dedicated column (e.g., "Filled by phase" or equivalent) that names the producing phase for each slot by name or number. A 3-column contract table — even one with format templates per slot (C-23) — does not satisfy; the phase assignment must appear as a queryable column in the contract table itself. This makes the forward link from contract to phase machine-readable without reading any phase heading. |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | format | The OUTPUT CONTRACTS declaration is a named subsection within the PREFLIGHT block — not a separate section before or after it. All mandatory gates and all output contract slots must be readable from within the same PREFLIGHT section. A separate OUTPUT CONTRACTS section placed outside PREFLIGHT does not satisfy even if it immediately precedes Phase 1. This extends C-26 from gate consolidation to full execution-specification consolidation. |
| C-29 | Full-path back-reference labels in producing phases | behavior | Back-reference labels in producing phase headings name the complete navigable path to the contract declaration (e.g., "PREFLIGHT > OUTPUT CONTRACTS" rather than just "OUTPUT CONTRACT"). This criterion applies only when OUTPUT CONTRACTS is embedded within a containing section (i.e., C-28 is satisfied); a top-level OUTPUT CONTRACT section needs no path prefix. A back-reference naming the contract section without its containing section does not satisfy when the contract is nested. |
| C-30 | Write-token instruction within INERTIA-REF gate | behavior | The INERTIA-REF gate (or equivalent gate for the inertia reference token) includes an explicit write instruction that directs the model to record the resolved token value at gate evaluation time (e.g., "Write INERTIA-REF = [specific mechanism phrase from C0 row]"). A gate that only checks for the presence or correctness of INERTIA-REF without a write directive does not satisfy. C-22 requires per-finding citation of INERTIA-REF; this criterion requires the gate itself to perform the token write — binding token resolution to gate execution. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-30 | 5 | 110 |
| **Max composite** | | | **200** |

**Composite formula:**
```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 22 x 110)
```

PARTIAL scores count as 0.5 for numerator purposes.

**Golden threshold:** All 5 essential pass AND composite >= 90

**Grade bands:**

| Score | Grade |
|-------|-------|
| 188 -- 200 | Exceptional |
| 168 -- 187 | Strong |
| 90 -- 167 | Passing |
| < 90 | Below bar |

Grade bands rescaled proportionally from v5 (v5 max = 180; v6 max = 200). Exceptional threshold
preserved at ~94% of max; Strong threshold at ~84% of max; Passing at golden threshold (90).

---

## Criterion Rationale (v2 additions)

**Why C-11 (Fully-cited table) over C-07 alone:**
Round 1 showed that requiring one citation is insufficient -- models satisfy C-07 with a single
verified claim and coast on unverified characterizations for all other rows. C-11 closes this
gap: WebSearch must be run per external competitor, not just once.

**Why C-12 (Self-negating cross-dimensional finding):**
C-09 scored PARTIAL in every variation across Round 1. The common failure: variations required
the finding to *cite* both dimensions but not to *prove* single-dimension insufficiency. C-12
makes the exclusion test explicit and output-level -- the finding must demonstrate what is lost
when either dimension is removed, not merely assert it draws on both.

**Why C-13 (Claim-level anchors) over C-10 alone:**
C-10 requires findings to name a competitor row. C-13 requires findings to name a specific
*claim within* that row -- a threat rating, mechanism sentence, or focus-column value. The
upgrade matters because "Competitor X reveals a gap" is technically grounded but epistemically
empty: the reader cannot verify the inference without re-reading the full row. Claim-level
anchors make inferences checkable in one glance.

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
Positive-only rule framing ("every row must have a citation") leaves the error state
implicit. When a gate is violated, the model has no named failure mode to report against.
Naming the failure state explicitly ("citation gate failure -- do not output the row")
makes gates self-enforcing: the model can produce a structured error rather than silently
violating the rule.

**Why C-17 (WHITESPACE grounded by attribute absence):**
C-04 requires the whitespace finding to exist. C-13 requires findings to anchor to
specific attributes. C-17 applies claim-level anchoring specifically to the WHITESPACE
finding: the gap must be shown to be vacant by naming which attributes across which rows
confirm no competitor owns it. Asserting "no competitor covers this space" without
attribute-level evidence is the WHITESPACE analogue of the name-only anchoring failure.

**Why C-18 (NOT ACCEPTABLE examples):**
V-03 and V-05 (Round 2) showed that ACCEPTABLE/NOT ACCEPTABLE example pairs are the
single most reliable mechanism for eliminating the name-only anchoring escape hatch.
Abstract prohibitions ("findings must cite a specific attribute") are consistently
interpreted as satisfied by naming the competitor. A NOT ACCEPTABLE example naming the
exact inadequate form ("Competitor 2 reveals that...") closes the interpretation gap.

---

## Criterion Rationale (v4 additions)

**Why C-19 (Synthesis-first output contracts):**
R4 V-01 and V-04 showed that declaring output slot requirements at data-collection time
changes what gets collected. When the instruction names "WHITESPACE absence evidence" as
a required output slot during Phase 3 collection, the collection step is automatically
cued to gather per-attribute absence data. When the requirement is only stated at synthesis
time, the model must backfill or fabricate what it failed to collect. Front-loading the
output contract at the collection phase makes Phase 3 serve Phase 4 by name.

**Why C-20 (Structural column coercion for anchoring):**
R4 V-02 demonstrated the most adversarially robust C-13 mechanism: an Anchor column
defined with format `Row C{N}, {attribute}: "{value}"`. This format makes name-only
entries syntactically incorrect before any rule evaluation occurs -- the cell either
contains a row reference plus attribute-value pair or it is malformed. Prohibition
instructions and NOT ACCEPTABLE examples (C-18) can be satisfied with a single
compliant example while allowing non-compliant cases to pass. A structural format
constraint eliminates the escape entirely.

**Why C-21 (Gate-as-section with PASS/FAIL table):**
R4 V-04 showed that gate-as-section with a three-column PASS/FAIL table produces the
most debuggable skill structure: each gate condition becomes a checklist row with an
unambiguous pass condition and a named failure state. Prose gates (even with bolded
failure names, as confirmed PASS in C-16) require the reader to parse natural language
to determine check, pass, and failure. Tabular gates are directly executable as a
review checklist without interpretation.

**Why C-22 (INERTIA-REF per-finding citation):**
R4 V-03 and V-05 showed that naming an INERTIA-REF token in the inertia section and
requiring each finding to cite it elevates inertia from a first-row table entry to a
gravitational reference frame. Without the per-finding requirement, inertia is assessed
once and then ignored during synthesis: findings treat external competitors as the
baseline. With a mandatory INERTIA-REF comparison per finding, every competitive
inference is measured against the status quo cost rather than against other external
competitors. This is the structural analogue of the C-15 SOURCE slot: name the baseline
before constructing the argument.

---

## Criterion Rationale (v5 additions)

**Why C-23 (Output contract slot format specification):**
R5 V-04 showed that an output contract table where each slot has both a label and a
required format shape (e.g., "Anchor column: `Row C{N}, {attribute}: \"{value}\"`") is
fundamentally stronger than a label-only contract. A label-only slot tells the producing
phase what to collect; a format-specified slot tells it what shape the collection must
take. This upgrades the contract from a reminder to a machine-checkable constraint:
a slot filled in the wrong format is detectable without prose parsing, in the same way
C-20's structural coercion makes name-only cells detectable without rule evaluation.
C-23 applies the C-20 insight to the contract layer itself.

**Why C-24 (Phase-to-contract back-references):**
R5 V-01 and V-04 showed that when the producing phase explicitly names the output
contract slot it fills ("fills WHITESPACE absence evidence slot -- see OUTPUT CONTRACTS"),
the collection-to-synthesis dependency becomes traceable in both directions. A forward-only
contract (declared before Phase 1 but not referenced in the producing phase) can drift:
the phase may collect something that does not actually satisfy the declared slot. When the
phase back-references the slot by name, the constraint is active at the moment of
production, not only at synthesis time. This is the temporal analogue of C-15's SOURCE
slot: name the contract you are filling before writing the content, not after.

**Why C-25 (Cross-table structural coercion):**
R5 V-02 and V-05 showed that structural column coercion applied to both the competitor
table and the findings table eliminates the most common compliance gap: collecting
claim-level anchor values correctly but then re-stating them as name-only anchors in
the findings. When the findings table has its own coerced Anchor column with the same
format template, the structural constraint propagates through the full pipeline. C-20
prevents name-only anchoring at collection time; C-25 ensures the same constraint is
enforced at synthesis time, closing the round-trip escape.

**Why C-26 (Consolidated PREFLIGHT gate block):**
R5 V-03 showed that consolidating all gates into a single PREFLIGHT section before
Phase 1 produces a skill that can be audited without reading the full phase sequence.
When gates are distributed across phases, verifying compliance requires executing the
full skill instruction mentally, gate by gate. A consolidated PREFLIGHT block exposes
all gates simultaneously: the model -- or a human reviewer -- can run the complete
gate checklist before any execution phase begins. This is the gate-architecture analogue
of the output contract: declare all constraints upfront so the execution phases produce
to known specifications rather than discovering constraints mid-execution.

---

## Criterion Rationale (v6 additions)

**Why C-27 (Machine-readable phase assignment in output contract):**
R6 V-02, V-04, and V-05 showed that adding a "Filled by phase" column to the output
contract table completes the bidirectionality introduced by C-24 at the contract level
itself. C-24 makes back-references from phase headings to contract slots mandatory, but
the contract table remains a one-way lookup (slot -> format). A 4-column contract table
(Slot / Label / Required format / Filled by phase) makes the phase assignment queryable
from the contract alone: given any slot, you can determine which phase is responsible
without reading any phase heading. This closes the navigation gap in the reverse direction:
contract -> phase (C-27) complements phase -> contract (C-24).

**Why C-28 (OUTPUT CONTRACTS co-located within PREFLIGHT):**
R6 V-03 and V-05 showed that embedding OUTPUT CONTRACTS as a subsection within PREFLIGHT
-- rather than as a separate section before or after it -- produces the tightest possible
front-loading. When gates and output contract slots are in the same section, a single
read of PREFLIGHT exposes the complete execution specification: what is checked (gates),
what is produced (output slots), what format it must take (C-23), and which phase produces
it (C-27). Separating OUTPUT CONTRACTS from PREFLIGHT creates two auditable sections
rather than one; co-location eliminates context switching between them. This extends C-26
from gate consolidation to full specification consolidation: PREFLIGHT becomes the single
source of truth for the skill.

**Why C-29 (Full-path back-reference labels in producing phases):**
R6 V-03 and V-05 showed that when OUTPUT CONTRACTS is nested within PREFLIGHT (C-28),
a back-reference label of "OUTPUT CONTRACT" alone is ambiguous: it names the section
but not its location. The full-path label "PREFLIGHT > OUTPUT CONTRACTS" provides a
navigable pointer that works even without document search -- the reader knows to enter
PREFLIGHT and then locate the OUTPUT CONTRACTS subsection. This criterion is only
meaningful when C-28 is satisfied; a top-level OUTPUT CONTRACT section is directly
addressable by name. When contracts are nested, the path prefix is the difference between
a navigable pointer and an unanchored name.

**Why C-30 (Write-token instruction within INERTIA-REF gate):**
R6 V-04 and V-05 showed that including an explicit write instruction within GATE 4
binds INERTIA-REF token resolution to gate execution rather than treating it as a
precondition. C-22 requires the token to be defined and per-finding cited; without C-30,
the definition can float in the inertia section while the gate merely checks for it.
When the gate itself contains a write instruction ("Write INERTIA-REF = [specific
mechanism phrase from C0 row]"), the token is actively produced at the gate evaluation
step rather than passively checked. This eliminates the gap between gate pass and token
availability: a gate that passes must have written the token, making the subsequent
per-finding citations (C-22) have a guaranteed referent.

---

## Note on C-21 vs C-16 (preserved from v4)

These are distinct -- C-16 requires naming failure states (satisfied by bolded prose),
C-21 requires the gate to be structured as a section with a PASS/FAIL table. R4 confirmed
both can be PASS simultaneously; they target different structural levels.

## Note on C-26 vs C-21

These are also distinct -- C-21 requires at least one gate to be a named section with a
PASS/FAIL table; C-26 requires all gates to be consolidated into a single pre-phase
PREFLIGHT block. A skill with one tabular gate (satisfying C-21) but gates distributed
across phases does not satisfy C-26. A skill with all gates in a PREFLIGHT block
automatically satisfies C-21 via the gates within it.

## Note on C-28 vs C-26

C-26 requires all gates in a single PREFLIGHT block. C-28 requires OUTPUT CONTRACTS to
also be a subsection within that block. A skill satisfying C-28 automatically satisfies
C-26; the converse is not true. A PREFLIGHT block containing only gates satisfies C-26
but not C-28.

## Note on C-29 dependency on C-28

C-29 is only applicable when C-28 is satisfied. If OUTPUT CONTRACTS is a top-level
section, no path prefix is needed and C-29 is vacuously satisfied by any C-24-compliant
back-reference. In scoring, if C-28 is not satisfied, C-29 cannot be meaningfully
evaluated; treat as N/A (score 0) in that case.

## Note on C-30 vs C-22

C-22 requires the INERTIA-REF token to be defined and per-finding cited. C-30 requires
the gate to perform the write at evaluation time. A skill satisfying C-30 automatically
satisfies C-22 (the write produces the token; gate pass guarantees its availability).
The converse is not true: a skill can define INERTIA-REF in the inertia section (C-22)
without the gate performing the write (C-30).

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
