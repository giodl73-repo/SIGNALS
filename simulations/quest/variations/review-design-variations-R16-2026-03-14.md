Written to `simulations/quest/rubrics/review-design-variate-R16-2026-03-15.md`.

---

## Round 16 Variations — Summary

**Baseline**: R15 V-05 (carries C-43 POSITION CONSTRAINT, C-44 bidirectional for all 6 halts, C-45 Elevation Record + CONSENSUS ELEVATION RULE, declarative register; fails C-46 and C-37/F-14).

**New criteria to encode**: C-45 (refine), C-46 (add SEALED gates), C-37 value-naming fix.

---

### Single-axis (V-01 through V-03)

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Lifecycle emphasis — C-46 SEALED gates | R15 V-05 + SEALED attestations after every block. Each names (a) what was verified and (b) what proceeds. Tests whether adding SEALED statements in isolation achieves C-46 pass. |
| **V-02** | Phrasing register — C-37 closed-enumeration value-naming | Fix F-14 to name AGREE/SPLIT explicitly; add F-31 halt on Elevation Record with ELEVATED/BASELINE named; F-02 already names P1/P2/P3. Isolates C-37 pass from SEALED noise. |
| **V-03** | Inertia framing prominence | Elevates the PRESERVATION PRINCIPLE to a named governing constraint (IC-01) declared at lifecycle entry and enforced at BLOCK 5. Also adds a BLOCK 2 prohibition on redesign-recommendation findings. Does NOT encode C-46 or fix C-37 — clean single-axis test. |

### Combination (V-04 through V-05)

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| **V-04** | C-46 SEALED + C-37 value-naming + enriched artifact attestation | SEALED statements enumerate specific F-codes cleared and intermediate artifact produced per block (e.g., "[M] Domain + 6 Stock = [total] reviewers"). Tests whether count-verifiable SEALED content adds enforcement salience beyond minimal attestation. |
| **V-05** | Declarative register + C-46 SEALED + C-37 value-naming + C-45 tiebreaker enumeration + inertia IC-01 | Full combination. SEALED invariants are verbose (names every F-code cleared). CONSENSUS ELEVATION RULE fully enumerates all three tiebreaker levels deterministically. F-31 halt on Elevation Record values. IC-01 as named constraint with explicit prohibition scope. Tests whether full specification achieves ceiling on C-37, C-45, and C-46 simultaneously. |

### Key structural changes across R16

- **F-14** (all variations except V-01/V-03): `"Replace the Type value with AGREE or SPLIT (whichever correctly classifies the row)"` — closes the R15 C-37 fail case
- **F-31** (V-02/V-04/V-05): new halt on Elevation Record Consensus Status cell — `ELEVATED or BASELINE` named explicitly  
- **SEALED statements** (V-01/V-04/V-05): present after every block including BLOCK 5 terminal (`Review lifecycle complete`)
- **CONSENSUS ELEVATION RULE** (V-05): fully enumerated 3-level tiebreaker — ELEVATED tier → BASELINE tier, each by Cost then reviewer count — eliminates inference at generation site
