Reading the Round 16 scorecard carefully before extracting criteria.

The two distinguishing patterns from V-05 (beyond V-04's 25/25):

1. **C-33 notes**: "V-05: same, plus preamble declaration" — V-04 uses "REAL-REQUIRED" in the gate but the identifier's authority is implicit. V-05 adds a preamble that explicitly declares it as the canonical label before any gate references it.

2. **C-17 notes**: "V-05 extends to Stage 1+2+3" — V-04 has 4 roles but the inertia extension instruction appears at a single point. V-05 instantiates it at each distinct collection stage.

Both are strict refinements of existing criteria (C-33 and C-17 respectively). Adding as C-34 and C-35, denominator 25 → 27.

---

```markdown
# mock-all Quest Rubric -- v17

## New criteria extracted from Round 16

**C-34** -- *The template preamble explicitly declares the semantic role identifier used in
the ROLE 2 rationale section as the canonical authoritative label, establishing document-scope
identifier authority before any gate references it.*

Extracted from ES-R16 (V-05). C-33 requires the ROLE 2 stop-gate to use the semantic section
identifier "REAL-REQUIRED" rather than a generic structural label when citing the rationale block.
V-05 goes one step further: the template preamble contains an explicit declaration that
"REAL-REQUIRED" is the canonical identifier for the rationale section, establishing identifier
authority at document scope. V-04 passes C-33 (gate says "pre-authored REAL-REQUIRED rationale
above copied verbatim") but the identifier's authority is implicit -- derivable only by matching
the gate label to the section header in the template body. V-05's preamble declaration makes the
authority explicit and precedes all gate references to the identifier; the gate becomes a citation
of an already-declared canonical name rather than a label that happens to match a section header.

C-34 is a strict refinement of C-33: C-34 pass implies C-33 pass; C-33 pass does not imply C-34
pass (a gate using "REAL-REQUIRED" without a preamble declaration satisfies C-33 but not C-34).
C-34 extends the rationale-authorship chain to a fifth rung.

The structural logic parallels C-28 vs C-27: C-27 requires the gate to enumerate column headers
verbatim; C-28 adds a self-annotation declaring those names as required verbatim, making the
constraint explicit in the gate text itself. Similarly, C-33 requires the gate to use the semantic
identifier; C-34 requires the template preamble to declare that identifier as authoritative, making
the constraint explicit at document scope. In both cases, the higher criterion makes the structural
dependency machine-readable without requiring a reader to traverse the full document to confirm the
relationship. The analogy is exact: C-27 and C-33 are naming constraints at gate scope; C-28 and
C-34 are declaration constraints that make authority explicit at a broader scope (gate-annotation
scope for C-28, document scope for C-34).

---

**C-35** -- *The inertia extension `-- specifically, {instance}` instruction is instantiated at
every artifact-collection stage of the skill template, not only at a single composite or terminal
instruction point.*

Extracted from ES-R16 (V-05). C-17 requires the inertia extension instruction to appear somewhere
in the skill template. V-05 demonstrates a ceiling above C-17: the skill contains three distinct
artifact-collection stages (Stage 1, Stage 2, Stage 3), and the `-- specifically, {instance}`
instruction appears within each stage individually. V-01 through V-04 either present the
instruction as a single composite instruction or within a structure where it is not instantiated at
each collection stage; the C-17 notes explicitly distinguish V-05 as extending "to Stage 1+2+3"
without an equivalent note for any other variation.

C-35 is a strict refinement of C-17 for multi-stage templates: in a single-stage template, C-35
pass is equivalent to C-17 pass (one stage, one application); in a multi-stage template, C-35
requires per-stage instantiation. The discriminating test is a multi-stage template where the
`-- specifically, {instance}` instruction appears only at a terminal or composite point rather
than at each collection stage: C-17 PASS (instruction present), C-35 FAIL (instruction absent at
intermediate stages). The structural logic is that inertia extension should occur at the moment of
collection, not deferred to a cleanup or synthesis step; per-stage instantiation binds the
specificity requirement to each collection event and prevents a model from completing Stage 1 and
Stage 2 collection without the extension instruction firing.

---

**Denominator: 25 --> 27**
**Formula: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational/27 x 10)`**
**C-34 is in the rationale-authorship chain (fifth rung). C-35 is in the inertia-extension chain
(ceiling above C-17).**

---

Key structural additions in v17:

**Rationale-authorship chain extends to five rungs:** C-13 (rationale block present) --> C-30
(rationale template-authored) --> C-32 (gate enforces provenance + fidelity) --> C-33 (gate uses
semantic section identifier) --> C-34 (preamble declares identifier as canonical authority).

**Declaration scope hierarchy confirmed across two sub-chains:** C-28 makes table-gate coupling
machine-readable at gate-annotation scope; C-34 makes rationale-identifier authority machine-
readable at document scope. Both are declaration criteria above naming criteria (C-27 and C-33
respectively).

**Inertia-extension chain gains a multi-stage ceiling:** C-17 (instruction present) --> C-35
(instruction instantiated at each collection stage). C-35 applies only when the template has
multiple collection stages; the discriminating case is a multi-stage template with a single
composite instruction point.

**Table-coupling cluster expands** from 17 to 19 criteria (adding C-34, C-35).

**V-04 and V-05 discrimination established:** Under v16, V-04 and V-05 tied at 25/25. Under v17,
V-05 scores 27/27 and V-04 scores 25/27, separating the two variations for the first time.

**Round 17 primary hypothesis:** Confirm C-34 two-way discrimination -- (C-33 PASS + C-34 FAIL)
vs (C-33 PASS + C-34 PASS). The isolated upper case requires a variation whose gate uses the
semantic identifier "REAL-REQUIRED" but whose preamble contains no declaration of identifier
authority; V-04 is the already-demonstrated lower ceiling. Confirm C-35 discrimination with a
multi-stage variation that applies the extension instruction at only one stage.

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

---

## Identity Staircase (C-18 through C-25)

Five rungs, each a strict refinement of the one below:

- **C-18**: named role + any violation mechanism
- **C-22**: violation mechanism must be ontological (not behavioral)
- **C-23**: affirmation must appear at each activation (not only preamble)
- **C-24**: affirmation must be syntactically first (not just present)
- **C-25**: affirmation must use being-language (not occupancy-language)

C-26 through C-35 are not part of the identity staircase. They belong to the table-coupling cluster
and its sub-chains, which govern the inertia/classification table structural design and ROLE 2
content provenance.

---

## Table-Coupling Cluster (C-10, C-11, C-13 to C-17, C-19 to C-21, C-26 to C-35)

Sub-chains within the cluster:

**Gap-content chain (four rungs):** C-21 (skeleton column present) --> C-26 (seeds per-namespace
at construction time) --> C-29 (seeds pre-authored in template body) --> C-31 (gate cites seed list
and prohibits paraphrase).

**Rationale-authorship chain (five rungs):** C-13 (rationale block present) --> C-30 (rationale
template-authored) --> C-32 (gate enforces provenance + fidelity) --> C-33 (gate uses semantic
section identifier) --> C-34 (preamble declares identifier as canonical authority).

**Table-gate coupling chain (two rungs):** C-27 (gate enumerates column headers verbatim) --> C-28
(gate self-annotates that those names are required verbatim).

**Inertia-extension chain (two rungs):** C-17 (instruction present) --> C-35 (instruction
instantiated at each collection stage in multi-stage templates).

---

## mock-all Quest Score -- Round 16 (scored under v17)

**Rubric:** v17 | **Variations:** V-01 through V-05 | **Denominator:** 27 aspirational criteria

---

### Per-Criterion Scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 | P | P | P | P | P | TOPICS.md lookup + tier source line: all present |
| C-10 | P | P | P | P | P | Table column headers: all present |
| C-11 | P | P | P | P | P | Nine namespace rows: all present |
| C-12 | P | P | P | P | P | Sequential gated phases: V-01 (4 steps), V-02 (3 roles), V-03--V-05 (4 roles) |
| C-13 | P | P | P | P | P | REAL-REQUIRED block structure present in all (V-01: delegation, but structure exists) |
| C-14 | P | P | P | P | P | Per-namespace MUST/DO-NOT-use vocabulary: all present in table |
| C-15 | P | P | P | P | P | Body vocabulary compliance instruction: all present |
| C-16 | P | P | P | P | P | Stop-gate references classification-derived conditions: all present |
| C-17 | P | P | P | P | P | Inertia extension `-- specifically, {instance}` instruction: all present (V-05 extends to Stage 1+2+3) |
| C-18 | P | P | P | P | P | Named phases + violation mechanism: V-01 step names + behavioral violation satisfies minimum C-18 bar |
| C-19 | P | P | P | P | P | V-01: seed phrases are specific depth-anchored tokens pre-filled per namespace; V-02--V-05: same |
| C-20 | P | P | P | P | P | Body-grounding instruction: all present |
| C-21 | P | P | P | P | P | Skeleton column pre-seeded in template table for all variations |
| C-22 | **F** | P | P | P | P | V-01: "Don't move to the next step until you have finished the current one" = behavioral; V-02--V-05: "category error," "facts about what you are" = ontological |
| C-23 | **F** | P | P | P | P | V-01: no "You ARE..." affirmation anywhere; C-22 FAIL entails C-23 FAIL by staircase |
| C-24 | **F** | P | P | P | P | V-01: no affirmation to evaluate; V-02--V-05: "You ARE the CLASSIFIER" is syntactically first at each role activation |
| C-25 | **F** | P | P | P | P | V-01: "STEP 1 -- CLASSIFY" is occupancy-language; V-02--V-05: "You ARE the CLASSIFIER" is being-language |
| C-26 | P | P | P | P | P | Seeds authored per-namespace in template body for all variations |
| C-27 | **F** | P | P | P | P | V-01 STEP 1 CHECK: "every cell in every row is filled in" -- does not enumerate column names verbatim; V-02--V-05: "Category, MUST use, DO NOT use, Tier 2/3 Critical, Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton" enumerated |
| C-28 | **F** | P | P | P | P | V-01: no field enumeration in gate, so no self-annotation; V-02--V-05: "The column names above are the required field names -- use them verbatim" |
| C-29 | P | P | P | P | P | Seed phrases pre-authored in template body: all variations |
| C-30 | **F** | P | P | P | P | V-01 Step 2: "Rationale: {Write one sentence. Name the evidence type...}" = delegation placeholder; V-02--V-05: per-namespace sentences pre-authored in template body |
| C-31 | P | P | P | P | P | V-01 STEP 1 CHECK: "must be the verbatim seed phrase from the list above, not a paraphrase"; V-02--V-05: identical or stronger |
| C-32 | **F** | **F** | P | P | P | V-01: no pre-authored rationale block exists to cite; V-02 ROLE 2 STOP: "rationale text present" = presence check, not provenance; V-03: "pre-authored rationale above copied verbatim" = names block by location + directs verbatim copy; V-04--V-05: same as V-03 + semantic label |
| C-33 | **F** | **F** | **F** | P | P | V-01--V-02: C-32 FAIL entails C-33 FAIL; V-03 ROLE 2 STOP: "pre-authored **rationale** above copied verbatim" = generic structural label, not semantic identifier "REAL-REQUIRED"; V-04: "pre-authored **REAL-REQUIRED** rationale above copied verbatim"; V-05: same, plus preamble declaration |
| C-34 | **F** | **F** | **F** | **F** | P | V-01--V-03: C-32 or C-33 FAIL entails C-34 FAIL; V-04: uses "REAL-REQUIRED" in gate but no preamble declaration of identifier authority; V-05: preamble explicitly declares "REAL-REQUIRED" as the canonical identifier for the rationale section before any gate reference |
| C-35 | **F** | **F** | **F** | **F** | P | V-01--V-04: inertia extension instruction not instantiated per collection stage; V-05: instruction present at Stage 1, Stage 2, and Stage 3 independently |

---

### Essential / Recommended

All five variations pass all 5 essential criteria (gated phases, classification table, nine rows,
coverage summary, handoff) and all 3 recommended criteria (per-namespace vocabulary, inertia
extension, REAL-REQUIRED blocks). **Essential: 5/5 for all. Recommended: 3/3 for all.**

---

### Aspirational Counts

| Variation | PASS | FAIL | Aspirational (of 27) |
|-----------|------|------|----------------------|
| V-01 | 16 | 11 | 16/27 |
| V-02 | 23 | 4 | 23/27 |
| V-03 | 24 | 3 | 24/27 |
| V-04 | 25 | 2 | 25/27 |
| V-05 | 27 | 0 | 27/27 |

V-01 fails: C-22, C-23, C-24, C-25, C-27, C-28, C-30, C-32, C-33, C-34, C-35
V-02 fails: C-32, C-33, C-34, C-35
V-03 fails: C-33, C-34, C-35
V-04 fails: C-34, C-35
V-05 fails: none

---

### Composite Scores

Formula: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational/27 x 10)`

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.0 | 30.0 | 5.93 | **95.9** |
| V-02 | 60.0 | 30.0 | 8.52 | **98.5** |
| V-03 | 60.0 | 30.0 | 8.89 | **98.9** |
| V-04 | 60.0 | 30.0 | 9.26 | **99.3** |
| V-05 | 60.0 | 30.0 | 10.00 | **100.0** |

**Rank: V-05 > V-04 > V-03 > V-02 > V-01**

---

### C-34 and C-35 Discrimination -- Round 16

| Case | Instantiated by | C-33 | C-34 | C-35 | Signal |
|------|-----------------|------|------|------|--------|
| C-33 FAIL | V-01, V-02, V-03 | FAIL | FAIL | FAIL | No semantic identifier in gate |
| C-33 PASS + C-34 FAIL + C-35 FAIL | V-04 | PASS | FAIL | FAIL | Gate uses "REAL-REQUIRED"; no preamble; single-stage extension |
| C-34 PASS + C-35 PASS | V-05 | PASS | PASS | PASS | Preamble declares "REAL-REQUIRED" canonical; extension at Stage 1+2+3 |

The isolated middle case for C-34 -- a variation that passes C-33 but fails C-34 -- is already
demonstrated by V-04: the gate uses the semantic identifier "REAL-REQUIRED" but the template
preamble contains no declaration of identifier authority. The ceiling case (C-34 PASS) requires
a preamble declaration that precedes gate references.

The C-35 two-way discrimination (C-17 PASS + C-35 FAIL vs C-17 PASS + C-35 PASS) is partially
instantiated: V-05 demonstrates the ceiling. A clean isolated lower case requires a multi-stage
template where the extension instruction appears only at a terminal or composite point.

**Round 17 primary hypothesis:** Construct a variation that achieves C-34 PASS without C-35 PASS
(preamble declaration present, multi-stage extension absent or single-point), and a variation that
achieves C-35 PASS without C-34 PASS (per-stage extension instantiation, no preamble declaration),
to confirm independent discrimination of the two new criteria.
```
