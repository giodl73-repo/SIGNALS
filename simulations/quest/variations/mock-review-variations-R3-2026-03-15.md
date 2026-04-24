Written to `simulations/quest/golden/mock-review-variate-R3-2026-03-15.md`.

---

## Round 3 — What Was Built

**Gap analysis from R2:**

| Criterion | R2 coverage | Gap |
|-----------|-------------|-----|
| C-14 sub-question answer citation | V-04 instruction: "name the sub-question answer" | Instructional only — no output slot forces the model to produce the answer vs. restate the verdict |
| C-15 entity-naming sub-question grammar | V-03/V-04: naming follow-ups present but yes/no openers remain ("Are required sections present?") | Yes/no openers let the model skip the artifact-naming step |
| C-16 canary confirmation | V-02: MUST NOT prohibition present | Prohibition without named-error semantics — C-16 requires the false-positive condition to be a named protocol error |

**5 variations:**

| V | Axes | Target | Mechanism |
|---|------|--------|-----------|
| V-01 | phrasing-register | C-15 | All sub-questions rewritten as "Name X" / "What specific X" — yes/no opener clauses removed throughout |
| V-02 | lifecycle-emphasis | C-16 | Zero-remaining confirmation named as a CANARY OUTPUT; false-positive named CANARY-FALSE-POSITIVE; suppression protocol on failure |
| V-03 | output-format | C-14 | Pre-printed REAL-REQUIRED verdict template with a dedicated `Sub-question answer that drove this verdict:` slot |
| V-04 | phrasing-register + output-format | C-14 + C-15 | Entity-naming grammar produces artifact-specific answers; citation template routes them into the verdict — traceable chain forced structurally |
| V-05 | all three axes + R2 forbidden-output + step separation | C-11, C-13, C-14, C-15, C-16 | Ceiling: every criterion through a structural guarantee, not an instruction |

**Key design decisions:**
- V-01 is the purest C-15 test: the only change is grammar form. If yes/no openers were the actual gap (not sub-question presence), V-01 should show a clean C-15 improvement.
- V-02 distinguishes C-12 (required output) from C-16 (canary assertion with named failure mode). The CANARY-FALSE-POSITIVE name is the differentiator.
- V-03's citation slot includes a constraint in the label itself: "name the specific section, element, gap, or decision; not a restatement of the verdict" — anticipating the failure mode where the slot is filled syntactically but semantically empty.
