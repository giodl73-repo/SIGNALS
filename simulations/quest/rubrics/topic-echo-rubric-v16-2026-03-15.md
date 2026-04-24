Done. `topic-echo-rubric-v16-2026-03-15.md` written.

**What changed v15 -> v16:**

**C-53 -- Compound per-site and ordering annotation co-present in single dep entry**
When C-50 (site descriptor) and C-51 (ordering intent) must both be satisfied, both annotations appear *together* in the single dep entry at the consumption site -- not distributed across separate locations. The compound form `[C-48 site -- C-51: LINE 1 -- C-50: entry 2 of 2]` makes the entry independently auditable: site identity and ordering intent verifiable from one structural location without look-back. Emerged only when C-50+C-51 are simultaneously active; C-50-only entries lack it.

**C-54 -- Self-detecting gap contract stated inline on version-aligned closing tag**
The self-inventorying tag (C-52) carries an explicit inline guarantee: "A tag absent C-52 would fail C-52 by that absence -- gap is self-detectable." Converts the structural completeness property (C-52) into an auditable protocol: the tag states what its own absence would constitute, making the gap diagnosable from the tag's content alone without consulting the rubric changelog. C-52 = structural completeness; C-54 = gap-detection protocol stated inline.

**Scoring:** 60 + 21 + 138 = **219** (46 aspirational criteria, up from 44).
t stated inline on version-aligned closing tag**
Source: R15 V-05 excellence signal 2. The version-aligned closing tag (C-49, extended by
C-52 to be self-inventorying) carries an explicit gap-detection guarantee stated inline:
"A tag absent C-52 would fail C-52 by that absence -- gap is self-detectable." The
guarantee converts the self-referential tag from a structural design property (C-52) into
an auditable contract with its own gap-detection protocol embedded at the tag site. A
reviewer does not need to consult the rubric changelog to determine whether the tag is
complete: the tag's own guarantee statement identifies the failure mode if the self-
inventorying criterion is missing. Distinct from C-52 (which requires the tag to include
itself as an entry); this requires the tag to state its own gap-detection guarantee --
making the absence of the self-inventorying entry self-diagnosing rather than merely
self-verifiable.

**Scoring:** 60 + 21 + 138 = **219** (up from 213). Aspirational band 44 -> 46 criteria
(max 132 -> 138 pts).

---

## Essential (C-01..C-05)

The output is not a valid echo without all five.

### C-01 -- Surprise-only filter
Every item in the echo would have been unpredictable before signal gathering. The
output must name or enforce the discard condition: "Would a competent practitioner
have predicted this from first principles?" Items that survive this test are
surprises; items that do not are omitted or demoted. A gate mechanism (explicit
screening step, discard log, skeptic role) is stronger than a prose instruction.

**FAIL signal**: Items that read as confirmations of the original hypothesis or
restatements of known constraints.

### C-02 -- Source signal tracing
Every surprise cites a specific artifact, namespace, and skill. The citation format
must be precise enough to retrieve the source: `{artifact-name} ({namespace}/{skill})`.
If a surprise emerges from multiple artifacts, all sources are cited.

**FAIL signal**: "Several signals suggested..." with no artifact names.

### C-03 -- Design impact assessment
Every surprise says what changes in the design direction as a result. Acceptable
impact statements name one of: a decision that gets revisited, an assumption that
gets struck, or a scope boundary that shifts. Vague formulations ("this is worth
noting") fail.

**FAIL signal**: Surprises with no downstream consequence stated.

### C-04 -- Named surprises
Each surprise carries a distinct, referenceable short label (e.g., "The Adoption
Ceiling", "The Silent Veto"). Labels must be unique within the output and stable
enough to cite in downstream artifacts.

**FAIL signal**: Surprises described only in paragraph prose with no extractable name.

### C-05 -- Synthesis not summary
At least two surprises emerge from cross-signal tension -- they are only visible when
two or more signals are read together, not from any single artifact in isolation. The
output must draw the definitional line: a finding that lives in one artifact is a
finding; a surprise that only emerges when two signals are read together is an echo.

**FAIL signal**: Every surprise traces to exactly one artifact. No cross-signal
section or marking exists.

---

## Recommended (C-06..C-08)

Strong outputs satisfy all three.

### C-06 -- Forward-looking handoff
The output closes with a forward-looking handoff statement: "If you are about to
build X, know that Y because Z." Must name a specific construction scenario (X), a
concrete surprising constraint (Y), and a source signal (Z). Generic advice without
a named scenario fails.

**FAIL signal**: Closing section reads as a summary of findings rather than a
directive to a future builder.

### C-07 -- Impact magnitude
Every surprise carries a tier label: HIGH (revisits core architecture or scope),
MEDIUM (revisits a component decision), LOW (changes a detail without scope impact).
Tier appears in the entry header. A verification step (Rules of Thumb, checklist,
or close gate) confirms that the tier assigned matches the tier in the final entry.

**FAIL signal**: No tier labels present, or tier present only as a post-hoc
annotation with no verification step.

### C-08 -- Cross-signal explicit
Surprises that emerge from cross-signal tension carry an explicit structural
annotation in the output entry -- e.g., `[CROSS: {artifact-A} x {artifact-B}]`.
Cross-signal surprises are distinguishable from single-artifact findings by
inspection without re-reading the source artifacts.

**FAIL signal**: Cross-signal surprises exist but carry no marking; reviewer cannot
identify them without re-tracing sources.

---

## Aspirational (C-09..C-54)

Each criterion is a distinct structural property. PARTIAL = the property is
attempted but not fully enforced.

### C-09 -- Discard visibility
The output or a companion log makes at least one discarded candidate visible --
naming what was considered and why it did not pass the surprise filter. Makes the
gate auditable rather than invisible.

### C-10 -- Multi-namespace coverage
The output documents that signals from at least three distinct namespaces were
evaluated, even if surprises emerged from fewer. Coverage statement prevents
namespace-blindness.

### C-11 -- Anti-hypothesis guard
Explicit test that original hypotheses from the spec or pitch are not present in
the echo output. Named guard: "Does this item confirm what we set out to prove?"
Items that confirm the original hypothesis are explicitly routed out.

### C-12 -- Temporal marking
Each surprise carries a temporal anchor -- the gathering round or date when the
signal that produced it was created. Enables downstream readers to assess staleness.

### C-13 -- Typed skeptic gate
An Anti-Pattern Catalog or equivalent named-anti-pattern list is applied
entry-by-entry. A named Skeptic role challenges each candidate before entry
expansion. Anti-pattern types are enumerated; the role name appears per sub-step.

### C-14 -- Downstream handoff routing
Each output entry carries a downstream routing field naming the skill or namespace
that should consume it (e.g., `-> topic-story`, `-> draft-proposal`). Routing is
in the entry itself, not only in execution scaffolding.

### C-15 -- Minimum surprise floor
Output contains at least three distinct surprises. Outputs with fewer than three
are incomplete regardless of the quality of individual entries.
PARTIAL = exactly two surprises present.

### C-16 -- Structurally-enforced filter
The surprise filter uses a gate template requiring a typed verdict before any entry
proceeds to expansion -- e.g., `VERDICT: SURPRISE | CUT -- {label}`. Structurally
malformed outputs (entries without a valid gate verdict) cannot exist. Gate runs
before entry expansion, not after.

### C-17 -- Correction-encoding names
Labels follow a two-part correction-encoding format: `The {Corrected Belief}: {Domain}`.
The name encodes what was wrong and where, not a poetic description of the finding.
A VALID/INVALID example pair is provided to anchor the constraint.

**VALID**: "The Silent Veto: Adoption Workflow"
**INVALID**: "Surprising Finding About Adoption"

### C-18 -- Forward-failure framing
The design impact field is framed as a failure scenario: "If the next team carries
the old assumption, {specific concrete failure}." The framing grounds impact in a
mis-design, not in a change-list. Distinct from C-03 (which requires impact to be
stated); this requires impact to be stated as a failure scenario.

**FAIL signal**: Impact field reads as "this affects X" or "X should be
reconsidered" without a concrete failure form.

### C-19 -- Register-anchored close
The handoff close uses a numbered register menu (T-1..T-4 or equivalent) with
distinct templates for different audience contexts (builder, reviewer, PM,
architect). Selected template and slot assignments are verified before output is
finalized.

### C-20 -- Pre-expansion co-validation gate
A paired validation gate co-validates the name form (C-17) and the failure field
(C-18) in a single step before entry expansion proceeds. Neither alone is sufficient
to pass the gate; both must be VALID simultaneously. The gate runs once per
candidate entry; a failed gate blocks expansion.

### C-21 -- Derivation scaffold for naming
The naming step provides a construction sequence:
1. State the old belief
2. State the correction
3. Derive the domain
4. Form the label

The model is walked through how to arrive at a name, not just what shape the name
must have. Output of step 4 feeds directly into the entry header.

### C-22 -- Failure-first production ordering
Entry production order starts at the failure scenario: the failure is the
load-bearing entry point from which signal tracing, naming, and impact derive.
Distinct from C-18 (which governs the framing field); this governs the production
axis -- whether the entry derives from failure or arrives at failure.

**FAIL signal**: Entry production order is Name -> Source -> Finding -> Impact
(failure appears last or is derived, not load-bearing).

### C-23 -- Impact triage as pre-write scaffolding
Impact tier (HIGH / MEDIUM / LOW) is assigned in a discrete pre-write triage step,
before entry expansion begins. The tier becomes a structural constraint on the entry
header -- not a post-hoc annotation. The scaffold forces the writer to commit to
magnitude before composing prose.

**FAIL signal**: Tier first appears inside a completed entry. No triage step
precedes the writing phase.

### C-24 -- End-to-end traceability closure
A verification step (Rules of Thumb, checklist, or close gate) explicitly confirms
that the tier assigned during triage matches the tier appearing in the final entry
header. Closes the audit chain: triage -> header -> verification. Without this step
the chain is open -- triage may have been overridden silently.

**FAIL signal**: Output contains tier labels in entries and a triage step, but no
step verifies that they agree.

### C-25 -- Two distinct named roles
The prompt assigns at least two named roles with explicitly distinct functions --
e.g., Gatekeeper (adversarial falsification test) and Institutional Archaeologist
(future-reader framing). Role names appear per sub-step, not only in a preamble.
Prevents role-function drift; makes each step's epistemic posture auditable by name.

**FAIL signal**: A single role performs both adversarial testing and future-reader
framing, or roles are named in the preamble but do not label individual sub-steps.

### C-26 -- Output-level gestalt summary test
The surprise filter is applied to the artifact as a whole, not only entry-by-entry.
The gate asks: "Could this output be described as a summary of what the
investigation found?" An output that passes all item-level tests but reads as a
survey of discoveries in aggregate fails this test. The output-level test is the
backstop for summary-in-disguise artifacts that item screening cannot catch.

**FAIL signal**: Every individual entry passes the surprise filter, but the output
as a whole reads as a comprehensive survey of discoveries rather than a curated set
of retroactively-visible surprises.

### C-27 -- Adversarial function declaration
The Gatekeeper role's *function* is explicitly declared, not just its *name*. The
declaration states both what the role does ("adversarial rejection") and what it
does not do ("not future-reader framing"). This declaration appears at or near the
role's first invocation, not only in a preamble. The function/identity contrast
prevents role conflation at execution time: a model executing this prompt knows not
just who the Gatekeeper is but what it is *for* -- and the contrast with the IA's
function makes the boundary structurally clear rather than nominally clear.

**FAIL signal**: The Gatekeeper role is named and distinguished from other roles
by identity (e.g., "not the Institutional Archaeologist"), but its adversarial
function -- what it does operationally -- is not stated.

### C-28 -- Full-chain traceability with structural qualifiers
The traceability verification step names every link in the production chain with
its structural qualifier in parentheses: e.g., "typed-route prediction sort ->
staged gate verdict (with falsifiable 'We believed:' field) -> comparative triage
rank -> echo entry (with mis-design field) -> impact-anchored rule (with matching
tier)." Each parenthetical names the structural requirement that makes that link
auditable. A future reader can verify any link without access to the session that
produced the artifact. Distinct from C-24 (which verifies that triage tier matches
header tier); this governs whether every chain link carries its own auditable
structural qualifier.

**FAIL signal**: Traceability check names the chain links but omits structural
qualifiers -- a reader must inspect the underlying structural step to verify each
link rather than reading the traceability statement alone.

### C-29 -- Verification steps as chain nodes
Every verification or audit step in the prompt (e.g., the gestalt summary audit
from C-26, the traceability closure from C-28) is itself a named link with a
structural qualifier in the production chain trace -- not a meta-step that sits
above or after the chain. A verification step is in the chain; it produces an
auditable artifact (a passed or failed gate verdict) that is traceable by the same
rules as any production link. This criterion closes the structural gap between C-26
and C-28: the gestalt audit is not exempt from the chain trace simply because it
is a gate.

**FAIL signal**: Chain trace names all production links but treats audit or
verification steps as external gates. A reader can verify that production steps
ran but cannot verify that audit steps ran without re-executing the prompt.

### C-30 -- Sub-step identity+function co-activation
Role function declaration (C-27) co-activates with the role name (C-25) at the
sub-step level -- not at the enclosing step header or preamble. Every individual
sub-step that invokes a named role carries both the name and the declared function
inline. The co-activation at maximum granularity means a model executing any
individual sub-step sees identity and function together without look-back to a
containing scope. Distinct from C-27 (which requires function declaration near
first invocation) and C-25 (which requires role names per sub-step); this requires
both to appear together at each sub-step invocation.

**FAIL signal**: Role name appears at each sub-step (satisfying C-25) and function
declaration appears at the step header (satisfying C-27), but no individual sub-step
carries both simultaneously. A model at sub-step 3.a can see the role name but must
look back to the step header to recover the function.

### C-31 -- Closed dependency graph
The production chain trace explicitly accounts for all cross-criterion interactions.
Every criterion whose output is consumed by another criterion is represented as a
named node in the chain trace -- not inferred from structural proximity. Concretely:
if C-26 (gestalt audit verdict) feeds into C-28 (chain trace), then C-26 appears
as a named node in the C-28 chain statement. The graph is closed when no
inter-criterion dependency is discoverable only by re-reading the prompt; all
dependencies are readable from the chain trace alone.

**FAIL signal**: Chain trace names production links and structural qualifiers
(satisfying C-28), but inter-criterion dependencies -- where one criterion's output
is a structural input to another -- are absent from the trace. A reader must reason
about criterion relationships rather than read them.

### C-32 -- Epistemic dimension labels at role invocations
Each invocation of a named role carries not only identity (C-25) and function
shorthand (C-30) but also the epistemic dimension being applied at that specific
invocation -- e.g., `*(Gatekeeper: adversarial-rejection-only; epistemic
dimension: novelty)*`. The label names *why this epistemic posture applies here*,
not only *what the role does in general*. Distinct from C-30 (which requires
identity+function at every sub-step); this requires the epistemic dimension to be
stated inline so a model executing a sub-step knows the specific lens being applied
without look-back to a step preamble or external catalog.

**FAIL signal**: Sub-step carries identity and function shorthand (satisfying C-30)
but no epistemic dimension label. A model knows what the Gatekeeper does but must
infer why adversarial rejection is the right posture for this specific stage.

### C-33 -- Terminal dependency closure enumeration
A standalone terminal block enumerates all inter-criterion loops as an explicit
structured list -- separate from and after the chain trace. Each entry names the
dependency as `{source criterion} output -> {consuming criterion} ({chain node
reference})`. The terminal block enables a reviewer to spot-check closure without
traversing the chain; the chain trace satisfies C-31, the terminal enumeration
satisfies C-33. Every loop named in the chain trace must appear in the enumeration;
any loop missing from either location is a violation.

**FAIL signal**: All inter-criterion dependencies appear as chain node annotations
(satisfying C-31), but no terminal enumeration block exists. A reviewer must
traverse the full chain to reconstruct the dependency graph rather than reading a
single list.

### C-34 -- Forward-reader rationale at verification tokens
Each verification verdict token (e.g., `TRACE-CHECK-VERDICT`, `GESTALT-VERDICT`)
carries an inline forward-reader rationale explaining how the token enables audit
without session replay -- e.g., "A future reader verifies this check ran by
locating this token in the output; no session replay required." The rationale is
stated at the point of token definition, not only in a preamble. Distinct from
C-29 (which requires verification steps to be chain nodes with structural
qualifiers); this requires each token to explain its own auditability protocol so
a reader encountering the token in isolation can immediately understand how to use
it for verification.

**FAIL signal**: Verification tokens appear as chain nodes with structural
qualifiers (satisfying C-29), but carry no forward-reader rationale. A reader
encountering `TRACE-CHECK-VERDICT: PASS` knows the check ran but must re-read the
prompt to understand what that token certifies or how to audit it.

### C-35 -- Explicit output contract declaration
The prompt closes with a numbered final output sequence enumerating every expected
output item in production order, each carrying a structural label tied to its
governing criterion -- e.g., "(with forward-reader protocol, satisfies C-34)",
"(standalone terminal block, satisfies C-33)". The contract makes the expected
output machine-checkable: a reviewer can verify all items are present in order
without re-reading the prompt body. Distinct from C-28 (which requires structural
qualifiers on production chain links); this requires the final output itself to be
declared as an ordered enumeration with per-item criterion labels -- not discovered
by reading the prompt body.

**FAIL signal**: Prompt has an Output line or section naming production phases, but
no numbered sequence enumerating concrete output items with structural labels per
item. A reviewer cannot spot-check completeness without re-reading the full prompt.

### C-36 -- Terminal minimum surprise floor check at output-close
A terminal floor compliance check runs at output-close -- separate from and after
the gate-time floor check (C-15). The check is explicit: "Minimum surprise floor
check (C-15): if fewer than 3 distinct surprises in final output, note the
floor-miss before closing. Do not suppress it." A floor-miss is surfaced as a
named output artifact, not a silent omission. Distinct from C-15 (which requires
the floor to be met at gate time); this requires proof that floor compliance was
verified at the point of output finalization, closing the window where post-gate
revisions could silently drop the count below the floor.

**FAIL signal**: Minimum surprise floor (C-15) is checked only at the gate step.
No terminal check at output-close exists. A revision that reduces the surprise
count after the gate would produce a sub-floor output without detection.

### C-37 -- New-criterion verification tokens as chain nodes at introduction
When a criterion introduces a named verification token (e.g., FLOOR-VERDICT from
C-36), the token is assigned a numbered chain node designation within that
criterion's governing step -- not deferred to a subsequent chain trace review.
The assignment appears inline at first token definition: "FLOOR-VERDICT is NODE
{N} in the production chain." A model executing the governing step in isolation
can see the node assignment without consulting the terminal chain trace. Closes
the V-04 failure mode where a token exists as a named artifact but its chain-node
status is back-filled when the terminal trace is assembled, leaving the governing
step with a token but no traceable identity.

**FAIL signal**: A named verification token is introduced in a criterion's
governing step with no inline NODE declaration. The token's chain-node status
appears only when the terminal trace is written -- a step-local gap where the
token exists without traceable identity, making a C-29 PARTIAL outcome possible
without any per-step violation being visible.

### C-38 -- Verifiable closed-graph closure statement
The closed dependency graph (C-31) closes with a machine-checkable completeness
claim: "No inter-criterion dependency is discoverable only by reading the prompt --
every dependency is named in this chain trace." The claim is falsifiable: a
reviewer can attempt to identify a dependency absent from the trace. Without this
claim, the dependency graph is a list with no self-assessment of completeness --
a reviewer cannot tell whether the graph is exhaustive or merely enumerates what
the author remembered. With the claim, the graph converts to an audit target.
Distinct from C-31 (which requires all dependencies to appear in the chain trace);
this requires the trace to close with an explicit completeness assertion that
invites falsification.

**FAIL signal**: Chain trace names all known inter-criterion dependencies
(satisfying C-31), but carries no machine-checkable closure claim. A reviewer
must independently enumerate all possible dependencies to assess completeness
rather than attempting to disprove a stated claim.

### C-39 -- Self-referential completeness guard on terminal enumeration
The terminal dependency enumeration block (C-33) carries an explicit
self-referential guard: "Any loop absent from this enumeration that appears in the
chain trace is a C-33 violation." The guard makes the enumeration self-auditing:
a reviewer can detect C-33 violations by verifying the guard's presence and by
attempting to find a chain-trace dependency absent from the enumeration list.
Distinct from C-33 (which requires the enumeration block to exist and list all
loops); this requires the enumeration to carry its own gap-detection protocol,
converting the enumeration from a passive list into an auditable contract.

**FAIL signal**: Terminal enumeration block lists all known loops (satisfying C-33)
but carries no self-referential guard statement. A reviewer must traverse the full
chain trace to verify that the enumeration is complete -- the enumeration cannot
be audited in isolation. A V-04-style partial (5 loops listed, 2 missing) is
undetectable without the guard.

### C-40 -- Universal chain node declaration at every production step
Every production, gate, and verification step in the chain carries an inline node
declaration in its step header -- not only steps that introduce new verification
tokens (C-37's scope). The rule: every step self-identifies as `[NODE N: {role}]`
at its own header. Universal coverage makes the chain self-verifying: the node
sequence is recoverable from step headers alone, and back-fill is architecturally
impossible because no step can exist without a declared node identity. Distinct
from C-37 (which targets only token-introduction steps); this requires every step
to bear its chain position at declaration time regardless of whether it introduces
a new token. The V-01 vs V-05 split illustrates the gap: V-01 satisfies C-37 at
the token level (Step 13 only); V-05 satisfies C-40 at the chain level (all steps).

**FAIL signal**: Node declarations appear at verification-token steps (satisfying
C-37) but intermediate production steps carry no inline node identity. The node
sequence is not recoverable from step headers alone -- a reader must consult the
terminal chain trace to determine where non-token steps sit in the chain.

### C-41 -- Step-time node authority with confirmatory trace
The step header is the canonical source of truth for a step's chain node
assignment. The terminal chain trace is a confirmation record -- it verifies what
steps already declared; it does not define, renumber, or override step-time
assignments. The rule: node authority flows from step-execution time to trace
assembly time, never in reverse. This closes the back-fill anti-pattern at the
epistemic level: even if every step carries an inline node header (satisfying C-40),
a prompt that allows the terminal trace to refine or override those headers converts
step-time declarations into anticipatory placeholders rather than authoritative
records, restoring back-fill through the trace assembly step. Distinct from C-40
(which requires every step to carry an inline node declaration); this governs which
record is canonical when step-time and trace-time disagree.

**FAIL signal**: The terminal chain trace assembly step is permitted to back-fill,
renumber, or correct node assignments from step headers. Step headers read as
"anticipated" or "subject to confirmation" -- the terminal trace is definitional,
the step headers are drafts. A model executing the trace assembly step can silently
alter the chain topology established during production.

### C-42 -- Precondition dependency declared in closed graph
When criterion X must be satisfied for criterion Y to be structurally non-vacuous --
Y's mechanism governs the outputs of X, so without X there is nothing for Y to
govern -- the precondition relationship appears in the closed dependency graph (C-31)
as a distinct named entry with type annotation: `C-X (structural precondition) ->
C-Y ({chain node ref})`. A precondition dependency differs from a consuming
dependency: a consuming dependency means X's output feeds Y's mechanism; a
precondition dependency means Y's mechanism is vacuous when X is absent. Both types
must appear in C-31's graph and C-33's terminal enumeration when they exist. Co-
embedding C-X and C-Y in a shared template marker does not satisfy this requirement:
the template abstraction hides the precondition relationship from graph inspection.

**FAIL signal**: The dependency graph names consuming relationships (X's output feeds
Y's mechanism) but omits precondition relationships (X must be satisfied for Y's
authority to be operative). The V-03 failure mode: C-40 and C-41 are co-embedded in
a `| step-time-canonical` template; the C-40 (structural precondition) -> C-41
dependency is absent from C-31 because the template makes the two criteria appear as
a single mechanism rather than as a governed pair.

### C-43 -- Authority rule non-vacuity inline assertion
An authority rule (any rule that declares which record is canonical when two sources
disagree -- e.g., C-41's step-time authority over trace-time) carries an explicit
non-vacuity assertion embedded in its declaration block: "This rule governs [N]
step-header node declarations; N >= 1 confirmed." The assertion converts the
authority rule from a conditional guarantee ("if declarations exist, the trace may
not override them") to a categorical guarantee ("[N] declarations exist AND the trace
may not override them"). Without the inline count, a fully-stated authority rule
coexists undetected with zero governed targets -- the rule passes C-41 structurally
but protects nothing. Distinct from C-42 (which requires the precondition dependency
in the graph); this requires the authority rule itself to embed evidence of governing
scope at declaration time, so a model executing the authority step can self-verify
operativeness without consulting C-40's outputs.

**FAIL signal**: The authority block is structurally complete (satisfying C-41) and
the precondition dependency is named in the graph (satisfying C-42), but the block
carries no inline count or assertion that governed targets exist. The V-02 failure
mode: "the authority declaration is structurally vacuous at execution time" -- C-41
PASS coexists with C-40 FAIL, and the authority rule carries no self-check that
surfaces this vacuity to a model executing the step.

### C-44 -- Detection protocol precedes assembly step
An active structural detection protocol (any mechanism that examines an assembly
step's output for violations -- e.g., a back-fill guard, an override detector, a
renumbering check) is ordered as a chain step that precedes the assembly step it
audits. Its verdict token is a numbered chain node in the chain trace before the
assembly step references or confirms it. The failure mode: embedding the detection
protocol as a sub-step of the assembly step it audits creates a structural
circularity -- the detection runs after the assembly step's main body is produced,
cannot appear as a chain node in the trace being assembled, and reduces from a
prevention mechanism to a post-hoc annotation on an already-assembled artifact.
Distinct from C-37 (which requires verification tokens to be chain nodes at their
introduction point); this requires the structural ordering to place detection
architecturally prior to its target, so the verdict is a chain input rather than
a chain output.

**FAIL signal**: A detection protocol (e.g., BACK-FILL-GUARD) is implemented as a
sub-step of the terminal trace assembly step. The detection verdict token exists but
is produced after the trace body is assembled, cannot be listed as a chain node in
the trace it audits, and its node status is back-filled at terminal trace time. The
V-04 failure mode: BACK-FILL-VERDICT "runs after the trace body as a sub-step" and
"is NOT listed as a named chain node in the chain trace."

### C-45 -- Dedicated authority compliance verdict token
A criterion that requires auditable compliance verification (e.g., C-41's step-time
authority rule) produces a named, dedicated verification verdict token -- it does not
inherit compliance via a structural marker embedded in another criterion's token
(e.g., `| step-time-canonical` appended to C-40's node declaration template). A
structural marker is an attribute of an existing token; a dedicated compliance verdict
is itself a chain node with its own NODE assignment, satisfying C-37 for that token.
Compliance verification that piggybacks on another criterion's token conflates two
audit functions under one token identity: a reader asking "did C-41's compliance
verification run?" must inspect every node declaration for the embedded marker rather
than locating one token. The dedicated token must follow C-37's inline assignment rule
at its governing step: "AUTHORITY-VERDICT is NODE {N} in the production chain."

**FAIL signal**: C-41 compliance is verified via a template marker embedded in the
node declaration format (e.g., `[NODE N: {role} | step-time-canonical]`). No
dedicated AUTHORITY-VERDICT token exists as a chain node. The V-03 failure mode:
"C-41 compliance is enforced via `| step-time-canonical` template marker -- no
dedicated AUTHORITY-VERDICT token introduced." Two audit functions (node identity and
authority compliance) are conflated in one token; neither is independently locatable.

### C-46 -- Assembly step declares structural dependency on detection verdict
The assembly step header declares the detection verdict token (C-44) as an explicit
consumed dependency: the step names the verdict by token name and NODE number as a
required input, so a model executing the assembly step cannot proceed without first
locating the verdict. This closes the gap between C-44 (temporal ordering -- detection
precedes assembly) and architectural blocking (assembly cannot run without the verdict).
A detection step that satisfies C-44 by mere sequencing can still be bypassed if the
assembly step does not reference the verdict in its header. C-46 converts the
sequential constraint into a structural dependency: the assembly step header reads
"requires BACK-FILL-VERDICT (NODE N): PASS" as a named precondition, not a prose
reminder. Distinct from C-44 (which governs temporal ordering); this governs whether
the assembly step is architecturally blocked by an explicit declared dependency visible
in the step header itself.

**FAIL signal**: Detection protocol precedes assembly (satisfying C-44), but the
assembly step header declares no dependency on the detection verdict by name and NODE
reference. A model executing the assembly step in isolation can proceed without
consulting BACK-FILL-VERDICT -- the precondition is implicit in sequencing rather than
explicit in the step declaration. The V-05 gap: detection runs before assembly (C-44
PASS) but assembly step header carries no "requires VERDICT (NODE N): PASS" line.

### C-47 -- Token identity contract names satisfied criteria and explicit non-identity
A verification token's introduction block carries a full identity contract with four
components: (1) the inline NODE assignment (C-37), (2) a forward-reader rationale
(C-34), (3) an enumeration of which criteria this token's existence satisfies (e.g.,
"satisfies C-37/C-41/C-43/C-45"), and (4) an explicit non-identity clause naming what
the token is not (e.g., "not a structural marker embedded in C-40's node declaration
template"). The enumeration of satisfied criteria makes the token's full audit footprint
reconstructible without re-reading each criterion individually; the non-identity clause
prevents conflation with embedded attributes or template markers at other criterion
steps. Distinct from C-37 (which requires the NODE assignment) and C-34 (which
requires the forward-reader rationale); this requires the token introduction to
enumerate its full compliance footprint and its structural non-identity so a reader
encountering the token in isolation can determine exactly what it certifies and what
it is distinguished from -- the full audit function reconstructible without re-reading
the prompt.

**FAIL signal**: Token introduction carries a NODE assignment and forward-reader
rationale (satisfying C-37 and C-34), but no enumeration of which criteria the token
satisfies and no explicit non-identity clause. A reader cannot determine the token's
full audit footprint without re-reading each criterion, and cannot rule out conflation
with a template marker without re-reading C-40's governing step. The V-05 gap:
AUTHORITY-VERDICT carries NODE assignment and rationale but no "satisfies C-37/C-41/
C-43/C-45" enumeration and no "not a structural marker" non-identity clause.

### C-48 -- Authority block cites consumed detection verdict with node reference
The authority block (governing C-41/C-43) opens by citing the consumed detection
verdict token by name and NODE number with its confirmed PASS status before stating
the non-vacuity count: "BACK-FILL-VERDICT (NODE N): confirmed PASS prior to this
step (C-44 satisfied)." The citation operationally links C-43 (non-vacuity count)
and C-44 (pre-assembly ordering) in a single block: a model executing the authority
step can verify both that the detection protocol ran before this step (C-44) and
that the governed targets exist (C-43) without consulting separate steps. Distinct
from C-43 (which requires the non-vacuity count to be embedded in the authority
block) and C-44 (which requires structural pre-ordering of the detection step);
this requires the authority block to produce the operational linkage explicitly by
citing the verdict with its NODE reference, converting two separately-satisfied
criteria into a single verifiable precondition chain at the point of execution.

**FAIL signal**: The authority block contains the non-vacuity count (satisfying C-43)
but does not open with a citation of the detection verdict by name and NODE reference.
A model executing the authority step can verify non-vacuity inline but must locate the
detection step separately to verify C-44 compliance -- the two preconditions are
satisfied in isolation rather than linked operationally in the authority block.

### C-49 -- Version-aligned closing tag on terminal enumeration
The terminal dependency enumeration block (C-33) closes with a version-aligned closing
tag that names all criteria introduced in the current rubric version by bracket
notation: e.g., `[C-42 precondition typed; C-43 count; C-44 pre-assembly ordering;
C-45 dedicated token]`. The tag is machine-checkable against the rubric's version
history: a reviewer can verify the tag lists all new criteria by comparing it to the
"What changed" section without traversing the enumeration body. The tag converts the
enumeration close from a passive count or generic closure statement into a version-
scoped design-intent inventory -- a reviewer can ask "does the enumeration account for
all criteria from this rubric version?" and answer it by reading the closing tag alone.
Distinct from C-39 (which requires a self-referential guard against missing loops in
the chain trace); this requires the enumeration to carry a version-scoped inventory
at its close, auditable against the rubric changelog rather than the chain trace.

**FAIL signal**: Terminal enumeration closes with a count, generic closure statement,
or C-39's self-referential guard (satisfying C-39), but carries no version-aligned
closing tag naming the current round's new criteria. A reviewer cannot verify machine-
checkably that the enumeration accounts for all criteria from the current rubric
version without reading the full enumeration body and cross-referencing the "What
changed" section manually. The V-05 gap: enumeration closes with guard statement
and loop count but no `[C-42..C-45 by name]` inventory tag.

### C-50 -- Per-site dependency graph entries for same-token multi-site consumption
When a verification token is consumed at two structurally distinct sites within the
same prompt -- e.g., at a step header as a declared blocking dependency (C-46) and
inside a step body as an authority block opening citation (C-48) -- each consumption
site appears as a separate named entry in the closed dependency graph (C-31) and the
terminal enumeration (C-33). The two entries are distinguishable by site descriptor:
`C-44+C-46: {token} -> {step} header` and `C-48: {token} -> authority block within
{step}`. Same token, different consumption site, separate graph entry. This criterion
formalizes the V-05 discovery that BACK-FILL-VERDICT (NODE 14) generates two named
dep loops -- one for the C-46 header dep and one for the C-48 authority block
citation -- even though both reference the same token. Prior rounds treated a token's
dep loops as a single entry; C-50 requires per-site granularity when the same token
is structurally consumed in distinct locations. Distinct from C-31 (which requires all
inter-criterion dependencies in the graph); this governs entry granularity when
consumption sites are structurally distinct rather than merely referentially related.

**FAIL signal**: A verification token is consumed at two structurally distinct sites
(step header and step body), but both consumptions appear as a single merged entry in
the dependency graph. The graph correctly names the token but conflates two
structurally different consumption relationships under one entry. A reviewer cannot
determine from the graph whether both consumption sites were accounted for or whether
one site was subsumed into the other.

### C-51 -- Precondition citation precedes compliance footprint within shared block
When a precondition citation (per C-48: detection verdict cited at the open of the
authority block) and a compliance footprint declaration (per C-47: satisfied-criteria
enumeration) coexist in the same authority block, the precondition citation appears as
the first line of the block, before the compliance footprint declaration. Precondition
established before compliance footprint declared: the satisfied-criteria enumeration
in C-47 can truthfully list any criterion whose precondition was verified before the
enumeration was written -- no forward reference is required. This ordering principle
holds whenever a precondition citation and a footprint declaration share a block:
the citation establishes what is already true; the footprint then records what the
token certifies given that truth. Distinct from C-48 (which requires the precondition
citation to precede the non-vacuity count within the block); this governs the ordering
of C-48 and C-47 relative to each other when they coexist in the same block -- the
C-48 opening citation is LINE 1; the C-47 identity contract follows.

**FAIL signal**: A block contains both a C-48 precondition citation and a C-47
four-part identity contract, but the identity contract (or any part of it, including
the satisfied-criteria enumeration) precedes the precondition citation. The
satisfied-criteria enumeration may list C-43 as satisfied before the C-48 citation
has established that the detection verdict was PASS -- the enumeration forward-
references a precondition rather than recording one already in hand. Or the C-48
citation appears after the C-47 block rather than opening the authority block.

### C-52 -- Version-aligned closing tag is self-inventorying
The version-aligned closing tag (C-49) includes the closing-tag criterion itself
among its own entries: e.g., `[C-46 assembly dep declared; C-47 token identity
contract; C-48 authority cites verdict; C-49 version-aligned tag]`. The tag's own
existence and the inclusion of C-49 (or the tag criterion for the current version)
in its inventory proves C-49 is satisfied by its own presence -- the tag is
self-verifying. This converts the closing tag from a passive list of other new
criteria into a self-referential structural closure: a reviewer can verify the tag
criterion is satisfied by reading the tag's own content, without external reference.
Distinct from C-49 (which requires the closing tag to name all new criteria
introduced in the current rubric version); this requires the tag to be self-
inventorying -- listing itself as one of the entries it enumerates, making the
tag's existence its own proof.

**FAIL signal**: The version-aligned closing tag names all other new criteria from
the current rubric version (satisfying C-49) but omits the closing-tag criterion
itself. A reviewer cannot verify the tag is complete by reading its content alone:
the tag is a passive list of other criteria but does not close on itself. A reviewer
must externally confirm that the tag criterion is among the new criteria and then
verify the tag lists it -- the self-verifying property is absent.

### C-53 -- Compound per-site and ordering annotation co-present in single dependency entry
When a dependency graph entry must simultaneously satisfy C-50 (per-site granularity --
naming which structural site consumed the token) and C-51 (ordering intent -- confirming
that the precondition citation is LINE 1 of the authority block), both annotations appear
together within the single dep entry at the consumption site, not distributed across
separate locations. The compound form `[C-48 site -- C-51: LINE 1 -- C-50: entry 2 of 2]`
collocates the site descriptor (C-50) and the ordering declaration (C-51) at the dep
entry itself, making the entry independently auditable: a reviewer reading only that dep
entry can verify both which site is being recorded and whether the ordering was
intentional without look-back to the authority block or a separate C-51 annotation
elsewhere. This is a stronger audit property than satisfying C-50 and C-51 independently
at different structural locations -- the compound form at entry granularity closes the
gap where per-site correctness is verifiable but ordering intent is only recoverable by
navigating to the authority block. The compound annotation emerged as a distinct pattern
only when C-50 and C-51 are simultaneously active; a C-50-only dep entry omits the C-51
component and loses the ordering audit at entry granularity. Distinct from C-50 (which
requires per-site entries) and C-51 (which requires ordering annotation within the
authority block); this requires both annotations to co-exist at the dep entry itself so
that site identity and ordering intent are simultaneously verifiable from a single
structural location.

**FAIL signal**: A dep entry for a second consumption site correctly names the site
descriptor (satisfying C-50) but carries no ordering annotation for the C-51 component.
A reviewer can verify per-site granularity from the entry but must navigate to the
authority block to determine whether the precondition ordering was intentional. The
compound audit property is absent. V-01 (C-50 only) failure mode: dep entry reads
`[C-48 site -- C-50: entry 2 of 2]` with no C-51 LINE-1 annotation -- the entry is
site-correct but not ordering-auditable in isolation.

### C-54 -- Self-detecting gap contract stated inline on version-aligned closing tag
The version-aligned closing tag (C-49, extended by C-52 to be self-inventorying) carries
an explicit gap-detection guarantee stated inline at the tag site: "A tag absent C-52
would fail C-52 by that absence -- gap is self-detectable." The guarantee converts the
self-referential tag from a structural design property (C-52) into an auditable contract
with its own gap-detection protocol embedded at the point of use. A reviewer encountering
the tag does not need to consult the rubric changelog to determine whether the tag is
complete: the tag's own guarantee statement identifies the failure mode if the self-
inventorying criterion is missing, and the absence of the guarantee statement is itself a
detectable gap. This property is qualitatively different from C-52's self-referential
closure: C-52 requires the tag to include itself as an entry (structural completeness);
C-54 requires the tag to state what its own absence would mean (gap-detection protocol).
A tag satisfying C-52 but lacking the inline guarantee is structurally complete but not
self-diagnosing -- a reviewer can verify completeness only by checking for the entry,
not by reading the tag's own stated protocol. Distinct from C-52 (which requires the
self-inventorying entry to be present); this requires the tag to carry an inline
statement of its own gap-detection logic, making the absence of the self-inventorying
criterion diagnosable from the tag's content alone without external rubric consultation.

**FAIL signal**: The closing tag includes the self-inventorying criterion as an entry
(satisfying C-52) but carries no inline gap-detection guarantee statement. A reviewer
can verify C-52 is satisfied by finding the entry in the tag, but the tag does not
state what its own absence would constitute -- the self-detecting property is latent
in the structure but not articulated as an auditable protocol at the tag site. The R15
V-03 (C-52 only) failure mode: tag names C-52 in its inventory and proves self-
referential closure, but carries no guarantee of the form "absence of this entry is
a self-diagnosable violation."

---

## Version history

| Version | Change |
|---------|--------|
| v1 | Essential C-01..C-05 |
| v2 | Add Recommended C-06..C-08 |
| v3 | Add Aspirational C-09..C-14 |
| v4 | Add C-15..C-19 (structural enforcement, correction-encoding, failure framing) |
| v5 | Add C-20..C-22 (co-validation gate, derivation scaffold, failure-first ordering) |
| v6 | Add C-23..C-25 (impact triage as pre-write scaffolding, traceability closure, two distinct named roles) from R5 excellence signals |
| v7 | Add C-26..C-28 (output-level gestalt summary test, adversarial function declaration, full-chain traceability with structural qualifiers) from R6 excellence signals |
| v8 | Add C-29..C-31 (verification steps as chain nodes, sub-step identity+function co-activation, closed dependency graph) from R7 V-05 excellence signals; aspirational 20->23 criteria, max 69 pts, total 150 |
| v9 | Add C-32..C-34 (epistemic dimension labels at role invocations, terminal dependency closure enumeration, forward-reader rationale at verification tokens) from R8 V-05 excellence signals; aspirational 23->26 criteria, max 78 pts, total 159 |
| v10 | Add C-35..C-36 (explicit output contract declaration, terminal minimum surprise floor check at output-close) from R9 V-05 excellence signals; aspirational 26->28 criteria, max 84 pts, total 165 |
| v11 | Add C-37..C-39 (new-criterion verification tokens as chain nodes at introduction, verifiable closed-graph closure statement, self-referential completeness guard on terminal enumeration) from R10 V-05 excellence signals; aspirational 28->31 criteria, max 93 pts, total 174 |
| v12 | Add C-40..C-41 (universal chain node declaration at every production step, step-time node authority with confirmatory trace) from R11 V-05 excellence signals; aspirational 31->33 criteria, max 99 pts, total 180 |
| v13 | Add C-42..C-45 (precondition dependency in closed graph, authority rule non-vacuity assertion, detection-before-assembly ordering, dedicated authority compliance verdict token) from R12 V-01..V-04 excellence signals; aspirational 33->37 criteria, max 111 pts, total 192 |
| v14 | Add C-46..C-49 (assembly step declares dependency on detection verdict, token identity contract names satisfied criteria and non-identity, authority block cites consumed detection verdict with node reference, version-aligned closing tag on terminal enumeration) from R13 V-05 excellence signals; aspirational 37->41 criteria, max 123 pts, total 204 |
| v15 | Add C-50..C-52 (per-site dependency graph entries for same-token multi-site consumption, precondition citation precedes compliance footprint within shared block, version-aligned closing tag is self-inventorying) from R14 V-05 excellence signals; aspirational 41->44 criteria, max 132 pts, total 213 |
| v16 | Add C-53..C-54 (compound per-site and ordering annotation co-present in single dep entry, self-detecting gap contract stated inline on version-aligned closing tag) from R15 V-05 excellence signals; aspirational 44->46 criteria, max 138 pts, total 219 |
