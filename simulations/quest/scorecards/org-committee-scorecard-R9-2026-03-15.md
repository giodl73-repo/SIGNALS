# org:committee — Round 9 Scoring

**Rubric**: v9 | **Composite max**: 132 | **Scoring date**: 2026-03-16

---

## V-01 — Skeleton-First Declaration (C-28 primary)

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Skeleton's `## PHASE 0` has `Committee Type: ___`; fill rule requires ROB / shiproom / arch-board / user-specified declaration before any content. |
| C-02 | PASS | `Charter Source: ___` + `Participants:` slots in skeleton; fill rule reads `.roles/` with explicit Signal-defaults fallback. |
| C-03 | PASS | Phase 3 fill rule: "2–4 sentences from documented role orientation"; voice prose derived from charter-defined orientation. |
| C-04 | PASS | Skeleton pre-declares `### DECISIONS`, `### ACTION ITEMS`, `### DISSENTING OPINIONS` as discrete sections in Phase 5. |
| C-05 | PASS | Fill rule: "At least one participant must declare `STANCE: CONDITION` or `STANCE: BLOCK`. An all-APPROVE voice section is a sort error — reopen Phase 2." |

**Essential score: 60/60**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | `Agenda Item: ___` slot in skeleton; Phase 3 fill rule: tier voices ground in named INERTIA-FINDING labels from this specific agenda. |
| C-07 | PASS | ACTION ITEMS fill rule: `[Owner Role] — [specific action] — [deadline]`; explicit: "'Investigate further' is not a specific deliverable." |
| C-08 | PASS | DISSENTING OPINIONS skeleton slot with fill rule: "resolution path — concrete condition + named authority who confirms when condition is met." |

**Recommended score: 30/30**

### Aspirational (42 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | GATE question: "Does at least one finding reveal a non-obvious cost the proposal author is unlikely to have anticipated?" Gate enforces non-obviousness. |
| C-10 | PASS | Skeleton's `Re-entry path` section has `Owner: ___` and `Trigger: ___` slots; fill rule: "Both fields required." |
| C-11 | PASS | Skeleton Phase 3 block: `[One block per participant, Tier 1 → Tier 2 → Tier 3]`; fill rule enforces strict tier ordering. |
| C-12 | PASS | Phase 1 (investigation) skeleton section appears before Phase 3 (voices); framing: what does the status quo protect? |
| C-13 | PASS | Skeleton block: `STANCE: ___` appears above prose slot; fill rule: "standalone labeled declaration before any prose. Prose must not soften, qualify, or contradict." |
| C-14 | PASS | Phase 4 skeleton: `TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK` / `OUTCOME: ___` precedes Phase 5 section unconditionally. |
| C-15 | PASS | `STANCE: ___` is a labeled skeleton field, separate from the prose `___` field below it. Structural, not woven into prose. |
| C-16 | PASS | Skeleton: `GATE-1: Question: / Answer: / Basis:` with three distinct fields; loop instruction enforces re-evaluation until YES. |
| C-17 | PASS | Fill rule: "Tier 3: complete `CITE:` and `RESPONDS-TO:` before any endorsement prose." `CITE:` must reference a named INERTIA-FINDING label. |
| C-18 | PASS | Fill rule: "At least one participant must declare `STANCE: CONDITION` or `STANCE: BLOCK`. An all-APPROVE voice section is a sort error — reopen Phase 2, revise tier assignments, re-run SORT-CHECK." |
| C-19 | PASS | `RESPONDS-TO: "___" — ___` is a required skeleton slot for Tier 3; fill rule requires quoting the named concern with attribution. |
| C-20 | PASS | Fill rule: "`CITE: INERTIA-FINDING-[A/B/C/D] — [content]`. The named label must be the first element after `CITE:`. A citation that writes content without the label fails C-27." |
| C-21 | PASS | Fill rule: "quoted string must attribute a specific concern by name and content. Generic acknowledgment ('inertia concerns have been noted') fails C-21." |
| C-22 | PASS | Loop instruction in skeleton Phase 1: "If GATE-1 Answer: NO → output INVESTIGATION-ATTEMPT-2 block, output GATE-2 block, re-evaluate; repeat until GATE-N Answer: YES." |
| C-23 | PASS | Skeleton: `Owner: ___` and `Trigger: ___` in re-entry path; fill rule: "Both `Owner:` and `Trigger:` are required (C-23)." |
| C-24 | PASS | Skeleton includes `### INVESTIGATION-ATTEMPT-2` with explicit sequential note; loop instruction: "sequential label increments with each attempt." |
| C-25 | PASS | Skeleton pre-declares `### SORT-CHECK` with `Test: ___` and `Result: ___` fields; fill rule requires both fields. |
| C-26 | PASS | Six named, numbered phases in skeleton: PHASE 0 through PHASE 5. All sections pre-printed. |
| C-27 | PASS | INERTIA-FINDING-A through D appear in skeleton as named slot labels. Fill rule: "not just a parenthesized letter"; label is citation anchor for all downstream CITE: / RESPONDS-TO:. |
| C-28 | **PASS** | Opening instruction: "Before generating any simulation content, print the complete skeleton with all fields at their placeholder values." Skeleton pre-declares phase headers, INVESTIGATION-ATTEMPT blocks, GATE fields, SORT-CHECK, STANCE:/CITE:/RESPONDS-TO: slots, TALLY, all DECISIONS/ACTION ITEMS/DISSENTING OPINIONS fields — all with `___`. Full pass, not PARTIAL. |
| C-29 | **PASS** | Phase 1 skeleton includes explicit loop instruction: "Phase 2 is always reached. The loop controls when, not whether." Crucially, Phase 2 section (`## PHASE 2 — TIER SORT`) is pre-printed in the skeleton unconditionally — the gate loop cannot make Phase 2 absent because Phase 2 already exists on the page before any gate evaluates. |

**Aspirational score: 42/42 (21 × 2)**

### V-01 Composite

```
60 (essential) + 30 (recommended) + 42 (aspirational) = 132/132
```

---

## V-02 — INERTIA-FINDING Named Labels as Primary Citation Anchors (C-27 primary)

### Essential: 60/60 — all pass (Phase 0–5 structure present; role-grounded voices; three sections in Phase 5; challenge requirement explicit)

### Recommended: 30/30 — all pass (agenda-threaded voices; action item format; dissent resolution paths)

### Aspirational

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 through C-27 | PASS | All 19 criteria pass. Named INERTIA-FINDING labels throughout; CITE: / RESPONDS-TO: labeled format; GATE-1 loop with sequential attempt labels; SORT-CHECK with Test:/Result:; named phase sections; re-entry path with Owner/Trigger/Resolves. |
| C-28 | **PARTIAL** | No pre-declared skeleton. Labels and structural slots emerge inline as content is generated. C-28: "An output that produces all required labels at the correct positions but only as they emerge from content generation (labels appear inline, not pre-declared) is a partial pass." |
| C-29 | PASS | Phase 2 section is present in the prompt as `### PHASE 2 — TIER SORT` after Phase 1. Loop instruction: "Phase 2 is reached unconditionally once the gate answers YES. The gate does not control whether Phase 2 exists." |

**Aspirational score: 40 (20 × 2) + 1 (C-28 PARTIAL) = 41/42**

### V-02 Composite

```
60 + 30 + 41 = 131/132
```

---

## V-03 — Phrasing Register — Imperative Micro-Instructions

### Essential: 60/60 — all pass (Phase 0 PRINT/LOAD; role-oriented voices; three Phase 5 sections; VALIDATE enforces challenge requirement)

### Recommended: 30/30 — all pass (agenda-specific voices; action item format; dissent resolution path validation)

### Aspirational

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 through C-27 | PASS | `LOOP UNTIL: GATE-N Answer: YES` with `IF/THEN` blocks; sequential labels; SORT-CHECK gate with `Test:`/`Result:` as discrete gate; named phases; VALIDATE blocks for CITE/RESPONDS-TO label rules. |
| C-28 | **PARTIAL** | No pre-declared skeleton. Imperative register is effective for reducing interpretive latitude but labels appear inline during content generation. |
| C-29 | PASS | `LOOP UNTIL: GATE-N Answer: YES` → `IF YES → EXIT LOOP → CONTINUE TO PHASE 2 (unconditional — phase 2 always executes)`. Phase 2 is a separate section after Phase 1 in the prompt. |

**Aspirational score: 41/42**

### V-03 Composite

```
60 + 30 + 41 = 131/132
```

---

## V-04 — Lifecycle Emphasis + C-29 Loop Diagrams

### Essential: 60/60 — all pass (five-phase structure; role-grounded voices; three Phase 5 sections; challenge requirement with all-APPROVE detection)

### Recommended: 30/30 — all pass (INERTIA-FINDING-grounded agenda specificity; action format; dissent with concrete trigger)

### Aspirational

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 through C-27 | PASS | ASCII loop diagrams show Phase 2 as unconditional exit from Phase 1 box; "Phase 1 commits when GATE-N Answer: YES. → Phase 2 (unconditional)"; explicit phase-commit transitions; named INERTIA-FINDING labels throughout. |
| C-28 | **PARTIAL** | No pre-declared skeleton. Loop diagrams are structurally expressive for C-29 but don't pre-declare STANCE:/CITE:/RESPONDS-TO:/TALLY slots. Labels appear inline. |
| C-29 | PASS | ASCII diagram is the strongest visual expression of C-29: Phase 2 box appears below the Phase 1 box with `↓ (unconditional)` arrow. Loop back-arrow cycles within Phase 1. Phase 2 is structurally present in the diagram before any gate evaluates. |

**Aspirational score: 41/42**

### V-04 Composite

```
60 + 30 + 41 = 131/132
```

---

## V-05 — Full Synthesis (Skeleton + Named Labels + Loop Architecture)

### Essential: 60/60 — all pass (skeleton Phase 0 declares committee type; `.roles/` fallback; role-lens voices; three Phase 5 sections; challenge requirement)

### Recommended: 30/30 — all pass (agenda-threaded via INERTIA-FINDING references in voice fill rules; action item format; dissent with named authority)

### Aspirational

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | PASS | GATE targets non-obvious cost; INERTIA-FINDING-D specifically defined as "the cost the proposal author almost certainly did not account for." |
| C-10 | PASS | Skeleton pre-declares `Verdict:`, `Conditions for full approval:`, `Owner:`, `Trigger:` in DECISIONS section. |
| C-11 | PASS | "Fill one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3." |
| C-12 | PASS | Phase 1 investigation (skeleton section) precedes Phase 3 voices; "what does the status quo protect?" |
| C-13 | PASS | Skeleton: `STANCE: ___` is a standalone labeled field above the prose `___` slot; fill rule: "standalone labeled line before any prose." |
| C-14 | PASS | Phase 4 skeleton: `TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK` / `OUTCOME: ___` — pre-declared slot appears between Phase 3 and Phase 5. |
| C-15 | PASS | `STANCE: ___` in skeleton as a structural field separate from prose slot. Fill rule emphasizes standalone label. |
| C-16 | PASS | Skeleton: `GATE-1: Question: / Answer: / Basis:` slots; fill rule enforces non-obvious threshold and rewrite loop. |
| C-17 | PASS | Fill rule: "Fill `CITE:` and `RESPONDS-TO:` before writing endorsement prose" for Tier 3; CITE format requires named label first. |
| C-18 | PASS | "An all-APPROVE fill means Phase 2 sort is invalid — reopen Phase 2, revise tier assignments, re-run SORT-CHECK." |
| C-19 | PASS | Skeleton: `RESPONDS-TO: "___" — ___` as required Tier 3 slot; fill rule requires named concern with attribution. |
| C-20 | PASS | Fill rule: "The named label (`INERTIA-FINDING-A`, etc.) must be the first element after `CITE:`. Prose before the label fails C-20." |
| C-21 | PASS | Fill rule: "Acceptable: `INERTIA-FINDING-A: [paraphrase]`... Fails: 'Inertia concerns have been acknowledged' (generic — no name, no content)." |
| C-22 | PASS | GATE fill rule: "GATE-1 Answer: NO → Phase 1 loop continues within Phase 1. → Fill INVESTIGATION-ATTEMPT-2 block (already in skeleton)." |
| C-23 | PASS | Skeleton: `Owner: ___` and `Trigger: ___` in re-entry path; fill rule: "Both fields required (C-23)." |
| C-24 | PASS | "Each new attempt must produce a new labeled block in output. A claimed internal rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24." |
| C-25 | PASS | Skeleton: `### SORT-CHECK` with `Test: Tier 1 and Tier 2 both empty?` and `Result: ___` — both fields pre-declared. |
| C-26 | PASS | Skeleton pre-declares PHASE 0 through PHASE 5 as headers. |
| C-27 | PASS | INERTIA-FINDING-A through D in skeleton slots; fill rule: "The label is the primary identifier — not an annotation on a letter." CITE format enforces named label first. |
| C-28 | **PASS** | STEP 1 instruction: "Print the complete skeleton below before generating any simulation content. Print every section header, every field label, and every `___` placeholder. Do not fill any values in this step." Skeleton pre-declares: phase headers (C-26), INVESTIGATION-ATTEMPT-1 and -2 blocks (C-24), GATE-1 and -2 with Question/Answer/Basis (C-16), SORT-CHECK with Test:/Result: (C-25), STANCE:/CITE:/RESPONDS-TO: per participant block (C-15/C-20/C-21), TALLY line (C-14), DECISIONS/ACTION ITEMS/DISSENTING OPINIONS with all sub-fields (C-04/C-07/C-08/C-23). Full pass. |
| C-29 | **PASS** | GATE-1 fill rule: "GATE-1 Answer: NO → Phase 1 loop continues within Phase 1. → Fill INVESTIGATION-ATTEMPT-2 block (already in skeleton)." AND "Phase 2 is always reached. The loop controls when, not whether." Decisive: Phase 2's skeleton section (`## PHASE 2 — TIER SORT`) is pre-printed in the skeleton unconditionally by STEP 1 — the gate loop operates within Phase 1's fill rules; Phase 2 cannot be made absent because its skeleton slot already exists on the page. |

**Aspirational score: 42/42**

### V-05 Composite

```
60 + 30 + 42 = 132/132
```

---

## Rankings

| Rank | Variation | Essential | Recommended | Aspirational | **Composite** |
|------|-----------|-----------|-------------|--------------|---------------|
| 1 (tie) | **V-01** | 60/60 | 30/30 | 42/42 | **132/132** |
| 1 (tie) | **V-05** | 60/60 | 30/30 | 42/42 | **132/132** |
| 3 (tie) | V-02 | 60/60 | 30/30 | 41/42 | **131/132** |
| 3 (tie) | V-03 | 60/60 | 30/30 | 41/42 | **131/132** |
| 3 (tie) | V-04 | 60/60 | 30/30 | 41/42 | **131/132** |

The only differentiator is C-28: V-01 and V-05 pre-declare the full skeleton before content generation (full PASS); V-02, V-03, and V-04 produce labels inline (PARTIAL).

---

## Excellence Signals from V-01 / V-05

**Signal 1: Pre-declared skeleton makes subsequent phase sections structurally present before any gate evaluates.**
In V-01 and V-05, Phase 2's skeleton section appears on the page from STEP 1, before any Phase 1 gate answer is computed. C-29's test — "can the simulation terminate after Phase 1 without reaching Phase 2?" — answers NO by construction. The skeleton is the enforcement mechanism: later phases cannot be made absent by gate logic because they already exist as declared structural slots. V-04's loop diagrams show Phase 2 as an unconditional exit target; V-01/V-05's skeleton shows Phase 2 as an unconditional structural presence.

**Signal 2: Two-pass architecture (declare then fill) prevents structural collapse under generation pressure.**
V-05 (and to a degree V-01) separates STEP 1 (print skeleton — no content) from STEP 2 (fill rules — all detail). This separation prevents fill instruction complexity from competing with structural declaration: the skeleton is legible as a template; the fill rules are legible as a protocol. When the skeleton exists as a committed artifact before any content generation begins, section skipping becomes a visible gap rather than an invisible omission.

**Signal 3: Bracket annotations for loop scope within phase sections outperform inter-phase conditionals.**
The inline loop instruction `[GATE-1 is NO → fill INVESTIGATION-ATTEMPT-2 within Phase 1 — Phase 2 is unconditional]` embedded in the Phase 1 section communicates both scope (the loop lives in Phase 1) and commitment (Phase 2 is unconditional) in a single, visually contained annotation. This is more reliable than a prose conditional at the end of Phase 1 instructions because the annotation does not resemble a halt condition — it reads as a within-phase behavior specification.

---

```json
{"top_score": 132, "all_essential_pass": true, "new_patterns": ["Pre-declared skeleton makes subsequent phase sections structurally present before any gate evaluates — gates can delay filling but cannot eliminate phases already declared as skeleton slots, satisfying C-29 by construction", "Two-pass architecture (STEP 1: print skeleton; STEP 2: fill rules) prevents structural collapse under generation pressure by separating structural declaration from content protocol — a skeleton gap is visible; an inline omission is not"]}
```
