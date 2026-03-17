Rubric written to `simulations/quest/rubrics/topic-open-rubric-v1-2026-03-17.md`.

---

## Summary

**5 essential** (must all pass):
- **C-01** — TOPICS.md entry exists with slug, description, date
- **C-02** — Strategy at correct path `simulations/{topic}/strategy.md`
- **C-03** — All five signal fields present in every row (namespace, skill, item name, owner role, priority)
- **C-04** — Priority vocabulary is valid (`essential`/`recommended`/`optional` only — no substitutions)
- **C-05** — At least one essential signal declared (implicit commit gate required)

**3 recommended**:
- **C-06** — Signal set spans 2+ namespaces
- **C-07** — Prose rationale present (why this topic, what decision it informs)
- **C-08** — Owner roles differentiated (2+ distinct roles)

**2 aspirational**:
- **C-09** — Explicit COMMIT GATE section naming the minimal required signal set
- **C-10** — Item names follow `{topic}-{signal}-{date}.md` convention

**Golden threshold**: all 5 essential pass + composite >= 80.

The hardest failure to catch is **C-04** — models routinely substitute `high/medium/low` for the canonical vocabulary, silently breaking commit gate logic downstream.
