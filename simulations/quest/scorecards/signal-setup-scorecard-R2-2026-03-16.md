Now I have everything. Let me score all five variations.

---

# Quest Scorecard — signal-setup (Round 2)

**Rubric**: v2 (12 criteria: 5 essential, 3 recommended, 4 aspirational)
**Denominator update**: Aspirational 4 criteria (C-09 through C-12)
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/4 * 10)`
**Golden threshold**: All 5 essential pass AND composite ≥ 80

---

## Criterion-by-Criterion Evaluation

### C-01 — File detection before write

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 1 reads both files, outputs Detection Report before any other gate runs. |
| V-02 | PASS | Step 1 reads both files and produces scan table before path selection. |
| V-03 | PASS | Step 1 checks both files and announces findings before any preview or write. |
| V-04 | PASS | Role 1 (DETECTOR) reads both files, outputs Detection Report, hands off to Role 2. Nothing else. |
| V-05 | PASS | Pre-flight Gates A/B check CLAUDE.md; Phase 1 confirms copilot file state — all before Phase 4 (Write). |

---

### C-02 — Preview shown before writing

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 3 (PREVIEW) labeled "this is exactly what will be written." Precedes Gate 5 (WRITE). |
| V-02 | PASS | Step 3 labeled "PREVIEW:" in a code block. Precedes Step 5. |
| V-03 | PASS | Step 2: "Here's exactly what I'll add" — framed as preview, not yet written. |
| V-04 | PASS | Role 2 shows "PREVIEW — exact content to be written" before confirmation, before hand-off to Role 3. |
| V-05 | PASS | Phase 2 labeled "PREVIEW — this is exactly what gets written." Precedes Phase 3 (Confirm) and Phase 4 (Write). |

---

### C-03 — Confirmation required

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 4 asks explicit yes/no. "Wait for explicit responses." If no: "No changes made." Stop. |
| V-02 | PASS | Step 4 pending-actions table + explicit ask. "Do not write until answers received." |
| V-03 | PASS | Step 3: "Don't write a thing yet. Ask: 'Should I add this to CLAUDE.md? (yes / no)'" |
| V-04 | PASS | Role 2: "If CLAUDE.md is declined: output 'No changes made.' Stop." Never hands off to Role 3 without confirmation. |
| V-05 | PASS | Phase 3: "Do not write until confirmed." Includes no-path with "Signal not configured. Inertia remains unaddressed." |

---

### C-04 — Signal section appended with skill advertising

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Preview lists all 9 namespaces with sub-skills enumerated for each. |
| V-02 | PASS | Preview uses a full table: namespace column, sub-skills column for all 9 namespaces. |
| V-03 | PASS | Preview lists all 9 `/signal-*` skills with description + sub-skill list. |
| V-04 | PASS | Preview lists all 9 namespaces with sub-skills in dash-list format. |
| V-05 | PASS | Preview uses namespace-grouped format with explicit sub-skill listings. Inertia Rule prominently labeled as core principle. |

---

### C-05 — Idempotent re-run

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 2A trigger: "CLAUDE.md exists AND contains a Signal section." Output + "Stop. Do not proceed to any further gate." |
| V-02 | PASS | Step 2 path table: "CLAUDE.md has Signal section → SKIP — already configured." With explicit stop. |
| V-03 | PASS | Step 1: "If CLAUDE.md already has a Signal section, stop here: 'Signal is already set up... I'll leave it as-is.'" |
| V-04 | PASS | Role 2, Case A: "Stop. Do not hand off to Role 3." |
| V-05 | PASS | Pre-flight Gate A: checks for existing Signal section first. "Skill ends here. The happy path does not run." |

---

### C-06 — Inertia rule included

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Preview content: "Inertia Rule:" paragraph with full explanation. |
| V-02 | PASS | Preview includes "Inertia Rule:" paragraph with two-sentence elaboration. |
| V-03 | PASS | Preview: "The inertia rule:" paragraph, prominently included. |
| V-04 | PASS | Preview: "Inertia Rule:" paragraph. |
| V-05 | PASS | Leads the entire skill with a three-paragraph inertia framing before any instructions. Preview designates it "The Inertia Rule (core principle):" as a labeled section. Strongest C-06 across all variants. |

---

### C-07 — Copilot instructions offered

All five variations: **PASS**. Every variant checks for `.github/copilot-instructions.md` in the detection step and offers to update it in the confirmation step if found without an existing Signal section.

---

### C-08 — User feedback on outcome

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 5 outputs "SETUP COMPLETE" report with per-file status lines and next step. |
| V-02 | PASS | Step 5 outputs a results table (file, action, outcome) + "Signal setup complete." |
| V-03 | PASS | Step 4 lists what was done per file, ends with "You're set. Run /signal-topic new." |
| V-04 | PASS | Role 3 (WRITER) outputs "SETUP COMPLETE" report with per-file status and activation message. |
| V-05 | PASS | Phase 5: itemized Written/Skipped list + activation message with inertia framing. |

---

### C-09 — Preview matches written output

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 5: "Write the content from Gate 3 **exactly as previewed — no modifications**." |
| V-02 | PASS | Step 5: "Write the previewed content **without modification**." |
| V-03 | PASS | Step 4: "Append (or create) the file with the same content from Step 2. Don't change a word." |
| V-04 | PASS | Role 3 rules: "Write the previewed content byte-for-byte. No rewording. No additions." Role 2 explicitly passes "the exact preview text" in the hand-off. |
| V-05 | PASS | Phase 4: "Write the previewed content exactly — no changes, no additions." |

---

### C-10 — Handles missing CLAUDE.md gracefully

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 2B (named gate): announces "Signal will create one containing only the Signal section." Sets CREATE mode. Continues to Gate 3. |
| V-02 | PASS | Step 2 path table includes CREATE row: "CLAUDE.md does not exist → CREATE — new file." Handled explicitly. |
| V-03 | PASS | Step 2 footnote: "Since there's no CLAUDE.md yet, I'll create one with just this section in it." Step 4 "Append (or create)." |
| V-04 | PASS | Role 2, Case B: dedicated labeled section. "'No CLAUDE.md found. Signal will create a new one...'" |
| V-05 | PASS | Pre-flight Gate B: dedicated named gate. Sets CREATE mode. Continues to happy path. |

---

### C-11 — Named gate checkpoints as explicit phase boundaries

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | GATE 1, 2A, 2B, 3, 4, 5 — numbered, named, with "each gate must complete before the next begins" and "edge-case gate exits the skill entirely." Trigger conditions stated per gate. |
| V-02 | PARTIAL | Step 1–5 are numbered and labeled but lack formal gate language or explicit trigger conditions per step. The SKIP path exits in Step 2 with stop language, but no "must complete before next begins" instruction. |
| V-03 | PARTIAL | Bold "Step N—Label" headers provide named phases. "Don't write a thing yet" enforces ordering within steps, but no formal gate mechanism, no trigger conditions, no "must complete before" language. |
| V-04 | PASS | Three single-responsibility roles (DETECTOR, PLANNER, WRITER) with named hand-offs. Role constraint: "does not read ahead or act outside its scope." Phase boundaries enforced by design — a role structurally cannot skip. |
| V-05 | PASS | PRE-FLIGHT GATE A/B + PHASE 1–5, all named and labeled. Pre-flight section explicitly scoped: "if either triggers, the skill ends at that gate." Phased structure makes implicit skipping impossible. |

---

### C-12 — Edge-case paths promoted to first-class gates

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Gate 2A (already configured) and Gate 2B (missing CLAUDE.md) are peer-level gates alongside 1, 3, 4, 5. Each has its own dedicated section with trigger condition and complete treatment. Gate 2A exits; Gate 2B modifies write mode. Neither is a conditional inside the happy path. |
| V-02 | PARTIAL | Both cases appear in Step 2's path determination table — same step, sharing a container with the happy path case. Closer to a decision matrix than first-class gates. No dedicated named section per edge case. |
| V-03 | FAIL | "Already configured" is an inline conditional at the end of Step 1. "Missing CLAUDE.md" is a footnote in Steps 2 and 4. Neither is a named, dedicated section with its own complete treatment. |
| V-04 | PASS | Role 2 has Case A (already configured), Case B (missing CLAUDE.md), Case C (normal path) — each a labeled, dedicated sub-section with complete explicit treatment. Case A terminates execution. Case B modifies the operation. Not inline conditionals. |
| V-05 | PASS | Architecturally strongest C-12 implementation: pre-flight gates run in a structurally separate zone that precedes the happy path entirely. "The following gates run first. If either triggers, the skill ends at that gate." Edge cases and happy path are distinct structural zones. |

---

## Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-02 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-03 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-04 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-05 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-06 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-07 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-10 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 | ✓ | ~0.5 | ~0.5 | ✓ | ✓ |
| C-12 | ✓ | ~0.5 | ✗ | ✓ | ✓ |

| Metric | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| Essential pass | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Essential pts | 60 | 60 | 60 | 60 | 60 |
| Recommended pass | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Recommended pts | 30 | 30 | 30 | 30 | 30 |
| Aspirational pts | 10.0 | 7.5 | 6.25 | 10.0 | 10.0 |
| **Composite** | **100** | **97.5** | **96.25** | **100** | **100** |
| All essential pass | YES | YES | YES | YES | YES |
| **Band** | **Golden** | **Golden** | **Golden** | **Golden** | **Golden** |

---

## Ranking

| Rank | Variation | Score | Distinguishing Strength |
|------|-----------|-------|------------------------|
| 1 (tied) | V-01 | 100 | Purest gate model — numbered gates with explicit trigger conditions, peer-level edge case gates |
| 1 (tied) | V-04 | 100 | Role isolation — DETECTOR/PLANNER/WRITER enforces phase separation by design, not by instruction |
| 1 (tied) | V-05 | 100 | Strongest C-12 + C-06 — pre-flight zone as architectural separation; inertia framing as design preamble |
| 4 | V-02 | 97.5 | Table-driven format — excellent scanability, partial C-11/C-12 due to shared container for edge cases |
| 5 | V-03 | 96.25 | Warmest UX — best C-03 feel, but edge cases are inline conditionals (C-12 FAIL) |

All five variations achieve **Golden** status. V-02 and V-03 fall short on the new aspirational criteria (C-11, C-12) that targeted structural enforcement.

---

## Excellence Signals

Patterns from the top-scoring variations (V-01, V-04, V-05) that made them better:

**1. Structural zone separation for pre-flight (V-05 originates)**
V-05 places edge cases in a named "pre-flight" zone that runs *before* the happy path section begins. This isn't merely naming edge cases as gates — it's an architectural division: the happy path cannot start until pre-flight clears. This is stronger than numbered gates for edge cases because the zone separation is self-enforcing by document structure.

**2. Inertia-as-preamble: why before what (V-05 originates)**
Leading with the design philosophy (why Signal exists, what inertia means) before the installation mechanics changes the semantic weight of the confirmation step. In V-03 and V-02, confirmation is "is this OK?" — in V-05, it becomes "do you want to activate the inertia rule?" The framing primes the user to understand the value of the action they're confirming.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-flight zone separation: edge cases as a structurally distinct zone that runs before the happy path begins, not gates numbered alongside it", "inertia-as-preamble: leading with design philosophy before mechanics primes confirmation to carry semantic weight beyond mechanical approval"]}
```
