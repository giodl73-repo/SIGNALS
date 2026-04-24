# Scorecard — flow-conversation — Round 7 (2026-03-14)

**Rubric version:** v6 | **Variations scored:** V-01 through V-05

---

## Variation Summaries

| ID | Axis | Key Addition Over v6 Baseline |
|----|------|-------------------------------|
| V-01 | Recovery path closure | Phase 3-R: mandatory RECOVERY record per FOUND defect; RECOVERABLE[min_turns, target] \| UNRECOVERABLE[reason] verdict |
| V-02 | Reachability completeness | Phase 0-D-5 REACHABILITY_MAP (entry → closure); REACHABILITY_STATUS column; C-08 becomes hard requirement (reachable_visited / total_reachable) |
| V-03 | Session variable persistence scope | PERSISTENCE_CLASS tracking in SESSION_STATE column; class transitions visible at topic-exit boundaries; persistence violation as candidate 5th defect class |
| V-04 | Defect severity triage | Phase 2 adds SEVERITY: P0\|P1\|P2 + BUSINESS_IMPACT per FOUND row; CONFIRMED_ABSENT rows add RISK_EXPOSURE field |
| V-05 | Clean baseline | Faithful implementation of C-01 through C-18; no new structural addition |

---

## Criterion Scoring

Weight reference: Essential C-01–C-04 = 15 pts each (60 total) · Recommended C-05–C-07 = 10 pts each (30 total) · Aspirational C-08–C-18 = 10 pts total (C-08 = 1 pt; C-09–C-18 = 0.9 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** turn-by-turn trace | PASS | PASS | PASS | PASS | PASS |
| **C-02** all 4 defect classes | PASS | PASS | PASS | PASS | PASS |
| **C-03** session state tracked | PASS | PASS | PASS | PASS | PASS |
| **C-04** CS vocabulary | PASS | PASS | PASS | PASS | PASS |
| **C-05** defect reproduction | PASS | PASS | PASS | PASS | PASS |
| **C-06** fallback chain | PASS | PASS | PASS | PASS | PASS |
| **C-07** collision disambiguation | PASS | PASS | PASS | PASS | PASS |
| **C-08** graph coverage metric | PARTIAL | **PASS** | PARTIAL | FAIL | PARTIAL |
| **C-09** (aspirational v1) | PASS | PASS | PASS | PASS | PASS |
| **C-10** prohibited vocab gate | PASS | PASS | PASS | PARTIAL | PASS |
| **C-11** turn-level conformance | PASS | PASS | PASS | PASS | PASS |
| **C-12** role-separated audit | PASS | PASS | PASS | PASS | PASS |
| **C-13** typed assertion fields | PASS | PASS | PASS | PARTIAL | PASS |
| **C-14** contract-first schema | PASS | PASS | PASS | PASS | PASS |
| **C-15** table columns structural | PASS | PASS | PASS | PASS | PASS |
| **C-16** developer pre-contract | PASS | PASS | PASS | PASS | PASS |
| **C-17** gap-closure annotation | PASS | PASS | PASS | PARTIAL | PASS |
| **C-18** invariant registry | PASS | PASS | PASS | **FAIL** | PASS |

### Evidence notes

**V-01**
- C-08 PARTIAL: No coverage ratio explicitly required; Phase 3-R recovery traversal implies node visits but no metric enforced
- All other criteria structurally enforced by phase gates and schema declarations

**V-02**
- C-08 PASS: REACHABILITY_MAP produces coverage ratio as first-class output; this is the first variation to fully satisfy C-08
- All other criteria inherit from established v6 baseline

**V-03**
- C-08 PARTIAL: Persistence focus enriches C-03 but does not require a coverage ratio
- Persistence violation as a defect class is an extension of C-03, not a structural novelty — it does not generate a new criterion

**V-04**
- C-08 FAIL: Severity triage emphasis displaces graph coverage; no metric required
- C-10 PARTIAL: Severity framing introduces business-domain terms ("high-impact", "critical") that may leak generic vocabulary into otherwise clean CS output
- C-13 PARTIAL: SEVERITY field uses free-text justification in BUSINESS_IMPACT — breaks typed-verdict discipline
- C-17 PARTIAL: GAP_CLOSURE_VERDICT annotations deprioritized when severity triage frame dominates
- C-18 FAIL: Severity focus displaces invariant registry entirely; CONFIRMED_ABSENT rows cite SEVERITY: N/A rather than INVARIANT-ID — a contract violation under C-18

**V-05**
- C-08 PARTIAL: No forcing function for coverage ratio; baseline prompt does not require a metric

---

## Composite Scores

| Variation | Essential /60 | Recommended /30 | Aspirational /10 | **Total /100** |
|-----------|---------------|-----------------|------------------|----------------|
| V-01 | 60 | 30 | 9.5 | **99** |
| V-02 | 60 | 30 | **10.0** | **100** |
| V-03 | 60 | 30 | 9.5 | **99** |
| V-04 | 60 | 30 | 6.8 | **97** |
| V-05 | 60 | 30 | 9.5 | **99** |

Aspirational detail: C-08 PASS = 1.0 / PARTIAL = 0.5 / FAIL = 0. C-18 FAIL loses 0.9. C-10, C-13, C-17 PARTIAL each lose 0.45.

---

## Ranking

| Rank | Variation | Score | Distinguishing factor |
|------|-----------|-------|----------------------|
| 1 | **V-02** | 100 | First variation to fully satisfy C-08 via reachability coverage ratio |
| 2 (tie) | **V-01** | 99 | Strongest new pattern (recovery closure); C-08 only weakness |
| 2 (tie) | **V-03** | 99 | C-03 enrichment via persistence class transitions; no new criterion |
| 2 (tie) | **V-05** | 99 | Cleanest implementation of existing rubric; no new patterns |
| 5 | **V-04** | 97 | Severity triage corrupts typed-verdict discipline and displaces C-18 |

---

## Excellence Signals

**From V-02 (top scorer):**
- **Reachability closure as Phase 0-D artifact**: Pre-computing which topics are reachable from the entry point exposes orphaned topics — a structural defect class absent from all four current defect categories. Reachability is a property of the graph, not of any individual execution trace; it requires its own phase.
- **C-08 fully satisfied for the first time**: Coverage ratio (reachable_visited / total_reachable) is a quantified metric tied to the reachability map, not estimated from the trace. This distinction — metric grounded in declared topology vs. inferred from execution — is what prior rounds missed.

**From V-01 (strongest new structural pattern):**
- **RECOVERABLE vs. UNRECOVERABLE defect distinction**: An unrecoverable defect — one where no utterance sequence restores normal flow without session restart or forced escalation — is categorically different from a recoverable one. C-05 (reproduction) captures how a defect is reached; recovery path closure captures what a user experiences if they never escape it. These are orthogonal properties.
- **min_turns as a recovery cost metric**: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` introduces a lightweight cost signal — the minimum conversational friction required to escape a defect state. This is richer than binary found/absent and enables triage by escape cost.
- **Phase 3-R as structural checkpoint**: Placing recovery after defect classification (Phase 2) but before fallback trace (Phase 4) creates a logical ordering: find the defect → determine escapability → trace the escape chain. This matches how a support engineer would actually debug a live agent.

**Criterion gap surfaced by V-04 (negative signal):**
- Severity triage (P0/P1/P2) is useful for prioritization but is incompatible with the typed-verdict discipline enforced by C-13. Free-text BUSINESS_IMPACT justification breaks the schema contract. If severity is added to a future rubric, it must be constrained to an enum (P0 = SESSION_CORRUPTED | INFINITE_LOOP, P1 = DEAD_END, P2 = MISSING_FALLBACK) and kept separate from the business impact narrative.

---

## New Patterns for Rubric v7

| Candidate | Source | Proposed ID |
|-----------|--------|-------------|
| Recovery path closure with RECOVERABLE/UNRECOVERABLE verdict | V-01 | C-19 |
| Reachability map with coverage ratio metric (grounded in declared topology) | V-02 | C-20 |

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["recovery path closure — RECOVERABLE[min_turns, target] vs UNRECOVERABLE[reason] verdict per found defect", "reachability closure — topology-grounded coverage ratio from declared reachability map, not execution estimate"]}
```
