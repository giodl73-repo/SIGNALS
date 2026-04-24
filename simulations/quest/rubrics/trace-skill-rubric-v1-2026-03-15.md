---
skill: quest-rubric
skill_target: trace-skill
date: 2026-03-15
version: 1
---

# trace-skill Rubric -- v1 (2026-03-15)

Hand-compile a skill execution before building it. Given a skill spec and a test invocation,
trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had
run. The hand-compiled artifact IS the expected output. It becomes the scenario baseline for
quest-golden. A skill that cannot be hand-compiled cannot be implemented.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.

**Golden threshold:** All 5 essential criteria PASS and composite >= 80.

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 pts total |
| Recommended | C-06, C-07, C-08 | 30 pts total |
| Aspirational | C-09, C-10 | 10 pts total |

---

## Essential Criteria (C-01--C-05)

### C-01 -- Four-phase structure present: Gather, Bind, Execute, Verdict
- **Weight**: essential
- **Category**: format
- **Pass condition**: All four labeled phases appear in sequence order: Gather, Bind, Execute,
  Verdict. Each section contains at least one substantive statement. Blank or placeholder
  sections ("TBD", "n/a") do not pass. A trace missing any phase is structurally incomplete
  and cannot serve as a golden baseline -- it leaves gaps an implementer cannot close.

---

### C-02 -- Gather phase enumerates all inputs by name
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: Every input the skill requires (SkillSpec, TraceInput, and any
  context-detected values) is named explicitly in the Gather phase with its source. Inputs
  stated as "inferred" or "assumed" without a named source do not pass. A trace that begins
  execution with unnamed inputs cannot be deterministically reproduced.

---

### C-03 -- Bind phase maps each Gather input to its resolved value
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: For every input named in Gather, Bind records the resolved value used
  during execution. Variable or conditional values are resolved to a single concrete value
  for this trace. A Bind phase that omits any Gather input, or that defers resolution to
  Execute, does not pass.

---

### C-04 -- Execute phase produces the target skill's output artifact
- **Weight**: essential
- **Category**: behavior
- **Pass condition**: Execute produces an artifact whose structure matches what the named
  target skill would actually output: naming convention (`{topic}-{skill}-{date}.md`),
  required sections per the skill spec, and no elided or placeholder content. A hand-compiled
  trace that produces a differently-shaped document than the real skill would produce is not
  a usable golden baseline.

---

### C-05 -- Verdict phase states PASS or FAIL with rationale
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: Verdict declares an explicit PASS or FAIL verdict for the trace as a
  whole. The verdict is accompanied by at minimum one sentence of rationale naming what
  passed or what caused failure. A Verdict that states no outcome, or that gives rationale
  without a verdict, does not pass.

---

## Recommended Criteria (C-06--C-08)

### C-06 -- All four phases carry schema-compliant section labels
- **Weight**: recommended
- **Category**: format
- **Pass condition**: Section headers match the Signal skill lifecycle naming exactly
  (Gather, Bind, Execute, Verdict). Synonyms ("Setup", "Collection", "Results") do not
  pass even if content is correct. Consistent labels are required so automated scoring and
  template matching work without per-trace normalization.

---

### C-07 -- Verdict cites specific criterion IDs, not free-form prose
- **Weight**: recommended
- **Category**: depth
- **Pass condition**: Verdict references at least one rubric criterion by ID (e.g., "C-02
  PASS -- all inputs named in Gather"). Verdicts written as free-form prose without criterion
  anchors are gradable only by human inspection and cannot be scored programmatically.

---

### C-08 -- Artifact is complete and self-contained -- no elision markers
- **Weight**: recommended
- **Category**: correctness
- **Pass condition**: The Execute artifact contains no elision markers ("...", "[continued]",
  "[see spec]", "[TBD]", or equivalent). Every section the real skill would produce is present
  in full. A partial artifact cannot serve as a golden baseline -- it constrains only the
  portions shown.

---

## Aspirational Criteria (C-09--C-10)

### C-09 -- Gather phase includes a Coverage Matrix listing all spec requirements by ID
- **Weight**: aspirational
- **Category**: coverage
- **Pass condition**: Gather contains a Coverage Matrix enumerating every named requirement
  from the skill spec by ID, with each row showing whether the requirement is addressed in
  this trace. The matrix preamble states the closed-world assumption: requirements not listed
  are considered out of scope for this invocation. A trace without a Coverage Matrix requires
  a human reviewer to independently reconstruct what was and was not traced.

---

### C-10 -- Each Execute relay carries evidence fields (role, signal, binding, status)
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: Every relay emitted during the Execute phase includes four named
  evidence fields: role (who performed this step), signal (what was observed), binding
  (which Bind value governed this step), and status (outcome of this step). The Verdict
  phase reads and copies these fields rather than reconstructing them from memory. A trace
  without relay evidence fields converts Verdict assembly from read-and-copy into
  end-of-trace reconstruction, which is error-prone and unverifiable.
