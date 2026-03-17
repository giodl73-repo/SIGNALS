# flow-dataflow — Round 16 Scoring

## Evaluation Framework

- **Essential (C-01–C-04)**: 15 pts each × 4 = 60 pts
- **Recommended (C-05–C-07)**: 10 pts each × 3 = 30 pts
- **Aspirational (C-08–C-49)**: 42 criteria × ~0.238 pts = 10 pts; PARTIAL = ~0.119 pts

Baseline observation: all five variations carry the same structural scaffold (three-role pipeline, [A-01]–[A-14] registry, REGISTER DECLARATION with closed-chain paragraph, phase gates, tabular trace except V-03). Essential and Recommended criteria are met by construction across all designs. Differentiation lives entirely in the aspirational tier.

---

## V-01 — Natural Role Sequence, Tabular, Universal Closed-Chain

**Finance → Operations → Commerce; e-commerce order-to-cash**

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01–C-04 | PASS × 4 | Full three-role registry with stage trace, boundary checks, schema state, error annotations declared by design |
| Recommended | C-05–C-07 | PASS × 3 | [A-11] stale analysis; elapsed accumulation in [A-13]; domain entity (revenue recognition SLA, AR ledger) vocabulary |
| Asp. C-08 | Recovery prescriptions | PASS | [A-12] RECOVERY PRESCRIPTIONS in registry |
| Asp. C-09 | Trade-off analysis | PASS | [A-14] TRADE-OFF ANALYSIS in registry |
| Asp. C-10–C-12 | Domain context gate + boundary gates + entity exposure | PASS × 3 | [A-02] DOMAIN CONTEXT; interleaved boundary check blocks; domain entity names at each boundary |
| Asp. C-13–C-17 | Staleness contract, elapsed accumulation, incumbent baseline, cross-role citation chain, immutability | PASS × 5 | All structurally declared; [A-01] ≥3 steps; C-14 additive in [A-13]; C-15 connected through [A-14] trade-off |
| Asp. C-18–C-25 | Prompt-required sections, citation convention, stage-write gate, freshness verdict, registry table, phase gate checklists, upfront constraint, phase gate as registry row | PASS × 8 | STRUCTURAL CONSTRAINTS section; phase gates [A-05] and [A-08] in registry; Phase Gate 2 includes skip-level item |
| Asp. C-26 | Non-natural role ordering | **FAIL** | Natural Finance → Operations → Commerce; C-26 requires non-natural ordering as citation stress test |
| Asp. C-27–C-35 | Named recovery formula, boundary block schema, trade-off + baseline token citation, output register declaration, pre-declared boundary schema, register compliance marker mapping, register-invariant declaration | PASS × 8 | Schema section pre-declared; [A-09]/[A-10] register declaration; tabular compliance markers designated |
| Asp. C-36–C-38 | Baseline-first artifact ordering, REGISTER DECLARATION Parts A/B, skip-level citation | PASS × 3 | Commerce (pos 3) cites Finance [A-04] skip-level; Parts A/B single-location authority |
| Asp. C-39–C-43 | Skip-level SC governs role in body, names position distance, Phase Gate 2 item cites SC identifier, C-37+C-41 co-occurrence, all three skip-level attributes co-present | PASS × 5 | Skip-level SC explicitly designed with all three attributes co-present in single SC block |
| Asp. C-44–C-47 | Baseline-closure SC, format-mode declaration, SC-13 as navigation entry, SC-14 as navigation entry | C-44 PASS, C-45 PASS, C-46 PASS, C-47 **FAIL** | C-47 requires SC-14 FORMAT MODE DECLARATION, activated only for non-tabular; tabular format excludes it |
| Asp. C-48 | Governed artifact tokens named per SC entry | PASS | Every SC-1 through SC-13 entry in closed-chain paragraph names governed [A-xx] tokens by explicit example (SC-9 governs [A-04],[A-07],[A-10]; SC-13 governs [A-12],[A-14]) |
| Asp. C-49 | Enforcement mechanism named per SC entry | PASS | Example: SC-13 "enforced by inline callbacks at both section headers verifying [A-01] citation by token match without output-prose inspection" |

**Aspirational hits**: 40/42 (C-26 FAIL, C-47 FAIL)
**Aspirational score**: 40 × 0.238 = **9.524 pts**
**Total V-01**: 60 + 30 + 9.524 = **99.52**

---

## V-02 — Non-Natural Finance-Last, Tabular, Exhaustive Closed-Chain

**Commerce → Operations → Finance; healthcare claims adjudication**

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01–C-04 | PASS × 4 | Same structural scaffold; claims pipeline domain |
| Recommended | C-05–C-07 | PASS × 3 | Stale analysis; elapsed accumulation; domain entities (claim submission, EOB, EFT settlement) |
| Asp. C-26 | Non-natural role ordering | **PASS** | Commerce → Operations → Finance; Finance-last is a non-natural sequence, explicitly designed as citation stress test |
| Asp. C-39–C-43 | Skip-level attributes | PASS × 5 | SC-12 governs [A-04] (Commerce's boundary checks) via Finance's `Citing:` line; position distance = 2 (Finance pos 3, Commerce pos 1) declared in SC-12 body; Phase Gate 2 item cites [SC-12] by number |
| Asp. C-47 | SC-14 FORMAT MODE | **FAIL** | Tabular format; SC-14 not active |
| Asp. C-48–C-49 | Governed tokens + enforcement per SC | PASS × 2 | SC-12 closed-chain entry names [A-04] (governed token) and Phase Gate 2 enforcement by SC number (mechanism) — closes the skip-level chain from the register index |
| All other Asp. | C-08–C-25, C-27–C-46 | PASS × 37 | Structurally identical to V-01 except C-26 now PASS |

**Aspirational hits**: 41/42 (C-47 FAIL)
**Aspirational score**: 41 × 0.238 = **9.762 pts**
**Total V-02**: 60 + 30 + 9.762 = **99.76**

---

## V-03 — Prose Register, SC-14 Active, Exhaustive Closed-Chain

**Finance → Operations → Commerce; SaaS subscription recurring billing**

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01–C-04 | PASS × 4 | Same structural scaffold; prose format does not affect lineage chain correctness |
| Recommended | C-05–C-07 | PASS × 3 | Stale analysis; elapsed accumulation; subscription billing domain entities |
| Asp. C-26 | Non-natural ordering | **FAIL** | Natural Finance → Operations → Commerce sequence |
| Asp. C-28 | Named-column boundary block schema | PARTIAL | Non-tabular prose format; criterion substitution map covers C-28 via labeled paragraph format; but prose blocks are structurally different — label-sequence compliance substitutes for column-level verification (0.119 pts) |
| Asp. C-30 | Output register with format-specific compliance markers | PARTIAL | Substitution map replaces column-form markers with label-sequence markers; PARTIAL credit as format-mode substitution is present but the standard criterion form doesn't fully apply (0.119 pts) |
| Asp. C-32 | Register compliance marker mapping per structural field | PARTIAL | Substitution map addresses this explicitly; PARTIAL since non-tabular format cannot satisfy the full column-form requirement (0.119 pts) |
| Asp. C-34 | Per-boundary incumbent equivalent column | PARTIAL | Substitution map covers this for non-tabular; equivalent field named in prose label block (0.119 pts) |
| Asp. C-37 | Baseline-first artifact ordering | PARTIAL | Substitution map covers this; ordering equivalent exists in label sequence (0.119 pts) |
| Asp. C-47 | SC-14 FORMAT MODE DECLARATION | **PASS** | SC-14 explicitly active; governs [A-03],[A-04],[A-06],[A-07],[A-09],[A-10],[A-13]; enforcement via substitution map completeness check — absent label sequence fails by the substitution map's prescribed form |
| Asp. C-49 for SC-14 | Enforcement mechanism for SC-14 | PASS | "enforced by substitution map completeness check — absent label sequence in any boundary paragraph fails by the substitution map's prescribed form" — mechanism named without output-prose inspection |
| All other Asp. | C-08–C-25, C-27, C-29, C-31, C-33, C-35–C-36, C-38–C-46, C-48 | PASS × 33 | Structurally present; prose register does not compromise these criteria |

**Aspirational hits**: 33 PASS + 5 PARTIAL (× 0.119) + C-47 PASS + C-49-SC14 counted in C-49 PASS = 35 PASS + 5 PARTIAL + C-26 FAIL
Adjusted: 35 × 0.238 + 5 × 0.119 = 8.330 + 0.595 = **8.925 pts**
**Total V-03**: 60 + 30 + 8.925 = **98.93**

---

## V-04 — Maximum Inertia Framing, Tabular

**Finance → Operations → Commerce; manufacturing MRO procurement-to-pay**

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01–C-04 | PASS × 4 | Full scaffold; MRO procurement domain |
| Recommended | C-05–C-07 | PASS × 3 | Stale analysis; elapsed accumulation; procurement domain entities |
| Asp. C-15 | Incumbent baseline connected to C-08/C-09 | PASS+ | ≥5 manual steps (not ≥3) — richer baseline; [A-01] explicitly connected through [A-12] and [A-14] via named callbacks |
| Asp. C-26 | Non-natural ordering | **FAIL** | Natural Finance → Operations → Commerce |
| Asp. C-46 | SC-13 as named navigation entry | PASS+ | SC-13 entry names [A-01] as procurement baseline authority at both enforcement sites — strongest [A-01] anchoring of any variation |
| Asp. C-47 | SC-14 FORMAT MODE | **FAIL** | Tabular; SC-14 not active |
| Asp. C-48 | Governed tokens per SC entry | PASS+ | SC-8, SC-9, SC-11, SC-13 entries explicitly name [A-01] in both governed-token declaration and enforcement mechanism — maximum token visibility |
| Asp. C-49 | Enforcement mechanism per SC entry | PASS+ | SC-13: "enforced by inline callbacks at both [A-12] and [A-14] headers that verify [A-01] citation by token match without output-prose inspection — [A-01] is the procurement baseline authority; its absence is a protocol violation detectable from the header line alone" |
| All other Asp. | C-08–C-25, C-27–C-45 | PASS × 36 | Structurally identical to V-01 in these respects |

**Aspirational hits**: 40/42 (C-26 FAIL, C-47 FAIL) — same count as V-01
**Aspirational score**: 40 × 0.238 = **9.524 pts**
**Total V-04**: 60 + 30 + 9.524 = **99.52**

*Note*: V-04 ties V-01 numerically but the quality of C-48/C-49 evidence is distinctly stronger — [A-01] anchoring across SC-8, SC-9, SC-11, SC-13 creates a more navigable authority map. This is a within-criterion quality signal, not a separate criterion.

---

## V-05 — Combined Non-Natural + Lifecycle Depth, Tabular

**Operations → Commerce → Finance; digital advertising spend reporting**

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01–C-04 | PASS × 4 | Full scaffold; digital advertising domain |
| Recommended | C-05–C-07 | PASS × 3 | Stale analysis; elapsed accumulation; advertising spend domain entities |
| Asp. C-23 | Phase gate self-verification checklists | PASS+ | Three phase gates ([A-00], [A-05], [A-08]); Phase Gate 0 checklist explicitly includes: "REGISTER DECLARATION closed-chain paragraph lists all SC-1 through SC-13 with governed tokens and enforcement mechanisms (C-48, C-49)" — most comprehensive phase gate coverage |
| Asp. C-25 | Phase gate artifacts as first-class registry rows | PASS+ | [A-00] added to registry; SC-6 governs all three phase gate tokens |
| Asp. C-26 | Non-natural role ordering | **PASS** | Operations → Commerce → Finance; Finance-last; skip-level: Finance (pos 3) cites Operations [A-04] (pos 1); position distance = 2 |
| Asp. C-39–C-43 | Skip-level attributes | PASS × 5 | SC-12 governs [A-04] (Operations' boundary checks); position distance 2 declared; Phase Gate 2 item cites [SC-12] |
| Asp. C-47 | SC-14 FORMAT MODE | **FAIL** | Tabular; SC-14 not active |
| Asp. C-48 | Governed tokens per SC entry | PASS++ | SC-6 closed-chain entry names **three** governed tokens ([A-00], [A-05], [A-08]) — maximum governed-token span of any SC in any variation; exhaustive coverage from pre-role setup through post-trace gates |
| Asp. C-49 | Enforcement mechanism per SC entry | PASS++ | SC-6 entry names gating callback enforcement for all three phase gates; Phase Gate 0 itself acts as enforcement mechanism for the entire closed-chain paragraph |
| All other Asp. | C-08–C-25, C-27–C-46 | PASS × 36 | Structurally equivalent to V-02 |

**Aspirational hits**: 41/42 (C-47 FAIL)
**Aspirational score**: 41 × 0.238 = **9.762 pts**
**Total V-05**: 60 + 30 + 9.762 = **99.76**

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 (tie) | **V-02** | 60/60 | 30/30 | 9.762 | **99.76** |
| 1 (tie) | **V-05** | 60/60 | 30/30 | 9.762 | **99.76** |
| 3 (tie) | V-01 | 60/60 | 30/30 | 9.524 | **99.52** |
| 3 (tie) | V-04 | 60/60 | 30/30 | 9.524 | **99.52** |
| 5 | V-03 | 60/60 | 30/30 | 8.925 | **98.93** |

**All essential pass**: Yes — C-01–C-04 PASS in all five variations.

**Differentiating axis**: C-26 (non-natural role ordering) is the sole binary discriminator between tier-1 and tier-3 variations. C-47 is the sole criterion that rewards non-tabular register but comes at the cost of five PARTIAL scores (C-28, C-30, C-32, C-34, C-37), resulting in net lower aspirational score for V-03.

---

## Excellence Signals — V-02 and V-05

**V-05 distinguishing signal (within-criterion quality, C-48/C-49)**:

SC-6 is the only SC in any variation whose closed-chain entry governs **three artifact tokens** ([A-00], [A-05], [A-08]). This arises directly from Phase Gate 0 adding [A-00] to the registry. The entry becomes a lifecycle-complete authority map for all phase gates: pre-role setup, post-Finance, post-Operations — navigable from the register index without reading any role instruction. No other SC in any variation governs more than two artifacts of the same type.

**V-05 novel structural pattern — Phase Gate 0 as closed-chain integrity checkpoint**:

Phase Gate 0's checklist explicitly contains an item that verifies C-48/C-49 compliance before any role writes output: `"REGISTER DECLARATION closed-chain paragraph lists all SC-1 through SC-13 with governed tokens and enforcement mechanisms (C-48, C-49)"`. This creates a **fail-fast** mechanism: a role cannot pass Phase Gate 0 without the closed-chain paragraph being complete and verifiable by token match. In all other variations, C-48/C-49 compliance can only be verified post-hoc by reading the final REGISTER DECLARATION. Phase Gate 0 moves this verification to before-first-role — the earliest detectable failure point in the lifecycle.

**V-02 distinguishing signal (within-criterion quality, C-39–C-43)**:

Healthcare claims adjudication creates a longer position-distance scenario (Commerce pos 1, Finance pos 3) where SC-12's governing of [A-04] crosses two role boundaries. The SC-12 closed-chain entry names [A-04] as governed token and cites Phase Gate 2 verification by SC number — the enforcement chain is: `register entry → SC-12 → Phase Gate 2 item → [A-04] in Finance's Citing: line`. This is the most navigation-dense skip-level chain in any variation.

**New patterns for R17 consideration**:

**C-50 candidate** — *Phase Gate 0 as pre-role closed-chain integrity checkpoint*: When Phase Gate 0 is present in the artifact registry, its verification checklist must include an explicit item confirming that the REGISTER DECLARATION closed-chain paragraph lists all SCs with governed [A-xx] tokens and enforcement mechanisms. This item must be checkable by token match without reading SC bodies or role instructions. A Phase Gate 0 that verifies artifact registry completeness but not closed-chain completeness does not satisfy this criterion.

**C-51 candidate** — *Phase gate count invariant in SC-6 governed-token declaration*: SC-6's closed-chain entry must name exactly as many phase gate tokens as exist in the artifact registry. When [A-00] (Phase Gate 0) is present, SC-6's entry must govern [A-00], [A-05], and [A-08] — not just the standard two. The count of governed tokens in SC-6's entry must equal the count of phase gate rows in the ARTIFACT REGISTRY. A mismatch is detectable from the register index alone without reading SC-6's body.

---

```json
{"top_score": 99.76, "all_essential_pass": true, "new_patterns": ["Phase Gate 0 as pre-role closed-chain integrity checkpoint — checklist item verifies C-48/C-49 by token match before any role writes output, creating a fail-fast mechanism for closed-chain completeness", "Phase gate count invariant in SC-6 governed-token declaration — SC-6 entry must name exactly as many phase gate tokens as exist in the artifact registry; count mismatch is detectable from register index alone"]}
```
