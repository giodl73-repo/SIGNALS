## campaign-track R7 Scorecard

All five variations score **98/98**. The open question is answered.

---

### Results

| Variation | Score | C-10 Quality |
|-----------|-------|---|
| V-01 | 98/98 | Prose section, untyped, no gate |
| V-02 | 98/98 | Typed Session Delta Contract |
| V-03 | 98/98 | Analyst-owned, Phase 3 gate requires delta.md |
| V-04 | 98/98 | Typed + 27-item terminal checklist |
| V-05 | 98/98 | Typed + owned + gated + two-pass update |

**Five-way tie.** C-10 is binary -- "session delta section: signals added, verdict change summary" is satisfied by V-01's two prose fields. Structural quality (typed fields, ownership, terminal gating) does not split the 3-pt aspirational award.

### Verdict on the open question

> Does C-10 require typed fields, role ownership, or terminal verification -- or only presence?

**Only presence.** V-01 passes C-10 with a minimal prose section. If a future round wants to discriminate structural quality, a new criterion (C-25+) would need to specify typed delta contract, role ownership, or terminal verification as explicit pass conditions.

### Excellence signals from V-05 (4 new patterns)

1. **Two-pass delta update** -- placeholder verdict_after in Phase 3 Step B, updated post-Phase 4; terminal item flags "placeholder fails" as the only order-dependent constraint across all rounds
2. **Dual-contract active-role annotation** -- Phase 3 header names both Phase 3 Contract AND Session Delta Contract at the execution site
3. **Conjunction progression gate** -- "status.md AND delta.md both present" makes delta non-skippable via the gate, not a post-Phase-4 appendage
4. **signals_added type-tightening** -- terminal item explicitly rejects string "NONE" sentinel, requires empty list `[]`

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["two-pass delta update -- delta.md written in Phase 3 Step B with placeholder verdict_after, updated post-Phase 4 with actual verdict_verb; terminal checklist item flags placeholder-fails as only order-dependent constraint", "dual-contract active-role annotation -- Phase 3 header names both Phase 3 Contract and Session Delta Contract at execution site when phase produces two artifacts", "conjunction progression gate -- Phase 3 postcondition requires status.md AND delta.md, making supplemental artifact non-skippable via the gate rather than post-Phase-4 appendage", "signals_added type-tightening note -- terminal item explicitly rejects string NONE sentinel and requires empty list [], closing first-invocation type-inconsistency from prior untyped versions"]}
```
 C-03 -- Nine-namespace coverage table (Essential, 10 pts)
All five: Phase 3 Contract explicitly requires "all 9 namespace rows required; each row: namespace / planned / collected / missing / zero_flag." Phase 3 body restates "All 9 namespace rows present -- no row skipped." **PASS all.**

### C-04 -- Readiness verdict from enumerated set (Essential, 10 pts)
All five: Phase 3 Contract declares "readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY." Phase 3 body lists the 3-token set. Terminal checklist item checks the constraint. **PASS all.**

### C-05 -- Narrative verdict with evidence (Essential, 10 pts)
All five: Phase 4 Contract requires verdict_verb (5-token set), hypothesis_mutation (s0 + current), echoes, next_signal_recommendations (3 items). The five-token set is enumerated. **PASS all.**

### C-06 -- Artifact write paths (Recommended, 5 pts)
All five: Every phase section ends with "Write to: simulations/topic/{{topic}}-[artifact]-{{date}}.md." V-03/V-05 add a second "Write delta to:" path at Phase 3. **PASS all.**

### C-07 -- Coverage ratio and readiness statement (Recommended, 5 pts)
All five: coverage_ratio typed as "X/N" format in Phase 3 Contract; readiness_verdict as labeled 3-token verdict. C-07 requires numeric ratio + labeled readiness verdict -- both present. **PASS all.**

### C-08 -- Cross-namespace signal balance (Recommended, 5 pts)
All five: All 9 namespace rows mandated in Phase 3 Contract; zero_flag = "NO SIGNALS" marks namespaces where planned = 0 AND collected = 0. Zero-signal namespaces flagged explicitly by contract. **PASS all.**

### C-09 -- Echo integration (Aspirational, 3 pts)
All five: Phase 4 Contract: "echoes: list of strings; if none, value must be ['NONE']." The "NONE" fallback and list format both present. Terminal checklist item: "echoes: list present with at least one entry (minimum ['NONE'])." **PASS all.**

### C-10 -- Dual-session delta (Aspirational, 3 pts)
C-10 criterion: session delta section present; signals added named; verdict change summary present; first-invocation case handled; written to artifact.

- **V-01**: Post-Phase-4 prose section. signals_added as named field with list-or-"NONE" values; verdict_before/after/changed. First invocation: "Session 1 -- no prior session" / "NONE" / "N/A." delta.md artifact. Dashboard item 5 references delta explicitly. **PASS** (minimal -- untyped fields, no gate, no checklist enforcement).
- **V-02**: Typed Session Delta Contract -- session_number (int), signals_added (list), signals_removed (list), verdict_before/after (enumerated tokens including NONE sentinel), verdict_changed (YES|NO|N/A). First invocation typed with empty lists and NONE sentinel. **PASS** (typed fields, no ownership gate).
- **V-03**: Analyst owns delta.md; role description explicitly states "Owns status.md AND delta.md." Phase 3 postcondition: "status.md AND delta.md both present" -- delta required to advance to Phase 4. signals_added + verdict_before/after/changed in prose delta. **PASS** (ownership-enforced, untyped).
- **V-04**: V-02 typed contract plus 5 delta fields in 27-item terminal checklist (session_number, signals_added, verdict_before, verdict_after, verdict_changed) -- each with targeted "FAIL: re-run Session Delta." **PASS** (typed + terminally gated).
- **V-05**: All three axes -- typed contract (V-02) + Analyst ownership (V-03) + 27-item checklist (V-04) + two-pass delta update (delta.md written Phase 3 Step B, verdict_after updated after Phase 4). Terminal item for verdict_after explicitly flags "placeholder fails." **PASS** (maximum enforcement).

**All five PASS.** C-10 is binary -- the criterion definition ("session delta section: signals added, verdict change summary") is satisfied by all. Structural quality differentiates V-01 through V-05 within the PASS verdict but does not split the 3-pt award.

### C-11 -- Role-gated phases (Aspirational, 3 pts)
All five: Four distinct named personas -- Registrar (Phase 1), Planner (Phase 2), Analyst (Phase 3), Narrator (Phase 4). Each phase section opens with "*[Role] active.*" annotation. Roles are domain-bounded: Registrar never synthesizes (Prohibition 2), Narrator never plans (Prohibition 2 forbids modifying signals). Generic "Assistant" labels absent. **PASS all.**

### C-12 -- Explicit progression gates (Aspirational, 3 pts)
All five: "GATE: Do not proceed to Phase X until [postcondition] is satisfied." between every adjacent phase pair. V-03/V-05 additionally gate Phase 3 on two artifacts: "status.md AND delta.md both present" -- tighter than V-01/V-02/V-04 which gate on status.md only. **PASS all.**

### C-13 -- Empty-state as named section (Aspirational, 3 pts)
All five: "## Empty-State Handling / ### First Invocation (0 signals collected)" section present with per-phase behavior specified individually (Phase 1 through 4, plus delta). Not a buried sentence -- dedicated labeled section. **PASS all.**

### C-14 -- Per-role prohibition lists (Aspirational, 3 pts)
All five: Each of the four roles has an explicitly numbered list headed "Forbidden actions (exactly 5):". Items are named forbidden actions, not just role descriptions. At least two roles per variation have named prohibited actions. All four roles have them. **PASS all.**

### C-15 -- Typed output contracts per phase (Aspirational, 3 pts)
All five: All four phases have typed output contracts in the "Typed Output Contracts" section. Fields specify exact value types (string | integer | enumerated token set), required fields are named, and verdict fields are constrained to enumerated sets. Criterion requires >= 2 phases -- all five deliver all 4. **PASS all.**

### C-16 -- Terminal completion checklist (Aspirational, 3 pts)
All five: "TERMINAL -- Field-Level Completion Checklist" section present. Per-phase PASS conditions present (each field with named constraint). Targeted re-run language: "FAIL: re-run Phase X" for each item. Dashboard emitted only after "All N items PASS." Distinction between targeted phase re-run and full restart present. V-01/V-02/V-03 have 22 items; V-04/V-05 have 27. **PASS all.**

### C-22 -- Prohibition-count parity (Aspirational, 3 pts)
All five: "Prohibition Parity Rule" section declares "Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and fails audit." All four role blocks confirmed at exactly 5 numbered items (verified: 1-5 in each). Parity rule explicit, count >= 3, verifiable without reading action content. **PASS all.**

### C-23 -- Full-phase type coverage (Aspirational, 3 pts)
All five: "Full-Phase Type Coverage Rule" section normatively declares all four campaign phases have typed output contracts; partial coverage fails. Rule statement present with "No phase is exempt." All four phase contracts delivered with type constraints. V-02/V-04/V-05 add explicit "supplemental" scope note for the delta contract ("does not affect the four-phase coverage rule"), preventing scorer confusion. V-01/V-03 declare the rule for four phases without mentioning delta -- delta is post-Phase-4, so four-phase coverage is not violated. **PASS all.**

### C-24 -- Field-level terminal checklist (Aspirational, 3 pts)
All five inherit R6 V-05's 22-item checklist which already had:
- >= 10 items naming specific artifact fields (topic_name, namespace, priority, planned_signals, coverage_ratio, readiness_verdict, verdict_verb, hypothesis_mutation.s0, hypothesis_mutation.current, echoes, next_signal_recommendations, etc.)
- Array-field notation: planned_signals[*].target_skill, namespace_coverage[*].collection_purpose, next_signal_recommendations[*].namespace, next_signal_recommendations[*].gap_reason
- Targeted FAIL actions naming the affected phase

V-04/V-05 extend to 27 items by adding 5 delta fields (session_number, signals_added, verdict_before, verdict_after, verdict_changed) with "FAIL: re-run Session Delta" targeted actions. V-05 adds the tightest constraint: signals_added notes "absent field or string 'NONE' fails." **PASS all.**

---

## Leaderboard

| Rank | Variation | Score | C-10 Implementation Quality |
|------|-----------|-------|-----------------------------|
| 1 (tie) | V-05 | 98/98 | Typed + Analyst-owned + terminally gated + two-pass update |
| 1 (tie) | V-04 | 98/98 | Typed + terminally gated (27-item checklist) |
| 1 (tie) | V-03 | 98/98 | Analyst-owned + Phase 3 gate enforces delta.md |
| 1 (tie) | V-02 | 98/98 | Typed Session Delta Contract |
| 1 (tie) | V-01 | 98/98 | Prose delta section (minimal, sufficient) |

**All five tie at 98/98.** C-10 is binary: the criterion definition ("session delta section: signals added, verdict change summary") is satisfied at the presence level by all five. Structural quality -- typed fields, role ownership, terminal gating, two-pass update -- does not split the 3-pt aspirational award. The rubric has no partial credit mechanism for within-criterion structural quality.

**Confirmed**: The variate-writers' prediction ("all five should score 98/98 if C-10 is binary") was correct.

---

## Excellence Signals

Patterns from the R7 campaign that distinguish structural robustness, extracted from V-05 (highest structural quality, same score):

### ES-1: Two-pass delta update
delta.md written in Phase 3 Step B with a placeholder verdict_after ("NOT YET REACHED" or readiness trend estimate), then updated after Phase 4 completes with the actual verdict_verb from story.md. The terminal checklist item for verdict_after explicitly notes "must reflect Phase 4 verdict_verb; placeholder fails" -- the only order-dependent checklist item in any campaign-track variation across all rounds. The FAIL action is uniquely qualified: "re-run Phase 3 Step B after Phase 4 completes."

**Signal**: When a supplemental artifact depends on a value not yet known at its creation time, the two-pass pattern (write placeholder, update after dependency resolves) with a terminal constraint catching un-updated placeholders is the right pattern. Cleaner than deferring the artifact entirely to Phase 4.

### ES-2: Dual-contract active-role annotation
Phase 3 header: "*Analyst active. Exactly 5 forbidden actions apply. / Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*" The constraint-at-execution-site pattern from R6 V-05 extends to name both contracts at the single execution point where two artifacts are produced. A model executing Phase 3 sees both contracts without jumping to the contract section.

**Signal**: When a phase produces two artifacts under two contracts, the active-role header should name both contracts. One contract named at execution site is not enough when the phase scope has expanded.

### ES-3: Progression gate on two artifacts
Phase 3 postcondition: "status.md AND delta.md both present. status.md: 9 rows with integer fields... delta.md: all Session Delta Contract fields present and typed correctly." The conjunction gate makes delta.md non-skippable -- a model that writes status.md but omits delta.md cannot advance to Phase 4. V-01 and V-02 have no such gate; their delta is post-Phase-4 and structurally optional.

**Signal**: When a supplemental artifact is required (not advisory), place it inside a phase gate rather than after the gate. Post-Phase-4 placement with no gate makes the artifact a dashboard appendage that can be silently omitted.

### ES-4: signals_added type-tightening note
Terminal checklist item for signals_added: "list present ([] permitted; absent field or string 'NONE' fails)." The explicit rejection of the string "NONE" (the V-01 first-invocation sentinel) as a valid list value distinguishes between "correctly omitted signals" (empty list []) and "untyped prose" ("NONE"). This closes the type-inconsistency gap that V-01 and V-03 leave open.

**Signal**: When a field has a valid empty-state token (e.g., "NONE") that was carried forward from a prior untyped version, the terminal checklist item should explicitly reject that token and require the typed alternative (empty list []). Otherwise, a model trained on the prior version will produce the prose sentinel and pass a sloppy check.

---

## Verdict on Open Question

**Open question from variate-writers**: "Does C-10 require typed fields, role ownership, or terminal verification -- or only presence of signals-added and verdict-change content?"

**Answer**: C-10 requires only presence. The criterion definition is "Session delta section: signals added, verdict change summary." V-01 satisfies this with untyped named fields and a prose first-invocation string. All five variations pass; none earns partial credit via structural quality. The aspirational tier treats structural robustness as a design excellence signal, not a scoring signal.

**Implication for R8**: If a future round wants to distinguish structural quality within C-10 implementations, a new criterion (C-25 or similar) would need to specify typed delta contract, role ownership, or terminal verification as explicit pass conditions -- not just "section present."

---

## R7 Final Scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50/50 | 15/15 | 33/33 | **98/98** |
| V-02 | 50/50 | 15/15 | 33/33 | **98/98** |
| V-03 | 50/50 | 15/15 | 33/33 | **98/98** |
| V-04 | 50/50 | 15/15 | 33/33 | **98/98** |
| V-05 | 50/50 | 15/15 | 33/33 | **98/98** |

**Maximum possible**: 98/98. **All five variations reach maximum.**

campaign-track is a **complete skill** at rubric v7. All 19 criteria pass. No gap criteria remain.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["two-pass delta update -- delta.md written in Phase 3 Step B with placeholder verdict_after, updated post-Phase 4 with actual verdict_verb; terminal checklist item flags placeholder-fails as only order-dependent constraint", "dual-contract active-role annotation -- Phase 3 header names both Phase 3 Contract and Session Delta Contract at execution site when phase produces two artifacts", "conjunction progression gate -- Phase 3 postcondition requires status.md AND delta.md, making supplemental artifact non-skippable via the gate rather than post-Phase-4 appendage", "signals_added type-tightening note -- terminal item explicitly rejects string NONE sentinel and requires empty list [], closing first-invocation type-inconsistency from prior untyped versions"]}
```
