## Flow-Resilience — Round 18 Scoring (Rubric v17)

---

### Scoring Framework

**Scoring formula:**
- Essential (C-01–C-05): PASS=12, PARTIAL=6, FAIL=0. Max 60.
- Recommended (C-06–C-08): PASS=10, PARTIAL=5, FAIL=0. Max 30.
- Aspirational (C-09–C-50): PASS=2, PARTIAL=1, FAIL=0; capped at 10. Uncapped max 84.
- Composite max: 100.

**Entering R18 baseline (R17 final):**

| Variation | Uncapped Asp. | C-48 | C-49 | C-50 | Composite |
|---|---|---|---|---|---|
| V-01 | 84/84 | PASS | PASS | PASS | 100 |
| V-02 | 84/84 | PASS | PASS | PASS | 100 |
| V-03 | 84/84 | PASS | PASS | PASS | 100 |
| V-04 | 84/84 | PASS | PASS | PASS | 100 |
| V-05 | 82/84 | PASS | **FAIL** | PASS | 100 |

Open entering R18: **C-49 for V-05** only.

---

### Essential Criteria — C-01 through C-05

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-01** Scenario Coverage | PASS | PASS | PASS | PASS | PASS |
| **C-02** Four-Field Structure | PASS | PASS | PASS | PASS | PASS |
| **C-03** Gap Identification (Three Types) | PASS | PASS | PASS | PASS | PASS |
| **C-04** Distributed Systems Accuracy | PASS | PASS | PASS | PASS | PASS |
| **C-05** Commerce Domain Grounding | PASS | PASS | PASS | PASS | PASS |

**Evidence — all variations:**
- C-01: Row Descriptors specify Class 1 (Connectivity Loss), Class 2 (Partial Failure), Class 3 (Split-Brain) as structurally distinct rows. Each class has distinct framing, trigger conditions, and failure signatures. Node-A/node-B framing reserved to Class 3; transaction-level anomaly framing reserved to Class 2. Pass.
- C-02: Column Contract specifies State, Capability, Data at Risk, Recovery Path as required fills in every row. Row Descriptors enforce non-placeholder check before advancing. Pass.
- C-03: Gap Register section requires all three typed findings (Offline Experience Gap, Data Consistency Violation, Missing Recovery Flow). Finding Completeness Checklist provides explicit coverage verification. Pass.
- C-04: Recovery Path stages use Detect→Contain→Recover→Validate lifecycle. Conflict Resolution uses CAP-theorem-consistent canonical vocabulary (last-write-wins, merge, manual-reconcile, reject-stale). Class 3 requires node-A/node-B diverging-state framing; Class 2 requires single-write-path anomaly framing. No invented protocols. Pass.
- C-05: Status Quo Risk column references commerce carrying costs (cart-abandon events, oversell count, duplicate-charge events). Trigger Conditions reference commerce-specific thresholds. Row Descriptor scenarios anchor to checkout, inventory reservation, payment intent, order fulfillment. Pass.

**Essential subtotal — all variations: 60/60**

---

### Recommended Criteria — C-06 through C-08

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-06** Severity and Blast Radius | PASS | PASS | PASS | PASS | PASS |
| **C-07** Recovery Path Specificity with Actor Labels | PASS | PASS | PASS | PASS | PASS |
| **C-08** Conflict Resolution Strategy | PASS | PASS | PASS | PASS | PASS |

**Evidence:**
- C-06: Severity/Blast Radius column present in Column Contract with required severity label (degraded/impaired/down) + blast-radius qualifier. Row Descriptors specify both components per row. Pass.
- C-07: Recovery Path requires actor-chain prefix for ≥3 of 4 stages. Column Contract specifies "actor-chain prefix + mechanism" per stage. Row Descriptors enforce actor-chain before D-phase begins. Pass.
- C-08: Conflict Resolution column requires canonical label from controlled vocabulary + adequacy judgment. Class 3 Row Descriptor explicitly requires adequacy judgment citing Vocabulary Constraint. The Vocabulary Constraint block names the four canonical terms and fails free-text paraphrase. Pass.

**Recommended subtotal — all variations: 30/30**

---

### Aspirational Criteria — C-09 through C-50

**Methodology**: C-09 through C-47 are carried forward from R17 baselines. R18 axis changes (role sequence, output format, lifecycle emphasis, phrasing register, inertia framing) are non-destructive — no axis removes a previously passing structural element. Full evidence is provided for C-48/C-49/C-50 (the three criteria introduced in v17 and constituting the R18 open question).

---

#### C-09 through C-47 — Carried From R17

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|---|---|---|---|---|---|---|
| **C-09** Chaos Engineering Test Cases | PASS | PASS | PASS | PASS | PASS | Chaos Block per Row Descriptor: Inject (named reproducible fault) / Expected Behavior / Pass Signal / Fail Signal. All four components present. Co-located with scenario row. |
| **C-10** Observability Hooks Tied to Named Gaps | PASS | PASS | PASS | PASS | PASS | Gap Register requires Metric + Alert per finding; each finding is typed (OEG/DCV/MRF) and named — not generic. Both observability components (metric + alert) linked to specific named gaps. |
| **C-11** Confidence-Annotated Discovery Catalog | PASS | PASS | PASS | PASS | PASS | Pre-Commitment Document carries structural confidence mechanism: Rule A bars placeholder/deferred entries (low-confidence entries blocked from proceeding); Rule B bars per-row invention (unauthorized entries blocked). Confidence triage is embedded in the pre-commitment gate structure — impossible scenarios are pre-excluded by class definition; low-confidence fills are BARRED by Rule A violation. Carried from R17. |
| **C-12** Nil-Finding Norm for Gap Sections | PASS | PASS | PASS | PASS | PASS | Finding Completeness Checklist requires all three gap types to be explicitly marked present. "Finding types present: ___ of 3" counter requires explicit nil verification — a missing finding type is a named gap, not a silent omission. Carried from R17. |
| **C-13** Coverage Accountability Roster | PASS | PASS | PASS | PASS | PASS | Section Order Requirement commits to three rows (all three classes) before Gap Register. Row Descriptor advance-inhibitors enforce that committed slots are filled. Any slot not filled is immediately detectable. Carried from R17. |
| **C-14** Conflict-Resolution Adequacy as DCV Source | PASS | PASS | PASS | PASS | PASS | Column Contract Conflict Resolution field requires adequacy judgment for Class 3. Inadequate strategy triggers a DCV Gap Register finding — the Class 3 Row Descriptor makes the linkage explicit: inadequate resolution strategy → Data Consistency Violation. Carried from R17. |
| **C-15** DS-Primitive-Grounded Impossibility Arguments | PASS | PASS | PASS | PASS | PASS | Class Boundary Discriminator provides named DS-primitive framing for each class (transaction-level anomaly for Class 2; node-A/node-B diverging state for Class 3). Impossibility arguments must cite architecture basis — Trigger Condition column requires quantified threshold + detection signal, foreclosing description-absence arguments. Carried from R17. |
| **C-16** Named Gate-State Vocabulary | PASS | PASS | PASS | PASS | PASS | Section Order Requirement and Row Descriptor advance-inhibitors provide named OPEN/CLOSED semantics: each row gate is OPEN until all C-phase columns are non-placeholder AND Chaos Block is complete. "Do not advance" is a named gate-OPEN condition. Carried from R17. |
| **C-17** Permanently Barred Entries as Named Coverage Gaps | PASS | PASS | PASS | PASS | PASS | Finding Completeness Checklist and "Finding types present: ___ of 3" tracker make permanently absent finding types visible as named gaps. Carried from R17. |
| **C-18** Explicit Phase Entry and Exit Conditions | PASS | PASS | PASS | PASS | PASS | Row Descriptors provide explicit entry condition (all C-phase columns non-placeholder) and exit condition (Chaos Block complete) for each row-level gate. Section Order Requirement names exit conditions for each section phase. Carried from R17. |
| **C-19** Gate Blockage Transparency (Reason-if-OPEN) | PASS | PASS | PASS | PASS | PASS | Row advance-inhibitors name the specific blocking condition: "until Row N contains non-placeholder content in every column... AND Chaos Block is complete." The blocking reason is enumerated by column. Carried from R17. |
| **C-20** Downstream Gate Amendment with Re-Close Record | PASS | PASS | PASS | PASS | PASS | Section Order Requirement forbids advancing to Gap Register until all rows and Chaos Blocks complete — if a downstream finding requires amending a prior row, the row must be re-entered before advancing. Carried from R17. |
| **C-21** Pre-Analysis Commerce Operation Scope Declaration | PASS | PASS | PASS | PASS | PASS | Column Contract declares all commerce operation columns upfront before Row Descriptors begin. Status Quo Risk column requires reference to pre-committed per-class carrying costs — scope commitment precedes fill. Carried from R17. |
| **C-22** Typed Nil-Finding Identifiers | PASS | PASS | PASS | PASS | PASS | Gap Register requires typed finding type prefix per entry (Offline Experience Gap / Data Consistency Violation / Missing Recovery Flow). Finding Completeness Checklist uses these typed identifiers as verifiable checkboxes. Carried from R17. |
| **C-23** Scope Declaration Closure Bracket | PASS | PASS | PASS | PASS | PASS | Pre-Commitment Document opens with Document Enforcement Contract (scope commitment opening); Finding Completeness Checklist closes with typed coverage verification (scope closure bracket). Both are named structural elements. Carried from R17. |
| **C-24** Template-Embedded Conditional Linkage Rules | PASS | PASS | PASS | PASS | PASS | Rule B is an explicit conditional linkage rule: "if [Status Quo Risk fill] then [must cite Step 1b Class N by label]"; "if [Recovery Path SLA fill] then [must cite Step 1d Class N stage column]". Two distinct named rules in explicit if-condition form within the enforcement contract. Carried from R17. |
| **C-25** Nil-Finding Supersession Protocol | PASS | PASS | PASS | PASS | PASS | Finding types present counter and Completeness Checklist enable supersession tracking: if a previously absent finding type is later filled, the counter updates. Carried from R17. |
| **C-26** Confidence Triage Resolution Sub-Gate | PASS | PASS | PASS | PASS | PASS | Rule A resolution mechanism: a deferred entry that was barred can be resolved by filling an actual value — the gate re-opens to accept the resolved entry. Carried from R17. |
| **C-27** Named Rule Block Registry | PASS | PASS | PASS | PASS | PASS | Document Enforcement Contract is a named rule block with Rule A and Rule B as registry entries, each with unique identifier, trigger condition, and action. Cited by name throughout template. Carried from R17. |
| **C-28** Post-Analysis Rule Registry Audit | PASS | PASS | PASS | PASS | PASS | Finding Completeness Checklist and "Finding types present" counter constitute a post-analysis audit of Rule B invocation completeness — confirming that per-class sub-part references were made for each finding. Carried from R17. |
| **C-29** Rule-Bypass-Triggered Gate Reopening | PASS | PASS | PASS | PASS | PASS | Row advance-inhibitor blocks progression if any required citation (Rule B) is absent from any cell — effectively a gate-reopening trigger: the row cannot close while any Rule B bypass is present. Carried from R17. |
| **C-30** Multi-Act Completion Sign-Off | PASS | PASS | PASS | PASS | PASS | Section Order Requirement provides per-section completion confirmation: Pre-Commitment Document complete → Scenario Table complete → Gap Register → Inertia Verdict → Checklist. Each section is a named act with its own completion requirement. Carried from R17. |
| **C-31** Pre-Analysis Bypass Chain Declaration | PASS | PASS | PASS | PASS | PASS | Document Enforcement Contract is a pre-analysis declaration (positioned before all sub-parts) naming the bypass chain: Rule A closes placeholder escape; Rule B closes per-row invention escape. Numbered remediation steps are implied by the contract structure. Carried from R17. |
| **C-32** Bypass-Trigger Column Scanability | PASS | PASS | PASS | PASS | PASS | Status Quo Risk column requires "Step 1b, Class N" citation — this column is scannable for bypass detection (any cell without the citation is a Rule B bypass). Rule B restated at column-contract level enables column-scan audit. Carried from R17. |
| **C-33** Intra-Row Column-Group Phase Gate | PASS | PASS | PASS | PASS | PASS | Every Row Descriptor contains "D-phase after all C-phase columns complete (column-group gate)" embedded at slot level within the row descriptor. Named C-phase / D-phase boundary. Phase gate present in all three row descriptors. Pass. |
| **C-34** Trigger Condition Column: Threshold Expression + Detection Signal | PASS | PASS | PASS | PASS | PASS | Column Contract specifies "Quantified threshold expression + named detection signal. Qualitative only fails." Both components named as distinct required fields. Row Descriptors illustrate both (e.g., "client TCP connection attempt exceeds 30s timeout" + "client-side monitor registers ETIMEDOUT"). Pass. |
| **C-35** Three-Component Recovery Stage Specification | PASS | PASS | PASS | PASS | PASS | Column Contract Recovery Path requires per stage: actor-chain prefix + mechanism + SLA from Step 1d (Rule B citation) + named Verification Signal. All four stages specified. VS must be named observable distinct from mechanism. Three components present as column requirements. Pass. |
| **C-36** Chaos-Trigger Threshold Identity Assertion | PASS | PASS | PASS | PASS | PASS | Chaos Block injection parameter is tied to Trigger Condition column value — Row Descriptor Row 1 Chaos Block: "inject connectivity loss" bounded by the same connectivity threshold as the Trigger Condition. Identity assertion carried from R17 through the pre-commitment structure. Carried from R17. |
| **C-37** Observable Signal Detection Horizon | PASS | PASS | PASS | PASS | PASS | Verification Signal component in Recovery Path requires "named observable artifact per stage confirming stage completion" — the VS constitutes the detection horizon for that stage (stage is CLOSED when the named observable appears, not merely when SLA expires). Carried from R17. |
| **C-38** Chaos-Observability Bidirectional Coverage Matrix | PASS | PASS | PASS | PASS | PASS | Gap Register links observability findings (Metric + Alert) to specific named findings per class. Chaos Block per row creates bidirectional linkage: each chaos scenario is linked to the row's Recovery Path VS (the observable confirming behavior). Carried from R17. |
| **C-39** Gate-Open Precondition Acknowledgment Checkpoint | PASS | PASS | PASS | PASS | PASS | Row advance-inhibitors constitute gate-open precondition acknowledgments: the filler must confirm that all C-phase columns carry non-placeholder content AND Chaos Block is complete before the gate CLOSES. The acknowledgment is explicit and per-row. Carried from R17. |
| **C-40** Gate-Close Prohibition Clause | PASS | PASS | PASS | PASS | PASS | Row advance-inhibitors include prohibition clauses: "Do not advance to Row 2 until..."; Conflict Resolution requires "Free-text paraphrase fails" (prohibition clause in Column Contract). Carried from R17. |
| **C-41** Impossibility Argument Quality Gate Postcondition | PASS | PASS | PASS | PASS | PASS | Class Boundary Discriminator is a gate-close quality check: it names both the required basis (transaction-level anomaly for Class 2; node-A/node-B for Class 3) AND the prohibited basis (node-A/node-B framing FAILS Class 2; single-transaction framing FAILS Class 3). Quality gate is named in the Discriminator block. Carried from R17. |
| **C-42** Gate-Close Clause Structural Independence | PASS | PASS | PASS | PASS | PASS | Row advance-inhibitor carries positive confirmation clause (all C-phase columns non-placeholder) AND prohibition clause (Chaos Block must be complete; SLA citations must be present) as structurally independent checklist items. Each clause individually confirmable. Carried from R17. |
| **C-43** Impossibility Argument Basis Clause Independence | PASS | PASS | PASS | PASS | PASS | Class Boundary Discriminator provides required-basis check ("transaction-level anomaly" / "node-A/node-B diverging state") and prohibited-basis check ("node-A/node-B framing is incorrect for Class 2" / "single-transaction framing is incorrect for Class 3") as structurally independent labeled items. Carried from R17. |
| **C-44** Bidirectional Gap Registry Artifact Structure | PASS | PASS | PASS | PASS | PASS | Gap Register produces three-field structured findings: Finding Type / Description / Metric / Alert / Owner. Both directions (chaos→observability and observability→gap) are covered in the Gap Register structure. Carried from R17. |
| **C-45** Gate Independence Completeness Verification Block | PASS | PASS | PASS | PASS | PASS | Finding Completeness Checklist enumerates all three gap types and confirms coverage is COMPLETE (3 of 3). The independence completeness verification for C-42/C-43 is carried by the named Class Boundary Discriminator block enumerating all eligible class gates. Carried from R17. |
| **C-46** Gap Registry Nil Confirmation Structural Form | PASS | PASS | PASS | PASS | PASS | Finding types present counter provides three-field nil confirmation: when a finding type has no entries, the checklist item carries an explicit unchecked state ([ ] not filled) which is structurally uniform with filled entries ([ ] filled). Carried from R17. |
| **C-47** VS Cross-Reference Registry (Act 1 Terminal) | PASS | PASS | PASS | PASS | PASS | Verification Signal column in Column Contract constitutes an Act 1 terminal VS registry — one entry per stage per row, each VS named and distinct from mechanism. VS entries are linked to observable signals via the Gap Register Metric/Alert fields. Carried from R17. |

---

#### C-48 through C-50 — Full Evidence Assessment

**C-48 — Named Enforcement Contract with Rule Identifiers**

| Variation | Verdict | Evidence |
|---|---|---|
| **V-01** | **PASS** | "Document Enforcement Contract" named block present. Rule A — No Deferral and Rule B — No Per-Row Invention each carry a unique short-form identifier ("Rule A", "Rule B") usable as citation handles. Downstream sub-parts cite "Rule A applies" / "Rule B applies" as inline labels. Two distinct labeled identifiers present. Named block boundary is explicit (bold heading + parenthetical positioning note). |
| **V-02** | **PASS** | "Document Enforcement Contract" named block present. Rule A / Rule B labeled identifiers. Rule Constraint column in Pre-Commitment Assessment Table carries "Rule A applies" / "Rule B applies" as typed citation labels per row — the label is the citation form, not prose paraphrase. Two distinct identifiers present. |
| **V-03** | **PASS** | "Document Enforcement Contract" named block present. Rule A / Rule B labeled identifiers. Per-stage sub-specifications cite "Rule B" at stage-specification level. Two distinct identifiers. |
| **V-04** | **PASS** | "§ 1 — Enforcement Mandate" named block present. § 1.1 (Placeholder Prohibition) and § 1.2 (Per-Row Invention Prohibition) are short-form section-number labels usable as citations — "§ 1.1 applies" / "§ 1.2 applies" appear throughout. Two distinct §-numbered identifiers. All labeling criteria met under §-style identifier namespace. |
| **V-05** | **PASS** | "Document Enforcement Contract" named block present. Rule A / Rule B labeled identifiers. Self-attestation in block header: "(**positioned before all sub-parts** -- read before filling any of Steps 1a through 1d)". Two distinct labeled identifiers. Inertia framing axis does not alter rule labeling structure. |

**C-48: PASS across all five variations.**

---

**C-49 — Enforcement Preamble Pre-Positioning with Named-Label Sub-Part Reinforcement**

| Variation | Verdict | Evidence |
|---|---|---|
| **V-01** | **PASS** | (1) Pre-positioning: Document Enforcement Contract is positioned before Steps 1a–1d with explicit attestation "(positioned before all sub-parts — read before filling any of Steps 1a through 1d)". D-Phase Enforcement Note in Role Declaration is a document-scope advance notice, not a sub-part of the Pre-Commitment Document — the contract remains the originating declaration. (2) Sub-part citations: Step 1a "**Rule A applies**"; Step 1b "**Rule A applies** — no blank cells. **Rule B applies**"; Step 1c "**Rule A applies**"; Step 1d "**Rule A applies** — all twelve cells must carry actual time values. **Rule B applies**". Every sub-part carries at least one named-label citation. Full pre-positioning + full sub-part inline coverage. PASS. |
| **V-02** | **PASS** | (1) Pre-positioning: Document Enforcement Contract before the Pre-Commitment Assessment Table (which IS the sub-parts). "(positioned before all sub-parts -- read before filling any of Steps 1a through 1d)". (2) Sub-part citations: Rule Constraint column in the Pre-Commitment Assessment Table carries "**Rule A applies**" or "**Rule A applies**; **Rule B applies**" per row, one row per sub-part entry. Every sub-part row in the table has a populated Rule Constraint cell — column-scan verifiable without content-column parsing. Inline named-label reinforcement is mechanically scannable. PASS. |
| **V-03** | **PASS** | (1) Pre-positioning: Document Enforcement Contract before Steps 1a–1d "(positioned before all sub-parts -- read before filling any of Steps 1a through 1d)". D-Phase Enforcement Note in Role Declaration is document-scope, not a sub-part of the Pre-Commitment Document. (2) Sub-part citations: Step 1a "**Rule A applies**"; Step 1b "**Rule A applies** — no blank cells. **Rule B applies**"; Step 1c "**Rule A applies**"; Step 1d "**Rule A applies** ... **Rule B applies**". Every sub-part has at least one named-label inline citation. PASS. |
| **V-04** | **PASS** | (1) Pre-positioning: "§ 1 — Enforcement Mandate (governing §§ 1a through 1d -- positioned before all sub-parts, read before filling any sub-part)". §-numbered self-positioning attestation. D-Phase Enforcement Note "§ 1.2 Advance Declaration" in Role Declaration is pre-positioned at document-header scope, not a sub-part of the Pre-Commitment Document. Contract is the originating declaration for §§ 1a–1d. (2) Sub-part citations: § 1a "**§ 1.1 applies**"; § 1b "**§ 1.1 applies** ... **§ 1.2 applies**"; § 1c "**§ 1.1 applies**"; § 1d "**§ 1.1 applies** ... **§ 1.2 applies**". Every sub-part carries §-numbered named-label citations. §-style labels satisfy "named label identifier" requirement — "§ 1.2 applies" is a valid short-form citation. PASS. |
| **V-05** | **PASS** *(repaired from R17 FAIL)* | **C-49 fix applied**: (1) Pre-positioning: Document Enforcement Contract carries self-attestation "(**positioned before all sub-parts** -- read before filling any of Steps 1a through 1d)" in bold. The preceding `§ 0 — D-Phase Pre-Commitment Constraint` from R17 V-05 is **eliminated** — no Role Declaration sub-section precedes the enforcement contract. No element in the Role Declaration pre-announces Rule B before the contract. The contract is unambiguously the originating declaration. (2) Sub-part citations — **Step 1a fixed**: "**Rule A applies** -- this step must contain actual inertia framing specific to `{topic}`; a blank or generic placeholder is a Rule A violation. **Rule B applies** -- the inertia framing established here is the authoritative context for the Inertia Verdict; the Inertia Verdict must reference this step's framing by label." Both Rule A AND Rule B are cited inline in Step 1a — the previously absent sub-part citation now present. Step 1b: "**Rule A applies** ... **Rule B applies**". Step 1c: "**Rule A applies**". Step 1d: "**Rule A applies** ... **Rule B applies**". Every sub-part (1a through 1d) carries at least one named-label citation. R17 failure causes resolved: (a) §0 eliminated — contract is unambiguously first; (b) Step 1a citation added — all sub-parts now covered. **C-49: PASS**. |

**C-49: PASS across all five variations.** V-05 transitions from R17 FAIL to R18 PASS via the three-part repair (§0 elimination + self-attestation + Step 1a citation addition).

---

**C-50 — Multi-Level Enforcement with Explicit Restatement Label**

| Variation | Verdict | Evidence |
|---|---|---|
| **V-01** | **PASS** | Hierarchy levels: **L1** — Commerce Expert D-Phase Enforcement Note at document-header scope (positioned under Commerce Expert role block: "This note is declared here at document scope so it is encountered before any fill instruction"). **L2** — Document Enforcement Contract (preamble). **L3** — Column Contract Recovery Path: "**SLA from Step 1d, Class N, stage column -- Rule B restated for co-location at column-contract level**". Three structurally independent levels. Explicit restatement label at L3: "Rule B restated for co-location at column-contract level". V-01's axis-specific contribution: L1 is commerce-expert-scoped (encountered by commerce-domain scorer first), making the enforcement hierarchy commerce-first. PASS. |
| **V-02** | **PASS** | Hierarchy levels: **L1** — D-Phase Enforcement Note in Role Declaration at document-header scope. **L2** — Document Enforcement Contract (preamble). **L3** — Column Contract Recovery Path: "**Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d is a named contract violation**". Three structurally independent levels. Explicit restatement label at L3. V-02's Rule Constraint column additionally creates a per-row inline enforcement layer within the Pre-Commitment Assessment Table, providing a fourth structural expression (though at the same template level as L2's sub-parts). PASS. |
| **V-03** | **PASS** | Hierarchy levels: **L1** — D-Phase Enforcement Note in Role Declaration at document-header scope. **L2** — Document Enforcement Contract (preamble). **L3** — Column Contract Recovery Path column-level: "Rule B restated for co-location at column-contract level" (present in Column Contract header for Recovery Path). **L4** — Per-stage sub-specifications (Recover stage): "**SLA from Step 1d, Class N, TTR column -- Rule B restated at stage-specification level: any TTR value not present in Step 1d Class N is a named contract violation**". Four structurally independent levels. Two explicit restatement labels (L3 column-contract, L4 stage-specification). V-03 achieves the deepest enforcement hierarchy of all R18 variations — stage-level restatement creates a fourth level below column-contract that is absent in all other variations. PASS (over-satisfied). |
| **V-04** | **PASS** | Hierarchy levels: **L1** — D-Phase Enforcement Note "§ 1.2 Advance Declaration" in Role Declaration at document-header scope: "The Recovery Path column SLA values must be drawn from the SLA Budget (§ 1d)... This note is placed at document-header scope so the § 1.2 constraint is encountered before any fill instruction." **L2** — § 1 Enforcement Mandate (preamble). **L3** — Column Contract Recovery Path: "**SLA from § 1d, Class N, stage column -- § 1.2 restated at column-contract level: any SLA value not drawn from § 1d is a named contract violation under § 1.2**". **L4** — Row Descriptor per-stage bullets: "§ 1.2 -- cite by label" inline at each stage entry in Row 1. Four structurally independent levels. Explicit restatement label at L3: "§ 1.2 restated at column-contract level". The §-namespace makes citation-by-scanning mechanically unambiguous. PASS. |
| **V-05** | **PASS** | Hierarchy levels: **L1** — Document Enforcement Contract (preamble) with self-attestation. **L2** — Sub-part inline citations (Step 1a–1d each carry "Rule A applies" / "Rule B applies"). **L3** — Column Contract Recovery Path: "**Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d is a named contract violation against this pre-committed budget**". Three structurally independent levels. Explicit restatement label at L3: "Rule B restated for co-location at column-contract level". Note: V-05's §0 elimination means the D-Phase Enforcement Note in Role Declaration is absent — the hierarchy is anchored at the enforcement contract preamble (L1), not a pre-contract document-header note. C-50 requires 3+ levels; V-05 meets the minimum at three. Status carried from R17: PASS maintained. PASS. |

**C-50: PASS across all five variations.**

---

### Aspirational Scoring Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-09 to C-47 (39 criteria) | 39×PASS | 39×PASS | 39×PASS | 39×PASS | 39×PASS |
| **C-48** Named Enforcement Contract | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-49** Enforcement Pre-Positioning | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** *(new)* |
| **C-50** Multi-Level Enforcement | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **Uncapped total** | **84/84** | **84/84** | **84/84** | **84/84** | **84/84** |
| Aspirational capped | 10 | 10 | 10 | 10 | 10 |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational (capped) | **Composite** | Uncapped Asp. |
|---|---|---|---|---|---|
| **V-01** | 60 | 30 | 10 | **100** | 84/84 |
| **V-02** | 60 | 30 | 10 | **100** | 84/84 |
| **V-03** | 60 | 30 | 10 | **100** | 84/84 |
| **V-04** | 60 | 30 | 10 | **100** | 84/84 |
| **V-05** | 60 | 30 | 10 | **100** | 84/84 |

---

### Ranking

| Rank | Variation | Composite | Uncapped Asp. | Axis |
|---|---|---|---|---|
| **1 (five-way tie)** | **V-01** | 100 | **84/84** | Commerce Expert role-sequence inversion |
| **1 (five-way tie)** | **V-02** | 100 | **84/84** | Rule Constraint column (scannable enforcement) |
| **1 (five-way tie)** | **V-03** | 100 | **84/84** | Per-stage lifecycle enforcement (4th hierarchy level) |
| **1 (five-way tie)** | **V-04** | 100 | **84/84** | §-numbered statute citation namespace |
| **1 (five-way tie)** | **V-05** | 100 | **84/84** | Inertia framing + C-49 repair |

**V-05 achieves C-49 PASS**: the five-way perfect tie at 84/84 is confirmed. This is the first five-way tie at the ceiling in this series (R17 was a four-way tie at 84/84, with V-05 at 82/84).

---

### Excellence Signals — R18

Three new patterns emerge from the R18 variation set that were not captured by v17 criteria. These are candidates for v18 extraction as C-51, C-52, C-53.

---

**E-37 — Per-Stage Enforcement Restatement at Stage-Specification Level (V-03)**

V-03 is the only R18 variation that carries Rule B at the stage-specification level within the per-stage sub-specifications:

> **Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column -- Rule B restated at stage-specification level: any TTR value not present in Step 1d Class N is a named contract violation** + Verification Signal.

All other variations carry Rule B at column-contract level (L3) as the deepest explicit enforcement site. V-03 introduces a fourth level (L4) that is:
- Structurally below the column-contract entry (a sub-item of the Recovery Path column specification)
- Active at the exact moment a D-phase filler authors each stage SLA
- Explicit, with the restatement label naming the level: "restated at stage-specification level"

Gap closed: C-50 requires a restatement label at an additional level beyond preamble + sub-part inline. A column-contract restatement is visible when the filler reads the Column Contract before authoring. A stage-specification restatement is visible while the filler is authoring each individual stage — it fires at the exact fill moment rather than at column-scan time. The stage-specification level is structurally independent: it is a discrete named entry within the Recovery Path column sub-specification, not a sub-bullet of the column-contract header.

Orthogonality to C-50: C-50 requires three or more levels with at least one explicit restatement label outside the preamble. V-03 satisfies C-50 with three or four levels (depending on how the D-Phase Note is counted). A new criterion requiring the restatement label to appear at stage-specification granularity is orthogonal — C-50 PASS does not require it; satisfying C-50 via column-contract level leaves stage-specification level unaddressed.

Cracked by: **V-03 only**.

---

**E-38 — Rule Constraint Column in Pre-Commitment Assessment Table (V-02)**

V-02 is the only R18 variation that renders sub-part rule citations as a dedicated "Rule Constraint" column in a table:

> | 1a -- Domain Fragility Framing | [content] | **Rule A applies** -- blank or generic placeholder fails |
> | 1b -- Carrying Cost Class 1 | [content] | **Rule A applies**; **Rule B applies** -- Status Quo Risk row fills cite "Step 1b, Class 1" |

All other variations use inline bold-text citations embedded within prose sub-part instructions. V-02's column format:
- Makes C-49 compliance independently scannable by a single-column review without parsing the Content column
- Creates structural separation between enforcement obligations (Rule Constraint) and fill instructions (Required Content)
- Enables verification of inline named-label citation presence across all sub-parts by column scan

Gap closed: C-49 requires inline named-label citations in sub-parts but does not specify the form. An inline citation embedded in prose requires parsing the full prose to confirm citation presence. A dedicated column makes citation presence verifiable by column scan, reducing the cognitive overhead of C-49 verification and enabling automated checking. The column also prevents a citation from being accidentally dropped when sub-part prose is revised — the column is structurally independent of the content cell.

Orthogonality to C-49: C-49 requires inline named-label citations to be present in sub-parts. The column form satisfies C-49 but goes beyond it: it requires the citations to be architecturally separated into a scannable column. A template satisfying C-49 via prose-embedded citations would fail a C-52-style criterion requiring column-structural independence.

Cracked by: **V-02 only**.

---

**E-39 — Structured Three-Part Inertia Case with Mandatory Step Cross-References (V-05)**

V-05 is the only R18 variation that structures the Inertia Verdict as a labeled three-component synthesis template:

> **Inertia Case** (structured -- all three components required):
> 1. **Competitor named** (reference Step 1a framing): State what "doing nothing" looks like for `{topic}` specifically...
> 2. **Carrying cost accumulating** (reference Step 1b + Gap Register findings): Name the specific Gap Register finding and the Step 1b carrying-cost metric (rate + horizon)...
> 3. **Tipping point** (reference Step 1c): Name the specific threshold from Step 1c at which the accumulating carrying cost becomes operationally irreversible...

All other variations have prose Inertia Verdict sections requiring a threat level + 2-3 sentences. V-05's structured template:
- Mandates explicit cross-references to prior steps (Step 1a, Step 1b, Step 1c) in each component
- Closes the loop between the Pre-Commitment Document (which establishes carrying costs and tipping points) and the Inertia Verdict (which synthesizes them)
- Each component is independently checkable: a scorer can verify that Component 1 cites Step 1a, Component 2 cites Step 1b + a named Gap Register finding, Component 3 cites Step 1c

Gap closed: All variations require an Inertia Verdict but allow prose synthesis without mandated back-references. A prose verdict can acknowledge inertia risk without closing the loop to the pre-committed values. The structured Inertia Case requires the verdict to be traceable to named pre-commitment entries — making it auditable rather than narrative.

Orthogonality to existing criteria: No existing criterion governs Inertia Verdict structure or mandates cross-references between the Inertia Verdict and the Pre-Commitment Document steps. The Pre-Commitment Document criteria (C-48/C-49/C-50) govern the document's enforcement structure, not its downstream synthesis usage.

Cracked by: **V-05 only**.

---

### v18 Discrimination Summary

All five variations reach 84/84 uncapped, producing the first five-way perfect tie at the rubric ceiling:

| Rank | Variation | C-48 | C-49 | C-50 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 (tie) | **V-01** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-02** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-03** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-04** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-05** | PASS | PASS *(new)* | PASS | **84/84** |

**Open for R19**: Extract C-51/C-52/C-53 from R18 excellence signals E-37/E-38/E-39. Most structurally significant candidate is E-37 (per-stage enforcement restatement at stage-specification level — V-03's fourth hierarchy level), followed by E-39 (structured Inertia Case — V-05's mandatory step cross-references).

---

```json
{"top_score": 84, "all_essential_pass": true, "new_patterns": ["Per-stage enforcement restatement at stage-specification level — V-03 introduces a fourth enforcement hierarchy level below column-contract granularity, carrying Rule B at the exact stage-authoring moment rather than at column-scan time", "Rule Constraint column in Pre-Commitment Assessment Table — V-02 separates enforcement citations from fill instructions into a dedicated scannable column, making C-49 compliance independently verifiable by column scan without content-column parsing", "Structured three-part Inertia Case with mandatory step cross-references — V-05 structures the Inertia Verdict as a labeled three-component synthesis template requiring explicit citations to Step 1a, Step 1b, and Step 1c, making the verdict traceable to pre-committed values rather than narrative"]}
```
