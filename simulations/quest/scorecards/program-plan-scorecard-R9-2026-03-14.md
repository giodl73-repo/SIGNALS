Now I have everything needed. Let me score all five R9 variations against the v9 rubric.

---

# program-plan — Round 9 Scorecard (v9 Rubric)

## Scoring Basis

All five R9 variates **inherit R8 V-05 ceiling (225/235 under v9)**. The four R9 new axes (`requires:`, `grounded-in:`, `falsified-if:`, `arc-asserts:`) are post-v9 innovations — no v9 criterion (C-01 through C-35) covers them. Scoring proceeds as: confirm inheritance (no regressions), then identify excellence signals for v10.

---

## Per-Criterion Evaluation (All Variations)

All five inherit all pre-computation steps, inline catalog, actor table, gate format family, and arc-strategy from R8 V-05. Per-criterion analysis confirms:

### Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-01 | Valid YAML structure | PASS | PASS | PASS | PASS | PASS | All include explicit YAML template with `stages:`, `name:`, `skills:`, `gate:`, `auto: true` |
| C-02 | Echo stage contract | PASS | PASS | PASS | PASS | PASS | All YAML templates include `name: echo`, `skills: []`, `auto: true`; no other stage named echo |
| C-03 | All skills valid | PASS | PASS | PASS | PASS | PASS | All include full 47-skill inline catalog; gate format references only catalog skills |
| C-04 | Gates present and non-trivial | PASS | PASS | PASS | PASS | PASS | Gate format strings include threshold + artifact + cascade + semantic claim; not empty or "done" |
| C-05 | Skills ordered by dependency | PASS | PASS | PASS | PASS | PASS | Actor table + displacement register enforce scout→draft→review/prove→flow/trace→listen→metrics/goals order |

**Essential score: 5/5 — all variations** → 60 pts

---

### Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-06 | Stages group skills meaningfully | PASS | PASS | PASS | PASS | PASS | Step 3 (Stage Grouping) + Step 5 (Cohesion Audit) enforce coherent phase grouping |
| C-07 | Gate conditions reference artifacts | PASS | PASS | PASS | PASS | PASS | Gate format mandates artifact type in lineage prefix (`[Skill X produces artifact_type]`) |
| C-08 | Stage names descriptive | PASS | PASS | PASS | PASS | PASS | Step 3 explicitly prohibits skill names as stage names; requires human-readable labels |

**Recommended score: 3/3 — all variations** → 30 pts

---

### Aspirational Criteria — All Variations

All five variates inherit R8 V-05's full aspirational pass set. The key inherited criteria:

| ID | Criterion | All V-01–V-05 | Key Evidence |
|----|-----------|---------------|-------------|
| C-09 | Strategic pacing | PASS | Arc strategy step names breadth→depth→validation→synthesis→closure arc |
| C-10 | Gates quantified | PASS | Step 9 threshold calibration; gate format embeds `>=N` |
| C-11 | Inline skill catalog | PASS | All five include full 47-skill block; no external file reference |
| C-12 | Actor-role framing | PASS | Gate format: "[Delivering actor] hands off to [Receiving actor]" |
| C-13 | `>=N` syntax instructed | PASS | Gate format specifies `>=N artifact_type` inline |
| C-14 | Naive-competitor framing | PASS | All openers name specific failure modes + structural choice defeating each |
| C-15 | Why-this-position column | PASS | Actor table column header + all entries have displacement consequence |
| C-16 | Unified handoff+threshold template | PASS | Gate format string combines actor + `>=N` + artifact in single required format |
| C-17 | What-happens-if-removed | PASS | Gate format embeds cascade-if-removed; Arc Strategy Q2 targets first gate |
| C-18 | Header displacement impossibility | PASS | "Why this actor cannot run earlier — and what cascade breaks downstream" |
| C-19 | Multi-hop consequence cascade | PASS | All actor entries include `->` notation with 3-hop chains |
| C-20 | Header embeds cascade spec | PASS | Header contains "use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries" |
| C-21 | All actor entries cascade | PASS | All six actor rows use 3-hop `->` chains crossing arc-layer boundaries |
| C-22 | Gate cascade-if-removed embedded | PASS | Gate format: "removing this gate: [A -> B -> C, minimum 2 hops…]" |
| C-23 | First-gate cascade explicit | PASS | Arc Strategy Q2 explicitly names scout handoff gate + traces first-gate cascade |
| C-24 | Gate cascade notation+depth | PASS | Gate template specifies "minimum 2 hops crossing arc-layer boundaries" |
| C-25 | Gate cascade audit table | PASS | Step 11 is mandatory gate cascade audit table covering all non-echo gates |
| C-26 | Echo displacement reasoning | PASS | Step 13 requires arc-completion signal + 2-hop consequence if echo fires early |
| C-27 | Gate-to-gate chain | PASS | Gate format includes "and gate N+1 loses: [adjacent consequence]" |
| C-28 | Stage displacement register | PASS | Step 4 mandates per-stage displacement impossibility + cascade column |
| C-29 | Stage cohesion audit | PASS | Step 5 mandates per-stage shared goal + per-skill displacement |
| C-30 | Skill omission register | PASS | Step 16 mandates every excluded skill named with topic-specific reason |
| C-31 | Artifact lineage chain | PASS | Step 7 mandates per-gate producing skill + artifact type |
| C-32 | Non-adjacent consumer traced | PASS | Step 8 (Consumer Map) requires non-adjacent consumer trace; long-reach flagged |
| C-33 | Arc-uniqueness register | PASS | Step 6 requires unique contribution + arc-gap cascade per non-echo stage |
| C-34 | Threshold calibration | PASS | Step 9 requires minimum N floor + topic-specific rationale per gate |
| C-35 | Gate semantic assertion (`asserting:`) | PASS | All gate format strings include `asserting:` clause (R9 additions embed it; V-02 adds `grounded-in:` inside it — does not remove it; C-35 still satisfied) |

**Aspirational score: 27/27 — all variations** → 135 pts

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite | Golden (≥188)? |
|-----------|-----------|-------------|-------------|-----------|----------------|
| V-01 | 60 | 30 | 135 | **225/235** | YES |
| V-02 | 60 | 30 | 135 | **225/235** | YES |
| V-03 | 60 | 30 | 135 | **225/235** | YES |
| V-04 | 60 | 30 | 135 | **225/235** | YES |
| V-05 | 60 | 30 | 135 | **225/235** | YES |

**All five variations tie at 225/235. All pass golden threshold.** The tie is expected: v9 has no criteria for R9 innovations (requires:, grounded-in:, falsified-if:, arc-asserts:).

---

## Variation Ranking

All five rank equal at 225/235 under v9. By richness of new axes (informing v10 priority):

1. **V-05** — all four axes: bidirectional gates + semantic chain + falsification + arc-asserts (R10 anchor)
2. **V-04** — two axes: bidirectional gates (requires: + grounded-in: triad)
3. **V-01** — one axis: gate entry pre-condition (requires:)
4. **V-02** — one axis: semantic gate chain (grounded-in:)
5. **V-03** — one axis: gate assertion falsification (falsified-if:)

V-01/V-02/V-03 rank equally by v9; V-04 and V-05 are formally richer but not discriminated by v9.

---

## Excellence Signals from V-05 (Ceiling)

**Signal R9-1: Gate Entry Pre-condition (`requires:`)**  
C-35 introduced exit semantics (`asserting:` = what becomes true after the threshold passes). V-01/V-05 add entry semantics: `requires:` = what must be established about the evidence state *before* counting begins. Without an explicit entry condition, a gate asserting ">=2 scout signals" is valid regardless of whether those signals address the right question. `requires:` names the evidence quality that makes the artifact count meaningful. Design family: completes C-35's one-directional exit claim into bidirectional gate semantics.

**Signal R9-2: Semantic Gate Chain (`grounded-in:`)**  
C-27 required that removing gate N names a consequence for gate N+1 (structural cascade chain). V-02/V-05 create the parallel at the semantic level: `grounded-in:` inside each `asserting:` clause names the prior gate's evidence assertion as the foundation this gate's assertion is built upon. A program whose evidence claims are semantically isolated (each gate asserts something independent) passes C-35 but hides whether the evidence arc is coherent. `grounded-in:` makes arc coherence structurally explicit. The first gate cites topic-scope assumptions rather than a prior gate.

**Signal R9-3: Gate Assertion Falsification (`falsified-if:`)**  
C-35's `asserting:` is a semantic declaration. V-03/V-05 add `falsified-if:` — the specific evidence event that would invalidate the assertion post-passage. This converts the declaration into a falsifiable claim. Without a falsification condition, a team that discovers contradicting evidence post-gate has no structural basis for revisiting. `falsified-if:` makes course-correction structurally triggered: if the named condition is encountered, the program must revisit prior stages rather than continuing on false evidence.

**Signal R9-4: Program-Level Evidence Arc Assertion (`arc-asserts:`) — R10 anchor**  
V-05 adds Step 15a and a top-level `arc-asserts:` field in YAML. This is the program-level analogue of C-35's gate-level `asserting:`: after the full `asserting:` sequence is produced, the program synthesizes them into a single proposition — what the program claims to prove when it runs to completion. The coherence test (every component of `arc-asserts:` must trace to at least one gate assertion) makes the program's overall evidence proposition verifiable against its own internal structure. This is the R9 single-variation signal, the natural v10 anchor.

**Structural pattern**: R9 completes the gate-semantics completeness family:
- C-35 (R8): exit condition (`asserting:`)
- R9 V-01: entry condition (`requires:`)
- R9 V-02: continuity assertion (`grounded-in:`)
- R9 V-03: falsification condition (`falsified-if:`)
- R9 V-05: program synthesis (`arc-asserts:`)

Gates are now fully specified at four semantic levels (entry → exit → continuity → falsification), with a program-level synthesis. V-05 is the first variation with complete gate semantics.

---

## v10 Gap

**C-36 candidate**: `arc-asserts:` coherence check — the program-level arc assertion is derivable from and constrained by the `asserting:` sequence. V-05 is the single-variation signal. This is the R10 anchor. Variations could explore: single-axis (`arc-asserts:` alone), falsification-of-arc (`arc-falsified-if:` at program level), or `arc-asserts:` + `requires:` coherence (the entry-to-program continuity chain).

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["Gate entry pre-condition (requires:) produces bidirectional gate semantics: entry evidence state (what must hold before counting) pairs with C-35 exit evidence claim (what becomes true when counting passes), making gate threshold evaluability explicit", "Semantic gate chain (grounded-in:) links consecutive asserting: clauses into an explicit evidence continuity chain — each gate's assertion names the prior gate assertion as its foundation, paralleling C-27's structural cascade chain at the evidence-meaning level", "Gate assertion falsification (falsified-if:) converts C-35's one-directional semantic declaration into a testable claim by naming the specific evidence event that would invalidate the assertion post-passage, enabling structurally triggered course correction", "Program-level arc assertion (arc-asserts:) synthesizes the full asserting: sequence into a single program-level evidence proposition with a coherence test requiring every component to trace to at least one gate assertion — the R10 anchor, program-granularity analogue of C-35"]}
```
