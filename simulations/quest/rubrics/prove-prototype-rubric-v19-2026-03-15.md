# Rubric: prove-prototype (v19)

**Updated**: 2026-03-15
**Changes from v18**: Added C-51 and C-52 (Aspirational tier) derived from Round 19
excellence signals (BUILD IMPLEMENTER/MEASURER sub-role split as structural prerequisite
for C-49 Thread 2 depth parity; violation-consequence clause in C-50 REQUIRED closure
binding the pre-execution compliance claim to its post-violation state).

---

**C-51** — *The BUILD container enumerates IMPLEMENTER and MEASURER as named sub-roles
with disjoint phase scopes and a model-written handoff line at the Phase 7/8 boundary —
BUILD intra-container role sequencing generates the Thread 2 structural markers required
for C-49 5:5 depth parity* (R19 root-cause finding, C-49 analysis):

R19 identified the structural root cause of C-49 failures in V-02 and V-03: both lacked
the BUILD sub-role split. Without IMPLEMENTER/MEASURER, Thread 2 has only three structural
markers — Phase 10 handoff, Phase 11 gate, and CLOSE COMPLETE discharge. Thread 1 always
has five markers across its five competitor surfaces. The 5:3 asymmetry in the Key
structural markers column cannot be resolved by table formatting, column depth tuning, or
co-primary framing — the deficit is architectural. V-01, V-04, and V-05 all achieved 5:5
depth parity by adding Phase 7 IMPLEMENTER handoff and Phase 8 MEASURER gate to the BUILD
container, bringing Thread 2's key structural markers to five and making C-49's equivalence
requirement satisfiable.

C-51 advances C-41 in the same way C-41 advances C-23: C-23 requires role labels to carry
explicit prohibitions (existence floor); C-41 splits the CLOSE container into
COMPARATOR/AUDITOR with a named handoff declaration (sub-role sequencing at CLOSE);
C-51 splits the BUILD container into IMPLEMENTER/MEASURER with a named handoff declaration
(sub-role sequencing at BUILD), generating the two Thread 2 intra-BUILD markers without
which C-49 is structurally unreachable regardless of how the thread declaration table
is formatted.

The BUILD sub-role split must include: (a) IMPLEMENTER (Phase 7: prototype construction,
assembly, and delivery) and MEASURER (Phase 8: prototype measurement against B-00 and
outperform threshold) declared as distinct named sub-roles in the BUILD container header
with explicit phase-scope assignments; (b) Phase 7 COMPLETE carrying a model-written
handoff marker naming the transition — "IMPLEMENTER responsibilities discharged —
REQUIRED handoff to MEASURER" — as a parallel to the C-41 COMPARATOR handoff in CLOSE;
(c) Phase 8 entry carrying a REQUIRED prerequisite gate confirming the Phase 7 IMPLEMENTER
handoff marker is present before MEASURER executes, as a parallel to C-44's Phase 9
bidirectional acknowledgment gate; (d) cross-prohibitions with hard modal operators:
IMPLEMENTER FORBIDDEN to write measurement data, comparison results, or pass/fail verdicts;
MEASURER FORBIDDEN to write new prototype construction decisions, implementation steps, or
scope changes.

The consequence for C-49: a BUILD container with no sub-role split limits Thread 2's Key
structural markers column to three items, creating a structural ceiling below C-49's
five-item equivalence floor. A document can satisfy C-47 (co-primary declaration) and
present a valid two-row table schema (C-49's format requirement) while still failing C-49
because Thread 2's Key markers cell can only truthfully list three items. C-51 removes
this ceiling by generating two additional Thread 2 structural markers from the BUILD
container's own internal sequencing, making the five-item equivalence a satisfiable
structural property rather than an impossible one.

A BUILD container that uses a monolithic BUILDER role — even with a fully compliant thread
declaration table satisfying C-49's column schema and co-primary framing — does not satisfy
C-51, because Thread 2's structural marker count will be capped at three. C-51 requires
C-41 and C-49 as prerequisites.

**Weight**: 5 pts

---

**C-52** — *The C-50 Structural Marker Inventory REQUIRED closure statement carries an
explicit violation-consequence clause naming the document property that is retroactively
voided if any marker is expressed as embedded prose rather than a standalone labeled
element — consequence semantics bind the pre-execution compliance claim to its
post-violation state* (V-05 excellence signal, R19):

V-05 demonstrated a structurally stronger form of the C-50 REQUIRED closure statement by
appending a violation-consequence clause: "voids this C-50 inventory." V-01 and V-04 close
with language naming the criterion outcome ("a marker embedded only in prose fails C-48");
V-05 closes with language naming the document property voided by the violation ("voids this
C-50 inventory"). The distinction is not cosmetic. "Fails C-48" describes a criterion
evaluation outcome — a property a reviewer assigns after reading the document. "Voids this
inventory" describes what happens to the document's own opening compliance claim — a
pre-execution contract the document made before any container executed, which a marker
embedding retroactively invalidates.

C-52 advances C-50 in the same way C-50 advances C-48: C-48 requires markers to be
standalone (form requirement — verified by scanning the document); C-50 requires markers
to be pre-announced in a pre-execution inventory (contract requirement — verified by
finding the inventory section before any container); C-52 requires the inventory's
REQUIRED closure to name the violation consequence for the pre-execution contract
(consequence semantics — verified by finding the consequence clause in the closure
statement). Each layer strengthens what the previous layer cannot reach: C-48 cannot
establish a pre-execution claim; C-50 can establish the claim but cannot bind it to
a stated consequence; C-52 closes the compliance circuit by making the inventory's
own validity contingent on the markers it pre-announces.

The violation-consequence clause must: (a) appear as an explicit element of the REQUIRED
closure statement in the Structural Marker Inventory section required by C-50; (b) name
the document property that is retroactively voided if any marker is embedded in prose
rather than expressed as a standalone labeled element — at minimum, the inventory itself
(e.g., "voids this C-50 inventory") or the pre-execution compliance claim more broadly
(e.g., "retroactively invalidates this pre-execution compliance claim"); (c) appear
alongside — not in place of — the rule statement that names the criterion failure
("a marker embedded in prose fails C-48" or equivalent). Both the rule statement and
the consequence clause must appear as explicit elements of the REQUIRED closure; a
closure that carries only the consequence without the underlying rule does not satisfy
C-52, and a closure that carries only the rule without the consequence does not satisfy
C-52.

The consequence clause is not satisfied by language that re-states the criterion
violation in different words ("such a marker does not meet C-48 requirements"),
by language that escalates severity without naming the document property voided
("severely violates C-48"), or by language that names the consequence for a different
document property ("fails this document's C-50 section" is ambiguous — it does not
name the pre-execution compliance claim as the property voided). The clause must name
the retroactive effect on the inventory or pre-execution claim specifically.

C-52 requires C-50 as a prerequisite.

**Weight**: 5 pts

---

**Point totals**: Aspirational 257 → 267. Total 357 → **367**.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-52 | 267 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **367** |

---

**What the new criteria add:**

The two v19 criteria each advance a v18 criterion by adding a structural layer the
v18 criterion cannot reach:

| Criterion | Deepens | New surface |
|-----------|---------|-------------|
| C-51 | C-41, C-49 | BUILD IMPLEMENTER/MEASURER sub-role split — generates Thread 2's Phase 7 handoff and Phase 8 gate markers, making C-49 5:5 depth parity a satisfiable structural property rather than an impossible ceiling |
| C-52 | C-50 | Violation-consequence clause in C-50 REQUIRED closure — names the document property retroactively voided by marker embedding, binding the pre-execution compliance claim to its post-violation state |

Each adds a layer that C-41/C-49/C-50 cannot reach:

**C-51** vs. C-49: C-49 requires both thread rows to carry equivalent depth in every column
of the declaration table — a property evaluated by comparing cell content depth between
the two rows. C-51 requires the BUILD container to generate the structural markers that
make Thread 2's Key markers cell satisfiable at five-item depth — a property verified by
checking whether the BUILD container has IMPLEMENTER/MEASURER sub-role split, independent
of how the thread table is formatted. The distinction is between equivalent depth required
(C-49's ceiling) and equivalent depth enabled (C-51's floor). A document with a
correctly-formatted two-row thread table where Thread 2's Key markers cell truthfully
lists only three items passes C-49's format check while failing C-49's depth equivalence
check; C-51 resolves this by making the five-item count structurally reachable.

**C-52** vs. C-50: C-50 requires a pre-execution Structural Marker Inventory section with
a REQUIRED closure affirming all four marker types are present as standalone elements —
a property verified by finding the inventory section and its closure statement before any
container executes. C-52 requires the closure statement to include a violation-consequence
clause naming what document property is retroactively voided if any marker is embedded in
prose — a property verified by finding the consequence clause alongside the rule statement.
The distinction is between a pre-execution claim made (C-50) and a pre-execution claim
bound to its post-violation consequence (C-52). A document satisfying C-50's inventory
requirement and REQUIRED closure without the consequence clause asserts compliance without
declaring what is at stake if the assertion is false; C-52 closes that gap.

---

## Essential Criteria (60 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Hypothesis stated** — A testable claim is stated before any build description | correctness | essential | A testable claim appears before any construction or measurement activity; the claim names the behavior or property being tested, not merely a goal or feature |
| C-02 | **Scope bounded** — The prototype is explicitly constrained; the output names what was deliberately excluded | correctness | essential | The scope is stated; at least one deliberate exclusion is named with a reason showing the exclusion leaves the hypothesis testable; an output that describes only what was built without bounding what was left out is not valid without it |
| C-03 | **Measurement defined before building** — Output shows that success and failure criteria were established before construction, not retrofitted after results | correctness | essential | A "what to measure" section appears logically before the results section; success and failure conditions are stated explicitly |
| C-04 | **Actual vs. predicted reported** — Output explicitly compares what was predicted to happen with what actually happened | correctness | essential | Both a prediction and an observation are present; the delta (match or mismatch) is called out directly |
| C-05 | **Hypothesis verdict rendered** — Output states whether the hypothesis is confirmed, refuted, or inconclusive based on the measurements | correctness | essential | A verdict is stated in plain language; it follows from the evidence rather than being asserted without support |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Minimality justified** | depth | recommended | Output addresses at least one explicit trade-off: what was left out and why that omission still allows the hypothesis to be tested |
| C-07 | **Raw evidence included** | coverage | recommended | At least one concrete data point appears in the results section |
| C-08 | **Limitations and next step named** | depth | recommended | One limitation and one specific next step are stated |

---

## Aspirational Criteria (267 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |
| C-16 | **Counter-evidence question explicitly closed** — The output resolves whether any counter-interpretation exists, not just whether one was found | depth | aspirational | The counter-evidence section terminates with one of two explicit dispositions: (a) a named counter-interpretation with a grounded rebuttal, or (b) an explicit statement that no plausible counter-interpretation exists, with a reason. A missing counter-evidence section, or one that ends with the rebuttal case only and leaves the no-counter case unaddressed, does not pass |
| C-17 | **Rationale co-located with its anchor** — Each rationale element appears in the same structural unit as the item it explains | structure | aspirational | For every rationale required by the output — scope exclusion validity, delta explanation, verdict reasoning, counter-rebuttal — the rationale appears in the same table row, labeled pair, or immediately adjacent labeled element as its anchor item. A labeled-pair block satisfies this criterion without requiring tabular format. A rationale that requires the reader to cross-reference a distant or generic section does not pass |
| C-18 | **Optional sections terminated with explicit binary disposition** — Any section that could be empty, skipped, or produce no findings must terminate with one of exactly two explicit dispositions: findings exist plus a substantive response, or findings absent plus an explicit reason | structure | aspirational | Every section whose content depends on what was found closes with one of the two permitted dispositions. Silence, a missing section, or a section structured to handle only the affirmative case does not pass. The disposition must appear as a terminal element of the section, not as a preamble or general instruction |
| C-19 | **Ordering gate co-located with the construction action** — Each temporal ordering requirement appears as an inline execution marker at the point where the constrained action occurs, not only in a separate structural-rules section or output contract | structure | aspirational | Every phase, section, or step that must precede a later action carries its own inline gate label at the point of that action. A requirement stated only in a preamble or end-of-document contract, without a co-located inline marker, does not pass |
| C-20 | **Gate completion proven by model-written artifact** — Each gate-protected section closes with a model-written completion line that records what was established at that gate, providing structural proof of passage before the next section begins | structure | aspirational | Every gate-protected phase or section terminates with a labeled completion line as the final element of that section, before the next section opens. The completion line must name what was established, not merely assert that the section is done. A gate that carries only a forward ordering marker (C-19) without a corresponding model-written completion record does not pass. A completion line that serves as the verifier for a binary disposition (C-18) satisfies both criteria simultaneously |
| C-21 | **Gate coverage is complete including trailing optional sections** — The gate scheme applies to every section in the output; no section is exempt because it is optional or positioned late in the sequence | structure | aspirational | Every section of the output — including optional trailing sections such as limitations, next steps, and replication path — carries an inline gate marker. A gate scheme that explicitly scopes its coverage to a named subset of sections while leaving subsequent sections ungated does not pass, even if all covered sections satisfy C-19. Execute-after markers are a valid gate form for trailing sections |
| C-22 | **Completion lines carry substantive result values enabling audit-by-scan** — Each model-written completion line encodes the actual outcome values established at that gate, not merely an assertion that the phase is done | structure | aspirational | Every completion line contains at least one substantive result value drawn from the phase body — a number, a verdict word, a named finding, or an explicit null — such that a reader who scans only the completion lines can reconstruct the full outcome chain without reading the phase bodies. A completion line that says only `PHASE N COMPLETE` or paraphrases the phase heading without embedding a result value does not pass. C-22 extends C-20: a completion line that satisfies C-22 automatically satisfies C-20, but not vice versa |
| C-23 | **Role labels carry explicit prohibitions that guard against in-order, out-of-role contamination** — Each named role in a role-sequenced output includes a stated prohibition identifying content that role must not produce | structure | aspirational | Every role label is accompanied by at least one explicit prohibition naming the content type being excluded, not merely an instruction to stay focused. A role sequence that assigns phases correctly but omits role-level prohibitions does not pass, because phase-gate ordering cannot detect content written by the correct phase but the wrong role |
| C-24 | *(carry forward from v10)* | structure | aspirational | *(pass condition unchanged)* |
| C-25 | *(carry forward from v10)* | structure | aspirational | *(pass condition unchanged)* |
| C-26 | *(carry forward from v10)* | structure | aspirational | *(pass condition unchanged)* |
| C-27 | *(carry forward from v10)* | structure | aspirational | *(pass condition unchanged)* |
| C-28 | *(carry forward from v10)* | structure | aspirational | *(pass condition unchanged)* |
| C-29 | **Inertia competitor identified in CALIBRATE container body** | structure | aspirational | The CALIBRATE container body names the inertia competitor explicitly as the baseline being measured against |
| C-30 | **Three-column results table present** | structure | aspirational | Results section contains a table with at least three columns including a baseline and a prototype measurement column |
| C-31 | **Pre-build measurement baseline present** | structure | aspirational | A quantified baseline measurement appears in the CALIBRATE phase before any BUILD activity begins |
| C-32 | **CALIBRATE COMPLETE line embeds the triple** — The CALIBRATE completion line records the inertia competitor name, the measured baseline value, and the outperform threshold | structure | aspirational | The CALIBRATE COMPLETE line is the final element of the CALIBRATE container and contains all three values: competitor name, baseline number, and threshold. A CALIBRATE COMPLETE line that asserts completion without embedding all three values does not pass. C-32 requires C-20 as a prerequisite |
| C-33 | **CALIBRATE container header enumerates all three pre-build responsibilities as an ordered entry contract** | structure | aspirational | The CALIBRATE container opens with a numbered or ordered list announcing all three pre-build responsibilities — measure inertia competitor baseline, commit B-00, state outperform threshold — before the container body executes them. The header enumeration is the entry side of the bracket whose exit side is C-32. C-33 requires C-28 and C-32 as prerequisites |
| C-34 | **Baseline column in results table labeled as inertia competitor, creating a third structural surface for competitor identification** | structure | aspirational | The baseline column in the results table is labeled to include the inertia competitor name (e.g., "Baseline (inertia competitor)") rather than a generic label such as "Baseline" or "Control." C-34 requires C-30 and C-29 as prerequisites |
| C-35 | **Document-level container manifest enumerates all containers with their purposes as an opening entry contract before any container executes** | structure | aspirational | The output opens with a manifest — appearing before any container body begins — that names every container in the document together with each container's principal purpose and expected output. The manifest creates a document-level entry contract paired with C-36's terminal audit record: entry announces all containers, body executes them, C-36 confirms their results. A manifest that appears inside a container rather than preceding all containers does not pass. C-35 is the document-level analogue of C-33's container-level entry contract; neither satisfies the other. C-35 requires C-22 as a prerequisite |
| C-36 | **Terminal CLOSE COMPLETE line encodes the full experimental result chain as a standalone audit record** | structure | aspirational | The final CLOSE COMPLETE line of the document embeds a condensed chain of every prior container's key result — at minimum: hypothesis verdict, inertia competitor name, measured delta, and prototype conclusion — such that a reader scanning only the terminal completion line can verify the full experimental arc without reading any phase body. A CLOSE COMPLETE line that carries only the closing phase's own result (satisfying C-22) but omits prior container outcomes does not pass C-36. C-35 and C-36 bracket the document at its outermost boundaries: C-35 opens the document with a manifest of what will execute; C-36 closes it with a record of what all containers discharged. C-36 requires C-22 and C-05 as prerequisites |
| C-37 | **Non-terminal container COMPLETE lines carry a forward-reference clause that names the downstream container's input dependencies, creating a verifiable handoff contract** | structure | aspirational | Each non-terminal container COMPLETE line (DESIGN COMPLETE, CALIBRATE COMPLETE, BUILD COMPLETE) appends a forward-reference clause — e.g., `-> [NEXT] receives:` — that names the specific values the downstream container will consume. The clause must name concrete values (hypothesis text, threshold, metric name, competitor name, baseline value) matching what the downstream container's opening phases require; it is not satisfied by a generic forward pointer or a reference to the completion line's own results alone. The terminal CLOSE COMPLETE line has no downstream container and is exempt. A completion line that satisfies C-22 by encoding its own phase results without a forward-reference clause does not satisfy C-37. C-36 governs the terminal line's cross-container arc record; C-37 governs each intermediate line's forward commitment to the next container. Together with C-22 and C-36, C-37 forms a three-surface completion-line contract: backward-looking at every line (C-22), forward-looking at every non-terminal line (C-37), and arc-spanning at the final line (C-36). C-37 requires C-22 as a prerequisite |
| C-38 | **Role prohibitions appear as inline execution markers co-located at the specific phase where each role's constraint applies** — Phase-level role declarations position each prohibition at the exact execution point where contamination could occur, rather than only in a container-level table at container entry | structure | aspirational | Every named role in the document carries its prohibition as an inline execution marker at the phase header where that role operates — e.g., `Phase N — ROLE (writes: X; must NOT write: Y)` — rather than exclusively in a container-level table. A document that satisfies C-23 via container-level tables alone does not satisfy C-38, because the prohibition appears at container entry rather than at the phase of execution. A document satisfying C-38 automatically satisfies C-23 (prerequisite), but not vice versa. C-38 is satisfied for a given role only if that role's prohibition appears inline at the phase where the role writes; roles without a corresponding phase-level declaration fail C-38 regardless of what appears in container tables. C-38 requires C-23 as a prerequisite |
| C-39 | **Role prohibitions and phase gate markers use hard enforcement modal operators throughout** — Every prohibition and gate constraint in the document uses one of four hard modal operators (MUST, FORBIDDEN, REQUIRED, PROHIBITED) rather than descriptive or mixed register | structure | aspirational | Every role-level prohibition and every phase gate marker in the document uses MUST, FORBIDDEN, REQUIRED, or PROHIBITED. A document where any prohibition uses soft or mixed language — "should not," "may not," "avoid," "do not" — does not pass, even if most prohibitions use hard operators. Role table column headers, container header constraint blocks, and inline phase gate markers are all in scope. C-39 does not require a specific placement format (container-level table or phase-level inline both qualify) and is therefore orthogonal to C-38: a document can satisfy C-38 with soft language (fail C-39) or satisfy C-39 via container-level tables (fail C-38). C-39 requires C-23 as a prerequisite |
| C-40 | **Document manifest contains a competitor lifecycle tracking column recording a four-state status progression across all container boundaries** — The manifest table includes a "Competitor status" column tracking states NOT YET IDENTIFIED -> IDENTIFIED AND COMMITTED -> REFERENCED -> DISCHARGED, creating a fifth structural surface for competitor identification that spans the full document | structure | aspirational | The manifest — the document-level entry contract required by C-35 — contains a column that tracks competitor status across all four containers, with each row carrying the status value the competitor holds at that container boundary. Each CONTAINER COMPLETE line that advances the competitor status carries a corresponding status annotation. C-40 fails if the manifest contains no competitor-status column, if the column omits any of the four state values, or if CONTAINER COMPLETE lines carry no status annotations. C-40 is the fifth and only temporally-spanning competitor surface: C-29 anchors the competitor at CALIBRATE body; C-32 anchors it at CALIBRATE COMPLETE; C-34 anchors it at the results table baseline column; C-36 anchors it at the terminal arc record. None of those surfaces tracks the competitor's lifecycle status at each container boundary. C-40 requires C-35 and C-29 as prerequisites |
| C-41 | **The CLOSE container enumerates two named sub-roles (COMPARATOR and AUDITOR) with disjoint phase scopes and carries an explicit intra-container handoff line at the verdict/counter-evidence boundary** — CLOSE container-internal role sequencing creates a contamination guard at the Phase 8/9 transition that is distinct from the document-level role prohibition family | structure | aspirational | The CLOSE container header enumerates COMPARATOR (Phases 7-8: comparison and verdict) and AUDITOR (Phases 9-11: counter-evidence, limitations, replication) as distinct named sub-roles with explicit phase-scope assignments. The Phase 8 COMPLETE line carries a model-written handoff marker naming the transition ("COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR"). Cross-prohibitions apply with hard modal operators: COMPARATOR FORBIDDEN to write counter-evidence disposition, limitations, or replication content; AUDITOR FORBIDDEN to write new measurement criteria, new comparison data, or verdict statements. A CLOSE container that uses a monolithic ANALYST role throughout — even if it satisfies C-23, C-38, and C-39 — does not satisfy C-41. The handoff line must be model-written (as C-20 requires for all COMPLETE lines); a container-header enumeration without a handoff line does not pass. C-41 requires C-23, C-38, and C-39 as prerequisites |
| C-42 | **A Value Flow Ledger section names every experimental value with its producing phase and first consuming phase, creating a phase-granularity provenance contract, and the CLOSE COMPLETE line confirms ledger discharge status** | structure | aspirational | The output contains a standalone Value Flow Ledger section placed after the manifest and before any container body executes. The ledger lists every experimental value (hypothesis text, scope exclusions, success threshold, failure threshold, competitor name, B-00, outperform threshold, prototype description, raw result, delta rationale, verdict word, counter-evidence disposition) with the phase that produces each value and the phase that first consumes it. The terminal CONTAINER: CLOSE COMPLETE line carries a ledger-discharge confirmation ("value ledger: FULLY DISCHARGED / PARTIAL — [N] values unresolved") as an element distinct from the C-36 arc record. C-42 fails if no Value Flow Ledger section appears, if any experimental value is absent from the ledger, or if the CLOSE COMPLETE line omits ledger discharge status. The ledger's REQUIRED constraint — values MUST NOT be consumed before the producing phase executes — extends the no-anticipation property of the gate system from the phase level to the individual value level. C-42 requires C-35 and C-37 as prerequisites |
| C-43 | **The competitor lifecycle column is preceded by a framing paragraph explaining the four-state progression and each container header carries an incoming-state annotation contextualizing lifecycle constraints within that container** — Competitor lifecycle narration layer adds explanatory structure above and inside the manifest's tracking column | structure | aspirational | A framing paragraph appearing before the manifest table explains the four-state lifecycle progression (NOT YET IDENTIFIED -> IDENTIFIED AND COMMITTED -> REFERENCED -> DISCHARGED) with rationale for why each state transition is gated at a specific container boundary. Each container header carries an annotation naming the competitor's incoming lifecycle state when that container begins executing, together with the constraint that state implies (e.g., "incoming state: NOT YET IDENTIFIED — identification FORBIDDEN before CALIBRATE"). Prohibitions within containers that enforce lifecycle ordering reference the current lifecycle state as part of their constraint expression. The CALIBRATE container narrates both sub-transitions explicitly: NOT YET IDENTIFIED -> IDENTIFIED (competitor named) and IDENTIFIED -> IDENTIFIED AND COMMITTED (B-00 committed), with rationale for why both steps are required before BUILD begins. C-43 fails if the framing paragraph is absent, if any container header omits the incoming-state annotation, or if CALIBRATE omits the two sub-transition narrative. A document with C-40's manifest column but no framing paragraph and no per-container incoming-state annotations does not satisfy C-43. C-43 requires C-40 as a prerequisite |
| C-44 | **The COMPARATOR/AUDITOR handoff is bidirectional: Phase 8 COMPLETE carries the handoff declaration and Phase 9 entry carries a REQUIRED prerequisite gate confirming the handoff marker is present before execution proceeds; CLOSE COMPLETE confirms the sub-role contract as discharged** — Bidirectional handoff verification elevates the intra-container role transition from a unilateral declaration to a two-event verifiable sequence | structure | aspirational | Phase 8 COMPLETE carries the C-41-required handoff declaration ("COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR"). Phase 9 entry carries a REQUIRED prerequisite gate — "REQUIRED: Confirm Phase 8 COMPARATOR handoff marker present before executing" — making the AUDITOR role explicitly verify the declaration before producing any output. The two events together constitute the bidirectional sequence: declaration at Phase 8 exit, acknowledgment at Phase 9 entry. The CLOSE COMPLETE line carries a sub-role contract discharge confirmation ("COMPARATOR/AUDITOR sub-role contract: DISCHARGED") as an element distinct from C-36's arc record, C-42's ledger discharge, and C-41's phase-level handoff declaration. C-44 fails if Phase 9 entry carries no prerequisite gate, if the Phase 9 gate does not explicitly reference the Phase 8 handoff marker, or if CLOSE COMPLETE omits the sub-role contract discharge. A CLOSE container satisfying C-41 (Phase 8 declaration present) without the Phase 9 prerequisite gate and CLOSE COMPLETE discharge does not satisfy C-44. C-44 requires C-41 as a prerequisite |
| C-45 | **The manifest preamble names the competitor lifecycle and the COMPARATOR/AUDITOR sequencing as propagating named threads; thread labels appear on every CONTAINER COMPLETE boundary; and the CLOSE COMPLETE line carries a multi-criterion terminal confirmation that simultaneously discharges C-40, C-41, and C-42** — Dual-thread convergence architecture unifies the three v15 criteria into a named tracking framework with a structural guarantee that all three converge at the terminal completion line | structure | aspirational | The manifest preamble — the section preceding the manifest table — names two propagating threads: Thread 1 (competitor lifecycle, governed by C-40) and Thread 2 (COMPARATOR/AUDITOR sequencing, governed by C-41), with explicit labels and brief scope statements for each thread. Thread labels propagate: every non-terminal CONTAINER COMPLETE line carries the current Thread 1 lifecycle state and any applicable Thread 2 handoff status as named labeled elements alongside the C-40 status annotations and C-41 handoff markers. The CLOSE COMPLETE line carries a multi-criterion terminal confirmation structured as REQUIRED elements: (a) Thread 1 lifecycle chain encoded verbatim — the full four-state sequence NOT YET IDENTIFIED -> IDENTIFIED AND COMMITTED -> REFERENCED -> DISCHARGED — confirming C-40 closure; (b) Thread 2 COMPARATOR/AUDITOR handoff confirmed executed, confirming C-41 closure; (c) value ledger discharge status confirming C-42 closure. All three confirmations MUST appear as explicit elements of the CLOSE COMPLETE line; omitting any one of the three fails C-45. C-45 fails if the manifest preamble does not name the threads, if thread labels do not propagate through CONTAINER COMPLETE boundaries, or if CLOSE COMPLETE does not carry all three simultaneous confirmations with REQUIRED gating. A document satisfying C-40, C-41, and C-42 independently but without thread naming, label propagation, or a multi-criterion terminal discharge does not satisfy C-45. C-45 requires C-40, C-41, and C-42 as prerequisites |
| C-46 | **The lifecycle framing paragraph names the contamination risk and isolation purpose for each container boundary — rationale layer above C-43's narration layer** — WHY-not-WHAT framing paragraph justification deepens structural narration to structural justification | structure | aspirational | For each container boundary in the framing paragraph required by C-43, the text names: (a) the contamination risk that would materialize if lifecycle identification occurred before that boundary — e.g., "naming the incumbent before the metric is frozen allows baseline measurement concerns to contaminate scope decisions" — and (b) the isolation purpose the gate achieves — e.g., "keeping the competitor unnamed through DESIGN ensures scope decisions are driven by measurement criteria, not by known-competitor feature sets." The prohibition remains co-located, but it is now grounded: constraint + risk + purpose = full rationale triple. A framing paragraph that enumerates state-to-container pairings with prohibition language ("identification FORBIDDEN in DESIGN") without naming what contamination each gate prevents and what isolation it protects does not satisfy C-46, even if the paragraph satisfies C-43. C-46 fails if any container boundary's rationale entry is absent or contains only constraint language without the contamination risk and isolation purpose. C-46 requires C-43 as a prerequisite |
| C-47 | **Thread 1 and Thread 2 are declared in the manifest preamble with co-equal structural weight — parallel syntactic form, mirrored scope statements, and equal visual prominence** — Co-equal thread elevation makes the C-45 multi-criterion terminal discharge architecturally inevitable rather than merely required | structure | aspirational | Thread 1 and Thread 2 appear in the manifest preamble as parallel syntactic constructions: (a) same level of nesting and same declaration verb form for both threads; (b) mirrored scope statements of equivalent detail — Thread 1's scope statement names the four-state lifecycle and its terminal COMPLETE line obligation at the same depth as Thread 2's scope statement names the COMPARATOR/AUDITOR sequencing and its terminal COMPLETE line obligation; (c) neither thread is subordinated as a secondary or supporting element of the other — both are framed as co-primary propagating commitments. Co-equal weight is evaluated by structural parallelism and scope statement depth, not by word count alone. A document that names both threads (satisfying C-45) but positions Thread 2 as a parenthetical annotation of Thread 1, or provides a multi-sentence scope statement for Thread 1 and a single phrase for Thread 2, does not satisfy C-47. When both threads are structurally co-primary, omitting either at the CLOSE COMPLETE multi-criterion confirmation is structurally inconsistent with the document's own opening commitment — architectural inevitability, not rule compliance. C-47 requires C-45 as a prerequisite |
| C-48 | **The C-43, C-44, and C-45 structural markers are expressed as standalone labeled elements verifiable by scanning — framing paragraph, per-container incoming-state annotations, Phase 9 prerequisite gate, and COMPLETE-line thread labels are dedicated structural components independent of phase body verbosity** — Compression-safe marker expression enables verification without reading phase bodies | structure | aspirational | Each of the four marker types introduced by C-43–C-45 is expressed as a dedicated standalone labeled element, not embedded in or merged with phase body prose: (a) the framing paragraph (C-43) appears as a dedicated section before the manifest, not as an introductory paragraph merged with the manifest header; (b) per-container incoming-state annotations (C-43) appear as labeled elements on each container header line, not as inline sentences within the first phase body paragraph; (c) the Phase 9 prerequisite gate (C-44) appears as a REQUIRED-prefixed standalone gate line at the Phase 9 entry point, not as a sentence within the Phase 9 instructional block; (d) COMPLETE-line thread labels (C-45) appear as explicitly labeled elements on each CONTAINER COMPLETE line (e.g., "Thread 1: IDENTIFIED AND COMMITTED | Thread 2: handoff pending"), not as paraphrased status notes embedded in the COMPLETE line's prose. A document where any of these four marker types is expressed only as embedded prose — legible when the phase body is read but not verifiable by scanning structural markers alone — does not satisfy C-48. A document where all four marker types are standalone labeled elements satisfies C-48 regardless of whether surrounding phase bodies are verbose or compressed. C-48 requires C-43, C-44, and C-45 as prerequisites |
| C-49 | **Thread 1 and Thread 2 are declared as rows in a two-row table with identical column schema — construction-enforced co-equality makes subordination structurally impossible** — Table-schema enforcement advances C-47's assertion-enforced co-equality to construction-enforced co-equality | structure | aspirational | Thread 1 and Thread 2 appear in the manifest preamble as rows in a two-row table with an identical column schema. The schema must include at minimum: (a) a Scope column naming the thread's operational domain — for Thread 1, the four-state lifecycle and tracking mechanism; for Thread 2, the COMPARATOR/AUDITOR sequencing and phase scope; (b) a Key structural markers column naming the primary observable artifacts each thread produces — for Thread 1, the manifest Competitor Status column and CONTAINER COMPLETE lifecycle annotations; for Thread 2, the Phase 8 handoff declaration, Phase 9 prerequisite gate, and CLOSE COMPLETE sub-role discharge; (c) a Terminal discharge obligation column naming what each thread must produce at CLOSE COMPLETE — for Thread 1, the verbatim four-state chain; for Thread 2, the COMPARATOR/AUDITOR contract DISCHARGED confirmation. Both rows must carry equivalent depth in every column. A table where Thread 1 has multi-clause entries and Thread 2 has single-phrase entries in the same column does not satisfy C-49. A document that declares threads via parallel syntactic prose (satisfying C-47) without expressing them as a table does not satisfy C-49, because prose co-equality is evaluated by parsing register while table co-equality is verified by column structure alone. C-49 requires C-47 as a prerequisite |
| C-50 | **A dedicated Structural Marker Inventory section appears before any container executes, cataloging all four C-43/C-44/C-45 marker types in a four-column table with governing criterion, document location, and required form** — Pre-execution inventory establishes C-48 compliance as a verifiable document property before a reader encounters any container | structure | aspirational | The output contains a dedicated Structural Marker Inventory section placed before any container body begins executing. The section contains a four-column table listing all four C-43/C-44/C-45 marker types: Marker type | Required by | Location | Form. Each row names the marker type (e.g., "lifecycle framing paragraph"), its governing criterion (e.g., "C-43"), its precise document location (e.g., "dedicated section before manifest table, not merged with manifest header"), and its required structural form (e.g., "standalone labeled section"). The section closes with an explicit REQUIRED statement affirming that all four marker types are present as standalone labeled elements and that a marker embedded only in prose fails C-48. The inventory section fails C-50 if it omits any of the four marker types, if it names governing criteria without specifying document location and form, if its closure statement is absent or uses non-REQUIRED modal language, or if it appears inside a container body rather than before container execution begins. C-50 is orthogonal to C-48: C-48 requires markers to be standalone (form requirement); C-50 requires markers to be pre-announced in an inventory (pre-execution contract requirement). A document can have standalone markers without a pre-execution inventory (C-48 passes, C-50 fails). C-50 requires C-48 as a prerequisite |
| C-51 | **The BUILD container enumerates IMPLEMENTER and MEASURER as named sub-roles with disjoint phase scopes and a model-written handoff line at the Phase 7/8 boundary — BUILD intra-container role sequencing generates the Thread 2 structural markers required for C-49 5:5 depth parity** | structure | aspirational | The BUILD container header names IMPLEMENTER (Phase 7: prototype construction and delivery) and MEASURER (Phase 8: prototype measurement against B-00 and outperform threshold) as distinct sub-roles with explicit phase-scope assignments. Phase 7 COMPLETE carries a model-written handoff marker naming the transition ("IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER"). Phase 8 entry carries a REQUIRED prerequisite gate confirming the Phase 7 IMPLEMENTER handoff marker is present before MEASURER executes. Cross-prohibitions use hard modal operators: IMPLEMENTER FORBIDDEN to write measurement data, comparison results, or pass/fail verdicts; MEASURER FORBIDDEN to write new prototype construction decisions, implementation steps, or scope changes. Without this split, Thread 2's Key structural markers column is capped at three items (Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge), making C-49's five-item depth equivalence structurally unreachable regardless of how the thread table is formatted. A BUILD container satisfying C-41's COMPARATOR/AUDITOR split in CLOSE but using a monolithic BUILDER role in BUILD does not satisfy C-51. C-51 requires C-41 and C-49 as prerequisites |
| C-52 | **The C-50 Structural Marker Inventory REQUIRED closure statement carries an explicit violation-consequence clause naming the document property retroactively voided if any marker is expressed as embedded prose** — Consequence semantics bind the pre-execution compliance claim to its post-violation state | structure | aspirational | The Structural Marker Inventory section's REQUIRED closure statement includes both (a) a rule statement naming the criterion failure ("a marker embedded only in prose fails C-48" or equivalent) and (b) an explicit violation-consequence clause naming the document property retroactively voided if any marker is not expressed as a standalone labeled element — at minimum, the inventory itself (e.g., "voids this C-50 inventory") or the pre-execution compliance claim more broadly (e.g., "retroactively invalidates this pre-execution compliance claim"). Both elements must appear as explicit parts of the REQUIRED closure; a closure carrying only the rule without the consequence does not satisfy C-52, and a closure carrying only the consequence without the underlying rule does not satisfy C-52. The consequence clause is not satisfied by severity escalation without property naming ("severely violates C-48"), by criterion-outcome restatement ("does not meet C-48 requirements"), or by reference to a different document property than the pre-execution compliance claim. C-52 is orthogonal to C-50's structural inventory requirement: C-50 requires the pre-execution claim to be made; C-52 requires the claim to be bound to its post-violation consequence. A document satisfying C-50's inventory structure without the consequence clause in the closure statement does not satisfy C-52. C-52 requires C-50 as a prerequisite |

---

## Excellence Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-12 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-13 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-14 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-15 | *(carry forward)* | excellence | excellence | *(unchanged)* |

---

**Design notes for C-51 and C-52 in relation to their structural families:**

**Thread convergence family — named threads, co-equal elevation, construction enforcement,
depth enablement:**

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Thread existence | C-45 | Both threads named in preamble; labels propagate through COMPLETE boundaries; simultaneous terminal discharge |
| Thread co-equality | C-47 | Parallel syntactic form + mirrored scope depth + co-primary framing -> architectural inevitability |
| Table-enforced co-equality | C-49 | Identical column schema for both thread rows -> subordination structurally impossible by construction |
| Depth-parity enablement | C-51 | BUILD IMPLEMENTER/MEASURER sub-role split -> Thread 2 five structural markers -> C-49 5:5 equivalence satisfiable |

C-51 resolves the structural ceiling that C-49 exposes: C-49 requires both thread rows to
carry equivalent depth in every column, but without BUILD sub-role split the Thread 2
Key markers cell can truthfully list only three items. C-51 is not a formatting criterion
(like C-47 and C-49) but a structural generator — it produces the markers that make
C-49's format requirement fulfillable. The progression is: threads exist (C-45) ->
threads are declared co-equally (C-47) -> co-equality is construction-enforced (C-49)
-> depth parity is structurally enabled (C-51).

**Compression-safety family — marker existence, scanability, pre-execution contract,
consequence binding:**

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Marker presence | C-43, C-44, C-45 | Framing paragraph, per-container annotations, Phase 9 gate, thread labels must exist |
| Marker independence | C-48 | All four marker types are standalone labeled elements — verifiable by scanning, not embedded in prose |
| Marker pre-announcement | C-50 | All four marker types cataloged in a pre-execution inventory table with governing criterion, location, and form |
| Claim consequence binding | C-52 | REQUIRED closure names the document property voided by violation — pre-execution claim bound to its post-violation state |

C-52 closes the compliance circuit that C-50 opens: C-50 makes the pre-execution
compliance claim; C-52 makes the claim self-binding by stating what is voided if the
claim is false. The progression is: markers present (C-43/C-44/C-45) -> markers
scannable (C-48) -> compliance pre-declared (C-50) -> pre-declaration consequence-bound
(C-52).

**Competitor identification family — five surfaces, three granularities, narration,
justification (unchanged from v17):**

| Surface | Criterion | Container | What it records |
|---------|-----------|-----------|-----------------|
| CALIBRATE body | C-29 | CALIBRATE | Competitor name + status-quo rationale |
| CALIBRATE COMPLETE | C-32 | CALIBRATE | Triple: competitor name, B-00, threshold |
| Results table column | C-34 | CLOSE | Baseline column label = competitor name |
| Terminal arc record | C-36 | CLOSE (terminal) | Full arc including competitor name |
| Manifest lifecycle column | C-40 | Document-level | Four-state status across all boundaries (structural record) |
| Lifecycle narration layer | C-43 | Document-level + per-container | Framing paragraph + incoming-state annotations (structural narration) |
| Lifecycle justification layer | C-46 | Document-level | Contamination risk + isolation purpose per boundary (structural justification) |

**Role contamination defense family — four layers plus bidirectional verification plus
BUILD sub-role split (updated v19):**

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Existence | C-23 | At least one explicit prohibition per role label |
| Position | C-38 | Prohibition co-located at execution point (phase-level) |
| Register | C-39 | Hard modal operators (MUST/FORBIDDEN/REQUIRED/PROHIBITED) throughout |
| Sub-role sequencing (CLOSE) | C-41 | COMPARATOR/AUDITOR intra-container split with handoff declaration at verdict/counter-evidence boundary |
| Bidirectional verification | C-44 | AUDITOR acknowledgment gate at Phase 9 entry + sub-role contract discharge at CLOSE COMPLETE |
| Sub-role sequencing (BUILD) | C-51 | IMPLEMENTER/MEASURER intra-container split with handoff declaration at prototype-delivery/measurement boundary |

C-51 mirrors C-41's pattern at the BUILD container boundary: C-41 splits CLOSE into
COMPARATOR/AUDITOR at the verdict/counter-evidence boundary; C-51 splits BUILD into
IMPLEMENTER/MEASURER at the prototype-delivery/measurement boundary. The BUILD split
serves a dual purpose: it creates a contamination guard within BUILD (IMPLEMENTER cannot
pre-empt measurement; MEASURER cannot revise construction) and it generates the two
structural markers that enable C-49 Thread 2 depth parity.

**Value-flow accountability family — four surfaces, three granularities (unchanged from v15):**

```
[C-35: document level -- manifest names containers and purposes (entry)]
  [C-42: phase level -- ledger names producing/consuming phase per value (provenance)]
  [C-37: container level -- COMPLETE lines name downstream inputs (forward-reference)]
[C-36: document level -- terminal line encodes full arc (exit/audit)]
```

Version history for all structural families:

| Version | Added | What it closed |
|---------|-------|----------------|
| v(early) | C-20 | Gate completion proven by model-written artifact |
| v(early) | C-22 | Completion lines encode substantive results (backward-looking) |
| v(early) | C-23 | Role labels carry explicit prohibitions (existence floor) |
| v12 | C-36 | Terminal CLOSE COMPLETE encodes full arc (arc-spanning) |
| v13 | C-37 | Non-terminal COMPLETE lines name downstream inputs (forward-looking) |
| v14 | C-38 | Role prohibitions co-located at phase execution point (position) |
| v14 | C-39 | Prohibitions use hard modal operators throughout (register) |
| v15 | C-40 | Manifest competitor lifecycle column — four-state status across all containers (temporal record) |
| v15 | C-41 | CLOSE sub-role split COMPARATOR/AUDITOR with model-written handoff declaration |
| v15 | C-42 | Value Flow Ledger — phase-level provenance contract + ledger discharge at CLOSE COMPLETE |
| v16 | C-43 | Lifecycle narration layer — framing paragraph + per-container incoming-state annotations (narration) |
| v16 | C-44 | Bidirectional COMPARATOR/AUDITOR handoff — AUDITOR acknowledgment gate + CLOSE COMPLETE sub-role contract discharge |
| v16 | C-45 | Dual-thread convergence architecture — named threads propagated through COMPLETE boundaries + multi-criterion simultaneous terminal discharge |
| v17 | C-46 | Lifecycle justification layer — contamination risk + isolation purpose per container boundary (WHY-not-WHAT rationale triple) |
| v17 | C-47 | Co-equal thread elevation — parallel syntactic form + mirrored scope depth + co-primary framing -> architectural inevitability for C-45 terminal discharge |
| v17 | C-48 | Compression-safe marker expression — all C-43/C-44/C-45 markers as standalone labeled elements verifiable by scanning independent of phase body verbosity |
| v18 | C-49 | Table-enforced thread co-equality — identical column schema for both thread rows makes subordination structurally impossible by construction rather than by linguistic assertion |
| v18 | C-50 | Structural Marker Inventory section — pre-execution four-column catalog establishes C-48 compliance as a verifiable document property before any container executes |
| **v19** | **C-51** | **BUILD IMPLEMENTER/MEASURER sub-role split — generates Thread 2's Phase 7 handoff and Phase 8 gate markers, making C-49 5:5 depth parity a structurally satisfiable property rather than an impossible ceiling** |
| **v19** | **C-52** | **C-50 REQUIRED closure consequence clause — names the document property retroactively voided by marker embedding, binding the pre-execution compliance claim to its post-violation state** |

Ceiling moves from **357 -> 367**. The R19 seed scores 347/357 under v18 (C-51 and C-52
are the two remaining gaps). The R20 seed should combine: BUILD IMPLEMENTER/MEASURER
sub-role split with Phase 7 handoff and Phase 8 REQUIRED gate (C-51) and a
violation-consequence clause in the C-50 REQUIRED closure statement (C-52) on the R19
base, expected to reach **367**.
