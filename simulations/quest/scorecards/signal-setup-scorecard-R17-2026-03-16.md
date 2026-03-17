# Quest Score — signal-setup Round 17 (v15 rubric)

## Scoring Reference

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/38 × 10)`
**Denominator**: A=38 (5 essential + 3 recommended + 30 aspirational C-09–C-38)
**Golden threshold**: all 5 essential PASS AND composite ≥ 80

---

## Essential Criteria (C-01–C-05) — All Variations

All five variations share the same gate structure for the primary flow and earn 5/5 on essential criteria.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | File detection before write | PASS | PASS | PASS | PASS | PASS |
| C-02 | Preview shown before writing | PASS | PASS | PASS | PASS | PASS |
| C-03 | Confirmation required | PASS | PASS | PASS | PASS | PASS |
| C-04 | Signal section with skill advertising | PASS | PASS | PASS | PASS | PASS |
| C-05 | Idempotent re-run | PASS | PASS | PASS | PASS | PASS |

**Essential score: 5/5 all variations → 60 pts**

---

## Recommended Criteria (C-06–C-08) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Inertia rule included in appended content | PASS | PASS | PASS | PASS | PASS |
| C-07 | Copilot instructions offered | PASS | PASS | PASS | PASS | PASS |
| C-08 | User feedback on outcome | PASS | PASS | PASS | PASS | PASS |

**Recommended score: 3/3 all variations → 30 pts**

---

## Aspirational Criteria (C-09–C-38) — Per Variation

### V-01 — Dominance-verb preamble (C-36 axis)

Evidence notes for each criterion:

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | GATE 5: "exactly as shown in GATE 3" |
| C-10 | PASS | GATE 1A creates file or offers creation |
| C-11 | PASS | All five phases (detect/preview/confirm/write/report) are numbered heading gates |
| C-12 | PASS | GATE 1A (missing file), GATE 2A (already configured) are `####` headings |
| C-13 | PASS | "Inertia wins the default choice... Signal names the force that holds that line and writes a question into Claude's context to contest it" — motivates WHY setup matters |
| C-14 | PASS | GATE 1B and GATE 4B both explicitly name consequence ("the question of why teams would do nothing never gets asked") |
| C-15 | PASS | GATE 2A: "Inertia already has a named opponent here" |
| C-16 | PASS | "Signal names the force that holds that line... to contest it" — inertia framed as force being opposed; GATE 2A reinforces: "named opponent" |
| C-17 | PASS | "Setup happens once; your CLAUDE.md loads it automatically every session, so the inertia question is present without you having to remember it" |
| C-18 | PASS | GATE 1B/4B: "never gets asked **before the feature direction is locked**" — future moment named |
| C-19 | PASS | GATE 1B and GATE 4B carry identical future-moment framing: "feature direction locked" anchor at both Signal-absent exits |
| C-20 | PASS | GATE 2A: "Your CLAUDE.md loads automatically every session — the inertia question is in Claude's context without you having to remember it. The configuration holds that position permanently." |
| C-21 | PASS | GATE 6B uses implementation-stage/Copilot vocabulary distinct from planning-stage/spec vocabulary at GATE 1B/4B |
| C-22 | PASS | GATE 1B/4B: "planning stage" + "feature direction locked"; GATE 6B: "implementation stage" + "build suggestion" + "Copilot" — non-overlapping phase vocabulary |
| C-23 | PASS | "Inertia wins **the planning stage**" (GATE 1B/4B) and "**At the implementation stage**" (GATE 6B) — explicit phase labels present |
| C-24 | PASS | GATE 6A-Found: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context — adoption assumptions surface during the build, not only at the planning stage" — Copilot-specific consequence |
| C-25 | PASS | GATE 1A/1B (parent=1), GATE 2A (parent=2), GATE 4A/4B (parent=4), GATE 6A/6B (parent=6), GATE 6A-Found/6A-Write (parent=6A) — all encode lineage |
| C-26 | PASS | GATE 6A (yes path) and GATE 6B (decline) are both `####` heading sub-gates |
| C-27 | PASS | All gate boundaries use `###`/`####` headings; no bold inline pseudo-gates |
| C-28 | PASS | File-existence detection inline with annotation: "(No sub-gate for file-existence — file creation is included in the confirmed write action when the file is missing; no separate confirmation point is required.)" |
| C-29 | PASS | All Route blocks: complete `(condition → GATE NX)` pairs with gate IDs at every branch (GATE 1A, 1B, 2A, 3, 4A, 4B, 5, 6A, 6B, 6A-Found, 6A-Write) |
| C-30 | PASS | File-existence inline in GATE 6A carries explicit rationale annotation; Signal-section content-detection promoted to sub-gates (no annotation needed) |
| C-31 | **FAIL** | GATE 1A/1B/2A/4A/4B/6A/6B use letter-slot; GATE 6A-Found and GATE 6A-Write use word-suffix — mixed convention throughout spec |
| C-32 | PASS | All consequence anchors are complete sentences with subject + predicate + stated outcome (e.g., "Inertia wins the planning stage: the spec gets committed without a Signal reminder in Claude's context, and the question... never gets asked before the feature direction is locked.") |
| C-33 | PASS | All three decline gates (GATE 1B, 4B, 6B) name inertia as the winning party |
| C-34 | PASS | All anchors express two steps: GATE 1B/4B: "spec committed → question never asked"; GATE 6B: "code generated without question → assumptions locked in" |
| C-35 | PASS | All Route blocks use "Route:" label with one `(condition → GATE)` entry per line |
| C-36 | **PASS** | "**Inertia wins** the default choice" and "**inertia collects** the outcome" — inertia is grammatical subject of active-victory verbs |
| C-37 | **FAIL** | No "choose a side" or equivalent explicit agency phrase anywhere in preamble; implied but not stated |
| C-38 | **PASS** | GATE 6B: "**inertia wins** the build suggestion **through Copilot**" — inertia is the winning force; Copilot is the channel |

**V-01 aspirational: 28/30 PASS** (fails C-31, C-37)
**V-01 score: 60 + 30 + (28/38 × 10) = 97.37**

---

### V-02 — Team-agency preamble (C-37 axis)

Changes from V-01: Preamble swaps dominance-verb construction for adversary + "choosing a side" language. Gate structure identical to V-01.

| ID | Result | Evidence |
|----|--------|----------|
| C-13 | PASS | "Inertia is the adversary every feature faces — the silent competitor that benefits when teams commit to a direction without asking why users would change their behavior. When you configure Signal, you are not just enabling a tool. **You are choosing a side.**" — motivational framing |
| C-16 | PASS | "Inertia is the adversary every feature faces — the silent competitor" — explicitly named as adversary and competitor |
| C-31 | **FAIL** | Same mixed letter-slot/word-suffix issue (GATE 6A-Found, GATE 6A-Write) |
| C-36 | **FAIL** | Preamble: "inertia is the adversary... benefits when..." — "benefits" is not an active-victory verb; inertia is never subject of "wins" or "collects the default"; "leave the field to inertia by default" has inertia as destination, not subject of victory clause |
| C-37 | **PASS** | "**You are choosing a side.**" — explicit text in preamble; GATE 2A echoes: "You chose a side" |
| C-38 | PASS | GATE 6B: "inertia wins the build suggestion through Copilot" (same as V-01) |

All other criteria: same PASS status as V-01 (identical gate structure).

**V-02 aspirational: 28/30 PASS** (fails C-31, C-36)
**V-02 score: 60 + 30 + (28/38 × 10) = 97.37**

---

### V-03 — Tool-specific force naming at GATE 6B only (C-38 axis, R16 V-01 base)

Base is R16 V-01 with intentionally weak preamble and inline bold labels for sub-paths.

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | GATE 5: "exactly as shown in GATE 3" |
| C-10 | PASS | GATE 1A creates file |
| C-11 | PASS | All phases have named gates |
| C-12 | PASS | GATE 1A and GATE 2A are `####` headings |
| C-13 | **FAIL** | "Signal helps teams gather evidence across 9 namespaces before committing to a feature. The inertia rule governs when a topic is ready." — informational, not motivational; does not frame WHY inertia mandates setup; "governs" is regulatory description |
| C-14 | PASS | GATE 1A Decline and GATE 4B name consequences |
| C-15 | PASS | GATE 2A affirms persistence |
| C-16 | **FAIL** | "The inertia rule governs when a topic is ready" — "governs" is a rule/principle framing, not adversary framing; no opponent or competitor language in preamble |
| C-17 | PASS | "so it is present in every session without anyone having to remember it" — persistence argument present |
| C-18 | PASS | GATE 1A Decline: "before the next feature commitment"; GATE 4B: "before the feature direction is locked" |
| C-19 | PASS | Both Signal-absent exits carry future-moment framing |
| C-20 | PASS | GATE 2A names CLAUDE.md auto-load mechanism |
| C-21 | PASS | GATE 6B uses implementation-stage/Copilot vocabulary |
| C-22 | PASS | Phase-indexed vocabulary: planning vs implementation |
| C-23 | PASS | "planning stage" and "At the implementation stage" explicit labels |
| C-24 | PASS | GATE 6A inline already-configured: "During implementation, Copilot has the inertia question in context when it suggests code" |
| C-25 | PASS | Letter-slot throughout (1A, 2A, 4A, 4B, 6A, 6B) — no word-suffix sub-sub-gates (content-detection paths are inline, not named sub-gates) |
| C-26 | PASS | GATE 6A and GATE 6B are `####` heading sub-gates |
| C-27 | **FAIL** | `**GATE 1A Decline:**` used as bold inline pseudo-gate delimiter inside GATE 1A body; `**Copilot already-configured message:**` and `**Copilot write result:**` are bold inline labels inside GATE 6A body — none are heading-level boundaries |
| C-28 | PASS | File-existence inline with rationale annotation present in GATE 6A |
| C-29 | **FAIL** | GATE 1A Route: `(no) → print decline message, exit` — action description, not a gate ID (no GATE 1B exists as heading); GATE 6A Route: `(Signal section already present) → print Copilot already-configured message, exit` — action description, not a gate ID |
| C-30 | **FAIL** | GATE 6A content-detection paths (already-configured vs write) are inline bold labels without annotation rationale (only file-existence gets annotation; Signal-section content-detection has no rationale comment) |
| C-31 | PASS | Uniform letter-slot throughout (no word-suffix sub-sub-gates promoted to headings) |
| C-32 | PASS | All consequence anchors are complete sentences |
| C-33 | PASS | GATE 1A Decline/4B/6B: all name inertia as winner |
| C-34 | PASS | Two-step chains at all decline gates |
| C-35 | PASS | All Route blocks use "Route:" label with one-per-line entries |
| C-36 | **FAIL** | "The inertia rule governs" — regulatory, not victorious; no dominance verb |
| C-37 | **FAIL** | No "choose a side" language |
| C-38 | **PASS** | GATE 6B: "inertia wins the build suggestion through Copilot" |

**V-03 aspirational: 23/30 PASS** (fails C-13, C-16, C-27, C-29, C-30, C-36, C-37)
**V-03 score: 60 + 30 + (23/38 × 10) = 96.05**

---

### V-04 — C-36 + C-37 preamble; GATE 6B intentionally retains "Copilot wins" (C-38 deliberately absent)

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | **FAIL** | Same mixed convention (6A-Found, 6A-Write word-suffix) |
| C-33 | **FAIL** | GATE 6B: "**Copilot** wins the build suggestion" — Copilot (a tool) is named as the winning party, not inertia (the adversary); fails at GATE 6B; C-38 failures propagate to C-33 per rubric |
| C-36 | PASS | "**Inertia wins** the default choice" + "**inertia collects** the default" |
| C-37 | PASS | "Teams that configure Signal **choose a side**: they appoint inertia as a named opponent in every session" |
| C-38 | **FAIL** | GATE 6B: "Copilot wins the build suggestion" — tool named as winner, not behavioral force (annotation present confirming deliberate design choice) |

All other criteria: same as V-05 (identical structure except GATE 6B and preamble from V-05). C-34 at GATE 6B: "code that assumes adoption gets written without the inertia question in context, and adoption assumptions get locked" — two-step chain is present, PASS.

**V-04 aspirational: 27/30 PASS** (fails C-31, C-33, C-38)
**V-04 score: 60 + 30 + (27/38 × 10) = 97.11**

---

### V-05 — Full synthesis (C-36 + C-37 + C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | GATE 5: "exactly as shown in GATE 3" |
| C-10 | PASS | GATE 1A creates file on yes |
| C-11 | PASS | All five phases as numbered heading gates |
| C-12 | PASS | GATE 1A and GATE 2A are first-class `####` headings |
| C-13 | PASS | "**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder to surface the adoption question — feature specs get committed without a challenge" — motivates setup in terms of inertia's effect |
| C-14 | PASS | GATE 1B/4B: "the question of why teams would do nothing never gets asked before the feature direction is locked" |
| C-15 | PASS | GATE 2A: "You chose a side — inertia already has a named opponent here" |
| C-16 | PASS | "inertia collects the default because no session named it as a competitor" — competitor framing; GATE 2A: "named opponent" |
| C-17 | PASS | "Setup happens once; your CLAUDE.md loads it automatically, so the choice holds without you having to repeat it" |
| C-18 | PASS | GATE 1B/4B: "**before the feature direction is locked**"; GATE 6B: "**before anyone asks whether they are warranted**" |
| C-19 | PASS | GATE 1B and GATE 4B carry identical future-moment framing ("feature direction locked") |
| C-20 | PASS | GATE 2A: "Your CLAUDE.md loads automatically every session, so the inertia question is in Claude's context without you having to remember it. The configuration holds that position permanently." |
| C-21 | PASS | GATE 6B: Copilot + implementation-stage-specific framing; GATE 1B/4B: planning-stage-specific framing |
| C-22 | PASS | "planning stage" + "feature direction locked" vs "implementation stage" + "build suggestion through Copilot" — non-overlapping vocabulary |
| C-23 | PASS | "Inertia wins **the planning stage**" (GATE 1B/4B); "**At the implementation stage**" (GATE 6B) |
| C-24 | PASS | GATE 6A-Found: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context — adoption assumptions surface during the build, not only at the planning stage." |
| C-25 | PASS | All sub-gates encode parent lineage: GATE 1A/1B (parent=1), GATE 2A (parent=2), GATE 4A/4B (parent=4), GATE 6A/6B (parent=6), GATE 6A-Found/6A-Write (parent=6A) |
| C-26 | PASS | GATE 6A (confirmation yes path) and GATE 6B (decline path) are both `####` headings |
| C-27 | PASS | All gate/sub-gate boundaries use `###`/`####` heading elements; no bold inline pseudo-gates anywhere |
| C-28 | PASS | File-existence detection in GATE 6A is inline with explicit rationale annotation; Signal-section content-detection is promoted to GATE 6A-Found/6A-Write (no annotation needed for promoted paths) |
| C-29 | PASS | All Route blocks enumerate complete `(condition → GATE ID)` pairs: GATE 1→1A/2; GATE 1A→GATE 3/1B; GATE 2→2A/3; GATE 4→4A/4B; GATE 6→6A/6B; GATE 6A internal→6A-Found/6A-Write |
| C-30 | PASS | Only inline detection path (file-existence in GATE 6A) carries explicit annotation; content-detection promoted to sub-gates — no unannotated inline detection paths |
| C-31 | **FAIL** | GATE 6A-Found and GATE 6A-Write use word-suffix identifier (`6A-Word`) while all first-level sub-gates use letter-slot (`1A`, `1B`, `2A`, `4A`, `4B`, `6A`, `6B`) — mixed conventions, fails uniformity requirement |
| C-32 | PASS | All consequence anchors are syntactically complete assertable propositions (subject + predicate + stated outcome) |
| C-33 | PASS | All three decline gates name inertia as winning party: GATE 1B ("Inertia wins the planning stage"), GATE 4B (same), GATE 6B ("inertia wins the build suggestion through Copilot") |
| C-34 | PASS | All anchors express two-step causal chain: GATE 1B/4B: "spec committed without competitor → question never asked"; GATE 6B: "code generated without question → adoption assumptions locked in" |
| C-35 | PASS | All Route blocks use "Route:" label with one entry per branch line |
| C-36 | **PASS** | "**Inertia wins** the default choice" (preamble opening) + "**inertia collects** the default because no session named it as a competitor" — inertia as grammatical subject of active-victory verbs |
| C-37 | **PASS** | "Teams that configure Signal **choose a side**: they write inertia a named opponent into every session, permanently" — explicit "choose a side" in text; echoed at GATE 2A: "You chose a side" |
| C-38 | **PASS** | GATE 6B: "**inertia wins** the build suggestion **through Copilot**: code that assumes adoption gets generated without the inertia question in context" — inertia is the winning force; Copilot is the channel |

**V-05 aspirational: 29/30 PASS** (fails C-31 only)
**V-05 score: 60 + 30 + (29/38 × 10) = 97.63**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| **V-05** | 5/5 | 3/3 | **29/30** | **97.63** | **#1** |
| V-01 | 5/5 | 3/3 | 28/30 | 97.37 | #2 (tied) |
| V-02 | 5/5 | 3/3 | 28/30 | 97.37 | #2 (tied) |
| V-04 | 5/5 | 3/3 | 27/30 | 97.11 | #4 |
| V-03 | 5/5 | 3/3 | 23/30 | 96.05 | #5 |

---

## Excellence Signals from V-05

**1. C-36 + C-37 stack without conflict in a single compact preamble.** The pattern is: sentence 1 establishes inertia's victory ("Inertia wins the default choice... inertia collects the default"), sentence 3 establishes team agency ("Teams that configure Signal choose a side"). The dominance-verb construction and the explicit-choice construction operate on independent grammatical subjects (inertia vs teams) so they can coexist without one displacing the other.

**2. C-38 is a pure gate-body fix — the preamble constructions are independent failure modes.** V-03 demonstrates C-38 can be fixed by a single targeted substitution at GATE 6B without touching the preamble. V-04 confirms the inverse: both preamble constructions can pass while GATE 6B still fails C-38. The criteria are genuinely independent; a spec writer can address each in isolation.

**3. Preamble agency echoes in GATE 2A.** V-05's already-configured path opens with "You chose a side" — threading the C-37 choice-language from the preamble into the positive-outcome affirmation. This is not required by any current criterion but creates rhetorical consistency: the user who configured Signal reads the confirmation that they did exactly what the preamble said mattered.

**4. C-31 is the universal structural ceiling for heading-promoted variants.** Every variation that promotes GATE 6A-Found and GATE 6A-Write to `####` headings (V-01/V-02/V-04/V-05) fails C-31 because word-suffix identifiers (`6A-Found`, `6A-Write`) coexist with letter-slot identifiers (`1A`, `1B`, `6A`, `6B`). V-03 passes C-31 by keeping content-detection inline, but trades that for C-27, C-29, and C-30 failures. The two conventions are in tension: heading-promotion satisfies structural navigability (C-27, C-29) but breaks identifier uniformity (C-31); inline treatment preserves identifier uniformity but requires bold pseudo-gates that violate C-27. No variation resolves this simultaneously. The fix is a third-level identifier convention consistent with letter-slot (e.g., `GATE 6AA`/`GATE 6AB`) that extends the existing scheme rather than switching to word-suffix.

---

```json
{"top_score": 97.63, "all_essential_pass": true, "new_patterns": ["C-31 is the universal structural ceiling for heading-promoted variations — word-suffix sub-sub-gate identifiers (6A-Found, 6A-Write) conflict with letter-slot first-level sub-gates (1A, 1B, 6A, 6B); the fix requires extending the letter-slot scheme to a third level (e.g., GATE 6AA, GATE 6AB) rather than switching conventions mid-spec", "Preamble agency language has a natural echo point at GATE 2A — 'You chose a side' threads C-37's explicit-choice construction from the opening framing into the already-configured affirmation, creating semantic consistency across all positive outcome states without requiring a new criterion"]}
```
