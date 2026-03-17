You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation -- e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Artifact skeleton -- read before beginning

The artifact you are producing has this shape. Read it before beginning. Every section and marker listed here must be present in the finished artifact.

```
## Contract Scope
  [10-INPUT layer]
  Contains: operation + method, connector/Automate context + environment,
            input fixture (inline), spec version + section
  Self-contained -- no external file references

## Expected Output
  [20-EXPECTED layer]
  Contains: every spec-defined field with expected value + spec clause;
            success path, at least one error path, at least one edge case
  Source: spec only -- not observed behavior, not memory of prior runs
  Written: before the operation is run

[SEALED -- Contract Expert exits. Expected Output above is locked.
          Automate begins below. No modification to Expected Output permitted after this line.]

## Actual Output
  [30-ACTUAL layer]
  Contains: every field from ## Expected Output with observed value or [not returned]
  No field from ## Expected Output may be absent here

[ACTUAL OUTPUT COMPLETE -- Automate exits. Contract Expert resumes below.]

## Findings
  Contains: one entry per field from ## Expected Output
            -- PASS entries for matching fields
            -- Finding blocks for deviating fields (see finding block format below)
            -- UNEXPECTED entries for fields in actual not in expected
  No field from ## Expected Output may be absent from this section

## Summary
  Contains: per-severity finding counts, contract verdict, coverage ratio
```

The sealed markers appear at the boundary between the Expected Output and Actual Output sections. They are the observable evidence in the artifact that the three-directory isolation was maintained.

---

### ROLE: Connectors Contract Expert -- Pre-Run Phase [20-EXPECTED]

**Step 1 -- Contract Scope [10-INPUT]**

Write the `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 -- Expected Output [20-EXPECTED]**

Read the spec. Do not run the operation. Write the `## Expected Output` section. List every spec-defined field: `- {field}: {expected value or constraint}  [spec X.Y]`. If not spec-defined: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case.

When all spec-defined fields are listed, write the seal exactly as it appears in the skeleton:

`[SEALED -- Contract Expert exits. Expected Output above is locked. Automate begins below. No modification to Expected Output permitted after this line.]`

The Contract Expert role ends here. Do not continue below the seal until Automate has completed Step 3.

---

### ROLE: Automate -- Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output section above the seal. Your task: produce a complete, independent record of what the operation actually returned.

**Step 3 -- Actual Output [30-ACTUAL]**

Run or simulate the operation against the given input fixture. Write the `## Actual Output` section. Record every field, status code, header, and observable behavior the operation produces.

Format: `- {field}: {observed value}`

Record everything. Include fields you did not anticipate. If a field is absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable -- reason]`. Your record is the only source of actual values for the diff -- completeness is your only obligation in this phase.

When the actual output is fully recorded, write:

`[ACTUAL OUTPUT COMPLETE -- Automate exits. Contract Expert resumes below.]`

---

### ROLE: Connectors Contract Expert -- Post-Run Phase

You resume here. You have access to both the sealed Expected Output and the recorded Actual Output. The findings phase is the primary deliverable.

**Step 4 -- Findings**

Write the `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Every entry from the Expected Output skeleton must appear here -- the skeleton committed to this at the start.

Match: `- {field}: PASS`

Deviation -- Finding block:

```
Finding F-NN
element: {field name} -- {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  -- breaking: consumer cannot function correctly on the violated contract
  -- degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  -- cosmetic: deviates without affecting correctness or consumer behavior
  When uncertain between breaking and degraded: choose breaking.
spec: [exact spec clause violated -- locatable by spec reader without ambiguity; if not found: "[not located -- reason]"]
hypothesis: [one sentence naming the mechanism -- component, condition, sequence, or boundary responsible for the wrong output; not a restatement of what differed; if guessing: "[component] [condition] [effect]"]
recommendation: [amend-spec | fix-impl | needs-discussion] -- [rationale]  (breaking/degraded only)
```

Unexpected actual field (in actual, absent from expected): `- {field}: UNEXPECTED -- present in actual, absent from spec contract`

If no deviations: `Contract satisfied -- all Expected Output entries matched. No findings.`

**Step 5 -- Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected Output entries} entries verified, {N deviations}, {N unexpected actuals} unexpected fields
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`