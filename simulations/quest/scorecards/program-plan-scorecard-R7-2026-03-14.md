I now have all five variation bodies. Let me score them systematically against the v7 rubric.

---

## program-plan — R7 Scorecard (Round 7, Rubric v7)

**Scoring date:** 2026-03-15
**Rubric:** v7 (185 pts max; golden threshold 148)
**Variations:** V-01 (Stage Displacement Register), V-02 (Stage Cohesion Audit Table), V-03 (Skill Omission Register), V-04 (V-01+V-02), V-05 (V-01+V-02+V-03+Artifact Lineage Chain)

---

### Shared Baseline Verification

All five R7 variations inherit R6 V-05 word-for-word on the following structural elements:

| Element | Present in all 5? | Evidence |
|---------|-------------------|----------|
| Inline skill catalog (all namespaces) | Yes | scout/draft/review/flow/trace/prove/listen/program/metrics/goals enumerated in every body |
| Actor ordering table with 3-hop -> entries | Yes | Same 6-row table with "Moved later: A -> B -> C" entries |
| Column header with displacement-impossibility + cascade notation + depth floor | Yes | "why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)" |
| Gate format: actor + threshold + `->` depth-floored cascade clause + adjacent N+1 clause | Yes | `"[Delivering actor] hands off ... when >=N ... -- removing this gate: [A -> B -> C, minimum 2 hops ...] -- and gate N+1 loses: ..."` |
| Gate Cascade Audit Table (pre-YAML, all non-echo gates, "Adjacent gate N+1 loses" column) | Yes | Separate required step before YAML assembly |
| Echo stage displacement reasoning (a + b) | Yes | Required step with arc-completion signal + consequence of firing at stage 2 |
| Arc strategy: first gate (scout handoff) cascade explicitly named | Yes | "Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed?" |
| Naive-competitor framing opener | Yes | All five open with explicit failure mode + structural response |

Baseline verdict: all five carry the full R6 V-05 structural payload.

---

### Per-Criterion Scoring — All Variations

#### Essential Criteria (C-01 through C-05)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Valid YAML structure | PASS | PASS | PASS | PASS | PASS |
| C-02 | Echo stage contract (`skills: []`, `auto: true`, last position) | PASS | PASS | PASS | PASS | PASS |
| C-03 | All referenced skills valid (catalog inline, no hallucination) | PASS | PASS | PASS | PASS | PASS |
| C-04 | Gates present and non-trivial (threshold + cascade clause) | PASS | PASS | PASS | PASS | PASS |
| C-05 | Skills ordered by dependency layer | PASS | PASS | PASS | PASS | PASS |

Essential score: **5/5 → 60 pts** for all variations.

#### Recommended Criteria (C-06 through C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Stages group skills meaningfully (3–6 coherent phases) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Gate conditions reference artifact types/counts | PASS | PASS | PASS | PASS | PASS |
| C-08 | Stage names are descriptive (human-readable labels) | PASS | PASS | PASS | PASS | PASS |

Recommended score: **3/3 → 30 pts** for all variations.

#### Aspirational Criteria (C-09 through C-27)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Strategic pacing across signal types | PASS | PASS | PASS | PASS | PASS | Actor table drives breadth→depth→synthesis ordering in all |
| C-10 | Gates are quantified (`>=N` threshold in output) | PASS | PASS | PASS | PASS | PASS | Gate format string embeds `>=N artifact_type` in all |
| C-11 | Skill catalog grounded inline | PASS | PASS | PASS | PASS | PASS | Full catalog in every body; no external reference |
| C-12 | Actor-role framing for gates | PASS | PASS | PASS | PASS | PASS | "[Delivering actor] hands off to [Receiving actor]" in all gate templates |
| C-13 | Quantified gate syntax instructed (`>=N` in gate-writing instruction) | PASS | PASS | PASS | PASS | PASS | `>=N artifact_type` embedded in gate format instruction in all |
| C-14 | Naive-competitor framing (failure mode + structural response named) | PASS | PASS | PASS | PASS | PASS | All five openers name specific failure mode(s) + defeating structure |
| C-15 | Why-this-position column in actor table (position + displacement consequence) | PASS | PASS | PASS | PASS | PASS | All actor table entries combine position rationale + "Moved later: A -> B -> C" |
| C-16 | Unified handoff+threshold gate template (actor + `>=N` + artifact_type in one string) | PASS | PASS | PASS | PASS | PASS | All gate formats contain all three elements unified |
| C-17 | What-happens-if-removed clause in arc strategy | PASS | PASS | PASS | PASS | PASS | First-gate-specific cascade in arc strategy step in all |
| C-18 | Column header frames displacement impossibility | PASS | PASS | PASS | PASS | PASS | Header: "cannot run earlier — and what cascade breaks downstream" |
| C-19 | Multi-hop downstream consequence cascade (at least one 2+ hop entry) | PASS | PASS | PASS | PASS | PASS | Every actor entry has 3-hop chain; all satisfy ≥1 cascade entry |
| C-20 | Header embeds cascade notation and depth requirement | PASS | PASS | PASS | PASS | PASS | Header contains both impossibility clause AND "use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries" |
| C-21 | All actor entries demonstrate cascade depth | PASS | PASS | PASS | PASS | PASS | 6/6 actor entries have 3-hop -> chains in all variations |
| C-22 | Gate template embeds cascade-if-removed clause | PASS | PASS | PASS | PASS | PASS | "-- removing this gate: [A -> B -> C, minimum 2 hops...]" inside gate format string |
| C-23 | Arc-strategy names first-gate cascade explicitly | PASS | PASS | PASS | PASS | PASS | "specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed?" |
| C-24 | Cascade-if-removed clause embeds `->` notation spec + depth floor | PASS | PASS | PASS | PASS | PASS | "[A -> B -> C, minimum 2 hops crossing arc-layer boundaries]" is inside the cascade clause in all gate templates |
| C-25 | Gate Cascade Audit Table pre-computes all non-echo gates before YAML | PASS | PASS | PASS | PASS | PASS | Dedicated required step in all; has "Adjacent gate N+1 loses" column |
| C-26 | Echo stage displacement reasoning (a + b) | PASS | PASS | PASS | PASS | PASS | All variations have dedicated echo justification step with arc-completion signal + stage-2 firing consequence |
| C-27 | Gate-to-gate chain: removing gate N names consequence for gate N+1 | PASS | PASS | PASS | PASS | PASS | "Adjacent gate N+1 loses" column in audit table; "-- and gate N+1 loses:" in every gate string |

Aspirational score: **19/19 → 95 pts** for all variations.

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (95) | Total (185) | Golden (>=148)? |
|-----------|---------------|-------------------|-------------------|-------------|-----------------|
| V-01 | 60 | 30 | 95 | **185** | YES |
| V-02 | 60 | 30 | 95 | **185** | YES |
| V-03 | 60 | 30 | 95 | **185** | YES |
| V-04 | 60 | 30 | 95 | **185** | YES |
| V-05 | 60 | 30 | 95 | **185** | YES |

All five R7 variations reach the v7 ceiling at **185/185**. The v7 rubric is fully saturated by all R7 designs. This is the expected outcome — R7 axes were designed to extend beyond the v7 discriminator surface, not to score differently under v7.

---

### Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tied) | V-01, V-02, V-03, V-04, V-05 | 185/185 | All pass all 27 criteria |

Under the v7 rubric the five are indistinguishable. Ranking requires the R8 rubric. The design order by R8 candidate density is:

**V-05 > V-04 > V-01 = V-02 = V-03** (V-05 introduces four new axes; V-04 introduces two; V-01/V-02/V-03 each introduce one).

---

### Excellence Signals (R8 Rubric Candidates)

The R7 variations introduce four structurally new forcing functions that are undetectable by C-01 through C-27. Each is a strong R8 candidate:

---

**Signal R7-01 — Stage Displacement Register (V-01, V-04, V-05)**

A pre-YAML register where every non-echo stage (positions 2 through N) must state:
(a) why it cannot fire one position earlier (specific artifact dependency on the predecessor), and
(b) what breaks if it does (2+ hop cascade crossing arc-layer boundaries).

*Why this discriminates:* This is the stage-level analogue of the actor ordering table. C-18/C-20/C-21 apply that pattern to actor entries; the Stage Displacement Register applies it to stage-boundary transitions. A variation without this register can produce a topologically valid stage sequence that is nonetheless ungrounded — each boundary is positioned by convention, not by an explicit impossibility argument. The register makes stage-boundary justification a mandatory pre-computation, not an emergent outcome.

*R8 criterion shape:* "The variation requires a Stage Displacement Register (or equivalent) as a mandatory pre-YAML step where every non-echo stage position 2+ produces (a) an impossibility clause naming the missing predecessor artifact and (b) a 2+ hop cascade consequence of premature firing crossing arc-layer boundaries."

---

**Signal R7-02 — Stage Cohesion Audit Table (V-02, V-04, V-05)**

A pre-YAML audit table where every non-echo stage must state:
(a) the shared phase goal that justifies this exact skill grouping (not namespace co-location but a named evidence objective), and
(b) per-skill displacement consequence (what breaks if skill X moves to a different stage).

*Why this discriminates:* C-06 checks whether output stages are meaningfully grouped. The Stage Cohesion Audit Table checks whether the grouping rationale is pre-computed and visible as a structural constraint before any YAML stage is assembled. The C-25 Gate Cascade Audit Table established this pattern for gate cascades; the Stage Cohesion Audit Table applies it to skill-grouping decisions. Without it, skill groupings are heuristic even when outputs look coherent.

*R8 criterion shape:* "The variation requires a Stage Cohesion Audit Table (or equivalent) as a mandatory pre-YAML step where every non-echo stage produces a shared phase goal statement + per-constituent-skill displacement consequence naming what is lost if that skill is moved."

---

**Signal R7-03 — Skill Omission Register (V-03, V-05)**

A post-YAML register where every skill in the inline catalog that does NOT appear in the program must be listed with a topic-specific exclusion reason (generic reasons explicitly prohibited).

*Why this discriminates:* C-11 ensures the full catalog is listed inline; C-03 ensures included skills are valid. But neither verifies that exclusions are deliberate. A program that omits `trace:migration` because the topic is a new feature with no existing schema is making a different decision than one that omits it accidentally. The Skill Omission Register makes catalog selection two-sided: inclusions are visible in YAML; exclusions are visible and justified in the register. Deliberate exclusion reasoning is not measurable from the YAML alone.

*R8 criterion shape:* "The variation requires a Skill Omission Register (or equivalent post-YAML step) listing every excluded catalog skill with a topic-specific reason; generic reasons ('not needed', 'optional') explicitly do not pass."

---

**Signal R7-04 — Artifact Lineage Chain (V-05 only)**

A pre-YAML table (step before the Gate Cascade Audit Table) that identifies, for each gate, the specific skill in the preceding stage that produces the artifact type named in the gate threshold. This lineage chain is then prefixed to every gate string: `"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- ..."`.

*Why this discriminates:* C-16 specifies that gates must combine actor + threshold + artifact in a single format string. C-22/C-24 require the cascade-if-removed clause. But none of these require the gate to name which specific skill produces the required artifact. Without artifact lineage, a gate that says "when >=2 scout artifacts present" is ambiguous — it could be `scout:feasibility` alone, `scout:market` alone, or any combination. The Artifact Lineage Chain resolves this by tying every threshold to a named producing skill. This is a different level of traceability than cascade-consequence reasoning: it is provenance, not impact.

*R8 criterion shape:* "The variation requires an Artifact Lineage Chain step or table identifying the specific producing skill for each gate threshold, with the producing skill prefixed into the gate format string — e.g., '[Skill X in stage N produces artifact_type]; [actor] hands off when >=N artifact_type present'."

---

### R7 Design Principle Summary

| Signal | Pattern | Extends |
|--------|---------|---------|
| R7-01 Stage Displacement Register | Displacement-impossibility pre-computation per stage | C-18 (per-actor) → per-stage |
| R7-02 Stage Cohesion Audit Table | Pre-computation audit table for skill groupings | C-25 (gate cascades) → stage memberships |
| R7-03 Skill Omission Register | Complement-side catalog coverage with topic-specific rationale | C-11 (inclusion visible) → exclusion visible + justified |
| R7-04 Artifact Lineage Chain | Artifact provenance in gate threshold (producing skill named) | C-22/C-24 (cascade in gate) → producing skill in gate |

The four R7 axes are structurally orthogonal: R7-01 addresses stage-boundary justification, R7-02 addresses skill-grouping justification, R7-03 addresses catalog-exclusion justification, R7-04 addresses artifact-threshold provenance. No axis overlaps with another. V-05 (all four combined) is the natural R8 baseline anchor.

---

### Scorecard Written

```
simulations/quest/scorecards/program-plan-scorecard-R7-2026-03-14.md
```

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["Stage Displacement Register: mandatory pre-YAML step where every non-echo stage 2+ produces an impossibility clause (why it cannot fire one position earlier) and a 2+ hop cascade consequence of premature firing crossing arc-layer boundaries", "Stage Cohesion Audit Table: mandatory pre-YAML step where every non-echo stage produces a shared phase goal statement and per-constituent-skill displacement consequence naming what is lost if that skill moves to a different stage", "Skill Omission Register: mandatory post-YAML step listing every excluded catalog skill with a topic-specific exclusion reason; generic reasons explicitly prohibited, making catalog selection two-sided (inclusions in YAML, exclusions in register)", "Artifact Lineage Chain: pre-YAML table identifying the specific producing skill for each gate threshold, with producing skill identity prefixed into every gate format string — tying each threshold to a named skill rather than an abstract namespace-level artifact count"]}
```
