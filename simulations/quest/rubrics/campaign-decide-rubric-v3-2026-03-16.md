Written to `simulations/quest/rubrics/campaign-decide-rubric-v3-2026-03-16.md`.

---

**What changed from v2:**

Three new aspirational criteria, denominator moves from `/4` to `/7`:

| ID | Criterion | Source | Independence from existing criteria |
|----|-----------|--------|-------------------------------------|
| C-13 | **Hypothesis-prior anchoring** | V-02 C-08 PASS+ | C-08 checks disposition exists. C-13 checks *when* the hypothesis was committed. Pass C-08 + fail C-13 = disposition present but stated post-hoc. |
| C-14 | **Cross-phase citation span** | V-04 C-05 | C-05 checks traceability exists. C-14 checks breadth (≥3 distinct phases cited). Pass C-05 + fail C-14 = all citations from one phase. |
| C-15 | **Per-finding unique citation keys** | V-03/V-04 FID system | C-12 checks citation format is templated. C-15 checks each finding has a unique enumerable key. Pass C-12 + fail C-15 = phase+section format without per-finding IDs. |

**R2 re-scores:** All four variants remain Gold under v3, but score compression surfaces: V-01 drops to ~95.7, V-02 to ~97.1, V-03/V-04 to 98.6–100 depending on whether the hypothesis appears in Phase 1 vs. later.
 FID system | C-12 checks that citation syntax is templated and mechanically auditable. It does not require unique per-finding identifiers. V-03 and V-04 introduced FIDs (e.g., `F1-01`, `F2-03`) that survive reordering and allow pinning to a specific finding without phase+section prose lookup. A brief can pass C-12 with `because Phase 3, competitors section` and still fail C-15 (no unique finding key). |

**Scoring formula update:** aspirational denominator moves from `/4` to `/7`. Max composite stays 100.

**R2 re-scores under v3:**

| Variant | C-13 | C-14 | C-15 | Aspirational pts | v3 Composite |
|---------|------|------|------|-----------------|--------------|
| V-01 (named-field schema) | FAIL — no Phase-1 hypothesis commit | PASS — Phase 6 requires multi-phase cite | FAIL — no FID | 4/7 × 10 = 5.7 | 95.7 |
| V-02 (hypothesis-first) | PASS — hypothesis is Phase 1 anchor | PASS — multi-phase cite | FAIL — no FID | 5/7 × 10 = 7.1 | 97.1 |
| V-03 (FID system) | PASS if hypothesis in Phase 1 | PASS — FID citations span phases | PASS — FID throughout | 6–7/7 × 10 = 8.6–10 | 98.6–100 |
| V-04 (named fields + FID) | PASS if hypothesis in Phase 1 | PASS — explicit 3-phase span required | PASS — FID throughout | 6–7/7 × 10 = 8.6–10 | 98.6–100 |

---

## Essential Criteria (60 pts total — output must pass all five)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Recommendation stated** | correctness | essential | Output includes an explicit, labeled build/no-build (commit/pause/pivot/abandon) recommendation. Absence of a stated recommendation is an automatic fail. |
| C-02 | **Confidence level stated** | correctness | essential | Recommendation is accompanied by a stated confidence (e.g., High/Medium/Low or a numeric percentage). A recommendation without confidence is incomplete. |
| C-03 | **All six sub-skill domains represented** | coverage | essential | Output contains distinct sections or evidence blocks attributable to each of the six orchestrated skills: competitors, feasibility, market, hypothesis, web-search evidence, and synthesis. Missing any domain means the campaign is incomplete. |
| C-04 | **Inertia-first competitor framing** | correctness | essential | The competitor analysis leads with incumbent/inertia forces (status-quo cost, switching cost, or "why people don't change") before listing named rivals. The orchestration spec requires this ordering. |
| C-05 | **Evidence-to-recommendation traceability** | correctness | essential | The recommendation is visibly grounded in evidence from the brief (citations, section references, or explicit "because" statements). A recommendation that floats free of its evidence base fails. |

---

## Recommended Criteria (30 pts total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Structured decision brief format** | format | recommended | Output uses a consistent document structure: titled sections, a summary block, and a clear recommendation block. Prose-only dumps without section hierarchy do not pass. |
| C-07 | **Risk and counter-evidence acknowledged** | depth | recommended | Brief surfaces at least one risk, caveat, or piece of counter-evidence that could undermine the recommendation. A one-sided brief fails this criterion. |
| C-08 | **Hypothesis disposition explicit** | depth | recommended | Each hypothesis entered into prove-hypothesis has an explicit outcome (confirmed / refuted / inconclusive). Hypotheses that disappear without resolution fail this criterion. |

---

## Aspirational Criteria (10 pts total — raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Confidence calibration narrative** | depth | aspirational | Brief explains *why* confidence is rated as it is — naming the specific evidence gaps or strength factors that drove the rating, not just asserting a level. |
| C-10 | **Actionable next steps conditioned on recommendation** | behavior | aspirational | If build: output includes a concrete next step (e.g., scope spike, prototype). If no-build: output includes an exit condition or revisit trigger. Generic "further research needed" does not pass. |
| C-11 | **Per-phase required-field schema** | format | aspirational | Each evidence phase has its own structured schema with required named rows (not just an overall summary block). The brief is verifiable at the phase level. A single recommendation block with no per-phase field structure does not pass. |
| C-12 | **Templated citation syntax in recommendation** | correctness | aspirational | The recommendation's evidence citations follow a prescribed format (e.g., "because Phase [N], [section reference]"), making traceability mechanically auditable at a glance. Free-prose citations such as "as shown above" or "based on the evidence" do not pass. |
| C-13 | **Hypothesis-prior anchoring** | behavior | aspirational | The hypothesis is committed as an explicit prior belief before any evidence phase executes (Phase 1 or equivalent). Synthesis then reports whether evidence confirmed, refuted, or left the hypothesis inconclusive — as a genuine experimental outcome. A hypothesis first stated in the synthesis phase, or inferred post-hoc from findings, does not pass. |
| C-14 | **Cross-phase citation span in synthesis** | correctness | aspirational | The synthesis "Because" block includes citations drawn from at least 3 distinct evidence phases. Ensures the recommendation integrates the full campaign breadth. A recommendation whose citations all come from one or two phases does not pass, even if those citations are otherwise well-formed (C-05 and C-12 may still pass). |
| C-15 | **Per-finding unique citation keys** | format | aspirational | Each finding is assigned a unique, enumerable identifier (e.g., `F1-01`, `F2-03`, or equivalent scheme) that makes individual citations pinnable without phase+section prose lookup. The key must be stable across sections — reordering findings should not break citation references. Phase+section templated syntax (C-12 pass) without unique per-finding keys (C-15 fail) is a legitimate split score. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

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
- **C-13 (hypothesis-prior)** requires evidence of temporal commitment — the hypothesis
  appears before Phase 2+ evidence sections, not just before the synthesis. Look for a Phase 1
  or pre-phase "Hypothesis:" field. A hypothesis restated in synthesis from findings is post-hoc
  regardless of how it is worded.
- **C-14 (cross-phase span)** is scored on the synthesis "Because" block alone. Count distinct
  phase numbers cited. Three citations from Phase 3 count as span = 1, not 3. Minimum passing
  span is 3 distinct phases.
- **C-15 (FID or equivalent)** is format-agnostic: any scheme that produces unique, enumerable
  keys per finding passes. Acceptable: `F1-01`, `C-2`, `finding-market-3`. Not acceptable:
  "the competitor section" or "Phase 3, feasibility." Score C-12 and C-15 independently — a
  brief using `because Phase 3, competitors section` passes C-12 and fails C-15; a brief using
  `because F3-01` may pass C-15 and face a strict-scorer risk on C-12 (FID differs from the
  rubric's example syntax but satisfies "mechanically auditable").
