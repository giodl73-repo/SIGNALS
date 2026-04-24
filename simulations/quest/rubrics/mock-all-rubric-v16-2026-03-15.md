# mock-all Quest Rubric -- v16

## New criteria extracted from Round 15

**C-33** -- *ROLE 2 stop-gate's provenance reference names the template section by its semantic role identifier, binding the gate condition to a specific machine-readable section label*

Extracted from ES-R15 (V-05). C-32 requires the ROLE 2 stop-gate to name the pre-authored block and direct verbatim copy. V-05's gate goes one step further: *"with the pre-authored REAL-REQUIRED rationale above copied verbatim"* -- it names the rationale content using the template section's own semantic role label ("REAL-REQUIRED") rather than a generic structural reference ("the pre-authored block" or "the pre-authored rationale above"). The semantic label is the section identifier assigned in the template body itself; using it in the gate creates a machine-readable binding between the gate condition and the named section. V-01 through V-04 fail C-33: V-01–V-03 fail C-32 (no pre-authored block is named at all); V-04 fails C-32 (gate checks presence, not provenance); no gate among V-01–V-04 uses the "REAL-REQUIRED" semantic identifier. C-33 is a strict refinement of C-32: C-33 pass implies C-32 pass; C-32 pass does not imply C-33 pass (a gate saying "pre-authored rationale above copied verbatim" satisfies C-32 but not C-33, because the semantic section label is absent). C-33 extends the rationale-authorship chain to a fourth rung. It is structurally parallel to the C-28 pattern applied to the rationale chain: where C-28 requires the stop-gate field enumeration to name the classification table's own column headers verbatim (making the table-gate coupling self-documenting), C-33 requires the stop-gate provenance reference to name the template section by its own semantic identifier (making the rationale-gate coupling self-documenting).

---

**Denominator: 24 --> 25**
**Formula: `(essential_pass/5 x 60) + (recommended_pass/3 x 30) + (aspirational/25 x 10)`**
**C-33 is in the rationale-authorship chain. It is not part of the identity staircase or the gap-content chain.**

---

Key structural additions in v16:

**Rationale-authorship chain extends to four rungs:** C-13 (rationale block present) --> C-30 (rationale template-authored) --> C-32 (gate enforces provenance + fidelity) --> C-33 (gate uses semantic section identifier).

**Structural parallel to C-28 confirmed:** The self-documenting gate principle now applies to both sub-chains. C-28 requires the gate's field enumeration to name the table's column headers by their verbatim identifiers; C-33 requires the gate's provenance reference to name the rationale section by its semantic role identifier. Both make structural dependencies machine-readable from the gate text alone.

**Table-coupling cluster expands** from 16 to 17 criteria (adding C-33).

**Round 16 primary hypothesis:** Confirm C-33 three-way discrimination -- (C-32 FAIL + C-33 FAIL), (C-32 PASS + C-33 FAIL), (C-32 PASS + C-33 PASS). The isolated middle case requires a variation whose ROLE 2 gate references a pre-authored block with generic language (e.g., "with the pre-authored rationale above copied verbatim") rather than the section's semantic identifier, passing C-32 but failing C-33.

---

## Version History

**v1** -- established core essential criteria (C-01 to C-04) and initial recommended tier.

**v2 through v6** -- iterative refinement of essential/recommended criteria; no aspirational tier additions in this range.

**v7** added two aspirational criteria (C-19 to C-20) extracted from Round 6 excellence signals: depth anchor inside placeholder token (C-19), and inertia question grounding artifact body semantics (C-20).

**v8** skipped (confirmation round; no new criteria).

**v9** added three aspirational criteria (C-21 to C-22) extracted from Round 8 excellence signals: inertia gap skeleton pre-seeded in classification table (C-21), and identity-violation mechanism must be ontological self-contradiction rather than behavioral prohibition (C-22). Denominator +2.

**v10** added one aspirational criterion (C-23) extracted from Round 9 excellence signals: positive identity affirmation must appear at each per-role activation header, not deferred to a preamble. Denominator +1.

**v11** added two aspirational criteria (C-24 to C-25) extracted from Round 10 excellence signals: positive identity affirmation must be syntactically first in each per-role header (C-24; elevated from C-23 diagnostic to standalone pass condition -- V-02 demonstrated the ceiling: "fires as syntactically first element at ROLE 1, ROLE 2, ROLE 3, and ROLE 4 activations"), and per-role headers must use being-language rather than occupancy-language (C-25; V-01 diagnostic: "conditional phrasing describes the model as *in* a role, not *being* it" -- "In the CLASSIFIER role" asserts positional occupancy; "You ARE the CLASSIFIER" asserts identity; these are linguistically distinct and C-25 prohibits the occupancy form explicitly). Denominator +2.

**v12** added two aspirational criteria (C-26 to C-27) extracted from Round 11 excellence signals: inertia gap skeleton column entries authored per-namespace at classification time (C-26; prerequisite for the C-21 + C-10 + C-17 three-criteria structural coupling -- V-05 demonstrated that per-namespace specificity in the table rows at construction time is what makes the coupling pass, not merely the column's presence), and stop-gate field enumeration names the classification table's own column headers verbatim (C-27; V-05 pattern: "the enumerated fields ARE the table columns -- C-16 compliance comes naturally when the stop-gate condition mirrors the table structure," making C-16 + C-11 + C-14 self-reinforcing from one structural choice). Denominator +2 (17 --> 19).

**v13** added two aspirational criteria (C-28 to C-29) extracted from Round 12 excellence signals: stop-gate self-annotation explicitly declares its enumerated field list as the required verbatim column names (C-28; V-02 R12 excellence -- the gate annotation "The column names above are the required field names -- use them verbatim" makes the table-gate coupling self-documenting and machine-readable, elevating C-27 from a naming constraint to a structural declaration), and inertia gap skeleton seed content is pre-authored in the skill template body rather than delegated to model-time generation (C-29; V-01 vs V-02 R12 contrast -- V-01 C-26 PASS because skill template provides seed phrases model copies verbatim; V-02 C-26 PARTIAL because template delegates generation to model, structural guarantee absent; C-29 is the authorship-residency ceiling above C-26). Denominator +2 (19 --> 21).

**v14** added one aspirational criterion (C-30) extracted from Round 13 excellence signals: ROLE 2 REAL-REQUIRED rationale content is pre-authored in the skill template body rather than delegated to model-time generation (C-30; V-03 R13 C-13 PARTIAL -- template supplies only a delegation instruction "one sentence explaining why real artifacts are required for this namespace" with no seed content; V-01 and V-02 passed C-13 because their templates pre-author rationale seed text the model copies or minimally adapts; C-30 applies the same authorship-residency principle that C-29 applies to skeleton gap phrases, but to the ROLE 2 rationale field; both criteria share the structural guarantee logic: template-authored content gives deterministic quality, model-generated content gives probabilistic quality). Denominator +1 (21 --> 22).

**v15** added two aspirational criteria (C-31 to C-32) extracted from Round 14 excellence signals: ROLE 1 stop-gate enforces skeleton seed provenance by citing the template seed list and prohibiting paraphrase (C-31; V-04 and V-05 R14 -- gate says "must be the verbatim seed phrase from the list above" / "not a paraphrase"; V-01 R14 diagnostic: C-29 PASS but C-31 FAIL because gate uses paraphrase field descriptions and does not cite the seed list as the authoritative source; C-31 is the gate-level ceiling above C-29, forming the fourth rung of the gap-content chain), and ROLE 2 stop-gate enforces rationale provenance by naming the pre-authored block and directing verbatim copy (C-32; V-01, V-04, and V-05 R14 -- ROLE 2 STOP says "with the pre-authored rationale above copied verbatim"; V-02 and V-03 R14 fail because no pre-authored rationale exists to cite; C-32 is structurally parallel to C-28 applied to the rationale-authorship chain; C-32 is the gate-level ceiling above C-30, forming the third rung of the rationale-authorship chain). Denominator +2 (22 --> 24).

**v16** added one aspirational criterion (C-33) extracted from Round 15 excellence signals: ROLE 2 stop-gate's provenance reference names the template section by its semantic role identifier rather than a generic structural reference (C-33; V-05 R15 -- gate says "with the pre-authored REAL-REQUIRED rationale above copied verbatim," using "REAL-REQUIRED" as the semantic section identifier assigned in the template body itself; V-01--V-04 fail because either C-32 fails (no block named at all) or the gate names presence without using the section identifier; C-33 is a strict refinement of C-32: C-33 pass implies C-32 pass, C-32 pass does not imply C-33 pass; C-33 extends the rationale-authorship chain to a fourth rung and is structurally parallel to C-28 -- both make structural dependencies machine-readable from the gate text alone, one via column header self-declaration, the other via semantic section identifier). Denominator +1 (24 --> 25).

---

## Identity Staircase (C-18 through C-25)

Five rungs, each a strict refinement of the one below:

- **C-18**: named role + any violation mechanism
- **C-22**: violation mechanism must be ontological (not behavioral)
- **C-23**: affirmation must appear at each activation (not only preamble)
- **C-24**: affirmation must be syntactically first (not just present)
- **C-25**: affirmation must use being-language (not occupancy-language)

C-26 through C-33 are not part of the identity staircase. They belong to the table-coupling cluster and its sub-chains, which govern the inertia/classification table structural design and ROLE 2 content provenance.

---

## Table-Coupling Cluster (C-10, C-11, C-13 to C-17, C-19 to C-21, C-26 to C-33)

Scorecard with excellence signals:

## mock-all Quest Score — Round 15 (scored under v16)

**Rubric:** v16 | **Variations:** V-01 through V-05 | **Denominator:** 25 aspirational criteria

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
| C-17 | P | P | P | P | P | Inertia extension `-- specifically, {instance}` instruction: all present |
| C-18 | P | P | P | P | P | Named roles + violation mechanism stated: all present (V-01 steps have names + behavioral violation stated) |
| C-19 | **F** | P | P | P | P | V-01: delegation placeholder `{write a phrase...}` has no depth-anchored seed; V-02--V-05: verbatim seed phrases ARE the depth anchors |
| C-20 | P | P | P | P | P | Body-grounding instruction: all present |
| C-21 | **F** | P | P | P | P | V-01: skeleton column is delegation placeholder, not pre-seeded |
| C-22 | **F** | P | P | P | P | V-01: "Don't jump ahead -- moving to a later step skips required work" = behavioral; V-02--V-05: ontological framing ("category error," "that is a fact about what you are") |
| C-23 | **F** | P | P | P | P | V-01: no "You ARE..." affirmation anywhere; C-22 FAIL entails C-23 FAIL by staircase |
| C-24 | **F** | P | P | P | P | V-01: no affirmation to evaluate; V-02--V-05: "You ARE the CLASSIFIER" is syntactically first in each role section |
| C-25 | **F** | P | P | P | P | V-01: step naming ("STEP 1 -- CLASSIFY") is occupancy-language; V-02--V-05: "You ARE..." is being-language |
| C-26 | **F** | P | P | P | P | V-01: entries are model-generated at runtime; V-02--V-05: per-namespace seed phrases are pre-authored in template body |
| C-27 | **F** | P | P | P | P | V-01: gate says "Any empty cell" without naming column headers; V-02--V-05: gate enumerates "Category, MUST use, DO NOT use, Tier 2/3 Critical, Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton" verbatim |
| C-28 | **F** | P | P | P | P | V-01: no field enumeration in gate; V-02--V-04: enumeration in gate self-annotates the required column names; V-05: also adds explicit declaration "The column names above are the required field names -- use them verbatim" |
| C-29 | **F** | P | P | P | P | V-01: delegation `{write a phrase specific...}`; V-02--V-05: seed list pre-authored in template body |
| C-30 | **F** | **F** | **F** | P | P | V-01--V-03: delegation placeholder for rationale; V-04--V-05: pre-authored rationale block ("Empirical validation of the core hypothesis requires actual prototype output...") |
| C-31 | **F** | **F** | P | P | P | V-01: no seed list exists to cite; V-02: gate says "non-empty for every row" -- no list citation, no paraphrase prohibition; V-03--V-05: gate says "must be the verbatim seed phrase from the list above, not a paraphrase" |
| C-32 | **F** | **F** | **F** | **F** | P | V-01--V-03: no pre-authored rationale to name; V-04: gate says "rationale text present" -- checks presence not provenance; V-05: gate says "with the pre-authored REAL-REQUIRED rationale above copied verbatim" |
| C-33 | **F** | **F** | **F** | **F** | P | V-01--V-03: fail C-32, no semantic section identifier possible; V-04: gate says "rationale text present" -- no section identifier, no provenance reference; V-05: "REAL-REQUIRED rationale" names the section by its semantic role identifier assigned in the template body |

---

### Essential / Recommended

All five variations pass all 5 essential criteria (four gated phases, classification table, nine rows, coverage summary, handoff) and all 3 recommended criteria (per-namespace vocab, inertia extension, REAL-REQUIRED blocks). **Essential: 5/5 for all. Recommended: 3/3 for all.**

---

### Aspirational Counts

| Variation | PASS | FAIL | Aspirational (of 25) |
|-----------|------|------|----------------------|
| V-01 | 11 | 14 | 11/25 |
| V-02 | 21 | 4 | 21/25 |
| V-03 | 22 | 3 | 22/25 |
| V-04 | 23 | 2 | 23/25 |
| V-05 | 25 | 0 | 25/25 |

V-01 fails: C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 (14 fails)
V-02 fails: C-30, C-31, C-32, C-33
V-03 fails: C-30, C-32, C-33
V-04 fails: C-32, C-33
V-05 fails: none

---

### Composite Scores

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/25 × 10)`

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.0 | 30.0 | 4.40 | **94.4** |
| V-02 | 60.0 | 30.0 | 8.40 | **98.4** |
| V-03 | 60.0 | 30.0 | 8.80 | **98.8** |
| V-04 | 60.0 | 30.0 | 9.20 | **99.2** |
| V-05 | 60.0 | 30.0 | 10.00 | **100.0** |

**Rank: V-05 > V-04 > V-03 > V-02 > V-01**

---

### C-33 Discrimination -- Round 16 Setup

**Chain 2 extended (C-30 / C-32 / C-33):**

| Case | Instantiated by | C-30 | C-32 | C-33 |
|------|-----------------|------|------|------|
| Bottom | V-01, V-02, V-03 | FAIL | FAIL | FAIL |
| Middle-low | V-04 | PASS | FAIL | FAIL |
| Middle-high | (not yet instantiated) | PASS | PASS | FAIL |
| Ceiling | V-05 | PASS | PASS | PASS |

The middle-high case -- a variation whose ROLE 2 gate references "the pre-authored rationale above copied verbatim" (passing C-32) but omits the semantic section identifier (failing C-33) -- has not yet been instantiated. Round 16's primary hypothesis is to produce this case, confirming that C-33 discriminates independently above C-32. V-04 remains the isolated C-32 middle case; the Round 16 goal is to isolate a C-33 middle case.
