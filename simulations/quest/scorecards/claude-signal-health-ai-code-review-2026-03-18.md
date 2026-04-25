Now I have everything needed. Here is the health report:

---

## Signal Health — Topic: `ai-code-review`

### 1. Skills Installed?

- **Global `~/.claude/skills/`**: 1 entry (`review-paper/`) — no Signal skills
- **Local `.claude/skills/`**: directory does not exist — 0 entries
- **Signal skill definitions in `signals/` root**: **134 files** (operative — skills invoked directly from these files)

Signal skills are not registered in `.claude/skills/` but are functional as inline skill invocations from the `signals/` flat-file definitions. Evidence: 16 artifacts produced successfully.

**Result**: WARN — 134 skill defs present and working; not formally registered in `.claude/skills/`

---

### 2. signals/ Directory Present?

**Present** at `sim/signals/`

Namespaces with artifact subdirectories (6 of 9):
- `discover/`, `specify/`, `validate/`, `simulate/`, `rhythm/`, `roles/`

Namespaces missing subdirectories (no artifacts yet):
- `scout/`, `trace/`, `flow/`, `prove/`, `topic/`

---

### 3. CLAUDE.md Present?

**Present** at `sim/CLAUDE.md`

---

### 4. Artifact Inventory — `ai-code-review` topic

| Namespace | Artifact count | Most recent | Oldest |
|-----------|---------------|-------------|--------|
| discover  | 6 | 2026-03-19 (competitors, risk, feasibility, websearch) | 2026-03-18 (inertia, hypothesis) |
| specify   | 1 | 2026-03-18 (proposal) | 2026-03-18 |
| validate  | 4 | 2026-03-19 (design v2, customers v2) | 2026-03-18 (design, customers) |
| simulate  | 2 | 2026-03-19 (state v2) | 2026-03-18 (state) |
| rhythm    | 2 | 2026-03-19 (decide v2) | 2026-03-18 (decide) |
| roles     | 1 | 2026-03-18 (check) | 2026-03-18 |
| scout     | 0 | — | — |
| trace     | 0 | — | — |
| flow      | 0 | — | — |
| prove     | 0 | — | — |
| topic     | 0 | — | — |
| **Total** | **16** | 2026-03-19 | 2026-03-18 |

**Bonus**: 19 scorecards in `simulations/quest/scorecards/` (10 claude + 9 github variants for ai-code-review).

---

### Health Score

| Check | Status | Notes |
|-------|--------|-------|
| Skills installed | WARN | 134 skill defs in signals/ root; functional but not in .claude/skills/ |
| signals/ present | OK | 6 namespace subdirs active |
| CLAUDE.md present | OK | Present at workspace root |
| Artifact count >= 1 | OK | 16 artifacts for ai-code-review |

**Overall: DEGRADED**

---

### Recommendations

1. **Run `/signal:topic-new ai-code-review`** (or equivalent) — no `topic/` namespace artifacts exist; the topic narrative has not been written yet
2. **Consider `scout/`, `trace/`, `flow/`, `prove/`** — 5 of 9 namespaces have zero coverage; signal density is concentrated in discover/validate/simulate
3. **Register skills in `.claude/skills/signal/`** if formal installation is required — currently functional via flat-file invocation, but health check cannot verify installed count against expected 47
4. **Commit untracked signals/** — 6 namespace directories are untracked in git; run `git add signals/` to persist artifact history

---

QUALITY: 4
CLAUDE_COMPATIBLE: Y
NOTES: signals/ root flat-files (134) are skill definitions, not artifacts — artifact count (16) reflects only the topic-scoped subdirectory files. No `topic/` namespace artifacts exist, which is the primary gap for a healthy topic story.
