Scorecard written to `simulations/quest/scorecards/corps-build-scorecard-R3-2026-03-16.md`.

---

## Summary

**All 5 essential criteria pass across all variations. All variations reach golden threshold.**

**Rankings:**

| # | Variation | Composite | Aspirational |
|---|-----------|-----------|--------------|
| 1 | V-05 | **100.00** | 8/8 |
| 2 | V-03 | 98.75 | 7/8 |
| 3 | V-04 | 97.50 | 6/8 |
| 4 | V-01 | 96.25 | 5/8 |
| 5 | V-02 | 96.25 | 5/8 |

**The differentiating criteria:**

- **C-13** (headcount table as pre-role build contract): only V-05 passes — every other variation writes IA files before the headcount table
- **C-14** (analytic prose): V-03 and V-05 pass; V-03 passes because it's output-forward and shows the prose by example; V-05 passes because Phase 3 makes it mandatory before any file write
- **C-15** (person-portrait quality): V-02 is PARTIAL — profile mechanism enforces specificity but no explicit generic-phrase prohibition or transplant test at write time
- **C-16** (resistance profile as pre-IA gate): V-01 fails — no PROFILE phase, just inline portrait guidance

**V-05 excellence**: The phase ordering `VALIDATE → CONTRACT → PROFILES → ROLES → CHART` is the key architectural signal. The table constrains the profiles which constrain the files. That ordering is absent in all other variations, including V-04 which has profiles but no pre-role contract phase.

**Two new rubric candidate patterns:**
1. CROSS-REF IA lens-phrase verification (C-17 candidate) — verifying derivation integrity at build-complete, not just at write time
2. Contract verbatim transcription — planning artifact written once and copied unchanged to final document, preventing drift

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CROSS-REF IA lens-phrase verification: build-complete step re-checks each IA lens opens verbatim with resistance profile lens-phrase -- closes C-16 derivation loop as structural invariant of finished build", "Contract verbatim transcription: headcount table and analytic prose written once in pre-role contract phase then transcribed unchanged into org-chart.md preventing drift between build contract and user-visible document"]}
```
e count target before a single file is written.

Signal 2 -- Analytic prose as Phase 3 output transcribed verbatim to org-chart.md
V-05 Phase 3 requires three mandatory sentences; Phase 6 transcribes them verbatim.

Signal 3 -- CROSS-REF C4: IA lens-phrase verbatim trace at build-complete
Fourth CROSS-REF check verifies every IA lens opens with Phase 4 lens-phrase verbatim.

Signal 4 -- Portrait self-check as 4-criterion inline gate
V-05: 4 checks. V-04: 3 checks. V-01: 1 check (transplant test only).

## Machine Block

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CROSS-REF IA lens-phrase verification: build-complete step re-checks each IA lens opens verbatim with resistance profile lens-phrase -- closes C-16 derivation loop as structural invariant of finished build", "Contract verbatim transcription: headcount table and analytic prose written once in pre-role contract phase then transcribed unchanged into org-chart.md preventing drift between build contract and user-visible document"]}
```
