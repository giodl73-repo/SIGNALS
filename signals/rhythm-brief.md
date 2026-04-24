You are running /rhythm-brief for: {{topic}}

Run the full topic narrative campaign in sequence. Orchestrates the core topic-tracking
skills to produce a complete briefing document: registration, signal roadmap, and
current coverage status.

DISPLAY ONLY -- this skill coordinates display skills. No artifact is written by this
skill directly. The sub-skill outputs are displayed inline.

---

## STEP 1 -- TOPIC REGISTRATION CHECK

Glob: signals/TOPICS.md or signals/**/{{topic}}-*
If no artifacts exist for this topic: display "Topic not yet registered. Run /topic-new {{topic}} to register."
If artifacts exist: display "Topic active. N artifacts found."

---

## STEP 2 -- SIGNAL STATUS (equivalent to /rhythm-status {{topic}})

Glob: signals/**/{{topic}}-*-*.md
Display the current signal state:

```
SIGNAL STATUS: {{topic}}
========================
Found:   N signals across N namespaces
Missing: M signals (from strategy.md baseline, if present)
Coverage: N/(N+M) = Z%

SIGNALS FOUND:
  <namespace>/<skill>  <date>
  ...

BLOCKING GAPS (run before commit):
  <namespace>/<skill>  -- <inertia risk: what the team assumes if they skip this>
  ...

COMMITMENT READINESS: READY | NOT READY | NO BASELINE
```

---

## STEP 3 -- ROADMAP (equivalent to /topic-plan {{topic}})

Based on the signals found and missing, display the recommended signal sequence:

```
RECOMMENDED NEXT SIGNALS:
  Priority 1 (blocks commitment):
    -> /[skill] {{topic}}   [reason this is blocking]
  Priority 2 (high value):
    -> /[skill] {{topic}}   [reason]
  Priority 3 (optional):
    -> /[skill] {{topic}}   [trade-off if skipped]
```

---

## STEP 4 -- BRIEF SUMMARY

Display a 3-sentence executive brief:

```
BRIEF: {{topic}}
[Sentence 1: What this topic is and why it matters]
[Sentence 2: What the signals say so far -- one key finding]
[Sentence 3: What the team needs to do next before committing]
```