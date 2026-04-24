## Quest Score — prove-topic R15

**Rubric**: v14 | **Variations**: V-01 through V-05 | **Date**: 2026-03-16

---

## Criterion Evaluation

### V-01 — Role Sequence

| ID | Description | Result | Evidence |
|----|-------------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | Stages 1–5 explicit with correct order: hypothesis → websearch → intelligence → analysis → synthesize |
| C-02 | Scout artifact named before hypothesis | **PASS** | ROLE 1 — SCOUT LOADER names `{topic}-scout-record-{date}.md`, gates Stage 1 via PRE-STAGE EXIT |
| C-03 | Progressive writes — one per stage | **PASS** | Five separate Write + confirm-write instructions, one per stage |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | "STAGE 5 EXIT: synthesis_complete — Evidence brief complete. Ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | **PASS** | Full `simulations/prove/prove-{stage}/{topic}-prove-{stage}-{date}.md` paths at each stage |
| C-06 | Forward-only with gate before Stage 1 | **PASS** | "Do not begin Stage 1 until PRE-STAGE EXIT is printed." ROLE 3 requires ROLES 1+2 confirmed |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 body: `source_artifact: [path — copied from ROLE 1 output, not re-inferred]` — written into artifact |
| C-08 | Evidence gaps flagged at point of discovery | **PASS** | `s2_key_gap` at Stage 2, `s3_key_gap` at Stage 3, `s4_counter_evidence` at Stage 4 |
| C-09 | Thin evidence propagates to synthesis | **PARTIAL** | `confidence_final` has one-sentence reasoning; no explicit rule to trace s2/s3 key_gap to named weakened claims in synthesis |
| C-10 | Hypothesis structurally blocked until scout | **PASS** | Dependency chain: ROLE 1 BLOCKED → ROLE 3 can't confirm → PRE-STAGE EXIT never printed → Stage 1 cannot begin |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: C-09 PARTIAL (2.5), C-10 PASS (5) → 7.5 pts  
**Composite: 97.5** | **Golden: YES**

---

### V-02 — Output Format

| ID | Description | Result | Evidence |
|----|-------------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | Five stages in correct order with explicit headers |
| C-02 | Scout artifact named before hypothesis | **PASS** | CAMPAIGN HEADER table names `{topic}-scout-record-{date}.md` before Stage 1; "Load scout_artifact now. If not found, halt." |
| C-03 | Progressive writes — one per stage | **PASS** | "Write: `path`" + "Confirm write before advancing to Stage N+1" at every stage |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | "EXIT: synthesis_complete — evidence brief ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | **PASS** | Full paths in backticks at each of the five write instructions |
| C-06 | Forward-only with gate before Stage 1 | **PASS** | "If not found, halt." + "Fill status_quo_comparator before advancing" — gate is prose but references scout presence |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 table: `\| source_artifact \| [scout_artifact path — copied from header, not re-inferred] \|` — field written into artifact |
| C-08 | Evidence gaps flagged at point of discovery | **PASS** | `s2_key_gap` in Stage 2 summary table, `s3_key_gap` in Stage 3 summary table, `s4_counter_evidence` in Stage 4 summary |
| C-09 | Thin evidence propagates to synthesis | **PARTIAL** | Confidence calculation: `base - counter_evidence_penalty = final` propagates counter-evidence numerically. Does not explicitly trace which claim a gap from s2_key_gap/s3_key_gap weakens |
| C-10 | Hypothesis structurally blocked until scout | **PARTIAL** | "If not found, halt" is advisory — no structural gate or blocking mechanism between HEADER and Stage 1 |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: C-09 PARTIAL (2.5), C-10 PARTIAL (2.5) → 5 pts  
**Composite: 95** | **Golden: YES**

---

### V-03 — Lifecycle Emphasis

| ID | Description | Result | Evidence |
|----|-------------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | Five stages in order, each with ENTRY CONDITIONS requiring the prior EXIT SIGNAL |
| C-02 | Scout artifact named before hypothesis | **PASS** | SCOUT LOAD section before CAMPAIGN GATE names `{topic}-scout-record-{date}.md`; gate requires `scout_loaded = true` |
| C-03 | Progressive writes — one per stage | **PASS** | STAGE N WRITE block at every stage with path + confirm before EXIT SIGNAL is printed |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | "STAGE 5 EXIT SIGNAL: synthesis_complete — Evidence brief complete. Ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | **PASS** | All five STAGE WRITE blocks contain full paths |
| C-06 | Forward-only with gate before Stage 1 | **PASS** | CAMPAIGN GATE checklist: "If any gate item is unchecked: CAMPAIGN BLOCKED." "Do not begin Stage 1 until GATE EXIT is printed." |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 body: `source_artifact: [path — copied from SCOUT LOAD above, not re-inferred]` — written into hypothesis artifact |
| C-08 | Evidence gaps flagged at point of discovery | **PASS** | `s2_key_gap` (Stage 2), `s3_key_gap` (Stage 3), `s4_counter_evidence` citing artifact + section (Stage 4) |
| C-09 | Thin evidence propagates to synthesis | **PASS** | COUNTER-HYPOTHESIS RESOLUTION in Stage 5 names the claim (counter_hypothesis), requires `resolution_evidence: [cite stage artifact]`, and `OPEN RISK → note explicitly in key_risk` — traces thin findings to specific claim with stage citation |
| C-10 | Hypothesis structurally blocked until scout | **PASS** | CAMPAIGN GATE checklist + "CAMPAIGN BLOCKED" if scout_loaded unchecked + "Do not begin Stage 1 until GATE EXIT is printed" — structural block, not advisory |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 2/2 → 10 pts  
**Composite: 100** | **Golden: YES**

---

### V-04 — Phrasing Register + Inertia Framing

| ID | Description | Result | Evidence |
|----|-------------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | Five numbered stages in correct order |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP: "You must name the file before running Stage 1." `scout_artifact: [path to the scout signal file]` |
| C-03 | Progressive writes — one per stage | **PASS** | "Write to: `path`" + "Confirm the write before moving to Stage N+1" at every stage |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | Stage 5 closes with: "Evidence brief complete. Ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | **PASS** | All five write instructions include full paths in backticks |
| C-06 | Forward-only with gate before Stage 1 | **PASS** | SETUP: "If you cannot find a scout artifact: stop here. Record what you searched and halt." — equivalent checkpoint referencing scout presence |
| C-07 | Scout anchor in hypothesis artifact | **PARTIAL** | `scout_artifact` is named in SETUP only; Stage 1 output fields contain only `hypothesis` and `counter_hypothesis` — no source link carried into the artifact |
| C-08 | Evidence gaps flagged at point of discovery | **PARTIAL** | `s2_displacement_read` flags conflicting web signals at S2; `s4_counter_hypothesis_status` flags open risk at S4; no explicit `key_gap` field at any stage — implicit rather than dedicated gap flags |
| C-09 | Thin evidence propagates to synthesis | **FAIL** | No per-stage gap flags to propagate; Stage 5 `confidence` and `key_risk` have no mechanism to trace thin findings to named weakened claims from prior stages |
| C-10 | Hypothesis structurally blocked until scout | **FAIL** | "Stop here" is advisory text; no structural block, gate mechanism, or confirmation token between SETUP and Stage 1 |

**Essential**: 5/5 → 60 pts | **Recommended**: C-06 PASS (10), C-07 PARTIAL (5), C-08 PARTIAL (5) → 20 pts | **Aspirational**: 0/2 → 0 pts  
**Composite: 80** | **Golden: YES (borderline)**

---

### V-05 — All Four Axes Combined

| ID | Description | Result | Evidence |
|----|-------------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | Five stages in strict order, each with ENTRY CONDITIONS requiring prior EXIT |
| C-02 | Scout artifact named before hypothesis | **PASS** | ROLE 1 — SCOUT LOADER names artifact in PRE-STAGE; "Do not begin Stage 1 until PRE-STAGE EXIT is printed" |
| C-03 | Progressive writes — one per stage | **PASS** | WRITE + confirm at every stage before EXIT SIGNAL |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | "STAGE 5 EXIT: synthesis_complete — 'Evidence brief complete. Ready for /topic-story.'" |
| C-05 | Artifact paths on every write instruction | **PASS** | Full paths in all five WRITE blocks |
| C-06 | Forward-only with gate before Stage 1 | **PASS** | Stage 1 ENTRY CONDITIONS: `[ ] PRE-STAGE EXIT received: campaign_open`; ROLE 1 halt if scout missing cascades up to block PRE-STAGE EXIT |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 table: `\| source_artifact \| [path — copied from ROLE 1, not re-inferred] \|` — written into hypothesis artifact |
| C-08 | Evidence gaps flagged at point of discovery | **PASS** | `s2_key_gap` (Stage 2), `s3_key_gap` (Stage 3), `s4_counter_evidence` citing artifact + section (Stage 4) |
| C-09 | Thin evidence propagates to synthesis | **PASS** | COUNTER-HYPOTHESIS RESOLUTION cites stage artifact, names OPEN RISK; `s4_aggregate_displacement_verdict` required in Stage 5 entry; `displacement_conclusion` field in synthesis makes evidence-to-claim tracing explicit |
| C-10 | Hypothesis structurally blocked until scout | **PASS** | ROLE 1 BLOCKED → ROLE 2 cannot execute → ROLE 3 cannot print PRE-STAGE EXIT → Stage 1 entry condition fails — dependency chain is structural |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 2/2 → 10 pts  
**Composite: 100** | **Golden: YES**

---

## Rankings

| Rank | Variation | Composite | Golden | Key gap |
|------|-----------|-----------|--------|---------|
| 1 | **V-03** (Lifecycle) | **100** | YES | — |
| 1 | **V-05** (All Four) | **100** | YES | — |
| 3 | V-01 (Role Sequence) | **97.5** | YES | C-09 partial: confidence_final doesn't require tracing key_gap to named claim |
| 4 | V-02 (Output Format) | **95** | YES | C-09 partial: counter_evidence_penalty is numerical but doesn't name weakened claim; C-10 partial: advisory halt only |
| 5 | V-04 (Phrasing + Inertia) | **80** | YES (borderline) | C-07/C-08 partial, C-09/C-10 fail — conversational register dropped structural machinery |

---

## Excellence Signals from Top Variations

**V-03 and V-05 both achieve 100 through four mechanisms the others lacked:**

1. **Counter-hypothesis resolution with artifact citation** — Stage 5 COUNTER-HYPOTHESIS RESOLUTION requires `resolution_verdict + resolution_evidence: [cite stage artifact]`. When OPEN RISK, the unresolved risk propagates explicitly to `key_risk`. This satisfies C-09 by making the claim being weakened (the counter-hypothesis) and the source stage citation structurally required — not advisory.

2. **Formal GATE block with CAMPAIGN BLOCKED status** — V-03's `CAMPAIGN GATE: [ ] scout_loaded = true` with an explicit "CAMPAIGN BLOCKED" state if unchecked is stronger than V-01's role-chain dependency. The checkpoint is printed, named, and its failure state is visible before Stage 1 headers appear. This satisfies C-10 without ambiguity.

3. **Named exit signals at every stage boundary** — `hypothesis_locked`, `websearch_complete`, `intelligence_complete`, `analysis_complete`, `synthesis_complete` are named tokens that each stage's ENTRY CONDITIONS require from the prior stage. This enforces forward-only sequencing structurally (a stage body cannot begin without naming receipt of the prior stage's token) rather than relying on section ordering.

4. **Interrupted-campaign resume logic** (V-03 exclusive) — "Find the most recent artifact for this topic in `simulations/prove/`. Identify the last stage that confirmed a write. Resume from the first stage whose artifact is missing." This pattern is absent in all other variations and converts partial-run recovery from undefined behavior to a stated protocol.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["counter-hypothesis resolution with artifact citation makes C-09 structural: names the claim, cites the stage, propagates OPEN RISK to key_risk", "formal GATE block with CAMPAIGN BLOCKED exit state before Stage 1 satisfies C-10 without ambiguity over advisory-vs-structural distinction", "named exit signal tokens at every stage boundary (hypothesis_locked, websearch_complete, etc.) enforce forward-only sequence via entry-condition receipt checks", "interrupted-campaign resume instruction identifies last confirmed artifact write and resumes from first missing stage"]}
```
