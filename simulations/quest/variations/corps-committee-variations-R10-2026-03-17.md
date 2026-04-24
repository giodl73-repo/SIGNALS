Here are the 5 complete, runnable variations for **corps-committee Round 10**:

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Per-block COMMIT seals (C-31) — single axis | Emitting explicit B1/B2/B3/B4 COMMIT seals after each block's content — before any downstream block or phase begins — makes availability explicit rather than implied by ordering. A downstream block cannot cite a B3 token before B3-COMMIT appears. |
| **V-02** | TOKEN TRACE CONFIRMATION in Phase 2 (C-32) — single axis | A named TOKEN TRACE CONFIRMATION table inside Phase 2 output re-validates each inertia token against its consumption sites. The TRACE GATE ensures tokens *enter* Phase 2; the CONFIRMATION ensures they *survive* to output. Gate-cleared dropouts are only detectable with an active Phase 2 re-validation. |
| **V-03** | AMEND-AFFECTED SITES notation (C-33) — single axis | Emitting an AMEND-AFFECTED SITES block listing every stale element by structural reference and affected token *before* re-execution begins makes amendment impact visible at the artifact layer, not just the routing layer. A reviewer can verify scope before any phase re-executes. |
| **V-04** | C-31 + C-32 combination | COMMIT seals and TOKEN TRACE CONFIRMATION close different windows in the same audit chain: COMMIT seals close the pre-execution availability window; CONFIRMATION closes the Phase 2 output survival window. Together: token minted (B3) → sealed (B3-COMMIT) → cited under seal → gate-cleared → confirmed at output. Any broken link is visible at the layer where it breaks. |
| **V-05** | Full integration: C-31 + C-32 + C-33 + best of R9 | Integrates all three new R10 criteria with the complete R9 best architecture (BLOCK DEPENDENCY MAP, TOKEN TRACE MANIFEST gate, AMEND routing table, vocabulary contract, tier-sequenced production, per-tier column grammar, inertia token anchoring in dissent, standalone Challenger block). Each mechanism closes its own window; none relies on another to cover its gap. |

---

**Key structural moves across the five variations:**

- **V-01** introduces the `B1-COMMIT / B3-COMMIT / B2-COMMIT / B4-COMMIT` seal pattern with an explicit note at each seal: "citation of tokens from this block before this COMMIT line = FAIL C-31"
- **V-02** adds the `### TOKEN TRACE CONFIRMATION` table inside Phase 2 as a named, mandatory section with a DROPOUT REPAIR rule and explicit cross-reference against the Phase 1 TOKEN TRACE MANIFEST
- **V-03** introduces the three-step AMEND process with the `AMEND-AFFECTED SITES` block as Step 2, including worked examples for composition change and committee type change
- **V-04** combines V-01 + V-02 and makes the two-window framing explicit in the block dependency map's downstream consumption obligations
- **V-05** fully integrates all R10 new criteria plus R9 complete architecture, with the AMEND-AFFECTED SITES block handling inertia finding corrections as a new amendment type (triggering B3 re-run)
