`trace-skill-variate-R4-v3-2026-03-15.md` written. Here's the structure:

---

## Round 4 — 5 Variations Against Rubric v3

**Entry state**: R3 V-05 achieves all 17 criteria. R4 explores alternative structural paths that surface three residual patterns not yet formalized in v3.

**Three R4 patterns identified from R3 V-05 execution**:

| Pattern | Gap in R3 V-05 | Potential v4 criterion |
|---------|---------------|----------------------|
| Relay-to-Bind provenance | Relay Binding column cites input name only — resolved value not carried, chain unverifiable | Relay must carry `InputName = "ResolvedValue"` per row |
| Per-row conflict annotation | C-17 rule declared as block; no per-row trace of which branch resolved each decision | Bind table gains `Precedence applied` column: `override \| default \| BLOCKED` |
| Coverage Matrix self-closure | BLOCKED gate passes silently; no named assertion the Verdict can cite as structural evidence | Explicit "Coverage Matrix: CLOSED" assertion after gate clears |

**Variation axes**:

- **V-01** (Single / Output format): Relay Binding column carries `InputName = "ResolvedValue"` pairs. Entire R3 V-05 architecture intact, relay table format changed.
- **V-02** (Single / Phrasing register): Each phase opens with 2–3 criterion-aligned self-check questions answered before content. Tests whether embedded compliance questions are as effective as structural tables.
- **V-03** (Single / Lifecycle emphasis): Bind gains `Precedence applied` column. C-17 becomes traceable per row, not just at declaration. Verdict C-17 evidence cites the column.
- **V-04** (Combined / Output format + lifecycle emphasis): All three R4 patterns together — relay provenance + per-row conflict + Coverage Matrix closure assertion.
- **V-05** (Combined golden): Full R3 V-05 architecture + all three R4 patterns. Seven-column Bind table; relay Binding carries verbatim resolved values; CLOSED assertion after gate; Verdict evidence rows updated to cite all new structural elements.
