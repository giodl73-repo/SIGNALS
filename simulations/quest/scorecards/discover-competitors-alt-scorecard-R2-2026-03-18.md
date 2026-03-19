## discover-competitors-alt — R2 Scorecard

### Scores

| Variation | Essential | Recommended | Aspirational | Composite | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-03 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-04 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-05 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-02 | 5/5 | 3/3 | 3.5/4 | **98.75** | Exceptional |
| V-01 | 5/5 | 3/3 | 3/4 | **97.5** | Exceptional |

All five variations pass all essential criteria — R2 closed the essential gap from R1.

---

### Key criterion calls

**C-11 (Inertia propagates downstream)**
- V-01 PASS — mandatory `vs INERTIA-REF:` third slot in every finding; also in competitive map column header. Structural.
- V-02 PARTIAL — "Inertia delta" column covers competitor comparisons, but the mechanism has no formal short label and findings have no slot. Propagation stops at the map.
- V-03 PASS — MECH label explicitly named by the model; "Use this label in the competitor map and in every finding below. Don't drop it after this section." Maximally explicit instruction.
- V-04 PASS — Template slot + INERTIA-REF block + column header. Full structural enforcement at both map and findings levels.
- V-05 PASS — `consumes: INERTIA-REF` declared in Phase 2, Phase 3, Phase 4, AMEND. Deepest architectural enforcement. Phase 3 uniquely requires confirming ROOT INERTIA-REF doesn't cover the gap.

**C-12 (AMEND evaluates inertia stability)**
- V-01 FAIL — AMEND has no stability column. Axis was findings propagation only; this outcome was by design.
- V-02 PASS — `INERTIA-REF stable?` column required per row, with substantive reasoning examples.
- V-03 PASS — "Say whether the amendment would change the MECH or leave it stable." Conversational but direct.
- V-04 PASS — `INERTIA-REF stable?` column, min 2 rows, "A silent entry does not pass C-12."
- V-05 PASS — Output contract framing: "whether the amendment would alter INERTIA-REF or leave it stable." "A silent cell does not satisfy the AMEND output contract."

---

### Excellence signals (new from R2)

1. **Named mechanism handle is the prerequisite for C-11 — format is secondary.** V-03 uses a model-defined MECH label; V-04 uses a template-defined INERTIA-REF block; V-05 uses a ROOT output declaration. All three work. The label is the operative element, not the syntax around it.

2. **C-12 is achievable without lifecycle scaffolding.** V-02 confirmed the column alone works. V-03 confirmed conversational instruction works. Minimum viable: one explicit stability question per AMEND entry.

3. **Conversational register achieves perfect score when three imperatives are stated in order:** (a) name the mechanism with a short label, (b) use that label in every subsequent section, (c) state stability per amendment entry. No tables, no phase headers required.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named mechanism handle satisfies C-11 in any register -- conversational label (MECH), template block (INERTIA-REF), or architectural ROOT declaration all work; the label is the operative element not the format around it", "AMEND stability column achieves C-12 independently of lifecycle scaffolding -- confirmed by V-02 isolation and V-03 conversational equivalent; minimum viable enforcement is one explicit stability question per AMEND entry", "Conversational register achieves perfect score when three direct imperatives are stated in order: name the mechanism with a label, use that label in every subsequent section, address stability per amendment entry"]}
```
-|--------|---------|
| C-01 | Threat levels on all entries | PASS | C0 section: "Assign a threat level (almost always HIGH)." Map: "Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-02 | Named entries, no generic labels | PASS | "Rows 1-N: minimum 3 named external competitors. No generic labels." C0 named specifically. |
| C-03 | Focus dimension woven | PASS | "[Focus column if active]" in table schema applied to every row. No trailing-section risk: the column is in the schema or absent entirely. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific uncontested dimension not owned by C0 or any listed competitor]" with explicit anti-generic instruction. |
| C-05 | Auto-detect | PASS | "Read the repo context (README, CLAUDE.md, package.json, or equivalent)... Proceed immediately." |
| C-06 | Mechanism-level inertia | PASS | "Name the specific stickiness mechanism -- one of: switching cost, habit lock-in, workaround satisfaction -- tied to something C0 does or provides. This is the **inertia mechanism** for the analysis." Specific taxonomy + binding to C0 behavior. |
| C-07 | Web citation inline | PASS | "for at least one external row, include an inline WebSearch citation -- in the cell, not a footnote." |
| C-08 | AMEND input-to-output pairs | PASS | AMEND table has "Input change," "Output effect," and "INERTIA-REF stable?" columns. Three populated example rows. Min 2 required. |
| C-09 | Cross-dimensional whitespace | PASS | "the gap must be uncontested across both dimensions simultaneously. Demonstrate that combining the competitive map and the focus lens surfaces a gap neither alone would produce." |
| C-10 | Grounded findings | PASS | "Each must reference at least one named competitor label from the competitive map (or C0). No finding may be free-floating prose that does not require the competitive analysis to support it." |
| C-11 | Inertia propagates downstream | PARTIAL | "Inertia delta" column in competitive map requires each competitor to address the C0 mechanism (covers competitor comparisons). However: the mechanism has no formal short label in the C0 section ("the **inertia mechanism**" is a role description, not a referenceable handle); the findings section has no structural slot for the mechanism. Propagation reaches the competitor map but not findings. |
| C-12 | AMEND evaluates inertia stability | PASS | "`INERTIA-REF stable?` column must be answered for every row -- Yes, No, or conditional with explanation. A silent entry does not satisfy C-12." Example rows show substantive reasoning (Yes with justification, No with justification). V-02's primary axis confirmed. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 3.5/4 (C-11 PARTIAL)**
**Composite: (5/5 x 60) + (3/3 x 30) + (3.5/4 x 10) = 60 + 30 + 8.75 = 98.75**
**Grade: Exceptional**

---

#### V-03 — Conversational Register (C-11+C-12 in plain English)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Threat levels on all entries | PASS | "Assign it a threat level (usually HIGH)." Competitors: "Say what their threat level is (HIGH / MEDIUM / LOW) -- be explicit." Both C0 and external competitors explicitly addressed. |
| C-02 | Named entries, no generic labels | PASS | "Name at least 3 external competitors -- actual products or tools, not category labels." C0: "Name it specifically (the actual tool, habit, or workaround -- not 'the status quo' or 'incumbent')." |
| C-03 | Focus dimension woven | PASS | Per-competitor notes when focus is active: "add a note on what market segment this competitor owns." Whitespace: "the gap should only be visible when you combine the competitive map with the focus lens." No trailing-section structure to drift into. |
| C-04 | Whitespace identified | PASS | "Name one specific gap... Label it clearly. Don't just say 'there's room to innovate' -- say what the specific uncontested dimension is." |
| C-05 | Auto-detect | PASS | "Start by reading the repo to figure out what topic you're analyzing -- look at the README, CLAUDE.md, or package.json. Don't ask the user what the topic is." |
| C-06 | Mechanism-level inertia | PASS | "name one concrete mechanism -- what would users lose if they switched, what habit would be interrupted, or what workaround already solves most of the problem." MECH label established: "**Inertia mechanism (MECH): [your label] -- [specific description]**". Specific taxonomy + named handle. |
| C-07 | Web citation inline | PASS | "Look up at least one competitor with WebSearch. Put the citation right next to that competitor -- not in a footnote at the bottom." |
| C-08 | AMEND input-to-output pairs | PASS | "Give at least 2 adjustments. For each one: Say what the user changes as input. Say what happens to the output as a result. 'You can adjust the focus dimension' is not enough -- say what changes when they do." Anti-pattern explicitly named. |
| C-09 | Cross-dimensional whitespace | PASS | "the gap should only be visible when you combine the competitive map with the focus lens. A gap you could spot without the focus doesn't count. Show what the focus dimension adds." |
| C-10 | Grounded findings | PASS | "Point back to a specific named competitor from the map (or C0)." "Don't write general observations about the domain that could have been written without doing the competitive analysis." Both conditions stated. |
| C-11 | Inertia propagates downstream | PASS | Model-defined MECH label established explicitly: "Give this mechanism a short label you'll use for the rest of the analysis." Propagation mandated: "Use this label in the competitor map and in every finding below. Don't drop it after this section." Findings: "Reference the MECH label -- say how this finding connects to the inertia mechanism you named at the start. Don't drop the thread." Maximally explicit instruction in conversational register. |
| C-12 | AMEND evaluates inertia stability | PASS | "Say whether the amendment would change the MECH (the inertia anchor) or leave it stable. If the anchor would change, say why." Required for every amendment entry. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 4/4**
**Composite: (5/5 x 60) + (3/3 x 30) + (4/4 x 10) = 60 + 30 + 10 = 100**
**Grade: Exceptional**

---

#### V-04 — Propagation Template + AMEND Stability Column (direct combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Threat levels on all entries | PASS | C0 block: "Threat: HIGH (or justified lower)." Map: "Every row: explicit HIGH / MEDIUM / LOW threat." Both levels structurally required. |
| C-02 | Named entries, no generic labels | PASS | "Rows 1-N: minimum 3 named external competitors. No generic category labels." C0 named specifically in block. |
| C-03 | Focus dimension woven | PASS | Focus column in table schema per row if active. C0 Focus block if active. Whitespace requires cross-dimensional proof: "Show the intersection -- state what the focus lens adds that the competitive map alone would not surface." |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific dimension not owned by C0 or any named competitor in the table]." |
| C-05 | Auto-detect | PASS | "Read the repo context (README, CLAUDE.md, package.json, or equivalent) to identify the topic. Do not prompt the user. Resolve `focus:` state before producing any output." |
| C-06 | Mechanism-level inertia | PASS | C0 block: `INERTIA-REF: [switching cost | habit lock-in | workaround satisfaction] -> [Specific description tied to what C0 does or provides]`. Block framing makes the mechanism a named artifact propagated to the competitive map's `vs INERTIA-REF` column. |
| C-07 | Web citation inline | PASS | Dedicated Source column: "For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote." Most structurally isolated citation enforcement. |
| C-08 | AMEND input-to-output pairs | PASS | AMEND table has "Input change," "Output effect," "INERTIA-REF stable?" columns. Three populated example rows. Min 2 required. |
| C-09 | Cross-dimensional whitespace | PASS | "gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show the intersection -- state what the focus lens adds that the competitive map alone would not surface." |
| C-10 | Grounded findings | PASS | Three-part template requires "[Competitor label or C0]" as first slot. "Do not write general domain observations. Each finding must require the competitive map to support it. The `vs INERTIA-REF` slot must reference the mechanism by its description -- not as a generic callback." |
| C-11 | Inertia propagates downstream | PASS | Mandatory "vs INERTIA-REF:" third slot in every finding. INERTIA-REF as named column in competitive map. "The `INERTIA-REF` block names the mechanism. It is referenced in the competitive map's `vs INERTIA-REF` column and in the third slot of every finding." Full structural enforcement at both map and findings levels. |
| C-12 | AMEND evaluates inertia stability | PASS | "`INERTIA-REF stable?` must be answered for every row -- Yes, No, or conditional. A silent entry does not pass C-12." Example rows cover all three answer types. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 4/4**
**Composite: (5/5 x 60) + (3/3 x 30) + (4/4 x 10) = 60 + 30 + 10 = 100**
**Grade: Exceptional**

---

#### V-05 — Role Sequence + Full Propagation Chain (consumption declarations)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Threat levels on all entries | PASS | ROOT: "Assign threat level." Phase 2 map: "Every row: explicit HIGH / MEDIUM / LOW threat." ROOT executes before any table row. |
| C-02 | Named entries, no generic labels | PASS | "Rows 1-N: minimum 3 named external competitors. No generic labels." ROOT names C0 specifically before any table exists. |
| C-03 | Focus dimension woven | PASS | Focus state declared pre-execution as a named declaration. Focus column in Phase 2 schema if active. `INERTIA-REF Focus:` in ROOT block if active. Phase 3 requires cross-dimensional proof if focus active. Three-level structural enforcement. |
| C-04 | Whitespace identified | PASS | "**GAP:** [specific dimension not owned by C0 or any Phase 2 competitor]." Phase 3 completion condition requires a named gap. |
| C-05 | Auto-detect | PASS | "Auto-detect: Read repo context (README, CLAUDE.md, package.json, or equivalent). Identify topic, market domain, and plausible competitor categories. Do not prompt the user. Proceed immediately." Strongest phrasing. |
| C-06 | Mechanism-level inertia | PASS | ROOT: "Name the stickiness mechanism -- one of: switching cost, habit lock-in, workaround satisfaction -- tied to a specific behavior or capability C0 does or provides." ROOT output format: `INERTIA-REF: [C0 name] -- [mechanism type]: [specific description]`. |
| C-07 | Web citation inline | PASS | Source column in Phase 2 schema. "for at least one external row, inline WebSearch citation in this cell. Not a footnote." Phase 2 completion condition includes citation requirement. |
| C-08 | AMEND input-to-output pairs | PASS | AMEND "output contract" explicitly requires all three elements per row: input change, output effect across affected phases, stability declaration. Four populated example rows with phase-level output specificity. |
| C-09 | Cross-dimensional whitespace | PASS | Phase 3: "gap must be uncontested across BOTH the competitive dimension AND the focus column simultaneously. Show intersection -- name what the focus lens adds that the competitive map alone would not surface. Confirm that ROOT INERTIA-REF does not cover this gap either." Three-condition gap proof required. |
| C-10 | Grounded findings | PASS | Template: "[Competitor label or C0 from Phase 2]" as first slot. "Findings that could be written without having run Phase 2 fail the grounding test." Named failure mode prevents free-floating prose. |
| C-11 | Inertia propagates downstream | PASS | Architectural consumption declarations: Phase 2 "Consumes: ROOT INERTIA-REF," Phase 3 "Consumes: ROOT INERTIA-REF," Phase 4 "Consumes: ROOT INERTIA-REF," AMEND "Consumes: all phases." Template slot "*INERTIA-REF: [connection to the ROOT mechanism]*" in every finding. Phase 3 gap rationale also explicitly requires confirming ROOT INERTIA-REF. Deepest architectural enforcement of any variation. |
| C-12 | AMEND evaluates inertia stability | PASS | AMEND output contract: "whether the amendment would alter INERTIA-REF or leave it stable." "A silent cell does not satisfy the AMEND output contract." Four populated example rows with phase-level justification. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 4/4**
**Composite: (5/5 x 60) + (3/3 x 30) + (4/4 x 10) = 60 + 30 + 10 = 100**
**Grade: Exceptional**

---

### Composite Scores Summary

| Variation | Essential | Recommended | Aspirational | Composite | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-03 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-04 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-05 | 5/5 | 3/3 | 4/4 | **100** | Exceptional |
| V-02 | 5/5 | 3/3 | 3.5/4 | **98.75** | Exceptional |
| V-01 | 5/5 | 3/3 | 3/4 | **97.5** | Exceptional |

All essential criteria pass across all five variations.

---

### Rank Order

1. **V-03 / V-04 / V-05 (100)** — All three satisfy C-11 and C-12. Tiebreak:
   - **V-05** wins on propagation architecture: `consumes: INERTIA-REF` declarations in Phase 2, Phase 3, Phase 4, and AMEND make the mechanism a live architectural dependency. Phase 3 uniquely requires confirming ROOT INERTIA-REF does not cover the gap -- the only variation to thread inertia through the gap rationale.
   - **V-04** wins on C-11 enforcement reliability: the three-part findings template (`vs INERTIA-REF:` mandatory slot) is structural prevention. The model cannot produce a finding without filling the slot. Also adds a dedicated Source column for citation isolation.
   - **V-03** wins on portability: achieves perfect score in conversational register with no formal syntax. The user-defined MECH label ("give it a short label you'll use for the rest of the analysis") is domain-adaptive. Establishes that structural enforcement is not required for 100-point performance.
   - Enforcement depth rank: V-05 > V-04 > V-03. Adoption ergonomics rank: V-03 > V-04 > V-05.

2. **V-02 (98.75)** — Confirms R2's single-axis hypothesis: the `INERTIA-REF stable?` AMEND column satisfies C-12 without lifecycle scaffolding. Docked on C-11 PARTIAL: "Inertia delta" propagates through the competitor map but the mechanism lacks a formal short label and the findings section has no slot. Propagation is incomplete.

3. **V-01 (97.5)** — Strongest C-11 enforcement of any single-axis variation (mandatory findings template slot). Docked on C-12 FAIL as designed: V-01 targeted exactly the one criterion it set out to address.

---

### Excellence Signals (from V-03/V-04/V-05)

Three patterns distinguish the 100-point variations from the rest:

**1. Named mechanism handle is the prerequisite for C-11 -- format is secondary**
All three top variations give the inertia mechanism a referenceable name before propagation occurs: V-03 uses a model-defined MECH label ("spreadsheet-habit," "CLI-workflow-lock"), V-04 uses a template-defined INERTIA-REF block, V-05 uses a ROOT output declaration. The R1 V-03 failure ("no named reference handle") was the correct diagnosis. What R2 confirms: the named handle works in any register -- conversational, template, or architectural. The label is the operative element, not the formatting around it.

**2. C-12 is achievable without lifecycle scaffolding -- the stability question alone is sufficient**
V-02 demonstrated this in isolation, and V-03 confirmed it in conversational register ("Say whether the amendment would change the MECH or leave it stable"). The `INERTIA-REF stable?` column is a reliable vehicle for C-12 independent of how elaborate the surrounding prompt structure is. Minimum viable C-12 enforcement is a single explicit stability question per AMEND entry.

**3. Conversational register closes both C-11 and C-12 when instructions are maximally explicit**
V-03 achieves 100 with no table syntax, no formal block notation, and no phase headers. The key difference from V-03-R1: (a) "Give this mechanism a short label" + (b) "Use this label in the competitor map and in every finding below. Don't drop it after this section" + (c) "Say whether the amendment would change the MECH or leave it stable." Three direct imperatives, in order. Plain English works when the instruction leaves no ambiguity about what must appear in each section.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named mechanism handle satisfies C-11 in any register -- conversational label (MECH), template block (INERTIA-REF), or architectural ROOT declaration all work; the label is the operative element not the format around it", "AMEND stability column achieves C-12 independently of lifecycle scaffolding -- confirmed by V-02 isolation and V-03 conversational equivalent; minimum viable enforcement is one explicit stability question per AMEND entry", "Conversational register achieves perfect score when three direct imperatives are stated in order: name the mechanism with a label, use that label in every subsequent section, address stability per amendment entry"]}
```
