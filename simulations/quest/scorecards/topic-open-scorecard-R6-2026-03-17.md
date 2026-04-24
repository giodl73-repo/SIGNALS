Now I have all five variations. Let me score each against the v6 rubric.

---

## Scoring: topic-open Round 6

### Scoring Formula
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 19 * 10)
```

---

## V-01 — Exit Gate and Checklist Tool Citation

**Essential (C-01–C-05):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | ROW TEMPLATE present; skill instructs appending to `simulations/TOPICS.md` |
| C-02 | PASS | Phase 4 writes `simulations/{topic}/strategy.md` explicitly |
| C-03 | PASS | F-01 through F-05 defined in FIELD SCHEMA; all five enforced in exit gate |
| C-04 | PASS | VOCABULARY LOCK locks `essential`/`recommended`/`optional` before any phase |
| C-05 | PASS | COV-01 exit gate condition requires >= 1 `essential` row |

**Recommended (C-06–C-08):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | COV-02 exit gate condition requires >= 2 distinct namespaces |
| C-07 | PASS | Phase 2 instructs >= 2 sentence rationale with two named requirements |
| C-08 | PASS | COV-03 exit gate condition requires >= 2 distinct owner roles |

**Aspirational (C-09–C-27):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Phase 3 defines isolated `## COMMIT GATE` section with exact item name placeholder |
| C-10 | PASS | F-04 shows `{topic}-{signal}-{date}.md` pattern; exit gate enforces it |
| C-11 | PASS | VOCABULARY LOCK block precedes all phase instructions |
| C-12 | PASS | Phase 5 is a full checkbox list with one item per essential criterion |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: If C-04 fails: list each row with drift." Named C-04 explicitly |
| C-14 | PASS | "Wrong vocabulary = silent breakage. This is the most common mistake." + `topic-status` exact string comparison explanation |
| C-15 | PASS | Phase 2 instructs rationale first, then signal table |
| C-16 | PASS | ROW TEMPLATE is field-complete: `{topic-slug} | {description} | {YYYY-MM-DD}` |
| C-17 | PASS | Phase 2 Decision table: "Owner roles emerge from decision context rather than post-hoc count enforcement" |
| C-18 | PASS | "COPY — DO NOT RECONSTRUCT" + names the date-field bypass failure mode |
| C-19 | PASS | FIELD SCHEMA and CONSTRAINT SURFACE both name tools; path constraint cites `topic-status` and `topic-scanner` |
| C-20 | PASS | Phase 2 Decision table shows both Compliant and Non-compliant paths with consequences |
| C-21 | PASS | Phase 1 Setup: "because `topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation with no merge path" |
| C-22 | PASS | VOCABULARY LOCK: "If you read this block first… / If you skip this block…" |
| C-23 | FAIL | Only Phase 2 Decision table present; Phases 1, 3, 4, 5 have no labeled decision tables |
| C-24 | PASS | CONSTRAINT SURFACE: Rule / Rationale / What Breaks / Tool — unified 4-column table covers all constraints |
| C-25 | PASS | Phase 2 Exit Gate: every item names tool + what-it-checks. Phase 5: every checklist item carries tool citation with failure consequence |
| C-26 | FAIL | ROW TEMPLATE says "COPY — DO NOT RECONSTRUCT" — no explicit if/if. Phase 5 timing has no if/if in instruction body. Not universal |
| C-27 | FAIL | Only Phase 2 has labeled decision table; all five required for C-27 |

**Aspirational pass: 16/19**

**V-01 Composite: 60 + 30 + 16/19 × 10 = 60 + 30 + 8.4 = 98.4**

---

## V-02 — Universal Comparative Framing

**Essential:** All 5 PASS (same structural elements support correct output)
**Recommended:** All 3 PASS

**Aspirational (C-09–C-27):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-22 | PASS | All carry over — vocabulary block, template, schema, constraint table, Phase 2 decision table, if/if in vocab block |
| C-23 | FAIL | Only Phase 2 Decision table present |
| C-24 | PASS | CONSTRAINT SURFACE: 4-column unified table |
| C-25 | FAIL | Phase 2 exit gate: items 1, 4, 5 (Rationale, COV-02, COV-03) have no tool citation. Phase 5 checklist: zero tool citations on any item |
| C-26 | PASS | VOCABULARY LOCK if/if; ROW TEMPLATE has "If you copy…/If you reconstruct…" inline if/if; Phase 2 prose has if/if; Phase 4 has if/if for both writes; Phase 5 has if/if for timing. All named ordering instructions covered |
| C-27 | FAIL | Only Phase 2 decision table; all five required |

**Aspirational pass: 16/19**

**V-02 Composite: 60 + 30 + 16/19 × 10 = 98.4**

---

## V-03 — Labeled Decision Tables at All Five Phases

**Essential:** All 5 PASS
**Recommended:** All 3 PASS

**Aspirational (C-09–C-27):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-22 | PASS | All carry over |
| C-23 | PASS | Five labeled decision tables: Phase 1 (Collision Check), Phase 2 (Content Order), Phase 3 (Gate Structure), Phase 4 (Output Write), Phase 5 (Check Timing) — consistent Path/Action/Consequence columns |
| C-24 | PASS | CONSTRAINT SURFACE 4-column table |
| C-25 | FAIL | Phase 2 exit gate items: bare checklist with no tool citations. Phase 5 checklist: no tool citations on any item |
| C-26 | FAIL | ROW TEMPLATE: "COPY — DO NOT RECONSTRUCT" with no if/if. Phase 2 instruction body: "Write narrative rationale first (see Phase 2 Decision above)" — references table, no inline if/if. Phase 5 instruction body: "Run after both files are written (see Phase 5 Decision above)" — no inline if/if. Ordering instructions delegate to tables rather than using if/if directly |
| C-27 | PASS | All five phase transitions have labeled decision tables — complete coverage |

**Aspirational pass: 17/19**

**V-03 Composite: 60 + 30 + 17/19 × 10 = 60 + 30 + 8.95 = 98.95**

---

## V-04 — C-25 + C-26 Combination

**Essential:** All 5 PASS
**Recommended:** All 3 PASS

**Aspirational (C-09–C-27):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-22 | PASS | All carry over |
| C-23 | FAIL | Only Phase 2 Decision table ("Phase 2 Decision: Content Order"). Phases 1, 3, 4, 5 have no labeled decision tables |
| C-24 | PASS | CONSTRAINT SURFACE 4-column table |
| C-25 | PASS | Phase 2 exit gate: all 6 items cite tool + what-it-checks (Rationale→`topic-status`, priority→`topic-status`, COV-01→`topic-status`, COV-02→`topic-scanner`, COV-03→`topic-status`, item names→`topic-scanner`). Phase 5: all 5 items cite tool with failure consequence |
| C-26 | PASS | VOCABULARY LOCK if/if; ROW TEMPLATE if/if with tool names; Phase 2 prose if/if; Phase 3 instruction body if/if ("If isolated as `## COMMIT GATE`…/ If embedded inside the signal table…"); Phase 4 Write 1 if/if; Phase 4 Write 2 if/if; Phase 5 timing if/if. Universal coverage |
| C-27 | FAIL | Only Phase 2 decision table; all five required for C-27 |

**Aspirational pass: 17/19**

**V-04 Composite: 60 + 30 + 17/19 × 10 = 98.95**

---

## V-05 — Full Integration (C-25 + C-26 + C-27)

**Essential:** All 5 PASS
**Recommended:** All 3 PASS

**Aspirational (C-09–C-27):**
| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Phase 3 isolated `## COMMIT GATE` with essential signal list |
| C-10 | PASS | F-04: `{topic}-{signal}-{date}.md` pattern throughout |
| C-11 | PASS | VOCABULARY LOCK precedes all phases |
| C-12 | PASS | Phase 5 full checkbox list |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: If C-04 fails" — names C-04 |
| C-14 | PASS | "Wrong vocabulary = silent downstream breakage. This is the most common mistake." + full `topic-status` consequence |
| C-15 | PASS | Phase 2 instructs rationale before signal table |
| C-16 | PASS | ROW TEMPLATE field-complete |
| C-17 | PASS | Phase 2 Decision table explains causal reason: owner roles emerge from rationale stakeholders |
| C-18 | PASS | "COPY — DO NOT RECONSTRUCT" + names date-field bypass failure mode |
| C-19 | PASS | FIELD SCHEMA and DEFAULTS TABLE both name tools per constraint |
| C-20 | PASS | Phase 2 Decision table contrasts both paths |
| C-21 | PASS | Phase 1 Setup: "`topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation with no merge path" |
| C-22 | PASS | VOCABULARY LOCK: "If you read this block first… / If you skip this block…" with `topic-status` named in both branches |
| C-23 | PASS | Five labeled decision tables at Phases 1–5 (Collision Check, Content Order, Gate Structure, Output Write, Check Timing) |
| C-24 | PASS | DEFAULTS TABLE: 5-column (Default / Rule / Why / What Breaks If You Skip / Tool) — covers all five major constraints in one block. Superset of C-19 and C-20 requirements simultaneously |
| C-25 | PASS | Phase 2 exit gate: all 6 items cite tool + mechanism. Phase 5: all 5 checklist items cite tool + failure consequence. No enforcement point without a named tool |
| C-26 | PASS | All ordering instructions use if/if: VOCABULARY LOCK, ROW TEMPLATE, Phase 2 prose, Phase 3 instruction body ("If isolated…/If embedded…"), Phase 4 Write 1, Phase 4 Write 2, Phase 5 timing — universal coverage |
| C-27 | PASS | All five phases preceded by labeled decision tables — each phase entry is a structural decision point |

**Aspirational pass: 19/19**

**V-05 Composite: 60 + 30 + 19/19 × 10 = 60 + 30 + 10 = 100**

---

## Rankings

| Rank | Variation | Composite | Aspirational | Fails |
|------|-----------|-----------|--------------|-------|
| 1 | V-05 | **100** | 19/19 | none |
| 2 (tie) | V-03 | 98.95 | 17/19 | C-25, C-26 |
| 2 (tie) | V-04 | 98.95 | 17/19 | C-23, C-27 |
| 4 (tie) | V-01 | 98.4 | 16/19 | C-23, C-26, C-27 |
| 4 (tie) | V-02 | 98.4 | 16/19 | C-23, C-25, C-27 |

---

## Excellence Signals from V-05

**Pattern 1 — Dual-channel phase framing**: V-05 places both a labeled decision table AND inline if/if prose in the instruction body at every phase. The model receives the same decision framed twice through two independent structural formats — the table provides a scannable reference before the phase begins; the if/if prose inside the instruction body reinforces it at execution time. V-03 and V-04 use one channel or the other but not both simultaneously for every phase.

**Pattern 2 — Defaults-override registry as constraint table**: V-05 replaces the 4-column CONSTRAINT SURFACE with a 5-column DEFAULTS TABLE that adds a "Default" column naming the starting cognitive state being overridden (e.g., "Any priority vocabulary", "Free-form TOPICS.md row", "Table before rationale"). This converts the constraint table from a rule list into a defaults-override registry — each row explicitly names what the model would do without intervention, making the replacement visible rather than assumed. This framing pattern could generalize to any skill that overrides common generation defaults.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-channel phase framing: every phase carries both a labeled decision table (structural) and inline if/if prose in the instruction body (executable), so the model receives the same decision framed twice through independent formats — the table as a pre-phase reference, the prose as an at-execution reinforcement", "Defaults-override registry: a 5-column constraint table with a 'Default' column naming the starting cognitive state being overridden converts the table from a rule list into a defaults-override registry, making each override explicit by naming what the model would generate without intervention"]}
```
