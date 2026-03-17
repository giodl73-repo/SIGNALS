# Quest Variations — flow-conversation — Round 10 (v9 rubric)

Five complete variations written. Here's the summary:

---

## Variation Axes

**Single-axis (3):**

| # | Axis | Key Innovation |
|---|------|----------------|
| V-01 | Output format — mutation-first authoring | Phase 1-S SESSION_TIMELINE is authored *before* Phase 1. SESSION_STATE in Phase 1 is derived from Phase 1-S replay, not independently populated. Eliminates the subtle inconsistency that Phase 6-E was designed to catch retroactively — makes it structurally impossible. |
| V-02 | Inertia framing | Phase 2 gets a `STATUS_QUO_GAP` column per defect row. Phase 5 gets a `SIMULATION_DELTA` block naming findings invisible to the team's declared status-quo review method. Forces the developer to articulate *why* each finding is a simulation-unique detection. |
| V-03 | Output format — timeline-headline coverage | Phase 5 restructured: TIMELINE_ANOMALY_RATE is reported first as a `COVERAGE_QUALITY_GATE` (CLEAN \| DEGRADED). If DEGRADED, downstream coverage ratios are marked PROVISIONAL. A developer cannot claim good TOPIC_COVERAGE without first clearing the temporal quality gate. |

**Combined (2):**

| # | Axes | Key Innovation |
|---|------|----------------|
| V-04 | Role sequence + mutation-first | Adds a **CONTRACT AUDITOR** role between Topology Architect and Developer. Contract Auditor verifies SESSION_VARIABLE_TIMELINE_CONTRACT completeness and reachability before Developer may begin Phase 1. Adds `AUTHORIZED_REWRITERS` field to Phase 0-A-6 so the Architect can pre-declare legitimate off-topic writes. Developer cites `CONTRACT_AUDIT_CITED: PASS` in Phase 0-D header. |
| V-05 | Inertia framing + phrasing register | Constraint-satisfaction register: Phase 0-D declares named constraints `CONV-NN`, each with `STATUS_QUO_DETECTABILITY: DETECTABLE\|NOT_DETECTABLE`. Phase 1 turns carry inline `CONSTRAINT_VERDICTS`. Phase 2 rows carry `CONV_VIOLATIONS`. Phase 6 Auditor verifies constraint verdict consistency rather than re-evaluating defects from scratch. |

---

## What's New vs. Round 9

Round 9 V-04 pioneered C-25–C-29 (which are now baseline requirements in v9). Round 10 variations all fully incorporate C-25–C-29 as given and then extend:

- **V-01**: Flips the authoring dependency between Phase 1-S and Phase 1 SESSION_STATE — the consistency C-29 checks after the fact becomes structurally impossible to violate
- **V-02/V-05**: Inertia framing makes the artifact self-justifying against teams that claim "we already reviewed this flow"
- **V-03**: Quality gate forces TIMELINE_ANOMALY_RATE to be the headline signal before coverage ratios are interpreted
- **V-04**: Contract Auditor promotes C-25 from documentation to a hard pre-execution gate with `AUTHORIZED_REWRITERS` to handle the common legitimate off-topic write pattern
