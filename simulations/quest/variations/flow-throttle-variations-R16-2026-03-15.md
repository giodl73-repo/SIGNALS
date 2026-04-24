Here are the five complete variations for Round 16:

---

## flow-throttle Variate — Round 16

**Rubric:** v16 (C-01–C-41, 33 aspirational) | **Max composite:** 255 | **Baseline ceiling:** 250/255 (C-41 FAIL)

---

### State Analysis

R15's best variant (V-04) has C-01–C-40 passing. C-41 fails because the count check is a bullet item *inside* the Role 2 PHASE 1 ENTRY CONDITION — it is readable without acting on it. A discrepancy is only detectable after Phase 1 produces output. C-41 requires the count check to be a structural gate that prevents Phase 1 from opening.

---

### Variation Map

| Variation | Axes | C-41 mechanism | Predicted |
|-----------|------|----------------|-----------|
| V-01 | Lifecycle emphasis (single) | Standalone INVENTORY GATE phase with CLEARED/BLOCKED outcomes | 255/255 |
| V-02 | Output format (single) | 3-row verification table with Expected/Actual/Verdict | 255/255 |
| V-03 | Role sequence (single) | Dedicated Role 1.5 (INVENTORY VERIFIER) with single responsibility | 255/255 |
| V-04 | Phrasing register + lifecycle | SHALL-dominant 3-subsection gate block | 255/255 |
| V-05 | Role sequence + output format + inertia framing | Handoff table + gate table + "looks complete" failure mode named and rejected | 255/255 |

---

### V-01 — Single Axis: Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** A standalone named phase — `INVENTORY GATE` — positioned between FORMAT CONTRACT COMPLETE and Role 2's opening, with its own section header, explicit GATE CLEARED / GATE BLOCKED state field, and a restart procedure, creates stronger lifecycle salience for C-41 than a bullet item inside a Phase 1 entry condition. The executor cannot skip it because it has a visible outcome field that must be resolved before Role 2 is named.

**Key C-41 implementation — INVENTORY GATE:**
```
---
**INVENTORY GATE — Phase 1 unlock procedure**

This is a standalone phase between FORMAT CONTRACT COMPLETE and Role 2.
Role 2 SHALL NOT open until this gate reaches GATE CLEARED.

Gate procedure:
1. Count Section C Annot-ID rows.
2. Compare to declared count: expected = 7.
3. Apply outcome:
   - Count = 7 → GATE CLEARED — proceed to Role 2 / Phase 1.
   - Count < 7 → GATE BLOCKED — FORMAT CONTRACT COMPLETE was stated prematurely.
     Return to Role 1, complete Section C to 7 rows, re-state FORMAT CONTRACT COMPLETE,
     then re-enter this gate.

GATE STATUS: [ CLEARED / BLOCKED ] — fill before proceeding.
An executor SHALL NOT open Phase 1 until GATE STATUS = CLEARED is explicitly recorded.
---
```

*(Full prompt body in file — identical structure for Role 1, Format Contract, Section C with C-38/C-39/C-40, then INVENTORY GATE above, then Role 2 Steps 1A–2H, then Audit block with Field 5 checking GATE STATUS.)*

---

### V-02 — Single Axis: Output Format

**Axis:** Output format
**Hypothesis:** Expressing the C-41 gate as a 3-row structured table (Check / Expected / Actual / Verdict) makes the count comparison mechanically visible and produces an observable cell that must be filled. A table-format gate cannot be "passed over" without the Verdict cell remaining blank — itself a detectable compliance failure. The annotation inventory adds a `Gate-weight` column so count derivation is auditable within the table.

**Key C-41 implementation — PHASE 1 ACTIVATION TABLE:**
```
---
**PHASE 1 ACTIVATION TABLE**

Fill before opening any analysis section. Phase 1 SHALL NOT open until Verdict = PROCEED.

| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| Section C Gate-weight=Y row count | 7 | [count them] | PROCEED / RETURN TO ROLE 1 |
| FORMAT CONTRACT COMPLETE stated | present | [Y/N] | PROCEED if Y |
| All Section C anchor sites populated | all 7 | [Y/N] | PROCEED if Y |

Activation outcome:
- All rows PROCEED → open Phase 1.
- Any row RETURN TO ROLE 1 → correct the gap, re-state FORMAT CONTRACT COMPLETE, re-fill.

ACTIVATION STATUS: [ PROCEED / RETURN TO ROLE 1 ] — fill this field.
Step 1A SHALL NOT begin if this field is unfilled or RETURN TO ROLE 1.
---
```

The annotation inventory table gains a `Gate-weight` column (all Y) making the 7-row count derivation visible without traversing annotation content.

---

### V-03 — Single Axis: Role Sequence

**Axis:** Role sequence
**Hypothesis:** Elevating the count check to a named standalone role — **Role 1.5 (INVENTORY VERIFIER)** — with a single responsibility and two-signal handoff chain (FORMAT CONTRACT COMPLETE triggers Role 1.5; INVENTORY VERIFIED triggers Role 2) creates the clearest possible role-sequence gate. A named role cannot be skipped without a visible structural gap. Role 2 has an explicit activation signal to check by name.

**Key C-41 implementation — Role 1.5:**
```
---
**ROLE 1.5 — INVENTORY VERIFIER**

Activation condition: FORMAT CONTRACT COMPLETE has been stated.
Single responsibility: Confirm Section C row count = declared count of 7.
This role produces no analysis output.

Handoff signal (conditional):
- Count = 7 → state INVENTORY VERIFIED → Role 2 activates.
- Count < 7 → state INVENTORY INCOMPLETE → return to Role 1.

Verification procedure:
1. Count Annot-ID rows in Section C.
2. Declared count: 7. Actual count: [fill].
3. Outcome: actual=7 → INVENTORY VERIFIED; actual<7 → INVENTORY INCOMPLETE.

HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ] — fill before Role 2.
---

**ROLE 2 — DOMAIN EXPERT**

Activation condition: INVENTORY VERIFIED (from Role 1.5).
An executor SHALL NOT open Step 1A if HANDOFF SIGNAL = INVENTORY INCOMPLETE or unfilled.
```

The role activation chain is also stated in an upfront table at the top of the prompt, making the four-role sequence (Role 1 → Role 1.5 → Role 2 → Role 3) visible before any content begins.

---

### V-04 — Combined: Phrasing Register + Lifecycle Emphasis

**Axes:** Formal normative register (primary) + lifecycle emphasis (secondary)
**Hypothesis:** Maximizing SHALL/MUST/PROHIBITED density at the Phase 1 entry gate — naming every decision point as a normative obligation — creates the strongest C-40 + C-41 joint coverage. Every branch says SHALL NOT; the return condition is stated as a sequence of SHALL obligations, not suggestions. Lifecycle emphasis: the gate is a full named section with three named subsections (Count declaration / Confirmation / Outcome).

**Key C-41 implementation — PHASE 1 ENTRY CONDITION:**
```
---
**PHASE 1 ENTRY CONDITION — MANDATORY GATE (C-41)**

An executor SHALL complete this section before opening Step 1A.
An executor SHALL NOT open Step 1A until this gate is cleared.

Subsection 1 — Count declaration:
  Section C declares 7 required annotations. Expected row count = 7.

Subsection 2 — Confirmation:
  An executor SHALL count the Annot-ID rows in Section C.
  Actual count: [fill — required before proceeding to Subsection 3].

Subsection 3 — Outcome (SHALL NOT proceed until resolved):
  - Actual = 7: PHASE 1 ENTRY CONDITION CLEARED.
    An executor SHALL proceed to Step 1A.
  - Actual < 7: PHASE 1 ENTRY CONDITION BLOCKED.
    An executor SHALL return to Role 1.
    An executor SHALL complete Section C to declared count of 7.
    An executor SHALL re-state FORMAT CONTRACT COMPLETE.
    An executor SHALL re-enter this gate from Subsection 1.
    An executor SHALL NOT proceed to Step 1A.

PHASE 1 ENTRY CONDITION STATUS: [ CLEARED / BLOCKED ]
An executor SHALL fill this field. An executor SHALL NOT open Step 1A if BLOCKED or unfilled.
---
```

---

### V-05 — Combined: Role Sequence + Output Format + Inertia Framing

**Axes:** Role sequence (primary) + output format (secondary) + inertia framing (secondary)
**Hypothesis:** Three axes compound:
1. A role-handoff table at the prompt's opening makes the activation chain legible before any content.
2. Gate tables with Verdict cells make compliance gaps visible as blank cells.
3. Inertia framing explicitly names the "looks complete" bypass failure mode and rejects it with a structural proof parallel to the C-26 circular-dependency proof at Step 1B — converting C-41 from a policy requirement into a logical necessity.

**Key C-41 implementation — Role 1.5 with inertia frame:**
```
Role activation chain:
| Role | Activation signal | Handoff signal |
|------|------------------|----------------|
| Role 1 — FORMAT CONTRACT | None | FORMAT CONTRACT COMPLETE |
| Role 1.5 — INVENTORY VERIFIER | FORMAT CONTRACT COMPLETE | INVENTORY VERIFIED / INCOMPLETE |
| Role 2 — DOMAIN EXPERT | INVENTORY VERIFIED | Step 2H closed |
| Role 3 — AUDIT | Step 2H closed | Audit complete |

---
**ROLE 1.5 — INVENTORY VERIFIER**

Inertia frame — the "looks complete" bypass failure mode:
The temptation to skip Role 1.5 is the "looks complete" framing — because FORMAT CONTRACT
COMPLETE has been stated and the analysis tables are scaffolded, activating Role 2 appears
to miss no required steps. This frame is self-defeating: FORMAT CONTRACT COMPLETE confirms
that Role 1's sections are present — it does not verify that the annotation inventory is
complete to its declared count. A partial Section C (e.g., 6 of 7 annotations) satisfies
Role 1's section presence check while failing the count declared in Section C's header.
Skipping Role 1.5 converts the Section C count from a verifiable gate into an unverified
assertion — a discrepancy is detectable only after Role 2 has produced output.

Verification table:
| Check | Expected | Actual | Verdict |
|-------|----------|--------|---------|
| Section C Annot-ID row count | 7 | [count] | PASS if =7 / FAIL if <7 |
| FORMAT CONTRACT COMPLETE stated | present | [Y/N] | PASS if Y |

HANDOFF SIGNAL: [ INVENTORY VERIFIED / INVENTORY INCOMPLETE ]
```

---

Written to `simulations/quest/golden/flow-throttle-variate-R16-2026-03-16.md`.

**Design decisions across variations:**

- **V-01** isolates the gate as a lifecycle event with its own phase name and observable status field — the cleanest single-axis test for C-41.
- **V-02** makes the gate mechanically verifiable via a table's Verdict column — tests whether output-format expression is sufficient for C-41 without a named phase.
- **V-03** tests whether role-sequence elevation alone (Role 1.5 named role) satisfies C-41 at the structural level — the handoff signal is the gate.
- **V-04** combines register density with lifecycle structure — tests C-40 + C-41 joint coverage; every SHALL NOT at the gate doubles as C-40 evidence.
- **V-05** is the strongest combination: the inertia frame's structural-proof argument (parallel to the C-26 escape-route at Step 1B) is the most durable C-41 formulation because it shows *why* the gate is logically necessary, not just that it is required.
