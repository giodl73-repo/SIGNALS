Written to `simulations/quest/variations/topic-retro-variations-R16-2026-03-17.md`.

---

## R16 — V-01 through V-05

**Three single-axis variations:**

**V-01 — Echo-First Role Sequence**
Echo candidate nominated before the wrong-verdict audit. The nomination is locked before Step 2 runs. The disqualification gate at Step 5 cross-references the pre-committed nomination against the completed verdict table. Hypothesis: prevents post-hoc rationalization of wrong predictions into surprises.

**V-02 — Audit Manifest Topology**
A single AUDIT MANIFEST table (columns: Signal ID, Namespace, Prediction, Actual, Verdict, Gap?, Echo Candidate?) is the primary artifact. All downstream sections are derived views — filtering WRONG rows gives backward recovery tables A+B (targeting C-38), grouping by Namespace gives coverage table, filtering Echo Candidate? = YES gives Echo input. Nothing is re-authored.

**V-03 — Phase Gates with C-38/C-39 as Explicit Gate Conditions**
Phase structure from R15 V-03, but Phase 1's exit checklist names C-38 and C-39 explicitly as checkbox conditions: "Backward Recovery Table A present as a named structural table (not prose)?" and "PRE-EXECUTION CONTRACT has Signal Window field?" and "Mode field?". The gate cannot be signed without those exact structures.

**Two combined variations:**

**V-04 — Echo-First + Challenge Voice**
Echo-first sequencing with adversarial phrasing ("Name your surprise now, before you see the numbers"). The disqualification table is framed as challenges rather than checks. Systemic pattern is a named structural field to prevent pattern reasoning from collapsing into prose.

**V-05 — Audit Manifest + Phase Gates**
Three-phase architecture: Phase 1 builds the manifest, Phase 2 derives accuracy+gap views from it, Phase 3 derives Echo from it. Phase 2's gate artifact explicitly asserts "Backward Recovery Table A: PRESENT" — making C-38 a named gate condition within the manifest+derivation topology.
ine surprise identification. The nomination is on record before the author knows the final audit results, preventing the pattern where a failed prediction is retroactively repackaged as a surprise. The disqualification gate cross-references the pre-committed nomination against the completed verdict table.

---

```
You are running /topic-retro. This retrospective begins with an Echo nomination BEFORE the wrong-verdict audit. This ordering forces genuine surprise identification: the candidate is on record before the audit results are known.

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [shipped feature / approved spec / cancelled initiative / pivoted] |
| Signal window | [start date] to [end date] — bounding range of signals evaluated |
| Mode | STANDARD or AMEND: [if AMEND, declare scope — e.g., "scout signals only, 30-day window"] |

If Mode = AMEND: every section below must include an explicit `[OUT OF SCOPE: <reason>]` row or notation for excluded signal types. Scope declared but not enforced per-section = structural failure.

---

## STEP 1 — ECHO NOMINATION (before the audit)

Before reviewing predictions, name your Echo candidate. This is the finding that genuinely surprised you — something that was not predictable from the signals you had at the time.

Write it here before continuing to Step 2:

| Field | Value |
|-------|-------|
| Candidate finding | [one sentence — what surprised you?] |
| Why it seemed unforeseeable | [what would have been required to predict this?] |
| Potential actionable follow-up | [what practice change does this suggest?] |

The nomination is locked after Step 1. It cannot be revised once Step 2 is complete.

---

## STEP 2 — WRONG VERDICT AUDIT

Enumerate every signal gathered during the topic's signal window. For each signal with a directional prediction, record what was predicted and what actually happened.

**Signal Accuracy Table:**

| # | Signal | Namespace | Prediction | Actual Outcome | Verdict |
|---|--------|-----------|------------|----------------|---------|
| 1 | | | | | CORRECT / WRONG |
| 2 | | | | | |
| … | | | | | |

Signals without directional predictions: record count separately as N/A (excluded from accuracy ratio). ABSENT signals (should have been gathered but weren't) feed Step 4, not this table.

**Forward Count Table:**

| Metric | Value |
|--------|-------|
| Total rows evaluated (N) | |
| CORRECT (C) | |
| WRONG (W) | |
| C + W = N? | YES / NO — resolve before proceeding |

---

## STEP 3 — BACKWARD RECOVERY

Starting from the WRONG verdicts, recover the total prediction count. This is a separate structural artifact from the forward count — not inline math and not prose.

**Backward Recovery Table A — WRONG Verdict Inventory:**

| Recovery # | Signal | Namespace | Why Prediction Failed |
|------------|--------|-----------|----------------------|
| R-01 | | | |
| R-02 | | | |
| … | | | |

**Backward Recovery Table B — Recovery to Total:**

| Step | Value |
|------|-------|
| WRONG verdicts counted in Table A (W_back) | |
| W_back equals W from Forward Count Table? | YES / NO |
| Implied CORRECT count (N minus W_back = C_back) | |
| C_back equals C from Forward Count Table? | YES / NO |
| Reconciled? | YES / NO |
| Discrepancy (if NO) | [describe and resolve before proceeding] |
| Reconciled accuracy ratio | C / N = ?% |

---

## STEP 4 — NAMESPACE COVERAGE AND GAP ANALYSIS

Scan all 9 namespaces for signals that were absent during the topic run. Do not revisit wrong verdicts here.

**Namespace Coverage Table:**

| Namespace | Signals Gathered | Signals Absent | Decision Impact of Absent |
|-----------|-----------------|----------------|--------------------------|
| scout | | | WOULD CHANGE / NO / UNKNOWN |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

[If AMEND: append `[OUT OF SCOPE: <reason>]` row for excluded namespaces]

**Gap Summary:**

| Gap ID | Namespace | Signal Type | Decision Impact | Priority |
|--------|-----------|-------------|-----------------|----------|
| G-01 | | | YES / NO / UNKNOWN | HIGH / MED / LOW |

---

## STEP 5 — ECHO DISQUALIFICATION GATE

The nomination from Step 1 is now cross-referenced against the verdict table from Step 2.

| Check | Candidate (from Step 1) | Result |
|-------|------------------------|--------|
| Nomination listed as WRONG in Step 2 Signal Accuracy Table? | [candidate] | YES → DISQUALIFIED / NO → proceed |
| Nomination predictable from signals gathered at the time? | | YES → DISQUALIFIED / NO → proceed |
| Nomination links to an actionable follow-up? | | NO → DISQUALIFIED / YES → proceed |
| Nomination survives all three checks? | | YES / NO |

If DISQUALIFIED: state which check triggered. Then assess whether any other finding from the retrospective qualifies. Apply the same three-check gate to each candidate. If none qualifies: **Echo: NONE** (valid result — state reason).

If nomination survives: it becomes the confirmed Echo.

---

## STEP 6 — ECHO

If Echo: NONE, state the reason. That is a valid and complete output for this section.

If Echo survives the disqualification gate:

| Field | Value |
|-------|-------|
| Finding | [one sentence — the unexpected finding] |
| Why unexpected | [what made this unforeseeable at prediction time] |
| Actionable follow-up | [specific practice change or investigation] |
| Systemic pattern | [Pattern name + recurrence description across topics] or [No systemic pattern identified] |

Systemic pattern is a named structural field in this table. It is not embedded in the follow-up prose.

---

## STEP 7 — IMPROVEMENT RECOMMENDATION

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id] or Echo: [pattern-name] |
| Practice change | [specific, implementable change to signal-gathering workflow] |
| Namespace affected | [which namespace and skill] |
| Expected improvement | [measurable outcome or metric] |

---

## SECTION ORDER (do not reorder)

1. PRE-EXECUTION CONTRACT
2. Step 1 — Echo Nomination (before predictions)
3. Step 2 — Signal Accuracy Table + Forward Count Table
4. Step 3 — Backward Recovery Table A (WRONG inventory) + Table B (recovery to total)
5. Step 4 — Namespace Coverage Table + Gap Summary
6. Step 5 — Echo Disqualification Gate
7. Step 6 — Echo (or NONE)
8. Step 7 — Improvement Recommendation

The Echo Nomination is committed at Step 1 and cross-referenced at Step 5. It cannot be revised between steps.
```

---

## V-02 — Single-axis: Output Format (Audit Manifest Topology)
**Axis**: Output format — master cross-reference manifest as primary artifact; all sections as derived views
**Hypothesis**: A single AUDIT MANIFEST table where every signal has a row — with columns for Verdict, Gap?, and Echo Candidate? — makes the backward recovery table (C-38) mechanically derivable by filtering WRONG rows, and makes namespace coverage (C-06) mechanically derivable by grouping the Namespace column. Sections become computed views over the manifest rather than independently authored artifacts, eliminating the authoring errors that come from re-narrating the same signals multiple times.

---

```
You are running /topic-retro. This retrospective is organized around a single AUDIT MANIFEST — a master table where every signal occupies one row. All subsequent sections are derived views over the manifest: they filter, group, or aggregate manifest content. They do not re-author content that is already in the manifest.

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [shipped feature / approved spec / cancelled initiative / pivoted] |
| Signal window | [start date] to [end date] |
| Mode | STANDARD or AMEND: [if AMEND, declare scope] |

---

## AUDIT MANIFEST

Build the manifest first. Every signal from the topic run gets a row. Do not skip any signal. The manifest is the authoritative record — sections below derive from it.

| Signal ID | Signal Name | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-------------|-----------|------------|----------------|---------|------|-----------------|
| S-01 | | | | | CORRECT / WRONG / N/A | YES / NO | YES / NO |
| S-02 | | | | | | | |
| … | | | | | | | |

**Column definitions:**
- **Verdict**: CORRECT (prediction matched actual), WRONG (prediction did not match), N/A (no directional prediction made — excluded from accuracy ratio)
- **Gap?**: YES if this signal type was absent and should have been gathered; NO if it was gathered
- **Echo Candidate?**: At most ONE row may be YES — the finding that genuinely surprised you. If no finding qualifies as a genuine surprise, every row = NO.

[If AMEND: append `[OUT OF SCOPE: <signal types>]` rows for excluded categories]

---

## ACCURACY VIEW (derived from manifest)

Filter the manifest on Verdict column. Do not re-author signal rows.

**Forward Count Table:**

| Metric | Value |
|--------|-------|
| Total rows with Verdict = CORRECT or WRONG (N) | [count from manifest] |
| CORRECT count (C) | [count from manifest] |
| WRONG count (W) | [count from manifest] |
| C + W = N? | YES / NO — resolve if NO by reconciling against manifest |
| Forward accuracy | C / (C + W) = ?% |

**Backward Recovery Table A — WRONG Verdict Inventory:**

List every manifest row where Verdict = WRONG. Derived from manifest — do not re-author.

| Recovery # | Signal ID | Signal Name | Namespace | Why Prediction Failed |
|------------|-----------|-------------|-----------|----------------------|
| R-01 | S-XX | | | |
| R-02 | S-XX | | | |
| … | | | | |

**Backward Recovery Table B — Recovery to Total:**

| Step | Value |
|------|-------|
| WRONG rows enumerated in Table A (W_back) | |
| W_back equals W from Forward Count Table? | YES / NO |
| Implied CORRECT count (N minus W_back = C_back) | |
| C_back equals C from Forward Count Table? | YES / NO |
| Reconciled? | YES / NO |
| Discrepancy (if NO) | [describe and resolve against manifest row IDs] |
| Reconciled accuracy ratio | C / N = ?% |

---

## NAMESPACE VIEW (derived from manifest)

Group manifest rows by Namespace. Count gathered and absent per namespace. One row per namespace — all 9 must appear.

**Namespace Coverage Table:**

| Namespace | Gathered Count | Absent Signal Types | Decision Impact of Absent |
|-----------|---------------|---------------------|--------------------------|
| scout | | | WOULD CHANGE / NO / UNKNOWN |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

[If AMEND: row for excluded namespaces with `[OUT OF SCOPE: <reason>]`]

**Gap Summary** (derived: manifest rows where Gap? = YES):

| Gap ID | Namespace | Signal Type | Decision Impact | Priority |
|--------|-----------|-------------|-----------------|----------|
| G-01 | | | YES / NO / UNKNOWN | HIGH / MED / LOW |

---

## ECHO VIEW (derived from manifest)

Filter manifest for rows where Echo Candidate? = YES.

If no row has Echo Candidate? = YES: **Echo: NONE**. State reason. Proceed directly to Recommendation.

If one row has Echo Candidate? = YES: apply the disqualification gate to that row.

**Echo Disqualification Gate:**

| Check | Candidate (Signal ID from manifest) | Result |
|-------|-------------------------------------|--------|
| Candidate row has Verdict = WRONG in manifest? | [Signal ID] | YES → DISQUALIFIED / NO → proceed |
| Candidate finding was predictable from gathered signals? | | YES → DISQUALIFIED / NO → proceed |
| Candidate links to an actionable follow-up? | | NO → DISQUALIFIED / YES → proceed |
| Candidate survives gate? | | YES / NO |

If DISQUALIFIED: **Echo: NONE** — state which check triggered. Do not nominate a second candidate from outside the manifest.

If survives:

| Field | Value |
|-------|-------|
| Finding | [one sentence derived from manifest row] |
| Why unexpected | [what made this unforeseeable at prediction time] |
| Actionable follow-up | [specific practice change] |
| Systemic pattern | [Pattern name + recurrence description across topics] or [No systemic pattern identified] |

---

## IMPROVEMENT RECOMMENDATION

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id] or Echo: [pattern-name] |
| Practice change | [specific, implementable change] |
| Namespace affected | [namespace and skill] |
| Expected improvement | [measurable outcome] |

---

## SECTION ORDER

1. PRE-EXECUTION CONTRACT
2. AUDIT MANIFEST
3. ACCURACY VIEW — Forward Count Table
4. ACCURACY VIEW — Backward Recovery Table A (WRONG inventory)
5. ACCURACY VIEW — Backward Recovery Table B (recovery to total)
6. NAMESPACE VIEW — Namespace Coverage Table
7. NAMESPACE VIEW — Gap Summary
8. ECHO VIEW — Echo Disqualification Gate
9. ECHO VIEW — Echo (or NONE)
10. IMPROVEMENT RECOMMENDATION

Sections 3–10 derive from the manifest. They filter, group, or aggregate manifest content. They do not re-author it. If a derived section contradicts the manifest, the manifest takes precedence.
```

---

## V-03 — Single-axis: Lifecycle Emphasis (Phase Gates with C-38/C-39 as Explicit Gate Conditions)
**Axis**: Lifecycle emphasis — phase gates where C-38 and C-39 are named explicit conditions in the phase exit criteria, not merely implied
**Hypothesis**: When C-38 (backward recovery as named two-table artifact) and C-39 (Signal Window + Mode as named structural fields in PRE-EXECUTION CONTRACT) appear as named checkbox conditions in the phase gate signing artifact, the model cannot sign the gate without those exact structures being present. This promotes C-38/C-39 from aspirational patterns that may or may not appear into structural requirements enforced at gate-signing time.

---

```
You are running /topic-retro. This retrospective runs in three phases. Each phase has entry criteria, a body, exit criteria, and a gate artifact. A phase cannot begin until the prior phase's gate is signed. Two structural artifacts are explicitly required by the phase gates: (1) a PRE-EXECUTION CONTRACT with four named structural fields — Topic, Commitment nature, Signal window, Mode — and (2) a two-table Backward Recovery artifact with step-by-step recovery columns. These are named conditions in the exit checklists, not style suggestions.

---

## PRE-EXECUTION CONTRACT

Fill all four fields before Phase 1 begins. These four fields are the entry condition for Phase 1.

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [what was committed and when] |
| Signal window | [start date] to [end date] — bounding range of signals evaluated |
| Mode | STANDARD or AMEND: [if AMEND, declare scope] |

If any of the four fields is absent or incomplete: Phase 1 does not begin. Fill all four, then proceed.

---

## PHASE 1 — ACCURACY AUDIT

**Entry criteria:**
- [ ] PRE-EXECUTION CONTRACT has all four named fields: Topic, Commitment nature, Signal window, Mode
- [ ] If Mode = AMEND: scope is declared in the CONTRACT

**Body:**

Enumerate every signal gathered during the topic's signal window. For each signal with a directional prediction, record prediction and actual outcome.

**Signal Accuracy Table:**

| # | Signal | Namespace | Prediction | Actual Outcome | Verdict |
|---|--------|-----------|------------|----------------|---------|
| 1 | | | | | CORRECT / WRONG |
| 2 | | | | | |
| … | | | | | |

Signals without directional predictions: record count separately as N/A (excluded from accuracy ratio).
[If AMEND: append `[OUT OF SCOPE: <scope>]` row to this table]

**Forward Count Table:**

| Metric | Value |
|--------|-------|
| Total evaluated (N) | |
| CORRECT (C) | |
| WRONG (W) | |
| C + W = N? | YES / NO |

**Backward Recovery Table A — WRONG Verdict Inventory** (named structural table — not prose, not inline math):

| Recovery # | Signal | Namespace | Why Prediction Failed |
|------------|--------|-----------|----------------------|
| R-01 | | | |
| R-02 | | | |
| … | | | |

**Backward Recovery Table B — Recovery to Total** (named structural table — step-by-step recovery columns required):

| Step | Value |
|------|-------|
| WRONG verdicts counted in Table A (W_back) | |
| W_back equals W from Forward Count Table? | YES / NO |
| Implied CORRECT count (N minus W_back = C_back) | |
| C_back equals C from Forward Count Table? | YES / NO |
| Reconciled? | YES / NO |
| Discrepancy (if NO) | [describe and resolve] |
| Reconciled accuracy ratio | C / N = ?% |

**Phase 1 Exit Checklist (all must be YES before signing):**
- [ ] Signal Accuracy Table complete
- [ ] Forward Count Table present with N, C, W stated
- [ ] C + W = N reconciled
- [ ] **Backward Recovery Table A present as a named structural table** (not prose or inline math)
- [ ] **Backward Recovery Table B present with step-by-step recovery columns** (starting W_back, implied C_back, reconciliation result row)
- [ ] Reconciled accuracy ratio stated after both tables agree
- [ ] **PRE-EXECUTION CONTRACT has all four named fields: Topic, Commitment nature, Signal window, Mode**

**PHASE 1 GATE:**
```
PHASE-1-COMPLETE
Reconciled accuracy: C=[C], W=[W], N=[N], ratio=[X%]
Backward Recovery Table A: [PRESENT / ABSENT]
Backward Recovery Table B: [PRESENT / ABSENT], reconciled=[YES / NO]
PRE-EXECUTION CONTRACT fields: Topic=[PRESENT], Commitment=[PRESENT], Signal window=[PRESENT], Mode=[PRESENT]
```

Phase 2 does not begin without `PHASE-1-COMPLETE` with all fields showing PRESENT.

---

## PHASE 2 — GAP ANALYSIS

**Entry criteria:** PHASE-1-COMPLETE is present in output.

**Body:**

Scan all 9 namespaces for signals absent during the topic run. Phase 2 does not revisit wrong verdicts from Phase 1. Wrong verdicts are closed.

**Namespace Coverage Table:**

| Namespace | Gathered | Absent Signal Types | Would Absent Signal Have Changed Decision? |
|-----------|----------|---------------------|-------------------------------------------|
| scout | | | YES / NO / UNKNOWN |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

[If AMEND: append `[OUT OF SCOPE: <reason>]` row for excluded namespaces]

**Gap Summary:**

| Gap ID | Namespace | Signal Type | Decision Impact | Priority |
|--------|-----------|-------------|-----------------|----------|
| G-01 | | | YES / NO / UNKNOWN | HIGH / MED / LOW |

**Phase 2 Exit Checklist:**
- [ ] All 9 namespaces present in coverage table
- [ ] Each namespace has at least one entry (even if "none absent")
- [ ] Gap summary lists all gaps with YES or UNKNOWN decision impact

**PHASE 2 GATE:**
```
PHASE-2-COMPLETE
Namespaces covered: [count]/9
High-impact gaps: [list gap IDs or NONE]
```

Phase 3 does not begin without `PHASE-2-COMPLETE`.

---

## PHASE 3 — ECHO

**Entry criteria:** PHASE-2-COMPLETE is present in output.

**Body:**

Phase 3 does not revisit wrong verdicts (Phase 1) or gap analysis (Phase 2). One task: identify the one unexpected finding that was not predictable from the signals gathered.

**Echo Disqualification Gate** (named gate — must appear explicitly before any Echo content is written):

| Check | Candidate | Result |
|-------|-----------|--------|
| Candidate listed as WRONG in Phase 1 Signal Accuracy Table? | [candidate description] | YES → DISQUALIFIED / NO → proceed |
| Candidate predictable from signals gathered at time of decision? | | YES → DISQUALIFIED / NO → proceed |
| Candidate links to an actionable follow-up? | | NO → DISQUALIFIED / YES → proceed |
| Candidate survives gate? | | YES / NO |

If no candidate survives: **Echo: NONE** (valid result — state reason).

**Echo** (if candidate survived gate):

| Field | Value |
|-------|-------|
| Finding | [one sentence] |
| Why unexpected | [what made this unforeseeable at prediction time] |
| Actionable follow-up | [specific practice change] |
| Systemic pattern | [Pattern name + recurrence description across topics] or [No systemic pattern identified] |

**Improvement Recommendation:**

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id] or Echo: [pattern-name] |
| Practice change | [specific, implementable] |
| Namespace affected | [namespace and skill] |
| Expected improvement | [measurable outcome] |

**Phase 3 Exit Checklist:**
- [ ] Echo Disqualification Gate explicitly applied and result stated
- [ ] Echo or Echo: NONE stated
- [ ] Improvement Recommendation addresses a named gap or Echo pattern

**PHASE 3 GATE:**
```
PHASE-3-COMPLETE
Echo: [one-sentence finding or NONE]
Recommendation addresses: [gap-id or pattern-name]
```

---

## RETROSPECTIVE COMPLETE

All three gate artifacts present and complete: PHASE-1-COMPLETE + PHASE-2-COMPLETE + PHASE-3-COMPLETE.

If AMEND mode was declared: confirm every section included an explicit out-of-scope notation for excluded signal types. Missing notation in any section = incomplete retrospective.
```

---

## V-04 — Combined: Role Sequence (Echo-First) + Phrasing Register (Challenge Voice)
**Axis**: Role sequence (Echo nominated before wrong-verdict audit) + Phrasing register (adversarial challenge voice — the prompt interrogates the author's Echo candidate, not describes it)
**Hypothesis**: A challenge register ("Name your surprise now, before you see the audit results") combined with pre-committed Echo nomination makes the disqualification gate feel adversarial rather than procedural. The model must defend each Echo candidate against explicit challenges, reducing the likelihood that a wrong prediction gets promoted to Echo and increasing the likelihood that the systemic pattern field is populated with genuine pattern reasoning rather than boilerplate.

---

```
You are running /topic-retro. Something has shipped or been committed. Before you calculate how many predictions were wrong — write down what surprised you. Write it now, while the audit results are still unknown. This is the only way to get an honest Echo.

---

## BEFORE ANYTHING ELSE — ESTABLISH CONTEXT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment | [what was committed and when — shipped feature, approved spec, cancelled initiative, etc.] |
| Signal window | [start date] to [end date] — how far back are you looking at signals?] |
| Mode | STANDARD (full retrospective) or AMEND: [scope if restricted to specific signal types or time window] |

If AMEND: write the scope here, and repeat it explicitly in every section below.

---

## STEP 1 — NAME YOUR SURPRISE NOW (before you see the audit)

Don't open the predictions yet. Don't calculate the score. Ask yourself: what genuinely surprised you about how this topic turned out?

Not something that went wrong that you should have caught — that's Step 2 territory. Something that came from outside the frame entirely. Something that none of your signals pointed to.

Write it down now:

| Field | Value |
|-------|-------|
| What surprised you | [one sentence — the unexpected finding] |
| Why you couldn't have predicted it | [what would you have needed at the time to foresee this?] |
| What it might mean for how you work | [initial action idea] |

This is locked. You cannot revise it after Step 2 is complete.

---

## STEP 2 — AUDIT YOUR PREDICTIONS

Now go through every signal gathered during the topic run. For each one: what did it predict, and what actually happened?

| # | Signal | Namespace | What was predicted | What actually happened | Right or wrong? |
|---|--------|-----------|-------------------|------------------------|-----------------|
| 1 | | | | | CORRECT / WRONG |
| 2 | | | | | |
| … | | | | | |

Count up:

| Metric | Value |
|--------|-------|
| Total predictions evaluated (N) | |
| CORRECT (C) | |
| WRONG (W) | |
| Do they add up? C + W = N? | YES / NO — if NO, find what you missed |

[If AMEND: note which signal types are out of scope in this step]

---

## STEP 3 — CHECK YOUR MATH BACKWARD

You counted forward. Now start from the WRONG verdicts and work backward to the total. This is a separate structural check — two named tables, not a verbal summary.

**Wrong Verdict Inventory — Table A** (one row per WRONG verdict):

| # | Signal | Namespace | Why the prediction failed |
|---|--------|-----------|--------------------------|
| W-01 | | | |
| W-02 | | | |
| … | | | |

**Recovery Check — Table B** (recover the total from Table A):

| Step | Value |
|------|-------|
| WRONG rows counted in Table A (W_back) | |
| Matches W from Step 2? | YES / NO |
| Implied CORRECT count (N minus W_back = C_back) | |
| Matches C from Step 2? | YES / NO |
| Reconciled? | YES / NO |
| If NO — what is the discrepancy? | [identify and resolve against the signal list] |
| Final accuracy ratio | C / N = ?% |

---

## STEP 4 — WHAT WAS NEVER GATHERED?

Different question from Step 2. Not "what predictions were wrong" — "what signals were never collected?"

Go through all 9 namespaces:

| Namespace | What did you get? | What was absent? |
|-----------|-----------------|-----------------|
| scout | | |
| draft | | |
| review | | |
| flow | | |
| trace | | |
| prove | | |
| listen | | |
| program | | |
| topic | | |

For each absent signal type, ask honestly: if you'd had it, would the commitment have looked different?

| Gap | Namespace | Would it have changed the decision? |
|-----|-----------|-------------------------------------|
| G-01 | | YES / NO / HONESTLY UNSURE |

[If AMEND: mark excluded namespaces with `[OUT OF SCOPE: <reason>]`]

---

## STEP 5 — CHALLENGE YOUR SURPRISE

You named your candidate in Step 1. The audit is now complete. Here is the challenge:

| Challenge | Your candidate | Verdict |
|-----------|---------------|---------|
| Does your candidate appear in the Step 2 WRONG table? | [candidate from Step 1] | YES → it was a failed prediction, not a surprise. DISQUALIFIED. / NO → survives |
| Would you have predicted this from the signals you actually had at the time? | | YES → it was foreseeable, not unexpected. DISQUALIFIED. / NO → survives |
| Does this finding point to something you can actually change? | | NO → an observation without action is not an Echo. DISQUALIFIED. / YES → survives |
| Does your candidate survive all three challenges? | | YES / NO |

If NO on any challenge: your Step 1 candidate is **disqualified**. State which challenge triggered it. Then ask: is there any other finding from the retrospective that passes all three? Apply the same challenge to each candidate in turn. If nothing survives: **Echo: NONE** — that is a legitimate result. Don't invent a surprise.

---

## STEP 6 — WRITE THE ECHO

If nothing survived: **Echo: NONE**. State which challenge eliminated your best candidate. Move directly to Step 7.

If a candidate survived all three challenges:

| Field | Value |
|-------|-------|
| Finding | [one sentence — the unexpected finding] |
| Why unexpected | [what made this genuinely unforeseeable at signal-gathering time?] |
| What you will do differently | [specific, implementable practice change] |
| Is this part of a pattern? | [Have you been surprised this way before, across topics? If yes: name the pattern and describe how it recurs. If isolated: "No systemic pattern identified."] |

The "Is this part of a pattern?" field is a named structural field in this table. Do not bury pattern reasoning in the "Why unexpected" prose.

---

## STEP 7 — ONE RECOMMENDATION

Name what you are addressing. Do not give generic process advice.

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id from Step 4] or Echo: [pattern-name from Step 6] |
| What changes | [specific change to how signals are gathered or interpreted] |
| Which namespace and skill this affects | [namespace name and skill name] |
| How you would know it worked | [what measurable outcome or metric would improve] |

---

## OUTPUT ORDER

1. Context (pre-execution fields)
2. Step 1 — Echo Nomination (locked before audit)
3. Step 2 — Signal Accuracy Table + Count
4. Step 3 — Wrong Verdict Inventory (Table A) + Recovery Check (Table B)
5. Step 4 — Namespace Coverage + Gap Summary
6. Step 5 — Echo Disqualification Challenge
7. Step 6 — Echo (or NONE)
8. Step 7 — Recommendation

The surprise is committed at Step 1. It is challenged at Step 5. The gap between these steps is what makes the challenge honest.
```

---

## V-05 — Combined: Output Format (Audit Manifest) + Lifecycle Emphasis (Phase Gates)
**Axis**: Output format (audit manifest as primary artifact) + Lifecycle emphasis (phase gates)
**Hypothesis**: Combining manifest topology with phase gates creates a three-layer architecture: Phase 1 BUILDS the manifest (no derived sections yet), Phase 2 DERIVES accuracy and gap views from the manifest, Phase 3 DERIVES Echo from the manifest. Cross-contamination between wrong verdicts, gaps, and Echo is structurally impossible because each phase only reads the manifest — it never re-authors it. Phase gate artifacts reference manifest row counts, making reconciliation auditable at each boundary.

---

```
You are running /topic-retro. This retrospective uses a two-layer architecture: a manifest layer and a derivation layer. Phase 1 builds the manifest. Phases 2 and 3 derive their output from the manifest. No derived section re-authors content that is already in the manifest.

---

## PRE-EXECUTION CONTRACT

| Field | Value |
|-------|-------|
| Topic | [topic name] |
| Commitment nature | [shipped feature / approved spec / cancelled initiative / pivoted] |
| Signal window | [start date] to [end date] |
| Mode | STANDARD or AMEND: [if AMEND, declare scope] |

All four fields are entry conditions for Phase 1. If any is absent: Phase 1 does not begin.

---

## PHASE 1 — BUILD THE MANIFEST

**Entry criteria:**
- [ ] PRE-EXECUTION CONTRACT has all four named fields: Topic, Commitment nature, Signal window, Mode
- [ ] If Mode = AMEND: scope is declared

**Purpose:** Populate the authoritative record. Every signal from the topic's signal window gets exactly one row. Assign Verdict, Gap?, and Echo Candidate? as you go. No derived sections are written in this phase.

**AUDIT MANIFEST:**

| Signal ID | Signal Name | Namespace | Prediction | Actual Outcome | Verdict | Gap? | Echo Candidate? |
|-----------|-------------|-----------|------------|----------------|---------|------|-----------------|
| S-01 | | | | | CORRECT / WRONG / N/A | YES / NO | YES / NO |
| S-02 | | | | | | | |
| … | | | | | | | |

**Column rules:**
- **Verdict**: CORRECT (prediction matched), WRONG (prediction did not match), N/A (no directional prediction — excluded from accuracy ratio)
- **Gap?**: YES if this signal type was absent and should have been gathered; NO if gathered
- **Echo Candidate?**: At most ONE row may be YES — the finding that genuinely surprised you. If no finding qualifies, all rows = NO.

[If AMEND: append `[OUT OF SCOPE: <signal types>]` rows for excluded categories]

**Phase 1 Exit Checklist:**
- [ ] Every signal from the topic run has a row in the manifest
- [ ] Every row has Verdict, Gap?, and Echo Candidate? assigned
- [ ] At most one row has Echo Candidate? = YES
- [ ] AMEND out-of-scope rows appended if Mode = AMEND

**PHASE 1 GATE:**
```
PHASE-1-COMPLETE
Manifest rows: [total]
CORRECT rows: [C]
WRONG rows: [W]
N/A rows: [X]
Gap? = YES rows: [gap_count]
Echo Candidate? = YES rows: [0 or 1]
```

Phase 2 does not begin without `PHASE-1-COMPLETE`.

---

## PHASE 2 — DERIVE ACCURACY AND GAP VIEWS

**Entry criteria:** PHASE-1-COMPLETE is present.

**Purpose:** Read the manifest. Derive accuracy and gap sections by filtering and grouping manifest rows. Do not re-author manifest content.

---

### 2A — ACCURACY VIEW (derived from manifest Verdict column)

**Forward Count Table:**

| Metric | Value |
|--------|-------|
| Total rows with Verdict = CORRECT or WRONG (N) | [from manifest — matches C + W in Phase 1 gate] |
| CORRECT rows (C) | [from manifest] |
| WRONG rows (W) | [from manifest] |
| C + W = N? | YES / NO — resolve against manifest if NO |
| Forward accuracy | C / N = ?% |

**Backward Recovery Table A — WRONG Verdict Inventory** (derived: list every manifest row where Verdict = WRONG):

| Recovery # | Signal ID | Signal Name | Namespace | Why Prediction Failed |
|------------|-----------|-------------|-----------|----------------------|
| R-01 | S-XX | | | |
| R-02 | S-XX | | | |
| … | | | | |

**Backward Recovery Table B — Recovery to Total:**

| Step | Value |
|------|-------|
| WRONG rows enumerated in Table A (W_back) | |
| W_back equals W from Forward Count Table? | YES / NO |
| Implied CORRECT count (N minus W_back = C_back) | |
| C_back equals C from Forward Count Table? | YES / NO |
| Reconciled? | YES / NO |
| Discrepancy (if NO) | [describe and resolve by citing manifest row IDs] |
| Reconciled accuracy ratio | C / N = ?% |

---

### 2B — NAMESPACE VIEW (derived from manifest Namespace and Gap? columns)

**Namespace Coverage Table** (group manifest rows by Namespace, count):

| Namespace | Gathered Count | Absent Signal Types | Decision Impact of Absent |
|-----------|---------------|---------------------|--------------------------|
| scout | | | WOULD CHANGE / NO / UNKNOWN |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

[If AMEND: row for excluded namespaces with `[OUT OF SCOPE: <reason>]`]

**Gap Summary** (derived: manifest rows where Gap? = YES):

| Gap ID | Namespace | Signal Type | Decision Impact | Priority |
|--------|-----------|-------------|-----------------|----------|
| G-01 | | | YES / NO / UNKNOWN | HIGH / MED / LOW |

**Phase 2 Exit Checklist:**
- [ ] Forward Count Table present
- [ ] Backward Recovery Table A present (WRONG rows from manifest enumerated)
- [ ] Backward Recovery Table B present (step-by-step recovery to total)
- [ ] Forward and backward counts reconciled
- [ ] All 9 namespaces present in Namespace Coverage Table
- [ ] Gap Summary lists all YES/UNKNOWN-impact gaps

**PHASE 2 GATE:**
```
PHASE-2-COMPLETE
Accuracy ratio: C=[C], W=[W], N=[N], reconciled=[X%]
Backward Recovery Table A: PRESENT ([W_back] rows)
Backward Recovery Table B: PRESENT, reconciled=[YES / NO]
Namespaces covered: [count]/9
High-impact gaps: [list gap IDs or NONE]
```

Phase 3 does not begin without `PHASE-2-COMPLETE`.

---

## PHASE 3 — DERIVE ECHO

**Entry criteria:** PHASE-2-COMPLETE is present.

**Purpose:** Identify the Echo from the manifest. Phase 3 does not revisit wrong verdicts (Phase 2 accuracy view) or gaps (Phase 2 namespace view). One task: identify the unexpected finding.

---

### 3A — ECHO DERIVATION (derived from manifest Echo Candidate? column)

Check the manifest for rows where Echo Candidate? = YES.

If no manifest row has Echo Candidate? = YES: **Echo: NONE**. State reason. Proceed directly to Recommendation.

If one manifest row has Echo Candidate? = YES: apply the disqualification gate to that row.

**Echo Disqualification Gate:**

| Check | Candidate (Signal ID from manifest) | Result |
|-------|-------------------------------------|--------|
| Candidate row has Verdict = WRONG in manifest? | [Signal ID] | YES → DISQUALIFIED / NO → proceed |
| Candidate finding was predictable from gathered signals at time of decision? | | YES → DISQUALIFIED / NO → proceed |
| Candidate links to an actionable follow-up? | | NO → DISQUALIFIED / YES → proceed |
| Candidate survives gate? | | YES / NO |

If DISQUALIFIED: **Echo: NONE** — state which check triggered. Do not nominate additional candidates not present in the manifest.

If candidate survives:

| Field | Value |
|-------|-------|
| Finding | [one sentence derived from manifest Echo Candidate row] |
| Why unexpected | [what made this unforeseeable at prediction time] |
| Actionable follow-up | [specific practice change] |
| Systemic pattern | [Pattern name + recurrence description across topics] or [No systemic pattern identified] |

---

### 3B — RECOMMENDATION

| Field | Value |
|-------|-------|
| Addresses | Gap: [gap-id from Phase 2] or Echo: [pattern-name from Phase 3] |
| Practice change | [specific, implementable change to signal-gathering workflow] |
| Namespace affected | [namespace and skill] |
| Expected improvement | [measurable outcome] |

**Phase 3 Exit Checklist:**
- [ ] Echo Disqualification Gate explicitly applied
- [ ] Echo or Echo: NONE stated with reason
- [ ] Recommendation addresses a named gap or Echo pattern

**PHASE 3 GATE:**
```
PHASE-3-COMPLETE
Echo: [one-sentence finding or NONE]
Recommendation addresses: [gap-id or pattern-name]
```

---

## RETROSPECTIVE COMPLETE

All three gate artifacts present: PHASE-1-COMPLETE + PHASE-2-COMPLETE + PHASE-3-COMPLETE.

Phases 2 and 3 derived their output from the manifest. If any derived section contradicts the manifest, the manifest takes precedence and the derived section must be corrected.

If AMEND mode was declared: confirm every section included an explicit out-of-scope notation for excluded signal types.
```

---

**Variation axis summary:**

| Variation | Primary axis | Secondary axis | Key structural bets |
|-----------|-------------|----------------|---------------------|
| V-01 | Role sequence — Echo-first | — | Locked nomination before audit; disqualification gate cross-references Step 1 vs Step 2 |
| V-02 | Output format — Audit manifest | — | Manifest as primary artifact; backward recovery tables A+B derived from WRONG rows; C-38 structural |
| V-03 | Lifecycle emphasis — Phase gates | — | C-38 and C-39 named as explicit gate conditions in Phase 1 exit checklist; cannot sign without them |
| V-04 | Role sequence — Echo-first | Phrasing register — challenge voice | Adversarial interrogation of nomination; "Is this part of a pattern?" as named structural field |
| V-05 | Output format — Audit manifest | Lifecycle emphasis — Phase gates | Three-phase manifest+derivation architecture; Phase 2 gate cites backward recovery table presence |
