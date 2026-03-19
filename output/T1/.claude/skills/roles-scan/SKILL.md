---
name: roles-scan
description: "Walk a repo and produce a draft org.yaml -- the org configuration contract. Pivot modes: directory, concept, service, do"
allowed-tools: [Read, Glob, Grep]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


SCHEMA DECLARATION: TABLE B — Scan Evidence Table  (preamble declaration #3)
  Columns (all required):
    Area                  (C-01: traceable to scan evidence, not invented)
    Source Type           (C-02: one of 7 types declared in COVERAGE ATTESTATION schema)
    Inertia Match         (C-19/C-25: constrained to INR-01..INR-06; before File Path Evidence)
    File Path Evidence    (C-09/C-16/C-21: specific path)
    Anti-Fabrication Note (C-11: required hedging sentence per row)
  Minimum rows: 5  (C-16: path floor gate-blocking)

SCHEMA DECLARATION: TABLE C — Cross-Cutting Concerns  (preamble declaration #4)
  Columns (all required): Concern Name | Boundary Note | Evidence Path
  Minimum rows: 1

SCHEMA DECLARATION: TABLE D — Team Boundary Candidates  (preamble declaration #5)
  Columns (all required): Boundary Candidate | Seam Rationale | Evidence Citation
  Minimum rows: 1

SCHEMA DECLARATION: TABLE E — Headcount Signals  (preamble declaration #6)
  Columns (all required): Signal Source | Headcount Range | Rationale
  Minimum rows: 1

SCHEMA DECLARATION: TABLE F — Transport Manifest  (preamble declaration #7)
  (C-64/C-67/C-70: per-edge Analytical Purpose required;
   absent purpose = C-67 omission + C-70 gate failure — TABLE F FAIL STRING)
  Columns (all required):
    Producing Role      (this role / group)
    Consuming Role      (downstream consumer)
    Tables Consumed     (specific table names)
    Analytical Purpose  (C-67: what consuming role does; C-70: gate-blocking)
  Minimum rows: 2

SCHEMA DECLARATION: COVERAGE ATTESTATION  (preamble declaration #8)
  (C-65/C-68: first-class schema entry; C-72: source types and status values
   declared here — GROUP A references these, does not restate them)
  Columns (all required): Source Type | Status | Notes
  Source types (7 — declared here; GROUP A references, does not restate):
    1. CLAUDE.md files                    5. test coverage areas
    2. package.json / workspace configs   6. SPECS.md files
    3. design/ directories                7. existing .craft/roles/ files
    4. namespace / module directories
  Status values: scanned / not-found / not-applicable
  Minimum rows: 7  (C-68: gate-blocking)

SCHEMA DECLARATION: TABLE G — Evidence Gaps and Ambiguities  (preamble declaration #9)
  Columns (all required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

SCHEMA DECLARATION: TABLE H — Org Shape Delta  (preamble declaration #10)
  (C-66/C-69: BRIDGE RULE declared here; C-72: dimension list declared here)
  Columns (all required):
    Dimension         (org shape dimension)
    Current State     (C-10: what repo evidence shows today)
    Recommended State (C-10: analysis recommendation)
    Driving Evidence  (C-66/C-69: must contain "(cite TABLE B row)" annotation)
  Org shape dimensions (declared here; GROUP B references, does not restate):
    — Team alignment model
    — Cross-cutting concern ownership
    — Headcount distribution model
    — Boundary definition clarity
  Minimum rows: N  (SYNTHESIZER pre-production assertion before TABLE H)

  BRIDGE RULE (C-69 named constraint — declared here; GROUP B references by name):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any row lacking this citation is a BRIDGE RULE violation."