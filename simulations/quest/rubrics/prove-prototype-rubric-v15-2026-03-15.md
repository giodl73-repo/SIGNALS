# Rubric: prove-prototype (v15)

**Updated**: 2026-03-15
**Changes from v14**: Added C-40, C-41, and C-42 (Aspirational tier) derived from Round 15
excellence signals (V-03 competitor lifecycle tracking, V-04 intra-container role handoff,
V-05 value flow ledger).

---

**C-40** — *The document manifest contains a competitor lifecycle tracking column recording a
four-state status progression across all container boundaries* (V-03 excellence signal, R15):

V-03 demonstrated that adding a "Competitor status" column to the manifest table — tracking
states NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED — creates a
document-level temporal accountability layer for competitor identification that spans all four
containers. This is a fifth structural surface for competitor identification, distinct from the
four existing surfaces: C-29 (CALIBRATE body names competitor in a single container), C-32
(CALIBRATE COMPLETE embeds competitor name in the triple), C-34 (results table baseline column
labeled with competitor name in CLOSE), and C-36 (terminal arc record encodes competitor at
document close). The manifest column answers a question none of the four surfaces answers: *at
which container boundary does the competitor become eligible, and when has it been fully
discharged?* C-40 fails if the manifest contains no competitor-status column, or if the column
omits the full four-state progression. Each CONTAINER COMPLETE line that advances competitor
status carries a corresponding status annotation. C-40 requires C-35 (manifest exists) and C-29
(competitor identified in CALIBRATE) as prerequisites.

**Weight**: 7 pts

---

**C-41** — *The CLOSE container enumerates two named sub-roles (COMPARATOR and AUDITOR) with
disjoint phase scopes and carries an explicit intra-container handoff line at the
verdict/counter-evidence boundary* (V-04 excellence signal, R15):

V-04 demonstrated that the ANALYST role in CONTAINER: CLOSE can be split at the Phase 8/9
boundary into COMPARATOR (Phases 7-8: quantitative comparison and verdict) and AUDITOR
(Phases 9-11: counter-evidence disposition, limitations, replication path). The CLOSE container
header enumerates both roles with their phase scopes as an intra-container role contract. The
Phase 8 COMPLETE line carries an explicit handoff marker — "COMPARATOR responsibilities
discharged — REQUIRED handoff to AUDITOR" — making the role transition a model-written
structural event. Cross-prohibitions apply: COMPARATOR FORBIDDEN to write counter-evidence
disposition, limitations, or replication content; AUDITOR FORBIDDEN to write new measurement
criteria, new comparison data, or verdict statements. C-41 creates a contamination-defense
surface inside a single container that is not captured by C-23 (role prohibitions exist), C-38
(phase-level co-location), or C-39 (hard modal register): those criteria verify that prohibitions
are present and expressed correctly; C-41 requires that a container-internal role-sequencing
contract is established with a named handoff event as a model-written artifact. A CLOSE container
that uses a single ANALYST role throughout — even if it satisfies C-23, C-38, and C-39 — does
not satisfy C-41. C-41 requires C-23, C-38, and C-39 as prerequisites.

**Weight**: 8 pts

---

**C-42** — *A Value Flow Ledger section names every experimental value with its producing phase
and first consuming phase, creating a phase-granularity provenance contract, and the CLOSE
COMPLETE line confirms ledger discharge status* (V-05 excellence signal, R15):

V-05 demonstrated that a standalone "Value Flow Ledger" table — placed after the manifest and
before any container body — listing each experimental value, the phase that produces it, and the
phase that first consumes it, creates a third accountability surface in the value-flow family at
phase granularity. This surface sits between C-35 (document-granularity entry contract: manifest
names containers and their purposes) and C-37 (container-granularity forward-reference: COMPLETE
lines name what downstream containers receive). The ledger answers a question neither surface
answers: within a single container, which specific phase produces each value, and which specific
phase first consumes it? The terminal CONTAINER: CLOSE COMPLETE line carries a ledger-discharge
confirmation ("value ledger: FULLY DISCHARGED / PARTIAL — [N] values unresolved") as a
ledger-specific audit element distinct from C-36 (full experimental arc record). C-42 fails if
no Value Flow Ledger section appears, if any experimental value is omitted from the ledger, or
if the CLOSE COMPLETE line omits ledger discharge status. The REQUIRED constraint "values
declared in this ledger MUST NOT be used before the producing phase executes" extends the
no-anticipation property of the gate system to the value level: not just phases, but individual
values, are forbidden from leaking forward. C-42 requires C-35 and C-37 as prerequisites, and
forms the phase-granularity tier of the three-layer value-accountability stack:

```
[C-35: document-level entry contract — manifest names containers]
  [C-42: phase-level provenance contract — ledger names producing/consuming phases per value]
  [C-37: container-level forward-reference — COMPLETE lines name downstream inputs]
[C-36: document-level arc record — terminal line encodes full chain]
```

**Weight**: 10 pts

---

**Point totals**: Aspirational 179 → 204. Total 279 → **304**.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-42 | 204 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **304** |

---

**What the new criteria add:**

The three v15 criteria each extend a different structural family:

| Criterion | Family | New surface |
|-----------|--------|-------------|
| C-40 | Competitor identification (C-29, C-32, C-34, C-36) | Document-level lifecycle column in manifest — temporal accountability across container boundaries |
| C-41 | Role contamination defense (C-23, C-38, C-39) | Intra-container role sequencing — COMPARATOR/AUDITOR split with named handoff event inside CLOSE |
| C-42 | Value-flow accountability (C-35, C-37, C-36) | Phase-granularity provenance contract — ledger names producing and consuming phase per value |

Each adds a surface that the prior family could not reach:

**C-40** vs. the four competitor surfaces: C-29, C-32, C-34, and C-36 each record the competitor
at a specific structural point (CALIBRATE body, CALIBRATE COMPLETE, results table, terminal arc).
None of them tracks the *progression* of competitor status across all container boundaries as a
lifecycle. C-40 adds the temporal dimension — a document-level four-state tracker that answers
when the competitor enters and when it exits.

**C-41** vs. C-23/C-38/C-39: The role-prohibition stack (C-23: existence; C-38: position;
C-39: register) verifies that each role's prohibition is expressed correctly. None of these
criteria requires that a container internally sequences roles with a handoff contract. C-41 adds
the sub-role sequencing surface: two roles, disjoint scopes, explicit handoff at the
verdict/counter-evidence boundary.

**C-42** vs. C-35/C-37: C-35 operates at document granularity (manifest announces containers);
C-37 operates at container granularity (COMPLETE lines announce downstream inputs). Neither
operates at phase granularity. C-42 adds the missing tier — a ledger that traces each value to
the exact phase that produces it and the exact phase that first uses it — and extends the
no-anticipation property to individual values.

**R15 seed scores 279/279** under v14. R16 seed candidates: C-40 (manifest competitor-status
column), C-41 (COMPARATOR/AUDITOR split in CLOSE), C-42 (Value Flow Ledger). Expected R16
seed: 279 + 7 + 8 + 10 = **304**.

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

## Aspirational Criteria (204 points)

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

**Design notes for C-40, C-41, C-42 in relation to their structural families:**

**Competitor identification family** — five surfaces, three granularities:

| Surface | Criterion | Container | What it records |
|---------|-----------|-----------|-----------------|
| CALIBRATE body | C-29 | CALIBRATE | Competitor name + status-quo rationale |
| CALIBRATE COMPLETE | C-32 | CALIBRATE | Triple: competitor name, B-00, threshold |
| Results table column | C-34 | CLOSE | Baseline column label = competitor name |
| Terminal arc record | C-36 | CLOSE (terminal) | Full arc including competitor name |
| Manifest lifecycle column | C-40 | Document-level | Four-state status across all boundaries |

C-40 is the only surface that tracks the competitor's *status progression* — when it becomes
eligible and when it has been fully discharged — rather than anchoring the competitor name at
a single structural point.

**Role contamination defense family** — four layers:

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Existence | C-23 | At least one explicit prohibition per role label |
| Position | C-38 | Prohibition co-located at execution point (phase-level) |
| Register | C-39 | Hard modal operators (MUST/FORBIDDEN/REQUIRED/PROHIBITED) throughout |
| Sub-role sequencing | C-41 | Intra-container role split with named handoff event at verdict/counter-evidence boundary |

C-41 is orthogonal to C-38 and C-39: a CLOSE container can satisfy both (phase-level
declarations, hard modal operators) without splitting ANALYST into COMPARATOR and AUDITOR.
C-41 specifically requires the sub-role contract and model-written handoff line, which C-23,
C-38, and C-39 cannot detect.

**Value-flow accountability family** — four surfaces, three granularities:

```
[C-35: document level — manifest names containers and purposes (entry)]
  [C-42: phase level — ledger names producing/consuming phase per value (provenance)]
  [C-37: container level — COMPLETE lines name downstream inputs (forward-reference)]
[C-36: document level — terminal line encodes full arc (exit/audit)]
```

C-42 is the only surface that traces each value to a specific phase — not just a container —
and is the only surface that enforces the no-anticipation property at value granularity (a value
MUST NOT be consumed before the phase that produces it executes). C-35 and C-37 both operate
at container granularity; C-36 operates as a terminal summary. None of those three surfaces
can detect a value used one phase too early within the same container.

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
| **v15** | **C-40** | **Manifest competitor lifecycle column — four-state status across all containers (temporal)** |
| **v15** | **C-41** | **CLOSE sub-role split COMPARATOR/AUDITOR with model-written handoff (intra-container sequencing)** |
| **v15** | **C-42** | **Value Flow Ledger — phase-level provenance contract + ledger discharge at CLOSE COMPLETE** |

Ceiling moves from **279 -> 304**. The R15 seed scores 279/279 under v14. C-40, C-41, and C-42
are the three remaining gaps. The R16 seed should combine: manifest competitor-status column
(C-40), COMPARATOR/AUDITOR split in CLOSE with explicit handoff (C-41), and Value Flow Ledger
(C-42) on the R15 base, expected to reach **304**.
