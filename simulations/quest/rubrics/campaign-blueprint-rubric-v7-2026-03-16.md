v7 written. Here's the summary of what changed:

---

## v7 changes

**Two new aspirational criteria (+10 pts, new ceiling 168):**

**C-25 — Scout traceability table** (5 pts): C-24 tests whether must-have citations *exist*; C-25 tests whether they take the form of a *dedicated labeled table* (Req-ID / Must-have / Originating Friction / Scout File). Table form is row-by-row auditable vs. general instruction. V-02 and V-05 earn FULL; others earn NO CREDIT.

**C-26 — Named inertia model entity** (5 pts): C-23 tests whether conviction types are *grounded* in the inertia baseline; C-26 tests whether the baseline is declared as a *named, multi-field entity* (Name / Behavior / Cost) with explicit field-to-conviction-type mapping. V-03 and V-05 earn FULL; others earn NO CREDIT.

**One new diagnostic rule:**

**D8**: C-23 FULL requires inertia-grounded phrasing at BOTH the matrix AND per-site execution reminders. Matrix-only grounding with abstract per-site labels earns PARTIAL (V-01 R6 finding).

**Retroactive R6 under v7:**

| Variant | v6 | C-25 | C-26 | v7 |
|---------|-----|------|------|-----|
| V-01 | 155.5 | 0 | 0 | **155.5** |
| V-02 | 158 | +5 | 0 | **163** |
| V-03 | 158 | 0 | +5 | **163** |
| V-04 | 153 | 0 | 0 | **153** |
| V-05 | 158 | +5 | +5 | **168** |

V-05 alone reaches 168. V-02 and V-03 tie at 163, each holding one of the two new mechanisms. The two patterns are architecturally separable — a future variant combining both without V-05's full convergence is the expected R7 design space.
 CREDIT.

**One new diagnostic rule:**

**D8 (v7)**: C-23 full credit requires inertia-grounded conviction type labels at BOTH the campaign-level matrix AND the per-artifact execution-site reminders. Matrix-only inertia grounding is insufficient — the per-site reminder is the proximal instruction at execution time, and abstract labels at per-site level sever the grounding at the moment the model produces the artifact. A campaign that declares inertia-grounded CONVICTION TYPE in the matrix but reverts to abstract labels (e.g., "Factual — assert what is true") in per-site reminders earns C-23 PARTIAL (V-01 R6 finding).

**Scale:** 160 base + 8 excellence = **168 ceiling**

**Retroactive R6 scoring** under v7 differentiates variants where v6 produced a three-way tie at 158:

| Variant | R6 Total (v6) | C-25 | C-26 | Total (v7) |
|---------|--------------|------|------|------------|
| V-01 — Per-site Abstract Labels | 155.5 | 0 | 0 | **155.5** |
| V-02 — Scout Traceability Table | 158 | +5 | 0 | **163** |
| V-03 — Named INERTIA MODEL Entity | 158 | 0 | +5 | **163** |
| V-04 — Minimal Density | 153 | 0 | 0 | **153** |
| V-05 — Full Convergence | 158 | +5 | +5 | **168** |

V-05 alone reaches the v7 ceiling. V-02 and V-03 tie at 163 — each implements one of the two new criteria but not both. V-01's matrix-only inertia grounding already cost it C-23 PARTIAL under v6; it gains nothing under v7. V-04's minimum-density approach continues to fall short of both new criteria.

---

## Essential

| ID | Criterion | Weight |
|----|-----------|--------|
| C-01 | All three artifacts produced | 12 |
| C-02 | Canonical paths | 12 |
| C-03 | Topic identity consistency | 12 |
| C-04 | Execution order | 12 |
| C-05 | Minimum structure per sub-artifact | 12 |

**Essential total: 60**

---

## Recommended

| ID | Criterion | Weight |
|----|-----------|--------|
| C-06 | Proposal respects spec | 10 |
| C-07 | Pitch crystallizes recommended option | 10 |
| C-08 | Campaign framing — campaign opens with setup summary, closes with package summary | 10 |

**Recommended total: 30**

---

## Aspirational

| ID | Criterion | Weight |
|----|-----------|--------|
| C-09 | Narrative arc — each artifact amplifies conviction without repeating content | 5 |
| C-10 | Scout signal pull is visible in the artifact that benefits from it | 5 |
| C-15 | Artifact contract — each artifact declares READ / WRITE / PRESERVE / CARRIES FORWARD before execution begins | 5 |
| C-16 | Post-execution FINDINGS block — pitch contains a labeled post-execution audit block, not a pre-execution intent declaration or checklist | 5 |
| C-17 | Dual-mechanism defense in depth — pre-execution contract with all four labeled fields AND a named FINDINGS template with explicit sub-fields | 5 |
| C-18 | Double-prohibition FINDINGS placement — instruction explicitly prohibits both "before" and "during" writing, not only "after" | 5 |
| C-19 | Structural double-prohibition — double-prohibition encoded as a named phase boundary condition, not as an instruction clause | 5 |
| C-20 | Contract proximity anchoring — per-artifact inline contract reminder restates READ and PRESERVE at each execution site | 5 |
| C-21 | Conviction typing — each artifact carries a declared CONVICTION TYPE label; post-execution audit block is typed to the pitch's conviction role | 5 |
| C-22 | Per-site conviction type restatement — per-artifact contract reminder restates READ, PRESERVE, and CONVICTION TYPE at each execution site | 5 |
| C-23 | Inertia-anchored conviction arc — conviction types are grounded in the competitive baseline, naming what the status quo produces at each conviction stage | 5 |
| C-24 | Scout-to-must-have traceability — each spec Must-have explicitly cites the scout-requirements friction that justifies its inclusion | 5 |
| C-25 | Scout traceability table — the must-have-to-friction citations are structured as a dedicated labeled table with explicit columns, not embedded in prose or encoded as a general instruction | 5 |
| C-26 | Named inertia model entity — the inertia baseline is declared as a named, multi-field structural entity with explicit field-to-conviction-type mapping, not as an inline sentence or compact label | 5 |

**Aspirational total: 70**

---

## Excellence Signals — added in v2

These criteria emerged from Round 1 analysis. They distinguish the 90+
performers from the passing tier. Scored as a bonus above the 160-pt base.

| ID | Criterion | Weight |
|----|-----------|--------|
| C-11 | Hard GATE per transition — explicit "do not begin [next artifact] until [this file] is written to disk" at both transitions | 2 |
| C-12 | Proactive scout inventory — setup phase globs simulations/scout/ and lists found signals before Artifact 1 begins; not conditional | 2 |
| C-13 | Conviction audit in pitch — FINDINGS block explicitly asks "what conviction does this version add that the previous artifacts did not" AND "note any content you nearly duplicated" | 2 |
| C-14 | Signal consumption log — campaign close records per artifact which scout namespace was consumed, not just artifact paths | 2 |

**Excellence bonus: 8**
**Scale: 160 base + 8 excellence = 168 ceiling**

---

## Scoring

```
Essential    = sum of passed essential criteria x 12        (max 60)
Recommended  = sum of passed/partial recommended x weight   (max 30)
Aspirational = sum of passed/partial aspirational x weight  (max 70)
Excellence   = sum of passed excellence signals x 2        (max 8, bonus)

Composite = Essential + Recommended + Aspirational + Excellence
```

PARTIAL = 50% of the criterion weight.

---

## Golden Threshold

**Pass**: All 5 essential criteria pass **AND** composite >= 80

Failure on any essential criterion disqualifies regardless of composite score.

---

## Failure Patterns

| Pattern | Criteria at risk |
|---------|-----------------|
| Partial campaign (missing artifact) | C-01, C-02 |
| Topic drift across artifacts | C-03 |
| Out-of-order contamination | C-04 |
| Thin sub-artifact (missing required sections) | C-05 |
| Proposal re-opens spec decisions | C-06 |
| Pitch not anchored to recommended option | C-07 |
| No campaign framing (no setup, no close) | C-08 |
| Repetition without conviction build | C-09 |
| Scout signals cosmetic or absent | C-10 |
| Soft ordering language instead of GATE | C-11 |
| Scout inventory conditional or deferred | C-12 |
| Pitch lacks conviction audit | C-13 |
| Campaign close has no per-artifact signal record | C-14 |
| Inter-artifact obligations implicit rather than declared | C-15 |
| Conviction reflection pre-execution or unlabeled | C-16 |
| Only one mechanism (contract or template) uses structured form | C-17 |
| FINDINGS prohibits only "before" -- "during" not prohibited | C-18 |
| Double-prohibition stated as clause, not enforced as phase boundary | C-19 |
| Contract obligations declared globally only, not at execution site | C-20 |
| Conviction roles implicit; post-execution audit not typed to role | C-21 |
| Per-site reminder omits CONVICTION TYPE -- READ and PRESERVE only | C-22 |
| Conviction types abstract labels without inertia-baseline grounding | C-23 |
| Scout pull unidirectional; must-haves do not cite originating friction | C-24 |
| Must-have citations embedded in prose or instruction, not in a labeled table | C-25 |
| Inertia baseline declared as inline sentence or compact label, not as named entity | C-26 |

---

## Criterion Detail

### C-01: All three artifacts produced

All three sub-skills must run and produce output: draft-spec, draft-proposal,
draft-pitch. Two out of three fails this criterion regardless of artifact
quality.

### C-02: Canonical paths

- spec:     `simulations/draft/specs/{topic}-spec-{date}.md`
- proposal: `simulations/draft/proposals/{topic}-proposal-{date}.md`
- pitch:    `simulations/draft/pitches/{topic}-pitch-{date}.md`

Abbreviated, renamed, or wrong-directory paths fail this criterion.

### C-03: Topic identity consistency

A shared identity contract -- feature name, audience, problem -- must be
established once and held by all three artifacts. Artifacts that each define
the topic independently risk drift. The best implementations lock identity
in a dedicated setup phase before Artifact 1 begins (see also C-12).

### C-04: Execution order

Proposal must be grounded in the spec. Pitch must be anchored to the
proposal's recommended option. Forward references -- pitch language that
pre-supposes spec content before the spec is written -- fail this criterion.
Soft dependency language ("grounded in," "read the spec") passes C-04.
Explicit GATE language is scored separately as C-11.

### C-05: Minimum structure per sub-artifact

- **Spec**: PURPOSE / REQUIREMENTS / DESIGN / CONSTRAINTS / OPEN QUESTIONS
- **Proposal**: Three options minimum + do-nothing baseline; each option with
  description, pros, cons, risk, effort; recommendation with three reasons
  grounded in spec decisions
- **Pitch**: Three versions (exec / dev / maker); each with Hook / What / Why /
  CTA; shared anti-positioning section

All sub-conditions within each artifact must be present for a full PASS.

### C-06: Proposal respects spec

Recommendation reasons must trace to spec decisions or constraints. The
proposal must not re-open design questions the spec resolved or introduce
new design work. Explicit instruction ("do not re-open anything the spec
resolved") earns full credit; reasoning that happens to be grounded but lacks
the instruction is PARTIAL. The artifact contract PRESERVES declaration (C-15)
is the strongest formulation of this criterion seen across all rounds.

### C-07: Pitch crystallizes recommended option

All three sub-conditions must pass for full credit:
- Exec version: leads with outcome of the recommended option
- Dev version: explicitly references the technical design from the spec
- Maker version: plain language only -- no spec terminology, no proposal jargon

Missing or implicit dev-version spec reference is the most common partial.
The artifact contract CARRIES FORWARD declaration (C-15) makes this criterion
structurally enforced rather than implied.

### C-08: Campaign framing

- **Open**: Names the topic and states which artifacts will be produced
- **Close**: Lists all three artifact paths, scout signals consumed, open
  questions

A close that lists artifacts but omits signal consumption is PARTIAL (see
C-14 for the excellence version of this criterion).

### C-09: Narrative arc (aspirational)

Each artifact advances the audience's conviction without rehashing prior
content. Role differentiation (spec -> proposal -> pitch) is a natural scaffold
but is not sufficient alone -- the criterion requires either explicit scope
separation language or an anti-duplication instruction. The post-execution
FINDINGS block (C-16) is the primary implementation mechanism; the conviction
audit content (C-13) is the excellence version. Conviction typing (C-21)
is the strongest abstract implementation: declared roles make repetition
diagnostically detectable rather than subjectively assessed. Inertia-anchored
conviction typing (C-23) is the most operationally precise implementation,
grounding each artifact's role in a specific claim about the status quo.

### C-10: Scout signal pull (aspirational)

Scout signals must be visibly pulled into the artifact that benefits from them:
- scout-requirements -> spec
- scout-feasibility -> proposal
- scout-positioning -> pitch

Cosmetic mention without integration is PARTIAL. A conditional pull ("if
scout signals exist...") passes C-10 but does not satisfy C-12. Labeled
bidirectional traceability (each must-have cites its originating scout
friction) is the strongest implementation; see C-24. The table form of
bidirectional traceability, which makes the linkage row-by-row auditable,
is tested separately as C-25.

---

### C-15: Artifact contract (aspirational) -- added in v3

Before execution begins, each artifact declares its obligations as a formal
contract with four fields:

- **READ**: which prior artifact(s) and scout signals this artifact consumes
- **WRITE**: canonical path and required sections this artifact produces
- **PRESERVE**: spec decisions this artifact must not re-open or contradict
- **CARRIES FORWARD**: content or decisions subsequent artifacts must inherit

A contract that includes all four fields for all three artifacts earns full
credit. A contract present but missing one field type (e.g., no CARRIES
FORWARD) is PARTIAL. Narrative instructions that imply the same obligations
without declaring them as a contract do not satisfy C-15.

**v5 superset rule (D4)**: A contract matrix with more than the four required
fields (e.g., adding CONVICTION TYPE as a fifth field) earns C-15 full credit
provided all four required fields are present. Extra fields do not cause
confusion or partial scoring.

**R3 diagnostic**: Format (matrix vs per-artifact inline) does not determine
the result -- completeness of pre-execution declaration does. The cascade design
(V-03, V-05 R3) earns PARTIAL because WRITE is not a labeled contract field (a
write instruction in the body signals an action, not an obligation) and CARRIES
FORWARD is declared post-execution rather than pre-execution. Both gaps cause
PARTIAL regardless of C-07 compliance.

### C-16: Post-execution FINDINGS block (aspirational) -- added in v3

The pitch must close with a labeled audit block that is post-execution:
written after the artifact is produced, not declared before it.

The label and post-execution placement are structural requirements. Two common
variations that do not satisfy C-16:
- **Pre-execution intent declaration** ("BEFORE WRITING -- conviction
  architecture"): asks the right questions but pre-supposes the artifact
  rather than reflecting on it. Earns PARTIAL.
- **Pre-flight checklist items**: contain the right semantic content but as
  verification boxes, not as narrative reflection. Earns PARTIAL.

Both variations earn PARTIAL (2.5 pts) when the semantic content of the
conviction audit is present. A labeled audit block with both conviction
questions post-execution earns full credit (5 pts).

**v5 functional equivalence rule (D5)**: Any labeled, post-execution audit
block satisfies C-16 regardless of exact block name. "CONVICTION DELTA,"
"FINDINGS," "POST-EXECUTION REVIEW," and similar names all qualify provided
the label is present and the block is written after the artifact. An unlabeled
post-execution reflection does not satisfy C-16. This resolves the V-03 (R4)
ambiguity -- CONVICTION DELTA earns C-16 FULL credit.

**R3 diagnostic**: Both open-prompt and named sub-field template earn C-16 FULL
when the label and post-execution instruction are explicit. The template
advantage is C-13 reliability and C-17/C-18 assurance -- named sub-fields make
pre-execution placement structurally difficult -- but a template is not required
for C-16 full credit.

Relationship to other criteria:
- C-09 (aspirational): whether narrative separation exists
- C-13 (excellence): what the FINDINGS block asks -- requires C-16 block
  structure to be in place to earn full credit
- C-17 (aspirational): whether the template form of C-16 is paired with the
  labeled contract form of C-15
- C-18 (aspirational): whether the FINDINGS placement instruction explicitly
  prohibits both "before" and "during"

---

### C-17: Dual-mechanism defense in depth (aspirational) -- added in v4

The campaign employs both structural mechanisms in their strongest form:

1. **Pre-execution contract** -- all four labeled fields (READ / WRITE /
   PRESERVE / CARRIES FORWARD) for all three artifacts, declared before
   Artifact 1 begins. This is C-15 at full credit.
2. **Named FINDINGS template** -- the post-execution audit block uses explicit
   named sub-fields (e.g., CONVICTION DELTA, NEAR-DUPLICATE CONTENT) rather
   than an open prompt. Named sub-fields make it structurally difficult to
   satisfy the audit with a pre-execution declaration and improve C-13
   assurance.

Neither mechanism alone earns C-17. A campaign with a contract matrix but
open-prompt FINDINGS earns PARTIAL. A campaign with a named FINDINGS template
but per-artifact inline contracts that are incomplete earns PARTIAL. Full
credit requires both mechanisms fully present.

V-04 (R3) is the reference implementation.

Relationship to C-15 and C-16: C-17 tests the combination, not either
mechanism alone. A campaign can earn full C-15 and full C-16 without earning
full C-17 (e.g., contract matrix + open-prompt FINDINGS: full C-15, full C-16,
C-17 PARTIAL).

### C-18: Double-prohibition FINDINGS placement (aspirational) -- added in v4

The FINDINGS placement instruction explicitly prohibits both timing violations:

- "not before" -- do not write this block before the artifact is produced
- "not during" -- do not write this block while producing the artifact; wait
  until production is complete

The standard C-16 instruction ("write this block after the pitch file is
written") ensures post-execution placement but leaves open a second failure
mode: reflection written concurrently with the artifact. Concurrent writing
contaminates the post-execution nature of the reflection.

Full credit: instruction explicitly contains both "not before" and "not during"
(or equivalent double prohibition language).
Partial (2.5 pts): instruction prohibits only one timing violation (typically
"not before") -- "not during" absent.
No credit: placement is implicit, declarative, or stated only as intent.

Relationship to C-16 and C-19: C-16 tests whether the block is labeled and
post-execution. C-18 tests whether the placement instruction explicitly closes
both pre-execution and concurrent writing as failure modes. C-19 tests whether
the double-prohibition is enforced structurally rather than stated verbally. A
campaign can earn full C-16 and full C-18 without earning full C-19.

---

### C-19: Structural double-prohibition (aspirational) -- added in v5

The double-prohibition (not before, not during) is encoded as a named phase
boundary condition rather than as an instruction clause. A campaign with a
distinct `CAMPAIGN REFLECTION` phase -- or equivalent named phase -- that begins
only after the pitch artifact is written to disk makes the prohibition
structural: the model cannot enter the FINDINGS phase before completing the
artifact any more than it can skip a phase gate.

V-01 (R4) is the reference implementation. The phase-gate structure means the
prohibition does not depend on the model remembering a constraint clause; it
depends on the model following phase sequence, which is a simpler and more
reliable behavior.

Full credit: double-prohibition enforced as a named phase boundary that is
explicitly sequenced after artifact completion; the phase name and sequencing
constraint are both present.
Partial (2.5 pts): named phase exists but sequencing is soft ("after the pitch
is written" without hard gate language) -- or: double-prohibition stated as an
inline instruction clause (C-18 satisfied but prohibition is still
clause-dependent).
No credit: no phase structure; prohibition is implicit or unstated.

Relationship to C-18: C-18 tests the text of the prohibition. C-19 tests the
enforcement mechanism. A campaign can earn full C-18 (explicit "not before, not
during") while earning only C-19 PARTIAL (prohibition is a clause, not a phase
gate).

### C-20: Contract proximity anchoring (aspirational) -- added in v5

The global pre-execution contract (C-15) declares all obligations before
execution begins. Proximity anchoring goes further: at each artifact's
execution site, an inline contract reminder restates the artifact's READ and
PRESERVE obligations. This reduces the cognitive distance between declaration
and enforcement, most directly strengthening C-06 PRESERVE compliance for the
proposal and C-07 CARRIES FORWARD compliance for the pitch.

V-02 (R4) is the reference implementation. The pattern: global matrix
declares all obligations; each artifact section opens with a `Contract
reminder -- READ: ... | PRESERVE: ...` line that mirrors the matrix entry.

Full credit: each of the three artifacts carries an inline reminder with at
minimum READ and PRESERVE stated.
Partial (2.5 pts): only some artifacts carry a reminder, or the reminder is
incomplete (e.g., READ only; PRESERVE absent).
No credit: obligations appear only in the global matrix with no per-site
reinforcement.

Relationship to C-15: C-15 tests whether the global contract exists with all
four fields. C-20 tests whether the obligations are restated at execution
sites. A campaign can earn full C-15 without earning C-20.

Relationship to C-22: C-20 tests whether READ and PRESERVE are restated
per-site (two fields). C-22 tests whether CONVICTION TYPE is additionally
restated per-site (three fields). A campaign that earns full C-20 with only
two-field reminders earns no credit for C-22. A campaign that earns full C-22
automatically earns full C-20.

### C-21: Conviction typing (aspirational) -- added in v5

Each artifact carries a declared CONVICTION TYPE label that names its role in
the narrative arc (e.g., Factual for spec, Optionality for proposal, Emotional
for pitch). The post-execution audit block is typed to the pitch's declared
conviction type -- asking "what conviction of type [X] does this pitch add that
spec and proposal did not?" rather than asking an open-ended conviction
question.

V-03 (R4) is the reference implementation. Conviction typing makes C-09
structurally testable: if each artifact declares a conviction type, duplication
is detectable (did this artifact deliver its declared type, or did it repeat
the prior artifact's type?). The CONVICTION DELTA audit question sharpens C-13
from an open audit to a typed diagnostic.

Full credit: all three artifacts carry a CONVICTION TYPE label AND the
post-execution audit block is typed to the pitch's conviction type.
Partial (2.5 pts): only some artifacts are labeled, or the post-execution block
does not reference the declared type.
No credit: conviction roles are implicit or undeclared; no typed audit.

Relationship to C-09 and C-13: C-09 tests whether conviction builds without
repetition; C-21 tests whether each artifact's conviction role is declared and
audited against type. C-13 tests whether the audit asks the right questions;
C-21 tests whether those questions are typed to the declared role. A campaign
can earn full C-09 and full C-13 without earning C-21 (e.g., strong narrative
arc with open-prompt FINDINGS but no conviction type labels).

Relationship to C-23: C-21 tests whether conviction types are declared. C-23
tests whether those types are grounded in the inertia baseline. A campaign can
earn full C-21 with abstract type labels without earning C-23. A campaign that
earns full C-23 automatically earns full C-21.

---

### C-22: Per-site conviction type restatement (aspirational) -- added in v6

The per-artifact contract reminder (C-20) is extended to a three-field form:
READ, PRESERVE, and CONVICTION TYPE are all restated at each artifact's
execution site. C-20 closes the distance between the global READ and PRESERVE
declarations and their enforcement moments; C-22 closes the same distance for
the conviction type obligation -- ensuring the declared conviction role is
visible at the moment of artifact execution, not only in the global contract.

V-01 (R5) is the reference implementation. The pattern: each artifact header
carries `Contract reminder -- READ: ... PRESERVE: ... CONVICTION TYPE: ...` --
all three obligations restated at the site where execution begins.

Full credit: each of the three artifacts carries an inline reminder with READ,
PRESERVE, and CONVICTION TYPE all stated.
Partial (2.5 pts): only some artifacts carry a three-field reminder, or the
reminder includes READ and PRESERVE but omits CONVICTION TYPE for some
artifacts.
No credit: per-site reminders are absent, or include only READ/PRESERVE without
CONVICTION TYPE at any site.

Diagnostic rule (D6): C-22 requires all three fields per-site. A campaign that
earns full C-20 with only two-field reminders earns no credit for C-22.
Restating CONVICTION TYPE per-site without READ and PRESERVE also earns no
credit -- C-20 full credit is a precondition. A complete three-field per-site
reminder satisfies both C-20 and C-22 simultaneously.

Relationship to C-20: C-22 is a superset of C-20. Full C-22 implies full C-20.
Relationship to C-21: C-21 tests whether conviction types are declared in the
global contract and audit block. C-22 tests whether they are also restated at
each execution site. A campaign can earn full C-21 without earning C-22.

### C-23: Inertia-anchored conviction arc (aspirational) -- added in v6

Conviction types are grounded in a defined inertia baseline -- the status-quo
outcome if the feature is not built. Rather than labeling artifacts with
abstract roles (Factual / Optionality / Emotional), the campaign declares what
the status quo produces at each conviction stage:

- **Spec**: names the specific problem the inertia baseline creates
- **Proposal**: prices the cost of staying on the inertia path
- **Pitch**: makes the inertia cost visceral and audience-specific

V-05 (R5) is the reference implementation. The inertia-anchored form makes
C-21's type labels operationally precise: each artifact's conviction role is a
claim about the status quo, not an abstract category. The CONVICTION DELTA
audit becomes "what conviction about the cost of inertia does the pitch
establish that the spec and proposal did not?" -- a sharper diagnostic than
the typed but abstract form.

Full credit: all three artifacts carry a declared conviction role grounded in
the inertia baseline at both the campaign-level contract and the per-artifact
execution-site reminders; the CONVICTION DELTA audit is typed to the
inertia-cost form of the pitch's conviction role.
Partial (2.5 pts): inertia-grounded conviction types appear at the campaign
level (matrix or equivalent) but per-site reminders restate abstract labels --
or: some artifacts declare inertia-anchored roles while others use abstract
labels.
No credit: conviction roles are abstract labels or implicit; no inertia baseline
defined.

Diagnostic rule (D7): Earning C-23 requires an inertia baseline defined at
the campaign level -- in the setup phase or identity contract. Campaigns without
a declared inertia model cannot earn C-23 regardless of conviction typing
quality. This is a campaign-level architectural choice, not a local
improvement.

Diagnostic rule (D8): C-23 full credit requires inertia-grounded conviction
type labels at BOTH the campaign-level matrix (or equivalent global
declaration) AND the per-artifact execution-site reminders. The per-site
reminder is the proximal instruction at execution time; abstract labels at
that level sever the inertia grounding precisely where the artifact is produced.
A campaign that declares inertia-grounded CONVICTION TYPE in the matrix but
uses abstract labels in per-site reminders (e.g., "Factual -- assert what is
true" instead of "Factual -- name the problem the inertia baseline creates")
earns C-23 PARTIAL (V-01 R6 finding).

Relationship to C-21: C-23 is a strengthened form of C-21. Full C-23 implies
full C-21. A campaign earning full C-21 with abstract labels earns no credit
for C-23.

Relationship to C-26: C-23 tests whether conviction types are grounded in the
inertia baseline. C-26 tests whether that baseline is declared as a named
structural entity. A campaign can earn full C-23 without earning C-26 (e.g.,
inertia-grounded inline sentence form satisfies C-23 but not C-26).

Relationship to C-09: Inertia anchoring provides an external reference that
makes near-duplicate detection more precise -- if both spec and proposal make
the same inertia claim, repetition is observable rather than inferred from
content resemblance.

### C-24: Scout-to-must-have traceability (aspirational) -- added in v6

Each spec Must-have explicitly cites the scout-requirements friction that
justifies its inclusion, creating a bidirectional linkage between the scout
signal layer and the spec requirement layer. C-10 requires that scout signals
be visibly pulled into the artifact that benefits from them (unidirectional:
scout -> artifact). C-24 requires the reverse linkage to also be labeled: each
must-have names the specific friction from scout-requirements that motivated
its inclusion.

V-05 (R5) is the reference implementation (general instruction form): "Each
Must-have must trace to a specific friction the inertia baseline creates." The
per-must-have citation makes the proposal's option evaluation and the pitch's
CTA auditable against the scout evidence chain.

Full credit: each spec Must-have carries a labeled citation of its originating
scout-requirements friction; the linkage is explicit and complete.
Partial (2.5 pts): most must-haves cite a friction, but some are undocumented;
or the citations are informal (embedded in prose rather than labeled); or the
instruction mandates citation but the format (e.g., compact inline tag without
scout file reference) leaves the source partially untraced.
No credit: scout signals are pulled into the spec (C-10 satisfied) but
must-haves do not individually cite their scout origin.

Relationship to C-10: C-10 tests whether scout signals are visible in the
artifact that benefits from them. C-24 tests whether each requirement is
traceable back to its scout evidence source. A campaign that earns full C-10
with a general scout-signal pull earns no credit for C-24 unless the
per-must-have citation is also present.

Relationship to C-25: C-24 tests whether per-must-have citations exist. C-25
tests whether those citations are structured as a dedicated labeled table. A
campaign can earn full C-24 with a general instruction form without earning
C-25. A campaign that earns full C-25 automatically earns full C-24.

---

### C-25: Scout traceability table (aspirational) -- new in v7

The scout-to-must-have citations (C-24) are structured as a dedicated labeled
table with explicit columns rather than embedded in prose, as an inline tag
appended to requirement bullets, or mandated by a general instruction. The
table form (Req-ID / Must-have / Originating Scout-Requirements Friction /
Scout File or equivalent) makes the linkage row-by-row auditable: a scorer,
reviewer, or the executing model can verify each must-have against its
originating evidence by inspecting a dedicated structure rather than tracing
citations embedded in requirement text.

V-02 (R6) and V-05 (R6) are the reference implementations. The distinguishing
feature is the separate labeled structure -- the table exists as its own named
section or block within the REQUIREMENTS section, not as annotations on the
requirement list. A "Scout File" column (or equivalent) that names the specific
evidence file makes the linkage bidirectionally auditable without prose
interpretation.

Full credit: a dedicated labeled table structure with at minimum: per-row entry
per Must-have, an explicit friction column, and a scout source column (file
path or namespace reference). The table must be structurally distinct from the
requirement list itself.
Partial (2.5 pts): a structured list or annotated requirement format that
provides per-must-have friction citations but omits scout file attribution; or
a table present but missing explicit source column.
No credit: citations exist only as a general instruction, embedded prose, or
inline tags appended to requirement bullets -- no dedicated labeled table
structure.

Relationship to C-24: C-25 is a superset of C-24. Full C-25 implies full C-24.
A general instruction form earns C-24 full credit but C-25 no credit.

Relationship to C-10: The table form of C-25 strengthens C-10 quality beyond
the instruction-form linkage. The "Scout File" column makes signal consumption
bidirectionally auditable at the must-have level, not just the artifact level.

### C-26: Named inertia model entity (aspirational) -- new in v7

The inertia baseline is declared as a named, multi-field structural entity in
the setup phase -- not as an inline sentence in the campaign framing or as a
compact label in a conviction type description. The entity form requires at
minimum a name and multiple declared fields (e.g., Name / Behavior / Cost), and
an explicit mapping from entity fields to conviction types, so that subsequent
CONVICTION TYPE labels can reference specific model fields by name.

V-03 (R6) and V-05 (R6) are the reference implementations. The distinguishing
feature is the named entity with field-level referenceability -- subsequent
conviction type declarations read "Factual -- document the INERTIA MODEL Cost
field as factual record" (referencing a specific declared field) rather than
"Factual -- names the problem the inertia baseline creates" (referencing the
concept of inertia). Every instruction that references the INERTIA MODEL by
field name is formally verifiable against the entity declaration.

Full credit: inertia baseline declared as a named entity with at least two
explicit fields and a field-to-conviction-type mapping in the setup phase;
subsequent CONVICTION TYPE labels reference entity fields by name.
Partial (2.5 pts): inertia baseline declared as a named entity but without
field-level structure or field-to-conviction-type mapping -- the name is
declared but the fields are not individually referenceable.
No credit: inertia baseline declared as an inline sentence, compact labels
(e.g., "Factual -- names inertia problem"), or not declared at the campaign
level. The baseline must be an independently named structural entity to earn
credit.

Diagnostic rule (D9): C-26 requires a named structural entity -- a declaration
that has a name, distinct fields, and a mapping. Compact inertia-grounded
conviction type labels that reference the concept of inertia without declaring
a named model (e.g., "Factual -- names inertia problem" in the matrix without a
prior INERTIA MODEL declaration) do not satisfy C-26 regardless of semantic
content. The entity must be declarable, referenceable, and named before
conviction type labels can cite its fields.

Relationship to C-23: C-23 tests whether conviction types are grounded in the
inertia baseline. C-26 tests whether that baseline is declared as a named
structural entity with referenceable fields. A campaign can earn full C-23
without earning C-26 (inline sentence or compact label form satisfies C-23 at
full credit). A campaign that earns full C-26 automatically earns full C-23
(named entity with field mapping is the strongest C-23 form).

Relationship to D7: D7 requires an inertia baseline defined at the campaign
level. C-26 extends D7: not only must the baseline be declared at campaign
scope (D7), it must be declared as a named, multi-field entity (C-26). D7 is a
necessary but not sufficient condition for C-26.

---

### C-11: Hard GATE per transition (excellence)

Each artifact transition must contain explicit blocking language:
- "Do not begin [Artifact 2] until [Artifact 1] is written to disk."
- "Do not begin [Artifact 3] until [Artifact 2] is written to disk."

Both gate statements must be present. Soft dependency language ("grounded
in the spec just written," "read the proposal") passes C-04 but does not
satisfy C-11. Full credit requires both transitions gated; one gate only
is PARTIAL (1 pt).

Note: campaigns with a named CAMPAIGN REFLECTION phase (C-19 FULL) implicitly
carry a third gate before the reflection phase; this strengthens C-19 but does
not change C-11 scoring, which tests artifact-production transitions only.

### C-12: Proactive scout inventory (excellence)

The setup phase -- before Artifact 1 begins -- must proactively glob
`simulations/scout/` and list found signals by namespace. The inventory
must be executed unconditionally, not gated on signal existence. A
conditional pull passes C-10 but does not satisfy C-12.

### C-13: Conviction audit (excellence)

The pitch post-execution audit block (C-16) must contain two explicit checks
stated as instructions:
1. "State what conviction this version establishes that the previous
   artifacts did not."
2. "Note any content you nearly duplicated from spec or proposal."

A strong narrative inertia thread (C-09) is not sufficient. The audit must
be written as a named instruction the executor follows. Missing either check
is PARTIAL (1 pt). Note: C-13 requires the post-execution block structure
established by C-16 -- a pre-execution block or checklist containing both
questions earns C-13 PARTIAL regardless of content quality.

When C-21 is also present (conviction typing), C-13 is strengthened: check 1
becomes "State what [CONVICTION TYPE] conviction this pitch adds..." A typed
version of C-13 check 1 earns full credit for both C-13 and C-21.

When C-23 is also present (inertia-anchored conviction arc), C-13 is further
sharpened: check 1 becomes "State what conviction about the cost of inertia
this pitch makes visceral that the spec and proposal could not." An
inertia-typed version of C-13 check 1 earns full credit for C-13, C-21, and
contributes to C-23.

### C-14: Signal consumption log (excellence)

The campaign close section must record, per artifact, which scout signal
namespace was consumed -- not merely list artifacts or list signals. A table
or structured list with columns for artifact path + signal namespace consumed
satisfies this criterion. A close that names signals globally (not per
artifact) is PARTIAL (1 pt).

---

## Round 1 Calibration

| Variant | Composite (v2) | Golden |
|---------|---------------|--------|
| V-03 -- Lifecycle Emphasis | ~106 | Yes |
| V-01 -- Role Sequence | ~95 | Yes |
| V-05 -- Full Integration | ~104 | Yes |
| V-04 -- Register + Inertia | ~82 | No (C-03, C-05 essential partial) |
| V-02 -- Output Format | ~79 | No (C-03 essential partial, C-09 fail) |

Excellence signal pattern: V-03 leads on C-11/C-12/C-13; V-05 leads on
C-14. No single variant in Round 1 fully satisfies all four.

---

## Round 2 Calibration

| Variant | Base | Excellence | Total | Golden |
|---------|------|------------|-------|--------|
| V-01 -- Artifact Contract | 100 | +8 | **108** | Yes |
| V-02 -- Pre-flight Checklist | 97.5 | +7 | **104.5** | Yes |
| V-03 -- Minimal Density | 100 | +8 | **108** | Yes |
| V-04 -- Lifecycle + Conviction Merge | 100 | +8 | **108** | Yes |
| V-05 -- Pre-execution Conviction | 100 | +7 | **107** | Yes |

All five Golden. R2 resolved both R1 excellence gaps -- three variants hit 108.

**R2 diagnostic finding**: C-13 requires the FINDINGS label and post-execution
placement. V-02 (checklist) and V-05 (BEFORE WRITING) both had correct semantic
content but earned PARTIAL. Pre-execution conviction architecture and structural
checklists are not substitutes for post-execution FINDINGS reflection. This
finding is codified as C-16.

**New patterns promoted to aspirational**:
- C-15 (Artifact contract): V-01's READ/WRITE/PRESERVE/CARRIES FORWARD
  mechanism. Strongest C-06/C-07 enforcement in two rounds.
- C-16 (Post-execution FINDINGS): label and placement are structural, not
  semantic. Closes the C-09/C-13 gap for pre-execution conviction architectures.

Note: Round 2 scores above reflect the v2 rubric (110-pt base scale introduced
in v3). Retroactive v3 scoring would add up to 10 pts for C-15/C-16.

---

## Round 3 Calibration

Scores below reflect the v3 rubric used at scoring time. Retroactive v4
scoring follows, adding up to 10 pts for C-17/C-18.

| Variant | Essential | Rec | Asp (v3) | Excel | Total (v3) | Golden |
|---------|-----------|-----|----------|-------|------------|--------|
| V-01 -- Contract Matrix | 60 | 30 | 20 | +8 | **118** | Yes |
| V-02 -- FINDINGS Template | 60 | 30 | 20 | +8 | **118** | Yes |
| V-03 -- CF Cascade | 60 | 30 | 17.5 | +8 | **115.5** | Yes |
| V-04 -- Matrix + Template | 60 | 30 | 20 | +8 | **118** | Yes |
| V-05 -- Cascade + Template + Density | 60 | 30 | 17.5 | +8 | **115.5** | Yes |

All five Golden. Three reach the 118 v3-ceiling. V-04 is the new reference
implementation.

**Retroactive v4 scoring** (adds C-17 and C-18):

| Variant | v3 Base | C-17 | C-18 | Excel | Total (v4) |
|---------|---------|------|------|-------|------------|
| V-01 -- Contract Matrix | 110 | +2.5 | +2.5 | +8 | **123** |
| V-02 -- FINDINGS Template | 110 | +5 | +2.5 | +8 | **125.5** |
| V-03 -- CF Cascade | 107.5 | +2.5 | +2.5 | +8 | **120.5** |
| V-04 -- Matrix + Template | 110 | +5 | +5 | +8 | **128** |
| V-05 -- Cascade + Template + Density | 107.5 | +2.5 | +2.5 | +8 | **120.5** |

V-04 uniquely reaches the 128 v4-ceiling.

**C-17 retroactive scoring**:
- V-01: matrix present (C-15 full) but open-prompt FINDINGS -- not a named template -> PARTIAL (2.5)
- V-02: per-artifact inline labeled fields (C-15 full) + named CONVICTION DELTA / NEAR-DUPLICATE CONTENT template -> FULL (5)
- V-03: cascade CF (C-15 partial) + open-prompt FINDINGS -> PARTIAL (2.5)
- V-04: contract matrix (C-15 full) + named CONVICTION DELTA / NEAR-DUPLICATE CONTENT template -> FULL (5)
- V-05: cascade CF (C-15 partial) + named template -> PARTIAL (2.5)

**C-18 retroactive scoring**:
- V-01: "not before" only -> PARTIAL (2.5)
- V-02: "write after the pitch file is complete" -- no "not during" -> PARTIAL (2.5)
- V-03: "not before" only -> PARTIAL (2.5)
- V-04: "not before, not during" -- explicit double prohibition -> FULL (5)
- V-05: "write after the pitch is written" -- no "not during" -> PARTIAL (2.5)

**R3 diagnostic findings**:

**D1**: WRITE must be a labeled contract field -- a write instruction in the body is not
sufficient. V-03 and V-05 both have canonical paths in body write instructions
but not as a labeled `WRITE:` contract field.

**D2**: Pre-execution CARRIES FORWARD is required for C-15 full credit -- cascade CF earns
PARTIAL. The cascade design is technically correct for C-07 compliance but costs C-15.

**D3**: Open-prompt FINDINGS earns C-16 full credit when explicit -- named sub-fields
improve C-13 assurance and C-17 credit.

**New patterns promoted to aspirational**:
- C-17 (Dual-mechanism defense in depth)
- C-18 (Double-prohibition FINDINGS placement)

---

## Round 4 Calibration

Scores below reflect the v4 rubric used at scoring time (128-pt ceiling).
V-04 was not fully scored in R4.

| Variant | Essential | Rec | Asp (v4) | Excel | Total (v4) | Golden |
|---------|-----------|-----|----------|-------|------------|--------|
| V-01 -- FINDINGS Gate Separation | 60 | 30 | 30 | +8 | **128** | Yes |
| V-02 -- Contract Anchor Reminders | 60 | 30 | 30 | +8 | **128** | Yes |
| V-03 -- Conviction Staging | 60 | 30 | 30 | +8 | **128** | Yes |

All three scored variants reach the 128 v4-ceiling. R4 is the first round
where all submitted variants simultaneously reach the ceiling -- confirming
v4 criteria fully captured the R3 reference implementation (V-04).

**Excellence basis per variant**:
- V-01: Phase-gate structure makes C-18 structural -- double-prohibition is a
  phase boundary condition, not a remembered clause.
- V-02: Proximity anchoring -- contract obligations restated at each execution
  site, minimizing enforcement distance, most directly strengthening C-06.
- V-03: Conviction typing -- CONVICTION TYPE labels make narrative arc roles
  declared rather than inferred; CONVICTION DELTA audit is more precise than
  an open FINDINGS block for C-09 diagnosis.

**Retroactive v5 scoring** (adds C-19, C-20, C-21):

| Variant | v4 Total | C-19 | C-20 | C-21 | Total (v5) |
|---------|----------|------|------|------|------------|
| V-01 -- FINDINGS Gate Separation | 128 | +5 | 0 | 0 | **133** |
| V-02 -- Contract Anchor Reminders | 128 | 0 | +5 | 0 | **133** |
| V-03 -- Conviction Staging | 128 | 0 | +2.5* | +5 | **135.5** |

*V-03's per-artifact CONVICTION TYPE entry in the contract matrix provides a
conviction-obligation reminder at each artifact site; READ and PRESERVE are not
restated per-site. C-20 PARTIAL (2.5) pending commissioner assessment.

**C-19 retroactive scoring**:
- V-01: Named CAMPAIGN REFLECTION phase sequenced after pitch completion with
  explicit gate -> FULL (5)
- V-02: No phase-gate structure; C-18 satisfied via inline clause -> PARTIAL (2.5)
- V-03: No phase-gate structure; C-18 satisfied via inline clause -> PARTIAL (2.5)

**C-20 retroactive scoring**:
- V-01: No per-artifact contract reminders at execution sites -> NO CREDIT (0)
- V-02: Per-artifact `Contract reminder -- READ: ... | PRESERVE: ...` line at each
  execution site -> FULL (5)
- V-03: Per-artifact CONVICTION TYPE in contract (C-15 superset) -- READ/PRESERVE
  not restated per-site -> PARTIAL (2.5, pending commissioner assessment)

**C-21 retroactive scoring**:
- V-01: No CONVICTION TYPE labels -> NO CREDIT (0)
- V-02: No CONVICTION TYPE labels -> NO CREDIT (0)
- V-03: CONVICTION TYPE labels (Factual / Optionality / Emotional) on all three
  artifacts + CONVICTION DELTA typed audit -> FULL (5)

**R4 diagnostic findings**:

**D4 (v5)**: A 5-field C-15 superset earns full C-15 credit. V-03's contract
matrix with CONVICTION TYPE as a fifth field satisfies all four required fields
and earns C-15 full credit. Extra fields do not confuse scoring.

**D5 (v5)**: Functional equivalence rule for C-16 FINDINGS block. V-03's
CONVICTION DELTA block earns C-16 full credit -- any labeled, post-execution
audit block qualifies regardless of exact name.

**New patterns promoted to aspirational**:
- C-19 (Structural double-prohibition): V-01's phase-gate encoding of C-18.
  Makes the prohibition a phase boundary condition rather than a clause.
- C-20 (Contract proximity anchoring): V-02's per-artifact contract reminder
  pattern. Reduces enforcement distance for PRESERVE and READ obligations.
- C-21 (Conviction typing): V-03's CONVICTION TYPE label + CONVICTION DELTA
  audit. Makes narrative arc roles declared rather than inferred.

---

## Round 5 Calibration

Scores below reflect the v5 rubric used at scoring time (143-pt ceiling).

| Variant | Essential | Rec | Asp (v5) | Excel | Total (v5) | Golden |
|---------|-----------|-----|----------|-------|------------|--------|
| V-01 -- C-20 Proximity Resolution | 60 | 30 | 42.5 | +8 | **140.5** | Yes |
| V-02 -- Phase Gate + Conviction Typing | 60 | 30 | 42.5 | +8 | **140.5** | Yes |
| V-03 -- Full Triple Combination | 60 | 30 | 45 | +8 | **143** | Yes |
| V-04 -- Full Triple + Minimal Density | 60 | 30 | 45 | +8 | **143** | Yes |
| V-05 -- Full Triple + Inertia-Forward | 60 | 30 | 45 | +8 | **143** | Yes |

All five Golden. Three variants (V-03, V-04, V-05) reach the 143 v5-ceiling
simultaneously, confirming v5 criteria fully captured the R4 synthesis.

**Aspirational partials**:
- V-01: C-19 PARTIAL (2.5) -- inline instruction clause satisfies C-18 but no
  named CAMPAIGN REFLECTION phase; prohibition is still clause-dependent
- V-02: C-20 PARTIAL (2.5) -- artifact 1 has no per-site reminder; artifact 3
  lacks PRESERVE; no artifact carries a complete READ + PRESERVE reminder

**Excellence basis per variant**:
- V-01: Per-site reminder extends to three fields (READ + PRESERVE +
  CONVICTION TYPE) -- first variant to restate the conviction obligation at
  each execution site.
- V-02: Named CAMPAIGN REFLECTION phase with explicit gate before reflection
  -- adds a third structural gate; phase structure resolves C-19 for all
  subsequent R5 variants.
- V-03/V-04: Combine C-19 (named phase gate), C-20 (full per-site reminders),
  and C-21 (conviction typing), each with three-field per-site restatement.
  V-04 demonstrates density invariance -- the ceiling is achievable at minimum
  word count.
- V-05: Inertia-anchored conviction arc and labeled scout-to-must-have
  traceability -- CONVICTION DELTA questions are qualitatively sharper
  (inertia-typed) but produce no scoring differential within existing FULL
  credit bands under v5.

**Retroactive v6 scoring** (adds C-22, C-23, C-24):

| Variant | v5 Total | C-22 | C-23 | C-24 | Total (v6) |
|---------|----------|------|------|------|------------|
| V-01 -- C-20 Proximity Resolution | 140.5 | +5 | 0 | 0 | **145.5** |
| V-02 -- Phase Gate + Conviction Typing | 140.5 | 0 | 0 | 0 | **140.5** |
| V-03 -- Full Triple Combination | 143 | +5 | 0 | 0 | **148** |
| V-04 -- Full Triple + Minimal Density | 143 | +5 | 0 | 0 | **148** |
| V-05 -- Full Triple + Inertia-Forward | 143 | +5 | +5 | +5 | **158** |

V-05 alone reaches the v6 ceiling.

**C-22 retroactive scoring**:
- V-01: Each artifact carries `Contract reminder -- READ: ... PRESERVE: ...
  CONVICTION TYPE: ...` -- all three fields present at every execution site
  -> FULL (5)
- V-02: Artifact 1 has no per-site reminder; artifact 2 has informal
  READ/PRESERVE (no CONVICTION TYPE); artifact 3 has READ but PRESERVE absent
  -- no artifact carries all three fields -> NO CREDIT (0)
- V-03: All three artifact sites carry `Contract reminder -- READ: ... PRESERVE:
  ... CONVICTION TYPE: ...` -> FULL (5)
- V-04: Compact labeled form (`READ: ... / PRESERVE: ... / CONVICTION TYPE: ...`)
  carries the same structural signal -> FULL (5)
- V-05: Inertia-typed CONVICTION TYPE restated alongside READ and PRESERVE at
  each execution site -> FULL (5)

**C-23 retroactive scoring**:
- V-01 to V-04: CONVICTION TYPE labels use abstract categories (Factual /
  Optionality / Emotional) without grounding in the inertia baseline ->
  NO CREDIT (0)
- V-05: Conviction types declared as inertia-anchored roles ("names the
  problem the inertia baseline creates / prices the cost of inertia / makes
  the inertia cost visceral"); CONVICTION DELTA typed to inertia cost ->
  FULL (5)

**C-24 retroactive scoring**:
- V-01 to V-04: Scout signals pulled unconditionally into the spec (C-10 FULL)
  but must-haves do not individually cite their originating scout friction ->
  NO CREDIT (0)
- V-05: "Each Must-have must trace to a specific friction the inertia baseline
  creates" -- labeled bidirectional linkage from must-have to scout-requirements
  friction -> FULL (5)

**R5 diagnostic findings**:

**D6 (v6)**: C-22 requires all three fields (READ, PRESERVE, CONVICTION TYPE)
per-site. Per-site reminders with only READ+PRESERVE earn C-20 FULL but C-22
NO CREDIT. A complete three-field per-site reminder satisfies both C-20 and
C-22 simultaneously.

**D7 (v6)**: C-23 and C-24 require an inertia baseline defined at the campaign
level. Campaigns without an explicit inertia model cannot earn these criteria
regardless of conviction typing quality. The inertia baseline is a
campaign-level architectural choice, not a local improvement to an existing
design pattern.

**New patterns promoted to aspirational**:
- C-22 (Per-site conviction type restatement): V-01's three-field per-site
  reminder pattern. Extends C-20 to include the conviction obligation at the
  execution site.
- C-23 (Inertia-anchored conviction arc): V-05's inertia-grounded conviction
  types. Makes C-21's abstract labels operationally precise.
- C-24 (Scout-to-must-have traceability): V-05's labeled must-have-to-friction
  linkage. Extends C-10's unidirectional pull to a bidirectional audit chain.

---

## Round 6 Calibration

Scores below reflect the v6 rubric used at scoring time (158-pt ceiling).

| Variant | Essential | Rec | Asp (v6) | Excel | Total (v6) | Golden |
|---------|-----------|-----|----------|-------|------------|--------|
| V-01 -- Per-site Abstract Labels | 60 | 30 | 57.5 | +8 | **155.5** | Yes |
| V-02 -- Scout Traceability Table | 60 | 30 | 60 | +8 | **158** | Yes |
| V-03 -- Named INERTIA MODEL Entity | 60 | 30 | 60 | +8 | **158** | Yes |
| V-04 -- Minimal Density | 60 | 30 | 55 | +8 | **153** | Yes |
| V-05 -- Full Convergence | 60 | 30 | 60 | +8 | **158** | Yes |

All five Golden. V-02, V-03, and V-05 reach the 158 v6-ceiling simultaneously.
V-01 earns C-23 PARTIAL (matrix-only inertia grounding). V-04 earns C-23 PARTIAL
(compact labels) and C-24 PARTIAL (inline-tag without scout file citation).

**Aspirational partials in R6**:
- V-01: C-23 PARTIAL (2.5) -- inertia-grounded labels in matrix but per-site
  reminders restate abstract labels ("Factual -- assert what is true"); model
  executing Artifact 1 reads abstract instruction, not inertia-grounded one
- V-04: C-23 PARTIAL (2.5) -- compact labels ("Factual -- names inertia problem")
  name the inertia connection but do not operationally define it; C-24 PARTIAL
  (2.5) -- inline tag format without scout file citation is less auditable

**Retroactive v7 scoring** (adds C-25, C-26):

| Variant | v6 Total | C-25 | C-26 | Total (v7) |
|---------|----------|------|------|------------|
| V-01 -- Per-site Abstract Labels | 155.5 | 0 | 0 | **155.5** |
| V-02 -- Scout Traceability Table | 158 | +5 | 0 | **163** |
| V-03 -- Named INERTIA MODEL Entity | 158 | 0 | +5 | **163** |
| V-04 -- Minimal Density | 153 | 0 | 0 | **153** |
| V-05 -- Full Convergence | 158 | +5 | +5 | **168** |

V-05 alone reaches the v7 ceiling.

**C-25 retroactive scoring**:
- V-01: General instruction form ("Each Must-have traces to a specific friction
  the inertia baseline creates") -- no dedicated table structure -> NO CREDIT (0)
- V-02: SCOUT TRACEABILITY TABLE in REQUIREMENTS with per-must-have rows
  (Req-ID / Must-have / Originating Scout-Requirements Friction / Scout File)
  -- dedicated labeled table, row-by-row auditable -> FULL (5)
- V-03: General instruction form (same as V-01/R5 pattern) -- no table ->
  NO CREDIT (0)
- V-04: Inline-tag approach ("[friction: {specific inertia or scout-requirements
  finding}]" appended to each must-have bullet) -- not a dedicated table
  structure -> NO CREDIT (0)
- V-05: SCOUT TRACEABILITY TABLE (same form as V-02) -> FULL (5)

**C-26 retroactive scoring**:
- V-01: Inertia-grounded labels in matrix without a named entity declaration
  -> NO CREDIT (0)
- V-02: Inertia-grounded inline sentence per-site labels without named entity
  -> NO CREDIT (0)
- V-03: INERTIA MODEL declared as named three-field entity (Name / Behavior /
  Cost) in SETUP; explicit field-to-conviction-type mapping; CONVICTION TYPE
  labels reference INERTIA MODEL fields by name at both matrix and per-site
  levels -> FULL (5)
- V-04: Compact matrix labels ("Factual -- names inertia problem") reference
  inertia concept but no named entity declared -> NO CREDIT (0)
- V-05: Named INERTIA MODEL entity (Name / Behavior / Cost) + field mapping +
  SCOUT TRACEABILITY TABLE + field-referenced per-site reminders -> FULL (5)

**R6 diagnostic findings**:

**D8 (v7)**: C-23 full credit requires inertia-grounded conviction type labels
at BOTH the campaign-level matrix AND the per-artifact execution-site reminders.
Matrix-only inertia grounding with abstract per-site labels earns PARTIAL -- the
per-site reminder is the proximal instruction at execution time, and reverting
to abstract labels there severs the inertia grounding at the moment the model
produces the artifact (V-01 R6 finding).

**D9 (v7)**: C-26 requires a named structural entity -- compact labels that
reference the concept of inertia (e.g., "Factual -- names inertia problem") are
not sufficient. The inertia model must be declared as a referenceable entity
with named fields before conviction type labels can cite those fields. Semantic
inertia-awareness in conviction labels does not substitute for the entity
declaration.

**R6 excellence signals**:

V-02 -- SCOUT TRACEABILITY TABLE form for C-24: The table (Req-ID / Must-have /
Originating Friction / Scout File) is the most auditable C-24 implementation.
It makes the reverse linkage checkable row-by-row -- a scorer, reviewer, or the
executing model can verify each must-have against its originating evidence.
General instructions require the model to remember to cite; the table requires
it to fill in a column.

V-03 -- Named INERTIA MODEL entity as campaign-level architectural choice:
Elevating the inertia baseline from a sentence to a named, three-field
structural entity (Name / Behavior / Cost) with explicit field-to-conviction-type
mapping creates a referenceable "opponent model." Every subsequent instruction
references the model by field name, making the inertia grounding formally
verifiable.

V-05 -- Full convergence without interference: Combining all three mechanisms
simultaneously -- named INERTIA MODEL + SCOUT TRACEABILITY TABLE +
field-referenced per-site reminders -- produces no criterion degradation.
Maximum explicitness at all levels is safe. The three mechanisms are
architecturally separable (SETUP entity + REQUIREMENTS table + per-site
reminders) and do not compete for the same instruction space.

**New patterns promoted to aspirational**:
- C-25 (Scout traceability table): V-02/V-05's dedicated labeled table
  structure. Extends C-24 from instruction form to auditable structure form.
- C-26 (Named inertia model entity): V-03/V-05's named entity declaration.
  Extends C-23 from grounded labels to formally referenceable opponent model.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial -- 5 essential, 3 recommended, 2 aspirational; 100-pt scale |
| v2 | 2026-03-16 | Added C-11 to C-14 excellence signals from Round 1 scorecard; 108-pt ceiling; calibration table added |
| v3 | 2026-03-16 | Added C-15 (artifact contract) and C-16 (post-execution FINDINGS) as aspirational from Round 2 patterns; aspirational total 10->20; base ceiling 100->110; 118-pt ceiling; R2 calibration added |
| v4 | 2026-03-16 | Added C-17 (dual-mechanism defense in depth) and C-18 (double-prohibition FINDINGS placement) as aspirational from Round 3 patterns; aspirational total 20->30; base ceiling 110->120; 128-pt ceiling; R3 calibration with retroactive v4 scoring added |
| v5 | 2026-03-16 | Added C-19 (structural double-prohibition), C-20 (contract proximity anchoring), C-21 (conviction typing) as aspirational from Round 4 patterns; resolved D4 (superset rule for C-15) and D5 (functional equivalence rule for C-16); aspirational total 30->45; base ceiling 120->135; 143-pt ceiling; R4 calibration with retroactive v5 scoring added |
| v6 | 2026-03-16 | Added C-22 (per-site conviction type restatement), C-23 (inertia-anchored conviction arc), C-24 (scout-to-must-have traceability) as aspirational from Round 5 patterns; resolved D6 (C-22 three-field per-site requirement) and D7 (inertia baseline is a campaign-level architectural choice); aspirational total 45->60; base ceiling 135->150; 158-pt ceiling; R5 calibration with retroactive v6 scoring added |
| v7 | 2026-03-16 | Added C-25 (scout traceability table) and C-26 (named inertia model entity) as aspirational from Round 6 patterns; resolved D8 (C-23 requires inertia grounding at both matrix and per-site reminders) and D9 (C-26 requires named structural entity, not compact labels); updated C-23 detail with D8 clarification; aspirational total 60->70; base ceiling 150->160; 168-pt ceiling; R6 calibration with retroactive v7 scoring added |
