Reading the Round 17 scorecard carefully before extracting criteria.

The two distinguishing patterns from V-05 (beyond V-04's 27/27):

1. **Preamble declaration labeling**: V-03 and V-04 both pass C-34 with declarative sentences
   ('"REAL-REQUIRED" is the canonical identifier...') but the declarations are unnamed. V-05
   assigns explicit reference labels -- Declaration A, Declaration B -- to each preamble
   authority statement, enabling gate instructions to cite them by name.

2. **Gate citation by declaration label**: V-04's stage STOP gates enforce per-stage inertia
   extension and REAL-REQUIRED provenance by restating the rule in the gate text. V-05's
   stage STOP gates instead cite the preamble declarations by label ("per Declaration B",
   "per Declaration A"), creating a closed reference loop where compliance is verifiable
   from preamble + gate citation alone without reading every stage instruction body.

Both are strict refinements of existing criteria. Adding as C-36 and C-37, denominator 27 --> 29.

---

```markdown
# mock-all Quest Rubric -- v18

## New criteria extracted from Round 17

**C-36** -- *The template preamble assigns explicit reference labels to its structural
authority declarations (e.g., "Declaration A", "Declaration B"), enabling stage STOP
gates and ROLE 2 instructions to cite each declaration by name rather than restating
the rule inline.*

Extracted from ES-R17 (V-05). C-34 requires the template preamble to contain an explicit
declarative statement establishing "REAL-REQUIRED" as the canonical identifier. V-03 and
V-04 both satisfy C-34 with an unnamed declarative sentence: '"REAL-REQUIRED" is the
canonical identifier for the rationale section in this template.' V-05 goes one step
further: both preamble authority declarations are assigned reference labels (Declaration A
for REAL-REQUIRED canonical authority; Declaration B for per-stage inertia extension
authority). The label transforms the declaration from a sentence a reader must locate by
traversal into a named contract a gate can cite by reference. V-04 passes C-34 (declarative
form present) but its preamble declarations are unnamed -- the gate cannot cite "Declaration A"
because no such label exists. V-05's labeled preamble makes the authority contracts
machine-addressable at gate scope.

C-36 is a strict refinement of C-34 (for the REAL-REQUIRED declaration chain) and of C-35
(for the inertia-extension chain): C-36 pass implies C-34 pass and C-35 pass; neither C-34
pass nor C-35 pass implies C-36 pass (a template can have declarative preamble statements
without assigning them reference labels, as V-03 and V-04 demonstrate). C-36 is also
structurally prerequisite for C-37: gate citation by label (C-37) is only possible when
labels exist in the preamble (C-36).

The structural logic: C-27 requires gate enumeration of column header names verbatim;
C-28 adds a self-annotation making that requirement explicit in the gate text. C-33 requires
the gate to use the semantic identifier "REAL-REQUIRED"; C-34 adds a preamble declaration
making the identifier's authority explicit at document scope. C-36 adds label assignment to
the preamble declarations, making the authority contracts addressable by name. Each step in
this chain moves from implicit derivability to explicit machine-readability at broader scope.

The discriminating test: a template whose preamble contains the declarative sentence
'"REAL-REQUIRED" is the canonical identifier for the rationale section in this template' but
assigns no reference label to that declaration satisfies C-34 but fails C-36. The label
requirement is the discriminant -- it is not satisfied by a declarative sentence alone.

---

**C-37** -- *The stage-level STOP gates cite the template's preamble structural authority
declarations by reference label (e.g., "per Declaration A", "per Declaration B"), forming
a closed verification loop in which compliance with each structural constraint is checkable
from the preamble declaration plus gate citation alone, without traversing full stage
instruction bodies.*

Extracted from ES-R17 (V-05). C-35 requires per-stage instantiation of the inertia
extension instruction within each collection stage. V-04 satisfies C-35: each stage body
contains its own binding instruction and each stage STOP gate explicitly checks for the
extended inertia statement. V-05 does the same but elevates the gate enforcement mechanism:
instead of restating the per-stage extension requirement inline, each stage STOP gate says
"per Declaration B" -- citing the preamble authority declaration by its assigned label.
Similarly, REAL-REQUIRED provenance enforcement in stage STOP gates says "per Declaration A"
rather than restating the provenance rule in gate text. The ROLE 2 terminal STOP gate
unifies both citations: "per Declaration B -- verified at Stage 1, Stage 2, and Stage 3
individually" and "per Declaration A."

C-37 is a strict refinement of C-36: C-37 pass requires labeled preamble declarations (C-36
pass) and requires gate instructions to reference them by label. C-36 pass does not imply
C-37 pass: a template can have Declaration A and Declaration B as labeled preamble statements
without stage gates citing those labels (the gates could enforce the same rules by restating
them inline, as V-04 does). The discriminating test: a stage STOP gate that contains the
rule verbatim ("each has an extended inertia statement with the skeleton phrase and a
topic-specific instance via '-- specifically'") satisfies C-35 but fails C-37 because it
enforces the rule by restatement rather than by preamble citation. V-04 illustrates the
lower ceiling; V-05 illustrates the upper.

The verification property: a scorer reading a V-05 template can confirm C-35 compliance
by reading (a) Declaration B in the preamble (where the rule is stated) and (b) the gate
citation "per Declaration B" (where it is enforced), without reading every line of Stage 1,
Stage 2, and Stage 3 instruction bodies. The same property holds for C-34 + Declaration A.
The closed reference loop is the structural gain: preamble states the canonical rule by
label; stage gates enforce it by citing the label; a reader traverses preamble plus gate
citations rather than preamble plus all stage instruction bodies.

The structural parallel: C-27/C-28 makes table-gate coupling self-documenting at gate
annotation scope. C-33/C-34 makes rationale-identifier authority explicit at document scope.
C-34/C-36 makes preamble declarations machine-addressable by label. C-36/C-37 makes gate
enforcement citations traceable to labeled preamble authorities. Each chain step reduces
the traversal cost of compliance verification by one scoping level.

---

**Denominator: 27 --> 29**
**Formula: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational/29 x 10)`**
**C-36 is in the preamble-declaration chain (label-assignment rung above C-34 + C-35).
C-37 is the gate-citation ceiling above C-36.**

---

Key structural additions in v18:

Preamble-authority chain extends to a unified label-citation structure. The prior chain
(C-33 --> C-34) covered the REAL-REQUIRED identifier sub-chain. C-36 unifies the
REAL-REQUIRED and inertia-extension sub-chains under a single labeled-declaration mechanism;
C-37 closes the loop by requiring gates to cite those labels by name.

Inertia-extension chain gains a preamble-declaration rung: C-17 (instruction present)
--> C-35 (per-stage instantiation) --> C-36 (preamble names the per-stage authority with
a reference label). The three rungs are strictly ordered.

Gate-citation chain established: C-32 (gate enforces provenance + fidelity) --> C-33 (gate
uses semantic section identifier) --> C-34 (preamble declares identifier as canonical) -->
C-36 (preamble assigns reference label) --> C-37 (gate cites preamble authority by label).
The full five-rung chain moves from presence at gate scope to closed-loop citation at
document scope.

V-04 and V-05 tied at 27/27 under v17; under v18, V-05 scores 29/29 and V-04 scores 27/29,
separating the two variations. V-03 fails both C-36 and C-37 (no labeled declarations,
no label citations in gates), scoring 27/29.

Round 18 primary hypothesis: Confirm C-36 two-way discrimination -- (C-34 PASS + C-36 FAIL)
vs (C-34 PASS + C-36 PASS). The lower case requires a preamble declarative sentence without
a reference label (V-03/V-04 pattern). Confirm C-37 discrimination with a template that
has labeled preamble declarations but gates that enforce rules by restatement rather than
by citation.

---

## Version History

**v1** -- established core essential criteria (C-01 to C-04) and initial recommended tier.

**v2 through v6** -- iterative refinement of essential/recommended criteria; no aspirational tier
additions in this range.

**v7** added two aspirational criteria (C-19 to C-20) extracted from Round 6 excellence signals:
depth anchor inside placeholder token (C-19), and inertia question grounding artifact body
semantics (C-20).

**v8** skipped (confirmation round; no new criteria).

**v9** added three aspirational criteria (C-21 to C-22) extracted from Round 8 excellence signals:
inertia gap skeleton pre-seeded in classification table (C-21), and identity-violation mechanism
must be ontological self-contradiction rather than behavioral prohibition (C-22). Denominator +2.

**v10** added one aspirational criterion (C-23) extracted from Round 9 excellence signals:
positive identity affirmation must appear at each per-role activation header, not deferred to a
preamble. Denominator +1.

**v11** added two aspirational criteria (C-24 to C-25) extracted from Round 10 excellence signals:
positive identity affirmation must be syntactically first in each per-role header (C-24; elevated
from C-23 diagnostic to standalone pass condition -- V-02 demonstrated the ceiling: "fires as
syntactically first element at ROLE 1, ROLE 2, ROLE 3, and ROLE 4 activations"), and per-role
headers must use being-language rather than occupancy-language (C-25; V-01 diagnostic: "conditional
phrasing describes the model as *in* a role, not *being* it" -- "In the CLASSIFIER role" asserts
positional occupancy; "You ARE the CLASSIFIER" asserts identity; these are linguistically distinct
and C-25 prohibits the occupancy form explicitly). Denominator +2.

**v12** added two aspirational criteria (C-26 to C-27) extracted from Round 11 excellence signals:
inertia gap skeleton column entries authored per-namespace at classification time (C-26; prerequisite
for the C-21 + C-10 + C-17 three-criteria structural coupling -- V-05 demonstrated that per-
namespace specificity in the table rows at construction time is what makes the coupling pass, not
merely the column's presence), and stop-gate field enumeration names the classification table's own
column headers verbatim (C-27; V-05 pattern: "the enumerated fields ARE the table columns -- C-16
compliance comes naturally when the stop-gate condition mirrors the table structure," making C-16 +
C-11 + C-14 self-reinforcing from one structural choice). Denominator +2 (17 --> 19).

**v13** added two aspirational criteria (C-28 to C-29) extracted from Round 12 excellence signals:
stop-gate self-annotation explicitly declares its enumerated field list as the required verbatim
column names (C-28; V-02 R12 excellence -- the gate annotation "The column names above are the
required field names -- use them verbatim" makes the table-gate coupling self-documenting and
machine-readable, elevating C-27 from a naming constraint to a structural declaration), and inertia
gap skeleton seed content is pre-authored in the skill template body rather than delegated to model-
time generation (C-29; V-01 vs V-02 R12 contrast -- V-01 C-26 PASS because skill template provides
seed phrases model copies verbatim; V-02 C-26 PARTIAL because template delegates generation to
model, structural guarantee absent; C-29 is the authorship-residency ceiling above C-26).
Denominator +2 (19 --> 21).

**v14** added one aspirational criterion (C-30) extracted from Round 13 excellence signals: ROLE 2
REAL-REQUIRED rationale content is pre-authored in the skill template body rather than delegated to
model-time generation (C-30; V-03 R13 C-13 PARTIAL -- template supplies only a delegation
instruction "one sentence explaining why real artifacts are required for this namespace" with no seed
content; V-01 and V-02 passed C-13 because their templates pre-author rationale seed text the model
copies or minimally adapts; C-30 applies the same authorship-residency principle that C-29 applies
to skeleton gap phrases, but to the ROLE 2 rationale field; both criteria share the structural
guarantee logic: template-authored content gives deterministic quality, model-generated content gives
probabilistic quality). Denominator +1 (21 --> 22).

**v15** added two aspirational criteria (C-31 to C-32) extracted from Round 14 excellence signals:
ROLE 1 stop-gate enforces skeleton seed provenance by citing the template seed list and prohibiting
paraphrase (C-31; V-04 and V-05 R14 -- gate says "must be the verbatim seed phrase from the list
above" / "not a paraphrase"; V-01 R14 diagnostic: C-29 PASS but C-31 FAIL because gate uses
paraphrase field descriptions and does not cite the seed list as the authoritative source; C-31 is
the gate-level ceiling above C-29, forming the fourth rung of the gap-content chain), and ROLE 2
stop-gate enforces rationale provenance by naming the pre-authored block and directing verbatim copy
(C-32; V-01, V-04, and V-05 R14 -- ROLE 2 STOP says "with the pre-authored rationale above copied
verbatim"; V-02 and V-03 R14 fail because no pre-authored rationale exists to cite; C-32 is
structurally parallel to C-28 applied to the rationale-authorship chain; C-32 is the gate-level
ceiling above C-30, forming the third rung of the rationale-authorship chain). Denominator +2
(22 --> 24).

**v16** added one aspirational criterion (C-33) extracted from Round 15 excellence signals: ROLE 2
stop-gate's provenance reference names the template section by its semantic role identifier rather
than a generic structural reference (C-33; V-05 R15 -- gate says "with the pre-authored REAL-
REQUIRED rationale above copied verbatim," using "REAL-REQUIRED" as the semantic section identifier
assigned in the template body itself; V-01--V-04 fail because either C-32 fails (no block named at
all) or the gate names presence without using the section identifier; C-33 is a strict refinement
of C-32: C-33 pass implies C-32 pass, C-32 pass does not imply C-33 pass; C-33 extends the
rationale-authorship chain to a fourth rung and is structurally parallel to C-28 -- both make
structural dependencies machine-readable from the gate text alone, one via column header self-
declaration, the other via semantic section identifier). Denominator +1 (24 --> 25).

**v17** added two aspirational criteria (C-34 to C-35) extracted from Round 16 excellence signals:
template preamble explicitly declares the semantic role identifier as the canonical authoritative
label for the ROLE 2 rationale section, establishing document-scope identifier authority before any
gate references it (C-34; V-05 R16 -- V-04 passes C-33 by using "REAL-REQUIRED" in the gate but
the identifier's authority is implicit; V-05 adds a preamble declaration that makes the identifier
canonical before the gate is reached; C-34 is a strict refinement of C-33 and extends the rationale-
authorship chain to a fifth rung; structurally parallel to C-28 vs C-27 -- C-33 is the naming
constraint at gate scope, C-34 is the declaration constraint at document scope), and inertia
extension `-- specifically, {instance}` instruction instantiated at every artifact-collection stage
rather than only at a single composite or terminal instruction point (C-35; V-05 R16 -- gate notes
"V-05 extends to Stage 1+2+3"; V-01--V-04 have the instruction at a single point or do not
distribute it per-stage; C-35 is a strict refinement of C-17 for multi-stage templates: per-stage
instantiation binds the specificity requirement to each collection event rather than deferring it
to a terminal pass). Denominator +2 (25 --> 27).

**v18** added two aspirational criteria (C-36 to C-37) extracted from Round 17 excellence signals:
template preamble assigns explicit reference labels to its structural authority declarations
(C-36; V-05 R17 -- V-03 and V-04 both pass C-34 with unnamed declarative sentences; V-05 assigns
"Declaration A" and "Declaration B" as reference labels, making the authority contracts
machine-addressable at gate scope; C-36 is a strict refinement of C-34 and C-35: C-36 pass implies
both C-34 pass and C-35 pass; neither C-34 pass nor C-35 pass implies C-36 pass; C-36 is
prerequisite for C-37; the discriminating test is a preamble declarative sentence without a
reference label -- C-34 PASS, C-36 FAIL), and stage-level STOP gates cite preamble authority
declarations by reference label rather than restating rules inline (C-37; V-05 R17 -- V-04 gates
enforce per-stage extension and REAL-REQUIRED provenance by restating rules inline; V-05 gates say
"per Declaration B" and "per Declaration A," creating a closed reference loop where compliance is
checkable from preamble declaration + gate citation alone without traversing stage instruction
bodies; C-37 is a strict refinement of C-36: C-37 pass implies C-36 pass; C-36 pass does not imply
C-37 pass; V-04 demonstrates C-36 FAIL, so the C-36 PASS + C-37 FAIL middle case requires a
variation whose preamble has labeled declarations but whose gates enforce rules by restatement).
Denominator +2 (27 --> 29).

---

## Identity Staircase (C-18 through C-25)

Five rungs, each a strict refinement of the one below:

- **C-18**: named role + any violation mechanism
- **C-22**: violation mechanism must be ontological (not behavioral)
- **C-23**: affirmation must appear at each activation (not only preamble)
- **C-24**: affirmation must be syntactically first (not just present)
- **C-25**: affirmation must use being-language (not occupancy-language)

C-26 through C-37 are not part of the identity staircase. They belong to the table-coupling
cluster and its sub-chains, which govern the inertia/classification table structural design
and ROLE 2 content provenance.

---

## Table-Coupling Cluster (C-10, C-11, C-13 to C-17, C-19 to C-21, C-26 to C-37)

Sub-chains within the cluster:

**Gap-content chain (four rungs):** C-21 (skeleton column present) --> C-26 (seeds per-namespace
at construction time) --> C-29 (seeds pre-authored in template body) --> C-31 (gate cites seed list
and prohibits paraphrase).

**Rationale-authorship chain (five rungs):** C-13 (rationale block present) --> C-30 (rationale
template-authored) --> C-32 (gate enforces provenance + fidelity) --> C-33 (gate uses semantic
section identifier) --> C-34 (preamble declares identifier as canonical authority).

**Table-gate coupling chain (two rungs):** C-27 (gate enumerates column headers verbatim) --> C-28
(gate self-annotates that those names are required verbatim).

**Inertia-extension chain (three rungs):** C-17 (instruction present) --> C-35 (instruction
instantiated at each collection stage in multi-stage templates) --> C-36 (preamble names the
per-stage authority with a reference label, unifying the inertia-extension and REAL-REQUIRED
chains under a shared labeled-declaration mechanism).

**Gate-citation chain (two rungs above C-36):** C-36 (preamble assigns reference labels to
authority declarations) --> C-37 (stage STOP gates cite preamble declarations by label, forming
closed verification loop).

---

## mock-all Quest Score -- Round 17 (scored under v18)

**Rubric:** v18 | **Variations:** V-01 through V-05 | **Denominator:** 29 aspirational criteria

---

### Per-Criterion Scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 | P | P | P | P | P | TOPICS.md lookup + tier source line: all present |
| C-10 | P | P | P | P | P | Table column headers: all present |
| C-11 | P | P | P | P | P | Nine namespace rows: all present |
| C-12 | P | P | P | P | P | Sequential gated phases: all present |
| C-13 | P | P | P | P | P | REAL-REQUIRED block structure present in all |
| C-14 | P | P | P | P | P | Per-namespace MUST/DO-NOT-use vocabulary: all present |
| C-15 | P | P | P | P | P | Body vocabulary compliance instruction: all present |
| C-16 | P | P | P | P | P | Stop-gate references classification-derived conditions: all present |
| C-17 | P | P | P | P | P | Inertia extension instruction: all present |
| C-18 | P | P | P | P | P | Named phases + violation mechanism: all present |
| C-19 | P | P | P | P | P | Depth-anchored seed phrases: all present |
| C-20 | P | P | P | P | P | Body-grounding instruction: all present |
| C-21 | P | P | P | P | P | Skeleton column pre-seeded: all present |
| C-22 | **F** | P | P | P | P | V-01: behavioral violation; V-02--V-05: ontological |
| C-23 | **F** | P | P | P | P | V-01: no per-activation affirmation; C-22 FAIL entails C-23 FAIL |
| C-24 | **F** | P | P | P | P | V-01: no affirmation; V-02--V-05: syntactically first |
| C-25 | **F** | P | P | P | P | V-01: occupancy-language; V-02--V-05: being-language |
| C-26 | P | P | P | P | P | Seeds per-namespace in template body: all present |
| C-27 | **F** | P | P | P | P | V-01: generic cell check; V-02--V-05: column names verbatim |
| C-28 | **F** | P | P | P | P | V-01: no self-annotation; V-02--V-05: self-annotates required names |
| C-29 | P | P | P | P | P | Seed phrases pre-authored in template body: all present |
| C-30 | **F** | P | P | P | P | V-01: delegation placeholder; V-02--V-05: pre-authored per-namespace |
| C-31 | P | P | P | P | P | Gate cites seed list and prohibits paraphrase: all present |
| C-32 | **F** | **F** | P | P | P | V-01: no pre-authored block to cite; V-02: presence check only; V-03--V-05: names block + directs verbatim copy |
| C-33 | **F** | **F** | **F** | P | P | V-01--V-02: C-32 FAIL entails C-33 FAIL; V-03: generic "rationale" label; V-04--V-05: "REAL-REQUIRED" semantic identifier |
| C-34 | **F** | **F** | P | P | P | V-01--V-02: C-33 FAIL entails C-34 FAIL; V-03--V-05: preamble declares "REAL-REQUIRED" as canonical identifier |
| C-35 | **F** | **F** | **F** | P | P | V-01--V-02: single-stage trivially N/A (C-35 = C-17; both FAIL via C-17 chain); V-03: multi-stage but terminal-only `-- specifically`; V-04--V-05: per-stage instantiation |
| **C-36** | **F** | **F** | **F** | **F** | **P** | V-01--V-02: no preamble declarations of any kind; V-03--V-04: unnamed declarative sentences (no reference labels assigned); V-05: Declaration A and Declaration B labeled in preamble before any role activates |
| **C-37** | **F** | **F** | **F** | **F** | **P** | V-01--V-04: C-36 FAIL entails C-37 FAIL (no labels to cite); V-05: stage STOP gates say "per Declaration B" and "per Declaration A," closing the verification loop |

---

### Essential / Recommended

All five variations pass all 5 essential criteria and all 3 recommended criteria.
**Essential: 5/5 for all. Recommended: 3/3 for all.**

---

### Aspirational Counts

| Variation | PASS | FAIL | Aspirational (of 29) |
|-----------|------|------|----------------------|
| V-01 | 16 | 13 | 16/29 |
| V-02 | 23 | 6 | 23/29 |
| V-03 | 25 | 4 | 25/29 |
| V-04 | 27 | 2 | 27/29 |
| V-05 | 29 | 0 | 29/29 |

V-01 fails: C-22, C-23, C-24, C-25, C-27, C-28, C-30, C-32, C-33, C-34, C-35, C-36, C-37
V-02 fails: C-32, C-33, C-34, C-35, C-36, C-37
V-03 fails: C-33, C-35, C-36, C-37
V-04 fails: C-36, C-37
V-05 fails: none

---

### Composite Scores

Formula: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational/29 x 10)`

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.0 | 30.0 | 5.52 | **95.5** |
| V-02 | 60.0 | 30.0 | 7.93 | **97.9** |
| V-03 | 60.0 | 30.0 | 8.62 | **98.6** |
| V-04 | 60.0 | 30.0 | 9.31 | **99.3** |
| V-05 | 60.0 | 30.0 | 10.00 | **100.0** |

**Rank: V-05 > V-04 > V-03 > V-02 > V-01**

---

### C-36 and C-37 Discrimination -- Round 17

| Case | Instantiated by | C-34 | C-35 | C-36 | C-37 | Signal |
|------|-----------------|------|------|------|------|--------|
| No preamble declaration | V-01, V-02 | FAIL | FAIL | FAIL | FAIL | No canonical-authority declaration of any kind |
| Unnamed declaration + terminal `-- specifically` | V-03 | PASS | FAIL | FAIL | FAIL | Declarative preamble sentence; no label; no per-stage extension |
| Unnamed declaration + per-stage `-- specifically` | V-04 | PASS | PASS | FAIL | FAIL | Declarative preamble sentence; no label; per-stage extension in stage bodies; gates enforce by restatement |
| Labeled declarations + gate citations | V-05 | PASS | PASS | PASS | PASS | Declaration A + Declaration B labeled in preamble; stage gates cite by label |

The isolated middle case for C-36 -- C-34 PASS + C-36 FAIL -- is demonstrated by V-03 and V-04:
preamble contains a declarative sentence but assigns no reference label. The C-36 PASS ceiling
requires labeled declarations (Declaration A and Declaration B patterns).

The C-36 PASS + C-37 FAIL intermediate case is not yet instantiated: a template whose preamble
contains labeled declarations but whose stage gates enforce rules by restating them inline (not
citing declaration labels) would score C-36 PASS, C-37 FAIL.

**Round 18 primary hypothesis:** Construct a variation with named preamble declarations
(C-36 PASS) but gate enforcement by inline restatement (C-37 FAIL), confirming independent
discrimination of C-36 and C-37. Secondary: confirm C-35 FAIL / C-36 FAIL with a multi-stage
template whose preamble has unnamed declarative sentences and whose extension instruction
appears only at a terminal point (extends V-03 pattern to verify C-36 diagnostic path).
```
