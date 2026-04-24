# Quest Score — corps-pr Round 2

**Rubric**: v2 | **Variations**: V-01 through V-05 | **Date**: 2026-03-16

---

## Per-Variation Criterion Evaluation

### V-01 — Inertia Framing: Advocate-First Baseline

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | ROUTING TABLE with file-group → org.yaml role → selection reason. "Every changed file must appear in a row." Coverage gap rule explicit. |
| C-02 | **PASS** | Inertia Advocate + technical roles each require F-ID + P1/P2/P3 severity per finding. Summary line mandatory. |
| C-03 | **PASS** | CONSENSUS ANALYSIS template covers all three: Inertia baseline status, Agreement, Divergence+Mechanism, Critical finding. |
| C-04 | **PASS** | RECOMMENDATION requires one of GO/NO-GO/GO WITH CONDITIONS, cites specific F-XX. Conditions include sign-off role. |
| C-05 | **PASS** | Validity check: "could only this role have raised it?" Inertia Advocate mandate covers the status-quo finding requirement. |
| C-06 | **PASS** | Coverage Gap entry defined. |
| C-07 | **PASS** | "Summary: [N] findings — [x] P1, [y] P2, [z] P3" required in every section. |
| C-08 | **PASS** | AMEND section with scope disclosure format. |
| C-09 | **PASS** | Divergence template requires "Mechanism: [structural or architectural property of the code causing this rating difference]." |
| C-10 | **PASS** | GO WITH CONDITIONS template includes "sign-off: [role who confirms resolution before merge]." |
| C-11 | **PASS** | "STEP 2 — INERTIA ADVOCATE (runs first, always)" — explicitly structural, appears before STEP 3. |
| C-12 | **PARTIAL** | Mechanism field required in template (positive instruction), but no explicit prohibition of perspective-label phrases. A model could still write "they have different perspectives" alongside a mechanism name. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 3.5/4 = 8.75
**Composite: 98.75** | All essential pass: YES

---

### V-02 — Output Format: Table-Centric

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | TABLE 1 ROUTING with every file required as a row. Coverage gap sub-table defined. "Missing file is a hard fail." |
| C-02 | **PASS** | TABLE 2 per-role findings with Severity column (P1/P2/P3 enum). Minimum 2 data rows. "Severity must vary." |
| C-03 | **PASS** | TABLE 3 CONSENSUS with Agreement/Divergence/Critical rows. "Zero data rows fails." |
| C-04 | **PASS** | TABLE 4 RECOMMENDATION with Decision enum. "'The team should consider' fails." Sign-off Role column. |
| C-05 | **PARTIAL** | Column contract requires naming specific function/module ("authentication concern fails"). But no domain-lens validation check — a generic reviewer could write a specifically-named finding. No Inertia Advocate requirement (C-05 clause N/A, but domain-specificity enforcement is weaker). |
| C-06 | **PASS** | Coverage Gap sub-table defined. |
| C-07 | **PASS** | TOTAL row structurally required — most reliable enforcement of C-07 of any variation. |
| C-08 | **PASS** | AMEND SCOPE block with Roles added/removed/superseded fields. |
| C-09 | **PARTIAL** | TABLE 3 Mechanism/Notes column present. Table format constrains explanation to a single cell, limiting depth of root cause synthesis. |
| C-10 | **PASS** | Sign-off Role column in TABLE 4 for GO WITH CONDITIONS. |
| C-11 | **PASS by default** | Inertia Advocate not included as a required reviewer. |
| C-12 | **PARTIAL** | TABLE 3 note: "'They have different priorities' fails" — one prohibited phrase named, not a comprehensive list. |

**Essential**: 4.5/5 = 54 | **Recommended**: 3/3 = 30 | **Aspirational**: 3/4 = 7.5
**Composite: 91.5** | All essential pass: NO (C-05 partial)

---

### V-03 — Phrasing Register: Descriptive/Role-Oriented

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | "Who reviews this PR:" bullet list maps files to roles with org.yaml reason. "Don't skip files." |
| C-02 | **PASS** | Per-reviewer section with F-ID, P1/P2/P3, minimum 2 findings, summary line. |
| C-03 | **PARTIAL** | "Consensus Analysis" in 2–4 prose sentences covers convergence and divergence + mechanism, but does not explicitly require surfacing the single most critical finding across all roles. Third element of C-03 is absent from the template. |
| C-04 | **PASS** | "## Recommendation" with one of GO/NO-GO/GO WITH CONDITIONS. "No hedging." Sign-off for conditions. |
| C-05 | **PASS** | Strongest domain-lens activation: "if a finding reads exactly the same regardless of which role wrote it, it isn't carrying its reviewer's lens. Revise it until it does." Security/compiler role behaviors described in first-person depth. No Inertia Advocate selected (C-05 clause N/A). |
| C-06 | **PASS** | "No role covers [path] — coverage gap in org.yaml." |
| C-07 | **PASS** | "[N] findings — [x] P1, [y] P2, [z] P3" at end of each reviewer section. |
| C-08 | **PASS** | AMEND prose with "say what role was added, which files triggered the addition, which prior findings superseded or unchanged." |
| C-09 | **PASS** | "Work out why — not because they have different jobs (that's obvious), but what specific property of the code makes one of them see a P1 and the other see a P3." Explicit rejection of the trivial answer. |
| C-10 | **PASS** | "Conditions (if applicable): [what must be resolved] — sign-off: [role who confirms]." |
| C-11 | **PASS by default** | No Inertia Advocate required. |
| C-12 | **PARTIAL** | Positive instruction only: "name the structural or architectural reason." No prohibited phrases listed. |

**Essential**: 4.5/5 = 54 | **Recommended**: 3/3 = 30 | **Aspirational**: 3.5/4 = 8.75
**Composite: 92.75** | All essential pass: NO (C-03 partial)

---

### V-04 — Role Sequence + Lifecycle Emphasis: Explicit Phase Gates

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | PHASE 1 ROUTE with routing table + Coverage Gap section. Hard exit condition: "every changed file assigned to a role or explicitly flagged." Phase 2 may not begin until this step is done. |
| C-02 | **PASS** | PHASE 2 REVIEW: per-role findings with F-ID, P1/P2/P3, Summary line. "Phase 2 complete when every role from the routing table has a section." |
| C-03 | **PASS** | PHASE 3 SYNTHESIZE explicitly identifies all three: Agreement, Divergence, Critical finding. |
| C-04 | **PASS** | PHASE 4 DECIDE: one of three decisions, "delegated or ambiguous decisions fail." Sign-off role for conditions. |
| C-05 | **PASS** | Validation per finding: "does it reflect this role's domain lens — not something any reviewer could have written?" Inertia Advocate conditional-first if in routing table. |
| C-06 | **PASS** | Coverage Gap section in PHASE 1. |
| C-07 | **PASS** | "Summary: [N] findings — [x] P1, [y] P2, [z] P3" required per role. |
| C-08 | **PASS** | AMEND: "Disclose at output start: what role was added, which files triggered the addition." Scope change: "which prior findings are superseded." |
| C-09 | **PASS** | "For any divergence found: explain the structural or architectural reason... Name the property of the code that causes one role to see P1 and another to see P3. Do not use perspective-label explanations ('they prioritize differently')." |
| C-10 | **PASS** | Conditions with "sign-off: [role who confirms resolution before merge]." |
| C-11 | **PASS** | Inertia Advocate runs before all others when present; passes by default when absent (conditional is satisfied either way). |
| C-12 | **PARTIAL** | One example of prohibited phrase given ("they prioritize differently"). Consensus template has "not a perspective label" constraint. Not as comprehensive as V-05's exhaustive prohibition list. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 3.5/4 = 8.75
**Composite: 98.75** | All essential pass: YES

---

### V-05 — Inertia Framing + Consensus Mechanism (Combination)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | STEP 1 ROUTING TABLE with file-group → role → scope match. Coverage gap rule: "Do not silently omit." |
| C-02 | **PASS** | Inertia Advocate + technical roles each with F-ID, P1/P2/P3, Summary line. Minimum 2 findings per section. |
| C-03 | **PASS** | STEP 4 CONSENSUS has explicit A/B/C/D structure: Inertia status (A), Agreement (B), Divergence with mechanism (C), Critical finding (D). All three rubric sub-requirements covered. |
| C-04 | **PASS** | STEP 5 RECOMMENDATION: GO/NO-GO/GO WITH CONDITIONS, Primary reason cites F-XX. Sign-off roles in conditions. |
| C-05 | **PASS** | "Validity check: if a finding could have been written by any reviewer regardless of their role, revise it until it carries the domain lens." Inertia Advocate structural mandate. Domain examples provided. |
| C-06 | **PASS** | Coverage Gap rule explicit. |
| C-07 | **PASS** | Summary line in every section including Inertia Advocate. |
| C-08 | **PASS** | AMEND section with "Prior findings superseded by this addition: [F-IDs or 'none']." |
| C-09 | **PASS** | Divergence section requires mechanism explanation; "valid divergence explanation format" given as template. |
| C-10 | **PASS** | Conditions require "sign-off: [role who confirms before merge]" — structurally embedded in template. |
| C-11 | **PASS** | "STEP 2 — INERTIA ADVOCATE (always runs first)" — "This is structural — not a default that can be overridden." |
| C-12 | **PASS** | Explicit "Prohibited divergence explanations" block lists 4 specific banned phrases plus catch-all "any equivalent phrase." Valid format provided with bidirectional code-property example for both roles. Only variation to fully pass C-12. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Composite: 100** | All essential pass: YES

---

## Score Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite | All Essential |
|------|-----------|-----------|-------------|--------------|-----------|---------------|
| 1 | **V-05** | 60 | 30 | 10.00 | **100** | YES |
| 2 (tie) | V-01 | 60 | 30 | 8.75 | **98.75** | YES |
| 2 (tie) | V-04 | 60 | 30 | 8.75 | **98.75** | YES |
| 4 | V-03 | 54 | 30 | 8.75 | **92.75** | NO |
| 5 | V-02 | 54 | 30 | 7.5 | **91.5** | NO |

---

## Excellence Signals from V-05

**What separated V-05 from V-01 and V-04** (both 98.75) was sole full passage of C-12.

**Signal 1 — Enumerated prohibition with catch-all**: V-05's prohibited phrase list names four specific patterns and adds "any equivalent phrase that attributes the divergence to role identity rather than code property." This dual structure (specific examples + principle) is harder to pattern-match around than a single example. V-01 and V-04 both give positive instructions ("name the mechanism") but leave the prohibited territory undescribed.

**Signal 2 — Bidirectional divergence explanation**: V-05's valid format template requires explaining BOTH sides: why role-A rates it P1 *and* why role-B rates it P3, each naming a distinct code property from their respective lens. Other variations only instruct the model to name "the reason" for divergence (implicitly one-sided). The bidirectional format prevents the model from explaining only the dissenting view.

**Signal 3 — Inertia feedback loop in consensus**: V-05's consensus STEP 4-A explicitly labels whether technical findings "confirmed / partially challenged / defeated" the Inertia Advocate's null hypothesis. This creates a closed loop: Inertia Advocate sets baseline in Step 2; consensus reconciles against it in Step 4A. V-01 has a similar field but without the three-value label, making the reconciliation less structured.

---

## New Patterns for Round 3 Consideration

These patterns from V-05 exceed the current rubric criteria and are candidates for C-13/C-14:

- **Bidirectional mechanism explanation**: Both sides of a divergence receive equal causal treatment — why role-A rates P1 AND why role-B rates P3, each naming the specific code property from their lens. One-sided divergence explanations (naming only why the higher severity is justified) leave the lower-severity rating unexplained.
- **Inertia feedback loop in consensus**: The consensus section explicitly labels whether technical findings confirmed, partially challenged, or defeated the null hypothesis baseline. This transforms the Inertia Advocate from a sequencing element into a testable claim that the rest of the run resolves — and makes the consensus section a baseline reconciliation step rather than a summary.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Bidirectional mechanism explanation: both sides of a divergence receive equal causal treatment — why role-A rates P1 AND why role-B rates P3, each naming the specific code property from their lens, rather than explaining only the dissenting rating", "Inertia feedback loop in consensus: the consensus section explicitly labels whether technical findings confirmed, partially challenged, or defeated the null hypothesis baseline, turning the Inertia Advocate section into a testable claim that the rest of the run resolves"]}
```
