# /hypothesis-investigation — Hypothesis-First Verification

> Installed from sim/techniques/08 + signal:prove-hypothesis skill.
> For: pacts S06 (self-modify block), S07 (bias detection)

## Usage

```
/hypothesis-investigation <hypothesis> <spec>
```

## Protocol

State what you believe and what would change your mind. A hypothesis has: a claim
(what you believe), a falsification condition (what evidence would prove it wrong),
a confidence level (0-100), and experiments that will test it.

The hypothesis is a commitment — you cannot move the goalposts after seeing results.

### Phase 1 — Hypothesis Statement

```markdown
**Claim**: {what we believe the contract guarantees}
**Falsification**: {what evidence would prove the guarantee doesn't hold}
**Confidence**: {0-100 before investigation}
**Spec basis**: {which spec sections support this claim}
```

### Phase 2 — Experiment Design

| # | Experiment | Type | What It Tests | Expected Result |
|---|-----------|------|---------------|-----------------|
| E1 | ... | spec-trace / code-trace / scenario-trace | ... | ... |
| E2 | ... | ... | ... | ... |

Experiment types:
- `spec-trace`: Derive expected behavior from spec text alone
- `code-trace`: Read implementation code and trace actual behavior
- `scenario-trace`: Check existing scenario findings for evidence
- `adversarial`: Design an input specifically intended to break the guarantee

### Phase 3 — Execute Experiments

For each experiment, record:
- **Input**: what was examined
- **Process**: how the trace was done
- **Result**: what was found
- **Supports/Refutes**: does this support or refute the hypothesis?

### Phase 4 — Synthesis

```markdown
**Original claim**: {restate}
**Original confidence**: {N}/100
**Evidence summary**:
- Supporting: {count} experiments
- Refuting: {count} experiments
- Ambiguous: {count} experiments

**Revised confidence**: {N}/100
**Verdict**: CONFIRMED / REFUTED / PARTIALLY CONFIRMED
**Key finding**: {the most important thing we learned}
```

### Phase 5 — Findings

For each refuting or ambiguous experiment:

| # | Finding | Experiment | Severity | Spec Clause |
|---|---------|-----------|----------|-------------|

## Output

Write to the scenario directory:
- `SCENARIO.md` — full hypothesis investigation
- `TRACE.md` — synthesis summary + findings table
