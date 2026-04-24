## R17 Scoring — corps-rob (Rubric v16)

### Methodology

All five R17 variations share the R16 V-05 proven base. The base already satisfies all explicitly named v16 aspirational criteria (C-09 through C-48), all recommended (C-06 through C-08), and all essential (C-01 through C-05). Scoring delta comes only from whether H-D, H-E, or H-F resolves the persistent unnamed gap criterion (tracked as a 5-point implicit deduction in the v16 composite since R14).

---

### Criteria Pass/Fail — All Variations Share Base

**Essential (C-01–C-05):** PASS in all five variations.

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage Identity and Labeling | PASS | Stage header template: `## Stage: [stage-name]` |
| C-02 | Role-Loaded Perspective | PASS | `ROLE: [name] \| Frame: [...] \| Lens: [...]` required per-stage |
| C-03 | ROB Document Format Compliance | PASS | Findings + Verdict + TPM summary structure enforced |
| C-04 | Actionable Findings (2x per stage) | PASS | "minimum 2 findings per stage; severity must vary" explicit |
| C-05 | Go/No-Go Signal in TPM Stage | PASS | `Go/No-Go` table required in TPM stage template |

**Recommended (C-06–C-08):** PASS in all five variations.

| ID | Criterion | Status | Evidence |
|----|-----------|--------|----------|
| C-06 | Cross-Stage Coherence | PASS | CARRY FORWARD + Inherits: pattern; 5 carry sites in 6-stage run |
| C-07 | Structured Risk Register in TPM | PASS | Risk register ≥3 rows, severity/likelihood/mitigation columns required |
| C-08 | Exec-Office Cascade Tracing | PASS | SPIRE stage Mission Cascade table; "named mission required" stated |

**Aspirational C-09 through C-48 — Abbreviated (all from base):**

| ID | Criterion | All Variations |
|----|-----------|---------------|
| C-09 | Inter-Stage Blocker Detection | PASS — RULE BLOCKER-PROTOCOL min 1 named BLOCKER per run |
| C-10 | Cross-Cutting Theme Elevation | PASS — doc-level cross-cutting themes template present |
| C-11 | Conditional Verdict Itemization | PASS — RULE CONDITIONAL-ITEM numbered items (1)(2)(3) |
| C-12 | Finding Severity Discrimination | PASS — "severity must vary" instruction explicit |
| C-13 | Risk Register Status Lifecycle | PASS — OPEN/WATCH/MITIGATED column required |
| C-14 | Pre-Finding Severity Calibration | PASS — Calibration Block with HIGH DRIVER/LOW ANCHOR/DISTRIBUTION FACTOR |
| C-15 | Risk Register Update Protocol | PASS — Risk Register Update Protocol table required |
| C-16 | Role-Lens Pre-Declaration | PASS — ROLE LENS field before first finding |
| C-17 | Pre-Commitment Enforcement Audit | PASS — POST-STAGE AUDIT SUITE with three named audit sections |
| C-18 | Universal Per-Stage Triage Note | PASS — Triage Note required in every stage template |
| C-19 | Zero-Deviation Explicit Declaration | PASS — RULE ZERO-STATE governs VIOLATIONS: NONE / GAPS: NONE |
| C-20 | Enforcement Audit Structured Table | PASS — named-column table (Stage/Pre-Commitment/Honored/Deviation) |
| C-21 | Named Triage Field Vocabulary | PASS — HIGH DRIVER: / LOW ANCHOR: / DISTRIBUTION FACTOR: |
| C-22 | Post-Stage Role-Concern Gap Scan | PASS — ROLE CONCERN AUDIT [Section 2, RULE BOOKEND-AUDIT] |
| C-23 | Post-Stage Triage Note Gap Scan | PASS — TRIAGE NOTE AUDIT [Section 3, RULE BOOKEND-AUDIT] |
| C-24 | Multi-Type Post-Stage Audit Suite | PASS — three distinct scope sections in RULE AUDIT-SUITE |
| C-25 | Triage Note Field-Level Compliance Audit | PASS — (a)/(b)/(c) three failure conditions per stage in audit |
| C-26 | Named Audit Rule with Anti-Pattern | PASS — RULE AUDIT-SUITE with Anti-pattern-1 and Anti-pattern-2 |
| C-27 | Gap-Scan Absence as Format Error | PASS — RULE BOOKEND-AUDIT: "Absence is a FORMAT VIOLATION" |
| C-28 | Named Field-Level Audit Schema | PASS — TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) labeled conditions |
| C-29 | Enumerated Condition Zero-State | PASS — AUDIT RESULT block with (a) NONE / (b) NONE / (c) NONE |
| C-30 | Run-Level Preamble Schema with Named Post-Stage Reference | PASS — schema declared in preamble; post-stage sections reference "preamble declaration applies" |
| C-31 | Rule Citation Anchors in Post-Stage Section Headers | PASS — `[RULE AUDIT-SUITE, Section 1]` and `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]` in headers |
| C-32 | Carry-Forward Structural Artifact | PASS — RULE CARRY-FORWARD; Inertia ID column; CARRY: NONE zero-state |
| C-33 | Synthesis Non-Audit Declaration | PASS — RULE SYNTHESIS: "NOT an audit section; does NOT count toward RULE AUDIT-SUITE" |
| C-34 | Conditional Item vs Condition Enum Disambiguation | PASS — "[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]" annotation |
| C-35 | Audit Table Additive-Not-Replacement Constraint | PASS — "inserted ABOVE the AUDIT RESULT block -- NOT replacing it" |
| C-36 | Synthesis Positive-Artifact Subsection Schema | PASS — 5 named required subsections in RULE SYNTHESIS |
| C-37 | Dual Illustrative Baseline Examples | PASS — IB-01 (technical: Status-Quo/Incumbent Forces/Displacement Cost/Validity Window) and IB-02 (organizational: Adopted Behavior/Resistance Source/Adoption Cost/Urgency Gradient/Validity Window) — structurally distinct field sets |
| C-38 | Carry Forward Inertia-ID Attribution Column | PASS — Inertia ID column in Carry Forward table template |
| C-39 | IB-02 Urgency Gradient Downstream Citation Cascade | PASS — RULE IB-URGENCY-CASCADE with three named cascade constraints (Go/No-Go, Risk Register, Inertia Pressure Summary) |
| C-40 | Named Rule Glossary Exclusivity Declaration | PASS — "exclusive locus" self-declaration in glossary header |
| C-41 | RULE AUDIT-TABLE Named Anti-Pattern Declaration | PASS — "Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's per-condition enumeration" |
| C-42 | Glossary Exclusivity Named-Criterion Enumeration | PASS — enumerates C-30 and C-34 by label |
| C-43 | Criterion Enumeration Label-Plus-Description Pairing | PASS — "C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)" and "C-34 (Conditional Item vs Condition Enum Disambiguation)" |
| C-44 | AUDIT RESULT Block Independence Declaration | PASS — RULE AUDIT-INDEPENDENCE governs unconditional mandatory status; satisfied via dedicated rule as required by C-47 |
| C-45 | Exclusivity Declaration Protected-Count Annotation | PASS — "Exactly 2 criteria require glossary scope -- any addition of a third... requires an explicit count update" |
| C-46 | RULE AUDIT-TABLE Bidirectional Condition Enumeration | PASS — RULE AUDIT-INDEPENDENCE: branch (1) table present; branch (2) table absent; both enumerated |
| C-47 | RULE AUDIT-INDEPENDENCE Named-Rule Decomposition | PASS — RULE AUDIT-TABLE sheds independence clause; RULE AUDIT-INDEPENDENCE is a separate named rule owning the two-branch enumeration |
| C-48 | RULE AUDIT-INDEPENDENCE Escalation-Boundary Annotation | PASS — "A single 'mandatory regardless of table presence' clause satisfies C-44 but not C-46 -- only explicit enumeration of both branches as separate numbered items satisfies C-46" |

**Persistent gap criterion (unnamed, present since R14):** FAIL in all five variations.

---

### Variation-Specific Delta Analysis

**V-01 (H-D: RULE ZERO-STATE Anti-pattern)**

Delta from base: RULE ZERO-STATE gains labeled Anti-pattern naming the silent-last-row disqualifying form. No existing v16 criterion explicitly requires RULE ZERO-STATE to have a labeled anti-pattern field. C-19 (zero-state declaration) passes via RULE ZERO-STATE's positive mandate regardless of whether an Anti-pattern is declared. H-D improves structural symmetry (RULE ZERO-STATE now matches the anti-pattern discipline of other governing rules) but does not satisfy any currently failing v16 criterion.

**V-02 (H-E: RULE VIOLATION-TAXONOMY elevation)**

Delta from base: RULE VIOLATION-TAXONOMY added to glossary, governing the violation taxonomy with structural element (ID/Description/Consequence), series-state constraint, and two anti-patterns. No existing v16 criterion explicitly requires the violation taxonomy to be governed by a named rule. The closest candidates (C-26 requiring RULE AUDIT-SUITE to have anti-patterns, C-41 requiring RULE AUDIT-TABLE to have anti-patterns) are already satisfied by the base. H-E closes the last ungoverned-artifact gap but maps to no failing v16 criterion.

**V-03 (H-F: RULE PHASE-GATE second Anti-pattern)**

Delta from base: RULE PHASE-GATE gains Anti-pattern-2 naming the category-citation-without-instance disqualifying form. No existing v16 criterion explicitly requires RULE PHASE-GATE to have two labeled anti-patterns. C-09 (inter-stage blocker detection) passes via RULE BLOCKER-PROTOCOL regardless. H-F closes the RULE PHASE-GATE structural asymmetry (peer rules RULE BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, RULE AUDIT-SUITE all have two anti-patterns) but maps to no failing v16 criterion.

**V-04 (H-D + H-E)**

Delta: V-01 + V-02 combined. Neither H-D nor H-E resolves the persistent gap individually; combined they do not produce a synergistic effect on any v16 criterion.

**V-05 (H-D + H-E + H-F full target)**

Delta: All three hypotheses combined. Same conclusion: no v16 criterion transitions from FAIL to PASS. V-05 achieves the broadest structural coverage of any R17 variation but produces the same composite as V-01 through V-04.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational (C-09–C-48) | Persistent Gap | Composite |
|-----------|-----------|-------------|--------------------------|----------------|-----------|
| V-01 | PASS (all 5) | PASS (all 3) | PASS (all 40) | FAIL | **285/290** |
| V-02 | PASS (all 5) | PASS (all 3) | PASS (all 40) | FAIL | **285/290** |
| V-03 | PASS (all 5) | PASS (all 3) | PASS (all 40) | FAIL | **285/290** |
| V-04 | PASS (all 5) | PASS (all 3) | PASS (all 40) | FAIL | **285/290** |
| V-05 | PASS (all 5) | PASS (all 3) | PASS (all 40) | FAIL | **285/290** |

**All five variations tie at 285/290.** The persistent gap criterion remains unresolved. Hypotheses H-D, H-E, and H-F are structurally sound improvements but none maps to a currently failing v16 criterion. R18 requires a different probe space.

---

### Ranking

All five variations rank equally at 285/290. V-05 is the preferred carry-forward for R18 due to broadest structural coverage (RULE ZERO-STATE Anti-pattern + RULE VIOLATION-TAXONOMY + RULE PHASE-GATE Anti-pattern-2 all incorporated).

---

### Excellence Signals from V-05

Three structural patterns in V-05 represent genuine improvements even without scoring impact under v16. These are candidates for v17 rubric criteria:

**Signal 1 — RULE ZERO-STATE labeled Anti-pattern (H-D)**
V-05's RULE ZERO-STATE adds: "A section whose last line is a populated entry row or list item -- with no explicit labeled zero-state line following it -- does not satisfy this rule, even when all entries in that row indicate no deviation." This parallels C-41's discipline on RULE AUDIT-TABLE applied to RULE ZERO-STATE: the positive mandate ("silence is not clean") is now paired with a named failure mode. A generator encountering RULE ZERO-STATE can now distinguish the compliant form from the adjacent-but-wrong form (table row with no-deviation column not followed by a separate zero-state line) without consulting the rubric. Structural asymmetry eliminated: every named rule governing an output artifact now has a labeled Anti-pattern.

**Signal 2 — RULE VIOLATION-TAXONOMY governing the violation taxonomy artifact (H-E)**
V-05 introduces RULE VIOLATION-TAXONOMY as the first governing rule for the violation taxonomy. Prior to H-E, the taxonomy was the only structural artifact in the format spec without a named governing rule — every other artifact (FINDING LEDGER, CARRY FORWARD, BLOCKER records, SYNTHESIS, audit sections, inertia baselines) had a named rule with structural element and anti-pattern. RULE VIOLATION-TAXONOMY closes this by declaring: structural element (ID/Description/Consequence), series-state constraint (terminator line "Current series: VIOLATION-01 through VIOLATION-NN"), Anti-pattern-1 (violation without Consequence annotation), Anti-pattern-2 (taxonomy without series-state terminator). The series-state constraint is novel: it makes the violation set closed and completeness-verifiable per run. A generator knows whether the taxonomy is exhaustive by checking the terminator line. This is the only non-artifact governing rule in the glossary (the taxonomy governs other artifacts' violations but is itself a structural artifact of the format spec).

**Signal 3 — RULE PHASE-GATE second Anti-pattern naming the adjacent-but-wrong form (H-F)**
V-05 adds Anti-pattern-2 to RULE PHASE-GATE: "ENTRY or EXIT condition that cites an artifact category or severity tier (e.g., 'all HIGH findings from teams', 'any open risk') without a specific LID or risk ID from the current run -- the category may be populated but the specific instance is unverifiable against the FINDING LEDGER or risk register." This distinguishes clearly-generic language (Anti-pattern-1: "all inputs ready") from falsifiable-in-appearance-but-unverifiable-against-artifacts language (Anti-pattern-2: "all HIGH findings from teams"). Anti-pattern-2 names the form that satisfies the spirit of specificity (a category is named) while remaining structurally unchecked (no LID, no FINDING LEDGER anchor). Peer rules RULE BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, and RULE AUDIT-SUITE all have two labeled anti-patterns; RULE PHASE-GATE now achieves the same structural parity.

---

### R18 Probe Direction

All three R17 hypotheses (H-D/H-E/H-F) were in the named-rule structural-completeness space. Their elimination confirms: the persistent gap is not resolvable by adding Anti-patterns to existing rules or adding governing rules for ungoverned artifacts. The gap lies in a structural dimension not yet probed. R18 candidates:

- **H-G**: RULE CARRY-FORWARD or RULE FINDING-LEDGER structural completeness (Inertia-ID tagging in the ledger itself vs. only in the carry block; cross-ledger verification)
- **H-H**: Phase Gate anti-pattern propagation — RULE STAGE-HANDOFF currently has a Zero-state declaration for the first stage but no analogous Zero-state governing the final stage's EXIT condition (no downstream stage to certify)
- **H-I**: SYNTHESIS subsection governs its own completeness via RULE SYNTHESIS (C-36) but BLOCKERS subsection within SYNTHESIS has no named minimum count constraint analogous to RULE BLOCKER-PROTOCOL's "minimum 1 named BLOCKER per full run"

---

```json
{"top_score": 285, "all_essential_pass": true, "new_patterns": ["RULE ZERO-STATE labeled Anti-pattern naming the silent-last-row disqualifying form -- positive mandate paired with named failure mode; structural parity with C-41 RULE AUDIT-TABLE and C-26 RULE AUDIT-SUITE anti-pattern discipline now achieved for zero-state governing rule", "RULE VIOLATION-TAXONOMY as first named governing rule for the violation taxonomy artifact -- structural element (ID/Description/Consequence), series-state terminator constraint, two anti-patterns; closes the last ungoverned-artifact gap; series-state makes violation set completeness-verifiable per run", "RULE PHASE-GATE second Anti-pattern naming the category-citation-without-instance form -- distinguishes clearly-generic language (Anti-pattern-1) from falsifiable-in-appearance-but-LID-unverifiable language (Anti-pattern-2); achieves two-anti-pattern structural parity with RULE BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, and RULE AUDIT-SUITE"]}
```
