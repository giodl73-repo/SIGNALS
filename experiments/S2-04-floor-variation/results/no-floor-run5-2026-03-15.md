Artifact written to `simulations/scout/competitors/plugin-competitors-R2-2026-03-15.md`.

---

## Competitive Brief: Signal

### The Primary Competitor: Inertia (Threat: HIGH)

The real threat is the team that opens a Jira ticket, writes three lines of acceptance criteria, and starts coding. Inertia wins because:
- No shared vocabulary for "pre-build evidence" — no word means no checklist, no gate
- Retrospective cost is invisible at commit time (rewrite appears 6 months later)
- Every AI tool in the dev environment (Copilot, Cursor, Claude Code) accelerates *toward* implementation — nothing pulls toward investigation
- The counterfactual is invisible: teams that shipped fine without it can't see the feature they didn't have to rewrite

### The Whitespace

**No tool occupies: structured, artifact-producing, multi-dimension evidence gathering for developers before feature commitment.**

- PM tools (Productboard, Dovetail) gather customer signals before roadmap decisions — different evidence, different audience
- ADR tools (adr-tools, Log4Brains) capture decisions already made — Signal investigates *before* the decision
- AI coding workspaces (Copilot Workspace, Cursor) assume the decision to build is made — Signal operates upstream
- Pre-mortem exists as a facilitation technique only — no product operationalizes it as a developer workflow

### Key Competitors

| Competitor | Threat | Why |
|-----------|--------|-----|
| Inertia | **HIGH** | Zero switching cost, pre-installed on every team |
| GitHub Copilot Workspace | **HIGH (future)** | Expanding brainstorm phase could grow backward into Signal's territory |
| Linear Product Intelligence | **MEDIUM (future)** | Managing in-flight work today; could expand to pre-feature triage |
| claude-code-workflows / Superpowers | LOW-MEDIUM | Lifecycle structure but no evidence-gathering taxonomy |
| Productboard / Dovetail | LOW | PM-side only; complementary |
| adr-tools | LOW | Post-decision capture; complementary |
| LaunchDarkly | NONE | Post-build release layer; purely complementary |

### --mode risk (Executive Frame)

One avoided full-feature rework per year = ~$80K (2 engineers at $200K/year). Signal's cost = one SKILL.md file + one session per feature. This is a risk management decision, not a tooling decision.

### 3 Amendments

1. **Narrow to Claude Code ecosystem** — tighter whitespace analysis, Copilot Workspace becomes the clear #1 threat
2. **Add enterprise procurement lens** — adds SOC 2 to table stakes, "approved vendor list" to inertia stickiness
3. **Focus on PM-to-dev handoff gap** — reframes Signal as "the missing middle layer" between Dovetail and Copilot Workspace
