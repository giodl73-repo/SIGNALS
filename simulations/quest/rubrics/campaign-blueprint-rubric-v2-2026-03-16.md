Reading the scorecard to extract the 4 excellence patterns before writing.

The four patterns that consistently separated V-03 (100) and V-05 from the failing variants:

1. **C-11** — Hard GATE language per transition (V-03/V-05 both; V-01 uses soft "grounded in" dependency)
2. **C-12** — Proactive scout inventory in setup phase (not conditional — V-03/V-05 glob before Artifact 1)
3. **C-13** — Conviction audit in pitch FINDINGS (V-03 explicit; V-05 partial — has inertia thread but no "note near-duplication" check)
4. **C-14** — Signal consumption log in campaign close (V-05 explicit per-artifact table; V-03 lists namespaces but not per-artifact)

Adding these as an **Excellence Signals** tier worth 2 pts each (8 pt bonus), keeping the 100-pt base scale and golden threshold unchanged.

```markdown
# Campaign Blueprint Rubric — v2

**Skill**: campaign-blueprint
**Version**: v2
**Updated**: 2026-03-16
**Based on**: Round 1 scorecard — V-01 through V-05

---

## Purpose

Evaluates whether a campaign-blueprint skill execution correctly coordinates
three sub-artifacts (spec, proposal, pitch) into a coherent decision package.

---

## Criteria

### Essential — all must pass

| ID | Criterion | Weight |
|----|-----------|--------|
| C-01 | All three artifacts produced (spec + proposal + pitch present) | 12 |
| C-02 | Each written to its canonical path | 12 |
| C-03 | Consistent topic identity across all three | 12 |
| C-04 | Execution order respected (spec → proposal → pitch, no forward refs) | 12 |
| C-05 | Each sub-artifact meets its own minimum structure | 12 |

**Essential total: 60**

---

### Recommended

| ID | Criterion | Weight |
|----|-----------|--------|
| C-06 | Proposal reflects spec decisions, no re-invention | 10 |
| C-07 | Pitch crystallizes the proposal's recommended option | 10 |
| C-08 | Campaign opens with setup summary, closes with package summary | 10 |

**Recommended total: 30**

---

### Aspirational

| ID | Criterion | Weight |
|----|-----------|--------|
| C-09 | Narrative arc — each artifact amplifies conviction without repeating content | 5 |
| C-10 | Scout signal pull is visible in the artifact that benefits from it | 5 |

**Aspirational total: 10**

---

### Excellence Signals — new in v2

These criteria emerged from Round 1 analysis. They distinguish the 90+
performers from the passing tier. Scored as a bonus above the 100-pt base.

| ID | Criterion | Weight |
|----|-----------|--------|
| C-11 | Hard GATE per transition — explicit "do not begin [next artifact] until [this file] is written to disk" at both transitions | 2 |
| C-12 | Proactive scout inventory — setup phase globs simulations/scout/ and lists found signals before Artifact 1 begins; not conditional | 2 |
| C-13 | Conviction audit in pitch — FINDINGS block explicitly asks "what conviction does this version add that the previous artifacts did not" AND "note any content you nearly duplicated" | 2 |
| C-14 | Signal consumption log — campaign close records per artifact which scout namespace was consumed, not just artifact paths | 2 |

**Excellence bonus: 8**
**Scale: 100 base + 8 excellence = 108 ceiling**

---

## Scoring

```
Essential    = sum of passed essential criteria × 12        (max 60)
Recommended  = sum of passed/partial recommended × weight   (max 30)
Aspirational = sum of passed/partial aspirational × weight  (max 10)
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
the instruction is PARTIAL.

### C-07: Pitch crystallizes recommended option

All three sub-conditions must pass for full credit:
- Exec version: leads with outcome of the recommended option
- Dev version: explicitly references the technical design from the spec
- Maker version: plain language only — no spec terminology, no proposal jargon

Missing or implicit dev-version spec reference is the most common partial.

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
separation language or an anti-duplication instruction. The conviction audit
(C-13) is the excellence implementation of this criterion.

### C-10: Scout signal pull (aspirational)

Scout signals must be visibly pulled into the artifact that benefits from them:
- scout-requirements → spec
- scout-feasibility → proposal
- scout-positioning → pitch

Cosmetic mention without integration is PARTIAL. A conditional pull ("if
scout signals exist...") passes C-10 but does not satisfy C-12.

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

The pitch FINDINGS block (or its equivalent closure section) must contain
two explicit checks stated as instructions:
1. "State what conviction this version establishes that the previous
   artifacts did not."
2. "Note any content you nearly duplicated from spec or proposal."

A strong narrative inertia thread (C-09) is not sufficient. The audit must
be written as a named instruction the executor follows. Missing either check
is PARTIAL (1 pt).

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
| V-03 — Lifecycle Emphasis | ~106 | ✓ |
| V-01 — Role Sequence | ~95 | ✓ |
| V-05 — Full Integration | ~104 | ✓ |
| V-04 — Register + Inertia | ~82 | ✗ (C-03, C-05 essential partial) |
| V-02 — Output Format | ~79 | ✗ (C-03 essential partial, C-09 fail) |

Excellence signal pattern: V-03 leads on C-11/C-12/C-13; V-05 leads on
C-14. No single variant in Round 1 fully satisfies all four.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial — 5 essential, 3 recommended, 2 aspirational; 100-pt scale |
| v2 | 2026-03-16 | Added C-11–C-14 excellence signals from Round 1 scorecard; 108-pt ceiling; calibration table added |
```

---

Four patterns extracted and promoted to C-11 through C-14:

- **C-11 (GATE)** — hard blocking language at both transitions, not soft dependency phrasing. V-03/V-05 both had it; V-01 only had "grounded in."
- **C-12 (Scout inventory)** — unconditional pre-flight glob in setup. Distinguishes from C-10 (conditional pull passing is fine for C-10; C-12 requires execution, not optionality).
- **C-13 (Conviction audit)** — V-03's explicit "state what conviction this version adds + note near-duplication" instruction. V-05 partial because it had the inertia thread but not the named check.
- **C-14 (Consumption log)** — V-05's per-artifact signal record in the close table. V-03 listed namespaces globally; C-14 requires per-artifact attribution.

No variant in Round 1 satisfies all four — the ceiling is open for Round 2.
