---
skill: quest-variate
skill_target: campaign-decide
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v2-2026-03-16.md
---

# Variations — campaign-decide / Round 2

Five complete, runnable skill body variations targeting the v2 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R1 diagnosis driving R2 axis choices:**

| R1 variation | v2 score | Failure mode |
|--------------|----------|--------------|
| V-01 (inertia framing) | 60 | Passed all essential; C-11/C-12 absent |
| V-02 (table-driven) | 100 | Gold — per-phase tables + `because Phase N` prescribed syntax |
| V-03 (conversational) | 53 | No section structure; C-11/C-12 absent |
| V-04 (lifecycle + inertia) | ~80 est. | Gates present; C-12 citation format not prescribed |
| V-05 (citation rules) | ~80 est. | Rules named; C-11 per-phase schema not enforced |

**R2 targets C-11 and C-12 directly.** Every variation must make a structural commitment to
per-phase schemas (C-11) and templated citation syntax (C-12). Axes vary *how* those commitments
are expressed, not *whether* they appear.

---

## V-01 — Axis: Per-phase schema format (named-field rows)

**Hypothesis**: Named-field rows (`Field: [value]`) achieve C-11 without markdown table
rendering dependency. A model that degrades table alignment under context pressure may still
produce correctly labeled fields. The `Because Phase N, field` pattern in Phase 6 prescribes
the citation format needed for C-12 without requiring table column headers.

```
Run the full pre-commitment decision campaign for: {{topic}}

Execute the six sub-skills below in order. Each phase MUST produce every listed required
field. An incomplete field means the phase is incomplete — do not advance.

---

## Phase 1 — scout-competitors

Inertia — status-quo cost: [why people pay the hidden cost of staying put]
Inertia — switching cost: [what a user loses by changing to any alternative]
Inertia — good-enough threshold: [conditions under which the current approach feels acceptable]
Rival 1 — name: [name] | type: named | threat: [Low/Medium/High] | notes: [one sentence]
Rival 2 — name: [name] | type: named | threat: [Low/Medium/High] | notes: [one sentence]

Ordering rule: all Inertia fields must appear before any Rival fields.

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
Primary segment: [name] | justification: [one sentence explaining priority]

---

## Phase 4 — prove-hypothesis

Claim: [one falsifiable sentence — what must be true for this to be worth building]
Falsification condition: [what evidence would disprove this claim]
Confidence prior: [Low/Medium/High] — [reason for prior before seeing external evidence]
Experiment 1: [name and method]
Experiment 2: [name and method]

---

## Phase 5 — prove-websearch

[Repeat the block below for each source — minimum 3 sources]

Source: [URL or publication citation]
Quote: "[direct quote — not paraphrase]"
Strength: [Weak/Moderate/Strong]
Verdict: [Supports/Refutes/Neutral]

---

## Phase 6 — prove-synthesize

Hypothesis outcome: [Confirmed/Refuted/Inconclusive]
Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
Confidence: [High/Medium/Low]
Confidence rationale: [name the specific findings or gaps that drove the rating — not just the label]

Because (required, cite by Phase and field):
- [claim] because Phase 1, [inertia or rival field]
- [claim] because Phase 2, [feasibility field]
- [claim] because Phase 3, [market field]
- [claim] because Phase 4/5, [hypothesis or source field]

Counter-evidence: [one risk or caveat that could undermine the recommendation]
Next step: [COMMIT → concrete action, not "do more research" | no-build → exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (named-field ordering rule enforces inertia-first by construction),
C-05 (Phase 6 "Because Phase N, field" pattern forces traceability), C-06 (section headers),
C-07 (counter-evidence field required), C-08 (hypothesis outcome field), C-09 (confidence
rationale field), C-10 (conditioned next step), C-11 (named-field schema per phase — every
phase has listed required fields), C-12 ("Because Phase N, [field name]" is a prescribed format).

**Risk**: Strict C-11 scorers may expect markdown table rows rather than labeled fields. If
"required named rows" means table rows specifically, named fields may score C-11 as partial
rather than full. The Phase 6 citation format `because Phase N, [field]` differs slightly from
the rubric example `because Phase N, [section reference]` — likely equivalent but worth flagging.

---

## V-02 — Axis: Role sequence (hypothesis-first)

**Hypothesis**: Opening with prove-hypothesis forces a falsifiable commitment before any
competitive or market data is gathered. Scouting phases become hypothesis-tests rather than
free-form scans — every Phase 2-5 row is interpreted through the Phase 1 claim. Synthesis
in Phase 6 then reports hypothesis disposition as a true outcome, not a post-hoc framing.
This should improve C-08 (hypothesis disposition explicit) because the hypothesis is the
anchor everything else references.

```
Run the full pre-commitment decision campaign for: {{topic}}

STATE YOUR BELIEF FIRST, THEN GATHER EVIDENCE. Evidence gathered in Phases 2-5 tests the
Phase 1 hypothesis — it does not build a case for a predetermined conclusion.

Execute in order:

---

## Phase 1 — prove-hypothesis [ANCHOR]

Before any scouting: state the core claim.

| Field | Value |
|-------|-------|
| Claim | [one falsifiable sentence — what must be true for this to be worth building] |
| Falsification condition | [what evidence would kill this hypothesis] |
| Confidence prior | [Low / Medium / High] |
| Prior rationale | [why you hold this prior before seeing external evidence] |
| Experiment 1 | [name and method] |
| Experiment 2 | [name and method] |

---

## Phase 2 — scout-competitors

Competitive evidence bearing on the Phase 1 claim.

| Force | Type | Strength (1-5) | Hypothesis impact |
|-------|------|----------------|-------------------|
| Inertia / status quo | inertia | | How it affects the Phase 1 claim |
| Switching cost | inertia | | What users lose by changing |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must precede named rival rows.)

---

## Phase 3 — scout-feasibility

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

Top risk: [single biggest buildability threat]

---

## Phase 4 — scout-market

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |

Primary target segment: [name] — [justification]

---

## Phase 5 — prove-websearch

External evidence testing the Phase 1 claim.

| Source | Direct Quote | Strength | Verdict |
|--------|--------------|----------|---------|
| | "[direct quote]" | Weak / Moderate / Strong | Supports / Refutes / Neutral |

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

Because (cite by Phase):
- [claim] because Phase 1, [hypothesis field]
- [claim] because Phase 2, [competitive force row]
- [claim] because Phase 3, [feasibility dimension]
- [claim] because Phase 4, [segment finding]
- [claim] because Phase 5, [source finding]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (inertia rows first in Phase 2 table), C-05 (Phase 6 because-citations),
C-06 (section headers per phase), C-07 (counter-evidence table row), C-08 (hypothesis outcome row in
Phase 6 table), C-09 (confidence rationale row), C-10 (conditioned next step row), C-11 (table schema
per phase), C-12 (prescribed "because Phase N, [field/row]" format).

**Risk**: C-03 requires "all six sub-skill domains represented." All six are present but in
non-standard order (prove-hypothesis is Phase 1, not Phase 4). A strict scorer checking for the
canonical sequence could flag this; a scorer checking for presence should pass it. The "Hypothesis
impact" column in Phase 2 table may produce shallow entries if the model hasn't yet formed a view
on how each competitive force relates to the anchor claim.

---

## V-03 — Axis: Citation anchor format (finding-ID system)

**Hypothesis**: Assigning each key claim a finding ID in the format `F[phase]-[seq]` (e.g.,
`F1-01`, `F3-02`) creates citations that pin to a specific row, not just a section. "Because
F1-01" is more precise than "because Phase 1, inertia section" when Phase 1 contains multiple
inertia rows. The FID format is a prescribed template — it should satisfy C-12's "mechanically
auditable" requirement while making C-05 trivially checkable by ID lookup.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING-ID PROTOCOL: As you produce evidence, each key claim receives a finding ID in the
format F[phase]-[sequence] (e.g., F1-01, F2-03). The recommendation section must cite by
finding ID. "Because F1-01" is auditable. "As shown above" or "based on the evidence" are not.

Execute in order:

---

## Phase 1 — scout-competitors

| FID | Force | Type | Strength (1-5) | Notes |
|-----|-------|------|----------------|-------|
| F1-01 | Inertia / status quo | inertia | | Why people don't change |
| F1-02 | Switching cost | inertia | | What users lose by changing |
| F1-03 | [Named Rival A] | named | | |
| F1-04 | [Named Rival B] | named | | |

(F1-01, F1-02 inertia rows must precede F1-03+ named rival rows.)

---

## Phase 2 — scout-feasibility

| FID | Dimension | Rating (R/Y/G) | Notes |
|-----|-----------|----------------|-------|
| F2-01 | Technical complexity | | |
| F2-02 | Team capability | | |
| F2-03 | Timeline | | |
| F2-04 | Cost | | |

Top risk — F2-05: [name the single biggest buildability threat]

---

## Phase 3 — scout-market

| FID | Segment | Est. Size | Fit Score (1-10) | Priority |
|-----|---------|-----------|-----------------|----------|
| F3-01 | | | | |
| F3-02 | | | | |

Primary segment — F3-03: [name] — [justification]

---

## Phase 4 — prove-hypothesis

F4-01  Claim: [one falsifiable sentence]
F4-02  Falsification condition: [what would disprove this]
F4-03  Confidence prior: [Low/Medium/High] — [reason]
F4-04  Experiment 1: [name and method]
F4-05  Experiment 2: [name and method]

---

## Phase 5 — prove-websearch

| FID | Source | Direct Quote | Strength | Verdict |
|-----|--------|--------------|----------|---------|
| F5-01 | | "[direct quote]" | Weak/Moderate/Strong | Supports/Refutes/Neutral |
| F5-02 | | "[direct quote]" | | |
| F5-03 | | "[direct quote]" | | |

---

## Phase 6 — prove-synthesize

Hypothesis outcome: [Confirmed/Refuted/Inconclusive]
Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
Confidence: [High/Medium/Low]
Confidence rationale: [name the specific findings — cite by FID — that drove this rating]

Because (required, cite by FID):
- [claim] because [FID]
- [claim] because [FID]
- [claim] because [FID]

Counter-evidence: [one risk or caveat — cite the finding it qualifies, by FID]
Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-03 (FID-prefixed row per domain forces all six to be populated),
C-04 (FID ordering rule: F1-01/F1-02 before F1-03+), C-05 (FID citations make traceability
lookup-based), C-11 (FID-prefixed rows per phase constitute a per-phase required-field schema),
C-12 ("because FID" is a prescribed citation format — more precise than Phase+section).

**Risk**: C-12 rubric example is "because Phase [N], [section reference]" not "because FID."
The rubric says "e.g." which suggests the example is not exhaustive, but a strict scorer may
require the Phase+section format. FID satisfies the spirit (mechanically auditable) but differs
in syntax. This is the primary C-12 pass risk for this variation.

---

## V-04 — Combined: Named-field schema + finding-ID citations

**Hypothesis**: Combining named-field rows (V-01's format) with finding IDs (V-03's system)
creates the most precise possible per-phase schema. Each field has both a human-readable label
and a machine-pinnable ID. The recommendation section cites by FID, making C-12 trivially
auditable — no table scanning required. Named-field format also removes markdown rendering
dependency, making this the most model-robust variation for C-11.

```
Run the full pre-commitment decision campaign for: {{topic}}

CITATION PROTOCOL: Each required field carries a finding ID in the format F[phase]-[seq].
All evidence citations in the recommendation must use the format "because F[phase]-[seq]" —
not "as shown above," "based on the evidence," or any other free-prose reference.

Execute in order:

---

## Phase 1 — scout-competitors

F1-01  Inertia — status-quo cost: [why people pay the hidden cost of staying put]
F1-02  Inertia — switching cost: [what a user loses by changing to any alternative]
F1-03  Inertia — good-enough threshold: [when the current approach feels acceptable]
F1-04  Rival 1 — name: [name] | type: named | threat: [Low/Medium/High]
F1-05  Rival 2 — name: [name] | type: named | threat: [Low/Medium/High]

Ordering rule: F1-01 through F1-03 (inertia) must be populated before F1-04+ (named rivals).

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
F4-03  Confidence prior: [Low/Medium/High] — [reason for prior before external evidence]
F4-04  Experiment 1: [name and method]
F4-05  Experiment 2: [name and method]

---

## Phase 5 — prove-websearch

[Repeat block for each source — minimum 3]

F5-[seq]  Source: [URL or citation]
          Quote: "[direct quote — not paraphrase]"
          Strength: [Weak/Moderate/Strong]
          Verdict: [Supports/Refutes/Neutral]

---

## Phase 6 — prove-synthesize

F6-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive]
F6-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F6-03  Confidence: [High/Medium/Low]
F6-04  Confidence rationale: [cite by FID the specific findings that drove the rating]

Because (required, cite by FID — minimum 4 citations spanning at least 3 phases):
- [claim] because [FID]
- [claim] because [FID]
- [claim] because [FID]
- [claim] because [FID]

F6-05  Counter-evidence: [one risk or caveat — cite the finding it qualifies, by FID]
F6-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: All 12 criteria. C-04 (F1-01 through F1-03 ordering rule is explicit).
C-05 (FID citations make every recommendation claim pinnable). C-07 (F6-05 requires citing
the finding counter-evidence qualifies). C-08 (F6-01 hypothesis outcome required). C-09
(F6-04 confidence rationale cites specific FIDs — not just a label). C-10 (F6-06 conditioned
next step). C-11 (every phase has FID-labeled required fields = per-phase schema). C-12
("because FID" is a prescribed, mechanically auditable citation format).

**Risk**: Same C-12 risk as V-03 — the rubric example uses Phase+section format; FID format
is different. Additionally, requiring "minimum 4 citations spanning at least 3 phases" is a
new constraint not in the rubric — it may produce over-cited synthesis blocks. The per-source
block structure in Phase 5 (indented under a repeating FID header) may render inconsistently
depending on context window and markdown mode.

---

## V-05 — Combined: Hypothesis-first + V-02 table structure (best-of synthesis)

**Hypothesis**: V-02 achieved 100 in R1 by having complete per-phase table schemas and the
prescribed `because Phase N, [section]` syntax. The only critique of V-02 is that evidence
phases gather data before a hypothesis is committed — synthesis can then confirm whatever the
evidence suggests rather than testing a prior belief. Combining hypothesis-first ordering
(V-02 this round) with V-02's R1 table structure and exact citation syntax should preserve
the 100-score structure while improving hypothesis-disposition quality (C-08) through the
anchor pattern.

```
Run the full pre-commitment decision campaign for: {{topic}}

STATE YOUR BELIEF FIRST. Then gather evidence. Evidence tests the hypothesis — it does not
post-hoc justify a conclusion. Execute in order.

---

## Phase 1 — prove-hypothesis [ANCHOR PHASE]

State the core claim before any scouting. All subsequent phases gather evidence that bears
on this hypothesis.

| Field | Value |
|-------|-------|
| Claim | [one falsifiable sentence — what must be true for this to be worth building] |
| Falsification condition | [what evidence would kill this hypothesis] |
| Confidence prior | [Low / Medium / High] |
| Prior rationale | [why you hold this prior before seeing evidence — name the assumption] |
| Experiment 1 | [name and method] |
| Experiment 2 | [name and method] |

---

## Phase 2 — scout-competitors

Competitive forces bearing on the Phase 1 claim.

| Force | Type | Strength (1-5) | Notes |
|-------|------|----------------|-------|
| Inertia / status quo | inertia | | Why people don't change |
| Switching cost | inertia | | What users lose by changing |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must appear before any named rival rows.)

---

## Phase 3 — scout-feasibility

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

Top risk: [single biggest buildability threat]

---

## Phase 4 — scout-market

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |

Primary target segment: [name it]

---

## Phase 5 — prove-websearch

External evidence testing the Phase 1 claim.

| Source | Direct Quote | Strength | Verdict |
|--------|--------------|----------|---------|
| | "[direct quote]" | Weak / Moderate / Strong | Supports / Refutes / Neutral |

(Minimum 3 sources.)

---

## Phase 6 — prove-synthesize

| Field | Value |
|-------|-------|
| Hypothesis outcome | [Confirmed / Refuted / Inconclusive — must match Phase 1 claim] |
| Recommendation | [COMMIT / PAUSE / PIVOT / ABANDON] |
| Confidence | [High / Medium / Low] |
| Confidence rationale | [name specific evidence gaps or strengths — not just the label] |
| Counter-evidence | [one risk or caveat that could undermine the recommendation] |
| Next step | [COMMIT: concrete action | no-build: exit condition or revisit trigger] |

Because (cite by Phase):
- [claim] because Phase 1, [hypothesis field]
- [claim] because Phase 2, [competitive force row]
- [claim] because Phase 3, [feasibility dimension]
- [claim] because Phase 4, [segment finding]
- [claim] because Phase 5, [source quote]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: All 12 criteria. C-11 via complete per-phase table schemas (exact V-02
R1 pattern). C-12 via `because Phase N, [field/row]` prescribed syntax (exact V-02 R1 pattern).
C-04 via inertia-row-first rule in Phase 2 table. C-08 via hypothesis outcome row that explicitly
references the Phase 1 claim ("must match Phase 1 claim"). C-09 via confidence rationale row.
C-10 via conditioned next step row.

**Risk**: The only structural change from V-02 R1 is (a) Phase 1 is now prove-hypothesis (not
scout-competitors), and (b) the Phase 1 table adds a "Prior rationale" row. If scorers interpret
C-03 as requiring skills to run in the canonical sequence (competitors → feasibility → market →
hypothesis → websearch → synthesis), this variation may lose C-03. Probability: low, since the
rubric says "six domains represented," not "six domains in order." The hypothesis-anchor pattern
in Phase 6's "Hypothesis outcome" row adds a linkage requirement back to Phase 1 that could
produce richer C-08 passes than V-02 R1.

---

## Variation Summary

| ID | Axes | Primary New Targets | C-11 Mechanism | C-12 Mechanism | Risk |
|----|------|--------------------|-----------------|-----------------|----|
| V-01 | Per-phase named-field schema | C-11, C-12 | Required labeled fields per phase | "Because Phase N, field" in Phase 6 | C-11 scorer may expect table rows |
| V-02 | Role sequence (hypothesis-first) | C-08 depth, C-09 depth | Table schema per phase (V-02 R1 tables) | "Because Phase N, [field/row]" | C-03 ordering interpretation |
| V-03 | Citation anchor (finding-ID) | C-12 precision, C-05 auditability | FID-prefixed rows per phase | "Because FID" prescribed format | C-12 scorer may require Phase+section format |
| V-04 | Named fields + finding-IDs | C-11 robustness, C-12 precision | FID-labeled named fields per phase | "Because FID" — minimum 4 citations | C-12 FID vs Phase format risk; Phase 5 indent rendering |
| V-05 | Hypothesis-first + V-02 R1 tables | C-08 depth via anchor linkage | Complete table schema per phase (V-02 proven) | "Because Phase N, [field/row]" exact V-02 syntax | C-03 ordering interpretation (low probability) |

**Predicted leaderboard going into quest-score**: V-05 >= V-02 > V-01 > V-04 >= V-03.

V-05 preserves V-02's R1 100-score structure exactly while improving C-08 through the anchor
pattern. V-02 (this round) reorders phases but keeps the winning table structure — should hit
100 unless C-03 is scored for ordering. V-01 hits C-11 and C-12 through named fields but has
a small scorer-interpretation risk on C-11. V-04 and V-03 share a C-12 risk from using FID
format instead of Phase+section format — likely equivalent in intent but different in syntax.
