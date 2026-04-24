## prove-synthesize — Round 4 Scorecard

### Scoring Structure (v4)

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational (v3 inherited) | C-09–C-15 | 2.5 | 17.5 |
| Aspirational (v4 new) | C-16–C-19 | 2.5 | 10 |
| **Total** | | | **117.5** |

---

### V-01: Role Sequence — Explicit Role Prohibition

**Axis:** Explicit prohibition statements appended to each role section opener. Single-axis C-16 implementation.

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: [YES/NO/MAYBE] opens the judgment paragraph by design. Direct answer before reasoning. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 block present with calibration gate ("High confidence >= 75: name converging signals"). |
| C-03 | **PASS** | EVIDENCE HIERARCHY names up to 3 signals by artifact; each paragraph argues why it carried weight. |
| C-04 | **PASS** | ADVERSARY phase structurally enforces counter-evidence before determination; gate requires "at least two paragraphs name specific record vulnerabilities." |
| C-05 | **PASS** | JUDGE issues a determination that weighs the ADVERSARY challenge — a judgment call, not a signal summary. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Principles section inherited from R3 structure; declarative extractions required. |
| C-07 | **PASS** | Open questions section inherited; gate requires specific, actionable naming. |
| C-08 | **PASS** | Confidence paragraph required by DETERMINATION SEAL: "CONFIDENCE notation without this paragraph is a procedural breach." |

**Recommended subtotal: 30/30**

#### Aspirational v3 inherited (C-09–C-15, 2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | R3 baseline answer-first structure enforced throughout. |
| C-10 | **PASS** | Three-phase gate architecture (SURVEYOR→ADVERSARY→JUDGE) inherited intact. |
| C-11 | **PASS** | ADVERSARY gate: "each challenge paragraph is sourced to a specific signal gap, logical gap, or unconsidered scenario." Named failure mode required. |
| C-12 | **PASS** | Evidence hierarchy prose paragraphs answer the comparative question (rank 1 vs rank 2 relative weight). Tension with C-11 preserved. |
| C-13 | **PASS** | SURVEYOR gate: "Record count: [N]" required explicitly; omission is gate breach. |
| C-14 | **PASS** | "DETERMINATION: is absent from the opening sentence — the register word must commit before reasoning follows." Sentence-level declaration enforced. |
| C-15 | **PASS** | ADVERSARY gate: "NOT: this section is placed after the DETERMINATION" — structural pre-placement enforced by gate clause. |

**v3 Aspirational subtotal: 17.5/17.5**

#### Aspirational v4 new (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-16 | **PASS** | Role labels (SURVEYOR/ADVERSARY/JUDGE) present *and* explicit prohibition statements appended: "A JUDGE cannot hedge. Violation is a procedural breach." / "An ADVERSARY cannot advocate... Advocacy in the ADVERSARY phase is a procedural breach." Foreclusion mechanism explicitly named. |
| C-17 | **FAIL** | ADVERSARY paragraph 3 asks for a "failure mode this synthesis must avoid — not a generic warning, but one that fits this investigation's signal set." This instructs record-specificity but does not supply the structural template (`Given this record's [N, method diversity, signal concentration], the most likely failure mode is [X]`) that makes the diagnosis verifiable and derivable. |
| C-18 | **PASS** | DETERMINATION: [YES/NO/MAYBE] format inherited; DETERMINATION is first word. DETERMINATION SEAL confirms: "DETERMINATION: [YES/NO/MAYBE] opens the judgment paragraph." Output-level enforcement sufficient; no explicit NOT:-first gate present but format produces the correct behavior. |
| C-19 | **FAIL** | No frontmatter DECLARATIONS block. Standard bottom-of-artifact metadata format retained (R3 pattern). |

**v4 Aspirational subtotal: 5.0/10.0**

**V-01 Composite: 112.5 / 117.5**

---

### V-02: Lifecycle Emphasis — Record-Specific Anti-Pattern Diagnosis

**Axis:** Record-specific anti-pattern template in PHASE 2. Descriptive PHASE 1/2/3/4/5 titles — no role labels. Single-axis C-17 implementation.

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: format inherited; PHASE 3: DETERMINATION opens with direct answer. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with calibration gate present. |
| C-03 | **PASS** | PHASE 4: EVIDENCE HIERARCHY retains ranked prose paragraph structure. |
| C-04 | **PASS** | PHASE 2: ADVERSARIAL CHALLENGE structurally enforces counter-evidence; gate retained. |
| C-05 | **PASS** | Synthesis phases issue judgment, not summary. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Principles section in PHASE 5 inherited. |
| C-07 | **PASS** | Open questions in PHASE 5 inherited. |
| C-08 | **PASS** | Confidence paragraph gate retained in DETERMINATION phase. |

**Recommended subtotal: 30/30**

#### Aspirational v3 inherited (C-09–C-15, 2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Answer-first structure enforced. |
| C-10 | **PASS** | Three-phase sequence retained via PHASE 1/2/3 structural ordering. |
| C-11 | **PASS** | ADVERSARY gate language retained; named failure mode required ("one that fits this investigation's signal set"). |
| C-12 | **PASS** | Evidence hierarchy prose paragraphs retained; comparative weight argument required. |
| C-13 | **PASS** | PHASE 1 SIGNAL INVENTORY still requires "Record count: [N]." |
| C-14 | **PASS** | DETERMINATION: register word at sentence level enforced. |
| C-15 | **PASS** | PHASE 2 structurally precedes PHASE 3; pre-placement gate retained. |

**v3 Aspirational subtotal: 17.5/17.5**

#### Aspirational v4 new (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-16 | **FAIL** | Explicit design decision: V-02 uses PHASE 1/2/3/4/5 descriptive titles precisely to *not* fire C-16. No role-identity labels (SURVEYOR/ADVERSARY/JUDGE) present; no prohibition statements. C-16 mechanism (procedural identity forecloses output type) requires role labels as the identity carrier. |
| C-17 | **PASS** | Template present in PHASE 2: `Given this record's [structural property — N=[count], method diversity, signal concentration], the most likely failure mode is [X]. Rationale: [causal link].` Structural property derivable from PHASE 1 inventory — verifiable. Record-specific derivation enforced by template structure, not mere instruction. |
| C-18 | **PASS** | DETERMINATION: [YES/NO/MAYBE] format produces register word as first word of commitment sentence. Output-level enforcement. |
| C-19 | **FAIL** | No frontmatter DECLARATIONS block; standard bottom-of-artifact format retained. |

**v4 Aspirational subtotal: 5.0/10.0**

**V-02 Composite: 112.5 / 117.5**

---

### V-03: Output Format — Frontmatter Commitment Declarations

**Axis:** Frontmatter DECLARATIONS block opens artifact before first prose. Role labels present; no explicit prohibition statements. Single-axis C-19 implementation.

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: format inherited; answer-first enforced. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with calibration gate. |
| C-03 | **PASS** | EVIDENCE HIERARCHY retained. |
| C-04 | **PASS** | ADVERSARY phase retained with structural pre-placement gate. |
| C-05 | **PASS** | Synthesis issues judgment against adversarial challenge. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Principles section inherited. |
| C-07 | **PASS** | Open questions section inherited. |
| C-08 | **PASS** | Confidence paragraph gate retained. |

**Recommended subtotal: 30/30**

#### Aspirational v3 inherited (C-09–C-15, 2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Inherited. |
| C-10 | **PASS** | SURVEYOR/ADVERSARY/JUDGE sequence retained. |
| C-11 | **PASS** | Named failure mode required in ADVERSARY gate. |
| C-12 | **PASS** | Evidence hierarchy prose paragraphs retained. |
| C-13 | **PASS** | Record count required in SURVEYOR gate. |
| C-14 | **PASS** | Sentence-level DETERMINATION: declaration enforced. |
| C-15 | **PASS** | ADVERSARY structurally precedes JUDGE; gate retained. |

**v3 Aspirational subtotal: 17.5/17.5**

#### Aspirational v4 new (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-16 | **PARTIAL** | Role labels (SURVEYOR/ADVERSARY/JUDGE) present — identity carrier exists. But no explicit prohibition statements appended ("A JUDGE cannot hedge. Violation is a procedural breach."). C-16's mechanism is that *procedural identity forecloses output type* — labels name the identity, but prohibition statements are the foreclusion mechanism. Labels alone establish identity without explicitly foreclosing output type at the procedural level. R3 V-05 had this same design; R4 distinguishes by adding prohibition statements in V-01/V-04/V-05. Scored as partial: identity present, foreclusion mechanism absent. **+1.25** |
| C-17 | **FAIL** | No record-specific anti-pattern template. ADVERSARY gate language is inherited R3 pattern ("fits this investigation's signal set") without the structural derivation template that makes C-17 verifiable. |
| C-18 | **PASS** | DETERMINATION: first word enforced by output format. |
| C-19 | **PASS** | Frontmatter DECLARATIONS block (`adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`) opens artifact before first prose. Writer fills each field at the structural point it becomes determinable. Explicit NOT: "frontmatter fields are left blank during writing and filled retroactively — retroactive completion defeats the function of a pre-commitment declaration." |

**v4 Aspirational subtotal: 6.25/10.0**

**V-03 Composite: 113.75 / 117.5**

---

### V-04: Role Prohibition + Record-Specific Diagnosis + Register-Word-First NOT:

**Axis:** C-16 + C-17 + C-18 explicit. No frontmatter declarations.

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: format inherited. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with calibration gate. |
| C-03 | **PASS** | EVIDENCE HIERARCHY retained. |
| C-04 | **PASS** | ADVERSARY phase with structural pre-placement gate. |
| C-05 | **PASS** | Judgment issued against adversarial challenge. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Inherited. |
| C-07 | **PASS** | Inherited. |
| C-08 | **PASS** | Confidence paragraph gate retained. |

**Recommended subtotal: 30/30**

#### Aspirational v3 inherited (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-15 | **PASS × 7** | All inherited intact; SURVEYOR/ADVERSARY/JUDGE sequence, record count, sentence-level DETERMINATION:, structural pre-placement all present. |

**v3 Aspirational subtotal: 17.5/17.5**

#### Aspirational v4 new (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-16 | **PASS** | Role labels + explicit prohibition: "A JUDGE cannot hedge. Violation is a procedural breach." / "An ADVERSARY does not advocate... Advocacy in the ADVERSARY phase is a procedural breach." Full foreclusion mechanism present. |
| C-17 | **PASS** | RECORD DIAGNOSIS template present: `Given this record's [structural property — N=[count], method diversity, signal concentration], the most likely failure mode is [X]. Rationale: [causal link].` Derives failure mode from verifiable record properties inventoried in SURVEYOR phase. |
| C-18 | **PASS** | DETERMINATION: format enforced *plus* explicit NOT: gate: "NOT: the register word appears in a section header, parenthetical, or after introductory language in the commitment sentence." Dual-layer enforcement: output format + explicit prohibition. Strongest C-18 pass condition. |
| C-19 | **FAIL** | No frontmatter DECLARATIONS block. V-04 retains standard bottom-of-artifact metadata (R3 format). |

**v4 Aspirational subtotal: 7.5/10.0**

**V-04 Composite: 115.0 / 117.5**

---

### V-05: Full Combo — All Four New Criteria + Complete R3 Inheritance

**Axis:** C-16 + C-17 + C-18 + C-19. Maximum score design.

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: opens judgment paragraph; answer-first maintained through frontmatter + prose structure. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with calibration gate. |
| C-03 | **PASS** | EVIDENCE HIERARCHY prose paragraphs naming up to 3 artifacts. |
| C-04 | **PASS** | ADVERSARY phase + structural pre-placement gate. |
| C-05 | **PASS** | JUDGE phase issues determination against adversarial challenge — judgment, not summary. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Principles section inherited. |
| C-07 | **PASS** | Open questions section inherited. |
| C-08 | **PASS** | Confidence paragraph gate retained. |

**Recommended subtotal: 30/30**

#### Aspirational v3 inherited (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-15 | **PASS × 7** | All R3 mechanisms inherited: role sequence, record count, adversarial pre-placement, sentence-level register word. |

**v3 Aspirational subtotal: 17.5/17.5**

#### Aspirational v4 new (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-16 | **PASS** | Full role-label + explicit prohibition: "A JUDGE cannot hedge. Violation is a procedural breach." Foreclusion at both identity and prohibition levels. |
| C-17 | **PASS** | RECORD DIAGNOSIS template: `Given this record's [N, method diversity, signal concentration], the most likely failure mode is [X]. Rationale: [causal link].` Derivable from SURVEYOR inventory; verifiable by reader. |
| C-18 | **PASS** | DETERMINATION: register word first (output format) + explicit NOT: gate (instruction level). Strongest enforcement. |
| C-19 | **PASS** | DECLARATIONS block *opens* artifact before first prose sentence. Writer fills each boolean (`adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`) at the structural point it becomes determinable, not retroactively. Explicit NOT: forecloses post-hoc completion. |

**v4 Aspirational subtotal: 10.0/10.0**

**V-05 Composite: 117.5 / 117.5**

---

## Composite Scores

| Variation | Essential | Recommended | Asp v3 | Asp v4 | Total | Delta from base |
|-----------|-----------|-------------|--------|--------|-------|-----------------|
| V-01 | 60 | 30 | 17.5 | 5.0 | **112.5** | +5.0 |
| V-02 | 60 | 30 | 17.5 | 5.0 | **112.5** | +5.0 |
| V-03 | 60 | 30 | 17.5 | 6.25 | **113.75** | +6.25 |
| V-04 | 60 | 30 | 17.5 | 7.5 | **115.0** | +7.5 |
| V-05 | 60 | 30 | 17.5 | 10.0 | **117.5** | +10.0 |

**Rank: V-05 > V-04 > V-03 > V-01 = V-02**

All five variations: all-essential PASS. All five: Golden (>= 90). V-05 is the only maximum score.

---

## R4 Calibration Questions — Resolved

**Q1: Does C-16 require explicit prohibition language, or do role labels alone suffice?**
V-01 (labels + prohibitions) and V-03 (labels only) diverge: V-01 = 112.5, V-03 = 113.75. V-03 scores *higher* due to C-19, but on C-16 specifically, V-03 is PARTIAL while V-01 is PASS. Verdict: **prohibition statements are the foreclusion mechanism; labels alone earn partial credit only.** R3 V-05 (labels only) did not fully satisfy C-16 under the v4 definition.

**Q2: Does C-18 require the explicit NOT: gate, or does the DETERMINATION: format alone satisfy it?**
All five variations produce DETERMINATION: as the first word of the commitment sentence. V-01/V-02/V-03 fire C-18 at the output level without the explicit NOT: instruction. V-04/V-05 add dual enforcement. Verdict: **output format alone satisfies C-18.** The explicit NOT: gate adds defensive robustness against prompt drift but is not required for the criterion to fire.

---

## Excellence Signals — V-05

**1. Pre-prose frontmatter as irreversible commitment architecture**
Placing `adversary_pre_determination: true` *before* the first sentence creates a constraint that cannot be retroactively satisfied. The boolean is determinable only when the adversary phase is actually complete before the determination — so the writer must complete the adversary phase first to truthfully fill the field. The frontmatter is a commitment mechanism, not a formatting convention. No other variation achieves this; bottom-of-artifact metadata can always be filled after reading the completed text.

**2. Record-derived failure mode: verifiable diagnosis via SURVEYOR inventory**
The template `Given this record's [N, method diversity, signal concentration], the most likely failure mode is [X]. Rationale: [causal link].` ties the anti-pattern diagnosis to properties inventoried in the SURVEYOR phase. A reader can falsify the diagnosis by checking whether the cited structural property actually appears in the SURVEYOR inventory. This turns C-11's "name a failure mode" from a template exercise into a record-specific diagnostic. No other variation closes this gap.

**3. Dual-layer role foreclusion: identity + prohibition**
Role labels name the procedural identity (SURVEYOR, ADVERSARY, JUDGE); explicit prohibition statements foreclose the output type at the lexical level ("A JUDGE cannot hedge. Violation is a procedural breach."). V-05 combines both: the label establishes *who the writer is* in that phase; the prohibition establishes *what that identity cannot produce*. Labels without prohibition create identity without foreclusion. Prohibition without labels creates a rule without a subject. Together they create the strongest constraint.

**4. Register-word-first across two enforcement layers**
DETERMINATION: format (output level) + explicit NOT: gate ("NOT: the register word appears after introductory language") creates defense in depth. The format produces the correct behavior; the gate forecloses the failure mode before the writer reaches the commitment sentence. V-04 has both; V-05 inherits them. The combination is more robust against prompt drift than either alone.

---

```json
{"top_score": 117.5, "all_essential_pass": true, "new_patterns": ["pre-prose frontmatter booleans create irreversible pre-commitment declarations: the writer must complete each structural phase to truthfully fill its boolean, making retroactive compliance impossible", "record-derived failure mode diagnosis links anti-pattern identification to verifiable properties in the SURVEYOR inventory (N, method diversity, signal concentration), turning a template exercise into a falsifiable record-specific diagnostic", "dual-layer role foreclusion combines identity labels (SURVEYOR/ADVERSARY/JUDGE) with explicit prohibition statements to foreclose output type at both the cognitive and lexical level — labels without prohibitions earn only partial credit for C-16"]}
```
