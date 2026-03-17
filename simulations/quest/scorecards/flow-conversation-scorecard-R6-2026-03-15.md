## flow-conversation — Round 6 Scoring (Rubric v6)

**Rubric:** C-01–C-16, 135 pts max
**Variations:** V-01 through V-05

---

### Per-Criterion Scoring

#### V-01 — C-15 Only (No Register, No Foils)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Phase 3 turn-by-turn table with named topic node, user utterance, agent response, terminal state required |
| C-02 Defect report present | PASS | Phase 5 defect scan: all four types, Found/Not found verdict, specific location per row |
| C-03 Intent-response pairing | PASS | Both Trigger Phrase/User Utterance and Agent Response columns required in every turn; blank Response is named prohibited pattern |
| C-04 Fallback handling shown | PASS | Phase 4 exception path must diverge at named node; Phase 5 missing-fallback verdict required |
| C-05 Session state tracked | PASS | "Session Variable Delta" column in trace tables; row 1 shows `var = value` pattern |
| C-06 Multi-path coverage | PASS | Phase 3 (happy) + Phase 4 (exception, must reach different terminal or traverse different nodes) |
| C-07 Topic graph completeness | PASS | Phase 2 inventory table per node; Phase 5 coverage table requires every Phase 2 node as a row |
| C-08 CS vocabulary | PASS | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate, End of Conversation), redirect nodes, entities, condition branches — well over 5 CS terms in context |
| C-09 Actionable remediation | PASS | Phase 5 remediation table: "Exact Change Required" + "Copilot Studio Object to Edit"; "MAY NOT write 'Add better error handling'" exits the phase |
| C-10 Named failure prohibition | PASS | Phase 3: "MAY NOT write 'Agent responds appropriately'"; Phase 1: "MAY NOT write 'Possible issues may exist throughout'" — specific plausible outputs named and banned |
| C-11 Structural CS-vocab enforcement | PASS | Column headers: "Topic Node (Copilot Studio)", "Redirect Target / System Topic", "Copilot Studio Object to Edit" — CS terms as headers, not generic labels |
| C-12 Phase exit conditions | PASS | All five phases carry labeled exit conditions naming specific blocked failures: active-node terminal, blank agent response, same-sequence exception path, combined no-issues statement, missing coverage row |
| C-13 Pre-instruction register | FAIL | No criteria table placed before role priming; first instruction is the role sentence |
| C-14 Per-section foil | FAIL | No phase-opening bad-form examples; prohibitions appear only in exit conditions |
| C-15 Pre-trace hypothesis | PASS | Phase 1 commits all four defect types to specific predicted candidate nodes before Phase 2 inventory and Phases 3–4 trace; Phase 5 hypothesis verdict table reconciles each with Confirmed/Refuted/Inconclusive + evidence cite |
| C-16 Cross-mechanism convergence | FAIL | C-13 absent; three-structure requirement cannot fire |

**Score: 120/135** — Essential 60, Recommended 30, Aspirational 30 (C-08 C-09 C-10 C-11 C-12 C-15)
*Matches prediction.*

---

#### V-02 — C-15 + C-13 (Hypothesis + Register, No Foils)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Same phase structure as V-01; Phase 3 trace intact |
| C-02 | PASS | Phase 5 defect scan unchanged |
| C-03 | PASS | Both columns required; "Agent responds appropriately" banned |
| C-04 | PASS | Exception path + missing-fallback verdict |
| C-05 | PASS | Session Variable Delta column |
| C-06 | PASS | Phase 3 + Phase 4 diverge at named node |
| C-07 | PASS | Phase 2 inventory + Phase 5 coverage |
| C-08 | PASS | CS terms throughout |
| C-09 | PASS | CS Object to Edit column; prohibited generic advice |
| C-10 | PASS | Register zero-point examples name specific prohibited outputs: blank Agent Response row, "No significant issues found. Consider adding error handling.", hypothesis row with no node named |
| C-11 | PASS | CS column headers retained |
| C-12 | PASS | Phase exit MAY NOT gates present across all five phases |
| C-13 | PASS | Register table with Full credit / Zero points columns placed before "You are a Copilot Studio domain expert"; each row provides a named zero-point output the register expects to pre-empt |
| C-14 | FAIL | Zero-point examples are gathered into the pre-instruction register rather than distributed as per-section foil leads; no section opens with a bad-form example |
| C-15 | PASS | Phase 1 hypothesis table; Phase 5 verdict reconciliation |
| C-16 | FAIL | C-14 absent; three-structure requirement cannot fire |

**Score: 125/135** — Aspirational adds C-13 (+5) vs V-01.
*Matches prediction.*

---

#### V-03 — C-15 + C-14 (Hypothesis + Foils, No Register)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Phase 3 trace intact |
| C-02 | PASS | Phase 5 defect scan |
| C-03 | PASS | Both columns; Agent Response prohibition |
| C-04 | PASS | Exception path + missing-fallback |
| C-05 | PASS | Session Variable Delta |
| C-06 | PASS | Phase 3 + Phase 4 |
| C-07 | PASS | Phase 2 + coverage |
| C-08 | PASS | CS terms |
| C-09 | PASS | CS Object to Edit |
| C-10 | PASS | Foils name specific prohibited outputs: "User greets the agent. Agent identifies intent and fulfills request. Conversation ends normally." (Phase 3 foil); "When unrecognized input is received, the agent re-prompts..." (Phase 4 foil); "No significant issues found..." (Phase 5 foil) |
| C-11 | PASS | CS column headers |
| C-12 | PASS | MAY NOT exit conditions on all five phases |
| C-13 | FAIL | No pre-instruction register; foils are per-section, not gathered into a table before role priming |
| C-14 | PASS | Five phases each open with a named bad-form foil positioned before exit condition and requirements: Phase 1 ("fallback gaps and possible intent conflicts... names no specific topic nodes"), Phase 2 ("covers order inquiries... names no individual topic nodes"), Phase 3 ("User greets the agent... names no topic nodes, shows no utterances"), Phase 4 ("agent re-prompts... names no divergence node"), Phase 5 ("No significant issues found... cannot be acted on") — all five before requirements |
| C-15 | PASS | Phase 1 hypothesis; Phase 5 verdict |
| C-16 | FAIL | C-13 absent; three-structure requirement cannot fire |

**Score: 125/135** — Aspirational adds C-14 (+5) vs V-01.
*Matches prediction.*

---

#### V-04 — C-15 + C-13 + C-14 Without Phase Gates

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Section 3 trace intact with named entry/terminal |
| C-02 | PASS | Section 5 defect scan, four types |
| C-03 | PASS | Both utterance and response required per turn |
| C-04 | PASS | Exception path + missing-fallback verdict |
| C-05 | PASS | Session Variable Delta column |
| C-06 | PASS | Sections 3 + 4 |
| C-07 | PASS | Section 2 inventory + Section 5 coverage |
| C-08 | PASS | CS terms |
| C-09 | PASS | "Name node and exact Copilot Studio object" in remediation instruction; "Add better error handling" named as zero points in register |
| C-10 | PASS | Register zero-point examples name specific prohibited outputs; foils name structural anti-patterns; both active |
| C-11 | PASS | "Topic Node (Copilot Studio)", "Copilot Studio Object to Edit" as column headers |
| C-12 | FAIL | Phase exit conditions deliberately removed. Sections 3–5 contain embedded constraints ("Final row must name a terminal state", "Four verdicts required", "'Possible' and 'unclear' are not verdicts") but these are not structured as labeled exit conditions on named phase gates — no "Exit condition: MAY NOT..." gate language. The criterion requires phase gates with explicit hard exit conditions; V-04's requirements are woven into narrative instructions, not gate blocks |
| C-13 | PASS | Pre-instruction register before "You are a Copilot Studio domain expert"; Full credit / Zero points table with named zero-point examples per criterion |
| C-14 | PASS | Five sections each open with a named bad-form foil: Section 1 ("The agent may experience issues with fallback coverage..."), Section 2 ("The agent includes nodes for handling common..."), Section 3 ("The user initiates the conversation. The agent recognizes the intent..."), Section 4 ("When invalid input is received, the agent reprompts..."), Section 5 ("No significant issues found. Fallback behavior could be improved...") — all positioned before requirements |
| C-15 | PASS | Section 1 hypothesis table before trace sections; Section 5 hypothesis verdict with Confirmed/Refuted/Inconclusive |
| C-16 | FAIL | C-12 FAIL automatically causes C-16 FAIL; exit-condition structure absent as prohibition-delivery mechanism |

**Score: 125/135** — C-13 + C-14 + C-15 all pass; C-12 FAIL pulls score to same tier as V-02/V-03.
*Matches prediction.*

---

#### V-05 — Full Ceiling (All Seven Mechanisms + C-16)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Phase 3 complete trace, entry to terminal |
| C-02 | PASS | Phase 5 defect scan, all four types, hard verdicts |
| C-03 | PASS | Both columns required; "Agent responds appropriately" named and banned |
| C-04 | PASS | Phase 4 exception path + missing-fallback verdict |
| C-05 | PASS | Session Variable Delta column enforced |
| C-06 | PASS | Phases 3 and 4 structurally distinct paths |
| C-07 | PASS | Phase 2 inventory + Phase 5 per-node coverage |
| C-08 | PASS | Topics, trigger phrases, system topics, entities, condition branches, redirect nodes, session variables — all in context |
| C-09 | PASS | Remediation table: Exact Change Required + Copilot Studio Object to Edit; "Add better error handling" banned by name in register zero-points |
| C-10 | PASS | Three independent structures all name specific prohibited outputs |
| C-11 | PASS | "Topic Node (Copilot Studio)", "Redirect Target / System Topic", "Copilot Studio Object to Edit" as column headers |
| C-12 | PASS | All five phases carry "Exit condition: MAY NOT..." gates naming specific blocked failures: Phase 1 (fewer than four rows; "Possible issues may exist"), Phase 2 (empty cell; summary substitution), Phase 3 (active-node final row; "Agent responds appropriately"), Phase 4 (same node sequence as Phase 3), Phase 5 (combined no-issues; "possible"/"unclear" verdicts; generic "Add better error handling"; missing Phase 2 node from coverage) |
| C-13 | PASS | Register before role priming: Full credit / Zero points table with named zero-point examples covering all criteria |
| C-14 | PASS | Five phase-opening foils: Phase 1 ("The flow may have issues... names no specific topic nodes"), Phase 2 ("The agent includes nodes for common order, account, and support scenarios... names no individual topic nodes"), Phase 3 ("User greets the agent. Agent identifies the intent and fulfills the request... names no topic nodes, shows no utterances"), Phase 4 ("When unrecognized input is received, the agent re-prompts... names no divergence node"), Phase 5 ("No significant issues found. Consider reviewing fallback configuration... cannot be acted on") |
| C-15 | PASS | Phase 1 hypothesis table for all four defect types with predicted candidate node + suspected condition + confidence; Phase 5 hypothesis verdict cross-references each prediction with Confirmed/Refuted/Inconclusive + evidence cite |
| C-16 | PASS | All three prohibition-delivery structures present (C-12 PASS + C-13 PASS + C-14 PASS). Non-redundancy verified: **Register-unique** — concept-level omissions: `"session context is maintained appropriately"` (no variable names), `"Collisions might occur if topics have similar phrasing"` (no predicted node), `"The agent addresses the main user scenarios comprehensively"` (no per-node inventory); **Foil-unique** — structural anti-patterns: `"User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally."` (prose substituting for turn table), `"When unrecognized input is received, the agent re-prompts..."` (exception path as summary); **Exit-unique** — completion-state blockers: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness), `"MAY NOT use 'possible' or 'unclear' as verdicts"` (specific forbidden words), `"MAY NOT omit a Phase 2 node from the coverage table"` (missing-row coverage failure). Zero overlap across three axes |

**Score: 135/135** — All 16 criteria PASS.
*Matches prediction.*

---

### Composite Score Table

| Variation | Mechanisms | C-13 | C-14 | C-15 | C-12 | C-16 | Score | Prediction | Delta |
|-----------|-----------|------|------|------|------|------|-------|------------|-------|
| V-01 | C-15 only | FAIL | FAIL | PASS | PASS | FAIL | 120/135 | 120/135 | 0 |
| V-02 | C-15 + C-13 | PASS | FAIL | PASS | PASS | FAIL | 125/135 | 125/135 | 0 |
| V-03 | C-15 + C-14 | FAIL | PASS | PASS | PASS | FAIL | 125/135 | 125/135 | 0 |
| V-04 | C-15 + C-13 + C-14, no gates | PASS | PASS | PASS | FAIL | FAIL | 125/135 | 125/135 | 0 |
| V-05 | All seven | PASS | PASS | PASS | PASS | PASS | 135/135 | 135/135 | 0 |

**All five predictions confirmed. Zero delta.**

---

### Excellence Signals from V-05

**Signal 1 — Three-axis prohibition taxonomy (enables C-16)**
V-05 reveals that prohibition coverage has a natural taxonomy across three orthogonal failure planes: *concept-level omissions* (named concept, missing specific instance — caught by register), *structural anti-patterns* (prose substituting for structured table — caught by foils), and *completion-state blockers* (stopping at an invalid phase state — caught by exit gates). Each plane catches failures invisible to the other two. C-16 fires precisely because these planes are non-overlapping; adding a fourth prohibition to any single plane adds no breadth.

**Signal 2 — Predict-verify closure creates artifact accountability**
The hypothesis table in Phase 1 commits the model to specific candidate nodes and suspected conditions before any evidence is gathered. The verdict table in Phase 5 then closes the loop: each prediction receives a named Confirmed/Refuted/Inconclusive outcome with a cited turn or node. This creates an accountability structure spanning the full artifact — the model cannot produce a defect scan that contradicts its own prior prediction without the contradiction becoming visible. V-01 through V-04 all carry this structure, which shows it transfers robustly across mechanism combinations.

**Signal 3 — Register foil taxonomy: abstraction failure as its own failure mode**
V-05's register zero-point examples specifically target the *abstraction failure* class: outputs that name the concept without the instance (`"session context is maintained appropriately"` vs naming `order_id = 12345`). This is distinct from the structural anti-patterns named by foils. Explicitly naming the abstraction failure pattern in the register makes it a recognizable class, not just a vague quality deficit.

---

### New Patterns

None. All phenomena observed in Round 6 are captured by existing criteria C-01 through C-16. The three-axis prohibition taxonomy was the generating insight for C-16 and is now fully encoded. The round validates the criterion without surfacing structural variation that would require C-17.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": []}
```
