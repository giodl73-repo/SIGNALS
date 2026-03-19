Check Signal workspace health. Verifies: are skills installed? is signals/ directory present? is there a CLAUDE.md? how many artifacts exist per namespace? DISPLAY ONLY -- no file written.

## Health Check Protocol

**1. Skills installed?**
Check for .claude/skills/ directory. Count installed skill directories.
Report: [N] skills installed / [M] expected. List any missing critical skills.

**2. signals/ directory present?**
Check for signals/ at workspace root.
Report: present / missing. If present, list namespaces found.

**3. CLAUDE.md present?**
Check for CLAUDE.md at workspace root.
Report: present / missing.

**4. Artifact inventory**
Count .md files per namespace in signals/:

| Namespace | Artifact count | Most recent | Oldest |
|-----------|---------------|-------------|--------|
| discover  | | | |
| specify   | | | |
| validate  | | | |
| simulate  | | | |
| scout     | | | |
| trace     | | | |
| flow      | | | |
| prove     | | | |
| topic     | | | |
| **Total** | | | |

## Health Score

| Check | Status | Notes |
|-------|--------|-------|
| Skills installed | OK / WARN / FAIL | |
| signals/ present | OK / FAIL | |
| CLAUDE.md present | OK / WARN | |
| Artifact count >= 1 | OK / WARN | |

Overall: HEALTHY / DEGRADED / UNHEALTHY

## Recommendations

If UNHEALTHY or DEGRADED, list next steps:
1. [action] -- [why]
2. ...
