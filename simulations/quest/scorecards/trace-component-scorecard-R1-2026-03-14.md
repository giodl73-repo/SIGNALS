## Round 1 Scorecard — trace-component

| Rank | Variation | Essential | Recommended | Aspirational | Score | Result |
|------|-----------|-----------|-------------|--------------|-------|--------|
| 1 | **V-01** Framework-declaration-first | 5/5 PASS | 2.5/3 | 1.5/2 | **92.5** | PASS |
| 2 | **V-04** Gated phases | 5/5 PASS | 2.5/3 | 2/2 | **90** | PASS |
| 2 | **V-05** Inertia + event table | 5/5 PASS | 2.5/3 | 1/2 | **90** | PASS |
| 4 | **V-03** Imperative register | 5/5 PASS | 2.5/3 | 1.5/2 | **87.5** | PASS |
| 5 | **V-02** Pre-printed event table | 5/5 PASS | 2/3 | 1/2 | **85** | PASS |

---

### The two discriminators

**C-07 (Issue Detection):** Only V-05 fully passes — the "What ad-hoc misses" column cannot say N/A. A column must be cleared per row; a FINDINGS section can be cleared once. V-01 through V-04 all carry advisory FINDINGS sections that can be satisfied with a single no-issues claim.

**C-08 (Framework Vocabulary):** Only V-01 fully passes — the FRAMEWORK GATE pre-declares 3–5 terms with definitions, then threads them via explicit instruction ("use vocabulary declared in FRAMEWORK GATE throughout this section"). V-02's post-hoc FRAMEWORK VOCABULARY NOTE detects drift too late.

**C-10 (Render Quantification):** Only V-04 fully passes — count AND verdict appear in the same table row for every component. V-01 has the count column but splits the verdict into a separate subsection. V-02 and V-05 have no count column at all.

### C-07/C-10 tradeoff

No single variation wins both. V-05 wins C-07, drops C-10. V-04 wins C-10, partially covers C-07. The Round 2 synthesis target: carry V-05's mandatory comparison column AND V-04's count+verdict columns in the same table — the table gets wider but both criteria become structurally unavoidable.

### Two new patterns

1. **Inline phase-close anti-patterns** (V-04): Print the failure condition inside the template at the phase boundary (`"'State updates' with no specifics does not close this phase"`). The rubric is external; the template is in the model's context at output time. Generalizable to any sequential trace skill.

2. **Mandatory comparison column** (V-05): A column that cannot say N/A forces per-row analysis. The only valid escape ("Nothing — this is the exception") is itself a substantive claim. A section can be satisfied once; a column must be satisfied per row.

```json
{"top_score": 93, "all_essential_pass": true, "new_patterns": ["Inline phase-close anti-patterns — print the fail condition inside the template at the phase boundary, not in external rubric instructions", "Mandatory comparison column — a column that cannot say N/A forces per-row comparative analysis; a section can be cleared once but a column must be cleared per row"]}
```
oes not close this phase." Gate enforced at phase boundary. |
| V-05 | **PASS** | "Component path" column with direction. Same enforcement as V-02. |

---

### C-03 · State Update Map (essential, 12 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | STATE MUTATION MAP: owner / key / old shape / new shape / mechanism per mutation. "Minimum one concrete mutation required. If no mutation: explicit justification. Do not leave this section empty." |
| V-02 | **PASS** | "State mutation" column: "Name the state key, its owner, and the old→new value shape for any mutation. If no mutation: 'None — [reason].'" No-mutation silence rejected. |
| V-03 | **PASS** | Step 3: "For every state change, write: '[ComponentName] mutates [stateKey]: [oldShape] → [newShape].' If no mutation: 'No mutation — Reason: [why].' Do not leave this step blank." |
| V-04 | **PASS** | PHASE 3: owner / key / old / new / mechanism / timing per mutation. PHASE 3 CLOSE: "'State updates' with no specifics does not close this phase." Close condition names the exact failure mode. |
| V-05 | **PASS** | "State mutation" column: "Name key, owner, old→new shape. 'None — [reason]' if no mutation." Same table enforcement. |

---

### C-04 · Re-render Inventory (essential, 12 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | RE-RENDER INVENTORY table: Component / Re-render cause / Render count per action. Plus "Unnecessary re-renders" subsection. "Minimum one row required." |
| V-02 | **PASS** | "Re-renders" column: "Name each component that re-renders because of this event and why. 'Several components' without names does not pass." |
| V-03 | **PASS** | Step 4: "For each component, write: '[ComponentName] re-renders because [...].' Do not write 'several components re-render' without naming them." |
| V-04 | **PASS** | PHASE 4 table: Component / Why it re-renders / Renders per action / Verdict. PHASE 4 CLOSE: "'Several components re-render' does not close this phase." Verdict column forces justified/unnecessary classification. |
| V-05 | **PASS** | "Re-renders" column: "Name each re-rendering component and why. 'None — [reason]' if none." Table enforcement. |

---

### C-05 · Final UI State (essential, 12 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | FINAL UI STATE: "Synchronous final state" + "Post-async final state." Explicitly: "'UI updates accordingly' does not satisfy this section." |
| V-02 | **PASS** | "UI change" column per event row covers synchronous state. POST-ASYNC STATE section covers async settle with both success and error paths. |
| V-03 | **PASS** | Step 6: "State the final UI after all synchronous effects. Name elements that are now visible, hidden, disabled, or updated. 'UI updates accordingly' does not satisfy this step." Anti-pattern named inline. |
| V-04 | **PASS** | PHASE 5: "Synchronous:" + "Post-async: success / error." PHASE 5 CLOSE: "'UI updates accordingly' does not close this phase." Gate rejects the exact failure mode. |
| V-05 | **PASS** | "UI change" column + POST-ASYNC STATE with "What ad-hoc DevTools would NOT show for success" extending the analysis beyond bare state description. |

---

### C-06 · Side Effect Coverage (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | SIDE EFFECTS table: Effect / Mechanism / Trigger condition. "If none: write a single row: 'No side effects | N/A | Confirmed...'" — silence is structurally rejected by table format. |
| V-02 | **PASS** | "Side effects" column: "Name any API call, timer, navigation, or storage write. Include mechanism. If none: 'None — confirmed.'" No-effect silence rejected. |
| V-03 | **PASS** | Step 5: "For each side effect, write: '[Type]: [detail] via [mechanism].' If no side effects: 'No side effects — confirmed: this action is synchronous with no subscriptions, API calls, or storage writes.'" |
| V-04 | **PASS** | PHASE 5 side effects section: Effect / Detail / Mechanism. "If no side effects: 'No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation.'" |
| V-05 | **PASS** | "Side effects" column: "API call, timer, navigation, or storage write with mechanism. 'None — confirmed' if none." Plus POST-ASYNC STATE extends coverage to the async settle. |

---

### C-07 · Issue Detection (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PARTIAL** | FINDINGS section with canonical issue types listed. Strong guidance but no structural forcing — "No issues detected" with a specific justification satisfies the section. Score: 5 pts. |
| V-02 | **PARTIAL** | ISSUES section with canonical types and "minimal fix per issue." Same advisory structure as V-01 — no structural forcing. Score: 5 pts. |
| V-03 | **PARTIAL** | Step 7: "Look at the complete trace above. Check for: [4 specific types]." Stronger imperative phrasing than V-01/V-02 but still advisory — "No issues detected" with specific per-check reasoning satisfies it. Score: 5 pts. |
| V-04 | **PARTIAL** | FINDINGS reviews five closed phases systematically with per-finding format (Severity / Location / Problem / Fix). Phase-referenced findings are more grounded than generic FINDINGS, but the section is still post-hoc advisory. Score: 5 pts. |
| V-05 | **PASS** | "What ad-hoc misses" column CANNOT be "N/A." The only escape: "Nothing — this row is fully observable in DevTools via [specific tab]. Note: this is the exception, not the rule." Per-row forcing mechanism — blank cells visible, N/A explicitly disallowed. FINDINGS consolidates from this column, so every finding has a row citation. Score: 10 pts. |

**C-07 discriminator:** V-05 is the only variation where issue detection is structurally unavoidable. The column mechanism makes a single no-issues claim insufficient — the model must clear the criterion per row, not once for the whole output.

---

### C-08 · Framework Vocabulary (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | FRAMEWORK GATE requires 3–5 terms declared with definitions before any trace begins. EVENT CHAIN instruction: "Use the framework vocabulary declared in the FRAMEWORK GATE throughout this section." Pre-declaration + threading mandate is the strongest C-08 mechanism of all variations. Score: 10 pts. |
| V-02 | **PARTIAL** | Framework declared (name + state management) but no vocabulary list required. FRAMEWORK VOCABULARY NOTE at end asks to verify 2+ terms in the table — post-hoc verification, not pre-declaration. Score: 5 pts. |
| V-03 | **PARTIAL** | Framework declared (2 fields before Step 1). No vocabulary list, no threading requirement. Terms may appear organically but are not mandated. Score: 5 pts. |
| V-04 | **PARTIAL** | PHASE 0 declares framework + state management + role. Role selection adds expert identity but no vocabulary list or threading mandate. Score: 5 pts. |
| V-05 | **PARTIAL** | Framework declared in SETUP (2 fields). No vocabulary list or threading requirement. INERTIA section names DevTools limitations which may surface framework-specific terms organically but does not mandate them. Score: 5 pts. |

**C-08 discriminator:** V-01 uniquely separates on C-08. The pre-declaration gate + threading instruction is the only mechanism that guarantees framework vocabulary appears consistently throughout the trace body, not just at declaration time.

---

### C-09 · Fix Recommendations (aspirational, 5 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | AMENDMENTS: "provide one concrete, minimal fix per finding. Name the specific API, hook, memoization boundary, or ARIA attribute. Do not give general advice." |
| V-02 | **PASS** | ISSUES: "provide a minimal fix (specific hook, attribute, or pattern)" per issue. |
| V-03 | **PASS** | Step 7: "give the minimal fix (name a specific hook, attribute, or boundary)" per problem. |
| V-04 | **PASS** | FINDINGS Fix field: "One concrete, minimal fix — specific hook, attribute, or boundary. Not general advice." Plus AMEND section for P1/P2 findings that warrant re-trace. |
| V-05 | **PASS** | FINDINGS Fix field: "Minimal, concrete — name a specific hook, attribute, or boundary." Plus "Do-nothing cost" field ties each fix to the production consequence. |

C-09 passes uniformly. All five variations carry a fix-per-finding instruction with "specific hook/attribute" language.

---

### C-10 · Render Quantification (aspirational, 5 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PARTIAL** | RE-RENDER INVENTORY table has "Render count per action" column (values: "1 / N / 'once per keystroke'"). Verdict is split: count in table row, verdict implicit (not in "Unnecessary re-renders" subsection = justified). Count + split verdict covers C-10 partially. Score: 2.5 pts. |
| V-02 | **FAIL** | "Re-renders" column names components and causes but no count column and no rate annotation required. Score: 0 pts. |
| V-03 | **PARTIAL** | Step 4: "Include the render count if it re-renders more than once per action." Count only required for components with >1 render — single-render components have no annotation requirement. Partial coverage. Score: 2.5 pts. |
| V-04 | **PASS** | PHASE 4 table: "Renders per action" column AND "Verdict" column (justified / unnecessary) in the same row for every component. "Unnecessary re-renders" section requires a fix for each "unnecessary" verdict. Count + in-row verdict is the most complete C-10 structure. Score: 5 pts. |
| V-05 | **FAIL** | "Re-renders" column names components and causes but no count or rate column. "What ad-hoc misses" column may surface render observations organically but no quantification structure is required. Score: 0 pts. |

---

## Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event Anchor | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-02 Tree Traversal | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-03 State Update Map | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-04 Re-render Inventory | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-05 Final UI State | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-06 Side Effects | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 Issue Detection | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | **PASS 10** |
| C-08 Framework Vocab | **PASS 10** | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 |
| C-09 Fix Recs | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-10 Render Quant | PARTIAL 2.5 | FAIL 0 | PARTIAL 2.5 | **PASS 5** | FAIL 0 |
| **Total** | **92.5** | **85** | **87.5** | **90** | **90** |
| All essential pass | YES | YES | YES | YES | YES |
| Result | PASS | PASS | PASS | PASS | PASS |

---

## Ranking

1. **V-01** (92.5) — Wins on C-08 (pre-declared vocabulary with threading mandate) and partially covers C-10. Only variation where framework terms are both committed upfront and required throughout the trace body.
2. **V-04** (90) — Wins on C-10 (render count + verdict in the same table row per component). Phase-close anti-patterns printed inline are the strongest collapse-prevention mechanism of any variation.
2. **V-05** (90) — Wins on C-07 (mandatory "What ad-hoc misses" column, cannot be N/A). Per-row forcing is the strongest issue detection mechanism of any variation.
4. **V-03** (87.5) — Partial C-10 (conditional count only) and partial C-08. Demonstrates all 5 essential criteria pass with imperative commands and no structural scaffolding — a clean floor measurement.
5. **V-02** (85) — Weakest on C-10 (no count column) and C-08 (post-hoc vocabulary verification only). Table format reliably guarantees essential criteria but does not extend to depth criteria.

---

## Excellence Signals from V-01

**Signal 1 — Vocabulary pre-commitment gates downstream output quality.**
V-01's FRAMEWORK GATE forces the model to declare 3–5 framework-specific terms with definitions before writing any trace content. The gate output becomes a self-referential constraint via "Use the framework vocabulary declared in the FRAMEWORK GATE throughout this section." This prevents vocabulary drift mid-trace and is the only mechanism that guarantees framework-specific language appears in all five essential trace sections rather than just the framework declaration field.

**Signal 2 — Pre-declaration is stronger than post-hoc verification.**
V-02's FRAMEWORK VOCABULARY NOTE asks the model to verify at the end whether 2+ framework terms appeared in the table. This is weaker because (a) the verification can be satisfied by retrofitting terms to the table rather than integrating them from the start, and (b) it does not prevent the trace body from being framework-agnostic until the verification step. V-01's gate prevents the problem; V-02's note detects it too late.

**Signal 3 — Two independent criteria compete for the C-07/C-10 tradeoff.**
No single variation wins both C-07 and C-10. V-05 wins C-07 (inertia column forces issue detection per row) but drops C-10 (no render count column). V-04 wins C-10 (verdict + count in same row) but only partially covers C-07. The Round 2 synthesis target is a combined variation that carries both the inertia column (C-07) and the count+verdict columns (C-10) — the table width increases but both criteria become structurally unavoidable.

---

## New Patterns

**Pattern 1 — Inline phase-close anti-patterns (V-04).**
Print the failure condition inside the template at the phase boundary, not only in the external rubric. "'State updates' with no specifics does not close this phase" written in PHASE 3 CLOSE gives the model a self-referential pass condition at the moment of writing. The rubric is external metadata; the template is in the model's context at output time. Generalizable: any criterion where a common failure mode exists should print the anti-pattern description at the structural boundary where that failure would occur.

**Pattern 2 — Mandatory comparison column (V-05).**
A column that cannot say N/A forces comparative analysis at per-row granularity rather than as a standalone framing section. A FINDINGS section can be satisfied with a single "no issues detected" claim. A mandatory column must be satisfied per row — and the only valid escape ("Nothing — this is the exception") is itself a substantive claim requiring justification. Generalizable: any criterion where the issue may be absent from individual rows but should not be absent from the full output benefits from a per-row column mechanism rather than a per-artifact section.
