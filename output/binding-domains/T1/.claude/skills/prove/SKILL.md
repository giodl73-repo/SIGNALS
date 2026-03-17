---
name: prove
description: "Prove namespace -- 9 skills for hypothesis-driven investigation.

/prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype   -> smallest-possible prototype with predicted vs actual results
/prove-analysis    -> data pattern analysis distinguishing correlation from causation
/prove-interview   -> persona-driven stakeholder interview simulation
/prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish     -> investigation write-up as paper with abstract and limitations
/prove-topic       -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.
"
allowed-tools: [Read, Write, Glob, Grep, WebSearch, WebFetch]
param_set: full
---
State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim (what you believe), a falsification condition (what evidence would prove it wrong), a confidence level (0-100), and a list of experiments that will test it. The hypothesis is a commitment -- you cannot move the goalposts after seeing results.

Write artifact to: simulations/prove/investigations/{topic}-hypothesis-{date}.md
