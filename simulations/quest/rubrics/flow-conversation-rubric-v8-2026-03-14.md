```markdown
# Rubric — flow-conversation — v8 (2026-03-14)

> **What changed in v8**: Added C-21 (severity co-residency audit), C-22
> (transition completeness map), C-23 (defect entanglement analysis), and C-24
> (topic-indexed trace aggregation), extracted from Round 8 excellence signals
> in V-01, V-02, V-03, and V-04 respectively.
>
> C-21 requires an independent Phase 6-B Severity Co-Residency Audit that
> verifies SEVERITY_CLASS and INVARIANT_CITE coexist in every FOUND defect row.
> The audit is a structural gate, not a narrative note: neither column may
> displace the other. This criterion was motivated by V-04's Round 7 failure
> (severity triage corrupted typed-verdict discipline), and V-01 demonstrates
> correct rehabilitation: SEVERITY_CLASS_MAP in Phase 0-D-6 anchors all five
> defect classes; EXEMPT locks CONFIRMED_ABSENT rows out of the co-residency
> check.
>
> C-22 requires a Phase 0-D-6 TRANSITION_MAP declaring all edges in the
> conversation graph (`TRANS-NN`: source, target, condition, REQUIRED|OPTIONAL).
> Phase 5 must report `transitions_exercised / total_declared` as a second
> coverage signal orthogonal to the topic-coverage ratio in C-08/C-19. An
> unexercised REQUIRED transition is an orphaned-edge defect — distinct from an
> orphaned topic (C-19) but equally invisible without a declared edge map.
> Unexercised REQUIRED transitions carry UNRECOVERABLE[missing edge] recovery
> verdicts under C-20. V-02 was the first variation to surface this class of
> structural gap; its dual-ratio implementation (topic + edge) exceeds the
> minimum criterion.
>
> C-23 requires a Phase 3-E ENTANGLEMENT_MAP where every FOUND defect row
> carries an ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] |
> MASKED_BY[DEFECT_CLASS]. MASKED_BY defects extend C-20 recovery verdicts to
> conditional form: RECOVERABLE[min_turns, target_state,
> requires_fix=DEFECT_CLASS]. A Phase 6-C independent entanglement audit
> confirms the map is consistent with turn-level evidence. This is the deepest
> structural innovation of Round 8: prior rounds classified defects flatly;
> entanglement makes the causal graph explicit, changes remediation priority
> order, and prevents spurious RECOVERABLE verdicts on defects that are in fact
> masked by an upstream cause.
>
> C-24 requires a Phase 1-T topic aggregate that is strictly additive to the
> turn-level trace — not replacing it. Each row in the aggregate shows: turns
> visited, session variables set/read (lifecycle summary), defect citations with
> TOPIC_ID provenance, adversarial injection count, and a conformance rollup.
> Phase 6-B audits consistency between per-topic conformance rollup (Phase 1-T)
> and turn-level verdicts (C-11). C-08's coverage ratio becomes per-topic
> visualizable: which topics contribute coverage versus dead weight is
> immediately legible from the aggregate.
>
> Aspirational denominator updated from 13 to 26.
>
> *(prior change history preserved unchanged)*

---

## Purpose

Evaluate a simulated Copilot Studio conversation-flow trace for dialog coverage,
defect classification completeness, session state fidelity, and domain vocabulary
discipline.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Dialog path traced as turns** | coverage | essential | Output walks the conversation turn-by-turn. Each turn shows: user utterance, topic matched, nodes executed, agent response, and transition target. No turns may be skipped or collapsed into a summary. |
| C-02 | **All four defect classes addressed** | correctness | essential | Output explicitly addresses all four defect classes: dead ends, infinite loops, intent collisions, missing fallbacks. Each class is either found (with example) or confirmed absent. CONFIRMED ABSENT requires an explicit statement of scope. |
| C-03 | **Session state tracked** | correctness | essential | Output maintains and displays session state across turns (e.g., active topic, slot values, prior intent history). State must visibly change or be held across at least two transitions. |
| C-04 | **Copilot Studio framing** | behavior | essential | Analysis uses Copilot Studio vocabulary: topics, trigger phrases, conditions, fallback topics, escalation, session variables. Generic chatbot terms without grounding are not sufficient. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Defect reproduction steps** | depth | recommended | For each defect found, output provides a minimal reproduction: the exact utterance sequence that triggers the defect and the observable failure mode. |
| C-06 | **Fallback chain coverage** | coverage | recommended | Output traces at least one fallback path to completion -- what happens when no topic matches, including escalation or graceful exit. Shows the full chain, not just the first fallback node. |
| C-07 | **Intent collision disambiguation** | depth | recommended | If intent collisions are found, output proposes a disambiguation strategy (e.g., entity enrichment, condition ordering, trigger phrase refactor) with rationale. |

---

## Aspirational Criteria (26 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Graph coverage metric** | depth | aspirational | Output reports a coverage ratio: topics visited / total topics in graph, or intents exercised / total trigger phrases. Gives a quantified signal, not just narrative. **When C-19 is also satisfied, the denominator must derive from the declared REACHABILITY_MAP (`reachable_visited / total_reachable`), not the count of all defined topics.** |
| C-09 | **Adversarial turn injection** | behavior | aspirational | Output includes at least one adversarial scenario -- unexpected user utterance mid-flow, topic switch during slot filling, or session timeout -- and shows how the agent responds. |
| C-10 | **Prohibited vocabulary gate** | behavior | aspirational | Output pre-maps the CS topology term set used in the trace AND explicitly lists prohibited generic terms with a verification that none appear in the output. Demonstrates active vocabulary enforcement, not passive CS term usage. |
| C-11 | **Turn-level conformance verdict** | correctness | aspirational | Each turn carries an explicit CONFORMS / DEVIATES verdict against the expected topology spec, separate from the defect classification section. |
| C-19 | **Reachability map pre-computation** | depth | aspirational | Phase 0-D declares a REACHABILITY_MAP: entry topic, all topics reachable by transitivity, and orphaned topics (defined but unreachable). Orphaned topics are classified as ORPHAN defects — a fifth structural defect class at graph level, required regardless of whether orphaned topics appear in any trace path. When C-19 is satisfied, C-08's denominator must derive from this map. |
| C-20 | **Recovery path verdict per defect** | correctness | aspirational | Every FOUND defect row carries a mandatory RECOVERY field: RECOVERABLE[min_turns, target_state] or UNRECOVERABLE[reason]. A FOUND row without a RECOVERY field is a structural failure. CONFIRMED_ABSENT rows are exempt. Extends C-05 from trigger path to escape path. |
| C-21 | **Severity co-residency audit** | correctness | aspirational | An independent Phase 6-B audit confirms that SEVERITY_CLASS and INVARIANT_CITE coexist in every FOUND defect row. The audit is a structural gate: a FOUND row may not carry SEVERITY_CLASS without INVARIANT_CITE, nor INVARIANT_CITE without SEVERITY_CLASS. CONFIRMED_ABSENT rows are exempt. |
| C-22 | **Transition completeness map** | coverage | aspirational | Phase 0-D-6 declares a TRANSITION_MAP for all edges in the conversation graph (`TRANS-NN`: source, target, condition, REQUIRED\|OPTIONAL). Phase 5 reports `transitions_exercised / total_declared`. An unexercised REQUIRED transition is an orphaned-edge defect, distinct from an orphaned topic (C-19); it carries an UNRECOVERABLE[missing edge] recovery verdict under C-20. When both C-19 and C-22 are satisfied, C-08 may report a dual ratio: topic coverage + edge coverage as orthogonal signals. |
| C-23 | **Defect entanglement analysis** | depth | aspirational | Phase 3-E provides an ENTANGLEMENT_MAP. Every FOUND defect row carries ENTANGLEMENT_VERDICT: ISOLATED \| ENABLES[DEFECT_CLASS] \| MASKED_BY[DEFECT_CLASS]. Recovery verdicts for MASKED_BY defects are conditional: RECOVERABLE[min_turns, target_state, requires_fix=DEFECT_CLASS]. A Phase 6-C independent entanglement audit confirms the map is consistent with turn-level evidence. CONFIRMED_ABSENT rows are exempt. |
| C-24 | **Topic-indexed trace aggregation** | coverage | aspirational | Phase 1-T provides a per-topic aggregate strictly additive to the turn-level trace. Each row shows: turns visited, session variables set/read, defect citations with TOPIC_ID provenance, adversarial injection count, and a conformance rollup. Phase 6-B audits consistency between the per-topic conformance rollup and turn-level C-11 verdicts. The aggregate makes C-08's coverage ratio per-topic visualizable. |

---

## Point Summary

| Bucket | Criteria | Points |
|--------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09, C-10, C-11 | 13 (3/3/3/4) |
| Aspirational | C-19, C-20, C-21, C-22, C-23, C-24 | 13 (3/2/3/3/4/3) |
| **Max** | | **116** |

*C-19 and C-20 were promoted in v7. C-21 through C-24 promoted in v8. Point
weights reflect structural complexity: C-23 (entanglement) carries 4 points as
the deepest causal innovation; C-20 carries 2 points as an extension of C-05
rather than a standalone structural layer.*
```
