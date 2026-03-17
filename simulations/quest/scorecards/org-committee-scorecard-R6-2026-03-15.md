## org:committee — Round 6 Scoring

**Rubric**: v6 | **Variations**: V-01 through V-05 | **Max composite**: 120

---

### V-01 — Single-axis: CITE: Label-First Notation

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Opens with `Committee: [TYPE: ROB / shiproom / arch-board / other]` |
| C-02 | Participants from `.craft/roles/` | **PASS** | Explicit instruction to load from charter; fallback with disclosure |
| C-03 | Each participant speaks from role lens | **PASS** | "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS all present |
| C-05 | At least one challenge / block | **PASS** | "At least one voice must be CONDITION or BLOCK" enforcement rule |
| C-06 | Agenda item specificity | **PASS** | Speakers respond from role orientation; contribute to prior concerns |
| C-07 | Action items owned and actionable | **PASS** | `[Owner Role] — [specific action] — [deadline]`; vague items explicitly fail |
| C-08 | Dissents include resolution paths | **PASS** | "dissenting role, substance, resolution path (concrete condition + named authority)" |
| C-09 | Non-obvious surprise | **PASS** | `(d) Non-obvious cost` field + GATE enforces non-obviousness before proceeding |
| C-10 | Decision-complete | **PASS** | Verdict + re-entry path with Owner/Trigger |
| C-11 | Challenger-first ordering | **PASS** | Three-tier sort (Tier 1 → 2 → 3) with SORT-CHECK validation |
| C-12 | Switching-cost investigation | **PASS** | `(a)` workflow, `(b)` integration deps, `(c)` habit disruption, `(d)` surprise |
| C-13 | Stance declared before prose | **PASS** | `STANCE:` standalone labeled declaration, prose follows |
| C-14 | Vote tally precedes formal minutes | **PASS** | `TALLY:` required before DECISIONS block |
| C-15 | `STANCE:` label is structural | **PASS** | "standalone labeled declaration — prose follows and must not soften or contradict it" |
| C-16 | Investigation self-check gate | **PASS** | GATE: YES requires "non-obvious because [specific reason]" — explicit verification |
| C-17 | Advocate voices grounded in investigation | **PASS** | `CITE:` required for every Tier 3 voice |
| C-18 | All-approve self-correction | **PASS** | "All-APPROVE means roles are mis-sorted — return to the sort and reassign" |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | `RESPONDS-TO:` required for every Tier 3 voice |
| C-20 | `CITE:` label is structural | **PASS** | Primary axis. "Parenthesized label must be the first token after CITE:" + explicit format rule `CITE: (X) —` |
| C-21 | `RESPONDS-TO:` must name and quote | **PASS** | Quoted slot `"[quote or close paraphrase ... by [Role Name]]"` with failure condition |
| C-22 | Investigation gate enforces self-correction | **PASS** | "If GATE: NO, output `INVESTIGATION-REVISION-1:` and rewrite all four fields" — labeled loop |
| C-23 | Re-entry path names owner and concrete trigger | **PASS** | `Owner:` and `Trigger:` pre-printed fields with explicit C-23 enforcement note |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 15/15 → 30

**V-01 Composite: 120 / 120**

---

### V-02 — Single-axis: RESPONDS-TO: Quote-Slot Template

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Header `Committee: [TYPE]` as first template field |
| C-02 | Participants from `.craft/roles/` | **PASS** | Rule 1: "Load participants from `.craft/roles/`; state fallback explicitly" |
| C-03 | Each participant speaks from role lens | **PASS** | "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS in template |
| C-05 | At least one challenge / block | **PASS** | "At minimum: one participant must declare CONDITION or BLOCK" |
| C-06 | Agenda item specificity | **PASS** | Template structure channels responses through role orientation |
| C-07 | Action items owned and actionable | **PASS** | Format row + "every item has a named owner, a specific deliverable, and a deadline" |
| C-08 | Dissents include resolution paths | **PASS** | "[concrete condition] — [authority role] confirms when [condition met]" |
| C-09 | Non-obvious surprise | **PASS** | `(d)` field + GATE-1 self-verification before proceeding |
| C-10 | Decision-complete | **PASS** | Verdict + Owner + Trigger fields |
| C-11 | Challenger-first ordering | **PASS** | Three-tier sort block with SORT-CHECK mechanism |
| C-12 | Switching-cost investigation | **PASS** | `(a)-(d)` investigation fields |
| C-13 | Stance declared before prose | **PASS** | STANCE: standalone labeled line, rule 4 |
| C-14 | Vote tally precedes formal minutes | **PASS** | TALLY: section before DECISIONS |
| C-15 | `STANCE:` label is structural | **PASS** | Rule 4: "standalone labeled line, not embedded in prose" |
| C-16 | Investigation self-check gate | **PASS** | GATE-N with YES/NO + non-obviousness verification |
| C-17 | Advocate voices grounded in investigation | **PASS** | CITE: required; rule 5 |
| C-18 | All-approve self-correction | **PASS** | SORT-CHECK: "Tier 1 and Tier 2 both empty? YES — mis-sorted; reassigning" |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | RESPONDS-TO: required; rule 6 |
| C-20 | `CITE:` label is structural | **PASS** | Rule 5: "parenthesized letter must be the first element after `CITE:`" |
| C-21 | `RESPONDS-TO:` must name and quote | **PASS** | Primary axis. Pre-printed `"[...]"` slot enforces attribution as a transcription task — rule 6 explicitly disqualifies generic acknowledgment |
| C-22 | Investigation gate enforces self-correction | **PASS** | Rule 2: INVESTIGATION-ATTEMPT-N+1 loop; labeled rewrite block required before proceeding |
| C-23 | Re-entry path names owner and concrete trigger | **PASS** | Owner: / Trigger: pre-printed fields; rule 7 |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 15/15 → 30

**V-02 Composite: 120 / 120**

---

### V-03 — Single-axis: Numbered Investigation Attempt Loop

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Phase 0 opens with Committee declaration |
| C-02 | Participants from `.craft/roles/` | **PASS** | Phase 0: explicit load + fallback disclosure |
| C-03 | Each participant speaks from role lens | **PASS** | Phase 3 voice format: "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | Phase 5 has DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| C-05 | At least one challenge / block | **PASS** | "At least one participant must declare CONDITION or BLOCK" |
| C-06 | Agenda item specificity | **PASS** | Phase-labeled structure routes contributions through role orientation |
| C-07 | Action items owned and actionable | **PASS** | Format + "every item: named owner, specific deliverable, deadline" |
| C-08 | Dissents include resolution paths | **PASS** | "dissenting role, substance, resolution path (concrete condition + named authority)" |
| C-09 | Non-obvious surprise | **PASS** | `(d)` + GATE-1 gate |
| C-10 | Decision-complete | **PASS** | Verdict + Owner + Trigger |
| C-11 | Challenger-first ordering | **PASS** | Three-tier sort + SORT-CHECK in Phase 2 |
| C-12 | Switching-cost investigation | **PASS** | `(a)-(d)` in Phase 1 |
| C-13 | Stance declared before prose | **PASS** | "STANCE: is a standalone declaration on its own line" |
| C-14 | Vote tally precedes formal minutes | **PASS** | Phase 4 TALLY: before Phase 5 |
| C-15 | `STANCE:` label is structural | **PASS** | "Standalone declaration on its own line — prose follows and must not soften or contradict it" |
| C-16 | Investigation self-check gate | **PASS** | GATE-1 field with YES/NO non-obviousness test |
| C-17 | Advocate voices grounded in investigation | **PASS** | CITE: required for Tier 3; explicit in Phase 3 enforcement |
| C-18 | All-approve self-correction | **PASS** | SORT-CHECK in Phase 2: "Tier 1 and Tier 2 both empty?" with reassignment |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | RESPONDS-TO: required for Tier 3 |
| C-20 | `CITE:` label is structural | **PASS** | "Parenthesized label `(a)/(b)/(c)/(d)` must be the first element after `CITE:`. A CITE: that opens with prose before the label fails C-20." |
| C-21 | `RESPONDS-TO:` must name and quote | **PASS** | Quoted attribution format: `"[Role Name]'s concern that [concern text]"` — "Generic acknowledgment fails C-21" |
| C-22 | Investigation gate enforces self-correction | **PASS** | Primary axis. Sequential INVESTIGATION-ATTEMPT-N / GATE-N labels make iteration count visible; "GATE-N: NO followed by no labeled rewrite attempt fails C-22" |
| C-23 | Re-entry path names owner and concrete trigger | **PASS** | Owner: + Trigger: with C-23 enforcement note; "both parts must be present" |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 15/15 → 30

**V-03 Composite: 120 / 120**

---

### V-04 — Combined: Inertia Framing + C-23 Re-Entry Tied to INERTIA-FINDING Tags

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Step 1 opens with Committee: declaration |
| C-02 | Participants from `.craft/roles/` | **PASS** | Step 1: load from charter + inertia-advocate.md fallback |
| C-03 | Each participant speaks from role lens | **PASS** | "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| C-05 | At least one challenge / block | **PASS** | Inertia-Advocate is mandatory first speaker with CONDITION/BLOCK stance |
| C-06 | Agenda item specificity | **PASS** | INERTIA-FINDING tags ground specificity; subsequent voices must engage named tags |
| C-07 | Action items owned and actionable | **PASS** | `[Owner Role] — [specific action] — [deadline]` + vague items fail |
| C-08 | Dissents include resolution paths | **PASS** | Inertia-advocate dissent must reference INERTIA-FINDING tags; named authority |
| C-09 | Non-obvious surprise | **PASS** | `(d)` + GATE with C-22 loop |
| C-10 | Decision-complete | **PASS** | Verdict + Owner + Resolves + Trigger |
| C-11 | Challenger-first ordering | **PARTIAL** | Inertia-Advocate first + Skeptics before Advocates preserves ordering principle, but does not use explicit three-tier (CHALLENGERS / CONDITIONALS / ADVOCATES) separation — CONDITIONAL tier is subsumed into Skeptics without distinct naming, creating ambiguity for ambiguous-stance voices |
| C-12 | Switching-cost investigation | **PASS** | `(a)-(d)` investigation + inertia-advocate grounds critique in named findings |
| C-13 | Stance declared before prose | **PASS** | `STANCE:` standalone labeled declaration |
| C-14 | Vote tally precedes formal minutes | **PASS** | TALLY: in Step 6 before Step 7 |
| C-15 | `STANCE:` label is structural | **PASS** | "standalone labeled declaration — prose follows and must not soften or contradict it" |
| C-16 | Investigation self-check gate | **PASS** | GATE field with YES/NO |
| C-17 | Advocate voices grounded in investigation | **PASS** | CITE: required for advocates; INERTIA-FINDING tags trace back to Step 2 |
| C-18 | All-approve self-correction | **PASS** | REMAINING-SORT-CHECK: "All remaining participants are advocates? YES — mis-sorted; reassigning to Skeptics" |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | RESPONDS-TO: with INERTIA-FINDING tag name required |
| C-20 | `CITE:` label is structural | **PASS** | "First element after `CITE:` must be the label — `(a)`, `(b)`, `(c)`, `(d)`, `INERTIA-FINDING-A`, or `INERTIA-FINDING-B`. No prose before the label." |
| C-21 | `RESPONDS-TO:` must name and quote | **PASS** | Naming INERTIA-FINDING tag + paraphrasing its content; "generic acknowledgment fails — tag name and paraphrase must appear" |
| C-22 | Investigation gate enforces self-correction | **PASS** | C-22 loop: "If GATE is NO, output `INVESTIGATION-REVISION-1:` and rewrite. Repeat until GATE: YES." |
| C-23 | Re-entry path names owner and concrete trigger | **PASS** | Primary axis (combined with inertia). Three-part re-entry: `Owner:` + `Resolves:` (named tag) + `Trigger:` — exceeds C-23 minimum |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 14 PASS + 1 PARTIAL = 14×2 + 1×1 = 29

**V-04 Composite: 119 / 120**

---

### V-05 — Golden Synthesis: All Four New Criteria as Pre-Printed Template Fields

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type declared | **PASS** | Header field `Committee: [TYPE]` as first pre-printed slot |
| C-02 | Participants from `.craft/roles/` | **PASS** | Rule 1: load from charter; explicit fallback |
| C-03 | Each participant speaks from role lens | **PASS** | "2-4 sentences from documented role orientation" |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS all in template |
| C-05 | At least one challenge / block | **PASS** | "At minimum: one participant must declare CONDITION or BLOCK" |
| C-06 | Agenda item specificity | **PASS** | Template structure channels role-specific contributions throughout |
| C-07 | Action items owned and actionable | **PASS** | Two pre-printed rows + rule: "every item has a named owner, a specific deliverable, and a deadline" |
| C-08 | Dissents include resolution paths | **PASS** | Resolution path: "[concrete condition] — [authority role] confirms when [condition met]" |
| C-09 | Non-obvious surprise | **PASS** | `(d) Non-obvious cost` + GATE-1 gate; pre-printed (d) makes the surprise a required slot |
| C-10 | Decision-complete | **PASS** | Verdict + Owner + Trigger as pre-printed fields |
| C-11 | Challenger-first ordering | **PASS** | Three-tier sort block + SORT-CHECK with explicit reassignment path |
| C-12 | Switching-cost investigation | **PASS** | `(a)-(d)` pre-printed fields |
| C-13 | Stance declared before prose | **PASS** | `STANCE:` pre-printed line; rule 4 |
| C-14 | Vote tally precedes formal minutes | **PASS** | TALLY: section between PARTICIPANT VOICES and DECISIONS |
| C-15 | `STANCE:` label is structural | **PASS** | Rule 4: "standalone labeled line, not embedded in prose" |
| C-16 | Investigation self-check gate | **PASS** | GATE-1 pre-printed field with NO → labeled loop instruction |
| C-17 | Advocate voices grounded in investigation | **PASS** | CITE: pre-printed field required for Tier 3 |
| C-18 | All-approve self-correction | **PASS** | SORT-CHECK: "Tier 1 and Tier 2 both empty?" with re-output instruction |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | RESPONDS-TO: pre-printed field with attribution slot |
| C-20 | `CITE:` label is structural | **PASS** | Rule 5: "`([a/b/c/d])` must be the first element after `CITE:`, followed by ` — `. A CITE: field that begins with prose before the label fails C-20." Pre-printed `([a/b/c/d]) —` prefix enforces this as transcription |
| C-21 | `RESPONDS-TO:` must name and quote | **PASS** | Pre-printed `"[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']"` — quotation marks pre-printed; rule 6: "A generic acknowledgment does not fill the attribution slot and fails C-21. Do not remove the quotation marks." |
| C-22 | Investigation gate enforces self-correction | **PASS** | Rule 2: INVESTIGATION-ATTEMPT-N+1 loop explicitly visible; "a claimed revision that produces no new labeled attempt block fails C-22" |
| C-23 | Re-entry path names owner and concrete trigger | **PASS** | `Owner:` and `Trigger:` both pre-printed as distinct required fields; rule 7 |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 15/15 → 30

**V-05 Composite: 120 / 120**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 60 | 30 | 30 (15/15) | **120** |
| V-02 | 60 | 30 | 30 (15/15) | **120** |
| V-03 | 60 | 30 | 30 (15/15) | **120** |
| V-04 | 60 | 30 | 29 (14 + C-11 partial) | **119** |
| V-05 | 60 | 30 | 30 (15/15) | **120** |

**Ranking**: V-01 = V-02 = V-03 = V-05 (120) > V-04 (119)

---

## Excellence Signals

**From V-05 (golden synthesis — most structurally complete):**

1. **Pre-printed template slots as compliance transcription.** Every enforcement criterion is a pre-printed field the model fills — not a prose instruction the model may de-prioritize. `CITE: ([a/b/c/d]) —` pre-printed with the parenthesized label notation already in place means the model transcribes the label, not generates it. `RESPONDS-TO: "[...]"` pre-printed quotation marks mean the model cannot deliver an unquoted string without leaving visible template residue.

2. **Quotation marks as unfillable gap signal.** The `"[...]"` template notation creates an invariant: an unfilled slot has visibly unresolved quotation marks. This is stronger than rule-based enforcement because the failure mode has a distinct visual signature distinguishable from compliant output.

3. **Duplicate enforcement: rule in template + rule in footnotes.** V-05 places the enforcement rule *inside* each pre-printed field block and also restates it in the numbered enforcement rules at the end. The rule appears where the model is writing (local) and in the authoritative summary (global) — reducing the probability that attention drift causes a miss.

**From V-04 (inertia framing — strongest C-23 traceability):**

4. **Named finding tags create a traceable committee record.** `INERTIA-FINDING-A` and `INERTIA-FINDING-B` pre-label the blocking concerns before the rest of the simulation runs. Every subsequent voice, the re-entry path, and the dissenting opinions can reference these tags by name — producing a traceable chain from investigation → voice → minutes that is absent when concerns live only in prose.

**From V-03 (phase labels — strongest C-22 observability):**

5. **Phase headers as mandatory output checkpoints.** Labeling sections Phase 0–5 makes section-skipping visually detectable. A model that jumps from Phase 1 to Phase 3 has left a visible gap where Phase 2 header should appear. This is a navigation-level enforcement mechanism layered on top of field-level enforcement.

---

## New Patterns (not yet formalized)

**Pattern R6-A: Three-part re-entry path (Owner + Resolves + Trigger).**
V-04 introduces a `Resolves:` field between Owner and Trigger, naming which specific finding or named concern is being addressed. C-23 requires two parts (Owner + Trigger). V-04 shows that a third field — the named blocking item being resolved — makes the path fully traceable to the committee record, not just internally consistent. A potential C-24: *"Re-entry path names the specific finding or condition being resolved by the owner, creating a three-way chain: who → what → when."*

**Pattern R6-B: Pre-printed quotation marks as slot integrity signal.**
The `"[...]"` notation in V-02 and V-05 creates a class of failure that is distinguishable from a correctly filled field by visual inspection alone. A non-quoted or unattributed `RESPONDS-TO:` string leaves the literal characters `"[` or `']"` in the output — a mechanical failure signal. No prior criterion formalizes the idea that the template's unresolved placeholder characters are themselves a compliance indicator.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Three-part re-entry path: Owner + Resolves (named finding tag) + Trigger — C-23 requires two parts; V-04's Resolves field adds the blocking finding reference, making the path traceable to the committee record", "Pre-printed quotation marks as slot integrity signal: RESPONDS-TO: \"[...]\" leaves literal unresolved characters when improperly filled, creating a visually detectable failure mode distinct from compliant output"]}
```
