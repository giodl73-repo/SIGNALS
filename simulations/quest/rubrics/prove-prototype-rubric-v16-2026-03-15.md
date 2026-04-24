# Rubric: prove-prototype (v16)

**Updated**: 2026-03-15
**Changes from v15**: Added C-43, C-44, and C-45 (Aspirational tier) derived from Round 16
excellence signals (V-03 competitor lifecycle narration, V-04 bidirectional COMPARATOR/AUDITOR
handoff, V-05 dual-thread convergence architecture with multi-criterion terminal discharge).

---

**C-43** — *The competitor lifecycle is preceded by an explicit framing paragraph and each
container header carries an incoming-state annotation that contextualizes lifecycle constraints
within that container* (V-03 excellence signal, R16):

V-03 demonstrated that the competitor lifecycle tracking introduced by C-40 can be enriched with
two additional structural layers: a pre-manifest framing paragraph and per-container incoming-state
annotations. The framing paragraph appears before the manifest table and explains the four-state
progression — NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED — with
rationale for why each state transition is gated at a specific container boundary. Each container
header then annotates the lifecycle state the competitor holds when that container begins executing
(e.g., "Competitor lifecycle — incoming state: NOT YET IDENTIFIED. Identification is FORBIDDEN
before CALIBRATE."). Prohibitions within containers that enforce lifecycle ordering carry the
current lifecycle state as explicit context, making the constraint legible without cross-reference
to the framing paragraph. CALIBRATE Phase 4 narrates both sub-transitions — NOT YET IDENTIFIED
→ IDENTIFIED, then IDENTIFIED → IDENTIFIED AND COMMITTED — with rationale for the two-step
commitment sequence.

C-43 is the narration layer of the competitor lifecycle family: C-40 tracks the four states in
the manifest column (structural record); C-43 explains them before the manifest and annotates
each container with incoming-state context (structural narration). A document that has C-40's
manifest column but no framing paragraph and no incoming-state container annotations does not
satisfy C-43. A document that has a framing paragraph but no incoming-state annotations on
container headers does not satisfy C-43 — both elements are required. C-43 requires C-40 as a
prerequisite.

**Weight**: 6 pts

---

**C-44** — *The COMPARATOR/AUDITOR handoff is bidirectional: Phase 8 COMPLETE declares the
handoff and Phase 9 entry carries a REQUIRED prerequisite gate confirming the Phase 8 handoff
marker is present before execution proceeds* (V-04 and V-05 excellence signal, R16):

V-04 and V-05 demonstrated that the handoff event introduced by C-41 can be elevated from a
unidirectional declaration to a verifiable two-event sequence. C-41 requires the Phase 8 COMPLETE
line to carry "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR." C-44
requires the corresponding acknowledgment: the Phase 9 entry header carries an explicit
prerequisite gate — "REQUIRED: Confirm Phase 8 COMPARATOR handoff marker present before
executing" — that forces the AUDITOR role to verify the handoff occurred before producing any
output. This bidirectional structure creates a verifiable sequence: COMPARATOR declares at Phase
8 exit; AUDITOR confirms receipt at Phase 9 entry. Neither event alone constitutes a
bidirectional handoff.

In addition, the CLOSE COMPLETE line carries a sub-role contract discharge confirmation —
"COMPARATOR/AUDITOR sub-role contract: DISCHARGED" — as an element distinct from C-36's arc
record and C-42's ledger discharge. This confirmation signals that the two-event handoff sequence
was executed and closed, not merely declared.

C-44 is orthogonal to C-41 in the same way C-22 is orthogonal to C-20: C-41 requires the
handoff declaration to exist; C-44 requires the acknowledgment and terminal confirmation to also
exist. A CLOSE container that carries the Phase 8 handoff declaration (satisfying C-41) without
the Phase 9 entry prerequisite gate or the CLOSE COMPLETE sub-role contract discharge does not
satisfy C-44. C-44 requires C-41 as a prerequisite.

**Weight**: 7 pts

---

**C-45** — *The manifest preamble names the competitor lifecycle and the COMPARATOR/AUDITOR
sequencing as propagating named threads; thread labels appear on every CONTAINER COMPLETE
boundary; and the CLOSE COMPLETE line carries a multi-criterion terminal confirmation that
simultaneously discharges all three new criteria (C-40, C-41, C-42)* (V-05 excellence signal, R16):

V-05 demonstrated that C-40, C-41, and C-42 can be unified into a named-thread convergence
architecture. The manifest preamble — the section preceding the manifest table — names two
propagating threads: Thread 1 (competitor lifecycle: four-state progression, governed by C-40)
and Thread 2 (COMPARATOR/AUDITOR sequencing: intra-CLOSE role contract, governed by C-41). The
thread names appear in the preamble with explicit labels before the manifest executes.

Once named, thread labels propagate. Every non-terminal CONTAINER COMPLETE line carries the
current thread status — Thread 1 lifecycle state at that boundary, Thread 2 handoff status if
applicable — as named labeled elements. The thread labels do not replace the C-40 competitor
status annotations or the C-41 handoff marker; they propagate alongside and reference them.

The CLOSE COMPLETE line carries a multi-criterion terminal confirmation that explicitly discharges
all three new criteria simultaneously as REQUIRED elements: (a) Thread 1 lifecycle chain encoded
verbatim with the full four-state sequence (NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED →
REFERENCED → DISCHARGED) confirming C-40 closure; (b) Thread 2 COMPARATOR/AUDITOR handoff
confirmed executed, confirming C-41 closure; (c) ledger discharge status confirming C-42 closure.
A CLOSE COMPLETE line that carries any subset of these three confirmations — or that carries all
three but without explicit REQUIRED gating — does not satisfy C-45.

C-45 is the convergence criterion of the v15 family: where C-40, C-41, and C-42 each introduce
an independent structural surface, C-45 requires that those surfaces be named, labeled, and
tracked as a unified convergence architecture whose final state is verifiable at the terminal
COMPLETE line by inspection. A document that satisfies C-40, C-41, and C-42 independently but
does not name them as threads, propagate thread labels, or guarantee simultaneous terminal
discharge does not satisfy C-45. C-45 requires C-40, C-41, and C-42 as prerequisites.

**Weight**: 12 pts

---

**Point totals**: Aspirational 204 → 229. Total 304 → **329**.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-45 | 229 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **329** |

---

**What the new criteria add:**

The three v16 criteria each deepen a different v15 criterion rather than opening a new family:

| Criterion | Deepens | New surface |
|-----------|---------|-------------|
| C-43 | C-40 | Lifecycle narration — framing paragraph + per-container incoming-state annotation |
| C-44 | C-41 | Bidirectional handoff — AUDITOR acknowledgment gate + CLOSE COMPLETE sub-role contract discharge |
| C-45 | C-40 + C-41 + C-42 | Thread convergence — named propagating threads + multi-criterion simultaneous terminal discharge |

Each adds a layer that C-40/C-41/C-42 cannot reach:

**C-43** vs. C-40: C-40 tracks the four lifecycle states in the manifest column — a structural
record. C-43 adds the *explanation* layer: why the transitions are gated where they are (framing
paragraph), and what state each container begins with (incoming-state annotation). A document
with C-40 but no framing paragraph has the record without the narration.

**C-44** vs. C-41: C-41 requires the handoff to be *declared* at Phase 8 exit. C-44 requires the
handoff to be *acknowledged* at Phase 9 entry and *confirmed closed* at CLOSE COMPLETE. The
distinction is between a structural declaration (unilateral) and a verifiable two-event sequence
(bidirectional). A document where the AUDITOR begins Phase 9 without confirming the Phase 8
marker is present has a handoff declaration but no handoff verification.

**C-45** vs. C-40 + C-41 + C-42 independently: A document can satisfy all three v15 criteria
without naming them as threads, without propagating thread labels through COMPLETE boundaries,
and without requiring simultaneous terminal discharge. C-45 requires that the three criteria be
treated as a unified tracking framework — named, labeled, propagated, and guaranteed to converge
at the same terminal line. This creates a structural guarantee that no new criterion can be
silently satisfied in isolation and then omitted from the document's closing audit.

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

## Aspirational Criteria (229 points)

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

**Design notes for C-43, C-44, C-45 in relation to their structural families:**

**Competitor identification family — five surfaces, three granularities, plus narration:**

| Surface | Criterion | Container | What it records |
|---------|-----------|-----------|-----------------|
| CALIBRATE body | C-29 | CALIBRATE | Competitor name + status-quo rationale |
| CALIBRATE COMPLETE | C-32 | CALIBRATE | Triple: competitor name, B-00, threshold |
| Results table column | C-34 | CLOSE | Baseline column label = competitor name |
| Terminal arc record | C-36 | CLOSE (terminal) | Full arc including competitor name |
| Manifest lifecycle column | C-40 | Document-level | Four-state status across all boundaries (structural record) |
| Lifecycle narration layer | C-43 | Document-level + per-container | Framing paragraph + incoming-state annotations (structural narration) |

C-43 is the explanation surface: where C-40 records what the lifecycle state is at each boundary,
C-43 explains why those boundaries are where they are and annotates each container with the state
it inherits. The record (C-40) and the narration (C-43) are orthogonal — a document can have the
column without the paragraph, or the paragraph without the column (though C-43 requires C-40).

**Role contamination defense family — four layers plus bidirectional verification:**

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Existence | C-23 | At least one explicit prohibition per role label |
| Position | C-38 | Prohibition co-located at execution point (phase-level) |
| Register | C-39 | Hard modal operators (MUST/FORBIDDEN/REQUIRED/PROHIBITED) throughout |
| Sub-role sequencing | C-41 | Intra-container role split with named handoff declaration at verdict/counter-evidence boundary |
| Bidirectional verification | C-44 | AUDITOR acknowledgment gate at Phase 9 entry + sub-role contract discharge at CLOSE COMPLETE |

C-44 extends C-41 in the same way C-22 extends C-20: C-41 requires the declaration; C-44 requires
the acknowledgment and the terminal confirmation. Together they close the loop: COMPARATOR
declares exit, AUDITOR declares entry, CLOSE COMPLETE declares contract closed.

**Value-flow accountability family — four surfaces, three granularities (unchanged from v15):**

```
[C-35: document level — manifest names containers and purposes (entry)]
  [C-42: phase level — ledger names producing/consuming phase per value (provenance)]
  [C-37: container level — COMPLETE lines name downstream inputs (forward-reference)]
[C-36: document level — terminal line encodes full arc (exit/audit)]
```

C-45 does not add a new value-flow surface but requires C-42's ledger discharge to appear as a
named thread confirmation in the CLOSE COMPLETE line, making it part of the convergence
guarantee rather than a standalone audit element.

**Thread convergence (C-45) in relation to the three v15 families:**

C-45 is a meta-criterion: it does not introduce a new structural surface in any of the three
families but requires that all three criteria share a unified naming framework and converge at the
same terminal point. The thread architecture is the structural guarantee that a model executing
the document cannot satisfy C-40, C-41, and C-42 silently (each in isolation) while failing to
prove their collective closure at the document's final line.

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
| **v16** | **C-43** | **Lifecycle narration layer — framing paragraph + per-container incoming-state annotations (narration)** |
| **v16** | **C-44** | **Bidirectional COMPARATOR/AUDITOR handoff — AUDITOR acknowledgment gate + CLOSE COMPLETE sub-role contract discharge** |
| **v16** | **C-45** | **Dual-thread convergence architecture — named threads propagated through COMPLETE boundaries + multi-criterion simultaneous terminal discharge** |

Ceiling moves from **304 -> 329**. The R16 seed scores 304/304 under v15. C-43, C-44, and C-45
are the three remaining gaps. The R17 seed should combine: lifecycle narration paragraph with
per-container incoming-state annotations (C-43), bidirectional AUDITOR acknowledgment gate and
CLOSE COMPLETE sub-role contract discharge (C-44), and dual-thread manifest preamble with
thread propagation and multi-criterion CLOSE COMPLETE (C-45) on the R16 base, expected to
reach **329**.
