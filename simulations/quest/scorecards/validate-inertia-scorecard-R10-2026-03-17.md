Now I have everything needed to score. Let me analyze each variation systematically.

---

## validate-inertia — Round 10 Scoring

### Variation Baselines

All five variations are V-45 derivatives. V-45 scores 340/340 on R10 — C-32/C-33/C-34 were extracted from its excellence signals. The R10 experiment tests structural implementation choices for these three criteria, not gaps. C-01 through C-31 are structurally preserved in all variations.

---

### V-46 — Duality in Audit Header Only

**Axis:** C-33 placement only.

**Structural change:** Preamble intro loses the "Architecture declares what is produced; the audit confirms what was produced" sentence. Duality framing moves to the Citation Chain Completeness Audit header:
> "These are structurally distinct roles: the preamble declares; the audit verifies. Neither artifact substitutes for the other's function."

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-31 | All PASS | V-45 structure preserved |
| C-32 | PASS | AMEND(d) retains V-45 bidirectional lock: "this must match the Evidence you wrote in the L3 row of the Citation Chain Completeness Audit verbatim" |
| C-33 | PASS | Audit-header placement is an explicitly listed valid site: "either in the preamble's introduction, **the audit's header**, or a dedicated framing statement." V-46 names both roles in the audit header. |
| C-34 | PASS | Row 5 audit format subsection preserved from V-45; declares 5-column structure including Evidence with actual-text requirement before Phase 1 |

**Score: 340/340**

**Key finding:** C-33 does NOT require preamble-intro placement. Audit-header satisfies. The tiebreak predicted 330/340 PARTIAL — the rubric text forecloses that outcome by explicitly naming audit-header as valid. This is the experiment's structural answer.

---

### V-47 — Audit Format Inlined in Row 5

**Axis:** C-34 delivery only.

**Structural change:** Separate "Row 5 audit format" subsection removed. Full column spec embedded in Row 5 Requirement cell:
> "5-column table: Source artifact | Consumer site | Evidence (write actual downstream cite text verbatim, not a summary) | Link type (Reference-chain or Description-chain) | Verdict (PASS or CHAIN INTEGRITY FAILURE); CHAIN COMPLETE gate required before CCV"

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-31 | All PASS | V-45 structure preserved |
| C-32 | PASS | AMEND(d) bidirectional lock identical to V-45 |
| C-33 | PASS | Preamble intro retains duality framing: "Architecture declares what is produced; the audit confirms what was produced" |
| C-34 | PASS | Row 5 cell declares all 5 column names AND specifies Evidence must contain actual cite text ("verbatim, not a summary"). Pass condition: column names + Evidence-must-be-actual-text. Both present inline. No pointer-skip risk — format is atomic with declaration. |

**Score: 340/340**

**Key finding:** Inline Row 5 column spec satisfies C-34 fully. The Evidence-column semantic instruction ("verbatim, not a summary") fits in the cell and meets the PARTIAL-guard condition. V-47 eliminates the two-step pointer read (Row 5 → subsection) at no scoring cost.

---

### V-48 — Audit-First Citation Flow

**Axis:** C-32 enforcement direction only.

**Structural change:** AMEND(d) restructured to derive the lever anchor FROM the L3 Evidence column rather than from CCV step (5) with retroactive Evidence match:
> "Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of that row contains the lever anchor text you pre-committed to when you wrote the audit. Copy it exactly, character-for-character... do not reconstruct from Phase 5(3) or CCV step (5)."

Row 3 of the preamble table also signals the direction: "AMEND(d) must derive lever anchor from L3 Evidence column of the audit, not construct independently."

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-31 | All PASS | V-45 structure preserved |
| C-32 | PASS | Bidirectional lock present and directionally reversed: the audit IS the authority, not a retroactive check. AMEND(d) references the L3 Evidence column by name as the explicit source. Pass condition met: "reinforce the Evidence column by name, creating a bidirectional lock." |
| C-33 | PASS | Preamble intro duality framing preserved |
| C-34 | PASS | Row 5 audit format subsection preserved from V-45 |

**Score: 340/340**

**Key finding:** Audit-first derivation is a structurally stronger C-32 enforcement than V-45's forward-then-verify pattern. Collapsing Phase 5(3) → CCV → AMEND to L3 Evidence → AMEND eliminates the two-step drift surface. This is a new pattern: the audit as authoritative source, not retroactive validator.

---

### V-49 — AUDIT ARCHITECTURE Merged Block

**Axis:** C-33 + C-34 consolidation.

**Structural changes:** Preamble intro loses duality sentence; Row 5 audit format subsection removed. A named block "AUDIT ARCHITECTURE DECLARED" inserted after the preamble table, before Phase 1, containing:
- Duality framing (C-33): "The preamble declares; the audit confirms. These roles are structurally distinct and neither artifact can substitute for or subsume the other."
- Full 5-column format spec (C-34) with Evidence-column instructions.
- Gate: "Do not proceed to Phase 1 until 'AUDIT ARCHITECTURE DECLARED' is written above."

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-31 | All PASS | V-45 structure preserved |
| C-32 | PASS | AMEND(d) bidirectional lock identical to V-45 |
| C-33 | PASS | "Dedicated framing statement" is the third valid placement in C-33. The AUDIT ARCHITECTURE DECLARED block is a named, required, gated framing statement before Phase 1. Both roles named distinctly. |
| C-34 | PASS | Column structure declared in the AUDIT ARCHITECTURE DECLARED block before Phase 1, including Evidence column with actual-text requirement. The block is in the Citation Architecture preamble section before Phase 1 — C-34's placement condition satisfied. |

**Score: 340/340**

**Key finding:** C-33 and C-34 can be co-resident in a single named artifact. This applies the C-24/C-28 named-artifact pattern to the audit architecture itself — "AUDIT ARCHITECTURE DECLARED" is a citable boundary artifact. Co-residence makes partial-criteria orphaning structurally impossible: both criteria live in the same required output block that cannot be emitted without both.

---

### V-50 — Double-Reinforcement

**Axis:** All three (C-32/C-33/C-34) at two structural positions.

**Structural changes:**
- **C-33:** Preamble intro AND audit header both carry duality framing
- **C-34:** Abbreviated column names inline in Row 5 AND full Evidence-column semantic spec in "Row 5 audit format" subsection
- **C-32:** AMEND(d) references CCV step (5) AND L3 Evidence column, with explicit mismatch-correction gate: "if the CCV step (5) text and the L3 Evidence cell text differ by even one character, return to the audit, correct the L3 Evidence row to match the exact LEVER POINT label, then re-copy here"

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-31 | All PASS | V-45 structure preserved |
| C-32 | PASS | Three-way mismatch gate: LEVER POINT / CCV step (5) / L3 Evidence must all agree. The strongest bidirectional lock in the R10 set. References both CCV and L3 Evidence column by name with explicit conflict-resolution instruction. |
| C-33 | PASS | Two valid placements covered: preamble intro AND audit header. Neither can be missed by attention degradation alone. |
| C-34 | PASS | Two delivery points: abbreviated inline in Row 5 (atomic, no pointer-skip) AND full semantic spec in subsection (Evidence-column depth). Model encounters format at both read-time declaration and execution-time reference. |

**Score: 340/340**

**Key finding:** Double-positioning is the PARTIAL-eliminator pattern. When a criterion appears at two structural positions — one declarative (preamble) and one proximate (execution site) — the model cannot partially satisfy it without encountering it at both. V-50 is the highest structural-compliance ceiling in R10.

---

### Composite Scores

| Variation | C-01–C-31 | C-32 | C-33 | C-34 | Total | All Essential Pass |
|-----------|-----------|------|------|------|-------|--------------------|
| V-46 | 310/310 | 10 | 10 | 10 | **340/340** | Yes |
| V-47 | 310/310 | 10 | 10 | 10 | **340/340** | Yes |
| V-48 | 310/310 | 10 | 10 | 10 | **340/340** | Yes |
| V-49 | 310/310 | 10 | 10 | 10 | **340/340** | Yes |
| V-50 | 310/310 | 10 | 10 | 10 | **340/340** | Yes |

**All five variations: 340/340. R10's three new criteria have multiple structurally valid implementation paths.**

---

### Excellence Signals

**Top-scoring variation:** All five tied at 340/340. V-50 is the defensively strongest — double-reinforcement with a three-way mismatch gate.

**New patterns identified:**

**1. Audit-first derivation direction (V-48)**
V-45 runs forward-then-verify: produce in Phase 5(3) → CCV step (5) → check against L3 Evidence. V-48 reverses: L3 Evidence IS the authoritative source; AMEND derives from the audit, not from production. This collapses two-step drift to one-step copy and makes the audit the source of truth rather than a retroactive check. Pattern: *the citation audit as upstream authority, not downstream verifier.*

**2. Co-resident named-artifact block for paired criteria (V-49)**
Applying the C-24/C-28 named-artifact pattern to the audit architecture itself creates a gated block that embeds two criteria in one required output. "AUDIT ARCHITECTURE DECLARED" cannot be emitted without both C-33 duality framing and C-34 column spec — the block is indivisible. Pattern: *pair structurally coupled criteria inside a single named, gated artifact to prevent partial-criteria orphaning.*

**3. Double-positioning as PARTIAL-path eliminator (V-50)**
One declaration plus one execution-site reinforcement eliminates attention-degradation PARTIALs. The execution-site position is always proximate to the action being governed — C-33 at the audit header fires at the exact moment the model writes the audit. Pattern: *declarative position (preamble) + proximate position (execution site) = no partial satisfaction path remains.*

**4. C-33 placement sensitivity finding (V-46)**
Audit-header placement fully satisfies C-33 — preamble-intro placement is not required. The rubric's "either in the preamble's introduction, the audit's header, or a dedicated framing statement" is a genuine OR. This confirms C-33 is placement-agnostic across all three listed sites. Pattern: *duality framing at the audit's execution site is structurally sufficient; preamble placement is not required for C-33 compliance.*

**5. Inline Row 5 column spec is atomically sufficient for C-34 (V-47)**
Embedding the full column spec (including Evidence-column actual-text requirement) directly in the Row 5 cell eliminates the pointer-skip failure mode (Row 5 → subsection) without losing any pass-condition requirements. The Evidence semantic instruction fits: "write actual downstream cite text verbatim, not a summary." Pattern: *atomic inline declaration in the declaration row beats subsection verbosity for drift-resistance when the semantic requirement can fit in a cell.*

---

```json
{"top_score": 340, "all_essential_pass": true, "new_patterns": ["audit-first derivation: making AMEND(d) derive from the L3 Evidence column rather than CCV collapses two-step drift to one-step copy, making the audit the authoritative upstream source rather than a retroactive verifier", "co-resident named-artifact block for paired criteria: embedding C-33 duality framing and C-34 column spec in a single named gated block (AUDIT ARCHITECTURE DECLARED) prevents partial-criteria orphaning — the block cannot be emitted without both criteria present", "double-positioning as PARTIAL eliminator: one declarative position (preamble) plus one execution-site position (audit header or AMEND) ensures the model encounters each criterion at the moment it governs, eliminating attention-degradation partial satisfaction paths"]}
```
