# Quest Score — org-build R15 (Rubric v11)

## V-01 — Inertia-First Sequence

> **Note**: V-01 text truncates mid-Phase 5 (at the ASCII org hierarchy skeleton). Criteria dependent on Phase 5 content (C-05, C-07, C-09, C-10, C-16, C-22) are scored on what is visible.

---

### Essential Criteria (5)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 5 Task Steps Section 1 explicitly instructs "Box-and-line diagram with min 2 org levels. FORBIDDEN: replacing the ASCII diagram with a flat name list." Skeleton begun. |
| C-02 | **PASS** | Phase 4 Task Step 2 lists all five fields verbatim: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. |
| C-03 | **PASS** | Phase 3 Task Step 3: "MUST include role named `inertia-advocate`." Phase 4 Constraints: "FORBIDDEN: omitting it." |
| C-04 | **PASS** | Phase 3: T1-DEPTH-FLAG = standard → 20–30 roles; T1-DEPTH-FLAG = deep → 50+ roles. Depth-conditional floor present. |
| C-05 | **FAIL** | Phase 5 text truncated after Section 1. Headcount-by-area table with `Decides`/`Escalates` columns not visible. Cannot verify. |

**Essential: 4 / 5**

---

### Recommended Criteria (3)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Phase 3: "Group roles into min 2 named area subdirectories." Phase 4 Constraints: "FORBIDDEN: placing all files flat with no area subdirectory structure." |
| C-07 | **FAIL** | No operating rhythm table or committee charter section visible anywhere in V-01's text. |
| C-08 | **PASS** | Phase 2 produces T2-PRESSURE (closed set) + T2-VERDICT (single, bidirectionally guarded). Phase 5 Input Contract: "T2-PRESSURE — MUST be present for FLAT-CASE-PRESSURE entry." Implies org-chart.md will carry the rated verdict. |

**Recommended: 2 / 3**

---

### Aspirational Criteria (26)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **FAIL** | Phase 5 truncated; Org Evolution Roadmap with typed triggers not visible. |
| C-10 | **FAIL** | Category derivation table (pre-phase) present, but the Anti-Pattern Watch table with `[element name] (cat-N) —` syntax in "Why It Applies Here" cells is in Phase 5 (cut off). |
| C-11 | **PASS** | Phase 4 Task Step 3: "look up T2-PRESSURE in the Verbatim IA Scope Templates table above." IA scope is explicitly derived from FLAT-CASE-PRESSURE rating via pre-written templates. |
| C-12 | **PASS** | Anti-Pattern Category Derivation table maps T2-VERDICT → category selection: CAN-OPERATE-FLAT → cat-2/cat-3; STRUCTURE-WARRANTED → cat-1/cat-4. Structural derivation explicit. |
| C-13 | **PASS** | Phase 2 Constraints: "FORBIDDEN: writing both… Both is an error." Explicit error framing present. |
| C-14 | **PASS** | Phase 1 RECORD → consumed by Phase 2 Input Contract (named variables, MUST bindings). Phase 2 RECORD → consumed by Phases 3, 4, 5. At minimum one named typed output consumed by named input contract. |
| C-15 | **PASS** | Phase 2: "FORBIDDEN: writing both… Both is an error." AND "FORBIDDEN: omitting both… Neither is an error." Both directions covered. |
| C-16 | **FAIL** | Anti-Pattern Watch table (with Mitigation cells) is in Phase 5, which is truncated. Cannot verify. |
| C-17 | **PASS** | Phase 4 Constraints: "MUST copy IA scope verbatim from template table, keyed to T2-PRESSURE. FORBIDDEN: paraphrasing or adapting the IA scope template text." |
| C-18 | **PASS** | Pre-phase derivation table has a "FORBIDDEN Categories" column per verdict row: CAN-OPERATE-FLAT FORBIDDEN cat-1/cat-4; STRUCTURE-WARRANTED FORBIDDEN cat-2/cat-3. |
| C-19 | **PASS** | Scanning all phases: constraint statements use MUST/FORBIDDEN uniformly. No advisory language ("should", "prefer", "consider") found in any constraint context. |
| C-20 | **PASS** | All 4 gate phases (1–4) declare named typed output variables. All consuming phases (2–5) declare explicit Input Contract sections naming upstream variables by name. |
| C-21 | **PASS** | Every named typed gate variable in every Input Contract is bound with MUST or FORBIDDEN (e.g., "T1-DEPTH-FLAG — MUST be present"). No advisory binding anywhere. |
| C-22 | **FAIL** | Phase 5 skeleton begun (`[Senior Org Unit]`) but immediately truncated. Placeholder slot coverage unknown. Cannot verify named slots keyed to gate variables. |
| C-23 | **PASS** | Every phase (1–4 visible) ends with a FORBIDDEN at the phase boundary in Constraints: "FORBIDDEN: beginning Phase N+1 before emitting the Phase N RECORD block." Per-boundary ordering guards present. |
| C-24 | **PASS** | Phases 1–4 each materialize a `=== RECORD: PHASE-N ===` block with named typed fields before the next phase. Phase 5 is terminal (produces org-chart.md artifact, not a gate); no Phase 6 to guard. Pattern complete for all gate phases. |
| C-25 | **PASS** | Every gate phase: outbound FORBIDDEN in PHASE-ORDERING-GUARD field inside RECORD block; inbound FORBIDDEN in consuming phase's Input Contract. Both directions at each boundary. |
| C-26 | **PASS** | Each `=== RECORD: PHASE-N ===` block simultaneously satisfies: gate variable declaration (typed fields), ordering anchor (PHASE-ORDERING-GUARD as first field), materialization checkpoint, and named bindings for downstream Input Contract. Single construct, four properties. |
| C-27 | **FAIL** | Count floor conditional is in **Phase 3** Task Steps and Constraints, not Phase 1. C-27 requires the binding to be inside Phase 1 instruction itself. Phase 1 only sets T1-DEPTH-FLAG without encoding the per-value count floor. |
| C-28 | **PASS** | All four RECORD blocks place `PHASE-ORDERING-GUARD:` as structurally first field, carrying FORBIDDEN naming the next phase. Not in preamble or surrounding prose. |
| C-29 | **PASS** | All prohibitions use `FORBIDDEN: [action]` throughout. No "do not", "never", "avoid" patterns found in constraint contexts. |
| C-30 | **PASS** | Every phase uses `### Task Steps` and `### Constraints` as separate structural headings. Task-step prose and MUST/FORBIDDEN declarations are always in distinct labeled sections. |
| C-31 | **FAIL** | Phases 1, 2, 4 use closed enumerations (`[standard \| deep]`, `[COMPLETE \| PARTIAL]`, etc.). Phase 3 RECORD uses `T3-ROLE-COUNT: [integer]` and `T3-AREA-COUNT: [integer ≥ 2]` — open-ended type annotations, not closed valid-value sets. Fails C-31 pass condition. |
| C-32 | **PASS** | All consuming phases (2–5) have structurally distinct `### Input Contract` and `### Constraints` headings. Gate-consumption and gate-production audits are independently readable. |
| C-33 | **PASS** | Each Input Contract names every upstream variable consumed, identifies its source phase, and carries MUST/FORBIDDEN per variable. A reader scanning only Input Contract sections can reconstruct the full gate-consumption chain. No upstream variable is left implicit in Task Steps. |
| C-34 | **PASS** | Pre-phase Anti-Pattern Category Derivation table has three columns: T2-VERDICT | Required Categories | FORBIDDEN Categories — with both verdict rows fully populated on both columns. Side-by-side structure present. |

**Aspirational: 20 / 26** (Fails: C-09, C-10, C-16, C-22, C-27, C-31)

---

### Composite Score

```
composite = (4/5 × 60) + (2/3 × 30) + (20/26 × 10)
          = 48.0 + 20.0 + 7.7
          = 75.7
```

---

### Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 — Inertia-First Sequence | **75.7** | No (C-05) |

---

### Excellence Signals from V-01

**Signal 1 — Inertia-first phase sequencing**
Phase 2 (Inertia Assessment) runs before Phase 3 (Role Enumeration). This forces the structural verdict to be locked before any role is counted or characterized — making role count, IA scope template selection, and anti-pattern category selection all verdict-coherent by construction. No criterion currently requires or rewards this ordering.

**Signal 2 — Pre-phase global constant tables**
Verbatim IA Scope Templates and the Anti-Pattern Category Derivation table are declared before Phase 1 as named lookup references. Phase instructions reference them by name rather than embedding definitions inline. The prompt has a "constants" section distinct from phase instructions — phases consume by reference, not by re-statement. No criterion requires this structural positioning.

---

```json
{"top_score": 75.7, "all_essential_pass": false, "new_patterns": ["Inertia-first phase sequencing: structural verdict locked in Phase 2 before role enumeration in Phase 3, forcing verdict-coherent downstream choices throughout", "Pre-phase global constant tables: IA scope templates and category derivation tables placed before Phase 1 as named lookup references consumed by phase instructions rather than embedded inline"]}
```
