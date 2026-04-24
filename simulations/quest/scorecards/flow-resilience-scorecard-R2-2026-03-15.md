## flow-resilience — Round 2 Scoring (Rubric v2)

---

### Scoring Legend

| Symbol | Essential (C-01–C-05) | Recommended (C-06–C-08) | Aspirational (C-09–C-13) |
|--------|-----------------------|------------------------|--------------------------|
| PASS   | 12                    | 10                     | 2                        |
| PARTIAL| 6                     | 5                      | 1                        |
| FAIL   | 0                     | 0                      | 0                        |

Max: 60 essential + 30 recommended + 10 aspirational = **100**

---

### V-01 — Lifecycle Emphasis: Confidence-Annotated Discovery Phase

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Scenario Structure | PASS | Phase 2 table enforces 6-row minimum, 2 per class; all three degradation classes named |
| C-02 Four-Field Completeness | PASS | "N/A or a dash is not acceptable; rephrase or split if a field has no meaningful content" |
| C-03 Gap Identification | PASS | Phase 3 has three labeled sections (OEG, DCV, MRF); each explicitly required |
| C-04 DS Accuracy | PASS | Phase 1 confidence ratings require "architecture constraint or DS theory basis" per entry; impossible entries excluded with rationale |
| C-05 Commerce Grounding | PASS | "Commerce grounding: [Named commerce flow this disrupts]" mandatory in Phase 1; Capability column references commerce ops |
| C-06 Severity + Blast Radius | PASS | Phase 2 State column: "severity (degraded / impaired / down) and blast radius (fraction or segment of users affected)" |
| C-07 Recovery Actor Labels | PASS | Recovery column: "[client] / [server] / [operator] / [user] — each step includes trigger condition and observable signal" |
| C-08 Conflict Resolution | PASS | Phase 4 covers every Class C scenario: strategy, adequacy verdict, rationale |
| C-09 Chaos Engineering | FAIL | No chaos test cases in any phase |
| C-10 Observability Hooks | FAIL | No observability signal recommendations |
| C-11 Confidence-Annotated Discovery | PASS | Phase 1 is the confidence annotation gate: High/Medium/Low/Impossible per entry; "Impossible" excluded with retained rationale; Low entries flagged and barred from Phase 2 |
| C-12 Nil-Finding Norm | PASS | Phase 3: "If a section has no findings, state so explicitly with a scope rationale — silence is not a valid nil finding." All three gap formats provided. |
| C-13 Coverage Accountability Roster | PARTIAL | No pre-analysis roster format; minimum-per-class rule present inline ("state the architectural constraint and treat it as an architecture finding") — coverage gaps argued but not checkable against a named roster |

**Essential**: 5 × 12 = 60 | **Recommended**: 3 × 10 = 30 | **Aspirational**: 2+2+0+0+1 = 5

**V-01 Composite: 95**

---

### V-02 — Output Format: Nil-Finding Protocol in Gap Sections

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Scenario Structure | PASS | Step 1 roster (min 2 per class); Step 2 four-field analysis for each roster entry |
| C-02 Four-Field Completeness | PASS | Step 2 defines all four fields with actor-prefixed recovery steps and trigger/observable-signal requirements |
| C-03 Gap Identification | PASS | Step 3 has three subsections with nil-finding and finding formats both provided |
| C-04 DS Accuracy | PASS | DS expert role; Step 2 State requires named services/replicas; no incorrect DS claims introduced |
| C-05 Commerce Grounding | PASS | Step 2 Capability explicitly lists: "checkout, cart update, inventory browse, payment capture, order tracking" |
| C-06 Severity + Blast Radius | PASS | Step 2 State: "Include severity (degraded / impaired / down) and a blast radius estimate" |
| C-07 Recovery Actor Labels | PASS | Step 2 Recovery: "Each step prefixed with actor…include trigger condition and observable signal that it succeeded" |
| C-08 Conflict Resolution | PASS | Step 4 covers Class C scenarios with strategy, adequacy verdict, rationale; "inadequate/undefined → DCV" |
| C-09 Chaos Engineering | FAIL | Not present |
| C-10 Observability Hooks | FAIL | Not present |
| C-11 Confidence-Annotated Discovery | FAIL | Step 1 is a scenario roster with slot-filling, not a confidence-annotated discovery phase; no confidence ratings on failure modes |
| C-12 Nil-Finding Norm | PASS | Step 3: "Each subsection MUST appear…nil-finding statement — silence is not a valid nil finding." Full nil-finding format with scope rationale provided for all three gap types. |
| C-13 Coverage Accountability Roster | PARTIAL | Step 1 roster is pre-analysis and requires commerce-grounded names; but challenge mechanism is soft: "state why in one sentence" without the "topic doesn't mention X is not an argument" strictness that C-13 requires |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 0+0+0+2+1 = 3

**V-02 Composite: 93**

---

### V-03 — Phrasing Register: Accountability Roster with Challenge Mechanism

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Scenario Structure | PASS | §0 names all scenarios before analysis; §1 produces full four-field analysis per entry |
| C-02 Four-Field Completeness | PASS | §1: "Every cell is mandatory — 'N/A' or a dash is not acceptable" |
| C-03 Gap Identification | PASS | §2 has all three labeled sections; nil-finding format present for each |
| C-04 DS Accuracy | PASS | §0 impossibility arguments must cite "a CAP guarantee, deployment topology, or synchronous consistency guarantee" — DS accuracy enforced at coverage gate |
| C-05 Commerce Grounding | PASS | §0: "named, commerce-grounded scenario — not 'TBD' or 'generic failure'"; §1 Capability: "Reference specific commerce operations by name" |
| C-06 Severity + Blast Radius | PASS | §1 State: "severity (degraded / impaired / down)" and "blast radius (fraction or segment of users affected)" |
| C-07 Recovery Actor Labels | PASS | §1 Recovery: "[actor] action — trigger condition — observable success signal" |
| C-08 Conflict Resolution | PASS | §3 covers Class C scenarios with strategy, adequacy, rationale; "inadequate/undefined → DCV" |
| C-09 Chaos Engineering | FAIL | Not present |
| C-10 Observability Hooks | FAIL | Not present |
| C-11 Confidence-Annotated Discovery | FAIL | No confidence-annotated discovery phase; §0 roster commits to names upfront but does not rate scenarios by DS confidence before populating the table |
| C-12 Nil-Finding Norm | PASS | §2: nil-finding format with "— or —" structure for all three gap sections; scope rationale required |
| C-13 Coverage Accountability Roster | PASS | §0 is a formal Coverage Accountability Register: pre-analysis, ≥2 per class, "You may not proceed to §1 until every mandatory slot is filled or its impossibility argument is complete"; "'The topic doesn't mention X' is not an impossibility argument" explicitly stated; independently checkable stated |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 0+0+0+2+2 = 4

**V-03 Composite: 94**

---

### V-04 — Combination: Confidence-Annotated Discovery + Nil-Finding Protocol

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Scenario Structure | PASS | Role 2 analysis table: 6-row minimum, 2 per class; all three degradation classes |
| C-02 Four-Field Completeness | PASS | "Every cell is mandatory"; expanded table includes Commerce Flow, Severity, Blast Radius columns |
| C-03 Gap Identification | PASS | Gap Identification section: three required subsections with nil-finding protocol |
| C-04 DS Accuracy | PASS | Role 1 is explicitly "Distributed Systems Expert"; confidence ratings force explicit DS constraint reasoning; impossible entries excluded with architecture rationale |
| C-05 Commerce Grounding | PASS | Commerce Flow column: "specific operation disrupted — 'checkout — payment capture step' not just 'checkout'" |
| C-06 Severity + Blast Radius | PASS | Explicit "Severity" and "Blast Radius" as separate table columns with definitions |
| C-07 Recovery Actor Labels | PASS | Recovery column: "actor-prefixed ordered steps — [client] action — trigger — observable success signal" |
| C-08 Conflict Resolution | PASS | Conflict Resolution section covers Class C entries with strategy, adequacy, rationale; feeds back to DCV |
| C-09 Chaos Engineering | FAIL | Not present |
| C-10 Observability Hooks | FAIL | Not present |
| C-11 Confidence-Annotated Discovery | PASS | Role 1 assigns High/Medium/Low/Impossible to each failure mode; "at least 3 candidates per class (some may be excluded)"; coverage gate: "at least two Include entries per class"; flagged entries resolved before table |
| C-12 Nil-Finding Norm | PASS | Gap Identification section: "All three sections are required. Nil-finding statements are required when no findings exist — silence is not valid." Nil format with scope rationale for each gap type. |
| C-13 Coverage Accountability Roster | PARTIAL | No pre-analysis roster in §0 format; Role 1's coverage gate ("at least two Include per class") enforces coverage inline with impossibility arguments, but roster is not independently checkable against the final scenario list before analysis begins |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 0+0+2+2+1 = 5

**V-04 Composite: 95**

---

### V-05 — Combination: Confidence Gate + Nil-Finding Norm + Coverage Accountability Roster

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 Scenario Structure | PASS | §0 roster + §2 table; minimum 6 rows, 2 per class; three degradation classes enforced |
| C-02 Four-Field Completeness | PASS | §2: "Every cell is mandatory — a dash, 'N/A', or single word is not acceptable"; all columns defined |
| C-03 Gap Identification | PASS | §3a/§3b/§3c each required; nil-finding norm closes each section |
| C-04 DS Accuracy | PASS | §1 confidence catalog: High/Medium/Low/Impossible ratings with "architecture constraint or DS theory basis"; Impossible rationale retained for audit |
| C-05 Commerce Grounding | PASS | §0: "Names must be commerce-grounded (operation + failure mode) — not 'TBD'"; §2 Commerce Flow: "named operation at the specific step level" |
| C-06 Severity + Blast Radius | PASS | §2 has separate "Severity" and "Blast Radius" columns with explicit definitions |
| C-07 Recovery Actor Labels | PASS | §2 Recovery: "[actor]-prefixed ordered steps, each with trigger condition and observable success signal" |
| C-08 Conflict Resolution | PASS | §4 is the strongest of all variations: adds "Why it matters: one sentence — what failure mode occurs if strategy is wrong or undefined" beyond just adequacy verdict |
| C-09 Chaos Engineering | FAIL | Not present |
| C-10 Observability Hooks | FAIL | Not present |
| C-11 Confidence-Annotated Discovery | PASS | §1 annotates every §0 roster entry before §2 is populated; "Impossible" entries loop back to §0 vacating the slot with impossibility argument; coverage gate: "at least two Include per class or impossibility argument recorded in §0" |
| C-12 Nil-Finding Norm | PASS | §3a/§3b/§3c each have nil-finding format: "silence is not valid and cannot substitute for a nil finding. The nil-finding statement must include a scope rationale explaining why this gap type does not apply." Strongest nil-finding language of all variations. |
| C-13 Coverage Accountability Roster | PASS | §0 is pre-analysis, independently checkable, commits to ≥2 per class; impossibility argument guidance explicit: "'The topic doesn't mention X' is not an impossibility argument"; coverage gate before §1: "You may not proceed to §1 until every mandatory slot is filled or its impossibility argument is complete"; slot vacation on §1 Impossible rating routes back to §0 |

**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 0+0+2+2+2 = 6

**V-05 Composite: 96**

---

### Rankings

| Rank | Variation | Score | New Criteria Hit |
|------|-----------|-------|-----------------|
| 1 | V-05 | 96 | C-11 + C-12 + C-13 (all three) |
| 2 | V-01 | 95 | C-11 + C-12 |
| 2 | V-04 | 95 | C-11 + C-12 |
| 4 | V-03 | 94 | C-12 + C-13 |
| 5 | V-02 | 93 | C-12 only |

All variations pass all essential criteria. Golden threshold (all essentials pass + composite ≥ 80) is met by every variation.

---

### Excellence Signals from V-05

**1. Bidirectional gate between §0 and §1.** When §1 confidence rating on a §0 roster entry comes back Impossible, the slot is vacated and an impossibility argument must appear back in §0. This links the two phases bidirectionally — the roster isn't just pre-analysis commitment, it's also the landing zone for §1 rejections. The roster stays accurate even after the discovery phase revises it.

**2. Three-checkpoint auditability pipeline.** §0 (coverage commitment, pre-analysis) → §1 (confidence triage, pre-table) → §3 nil-finding norms (completeness declaration, post-analysis) creates three independently verifiable checkpoints. A reviewer can audit at any layer without reading the full analysis.

**3. "Why it matters" extension on conflict resolution.** §4 adds a causal consequence field to every adequacy judgment: "what failure mode occurs if the strategy is wrong or undefined." The other variations treat conflict resolution as a binary verdict; V-05 treats it as a risk statement. This propagates into DCV findings with stronger rationale.

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["Bidirectional gate: §1 Impossible ratings vacate §0 roster slots and require impossibility arguments in §0, keeping the pre-analysis roster accurate after discovery-phase revision", "Three-checkpoint auditability: coverage roster (pre-analysis) → confidence triage (pre-table) → nil-finding norms (post-gap) are each independently verifiable without reading the full analysis", "Causal consequence extension on conflict resolution: 'Why it matters' field forces the analysis to state the failure mode that results if the strategy is wrong or undefined, not just the adequacy verdict"]}
```
