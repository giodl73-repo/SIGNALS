---

## Quest Score — campaign-behavior R11

**Rubric:** v9 (C-01–C-31, denominator 23)

---

### Per-Variation Scores

| Variation | C-30 | C-31 | Aspirational | Total |
|-----------|------|------|-------------|-------|
| V-03 | PARTIAL | PARTIAL | 21/23 → 9 | **89** |
| V-01 | PASS | PARTIAL | 22/23 → 10 | **90** |
| V-02 | PARTIAL | PASS | 22/23 → 10 | **90** |
| V-04 | PASS | PASS | 23/23 → 10 | **90** |
| **V-05** | PASS | PASS | 23/23 → 10 | **90** |

---

### Detailed Analysis

**V-01 (C-30 enforcement):** Adds explicit "free-form terminal name is INVALID here" gate before EXECUTIVE SUMMARY write. C-30 PASS. C-31 is PARTIAL — the bullet template has the correct citation format but no "plain [CONFIRMED] is NOT valid" prohibition. 22/23 → 10 pts → **90**.

**V-02 (C-31 enforcement):** Adds "The plain token [CONFIRMED] is NOT valid in EXECUTIVE SUMMARY bullets." C-31 PASS. C-30 is PARTIAL — `[terminal: T-NN]` in template but no free-form rejection language. 22/23 → 10 pts → **90**.

**V-03 (phrasing register shift):** WHY framing explains that T-NN codes are required "rather than free-form component names" and that confirmation status needs "evidence citation (so the reader knows...)". This is instructional contrast, not prohibition. No "INVALID" or "NOT valid" language. Both C-30 and C-31 remain PARTIAL — explanatory register does not cross the PARTIAL→PASS boundary. 21/23 → 9 pts → **89**.

**V-04 (C-30 + C-31 combined):** VALIDITY RULES section with two numbered orthogonal rules: rule 1 covers chain terminus (C-30), rule 2 covers confirmation slot (C-31). Both PASS. 23/23 → 10 pts → **90**.

**V-05 (full integration):** Adds three-layer enforcement over V-04 — VALIDITY RULES at write time, Q2 extended to preview EXECUTIVE SUMMARY slots before writing, Q7 dedicated post-write audit before CONSOLIDATE. C-30 and C-31 both PASS with two/three independent enforcement points respectively. 23/23 → 10 pts → **90**.

---

### Key Finding: Threshold Behavior

The 22/23 rounding boundary (9.565 → 10) means adding **either** C-30 or C-31 alone reaches the 90 ceiling. V-03 confirms WHY framing without explicit prohibition is insufficient — the operative structural element is "INVALID" / "NOT valid" language, not explanatory context.

---

### Excellence Signals from V-05

1. **Three-layer enforcement structure** — rejection at write time + Q2 pre-audit flag + Q7 dedicated post-write gate. Each layer catches the same failure mode at a different execution phase; any single failure leaves two fallbacks.
2. **Q7 as output-boundary gate** — fires after EXECUTIVE SUMMARY is written, before CONSOLIDATE; produces a traceable per-bullet status statement. Makes compliance visible in output, not just instructed in template.
3. **Q2 extended to preview summary compliance** — flags citation problems before the section is written; Q2 identifies, Q7 verifies fix. Bridges calibration and output phases.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Three-layer enforcement at a single output location (VALIDITY RULES rejection at write time + Q2 pre-audit flag + Q7 dedicated post-write gate) closes C-30/C-31 format-drift risk through independent fallbacks", "Q7 named post-write gate fires after EXECUTIVE SUMMARY and before CONSOLIDATE — produces a traceable status statement per bullet making compliance visible in output not just instructed in template", "Q2 extended to preview EXECUTIVE SUMMARY bullet compliance before the section is written — forward reference: Q2 flags, Q7 verifies fix; bridges calibration and output phases"]}
```
acing |
| C-27 | PASS | T-NN terminus table in Phase 0; chains use `[terminal: T-NN]`; Q1 flags registry miss |
| C-28 | PASS | Dedicated `## EXECUTIVE SUMMARY` heading; exactly 3 structured bullets |
| C-29 | PASS | Inline citation in field 6, VERDICT, EXECUTIVE SUMMARY bullets, Q2 — all 4 checkpoints |
| C-30 | PARTIAL | Template has `[terminal: T-NN]` — correct format; no rejection rule for free-form names |
| C-31 | PARTIAL | Template has `CONFIRMED -- evidence:` format — correct; no rejection rule for plain tokens |

**Baseline aspirational under v9: 21/23** (C-30 and C-31 both PARTIAL = FAIL for count)
**Baseline score: 50 + 30 + 9 = 89**

---

### V-01 — C-30 Explicit Enforcement

**What it adds:** Pre-write validation gate in EXECUTIVE SUMMARY: "BEFORE writing each bullet,
verify: 1. The chain terminus resolves to T-NN in Phase 0 registry. A free-form terminal name
(e.g., 'DataLayer') is INVALID here — use the T-NN code (e.g., T-04). If chain cannot resolve:
write 'unresolved chain — registry miss: [name]' and exclude."

| Criterion | Status | Note |
|-----------|--------|------|
| C-01–C-29 | PASS | All baseline criteria carry |
| C-30 | **PASS** | Explicit rejection: "free-form terminal name is INVALID" + T-NN code required + unresolved chain exclusion path |
| C-31 | PARTIAL | Correct format in template (`CONFIRMED -- evidence: [phase]: [finding]`); no "plain [CONFIRMED] is NOT valid" prohibition; same as baseline |

**Aspirational: 22/23 → 9.565 → 10**
**Score: 50 + 30 + 10 = 90**

---

### V-02 — C-31 Explicit Enforcement

**What it adds:** Explicit prohibition in EXECUTIVE SUMMARY after the bullet format template:
"IMPORTANT: The confirmation slot in each bullet MUST use the inline evidence citation format
above. The plain token [CONFIRMED] is NOT valid in EXECUTIVE SUMMARY bullets — it omits the
evidence link that makes the top-3 summary independently auditable."

| Criterion | Status | Note |
|-----------|--------|------|
| C-01–C-29 | PASS | All baseline criteria carry |
| C-30 | PARTIAL | Correct `[terminal: T-NN]` in template; no rejection rule for free-form names; same as baseline |
| C-31 | **PASS** | Explicit rejection: "plain token [CONFIRMED] is NOT valid in EXECUTIVE SUMMARY bullets"; explains consequence (evidence link omitted) |

**Aspirational: 22/23 → 9.565 → 10**
**Score: 50 + 30 + 10 = 90**

---

### V-03 — Phrasing Register Shift

**What it adds:** Converts the entire template from imperative to descriptive/explanatory register.
DEFINITIONS explain WHY each term exists. Phase headers explain anchor intent with causation.
EXECUTIVE SUMMARY section provides explanatory framing: "Using T-NN codes here, rather than
free-form component names, ensures the summary bullets are consistent with the Phase 0 registry
without requiring a manual re-read of the registry to verify." Bullet template unchanged from
R10 V-05.

**Key test:** Is R10 V-05's format already sufficient for C-30/C-31, or do explicit rejection
rules do real structural work? V-03 isolates phrasing register as the only variable.

| Criterion | Status | Note |
|-----------|--------|------|
| C-01–C-29 | PASS | All baseline criteria carry; WHY framing adds explanatory depth but no new structural passes |
| C-30 | PARTIAL | WHY framing: "T-NN codes here, rather than free-form component names" — this is instructional contrast, not a prohibition. No "INVALID" language. Template format correct but no rejection gate |
| C-31 | PARTIAL | WHY framing: "confirmation status with evidence citation (so the reader knows...)" — explains purpose, not prohibition. Same format as baseline, no "NOT valid" language |

**Aspirational: 21/23 → 9.13 → 9**
**Score: 50 + 30 + 9 = 89**

*Hypothesis verdict: Explicit rejection rules DO real structural work. WHY framing explains the*
*intent but doesn't constitute a rejection gate — a model can still substitute free-form names*
*or plain tokens after reading explanatory text, whereas "INVALID" / "NOT valid" language closes*
*the failure path directly.*

---

### V-04 — C-30 + C-31 Enforcement Combined

**What it adds:** VALIDITY RULES section in EXECUTIVE SUMMARY combining V-01 and V-02 rejection
rules in a numbered list:
1. "Chain terminus must use T-NN code from Phase 0 registry. A bullet with a free-form terminus
   is INVALID and must be rewritten using the T-NN code before this section is complete."
2. "Confirmation slot must carry inline evidence citation format: CONFIRMED -- evidence: ...
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets. A bullet that uses
   [CONFIRMED] without '-- evidence: ...' is structurally incomplete and must be revised."

| Criterion | Status | Note |
|-----------|--------|------|
| C-01–C-29 | PASS | All baseline criteria carry |
| C-30 | **PASS** | Explicit rejection in VALIDITY RULES rule 1: "free-form terminus is INVALID" + rewrite required |
| C-31 | **PASS** | Explicit rejection in VALIDITY RULES rule 2: "Plain [CONFIRMED] token is NOT valid" + revision required |

**Aspirational: 23/23 → 10**
**Score: 50 + 30 + 10 = 90**

*Note: VALIDITY RULES numbered list makes the two rules structurally orthogonal — rule 1 covers*
*the chain field, rule 2 covers the confirmation slot. No structural interference.*

---

### V-05 — Full Integration (C-30 + C-31 enforcement + Q7 gate + Q2 extension)

**What it adds over V-04:**
- Q2 extended: "Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as
  CONFIRMED, confirm that the same inline citation format will be used in the summary bullet
  (not a plain [CONFIRMED] token). Note any summary slots that would use plain tokens — revise
  those bullets after Q7."
- Q7 dedicated EXECUTIVE SUMMARY structural audit: fires after EXECUTIVE SUMMARY is written,
  before CONSOLIDATE. Per-bullet C-30 check (chain terminates at T-NN code) and C-31 check
  (confirmation slot uses inline citation). Produces: "EXECUTIVE SUMMARY audit complete —
  C-30 and C-31 satisfied for all three bullets. Proceeding to CONSOLIDATE."

Three-layer enforcement:
- Layer 1: VALIDITY RULES rejection at write time (same as V-04)
- Layer 2: Q2 extended pre-audit — flags EXECUTIVE SUMMARY slots before they're written
- Layer 3: Q7 post-write gate — re-audits all three bullets before CONSOLIDATE

| Criterion | Status | Note |
|-----------|--------|------|
| C-01–C-29 | PASS | All baseline criteria carry |
| C-30 | **PASS** | VALIDITY RULES rule 1 (write time) + Q7 C-30 check (post-write) — two independent enforcement points |
| C-31 | **PASS** | VALIDITY RULES rule 2 (write time) + Q2 extended (pre-audit) + Q7 C-31 check (post-write) — three independent enforcement points |

**Aspirational: 23/23 → 10**
**Score: 50 + 30 + 10 = 90**

*Note: Q7 maps to C-18 (calibration questions n>=3) but does not introduce any new unscored*
*aspirational criterion — n was already ≥3 with Q1–Q6. V-05's structural advantage is*
*enforcement depth, not new criterion passes. Both V-04 and V-05 score 23/23.*

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | C-30 | C-31 | Notes |
|-----------|-----------|-------------|--------------|-------|------|------|-------|
| V-03 | 50 | 30 | 9 (21/23) | **89** | PARTIAL | PARTIAL | WHY framing; no rejection rules |
| V-01 | 50 | 30 | 10 (22/23) | **90** | PASS | PARTIAL | C-30 gate only |
| V-02 | 50 | 30 | 10 (22/23) | **90** | PARTIAL | PASS | C-31 gate only |
| V-04 | 50 | 30 | 10 (23/23) | **90** | PASS | PASS | both gates; no extra layers |
| **V-05** | 50 | 30 | 10 (23/23) | **90** | PASS | PASS | both gates + Q7 + Q2 extension |

**Ranking:** V-05 = V-04 = V-01 = V-02 (90) > V-03 (89)
**Top variation:** V-05 — tied on score but deepest structural enforcement; golden candidate for v9

---

### Key Finding: C-30/C-31 Threshold Behavior

The aspirational rounding creates a discontinuity at 22/23:
- 21/23 = 9.13 → 9 pts (R10 V-05 baseline under v9, V-03)
- 22/23 = 9.565 → **10 pts** (V-01, V-02)
- 23/23 = 10.00 → 10 pts (V-04, V-05)

This means adding EITHER C-30 or C-31 alone (V-01 or V-02) is sufficient to reach the 90 ceiling
under v9. V-03 confirms that WHY framing without explicit rejection language is not sufficient —
the explanatory framing does not cross the PARTIAL→PASS boundary for C-30 or C-31. Explicit
prohibition language ("INVALID", "NOT valid") is the operative structural element.

---

### Excellence Signals from V-05

**Signal 1 — Three-layer enforcement at a single output location**
C-30 and C-31 were identified as format-drift risks: a model executing the template might
substitute free-form names or plain tokens at the one section (EXECUTIVE SUMMARY) that is
written after all calibration questions. V-05 closes this with three independent layers:
rejection at write time (VALIDITY RULES), pre-audit before writing (Q2 extension), post-write
re-audit before output boundary (Q7). Each layer catches the same failure mode at a different
execution phase. Any single layer failing leaves two fallbacks.

**Signal 2 — Q7 as an explicit output-boundary gate**
The Q7 gate fires after EXECUTIVE SUMMARY is written and before CONSOLIDATE begins. This creates
a visible audit step in the output — "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
for all three bullets" — making compliance traceable, not just instructed. The reviewer can
confirm the gate ran and what it found. Pattern: when a structural requirement is at risk of
format drift, add a named post-write gate that produces a traceable status statement.

**Signal 3 — Q2 extension bridges calibration and summary writing**
Extending Q2 to preview EXECUTIVE SUMMARY bullet compliance means the calibration phase identifies
citation problems before the section is written, not after. "Note any summary slots that would
use plain tokens — revise those bullets after Q7." This creates a forward reference: Q2 flags
the issue, Q7 verifies the fix. Pattern: extend existing calibration gates to preview output
sections before those sections are written.

**Signal 4 — Orthogonal enforcement: chain field vs confirmation slot**
The two VALIDITY RULES address structurally independent fields of the bullet format. Rule 1
governs the chain terminus field (C-30); Rule 2 governs the confirmation slot (C-31). They
can be verified independently and do not require cross-field reasoning. Pattern: when two
integrity requirements apply to the same output location, decompose them into orthogonal rules
per field to avoid a single composite rule that is harder to audit and easier to partially satisfy.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Three-layer enforcement at a single output location (VALIDITY RULES rejection at write time + Q2 pre-audit flag + Q7 dedicated post-write gate) closes C-30/C-31 format-drift risk through independent fallbacks", "Q7 named post-write gate fires after EXECUTIVE SUMMARY and before CONSOLIDATE — produces a traceable status statement per bullet making compliance visible in output not just instructed in template", "Q2 extended to preview EXECUTIVE SUMMARY bullet compliance before the section is written — forward reference: Q2 flags, Q7 verifies fix; bridges calibration and output phases"]}
```
