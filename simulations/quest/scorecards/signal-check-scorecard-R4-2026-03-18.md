**R4 Results:**

| Variation | Aspirational | Composite | Gold? |
|-----------|-------------|-----------|-------|
| V-01 (C-17 alone) | 9/11 | 98.18 | Yes |
| V-02 (C-18 alone) | 9/11 | 98.18 | Yes |
| V-03 (C-19 alone) | 9/11 | 98.18 | Yes |
| V-04 (C-17+C-18) | 10/11 | 99.09 | Yes |
| **V-05 (all three)** | **11/11** | **100.0** | **Yes** |

All five are gold. The three single-axis variations tied — each new criterion is independently countable and non-overlapping. V-04 = R3 V-05 confirmed at 99.09 under the v4 denominator (C-19 the only miss). V-05 closes it with the ENFORCEMENT STACK NOTE.

**Two new patterns from V-05 not yet captured as criteria:**

1. **EX-01 — Location-enumeration as named meta-rule (Rule 3):** V-04 satisfies C-16 via "Applies to:" lines on each rule. V-05 adds Rule 3 which governs rule declarations themselves, making the location-scope requirement forward-compatible — future rule additions must also enumerate locations. The meta-constraint pattern is new.

2. **EX-02 — Per-rule failure mode naming:** The ENFORCEMENT STACK NOTE assigns a failure class to each rule (absence drift / reference ambiguity / constraint scope gaps). This is separately testable from C-19: an output could name the stack without naming what each rule prevents. Failure-mode vocabulary turns the stack from a prohibition list into a diagnostic taxonomy.

→ C-20 and C-21 candidates for R5.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Location-enumeration as a named meta-rule (Rule 3) that governs rule declarations including itself -- closes forward-compatibility gap for future rule additions beyond what Applies-to lists on individual rules provide", "Per-rule failure mode naming (absence drift / reference ambiguity / constraint scope gaps) transforms enforcement stack from prohibitions list into diagnostic taxonomy -- separately testable from C-19 stack declaration"]}
```
 explicitly | PASS | PASS | PASS | PASS | PASS | Rule 1 requires in all |
| C-14 Named STANDING RULES block precedes inventory | PASS | PASS | PASS | PASS | PASS | All have STANDING RULES before GATHER YOUR SIGNALS |
| C-15 Each dimension specifies verbatim absence phrases | PASS | PASS | PASS | PASS | PASS | V-01/V-04/V-05: inline per dimension. V-02/V-03: reference table with one row per dimension -- table satisfies "dimension specifies" |
| C-16 Every constraint enumerates all output locations | PASS | PASS | PASS | PASS | PASS | V-01/V-02/V-04: Rules 1+2 each have "Applies to:" lists. V-03/V-05: Rule 3 adds "Applies to: all Rule declarations" meta-scope |
| C-17 Verbatim phrases embedded at point of use | PASS | FAIL | FAIL | PASS | PASS | V-01: inline within each dimension block. V-02/V-03: phrases in pre-analysis reference table -- model must look up rather than encounter at drafting moment |
| C-18 Advisory register carried structurally | FAIL | PASS | FAIL | PASS | PASS | V-01/V-03: "ADVISORY NOTE" disclaimer at top; technical labels (HEALTH CHECK DIMENSIONS, STATUS: OK/FLAG/OPEN, Finding:, Action:) throughout. V-02: PILOT BRIEFING, PREFLIGHT CHECK, Preflight Item N, ADVISORY STATUS: CLEAR/REVIEW/OPEN, Advisory: field. V-04/V-05: "THE PREFLIGHT CHECK" header, pilot briefing framing in READINESS SUMMARY |
| C-19 Triple enforcement stack declared as unit | FAIL | FAIL | PASS | FAIL | PASS | V-03/V-05 only: ENFORCEMENT STACK NOTE names Rules 1+2+3 as coordinated stack, enumerates each failure mode (absence drift / reference ambiguity / constraint scope gaps), states "No rule substitutes for another" |

---

### Score Summary

| Variation | Axis | Essential | Recommended | Aspirational | Composite | Gold? |
|-----------|------|-----------|-------------|-------------|-----------|-------|
| V-01 | C-17 alone | 5/5 | 3/3 | 9/11 (C-18, C-19 fail) | 98.18 | Yes |
| V-02 | C-18 alone | 5/5 | 3/3 | 9/11 (C-17, C-19 fail) | 98.18 | Yes |
| V-03 | C-19 alone | 5/5 | 3/3 | 9/11 (C-17, C-18 fail) | 98.18 | Yes |
| V-04 | C-17 + C-18 | 5/5 | 3/3 | 10/11 (C-19 fails) | 99.09 | Yes |
| V-05 | C-17+C-18+C-19 | 5/5 | 3/3 | 11/11 | 100.0 | Yes |

Rank: V-05 > V-04 > V-01 = V-02 = V-03

---

### Confirmed Hypotheses

**H1 (C-17 vs reference table):** Confirmed. V-01 passes C-17 with inline phrases; V-02 fails C-17
with reference table. Inline placement is the discriminator independently of whether structural
framing is present. C-17 and C-18 are separately countable.

**H2 (C-18 structural framing):** Confirmed. V-02 passes C-18 with PILOT BRIEFING / Preflight Item N
/ ADVISORY STATUS vocabulary; V-01 fails with top-of-file ADVISORY NOTE only. Structural vocabulary
in section labels prevents register drift where a disclaimer cannot.

**H3 (C-19 stack declaration):** Confirmed. V-03 passes C-19 with ENFORCEMENT STACK NOTE; V-01 and
V-02 fail. Explicitly naming three rules as addressing independent failure modes adds robustness
independently of phrase placement and structural framing.

**V-04 floor confirmed:** R3 V-05 scores 10/11 aspirational under v4 denominator (C-09 through C-18
pass, C-19 fails). Composite 99.09. No change from expected.

---

### Excellence Signals from V-05

**EX-01: Location-enumeration as a named meta-rule.**
V-04 satisfies C-16 because Rules 1 and 2 each carry "Applies to:" lists. V-05 adds Rule 3
("CONSTRAINTS ARE LOCATION-COMPLETE") as an explicit named rule that self-applies ("Applies to: all
Rule declarations in this STANDING RULES block"). This closes a forward-compatibility gap: in V-04,
adding a future Rule 4 would not automatically require it to enumerate locations. Rule 3 makes the
requirement durable against future rule additions. The meta-constraint pattern -- a rule that governs
rule declarations -- does not appear in any variation before V-05 and is not yet captured as a
criterion.

**EX-02: Per-rule failure mode naming as diagnostic vocabulary.**
The ENFORCEMENT STACK NOTE in V-05 assigns a specific failure class to each rule: absence drift
(Rule 1), reference ambiguity (Rule 2), constraint scope gaps (Rule 3). This transforms the
enforcement stack from a list of prohibitions into a diagnostic taxonomy. A reviewer classifying a
violation can map it to a failure mode type from the rule name alone, without reading the full rule
body. Naming failure modes is distinct from naming the interdependency (C-19): an output could
satisfy C-19 by declaring the three-rule stack without enumerating what each rule prevents. The
failure-mode naming pattern is separately testable.

---

### Research Questions for R5

1. **C-20 candidate -- Rule 3 meta-constraint**: Does explicitly stating Rule 3 (location-enumeration
   as a named rule that governs rule declarations, including itself) improve compliance durability
   beyond having Rules 1 and 2 carry "Applies to:" lists independently? V-04 satisfies C-16 without
   Rule 3; V-05 adds it. Tests whether the meta-constraint makes the location-enumeration requirement
   forward-compatible with future rule additions.

2. **C-21 candidate -- per-rule failure mode naming**: Does naming each rule's failure class in the
   ENFORCEMENT STACK NOTE (absence drift / reference ambiguity / constraint scope gaps) improve
   violation detection and classification compared to naming the interdependency without failure-mode
   taxonomy? Tests whether diagnostic vocabulary is independently contributive beyond the stack
   declaration already captured by C-19.
