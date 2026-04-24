---
skill: quest-variate
skill_target: campaign-decide
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v3-2026-03-16.md
---

# Variations — campaign-decide / Round 3

Five complete, runnable skill body variations targeting the v3 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R2 diagnosis driving R3 axis choices:**

| R2 variation | v3 score | Failure mode |
|--------------|----------|--------------|
| V-01 (named-field schema) | 95.7 | C-13 FAIL (no Phase-0 prior), C-15 FAIL (no FID) |
| V-02 (hypothesis-first) | 97.1 | C-15 FAIL (no FID); C-13 passes because hypothesis is Phase 1 |
| V-03 (FID system) | 98.6–100 | C-13 conditional — passes ONLY IF hypothesis lands in Phase 1; not guaranteed by template construction |
| V-04 (named fields + FID) | 98.6–100 | Same C-13 conditionality as V-03; "minimum 4 citations" in Because block covers C-14 but not explicitly phase-labeled |

**R3 targets C-13, C-14, C-15 by construction.** Each single-axis variation addresses
one new criterion in isolation. Combined variations layer them until V-05 closes all three
gaps simultaneously.

| Axis | Criterion targeted | Mechanism |
|------|--------------------|-----------|
| C-13 structural lock | C-13 | Phase 0 pre-evidence commitment — structurally precedes all scouting phases |
| C-14 span mandate | C-14 | Per-phase labeled slots in Because block — each phase gets exactly one required citation row |
| C-15 pre-assigned FIDs | C-15 | Template pre-assigns all finding IDs — model fills values, cannot skip ID assignment |

---

## V-01 — Axis: C-13 structural hypothesis lock (Phase 0 pre-evidence)

**Hypothesis**: Adding an explicit Phase 0 that must be completed before Phase 1
makes C-13 fail-proof by position. The template rule "Phase 0 must be complete
before Phase 1 begins" turns hypothesis commitment from a best-effort instruction
into a structural gate. All other format decisions (named-field rows, Phase+section
citation syntax) are carried from R2 V-01, isolating C-13 as the single new axis.
C-15 still fails (no FID system). C-14 is likely but not guaranteed — Because block
has four labeled placeholders spanning three or four phases.

```
Run the full pre-commitment decision campaign for: {{topic}}

HYPOTHESIS LOCK: Phase 0 must be fully populated before Phase 1 begins.
No evidence is gathered before the hypothesis is committed. An incomplete
Phase 0 field means the campaign cannot advance.

---

## Phase 0 — prove-hypothesis [PRIOR COMMITMENT — COMPLETE BEFORE SCOUTING]

Claim: [one falsifiable sentence — what must be true for this to be worth building]
Falsification condition: [what single piece of evidence would disprove this claim]
Confidence prior: [Low/Medium/High]
Prior rationale: [reason for your prior — name the assumption before seeing any external data]
Experiment 1: [name and method]
Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

Inertia — status-quo cost: [why people pay the hidden cost of not changing]
Inertia — switching cost: [what users lose by moving to any alternative]
Inertia — good-enough threshold: [when the current approach feels acceptable]
Rival 1 — name: [name] | type: named | threat: [Low/Medium/High] | notes: [one sentence]
Rival 2 — name: [name] | type: named | threat: [Low/Medium/High] | notes: [one sentence]

Ordering rule: all Inertia fields must precede any Rival field.

---

## Phase 2 — scout-feasibility

Technical complexity: [R/Y/G] — [reason]
Team capability: [R/Y/G] — [reason]
Timeline: [R/Y/G] — [reason]
Cost: [R/Y/G] — [reason]
Overall feasibility: [R/Y/G]
Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

Addressable market: [size estimate with stated basis]
Segment 1 — name: [name] | fit: [1-10] | reason: [one sentence]
Segment 2 — name: [name] | fit: [1-10] | reason: [one sentence]
Primary segment: [name] | justification: [one sentence]

---

## Phase 4 — prove-websearch

[Repeat for each source — minimum 3]

Source: [URL or citation]
Quote: "[direct quote — not paraphrase]"
Strength: [Weak/Moderate/Strong]
Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 — prove-synthesize

Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves the Phase 0 claim]
Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
Confidence: [High/Medium/Low]
Confidence rationale: [name the specific findings or gaps that drove this rating — not just the label]

Because (required, cite by Phase and field):
- [claim] because Phase 0, [claim or prior-rationale field]
- [claim] because Phase 1, [inertia or rival field]
- [claim] because Phase 2, [feasibility field]
- [claim] because Phase 3 or Phase 4, [market or source field]

Counter-evidence: [one risk or caveat that could undermine the recommendation]
Next step: [COMMIT → concrete action, not "do more research" | no-build → exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (ordering rule enforces inertia-first by construction), C-05 (Phase+field
citations in Because block), C-06 (section headers per phase), C-07 (counter-evidence field),
C-08 (hypothesis outcome field resolves Phase 0), C-09 (confidence rationale required), C-10
(conditioned next step), C-11 (required labeled fields per phase), C-12 ("because Phase N, field"
is prescribed format), C-13 (Phase 0 structurally precedes all evidence phases — PASS by construction).

**C-14 risk**: Because block has four placeholder slots spanning "Phase 0, Phase 1, Phase 2,
Phase 3 or Phase 4." If the model chooses only Phase 3 for the last slot, the Because block
spans three distinct phases (Phase 0, 1, 2, 3) — C-14 passes (minimum is 3). If the model
collapses the last slot to prose without a phase number, C-14 may fail. This is the residual
C-14 risk of single-axis isolation — C-14 is likely but not guaranteed by template construction.

**C-15**: FAIL — no FID system. Named fields are human-readable labels, not enumerable citation keys.

**Predicted v3 score**: C-13 PASS, C-14 likely PASS (3+ phases in Because), C-15 FAIL →
5–6/7 aspirational → 97.1–98.6.

---

## V-02 — Axis: C-14 explicit five-phase citation slots

**Hypothesis**: Labeling each slot in the Because block with its required evidence phase
turns citation breadth from a best-effort goal into a template obligation. Five labeled
slots ("PHASE 1 (competitors):", "PHASE 2 (feasibility):", etc.) force the model to cite
at least one finding from each evidence phase. The hypothesis remains in Phase 4 (canonical
ordering) — C-13 fails because scouting Phases 1-3 execute before the hypothesis is
committed. This isolates C-14 as the single new axis. The table-per-phase structure from
R2 V-02 is retained for C-11 continuity.

```
Run the full pre-commitment decision campaign for: {{topic}}

Execute the six sub-skills in order. Each phase must be complete before advancing.
SYNTHESIS RULE: The Because block must include exactly one citation per evidence phase.
All five evidence phases must appear. A synthesis drawn from fewer than three phases is incomplete.

---

## Phase 1 — scout-competitors

| Force | Type | Strength (1-5) | Notes |
|-------|------|----------------|-------|
| Status-quo inertia | inertia | | Why people don't change |
| Switching cost | inertia | | What users lose by moving to any alternative |
| Good-enough threshold | inertia | | When the current approach feels acceptable |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must precede named rival rows.)

---

## Phase 2 — scout-feasibility

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |
| | | | |

Primary target segment: [name] — [justification]

---

## Phase 4 — prove-hypothesis

| Field | Value |
|-------|-------|
| Claim | [one falsifiable sentence — what must be true for this to be worth building] |
| Falsification condition | [what evidence would disprove this claim] |
| Confidence prior | [Low / Medium / High] |
| Prior rationale | [reason before seeing external evidence] |
| Experiment 1 | [name and method] |
| Experiment 2 | [name and method] |

---

## Phase 5 — prove-websearch

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

Because (one labeled slot per evidence phase — all five required):
- PHASE 1 (competitors): [claim] because Phase 1, [force row]
- PHASE 2 (feasibility): [claim] because Phase 2, [dimension row]
- PHASE 3 (market): [claim] because Phase 3, [segment finding]
- PHASE 4 (hypothesis): [claim] because Phase 4, [hypothesis field]
- PHASE 5 (web evidence): [claim] because Phase 5, [source citation]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (inertia rows before named rivals — structural rule in Phase 1 table),
C-05 (Because block with five citation slots), C-06 (section headers + table per phase), C-07
(counter-evidence table row), C-08 (hypothesis outcome row), C-09 (confidence rationale row),
C-10 (conditioned next step row), C-11 (table schema per phase), C-12 ("because Phase N,
[row reference]" prescribed syntax in all five Because slots), C-14 (five labeled phase slots
guarantee citations span exactly 5 distinct phases — C-14 PASS by template construction).

**C-13 FAIL**: Hypothesis is Phase 4. Evidence from Phases 1-3 (competitors, feasibility, market)
is gathered before the hypothesis is committed. The rubric requires commitment "before any evidence
phase executes." Phase 4 is after three scouting phases — C-13 fails by position.

**C-15 FAIL**: No FID system. Phase+section citations are templated (C-12 pass) but each
finding is not assigned a unique enumerable key (C-15 fail).

**Predicted v3 score**: C-14 PASS, C-13 FAIL, C-15 FAIL → 5/7 aspirational → 97.1.

---

## V-03 — Axis: C-15 pre-assigned FID template

**Hypothesis**: Pre-assigning finding IDs in the template skeleton — so the model fills values
into pre-labeled slots rather than assigning IDs as it writes — guarantees C-15 coverage even
under context pressure. When IDs are assigned by the model in-flight, a distracted or compressed
pass may produce some FID-labeled rows and some unlabeled rows. Pre-assignment removes this
variance. Hypothesis remains in Phase 4 (canonical ordering, C-13 may fail). The Because block
instructs "minimum 3 distinct phase prefixes" — a soft C-14 guardrail, not a hard template slot.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING-ID PROTOCOL: Every field in the template below carries a pre-assigned finding ID.
Fill each row. Do not skip. The synthesis Because block must cite by finding ID. Free-prose
citations ("as shown above", "based on the evidence") are not permitted.

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

## Phase 4 — prove-hypothesis

F4-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F4-02  Falsification condition: [what evidence would disprove this claim]
F4-03  Confidence prior: [Low/Medium/High] — [reason before external evidence]
F4-04  Experiment 1: [name and method]
F4-05  Experiment 2: [name and method]

---

## Phase 5 — prove-websearch

F5-01  Source: [URL or citation]
       Quote: "[direct quote — not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F5-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F5-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 6 — prove-synthesize

F6-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive]
F6-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F6-03  Confidence: [High/Medium/Low]
F6-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F6-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F6-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (required, cite by FID — minimum 3 distinct phase prefixes must appear):
- [claim] because [FID]
- [claim] because [FID]
- [claim] because [FID]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (F1-01 through F1-03 ordering rule), C-05 (FID citations in Because
block — each claim pinnable by ID lookup), C-06 (section headers per phase), C-07 (F6-05
counter-evidence field with FID reference), C-08 (F6-01 hypothesis outcome), C-09 (F6-04
confidence rationale cites FIDs), C-10 (F6-06 conditioned next step), C-11 (FID-labeled
required fields per phase constitute a per-phase schema), C-12 ("because F[phase]-[seq]"
is mechanically auditable — rubric uses "e.g." leaving format open), C-14 (soft guardrail:
"minimum 3 distinct phase prefixes"), C-15 (pre-assigned FIDs throughout — PASS by construction).

**C-12 risk**: The rubric example is "because Phase [N], [section reference]." FID format
"because F1-01" differs syntactically. The rubric says "e.g." which suggests the example is not
exhaustive, and FID satisfies "mechanically auditable at a glance." Strict scorers may require
Phase+section format — FID format is the known C-12 risk for all FID-based variations.

**C-13 FAIL**: Hypothesis is Phase 4 — three scouting phases precede it. Not a prior commitment.

**C-14**: Likely PASS — "minimum 3 distinct phase prefixes" instruction plus Because block
producing 3+ FIDs from different phases typically satisfies C-14. But this is a soft guardrail
(instruction-based), not a template slot. One-phase-heavy synthesis could still fail C-14 if
the model ignores the minimum.

**Predicted v3 score**: C-15 PASS, C-13 FAIL, C-14 likely PASS → 5–6/7 aspirational → 97.1–98.6.

---

## V-04 — Combined: C-13 + C-14 (Phase 0 lock + per-phase Because slots)

**Hypothesis**: Phase 0 hypothesis commitment (C-13) combined with labeled per-phase Because
slots (C-14) should push to 98.6. The two mechanisms are complementary: Phase 0 makes the
hypothesis a genuine prior; labeled slots force synthesis to integrate evidence across the full
campaign width. No FID system (C-15 still fails), but C-12 citation format is clean
Phase+section, reducing scorer risk. Uses table-per-phase structure for C-11.

```
Run the full pre-commitment decision campaign for: {{topic}}

TWO RULES:
1. HYPOTHESIS FIRST — Phase 0 must be complete before Phase 1 begins. Evidence tests
   the Phase 0 claim. It does not build post-hoc justification for a conclusion.
2. EVIDENCE BREADTH — The Because block in Phase 5 must include one citation per
   evidence phase. All five phases must appear. Fewer than three evidence phases
   cited in synthesis means the campaign is incomplete.

---

## Phase 0 — prove-hypothesis [PRIOR COMMITMENT — COMPLETE BEFORE SCOUTING]

| Field | Value |
|-------|-------|
| Claim | [one falsifiable sentence — what must be true for this to be worth building] |
| Falsification condition | [what single piece of evidence would disprove this claim] |
| Confidence prior | [Low / Medium / High] |
| Prior rationale | [reason for your prior before any external data is gathered] |
| Experiment 1 | [name and method] |
| Experiment 2 | [name and method] |

---

## Phase 1 — scout-competitors

| Force | Type | Strength (1-5) | Notes |
|-------|------|----------------|-------|
| Status-quo inertia | inertia | | Why people don't change |
| Switching cost | inertia | | What users lose by moving to any alternative |
| Good-enough threshold | inertia | | When current approach feels acceptable |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must precede named rival rows.)

---

## Phase 2 — scout-feasibility

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

Top risk: [single biggest buildability threat]

---

## Phase 3 — scout-market

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |
| | | | |

Primary target segment: [name] — [justification]

---

## Phase 4 — prove-websearch

| Source | Direct Quote | Strength | Verdict |
|--------|--------------|----------|---------|
| | "[direct quote]" | Weak / Moderate / Strong | Supports / Refutes / Neutral |
| | "[direct quote]" | | |
| | "[direct quote]" | | |

(Minimum 3 sources.)

---

## Phase 5 — prove-synthesize

| Field | Value |
|-------|-------|
| Hypothesis outcome | [Confirmed / Refuted / Inconclusive — resolves Phase 0 claim] |
| Recommendation | [COMMIT / PAUSE / PIVOT / ABANDON] |
| Confidence | [High / Medium / Low] |
| Confidence rationale | [name specific evidence gaps or strengths — not just the label] |
| Counter-evidence | [one risk or caveat that could undermine the recommendation] |
| Next step | [COMMIT: concrete action | no-build: exit condition or revisit trigger] |

Because (one labeled slot per evidence phase — all five required):
- PHASE 0 (hypothesis prior): [claim] because Phase 0, [field name]
- PHASE 1 (competitors): [claim] because Phase 1, [force row]
- PHASE 2 (feasibility): [claim] because Phase 2, [dimension row]
- PHASE 3 (market): [claim] because Phase 3, [segment finding]
- PHASE 4 (web evidence): [claim] because Phase 4, [source citation]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (inertia-before-rivals rule in Phase 1 table), C-05 (five Because
slots with Phase+field citations), C-06 (section headers + tables per phase), C-07 (counter-evidence
table row), C-08 (hypothesis outcome row links to Phase 0 claim), C-09 (confidence rationale row),
C-10 (conditioned next step row), C-11 (table-per-phase structure = per-phase required-field schema),
C-12 ("because Phase N, [field/row]" prescribed syntax in all five Because slots),
C-13 (Phase 0 structurally precedes all evidence phases — PASS by construction),
C-14 (five labeled phase slots guarantee five distinct phases cited — PASS by template construction).

**C-15 FAIL**: No FID system. Phase+section citations are clean (C-12 pass) but individual
findings have no unique enumerable key.

**C-13 vs V-02**: The "hypothesis is Phase 0" framing is stronger than "RULE 1" prose instruction.
Phase numbering forces the model to complete Phase 0 before Phase 1 is rendered — the structural
position does the enforcement rather than relying on rule-following.

**Predicted v3 score**: C-13 PASS, C-14 PASS, C-15 FAIL → 6/7 aspirational → 98.6.

---

## V-05 — Combined: C-13 + C-14 + C-15 (Phase 0 lock + per-phase FID slots — 100-target)

**Hypothesis**: Phase 0 hypothesis commitment (C-13) plus pre-assigned FIDs throughout
(C-15) plus five labeled FID-phase slots in synthesis (C-14) should close all three new
aspirational criteria simultaneously. The Because block design is the key integration:
each slot requires both a phase label (satisfying C-14 span breadth) and a specific FID
(satisfying C-15 citation precision and C-12 mechanical auditability). This is the most
constrained variation — every gap identified in R2 is addressed by template structure,
not instruction.

```
Run the full pre-commitment decision campaign for: {{topic}}

THREE RULES:
1. HYPOTHESIS FIRST — Phase 0 must be complete before Phase 1 begins.
   Evidence tests the Phase 0 claim. It does not build post-hoc justification.
2. PRE-ASSIGNED FIDs — every field has an ID (F0-01, F1-01, ...). Fill each.
   Cite by FID in synthesis. "Because F1-01" is auditable. "As shown above" is not.
3. EVIDENCE BREADTH — the Because block must cite at least one FID from each of
   the five evidence phases. All five phase prefixes (F0-xx through F4-xx) required.

---

## Phase 0 — prove-hypothesis [PRIOR COMMITMENT — COMPLETE BEFORE SCOUTING]

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High] — [reason before any external data is gathered]
F0-04  Experiment 1: [name and method]
F0-05  Experiment 2: [name and method]

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

Because (one FID citation per evidence phase — all five phase prefixes required):
- PRIOR (Phase 0): [claim] because F0-[seq]
- COMPETITORS (Phase 1): [claim] because F1-[seq]
- FEASIBILITY (Phase 2): [claim] because F2-[seq]
- MARKET (Phase 3): [claim] because F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: All 15 criteria.

- C-01: F5-02 (recommendation field) — required, labeled, cannot be absent
- C-02: F5-03 (confidence field) — required, labeled
- C-03: All six domains present — Phase 0 (prove-hypothesis), Phase 1 (competitors), Phase 2
  (feasibility), Phase 3 (market), Phase 4 (websearch), Phase 5 (synthesize)
- C-04: F1-01 through F1-03 ordering rule — inertia before rivals by construction
- C-05: Because block with five FID citations — each recommendation claim pinnable by ID lookup
- C-06: Section headers per phase + labeled field rows
- C-07: F5-05 counter-evidence field with required FID reference
- C-08: F5-01 hypothesis outcome resolves F0-01 — both fields are required
- C-09: F5-04 confidence rationale cites FIDs — not just a label
- C-10: F5-06 conditioned next step (COMMIT action vs. no-build trigger)
- C-11: Pre-assigned FID rows per phase constitute a per-phase required-field schema — every
  phase is verifiable at the field level
- C-12: "because F[phase]-[seq]" is prescribed, mechanically auditable format. Rubric example
  uses Phase+section syntax; FID is more precise. The rubric uses "e.g." — FID satisfies the
  spirit. Strict-scorer risk remains (see below).
- C-13: Phase 0 structurally precedes all evidence phases — PASS by template position
- C-14: Five labeled phase slots require five distinct phase prefixes in Because block — PASS by
  template construction, not instruction compliance
- C-15: Pre-assigned FIDs on every field throughout all phases — PASS by construction, no
  in-flight assignment variance

**C-12 strict-scorer risk**: The rubric example is "because Phase [N], [section reference]."
V-05 uses "because F0-01" (FID format). Both are mechanically auditable. The rubric says "e.g."
and defines passing as "making traceability mechanically auditable at a glance" — FID satisfies
this definition. Risk: low-to-moderate. Mitigation: if strict C-12 scoring is a concern,
V-04 uses Phase+section format and avoids this risk at the cost of C-15.

**C-03 ordering note**: C-03 requires "all six domains represented," not "in canonical sequence."
Phase 0 for prove-hypothesis (before scouting) satisfies coverage. A scorer checking for canonical
ordering (competitors first) would be applying a requirement not stated in the rubric. Risk: low.

**Predicted v3 score**: C-13 PASS, C-14 PASS, C-15 PASS → 6–7/7 aspirational → 98.6–100.
C-12 strict-scorer scenario: 6/7 → 98.6. C-12 liberal-scorer scenario: 7/7 → 100.

---

## Variation Summary

| ID | Axes | C-13 | C-14 | C-15 | Other new risks | Predicted v3 |
|----|------|------|------|------|-----------------|--------------|
| V-01 | C-13 structural lock | PASS (Phase 0 by position) | Likely (3+ phases in Because) | FAIL (no FID) | C-14 not guaranteed by template | 97.1–98.6 |
| V-02 | C-14 five-phase slots | FAIL (hypothesis Phase 4) | PASS (5 labeled slots) | FAIL (no FID) | C-13 fails by position | 97.1 |
| V-03 | C-15 pre-assigned FIDs | FAIL (hypothesis Phase 4) | Likely (soft "min 3" guardrail) | PASS (pre-assigned) | C-12 FID risk; C-14 not template-guaranteed | 97.1–98.6 |
| V-04 | C-13 + C-14 combined | PASS (Phase 0) | PASS (5 labeled slots) | FAIL (no FID) | None new | 98.6 |
| V-05 | C-13 + C-14 + C-15 | PASS (Phase 0) | PASS (5 FID-phase slots) | PASS (pre-assigned) | C-12 strict-scorer risk (FID vs Phase syntax) | 98.6–100 |

**Predicted ranking**: V-05 > V-04 > V-01 ~= V-03 > V-02.

V-05 is the 100-target: all three new aspirational criteria pass by construction, not by
instruction compliance. V-04 is the 98.6 floor with no C-12 risk — the safest high-scorer
if FID format is disputed. V-01 and V-03 share a similar score band: each closes one new
criterion with residual gaps on the other two. V-02 isolates C-14 cleanly but sacrifices
C-13, landing at the same score as R2 V-02.

**Rubric evolution observation**: C-13 and C-14 are best addressed through schema structure
(Phase 0 position, labeled slots) rather than instruction ("state your belief first"). C-15
is best addressed through pre-assignment rather than in-flight assignment. V-05 applies
all three structural mechanisms simultaneously — the template does the enforcement so the
model doesn't have to remember.
