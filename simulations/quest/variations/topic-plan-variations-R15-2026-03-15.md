Written. Here's the summary:

---

## R15 — topic-plan Variations (C-48 + C-49)

**Gap source**: Both new criteria were already present in R14 V-05. The exercise isolates the two mechanisms and tests their phrasing variants.

**The pivot point** — R14 gap table:

| R14 variation | C-48 (halt declaration) | C-49 (attestation) |
|---|---|---|
| V-01 | YES (inline: "one STOP result halts Phase 1") | NO |
| V-02 | **NO** (pass-only annotation) | NO |
| V-03 | YES (labeled field: "blocked by any single STOP result") | NO |
| V-04 | YES | NO |
| V-05 | YES | YES — ceiling |

**R15 variation map:**

| Variation | Axis | Gate-0 annotation form | Gate-0 condition form | C-48 | C-49 |
|---|---|---|---|---|---|
| V-01 | Lifecycle | inline halt clause | flat AND-conjunction | YES | NO |
| V-02 | Output format | inline halt clause | grouped + attestation suffix | YES | YES |
| V-03 | Phrasing register | labeled THRESHOLD field | grouped, no attestation | YES | NO |
| V-04 | Combined LC+OF | labeled THRESHOLD field | grouped + attestation suffix | YES | YES |
| V-05 | Full ceiling | inline halt clause | flat AND + attestation suffix | YES | YES |

**Key structural distinction V-04 vs V-05**: V-04 uses the labeled-field form of C-48 (`GATE-0 PASS THRESHOLD: ... blocked by any single STOP result`) with grouped-label C-47. V-05 uses the inline-annotation form of C-48 with flat AND-conjunction C-47. Both should reach the ceiling; the comparison tests whether the two C-48 surface forms are equivalent.
