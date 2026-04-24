rubric = """\
# flow-trigger rubric v7

Rubric for evaluating trigger analysis outputs produced by the `flow:trigger` skill.
Version history in footer.

---

## Essential Criteria (60% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Trigger enumeration completeness** | coverage | All triggers that fire given the described change scenario are listed. No triggers that would fire under the scenario are omitted. Evaluated against a hand-compiled ground truth when available; against structural completeness of the trace when not. |
| C-02 | **Correct firing determination** | behavior | Each listed trigger is correctly determined to fire or not fire under the given scenario. Triggers that do not fire under the scenario are excluded from the inventory; if included, they are explicitly marked as non-firing with reasoning. |
| C-03 | **I/O specificity** | behavior | For each firing trigger: input identifies the specific record entity and field(s) that caused the trigger; output identifies the specific action taken (field updated, email sent, HTTP call made, etc.) with named targets. Generic descriptions ("processes the record", "updates the system") are partial fails. |
| C-04 | **Pathology coverage** | coverage | The output addresses all three pathology classes: trigger storm risk, missing trigger risk, and circular trigger risk. Claiming absence of a pathology is valid; silently omitting a pathology class is not. |
| C-05 | **No false positives** | coverage | No trigger that does not fire under the given scenario is presented as firing. Each entry in the trigger inventory corresponds to an actual firing event traceable to the scenario inputs. |

---

## Recommended Criteria (30% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Side effect chain** | depth | Side effects that cascade beyond the immediate trigger (e.g., trigger A writes a field, which fires trigger B) are traced at least one level deep. The chain is shown as a sequence, not just mentioned. |
| C-07 | **Conditional branch coverage** | coverage | If any trigger has a condition (runs only when field X = value Y), the output identifies what branch executes under the given change scenario and what branch is skipped and why. |
| C-08 | **Platform vocabulary** | behavior | Output uses Power Automate / Copilot Studio vocabulary correctly: flow types (instant, automated, scheduled), connector names, trigger event names (e.g., "When a row is added, modified or deleted"). Generic automation vocabulary without platform grounding is a partial fail. |

---

## Aspirational Criteria (10% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk-ranked pathology summary** | depth | Identified pathologies are ranked by operational risk (e.g., circular trigger ranked higher than redundant notification). Each risk includes a one-line mitigation suggestion. |
| C-10 | **Timing and latency annotations** | depth | The output distinguishes synchronous triggers (block the transaction) from asynchronous triggers (fire-and-forget) and notes any latency implications (e.g., "runs within 5 minutes in Power Automate standard tier"). |
| C-11 | **Pre-enumeration ghost denominator** | technique | The output runs a candidate pre-scan *before* the trigger list, naming expected trigger candidates from the graph. The final enumeration then reconciles against those candidates -- any candidate not found is explicitly resolved (confirmed absent or flagged as missing). This two-pass structure catches omissions by construction rather than by inspection. Pre-scan must precede enumeration; post-hoc reconciliation does not count. |
| C-12 | **Format-enforced structural falsifiability** | technique | The trigger inventory is presented in a table with required columns (e.g., Trigger Name, Firing Order, Input Payload, Output Action, Side Effects). Empty cells in required columns are structurally visible as failures, making omissions and false positives undeniable without requiring prose evaluation. A table with only Trigger Name and Description does not pass -- all dedicated columns must be present and populated. |
| C-13 | **Anti-example vocabulary anchoring** | technique | The output names at least one explicit bad-form/good-form pair for platform vocabulary or I/O specificity (e.g., "DO NOT write 'processes the record' -- write 'sets Status to Approved on the Request table'"). Named anti-examples calibrate the specificity bar in a way that positive guidance alone does not. Examples must reference actual platform vocabulary or actual payload names, not generic writing quality. |
| C-14 | **Sync/async tier separation as structure** | technique | Sync and async triggers are enumerated in physically distinct sections or tables (e.g., Sync Tier / Async Tier), not interleaved with inline timing annotations. Every trigger is assigned to exactly one tier at enumeration time. Each tier includes a reconciliation summary (registered count vs firing count), making cross-tier misclassification structurally visible. |
| C-15 | **Multi-domain vocabulary contract** | technique | A governing preamble (e.g., VOCABULARY CONTRACT) defines multiple domain-specific term sets -- at minimum: trigger type names, I/O payload field names, output action verbs, and pathology forms -- before any enumeration begins. All subsequent sections must conform to these definitions. This criterion requires a structured multi-domain model, not a single bad/good pair (C-13 covers that). |
| C-16 | **Absence-requires-evidence pathology clearance** | depth | For each of the three pathology classes (storm, missing trigger, circular), claiming absence must be backed by explicit reasoning or structural evidence (e.g., "No circular triggers -- trigger graph is a DAG with no back-edges"). A bare assertion of absence ("No circular triggers found") without supporting argument is a partial fail. |
| C-17 | **Vocabulary contract with table caption binding** | technique | When a vocabulary contract (C-15) is present, its term set identifiers are incorporated as column caption labels in the trigger inventory table (e.g., "Type (Term Set A)", "Input Payload (Term Set B)"). Nonconforming cell entries in term-set-captioned columns are structural partial fails, making vocabulary violations detectable at cell level without prose evaluation. Pass requires at least two table columns with explicit term-set caption bindings; the vocabulary contract must precede the table. Requires C-15 to be present; C-17 tests whether the contract extends into table structure. |
| C-18 | **Prosecutorial investigation protocol** | depth | Each pathology class is assessed via a named investigation protocol (e.g., Q1/Q2/Q3 evidence questions, or a case-building structure) that requires producing affirmative evidence before the investigation closes. "Not found" is an open investigation state, not a terminal answer -- it must be closed by a count, a graph property, a scope exclusion, or equivalent structural argument. Pass requires all three pathology classes to use a named multi-step investigation structure. Augments C-16 (which requires evidence) by requiring the investigation to be structurally organized rather than prose-justified. |
| C-19 | **Pre-enumeration investigation case register** | technique | Before any trigger enumeration begins, each pathology class is formally opened as a named case with its evidence standard declared upfront (e.g., "EVIDENCE REQUIRED: trigger count exceeds N, storm threshold calculation shown"). The case register creates a binding obligation: subsequent phases must produce the declared evidence to close each case; a case cannot be closed by assertion. The investigator role is structurally separated from the enumerator role -- investigation cases are registered, then enumeration proceeds, then cases are closed against what was found. Post-enumeration investigation structure satisfies C-18 but not C-19. Pass requires all three pathology classes to have named cases with declared evidence standards opened before the trigger enumeration table. |
| C-20 | **Vocabulary-contract-linked anti-example table** | technique | Anti-example pairs are organized in a table that includes a column explicitly identifying which named term set from the vocabulary contract (C-15) is violated by each bad-form example (e.g., "Term Set Violated: Term Set A -- Trigger Type"). This makes each violation structurally traceable to the contract rather than a standalone domain example. Requires C-13 (anti-examples present) and C-15 (vocabulary contract with named term sets); C-20 tests whether the anti-example table binds to the contract structure. A table with domain-specific bad/good pairs but no term-set violation column does not satisfy C-20 -- it satisfies C-13 only. |
| C-21 | **Pre-investigation status quo failure catalog** | technique | Before any ghost denominator or trigger enumeration begins, the output opens with a named catalog of status-quo failure modes documenting how naive or incomplete trigger analysis fails (e.g., "Failure Mode 1: generic output descriptions -- writing 'processes the record' instead of naming entity/field/action"). The catalog makes the evidence bar concrete before any investigation structure is erected, and its entries are referenced by name in subsequent anti-examples and column rules. Must precede C-11 (ghost denominator) structurally; must name at least two distinct failure modes with documented consequences. A generic methodology preamble or a disclaimer about quality does not pass. Complements C-19 (which opens pathology cases with evidence standards) and C-13 (which provides anti-examples): C-21 establishes the motivational frame that explains why those standards are needed. |
| C-22 | **Per-entry evidence-gated verdict rule** | technique | Each trigger inventory entry includes a dedicated Evidence field, and the governing format rule explicitly states that no Verdict may be written without a populated Evidence field. The gate is stated as a structural constraint on the entry format, not a general quality guideline. Pass requires: (1) the evidence-before-verdict rule is stated explicitly as a governing constraint (e.g., in a Ledger Format Rule preamble), (2) each entry has a dedicated Evidence field distinct from other fields, (3) the rule applies to all verdict types including NOT FIRED and FLAGGED MISSING entries. A table with a Notes column that sometimes contains reasoning does not pass; the field must be named and the gate must be declared. Distinct from C-16 (pathology-level evidence requirement) and C-18 (investigation protocol structure): C-22 operates at individual trigger entry level. |
| C-23 | **Terminal cross-reference integrity check** | technique | After all enumeration and pathology sections are complete, the output includes a dedicated Integrity Check (or equivalent named section) that enumerates explicit cross-reference verifications. At minimum: (1) every ghost denominator candidate (GD-NN) has a corresponding trigger entry -- count stated; (2) every non-firing verdict has a populated evidence field -- count or attestation stated; (3) all three pathology classes are addressed -- class names listed. Each check is enumerated individually; violations are flagged rather than silently passed. A closing summary paragraph does not pass; the check must be a structured list or table of named verification results with explicit completeness claims. Distinct from C-12 (which makes omissions structurally visible at table design time): C-23 is a terminal audit pass verifying that the structural guarantees were honored in the produced content. |
| C-24 | **Three-state GD reconciliation verdict taxonomy** | technique | After the ghost denominator pre-scan (C-11) and trigger enumeration, each GD candidate is formally classified into exactly one of three named terminal states: (1) FIRED -- affirmative evidence of execution under the scenario; (2) CONFIRMED ABSENT -- affirmative evidence the trigger does not apply (condition never satisfied, trigger type excluded from scenario, scope argument shown); (3) FLAGGED MISSING -- GD candidate for which evidence is insufficient to confirm or deny. The three-state taxonomy is structurally significant because CONFIRMED ABSENT requires a positive closure argument while FLAGGED MISSING represents an open investigation obligation. Pass requires: the three states (or named equivalents) are defined in the format specification; every GD candidate is assigned to exactly one state with stated evidence; "not found" alone does not constitute CONFIRMED ABSENT -- a scope exclusion, condition analysis, or trigger graph argument is required. Augments C-02 (correct firing determination) and C-11 (ghost denominator reconciliation) by introducing a tripartite structure that distinguishes evidence of absence from absence of evidence. |
| C-25 | **Tier-aware ghost denominator pre-assignment** | technique | Before trigger enumeration begins, each ghost denominator candidate is pre-assigned to its expected execution tier (Sync or Async). When tier-separated tables are constructed per C-14, each tier table reconciles against only its pre-assigned GD subset -- not the global GD pool. Each tier includes a reconciliation summary of the form: GD candidates assigned to tier / triggers confirmed in tier / absent or missing in tier. Cross-tier misclassification -- a GD candidate pre-assigned to Sync appearing as a confirmed fire in the Async table -- is structurally flagged rather than silently absorbed into the global count. Requires C-11 (ghost denominator) and C-14 (physical tier separation); C-25 tests whether the GD pre-scan is tier-aware and whether per-tier completeness is independently verifiable. A global GD-to-entry count (as verified by C-23 Check 1) satisfies C-23 but not C-25 -- the per-tier breakdown is required. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0

**Gold threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Production-quality trigger trace |
| Silver | >= 60, all essential pass | Useful but missing depth |
| Bronze | >= 40, <=4 essential pass | Partial -- gaps in enumeration or pathology |
| Fail | Any essential fail OR < 40 | Not usable |

---

## Evaluator Notes

- **C-01 vs C-05 tension**: C-01 penalizes omissions; C-05 penalizes false positives. A good output is precise in both directions.
- **C-04 absence is valid**: Stating "no circular triggers detected -- trigger graph is a DAG" is a passing answer for that pathology class; silent omission of the class is not.
- **C-03 specificity bar**: Inputs must name the record entity and fields; outputs must name the action type (update field, send email, call HTTP endpoint, etc.).
- **C-11 ordering matters**: The pre-scan must precede enumeration, not follow it -- a post-hoc reconciliation does not earn this criterion.
- **C-12 column completeness**: All dedicated columns must be present and populated. A table with only Trigger Name and Description columns does not pass.
- **C-13 examples must be domain-specific**: Anti-examples must reference actual platform vocabulary or actual payload specificity, not generic writing quality.
- **C-14 tier vs annotation**: Annotating timing inline (e.g., "(async)" next to a trigger name) does not satisfy C-14. Physical structural separation with independent sequences and reconciliation summaries is required.
- **C-15 vs C-13 distinction**: C-13 requires at least one bad/good pair. C-15 requires a multi-domain preamble that governs all subsequent sections. A vocabulary contract satisfies both; a single anti-example pair satisfies only C-13.
- **C-16 vs C-04**: C-04 requires all three pathology classes to be addressed. C-16 raises the bar on clearance quality -- addressed-with-evidence vs addressed-by-assertion. A C-04 pass does not imply a C-16 pass.
- **C-17 requires C-15**: C-17 is vacuously absent if there is no vocabulary contract. A table with descriptive column names (e.g., "Flow Type") does not satisfy C-17 -- the caption must reference a named term set defined in a preceding preamble.
- **C-18 vs C-16**: C-16 asks whether evidence supports the clearance claim. C-18 asks whether the investigation was conducted through a structured protocol. A certificate schema can satisfy C-16 but not C-18 if it does not require named investigation steps. A prosecutorial protocol satisfies both.
- **C-18 all-three requirement**: All three pathology classes must use a named investigation protocol. Addressing one or two with evidence-backed clearance earns C-16 credit (partial) but not C-18.
- **C-19 vs C-18**: C-18 requires a named multi-step investigation structure; C-19 requires that structure to be pre-committed before enumeration with evidence standards declared upfront. An investigation conducted entirely post-enumeration can satisfy C-18 but not C-19. The test is: were the evidence standards for closing each case established before any triggers were listed?
- **C-19 all-three requirement**: All three pathology cases must be opened with declared evidence standards before enumeration. Opening one or two pre-enumeration and handling the third post-hoc does not pass.
- **C-20 requires C-13 and C-15**: C-20 is vacuously absent if there is no vocabulary contract with named term sets. Domain-specific bad/good pairs without a vocabulary contract satisfies C-13 only. C-20 requires the anti-example table to reference the contract's term set identifiers by name.
- **C-20 vs C-13**: C-13 tests specificity of examples (domain vocabulary, actual payload names). C-20 tests structural linkage of those examples to the vocabulary contract. A table with a "Term Set Violated" column pointing to generic labels (not named term sets from a C-15 contract) does not satisfy C-20.
- **C-21 vs C-13**: C-13 tests whether anti-examples are domain-specific; C-21 tests whether a named failure catalog precedes the investigation and is referenced by downstream sections. A failure catalog satisfies C-21 and provides the raw material for C-13, but C-13 can be satisfied without C-21 (a standalone anti-example pair suffices for C-13).
- **C-21 vs C-19**: C-21 (failure catalog) establishes why the investigation is needed; C-19 (case register) establishes what evidence will close each pathology case. Both require pre-enumeration positioning. A pre-enumeration section that only opens pathology cases satisfies C-19 but not C-21; a pre-enumeration failure catalog that does not open pathology cases satisfies C-21 but not C-19.
- **C-22 scope is entry-level**: C-16 requires evidence for pathology clearances; C-22 requires evidence for every trigger verdict including non-firing entries. A prompt that requires pathology evidence (satisfying C-16) but allows trigger entries without evidence fields does not satisfy C-22.
- **C-22 the gate must be declared**: An implicit expectation that entries will be complete does not pass. The rule "No Verdict may be written without a populated Evidence field" (or equivalent) must be stated explicitly as a constraint in the format specification.
- **C-23 vs C-12**: C-12 requires the table structure to make omissions structurally visible at design time. C-23 requires a terminal audit that verifies the structure was honored in the actual produced content. A well-designed table (C-12) does not imply a passing terminal check (C-23); both can be present independently.
- **C-23 enumeration requirement**: The integrity check must name each verification individually. "All checks passed" without enumeration does not pass. Violations must be flagged; a check that only reports pass states is insufficient.
- **C-24 vs C-11**: C-11 requires the GD pre-scan to precede enumeration and requires reconciliation. C-24 raises the bar on the reconciliation phase itself: the three terminal states (FIRED, CONFIRMED ABSENT, FLAGGED MISSING or named equivalents) must be defined and every GD candidate must be classified into exactly one. A narrative reconciliation that says "GD-03 not found" without assigning it to CONFIRMED ABSENT or FLAGGED MISSING does not satisfy C-24.
- **C-24 CONFIRMED ABSENT requires a positive argument**: Saying a trigger "was not observed" or "was not found" does not constitute CONFIRMED ABSENT. The output must provide affirmative evidence -- a condition analysis showing the branch is never entered, a trigger graph showing the node is unreachable under the scenario, or an explicit scope exclusion. FLAGGED MISSING is the correct classification when affirmative evidence is unavailable.
- **C-24 vs C-02**: C-02 tests whether the firing determination is correct for listed triggers. C-24 tests whether every GD candidate is formally reconciled into a named terminal state. A correct non-firing verdict in the trigger table does not imply a C-24 pass -- the GD reconciliation classification must exist separately and explicitly.
- **C-25 requires C-11 and C-14**: C-25 is vacuously absent if there is no ghost denominator (C-11) or no physical tier separation (C-14). A per-tier firing count in a physically separated table satisfies C-14 but not C-25 -- the GD candidates must be pre-assigned by tier, and each tier's reconciliation must reference its own GD subset.
- **C-25 vs C-23**: C-23 Check 1 verifies global GD-to-entry completeness (all GD candidates have a corresponding entry). C-25 requires the GD completeness check to be decomposed by tier. A global count satisfies C-23 but not C-25.
- **C-25 cross-tier flagging**: A GD candidate pre-assigned to Sync that fires and appears in the Async table represents a misclassification in the original pre-scan. C-25 requires this to be flagged rather than silently absorbed. The structural signal is that tier-level reconciliation totals will not balance without explicit explanation.
- **Placeholder trace**: This rubric was generated against a placeholder ground truth. When a real hand-compiled trace is available, re-score C-01 and C-05 against it directly.

---

## Round 6 Score Reference (v7 denominator /17)

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (Inertia Framing: Status Quo Contrast Protocol) | 5/5 | 3/3 | C-09 C-10 C-11 C-12 C-13 C-16 C-18 C-19 C-21 C-22 C-23 C-24 + 0.5*C-14 = 12.5/17 | 60+30+7.35 = **97.35** | Gold |
| V-02 (Phrasing Register: Evidence Ledger + Failure Catalog) | 5/5 | 2.5/3 (C-08 partial) | C-09 C-10 C-11 C-12 C-16 C-18 C-21 C-22 C-23 C-24 = 10/17 | 60+25+5.88 = **90.88** | Gold |

---

## Round 5 Score Reference (v6 denominator /15)

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (Inertia Framing: Status Quo Contrast Protocol) | 5/5 | 3/3 | C-09 C-10 C-11 C-12 C-13 C-16 C-18 C-21 + 0.5*C-14 + 0.5*C-22 = 10/15 | 60+30+6.67 = **96.67** | Gold |
| V-02 (Phrasing Register: Evidence Ledger) | 5/5 | 2.5/3 (C-08 partial) | C-09 C-10 C-11 C-22 C-23 + others pending | 60+25+? | Gold (projected) |

---

## Round 4 Score Reference (v5 denominator /12)

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (Role Sequence: Investigators Before Enumerators) | 5/5 | 3/3 | C-09 C-11 C-12 C-13 C-16 C-18 C-19 + 0.5*C-10 = 7.5/12 | 60+30+6.25 = **96.25** | Gold |
| V-02 (Caption-Bound Vocabulary Table) | 5/5 | 2.5/3 (C-07 partial) | C-09 C-10 C-12 C-13 C-14 C-15 C-16 C-17 C-20 + 0.5*C-18 = 9.5/12 | 60+25+7.92 = **92.92** | Gold |

---

## Round 3 Score Reference (v5 denominator /12)

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (Structured Clearance Certificate) | 5/5 | 2/3 (C-07 fail) | C-09 C-10 C-12 C-13 C-16 = 5/12 | 60+20+4.17 = **84.17** | Gold |
| V-02 (Tier-Organized Pre-Scan) | 5/5 | 3/3 | C-10 C-11 C-12 C-14 + 0.5*C-16 = 4.5/12 | 60+30+3.75 = **93.75** | Gold |
| V-03 (Vocabulary Contract as Governing Preamble) | 5/5 | 3/3 | C-10 C-11 C-12 C-13 C-15 C-16 C-17 = 7/12 | 60+30+5.83 = **95.83** | Gold |
| V-04 (Prosecute the Absence) | 5/5 (partial scorecard) | -- | C-18 confirmed; full tally pending | -- | -- |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-15 | Round 1 excellence signals: added C-11 (ghost denominator), C-12 (structural falsifiability), C-13 (anti-example anchoring); aspirational denominator /2 -> /5 |
| v3 | 2026-03-15 | Round 2 excellence signals: added C-14 (sync/async tier separation), C-15 (multi-domain vocabulary contract), C-16 (absence-requires-evidence clearance); aspirational denominator /5 -> /8 |
| v4 | 2026-03-15 | Round 3 excellence signals: added C-17 (vocabulary contract with table caption binding), C-18 (prosecutorial investigation protocol); aspirational denominator /8 -> /10 |
| v5 | 2026-03-15 | Round 4 excellence signals: added C-19 (pre-enumeration investigation case register), C-20 (vocabulary-contract-linked anti-example table); aspirational denominator /10 -> /12 |
| v6 | 2026-03-15 | Round 5 excellence signals: added C-21 (pre-investigation status quo failure catalog), C-22 (per-entry evidence-gated verdict rule), C-23 (terminal cross-reference integrity check); aspirational denominator /12 -> /15 |
| v7 | 2026-03-15 | Round 6 excellence signals: added C-24 (three-state GD reconciliation verdict taxonomy), C-25 (tier-aware ghost denominator pre-assignment); aspirational denominator /15 -> /17 |
"""

with open("C:/src/sim/simulations/quest/rubrics/flow-trigger-rubric-v7-2026-03-15.md", "w") as f:
    f.write(rubric)

print("done")
