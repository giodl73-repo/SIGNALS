---
skill: signal
date: 2026-03-17
rounds: 0
score: 100
status: GOLDEN
notes: "Index/help meta-skill -- golden written directly, no quest loop needed (deterministic output)"
---

## Prompt Body

You are running /signal — the Signal command index.

Show the user what Signal can do.

If called with no arguments: show the namespace overview and top commands.
If called with a namespace name (e.g. /signal scout): show all skills in that namespace.
If called with --bare: show all commands as bare stems, alphabetical.
If called with --all: show all 77+ commands including internals.

## Namespace Overview

Show this summary when called with no arguments:

```
Signal — Feature Decision Intelligence
77 skills across 14 namespaces

CAMPAIGNS (start here):
  /decide          Full pre-commitment decision campaign
  /simulate        Technical simulation campaign  
  /validate        Design validation campaign
  /evidence        Full evidence campaign
  /blueprint       Complete specification package
  /brief           Topic narrative campaign

DISCOVERY:
  /competitors  /inertia  /feasibility  /risk  /size
  /compliance   /market   /naming       /positioning  /stakeholders  /requirements

SPECIFICATION:
  /spec  /proposal  /pitch  /brainstorm

VALIDATION:
  /design  /users  /customers  /code

EVIDENCE:
  /hypothesis  /websearch  /intelligence  /analysis
  /synthesize  /prototype  /publish  /interview

SIMULATION:
  /lifecycle  /conversation  /dataflow  /integration
  /trigger    /ratelimit     /resilience

VERIFICATION:
  /request  /state  /contract  /component
  /deployment  /migration  /permissions  /inspect

ADOPTION:
  /feedback  /support  /adoption

NARRATIVE:
  /open  /status  /roadmap  /story  /reflect  /retro  /report
  /achievements  /signal (this)

GOVERNANCE:
  /scan  /build  /rob  /pr  /chart  /committee  /roles  /check  /leaderboard

TOOLS:
  /setup  /coverage  /preview  /accept  /file-issue

Type /signal <namespace> for skills in that namespace.
Type /signal --bare for the full alphabetical command list.
```

The primary rule: the primary competitor is always inertia.
Before any feature decision, ask: why would teams do nothing instead?
