## org:committee — Round 10 Scoring (Rubric v10, C-01 through C-30)

**Composite max**: 134 pts (60 essential + 30 recommended + 44 aspirational)

---

## V-01 — Single-axis: Phrasing Register (Imperative Fill Rules in Skeleton)

### Essential (60/60)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | PRINT: Committee Type declared before any content; VALIDATE enforces it |
| C-02 | PASS | LOAD: from `.roles/`; ENFORCE: fallback to Signal defaults with disclosure |
| C-03 | PASS | WRITE: from charter-documented role orientation per participant |
| C-04 | PASS | DECISIONS / ACTION ITEMS / DISSENTING OPINIONS all present in Phase 5 |
| C-05 | PASS | VALIDATE: at least one CONDITION or BLOCK; all-APPROVE triggers Phase 2 re-sort |

### Recommended (30/30)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-06 | PASS | Agenda Item loaded in Phase 0, threaded through Phase 3 voices per charter orientation |
| C-07 | PASS | PRINT: `[Owner Role] — [specific action] — [deadline]`; REQUIRE: all three parts; "investigate" alone fails |
| C-08 | PASS | CONFIRM: resolution path names concrete trigger + named authority |

### Aspirational (44/44)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-09 | PASS | INERTIA-FINDING-D: REQUIRE specific enough author would say "I missed that" |
| C-10 | PASS | Verdict + re-entry path with Owner and Trigger in Phase 5 |
| C-11 | PASS | ASSIGN: Tier 1 → 2 → 3; ENFORCE: Tier 1 speaks before all others |
| C-12 | PASS | Phase 1 investigation before Phase 3 voices; INERTIA-FINDING-D targets non-obvious cost |
| C-13 | PASS | PRINT: `STANCE:` as standalone labeled line before prose |
| C-14 | PASS | TALLY printed after last Phase 3 voice, before Phase 5 |
| C-15 | PASS | STANCE: standalone labeled declaration; prose must not soften or contradict |
| C-16 | PASS | GATE-1 with explicit Question/Answer/Basis; non-obvious threshold enforced |
| C-17 | PASS | REQUIRE: Tier 3 — fill CITE: before endorsement prose; named label required |
| C-18 | PASS | VALIDATE: all-APPROVE → REOPEN Phase 2, revise tier assignments, RE-RUN SORT-CHECK |
| C-19 | PASS | RESPONDS-TO: must name participant or concern specifically; acceptable/fail examples given |
| C-20 | PASS | ENFORCE: named label is first element after `CITE:`; prose before label fails |
| C-21 | PASS | REQUIRE: quoted string names specific finding; `FAILS: generic acknowledgment` examples |
| C-22 | PASS | IF GATE-N NO → INCREMENT N; REQUIRE: each rewrite produces new labeled block |
| C-23 | PASS | VALIDATE: both Owner and Trigger present; missing either field is incomplete |
| C-24 | PASS | REQUIRE: sequential label increments by 1; label must appear in output |
| C-25 | PASS | SORT-CHECK with `Test:` and `Result:` fields as discrete labeled gate in skeleton |
| C-26 | PASS | PHASE 0 through PHASE 5 labeled sequentially; skeleton pre-declares all phase headers |
| C-27 | PASS | VALIDATE: INERTIA-FINDING-* as first token; `(a)` without label name fails |
| C-28 | **PASS** | STEP 1 prints full skeleton — all phase headers, INVESTIGATION-ATTEMPT-1/2 blocks, SORT-CHECK, STANCE:, CITE:, RESPONDS-TO:, TALLY, DECISIONS/ACTION ITEMS/DISSENTING OPINIONS — before any content |
| C-29 | PASS | ENFORCE: gate loop runs within Phase 1; Phase 2 is pre-declared in skeleton — present unconditionally |
| C-30 | **PASS** | Every STEP 2 fill rule is verb-first imperative: LOAD:, ENFORCE:, PRINT:, VALIDATE:, WRITE:, REQUIRE:, CONFIRM:, LABEL:, ASSIGN:, COUNT: throughout; no descriptive prose in instruction role |

**V-01 Score: 134/134**

---

## V-02 — Single-axis: Output Format (Flat Imperative Sequence, No Skeleton)

### Essential (60/60) — all PASS (identical rationale to V-01; LOAD/ENFORCE fallback, VALIDATE Committee Type, all sections present, tier sort enforces challenge)

### Recommended (30/30) — all PASS

### Aspirational

| ID | Pass? | Evidence |
|----|-------|----------|
| C-09 through C-27 | PASS | All imperative; all structural labels inline (STANCE:, CITE:, RESPONDS-TO:, TALLY, SORT-CHECK, INVESTIGATE-FINDING-*); retry loops; re-entry path; named owners |
| C-28 | **PARTIAL (1)** | No pre-declared skeleton before Phase 0 execution. Inline PRINT: blocks with `[placeholder]` format at each phase satisfy "labels appear inline at correct positions" partial condition; full pass requires unified skeleton printed before any content |
| C-29 | PASS | LOOP UNTIL: GATE-N YES; ENFORCE Phase 2 executes unconditionally |
| C-30 | PASS | All phase instructions are verb-first: LOAD, ENFORCE, PRINT, WRITE, GATE, LOOP UNTIL, ASSIGN, EXECUTE, CONFIRM — no descriptive prose in instruction role |

**V-02 Score: 133/134** (C-28 partial)

---

## V-03 — Single-axis: Inertia Framing (Command-Driven Discovery Protocol)

### Essential (60/60) — all PASS

### Recommended (30/30) — all PASS

### Aspirational

| ID | Pass? | Evidence |
|----|-------|----------|
| C-09 | PASS | DISCOVER INERTIA-FINDING-D: REQUIRE "specific enough author would say I missed that"; ENFORCE non-obvious threshold explicit |
| C-12 | PASS | Four-command discovery protocol before any participant voice; DISCOVER: A/B/C/D with per-finding REQUIRE: constraints |
| C-16 | PASS | CONFIRM: GATE-1 with explicit question/answer/basis; non-obvious threshold as part of FINDING-D's own DISCOVER: command |
| C-10 through C-27 (except C-28) | PASS | All structural labels inline; retry loop with INCREMENT N; SORT-CHECK; STANCE:; CITE:; RESPONDS-TO:; TALLY; re-entry path |
| C-28 | **PARTIAL (1)** | No pre-declared skeleton. Inline GATE/TIER SORT/PRINT template blocks produce all required labels at correct positions — partial pass condition met |
| C-29 | PASS | ENFORCE gate loop within Phase 1; LOOP UNTIL YES; Phase 2 executes unconditionally |
| C-30 | PASS | DISCOVER:, REQUIRE:, ENFORCE:, CONFIRM:, ASSIGN:, LOAD:, PRINT:, EXECUTE:, VALIDATE: throughout — all instructions verb-first imperatives. Notable: per-finding DISCOVER: + REQUIRE: pairing embeds specificity constraint within the generation command |

**V-03 Score: 133/134** (C-28 partial)

---

## V-04 — Combined: Lifecycle Emphasis + C-30 (Phase-Commit Architecture)

### Essential (60/60) — all PASS

### Recommended (30/30) — all PASS

### Aspirational

| ID | Pass? | Evidence |
|----|-------|----------|
| C-26 | PASS | Five phases with COMMIT: statements at end of each; COMMIT Phase N: names what was produced before releasing |
| C-09 through C-27 (except C-28) | PASS | All structural labels; retry loops; sort validation; STANCE:; CITE: + RESPONDS-TO:; TALLY; re-entry path with Owner/Trigger |
| C-28 | **PARTIAL (1)** | COMMIT Phase N: statements and inline PRINT blocks with `___` placeholders appear at Phase 3, 4, 5 — labels at correct positions inline. Phase 1 and 2 use WRITE:/ASSIGN: without full placeholder blocks. No unified pre-declared skeleton before Phase 0. Partial pass condition met (structural labels inline) but not full pass (no unified pre-print step) |
| C-29 | PASS | ENFORCE: Phase 1 contains intra-phase gate loop; Phase 2 is always reached; loop controls when Phase 1 releases, not whether Phase 2 runs |
| C-30 | PASS | LOAD:, ENFORCE:, PRINT:, VALIDATE:, LABEL:, WRITE:, CONFIRM:, ASSIGN:, REQUIRE:, EXECUTE:, COUNT: throughout all phases; COMMIT Phase N: statements themselves use verb-first imperative register. Every instruction has explicit action verb |

**V-04 Score: 133/134** (C-28 partial)

---

## V-05 — Combined: Full Synthesis (Skeleton + Imperative Fill Rules + Named Labels + Loop Architecture + Phase-Commit)

### Essential (60/60) — all PASS

### Recommended (30/30) — all PASS

### Aspirational (44/44)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-09 | PASS | INERTIA-FINDING-D: REQUIRE specific enough author would say "I missed that" |
| C-10 | PASS | WRITE: Verdict; WRITE: Owner (named role) + Trigger (concrete deliverable); VALIDATE: both required |
| C-11 | PASS | ASSIGN: Tier 1/2/3; ENFORCE: Tier 1 speaks before all others; ENFORCE: Tier 3 speaks last |
| C-12 | PASS | Phase 1 investigation pre-dated Phase 3 voices; inertia framing as primary discovery axis |
| C-13 | PASS | PRINT: `STANCE:` standalone labeled line; VALIDATE: prose must not soften |
| C-14 | PASS | PRINT: `TALLY:` after last Phase 3 voice block and before Phase 5; CONFIRM: standalone line |
| C-15 | PASS | PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone; VALIDATE: committed declaration |
| C-16 | PASS | GATE-1 with Question/Answer/Basis; non-obvious threshold explicit |
| C-17 | PASS | REQUIRE Tier 3: fill CITE: before any endorsement prose; ENFORCE: named label first element |
| C-18 | PASS | VALIDATE: all-APPROVE → REOPEN Phase 2; RE-ASSIGN; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK |
| C-19 | PASS | PRINT: `RESPONDS-TO:` with REQUIRE quoting specific finding or concern; acceptable/fail examples |
| C-20 | PASS | ENFORCE: named label first element after `CITE:`; prose before label fails; content without label fails C-27 |
| C-21 | PASS | REQUIRE: quoted string names specific finding or concern; ACCEPTABLE/FAILS examples with attribution |
| C-22 | PASS | IF GATE-N NO → INCREMENT N; REQUIRE: each rewrite produces new labeled block; rewrite without visible label fails |
| C-23 | PASS | VALIDATE: both Owner and Trigger present; ENFORCE: not a team, named role only; ENFORCE: "sufficient progress" fails |
| C-24 | PASS | REQUIRE: sequential label increments by 1; label must appear in output, not only in reasoning |
| C-25 | PASS | SORT-CHECK with `Test:` and `Result:` in skeleton; ENFORCE: discrete labeled gate; correct ordering without block fails |
| C-26 | PASS | PHASE 0–5 labeled in skeleton; COMMIT: statements at end of each phase make sequential commitment explicit |
| C-27 | PASS | VALIDATE: INERTIA-FINDING-* as first token; `(a)` without label name fails; ENFORCE: downstream CITE: and RESPONDS-TO: reference labels by name |
| C-28 | **PASS** | STEP 1 prints full skeleton with all required slots: phase headers, INVESTIGATION-ATTEMPT-1/2 blocks, GATE-1/2, SORT-CHECK with Test/Result, STANCE:, CITE:, RESPONDS-TO:, TALLY, OUTCOME, DECISIONS/ACTION ITEMS/DISSENTING OPINIONS, **plus COMMIT Phase N: placeholders** — before any content is generated |
| C-29 | PASS | ENFORCE: gate loop runs within Phase 1; Phase 2 is pre-declared in skeleton — present unconditionally; gate controls when Phase 1 releases |
| C-30 | **PASS** | All STEP 2 fill rules are verb-first imperatives: LOAD:, ENFORCE:, PRINT:, VALIDATE:, CONFIRM:, LABEL:, WRITE:, REQUIRE:, ASSIGN:, COUNT:; CONFIRM: COMMIT Phase N as the fill instruction for commit slots — no descriptive prose appears in instruction role anywhere |

**V-05 Score: 134/134**

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | C-28 | C-30 |
|-----------|-----------|-------------|--------------|-----------|------|------|
| V-01 | 60/60 | 30/30 | 44/44 | **134/134** | PASS | PASS |
| V-02 | 60/60 | 30/30 | 43/44 | **133/134** | PARTIAL | PASS |
| V-03 | 60/60 | 30/30 | 43/44 | **133/134** | PARTIAL | PASS |
| V-04 | 60/60 | 30/30 | 43/44 | **133/134** | PARTIAL | PASS |
| V-05 | 60/60 | 30/30 | 44/44 | **134/134** | PASS | PASS |

**Rank**: V-01 = V-05 (134) > V-02 = V-03 = V-04 (133)

---

## Excellence Signals (V-05)

### Signal 1 — COMMIT: slots in skeleton create a dual-layer phase-completion guarantee

V-05 adds COMMIT: lines to the pre-declared skeleton itself (C-28: structural pre-declaration). The fill rule for each COMMIT: slot is `CONFIRM: COMMIT Phase N — write the commit line with [field] populated` (C-30: imperative). This means:
- C-28 makes the COMMIT: slot architecturally impossible to omit — it's a pre-declared container
- C-30 makes the fill instruction unambiguous — CONFIRM: is a verb-first command
- The COMMIT: mechanism is absent from V-01's skeleton (V-01 has identical phase headers and structural slots but no COMMIT: blocks)

V-05's commit is the missing layer: C-28 pre-declares structural slots; C-30 makes fill rules imperative; COMMIT: pre-declares **phase-completion assertions** and fills them imperatively. The three together create a simulation where no phase can silently produce incomplete output — the commit block exists, the commit instruction is a command.

### Signal 2 — COMMIT: content names specific artifacts, not generic completion

V-05's commit statements carry structured content: `COMMIT Phase 1: INVESTIGATION-ATTEMPT-___ complete, GATE-___ answered YES, INERTIA-FINDING-A through D active as citation anchors`. The `___` placeholders are filled with specific values (attempt number, gate number) when the fill rules execute. This makes each commit a forward-reference anchor: Phase 2 implicitly builds on Phase 1's committed findings by name. The commit is self-certifying (it names what it produced, not just that it ran).

**C-31 candidate**: Phase-commit specificity — COMMIT: statements must name the specific outputs produced (attempt number, gate status, active labels) rather than declaring generic phase completion. A commit that says `Phase 1 complete` without naming the active findings and gate answer is a structural declaration, not a self-certifying record.

---

```json
{"top_score": 134, "all_essential_pass": true, "new_patterns": ["Skeleton-embedded COMMIT: statements pre-declare phase completion as C-28 structural slots filled by CONFIRM: imperative commands — phase completion becomes both architecturally guaranteed (slot pre-declared, cannot be omitted) and normatively unambiguous (fill rule is an imperative command with exactly one interpretation); this dual-layer guarantee is absent when C-28 and C-30 are satisfied independently", "COMMIT: specificity pattern: commit statements name specific artifacts produced (attempt number, gate status, active INERTIA-FINDING-* labels) rather than declaring generic completion — creates forward-referenceable phase records that downstream phases build on by name; a generic 'phase complete' commit is a structural declaration; a specific 'GATE-1 answered YES, INERTIA-FINDING-A through D active' commit is a self-certifying record"]}
```
