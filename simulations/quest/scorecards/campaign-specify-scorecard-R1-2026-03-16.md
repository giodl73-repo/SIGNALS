Scorecard written to `simulations/quest/scorecards/campaign-specify-scorecard-R1-2026-03-16.md`.

---

**Summary of Round 1 results:**

| Rank | Output | Composite | Golden? |
|------|--------|-----------|---------|
| 1 | V-01 | 100 | YES |
| 2 | V-02 | 24.5* | NO |

*V-02 is corrupted input — Phases 2 and 3 are absent/replaced by quest-score instructions. The 7 failures are structural voids, not design failures.

**V-01 hits golden (100/100)** — all 5 essential and all 5 recommended/aspirational pass. Three excellence patterns extracted:

1. **Phase 0 audience framing** — establishing voice contracts before any artifact is written, structurally preventing per-phase drift (C-10 driver)
2. **Multi-phase namespace-targeted scout pull** — Phase 1: generic glob, Phase 2: feasibility, Phase 3: positioning (C-09 driver)
3. **Completion Check fail-safe** — active recovery instruction prevents orchestration stop-short (C-01 reliability)

**Input quality issues to resolve before Round 2:**
- V-02 needs re-generation: Phase 2 and Phase 3 are absent (the checklist-before-write approach is sound but untested for proposal/pitch)
- V-03 through V-05 were not provided — round is partial

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 0 audience framing before any writing establishes distinct voice contracts preventing per-phase drift", "Multi-phase scout pull with namespace-specific targeting across all 3 artifacts (scout + feasibility + positioning)", "Completion Check fail-safe enforcement with active recovery instruction prevents orchestration stop-short"]}
```
 |
| VERIFIER  | ANALYST COMPLETE                                                | VERIFIER AUDIT COMPLETE                               | Evidence cell non-genericity; Present_mechanism and Absent_mechanism non-emptiness on PARTIAL rows | Diagnostic content quality, evidence standards |
| CONFIRMER | VERIFIER AUDIT COMPLETE                                         | CONFIRMATION COMPLETE                                 | Content quality: do Present/Absent cells name specific structural properties? | Format presence, scoring verdicts |
| SYNTHESIS | BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED | (terminal output) | Leaderboard, excellence signals, failure patterns, regression signals | Re-scoring, re-auditing |

Gate rules: no role begins without its Requires token. No role may be skipped or merged.

---

## ROLE 1: JUDGE

Domain: Evidence quality standards for C-01 through C-10 (campaign-specify rubric).

DUAL-FAMILY CLASSIFICATION PREAMBLE

No position-sensitive criteria (structural ordering is not a pass condition in this rubric).
No structural-class-recognition criteria (no named-class identification requirements in this rubric).
Both families enumerate zero members for this rubric version.

---

**C-01: Three artifacts written**
ACCEPTABLE: from V-01: "Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md ... Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md ... Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md ... Completion Check: Confirm all three artifacts were written. If any artifact was skipped, write it now -- do not end without all three on disk."
UNACCEPTABLE: from V-02: "Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md / Print: 'SPEC DONE:...' " [proposal and pitch write paths absent; no completion check]
Separating property: all-3-write-paths declared with completion-check fail-safe vs single-phase write path with no completion gate

**C-02: Spec contains required sections**
ACCEPTABLE: from V-01: "Required sections -- do not skip any: ### Purpose ... ### Requirements ... ### Design ... ### Constraints ... ### Open Questions"
ACCEPTABLE: from V-02: "Section checklist -- | Purpose | [ ] | REQUIRED ... | Requirements | [ ] | REQUIRED ... | Design | [ ] | REQUIRED ... | Constraints | [ ] | REQUIRED ... | Open Questions | [ ] | REQUIRED"
UNACCEPTABLE: "Write a spec for {topic} with all necessary sections." [no named section list]
Separating property: named 5-section list with do-not-skip enforcement vs unstructured instruction

**C-03: Proposal contains three options with recommendation**
ACCEPTABLE: from V-01: "### Option 1: Do Nothing / Description | Pros | Cons | Risk | Effort ... ### Option 2: [Name the approach] ... ### Option 3: [Name the approach] ... ### Recommendation / State the recommended option. Then state the key trade-off that drove the choice."
UNACCEPTABLE: from V-02: [Phase 2 absent -- contains quest-score instructions, not a proposal template]
Separating property: explicit 3-option slots with do-nothing named + recommendation trade-off constraint vs absent proposal structure

**C-04: Pitch covers three audience versions**
ACCEPTABLE: from V-01: "### Exec Version ... Voice contract: outcome-first, ROI framing, risk mention ... ### Developer Version ... Voice contract: show the tool, not the business case ... ### Maker Version ... Voice contract: jargon-free, 'can I do this?' framing ... Each [version]: Hook | What it does | Why it matters | Call to action"
UNACCEPTABLE: from V-02: [Phase 3 absent]
Separating property: named 3-version structure with voice contracts and 4-element slots vs absent pitch template

**C-05: Cross-artifact consistency**
ACCEPTABLE: from V-01: "Read simulations/draft/specs/{topic}-spec-{date}.md before writing." (Phase 2) and "Read simulations/draft/specs/{topic}-spec-{date}.md before writing. Read simulations/draft/proposals/{topic}-proposal-{date}.md before writing." (Phase 3)
UNACCEPTABLE: from V-02: [only Phase 1 defined; no prior-artifact read instructions possible for Phases 2-3]
Separating property: explicit prior-artifact read instruction at each phase boundary vs single-phase isolation with no cross-artifact coupling

**C-06: Spec self-review flags gaps**
ACCEPTABLE: from V-01: "### Self-Review (Architect) / Look back at the five sections. Flag: Any section that is thin or needs more detail / Any ambiguity that would confuse an engineer / Any assumption that should be a requirement instead"
ACCEPTABLE: from V-02: "| Self-Review | [ ] | REQUIRED -- gaps, ambiguities, thin sections called out"
UNACCEPTABLE: "Review the spec before moving on." [no named output items]
Separating property: named self-review section with specific gap categories to flag vs generic review instruction

**C-07: Pitch contains anti-positioning section**
ACCEPTABLE: from V-01: "### Anti-Positioning / What {topic} is NOT. Three statements that preempt scope creep or misuse. Each starts with: '{topic} is not...'"
UNACCEPTABLE: from V-02: [Phase 3 absent; no anti-positioning possible]
Separating property: explicit anti-positioning section with 3-statement format vs absent pitch template

**C-08: Proposal recommendation cites trade-off**
ACCEPTABLE: from V-01: "Then state the key trade-off that drove the choice -- not just a preference. The trade-off must reference a concrete constraint or risk from the options above."
UNACCEPTABLE: from V-02: [Phase 2 absent; no recommendation section]
Separating property: explicit "must reference concrete constraint or risk" enforcement vs absent proposal recommendation

**C-09: Scout signal pull-through**
ACCEPTABLE: from V-01: "Pull any scout signals from simulations/scout/ for {topic}. List which signals were found (path + signal type). If none, note that." (Phase 1) + "Pull any scout-feasibility signal for {topic} if available." (Phase 2) + "Pull any scout-positioning signal for {topic} if available." (Phase 3)
ACCEPTABLE: from V-02: "Scout signal check: glob simulations/scout/ for {topic} signals. List found: [signal name | path] for each. If none: '(no scout signals found)'"
UNACCEPTABLE: "Check if any scout data is available." [no glob path, no list format, no per-namespace targeting]
Separating property: glob-path-specific scout pull with namespace-targeted phases (feasibility, positioning) vs scope-agnostic or absent pull

**C-10: Audience voice differentiation**
ACCEPTABLE: from V-01: Phase 0 declares "What is the one sentence each audience cares about most?" before writing begins + voice contracts per version: "outcome-first, ROI framing, risk mention" vs "show the tool, not the business case" vs "jargon-free, 'can I do this?' framing"
UNACCEPTABLE: from V-02: [Phase 3 absent; no voice differentiation structure]
Separating property: upfront audience framing phase (Phase 0) establishing distinct voice contracts before any artifact is written vs absent pitch structure

---

CONSOLIDATED PRODUCTION-TIME REGISTER

| Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
|-----------|----------------|--------------|------------------------------|-----------------------------|
| C-01 | Three artifacts written | YES | YES | YES |
| C-02 | Spec required sections | YES | YES | YES |
| C-03 | Proposal three options + recommendation | YES | YES | YES |
| C-04 | Pitch three audience versions | YES | YES | YES |
| C-05 | Cross-artifact consistency | YES | YES | YES |
| C-06 | Spec self-review | YES | YES | YES |
| C-07 | Pitch anti-positioning | YES | YES | YES |
| C-08 | Proposal recommendation trade-off | YES | YES | YES |
| C-09 | Scout signal pull-through | YES | YES | YES |
| C-10 | Audience voice differentiation | YES | YES | YES |

REGISTER COMPLETENESS CONFIRMED

JUDGE STANDARD COMPLETE

---

## ROLE 2: ANALYST

Domain: Per-criterion scoring; composite computation using rubric formula (essential/5, recommended/3, aspirational/2).
Do not begin until JUDGE STANDARD COMPLETE appears above. [Gate satisfied.]

Rubric formula:
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
PARTIAL counts as 0.5
```

---

### V-01 Scoring Table

Axis: PM-first role sequence. Phase 0 frames audiences before writing. Phases 1-3 are spec, proposal, pitch.

| ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |
|----|-----------|--------|---------|----------|-------------------|------------------|
| C-01 | Three artifacts written | essential | PASS | Explicit write paths for all 3 artifacts declared in Phases 1-3. Completion Check: "If any artifact was skipped, write it now -- do not end without all three on disk." | -- | -- |
| C-02 | Spec required sections | essential | PASS | "Required sections -- do not skip any: Purpose, Requirements, Design, Constraints, Open Questions." All 5 named with explicit do-not-skip constraint. | -- | -- |
| C-03 | Proposal three options + rec | essential | PASS | Option 1: Do Nothing, Option 2, Option 3 slots each with Description|Pros|Cons|Risk|Effort. Recommendation requires "key trade-off that drove the choice -- not just a preference." | -- | -- |
| C-04 | Pitch three audience versions | essential | PASS | Exec/Developer/Maker versions each with named 4 elements: Hook, What it does, Why it matters, Call to action. Voice contracts declared per version. | -- | -- |
| C-05 | Cross-artifact consistency | essential | PASS | Phase 2 reads spec before writing. Phase 3 reads spec AND proposal before writing. Phase 0 audience framing reused in Phase 3: "The PM frame from Phase 0 stated what each audience cares about. Use that to write..." | -- | -- |
| C-06 | Spec self-review | recommended | PASS | Self-Review (Architect) section with 3 named flagging targets: thin sections, ambiguities that would confuse an engineer, assumptions that should be requirements. | -- | -- |
| C-07 | Pitch anti-positioning | recommended | PASS | Anti-Positioning section: "What {topic} is NOT. Three statements that preempt scope creep or misuse. Each starts with: '{topic} is not...'" | -- | -- |
| C-08 | Proposal recommendation trade-off | recommended | PASS | "The trade-off must reference a concrete constraint or risk from the options above." Explicit prohibition against preference-only rationale. | -- | -- |
| C-09 | Scout signal pull-through | aspirational | PASS | Phase 1 pulls from simulations/scout/ with path+type listing. Phase 2 pulls scout-feasibility. Phase 3 pulls scout-positioning. Three namespace-specific pull points across all phases. | -- | -- |
| C-10 | Audience voice differentiation | aspirational | PASS | Phase 0 Business Context Frame asks "one sentence each audience cares about most" before any writing. Each pitch version has a declared voice contract naming distinct orientation: outcome-first ROI vs tool capability vs jargon-free can-I-do-this. | -- | -- |

essential_pass = 5/5 = 5.0
recommended_pass = 3/3 = 3.0
aspirational_pass = 2/2 = 2.0

composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10) = 60 + 30 + 10 = **100**

Golden: **YES** -- all 5 essentials PASS; composite = 100

---

### V-02 Scoring Table

Axis: Checklist-before-write format. Phase 1 (spec checklist) is present and well-structured. Phase 2 is absent/corrupted (contains quest-score instructions). Phase 3 is absent.

| ID | Criterion | Weight | Verdict | Evidence | Present_mechanism | Absent_mechanism |
|----|-----------|--------|---------|----------|-------------------|------------------|
| C-01 | Three artifacts written | essential | FAIL | Only spec write path present ("SPEC DONE: simulations/draft/specs/..."). Proposal write path absent. Pitch write path absent. No completion check. | -- | -- |
| C-02 | Spec required sections | essential | PASS | Phase 1 checklist table declares all 5 sections as REQUIRED rows: Purpose, Requirements, Design, Constraints, Open Questions. Checklist-mark-as-done mechanism before write. | -- | -- |
| C-03 | Proposal three options + rec | essential | FAIL | Phase 2 absent. No proposal template defined. No option slots, no do-nothing option, no recommendation section. | -- | -- |
| C-04 | Pitch three audience versions | essential | FAIL | Phase 3 absent. No pitch template defined. No audience version slots. | -- | -- |
| C-05 | Cross-artifact consistency | essential | FAIL | Only Phase 1 defined. No prior-artifact read instructions exist for Phases 2-3. Cross-phase coupling structurally impossible with absent phases. | -- | -- |
| C-06 | Spec self-review | recommended | PASS | Checklist includes "Self-Review | [ ] | REQUIRED -- gaps, ambiguities, thin sections called out" as an explicit named row in the section checklist. | -- | -- |
| C-07 | Pitch anti-positioning | recommended | FAIL | Phase 3 absent. No anti-positioning section possible. | -- | -- |
| C-08 | Proposal recommendation trade-off | recommended | FAIL | Phase 2 absent. No recommendation section defined. | -- | -- |
| C-09 | Scout signal pull-through | aspirational | PARTIAL | Phase 1 has "Scout signal check: glob simulations/scout/ for {topic} signals. List found: [signal name | path] for each." Scope-agnostic glob with inventory list present in Phase 1. | Phase 1 scout glob instruction with signal inventory list | Phases 2-3 absent; feasibility and positioning namespace-specific pull instructions cannot exist; multi-phase pull-through structurally blocked |
| C-10 | Audience voice differentiation | aspirational | FAIL | Phase 3 absent. No audience version structure. No voice contracts. | -- | -- |

essential_pass = 1/5 (C-02 only) = 1.0
recommended_pass = 1/3 (C-06 only) = 1.0
aspirational_pass = 0.5/2 (C-09 PARTIAL) = 0.5

composite = (1/5 * 60) + (1/3 * 30) + (0.5/2 * 10) = 12 + 10 + 2.5 = **24.5**

Golden: **NO** -- C-01, C-03, C-04, C-05 fail; composite = 24.5

Note: V-02's failures on C-01, C-03, C-04, C-05, C-07, C-08, C-10 are attributable to input corruption/truncation, not to the checklist-before-write design approach itself.

ANALYST COMPLETE -- 2 outputs scored

---

## ROLE 3: VERIFIER

Domain: Evidence cell non-genericity; Present/Absent column non-emptiness on PARTIAL rows.
Do not begin until ANALYST COMPLETE appears above. [Gate satisfied.]

### V-01 -- Post-write Evidence and Diagnostic Column Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 | PASS | "Explicit write paths for all 3 artifacts declared in Phases 1-3. Completion Check..." | PASS | n/a | ACCEPTED |
| C-02 | PASS | "'Required sections -- do not skip any: Purpose, Requirements, Design, Constraints, Open Questions.'" | PASS | n/a | ACCEPTED |
| C-03 | PASS | "Option 1: Do Nothing, Option 2, Option 3 slots each with Description|Pros|Cons|Risk|Effort." | PASS | n/a | ACCEPTED |
| C-04 | PASS | "Exec/Developer/Maker versions each with named 4 elements: Hook, What it does, Why..." | PASS | n/a | ACCEPTED |
| C-05 | PASS | "Phase 2 reads spec before writing. Phase 3 reads spec AND proposal before writing." | PASS | n/a | ACCEPTED |
| C-06 | PASS | "Self-Review (Architect) section with 3 named flagging targets: thin sections, ambiguities..." | PASS | n/a | ACCEPTED |
| C-07 | PASS | "Anti-Positioning section: 'What {topic} is NOT. Three statements that preempt scope creep...'" | PASS | n/a | ACCEPTED |
| C-08 | PASS | "'The trade-off must reference a concrete constraint or risk from the options above.'" | PASS | n/a | ACCEPTED |
| C-09 | PASS | "Phase 1 pulls from simulations/scout/ with path+type listing. Phase 2 pulls scout-feasibility." | PASS | n/a | ACCEPTED |
| C-10 | PASS | "Phase 0 Business Context Frame asks 'one sentence each audience cares about most' before..." | PASS | n/a | ACCEPTED |

All V-01 rows: ACCEPTED.

### V-02 -- Post-write Evidence and Diagnostic Column Audit

| ID | Verdict | Evidence excerpt (first 15 words) | Audit A | Audit B | Status |
|----|---------|-----------------------------------|---------|---------|--------|
| C-01 | FAIL | "Only spec write path present ('SPEC DONE: simulations/draft/specs/...'). Proposal write path..." | PASS | n/a | ACCEPTED |
| C-02 | PASS | "Phase 1 checklist table declares all 5 sections as REQUIRED rows: Purpose, Requirements..." | PASS | n/a | ACCEPTED |
| C-03 | FAIL | "Phase 2 absent. No proposal template defined. No option slots, no do-nothing option..." | PASS | n/a | ACCEPTED |
| C-04 | FAIL | "Phase 3 absent. No pitch template defined. No audience version slots." | PASS | n/a | ACCEPTED |
| C-05 | FAIL | "Only Phase 1 defined. No prior-artifact read instructions exist for Phases 2-3." | PASS | n/a | ACCEPTED |
| C-06 | PASS | "Checklist includes 'Self-Review | [ ] | REQUIRED -- gaps, ambiguities, thin sections called out'" | PASS | n/a | ACCEPTED |
| C-07 | FAIL | "Phase 3 absent. No anti-positioning section possible." | PASS | n/a | ACCEPTED |
| C-08 | FAIL | "Phase 2 absent. No recommendation section defined." | PASS | n/a | ACCEPTED |
| C-09 | PARTIAL | "Phase 1 has 'Scout signal check: glob simulations/scout/ for {topic} signals.'" | PASS | PASS | ACCEPTED |
| C-10 | FAIL | "Phase 3 absent. No audience version structure. No voice contracts." | PASS | n/a | ACCEPTED |

All V-02 rows: ACCEPTED. No flags.

VERIFIER AUDIT COMPLETE

---

## ROLE 4: CONFIRMER

Domain: Content quality -- do Present/Absent mechanism cells name specific structural properties?
Do not begin until VERIFIER AUDIT COMPLETE appears above. [Gate satisfied.]

Only one PARTIAL verdict across all inputs: V-02 / C-09.

### V-02 -- Diagnostic Content Audit

| Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status |
|-----------|--------------------------------------|-----------|-------------------------------------|-----------|--------|
| C-09 | "Phase 1 scout glob instruction with signal inventory list" | YES | "Phases 2-3 absent; feasibility and positioning namespace-specific pull instructions cannot exist; multi-phase pull-through structurally blocked" | YES | CONFIRMED |

Present names a specific structural element (Phase 1 scout glob with list format) -- not a generic quality phrase.
Absent names a specific structural gap (absent phases + named missing namespace targets: feasibility, positioning) -- not a restatement of the verdict.

CONFIRMATION COMPLETE

---

## SYNTHESIS

BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE AND REGISTER COMPLETENESS CONFIRMED satisfied above.

### LEADERBOARD

| Rank | Output | Composite | Golden? |
|------|--------|-----------|---------|
| 1 | V-01 | 100 | YES |
| 2 | V-02 | 24.5* | NO |

*V-02 score is artificially depressed by input corruption/truncation. Phases 2 and 3 were absent -- 7 of 8 failures are structural voids, not design decisions. The checklist approach (Phase 1 of V-02) is competitive on C-02 and C-06.

Note: V-03 through V-05 were not provided. This scorecard covers 2 of 5 expected variations.

---

### EXCELLENCE SIGNALS

Signal: V-01 -- C-10 -- Phase 0 "Business Context Frame" role establishes audience framing before any artifact is written, producing structural voice contract separation (outcome-first vs tool-capability vs jargon-free can-I-do-this) rather than relying on per-phase recall. This is the most architecturally novel mechanism in V-01 and the primary driver of C-10 reliability.

Signal: V-01 -- C-09 -- Three-phase scout pull with namespace-specific targeting (generic scout in Phase 1, feasibility in Phase 2, positioning in Phase 3) vs V-02's Phase 1 scope-agnostic glob. Explicit namespace routing increases signal specificity per artifact type.

Signal: V-01 -- C-01 -- Completion Check fail-safe with active enforcement instruction ("write it now -- do not end without all three on disk") vs implicit completion. Fail-safe addresses the C-01 failure pattern (orchestration stopped early) by naming the recovery action.

Signal: V-01 -- C-05 -- Phase 3 reads both spec and proposal before writing. V-01 adds a second read dependency in Phase 3 (not just spec) creating a chain: spec -> read-by-proposal -> read-by-pitch. This double-link is the structural mechanism preventing scope drift across all three artifacts.

Signal: V-02 (Phase 1) -- C-02 and C-06 -- Pre-write section checklist with REQUIRED/OPTIONAL labeling and per-row mark-as-done forces commitment to structure before prose generation begins. This mechanism may outperform V-01's do-not-skip instruction by making section completion a tracked state.

---

### FAILURE PATTERNS

No criterion fails across ALL inputs in this round. V-02's failures are input-quality (corrupted prompt), not skill-design failures.

Pattern: PARTIAL-only pattern -- C-09 in V-02
Diagnosis: input quality issue -- V-02 Phase 2 and Phase 3 are absent, making multi-namespace pull-through structurally impossible. The V-02 axis (checklist-before-write) did not define Phase 2 or Phase 3, so scout pull for proposal and pitch phases could not be evaluated. This is an incomplete prompt design, not a rubric gap.

---

### REGRESSION SIGNALS

No prior round data; regression analysis not possible.

---

## Input Quality Note

V-02's Phase 2 contains quest-score evaluation instructions rather than a draft-proposal template. This is a generation artifact -- the quest-variate output was likely concatenated with the quest-score instructions without a separator, causing the scoring instructions to appear inside V-02's body. The checklist approach underlying V-02 Phase 1 is structurally sound and competitive on C-02/C-06. A clean V-02 re-generation with Phase 2 (checklist for proposal) and Phase 3 (checklist for pitch) should be scored in Round 2 as V-02-clean before comparing axes.

V-03 through V-05 were not included in this invocation. Round 1 scoring is partial. The quest:golden loop should either re-invoke quest:variate to produce V-03-V-05 or provide them as inputs before declaring a Round 1 winner.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 0 audience framing before any writing establishes distinct voice contracts preventing per-phase drift", "Multi-phase scout pull with namespace-specific targeting across all 3 artifacts (scout + feasibility + positioning)", "Completion Check fail-safe enforcement with active recovery instruction prevents orchestration stop-short"]}
```
