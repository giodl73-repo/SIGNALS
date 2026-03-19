---
name: commitment
description: "Sequence skills into a staged program plan with gates and topic tracking. Generate program.yaml for the topic: stages (n"
allowed-tools: [Read, Write, Edit, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


# BOUNDED BLOCK PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
# Verify before finalizing this Component 1: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                                 | C-42 back-ref                      |
# |---------------|---------------|---------------------------------------------------------------------------------------|------------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable                   | BOUNDED BLOCK PROTOCOL decl. above |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                           | BOUNDED BLOCK PROTOCOL decl. above |

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements          # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header index confirmed present in block above.