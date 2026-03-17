---

## scout-compliance R2 Scorecard

**All 5 variations: 109/109**

| Rank | Variation | Score | C-11 | C-12 | C-13 |
|------|-----------|-------|------|------|------|
| 1 (tie) | V-01: Section-contract | 109 | PASS | PASS | PASS |
| 1 (tie) | V-02: Synthesis-gate | 109 | PASS | PASS | PASS |
| 1 (tie) | V-03: Terse imperative | 109 | PASS | PASS | PASS* |
| 1 (tie) | V-04: Architect + template | 109 | PASS | PASS | PASS |
| 1 (tie) | V-05: Risk + synthesis | 109 | PASS | PASS | PASS |

*C-13 most fragile encoding — terse but sufficient.
**C-11 in V-05: passes by pass condition letter; violates spirit (VERDICT at position 2, not 1).

### Design bets resolved

| Bet | Prediction | Result |
|-----|-----------|--------|
| All 5 encode C-13 | All PASS | CONFIRMED |
| C-11/C-12 are section-ordering problems | Named headings in fixed order = sufficient | CONFIRMED |
| V-03 terse is the pivot test | Terse + section contract reaches 109 | CONFIRMED — instruction length is not the variable |
| V-05 synthesis gate rescues default-risk | Gate prevents omission; verdict lands at position 2 | PARTIALLY CONFIRMED — gate fixes omission, not displacement |

### Excellence signals

1. **Plant C-13 explicitly** — SR 11-7 misapplication framing is too specific to derive from "vendor vs. methodology" framing alone. R1: 1/5 emergent. R2: 5/5 planted.
2. **Section-contract template is portable** — named headings in fixed order produce C-11/C-12 across all phrasing registers.
3. **C-11 rubric gap exposed** — pass condition catches verdict *omission*; does not catch verdict *displacement* (VERDICT at position 2 passes the letter). Candidate v3 fix: require verdict as the first named output section heading.

### R1 -> R2 lift summary

V-01: 87→109 (+22) | V-02: 96→109 (+13) | V-03: 109→109 (0) | V-04: 106→109 (+3) | V-05: 95→109 (+14)

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["explicit C-13 instruction in all variations eliminates R1 emergent variance -- planting SR 11-7 misapplication text is the reliable mechanism; general vendor-vs-methodology framing is insufficient to elicit the specific misapplication warning", "section-contract template (named headings in fixed order) is portable across all phrasing registers -- terse, formal, lifecycle-gated, and risk-framed variations all hit C-11/C-12 with the same template; instruction style is not the variable", "DEFAULT RISK before VERDICT in V-05 exposes C-11 rubric gap: pass condition catches verdict omission but not verdict displacement -- verdict at position 2 passes the letter, violates the spirit; candidate v3 fix: require verdict as the first named section heading"]}
```
east one SATISFIED by design. At least one ACTION." | 10 |
| C-07 | PASS | ## VERDICT is first output section; form specified: "Do not hedge. Do not write 'it depends.'" | 10 |
| C-08 | PASS | "PCI DSS, GDPR, and CCPA are conditional. Mark each with its trigger condition. Do not assert universal applicability." + FRAMEWORK CATALOG requires UNIVERSAL/CONDITIONAL column | 10 |
| C-09 | PASS | ## REFRAME is second output section (before any framework table): "One sentence. Distinguish approving a methodology from approving a vendor." | 5 |
| C-10 | PASS | ## DATA-SENSITIVITY TIER section: "Recommend a tiering model (e.g., GREEN / YELLOW / RED) or identify the policy gap. Name a specific control or remediation." | 5 |
| C-11 | PASS | Section order: VERDICT(1) -> REFRAME(2) -> SR 11-7 WARNING(3) -> SCOPE BOUNDARY(4) -> FRAMEWORK CATALOG(5). Verdict before catalog. Reframe immediately follows verdict. Structural guarantee holds. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both appear as dedicated named section headings in the output contract | 3 |
| C-13 | PASS | CORE RULES explicitly: "SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling contexts. The misapplication occurs because teams see an AI tool and reflexively apply model risk rules to every component." + SR 11-7 MISAPPLICATION WARNING section requires anticipating compliance officer's objection | 3 |

**Verdict**: Clean 109. Section-contract is the most locked-down mechanism -- structure is defined, model fills content. C-13 encoding is substantive (multi-sentence explanation with mechanism). Most reliable variation for adversarial testing.

---

### V-02: Synthesis-gate (109/109)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain, data handling scope, and deployment model from repo context. Do not prompt. Identify >= 4 applicable frameworks from signals alone." | 12 |
| C-02 | PASS | Phase 1 ARCHITECT: "Which component calls external APIs? Who is the data processor?" + Phase 2 SCOPE BOUNDARY: "Signal: methodology, not vendor." | 12 |
| C-03 | PASS | Phase 1 COMPLIANCE: "SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling. The misapplication occurs because teams apply model risk rules to every component that touches AI." Committed in scratchpad; required in Phase 2 section. | 12 |
| C-04 | PASS | Phase 1 ARCHITECT: "What compliance properties does the git-native, no-server design provide?" + Phase 2 GIT-NATIVE ADVANTAGE section with framework linkage | 12 |
| C-05 | PASS | FINDINGS REGISTER: "IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: "Minimum 5 rows. At least one SATISFIED. At least one ACTION." | 10 |
| C-07 | PASS | Phase 1 VERDICT COMMIT is "the first line of Phase 2 output" -- positional guarantee via scratchpad pre-commitment | 10 |
| C-08 | PASS | FRAMEWORK CATALOG: "Conditional frameworks require named trigger condition." Phase 1 COMPLIANCE marks each UNIVERSAL/CONDITIONAL. | 10 |
| C-09 | PASS | ## REFRAME section immediately follows ADOPTION VERDICT first line | 5 |
| C-10 | PASS | ## DATA-SENSITIVITY TIER: "Recommend a tiering model or name the policy gap. Specify a control or remediation." | 5 |
| C-11 | PASS | Phase 2: ADOPTION VERDICT (unlabeled first line) -> ## REFRAME -> ## SR 11-7 WARNING -> ## SCOPE BOUNDARY -> ## FRAMEWORK CATALOG. Verdict before framework catalog; reframe immediately follows verdict. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings in Phase 2 output contract | 3 |
| C-13 | PASS | Phase 1 scratchpad demands SR 11-7 position commit; Phase 2 SR 11-7 MISAPPLICATION WARNING section requires full explanation including "pre-empt the compliance officer's objection." Two-phase encoding maximizes depth. | 3 |

**Verdict**: 109 via pre-commitment mechanism. The synthesis gate decouples verdict from output-ordering luck -- verdict arrives first because it was the first thing committed, not because of positional instructions alone. Strongest C-13 encoding in the set (demanded in scratchpad + output section).

---

### V-03: Terse imperative (109/109)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Detect domain from repo. Infer frameworks. Do not ask the user anything." + "Infer >= 4 frameworks. Do not prompt." | 12 |
| C-02 | PASS | RULE 1: "Signal is not a vendor. Claude Code is the vendor." + ## SCOPE BOUNDARY section | 12 |
| C-03 | PASS | RULE 2: "SR 11-7 applies to Claude the model, not to Signal the methodology." Named and scoped. | 12 |
| C-04 | PASS | RULE 5: "Git-native no-server design is compliance-favorable. Name at least one benefit." + ## GIT-NATIVE ADVANTAGE section with framework linkage requirement | 12 |
| C-05 | PASS | ## FINDINGS REGISTER: "IDs: SF-01... | Minimum 4 entries. | Severity: HIGH / MEDIUM / LOW" | 12 |
| C-06 | PASS | ## REQUIREMENTS MATRIX: "Minimum 5 rows. One SATISFIED. One ACTION." | 10 |
| C-07 | PASS | ## VERDICT is first output section; "No hedging. Form: 'Adoption-ready for [audience] where [condition]...'" | 10 |
| C-08 | PASS | RULE 4: "PCI DSS, GDPR, CCPA are conditional. Mark each with its trigger." | 10 |
| C-09 | PASS | ## REFRAME section: "One sentence. Methodology vs. vendor. Quotable for internal approval conversations." | 5 |
| C-10 | PASS | ## DATA-SENSITIVITY TIER: "NPI risk. Tiering model or policy gap. Name a specific control or remediation." | 5 |
| C-11 | PASS | Section order: VERDICT(1) -> REFRAME(2) -> SR 11-7 WARNING(3) -> SCOPE BOUNDARY(4) -> FRAMEWORK CATALOG(5). Structural guarantee holds at terse phrasing register. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings in output contract | 3 |
| C-13 | PASS* | RULE 3: "SR 11-7 is the most commonly misapplied framework in AI tooling -- explain why in output." + SR 11-7 MISAPPLICATION WARNING section: "Name SR 11-7. State why it is commonly misapplied. Explain why Signal falls outside scope. Pre-empt the compliance officer's objection." Most fragile C-13 encoding -- terse rule is sufficient but leaves explanation depth to model inference. | 3 |

**Verdict**: 109 at minimum instruction density. The pivot test result: instruction length is not the variable for C-11 and C-12 -- section ordering in the template is sufficient. C-13 is the fragility point: terse instruction ("explain why in output") combined with section-level directive ("Pre-empt the compliance officer's objection") reaches PASS, but has less redundancy than V-01/V-02/V-04. If R3 testing finds variance, the C-13 instruction should be expanded first.

---

### V-04: Architect-first + named sections (109/109)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Detect domain, data handling, and deployment model from repo context. Do not prompt. Identify >= 4 frameworks from signals alone." | 12 |
| C-02 | PASS | STEP 1 ARCHITECT establishes scope; output SCOPE BOUNDARY: "Claude Code / Anthropic is the data processor. Signal is a methodology, not a vendor." | 12 |
| C-03 | PASS | STEP 2 COMPLIANCE: "SR 11-7 applies to AI models, not to structured prompt methodologies. This is the most frequently misapplied framework in AI-adjacent tooling. The misapplication occurs because teams apply model risk rules to every component that touches AI -- but a prompt methodology that invokes a model is not itself a model." + output SR 11-7 MISAPPLICATION WARNING section | 12 |
| C-04 | PASS | STEP 1: "What compliance properties does the git-native, no-server design provide? Name each." + GIT-NATIVE ADVANTAGE output section with framework linkage | 12 |
| C-05 | PASS | FINDINGS REGISTER: "IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: "Minimum 5 rows. At least one SATISFIED. At least one ACTION." | 10 |
| C-07 | PASS | ## VERDICT is first output section: "One sentence. Name the adoption-readiness condition and audience. Do not hedge." | 10 |
| C-08 | PASS | STEP 2: "Mark PCI DSS, GDPR, CCPA as conditional with explicit trigger conditions." + FRAMEWORK CATALOG requires UNIVERSAL/CONDITIONAL column | 10 |
| C-09 | PASS | ## REFRAME section (second output section): "One sentence. Methodology approval vs. vendor approval. Quotable." | 5 |
| C-10 | PASS | ## DATA-SENSITIVITY TIER: "Recommend a tiering model (e.g., GREEN / YELLOW / RED) or name the policy gap. Name a specific control or remediation." | 5 |
| C-11 | PASS | Section order: VERDICT(1) -> REFRAME(2) -> SR 11-7 WARNING(3) -> SCOPE BOUNDARY(4) -> FRAMEWORK CATALOG(5). Role execution in STEPS 1-4 does not affect output ordering -- structural contract governs. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings in output contract | 3 |
| C-13 | PASS | STEP 2 contains full mechanism explanation ("teams apply model risk rules to every component that touches AI -- but a prompt methodology that invokes a model is not itself a model") + output SR 11-7 MISAPPLICATION WARNING requires anticipating objection. Best C-13 encoding alongside V-02. | 3 |

**Verdict**: 109 with double-encoding of scope (role execution + output template). Architect-first R1 hypothesis was sound but structurally incomplete; adding the section-contract template to R1 V-02 produces the missing gap-close. Most inspection-ready variation -- execution order maps to rubric sections 1:1.

---

### V-05: Default-risk + synthesis gate (109/109)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | "Auto-detect domain from repo. Do not prompt. Identify >= 4 frameworks from signals alone." | 12 |
| C-02 | PASS | Phase 1 SCOPE LOCK: "Which component calls external APIs? Who is the data processor?" + Phase 2 SCOPE BOUNDARY: "Claude Code / Anthropic: data processor. Signal: methodology, not vendor." | 12 |
| C-03 | PASS | Phase 1 SCOPE LOCK: "SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling -- teams apply model risk rules to every component that touches AI." + Phase 2 SR 11-7 MISAPPLICATION WARNING section | 12 |
| C-04 | PASS | Phase 2 GIT-NATIVE ADVANTAGE section: "List each, linked to a named framework or requirement." | 12 |
| C-05 | PASS | FINDINGS REGISTER: "IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: "Minimum 5 rows. At least one SATISFIED. At least one ACTION." | 10 |
| C-07 | PASS | Phase 1 VERDICT COMMIT required verbatim in Phase 2 ## VERDICT section (position 2, after DEFAULT RISK) | 10 |
| C-08 | PASS | FRAMEWORK CATALOG: "Conditional frameworks require explicit trigger condition." Phase 1 demands per-framework UNIVERSAL/CONDITIONAL commitment. | 10 |
| C-09 | PASS | ## REFRAME section (position 3, immediately following VERDICT) | 5 |
| C-10 | PASS | ## DATA-SENSITIVITY TIER: "Tiering model (e.g., GREEN / YELLOW / RED) or policy gap. Name a specific control or remediation." | 5 |
| C-11 | PASS** | Pass condition met by letter: VERDICT (position 2) before FRAMEWORK CATALOG (position 6); REFRAME (position 3) immediately following verdict. Spirit violated: DEFAULT RISK at position 1 means VERDICT is not "in the first substantive section." See design note below. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings | 3 |
| C-13 | PASS | Phase 1 SCOPE LOCK has full misapplication explanation; Phase 2 SR 11-7 MISAPPLICATION WARNING requires: "name SR 11-7, explain why it is commonly misapplied, state why Signal falls outside scope, pre-empt the objection." | 3 |

**C-11 design note**: V-05 confirms the design bet is resolved -- the synthesis gate is sufficient to prevent the risk narrative from *crowding out* the verdict (R1 V-05 failed C-11 entirely). But the DEFAULT RISK section preceding VERDICT means the verdict is never in the FIRST position. The synthesis gate fixes the verdict-omission failure mode; it does not fix the verdict-displacement failure mode. The rubric's current pass condition catches omission but not displacement. This is a rubric gap: a candidate v3 fix would add "Adoption verdict must appear in the first named output section."

**Verdict**: 109 by letter. R1's inertia-frame problem was not that the frame is incompatible with verdict-first -- it's that the frame displaces rather than eliminates the verdict. The synthesis gate rescues C-13 and C-07. If structural primacy matters for the compliance officer's reading experience, V-05 is the weakest of the four 109s.

---

## Excellence Signals

**1. Explicit C-13 encoding eliminates R1 variance -- planting the instruction is the mechanism, not model discovery**
R1 produced C-13 emergently in only 1 of 5 variations (V-03 Verdict-first). R2 planted explicit SR 11-7 misapplication text in all 5 variations (CORE RULES / STEP instructions / Phase 1 scratchpad), and all 5 passed C-13. The mechanism is presence vs. absence of the directive, not instruction style. The SR 11-7 misapplication framing is too specific to derive from "vendor vs. methodology" framing alone.

**2. Section-contract template is the portable C-11/C-12 mechanism across all phrasing registers**
V-01 (section-contract), V-03 (terse), V-04 (role sequence), and V-05 (risk frame) all used named section headings in the same fixed order (VERDICT -> REFRAME before FRAMEWORK CATALOG). V-02 (synthesis-gate) used an unlabeled first-line verdict followed by named sections. All 5 passed C-11 and C-12. Named section headings in specified order are both necessary and sufficient for C-11/C-12 regardless of surrounding framing style.

**3. DEFAULT RISK before VERDICT in V-05 exposes a C-11 spirit/letter gap**
The current pass condition catches verdict omission but not verdict displacement. VERDICT at position 2 satisfies "before any framework table" but not "in the first substantive section." Candidate v3 tightening: require verdict as the first named section heading in the output.

---

## Round 2 Summary

- **Floor**: 109 (all variations)
- **Ceiling**: 109 (all variations)
- **R1 -> R2 lift**: V-01: 87->109 (+22), V-02: 96->109 (+13), V-03: 109->109 (0), V-04: 106->109 (+3), V-05: 95->109 (+14)
- **Lift source**: Explicit C-13 encoding (+3 per variation) + named sections for C-09/C-10 where missing (+5-9 per variation)
- **Design bets resolved**:
  - Bet 1 (all 5 encode C-13): CONFIRMED -- all 5 PASS C-13
  - Bet 2 (C-11/C-12 are section-ordering problems): CONFIRMED -- named sections in fixed order sufficient in all registers
  - Bet 3 (V-03 terse is the pivot test): CONFIRMED -- terse instructions + section contract reaches 109; instruction length is not the variable
  - Bet 4 (V-05 synthesis gate rescues default-risk): PARTIALLY CONFIRMED -- synthesis gate rescues C-13/C-07; produces second-position verdict (spirit gap), not first-position verdict
- **Rubric candidate for v3**: Tighten C-11 to require verdict as the first named output section heading

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["explicit C-13 instruction in all variations eliminates R1 emergent variance -- planting SR 11-7 misapplication text is the reliable mechanism; general vendor-vs-methodology framing is insufficient to elicit the specific misapplication warning", "section-contract template (named headings in fixed order) is portable across all phrasing registers -- terse, formal, lifecycle-gated, and risk-framed variations all hit C-11/C-12 with the same template; instruction style is not the variable", "DEFAULT RISK before VERDICT in V-05 exposes C-11 rubric gap: pass condition catches verdict omission but not verdict displacement -- verdict at position 2 passes the letter, violates the spirit; candidate v3 fix: require verdict as the first named section heading"]}
```
