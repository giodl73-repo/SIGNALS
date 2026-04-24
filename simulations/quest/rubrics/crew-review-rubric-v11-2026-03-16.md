**v11 written.** Here is the extraction:

---

## New criterion: C-33

**G2 Closure Predicate — Quantified N-Verdict-for-N-Slot Form**

| Field | Value |
|-------|-------|
| Source | V-01 R11 C-27 evidence: "G2 checks N verdicts for N slots" |
| Extends | C-32, by the same step C-20 extends C-17 |
| Structural logic | C-32 requires a named G2 gate with a per-slot closure condition. C-33 requires that condition to be **quantified against the LOAD manifest cardinality** — not merely narrative ("synthesis done"). The predicate becomes machine-checkable: verdict count == slot count. |

**Chain tail update:**
```
C-07 -> C-22 -> C-27 -> C-31 -> C-32 -> C-33
```

The step is exact: C-32's own pass condition already flagged it — *"a named gate with a multi-condition closure predicate (C-20 pattern applied to synthesis) would exceed C-32."* That signal is now in evidence.

---

**Scoring delta:**

| | v10 | v11 |
|-|-----|-----|
| Aspirational count | 21 | 22 |
| Aspirational max | 52.5 | 55.0 |
| Total max | 172.5 | 175.0 |
| V-01 R11 | 172.5 | **175.0** |
| R10 variations | 167.5 | **167.5** (unchanged — C-33 FAIL in R10) |
