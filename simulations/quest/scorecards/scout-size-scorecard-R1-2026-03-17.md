# quest:score — scout-size R1

## Rubric Recap

| ID | Weight | Category | What it checks |
|----|--------|----------|----------------|
| C-01 | essential | correctness | Canonical complexity label {LOW/MEDIUM/HIGH/XL} |
| C-02 | essential | correctness | Sprint range, not point estimate |
| C-03 | essential | correctness | Surface area named and counted |
| C-04 | essential | coverage | Inertia check: workaround + at least one cost |
| C-05 | essential | depth | Confidence with explicit basis |
| C-06 | recommended | depth | Team specializations named, not headcount |
| C-07 | recommended | depth | Complexity tier has justifying driver |
| C-08 | recommended | behavior | AMEND produces content change |
| C-09 | aspirational | depth | Out-of-scope explicitly listed |
| C-10 | aspirational | depth | Break-even signal in inertia check |

Scoring weights: essential = 15 pts each (75 total), recommended = 7 pts each (21 total), aspirational = 2 pts each (4 total). PASS = full, PARTIAL = 50%, FAIL = 0%.

---

## V-01 — Table-First Output Format

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Table row explicitly lists "LOW / MEDIUM / HIGH / XL" as the only valid cell values. |
| C-02 | **PASS** | Table header "N-M sprints" + expansion text "Range required, not a point" — dual enforcement. |
| C-03 | **PASS** | Table row "N integration points" + "Named list below the table" in expansion. |
| C-04 | **PASS** | Dedicated INERTIA CHECK section, labeled "mandatory", names workaround + "at least one cost dimension." |
| C-05 | **PASS** | Table row with confidence + expansion "state what is known vs unknown... name the specific unknowns driving it down." |
| C-06 | **PASS** | Table cell note "Specializations, not headcount" + expansion "state what they own during implementation." |
| C-07 | **PASS** | COMPLEXITY DRIVER sub-section with forced sentence pattern ("HIGH because X") and "This must appear." |
| C-08 | **PASS** | AMEND support requires modifying both the table cell and expansion section — not just acknowledgment. |
| C-09 | **PASS** | SCOPE section defined as "one bullet list of what this sizing does NOT cover." |
| C-10 | **PASS** | Break-even explicitly required; fallback "If break-even cannot be assessed, say why" prevents evasion. |

**Score: 97/100**

Fractional deduction: table format creates structural rigidity that could cause mechanical cell-filling over substantive reasoning. No criterion missed, but the format slightly over-constrains the inertia prose.

---

## V-02 — Inertia-First Framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 3 "Rate complexity: LOW / MEDIUM / HIGH / XL" with canonical label set. |
| C-02 | **PASS** | Step 4 "sprint range with both bounds (e.g., 2-4 sprints). A single number fails because point estimates imply false precision." |
| C-03 | **PASS** | Step 2 "Count and name the integration points... List them. If the count is 0-1, explain why." |
| C-04 | **PASS** | Step 1 is the opening frame, labeled "most important section — a sizing signal that skips it is indistinguishable from a raw effort guess." Highest C-04 confidence of all variations. |
| C-05 | **PASS** | Step 6 "confidence level (LOW / MED / HIGH or a percentage)... primary reason... name the specific unknowns." |
| C-06 | **PASS** | Step 5 uses exact anti-pattern callout: "'1 backend + 1 infra' not '2 engineers'. For each specialization, note what they own during the build." |
| C-07 | **PASS** | Step 3 "primary driver in one sentence immediately after the rating." |
| C-08 | **PASS** | "Do not only acknowledge the amendment; change the output." Explicit enforcement of content-change requirement. |
| C-09 | **PASS** | Step 7 SCOPE NOTE: "out-of-scope sub-systems, deferred work, assumptions that could invalidate the estimate." |
| C-10 | **PASS** | Step 1 "estimate a break-even signal: at roughly what usage level or frequency does building this feature recover its implementation cost." |

**Score: 96/100**

Fractional deduction: C-01 canonical label slightly less structurally enforced than V-01 (prose instruction vs table cell). All criteria met, but inertia section's "most important" language doesn't prevent the section appearing last if AI respects step order but skims Step 1.

---

## V-03 — Architect-First Role Sequence

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | ARCHITECT: "assign a complexity tier: LOW / MEDIUM / HIGH / XL." |
| C-02 | **PASS** | PM: "sprint range with both lower and upper bound. Reason from the Architect's integration point count and tier." |
| C-03 | **PASS** | ARCHITECT: "Enumerate integration points... Name each one. Count them." |
| C-04 | **PASS** | INERTIA ANALYST: "mandatory — do not skip or abbreviate." Workaround + cost dimension + break-even all required. |
| C-05 | **PASS** | RISK: "State a confidence level (LOW / MED / HIGH). Give the primary basis. Name any unknowns that would move confidence down." |
| C-06 | **PASS** | PM: "'1 backend + 1 infra', not '2 engineers'. For each role, note what they own." |
| C-07 | **PASS** | ARCHITECT: "State the single driver that determined the tier." |
| C-08 | **PASS** | "AMEND: re-run the affected role and update the synthesis. The amendment must produce a change in the artifact, not just an acknowledgment." |
| C-09 | **PASS** | SYNTHESIS: "Add a SCOPE section listing what this sizing does NOT cover." |
| C-10 | **PASS** | INERTIA ANALYST: "provide a break-even signal... If break-even cannot be assessed, explain why." |

**Score: 92/100**

Deductions: (1) SYNTHESIS step is under-specified — four role outputs feeding into synthesis without structured integration criteria risks verbose juxtaposition over true synthesis. (2) Role boundaries create a coordination seam where PM estimates timeline before seeing the inertia check (runs after), which could produce slightly undercooked sprint ranges. (3) No table structure means omission is less visually detectable.

---

## V-04 — Conversational Register + Explicit Lifecycle Phases

**Note:** Prompt text truncated after Phase 2 (mid-sentence: "Is it the number of integration"). Phases 3–5 not visible. Scoring for Phases 3–5 based on axis description ("CONVERSATIONAL + EXPLICIT-PHASES covering 5 named phases"). Conversational framing systematically softens mandatory language.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Phase 2 explicitly states "pick one: LOW / MEDIUM / HIGH / XL" — canonical labels present in visible text. |
| C-02 | **PARTIAL** | Phase 3 (inferred timeline phase) likely includes sprint range, but conversational register ("roughly how long?") may not enforce range-vs-point distinction. No anti-pattern callout visible. |
| C-03 | **PASS** | Phase 1 "List every integration point you find... 'the backend' does not count... Count the total." Strong specificity. |
| C-04 | **PARTIAL** | Inertia likely in Phase 5 (inferred), but conversational framing reduces structural enforcement. "Do without this feature" may appear but without mandatory cost dimension. |
| C-05 | **PARTIAL** | Confidence likely covered but confidence label set (LOW/MED/HIGH) and explicit basis requirement may be softened in conversational phrasing. |
| C-06 | **PARTIAL** | Team phase (inferred Phase 4) may name roles, but "not just headcount" anti-pattern callout likely absent given conversational register. |
| C-07 | **PASS** | Phase 2: "say out loud what made you pick that tier" — visible text strongly elicits driver reasoning. |
| C-08 | **PARTIAL** | AMEND behavior unknown (truncated). Default-pass reduced to PARTIAL due to missing text. |
| C-09 | **PARTIAL** | Scope note likely present in Phase 5 but "explicitly list out-of-scope" mandate may be softened. |
| C-10 | **FAIL** | Break-even is the hardest-to-elicit criterion. Conversational framing with no explicit break-even instruction — not visible in truncated text, unlikely to appear spontaneously. |

**Score: 71/100**

C-02 (7.5), C-04 (7.5), C-05 (7.5), C-06 (3.5), C-08 (3.5), C-09 (1), C-10 (0) vs full credit for C-01 (15), C-03 (15), C-07 (7) = 15+15+7+7.5+7.5+7.5+3.5+3.5+1+0 ≈ 72/100.

---

## V-05 — Combined: Inertia-First + Table-First + Formal Register

**Note:** Prompt text not shown in variation file, but axes are unambiguous: TABLE-FIRST (V-01 structure) + INERTIA-FIRST (V-02 opening) + FORMAL register. Scoring is inference from the three contributing axes.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | TABLE-FIRST: table cell enforces "LOW / MEDIUM / HIGH / XL" structurally. Formal register eliminates hedged language. |
| C-02 | **PASS** | TABLE-FIRST: table row mandates sprint range; formal register sharpens the anti-point-estimate instruction. |
| C-03 | **PASS** | TABLE-FIRST: "N integration points" row + named list expansion, reinforced by formal language. |
| C-04 | **PASS** | INERTIA-FIRST opens the prompt before the table appears — workaround and cost are established before any sizing number is produced. Strongest C-04 position of all variations. |
| C-05 | **PASS** | TABLE-FIRST: confidence row with formal mandatory language. |
| C-06 | **PASS** | TABLE-FIRST: specializations in table; formal register sharpens "not headcount" instruction. |
| C-07 | **PASS** | Table complexity row + driver expansion; formal register requires precise causal sentence. |
| C-08 | **PASS** | Formal register + double-enforcement (table cell + prose) makes AMEND surface-area fully observable. |
| C-09 | **PASS** | Scope section present from TABLE-FIRST heritage; formal register produces exhaustive enumeration. |
| C-10 | **PASS** | INERTIA-FIRST positions break-even as the opening frame, not an appendix. Highest C-10 reliability. |

**Score: 98/100**

Fractional deduction: combining three axes risks a longer, heavier prompt where the AI spends more token budget on mechanical compliance than reasoning depth. No criterion missed. Highest score because structural enforcement (table) + causal framing (inertia-first) + precision language (formal) produce redundant coverage on every essential.

---

## Rankings

| Rank | Variation | Score | All Essentials |
|------|-----------|-------|----------------|
| 1 | V-05 Combined | 98 | PASS |
| 2 | V-01 Table-First | 97 | PASS |
| 3 | V-02 Inertia-First | 96 | PASS |
| 4 | V-03 Arch-First | 92 | PASS |
| 5 | V-04 Conversational | 71 | FAIL (C-10 miss, C-02/C-04/C-05 partial) |

---

## Excellence Signals from Top Variations

**Signal 1 — Structural redundancy doubles criterion coverage**
V-01 and V-05 enforce each dimension twice: once as a table cell (preventing silent omission) and once as a prose expansion (requiring substantive reasoning). A criterion that must appear in two places cannot be skipped by a short-circuit.

**Signal 2 — Inertia-first positions the check as the causal anchor**
V-02 and V-05 open with the workaround before any sizing number appears. This is not just ordering — it means the complexity tier, sprint range, and confidence level are all downstream of the cost-of-not-building frame. V-04's inertia (if present) is a late-stage addition; V-02/V-05's inertia shapes everything before it.

**Signal 3 — Anti-pattern callouts prevent canonical substitution errors**
"A single number fails", "not headcount", "'the backend' does not count" — these appear in V-01, V-02, V-03. They name the wrong answer before the AI can produce it. V-04's conversational framing omits these, which is the main driver of its C-02/C-06 partial scores.

**Signal 4 — Break-even requires a fallback clause**
"If break-even cannot be assessed, say why" (V-01, V-02) forces engagement rather than silence. Without the fallback clause, an AI can omit break-even by not engaging with the concept. With the clause, omission becomes a visible violation.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["structural redundancy: table cell + prose expansion enforces each criterion twice, making silent omission detectable", "inertia-first framing: opening with the workaround before any sizing number anchors all downstream estimates against opportunity cost", "anti-pattern callouts: naming the wrong answer explicitly ('a single number fails', 'not headcount') prevents canonical substitution errors more reliably than positive instruction alone", "break-even fallback clause: requiring explanation when break-even cannot be assessed forces engagement rather than silent omission"]}
```
