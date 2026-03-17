---

## Simplification Report — campaign-brief / QU5

### What was removed and why

**PREAMBLE — 4 excisions (~194 words)**

| Removed | Why |
|---|---|
| Final sentence of preamble opening: "When execution notes...they invoke it." | Meta-commentary about how execution notes work. The notes function without this description. |
| TOKEN-PRESSURE GUARD paragraph (entire, ~78w) | "This rule does not suspend when `found` is non-empty. It fires unconditionally at any token budget." Both sentences restate "apply unconditionally before any STORY synthesis begins" already stated in the rule header. The positional/declarative mechanism explanation is architecture documentation, not a behavioral constraint. |
| Basis sentence (~33w): "uniform absence is itself evidence…neither permits disclaimer substitution." | Rationale prose. The sparse-coverage behavior is already governed by the STORY block rule ("synthesize on available signals"). |
| COMPRESSED-COLLAPSE GUARD tail (~83w): "Blocking entries may be compressed; found timestamps may not" + positional mechanism sentence + execution-note cross-reference sentence | "Blocking entries may be compressed..." directly restates the rule above it. The positional/declarative mechanism sentences explain the architecture; the rule is already operative from the GUARD's first sentence. |

**STATUS execution note — 3 excisions (~91w)**

| Removed | Why |
|---|---|
| "When the companion execution note is present...must both execute." | Describes the normal (non-elision) case. The preamble already mandates both rules unconditionally. This sentence adds no behavioral constraint beyond what the preamble + each note's own operative content already guarantees. |
| "This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE." | Self-referential label. The note is identifiable from its header; stating "this invokes" adds no behavioral force. |
| "The declarative mechanism for C-30: this note names the COMPRESSED-collapse failure mode — simultaneous compression...compensating if preamble processing occurred without full rule absorption." | Explains why the note names the failure mode. The naming itself is operative; this sentence explains the naming. Architecture documentation, not a constraint. |

**STORY execution note — 3 excisions (~98w)**

| Removed | Why |
|---|---|
| "When the companion execution note is present...must both execute." | Same reason as STATUS: redundant with preamble unconditional mandate. |
| "This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named pointer — the declarative mechanism for C-29...compensating if preamble processing occurred without full rule absorption." | Architecture documentation explaining why the note fires. The operative firing is already in the "If `found` is empty" clause. |
| "Gap pattern is the evidence set." | Isolated standalone sentence whose meaning is fully subsumed by the three required questions and the STORY block rules. |

**VERDICT execution note — 2 excisions (~52w)**

| Removed | Why |
|---|---|
| "The action sub-label is not optional format — it is the field that makes VERDICT self-contained and enables the team to derive their commit posture from this block alone without re-reading STORY or item-level gap entries." | Rationale for a rule already stated as "required regardless of COMPRESSED format state and regardless of token pressure." The rule is the constraint; this is its justification. |
| "If COMPRESSED was active for blocking entries, it does not extend to VERDICT fields." | Redundant with "VERDICT is never abbreviated," which is a stronger statement that subsumes this. |

---

### Criteria verification

| Criterion | Passes in simplified? | Mechanism preserved |
|---|---|---|
| C-29 zero-signal synthesis | YES | PREAMBLE rule (2 clauses) + STORY Q1 inline directive + "If `found` is empty" clause in execution note |
| C-30 timestamp isolation | YES | PREAMBLE rule + inline template comments + execution note operative content |
| C-38 parity constraint | YES | "must be executed as if...at full depth, at parity with what would be produced if the companion's execution note were present in this context" — in both execution notes |
| C-39 structural deliverables enumeration | YES | "For this companion (ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution means: Q1/Q2/Q3..." and "For this companion (TIMESTAMP ISOLATION), full-depth execution means: each entry...`current_date:`...regardless..." — both retained |
| C-40 non-degradation (depth symmetry) | YES | "This parity constraint is symmetric: executing this companion mandate does not reduce the present clause's own output depth. Both mandates execute at full depth simultaneously." — retained in both execution notes |
| VERDICT action sub-label | YES | "VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is required regardless of COMPRESSED format state and regardless of token pressure" — retained |
| COMPRESSED/FULL format switching | YES | Density contract + block template + BLOCKING-DETAIL block — all retained |

**All essential criteria: YES**

---

```json
{"simplified_word_count": 1494, "original_word_count": 1931, "all_essential_still_pass": true}
```
