---

# Variations: `topic:status` — Round 8
**Rubric:** v8 (max 210) | Written to:** `simulations/quest/rubrics/topic-status-rubric-v8-variations-R8-2026-03-14.md`

---

## Design Context

R7 V-02 scored **195/195** against v7. Scored retroactively against v8, it hits **205/210** — already satisfying C-29 and C-31, failing only C-30. The R7 V-02 combined `If absent or no topic entry` branch produces a single message regardless of which axis triggered the stop; C-30 requires structurally distinct branches with a topic-specific message for the topic-absent case.

**Baseline score map:**

| Variant | C-29 | C-30 | C-31 | Predicted |
|---------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | 210/210   |
| V-02    | PASS | FAIL | PASS | 205/210   |
| V-03    | PASS | PASS | PASS | 210/210   |
| V-04    | PASS | PASS | PASS | 210/210   |
| V-05    | PASS | PASS | PASS | 210/210   |

---

## V-01: Single-axis — C-30 sequential guard (minimum delta)

**Axis:** C-30 only. Two numbered sequential stop conditions replace the combined branch in PHASE 2. Everything else is R7 V-02 unchanged.

**Hypothesis:** The minimum structural change to satisfy C-30 is splitting the combined guard into ordered numbered entries — Guard 1 for file-absent, Guard 2 for topic-absent-within-file with a topic-specific message. Isolates C-30 as the single independent criterion; satisfying it should move 205 → 210.

*(Full body in file.)*

---

## V-02: Single-axis — C-30 deliberately withheld (isolation test)

**Axis:** C-30 intentionally absent. PHASE 2 retains the R7 V-02 combined `If absent or no topic entry` branch verbatim.

**Hypothesis:** If C-30 scores independently from C-12, this lands at 205/210 — passing C-12 (file-absent stop) but failing C-30 (no distinct topic-absent branch, no topic-specific message). Confirms that C-12 ⊄ C-30 and a combined branch cannot satisfy either separately.

*(Full body in file.)*

---

## V-03: Single-axis — Lifecycle emphasis (phase boundary contracts, dual GUARD block)

**Axis:** Phase contract blocks (`INPUT / GUARD / OUTPUT`). PHASE 2's GUARD block lists both stop conditions as separate numbered entries — structurally unambiguous dual-axis exit.

**Hypothesis:** Declaring the two PHASE 2 stop conditions inside a formal GUARD block makes the C-30 distinction a first-class structural contract, not prose. A scorer cannot read a two-entry GUARD as a combined branch. Contract blocks also redundantly satisfy C-11/C-12 via OUTPUT and GUARD fields.

*(Full body in file.)*

---

## V-04: Combination — C-30 + vocabulary coherence preamble + inertia framing

**Axes:** Preamble declares the dual-axis C-30 exit as an architectural invariant (alongside C-26/C-27 rules). PRIMARY ADVERSARY named in COMMIT DECISION.

**Hypothesis:** Elevating C-30's two-branch logic to the preamble makes it a structural contract auditable before execution. The inertia framing deepens C-16's consequence verdict from threshold-based to comparative. Highest structural redundancy for C-30 across preamble + execution prose.

*(Full body in file.)*

---

## V-05: Combination — Lifecycle emphasis + full tier 7 + inertia framing

**Axes:** Phase contract blocks + all three Tier 7 criteria woven explicitly into phase contracts: C-29 in PHASE 2 OUTPUT declaration, C-30 as dual GUARD entries, C-31 in PHASE 2 OUTPUT declaration. PRIMARY ADVERSARY in COMMIT DECISION. Vocabulary preamble.

**Hypothesis:** Each Tier 7 criterion appears in at least two structural sites — template section AND phase contract declaration. C-30's two stop conditions appear in a named GUARD with distinct output text. Most auditable variant; scorer can verify all three Tier 7 criteria without reading the execution prose, from contracts alone.

*(Full body in file.)*

---

**C-30 isolation test (V-02 vs V-01):** If C-30 is independent of C-12, V-02 scores 205 and V-01 scores 210 — a clean 5-point gap confirming the combined branch is structurally insufficient regardless of message content.
