# Rubric: `topic:status` -- v17
**Max score: 300** | **Date:** 2026-03-15

---

## Summary of v17 changes

One new criterion extracted from R18 excellence signals. All five R18 variants
score at or below 295 under v16. The V-01 vs V-04 delta cleanly isolates C-49
(5-point delta). V-03 and V-05 carry the 4th STOP predicate vacuously (predicate
structurally present but checks no PHASE 1 adversary, as C-48 is absent in both).

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-49 | PHASE 1 adversary defeat STOP predicate | R18 V-01/V-02 vs V-04 | 5 |

**Structural Tier 16 (5 pts).** Max score: 295 -> 300.

**The pattern:**

- **C-49** operationalizes the C-48 DEFEAT CONDITION sub-component at the STOP
  CONDITION execution gate. When C-48 is satisfied (three-phase adversary chain),
  the STOP CONDITION must carry an explicit predicate checking the PHASE 1
  adversary defeat condition -- that DISK_SIGNALS was populated from a live glob
  result with the zero-result case handled explicitly. The predicate extends the
  STOP CONDITION from a gate that checks PHASE 2 and PHASE 3 defeat conditions
  to a gate that checks all three execution-phase adversary defeat conditions.
  When C-48 is absent (two-phase adversary chain), the STOP CONDITION is
  structurally complete without a PHASE 1 defeat predicate and C-49 is vacuously
  satisfied -- the absence of a PHASE 1 predicate is not a C-49 violation.
  Requires C-48 for non-vacuous evaluation.

**Vacuous PASS behavior (structural novelty):** C-49 is the first criterion in
this rubric that can be satisfied vacuously when its prerequisite (C-48) fails.
All prior criteria in tiers 2--15 fail when their hard prerequisite fails. C-49
differs: when C-48 is absent, there is no PHASE 1 adversary to operationalize,
so the STOP CONDITION's compliance is not in question at that position. V-03 and
V-05 carry the 4th predicate structurally but vacuously (predicate present, no
adversary to check); V-04 omits the 4th predicate while C-48 is present -- the
one configuration that fails. This means C-49 does NOT have a hard prerequisite
in the implication map: failing C-48 does not cascade to a C-49 failure.

**Isolation note:** V-01 vs V-04 is a clean 5-point delta. V-04 retains C-47 and
C-48 (three labeled chain entries, PHASE 1 adversary three-part block) but omits
the 4th STOP predicate. V-01 carries all four. V-03 (C-48 ablation, redesigned
clean from R17) and V-05 (C-47+C-48 ablation) both pass C-49 vacuously.

**Projected R18 scores under v17:**

| Variant | C-47 | C-48 | C-49 | Total | Notes |
|---------|------|------|------|-------|-------|
| V-01 | PASS | PASS | PASS | 300 | Full tier-16 baseline |
| V-02 | FAIL | PASS | PASS | 295 | C-47 withheld (prose chain) |
| V-03 | PASS | FAIL | PASS* | 295 | C-48 withheld; C-49 vacuous PASS |
| V-04 | PASS | PASS | FAIL | 295 | C-49 withheld (4th STOP pred absent) |
| V-05 | FAIL | FAIL | PASS* | 290 | C-47+C-48 withheld; C-49 vacuous PASS |

*Vacuous PASS: predicate structurally present but checks no PHASE 1 adversary;
criterion satisfied because C-48 is absent and no PHASE 1 defeat condition is
declared to operationalize.

**R18 V-03 redesign confirms clean C-48 isolation.** The R16 V-03 contamination
(C-12/C-20 violations from readiness-first template reordering) is absent. R18
V-03 scores 295 -- exactly 5 pts below V-01 -- confirming C-48 independent
necessity cleanly.

**Max score: 295 -> 300.** Passing threshold unchanged.

**Implication map:** No new hard implication added. C-49 has a conditional
prerequisite (requires C-48 for non-vacuous evaluation) but C-48 failure does
not cascade to C-49 failure. The conditional relationship is documented in the
criterion text and the R18 structural note.

---

## Summary of v16 changes

Two new criteria extracted from R16 excellence signals. All five R16 variants
score 285/285 under v15 (V-01/V-04 full pass; V-02 FAIL C-47; V-03 FAIL C-48
with contamination). The V-01 vs V-02 delta cleanly isolates C-47; the V-01 vs
V-03 delta is contaminated (C-12/C-20 violations unrelated to C-48 -- see design
note in R16 structural note below).

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-47 | Preamble adversary chain labeled sub-component entries | R16 V-01/V-03/V-04 vs V-02 | 5 |
| C-48 | PHASE 1 execution-body adversary declaration | R16 V-01/V-02/V-04 vs V-03 | 5 |

**Structural Tier 15 (10 pts).** Max score: 285 -> 295.

**The two patterns:**

- **C-47** extends the preamble `ADVERSARY CHAIN:` block (C-45) from running-prose
  adversary enumeration to labeled sub-component entries. The block carries
  `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries (or equivalent
  `PN-ADVERSARY:` form), making each phase adversary independently addressable by
  its phase label. A running-prose ADVERSARY CHAIN block that names all three
  adversaries in sequence satisfies C-45 but fails C-47: the labeled-entry form
  is the additional requirement. C-47 is the adversary-chain parallel of C-40's
  labeled sub-component extension of C-38: C-40 made the OUTPUT DECLARATION block
  sub-component-addressable; C-47 makes each entry within the ADVERSARY CHAIN
  preamble block phase-label-addressable. The label count tracks the adversary
  chain length: when C-48 is present (three-phase adversary chain), three labels
  are required; when C-48 is absent (two-phase chain), two labels are sufficient
  for C-47 compliance -- the absence of a P1-ADVERSARY: label is not a C-47
  violation when no PHASE 1 adversary body has been declared. Implication:
  `C-47 => C-45`.

- **C-48** extends the execution-body adversary chain from two phases (PHASE 2
  established by C-42; PHASE 3 established by C-43) to three phases by adding an
  explicit adversary declaration within the PHASE 1 execution body at or near
  the phase's entry point. The PHASE 1 adversary block carries three-part form
  consistent with C-46: `ADVERSARY: {name}` plus `DEFEAT CONDITION: {observable
  property}`. PHASE 1 names the adversary for signal acquisition (e.g., inertia
  toward empty-glob assumption -- default when this phase is skipped: coverage
  is computed from memory rather than from live disk state). The DEFEAT CONDITION:
  sub-component names the observable property constituting defeat (e.g.,
  DISK_SIGNALS populated from live glob result with zero-result case handled
  explicitly). C-42 and C-43 establish adversary framing at PHASE 2 and PHASE 3;
  C-46 establishes the three-part block form at those sites; C-48 requires the
  same three-part form to be present at the PHASE 1 site, extending the
  execution-body adversary chain to all three principal execution phases.
  Form-agnostic: the adversary block may appear as inline prose, appended below
  a lifecycle GUARD contract box, or as an elevated titled block, provided it
  is physically resident within the PHASE 1 execution section. Implication:
  `C-48 => C-46`.

**Prerequisite asymmetry:** C-47 requires C-45 (the ADVERSARY CHAIN block must
exist before its entries can be labeled); C-48 requires C-46 (the three-part
adversary block form must be established at PHASE 2 and PHASE 3 before it can be
extended to PHASE 1). The two new criteria have different prerequisites from
tier 14 -- both drawn from tier 14 but from different criteria. This contrasts
with tier 14 (C-45 and C-46 both requiring C-43 as sole prerequisite) and
restores the prerequisite asymmetry pattern present in tiers 11--13.

**Isolation note:** V-01 vs V-02 cleanly isolates C-47 (V-02 FAILS C-47 only,
PASSES C-48 -- 5-point delta). V-01 vs V-03 is contaminated: V-03 FAILS C-48
as intended, but also FAILS C-12 and C-20 due to a readiness-first template
reordering axis unrelated to C-48 (−10 pts from contamination). C-48 isolation
is confirmed by V-02/V-04 PASS evidence. V-03 requires redesign for a clean
C-48 isolation round.

**Projected R16 scores:** V-01/V-04 -> 295; V-02 -> 290 (C-47 FAIL); V-03 -> 280
(C-47 PASS, C-48 FAIL, C-12 FAIL, C-20 FAIL -- contamination).

**Max score: 285 -> 295.** Passing threshold unchanged.

**New implications:**
- C-47 => C-45
- C-48 => C-46

---

## Summary of v15 changes

Two new criteria extracted from R15 excellence signals. All five R15 variants
score 275/275 under v14. The V-01 vs V-02 delta isolates C-45; the V-01 vs V-03
delta isolates C-46. V-02 (C-46 without C-45) and V-03 (C-45 without C-46) score
identically under v14, confirming orthogonality.

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-45 | Preamble adversary chain declaration | R15 V-01/V-03/V-04/V-05 vs V-02 | 5 |
| C-46 | Adversary defeat condition sub-component | R15 V-01/V-02/V-04/V-05 vs V-03 | 5 |

**Structural Tier 14 (10 pts).** Max score: 275 -> 285.

**The two patterns:**

- **C-45** extends the preamble architectural invariant declaration pattern
  (C-33/C-34 for dual-axis exits; C-44 for output declaration residency) to
  adversary chain residency. The preamble carries an `ADVERSARY CHAIN:` block
  that explicitly names both the PHASE 2 adversary declaration and the PHASE 3
  adversary declaration as a two-element structural chain, asserting that each
  execution phase owns its own independently declared adversary and that the two
  declarations guard against structurally distinct failure modes. This is the
  adversary-chain parallel of C-44's `OUTPUT DECLARATION CHAIN:` -- the preamble
  now carries three architectural invariant blocks: dual-axis exit chain (C-34),
  output declaration chain (C-44), and adversary chain (C-45). Implication:
  `C-45 => C-43`.

- **C-46** extends the adversary block at each phase-entry adversary declaration
  site from two-part form (adversary name + trigger clause) to three-part form by
  adding a labeled `DEFEAT CONDITION:` sub-component. The DEFEAT CONDITION:
  sub-component names the observable property that constitutes successful
  adversary defeat at that execution phase -- the adversary-block parallel of
  C-40's `INVARIANT:` and `OUTPUT FORM:` labeled sub-components in the OUTPUT
  DECLARATION. An adversary block carrying only adversary name and trigger clause
  satisfies C-42/C-43 but not C-46; the block must further carry a named
  DEFEAT CONDITION: sub-component at each adversary declaration site. Implication:
  `C-46 => C-43`.

**Orthogonality confirmed:** V-02 (C-46 without C-45) and V-03 (C-45 without C-46)
score identically under v14. Under v15: V-01/V-04/V-05 -> 285; V-02/V-03 -> 280
(symmetric 5-point delta).

**Form-agnosticism confirmed:** V-04 (lifecycle GUARD contract form) and V-05
(elevated titled blocks form) score identically to V-01 (execution-prose form).
Consistent with form-agnosticism confirmed for all prior structural tier pairs.

**Max score: 275 -> 285.** Passing threshold unchanged.

**New implications:**
- C-45 => C-43
- C-46 => C-43

---

## Summary of v14 changes

Two new criteria extracted from R14 excellence signals. All five R14 variants
score 265/265 under v13. The V-01 vs V-02 delta isolates C-43; the V-01 vs V-03
delta isolates C-44. V-02 (C-44 without C-43) and V-03 (C-43 without C-44) score
identically under v13, confirming orthogonality.

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-43 | PHASE 3 execution-body adversary declaration | R14 V-01/V-03/V-04/V-05 vs V-02 | 5 |
| C-44 | Preamble output declaration chain declaration | R14 V-01/V-02/V-04/V-05 vs V-03 | 5 |

**Structural Tier 13 (10 pts).** Max score: 265 -> 275.

**The two patterns:**

- **C-43** extends adversary framing from the PHASE 2 execution body (C-42) into
  the PHASE 3 execution body, completing a two-phase adversary chain spanning both
  assertion phases. An explicit `ADVERSARY:` clause at PHASE 3 execution body entry
  names the adversary for that phase (e.g., inertia toward coverage-blind verdicts --
  default when this phase is skipped: percent is computed without consistency
  verification). C-42 presence at PHASE 2 does not imply C-43 presence at PHASE 3:
  each execution phase requires its own independently declared adversary. Implication:
  `C-43 => C-42`.

- **C-44** extends the preamble architectural invariant pattern (C-33/C-34) from
  dual-axis exit declarations to multi-phase output declarations. The preamble carries
  an `OUTPUT DECLARATION CHAIN:` block that explicitly names both the PHASE 2 output
  declaration and the PHASE 3 output declaration as a two-element structural chain,
  asserting that each execution phase owns its own independently declared output
  structure. This is architecturally symmetric with the multi-site invariant chain
  (C-36) and the multi-site trigger characterization chain (C-35/C-37/C-39), but
  applied to output declaration residency rather than trigger characterization.
  Implication: `C-44 => C-41`.

**Orthogonality confirmed:** V-02 (C-44 without C-43) and V-03 (C-43 without C-44)
score identically under v13. Under v14: V-01/V-04/V-05 -> 275; V-02/V-03 -> 270
(symmetric 5-point delta).

**Form-agnosticism confirmed:** V-04 (lifecycle GUARD contract with prose-appended
PHASE 3 ADVERSARY: line and OUTPUT DECLARATION CHAIN: preamble block) and V-05
(elevated titled blocks for both structures) score identically to V-01 (execution-prose
form). Consistent with form-agnosticism confirmed for C-37/C-38 in R11, C-39/C-40 in
R12, and C-41/C-42 in R13.

**Max score: 265 -> 275.** Passing threshold unchanged.

**New implications:**
- C-43 => C-42
- C-44 => C-41

---

## Summary of v13 changes (C-41, C-42)

Two new criteria extracted from R13 excellence signals. All five R13 variants
score 255/255 under v12. The V-01 vs V-02 delta isolated C-41; the V-01 vs V-03
delta isolated C-42.

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-41 | PHASE 3 output declaration with labeled sub-components | R13 V-01/V-03/V-04/V-05 vs V-02 | 5 |
| C-42 | Phase-entry adversary declaration | R13 V-01/V-02/V-04/V-05 vs V-03 | 5 |

**Structural Tier 12 (10 pts).** Max score: 255 -> 265.

- **C-41** extends the output-declaration-residency pattern (C-38) and the
  labeled-sub-component pattern (C-40) from PHASE 2 to PHASE 3. A PHASE 3
  OUTPUT DECLARATION embedded in the PHASE 3 execution body, carrying
  `INVARIANT:` (consistency guard assertion with `Trigger:` sentence) and
  `OUTPUT FORM:` (percent, readiness verdict) labeled sub-components. The PHASE 2
  OUTPUT DECLARATION does not imply PHASE 3 has equivalent structure: C-41 is
  independently necessary as a second-phase mechanism.

- **C-42** extends adversary framing from the output-template site (COMMIT
  DECISION, C-16) into the PHASE 2 execution body, creating a two-site adversary
  chain. An explicit `ADVERSARY:` clause at PHASE 2 execution body entry names
  inertia as what the phase defeats. C-16 presence does not imply C-42 presence:
  the output-template adversary fires post-execution; the execution-body adversary
  fires at phase entry, before the guard and assertion loop execute.

**Orthogonality confirmed:** V-02 (C-42 without C-41) and V-03 (C-41 without C-42)
score identically under v12. Under v13: V-01/V-04/V-05 -> 265; V-02/V-03 -> 260
(symmetric 5-point delta).

**Form-agnosticism confirmed:** V-04 (lifecycle GUARD contract with prose-appended
PHASE 3 OUTPUT DECLARATION and PHASE 2 ADVERSARY: line) and V-05 (elevated titled
blocks for both structures) score identically to V-01 (execution-prose form).
Consistent with form-agnosticism confirmed for C-37/C-38 in R11 and C-39/C-40 in R12.

**Max score: 255 -> 265.** Passing threshold unchanged.

**Implications added in v13:**
- C-41 => C-40, C-39
- C-42 => C-16

---

## Summary of v12 changes (C-39, C-40)

Two criteria extracted from R12 excellence signals. All five R12 variants scored
245/245 under v11. The V-01 vs V-02 delta isolated C-39; the V-01 vs V-03 delta
isolated C-40.

| ID | Name | Source | Points |
|----|------|--------|--------|
| C-39 | OUTPUT DECLARATION trigger characterization | R12 V-01/V-03/V-04/V-05 vs V-02 | 5 |
| C-40 | OUTPUT DECLARATION sub-component labeling | R12 V-01/V-02/V-04/V-05 vs V-03 | 5 |

**Structural Tier 11 (10 pts).** Max score: 245 -> 255.

- **C-39** extends the trigger-characterization site chain from two sites (preamble
  C-35, GUARD C-37) to three by adding per-axis trigger sentences within the PHASE 2
  OUTPUT DECLARATION's `INVARIANT:` sub-component. Trigger characterization at
  preamble and GUARD does not propagate to the OUTPUT DECLARATION automatically.

- **C-40** adds explicitly named sub-components (`INVARIANT:` and `OUTPUT FORM:`)
  within the PHASE 2 OUTPUT DECLARATION block, making each sub-declaration
  independently addressable. An OUTPUT DECLARATION with undifferentiated prose
  satisfies C-38 but not C-40.

**Implications added in v12:**
- C-39 => C-38, C-37
- C-40 => C-38

---

## R12 structural note

C-39 and C-40 are structurally orthogonal. C-39 extends C-37 in site -- the
trigger-characterization property established at the GUARD site (C-37) is
additionally present at the OUTPUT DECLARATION site, completing a three-site
chain: preamble (C-35), GUARD (C-37), OUTPUT DECLARATION (C-39). C-40 extends
C-38 in structure -- the OUTPUT DECLARATION block mandated by C-38 is further
required to have explicitly named sub-components, making the invariant declaration
and the output form specification independently addressable. A skill can satisfy
C-39 without C-40 (OUTPUT DECLARATION with trigger sentences but undifferentiated
prose -- V-03). A skill can satisfy C-40 without C-39 (OUTPUT DECLARATION with
labeled sub-components but no trigger characterization within the INVARIANT
sub-component -- V-02). No R12 variant achieves 255 -- the gap that defines Round 13.

C-39 requires C-38 (the OUTPUT DECLARATION must exist before its INVARIANT
sub-component can carry trigger sentences) and C-37 (trigger characterization
at the GUARD site must be established; C-39 extends the pattern to a third site).
C-40 requires only C-38 (the OUTPUT DECLARATION must exist before its sub-components
can be labeled). The implication asymmetry is intentional: C-39 extends a
two-site chain (requiring both prior sites to be established); C-40 only requires
the OUTPUT DECLARATION site that C-38 mandates.

---

## R13 structural note

C-41 and C-42 are structurally orthogonal. C-41 concerns PHASE 3 output structure
(extending the OUTPUT DECLARATION residency and labeled-sub-component patterns
from PHASE 2 to PHASE 3). C-42 concerns PHASE 2 execution framing (extending
adversary framing from the output template into the execution phase body). A
variant can carry PHASE 3 OUTPUT DECLARATION without execution-body adversary
framing at PHASE 2 entry (C-41 PASS, C-42 FAIL -- V-03). A variant can carry
execution-body adversary framing without PHASE 3 OUTPUT DECLARATION (C-41 FAIL,
C-42 PASS -- V-02).

C-41 requires C-40 (labeled sub-components at PHASE 2 OUTPUT DECLARATION must be
established; C-41 extends the labeled-sub-component and trigger-sentence patterns
to a second execution phase) and C-39 (the trigger-sentence-within-INVARIANT
pattern established at PHASE 2 by C-39 is the pattern C-41 extends to PHASE 3 --
PHASE 3 INVARIANT: sub-component carries its own Trigger: sentence). C-42 requires
only C-16 (adversary framing at the output template site must be established;
C-42 extends adversary framing to the execution phase body site, creating a
two-site chain anchored by C-16).

V-01 demonstrates that both C-41 and C-42 are satisfiable in minimum execution-
prose form, establishing the baseline from which the V-04 and V-05 form-agnosticism
variants confirm that lifecycle-contract and elevated-titled-block forms are equally
sufficient. Neither C-41 nor C-42 is a pass-condition clarification of any prior
criterion -- each requires evidence from a round where the structural gap was
observable.

---

## R14 structural note

C-43 and C-44 are structurally orthogonal. C-43 concerns PHASE 3 execution framing
(extending the adversary declaration pattern from PHASE 2 entry into PHASE 3 entry,
completing a two-phase adversary chain). C-44 concerns preamble architecture
(extending the preamble invariant declaration pattern to output declarations,
asserting multi-phase output declaration residency as a structural chain). A variant
can carry a PHASE 3 adversary declaration without a preamble output declaration chain
(C-43 PASS, C-44 FAIL -- V-03). A variant can carry a preamble output declaration
chain without a PHASE 3 adversary declaration (C-43 FAIL, C-44 PASS -- V-02).

C-43 requires C-42 (adversary framing must be established at the PHASE 2 execution
body site; C-43 extends that pattern to the PHASE 3 execution body, creating a
two-phase adversary chain -- PHASE 2 adversary anchor established by C-42, PHASE 3
adversary extension established by C-43). C-44 requires C-41 (both PHASE 2 and PHASE 3
output declarations must exist before a preamble can enumerate them as a chain; C-41
establishes the PHASE 3 OUTPUT DECLARATION; C-38 establishes the PHASE 2 OUTPUT
DECLARATION; the chain requires both links to be present before the preamble can
declare the chain as a structural invariant).

The structural parallel is exact: C-43 extends C-42 in the adversary-chain dimension
(PHASE 2 -> PHASE 3) exactly as C-42 extended C-16 in the adversary-chain dimension
(output-template -> PHASE 2 execution body). C-44 extends C-33/C-34 in the preamble
declaration dimension -- the pattern of declaring a structural invariant in the preamble
before implementing it, established for dual-axis exits by C-33/C-34, is applied to
multi-phase output declaration residency. Neither C-43 nor C-44 is a pass-condition
clarification of any prior criterion.

V-01 demonstrates that both C-43 and C-44 are satisfiable in minimum execution-
prose form. V-04 and V-05 confirm form-agnosticism.

---

## R15 structural note

C-45 and C-46 are structurally orthogonal. C-45 concerns preamble architecture
(extending the preamble invariant declaration pattern from output declaration residency
to adversary chain residency, completing the preamble's third architectural invariant
block). C-46 concerns adversary block structure (extending the adversary block at each
phase-entry declaration site from two-part to three-part form by adding a labeled
DEFEAT CONDITION: sub-component). A variant can carry a preamble adversary chain
declaration without defeat-condition sub-components at the adversary declaration sites
(C-45 PASS, C-46 FAIL -- V-03). A variant can carry defeat-condition sub-components
at adversary declaration sites without a preamble adversary chain declaration
(C-45 FAIL, C-46 PASS -- V-02).

C-45 requires C-43 (both PHASE 2 and PHASE 3 adversary declarations must exist before
the preamble can enumerate them as a chain; C-43 establishes the PHASE 3 adversary
declaration; C-42 establishes the PHASE 2 adversary declaration; the chain requires
both links to be present before the preamble can declare the chain as a structural
invariant). C-46 also requires C-43 (the PHASE 3 adversary declaration site must exist
for its adversary block to carry a DEFEAT CONDITION: sub-component; C-42 establishes
the PHASE 2 adversary site; C-43 establishes the PHASE 3 adversary site; both sites
must be present before C-46's three-part block form can be required at each site).

The structural parallels are exact on two axes:
- C-45 parallels C-44 in the preamble dimension: C-44 declared output declaration
  residency as a preamble chain; C-45 declares adversary chain residency as a preamble
  chain using the same architectural invariant pattern. Together C-44 and C-45 complete
  the preamble's architectural declaration inventory: exits (C-34), output declarations
  (C-44), adversary declarations (C-45).
- C-46 parallels C-40 in the block sub-component dimension: C-40 extended the OUTPUT
  DECLARATION block from undifferentiated prose to labeled sub-components (INVARIANT:,
  OUTPUT FORM:); C-46 extends each adversary block from two-part form to three-part
  form by adding a DEFEAT CONDITION: labeled sub-component. The sub-component makes
  the defeat observable independently of the adversary name and trigger clause.

Neither C-45 nor C-46 is a pass-condition clarification of any prior criterion --
each requires evidence from a round where the structural gap was observable.

V-01 demonstrates that both C-45 and C-46 are satisfiable in minimum execution-prose
form. V-04 and V-05 confirm form-agnosticism.

---

## R16 structural note

C-47 and C-48 are structurally orthogonal. C-47 concerns preamble block entry
labeling (extending the ADVERSARY CHAIN block from named-in-prose to labeled
sub-entries per phase, making each adversary independently addressable by phase
label). C-48 concerns PHASE 1 execution framing (extending the execution-body
adversary chain from two phases -- PHASE 2 and PHASE 3 -- to three phases by
adding adversary framing at PHASE 1, the signal acquisition phase). A variant
can carry labeled ADVERSARY CHAIN sub-entries without a PHASE 1 adversary body
(C-47 PASS, C-48 FAIL -- V-03, with contamination). A variant can carry a PHASE 1
adversary body without labeled ADVERSARY CHAIN sub-entries in the preamble
(C-47 FAIL, C-48 PASS -- V-02).

C-47 requires C-45 (the ADVERSARY CHAIN block must exist in the preamble before
its entries can be labeled; C-45 establishes the ADVERSARY CHAIN block; C-47
extends that block from prose enumeration to labeled sub-entry form). C-48 requires
C-46 (the three-part adversary block form -- ADVERSARY: + DEFEAT CONDITION: --
must be established at PHASE 2 and PHASE 3 before it can be required at PHASE 1;
C-46 establishes three-part form at both existing adversary sites; C-48 extends
three-part form to the PHASE 1 adversary site). The two new criteria have different
prerequisites from tier 14 -- restoring the prerequisite asymmetry pattern of
tiers 11--13 after tier 14's symmetric prerequisite (both C-45 and C-46 required
only C-43).

The structural parallels operate on two independent axes:
- C-47 parallels C-40 in the labeled-sub-component dimension: C-40 extended the
  OUTPUT DECLARATION block from undifferentiated prose to labeled sub-components
  (INVARIANT:, OUTPUT FORM:); C-47 extends the ADVERSARY CHAIN preamble block from
  running-prose adversary enumeration to labeled PN-ADVERSARY: sub-entries, making
  each phase adversary independently addressable without prose scanning. C-47 is
  the preamble-block parallel of C-40 applied to the adversary chain inventory.
- C-48 parallels C-43 in the execution-phase-extension dimension: C-43 extended
  the execution-body adversary chain from PHASE 2 to PHASE 3 (forward extension);
  C-48 extends the adversary chain to PHASE 1 (backward extension to the earliest
  execution phase), completing a three-phase execution-body adversary chain spanning
  all principal execution phases. Unlike C-43 which required only a two-part
  adversary block form (adversary name + trigger clause per C-42), C-48 requires
  the full three-part form established by C-46 (adversary + defeat condition) at
  the new PHASE 1 site -- the PHASE 1 adversary block must be three-part from the
  outset, not retrofitted.

**Contamination note (V-03):** The V-01 vs V-03 delta is not a clean C-48
isolation. V-03 withheld C-48 as intended but also introduced a readiness-first
template reordering axis that violates C-12 (gap-first output ordering) and C-20
(assertion table as primary gap artifact) -- two criteria unrelated to C-48. The
actual V-03 delta under v16 is -15 pts (C-48 -5, C-12 -5, C-20 -5), not -5.
C-48 independent necessity is confirmed by V-02 and V-04 PASS evidence and by
V-03's explicit ADVERSARY:/DEFEAT CONDITION: absence at PHASE 1. Clean C-48
isolation requires a redesigned V-03 with a second axis that preserves C-12/C-20
compliance (e.g., template column reordering within the gap register, not
sectional reordering of gap register vs. aggregate).

Neither C-47 nor C-48 is a pass-condition clarification of any prior criterion.

V-01 demonstrates that both C-47 and C-48 are satisfiable in minimum execution-
prose form. V-04 confirms form-agnosticism (lifecycle GUARD contract).

---

## R18 structural note

C-49 differs from all prior structural tier criteria in one critical property:
it has a conditional prerequisite rather than a hard prerequisite. All criteria
in tiers 2--15 carry hard implications (failing C-N cascades to failing any C-M
where C-M => C-N). C-49 does not: when C-48 fails, C-49 is vacuously satisfied
-- there is no PHASE 1 adversary to operationalize, so the STOP CONDITION's
compliance at the PHASE 1 position is not in question.

**The underlying structural logic:** The STOP CONDITION (DISPLAY GATE execution
gate) carries predicates that check whether each declared adversary was defeated
before output is rendered. When the adversary chain has N phases, the STOP
CONDITION requires N adversary-defeat predicates. With C-48 absent (two-phase
chain), the STOP CONDITION requires predicates for PHASE 2 and PHASE 3 only --
correct. With C-48 present (three-phase chain), a STOP CONDITION with only two
adversary-defeat predicates is incomplete: PHASE 1's declared adversary has no
corresponding gate check. C-49 enforces this synchronization: predicate count
must match adversary chain length.

**Vacuous PASS behavior explained:** V-03 and V-05 carry the 4th STOP predicate
structurally (the predicate text is present) but vacuously (it checks a PHASE 1
defeat condition when no PHASE 1 adversary has been declared). The predicate is
present but references an absent adversary -- the criterion is satisfied because
the structural commitment (predicate count = adversary chain length) is not
violated from the STOP CONDITION side. The violation in V-04 is the inverse:
C-48 declares a PHASE 1 adversary, the adversary commits a DEFEAT CONDITION, but
the STOP CONDITION carries no corresponding predicate -- the adversary chain and
the STOP CONDITION are out of sync.

**Isolation geometry:** V-01 vs V-04 is a clean single-axis 5-point delta. No
contamination is observed: V-04's ablation (removing the 4th STOP predicate while
retaining all three adversary blocks including C-48's PHASE 1 block) is surgical.
V-03 (redesigned from R16) provides clean C-48 isolation at 290 under v16 -- the
redesign successfully eliminates the C-12/C-20 contamination from R16.

**Implication map:** No new hard implication. C-49's conditional prerequisite
(requires C-48 for non-vacuous evaluation) does not appear in the hard implication
chain. The conditional relationship is documented here and in the C-49 criterion
definition.

---

## Score Distribution

| Section | Criteria | Points |
|---------|----------|--------|
| Essential | C-01--C-04 | 60 (15 each) |
| Recommended | C-05--C-07 | 30 (10 each) |
| Aspirational | C-08--C-12 | 25 (5 each) |
| Structural Tier 2 | C-13--C-16 | 20 (5 each) |
| Structural Tier 3 | C-17--C-19 | 15 (5 each) |
| Structural Tier 4 | C-20--C-22 | 15 (5 each) |
| Structural Tier 5 | C-23--C-25 | 15 (5 each) |
| Structural Tier 6 | C-26--C-28 | 15 (5 each) |
| Structural Tier 7 | C-29--C-31 | 15 (5 each) |
| Structural Tier 8 | C-32--C-34 | 15 (5 each) |
| Structural Tier 9 | C-35--C-36 | 10 (5 each) |
| Structural Tier 10 | C-37--C-38 | 10 (5 each) |
| Structural Tier 11 | C-39--C-40 | 10 (5 each) |
| Structural Tier 12 | C-41--C-42 | 10 (5 each) |
| Structural Tier 13 | C-43--C-44 | 10 (5 each) |
| Structural Tier 14 | C-45--C-46 | 10 (5 each) |
| Structural Tier 15 | C-47--C-48 | 10 (5 each) |
| **Structural Tier 16** | **C-49** | **5** |
| **Total** | **C-01--C-49** | **300** |

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Signal discovery** -- The skill scans the `simulations/` directory for existing signal files matching the topic, using a Glob pattern. The scan is explicit and disk-based, not inferred from memory. | 15 | coverage | A Glob or equivalent disk-scan instruction is present. Results are assigned to a named variable (e.g. `DISK_SIGNALS`). Zero-result case is handled: output states "no signals found" rather than silently computing 0%. |
| C-02 | **Coverage percentage** -- Output reports a numeric coverage percentage derived from signals found on disk versus signals planned in `strategy.md`. The percentage is mathematically consistent with the gap list. | 15 | coverage | A percentage formula is present (`found / planned * 100` or equivalent). A consistency check guards against the contradiction failure mode: if the gap list is non-empty and percentage equals 100%, execution halts and recomputes. |
| C-03 | **Gap identification** -- Signals planned in `strategy.md` but not yet present on disk are listed as open gaps. | 15 | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** -- The skill writes nothing to disk. No file is created or modified. | 15 | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** -- Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY -- 3 essential gaps remain", "READY -- all scout + draft signals present"). | 10 | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number -- a qualitative judgment. |
| C-06 | **Namespace breakdown** -- Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | 10 | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** -- Output names the `strategy.md` file used as the planned-signal baseline and notes if `strategy.md` is missing or has no planned signals for this topic. | 10 | correctness | `strategy.md` reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** -- Output identifies the most recently modified signal file and flags any signals not modified within the last N days as potentially stale. | 5 | depth | A STALE EVIDENCE section or equivalent is present. Signal file dates are surfaced, not just counts. |
| C-09 | **Actionable next step** -- Output names the single highest-priority gap and the specific skill invocation that would close it. | 5 | depth | A HIGHEST PRIORITY RISK section or equivalent is present. It contains a concrete skill invocation (e.g. `/scout:feasibility {topic}`), not a generic recommendation. |
| C-10 | **Structural namespace completeness** -- The namespace breakdown table contains a row for all nine namespaces. Namespaces with zero planned or zero found signals are shown with explicit zeros, not omitted. | 5 | format | All nine namespaces present in the table. Zero rows display `0 \| 0 \| --` rather than being suppressed. |
| C-11 | **Phase-gated execution** -- The skill defines named execution phases and includes a DISPLAY GATE phase that performs a pre-display check before producing output. | 5 | structure | Named phases are declared in the skill. A DISPLAY GATE phase or equivalent explicitly gates display on a pre-condition check. |
| C-12 | **Gap-first output ordering** -- The output template places the risk register (gap list) before the aggregate summary. Gaps are seen before the rolled-up percentage. | 5 | format | The COMMIT RISK REGISTER or equivalent gap artifact appears before the EXPOSURE SUMMARY or equivalent aggregate. The template ordering is fixed, not conditional. |

---

## Structural Tier 2 (20 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-13 | **Triple-redundancy ordering guard** -- The skill contains three structurally distinct redundancy layers at mechanism locations, and declares their ordering as an invariant (structural -> semantic -> execution). | 5 | structure | Three distinct layer types are present at mechanism locations. An ordering invariant is declared, not merely implied by position. |
| C-14 | **Template-first structural absorption** -- The output template (with all sections and column headers) appears before the execution section in the skill body. Execution fills slots defined by the template; the template is not assembled during execution. | 5 | structure | The output template section precedes the execution section in skill order. Column and section headers are declared in the template, not emitted ad-hoc during execution. |
| C-15 | **Per-signal assertion chain** -- Each signal listed as PLANNED in the coverage baseline receives exactly one VERIFIED or UNVERIFIED assertion. No planned signal is silently omitted; no assertion is made for unplanned signals. | 5 | correctness | A one-to-one mapping between PLANNED signals and assertion results is enforced. The assertion mechanism processes each signal individually, not in batches. |
| C-16 | **Consequence-framed readiness verdict** -- The readiness verdict is stated as a shipping consequence, not a coverage label. "Committing now means shipping without: {list}" rather than "Coverage: 60%." | 5 | depth | A consequence-framed verdict is present. The verdict names specific missing items in the context of a commit or ship action, not just a percentage. |

---

## Structural Tier 3 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-17 | **Labeled redundancy layers** -- Each of the three redundancy layers (structural, semantic, execution) carries an explicit label at the location in the skill where it operates: `[LAYER 1 -- STRUCTURAL]`, `[LAYER 2 -- SEMANTIC]`, `[LAYER 3 -- EXECUTION]`. | 5 | structure | All three layer labels are present at their mechanism locations in the skill body. Labels are not in comments or headers only -- they appear at the point of the mechanism. |
| C-18 | **Assertion table pre-seeded in template** -- The COMMIT RISK REGISTER (or equivalent assertion table) with VERIFIED and UNVERIFIED column headers is defined in the output template section, not constructed during execution. The table structure is part of the pre-execution template. | 5 | structure | The assertion table with column headers appears in the output template section. The execution section fills rows into a pre-existing table structure. |
| C-19 | **Consequence vocabulary saturation** -- All output section headers use consequence vocabulary (COMMIT RISK REGISTER, COMMIT RISKS, EXPOSURE SUMMARY, COMMIT DECISION, HIGHEST PRIORITY RISK). No section header uses neutral or descriptive vocabulary (Coverage Summary, Gap List, Status). | 5 | vocabulary | Every top-level output section header uses a word from the consequence domain (COMMIT, EXPOSURE, RISK). Neutral section titles are absent. |

---

## Structural Tier 4 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-20 | **Assertion table as primary gap display artifact** -- The COMMIT RISK REGISTER is labeled as the primary gap artifact and is structurally designated as the first output section, preceding the EXPOSURE SUMMARY. Its label explicitly states its role: `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]`. | 5 | structure | The COMMIT RISK REGISTER label contains both `primary gap artifact` and `precedes EXPOSURE SUMMARY` (or equivalent). It is the first output section. |
| C-21 | **Execution phase names in consequence vocabulary** -- All execution phases are named using consequence vocabulary drawn from the commit/exposure domain. Canonical example: SIGNAL ACQUISITION, COMMITMENT ASSERTION, EXPOSURE COMPUTATION, DISPLAY GATE. No phase is named with neutral or ordinal vocabulary (Phase 1, Step 2, Data Collection). | 5 | vocabulary | All execution phase names use consequence-domain vocabulary. Ordinal or neutral phase names are absent. |
| C-22 | **Missing baseline as epistemic consequence** -- When `strategy.md` is absent or contains no planned signals for the topic, the output does not silently compute against zero. It explicitly states that the epistemic consequence of the missing baseline is that commit exposure cannot be quantified: "No planned baseline -- commit exposure is unquantifiable." | 5 | correctness | The missing-baseline branch produces an explicit epistemic-consequence statement, not a zero-coverage result or a silent skip. |

---

## Structural Tier 5 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-23 | **Phase name as compressed criterion statement** -- The assertion phase name encodes both the evaluation granularity (per-signal, not batch) and the decision stake (commitment), compressing the C-15 per-signal requirement into the execution architecture label. The phase name is a structural specification, not a description. Canonical example: `PER-SIGNAL COMMITMENT ASSERTION`. Extends C-21. | 5 | vocabulary | The assertion phase name contains both an evaluation-granularity term and a decision-stake term. The terms are in the phase name itself, not in a parenthetical annotation. C-21 pass required. |
| C-24 | **Cross-layer vocabulary coherence** -- Structural enforcement labels use the same vocabulary as the active phase names they govern. When C-21 is satisfied, `[LAYER 3]` reads `DISPLAY GATE render order:` not `Phase 4 render order:`. Consequence-phase vocabulary flows into structural enforcement mechanism labels, collapsing two parallel vocabulary systems into one. Extends C-17 and C-21. | 5 | vocabulary | Each `[LAYER N]` label at an enforcement location uses vocabulary from the phase name it governs, not ordinal or neutral vocabulary. C-17 and C-21 pass required. |
| C-25 | **Template field inline consequence annotation** -- Template fields contain their epistemic consequence inline within the field format string itself, making each field self-documenting about decision impact. Canonical example: `[FOUND \| NOT FOUND -- if absent: commit exposure is unquantifiable]`. The annotation is structurally inseparable from the field. Extends C-22 from section-level to field-level consequence. | 5 | vocabulary | At least one template field contains an inline `if absent:` consequence clause. The clause is in the field format string, not in a separate note. The consequence uses commit-domain vocabulary. |

---

## Structural Tier 6 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-26 | **Granularity-prefix left-edge declaration** -- In a C-23-compliant phase name, the evaluation-granularity term occupies the leftmost position, establishing quantifier scope before the decision-stake noun phrase. `PER-SIGNAL COMMITMENT ASSERTION` satisfies (granularity prefix precedes stake); a hypothetical `COMMITMENT PER-SIGNAL ASSERTION` would contain both required terms (passing C-23) but fail this criterion (stake precedes scope). Left-edge position makes scope the first token in name-scanning order, not a later modifier or infix qualifier. Extends C-23. | 5 | vocabulary | The granularity term is the leftmost token in the assertion phase name. Stake noun phrase follows granularity prefix. C-23 pass required. |
| C-27 | **Full compressed phase name in C-24 layer labels** -- When C-23 and C-24 are jointly satisfied, the layer label governing the assertion phase carries the *complete* C-23 phase name -- granularity prefix included -- not merely the stake noun phrase. `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` satisfies; `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` satisfies C-24 but not this criterion (granularity prefix absent from label). The full compressed form propagates from the phase header into the layer enforcement label, collapsing phase-name and label vocabulary into a single token. Requires C-23 and C-24. Extends C-23 and C-24. | 5 | vocabulary | The layer label for the assertion phase contains the full C-23 phase name including granularity prefix. Presence of stake noun phrase alone is insufficient. C-23 and C-24 pass required. |
| C-28 | **Field annotation phase-attribution** -- A C-25-compliant field annotation identifies by name the specific execution phase (from C-21) whose function is impaired when the field is absent. The consequence is phase-attributed, not epistemic-generic. `[FOUND \| NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]` satisfies; `[FOUND \| NOT FOUND -- if absent: commit exposure is unquantifiable]` satisfies C-25 but not this criterion (consequence is valid but names no phase). Requires C-25 and C-21. Extends C-25 from generic epistemic annotation to phase-attributed consequence annotation. | 5 | vocabulary | At least one C-25-compliant field annotation names a C-21 execution phase as the impaired party. Generic `commit exposure` or coverage language without phase attribution is insufficient. C-25 and C-21 pass required. |

---

## Structural Tier 7 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-29 | **Multi-site phase-attributed annotation** -- A C-28-compliant skill satisfies phase attribution at the minimum required site (strategy.md field, `cannot execute`). This criterion requires phase-attributed consequence annotations at *every* consequence annotation site -- including the stale evidence section. The stale-evidence annotation carries `if stale: {PHASE-NAME} may rest on expired evidence`, naming the C-21 execution phase whose inputs are weakened by stale data. Consequence verb shifts from `cannot execute` (C-28, absent field -- hard failure) to `may rest on expired evidence` (C-29, stale field -- degraded execution). The verb downgrade is intentional and required: stale evidence does not prevent phase execution, it degrades it. Canonical: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence`. Requires C-28 and C-05. Extends C-28 from minimum-one-site to all-consequence-sites. | 5 | vocabulary | The stale evidence section carries a phase-attributed consequence annotation naming a C-21 execution phase. Generic staleness descriptions without phase attribution are insufficient. Consequence verb must reflect degraded-not-blocked semantics (`may rest on expired evidence`, not `cannot execute`). C-28 and C-05 pass required. |
| C-30 | **Absent-topic early exit** -- PHASE 2 implements two distinct stop conditions on the strategy.md read: (1) strategy.md file absent -- C-12 satisfied; (2) strategy.md present but topic not registered -- this criterion. For case 2, output states `"topic not registered: no planned signals for {topic}"` (or equivalent topic-specific message) and execution stops before PHASE 3 (EXPOSURE COMPUTATION). Distinguishes file-level absence (C-12) from topic-level absence within a present file. Prevents false 0% coverage computation against an empty baseline for an unregistered topic. Extends C-12 from single-axis exit (file absent) to dual-axis exit (file absent OR topic absent within file). | 5 | correctness | PHASE 2 contains a topic-presence check distinct from the file-presence check. A topic-absent branch produces a topic-specific stop message before EXPOSURE COMPUTATION executes. The stop message names the topic. C-12 pass required. |
| C-31 | **Per-register-row commit-consequence annotation** -- Each row of the COMMIT RISK REGISTER carries an inline commit-framed consequence annotation stating the shipping impact of the signal's absence. Canonical form: `VERIFIED \| UNVERIFIED -- if absent: ships without this signal on commit`. Extends C-25's field-level annotation (applied once at the strategy.md template field) down into every row of the assertion table -- one annotation per planned signal, not one annotation for the whole template. The consequence vocabulary is commit-framed (`ships without...on commit`), not phase-execution-framed (`cannot execute`), distinguishing register-row consequence (what ships) from field-level consequence (what fails to run). Requires C-09 and C-25. Extends C-25 and C-09. | 5 | vocabulary | Every planned-signal row in the COMMIT RISK REGISTER contains an inline `if absent: ships without...on commit` consequence clause. Rows without consequence annotation fail this criterion. C-09 and C-25 pass required. |

---

## Structural Tier 8 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-32 | **Named-exit labeling** -- When a dual-axis stop condition (C-30) is implemented, each exit branch carries a distinct named identifier at the branch declaration site. Named labels (`Exit A -- file absent:`, `Exit B -- topic not registered:`) make each branch independently addressable by name. A scorer can identify and verify each branch by its label without parsing conditional logic. The names may be ordinal-alpha (`Exit A`, `Exit B`) or semantic (`FILE-ABSENT EXIT`, `TOPIC-ABSENT EXIT`). Unnamed sequential branches (numbered list items `1.`/`2.` or unlabeled `if/then` blocks) do not satisfy this criterion regardless of structural correctness. The label form is agnostic: inline execution prose and GUARD contract fields both satisfy, provided the branch-level name appears at the declaration site. Requires C-30. Extends C-30 from implemented-dual-exit to labeled-dual-exit. | 5 | structure | Each exit branch in the dual-axis stop condition has a distinct declared name at the branch declaration site. Numbered list items or conditional clauses without branch-level names are insufficient. Form (prose vs. GUARD field) is not evaluated. C-30 pass required. |
| C-33 | **Preamble architectural invariant declaration** -- A preamble block appearing *before* the guard mechanism that implements C-30 explicitly declares the architectural invariant the mechanism satisfies. The preamble names the structural property being enforced (e.g., "PHASE 2 dual-axis exit") as a declared constraint. The preamble is physically separate from the guard block or conditional; it precedes and frames the implementation. A comment embedded within the guard block is not a preamble. A preamble that cites only a criterion number without naming the structural property does not satisfy this criterion; the structural property must be named (by description or by implication from an axis enumeration). Requires C-30. Extends C-30 from implementation-only to declared-then-implemented. | 5 | structure | A preamble block preceding the dual-axis guard mechanism is present. The preamble names the structural invariant being enforced. The preamble is physically separate from (and precedes) the guard block. C-30 pass required. |
| C-34 | **Axis-enumerated invariant declaration** -- A C-33-compliant preamble explicitly enumerates all axes of the dual-axis exit condition by name, characterizes the trigger condition for each axis, and asserts that the axes are structurally distinct conditions producing distinct output messages. The enumeration must be axis-complete: (1) file-axis trigger named, (2) topic-axis trigger named, (3) structural distinctness of the two conditions asserted, (4) distinct output messages asserted. Canonical sufficient form: `"PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions with distinct messages"`. A generic declaration ("PHASE 2 has two stop conditions") satisfies C-33 but not C-34 (axes not named). A criterion-citation preamble ("implements C-30 as architectural invariant") satisfies C-33 but not C-34 (no axis enumeration). A single canonical line is minimum-sufficient; elaboration is additive but not required. Requires C-33. Extends C-33 from declaration-present to axis-complete declaration. | 5 | structure | The C-33-compliant preamble names both axes (file-absent, topic-absent), characterizes each trigger condition, and asserts structural distinctness with distinct messages. Generic or criterion-citing preambles without axis enumeration are insufficient. Single-line canonical form is sufficient; additional sentences are not required. C-33 pass required. |

---

## Structural Tier 9 (10 pts total) -- new in v10

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-35 | **Per-axis trigger sentence characterization** -- A C-34-compliant preamble names both axes in canonical form. C-35 requires the preamble to additionally provide a dedicated trigger sentence for each axis that explicitly characterizes the condition activating that axis. Naming an axis (`file-absent`) and characterizing its trigger (`file-absent triggers when strategy.md does not exist on disk`) are structurally distinct declarations. The canonical sentence satisfies C-34 by naming axes; trigger sentences go further by specifying what causes each axis to fire. Canonical per-axis form: `"file-absent triggers when strategy.md does not exist on disk; topic-absent triggers when strategy.md is present but contains no planned-signal entry for the named topic"`. Trigger sentences appear within or immediately after the preamble block; they may be a continuation of the preamble or a parenthetical expansion. A single canonical axis-named line without per-axis trigger expansion satisfies C-34 but not C-35. Requires C-34. Extends C-34 from axis-named to axis-trigger-characterized. | 5 | structure | The C-34-compliant preamble contains at least one dedicated trigger sentence per axis (file-absent trigger condition stated, topic-absent trigger condition stated). Axis names alone in the canonical declaration are insufficient. C-34 pass required. |
| C-36 | **Multi-site invariant declaration chain** -- The dual-axis invariant is independently echoed at every structurally distinct site in the skill body: (1) the preamble (C-33/C-34 compliance), (2) the GUARD entry names (C-32 compliance), and (3) at least one additional structural site -- OUTPUT block, commit-framing section, or equivalent. Each site declares the invariant in a form that is independently verifiable without reference to other sites. A scorer reading only site (3) must be able to determine that the dual-axis property is enforced without consulting the preamble or the GUARD entries. A skill satisfying C-32 and C-34 but lacking an OUTPUT block echo fails this criterion (two sites satisfied, third absent). The minimum chain length is three sites; additional sites are compatible and additive. Requires C-32 and C-34. Extends C-32 and C-34 from single-declaration-site to multi-site declaration chain. | 5 | structure | The dual-axis invariant is declared at the preamble site (C-33/C-34), the GUARD-entry site (C-32), and at least one additional structural site (OUTPUT block, commit-framing, or equivalent). Each site independently declares the invariant. C-32 and C-34 pass required. |

---

## Structural Tier 10 (10 pts total) -- new in v11

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-37 | **GUARD-site trigger characterization** -- When C-32 (named exits at GUARD) and C-35 (per-axis trigger sentences in preamble) are jointly satisfied, this criterion additionally requires that each named GUARD exit carries an inline trigger characterization at the GUARD declaration site. The GUARD block is extended from exit-named (C-32) to trigger-characterized: each exit entry declares both its name and the condition activating it. Canonical GUARD-site form: `Exit A -- file absent: fires when strategy.md does not exist on disk`. A skill where per-axis trigger sentences appear only in the preamble (satisfying C-35) and named exits appear only at the GUARD site (satisfying C-32) satisfies both at separate structural locations but not C-37 (no co-location at GUARD). The GUARD site becomes the authoritative exit manifest: name and trigger co-resident at the same structural declaration. Requires C-32 and C-35. Extends the conjunction of C-32 and C-35 from co-presence at separate structural locations to co-location at the GUARD declaration site. | 5 | structure | Each named GUARD exit in the C-32-compliant structure carries an inline trigger clause characterizing the condition activating that exit. Preamble trigger sentences alone with named but un-triggered GUARD entries are insufficient. C-32 and C-35 pass required. |
| C-38 | **Phase-output invariant declaration** -- When C-36 (multi-site invariant chain, minimum three sites) is satisfied, this criterion requires that the third site is an explicitly declared OUTPUT DECLARATION block embedded within the execution phase body -- not a commit-framing section (COMMIT DECISION) or a lifecycle phase definition field. The OUTPUT DECLARATION is structurally resident in the active execution phase (e.g. within PHASE 2's execution body), co-located with the logic the invariant constrains. A COMMIT DECISION block echo satisfies C-36 (valid commit-framing section) but not C-38 (post-execution structural section, outside any execution phase body). A lifecycle PHASE 2 OUTPUT field in a phase definition header satisfies C-36 (valid OUTPUT block) but not C-38 (phase definition, not execution body). An explicit PHASE 2 OUTPUT DECLARATION block embedded within the PHASE 2 execution section satisfies both C-36 and C-38. The distinction: commit-framing sections occur after all phases complete; lifecycle phase definition fields are structural headers; PHASE OUTPUT DECLARATIONS are execution-body components active during phase execution. Requires C-36. Extends C-36 from third-site-present to third-site-execution-phase-resident. | 5 | structure | The third C-36 site is an explicitly declared OUTPUT DECLARATION block embedded in the execution phase body. Commit-framing section echoes (COMMIT DECISION) and lifecycle phase definition fields fail this criterion regardless of structural correctness. C-36 pass required. |

**Implication map additions:** `C-37 => C-32`, `C-37 => C-35`, `C-38 => C-36`

**Projected R10 variant scores under v11:**

| Variant | C-35 | C-36 | C-37 | C-38 | Total |
|---------|------|------|------|------|-------|
| V-01 | PASS | PASS | FAIL | FAIL | 235 |
| V-02 | FAIL | PASS | FAIL | FAIL | 230 |
| V-03 | PASS | FAIL | FAIL | FAIL | 230 |
| V-04 | PASS | PASS | PASS | FAIL | 240 |
| V-05 | PASS | PASS | FAIL | PASS | 240 |

No R10 variant achieves 245. C-37 and C-38 are not jointly satisfied by any single variant -- the gap that defines Round 11.

---

## Structural Tier 11 (10 pts total) -- new in v12

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-39 | **OUTPUT DECLARATION trigger characterization** -- When C-38 (PHASE 2 execution-body OUTPUT DECLARATION) and C-37 (GUARD-site trigger characterization) are jointly satisfied, this criterion additionally requires that the PHASE 2 OUTPUT DECLARATION's `INVARIANT:` sub-component carries per-axis trigger sentences naming each exit's firing condition at the OUTPUT DECLARATION structural site. C-35 establishes per-axis trigger sentences at the preamble site; C-37 co-locates trigger characterization at the GUARD site; C-39 extends trigger characterization to the OUTPUT DECLARATION site, completing a three-site trigger-characterization chain (preamble, GUARD, OUTPUT DECLARATION). A skill where the OUTPUT DECLARATION's INVARIANT sub-component states the dual-axis property without per-axis trigger sentences satisfies C-38 and C-37 but fails C-39 -- naming the exits without characterizing when each fires at this third structural site. Canonical INVARIANT sub-component trigger form: `Trigger: file-absent fires when strategy.md does not exist on disk; topic-absent fires when strategy.md present but {topic} has no registered planned signals`. Requires C-38 and C-37. Extends the trigger-characterization site chain from two sites (preamble + GUARD) to three sites (preamble + GUARD + OUTPUT DECLARATION). | 5 | structure | The PHASE 2 OUTPUT DECLARATION INVARIANT sub-component contains at least one `Trigger:` sentence naming both exit conditions at the OUTPUT DECLARATION structural site. INVARIANT sub-component without trigger characterization fails. Presence of trigger sentences at preamble (C-35) and GUARD (C-37) is necessary but not sufficient. C-38 and C-37 pass required. |
| C-40 | **OUTPUT DECLARATION sub-component labeling** -- When C-38 (PHASE 2 execution-body OUTPUT DECLARATION) is satisfied, this criterion requires that the OUTPUT DECLARATION block contains explicitly named sub-components: `INVARIANT:` for the dual-axis gate invariant declaration and `OUTPUT FORM:` for the per-signal output specification. The labels make each sub-component independently addressable by name -- a scorer can locate and verify the invariant declaration by the INVARIANT: label and the output form specification by the OUTPUT FORM: label without parsing undifferentiated prose. An OUTPUT DECLARATION whose content is undifferentiated prose (dual-axis invariant and output form stated but not labeled) satisfies C-38 but not C-40. The label names `INVARIANT:` and `OUTPUT FORM:` are canonical; semantically equivalent labels at the same structural positions satisfy, provided both sub-components carry independent names. The label form is agnostic: inline prose labels and elevated titled box sub-declarations both satisfy, provided independent names are present at both sub-component positions within the OUTPUT DECLARATION block. Requires C-38. Extends C-38 from block-present to block-with-labeled-sub-components. | 5 | structure | The PHASE 2 OUTPUT DECLARATION block contains `INVARIANT:` and `OUTPUT FORM:` labels (or equivalent named sub-component labels) at independent sub-component positions within the block. An OUTPUT DECLARATION with no sub-component labels fails. C-38 pass required. |

**Implication map additions:** `C-39 => C-38`, `C-39 => C-37`, `C-40 => C-38`

**Projected R12 variant scores under v12:**

| Variant | C-37 | C-38 | C-39 | C-40 | Total |
|---------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | PASS | 255 |
| V-02 | PASS | PASS | FAIL | PASS | 250 |
| V-03 | PASS | PASS | PASS | FAIL | 250 |
| V-04 | PASS | PASS | PASS | PASS | 255 |
| V-05 | PASS | PASS | PASS | PASS | 255 |

No R12 variant achieves 255 with C-41 or C-42 -- those criteria do not yet exist. The gap that defines Round 13.

---

## Structural Tier 12 (10 pts total) -- new in v13

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-41 | **PHASE 3 output declaration with labeled sub-components** -- When C-40 (PHASE 2 OUTPUT DECLARATION with labeled sub-components) and C-39 (PHASE 2 OUTPUT DECLARATION trigger characterization) are jointly satisfied, this criterion additionally requires an independently declared OUTPUT DECLARATION block embedded within the PHASE 3 execution body, carrying `INVARIANT:` and `OUTPUT FORM:` labeled sub-components and a `Trigger:` sentence within the INVARIANT sub-component. The PHASE 2 OUTPUT DECLARATION (C-38/C-40) establishes the pattern: an execution-phase-resident OUTPUT DECLARATION that declares the phase's invariant with trigger characterization and names its output form with labeled sub-components. C-41 extends that pattern to PHASE 3 as a second independently necessary execution-phase mechanism. The PHASE 3 INVARIANT: sub-component names the consistency guard property and its trigger condition (`guard fires when UNVERIFIED count > 0 and computed percent = 100%`). The PHASE 3 OUTPUT FORM: sub-component names the percent and readiness verdict. The PHASE 2 OUTPUT DECLARATION satisfying C-38/C-39/C-40 does not imply a PHASE 3 OUTPUT DECLARATION: each execution phase requires its own independently declared output structure. A skill where PHASE 3 ends at the readiness threshold line with no OUTPUT DECLARATION block satisfies C-38/C-39/C-40 but fails C-41. Form-agnostic: the PHASE 3 OUTPUT DECLARATION may appear as inline prose, lifecycle-contract-appended prose, or an elevated titled block within the PHASE 3 execution section. Requires C-40 and C-39. Extends the output-declaration-residency and labeled-sub-component patterns from PHASE 2 to PHASE 3 as a second independently necessary execution-phase mechanism. | 5 | structure | The PHASE 3 execution body contains an OUTPUT DECLARATION block with `INVARIANT:` and `OUTPUT FORM:` labels and at least one `Trigger:` sentence within the INVARIANT sub-component naming the consistency guard firing condition. PHASE 3 execution prose ending at readiness thresholds without an OUTPUT DECLARATION block fails. C-40 and C-39 pass required. |
| C-42 | **Phase-entry adversary declaration** -- When C-16 (consequence-framed readiness verdict with adversary framing in the COMMIT DECISION output-template section) is satisfied, this criterion additionally requires an explicit adversary declaration within the PHASE 2 execution body at or near the phase's entry point, naming inertia (or the equivalent execution adversary) as what the phase defeats. C-16 establishes adversary framing at the output-template site (COMMIT DECISION block, rendered post-execution); C-42 establishes adversary framing at the execution-phase-body site (PHASE 2 body, encountered at phase entry before the guard and assertion loop execute), creating a two-site adversary chain. The two sites are structurally distinct: the output-template adversary is present in the rendered output regardless of whether PHASE 2 executes; the execution-body adversary is encountered when the execution engine enters PHASE 2. Presence of adversary framing in the COMMIT DECISION block (C-16) does not imply an adversary declaration at the PHASE 2 execution body site. Canonical PHASE 2 entry form: `ADVERSARY: inertia toward evidence-blind commits -- default when this phase is skipped: each unverified signal ships without explicit assertion.` Form-agnostic: the adversary clause may appear as an inline prose line, a titled contract block (e.g. `+-- PHASE 2 ADVERSARY DECLARATION --+`), or a lifecycle entry annotation, provided it is physically resident within the PHASE 2 execution section. Requires C-16. Extends adversary framing from output-template-only site (C-16, COMMIT DECISION) to a two-site adversary chain spanning output template and PHASE 2 execution body. | 5 | structure | An explicit adversary declaration (ADVERSARY: clause or named adversary statement) is present within the PHASE 2 execution body. Adversary framing present only in the COMMIT DECISION output-template section is insufficient. The adversary clause must name the execution-phase adversary (inertia toward evidence-blind commits, or equivalent). C-16 pass required. |

**Implication map additions:** `C-41 => C-40`, `C-41 => C-39`, `C-42 => C-16`

**Projected R13 variant scores under v13:**

| Variant | C-39 | C-40 | C-41 | C-42 | Total |
|---------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | PASS | 265 |
| V-02 | PASS | PASS | FAIL | PASS | 260 |
| V-03 | PASS | PASS | PASS | FAIL | 260 |
| V-04 | PASS | PASS | PASS | PASS | 265 |
| V-05 | PASS | PASS | PASS | PASS | 265 |

V-02 and V-03 score identically (260) -- symmetric 5-point delta confirming independent necessity and orthogonality of C-41 and C-42. No R13 variant fails both: the gap that defines Round 14.

---

## Structural Tier 13 (10 pts total) -- new in v14

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-43 | **PHASE 3 execution-body adversary declaration** -- When C-42 (adversary declaration in the PHASE 2 execution body) is satisfied, this criterion additionally requires an explicit adversary declaration within the PHASE 3 execution body at or near the phase's entry point, naming the adversary that PHASE 3 defeats (e.g., inertia toward coverage-blind verdicts -- default when this phase is skipped: percent is computed and reported without consistency verification). C-42 establishes adversary framing at the PHASE 2 execution body site (before the assertion loop); C-43 extends adversary framing to the PHASE 3 execution body site (before the consistency guard and threshold evaluation), completing a two-phase adversary chain spanning the two principal execution phases. The PHASE 2 adversary names what is bypassed when per-signal assertion is skipped (evidence-blind commits); the PHASE 3 adversary names what is bypassed when consistency verification is skipped (coverage-blind verdicts). The two adversary declarations are structurally distinct: they are residents of different execution phase bodies, guard against different failure modes, and require independent satisfaction. C-42 presence at PHASE 2 does not imply C-43 presence at PHASE 3: each execution phase's adversary declaration is independently necessary. Canonical PHASE 3 entry form: `ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase is skipped: percent is emitted as computed without consistency guard verification.` Form-agnostic: the adversary clause may appear as an inline prose line, a titled contract block, or a lifecycle entry annotation, provided it is physically resident within the PHASE 3 execution section. Requires C-42. Extends the execution-body adversary chain from one phase (PHASE 2, C-42) to two phases (PHASE 2 + PHASE 3). | 5 | structure | An explicit adversary declaration (ADVERSARY: clause or named adversary statement) is present within the PHASE 3 execution body. Adversary framing present only in the PHASE 2 execution body (C-42) or the COMMIT DECISION output-template section (C-16) is insufficient. The adversary clause must name the PHASE 3 execution adversary (inertia toward coverage-blind verdicts, or equivalent). C-42 pass required. |
| C-44 | **Preamble output declaration chain declaration** -- When C-41 (PHASE 3 execution-body OUTPUT DECLARATION with labeled sub-components) is satisfied, this criterion requires the preamble to contain an `OUTPUT DECLARATION CHAIN:` block that explicitly enumerates both the PHASE 2 output declaration and the PHASE 3 output declaration as a named two-element structural chain, asserting that each execution phase owns its own independently declared output structure. The preamble OUTPUT DECLARATION CHAIN parallels the dual-axis exit preamble of C-33/C-34: just as C-34 requires the preamble to enumerate both axes of the dual-axis exit invariant before the GUARD implements it, C-44 requires the preamble to enumerate both execution-phase output declarations before the execution phases implement them. The chain declaration names each link by phase (PHASE 2 OUTPUT DECLARATION, PHASE 3 OUTPUT DECLARATION) and asserts their structural independence (each phase declares its own output structure; neither phase's declaration implies the other). A preamble that describes output behavior generically without enumerating the two-phase output declaration chain fails C-44. A preamble that enumerates the dual-axis exit (C-34) without also carrying an OUTPUT DECLARATION CHAIN fails C-44: the two preamble declarations are independently required. The OUTPUT DECLARATION CHAIN preamble block may appear immediately adjacent to the dual-axis exit preamble (C-34) or as a separate preamble section, provided it is physically resident before the execution phases and independently named. Requires C-41. Extends the preamble architectural declaration pattern (C-33/C-34) from exit-condition invariants to output-declaration-residency invariants. | 5 | structure | The preamble contains an `OUTPUT DECLARATION CHAIN:` block (or equivalent named output-declaration-chain declaration) that names both the PHASE 2 output declaration and the PHASE 3 output declaration as a two-element structural chain and asserts their independence. A preamble with dual-axis exit declaration (C-34) but without an output declaration chain declaration fails. A preamble with output behavior description not organized as a named two-phase chain fails. C-41 pass required. |

**Implication map additions:** `C-43 => C-42`, `C-44 => C-41`

**Projected R14 variant scores under v14:**

| Variant | C-41 | C-42 | C-43 | C-44 | Total |
|---------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | PASS | 275 |
| V-02 | PASS | PASS | FAIL | PASS | 270 |
| V-03 | PASS | PASS | PASS | FAIL | 270 |
| V-04 | PASS | PASS | PASS | PASS | 275 |
| V-05 | PASS | PASS | PASS | PASS | 275 |

V-02 and V-03 score identically (270) -- symmetric 5-point delta confirming independent necessity and orthogonality of C-43 and C-44. No R14 variant fails both: the gap that defines Round 15.

---

## Structural Tier 14 (10 pts total) -- new in v15

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-45 | **Preamble adversary chain declaration** -- When C-43 (PHASE 3 execution-body adversary declaration) is satisfied, this criterion requires the preamble to contain an `ADVERSARY CHAIN:` block that explicitly enumerates both the PHASE 2 adversary declaration and the PHASE 3 adversary declaration as a named two-element structural chain, asserting that each execution phase owns its own independently declared adversary and that the two declarations guard against structurally distinct failure modes. The preamble ADVERSARY CHAIN parallels the dual-axis exit preamble (C-34) and the output declaration chain (C-44): just as C-44 requires the preamble to enumerate both execution-phase output declarations before the phases implement them, C-45 requires the preamble to enumerate both execution-phase adversary declarations before the phases encounter them. The chain declaration names each link by phase (PHASE 2 ADVERSARY: inertia toward evidence-blind commits; PHASE 3 ADVERSARY: inertia toward coverage-blind verdicts) and asserts structural independence (each phase's adversary is distinct; one phase's declaration does not imply the other). A preamble carrying C-44's OUTPUT DECLARATION CHAIN but without an ADVERSARY CHAIN fails C-45: the two preamble chain declarations are independently required. The ADVERSARY CHAIN block may appear adjacent to or separate from the OUTPUT DECLARATION CHAIN, provided it is physically resident in the preamble before the execution phases. The preamble now carries three architectural invariant blocks: dual-axis exit chain (C-34), output declaration chain (C-44), adversary chain (C-45). Requires C-43. Extends the preamble architectural declaration pattern from exit-condition invariants (C-34) and output-declaration-residency invariants (C-44) to adversary-chain-residency invariants. | 5 | structure | The preamble contains an `ADVERSARY CHAIN:` block (or equivalent named adversary-chain declaration) that names both the PHASE 2 adversary and the PHASE 3 adversary as a two-element structural chain and asserts their structural independence and distinct failure-mode targets. A preamble with output declaration chain (C-44) but without an adversary chain declaration fails. A preamble with generic adversary framing not organized as a named two-phase chain fails. C-43 pass required. |
| C-46 | **Adversary defeat condition sub-component** -- When C-43 (PHASE 3 execution-body adversary declaration, completing a two-phase adversary chain at PHASE 2 and PHASE 3) is satisfied, this criterion additionally requires that each phase-entry adversary declaration block carries a labeled `DEFEAT CONDITION:` sub-component naming the observable property that constitutes successful adversary defeat at that execution phase. C-42 and C-43 establish two-part adversary blocks (adversary name + trigger clause: `ADVERSARY: {name} -- default when skipped: {consequence}`). C-46 extends each such block to three-part form by adding `DEFEAT CONDITION: {observable property}` as a labeled sub-component at the same adversary declaration site. The DEFEAT CONDITION: sub-component is the adversary-block parallel of C-40's `INVARIANT:` and `OUTPUT FORM:` labeled sub-components within the OUTPUT DECLARATION: C-40 made the OUTPUT DECLARATION block sub-component-addressable; C-46 makes the adversary block sub-component-addressable. Canonical PHASE 2 form: `ADVERSARY: inertia toward evidence-blind commits -- default when this phase is skipped: each unverified signal ships without explicit assertion. DEFEAT CONDITION: every planned signal receives an explicit VERIFIED or UNVERIFIED disposition before EXPOSURE COMPUTATION begins.` Canonical PHASE 3 form: `ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase is skipped: percent is emitted without consistency guard verification. DEFEAT CONDITION: consistency guard executes and UNVERIFIED count is confirmed zero before percent is accepted as coverage.` A two-part adversary block without a DEFEAT CONDITION: sub-component satisfies C-42/C-43 but not C-46. The DEFEAT CONDITION: label must appear at both phase adversary declaration sites (PHASE 2 and PHASE 3); presence at one site only is insufficient. Form-agnostic: inline prose label and elevated titled sub-block both satisfy. Requires C-43. Extends the adversary block at each execution-phase-entry site from two-part to three-part labeled form. | 5 | structure | Both the PHASE 2 adversary declaration block and the PHASE 3 adversary declaration block each carry a labeled `DEFEAT CONDITION:` sub-component (or equivalent named defeat-condition label) naming the observable property constituting adversary defeat at that phase. A two-part adversary block (adversary + trigger only) at either site fails. Absence of DEFEAT CONDITION: at either phase site fails. C-43 pass required. |

**Implication map additions:** `C-45 => C-43`, `C-46 => C-43`

**Projected R15 variant scores under v15:**

| Variant | C-43 | C-44 | C-45 | C-46 | Total |
|---------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | PASS | 285 |
| V-02 | PASS | PASS | FAIL | PASS | 280 |
| V-03 | PASS | PASS | PASS | FAIL | 280 |
| V-04 | PASS | PASS | PASS | PASS | 285 |
| V-05 | PASS | PASS | PASS | PASS | 285 |

V-02 and V-03 score identically (280) -- symmetric 5-point delta confirming independent necessity and orthogonality of C-45 and C-46. No R15 variant fails both: the gap that defines Round 16.

---

## Structural Tier 15 (10 pts total) -- new in v16

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-47 | **Preamble adversary chain labeled sub-component entries** -- When C-45 (preamble `ADVERSARY CHAIN:` block present) is satisfied, this criterion additionally requires that the entries within the ADVERSARY CHAIN block carry individually labeled sub-component identifiers, using `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labels (or equivalent `PN-ADVERSARY:` phase-indexed form), making each phase adversary independently addressable by its phase label. C-45 establishes the ADVERSARY CHAIN block and requires it to name both PHASE 2 and PHASE 3 adversaries; a running-prose block that names both adversaries in sequence satisfies C-45 but fails C-47. C-47 requires labeled sub-entries -- the block must be organized so that a scorer can locate any individual phase adversary by its label without prose scanning. C-47 is the adversary-chain parallel of C-40's labeled-sub-component extension of C-38: C-40 made the OUTPUT DECLARATION block sub-component-addressable (INVARIANT:, OUTPUT FORM:); C-47 makes each entry within the ADVERSARY CHAIN preamble block phase-label-addressable. The label count tracks the declared adversary chain length: when C-48 is present (three-phase adversary chain including PHASE 1), three labels are required; when C-48 is absent (two-phase chain), two labels (`P2-ADVERSARY:`, `P3-ADVERSARY:`) satisfy the criterion -- the absence of a `P1-ADVERSARY:` label is not a C-47 violation when no PHASE 1 adversary body has been declared. Form-agnostic: inline labeled list entries and elevated PN-ADVERSARY titled sub-blocks both satisfy, provided the phase label is present at each entry position. Requires C-45. Extends C-45 from prose-enumerated adversary chain to labeled-sub-entry adversary chain with per-phase addressability. | 5 | structure | The preamble `ADVERSARY CHAIN:` block contains `PN-ADVERSARY:` labeled entries (P2-ADVERSARY: and P3-ADVERSARY: at minimum; P1-ADVERSARY: additionally required when C-48 is satisfied) at individually labeled sub-entry positions within the block. A block whose adversary names appear in running prose without per-entry labels fails. C-45 pass required. |
| C-48 | **PHASE 1 execution-body adversary declaration** -- When C-46 (three-part adversary block form -- ADVERSARY: + DEFEAT CONDITION: -- established at both PHASE 2 and PHASE 3) is satisfied, this criterion additionally requires an explicit adversary declaration within the PHASE 1 execution body at or near the phase's entry point, carrying the same three-part form. The PHASE 1 adversary block contains: (1) `ADVERSARY: {name}` naming the adversary for signal acquisition (e.g., inertia toward empty-glob assumption -- default when this phase is skipped: coverage is computed from memory rather than from live disk state); (2) `DEFEAT CONDITION: {observable property}` naming what constitutes defeat (e.g., DISK_SIGNALS populated from live glob result with zero-result case handled explicitly). C-42 and C-43 established a two-phase execution-body adversary chain at PHASE 2 and PHASE 3; C-46 established the three-part block form at those sites; C-48 extends both the adversary chain and the three-part block form to PHASE 1, completing a three-phase execution-body adversary chain spanning all principal execution phases (SIGNAL ACQUISITION, COMMITMENT ASSERTION, EXPOSURE COMPUTATION). The PHASE 2 and PHASE 3 adversary declarations do not imply a PHASE 1 adversary declaration: PHASE 1 adversary framing is independently necessary. The PHASE 1 adversary block must carry three-part form from its first appearance -- a two-part PHASE 1 adversary block satisfying form requirements from prior rounds but omitting DEFEAT CONDITION: fails C-48. Form-agnostic: inline prose, appended-below-GUARD-box, and elevated titled block all satisfy, provided the adversary block is physically resident within the PHASE 1 execution section. Requires C-46. Extends the execution-body adversary chain from two execution phases (PHASE 2 + PHASE 3) to all three principal execution phases, and extends the three-part adversary block form requirement from PHASE 2 and PHASE 3 to PHASE 1. | 5 | structure | An explicit adversary declaration is present within the PHASE 1 execution body carrying both `ADVERSARY:` (naming the PHASE 1 adversary) and `DEFEAT CONDITION:` (naming the observable defeat property) as labeled sub-components. A PHASE 1 execution body with only `ADVERSARY:` and no `DEFEAT CONDITION:` fails. Absence of any adversary framing at PHASE 1 fails. Adversary framing present only at PHASE 2 and PHASE 3 is insufficient. C-46 pass required. |

**Implication map additions:** `C-47 => C-45`, `C-48 => C-46`

**Projected R16 variant scores under v16:**

| Variant | C-45 | C-46 | C-47 | C-48 | Total | Notes |
|---------|------|------|------|------|-------|-------|
| V-01 | PASS | PASS | PASS | PASS | 295 | |
| V-02 | PASS | PASS | FAIL | PASS | 290 | C-47 withheld (prose ADVERSARY CHAIN) |
| V-03 | PASS | PASS | PASS | FAIL | 280* | C-48 withheld; contaminated by C-12/C-20 violations |
| V-04 | PASS | PASS | PASS | PASS | 295 | lifecycle GUARD contract form |

*V-03 scores 280, not 285, due to C-12 (-5) and C-20 (-5) violations from a
readiness-first template reordering axis introduced alongside C-48 withholding.
The V-02/V-03 delta is asymmetric (290 vs 280) -- V-02 is -5 from V-01 (C-47 only);
V-03 is -15 from V-01 (C-48 + C-12 + C-20). Clean C-48 isolation requires V-03
redesign preserving C-12/C-20 compliance. The gap that defines Round 17 is C-47
and C-48 jointly satisfied above 295 -- no R16 variant fails both.

---

## Structural Tier 16 (5 pts total) -- new in v17

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-49 | **PHASE 1 adversary defeat STOP predicate** -- When C-48 (PHASE 1 execution-body adversary declaration with three-part block form including a named DEFEAT CONDITION) is satisfied, this criterion additionally requires an explicit predicate within the STOP CONDITION (or equivalent execution gate) verifying that the PHASE 1 adversary defeat condition was met: specifically, that DISK_SIGNALS was populated from a live glob result with the zero-result case handled explicitly, as named in the C-48 DEFEAT CONDITION sub-component. The predicate operationalizes the C-48 DEFEAT CONDITION at the gate: the adversary block declares what constitutes defeat; the STOP predicate checks that the declared defeat condition was observed before execution proceeds to display. A STOP CONDITION that carries predicates for PHASE 2 and PHASE 3 adversary defeat conditions but omits the PHASE 1 defeat predicate fails this criterion when C-48 is satisfied: the PHASE 1 adversary has been declared and its defeat condition named, but no gate check enforces it. When C-48 is absent (two-phase adversary chain only), the STOP CONDITION is structurally complete without a PHASE 1 defeat predicate -- C-49 is vacuously satisfied regardless of predicate count. A STOP CONDITION that carries the 4th predicate structurally while C-48 is absent (predicate present but no PHASE 1 adversary to check) satisfies C-49 vacuously: the gate commitment is not violated from the STOP side. The criterion enforces adversary-chain synchronization: each declared adversary's defeat condition must be checked at the gate. C-49 is the STOP-gate parallel of C-48: C-48 declares the PHASE 1 adversary and names its defeat condition; C-49 requires that named defeat condition to be enforced by a gate predicate before rendering output. Form-agnostic: the predicate may appear as an inline STOP clause, a GUARD box predicate entry, a named exit branch in the DISPLAY GATE, or a pre-display assertion, provided it is identifiable as a check of the PHASE 1 adversary defeat condition as declared in C-48. Canonical form: `STOP if DISK_SIGNALS unpopulated or zero-result case unhandled (PHASE 1 adversary not defeated)` or equivalent. Requires C-48 for non-vacuous evaluation. | 5 | structure | When C-48 is satisfied: an explicit gate predicate checking the PHASE 1 adversary defeat condition (DISK_SIGNALS populated from live glob, zero-result handled) is present in the STOP CONDITION or equivalent execution gate. Absence of this predicate while C-48 is satisfied fails the criterion. When C-48 is absent: criterion is vacuously satisfied regardless of predicate presence. |

**Implication map note:** C-49 has a conditional prerequisite. When C-48 is present,
C-49 requires the PHASE 1 defeat predicate at the STOP gate. When C-48 is absent,
C-49 is vacuously satisfied -- C-48 failure does NOT cascade to C-49 failure. No
hard implication `C-49 => C-48` is added to the implication map; the conditional
relationship is documented here and in the R18 structural note. This is the first
criterion in this rubric with vacuous-PASS behavior.

**Projected R18 variant scores under v17:**

| Variant | C-47 | C-48 | C-49 | Total | Notes |
|---------|------|------|------|-------|-------|
| V-01 | PASS | PASS | PASS | 300 | Full tier-16 baseline |
| V-02 | FAIL | PASS | PASS | 295 | C-47 withheld; C-49 genuine PASS |
| V-03 | PASS | FAIL | PASS* | 295 | C-48 withheld (clean); C-49 vacuous |
| V-04 | PASS | PASS | FAIL | 295 | C-49 withheld (4th STOP pred absent) |
| V-05 | FAIL | FAIL | PASS* | 290 | C-47+C-48 withheld; C-49 vacuous |

*Vacuous PASS: STOP predicate structurally present but checks no PHASE 1 adversary
(C-48 absent). C-49 criterion not violated from the gate side.

V-02, V-03, V-04 each score 295 -- three distinct 5-point deltas from V-01, each
isolating a different criterion (C-47, C-48, C-49 respectively). V-03 redesign
from R17 eliminates the R16 contamination: clean C-48 isolation confirmed.

---

## Implication Map

```
C-02 => C-01
C-03 => C-01
C-05 => C-03
C-09 => C-05
C-13 => C-11
C-14 => C-11
C-15 => C-11
C-16 => C-05
C-17 => C-13
C-18 => C-14, C-17
C-19 => C-16
C-20 => C-18, C-12
C-21 => C-11, C-19
C-22 => C-07
C-23 => C-21
C-24 => C-17, C-21
C-25 => C-22
C-26 => C-23
C-27 => C-23, C-24
C-28 => C-25, C-21
C-29 => C-28, C-05
C-30 => C-12
C-31 => C-09, C-25
C-32 => C-30
C-33 => C-30
C-34 => C-33
C-35 => C-34
C-36 => C-32, C-34
C-37 => C-32, C-35
C-38 => C-36
C-39 => C-38, C-37
C-40 => C-38
C-41 => C-40, C-39
C-42 => C-16
C-43 => C-42
C-44 => C-41
C-45 => C-43
C-46 => C-43
C-47 => C-45
C-48 => C-46
-- C-49: conditional prerequisite C-48 (non-vacuous only); not a hard implication
```
