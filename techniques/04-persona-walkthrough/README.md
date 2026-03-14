# Persona-Driven Walkthrough Simulation

5 persona advocates walk through specs as their persona, identifying confusion, friction, fear, jargon, and missing context before code is written.

## What It Simulates

Real users — maker, developer, compliance officer, supervisor, operator. Each persona reads specs through their lens and flags design problems technical reviewers miss.

## Scale

5 walkthroughs per feature area. Findings tagged by severity (blocking, major, minor, cosmetic).

## Evidence Files

### Pipeline Stage Definition

| File | Purpose |
|------|---------|
| `C:\src\craftworks\.craft\pipelines\suite\simulate.md` | Simulate stage — 5 personas, walkthrough protocol, gate criteria |

### Sample Walkthrough Outputs

| File | Persona |
|------|---------|
| `C:\src\craftworks\.craft\waves\260314+theseus-the-unifier+suite-cli\simulate-maker.md` | Maker persona |
| `C:\src\craftworks\.craft\waves\260314+theseus-the-unifier+suite-cli\simulate-developer.md` | Developer persona |
| `C:\src\craftworks\.craft\waves\260314+theseus-the-unifier+suite-cli\simulate-compliance.md` | Compliance officer persona |
| `C:\src\craftworks\.craft\waves\260314+theseus-the-unifier+suite-cli\simulate-supervisor.md` | Supervisor persona |
| `C:\src\craftworks\.craft\waves\260314+theseus-the-unifier+suite-cli\simulate-operator.md` | Operator persona |

## Persona Journeys

| Persona | Typical Journey | Key Test |
|---------|----------------|----------|
| **Maker** | `craft new` → `craft test` → `craft build` → `craft deploy` | "Can I do this without reading a manual?" |
| **Developer** | JSON output, exit codes, piping to jq, pre-commit hooks | "Are outputs machine-parseable?" |
| **Compliance** | `guard comply`, audit reports, evidence collection | "Would an auditor accept this?" |
| **Supervisor** | `fleet status` → `fleet approve` → `fleet kill` | "Can I intervene in 30 seconds?" |
| **Operator** | `fleet status`, trace reading, health checks | "Would a Terraform user be confused?" |

## Gate Criteria

- All 5 persona walkthrough reports written and filed
- Spec amendments applied for all blocking and major findings
- No blocking persona findings remain open
- Each persona advocate confirms their amendments address the concern
