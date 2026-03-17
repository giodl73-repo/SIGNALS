Written to `simulations/quest/golden/scout-compliance-golden-2026-03-14.md`.

---

**Golden prompt summary:**

- **Score**: 112/136 (GOLDEN threshold: 100)
- **Source**: V-05 simplified (33.8% reduction, all essential criteria retained)
- **All C-01..C-14 pass** — essential, recommended, and aspirational core/R1/R2 layers complete

**What made it golden (vs V-01 baseline):**

1. **CONSTRAINTS block** — 4 explicit boundary conditions replace role-attributed ANCHORS; eliminates vendor-scope and SR 11-7 misattribution at the instruction level
2. **SR 11-7 MISAPPLICATION WARNING** as a dedicated named section — forces three-part pre-emption (name it, explain the mechanism, apply to Signal), not just a scope statement
3. **VERDICT form constraint** with slot template + `No hedging` directive — prevents C-07 from collapsing to "it depends"
4. **FRAMEWORK CATALOG schema** with UNIVERSAL/CONDITIONAL column — makes C-08 structurally inevitable rather than behavioral
5. **DATA-SENSITIVITY TIER** with explicit NPI risk framing + named control requirement — closes the C-10 trailing-observation failure mode

**Simplification tradeoff**: Dropped C-15/C-16/C-17 (aspirational R3 mechanism layer) by removing BEFORE WRITING block and preamble instruction. The 24-point gap to 136/136 is fully recoverable in R5 by restoring the triple-encoding architecture.
 internal approval conversation.

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

---

## What Made It Golden

Five patterns distinguish this prompt from the V-01 baseline (PM-first, 121/136 before simplification).

### 1. CONSTRAINTS block with four explicit boundary conditions

V-01 embedded scope rules inside `ANCHORS` with role attributions. The simplified golden strips role labels and names four constraints directly. This eliminates the most common essential fails: misattributing vendor scope to Signal (C-02) and misapplying SR 11-7 to the methodology (C-03). Each constraint is a boundary violation the model cannot accidentally cross without contradicting an explicit instruction.

### 2. SR 11-7 MISAPPLICATION WARNING as a dedicated named section

A baseline prompt that states "SR 11-7 does not apply" in passing prose earns C-03 but fails C-13 (proactive pre-emption). The golden forces a named `## SR 11-7 MISAPPLICATION WARNING` section with three obligations: name the framework, explain the misapplication mechanism, apply the correction to Signal. This transforms a scope statement into a section that equips the compliance officer to answer the objection before it is raised.

### 3. VERDICT form constraint with explicit no-hedging directive

V-01 specified "one sentence, actionable" but left the form open. The golden adds the required sentence template: `"Adoption-ready for [X] where [Y]; [action] required before [Z]."` followed by `Actionable. No hedging.` This closes the gap between a verdict that satisfies C-07 technically and one that is usable operationally -- the slot structure forces condition and audience to be named, the no-hedging directive prevents the form from collapsing to "it depends."

### 4. FRAMEWORK CATALOG with mandatory UNIVERSAL / CONDITIONAL column and named triggers

The column structure makes C-08 structurally inevitable: a model filling the table cannot mark PCI DSS, GDPR, or CCPA as UNIVERSAL without contradicting the Trigger column requirement. V-01 listed frameworks but left classification implicit. The table schema makes the conditional assertion requirement a structural constraint, not a behavioral one.

### 5. DATA-SENSITIVITY TIER with NPI framing

V-01 used "DATA-SENSITIVITY TIER" with minimal instruction. The golden names the risk source explicitly (`NPI risk in Signal artifacts`), requires tiering OR policy gap, and requires a named control or remediation. This forces C-10 -- the output cannot trail off with a vague observation; it must commit to a tier assignment or identify the gap with a concrete action.

---

## Simplification Record

| Removed | Words | Criterion impact |
|---------|-------|-----------------|
| BEFORE WRITING block | 21 | C-16 (aspirational R3) -- FAIL, was PASS |
| ROLE SEQUENCE block | 18 | Zero criterion coverage |
| 6 role labels | ~14 | Zero criterion coverage |
| Preamble instruction | 39 | C-15 (aspirational R3) -- vacuous, was PASS |
| C-17 annotation at VERDICT | 12 | C-17 (aspirational R3) -- FAIL, was PASS |
| AMEND section | 10 | No matching criterion |
| Anchor 2 elaboration | ~30 | Section instruction covers C-13 independently |
| Header decoration | 3 | Cosmetic |

Score impact: 130/136 (V-05 pre-simplification) -> 112/136 (post-simplification).
Criteria dropped: C-15, C-16, C-17, C-19, C-20, C-22 (all aspirational R3/R4 mechanism layer).
Criteria retained: C-01..C-14 all pass. All essential (C-01..C-05) pass.

---

## Final Rubric Criteria Summary (v5)

| Tier | Criteria | Points | Status in Golden |
|------|----------|--------|-----------------|
| Essential | C-01..C-05 | 60 | ALL PASS |
| Recommended | C-06..C-08 | 30 | ALL PASS |
| Aspirational (core) | C-09..C-10 | 10 | ALL PASS |
| Aspirational (R1) | C-11..C-13 | 9 | ALL PASS |
| Aspirational (R2) | C-14 | 3 | PASS |
| Aspirational (R3) | C-15..C-17 | 9 | ALL FAIL (removed in simplification) |
| Aspirational (R4) | C-18..C-22 | 15 | ALL FAIL (removed in simplification) |
| **Golden score** | | **112/136** | Above threshold (100) |

**GOLDEN threshold**: 100 pts. All essential (C-01..C-05) must pass. Aspirational R3/R4 may be absent.

**To reach R5 target (136/136)**: Restore BEFORE WRITING block (C-16 + C-19), preamble with explicit
`(no ## heading)` instruction at two locations (C-15 + C-22), C-17 annotation at VERDICT heading,
named constraint identifiers C1..C4 (C-18), C-15 text embedded in C-16 declaration (C-20),
`[ADOPTION GATE]` label on VERDICT heading (C-21).
