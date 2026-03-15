# Signal v0.1 — Shipping List (Bill of Materials)

**Target**: B-01 flat binding, skills-in-repo, 52 atomic skills
**Audience**: 5,000 Microsoft developers at all-hands
**Date started**: 2026-03-14

---

## Status Key

- [x] Done
- [~] In progress
- [ ] Not started
- [!] Blocked

---

## 1. Content — Golden Prompts (52 skills)

Each skill needs: trace-skill run -> spec findings applied -> rubric -> variate -> score -> golden

### /scout: (8 skills)
- [x] scout-competitors — GOLDEN (Round 2, score 100)
- [~] scout-feasibility — quest-run-one.sh running now
- [ ] scout-naming
- [ ] scout-compliance
- [ ] scout-market
- [ ] scout-stakeholders
- [ ] scout-positioning
- [ ] scout-requirements

### /draft: (3 skills)
- [ ] draft-spec
- [ ] draft-proposal
- [ ] draft-pitch

### /review: (4 skills)
- [ ] review-design
- [ ] review-code
- [ ] review-users
- [ ] review-customers

### /flow: (7 skills)
- [ ] flow-lifecycle
- [ ] flow-conversation
- [ ] flow-trigger
- [ ] flow-dataflow
- [ ] flow-integration
- [ ] flow-throttle
- [ ] flow-resilience

### /trace: (7 skills)
- [ ] trace-request
- [ ] trace-state
- [ ] trace-contract
- [ ] trace-component
- [ ] trace-deployment
- [ ] trace-migration
- [ ] trace-permissions

### /prove: (8 skills)
- [ ] prove-hypothesis
- [ ] prove-websearch
- [ ] prove-intelligence
- [ ] prove-prototype
- [ ] prove-analysis
- [ ] prove-interview
- [ ] prove-synthesize
- [ ] prove-publish

### /listen: (3 skills)
- [ ] listen-feedback
- [ ] listen-support
- [ ] listen-adoption

### /program: (1 skill)
- [ ] program-plan

### /topic: (6 skills)
- [ ] topic-new
- [ ] topic-status
- [ ] topic-report
- [ ] topic-plan
- [ ] topic-story
- [ ] topic-echo

### /quest: (4 skills)
- [ ] quest-rubric
- [ ] quest-variate
- [ ] quest-score
- [ ] quest-golden

### meta (2 tools, not user-facing)
- [x] trace-skill (defined in program.yaml + signal.skills.yaml)
- [ ] trace-skill golden prompt (self-trace)

---

## 2. Binding — B-01 Flat (skills-in-repo)

- [ ] `binding-flat.program.yaml` — 52 commands, one per atomic skill, with golden prompt bodies
- [ ] `craft generate --stage program` from binding-flat.program.yaml → 52 SKILL.md files
- [ ] Verify no double-frontmatter bug (CF-01) in output, or wait for craftworks fix
- [ ] `output/flat/` directory with all 52 SKILL.md files ready to copy

---

## 3. Infrastructure

### Quest automation
- [x] `quest-run-one.sh` — single skill quest loop via relay
- [x] `quest-run.py` — parallel Python runner (needs ANTHROPIC_API_KEY, use relay instead)
- [ ] `tools/quest-run-all.sh` — dispatches quest-run-one.sh for all non-golden skills in parallel via relay

### Craftworks findings to file
- [ ] CF-01: Double frontmatter in generated SKILL.md — file with `gh issue create`
- [ ] CF-02: `--hydrate` flag not compiled into CLI — file with `gh issue create`
- [ ] CF-03: program.yaml 1024-char description cap — file with `gh issue create`

### Session handover
- [ ] Update `PROMPT-HANDOVER.md` for next session with full current state

---

## 4. Dogfood (using Signal on Signal)

### Already done
- [x] `/review:customers` on plugin design — 12 personas, A-01 through A-06 recommendations
- [x] `/trace-skill` on all 8 scout skills — wave 1 + wave 2, 16 findings documented
- [x] `findings/signal-findings-2026-03-14.md` — all findings consolidated

### Remaining dogfood (run after golden prompts land)
- [ ] `/review:users` on plugin design — 5 persona advocates
- [ ] `/listen:adoption` on all-hands rollout — 5,000 developer simulation
- [ ] `/topic:status signal` — coverage check across all signals gathered
- [ ] `/topic:story signal` — synthesize everything into a narrative
- [ ] `/topic:echo signal` — what surprised us

---

## 5. Documentation

- [ ] `README.md` — one-page install + quickstart (developer path, PM path, architect path)
- [ ] `QUICKSTART.md` — first 10 minutes: copy one skill, run it, get a result
- [ ] `SKILLS.md` — human-readable catalog of all 52 skills by namespace and audience
- [ ] Update `signal.program.yaml` header comment (still says 9 namespaces, 48 skills)
- [ ] Update `signal.manifest.json` description (still says 9 namespaces)

---

## 6. Release Criteria (per namespace — all must pass before v0.1 ships)

A namespace is released when:
1. All skills traced (trace-skill runs with USEFUL verdict)
2. All spec findings applied
3. All skills quested (golden prompts, dual convergence)
4. All golden prompt bodies in signal.skills.yaml
5. binding-flat.program.yaml updated with golden bodies
6. craft generate produces clean SKILL.md (no double-frontmatter)
7. Review pass: run /review:users on the namespace's actual skill outputs

### Namespace release status

| Namespace | Traced | Spec clean | Golden | SKILL.md | Released |
|-----------|--------|-----------|--------|----------|----------|
| scout | 8/8 | 12/12 fixes | 1/8 | 0/8 | No |
| draft | 0/3 | 0 | 0/3 | 0/3 | No |
| review | 0/4 | 0 | 0/4 | 0/4 | No |
| flow | 0/7 | 0 | 0/7 | 0/7 | No |
| trace | 0/7 | 0 | 0/7 | 0/7 | No |
| prove | 0/8 | 0 | 0/8 | 0/8 | No |
| listen | 0/3 | 0 | 0/3 | 0/3 | No |
| program | 0/1 | 0 | 0/1 | 0/1 | No |
| topic | 0/6 | 0 | 0/6 | 0/6 | No |
| quest | 0/4 | 0 | 0/4 | 0/4 | No |

---

## 7. Post-v0.1 (future releases)

### v0.2 — Grouped binding + Plugin
- [ ] `binding-grouped.program.yaml` — 9 namespace dispatchers + T3 subcommand references
- [ ] `binding-plugin.program.yaml` — plugin format with signal: namespace prefix
- [ ] Test grouped binding on scout namespace first

### v0.3 — Cursor
- [ ] Cross-compile from flat binding via `craft generate --mode cross --target cursor`
- [ ] Validate against Spec 105 (Cursor Rules Workspace Conformance)

### v0.4 — Cline/Roo
- [ ] Cross-compile to Roo Code format
- [ ] Validate against Spec 107 (Cline/Roo Code Workspace Conformance)

### v0.5 — CREST experiment
- [ ] Author `CREST.md` for Signal workspace (Spec 109 validation target)
- [ ] Validate CREST generates same binding outputs as program.yaml

---

## Critical Path to v0.1

```
quest-run-all.sh (dispatch 51 skills) -- ~2-4 hours via relay
        |
        v
binding-flat.program.yaml (update 52 skill descriptions from golden prompts)
        |
        v
craft generate --stage program (build 52 SKILL.md files)
        |
        v
CF-01 fix lands in craftworks (or hand-fix double-frontmatter)
        |
        v
README.md + QUICKSTART.md
        |
        v
/review:users dogfood on actual skill outputs
        |
        v
SIGNAL v0.1 ships
```

---

*Last updated: 2026-03-14*
