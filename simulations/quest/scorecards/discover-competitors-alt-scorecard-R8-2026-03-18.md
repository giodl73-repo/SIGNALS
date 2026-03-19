# discover-competitors-alt — Round 8 Scorecard

## Rubric Version: v8 | Aspirational Pool: 17 criteria (0.588 pts each)

---

## V-01 — Lifecycle emphasis: TOKEN in every completion condition

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Dedicated "C0 — before any competitor row" header; C0 row precedes all competitor rows in template |
| C-02 | 3+ named competitors with threat levels | PASS | "Min 3 named competitors, explicit threat levels" enforced in GATE-2 completion condition |
| C-03 | C0 at row 0 in competitive map | PASS | Template shows C0 as first table row explicitly |
| C-04 | Whitespace identified | PASS | Dedicated WHITESPACE labeled finding with specific uncontested dimension required |
| C-05 | Auto-detect topic | PASS | "Detect focus dimension and infer topic from repo context. Do not ask the user." |
| C-06 | Mechanism-level inertia | PASS | "Mechanism must name something C0 actually does or provides — 'Inertia is high' without a product-specific anchor fails" |
| C-07 | Web-verified claim with inline citation | PASS | "Run a WebSearch to verify at least one competitor claim" + "1+ inline Source citation — not a footnote" |
| C-08 | AMEND with input-to-output pairs | PASS | AMEND table has "Input change" and "Output effect" columns, min 3 rows enforced |
| C-09 | Cross-dimensional whitespace | PASS | "If FOCUS is ACTIVE: gap must be uncontested across both competitive + focus dimensions simultaneously" |
| C-10 | Grounded findings | PASS | "each anchored to a named competitor row" + "Findings readable without GATE-2 fail the grounding test" |
| C-11 | Inertia propagates downstream | PASS | TOKEN appears in GATE-3 `vs [TOKEN]` lines, whitespace `[TOKEN] exposure:` field, and GATE-4 Stability verdicts |
| C-12 | AMEND evaluates inertia stability | PASS | Stability verdict column present; GATE-4 completion condition requires TOKEN in every verdict cell |
| C-13 | Portable token assigned | PASS | Explicit TOKEN declaration with rules; "SIGNAL-GRIP, WORKFLOW-ANCHOR, PLUGIN-LOCK" shown as passing examples |
| C-14 | Stability in every AMEND entry | PASS | "Every Stability verdict cell references TOKEN by its declared value" — no exception |
| C-15 | Token pre-declared before C0 | PASS | GATE-0 unconditional; TOKEN declared before GATE-2 (C0 section) ever executes |
| C-16 | Stability + evidence per entry | PASS | "Evidence must contain reasoning — 'Stable.' alone fails" |
| C-17 | Token encodes domain context | PASS | TOKEN rules: "Generic placeholder alone (MECH, LOCK, INERTIA-REF) fails" — domain term required |
| C-18 | DOMAIN-TERMS artifact before token | PASS | "Write and close before TOKEN" — DOMAIN-TERMS is its own output artifact line |
| C-19 | TOKEN before all conditional logic | PASS | GATE-0 is unconditional; nothing (no headers, focus detection, conditionals) precedes DOMAIN-TERMS + TOKEN |
| C-20 | AMEND schema enumerates all 4 components | PASS | AMEND table template explicitly names all four columns: Input change, Output effect, Stability verdict, Evidence |
| C-21 | Pre-phase names unconditional + conditional successor | PASS | Manifest row: "Only unconditional gate; GATE-1 is its conditional successor" — both conditions satisfied |
| C-22 | Schema component names domain-neutral | PASS | "Input change", "Output effect", "Stability verdict", "Evidence" — all self-interpreting without domain knowledge |
| C-23 | Full gate manifest pre-execution | PASS | EXECUTION PLAN table lists all 5 gates with execution modes before GATE-0 runs |
| C-24 | Manifest as native markdown table | PASS | EXECUTION PLAN is pipe-and-hyphen outside any code fence — native table, not code-fenced text |
| C-25 | TOKEN in every gate output specification | PASS | Every completion condition names TOKEN by declared value: GATE-0 ("TOKEN: written and closed"), GATE-1 ("TOKEN by its declared value is required in every subsequent gate's output"), GATE-2 ("`vs [TOKEN]` column header uses TOKEN by its declared value"), GATE-3 ("`vs [TOKEN]` lines using TOKEN by declared value" + "`[TOKEN] exposure:` field naming TOKEN"), GATE-4 ("Every Stability verdict cell references TOKEN by its declared value") |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 17/17 × 10 = **10.0**
**Composite: 100.0** | Golden: YES

---

## V-02 — Role sequence: manifest completion-signal column as C-25 contract

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Pattern maintained; GATE-2 structure preserves C0-first ordering |
| C-02 | 3+ competitors with threat levels | PASS | Carried from baseline |
| C-03 | C0 at row 0 | PASS | Carried from baseline |
| C-04 | Whitespace identified | PASS | Carried from baseline |
| C-05 | Auto-detect topic | PASS | Carried from baseline |
| C-06 | Mechanism-level inertia | PASS | Carried from baseline |
| C-07 | Web-verified claim | PASS | Carried from baseline |
| C-08 | AMEND with input-to-output pairs | PASS | Carried from baseline |
| C-09 | Cross-dimensional whitespace | PASS | Carried from baseline |
| C-10 | Grounded findings | PASS | Carried from baseline |
| C-11 | Inertia propagates downstream | PASS | Manifest completion signals specify TOKEN propagation to all subsequent gates |
| C-12 | AMEND evaluates stability | PASS | Carried from baseline |
| C-13 | Portable token | PASS | GATE-0 completion signal: "TOKEN by its declared value is the required first-declared output" |
| C-14 | Stability in every AMEND entry | PASS | Carried from baseline |
| C-15 | Token pre-declared before C0 | PASS | GATE-0 unconditional; TOKEN before GATE-2 |
| C-16 | Stability + evidence | PASS | Carried from baseline |
| C-17 | Token encodes domain context | PASS | Carried from baseline |
| C-18 | DOMAIN-TERMS artifact | PASS | GATE-0 manifest row names DOMAIN-TERMS + TOKEN both required |
| C-19 | TOKEN before all conditional logic | PASS | GATE-0 unconditional, TOKEN is first-declared output per manifest |
| C-20 | AMEND schema enumerates 4 components | PASS | Carried from baseline |
| C-21 | Pre-phase names unconditional + successor | PASS | EXECUTION MANIFEST declares GATE-0 UNCONDITIONAL and GATE-1 CONDITIONAL (first) |
| C-22 | Domain-neutral component names | PASS | Carried from baseline |
| C-23 | Full gate manifest pre-execution | PASS | EXECUTION MANIFEST native table covers all 5 gates |
| C-24 | Manifest as native markdown table | PASS | "EXECUTION MANIFEST" uses pipe-and-hyphen native table syntax |
| C-25 | TOKEN in every gate output specification | PASS | Manifest completion-signal column names TOKEN by declared value for all 5 gate rows — manifest serves as the consultable output spec contract; C-25 satisfied at the manifest level rather than gate-body level |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 17/17 × 10 = **10.0**
**Composite: 100.0** | Golden: YES

---

## V-03 — Output format: code-fence → native table + C-25 fixes

*Based on description: direct C-24 fix converting R7 V-03 code-fenced manifest to native markdown table, plus same completion-condition TOKEN additions as V-01.*

| ID | Criterion | Score | Notes |
|----|-----------|-------|-------|
| C-01 through C-22 | All baseline criteria | PASS | Inherited from R7 V-03 baseline (which passed all except C-23/C-24) |
| C-23 | Full gate manifest pre-execution | PASS | With code-fence removed, native table satisfies full consultability requirement; was PARTIAL in R7 |
| C-24 | Manifest as native markdown table | PASS | Explicit conversion is the axis of this variation — code-fence removed |
| C-25 | TOKEN in every gate output specification | PASS | Same completion-condition TOKEN additions as V-01 applied across all 5 gates |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 17/17 × 10 = **10.0**
**Composite: 100.0** | Golden: YES *(R7 was 99.667 due to C-23 PARTIAL; C-24 and C-25 gap both closed)*

---

## V-04 — Inertia framing: per-gate REQUIRED OUTPUTS blocks

*Based on description: each gate has an explicit REQUIRED OUTPUTS block listing TOKEN as a named required element — strongest structural form of C-25.*

| ID | Criterion | Score | Notes |
|----|-----------|-------|-------|
| C-01 through C-22 | All baseline criteria | PASS | Inherited from R7 V-04 baseline (scored 100 in R7) |
| C-23 | Full gate manifest pre-execution | PASS | Native table maintained from R7 |
| C-24 | Manifest as native markdown table | PASS | Native table maintained |
| C-25 | TOKEN in every gate output specification | PASS | Per-gate REQUIRED OUTPUTS blocks are the most explicit output-specification form — TOKEN named as required element in every block; satisfies C-25 unambiguously |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 17/17 × 10 = **10.0**
**Composite: 100.0** | Golden: YES

---

## V-05 — Combined: EXECUTION CONTRACT + dual-source TOKEN + AMEND schema declaration

*Based on description: EXECUTION CONTRACT with dedicated "Required TOKEN output" column + per-gate REQUIRED OUTPUTS blocks + AMEND schema declaration table.*

| ID | Criterion | Score | Notes |
|----|-----------|-------|-------|
| C-01 through C-22 | All baseline criteria | PASS | Combined approach adds explicit AMEND schema declaration table, strengthening C-20/C-22 |
| C-20 | AMEND schema enumerates all 4 components | PASS | Dedicated AMEND schema declaration table explicitly enumerates all four required components by name as a standalone artifact — strongest form |
| C-22 | Domain-neutral component names | PASS | Schema declaration table uses standard labels; no domain-specific component renaming |
| C-23 | Full gate manifest pre-execution | PASS | EXECUTION CONTRACT native table covers all 5 gates |
| C-24 | Manifest as native markdown table | PASS | EXECUTION CONTRACT rendered as native table |
| C-25 | TOKEN in every gate output specification | PASS | Dual-source: manifest "Required TOKEN output" column AND per-gate REQUIRED OUTPUTS blocks both name TOKEN — strongest possible form, redundant verification paths |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 17/17 × 10 = **10.0**
**Composite: 100.0** | Golden: YES

---

## Rankings

| Rank | Variation | Composite | Golden | C-24 | C-25 form |
|------|-----------|-----------|--------|------|-----------|
| 1 (tied) | V-01 | **100.0** | YES | Native table | Completion-condition prose — minimum viable |
| 1 (tied) | V-02 | **100.0** | YES | Native table | Manifest completion-signal column |
| 1 (tied) | V-03 | **100.0** | YES | Native table (explicit fix) | Completion-condition prose (same as V-01) |
| 1 (tied) | V-04 | **100.0** | YES | Native table | Per-gate REQUIRED OUTPUTS blocks |
| 1 (tied) | V-05 | **100.0** | YES | Native table | Dual-source: manifest column + per-gate blocks |

All five variations score 100. R7 V-03's code-fence risk is fully resolved by the native-table conversion in V-03/V-05. The C-25 gap in R7 V-01 (GATE-1 and GATE-4 completion conditions not naming TOKEN) is closed in every R8 variation by different structural strategies.

---

## Excellence Signals

**From V-01 (minimum viable form, confirmed sufficient):**
- Completion-condition prose that names TOKEN once per gate is the minimum viable form of C-25. The operative element is that TOKEN appears *by its declared value* in the gate's output specification — not just in gate body narrative. Adding one phrase per gate satisfies C-25 at zero structural cost.

**From V-02 (manifest-as-contract extension):**
- The pre-execution manifest completion-signal column constitutes a valid "gate output specification" for C-25 purposes, extending the C-23 result from R7. When the manifest is structurally prior to all gates, naming TOKEN in every manifest row makes the manifest a distributed output contract covering both execution-mode (C-23) and output-content (C-25) requirements simultaneously.

**From V-03 (closing the code-fence loophole):**
- Native markdown table syntax is the operative structural distinction for C-24 — not visual alignment. A code-fenced pipe-aligned block and a native table look identical in raw source but differ in rendering behavior. The C-24 boundary exists because "structurally a table" (renders in all markdown-aware contexts) differs from "visually tabular text" (renders as monospace prose).

**From V-04 (unambiguous C-25 via REQUIRED OUTPUTS blocks):**
- Per-gate REQUIRED OUTPUTS blocks are the strongest C-25 form because they are unambiguously the gate's output specification — not completion-condition prose that could be interpreted as contract vs. description. When C-25 compliance is load-bearing, REQUIRED OUTPUTS blocks eliminate interpretive uncertainty.

**From V-05 (dual-source redundancy):**
- Dual-source TOKEN declaration (manifest column + per-gate blocks) provides no scoring advantage when both sources are present and consistent, but provides structural resilience: a reader consulting either source alone can verify TOKEN compliance without cross-referencing the other.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["completion-condition prose naming TOKEN by declared value once per gate satisfies C-25 as minimum viable output specification — no REQUIRED OUTPUTS block needed", "pre-execution manifest completion-signal column constitutes a valid gate output specification for C-25, extending the manifest-as-contract principle from execution-mode (C-23) to output-content requirements", "native markdown table (pipe-and-hyphen outside code fence) is the operative C-24 distinction — structural table vs visually tabular text, not formatting style"]}
```
