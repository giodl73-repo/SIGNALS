## scout-compliance R3 Scorecard

**All 5 variations: 112/112** — R3 design bets all confirmed.

---

### Scores

| Rank | Variation | Score | C-14 mechanism |
|------|-----------|-------|----------------|
| 1 (tie) | V-01: C-14-safe inertia | 112 | Prose demotion + local annotation |
| 1 (tie) | V-02: Forward declaration | 112 | One-sentence pre-commit + annotation |
| 1 (tie) | V-03: Verdict annotation | 112 | Inline annotation at point of use |
| 1 (tie) | V-04: Combo declaration + inertia | 112 | Triple-encoding (highest robustness) |
| 1 (tie) | V-05: Terse + annotation | 112 | Annotation at point of use, min density |

---

### Design bets resolved

| Bet | Result |
|-----|--------|
| Inertia frame rehabilitated by prose demotion (V-01) | CONFIRMED — `(no ## heading)` instruction suppresses autonomous heading addition |
| One-sentence pre-commitment replaces synthesis gate (V-02) | CONFIRMED — synthesis gate was over-engineered for this specific guarantee |
| Annotation at point of use reduces displacement variance (V-03/V-05) | CONFIRMED — locally readable, future-edit safe |
| Double-encoding under adversarial register (V-04) | CONFIRMED — highest robustness at cost of longest prompt |

---

### R2 → R3 lift: +3 pts across all variations (C-14 PASS)

### New patterns (3)

1. **Prose preamble demotion** rescues the inertia frame — demoting motivational context from `##` to headingless prose is the minimum required change; register is fully preserved.
2. **One-sentence pre-commitment** is the minimum viable C-14 mechanism — a single declaration before output starts is sufficient; full synthesis gate not required.
3. **Annotation at point of use** is the superior mechanism for maintained prompts — local property, future-edit safe, zero reliance on global ordering rules that are silent when sections are inserted above the target.

### Golden prompt candidates

- **V-03** — most inspectable (rubric annotations throughout)
- **V-05** — minimum viable density (~25-30 lines); production default

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["prose preamble demotion (no ## heading) rescues the inertia frame for C-14 -- structural register change is sufficient, no mechanism overhead; motivational context survives as headingless prose preceding ## VERDICT", "forward pre-commitment declaration (one sentence, not full synthesis gate) is sufficient for C-14 guarantee when section ordering already specified -- synthesis gate over-engineered for verdict primacy specifically", "annotation at point of use ([WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT.]) is the superior C-14 mechanism for maintained prompts -- local property, future-edit safe, zero reliance on global ordering scan; global ordering rules are silent when sections are inserted above the target"]}
```
�� SCOPE BOUNDARY(4) → FRAMEWORK CATALOG(5). Verdict unconditionally precedes all framework analysis tables. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both present as named `##`-level section headings in the output template. | 3 |
| C-13 | PASS | AMEND section: "3 specific adjustments. Each: what the user changes + what changes in the output." Explicit count and structure. | 3 |
| C-14 | PASS | Prose preamble instruction explicitly "(no ## heading)" — structural demotion prevents displacement. Annotation at VERDICT: "[This is the first ## heading in this output. No ## heading precedes it.]" Mechanism: structural demotion + local annotation. Risk: model could autonomously add `## DEFAULT RISK` despite instruction; explicit "(no ## heading)" suppresses this. | 3 |

**Verdict**: 112. The inertia frame is fully rehabilitated by a single structural demotion: risk motivation becomes headingless prose, making `## VERDICT` unconditionally first. The annotation at VERDICT is a second guard. C-14-safe inertia is viable — the motivational register (compliance-risk-of-skipping-review) is preserved without displacement. Highest-stakes bet in R3: CONFIRMED.

---

### V-02: Forward verdict declaration (112/112)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | SETUP: "Infer domain, data handling, and applicable frameworks from signals alone. Do not prompt. Identify >= 4 frameworks." | 12 |
| C-02 | PASS | Pre-write declaration: "The data processor is [component sending data to external API]. Signal is a methodology." ANCHORS reinforce. SCOPE BOUNDARY section: "Data processor: Claude Code / Anthropic. Not under review: Signal (methodology, not vendor, not data processor)." | 12 |
| C-03 | PASS | ANCHORS: "SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams extend model risk obligations to every AI-adjacent component. A prompt methodology that invokes a model is not itself a model. State this in output. Pre-empt the compliance officer's objection." SR 11-7 MISAPPLICATION WARNING section required. | 12 |
| C-04 | PASS | ANCHORS: "Git-native no-server: compliance-favorable. Name >= 1 property with framework linkage." GIT-NATIVE ADVANTAGE section with framework linkage. | 12 |
| C-05 | PASS | FINDINGS REGISTER: "SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: ">= 5 rows. >= 1 SATISFIED. >= 1 ACTION." | 10 |
| C-07 | PASS | VERDICT: "Form: 'Adoption-ready for [X] where [Y]; [action] required before [Z].' No hedging. This is the first ## heading you produce." | 10 |
| C-08 | PASS | ANCHORS: "PCI DSS, GDPR, CCPA: conditional. Named trigger required for each. No universal assertion." FRAMEWORK CATALOG requires conditional trigger for all conditional entries. | 10 |
| C-09 | PASS | REFRAME: "One quotable sentence. Methodology approval vs. vendor approval. Suitable for a compliance officer's internal approval conversation." | 5 |
| C-10 | PASS | DATA-SENSITIVITY TIER: "Specific control or remediation -- not just the flag." Tiering model or policy gap required. | 5 |
| C-11 | PASS | Template section order: VERDICT(1) → REFRAME(2) → SR 11-7 WARNING(3) → SCOPE BOUNDARY(4) → FRAMEWORK CATALOG(5). Verdict before all framework analysis. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both present as named section headings in template. | 3 |
| C-13 | PASS | AMEND: "3 adjustments. Each: user change + output impact." | 3 |
| C-14 | PASS | Pre-write declaration: "## VERDICT is the first ## heading I will produce. No ## heading precedes it." committed before output begins. Template annotation: "This is the first ## heading you produce." Declaration is prose (not a heading in output). "These declarations are your scope commitment. They are not part of the output." Double-layer: commitment + template annotation. | 3 |

**Verdict**: 112. The forward declaration is a lighter mechanism than R2 V-02's full two-phase synthesis gate — one sentence pre-commitment plus template annotation achieves C-14 parity. The synthesis gate was over-engineered for this specific guarantee. Minimum viable pre-commitment mechanism for C-14 is a single scope-declaration sentence.

---

### V-03: Verdict-annotated template (112/112)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | SETUP: "Infer domain, data scope, and applicable frameworks from repo context. Do not prompt. Identify >= 4 frameworks." FRAMEWORK CATALOG annotated "[C-01: >= 4 frameworks inferred from repo signals]". | 12 |
| C-02 | PASS | INVARIANT 1: "Signal is a methodology -- not a vendor, not a data processor. The compliance surface is Claude Code (the tool sending repo content to the Anthropic API)." SCOPE BOUNDARY annotated "[identifies data processor; excludes Signal from vendor scope]". | 12 |
| C-03 | PASS | INVARIANT 2: "SR 11-7 applies to Claude the AI model, not to Signal the prompt methodology. SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams extend model risk obligations to every component that touches AI, including non-model layers. A structured prompt methodology is not a model. State this and pre-empt the compliance officer's objection." SR 11-7 MISAPPLICATION WARNING annotated "[C-13: named framework, misapplication mechanism, Signal-specific correction, objection pre-empted]". | 12 |
| C-04 | PASS | INVARIANT 4: "Git-native no-server design is compliance-favorable. Name >= 1 specific property with framework linkage." GIT-NATIVE ADVANTAGE annotated "[C-04: >= 1 compliance property of no-server design; named framework linkage]". | 12 |
| C-05 | PASS | FINDINGS REGISTER annotated "[C-05: >= 4 entries with IDs and severity labels]". Format explicit. | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX annotated "[C-06: >= 5 rows; >= 1 SATISFIED by design; >= 1 ACTION]". | 10 |
| C-07 | PASS | VERDICT: "One sentence. Audience named. Condition named. Form: 'Adoption-ready for [X] where [Y]; [action] required before [Z].' Do not hedge." | 10 |
| C-08 | PASS | INVARIANT 3: "PCI DSS, GDPR, CCPA are conditional frameworks. Each requires an explicit named trigger. Do not assert universal applicability." FRAMEWORK CATALOG annotation reinforces conditional trigger requirement. | 10 |
| C-09 | PASS | REFRAME: "[quotable statement for compliance officer internal conversations] One sentence. Methodology approval vs. vendor approval." | 5 |
| C-10 | PASS | DATA-SENSITIVITY TIER: "[C-10: NPI risk identified; tiering model or policy gap; specific control or remediation]...Named control or remediation." | 5 |
| C-11 | PASS | Template order: VERDICT(1) → REFRAME(2) → SR 11-7(3) → SCOPE BOUNDARY(4) → FRAMEWORK CATALOG(5). Verdict unconditionally before framework catalog. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings in template. | 3 |
| C-13 | PASS | AMEND: "[3 specific adjustments with output impact] Each: user change + what changes in the output." | 3 |
| C-14 | PASS | Inline annotation at VERDICT: "[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]" Local, unambiguous, at exact point of failure. No section precedes VERDICT in template — annotation makes C-14 a locally-readable property. Most maintainable mechanism: future template edits cannot drop VERDICT from first position without touching the annotation. | 3 |

**Verdict**: 112. Annotation at the point of use is the strongest C-14 mechanism for long-term maintainability. Rubric annotations throughout the template make each criterion locally traceable — inspection without cross-referencing. Golden prompt candidate: highest maintainability, no global ordering reliance.

---

### V-04: Combo forward declaration + C-14-safe inertia framing (112/112)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | SETUP: "Infer domain, data handling scope, and frameworks from signals alone. Do not prompt. Identify >= 4 frameworks." | 12 |
| C-02 | PASS | Pre-write scope commitment: identifies data processor as "component that sends repo content to an external API." ANCHORS: "Claude Code / Anthropic: data processor. Signal: methodology, not vendor." SCOPE BOUNDARY section. | 12 |
| C-03 | PASS | Pre-write SR 11-7 commitment: "SR 11-7 is model risk management. It applies to Claude the AI model, not to Signal the prompt methodology. SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling -- teams extend model risk obligations to every AI-touching component. A prompt methodology is not a model. This distinction appears as a named section in output." SR 11-7 MISAPPLICATION WARNING section required. | 12 |
| C-04 | PASS | ANCHORS: "Git-native no-server: compliance-favorable. Name >= 1 property with framework linkage." GIT-NATIVE ADVANTAGE section required. | 12 |
| C-05 | PASS | FINDINGS REGISTER: "SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: ">= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION." | 10 |
| C-07 | PASS | VERDICT: "One sentence. Adoption condition. Audience named. Form: 'Adoption-ready for [X] where [Y]; [action] required before [Z].' Actionable. No hedging." | 10 |
| C-08 | PASS | ANCHORS: "PCI DSS, GDPR, CCPA: conditional. Named trigger for each. No universal assertion." | 10 |
| C-09 | PASS | REFRAME: "One quotable sentence. Methodology approval vs. vendor approval. Usable verbatim in a compliance officer's internal approval conversation." | 5 |
| C-10 | PASS | DATA-SENSITIVITY TIER: "Named control or remediation." Tiering (GREEN / YELLOW / RED) or policy gap required. | 5 |
| C-11 | PASS | Prose intro (no ##) → VERDICT(first ##) → REFRAME → SR 11-7 → SCOPE BOUNDARY → FRAMEWORK CATALOG. Verdict before all framework tables. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both present as named section headings. | 3 |
| C-13 | PASS | AMEND: "3 adjustments. Each: user change + output impact." | 3 |
| C-14 | PASS | Triple-encoding: (1) pre-write structural commitment — "The risk context appears as introductory prose with no ## heading. No ## section precedes ## VERDICT." (2) template prose block — "[Introductory prose -- no ## heading -- 2-3 sentences...]" (3) VERDICT annotation — "[First ## heading in this document -- per your pre-write commitment.]" Highest robustness under adversarial register. | 3 |

**Verdict**: 112. Most robust C-14 mechanism — three independent guards under the highest-pressure framing register (prose expansion + risk motivation). If any other variation shows variance in adversarial testing, V-04's triple-encoding is the fallback. Trade-off: longest prompt, highest maintenance overhead.

---

### V-05: Terse + annotation (112/112)

| ID | Result | Evidence | Pts |
|----|--------|----------|-----|
| C-01 | PASS | SETUP: "Detect domain from repo. Infer frameworks. Do not ask anything. Identify >= 4 frameworks." Terse but complete. | 12 |
| C-02 | PASS | RULE 1: "Signal is not a vendor. Claude Code / Anthropic is the data processor." SCOPE BOUNDARY section: "Claude Code / Anthropic: data processor. Signal: methodology, not vendor." | 12 |
| C-03 | PASS | RULE 2: "SR 11-7 applies to Claude the model, not to Signal the methodology." RULE 3: "SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling -- explain the mechanism in output (teams extend model risk rules to non-model layers) and pre-empt the compliance officer's objection." SR 11-7 MISAPPLICATION WARNING section: "Name SR 11-7. Mechanism of misapplication. Why Signal is outside scope. Objection pre-empted." Full C-13 chain maintained at terse density. | 12 |
| C-04 | PASS | RULE 5: "Git-native no-server design is compliance-favorable -- name >= 1 benefit with framework link." GIT-NATIVE ADVANTAGE section: "List. Each item: property + named framework. >= 1 item." | 12 |
| C-05 | PASS | FINDINGS REGISTER: "SF-01... | HIGH / MEDIUM / LOW | >= 4 entries." | 12 |
| C-06 | PASS | REQUIREMENTS MATRIX: ">= 5 rows. >= 1 SATISFIED. >= 1 ACTION." | 10 |
| C-07 | PASS | VERDICT: "Form: 'Adoption-ready for [X] where [Y]; [Z] before [W].' No hedging." | 10 |
| C-08 | PASS | RULE 4: "PCI DSS, GDPR, CCPA are conditional -- mark each with its trigger, do not assert universal." FRAMEWORK CATALOG requires triggers. | 10 |
| C-09 | PASS | REFRAME: "One sentence. Methodology vs. vendor. Quotable." Terse but all three requirements present. | 5 |
| C-10 | PASS | DATA-SENSITIVITY TIER: "NPI risk. Tiering (GREEN / YELLOW / RED) or policy gap. Specific control or remediation." Terse but complete. | 5 |
| C-11 | PASS | Template order: VERDICT(1) → REFRAME(2) → SR 11-7 WARNING(3) → SCOPE BOUNDARY(4) → FRAMEWORK CATALOG(5). Verdict before all framework analysis. | 3 |
| C-12 | PASS | ## REFRAME and ## DATA-SENSITIVITY TIER both named section headings in ordered template. | 3 |
| C-13 | PASS | AMEND: "3 items. Each: change + output impact." | 3 |
| C-14 | PASS | Annotation at VERDICT: "[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]" No prose preamble in template — VERDICT is unconditionally first. Annotation adds local redundancy to the section ordering. | 3 |

**Verdict**: 112 at minimum instruction density (~25-30 lines). R2 V-03 (terse baseline) likely also reaches 112 under the v3 rubric because `## VERDICT` was already its first heading; V-05 confirms annotation adds local robustness without changing correctness floor. The minimum viable prompt for scout-compliance is V-05 plus the C-14 annotation. Golden prompt candidate alongside V-03.

---

### Design bets resolved

| Bet | Prediction | Result |
|-----|-----------|--------|
| V-01 inertia frame rehabilitated by prose demotion | C-14 PASS | CONFIRMED |
| V-02 forward declaration lighter than synthesis gate | C-14 PASS | CONFIRMED — one sentence sufficient |
| V-03 annotation at point of use reduces variance | C-14 PASS, locally readable | CONFIRMED |
| V-04 double-encoding under adversarial register | C-14 PASS, highest robustness | CONFIRMED |
| V-05 terse + annotation reaches 112 | C-14 PASS, minimum viable density | CONFIRMED |

### Excellence signals

1. **Prose preamble demotion rescues the inertia frame** — demoting motivational context from a `##` section to headingless prose is the minimum required structural change. The inertia register (compliance-risk-without-review) is fully preserved in prose form. No mechanism overhead beyond the demotion itself.

2. **One-sentence pre-commitment is sufficient for C-14** — R2 V-02's full synthesis gate was over-engineered for verdict primacy. A single declaration ("## VERDICT is the first ## heading I will produce") committed before output begins achieves the same guarantee. The synthesis gate's value is primarily for scope commitment (SR 11-7, vendor boundary), not for section ordering.

3. **Annotation at point of use is the superior C-14 mechanism for production prompts** — local annotation at `## VERDICT` makes compliance a locally-readable property: future template edits cannot accidentally displace VERDICT without touching the annotation. Global ordering rules (R2 style) are silent when sections are added above. Annotation is the right default for maintained prompts.

### R2 -> R3 lift summary

V-01: 109→112 (+3) | V-02: 109→112 (+3) | V-03: 109→112 (+3) | V-04: 109→112 (+3) | V-05: 109→112 (+3)

All lifts: C-14 PASS (structural demotion / pre-commitment / annotation at point of use).

### R3 golden prompt candidates

| Candidate | Why |
|-----------|-----|
| **V-03** | Annotation at point of use; rubric annotations make each criterion locally traceable; most inspectable |
| **V-05** | Minimum viable density (~25-30 lines); annotation adds local C-14 guard without overhead; best for concise production deployment |

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["prose preamble demotion (no ## heading) rescues the inertia frame for C-14 -- structural register change is sufficient, no mechanism overhead; motivational context survives as headingless prose preceding ## VERDICT", "forward pre-commitment declaration (one sentence, not full synthesis gate) is sufficient for C-14 guarantee when section ordering already specified -- synthesis gate over-engineered for verdict primacy specifically", "annotation at point of use ([WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT.]) is the superior C-14 mechanism for maintained prompts -- local property, future-edit safe, zero reliance on global ordering scan; global ordering rules are silent when sections are inserted above the target"]}
```
