I have the full rubric v5 (C-01 through C-21) and V-01 through V-05 from the R3 variate file. The quest-score prompt is running the R3 variations against the v5 rubric. Let me score all five.

---

# Quest Score: campaign-track — Round 5

**Rubric version**: v5 (adds C-17, C-18, C-19, C-20, C-21)
**Variations source**: campaign-track-variate-R3-2026-03-16.md

---

## V-01: Per-Role Prohibition Lists

### Criterion Scores

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Orchestration sequence | PASS | Four phases explicit: Register→Plan→Status→Narrative, distinct artifact per phase |
| C-02 | Topic registration artifact | PASS | strategy.md with namespace, priority (High/Medium/Low), ≥3 planned signals each with skill + rationale |
| C-03 | Coverage delta display | PASS | 9-namespace table Namespace\|Planned\|Collected\|Missing; missing signals named, zero-signal = "NO SIGNALS" |
| C-04 | Narrative synthesis present | PASS | Verdict CONFIRMED/REFUTED/EVOLVING/INSUFFICIENT/NOT YET REACHED + mutation block S0/current/"UNCHANGED" |
| C-05 | Session-bookend utility | PASS | Dedicated "Empty-State Handling" section, per-phase: Phase 4 verdict = NOT YET REACHED, mutation = S0 unchanged |
| C-06 | Actionable next-signal recommendations | PASS | Top-3 with namespace+skill+gap reason explicitly required |
| C-07 | Coverage ratio and readiness statement | PASS | "Coverage ratio: X collected / N planned" + READY\|NOT READY\|CONDITIONALLY READY |
| C-08 | Cross-namespace signal balance | PASS | "Zero-signal namespaces flagged explicitly with 'NO SIGNALS'" |
| C-09 | Echo integration | PASS | "At least one echo entry (unexpected finding); if none: 'NONE'" |
| C-10 | Dual-session delta | FAIL | No session delta section |
| C-11 | Role-gated phases | PASS | Four personas (Registrar/Planner/Analyst/Narrator) with dedicated sections; Registrar must not synthesize, Narrator must not plan |
| C-12 | Explicit progression gates | PASS | "Gate: Do not proceed to Phase N+1 until [artifact] is present" between every adjacent phase |
| C-13 | Empty-state as named section | PASS | "Empty-State Handling" section addresses all four phases individually with per-phase behavior |
| C-14 | Per-role prohibition lists | PASS | Each of 4 roles carries 5 explicitly enumerated forbidden actions; well over "≥2 roles with ≥1 prohibition" threshold |
| C-15 | Typed output contracts per phase | FAIL | Role descriptions and gate language present; no field-level type specification (integer vs string vs enum). Coverage table says "Named gap entries" but doesn't specify "planned: integer". Fails "at least two phases with typed specifications" |
| C-16 | Terminal completion checklist | FAIL | No TERMINAL section; completion is implicit |
| C-17 | Prohibition-to-field traceability | FAIL | Prohibitions are behavior-labeled ("Must not produce coverage tables") but no prohibition cites the guarded field name in format "MUST NOT populate \`field\` (Persona-owned)" |
| C-18 | Phase precondition gates | FAIL | Gates are end-of-phase postconditions ("Do not proceed to Phase 2 until strategy.md is present"). No precondition stated at the *start* of each phase. C-18 requires all four phases carry an explicit precondition gate before that phase begins |
| C-19 | Prohibition-field ownership table | FAIL | No table with Phase/Persona/Artifact/Field-Bound-Prohibitions structure |
| C-20 | Symmetric pre/post gate pairs | FAIL | Only postcondition gates present; no precondition gate at start of each phase to form a pair |
| C-21 | Entry-gate null declaration | FAIL | Phase 1 has no precondition declaration at all; "Gate: Do not proceed to Phase 2..." is only a postcondition |

**Essential**: 5/5 PASS  
**Recommended**: 3/3 PASS  
**Aspirational**: C-09, C-11, C-12, C-13, C-14 = 5 PASS | C-10, C-15, C-16, C-17, C-18, C-19, C-20, C-21 = 8 FAIL

**Score: 67/100**

> Scoring: Essential 10 pts each (50), Recommended 5 pts each (15), Aspirational 2.7 pts each (35 max across 13).  
> Earned: 50 + 15 + 5×2.7 = 50 + 15 + 13.5 = **78.5** → let me recount.

Aspirational PASS: C-09, C-11, C-12, C-13, C-14 = 5 criteria × 2.7 = 13.5  
Aspirational FAIL: 8 criteria × 0 = 0  
**Total: 50 + 15 + 13.5 = 78.5 → 79**

---

## V-02: Typed Output Contracts

### Criterion Scores

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Orchestration sequence | PASS | Four phases explicit with distinct typed artifacts |
| C-02 | Topic registration artifact | PASS | Phase 1 Contract: topic_name (string), namespace (one of 9), priority (one of 3), planned_signals (list ≥3 items with signal_name+target_skill+rationale) |
| C-03 | Coverage delta display | PASS | Phase 3 Contract: 9 rows, planned (integer), collected (integer), missing (list of strings), zero_signal_flag (boolean), coverage_ratio ("X/N") |
| C-04 | Narrative synthesis present | PASS | Phase 4 Contract: verdict_verb (enumerated), hypothesis_mutation {s0, current}, echoes list |
| C-05 | Session-bookend utility | PASS | Empty-State section; Phase 4 = "NOT YET REACHED", current = "UNCHANGED", echoes = ["NONE"] |
| C-06 | Actionable next-signal recommendations | PASS | next_signal_recommendations: list of exactly 3 items, each with namespace+skill+gap_reason |
| C-07 | Coverage ratio and readiness statement | PASS | coverage_ratio: "X/N" typed string, readiness_verdict: enum READY\|NOT READY\|CONDITIONALLY READY |
| C-08 | Cross-namespace signal balance | PASS | zero_signal_flag: boolean true for namespaces with both planned=0 and collected=0 |
| C-09 | Echo integration | PASS | echoes: list of strings; if empty, must contain "NONE" |
| C-10 | Dual-session delta | FAIL | No session delta section |
| C-11 | Role-gated phases | PASS | Registrar/Planner/Analyst/Narrator named, phase assignment explicit |
| C-12 | Explicit progression gates | PASS | "Gate: Do not proceed to Phase N until [artifact] contains all required fields with correct types" — gates on both artifact presence AND type compliance |
| C-13 | Empty-state as named section | PASS | "### First Invocation (0 signals collected)" — dedicated section, all four phases addressed with typed field values |
| C-14 | Per-role prohibition lists | FAIL | Roles named and assigned but no enumerated forbidden actions. "Registrar: Runs topic-new. Produces strategy.md per Phase 1 Contract." — description only, no prohibitions |
| C-15 | Typed output contracts per phase | PASS | Phase 1: 5-field contract with types. Phase 2: namespace+planned_skills+rationale typed. Phase 3: planned/collected integer, missing string[], coverage_ratio "X/N". Phase 4: verdict_verb enum, all sub-fields typed. All four phases fully typed |
| C-16 | Terminal completion checklist | FAIL | No TERMINAL section |
| C-17 | Prohibition-to-field traceability | FAIL | No prohibitions at all |
| C-18 | Phase precondition gates | FAIL | Same pattern as V-01: end-of-phase postcondition gates, no start-of-phase preconditions |
| C-19 | Prohibition-field ownership table | FAIL | No table |
| C-20 | Symmetric pre/post gate pairs | FAIL | Postcondition gates only |
| C-21 | Entry-gate null declaration | FAIL | Phase 1 has no precondition |

**Essential**: 5/5 PASS  
**Recommended**: 3/3 PASS  
**Aspirational PASS**: C-09, C-11, C-12, C-13, C-15 = 5 × 2.7 = 13.5  
**Total: 50 + 15 + 13.5 = 78.5 → 79**

Same score as V-01. V-02 gains C-15 but loses C-14.

---

## V-03: Terminal Completion Checklist

### Criterion Scores

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Orchestration sequence | PASS | Four phases in order with distinct artifacts |
| C-02 | Topic registration artifact | PASS | strategy.md with topic, namespace, priority, ≥3 signals each with name+skill+rationale |
| C-03 | Coverage delta display | PASS | 9-namespace table; zero-signal namespaces flagged "NO SIGNALS"; named missing signals |
| C-04 | Narrative synthesis present | PASS | Verdict vocab + S0 mutation block + "UNCHANGED" option |
| C-05 | Session-bookend utility | PASS | Dedicated "First Invocation (0 signals collected)" section; all four phases addressed with per-phase behavior |
| C-06 | Actionable next-signal recommendations | PASS | Top-3 with namespace+skill+gap reason |
| C-07 | Coverage ratio and readiness statement | PASS | Coverage ratio + readiness verdict enum |
| C-08 | Cross-namespace signal balance | PASS | Zero-signal flag |
| C-09 | Echo integration | PASS | Echo entries with "NONE" fallback |
| C-10 | Dual-session delta | FAIL | No session delta |
| C-11 | Role-gated phases | PASS | Registrar/Planner/Analyst/Narrator named in role section |
| C-12 | Explicit progression gates | PASS | "Gate: Do not proceed to Phase N+1 until [artifact] present" — all four adjacent transitions |
| C-13 | Empty-state as named section | PASS | "### First Invocation (0 signals collected)" — dedicated labeled section with all four phases |
| C-14 | Per-role prohibition lists | FAIL | Role descriptions only (name + phase + sub-skill) — no enumerated forbidden actions |
| C-15 | Typed output contracts per phase | FAIL | Fields described narratively ("list planned signals with rationale") but no type specifications |
| C-16 | Terminal completion checklist | PASS | TERMINAL section with four items, each as "[ ] Phase N postcondition: [artifact] AND [fields] PASS/FAIL — re-run if FAIL" |
| C-17 | Prohibition-to-field traceability | FAIL | No prohibitions |
| C-18 | Phase precondition gates | FAIL | End-of-phase postcondition gates only |
| C-19 | Prohibition-field ownership table | FAIL | No table |
| C-20 | Symmetric pre/post gate pairs | FAIL | Postconditions only |
| C-21 | Entry-gate null declaration | FAIL | No Phase 1 precondition declaration |

**Essential**: 5/5  
**Recommended**: 3/3  
**Aspirational PASS**: C-09, C-11, C-12, C-13, C-16 = 5 × 2.7 = 13.5  
**Total: 50 + 15 + 13.5 = 78.5 → 79**

Three-way tie at 79. V-01, V-02, V-03 each target a single R2 axis and each pass exactly the same 5 aspirationals (swapping C-14/C-15/C-16 accordingly).

---

## V-04: Per-Role Prohibitions + Typed Output Contracts

### Criterion Scores

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Orchestration sequence | PASS | Four phases explicit |
| C-02 | Topic registration artifact | PASS | Phase 1 Contract: topic_name (string), namespace (one of 9), priority (one of 3 tokens), planned_signals (list ≥3 with all sub-fields typed) |
| C-03 | Coverage delta display | PASS | Phase 3 Contract: 9 rows required, integer cells, missing as named string list, zero_flag "NO SIGNALS", coverage_ratio "X/N" |
| C-04 | Narrative synthesis present | PASS | Phase 4 Contract: verdict_verb enumerated, hypothesis_mutation typed {s0, current}, echoes list typed |
| C-05 | Session-bookend utility | PASS | "First Invocation (0 signals collected)" section; all four phases with typed empty-state values |
| C-06 | Actionable next-signal recommendations | PASS | next_signals typed: 3 items, each namespace+skill+gap_reason |
| C-07 | Coverage ratio and readiness statement | PASS | coverage_ratio "X/N" format-typed, readiness_verdict exact enum |
| C-08 | Cross-namespace signal balance | PASS | zero_flag = "NO SIGNALS" typed condition |
| C-09 | Echo integration | PASS | echoes list minimum ["NONE"] |
| C-10 | Dual-session delta | FAIL | No session delta |
| C-11 | Role-gated phases | PASS | Four personas with phase-exclusive sub-skills and full prohibition lists |
| C-12 | Explicit progression gates | PASS | "Gate: Do not proceed to Phase N+1 until [artifact] present" on all typed-field conditions |
| C-13 | Empty-state as named section | PASS | Dedicated section; all four phases addressed with typed empty-state field values |
| C-14 | Per-role prohibition lists | PASS | Each of 4 roles: 5 enumerated forbidden actions; Analyst explicitly "Must not use prose counts ('several', 'many') where integers are required" — operationally specific |
| C-15 | Typed output contracts per phase | PASS | All four phases fully typed with field names, types, enumerated tokens, format constraints |
| C-16 | Terminal completion checklist | FAIL | No TERMINAL section |
| C-17 | Prohibition-to-field traceability | PARTIAL | Analyst prohibition "Must not use prose counts where integers are required" implicitly guards `planned` and `collected` fields; Narrator "Must not paraphrase verdict verbs" guards `verdict_verb`. Field names not explicitly cited in "MUST NOT populate `field` (Persona-owned)" format, but typed contracts + prohibition lists together make the guarded fields inferrable. Closest any R3 variation gets to C-17, but still prose-adjacent rather than formally field-bound |
| C-18 | Phase precondition gates | FAIL | End-of-phase postcondition gates only |
| C-19 | Prohibition-field ownership table | FAIL | No compact table |
| C-20 | Symmetric pre/post gate pairs | FAIL | Postconditions only |
| C-21 | Entry-gate null declaration | FAIL | No Phase 1 precondition |

**Essential**: 5/5  
**Recommended**: 3/3  
**Aspirational PASS**: C-09, C-11, C-12, C-13, C-14, C-15 = 6 × 2.7 = 16.2  
**Aspirational PARTIAL**: C-17 = 1 × 1.35 = 1.35  
**Total: 50 + 15 + 16.2 + 1.35 = 82.55 → 83**

V-04 breaks from the three-way tie — the dual enforcement of C-14 + C-15 together surfaces C-17 proximity that neither axis alone reached.

---

## V-05: Full Stack (Prohibitions + Typed Contracts + Terminal Checklist + Lifecycle)

### Criterion Scores

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Orchestration sequence | PASS | "This campaign runs in exactly four phases: Register → Plan → Status → Narrative"; distinct artifacts, explicit phase structure |
| C-02 | Topic registration artifact | PASS | Phase 1 Contract: topic_name (string), namespace (exact one of 9 tokens listed), priority (one of 3 tokens), planned_signals (list ≥3, each with 3 typed sub-fields) |
| C-03 | Coverage delta display | PASS | Phase 3 Contract: all 9 rows required, planned/collected integers, missing string list, coverage_ratio "X/N" format |
| C-04 | Narrative synthesis present | PASS | Phase 4 Contract: verdict_verb (5-token enum), hypothesis_mutation {s0, current or "UNCHANGED"}, at least one S0 required |
| C-05 | Session-bookend utility | PASS | "First Invocation (0 signals collected)" section; all four phases with typed empty-state values; Phase 4 = "NOT YET REACHED" / current = "UNCHANGED" |
| C-06 | Actionable next-signal recommendations | PASS | next_signal_recommendations: exactly 3 items typed with namespace+skill+gap_reason |
| C-07 | Coverage ratio and readiness statement | PASS | coverage_ratio "X/N", readiness_verdict one of 3 tokens |
| C-08 | Cross-namespace signal balance | PASS | zero_flag = "NO SIGNALS" for planned=0 AND collected=0 |
| C-09 | Echo integration | PASS | echoes list minimum ["NONE"] — "absent field fails" explicitly stated |
| C-10 | Dual-session delta | FAIL | No session delta section |
| C-11 | Role-gated phases | PASS | Four roles with active persona markers at each phase section ("*Registrar active. All Phase 1 forbidden actions apply.*") — strongest role-gating signal across all R3 variations |
| C-12 | Explicit progression gates | PASS | "GATE: Do not proceed to Phase N+1 until Phase N postcondition is satisfied" — explicit, labeled GATE keyword on all transitions |
| C-13 | Empty-state as named section | PASS | "### First Invocation (0 signals collected)" dedicated section; all four phases with typed empty-state contracts |
| C-14 | Per-role prohibition lists | PASS | All 4 roles: 5 enumerated forbidden actions labeled 1–5; Narrator "Must not paraphrase verdict verbs — only exact Phase 4 Contract tokens are valid" — strongest operationalization across all variations |
| C-15 | Typed output contracts per phase | PASS | All four phases fully typed; Phase 3 explicitly states "planned and collected are integers — no narrative, no ranges"; Phase 4 contract specifies exact 5-token enum |
| C-16 | Terminal completion checklist | PASS | TERMINAL section: 4 items, each with "[ ] Phase N PASS condition" explicitly listing required typed fields plus "Result: PASS / FAIL" |
| C-17 | Prohibition-to-field traceability | PARTIAL | Phase 3 GATE postcondition: "planned and collected are integers verified" references the fields; Analyst prohibition #5 "Must not use narrative counts where integers are required" guards integer fields. Phase 4 GATE references "verdict_verb is one of 5 tokens." Typed contracts and prohibitions together trace to fields but no explicit "MUST NOT populate `<field>` (Persona-owned)" line |
| C-18 | Phase precondition gates | FAIL | Gates are placed at end of preceding phase or as GATE blocks at end of each phase. Phases do not open with "Precondition: [artifact X] must exist before this phase begins." Pattern is postcondition-heavy — no true start-of-phase precondition |
| C-19 | Prohibition-field ownership table | FAIL | No Phase/Persona/Artifact/Field-Bound-Prohibitions table |
| C-20 | Symmetric pre/post gate pairs | FAIL | No explicit precondition gates at phase start — only postconditions. Phase pairs are asymmetric |
| C-21 | Entry-gate null declaration | FAIL | Phase 1 has no "this is the entry gate, no prior artifact required" declaration |

**Essential**: 5/5  
**Recommended**: 3/3  
**Aspirational PASS**: C-09, C-11, C-12, C-13, C-14, C-15, C-16 = 7 × 2.7 = 18.9  
**Aspirational PARTIAL**: C-17 = 1 × 1.35 = 1.35  
**Total: 50 + 15 + 18.9 + 1.35 = 85.25 → 85**

---

## Composite Rankings

| Rank | Variation | Score | Criteria Passed | Key Win | Key Gap |
|------|-----------|-------|-----------------|---------|---------|
| 1 | V-05 | **85** | All essential + recommended; C-09/C-11–C-16; C-17 partial | Only variation passing C-14+C-15+C-16 simultaneously; active persona markers per phase | C-17 partial only; C-18/C-19/C-20/C-21 all fail |
| 2 | V-04 | **83** | All essential + recommended; C-09/C-11–C-15; C-17 partial | C-14+C-15 combination surfaces C-17 proximity; typed contracts strongest per-field enforcement | No C-16 terminal checklist |
| 3 (tie) | V-01 | **79** | All essential + recommended; C-09/C-11–C-14 | Per-role prohibition lists strongest single-axis coverage | Misses C-15, C-16, C-17–C-21 |
| 3 (tie) | V-02 | **79** | All essential + recommended; C-09/C-11–C-13/C-15 | Typed contracts strongest single-axis coverage | Misses C-14, C-16, C-17–C-21 |
| 3 (tie) | V-03 | **79** | All essential + recommended; C-09/C-11–C-13/C-16 | Terminal checklist cleanest single-axis coverage; PASS/FAIL re-run semantics | Misses C-14, C-15, C-17–C-21 |

**Predicted leaderboard was V-05 > V-04 > V-01=V-02=V-03** — confirmed exactly.

---

## Excellence Signals (from V-05)

The R5 rubric added C-18, C-19, C-20, C-21. V-05 scored 85 but fails all four. The gap reveals three structural patterns missing across all R3 variations:

**Signal 1 — Precondition gates are absent from every variation**  
All R3 variations use end-of-phase postconditions ("do not proceed until X is written"). No variation opens a phase section with "Precondition: [prior artifact] must exist before this phase begins." C-18 scores zero across all five. C-20 (symmetric pairs) requires both — and can't pass without C-18. The fix is structural: each phase section needs a precondition header.

**Signal 2 — Phase 1 has no entry gate in any variation**  
V-05 Phase 1 opens with "Registrar active. All Phase 1 forbidden actions apply." — but no null precondition declaration. C-21 requires Phase 1 explicitly say "None — entry gate, no prior artifact required." This is a one-line addition that unlocks Phase 1 symmetry with all other phases.

**Signal 3 — Prohibitions guard behaviors, not fields**  
C-19 requires a compact table with Phase/Persona/Artifact/Field-Bound columns, with field names cited in prohibitions. V-04 and V-05 get closest (Analyst prohibition guards integer fields implicitly), but no variation writes "MUST NOT populate `planned` (Analyst-owned field)." C-17 and C-19 remain partially blocked by the same root gap.

---

## New R5 Patterns for Next Rubric

1. **Pre/post gate symmetry within phase section**: Phase 2–4 open with a labeled precondition ("Precondition: [prior artifact] must exist") and close with a labeled postcondition GATE. Both in the same section block, paired explicitly.

2. **Phase 1 null entry gate**: Phase 1 carries a precondition section that reads "None — this is the entry gate" or equivalent. Makes Phase 1 structurally parallel to all other phases.

---

```json
{"top_score": 85, "all_essential_pass": true, "new_patterns": ["pre/post gate symmetry within phase section: each phase opens with named precondition and closes with named postcondition in the same block", "Phase 1 null entry gate: Phase 1 precondition explicitly declared as null/none using entry-gate language"]}
```
