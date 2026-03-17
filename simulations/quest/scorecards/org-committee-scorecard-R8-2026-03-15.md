# org:committee — Round 8 Scoring

**Rubric**: v8 | **Variations presented**: V-01, V-02 | **Composite max**: 130

> **Note**: The prompt instructs scoring V-01 through V-05, but only V-01 and V-02 are provided in this round. Scoring reflects what is present.

---

## V-01 — Named Labels Integrated into Phase Architecture (C-27 + C-26)

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Phase 0 template: `Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]` |
| C-02 | Participants from `.craft/roles/` | **PASS** | Phase 0 reads charter explicitly; fallback to Signal defaults with mandatory disclosure |
| C-03 | Role-lens speech | **PASS** | Phase 3 requires "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | Phase 5 has explicit DECISIONS / ACTION ITEMS / DISSENTING OPINIONS headers |
| C-05 | At least one challenge/block | **PASS** | Phase 3: "An all-APPROVE Phase 3 means Phase 2 sort is invalid — reopen Phase 2, re-sort, re-evaluate SORT-CHECK" |

**Essential: 5/5 → 60/60**

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Agenda item specificity | **PASS** | RESPONDS-TO: requires named concern; CITE: ties voice to specific Phase 1 finding |
| C-07 | Owned/actionable action items | **PASS** | Phase 5: `[Owner Role] — [specific action] — [deadline]`; "'Investigate further' fails" |
| C-08 | Dissents with resolution paths | **PASS** | Phase 5 DISSENTING OPINIONS: "dissenting role, substance of objection, resolution path (named owner + concrete trigger)" |

**Recommended: 3/3 → 30/30**

### Aspirational (40 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Non-obvious surprise | **PASS** | Enforced via C-16 gate: GATE-1 Test requires non-obvious finding before Phase 1 closes |
| C-10 | Decision-complete outcome | **PASS** | Phase 5 DECISIONS: Owner + Trigger both required fields; "path specifying only one fails" |
| C-11 | Challenger-first ordering | **PASS** | Phase 2: Tier 1 CHALLENGERS → Tier 2 CONDITIONALS → Tier 3 ADVOCATES with tie-break rule |
| C-12 | Switching-cost investigation precedes | **PASS** | Phase 1 runs before any participant speaks; INERTIA-FINDING-A/B/C/D required |
| C-13 | Stance declared before prose | **PASS** | Phase 3: "STANCE: is a standalone labeled declaration on its own line" |
| C-14 | Vote tally precedes minutes | **PASS** | Phase 4 TALLY block between all voices and Phase 5 minutes |
| C-15 | `STANCE:` structural label | **PASS** | Phase 3: "`STANCE:` is a discrete labeled declaration. Prose follows on the next line; it may not revise the declared stance." |
| C-16 | Investigation self-check gate | **PASS** | Phase 1: `GATE-1: Test: / Answer:` with "Phase 1 exit condition: GATE-N Answer must be YES" |
| C-17 | Advocate voices cite investigation | **PASS** | Phase 3 Tier 3: `CITE: INERTIA-FINDING-[A/B/C/D]` required in every Tier 3 block |
| C-18 | All-approve self-correction | **PASS** | Phase 3: "An all-APPROVE Phase 3 means Phase 2 sort is invalid — reopen Phase 2" |
| C-19 | Tier 3 responds to Tier 1/2 concern | **PASS** | Phase 3 Tier 3: `RESPONDS-TO:` required in every Tier 3 block |
| C-20 | `CITE:` structural label | **PASS** | Phase 3: "the `INERTIA-FINDING-[X]` label must be the first element after `CITE:`. Any prose before the label fails." |
| C-21 | `RESPONDS-TO:` names and quotes | **PASS** | Phase 3: "must quote or paraphrase a specific named concern by role name or finding label. Generic acknowledgment fails." |
| C-22 | Investigation gate enforces rewrite | **PASS** | Phase 1: "a claimed revision with no new labeled block does not satisfy C-22"; loop runs until YES |
| C-23 | Re-entry path names owner + trigger | **PASS** | Phase 5: Owner and Trigger both required; "Both Owner and Trigger are required fields (C-23). A path specifying only one fails." |
| C-24 | Rewrite attempts carry sequential labels | **PASS** | Phase 1: `INVESTIGATION-ATTEMPT-1:` initial label; `INVESTIGATION-ATTEMPT-N:` / `GATE-N:` for subsequent loops |
| C-25 | Tier sort validation as named gate | **PASS** | Phase 2: `SORT-CHECK: Test: / Result:` explicit labeled block |
| C-26 | Explicitly labeled sequential phases | **PASS** | Six numbered Phase 0–5 headers, each committing before the next begins |
| C-27 | Switching-cost findings carry named labels | **PASS** | Phase 1 template places `INERTIA-FINDING-A/B/C/D` directly on findings; CITE: in Phase 3 references these labels by name |
| C-28 | Full skeleton pre-declared before content | **PARTIAL** | Phase templates are introduced per-phase as execution proceeds; labels emerge alongside content generation rather than from a single upfront pre-declared skeleton. All labels appear in the correct positions, but none are pre-committed as empty slots before Phase 0 content begins. |

**Aspirational: 19 × 2 + 1 = 39/40**

### V-01 Composite: 60 + 30 + 39 = **129/130**

---

## V-02 — Table-Based Investigation with Named Labels as Structural Column (C-27)

> **Structural note**: V-02 as written ends after the SWITCHING-COST INVESTIGATION section ("Do not proceed to the tier sort until GATE-N Answer is YES"). The tier sort, participant voices (Phase 3), tally (Phase 4), and minutes (Phase 5) are absent. Scoring reflects the prompt as presented; missing sections fail their dependent criteria.

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | DECLARE section: `Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]` |
| C-02 | Participants from `.craft/roles/` | **PASS** | "Read `.craft/roles/`" with explicit fallback disclosure |
| C-03 | Role-lens speech | **FAIL** | No participant voice section present; no instructions for role-oriented contributions |
| C-04 | All three required sections | **FAIL** | No DECISIONS, ACTION ITEMS, or DISSENTING OPINIONS sections |
| C-05 | At least one challenge/block | **FAIL** | No mechanism to require or enforce challenge/block in missing voice section |

**Essential: 2/5 → 24/60**

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Agenda item specificity | **FAIL** | No voice section present |
| C-07 | Owned/actionable action items | **FAIL** | No action items section |
| C-08 | Dissents with resolution paths | **FAIL** | No dissenting opinions section |

**Recommended: 0/3 → 0/30**

### Aspirational (40 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Non-obvious surprise | **PASS** | GATE-1 Test explicitly tests for non-obvious finding (2) |
| C-10 | Decision-complete outcome | **FAIL** | No minutes section; no re-entry path |
| C-11 | Challenger-first ordering | **FAIL** | No tier sort section |
| C-12 | Switching-cost investigation precedes | **PASS** | Investigation section present before any participant speaks (2) |
| C-13 | Stance declared before prose | **FAIL** | No voice section |
| C-14 | Vote tally precedes minutes | **FAIL** | No tally section |
| C-15 | `STANCE:` structural label | **FAIL** | No voice section |
| C-16 | Investigation self-check gate | **PASS** | `GATE-1: Test: / Answer:` present; loop condition stated (2) |
| C-17 | Advocate voices cite investigation | **FAIL** | No voice section |
| C-18 | All-approve self-correction | **FAIL** | No sort section |
| C-19 | Tier 3 responds to Tier 1/2 concern | **FAIL** | No voice section |
| C-20 | `CITE:` structural label | **FAIL** | No voice section |
| C-21 | `RESPONDS-TO:` names and quotes | **FAIL** | No voice section |
| C-22 | Gate enforces rewrite | **PASS** | Sequential `INVESTIGATION-ATTEMPT-N` / `GATE-N` loop present; "a prose summary without a new table header fails" (2) |
| C-23 | Re-entry path names owner + trigger | **FAIL** | No minutes section |
| C-24 | Sequential labels on rewrites | **PASS** | `### INVESTIGATION-ATTEMPT-1` and `GATE-1:` with sequential numbering stated (2) |
| C-25 | Tier sort validation as named gate | **FAIL** | No tier sort section |
| C-26 | Explicitly labeled sequential phases | **FAIL** | Flat headers (DECLARE / LOAD PARTICIPANTS / SWITCHING-COST INVESTIGATION) without numbered phase structure |
| C-27 | Switching-cost findings carry named labels | **PASS** | Table Label column enforces `INERTIA-FINDING-A/B/C/D` tags structurally — a row cannot exist without its label (2) |
| C-28 | Full skeleton pre-declared before content | **FAIL** | No pre-declared skeleton; sequential generation; missing most structural slots |

**Aspirational: 6 × 2 = 12/40**

### V-02 Composite: 24 + 0 + 12 = **36/130**

---

## Rankings

| Rank | Variation | Composite | Essential | Recommended | Aspirational |
|------|-----------|-----------|-----------|-------------|--------------|
| 1 | V-01 | **129/130** | 60/60 | 30/30 | 39/40 |
| 2 | V-02 | **36/130** | 24/60 | 0/30 | 12/40 |

---

## Excellence Signals from V-01

**Signal 1 — The named-label citation chain is closed end-to-end.**
V-01 places `INERTIA-FINDING-A/B/C/D` labels directly on Phase 1 findings, then requires `CITE: INERTIA-FINDING-[X]` as the first element in every Tier 3 CITE: field, then requires `RESPONDS-TO:` to quote or paraphrase a specific named concern by label. The result is a traceable path: Phase 1 label → Phase 3 CITE: → Phase 3 RESPONDS-TO:. No downstream citation in the simulation can reference anonymous content; every citation traces to a specific named entry. This is the complete structural realization of C-27 + C-20 + C-21 working together.

**Signal 2 — Cross-phase correction loops are explicitly declared.**
V-01 specifies that a failing Phase 3 (all-APPROVE) reopens Phase 2 (resort) and a failing Phase 1 gate loops within Phase 1. Both correction mechanisms cross phase boundaries and are explicitly stated as rules rather than implied. A simulation following V-01 cannot reach the wrong state and silently proceed; it must detect the structural failure and re-enter the correct phase.

**Signal 3 — V-02's table-column enforcement is architecturally stronger than V-01's prose-label enforcement for C-27, but the variation is incomplete.**
The table Label column makes C-27 compliance structural: a row without a label cannot exist. V-01's prose template (`INERTIA-FINDING-A: [finding text]`) is behaviorally enforced — the model could omit a label under generation pressure. V-02's architecture is superior for C-27 specifically, but the variation fails to carry the mechanism through the rest of the simulation. The insight should be incorporated into a future complete variation.

---

```json
{"top_score": 129, "all_essential_pass": true, "new_patterns": ["Named INERTIA-FINDING labels placed directly on Phase 1 investigation entries create a closed end-to-end citation chain: Phase 1 label is the primary citation target for Phase 3 CITE:, which anchors RESPONDS-TO: quotation — no downstream citation can reference anonymous content", "Table-column enforcement (Label as first column) provides a structurally guaranteed compliance mechanism for named investigation labels: a table row cannot exist without its Label column, making omission architecturally impossible rather than behaviorally enforced"]}
```
