---

## campaign-simulate -- Round 2 Variations

**Axes chosen:** V-01 and V-02 and V-03 are single-axis; V-04 and V-05 are combinations.

---

### V-01 -- Filtering Evidence Axis
**Targets:** C-13 (discriminating rejection)
**Mechanism:** Mandatory `CANDIDATE OBSERVATIONS` table before the findings table. Every sub-skill lists raw observations including weak ones. Filter rules are enumerated. At least one observation must be explicitly rejected with a named rule — a filter that rejects nothing is flagged as non-functional.
**Hypothesis:** C-13 passes by construction. Also strengthens C-05 because evaluating candidates against anchoring rules makes those rules active rather than passive. Hardest remaining: C-11 (only sub-skill sections get empty-state treatment, not all sections).

---

### V-02 -- Elevation Narrative Axis
**Targets:** C-12 (compounding elevation documentation)
**Mechanism:** Compounding patterns section requires a full elevation record with four required fields: `Isolated scope`, `Elevated scope`, `Elevation rationale` ("Promoted from X to Y because..."). This is a schema field on the compounding record, not a prose annotation. Explicit failure condition stated for shallow entries.
**Hypothesis:** C-12 passes by construction. Also improves C-09 (forces precision about which F-IDs share a root cause) and C-10 (elevation narrative is the strongest form of blast radius rationale). Hardest remaining: C-11, C-13.

---

### V-03 -- Universal Empty-State Protocol Axis
**Targets:** C-11 (empty-state discipline across all sections)
**Mechanism:** Six empty-state templates defined upfront — one per section type: sub-skill with no findings, filter log with all passes, findings table empty, ranked tier empty, cross-skill patterns empty, execution log row with zero candidates. Using omission is not permitted. The cross-skill patterns template is notably stronger than prior rounds: requires naming the related-looking findings that were compared before determining independence.
**Hypothesis:** C-11 passes by construction. Also strengthens C-01 and C-09. The cross-skill patterns template's "candidate compounds reviewed" requirement means even a genuine negative requires active comparison work. Hardest remaining: C-12, C-13.

---

### V-04 -- Combined (Filtering Evidence + Universal Empty-State)
**Targets:** C-13 + C-11 simultaneously
**Mechanism:** Filter log from V-01 + all six empty-state templates from V-03. Two orthogonal silent-failure modes closed simultaneously. The filter log template ("Filter applied. All N candidates passed. Note: revisit if true") even handles the edge case where the filter is vacuous.
**Hypothesis:** The combination closes all silent-path failures in the report. C-01, C-07, C-11, C-13 all benefit. Hardest remaining: C-12 (no elevation narrative).

---

### V-05 -- Combined (Elevation Narrative + Tightened Finding Schema)
**Targets:** C-12 + C-06 (standalone Impact) + C-08 (finding-level Remediation)
**Mechanism:** Finding schema has explicit `FAILURE:` conditions on three fields — Spec location, Impact (must be standalone, merging fails), and Remediation (must be on finding record, closing-summary-only fails). Compounding patterns section has the V-02 elevation record. Phase 3 of each sub-skill is renamed "Extract and Filter" and requires naming at least one rejected observation per sub-skill, targeting C-13.
**Hypothesis:** C-12, C-06, C-08 all pass by construction through schema-level enforcement. C-13 is addressed per-sub-skill in Phase 3. The `FAILURE:` annotations are the strongest form of field enforcement — stronger than "this field is required" alone. Risk: per-sub-skill filter requirement in Phase 3 may produce thin, checkbox-style rejection entries rather than genuine filtering judgment.

---

**Coverage map across Round 2 variations:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 empty-state | -- | -- | structural | structural | -- |
| C-12 elevation | -- | structural | -- | -- | structural |
| C-13 filter | structural | -- | -- | structural | Phase 3 gate |
| C-06 standalone Impact | schema | schema | field | schema | explicit FAILURE |
| C-08 finding-level remediation | required col | schema | field | schema | explicit FAILURE |
