Written to `simulations/quest/golden/quest-variate-mock-ns-R2-2026-03-15.md`.

---

## Round 2 — mock-ns Variations

### Axis Assignment

| V | Axes | Target criteria | Predicted outcome |
|---|------|-----------------|-------------------|
| **V-01** | lifecycle-emphasis | **C-11** | FLAG resolved to named variable in S-4, emitted before header; header copies it verbatim — flag can't drift into inline computation |
| **V-02** | output-format | **C-13** | `## FIDELITY CONTEXT` is Section 2 of the artifact, flanked by `---` delimiters, before any mock body — warning is structural, not positional |
| **V-03** | phrasing-register | **C-12** | Default skill table gains an inline `Exclusion` column; the topic row reads "Do NOT use topic-status" in the same cell as the affirmative default |
| **V-04** | lifecycle-emphasis + output-format | **C-11 + C-13** | V-01 named FLAG computation + V-02 FIDELITY CONTEXT section; two changes operate at different procedure points without interfering |
| **V-05** | phrasing-register + inertia-framing | **C-12 + C-07** | V-03 inline exclusion with inertia-cost explanation ("zero new signal, defeats purpose") + per-category inertia risk language in warnings; prevents HIGH-STRUCTURE warning truncation |

### Key innovations over Round 1

**C-11:** R1 V-03 had "Write it now. Do not defer it." but the flag was still resolved inline during header construction. V-01 and V-04 introduce `FLAG = {value}` as an emitted named variable in a step that must complete before the header step — the header is explicitly told to "copy FLAG from S-4 verbatim."

**C-12:** R1 carried the exclusion as a note below the table (V-01) or a separate line after (V-03). V-03 and V-05 move it into the table as a third column — same visual register as the affirmative default, impossible to skip on a scan.

**C-13:** R1 V-04 came closest with `---`-delimited warnings. V-02 and V-04 elevate this to a named section (`## FIDELITY CONTEXT`) — a structural property of the artifact, not just positioning guidance.

**Round 3 candidate:** V-01 + V-02 + V-03 as a three-axis combination, pending independent pass confirmation on each single-axis variation.
