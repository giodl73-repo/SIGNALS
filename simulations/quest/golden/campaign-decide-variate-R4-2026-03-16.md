---
skill: quest-variate
skill_target: campaign-decide
round: 4
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v4-2026-03-16.md
---

# Variations — campaign-decide / Round 4

Five complete, runnable skill body variations targeting the v4 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R3 → R4 diagnosis:**

The v4 rubric added two new aspirational criteria (C-16 and C-17) and expanded the
denominator from /7 to /9. R3's best variant (V-05) is now ambiguous on C-16:

| R3 variation | v4 C-16 status | v4 C-17 status | v4 composite |
|--------------|----------------|----------------|--------------|
| V-01 (Phase 0 + named fields) | FAIL — no FID system | FAIL — 4 slots for 5 phases | 96.7 |
| V-02 (5-slot synthesis + Phase 4 hyp.) | FAIL — no FID system | PASS — 5 slots by construction | 96.7 |
| V-03 (FID inline, Phase 4 hyp.) | AMBIGUOUS — FIDs inline in phases, no preamble | PASS if slots match phases | 97.8–98.9 |
| V-04 (Phase 0 + 5-slot synthesis) | FAIL — no FID system | PASS — 5 slots by construction | 98.6 |
| V-05 (Phase 0 + FID + 5-slot) | AMBIGUOUS — FIDs inline in phases, no preamble | PASS — 5 labeled FID-phase slots | 98.9–100 |

**The C-16 ambiguity**: The rubric evaluation note says "a brief that lists all FIDs in a
preamble section *before any evidence heading* passes; one that accumulates FIDs inline as
findings are recorded fails." R3 V-03 and V-05 assign FIDs inline within phase sections —
there is no standalone preamble register. Under strict C-16 scoring, both fail. Under the
summary table's reading ("pre-assigned = pre-seeded"), both pass.

**R4 axes:**

| Axis | Criterion targeted | Mechanism |
|------|--------------------|-----------|
| C-16 full preamble register | C-16 strict | Standalone FINDING REGISTER section before Phase 0, all FID skeletons listed with "—" placeholder values |
| C-17 explicit slot-count formula | C-17 strict | "PHASE COUNT: N. SYNTHESIS SLOTS: N. Slot count must equal phase count." declared as a formula, not just a count |
| C-16 compact range register | C-16 minimal | Lightweight preamble listing FID ranges per phase rather than individual skeleton rows |

Single-axis: V-01 (C-16 full preamble), V-02 (C-17 formula), V-03 (C-16 minimal range).
Combined: V-04 (all criteria, V-01 preamble + C-17 formula + Phase 0 + FIDs), V-05 (V-04
structure, conversational phrasing register).

---

## V-01 — Axis: C-16 full preamble register (strict pre-phase FID table)

**Hypothesis**: A dedicated FINDING REGISTER section listing every FID skeleton as a table
row with "—" placeholder values, positioned before Phase 0, satisfies C-16 under any
scoring interpretation. The evaluation note requires "a preamble section before any evidence
heading" — this is the only design that cannot be disputed. All other structure is carried
from R3 V-05: Phase 0 hypothesis lock (C-13 PASS), inline FIDs per phase (C-15 PASS), five
labeled synthesis slots (C-17 PASS). C-16 is the single new axis.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by FID in synthesis.
Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE ENTERING PHASE 0]

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

## Phase 0 — prove-hypothesis [PRIOR COMMITMENT — COMPLETE BEFORE PHASE 1]

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

Because (one FID per evidence phase — exactly 5 slots, one per phase):
- PRIOR (Phase 0): [claim] because F0-[seq]
- COMPETITORS (Phase 1): [claim] because F1-[seq]
- FEASIBILITY (Phase 2): [claim] because F2-[seq]
- MARKET (Phase 3): [claim] because F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**:
- C-01: F5-02 (recommendation field) — required, labeled, cannot be absent
- C-02: F5-03 (confidence field) — required, labeled
- C-03: All six domains present — Phase 0 (prove-hypothesis), Phase 1 (competitors), Phase 2 (feasibility), Phase 3 (market), Phase 4 (websearch), Phase 5 (synthesize)
- C-04: F1-01–F1-03 ordering rule — inertia before rivals by construction
- C-05: Because block with five FID citations
- C-06: Section headers per phase + labeled field rows
- C-07: F5-05 counter-evidence field with required FID reference
- C-08: F5-01 hypothesis outcome resolves F0-01
- C-09: F5-04 confidence rationale cites FIDs
- C-10: F5-06 conditioned next step (COMMIT action vs. no-build trigger)
- C-11: FID-labeled required fields per phase = per-phase required-field schema
- C-12: "because F[N]-[seq]" prescribed, mechanically auditable. FID format risk vs. "Phase [N], [section reference]" example (same risk as R3 V-05).
- C-13: Phase 0 structurally precedes all evidence phases — PASS by position
- C-14: Five labeled phase slots guarantee 5 distinct phases — PASS by template construction
- C-15: Pre-assigned FIDs throughout — PASS by construction, no in-flight variance
- **C-16: Standalone FINDING REGISTER section before Phase 0 with "—" skeleton placeholders — PASS by construction under all interpretations, strict and liberal**
- C-17: Exactly 5 labeled slots declared in Because block for 5 evidence phases — PASS by construction

**C-12 strict-scorer risk**: Retained from R3 V-05. FID format ("because F0-01") differs from
rubric example ("because Phase [N], [section reference]") but the rubric says "e.g." and defines
passing as "mechanically auditable at a glance" — FID satisfies this. Risk: low-to-moderate.

**Predicted v4 score**: C-16 PASS (preamble register), C-17 PASS (5 labeled slots), C-13 PASS
(Phase 0), C-14 PASS (5 slots), C-15 PASS (pre-assigned) → 8–9/9 aspirational → **98.9–100**.
C-12 strict-scorer scenario: 8/9 → 98.9. Liberal: 9/9 → 100.

---

## V-02 — Axis: C-17 explicit phase-count formula (no FIDs, canonical hypothesis ordering)

**Hypothesis**: The C-17 gap in R3 V-01 was not a missing slot — it was a collapsed slot
("Phase 3 or Phase 4" merged two phases into one). The fix is not counting to 5 manually
but declaring the formula "SLOT COUNT = PHASE COUNT = N" explicitly in the template
preamble. When the model sees the declared integer equality, slot collapse becomes
arithmetically detectable. This variation isolates C-17 using named-field format (no FIDs,
C-15/C-16 both fail) and canonical hypothesis ordering (Phase 4, C-13 fails) — single axis
on C-17. The v4 table shows V-02 (R3) already passes C-17 with 5 labeled slots; V-02 (R4)
adds an explicit slot-count declaration to make the enforcement structural rather than
incidental. Uses table-per-phase for C-11.

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

**Rubric targeting**:
- C-01/C-02: recommendation + confidence table rows
- C-03: Phases 1–6 cover all six sub-skills
- C-04: Inertia rows before named rivals (table structure)
- C-05: Because block with five Phase+field citations
- C-06: Section headers + table per phase
- C-07: Counter-evidence table row
- C-08: Hypothesis outcome row
- C-09: Confidence rationale row
- C-10: Conditioned next step row
- C-11: Table schema per phase = per-phase required-field schema
- C-12: "because Phase N, [row reference]" — exact rubric example format. PASS by construction, no FID risk.
- C-13: FAIL — hypothesis is Phase 4. Three scouting phases (Phases 1–3) execute before the hypothesis is committed.
- C-14: PASS — 5 labeled phase slots require citations from 5 distinct phases by template construction
- C-15: FAIL — no FID system. Phase+section citations are clean (C-12 pass) but no unique per-finding keys.
- C-16: FAIL — no FID system, no register.
- **C-17: PASS by construction — "SLOT COUNT (5) = PHASE COUNT (5)" declared as a formula. The no-merge rule ("no slot may be omitted or merged") makes slot collapse detectably wrong.**

**Design note**: C-17 PASS mechanism here is stronger than R3 V-02's 5-slot template alone.
R3 V-02 had 5 labeled slots — a scorer could ask "are there 5 phases?" and count. R4 V-02
declares the integer equality in the preamble phase map, so the constraint is self-describing.

**Predicted v4 score**: C-17 PASS, C-12 PASS (Phase+section exact format), C-13 FAIL, C-15/C-16 FAIL → 6/9 aspirational → composite **96.7**. Same band as v4 V-02 (R3), but C-17 enforcement is now structural rather than incidental.

---

## V-03 — Axis: C-16 compact range register (minimal preamble)

**Hypothesis**: The FINDING REGISTER does not need to enumerate every individual FID row
to satisfy C-16 — it needs to be a distinct pre-phase section that commits the finding
structure. A compact table listing FID ranges per phase (F0-01..F0-06, F1-01..F1-05, etc.)
with a domain label is a "numbered finding register with skeleton FID placeholders" if the
downstream phase sections fill those ranges. This is the minimum viable register test: does
range-based pre-commitment satisfy C-16's "before any evidence phase executes" requirement,
or does the rubric require individual FID skeletons? If compact range works, it saves
significant template space. The hypothesis is in Phase 0 (C-13 PASS) to isolate C-16 as
the single new variable.

```
Run the full pre-commitment decision campaign for: {{topic}}

CAMPAIGN REGISTER — commit this finding skeleton before any evidence phase begins.
Populate each FID range in its phase section. Cite findings by FID in synthesis.

| Phase | Sub-skill            | Domain          | FID range       |
|-------|----------------------|-----------------|-----------------|
| 0     | prove-hypothesis     | Prior belief    | F0-01 .. F0-06  |
| 1     | scout-competitors    | Inertia + rivals| F1-01 .. F1-05  |
| 2     | scout-feasibility    | Buildability    | F2-01 .. F2-06  |
| 3     | scout-market         | Segments        | F3-01 .. F3-04  |
| 4     | prove-websearch      | Ext. evidence   | F4-01 .. F4-03  |
| 5     | prove-synthesize     | Decision        | F5-01 .. F5-06  |

---

## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High] — [reason]
F0-04  Prior rationale: [why you believe this before seeing any data]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]
F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

(F1-01 through F1-03 first — inertia before rivals.)

---

## Phase 2 — scout-feasibility

F2-01  Technical complexity: [R/Y/G] — [reason]
F2-02  Team capability: [R/Y/G] — [reason]
F2-03  Timeline: [R/Y/G] — [reason]
F2-04  Cost: [R/Y/G] — [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [biggest buildability threat]

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
F5-04  Confidence rationale: [cite the FIDs that drove this rating]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one FID from each registered phase — 5 slots, 5 phases, no phase may be skipped):
- PRIOR (Phase 0): [claim] because F0-[seq]
- COMPETITORS (Phase 1): [claim] because F1-[seq]
- FEASIBILITY (Phase 2): [claim] because F2-[seq]
- MARKET (Phase 3): [claim] because F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: Same as V-01 for C-01 through C-15 and C-17. The single difference is
the C-16 mechanism.

**C-16 analysis**: The CAMPAIGN REGISTER section is a distinct pre-phase section that appears
before Phase 0 (the first evidence heading). It commits FID ranges ("F0-01 .. F0-06") per
phase. The question is: does range-based pre-commitment constitute "skeleton FID placeholders"?

- **Liberal interpretation** (range counts as placeholder): The register declares which FID
  blocks exist per phase — C-16 PASS.
- **Strict interpretation** (individual skeletons required): The register lists ranges, not
  individual FID rows with "—" values. A scorer may require each FID to be individually listed
  before Phase 0 starts — C-16 FAIL (only V-01 and V-04 satisfy this).

This variation intentionally tests the boundary. If C-16 passes with compact ranges, it
reveals the minimum viable register design.

**C-16**: Conditional PASS/FAIL. **C-17**: PASS (5 labeled slots). **C-13**: PASS (Phase 0
before Phase 1). **C-15**: PASS (pre-assigned FIDs). **C-12**: FID format risk (same as V-01).

**Predicted v4 score**:
- Strict C-16 scoring: 7/9 aspirational → composite **97.8**
- Liberal C-16 scoring: 8–9/9 → composite **98.9–100** (with C-12 risk)

---

## V-04 — Combined: C-16 full preamble + C-17 formula + C-13 + C-15 (100-target)

**Hypothesis**: Combining V-01's full preamble register (C-16 unambiguous PASS) with V-02's
explicit slot-count formula (C-17 formula-declared PASS), Phase 0 hypothesis commitment
(C-13 PASS), and pre-assigned FIDs throughout (C-15 PASS) closes all 9 aspirational criteria
simultaneously. The template does all enforcement — no criterion depends on analyst recall
or choice. This is the R4 100-target.

The key addition over R3 V-05: the FINDING REGISTER is now a standalone section that
appears BEFORE Phase 0, resolving the C-16 ambiguity. The synthesis preamble now declares
"SLOT COUNT (5) = PHASE COUNT (5)" as a formula, resolving any residual C-17 collapse risk.

```
Run the full pre-commitment decision campaign for: {{topic}}

FOUR STRUCTURAL RULES — enforced by template position, not by instruction compliance:
1. REGISTER FIRST — the finding register below commits all FID skeletons before any phase
   executes. Fill values in phase sections. Do not create FIDs outside the register.
2. HYPOTHESIS FIRST — Phase 0 must be complete before Phase 1 begins.
3. FID CITATIONS — all synthesis citations must reference registered FIDs.
4. SLOT MATCH — the Because block has exactly 5 slots for 5 evidence phases (Phases 0–4).
   SLOT COUNT (5) = PHASE COUNT (5). No slot may be omitted or merged with another.

---

## FINDING REGISTER [COMMIT BEFORE PHASE 0]

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

Ordering rule: F1-01 through F1-03 (inertia) must precede F1-04+ (rivals).

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

Because (SLOT COUNT = PHASE COUNT = 5 — one FID citation per evidence phase,
no slot may be omitted or merged, no phase may appear more than once):
- PRIOR (Phase 0): [claim] because F0-[seq]
- COMPETITORS (Phase 1): [claim] because F1-[seq]
- FEASIBILITY (Phase 2): [claim] because F2-[seq]
- MARKET (Phase 3): [claim] because F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting** — all 17 criteria:
- C-01: F5-02 recommendation field
- C-02: F5-03 confidence field
- C-03: All six sub-skills covered (Phase 0 = prove-hypothesis, Phase 1 = competitors, Phase 2 = feasibility, Phase 3 = market, Phase 4 = websearch, Phase 5 = synthesize)
- C-04: F1-01–F1-03 ordering rule — inertia before rivals by construction
- C-05: Because block with five FID citations — each claim pinnable by register lookup
- C-06: Section headers per phase + labeled field rows
- C-07: F5-05 counter-evidence with required FID reference
- C-08: F5-01 hypothesis outcome resolves F0-01 — both required fields
- C-09: F5-04 confidence rationale cites FIDs
- C-10: F5-06 conditioned next step
- C-11: FID-labeled required rows per phase = per-phase required-field schema, verifiable at the field level
- C-12: "because F[N]-[seq]" prescribed format. FID risk (same as R3 V-05 — low-to-moderate)
- C-13: Phase 0 before Phase 1 by document position — PASS by construction
- C-14: 5 labeled phase slots = 5 distinct phases cited — PASS by template construction
- C-15: FINDING REGISTER pre-assigns all FIDs — PASS by construction, zero in-flight variance
- **C-16: FINDING REGISTER is a standalone section before Phase 0 with "—" placeholder rows — PASS under both strict and liberal interpretations, no ambiguity**
- **C-17: "SLOT COUNT = PHASE COUNT = 5" declared as a formula in synthesis preamble, plus no-merge rule — PASS by template declaration, not by slot counting alone**

**Predicted v4 score**: 8–9/9 aspirational → composite **98.9–100**.
Only remaining risk: C-12 strict FID-vs-Phase-syntax debate (low-to-moderate).

---

## V-05 — Combined: all criteria, conversational phrasing register

**Hypothesis**: V-04's template closes all 9 aspirational criteria by structural position. The
open question is whether the all-caps-imperative phrasing style ("REGISTER FIRST", "SLOT COUNT
= PHASE COUNT = 5") is doing the enforcement or whether the structural template position is
doing it. V-05 uses identical structural elements — same FINDING REGISTER before Phase 0, same
5-slot Because block with "SLOT COUNT = PHASE COUNT" arithmetic, same FID inline rows — but
replaces all-caps imperatives with plain explanatory prose. If compliance rates are equivalent,
the imperative style was unnecessary markup. If compliance drops, the all-caps style was doing
real enforcement work.

```
Run the full pre-commitment decision campaign for: {{topic}}

This is a six-phase decision brief. Each phase produces findings that feed the synthesis.
The brief begins with a finding register that reserves slots for every finding across all
phases — this is the structural skeleton you'll fill in. Completing the register before
Phase 0 ensures all finding slots are committed before any evidence is gathered.

---

## Finding Register

This section reserves all finding IDs before any evidence phase begins. Fill in the value
for each finding ID when you reach its phase. Synthesis citations must use these IDs.

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

## Phase 0 — prove-hypothesis

Before gathering any market, competitor, or feasibility data, commit your prior belief.
This is the hypothesis the campaign will test — not a conclusion you'll build toward.
Completing Phase 0 before Phase 1 means the evidence either confirms or challenges a
genuine prior, not a post-hoc rationalization.

F0-01  Claim: [one falsifiable sentence — what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 — scout-competitors

Start with incumbent inertia — the forces that keep people from changing — before naming
specific rivals. Inertia explains why people don't move even when better options exist.

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]
F1-04  Rival A — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B — name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

(F1-01 through F1-03 before F1-04 onward — inertia before named rivals.)

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

This is where you draw the campaign together. The synthesis has a required structure:
one Because slot per evidence phase (Phases 0 through 4 = 5 phases = 5 slots). The
slot count and phase count must match — if a phase is absent from the Because block,
that phase's evidence didn't reach the recommendation.

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]
F5-05  Counter-evidence: [one risk or caveat — cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (5 evidence phases = 5 slots, one per phase — cite a specific FID from each):
- Prior (Phase 0): [claim] because F0-[seq]
- Competitors (Phase 1): [claim] because F1-[seq]
- Feasibility (Phase 2): [claim] because F2-[seq]
- Market (Phase 3): [claim] because F3-[seq]
- Web evidence (Phase 4): [claim] because F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Phrasing register contrast with V-04**:

| Element | V-04 (imperative) | V-05 (conversational) |
|---------|-------------------|-----------------------|
| Header | `FINDING REGISTER [COMMIT BEFORE PHASE 0]` | `Finding Register` + prose explanation |
| Slot rule | `SLOT COUNT (5) = PHASE COUNT (5). No slot may be omitted or merged.` | "5 evidence phases = 5 slots... slot count and phase count must match" |
| Inertia rule | `Ordering rule: F1-01 through F1-03 (inertia) must precede F1-04+` | "(F1-01 through F1-03 before F1-04 onward — inertia before named rivals.)" |
| Phase 0 gate | `## Phase 0 — prove-hypothesis [COMPLETE BEFORE PHASE 1]` | Section header + prose explanation of why |

**Structural equivalence**: All FID rows, section ordering, and synthesis slot count are
identical between V-04 and V-05. The only variation axis is the phrasing register.

**Rubric targeting**: Identical to V-04 for all 17 criteria. C-16 PASS (register before
Phase 0, standalone section). C-17 PASS (5 slots explained by prose formula). C-13 PASS
(Phase 0 section before Phase 1). C-15 PASS (pre-assigned FIDs). C-12 FID risk (same).

**C-17 nuance**: V-04's formula "SLOT COUNT (5) = PHASE COUNT (5)" is more explicit than
V-05's "5 evidence phases = 5 slots." A strict C-17 scorer checking "slot count must equal
phase count" can verify either, but V-04's all-caps declaration is harder to overlook.
V-05's explanation ("if a phase is absent... that phase's evidence didn't reach the
recommendation") provides the rationale but not the arithmetic assertion. This is the
predicted V-04 > V-05 differentiator.

**Predicted v4 score**: Same band as V-04, 8–9/9 aspirational → composite **98.9–100**.
Potential 0.5-pt downside vs. V-04 on C-17 if "SLOT COUNT = PHASE COUNT" explicit formula
is scored differently from prose explanation. Phrasing register itself does not affect any
criterion score.

---

## Variation Summary

| ID | Axes | C-13 | C-15 | C-16 | C-17 | Other risks | Predicted v4 |
|----|------|------|------|------|------|-------------|--------------|
| V-01 | C-16 full preamble register | PASS (Phase 0) | PASS (pre-assigned) | **PASS (full table, unambiguous)** | PASS (5 labeled slots) | C-12 FID risk (low-mod) | 98.9–100 |
| V-02 | C-17 explicit slot-count formula | FAIL (Phase 4) | FAIL (no FID) | FAIL (no register) | **PASS (formula declared)** | None new | 96.7 |
| V-03 | C-16 compact range register | PASS (Phase 0) | PASS (pre-assigned) | **CONDITIONAL (range vs. individual FIDs)** | PASS (5 labeled slots) | C-16 strict scorer; C-12 FID risk | 97.8–100 |
| V-04 | C-16 full + C-17 formula + C-13 + C-15 | PASS | PASS | **PASS (full table)** | **PASS (formula declared)** | C-12 FID risk (low-mod) | 98.9–100 |
| V-05 | All criteria, conversational phrasing | PASS | PASS | **PASS (full table)** | **PASS (prose formula)** | C-12 FID risk; C-17 nuance vs. V-04 | 98.9–100 |

**Predicted ranking**: V-04 >= V-01 >= V-05 > V-03 >> V-02.

- **V-04** is the R4 100-target: explicit formula declaration + full preamble register closes the
  final C-16/C-17 ambiguity. Only C-12 FID-syntax risk remains, and it is low-to-moderate.
- **V-01** is equivalent except it lacks the explicit "SLOT COUNT = PHASE COUNT" formula in V-02
  style. Predicted same score but C-17 enforcement is template-positional (5 labeled slots)
  rather than arithmetically declared.
- **V-05** tests whether phrasing register matters. Expected to score within 1 point of V-04;
  the gap (if any) lives in C-17 strictness.
- **V-03** tests the minimal register boundary. If compact range passes C-16, it is a cleaner
  design choice for future skill maintenance. If it fails, V-01/V-04 are the confirmed minimum.
- **V-02** isolates C-17 explicitly but makes no progress on C-13/C-15/C-16. Validates the
  slot-count formula mechanism in isolation.

**R4 structural thesis**: C-16 requires a distinct document section before any evidence heading
(not just inline FID tags within phase sections). C-17 is strengthened by declaring the
slot-count equality as an arithmetic formula, not just counting to 5. V-04 applies both
mechanisms simultaneously — the template enforces all 9 aspirational criteria by position
and declaration, not by analyst recall.
