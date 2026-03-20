---
name: discover-orchestrate
description: "Orchestrate a full discovery campaign. Assesses which discover skills have run, then sequences the remaining ones in optimal order. Display only -- does not run skills."
allowed-tools: [Read, Glob]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


If --compact: list the top 3 discover skills to run next with one-sentence rationale each. Skip full sequence.

You are running /discover-orchestrate for: {{topic}}

Coordinate a full discovery campaign. This skill assesses what has already been run
and sequences the remaining discover skills in the optimal order.

This skill DOES NOT run other skills. It tells the user which skills to run next and why.

---

## PHASE 1: WHAT HAS ALREADY RUN

Glob signals/**/{topic}-* to find all existing signal artifacts for {{topic}}.

| Signal | Artifact Found | Date | Status |
|--------|---------------|------|--------|
| discover-competitors | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-inertia     | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-feasibility | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-risk        | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-hypothesis  | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-websearch   | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-causal      | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-coherence   | [path or MISSING] | [date or --] | DONE / MISSING |
| discover-synthesize  | [path or MISSING] | [date or --] | DONE / MISSING |

Skills complete: [N of 9]
Skills pending: [N of 9]

---

## PHASE 2: RECOMMENDED SEQUENCE

For each pending skill, show the recommended order, the question it answers, and why it
matters for {{topic}} specifically.

Run in this order:

**1. discover-competitors** (if MISSING)
Question answered: Who else solves this problem, and why does inertia win?
Why it matters for {{topic}}: [Infer from topic context -- what is the likely incumbent or workaround?]
Prerequisite: None. Always run first.

**2. discover-inertia** (if MISSING)
Question answered: How entrenched is the status quo? What will it cost to displace?
Why it matters for {{topic}}: [What is the likely current workaround? What switching friction exists?]
Prerequisite: discover-competitors helps frame the status quo.

**3. discover-feasibility** (if MISSING)
Question answered: Can the team actually build this, given size and timeline?
Why it matters for {{topic}}: [What is the likely build complexity? What dependencies exist?]
Prerequisite: Inertia analysis informs the do-nothing cost column in feasibility.

**4. discover-risk** (if MISSING)
Question answered: What could go wrong across technical, compliance, adoption, and dependency dimensions?
Why it matters for {{topic}}: [What are the likely risk dimensions -- regulated domain? Complex integrations?]
Prerequisite: Feasibility surfaces technical risks that risk should confirm or expand.

**5. discover-hypothesis** (if MISSING)
Question answered: What is the team assuming, and what would prove them wrong?
Why it matters for {{topic}}: [What is the core assumption behind this feature? What would invalidate it?]
Prerequisite: Competitors + risk context sharpens the hypothesis.

**6. discover-websearch** (if MISSING)
Question answered: What does public evidence say? Are the claims grounded in reality?
Why it matters for {{topic}}: [What claims most need external grounding for this topic?]
Prerequisite: Hypothesis defines the claims to ground.

**7. discover-causal** (if MISSING)
Question answered: What causes the problem this feature solves? Is the root cause addressable?
Why it matters for {{topic}}: [What is the assumed cause-effect chain? Is it validated?]
Prerequisite: Websearch provides external grounding for causal claims.

**8. discover-coherence** (if MISSING)
Question answered: Is the feature definition internally consistent? Do the signals agree?
Why it matters for {{topic}}: [Where are the likely consistency gaps -- scope, assumptions, constraints?]
Prerequisite: At least 3 prior signals to check for coherence.

**9. discover-synthesize** (if MISSING)
Question answered: What do all the signals say together? Proceed, pause, or pivot?
Why it matters for {{topic}}: [What is the key decision this synthesis will inform?]
Prerequisite: Run last. Requires at least 2 prior signals to be meaningful.

---

## DISPLAY SUMMARY

**Next skill to run**: [Name the highest-priority missing skill]
**Command**: /discover-[skill] {{topic}}

**Full remaining sequence**:
1. /discover-[skill1] {{topic}}
2. /discover-[skill2] {{topic}}
3. /discover-[skill3] {{topic}}
[... continue for all pending skills]

Campaign complete when: discover-synthesize has run and returned a PROCEED / PAUSE / PIVOT verdict.

---

No artifact written. This skill produces display output only.
