---
skill: quest-rubric
skill_target: signal
date: 2026-03-17
version: 1
---

# Scoring Rubric: `/signal`

**Skill description**: Show the Signal command index. Lists all available skills organized by
namespace with one-line descriptions. Supports `/signal` (full index), `/signal <namespace>`
(namespace-scoped), and `/signal --bare` (bare command names only).

---

## Essential Criteria

*All must pass. Without these the output is not useful.*

### C-01 — All 12 namespaces present
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Output contains all 12 namespaces by name: `scout`, `draft`, `review`,
  `flow`, `trace`, `prove`, `listen`, `program`, `topic`, `quest`, `mock`, `org`. Missing
  any namespace is an automatic fail.

### C-02 — Sub-skills listed per namespace
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Every namespace section shows its sub-skills as individually named
  commands (e.g. `/scout-competitors`, `/draft-spec`). A namespace shown with zero sub-skills
  listed fails this criterion.

### C-03 — One-line description per sub-skill
- **Category**: format
- **Weight**: essential
- **Pass condition**: Every sub-skill entry includes a non-empty description. A raw command
  list with no descriptions fails. Descriptions must be on the same line or directly associated
  with the command, not buried in prose.

### C-04 — `--bare` mode produces command names only
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal --bare`, output contains only bare command names
  (e.g. `scout-competitors`) with no descriptions, no namespace headers, and no prose. One
  command per line. If `--bare` is not handled and the full index is emitted instead, fails.

### C-05 — `<namespace>` filter scopes output correctly
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal <namespace>` (e.g. `/signal flow`), output
  shows only the skills in that namespace. Skills from other namespaces must not appear. If
  no filtering occurs and the full index is returned, fails.

---

## Recommended Criteria

*Output is meaningfully better with these. Combined weight = 30 pts.*

### C-06 — Sub-skill count per namespace is accurate
- **Category**: correctness
- **Weight**: recommended
- **Pass condition**: The skill count stated in each namespace header matches the actual number
  of sub-skills listed. Authoritative counts: scout=8, draft=4, review=4, flow=7, trace=7,
  prove=9, listen=3, program=2, topic=6, quest=4, mock=3, org=4. Off-by-one or missing count
  annotation is a soft fail.

### C-07 — Each namespace includes a dispatch footer
- **Category**: format
- **Weight**: recommended
- **Pass condition**: Each namespace section ends with a "Run any sub-skill directly, or
  describe your [X] and the most relevant skill will run" guidance line. This signals the
  namespace is entry-point friendly. Missing footers in 3+ namespaces fails.

### C-08 — Namespace headers state the namespace purpose
- **Category**: coverage
- **Weight**: recommended
- **Pass condition**: Each namespace header includes a brief purpose phrase (e.g. "Scout
  namespace -- 8 skills for discovery and research"). A bare namespace name with no context
  phrase fails. At least 8 of 12 namespaces must have annotated headers to pass.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 — Sub-skill descriptions match canonical one-liners
- **Category**: correctness
- **Weight**: aspirational
- **Pass condition**: Sub-skill descriptions match (or are semantically equivalent to) the
  authoritative one-liners in `output/T1/CLAUDE.md`. Minor paraphrase is acceptable; omitting
  a key distinguishing detail (e.g. "inertia as primary competitor" for scout-competitors) is
  a soft fail. At least 80% of sub-skills must match to pass.

### C-10 — Output is scannable without overwhelming
- **Category**: format
- **Weight**: aspirational
- **Pass condition**: Full-index output uses consistent visual alignment (e.g. `->` separator,
  consistent indentation). Namespace sections are visually separated. No sub-skill description
  wraps to create orphan lines that break the scan rhythm. A human can locate any skill within
  10 seconds of scanning.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Shippable — meets the bar |
| Silver | >= 60, all essential pass | Useful but polish needed |
| Bronze | any essential fail | Not yet useful |

---

## Evaluation Notes

- Criteria C-04 and C-05 require specific invocation modes. If a single run is being scored
  (not a multi-mode run), mark C-04 and C-05 as N/A and adjust the essential denominator to 3.
  Composite formula becomes: `(essential_pass/3 * 60) + ...`
- C-06 counts are authoritative as of 2026-03-17. If new sub-skills are added to a namespace,
  update the counts before scoring.
- The dispatch footer text (C-07) may vary in phrasing; the key signal is that it is present
  and invites open-ended invocation.
