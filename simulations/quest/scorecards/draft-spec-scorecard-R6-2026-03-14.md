# Round 6 Scorecard — `draft-spec`

**Rubric**: v6 | **Date**: 2026-03-15 | **Variations**: V-01 through V-05

---

## Scoring Key

| Symbol | Meaning | Points |
|--------|---------|--------|
| ✓ | PASS | Full |
| ~ | PARTIAL | Half |
| ✗ | FAIL | 0 |

**Essential**: 12 pts each (5 × 12 = 60)
**Recommended**: 10 pts each (3 × 10 = 30)
**Aspirational**: 5 pts each (16 × 5 = 80)
**Max composite**: 170

---

## Baseline Posture (carried from R5)

Before any R6 axis is applied, the starting spec has:

| Criterion | Status | Rationale |
|-----------|--------|-----------|
| C-01 through C-08 | ✓ | Established structure/behavior/coverage, unchanged |
| C-09 through C-17 | ✓ | All aspirational structural/depth/coverage patterns from prior rounds hold |
| C-18 | ~ | Fallback exists as behavioral instruction; no demarcated verbatim copy |
| C-19 through C-21 | ✓ | Ordinal markers, unified declaration, gate proof-of-work established |
| C-22 | ~ | IG-ID section exists but conflates guards and defeats into single rows — "not instantiated" as parallel namespaces with distinct ID sequences |
| C-23 | ✗ | New in v6; no Responsible Role column on IG guard entries anywhere in baseline |
| C-24 | ✗ | New in v6; no CASCADE TO: annotation on any unified declaration |

**Baseline effective aspir. passes**: 12.0 (C-09–C-17 + C-19–C-21) + 0.5 (C-18) + 0.5 (C-22) + 0 + 0 = **13.0 / 16**

---

## Per-Variation Scoring

### V-01 — IG/ID Register Split (C-22 axis)

Primary change: `[IG-REGISTER]` (IG-XX guards) and `[ID-REGISTER]` (ID-XX defeats) as parallel tables with distinct ID sequences.

| Tier | ID | Criterion (abbreviated) | Status | Evidence |
|------|----|--------------------------|--------|----------|
| E | C-01 | Guided section structure | ✓ | All five sections present and ordered |
| E | C-02 | Scout artifact status table | ✓ | LOADED/NOT FOUND rows in SETUP block |
| E | C-03 | P0 requirement coverage | ✓ | 20/20 coverage count stated |
| E | C-04 | Self-review findings | ✓ | Findings section with named contradictions |
| E | C-05 | Artifact frontmatter complete | ✓ | `{topic}-spec-{date}.md`, all fields |
| R | C-06 | Secondary role validation | ✓ | PM, Compliance invoked with PASS/finding |
| R | C-07 | Contradiction detection | ✓ | Conflicting IDs named and flagged |
| R | C-08 | Actionable amendment list | ✓ | ≥ 2 specific numbered items |
| A | C-09 | No-scout fallback documented | ✓ | Named conditional present |
| A | C-10 | Cross-namespace coherence | ✓ | Decision traced to feasibility artifact |
| A | C-11 | Pre-printed cross-namespace column | ✓ | Column structurally present in Purpose |
| A | C-12 | Role annotations inline | ✓ | Secondary role embedded in Requirements block |
| A | C-13 | Per-row P0 status column | ✓ | Row-level Spec Entry column with named entries |
| A | C-14 | Active inspection guard | ✓ | Named scan source required before absent-confirm |
| A | C-15 | Cross-namespace signal in two locations | ✓ | SETUP table + Purpose row both instantiated |
| A | C-16 | PM-first coverage pre-assignment | ✓ | PM step pre-fills rows before Architect writes |
| A | C-17 | Named progression gate token | ✓ | Gate artifact named; downstream phase declares dependency |
| A | C-18 | Scripted verbatim fallback text | ~ | Fallback conditional present (C-09 ✓) but no demarcated `VERBATIM RESPONSE:` copy |
| A | C-19 | Ordinal location markers | ✓ | Location 1 of 2 / 2 of 2 on multi-instance fields |
| A | C-20 | Unified role-and-source declaration | ✓ | Role + scan source combined in single structural element |
| A | C-21 | Gate token proof-of-work validity rule | ✓ | Token without prerequisite block declared invalid |
| A | C-22 | IG-ID register (proper) | ✓ | Split into `[IG-REGISTER]` (IG-XX) and `[ID-REGISTER]` (ID-XX) — parallel structure, distinct IDs |
| A | C-23 | IG-role binding inline | ✗ | No Responsible Role column on IG entries; role binding not present |
| A | C-24 | Cascade directive on unified decl. | ✗ | No `CASCADE TO:` annotation; propagation still behaviorally implied |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 12 ✓ (C-09–C-17 excl. C-18, + C-19–C-21) + C-18 ~ (2.5) + C-22 ✓ (5) + C-23 ✗ (0) + C-24 ✗ (0) = **67.5**

**Composite: 157.5 / 170**
Golden threshold: ✓ (all essential pass, composite ≥ 85)

---

### V-02 — Scripted Verbatim Fallback (C-18 axis)

Primary change: Two `VERBATIM RESPONSE:` blockquote variants — Branch A (all scout missing) and Branch B (requirements missing, others present).

| Tier | ID | Criterion (abbreviated) | Status | Evidence |
|------|----|--------------------------|--------|----------|
| E | C-01–C-05 | All essential | ✓ | Unchanged from baseline |
| R | C-06–C-08 | All recommended | ✓ | Unchanged from baseline |
| A | C-09 | No-scout fallback documented | ✓ | Two-branch conditional named; C-18 satisfies the more demanding check |
| A | C-10–C-17 | Cross-namespace through gate | ✓ | Unchanged |
| A | C-18 | Scripted verbatim fallback text | ✓ | `VERBATIM RESPONSE:` blockquotes demarcate model-ready copy; Branch B adds partial-context variant — both conditions met |
| A | C-19–C-21 | Ordinal, unified, gate PoW | ✓ | Unchanged |
| A | C-22 | IG-ID register (proper) | ~ | Still conflated; V-02 does not address register structure |
| A | C-23 | IG-role binding inline | ✗ | Not addressed |
| A | C-24 | Cascade directive | ✗ | Not addressed |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 12 ✓ + C-18 ✓ (5) + C-22 ~ (2.5) + C-23 ✗ (0) + C-24 ✗ (0) = **67.5**

**Composite: 157.5 / 170**
Golden threshold: ✓

---

### V-03 — Cascade Directives (C-24 axis)

Primary change: `CASCADE TO: [location A of N] → [location B of N]` annotation on every unified role-and-source declaration (C-20 elements).

| Tier | ID | Criterion (abbreviated) | Status | Evidence |
|------|----|--------------------------|--------|----------|
| E | C-01–C-05 | All essential | ✓ | Unchanged |
| R | C-06–C-08 | All recommended | ✓ | Unchanged |
| A | C-09–C-17 | Aspirational baseline set | ✓ | Unchanged |
| A | C-18 | Scripted verbatim fallback | ~ | Fallback conditional present; still no demarcated verbatim copy |
| A | C-19 | Ordinal location markers | ✓ | CASCADE TO: `[location A of N]` notation reinforces existing ordinal markers; C-19 already PASS, now doubly confirmed |
| A | C-20 | Unified role-and-source | ✓ | CASCADE TO: appended to each unified element without disrupting the role+source combination requirement |
| A | C-21 | Gate token PoW | ✓ | Unchanged |
| A | C-22 | IG-ID register (proper) | ~ | Still conflated; V-03 does not address register structure |
| A | C-23 | IG-role binding inline | ✗ | Not addressed |
| A | C-24 | Cascade directive | ✓ | Every unified declaration carries `CASCADE TO:` with ordinal denominators; C-15 upgrades from convention to structurally declared contract |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 12 ✓ + C-18 ~ (2.5) + C-22 ~ (2.5) + C-23 ✗ (0) + C-24 ✓ (5) = **70.0**

**Composite: 160.0 / 170**
Golden threshold: ✓

---

### V-04 — IG/ID Split + Role Binding (C-22 + C-23 axes)

Primary change: Split registers (C-22) plus `Responsible Role` column on `[IG-REGISTER]` entries and `Confirming Role` on `[ID-REGISTER]` entries, cross-matched (C-23).

| Tier | ID | Criterion (abbreviated) | Status | Evidence |
|------|----|--------------------------|--------|----------|
| E | C-01–C-05 | All essential | ✓ | Unchanged |
| R | C-06–C-08 | All recommended | ✓ | Unchanged |
| A | C-09–C-17 | Aspirational baseline set | ✓ | Unchanged |
| A | C-18 | Scripted verbatim fallback | ~ | Still behavioral instruction only; V-04 does not address fallback copy |
| A | C-19–C-21 | Ordinal, unified, gate PoW | ✓ | Unchanged |
| A | C-22 | IG-ID register (proper) | ✓ | Parallel tables with distinct IG-XX and ID-XX sequences; pair completeness verifiable by counting |
| A | C-23 | IG-role binding inline | ✓ | `Responsible Role` column on each IG-XX row; `Confirming Role` on each ID-XX row; both inline on guard/defeat entry, not deferred to a phase |
| A | C-24 | Cascade directive | ✗ | No `CASCADE TO:` annotation; propagation still implied |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 12 ✓ + C-18 ~ (2.5) + C-22 ✓ (5) + C-23 ✓ (5) + C-24 ✗ (0) = **72.5**

**Composite: 162.5 / 170**
Golden threshold: ✓

---

### V-05 — All Four Axes (C-22 + C-23 + C-24 + C-18)

Primary change: IG/ID split (V-01) + role binding on registers (V-04) + CASCADE TO: annotations (V-03) + VERBATIM RESPONSE: blockquotes with two branches (V-02) — all applied simultaneously.

| Tier | ID | Criterion (abbreviated) | Status | Evidence |
|------|----|--------------------------|--------|----------|
| E | C-01 | Guided section structure | ✓ | All five sections, correct order |
| E | C-02 | Scout artifact status table | ✓ | LOADED/NOT FOUND rows in SETUP |
| E | C-03 | P0 requirement coverage | ✓ | 20/20 with explicit count |
| E | C-04 | Self-review findings | ✓ | Named findings and contradictions |
| E | C-05 | Artifact frontmatter | ✓ | `{topic}-spec-{date}.md`, all fields |
| R | C-06 | Secondary role validation | ✓ | PM and Compliance invoked with PASS |
| R | C-07 | Contradiction detection | ✓ | Conflict IDs named and flagged |
| R | C-08 | Actionable amendments | ✓ | ≥ 2 specific numbered items |
| A | C-09 | No-scout fallback | ✓ | Two-branch named conditional |
| A | C-10 | Cross-namespace coherence | ✓ | Decision traced to feasibility artifact by name |
| A | C-11 | Pre-printed cross-namespace column | ✓ | Column structurally present in Purpose |
| A | C-12 | Role annotations inline | ✓ | Secondary role embedded inline in Requirements block |
| A | C-13 | Per-row P0 status column | ✓ | Named Spec Entry per P0 row |
| A | C-14 | Active inspection guard | ✓ | Named scan source required before absent-confirm |
| A | C-15 | Cross-namespace signal, two locations | ✓ | SETUP table + Purpose row; CASCADE TO: makes design choice structurally declared |
| A | C-16 | PM-first coverage pre-assignment | ✓ | PM pre-fills rows before Architect writes |
| A | C-17 | Named gate token | ✓ | Gate artifact named; downstream phase declares dependency |
| A | C-18 | Scripted verbatim fallback | ✓ | `VERBATIM RESPONSE:` blockquotes; Branch A (all-missing) + Branch B (requirements-missing); model-ready copy for both contexts |
| A | C-19 | Ordinal location markers | ✓ | Location A of N / B of N on all multi-instance fields; CASCADE TO: denominators reinforce |
| A | C-20 | Unified role-and-source declaration | ✓ | Role + scan source in single structural element; CASCADE TO: appended without breaking unification |
| A | C-21 | Gate token PoW validity | ✓ | Token without prerequisite block declared invalid |
| A | C-22 | IG-ID register (proper) | ✓ | `[IG-REGISTER]` (IG-XX guards) and `[ID-REGISTER]` (ID-XX defeats) as parallel tables; pair count verifiable |
| A | C-23 | IG-role binding inline | ✓ | `Responsible Role` on each IG-XX; `Confirming Role` on each ID-XX; inline, not deferred |
| A | C-24 | Cascade directive | ✓ | Every C-20 unified element carries `CASCADE TO: [loc A of N] → [loc B of N]`; propagation contract declared at source |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 16/16 × 80 = **80**

**Composite: 170 / 170**
Golden threshold: ✓ (all essential pass, composite = 170 ≥ 85)

---

## Summary Table

| Variation | Axis Focus | C-18 | C-22 | C-23 | C-24 | Aspir. | Composite | Rank |
|-----------|------------|------|------|------|------|--------|-----------|------|
| V-01 | IG/ID split | ~ | ✓ | ✗ | ✗ | 67.5 | **157.5** | 4= |
| V-02 | Verbatim fallback | ✓ | ~ | ✗ | ✗ | 67.5 | **157.5** | 4= |
| V-03 | Cascade directive | ~ | ~ | ✗ | ✓ | 70.0 | **160.0** | 3 |
| V-04 | IG split + role bind | ~ | ✓ | ✓ | ✗ | 72.5 | **162.5** | 2 |
| V-05 | All four axes | ✓ | ✓ | ✓ | ✓ | 80.0 | **170.0** | 1 |

**Tie-break V-01 vs V-02**: V-01 resolves a structural criterion (C-22 PARTIAL→PASS); V-02 resolves a content criterion (C-18 PARTIAL→PASS). Both gain the same points; V-01 ranks marginally higher on criterion weight (structural criterion affects verifiability of other criteria) but the composite is identical.

---

## Excellence Signals from V-05

**Signal 1 — Register namespace parity via structural split (C-22 ✓)**
Splitting into `[IG-REGISTER]` (IG-XX) and `[ID-REGISTER]` (ID-XX) makes guard-defeat pairing verifiable by counting rows in each table. Conflating them into single rows hid whether a guard had an assigned defeat path; the split makes the gap immediately visible as an empty ID-XX row.

**Signal 2 — Accountability co-located with risk declaration (C-23 ✓)**
`Responsible Role` on each IG-XX entry and `Confirming Role` on each ID-XX entry binds accountability to the risk at declaration time, not at execution time. Deferring role assignment to a behavioral phase allows the spec to appear complete while leaving the accountability relationship unbound until runtime.

**Signal 3 — Propagation structurally declared at the source element (C-24 ✓)**
`CASCADE TO: [location A of N] → [location B of N]` on each unified declaration converts C-15's two-location requirement from a design aspiration (verifiable only by prose search) to a structurally declared contract (verifiable by reading the annotation). The cascade annotation also makes C-19's ordinal denominators load-bearing rather than ornamental.

**Signal 4 — Dual-branch verbatim copy removes composition from scratch (C-18 ✓)**
Two `VERBATIM RESPONSE:` blockquotes — one for all-scout-missing (Branch A) and one for requirements-missing-only (Branch B) — ensure the model emits model-ready text regardless of which absent-context condition fires. A single fallback branch leaves the partial-context case open to improvisation; the dual-branch design closes it.

---

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["IG/ID register split into parallel namespaces with distinct IG-XX guard entries and ID-XX defeat entries makes pair completeness verifiable by counting rows rather than by reading prose", "Responsible Role bound inline on each IG guard entry co-locates risk declaration with accountability at definition time rather than deferring role assignment to a behavioral phase", "CASCADE TO: annotation on every unified role-and-source declaration structurally declares propagation to named ordinal locations at the source element converting C-15 two-location requirement from design aspiration to declared contract", "Dual-branch VERBATIM RESPONSE: blockquotes for all-missing and requirements-missing-only fallback contexts provide model-ready copy for both conditions eliminating composition from scratch in either branch"]}
```
