**R13 variations written.** Here's the summary:

---

## R13 Variation Summary

| V | Axis | C-34 | C-35 | C-36 | Predicted |
|---|------|------|------|------|-----------|
| **V-01** | Regression: C-34 advisory — Step 8 Header reverts to prose re-affirmation; VT-N quoted schema + TOKEN-COUNT removed; Row-Verdict/CHECK RESULT kept | FAIL | PASS | FAIL | 225/235 |
| **V-02** | Regression: C-35 advisory — VT-N schema + TOKEN-COUNT kept; Row-Verdict column + CHECK RESULT removed; CONTRADICTION HALT prose-only | PASS | FAIL | FAIL | 225/235 |
| **V-03** | Output format: CHECKER ALGORITHM block in Step 8 Header — declares `MATCH-RULE`, `HALT-RULE`, `OUTPUT-RULE` as formal pseudocode tokens immediately after TOKEN-COUNT; comparison predicate machine-readable without semantic reading | PASS | PASS | PASS | 235/235 + C-37 ES-1 |
| **V-04** | Lifecycle emphasis: Step 8d CHECKER INVOCATION gate — REQUIRED named lifecycle step after Step 8c; formal inputs (`schema_lines`, `schema_count`, `algorithm`, `table_rows`, `verdict_column`), PRECONDITION CHECK (TOKEN-COUNT validation), arithmetic EXECUTION, typed CHECKER OUTPUT | PASS | PASS | PASS | 235/235 + C-37 ES-2 |
| **V-05** | Combination V-03 + V-04 — algorithm declared at Step 8 Header (rule tokens), invoked at Step 8d (procedure); full tool contract: parse header → verify TOKEN-COUNT → apply MATCH-RULE/HALT-RULE → invoke Step 8d → emit CHECK RESULT. Also opens C-38 surface: SCHEMA COUNT ERROR as typed precondition halt | PASS | PASS | PASS | 235/235 + C-37 ES-3 |

**Key design choices:**
- V-01/V-02 are cleanly separated regressions — each drops exactly one promoted criterion while holding the other intact
- V-03's `MATCH-RULE`/`HALT-RULE`/`OUTPUT-RULE` are machine-greppable tokens independent of the Step 8 Header schema tokens
- V-04's Step 8d `PRECONDITION CHECK` introduces `SCHEMA COUNT ERROR` as a bonus signal (C-38 surface)
- V-05 separates algorithm declaration from invocation as distinct structural events, making each independently greppable
ed rule declaration that makes
  the comparison predicate machine-readable without prose. MATCH-RULE, HALT-RULE, OUTPUT-RULE
  are the machine-greppable tokens. This is the C-37a pre-condition: the algorithm is declared
  as structural tokens within the prompt.

**The C-37 design surface (V-04/V-05):** Step 8d CHECKER INVOCATION lifts the checker from
an embedded note to a first-class lifecycle event. V-05 combines algorithm declaration (Step
8 Header) with invocation protocol (Step 8d) -- if both properties appear consistently across
R13 rounds, the full C-37 checker contract (input schema + output tokens + algorithm + invocation)
is specifiable from structural tokens alone.

**C-38 surface opened by V-04/V-05:** The Step 8d PRECONDITION CHECK introduces SCHEMA COUNT
ERROR as a named halt type -- the checker's input validation is itself a structural event. If
R13 produces consistent evidence that TOKEN-COUNT mismatch is handled as a typed halt (not
silent failure), C-38 becomes a candidate: schema self-validation as a required structural
property of the Step 8 Header.
