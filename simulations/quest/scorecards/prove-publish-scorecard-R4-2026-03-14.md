Scorecard written to `simulations/quest/scorecards/prove-publish-scorecard-R4-2026-03-14.md`.

---

## Quest Score -- prove-publish R4

### Rankings

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-01: Checklist-Symmetry-Chain** | **114/114** | YES |
| 1 | **V-05: Quad-Criterion-Distribution** | **114/114** | YES |
| 3 | V-02: Structural-Visibility-Table | 112/114 | YES |
| 4 | V-04: Document-Header-Declaration | 111/114 | YES |
| 5 | V-03: Scaffold-Audit-Section | 109/114 | YES |

All five are Golden. The R4 ceiling is 114; two variations hit it.

---

### R4 Criterion Discrimination

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17 Pre-flight mirrors post-review | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-18 FW table machine-visible column | PASS | PASS | **FAIL** | PARTIAL | PASS |
| C-19 Scaffold conflict mechanism | PASS | PARTIAL | PASS | **FAIL** | PASS |
| C-20 Non-negotiables forward-declared | PASS | PASS | **FAIL** | PASS | PASS |

**The C-18/C-19 split is the R4 discriminator.** V-03 and V-04 are mirror images: V-03 solves C-19 definitively but misses C-18 and C-20. V-04 solves C-17 and C-20 definitively but misses C-19. Only V-01 and V-05 pass all four.

---

### Excellence Signals (5 new patterns)

1. **Pre-Skeptic writes C-20 block before investigation begins** -- V-05's defining axis. A NON-NEGOTIABLES block produced in Phase 2 (before any evidence or prose) by a role that doesn't write the paper cannot be retrofitted to match what the paper ended up saying. V-01 adds the block during paper writing (same role); V-05's production-time sequence is the enforcement distinction.

2. **SCAFFOLD AUDIT as required subsection with per-finding slots** -- C-19 only holds when every finding has a structural slot (CONFIRMED or CONFLICT). A missing slot is a blank. A "state reason" prose instruction (V-04) has no structural home and no attestation path for the no-change case.

3. **PF-NN antecedent ID transforms C-17 from reader comparison to field-level check** -- a "[Pre-flight antecedent: PF-NN]" field per post-review item makes symmetry machine-verifiable. Variations without this ID system (V-02, V-03) can only claim design-level symmetry.

4. **FW Status column as binary classification distinct from anchor content** -- the Status column (B-NN ANCHOR / NET-NEW) is a separate field from the B-NN anchor value. A blank Status cell is visible without reading anchor content. Block formats (V-03, V-04) require reading the anchor field to determine classification.

5. **Role separation: Mid-Skeptic produces scaffold, Lead Author writes prose** -- when a different named role commits the novelty scaffold before prose exists, C-14 and C-19 enforcement is structurally independent. Lead Author's only option when findings diverge is to file a SCAFFOLD CONFLICT entry -- bypassing it requires explicitly failing a named sole responsibility.

---

```json
{"top_score": 114, "all_essential_pass": true, "new_patterns": ["pre-skeptic-writes-C20-block-before-investigation-in-phase-2-not-lead-author-during-paper-writing", "scaffold-audit-required-subsection-with-per-finding-slots-missing-slot-is-blank-not-absent-sentence", "PF-NN-antecedent-ID-field-per-post-review-item-transforms-C17-from-reader-comparison-to-field-check", "FW-status-column-as-binary-classification-distinct-from-anchor-content-cell", "role-separation-mid-skeptic-scaffold-producer-vs-lead-author-prose-writer-strongest-C14-C19-enforcement"]}
```
fore Findings Prose)": classifications committed after citation audit passes, before Phase 6 finding prose |
| C-15 | Skeptic post-review structured | PASS (2/2) | Phase 7 SKEPTIC POST-REVIEW: Items 1-5 with PASS/FLAG per item; pre-flight prediction outcome; "Final verdict: [APPROVED] or [FLAG: items N failed -- paper must be amended]"; panel blocked until APPROVED |
| C-16 | Future Work closes Status Quo loop | PASS (2/2) | Phase 6 FW table: column rules require "at least one row carries Status: B-NN ANCHOR naming a gap from the Status Quo section"; NON-NEGOTIABLES item 5 references it |
| C-17 | Pre-flight mirrors post-review | PASS (2/2) | PF-01 through PF-05 IDs emitted in Phase 2 Output A. Phase 7 requires "[Pre-flight antecedent: PF-NN]" per checklist item; "C-17 minimum: at least 3 items cite a PF-NN from Phase 2 Output A. Result: [N of 5]." Symmetry is one named field per item, not a reader comparison. |
| C-18 | FW table machine-visible column | PASS (2/2) | Phase 6 FW table has B-NN Anchor AND Status columns; "Status: 'B-NN ANCHOR' or 'NET-NEW' -- blank Status = structural failure"; at least one B-NN ANCHOR row required; NON-NEGOTIABLES item 5 enforces it |
| C-19 | Scaffold conflict mechanism | PASS (2/2) | Phase 6 Findings: SCAFFOLD AUDIT required subsection before finding prose; per-finding slots with CONFIRMED or CONFLICT (4 fields: finding ID, original, revised, reason); "ATTESTATION (if no conflicts): All [N] pre-committed classifications confirmed. No changes." Both pass paths covered. |
| C-20 | Non-negotiables forward-declared | PASS (2/2) | Phase 6: "Paper opens with a NON-NEGOTIABLES BLOCK before the Abstract. This is the first visible element of the document. A reviewer can check these without reading any section content." 5 verifiable items; none are generic quality statements. |

**V-01 Total: 114/114** -- All essential pass. All aspirational pass. Golden. Defining R4 achievement: PF-NN ID system makes C-17 a field-level check -- the Skeptic cites "Pre-flight antecedent: PF-02" as a named reference, not a conceptual claim of symmetry. The SCAFFOLD AUDIT subsection combines C-14 and C-19 in a single mechanism: per-finding slots enforce structure, and the ATTESTATION line closes both pass paths (conflict present OR no-change confirmed).

---

### V-02: Structural-Visibility-Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | PASS (12/12) | Phase 6 lists all 8 sections with per-section guidance; PAPER NON-NEGOTIABLES item 1 explicitly names all 8 |
| C-02 | Hypothesis explicitly resolved | PASS (12/12) | Phase 5 HYPOTHESIS VERDICT: "Not accepted: 'The evidence is mixed.' / 'The evidence suggests...'" -- committed sentence, no hedging; SQ-04 checks it |
| C-03 | Evidence traceable | PASS (12/12) | Phase 3 citation format; CITATION AUDIT hard gate; "Do not proceed to Phase 4 until Status: PASS"; SQ-02 checks CITATION AUDIT in post-review |
| C-04 | Findings synthesized | PASS (12/12) | Phase 4 FINDING CLASSIFICATION TABLE committed before prose; "conclusion answering 'what does this mean?' -- not 'what happened?'" |
| C-05 | Principles extractable | PASS (12/12) | "Always X", "When Y, do Z", "Prefer A over B because..." minimum 2 numbered; P-01 [from F-02] required |
| C-06 | Panel review, 2+ named roles | PASS (10/10) | Phase 8: Domain Expert (critique + N/10) + Practitioner (critique + N/10) -- two named roles |
| C-07 | Abstract standalone | PASS (10/10) | Phase 6: "<200 words: question, method, key finding, implication. Not structure. Written after verdict is known." |
| C-08 | Future Work concrete | PASS (10/10) | Phase 6 FW table: minimum 2 rows; "at least one row must carry Status: B-NN ANCHOR"; SQ-05 checks; FW template provided |
| C-09 | Principles cross-referenced | PASS (2/2) | "Each cites finding: P-01 [from F-02]: ..." -- required |
| C-10 | Cold-start readable | PASS (2/2) | Phase 6 Method: "Cold-start readable: define domain-specific terms on first use." Prior Belief Table orients new readers. |
| C-11 | Findings classified by novelty | PASS (2/2) | Phase 4 FINDING CLASSIFICATION TABLE: dedicated Classification column (BASELINE MATCH/NEW SIGNAL) required per row; RECLASSIFICATION ROW for post-prose changes |
| C-12 | Status Quo prior beliefs | PASS (2/2) | Phase 2 Prior Belief Table: "Before writing any paper section, build the prior belief table." Minimum 2 rows. Precedes Hypothesis. |
| C-13 | Citation audit precedes Findings | PASS (2/2) | Phase 3 CITATION AUDIT: "Do not proceed to Phase 4 until Status: PASS" -- hard gate |
| C-14 | Novelty scaffold pre-committed | PASS (2/2) | Phase 4 "Finding Classification Table (Before Findings Prose)": committed from Evidence only; "To reclassify after prose: add a RECLASSIFICATION ROW. Reclassification without a reason row fails C-14." |
| C-15 | Skeptic post-review structured | PASS (2/2) | Phase 7 SKEPTIC POST-REVIEW: SQ-01 through SQ-05, PASS/FLAG per item, APPROVED/FLAG verdict; panel blocked until APPROVED |
| C-16 | Future Work closes Status Quo loop | PASS (2/2) | FW table column rules: "at least one row must carry Status: B-NN ANCHOR"; SQ-05 checks; C-12 passes |
| C-17 | Pre-flight mirrors post-review | PARTIAL (1/2) | SQ-01 through SQ-05 items can be traced conceptually to the 3 prompt-level non-negotiable rules and the paper NON-NEGOTIABLES requirement, but no PF-NN IDs are emitted in Phase 2 and no "[Pre-flight antecedent: PF-NN]" fields appear in Phase 7. Symmetry exists by design but is not machine-verifiable via named reference. A reviewer must compare two blocks to confirm alignment. |
| C-18 | FW table machine-visible column | PASS (2/2) | Phase 6 FW table: B-NN Anchor AND Status columns; "Status must be 'B-NN ANCHOR' or 'NET-NEW' -- no blank Status cells"; "A blank Status cell is a structural failure visible without reading the question text"; SQ-05 checks |
| C-19 | Scaffold conflict mechanism | PARTIAL (1/2) | Phase 4 RECLASSIFICATION ROW has all 4 required fields: "RECLASSIFICATION: F-NN / Original: [...] / Revised: [...] / Reason: [...]". Satisfies the conflict-present path of C-19. Missing: explicit no-change attestation path. If all classifications remain unchanged, there is no ATTESTATION statement -- a paper where RECLASSIFICATION ROW is absent cannot be distinguished from silent reclassification vs. genuine no-conflict. |
| C-20 | Non-negotiables forward-declared | PASS (2/2) | Phase 6 paper output opens with PAPER NON-NEGOTIABLES block before the Abstract: "This block is not a section -- it is a pre-section compliance declaration. A reviewer can check it without reading any section content." 6 verifiable items. |

**V-02 Total: 112/114** -- All essential pass. Aspirational: 22/24. Golden. Losses: C-17 (no PF-NN ID system -- symmetry is design-claim only), C-19 (no-change attestation path not specified). V-02 is strongest on C-18 (Status column first introduced here) and C-20 among the single-axis variations; C-17 is its structural gap.

---

### V-03: Scaffold-Audit-Section

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | PASS (12/12) | Phase 5 lists all 8 sections with per-section guidance |
| C-02 | Hypothesis explicitly resolved | PASS (12/12) | Phase 4 HYPOTHESIS VERDICT: "Not accepted: 'The evidence suggests...' / 'Further investigation is needed.'" Committed sentence required |
| C-03 | Evidence traceable | PASS (12/12) | Phase 3 CITATION AUDIT: "Do not continue until Status: PASS"; E-[N] citation format; UNCITABLE routing |
| C-04 | Findings synthesized | PASS (12/12) | Phase 5 findings use pre-evidence scaffold; "conclusion answering 'what does this mean?' -- not 'what happened?'"; Phase 6 item 4 checks synthesis quality |
| C-05 | Principles extractable | PASS (12/12) | "Always X", "When Y, do Z", "Prefer A over B because..." minimum 2 numbered; P-01 [from F-02] required |
| C-06 | Panel review, 2+ named roles | PASS (10/10) | Phase 7: Domain Expert + Practitioner -- two named roles with substantive critique + N/10; Domain Expert assesses SCAFFOLD AUDIT conflict quality |
| C-07 | Abstract standalone | PASS (10/10) | Phase 5: "<200 words: question, method, key finding, implication. Not structure." |
| C-08 | Future Work concrete | PASS (10/10) | Phase 5 Future Work: "Minimum 2 specific investigable questions"; "Required: at least one item explicitly names a B-NN gap"; FW-NN block template with B-NN anchor field |
| C-09 | Principles cross-referenced | PASS (2/2) | "Each cites finding: P-01 [from F-02]: ..." -- required |
| C-10 | Cold-start readable | PASS (2/2) | Phase 5 Method: "Cold-start readable: define domain-specific terms on first use"; documents pre-evidence scaffold rationale for cold readers |
| C-11 | Findings classified by novelty | PASS (2/2) | Phase 2 Output B PRE-EVIDENCE NOVELTY CLASSIFICATION SCAFFOLD: BASELINE MATCH/NEW SIGNAL committed from artifact summaries before Evidence writing; carried into Phase 5 via SCAFFOLD AUDIT |
| C-12 | Status Quo prior beliefs | PASS (2/2) | Phase 2 Output A Prior Belief Inventory: minimum 2 concrete B-NN beliefs; written before any paper section; precedes Hypothesis in Phase 5 |
| C-13 | Citation audit precedes Findings | PASS (2/2) | Phase 3 CITATION AUDIT: "Do not continue until Status: PASS" -- hard gate |
| C-14 | Novelty scaffold pre-committed | PASS (2/2) | Phase 2 Output B: scaffold committed "from artifact summaries loaded in Phase 1 only -- before writing any evidence claim." Earliest possible C-14 intervention -- before Evidence writing, not just before Findings prose. |
| C-15 | Skeptic post-review structured | PASS (2/2) | Phase 6 SKEPTIC POST-REVIEW: 5 items, PASS/FLAG per item, APPROVED/FLAG verdict; panel blocked until APPROVED |
| C-16 | Future Work closes Status Quo loop | PASS (2/2) | Phase 5 Future Work: "Required: at least one item explicitly names a B-NN gap from the Status Quo section"; Phase 6 item 5 checks; C-12 passes |
| C-17 | Pre-flight mirrors post-review | PARTIAL (1/2) | Phase 6 Skeptic Post-Review has 5 items with PASS/FLAG, but no PF-NN IDs are emitted in Phase 2 and no "[Pre-flight antecedent: PF-NN]" fields appear in Phase 6. Items can be traced to Phase 2/3 pre-work commitments conceptually but not by named reference. A reviewer must compare two blocks. |
| C-18 | FW table machine-visible column | FAIL (0/2) | Phase 5 Future Work uses a per-block prose format: "FW-01 [addresses B-NN gap]: / Question: [...] / B-NN anchor: [B-ID] -- [gap] / Method: [...]". NOT a table with a Status column. Compliance requires reading the B-NN anchor field to determine status. C-18's machine-visibility requirement (blank Status cell visible without reading anchor content) is not met. |
| C-19 | Scaffold conflict mechanism | PASS (2/2) | Phase 5 Findings: SCAFFOLD AUDIT as required subsection before finding prose. One slot per finding from Phase 2 Output B. Each slot: "Status: CONFIRMED" or "Status: CONFLICT" with 4 required fields (Finding ID, Original classification, Revised classification, Reason). ATTESTATION: "[N] findings -- [N] confirmed, [N] reclassified (each has CONFLICT entry above)." Both pass paths explicitly covered. V-03's defining R4 axis. |
| C-20 | Non-negotiables forward-declared | FAIL (0/2) | Phase 5 paper structure begins with "1. Abstract" as the first element. No NON-NEGOTIABLES block is produced before the Abstract. The prompt has 3 non-negotiable rules at header scope, but C-20 requires them in the paper document "before Abstract or as the first visible element." The paper output does not open with such a block. |

**V-03 Total: 109/114** -- All essential pass. Aspirational: 19/24. Golden. Losses: C-17 (no PF-NN ID system), C-18 (FW block format, not table with Status column), C-20 (no paper-level NON-NEGOTIABLES block before Abstract). V-03 achieves the strongest C-14 (pre-evidence scaffold from raw artifacts, before Evidence writing) and most rigorous C-19 (SCAFFOLD AUDIT as required subsection with per-finding slots) of any single-axis variation, but its single-axis focus left C-18 and C-20 unaddressed.

---

### V-04: Document-Header-Declaration

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | PASS (12/12) | Phase 6 lists all 8 sections; PAPER STRUCTURAL COMMITMENTS item 1 names all 8 |
| C-02 | Hypothesis explicitly resolved | PASS (12/12) | Phase 5 HYPOTHESIS VERDICT: "Not accepted: 'The evidence is mixed.'" Rule 1 declares committed sentence required at header scope |
| C-03 | Evidence traceable | PASS (12/12) | Rule 2 (header): "CITATION AUDIT block with zero uncited claims before Findings." Phase 3 hard BLOCKED gate. PAPER STRUCTURAL COMMITMENTS item 2 references it. |
| C-04 | Findings synthesized | PASS (12/12) | Phase 6 findings: "conclusion answering 'what does this mean?'"; Phase 7 Item 4 checks; PAPER STRUCTURAL COMMITMENTS items 3-4 enforce scaffold-before-prose |
| C-05 | Principles extractable | PASS (12/12) | "Always X", "When Y, do Z", "Prefer A over B because..." minimum 2 numbered; P-01 [from F-02] required |
| C-06 | Panel review, 2+ named roles | PASS (10/10) | Phase 8: Domain Expert + Practitioner -- two named roles with critique + N/10 |
| C-07 | Abstract standalone | PASS (10/10) | Phase 6: "<200 words: question, method, key finding, implication. Not structure." |
| C-08 | Future Work concrete | PASS (10/10) | Rule 6 (header): "At least one Future Work item names a specific B-NN gap." Phase 6 FW: "Rule 6 requires this." |
| C-09 | Principles cross-referenced | PASS (2/2) | "Each cites finding: P-01 [from F-02]: ..." -- required |
| C-10 | Cold-start readable | PASS (2/2) | Phase 6 Method: "Cold-start readable: define terms on first use." Status Quo written by Skeptic pre-flight orients new readers before authoring begins. |
| C-11 | Findings classified by novelty | PASS (2/2) | Rule 3 (header): "Every finding carries a BASELINE MATCH or NEW SIGNAL tag." Phase 4 NOVELTY CLASSIFICATION SCAFFOLD; PAPER STRUCTURAL COMMITMENTS item 3 enforces it |
| C-12 | Status Quo prior beliefs | PASS (2/2) | Rule 1 (header): "Status Quo section produced by Skeptic before any paper section is written." Phase 2 Output B with minimum 2 concrete B-NN beliefs |
| C-13 | Citation audit precedes Findings | PASS (2/2) | Rule 2 (header): "CITATION AUDIT block with zero uncited claims before Findings." Phase 3: "Status: [PASS -- Findings unlocked] or [BLOCKED]" |
| C-14 | Novelty scaffold pre-committed | PASS (2/2) | Rule 4 (header): "Novelty classification scaffold committed in a named block before any finding prose." Phase 4: "Rules 3 and 4 require this block named and sequenced before Phase 6 finding prose." |
| C-15 | Skeptic post-review structured | PASS (2/2) | Rule 5 (header): "Skeptic Post-Review with 5+ item structural checklist and APPROVED/FLAG verdict." Phase 7: Items 1-5 with PF-NN antecedent references, APPROVED/FLAG verdict |
| C-16 | Future Work closes Status Quo loop | PASS (2/2) | Rule 6 (header): "At least one Future Work item names a specific B-NN gap." PAPER STRUCTURAL COMMITMENTS item 6 enforces it at paper level |
| C-17 | Pre-flight mirrors post-review | PASS (2/2) | Phase 2 PF-01 through PF-05 declared. Phase 7 Items 1-5 each carry "[Pre-flight antecedent: PF-NN]" by ID. "Rule 7 trace check: 5 items -- all 5 cite PF-NN antecedents from Phase 2 Output A. C-17 minimum (3 of 5 traceable): [N of 5]." PAPER STRUCTURAL COMMITMENTS item 7 enforces it. |
| C-18 | FW table machine-visible column | PARTIAL (1/2) | Phase 6 Future Work uses a per-block format: "FW-01: / Question: [...] / B-NN anchor: [B-ID] / Method: [...]" and "FW-02: / Anchor: NET-NEW". Dedicated anchor field per item and explicit NET-NEW marking present. Missing: a distinct Status column as a binary-classifiable field independent of anchor content. Machine-visibility of a blank Status cell is absent -- compliance requires reading the anchor field to determine B-NN ANCHOR vs NET-NEW classification. |
| C-19 | Scaffold conflict mechanism | FAIL (0/2) | Phase 6 Findings: "If reclassification from scaffold: state reason explicitly." Phase 9 Amend: "If finding reclassified: state reason." This is a prose instruction without a structured SCAFFOLD CONFLICT entry (finding ID + original + revised + reason as named fields), and without an attestation mechanism for the no-change path. Silent reclassification is not prevented by structure. |
| C-20 | Non-negotiables forward-declared | PASS (2/2) | Rule 8 (header): "Paper output opens with a PAPER STRUCTURAL COMMITMENTS block before the Abstract, listing Rules 1-8 in verifiable form." Phase 6 opens with PAPER STRUCTURAL COMMITMENTS block (8 items) as "first visible element." "Each commitment is verifiable by scanning structure. A reviewer may reject if any is absent." |

**V-04 Total: 111/114** -- All essential pass. Aspirational: 21/24 (C-18 partial, C-19 fail). Golden. Losses: C-18 (FW block format, not table with Status column), C-19 (scaffold conflict is prose instruction only -- no 4-field structure, no no-change attestation). V-04 achieves the fullest forward-declaration at both prompt level (8 rules, each mapped to a phase) and paper level (PAPER STRUCTURAL COMMITMENTS block), and the strongest C-17 among non-V-05 variations. C-19 is V-04's structural gap: the 8-rule architecture covered C-17 and C-20 as R4 innovations but did not add SCAFFOLD AUDIT subsection structure.

---

### V-05: Quad-Criterion-Distribution

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | PASS (12/12) | Phase 6 lists all 8 sections with per-section guidance; Phase 2 Output A NON-NEGOTIABLES block item 1 names required sections |
| C-02 | Hypothesis explicitly resolved | PASS (12/12) | Phase 5 HYPOTHESIS VERDICT: "Not accepted: 'The evidence is mixed.' / 'Further work is needed.'" N-03 requires verbatim verdict sentence in Findings |
| C-03 | Evidence traceable | PASS (12/12) | Phase 4 Mid-Skeptic Task A: line-by-line citation audit per evidence item ("E-01: [CITED -- source: file.md, section] or [UNCITED -- move to Limitations]"); "Total: [N] | Cited: [N] | Uncited (must be 0): [N] Status: [PASS -- Task B unlocked] or [BLOCKED]"; separate named role, not just a format check |
| C-04 | Findings synthesized | PASS (12/12) | Phase 4 Mid-Skeptic Task B produces provisional scaffold before prose; Phase 6 findings use SCAFFOLD AUDIT final classifications; "conclusion answering 'what does this mean?'"; Phase 7 Item 4 checks |
| C-05 | Principles extractable | PASS (12/12) | "Minimum 2 numbered action-oriented rules. Each cites finding: P-01 [from F-02]: ..." -- required |
| C-06 | Panel review, 2+ named roles | PASS (10/10) | Phase 8: Domain Expert (critique + N/10, including scaffold conflict assessment) + Practitioner (critique + N/10) -- two named panel roles structurally separate from the three Skeptic roles |
| C-07 | Abstract standalone | PASS (10/10) | Phase 6: "<200 words: question, method, key finding, implication. Not structure." |
| C-08 | Future Work concrete | PASS (10/10) | Phase 6 FW table: "Lead Author owns C-18 -- table with Status column required." N-04 requires at least one B-NN ANCHOR row; FW template provided; Phase 7 checks N-04 |
| C-09 | Principles cross-referenced | PASS (2/2) | "Each cites finding: P-01 [from F-02]: ..." -- required |
| C-10 | Cold-start readable | PASS (2/2) | Phase 6 Method includes: "Evidence was audited by Mid-Skeptic; novelty scaffold committed by Mid-Skeptic before Findings were written" -- explains method choice; Pre-Skeptic Status Quo orients new readers |
| C-11 | Findings classified by novelty | PASS (2/2) | Phase 4 Mid-Skeptic Task B MID-SKEPTIC NOVELTY SCAFFOLD: per-finding Provisional classification column (BASELINE MATCH/NEW SIGNAL) with Evidence basis; Lead Author uses SCAFFOLD AUDIT final classifications |
| C-12 | Status Quo prior beliefs | PASS (2/2) | Phase 2 Output C: Pre-Skeptic writes Status Quo before Lead Author writes anything; minimum 2 concrete B-NN beliefs; precedes Hypothesis in Phase 6 |
| C-13 | Citation audit precedes Findings | PASS (2/2) | Phase 4 Mid-Skeptic Task A: separate named role performs line-by-line audit; "If BLOCKED: specify which items. Lead Author fixes. Mid-Skeptic re-runs Task A." Role handoff enforces gate more strongly than a format check -- the evidence-writer and the auditor are different actors |
| C-14 | Novelty scaffold pre-committed | PASS (2/2) | Phase 4 Mid-Skeptic Task B: "Classifications committed from evidence items only, before any finding prose. Lead Author uses them in Phase 6." Role separation -- scaffold producer (Mid-Skeptic) is distinct from prose writer (Lead Author) |
| C-15 | Skeptic post-review structured | PASS (2/2) | Phase 7 POST-SKEPTIC: "Post-Skeptic's job: structural checklist audit + verdict. Nothing else." Items 1-5 with PF-NN antecedent trace, APPROVED/FLAG verdict; panel blocked until APPROVED; single-job isolation prevents abbreviation under session drift |
| C-16 | Future Work closes Status Quo loop | PASS (2/2) | Phase 6 FW table: N-04 requires at least one row Status: B-NN ANCHOR; Phase 7 checks N-04; Phase 9 confirms B-NN anchor retained after amendments; C-12 passes |
| C-17 | Pre-flight mirrors post-review | PASS (2/2) | Phase 2 Output B: PF-01 through PF-05 IDs declared by Pre-Skeptic. Phase 7 Post-Skeptic items each carry "[Pre-flight antecedent: PF-NN]" by ID. "All 5 items cite PF-NN antecedents from Phase 2 Output B. C-17 minimum (3 of 5 traceable): [N of 5 traceable]." Post-Skeptic's only new R4 job is this trace -- single-job isolation prevents it from being dropped. |
| C-18 | FW table machine-visible column | PASS (2/2) | Phase 6 FW table: B-NN Anchor AND Status columns; "A blank Status cell is a structural failure visible without reading the content"; Status: "B-NN ANCHOR" or "NET-NEW"; N-04 enforces at least one B-NN ANCHOR row; Lead Author is sole C-18 owner -- no competing responsibilities |
| C-19 | Scaffold conflict mechanism | PASS (2/2) | Phase 4 Mid-Skeptic Task B: "Provisional classifications may not be silently changed." Phase 6 SCAFFOLD AUDIT: per-finding slots with CONFIRMED or CONFLICT (4 required fields: finding ID, original, revised, reason); ATTESTATION: "[N] findings -- [N] confirmed, [N] reclassified with CONFLICT entries." Mid-Skeptic owns C-19 exclusively -- cannot be abbreviated without failing a named role's named sole responsibility. |
| C-20 | Non-negotiables forward-declared | PASS (2/2) | Phase 2 Output A: Pre-Skeptic writes NON-NEGOTIABLES block (N-01 through N-05) before any paper section exists -- in Phase 2, before Phase 3 Evidence, before Lead Author writes. Lead Author inserts it verbatim as first visible element in Phase 6. Production-time sequence is the C-20 ceiling: the block is produced by a different role at a different phase from the paper itself. Cannot be retrofitted after writing. |

**V-05 Total: 114/114** -- All essential pass. All aspirational pass. Golden. Defining R4 achievement: each of C-17, C-18, C-19, C-20 owned by exactly one role with no competing R4 responsibilities. Pre-Skeptic's C-20 implementation is the R4 ceiling: NON-NEGOTIABLES block produced in Phase 2 before the investigation begins -- before any evidence or prose exists. A block written before the investigation cannot be tailored to what the paper ended up saying.

---

### Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01: Checklist-Symmetry-Chain | 5/5 | 3/3 | 12/12 | 114 | YES |
| 1 | V-05: Quad-Criterion-Distribution | 5/5 | 3/3 | 12/12 | 114 | YES |
| 3 | V-02: Structural-Visibility-Table | 5/5 | 3/3 | 10/12 + 2 partial | 112 | YES |
| 4 | V-04: Document-Header-Declaration | 5/5 | 3/3 | 10/12 + 1 partial | 111 | YES |
| 5 | V-03: Scaffold-Audit-Section | 5/5 | 3/3 | 9/12 + 1 partial | 109 | YES |

All five variations are Golden. The R4 discriminating question: which variations enforced C-17, C-18, C-19, C-20 structurally vs. by prose instruction.

---

### Criterion-level R4 discrimination

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17 Pre-flight mirrors post-review | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-18 FW table machine-visible column | PASS | PASS | FAIL | PARTIAL | PASS |
| C-19 Scaffold conflict mechanism | PASS | PARTIAL | PASS | FAIL | PASS |
| C-20 Non-negotiables forward-declared | PASS | PASS | FAIL | PASS | PASS |

The C-18/C-19 split: V-02 and V-04 both solve C-20 but diverge on C-18 (V-02 has Status column, V-04 uses prose blocks) and C-19 (V-02 has RECLASSIFICATION ROW with 4 fields but no attestation, V-04 gives only a "state reason" instruction). V-03 and V-04 are mirror images: V-03 solves C-19 definitively (required subsection per finding) but misses C-18 and C-20; V-04 solves C-17 and C-20 definitively but misses C-19. Only V-01 and V-05 pass all four R4 criteria.

---

### Excellence Signals from R4

1. **Pre-Skeptic as C-20 author before investigation begins** (V-05 defining axis): The strongest C-20 implementation is when the NON-NEGOTIABLES block is produced by a named role in Phase 2 -- before any evidence, prose, or findings exist -- and inserted verbatim by Lead Author in Phase 6. A block written before the investigation cannot be tailored to what the paper ended up saying. V-01 adds the block during Phase 6 paper writing (same role that writes the paper); V-05's Pre-Skeptic produces it as an independent Phase 2 output. The production-time sequence is the C-20 distinction between enforcement and compliance-in-retrospect.

2. **SCAFFOLD AUDIT as required subsection with per-finding slots** (V-01, V-03, V-05 all pass C-19): C-19 is only fully enforced when the conflict mechanism has a structural home (required subsection) with a slot per finding. Every finding has a slot regardless of whether conflict occurred -- a missing slot is a blank, a silent reclassification is a structural failure visible without reading prose. The ATTESTATION line closes the no-change path. V-04's "state reason" instruction fails C-19 because it produces no structural home and no attestation when no changes occur.

3. **PF-NN antecedent ID as machine-verifiable symmetry field** (V-01, V-04, V-05 pass C-17; V-02, V-03 only partial): A "[Pre-flight antecedent: PF-NN]" field per checklist item transforms C-17 from a reader comparison into a field-level check. A blank or mismatched PF-NN citation is detectable without reading the checklist items' content. Variations without this ID system can only claim design-level symmetry.

4. **FW table Status column as binary classification distinct from anchor content** (V-01, V-02, V-05 pass C-18; V-03 fail, V-04 partial): The Status column (B-NN ANCHOR / NET-NEW) is a separate field from the B-NN Anchor column. A blank Status cell is visible without reading the anchor value. V-03 and V-04 use block formats where anchor presence encodes status -- compliance requires reading anchor content to determine classification. The Status column makes C-18 a true machine-visible binary check.

5. **Role separation between scaffold production and prose writing** (V-05 Mid-Skeptic, strongest C-14 + C-19 enforcement): When the novelty scaffold is produced by a named role (Mid-Skeptic) separate from the prose writer (Lead Author), independence enforces C-14 more strongly than any self-enforcement can. Mid-Skeptic cannot rationalize scaffold entries to fit prose that hasn't been written yet. Lead Author's only option when findings diverge from the Mid-Skeptic scaffold is to file a SCAFFOLD CONFLICT entry in SCAFFOLD AUDIT -- bypassing the mechanism requires explicitly failing a named role's named sole responsibility.

---

```json
{"top_score": 114, "all_essential_pass": true, "new_patterns": ["pre-skeptic-writes-C20-block-before-investigation-in-phase-2-not-lead-author-during-paper-writing", "scaffold-audit-required-subsection-with-per-finding-slots-missing-slot-is-blank-not-absent-sentence", "PF-NN-antecedent-ID-field-per-post-review-item-transforms-C17-from-reader-comparison-to-field-check", "FW-status-column-as-binary-classification-distinct-from-anchor-content-cell", "role-separation-mid-skeptic-scaffold-producer-vs-lead-author-prose-writer-strongest-C14-C19-enforcement"]}
```
