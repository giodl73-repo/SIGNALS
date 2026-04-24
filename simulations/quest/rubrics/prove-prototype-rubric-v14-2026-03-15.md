# Rubric: prove-prototype (v14)

**Updated**: 2026-03-15
**Changes from v13**: Added C-38 and C-39 (Aspirational tier) derived from Round 14 excellence
signals (V-04 phase-level role co-location and V-01 imperative prohibition register).

---

**C-38** — *Role prohibitions appear as inline execution markers co-located at the specific phase
where each role's constraint applies, rather than only in a container-level table at container
entry* (V-04 excellence signal, R14):

V-04 demonstrated that container-level role tables can be replaced entirely by per-phase inline
role declarations of the form `Phase N — ROLE (writes: X; must NOT write: Y)`. The scorecard
confirmed this satisfies C-23 — each role label still carries an explicit prohibition — but
observed that "each role prohibition is co-located at the exact execution point where
contamination could occur. This is finer granularity than container-level tables." C-23 requires
role prohibitions to exist; C-38 requires them to be positioned at the phase-level execution
point, making the prohibition maximally proximate to the moment of potential contamination. A
document that satisfies C-23 via a container-level table alone does not satisfy C-38, because
the prohibition appears at container entry rather than at the phase where each role writes. A
document satisfying C-38 automatically satisfies C-23 (the prerequisite), but not vice versa.
C-38 applies to every named role in the document; it is satisfied for a given role only if that
role's prohibition appears inline at the phase header where the role operates.

**Weight**: 7 pts

---

**C-39** — *Role prohibitions and phase gate markers throughout the document use hard enforcement
modal operators (MUST, FORBIDDEN, REQUIRED, PROHIBITED) rather than descriptive or mixed
register* (V-01 excellence signal, R14):

V-01 systematically converted all descriptive or mixed-register instructions — "Execute before
Phase 2," "Name the counter-interpretation" — to hard enforcement language, renaming role table
columns "MUST Write" / "FORBIDDEN to Write" and marking every container header with REQUIRED,
PROHIBITED, and FORBIDDEN labels. The scorecard observed this is the "strongest prohibition
expression of any variation." C-23 requires at least one explicit prohibition per role label;
C-23 is satisfied by "Must NOT Write" or "should not write" with equal status. C-39 is not
satisfied by mixed register: every prohibition — both role-level and phase-gate — must use one
of the four hard modal operators (MUST, FORBIDDEN, REQUIRED, PROHIBITED). A document where some
prohibitions use soft language while others use hard language does not pass C-39. C-39 is
compatible with both container-level tables (C-23 via table) and phase-level declarations (C-38),
and imposes a register requirement on whichever surface the prohibitions occupy. C-39 requires
C-23 as a prerequisite.

**Weight**: 5 pts

---

**Point totals**: Aspirational 167 → 179. Total 267 → **279**.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-39 | 179 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **279** |

---

**What the new criteria add:**

C-23 establishes that each named role must carry at least one explicit prohibition — it is the
floor criterion for role-level contamination defense. C-38 and C-39 add two independent
dimensions above that floor:

| Criterion | Dimension | What it upgrades |
|-----------|-----------|-----------------|
| C-23 | Existence — prohibitions must be present | None (floor) |
| C-38 | Position — prohibitions must be co-located at execution point | C-23's container-level scope |
| C-39 | Register — prohibitions must use hard modal operators | C-23's language permissiveness |

C-38 and C-39 are orthogonal: a document can achieve C-38 (phase-level placement) with soft
language and fail C-39; it can achieve C-39 (imperative register) in a container-level table and
fail C-38. Both are required for the strongest contamination-defense posture demonstrated in R14.

The R14 seed scores 267/279 under v14 — C-38 and C-39 are the two remaining gaps. The R15 seed
adds V-04's phase-level inline declarations and V-01's imperative register to the R14 base,
expected to score 267 + 7 + 5 = **279**.

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

## Aspirational Criteria (179 points)

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
| C-37 | **Non-terminal container COMPLETE lines carry a forward-reference clause that names the downstream container's input dependencies, creating a verifiable handoff contract** | structure | aspirational | Each non-terminal container COMPLETE line (DESIGN COMPLETE, CALIBRATE COMPLETE, BUILD COMPLETE) appends a forward-reference clause — e.g., `→ [NEXT] receives:` — that names the specific values the downstream container will consume. The clause must name concrete values (hypothesis text, threshold, metric name, competitor name, baseline value) matching what the downstream container's opening phases require; it is not satisfied by a generic forward pointer or a reference to the completion line's own results alone. The terminal CLOSE COMPLETE line has no downstream container and is exempt. A completion line that satisfies C-22 by encoding its own phase results without a forward-reference clause does not satisfy C-37. C-36 governs the terminal line's cross-container arc record; C-37 governs each intermediate line's forward commitment to the next container. Together with C-22 and C-36, C-37 forms a three-surface completion-line contract: backward-looking at every line (C-22), forward-looking at every non-terminal line (C-37), and arc-spanning at the final line (C-36). C-37 requires C-22 as a prerequisite |
| C-38 | **Role prohibitions appear as inline execution markers co-located at the specific phase where each role's constraint applies** — Phase-level role declarations position each prohibition at the exact execution point where contamination could occur, rather than only in a container-level table at container entry | structure | aspirational | Every named role in the document carries its prohibition as an inline execution marker at the phase header where that role operates — e.g., `Phase N — ROLE (writes: X; must NOT write: Y)` — rather than exclusively in a container-level table. A document that satisfies C-23 via container-level tables alone does not satisfy C-38, because the prohibition appears at container entry rather than at the phase of execution. A document satisfying C-38 automatically satisfies C-23 (prerequisite), but not vice versa. C-38 is satisfied for a given role only if that role's prohibition appears inline at the phase where the role writes; roles without a corresponding phase-level declaration fail C-38 regardless of what appears in container tables. C-38 requires C-23 as a prerequisite |
| C-39 | **Role prohibitions and phase gate markers use hard enforcement modal operators throughout** — Every prohibition and gate constraint in the document uses one of four hard modal operators (MUST, FORBIDDEN, REQUIRED, PROHIBITED) rather than descriptive or mixed register | structure | aspirational | Every role-level prohibition and every phase gate marker in the document uses MUST, FORBIDDEN, REQUIRED, or PROHIBITED. A document where any prohibition uses soft or mixed language — "should not," "may not," "avoid," "do not" — does not pass, even if most prohibitions use hard operators. Role table column headers, container header constraint blocks, and inline phase gate markers are all in scope. C-39 does not require a specific placement format (container-level table or phase-level inline both qualify) and is therefore orthogonal to C-38: a document can satisfy C-38 with soft language (fail C-39) or satisfy C-39 via container-level tables (fail C-38). C-39 requires C-23 as a prerequisite |

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

**Design notes for C-38 and C-39 in relation to the role-prohibition family:**

C-23, C-38, and C-39 form a three-layer contamination-defense stack above the phase-gate
ordering layer (C-19/C-20):

| Layer | Criterion | What it enforces |
|-------|-----------|-----------------|
| Existence | C-23 | At least one explicit prohibition per role label |
| Position | C-38 | Prohibition co-located at execution point (phase-level), not only at container entry |
| Register | C-39 | Hard modal operators (MUST/FORBIDDEN/REQUIRED/PROHIBITED) throughout |

Each layer is independently testable and independently satisfiable or violatable:

- C-23 ∧ ¬C-38 ∧ ¬C-39: Prohibitions exist in container-level tables with soft language
- C-23 ∧ C-38 ∧ ¬C-39: Phase-level declarations with mixed-register language
- C-23 ∧ ¬C-38 ∧ C-39: Container-level tables with hard modal operators
- C-23 ∧ C-38 ∧ C-39: Phase-level declarations with hard modal operators (V-01+V-04 combined — maximum contamination-defense expression)

The R14 variations tested each combination independently before combining:
- V-04 tested C-38 isolation (phase-level declarations, mixed register) → C-38 PASS, C-39 scored by register present
- V-01 tested C-39 isolation (container-level tables, full imperative register) → C-39 PASS, C-38 scored by table format

The R15 seed should combine both: phase-level declarations with hard modal operators throughout,
targeting the maximum expression.

The full role-prohibition layer now spans:

```
[C-23: prohibition existence — floor criterion for all role surfaces]
  [C-38: prohibition position — co-located at phase execution point]
  [C-39: prohibition register — hard modal operators throughout]
```

C-38 and C-39 are both prerequisites-upward from C-23 and are independent of each other.
Neither implies the other.

Version history for the role-prohibition and completion-line families:

| Version | Added | What it closed |
|---------|-------|----------------|
| v(early) | C-20 | Gate completion proven by model-written artifact |
| v(early) | C-22 | Completion lines encode substantive results (backward-looking) |
| v(early) | C-23 | Role labels carry explicit prohibitions (existence floor) |
| v12 | C-36 | Terminal CLOSE COMPLETE encodes full arc (arc-spanning) |
| v13 | C-37 | Non-terminal COMPLETE lines name downstream inputs (forward-looking) |
| **v14** | **C-38** | **Role prohibitions co-located at phase execution point (position)** |
| **v14** | **C-39** | **Prohibitions use hard modal operators throughout (register)** |

Ceiling moves from **267 → 279**. The R14 seed scores 267/279 under v14 — C-38 and C-39 are
the two remaining gaps. The R15 seed combines V-04's phase-level declarations with V-01's
imperative register on the R14 base, expected to reach **279**.
