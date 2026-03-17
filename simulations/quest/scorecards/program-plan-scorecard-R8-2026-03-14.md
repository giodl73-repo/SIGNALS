## program-plan — Round 8 Scorecard (v8 rubric)

**Baseline condition:** All five variations inherit R7 V-05's complete structural payload (205/205 under v8). The R8 variate document makes this explicit: *"All five variations inherit R7 V-05's full structural payload (205/205 under v8). New axes isolate three single-axis extensions of the C-31 lineage-and-justification family, then combine."* Trace artifact is placeholder — scoring is on variation design specs.

---

### Essential Criteria (C-01 to C-05) — 60 pts

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Valid YAML structure | PASS | PASS | PASS | PASS | PASS |
| C-02 | Echo stage contract | PASS | PASS | PASS | PASS | PASS |
| C-03 | All referenced skills valid | PASS | PASS | PASS | PASS | PASS |
| C-04 | Gates present and non-trivial | PASS | PASS | PASS | PASS | PASS |
| C-05 | Skills ordered by dependency | PASS | PASS | PASS | PASS | PASS |

All essential criteria inherited from R7 V-05 payload. **60/60 all variations.**

---

### Recommended Criteria (C-06 to C-08) — 30 pts

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Stages group skills meaningfully | PASS | PASS | PASS | PASS | PASS |
| C-07 | Gate conditions reference artifacts | PASS | PASS | PASS | PASS | PASS |
| C-08 | Stage names are descriptive | PASS | PASS | PASS | PASS | PASS |

**30/30 all variations.**

---

### Aspirational Criteria (C-09 to C-31) — 115 pts

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|----|-----------|------|------|------|------|------|------|
| C-09 | Strategic pacing across signal types | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-10 | Gates quantified where possible | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-11 | Skill catalog grounded inline | PASS | PASS | PASS | PASS | PASS | Inherited — 47 skills enumerated |
| C-12 | Actor-role framing for gates | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-13 | Quantified gate syntax instructed | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-14 | Naive-competitor framing | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-15 | Why-this-position column in actor table | PASS | PASS | PASS | PASS | PASS | Inherited — consequence-of-displacement present |
| C-16–C-27 | (Prior round criteria) | PASS | PASS | PASS | PASS | PASS | Inherited from R7 V-05 |
| C-28 | Stage displacement register | PASS | PASS | PASS | PASS | PASS | Inherited from R7 V-05 |
| C-29 | Stage Cohesion Audit Table | PASS | PASS | PASS | PASS | PASS | Inherited from R7 V-05 |
| C-30 | Skill Omission Register | PASS | PASS | PASS | PASS | PASS | Inherited from R7 V-05 |
| C-31 | Artifact Lineage Chain | PASS | PASS | PASS | PASS | PASS | Inherited — R7 V-05 ceiling |

**115/115 all variations.**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | % |
|-----------|-----------|-------------|--------------|-------|---|
| V-01 | 60 | 30 | 115 | **205/205** | 100% |
| V-02 | 60 | 30 | 115 | **205/205** | 100% |
| V-03 | 60 | 30 | 115 | **205/205** | 100% |
| V-04 | 60 | 30 | 115 | **205/205** | 100% |
| V-05 | 60 | 30 | 115 | **205/205** | 100% |

**All five variations: ceiling under v8.** The v8 rubric has no discriminating surface among R8 variations — the R8 axes (Consumer Map, Arc-Uniqueness, Threshold Calibration, Semantic Claim) extend beyond C-31 and are not yet criteria.

---

### Ranking

**Structural rank under v8:** All tied at ceiling. Extension depth under post-v8 lens:

1. **V-05** — four new axes (R8-01 + R8-02 + R8-03 + R8-04); deepest structural payload
2. **V-04** — two new axes (R8-01 + R8-02); orthogonal graph + arc coverage
3. **V-01 / V-02 / V-03** — one new axis each; single-dimension extension

---

### Excellence Signals from V-05

V-05 is the natural ceiling candidate for four reasons:

1. **Full consumer lattice (R8-01):** C-31 traces each artifact to its gate consumer. V-05's Artifact Consumer Map extends this to *all* downstream consumers — including non-adjacent ones. The dependency graph becomes a lattice, not a chain. This exposes hidden multi-stage coupling that single-hop tracing leaves invisible.

2. **Irreplaceability justification per stage (R8-02):** C-28 asks why a stage cannot run earlier. V-05's Arc-Uniqueness Register asks the complementary question: why can't this stage be *absent*? Each stage must declare its unique evidence contribution AND the arc gap created by removal (2+ hops, arc-layer crossing). This closes the coverage gap between displacement-impossibility (C-28) and necessity-of-presence.

3. **N-selection as deliberate design (R8-03):** C-10 verifies N exists; C-13 verifies syntax. Neither requires reasoning for the specific N. V-05's Gate Threshold Calibration forces per-gate N-selection with a minimum floor (topic-independent lower bound) plus topic-specific choice rationale. N becomes an evidence-based design decision, not a placeholder.

4. **Gate as semantic assertion (R8-04):** The prior gate template structure (C-16/C-22/C-24) encodes cascade consequences. V-05's `asserting:` clause adds the evidence state claim — what is now true about the evidence when the threshold passes. This separates *count satisfied* from *claim established*, making gates verifiable at the semantic level.

---

### v9 Candidate Criteria

These four axes are the natural C-32 through C-35 candidates:

| ID (proposed) | Axis | Discriminates |
|---------------|------|---------------|
| C-32 | Artifact Consumer Map: non-adjacent consumer traced | V-01/V-04/V-05 vs V-02/V-03 |
| C-33 | Stage Arc-Uniqueness Register: contribution + arc gap per stage | V-02/V-04/V-05 vs V-01/V-03 |
| C-34 | Gate Threshold Calibration: N-selection with minimum floor + topic rationale | V-03/V-05 vs V-01/V-02/V-04 |
| C-35 | Gate Semantic Claim: `asserting:` clause per gate | V-05 only |

V-05 passes all four; V-04 passes C-32 + C-33; V-03 passes C-34; V-01 passes C-32; V-02 passes C-33.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["Artifact Consumer Map: full dependency lattice tracing every artifact to all downstream consumers including non-adjacent, extending C-31 single-hop lineage to multi-stage coverage", "Stage Arc-Uniqueness Register: irreplaceability justification requiring unique evidence contribution plus 2+-hop arc gap on removal, complementing C-28 displacement-impossibility with necessity-of-presence", "Gate Threshold Calibration: N-selection as deliberate design decision with minimum floor and topic-specific rationale, extending C-10/C-13 from syntax verification to reasoning requirement", "Gate Semantic Claim via asserting: clause embedding evidence state assertion in gate string, separating count-satisfied from claim-established for semantic-level gate verification"]}
```
