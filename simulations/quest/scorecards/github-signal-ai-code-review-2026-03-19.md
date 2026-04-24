● List directory .
  └ 13 files found

● Read CLAUDE.md
  └ 12 lines read

● List directory signals
  └ 8 files found

● List directory .roles
  └ 1 file found

● List directory signals\discover
  └ 13 files found

● List directory signals\draft
  └ 1 file found

● List directory signals\simulate
  └ 3 files found

● List directory signals\validate
  └ 7 files found

● List directory signals\rhythm
  └ 3 files found

● List directory signals\roles
  └ 6 files found

● List directory signals\specify
  └ 3 files found

● List directory signals\review
  └ 3 files found

● Search (glob)
  │ "signals/**/*.md"
  └ 38 files found

Now let me check a few key signal artifacts to understand the topic context:

● Read ai-code-review-hypothesis-2026-03-19.md
  │ signals\discover\hypothesis\ai-code-review-hypothesis-2026-03-19.md
  └ L1:25 (25 lines read)

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ L1:25 (25 lines read)

● Read ai-code-review-synthesize-2026-03-19.md
  │ signals\discover\synthesize\ai-code-review-synthesize-2026-03-19.md
  └ L1:30 (30 lines read)

● Read ai-code-review-synthesize-2026-03-19.md
  │ signals\discover\synthesize\ai-code-review-synthesize-2026-03-19.md
  └ L30:50 (21 lines read)

---

# Signal — Topic Dashboard: `ai-code-review`

**Domain:** AI-powered automated code review tooling
**Date:** 2026-03-19
**Signal artifacts:** 38 across 8 namespaces
**Synthesis verdict:** PROCEED (confidence 72)
**Hypothesis confidence:** 60 — OPEN

---

## COVERAGE DASHBOARD

```
Namespace          Artifacts   Status
─────────────────────────────────────────
discover/          13/13       ██████████ COMPLETE
specify/            3/4        ████████░░ NEAR
draft/              1/1        ██████████ COMPLETE
review/             3/3        ██████████ COMPLETE
validate/           7/7        ██████████ COMPLETE
simulate/           3/7        ████░░░░░░ GAPS
roles/              5/6        █████████░ NEAR
rhythm/             3/3        ██████████ COMPLETE
prove/              0/8        ░░░░░░░░░░ NOT STARTED
─────────────────────────────────────────
Total:             38/52       ███████░░░ 73%
```

---

## SIGNAL INVENTORY

### 🔍 DISCOVERY — `discover/` (13/13 COMPLETE)

| Skill | Artifact | Key Finding |
|-------|----------|-------------|
| discover-competitors | ✅ competitors | 7+ competitors; Copilot HIGH threat via distribution |
| discover-competitors-alt | ✅ competitors-alt | Copilot CRITICAL/existential; 12–18mo window |
| discover-inertia | ✅ inertia | HIGH inertia; tips when AI code >50% of commits |
| discover-feasibility | ✅ feasibility | 68/100; 1,580 hrs / 5 eng / 12 wks; self-hosted RED |
| discover-feasibility-alt | ✅ feasibility-alt | PROCEED-WITH-GATES; DPA highest schedule risk |
| discover-risk | ✅ risk | FP fatigue CRITICAL + Copilot moat CRITICAL |
| discover-hypothesis | ✅ hypothesis | <15% FP → ≥30% labor reduction in 90 days |
| discover-brainstorm | ✅ brainstorm | 5 candidates ranked; full-PR review leads |
| discover-websearch | ✅ websearch | 5/5 key data claims CONFIRMED |
| discover-compare | ✅ compare | Option B (narrow AI-code auditor) WINS |
| discover-causal | ✅ causal | 6-step mechanism; break point at Step 3 (precision) |
| discover-coherence | ✅ coherence | 5 contradictions (2 blocking); NOT READY |
| discover-synthesize | ✅ synthesize | 12 signals → PROCEED at 72% confidence |

### 📋 SPECIFICATION — `specify/` + `draft/` (4/5)

| Skill | Artifact | Status |
|-------|----------|--------|
| draft-spec | ✅ spec | Written |
| draft-proposal | ✅ proposal | Written |
| draft-pitch | ✅ pitch | Written |
| specify-commitment | ✅ commitment | Written |
| draft-brainstorm | ⬜ — | Not run |

### 👥 REVIEW — `review/` (3/3 COMPLETE)

| Skill | Artifact | Status |
|-------|----------|--------|
| review-design | ✅ design | Written |
| review-users | ✅ users | Written |
| review-customers | ✅ customers | Written |

### ✅ VALIDATION — `validate/` (7/7 COMPLETE)

| Skill | Artifact | Status |
|-------|----------|--------|
| validate-design | ✅ design | Written |
| validate-customers | ✅ customers | Written |
| validate-code | ✅ code | Written |
| listen-feedback | ✅ feedback | Written |
| listen-support | ✅ support | Written |
| listen-adoption | ✅ adoption | Written |
| validate-adoption-blocker | ✅ adoption-blocker | Written |

### 🔄 SIMULATION — `simulate/` (3/7 GAPS)

| Skill | Artifact | Status |
|-------|----------|--------|
| flow-lifecycle | ✅ lifecycle | Written |
| trace-request | ✅ request | Written |
| trace-contract | ✅ contract | Written |
| flow-conversation | ⬜ — | Not run |
| flow-dataflow | ⬜ — | Not run |
| flow-integration | ⬜ — | Not run |
| flow-trigger | ⬜ — | Not run |

### 🏛️ GOVERNANCE — `roles/` (5/6)

| Skill | Artifact | Status |
|-------|----------|--------|
| roles-scan | ✅ scan | Written |
| roles-build | ✅ build | Written |
| roles-create | ✅ create | Written |
| roles-generate | ✅ generate | Written |
| roles-pull-request | ✅ pull-request | Written |
| roles-product-review | ⬜ — | Not run |

### 📖 NARRATIVE — `rhythm/` (3/3 COMPLETE)

| Skill | Artifact | Status |
|-------|----------|--------|
| rhythm-decide | ✅ decide | Campaign complete |
| rhythm-behavior | ✅ behavior | Campaign complete |
| rhythm-story | ✅ story | Synthesis written |

### 🔬 EVIDENCE — `prove/` (0/8 NOT STARTED)

| Skill | Artifact | Status |
|-------|----------|--------|
| prove-hypothesis | ⬜ — | Not run |
| prove-websearch | ⬜ — | Not run |
| prove-intelligence | ⬜ — | Not run |
| prove-analysis | ⬜ — | Not run |
| prove-synthesize | ⬜ — | Not run |
| prove-prototype | ⬜ — | Not run |
| prove-publish | ⬜ — | Not run |
| prove-interview | ⬜ — | Not run |

---

## GAP ANALYSIS

### 🔴 Critical Gap: Evidence Campaign (prove/)
Zero evidence artifacts. The hypothesis is OPEN at 60% confidence with no empirical validation. The discover-synthesize signal recommended PROCEED but flagged precision (<15% FP) as the existential variable. Without a prove campaign, the "PROCEED" verdict rests entirely on desk research and simulation — not field evidence.

### 🟡 Moderate Gap: Simulation Coverage (simulate/)
3/7 simulations run. Missing: `flow-conversation` (multi-turn agent interaction), `flow-dataflow` (ETL/sync tracing), `flow-integration` (cross-system API), `flow-trigger` (automation side-effects). These gaps leave blind spots in how the AI review tool integrates with CI/CD pipelines and developer workflows.

### 🟢 Minor Gaps
- **draft-brainstorm** — discover-brainstorm exists; draft variant would add spec-level ideation
- **roles-product-review** — governance roles are 5/6; product review perspective missing

---

## BLOCKING CONTRADICTIONS (from coherence)

Two **blocking** contradictions remain unresolved:
1. **Copilot threat level** — competitors says HIGH, competitors-alt says CRITICAL/existential
2. **Copilot context depth** — feasibility and competitors disagree on Copilot's cross-repo capability

> These must resolve before commitment. Run `/discover-coherence --amend` or update source signals.

---

## RECOMMENDED NEXT ACTIONS

| Priority | Action | Why |
|----------|--------|-----|
| **1** | `/prove-hypothesis ai-code-review` | Ground the OPEN hypothesis with falsification experiments |
| **2** | `/prove-prototype ai-code-review` | Build smallest-possible shadow-mode prototype to validate <15% FP |
| **3** | `/discover-coherence --amend` | Resolve 2 blocking contradictions before commitment |
| **4** | `/flow-conversation ai-code-review` | Simulate developer↔AI review interaction loops |
| **5** | `/flow-integration ai-code-review` | Trace CI/CD connector paths and gap analysis |

**Campaign shortcut:** `/evidence ai-code-review` — orchestrates prove-hypothesis → websearch → analysis → synthesize in sequence.

---

*38 signals collected • 14 gaps remaining • 2 blocking contradictions • Evidence campaign not started*
*Run `/rhythm-status ai-code-review` for commitment readiness gate.*

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Dashboard renders well in Copilot CLI. The 38-artifact scan required multiple parallel file reads — Copilot handled the glob + view pattern efficiently. No rendering issues with markdown tables in terminal. Minor concern: the skill list in `<available_skills>` was truncated to 69/178, so some skill mappings were inferred from directory structure rather than skill definitions.


Total usage est:        6 Premium requests
API time spent:         1m 42s
Total session time:     1m 49s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       228.0k in, 5.9k out, 207.6k cached (Est. 6 Premium requests)
