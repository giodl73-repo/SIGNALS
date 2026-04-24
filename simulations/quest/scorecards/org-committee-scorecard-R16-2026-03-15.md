## org:committee — Round 16 Scoring (v16 Rubric)

### Rubric Structure Recap

- **Essential**: C-01–C-05 × 12 pts = 60 pts (all-fail-means-rubric-fail)
- **Recommended**: C-06–C-08 × 10 pts = 30 pts
- **Aspirational**: C-09–C-41 × 2 pts each = 66 pts (partial = 1 pt)
- **Composite max**: 156 pts

**New in v16**: C-40 (seal declarations in named manifest sections) and C-41 (bidirectionality constraint clause in commit cross-references).

---

## V-01 — Single-Axis: Lifecycle Emphasis

**Architecture**: Two-step skeleton + fill. Minimal diff from R15. Four targeted upgrades: INERTIA INVARIANT placeholder in skeleton, STANCE INVARIANT placeholder in skeleton, PHASE-1-COMMIT bidirectionality clause, PHASE-3-COMMIT bidirectionality clause.

### Essential (60/60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | `Committee Type: ___` in skeleton with bilateral VALIDATE ACCEPTABLE/FAILS at Phase 0 fill rule |
| C-02 | PASS | `LOAD: charter from .roles/`; fallback to Signal defaults with Inertia-Advocate |
| C-03 | PASS | `WRITE: 2-4 sentences per participant from their charter-documented role orientation` |
| C-04 | PASS | Phase 5 skeleton has `### DECISIONS`, `### ACTION ITEMS`, `### DISSENTING OPINIONS` explicitly |
| C-05 | PASS | `VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid` |

### Recommended (30/30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Agenda Item fill rule references "the specific item under review as stated in the request"; Phase 3 voices "responding to this specific agenda item" |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]` with `REQUIRE: all three parts; "investigate" alone fails` |
| C-08 | PASS | Dissenting opinions fill rule: "resolution path (concrete condition + named authority who confirms when condition is met)" |

### Aspirational (66/66)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | INERTIA-FINDING-D: "non-obvious cost the proposal author almost certainly did not account for" |
| C-10 | PASS | Phase 5: Verdict + Conditions for full approval + Re-entry path (Owner + Trigger) |
| C-11 | PASS | Three-tier sort (Tier 1 → 2 → 3), tie-break field in skeleton, SORT-CHECK gate |
| C-12 | PASS | Investigation precedes all voices; Tier 1 concerns grounded in named INERTIA-FINDING labels |
| C-13 | PASS | `PRINT: STANCE: [BLOCK/CONDITION/APPROVE] as a standalone labeled line before any prose` |
| C-14 | PASS | Phase 4 TALLY line before Phase 5 MINUTES |
| C-15 | PASS | Bilateral VALIDATE: `FAILS: "STANCE: BLOCK (pending clarification)" — qualified token softens the structural commitment` |
| C-16 | PASS | GATE-1 with YES/NO question and Basis field |
| C-17 | PASS | `REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose` |
| C-18 | PASS | `VALIDATE: all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK` |
| C-19 | PASS | `REQUIRE (Tier 3): fill RESPONDS-TO: before endorsement prose` |
| C-20 | PASS | Bilateral VALIDATE: CITE: opens with INERTIA-FINDING-* label; parenthesized-letter FAILS case |
| C-21 | PASS | Bilateral VALIDATE for RESPONDS-TO:; `FAILS: "Inertia concerns have been acknowledged" — generic, no attribution` |
| C-22 | PASS | `IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new findings; re-evaluate; REPEAT` |
| C-23 | PASS | Owner: named role; Trigger: "concrete deliverable, evidence artifact, or event"; "ENFORCE: 'sufficient progress' fails" |
| C-24 | PASS | `REQUIRE: each rewrite produces a new labeled block; a rewrite without INVESTIGATION-ATTEMPT-N+1 fails C-22 and C-24` |
| C-25 | PASS | `ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both Test: and Result: fields` |
| C-26 | PASS | Phase 0–5 with PHASE-N-COMMIT: terminal markers |
| C-27 | PASS | INERTIA-FINDING-A through D named label tokens; bilateral VALIDATE against parenthesized-letter forms |
| C-28 | PASS | Step 1 prints full skeleton with all headers, field labels, `___` placeholders, PHASE-N-COMMIT: blocks, INERTIA/STANCE INVARIANT slots |
| C-29 | PASS | `ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached` |
| C-30 | PASS | All fill rules are verb-first: LOAD, ENFORCE, PRINT, WRITE, REQUIRE, CONFIRM, VALIDATE, LABEL |
| C-31 | PASS | PHASE-N-COMMIT: [locked] at terminal of each phase |
| C-32 | PASS | `ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` in every commit block |
| C-33 | PASS | PHASE-1-COMMIT: "Citation-anchor manifest declared in ## INERTIA RECORD above; Findings A–D locked" — delegates to named section |
| C-34 | PASS | INERTIA RECORD entries require "one-phrase anchor"; bilateral VALIDATE: `FAILS: INERTIA-FINDING-A: [one-phrase anchor] — unfilled skeleton placeholder is not a real anchor` |
| C-35 | PASS | PHASE-3-COMMIT: "Vote-anchor manifest declared in ## STANCE MANIFEST above; All stances locked" |
| C-36 | PASS | Bilateral ACCEPTABLE/FAILS on: INERTIA RECORD entries, CITE:, RESPONDS-TO:, STANCE:, Committee Type |
| C-37 | PASS | `## INERTIA RECORD` and `## STANCE MANIFEST` appear as named skeleton section headers (not only inside commit blocks) |
| C-38 | PASS | PHASE-1-COMMIT: "declared in ## INERTIA RECORD above"; PHASE-3-COMMIT: "declared in ## STANCE MANIFEST above" |
| C-39 | PASS | Phase 0 VALIDATE with `ACCEPTABLE: Committee Type — ROB` / `FAILS: Committee Type — unspecified` |
| C-40 | PASS | Skeleton carries `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___` placeholder; fill rule: `PRINT: INERTIA INVARIANT...` with bilateral VALIDATE; matching STANCE INVARIANT at Phase 3 |
| C-41 | PASS | PHASE-1-COMMIT skeleton: "modifications to that record require updating this commit; modifications to this commit require updating that record"; PHASE-3-COMMIT: parallel clause; both pre-declared in skeleton and enforced in fill rules |

**V-01 Score: 60 + 30 + 66 = 156/156**

---

## V-02 — Single-Axis: Output Format (Flat Command Sequence)

**Architecture**: No skeleton pre-declaration. All requirements as direct imperative commands in a single execution sequence.

### Essential: 60/60 — all present with bilateral VALIDATE (C-01 bilateral at Phase 0)

### Recommended: 30/30 — all present

### Aspirational Differences from V-01

| ID | Verdict | Evidence |
|----|---------|----------|
| C-28 | **FAIL** | No two-step skeleton; instructions are generated inline as content is produced, not pre-declared as empty containers. The variations hypothesis explicitly targets C-28 as the gap. |
| All others | PASS | All structural slot labels (INERTIA-FINDING-*, INERTIA RECORD, STANCE MANIFEST, PHASE-N-COMMIT:, SORT-CHECK, TALLY, STANCE:, CITE:, RESPONDS-TO:) are present and correctly imperative. C-40 seal declarations expressed as PRINT instructions; C-41 bidirectionality clause present in PHASE-1-COMMIT and PHASE-3-COMMIT. |

**Aspirational: 64/66 (C-28 = 0)**

**V-02 Score: 60 + 30 + 64 = 154/156**

---

## V-03 — Single-Axis: Phrasing Register (Conversational + Skeleton)

**Architecture**: Two-step skeleton preserved. Fill guidance in readable explanatory register. Key commands (ENFORCE, PRINT) retain imperative register; framing and seal/coupling explanations are conversational.

### Essential: 60/60 — committee type, participants, role lens, three sections, challenge all enforced

### Recommended: 30/30 — agenda specificity, action items, dissent paths all present

### Aspirational Differences

| ID | Verdict | Evidence |
|----|---------|----------|
| C-30 | **PARTIAL** (1 pt) | Phase 0 opens with "The first thing to establish is which type of committee is meeting..." — descriptive prose, not a verb-first command. Phase 3: "Tier 1 speaks first, then Tier 2, then Tier 3. For each participant, the very first thing is a STANCE: line..." — conversational framing. Phase 1 finding instructions: "INERTIA-FINDING-A: name the specific production artifact..." — implicit verb without the explicit token (WRITE/PRINT). Critical ENFORCE and PRINT slots remain imperative; framing around them is descriptive. |
| C-36 | **PARTIAL** (1 pt) | Content-fill bilateral examples use `Correct:` and `Wrong:` format rather than `ACCEPTABLE:` and `FAILS:` format. Bilateral examples exist for INERTIA RECORD entries, CITE:, RESPONDS-TO:, and STANCE:, but not in VALIDATE block structure. The intent is bilateral but the label tokens differ from the rubric's structural requirement. |
| C-39 | **PARTIAL** (1 pt) | Committee Type bilateral examples appear as conversational narrative ("A correct opening: `Committee Type — ROB` — ... A wrong opening: `Committee Type — unspecified`...") rather than a formal `VALIDATE:` block with `ACCEPTABLE:/FAILS:` fields. Bilateral examples exist but not as a declared VALIDATE rule. |
| C-40 | PASS | Skeleton carries INERTIA INVARIANT and STANCE INVARIANT placeholder slots; fill guidance explicitly states the seal declaration text and declares it "not optional" with rationale for why it is required. The structural requirement is met. |
| C-41 | PASS | PHASE-1-COMMIT and PHASE-3-COMMIT both include full bidirectionality clauses in skeleton and fill rules. The conversational explanation after PHASE-1-COMMIT fill rule ("The commit's cross-reference is not just a pointer — it is a contract...") reinforces rather than undermines the requirement. |
| All others | PASS | Skeleton pre-declared (C-28 passes); intra-phase retry loops present (C-29); all named structural slots present. |

**Aspirational: 63/66 (C-30 = 1, C-36 = 1, C-39 = 1)**

**V-03 Score: 60 + 30 + 63 = 153/156**

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing

**Architecture**: Full skeleton. Inertia-Advocate synthesized as mandatory participant if absent. C-40 framed as "Inertia Invariant" structural identity — the adversarial floor, not merely a lifecycle marker. C-41 with explicit VALIDATE naming the C-38/C-41 compliance boundary.

### Essential: 60/60

| ID | Verdict | Additional Evidence |
|----|---------|---------------------|
| C-01 | PASS | Bilateral VALIDATE including synthesized-Inertia-Advocate confirmation |
| C-02 | PASS | `CONFIRM: Inertia-Advocate role is present`; `ENFORCE: if charter has no Inertia-function role — SYNTHESIZE Inertia-Advocate` |
| C-03 | PASS | Each participant's voice tied to charter orientation; Inertia-Advocate explicitly references INERTIA-FINDING-D |
| C-04 | PASS | Three sections present |
| C-05 | PASS | All-approve triggers Phase 2 reopen |

### Recommended: 30/30

### Aspirational (66/66)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-12 | **PARTICULARLY STRONG** | Inertia-Advocate synthesized if absent from charter; INERTIA-FINDING-D labeled as "the Inertia-Advocate's primary argument"; Tier 1 `ENFORCE: Inertia-Advocate is always Tier 1` |
| C-27 | PASS | Named labels + PHASE-2-COMMIT confirms "Inertia-Advocate in Tier 1" |
| C-28 | PASS | Full skeleton with all slots including INERTIA/STANCE INVARIANT pre-declared |
| C-30 | PASS | All fill rules verb-first (LOAD, CONFIRM, ENFORCE, PRINT, WRITE, VALIDATE) throughout all phases |
| C-36 | PASS | All content-fill VALIDATE rules have formal ACCEPTABLE/FAILS pairs |
| C-37 | PASS | Named sections present |
| C-38 | PASS | Commit blocks reference sections by heading |
| C-39 | PASS | Bilateral VALIDATE at Committee Type declaration slot |
| C-40 | **PARTICULARLY STRONG** | INERTIA INVARIANT seal text: "sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1. **These findings are the adversarial floor for all advocate voices.**" — seal asserts section's purpose, not merely its lifecycle boundary. Bilateral VALIDATE with `FAILS: ## INERTIA RECORD with correct entries but no INERTIA INVARIANT line — immutability is assumed, not declared; fails C-40` |
| C-41 | **PARTICULARLY STRONG** | ENFORCE + bilateral VALIDATE: `ACCEPTABLE: PHASE-1-COMMIT includes "modifications to that record require updating this commit; modifications to this commit require updating that record" — coupling obligation stated in both directions` / `FAILS: PHASE-1-COMMIT reads only "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" — navigational pointer, no coupling contract; fails C-41`. The FAILS case explicitly distinguishes C-38 compliance from C-41 compliance. Parallel enforcement at PHASE-3-COMMIT. |

**Aspirational: 66/66**

**V-04 Score: 60 + 30 + 66 = 156/156**

---

## V-05 — Full Synthesis

**Architecture**: All axes. Every criterion C-01 through C-41. Inertia-Advocate mandatory (synthesized if absent). Skeleton includes INERTIA INVARIANT and STANCE INVARIANT slots. Explicit VALIDATE with bilateral examples for C-40 (seal declarations) and C-41 (bidirectionality clauses). Tie-break stated explicitly. C-23 bilateral VALIDATE added at Phase 5.

### Essential: 60/60

All essential criteria present with bilateral VALIDATE. Inertia-Advocate confirmed present including in PHASE-0-COMMIT ("Inertia-Advocate confirmed present").

### Recommended: 30/30

### Aspirational (66/66)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-28 | PASS | Skeleton instruction explicitly includes "INERTIA/STANCE INVARIANT slot" in what must be pre-declared |
| C-30 | PASS | Fully imperative throughout all phases |
| C-36 | PASS | All four C-36 categories covered with bilateral VALIDATE |
| C-37 | PASS | Named sections present |
| C-38 | PASS | Heading cross-references in both commits |
| C-39 | PASS | Bilateral VALIDATE at Phase 0 Committee Type slot |
| C-40 | PASS | VALIDATE with `ACCEPTABLE` / `FAILS: ...no INERTIA INVARIANT line — section is navigable and cited but carries no stated lifecycle boundary; fails C-40` |
| C-41 | PASS | VALIDATE with `ACCEPTABLE` / `FAILS: PHASE-1-COMMIT reads only "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" — heading cross-reference present but coupling obligation unstated; passes C-38, fails C-41` |
| C-23 (Phase 5) | **BONUS COVERAGE** | Bilateral VALIDATE: `ACCEPTABLE: Owner = [PM Lead], Trigger = signed load-test report at >99.9% SLA delivered to Arch-Board chair` / `FAILS: Trigger = address scalability concerns — trigger is a condition, not a concrete event; fails C-23`. Not required by C-36 (beyond the four listed categories) but extends bilateral coverage to Phase 5. |

**Aspirational: 66/66**

**V-05 Score: 60 + 30 + 66 = 156/156**

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | **Total** | Gap |
|-----------|-----------|-------------|--------------|-----------|-----|
| V-01 | 60/60 | 30/30 | 66/66 | **156/156** | — |
| V-02 | 60/60 | 30/30 | 64/66 | **154/156** | C-28 absent |
| V-03 | 60/60 | 30/30 | 63/66 | **153/156** | C-30 partial, C-36 partial, C-39 partial |
| V-04 | 60/60 | 30/30 | 66/66 | **156/156** | — |
| V-05 | 60/60 | 30/30 | 66/66 | **156/156** | — |

**Ranking**: V-01 = V-04 = V-05 (156) > V-02 (154) > V-03 (153)

---

## Excellence Signals from Top Scorers

**V-04** is the architectural standout even though all three top scorers tie at 156:

1. **Seal declaration as purpose assertion, not just lifecycle marker** — V-04's INERTIA INVARIANT reads: "sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1. These findings are the adversarial floor for all advocate voices." The second sentence elevates the seal from a lifecycle close to a structural contract: the sealed findings are the floor against which all advocate voices are tested. V-01 and V-05 have only the lifecycle assertion without the purpose clause.

2. **C-38/C-41 compliance boundary named in VALIDATE FAILS case** — V-04 and V-05's VALIDATE for C-41 includes: `FAILS: PHASE-1-COMMIT reads only "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" — navigational pointer, no coupling contract; **passes C-38, fails C-41**`. Naming the exact criterion the failure violates (vs. just "fails C-41") makes the distinction between cross-reference (C-38) and governing contract (C-41) a testable, named boundary. V-01 has no C-41 VALIDATE rule at all — the bidirectionality clause is in the skeleton and fill PRINT instruction but not validated.

3. **Bilateral VALIDATE extended to Phase 5 re-entry path** (V-05 exclusive) — `ACCEPTABLE: Trigger = signed load-test report at >99.9% SLA` / `FAILS: Trigger = address scalability concerns` at C-23. Not required by C-36's four listed categories, but extends bilateral coverage to the final structural content requirement. Forward-leaning pattern toward C-36-style coverage for all structural content requirements, not only the four explicitly listed.

---

```json
{"top_score": 156, "all_essential_pass": true, "new_patterns": ["seal declaration asserts section purpose beyond lifecycle boundary (adversarial-floor clause makes immutability a design principle, not a phase-close side effect)", "bidirectionality VALIDATE FAILS case names the C-38/C-41 distinction explicitly (passes C-38, fails C-41) — makes the pointer-vs-contract boundary a testable named rule rather than an inferred property", "bilateral VALIDATE extended to Phase 5 re-entry path Owner/Trigger requirement — C-36 coverage pattern applied beyond the four enumerated content-fill categories"]}
```
