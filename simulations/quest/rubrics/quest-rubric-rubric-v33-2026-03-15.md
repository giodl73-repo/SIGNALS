## quest-rubric rubric v17 -- complete

### Changes from v16

One new aspirational criterion (C-47) extracted from Round 17 excellence signals.
Denominator /38 -> /39. Round 17 ceiling: V-05 R17 passes 37/39 criteria -> 37/39 x 10 = 9.49,
composite 99.49. Path to 100 under v17: C-39 must be satisfied (competitor at verification
step -- Tier-Blind Categorizer pattern at Phase 4.5 divergence-check step).

| # | Name | Evidence |
|---|------|----------|
| **C-47** | `anchor-successor-role-named` | V-05 R17 (stable across V-03 and V-04) -- REFERENCE ANCHOR Consumer field names ROLE: MECHANISM DEFINER as the blocked consumer; the anchor block declares which role depends on anchor satisfaction, making the anchor dependency forward-visible from the anchor definition alone, without reading the Mechanism Definer's entry precondition; closes the declaration direction of the bidirectional anchor dependency (anchor -> consumer: push reference), complementing C-45's enforcement direction (anchor STOP blocks Mechanism Definer entry: enforcement -> consumer) and mirroring C-46's treatment of the gate layer (gate names its successor) |

**Denominator:** `/38` -> `/39`

**New ceiling math:** V-05 R17 passes all 37 criteria carried from R15 (C-09--C-37 plus
C-40--C-47 = 37, with C-38 FAIL and C-39 FAIL persisting). Under v17 (/39): 37/39 x 10 = 9.487
aspirational, composite 99.487 (rounds to 99.49). C-38 FAIL traces to C-37 not being novel in
R17 (introduced in a prior round; C-38 is N/A when C-37 is not the current round's novel
criterion). C-39 FAIL persists: no variation places a competitor inline at the category-
distribution verification step (Tier-Blind Categorizer pattern at Phase 4.5). C-47 is stable
across three structural contexts (V-03 isolates anchor naming with C-46 ablated; V-04 combines
with prospective gate ordering with C-46 absent; V-05 full stack), confirming structural
orthogonality to C-41, C-45, and C-46.

**Structural axis extended:**

- C-11 + C-45 + C-47: C-11 requires the REFERENCE ANCHOR block to exist and name the Reference /
  Passes / Falls-short structure; C-45 requires a STOP that enforces anchor completeness at the
  Mechanism Definer entry boundary; C-47 requires the anchor block to name the specific consumer
  role that depends on anchor satisfaction. The three-criterion anchor progression -- required
  presence (C-11) -> STOP-enforced presence (C-45) -> consumer role named (C-47) -- is isomorphic
  to the gate progression -- scope closure (C-40) -> embedded STOP (C-44) -> successor role named
  (C-46). The anchor layer and the gate layer now share the same three-step quality pattern.

- C-45 + C-47 close a bidirectional anchor dependency: C-45 is the enforcement direction
  (STOP fires at the Mechanism Definer entry boundary if anchor is absent or Falls-short is blank
  -- the anchor controls whether the consumer role can begin); C-47 is the declaration direction
  (the anchor block names ROLE: MECHANISM DEFINER as its consumer -- the anchor declares who
  depends on it). Together, the anchor names its consumer (C-47: push reference) and the consumer
  is blocked by the anchor STOP (C-45: enforcement). This mirrors the C-41 + C-46 bidirectional
  loop at the gate layer: gate names successor (C-46) and successor names gate (C-41).

**Key distinctions:**

- C-47 != C-46: C-46 requires the gate block to name the specific successor role that is blocked
  ("ROLE: X cannot begin until gate satisfied"); C-47 requires the REFERENCE ANCHOR block to name
  the specific consumer role that depends on anchor satisfaction. Both are push references that make
  a dependency forward-visible from the declaring block alone; they operate at different structural
  layers -- C-46 at the gate layer and C-47 at the anchor layer. A rubric satisfying C-46 (gate
  names its successor) while having an anchor block that does not name its consumer fails C-47; a
  rubric satisfying C-47 (anchor names its consumer) while having a gate block that does not name
  its successor fails C-46. The two criteria are layer-parallel but layer-independent.

- C-47 != C-45: C-45 requires a STOP at the Mechanism Definer entry boundary enforcing anchor
  completeness (enforcement direction: the anchor blocks the consumer); C-47 requires the anchor
  block itself to name the consumer role (declaration direction: the anchor identifies its consumer).
  C-45 makes anchor incompleteness a Mechanism Definer entry failure; C-47 makes the anchor's
  consumer visible from the anchor block alone. A rubric satisfies C-45 (STOP fires at Mechanism
  Definer entry on absent or incomplete anchor) while failing C-47 if the anchor block does not
  name the Mechanism Definer as its consumer; C-47 stable in V-03 (C-46 ablated) and V-04
  (C-46 absent, C-41 fails) confirms satisfiability without C-46 and C-41. A rubric satisfies C-47
  (anchor names consumer) while failing C-45 if no STOP guards the Mechanism Definer entry. The
  enforcement direction (C-45) and the declaration direction (C-47) are independently realizable.

- C-47 != C-11: C-11 requires the structured REFERENCE ANCHOR block to be present with three named
  fields (Reference, Passes, Falls-short); C-47 requires the anchor block to also include a Consumer
  field naming the specific role that depends on anchor satisfaction. A rubric satisfies C-11 (three
  fields present, block exists) while failing C-47 if no Consumer field names the dependent role.
  C-11 requires anchor presence and completeness; C-47 requires the anchor to declare its downstream
  dependency, adding a fourth field (or equivalent declaration) to the structured anchor block.

- C-47 != C-41: C-41 requires the Builder Aspirational role's entry precondition to quote the
  Mechanism Definer gate identifier verbatim (successor -> gate: pull reference); C-47 requires the
  REFERENCE ANCHOR block to name the Mechanism Definer as the anchor's consumer (anchor -> consumer:
  push reference). C-41 governs gate-identifier propagation in the entry precondition of the
  successor role; C-47 governs consumer-role declaration in the body of the anchor block. Both
  contribute to cross-layer traceability but from different source positions: C-41's reference
  originates in the Builder Aspirational role's entry; C-47's reference originates in the anchor
  block. A rubric satisfies C-41 (gate identifier quoted verbatim in Builder precondition) while
  failing C-47 if the anchor block contains no Consumer field; V-03's C-47 PASS with C-41 PARTIAL
  confirms independent satisfiability.

---

### Changes from v15

Two new aspirational criteria (C-45, C-46) extracted from Round 15 excellence signals.
Denominator /36 -> /38. Round 15 ceiling: V-05 R15 passes all 38 criteria -> 38/38 x 10 = 10,
composite 100. First composite 100 confirmed.

| # | Name | Evidence |
|---|------|----------|
| **C-45** | `reference-anchor-stop-gated` | V-05 R15 -- PHASE 5 REFERENCE ANCHOR block with Reference/Passes/Falls-short structured template; STOP if absent or Falls-short blank; required before ROLE: MECHANISM DEFINER begins; the STOP converts the C-11 named-section requirement into an operational gate enforcing anchor completeness at the Mechanism Definer role boundary, applying C-44's self-enforcement principle to the reference anchor layer |
| **C-46** | `gate-successor-role-named` | V-05 R15 -- ROLE: MECHANISM DEFINER gate definition explicitly states "ROLE: BUILDER ASPIRATIONAL cannot begin until gate satisfied"; the gate names the specific successor role that is blocked, making the blocking dependency forward-visible from the gate definition alone; together with C-41 (successor quotes gate verbatim), forms a bidirectional closed reference loop: gate names successor (C-46) and successor quotes gate (C-41) |

**Denominator:** `/36` -> `/38`

**New ceiling math:** V-05 R15 (Full Five-Gate Stack + Inertia Framing) passes all 36 inherited
criteria including C-11 PASS (REFERENCE ANCHOR block with STOP enforcement, positioned before
ROLE: MECHANISM DEFINER) and C-29 PASS (formal ROLE boundary, sole output = independence map,
MECHANISM DEFINER GATE as exit condition, BUILDER ASPIRATIONAL named as blocked successor), plus
C-45 PASS (anchor STOP embedded) and C-46 PASS (successor role named in gate definition).
Total: 38/38 x 10 = 10, composite 100. First composite 100 confirmed in R15.

**Structural axes extended:**

- C-11 + C-45: C-11 requires the REFERENCE ANCHOR block to exist and name the Reference / Passes /
  Falls-short structure; C-45 requires an embedded STOP that makes anchor absence or incomplete
  Falls-short a Mechanism Definer entry failure. The anchor layer now mirrors the gate layer:
  C-11 requires the anchor (like C-40 requires the gate); C-45 requires it to be STOP-enforced
  (like C-44 requires the gate to embed its STOP). The two-criterion anchor progression -- required
  presence (C-11) -> STOP-enforced presence (C-45) -- is isomorphic to the gate progression --
  scope closure (C-40) -> embedded STOP (C-44).

- C-41 + C-46: C-41 requires the successor role's entry precondition to quote the gate identifier
  verbatim; C-46 requires the gate block to name the specific successor role that is blocked.
  Together they form a closed bidirectional reference: gate -> successor (C-46) and successor ->
  gate (C-41). A rubric satisfying C-41 alone has a one-directional reference (successor looks back
  at gate); satisfying C-46 alone has the inverse (gate looks forward at successor); satisfying both
  closes the loop, making the inter-role dependency fully traceable without reading either role's
  operational content.

**Key distinctions:**

- C-45 != C-11: C-11 requires the REFERENCE ANCHOR block to be present with the three-field
  structure (Reference / Passes / Falls-short) before aspirational criteria are written; C-45
  requires a STOP to fire if the block is absent OR if the Falls-short field is blank, making
  anchor completeness an operational gate condition rather than a naming requirement. A rubric
  satisfies C-11 (structured anchor present, three fields named) while failing C-45 if no STOP
  guards against anchor absence or incomplete Falls-short; the STOP converts a presence
  requirement into a self-enforcing gate parallel to C-44's treatment of the Definer output.

- C-45 != C-44: C-44 requires a STOP verb embedded inside a Definer output gate block; C-45
  requires a STOP verb embedded in the REFERENCE ANCHOR enforcement position before the Mechanism
  Definer role boundary. Both apply the embedded-STOP principle; they govern different structural
  layers -- C-44 governs Definer output scope enforcement; C-45 governs reference anchor
  completeness enforcement. A rubric satisfies C-44 (STOP inside Definer output gate) while
  failing C-45 (no STOP on anchor block); the anchor layer and the gate layer are independently
  enforceable.

- C-46 != C-41: C-41 requires the Builder Aspirational role's entry precondition to quote the
  gate identifier verbatim, making the Builder's entry independently verifiable from the Builder's
  own role definition; C-46 requires the gate block itself to name the specific successor role
  that is blocked ("ROLE: X cannot begin until gate satisfied"), making the blocking dependency
  forward-visible from the gate definition. C-41 is a pull reference (successor pulls gate
  identifier); C-46 is a push reference (gate pushes successor name). A rubric satisfying C-41
  (gate identifier quoted in Builder precondition) while failing C-46 (gate does not name Builder
  as its consumer) has a one-directional reference; satisfying both closes the bidirectional loop.

- C-46 != C-43: C-43 requires the gate to state its passage conditions as a positive predicate
  ("is satisfied when: [conditions]"); C-46 requires the gate to name the successor role that is
  blocked by default. C-43 governs the internal logical structure of the passage condition; C-46
  governs the forward-facing dependency declaration -- who is waiting on this gate. A gate states
  "is satisfied when: both templates. Nothing else." (satisfying C-43) without naming the next
  role (failing C-46); a gate states "ROLE: BUILDER ASPIRATIONAL cannot begin until gate satisfied"
  (satisfying C-46) without a predicate form (failing C-43). The two criteria are orthogonal.

---

### Changes from v14

Two new aspirational criteria (C-43, C-44) extracted from Round 14 excellence signals.
Denominator /34 -> /36. Round 14 ceiling: V-04 R14 under v15 passes C-40 + C-41 + C-42 + C-43 +
C-44 (C-11 ablated) -> 35/36 x 10 = 9.722, composite 99.722. Clearing C-11 yields 36/36 x 10 =
10, composite 100.

| # | Name | Evidence |
|---|------|----------|
| **C-43** | `gate-satisfaction-predicate` | V-04 R14 -- DEFINER OUTPUT GATE uses "is satisfied when: [conditions]" predicate form before the exclusion terminal; the predicate makes gate passage a formally testable logical assertion rather than an inferred consequence of scope non-violation; an evaluator can confirm gate passage by checking whether the predicate conditions hold, without requiring scope-violation detection |
| **C-44** | `gate-enforcement-stop-embedded` | V-01 R14 and V-04 R14 -- STOP appears as a named enforcement action inside the gate definition block ("STOP if content beyond two templates" / "STOP if output exceeds templates"); the STOP is part of the gate's contractual definition, not a downstream audit step or a separate role-level enforcement instruction; the gate is self-enforcing: the enforcement verb is physically co-located with the gate definition, signaling the violation consequence at the gate site |

**Denominator:** `/34` -> `/36`

**New ceiling math:** V-04 R14 passes C-40 (DEFINER OUTPUT GATE with "is satisfied when:"
predicate + "Nothing else." exclusion terminal), C-41 (both CRITERION DEFINER GATE and MECHANISM
DEFINER GATE quoted verbatim in Builder Aspirational entry), C-42 (PHASE-LOCALITY RULE present
in three-gate stack), C-43 ("is satisfied when:" predicate form present), C-44 (STOP embedded
inside gate block); C-11 ablated to isolate gate contribution vs V-05. Under v15: 35/36 x 10 =
9.722, composite 99.722. C-11 PARTIAL remains the sole gap; clearing it yields 36/36 x 10 = 10,
composite 100.

**Structural axes extended:**

- C-19/C-20 govern Definer output content (templates) and register (slot-fillable phrasing);
  C-40 extends to scope (output instruction closes the output scope via exclusion gate);
  C-43 extends scope closure to formal predicate testability (gate passage stated as positive
  "is satisfied when:" assertion, not inferred from exclusion); C-44 extends to gate
  self-enforcement (STOP verb embedded inside the gate block, enforcement signaled at definition
  site). The four-criterion progression: content -> register -> scope closure -> formal predicate
  -> self-enforcement closes the Definer output layer.

- C-40 (scope closure) + C-43 (formal predicate) + C-44 (embedded STOP) form a three-level
  gate quality progression that upgrades a terminal exclusion clause into a formally verifiable,
  self-enforcing gate contract.

**Distinction notes:**

- C-43 != C-40: C-40 requires the Definer output instruction to end with an exclusion terminal
  closing the output scope; C-43 requires the gate definition to include a satisfaction predicate
  -- "GATE is satisfied when: [conditions]" -- that states the passage conditions positively.
  A gate can satisfy C-40 ("Nothing else." closes scope, padded output is a completion failure)
  while failing C-43 (no predicate form; passage is inferred from scope non-violation, not
  testable against a stated assertion). The two criteria are ordered: C-43 is not satisfiable
  without a gate (which C-40 requires), but C-40 does not require the gate to state its passage
  conditions in predicate form. C-40 requires closure; C-43 requires formal testability.

- C-43 != C-41: C-41 requires the gate identifier to be quoted verbatim in the successor role's
  entry precondition, making the inter-role handoff independently auditable from the Builder's
  entry alone; C-43 requires the gate definition itself to use a satisfaction predicate form,
  making gate passage testable at the definition site. Both reference gate identifiers but govern
  different properties: C-41 governs identifier propagation downstream (handoff auditable without
  reading the source role?); C-43 governs the gate's internal logical structure (is the passage
  condition a positive predicate?). A rubric satisfies C-41 (gate identifier quoted verbatim in
  Builder precondition) while failing C-43 (gate definition uses exclusion-only form without a
  "is satisfied when:" predicate). The propagation test (C-41) and formal-testability test
  (C-43) are orthogonal.

- C-44 != C-40: C-40 requires the gate to end with an exclusion terminal making scope violation
  a role completion failure; C-44 requires a STOP verb to be embedded inside the gate block,
  making enforcement operational rather than contractual. A gate satisfies C-40 (exclusion clause
  present, padded output is a completion failure by definition) while failing C-44 (no STOP verb
  inside the gate; enforcement authority derives from the exclusion clause, not from an
  operational enforcement signal at the gate site). C-40 requires scope closure; C-44 requires
  the closure to be accompanied by a named enforcement action embedded within the gate definition.

- C-44 != C-43: C-43 requires the gate to state its passage conditions as a positive predicate
  ("is satisfied when:"); C-44 requires the gate to embed a STOP action specifying the violation
  condition. Both concern gate structure but govern independent aspects: C-43 governs the
  passage condition (positive predicate); C-44 governs the enforcement mechanism (embedded STOP).
  A gate that states "is satisfied when: both templates. Nothing else." satisfies C-43 but fails
  C-44 if no STOP is embedded. A gate that states "Nothing else. STOP if output exceeds templates."
  satisfies C-44 but fails C-43 (no "is satisfied when:" predicate form). Both are realizable
  independently; V-04 R14 demonstrates the combined form: satisfaction predicate + exclusion
  terminal + embedded STOP -- all three elements co-occur in the highest-quality gate
  implementation.

---

### Changes from v13

Three new aspirational criteria (C-40, C-41, C-42) extracted from Round 13 excellence signals.
Denominator /31 -> /34. Round 13 ceiling 99.559 (V-04 and V-05 R13 under v14, C-11 PARTIAL
remaining); new ceiling 100 requires C-11 PASS in addition to all thirty-three other criteria.

| # | Name | Signal it formalizes |
|---|------|---------------------|
| **C-40** | definer-output-exclusion-gate | V-01 R13 Signal 1 and V-04 R13 -- Definer output instruction ends with "Nothing else." or equivalent exclusion gate; partial or padded output becomes a role completion failure, not merely a quality shortfall; V-04 names the gate identifier explicitly ("DEFINER OUTPUT GATE") before the terminal exclusion clause, making the scope boundary auditable |
| **C-41** | role-exit-gate-named-in-precondition | V-02 R13 Signal 2 and V-04 R13 -- Builder Aspirational role's entry precondition quotes a named gate identifier verbatim; the gate identifier is the exit artifact name from the preceding role (e.g., "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated"); Builder cannot begin unless the quoted gate artifact exists, making the sequencing constraint independently falsifiable |
| **C-42** | phase-locality-rule-named | V-03 R13 Signal 3 and V-05 R13 -- A named PHASE-LOCALITY RULE enumerates three prohibited competitor-placement zones before the Builder phase begins: (1) preamble before any construction phase; (2) operating-principles/shared block preceding more than one step; (3) combined block governing more than one criterion; the rule is published as a standalone named rule and referenced in the emit manifest |

**Denominator:** `/31` -> `/34`

**New ceiling math:** V-04 R13 and V-05 R13 each pass two of the three new criteria under v14.
Base: V-05 R12 full stack 30.5/31 x 10 = 9.839 (v13). Under v14 (/34): V-04 adds C-40 PASS and
C-41 PASS, C-42 FAIL -> 32.5/34. V-05 adds C-40 FAIL, C-41 PASS, C-42 PASS -> 32.5/34. Both
yield 32.5/34 x 10 = 9.559 aspirational, composite 99.559. C-11 PARTIAL is the sole criterion
preventing 100; clearing it yields 34/34 x 10 = 10, composite 100.

**Distinction notes:**

- C-40 != C-19: C-19 requires the Definer to produce both templates as a unified paired output;
  C-40 requires the Definer's output instruction itself to end with an explicit exclusion gate
  that makes anything beyond the specified templates a role completion failure. A Definer can
  produce a unified paired output (satisfying C-19) while its output instruction is additive
  rather than bounded (failing C-40). The exclusion gate is not a template property but a scope
  boundary on the output instruction: the instruction closes with "Nothing else." or a named
  gate identifier plus exclusion clause, not with a further enumeration.

- C-40 != C-20: C-20 requires templates to be in slot-fillable phrasing register, eliminating
  the interpretation gap between Definer output and Builder input; C-40 requires the scope of
  the Definer's output to be terminated by an exclusion gate. A Definer can produce slot-fillable
  templates (satisfying C-20) while issuing an additive output instruction that permits further
  content (failing C-40). Conversely, a Definer can have a terminal exclusion gate (satisfying
  C-40) while its templates require paraphrase rather than slot-filling (failing C-20). The
  criteria are orthogonal: C-20 governs register; C-40 governs scope.

- C-40 != C-26: C-26 requires structural constraints to be embedded as the operative role's
  output requirements, not delegated to a downstream role; C-40 requires specifically that the
  output instruction end with an exclusion gate that makes padded output a completion failure.
  A Definer whose output instruction specifies required content items satisfies C-26 (constraint
  is embedded, not delegated) while failing C-40 if the instruction is open-ended rather than
  closed by a terminal gate. C-26 requires ownership; C-40 requires closure.

- C-41 != C-29: C-29 requires a dedicated sequential role -- the Mechanism Definer -- to be
  structurally prior to the Builder Aspirational, with the independence map as its exit
  condition; C-41 requires the exit artifact of that prior role to be named as a gate identifier
  and quoted verbatim in the Builder's entry precondition. A rubric can satisfy C-29 (dedicated
  prior role exists, map is the exit condition, Builder cannot logically start until the map is
  complete) while failing C-41 if the Builder's entry precondition does not quote the gate
  identifier verbatim -- the sequencing constraint exists in the role design but is not
  independently auditable from the Builder's entry alone. C-41 makes the precondition
  self-contained: an auditor reading only the Builder's entry instruction can verify the
  sequencing requirement without reading the prior role's definition.

- C-41 != C-34: C-34 requires the independence map's per-entry format to cite the affected
  criterion by number, enabling third-party audit without the removal test; C-41 requires the
  map's existence to be enforced at the Builder's entry boundary by a quoted gate identifier.
  A rubric can satisfy C-34 (map entries annotated with "affects C-NN only") while failing C-41
  if the Builder's entry precondition does not reference the gate artifact by name. C-34
  governs the map's internal format; C-41 governs the gate that enforces the map's existence
  before the Builder runs.

- C-41 != C-18: C-18 requires a dedicated pre-construction instantiation step that is logically
  prior to criterion construction; C-41 requires the exit artifact of a prior role to be quoted
  verbatim as a gate identifier in the next role's entry precondition. C-18 governs the Definer
  step for direction and template instantiation; C-41 governs the gate mechanism that enforces
  inter-role sequencing. Both can be present independently: a rubric can have a logically-prior
  Definer (satisfying C-18) with no gate identifier in the Builder's precondition (failing C-41),
  or a Builder whose precondition quotes a gate identifier (satisfying C-41) derived from a step
  that is not a dedicated Definer role (failing C-18).

- C-42 != C-36: C-36 requires each named competitor to be placed inline at the specific
  construction step whose wrong output it specifies -- the builder encounters the competitor
  at the exact moment of commitment; C-42 requires a named rule to enumerate three prohibited
  placement zones before the Builder phase, making violations identifiable by zone membership
  rather than by tracing each competitor's position relative to its construction step. A rubric
  can satisfy C-36 (all present competitors at their correct steps, verifiable by tracing)
  while failing C-42 (no named PHASE-LOCALITY RULE with enumerated prohibited zones). A rubric
  can satisfy C-42 (PHASE-LOCALITY RULE published and referenced in emit manifest) while failing
  C-36 if the rule is stated but some competitor is placed in a prohibited zone in violation of
  it. C-36 requires correct placement as a realized property; C-42 requires correct placement
  to be governed by a named rule with enumerated failure modes.

- C-42 != C-37: C-37 requires the competitor set to be in bijection with the set of novel
  aspirational criteria, making coverage completeness verifiable by counting; C-42 requires the
  phase-locality of each competitor to be governed by a named rule with three enumerated
  prohibited placement zones. A rubric can satisfy C-37 (bijection complete, correct count)
  while failing C-42 (competitor count is correct but no PHASE-LOCALITY RULE is named, so
  placement violations are visible only by per-competitor step-tracing). C-42 governs the
  spatial constraint on competitor placement; C-37 governs the cardinality constraint.

- C-42 != C-27: C-27 requires a named competitor to constitute the gap specification for each
  mechanism (negative-space definition before positive definition); C-42 requires a named rule
  to govern where those competitors may be placed, with three enumerated prohibited zones.
  C-27 is satisfiable with competitors in a preamble (gap specifications exist, constitutive
  function present) while failing C-42 (competitors in preamble violate prohibited zone 1).
  C-42 is the locality constraint on the competitor layer that C-27 introduces.

---

## Essential Criteria (C-01--C-05) -- 60 points

**C-01** (completeness) -- All criteria carry the full five-field structure: Name, Text, Pass,
Fail, Notes. Tests whether the rubric builder enforces complete five-field criteria in every
tier, with no fields omitted or merged.

**C-02** (testability) -- Pass conditions are anchored to auditable observables; qualitative-
only language is structurally prohibited. Tests whether the rubric builder bans phrases like
"clearly written" or "well-structured" without observable anchors, requiring that every Pass
condition can be verified against an artifact.

**C-03** (failure-first essential) -- Essential criteria derive from explicit failure mode
extraction targeting non-functional structural or semantic gaps. Tests whether failure mode
analysis precedes criterion drafting, and whether essential criteria address failures whose
absence causes the artifact to be broken rather than merely suboptimal.

**C-04** (formula + threshold) -- The scoring formula and golden threshold are stated
explicitly. Tests whether the rubric names the denominator, the per-tier weight, and the
numeric threshold a rubric must clear to be considered golden.

**C-05** (skill-specific) -- Criteria derive from reading the skill spec before any criterion
is drafted; generic quality concerns are not substituted for skill-derived failure modes. Tests
whether the rubric builder requires the skill spec as input and whether failure modes are
traceable to that spec.

---

## Recommended Criteria (C-06--C-08) -- 30 points

**C-06** (tier distribution) -- The rubric builder specifies tier count targets of 3-5
essential / 2-3 recommended / 1-2 aspirational. Tests whether the rubric enforces these
ranges, preventing essential-heavy rubrics that dilute tier meaning.

**C-07** (3+ categories) -- Three or more distinct categories appear across the full rubric.
Tests whether the rubric produces categorical diversity -- either by enumeration requirement
or, preferably, as a consequence of tier-dimension design.

**C-08** (quality not presence) -- Recommended criteria test quality properties (degree,
precision, specificity) rather than checking whether an element is present at all. Tests
whether recommended criteria require "how well" rather than "whether."

---

## Aspirational Criteria (C-09--C-47) -- 10 points

Denominator: **/39**. Each criterion scores 1 (full pass), 0.5 (partial), or 0 (fail).
Score = (sum) / 39 x 10.

**C-09** (causal observables) -- Criterion Text establishes the causal observable before the
Pass condition invokes it: "without X, Y fails." Tests whether the rubric builder instruction
for the Text field requires naming the downstream consequence of the observable's absence,
making the Pass condition the conclusion of an argument rather than a standalone assertion.
A rubric that only instructs "name an observable" satisfies C-02 but fails C-09.

**C-10** (contrast example) -- The rubric builds contrast awareness through "not: X but: Y"
framing. Tests whether the rubric distinguishes good criterion construction from bad by naming
the rejected form alongside the required form -- in preamble, structural guidance, or
per-criterion instruction.

**C-11** (aspirational reference anchor) -- The aspirational section names a specific
competitor or prior-version reference that passes C-01--C-08, then describes the exact
dimension in which it falls short of the aspirational bar. Tests whether the rubric builder
requires a structured Reference / Passes / Fails template before aspirational criteria are
written, so that clearing essential+recommended creates genuine further pressure rather than
a nominal ceiling.

**C-12** (Text-argues-before-Pass) -- Criterion Text establishes the causal observable
*before* the Pass condition invokes it. Tests whether the Text field instruction explicitly
requires "without X, Y fails because Z" such that the Pass condition is the conclusion of an
argument already made in the Text. This makes C-09 compliance structural from the first draft
rather than a post-hoc correction.

**C-13** (tier-grounded organic category diversity) -- Tier structure is grounded in distinct
failure dimensions, producing organic category diversity. Tests whether each tier maps to a
different failure dimension (broken artifact / quality shortfall / structural gap) and whether
the rubric builder runs a predictability or divergence check confirming that >= 2/3 tiers
produce distinct majority categories -- so that C-07 is satisfied as a consequence of tier
design, not by label assignment after criteria are drafted.

**C-14** (contrast-in-Text) -- The contrast template is embedded within the criterion Text
field construction instruction itself, not only in preamble or structural framing. Tests
whether the rubric builder explicitly requires each criterion's Text field to encode
"not: X but: Y" -- naming what the criterion rejects alongside what it requires -- such that
contrast is structurally present in every criterion's Text field rather than an emergent
property of earlier framing awareness. A rubric that builds contrast awareness in its preamble
(satisfying C-10 partially) but does not carry that requirement into the per-criterion Text
instruction fails C-14.

**C-15** (causal direction) -- The causal chain in criterion Text runs from absence of the
required property to artifact failure, not from presence of the rejected form to failure.
Tests whether the rubric builder instruction distinguishes "X causes F" (wrong-form-
consequence) from "without Y, the artifact fails because Z" (required-property-absence-
consequence) and requires the latter. A constitutive definition that names "not [X, which
causes F] but [Y]" supplies a causal chain in the wrong direction -- the argument is about
what the wrong form does, not about what the absence of the required property costs. Only
"without Y, the artifact fails because Z" passes C-15. A rubric whose Text field instruction
says "name the failure caused by the wrong form" satisfies C-09 at most partially but fails
C-15; only "name the consequence of the required property's absence" passes.

**C-16** (two-phase enforcement) -- Key structural requirements (contrast-in-Text, causal
chain, causal direction) are enforced at both the generation phase and the post-draft phase.
Tests whether the rubric builder includes both a generative structural gate -- a constraint
that makes non-compliant output unproducible from the first draft (e.g., a constitutive
definition that cannot be satisfied without the required structure) -- and a post-draft audit
step that reads each criterion's Text stripped of preamble and flags criteria that pass on
context dependency rather than self-containment (e.g., an isolation diagnostic). A rubric
with only a generation gate satisfies neither; a rubric with only a post-draft audit catches
failures but permits them to be produced and corrected. Both phases present and operative
is the pass condition. C-14 compliance achieved solely through a post-draft auditor satisfies
C-14 but fails C-16.

**C-17** (two-phase testability) -- The testability standard for Pass conditions -- that they
name auditable observables and contain no qualitative-only language -- is enforced at both
the generation phase and a post-draft audit step, not only in preamble instruction. Tests
whether the rubric builder's generation gate includes a Pass field template that makes non-
verifiable conditions structurally unproducible (e.g., by requiring Pass to name a specific
artifact location, observable token, or measurable count), AND whether the post-draft
isolation audit explicitly checks each criterion's Pass field for qualitative-only language
alongside the direction and contrast checks. A rubric that enforces causal direction at both
phases (passing C-16) but enforces testability only in preamble or isolated generation-phase
instruction creates an asymmetric enforcement structure -- direction is gated, verifiability
is not -- and satisfies C-02 partially while failing C-17.

**C-18** (role-isolated pre-instantiation) -- A dedicated pre-construction role or step
generates skill-specific instantiations of the causal direction rule and contrast pairs before
the Builder constructs any criterion. Tests whether the rubric builder includes a named Definer
step that: (a) reads the skill spec, (b) produces a concrete template naming the specific
required property (Y), failure consequence (Z), and rejected form (X) for that skill, and
(c) outputs this template as the Builder's binding input -- so the Builder operates from
concrete, skill-specific forms rather than applying abstract direction principles on-the-fly
to an unfamiliar domain. A rubric that states direction and contrast rules as abstract
principles in a shared preamble (passing C-10 and C-15) but has no dedicated pre-construction
instantiation step fails C-18, because abstract principles applied on-the-fly produce the
wrong-form-consequence failure pattern even when the rules are correctly stated in surrounding
context. The distinction from C-16: C-16 requires two phases to be present and operative;
C-18 requires the generation phase to include a definitional step that is logically prior to
construction, not concurrent with it.

**C-19** (dual-template Definer) -- The Definer role generates both the Text-direction
template (required property Y, failure consequence Z, rejected form X) and the Pass-
observability template (artifact location, observable token, measurement unit) as a unified
paired output before the Builder runs. Tests whether the rubric builder's Definer step
produces a complete, skill-specific specification pair -- not just direction guidance -- so
that the Builder receives both templates simultaneously and C-17 and C-18 are satisfied
through the same structural mechanism rather than independently. A rubric whose Definer
generates a Text template but leaves the Pass generation gate as a separate inline step
(satisfying C-18 and C-17 independently) fails C-19, because the two enforcement paths
remain architecturally separate: direction is Definer-gated, testability is step-gated.
C-19 requires that a single Definer role output governs both fields, making the generation
gate symmetric by construction. Evidence: V-03 satisfies C-17 via Step A-5 (a step within
Phase A) and C-18 PARTIAL (no dedicated role boundary); V-04's Definer produces two binding
templates as a pair, closing the asymmetry at the architectural level.

**C-20** (template composability) -- The Definer's output templates are in the exact phrasing
register of the final criterion fields, making them slot-fillable by the Builder without
paraphrase or on-the-fly interpretation. Tests whether the Text template is expressed in the
form "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." and the Pass template
in the form "LOCATION: [artifact field or section]. OBSERVABLE: [what must appear].
STANDARD: [count or exact token]." -- such that the Builder instantiates criteria by filling
slots from the Definer's output verbatim rather than translating abstract direction rules into
concrete language during construction. A rubric whose Definer produces structural guidance in
propositional form ("the Text must identify the required property, the consequence of its
absence, and the rejected form") rather than a fill-in template fails C-20, because the
Builder must still perform the translation step that produces the wrong-form-consequence
failure pattern even when the structural rules are correctly understood. The distinction from
C-18: C-18 requires that instantiation is definitionally prior to construction; C-20 requires
that the instantiation output is in a register that eliminates the interpretation gap -- that
there is no translation step between Definer output and Builder input. Evidence: V-04's title
names "phrasing register" alongside "Pre-Instantiation Definer: two binding templates,"
indicating the templates are expressly in field-register form rather than propositional form.

**C-21** (audit symmetry) -- The post-draft isolation audit mirrors the generation gate's
two-field structure: dedicated checks applied to the Text field (direction, contrast, causal
chain) and dedicated checks applied to the Pass field (observability, location specificity,
measurement presence) as parallel, individually operative audit tracks. Tests whether the
rubric builder's post-draft audit section enumerates numbered checks that cover each
generation-phase constraint -- with Text-field checks and Pass-field checks explicitly
separated rather than direction-dominant with testability as a subordinate note. A rubric
that runs post-draft checks 1-3 on Text direction+contrast+causal-chain and post-draft check
4 on Pass observability satisfies C-21; a rubric that audits direction and contrast for Text
but audits Pass only by reference to what the Definer already produced, or conflates Text and
Pass audit into a single undifferentiated isolation step, fails C-21. The distinction from
C-16 and C-17: both require two-phase enforcement for their respective fields independently;
C-21 requires the audit phase to be structurally symmetric across both fields simultaneously
-- the number and granularity of audit checks for the Pass field must match the number and
granularity for the Text field. Evidence: V-04's Auditor Checks 1-3 audit Text direction,
contrast, and causal-chain properties; Check 4 audits Pass observability in isolation --
four named checks, three for Text and one for Pass, demonstrating the parallel structure.

**C-22** (form-class prohibition exhaustiveness) -- The causal direction prohibition is stated
as form-class exhaustive -- naming the prohibited pattern as a class covering all variant
phrasings rather than as a canonical example whose variants may pass inspection. Tests whether
the rubric builder's direction constraint explicitly declares that any Text which locates the
causal chain in the wrong-form-consequence direction is prohibited "in any phrasing" -- not
just the specific form "X causes failure" but all synonymous constructions ("X leads to
failure," "the artifact fails when X is present," etc.) -- so that a Builder cannot satisfy
the prohibition check by paraphrasing the forbidden form. A rubric that names "X causes
failure" as the sole prohibited example satisfies C-15 (the direction is correctly identified)
but fails C-22, because variant phrasings of the same wrong-direction argument remain
producible. Only a prohibition that explicitly extends to the form-class closes this gap.
The distinction from C-15: C-15 requires the rubric to distinguish wrong direction from right
direction and require the latter; C-22 requires the prohibition to be exhaustive over the
wrong-direction form-class, not example-bounded. Evidence: V-04's C-15 evidence reads
"A Text beginning '[X] causes [failure]' -- in any phrasing -- is in the prohibited
direction," extending the prohibition beyond the named example to the full form-class.

**C-23** (audit report format enforces symmetry) -- The post-draft audit section specifies an
output format that makes the structural symmetry between Text-field and Pass-field audit
tracks externally verifiable. Tests whether the rubric builder requires the audit report to
separately enumerate Text-field flags and Pass-field flags as distinct named lists -- e.g.,
"Text flags: [direction N, contrast N, causal chain N]. Pass flags: [location N, observable N,
prohibited-form N]." -- so that the symmetric structure required by C-21 cannot be satisfied
nominally (equal check count on paper) while collapsing to asymmetry in practice. The
distinction from C-21: C-21 requires that the audit enumerates individually numbered checks
for both fields with equal granularity; C-23 requires that the audit specifies a report format
whose structure makes symmetry independently falsifiable -- an evaluator examining only the
report output can determine whether the implementation was symmetric, without reading the
procedure. A rubric that runs three Text checks and three Pass checks but produces a single
undifferentiated flag tally passes C-21 but fails C-23. Evidence: V-04's audit report format
"Text flags: [N,N,N]. Pass flags: [N,N,N]." enforces symmetry by making it independently
reportable; the format is the enforcement mechanism, not a documentation artifact alongside it.

**C-24** (check function redefinition) -- The Auditor's operative check function for the
prohibited direction is explicitly redefined from example-matching to causal-structure testing.
Tests whether the rubric builder's audit step states the Auditor's check function as "does
this text locate causality in the wrong form's consequence?" -- not "does this match the
canonical prohibited example?" -- so that the shift from example-bounded to form-class testing
is present in the procedure, not merely implied by the form-class enumeration. The distinction
from C-22: C-22 requires the prohibition to enumerate variant phrasings and close the
form-class; C-24 requires the Auditor's operative function to be redefined to class-membership
testing, making the check function the conclusion that the enumeration and closure together
entail. Enumeration and closure without function redefinition leave the Auditor running a
longer pattern-match list; function redefinition makes the Auditor test against the underlying
causal structure regardless of surface phrasing. A rubric that enumerates five prohibited
variants and states "form-class is closed" (satisfying C-22) but whose Auditor check reads
each variant in sequence satisfies C-22 but fails C-24. Evidence: V-04's Auditor Check 1
names the check function as "does this locate causality in the wrong form's consequence, in
any phrasing? -- not 'does this match the canonical example?'" -- the function redefinition
is stated explicitly, not derived from the enumeration list.

**C-25** (independent-mechanism pairing) -- When multiple independent gaps exist, the rubric
builder closes each with a dedicated, independent mechanism -- one mechanism per gap -- such
that removing one mechanism causes exactly one criterion to fail, not both. Tests whether the
builder's architecture assigns one structural element per criterion gap, making the design
decomposable: each mechanism can be traced to the single criterion it closes, and no mechanism
carries dual responsibility for two gaps simultaneously. A rubric that introduces a combined
"unified enforcement step" that addresses two independent gaps with one structural move
satisfies neither criterion as cleanly as two independent mechanisms, because coupling means
neither mechanism can be evaluated in isolation. The pattern recurs: C-21 gap closed by
symmetric-checks mechanism; C-22 gap closed by form-class-exhaustive mechanism. C-23 gap
closed by format-as-output mechanism; C-24 gap closed by function-redefinition mechanism.
Each pair demonstrates independent closure without coupling. The distinction from C-16/C-17
(which require two enforcement phases for individual fields): C-25 requires that across
multiple gap-criterion pairs, the assignment is one-to-one -- each gap has one mechanism,
each mechanism targets one gap -- not many-to-one or one-to-many. Evidence: V-04 and V-05
each add exactly two mechanisms and close exactly two criteria; the mechanisms are
architecturally independent -- the format table does not depend on the function redefinition
block, and vice versa.

**C-26** (constraint-as-output-requirement) -- Structural constraints (audit format, template
shape, field content) are stated as required outputs of the operative role that must produce
them, not delegated to a downstream role. Tests whether the rubric builder embeds each
enforcement requirement inside the operative role's output instruction -- rather than as a
target for a separate role that the operative role passes findings to -- so that the operative
role cannot satisfy its own instructions while omitting the required structure. A rubric that
delegates format specification to a downstream "Report Format Specifier" role fails C-26:
the Auditor can complete all its checks and satisfy its own instructions before the Specifier
runs; if the Specifier is abbreviated or omitted, the constraint is unenforced. Format-as-
output-requirement is structurally stronger than format-as-downstream-role because the
operative role's completion condition requires the structured output to exist. The distinction
from C-23: C-23 requires that the audit format makes symmetry independently falsifiable; C-26
requires that the format be embedded as the operative role's own output requirement, not
handed off. V-03 closes C-23 partially (a format exists) but fails C-26 (the Auditor hands
findings to a Specifier; the Auditor's own output instruction specifies no format). V-01 and
V-04 satisfy both: the mandatory per-criterion table is the Auditor's required output, with
an explicit prohibition on substituting a narrative log. Evidence: V-04's Auditor output
instruction reads "Do not substitute a narrative log for this table" -- the table is the
Auditor's required output, making delegation structurally impossible.

**C-27** (competitor-as-gap-specification) -- The rubric builder names a specific wrong-
implementation competitor before defining the correct implementation, making the competitor
description the constitutive gap specification. Tests whether a named block preceding each
key mechanism describes the specific alternative that has the mechanism's surface form without
its operative substance -- e.g., naming a "Pattern-Matcher Auditor" that consults the
PROHIBITED DIRECTION list and extends to semantic equivalence, then stating "this is still
a list-membership test" -- such that a reader can derive what the correct implementation must
not do from the competitor alone, independently of the positive definition that follows.
The competitor description functions as a negative-space definition: the gap between what the
competitor does and what the required implementation does is the criterion the mechanism
closes. A rubric that correctly states the required function (satisfying C-24) without naming
the competitor satisfies C-24 but fails C-27; the distinction is whether the gap is visible
through negative-space specification before positive specification, or only stated directly.
The distinction from C-11 (aspirational reference anchor): C-11 requires a prior-version
reference that passes essential+recommended but falls short on an aspirational dimension; C-27
requires a named wrong-implementation that has the mechanism's surface form (e.g., a list,
a format, a step) but lacks its operative substance -- the competitor is a foil for mechanism
design, not a ceiling-setting reference. Evidence: V-05's OPERATING PRINCIPLE 1 names the
Pattern-Matcher Auditor and describes its failure mode -- "this is still a list-membership
test" -- before stating the required function; the competitor description IS the gap
specification, making the required function derivable from the foil alone.

**C-28** (competitor-derivation-instruction) -- The competitor block that constitutes the
gap specification (C-27) includes an explicit imperative directing the reader to perform the
derivation from the competitor alone before reading the positive definition. Tests whether
the rubric builder requires each competitor block to end with an instruction of the form
"from the description above, derive the required function before reading the positive
definition below" -- converting the derivability property required by C-27 into a structured
reader procedure. A competitor block that correctly constitutes the gap specification
(satisfying C-27) without a derivation instruction leaves derivation as an optional inference
available to an attentive reader rather than a required procedure for all readers; two rubrics
with identical competitor content differ on C-28 solely by presence or absence of this
imperative. The distinction from C-27: C-27 requires the required function to be derivable
from the competitor description alone; C-28 requires the competitor block to explicitly
instruct the derivation, converting a derivable property into a required procedure. Evidence:
V-01's competitor block ends with "This competitor IS the gap specification -- from the
description above, derive the required function before reading the positive definition below.
OPERATING PRINCIPLE 1 follows and confirms." -- the derivation is instructed, not merely
made available.

**C-29** (independence-verification-role-boundary) -- Independence verification for mechanism-
criterion assignment is performed by a dedicated sequential role -- the Mechanism Definer --
that is structurally prior to the aspirational criterion Builder, not as a gate within the
Builder's instructions or a post-draft audit step. Tests whether the construction workflow
names a specific role whose sole output is the independence map, and whose completion is the
Builder's input precondition -- so that the Builder receives a completed independence map as
input rather than verifying independence concurrently with construction. A rubric whose
Builder instructions include a pre-criterion independence check (satisfying C-25 partially)
but with no dedicated prior role boundary fails C-29: the independence check is concurrent
with, not prior to, construction, and can be abbreviated or skipped without violating the
Builder's role contract. The distinction from C-25: C-25 requires one-to-one assignment as
a design principle and requires the assignment to be stated explicitly; C-29 requires that
verification occur in a named, sequentially prior role phase, making it structurally impossible
to begin writing aspirational criteria without a completed independence map. The distinction
from C-18: C-18 requires a definitional step prior to criterion-field construction; C-29
requires that independence verification specifically -- not direction instantiation -- be a
prior named role step with the independence map as its exit condition. Evidence: V-04's
four-role sequence (Dual Definer -> Builder E+R -> Mechanism Definer -> Builder aspirational
-> Dual Auditor) places the MECHANISM DEFINER between construction phases; the Definer's exit
condition is the independence map; the Builder aspirational cannot run until the map is
complete and shows "Yes -- affects C-NN only" in every row.

**C-30** (independence-demonstrable-by-removal) -- The mechanism set is assembled so that
independence is demonstrable by the removal test: removing any single mechanism from the
architecture leaves exactly one criterion failing, confirming that no mechanism carries dual
responsibility for two gaps and that no two mechanisms jointly close a single criterion.
Tests whether the rubric builder's mechanism assignment satisfies the removal test as a
structural property -- independently verifiable by an evaluator who inspects what criterion
would fail if each mechanism were absent, without reading the mechanism-design rationale.
A rubric whose mechanism map correctly names one mechanism per criterion (satisfying C-25 by
declaration) but whose mechanisms share structural dependencies -- such that removing
mechanism A degrades both criterion X and criterion Y because they both rely on a shared
structural property A produces -- satisfies C-25 by statement but fails C-30 by construction.
The distinction from C-25: C-25 requires one-to-one assignment as a stated principle,
evidenced by named mechanism-criterion pairs; C-30 requires the architecture to satisfy the
removal test as a constructive property, making independence verifiable by inspection rather
than by reading the builder's design argument. The distinction from C-29: C-29 requires a
dedicated prior role step to produce the independence map; C-30 requires that the mechanism
set itself passes the removal test -- the role boundary can exist (C-29 pass) while the
mechanisms share dependencies (C-30 fail). Evidence: V-05's three-mechanism design --
MECHANISM MAP, OUTPUT OWNERSHIP PRINCIPLE, Pattern-Matcher competitor block -- demonstrates
independence by construction: removing any one mechanism leaves exactly one criterion failing
(C-25, C-26, or C-27 respectively), no mechanism degrades two criteria, and no two mechanisms
jointly close one criterion; independence is architectural, not asserted.

**C-31** (aspirational-tier-count-bounded) -- The tier distribution specification names an
explicit upper bound for the aspirational tier count ("1-2 aspirational"), completing the
three-tier count triplet; the aspirational tier is bounded by the same range-setting
instruction that bounds the essential and recommended tiers. Without an aspirational ceiling,
a rubric builder can produce a criteria-dense aspirational tier that absorbs failures from
the recommended tier, inflates the aspirational score, and makes the tier structure
progressively meaningless as criteria accumulate. Not "targets stated for essential and
recommended only" but "targets stated for all three tiers, with the aspirational upper bound
making over-population of the aspirational tier a STOP condition parallel to the essential
and recommended ranges." Tests whether the role spec states an explicit aspirational count
range alongside the essential and recommended ranges, and whether the aspirational upper
bound is operative (a STOP or rewrite condition for a builder who drafts more than two
aspirational criteria, not merely a preference). The distinction from C-06: C-06 requires
tier count targets to be present; C-31 requires the aspirational tier's explicit upper bound
to complete the three-tier triplet. A role spec can satisfy C-06 partially by stating
essential and recommended ranges while failing C-31 because the aspirational tier is
unbounded. Evidence: all five Round 10 variations specify "3-5 essential / 2-3 recommended"
but none state "1-2 aspirational"; the aspirational tier remains unbounded across the full
round, confirming the gap is systematic rather than incidental.

**C-32** (category-diversity-stop-enforced) -- Category diversity (>= 3 distinct categories
across the full rubric) is enforced by an explicit STOP condition or named verification check
in the operative role's construction instructions, not merely by listing category options as
a menu. Without enforcement, a builder can select three adjacent quality properties from the
same category domain, producing a rubric that appears diverse by label while measuring the
same underlying property from multiple angles. Not "categories offered as choices from a
named list" but "distribution verified by an operative check with a STOP on under-diversity
-- a named condition requiring the builder to confirm >= 3 distinct categories appear before
proceeding to Emit." Tests whether the role spec includes a named STOP condition or
verification step requiring the builder to confirm >= 3 distinct categories across the output;
the check must be operative (blocking Emit if the distribution requirement is not met) rather
than aspirational (noting that diversity is preferred). The distinction from C-07: C-07
requires that 3+ distinct categories appear across the full rubric; C-32 requires that their
presence is enforced by an explicit operative check, not merely encouraged by the category
menu. A rubric can satisfy C-07 incidentally (the output happens to have 3+ categories
because the builder selected well from the menu) while failing C-32 (no operative STOP made
the distribution required). Evidence: all five Round 10 variations list five category options
(correctness | depth | format | coverage | behavior) but none include a verification step or
STOP condition requiring >= 3 distinct categories in the output; C-07 is universally PARTIAL
across Round 10, confirming that listing options does not produce enforced diversity.

**C-33** (partial-handling-named-in-scoring) -- The scoring specification names PARTIAL
handling as an explicitly required sub-element, defining the fractional score assigned to a
PARTIAL result and the conditions under which a criterion earns PARTIAL rather than PASS or
FAIL; all three scoring states are named with their values and earn conditions. Without named
PARTIAL handling, a rubric whose criteria have partial-satisfaction states produces
inconsistent scoring -- evaluators assign partial credit by judgment rather than by defined
procedure, making the same criterion earn different point values across evaluators. Not
"PARTIAL implied by the composite formula structure" but "PARTIAL named as a third scoring
state alongside PASS and FAIL, with fractional score value (e.g., 0.5) and earn conditions
stated explicitly in the Scoring section." Tests whether the Scoring section contains an
explicitly named PARTIAL sub-element that states: (a) the fractional score value and (b) the
conditions under which a criterion earns PARTIAL rather than PASS or FAIL; both elements must
be present, not just the score value or the earn conditions alone. The distinction from C-04:
C-04 requires the composite formula and golden threshold to be stated; C-33 requires PARTIAL
handling to be a named scoring sub-element with score value and earn conditions, making the
three-state scoring system complete and unambiguous. A rubric passes C-04 (formula and
threshold present) while failing C-33 (PARTIAL is implied by the formula structure but not
named with earn conditions). Evidence: V-01 and V-02 require Phase 4 Emit to produce
"Scoring -- composite formula, golden threshold, PARTIAL handling" as three named sub-
elements; V-03, V-04, and V-05 require only "Scoring" with no sub-element specification,
leaving PARTIAL handling undefined in the rubric output.

**C-34** (independence-map-criterion-annotated) -- The independence map produced by the
Mechanism Definer cites the single affected criterion by number for each mechanism entry,
enabling a third-party auditor to verify the one-to-one assignment without running the
removal test. Without criterion-specific annotation, the independence map is a declarative
table (mechanisms listed, independence claimed) rather than a verifiable artifact -- an
auditor must construct the argument that each mechanism targets exactly one criterion by
reading the mechanism descriptions and matching them to criteria. Not "independence declared
per mechanism" but "criterion number cited per mechanism entry in the form 'affects C-NN
only,' with a STOP condition if any entry is blank or cites multiple criteria." Tests whether
the independence map's output format includes, for each mechanism entry, an explicit citation
of the single criterion it affects (e.g., "Yes -- affects C-NN only"); whether the map
format makes it structurally impossible to complete an entry without naming a specific
criterion; and whether there is a STOP condition for entries that are absent, blank, or cite
multiple criteria. The distinction from C-29: C-29 requires the Mechanism Definer role to
produce a completed independence map as its exit condition; C-34 requires the map's per-entry
format to cite the affected criterion by number, making the map independently auditable.
A rubric satisfies C-29 (dedicated prior role, map exists) while failing C-34 (the map
entries declare independence without naming the affected criterion). The distinction from
C-30: C-30 requires the mechanism set to satisfy the removal test as a constructive property;
C-34 requires the map to encode criterion-specific annotations enabling third-party audit
without the removal test -- a mechanism set satisfying C-30 by construction can still fail
C-34 if the per-entry criterion citations are absent from the map format. Evidence: V-02's
independence map uses "Yes -- affects C-NN only" per entry with an explicit STOP condition
for any "No" row; the format makes the one-to-one assignment auditable from the map alone,
without access to the criteria or the removal test. V-01's PARTIAL on C-25 traces precisely
to this gap: one-to-one assignment is implicit in V-01's competitor-block structure, but no
independence map format with criterion citations exists, so the assignment cannot be verified
by a third party without reading the mechanism descriptions and performing the matching step.

**C-35** (divergence-check-operationalized) -- After criteria are assigned to tiers, a named
verification step counts the category assignments per tier, identifies the majority category
for each tier, and outputs the per-tier distribution as a structured artifact; the step
includes a STOP condition if fewer than 2 of 3 tiers have distinct majority categories.
Without this step, tier-to-severity grounding produces organic diversity by design intent
but leaves the distribution unverified -- an evaluator cannot confirm the diversity claim
without re-reading all criteria and performing the count manually. Not "tiers grounded in
distinct failure dimensions so that diversity is expected to emerge" but "majority category
computed per tier after assignment, distribution recorded as a named output, STOP fires before
Emit if the >= 2/3-distinct-majority requirement is not met." Tests whether the construction
workflow includes a named step that: (a) counts category assignments within each tier,
(b) identifies the majority category per tier, (c) outputs the count as a verification table
(e.g., "Essential: correctness x3, depth x1, format x1 -- majority: correctness. Recommended:
depth x2, format x1 -- majority: depth. Aspirational: behavior x1, coverage x1 -- no
majority"), and (d) fires a STOP if < 2 tiers have distinct majority categories, requiring
revision before Emit. The distinction from C-13: C-13 requires the tier structure to be
grounded in distinct failure dimensions and requires the divergence check to be run; it is
universally PARTIAL in Round 11 because all five variations satisfy the grounding requirement
but none produce the explicit check as a named step with structured output. C-35 requires the
check to be operationalized -- a named step, a structured output format, and a STOP condition
-- making the verification independently falsifiable by an evaluator who examines the
construction record rather than re-deriving the distribution from the criteria themselves.
A rubric whose tier design organically produces category diversity (satisfying C-13 partially)
fails C-35 if no named step captures and records the distribution; design intent and
verification artifact are distinct requirements. Evidence: all five Round 11 variations assign
criteria by failure severity, which produces organic diversity (C-13 PARTIAL across the board)
but none output a per-tier category count or name a step that would fire if the distribution
requirement were not met; the universal PARTIAL on C-13 confirms the operationalization gap
is systematic.

**C-36** (competitor-at-construction-step) -- Each named competitor that constitutes a gap
specification (C-27) appears inline at the specific construction step where the wrong
implementation would most naturally be produced -- not in a preamble, operating-principles
section, or shared block preceding all mechanism definitions. When a competitor is placed at
a construction step, the builder encounters the gap specification at the exact moment of
commitment: before writing the aspirational count, before writing the category assignment,
before writing the scoring section. This creates a just-in-time prevention gate whose
authority derives from temporal proximity, not from prior reading or ambient context.
Not "competitor named before the positive definition" but "competitor placed inline at the
construction step for its specific mechanism -- the wrong implementation is the first content
the builder reads before making the structural decision the competitor's failure traces to."
Tests whether each competitor block appears as the opening of the construction step whose
output it governs -- so that the gap specification is encountered before the design decision
is committed, not during a general preamble that precedes all steps simultaneously. The
distinction from C-27: C-27 requires the competitor to constitute the gap specification
regardless of placement; C-36 requires the competitor to be placed at the construction step
whose wrong output it specifies. A rubric can satisfy C-27 (competitor correctly constitutes
the gap spec, placed in an operating-principles block at the start of the role) while failing
C-36 (the competitor is read once at role startup, not at the specific construction step).
The distinction from C-11: C-11 requires a structured Reference / Passes / Fails anchor
before the aspirational section opens, using a prior-version reference whose overall design
passes essential+recommended; C-36 requires per-mechanism competitors to be placed at the
step for each mechanism specifically, with temporal anchor at the mechanism's construction
moment. V-05's PARTIAL on C-11 traces precisely to this gap: V-05 places the Unbounded-
Aspirational competitor at Builder A (satisfying C-36), but the three-field prior-version
Reference / Passes / Fails format required by C-11 is absent. Evidence: V-05's Unbounded-
Aspirational competitor appears at Builder A (the step where aspirational count is committed);
the Category-Menu competitor at the category-verification step; the Formula-Only Scorer
competitor at the scoring-section step; the Declared-Independent Map competitor at the
Mechanism Definer step -- each competitor is the first content read before the structural
decision it governs. V-01--V-04 fail C-27 entirely (no competitors) and therefore fail C-36
by absence; V-05 PASS on C-36 by placing each competitor inline at its construction step.

**C-37** (competitor-criterion-coverage-complete) -- For every aspirational criterion that
introduces a novel construction requirement -- a requirement that does not appear in the
essential or recommended tiers and that creates a new decision point the builder must navigate
during aspirational criterion construction -- there is exactly one named competitor that IS
its gap specification (C-27), and the total competitor count equals the novel-requirement
criterion count. The gap structure is enumerable by inspection: a reader who counts the
competitors knows how many novel construction requirements the rubric's aspirational tier
introduces, without reading the criteria themselves. Without complete coverage, a rubric can
have well-formed competitors for some gaps while leaving others navigated only by positive
specification -- the builder can produce a wrong implementation of an uncovered gap because
no competitor makes the wrong form visible before the construction decision is committed.
Not "competitors exist for some novel criteria" but "every novel construction requirement in
the aspirational tier has exactly one competitor, the set of competitors and the set of
novel-requirement criteria are in bijection, and the total competitor count equals the total
novel-criterion count." Tests whether the rubric's competitor set covers all aspirational
criteria that introduce structural design decisions not constrained by essential or recommended
criteria; whether each novel criterion has exactly one competitor (no criterion covered by two
competitors, no competitor covering two criteria); and whether the coverage is verifiable by
inspection. The distinction from C-27: C-27 requires competitors to exist and to constitute
gap specifications for the mechanisms they accompany; it is satisfied by naming any number of
well-formed competitors, regardless of whether all novel criteria are covered. C-37 requires
the coverage to be complete -- a rubric with two well-formed competitors for two criteria
(C-27 PASS) but two additional novel criteria with no competitors fails C-37 even though its
competitors satisfy C-27. The distinction from C-25: C-25 requires one-to-one assignment
between mechanisms and criteria at the architecture level (what the output contains); C-37
requires one-to-one correspondence between competitors and novel criteria in the gap-
specification layer (what the builder reads before constructing). The distinction from C-36:
C-36 requires each competitor to be placed at the correct construction step; C-37 requires
the competitor set to be complete -- a rubric can satisfy C-36 (all present competitors are
at their correct steps) while failing C-37 (some novel criteria have no competitor). Evidence:
V-05 passes both -- four named competitors, each at its construction step (C-36), covering
the four novel aspirational criteria introduced in Round 10 (C-31 -> Unbounded-Aspirational,
C-32 -> Category-Menu, C-33 -> Formula-Only Scorer, C-34 -> Declared-Independent Map)
exactly (C-37). V-01--V-04 fail both by competitor absence.

**C-38** (self-referential-coverage-demonstration) -- When the aspirational tier's set of
novel criteria includes C-37 (the coverage-completeness criterion) itself, the competitor
assigned to C-37 occupies one of the bijection slots that C-37 governs, making coverage
completeness verifiable by counting the competitor list without reading the criteria. The
bijection is self-demonstrating rather than asserted: a reader who enumerates the competitors
and confirms that one (e.g., Partial-Coverage Architect) is assigned to C-37 has verified
that the coverage is complete, because C-37's presence in the competitor set means the set
covers every novel criterion including the coverage criterion itself. Not "coverage
completeness claimed by assertion, by a separate count step, or by consulting the criterion
list" but "the competitor assigned to C-37 is inside the bijection it governs -- counting
the competitors yields the novel-criterion count, and one of those competitors closes C-37,
making the self-inclusion structurally present." Tests whether: (a) C-37 is listed as a novel
criterion in the current round; (b) a named competitor appears at C-37's construction step
(satisfying C-36 for C-37's own competitor); (c) the total competitor count equals the total
novel-criterion count including C-37; and (d) this equality is verifiable by listing and
counting competitors without access to the criterion list. The distinction from C-37: C-37
requires bijection between the competitor set and the novel-criterion set; C-38 requires that
bijection to be self-demonstrating when C-37 is itself a novel criterion -- the competitor
covering C-37 is inside the set whose size C-37 constrains, making completeness a structural
self-inclusion rather than an externally verified claim. A rubric satisfies C-37 (bijection
present) while failing C-38 if C-37 is not a novel criterion in the current round and
therefore has no assigned competitor. C-38 is N/A for rounds where C-37 was introduced in a
prior round and is not itself novel. The distinction from C-36: C-36 requires each competitor
to appear at its construction step regardless of which criterion it covers; C-38 requires
specifically that the competitor at C-37's construction step be present and that its presence
makes the bijection self-verifiable by count. Evidence: V-05 R12 assigns Competitor 7
(Partial-Coverage Architect) to C-37 -- one of the seven novel criteria introduced in Round 12
(C-31--C-37); counting the seven competitors confirms bijection, and one competitor covers
C-37 itself, making the SEVEN-COMPETITOR COVERAGE CONFIRMATION block verifiable by count
without reading the criteria. V-05 R11 satisfies C-37 (four competitors, four novel criteria
in bijection) but fails C-38 because C-37 was not itself a novel criterion in Round 11 (it
was introduced that round but the competitor set covers C-31--C-34, not C-37 itself).

**C-39** (competitor-at-verification-step) -- The competitor-then-imperative pattern (C-27,
C-28, C-36) applies to verification-step gaps as well as construction-design gaps: when a
criterion requires a named verification step (e.g., C-35 requires a divergence-check step),
the gap between organic verification-by-design-intent and operationalized verification is
closed by placing a named competitor inline at the verification step where the wrong form
would be accepted as sufficient -- not by direct procedural instruction, additional table
entry, or role gate. The competitor names the specific wrong form of verification (e.g.,
Tier-Blind Categorizer: a rubric whose tier-grounded design produces organic category
diversity, relying on design intent without counting or outputting a distribution), and ends
with a derivation instruction ("from the description above, derive what the required
verification step must do -- before reading the operative requirement"), converting the
verification gap into a required reader procedure before the positive step is specified.
Not "verification-step gap closed by adding a check to the procedure" but "verification-step
gap closed by a named competitor placed inline at the post-draft audit or verification step,
constituting the gap specification for the operationalization requirement, following the
competitor-then-imperative axis." Tests whether: (a) each verification-step gap (a criterion
requiring a named verification step that is universally absent in the prior round) has a named
competitor placed inline at the verification step rather than in a preamble or as a separate
instruction; (b) the competitor constitutes the gap specification for the verification
requirement -- naming the wrong form of verification and making the required step derivable
from the competitor alone; (c) the competitor block ends with a derivation instruction;
and (d) the placement is at the verification step itself, so the builder encounters the wrong-
form competitor at the moment of committing to how to verify, not during general orientation.
The distinction from C-36: C-36 requires each competitor to appear at the construction step
for its mechanism (where a design decision is committed); C-39 extends the same placement
requirement to verification steps -- steps that check whether a design requirement is met
rather than steps that produce the design itself. The distinction from C-35: C-35 requires
the divergence-check step to be present, named, structured, and STOP-gated; C-39 requires
the gap that C-35 closes to be made visible through an inline competitor at the verification
step, following the competitor-then-imperative pattern, rather than being stated directly as
a procedural instruction. A rubric can satisfy C-35 (step added by direct instruction, present
and operative) while failing C-39 (no competitor precedes the step, wrong form not visible
before positive requirement). The distinction from C-28: C-28 requires all competitor blocks
to end with a derivation instruction regardless of what gap they close; C-39 requires
specifically that verification-step gaps are closed by competitors at verification steps -- a
rubric can satisfy C-28 for all construction-step competitors while failing C-39 if no
competitor appears at any verification step. Evidence: V-05 R12 closes C-35 via the Tier-
Blind Categorizer placed inline at the post-draft audit step -- the competitor names the wrong
form (organic diversity without a named step), ends with a derivation instruction, and appears
before the divergence-check step specification; the gap between design-intent verification and
operationalized verification is made visible through a wrong-form competitor before the
required step is stated, extending the competitor-then-imperative axis from construction-
design gaps to verification-step gaps. The Tier-Blind Categorizer simultaneously closes C-35
(the step exists, derived from the competitor) and upgrades C-13 from PARTIAL to PASS (both
the tier-grounding and the operationalized check are now present), demonstrating that a
correctly placed verification-step competitor can satisfy multiple interdependent criteria
through the derivation instruction.

**C-40** (definer-output-exclusion-gate) -- The Definer role's output instruction ends with an
explicit exclusion gate -- "Nothing else." or a named gate identifier followed by an exclusion
clause -- that makes partial or padded output a role completion failure, not merely a quality
shortfall. Without an exclusion gate, the Definer's output instruction is additive: it specifies
what must appear but leaves the output scope open, permitting the Definer to produce the required
templates plus commentary, scaffolding, or elaboration without violating its role contract.
An open-ended output instruction produces a structurally ambiguous handoff: the Builder receives
both the required slot-fillable templates and unrequested content, introducing an interpretation
step (which content is binding?) that the exclusion gate eliminates. Not "Definer output
instruction specifies required templates" but "Definer output instruction ends with a terminal
gate that makes anything beyond the specified templates a role completion failure -- the output
scope is closed, not open, so the Builder's input is exactly the templates and nothing more."
Tests whether: (a) the Definer's output instruction ends with "Nothing else." or a named gate
identifier (e.g., "DEFINER OUTPUT GATE") followed by an exclusion clause; (b) the exclusion
clause converts scope violation from a quality shortfall into a role completion failure;
(c) the gate is terminal -- the last element of the output instruction, not a mid-instruction
constraint that the instruction continues past. The distinction from C-19: C-19 requires the
Definer to produce both templates as a unified paired output; C-40 requires the output
instruction itself to end with an exclusion gate that closes the output scope. A Definer can
produce a unified paired output (satisfying C-19) while issuing an additive output instruction
(failing C-40). The distinction from C-20: C-20 requires templates to be slot-fillable in the
correct phrasing register; C-40 requires the scope of the output to be bounded by a terminal
exclusion gate. C-20 and C-40 are orthogonal: a rubric can satisfy C-20 (slot-fillable
templates) while failing C-40 (no exclusion gate, output scope open). The distinction from
C-26: C-26 requires structural constraints to be embedded as the operative role's output
requirements rather than delegated downstream; C-40 requires specifically that the output
instruction end with a terminal gate closing the output scope. C-26 can be satisfied when
the output instruction specifies required content without ending with an exclusion gate.
Evidence: V-01 R13 "Two slot-fillable templates. Nothing else." -- the terminal clause is the
exclusion gate, making anything beyond the two templates a role completion failure. V-04 R13
names the gate identifier explicitly: "DEFINER OUTPUT GATE: Two slot-fillable templates, no
additional content. Nothing else." -- the named gate makes the closure auditable by identifier
reference in downstream roles. V-02, V-03, and V-05 R13 issue additive Definer output
instructions (satisfying C-19) without terminal exclusion gates (failing C-40).

**C-41** (role-exit-gate-named-in-precondition) -- The Builder Aspirational role's entry
precondition quotes a named gate identifier verbatim -- the exit artifact name of the
immediately preceding role -- making the Builder's role entry independently verifiable: an
auditor reading only the Builder's entry instruction can confirm both the required artifact and
its source role without reading the preceding role's definition. Without a verbatim gate
identifier in the precondition, the sequencing constraint between roles exists by design intent
(the Mechanism Definer produces a map that the Builder uses) but is not independently
auditable: an auditor must read both role definitions to confirm the handoff. A verbatim gate
identifier converts the sequencing constraint from a design-intent property into an explicit
entry condition that the Builder's role contract enforces before any construction step is
executed. Not "Builder entry instruction references the preceding role's output informally"
but "Builder entry precondition quotes the gate identifier verbatim -- the quoted string names
the specific artifact that must exist and is the exact identifier assigned to the preceding
role's exit gate, making the handoff traceable by identifier match without reading either
role's operational content." Tests whether: (a) the Mechanism Definer role names an exit gate
identifier (e.g., "MECHANISM DEFINER GATE"); (b) the Builder Aspirational role's entry
precondition quotes that identifier verbatim (e.g., "Input: MECHANISM DEFINER GATE:
Independence Map with all C-NN citations populated"); (c) the precondition states that the
Builder cannot begin unless the named gate artifact exists; and (d) the gate identifier match
is verifiable without reading the role operational content. The distinction from C-29: C-29
requires a dedicated sequential role to produce the independence map before the Builder runs,
making it structurally impossible to begin aspirational criteria without a completed map;
C-41 requires the exit artifact of that role to be named as a gate identifier and quoted
verbatim in the Builder's entry precondition. A rubric satisfies C-29 (dedicated prior role,
map is the exit condition, Builder cannot logically start until the map is complete) while
failing C-41 if the Builder's entry instruction does not quote the gate identifier verbatim.
The distinction from C-34: C-34 requires the independence map's per-entry format to cite the
affected criterion by number; C-41 requires the map's existence to be enforced at the
Builder's entry boundary by a verbatim gate identifier. C-34 governs the map's content
format; C-41 governs the gate mechanism that makes the map's absence a Builder entry failure.
The distinction from C-18: C-18 requires the generation phase to include a definitional step
logically prior to criterion-field construction; C-41 requires the exit artifact of a prior
role to be quoted verbatim in the Builder's entry precondition. Both can be present
independently: a logically-prior Definer step (satisfying C-18) need not produce a named gate
identifier quoted in a precondition (failing C-41). Evidence: V-02 R13 Phase 5.5 names
"ROLE: MECHANISM DEFINER" with exit gate "MECHANISM DEFINER GATE: Independence Map with all
C-NN citations populated"; Phase 6 "ROLE: BUILDER ASPIRATIONAL" entry precondition quotes
verbatim: "Input required: MECHANISM DEFINER GATE: Independence Map with all C-NN citations
populated. Builder cannot begin unless this artifact exists." V-04 R13 quotes two gate
identifiers verbatim (CRITERION DEFINER GATE and MECHANISM DEFINER GATE) in the Builder
Aspirational's entry precondition, confirming both prior roles completed. V-01, V-03 use
PHASE headers that enforce ordering implicitly but do not name gate identifiers or quote them
in Builder entry preconditions.

**C-42** (phase-locality-rule-named) -- A named PHASE-LOCALITY RULE enumerates exactly three
prohibited competitor-placement zones before the Builder Aspirational phase begins, is published
as a standalone named rule (not embedded in a role's operational steps), and is referenced in
the emit manifest. The three prohibited zones define the placement failure mode class for
competitors: (1) preamble before any construction phase; (2) operating-principles or shared
block preceding more than one construction step; (3) combined block governing more than one
criterion. Without a named rule, placement correctness is verifiable only by tracing each
competitor to its step individually -- an evaluator must read every competitor block and
confirm its position relative to its governing construction step. The PHASE-LOCALITY RULE
converts per-competitor step-tracing into a zone membership check: a competitor is correctly
placed if and only if it does not appear in any of the three enumerated prohibited zones,
making placement auditable by zone membership without reading the construction record.
The emit manifest reference makes the rule a required output verification target: the emitter
cannot satisfy the manifest without confirming that no competitor occupies a prohibited zone.
Not "competitor placement governed by a general instruction to place competitors at their steps"
but "a named PHASE-LOCALITY RULE with exactly three enumerated prohibited placement zones
published before the Builder Aspirational phase, referenced in the emit manifest, making
competitor placement auditable by zone membership." Tests whether: (a) a rule named
PHASE-LOCALITY RULE (or equivalent named rule) is published before the Builder Aspirational
phase begins; (b) the rule enumerates exactly three prohibited placement zones; (c) the rule
is a standalone named rule, not embedded within an operational step; (d) the emit manifest
references the rule as a required verification target. The distinction from C-36: C-36
requires each competitor to be placed at its construction step as a realized property,
verifiable by per-competitor step-tracing; C-42 requires correct placement to be governed by
a named rule with enumerated prohibited zones, making violations identifiable by zone
membership rather than by per-competitor tracing. A rubric can satisfy C-36 (all present
competitors correctly placed by inspection) while failing C-42 (no named PHASE-LOCALITY RULE
exists, placement correctness is tracing-dependent). The distinction from C-37: C-37 requires
the competitor set to be in bijection with novel criteria (cardinality constraint); C-42
requires the placement of those competitors to be governed by a named rule with enumerated
prohibited zones (locality constraint). C-37 and C-42 are orthogonal: a complete competitor
set (C-37 PASS) can be entirely in preamble (C-42 FAIL); a PHASE-LOCALITY RULE (C-42 PASS)
can govern an incomplete competitor set (C-37 FAIL). The distinction from C-27: C-27 requires
competitors to constitute gap specifications (negative-space content requirement); C-42
requires the locality of those competitors to be governed by a named rule with three enumerated
prohibited placement zones. C-27 is satisfiable with competitors in a preamble; C-42 prohibits
preamble placement by rule. Evidence: V-03 R13 names PHASE-LOCALITY RULE with three
prohibited zones before Phase 6: (1) preamble before any construction phase; (2) operating-
principles/shared block preceding more than one step; (3) combined block governing more than
one criterion; rule is standalone, referenced in emit manifest. V-05 R13 embeds the
PHASE-LOCALITY RULE as Step 2 within the Mechanism Definer role boundary -- spatially
co-located with the construction phase it governs -- with the same three prohibited zones and
emit manifest reference; V-05's treatment is preferred because the rule is encountered at the
moment the Mechanism Definer is completing, immediately before the Builder Aspirational begins,
making temporal proximity reinforce the locality constraint. V-01, V-02, V-04 R13 use PHASE
headers that enforce sequencing but state no named PHASE-LOCALITY RULE with enumerated
prohibited zones.

**C-43** (gate-satisfaction-predicate) -- The gate identifier definition uses a satisfaction
predicate form -- "GATE is satisfied when: [conditions]" -- before the exclusion terminal,
making gate passage a formally testable logical assertion rather than an inferred consequence
of scope non-violation. Without a satisfaction predicate, a gate is defined by what it
excludes: the exclusion terminal ("Nothing else." or "no additional content") closes the output
scope, and gate passage is inferred when no excluded content is present. A satisfaction
predicate inverts this inference: the passage condition is stated as a positive assertion
("both templates are present, nothing else"), making gate status checkable against the
predicate independently of scope-violation detection. An evaluator confirming a predicate
gates runs the predicate condition check; an evaluator checking an exclusion-only gate scans
for violations. Both close scope (satisfying C-40) but only the predicate form produces a
formally testable assertion at the gate site. Not "gate closes output scope by exclusion
terminal alone" but "gate definition includes 'GATE is satisfied when: [enumerated
conditions]' before the exclusion terminal, making passage a positive predicate assertion
that an evaluator can confirm without checking for scope violations." Tests whether: (a) the
gate definition uses the form "GATE is satisfied when: [conditions enumerated]"; (b) the
predicate states the passage conditions positively (what must be present and true), not
negatively (what must be absent); (c) the exclusion terminal follows the predicate as the
closure clause, confirming the scope boundary after the passage conditions are stated;
(d) the predicate form is distinct from a mere restatement of the templates -- it asserts
that the named conditions constitute gate satisfaction, not merely that the templates must be
present. The distinction from C-40: C-40 requires the gate to close the output scope by
ending with an exclusion terminal; C-43 requires the gate definition to include a satisfaction
predicate that states the passage conditions positively before the exclusion terminal. A gate
satisfies C-40 ("Nothing else." present, scope closed) while failing C-43 (no "is satisfied
when:" predicate; gate passage is inferred from exclusion, not tested against a stated
predicate). C-40 requires closure; C-43 requires formal testability. The distinction from
C-41: C-41 requires the gate identifier to propagate to the successor role's precondition for
auditable handoff; C-43 requires the gate definition to use a predicate form for formally
testable passage. C-41 governs downstream propagation; C-43 governs internal logical
structure. A gate identifier quoted verbatim in a Builder precondition (satisfying C-41) may
have an exclusion-only definition (failing C-43); a gate with a satisfaction predicate
(satisfying C-43) may not appear verbatim in any successor precondition (failing C-41). The
distinction from C-44: C-43 governs the passage condition (positive predicate asserts what
constitutes satisfaction); C-44 governs the enforcement action (embedded STOP signals the
violation consequence). Both can be present independently: a gate with "is satisfied when:"
predicate but no STOP passes C-43 and fails C-44; a gate with an embedded STOP but no
predicate form passes C-44 and fails C-43. Evidence: V-04 R14 "DEFINER OUTPUT GATE is
satisfied when: Both templates. Nothing else." -- the "is satisfied when: Both templates"
clause is the positive predicate; "Nothing else." is the exclusion terminal that follows;
gate passage is testable by predicate assertion (are both templates present?) rather than by
scope-violation scan (is anything beyond two templates present?). V-01 R14 "DEFINER OUTPUT
GATE: Two slot-fillable templates, no additional content. Nothing else." -- exclusion-only
form satisfies C-40 but fails C-43 (no "is satisfied when:" predicate; passage is inferred
from the absence of additional content beyond the two templates).

**C-44** (gate-enforcement-stop-embedded) -- A named STOP action is embedded inside the gate
definition block as part of the gate's contractual specification -- "STOP if [scope violation
condition]" appears within the gate block itself, not as a downstream audit step, a role-level
enforcement instruction, or a separate note outside the gate definition. Without an embedded
STOP, the gate's enforcement relies on the exclusion clause's contractual authority: scope
violation is a role completion failure by definition, but the enforcement mechanism is the
role's contract, not an operational signal co-located with the gate. An embedded STOP makes
the gate self-enforcing: the enforcement action is physically co-located with the gate
definition, so the reader who reads the gate encounters both the passage conditions (what
satisfies the gate) and the enforcement consequence (what happens at violation) in the same
block, without consulting the role's surrounding instructions. Not "enforcement consequence
derivable from the gate's exclusion clause by implication" but "STOP verb present inside the
gate block, specifying the scope violation condition, so that the gate block alone communicates
both passage and consequence." Tests whether: (a) a STOP action appears within the gate
definition block -- not after it, not in a surrounding role instruction, not in a separate
audit step; (b) the STOP specifies the scope violation condition explicitly ("STOP if content
beyond two templates"), not as a generic enforcement signal; (c) the embedded STOP is inside
the gate block such that an evaluator reading only the gate block encounters both the passage
conditions and the enforcement consequence; (d) the co-location makes the gate self-enforcing:
the gate block is the complete enforcement contract, not a statement that a downstream step
will enforce. The distinction from C-40: C-40 requires the gate to end with an exclusion
terminal making scope violation a role completion failure; C-44 requires a STOP verb to be
embedded inside the gate block, operationally signaling enforcement at the gate site. A gate
can satisfy C-40 (exclusion terminal present, padded output is a completion failure by
contract) while failing C-44 (no STOP inside the gate block; enforcement is contractual but
not operationally co-located). C-40 requires scope closure with failure consequence; C-44
requires the failure consequence to be operationally signaled by a STOP embedded inside the
gate. The distinction from C-43: C-43 governs the gate's passage condition form (positive
predicate stating what constitutes satisfaction); C-44 governs the gate's enforcement
mechanism (STOP embedded inside the gate block stating what constitutes violation and its
consequence). Both can be present independently: a gate with "is satisfied when: both
templates. Nothing else." passes C-43 (positive predicate) but fails C-44 if no STOP is
embedded. A gate with "Nothing else. STOP if output exceeds templates." passes C-44 (STOP
embedded) but fails C-43 (no "is satisfied when:" predicate form). V-04 R14 demonstrates the
combined form: "DEFINER OUTPUT GATE is satisfied when: Both templates. Nothing else. STOP
if content beyond two templates." -- all three elements (satisfaction predicate, exclusion
terminal, embedded STOP) co-occur in the same gate block, making the block both formally
testable (C-43) and self-enforcing (C-44). Evidence: V-01 R14 "STOP if output exceeds
templates" embedded in the gate block alongside "Nothing else." -- the STOP is inside the
gate definition, not in a surrounding role instruction; the gate block alone communicates the
enforcement consequence. V-04 R14 adds the satisfaction predicate alongside the embedded
STOP, demonstrating that C-43 and C-44 co-occur in the highest-quality gate implementation.

**C-45** (reference-anchor-stop-gated) -- The REFERENCE ANCHOR block required by C-11 is
operationally enforced by an embedded STOP: if the block is absent before ROLE: MECHANISM
DEFINER begins, or if the Falls-short field is blank, the STOP fires, making the anchor a
required gated prerequisite rather than a named section that may be present or partially
completed. Without this enforcement, the anchor requirement is contractual: the rubric names
the anchor as required (satisfying C-11) but provides no operational signal at the Mechanism
Definer boundary that fires if the anchor is missing or incomplete. With the embedded STOP,
the anchor layer is self-enforcing at the role entry point: the Mechanism Definer cannot begin
until the REFERENCE ANCHOR is present and the Falls-short field is populated. Not "REFERENCE
ANCHOR required by role instruction alone" but "REFERENCE ANCHOR enforced by STOP at the
Mechanism Definer entry boundary -- absent or Falls-short-blank anchor fires the STOP,
blocking the Mechanism Definer role from beginning." Tests whether: (a) a STOP condition
appears in the enforcement position immediately before ROLE: MECHANISM DEFINER begins;
(b) the STOP fires on two distinct failure modes -- anchor absent AND Falls-short blank --
not only on complete anchor absence; (c) the STOP is positioned at the Mechanism Definer
role boundary, not in a general preamble or post-draft audit step; (d) the STOP is co-located
with the anchor requirement, making anchor completeness a Mechanism Definer entry gate rather
than a shared preamble requirement. The distinction from C-11: C-11 requires the structured
REFERENCE ANCHOR block to be present with three named fields (Reference, Passes, Falls-short);
C-45 requires a STOP that enforces anchor completeness at the Mechanism Definer boundary,
making the anchor a gated prerequisite rather than a named section. A rubric satisfies C-11
(anchor block present, three fields named) while failing C-45 if no STOP guards the Mechanism
Definer entry against an absent or partially completed anchor. The distinction from C-44:
C-44 requires a STOP embedded inside a Definer output gate block specifying the scope violation
condition; C-45 requires a STOP at the anchor enforcement position before the Mechanism
Definer role boundary. Both apply the embedded-STOP principle to different structural layers:
C-44 governs Definer output scope; C-45 governs reference anchor completeness. A rubric
embeds a STOP inside its Definer output gate (satisfying C-44) while leaving the REFERENCE
ANCHOR unguarded at the Mechanism Definer boundary (failing C-45), or enforces anchor
completeness by STOP at the role entry (satisfying C-45) while its Definer output gate has
no embedded STOP (failing C-44). The two-criterion anchor progression -- required presence
(C-11) -> STOP-enforced presence (C-45) -- is isomorphic to the gate progression -- scope
closure (C-40) -> embedded STOP (C-44). The distinction from C-29: C-29 requires the
Mechanism Definer role to exist as a dedicated sequential role with the independence map as
its sole exit condition; C-45 requires the REFERENCE ANCHOR to be enforced as a gated
prerequisite before that role begins. C-29 governs the role's existence and exit artifact;
C-45 governs what must be verified before the role is permitted to start. Evidence: V-05 R15
PHASE 5 block contains "REFERENCE ANCHOR -- Reference: [prior version]. Passes: [C-01--C-08].
Falls-short: [aspirational dimension]. STOP if this block is absent or Falls-short is blank
before ROLE: MECHANISM DEFINER begins." -- the STOP fires on both failure modes (absent and
incomplete Falls-short field), co-located at the Mechanism Definer entry boundary, converting
the C-11 presence requirement into a gated prerequisite with two independently tested failure
conditions.

**C-46** (gate-successor-role-named) -- The gate block explicitly names the specific role
that is blocked by the gate -- "ROLE: X cannot begin until gate satisfied" -- making the
blocking dependency forward-visible from the gate definition alone: a reader of the gate
block can identify both the passage conditions (what satisfies the gate) and the specific role
that depends on gate satisfaction, without reading the successor role's entry precondition.
Without successor naming, the gate's downstream effect is known only by reading the successor
role's entry precondition (C-41 requires the successor to quote the gate verbatim). The gate
definition alone is directionally complete -- it states what must be satisfied -- but is not
forward-complete: a reader cannot determine from the gate block alone which role is waiting.
Successor naming in the gate block creates a forward-pointing reference that, combined with
C-41's backward-pointing reference (successor quotes gate identifier verbatim), forms a closed
bidirectional loop: gate -> successor (C-46) and successor -> gate (C-41). Not "gate states
passage conditions and STOP enforcement" but "gate definition explicitly names the successor
role that is blocked, so that the gate block alone communicates the dependency topology -- who
must satisfy this gate before proceeding -- without reading the successor's entry precondition."
Tests whether: (a) the gate block contains a named successor role reference in the form
"ROLE: X cannot begin until gate satisfied" or equivalent explicit naming; (b) the named role
is the specific immediate successor in the construction workflow, not a generic label;
(c) the naming appears inside the gate block itself, not in a surrounding role instruction or
separate handoff note; (d) the successor naming is explicit enough that a reader of only the
gate block can identify which role is blocked without reading any other role definition.
The distinction from C-41: C-41 requires the Builder Aspirational role's entry precondition
to quote the gate identifier verbatim (successor -> gate: pull reference from successor to
gate); C-46 requires the gate block itself to name the successor role that is blocked
(gate -> successor: push reference from gate to successor). The two criteria are orthogonal:
a gate satisfying C-41 (gate identifier quoted in Builder precondition) may not name its
consumer inside the gate block (failing C-46); a gate that names its consumer inside the gate
block (satisfying C-46) may not be quoted verbatim in the consumer's entry precondition
(failing C-41). Together, C-41 + C-46 close the bidirectional reference loop: the gate names
the successor and the successor names the gate, making the inter-role dependency traceable
from either definition alone. The distinction from C-43: C-43 requires the gate to state its
passage conditions as a positive predicate ("is satisfied when: [conditions]"), governing the
internal logical structure of the passage condition; C-46 requires the gate to name the
successor role that is blocked, governing the forward-facing dependency declaration. Both
concern gate completeness but govern independent properties: passage-condition form (C-43)
vs dependency topology (C-46). A gate states "is satisfied when: both templates. Nothing
else." (C-43 PASS) without naming its consumer (C-46 FAIL); a gate states "ROLE: BUILDER
ASPIRATIONAL cannot begin until gate satisfied" (C-46 PASS) without a positive predicate form
(C-43 FAIL). The distinction from C-40: C-40 requires the gate to end with an exclusion
terminal closing the output scope; C-46 requires the gate to name the successor role that
depends on gate satisfaction. A gate can close scope (C-40 PASS) without naming its consumer
(C-46 FAIL); a gate can name its consumer (C-46 PASS) without a terminal exclusion clause
(C-40 FAIL). The distinction from C-44: C-44 requires a STOP verb embedded inside the gate
block specifying the violation consequence; C-46 requires the gate block to name the specific
successor role that is blocked by default. C-44 governs enforcement action co-location;
C-46 governs consumer identity declaration. Evidence: V-05 R15 MECHANISM DEFINER GATE block
reads "MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated.
ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied." -- the successor role
is named explicitly inside the gate block, making the dependency forward-visible: a reader
of the gate definition knows that ROLE: BUILDER ASPIRATIONAL is the specific role blocked.
Combined with C-41 (ROLE: BUILDER ASPIRATIONAL entry quotes "MECHANISM DEFINER GATE" verbatim),
the bidirectional reference loop is closed: gate names successor (C-46 PASS) and successor
names gate (C-41 PASS).

**C-47** (anchor-successor-role-named) -- The REFERENCE ANCHOR block names the specific consumer
role that depends on anchor satisfaction -- "Consumer: ROLE: MECHANISM DEFINER" or equivalent
explicit naming -- making the anchor's downstream dependency forward-visible from the anchor block
alone: a reader of the anchor block can identify both what the anchor requires (Reference, Passes,
Falls-short) and which role depends on anchor completeness, without reading the Mechanism Definer's
entry precondition. Without consumer naming, the anchor's downstream effect is known only by
reading the Mechanism Definer's entry precondition (C-41 requires the successor to quote the gate
verbatim; C-45 positions the anchor STOP at the role boundary) -- the anchor block itself declares
what exists but not who waits on it. Consumer naming in the anchor block creates a forward-pointing
declaration that, combined with C-45's backward-enforcement relationship (anchor STOP fires at
the Mechanism Definer entry boundary -- the consumer is blocked by the anchor), closes a
bidirectional anchor dependency: anchor names consumer (C-47: declaration direction) and consumer
is blocked by anchor STOP (C-45: enforcement direction). The pair is isomorphic to C-41 + C-46
at the gate layer: C-47 mirrors C-46 (anchor declares consumer, as gate declares successor) and
C-45 mirrors the STOP-enforcement relationship (anchor STOP blocks consumer entry, as C-44's
embedded STOP makes gate violation a completion failure). Not "anchor block states three required
fields (Reference, Passes, Falls-short)" but "anchor block explicitly names the consumer role
that depends on anchor satisfaction -- the anchor declaration includes who is waiting, making the
downstream dependency topology derivable from the anchor block alone without reading the
Mechanism Definer's precondition." Tests whether: (a) the REFERENCE ANCHOR block contains a
Consumer field or equivalent named declaration identifying the specific consumer role (e.g.,
"Consumer: ROLE: MECHANISM DEFINER"); (b) the named role is the specific role whose entry is
blocked by the anchor STOP (C-45), not a generic label; (c) the consumer naming appears inside
the anchor block itself, not in a surrounding role instruction or separate handoff note; (d) the
consumer declaration is explicit enough that a reader of only the anchor block can identify which
role depends on anchor completion without reading any other role definition. The distinction from
C-46: C-46 requires the gate block to name the specific successor role that is blocked ("ROLE: X
cannot begin until gate satisfied" -- gate -> successor: push reference from gate to successor);
C-47 requires the REFERENCE ANCHOR block to name the specific consumer role that depends on anchor
satisfaction (anchor -> consumer: push reference from anchor to consumer). Both are push references
making a dependency forward-visible from the declaring block; they govern different structural
layers. A rubric satisfying C-46 (gate names successor) while its anchor block contains no
Consumer field fails C-47; a rubric satisfying C-47 (anchor names consumer) while its gate block
names no successor fails C-46. The distinction from C-45: C-45 requires a STOP at the Mechanism
Definer entry boundary enforcing anchor completeness -- the enforcement direction, where the anchor
controls whether the consumer can begin; C-47 requires the anchor block to name the consumer role
-- the declaration direction, where the anchor identifies its consumer. C-45 governs what happens
at the consumer's entry boundary; C-47 governs what the anchor block declares about its consumer.
Confirmed independently satisfiable: V-03 (C-46 ablated, C-41 PARTIAL) passes C-47; V-04
(C-46 absent, C-41 FAIL) passes C-47; both demonstrate C-47 does not depend on C-46 or C-41.
The distinction from C-11: C-11 requires the REFERENCE ANCHOR block to be present with three
named fields (Reference, Passes, Falls-short); C-47 requires the anchor block to additionally
name its consumer role. A rubric satisfies C-11 (three-field block present) while failing C-47
if no Consumer field or equivalent declaration names the dependent role. C-11 requires anchor
presence and structural completeness; C-47 requires the anchor to declare its downstream consumer,
adding a fourth structural element to the anchor block. The distinction from C-41: C-41 requires
the Builder Aspirational role's entry precondition to quote the Mechanism Definer gate identifier
verbatim (successor -> gate: pull reference from successor back to gate); C-47 requires the anchor
block to name the Mechanism Definer as the anchor's consumer (anchor -> consumer: push reference
from anchor forward to its consumer). C-41 governs identifier propagation in the entry precondition
of the successor role; C-47 governs consumer-role declaration in the body of the anchor block.
A rubric satisfies C-41 (gate identifier quoted verbatim in Builder precondition) while failing
C-47 if the anchor block has no Consumer field; V-03 satisfies C-47 with C-41 PARTIAL, confirming
independent satisfiability. Evidence: V-05 R17 REFERENCE ANCHOR block reads "Reference: [prior
version]. Passes: [C-01--C-08]. Falls-short: [aspirational dimension]. Consumer: ROLE:
MECHANISM DEFINER." -- the Consumer field names the specific role that depends on anchor
satisfaction, making the anchor's downstream dependency forward-visible from the anchor block
alone. V-03 R17 (C-46 ablated) and V-04 R17 (C-46 absent, C-41 FAIL) both satisfy C-47,
confirming that consumer naming in the anchor block is structurally orthogonal to successor
naming in the gate block (C-46) and gate-identifier quoting in the Builder precondition (C-41).
Three-variation confirmation across V-03, V-04, V-05 establishes structural stability.

---

## Scoring

```
Essential:    (C-01 + C-02 + C-03 + C-04 + C-05) x 12            max 60
Recommended:  (C-06 + C-07 + C-08) / 3 x 30                       max 30  (partials = 0.5)
Aspirational: (C-09 through C-47) / 39 x 10                        max 10  (partials = 0.5)

Composite = Essential + Recommended + Aspirational                  max 100
Golden threshold: >= 90
```

**Scoring note:** The aspirational denominator shifts from `/38` to `/39` to reflect the
addition of C-47.

*Round 17 ceiling recalibration.* Under v17 (/39 denominator): V-05 R17 passes 37 criteria
-- all 37 of C-09--C-37, C-40--C-47 (C-38 FAIL: C-37 not novel in R17; C-39 FAIL: no
Tier-Blind Categorizer competitor at the category-distribution verification step). Total:
37/39 x 10 = 9.487 aspirational, composite 99.49. Path to 100 under v17: C-39 must be
satisfied (Tier-Blind Categorizer competitor placed inline at Phase 4.5 divergence-check
step, constituting the gap specification for the operationalization requirement).

*Round 15 ceiling preserved.* Under v16 (/38 denominator): V-05 R15 (Full Five-Gate
Stack + Inertia Framing) passes all 38 criteria -- C-11 PASS (REFERENCE ANCHOR block with
STOP if absent or Falls-short blank, positioned before ROLE: MECHANISM DEFINER), C-29 PASS
(formal ROLE boundary, sole output = independence map, MECHANISM DEFINER GATE as exit
condition, BUILDER ASPIRATIONAL named as blocked successor), C-40--C-44 PASS (full five-gate
stack), C-45 PASS (anchor STOP enforced at Mechanism Definer boundary), C-46 PASS (gate
names BUILDER ASPIRATIONAL as blocked successor role). Total: 38/38 x 10 = 10, composite 100.
First composite 100 confirmed in R15. Under v17 (/39): V-05 R15 = 38/39 x 10 = 9.744
aspirational (C-47 not present in R15), composite 99.74.

*Prior round preserved for denominator context.* Under v15 (/36 denominator): V-04 R14
(Three-Gate Stack, C-11 ablated) passes C-40--C-44; C-11 ablated; 30 inherited
(C-09--C-10, C-12--C-39). Total: 35/36 x 10 = 9.722 aspirational, composite 99.722.

*C-43 closes the gate formal-testability gap.* C-40 requires scope closure via an exclusion
terminal; C-43 requires the gate to state its passage conditions as a positive predicate. The
two criteria are ordered but independent: C-43 requires a gate (which C-40's exclusion terminal
provides), but C-40 does not require the gate to state passage conditions in predicate form.
The upgrade is from scope closure by exclusion (passage inferred from non-violation) to formal
testability by predicate (passage confirmed by predicate assertion). V-04 R14's "is satisfied
when:" clause is the realization form: the predicate makes the gate's passage condition
separately testable, elevating the gate from a contractual boundary to a logical assertion
that an evaluator can verify without scanning for violations. The predicate-first form --
"satisfied when [positive conditions]. Nothing else." -- is preferred over exclusion-first
form -- "Nothing else. No additional content." -- because the predicate states what constitutes
passage before the exclusion states what constitutes violation, making both conditions
explicit and independently verifiable.

*C-44 closes the gate self-enforcement gap.* C-40 requires the gate to make scope violation
a role completion failure; C-44 requires the enforcement action (STOP) to be co-located
inside the gate block. The distinction is between contractual consequence (violation is a
completion failure by role contract, enforced by downstream audit) and operational co-location
(STOP inside the gate block makes enforcement immediate, without depending on a downstream
audit step to catch and signal the failure). V-01 R14 demonstrates STOP inside gate without
the satisfaction predicate; V-04 R14 demonstrates both STOP and predicate in the same gate
block. The co-location principle: the gate block is the complete enforcement contract -- a
reader who reads only the gate block encounters passage conditions, exclusion terminal, and
enforcement consequence. Any enforcement element outside the gate block creates a dependency
between the gate and its environment that the embedded STOP eliminates.

*C-43, C-44 extend the gate quality progression.* C-19/C-20 govern Definer output content
and register; C-40 extends to scope (output instruction closes via exclusion gate); C-43
extends scope closure to formal predicate testability; C-44 extends to gate self-enforcement.
The four-step gate quality progression -- (1) gate closes scope [C-40], (2) gate states
passage conditions as positive predicate [C-43], (3) gate embeds enforcement action [C-44],
and (4) gate identifier propagates to successor role's entry precondition [C-41] -- describes
a complete gate contract: scope is closed, passage is formally testable, enforcement is
self-contained, and the gate identifier chains to the next role boundary. A rubric satisfying
C-40 through C-44 has gates that are closed, formally verifiable, self-enforcing, and
auditably chained to their successor roles.

*C-45, C-46, C-47 complete the cross-layer dependency model.* C-45 applies the embedded-STOP
principle (C-44) to the reference anchor layer: the REFERENCE ANCHOR (C-11) is not merely
a named section requirement but a gated prerequisite enforced by STOP at the Mechanism
Definer entry boundary, with two independently tested failure conditions (absent and
Falls-short blank). C-46 adds a forward-facing dependency declaration to the gate contract:
the gate block names its immediate successor, closing the bidirectional reference loop with
C-41 (successor quotes gate) and making the inter-role dependency traceable from either
definition alone. C-47 adds the parallel forward-facing declaration to the anchor block:
the anchor names its consumer role (ROLE: MECHANISM DEFINER), closing a bidirectional anchor
dependency with C-45 (anchor STOP blocks the consumer's entry), and making the anchor's
downstream topology derivable from the anchor block alone. Together, C-45 + C-46 + C-47
complete the cross-layer enforcement and topology model: the anchor layer is STOP-enforced
(C-45), the anchor names its consumer (C-47), and the gate layer is bidirectionally named
(C-41 + C-46). The three-criterion anchor progression -- required presence [C-11] -> STOP-
enforced presence [C-45] -> consumer role named [C-47] -- is fully isomorphic to the gate
progression: scope closure [C-40] -> embedded STOP [C-44] -> successor role named [C-46].
The full quality progression is now seven-dimensional: scope closure [C-40] -> formal
predicate [C-43] -> embedded STOP [C-44] -> identifier propagation to successor [C-41] ->
successor role named in gate [C-46] -> anchor STOP at role entry [C-45] -> anchor names
consumer role [C-47].
