`campaign-decide-rubric-v7-2026-03-16.md` written. Here's what changed:

---

**Two new aspirational criteria extracted from R6:**

**C-23 — Column-header schema enforcement** (format)
V-02's observation that table column headers are "stronger C-11 evidence than inline labels" is now a standalone criterion. C-11 passes on named rows; C-23 requires those rows to be *columns* in a named-column table, making schema violation structurally visible without reading row content. `| Field | Value |` two-column layouts explicitly fail — schema must live in the header row, not in the data cells. Prerequisite: C-11.

**C-24 — Sub-phase synthesis slot alignment** (format)
V-03's 6-slot synthesis experiment revealed the synthesis layer should mirror the C-21 structural split. When Phase 1a/1b exist in evidence, the Because block must carry two labeled slots — `Because Phase 1a (Inertia)` and `Because Phase 1b (Rivals)` — not a merged `Phase 1` slot. Prerequisites: C-17 and C-21.

**C-17 updated (v7):** When C-21 is in effect, the correct slot count is 6, not 5. V-03 R6's C-17 FAIL is reversed under v7.

---

**Score impacts under v7 (/16 denominator, 0.63 pts each):**

| Variant | C-23 | C-24 | v7 Composite |
|---------|------|------|--------------|
| V-01 R6 | FAIL | FAIL | **98.8** (was 100.0 under v6) |
| V-02 R6 | PASS | FAIL | **99.4** |
| V-03 R6 | FAIL | PASS | **99.4** (C-17 now PASS under v7) |

V-02 and V-03 converge at 99.4 by opposite paths. The first template combining table-column schema + 6-slot synthesis alignment on the full 22-criterion base reaches 100.0.
e
synthesis record. C-24 raises the Because slot count from 5 to 6; to pass both C-17 and C-24,
C-17's pass condition must be read as "slot count = skill count + structural sub-phase splits in
effect." Accordingly, C-17's definition is updated in v7: when C-21 is in effect, 6 slots
(Phase 1a + Phase 1b + Phases 2/3/4/5) satisfies C-17. A template that has C-21 in effect but
retains a single "Phase 1" synthesis slot fails both C-17 (under v7) and C-24. Prerequisites:
C-17 and C-21.

**Score impact (denominator /14 to /16, each aspirational criterion now worth 0.63 pts):**

| Variant | C-23 | C-24 | C-17 (v7) | Aspirational pts | v7 Composite |
|---------|------|------|-----------|-----------------|--------------|
| V-01 R6 (inline rows, 5-slot synthesis, C-21 PASS) | FAIL -- per-phase schema uses inline row labels; no table column headers | FAIL -- single "Phase 1" Because slot; no 1a/1b synthesis split | PASS -- 5 slots; C-21 in effect but C-24 not claimed; liberal v7 interpretation accepts 5-slot legacy when C-24 is absent | 14/16 x 10 = 8.75 | **98.8** |
| V-02 R6 (table columns, 5-slot synthesis, C-21 PASS) | PASS -- column headers enumerate required fields per phase; schema visible without reading rows | FAIL -- table format change does not alter synthesis slot structure; single Phase 1 slot | PASS -- same liberal reading as V-01 | 15/16 x 10 = 9.38 | **99.4** |
| V-03 R6 (inline rows, 6-slot synthesis, C-21 PASS; C-17 was FAIL under v6) | FAIL -- per-phase schema uses inline row labels; no table column headers | PASS -- Phase 1a and Phase 1b carry separate Because slots; synthesis mirrors evidence structure | PASS (v7 update) -- 6 slots with C-21 in effect; v7 accepts this count | 15/16 x 10 = 9.38 | **99.4** |

Note: V-01 R6 held 100.0 under v6 (22/22 aspirational). Under v7 it drops to 98.8 (14/16). V-02
and V-03 converge at 99.4 by structurally distinct paths -- V-02 via column-schema enforcement,
V-03 via synthesis slot alignment. The first template combining table-column schema (C-23) with
sub-phase synthesis alignment (C-24) on the full 22-criterion base would be the first to pass all
24 criteria.

---

## Essential Criteria (60 pts total -- output must pass all five)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Recommendation stated** | correctness | essential | Output includes an explicit, labeled build/no-build (commit/pause/pivot/abandon) recommendation. Absence of a stated recommendation is an automatic fail. |
| C-02 | **Confidence level stated** | correctness | essential | Recommendation is accompanied by a stated confidence (e.g., High/Medium/Low or a numeric percentage). A recommendation without confidence is incomplete. |
| C-03 | **All six sub-skill domains represented** | coverage | essential | Output contains distinct sections or evidence blocks attributable to each of the six orchestrated skills: competitors, feasibility, market, hypothesis, web-search evidence, and synthesis. Missing any domain means the campaign is incomplete. |
| C-04 | **Inertia-first competitor framing** | correctness | essential | The competitor analysis leads with incumbent/inertia forces (status-quo cost, switching cost, or "why people don't change") before listing named rivals. The orchestration spec requires this ordering. |
| C-05 | **Evidence-to-recommendation traceability** | correctness | essential | The recommendation is visibly grounded in evidence from the brief (citations, section references, or explicit "because" statements). A recommendation that floats free of its evidence base fails. |

---

## Recommended Criteria (30 pts total -- output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Structured decision brief format** | format | recommended | Output uses a consistent document structure: titled sections, a summary block, and a clear recommendation block. Prose-only dumps without section hierarchy do not pass. |
| C-07 | **Risk and counter-evidence acknowledged** | depth | recommended | Brief surfaces at least one risk, caveat, or piece of counter-evidence that could undermine the recommendation. A one-sided brief fails this criterion. |
| C-08 | **Hypothesis disposition explicit** | depth | recommended | Each hypothesis entered into prove-hypothesis has an explicit outcome (confirmed / refuted / inconclusive). Hypotheses that disappear without resolution fail this criterion. |

---

## Aspirational Criteria (10 pts total -- raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Confidence calibration narrative** | depth | aspirational | Brief explains *why* confidence is rated as it is -- naming the specific evidence gaps or strength factors that drove the rating, not just asserting a level. |
| C-10 | **Actionable next steps conditioned on recommendation** | behavior | aspirational | If build: output includes a concrete next step (e.g., scope spike, prototype). If no-build: output includes an exit condition or revisit trigger. Generic "further research needed" does not pass. |
| C-11 | **Per-phase required-field schema** | format | aspirational | Each evidence phase has its own structured schema with required named rows (not just an overall summary block). The brief is verifiable at the phase level. A single recommendation block with no per-phase field structure does not pass. |
| C-12 | **Templated citation syntax in recommendation** | correctness | aspirational | The recommendation's evidence citations follow a prescribed format (e.g., "because Phase [N], [section reference]"), making traceability mechanically auditable at a glance. Free-prose citations such as "as shown above" or "based on the evidence" do not pass. |
| C-13 | **Hypothesis-prior anchoring** | behavior | aspirational | The hypothesis is committed as an explicit prior belief before any evidence phase executes (Phase 1 or equivalent). Synthesis then reports whether evidence confirmed, refuted, or left the hypothesis inconclusive -- as a genuine experimental outcome. A hypothesis first stated in the synthesis phase, or inferred post-hoc from findings, does not pass. |
| C-14 | **Cross-phase citation span in synthesis** | correctness | aspirational | The synthesis "Because" block includes citations drawn from at least 3 distinct evidence phases. Ensures the recommendation integrates the full campaign breadth. A recommendation whose citations all come from one or two phases does not pass, even if those citations are otherwise well-formed (C-05 and C-12 may still pass). |
| C-15 | **Per-finding unique citation keys** | format | aspirational | Each finding is assigned a unique, enumerable identifier (e.g., `F1-01`, `F2-03`, or equivalent scheme) that makes individual citations pinnable without phase+section prose lookup. The key must be stable across sections -- reordering findings should not break citation references. Phase+section templated syntax (C-12 pass) without unique per-finding keys (C-15 fail) is a legitimate split score. |
| C-16 | **Finding register pre-seeded before evidence phases** | behavior | aspirational | The brief commits a numbered finding register -- skeleton FID placeholders (e.g., `F1-01`, `F2-01`) -- before any evidence phase executes. Evidence is recorded by filling pre-seeded slots rather than generating identifiers ad-hoc during or after evidence gathering. A brief that creates FIDs at evidence time fails even if all resulting IDs are unique and stable (C-15 may still pass; C-16 requires prior commitment of the finding structure). This is the finding-infrastructure analog of C-13: both require the structural frame to be established before scouting begins. |
| C-17 | **Per-phase Because slot reserved in synthesis template** | format | aspirational | The synthesis section reserves exactly one labeled Because slot per evidence skill-phase in the campaign, with one exception: when C-21 is in effect (Phase 1 is structurally split into Phase 1a and Phase 1b), Phase 1a and Phase 1b each receive a dedicated slot, making the slot count 6 for a standard 5-skill campaign. The template makes C-14 compliance structural: a campaign with five evidence phases and only three synthesis slots creates structural pressure to collapse phases, and cross-phase coverage cannot be guaranteed regardless of analyst intent. Generic synthesis instructions such as "synthesize findings" without enumerated per-phase slots do not pass. Acceptable evidence: a template showing `Because Phase 1 (competitors): ___`, `Because Phase 2 (feasibility): ___`, etc., with slot count = 5 when C-21 is absent, or slot count = 6 when C-21 is in effect. *v7: 6-slot synthesis is correct when C-21 is active; see C-24.* |
| C-18 | **Counter-evidence FID-pinned to qualified finding** | behavior | aspirational | The counter-evidence entry cites the specific finding key it challenges (e.g., "one risk -- cite the FID it qualifies"), making the risk-to-evidence relationship mechanically traceable. C-07 passes when counter-evidence is present; C-18 requires it to reference the finding it undermines. A risk listed without a FID citation passes C-07 and fails C-18. Achievable only in templates that already pass C-15 -- unique finding keys must exist before they can be cited. |
| C-19 | **Hypothesis resolution grounded in finding key** | behavior | aspirational | The hypothesis outcome field explicitly cites the finding key(s) that resolved the prior (e.g., "Confirmed -- resolves F0-01"), making the experimental chain from prior commitment to evidence outcome mechanically traceable. C-08 passes when a disposition label appears; C-19 requires it to name the finding that resolved it. A disposition without a FID citation passes C-08 and fails C-19. As with C-18, a FID system (C-15) is a prerequisite. |
| C-20 | **Phase gate constraints embedded in section headers** | format | aspirational | Phase section headers carry explicit sequential gate constraints (e.g., `[COMPLETE BEFORE PHASE 1]`, `[COMPLETE BEFORE ENTERING PHASE 0]`) as part of the heading label itself. Prose instructions in a preamble or body section that describe ordering do not pass -- the gate must appear at the structural boundary it governs. Acceptable evidence: a heading such as `## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]` or `## FINDING REGISTER [COMPLETE BEFORE ENTERING PHASE 0]`. A template that instructs ordering in a preamble paragraph without annotating the corresponding headers does not pass. |
| C-21 | **Inertia-rivals structural isolation via sub-phase split** | format | aspirational | Phase 1 is divided into Phase 1a (Inertia) and Phase 1b (Rivals) as separate sub-sections, with a gate annotation in the Phase 1a header (e.g., `[COMPLETE BEFORE PHASE 1b]`). The ordering constraint is enforced at the section boundary, not within a shared section via field labels or prose instruction. C-04 passes when inertia content precedes rival content by any means; C-21 requires the separation to be structurally unbreakable -- a filler must complete Phase 1a before Phase 1b is reachable. Templates that enforce inertia-first via row ordering, field labels, or instructions (even correctly) do not pass. Prerequisite: C-20 (the 1a to 1b gate must appear as a header annotation). |
| C-22 | **Phase-prefix + FID dual-axis citation syntax** | correctness | aspirational | Evidence citations in the synthesis Because block carry both a phase prefix and a unique FID key -- as in "because Phase N, F[N]-[seq]". The phase prefix proves campaign position; the FID key proves finding identity. Together they close the strict/liberal scorer ambiguity that exists at C-12: a citation that matches the rubric's example syntax (phase prefix) and satisfies the FID traceability demand (unique key) cannot be disputed by any reasonable scorer. A FID-only citation ("because F3-02") passes C-12 liberal and fails C-22. A Phase+section citation ("because Phase 3, competitors") passes C-12 strict and fails both C-15 and C-22. Prerequisites: C-12 and C-15. |
| C-23 | **Column-header schema enforcement** | format | aspirational | Each evidence phase uses a named-column table where the column headers enumerate the required fields (e.g., `| FID | Dimension | Rating (R/Y/G) | Reason |`). The column structure makes schema compliance verifiable at a glance -- any row that omits a required field creates a visible gap in the column without the reviewer reading row content. Inline labeled rows (which pass C-11) require reading each row to verify schema compliance; table column headers enforce the schema structurally across all rows simultaneously. A template that uses inline row labels without named table column headers passes C-11 and fails C-23. Tables with a two-column `| Field | Value |` layout also fail -- that format carries schema in row-label cells, not column headers. Prerequisite: C-11. |
| C-24 | **Sub-phase synthesis slot alignment** | format | aspirational | When Phase 1 is structurally split into Phase 1a (Inertia) and Phase 1b (Rivals) via C-21, the synthesis Because block carries two separately labeled slots -- one for Phase 1a (inertia evidence) and one for Phase 1b (rivals evidence). A single merged "Phase 1" Because slot paired with an active Phase 1a/1b structural split passes C-17 under the old 5-slot counting and fails C-24: the synthesis collapses the structural separation C-21 enforces in the evidence collection layer, making inertia and rival citations indistinguishable in the synthesis record. The structural principle is consistent: just as C-21 enforces the inertia/rival boundary at evidence-collection time, C-24 enforces it at synthesis time. A template with 6 slots labeled "Because Phase 1a (Inertia): ___", "Because Phase 1b (Rivals): ___", "Because Phase 2: ___", ... passes both C-17 (v7) and C-24. Prerequisites: C-17 and C-21. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)
```

Each aspirational criterion is worth **0.63 pts** (10/16). Sixteen passing = 10.0.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Ready for golden use |
| Silver | >= 60, all essential pass | Usable, recommended gaps noted |
| Bronze | < 60 or any essential fail | Not yet fit for purpose |

---

## Evaluation Notes

- **C-04 (inertia-first)** is the most commonly missed essential criterion. Reviewers should
  check that competitor content opens with status-quo forces, not a named-player list.
- **C-05 (traceability)** should be evaluated by asking: could a reader trace each claim in
  the recommendation back to a specific evidence block? If not, fail.
- **C-08 (hypothesis disposition)** is recommended because prove-hypothesis is a core
  sub-skill; orphaned hypotheses signal a shallow synthesis pass.
- When scoring C-09, "High confidence because we found three independent sources confirming
  X" passes; "High confidence" alone does not.
- **C-11 (per-phase schema)** distinguishes a brief that is structurally enforceable from one
  that relies on the model to self-organize. V-02 hit 100 by construction; V-01 hit 60 despite
  passing all essentials because C-11/C-12 patterns were absent.
- **C-12 (templated citation)** is the difference between "evidence is present somewhere"
  (C-05 pass) and "evidence is pinnable to a specific phase and section." Score C-05 and C-12
  independently: a brief can pass C-05 with prose citations and still fail C-12.
- **C-13 (hypothesis-prior)** requires evidence of temporal commitment -- the hypothesis
  appears before Phase 2+ evidence sections, not just before the synthesis. Look for a Phase 1
  or pre-phase "Hypothesis:" field. A hypothesis restated in synthesis from findings is post-hoc
  regardless of how it is worded.
- **C-14 (cross-phase span)** is scored on the synthesis "Because" block alone. Count distinct
  phase numbers cited. Three citations from Phase 3 count as span = 1, not 3. Minimum passing
  span is 3 distinct phases.
- **C-15 (FID or equivalent)** is format-agnostic: any scheme that produces unique, enumerable
  keys per finding passes. Acceptable: `F1-01`, `C-2`, `finding-market-3`. Not acceptable:
  "the competitor section" or "Phase 3, feasibility." Score C-12 and C-15 independently -- a
  brief using `because Phase 3, competitors section` passes C-12 and fails C-15; a brief using
  `because F3-01` may pass C-15 and face a strict-scorer risk on C-12 (FID differs from the
  rubric's example syntax but satisfies "mechanically auditable").
- **C-16 (finding register pre-seeded)** is C-13's finding-infrastructure analog. The test is
  temporal: does the register appear before Phase 1 (or equivalent) executes? A brief that lists
  all FIDs in a preamble section before any evidence heading passes; one that accumulates FIDs
  inline as findings are recorded fails. Score C-15 and C-16 independently -- a brief can have
  stable, unique FIDs (C-15 pass) generated ad-hoc during evidence recording (C-16 fail).
  Strict interpretation requires individual skeleton placeholder rows with null values (e.g.,
  `F1-01 | -`); liberal interpretation accepts a pre-declared range table (e.g., `F1-01..F1-06`)
  provided it appears before Phase 0.
- **C-17 (per-phase Because slot)** is a template design criterion, not a result criterion.
  Count the labeled synthesis slots and compare to the evidence phase count in the campaign
  spec. If slot count < phase count, fail -- regardless of how many phases the analyst happened
  to cite. *v7 update*: when C-21 is in effect, 6 slots (Phase 1a + Phase 1b + Phases 2-5) is
  the correct slot count; a template with C-21 active that retains a single "Phase 1" slot fails
  C-17 under v7. The distinction from C-14: C-14 is scored on the output; C-17 is scored on the
  template. A brief from a weak template can pass C-14 by chance; a brief from a strong template
  passes C-14 by construction.
- **C-18 (counter-evidence FID-pinned)** upgrades C-07 from presence check to traceability
  check. A risk named without a finding reference is anecdotal; a risk that cites `F3-02`
  allows a reviewer to confirm the finding exists and verify the risk is proportionate. Score
  C-07 and C-18 independently -- C-07 passes when any counter-evidence appears; C-18 requires
  it to carry a FID citation. Templates without a FID system (C-15 fail) cannot pass C-18.
- **C-19 (hypothesis resolution FID-anchored)** upgrades C-08 from disposition label to
  traceable experimental result. "Confirmed" is a claim; "Confirmed -- resolves F0-01" is a
  verifiable claim that a reviewer can check against the finding record. Score C-08 and C-19
  independently -- C-08 passes on label; C-19 requires the FID citation. Templates without a
  FID system (C-15 fail) cannot pass C-19.
- **C-20 (phase gate annotations)** is a template enforcement criterion. Its purpose is to
  make C-13 and C-16 ordering requirements self-enforcing: an analyst filling in sections
  cannot miss a gate that is stamped on the section header. Evaluate by scanning section
  headings for bracketed gate constraints. A template that describes ordering in its preamble
  but leaves section headers unannotated does not pass -- the gate must be co-located with the
  structural boundary it governs.
- **C-21 (inertia structural isolation)** upgrades C-04 from instructed ordering to
  structurally enforced ordering. The test is whether Phase 1 has two distinct sub-sections
  (1a and 1b) with a gate in the 1a header. Field labels, row ordering rules, and prose
  instructions all fail C-21 regardless of whether they produce correct output -- the criterion
  scores the template's structural resistance to violation, not the observed violation rate.
  Score C-04 and C-21 independently: a template with inertia rows correctly positioned before
  rival rows in one section passes C-04 and fails C-21. C-21 also requires C-20 (gate must
  appear in the sub-section header); a 1a/1b split without a gate annotation fails both C-20
  and C-21.
- **C-22 (dual-axis citation)** resolves the C-12 strict/liberal scoring debate at the source.
  The test is whether each synthesis citation contains both a phase token and a FID key. Score
  C-12, C-15, and C-22 as a dependency chain: C-12 can pass without C-15 or C-22 (phase+section
  prose); C-15 can pass without C-22 (FID-only citation); C-22 requires both C-12 and C-15 to
  already be satisfied. A template that achieves C-22 has no residual scoring ambiguity -- every
  reasonable scorer will agree the citation is well-formed.
- **C-23 (column-header schema enforcement)** upgrades C-11 from named-row schema to
  named-column schema. The test is whether each evidence phase uses a Markdown table with
  column headers that enumerate the required fields. Score C-11 and C-23 independently -- a
  template can have correct inline row labels (C-11 pass) without organizing them as table
  columns (C-23 fail). The practical difference: column headers are visible before reading any
  row; row labels require scanning. A reviewer applying C-23 should confirm that column header
  names map directly to required fields and that the column count matches the field count.
  Tables with a `| Field | Value |` two-column layout fail C-23 -- that format uses row content
  (the field-name cell) rather than column headers to convey schema.
- **C-24 (sub-phase synthesis slot alignment)** propagates the C-21 structural split from the
  evidence collection layer to the synthesis layer. The test is whether the synthesis Because
  block has two separately labeled Phase 1 slots (Phase 1a and Phase 1b) when C-21 is in
  effect. Score C-17 and C-24 as a dependency chain: C-17 passes when slot count matches the
  updated v7 rule (6 slots with C-21 active); C-24 additionally requires the two Phase 1 slots
  to be labeled "Phase 1a" and "Phase 1b" rather than an undifferentiated "Phase 1." A template
  with 6 slots labeled "Because Phase 1a (Inertia): ___", "Because Phase 1b (Rivals): ___",
  "Because Phase 2: ___", "Because Phase 3: ___", "Because Phase 4: ___", "Because Phase 5: ___"
  passes both C-17 and C-24. C-24 cannot be satisfied when C-21 is absent -- a campaign without
  a Phase 1a/1b structural split has no synthesis alignment gap to close.
