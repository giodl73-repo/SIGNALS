---

# campaign-blueprint R19 — Scoring Report

## Rubric Version: v19 | Ceiling: 283

---

## Per-Variant Scoring

### V-01 — Five-Sentinel Control

**Axis:** Lifecycle isolation. R18 V-02 reproduced exactly. All five structural tables carry exactly one in-table RULE sentinel.

| Criterion | Points | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01–C-41 (structural foundation) | 213 | FULL | Inherited from R18 V-02 base — all structural properties confirmed |
| C-42 MAP single-sentinel | 5 | FULL | `RULE` row in INERTIA MODEL MAP (line 171): named-conviction-type absence declared |
| C-43 CONVICTION DELTA single-sentinel | 5 | FULL | `RULE` row in CONVICTION DELTA (line 262): MAP entry binding declared |
| C-44 SCOUT TRACEABILITY TABLE single-sentinel | 5 | FULL | `RULE` row in STT (line 163): named-identifier absence declared |
| C-45 TRACEABILITY AUDIT dual-sentinel | 10 | FULL | Two RULE rows (lines 244–245): named-absence + N+blank STRUCTURAL FAIL — R17 dual form retained |
| C-46 CGD single in-table sentinel | 5 | FULL | One RULE row in CGD (line 287): identifier-to-MAP binding + named-artifact absence declared |
| C-47 complete five-table single-sentinel | 5 | FULL | All five tables carry ≥1 RULE sentinel — complete single-sentinel coverage confirmed |
| **C-48** CGD dual in-table sentinel | **5** | **NO CREDIT** | CGD carries exactly one RULE row. No second sentinel declaring N+blank STRUCTURAL FAIL. C-48 requirement unmet. |
| **C-49** complete five-table dual-sentinel | **5** | **NO CREDIT** | C-49 is strict superset of C-48. C-48 NO CREDIT → C-49 unreachable. |

**Composite Score: 273 / 283**

---

### V-02 — Minimum CGD Dual-Sentinel

**Axis:** Output format — minimum-text second RULE sentinel added to CGD only.

| Criterion | Points | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01–C-47 (all prior criteria) | 273 | FULL | Inherited from R18 V-02 base + five-table single-sentinel architecture intact |
| **C-48** CGD dual in-table sentinel | **5** | **FULL** | Two RULE rows in CGD (lines 481–482): first sentinel = identifier binding + named-absence; second sentinel = "An artifact row with all substantive analysis cells… blank or populated exclusively with structural placeholders (dashes) = STRUCTURAL FAIL — not a present-but-incomplete entry." In-table placement confirmed (positioned before data rows, after first RULE row). Rule content present. |
| **C-49** complete five-table dual-sentinel | **5** | **NO CREDIT** | MAP (line 365): one RULE row. CONVICTION DELTA (line 456): one RULE row. STT (line 357): one RULE row. Three of five tables single-sentinel. C-49 requires all five dual. |

**Composite Score: 278 / 283**

---

### V-03 — Conversational CGD Dual-Sentinel

**Axis:** Phrasing register — second CGD sentinel in conversational (plain-language) register.

| Criterion | Points | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01–C-47 (all prior criteria) | 273 | FULL | Conversational register throughout; structural properties unchanged from V-02 in all five tables |
| **C-48** CGD dual in-table sentinel | **5** | **FULL** | Two RULE rows in CGD (lines 715–716): first sentinel = "Every row here must be one of the three artifacts… If Proposal is missing, say 'Proposal absent'…" (named-absence rule, conversational). Second sentinel = "If you name an artifact in col 1 but leave Sub-section, Register found, Register declared, Scout sub-skill, and Evidence needed all blank or dashed, that row is broken — treat it as a STRUCTURAL FAIL, not a partial answer you can leave incomplete." Register is conversational; structural placement and rule content requirements are met. D18/D19 register invariance confirmed at second-sentinel level. |
| **C-49** complete five-table dual-sentinel | **5** | **NO CREDIT** | STT (line 558): one RULE row. MAP (line 568): one RULE row. CONVICTION DELTA (line 686): one RULE row. Three tables single-sentinel. C-49 NO CREDIT. |

**Composite Score: 278 / 283**

---

### V-04 — Complete Five-Table Dual-Sentinel, Maximum Density

**Axis:** Lifecycle emphasis — all five structural tables dual-sentinel at maximum directive density.

| Criterion | Points | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01–C-47 (all prior criteria) | 273 | FULL | Full structural foundation intact with maximum-density prose surrounding all tables |
| **C-48** CGD dual in-table sentinel | **5** | **FULL** | Two RULE rows in CGD (lines 965–966): first sentinel = named-artifact absence with "Proposal absent means… not a count discrepancy discoverable only by comparing totals"; second sentinel = "A CONVICTION GAP DIAGNOSIS data row with all substantive analysis cells (Sub-section, Register found, Register declared, Scout sub-skill, Evidence needed) blank or populated exclusively with structural placeholders (dashes) = STRUCTURAL FAIL — not a present-but-incomplete entry. Naming the artifact in col 1 while leaving all analysis cells empty does not constitute a valid partial diagnosis." Both rows table-internal, positioned before data rows. |
| **C-49** complete five-table dual-sentinel | **5** | **FULL** | STT (lines 804–805): two RULE rows — named-absence + STRUCTURAL FAIL for blank substantive cells. MAP (lines 817–818): two RULE rows — named-conviction-type absence + STRUCTURAL FAIL for blank analysis cells. TRACEABILITY AUDIT (lines 915–916): two RULE rows — named-absence + N+blank STRUCTURAL FAIL (C-45 form retained). CONVICTION DELTA (lines 934–935): two RULE rows — named-conviction-type absence + STRUCTURAL FAIL for blank analytical cells. CGD (lines 965–966): two RULE rows (C-48 FULL). All five tables dual-sentinel simultaneously. 12-step chain complete. |

**Composite Score: 283 / 283**

---

### V-05 — Complete Five-Table Dual-Sentinel, Compressed

**Axis:** Lifecycle compression — all five structural tables dual-sentinel; surrounding prose stripped to minimum viable form.

| Criterion | Points | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01–C-47 (all prior criteria) | 273 | FULL | Structural properties preserved; compressed prose does not affect table-internal architecture. All five tables carry single-sentinel coverage (C-44/C-43/C-42 compressed but present). C-45 dual TRACEABILITY AUDIT retained in compact form. |
| **C-48** CGD dual in-table sentinel | **5** | **FULL** | Two RULE rows in CGD (lines 1133–1134): first = "Each row here must match a named INERTIA MODEL MAP entry (Spec, Proposal, Pitch). Missing row = [artifact-ID] absent, not a count discrepancy." Second = "A data row with all substantive analysis cells blank or dash-filled = STRUCTURAL FAIL — not a present-but-incomplete entry." Both table-internal, positioned before data rows. Minimum viable text; rule content requirements met. |
| **C-49** complete five-table dual-sentinel | **5** | **FULL** | STT (lines 1030–1031): two RULE rows — named-absence + "A data row with all substantive cells blank or dash-filled = STRUCTURAL FAIL." MAP (lines 1038–1039): two RULE rows — named-conviction-type absence + "A data row with all analysis cells blank or placeholder-filled = STRUCTURAL FAIL." TRACEABILITY AUDIT (lines 1101–1102): two RULE rows — named-absence + "N + blank col 5 = STRUCTURAL FAIL." CONVICTION DELTA (lines 1110–1111): two RULE rows — named-conviction-type absence + "A row with all analytical cells blank or bracket-unfilled = STRUCTURAL FAIL." CGD (lines 1133–1134): two RULE rows (C-48 FULL). All five tables dual-sentinel at minimum viable text density. |

**Composite Score: 283 / 283**

---

## Composite Score Summary

| Variant | C-48 | C-49 | v19 Score | Rank |
|---------|------|------|-----------|------|
| V-04 — Complete Five-Table Dual-Sentinel, Max Density | FULL | FULL | **283** | 1 (tie) |
| V-05 — Complete Five-Table Dual-Sentinel, Compressed | FULL | FULL | **283** | 1 (tie) |
| V-02 — Minimum CGD Dual-Sentinel | FULL | NO | **278** | 3 (tie) |
| V-03 — Conversational CGD Dual-Sentinel | FULL | NO | **278** | 3 (tie) |
| V-01 — Five-Sentinel Control | NO | NO | **273** | 5 |

---

## Diagnostic Tests — Results

| Test | Verdict |
|------|---------|
| V-01 vs V-02: Does C-48 depend specifically on second CGD sentinel? | **CONFIRMED.** V-01 (273) vs V-02 (278) — 5-point gap isolated to presence of second in-table RULE row in CGD only. |
| V-02 vs V-03: Register invariance for second CGD sentinel (D19) | **CONFIRMED.** Both score 278. Formal vs conversational phrasing is non-load-bearing at C-48 level. |
| V-04 vs V-05: Prose density invariance at complete dual-sentinel level | **CONFIRMED.** Both score 283. Adjacent prose volume is non-load-bearing for C-49. D16/D17/D18 invariance stack extends to complete five-table dual-sentinel architecture. |

---

## Excellence Signals from V-04 / V-05

**Pattern 1 — Symmetric dual-sentinel architecture across all five tables.** V-04 and V-05 apply the identical dual-sentinel pattern to all five structural tables simultaneously: each table carries (a) a named-absence rule and (b) an N+blank STRUCTURAL FAIL rule as separate in-table RULE rows. No table operates at lower enforcement density than any other. The structural instrument becomes uniformly self-enforcing at both entry-presence and entry-completeness levels across the full chain.

**Pattern 2 — Upstream SETUP-phase completeness enforcement.** The second RULE sentinel appears in SETUP-phase tables (SCOUT TRACEABILITY TABLE and INERTIA MODEL MAP), not only in REFLECTION-phase tables. This moves completeness-level enforcement upstream: a data row with blank analysis cells is declared a STRUCTURAL FAIL before any artifact is written, not only after REFLECTION audits it. The instrument fails fast rather than silently accepting present-but-hollow entries.

**Pattern 3 — Minimum-text sufficiency of N+blank STRUCTURAL FAIL declarations (V-05 evidence).** V-05 demonstrates that a second RULE sentinel reading "A data row with all analysis cells blank or placeholder-filled = STRUCTURAL FAIL" earns C-48/C-49 FULL at 5 words of rule text. The scoring evaluates structural placement (in-table, before data rows) and rule content presence (the N+blank = STRUCTURAL FAIL equivalence). Neither criterion is sensitive to surrounding prose volume, enabling the dual-sentinel architecture to be deployed in compressed prompts without score loss.

---

```json
{"top_score": 283, "all_essential_pass": true, "new_patterns": ["Symmetric dual-sentinel architecture across all five structural tables — each table carries both a named-absence RULE sentinel and a second N+blank STRUCTURAL FAIL RULE sentinel, achieving uniform enforcement density across the full instrument", "Upstream SETUP-phase completeness enforcement — second RULE sentinel in SCOUT TRACEABILITY TABLE and INERTIA MODEL MAP moves blank-row STRUCTURAL FAIL detection into SETUP before any artifact is written", "Minimum-text sufficiency of N+blank STRUCTURAL FAIL declarations confirmed at 283-point level — five-word compressed rule text earns full C-48/C-49 credit, confirming adjacent prose volume is non-load-bearing for complete dual-sentinel architecture"]}
```
