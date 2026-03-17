**campaign-blueprint Quest Score R5 — complete.**

---

### Summary

| Rank | Variation | Score | Key difference |
|---|---|---|---|
| 1 | **V-05** | **140 / 140** | First perfect score — DISCIPLINE RULE (C-13) + four-element pitch structure (C-14) |
| 2 | V-04 | 132.5 | C-17 + C-18 FULL; C-13 + C-14 still partial |
| 3 | V-01 | 130 | C-17 FULL, C-18 PARTIAL (no load-bearing labels) |
| 4T | V-02, V-03 | 122.5 | C-18 FULL, C-09/C-17 FAIL (no contract matrix) |

**Key findings this round:**

- **V-05 is golden (140/140)** — the first perfect score in the campaign-blueprint series. The rubric is now fully addressed.
- **C-17 vs. C-18 are orthogonal** — you can achieve one without the other (V-02/V-03 get C-18, miss C-17; V-01 gets C-17, misses C-18). V-04/V-05 achieve both via explicit preamble declaration.
- **Register invariance confirmed for C-18** — V-02 (table format) and V-03 (conversational questions) score identically. The load-bearing designation achieves C-18 in any register.
- **C-13 and C-14 require structural slots, not instructional prose** — the DISCIPLINE RULE (in-section named rule) and numbered delta statement (element 3 of four) are the key techniques that cross from PARTIAL to FULL.
- **No new rubric patterns extracted** — V-05's perfection confirms the rubric is complete at 140 pts. The three C-19+ hypotheticals (extended audit table, in-section named constraints, structural slot enforcement) are implementation techniques for existing criteria, not new observable properties.

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": []}
```
/arch) | 5 | FAIL | FAIL | FAIL | FAIL | FULL |
| **C-14** Per-audience delta statement in each pitch version | 5 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | FULL |
| **C-15** Pre-artifact forcing function (Phase 0 inertia setup) | 5 | FULL | FULL | FULL | FULL | FULL |
| **C-16** Named do-nothing in setup with propagation rule | 5 | FULL | FULL | FULL | FULL | FULL |
| **C-17** Compound Phase 0 co-location (C-09 + C-15 + C-16 all inside Phase 0) | 5 | FULL | FAIL | FAIL | FULL | FULL |
| **C-18** Canonical Phase 0 form (4-field min + load-bearing labels + density statement) | 5 | PARTIAL | FULL | FULL | FULL | FULL |
| **Total** | **140** | **130** | **122.5** | **122.5** | **132.5** | **140** |

---

### Evidence Notes

**C-08 FULL (all)** -- All R5 variations explicitly state "At least two specific non-boilerplate
gaps. At least one names a missing signal by namespace." The minimum count is now a structural
requirement, unlike R4 where it was implicit.

**C-09 FAIL (V-02, V-03)** -- V-02 and V-03 omit the artifact contract matrix entirely. Phase 0
contains only the four canonical fields plus load-bearing elements. No READ/WRITE/PRESERVE/
CARRIES FORWARD table appears anywhere. V-01, V-04, V-05 carry the matrix in Phase 0
ELEMENT A / ELEMENT 1.

**C-11 FULL (all)** -- All R5 variations enforce "at least one concrete dimension" or stronger.
V-05 provides a three-part template (Time/Effort/Risk with N/A slots). V-01 uses "[Option 0
cost -- concrete dimension]" as a forced slot in the proposal Cons cell. Qualitative-only
descriptions are prohibited by instruction in all five.

**C-12 FULL (all)** -- All variations include explicit output gate tokens: [PHASE 0 COMPLETE],
[SPEC WRITTEN], [PROPOSAL WRITTEN -- Option {X} recommended], [PITCH WRITTEN]. First round
where C-12 reaches FULL across all variations. R4 used disk-existence gates rather than visible
output tags.

**C-13 FAIL (V-01 through V-04)** -- "At least two specific gaps. At least one names a signal
namespace" routes executors to signal namespaces (scout-requirements, prove-interview,
trace-contract) but does not split by domain. The product/user vs. technical/architecture
discipline split is absent.

**C-13 FULL (V-05)** -- DISCIPLINE RULE is embedded as an in-section named instruction inside
the SPEC's OPEN QUESTIONS block: "include at least one question from the product/user domain
AND at least one from the technical/architecture domain." Compliance is auditable by inspection.
First time C-13 reaches FULL in any campaign-blueprint round.

**C-14 PARTIAL (V-01 through V-04)** -- EXEC/DEV/MAKER sections have differentiated hooks,
framing, and CTAs but no structural slot for an explicit "What changes for [audience] is [X]"
delta statement. Audience tone differentiation is present; named delta is absent.

**C-14 FULL (V-05)** -- V-05 defines a four-element structure per pitch version: (1) Hook,
(2) What it does, (3) Delta statement ("What changes for [audience] is [X]"), (4) CTA. Element
3 is a distinct numbered slot separate from the hook and why-it-matters framing. EXEC/DEV/MAKER
deltas are defined (outcome/risk eliminated / capability unlocked / daily task that disappears).
First time C-14 reaches FULL in any campaign-blueprint round.

**C-16 FULL (all)** -- Option 0 naming and propagation rule appear in Phase 0 for all five
variations. Direct fix for R4 failure (Option 0 named only at proposal time). Propagation
verbatim from Phase 0 -> proposal row 0 -> pitch framing is explicit in all five.

**C-17 FAIL (V-02, V-03)** -- V-02 and V-03 satisfy C-15 and C-16 but fail C-09 (no contract
matrix). C-17 requires all three co-located. The pure-canonical-form approach achieves minimal
sufficient Phase 0 while sacrificing the compound gate property.

**C-17 FULL (V-01, V-04, V-05)** -- Contract matrix (Element A/Element 1) + forcing function
(Element B/Element 2) + named do-nothing propagation (Element C/Element 3) are all physically
co-located inside Phase 0 with a single gate token closing all three simultaneously. V-04/V-05
additionally name the co-location as an explicit structural property: "All three are declared
here, together... no separate declaration step elsewhere that can be deferred."

**C-18 PARTIAL (V-01)** -- V-01 has all four fields distributed across Element B (Topic,
Inertia, Scout inventory) and Element C (Option 0 name, Option 0 cost). Gate token and
propagation rule are present. But: fields are not labeled as a "minimum form," no statement
that density beyond them is not required, gate marker and propagation rule are not labeled
"load-bearing." V-01 achieves C-18 substance through structural coincidence rather than
explicit designation.

**C-18 FULL (V-02, V-03, V-04, V-05)** -- V-02: "Four fields... these are the minimum
required for Phase 0 to be complete. Additional fields are permitted but are not required --
density beyond these four does not change Phase 0 compliance status." Gate marker and
propagation rule labeled "(load-bearing)" inline. V-03: "More context is fine if you have it,
but it is not required for this phase to be complete" and calls gate/propagation "not optional."
V-04/V-05: "Phase 0 minimum form: four fields... Density beyond these four is permitted but is
not required... The gate marker and propagation rule are the load-bearing elements -- they are
not optional even when the four fields are filled."

---

### Ranking

| Rank | Variation | Score | Golden? | Notes |
|---|---|---|---|---|
| 1 | **V-05** | **140 / 140 (100%)** | **YES** | First perfect score in campaign-blueprint series |
| 2 | V-04 | 132.5 / 140 (94.6%) | YES | C-17 + C-18 FULL; C-13 FAIL, C-14 PARTIAL |
| 3 | V-01 | 130 / 140 (92.9%) | YES | C-17 FULL, C-18 PARTIAL; C-13 FAIL, C-14 PARTIAL |
| 4 (T) | V-02 | 122.5 / 140 (87.5%) | YES | C-18 FULL; C-09 FAIL drives C-17 FAIL |
| 4 (T) | V-03 | 122.5 / 140 (87.5%) | YES | C-18 FULL; C-09 FAIL drives C-17 FAIL; register invariant with V-02 |

All five variations pass golden threshold (all 5 essentials FULL + composite >= 94/140).
V-05 is the first variation in the campaign-blueprint series to achieve 140/140.

---

### Axis Diagnostics

**Axis A alone (V-01) vs. A + B combined (V-04):**
V-01 achieves C-17 FULL but C-18 PARTIAL. The compound gate structure satisfies co-location,
but absent the explicit "minimum form / density not required / load-bearing" designation, C-18
scores PARTIAL. V-04 adds these designations in the Phase 0 preamble and achieves both FULL.
The preamble statement is the marginal element for C-18 -- not the presence of the 4 fields
(V-01 also has them), but the explicit naming of them as load-bearing.

**Axis B alone (V-02) vs. A + B combined (V-04):**
V-02 achieves C-18 FULL but fails C-09 and C-17. The canonical minimal Phase 0 correctly
designates load-bearing elements but omits the contract matrix. V-04 demonstrates both are
compatible in a single Phase 0 block without contradiction.

**Axis C (conversational register, V-03) as control:**
V-03 scores identically to V-02 (122.5). Register (formal table vs. conversational questions)
has zero scoring effect when structural criteria are the same. The "load-bearing" designation
achieves C-18 regardless of whether it appears as a table label or as prose. Register
invariance confirmed for C-18.

**Axis E (full stack, V-05) closes the rubric:**
V-05 achieves all 10 aspirational criteria simultaneously, confirming criteria are mutually
compatible. Additions over V-04: DISCIPLINE RULE (C-13), four-element pitch structure with
named delta slot (C-14), three-part cost template (C-11 strengthened). None conflict with
Phase 0 compound gate structure.

---

### Excellence Signals

From V-05 (140/140, the new benchmark):

**1. DISCIPLINE RULE as in-section named constraint (C-13 path)**
Placing an explicit named rule inside the artifact section it governs ("DISCIPLINE RULE:
include at least one question from product/user domain AND at least one from technical/
architecture domain") converts C-13 from an observer judgment into an executor instruction.
Checkable by inspection of the OPEN QUESTIONS section. Contrast: namespace-routing alone
("name the signal namespace that could resolve it") sends the executor to the right tooling
but does not enforce domain coverage.

**2. Named structural slot as delta enforcement (C-14 path)**
V-05's four-element pitch version structure (1. Hook, 2. What it does, 3. Delta statement,
4. CTA) achieves C-14 FULL where all prior variations achieved PARTIAL. The delta statement
is numbered, labeled "DELTA STATEMENT: 'What changes for [audience] is [X]'", and
distinguished explicitly from the hook. Making it a structural element -- not an embedded
instruction in a paragraph -- forces the executor to produce a distinct named delta, not
merely audience-appropriate framing.

**3. Cost template vs. cost instruction (C-11 confirmation)**
V-05's three-part template (Time dimension / Effort dimension / Risk dimension, each with
N/A slot) achieves C-11 at higher compliance confidence than "at least one concrete dimension"
alone. The template makes under-compliance visible by structural absence -- an executor cannot
fill in "users struggle with this" because the template fields demand a format.

**4. Phase 0 preamble as prerequisite contract**
V-04 and V-05 open Phase 0 with a preamble: "Three elements. All co-located here. An executor
who completes Phase 0 satisfies all three simultaneously." This declaration is the load-bearing
difference between V-01 (C-18 PARTIAL) and V-04 (C-18 FULL). Structural properties need to be
declared, not just exhibited -- the rubric rewards visible intent, not emergent structure.

---

### Gaps to Ceiling from V-04 (132.5 -> 140)

| Gap | What's missing | Points |
|---|---|---|
| C-13 | DISCIPLINE RULE in SPEC section: product/user + technical/arch domain split | 5 |
| C-14 | Named structural slot (element 3: Delta statement) in each pitch version | 2.5 |
| **Total** | | **7.5** |

V-04 + C-13 fix + C-14 fix = 140. The two missing criteria are independent additions with no
structural conflict with the Phase 0 compound gate.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": []}
```
