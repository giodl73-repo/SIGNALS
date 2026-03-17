## org:committee — Round 11 Scorecard

**Rubric**: v11 | **New criterion**: C-31 (phase transitions carry explicit commit declarations) | **Max**: 136

---

### Variation Scores

#### V-01 — Single-axis: Lifecycle Emphasis (PHASE-N-COMMIT: locked markers, minimal diff from R10 V-05)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | `VALIDATE: Committee Type is declared before any other content` |
| **C-02** | PASS | `LOAD: charter from .craft/roles/` + Signal defaults fallback with disclosure |
| **C-03** | PASS | `WRITE: from charter-documented role orientation` per participant |
| **C-04** | PASS | Phase 5 has DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| **C-05** | PASS | `VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2` |
| C-06 | PASS | Agenda Item declared in Phase 0; each voice responds to specific item |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]`; "investigate alone fails" |
| C-08 | PASS | `CONFIRM: resolution path names a concrete trigger, not a general condition` |
| C-09 | PASS | INERTIA-FINDING-D: non-obvious cost; REQUIRE: "proposal author would say I missed that" |
| C-10 | PASS | OUTCOME derivation rule; re-entry path with Owner + Trigger |
| C-11 | PASS | Tier 1 → Tier 2 → Tier 3; ENFORCE: challengers speak before all others |
| C-12 | PASS | Phase 1 investigation precedes Phase 3 voices structurally |
| C-13 | PASS | `VALIDATE: STANCE: is a committed declaration; prose must not soften it` |
| C-14 | PASS | TALLY in Phase 4 skeleton slot before Phase 5 header |
| C-15 | PASS | `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line in skeleton |
| C-16 | PASS | GATE-1 with YES/NO; `CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost?` |
| C-17 | PASS | `REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose` |
| C-18 | PASS | `VALIDATE: at least one CONDITION or BLOCK; all-APPROVE → REOPEN Phase 2` |
| C-19 | PASS | `RESPONDS-TO: "[named concern]" — [one sentence addressing it]` required |
| C-20 | PASS | `ENFORCE: named label is the first element after CITE:`; prose before label fails |
| C-21 | PASS | `REQUIRE: quoted string names a specific finding or concern; generic fails` |
| C-22 | PASS | Gate NO → INCREMENT N → relabel → rewrite → re-gate → REPEAT within Phase 1 |
| C-23 | PASS | `VALIDATE: both Owner and Trigger present; a path missing either field is incomplete` |
| C-24 | PASS | `REQUIRE: sequential label increments by 1 with each attempt; label must appear in output` |
| C-25 | PASS | `ENFORCE: SORT-CHECK must appear as a discrete labeled gate with Test: and Result: fields` |
| C-26 | PASS | Six numbered, named phases; each closes with PHASE-N-COMMIT: [locked] |
| C-27 | PASS | `VALIDATE: each finding carries INERTIA-FINDING-* label as first token; (a) without label fails C-27` |
| C-28 | PASS | Full skeleton pre-declared (STEP 1) before any content generation (STEP 2) |
| C-29 | PASS | Gate loop runs within Phase 1; `Phase 2 is unconditional`; loop controls release not destination |
| C-30 | PASS | All fill rules verb-first imperative: LOAD:, ENFORCE:, PRINT:, VALIDATE:, WRITE:, REQUIRE:, CONFIRM: |
| C-31 | PASS | PHASE-N-COMMIT: [locked] in skeleton + ENFORCE: terminal position + PRINT: fill rule in every phase |

**V-01 score: 136/136** — All essential PASS.

---

#### V-02 — Single-axis: Output Format — Flat Command Sequence (no skeleton)

| Key Criteria | Result | Note |
|---|---|---|
| C-01 through C-05 | PASS | All essential satisfied |
| C-06, C-07, C-08 | PASS | All recommended satisfied |
| C-09–C-27, C-29–C-31 | PASS | All aspirational satisfied |
| **C-28** | **FAIL** | No skeleton pre-declaration — flat command sequence only; slots emerge inline, not pre-declared |
| C-30 | PASS | All instructions verb-first imperative throughout (LOAD, ENFORCE, ASSIGN, WRITE, PRINT, CONFIRM) |
| C-31 | PASS | PHASE-N-COMMIT: [locked] present and ENFORCE: terminal position stated in every phase |

**V-02 score: 134/136** — Lost C-28 (2 pts).

---

#### V-03 — Single-axis: Phrasing Register — Conversational Frame

| Key Criteria | Result | Note |
|---|---|---|
| C-01 through C-05 | PASS | All essential satisfied |
| C-06, C-07, C-08 | PASS | All recommended satisfied |
| C-09–C-27, C-29, C-31 | PASS | Aspirational otherwise intact |
| **C-28** | **FAIL** | No skeleton pre-declaration — narrative instruction format only |
| **C-30** | **PARTIAL** | PHASE-N-COMMIT: blocks themselves are imperative; main guidance uses descriptive prose ("Start by identifying...", "Sort all participants...", "Write one block per participant") — not verb-first imperative fill rules |
| C-31 | PASS | PHASE-N-COMMIT: [locked] blocks with `\| NO PHASE N CONTENT MAY FOLLOW THIS LINE.` |

**V-03 score: 133/136** — Lost C-28 (2 pts) + C-30 partial (1 pt lost).

---

#### V-04 — Combined: Lifecycle Emphasis + Inertia Framing

| Key Criteria | Result | Note |
|---|---|---|
| C-01 through C-05 | PASS | All essential satisfied |
| C-06, C-07, C-08 | PASS | All recommended satisfied |
| C-09–C-27, C-29–C-31 | PASS | All aspirational except C-28 |
| **C-28** | **FAIL** | No skeleton print step — direct phase execution sequence only |
| C-30 | PASS | All phase instructions verb-first imperative (LOAD:, ENFORCE:, PRINT:, WRITE:, VALIDATE:, REQUIRE:, ASSIGN:, CONFIRM:) |
| C-31 | PASS | PHASE-N-COMMIT: [locked] with ENFORCE: terminal position; Phase 1 commit enumerates locked INERTIA-FINDING tokens by name (citation-anchor manifest) |

**V-04 score: 134/136** — Lost C-28 (2 pts).

---

#### V-05 — Full Synthesis — Skeleton + Imperative Fill Rules + PHASE-N-COMMIT: Locked Terminal Markers

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** | PASS | `VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01` |
| **C-02** | PASS | `LOAD: charter from .craft/roles/` + fallback with disclosure |
| **C-03** | PASS | Charter-documented role orientation required for each participant |
| **C-04** | PASS | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS all required in Phase 5 |
| **C-05** | PASS | `VALIDATE: at least one CONDITION or BLOCK; all-APPROVE → REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK; RE-EXECUTE Phase 3` |
| C-06 | PASS | Agenda Item declared; voices respond to this specific item |
| C-07 | PASS | Three-part format with specific deliverable; "investigate alone fails" |
| C-08 | PASS | Resolution path: concrete trigger + named confirming authority |
| C-09–C-31 (all aspirational) | PASS | All 23 criteria satisfied |
| C-28 | PASS | STEP 1 pre-declares full skeleton including PHASE-N-COMMIT: [locked] markers; STEP 2 fills |
| C-30 | PASS | Every fill rule verb-first imperative; PRINT: PHASE-N-COMMIT: [locked] simultaneously satisfies C-30 and C-31 |
| C-31 | PASS | PHASE-N-COMMIT: [locked] in skeleton pre-declaration + ENFORCE: terminal position + PRINT: fill rule — lifecycle lock structurally guaranteed |

**V-05 score: 136/136** — All essential PASS.

---

### Ranking

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 (tie) | **V-01** | 136/136 | — |
| 1 (tie) | **V-05** | 136/136 | — |
| 3 (tie) | V-02 | 134/136 | C-28 |
| 3 (tie) | V-04 | 134/136 | C-28 |
| 5 | V-03 | 133/136 | C-28, C-30 partial |

---

### Excellence Signals (from top-scoring variations)

**1. PHASE-N-COMMIT: fill rule serves C-30 and C-31 simultaneously**
Both V-01 and V-05 structure the commit marker as an imperative PRINT: command that produces a structural lock. The same token (`PRINT: PHASE-N-COMMIT: [locked] — ...`) satisfies the verb-first imperative register (C-30) and the terminal structural lock (C-31) through one mechanism — no separate enforcement step needed.

**2. Commit-marker enumeration as citation-anchor manifest (V-04)**
V-04 introduced PHASE-1-COMMIT: enumerating locked INERTIA-FINDING tokens by name: `INERTIA-FINDING-A: [3-word token], ..., INERTIA-FINDING-D: [3-word token]`. The commit marker becomes a citation-anchor manifest — the investigation output is not merely implied by GATE: YES but explicitly locked in the commit. V-04's Phase 3 commit then references which labels were cited: `Tier 3 cited: [list INERTIA-FINDING labels]`, creating a fully traceable chain: finding → Phase 1 commit → voice citation → Phase 3 commit reference. V-05 should absorb this pattern.

**3. Skeleton-side pre-declaration of PHASE-N-COMMIT: markers closes the retroactive-softening gap structurally**
C-31's goal is to make retroactive Phase N modification architecturally impossible. The key mechanism: PHASE-N-COMMIT: appears in the STEP 1 skeleton, not only as a STEP 2 fill-rule output. Because the skeleton commits the slot before any content is generated, the commit marker cannot be omitted under content pressure — an empty container cannot be forgotten, whereas a dynamically generated marker can be skipped. This is C-28's structural guarantee applied specifically to the lifecycle boundary.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["PHASE-N-COMMIT: fill rule serves C-30 and C-31 simultaneously — a single PRINT: imperative produces the structural lock, no separate enforcement step needed", "Commit-marker-as-citation-anchor-manifest: PHASE-1-COMMIT: enumerates locked INERTIA-FINDING tokens by name; Phase 3 commit references which labels were cited, creating a fully traceable finding-to-commit-to-voice-to-commit chain"]}
```
