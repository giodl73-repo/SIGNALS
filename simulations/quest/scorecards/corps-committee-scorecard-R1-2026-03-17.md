---

## corps-committee R1 — Score Summary

**All five variations: 84 / Silver**

All essential criteria PASS except C-01 (PARTIAL). Committee type is declared, but none of the five enforce committee-type-specific Phase 5 framing — arch-board outputs no ADR, ROB outputs no explicit readiness verdict. That partial miss blocks the Gold essential-pass gate.

| Criterion | All Five | Note |
|-----------|----------|------|
| C-01 Committee type | **PARTIAL** | Type declared; arch-board ADR format not enforced |
| C-02 Role voice | PASS | Tier sort + charter-based voice rules |
| C-03 Decisions | PASS | Phase 5 DECISIONS/Verdict chain |
| C-04 Action items | PASS | V-04 PASS+ via table format |
| C-05 Dissent | PASS | V-05 PASS+ via RULE 2 injection default |
| C-06 Structure | PASS | Full skeleton: header → discussion → tally → decisions |
| C-07 Depth | **PARTIAL** | Inertia depth present; type-specific depth not enforced |
| C-08 AMEND | PASS (vacuous) | Not invoked |
| C-09 Pre-mortem | PASS | V-03/V-05 stronger gate ("outside-in perspective required") |
| C-10 Charter fidelity | **FAIL** | Charter loaded but constraints not cited in minutes |

**Ranking:** V-05 > V-03 > V-01 > V-04 > V-02 (all 84)

**One fix closes Gold:** Restore the `COMMITTEE-TYPE REQUIREMENTS` section from the golden baseline prompt into Step 2 fill rules. That closes C-01 and C-07 simultaneously, moving composite from 84 → ~96.

```json
{"top_score": 84, "all_essential_pass": false, "new_patterns": ["injection-as-default flips cognitive burden — model proves YES rather than remembering to inject on NO", "provisional participant annotation in Phase 0 creates forward-reference link to bridge reducing skip errors"]}
```
tain section boundaries |
| C-07 | Discussion depth reflects committee type | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | Inertia investigation provides switching-cost depth; no variation enforces ROB metric readiness, shiproom risk register, or arch-board trade-off comparison — systematic gap (committee-type requirements section was dropped from all variations) |
| C-08 | AMEND capability honored when invoked | PASS | PASS | PASS | PASS | PASS | AMEND not invoked; vacuously satisfied |
| C-09 | Pre-mortem risk the committee would miss | PASS | PASS | PASS+ | PASS | PASS+ | FINDING-D requires non-obvious switching cost in all; V-03 and V-05 raise gate threshold to "outside-in perspective required — if competent internal reviewer would have predicted it, GATE answers NO" |
| C-10 | Charter fidelity traceable | FAIL | FAIL | FAIL | FAIL | FAIL | Charter loaded for tier sort; Phase 5 output does not require citing charter-specific constraints (quorum, veto, escalation); systematic gap across all variations |

---

## Composite Scores

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)`
PARTIAL = 0.5 pass.

| Criterion | Pts/pass | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 Essential | 12 | 6 | 6 | 6 | 6 | 6 |
| C-02 Essential | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 Essential | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 Essential | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 Essential | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 Recommended | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 Recommended | 10 | 5 | 5 | 5 | 5 | 5 |
| C-08 Recommended | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 Aspirational | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 Aspirational | 5 | 0 | 0 | 0 | 0 | 0 |
| **Composite** | | **84** | **84** | **84** | **84** | **84** |

---

## Ranking

| Rank | Variation | Score | Band | Deciding Factor |
|------|-----------|-------|------|-----------------|
| 1 | V-05 | 84 | Silver | RULE 2 injection-as-default closes incorrect-YES failure; provisional Phase 0 annotation creates forward-reference link to bridge; strongest C-05 |
| 2 | V-03 | 84 | Silver | Strongest C-09 gate (outside-in language); INERTIA PRINCIPLE preamble deepens Phase 1 intent; hardcoded INERTIA INVARIANT |
| 3 | V-01 | 84 | Silver | Voice-length contract (3-4 Tier 1 / 2 Tier 3) produces most differentiated role voice; challenger-first ORDERING RULE prominent |
| 4 | V-04 | 84 | Silver | Table format for ACTION ITEMS provides strongest C-04 structural guarantees |
| 5 | V-02 | 84 | Silver | Compact INPUT/OUTPUT/COMMIT contracts efficient but lose some framing guidance for edge cases |

Band: **Silver** — C-01 PARTIAL (type declared, framing not enforced for arch-board) prevents Gold essential-pass gate.

---

## Excellence Signals from V-05

**Signal 1 — Injection as default, not exception**
RULE 2: "Injection is the default when charter roles don't cover it. YES requires evidence." The model must actively prove a qualifying participant exists. The explicit statement "Claiming YES without such a participant is an incorrect affirmation" closes the silent failure mode where the bridge outputs YES without a role that covers switching-cost analysis.

**Signal 2 — Provisional participant annotation in Phase 0**
Adding `[Note: Inertia-Advocate is a candidate participant — confirmed or replaced by bridge in Phase 2]` to the Phase 0 participant list creates a forward-reference link before the bridge runs. The injection/confirmation becomes a continuation rather than a late-arriving intervention, reducing bridge-skip errors.

---

## Gap Requiring Fix Before Gold

**C-01 + C-07 — Committee-type-specific framing dropped**

The golden baseline prompt included an explicit committee-type requirements section:

```
## COMMITTEE-TYPE REQUIREMENTS
ROB: Discussion must reference feature/metric readiness evidence.
  Decisions section must include a verdict on readiness (ready / not ready / conditional).
Shiproom: Discussion must include a risk register or blocking issues.
  Go/no-go decision must be explicit.
Arch-board: Discussion must include named architectural trade-offs (at least two alternatives).
  Decision produces an ADR summary with rejected alternatives and rationale.
```

All five variations dropped this section. Adding it to Step 2 fill rules (or as a Phase 5 conditional block) would close both C-01 and C-07, moving composites from 84 to approximately 96, crossing the Gold threshold.

```json
{"top_score": 84, "all_essential_pass": false, "new_patterns": ["injection-as-default flips cognitive burden — model proves YES rather than remembering to inject on NO", "provisional participant annotation in Phase 0 creates forward-reference link to bridge reducing skip errors"]}
```
