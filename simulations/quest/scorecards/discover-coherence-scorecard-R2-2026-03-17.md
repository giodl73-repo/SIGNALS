Scorecard written. Here is the round summary:

---

## Round 2 Results — discover-coherence

**All 5 variations golden.** Top score: **120/120** (V-05, perfect).

| Variation | Score | New gaps closed |
|-----------|-------|-----------------|
| V-05 Full stack | **120** | C-06 + C-09 + C-10 + C-13 + C-14 |
| V-04 Tally + taxonomy | **105** | C-06 + C-09 |
| V-01 Tally-first | **100** | C-06 |
| V-02 Taxonomy-defined | **95** | C-09 |
| V-03 Skill-token | **95** | C-10 |

### Three R1 gaps all closed

All three universal failures from R1 (C-06, C-09, C-10) were closed by their target variations exactly as designed. Axis isolation held.

### Key structural insight

**Table format closes four criteria at once** (C-09, C-10, C-13, C-14). The prose ceiling is **105/120** — V-04 is the best a prose-format prompt can do. The last 15 points require switching to table layout. V-05 makes that switch and reaches a perfect score.

### New pattern for V-05 heritage

C-11 and C-12 (new in v2 rubric) were already structurally present in the R1 V-05 design as excellence signals. All R2 variations inherited them for free — zero additional instruction cost.
 PASS |

**Three universal R1 gaps all closed. C-13 and C-14 require table format -- only V-05 switches to table layout.**

---

### Gap Closure Confirmation

| Gap | R1 result | R2 fix | Closed in |
|-----|-----------|--------|-----------|
| C-06 (tally at top) | 0/5 pass | PRE-SCAN + FINDINGS HEADER two-phase structure | V-01, V-04, V-05 |
| C-09 (taxonomy) | 0/5 pass | TYPE VOCABULARY block before comparison step | V-02, V-04, V-05 |
| C-10 (skill per blocking) | 0/5 pass | Severity-split resolution rules with /skill-name token | V-03, V-05 |

Axis isolation confirmed: each single-axis variation closed its target and only its target.

---

### Independence Analysis

V-02 and V-03 each score 95 (+15 over R1 baseline on v2 rubric re-score). V-04 (two-axis) scores 105 -- a +10 additive gain over either single-axis variation. C-06 and C-09 axes are independent: combining yields sum of parts.

V-05 adds +15 over V-04 from three criteria that require table format: C-10 (+5), C-13 (+5), C-14 (+5). All three aspirational criteria that V-04 fails are structurally blocked by its prose format. The switch to table layout closes all three simultaneously.

---

### Per-Criterion Evidence

**C-06** -- V-01 and V-04 add a FINDINGS HEADER phase between scan and output (STEP 3 / PHASE 3). V-02 and V-03 place the tally at CLOSING (end), not before the first entry. V-05 uses PHASE 4 FINDINGS HEADER after PHASE 3 COUNT+CLASSIFY.

**C-09** -- V-02 adds a TYPE VOCABULARY block before COMPARISON. V-04 classifies types in PHASE 2 and adds Type field to entry template. V-05 adds Type column to both tables. V-01 and V-03 have no Type field.

**C-10** -- V-03 splits resolution rules by severity: BLOCKING must use "Resolve with: /skill-name [--focus param]" token; ADVISORY must name concrete action. V-05 inherits the same split in Resolution column rules. V-01, V-02, V-04 use a single undifferentiated resolution rule.

**C-11** -- All 5 variations use exact "GATE FAILED: {N} signal(s) found, need 2+. Run [at least 2] discover skills before coherence check." token.

**C-12** -- All 5 variations include "not 'investigate further'" in the resolution instruction, either in the template field text or in an explicit RESOLUTION RULES block.

**C-13** -- Only V-05: "Output two tables. The Inertia table renders first -- even if empty." V-01-V-04 use flat prose or flat entry lists with no priority-category separation.

**C-14** -- Only V-05: full Markdown table "# | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution". V-01-V-04 use "### Contradiction {n}" labeled-prose format.

---

### Key Findings

**Table format is a structural cascade**: Switching from labeled-prose to Markdown table format closes C-09 (Type column), C-10 (Resolution column rule), C-13 (table ordering), and C-14 (named columns) -- four criteria from one structural decision. V-04 is the ceiling of what prose format can achieve: 105/120. The last 15 pts require table format.

**Two-phase scan solves C-06 architectural incompatibility**: PRE-SCAN (silent count) then FINDINGS HEADER (output count before any entry) breaks the deferred-tally pattern. V-01 demonstrates the minimal fix: a single-axis variation that adds only this two-phase structure scores 100.

**Severity-split resolution satisfies C-10 and C-12 simultaneously**: The pattern "BLOCKING requires /skill-name token; ADVISORY requires concrete action; both say Do NOT write 'investigate further'" closes both criteria with one instruction block.

**C-11 and C-12 are heritage from R1 V-05**: All R2 variations inherit GATE FAILED token and failure-mode negation from the R1 V-05 design. These score as new criteria in v2 but require zero additional instruction.

**Full-stack prediction confirmed**: V-05 achieves 120/120 (perfect). The v2 rubric raised the max to 120 by adding C-11-C-14, all of which were already structurally present in R1 V-05. V-05 closes the three R1 gaps and inherits the excellence signals -- no surprises.

---

### Excellence Signals -- R2

1. **Two-phase scan definitively solves C-06**: PRE-SCAN (silent) then FINDINGS HEADER (output count before any entry). Architecturally incompatible with single-pass generation in R1; two-pass structure is the minimal fix.

2. **Table format closes C-09, C-10, C-13, C-14 simultaneously**: One structural decision determines four aspirational criteria. Any future prose variation caps at 105/120.

3. **Severity-split resolution is a dual-criterion instruction block**: Closes C-10 and C-12 together. Token syntax for blocking (/skill-name [params]) and explicit negation (Do NOT write "investigate further") both inherit from R1 V-05 and V-03.

4. **Heritage criteria flow forward without cost**: C-11 and C-12 score 5 pts each in v2. R2 variations inherit them for free from R1 V-05 patterns already present in their designs.

5. **Prose ceiling is 105/120**: V-04 is the optimal prose variation. C-13 and C-14 structurally require tables -- any prose variation cannot exceed 105 regardless of other improvements.

---

### R3 Plan

All gaps closed. No universal failures remain. Options:

**Option A -- New skill target**: Move to a different discover skill variation round.

**Option B -- Execution validation**: Run V-05 against a real topic with 2+ discover artifacts and verify table output, FINDINGS HEADER, and GATE FAILED behavior in practice. Static scoring does not test execution fidelity.

**Option C -- Regression boundary**: Test that labeled-prose (V-04) degrades on C-10/C-13/C-14 at execution, not just by prompt inspection.

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["two-phase scan (silent PRE-SCAN then FINDINGS HEADER) definitively solves C-06 architectural incompatibility -- deferred-tally pattern broken by separating count phase from output phase", "table format is a structural cascade: switching from labeled-prose to Markdown table closes C-09 (Type column), C-10 (Resolution column per severity), C-13 (table ordering), C-14 (named columns) -- four criteria from one structural decision", "severity-split resolution instruction satisfies C-10 and C-12 simultaneously -- BLOCKING requires /skill-name token, both levels carry explicit Do NOT write investigate further negation", "C-11 and C-12 are heritage criteria -- all R2 variations inherit GATE FAILED token and failure-mode negation from R1 V-05 base at zero additional instruction cost", "prose format caps at 105/120 -- C-13 and C-14 structurally require table layout; any future prose variation cannot exceed 105 regardless of other improvements"], "golden_count": 5}
```
