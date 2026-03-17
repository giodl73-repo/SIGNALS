---

# scout-inertia — Prompt Variations R2

Written to `simulations/quest/golden/scout-inertia-variate-R2-2026-03-17.md`.

---

## Variation Map

| ID | Axis | New Target |
|----|------|------------|
| V-01 | Replication Fidelity Standard on workaround section | C-13 |
| V-02 | "Verification Command" column with explicit format constraint | C-11 |
| V-03 | STRONGEST CLAIM / NAMED CLAIM extraction + copy-before-rebut | C-12 |
| V-04 | Combined: Verification Command + anchored rebuttal in phase structure | C-11 + C-12 |
| V-05 | R1 V-05 scaffold + all three new mechanisms | C-11 + C-12 + C-13 |

---

## Design decisions

**V-01, V-02, V-03 are strict single-axis.** Each is the closest R1 variation with exactly one structural change. This isolates which mechanism is responsible if a criterion passes or fails — no ambiguity about whether two things interacted.

**The key R1 gap for all three criteria was naming vs. format.** R1 variations *named* what was needed (e.g., "Verifiable How", "specific enough to follow") but left the format to the model. R2 replaces naming with format constraints:
- C-11: Column renamed to "Verification Command" + `[Tool]: [Action] → [Result]` format required, with passing and failing examples
- C-12: STRONGEST CLAIM label in Role 1 forces a named sentence; NAMED CLAIM verbatim copy in Role 2 makes non-traceability structurally impossible
- C-13: Three-item checklist (product names, numbered steps, flagged institutional knowledge) converts "specific enough to follow" from an adjective into a checklist

**V-05 predicts 100/100 on v2.** The three mechanisms slot directly into the sections of the R1 V-05 scaffold that already covered the adjacent criteria (C-01, C-07, C-10), so no existing pass degrades.
