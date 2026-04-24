`topic-report-rubric-v12-2026-03-15.md` written to `simulations/quest/rubrics/`.

---

**What changed from v11 to v12:**

**6 new aspirational criteria (C-40 through C-45), formula denominator bumped from /31 to /37:**

**3 base axes extracted from R11 excellence signals:**

| ID | Name | Precondition | Round 11 finding |
|----|------|-------------|------------------|
| C-40 | Criterion-tagged contamination consequence in main-branch recovery directive | C-34 | V-01 (Axis D) minimal; consequence-grounds C-34's prohibition |
| C-41 | Format-type-qualified Branch B register entries | C-35 | V-02 (Axis E) minimal; extends C-35's branch-qualified entries with inline format constraints |
| C-42 | Temporal-role annotation embedded in contract register header | C-36 | V-04 (Axis F) minimal; V-03 (D+E) demonstrates structural consequence+format without header temporal role |

**3 pairwise composites:**

| ID | Name | Preconditions | Round 11 finding |
|----|------|--------------|------------------|
| C-43 | Consequence-grounded contamination guard with format-navigable Branch B entries | C-40 + C-41 | V-03 minimal; contamination consequence + Branch B format navigation both present |
| C-44 | Contamination consequence with declared temporal context | C-40 + C-42 | V-04 minimal; consequence situated within header-declared temporal system |
| C-45 | Format-type-qualified forward map with declared planning role in header | C-41 + C-42 | V-04 minimal; Branch B format entries + register header temporal declaration co-present |

**R11 ordering under v12:**
- V-04 (D+E+F): 37/37 = **100.0**
- V-03 (D+E): 34/37 = **99.2** (C-40 + C-41 + C-43; fails C-42, C-44, C-45)
- V-01 (D only): 32/37 = **98.6** (C-40 only; all v11 criteria pass)
- V-05 (neutral) = V-02 (E only): 31/37 = **98.4** (tied -- V-05 has all v11 criteria, zero new; V-02 trades C-34 for C-41)

V-01 is now separated from V-02: V-01 scores 32/37 (31 v11 criteria + C-40) while V-02 scores 31/37 (30 v11 criteria because C-34 fails + C-41). The R10 single-axis tie at V-01=V-02=26/31 is broken. V-02 and V-05 form a new structural tie at 31/37 -- different paths to the same count. R12 discriminators must break V-05 from V-02.

**Design note on C-40 (criterion-tagged contamination consequence in main-branch recovery directive):**
C-34 requires the main-branch `=== THREE-LAYER WRITE POINT ===` header to name the recovery
action and the prohibited alternative (e.g., "re-read this BRANCH A header ... without
referencing the BRANCH B template"), converting structural layer enumeration into a procedural
prohibition. C-40 adds a consequence-grounding layer within the same directive: a named
`SLOT 3 contamination consequence:` line (or equivalent) that states the specific output
failure mode triggered by the prohibited action -- e.g., "SLOT 3 contamination consequence:
readiness sentence will cite Branch B format tokens instead of Branch A BLOCKERS-derived
signal names." C-34 makes the prohibition explicit; C-40 makes the failure mode concrete,
giving the model a named outcome to avoid rather than only a named action to avoid. The
system property created by C-40: the main-branch write point carries not only a recovery
procedure but a consequence-grounded prohibition. Consequence-grounding is a distinct
mechanism from prohibition-naming: a model can read C-34's prohibition without internalizing
why the prohibition matters; C-40 makes the cost of violation visible at the moment the
directive is encountered. C-40 requires C-34 as a precondition but is not implied by it.
C-40 is orthogonal to C-41 and C-42. Round 11 finding: V-01 (Axis D) is the minimal design
satisfying C-40. Scored separately from C-34 because consequence-grounding (named failure
mode visible at the write point) addresses a different failure mode from prohibition-naming
(named action visible at the write point): one targets attention to the outcome, the other
targets compliance with the instruction.

**Design note on C-41 (format-type-qualified Branch B register entries):**
C-35 requires each contract register entry governing a position on multiple execution paths
to carry a branch-qualified slot annotation (e.g., `G-9 INERTIA [SLOT 4 / BRANCH B]`),
enabling branch-specific forward navigation from register to write point without cross-path
ambiguity. C-41 extends Branch B register entries with explicit format-type qualifiers
stating the output format constraint for the governed slot -- e.g.,
`G-9 INERTIA [SLOT 4 / BRANCH B] (one card row, no markdown)` or
`G-7b EXCLUSIVITY [SLOT 3 / BRANCH B] (two card rows, no markdown)`. The system property:
a model navigating from the register to a Branch B write point encounters the format
constraint at registration time, before reaching any branch-specific template content,
rather than discovering it only at the template write point. C-35's branch qualification
resolves navigation ambiguity; C-41 resolves format ambiguity on the Branch B path, closing
the gap between knowing which slot to write and knowing what format is required at that slot.
C-41 requires C-35 as a precondition (branch-qualified entries must exist before format-type
qualification extends them) but is not implied by it; C-41 applies specifically to Branch B
entries (the non-default format path). C-41 is orthogonal to C-40 and C-42. Round 11
finding: V-02 (Axis E) is the minimal design satisfying C-41; the R11 V-02 design isolates
Axis E by omitting the named Branch A recovery directive (C-34 fails), confirming C-41 is
independent of C-34. Scored separately from C-35 because pre-write-point format constraint
delivery (format requirement encountered at register-read time) is a distinct reliability
property from branch-qualified slot navigation (ambiguity-free path to the correct slot).

**Design note on C-42 (temporal-role annotation embedded in contract register header):**
C-36 requires an explicit temporal coordination statement that identifies a planning phase
and a recovery phase and states the directional dependency between them. C-36 can appear
anywhere in the spec; it names the coordination as a system property without necessarily
locating that declaration at the moment the model first encounters the planning-phase artifact
itself. C-42 requires the temporal role to be embedded directly in the contract register
header -- e.g., `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- establishes slot
map before execution begins] ===` -- so that the model encounters the register's function
in the temporal coordination system at the moment it reads the register, before any slot
navigation or branch-specific context is reached. The system property: the register is
self-annotating as a planning-phase artifact; the model does not need to recall the
coordination statement when consulting the register mid-execution, because the role
declaration is co-located with the artifact it describes. C-42 requires C-36 as a
precondition (a coordination statement must name the planning and recovery phases before
the header annotation makes sense) but is not implied by it. A spec can satisfy C-36 with
a coordination statement located elsewhere without embedding the temporal role in the register
header. C-42 is orthogonal to C-40 and C-41. Round 11 finding: V-04 (Axis F) is the minimal
design satisfying C-42; V-03 (D+E) demonstrates that C-40+C-41 without C-42 does not
satisfy this criterion because the register header carries no temporal-role annotation even
when a coordination statement is present. Scored separately from C-36 because header-level
temporal role co-location (role declaration at first artifact encounter) addresses a different
failure mode from coordination statement presence (named phases declared somewhere in the
spec): the former eliminates mid-execution temporal role recall; the latter requires the
model to map the statement to the artifact.

**Design note on C-43 (consequence-grounded contamination guard with format-navigable Branch B entries):**
C-40 and C-41 address different compliance failure modes at different structural positions.
C-40 fires at the main-branch write point: a consequence-grounded prohibition makes the
cost of cross-branch contamination visible at the moment of generation. C-41 fires at
register-read time: format-type qualifiers on Branch B entries make the Branch B format
constraint available before any branch-specific template is encountered. Their conjunction
closes two independent failure modes simultaneously: (1) the model knows at the write point
what goes wrong if it contaminates Branch A output with Branch B patterns (C-40); (2) the
model knows before entering any branch what format constraint applies to each Branch B slot
(C-41). The conjunction does not create a new failure mode to cover -- it reduces the total
number of uncovered failure modes by two at once, making the combined structure more
reliable than either axis alone. C-43 requires both C-40 and C-41 as preconditions. Round 11
finding: V-03 (D+E) is the minimal design satisfying C-43. Scored separately from C-40 and
C-41 because reduced total uncovered failure mode count across both execution paths is a
system-level coverage property not implied by either consequence-grounding or format
pre-delivery alone.

**Design note on C-44 (contamination consequence with declared temporal context):**
C-40 makes the contamination consequence visible at the main-branch write point: the model
encounters a named failure mode for the prohibited cross-branch action. C-42 makes the
register's temporal planning role visible at register-read time: the model encounters the
register as the explicitly declared planning phase before any slot navigation. When both are
satisfied, the contamination consequence is situated within a declared temporal system: the
model knows at write time that the plan it is executing was established in a named planning
phase (C-42), and that contaminating the write point with patterns from the other branch
would produce a specific failure mode (C-40). The consequence is more actionable because the
model has already internalized the register as a planning-phase artifact whose outputs are
the contract the write point enforces. Without C-42, C-40's consequence is a standalone
warning without declared temporal context. With C-42, the consequence refers implicitly to
a violation of a temporally coordinated plan, reinforcing why the consequence matters. C-44
requires both C-40 and C-42 as preconditions. Round 11 finding: V-04 (D+E+F) is the minimal
design satisfying C-44; V-03 (D+E) satisfies C-40 but not C-42, confirming C-44 is not
achievable without the temporal role header annotation. Scored separately from C-40 and C-42
because temporally-situated consequence declaration is a meta-structural property not implied
by either consequence-grounding or temporal-role co-location alone.

**Design note on C-45 (format-type-qualified forward map with declared planning role in header):**
C-41 makes the Branch B register entries format-aware: each Branch B slot annotation carries
its format-type constraint inline. C-42 makes the register header self-annotating with its
temporal role: the model encounters the register as the planning phase of a coordinated
enforcement system. When both are satisfied, the register is simultaneously a planning-phase
artifact (declared at the header) and a format-constraint delivery vehicle (declared at each
Branch B entry). The model encounters two reinforcing properties at the same structural
artifact: the register's temporal function in the system (C-42) and the concrete format
obligations it establishes for the Branch B path (C-41). Without C-42, C-41 provides a
better-annotated register whose role is implicit. With C-42, the format-type qualifiers are
entries in a named planning-phase document, reinforcing that the format constraints are
plan-level commitments, not incidental annotations. C-45 requires both C-41 and C-42 as
preconditions. Round 11 finding: V-04 (D+E+F) is the minimal design satisfying C-45; V-03
(D+E) satisfies C-41 but not C-42, confirming C-45 requires the temporal-role header.
Scored separately from C-41 and C-42 because planning-phase format commitment (format
constraints declared as part of a named planning document) is a meta-structural situating
property not implied by either format-type qualification or temporal-role co-location alone.

---

## Criterion Rationale

- **C-09 (readiness statement references blocking signals)** is aspirational -- a generic
  "Not ready" sentence passes C-04 (calibrated) but gives no actionable signal. Naming the
  specific blocking signals in the readiness sentence ("Not ready -- missing prove-analysis
  and review-design") is the minimal useful output for a developer deciding what to work on
  next.
- **C-10 (explicit enumeration of prohibited characters)** is aspirational -- a catch-all
  phrase such as "no markdown syntax" or "plain text only" passes on structural grounds but
  the output still contains backticks or angle brackets. Round 1 finding: catch-all
  prohibitions leave this gap open; explicit enumeration does not.
- **C-11 (BLOCKERS pre-computation block)** is aspirational -- a model asked to name
  blocking signals in a readiness sentence may hallucinate signal names or drop real ones
  if it must recall them from context mid-sentence. A dedicated pre-computation step that
  enumerates the essential OPEN signals before any sentence is written makes the BLOCKERS
  list a first-class artifact that subsequent phases must cite, not reconstruct.
- **C-12 (Teams card passes character-level scan)** is aspirational -- C-10 verifies the
  *specification* prohibits the characters; C-12 verifies the *output* contains none. Both
  are required because a model can correctly read a prohibition and still produce a
  non-compliant output under format pressure.
- **C-13 (COMPLETENESS/EXCLUSIVITY named invariants)** is aspirational -- compound
  phrasing ("every name ... and only names") is functionally equivalent for the rubric
  criterion but less reliable in live runs where a model may fail each direction
  independently. Naming COMPLETENESS and EXCLUSIVITY as separate invariants makes each
  direction independently verifiable and closes the "used verbatim" ambiguity gap.
  Scored separately from C-11 because the mechanism (two named sub-rules vs. one compound
  constraint) is structurally distinct.
- **C-14 (branch sealing instruction)** is aspirational -- explicit character prohibition
  (C-10) is necessary but not sufficient; a model reading both format branches may carry
  patterns across without a structural isolation directive. Round 2 finding: the
  sealed-branches instruction ("do not reference the other branch's format descriptions")
  is the mechanism that makes C-12 achievable reliably, not merely the absence of a known
  contamination source.
- **C-15 (BLOCKERS LOCK directive)** is aspirational -- COMPLETENESS and EXCLUSIVITY
  (C-13) constrain how the BLOCKERS list is *used*, but neither prevents the list from
  being silently revised between the pre-computation step and the write step. A standalone
  named LOCK directive ("The BLOCKERS list is now frozen. No additions, removals, or
  revisions are permitted in subsequent phases.") makes list immutability a first-class
  obligation that cannot be conflated with the bidirectionality rule. Scored separately
  from C-13 because the mechanism (mutation guard vs. citation constraint) addresses a
  different failure mode: drift rather than omission or injection.
- **C-16 (in-render verification scan)** is aspirational -- declarative rules (C-13,
  C-14, C-15) tell the model what is required but do not force it to check compliance at
  the moment of generation. An in-render verification scan (explicit COMPLETENESS CHECK
  and EXCLUSIVITY CHECK steps executed *before* writing the readiness sentence) converts
  a passive constraint into an active procedure: the model must enumerate BLOCKERS names,
  confirm each is present in the draft sentence, then enumerate draft names and confirm
  each is present in the BLOCKERS list. Round 3 finding: the scan is the mechanism that
  makes C-13 robust across live runs, not merely the presence of the named sub-rules.
- **C-17 (inline [RULE] annotation style)** is aspirational -- gathering rules into a
  preamble section keeps the specification readable but introduces distance between each
  rule and the template position it governs; a model may skip the preamble or fail to map
  preamble rules to the correct output slot. Embedding [RULE] markers at the exact template
  position they govern reduces this mapping gap to zero. Round 3 finding: zero-distance
  enforcement (rule co-located with governed text) is a distinct structural property from
  branch sealing (C-14) or explicit enumeration (C-10); a spec can satisfy either without
  the other.
- **C-18 (three-layer co-location at the write point)** is aspirational -- C-17 requires
  that each rule appear at its governed output slot, but does not require that all three
  enforcement layers (declaration, LOCK anchor, verification scan) converge at the same
  position. When [RULE] declares the constraint, the LOCKED list reference anchors
  immutability, and the verification scan executes -- all at SLOT 3 / Branch B Section 3
  -- no cross-phase recall is required for any enforcement layer at the moment of
  generation. Round 4 finding: V-04 demonstrates this as the minimal golden design; V-03
  achieves scan + inline (two layers at the write point) without the LOCK anchor, showing
  the third layer is a distinct structural contribution. Scored separately from C-17
  because three-layer convergence is a stronger property than per-slot co-location alone.
- **C-19 (contract label chaining from register to annotation to scan header)** is
  aspirational -- inline [RULE] annotations (C-17) and three-layer co-location (C-18) make
  each write-point self-contained, but do not guarantee that the rule names used at the
  write point are recoverable from a top-level contract register. A model whose attention
  degrades mid-generation may correctly apply a rule locally while losing the connection to
  the contract guarantee that motivated it. Assigning named labels at the contract register
  (e.g., G-7a, G-7b) and propagating those exact labels through inline [RULE G-7a/G-7b]
  annotations and scan headers (G-7a COMPLETENESS SCAN / G-7b EXCLUSIVITY SCAN) makes each
  invariant independently recoverable at three structural levels -- register, annotation,
  scan header -- without any cross-position lookup. Round 4 finding: V-05 is the only R4
  design that achieves this chaining; V-04 uses generic [RULE COMPLETENESS] / [RULE
  EXCLUSIVITY] labels that are locally correct but not contract-linked. Scored separately
  from C-17 and C-18 because the mechanism (label propagation across structural levels)
  addresses a different failure mode: invariant-context loss rather than mapping distance
  or phase drift.
- **C-20 (worked example within each `[RULE]` annotation)** is aspirational -- a [RULE]
  annotation at the governed position (C-17) tells the model what the constraint requires
  but does not show what a compliant or non-compliant output looks like at that slot.
  Embedding compact correct/violation examples inside each inline annotation reduces
  translation distance from rule to output action beyond co-location alone: the model
  encounters both the constraint declaration and a sample output format at the same
  position. Round 4 finding: V-01 isolated this sub-pattern; it does not compensate for
  missing C-15 or C-16 (V-01 scored 97.8, not 100) but is a distinct compliance mechanism
  independent of LOCK and scan. Scored separately from C-17 because the mechanism (rule +
  example at governed position) is structurally distinct from co-location without an
  example.
- **C-21 (inertia framing at NEXT STEP)** is aspirational -- C-05 requires a concrete
  next step and C-17 requires its governing rule to appear at the SLOT 4 position, but
  neither requires the rule to communicate the readiness consequence of deferring the
  action. A `[RULE NEXT-CONCRETE]` that states "Run /scout:feasibility (scout). Leaving
  this open holds the topic at Not Ready." converts the next step from a navigation label
  into a commitment statement: the model encodes both the action and the inertia cost of
  not taking it. Round 5 finding: V-05 is the only R5 design to carry this framing; V-04
  names the skill without the stall cost, confirming the pattern is a real design
  distinction. Scored separately from C-05 because inertia framing (action + consequence)
  is structurally distinct from concreteness (action + no generic fallback).
- **C-22 (explicit THREE-LAYER WRITE POINT header present)** is aspirational -- C-18
  requires all three enforcement layers to converge at the write point structurally, but
  structural convergence and named convergence are distinct reliability properties. An
  explicit `=== THREE-LAYER WRITE POINT ===` header that enumerates LAYER 1 DECLARE /
  LAYER 2 ANCHOR / LAYER 3 VERIFY before the model encounters any enforcement layer
  creates a named recovery point: a model whose attention degrades mid-generation can
  re-read the header and reconstruct the expected layer sequence without searching the
  surrounding spec. Round 5 finding: V-02 and V-05 both carry this header; V-01, V-03,
  and V-04 achieve structural C-18 without it and score identically under binary
  layer-presence scoring. The explicit header is a reliability mechanism (lower live-run
  variance) not captured by C-18's binary pass condition. Scored separately from C-18
  because the mechanism (named checklist at the entry point) addresses attention recovery,
  a different failure mode from layer absence.
- **C-23 (criterion-tagged violation example in `[RULE]` annotation)** is aspirational --
  C-20 requires a correct/violation example pair within each `[RULE]` annotation, but does
  not require the violation example to name the criterion ID being violated. A violation
  example that states only the bad output pattern is contrast-demonstrative; a violation
  example that appends the criterion tag (e.g., "(no stall cost -- C-21 violation)") is
  criterion-recoverable: a model encountering the violation knows which invariant is at
  stake and can trace it back to the register and governing rule without a scan. Round 6
  finding: V-04 is the first design to carry this tag; the tagging pattern applies wherever
  C-20 is satisfied with a named invariant that has a rubric ID. Scored separately from
  C-20 because the mechanism (criterion ID embedded in violation text vs. contrast pair
  without ID) addresses a different failure mode: invariant traceability rather than format
  demonstration alone.
- **C-24 (contract label chaining for single-position output invariants)** is aspirational
  -- C-19 applies the register-to-annotation-to-scan-header chaining pattern to
  bidirectional list invariants. NEXT STEP phrasing is a single-position invariant: it
  constrains one output slot without a pre-computation phase or scan. Assigning a named
  register entry (e.g., G-9 INERTIA) and propagating that exact label to the inline
  `[RULE G-9 INERTIA]` annotation makes the invariant chain-traceable at two structural
  levels (register, annotation) without requiring a scan step, which is the correct
  structural treatment for single-position invariants. Round 6 finding: V-05 is the first
  design to apply C-19's chaining pattern to a single-position invariant; V-04 uses
  `[RULE NEXT-CONCRETE C-21]` which is locally correct but not register-linked. Scored
  separately from C-19 because the mechanism (two-level chaining without a scan step vs.
  three-level chaining through a scan step) is structurally appropriate to a different
  class of invariant.
- **C-25 (Branch B independent THREE-LAYER WRITE POINT header)** is aspirational -- C-22
  requires an explicit `=== THREE-LAYER WRITE POINT ===` header at the default execution
  path write point (SLOT 3), but does not require Branch B (`--format teams`) to carry its
  own equivalent header. A self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===`
  header within Branch B enumerates LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY
  independently, so a model in Branch B reconstructs the enforcement sequence without any
  cross-branch reference. Round 6 finding: V-05 is the only R6 design to carry a Branch B
  independent header. Scored separately from C-22 because the mechanism (branch-local
  recovery point vs. shared header) addresses a different failure mode: cross-branch
  attention loss on the `--format teams` path vs. mid-generation layer forgetting on the
  default path.
- **C-26 (dual-chain co-presence at governed annotation slot)** is aspirational -- C-23
  (criterion-tagged violation) and C-24 (register-linked label) each address different
  failure modes at the same structural position: C-23 makes the failure mode
  criterion-recoverable; C-24 makes the invariant register-recoverable. When both are
  co-present at the same `[RULE]` annotation, the annotation supports two independent
  recovery chains at one structural position without conflict. A spec satisfying C-23 alone
  or C-24 alone does not satisfy this criterion; both must be co-present at the same
  annotation position. Round 7 finding: V-04 and V-05 demonstrate co-presence without
  conflict; V-01 (C-23 only) and V-02 (C-24 only) isolate each chain. Scored separately
  from C-23 and C-24 because two independent recovery paths at one position is a composite
  property not implied by either criterion in isolation.
- **C-27 (dual-branch three-layer closure)** is aspirational -- C-22 (main-branch header)
  and C-25 (Branch B independent header) each close the attention-recovery gap for one
  execution path. When both are present the spec achieves complete dual-branch closure: no
  cross-branch lookup or cross-spec search is required at any point on either path. The
  property is conjunctive: either header alone leaves one execution path exposed. Round 7
  finding: V-05 is the only R7 design achieving dual-branch closure. Scored separately
  from C-22 and C-25 because complete dual-branch self-containment is a system-level
  property not implied by either header criterion in isolation.
- **C-28 (dual-identifier violation example)** is aspirational -- C-26 requires both the
  register-linked label (C-24) and the criterion-tagged violation (C-23) to be co-present
  at the same `[RULE]` annotation, creating two independent recovery chains accessible
  from the annotation slot. C-28 is a stronger property at the violation-text level: the
  violation example itself carries both the register label and the rubric criterion ID as a
  single compound fragment -- e.g., `(no stall cost -- G-9 INERTIA / C-21 violation)` --
  so that a model tracing from any bad output reaches both the contract register and the
  rubric invariant definition from one text fragment without needing to read the annotation
  label separately. C-26 guarantees co-presence at the annotation level (two chain
  endpoints); C-28 guarantees the violation fragment is itself dual-linked (one fragment,
  both chains reachable). C-28 requires C-26 as a precondition but is not implied by it.
  Round 8 finding: V-01 demonstrates the dual-identifier violation in isolation. Scored
  separately from C-26 because the mechanism (single fragment tracing to both chains vs.
  two separate chain endpoints at the annotation) addresses a different failure mode:
  split-attention during violation parsing vs. independent recovery path availability.
- **C-29 (explicit named recovery directive in Branch B header)** is aspirational -- C-25
  requires the Branch B header to enumerate LAYER 1/2/3 independently (structural
  self-containment without cross-branch reference). C-29 adds a meta-instruction layer: an
  explicit named recovery directive within the Branch B header that names both the recovery
  action and the prohibited alternative -- e.g., "re-read this BRANCH B header to
  reconstruct the required layer sequence without referencing BRANCH A" -- converting
  structural self-containment into a procedural instruction the model encounters at Branch
  B entry before encountering any enforcement layer. C-25 makes cross-branch lookup
  unnecessary; C-29 makes the recovery procedure explicit at the moment the model enters
  Branch B. C-29 requires C-25 as a precondition but is not implied by it; C-29 is
  orthogonal to C-28. Round 8 finding: V-02 carries the recovery directive in isolation.
  Scored separately from C-25 because the mechanism (named recovery action instruction vs.
  structural self-containment) addresses a different failure mode: attention-recovery after
  degradation vs. structural independence from Branch A.
- **C-30 (slot-indexed contract register)** is aspirational -- C-19 and C-24 both chain
  invariant labels backward from annotation positions to the contract register, enabling
  recovery from a degraded annotation. C-30 adds forward indexing: each register entry
  carries a slot annotation naming the output position it governs -- e.g.,
  `G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, `G-7b EXCLUSIVITY [SLOT 3]`,
  `G-1 [PHASE 4]` -- so that a model reading the register at the start of execution can
  navigate forward to the governed slot without searching the spec. C-30 is orthogonal to
  C-19 and C-24: C-19/C-24 chain labels backward (annotation to register); C-30 indexes
  labels forward (register to slot). Round 8 finding: V-03 is the first design to carry
  slot-indexed register entries. Scored separately from C-19 and C-24 because forward
  register-to-slot navigation addresses a different failure mode from backward
  annotation-to-register traceability.
- **C-31 (Branch B SLOT 4 complete attention-recovery envelope)** is aspirational -- C-28
  and C-29 both address Branch B reliability but at different failure points. C-29 fires at
  Branch B entry, covering entry-point context degradation before any enforcement layer is
  encountered. C-28 fires at SLOT 4 within Branch B, covering write-point traceability
  failure if the model generates a stall-cost-free next step. Their conjunction creates a
  complete attention-recovery envelope: no unrecovered failure mode exists on the Branch B
  SLOT 4 path. C-31 requires both C-28 and C-29 as preconditions (which themselves require
  C-26 and C-25). Round 9 finding: V-01 (A+B) is the minimal design satisfying C-31; V-04
  carries it alongside C-32 and C-33. Scored separately from C-28 and C-29 because
  no-unrecovered-failure-mode on a complete execution path is a system-level coverage
  property not implied by either entry-point recovery or violation-level dual-linking alone.
- **C-32 (register-to-violation closed traceability loop)** is aspirational -- C-30 and
  C-28 address traceability in opposite directions. C-30 indexes forward (register -> slot);
  C-28 embeds backward (violation fragment -> register label + rubric ID in one fragment).
  Their conjunction closes a bidirectional traceability loop: from any entry point in the
  enforcement chain -- the register, the template position, or a bad output -- a model
  reaches any other position without a spec-level search. C-32 requires both C-28 and C-30
  as preconditions. Round 9 finding: V-02 (A+C) is the minimal design satisfying C-32;
  V-04 carries it alongside C-31 and C-33. Scored separately from C-28 and C-30 because
  bidirectional loop closure (every enforcement position reachable from every other without
  spec search) is a connectivity property not implied by either forward indexing or backward
  dual-linking alone.
- **C-33 (Branch B forward-to-procedural navigation coordination)** is aspirational -- C-30
  and C-29 address Branch B navigation at two distinct temporal points. C-30 acts before
  Branch B entry (planning phase): the register's slot annotations establish the output
  slot map before any branch-specific context is encountered. C-29 acts at Branch B entry
  (recovery phase): the recovery directive names the recovery action and the prohibited
  alternative at the moment the model enters the branch. The coordination property: C-30
  makes C-29 more effective because the model already holds an internalized slot map when
  the recovery directive fires. C-33 requires both C-29 and C-30 as preconditions (which
  themselves require C-25 and the base register structure). Round 9 finding: V-03 (B+C) is
  the minimal design satisfying C-33; V-04 carries it alongside C-31 and C-32. Scored
  separately from C-29 and C-30 because temporal coordination across pre-entry and at-entry
  failure points is a sequencing property not implied by either the forward index or the
  procedural directive in isolation.
- **C-34 (explicit named recovery directive in main-branch header)** is aspirational --
  C-22 requires the main-branch header to enumerate all three enforcement layers as a named
  checklist (structural completeness), but does not require the header to state a recovery
  procedure. C-34 adds a named directive within the same header that tells the model how to
  use the header for recovery and which cross-branch contamination path to avoid -- e.g.,
  "re-read this BRANCH A header to reconstruct the required layer sequence without
  referencing the BRANCH B template." C-22 makes the layers recoverable; C-34 makes the
  recovery procedure explicit. C-34 is the main-branch structural analogue of C-29 applied
  to the default execution path rather than the teams path. C-34 requires C-22 as a
  precondition but is not implied by it; C-34 is orthogonal to C-35 and C-36. Round 10
  finding: V-01 (Axis A) is the minimal design satisfying C-34. Scored separately from
  C-22 because procedural recovery instruction vs. structural layer enumeration addresses
  a different failure mode: attention-recovery after degradation vs. layer forgetting
  without a named recovery path.
- **C-35 (branch-qualified slot indexing)** is aspirational -- C-30 requires each register
  entry to carry a slot annotation naming the output position it governs, creating a
  forward-navigation path from register to slot. When the same invariant governs equivalent
  positions on two execution paths (e.g., G-9 INERTIA governs SLOT 4 on both BRANCH A and
  BRANCH B), unqualified `[SLOT 4]` creates a forward path but leaves the model uncertain
  which execution path the annotation refers to. C-35 extends C-30 with branch
  qualification: separately qualified entries (e.g., `[SLOT 4 / BRANCH A]` and
  `[SLOT 4 / BRANCH B]`) provide branch-specific forward navigation with no cross-path
  ambiguity. A model following the BRANCH A register entry arrives at the BRANCH A write
  point unambiguously. C-35 requires C-30 as a precondition; C-35 is orthogonal to C-34
  and C-36. Round 10 finding: V-02 (Axis B) is the minimal design satisfying C-35. Scored
  separately from C-30 because branch-specific forward navigation is a stronger property
  than coarse slot indexing -- it eliminates cross-path ambiguity that C-30 alone cannot
  resolve.
- **C-36 (explicit temporal coordination statement)** is aspirational -- C-33 achieves
  temporal coordination between C-30 (planning phase) and C-29 (recovery phase) on the
  Branch B path by their structural co-presence, without naming the coordination as an
  invariant. C-36 extends this by requiring an explicit named declaration that identifies
  at least one planning-phase element and one recovery-phase element, states the
  directional dependency (the planning phase establishes context that makes the recovery
  phase more effective), and converts structural temporal ordering into a declared system
  property. V-03 (A+B in R10) achieves structural coordination of C-35 (branch-qualified
  map, planning phase) and C-34 (recovery directive, recovery phase) without satisfying
  C-36 because no coordination statement is present. V-04 (A+B+C in R10) adds the explicit
  coordination declaration, satisfying C-36. C-36 is orthogonal to C-34 and C-35: a spec
  can name the coordination between other elements (e.g., C-30 and C-29) or can satisfy
  C-34+C-35 without a coordination statement. Round 10 finding: V-04 (A+B+C) is the
  minimal design satisfying C-36; V-03 (A+B) is the minimal design demonstrating that
  structural coordination does not imply C-36. Scored separately from C-34 and C-35
  because explicit coordination declaration (named planning/recovery roles) is a
  meta-invariant property not implied by structural presence of either phase.
- **C-37 (main-branch SLOT 4 complete attention-recovery envelope)** is aspirational --
  C-34 and C-35 address the main-branch SLOT 4 path at different failure points. C-35
  covers planning confusion: branch-qualified register entries enable the model to navigate
  to the correct execution-path position from the register without ambiguity before
  encountering any branch-specific template content. C-34 covers write-point degradation:
  the named recovery directive fires at the C-22 header, which the model encounters before
  any enforcement layer. Their conjunction creates a complete attention-recovery envelope
  for the main-branch SLOT 4 path, mirroring C-31's Branch B SLOT 4 envelope. C-37
  requires both C-34 and C-35 as preconditions. Round 10 finding: V-03 (A+B) is the
  minimal design satisfying C-37; V-04 carries it alongside C-38 and C-39. Scored
  separately from C-34 and C-35 because system-level coverage (no unrecovered failure mode
  on the complete main-branch SLOT 4 path) is not implied by either planning disambiguation
  or write-point recovery alone.
- **C-38 (named recovery directive with declared temporal role)** is aspirational -- C-34
  makes the recovery directive procedurally explicit (the model knows what to do when it
  encounters the directive at the C-22 header). C-36 makes temporal coordination explicitly
  declared (the model knows that planning and recovery phases exist as a named system). When
  both are satisfied, the recovery directive is situated within a declared temporal
  structure: the model encounters not only the instruction but also an explicit statement
  that this instruction plays the recovery-phase role against a pre-established plan.
  Without C-36, C-34 is a standalone directive with no declared temporal context. With
  C-36, the directive is a named phase in a coordinated system. C-38 requires both C-34
  and C-36 as preconditions. Round 10 finding: V-04 (A+B+C) is the minimal design
  satisfying C-38 because V-03 satisfies C-34 and C-35 but not C-36. Scored separately
  from C-34 and C-36 because declared temporal role is a meta-structural situating
  property not implied by either the directive's procedural content or the coordination
  statement in isolation.
- **C-39 (branch-qualified forward map with declared planning role)** is aspirational --
  C-35 makes forward navigation branch-specific (no cross-path ambiguity). C-36 makes
  temporal coordination explicitly declared (a named planning phase and recovery phase
  exist as a system). When both are satisfied, the branch-qualified register is situated
  within a declared temporal structure: the model encounters not only a navigation map but
  also an explicit statement that this map plays the planning-phase role that the recovery
  directive fires against. Without C-36, C-35 is a better forward index with no declared
  temporal context. With C-36, the index is the named planning input of a coordinated
  system. C-39 requires both C-35 and C-36 as preconditions. Round 10 finding: V-04
  (A+B+C) is the minimal design satisfying C-39. Scored separately from C-35 and C-36
  because declared planning role is a meta-structural situating property not implied by
  either branch-qualified annotations or the coordination statement in isolation.
- **C-40 (criterion-tagged contamination consequence in main-branch recovery directive)**
  is aspirational -- C-34 names both the recovery action and the prohibited alternative
  within the main-branch header, converting structural layer enumeration into a procedural
  prohibition. C-40 adds a consequence-grounding layer: a named consequence line within the
  same directive that states the specific output failure mode the prohibited action produces
  -- e.g., "SLOT 3 contamination consequence: readiness sentence will cite Branch B format
  tokens instead of Branch A BLOCKERS-derived signal names." C-34 tells the model what not
  to do; C-40 tells the model what goes wrong if it does. Consequence-grounding converts an
  abstract prohibition into an outcome-aware instruction: the model encounters the failure
  mode at the moment it reads the directive, before generating any output. C-40 requires
  C-34 as a precondition but is not implied by it. C-40 is orthogonal to C-41 and C-42.
  Round 11 finding: V-01 (Axis D) is the minimal design satisfying C-40. Scored separately
  from C-34 because consequence visibility (named failure mode at write time) is
  structurally distinct from prohibition naming (named action at write time): one targets
  the outcome the model is avoiding; the other targets the instruction the model is
  following.
- **C-41 (format-type-qualified Branch B register entries)** is aspirational -- C-35
  extends C-30's unqualified slot indexing with branch qualification, so each register
  entry navigates to the correct branch-specific write point without cross-path ambiguity.
  C-41 extends Branch B register entries further with explicit format-type qualifiers that
  state the output format constraint for the governed slot -- e.g.,
  `G-9 INERTIA [SLOT 4 / BRANCH B] (one card row, no markdown)`. A model following the
  Branch B register path encounters the format requirement at register-read time, before any
  branch-specific template content is reached. C-35's branch qualification closes navigation
  ambiguity; C-41 closes format ambiguity on the Branch B path, making the register a
  complete pre-execution specification of both destination and format constraint for each
  Branch B write point. C-41 requires C-35 as a precondition but is not implied by it;
  C-41 applies specifically to Branch B entries (the non-default format path). C-41 is
  orthogonal to C-40 and C-42. Round 11 finding: V-02 (Axis E) is the minimal design
  satisfying C-41; the R11 V-02 design omits the named Branch A recovery directive (C-34
  fails) to isolate Axis E, confirming C-41 is achievable independently of C-34. Scored
  separately from C-35 because pre-write-point format constraint delivery (format
  requirement encountered at register-read time, before template entry) is a distinct
  reliability property from branch-qualified navigation (ambiguity-free path to the correct
  write point).
- **C-42 (temporal-role annotation embedded in contract register header)** is aspirational
  -- C-36 requires an explicit temporal coordination statement identifying planning and
  recovery phases and their directional dependency; this statement can appear anywhere in
  the spec. C-42 requires the temporal role to be co-located in the contract register
  header itself -- e.g., `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase --
  establishes slot map before execution begins] ===` -- so the model encounters the
  register's function in the temporal system at the moment it reads the register, before
  any slot navigation or branch-specific context is reached. The system property: the
  register is self-annotating as a planning-phase artifact; mid-execution, the model need
  not recall a separately located coordination statement to know the register's temporal
  role. C-42 requires C-36 as a precondition (the named coordination structure must exist
  before the header annotation can refer to it) but is not implied by it. A spec can
  satisfy C-36 with the coordination statement located in a preamble or footer without
  embedding the temporal role in the register header. C-42 is orthogonal to C-40 and C-41.
  Round 11 finding: V-04 (Axis F) is the minimal design satisfying C-42; V-03 (D+E)
  satisfies C-40+C-41 without C-42, confirming the register header temporal annotation is
  not implied by consequence-grounding or format-type qualification. Scored separately from
  C-36 because header-level temporal role co-location (role declaration encountered at
  first artifact read) eliminates a distinct failure mode -- mid-execution temporal role
  recall -- that coordination statement presence alone does not address.
- **C-43 (consequence-grounded contamination guard with format-navigable Branch B entries)**
  is aspirational -- C-40 and C-41 close independent failure modes at different structural
  positions: C-40 fires at the main-branch write point (consequence of cross-branch
  contamination visible before output is written); C-41 fires at register-read time (Branch
  B format constraint visible before any branch-specific template is entered). Their
  conjunction closes two failure modes simultaneously without overlap: no unresolved format
  ambiguity on the Branch B navigation path (C-41) and no un-consequenced contamination
  prohibition on the main-branch write path (C-40). C-43 requires both C-40 and C-41 as
  preconditions. Round 11 finding: V-03 (D+E) is the minimal design satisfying C-43; V-04
  carries it alongside C-44 and C-45. Scored separately from C-40 and C-41 because reduced
  total uncovered failure mode count across both execution paths is a system-level coverage
  property not implied by either consequence-grounding or format pre-delivery alone.
- **C-44 (contamination consequence with declared temporal context)** is aspirational --
  C-40 makes the contamination consequence visible at the main-branch write point. C-42
  makes the register's temporal planning role visible at register-read time. When both are
  satisfied, the contamination consequence is situated within a declared temporal system:
  the model knows at write time that the plan it is executing was established in a named
  planning phase (C-42 declared at register-read time), and that contaminating the write
  point with patterns from the other branch would produce a specific failure mode (C-40).
  The consequence is more actionable because the model has already internalized the register
  as a planning-phase artifact whose outputs form the contract the write point enforces;
  violating that contract has a named cost. Without C-42, C-40's consequence is a standalone
  warning without temporal context. With C-42, the consequence refers to a violation of a
  temporally coordinated plan. C-44 requires both C-40 and C-42 as preconditions. Round 11
  finding: V-04 (D+E+F) is the minimal design satisfying C-44. Scored separately from C-40
  and C-42 because temporally-situated consequence declaration is a meta-structural property
  not implied by either consequence-grounding or temporal-role co-location alone.
- **C-45 (format-type-qualified forward map with declared planning role in header)** is
  aspirational -- C-41 makes the Branch B register entries format-aware: each Branch B slot
  annotation carries its format-type constraint inline. C-42 makes the register header
  self-annotating with its temporal role: the model encounters the register as the planning
  phase of a coordinated enforcement system. When both are satisfied, the register is
  simultaneously a planning-phase artifact (declared at the header) and a format-constraint
  delivery vehicle (declared at each Branch B entry). The format-type qualifiers are entries
  in a named planning-phase document, reinforcing that the format constraints are
  plan-level commitments, not incidental annotations. The model encounters two reinforcing
  properties at the same structural artifact: the register's temporal function (C-42) and
  the concrete format obligations it establishes for Branch B (C-41). Without C-42, C-41
  provides a better-annotated register whose role is implicit. With C-42, the format-type
  qualifiers are part of a declared planning-phase document. C-45 requires both C-41 and
  C-42 as preconditions. Round 11 finding: V-04 (D+E+F) is the minimal design satisfying
  C-45. Scored separately from C-41 and C-42 because planning-phase format commitment
  (format constraints as entries in a named planning document) is a meta-structural
  situating property not implied by either format-type qualification or temporal-role
  co-location alone.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Artifact written and path echoed** | completeness | essential | Output includes a write instruction that lands the report at a deterministic path and echoes that path after write; artifact must exist on disk |
| C-02 | **Progress table present with accurate counts** | correctness | essential | Table with one row per namespace, total/complete/open columns, counts from actual discovered signals, includes a completion percentage or status symbol |
| C-03 | **Open signals listed with owners** | coverage | essential | Every incomplete signal enumerated with an owner field (even if "unassigned"); no open signal silently omitted |
| C-04 | **Readiness statement present and calibrated** | correctness | essential | Single sentence or labeled field states ready/not ready/conditionally ready; consistent with signal counts in the progress table |
| C-05 | **Recommended next step present** | depth | essential | Output concludes with one concrete next action; next step matches the most critical open signal |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **`--format teams` produces compact ASCII card** | format | recommended | Single ASCII block, all four sections, <= 40 lines and <= 80 chars wide |
| C-07 | **Content matches topic-status output** | correctness | recommended | Signal counts, readiness state, and next step identical to `topic-status` for the same topic at the same point in time |
| C-08 | **Open signals include signal type and namespace** | coverage | recommended | Each open signal entry names both namespace and signal type, not just a freeform description |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Readiness statement references blocking signals** | depth | aspirational | Readiness statement names the specific signals that are blocking (e.g., "Not ready -- missing prove-analysis and review-design") rather than a generic message |
| C-10 | **Teams card prohibition is explicitly enumerated** | format | aspirational | The spec explicitly prohibits backtick characters, angle brackets (`<`, `>`), and markdown emphasis markers *by name* -- not satisfied by a catch-all phrase such as "no markdown syntax" |
| C-11 | **Output includes BLOCKERS pre-computation block** | depth | aspirational | Before the readiness statement, the output contains an explicit enumeration of essential OPEN signals (a BLOCKERS block); the readiness sentence references signal-type names drawn from that block and cannot introduce new names or omit names present in the block |
| C-12 | **Teams card passes character-level scan** | format | aspirational | Independent of C-10's specification check, the `--format teams` output contains zero backtick characters and zero angle-bracket characters when scanned character by character |
| C-13 | **Bidirectionality stated as two named invariants** | depth | aspirational | The BLOCKERS constraint is expressed as two separately named sub-rules -- COMPLETENESS (the readiness sentence must cite every name in the BLOCKERS block) and EXCLUSIVITY (the readiness sentence must not introduce any name absent from the BLOCKERS block) -- each verifiable independently; compound phrasing such as "every name ... and only names" does not satisfy this criterion |
| C-14 | **Branch sealing instruction present** | format | aspirational | The spec contains an explicit directive that separates the default and `--format teams` rendering paths -- e.g., "the branches are sealed; do not reference the other branch's format descriptions when executing" -- so that format patterns cannot bleed across branches even when a model processes both in a single pass; explicit character prohibition (C-10) alone does not satisfy this criterion |
| C-15 | **BLOCKERS LOCK directive present** | depth | aspirational | The spec contains a standalone named directive that explicitly freezes the BLOCKERS list after its pre-computation step -- e.g., "The BLOCKERS list is now frozen. No additions, removals, or revisions are permitted in subsequent phases." -- making list immutability a first-class obligation distinct from the COMPLETENESS/EXCLUSIVITY bidirectionality rules (C-13); the embedded clause "this list is closed" within the pre-computation step does not satisfy this criterion because it does not name the directive or assert it as a phase-spanning constraint |
| C-16 | **In-render verification scan present** | depth | aspirational | The spec instructs the model to execute an explicit two-step compliance scan *before* writing the readiness sentence: (1) COMPLETENESS CHECK -- enumerate every name in the BLOCKERS list and confirm each appears in the draft sentence; (2) EXCLUSIVITY CHECK -- enumerate every name in the draft sentence and confirm each appears in the BLOCKERS list; declarative statements of COMPLETENESS/EXCLUSIVITY (C-13) alone do not satisfy this criterion because they do not require active verification at generation time |
| C-17 | **Rules co-located with governed template positions** | format | aspirational | Constraint rules are embedded as inline markers (e.g., `[RULE ...]`) at the exact template position they govern -- not collected in a separate preamble or appendix -- so that zero mapping distance exists between each rule and the output slot it constrains; branch isolation achieved by two independently placed seal markers (one at the branch dispatch point, one at the Branch B entry point) rather than a single preamble directive; C-14's sealed-branch requirement and C-17's co-location requirement are independent: a spec can satisfy either without satisfying the other |
| C-18 | **Three-layer co-location at the write point** | depth | aspirational | At the readiness sentence write point (SLOT 3 and its `--format teams` equivalent), all three enforcement layers converge at the same structural position: (1) `[RULE]` annotation declares the COMPLETENESS/EXCLUSIVITY constraint; (2) an explicit reference to the LOCKED BLOCKERS list anchors list immutability at that position; (3) the in-render verification scan (C-16) executes immediately before writing -- so no cross-phase recall is required for any enforcement layer at the moment of generation; satisfying C-15, C-16, and C-17 independently does not satisfy this criterion if the LOCK anchor is absent at the write point itself |
| C-19 | **Contract label chaining from register to annotation to scan header** | depth | aspirational | Invariant names are assigned at a top-of-specification contract register (e.g., G-7a COMPLETENESS, G-7b EXCLUSIVITY) and those exact labels are propagated to the inline `[RULE G-7a/G-7b]` annotations at governed template positions and to the scan step headers (e.g., "G-7a COMPLETENESS SCAN") -- making the invariant independently recoverable at three structural levels (register, annotation, scan header) without any cross-position lookup; generic annotation labels such as `[RULE COMPLETENESS]` that are not linked to a named contract register entry do not satisfy this criterion |
| C-20 | **Worked example embedded within each `[RULE]` annotation** | format | aspirational | Each inline `[RULE]` annotation governing output phrasing (readiness sentence, next step) includes a compact correct/violation example immediately after the rule statement at the same position -- so that the model encounters both the constraint declaration and a sample output format at the governed slot; a worked example collected in a separate section or preamble does not satisfy this criterion; structural-format rules (table borders, character counts) are exempt |
| C-21 | **Inertia framing at NEXT STEP** | depth | aspirational | The `[RULE]` annotation governing the recommended next step names both the concrete action *and* the readiness consequence of deferring it -- e.g., "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready." -- converting the next step from a navigation label into a commitment statement; a rule that names only the skill or action without a stall-cost statement does not satisfy this criterion; C-05's concreteness requirement is necessary but not sufficient |
| C-22 | **Explicit THREE-LAYER WRITE POINT header present** | format | aspirational | The spec contains an explicit named header at the readiness write point (e.g., `=== THREE-LAYER WRITE POINT ===`) that enumerates all three enforcement layers -- LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY -- before the model encounters any of them, creating a named checklist that enables attention recovery mid-generation without a cross-spec search; structural C-18 (all three layers present without explicit labeling) does not satisfy this criterion; the header must appear at the write point itself, not in a preamble |
| C-23 | **Criterion-tagged violation example in `[RULE]` annotation** | format | aspirational | Within each `[RULE]` annotation that carries a correct/violation example pair (C-20), the violation example explicitly names the criterion ID being violated -- e.g., "(no stall cost -- C-21 violation)" -- making the failure mode criterion-traceable rather than only contrast-demonstrative; a violation example that shows an incorrect output pattern without naming the criterion ID does not satisfy this criterion even if it satisfies C-20; C-23 requires C-20 as a precondition but is not implied by it |
| C-24 | **Contract label chaining for single-position output invariants** | depth | aspirational | Single-position output invariants -- those that constrain one output slot without a pre-computation block or bidirectional scan (e.g., NEXT STEP phrasing) -- are assigned named register entries (e.g., G-9 INERTIA) at the top-of-specification contract register, and those exact labels are propagated to the inline `[RULE G-9 INERTIA]` annotation at the governed slot, making the invariant chain-traceable at two structural levels (register, annotation) without requiring a scan step; a `[RULE]` annotation whose label is not linked to a named register entry does not satisfy this criterion; C-19 covers bidirectional list invariants; C-24 covers single-position invariants; both can be present independently |
| C-25 | **Branch B independent THREE-LAYER WRITE POINT header** | format | aspirational | The `--format teams` execution path contains its own self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header that enumerates LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY independently of the main-branch C-22 header, so that a model executing Branch B reconstructs the enforcement layer sequence without any cross-branch lookup; the main-branch C-22 header alone does not satisfy this criterion; the Branch B header must appear within Branch B itself, not in a shared preamble |
| C-26 | **Dual-chain co-presence at governed annotation slot** | depth | aspirational | Within the same `[RULE]` annotation, both C-23 (criterion-tagged violation) and C-24 (register-linked label) are satisfied simultaneously: the annotation label carries the register name (e.g., `[RULE G-9 INERTIA]`) providing the register-recovery path, while the violation example appends the rubric criterion ID (e.g., `(no stall cost -- C-21 violation)`) providing the rubric-recovery path -- creating two independent recovery chains at one structural position without conflict; satisfying C-23 alone or C-24 alone does not satisfy this criterion; C-26 requires both C-23 and C-24 as preconditions at the same annotation position |
| C-27 | **Dual-branch three-layer closure** | format | aspirational | Both C-22 (main-branch `=== THREE-LAYER WRITE POINT ===` header) and C-25 (Branch B `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header) are present, so that neither execution path requires cross-branch lookup or cross-spec search to reconstruct the enforcement layer sequence; the property is conjunctive -- either header alone leaves one execution path exposed; C-27 requires both C-22 and C-25 as preconditions |
| C-28 | **Dual-identifier violation example** | depth | aspirational | Within the `[RULE]` annotation at SLOT 4 (NEXT STEP), the violation example carries both the contract register label and the rubric criterion ID as a single compound fragment -- e.g., `(no stall cost -- G-9 INERTIA / C-21 violation)` -- so that a model tracing from any bad next-step output reaches both the register obligation and the rubric invariant definition from one text fragment without splitting attention between the annotation label and the violation text; a violation example that carries only one identifier does not satisfy this criterion; C-28 requires C-26 as a precondition but is not implied by it |
| C-29 | **Explicit named recovery directive in Branch B header** | format | aspirational | Within the Branch B `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header (C-25), an explicit named recovery directive names both the recovery action and the prohibited alternative -- e.g., "re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A" -- converting structural self-containment into a procedural instruction the model encounters at Branch B entry before any enforcement layer; a Branch B header that enumerates LAYER 1/2/3 without a named recovery directive does not satisfy this criterion; C-29 requires C-25 as a precondition but is not implied by it; C-29 is orthogonal to C-28 |
| C-30 | **Slot-indexed contract register** | depth | aspirational | Each entry in the top-of-specification contract register carries an annotation naming the output position it governs -- e.g., `G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, `G-7b EXCLUSIVITY [SLOT 3]`, `G-1 [PHASE 4]` -- creating a forward-navigation path from register to governed template position without requiring a spec search; a register that assigns named labels without slot annotations does not satisfy this criterion; C-30 is orthogonal to C-19 and C-24: C-19/C-24 chain labels backward (annotation to register); C-30 indexes labels forward (register to slot) |
| C-31 | **Branch B SLOT 4 complete attention-recovery envelope** | depth | aspirational | Both C-28 (dual-identifier violation at SLOT 4) and C-29 (named recovery directive in Branch B header) are satisfied simultaneously, creating a complete attention-recovery envelope for the Branch B SLOT 4 path: C-29 fires at Branch B entry before any enforcement layer (covers entry-point context degradation); C-28 fires at SLOT 4 if the model writes a stall-cost-free next step (covers write-point traceability failure); no unrecovered failure mode exists on the Branch B SLOT 4 path; satisfying C-28 alone or C-29 alone does not satisfy this criterion because each covers a different failure point on the same execution path; C-31 requires both C-28 and C-29 as preconditions |
| C-32 | **Register-to-violation closed traceability loop** | depth | aspirational | Both C-28 (dual-identifier violation at SLOT 4) and C-30 (slot-indexed contract register) are satisfied simultaneously, closing a bidirectional traceability loop: C-30 enables forward navigation (register -> slot annotation -> governed position); C-28 enables backward traceability (violation fragment -> register label + rubric criterion ID in one fragment); from any entry point in the enforcement chain -- the register, the template position, or a bad output -- a model reaches any other position without a spec-level search; satisfying C-28 alone or C-30 alone does not satisfy this criterion because each provides only one direction of the loop; C-32 requires both C-28 and C-30 as preconditions |
| C-33 | **Branch B forward-to-procedural navigation coordination** | depth | aspirational | Both C-29 (named recovery directive in Branch B header) and C-30 (slot-indexed contract register) are satisfied simultaneously, providing temporal coordination across two failure points: C-30 establishes the output slot map before Branch B entry (planning phase -- model internalizes slot positions from the register before encountering any branch-specific context); C-29 provides a named recovery instruction at Branch B entry (recovery phase -- model encounters the directive after the slot map is already internalized, making recovery more effective against a pre-established layout); satisfying C-29 alone or C-30 alone does not satisfy this criterion because each addresses a different temporal point on the Branch B path; C-33 requires both C-29 and C-30 as preconditions |
| C-34 | **Explicit named recovery directive in main-branch header** | format | aspirational | Within the main-branch `=== THREE-LAYER WRITE POINT ===` header (C-22), an explicit named recovery directive names both the recovery action and the prohibited alternative -- e.g., "re-read this BRANCH A header to reconstruct the required layer sequence without referencing the BRANCH B template" -- converting structural layer enumeration into a procedural instruction the model encounters at the main-branch write point before any enforcement layer; a main-branch header that enumerates LAYER 1/2/3 without a named recovery directive does not satisfy this criterion; C-34 requires C-22 as a precondition but is not implied by it; C-34 is the main-branch structural analogue of C-29 and is orthogonal to C-35 and C-36 |
| C-35 | **Branch-qualified slot indexing** | depth | aspirational | Each contract register entry that governs a position present on multiple execution paths carries a branch-qualified slot annotation -- e.g., `G-9 INERTIA [SLOT 4 / BRANCH A]` and `G-9 INERTIA [SLOT 4 / BRANCH B]` as separately qualified entries, `G-7a COMPLETENESS [SLOT 3 / BRANCH A]` -- distinguishing which execution path each entry governs and enabling branch-specific forward navigation without cross-path ambiguity; C-30's unqualified slot indexing (e.g., `[SLOT 4]`) does not satisfy this criterion because it leaves cross-path ambiguity unresolved; C-35 requires C-30 as a precondition but is not implied by it; C-35 is orthogonal to C-34 and C-36 |
| C-36 | **Explicit temporal coordination statement** | depth | aspirational | The spec contains a named declaration that explicitly identifies a planning phase (an element establishing a slot map or context before branch-specific execution begins) and a recovery phase (an element firing a directive at a write point against that pre-established map) and states the directional dependency between them -- e.g., "TEMPORAL COORDINATION: C-35 branch-qualified register establishes the slot map before execution (planning phase); C-34 recovery directive fires at the write point against that pre-established map (recovery phase)" -- converting structural temporal ordering into a declared system property; structural co-presence of a slot-indexed register and a header-embedded directive (C-30 + C-22) does not satisfy this criterion; the coordination must be explicitly named; C-36 is orthogonal to C-34 and C-35 |
| C-37 | **Main-branch SLOT 4 complete attention-recovery envelope** | depth | aspirational | Both C-34 (named recovery directive in main-branch header) and C-35 (branch-qualified slot indexing) are satisfied simultaneously, creating a complete attention-recovery envelope for the main-branch SLOT 4 path: C-35 covers planning confusion (branch-qualified forward navigation eliminates cross-path ambiguity before execution enters the template); C-34 covers write-point degradation (named recovery directive fires at the C-22 header before any enforcement layer); no unrecovered failure mode exists on the main-branch SLOT 4 path; satisfying C-34 alone or C-35 alone does not satisfy this criterion because each covers a different failure point; C-37 requires both C-34 and C-35 as preconditions; C-37 is the main-branch analogue of C-31 |
| C-38 | **Named recovery directive with declared temporal role** | depth | aspirational | Both C-34 (named recovery directive in main-branch header) and C-36 (explicit temporal coordination statement) are satisfied simultaneously, situating the recovery directive within a declared temporal structure: C-36 identifies the recovery directive as the recovery phase of a coordinated system; C-34 provides the directive itself; the model encounters not only the procedural instruction but also an explicit declaration of its temporal role before reaching the write point; satisfying C-34 alone leaves the directive without a declared temporal context; satisfying C-36 alone names the coordination without providing the directive; C-38 requires both C-34 and C-36 as preconditions |
| C-39 | **Branch-qualified forward map with declared planning role** | depth | aspirational | Both C-35 (branch-qualified slot indexing) and C-36 (explicit temporal coordination statement) are satisfied simultaneously, situating the branch-qualified register within a declared temporal structure: C-36 identifies the branch-qualified register as the planning phase of a coordinated system; C-35 provides the branch-specific forward map; the model encounters not only a navigation map but also an explicit declaration of its temporal role (the plan that the recovery-phase directive fires against); satisfying C-35 alone leaves the forward map without a declared temporal context; satisfying C-36 alone names the coordination without providing the branch-qualified map; C-39 requires both C-35 and C-36 as preconditions |
| C-40 | **Criterion-tagged contamination consequence in main-branch recovery directive** | format | aspirational | Within the C-34 recovery directive (or co-located with it in the main-branch header), an explicit named consequence line states the specific output failure mode produced by the prohibited cross-branch action -- e.g., "SLOT 3 contamination consequence: readiness sentence will cite Branch B format tokens instead of Branch A BLOCKERS-derived signal names" -- grounding the prohibition in a named outcome rather than only a named action; a recovery directive that names the prohibited alternative (C-34) without naming the resulting failure mode does not satisfy this criterion; C-40 requires C-34 as a precondition but is not implied by it; C-40 is orthogonal to C-41 and C-42 |
| C-41 | **Format-type-qualified Branch B register entries** | depth | aspirational | Each contract register entry governing a Branch B slot carries an explicit format-type qualifier appended to the branch-qualified slot annotation -- e.g., `G-9 INERTIA [SLOT 4 / BRANCH B] (one card row, no markdown)`, `G-7b EXCLUSIVITY [SLOT 3 / BRANCH B] (two card rows, no markdown)` -- making the output format constraint for each Branch B write point available at register-read time, before any branch-specific template content is encountered; a Branch B register entry that carries branch qualification (C-35) without a format-type qualifier does not satisfy this criterion; C-41 requires C-35 as a precondition but is not implied by it; C-41 applies to Branch B entries only; C-41 is orthogonal to C-40 and C-42 |
| C-42 | **Temporal-role annotation embedded in contract register header** | depth | aspirational | The contract register section header carries an explicit temporal-role annotation declaring the register's function in the enforcement system's planning/recovery structure -- e.g., `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- establishes slot map before execution begins] ===` -- so that the model encounters the register's temporal role at the moment it reads the register, before any slot navigation or branch-specific context is reached; a temporal coordination statement (C-36) located elsewhere in the spec does not satisfy this criterion; the annotation must appear in the register header itself; C-42 requires C-36 as a precondition but is not implied by it; C-42 is orthogonal to C-40 and C-41 |
| C-43 | **Consequence-grounded contamination guard with format-navigable Branch B entries** | depth | aspirational | Both C-40 (contamination consequence in main-branch recovery directive) and C-41 (format-type-qualified Branch B register entries) are satisfied simultaneously, closing two independent failure modes without overlap: C-40 makes the cost of cross-branch contamination visible at the main-branch write point; C-41 makes the Branch B format constraint visible at register-read time before any branch-specific template is entered; satisfying C-40 alone or C-41 alone does not satisfy this criterion; C-43 requires both C-40 and C-41 as preconditions |
| C-44 | **Contamination consequence with declared temporal context** | depth | aspirational | Both C-40 (contamination consequence in main-branch recovery directive) and C-42 (temporal-role annotation in register header) are satisfied simultaneously, situating the contamination consequence within a declared temporal system: C-42 declares the register's planning-phase role at register-read time; C-40 declares the specific failure mode at write time; the model encounters the consequence of contaminating a temporally coordinated plan, not merely the consequence of a standalone prohibition; satisfying C-40 alone or C-42 alone does not satisfy this criterion; C-44 requires both C-40 and C-42 as preconditions |
| C-45 | **Format-type-qualified forward map with declared planning role in header** | depth | aspirational | Both C-41 (format-type-qualified Branch B register entries) and C-42 (temporal-role annotation in register header) are satisfied simultaneously: C-42 declares the register's planning-phase temporal role at the header level; C-41 declares the output format constraint for each Branch B slot at the entry level; the register is both a named planning-phase artifact (header declaration) and a format-constraint delivery vehicle (entry-level qualifiers); satisfying C-41 alone or C-42 alone does not satisfy this criterion; C-45 requires both C-41 and C-42 as preconditions |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-45 that pass   (max 37)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/37 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

**Notes**:
- Aspirational criteria are independent -- any combination can pass.
- C-15 (LOCK) and C-16 (scan) both address list integrity but via different mechanisms:
  C-15 guards against mutation between steps; C-16 guards against omission or injection
  at write time. A spec can include either without the other.
- C-17 (co-location) and C-14 (sealing) are orthogonal format properties.
  Co-location concerns rule-to-slot distance; sealing concerns branch-to-branch
  contamination. Both can be present, absent, or mixed independently.
- C-18 (three-layer co-location) requires C-15, C-16, and C-17 all to be satisfied *and*
  the LOCK anchor to appear at the write point itself -- not merely at the phase level.
  V-03 (scan + inline, no LOCK) demonstrates that C-16 + C-17 without a write-point
  LOCK anchor does not satisfy C-18.
- C-19 (contract label chaining) requires a named contract register -- a structurally
  distinct section before execution begins that assigns canonical label names to each
  invariant. Generic inline labels that happen to be consistent across positions satisfy
  C-17 but not C-19. C-19 applies to bidirectional list invariants (three-level chain:
  register, annotation, scan header). C-24 applies to single-position invariants
  (two-level chain: register, annotation). Both can be present independently.
- C-20 (worked examples) is orthogonal to C-17, C-18, and C-19 -- a spec can embed
  examples without co-location, or co-locate rules without examples.
- C-21 (inertia framing) is orthogonal to C-05 -- C-05 tests that the next step is
  concrete (not "gather more signals"); C-21 tests that the rule governing the next step
  also states the stall cost of deferral.
- C-22 (explicit header) is a reliability extension of C-18, not a replacement. A spec
  that passes C-22 necessarily passes C-18 (all three layers must be present to name them),
  but C-18 does not imply C-22 (structural convergence without naming).
- C-23 (criterion-tagged violation) requires C-20 as a precondition -- a spec cannot carry
  a criterion-tagged violation without first carrying a violation example. C-23 is not
  implied by C-20: any spec satisfying C-20 with an untagged violation passes C-20 only.
- C-24 (single-position invariant chaining) is orthogonal to C-19 -- C-19 requires a
  pre-computation block and scan step as the third chain level; C-24 applies to invariants
  without those structures. A spec can satisfy C-19 without C-24 or C-24 without C-19.
- C-25 (Branch B independent header) is a reliability extension of C-22, not a
  replacement. C-22 and C-25 together close the attention-recovery gap for both execution
  paths independently.
- C-26 (dual-chain co-presence) requires C-23 and C-24 as preconditions. Both must be
  co-present at the *same* annotation position -- satisfying C-23 at one slot and C-24 at
  a different slot does not satisfy C-26.
- C-27 (dual-branch closure) requires C-22 and C-25 as preconditions. The property is
  system-level: it describes the absence of any cross-branch dependency across all
  execution paths, not merely the presence of two headers.
- C-28 (dual-identifier violation) requires C-26 as a precondition. C-28 is not implied
  by C-26: any spec satisfying C-26 may carry a violation example with only one identifier.
  Round 8 finding: V-01 demonstrates C-28 in isolation (Axis A); V-04/V-05 carry it
  alongside C-29.
- C-29 (Branch B recovery directive) requires C-25 as a precondition. C-29 is not implied
  by C-25. C-29 is orthogonal to C-28: neither implies the other. Round 8 finding: V-02
  demonstrates C-29 in isolation (Axis B); V-04/V-05 carry it alongside C-28.
- C-30 (slot-indexed register) is orthogonal to C-19 and C-24. Round 8 finding: V-03
  demonstrates C-30 in isolation (Axis C); V-05 carries all three axes.
- C-31 (Branch B SLOT 4 envelope) requires C-28 and C-29 as preconditions. The conjunctive
  property (no unrecovered failure mode on Branch B SLOT 4 path) is only achieved when both
  are present. Round 9 finding: V-01 (A+B) demonstrates C-31 in isolation; V-04 carries
  it alongside C-32 and C-33.
- C-32 (closed traceability loop) requires C-28 and C-30 as preconditions. Either
  direction alone leaves the loop open. Round 9 finding: V-02 (A+C) demonstrates C-32 in
  isolation; V-04 carries it alongside C-31 and C-33.
- C-33 (Branch B forward-to-procedural coordination) requires C-29 and C-30 as
  preconditions. Either temporal phase alone leaves the other failure point uncovered.
  Round 9 finding: V-03 (B+C) demonstrates C-33 in isolation; V-04 carries it alongside
  C-31 and C-32.
- C-31, C-32, and C-33 are inherently symmetric composites: each pairwise variation
  (V-01, V-02, V-03 in R9) satisfies exactly one of the three composites. The triple
  (R9 V-04) satisfies all three. No v10 criterion differentiates pairwise variations.
- C-34 (main-branch recovery directive) requires C-22 as a precondition. C-34 is the
  main-branch structural analogue of C-29. C-34 is orthogonal to C-35 and C-36. Round 10
  finding: V-01 (Axis A) demonstrates C-34 in isolation.
- C-35 (branch-qualified slot indexing) requires C-30 as a precondition. C-35 extends
  C-30's unqualified indexing with branch-specific qualification. C-35 is orthogonal to
  C-34 and C-36. Round 10 finding: V-02 (Axis B) demonstrates C-35 in isolation.
- C-36 (explicit temporal coordination statement) is orthogonal to C-34 and C-35. Round 10
  finding: V-04 (A+B+C) is the minimal design satisfying C-36; V-03 (A+B) demonstrates
  that structural coordination of C-34+C-35 does not imply C-36.
- C-37 (main-branch SLOT 4 envelope) requires C-34 and C-35 as preconditions. The
  conjunctive property (no unrecovered failure mode on the main-branch SLOT 4 path)
  mirrors C-31's Branch B SLOT 4 envelope. Round 10 finding: V-03 (A+B) demonstrates
  C-37 in isolation; V-04 carries it alongside C-38 and C-39.
- C-38 (named recovery directive with declared temporal role) requires C-34 and C-36 as
  preconditions. Neither the directive alone (C-34) nor the coordination statement alone
  (C-36) situates the directive within a declared temporal system. Round 10 finding: V-04
  (A+B+C) is the minimal design satisfying C-38.
- C-39 (branch-qualified forward map with declared planning role) requires C-35 and C-36
  as preconditions. Neither the forward map alone (C-35) nor the coordination statement
  alone (C-36) situates the map within a declared temporal system. Round 10 finding: V-04
  (A+B+C) is the minimal design satisfying C-39.
- C-37, C-38, and C-39 are inherently asymmetric composites under v11: V-03 (A+B in R10)
  satisfies C-37 but not C-38 or C-39; V-01 (A only) and V-02 (B only) satisfy no
  composite. The single-axis tie at V-01=V-02 (26/31) is structurally preserved: neither
  C-38 (requires C-34+C-36) nor C-39 (requires C-35+C-36) is achievable without C-36.
- C-40 (contamination consequence) requires C-34 as a precondition. C-40 is orthogonal to
  C-41 and C-42. Round 11 finding: V-01 (Axis D) demonstrates C-40 in isolation.
- C-41 (format-type-qualified Branch B entries) requires C-35 as a precondition. C-41
  applies to Branch B entries only; Main-branch (Branch A) entries are not in scope.
  C-41 is orthogonal to C-40 and C-42. Round 11 finding: V-02 (Axis E) demonstrates C-41
  in isolation; V-02 omits C-34 to isolate Axis E, so C-41 is confirmed independent of
  C-34.
- C-42 (temporal-role annotation in register header) requires C-36 as a precondition. C-42
  is orthogonal to C-40 and C-41. Round 11 finding: V-04 (Axis F) is the minimal design
  satisfying C-42; V-03 (D+E) satisfies C-40+C-41 without C-42.
- C-43 (consequence-grounded guard + format-navigable Branch B) requires C-40 and C-41 as
  preconditions. Round 11 finding: V-03 (D+E) demonstrates C-43 in isolation; V-04 carries
  it alongside C-44 and C-45.
- C-44 (contamination consequence with temporal context) requires C-40 and C-42 as
  preconditions. Round 11 finding: V-04 (D+E+F) is the minimal design satisfying C-44.
- C-45 (format-type-qualified map with header planning role) requires C-41 and C-42 as
  preconditions. Round 11 finding: V-04 (D+E+F) is the minimal design satisfying C-45.
- C-43, C-44, and C-45 are asymmetric under v12: V-03 (D+E) satisfies C-43 but not C-44
  or C-45. V-01 (D only) and V-02 (E only) satisfy no composite. The structural tie
  V-01=V-02 from R10 is broken under v12: V-01 scores 32/37 (31 v11 criteria + C-40);
  V-02 scores 31/37 (30 v11 criteria because C-34 fails + C-41). A new structural tie
  forms at V-02=V-05 (31/37): V-05 holds all v11 criteria with no new axes; V-02 trades
  C-34 for C-41. R12 discriminators must break V-05 from V-02.

---

## R12 Discriminator Candidates

| ID | Design question | V-isolation needed |
|----|-----------------|-------------------|
| C-46 candidate: Consequence-tagged contamination consequence | C-40 names the failure mode at the write point. Does adding a criterion tag to the consequence line (e.g., "SLOT 3 contamination consequence [C-40]: ...") make the consequence criterion-recoverable in the same way C-23 makes violation examples criterion-recoverable, creating a three-level contamination-traceability chain (register prohibition -> named consequence -> criterion tag)? C-46 would require C-40 as a precondition. | V-A: C-40 only (consequence named, no criterion tag); V-B: C-40 + criterion tag; measure contamination-traceability recovery rate |
| C-47 candidate: Main-branch format-type-qualified register entries | C-41 qualifies Branch B register entries with format-type constraints. Does applying equivalent format-type qualifiers to Branch A entries (e.g., `G-9 INERTIA [SLOT 4 / BRANCH A] (one next-step line, prose)`) symmetrically close the format-ambiguity gap on the default execution path, creating a global format-pre-delivery property across both branches? C-47 would require C-41 as a precondition. | V-C: C-41 only (Branch B entries qualified, Branch A unqualified); V-D: C-41 + Branch A qualifiers; measure format-ambiguity error rate on main branch vs. Branch B independently |
| C-48 candidate: V-02 vs. V-05 discriminator | V-02 (E only) and V-05 (neutral) tie at 31/37 under v12 via different paths: V-05 holds all 31 v11 criteria; V-02 trades C-34 for C-41. What property is satisfied by C-41 without C-34 that V-05 does not satisfy, or by C-34 without C-41 that V-02 does not satisfy? Candidate: the absence of C-34 in V-02 means V-02 has no main-branch recovery directive; V-05 has C-34 but no format-type qualifiers on Branch B entries. A criterion requiring both C-34 and C-41 simultaneously (a D+E composite under v11 labeling but an A-axis / E-axis composite) would distinguish both from V-03 and from each other. This is structurally equivalent to C-43 but applied to the A-axis + E-axis pair (C-34 + C-41) rather than D+E (C-40 + C-41). If C-34+C-41 has a measurable joint property distinct from either alone, it would break V-02=V-05 by requiring C-34 (which V-02 lacks). | V-E: C-34 + C-41 (no C-40); V-02: C-41 only (no C-34); V-05: C-34 only (no C-41); measure joint reliability of main-branch recovery + Branch B format pre-delivery |
