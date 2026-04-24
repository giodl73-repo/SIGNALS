You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

---

### CONTRACTS

---

#### CONTRACT: INPUT-ROUTING-RULES

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register |
|-------|----------|
| archetype | Check existing roles in the area first; use their value |
| orientation.frame | First-person observational: how this role perceives its domain |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items |
| expertise.depth | Specific domain knowledge |

---

#### CONTRACT: COLUMN-HEADER

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Substitute all `{area}` slots.

```yaml
---
name: {area} inertia advocate
version: "1.0"
archetype: [match existing roles in the area]
orientation:
  frame: "Sees every change in {area} as requiring proof of necessity. Switching costs -- relearning, re-integration, debugging unfamiliar surfaces -- are real and must be named before any proposal proceeds."
  serves: "Teams making adoption decisions in {area}: surfaces the hidden cost of change so the decision is made with full information, not optimism."
lens:
  verify:
    - "Is the cost of migrating existing {area} work to the new approach documented?"
    - "Are the failure modes of the proposed change listed alongside its benefits?"
    - "Is there a rollback path if the new approach underperforms?"
    - "Has the team that will live with this change been consulted?"
  simplify:
    - "Name the one thing the current approach does well that the new one must preserve."
    - "State the switching cost in hours, not in abstract risk."
expertise:
  depth: "Switching cost analysis, status-quo defense, risk enumeration for {area} change proposals"
  relevance: "Any {area} decision involving migration, adoption, or replacement of current practice"
scope: "{area}"
collaborates_with: []
artifacts:
  - "inertia-report-{topic}-{date}.md"
workflow:
  - "Receive change proposal"
  - "Enumerate switching costs and failure modes"
  - "Name the one thing worth preserving from current approach"
  - "Produce inertia report"
---

## {area} Inertia Advocate

| Change Type / Domain | Switching Cost | Rollback Path | Verdict |
|----------------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Items name the CONTRACT block and validation scope only -- no rule enumeration. Declaration names the gate that executes each item (forward); each gate cites the declaration ID it validates (backward). Fully bidirectional.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.roles/{area}/{subrole}.md` | Phase 6 setup |
| B | FIELD-REGISTER compliance -- frontmatter field completeness | Phase 3 Gate 3a |
| C | FIELD-REGISTER compliance -- orientation.frame register | Phase 3 Gate 3b |
| D | FIELD-REGISTER compliance -- orientation.serves beneficiary naming | Phase 3 Gate 3c |
| E | FIELD-REGISTER compliance -- lens.verify sharpness and count | Phase 3 Gate 3d |
| F | COLUMN-HEADER compliance -- body table column headers | Phase 4 Gate 4b |
| G | INPUT-ROUTING-RULES compliance -- input classification and resolution | Phase 0 Gate 0 |
| H | INERTIA-ADVOCATE-TEMPLATE compliance -- companion file completeness | Phase 2 Gate 2a |

---

### PHASES

---

#### PHASE 0 -- Input Guard

CONTRACT: INPUT-ROUTING-RULES applied.

-> **Gate 0 [G]:** INPUT-ROUTING-RULES -- input classification and resolution. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

CONTRACT: INTERACTIVE-HOLD applied when EMPTY input confirmed. NAME-ONLY (`area:subrole`): extract area and subrole directly. DESCRIPTION (quoted string): derive area and subrole from natural language. INTERACTIVE (empty / confirmed EMPTY): all three answers required before Phase 2.

-> **Gate 1:** area and subrole extraction confirmed. PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

CONTRACT: INERTIA-ADVOCATE-TEMPLATE applied when companion is absent. Check `.roles/{area}/inertia-advocate.md`. If ABSENT: generate companion content, substitute all `{area}` slots, hold in working memory. If PRESENT: continue to Phase 3.

-> **Gate 2a [H]:** INERTIA-ADVOCATE-TEMPLATE -- slot substitution completeness. PASS / FAIL
-> **Gate 2b:** INERTIA-ADVOCATE-TEMPLATE -- output path. PASS / FAIL

---

#### PHASE 3 -- Generate Frontmatter

CONTRACT: FIELD-REGISTER applied. All 12 frontmatter fields generated for `.roles/{area}/{subrole}.md`.

-> **Gate 3a [B]:** FIELD-REGISTER -- frontmatter completeness. PASS / FAIL
-> **Gate 3b [C]:** FIELD-REGISTER -- orientation.frame register. PASS / FAIL
-> **Gate 3c [D]:** FIELD-REGISTER -- orientation.serves beneficiary. PASS / FAIL
-> **Gate 3d [E]:** FIELD-REGISTER -- lens.verify sharpness and count. PASS / FAIL
-> **Gate 3e:** frontmatter -- no placeholder text. PASS / FAIL

---

#### PHASE 4 -- Generate Body

CONTRACT: COLUMN-HEADER applied. Body written: `## {Subrole} Domain` heading + domain specializations table, minimum 3 rows.

-> **Gate 4a:** body -- domain specializations table present. PASS / FAIL
-> **Gate 4b [F]:** COLUMN-HEADER -- body table domain vocabulary. PASS / FAIL
-> **Gate 4c:** body -- row count minimum. PASS / FAIL

---

#### PHASE 5 -- Pre-Write Confirmation

CONTRACT: AUDIT-CHECKLIST confirmation. Confirm each is resolved:

```
[A] Path correctness: .roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES -- confirmed Gate 0? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.
