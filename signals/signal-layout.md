You are running /layout for: {{workspace}}

Scan the .claude/skills/ directory in the current workspace and help the team understand,
organize, and navigate their skills. This works on ANY skills — Signal-installed, custom-built,
or a mix of both.

---

## Step 1: Scan and inventory

Read every SKILL.md in .claude/skills/ (including subdirectories).
For each skill extract: name, description (first line), tools, tier (T1/T3).

Build a catalog:
- Total skill count
- Skills by namespace/prefix (group by common prefix: scout-, trace-, etc.)
- Skills without a clear namespace (standalone names)
- T3 skills (full golden body) vs T1 skills (lightweight pointer)
- Any skills that appear to be drafts or stubs (very short body, generic description)

---

## Step 2: Show the inventory

```
Skills in this workspace: N total

BY GROUP:
  scout     8 skills  → /scout-competitors, /scout-feasibility, ...
  trace     7 skills  → /trace-contract, /trace-state, ...
  [custom]  3 skills  → /my-deploy, /my-review, /my-test

QUALITY:
  Golden (full body):  N  ████████████
  Draft (stub/short):  N  ███
  Unknown:             N  █

SUGGESTIONS:
  → 3 skills have no description — consider adding one
  → /deploy and /deploy-prod may be duplicates
  → 4 skills have no examples section
```

---

## Step 3: Offer actions

Ask the user what they want to do:

**A. Generate an index**
Create docs/COMMANDS.md listing all skills with: name, bare form, description.
"Type /name → description" format, one line per skill, alphabetical.

**B. Suggest groupings**
Analyze skill names and descriptions. Propose 3-5 logical groups the team could navigate by.
Example: "Your skills naturally group into: deploy (4), review (3), test (2), setup (2)"
Show how a grouped binding would look.

**C. Find gaps**
Compare skills to common workflows. What's missing?
"You have /deploy but no /rollback. You have /review but no /review-code."

**D. Audit quality**
Score each skill on: has-description, has-examples, has-error-handling, body-length.
Flag skills that are too short (<100 words) or have generic descriptions.

**E. Export**
Write a SKILLS.md summary file to .claude/ that documents the skill set.
Format: name, invocation, description, when to use.

---

## AMEND

1. **Filter by group**: Focus on one prefix or namespace only
2. **Include T3 only**: Show only skills with full golden bodies
3. **Compare two directories**: Compare .claude/skills/ against another workspace's skills
