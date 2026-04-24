# Quest Score — corps-scan R1

## Rubric: v1 · 10 criteria · 100 pts

---

## V-01 — Lifecycle Emphasis

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 YAML present | essential | **PASS** | Phase 2 explicitly produces "a single org.yaml code fence" with full structure template |
| C-02 Repo-grounded | essential | **PASS** | Phase 1 inventory precedes YAML; YAML template requires "team name based on signals"; inventory enables reviewer verification |
| C-03 Group hierarchy | essential | **PASS** | "groups: must contain at least one named group with teams beneath it" — hard requirement in Phase 2 |
| C-04 Roles per team | essential | **PASS** | "Each team must have a roles: list with at least one substantive role name"; Inertia Advocate explicitly excluded |
| C-05 No .roles writes | essential | **PASS** | DRAFT NOTICE line 1 + "Do NOT write .roles/ file content anywhere in this output" in Phase 2 — double boundary |
| C-06 Pivot mode + rationale | recommended | **PASS** | Phase 1 requires mode declaration + "one sentence explaining why this mode fits the signals found above" |
| C-07 Exec-office placeholder | recommended | **PASS** | YAML template includes `exec-office: name:` field as required section |
| C-08 Amend options | recommended | **PASS** | Phase 3 lists 3 named AMEND options with command syntax, drawn from documented AMEND set |
| C-09 Pre-YAML scan inventory | aspirational | **PASS** | Phase 1 requires inventory "before writing any YAML" with bullet format; `--- [SCAN COMPLETE] ---` gate enforces order |
| C-10 Draft boundary front-loaded | aspirational | **PASS** | "DRAFT NOTICE: This output is a draft org.yaml for human review and confirmation." is line 1 |

**Score: 100 / 100**

---

## V-02 — Output Format (Typed Table)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 YAML present | essential | **PASS** | Step 3 produces single `yaml` code fence with full template; "DO NOT begin STEP 2 until the table is written" gates entry |
| C-02 Repo-grounded | essential | **PASS** | Typed table with `Source Path` column; rationale must "cite at least one specific Signal from the table above"; "team name based on inventory signals" |
| C-03 Group hierarchy | essential | **PASS** | "groups: must have at least one named group containing teams beneath it" — explicit in Step 3 |
| C-04 Roles per team | essential | **PASS** | "substantive role name" required; Inertia Advocate excluded |
| C-05 No .roles writes | essential | **PASS** | DRAFT NOTICE line 1 + "Do NOT write .roles/ file content anywhere in this output" in Step 3 |
| C-06 Pivot mode + rationale | recommended | **PASS** | Step 2 requires mode name + "rationale citing at least one specific Signal from the table above" — rationale is table-anchored, stronger evidence chain than V-01 |
| C-07 Exec-office placeholder | recommended | **PASS** | YAML template includes `exec-office: name:` field |
| C-08 Amend options | recommended | **PASS** | Step 4 requires 2+ options in `AMEND A — [name]: [action]` format drawn from documented set |
| C-09 Pre-YAML scan inventory | aspirational | **PASS** | 4-column typed table before YAML; hard gate "DO NOT begin STEP 2 until the table is written" |
| C-10 Draft boundary front-loaded | aspirational | **PASS** | "DRAFT NOTICE: This is a draft org.yaml for human review and confirmation." is line 1 |

**Score: 100 / 100**

*Marginal quality advantage over V-01 on C-02 and C-06: typed columns make grounding column-verifiable; rationale must cite a specific table row rather than a free-form sentence.*

---

## V-03 — Phrasing Register (Conversational)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 YAML present | essential | **PASS** | Conversational direction still steers toward YAML production; no evidence it would omit the code fence |
| C-02 Repo-grounded | essential | **PARTIAL** | Inventory required as "bulleted list with path" but no enforcement that YAML team names derive from it; grounding implied, not required |
| C-03 Group hierarchy | essential | **PARTIAL** | No explicit group hierarchy requirement in visible body; conversational register lacks "must contain at least one named group" enforcement |
| C-04 Roles per team | essential | **PARTIAL** | Role requirements conversationally framed if present; no "at least one substantive role name" hard constraint in visible body |
| C-05 No .roles writes | essential | **PARTIAL** | "Nothing gets built from this output" communicates intent but lacks explicit "Do NOT write .roles/" prohibition — weaker boundary |
| C-06 Pivot mode + rationale | recommended | **PASS** | "pick a pivot mode… Write one sentence explaining why you chose it, naming at least one signal" — explicit despite register |
| C-07 Exec-office placeholder | recommended | **FAIL** | No exec-office mention in visible body; no YAML template anchors the requirement; conversational register with no structural template makes omission likely |
| C-08 Amend options | recommended | **PARTIAL** | Axis description says "presented as suggestions"; no minimum count or required format stated — suggestions may be too vague to satisfy C-08 pass condition |
| C-09 Pre-YAML scan inventory | aspirational | **PASS** | "List what you find as a readable inventory — a bulleted list of signal names with the path where you found each one" — explicit |
| C-10 Draft boundary front-loaded | aspirational | **PASS** | "Start with a single sentence telling the reviewer that what follows is a draft" — explicit front-load instruction |

**Score: 65 / 100** *(10+5+5+5+5+10+0+5+10+10)*

*Root cause: conversational register removes structural enforcement at the YAML-content level. C-03, C-04, C-05 all partial because no imperative requirement enforces them. C-07 fails because no YAML template anchors the exec-office section.*

---

## V-04 — Lifecycle + Conversational

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 YAML present | essential | **PASS** | Phase gate forces YAML production; structure survives register change |
| C-02 Repo-grounded | essential | **PASS** | Phase 1 inventory gate structurally precedes Phase 2 regardless of phrasing |
| C-03 Group hierarchy | essential | **PARTIAL** | Phase gate present but conversational phrasing of Phase 2 YAML requirements softens "must contain at least one named group" to guidance — enforcement weakened |
| C-04 Roles per team | essential | **PARTIAL** | Same pattern: phase gate preserves the step, conversational language reduces hard constraint on "at least one substantive role" |
| C-05 No .roles writes | essential | **PASS** | DRAFT NOTICE + phase gate structure preserves boundary under conversational register |
| C-06 Pivot mode + rationale | recommended | **PASS** | Phase 1 gate enforces pivot mode + rationale; structural sequence survives register |
| C-07 Exec-office placeholder | recommended | **PASS** | Phase 2 YAML template (from V-01) includes exec-office; template content preserved even if phrasing is conversational |
| C-08 Amend options | recommended | **PASS** | Phase 3 gate enforces amend options presence; conversational phrasing affects tone not existence |
| C-09 Pre-YAML scan inventory | aspirational | **PASS** | Phase 1 gate mechanically enforces pre-YAML inventory |
| C-10 Draft boundary front-loaded | aspirational | **PASS** | Draft notice as first line preserved from V-01 base |

**Score: 90 / 100** *(10+10+5+5+10+10+10+10+10+10)*

*Phase gates rescue most criteria. C-03 and C-04 are the failure surface: conversational phrasing of YAML content requirements leaves group hierarchy and role enforcement below threshold.*

---

## V-05 — Full Integration (Lifecycle + Typed Table + Imperative)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 YAML present | essential | **PASS** | Phase gate + explicit YAML template + imperative register — strongest guarantee |
| C-02 Repo-grounded | essential | **PASS** | Phase 1 typed table + phase gate + imperative rationale citing specific table row; best grounding chain of all five |
| C-03 Group hierarchy | essential | **PASS** | Phase gate + imperative "groups: must contain" requirement — both structural mechanisms active simultaneously |
| C-04 Roles per team | essential | **PASS** | Phase gate + imperative role requirements + explicit Inertia Advocate exclusion — double enforcement |
| C-05 No .roles writes | essential | **PASS** | DRAFT NOTICE + phase gate + explicit DO NOT prohibition — triple boundary |
| C-06 Pivot mode + rationale | recommended | **PASS** | Phase 1 gate + typed table `Pivot Relevance` column + imperative rationale citing specific row; most auditable rationale chain |
| C-07 Exec-office placeholder | recommended | **PASS** | Phase 2 YAML template + exec-office as required section |
| C-08 Amend options | recommended | **PASS** | Phase 3 gate + imperative `AMEND A — [name]: [action]` format |
| C-09 Pre-YAML scan inventory | aspirational | **PASS** | Phase 1 gate + 4-column typed table + "DO NOT begin next step until table written" — triple gate |
| C-10 Draft boundary front-loaded | aspirational | **PASS** | DRAFT NOTICE as line 1 + imperative language throughout |

**Score: 100 / 100**

*V-05 inherits every positive enforcement mechanism from both V-01 and V-02. No criterion is structurally at risk.*

---

## Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score |
|-----------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 Lifecycle | P | P | P | P | P | P | P | P | P | P | **100** |
| V-02 Typed Table | P | P | P | P | P | P | P | P | P | P | **100** |
| V-03 Conversational | P | ½ | ½ | ½ | ½ | P | F | ½ | P | P | **65** |
| V-04 Life+Conv | P | P | ½ | ½ | P | P | P | P | P | P | **90** |
| V-05 Full Integration | P | P | P | P | P | P | P | P | P | P | **100** |

**Ranking: V-01 = V-02 = V-05 (100) > V-04 (90) > V-03 (65)**

---

## Excellence Signals

Three patterns explain the score ceiling in V-01, V-02, V-05:

1. **Phase-closure separators as mechanical gates** — `--- [SCAN COMPLETE] ---` / `--- [DRAFT COMPLETE] ---` terminators prevent phase content bleed and enforce criterion order. C-09 and C-10 become structurally unavoidable because Phase 1 cannot close until inventory exists and Phase 0 (opening) sets the draft boundary before anything else runs.

2. **Typed inventory table with `Pivot Relevance` column** — transforms pre-YAML scan from a "list what you find" instruction into a structured audit trail. The `Pivot Relevance` column forces per-signal assessment that directly feeds the C-06 rationale citation requirement. Makes C-02 grounding column-verifiable rather than prose-dependent: a reviewer can confirm grounding by scanning a single column.

3. **Layered boundary enforcement on C-05** — opening DRAFT NOTICE + in-YAML "Do NOT write .roles/ file content" creates double (or triple in V-05) enforcement. Neither layer alone is as robust; together they make the boundary nearly failure-proof regardless of how far into the output a model drifts.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-closure separators enforce criterion sequencing by making phase skipping structurally impossible", "typed inventory table with Pivot Relevance column makes C-02 grounding column-verifiable rather than prose-dependent", "layered C-05 boundary via opening DRAFT NOTICE plus in-YAML DO-NOT prohibition"]}
```
