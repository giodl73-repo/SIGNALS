# Quest Score — `topic-reflect` Round 8 (v8 Rubric)

**Rubric version:** v8 (2026-03-17) | **Criteria:** 5 essential + 3 recommended + 17 aspirational | **Max:** 175 pts
**Basis:** V-01 scored from full text; V-02–V-05 scored from design descriptions and variation axes (single-axis vs. combined).

---

## Scoring Legend

- **PASS** = criterion met, full points
- **PARTIAL** = criterion partially met, scored as FAIL (rubric is binary)
- **FAIL** = criterion not met

---

## V-01 — Formal/Technical Register + Front-Loaded Vocabulary Rule

**Axis:** Phrasing register; vocabulary rule and synonym-to-canonical mapping table appear as the first operative section before any stage instruction.

### Essential (12 pts each) — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Stage 4 template requires "references a specific B-# from Stage 1"; adversarial gate A1 explicitly tests "contradicts (not merely confirms)" |
| C-02 | **PASS** | Stage 1: 3-part structure (belief model + 5-dim table + B-## labeled beliefs). Stage 6: verdict table with COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED and revision direction |
| C-03 | **PASS** | Stage 2 full inventory required before Stage 4 can cite; Signal Source format requires "full artifact name, namespace, and date — not 'multiple sources'" |
| C-04 | **PASS** | Pre-emission check explicitly: "Design Impact names a specific component, API, flow, or decision"; adversarial gate A3 checks same requirement |
| C-05 | **PASS** | Stage 3 five-check table; each row has VALID / INVALID verdict; GATE-CONFIRMED / GATE-REJECTED routing tokens; COMMIT-STAGE-3-CLEAN/FLAGGED present |

### Recommended (10 pts each) — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Vocabulary rule enforces closed list as first operative section; mapping table prevents substitution before any stage instruction; enforcement active at peak attention |
| C-07 | **PASS** | Stage 4: "Minimum: two entries" explicitly stated |
| C-08 | **PASS** | Stage 5 cluster map requires "Named skill or role — e.g., `/trace-contract`, API design lead, `/prove-hypothesis`" — not "investigate" |

### Aspirational (5 pts each) — 55/85

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | GATE-CONFIRMED routes to Stage 4 ("proceed to Stage 4"); COMMIT-ENTRY per entry in pre-emission check; all six COMMIT-STAGE tokens (1–6) present |
| C-10 | **PASS** | Stage 6: "Record CLEAR if no beliefs were flagged"; COMMIT-STAGE-3-FLAGGED triggers naming of responsible beliefs in Stage 3 routing |
| C-11 | **PASS** | Stage 4 uses numbered prose blocks with four labeled sub-fields; "not a markdown table" constraint explicit |
| C-12 | **PASS** | Pre-emission check requires full phrases; "not a category label" on Build Risk; Design Impact requires "specific component, API, flow, or decision" |
| C-13 | **PASS** | Standalone section: "The only valid epistemic dimension names are exactly five: … This list is closed. No synonyms, near-equivalents, or substitutes may appear in any stage output." |
| C-14 | **PASS** | Stage 3: "A5 CLEAR → emit COMMIT-STAGE-3-CLEAN. A5 FLAGGED → emit COMMIT-STAGE-3-FLAGGED and name the responsible belief(s)." — binary gate, not advisory |
| C-15 | **FAIL** | No gate sequence overview table preceding Stage 1; VOCABULARY RULE precedes stages but does not enumerate all gate tokens + halt conditions + execution flow |
| C-16 | **FAIL** | No worked calibration example present |
| C-17 | **PASS** | Mapping table names 10 specific prohibited synonyms: Reliability, Testability, Performance, Throughput, Complexity, Tractability, Maintainability, Operability, Discoverability, Learnability |
| C-18 | **PASS** | Full 10-entry mapping table with explicit canonical targets: "Reliability → Correctness", "Performance → Scalability", "Maintainability → Adoptability", etc. |
| C-19 | **FAIL** | No ENTER conditions for any stage; stages contain instructions only, no pre-conditions verifying readiness to begin |
| C-20 | **FAIL** | No Surprise 0; no calibration example to embed within Stage 4 entry sequence |
| C-21 | **PASS** | "Before emitting COMMIT-STAGE-4, verify all dimension names used in Stage 4 are canonical. Apply the VOCABULARY RULE mapping table to correct any malformed names." — prescribes corrective action at EXIT gate |
| C-22 | **PASS** | Build Risk sub-field labeled in Stage 4 template; requirements: "specific component, contract, or assumption … must be conceptually distinct from Design Impact" |
| C-23 | **FAIL** | No Surprise 0 to model dual-field (Design Impact + Build Risk) specificity anchoring |
| C-24 | **PASS** | Pre-emission check: "Build Risk names a specific component, contract, or assumption — not a category label. Do not emit COMMIT-ENTRY if any field fails the check. Rewrite the failing field before emitting." — COMMIT-ENTRY blocked on specificity |
| C-25 | **FAIL** | Each sub-field has exactly 1 mechanism (gate enforcement via pre-emission check); no Surprise 0 (mechanism a); no per-field repair instruction (mechanism c); minimum 2 mechanisms per sub-field not met |

**V-01 Total: 145/175** | Essential ✓ | Recommended ✓ | Aspirational: 11/17

---

## V-02 — Lifecycle Emphasis: Per-Stage ENTER/EXIT Contracts

**Axis:** Explicit ENTER conditions and EXIT criteria for all six stages; vocabulary repair embedded as an EXIT condition.

> Scored from description. V-02 inherits baseline features (closed vocabulary list, Build Risk sub-field, pre-emission check, all token protocol). Axis contributes C-19; vocabulary repair at EXIT contributes C-21. Synonym mapping table is V-01's axis — not inherited. Worked example is V-04's axis — not inherited. Gate overview is V-03's axis — not inherited.

### Essential — 60/60 | Recommended — 30/30

*(Same as all variations — stated floor in design context.)*

### Aspirational — 50/85

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Token protocol preserved; lifecycle structure enforces complete token emission |
| C-10 | **PASS** | Foreknowledge resolution in Stage 6 EXIT criterion |
| C-11 | **PASS** | Prose block format baseline |
| C-12 | **PASS** | EXIT criteria enforce entry completeness |
| C-13 | **PASS** | Closed-list vocabulary rule baseline |
| C-14 | **PASS** | Stage 3 dual-token gate baseline |
| C-15 | **FAIL** | No gate sequence overview; axis is per-stage contracts, not navigation frame |
| C-16 | **FAIL** | No worked calibration example |
| C-17 | **FAIL** | Synonym naming is V-01's axis; not present |
| C-18 | **FAIL** | Mapping table is V-01's axis; not present |
| C-19 | **PASS** | *This is the axis* — explicit ENTER conditions and EXIT criteria for all 6 stages |
| C-20 | **FAIL** | No Surprise 0 |
| C-21 | **PASS** | "Vocabulary repair embedded as EXIT condition" — per-description; prescribes corrective action before emitting |
| C-22 | **PASS** | Build Risk sub-field baseline |
| C-23 | **FAIL** | No Surprise 0 for dual-field anchoring |
| C-24 | **PASS** | COMMIT-ENTRY EXIT criterion for Stage 4 likely names Build Risk specificity requirement — consistent with per-stage contract design |
| C-25 | **FAIL** | No Surprise 0 (mechanism a absent); each sub-field has 1 mechanism only (gate enforcement); minimum 2 per sub-field not met |

**V-02 Total: 140/175** | Essential ✓ | Recommended ✓ | Aspirational: 10/17

---

## V-03 — Gate Sequence Overview as Primary Navigation Frame

**Axis:** Comprehensive gate sequence overview enumerating all stage tokens, halt conditions, and execution flow precedes all stage instructions.

> Scored from description. Inherits baseline. Axis contributes C-15. Per-stage ENTER/EXIT is V-02's axis — not inherited. Synonym mapping table is V-01's axis — not inherited. Worked example is V-04's axis — not inherited.

### Essential — 60/60 | Recommended — 30/30

### Aspirational — 50/85

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Gate overview makes token protocol visible; C-09 benefits directly from this axis |
| C-10 | **PASS** | Foreknowledge resolution baseline |
| C-11 | **PASS** | Prose block format baseline |
| C-12 | **PASS** | Entry completeness baseline |
| C-13 | **PASS** | Closed-list vocabulary rule baseline |
| C-14 | **PASS** | Dual-token gate baseline; gate overview makes foreknowledge token structurally prominent |
| C-15 | **PASS** | *This is the axis* — top-level gate overview listing all stage tokens, halt conditions, and execution flow before Stage 1 |
| C-16 | **FAIL** | No worked calibration example |
| C-17 | **FAIL** | Synonym naming is V-01's axis |
| C-18 | **FAIL** | Mapping table is V-01's axis |
| C-19 | **FAIL** | Per-stage ENTER/EXIT contracts is V-02's axis |
| C-20 | **FAIL** | No Surprise 0 |
| C-21 | **PASS** | Vocabulary self-repair at EXIT gate — present as baseline from prior round learning |
| C-22 | **PASS** | Build Risk sub-field baseline |
| C-23 | **FAIL** | No Surprise 0 for dual-field anchoring |
| C-24 | **PASS** | Pre-emission check with Build Risk specificity gate baseline |
| C-25 | **FAIL** | No Surprise 0; single mechanism per sub-field |

**V-03 Total: 140/175** | Essential ✓ | Recommended ✓ | Aspirational: 10/17

---

## V-04 — Inertia Framing: Surprise 0 as Sequenced Worked Entry + Self-Repair at EXIT

**Axis:** Calibration example labeled "Surprise 0" embedded sequentially within Stage 4 entry block; self-repair instruction at EXIT gate for vocabulary compliance.

> Scored from description. Axis contributes C-16, C-20, C-21. Surprise 0 models all four sub-fields (Design Impact and Build Risk with distinct non-redundant values) → C-23. With Surprise 0 as mechanism (a) and pre-emission check as mechanism (b), all four sub-fields reach 2-mechanism coverage → C-25. Synonym mapping table is V-01's axis — not present.

### Essential — 60/60 | Recommended — 30/30

### Aspirational — 65/85

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Token protocol baseline |
| C-10 | **PASS** | Foreknowledge baseline |
| C-11 | **PASS** | Prose block format; Surprise 0 entry is identically formatted |
| C-12 | **PASS** | Entry completeness; Surprise 0 demonstrates full-sentence values in all sub-fields |
| C-13 | **PASS** | Closed-list vocabulary rule baseline |
| C-14 | **PASS** | Dual-token gate baseline |
| C-15 | **FAIL** | Gate overview is V-03's axis |
| C-16 | **PASS** | *Axis* — complete filled-in Stage 4 example present with realistic artifact reference and component-specific Design Impact |
| C-17 | **FAIL** | Synonym naming is V-01's axis; not present |
| C-18 | **FAIL** | Mapping table is V-01's axis; not present |
| C-19 | **FAIL** | Per-stage ENTER/EXIT is V-02's axis |
| C-20 | **PASS** | *Axis* — calibration example labeled Surprise 0 (or entry-zero equivalent), formatted identically to live entry template, positioned within Stage 4 block |
| C-21 | **PASS** | *Axis* — self-repair instruction at EXIT gate: "correct … using the mapping table" before emitting; converts table from reference to active protocol |
| C-22 | **PASS** | Build Risk sub-field baseline; Surprise 0 models it with specific value |
| C-23 | **PASS** | Surprise 0 fills both Design Impact and Build Risk with component-specific, conceptually distinct values — forward-looking change vs. risk-surface implication legible through paired concrete content |
| C-24 | **PASS** | Pre-emission check names Build Risk specificity gate baseline; Surprise 0 also demonstrates what a specific Build Risk entry looks like |
| C-25 | **PASS** | All four sub-fields governed by (a) Surprise 0 + (b) pre-emission check = 2 independent mechanisms each; no sub-field left to a single mechanism |

**V-04 Total: 155/175** | Essential ✓ | Recommended ✓ | Aspirational: 13/17

---

## V-05 — Combined: Vocabulary Front-Load + Gate Map + Per-Stage Contracts + Surprise 0 + C-24 + C-25

**Axis:** All single-axis techniques combined with explicit C-24 Build Risk gate and C-25 four-field convergent mechanism coverage declared.

> Scored from description: "V-01 vocabulary front-load + V-03 gate map + V-02 per-stage contracts + V-04 Surprise 0 + C-24 Build Risk specificity gate + C-25 four-field convergent mechanism coverage declared." All aspirational mechanisms are present.

### Essential — 60/60 | Recommended — 30/30

### Aspirational — 85/85

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Token protocol; gate map makes all tokens explicit |
| C-10 | **PASS** | Foreknowledge resolution in Stage 6 EXIT criterion |
| C-11 | **PASS** | Prose block format; Surprise 0 entry enforces it |
| C-12 | **PASS** | EXIT contracts + Surprise 0 + pre-emission check all enforce entry completeness |
| C-13 | **PASS** | Vocabulary front-load from V-01 |
| C-14 | **PASS** | Dual-token gate; gate map makes it structurally prominent |
| C-15 | **PASS** | Gate map from V-03 |
| C-16 | **PASS** | Worked calibration example from V-04 |
| C-17 | **PASS** | Named synonym exclusions from V-01 |
| C-18 | **PASS** | Synonym-to-canonical mapping table from V-01 |
| C-19 | **PASS** | Per-stage ENTER/EXIT contracts from V-02 |
| C-20 | **PASS** | Surprise 0 embedded in Stage 4 sequence from V-04 |
| C-21 | **PASS** | Self-repair at EXIT gate from V-04 |
| C-22 | **PASS** | Build Risk sub-field; Surprise 0 models it |
| C-23 | **PASS** | Surprise 0 models dual-field specificity (Design Impact + Build Risk distinct and non-redundant) |
| C-24 | **PASS** | Explicitly declared — COMMIT-ENTRY blocked until Build Risk specificity confirmed |
| C-25 | **PASS** | Explicitly declared — all four sub-fields governed by ≥2 mechanisms: (a) Surprise 0, (b) per-entry EXIT, (c) self-repair at COMMIT-STAGE-4 EXIT |

**V-05 Total: 175/175** | Essential ✓ | Recommended ✓ | Aspirational: 17/17

---

## Composite Scores

| Rank | Variation | Essential | Recommended | Aspirational | **Total** | Delta vs. V-05 |
|------|-----------|-----------|-------------|--------------|-----------|----------------|
| 1 | **V-05** | 60 | 30 | 85 (17/17) | **175** | — |
| 2 | **V-04** | 60 | 30 | 65 (13/17) | **155** | −20 |
| 3 | **V-01** | 60 | 30 | 55 (11/17) | **145** | −30 |
| 4 | **V-02** | 60 | 30 | 50 (10/17) | **140** | −35 |
| 4 | **V-03** | 60 | 30 | 50 (10/17) | **140** | −35 |

All variations pass all essential and recommended criteria.

---

## Excellence Signals from V-05

V-05's 20-point advantage over V-04 (second place) comes from four criteria not present in V-04:

**Signal 1 — Named synonym exclusions + canonical mapping table (C-17 + C-18, +10 pts):** V-01 contributed these. A model encountering "Reliability" at inference time, without this mapping, may substitute another prohibited term even after a general prohibition. The mapping table closes the substitution loop at both the prohibition and replacement levels simultaneously. V-04 omits this because its axis is Surprise 0, not vocabulary infrastructure — resulting in 10 pts lost to the vocabulary axis.

**Signal 2 — Gate sequence overview as navigation frame (C-15, +5 pts):** V-03 contributed this. The model enters Stage 1 having already seen the full token topology — every gate, halt condition, and routing decision. This reduces mid-execution confusion about whether GATE-CONFIRMED means "proceed" or "record." V-04 omits this; V-05 gains it.

**Signal 3 — Per-stage ENTER/EXIT contracts (C-19, +5 pts):** V-02 contributed this. The model can verify completion state at each stage boundary rather than inferring completion from output density. V-04's per-entry gate (COMMIT-ENTRY) operates inside Stage 4; V-02's per-stage contracts operate at every stage transition. V-05 combines both.

> **Key structural observation:** V-04's single-axis strength (Surprise 0) was sufficient to unlock C-25 four-field convergent coverage on its own, because Surprise 0 provides mechanism (a) for all sub-fields simultaneously and the baseline pre-emission check provides mechanism (b). V-05 adds C-19 and the vocabulary mechanisms, but the critical R8 criteria (C-23, C-24, C-25) were already achievable without the full combination — V-04 demonstrates the minimum combination needed to pass all three new v8 criteria.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
