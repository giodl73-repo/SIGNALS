## topic-plan Rubric Evaluation — Round 1

> **Note:** Only V-01 and V-02 are present in the variate set. V-03 through V-05 content is absent from the input — scoring covers the two available variations.

---

### V-01 — Single Axis: Table-heavy, structured diff format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Reads strategy.md | **PASS** | Step 1 explicitly reads `simulations/{topic}/strategy.md` and extracts namespaces, planned skills, rationale, acknowledged gaps |
| C-02 | Reads signal artifacts | **PASS** | Step 2 globs `simulations/{topic}/**/*-{date}.md`, reads each artifact, notes namespace/skill/finding |
| C-03 | Identifies delta | **PASS** | Step 3 asks "What did the signals reveal that the strategy did not anticipate?" with explicit anti-inventory warning: "A plain inventory of signals is not the delta" |
| C-04 | Proposes typed changes | **PASS** | Step 4 table enforces `ADD / REMOVE / REPRIORITIZE` columns; "Untyped observations do not belong in this table" |
| C-05 | Confirmation gate | **PASS** | Step 8: "Do not modify strategy.md yet" + explicit "Reply 'apply' to confirm, or tell me what to adjust" prompt |
| C-06 | Cites signal evidence | **PASS** | Table includes `Signal Evidence` column; each row requires artifact name |
| C-07 | Before/after summary | **PASS** | Step 5 provides explicit diff-style `BEFORE / AFTER` block with inline evidence brackets per changed namespace |
| C-08 | All three change types | **PASS** | "If a category has no changes, include one row with 'No changes' under that type — do not omit the category" |
| C-09 | Namespace gap detection | **PASS** | Step 6 reviews all 9 namespaces explicitly, requires ADD-or-DEFER verdict per absent namespace |
| C-10 | Conflicting signals | **PASS** | Step 7 dedicated "Conflict Detection" section; requires naming the conflict and stating how the revised strategy handles it |

**Essential:** 5/5 PASS → 60 pts
**Recommended:** 3/3 PASS → 30 pts
**Aspirational:** 2/2 PASS → 10 pts
**V-01 Composite: 100/100** ✓ Golden threshold met

---

### V-02 — Single Axis: Lifecycle Emphasis / Hard Stop Gates

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Reads strategy.md | **PASS** | Phase 1a reads `simulations/{topic}/strategy.md` with extraction detail |
| C-02 | Reads signal artifacts | **PASS** | Phase 1b finds all artifacts, builds inventory; hard STOP gate after both reads |
| C-03 | Identifies delta | **PASS** | Phase 2 is entirely devoted to the gap question; "This is not an inventory. Do not list the signals. Answer the gap question." — strong framing |
| C-04 | Proposes typed changes | **PASS** | Phase 3 defines ADD/REMOVE/REPRIORITIZE with per-item structure; explicit "none" conclusion required per type |
| C-05 | Confirmation gate | **FAIL** | Phase 5 says "Present to the user. Do not write files." — this is an instruction to the model, not a user-facing gate. No explicit confirmation prompt or "apply" verb presented to the user. Rubric: "omits the confirmation gate fails." (Phase 5 also appears truncated) |
| C-06 | Cites signal evidence | **PASS** | Phase 3 requires "Cite the signal artifact(s) that motivated it" per proposal |
| C-07 | Before/after summary | **FAIL** | No before/after diff block in any phase; content may be truncated but no structural slot for it is visible |
| C-08 | All three change types | **PASS** | Phase 3: "If your delta findings produced no ADDs/REMOVEs/REPRIORITIZEs, say so explicitly" — explicit coverage mandate |
| C-09 | Namespace gap detection | **PASS** | Phase 4: "GAP AUDIT" covering all 9 namespaces with ADD-or-DEFER verdict required per row |
| C-10 | Conflicting signals | **FAIL** | No conflict detection section in visible content; may be in truncated portion but cannot be credited |

**Essential:** 4/5 PASS → 48 pts (C-05 failure caps score below passing regardless of downstream)
**Recommended:** 2/3 → 20 pts
**Aspirational:** 1/2 → 5 pts
**V-02 Composite: 73/100** ✗ Not golden (essential cap; 4/5 essential pass)

---

### Rankings

| Rank | Variation | Composite | All Essential | Golden |
|------|-----------|-----------|---------------|--------|
| 1 | V-01 (Table-heavy diff) | **100** | Yes | **Yes** |
| 2 | V-02 (Lifecycle phases) | 73 | No | No |
| — | V-03 through V-05 | N/A | N/A | absent |

---

### Excellence Signals — V-01 Patterns

1. **Typed confirmation verb in the gate**: "Reply 'apply' to confirm" removes ambiguity about what triggers the write. Vague gates ("let me know when ready") allow the model to rationalize early application.

2. **Mandatory "No changes" rows**: Requiring an explicit no-change row per type forces the model to address all three axes before outputting. Omitting a category is a common coverage failure mode.

3. **Inline evidence brackets in the BEFORE/AFTER diff block**: `[+stakeholders: signal S3 showed missing exec alignment]` attaches the rationale at the point of change, not in a separate section. Reduces confirmation friction — user sees the "why" without cross-referencing.

4. **Anti-inventory warning at the delta step**: Naming the failure mode ("A plain inventory of signals is not the delta") makes the criterion self-enforcing. The model reads the criterion and the anti-pattern simultaneously.

5. **9-namespace gap audit as a named, bounded step**: Listing all 9 namespaces by name in the prompt makes omission structurally visible. An unbounded "check for gaps" instruction is easy to skip; an enumerated list is not.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["typed confirmation verb ('apply') in gate removes ambiguity and prevents rationalized early writes", "mandatory 'No changes' rows per change type prevent category omission as a coverage failure mode", "inline evidence brackets in BEFORE/AFTER diff attach rationale at the point of change rather than in a separate section", "anti-inventory warning embedded at the delta step makes the failure mode self-enforcing", "enumerating all 9 namespaces by name in the gap audit step makes omission structurally visible"]}
```
