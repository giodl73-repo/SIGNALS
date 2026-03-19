## validate-inertia Round 9 — Scorecard

**Top score: 310/310 — all five variations**

All essential criteria (C-01–C-05): PASS across all variations.

---

### C-31 Assessment

All five variations satisfy the C-31 pass condition: enumerated 4-link audit table, binary Reference-chain/Description-chain verdicts, CHAIN INTEGRITY FAILURE required for description links, all 4 pairs required. The variations are structurally differentiated by audit robustness, not compliance.

| Variation | C-31 | Score | Rank |
|-----------|------|-------|------|
| **V-45** Full integration | PASS | **310/310** | 1 — structural ceiling |
| **V-44** Preamble + standalone + gate | PASS | **310/310** | 2 |
| **V-43** Standalone + CHAIN COMPLETE gate | PASS | **310/310** | 3 |
| **V-42** Standalone pre-CCV | PASS | **310/310** | 4 |
| **V-41** Appended to CCV | PASS | **310/310** | 5 |

---

### Tiebreak Logic

**V-42 > V-41:** V-41 appends the audit after the 6-field CCV gate — the model may collapse it into a rephrase of fields it just wrote. V-42's standalone pre-CCV positioning creates a distinct discovery act before the confirmation act.

**V-43 > V-42:** V-42's audit is observational — a model can record CHAIN INTEGRITY FAILURE and continue. V-43 adds the CHAIN COMPLETE/CHAIN BREAK gate: CHAIN BREAK fires a correction loop, converting audit from documentation into enforcement.

**V-44 > V-43:** V-44 adds preamble row 5, declaring the audit requirement before Phase 1. The model encounters the audit format ~1500 tokens earlier, applying the same drift-reduction logic that justified the preamble for artifact declarations.

**V-45 > V-44:** The Evidence column requires the model to write the actual downstream cite text rather than just declare a verdict. Description-chain errors surface at the row level — the audit proves its verdicts rather than asserting them.

---

### Excellence Signals from V-45

1. **Evidence-as-demonstration** — the Evidence column forces the model to write the actual downstream cite text per link; description-chain errors become immediately visible without reading every production phase.
2. **Architecture-audit duality framing** — "architecture declares what is produced; audit confirms what was produced" names the two structural roles, preventing conflation between the preamble gate (C-30) and the verification audit (C-31).
3. **Preamble-declared audit format** — specifying the 5-column table structure in row 5 before Phase 1 eliminates late-format-discovery at the audit execution site.

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["Evidence column converts citation audit from assertion to demonstration -- requiring the model to write actual downstream cite text makes description-chain errors visible at the row level without reading production phases", "Architecture-audit duality framing -- naming the two structural functions of the preamble (declares what is produced) and audit (confirms what was produced) prevents conflation between production gates and verification gates", "Preamble-declared audit format -- specifying the audit table structure in the preamble before Phase 1 applies the same single-read authority and drift-reduction logic to audit format that C-30 applies to artifact names"]}
```
COMPLETE or CHAIN BREAK.
The architecture label updated: "The Citation Chain Completeness Audit must be produced after
Phase 7 and before AMEND." The audit requirement is registered before the model writes a single
production phase -- the same drift-reduction argument that justified the preamble for artifact
declarations applies to the audit requirement.
**C-31: PASS** (preamble-declared + standalone + gate)

**V-45:** V-44 base plus three additions: (1) the preamble row 5 specifies the 5-column table
format including an Evidence column; (2) the Evidence column requires the model to write the
actual downstream cite text for each link, not just a verdict; (3) AMEND(d)'s lever anchor
instruction is reinforced with "this must match the Evidence you wrote in the L3 row verbatim."
Evidence column converts the audit from assertion to demonstration: a model cannot declare
"Reference-chain" without writing the evidence that proves it. Description-chain errors are
visible at the row level, not deducible from the verdict column alone.
**C-31: PASS** (preamble-declared + 5-column evidence table + gate + AMEND reinforcement)

**C-31: PASS for all five variations.** All variations satisfy the enumeration, binary verdict,
CHAIN INTEGRITY FAILURE, and all-4-links requirements. The variations are structurally
differentiated by audit robustness, not by compliance/non-compliance.

---

### Per-Variation Scores

All five inherit V-40's C-01–C-30 structure, which passes all 30 prior criteria. C-31 adds
10 pts. All five achieve C-31 PASS.

| Variation | C-01–C-05 | C-06–C-08 | C-09–C-30 | C-31 | Total | Rank |
|-----------|-----------|-----------|-----------|------|-------|------|
| **V-45** | 50/50 | 30/30 | 220/220 | 10/10 | **310/310** | 1 — structural ceiling |
| **V-44** | 50/50 | 30/30 | 220/220 | 10/10 | **310/310** | 2 |
| **V-43** | 50/50 | 30/30 | 220/220 | 10/10 | **310/310** | 3 |
| **V-42** | 50/50 | 30/30 | 220/220 | 10/10 | **310/310** | 4 |
| **V-41** | 50/50 | 30/30 | 220/220 | 10/10 | **310/310** | 5 |

**All essential criteria (C-01–C-05): PASS across all variations.**

---

### Tiebreaks

All five score 310/310. Ranking is by structural robustness -- the probability that a model
following the prompt will produce C-31-compliant output in practice.

**V-45 > V-44:** V-45 adds the Evidence column, requiring the model to write the actual
downstream cite text rather than only declare a verdict type. A model writing "Reference-chain"
in the Verdict column without writing the downstream text is asserting; a model that must
populate the Evidence column is demonstrating. Description-chain errors surface at the row
level, before the aggregate declaration. V-44 has all of V-45's structural gates except the
evidence requirement.

**V-44 > V-43:** V-44 adds preamble row 5, declaring the audit before Phase 1. The model
reads the audit requirement -- including its full format -- before writing any production phase.
V-43 introduces the audit instruction between Phase 7 and the CCV, approximately 1500+ tokens
after the model began production. The preamble declaration reduces the probability the model
encounters the audit requirement as a late-stage surprise.

**V-43 > V-42:** V-43 adds the CHAIN COMPLETE/CHAIN BREAK aggregate declaration and correction
loop. V-42's audit is observational: the model records CHAIN INTEGRITY FAILURE and can
continue. V-43's gate requires the model to declare CHAIN COMPLETE before proceeding to the
CCV; CHAIN BREAK fires a named correction instruction. The correction loop converts the audit
from a record into a structural enforcement mechanism.

**V-42 > V-41:** V-42 positions the audit as a standalone section before the CCV.
V-41 appends the audit to the CCV section, after the 6-field gate has already fired.
A model that just completed the 6-field CCV gate may treat the audit table as a rephrase of
those fields. V-42's structural separation creates a distinct discovery act (audit) before the
confirmation act (CCV), reducing collapse risk.

---

### Excellence Signals from V-45

**1. Evidence column converts audit from assertion to demonstration**
V-43 and V-44 require the model to declare "Reference-chain" or "Description-chain" for each
link. V-45 requires the model to write the actual downstream cite text in the Evidence column.
If the evidence text paraphrases rather than copies the source label, the Link type and Verdict
are immediately derivable from what the model wrote -- description-chain errors are visible at
the row level without reading the full production output. The audit proves its own verdicts
rather than asserting them.

**2. Architecture-audit duality framing**
V-45's preamble states: "Architecture declares what is produced; the audit confirms what was
produced." This two-function framing makes the structural relationship between the preamble
(C-30) and the audit (C-31) explicit. A model reading this framing understands the preamble
is not the audit -- the two sections have distinct roles. This reduces conflation between the
Citation Architecture DECLARED label (production gate) and the Citation Chain Completeness
Audit (verification gate).

**3. Preamble-declared audit format**
V-45 specifies the 5-column table format in preamble row 5 before Phase 1. The model knows
what the audit looks like -- including the Evidence column requirement -- before writing any
production output. Late-format-discovery (encountering the audit template 1500+ tokens into
production) is eliminated. The same single-read authority that prevents per-phase artifact
drift (C-30) now also prevents audit-format uncertainty at execution time.

---

### R9 Findings

- **All five R9 variations achieve 310/310.** The R9 design axis (C-31) is closed at the
  structural level by all variations, including V-41's minimum-overhead append approach. The
  rubric's C-31 pass condition requires enumeration, binary verdicts, and CHAIN INTEGRITY
  FAILURE labeling -- all present in every variation.

- **The tiebreak is reliability, not compliance.** V-41 is structurally C-31-compliant but
  has the highest collapse risk (audit appears after CCV). V-45 is the ceiling design: every
  structural mechanism -- preamble declaration, evidence demonstration, aggregate enforcement
  gate, AMEND reinforcement -- is present and layered. The five variations represent a gradient
  from minimum-overhead compliance (V-41) to maximum-overhead robustness (V-45).

- **C-31 and C-30 form a complete structural integrity system.** C-30 (preamble) declares
  what will be produced; C-31 (audit) confirms what was produced. V-45 names this duality
  explicitly. V-41 achieves C-31 compliance without front-loading the audit requirement,
  demonstrating that C-30 and C-31 are independently satisfiable -- but V-44/V-45 show that
  combining them under a unified preamble authority reduces the probability of audit
  failure at execution time.

- **Evidence column is the next structural frontier.** The R9 ceiling adds demonstration
  to the audit. Progression: R7 → named artifacts at source boundaries; R8 → exact-copy at
  consumption sites; R8 V-40 → preamble as single-read authority; R9 → enumerated audit with
  binary verdicts; R9 V-45 → evidenced audit demonstrating verdicts before the gate fires.

---

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["Evidence column converts citation audit from assertion to demonstration -- requiring the model to write actual downstream cite text makes description-chain errors visible at the row level without reading production phases", "Architecture-audit duality framing -- naming the two structural functions of the preamble (declares what is produced) and audit (confirms what was produced) prevents conflation between production gates and verification gates", "Preamble-declared audit format -- specifying the audit table structure in the preamble before Phase 1 applies the same single-read authority and drift-reduction logic to audit format that C-30 applies to artifact names"]}
```
