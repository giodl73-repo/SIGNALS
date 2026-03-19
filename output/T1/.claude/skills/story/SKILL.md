---
name: story
description: Synthesize all signals into a coherent narrative. NOT a summary of each signal -- an editorial synthesis in the author's
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


[DERIVATION PACKET SEALED]
  S0: {from E-1}
  S3: {from E-3}
  Net vector: {from E-3}
  Evidence trajectory: {from E-3}
  Signal extracts: {from E-2}
  Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- {consequence from E-4}
  Contestation analysis:
    Derivation (from E-8.5): Adjacent verb {ADJACENT_VERB} via pivot row `{artifact-name}`,
      {CURRENT} -> {ALTERNATIVE}, {VECTOR}/{ALTERNATIVE_WEIGHT} rule fires
    C-37 inline: PASS
    Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule [verbatim from E-8.5]
  C-35 verification: PASS
  C-37 verification: PASS -- two-level (E-8.5 inline + E-8.75 cross-check)
  C-38 compliance:
    AXIOM: REVISED IS the E-8.5 re-derivation event (constitutive, C-39 PASS). Declaring
      `Vector status: UNCHANGED` IS the UNCHANGED terminal outcome: E-8.5 absence declared,
      not deferred.
    Evaluation outcome: [REVISED -- Contestation re-derivation performed within step b;
      E-8.5 re-run complete before step b finished; new Contestation output sealed] |
      [UNCHANGED -- Contestation rule carried forward; no E-8.5 re-run; prior output
      retained]
  Branch Architecture Record:
    REVISED branch: `Vector status: REVISED` IS E-8.5 (AXIOM constitutive). New
      Contestation output produced within step b -> E-4 `Contestation rule:` updated ->
      E-8.75 re-runs -> re-seal. Terminal state: new derivation sealed; prior superseded.
      Causal chain: AXIOM constitutive -> E-8.5 within step b -> E-4 update ->
      step b done -> E-8.75 -> re-seal.
    UNCHANGED branch: `Vector status: UNCHANGED` IS the UNCHANGED outcome (AXIOM
      constitutive). `Contestation rule:` carried forward verbatim -> E-8.75 re-runs ->
      re-seal. Terminal state: prior derivation retained. Causal chain: AXIOM constitutive
      -> no E-8.5 -> prior output retained -> step b done -> E-8.75 -> re-seal.
  Pattern synthesis: {from E-6}
  Band: {HIGH | MEDIUM | LOW}
  Selected stance: {PROCEED | PAUSE | PIVOT | ABANDON}
  IMMUTABLE -- contents fixed after this seal. Prose and recommendation preference
    are prohibited inputs to retroactive revision.
]