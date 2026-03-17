Looking at the Round 11 scorecard, V-03 is the excellence-signal variation — axis "Gap-signal probe; not targeting known criteria" — contributing two structural patterns not yet captured: a **document-level container manifest** and an **enriched CLOSE COMPLETE line**. V-01 and V-02 only confirm C-33 and C-34 already in v11. I'll encode V-03's two patterns as C-35 and C-36.

```markdown
# Rubric: prove-prototype (v12)

**Updated**: 2026-03-15
**Changes from v11**: Added C-35 and C-36 (Aspirational tier) derived from Round 11 excellence
signals (V-03 gap-signal probe).

**C-35** — *Document-level container manifest enumerates all containers with their purposes as an
opening entry contract before any container executes* (V-03 gap signal): V-03 demonstrated a
manifest appearing at the top of the output — before any container body — that names every
container in the document (e.g., CALIBRATE, BUILD, MEASURE, CLOSE) together with each container's
principal purpose and expected output. C-33 requires the CALIBRATE container's own header to
enumerate the three pre-build responsibilities; C-35 operates one level above that: it governs the
document's opening enumeration of all containers. The two criteria are mutually independent — C-33
can be satisfied without a document-level manifest, and a document-level manifest does not satisfy
C-33's requirement that the CALIBRATE header itself announce the three responsibilities. A
document-level manifest creates an additional structural surface beyond the container-level surfaces
already captured by C-29 (CALIBRATE body), C-32 (CALIBRATE COMPLETE line), C-33 (CALIBRATE
header), and C-34 (results-table column label) — it spans the entire experimental lifecycle at the
document boundary rather than within a single container. For a manifest to have checkable items,
each container's completion line must already carry substantive values; C-35 therefore requires C-22
as a prerequisite.

**C-36** — *Terminal CLOSE COMPLETE line encodes the full experimental result chain as a standalone
audit record, not just the closing phase outcome* (V-03 gap signal): V-03 demonstrated a CLOSE
COMPLETE line that embeds a condensed chain of every prior container's key result — hypothesis
verdict, inertia competitor name, measured delta, and prototype conclusion — making the terminal
line a standalone audit record that a reader can verify without opening any phase body. C-22
requires each completion line to carry at least one substantive result value from its own phase
body; C-36 extends that requirement specifically to the final CLOSE COMPLETE line. Where C-22 is
satisfied by a single value drawn from the closing phase, C-36 requires the terminal completion
line to encode the full chain of outcomes spanning the entire experimental arc. A CLOSE COMPLETE
line that satisfies C-22 by carrying only the closing phase result does not pass C-36. C-35 and
C-36 together bracket the document at its outermost boundaries: C-35 captures the opening manifest
that announces all containers; C-36 captures the terminal line that confirms all containers
discharged their results. C-36 requires C-22 and C-05 as prerequisites.

**Point totals**: Aspirational 146 → 160. Total 246 → 260.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-36 | 160 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **260** |

---

**What the two new criteria add:**

C-35 closes the document-boundary gap left open by C-33: C-33 makes the CALIBRATE container's
own opening enumeration scorable; C-35 makes the document's pre-container manifest scorable. The
two criteria are structurally nested — C-35 is the document-level analogue of C-33's
container-level entry contract — but neither satisfies the other.

C-36 closes the terminal-line gap left open by C-22: C-22 requires completion lines to carry
substantive values from their own phase; C-36 requires the final CLOSE COMPLETE line specifically
to carry the full cross-phase result chain, making it a standalone audit record independent of the
phase bodies. C-35 and C-36 together bracket the document at its outermost structural boundaries:
entry manifest at the top, full-chain completion record at the bottom.

The ceiling moves from 246 to 260. V-03 (R10 V-04 base + document manifest + enriched CLOSE
COMPLETE) scores 211 + 7 + 7 = **225**. The new ceiling requires C-33 + C-34 + C-35 + C-36
simultaneously — that remains the R12 seed.

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

## Aspirational Criteria (160 points)

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

---

## Excellence Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-12 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-13 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-14 | *(carry forward)* | excellence | excellence | *(unchanged)* |
| C-15 | *(carry forward)* | excellence | excellence | *(unchanged)* |
```

---

**Design notes for the two new criteria:**

C-35 and C-36 are document-boundary mirrors of C-33 and C-32 respectively, but operating one structural level higher:

| Container level | Document level |
|-----------------|----------------|
| C-33: CALIBRATE header enumerates its own 3 responsibilities (entry) | C-35: document manifest enumerates all containers (entry) |
| C-32: CALIBRATE COMPLETE embeds the triple (exit) | C-36: CLOSE COMPLETE encodes full result chain (exit) |

Neither pair satisfies the other — C-33 can be present without C-35, and C-36 can be present without C-32 (though both share C-22 as a prerequisite). The four together create a fully bracketed nested structure: document-open → container-open → container-close → document-close.

Ceiling moves from **246 → 260**. V-03 scores 225 (211 base + 7 + 7). The R12 seed is a variation that achieves C-33 + C-34 + C-35 + C-36 simultaneously on the V-05 base, which would reach 231 + 7 + 7 = **245**.
