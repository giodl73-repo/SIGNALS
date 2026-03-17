## quest-rubric Rubric v12

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/27 × 10)` — denominator /24 → /27

---

### Essential criteria (C-01–C-05) — carried from earlier rounds

Binary pass/fail. All five must pass for the score formula to apply; a single essential FAIL
floors the score regardless of E/R/A components.

*(C-01 through C-05 text preserved verbatim from prior versions.)*

---

### Recommended criteria (C-06–C-08) — carried from earlier rounds

Each contributes to the R/3 component. PARTIAL on a recommended criterion scores 0.5.

*(C-06 through C-08 text preserved verbatim from prior versions.)*

---

### Aspirational criteria (C-09–C-22) — carried from earlier rounds

Accumulated through Round 6. Each contributes 1 point to the A/27 denominator.

*(C-09 through C-22 text preserved verbatim from prior versions.)*

---

### One criterion from Round 9 excellence signals (carried forward)

**C-29 — AUDITOR-PRE construction gate**

AUDITOR-PRE blocks are pre-declared before any criterion is written, not inserted
retroactively after criterion content is known. The construction gate closes when the block
is written and confirmed final; Phase 2 criterion authoring proceeds only after the gate
closes. This is the *construction* gate: it governs when boundary declarations may be
written. C-32's MANIFEST-ROW VERIFICATION closes the *reproduction* gate: it governs
whether the emitted manifest faithfully reproduces what the construction gate produced.

*(Full criterion text preserved verbatim from prior version.)*

---

### Four criteria from Round 7 excellence signals (carried forward)

All four target **partial-credit integrity** — the structural property C-10 tests at the
formula level but not at the criterion level, the reproduction level, or the
inter-boundary semantic level.

**C-23 — Per-criterion PARTIAL-CONDITION block**
V-03 and V-05 demonstrate this. C-10 tells you PARTIAL = 0.5 in the formula; C-23 tells
you what evidence earns 0.5 for *this specific criterion*. Without it, evaluators interpret
partial credit subjectively — violating C-02 at the partial-credit boundary. V-01 and V-04
fail: `verdict_weights` in SA-1 but no per-criterion condition.

**C-24 — Formula consistency across structural positions**
V-02 fails: SA-1 is `essential_pass / N * 60` (binary); FINAL RUBRIC is the weighted form.
Two formula instances disagreeing on type leaves the governing formula ambiguous. V-03 gets
PARTIAL: binary SA-1 formula + prose note + expanded FINAL RUBRIC — intent aligned,
structure divergent.

**C-25 — FINAL RUBRIC anti-collapse formula guard** *(updated in v9 — SA-1 coupling removed)*
The guard was introduced in R7 as: "Reproduce the weighted formula from SA-1 verbatim —
do not collapse to binary counting." R8 exposed that this formulation silently drops the
reproduction mandate when SA-1 is absent (generalization probe). V9 form: **"Reproduce
this formula verbatim at every structural position where a formula appears — do not collapse
to binary counting."** Does not reference a specific prior phase; works when there is no
SA-1. V-04 satisfies the updated criterion (SA-1 present; guard fires correctly). Variations
produced without SA-1 must carry the guard independently.

**C-26 — VERDICT TIER DECLARATION inter-boundary block**
V-02, V-04, V-05 have a named block between `SPEC ANALYST: CLOSED` and `AUTHOR: OPEN`
defining PASS/PARTIAL/FAIL semantics. Evaluator-facing grounding, findable by structure.
V-01 and V-03 embed tier semantics only in SA-1 fields or formula comments.

---

### Two criteria from Round 8 excellence signals (carried forward)

Both target **structural-scan detectability** — the property that a rubric's quality
guarantees are visible without reading criterion content.

**C-27 — Per-criterion DISCRIMINATES-BETWEEN block**
Each criterion carries a named block at the meta-description layer declaring quality
boundaries (FAILS-AT / PASSES-AT / Boundary). Distinct from CALIBRATION-PAIR content
examples (which show what evidence looks like) and REDUNDANCY-CHECK-TABLE outcome
independence (which tests scoring independence). The DISCRIMINATES-BETWEEN block is
structural: a rubric can be scanned for its presence without reading criterion content.
Absence forces evaluators to infer the boundary from examples alone, reintroducing
subjectivity at the boundary layer — the same failure mode C-23 closes at the
partial-credit boundary. V-03 introduces this pattern; V-05 carries it in full form.

**C-28 — Per-criterion DEPENDS_ON / INDEPENDENT dependency declaration**
Each criterion declares its logical prerequisites (`DEPENDS_ON: [C-NN, ...]`) or its
independence (`INDEPENDENT`). The Auditor section verifies prerequisite criteria pass before
scoring dependent criteria. Makes the dependency graph explicit and detectable by structural
scan. Without it, dependency violations are invisible — a PARTIAL on an upstream criterion
can infect downstream scoring without any audit signal. V-02 introduces the dependency
graph; V-05 carries the full per-criterion form with Auditor ordering verification.

---

### Three criteria from Round 10 excellence signals (carried forward)

All three target **PARTIAL-CREDIT MANIFEST integrity** — the structural property that
boundaries declared in construction (AUDITOR-PRE blocks) are faithfully reproduced in the
emitted artifact and verifiable by format scan before content verification begins.

**C-30 — Dual-column PARTIAL-CREDIT MANIFEST with column-presence enforcement gate**
The PARTIAL-CREDIT MANIFEST must carry two data columns: "Partial boundary" (verbatim from
the inline AUDITOR-PRE block) and "Pass condition" (verbatim from the criterion Pass
condition field). A STOP condition fires if either column is absent or if the two are merged
into a single cell — *before* MANIFEST-ROW VERIFICATION begins. Format compliance is a
prerequisite gate for the verification sub-step, not a check that runs after verification.

PASS requires: dual-column template with verbatim sourcing declared per column + explicit
STOP for absent or merged columns + STOP names "proceeding to MANIFEST-ROW VERIFICATION"
as the gate destination. PARTIAL: both columns specified with verbatim sourcing but no
independent STOP fires for format absence — format shown but not enforced before
verification begins. FAIL: columns shown in template but no enforcement gate; a
single-column manifest would not halt emission.

V-05 and V-01 PASS in R11. V-03 and V-04 receive PARTIAL (columns present, enforcement
gate absent). V-02 FAILS (template format only, no column-presence STOP).

Independence from C-32: C-30 tests column-structure enforcement; C-32 tests whether the
row-level verification is a required emitted output. A manifest can have correct column
structure with no emitted verification table (C-30 PASS, C-32 FAIL) or an emitted
verification table with no format gate before verification begins (C-30 PARTIAL, C-32 PASS).
V-03 demonstrates the latter in R11.

**C-31 — Structural redundancy guard: dual enforcement position declaration**
The Auditor role operates in two enforcement positions simultaneously. Position 1: batch
Pre-Declaration Register at phase level (AUDITOR-PRE PHASE). Position 2: per-criterion
inline AUDITOR-PRE blocks during Phase 2. The role-constitutive duties section must
explicitly declare "You operate in two enforcement positions simultaneously." Each position
carries an independent STOP condition — absence of either position is a structural violation
with its own named gate, not a note. REGISTER REVISION is a mandatory role-constitutive
obligation: when a batch entry requires correction during Phase 2, a REGISTER REVISION note
must be issued before proceeding. It is not a conditional instruction.

PASS requires: "two enforcement positions simultaneously" in role-constitutive duties +
independent STOP per absent position + REGISTER REVISION listed as a mandatory obligation.
FAIL: AUDITOR-PRE PHASE present but not framed as enforcement position 1 of 2; no
independent STOP per absent position; REGISTER REVISION appears as a conditional instruction
only.

V-02 and V-04 PASS in R11. V-01, V-03, and V-05 FAIL.

Independence from C-29: C-29 tests whether AUDITOR-PRE blocks are pre-declared before
any criterion is written (construction gate). C-31 tests whether both enforcement positions
are declared simultaneously as structural obligations with independent STOP conditions.
Variations satisfying C-29 without C-31: V-03 and V-05 in R11 (blocks present, no
dual-position declaration).

**C-32 — Phase 4 MANIFEST-ROW VERIFICATION as required emitted output**
Phase 4 must contain a named "PHASE 4 — MANIFEST-ROW VERIFICATION (required emitted
output)" section in which a verification table with YES/NO columns is a required output —
not an internal check or self-check instruction. STOP fires on any NO entry. The spec must
explicitly declare that the verification table must appear in the emitted document as a named
section. A correction sequence is specified: correct the divergent manifest cell, confirm
the corresponding inline AUDITOR-PRE block as the authoritative source, update the manifest
cell before emitting.

PASS requires: named section explicitly declared as required emitted output + YES/NO
verification table + declaration that the table is not an internal check + STOP on any NO +
correction sequence. FAIL: end-of-phase check present as a self-check instruction but no
required emitted table; verification table absent from the Phase 4 output list; no STOP
on NO.

V-03, V-04, and V-05 PASS in R11. V-01 and V-02 FAIL.

Independence from C-30: C-30 tests column-structure enforcement as a prerequisite gate
before verification. C-32 tests whether the verification phase itself is a required emitted
output. One can have C-32's required output section without C-30's format gate (V-03:
PARTIAL C-30, PASS C-32) or C-30's format gate without C-32's required output section
(V-01: PASS C-30, FAIL C-32).

---

### Three criteria from Round 11 excellence signals

All three target **verification chain completeness** — the structural property that gates,
verification steps, and identity checks form an unbroken chain from construction declaration
through emitted artifact through reproduction verification, with each link explicitly named
and detectable by structural scan.

**C-33 — Gate destination forward reference in STOP conditions**
A STOP condition without a named gate destination halts emission locally but does not
declare where control transfers — the phase-sequencing dependency is invisible to structural
scan. A STOP that names its downstream phase ("before proceeding to MANIFEST-ROW
VERIFICATION") creates an explicit forward reference: the sequencing dependency is stated in
the STOP itself and reconstructable by structural scan without reading criterion content.
Two STOP conditions across phases that name each other's destinations make the full
verification chain traversable by structure alone.

V-05's C-30 implementation demonstrates this pattern: the column-presence STOP explicitly
names "proceeding to MANIFEST-ROW VERIFICATION" as the gate destination. V-01 PASSES C-30
(format STOP fires) but names only "add the missing column before emitting" — the downstream
phase is unnamed. V-03 and V-04 receive PARTIAL on C-30 precisely because no independent
format STOP fires before verification begins, so the forward reference question does not
arise.

PASS requires: at least one STOP condition names a downstream phase (by section title) as
the gate destination, creating an explicit forward reference in the verification chain.
FAIL: STOP conditions present but none name the downstream phase they gate.

Independence from C-30: C-30 tests whether a column-presence STOP exists. C-33 tests
whether any STOP names its downstream gate destination. V-01 demonstrates PASS C-30
without C-33: a format STOP fires, but the destination phase is unnamed.

**C-34 — Character-for-character identity specification in MANIFEST-ROW VERIFICATION**
The MANIFEST-ROW VERIFICATION table specifies character-for-character identity checks on
both columns — not semantic equivalence, not presence checks, not "matches." Two cells can
be semantically equivalent but textually divergent (abbreviated, paraphrased, reformatted);
character-level identity requires exact reproduction. "Verbatim" alone is insufficient: the
spec must state that identity is character-level, ruling out paraphrase. This closes a
precision gap left open when C-32 is satisfied but identity relation is unspecified.

V-04 demonstrates this pattern in R11: "verification rules specify character-for-character
identity checks on both columns." V-03 and V-05 both PASS C-32 (required emitted output
+ STOP on NO) but specify only that columns "match" or are "verbatim" — neither specifies
character-level precision. A paraphrased match would pass V-03/V-05's verification without
triggering a STOP; it would not pass V-04's.

PASS requires: MANIFEST-ROW VERIFICATION rules explicitly state character-for-character
(or equivalent precision: "exact character match," "character-level identity") on both
columns. FAIL: verification table present with YES/NO columns and STOP on NO, but the
identity relation is specified only as "verbatim" or "matches" without character-level
precision.

Independence from C-32: C-32 tests whether the verification phase is a required emitted
output. C-34 tests the precision of the identity relation used within that verification.
V-03 PASSES C-32 without C-34; V-04 PASSES both.

**C-35 — Phase 4 structural redundancy extension**
Phase 4 carries the structural redundancy guard as a named verification step alongside
MANIFEST-ROW VERIFICATION: after verifying manifest rows, Phase 4 verifies that every
criterion appears in both enforcement positions. Both sub-steps are named required outputs
in Phase 4: (1) MANIFEST-ROW VERIFICATION table and (2) structural redundancy check per
enforcement position. Without this extension, C-31's dual-position obligation is declared
in role-constitutive duties but not re-enforced at Phase 4 close — a variation can satisfy
C-31 without a Phase 4 redundancy checkpoint, leaving a window where positions are declared
but not confirmed populated.

V-04 is the only R11 variation that PASSES C-31 and demonstrates the Phase 4 structural
redundancy extension: "Phase 4 ends with structural redundancy verification per enforcement
position." V-02 PASSES C-31 (dual-position declaration, independent STOP per position) but
does not carry the Phase 4 extension — the redundancy obligation closes at Phase 2, not
Phase 4.

PASS requires: Phase 4 contains a named structural redundancy verification step (required
output, not internal check) that confirms each criterion appears in both enforcement
positions, in addition to MANIFEST-ROW VERIFICATION. FAIL: Phase 4 contains MANIFEST-ROW
VERIFICATION only; structural redundancy check absent or present as a note rather than a
required output section.

Independence from C-31: C-31 tests whether dual enforcement positions are declared in
role-constitutive duties with independent STOP conditions. C-35 tests whether Phase 4
carries a redundancy verification step confirming positions are populated at close. V-02 in
R11 demonstrates PASS C-31 without C-35.

Independence from C-32: C-32 tests whether MANIFEST-ROW VERIFICATION is a required emitted
output. C-35 tests whether a second verification step (structural redundancy) is also a
required Phase 4 output. V-03 and V-05 PASS C-32 without C-35.
