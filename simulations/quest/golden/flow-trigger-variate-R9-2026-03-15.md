---
skill: flow-trigger
round: 9
date: 2026-03-15
rubric_version: 9
new_criteria: [C-30]
---

# flow-trigger — Round 9 Variations

**New criterion this round:**
- **C-30** ADR register Required Block Label column — pre-specifies the exact instruction block label text for each register entry, reducing ADR-to-block correspondence from a semantic match to a string-match operation; a reader verifies compliance by confirming the Required Block Label string appears verbatim as a structural header in the corresponding phase

C-30 elevates an evidence pattern cited in the C-22 discussion of R8 variations (V-02 scored it) but never declared as its own structural criterion. The full protocol hierarchy now requires: phase-scoped IDs (C-22) → named block labels (C-23) → bidirectional rule (C-25) → **Required Block Label column pre-specifying the exact expected string** (C-30).

**Variation axes used:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence — Auditor constructs and locks the Required Block Label column before Expert begins | Requiring the Auditor to pre-specify exact label strings at the register-construction step makes label deviations in the Expert role detectable as inter-role gate violations rather than post-hoc findings |
| V-02 | Output format — ADR register table schema pre-filled with Required Block Label values as a typed contract | Presenting the full table with Required Block Label pre-populated forces the model to treat label matching as a copy operation, not an inference — making the exact-string requirement structurally visible in the prompt template itself |
| V-03 | Phrasing register — Required Block Label declared as a governing law article with explicit string-equality constraint | Framing label exactness as a law ("SHALL equal", "non-compliance is a Declaration violation") creates a refutable rule rather than a procedural instruction, making deviations violations rather than mistakes |
| V-04 | Role sequence + Lifecycle emphasis — Auditor ADR construction step weighted with extended sub-step scaffolding | Giving the ADR construction step proportionally more structural space (sub-steps, required-label derivation rule, self-verification element) increases the probability the Required Block Label column is fully populated before Expert execution begins |
| V-05 | Output format + Inertia framing — Required Block Label contrasted against naive semantic-matching baseline | Naming what a naive protocol produces (ADR with phase IDs but no pre-specified label strings, correspondence verified by reading) gives the Required Block Label column a concrete improvement target — the contrast makes the structural gain from C-30 explicit |

---

## V-01

**Variation axis:** Role sequence — Auditor constructs and locks Required Block Label column before Expert begins
**Hypothesis:** When the Auditor role is required to populate the Required Block Label column as a named construction step, and the inter-role gate checks that the column is non-empty for every ADR entry, the Expert role inherits exact label strings as a contract rather than discovering the correspondence requirement during execution. The gate makes incomplete label pre-specification a detectable pre-execution failure rather than a per-phase oversight.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following two roles in sequence. The Auditor role completes first. The Domain Expert role may not begin until the Auditor Declaration Gate is issued.

---

## ROLE A: AUDITOR

**The Auditor produces no analytical content about the record change.** The Auditor builds the structural foundation the Domain Expert will execute against. All Auditor output is protocol infrastructure.

### A-1. Failure Mode Catalog

The following catalog names structural deficiencies this protocol prevents. Every entry is a citable violation identifier. A response exhibiting FM-NN behavior after declaring this catalog incurs a compounded failure — the defect was named before it occurred.

| FM-ID | Failure Mode |
|-------|-------------|
| FM-01 | Trigger listed without input payload or output action |
| FM-02 | Sync/async not separated — single flat enumeration |
| FM-03 | Pathology class answered without investigation case opened and closed |
| FM-04 | Enumeration begins without pre-declared ghost denominator candidate list |
| FM-05 | Protocol ends without reconcile-and-close phase |
| FM-06 | GD count reported globally without per-tier split |
| FM-07 | Verdict taxonomy absent — "not found" used as terminal disposition |
| FM-08 | Tier assigned at enumeration time rather than from pre-declared manifest |
| FM-09 | Case closed without verbatim citation of opening evidence standard |
| FM-10 | Phase entered without gate check on prior-phase deliverables |
| FM-11 | Analytical dimension register absent — phases declare dimensions independently |
| FM-12 | Instruction block present without corresponding ADR register entry |
| FM-13 | ADR register lacks Required Block Label column — correspondence is semantic, not string-match |
| FM-14 | Instruction block label deviates from Required Block Label value — string equality violated |

### A-2. Verdict Taxonomy — Term Set V

Declare this taxonomy before any candidate is evaluated. Every ghost denominator entry must receive exactly one verdict from Term Set V. Using a verdict without meeting its evidence requirement is a Term Set violation.

| Verdict | Code | Evidence Required |
|---------|------|------------------|
| FIRED | V-F | Affirmative activation evidence: the specific field or event matches the trigger's configured activation condition and the trigger is enabled |
| CONFIRMED ABSENT | V-CA | Structural argument — one of: (a) scope exclusion: trigger not configured for this entity/table; (b) condition analysis: activation condition evaluates FALSE; (c) reachability: execution path does not reach trigger for this change type |
| FLAGGED MISSING | V-FM | Detection gap: expected behavior or design intent suggests a trigger should exist or fire but cannot be confirmed or ruled out |

**Anti-examples — these are NOT valid V-CA closures:**
- "No trigger found" — absence of evidence is not a structural argument; use V-FM
- "Does not apply" — no structural basis named; provide scope exclusion or condition argument
- "Not relevant" — assertion without evidence; assign V-FM or state the condition argument

FM-07 applies if Term Set V is absent or if V-CA is used without a structural argument.

### A-3. Tier Assignment Manifest

Tier assignments will be established after the ghost denominator scan in Phase 2. The manifest structure is declared here; it is populated there.

```
TIER MANIFEST
═══════════════════════════════════════════════════════
SYNC_IDS  : []   ← populate after ghost denominator scan in Phase 2
ASYNC_IDS : []   ← populate after ghost denominator scan in Phase 2
───────────────────────────────────────────────────────
TOTAL_COUNT   : 0   ← total GD candidates
SYNC_COUNT    : 0   ← |SYNC_IDS|
ASYNC_COUNT   : 0   ← |ASYNC_IDS|
TOTAL_CHECK   : SYNC_COUNT + ASYNC_COUNT = TOTAL_COUNT → [YES / NO]
═══════════════════════════════════════════════════════
GATE: Phase 3 may not begin if TOTAL_CHECK ≠ YES.
FM-06 if counts are global only. FM-08 if tier is assigned during enumeration.
```

### A-4. Analytical Dimension Register (ADR) with Required Block Labels

**Required Block Label column construction rule:** For each ADR entry, the Required Block Label is the exact string that MUST appear as a named structural header in the Domain Expert's corresponding phase. Construct each value as: `ANALYTICAL INSTRUCTIONS [ADR-xx]` where `xx` is the ADR-ID suffix. This string must be used verbatim — no synonym, paraphrase, or abbreviation. The Domain Expert MAY NOT substitute an equivalent label.

**Governing constraints:**
- Every ADR entry → must have a named instruction block whose label exactly equals the Required Block Label value (register → block)
- Every instruction block → must cite a valid ADR-ID from this register (block → register)
- Violations are detectable by string comparison of Required Block Label column value against response headers

**FM-13 applies if the Required Block Label column is absent. FM-14 applies if any instruction block label deviates from its Required Block Label value.**

| ADR-ID | Analytical Dimension | Assigned Phase | Required Block Label |
|--------|---------------------|----------------|---------------------|
| ADR-1a | Investigation cases — evidence standard per pathology class | Phase 1 | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | Ghost denominator scan — all candidates with Term Set V disposition | Phase 2 | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | Trigger enumeration — sync tier (firing order, I/O, branch resolution, latency) | Phase 3 | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | Trigger enumeration — async tier (firing order, I/O, delay estimate) | Phase 3 | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | Cascading side-effect trace (≥ L1) per V-F trigger | Phase 4 | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | Investigation case closure with verbatim evidence standard citation | Phase 4 | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | Risk-ranked pathology summary with one-line mitigation per instance | Phase 5 | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

**Auditor Required Block Label Verification:**
- [ ] Every ADR entry has a non-empty Required Block Label value
- [ ] All Required Block Label values follow the form `ANALYTICAL INSTRUCTIONS [ADR-xx]`
- [ ] No two entries share the same Required Block Label value

### AUDITOR DECLARATION GATE

Domain Expert may not begin Phase 1 until this gate is satisfied. Verify each condition:

- [ ] FM catalog declared — 14 entries (FM-01 through FM-14)
- [ ] Term Set V declared with anti-examples — 3 verdicts
- [ ] Tier Manifest structure declared
- [ ] ADR register complete — 7 entries with Required Block Label column fully populated, all values non-empty and distinct
- [ ] Required Block Label column verification passed (3 checks above)
- [ ] Governing constraints stated: register → block and block → register

**AUDITOR DECLARATION: Gate satisfied. Domain Expert execution authorized.**

---

## ROLE B: DOMAIN EXPERT (Power Automate / Copilot Studio)

Execute the five analytical phases using Power Automate and Copilot Studio vocabulary. Instruction blocks MUST use the exact Required Block Label strings from the ADR register. Deviation from a Required Block Label string is FM-14 — a string-equality violation detectable without semantic interpretation.

### Phase 1: Investigation Case Opening

**PHASE ENTRY GATE — Phase 1:**
- [ ] Auditor Declaration Gate issued and all conditions checked
- [ ] Prohibition: Do not list, name, or evaluate any trigger in Phase 1

**`ANALYTICAL INSTRUCTIONS [ADR-1a]`**
Open three named investigation cases. For each case, state the evidence standard as a specific, falsifiable condition — not a judgment. This text will be cited verbatim at closure in Phase 4.

| Case ID | Pathology Class | Evidence Standard for Closure |
|---------|----------------|-------------------------------|
| CASE-STORM | Trigger Storm | A storm is confirmed when: |
| CASE-MISSING | Missing Trigger | A missing trigger is confirmed when: |
| CASE-CIRCULAR | Circular Trigger | A circular trigger is confirmed when: |

**REGISTER CHECK — Phase 1:**
- [ ] ADR-1a: Three cases open; evidence standards stated in full; label used: `ANALYTICAL INSTRUCTIONS [ADR-1a]` ✓
Phase 1 is complete when this check passes.

---

### Phase 2: Ghost Denominator Pre-Scan

**PHASE ENTRY GATE — Phase 2:**
- [ ] Phase 1 REGISTER CHECK passed; three cases open with evidence standards
- [ ] Prohibition: Do not describe any trigger's firing behavior or inputs/outputs in Phase 2

**`ANALYTICAL INSTRUCTIONS [ADR-2a]`**
List every trigger candidate plausibly relevant to this change. Include candidates expected to be absent. Assign GD-IDs. Assign each candidate exactly one verdict from Term Set V per the Auditor declaration. No candidate may remain without a verdict. An omission here is FM-04.

| GD-ID | Candidate Trigger | Verdict [Term Set V] | Structural Basis |
|-------|------------------|---------------------|-----------------|

Caption: Ghost denominator. Verdict ∈ Term Set V = {V-F, V-CA, V-FM}. Violations: `[NC: TermSet-V value]`.

**Manifest update:** After GD table is complete, populate the Tier Manifest in Role A § A-3 with SYNC_IDS and ASYNC_IDS. Run TOTAL_CHECK. Do not proceed to Phase 3 if TOTAL_CHECK ≠ YES.

**REGISTER CHECK — Phase 2:**
- [ ] ADR-2a: All candidates listed; every entry has Term Set V verdict; Tier Manifest updated; TOTAL_CHECK = YES; label used: `ANALYTICAL INSTRUCTIONS [ADR-2a]` ✓
Phase 2 is complete when this check passes.

---

### Phase 3: Trigger Enumeration (Sync / Async Tier-Split)

**PHASE ENTRY GATE — Phase 3:**
- [ ] Phase 2 REGISTER CHECK passed; N ≥ 1 V-F entries present
- [ ] Tier Manifest TOTAL_CHECK = YES; SYNC_IDS and ASYNC_IDS populated
- [ ] Prohibition: Do not introduce any GD-ID not in the Phase 2 GD table; do not re-determine tier

**`ANALYTICAL INSTRUCTIONS [ADR-3a]`**
Enumerate synchronous tier. Derive tier membership from TIER MANIFEST SYNC_IDS — do not re-evaluate. Order by firing sequence (first → last). For conditional triggers: state Branch Executed and Condition Evaluated. Input Payload: exact fields consumed. Output Action: exact action produced — no generic entries. FM-01 applies to generic I/O. FM-02 applies if tiers are merged.

### SYNC TIER (derived from TIER MANIFEST SYNC_IDS)

Caption: Synchronous execution tier. Status ∈ Term Set TS = {Active, Conditional-passes, Conditional-fails, Inactive}. Violations: `[NC: TermSet-TS value]`.

| GD-ID | Trigger Name | Status [TS] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Latency Impact |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**`ANALYTICAL INSTRUCTIONS [ADR-3b]`**
Enumerate asynchronous tier. Derive membership from TIER MANIFEST ASYNC_IDS. Same I/O requirements as sync tier. Delay Estimate column replaces Latency Impact — semantically distinct: scheduling window semantics vs immediate execution semantics. FM-02 applies if merged with sync tier.

### ASYNC TIER (derived from TIER MANIFEST ASYNC_IDS)

Caption: Asynchronous execution tier. Status ∈ Term Set TA = {Queued, Deferred, Skipped}. Violations: `[NC: TermSet-TA value]`.

| GD-ID | Trigger Name | Status [TA] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Delay Estimate |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**REGISTER CHECK — Phase 3:**
- [ ] ADR-3a: Sync tier complete; firing order declared; no generic I/O; all SYNC_IDS present; label ✓
- [ ] ADR-3b: Async tier complete; ASYNC_IDS present; Delay Estimate column semantically distinct; label ✓
Phase 3 is complete when both checks pass.

---

### Phase 4: Reconcile and Close

**PHASE ENTRY GATE — Phase 4:**
- [ ] Phase 3 REGISTER CHECK passed; both tier tables complete
- [ ] Phase 1 CASE table available for verbatim evidence standard citation
- [ ] Phase 2 GD table available — V-FM entries needed for CASE-MISSING review

**`ANALYTICAL INSTRUCTIONS [ADR-4a]`**
For every V-F trigger, trace cascading side effects at least one level deep. Format: `[Trigger] → [Side Effect L1] → [Downstream L2 or "terminal"]`. Do not skip any FIRED trigger. FM-05 applies if this phase is absent.

| Trigger Name | Side Effect (L1) | Downstream (L2) |
|---|---|---|

**`ANALYTICAL INSTRUCTIONS [ADR-4b]`**
Close each investigation case. At closure, cite the **verbatim** evidence standard text from Phase 1. FM-09 applies if closure uses paraphrase or judgment rather than the exact stated standard.

> CASE [ID]: [CONFIRMED ABSENT / INSTANCE FOUND — describe].
> Evidence standard applied: "[exact text from Phase 1 CASE table]"

**REGISTER CHECK — Phase 4:**
- [ ] ADR-4a: Side-effect chains traced for all V-F triggers; label ✓
- [ ] ADR-4b: All three cases closed; each closure cites verbatim evidence standard; label ✓
Phase 4 is complete when both checks pass.

---

### Phase 5: Risk Summary

**PHASE ENTRY GATE — Phase 5:**
- [ ] Phase 4 REGISTER CHECK passed; all cases closed; all GD entries resolved to Term Set V verdict

**`ANALYTICAL INSTRUCTIONS [ADR-5a]`**
List all confirmed pathology instances ranked by operational risk. If none confirmed, state: "No pathologies confirmed. All three cases closed without findings."

| Pathology Class | Instance | Risk [Term Set RK] | Mitigation (one sentence) |
|---|---|---|---|

Caption: Risk summary. Risk ∈ Term Set RK = {High, Medium, Low}. Violations: `[NC: TermSet-RK value]`.

**REGISTER CHECK — Phase 5:**
- [ ] ADR-5a: Confirmed pathologies listed; risk ranked; mitigations present; label ✓
Phase 5 is complete when this check passes.

---

### FINAL BIDIRECTIONAL AUDIT

Whole-protocol verification:

(a) **Register → Block:** Every ADR entry in Role A § A-4 has a corresponding instruction block whose label exactly equals the Required Block Label value.

| ADR-ID | Required Block Label | Block Found (exact string match) |
|--------|---------------------|----------------------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` | |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` | |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` | |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` | |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` | |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` | |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` | |

(b) **Block → Register:** Every instruction block above cites a valid ADR-ID from the register.

Bidirectional consistency contract satisfied. FM-13/FM-14 not triggered. ✓

---

## V-02

**Variation axis:** Output format — ADR register table schema pre-filled with Required Block Label values as a typed contract
**Hypothesis:** When the ADR register is presented as a table with the Required Block Label column already populated with exact strings (not placeholders), the Domain Expert treats label assignment as a copy operation rather than a derivation. The format contract makes the exact-string requirement visible without requiring the model to infer it from a rule description — the expected label string is present in the prompt as data, not as an instruction.

---

You are a Power Automate / Copilot Studio domain expert.

A record change has occurred. Analyze which automations fire, their order, inputs, outputs, and any trigger pathologies (storms, missing triggers, circular triggers).

---

## PRE-EXECUTION BLOCK

Complete this block before any phase executes. This block contains no content specific to the provided record change — it is protocol infrastructure only.

### Failure Mode Catalog

| FM-ID | Named Failure Mode |
|-------|-------------------|
| FM-01 | Trigger listed without input payload or output action |
| FM-02 | Sync/async not separated |
| FM-03 | Pathology class answered without opened and closed investigation case |
| FM-04 | Enumeration begins without pre-declared ghost denominator list |
| FM-05 | Protocol ends without reconcile-and-close phase |
| FM-06 | GD count global only, no per-tier split |
| FM-07 | Verdict taxonomy absent or V-CA used without structural argument |
| FM-08 | Tier assigned at enumeration time, no pre-declared manifest |
| FM-09 | Case closed without verbatim citation of opening evidence standard |
| FM-10 | Phase entered without gate check |
| FM-11 | ADR absent — phases declare dimensions independently |
| FM-12 | Instruction block present with no corresponding ADR entry |
| FM-13 | ADR lacks Required Block Label column — correspondence is semantic |
| FM-14 | Instruction block label deviates from Required Block Label — string equality violated |

### Verdict Taxonomy — Term Set V

```
TERM SET V
──────────────────────────────────────────────────────
V-F   FIRED
      Evidence: field/event matches configured activation condition; trigger enabled

V-CA  CONFIRMED ABSENT
      Evidence: ONE structural argument —
        (a) scope exclusion: not configured for this entity/table
        (b) condition analysis: activation condition evaluates FALSE
        (c) reachability: execution path does not reach trigger
      Anti-example: "Not found" → INVALID (no structural arg) → assign V-FM
      Anti-example: "Does not apply" → INVALID → name the argument

V-FM  FLAGGED MISSING
      Evidence: named detection gap — expected behavior suggests trigger
      should fire but cannot be confirmed or ruled out structurally
──────────────────────────────────────────────────────
FM-07 if taxonomy absent or V-CA used without structural argument.
```

### Tier Assignment Manifest

```
TIER MANIFEST
═══════════════════════════════════════════════════════
SYNC_IDS  : []            ← fill after Phase 2 GD scan
ASYNC_IDS : []            ← fill after Phase 2 GD scan
───────────────────────────────────────────────────────
TOTAL_COUNT   : 0
SYNC_COUNT    : 0
ASYNC_COUNT   : 0
TOTAL_CHECK   : SYNC_COUNT + ASYNC_COUNT = TOTAL_COUNT → [YES / NO]
═══════════════════════════════════════════════════════
Phase 3 gate: TOTAL_CHECK must equal YES. FM-06, FM-08 if bypassed.
```

### Analytical Dimension Register (ADR) — Full Schema

The following table is the complete ADR. The **Required Block Label** column is pre-specified — these are the exact strings that must appear as named structural headers in the corresponding phase. This is not a format suggestion. It is a string contract.

**Contract rule:** The instruction block label in Phase N must equal the Required Block Label string in this table. Compliance is verified by string comparison. FM-13 if this column is absent. FM-14 if any label deviates.

| ADR-ID | Analytical Dimension | Assigned Phase | Required Block Label |
|--------|---------------------|----------------|---------------------|
| ADR-1a | Investigation cases — evidence standard per pathology class | Phase 1 | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | Ghost denominator — all candidates with Term Set V disposition | Phase 2 | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | Sync tier enumeration — firing order, I/O, branch resolution, latency | Phase 3 | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | Async tier enumeration — firing order, I/O, delay estimate | Phase 3 | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | Side-effect trace (≥ L1) per V-F trigger | Phase 4 | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | Investigation case closure with verbatim evidence citation | Phase 4 | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | Risk-ranked pathology summary with one-line mitigation | Phase 5 | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

**Bidirectional constraint:** register → block (every ADR-ID has a block with the Required Block Label string verbatim) AND block → register (every instruction block cites a valid ADR-ID). Violations detectable by string comparison.

---

## PHASE 1: INVESTIGATION CASE OPENING

**ENTRY GATE:**
- [ ] Pre-Execution Block complete: FM catalog (14 entries), Term Set V (3 verdicts, anti-examples), Tier Manifest declared, ADR complete (7 entries, Required Block Label column fully populated)
- [ ] Prohibition: Do not list, name, or evaluate any trigger in Phase 1

**`ANALYTICAL INSTRUCTIONS [ADR-1a]`** *(Required Block Label — use this string verbatim)*
Open three named investigation cases. State evidence standard as a specific falsifiable condition. This text will be cited verbatim at closure in Phase 4.

| Case ID | Pathology Class | Evidence Standard for Closure |
|---------|----------------|-------------------------------|
| CASE-STORM | Trigger Storm | A storm is confirmed when: |
| CASE-MISSING | Missing Trigger | A missing trigger is confirmed when: |
| CASE-CIRCULAR | Circular Trigger | A circular trigger is confirmed when: |

**REGISTER CHECK — Phase 1:** ADR-1a addressed. Label match: `ANALYTICAL INSTRUCTIONS [ADR-1a]` ✓

---

## PHASE 2: GHOST DENOMINATOR PRE-SCAN

**ENTRY GATE:**
- [ ] Phase 1 REGISTER CHECK passed; three cases open with evidence standards
- [ ] Prohibition: Do not describe firing behavior in Phase 2

**`ANALYTICAL INSTRUCTIONS [ADR-2a]`** *(Required Block Label — use this string verbatim)*
List every trigger candidate plausibly relevant to this change. Assign GD-IDs. Assign Term Set V verdict. No omissions — an absent candidate is FM-04.

| GD-ID | Candidate Trigger | Verdict [Term Set V] | Structural Basis |
|-------|------------------|---------------------|-----------------|

Caption: Ghost denominator. Verdict ∈ {V-F, V-CA, V-FM}. Violations: `[NC: TermSet-V value]`.

After completing the GD table: populate TIER MANIFEST SYNC_IDS and ASYNC_IDS. Verify TOTAL_CHECK = YES. Do not proceed to Phase 3 without it.

**REGISTER CHECK — Phase 2:** ADR-2a addressed. Label match: `ANALYTICAL INSTRUCTIONS [ADR-2a]` ✓

---

## PHASE 3: TRIGGER ENUMERATION (SYNC / ASYNC)

**ENTRY GATE:**
- [ ] Phase 2 REGISTER CHECK passed; N ≥ 1 V-F entries; TOTAL_CHECK = YES
- [ ] Prohibition: Do not introduce GD-IDs not in Phase 2; do not re-determine tier

**`ANALYTICAL INSTRUCTIONS [ADR-3a]`** *(Required Block Label — use this string verbatim)*
Synchronous tier — derive from TIER MANIFEST SYNC_IDS. Order by firing sequence. Exact I/O required. FM-01 for generic entries.

### SYNC TIER

Caption: Synchronous. Status ∈ Term Set TS = {Active, Conditional-passes, Conditional-fails, Inactive}. Violations: `[NC: TermSet-TS value]`.

| GD-ID | Trigger Name | Status [TS] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Latency Impact |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**`ANALYTICAL INSTRUCTIONS [ADR-3b]`** *(Required Block Label — use this string verbatim)*
Asynchronous tier — derive from TIER MANIFEST ASYNC_IDS. Delay Estimate column (scheduling window semantics, distinct from Latency Impact). FM-02 if merged with sync.

### ASYNC TIER

Caption: Asynchronous. Status ∈ Term Set TA = {Queued, Deferred, Skipped}. Violations: `[NC: TermSet-TA value]`.

| GD-ID | Trigger Name | Status [TA] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Delay Estimate |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**REGISTER CHECK — Phase 3:** ADR-3a, ADR-3b addressed. Labels match ✓

---

## PHASE 4: RECONCILE AND CLOSE

**ENTRY GATE:**
- [ ] Phase 3 REGISTER CHECK passed; both tier tables complete
- [ ] Phase 1 case evidence standards available for verbatim citation

**`ANALYTICAL INSTRUCTIONS [ADR-4a]`** *(Required Block Label — use this string verbatim)*
Trace cascading side effects for every V-F trigger at ≥ L1 depth. Format: `[Trigger] → [Side Effect L1] → [Downstream L2 or "terminal"]`.

| Trigger Name | Side Effect (L1) | Downstream (L2) |
|---|---|---|

**`ANALYTICAL INSTRUCTIONS [ADR-4b]`** *(Required Block Label — use this string verbatim)*
Close each investigation case. Cite verbatim evidence standard from Phase 1. FM-09 if paraphrase is used.

> CASE [ID]: [disposition]. Evidence standard applied: "[exact text from Phase 1]"

**REGISTER CHECK — Phase 4:** ADR-4a, ADR-4b addressed. Labels match ✓

---

## PHASE 5: RISK SUMMARY

**ENTRY GATE:**
- [ ] Phase 4 REGISTER CHECK passed; all cases closed; all GD entries resolved

**`ANALYTICAL INSTRUCTIONS [ADR-5a]`** *(Required Block Label — use this string verbatim)*
Risk-ranked pathology summary. If no pathologies confirmed: "No pathologies confirmed. All three cases closed without findings."

| Pathology Class | Instance | Risk [Term Set RK] | Mitigation |
|---|---|---|---|

Caption: Risk ∈ Term Set RK = {High, Medium, Low}. Violations: `[NC: TermSet-RK value]`.

**REGISTER CHECK — Phase 5:** ADR-5a addressed. Label match ✓

---

## FINAL BIDIRECTIONAL AUDIT

(a) Register → Block — every Required Block Label string appears verbatim in the response:

| ADR-ID | Required Block Label | Present (exact string) |
|--------|---------------------|------------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` | |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` | |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` | |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` | |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` | |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` | |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` | |

(b) Block → Register — every instruction block cites a valid ADR-ID. ✓

FM-13 not triggered (Required Block Label column present). FM-14 not triggered (all labels match). Protocol complete.

---

## V-03

**Variation axis:** Phrasing register — Required Block Label constraint declared as a governing law article with explicit string-equality rule
**Hypothesis:** When label exactness is framed as a law ("SHALL equal", "a deviation is a Declaration violation"), the model treats non-matching labels as structural violations rather than minor formatting variations. Governing law framing creates a refutable rule against which the model's output can be tested — the declaration exists in the prompt as a falsifiable assertion, making deviations harder to produce accidentally than when the same requirement is stated as a procedural instruction.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Determine exactly which automations fire, their order, inputs/outputs, and all trigger pathologies (storms, missing triggers, circular triggers).

Before any analytical phase executes, the following declarations are issued as governing law. Declarations are binding constraints — not instructions. Deviation from a declaration is a structural violation detectable against the declaration text itself.

---

## GOVERNING DECLARATIONS

### Declaration 1 — Failure Mode Law

The following failure modes are declared binding. A response that exhibits FM-NN behavior after issuing this declaration incurs a documented structural violation.

| FM-ID | Violation |
|-------|-----------|
| FM-01 | Trigger listed without input payload or output action |
| FM-02 | Sync/async tiers merged |
| FM-03 | Pathology answered without opened and closed case |
| FM-04 | Enumeration without pre-declared ghost denominator list |
| FM-05 | Protocol ends without reconcile-and-close phase |
| FM-06 | GD count global, no per-tier split |
| FM-07 | Verdict taxonomy absent or V-CA used without structural argument |
| FM-08 | Tier assigned during enumeration rather than from pre-declared manifest |
| FM-09 | Case closed without verbatim citation of opening evidence standard |
| FM-10 | Phase entered without gate check |
| FM-11 | ADR absent |
| FM-12 | Instruction block with no corresponding ADR entry |
| FM-13 | ADR lacks Required Block Label column — ADR-to-block correspondence is semantic |
| FM-14 | Instruction block label deviates from Required Block Label string — string equality violated |

### Declaration 2 — Verdict Law

The following term set governs ALL trigger disposition decisions. No disposition outside Term Set V is valid.

| Code | Verdict | Evidence Law |
|------|---------|-------------|
| V-F | FIRED | SHALL require: affirmative activation evidence — field/event matches configured condition; trigger enabled |
| V-CA | CONFIRMED ABSENT | SHALL require: structural argument — scope exclusion, condition analysis evaluates FALSE, or reachability argument; "not found" is not structural; V-CA without structural argument is a Declaration 2 violation |
| V-FM | FLAGGED MISSING | SHALL require: named detection gap — expected behavior suggests trigger should fire but cannot be confirmed or ruled out |

### Declaration 3 — Label Exactness Law

**The Required Block Label column in the ADR register pre-specifies the exact text that SHALL appear as a named structural header in the corresponding phase. Label matching SHALL be a string-equality operation. A label that paraphrases, abbreviates, or synonymizes the Required Block Label value is a Declaration 3 violation — FM-14.**

Formal statement: ∀ ADR entry e: label(instruction_block(e)) = RequiredBlockLabel(e)

Compliance verification: a reader confirms compliance by finding the Required Block Label string verbatim in the response. No semantic interpretation is required. No semantic interpretation is permitted as a substitute for string equality.

### Declaration 4 — Sequencing Law

Phases execute in declared order. No phase may begin until its entry gate conditions are satisfied. Entry gate conditions reference specific prior-phase deliverables — they are verifiable preconditions, not prohibitions on content. Declaration 4 violation: entering a phase when its entry gate conditions are not met.

### Declaration 5 — Bidirectional Consistency Law

The ADR register and instruction blocks SHALL maintain bidirectional correspondence:
- (register → block): Every ADR entry SHALL have a corresponding instruction block whose label exactly equals the Required Block Label value
- (block → register): Every instruction block SHALL cite a valid ADR-ID from the register

Violations are detectable by ID cross-reference and string comparison. Declaration 5 violation: any ADR entry without a corresponding instruction block, or any instruction block without a valid ADR-ID citation.

---

## PRE-EXECUTION REGISTER: Analytical Dimensions

Declared before any phase executes. Each dimension assigned a phase-scoped identifier. Required Block Label pre-specifies the exact string demanded by Declaration 3.

| ADR-ID | Analytical Dimension | Phase | Required Block Label |
|--------|---------------------|-------|---------------------|
| ADR-1a | Investigation cases — evidence standard per pathology class | 1 | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | Ghost denominator — all candidates with Term Set V disposition | 2 | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | Sync tier — firing order, input payload, output action, latency, branch resolution | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | Async tier — firing order, input payload, output action, delay estimate | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | Side-effect trace ≥ L1 per V-F trigger | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | Case closure with verbatim evidence standard citation | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | Risk-ranked pathology summary with one-line mitigation | 5 | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

Declaration 3 applies to every Required Block Label value above. Declaration 5 applies to the full register.

## PRE-EXECUTION REGISTER: Tier Assignment Manifest

```
TIER MANIFEST
═══════════════════════════════════════════════════════
SYNC_IDS  : []   ← populate after Phase 2
ASYNC_IDS : []   ← populate after Phase 2
───────────────────────────────────────────────────────
TOTAL_COUNT   : 0
SYNC_COUNT    : 0
ASYNC_COUNT   : 0
TOTAL_CHECK   : SYNC_COUNT + ASYNC_COUNT = TOTAL_COUNT → [YES / NO]
═══════════════════════════════════════════════════════
Declaration 4 violation if Phase 3 begins with TOTAL_CHECK ≠ YES.
```

---

## PHASE 1: INVESTIGATION CASE OPENING

**ENTRY GATE — Phase 1:**
Declaration 4: Pre-execution registers (ADR, Tier Manifest, all 5 Declarations) must be present and complete.
Declaration 4: Prohibition — Do not list, evaluate, or name any trigger in Phase 1.

**`ANALYTICAL INSTRUCTIONS [ADR-1a]`**
*(Declaration 3 applies: this label must equal `ANALYTICAL INSTRUCTIONS [ADR-1a]` exactly. No other string satisfies Declaration 3 for ADR-1a.)*

Open three named investigation cases. State each evidence standard as a specific, falsifiable condition. Cite verbatim at Phase 4 closure.

| Case ID | Pathology Class | Evidence Standard |
|---------|----------------|-------------------|
| CASE-STORM | Trigger Storm | |
| CASE-MISSING | Missing Trigger | |
| CASE-CIRCULAR | Circular Trigger | |

**REGISTER CHECK — Phase 1:**
Declaration 5 check: ADR-1a block present with exact Required Block Label string. ✓
Phase 1 complete.

---

## PHASE 2: GHOST DENOMINATOR PRE-SCAN

**ENTRY GATE — Phase 2:**
Declaration 4: Phase 1 REGISTER CHECK passed; three cases open.
Declaration 4: Prohibition — Do not describe trigger firing behavior in Phase 2.

**`ANALYTICAL INSTRUCTIONS [ADR-2a]`**
*(Declaration 3 applies: exact string required.)*

List all trigger candidates. Assign GD-IDs. Assign Term Set V verdict per Declaration 2. No candidate may be omitted — FM-04.

| GD-ID | Candidate Trigger | Verdict [Term Set V] | Structural Basis |
|-------|------------------|---------------------|-----------------|

Caption: Verdict ∈ {V-F, V-CA, V-FM}. Non-compliant values: `[NC: TermSet-V value]`.

After GD table: update Tier Manifest SYNC_IDS / ASYNC_IDS. Verify TOTAL_CHECK = YES. Declaration 4 violation if Phase 3 begins with TOTAL_CHECK ≠ YES.

**REGISTER CHECK — Phase 2:** ADR-2a: Declaration 5 ✓

---

## PHASE 3: TRIGGER ENUMERATION

**ENTRY GATE — Phase 3:**
Declaration 4: Phase 2 REGISTER CHECK passed; N ≥ 1 V-F entries; TOTAL_CHECK = YES.
Declaration 4: Prohibition — Do not introduce GD-IDs not in Phase 2; do not re-evaluate tier assignments.

**`ANALYTICAL INSTRUCTIONS [ADR-3a]`**
*(Declaration 3 applies.)*

Synchronous tier from TIER MANIFEST SYNC_IDS. Firing order: first to last. Exact I/O. Declaration 1 FM-01 if generic. Declaration 2 applied at V-CA decisions.

### SYNC TIER

Caption: Status ∈ Term Set TS = {Active, Conditional-passes, Conditional-fails, Inactive}.

| GD-ID | Trigger Name | Status [TS] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Latency Impact |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**`ANALYTICAL INSTRUCTIONS [ADR-3b]`**
*(Declaration 3 applies.)*

Asynchronous tier from TIER MANIFEST ASYNC_IDS. Delay Estimate column (scheduling window semantics). Declaration 3 violation if column is named "Latency Impact" — string equality demanded in column naming as well as in label matching.

### ASYNC TIER

Caption: Status ∈ Term Set TA = {Queued, Deferred, Skipped}.

| GD-ID | Trigger Name | Status [TA] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Delay Estimate |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**REGISTER CHECK — Phase 3:** ADR-3a, ADR-3b: Declaration 5 ✓

---

## PHASE 4: RECONCILE AND CLOSE

**ENTRY GATE — Phase 4:**
Declaration 4: Phase 3 REGISTER CHECK passed; Phase 1 evidence standards available.

**`ANALYTICAL INSTRUCTIONS [ADR-4a]`**
*(Declaration 3 applies.)*

Side-effect trace for every V-F trigger. Minimum depth L1. `[Trigger] → [L1] → [L2 or terminal]`.

| Trigger Name | Side Effect (L1) | Downstream (L2) |
|---|---|---|

**`ANALYTICAL INSTRUCTIONS [ADR-4b]`**
*(Declaration 3 applies.)*

Close CASE-STORM, CASE-MISSING, CASE-CIRCULAR. Citation SHALL be verbatim — Declaration 1 FM-09 if paraphrased.

> CASE [ID]: [disposition]. Evidence standard applied: "[verbatim from Phase 1]"

**REGISTER CHECK — Phase 4:** ADR-4a, ADR-4b: Declaration 5 ✓

---

## PHASE 5: RISK SUMMARY

**ENTRY GATE — Phase 5:**
Declaration 4: Phase 4 REGISTER CHECK passed; all cases closed.

**`ANALYTICAL INSTRUCTIONS [ADR-5a]`**
*(Declaration 3 applies.)*

Risk-ranked pathology summary. No findings: "No pathologies confirmed."

| Pathology Class | Instance | Risk [Term Set RK] | Mitigation |
|---|---|---|---|

Caption: Risk ∈ Term Set RK = {High, Medium, Low}.

**REGISTER CHECK — Phase 5:** ADR-5a: Declaration 5 ✓

---

## FINAL DECLARATION AUDIT

Declaration 5 whole-protocol verification:

(a) Register → Block — Required Block Label string appears verbatim for each ADR entry:

| ADR-ID | Required Block Label | Declaration 3 Status |
|--------|---------------------|----------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` | |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` | |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` | |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` | |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` | |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` | |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` | |

(b) Block → Register — all instruction blocks cite valid ADR-IDs.

No Declaration violations. Protocol complete under governing law.

---

## V-04

**Variation axes:** Role sequence + Lifecycle emphasis — Auditor constructs ADR with Required Block Label column using a weighted, sub-stepped construction process; pre-execution phases receive proportionally more instruction space
**Hypothesis:** When the ADR Required Block Label construction is broken into explicit sub-steps (enumerate dimensions, assign phase, derive label string by rule, verify uniqueness, verify non-emptiness), the model is more likely to produce a fully populated column with correct strings than when Required Block Label is stated as a column requirement in a single sentence. The Auditor/Expert split ensures this construction work is complete before any analysis begins — the heavier Auditor instruction space is structural load-bearing, not decoration.

---

You are running a structured trigger investigation protocol with two roles: **Auditor** and **Domain Expert**.

A record change has occurred. The Auditor builds the analytical infrastructure. The Domain Expert executes the investigation. The Domain Expert may not begin until the Auditor Declaration is issued.

---

## ROLE A: AUDITOR — PRE-EXECUTION INFRASTRUCTURE

**Prohibition: The Auditor produces no content about the record change. No trigger names. No firing analysis. No I/O descriptions. Auditor output is protocol infrastructure only.**

### A-1. Failure Mode Catalog

Declare before any role executes.

| FM-ID | Failure Mode | Phase Governed |
|-------|-------------|----------------|
| FM-01 | Trigger listed without input payload or output action | Phase 3 |
| FM-02 | Sync/async tiers merged into one enumeration | Phase 3 |
| FM-03 | Pathology class answered without opened and closed investigation case | Phase 4 |
| FM-04 | Enumeration begins without pre-declared ghost denominator list | Phase 2 |
| FM-05 | Protocol ends without reconcile-and-close phase | Phase 4 |
| FM-06 | GD count reported globally without per-tier split | Phase 2 |
| FM-07 | Verdict taxonomy absent or V-CA used without structural argument | Phase 2 |
| FM-08 | Tier assigned during enumeration — no pre-declared manifest | Phase 3 |
| FM-09 | Case closed without verbatim citation of opening evidence standard | Phase 4 |
| FM-10 | Phase entered without prior-phase gate check | All phases |
| FM-11 | ADR absent — phases declare dimensions independently | Pre-execution |
| FM-12 | Instruction block present without corresponding ADR entry | All phases |
| FM-13 | ADR lacks Required Block Label column — correspondence remains semantic | Pre-execution |
| FM-14 | Instruction block label deviates from Required Block Label — string equality violated | All phases |

### A-2. Verdict Taxonomy — Term Set V

| Code | Verdict | Evidence Required | Invalid Application |
|------|---------|------------------|---------------------|
| V-F | FIRED | Affirmative activation: field/event matches configured condition; trigger enabled | Asserted without naming matched condition |
| V-CA | CONFIRMED ABSENT | Structural argument (scope exclusion, condition FALSE, reachability) | "Not found", "Does not apply" without structural basis → assign V-FM |
| V-FM | FLAGGED MISSING | Named detection gap; expected behavior suggests trigger should fire but cannot be confirmed | Omitting a candidate rather than flagging it |

### A-3. Tier Assignment Manifest

```
TIER MANIFEST
═══════════════════════════════════════════════════════
SYNC_IDS  : []   ← Domain Expert populates after Phase 2
ASYNC_IDS : []   ← Domain Expert populates after Phase 2
───────────────────────────────────────────────────────
TOTAL_COUNT   : 0
SYNC_COUNT    : 0
ASYNC_COUNT   : 0
TOTAL_CHECK   : SYNC_COUNT + ASYNC_COUNT = TOTAL_COUNT → [YES / NO]
═══════════════════════════════════════════════════════
Phase 3 gate: TOTAL_CHECK = YES required. FM-06, FM-08 if bypassed.
```

### A-4. ADR Construction — Analytical Dimension Register with Required Block Labels

The ADR construction process has five sub-steps. Complete each sub-step before proceeding to the next.

**Sub-step A-4.1: Enumerate all analytical dimensions**

List every dimension of analysis the Domain Expert must perform across the full protocol. Group by phase.

Phase 1 dimensions:
- Investigation case opening with evidence standards

Phase 2 dimensions:
- Ghost denominator pre-scan with Term Set V dispositions

Phase 3 dimensions:
- Synchronous tier enumeration (firing order, I/O, branch resolution, latency semantics)
- Asynchronous tier enumeration (firing order, I/O, delay semantics)

Phase 4 dimensions:
- Side-effect trace ≥ L1 per V-F trigger
- Investigation case closure with verbatim evidence standard citation

Phase 5 dimensions:
- Risk-ranked pathology summary with one-line mitigations

**Sub-step A-4.2: Assign phase-scoped identifiers**

| Dimension | Phase | ADR-ID |
|-----------|-------|--------|
| Investigation cases — evidence standard per pathology class | 1 | ADR-1a |
| Ghost denominator — all candidates with Term Set V disposition | 2 | ADR-2a |
| Sync tier — firing order, I/O, branch resolution, latency | 3 | ADR-3a |
| Async tier — firing order, I/O, delay estimate | 3 | ADR-3b |
| Side-effect trace ≥ L1 per V-F trigger | 4 | ADR-4a |
| Case closure with verbatim evidence citation | 4 | ADR-4b |
| Risk-ranked pathology summary with one-line mitigation | 5 | ADR-5a |

**Sub-step A-4.3: Derive Required Block Label strings**

The Required Block Label for each ADR entry is derived by the following rule:

> Required Block Label = `ANALYTICAL INSTRUCTIONS [` + ADR-ID + `]`

Applying the rule to each entry:

| ADR-ID | Derived Required Block Label |
|--------|------------------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

**Sub-step A-4.4: Uniqueness and completeness verification**

- [ ] All ADR-IDs are distinct
- [ ] All Required Block Label values are distinct
- [ ] No Required Block Label value is empty
- [ ] Every phase that performs analysis has at least one ADR entry
- [ ] The Required Block Label derivation rule was applied uniformly (no exceptions)

All checks passed.

**Sub-step A-4.5: Assemble final ADR register**

This is the authoritative register. The Domain Expert's instruction blocks SHALL use Required Block Label strings as structural headers — verbatim, no deviation.

| ADR-ID | Analytical Dimension | Phase | Required Block Label |
|--------|---------------------|-------|---------------------|
| ADR-1a | Investigation cases — evidence standard per pathology class | 1 | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | Ghost denominator — all candidates with Term Set V disposition | 2 | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | Sync tier — firing order, I/O, branch resolution, latency | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | Async tier — firing order, I/O, delay estimate | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | Side-effect trace ≥ L1 per V-F trigger | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | Case closure with verbatim evidence citation | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | Risk-ranked pathology summary | 5 | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

**Bidirectional rule:** Every ADR-ID → must have an instruction block with the exact Required Block Label string (register → block). Every instruction block → must cite a valid ADR-ID (block → register). Violations detectable by string comparison. FM-13 if Required Block Label column absent. FM-14 if any label deviates.

### AUDITOR DECLARATION

Pre-execution infrastructure is complete. Verify before Domain Expert begins:

- [ ] FM catalog: 14 entries (FM-01 through FM-14) with Phase Governed column
- [ ] Term Set V: 3 verdicts with evidence requirements and invalid application examples
- [ ] Tier Manifest: structure declared, TOTAL_CHECK logic present
- [ ] ADR: 5 sub-steps completed; 7 entries; Required Block Label column fully populated with unique non-empty strings derived by the declared rule
- [ ] Uniqueness/completeness verification (A-4.4): all 5 checks passed
- [ ] Bidirectional rule stated

**AUDITOR DECLARATION ISSUED. Domain Expert execution authorized.**

---

## ROLE B: DOMAIN EXPERT (Power Automate / Copilot Studio)

Use Power Automate and Copilot Studio vocabulary throughout. Instruction blocks use Required Block Label strings from the Auditor's ADR register — exact strings, no variation.

### Phase 1: Investigation Case Opening

**ENTRY GATE:**
- [ ] Auditor Declaration issued; FM catalog, Term Set V, Tier Manifest, ADR all present
- [ ] Prohibition: Do not name, evaluate, or list any trigger in Phase 1

**`ANALYTICAL INSTRUCTIONS [ADR-1a]`**
Open three cases. State evidence standard as a specific, falsifiable condition. Cite verbatim at Phase 4 closure.

| Case ID | Pathology Class | Evidence Standard |
|---------|----------------|-------------------|
| CASE-STORM | Trigger Storm | |
| CASE-MISSING | Missing Trigger | |
| CASE-CIRCULAR | Circular Trigger | |

**REGISTER CHECK — Phase 1:** ADR-1a addressed. ✓

---

### Phase 2: Ghost Denominator Pre-Scan

**ENTRY GATE:**
- [ ] Phase 1 REGISTER CHECK passed; three cases open with evidence standards
- [ ] Prohibition: Do not describe trigger firing behavior in Phase 2

**`ANALYTICAL INSTRUCTIONS [ADR-2a]`**
All trigger candidates for this change — including those expected absent. Assign GD-IDs. Assign Term Set V verdict with structural basis. FM-04 if any candidate is omitted.

| GD-ID | Candidate Trigger | Verdict [Term Set V] | Structural Basis |
|-------|------------------|---------------------|-----------------|

Caption: Verdict ∈ {V-F, V-CA, V-FM}. Violations: `[NC: value]`.

After GD table: populate Tier Manifest. TOTAL_CHECK must = YES before Phase 3.

**REGISTER CHECK — Phase 2:** ADR-2a addressed. ✓

---

### Phase 3: Trigger Enumeration

**ENTRY GATE:**
- [ ] Phase 2 REGISTER CHECK passed; N ≥ 1 V-F entries; TOTAL_CHECK = YES
- [ ] Prohibition: Do not introduce new GD-IDs; do not re-assign tier membership

**`ANALYTICAL INSTRUCTIONS [ADR-3a]`**
Sync tier from SYNC_IDS. Firing sequence first to last. Exact fields consumed (Input Payload) and exact action produced (Output Action). For conditional triggers: branch executed, condition evaluated (TRUE/FALSE). FM-01 if generic. FM-02 if merged with async.

### SYNC TIER

| GD-ID | Trigger Name | Status [TS] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Latency Impact |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

Caption: Status ∈ {Active, Conditional-passes, Conditional-fails, Inactive}.

**`ANALYTICAL INSTRUCTIONS [ADR-3b]`**
Async tier from ASYNC_IDS. Delay Estimate column (scheduling window semantics). Distinct from Latency Impact (immediate execution semantics) — different columns, different semantics. FM-02 if merged.

### ASYNC TIER

| GD-ID | Trigger Name | Status [TA] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Delay Estimate |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

Caption: Status ∈ {Queued, Deferred, Skipped}.

**REGISTER CHECK — Phase 3:** ADR-3a, ADR-3b addressed. ✓

---

### Phase 4: Reconcile and Close

**ENTRY GATE:**
- [ ] Phase 3 REGISTER CHECK passed
- [ ] Phase 1 case evidence standards available for verbatim citation
- [ ] Phase 2 V-FM entries available for CASE-MISSING review

**`ANALYTICAL INSTRUCTIONS [ADR-4a]`**
Side-effect chains for all V-F triggers. Minimum L1. `[Trigger] → [Side Effect L1] → [L2 or terminal]`.

| Trigger | Side Effect (L1) | Downstream (L2) |
|---|---|---|

**`ANALYTICAL INSTRUCTIONS [ADR-4b]`**
Close all three investigation cases. Required: verbatim evidence standard citation from Phase 1. FM-09 if paraphrased.

> CASE [ID]: [disposition]. Evidence standard applied: "[verbatim text from Phase 1]"

**REGISTER CHECK — Phase 4:** ADR-4a, ADR-4b addressed. ✓

---

### Phase 5: Risk Summary

**ENTRY GATE:**
- [ ] Phase 4 REGISTER CHECK passed; all cases closed; all GD entries resolved

**`ANALYTICAL INSTRUCTIONS [ADR-5a]`**
Risk table ranked by operational risk. No findings: state "No pathologies confirmed."

| Pathology Class | Instance | Risk [RK] | Mitigation |
|---|---|---|---|

Caption: Risk ∈ {High, Medium, Low}.

**REGISTER CHECK — Phase 5:** ADR-5a addressed. ✓

---

### FINAL BIDIRECTIONAL AUDIT

(a) Register → Block string match:

| ADR-ID | Required Block Label | Block Found (verbatim) |
|--------|---------------------|------------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` | |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` | |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` | |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` | |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` | |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` | |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` | |

(b) Block → Register: all instruction blocks cite valid ADR-IDs. ✓

FM-13 not triggered. FM-14 not triggered. Protocol complete.

---

## V-05

**Variation axes:** Output format + Inertia framing — Required Block Label contrasted against a named naive-protocol baseline; the column is introduced as a concrete structural improvement over semantic matching
**Hypothesis:** When the prompt explicitly names what a default high-quality protocol produces (ADR with phase-scoped IDs and bidirectional rule, but no pre-specified label strings — correspondence verified by reading prose) and then names the structural improvement the Required Block Label column provides (correspondence reduced to string comparison), the model has a concrete contrast target. The inertia framing makes C-30 a named improvement rather than an additional structural requirement — the model understands what it's replacing and why, increasing the probability that the column is populated correctly and the label strings are used exactly.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Determine which automations fire, their order, inputs/outputs, and any trigger pathologies.

---

## PROTOCOL BASELINE AND IMPROVEMENT CONTRACT

A competent trigger analysis response typically contains:
- A ghost denominator pre-scan of trigger candidates
- A verdict taxonomy for dispositions
- A tier-split enumeration (sync / async)
- Investigation cases for pathology classes
- A reconcile-and-close phase

**What a strong-but-not-complete protocol produces:** The above plus an Analytical Dimension Register (ADR) that assigns phase-scoped identifiers to each dimension and states a bidirectional consistency rule (every ADR-ID has a corresponding instruction block, and every instruction block cites a valid ADR-ID). Correspondence between register entries and instruction blocks is verified by reading and semantic matching.

**What this protocol adds — the Required Block Label improvement:**

The ADR register in this protocol includes a **Required Block Label** column that pre-specifies the exact instruction block header string for each dimension. This reduces the ADR-to-block correspondence check from a semantic operation (does this instruction block cover dimension X?) to a string-match operation (does the string `ANALYTICAL INSTRUCTIONS [ADR-xx]` appear verbatim in Phase N?).

The structural gain: a reader verifying compliance does not need to interpret content — only scan for the Required Block Label string. A response that uses a label like "Trigger Analysis for ADR-3a" instead of `ANALYTICAL INSTRUCTIONS [ADR-3a]` fails the string-match check even if the content is correct — because the verification protocol is string equality, not semantic coverage.

This is not a formatting preference. It is a verification protocol improvement.

---

## PRE-EXECUTION DECLARATIONS

### Failure Mode Catalog

| FM-ID | Failure Mode | What the Baseline Produces Instead |
|-------|-------------|-------------------------------------|
| FM-01 | Trigger listed without input payload or output action | Trigger name + "sends notification" |
| FM-02 | Sync/async tiers merged | Single flat table or list |
| FM-03 | Pathology answered without opened/closed case | "No storm detected" with no case |
| FM-04 | Enumeration without pre-declared candidate list | Enumeration begins directly |
| FM-05 | No reconcile-and-close phase | Protocol ends after enumeration |
| FM-06 | GD count global, no per-tier split | "7 triggers total" |
| FM-07 | Verdict taxonomy absent or V-CA without structural argument | "trigger not found" as final answer |
| FM-08 | Tier assigned at enumeration time | No manifest, tier assigned per row |
| FM-09 | Case closed without verbatim evidence standard citation | "confirmed no storm" without citing standard |
| FM-10 | Phase entered without gate check | Phases run in sequence without verification |
| FM-11 | ADR absent | Each phase defines own dimensions |
| FM-12 | Instruction block without ADR entry | Block present, no register entry |
| FM-13 | ADR lacks Required Block Label column | ADR present but correspondence is semantic |
| FM-14 | Instruction block label deviates from Required Block Label | Label uses synonym or paraphrase |

*FM-13 and FM-14 are the failures the Required Block Label improvement prevents. A response with a correct ADR but no Required Block Label column has FM-13. A response with the column but deviant labels has FM-14.*

### Verdict Taxonomy — Term Set V

```
TERM SET V
──────────────────────────────────────────────────────────────
V-F   FIRED
      Baseline behavior: trigger listed; activation assumed
      This protocol: affirmative activation evidence required —
      field/event matches configured condition; trigger enabled

V-CA  CONFIRMED ABSENT
      Baseline behavior: "not found" accepted as closure
      This protocol: structural argument required — scope exclusion,
      condition analysis (FALSE), or reachability argument;
      "not found" → assign V-FM instead

V-FM  FLAGGED MISSING
      Baseline behavior: candidate omitted entirely
      This protocol: named detection gap — expected behavior suggests
      trigger should fire; cannot confirm or rule out structurally
──────────────────────────────────────────────────────────────
```

### Tier Assignment Manifest

```
TIER MANIFEST
═══════════════════════════════════════════════════════
SYNC_IDS  : []   ← populate after Phase 2 GD scan
ASYNC_IDS : []   ← populate after Phase 2 GD scan
───────────────────────────────────────────────────────
TOTAL_COUNT   : 0
SYNC_COUNT    : 0
ASYNC_COUNT   : 0
TOTAL_CHECK   : SYNC_COUNT + ASYNC_COUNT = TOTAL_COUNT → [YES / NO]
═══════════════════════════════════════════════════════
Phase 3 gate: TOTAL_CHECK = YES. FM-06 if global count only. FM-08 if tier assigned during enumeration.
```

### Analytical Dimension Register (ADR) — with Required Block Labels

**Baseline ADR (what strong-but-not-complete looks like):**

| ADR-ID | Analytical Dimension | Phase |
|--------|---------------------|-------|
| ADR-1a | Investigation cases | 1 |
| ADR-2a | Ghost denominator | 2 |
| ... | ... | ... |

This produces a usable register, but ADR-to-block correspondence requires semantic reading. A reviewer must read the instruction block content and judge whether it covers the dimension — a subjective operation.

**This protocol's ADR — with Required Block Label column:**

Each row adds the exact label string the instruction block must use. Compliance check: find the Required Block Label string verbatim in Phase N. No interpretation needed.

| ADR-ID | Analytical Dimension | Phase | Required Block Label |
|--------|---------------------|-------|---------------------|
| ADR-1a | Investigation cases — evidence standard per pathology class | 1 | `ANALYTICAL INSTRUCTIONS [ADR-1a]` |
| ADR-2a | Ghost denominator — all candidates with Term Set V disposition | 2 | `ANALYTICAL INSTRUCTIONS [ADR-2a]` |
| ADR-3a | Sync tier — firing order, I/O, branch resolution, latency | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3a]` |
| ADR-3b | Async tier — firing order, I/O, delay estimate | 3 | `ANALYTICAL INSTRUCTIONS [ADR-3b]` |
| ADR-4a | Side-effect trace ≥ L1 per V-F trigger | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4a]` |
| ADR-4b | Case closure with verbatim evidence citation | 4 | `ANALYTICAL INSTRUCTIONS [ADR-4b]` |
| ADR-5a | Risk-ranked pathology summary | 5 | `ANALYTICAL INSTRUCTIONS [ADR-5a]` |

**Bidirectional contract:** register → block (every ADR-ID has a block labeled with its Required Block Label exactly) AND block → register (every instruction block cites its ADR-ID). String comparison verifies direction (a). ID cross-reference verifies direction (b). FM-13 if column absent. FM-14 if label deviates.

---

## PHASE 1: INVESTIGATION CASE OPENING

**ENTRY GATE:**
- [ ] Pre-execution declarations complete: FM catalog (14 entries), Term Set V, Tier Manifest, ADR (7 entries with Required Block Label column fully populated)
- [ ] Prohibition: Do not name, list, or evaluate any trigger in Phase 1

**`ANALYTICAL INSTRUCTIONS [ADR-1a]`**
*(Baseline would label this "Pathology Investigation Setup" or "Case Opening". This protocol requires this exact string — string equality, not content equivalence.)*

Open three investigation cases. State evidence standard as a specific, falsifiable condition — not a judgment call. This text will be cited verbatim at closure in Phase 4.

| Case ID | Pathology Class | Evidence Standard for Closure |
|---------|----------------|-------------------------------|
| CASE-STORM | Trigger Storm | |
| CASE-MISSING | Missing Trigger | |
| CASE-CIRCULAR | Circular Trigger | |

**REGISTER CHECK — Phase 1:** ADR-1a: Required Block Label match confirmed. ✓

---

## PHASE 2: GHOST DENOMINATOR PRE-SCAN

**ENTRY GATE:**
- [ ] Phase 1 REGISTER CHECK passed; three cases open with evidence standards
- [ ] Prohibition: Do not describe firing behavior in Phase 2

**`ANALYTICAL INSTRUCTIONS [ADR-2a]`**
*(The baseline might label this "Candidate Triggers" or "Trigger Inventory". The string `ANALYTICAL INSTRUCTIONS [ADR-2a]` is required — no equivalent accepted.)*

All candidates plausibly relevant to this change — including those expected absent. GD-IDs assigned. Term Set V verdict per pre-execution taxonomy. Structural basis for each V-CA verdict required. FM-04 if any candidate omitted.

| GD-ID | Candidate Trigger | Verdict [Term Set V] | Structural Basis |
|-------|------------------|---------------------|-----------------|

Caption: Verdict ∈ {V-F, V-CA, V-FM}. Violations: `[NC: value]`.

After GD table: populate Tier Manifest SYNC_IDS / ASYNC_IDS. TOTAL_CHECK must = YES.

**REGISTER CHECK — Phase 2:** ADR-2a: Required Block Label match confirmed. ✓

---

## PHASE 3: TRIGGER ENUMERATION

**ENTRY GATE:**
- [ ] Phase 2 REGISTER CHECK passed; N ≥ 1 V-F entries; TOTAL_CHECK = YES
- [ ] Prohibition: Do not introduce new GD-IDs; do not re-determine tier

**`ANALYTICAL INSTRUCTIONS [ADR-3a]`**
Synchronous tier from SYNC_IDS. Firing order first to last. Exact fields (Input Payload), exact action (Output Action). Branch Executed and Condition Evaluated for conditional triggers. FM-01 if generic I/O.

### SYNC TIER

Caption: Status ∈ {Active, Conditional-passes, Conditional-fails, Inactive}. Violations: `[NC: value]`.

| GD-ID | Trigger Name | Status [TS] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Latency Impact |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**`ANALYTICAL INSTRUCTIONS [ADR-3b]`**
Asynchronous tier from ASYNC_IDS. Delay Estimate (scheduling window semantics). The baseline uses "Latency" for both tiers — this protocol requires semantically distinct column names because the semantics of sync and async timing differ.

### ASYNC TIER

Caption: Status ∈ {Queued, Deferred, Skipped}. Violations: `[NC: value]`.

| GD-ID | Trigger Name | Status [TA] | Input Payload | Output Action | Branch Executed | Condition Evaluated | Delay Estimate |
|-------|-------------|-------------|--------------|--------------|----------------|--------------------|----|

**REGISTER CHECK — Phase 3:** ADR-3a, ADR-3b: Required Block Label matches confirmed. ✓

---

## PHASE 4: RECONCILE AND CLOSE

**ENTRY GATE:**
- [ ] Phase 3 REGISTER CHECK passed
- [ ] Phase 1 evidence standards available for verbatim citation

**`ANALYTICAL INSTRUCTIONS [ADR-4a]`**
Side-effect chains per V-F trigger. Baseline traces side effects in prose at the end of the enumeration table — this protocol requires a dedicated traced chain with explicit L1/L2 structure.

| Trigger | Side Effect (L1) | Downstream (L2) |
|---|---|---|

**`ANALYTICAL INSTRUCTIONS [ADR-4b]`**
Case closure. Baseline closes with judgment: "No storm found." This protocol requires verbatim citation of the evidence standard from Phase 1 — FM-09 if paraphrased or omitted.

> CASE [ID]: [disposition]. Evidence standard applied: "[exact text from Phase 1]"

**REGISTER CHECK — Phase 4:** ADR-4a, ADR-4b: Required Block Label matches confirmed. ✓

---

## PHASE 5: RISK SUMMARY

**ENTRY GATE:**
- [ ] Phase 4 REGISTER CHECK passed; all cases closed; all GD entries resolved

**`ANALYTICAL INSTRUCTIONS [ADR-5a]`**
Risk-ranked pathology table. Baseline lists pathologies in prose or as bullet points. This protocol uses a table with Risk [Term Set RK] column and one-sentence mitigation per instance.

| Pathology Class | Instance | Risk [Term Set RK] | Mitigation |
|---|---|---|---|

Caption: Risk ∈ {High, Medium, Low}.

**REGISTER CHECK — Phase 5:** ADR-5a: Required Block Label match confirmed. ✓

---

## FINAL BIDIRECTIONAL AUDIT

(a) Register → Block — string-match verification (the improvement over semantic matching):

| ADR-ID | Required Block Label | String Found Verbatim |
|--------|---------------------|-----------------------|
| ADR-1a | `ANALYTICAL INSTRUCTIONS [ADR-1a]` | |
| ADR-2a | `ANALYTICAL INSTRUCTIONS [ADR-2a]` | |
| ADR-3a | `ANALYTICAL INSTRUCTIONS [ADR-3a]` | |
| ADR-3b | `ANALYTICAL INSTRUCTIONS [ADR-3b]` | |
| ADR-4a | `ANALYTICAL INSTRUCTIONS [ADR-4a]` | |
| ADR-4b | `ANALYTICAL INSTRUCTIONS [ADR-4b]` | |
| ADR-5a | `ANALYTICAL INSTRUCTIONS [ADR-5a]` | |

(b) Block → Register — ID cross-reference: all instruction blocks cite valid ADR-IDs. ✓

FM-13 not triggered (Required Block Label column present and populated).
FM-14 not triggered (all instruction block labels match Required Block Label strings exactly).
Protocol complete. Improvement contract satisfied.
