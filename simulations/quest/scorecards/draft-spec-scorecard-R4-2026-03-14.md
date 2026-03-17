# Quest Score — `draft-spec` Round 4 (Rubric v4)

## Scoring Grid

### Essential Criteria (5 × 12 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Guided sections | PASS | PASS | PASS | PASS | PASS |
| C-02 Scout status table | PASS | PASS | PASS | PASS | PASS |
| C-03 P0 coverage | PASS | PASS | PASS | PASS | PASS |
| C-04 Self-review findings | PASS | PASS | PASS | PASS | PASS |
| C-05 Frontmatter complete | PASS | PASS | PASS | PASS | PASS |
| **Essential pts** | **60** | **60** | **60** | **60** | **60** |

All variations clear all essential criteria. Role sequence, REQUIRES/PRODUCES, and conversational registers all preserve the base scaffold.

---

### Recommended Criteria (3 × 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Secondary role validation | PASS — PM + Strategy invoked in sequence | PASS — REQUIRES declarations invoke named roles | PASS — roles named conversationally | PASS | PASS |
| C-07 Contradiction detection | PASS — PM scan phase includes R-ID collision check | PASS — PRODUCES a contradiction-finding artifact | PARTIAL — conversational detection less systematic; no R-ID pair naming confirmed | PASS | PASS |
| C-08 Actionable amendment list | PASS | PASS | PASS | PASS | PASS |
| **Recommended pts** | **30** | **30** | **20** | **30** | **30** |

V-03 loses C-07: conversational phrasing reduces detection to narrative description; "R-06 vs R-10" ID-pair naming isn't confirmed in register.

---

### Aspirational Criteria (11 × 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 No-scout fallback | PASS — scripted block present (C-18 implies C-09) | PASS | PASS | PASS | PASS |
| C-10 Cross-namespace coherence | PASS — PM scan surfaces feasibility/compliance traces | PASS — REQUIRES names cross-NS artifact | PASS | PASS | PASS |
| C-11 Pre-printed CNS column | PASS — two-step CNS placement implies structural column in Purpose | PASS — PRODUCES declaration creates structural slot | FAIL — conversational "name the artifact" instruction ≠ pre-printed column | PASS | PASS |
| C-12 Role annotations inline | PASS — PM→Strategy→Architect sequence embeds annotations within target sections | FAIL — REQUIRES/PRODUCES roles declared at phase level, not inline within section content block | PASS — conversational register naturally embeds inline | PASS — role-sequence axis satisfies inline; PRODUCES axis provides structure | PASS |
| C-13 Per-row P0 status column | PASS — PM coverage pre-assignment (C-16) produces per-row rows with named entries | PASS — PRODUCES creates per-row output table with spec-entry names | FAIL — conversational tables lack rigidly enforced per-row naming | PASS | PASS |
| C-14 Active inspection guard | FAIL — PM-SCAN-GATE is phase-level; no field-level named blank or scan instruction | PASS — REQUIRES names the data source to inspect before confirming absence | PASS — `[SCAN REQUIRED]` inline cues are field-level | PASS — REQUIRES (from V-02 axis) + role-ordered scan (from V-01 axis) cover both levels | PASS — extended to per-IG-ID fields |
| C-15 CNS in two independent locations | PASS — "two-step CNS placement" names independent template slots; C-19 confirms deliberateness | PASS — A-of-2/B-of-2 slot labels in REQUIRES chain name two structurally independent slots | FAIL — "entry 1/2 / entry 2/2" labels may co-occur within same section; structural independence not confirmed | PASS | PASS |
| C-16 PM-first coverage pre-assignment | PASS — strict PM→Architect ordering assigns requirements before any prose | PASS — PRODUCES pre-fills PM-assignment rows; Architect receives pre-written cells | FAIL — PM-first pre-assignment not explicit in conversational register | PASS | PASS |
| C-17 Named gate token | PASS — `[PM-SCAN-GATE]` | PASS — `[DISCOVERY-TABLE]` via PRODUCES declaration | PASS — `✓ SCOUT SCAN SEALED` | PASS — PRODUCES + **token validity rule**: gate declared without scan evidence is invalid | PASS — adds `[INERTIA-ANALYZED]` for TYPE E |
| C-18 Scripted verbatim fallback | PASS — `write: "..."` block in Phase 1 | PASS — `respond: "..."` as PRODUCES of NOT FOUND branch | PASS — `respond: "..."` quoted block | PASS — `write: "..."` as PRODUCES of NOT FOUND branch | PASS |
| C-19 Ordinal location markers | PASS — "location 1 of 2 / 2 of 2" | PASS — "[slot A-of-2] / [slot B-of-2]" | PASS — "entry 1/2 / entry 2/2" | PASS — "location 1 of 2 / 2 of 2" | PASS — extended to IG-ID column |
| **Asp pass/11** | **10** | **10** | **7** | **11** | **11** |
| **Asp pts** | **50** | **50** | **35** | **55** | **55** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** | Golden? |
|-----------|-----------|-------------|--------------|---------------|---------|
| V-01 | 60 | 30 | 50 | **140** | Yes |
| V-02 | 60 | 30 | 50 | **140** | Yes |
| V-03 | 60 | 20 | 35 | **115** | No — C-07 fail; 5 asp fails |
| V-04 | 60 | 30 | 55 | **145** | Yes |
| V-05 | 60 | 30 | 55 | **145** | Yes |

---

## Rankings

| Rank | Variation | Score | Gap from top |
|------|-----------|-------|--------------|
| 1T | V-04 | 145 | — |
| 1T | V-05 | 145 | — |
| 3T | V-01 | 140 | -5 |
| 3T | V-02 | 140 | -5 |
| 5 | V-03 | 115 | -30 |

---

## Why V-04 / V-05 Clear the Last Gap

V-01 and V-02 each miss exactly one criterion:

- **V-01 fails C-14** — PM-SCAN-GATE is a phase-level proof mechanism, not a field-level inspection guard. There is no named blank requiring "R-XX vs R-YY" format or a `REQUIRES: [scan source]` declaration per field.
- **V-02 fails C-12** — REQUIRES/PRODUCES role declarations appear at phase headers, not embedded inline within the section content block. An axis declaration at phase top does not satisfy "inline within its target section in the same content block."

V-04 combines both axes: the role-sequence axis places roles inline with their target sections (fixing V-02's C-12 gap); the REQUIRES/PRODUCES axis names data sources field-by-field (fixing V-01's C-14 gap). The lifecycle-emphasis axis adds the **token validity rule**: a gate token emitted without its prerequisite scan evidence is structurally invalid — this upgrades C-17 from "gate artifact must appear" to "gate artifact must prove it earned its presence."

V-05 inherits all of V-04 and adds a parallel finding surface: IG-IDs (inertia-guard IDs) receive the same treatment as R-IDs — elimination-paths, an AMPLIFIED risk signal when the NS column shows feasibility < 70 or any blocking compliance requirement, a TYPE E finding category, and a dedicated `[INERTIA-ANALYZED]` gate token. This doesn't score on the existing 19 criteria but surfaces candidate C-20.

---

## Excellence Signals (top-scoring variation)

**From V-04 (three-axis combination):**

1. **Axis complementarity is the unlock** — no single axis achieves 145; V-01 has inline roles but weak field-level inspection; V-02 has structured REQUIRES but phase-level roles; combining them eliminates each other's residual gap
2. **Token validity rule elevates C-17 semantics** — the gate token becomes self-invalidating if declared without its prerequisite scan block; this transforms a structural-presence check into a proof-of-work check
3. **REQUIRES declarations double as C-14 field guards** — naming the data source in a REQUIRES block satisfies the active-inspection criterion without a separate `[SCAN REQUIRED]` cue; one structural element satisfies two criteria

**From V-05 (unique contribution):**

4. **Parallel finding namespace via IG-IDs** — treating inertia-guard hypotheses as first-class named entities (IG-01, IG-02…) creates a finding surface isomorphic to R-IDs; each IG-ID gets an elimination-path, an AMPLIFIED flag, and its own gate token — this pattern could apply to any named enumerable risk class beyond inertia
5. **Risk amplification via cross-namespace NS column** — feasibility score and compliance posture feed a per-IG-ID risk signal rather than being consulted once at SETUP; this turns the cross-namespace column into a live discriminator that modulates finding severity

---

## Candidate C-20 (from V-05)

*"Per-IG-ID elimination-path analysis with AMPLIFIED risk signal when the NS cross-namespace column records feasibility < 70 or any blocking compliance requirement; each IG-ID must produce an explicit elimination verdict before the [INERTIA-ANALYZED] gate token may be emitted."*

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["Token validity rule: gate token declared without its prerequisite scan evidence is structurally invalid — upgrades gate presence check to proof-of-work check", "Per-IG-ID elimination-path with AMPLIFIED risk signal when NS column shows feasibility < 70 or blocking compliance — parallel finding surface isomorphic to R-ID namespace"]}
```
