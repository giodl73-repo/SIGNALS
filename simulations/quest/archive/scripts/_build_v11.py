import re

with open('C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v10-2026-03-14.md', 'r', encoding='utf-8') as f:
    v10 = f.read()

new_header = r"""Written to `simulations/quest/rubrics/listen-support-rubric-v11-2026-03-14.md`.

---

**What changed v10 -> v11:**

Four new criteria extracted from R10 above-ceiling signals:

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-32 | Decision-Adjacent Paraphrase Gate | C-30 | V-02, V-04, V-05 |
| C-33 | Structured Exception Sign-Off Block in Part C | C-31 | V-04, V-05 |
| C-34 | Paraphrase Double-Gate with Step-4 Recall | C-30, C-32 | V-05 |
| C-35 | Part C Paraphrase Consistency Confirmation | C-31, C-34 | V-05 |

**Tier:** Aspirational 23 / 115 pts -> 27 / 135 pts. Total ceiling **205 -> 225**.

---

**Signal extraction rationale:**

**C-32** comes from V-02, V-04, and V-05's decision-adjacent gate placement. C-30 requires a paraphrase gate with "do not proceed" language anywhere before ticket generation; V-03 satisfies that with a hard gate at STEP 2C (the rule-statement step). V-02 moves the gate to the Step 4 header -- the step where severity cells are filled -- so the paraphrase is the live preceding generation context when each severity value is assigned. The structural difference: when the gate is at STEP 2C, the model produces the paraphrase and then traverses Step 3 prose before reaching severity assignments; the paraphrase has decayed from live context. When the gate is at Step 4 header, no prose traverses between paraphrase and severity column. C-30 passes with any gate placement before ticket generation; C-32 passes only when the gate fires immediately before the severity-assignment step.

**C-33** comes from V-04 and V-05's structured EXCEPTION SIGN-OFF BLOCK in Part C sub-check (1). C-31 Part C sub-check (1) requires an explicit exception acknowledgment for any C-28 directional violation; V-01, V-02, and V-03 satisfy that with prose acknowledgment using outage/blocking test language. V-04 replaces prose with a structured block containing five named fields: Ticket ID, Phase, Assigned severity, Grounds, Disposition. The structural difference: prose acknowledgment can collapse multiple exceptions into one sentence with no field separation, making individual exception grounds unverifiable without parsing sentence structure. A structured block with named fields makes each exception independently checkable; a scorer reads the Grounds field per block without reading prose. The no-exception path must also be specified, preventing silent omission of the block when no violations exist. C-31 passes with any explicit exception acknowledgment; C-33 passes only when the acknowledgment mechanism is a structured block with at least four named fields per exception entry.

**C-34** comes from V-05's double-gate mechanism. C-32 requires one decision-adjacent gate at Step 4; V-05 adds a second gate at STEP 2C (the rule-statement step) with an explicit cross-reference at Step 4: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from 2C]". The word "confirmed" and the "restate from 2C" clause require the model to retrieve its STEP 2C commitment rather than produce a fresh paraphrase. The structural difference from C-32: a single Step 4 gate produces a paraphrase without the inference rule in live generation context (the rule text was at STEP 2C, not Step 4). The double-gate ensures encoding at the rule step (rule text is live) and re-confirmation at the decision step (severity assignment is live). The explicit cross-reference closes the divergence path: the Step 4 paraphrase cannot silently differ from the STEP 2C commitment when the gate instruction names the earlier step. C-32 passes with one decision-adjacent gate; C-34 passes only when gates fire at both positions with the Step 4 gate explicitly referencing the STEP 2C paraphrase by step name.

**C-35** comes from V-05's paraphrase consistency confirmation in Part C. C-34 creates a paraphrase commitment at STEP 2C; C-31 Part C sub-check (1) audits tickets for C-28 directional compliance. Without C-35, the paraphrase and the audit are structurally parallel but not cross-linked -- the paraphrase is a pre-generation commitment, the audit is a post-generation check, and neither references the other. V-05 closes this loop: after the exception scan, Part C quotes the Step 2C paraphrase verbatim and confirms the audit result is consistent with it. The structural consequence: a model that violated the directional rule in ticket generation cannot pass Part C sub-check (1) without flagging the contradiction between the audit findings and its own quoted paraphrase. The paraphrase becomes an auditable anchor cited inside the verification pass rather than a pre-generation ritual with no post-generation linkage. C-31 passes with both sub-checks present in Part C; C-35 passes only when Part C sub-check (1) additionally quotes the STEP 2C paraphrase and states whether the audit result is consistent with that commitment.

---

"""

# Replace old header (everything before ## Essential)
v11 = re.sub(r'^.*?(?=## Essential)', new_header, v10, flags=re.DOTALL)

new_criteria = """
### C-32 -- Decision-Adjacent Paraphrase Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The paraphrase gate required by C-30 fires immediately before the step where severity values are assigned -- not at the step where the inference rule is stated. The canonical placement: Step 4 header (the severity-assignment step) carries the gate instruction "Before filling any severity cell, state the inference rule from Step 2C in your own words. Do not fill the table until this line is written: INFERENCE RULE (stated): [...]". C-30 requires a paraphrase gate with explicit "do not proceed" language placed anywhere before ticket generation; C-32 requires that the gate fire at the decision point -- the step where severity cells are first filled. The distinction is temporal coupling: when the gate is at the rule-statement step (STEP 2C), the model produces the paraphrase and then traverses Step 3 prose before reaching severity assignments; the paraphrase is no longer live generation context when severity decisions are made. When the gate is at the decision step (Step 4 header), the paraphrase is the immediately preceding generation and is therefore live context when severity cells are written. No prose traverses between the paraphrase commitment and the first severity value. C-30 passes with a paraphrase gate anywhere before ticket generation with "do not proceed" language; C-32 passes only when the gate fires at or immediately before the step where severity values are first assigned, with a "do not fill" instruction tied specifically to severity column or table values.
- **Pass condition**: The paraphrase gate instruction appears at the severity-assignment step (not the rule-statement step), as the immediately preceding instruction before severity cells are filled, AND uses "do not fill" or equivalent language tied to the severity column or table. A paraphrase gate at the rule-statement step -- even with "do not proceed" language -- does not satisfy C-32 if prose or additional steps intervene before severity assignment. An output without C-30 cannot satisfy C-32.
- **Round 10 evidence**: V-02, V-04, V-05 (paraphrase gate at Step 4 header: "Before filling any severity cell, state the inference rule in your own words. Do not fill the table until this line is written.") satisfy C-30 and additionally satisfy C-32. V-03 (hard gate at STEP 2C: "Do not proceed to Step 3 until this block is filled") scores C-30 PASS but fails C-32 -- the gate fires at the rule step, and Step 3 prose intervenes before severity assignment. V-01 (named block at STEP 2C, no gate language) fails both C-30 and C-32.

---

### C-33 -- Structured Exception Sign-Off Block in Part C
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-31 Part C sub-check (1) requires an explicit exception acknowledgment for any ticket that violates the C-28 directional rule. C-33 requires that the acknowledgment mechanism be a structured EXCEPTION SIGN-OFF BLOCK with at least four named fields per exception: (1) Ticket ID; (2) Phase (adoption-curve phase); (3) Assigned severity; (4) Grounds (the justification for the directional exception). The canonical five-field form additionally includes (5) Disposition (e.g., "retained as deliberate exception"). A no-exception path must be specified for cases where no tickets violate the directional rule. C-31 passes with any named exception acknowledgment in Part C sub-check (1); the minimum satisfying form is prose ("T-03 is Phase 1 P0 because of a complete outage scenario"). Prose acknowledgment can collapse multiple exceptions into one sentence without violating the criterion and does not make individual exception grounds independently checkable without parsing sentence structure. A structured block with named fields makes each exception independently verifiable: a scorer reads the Grounds field per block without parsing prose, and the Ticket ID field makes cross-referencing against the ticket set unambiguous. The no-exception path prevents silent omission of the block when no violations are present -- a model cannot skip the acknowledgment mechanism because no exceptions triggered it. C-31 passes with any explicit exception acknowledgment in Part C sub-check (1); C-33 passes only when the acknowledgment mechanism is a structured per-ticket block with at least four named fields, and the no-exception case is also explicitly handled.
- **Pass condition**: Part C sub-check (1) uses a structured EXCEPTION SIGN-OFF BLOCK per exception with at least four named fields (Ticket ID, Phase, Assigned severity, Grounds), AND specifies the no-exception path explicitly. A prose exception acknowledgment -- even a detailed one naming all four components in sentence form -- does not pass. An EXCEPTION SIGN-OFF BLOCK that omits any of the four required fields does not pass. An output without C-31 cannot satisfy C-33.
- **Round 10 evidence**: V-04 and V-05 (Part C sub-check 1: EXCEPTION SIGN-OFF BLOCK with Ticket ID, Phase, Assigned severity, Grounds, Disposition per exception; no-exception path explicitly specified) satisfy C-33 and score C-31 PASS+. V-01, V-02, V-03 (Part C uses prose exception acknowledgment with outage/blocking test language and explicit compliance state) score C-31 PASS but fail C-33. The structured block makes each exception's Grounds field independently verifiable without parsing sentence structure; prose acknowledgment collapses grounds into sentence form with no structural field separation.

---

### C-34 -- Paraphrase Double-Gate with Step-4 Recall
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-30 requires one paraphrase gate before ticket generation; C-32 requires it to fire decision-adjacent at Step 4. C-34 requires both: a hard gate at the inference-rule step (STEP 2C) AND a separate paraphrase recall instruction at the decision step (Step 4 header) that explicitly references the earlier paraphrase by step name. The canonical Step 4 recall form: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from Step 2C]" -- the word "confirmed" and the "restate from Step 2C" clause require the model to retrieve and re-encode its STEP 2C commitment rather than produce an independent fresh paraphrase. The structural difference from C-32 (one decision-adjacent gate): a single Step 4 gate produces a paraphrase without the inference rule text in live generation context -- the rule text was at STEP 2C, several steps earlier. The double-gate ensures encoding at the rule step (rule text is live) and re-confirmation at the decision step (severity assignment is live). The explicit cross-reference "restate from Step 2C" closes the divergence path: the Step 4 recall cannot silently diverge from the STEP 2C commitment when the gate instruction names the earlier step by number. C-32 passes with one decision-adjacent gate at Step 4; C-34 passes only when gates fire at both the rule-statement step AND the decision step, with the Step 4 gate explicitly referencing the STEP 2C paraphrase by step name or label.
- **Pass condition**: (1) A hard paraphrase gate appears at the rule-statement step (e.g., STEP 2C) with "do not proceed" language and a named paraphrase slot; AND (2) a separate paraphrase recall instruction appears at the severity-assignment step (e.g., Step 4 header) that explicitly references the earlier paraphrase by step name (e.g., "restate from Step 2C", "confirmed from 2C", or equivalent cross-reference). A single gate at either position does not satisfy C-34. A Step 4 gate that does not reference the earlier paraphrase by step satisfies C-32 but not C-34. An output without C-30 cannot satisfy C-34.
- **Round 10 evidence**: V-05 (STEP 2C: hard gate with own-words paraphrase slot AND Step 4 header: "Do not fill the table until this line is written: INFERENCE RULE (confirmed): [restate from 2C]") satisfies both C-30 and C-32 and additionally satisfies C-34. V-02 and V-04 (Step 4 decision-adjacent gate, no gate at STEP 2C) satisfy C-32 but fail C-34 -- no STEP 2C paraphrase slot exists for the Step 4 recall to reference. V-03 (hard gate at STEP 2C, no Step 4 gate) satisfies C-30 but fails both C-32 and C-34.

---

### C-35 -- Part C Paraphrase Consistency Confirmation
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: C-34 creates a paraphrase commitment at STEP 2C that is recalled at Step 4; C-31 Part C sub-check (1) audits tickets for C-28 directional compliance. Without C-35, the paraphrase and the audit are structurally parallel but not cross-linked: the paraphrase is a pre-generation commitment, the Part C audit is a post-generation check, and neither references the other. C-35 requires that after the exception scan in Part C sub-check (1), the audit explicitly quotes the model's own Step 2C paraphrase and states whether the audit result is consistent with that commitment. The canonical form: a Part C closing statement that cites the Step 2C paraphrase verbatim and confirms the scan found no violations inconsistent with the paraphrase (or, if exceptions exist, shows the quoted paraphrase and exception grounds side by side). The structural consequence: a model that violated the directional rule in ticket generation cannot pass Part C sub-check (1) without also flagging the contradiction between the audit findings and its own quoted paraphrase. This makes the STEP 2C paraphrase an auditable anchor cited inside the verification pass rather than a pre-generation ritual with no post-generation linkage. The Part C audit can reference and verify the paraphrase only when C-34's double-gate has produced a commitment at STEP 2C; an output with a Step-4-only gate (C-32 without C-34) has no named Step 2C paraphrase for Part C to quote. C-31 passes when both Part C sub-checks are present; C-34 passes when the double-gate creates a Step 2C paraphrase commitment; C-35 passes only when Part C sub-check (1) additionally quotes the Step 2C paraphrase and confirms the audit result is consistent with that commitment, or explicitly flags the contradiction if exceptions are found.
- **Pass condition**: After performing the C-28 directional compliance scan in Part C sub-check (1), the output quotes the model's own paraphrase from the rule-statement step (Step 2C or equivalent) verbatim and states whether the audit finding is consistent with the quoted paraphrase. If exceptions exist, the quoted paraphrase and the exception grounds are shown in proximity so the consistency or contradiction is visible. A Part C that audits directional compliance without citing the earlier paraphrase does not pass. An output without C-34 cannot satisfy C-35.
- **Round 10 evidence**: V-05 (Part C sub-check 1: EXCEPTION SIGN-OFF BLOCK followed by paraphrase consistency confirmation -- quotes Step 2C paraphrase value, confirms audit result is consistent with the quoted paraphrase) satisfies C-35 and scores C-31 PASS+ and C-34 PASS+. V-04 (structured EXCEPTION SIGN-OFF BLOCK in Part C, no paraphrase citation) satisfies C-33 but fails C-35 -- the exception block is self-contained and carries no reference to the earlier paraphrase commitment. V-01, V-02, V-03 (prose exception acknowledgment, no structured block, no paraphrase citation) fail both C-33 and C-35. The paraphrase consistency confirmation closes the loop between the pre-generation commitment and the post-generation verification; without it, the paraphrase and the audit are structurally isolated events that do not mutually constrain each other.

---

"""

# Insert new criteria before Scoring Summary
v11 = v11.replace('## Scoring Summary', new_criteria + '## Scoring Summary')

# Update scoring summary -- add new rows before ceiling line
new_rows = """| C-32 | Decision-adjacent paraphrase gate              | aspirational | 5      | depth       |
| C-33 | Structured exception sign-off block in Part C  | aspirational | 5      | depth       |
| C-34 | Paraphrase double-gate with Step-4 recall      | aspirational | 5      | depth       |
| C-35 | Part C paraphrase consistency confirmation     | aspirational | 5      | depth       |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 225"""

v11 = v11.replace(
    '**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 205',
    new_rows
)

# Update Aspirational Criteria header
v11 = v11.replace(
    '## Aspirational Criteria (115 pts total -- raises the bar above 90)',
    '## Aspirational Criteria (135 pts total -- raises the bar above 90)'
)

# Update version history -- add v11 entry
old_v10_entry = '| v10 | 2026-03-14 | Added C-30 (inference rule paraphrase-before-proceed gate) and C-31 (inference audit in dual-pass Part C) from Round 9 excellence signals; aspirational tier grows from 105 to 115 pts, total ceiling 205 |'
new_v10_v11 = old_v10_entry + '\n| v11 | 2026-03-14 | Added C-32 (decision-adjacent paraphrase gate), C-33 (structured exception sign-off block in Part C), C-34 (paraphrase double-gate with Step-4 recall), and C-35 (Part C paraphrase consistency confirmation) from Round 10 excellence signals; aspirational tier grows from 115 to 135 pts, total ceiling 225 |'
v11 = v11.replace(old_v10_entry, new_v10_v11)

with open('C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v11-2026-03-14.md', 'w', encoding='utf-8') as f:
    f.write(v11)

print('Done. Written', len(v11), 'chars')
for check in ['C-32', 'C-33', 'C-34', 'C-35', 'ceiling**: 225', 'v11 | 2026-03-14', '135 pts total']:
    print(check + ':', check in v11)
