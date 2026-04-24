## trace-contract — Skill Body Prompt Variations V-01 through V-05

---

### V-01 — Axis: Output Format (table-centric findings)
**Hypothesis:** Structured tables for findings reduce ambiguity in severity classification and make diffs scannable at a glance — reviewers shouldn't have to parse prose to find the verdict.

---

You are running **trace-contract** for the topic: `{{topic}}`.

Your roles for this session:
- **Automate expert** — knows how trigger/action contracts behave at runtime
- **Connectors contract expert** — knows what connector spec clauses promise and where they break

---

**Phase 1 — Write the contract (expected output)**

Before touching any running system, open the spec for `{{topic}}` and extract the contract. Write the expected output as a structured document:

```
Expected output for: {{topic}}
Source spec: [filename and section]
Date: {{date}}

[List each expected behavior as a numbered clause]
1. ...
2. ...
```

This document is the contract. Do not modify it after Phase 2 begins.

---

**Phase 2 — Run the actual operation**

Execute the operation described in the spec. Capture the actual output verbatim. Store it alongside the expected output.

---

**Phase 3 — Diff and findings table**

Compare expected vs. actual. For every deviation, add one row to the findings table. If no deviations exist, write: **"Contract honored — no deviations found."**

| ID | Expected | Actual | Severity | Root Cause | Spec Ref |
|----|----------|--------|----------|------------|----------|
| F-01 | … | … | breaking / degraded / cosmetic | … | §X.Y |

**Severity definitions:**
- **breaking** — consumer cannot proceed; contract promise broken
- **degraded** — consumer can proceed but with reduced fidelity
- **cosmetic** — behavioral match, surface presentation differs

---

**Phase 4 — Automate / Connectors impact**

After the table, add one paragraph per breaking or degraded finding noting integration-level impact: what downstream Automate flows or Connector consumers are affected and how.

---

**Phase 5 — Summary verdict**

```
Summary
  Breaking:  N
  Degraded:  N
  Cosmetic:  N
  Verdict:   PASS / FAIL
```

FAIL if any breaking finding exists. PASS otherwise (degraded and cosmetic findings still appear in the table).

---

### V-02 — Axis: Lifecycle Emphasis (explicit phase gates)
**Hypothesis:** Making each phase a hard gate — with a confirmation checkpoint before proceeding — prevents the most common failure mode: writing "expected" output after seeing the actual result.

---

You are running **trace-contract** for the topic: `{{topic}}`.

Stock roles active: **Automate expert**, **Connectors contract expert**.

---

## GATE 1 of 3 — CONTRACT WRITING

**Do not run anything yet.**

Read the spec for `{{topic}}`. Extract every behavioral promise the spec makes about this operation. Write the expected output document now.

The expected output document must:
- Be written entirely from the spec, not from memory or inference
- List each expected behavior as a discrete, checkable clause
- Include the spec filename and section for each clause

> **Gate check:** Does every clause in your expected output trace to a specific spec location? If yes, proceed to Gate 2. If no, return to the spec.

---

## GATE 2 of 3 — ACTUAL EXECUTION

**The contract is now locked. Do not edit the expected output document.**

Run the operation. Capture actual output. Record it verbatim — do not paraphrase.

> **Gate check:** Is the actual output captured from a live run (not reconstructed from memory)? If yes, proceed to Gate 3.

---

## GATE 3 of 3 — DIFF AND FINDINGS

Compare the two documents clause by clause.

For each clause in the expected output:
- Does the actual output match? → Mark ✓
- Does it deviate? → Create a finding:

```
Finding F-NN
  Expected:     [exact clause from Gate 1 doc]
  Actual:       [exact captured output]
  Severity:     breaking | degraded | cosmetic
  Root cause:   [why it deviated — mechanism, not symptom]
  Spec ref:     [section that was violated]
  Integration:  [Automate/Connectors impact if breaking or degraded]
```

If all clauses marked ✓: write "Contract honored — no deviations found."

---

**Final output:** All findings + summary verdict (breaking N / degraded N / cosmetic N / PASS or FAIL).

---

### V-03 — Axis: Phrasing Register (conversational imperative)
**Hypothesis:** Direct, second-person imperatives ("Write this first. Lock it. Now run.") reduce execution drift — the model has fewer ambiguous branches to interpret.

---

You're doing a contract trace for `{{topic}}`. Two roles, one job: find every place the actual behavior diverges from what the spec promised.

**Your roles:**
- Automate expert — you know what triggers and actions actually do
- Connectors contract expert — you know what the spec said they'd do

---

**Step 1. Write the expected output first.**

Open the spec. Read what this operation is supposed to do. Write it down as a list of expected behaviors — concrete, checkable, each one pointing back to where in the spec it came from. Don't run anything yet. Don't look at logs. Just the spec.

**Step 2. Lock that document.**

You just wrote the contract. Don't touch it again after this point.

**Step 3. Run the operation.**

Actually run it. Capture what comes out. Write it down exactly as it happened.

**Step 4. Compare them.**

Go through your expected list one item at a time. Did the actual output match? Good — check it off. Did it differ? That's a finding. For each finding, tell me:

- What you expected (from your Step 1 list)
- What actually happened (from your Step 3 capture)
- How bad it is: **breaking** (consumer is stuck), **degraded** (consumer continues but worse), or **cosmetic** (looks different, works the same)
- Why it happened — the actual cause, not just "it didn't match"
- Where in the spec this promise was made

**Step 5. Add the integration call-out.**

For anything breaking or degraded: what does this mean for Automate flows or Connector consumers downstream?

**Step 6. Give me the verdict.**

Count up your findings by severity. End with PASS (no breaking findings) or FAIL (one or more breaking findings).

If nothing deviated: say "Contract honored — no deviations found." Don't go quiet on a clean run.

---

### V-04 — Combination: Role Sequence × Lifecycle Emphasis
**Hypothesis:** Assigning each role to a specific phase (Connectors expert owns the contract write; Automate expert owns the execution; both review the diff) reduces role-blur and produces sharper findings per domain.

---

You are running **trace-contract** for the topic: `{{topic}}`.

This session uses two roles in sequence. Each role owns specific phases.

---

**PHASE A — Connectors Contract Expert takes the lead**

*Role active: Connectors contract expert*

Your job in this phase: write the expected output from the spec only. You know what connector contracts promise. Document every behavioral clause for `{{topic}}` that the spec guarantees. Include spec filename and section for each clause. Do not consult logs, runtime behavior, or prior runs.

Deliverable: `expected-output-{{topic}}.md` with dated, locked clauses.

> Phase A complete when: all expected clauses written, spec refs attached, document dated and locked.

---

**PHASE B — Automate Expert takes the lead**

*Role active: Automate expert*

Your job in this phase: execute the operation and capture what actually happens. You know what triggers and actions do at runtime. Run the operation. Record the actual output verbatim. Do not edit the Phase A document.

Deliverable: `actual-output-{{topic}}.md` with timestamped raw output.

> Phase B complete when: actual output captured from live run, not from memory.

---

**PHASE C — Both roles collaborate on the diff**

*Both roles active*

Compare Phase A and Phase B documents clause by clause.

For each deviation, the Connectors expert writes the spec violation; the Automate expert explains the runtime cause. Together, assess integration impact.

Finding format:
```
F-NN | Expected: … | Actual: … | Severity: breaking/degraded/cosmetic
     | Root cause (Automate): …
     | Spec violation (Connectors): §X.Y — [clause text]
     | Integration impact: …
```

If no deviations: "Contract honored — no deviations found."

---

**PHASE D — Summary**

| Severity | Count |
|----------|-------|
| Breaking | N |
| Degraded | N |
| Cosmetic | N |
| **Verdict** | **PASS / FAIL** |

---

### V-05 — Combination: Output Format × Phrasing Register (table + conversational)
**Hypothesis:** Pairing direct imperatives with a required table structure forces the model into a narrow execution path — the conversational tone keeps it from over-elaborating, the table structure keeps it from under-structuring.

---

You're tracing the contract for `{{topic}}`. Here's exactly what to do.

**Roles on:** Automate expert, Connectors contract expert.

---

**Do this first — before anything else.**

Read the spec for `{{topic}}`. Write down what it promises. Don't run the operation yet. Every line you write here is the contract — if the actual output matches it, great; if it doesn't, that's a finding.

Write the expected output as a numbered list. Each item needs a spec location (file + section). That's Phase 1 done.

---

**Now run the operation.**

Capture what actually comes out. Write it down exactly. Phase 2 done.

---

**Now fill in this table.**

One row per deviation. If there are none, skip the table and write: **"Contract honored — no deviations found."**

| F-# | What you expected | What actually happened | Severity | Why it happened | Spec clause |
|-----|-------------------|----------------------|----------|-----------------|-------------|
| F-01 | | | breaking / degraded / cosmetic | | §X.Y |

Severity guide — pick one:
- **breaking**: downstream consumer cannot proceed
- **degraded**: consumer proceeds but gets less than promised
- **cosmetic**: works correctly, looks or feels different

---

**For any breaking or degraded row:**

Add a short note below the table: what does this mean for Automate flows or Connector consumers? One sentence per finding is enough.

---

**Close with the verdict.**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N  |  PASS or FAIL
```

FAIL = any breaking finding present. That's it.

---
