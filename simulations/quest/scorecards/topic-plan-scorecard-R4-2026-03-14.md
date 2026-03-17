Now I have everything I need. Let me write the full scorecard.

---

# Quest Score — `topic:plan` Round 4

**Rubric**: v4 (C-01–C-20, 150 pts)
**Trace artifact**: placeholder (no execution output — evaluating prompt design compliance)
**Methodology**: Each variation is assessed as a prompt specification. Criterion = PASS if the prompt reliably instructs a model to produce compliant output; PARTIAL if the instruction is present but weaker than the pass condition; FAIL if absent.

---

## Criterion Definitions (Quick Reference)

| Tier | ID | Criterion | Points |
|------|----|-----------|--------|
| Essential | C-01 | Reads strategy.md | 12 |
| Essential | C-02 | Reads signal artifacts | 12 |
| Essential | C-03 | Identifies delta, not inventory | 12 |
| Essential | C-04 | Proposes typed changes | 12 |
| Essential | C-05 | Requires confirmation before writing | 12 |
| Recommended | C-06 | Evidence per change | 10 |
| Recommended | C-07 | Before/after diff | 10 |
| Recommended | C-08 | All three change types | 10 |
| Aspirational | C-09 | Namespace coverage gaps | 5 |
| Aspirational | C-10 | Conflicting signals surfaced | 5 |
| Aspirational | C-11 | Typed confirmation verb | 5 |
| Aspirational | C-12 | Explicit no-change rows | 5 |
| Aspirational | C-13 | Inline evidence in diff | 5 |
| Aspirational | C-14 | Anti-inventory warning at delta step | 5 |
| Aspirational | C-15 | All 9 namespaces enumerated | 5 |
| Aspirational | C-16 | Two-level traceability chain | 5 |
| Aspirational | C-17 | Explicit no-conflicts declaration | 5 |
| Aspirational | C-18 | Structured delta format per finding | 5 |
| Aspirational | C-19 | Diff Proposal ID cross-reference column | 5 |
| Aspirational | C-20 | Delta Finding column in proposals | 5 |

---

## V-01 — Signals-First

**Axis**: Role sequence — signals before strategy

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Step 2 reads strategy.md and extracts all required fields in structured table |
| C-02 | PASS | Step 1 globs and reads all signal artifacts, records key finding per file |
| C-03 | PASS | Step 3: "Anti-pattern warning: A plain inventory of signal files is not the delta." |
| C-04 | PASS | Step 6 proposals table has explicit Type column with ADD/REMOVE/REPRIORITIZE |
| C-05 | PASS | Step 8: "Reply YES to apply all proposals... Waiting." |
| C-06 | PASS | Step 6 proposals table has "Evidence [file(s)]" column per row |
| C-07 | PASS | Step 7 is a dedicated before/after diff table with Namespace/Before/After columns |
| C-08 | PASS | Step 6: "All three types must appear. For empty types, use 'None proposed'..." with example rows |
| C-09 | PASS | Step 4 table enumerates all 9 namespaces with "Stage-Relative Status" column |
| C-10 | PASS | Step 5: opposing signals → name files + state implication for strategy |
| C-11 | PASS | Step 8: "Reply **YES**" — typed token |
| C-12 | PASS | Step 6: "None proposed" rows shown for REMOVE and REPRIORITIZE with "Delta Finding: N/A" |
| C-13 | PASS | Step 7: "Evidence inline: [file.md — key finding in ≤10 words]" explicit format in diff template |
| C-14 | PASS | Step 3 names "plain inventory" as the exact anti-pattern label |
| C-15 | PASS | Step 4 table lists all 9 namespace names explicitly |
| C-16 | PASS | Step 6 has both "Delta Finding" column (Finding ID + full text) and "Evidence" column — two-level chain |
| C-17 | PASS | Step 5: "regardless of whether your format is tabular or inline" — format-agnostic; mandatory null statement |
| C-18 | PASS | Step 3: "Strategy assumed [X] / Signal revealed [Y]" template per row; stop condition present |
| C-19 | PASS | Step 7 diff template has "Proposal" column with "ADD-1" example |
| C-20 | PASS | Step 6: "Every row must include a Delta Finding column... reproduce the full text... Delta Finding: N/A for empty types" |

**Essential**: 5/5 × 60 = 60  
**Recommended**: 3/3 × 30 = 30  
**Aspirational**: 12/12 × 60 = 60  
**Total: 150 / 150**

---

## V-02 — Template-Driven

**Axis**: Output format — template with named mandatory columns

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Phase A reads strategy.md; "fill every cell" template with all required fields |
| C-02 | PASS | Phase B globs all signal artifacts into Signal Inventory template |
| C-03 | PASS | Phase C: "Stop here and name the anti-pattern you are guarding against: A plain inventory of signal files is not the delta." |
| C-04 | PASS | Phase F proposals template has Type column with ADD/REMOVE/REPRIORITIZE |
| C-05 | PASS | Phase H: "Reply YES... Waiting." |
| C-06 | PASS | Phase F Evidence column; Phase G Evidence column in diff |
| C-07 | PASS | Phase G is dedicated Change Diff template with Before/After columns |
| C-08 | PASS | Phase F: all three types required; "Empty types: write 'None proposed'" |
| C-09 | PASS | Phase D template enumerates all 9 namespaces with "Stage-Relative Status" |
| C-10 | PASS | Phase E conflict table with "Implication for strategy" column |
| C-11 | PASS | Phase H: "Reply **YES**" — typed token |
| C-12 | PASS | Phase F: "Empty types: write 'None proposed' in Change; write 'Delta Finding: N/A' in Delta Finding" |
| C-13 | PASS | Phase G: "Evidence: [file.md — finding in ≤10 words] inline per row — no separate evidence section required" |
| C-14 | PASS | Phase C: "plain inventory" named explicitly as the anti-pattern label |
| C-15 | PASS | Phase D template lists all 9 namespace names |
| C-16 | PASS | Phase F: "Delta Finding must reproduce the full 'Strategy assumed [X] / Signal revealed [Y]' text" + Evidence column |
| C-17 | PASS | Phase E: mandatory null row template pre-reproduced for model to copy; "Do not omit this table" |
| C-18 | PASS | Phase C: structured template with Finding ID + "Strategy assumed / Signal revealed" columns; stop condition |
| C-19 | PASS | Phase G diff template: Proposal column declared with "The following columns are mandatory. Do not omit any column." |
| C-20 | PASS | Phase F: "The following columns are mandatory. Do not omit any column." — Delta Finding column pre-declared in template |

**Essential**: 5/5 × 60 = 60  
**Recommended**: 3/3 × 30 = 30  
**Aspirational**: 12/12 × 60 = 60  
**Total: 150 / 150**

**Mechanism distinction**: V-02 is the only variation that uses the header "The following columns are mandatory. Do not omit any column." before both Phase F and Phase G. This unconditional declaration forces column compliance without requiring the model to reason about navigability — it fills blanks in a pre-existing schema. The Phase E null row is also pre-reproduced in the template, replacing judgment ("should I write this?") with a copy instruction.

---

## V-03 — Conversational Register

**Axis**: Phrasing register — first-person narration before tables

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Step 2: "I'll read strategy.md and note everything the strategy explicitly or implicitly assumed" |
| C-02 | PASS | Step 1 globs and reads all artifacts; records key finding |
| C-03 | PASS | Step 3: "I'm guarding against a specific failure mode: **a plain inventory of signal files is not the delta**" (bold) |
| C-04 | PASS | Step 6 proposals table with typed rows; narrated before building |
| C-05 | PASS | Step 8: "Reply **YES**... I will not write anything until you confirm." |
| C-06 | PASS | Step 6 Evidence column; narrated: "Each row will carry... Evidence..." |
| C-07 | PASS | Step 7 is a dedicated before/after diff table |
| C-08 | PASS | Step 6: "All three types must appear. Empty types get a 'None proposed' row" |
| C-09 | PASS | Step 4: "I'll check every namespace — scout, draft, review..." all 9 named in narration + table; "not just counting signals; asking whether this much coverage is right for this stage" |
| C-10 | PASS | Step 5: name files and "say what it means for the strategy" |
| C-11 | PASS | Step 8: "Reply **YES**" |
| C-12 | PASS | Step 6 shows "None proposed" rows with "Delta Finding: N/A" in template |
| C-13 | PASS | Step 7: "Evidence inline: [file.md — key finding in ≤10 words] — no cross-referencing to a separate section" |
| C-14 | PASS | Step 3: "plain inventory" named in bold as the anti-pattern label |
| C-15 | PASS | Step 4 narrates all 9 namespace names explicitly |
| C-16 | PASS | Step 6: "a Delta Finding column: the specific Finding #N... with the full text reproduced — not just the Finding ID" + Evidence column |
| C-17 | PASS | Step 5: "I'll write 'No conflicts detected.' rather than leaving this section blank... This applies whether I'm using a table or inline annotation" — strongest C-17 language of all 5 variations |
| C-18 | PASS | Step 3: "Strategy assumed / Signal revealed" template structure; stop condition present |
| C-19 | PASS | Step 7: "Proposal column: the Proposal ID from Step 6" narrated then shown in template |
| C-20 | PASS | Step 6: narrated "Each row will carry... a Proposal ID... a Delta Finding column..." then table confirms structure |

**Essential**: 5/5 × 60 = 60  
**Recommended**: 3/3 × 30 = 30  
**Aspirational**: 12/12 × 60 = 60  
**Total: 150 / 150**

**Mechanism distinction**: V-03 has the strongest C-17 instruction of any variation — it names the exact text to write ("No conflicts detected."), explains the reasoning, AND explicitly covers both table and inline annotation formats. The first-person narration ("Each row will carry...") creates a self-monitoring channel where the model commits to the structure in prose before the table is built.

---

## V-04 — Hypothesis-First + Unified Table

**Axis**: Role sequence + Output format — pre-reading hypothesis; proposals and diff merged

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Step 3 reads strategy.md and extracts all required fields |
| C-02 | PASS | Step 2 globs and reads all artifacts with hypothesis-confirmation column |
| C-03 | PASS | Step 4: "Anti-pattern check: A plain inventory of signal files is not the delta." |
| C-04 | PASS | Step 6 unified table has Type column with ADD/REMOVE/REPRIORITIZE |
| C-05 | PASS | Step 7: "Reply **YES**... Waiting." |
| C-06 | PASS | Step 6 unified table has Evidence column per row |
| C-07 | PASS | Step 6 unified table has Before and After columns — is the diff; "this IS the diff — the table makes a separate diff section unnecessary" |
| C-08 | PASS | Step 6: all three types required; "None proposed" rows shown with "Delta Finding: N/A" |
| C-09 | PASS | Step 5 namespace table enumerates all 9 with "Stage-Relative Status" |
| C-10 | PASS | Step 5 has dedicated conflict table with "Implication for strategy" column |
| C-11 | PASS | Step 7: "Reply **YES**" |
| C-12 | PASS | Step 6: "All three types must appear; 'None proposed' rows require 'Delta Finding: N/A'" |
| C-13 | PASS | Step 6 unified table: Evidence column is inline per row "[file.md — ≤10 word finding]" — structurally trivial since there is no separate section |
| C-14 | PASS | Step 4: "plain inventory" named as anti-pattern |
| C-15 | PASS | Step 5 namespace table lists all 9 names |
| C-16 | PASS | Step 6 unified table: "Delta Finding: Finding ID + full text from Step 4" + Evidence column — two-level chain on same row |
| C-17 | PASS | Step 5: mandatory null row pre-reproduced: "No conflicts detected — audit ran, none found" |
| C-18 | PASS | Step 4: "Strategy assumed / Signal revealed" template; stop condition present |
| C-19 | PASS | Trivially satisfied: Proposal ID is a column in the unified table; the row IS the proposal — no cross-referencing needed |
| C-20 | PASS | Step 6: "Delta Finding column... mandatory" with full text requirement; "None proposed" rows require "Delta Finding: N/A" |

**Essential**: 5/5 × 60 = 60  
**Recommended**: 3/3 × 30 = 30  
**Aspirational**: 12/12 × 60 = 60  
**Total: 150 / 150**

**Mechanism distinction**: V-04 structurally collapses the C-13/C-19 navigation problem — there is no separate diff section to cross-reference because the unified table IS both the proposal record and the diff. C-13 and C-19 are satisfied not by instruction compliance but by the impossibility of non-compliance. The hypothesis-first step also creates a double-update pattern (hypothesis → signals → strategy → revised hypothesis) that deepens the "Strategy assumed X" anchor for C-20 Delta Finding entries.

---

## V-05 — Inertia-Foregrounded

**Axis**: Lifecycle emphasis + Inertia framing — strategy assumptions explicit before signals

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Step 1 reads strategy.md and reconstructs ALL commitments including unstated assumptions; richest extraction of any variation |
| C-02 | PASS | Step 2 globs and reads all artifacts with "Confirms or challenges which assumption?" column |
| C-03 | PASS | Step 3: "Anti-pattern warning: A plain inventory of signal files is not the delta." |
| C-04 | PASS | Step 6 proposals table has Type column |
| C-05 | PASS | Step 8: "Reply **YES**... Waiting." |
| C-06 | PASS | Step 6 Evidence column |
| C-07 | PASS | Step 7 dedicated before/after diff table |
| C-08 | PASS | Step 6: all three types required; "None proposed" rows with "Delta Finding: N/A" and "If unchanged: N/A" |
| C-09 | PASS | Step 4 has "Expected at this stage?" AND "Status" AND "Gap?" columns — most granular namespace audit |
| C-10 | PASS | Step 5: name conflict and "its implication for strategy" |
| C-11 | PASS | Step 8: "Reply **YES**" |
| C-12 | PASS | Step 6 shows "None proposed" rows with both N/A fields |
| C-13 | PASS | Step 7: "Evidence inline: [file.md — ≤10 word finding] — no cross-referencing needed" |
| C-14 | PASS | Step 3: "plain inventory" named as anti-pattern label |
| C-15 | PASS | Step 4 table lists all 9 namespace names |
| C-16 | PASS | Step 6: Delta Finding column + Evidence column — two-level chain; inertia framing forces causal depth |
| C-17 | PASS | Step 5: "regardless of whether your format is tabular or inline" — format-agnostic; mandatory null statement verbatim |
| C-18 | PASS | Step 3: "Strategy assumed [X] / Signal revealed [Y]" template; stop condition present |
| C-19 | PASS | Step 7 diff template has "Proposal" column |
| C-20 | PASS | Step 6: "Every row must include... Delta Finding" + "If unchanged" column forces causal tracing; "None proposed" rows require both N/A fields |

**Essential**: 5/5 × 60 = 60  
**Recommended**: 3/3 × 30 = 30  
**Aspirational**: 12/12 × 60 = 60  
**Total: 150 / 150**

**Mechanism distinction**: V-05's Step 1 is the richest strategy extraction of any variation — it requires "What it assumed without naming [at least one item]" which makes the "Strategy assumed X" anchor for C-20 Delta Findings naturally non-fabricatable. The "If unchanged: [cost]" column in Step 6 forces the model to have traced the full causal path from assumption → gap → consequence, making Delta Finding entries substantive rather than mechanical label fills.

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (60) | Total |
|-----------|---------------|------------------|-------------------|-------|
| V-01 Signals-First | 60 | 30 | 60 | **150** |
| V-02 Template-Driven | 60 | 30 | 60 | **150** |
| V-03 Conversational | 60 | 30 | 60 | **150** |
| V-04 Hypothesis+Unified | 60 | 30 | 60 | **150** |
| V-05 Inertia-Foregrounded | 60 | 30 | 60 | **150** |

---

## Ranking

All 5 variations achieve full structural coverage of C-01 through C-20. The R4 variation designs specifically targeted the R3 universal gaps (C-13, C-16, C-17, C-19, C-20) and all 5 address them sufficiently. Ranking is by **mechanism strength** for the discriminating criteria:

| Rank | Variation | Differentiator |
|------|-----------|----------------|
| 1 | **V-02 Template-Driven** | "The following columns are mandatory. Do not omit any column." before Phase F and Phase G; pre-reproduced null row in Phase E template — compliance is fill-in-the-blank, not instructed judgment |
| 2 | **V-04 Hypothesis+Unified** | Unified table makes C-13/C-19 structurally impossible to fail — there is no separate diff to forget to annotate |
| 3 | **V-03 Conversational** | Strongest C-17 language (exact text + both formats named); first-person commitment before each table creates self-monitoring channel |
| 4 | **V-01 Signals-First** | Clean format-agnostic C-17; signals-before-strategy ordering sharpens delta detection; solid all-around |
| 5 | **V-05 Inertia-Foregrounded** | Richest Delta Finding depth via inertia framing, but most complex prompt structure; C-20 entries will be most substantive |

---

## Excellence Signals — V-02 (Top Mechanism)

**Signal 1 — Mandatory column declaration header**

"The following columns are mandatory. Do not omit any column." appears as a section header before Phase F (proposals) and Phase G (diff). This single line shifts compliance from *inference* to *instruction*: the model doesn't need to reason about navigability or wonder whether the column is optional. It has been told the column exists and must be filled. This is the cleanest possible enforcement for C-19 and C-20 — no narration, no reasoning, just a schema requirement.

**Signal 2 — Null-row-as-copy-instruction**

Phase E pre-reproduces the exact null row the model should use when no conflicts are found: `| CF-00 | — | — | No conflicts detected | No action needed |`. The instruction says "reproduce this exact row." This replaces the C-17 failure mode (model forgets to declare absence) with a copy operation. The model doesn't decide *whether* to write the null case — it decides only *whether* to add conflict rows above it.

**Signal 3 — "Fill every cell" as universal instruction**

Every phase begins with the output template and a "fill every cell" directive. This creates a uniform schema-filling contract across all 9 phases. V-02 is the only variation where the model never needs to decide whether to produce a table — every section is already a table awaiting content.

---

## Round 4 Meta-Assessment

**Why all 5 score 150**: The R4 variation designs collectively represent a full-round convergence. All R3 universal gaps were explicitly diagnosed, all 5 variations were designed to address them simultaneously via different mechanisms, and the v4 rubric formalized those gaps as new criteria (C-19, C-20). When a round's design axes are precisely targeted at the rubric's open criteria, and the coverage matrix shows all 5 addressing all 5 gap criteria, structural perfection is the expected outcome. The discriminator in actual execution will be model behavior, not prompt design.

**What Round 5 needs**: The 150/150 ceiling reveals that the prompt-design phase is saturated for this skill. Round 5 discriminators should move to *execution fidelity* — run all 5 variations against a real topic with actual signals and score the live outputs. Alternatively, add a C-21 that targets depth of "Strategy assumed X" content (not just presence of the column) — distinguishing V-05's rich inertia anchors from mechanical Finding-ID fills.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["Mandatory-column declaration header ('The following columns are mandatory. Do not omit any column.') before compliance-critical tables shifts C-19/C-20 compliance from instructed judgment to schema fill-in-the-blank — the model fills a pre-existing column rather than deciding whether to create one", "Null-row-as-copy-instruction: pre-reproducing the exact null row the model should write when no conflicts are found replaces the C-17 judgment failure with a copy operation — model decides only whether to add conflict rows above it, not whether to write the null case"]}
```
