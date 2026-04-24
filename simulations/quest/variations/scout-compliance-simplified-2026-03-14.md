---

## QU5 Result

**493 words → 326 words — 33.8% reduction. All essential criteria maintained.**

### Simplified prompt (complete)

```
You are running /scout-compliance.

SETUP: Read README, CLAUDE.md, plugin-plan.md, package files.
Infer regulatory domain and applicable frameworks from repo signals alone.
Do not prompt. Identify >= 4 frameworks.

CONSTRAINTS:
1. Signal is a methodology -- not a vendor, not a data processor. Compliance surface:
   Claude Code (the tool transmitting repo content to the Anthropic API).
2. SR 11-7 applies to Claude the AI model, not to Signal. State this in output.
3. PCI DSS, GDPR, CCPA: conditional. Named trigger required for each. No universal assertion.
4. Git-native no-server design: compliance-favorable. Name >= 1 property with framework linkage.

OUTPUT:

## VERDICT
One sentence. Adoption condition named. Audience named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Actionable. No hedging.

## REFRAME
One quotable sentence. Methodology approval vs. vendor approval.
Suitable for a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. Explain the misapplication mechanism (model risk extended to
non-model components). Apply the correction to Signal. Pre-empt the objection.

## SCOPE BOUNDARY
Data processor: Claude Code / Anthropic.
Not under review: Signal (methodology, not vendor, not data processor).

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional trigger required for all conditional entries.

## GIT-NATIVE ADVANTAGE
List. Each: compliance property + named framework linkage. >= 1 item.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
NPI risk in Signal artifacts. Tiering (GREEN / YELLOW / RED) or policy gap.
Named control or remediation.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

### What was removed and why

| Removed | Words | Criterion impact |
|---------|-------|-----------------|
| BEFORE WRITING block | 21 | C-16 (aspirational R3) — FAIL, was PASS |
| ROLE SEQUENCE block | 18 | Zero criterion coverage |
| 6 role labels | ~14 | Zero criterion coverage |
| Preamble instruction | 39 | C-15 (aspirational R3) — vacuous, was PASS |
| C-17 annotation at VERDICT | 12 | C-17 (aspirational R3) — FAIL, was PASS |
| AMEND section | 10 | No matching criterion |
| Anchor 2 elaboration | ~30 | Section instruction covers C-13 independently |
| Header decoration | 3 | Cosmetic |

Score: **112/136** (down from 121, still well above GOLDEN threshold of 100). All C-01..C-10 pass.

The 9-point loss is entirely from C-15/C-16/C-17 (mechanism robustness battery). These are all aspirational R3 — they make the prompt more robust to model drift, but are not required to produce a correct GOLDEN output.

```json
{"simplified_word_count": 326, "original_word_count": 493, "all_essential_still_pass": true}
```
/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## Criteria coverage

| ID | Criterion | Covered by |
|----|-----------|------------|
| C-01 | Framework inference, no prompting, >= 4 | SETUP: signals-only + do not prompt + >= 4 |
| C-02 | Signal vs. Claude Code scope | Constraint 1 + SCOPE BOUNDARY section |
| C-03 | SR 11-7 scope | Constraint 2 + SR 11-7 section |
| C-04 | Git-native compliance-favorable | Constraint 4 + GIT-NATIVE ADVANTAGE |
| C-05 | Findings register >= 4 | FINDINGS REGISTER: IDs, severity, >= 4 |
| C-06 | Requirements matrix >= 5 rows | REQUIREMENTS MATRIX: >= 5 + SATISFIED + ACTION |
| C-07 | Adoption-readiness verdict | VERDICT form instruction |
| C-08 | Conditional frameworks with triggers | Constraint 3 + FRAMEWORK CATALOG trigger column |
| C-09 | Quotable reframe | REFRAME: quotable, methodology vs. vendor |
| C-10 | NPI tiering or policy gap | DATA-SENSITIVITY TIER section |
| C-11 | Verdict-first structure | VERDICT is first section in template |
| C-12 | Named sections for C-09/C-10 | REFRAME + DATA-SENSITIVITY TIER both named |
| C-13 | SR 11-7 proactively flagged | Section instruction: "explain mechanism... pre-empt" |
| C-14 | Verdict is first ## heading | No ## heading precedes VERDICT in template |

```json
{"simplified_word_count": 326, "original_word_count": 493, "all_essential_still_pass": true}
```
