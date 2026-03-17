Written to `simulations/quest/golden/campaign-brief-variate-R16-2026-03-17.md`.

---

## R16 Variations Summary

**Single axis of variation:** The companion-activation instruction components in the execution-note clause bodies. All five variations are identical on C-01 through C-34. The v15 ceiling is 350 pts.

| Var | STATUS body | STORY body | Expected |
|-----|-------------|------------|----------|
| V-01 | C-34 PASS -- membership + independence (no companion-activation) | Same | 340/350 (C-35 PARTIAL) |
| V-02 | C-34 PASS + companion named by designation, no activation rules | Same | 340/350 (C-35 PARTIAL) |
| V-03 | C-34 PASS + companion named + present-state rule only (absent-state omitted) | Same | 340/350 (C-35 PARTIAL) |
| V-04 | C-35 PASS standard -- all three components, absent-state: "activates independently -- companion's absence does not suppress" | Same | 350/350 (C-35 PASS) |
| V-05 | C-35 PASS extended -- absent-state: "execute this clause's mandate fully; treat absent companion's mandate as independently operative" | Same | 350/350 + R16 investigation |

**Three PARTIAL bands confirmed by design:**
1. V-01: no companion-activation (C-35 absent entirely)
2. V-02: companion identified but activation contract absent
3. V-03: activation contract incomplete (present-state only -- the structurally important absent-state rule missing)

**R16 behavioral investigation (V-04 vs V-05):**
- V-04 absent-state rule: authorizes independent activation, companion acknowledged as absent
- V-05 absent-state rule: extends to "treat absent companion's mandate as independently operative" -- tests whether a model encountering only the STORY body under double-elision enforces timestamp isolation on `found` entries (the companion's mandate) without the TIMESTAMP ISOLATION execution note being present

If V-05 produces observable timestamp isolation enforcement from the STORY body alone, the extension reaches inferred two-mechanism activation. If V-04 and V-05 produce identical behavior, the extension is structural documentation without additional behavioral reach -- and C-35's scope is bounded to single-clause full authority with companion gap acknowledged.
