Written to `simulations/quest/rubrics/campaign-blueprint-rubric-v3-2026-03-16.md`.

**What changed in v3:**

Two new aspirational criteria extracted from R2 patterns:

**C-15 — Artifact contract** (5 pts): READ/WRITE/PRESERVE/CARRIES FORWARD declared before execution. Strongest C-06/C-07 enforcement seen in two rounds — PRESERVES makes spec-respect explicit; CARRIES FORWARD makes pitch anchoring structurally required rather than implied. Partial credit when a field type is missing.

**C-16 — Post-execution FINDINGS block** (5 pts): The R2 diagnostic answer codified as a criterion. Label and post-execution placement are structural requirements. Both V-02 (checklist) and V-05 (BEFORE WRITING) earn PARTIAL when semantic content is present — the mechanism of reflection matters, not just the content. Clarifies the C-09/C-13 relationship: C-09 can be satisfied without C-16; C-13 requires C-16's block structure to earn full credit.

**Scale updates:**
- Aspirational total: 10 → 20
- Base ceiling: 100 → 110
- Full ceiling: 118 (110 + 8 excellence bonus)
paign opens with setup summary, closes with package summary | 10 |

**Recommended total: 30**

---

### Aspirational

| ID | Criterion | Weight |
|----|-----------|--------|
| C-09 | Narrative arc — each artifact amplifies conviction without repeating content | 5 |
| C-10 | Scout signal pull is visible in the artifact that benefits from it | 5 |
| C-15 | Artifact contract — each artifact declares READ / WRITE / PRESERVE / CARRIES FORWARD before execution begins | 5 |
| C-16 | Post-execution FINDINGS block — pitch contains a labeled FINDINGS block written after the artifact, not a pre-execution intent declaration or checklist | 5 |

**Aspirational total: 20**

---

### Excellence Signals — added in v2

These criteria emerged from Round 1 analysis. They distinguish the 90+
performers from the passing tier. Scored as a bonus above the 110-pt base.

| ID | Criterion | Weight |
|----|-----------|--------|
| C-11 | Hard GATE per transition — explicit "do not begin [next artifact] until [this file] is written to disk" at both transitions | 2 |
| C-12 | Proactive scout inventory — setup phase globs simulations/scout/ and lists found signals before Artifact 1 begins; not conditional | 2 |
| C-13 | Conviction audit in pitch — FINDINGS block explicitly asks "what conviction does this version add that the previous artifacts did not" AND "note any content you nearly duplicated" | 2 |
| C-14 | Signal consumption log — campaign close records per artifact which scout namespace was consumed, not just artifact paths | 2 |

**Excellence bonus: 8**
**Scale: 110 base + 8 excellence = 118 ceiling**

---

## Scoring

```
Essential    = sum of passed essential criteria × 12        (max 60)
Recommended  = sum of passed/partial recommended × weight   (max 30)
Aspirational = sum of passed/partial aspirational × weight  (max 20)
Excellence   = sum of passed excellence signals × 2        (max 8, bonus)

Composite = Essential + Recommended + Aspirational + Excellence
```

PARTIAL = 50% of the criterion weight.

---

## Golden Threshold

**Pass**: All 5 essential criteria pass **AND** composite >= 80

Failure on any essential criterion disqualifies regardless of composite score.

---

## Failure Patterns

| Pattern | Criteria at risk |
|---------|-----------------|
| Partial campaign (missing artifact) | C-01, C-02 |
| Topic drift across artifacts | C-03 |
| Out-of-order contamination | C-04 |
| Thin sub-artifact (missing required sections) | C-05 |
| Proposal re-opens spec decisions | C-06 |
| Pitch not anchored to recommended option | C-07 |
| No campaign framing (no setup, no close) | C-08 |
| Repetition without conviction build | C-09 |
| Scout signals cosmetic or absent | C-10 |
| Soft ordering language instead of GATE | C-11 |
| Scout inventory conditional or deferred | C-12 |
| Pitch lacks conviction audit | C-13 |
| Campaign close has no per-artifact signal record | C-14 |
| Inter-artifact obligations implicit rather than declared | C-15 |
| Conviction reflection pre-execution or unlabeled | C-16 |

---

## Criterion Detail

### C-01: All three artifacts produced

All three sub-skills must run and produce output: draft-spec, draft-proposal,
draft-pitch. Two out of three fails this criterion regardless of artifact
quality.

### C-02: Canonical paths

- spec:     `simulations/draft/specs/{topic}-spec-{date}.md`
- proposal: `simulations/draft/proposals/{topic}-proposal-{date}.md`
- pitch:    `simulations/draft/pitches/{topic}-pitch-{date}.md`

Abbreviated, renamed, or wrong-directory paths fail this criterion.

### C-03: Topic identity consistency

A shared identity contract — feature name, audience, problem — must be
established once and held by all three artifacts. Artifacts that each define
the topic independently risk drift. The best implementations lock identity
in a dedicated setup phase before Artifact 1 begins (see also C-12).

### C-04: Execution order

Proposal must be grounded in the spec. Pitch must be anchored to the
proposal's recommended option. Forward references — pitch language that
pre-supposes spec content before the spec is written — fail this criterion.
Soft dependency language ("grounded in," "read the spec") passes C-04.
Explicit GATE language is scored separately as C-11.

### C-05: Minimum structure per sub-artifact

- **Spec**: PURPOSE / REQUIREMENTS / DESIGN / CONSTRAINTS / OPEN QUESTIONS
- **Proposal**: Three options minimum + do-nothing baseline; each option with
  description, pros, cons, risk, effort; recommendation with three reasons
  grounded in spec decisions
- **Pitch**: Three versions (exec / dev / maker); each with Hook / What / Why /
  CTA; shared anti-positioning section

All sub-conditions within each artifact must be present for a full PASS.

### C-06: Proposal respects spec

Recommendation reasons must trace to spec decisions or constraints. The
proposal must not re-open design questions the spec resolved or introduce
new design work. Explicit instruction ("do not re-open anything the spec
resolved") earns full credit; reasoning that happens to be grounded but lacks
the instruction is PARTIAL. The artifact contract PRESERVES declaration (C-15)
is the strongest formulation of this criterion seen in two rounds.

### C-07: Pitch crystallizes recommended option

All three sub-conditions must pass for full credit:
- Exec version: leads with outcome of the recommended option
- Dev version: explicitly references the technical design from the spec
- Maker version: plain language only — no spec terminology, no proposal jargon

Missing or implicit dev-version spec reference is the most common partial.
The artifact contract CARRIES FORWARD declaration (C-15) makes this criterion
structurally enforced rather than implied.

### C-08: Campaign framing

- **Open**: Names the topic and states which artifacts will be produced
- **Close**: Lists all three artifact paths, scout signals consumed, open
  questions

A close that lists artifacts but omits signal consumption is PARTIAL (see
C-14 for the excellence version of this criterion).

### C-09: Narrative arc (aspirational)

Each artifact advances the audience's conviction without rehashing prior
content. Role differentiation (spec → proposal → pitch) is a natural scaffold
but is not sufficient alone — the criterion requires either explicit scope
separation language or an anti-duplication instruction. The post-execution
FINDINGS block (C-16) is the primary implementation mechanism; the conviction
audit content (C-13) is the excellence version.

### C-10: Scout signal pull (aspirational)

Scout signals must be visibly pulled into the artifact that benefits from them:
- scout-requirements → spec
- scout-feasibility → proposal
- scout-positioning → pitch

Cosmetic mention without integration is PARTIAL. A conditional pull ("if
scout signals exist...") passes C-10 but does not satisfy C-12.

---

### C-15: Artifact contract (aspirational) — new in v3

Before execution begins, each artifact declares its obligations as a formal
contract with four fields:

- **READ**: which prior artifact(s) and scout signals this artifact consumes
- **WRITE**: canonical path and required sections this artifact produces
- **PRESERVE**: spec decisions this artifact must not re-open or contradict
- **CARRIES FORWARD**: content or decisions subsequent artifacts must inherit

A contract that includes all four fields for all three artifacts earns full
credit. A contract present but missing one field type (e.g., no CARRIES
FORWARD) is PARTIAL. Narrative instructions that imply the same obligations
without declaring them as a contract do not satisfy C-15.

This is the strongest C-06 and C-07 formulation observed across Rounds 1 and
2. PRESERVES enforces spec-respect explicitly; CARRIES FORWARD makes pitch
anchoring structurally required rather than implied.

### C-16: Post-execution FINDINGS block (aspirational) — new in v3

The pitch must close with a labeled FINDINGS block that is post-execution:
written after the artifact is produced, not declared before it.

The FINDINGS label and post-execution placement are structural requirements.
Two common variations that do not satisfy C-16:
- **Pre-execution intent declaration** ("BEFORE WRITING — conviction
  architecture"): asks the right questions but pre-supposes the artifact
  rather than reflecting on it. Earns PARTIAL.
- **Pre-flight checklist items**: contain the right semantic content but as
  verification boxes, not as narrative reflection. Earns PARTIAL.

Both variations earn PARTIAL (2.5 pts) when the semantic content of the
conviction audit is present. A labeled FINDINGS block with both conviction
questions post-execution earns full credit (5 pts).

Relationship to other criteria:
- C-09 (aspirational): whether narrative separation exists — BEFORE WRITING
  and checklist formats can satisfy C-09 without satisfying C-16
- C-13 (excellence): what the FINDINGS block asks — requires C-16's block
  structure to be in place to earn full credit

---

### C-11: Hard GATE per transition (excellence)

Each artifact transition must contain explicit blocking language:
- "Do not begin [Artifact 2] until [Artifact 1] is written to disk."
- "Do not begin [Artifact 3] until [Artifact 2] is written to disk."

Both gate statements must be present. Soft dependency language ("grounded
in the spec just written," "read the proposal") passes C-04 but does not
satisfy C-11. Full credit requires both transitions gated; one gate only
is PARTIAL (1 pt).

### C-12: Proactive scout inventory (excellence)

The setup phase — before Artifact 1 begins — must proactively glob
`simulations/scout/` and list found signals by namespace. The inventory
must be executed unconditionally, not gated on signal existence. A
conditional pull passes C-10 but does not satisfy C-12.

### C-13: Conviction audit (excellence)

The pitch FINDINGS block (C-16) must contain two explicit checks stated
as instructions:
1. "State what conviction this version establishes that the previous
   artifacts did not."
2. "Note any content you nearly duplicated from spec or proposal."

A strong narrative inertia thread (C-09) is not sufficient. The audit must
be written as a named instruction the executor follows. Missing either check
is PARTIAL (1 pt). Note: C-13 requires the post-execution FINDINGS structure
established by C-16 — a pre-execution block or checklist containing both
questions earns C-13 PARTIAL regardless of content quality.

### C-14: Signal consumption log (excellence)

The campaign close section must record, per artifact, which scout signal
namespace was consumed — not merely list artifacts or list signals. A table
or structured list with columns for artifact path + signal namespace consumed
satisfies this criterion. A close that names signals globally (not per
artifact) is PARTIAL (1 pt).

---

## Round 1 Calibration

| Variant | Composite (v2) | Golden |
|---------|---------------|--------|
| V-03 — Lifecycle Emphasis | ~106 | Yes |
| V-01 — Role Sequence | ~95 | Yes |
| V-05 — Full Integration | ~104 | Yes |
| V-04 — Register + Inertia | ~82 | No (C-03, C-05 essential partial) |
| V-02 — Output Format | ~79 | No (C-03 essential partial, C-09 fail) |

Excellence signal pattern: V-03 leads on C-11/C-12/C-13; V-05 leads on
C-14. No single variant in Round 1 fully satisfies all four.

---

## Round 2 Calibration

| Variant | Base | Excellence | Total | Golden |
|---------|------|------------|-------|--------|
| V-01 — Artifact Contract | 100 | +8 | **108** | Yes |
| V-02 — Pre-flight Checklist | 97.5 | +7 | **104.5** | Yes |
| V-03 — Minimal Density | 100 | +8 | **108** | Yes |
| V-04 — Lifecycle + Conviction Merge | 100 | +8 | **108** | Yes |
| V-05 — Pre-execution Conviction | 100 | +7 | **107** | Yes |

All five are Golden. R2 resolved both R1 excellence gaps — three variants hit 108.

**R2 diagnostic finding**: C-13 requires the FINDINGS label and post-execution
placement. V-02 (checklist) and V-05 (BEFORE WRITING) both had correct semantic
content but earned PARTIAL. Pre-execution conviction architecture and structural
checklists are not substitutes for post-execution FINDINGS reflection. This
finding is codified as C-16.

**New patterns promoted to aspirational**:
- C-15 (Artifact contract): V-01's READ/WRITE/PRESERVE/CARRIES FORWARD
  mechanism. Strongest C-06/C-07 enforcement in two rounds.
- C-16 (Post-execution FINDINGS): label and placement are structural, not
  semantic. Closes the C-09/C-13 gap for pre-execution conviction architectures.

Note: Round 2 scores above reflect the v2 rubric (110-pt base scale introduced
in v3). Retroactive v3 scoring would add up to 10 pts for C-15/C-16.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial — 5 essential, 3 recommended, 2 aspirational; 100-pt scale |
| v2 | 2026-03-16 | Added C-11–C-14 excellence signals from Round 1 scorecard; 108-pt ceiling; calibration table added |
| v3 | 2026-03-16 | Added C-15 (artifact contract) and C-16 (post-execution FINDINGS) as aspirational from Round 2 patterns; aspirational total 10→20; base ceiling 100→110; 118-pt ceiling; R2 calibration added |
