## crew-check — Quest Scorecard R3

---

### Evaluation

#### V-01 — Readiness-gate framing (C-14)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Role source traceability | 12 | Gate 1 reads `.craft/roles/` exclusively; "Do not add roles not present in that directory"; ERROR+halt if absent |
| C-02 | Review matrix structure | 12 | Gate 5: 4-column matrix, all rows required |
| C-03 | Perspective fidelity | 12 | Gate 4 sub-gate: lens quote mandatory before writing finding; "A review without a lens anchor is not a review" |
| C-04 | Depth mode compliance | 12 | Gate 3 distinguishes standard (2–4 roles) and `--depth deep` (all roles); challenger always included |
| C-05 | Severity presence | 12 | Gate 2 locks HIGH/MEDIUM/LOW; "If a row would produce any other value, you are not ready to stage that row" |
| C-06 | Finding specificity | 10 | Step 2: "Name the specific artifact surface... section heading, field name, stated assumption, diagram element. You are not ready to assign severity until a specific surface is named." |
| C-07 | Recommendation actionability | 10 | Step 4: "One concrete action — what to do and where in the artifact. You are not ready to stage the row until the recommendation names a location." |
| C-08 | Severity calibration consistency | 10 | Gate 2 locked; readiness framing prevents staging invalid-severity rows |
| C-09 | Cross-role synthesis | 2 | Gate 6: convergence + conflict; "No cross-role signal detected" fallback |
| C-10 | AMEND responsiveness | 2 | AMEND block: add, deep, rerun, reload |
| C-11 | Lens-anchoring step | 2 | Gate 4 sub-gate explicit; strongest prose: "it is generic observation that does not reflect the role's documented perspective" |
| C-12 | Severity calibration contract | 2 | Gate 2 written and locked before any reviewer runs |
| C-13 | Challenger-first sequencing | 2 | "Process roles in order: challenger archetype roles first, then others" |
| C-14 | Readiness-gate framing | 2 | Primary axis; every gate header uses "You are not ready to advance past any gate until its condition is fully met" as universal idiom |
| C-15 | Severity-sorted matrix output | 0 | Gate 5: "Rows appear in execution order" — no severity sort |
| C-16 | Hard-halt execution gate | 1 | G1 error+halt present; per-reviewer gates use "you are not ready" / "revise until" but no formal halt registry or named per-gate messages |

**V-01 total: 103 / 106** | Composite: 97.2% | All essential: PASS

---

#### V-02 — Hard-halt execution gate (C-16)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Role source traceability | 12 | Step 1: `.craft/roles/` only; HALT [G1] if absent/empty |
| C-02 | Review matrix structure | 12 | Step 5: 4-column matrix; challenger rows first |
| C-03 | Perspective fidelity | 12 | Step 4a: lens anchor with HALT [G4-{role}] lens message if absent; "Finding blocked until lens is quoted" |
| C-04 | Depth mode compliance | 12 | Step 3: standard vs `--depth deep`; challenger always included |
| C-05 | Severity presence | 12 | Step 2: contract locked; HALT [G4-{role}] severity on invalid value |
| C-06 | Finding specificity | 10 | Step 4b: "Name the specific artifact surface... Name required. If no specific surface can be named, note the gap inline" |
| C-07 | Recommendation actionability | 10 | Step 4d: "what to do and where in the artifact"; HALT [G4-{role}] location if missing |
| C-08 | Severity calibration consistency | 10 | Halt mechanism enforces valid labels at row-stage time |
| C-09 | Cross-role synthesis | 2 | Step 6: convergence + conflict; fallback present |
| C-10 | AMEND responsiveness | 2 | AMEND adds `--amend halts` (lists every gate that fired) — strongest C-10 in R3 |
| C-11 | Lens-anchoring step | 2 | Step 4a with HALT enforcement |
| C-12 | Severity calibration contract | 2 | Step 2 locked before any reviewer runs |
| C-13 | Challenger-first sequencing | 2 | "challenger archetype first, then others alphabetically" |
| C-14 | Readiness-gate framing | 1 | Gate headers use imperative steps ("Before running any reviewer, lock..."); halt messages use "blocked until" / "cannot be staged" language but no "you are not ready" idiom in transition gates |
| C-15 | Severity-sorted matrix output | 0 | No severity sort; "challenger first, then domain roles" only |
| C-16 | Hard-halt execution gate | 2 | Named halt registry for G1, G4-lens, G4-severity, G4-location, G5-empty; "Any condition not listed here does not trigger a halt" — explicit scope boundary |

**V-02 total: 103 / 106** | Composite: 97.2% | All essential: PASS

---

#### V-03 — Interrogative/diagnostic phrasing (softer C-14 + C-16)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Role source traceability | 12 | Stage 1 Q1–Q3: existence check + "pool is exactly what the directory contains, nothing more"; ERROR+stop if absent |
| C-02 | Review matrix structure | 12 | Stage 5: 4-column matrix |
| C-03 | Perspective fidelity | 12 | Q1: "What does this role actually care about? Quote or paraphrase one line from their orientation.frame or lens.verify." — diagnostic framing may elicit more genuine lens engagement |
| C-04 | Depth mode compliance | 12 | Stage 2 Q1: `--depth deep` branch; challenger auto-included per Q3 |
| C-05 | Severity presence | 12 | Stage 3 contract with explicit "Are these the only valid severity values? Answer: Yes." |
| C-06 | Finding specificity | 10 | Q2: "Which section heading, field, assumption, or diagram element are you pointing at? If you cannot name a specific surface, the finding is not ready — revisit Q1." |
| C-07 | Recommendation actionability | 10 | Q4: "Concrete action with a location. Not a directive. 'Address this concern' is not an answer." |
| C-08 | Severity calibration consistency | 10 | Stage 3 contract; "Any other label is not a valid answer — pick again." |
| C-09 | Cross-role synthesis | 2 | Stage 6 with convergence + conflict questions |
| C-10 | AMEND responsiveness | 2 | AMEND adds `--amend rerun:severity` for Stage 3 re-entry |
| C-11 | Lens-anchoring step | 2 | Q1 is the lens anchor question; enforced by "if you cannot quote or paraphrase, you are not ready to write the finding" |
| C-12 | Severity calibration contract | 2 | Stage 3 precedes all reviewers |
| C-13 | Challenger-first sequencing | 2 | Stage 4: "challenger archetype roles first"; Stage 5: "challenger rows first (from Q5 findings)" |
| C-14 | Readiness-gate framing | 1 | Q1: "not ready to write the finding"; Q2: "finding is not ready — revisit Q1" — readiness language present but localised to Q1/Q2, not universal idiom across stage transitions |
| C-15 | Severity-sorted matrix output | 0 | Stage 5: "challenger rows first, then domain rows" — no severity descending sort |
| C-16 | Hard-halt execution gate | 0 | Stage 1 ERROR+stop on missing registry; per-reviewer gates use diagnostic questions with "revisit Q1" — no named halt registry, no explicit halt messages for G4 conditions; design intent states "softer gates, no formal halt messages" |

**V-03 total: 101 / 106** | Composite: 95.3% | All essential: PASS

---

#### V-04 — Readiness-gate + Hard-halt (C-14 + C-16)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Role source traceability | 12 | Gate 1: `.craft/roles/` only; HALT [G1] named in registry; "zero invented roles" |
| C-02 | Review matrix structure | 12 | Gate 5: 4-column matrix; no blank cells |
| C-03 | Perspective fidelity | 12 | Sub-gate G4a: "You are not ready to write the finding until the lens is quoted"; HALT [G4-{role}] lens on failure |
| C-04 | Depth mode compliance | 12 | Gate 3: standard vs `--depth deep`; challenger always included |
| C-05 | Severity presence | 12 | Gate 2: locked scale with numeric sort scores; HALT [G4-{role}] severity on invalid value |
| C-06 | Finding specificity | 10 | Sub-gate G4b: "Name the section, field, assumption, or diagram element the finding references." |
| C-07 | Recommendation actionability | 10 | Sub-gate G4d: "what to do and where"; HALT [G4-{role}] location on failure |
| C-08 | Severity calibration consistency | 10 | Gate 2 locked; halt at G4c prevents invalid rows staging |
| C-09 | Cross-role synthesis | 2 | Gate 6: convergence + conflict; fallback present |
| C-10 | AMEND responsiveness | 2 | AMEND: add, deep, rerun, reload, halts, unsorted |
| C-11 | Lens-anchoring step | 2 | Sub-gate G4a with readiness assertion and HALT |
| C-12 | Severity calibration contract | 2 | Gate 2 locked before any reviewer runs |
| C-13 | Challenger-first sequencing | 2 | Gate 4: "challenger archetype first, then others alphabetically"; matrix sort: challengers before domain within each tier |
| C-14 | Readiness-gate framing | 2 | Intro declares the property: "Prerequisites are gates, not guidelines"; every gate header uses "You are not ready to advance past any gate until its condition is fully met"; sub-gate labels reinforce per-reviewer |
| C-15 | Severity-sorted matrix output | 2 | Intro: "produce a severity-sorted review matrix"; Gate 5: "Sort rows by severity score descending (HIGH first, then MEDIUM, then LOW). Within each tier: challenger rows before domain rows." Numeric scores (3/2/1) encode sort key in Gate 2. |
| C-16 | Hard-halt execution gate | 2 | Named halt registry for G1, G4-lens, G4-severity, G4-location; intro: "No partial output. No silent skips. Revise and re-enter." Combined with readiness framing. |

**V-04 total: 106 / 106** | Composite: 100% | All essential: PASS

---

#### V-05 — Readiness-gate + Hard-halt + Severity-sorted (C-14 + C-16 + C-15)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Role source traceability | 12 | GATE 1: `.craft/roles/` only; HALT [G1]; zero invented roles |
| C-02 | Review matrix structure | 12 | GATE 5: 4-column matrix; sorted; no blank cells |
| C-03 | Perspective fidelity | 12 | G4a: readiness condition labeled inline "(readiness condition: not ready for the finding)"; HALT [G4-{role}] lens on failure |
| C-04 | Depth mode compliance | 12 | GATE 3: standard vs `--depth deep`; challenger always included |
| C-05 | Severity presence | 12 | GATE 2: scale locked; numeric scores for sort; HALT on invalid |
| C-06 | Finding specificity | 10 | G4b: "Name the specific artifact surface this lens flags: section, field, assumption, diagram element." |
| C-07 | Recommendation actionability | 10 | G4d: "what to do AND where"; HALT [G4-{role}] location on failure |
| C-08 | Severity calibration consistency | 10 | GATE 2 + halt enforcement + sort failure as calibration signal |
| C-09 | Cross-role synthesis | 2 | Cross-role synthesis block: convergence + conflict + fallback |
| C-10 | AMEND responsiveness | 2 | AMEND: add, deep, rerun, reload, unsorted, halts |
| C-11 | Lens-anchoring step | 2 | G4a with readiness label and HALT |
| C-12 | Severity calibration contract | 2 | GATE 2 locked before any reviewer |
| C-13 | Challenger-first sequencing | 2 | GATE 4: challenger first; GATE 5 sort: "challengers before domain within each tier" |
| C-14 | Readiness-gate framing | 2 | Intro enumerates the three structural properties; all GATE headers use "You are not ready…" idiom; sub-gate labels use inline readiness condition text |
| C-15 | Severity-sorted matrix output | 2 | GATE 5 sort step with its own HALT [G5]: "Matrix sort failed — severity values inconsistent. Resolve before rendering." Sort is load-bearing, not cosmetic. |
| C-16 | Hard-halt execution gate | 2 | Named halt registry for G1, G4-lens, G4-severity, G4-location, G5-sort; intro: "No partial output. No silent skips. The failure is visible and addressable." |

**V-05 total: 106 / 106** | Composite: 100% | All essential: PASS

---

### Score Summary

| Variation | C-14 | C-15 | C-16 | Total | Composite | Rank |
|-----------|------|------|------|-------|-----------|------|
| V-04 | 2 | 2 | 2 | **106** | 100% | 1 (tie) |
| V-05 | 2 | 2 | 2 | **106** | 100% | 1 (tie) |
| V-01 | 2 | 0 | 1 | **103** | 97.2% | 3 (tie) |
| V-02 | 1 | 0 | 2 | **103** | 97.2% | 3 (tie) |
| V-03 | 1 | 0 | 0 | **101** | 95.3% | 5 |

All five variations pass all five essential criteria. Golden threshold met by all variations (all essential PASS + composite >= 80).

---

### Excellence Signals (V-04 and V-05)

**1. Combination is stronger than either property alone.**
V-01 (readiness only) and V-02 (halt only) both score 103. V-04 and V-05 combine both and reach 106. The two mechanisms are not additive by coincidence — readiness framing changes the internal state question from "did I follow the rule?" to "am I in the right state?", while hard halts make failure visible and named. Neither property fully substitutes for the other.

**2. Numeric sort keys belong in the severity contract, not the sort step.**
V-04 and V-05 define HIGH=3, MEDIUM=2, LOW=1 in Gate 2 (the severity contract), not in Gate 5. This means the sort key is locked at the same time severity meaning is locked — they are one artifact, not two separate definitions. This prevents a class of inconsistency where the contract and the sort key diverge.

**3. Sort halt as calibration signal (V-05 exclusively).**
V-05 adds HALT [G5]: "Matrix sort failed — severity values inconsistent." This makes the sort step a calibration check, not just an ordering operation. A matrix that cannot be sorted consistently has inconsistent severity labels; the sort failure surfaces that before render. This is categorically different from C-15 (sort present) — it is C-15 made load-bearing.

**4. Priority summary tier between matrix and synthesis (V-05).**
V-05 inserts GATE 6 as a per-severity-tier count (`HIGH: N finding(s)`, `MEDIUM: N`, `LOW: N`) before the cross-role synthesis. This produces a scannable triage view and makes the severity distribution explicit before the prose synthesis step.

**5. Inline readiness condition labels on sub-gates (V-05).**
V-05 labels each sub-gate with its readiness condition in parentheses: `G4a — Lens anchor (readiness condition: not ready for the finding)`. This makes the gate purpose scannable without reading the body — useful when the skill is long and the model is context-scanning rather than reading linearly.

---

### New Patterns for v4 Rubric Consideration

Two patterns in V-05 are not captured in C-01 through C-16:

| Pattern | Source | Evidence |
|---------|--------|----------|
| Sort-halt as calibration check | V-05 G5 | "Matrix sort failed — severity values inconsistent. Resolve before rendering." Sort failure = severity inconsistency = calibration failure surfaced at render time, not after |
| Priority summary tier | V-05 GATE 6 | Per-severity-tier count block (`HIGH: N / MEDIUM: N / LOW: N`) inserted between matrix and synthesis; makes triage explicit and gives the synthesis step quantified input |

---

```json
{"top_score": 106, "all_essential_pass": true, "new_patterns": ["sort-halt as calibration check: treating matrix sort failure as a severity-inconsistency signal rather than an ordering error, with a dedicated halt condition", "priority summary tier: per-severity-tier count block between matrix and synthesis that makes triage explicit before prose synthesis"]}
```
