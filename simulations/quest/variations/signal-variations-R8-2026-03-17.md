---

# Quest Variate -- /signal (Round 8)

**Skill**: `signal` | **Rubric**: v8 (C-01 through C-27, 19 aspirational)
**Base**: R7 V-05 at 100.00 under v8. All five R8 variations carry the full R7 V-05 mechanism set.

---

## Context

R7 V-05 is the ceiling at 100.00/100 under v8. R8 probes for excellence signals beyond that ceiling. Three structural gaps identified in R7 V-05:

| Axis | Gap | Structural precedent |
|------|-----|---------------------|
| **J** | FULL MODE has no emit-order check. C-25 verifies presence + count; a model could reorder namespaces and still pass. | BARE MODE has C-21 (begin/end anchors). FULL has none. |
| **K** | FILTER MODE compliance gate has scope + count (C-20) but no format check. A malformed-but-correctly-scoped filter output passes. | BARE MODE compliance gate has a format check (C-18 Check 1). FILTER has none. |
| **L** | BARE MODE says "No `/` prefix" but all catalog entries carry `/`. No transformation example is given. Model must infer the strip rule. | C-16 (per-row example-pad) established that worked examples outperform stated rules. |

---

## Spread Design

| V | Axis | Change from R7 V-05 | Predicted |
|---|------|---------------------|-----------|
| V-01 | J single | Add Check 3 (order) to COMPLIANCE GATE -- FULL MODE: canonical sequence scout...org, restart if violated | 100.00 |
| V-02 | K single | Add Check 3 (format) to COMPLIANCE GATE -- FILTER MODE: SECTION FORMAT compliance verified, restart if violated | 100.00 |
| V-03 | L single | Add slash-strip transformation rule to BARE MODE with first+last worked examples | 100.00 |
| V-04 | J+K | FULL order check + FILTER format check; no slash-strip | 100.00 |
| V-05 | J+K+L | Triple convergence; all three axes | 100.00 |

---

## Variation Summaries

### V-01 (Axis J) -- FULL MODE Order Check
COMPLIANCE GATE -- FULL MODE gains a **Check 3 (order)**:
```
Check 3 (order): Are namespace sections emitted in canonical order?
  Canonical order: scout, draft, review, flow, trace, prove, listen, program,
  topic, quest, mock, org. (First section: scout. Last section: org.)
  If any section appears out of canonical sequence -- order violated. Restart.
```
All other mechanisms unchanged from R7 V-05.

### V-02 (Axis K) -- FILTER MODE Format Check
COMPLIANCE GATE -- FILTER MODE gains a **Check 3 (format)**:
```
Check 3 (format): Does the filter output follow SECTION FORMAT?
  Required: header line, sub-skill lines with -> separator, dispatch footer.
  If any element absent or malformed -- FILTER output format violated. Restart.
```

### V-03 (Axis L) -- BARE MODE Slash-Strip Example
BARE MODE gains an explicit transformation rule:
```
Slash-strip transformation: catalog entries carry a leading `/`. Strip it.
  `/scout-competitors` becomes `scout-competitors`  (first entry)
  `/org-committee`     becomes `org-committee`      (last entry)
Remove only the leading `/`. No other characters change.
```

### V-04 (Axes J+K) -- FULL Order + FILTER Format
Combines V-01 and V-02. No slash-strip. Confirms J and K are independently additive.

### V-05 (Axes J+K+L) -- Triple Convergence (Golden Target)
All three axes. The three changes from R7 V-05: FULL gate Check 3 (order), FILTER gate Check 3 (format), BARE MODE slash-strip with first+last examples.

---

Output saved to: `simulations/quest/golden/signal-variate-R8-2026-03-17.md`
