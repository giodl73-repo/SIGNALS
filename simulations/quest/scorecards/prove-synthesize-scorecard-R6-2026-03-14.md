## prove-synthesize — Round 6 Scorecard

### Scores

| Variation | Total | Status |
|-----------|-------|--------|
| V-05 | **132.5** | GOLDEN (max) |
| V-03 | **122.5** | GOLDEN |
| V-04 | **122.5** | GOLDEN |
| V-01 | **120.0** | GOLDEN |
| V-02 | **117.5** | GOLDEN |

All five Golden. New maximum: **132.5 / 132.5** (V-05).

---

### Aspirational Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 through C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 (role prohibitions) | FAIL | FAIL | PASS | PASS | PASS |
| C-17 (record-specific) | PASS | PASS | PASS | PASS | PASS |
| C-18 (register word opens) | PASS | PASS | PASS | PASS | PASS |
| C-19 (frontmatter at open) | PASS | FAIL | FAIL | FAIL | PASS |
| C-20 (phase-sequenced fill) | PASS | FAIL | FAIL | PASS | PASS |
| C-21 (SURVEYOR-traceable) | FAIL | PASS | PASS | PASS | PASS |
| C-22 (dual-layer enforcement) | FAIL | FAIL | PASS | PASS | PASS |
| **C-23 (named-violation gates)** | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-24 (arrow-chain diagnosis)** | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| **C-25 (pre-JUDGE pre-flight)** | FAIL | FAIL | **PASS** | FAIL | **PASS** |

---

### Three Calibration Q Answers

**Q1 (C-23 embedding vs. standalone):** C-23 fires with inline embedding. V-01's pattern — "Filling X is a PREMATURE COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION." — satisfies the criterion. Named violation types do not need to appear as standalone labels outside the prohibition text.

**Q2 (C-24 prose-only vs. two-site):** C-24 fires with arrow-chain in RECORD DIAGNOSIS alone (V-02 PASS, no PRE-FLIGHT). PRE-FLIGHT audit verification is not required. The arrow-chain syntax is the criterion; audit propagation is C-27 territory.

**Q3 (C-25 phase count):** Three-phase PRE-FLIGHT fully satisfies C-25 (V-03 PASS). SCHEMA-CITATION AUDIT as a named Phase B produces a v7 candidate (C-27). V-03's structure is a fuller realization of C-25 and the direct C-27 predecessor.

---

### v7 Candidates Predicted

| ID | Name | Mechanism |
|----|------|-----------|
| C-26 | Violation registry at document open | All four violation types indexed as a named block before FRONTMATTER — C-23 is necessary but not sufficient |
| C-27 | Arrow-chain three-site chain of custody | Arrow chain propagates creation (ADVERSARY) → audit (PRE-FLIGHT Phase B) → application (JUDGE confidence reference) — C-24 + C-25 necessary but not sufficient |

---

```json
{"top_score": 132.5, "all_essential_pass": true, "new_patterns": ["named violation registry block before frontmatter indexes all four violation types before any fill window is encountered -- violation taxonomy visible before first constraint", "arrow-chain three-site chain of custody: RECORD DIAGNOSIS creates chain, PRE-FLIGHT Phase B audits it, JUDGE confidence paragraph applies it -- three named verification sites", "anti-skip gate on PRE-FLIGHT forecloses looking-complete-but-incomplete failure mode by naming it as PHASE-ADVANCE VIOLATION before the block can be bypassed"]}
```
|
| V-02 | 60.0 | 30.0 | 27.5 | **117.5** |
| V-03 | 60.0 | 30.0 | 32.5 | **122.5** |
| V-04 | 60.0 | 30.0 | 32.5 | **122.5** |
| V-05 | 60.0 | 30.0 | 42.5 | **132.5** |

---

### Criterion-by-criterion notes

**C-16**: V-01 has role phase labels (SURVEYOR, ADVERSARY, JUDGE headings) but no explicit prohibition statements ("A SURVEYOR does not evaluate... Violation is a procedural breach regardless of accuracy"). V-02 uses PHASE 1-5 titles with no role identity or prohibition. V-03, V-04, V-05 all carry both identity labels and explicit prohibition statements at each role section. FAIL for V-01/V-02.

**C-17**: V-01 ADVERSARY Paragraph 3 instructs "Name one failure mode this synthesis must avoid -- not generic, but derived from what the SURVEYOR found." This enforces record-specific derivation even without INVENTORY SCHEMA fields. V-02/V-03/V-04/V-05 reference INVENTORY SCHEMA values explicitly. All PASS.

**C-19**: V-01 and V-05 open with FRONTMATTER DECLARATIONS block before any phase content begins. V-02, V-03, V-04 state frontmatter fields only in the end-of-artifact "Write artifact" section. FAIL for V-02/V-03/V-04.

**C-20**: V-01 has fill-window instructions on each frontmatter field with phase-sequenced bounds (signal_count: set after SURVEYOR COMPLETE, adversary_pre_determination: set at ADVERSARY, etc.). V-04 has phase-exit fill instructions embedded in gate text ("Set adversary_pre_determination: true in frontmatter now") and PHASE-ADVANCE VIOLATION labels at exits. Both satisfy sequential determinability. V-02 and V-03 have no phase-sequenced fill instructions; frontmatter at end only. FAIL for V-02/V-03.

**C-21**: V-01 has no INVENTORY SCHEMA; the ADVERSARY challenge cannot cite named schema fields by value. Cross-reference is not possible. FAIL for V-01. V-02/V-03/V-04/V-05 all produce INVENTORY SCHEMA with five named fields; their ADVERSARY challenges require citing those fields by name and exact value. PASS for V-02/V-03/V-04/V-05.

**C-22**: Requires an instruction-level NOT: gate that explicitly names the positional failure modes ("NOT: the register word appears after introductory language ('Our final DETERMINATION is:' / 'Based on the foregoing, DETERMINATION:')"). V-01's DETERMINATION SEAL: "NOT: DETERMINATION: is absent from the opening sentence" -- addresses presence, not positional placement. V-02's DETERMINATION GATE: same. V-03's PRE-FLIGHT PHASE C: "NOT: the commitment sentence begins with any word other than the register word. 'Our final DETERMINATION is:' violates this gate before you write it. 'Based on the foregoing, DETERMINATION:' violates this gate before you write it." -- specific positional examples. V-04's DETERMINATION SEAL: "NOT: the register word appears after introductory language ('Our final DETERMINATION is:', 'Based on the foregoing, DETERMINATION:')..." -- same specific language. V-05: both PHASE C and DETERMINATION SEAL with examples. FAIL for V-01/V-02; PASS for V-03/V-04/V-05.

**C-23**: Requires both premature and deferred named violation labels on each fill-window bound (where both bounds are structurally applicable).

- V-01: "Filling signal_count before any SURVEYOR content is written is a PREMATURE COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION. Filling signal_count after ADVERSARY content begins is a DEFERRED COMPLETION VIOLATION. Named violation type: DEFERRED COMPLETION VIOLATION." Both bounds named for all applicable fields (signal_count, adversary_pre_determination, answer). Fields with one directional bound only (confidence: only premature; register_word_used: only premature) are not counterexamples -- no deferred bound is structurally applicable. PASS.
- V-02: No fill-window bounds; frontmatter at end only. No named violation categories. FAIL.
- V-03: Phase-exit statements do not name violation types. "SURVEYOR COMPLETE." has no named violation label for premature or deferred fill on individual fields. FAIL.
- V-04: Phase-exit PHASE-ADVANCE VIOLATION labels catch the "advancing without field set" direction (deferred). No PREMATURE COMPLETION VIOLATION labels for any field. C-23 requires both bounds; only one direction named. FAIL.
- V-05: Full named violation on all applicable fields -- PREMATURE COMPLETION VIOLATION for early fill, DEFERRED COMPLETION VIOLATION for late fill where applicable, FALSE ATTESTATION VIOLATION for wrong-state booleans. Plus named violation types indexed before FRONTMATTER. PASS.

**Calibration Q1 answer (R6)**: C-23 fires with inline embedding. V-01's pattern -- "Filling X is a PREMATURE COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION." -- satisfies C-23. The named violation type does not need to appear as a standalone citable label outside the NOT: text. Embedding the name within the fill-window sentence is sufficient. C-23 confirmed to fire on V-01.

**C-24**: Requires arrow-chain field:value notation in RECORD DIAGNOSIS with NOT: gates foreclosing prose and bracket-placeholder formats. "RECORD DIAGNOSIS: convergence_pattern: thin -> failure mode: false confidence ceiling; coverage_gaps: none identified -> exposure: full hypothesis coverage assumed." One-lookup falsifiability.

- V-01: No INVENTORY SCHEMA. ADVERSARY paragraphs use prose instruction ("Name one failure mode... derived from what the SURVEYOR found"). No arrow-chain format instructed. FAIL.
- V-02: Arrow-chain notation required: "RECORD DIAGNOSIS: [INVENTORY SCHEMA field]: [exact value from Phase 1 INVENTORY SCHEMA] -> failure mode: [specific failure mode]; [INVENTORY SCHEMA field]: [exact value] -> exposure: [why...]." NOT: gates foreclose prose description and bracket-placeholder formats. Arrow-chain verification procedure documented. PASS.
- V-03: RECORD DIAGNOSIS is prose form -- "Name at least two INVENTORY SCHEMA fields by name and state their exact values as the basis for the diagnosis." ADVERSARY GATE verifies field names and values are cited but does not require arrow-chain syntax. FAIL.
- V-04: Arrow-chain required. NOT: gates foreclose prose and bracket-placeholder. PASS.
- V-05: Arrow-chain required. PASS.

**Calibration Q2 answer (R6)**: C-24 fires with arrow-chain in RECORD DIAGNOSIS prose alone (V-02 PASS without PRE-FLIGHT). C-24 does not require PRE-FLIGHT schema-citation audit to be present. The arrow-chain syntax in RECORD DIAGNOSIS is the criterion; audit verification is a PRE-FLIGHT extension (C-25/C-27 territory).

**C-25**: Requires a named pre-JUDGE structural phase (PRE-FLIGHT or equivalent), not the commitment gate itself.

- V-01/V-02: No PRE-FLIGHT block. FAIL.
- V-03: PRE-JUDGE PRE-FLIGHT with three named phases: (A) structural completeness, (B) SCHEMA-CITATION AUDIT, (C) register-word gate. Phase B is a distinct structural phase that verifies RECORD DIAGNOSIS schema citations before JUDGE begins. Positioned between ADVERSARY COMPLETE and JUDGE. PASS.
- V-04: No PRE-FLIGHT block. DETERMINATION SEAL is at commitment point (gate encountered at failure, not before). FAIL.
- V-05: PRE-JUDGE PRE-FLIGHT with same three-phase structure plus anti-skip gate ("NOT: this pre-flight block is skipped because the preceding sections appear complete -- the block exists to catch structural violations that read as complete. Skipping this block is a PHASE-ADVANCE VIOLATION."). PASS.

**Calibration Q3 answer (R6)**: Three-phase PRE-FLIGHT satisfies C-25 (V-03 PASS). SCHEMA-CITATION AUDIT as a named Phase B step constitutes a v7 candidate (C-27) beyond C-25. V-03's three-phase structure is a fuller realization of C-25 and a direct predecessor to C-27.

---

### Excellence Signals -- V-05

V-05 achieves 132.5/132.5. Mechanisms that differentiated V-05 from V-03 and V-04 (both at 122.5):

**1. Named violation registry before FRONTMATTER**
V-05 opens with an indexed vocabulary block listing all four violation types before the first field:
"Named violation types in this artifact: PREMATURE COMPLETION VIOLATION / DEFERRED COMPLETION VIOLATION / PHASE-ADVANCE VIOLATION / FALSE ATTESTATION VIOLATION."
A reviewer encounters the complete taxonomy before any fill window. No other variation has this pre-frontmatter registry.

**2. C-23 + C-19 integration -- compliance ledger**
V-05 combines frontmatter-at-open (C-19) with named violation categories (C-23). The frontmatter block becomes an auditable compliance ledger: each field carries its violation types, each boolean carries its attestation risk. A reviewer audits the ledger by violation class without re-reading phase content. V-01 has both C-23 and C-19 but lacks the FALSE ATTESTATION VIOLATION extension for boolean fields. V-04 has C-20 and C-22 but not C-19.

**3. Arrow-chain three-site chain of custody**
RECORD DIAGNOSIS creates the chain (ADVERSARY phase). PRE-FLIGHT PHASE B verifies it: "Identify the first INVENTORY SCHEMA field name cited in RECORD DIAGNOSIS arrow chain... Confirm the value cited in the arrow chain matches INVENTORY SCHEMA exactly." JUDGE confidence paragraph applies it: "reference the chain if the diagnosed risk is live -- e.g., 'convergence_pattern: thin -> failure mode: false confidence ceiling limits this score.'" Three sites: creation, audit, application. V-02 and V-04 create the chain; V-03 audits schema values; only V-05 does all three.

**4. PRE-FLIGHT anti-skip gate**
V-05 adds: "NOT: this pre-flight block is skipped because the preceding sections appear complete -- the block exists to catch structural violations that read as complete. Skipping this block is a PHASE-ADVANCE VIOLATION." V-03 has the three-phase structure but not this meta-gate. The anti-skip gate forecloses the failure mode of looking-complete-but-structurally-incomplete.

**v7 candidates predicted from V-05:**

| ID | Name | Mechanism | Predecessor |
|----|------|-----------|-------------|
| C-26 | Violation registry at document open | All named violation types indexed as a formal block before FRONTMATTER -- not embedded in fill-window text, but named and defined before any fill window is encountered | V-05 pre-frontmatter listing |
| C-27 | Arrow-chain three-site chain of custody | Arrow-chain propagates from RECORD DIAGNOSIS (creation) through PRE-FLIGHT PHASE B (audit) through JUDGE confidence paragraph (application reference) -- three named verification sites constituting a verification chain of custody | V-05 three-site propagation |

C-26 vs. C-23: C-23 requires named violation categories on each fill-window bound. C-26 requires a formal registry block at document open that indexes all named types before the first field is encountered. C-23 is necessary but not sufficient for C-26.

C-27 vs. C-24/C-25: C-24 requires arrow-chain syntax in RECORD DIAGNOSIS. C-25 requires PRE-FLIGHT Phase B to verify it. C-27 requires the arrow chain to be cited by notation at a third site in the JUDGE output -- the chain travels from creation to audit to application. C-24 and C-25 are necessary but not sufficient for C-27.

---

### Round Delta from R5

| Variation | R5 Score (v5) | R6 Score (v6) | Delta | New criteria passed |
|-----------|---------------|---------------|-------|---------------------|
| V-05 | 125.0 | **132.5** | +7.5 | C-23, C-24, C-25 all confirmed |
| V-03 | 115.0 | **122.5** | +7.5 | C-21, C-22 now pass (PRE-FLIGHT PHASE B enables SURVEYOR-traceable verification); C-25 confirmed |
| V-04 | 122.5 | **122.5** | 0.0 | C-24 added; C-23 fails (PHASE-ADVANCE only = one bound); net wash |
| V-01 | 115.0 | **120.0** | +5.0 | C-23 confirmed pass |
| V-02 | 115.0 | **117.5** | +2.5 | C-24 confirmed pass |

Note: V-03 delta requires explanation. R5 V-03 scored 115.0 with 10/14 aspirational (C-16/C-17/C-19/C-20 failing). Under v6 R6, V-03 base description was corrected per V-03 structure: "role prohibitions C-16, PRE-FLIGHT C-22/C-25." V-03 R6 passes C-16, C-17, C-21, C-22, C-25. Fails C-19, C-20, C-23, C-24. Net: 13/17 = 122.5. The +7.5 gain comes from C-21 and C-22 now firing correctly under R6 evaluation of the full three-phase PRE-FLIGHT structure.

---

### All Golden

All 5 variations: all essential pass, composite >= 90. Sixth consecutive Golden round for prove-synthesize.

New maximum under v6: 132.5 (previously 125.0 under v5).
