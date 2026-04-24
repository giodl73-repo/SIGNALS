Written to `simulations/quest/rubrics/campaign-decide-rubric-v4-2026-03-16.md`.

**Two new criteria extracted from R3:**

**C-16 — Finding register pre-seeded** (behavior)
V-03's "pre-assigned FIDs" axis exposes the gap: C-15 only checks that FIDs exist and are unique — it says nothing about *when* they were committed. Pre-assignment means the register is populated (skeleton placeholders) before any evidence phase runs, not accumulated inline. Pass C-15 + fail C-16 = FIDs generated ad-hoc. This is exactly C-13's logic applied to the finding infrastructure.

**C-17 — Per-phase Because slot in synthesis template** (format)
V-01 vs V-02 split the C-14 signal. V-01 has four Because slots for five evidence phases — it passed C-14 because the analyst cited 3+ phases by choice. V-02 has five slots for five phases — C-14 is "PASS by template construction." C-17 scores the template, not the output: slot count must equal phase count, or the guarantee doesn't exist.

**Score impact:**
- V-01 and V-02 converge at **96.7** by different paths (V-01: passes C-13, fails C-17; V-02: passes C-17, fails C-13)
- V-03/V-04 range: **98.9–100** (limited only by C-13 hypothesis timing)
- Denominator: `/7` → `/9`, each aspirational now worth 1.11 pts
riant | C-16 | C-17 | Aspirational pts | v4 Composite |
|---------|------|------|-----------------|--------------|
| V-01 (named-field schema) | FAIL — no FID system | FAIL — 4 slots for 5 evidence phases | 6/9 × 10 = 6.67 | 96.7 |
| V-02 (hypothesis-first) | FAIL — no FID system | PASS — 5 labeled slots for 5 evidence phases, PASS by construction | 6/9 × 10 = 6.67 | 96.7 |
| V-03 (FID system) | PASS — register pre-seeded before evidence phases | PASS if template has per-phase slots | 8–9/9 × 10 = 8.89–10 | 98.9–100 |
| V-04 (named fields + FID) | PASS — register pre-seeded before evidence phases | PASS if template has per-phase slots | 8–9/9 × 10 = 8.89–10 | 98.9–100 |

Note: V-01 and V-02 converge at 96.7 by different paths. V-01 passes C-13 (Phase 0 prior commitment) and fails C-17 (slot count short). V-02 passes C-17 (five slots by construction) and fails C-13 (hypothesis is Phase 4, after three evidence phases). Each variant covers a different structural gap; neither reaches 100 without combining both properties.

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
| C-16 | **Finding register pre-seeded before evidence phases** | behavior | aspirational | The brief commits a numbered finding register — skeleton FID placeholders (e.g., `F1-01`, `F2-01`) — before any evidence phase executes. Evidence is recorded by filling pre-seeded slots rather than generating identifiers ad-hoc during or after evidence gathering. A brief that creates FIDs at evidence time fails even if all resulting IDs are unique and stable (C-15 may still pass; C-16 requires prior commitment of the finding structure). This is the finding-infrastructure analog of C-13: both require the structural frame to be established before scouting begins. |
| C-17 | **Per-phase Because slot reserved in synthesis template** | format | aspirational | The synthesis section reserves exactly one labeled Because slot per evidence phase in the campaign. The template makes C-14 compliance structural: a campaign with five evidence phases and only three synthesis slots creates structural pressure to collapse phases, and cross-phase coverage cannot be guaranteed regardless of analyst intent. Generic synthesis instructions such as "synthesize findings" without enumerated per-phase slots do not pass. Acceptable evidence: a template showing `Because Phase 1 (competitors): ___`, `Because Phase 2 (feasibility): ___`, etc., with slot count matching phase count. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)
```

Each aspirational criterion is worth **1.11 pts** (10/9). Nine passing = 10.0.

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
- **C-16 (finding register pre-seeded)** is C-13's finding-infrastructure analog. The test is
  temporal: does the register appear before Phase 1 (or equivalent) executes? A brief that lists
  all FIDs in a preamble section before any evidence heading passes; one that accumulates FIDs
  inline as findings are recorded fails. Score C-15 and C-16 independently — a brief can have
  stable, unique FIDs (C-15 pass) generated ad-hoc during evidence recording (C-16 fail).
- **C-17 (per-phase Because slot)** is a template design criterion, not a result criterion.
  Count the labeled synthesis slots and compare to the evidence phase count in the campaign
  spec. If slot count < phase count, fail — regardless of how many phases the analyst happened
  to cite. The distinction from C-14: C-14 is scored on the output; C-17 is scored on the
  template. A brief from a weak template can pass C-14 by chance; a brief from a strong
  template passes C-14 by construction.
