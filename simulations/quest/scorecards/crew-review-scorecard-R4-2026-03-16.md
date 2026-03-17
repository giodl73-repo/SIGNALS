## crew-review — Quest Score R4 (Rubric v4)

### Scoring Parameters

| Tier | Count | Per Criterion | Max |
|------|-------|--------------|-----|
| Essential | 5 | 12 | 60 |
| Recommended | 6 | 10 | 60 |
| Aspirational | 8 | 2.5 | 20 |
| **Total** | | | **140** |

PARTIAL = half points. Golden threshold: composite >= 80 with all essential passing.

---

## V-01 — Challenger Phase Gate (C-17 axis)

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | Step 1 reads all `.craft/roles/` files; "Zero roles may be fabricated" |
| C-02 | PASS | 4-column output table (Role, Findings, Severity, Recommendation) |
| C-03 | PASS | Column constraint: "exactly HIGH, MEDIUM, or LOW -- no other labels" |
| C-04 | PASS | Domain roles apply `lens.verify` perspective; challenger applies null-hypothesis frame |
| C-05 | PASS | "one concrete action naming what to do and where in the artifact" |

Essential: **60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Standard: 2-3 roles; `--depth deep`: all non-challenger roles |
| C-07 | PASS | Cross-role synthesis required after table |
| C-08 | PASS | AMEND section with 4 specific options including rerun:challengers |
| C-09 | PASS | CHALLENGER PHASE runs all `archetype: challenger` roles first; null hypothesis 4-slot form present |
| C-10 | PASS | "Name a specific artifact surface in each finding" |
| C-14 | PASS | Three unconditional ERROR halts; no soft fallback |

Recommended: **60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | PASS | 4-slot form (SLOT-A through SLOT-D) with named blanks |
| C-12 | FAIL | No per-role Lens column or one-sentence lens declaration before findings |
| C-13 | FAIL | Column constraints listed in Output section but no per-row validation gate |
| C-15 | PASS | CHALLENGER PHASE and DOMAIN PHASE named as discrete sections |
| C-16 | PASS | Per-slot escalation rule: "log a HIGH finding" per unfilled slot individually |
| C-17 | PASS | G1 with named OPEN/CLOSED state; 5-condition closure; "Domain review does not begin until G1 closes." — structural gate, not sequence hint |
| C-18 | FAIL | Escalation produces "a HIGH finding" but does not specify it as a separate dedicated matrix row |
| C-19 | FAIL | Column constraints state valid values only; no named anti-pattern exclusions |

Aspirational: **10/20** (C-11, C-15, C-16, C-17)

**V-01 composite: 60 + 60 + 10 = 130/140 — GOLDEN**

---

## V-02 — Slot-to-Row Escalation (C-18 axis)

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | Step 1 reads registry; "Zero roles may be invented" |
| C-02 | PASS | 4-column table; slot-gap escalation rows follow same schema |
| C-03 | PASS | "Severity: exactly HIGH, MEDIUM, or LOW -- no other values" |
| C-04 | PASS | Domain roles apply `lens.verify`; challenger applies null-hypothesis frame |
| C-05 | PASS | "Recommendation: one concrete action naming what to do and where" |

Essential: **60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Standard 2-3 roles; `--depth deep` all non-challenger |
| C-07 | PASS | Cross-role synthesis required; slot-gap rows count for convergence detection |
| C-08 | PASS | AMEND section with 4 specific options |
| C-09 | PASS | "Find all roles with `archetype: challenger`. Run each one before any domain review" + null hypothesis form |
| C-10 | PASS | "Name a specific artifact surface in each finding" |
| C-14 | PASS | Unconditional ERROR halts; no soft fallback |

Recommended: **60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | PASS | 4-slot form with SLOT-A through SLOT-D named blanks |
| C-12 | FAIL | No Lens column or per-role lens-lock declaration |
| C-13 | FAIL | No typed column schema; no per-row validation gate |
| C-15 | PASS | "Step 2 -- Challenger bracket" and "Step 3 -- Domain review" as named discrete steps |
| C-16 | PASS | Slot-to-row escalation rule includes HIGH severity per slot individually |
| C-17 | FAIL | No named gate; "Run each one before any domain review" is a sequence instruction, not an exit condition |
| C-18 | PASS | Explicit: "Produce a **separate, dedicated matrix row**"; "Do not embed... as a sentence"; "Two unfilled slots = two rows" — fully specified |
| C-19 | FAIL | No anti-pattern exclusions in column constraints |

Aspirational: **10/20** (C-11, C-15, C-16, C-18)

**V-02 composite: 60 + 60 + 10 = 130/140 — GOLDEN**

---

## V-03 — Anti-Pattern Exclusion in Typed Column Constraints (C-19 axis)

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | Phase 1 -- Load reads all `.craft/roles/` files; "Zero roles may be invented" |
| C-02 | PASS | 5-column table is superset; all four required columns present |
| C-03 | PASS | Severity column: "enum -- exactly `HIGH`, `MEDIUM`, or `LOW`" + NOT: freestyle labels |
| C-04 | PASS | Per-role Lens column traceable to `lens.verify`; per-row validation gate enforces non-overlap |
| C-05 | PASS | Recommendation column: "names (1) what to do and (2) where in the artifact" + NOT exclusion |

Essential: **60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Standard selects 2-4 roles; `--depth deep` all roles in registry |
| C-07 | PASS | Cross-role synthesis required |
| C-08 | PASS | AMEND section with 4 specific options including rerun:[role-name] |
| C-09 | PASS | "Execute roles in this order: `archetype: challenger` first"; Lens cell opens with null hypothesis framing |
| C-10 | PASS | Findings column type: "names a specific artifact surface: a section title, field name, diagram element, or named assumption"; NOT abstract observations |
| C-14 | PASS | Unconditional ERROR halts in Phase 1 |

Recommended: **60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | FAIL | No 4-slot null hypothesis template; challenger only has "null hypothesis framing" in Lens cell |
| C-12 | PASS | Lens column with required format "As a [role], I care about [specific concern from `lens.verify`]"; NOT: generic restatements |
| C-13 | PASS | 5-column typed schema declared before execution; per-row validation gate explicitly required before writing each row |
| C-15 | FAIL | No separate challenger phase; ordering instruction ("`archetype: challenger` first") is within a single Phase 3 -- Review step |
| C-16 | FAIL | No null hypothesis slot template; no slot-level escalation defined |
| C-17 | FAIL | No named gate or exit condition |
| C-18 | FAIL | No slot-to-row escalation (no slots defined) |
| C-19 | PASS | Every column definition includes "NOT:" exclusion inline: Lens ("NOT: generic role restatements"), Findings ("NOT: abstract observations without a named surface"), Severity ("NOT: freestyle labels"), Recommendation ("NOT: generic directives") |

Aspirational: **7.5/20** (C-12, C-13, C-19)

**V-03 composite: 60 + 60 + 7.5 = 127.5/140 — GOLDEN**

---

## V-04 — Gate Exit Condition Tied to Row Production (C-17 + C-18 axes)

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | PHASE 1 L3 halts; "Zero roles may be invented" |
| C-02 | PASS | 4-column output table with challenger rows + slot-gap rows + domain rows |
| C-03 | PASS | "Severity: exactly HIGH, MEDIUM, or LOW only" |
| C-04 | PASS | Domain roles apply `lens.verify`; non-repeat rule enforced |
| C-05 | PASS | "one action naming what to do and where" |

Essential: **60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Standard 2-3; `--depth deep` all non-challenger |
| C-07 | PASS | Cross-role synthesis required; slot-gap rows count |
| C-08 | PASS | AMEND section with 4 specific options |
| C-09 | PASS | PHASE 2 runs challengers first; 4-slot form present |
| C-10 | PASS | "Name a specific artifact surface in each finding" |
| C-14 | PASS | Unconditional L3 ERROR halts |

Recommended: **60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | PASS | 4-slot form (SLOT-A through SLOT-D) with named blanks |
| C-12 | FAIL | No Lens column; no per-role one-sentence lens declaration |
| C-13 | FAIL | No typed column schema; Output section has no per-row validation gate |
| C-15 | PASS | PHASE 2 -- CHALLENGER BRACKET and PHASE 3 -- DOMAIN REVIEW AND OUTPUT as named discrete phases with entry conditions |
| C-16 | PASS | C4 per-slot escalation to HIGH; "Generic placeholders count as unfilled" |
| C-17 | PASS | Gate G1 with explicit 5-condition exit; "**Domain review does not begin until G1 exits.**"; C6 verify step — structural block, not sequence hint |
| C-18 | PASS | G1 exit condition 3 requires "a **dedicated, separate matrix row** exists... a full 4-column row... with severity HIGH"; C4 makes explicit: "not a sentence within the challenger's primary Findings cell"; "Two unfilled slots = two separate rows" |
| C-19 | FAIL | No anti-pattern exclusions in column constraints |

Aspirational: **12.5/20** (C-11, C-15, C-16, C-17, C-18)

**V-04 composite: 60 + 60 + 12.5 = 132.5/140 — GOLDEN**

---

## V-05 — Maximal Combination (C-17 + C-18 + C-19)

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | PHASE 1 L3 halts; "Zero roles may be invented" |
| C-02 | PASS | 5-column table includes all four required columns; per-row validation gate enforces completeness |
| C-03 | PASS | Severity: "enum -- exactly `HIGH`, `MEDIUM`, or `LOW`"; NOT: freestyle labels; NOT: combinations — strongest specification |
| C-04 | PASS | Lens column forces per-role perspective declaration traceable to `lens.verify`; NOT: concerns from another role's lens |
| C-05 | PASS | Recommendation: "names (1) what to do and (2) where in the artifact"; NOT: generic directives; per-row validation gate enforces |

Essential: **60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | "Target 2-4 total" standard; `--depth deep` all non-challenger |
| C-07 | PASS | R3 cross-role synthesis required; slot-gap rows count for convergence detection |
| C-08 | PASS | AMEND section with 5 specific options including scope:group[N] |
| C-09 | PASS | PHASE 2 challenger bracket runs first; 4-slot null hypothesis form; slot-gap rows follow 5-column schema |
| C-10 | PASS | Findings column: "names a specific artifact surface: section title, field name, diagram element, or named assumption"; NOT: abstract observations — both positive and negative defined |
| C-14 | PASS | Unconditional L3 ERROR halts; no soft fallback |

Recommended: **60/60**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | PASS | 4-slot form (SLOT-A through SLOT-D) in C2 |
| C-12 | PASS | Lens column with "one sentence: 'As a [role], I care about [specific concern from `lens.verify`]'"; NOT: generic restatements ("As a PM, I review as a PM") — strongest Lens definition |
| C-13 | PASS | 5-column typed schema declared before execution; "Per-row validation gate: before writing any row, verify all five cells against their constraints, including anti-pattern exclusions"; also applied to slot-gap rows in C4 |
| C-15 | PASS | PHASE 2 -- CHALLENGER BRACKET and PHASE 3 -- DOMAIN REVIEW as named discrete phases with explicit entry conditions |
| C-16 | PASS | C4 slot-to-row escalation with "Severity: HIGH" per slot individually; "Generic placeholders count as unfilled" |
| C-17 | PASS | G1 with explicit 4-condition exit; "**Domain review does not begin until G1 exits.**"; G1 exit condition defined in terms of row production, not declaration |
| C-18 | PASS | G1 exit condition 3: "a **dedicated, separate matrix row** exists -- a full 5-column row following the output schema above, with Severity = HIGH. This row is in the matrix. It is not a sentence inside another row's Findings cell. It is not an appended note."; C4 slot-gap row includes all 5 columns with lens statement; per-row validation gate applied to slot-gap rows |
| C-19 | PASS | Every column definition includes explicit "NOT:" exclusion: Role (NOT: invented names), Lens (NOT: generic restatements; NOT: concerns from another role's lens; NOT: multi-sentence), Findings (NOT: abstract observations without named surface), Severity (NOT: freestyle labels; NOT: blank cells; NOT: combinations), Recommendation (NOT: generic directives; NOT: without named location) |

Aspirational: **20/20 — perfect**

**V-05 composite: 60 + 60 + 20 = 140/140 — GOLDEN**

---

## Rankings

| Rank | Var | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----|-----------|-------------|--------------|-----------|--------|
| 1 | V-05 | 60/60 | 60/60 | 20/20 | **140** | YES |
| 2 | V-04 | 60/60 | 60/60 | 12.5/20 | **132.5** | YES |
| 3 | V-01 | 60/60 | 60/60 | 10/20 | **130** | YES |
| 3 | V-02 | 60/60 | 60/60 | 10/20 | **130** | YES |
| 5 | V-03 | 60/60 | 60/60 | 7.5/20 | **127.5** | YES |

All five variations are GOLDEN. All five pass all essential criteria.

---

## Excellence Signals from V-05

**1. Gate exit condition defined in terms of artifact production**
V-05's G1 exit condition 3 states the gate cannot close unless each unfilled slot "has a dedicated, separate matrix row" existing in the output. The gate's truth is evaluated by inspecting the matrix, not by checking whether an action was declared complete. C-17 and C-18 become mutually enforcing: you cannot satisfy the gate (C-17) without having produced the rows (C-18). Neither criterion can be gamed in isolation.

**2. Slot-gap escalation rows carry the full output schema including Lens**
In V-01 and V-04, slot-gap rows use the same 4-column schema. In V-05, slot-gap rows use the full 5-column schema — the Lens cell of a slot-gap row reads "As a [role], I care about whether the null hypothesis can be stated completely -- SLOT-[letter] is missing." The escalated gap is not structurally demoted from domain findings; it is on the same footing, scored the same way, with the same per-row validation gate applied before writing.

**3. Anti-pattern exclusion in every column definition, including Lens**
V-03 introduced C-19 with anti-pattern exclusions across columns. V-05 extends this to the Lens column with "NOT: generic restatements ('As a PM, I review as a PM'); NOT: concerns taken from a different role's lens; NOT: lens statements longer than one sentence" — three specific failure modes named inside the column type definition. The Lens column is the hardest to enforce correctly (it requires perspective specificity); having its failure modes named within the constraint makes drift detectable at construction time.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Gate exit condition defined in terms of artifact production: the gate cannot close until the required rows exist in the matrix, making C-17 and C-18 mutually enforcing rather than independently instructed", "Slot-gap escalation rows carry the full output schema including the Lens column: escalated gaps are structurally equal to domain findings, same per-row validation gate applied, same five columns produced"]}
```
