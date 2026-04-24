**rhythm-behavior R11 scored.** Scorecard written to `simulations/quest/scorecards/rhythm-behavior-scorecard-R11-2026-03-17.md`.

---

### Results

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 24/24 | **100** | YES |
| V-02 | 4/4 | 3/3 | 24/24 | **100** | YES |
| V-03 | 4/4 | 3/3 | 24/24 | **100** | YES |
| V-04 | 4/4 | 3/3 | 24/24 | **100** | YES |
| V-05 | 4/4 | 3/3 | 24/24 | **100** | YES |

**5/5 golden** -- all predictions confirmed.

---

### Open Questions Resolved

| Question | V | Result |
|----------|---|--------|
| Does C-31 extend to flow-lifecycle body? | V-02 | YES |
| Does C-31 extend to trace-permissions body? | V-03 | YES |
| Dual section-body placement composes cleanly? | V-04 | YES -- second body inert |
| Phrasing register irrelevant to all 24 criteria? | V-05 | YES |

---

### New Patterns

1. **C-31 fully closed.** All named section bodies now confirmed: positions 1 (flow-lifecycle, V-02), 3 (trace-state, R10 V-04), 5 (trace-permissions, V-03), and Synthesis (R9 V-04). No exception exists. The disqualifier set remains strictly gate body and example block.

2. **Dual body composition is clean.** Two qualifying section-body placements in one prompt satisfy C-22 at the first occurrence; the second is redundant but inert. Consistent with all prior dual-placement forms (R8 V-05, R10 V-04).

3. **Register invariance confirmed.** Descriptive/explanatory register throughout -- with all structural requirements preserved -- scores identically to imperative register across all 24 criteria. Criteria are structure-sensitive, not register-sensitive.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-31 confirmed at both extremes -- flow-lifecycle body (position 1) and trace-permissions body (position 5) both qualify; C-31 claim closed across all named section bodies with no exceptions", "Dual named section-body placement composes cleanly -- C-22 satisfied at first occurrence, second is redundant and inert; consistent with dual inter-section slot pattern from R8", "Phrasing register is orthogonal to all 24 aspirational criteria -- descriptive register preserving structural requirements scores identically to imperative form; criteria are structure-sensitive not register-sensitive"]}
```
n
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-31 confirmed at both extremes of the sub-skill sequence -- flow-lifecycle body (position 1, earliest, V-02) and trace-permissions body (position 5, last pre-Synthesis, V-03) both qualify; together with trace-state (R10 V-04) and Synthesis (R9 V-04), C-31's 'all named section bodies' claim is closed across the full sub-skill span with no exceptions", "Dual named section-body placement composes cleanly -- two qualifying body positions in the same prompt satisfy C-22 at the first occurrence; the second is redundant and inert; no criterion penalizes multiple qualifying placements; dual-body configuration is structurally distinct from dual inter-section slots (R8 V-05) and single body (R10 V-04)", "Phrasing register is orthogonal to all 24 aspirational criteria -- descriptive/explanatory register that preserves all structural requirements scores identically to imperative register; criteria are structure-sensitive, not register-sensitive; axis-named repair verbs satisfy C-20 in either register provided the axis target is named explicitly"]}
```

---

### Per-Criterion Verdicts

#### Essential Criteria

**C-01 -- Declared Execution Sequence**
All five: section order "flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings" declared before any findings. V-05 uses declarative phrasing ("The report proceeds through these sections in sequence: ...") which is order-complete and pre-findings. All PASS.

**C-02 -- Single Unified Report**
V-01 through V-04: "Write everything as one document from start to finish. Do not promise to continue." V-05: "The entire report is produced as one document from start to finish, without any promise of continuation." All PASS.

**C-03 -- Blast Radius Ranking Present**
All five: sort label `"Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"` structurally adjacent to the sorted table in Consolidated Findings. All PASS.

**C-04 -- Spec Gap and Contract Violation Coverage**
All five define spec-gap and contract-violation in "What to look for." Coverage Axis Gate checks for both and fires a correction loop if either is absent. All PASS.

---

#### Recommended Criteria

**C-05 -- Per-Finding Sub-Skill Attribution**
All five: table pre-opened with Sub-Skill column; each sub-skill section instructs "(Sub-Skill = flow-lifecycle, classify, assign blast radius)" etc. at discovery time. V-05 uses equivalent descriptive phrasing "(Sub-Skill = flow-lifecycle, finding type classified, blast radius assigned)". All PASS.

**C-06 -- Actionable Next Step for Top Finding**
V-01 through V-04: "Top finding: one concrete next step naming the exact spec section, boundary, or component a developer must address before writing implementation code." V-05: "Top finding: a concrete next step naming the exact spec section, boundary, or component a developer must address before writing any implementation code." Both name the axis target; neither is generic. All PASS.

**C-07 -- Sub-Skill Section Completeness**
All five: each section ends with an explicit null-result instruction ("If a phase has no findings, say so briefly." or "If none: say so explicitly." or equivalent descriptive form in V-05). All PASS.

---

#### Aspirational Criteria

**C-08 -- Blast Radius Justification**
All five: Blast Radius Rationale column pre-declared in the findings table; "Blast Radius Rationale is required for every row" (V-01 through V-04) or column header makes it structurally visible (V-05). All PASS.

**C-09 -- Cross-Sub-Skill Synthesis**
All five: SYNTHESIS section with CROSS-SKILL label; "Add to findings table with Sub-Skill = CROSS-SKILL"; coverage summary includes CROSS-SKILL row. All PASS.

**C-10 -- Self-Documenting Ranking Label**
All five: `Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"` adjacent to sorted table. All PASS.

**C-11 -- Active Coverage Confirmation**
All five: Coverage Axis Gate checks for spec-gap AND contract-violation; fires "add one before Format Axis Gate" (or descriptive equivalent in V-05: "add the missing finding before proceeding to the Format Axis Gate"). All PASS.

**C-12 -- At-Discovery Attribution**
All five: table opened before flow-lifecycle begins; each sub-skill section instructs appending rows as findings are discovered. All PASS.

**C-13 -- Dedicated Synthesis Step**
All five: SYNTHESIS section structurally isolated between trace-permissions and Consolidated Findings by `---` dividers. Not embedded in a sub-skill section or appended to the report end. All PASS.

**C-14 -- Rationale Column Enforcement**
All five: table definition includes Blast Radius Rationale column before flow-lifecycle runs; empty cell would be structurally visible as omission. All PASS.

**C-15 -- CROSS-SKILL Findings as First-Class Table Citizens**
All five: SYNTHESIS instructs insertion into findings table with Sub-Skill = CROSS-SKILL; coverage summary carries CROSS-SKILL row. All PASS.

**C-16 -- 3-Slot Rationale Format**
All five: template string `[LEVEL] because [boundary] propagates to [caller/component], [effect]` present; inline example "WIDE because session-sequence-number contract propagates to flow-conversation routing and trace-contract pre-check, producing stale-state errors at both." present; Format Axis Gate enforces 3-slot format as Gate 2. Both load-bearing elements (C-27/C-28) present. All PASS.

**C-17 -- CROSS-SKILL Blast Radius Inheritance Rule**
All five: SYNTHESIS declares "CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted"; requires "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" provenance; Inheritance Axis Gate enforces with independent correction loop. All PASS.

**C-18 -- Closing Confirmation Multi-Gate Enforcement**
All five: exactly three gates -- Coverage Axis Gate, Format Axis Gate, Inheritance Axis Gate -- each with an independent correction loop. V-05 uses descriptive correction language but preserves independence of loops. All PASS.

**C-19 -- One-Axis-Per-Gate Rule**
All five: each gate covers one axis (coverage / format / inheritance). Three gates, one axis each. No compound gate. All PASS.

**C-20 -- Axis-Named Repair Verb**
- V-01 through V-04: Coverage = "**add** one before Format Axis Gate" (coverage axis); Format = "**rewrite** those cells before Inheritance Axis Gate" (format axis); Inheritance = "**fix** blast radius and annotation before closing" (inheritance axis). All axis-specific.
- V-05: Coverage = "add the missing finding before proceeding to the Format Axis Gate"; Format = "rewritten using the [LEVEL] / [boundary] / [caller/component] / [effect] structure before proceeding to the Inheritance Axis Gate"; Inheritance = "has its CROSS-SKILL blast radius and provenance annotation corrected before closing". All name the axis target explicitly. PASS.

**C-21 -- Axis-Labeled Gate Header Encoding**
All five: "**Coverage Axis Gate**", "**Format Axis Gate**", "**Inheritance Axis Gate**" -- axis label appears in the header token itself, not only in the body. All PASS.

**C-22 -- Explicit Axis-Header Preamble Rule**
- V-01: `**Axis-Header Rule**: Each gate header names its axis.` in its own inter-section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers. Confirmed qualifying position. PASS.
- V-02: Same labeled sentence at the end of the flow-lifecycle section body, after the null-result instruction ("If a phase has no findings, say so briefly."), before the closing `---`. Named section body placement. Per C-26 (non-disqualifying) and C-31 (extends to all named section bodies), this position qualifies. Disqualifiers (gate body, example block) not met. PASS.
- V-03: Same labeled sentence at the end of the trace-permissions section body, after "If none: say so explicitly.", before the closing `---`. Structurally identical to the trace-state body confirmed in R10 V-04 and the Synthesis body confirmed in R9 V-04. Per C-31, all named section bodies qualify. PASS.
- V-04: Same labeled sentence in TWO section bodies (flow-lifecycle and trace-state). C-22 is satisfied at the first qualifying occurrence (flow-lifecycle body); the second (trace-state body) is redundant but inert. No criterion penalizes dual qualifying placements. PASS.
- V-05: `**Axis-Header Rule**: Each gate header names its axis.` in the inter-section peer slot between Synthesis and Consolidated Findings (identical placement to V-01). PASS.

**C-23 -- Axis-Header Rule Isolation Primacy**
All five: the deciding factor is physical isolation from gate bodies and example blocks, not label presence. All five use the bold-labeled form in isolated positions (V-02 through V-04 in section bodies, which qualify under C-26/C-31; V-01 and V-05 in the inter-section slot). No position is disqualifying. All PASS.

**C-24 -- Axis-Header Rule Placement Invariance**
- V-01, V-05: inter-section peer slot (confirmed position in C-24's enumeration). PASS.
- V-02: flow-lifecycle body -- not in C-24's four-position confirmed list, but C-25 applies: the list is illustrative; "any non-buried position" is operative. C-30 further confirms the full span includes positions as early as the flow-lifecycle/flow-conversation boundary. No proximity floor. PASS.
- V-03: trace-permissions body -- covered by C-25's "any non-buried position." PASS.
- V-04: two section bodies -- both covered by C-25. PASS.

**C-25 -- C-24 Confirmed-Position List Is Illustrative**
- V-01, V-05: rule in confirmed inter-section position; C-25 trivially PASS.
- V-02: flow-lifecycle body is not in C-24's four enumerated positions. C-25 governs: scorer must not deny C-22 credit solely because the position is not among the four named examples. "Any non-buried position" is operative; flow-lifecycle body is not buried (not inside a gate body, not inlined in an example block). PASS.
- V-03: trace-permissions body similarly outside the four-position list. PASS.
- V-04: both bodies outside the list. PASS.

**C-26 -- Named Section Bodies Are Non-Disqualifying**
- V-01, V-05: rule NOT in a section body; C-26 trivially PASS.
- V-02: rule in flow-lifecycle body. C-26 specifies named section bodies are not disqualifying; disqualifier set is strictly gate body and example block. Flow-lifecycle body is neither. PASS.
- V-03: rule in trace-permissions body. Same reasoning. PASS.
- V-04: rules in flow-lifecycle and trace-state bodies. Both qualify. PASS.

**C-27 -- 3-Slot Template Load-Bearing Elements**
All five: template string and inline example both present; slot-name definition lines absent (decorative per C-27). Scorer must not withhold C-16 credit for missing definition lines when template + example are both present. All PASS.

**C-28 -- Inline Example Is Load-Bearing for C-16**
All five: inline example IS present. C-28's fail condition fires when a scorer wrongly awards C-16 credit to a prompt lacking the example. All five have the example; no such error is possible. Trivial PASS for all.

**C-29 -- C-27 Scope: Missing Example Is Not Shielded**
All five: inline example IS present. C-29's fail condition fires when C-27 is invoked to shield a genuinely missing example from C-16 failure. Since the example is present, C-27 correctly applies and C-29 is not triggered. Trivial PASS for all.

**C-30 -- C-25 Position Invariance Confirmed Across Full Prompt Span**
- V-01, V-05: rule in late inter-section slot (well within confirmed invariant range). PASS.
- V-02: rule at end of flow-lifecycle body -- at the flow-lifecycle/flow-conversation boundary, which C-30 explicitly confirms as the earliest qualifying position. No proximity floor to gate blocks exists. PASS.
- V-03: trace-permissions body is within the invariant range (later than flow-lifecycle, earlier than the Synthesis/Consolidated boundary). PASS.
- V-04: both bodies within the invariant range. PASS.

**C-31 -- C-26 Named Section Bodies Are Fully Illustrative**
- V-01, V-05: rule NOT in any section body; C-31 trivially PASS.
- V-02: rule in flow-lifecycle body (position 1, earliest sub-skill section). C-31 says C-26's "e.g." is genuinely illustrative and C-26 extends to ALL named section bodies, not only Synthesis. Scorer must not restrict C-26 to previously named bodies. Flow-lifecycle body qualifies. PASS.
- V-03: rule in trace-permissions body (position 5, last sub-skill section before Synthesis). C-31 extends to all named section bodies; trace-permissions body qualifies. PASS.
- V-04: rules in flow-lifecycle and trace-state bodies (positions 1 and 3). Both qualify under C-31. PASS.

---

### Composite Score Summary

| Variation | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 | C-25 | C-26 | C-27 | C-28 | C-29 | C-30 | C-31 | Score |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **100** |

---

### Open Questions Resolved

| Question | V | Result |
|----------|---|--------|
| Does C-31 extend to flow-lifecycle body (earliest sub-skill section)? | V-02 | YES -- confirmed |
| Does C-31 extend to trace-permissions body (last sub-skill section before Synthesis)? | V-03 | YES -- confirmed |
| Do two section-body placements compose cleanly (dual body, no inter-section slot)? | V-04 | YES -- second body redundant, inert |
| Is phrasing register (descriptive vs. imperative) irrelevant to all 24 criteria? | V-05 | YES -- fully register-invariant |

---

### Excellence Signals

**From V-02 + V-03 (C-31 bracket closure)**
C-31's "all named section bodies" claim is now fully bracketed:
- Position 1: flow-lifecycle body (V-02, this round)
- Position 3: trace-state body (R10 V-04)
- Position 5: trace-permissions body (V-03, this round)
- Synthesis body (R9 V-04)

No named section body has failed. The disqualifier set remains strictly: gate body and example block.

**From V-04 (dual body composition)**
Multiple qualifying rule placements in the same prompt compose without interference. The pattern is consistent across all dual-placement forms tested: two inter-section slots (R8 V-05), one section body (R10 V-04), two section bodies (R11 V-04). C-22 is satisfied at the first qualifying occurrence; subsequent qualifying occurrences are redundant but inert.

**From V-05 (register invariance)**
All 24 aspirational criteria are register-invariant. A prompt written entirely in descriptive/explanatory register that preserves all structural requirements scores identically to the canonical imperative form. Axis-named repair verbs satisfy C-20 in either register. The structural requirements are more expensive to verify by reading in descriptive form, since imperative register encodes requirements more concisely -- but scoring is unaffected.

---

### Design Notes for R12

1. **C-31 fully closed.** All five named section bodies confirmed across two rounds (R9-R11). No further C-31 extension probes needed.

2. **Register invariance established.** V-05 confirms descriptive register is inert to all 24 criteria. Mixed-register variations would yield no new information.

3. **Candidate new axes for R12**: (a) gate count stress-test -- fewer than three gates (omit one axis gate) or redundant fourth gate; targets C-18 and C-19; (b) CROSS-SKILL provenance omission -- targets C-17; (c) table pre-opening delay (table opened after first sub-skill section) -- targets C-12 and C-14; (d) null-result omission in one section -- targets C-07; (e) dual-column format axis (rationale + non-rationale column) -- targets C-08 and C-14 interaction.

4. **R11 V-01 is the confirmed production baseline at 24/24.** Golden. Inter-section peer slot placement, minimal form, no slot-name defs, inline example retained. Stable across v10 and v11 rubric expansion.
