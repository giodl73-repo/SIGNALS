# Quest Variate — org-build (Round 1)

Five complete prompt body variations for `/signal:org-build`. Single-axis first (V-01 through V-03), then two combinations (V-04–V-05).

---

## V-01 — Axis: Role Sequence (Inertia-Advocate Anchored First)

**Hypothesis**: Placing the inertia-advocate role as the first role generated anchors the model's "status quo pressure" lens before it builds out the rest of the org, producing richer anti-pattern commentary throughout.

```markdown
Generate a complete org model from the provided scan results or repository context.

## Step 1 — Anchor Role: Inertia-Advocate

Before generating any other role, create the inertia-advocate role file first:
- Path: `.roles/governance/inertia-advocate.md`
- This role represents the voice of status-quo inertia — the forces that resist structural change.
- It must include all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
- In the `lens` field, describe what signals this advocate would point to when arguing the flat structure is working fine.
- In the `scope` field, describe the boundary at which this advocate concedes structure is warranted.

This role is non-optional. It is generated first, regardless of depth flag.

## Step 2 — Org Chart

Produce `org-chart.md` with:

1. **ASCII hierarchy diagram** — box-and-line format, minimum 2 levels. Show the org shape.
   Example shape (adapt to actual context):
   ```
   ┌──────────────────────────────────────┐
   │            [Org Name]                │
   │              GM / Lead               │
   └────────────┬──────────┬─────────────┘
                │          │
         ┌──────┴──┐  ┌────┴──────┐
         │  Area A  │  │  Area B   │
         └──────────┘  └───────────┘
   ```

2. **Headcount by Area table** with columns: `Area | Headcount | Key Roles | Decides | Escalates`

3. **Flat-Case Pressure Assessment**
   Rate the inertia pressure using this closed-set scale:
   - `FLAT-CASE-PRESSURE: LOW` — strong case for adding structure
   - `FLAT-CASE-PRESSURE: MEDIUM` — mixed signals
   - `FLAT-CASE-PRESSURE: HIGH` — flat structure is defensible
   
   Close with one of two verdicts:
   - `CAN-OPERATE-FLAT: [reason]`
   - `STRUCTURE-WARRANTED: [reason]`

4. **Operating Rhythm** — table with 3+ distinct rows. Required row types: ROB (review of business), Shiproom, Governance. Each row: `Meeting | Cadence | Owner | Attendees | Key Output`.

5. **Committee Charters** — one charter per governance meeting. Each charter: `Name | Purpose | Membership | Quorum (N of M) | Escalation path | Output artifact`.

6. **Org Evolution Roadmap** — 2+ rows with typed triggers. Row types must differ: at minimum one headcount threshold trigger and one non-headcount trigger (e.g., capability gap, geographic expansion, funding stage).

7. **Anti-Pattern Watch** — 2+ rows. Each "Why It Applies Here" cell must open with `[element name] (cat-N) —` syntax. Use these categories:
   - cat-1: coordination overhead
   - cat-2: single point of failure
   - cat-3: authority ambiguity
   - cat-4: role duplication
   - cat-5: missing expertise

## Step 3 — Role Files (Standard: 20–30 | Deep: 50+)

For each role, create `.roles/{area}/{role-name}.md` with exactly these five fields:

```yaml
orientation: [what this role is fundamentally trying to accomplish]
lens: [the specialized viewpoint this role brings to every decision]
expertise: [specific skills, domains, or tools this role owns]
scope: [what this role decides unilaterally vs. coordinates on]
collaborates_with: [comma-separated list of roles this role has high-bandwidth relationships with]
```

Organize roles into area subdirectories (minimum 2 subdirectories).

For standard depth, cover: engineering lead, product, design, data/analytics, infrastructure/platform, customer-facing, and governance areas. Ensure the inertia-advocate (already written in Step 1) is included in the final count.

## Inputs

Use the provided scan output or infer from repository structure. If neither is present, generate a representative org for a mid-stage B2B SaaS product team (25–40 people).

## Output Checklist

Before finishing, verify:
- [ ] `.roles/governance/inertia-advocate.md` exists with all 5 fields
- [ ] `org-chart.md` has ASCII diagram spanning 2+ levels
- [ ] Headcount table has all 5 columns including `Decides` and `Escalates`
- [ ] `FLAT-CASE-PRESSURE:` rating is one of the three closed-set values
- [ ] Verdict is `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
- [ ] Role count is 20–30 (standard) or 50+ (deep)
- [ ] All role files have all 5 required fields
- [ ] Anti-pattern rows use `[element] (cat-N) —` syntax
```

---

## V-02 — Axis: Output Format (Template-First, Fill-in-the-Blanks)

**Hypothesis**: Providing explicit fill-in templates for every output artifact reduces omission errors (missing fields, wrong column names) by removing ambiguity about what "complete" looks like.

```markdown
Generate a complete org model. Follow the exact templates below — fill them in, do not invent alternate structures.

---

## Output 1: org-chart.md

### Section 1.1 — ASCII Hierarchy Diagram

Required: box-and-line diagram with minimum 2 levels. Substitute actual org structure:

```
┌──────────────────────────────────────────┐
│  [Org / Product Name]                    │
│  [Top-level role title]                  │
└───────────┬──────────────┬───────────────┘
            │              │
   ┌─────────┴───┐   ┌──────┴──────┐
   │  [Area 1]   │   │  [Area 2]   │
   └──────┬──────┘   └──────┬──────┘
          │                 │
   ┌──────┴──────┐   ┌──────┴──────┐
   │ [Sub-team]  │   │ [Sub-team]  │
   └─────────────┘   └─────────────┘
```

Add more levels and branches as the actual org warrants.

### Section 1.2 — Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [Area name] | [N] | [role1, role2] | [what this area owns] | [what goes up] |
| ... | | | | |

Minimum 3 rows. `Decides` = autonomous decisions. `Escalates` = requires cross-area approval.

### Section 1.3 — Flat-Case Pressure Assessment

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]

Evidence for flat: [1-2 sentences]
Evidence against flat: [1-2 sentences]

[CAN-OPERATE-FLAT: reason]
  OR
[STRUCTURE-WARRANTED: reason]
```

Only one verdict. Both is an error.

### Section 1.4 — Operating Rhythm

| Meeting | Cadence | Owner | Attendees | Key Output |
|---------|---------|-------|-----------|------------|
| [Review of Business (ROB)] | [weekly/biweekly] | [role] | [role list] | [artifact] |
| [Shiproom] | [weekly] | [role] | [role list] | [artifact] |
| [Governance review] | [monthly/quarterly] | [role] | [role list] | [artifact] |

Minimum 3 rows. ROB and Shiproom must both appear.

### Section 1.5 — Committee Charters

One charter per governance meeting listed in 1.4:

```
**[Meeting Name]**
- Purpose: [one sentence]
- Membership: [role list]
- Quorum: [N of M] (e.g., "3 of 5")
- Escalation path: [what happens if committee deadlocks]
- Output artifact: [what gets published after each meeting]
```

### Section 1.6 — Org Evolution Roadmap

| Trigger | Type | New Structure | Owner |
|---------|------|---------------|-------|
| [Headcount reaches N] | headcount-threshold | [what changes] | [who decides] |
| [Different trigger] | [capability-gap | geographic | funding-stage | other] | [what changes] | [who decides] |

Minimum 2 rows. Row 1 and Row 2 must have different `Type` values.

### Section 1.7 — Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Signal to Watch |
|--------------|---------------------|-----------------|
| [name] | [element name] (cat-N) — [explanation] | [observable signal] |
| [name] | [element name] (cat-N) — [explanation] | [observable signal] |

Minimum 2 rows. `Why It Applies Here` MUST start with `[element name] (cat-N) —`.
Category codes: cat-1=coordination overhead, cat-2=single point of failure, cat-3=authority ambiguity, cat-4=role duplication, cat-5=missing expertise.

---

## Output 2: .roles/ Files

### Role File Template

Path: `.roles/{area}/{role-name}.md`

```yaml
orientation: |
  [What this role is fundamentally trying to accomplish — the job-to-be-done]

lens: |
  [The specialized viewpoint this role brings to every decision and review]

expertise: |
  [Specific skills, domains, methods, or tools this role owns and is accountable for]

scope: |
  [What this role decides unilaterally. What requires coordination. What requires escalation.]

collaborates_with: |
  [Comma-separated list of roles. High-bandwidth = daily/weekly touch. Low-bandwidth = monthly.]
```

### Required Role

**Inertia-Advocate** must be present at `.roles/governance/inertia-advocate.md`.
- `lens`: describe what a status-quo defender would cite as evidence the current structure is fine
- `scope`: the threshold at which this advocate acknowledges structure is warranted

### Depth

- Standard (default): 20–30 role files
- Deep (`--depth deep`): 50+ role files

### Area Subdirectories

Minimum 2 subdirectories under `.roles/`. Example areas: engineering, product, design, data, platform, go-to-market, governance.

---

## Inputs

Scan results, repo context, or (if absent) assume a mid-stage B2B SaaS product team.

## Final Verification

Confirm before submitting:
- org-chart.md sections 1.1 through 1.7 all present
- inertia-advocate.md exists with all 5 fields
- Role count: 20–30 or 50+ depending on depth flag
- All role files use the exact 5-field template
- Flat-case verdict is exactly one of the two closed-set strings
- Every anti-pattern row opens `Why It Applies Here` with `[element] (cat-N) —`
```

---

## V-03 — Axis: Inertia Framing (Inertia as Structural Competitor)

**Hypothesis**: Framing "flat structure" as a named competing design rather than an absence of structure produces sharper FLAT-CASE-PRESSURE ratings and more specific anti-pattern analysis.

```markdown
You are building an org model for a product team. Your job is not just to draw boxes — it is to answer a design question:

**Does this team need structure, or is flat-and-coordinated the right operating model?**

Flat is a legitimate competitor. Treat it as such. A 20-person team with high trust, low coordination cost, and collocated expertise may genuinely be better served by fluid coordination than a formal org chart. Your org model must contend with that case, not assume it away.

---

## Phase 1 — The Flat Case

Before drawing any structure, characterize the flat-case argument:

1. **What signals support flat?** (team size, trust, communication density, co-location, domain overlap)
2. **What signals argue for structure?** (coordination failures, ambiguous ownership, escalation pressure, growth trajectory)
3. **Assign a FLAT-CASE-PRESSURE rating:**
   - `FLAT-CASE-PRESSURE: HIGH` — flat is strongly defensible; structure adds overhead without clear benefit
   - `FLAT-CASE-PRESSURE: MEDIUM` — mixed signals; structure helps some areas but not all
   - `FLAT-CASE-PRESSURE: LOW` — structure is clearly warranted; flat is causing friction

4. **Issue one verdict:**
   - `CAN-OPERATE-FLAT: [specific condition under which this remains true]`
   - `STRUCTURE-WARRANTED: [specific coordination failure or scale signal that tips the balance]`

Place this assessment in `org-chart.md` before the org diagram.

---

## Phase 2 — Inertia-Advocate Role

Now create the named voice of inertia. File: `.roles/governance/inertia-advocate.md`

This role is not hypothetical — it represents a real force in every org: the people, incentives, and history that resist structural change. Model it honestly.

Required fields:

```yaml
orientation: |
  Preserve the operating patterns that currently work. Minimize disruption to productive relationships.

lens: |
  [Describe what this advocate would point to: stable team output, low coordination overhead, 
  trust built over time, the cost of org change itself. What would they say at the design review?]

expertise: |
  [Organizational memory. Informal network mapping. Historical context on why things are the way they are.]

scope: |
  [Decisions this advocate influences: any structural change proposal. 
  Threshold for conceding: identify the specific signal (e.g., headcount, recurring coordination failures, 
  customer escalations) at which this advocate would say "structure is warranted."]

collaborates_with: |
  [All roles being restructured. Senior leadership. HR/People team.]
```

---

## Phase 3 — Org Chart

Produce `org-chart.md` (continuing the file from Phase 1):

1. **ASCII hierarchy** — box-and-line diagram, minimum 2 levels. Show the proposed structure.

2. **Headcount by Area** — table with columns: `Area | Headcount | Key Roles | Decides | Escalates`

3. **Operating Rhythm** — 3+ rows covering ROB, Shiproom, and Governance. Columns: `Meeting | Cadence | Owner | Attendees | Key Output`

4. **Committee Charters** — one per governance meeting. Each charter includes: Name, Purpose, Membership, Quorum (expressed as `N of M`), Escalation path, Output artifact.

5. **Org Evolution Roadmap** — typed triggers for when this structure should evolve. Minimum 2 rows with different trigger types. One must be a headcount threshold; one must be a non-headcount trigger (capability gap, funding stage, geographic expansion, or similar).

6. **Anti-Pattern Watch** — where the proposed structure creates its own risks. 2+ rows. Format for "Why It Applies Here": `[element name] (cat-N) — [explanation]`
   - cat-1: coordination overhead, cat-2: single point of failure, cat-3: authority ambiguity, cat-4: role duplication, cat-5: missing expertise

---

## Phase 4 — Role Files

Generate `.roles/{area}/{role-name}.md` for every role in the org.

**Depth**: Standard = 20–30 files. Deep (`--depth deep`) = 50+ files.

**Required fields in every file**:
- `orientation` — what this role is fundamentally trying to accomplish
- `lens` — the specialized viewpoint this role brings to decisions
- `expertise` — specific skills, domains, tools this role owns
- `scope` — what this role decides alone vs. coordinates vs. escalates
- `collaborates_with` — roles this role has high-bandwidth relationships with

**Area subdirectories**: Group roles under minimum 2 area subdirs under `.roles/`.

**Coverage for standard depth**: engineering, product, design, data/analytics, platform/infrastructure, customer-facing, governance. The inertia-advocate counts toward the total.

---

## Inputs

Use provided scan results or repo context. If absent: assume a mid-stage B2B SaaS team, ~25 people.

---

## Completion Check

- `FLAT-CASE-PRESSURE` rating is exactly one of: LOW, MEDIUM, HIGH
- Exactly one verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
- `inertia-advocate.md` exists with all 5 fields populated (not boilerplate — specific to this org)
- ASCII diagram present with 2+ levels
- Headcount table has `Decides` and `Escalates` columns
- Role count in range for depth flag
- Anti-pattern rows use `[element] (cat-N) —` format
- Evolution roadmap has 2+ rows with different trigger types
```

---

## V-04 — Axis: Phrasing Register (Conversational Imperative)

**Hypothesis**: Short, direct imperative sentences reduce parsing overhead and keep the model focused on producing artifacts rather than reasoning about producing artifacts.

```markdown
Build a complete org model. Two outputs: `org-chart.md` and a set of `.roles/` files.

Start with org-chart.md. Build it in this order:

---

**1. ASCII org diagram.**

Draw the hierarchy. Use box-and-line style. Show at least 2 levels. Don't use a flat list — use actual boxes connected by lines.

---

**2. Headcount table.**

Five columns: `Area | Headcount | Key Roles | Decides | Escalates`

`Decides` = what this area owns outright. `Escalates` = what goes up. Both columns required. At least 3 rows.

---

**3. Flat-case pressure check.**

Answer one question: is flat structure a legitimate competitor here, or is structure clearly warranted?

Write:
```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
[One sentence on what's driving this rating]
[CAN-OPERATE-FLAT: condition] OR [STRUCTURE-WARRANTED: signal]
```

Pick one verdict. Not both.

---

**4. Operating rhythm.**

Table: `Meeting | Cadence | Owner | Attendees | Key Output`

Three rows minimum. Include: ROB (review of business), Shiproom, and a Governance meeting. These are different meeting types — don't use three ROBs.

---

**5. Committee charters.**

One charter per governance meeting from step 4. Each charter: Name, Purpose, Membership, Quorum (write it as `N of M`, e.g., `3 of 5`), Escalation path, Output artifact.

---

**6. Evolution roadmap.**

Table: `Trigger | Type | New Structure | Owner`

Two rows minimum. First row: a headcount threshold. Second row: something else — capability gap, funding stage, geographic expansion, etc. Different types only.

---

**7. Anti-pattern watch.**

Table: `Anti-Pattern | Why It Applies Here | Signal to Watch`

Two rows minimum. In the "Why It Applies Here" cell, open with: `[element name] (cat-N) —` then the explanation.

Category codes: cat-1=coordination overhead, cat-2=single point of failure, cat-3=authority ambiguity, cat-4=role duplication, cat-5=missing expertise.

---

Now build the role files.

---

**8. Inertia-advocate role (first, required, non-optional).**

File: `.roles/governance/inertia-advocate.md`

Five fields:
- `orientation` — what this role is trying to accomplish
- `lens` — what a status-quo defender would cite when arguing the current structure works fine
- `expertise` — what they know that others don't (org history, informal networks)
- `scope` — what they influence; at what threshold they'd say structure is warranted
- `collaborates_with` — who they work with

Make it specific. Don't write boilerplate.

---

**9. All other roles.**

One file per role: `.roles/{area}/{role-name}.md`

Same five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. All five. Every file.

Group by area subdirectory. At least 2 subdirs.

Standard depth: 20–30 files total (including inertia-advocate).
Deep (`--depth deep`): 50+ files.

Cover: engineering, product, design, data/analytics, platform, customer-facing, governance.

---

**Inputs**: Use scan results or repo context. If neither: assume a 25-person B2B SaaS product team.

**Before finishing, check:**
- ASCII diagram has boxes and lines (not a flat list)
- Headcount table has Decides + Escalates
- FLAT-CASE-PRESSURE is LOW, MEDIUM, or HIGH
- Verdict is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (not both)
- inertia-advocate.md exists and has all 5 fields
- Role count: 20–30 or 50+
- Every anti-pattern row opens with `[element] (cat-N) —`
- Evolution roadmap has 2+ rows with different trigger types
```

---

## V-05 — Axis: Combination (Lifecycle Emphasis + Inertia Framing + Role Sequence)

**Hypothesis**: Making the skill explicitly lifecycle-aware (scan → assess → design → document) with inertia-advocate as the structural gate between assess and design phases produces the most coherent artifact set — the flat-case assessment directly shapes which roles get generated and how their `scope` fields are written.

```markdown
You are running the org-build skill. It operates in four phases. Complete each phase before the next.

---

## Phase A — Scan

Read the inputs: scan results, repo structure, or contextual signals. Extract:

- **Team signals**: approximate headcount, seniority distribution, known roles or titles
- **Coordination signals**: communication patterns, escalation paths, known friction points
- **Domain signals**: product areas, technical domains, customer segments served
- **Growth signals**: trajectory, funding stage, hiring plan if known

If no inputs are provided, assume: B2B SaaS, ~25 people, Series B stage, single product, remote-first.

Produce a 3–5 bullet **Scan Summary** at the top of `org-chart.md`.

---

## Phase B — Assess (Flat vs. Structure)

Before designing anything, assess whether structure is warranted.

**B1. Flat-Case Argument**

Write 2–3 sentences describing the strongest case for staying flat. Draw on the scan signals. Be honest — if the flat case is strong, say so.

**B2. Structure Argument**

Write 2–3 sentences describing what the scan signals indicate about coordination overhead, ownership ambiguity, or scale pressure that argues for structure.

**B3. Rating and Verdict**

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]

[One sentence tying the rating to the specific scan signals that drove it]

[CAN-OPERATE-FLAT: specific condition under which flat remains viable]
  OR
[STRUCTURE-WARRANTED: specific signal from the scan that tips the balance]
```

Issue exactly one verdict.

**B4. Inertia-Advocate Gate**

Create `.roles/governance/inertia-advocate.md` now, before the org diagram. This role's `scope` field must reference the FLAT-CASE-PRESSURE rating from B3:
- If HIGH: scope includes "advocate for preserving flat coordination until [specific threshold]"
- If MEDIUM: scope includes "flag structural proposals that add overhead without resolving the coordination failures identified in scan"
- If LOW: scope includes "track residual flat-case pressure; escalate if structure creates more overhead than it eliminates"

Fields required: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

---

## Phase C — Design (Org Structure)

Produce the main body of `org-chart.md`.

**C1. ASCII Hierarchy Diagram**

Box-and-line diagram. Minimum 2 levels. Derive the structure from Phase B — if FLAT-CASE-PRESSURE was HIGH, the structure should be shallow (few levels, wide spans). If LOW, structure can be deeper.

```
┌─────────────────────────────────┐
│  [Org Name / Product Name]      │
│  [Accountable Role]             │
└──────────┬──────────┬───────────┘
           │          │
    ┌───────┴───┐ ┌────┴───────┐
    │  [Area]   │ │  [Area]    │
    └───────────┘ └────────────┘
```

**C2. Headcount by Area**

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Minimum 3 rows. `Decides` and `Escalates` columns required. Derive `Decides`/`Escalates` boundaries from the coordination failures identified in Phase B.

**C3. Operating Rhythm**

| Meeting | Cadence | Owner | Attendees | Key Output |
|---------|---------|-------|-----------|------------|

Minimum 3 rows. Required types: ROB, Shiproom, Governance. Each must be a distinct meeting type.

**C4. Committee Charters**

One per governance meeting. Each: Name, Purpose, Membership, Quorum (`N of M` format), Escalation path, Output artifact.

**C5. Org Evolution Roadmap**

| Trigger | Type | New Structure | Owner |
|---------|------|---------------|-------|

Minimum 2 rows, different trigger types. At least one headcount threshold. At least one non-headcount trigger.

**C6. Anti-Pattern Watch**

| Anti-Pattern | Why It Applies Here | Signal to Watch |
|--------------|---------------------|-----------------|

Minimum 2 rows. "Why It Applies Here" must open with `[element name] (cat-N) —`.
- cat-1: coordination overhead, cat-2: single point of failure, cat-3: authority ambiguity, cat-4: role duplication, cat-5: missing expertise

Anti-patterns should reflect the specific structure chosen in C1 — if you designed a flat org, the anti-patterns should be cat-3 and cat-2; if deep hierarchy, cat-1 and cat-4.

---

## Phase D — Document (Role Files)

Generate `.roles/{area}/{role-name}.md` for every role.

**Depth**: Standard = 20–30 files. Deep (`--depth deep`) = 50+ files. The inertia-advocate (created in Phase B) counts.

**Role file format** — five fields, all required:

```yaml
orientation: |
  [What this role is fundamentally trying to accomplish]

lens: |
  [The specialized viewpoint this role brings to every decision]

expertise: |
  [Specific skills, domains, tools, methods this role owns]

scope: |
  [Unilateral decisions vs. coordinated decisions vs. escalation triggers.
   Be specific — derive from the Decides/Escalates columns in the headcount table.]

collaborates_with: |
  [Comma-separated list. Note frequency: daily, weekly, or event-driven.]
```

**Sequencing**: Generate roles in this order:
1. Inertia-advocate (already done in Phase B — verify it's complete)
2. The accountable/top-level role
3. Area leads (one per area in the headcount table)
4. Contributing roles within each area
5. Cross-functional or shared-service roles last

**Coverage for standard depth**: engineering, product, design, data/analytics, platform, go-to-market, governance.

**Area subdirectories**: minimum 2 under `.roles/`.

---

## Completion Verification

Walk this checklist before finishing:

- [ ] Scan Summary present in org-chart.md
- [ ] FLAT-CASE-PRESSURE is LOW, MEDIUM, or HIGH
- [ ] Exactly one verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED)
- [ ] inertia-advocate scope references the FLAT-CASE-PRESSURE rating
- [ ] ASCII diagram has boxes and lines, minimum 2 levels
- [ ] Headcount table has all 5 columns including Decides and Escalates
- [ ] Operating rhythm has 3+ rows with distinct meeting types
- [ ] Each governance meeting has a charter with Quorum as N of M
- [ ] Evolution roadmap has 2+ rows with different trigger types
- [ ] Anti-pattern rows open with `[element] (cat-N) —`
- [ ] Role count: 20–30 (standard) or 50+ (deep)
- [ ] All role files have all 5 required fields
- [ ] Role files grouped under minimum 2 area subdirs
```

---

## Variation Summary

| Variation | Axis | Hypothesis | Key Differentiator |
|-----------|------|------------|--------------------|
| V-01 | Role Sequence | Anchoring inertia-advocate first colors all subsequent roles | IA generated in Step 1, rest of org follows |
| V-02 | Output Format | Explicit templates reduce field omissions | Every section has a fill-in schema |
| V-03 | Inertia Framing | Flat as named competitor sharpens ratings | Flat-case phase before org diagram |
| V-04 | Phrasing Register | Short imperatives reduce parsing overhead | Numbered bullets, no explanation prose |
| V-05 | Combination (Lifecycle + Inertia + Sequence) | Phase gates produce coherent cross-artifact consistency | Scan → Assess (IA gate) → Design → Document |
