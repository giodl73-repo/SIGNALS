Written to `simulations/quest/variations/discover-compare-variations-R4-2026-03-17.md`.

---

## Round 4 — discover-compare variations

**Three single-axis variations:**

**V-01** — Output format (C-15 target): RULE 4 evidence template upgraded to triple-slot machine-parseable format. Each citation entry is: `[Option × Dimension] = [finding] → [direction]` — finding and direction are separate named fields, not merged prose. All other elements identical to R3 V-04. Isolates whether the field split is the discriminating factor for C-15.

**V-02** — Lifecycle emphasis (C-14 target): COMPETITIVE AXIS PRE-CHECK upgraded from prose bullet slots to a named-column table `| Axis Slot | Option A | Option B |`. Makes "explicit axis slots" unambiguous. RULE 4 template unchanged from R3 V-04. Isolates whether the tabular pre-check closes C-14's first mechanism gap.

**V-03** — Phrasing register (C-14 second mechanism): Inline "invalid — not incomplete, invalid" vocabulary added to each competitive section annotation header: `*(RULE 3 — confirmed axis: ___; if this axis also describes Option B, it is invalid — not incomplete, invalid; return to Pre-Check)*`. Tests whether the vocabulary must appear AT the competitive section (not just in the pre-analysis rules block) for C-14's second mechanism to pass.

**Two combined variations:**

**V-04** — V-01 + V-02: tabular pre-check (named slot columns) + triple-slot RULE 4 evidence. Predicted 130/130. Tests whether the two structural upgrades close both C-14 and C-15 without requiring the inline section-header annotation.

**V-05** — Maximalist: V-04 + V-03 (inline section header "invalid") + typed AMEND protocols (Type 1/2/3 with full execution instructions) + CONVERGENCE UNRESOLVABLE with strategic forward interpretation. Belt-and-suspenders-and-belt on C-14. Predicted 130/130.

**Key isolation bets:**
- If V-01 scores C-14 PASS → RULE 3 pre-analysis block counts as "point of competitive analysis"; inline annotation redundant for scoring
- If V-02 scores C-15 PASS → R3 V-04 template already satisfied C-15; triple-slot is quality upgrade only
- If both gaps are real → V-04/V-05 are required for 130/130
ive section header annotation level
4. Combine upgrades
5. Maximize

**Three single-axis variations:**
- **V-01** (output format) — RULE 4 triple-slot format: `[Option × Dimension] = [finding] → [direction]`
- **V-02** (lifecycle emphasis) — tabular COMPETITIVE AXIS PRE-CHECK with named column headers: `| Axis Slot | Option A | Option B |`
- **V-03** (phrasing register) — inline "invalid" vocabulary embedded in competitive section annotation header, not just in pre-analysis rules block

**Two combined variations:**
- **V-04** — V-01 (triple-slot RULE 4) + V-02 (tabular pre-check): closes C-15 and strengthens C-14 first mechanism
- **V-05** — V-04 + V-03 (inline section header) + typed AMEND protocols + CONVERGENCE UNRESOLVABLE strategic framing: full C-14 dual-mechanism + C-15 machine-parseable + all C-08 depth

**Key design bets**:
1. V-01 vs V-02 isolation: C-15 depends on the triple-slot field split, not on pre-check structure. V-02 keeps the R3 evidence format — if C-15 is still PARTIAL for V-02, the field-split is confirmed as the discriminating factor.
2. V-03 isolation: C-14's second mechanism ("disqualification language at the point of competitive analysis") requires the "invalid" vocabulary to appear AT the competitive section, not just in the pre-analysis rules block. V-03 tests this without changing other elements.
3. V-04 bet: tabular pre-check + triple-slot closes both C-14 and C-15 without requiring the inline header annotation. If V-04 scores 130/130, the inline annotation (V-03) is redundant for scoring — only adds belt-to-suspenders-to-belt.
4. V-05 bet: all mechanisms simultaneously active; if V-04 reaches 130, V-05 is the canonical maximalist form of the full prompt.

---

## V-01 — Triple-slot RULE 4 evidence template

**Axis**: Output format — RULE 4 evidence template upgraded from single prose field to triple-slot machine-parseable format: `[Option × Dimension] = [finding] → [direction]`
**Hypothesis**: R3 V-04's evidence template has the coordinate slot but merges finding and direction into a single fill-in field (`___ — drives the recommendation because ___`). C-15's pass condition requires explicitly named finding and direction slots as separate fields. Splitting them with the `= [finding] → [direction]` format creates the machine-parseable contract C-15 describes — each field has a bounded, named role, making it unambiguous what goes where. All other elements identical to R3 V-04.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Axes are declared before analysis begins and tested for convergence. If convergence is detected, distinct axes must be assigned before analysis proceeds.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells using the named triple-slot evidence format. Each citation entry has three required named fields:

```
[Option × Dimension] = [finding] → [direction]
```

- `[Option × Dimension]` — the cell coordinate (e.g., "Option A × Risk")
- `[finding]` — what the matrix cell says, verbatim or close paraphrase
- `[direction]` — how this finding votes: "favors Option A," "rules out Option B," "supports neither," etc.

Do not merge finding and direction into a prose sentence. Fill each slot separately.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

Declare each option's primary competitive axis before writing any option analysis:

- **Option A axis**: ___ (what does it beat, on what dimension?)
- **Option B axis**: ___ (what does it beat, on what dimension?)

**Convergence test**: same axis?

- **[YES — both claim ___]**: **RULE 3: both axes claiming [same axis] are invalid.** Resolve before proceeding:
  - Option A distinct axis: ___ (the axis Option A owns that Option B does not)
  - Option B distinct axis: ___ (the axis Option B owns that Option A does not)
  - If no distinct axes can be found: "CONVERGENCE UNRESOLVABLE — both options compete identically on [axis]. This is a strategic finding, not a comparison result. A third option claiming [different axis] may dominate. Return to option framing." Stop here.

- **[NO — axes are distinct]**: axes confirmed. Proceed.

*Confirmed axes are locked. Do not modify during option analysis.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option A's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option B's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axes in their respective rows. You will complete RULE 4 citations from these cells — note the coordinate of any cell you may cite.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — complete two RULE 4 citation entries (fill all three named slots per entry):

```
[Option × Dimension] = [finding] → [direction]
[Option × Dimension] = [finding] → [direction]
```

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

Suggest at least one amendment:
- A third option not yet considered (declare its axis in Pre-Check, apply all four rules, expand matrix)
- A dimension that should carry more weight for this topic (state whether conclusion flips if it doubles)
- An audience variant (exec leads with strategic implication; engineering leads with feasibility/risk delta)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-02 — Tabular axis pre-check

**Axis**: Lifecycle emphasis — COMPETITIVE AXIS PRE-CHECK upgraded from prose bullet slots to a table with named column headers; axis slots become explicit named cells in a two-column table (`| Axis Slot | Option A | Option B |`) rather than prose fill-ins
**Hypothesis**: C-14's first mechanism requires "explicit axis slots." The R3 V-04 format (`- **Option A axis**: ___ (what does it beat, on what dimension?)`) is a prose slot — the slot exists but is not a named, bounded field. A table with column headers creates unambiguous named slots: the cell at row "Primary axis" / column "Option A" is an explicit, addressable field. If C-14 is PARTIAL for R3 V-04 due to "explicit" ambiguity, the table form resolves it. RULE 4 evidence template unchanged from R3 V-04 to isolate C-14 effect.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Axes are declared and slot-filled in the Pre-Check table before analysis begins. If both options fill the same slot values, the claim is disqualified — distinct axes must be assigned before analysis proceeds.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells by coordinate ([Option x Dimension]) as evidence. Asserting a winner without naming specific cells is insufficient.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

*Fill all axis slots in the table below before writing any option analysis. Slot values are locked after this section.*

| Axis Slot | Option A | Option B |
|-----------|----------|----------|
| Primary axis name | | |
| What does it beat? | | |
| On what dimension? | | |

**Convergence test**: do both options claim the same primary axis name or the same dimension?

- **[YES — both claim ___]**: **RULE 3: convergence detected — this axis claim is invalid.** Resolve before proceeding:
  - Replace Option A "Primary axis name" slot with: ___ (an axis Option A owns that Option B does not)
  - Replace Option B "Primary axis name" slot with: ___ (an axis Option B owns that Option A does not)
  - If no distinct axes can be found: "CONVERGENCE UNRESOLVABLE — both options compete identically on [axis]. A third option claiming [different axis] may dominate. Return to option framing." Stop here.

- **[NO — axes are distinct]**: slot values confirmed. Proceed.

*Confirmed slot values are locked for the analysis below. Do not modify them without re-running this section.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis from Pre-Check table)*
Build the strategic story on Option A's confirmed axis (from the "Primary axis name" slot). Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis from Pre-Check table)*
Build the strategic story on Option B's confirmed axis (from the "Primary axis name" slot). Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axis slot values in their respective rows. You will reference these cells by [Option x Dimension] in the recommendation.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — cite at least two matrix cells by coordinate:
- **[Option x Dimension]**: ___ — drives the recommendation because ___
- **[Option x Dimension]**: ___ — [supports or rules out] because ___

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

Suggest at least one amendment:
- A third option not yet considered (add a row to the Pre-Check axis table for Option C, apply all four rules, expand matrix)
- A dimension that should carry more weight for this topic (state whether conclusion flips if it doubles)
- An audience variant (exec leads with strategic implication; engineering leads with feasibility/risk delta)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-03 — Inline section-header disqualification

**Axis**: Phrasing register — competitive section annotation upgraded from `*(RULE 3 — expand confirmed axis)*` to an inline disqualification trigger that contains the "invalid — not incomplete, invalid" vocabulary directly at the section header; pre-check gate and RULE 3 pre-analysis block unchanged
**Hypothesis**: C-14's second mechanism is "inline disqualification vocabulary at the point of competitive analysis." R3 V-04/V-05 have RULE 3 "invalid" vocabulary in the PRE-ANALYSIS RULES block, but the competitive section annotation only says `*(RULE 3 — expand confirmed axis)*` — it references the rule but does not reproduce the disqualification language. If C-14 requires the vocabulary to appear AT the competitive section (not just in the pre-analysis block), adding it to the annotation closes this. This tests whether the section-header location of "invalid — not incomplete, invalid" is the discriminating factor for C-14's second mechanism.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Axes are declared before analysis begins and tested for convergence. If convergence is detected, distinct axes must be assigned before analysis proceeds.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells by coordinate ([Option x Dimension]) as evidence. Asserting a winner without naming specific cells is insufficient.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

Declare each option's primary competitive axis before writing any option analysis:

- **Option A axis**: ___ (what does it beat, on what dimension?)
- **Option B axis**: ___ (what does it beat, on what dimension?)

**Convergence test**: same axis?

- **[YES — both claim ___]**: **RULE 3: this axis is invalid — not incomplete, invalid.** Resolve before proceeding:
  - Option A distinct axis: ___ (the axis Option A owns that Option B does not)
  - Option B distinct axis: ___ (the axis Option B owns that Option A does not)
  - If unresolvable: "CONVERGENCE UNRESOLVABLE — both options compete on [axis]. A third option claiming [different axis] may dominate. Return to option framing." Do not continue.

- **[NO — axes are distinct]**: axes confirmed. Proceed.

*Confirmed axes are locked. Do not modify them during option analysis.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — confirmed axis from Pre-Check: ___; if this axis also describes Option B, it is invalid — not incomplete, invalid; return to Pre-Check before expanding)*
Build the strategic story on Option A's confirmed axis. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — confirmed axis from Pre-Check: ___; if this axis also describes Option A, it is invalid — not incomplete, invalid; return to Pre-Check before expanding)*
Build the strategic story on Option B's confirmed axis. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axes in their respective rows. You will reference these cells by [Option x Dimension] in the recommendation.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — cite at least two matrix cells by coordinate:
- **[Option x Dimension]**: ___ — drives the recommendation because ___
- **[Option x Dimension]**: ___ — [supports or rules out] because ___

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

Suggest at least one amendment:
- A third option not yet considered (declare its axis in Pre-Check, apply all four rules, expand matrix)
- A dimension that should carry more weight for this topic (state whether conclusion flips if it doubles)
- An audience variant (exec leads with strategic implication; engineering leads with feasibility/risk delta)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-04 — Combination: tabular pre-check + triple-slot RULE 4

**Axis**: Combination of V-02 (tabular COMPETITIVE AXIS PRE-CHECK with named slot headers) and V-01 (RULE 4 triple-slot machine-parseable evidence template); all four PRE-ANALYSIS RULES; no V-03 inline header annotation
**Hypothesis**: The two single-axis variations address different gaps. V-02's tabular pre-check closes C-14's "explicit axis slots" requirement — named column headers make the slot structure unambiguous. V-01's triple-slot RULE 4 format closes C-15 — the `= [finding] → [direction]` split makes citation machine-parseable with bounded named fields. Combining both should close C-14 and C-15 simultaneously without requiring the V-03 inline annotation. If this combination reaches 130/130, the inline annotation is redundant for scoring and V-03 measures a non-discriminating enhancement.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Axes are declared and slot-filled in the Pre-Check table before analysis begins. If both options fill the same slot values, the claim is disqualified — distinct axes must be assigned.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells using the named triple-slot evidence format. Each citation entry has three required named fields:

```
[Option × Dimension] = [finding] → [direction]
```

- `[Option × Dimension]` — the cell coordinate (e.g., "Option A × Inertia")
- `[finding]` — what the matrix cell says, verbatim or close paraphrase
- `[direction]` — how this finding votes: "favors Option A," "rules out Option B," "supports neither," etc.

Do not merge finding and direction into a prose sentence. Fill each slot separately.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

*Fill all axis slots in the table below before writing any option analysis. Slot values are locked after this section.*

| Axis Slot | Option A | Option B |
|-----------|----------|----------|
| Primary axis name | | |
| What does it beat? | | |
| On what dimension? | | |

**Convergence test**: do both options claim the same primary axis name or the same dimension?

- **[YES — both claim ___]**: **RULE 3: convergence detected — this axis claim is invalid — not incomplete, invalid.** Resolve before proceeding:
  - Replace Option A "Primary axis name" slot with: ___ (an axis Option A owns that Option B does not)
  - Replace Option B "Primary axis name" slot with: ___ (an axis Option B owns that Option A does not)
  - If no distinct axes can be found: "CONVERGENCE UNRESOLVABLE — both options compete identically on [axis]. This is a strategic finding, not a comparison result. A third option claiming [different axis] may dominate. Return to option framing." Stop here.

- **[NO — axes are distinct]**: slot values confirmed. Proceed.

*Confirmed slot values are locked for the analysis below. Do not modify them without re-running this section.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis from Pre-Check table)*
Build the strategic story on Option A's confirmed axis (from the "Primary axis name" slot). Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis from Pre-Check table)*
Build the strategic story on Option B's confirmed axis (from the "Primary axis name" slot). Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axis slot values in their respective rows. You will complete RULE 4 citations from these cells.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — complete two RULE 4 citation entries (fill all three named slots per entry):

```
[Option × Dimension] = [finding] → [direction]
[Option × Dimension] = [finding] → [direction]
```

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

Suggest at least one amendment:
- A third option not yet considered (add a row to the Pre-Check axis table for Option C, apply all four rules, expand matrix)
- A dimension that should carry more weight for this topic (state whether conclusion flips if it doubles)
- An audience variant (exec leads with strategic implication; engineering leads with feasibility/risk delta)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-05 — Maximalist: tabular pre-check + inline header + triple-slot RULE 4 + typed AMEND

**Axis**: Combination — V-04 (tabular pre-check + triple-slot RULE 4) + V-03 (inline section-header disqualification vocabulary) + typed AMEND protocols (three distinct amendment types with full execution instructions) + CONVERGENCE UNRESOLVABLE with strategic forward interpretation
**Hypothesis**: V-04 closes C-14 and C-15 via structural upgrades (table slots + triple-slot evidence). V-05 adds V-03's inline section-header mechanism as a third enforcement layer on C-14 — making the "invalid" vocabulary appear at three locations: RULE 3 pre-analysis block, COMPETITIVE AXIS PRE-CHECK convergence test, AND each competitive section header annotation. Typed AMEND protocols (AMEND Type 1/2/3 with full execution instructions) maximize C-08. CONVERGENCE UNRESOLVABLE path adds strategic interpretation rather than a bare halt. If V-04 already reaches 130/130, V-05 is the fully-armored canonical form of the discover-compare prompt.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, it is not a distinguishing finding. Discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Declare and slot-fill axes in the Pre-Check table before analysis begins. If convergence is detected, distinct axes must be assigned or convergence is surfaced as a strategic finding.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells using the named triple-slot evidence format. Each citation entry has three required named fields:

```
[Option × Dimension] = [finding] → [direction]
```

- `[Option × Dimension]` — the cell coordinate (e.g., "Option B × Competitive")
- `[finding]` — what the matrix cell says, verbatim or close paraphrase
- `[direction]` — how this finding votes: "favors Option A," "rules out Option B," "supports neither," etc.

Do not merge finding and direction into a prose sentence. Fill each slot separately.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

*Fill all axis slots in the table below before writing any option analysis. Slot values are locked after this section.*

| Axis Slot | Option A | Option B |
|-----------|----------|----------|
| Primary axis name | | |
| What does it beat? | | |
| On what dimension? | | |

**Convergence test**: do both options claim the same primary axis name or the same dimension?

- **[YES — both claim ___]**: **RULE 3: this axis is invalid — not incomplete, invalid.** Resolve before proceeding:
  - Replace Option A "Primary axis name" slot with: ___ (the axis Option A owns that Option B does not)
  - Replace Option B "Primary axis name" slot with: ___ (the axis Option B owns that Option A does not)
  - If unresolvable: "CONVERGENCE UNRESOLVABLE — both options compete on [axis]. This weakens the case for both and is a strategic finding in its own right. A third option claiming [different axis] may dominate the comparison entirely. Return to option framing before proceeding." Do not continue.

- **[NO — axes are distinct]**: slot values confirmed. Proceed.

*Confirmed slot values are locked for the analysis below. Do not modify them without re-running this section.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — confirmed axis from Pre-Check table: ___; if this axis also describes Option B, it is invalid — not incomplete, invalid; return to Pre-Check before expanding)*
Build the strategic story on Option A's confirmed axis. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — confirmed axis from Pre-Check table: ___; if this axis also describes Option A, it is invalid — not incomplete, invalid; return to Pre-Check before expanding)*
Build the strategic story on Option B's confirmed axis. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axis slot values in their respective rows. You will complete RULE 4 citations from these cells.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — complete two RULE 4 citation entries (fill all three named slots per entry):

```
[Option × Dimension] = [finding] → [direction]
[Option × Dimension] = [finding] → [direction]
```

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

**AMEND Type 1 (add Option C)**: If the user provides a third option, add a column to the COMPETITIVE AXIS PRE-CHECK table for Option C, fill all three axis slots, run the convergence test against both existing options, apply all four PRE-ANALYSIS RULES to Option C, expand the matrix to three columns, and issue a revised recommendation with updated triple-slot RULE 4 citations.

**AMEND Type 2 (reweight)**: If the user names a dimension to weight more heavily, re-examine whether the recommendation changes if that dimension counts double in the RULE 4 evidence. State explicitly whether the conclusion flips and which `[finding] → [direction]` entry changes.

**AMEND Type 3 (audience)**: If the user specifies exec or engineering audience, re-render the recommendation with a register-appropriate lead — exec leads with the bottom line and strategic implication from the Competitive row; engineering leads with the feasibility and risk delta.

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## Predicted Rubric Coverage (v4 — 130 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 all 4 dimensions per option | P | P | P | P | P |
| C-02 inertia = "do nothing vs THIS" | P | P | P | P | P |
| C-03 decision matrix present | P | P | P | P | P |
| C-04 recommendation with rationale | P | P | P | P | P |
| C-05 inertia friction specific | P | P | P | P | P |
| C-06 option-specific risks | P | P | P | P | P |
| C-07 neither outcome considered | P | P | P | P | P |
| C-08 AMEND paths surfaced | P | P | P | P | P |
| C-09 competitive positioning distinct | P | P | P | P | P |
| C-10 inertia hard gate | P | P | P | P | P |
| C-11 cross-option risk disqualifier | P | P | P | P | P |
| C-12 recommendation traces to cells | P | P | P | P | P |
| C-13 competitive axis distinctness rule | P | P | P | P | P |
| C-14 dual-mechanism axis enforcement | PART | PART | P | P | P |
| C-15 recommendation evidence template | P | PART | PART | P | P |

**Notes on PARTIAL predictions:**
- V-01 C-14 PARTIAL: pre-check gate present (named section with prose slots) but C-14 requires "explicit axis slots" — prose bullet slots may be borderline; inline "invalid" vocabulary present only in RULE 3 pre-analysis block, not at competitive section annotation level. May pass on the RULE 3 block alone; scored PART as conservative estimate. The key test: does the pre-analysis rules block count as "at the point of competitive analysis" for C-14's second mechanism?
- V-02 C-15 PARTIAL: evidence template keeps R3 V-04 format (`[Option x Dimension]: ___ — drives the recommendation because ___`); one field merges finding+direction. C-15 requires explicitly split named fields. Scored PART.
- V-03 C-15 PARTIAL: same as V-02 — evidence template unchanged from R3 V-04. Scored PART.
- V-03 C-14 PASS: named pre-check gate present (prose slots, same as R3 V-04) + inline "invalid — not incomplete, invalid" vocabulary in competitive section annotation headers. Both mechanisms explicitly present at their respective locations.
- V-04 C-14 PASS: tabular pre-check with named column headers closes "explicit axis slots"; RULE 3 "invalid" vocabulary in pre-analysis block + convergence test "invalid — not incomplete, invalid" phrasing. Both mechanisms present.
- V-04 C-15 PASS: triple-slot RULE 4 with named `[finding]` and `[direction]` fields is machine-parseable and satisfies the binary fill-in contract.

**Predicted scores** (Essential 60 + Recommended 30 + Aspirational 40 = 130 pts total):
- V-01: ~125 (C-14 PART = -3; all other criteria pass; C-15 expected PASS from triple-slot upgrade)
- V-02: ~125 (C-15 PART = -3; C-14 tabular pre-check expected PASS)
- V-03: ~125 (C-15 PART = -3; C-14 inline annotation expected PASS)
- V-04: 130 (C-14 tabular + C-15 triple-slot both pass; all other criteria inherited from R3 V-04)
- V-05: 130 (same as V-04 + belt-to-suspenders-to-belt on C-14; typed AMEND protocols strongest C-08)

All predicted Golden (>= 102, all essential pass). V-04 and V-05 predicted 130/130. V-01/V-02/V-03 predicted ~125 — each 5 pts below perfect on the single criterion they do not upgrade.

**Key isolation signals from this round:**
- If V-01 scores C-14 PASS: the pre-analysis RULE 3 block counts as "at the point of competitive analysis" — inline section annotation is not required for C-14's second mechanism.
- If V-01 scores C-14 PARTIAL: the second mechanism must be AT the competitive section, not just in the rules block — V-03 and V-05 are the reliable C-14 mechanisms.
- If V-02 scores C-15 PASS: the R3 V-04 evidence template already satisfied C-15 — the triple-slot format is a quality upgrade, not a pass/fail gate.
- If V-02 scores C-15 PARTIAL: the field split (`[finding]` vs `[direction]`) is the discriminating factor — V-01, V-04, V-05 are required for C-15 PASS.
