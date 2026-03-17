---
skill: quest-variate
skill_target: campaign-decide
round: 5
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v5-2026-03-16.md
---

# Variations — campaign-decide / Round 5

Five complete, runnable skill body variations targeting the v5 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R4 → R5 diagnosis:**

The v5 rubric added three new aspirational criteria (C-18, C-19, C-20) and expanded
the denominator from /9 to /12. R4's best variants (V-01, V-04, V-05) already
contained the structural elements that pass all three new criteria:

| R4 variation | v5 C-18 | v5 C-19 | v5 C-20 | v5 composite |
|--------------|---------|---------|---------|--------------|
| V-01 (full preamble register + Phase 0) | PASS — F5-05 cites FID | PASS — F5-01 resolves F0-01 | PASS — gate in Phase 0 header | 100.0 liberal / 99.2 strict C-12 |
| V-02 (table format, no FIDs, Phase 4 hyp.) | FAIL — no FID system | FAIL — no FID system | FAIL — no gate annotations | 95.0 |
| V-03 (compact range register, Phase 0) | PASS | PASS | PASS | 100.0 liberal / 98.3 strict |
| V-04 (full preamble + formula) | PASS | PASS | PASS | 100.0 liberal / 99.2 strict C-12 |
| V-05 (V-04 conversational) | PASS | PASS | PASS | 100.0 liberal / 99.2 strict C-12 |

**The only remaining scoring risk across all 12 criteria**: C-12 strict interpretation.

The rubric defines C-12 as requiring "mechanically auditable at a glance" citations in
the Because block. The rubric example is "because Phase [N], [section reference]"; R4's
FID-based variants used "because F[N]-[seq]" — FID satisfies "mechanically auditable"
but the Phase prefix is absent. All scorers agree FID passes; strict scorers may require
the Phase token. The ambiguity is low-to-moderate probability but eliminates the
12/12 certainty claim.

**R5 axes:**

| Axis | Criterion targeted | Mechanism |
|------|--------------------|-----------|
| C-12 hybrid citation | C-12 strict, unambiguous | "because Phase N, F[N]-[seq]" — both Phase prefix AND FID key, satisfies rubric example format AND FID scheme simultaneously |
| Inertia elevation | C-04 structural | Phase 1 split into Phase 1a (Inertia) gated before Phase 1b (Named Rivals) at the sub-section level, not just field ordering |
| C-20 graft on non-FID template | C-20 isolation | Take R4 V-02 (no FID system) and add gate annotations to all headers — tests whether C-20 is achievable without C-15 and what its marginal value is |

Single-axis: V-01 (C-12 hybrid citation), V-02 (inertia elevation), V-03 (C-20 graft
on non-FID template). Combined: V-04 (C-12 hybrid + inertia elevation), V-05 (V-04
with conversational phrasing register).

---

## V-01 — Axis: C-12 hybrid citation format ("Phase N, F[N]-[seq]")

**Hypothesis**: The one remaining ambiguity in R4's 100-target variants is the C-12
citation format. The rubric example is "because Phase [N], [section reference]"; R4's
FID variants used "because F0-[seq]" — no Phase prefix. A hybrid format "because Phase
0, F0-[seq]" satisfies both simultaneously: the Phase token matches the rubric example;
the FID key makes it mechanically auditable without phase-section prose lookup. If C-12
passes under both liberal AND strict scoring, the composite is unambiguously 12/12 = 100.

Base: R4 V-01 (full preamble register, Phase 0 gate, 5-slot synthesis).
Single-axis change: Because block citation format only.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by FID in synthesis.
Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | —     |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | —     |
| F0-03 | Phase 0 (prior)    | Confidence prior     | —     |
| F0-04 | Phase 0 (prior)    | Prior rationale      | —     |
| F0-05 | Phase 0 (prior)    | Experiment 1         | —     |
| F0-06 | Phase 0 (prior)    | Experiment 2         | —     |
| F1-01 | Phase 1 (rivals)   | Status-quo inertia   | —     |
| F1-02 | Phase 1 (rivals)   | Switching cost       | —     |
| F1-03 | Phase 1 (rivals)   | Good-enough thresh.  | —     |
| F1-04 | Phase 1 (rivals)   | Rival A              | —     |
| F1-05 | Phase 1 (rivals)   | Rival B              | —     |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | —     |
| F2-02 | Phase 2 (feasib.)  | Team capability      | —     |
| F2-03 | Phase 2 (feasib.)  | Timeline             | —     |
| F2-04 | Phase 2 (feasib.)  | Cost                 | —     |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | —     |
| F2-06 | Phase 2 (feasib.)  | Top risk             | —     |
| F3-01 | Phase 3 (market)   | Addressable market   | —     |
| F3-02 | Phase 3 (market)   | Segment 1            | —     |
| F3-03 | Phase 3 (market)   | Segment 2            | —     |
| F3-04 | Phase 3 (market)   | Primary segment      | —     |
| F4-01 | Phase 4 (web)      | Source 1             | —     |
| F4-02 | Phase 4 (web)      | Source 2             | —     |
| F4-03 | Phase 4 (web)      | Source 3             | —     |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | —     |
| F5-02 | Phase 5 (synth)    | Recommendation       | —     |
| F5-03 | Phase 5 (synth)    | Confidence           | —     |
| F5-04 | Phase 5 (synth)    | Confidence rationale | —     |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | —     |
| F5-06 | Phase 5 (synth)    | Next step            | —     |

---

## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]
F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

Ordering rule: F1-01 through F1-03 (inertia) must be populated before F1-04+ (rivals).

---

## Phase 2 — scout-feasibility

F2-01  Technical complexity: [R/Y/G] — [reason]
F2-02  Team capability: [R/Y/G] — [reason]
F2-03  Timeline: [R/Y/G] — [reason]
F2-04  Cost: [R/Y/G] — [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 — prove-websearch

F4-01  Source: [URL or citation]
       Quote: "[direct quote — not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 — prove-synthesize

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per evidence phase — exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting:**
- C-01: F5-02 recommendation field — labeled, required
- C-02: F5-03 confidence field — labeled, required
- C-03: All six domains — Phase 0 (prove-hypothesis), Phase 1 (competitors), Phase 2 (feasibility), Phase 3 (market), Phase 4 (websearch), Phase 5 (synthesize)
- C-04: F1-01–F1-03 ordering rule — inertia before rivals by field position
- C-05: Because block with five phase+FID citations
- C-06: Section headers per phase + labeled field rows
- C-07: F5-05 counter-evidence with required FID reference
- C-08: F5-01 hypothesis outcome — resolves F0-01
- C-09: F5-04 confidence rationale cites FIDs
- C-10: F5-06 conditioned next step
- C-11: FID-labeled required rows per phase = per-phase required-field schema
- **C-12: "because Phase N, F[N]-[seq]" — Phase prefix satisfies rubric example; FID key satisfies mechanical auditability. No residual strict-scorer risk.**
- C-13: Phase 0 precedes all evidence phases by document position
- C-14: Five labeled phase slots guarantee 5 distinct phases
- C-15: FINDING REGISTER pre-assigns all FIDs — PASS by construction
- C-16: Standalone FINDING REGISTER before Phase 0 with "—" skeleton rows — PASS strict and liberal
- C-17: Exactly 5 labeled Because slots for 5 evidence phases
- C-18: F5-05 cites the FID it qualifies — PASS
- C-19: F5-01 resolves F0-01 by FID reference — PASS
- C-20: `[COMPLETE BEFORE PHASE 1]` in Phase 0 header; `[COMPLETE BEFORE PHASE 0]` in FINDING REGISTER header — PASS

**C-12 hybrid rationale**: "because Phase 0, F0-[seq]" contains both tokens. The Phase token satisfies the rubric's stated example format "because Phase [N], [section reference]". The FID token (F0-[seq]) replaces the prose section reference with a unique key that is mechanically auditable without positional lookup. A strict scorer who requires the Phase prefix cannot fail this; a liberal scorer who accepts FID alone cannot fail this either.

**Predicted v5 score**: 12/12 aspirational → composite **100.0** (no remaining strict-scorer risk).
Difference from R4 V-01: C-12 strict risk eliminated. All other criteria: identical.

---

## V-02 — Axis: Inertia elevation (Phase 1a/1b sub-section structure)

**Hypothesis**: In R4 variants, C-04 inertia-first enforcement lived in a prose rule
("F1-01 through F1-03 must be populated before F1-04+") and field ordering. The
structural guarantee is field-position — a model filling the template can still skip
to F1-04 if it misreads the instruction. Splitting Phase 1 into a gated sub-section
pair — Phase 1a (Inertia) with its own completion gate before Phase 1b (Named Rivals) —
makes C-04 compliant at the section boundary, not just the field boundary. C-20 bonus:
the Phase 1a gate annotation (`[COMPLETE BEFORE PHASE 1b]`) adds a second gate in the
template, reinforcing the pattern. Single axis: only Phase 1 structure changes from
R4 V-01.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by FID in synthesis.
Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | —     |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | —     |
| F0-03 | Phase 0 (prior)    | Confidence prior     | —     |
| F0-04 | Phase 0 (prior)    | Prior rationale      | —     |
| F0-05 | Phase 0 (prior)    | Experiment 1         | —     |
| F0-06 | Phase 0 (prior)    | Experiment 2         | —     |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | —     |
| F1-02 | Phase 1a (inertia) | Switching cost       | —     |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | —     |
| F1-04 | Phase 1b (rivals)  | Rival A              | —     |
| F1-05 | Phase 1b (rivals)  | Rival B              | —     |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | —     |
| F2-02 | Phase 2 (feasib.)  | Team capability      | —     |
| F2-03 | Phase 2 (feasib.)  | Timeline             | —     |
| F2-04 | Phase 2 (feasib.)  | Cost                 | —     |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | —     |
| F2-06 | Phase 2 (feasib.)  | Top risk             | —     |
| F3-01 | Phase 3 (market)   | Addressable market   | —     |
| F3-02 | Phase 3 (market)   | Segment 1            | —     |
| F3-03 | Phase 3 (market)   | Segment 2            | —     |
| F3-04 | Phase 3 (market)   | Primary segment      | —     |
| F4-01 | Phase 4 (web)      | Source 1             | —     |
| F4-02 | Phase 4 (web)      | Source 2             | —     |
| F4-03 | Phase 4 (web)      | Source 3             | —     |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | —     |
| F5-02 | Phase 5 (synth)    | Recommendation       | —     |
| F5-03 | Phase 5 (synth)    | Confidence           | —     |
| F5-04 | Phase 5 (synth)    | Confidence rationale | —     |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | —     |
| F5-06 | Phase 5 (synth)    | Next step            | —     |

---

## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

### Phase 1a — Inertia Analysis [COMPLETE BEFORE PHASE 1b]

Why do people not change? Answer inertia before naming any rival. A competitor analysis
that opens with product names skips the primary barrier to adoption.

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b — Named Rivals

F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

---

## Phase 2 — scout-feasibility

F2-01  Technical complexity: [R/Y/G] — [reason]
F2-02  Team capability: [R/Y/G] — [reason]
F2-03  Timeline: [R/Y/G] — [reason]
F2-04  Cost: [R/Y/G] — [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 — prove-websearch

F4-01  Source: [URL or citation]
       Quote: "[direct quote — not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 — prove-synthesize

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one FID per evidence phase — exactly 5 slots):
- PRIOR (Phase 0): [claim] because F0-[seq]
- COMPETITORS (Phase 1): [claim] because F1-[seq]
- FEASIBILITY (Phase 2): [claim] because F2-[seq]
- MARKET (Phase 3): [claim] because F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting:**
- C-04: Phase 1a (Inertia) is a complete section with its own header gated before Phase 1b (Named Rivals). C-04 pass is structural at the section level — even if a model fills Phase 1b first, the document structure names the inertia sub-section first. Stronger than field-ordering instruction alone.
- All other criteria: identical to R4 V-01. FINDING REGISTER pre-seeds FIDs; Phase 0 gate; five synthesis slots.
- C-20: Three gate annotations now present: FINDING REGISTER header, Phase 0 header, Phase 1a header (`[COMPLETE BEFORE PHASE 1b]`). Reinforced pattern.
- C-12: Same FID-only format risk as R4 V-01 (low-to-moderate). Citation is `because F[N]-[seq]` not `because Phase N, F[N]-[seq]`.

**FINDING REGISTER note**: Phase 1a and 1b are sub-sections of Phase 1. The register uses
"Phase 1a (inertia)" and "Phase 1b (rivals)" to reflect the sub-structure. The Because
block still cites Phase 1 (not 1a/1b) since the synthesis slot covers the full Phase 1
finding set. This avoids a C-17 slot-count mismatch (still 5 phases = 5 slots).

**Predicted v5 score**: 12/12 aspirational → composite **100.0** (liberal) / **99.2** (strict C-12).
C-04 is now section-structurally enforced. Single axis from R4 V-01 is Phase 1 structure.

---

## V-03 — Axis: C-20 graft on non-FID template (boundary test)

**Hypothesis**: C-20 (phase gate constraints embedded in section headers) does not
require a FID system. It is a formatting criterion that measures whether ordering
constraints are co-located with the structural boundaries they govern. R4 V-02 (table
format, no FIDs, hypothesis Phase 4) scored 95.0 at v5 — it failed C-20 because no
gate annotations appeared in its headers. Adding `[COMPLETE BEFORE PHASE N]` to each
section header satisfies C-20's pass condition ("the gate must appear at the structural
boundary it governs, as part of the heading label itself") independently of the FID
system. If this passes, C-20 is achievable without C-15 and the marginal value of
adding C-20 alone to a non-FID template is exactly 0.83 pts (one additional aspirational
criterion). The variant also tests: do gates that do not enforce hypothesis-prior ordering
still pass C-20?

Base: R4 V-02 (table-per-phase, no FIDs, hypothesis Phase 4, C-17 formula declared).
Single-axis change: add `[COMPLETE BEFORE PHASE N]` to all section headers.

```
Run the full pre-commitment decision campaign for: {{topic}}

CAMPAIGN PHASE MAP (5 evidence phases — in order):
  1. competitors — scout-competitors
  2. feasibility — scout-feasibility
  3. market      — scout-market
  4. hypothesis  — prove-hypothesis
  5. web-search  — prove-websearch

SYNTHESIS RULE: The Because block must contain exactly one labeled slot per phase in
the campaign phase map above. SLOT COUNT (5) = PHASE COUNT (5). A synthesis block
with fewer than 5 labeled phase slots means at least one phase is absent from the
recommendation's evidence base — regardless of how many citations appear in the slots
that do exist.

---

## Phase 1 — scout-competitors [COMPLETE BEFORE PHASE 2]

| Force | Type | Strength (1-5) | Notes |
|-------|------|----------------|-------|
| Status-quo inertia | inertia | | Why people don't change |
| Switching cost | inertia | | What users lose by moving to any alternative |
| Good-enough threshold | inertia | | When current approach feels acceptable |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must precede named rival rows.)

---

## Phase 2 — scout-feasibility [COMPLETE BEFORE PHASE 3]

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market [COMPLETE BEFORE PHASE 4]

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |
| | | | |

Primary target segment: [name] — [justification]

---

## Phase 4 — prove-hypothesis [COMPLETE BEFORE PHASE 5]

| Field | Value |
|-------|-------|
| Claim | [one falsifiable sentence — what must be true for this to be worth building] |
| Falsification condition | [what evidence would disprove this claim] |
| Confidence prior | [Low / Medium / High] |
| Prior rationale | [reason before seeing external evidence] |
| Experiment 1 | [name and method] |
| Experiment 2 | [name and method] |

---

## Phase 5 — prove-websearch [COMPLETE BEFORE PHASE 6]

| Source | Direct Quote | Strength | Verdict |
|--------|--------------|----------|---------|
| | "[direct quote]" | Weak / Moderate / Strong | Supports / Refutes / Neutral |
| | "[direct quote]" | | |
| | "[direct quote]" | | |

(Minimum 3 sources.)

---

## Phase 6 — prove-synthesize

| Field | Value |
|-------|-------|
| Hypothesis outcome | [Confirmed / Refuted / Inconclusive] |
| Recommendation | [COMMIT / PAUSE / PIVOT / ABANDON] |
| Confidence | [High / Medium / Low] |
| Confidence rationale | [name specific evidence gaps or strengths — not just the label] |
| Counter-evidence | [one risk or caveat that could undermine the recommendation] |
| Next step | [COMMIT: concrete action | no-build: exit condition or revisit trigger] |

Because (exactly 5 slots — slot count = phase count = 5, one per phase in the campaign
phase map, no slot may be omitted or merged with another):
- PHASE 1 (competitors): [claim] because Phase 1, [force row]
- PHASE 2 (feasibility): [claim] because Phase 2, [dimension row]
- PHASE 3 (market): [claim] because Phase 3, [segment finding]
- PHASE 4 (hypothesis): [claim] because Phase 4, [hypothesis field]
- PHASE 5 (web-search): [claim] because Phase 5, [source citation]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting:**
- C-01/C-02: Recommendation + confidence table rows
- C-03: Phases 1–6 cover all six sub-skills
- C-04: Inertia rows before named rivals by table structure
- C-05: Because block with five Phase+field citations
- C-06: Section headers + table per phase
- C-07: Counter-evidence table row
- C-08: Hypothesis outcome row
- C-09: Confidence rationale row (strength factors required)
- C-10: Conditioned next step row
- C-11: Table schema per phase = per-phase required-field schema
- C-12: "because Phase N, [row reference]" — exact rubric example format. PASS.
- C-13: FAIL — hypothesis is Phase 4, after three scouting phases
- C-14: PASS — 5 labeled phase slots require 5 distinct phases
- C-15: FAIL — no FID system
- C-16: FAIL — no FID system, no register
- C-17: PASS — "SLOT COUNT (5) = PHASE COUNT (5)" formula declared
- C-18: FAIL — no FID system (prerequisite C-15 absent)
- C-19: FAIL — no FID system (prerequisite C-15 absent)
- **C-20: PASS — gate annotations present in all five evidence phase headers. The gates (`[COMPLETE BEFORE PHASE N]`) are co-located with each section boundary as required. Note: the gates sequence phases 1→2→3→4→5 but do not enforce hypothesis-prior ordering (C-13 fails independently). C-20 is a structural format criterion, not an ordering correctness criterion.**

**C-20 boundary test result**: C-20 passes even though the template fails C-13. The criterion
measures whether gate constraints are in section headers — not whether the gates enforce the
right order. A template can have C-20 PASS + C-13 FAIL simultaneously. This confirms C-20
is a mechanical enforcement criterion separable from the hypothesis-prior correctness C-13
measures.

**Marginal value of C-20 graft**: R4 V-02 at v5 scored 6/12 = 95.0. Adding C-20 gives 7/12 = 95.83.
A gain of 0.83 pts. Compared to adding the full FID system (C-15, C-16, C-18, C-19 = 4 criteria
= 3.33 pts, reaching 10/12 = 98.33), the graft is low-yield. The FID system's value is additive:
it enables C-15, which unlocks C-16, C-18, and C-19 as achievable.

**Predicted v5 score**: 7/12 aspirational → composite **95.83**.

---

## V-04 — Combined: C-12 hybrid citation + Phase 1a/1b inertia elevation

**Hypothesis**: V-01 closes the C-12 strict-scorer risk; V-02 elevates C-04 to section
level enforcement. Combining both axes on the R4 V-01 base produces a template with
zero remaining scoring ambiguity and a structurally stronger C-04 guarantee. The
expected score is 12/12 = 100.0 with no residual risks under any interpreter.

Changes from R4 V-01:
1. Because block citation format: `because Phase N, F[N]-[seq]` (V-01 axis)
2. Phase 1 structure: Phase 1a (Inertia) gated before Phase 1b (Rivals) (V-02 axis)
3. FINDING REGISTER Phase column reflects 1a/1b sub-structure

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by FID in synthesis.
Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | —     |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | —     |
| F0-03 | Phase 0 (prior)    | Confidence prior     | —     |
| F0-04 | Phase 0 (prior)    | Prior rationale      | —     |
| F0-05 | Phase 0 (prior)    | Experiment 1         | —     |
| F0-06 | Phase 0 (prior)    | Experiment 2         | —     |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | —     |
| F1-02 | Phase 1a (inertia) | Switching cost       | —     |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | —     |
| F1-04 | Phase 1b (rivals)  | Rival A              | —     |
| F1-05 | Phase 1b (rivals)  | Rival B              | —     |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | —     |
| F2-02 | Phase 2 (feasib.)  | Team capability      | —     |
| F2-03 | Phase 2 (feasib.)  | Timeline             | —     |
| F2-04 | Phase 2 (feasib.)  | Cost                 | —     |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | —     |
| F2-06 | Phase 2 (feasib.)  | Top risk             | —     |
| F3-01 | Phase 3 (market)   | Addressable market   | —     |
| F3-02 | Phase 3 (market)   | Segment 1            | —     |
| F3-03 | Phase 3 (market)   | Segment 2            | —     |
| F3-04 | Phase 3 (market)   | Primary segment      | —     |
| F4-01 | Phase 4 (web)      | Source 1             | —     |
| F4-02 | Phase 4 (web)      | Source 2             | —     |
| F4-03 | Phase 4 (web)      | Source 3             | —     |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | —     |
| F5-02 | Phase 5 (synth)    | Recommendation       | —     |
| F5-03 | Phase 5 (synth)    | Confidence           | —     |
| F5-04 | Phase 5 (synth)    | Confidence rationale | —     |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | —     |
| F5-06 | Phase 5 (synth)    | Next step            | —     |

---

## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

### Phase 1a — Inertia Analysis [COMPLETE BEFORE PHASE 1b]

Why do people not change? Answer inertia before naming any rival. A competitor analysis
that opens with product names skips the primary barrier to adoption.

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b — Named Rivals

F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

---

## Phase 2 — scout-feasibility

F2-01  Technical complexity: [R/Y/G] — [reason]
F2-02  Team capability: [R/Y/G] — [reason]
F2-03  Timeline: [R/Y/G] — [reason]
F2-04  Cost: [R/Y/G] — [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 — prove-websearch

F4-01  Source: [URL or citation]
       Quote: "[direct quote — not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 — prove-synthesize

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per evidence phase — exactly 5 slots, one per phase):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting — all 20 criteria:**
- C-01: F5-02 labeled recommendation field
- C-02: F5-03 labeled confidence field
- C-03: All six sub-skill domains covered
- C-04: Phase 1a (Inertia) section complete before Phase 1b (Named Rivals) — structural not instructional
- C-05: Because block with five phase+FID citations, each claim pinnable by register lookup
- C-06: Section headers + labeled field rows
- C-07: F5-05 counter-evidence with required FID reference
- C-08: F5-01 hypothesis outcome resolves F0-01
- C-09: F5-04 confidence rationale cites FIDs
- C-10: F5-06 conditioned next step
- C-11: FID-labeled required rows per phase = per-phase required-field schema
- **C-12: "because Phase N, F[N]-[seq]" — Phase prefix satisfies rubric example; FID key provides unique auditable reference. No strict-scorer risk.**
- C-13: Phase 0 section before Phase 1 by document position
- C-14: Five labeled phase slots = five distinct phases — PASS by template construction
- C-15: FINDING REGISTER pre-assigns all FIDs — PASS by construction
- C-16: Standalone FINDING REGISTER before Phase 0 with "—" skeleton rows — PASS strict and liberal
- C-17: Five labeled Because slots for five evidence phases
- C-18: F5-05 cites the FID it qualifies
- C-19: F5-01 resolves F0-01 by FID reference
- C-20: Gate in FINDING REGISTER header, Phase 0 header, Phase 1a header — three gate points

**Zero residual risks.** C-12 hybrid closes the only remaining ambiguity from R4.
C-04 is now section-structurally enforced (Phase 1a section header + gate before Phase 1b).

**Predicted v5 score**: 12/12 aspirational → composite **100.0** (no residual risks, strict or liberal).

---

## V-05 — Combined: all R5 axes + conversational phrasing register

**Hypothesis**: V-04 applies all structural mechanisms with all-caps-imperative phrasing.
V-05 uses the identical structure — same FINDING REGISTER, same Phase 1a/1b split, same
hybrid citation format — but replaces imperative headings with conversational prose. Tests
whether the phrasing register affects criterion scores when structure is equivalent.
If scores match V-04, phrasing is neutral. If scores diverge, the imperative annotations
were doing enforcement work that prose descriptions do not replicate.

Specific phrasing changes from V-04:
1. FINDING REGISTER header: `## Finding Register` + prose description vs. `## FINDING REGISTER [COMPLETE BEFORE PHASE 0]`
2. Phase 0 header: no bracket annotation vs. `[COMPLETE BEFORE PHASE 1]` — C-20 test point
3. Phase 1a header: parenthetical note vs. `[COMPLETE BEFORE PHASE 1b]`
4. Synthesis slot rule: prose explanation vs. "one citation per evidence phase — exactly 5 slots"

Note: C-20 requires gate constraints in section headers as bracket annotations. If dropping
`[COMPLETE BEFORE PHASE N]` from Phase 0 and Phase 1a headers while retaining them only in
the FINDING REGISTER header — C-20 is ambiguous. This variation intentionally tests the
minimum gate annotation count for C-20 passage.

```
Run the full pre-commitment decision campaign for: {{topic}}

This is a six-phase decision brief. The brief begins with a finding register that
reserves slots for every finding across all phases. Filling the register before
Phase 0 commits the finding structure before any evidence is gathered.

---

## Finding Register [COMPLETE BEFORE PHASE 0]

Fill in the value for each finding ID when you reach its phase.
Synthesis citations must reference these IDs.

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | —     |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | —     |
| F0-03 | Phase 0 (prior)    | Confidence prior     | —     |
| F0-04 | Phase 0 (prior)    | Prior rationale      | —     |
| F0-05 | Phase 0 (prior)    | Experiment 1         | —     |
| F0-06 | Phase 0 (prior)    | Experiment 2         | —     |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | —     |
| F1-02 | Phase 1a (inertia) | Switching cost       | —     |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | —     |
| F1-04 | Phase 1b (rivals)  | Rival A              | —     |
| F1-05 | Phase 1b (rivals)  | Rival B              | —     |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | —     |
| F2-02 | Phase 2 (feasib.)  | Team capability      | —     |
| F2-03 | Phase 2 (feasib.)  | Timeline             | —     |
| F2-04 | Phase 2 (feasib.)  | Cost                 | —     |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | —     |
| F2-06 | Phase 2 (feasib.)  | Top risk             | —     |
| F3-01 | Phase 3 (market)   | Addressable market   | —     |
| F3-02 | Phase 3 (market)   | Segment 1            | —     |
| F3-03 | Phase 3 (market)   | Segment 2            | —     |
| F3-04 | Phase 3 (market)   | Primary segment      | —     |
| F4-01 | Phase 4 (web)      | Source 1             | —     |
| F4-02 | Phase 4 (web)      | Source 2             | —     |
| F4-03 | Phase 4 (web)      | Source 3             | —     |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | —     |
| F5-02 | Phase 5 (synth)    | Recommendation       | —     |
| F5-03 | Phase 5 (synth)    | Confidence           | —     |
| F5-04 | Phase 5 (synth)    | Confidence rationale | —     |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | —     |
| F5-06 | Phase 5 (synth)    | Next step            | —     |

---

## Phase 0 — prove-hypothesis

Before gathering any market, competitor, or feasibility data, commit your prior
belief. This is the hypothesis the campaign will test — complete Phase 0 before
starting Phase 1 so that evidence either confirms or challenges a genuine prior.

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

### Phase 1a — Inertia Analysis

Start here. Understand why people don't change before naming any product or company.
The hidden cost of the status quo is the primary competitor in most markets.

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b — Named Rivals

Complete Phase 1a before filling Phase 1b.

F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

---

## Phase 2 — scout-feasibility

F2-01  Technical complexity: [R/Y/G] — [reason]
F2-02  Team capability: [R/Y/G] — [reason]
F2-03  Timeline: [R/Y/G] — [reason]
F2-04  Cost: [R/Y/G] — [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 — name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 — prove-websearch

F4-01  Source: [URL or citation]
       Quote: "[direct quote — not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 — prove-synthesize

The synthesis draws the full campaign together. One citation from each evidence
phase (Phases 0 through 4 = 5 phases = 5 slots). If a phase is absent from the
Because block, that phase's evidence didn't reach the recommendation.

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (5 evidence phases = 5 slots — one FID citation per phase):
- Prior (Phase 0): [claim] because Phase 0, F0-[seq]
- Competitors (Phase 1): [claim] because Phase 1, F1-[seq]
- Feasibility (Phase 2): [claim] because Phase 2, F2-[seq]
- Market (Phase 3): [claim] because Phase 3, F3-[seq]
- Web evidence (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Phrasing register contrast with V-04:**

| Element | V-04 (imperative) | V-05 (conversational) |
|---------|-------------------|-----------------------|
| Register header | `## FINDING REGISTER [COMPLETE BEFORE PHASE 0]` | `## Finding Register [COMPLETE BEFORE PHASE 0]` + prose |
| Phase 0 header | `[COMPLETE BEFORE PHASE 1]` bracket annotation | Prose preamble ("complete Phase 0 before starting Phase 1") |
| Phase 1a header | `[COMPLETE BEFORE PHASE 1b]` bracket annotation | Prose instruction ("Complete Phase 1a before filling Phase 1b.") |
| Citation format | `because Phase 0, F0-[seq]` | `because Phase 0, F0-[seq]` (identical) |

**C-20 analysis**: V-05 retains the bracket annotation in the FINDING REGISTER header
(`[COMPLETE BEFORE PHASE 0]`). Phase 0 and Phase 1a headers drop their bracket annotations
in favor of prose preambles. C-20 requires gate constraints to be "part of the heading
label itself" — prose in the section body does not count. A scorer checking headers will
find one annotated header (Finding Register) and two unannotated ones (Phase 0, Phase 1a).
- **Liberal scoring**: The Finding Register gate annotation passes C-20 since at least one
  structural boundary carries the gate in its header.
- **Strict scoring**: C-20 may fail because Phase 0 and Phase 1a no longer carry their
  gate constraints in the heading label — only in prose bodies. If C-20 requires ALL
  ordering-relevant headers to carry annotations, V-05 fails.

This is the predicted V-04 > V-05 differentiator: V-05 tests the minimum gate annotation
count for C-20 passage. A partial-annotation template (one header annotated, others prose)
sits at the C-20 boundary.

**Predicted v5 score**:
- C-20 liberal (one annotated header sufficient): 12/12 = **100.0**
- C-20 strict (all ordering headers must be annotated): 11/12 = **99.2**
- C-12 risk is eliminated (hybrid citation same as V-04). The only open question is C-20.

---

## Variation Summary

| ID | Axes | C-12 | C-13 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | Predicted v5 |
|----|------|------|------|------|------|------|------|------|------|--------------|
| V-01 | C-12 hybrid citation | **PASS (hybrid, no risk)** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100.0** |
| V-02 | Inertia elevation (Phase 1a/1b) | PASS (FID risk, low-mod) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100.0** liberal / **99.2** strict |
| V-03 | C-20 graft on non-FID template | PASS (Phase+section) | FAIL | FAIL | FAIL | PASS | FAIL | FAIL | **PASS** | **95.83** |
| V-04 | C-12 hybrid + inertia elevation | **PASS (hybrid, no risk)** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100.0** |
| V-05 | All axes, conversational register | **PASS (hybrid, no risk)** | PASS | PASS | PASS | PASS | PASS | PASS | CONDITIONAL | **100.0** liberal / **99.2** strict |

**Predicted ranking**: V-04 >= V-01 > V-02 = V-05 >> V-03.

- **V-04** is the R5 unambiguous 100-target. Hybrid citation eliminates C-12 risk; Phase 1a/1b
  elevates C-04 enforcement to the section level. No remaining ambiguity under any
  interpretation.
- **V-01** closes the last C-12 strict risk from R4 with a single-axis change. Expected to score
  identically to V-04 on the rubric. The design difference (no Phase 1a/1b) is invisible to
  rubric scoring but matters for C-04 structural strength in practice.
- **V-02** tests whether inertia elevation is detectable by the rubric. Predicted 100.0 liberal;
  the C-12 FID-only risk (same as R4 V-01) is the only residual.
- **V-05** tests whether conversational phrasing changes anything when structure is constant.
  Predicted same band as V-02 — conditional on C-20 partial-annotation interpretation. If
  prose preambles suffice for C-20, scores match V-04.
- **V-03** is a deliberate boundary test on a no-FID baseline. Confirms that C-20 is achievable
  without C-15 but delivers only 0.83 pts on a 95.0 baseline. The FID system (C-15) is the
  higher-yield investment.

**R5 structural thesis**: The C-12 hybrid citation format ("because Phase N, F[N]-[seq]")
is the minimum change required to eliminate the last residual scoring risk from the R4
100-target variants. C-20 is a structural format criterion that is achievable without a
FID system but has low marginal yield in isolation. The Phase 1a/1b inertia elevation
strengthens C-04 structurally without affecting any rubric criterion score — its value
is in reducing C-04 false-positive rates in practice (a model that fills Phase 1b before
1a has to skip a clearly labeled "Inertia Analysis" section to do so).
