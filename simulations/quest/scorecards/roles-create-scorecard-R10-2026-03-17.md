## roles-create Scorecard R10

### Composite Scores

| Rank | Variation | Fails | Score |
|------|-----------|-------|-------|
| 1 | **V-05** Canonical | — | **100** |
| 2 (tied) | V-01 Mixed gates | C-24 | **99.47** |
| 2 (tied) | V-02 Expanded bodies | C-25 | **99.47** |
| 2 (tied) | V-03 CONTRACT swap | C-26 | **99.47** |
| 5 | V-04 C-25+C-26 | C-25, C-26 | **98.95** |

### Per-Variation Analysis

**V-01 (C-24 fail):** Phase 0 uses a gate TABLE; Phases 1–4 use inline annotations. C-24 fires on the single inconsistency — structural idiom commitment is all-or-nothing. C-15 passes (gate table is still in-phase, not consolidated); C-16 passes (the `[ID]` column in the Phase 0 table preserves bidirectionality).

**V-02 (C-25 fail):** Connector openers and fix-and-retry prose added to phase bodies. All gates remain inline (C-24 passes). C-25 fails because phase bodies exceed minimum surface even without restating CONTRACT rules — bridging prose that contextualizes phases is a distinct failure mode not captured by the no-restatement rule.

**V-03 (C-26 fail):** COLUMN-HEADER placed before FIELD-REGISTER in the CONTRACTS block. FIELD-REGISTER is first cited in Phase 3, COLUMN-HEADER in Phase 4; the swap puts a Phase-4-cited contract before a Phase-3-cited contract. C-26 applies to adjacent unconditional main-flow pairs — the displacement doesn't need to be dramatic to trigger the rule.

**V-04 (C-25 + C-26 fail):** Combined V-02 prose + V-03 swap. Deduction is exactly 2× the single-criterion penalty (98.95 = 100 − 1.05). C-25 and C-26 are orthogonal — phase surface area and CONTRACT ordering are independent axes.

**V-05 (no fails):** All 19 criteria pass. Single gate idiom throughout, minimum phase bodies (citation + artifact only), CONTRACTS block in first-citation sequence with unconditional main-flow pair (FIELD-REGISTER → COLUMN-HEADER) in Phase 3 < Phase 4 order.

### Excellence Signals from V-05

1. **Single gate idiom commitment:** One structural form (inline `-> Gate N [ID]: PASS / FAIL`) across all content-producing phases — no mixing, no exceptions within gate phases.
2. **Phase body as pointer:** CONTRACT name + artifact name only; any contextual or retry prose belongs in the CONTRACT block or not at all.
3. **CONTRACTS block as execution table of contents:** Unconditional main-flow contracts in first-citation order; conditional and meta contracts trail without violating the rule.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
ged from V-05. |
| C-08–C-14 | PASS | Archetype calibration, orientation registers, domain column headers, inertia companion, interactive hold, self-cert phase, malformed routing — all unchanged. |
| C-15 | PASS | Gate table in Phase 0 is still an in-phase distributed gate; criteria not batched at Phase 5. C-15 governs distribution, not structural form. |
| C-16 | PASS | AUDIT-CHECKLIST CONTRACT pre-declares all obligations with forward Gate IDs. The Phase 0 table provides the backward [ID] reference for item [G], preserving bidirectionality. |
| **C-24** | **FAIL** | Phase 0 uses a gate TABLE; Phases 1–4 use inline annotations. Mixed structural forms across content-producing phases. A single out-of-idiom gate is sufficient to trigger C-24. |
| C-25 | PASS | Phase bodies unchanged from V-05 — minimum surface (CONTRACT citation + artifact reference, no bridging prose). |
| C-26 | PASS | CONTRACTS block ordering unchanged from V-05 — canonical first-citation sequence. |

**Fails:** C-24
**Score:** 18/19 → **99.47**

---

## V-02 — Expanded Phase Bodies

**Axis:** Connector openers ("This phase transitions from...") and fix-and-retry prose ("If the gate fails, apply [fix] and re-run") added to phase bodies. No CONTRACT rule restatement (C-19-analog safe). Gate forms unchanged from V-05 (all inline). CONTRACTS block unchanged.

**Targeted failure:** C-25

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01–C-07 | PASS | All essential and recommended criteria unaffected by prose additions in phase bodies. |
| C-08–C-14 | PASS | Aspirational structural and behavioral criteria through C-14 unaffected. |
| C-15 | PASS | Gates remain inline at each phase; in-phase distribution pattern unchanged. |
| C-16 | PASS | AUDIT-CHECKLIST pre-declaration structure unchanged. |
| C-24 | PASS | All gates inline — structural form is homogeneous across all content-producing phases. |
| **C-25** | **FAIL** | Phase bodies contain connector openers and fix-and-retry workflow prose beyond the CONTRACT citation + artifact reference. Minimum surface violated. C-25 is stricter than the no-restatement rule: prose that contextualizes the phase without restating CONTRACT rules still fails C-25. |
| C-26 | PASS | CONTRACTS block ordering unchanged. |

**Fails:** C-25
**Score:** 18/19 → **99.47**

---

## V-03 — Adjacent CONTRACTS Swap

**Axis:** COLUMN-HEADER placed immediately before FIELD-REGISTER in the CONTRACTS block (Phase-4-cited contract appearing before Phase-3-cited contract). Phase bodies unchanged from V-05. Gate forms unchanged (all inline).

**Targeted failure:** C-26

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01–C-07 | PASS | All essential and recommended criteria unaffected by CONTRACTS block reordering. |
| C-08–C-14 | PASS | Execution phases, frontmatter, mode detection, archetype, orientation registers, body table, companion generation, interactive hold, self-cert, malformed routing — all unchanged. |
| C-15 | PASS | In-phase gate distribution unchanged. |
| C-16 | PASS | AUDIT-CHECKLIST pre-declaration structure unchanged. |
| C-24 | PASS | Gate forms unchanged — all inline, homogeneous. |
| C-25 | PASS | Phase bodies unchanged — minimum surface preserved. |
| **C-26** | **FAIL** | CONTRACTS block shows COLUMN-HEADER before FIELD-REGISTER. FIELD-REGISTER is first cited in Phase 3; COLUMN-HEADER is first cited in Phase 4. C-26 requires Phase 3 citation (FIELD-REGISTER) to appear before Phase 4 citation (COLUMN-HEADER) in the CONTRACTS block. Swapping an adjacent unconditional main-flow pair is a clear citation-sequence violation. |

**Fails:** C-26
**Score:** 18/19 → **99.47**

---

## V-04 — Combination: Expanded Bodies + CONTRACT Swap

**Axis:** V-02 connector/fix-and-retry prose combined with V-03 FIELD-REGISTER/COLUMN-HEADER swap. Gate forms unchanged (all inline).

**Targeted failures:** C-25 + C-26

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01–C-07 | PASS | Essential and recommended criteria unaffected. |
| C-08–C-14 | PASS | Aspirational criteria through C-14 unaffected. |
| C-15 | PASS | In-phase gate distribution unchanged. |
| C-16 | PASS | Pre-declaration structure unchanged. |
| C-24 | PASS | All gates inline — form is homogeneous. |
| **C-25** | **FAIL** | Connector openers and fix-and-retry prose in phase bodies exceed minimum surface. Same failure as V-02. |
| **C-26** | **FAIL** | COLUMN-HEADER before FIELD-REGISTER in CONTRACTS block violates Phase 3 < Phase 4 citation order. Same failure as V-03. |

**Independence check:** C-25 governs phase surface area; C-26 governs CONTRACTS block ordering. The two failure axes are structurally orthogonal — prose content in phase bodies has no relationship to the sequence of CONTRACT definitions. Both fail independently with no cascade. Combined deduction: 2 × (1/190 × 100) = 1.05 pts.

**Fails:** C-25, C-26
**Score:** 17/19 → **98.95**

---

## V-05 — Full Ceiling (Canonical Form)

**Axis:** R9 V-05 reproduced. All 19 criteria pass.

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | File written to `.roles/{area}/{subrole}.md` — correct path, correct location. |
| C-02 | PASS | All frontmatter fields present: name, version, archetype, orientation.frame, orientation.serves, lens.verify (list, ≥4), lens.simplify (list), expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, workflow. |
| C-03 | PASS | Phase 1 correctly routes name-only (`area:subrole`) → extract and proceed; description (quoted) → derive and proceed; empty / confirmed EMPTY → INTERACTIVE-HOLD sequence. |
| C-04 | PASS | Frontmatter content derived from named domain — no generic placeholder text. |
| C-05 | PASS | Inertia-advocate absence triggers suggestion or companion generation. |
| C-06 | PASS | Lens.verify items are boolean, cite specific artifact or state, ≥4 items. |
| C-07 | PASS | Body contains at least one structured domain specializations table. |
| C-08 | PASS | Archetype checked against existing roles in the target area before assignment. |
| C-09 | PASS | orientation.frame is first-person observational; orientation.serves names a specific beneficiary in third-person receiver register. |
| C-10 | PASS | Table column headers use domain vocabulary (not generic Entity/Purpose/Notes). |
| C-11 | PASS | Complete companion inertia-advocate file (valid frontmatter + body) generated when no existing file found. |
| C-12 | PASS | Interactive mode holds through all three sequential questions before any generation begins. |
| C-13 | PASS | Phase 5 self-certification audit runs against the pre-declared AUDIT-CHECKLIST; file written only after passing audit. |
| C-14 | PASS | Phase 0 classifies BARE AREA, EXTRA COLONS, VAGUE PHRASE, and EMPTY inputs deterministically before mode detection. |
| C-15 | PASS | Gates distributed across Phases 0, 1, 2 (Gate 2a), 3 (Gates 3a–3d), and 4 (Gate 4b) — not batched at Phase 5. Phase 5 serves as confirmation, not sole checkpoint. |
| C-16 | PASS | AUDIT-CHECKLIST CONTRACT pre-declares all 8 obligations (A–H) with forward gate pointers and item IDs before Phase 0 executes. Phase 5 executes against the declared list. |
| C-24 | PASS | All content-producing phases use inline `-> Gate N [ID]: ... PASS / FAIL` — single structural form, no mixing with gate tables. Phase 5 is exempt (confirmation checklist, not a gate phase). |
| C-25 | PASS | Each phase body contains exactly one CONTRACT name citation + one artifact reference. No bridging prose, no transition openers, no fix-and-retry workflow text. |
| C-26 | PASS | CONTRACTS block: INPUT-ROUTING-RULES (Ph.0) → INTERACTIVE-HOLD (Ph.1) → FIELD-REGISTER (Ph.3) → COLUMN-HEADER (Ph.4) → INERTIA-ADVOCATE-TEMPLATE (Ph.2, conditional) → AUDIT-CHECKLIST (meta-declaration). Main-flow unconditional pair FIELD-REGISTER/COLUMN-HEADER appears in Ph.3 < Ph.4 citation order. Conditional (INERTIA-ADVOCATE-TEMPLATE) and meta (AUDIT-CHECKLIST) contracts trail without violating the rule. |

**Fails:** None
**Score:** 19/19 → **100**

---

## Composite Scores

| Rank | Variation | Fails | Criteria Failed | Score |
|------|-----------|-------|-----------------|-------|
| 1 | V-05 Canonical | 0 | — | **100** |
| 2 (tied) | V-01 Mixed gates | 1 | C-24 | **99.47** |
| 2 (tied) | V-02 Expanded bodies | 1 | C-25 | **99.47** |
| 2 (tied) | V-03 CONTRACT swap | 1 | C-26 | **99.47** |
| 5 | V-04 C-25+C-26 | 2 | C-25, C-26 | **98.95** |

All essential criteria (C-01–C-05) pass in all 5 variations. All recommended criteria (C-06–C-07) pass in all 5 variations. Discrimination is entirely within the three new aspirational criteria (C-24, C-25, C-26).

---

## Excellence Signals from V-05

### Signal 1: Single gate idiom across all content-producing phases (C-24 confirmed)

V-05 commits to one structural form — inline `-> Gate N [ID]: PASS / FAIL` — across every content-producing phase. The Phase 5 confirmation checklist is structurally distinct (not a gate phase) and exempt, making the commitment clean and unambiguous. V-01 shows that even a single phase defecting to a table form signals an unresolved structural decision; C-24 fires on the first inconsistency, not on a majority. The implication: once a gate idiom is chosen, the skill must maintain it throughout. Format-neutral criteria (C-15 governs distribution, C-16 governs bidirectionality) do not protect against C-24.

### Signal 2: Phase body as a pointer, not a narrative (C-25 confirmed)

V-05 reduces each phase body to its minimum viable form: CONTRACT name + artifact name. The CONTRACT block already contains the rules; the phase body need only say which contract governs and what artifact results. Any prose that transitions between phases, frames context, or describes retry behavior is redundant given the CONTRACT structure — and V-02 confirms that such prose fails C-25 even when it adds no rule restatement. The discipline: if information belongs in a phase, it belongs in a CONTRACT. If it's not in a CONTRACT, it shouldn't be in the phase either.

### Signal 3: CONTRACTS block as execution table of contents (C-26 confirmed)

V-05's CONTRACTS block reads top-to-bottom as the skill's execution order: Phase 0 → Phase 1 → Phase 3 → Phase 4 → (conditional Phase 2) → (meta). The unconditional main-flow pair FIELD-REGISTER/COLUMN-HEADER appears in Phase 3 < Phase 4 citation order. Conditional contracts (INERTIA-ADVOCATE-TEMPLATE) and meta declarations (AUDIT-CHECKLIST) trail without violating the rule, establishing a natural "unconditional first, conditional trailing" pattern. V-03 confirms that swapping adjacent unconditional contracts — even just FIELD-REGISTER and COLUMN-HEADER — is a C-26 violation regardless of how minor the displacement appears.

---

## R10 Findings

1. **C-24 fires on the minimum possible violation:** One table amid all-inline phases is sufficient. Structural idiom commitment is all-or-nothing.

2. **C-25 and C-19 (no-restatement) are independent:** V-02 passes the no-restatement rule and still fails C-25. Bridging prose that adds context without restating rules is the C-25 failure mode, not covered by any prior criterion.

3. **C-26 applies to adjacent unconditional pairs:** V-03 confirms the rule extends to FIELD-REGISTER/COLUMN-HEADER, not just to the dramatic displacement tested in R9 V-03. Any out-of-citation-order placement among unconditional main-flow contracts is a violation.

4. **C-25 + C-26 are orthogonal:** V-04 shows exactly 2× the single-criterion deduction (98.95 = 100 − 2 × 0.526). No cascade between phase surface area and CONTRACT ordering.

5. **V-05 is the sole R10 form passing all 19 criteria.** The canonical form from R9 carries forward without regression.
