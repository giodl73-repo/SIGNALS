---
mode: agent
description: "Inspect the installed role registry in .craft/roles/. Maps roles by domain into an org chart display. No file written — display only."
---
Workspace: {workspace}   # infer from cwd if not provided

---

## PHASE 1 — ROLE REGISTRY SCAN

Glob .craft/roles/**/*.md — list all role files found.

If .craft/roles/ does not exist:

```
No roles installed.
Run /roles-build to create your first role, or install domain roles with install-roles.sh.
```

Stop here if no roles directory found. Do not write a file.

---

## PHASE 2 — ROLE GROUPING

For each role file found, extract:
- Directory path (= domain)
- Role name (from `name:` field in frontmatter or filename)
- orientation.serves (one-liner from role file, or filename if unreadable)

Group by directory. If a role file cannot be read, list it as "[unreadable — path only]".

| Domain | Role slug | orientation.serves |
|--------|-----------|--------------------|
| [dir] | [slug] | [one-liner] |
| ... | | |

Total found: [N] roles across [M] domains

---

## PHASE 3 — ORG CHART DISPLAY

```
ROLE REGISTRY: {workspace}
========================

Domain: {domain-1}
  - {role-slug}: {orientation.serves one-liner}
  - {role-slug}: {orientation.serves one-liner}

Domain: {domain-2}
  - {role-slug}: {orientation.serves one-liner}
  ...

========================
Total: {N} roles across {M} domains

Coverage gaps:
  {list any standard domains with no roles installed}
  Standard domains: signal, craft, platform, security, data, ops
  Missing: {list missing domains, or "None — all standard domains covered"}
```

Coverage gap logic: compare installed domains against the standard domain list
[signal, craft, platform, security, data, ops]. Any standard domain with zero installed
roles is a gap. If all 6 are covered, report "None."

---

DISPLAY ONLY — no file is written by this skill. This is a workspace inspection command.
