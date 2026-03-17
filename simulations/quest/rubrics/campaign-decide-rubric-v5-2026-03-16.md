Written to `simulations/quest/rubrics/campaign-decide-rubric-v5-2026-03-16.md`.

---

**Three new criteria added (C-18, C-19, C-20):**

**C-18 — Counter-evidence FID-pinned to qualified finding** (behavior)
C-07 passes when counter-evidence is present. C-18 requires it to cite the specific finding it challenges. Same traceability demand as C-12 applies to recommendations — but for risks. Prerequisite: C-15 (FID system must exist).

**C-19 — Hypothesis resolution grounded in finding key** (behavior)
C-08 passes on disposition label alone. C-19 requires the outcome field to name the specific finding that resolved the prior (e.g., "resolves F0-01"). Upgrades hypothesis closure from assertion to verifiable experimental result. Prerequisite: C-15.

**C-20 — Phase gate constraints embedded in section headers** (format)
C-13 and C-16 require temporal ordering; C-20 requires that ordering constraint to live in the section header itself (`[COMPLETE BEFORE PHASE 1]`), not just in prose preamble. Makes gates machine-readable and impossible to overlook when filling the template.

**Score impact (denominator /9 → /12, each criterion now worth 0.83 pts):**

| Variant | v4 | v5 |
|---------|----|----|
| V-01 | 96.7 | **100.0** (liberal) / 99.2 (strict C-12) |
| V-02 | 96.7 | **95.0** (wider denominator, 0 new passes) |
| V-03 | 98.9–100 | **100.0** (liberal) / 98.3 (strict C-12+C-16) |

V-01 and V-03 now reach 100 by structurally distinct paths; V-02 drops because the denominator widened and it doesn't participate in the FID-system criteria.
, PASS by construction | 6/9 × 10 = 6.67 | 96.7 |
| V-03 (FID system) | PASS — register pre-seeded before evidence phases | PASS if template has per-phase slots | 8–9/9 × 10 = 8.89–10 | 98.9–100 |
| V-04 (named fields + FID) | PASS — register pre-seeded before evidence phases | PASS if template has per-phase slots | 8–9/9 × 10 = 8.89–10 | 98.9–100 |

Note: V-01 and V-02 converge at 96.7 by different paths. V-01 passes C-13 (Phase 0 prior commitment) and fails C-17 (slot count short). V-02 passes C-17 (five slots by construction) and fails C-13 (hypothesis is Phase 4, after three evidence phases). Each variant covers a different structural gap; neither reaches 100 without combining both properties.

---

**Three new criteria extracted from R4:**

**C-18 — Counter-evidence FID-pinned to qualified finding** (behavior)
C-07 is satisfied by any present counter-evidence row. V-01's `F5-05 Counter-evidence: [one risk — cite the FID it qualifies]` adds the next structural layer: the risk must be anchored to the specific finding it challenges. Without a FID citation, counter-evidence is a free-floating assertion. C-18 requires the link to exist as a named key — the same traceability demand C-12 applies to recommendations. Pass C-07 + fail C-18 = risk identified but not grounded in the evidence base. This criterion is only achievable in templates that already pass C-15 (unique finding keys must exist before they can be cited).

**C-19 — Hypothesis resolution grounded in finding key** (behavior)
C-08 is satisfied by a disposition label (Confirmed/Refuted/Inconclusive). V-01's `F5-01 Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]` adds the experimental anchor: the outcome must name the specific finding that resolved the prior. A disposition without a finding reference is an assertion; a disposition with a FID citation is a traceable experimental result. C-19 scores the anchor, not the label. As with C-18, a FID system (C-15) is a prerequisite. Pass C-08 + fail C-19 = hypothesis closed but the resolution chain is opaque.

**C-20 — Phase gate constraints embedded in section headers** (format)
C-13 requires hypothesis-prior anchoring before Phase 1; C-16 requires the finding register to be pre-seeded before Phase 0. Neither criterion specifies *how* the ordering constraint is enforced. V-01 and V-03 both encode the constraint directly in the section header: `## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]`, `## FINDING REGISTER [COMPLETE BEFORE ENTERING PHASE 0]`. A prose preamble that describes ordering does not pass — the gate must appear at the structural boundary it governs, as part of the heading label itself. Phase gate annotations make ordering constraints machine-readable and impossible to overlook when filling the template.

**Score impact (R4):**
- V-01 now passes all three new criteria: 12/12 = **100.0** (liberal), 11/12 = **99.2** (strict C-12)
- V-02 passes none of the three new criteria: 6/12 = **95.0** (down from 96.7 due to wider denominator)
- V-03 passes all three new criteria: 12/12 = **100.0** (liberal), 10/12 = **98.3** (strict C-12 + C-16)
- Denominator: `/9` → `/12`, each aspirational now worth **0.83 pts**

| Variant | C-18 | C-19 | C-20 | Aspirational pts | v5 Composite |
|---------|------|------|------|-----------------|--------------|
| V-01 (full preamble register) | PASS — F5-05 cites the FID it qualifies | PASS — F5-01 resolves by F0-01 reference | PASS — `[COMPLETE BEFORE PHASE 1]` in Phase 0 header | 12/12 × 10 = 10.0 | 100.0 (liberal) / 99.2 (strict C-12) |
| V-02 (hypothesis-first, no FIDs) | FAIL — no FID system, no key to cite | FAIL — no FID system, resolution is label-only | FAIL — no gate annotations in evidence | 6/12 × 10 = 5.0 | 95.0 |
| V-03 (compact range register) | PASS — F5-05 cites FID qualifier | PASS — F5-01 resolves F0-01 | PASS — `[COMPLETE BEFORE PHASE 1]` in Phase 0 header | 12/12 × 10 = 10.0 | 100.0 (liberal) / 98.3 (strict C-12 + C-16) |

Note: V-01 achieves 100 via the full-preamble skeleton register (C-16 strict PASS). V-03 achieves 100 only under liberal C-16 interpretation; under strict reading its CAMPAIGN REGISTER uses range notation rather than individual skeleton placeholders. The paths to 100 are structurally distinct: V-01 wins on register granularity, V-03 on compact pre-declaration.

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
| C-18 | **Counter-evidence FID-pinned to qualified finding** | behavior | aspirational | The counter-evidence entry cites the specific finding key it challenges (e.g., "one risk — cite the FID it qualifies"), making the risk-to-evidence relationship mechanically traceable. C-07 passes when counter-evidence is present; C-18 requires it to reference the finding it undermines. A risk listed without a FID citation passes C-07 and fails C-18. Achievable only in templates that already pass C-15 — unique finding keys must exist before they can be cited. |
| C-19 | **Hypothesis resolution grounded in finding key** | behavior | aspirational | The hypothesis outcome field explicitly cites the finding key(s) that resolved the prior (e.g., "Confirmed — resolves F0-01"), making the experimental chain from prior commitment to evidence outcome mechanically traceable. C-08 passes when a disposition label appears; C-19 requires it to name the finding that resolved it. A disposition without a FID citation passes C-08 and fails C-19. As with C-18, a FID system (C-15) is a prerequisite. |
| C-20 | **Phase gate constraints embedded in section headers** | format | aspirational | Phase section headers carry explicit sequential gate constraints (e.g., `[COMPLETE BEFORE PHASE 1]`, `[COMPLETE BEFORE ENTERING PHASE 0]`) as part of the heading label itself. Prose instructions in a preamble or body section that describe ordering do not pass — the gate must appear at the structural boundary it governs. Acceptable evidence: a heading such as `## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]` or `## FINDING REGISTER [COMPLETE BEFORE ENTERING PHASE 0]`. A template that instructs ordering in a preamble paragraph without annotating the corresponding headers does not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

Each aspirational criterion is worth **0.83 pts** (10/12). Twelve passing = 10.0.

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
  Strict interpretation requires individual skeleton placeholder rows with null values (e.g.,
  `F1-01 | —`); liberal interpretation accepts a pre-declared range table (e.g., `F1-01..F1-06`)
  provided it appears before Phase 0.
- **C-17 (per-phase Because slot)** is a template design criterion, not a result criterion.
  Count the labeled synthesis slots and compare to the evidence phase count in the campaign
  spec. If slot count < phase count, fail — regardless of how many phases the analyst happened
  to cite. The distinction from C-14: C-14 is scored on the output; C-17 is scored on the
  template. A brief from a weak template can pass C-14 by chance; a brief from a strong
  template passes C-14 by construction.
- **C-18 (counter-evidence FID-pinned)** upgrades C-07 from presence check to traceability
  check. A risk named without a finding reference is anecdotal; a risk that cites `F3-02`
  allows a reviewer to confirm the finding exists and verify the risk is proportionate. Score
  C-07 and C-18 independently — C-07 passes when any counter-evidence appears; C-18 requires
  it to carry a FID citation. Templates without a FID system (C-15 fail) cannot pass C-18.
- **C-19 (hypothesis resolution FID-anchored)** upgrades C-08 from disposition label to
  traceable experimental result. "Confirmed" is a claim; "Confirmed — resolves F0-01" is a
  verifiable claim that a reviewer can check against the finding record. Score C-08 and C-19
  independently — C-08 passes on label; C-19 requires the FID citation. Templates without a
  FID system (C-15 fail) cannot pass C-19.
- **C-20 (phase gate annotations)** is a template enforcement criterion. Its purpose is to
  make C-13 and C-16 ordering requirements self-enforcing: an analyst filling in sections
  cannot miss a gate that is stamped on the section header. Evaluate by scanning section
  headings for bracketed gate constraints. A template that describes ordering in its preamble
  but leaves section headers unannotated does not pass — the gate must be co-located with the
  structural boundary it governs.
