## prove-prototype R16 Scorecard — v15 Rubric (304 pts ceiling)

**Rubric**: v15 (adds C-40, C-41, C-42; ceiling 304)
**Base**: R15 scored 279/279 under v14. All five variations build on R15 base.
**New criteria under evaluation**: C-40 (+7), C-41 (+8), C-42 (+10)

---

### Baseline Confirmation (C-01 – C-39)

All five variations inherit the R15 base without modification to any prior structure. C-01 through C-39 (279 pts) carry forward PASS across V-01 – V-05.

Critical prerequisites for new criteria:
- **C-35** (manifest, required by C-40 + C-42): All five have manifest before any container body. ✓
- **C-29** (competitor identified in CALIBRATE, required by C-40): Phase 4 CALIBRATOR with INERTIA COMPETITOR labeled block in all five. ✓
- **C-37** (forward-reference COMPLETE lines, required by C-42): All non-terminal CONTAINER COMPLETE lines carry `→ [NEXT] receives:` clauses. ✓
- **C-23, C-38, C-39** (role prohibition stack, required by C-41): Phase-level role headers with MUST/FORBIDDEN inline, hard modal throughout in all five. ✓

All prerequisites satisfied. New criteria evaluation proceeds.

---

### New Criteria Evaluation

#### C-40 — Manifest competitor lifecycle column (7 pts)

Pass condition: Manifest has "Competitor status" column tracking four states. Each CONTAINER COMPLETE line that advances status carries an annotation.

| Var | Column present | All 4 states | DESIGN COMPLETE annotation | CALIBRATE COMPLETE annotation | BUILD COMPLETE annotation | CLOSE COMPLETE annotation | Verdict |
|-----|---------------|-------------|---------------------------|------------------------------|--------------------------|--------------------------|---------|
| V-01 | ✓ | ✓ | "Competitor status: NOT YET IDENTIFIED" | "Competitor status: IDENTIFIED AND COMMITTED — '[name]' committed as B-00 baseline" | "Competitor status: REFERENCED — B-00 from '[name]' carried as comparison baseline into CLOSE" | "Competitor status: DISCHARGED — '[name]' fully incorporated in results table baseline column and terminal arc record" | **PASS** |
| V-02 | ✓ | ✓ | "Competitor identification FORBIDDEN here — REQUIRED in CALIBRATE. Competitor status: NOT YET IDENTIFIED" | "Competitor status: IDENTIFIED AND COMMITTED — '[name]' committed as B-00 baseline" | "Competitor status: REFERENCED — B-00 from '[name]' carried into CLOSE" | "Competitor status: DISCHARGED — '[name]' incorporated in results table and arc record" | **PASS** |
| V-03 | ✓ | ✓ + lifecycle framing paragraph before manifest | "Competitor lifecycle — status at DESIGN exit: NOT YET IDENTIFIED. FORBIDDEN: Identification MUST NOT occur before CALIBRATE." | "Competitor lifecycle — status at CALIBRATE exit: IDENTIFIED AND COMMITTED — '[name]' named and B-00 committed before any build activity begins." | "Competitor lifecycle — status at BUILD exit: REFERENCED — B-00 from '[name]' active as comparison standard; verdict and discharge occur in CLOSE." | "Competitor lifecycle — status at CLOSE exit: DISCHARGED — '[name]' incorporated in results table baseline column (Phase 7), arc record (this line); all four lifecycle states traversed." | **PASS** (depth++) |
| V-04 | ✓ | ✓ | "Competitor status: NOT YET IDENTIFIED" | "Competitor status: IDENTIFIED AND COMMITTED — '[name]' committed as B-00 baseline" | "Competitor status: REFERENCED — B-00 from '[name]' carried into CLOSE" | "Competitor status: DISCHARGED — '[name]' fully incorporated in results table baseline column and arc record" | **PASS** |
| V-05 | ✓ | ✓ | "Thread 1 (competitor lifecycle) — status at DESIGN: NOT YET IDENTIFIED. Identification is FORBIDDEN before CALIBRATE." | "Thread 1 (competitor lifecycle) — status at CALIBRATE: IDENTIFIED AND COMMITTED — '[name]' named and B-00 committed; lifecycle advances to REFERENCED in BUILD." | "Thread 1 (competitor lifecycle) — status at BUILD: REFERENCED — B-00 from '[name]' active as comparison baseline; competitor reaches DISCHARGED in CLOSE." | "Thread 1 (competitor lifecycle) — DISCHARGED: '[name]' traversed all four states (NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED); incorporated in results table baseline column and this arc record." | **PASS** (depth++) |

**C-40 finding**: All five PASS. V-03 and V-05 exceed minimum — V-03 adds container-level lifecycle sub-headers and phase-prohibition annotations with lifecycle state context; V-05 names the lifecycle as a thread, propagates the thread label explicitly, and embeds the full four-state chain in the terminal record.

---

#### C-41 — CLOSE sub-role split COMPARATOR/AUDITOR with handoff (8 pts)

Pass condition: CLOSE container header enumerates both sub-roles with disjoint phase scopes. Phase 8 COMPLETE carries "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR." Cross-prohibitions in hard modal.

| Var | Container-level sub-role table | Phase scopes explicit | Phase 8 handoff marker | Cross-prohibitions hard modal | Phase-level inline role headers (C-38 satisfied) | Verdict |
|-----|-------------------------------|----------------------|----------------------|------------------------------|--------------------------------------------------|---------|
| V-01 | ✓ 4-col: sub-role / scope / writes / FORBIDDEN | COMPARATOR 7-8; AUDITOR 9-11 | "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" ✓ | FORBIDDEN throughout in table + phase headers | Phase 7 "COMPARATOR (MUST write: ...; FORBIDDEN to write: ...)" etc. ✓ | **PASS** |
| V-02 | ✓ 3-col: sub-role / phases / FORBIDDEN (no MUST write column) | COMPARATOR 7-8; AUDITOR 9-11 | "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" ✓ | FORBIDDEN in table; MUST/FORBIDDEN in phase headers | Phase 7/8/9/10/11 headers carry role + inline MUST/FORBIDDEN ✓ | **PASS** |
| V-03 | ✓ 4-col table | COMPARATOR 7-8; AUDITOR 9-11 | "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" ✓ | Hard modal throughout ✓ | Phase headers carry role + inline MUST/FORBIDDEN ✓ | **PASS** |
| V-04 | ✓ Dedicated "CLOSE Sub-Role Architecture" section with named role headers, scope rationale, and separate "Phase 8/9 handoff — REQUIRED structural event" subsection | COMPARATOR 7-8 with rationale; AUDITOR 9-11 with rationale | "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" ✓ **plus** separate "AUDITOR takes over from this point. REQUIRED: Confirm Phase 8 handoff marker present before executing Phase 9." bidirectional confirmation | Hard modal throughout ✓ | Phase headers carry role + inline MUST/FORBIDDEN ✓ | **PASS** (depth++) |
| V-05 | ✓ 4-col table | COMPARATOR 7-8; AUDITOR 9-11 | "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" ✓; Phase 9 header carries "REQUIRED: Confirm handoff before executing" | Hard modal throughout ✓ | Phase headers carry role + inline MUST/FORBIDDEN ✓ | **PASS** |

**C-41 finding**: All five PASS. V-04 exceeds minimum with a dedicated sub-role architecture section and bidirectional handoff (COMPARATOR declares → AUDITOR confirms receipt). V-05 carries the bidirectional confirmation inline at Phase 9's prerequisite gate.

---

#### C-42 — Value Flow Ledger with ledger-discharge at CLOSE COMPLETE (10 pts)

Pass condition: Standalone Value Flow Ledger after manifest, before any container body. All 12 experimental values listed with producing and first consuming phase. CLOSE COMPLETE carries ledger-discharge confirmation distinct from C-36 arc record.

| Var | Ledger placement | All 12 values | Role-annotated phases | CLOSE COMPLETE ledger discharge | Verdict |
|-----|-----------------|--------------|----------------------|--------------------------------|---------|
| V-01 | ✓ After manifest header, before CONTAINER: DESIGN | ✓ All 12 (hypothesis text, scope exclusions, success threshold, failure threshold, competitor name, B-00, outperform threshold, prototype description, raw result, delta rationale, verdict word, counter-evidence disposition) | ✓ "Phase 1 (FRAMER)", "Phase 4 (CALIBRATOR)", "Phase 8 (COMPARATOR — verdict grounding)", etc. | "Value ledger: [FULLY DISCHARGED \| PARTIAL — [N] values unresolved]" ✓ | **PASS** |
| V-02 | ✓ After manifest, before CONTAINER: DESIGN | ✓ All 12 | Abbreviated: "Phase 1", "Phase 2", etc. (no role names) — criterion doesn't require role labels | "Value ledger: [FULLY DISCHARGED \| PARTIAL — [N] values unresolved]" ✓ | **PASS** |
| V-03 | ✓ After manifest, before CONTAINER: DESIGN | ✓ All 12 with role annotations | ✓ Role-annotated | "Value ledger: [FULLY DISCHARGED \| PARTIAL — [N] values unresolved]" ✓ | **PASS** |
| V-04 | ✓ After manifest, before CONTAINER: DESIGN | ✓ All 12 with role annotations | ✓ Role-annotated | "Value ledger: [FULLY DISCHARGED \| PARTIAL — [N] values unresolved]" ✓ | **PASS** |
| V-05 | ✓ After manifest, before CONTAINER: DESIGN | ✓ All 12 with role annotations | ✓ Role-annotated | "Value ledger: [FULLY DISCHARGED \| PARTIAL — [N] values unresolved]" ✓ | **PASS** |

Note on V-05 terminal integration: "REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four containers, confirm competitor lifecycle DISCHARGED, confirm COMPARATOR/AUDITOR handoff executed, and confirm ledger discharge status." — V-05 explicitly scopes all three new criteria as required terminal confirmations, creating a structural guarantee that none is omitted.

---

### Composite Scores

| Tier | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-----|------|------|------|------|------|
| Essential (C-01–C-05) | 60 | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–C-08) | 30 | 30 | 30 | 30 | 30 | 30 |
| Aspirational prior (C-09–C-39) | 164 | 164 | 164 | 164 | 164 | 164 |
| Excellence (C-11–C-15) | 10 | 10 | 10 | 10 | 10 | 10 |
| **C-40 (new, +7)** | 7 | **7** | **7** | **7** | **7** | **7** |
| **C-41 (new, +8)** | 8 | **8** | **8** | **8** | **8** | **8** |
| **C-42 (new, +10)** | 10 | **10** | **10** | **10** | **10** | **10** |
| **TOTAL** | **304** | **304** | **304** | **304** | **304** | **304** |

All essential criteria PASS across all variations.

---

### Ranking

All five variations reach the 304/304 ceiling. Ranking by structural depth, robustness, and quality of criterion satisfaction:

| Rank | Variation | Distinguishing structural contribution |
|------|-----------|--------------------------------------|
| 1 | **V-05** | Dual-thread convergence architecture — C-40 and C-41 named as Thread 1/Thread 2 in manifest preamble; propagated as named labels through every CONTAINER COMPLETE boundary; CLOSE COMPLETE explicitly required to discharge all three new criteria simultaneously with Thread 1 lifecycle chain encoded verbatim |
| 2 | **V-04** | Deepest C-41 architecture — dedicated "CLOSE Sub-Role Architecture" section with scope rationale per role; Phase 8/9 transition elevated to "REQUIRED structural event" subsection; bidirectional handoff (COMPARATOR declares at Phase 8 COMPLETE, AUDITOR confirms receipt at Phase 9 entry); CLOSE COMPLETE confirms "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" |
| 3 | **V-03** | Richest C-40 documentation — competitor lifecycle framing paragraph before manifest explains the four-state progression; each container header annotated with incoming lifecycle state; DESIGN container carries "competitor does not exist yet" rationale; Phase 2/3 prohibitions annotated with lifecycle state context; CALIBRATE Phase 4 narrates the two sub-transitions (NOT YET IDENTIFIED → IDENTIFIED; IDENTIFIED → IDENTIFIED AND COMMITTED) |
| 4 | **V-01** | Full balanced elaboration — all three new criteria at complete specification depth; phase-body scaffolding maximally instructive for model execution; C-40 annotations present on all CONTAINER COMPLETE lines; C-41 table has full MUST write + FORBIDDEN columns; C-42 ledger role-annotated |
| 5 | **V-02** | Compressed — all three new criteria structurally present and criterion-passing; C-42 ledger uses abbreviated phase labels (no role names); C-41 container-level table omits MUST write column (satisfied by phase-level headers per C-38); minimal elaboration may reduce execution fidelity |

---

### Excellence Signals (from V-05)

Three patterns in V-05 made it the top-ranked variation:

**1. Named structural thread architecture (new)**
Abstracting C-40 and C-41 into explicit named threads ("Thread 1 — Competitor lifecycle" and "Thread 2 — CLOSE role sequencing") in the manifest preamble creates a document-level vocabulary for the two independent accountability concerns. The thread names propagate uniformly through every CONTAINER COMPLETE annotation, making each concern independently scannable without reconstructing it from phase bodies. This is a new structural pattern — R15 variations tracked these concerns implicitly through annotation content; V-05 makes each concern a named, labeled structural object.

**2. Convergence point declaration (new)**
Explicitly declaring that both threads terminate at the same structural point ("Both threads terminate at CONTAINER: CLOSE COMPLETE — the competitor reaches DISCHARGED and the AUDITOR completes Phase 11 simultaneously. The terminal line confirms both.") prevents the two concerns from appearing to be in tension. It also creates a contractual obligation: the terminal line must confirm both thread discharges plus the ledger discharge, making CLOSE COMPLETE a three-criterion audit checkpoint. The output contract for the terminal line reads: "REQUIRED: The terminal CONTAINER: CLOSE COMPLETE line MUST encode results from all four containers, confirm competitor lifecycle DISCHARGED, confirm COMPARATOR/AUDITOR handoff executed, and confirm ledger discharge status." — no prior variation required all three simultaneously at a named contract point.

**3. Full lifecycle chain embedded in terminal arc record (new)**
V-05's CLOSE COMPLETE Thread 1 discharge line encodes the complete four-state progression verbatim: "NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED" alongside the competitor name. This makes the terminal arc record a self-contained audit of the competitor lifecycle without requiring the reader to scan the intermediate CONTAINER COMPLETE lines. Combined with C-36's requirement that the terminal line encode the full experimental arc, V-05 creates a terminal line that is simultaneously: a C-36 arc record, a C-40 lifecycle discharge confirmation, a C-41 sub-role contract discharge confirmation, and a C-42 ledger discharge confirmation.

---

```json
{"top_score": 304, "all_essential_pass": true, "new_patterns": ["named structural thread architecture — abstracting C-40 and C-41 into Thread 1/Thread 2 labels propagated through every CONTAINER COMPLETE boundary, creating independently scannable accountability concerns", "convergence point declaration — explicit contract that both threads (document-level lifecycle + container-level role sequencing) and ledger all discharge at CONTAINER: CLOSE COMPLETE, making the terminal line a three-criterion audit checkpoint", "full lifecycle chain in terminal arc record — embedding the complete four-state progression verbatim in the Thread 1 discharge line, making the terminal line a self-contained audit of the competitor lifecycle without scanning intermediate boundaries"]}
```
