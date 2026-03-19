Role name:   {role-name}    # e.g., "rate-limit-analyst"
Domain:      {domain}       # e.g., "signal", "craft", "platform"
Reviews:     {what-reviewed} # e.g., "flow signal artifacts", "API design docs"
# If not provided, infer from context. State inferred values before proceeding.

---

## PHASE 1 — CONTEXT CHECK

If role name, domain, or reviews are not explicitly provided, infer from the topic and any
signal artifacts in scope. State inferences here before generating the role.

| Field | Provided? | Value used | Inference rationale |
|-------|-----------|------------|---------------------|
| Role name | [YES / NO] | [value] | [if inferred: how derived] |
| Domain | [YES / NO] | [value] | [if inferred: how derived] |
| Reviews | [YES / NO] | [value] | [if inferred: how derived] |

Proceed only after all three fields are resolved.

---

## PHASE 2 — ROLE DEFINITION

Generate the full Signal role structure. Every field is required — write [N/A — reason] only
if the field genuinely cannot apply to this role.

```yaml
name: {role-slug}
# slug format: lowercase-hyphenated, e.g., "rate-limit-analyst"

orientation:
  frame: >
    {what this role focuses on — specific, not generic. Not "reviews code quality" but
    "identifies rate-limiting boundaries that are asserted without causal evidence"}
  serves: >
    {who benefits from this role's findings — name the audience and what they do with
    the findings. One sentence.}

lens:
  verify:
    # 6-8 specific checks. Each check names what the reviewer looks for and what
    # "failure" looks like. Not "check for errors" but "verify that each rate limit
    # entry carries a numeric value with unit — vague labels like 'throttled' fail."
    - {check 1}
    - {check 2}
    - {check 3}
    - {check 4}
    - {check 5}
    - {check 6}
    # add up to 2 more if the domain warrants
  simplify:
    # 3-4 principles for reducing complexity in this domain
    # Each should name what to remove or consolidate, not just "keep it simple"
    - {principle 1}
    - {principle 2}
    - {principle 3}

expertise:
  depth: >
    {specific domain knowledge this role applies. Name the framework, standard,
    platform, or technique — not generic "deep knowledge of the domain."}
  relevance: >
    {when this role fires — what signal types, artifact types, or lifecycle stages
    trigger this reviewer. Be specific: "fires on flow-throttle and flow-resilience
    artifacts; also fires when architecture artifacts describe external API calls."}

collaborates_with:
  # list role slugs that frequently share findings with this role
  - {related-role-1}
  - {related-role-2}
```

---

## PHASE 3 — AMEND

Three ways to sharpen the lens.verify checks for this role:

1. **Specificity**: [One check from lens.verify that is still too generic. Rewrite it with
   a specific failure condition and pass criterion.]

2. **Coverage gap**: [A check that is missing from the lens.verify list. Name the gap and
   write the check.]

3. **Disambiguation**: [A check that could be confused with another reviewer's scope. Rewrite
   it to clarify the boundary — what this role checks vs. what the adjacent role checks.]

---

Write role file to: .craft/roles/{domain}/{role-slug}.md
Write artifact to:  signals/roles/build/{topic}-roles-build-{date}.md

Frontmatter:
```
skill: roles-build
topic: {topic}
date: {date}
role_created: {role-slug}
```
