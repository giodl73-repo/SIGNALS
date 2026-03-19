import os
os.chdir('C:/src/sim')

OUT = 'simulations/quest/golden/prove-topic-variate-R3-2026-03-16.md'

# -----------------------------------------------------------------------
# BUILDING BLOCKS
# -----------------------------------------------------------------------

def campaign_open_basic():
    return (
        "---\n"
        "CAMPAIGN OPEN\n\n"
        "topic: {topic}\n"
        "date: {date}\n"
        "status_quo_comparator: {status_quo_comparator}\n"
        "---\n"
    )

def campaign_open_with_incumbent():
    return (
        "---\n"
        "CAMPAIGN OPEN\n\n"
        "topic: {topic}\n"
        "date: {date}\n"
        "status_quo_comparator: {status_quo_comparator}\n"
        "incumbent: [full name of the primary incumbent or dominant current approach for {topic}]\n"
        "incumbent_strength: [LOW / MEDIUM / HIGH: one-sentence quantified justification,"
        " e.g., \"HIGH: 67% market share, $50K average switching cost\"]\n\n"
        "NOTE: All Invariant D checks in this session bind to the incumbent named above.\n"
        "Do not re-establish or rename the incumbent within stage bodies.\n"
        "---\n"
    )

def incumbent_anchor_basic():
    return (
        "---\n"
        "INCUMBENT ANCHOR\n\n"
        "incumbent_name: [identify the primary incumbent or dominant current approach for {topic}]\n"
        "incumbent_strength: [assess resistance level: LOW / MEDIUM / HIGH -- with one-sentence justification]\n"
        "incumbent_vulnerability: [identify the most likely displacement vector]\n"
        "---\n"
    )

def incumbent_anchor_c15():
    return (
        "---\n"
        "INCUMBENT ANCHOR\n\n"
        "incumbent_name: [same value as `incumbent` declared in CAMPAIGN OPEN above]\n"
        "incumbent_vulnerability: [identify the most likely displacement vector]\n"
        "---\n"
    )

def session_invariants_basic():
    return (
        "---\n"
        "SESSION INVARIANTS\n\n"
        "  Invariant A -- Write sequencing:\n"
        "    No artifact write may occur before its stage gate clears.\n\n"
        "  Invariant B -- Null tally chain:\n"
        "    The running null count carried forward into each stage must match\n"
        "    the closing count from the prior stage. Cross-check at Stage 4 close.\n\n"
        "  Invariant C -- Dual-lock:\n"
        "    Both hypothesis_verdict and confidence_composite must be locked\n"
        "    before Stage 5 prose begins.\n\n"
        "  Invariant D -- Incumbent displacement framing:\n"
        "    Every INCUMBENT CHECK TABLE question must use the exact template for its stage:\n"
        "      Stage 2: \"Does [evidence item] support the displacement of...\"\n"
        "      Stage 3: \"Does [practitioner account] reveal a viable transition path from...\"\n"
        "      Stage 4: \"Does [prototype result] make a credible case for displacing...\"\n\n"
        "  Invariant E -- Handoff schema completeness:\n"
        "    HANDOFF TABLE must contain all 11 fields with [derived from: X] annotations.\n"
        "---\n"
    )

def session_invariants_c15_basic():
    return (
        "---\n"
        "SESSION INVARIANTS\n\n"
        "  Invariant A -- Write sequencing:\n"
        "    No artifact write may occur before its stage gate clears.\n\n"
        "  Invariant B -- Null tally chain:\n"
        "    The running null count carried forward into each stage must match\n"
        "    the closing count from the prior stage. Cross-check at Stage 4 close.\n\n"
        "  Invariant C -- Dual-lock:\n"
        "    Both hypothesis_verdict and confidence_composite must be locked\n"
        "    before Stage 5 prose begins.\n\n"
        "  Invariant D -- Incumbent displacement framing (bound to CAMPAIGN OPEN incumbent):\n"
        "    Every INCUMBENT CHECK TABLE question must use the exact template for its stage.\n"
        "    The incumbent named in CAMPAIGN OPEN is the displacement target throughout.\n"
        "      Stage 2: \"Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN] by {topic}?\"\n"
        "      Stage 3: \"Does [practitioner account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN] to {topic}?\"\n"
        "      Stage 4: \"Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN OPEN] with {topic}?\"\n\n"
        "  Invariant E -- Handoff schema completeness:\n"
        "    HANDOFF TABLE must contain all 11 fields with [derived from: X] annotations.\n"
        "---\n"
    )

def session_invariants_registry(c15=False, c17=False):
    d_block = (
        "  Invariant D -- Incumbent displacement framing (bound to CAMPAIGN OPEN incumbent)\n"
        "    Registered label: FORMAT ERROR\n"
        "    Rule: Every INCUMBENT CHECK TABLE question must use the exact template for its stage.\n"
        "          The incumbent named in CAMPAIGN OPEN is the displacement target throughout.\n"
        "            Stage 2: \"Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN] by {topic}?\"\n"
        "            Stage 3: \"Does [practitioner account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN] to {topic}?\"\n"
        "            Stage 4: \"Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN OPEN] with {topic}?\"\n"
    ) if c15 else (
        "  Invariant D -- Incumbent displacement framing\n"
        "    Registered label: FORMAT ERROR\n"
        "    Rule: Every INCUMBENT CHECK TABLE question must use the exact template\n"
        "          for its stage:\n"
        "            Stage 2: \"Does [evidence item] support the displacement of...\"\n"
        "            Stage 3: \"Does [practitioner account] reveal a viable transition path from...\"\n"
        "            Stage 4: \"Does [prototype result] make a credible case for displacing...\"\n"
    )
    f_block = (
        "\n  Invariant F -- Synthesis declarations format\n"
        "    Registered label: SYNTHESIS FORMAT ERROR\n"
        "    Rule: hypothesis_verdict, confidence_composite, and key_risk must appear\n"
        "          as labeled key-value pairs in the SYNTHESIS DECLARATIONS section.\n"
        "          They must NOT be embedded only within prose sentences.\n"
    ) if c17 else ""
    return (
        "---\n"
        "SESSION INVARIANTS -- FAILURE LABEL REGISTRY\n\n"
        "The following canonical failure labels are registered for this session.\n"
        "Every inline enforcement checkpoint MUST echo the exact label from this registry.\n"
        "Any checkpoint that uses a different label is itself a FORMAT ERROR.\n\n"
        "  Invariant A -- Write sequencing\n"
        "    Registered label: ORDER ERROR\n"
        "    Rule: No artifact write may occur before its stage gate clears.\n\n"
        "  Invariant B -- Null tally chain\n"
        "    Registered label: INTEGRITY FAILURE\n"
        "    Rule: The running null count carried forward into each stage must match\n"
        "          the closing count from the prior stage. Cross-check at Stage 4 close.\n\n"
        "  Invariant C -- Dual-lock\n"
        "    Registered label: DUAL-LOCK ERROR\n"
        "    Rule: Both hypothesis_verdict and confidence_composite must be locked\n"
        "          before Stage 5 prose begins.\n\n"
        + d_block +
        "\n  Invariant E -- Handoff schema completeness\n"
        "    Registered label: FAIL\n"
        "    Rule: HANDOFF TABLE must contain all 11 fields with [derived from: X]\n"
        "          annotations. Any missing field triggers FAIL.\n"
        + f_block +
        "---\n"
    )

def role_table(c15=False):
    if c15:
        return (
            "---\n"
            "ROLE OWNERSHIP TABLE\n\n"
            "| Role   | Owner                        | Runs    | Responsibility                                       |\n"
            "|--------|------------------------------|---------|------------------------------------------------------|\n"
            "| ROLE C | incumbent threat analyst     | first   | Confirm CAMPAIGN OPEN incumbent, assess vulnerability|\n"
            "| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data  |\n"
            "| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence                |\n"
            "---\n"
        )
    return (
        "---\n"
        "ROLE OWNERSHIP TABLE\n\n"
        "| Role   | Owner                        | Runs    | Responsibility                                      |\n"
        "|--------|------------------------------|---------|-----------------------------------------------------|\n"
        "| ROLE C | incumbent threat analyst     | first   | Identify incumbent, assess strength + vulnerability |\n"
        "| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data |\n"
        "| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence               |\n"
        "---\n"
    )

def ce_verdict_table():
    return (
        "---\n"
        "CE VERDICT OWNERSHIP TABLE\n\n"
        "| Stage | CE Verdict Owner         | Output                                      |\n"
        "|-------|--------------------------|---------------------------------------------|\n"
        "| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |\n"
        "| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |\n"
        "| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |\n"
        "| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |\n"
        "| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |\n"
        "| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |\n"
        "---\n"
    )

def handoff_schema(c15=False, fail_note=False):
    inc_src = "campaign open" if c15 else "incumbent anchor"
    note = "\nAny field absent triggers Invariant E: FAIL.\n" if fail_note else "\n"
    return (
        "---\n"
        "PRE-COMMITTED HANDOFF SCHEMA TABLE\n\n"
        "The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5."
        + note +
        "| Field                  | Source stage | Annotation requirement          |\n"
        "|------------------------|--------------|---------------------------------|\n"
        "| topic                  | S0           | [derived from: campaign open]   |\n"
        "| hypothesis_text        | S1           | [derived from: S1 lock]         |\n"
        "| hypothesis_verdict     | S5           | [derived from: dual-lock]       |\n"
        "| confidence_composite   | S5           | [derived from: dual-lock]       |\n"
        "| key_risk               | S5           | [derived from: synthesis body]  |\n"
        "| null_tally_final       | S4           | [derived from: S4 cross-check]  |\n"
        f"| incumbent_name         | S0           | [derived from: {inc_src}]|\n"
        "| incumbent_verdict      | S5           | [derived from: synthesis body]  |\n"
        "| counter_hypothesis     | S5           | [derived from: counter-hyp res] |\n"
        "| counter_verdict        | S5           | [derived from: counter-hyp res] |\n"
        "| next_signal            | S5           | [derived from: synthesis body]  |\n"
        "---\n"
    )

def exit_signals():
    return (
        "---\n"
        "EXIT SIGNALS (declared in order, pre-committed)\n\n"
        "  Stage 0: gate_open\n"
        "  Stage 1: hypothesis_locked\n"
        "  Stage 2: websearch_complete\n"
        "  Stage 3: interview_complete\n"
        "  Stage 4: prototype_complete\n"
        "  Stage 5: synthesis_complete\n"
        "---\n"
    )

def stage0(two_layer=False, c15=False):
    rows = (
        "| Topic is scoped and bounded                 | [PASS / FAIL] |\n"
        "|---------------------------------------------|---------------|\n"
        "| Status-quo comparator is named              | [PASS / FAIL] |\n"
        "| Prior scout data available or waived        | [PASS / FAIL] |\n"
        "| Incumbent confirmed (matches CAMPAIGN OPEN) | [PASS / FAIL] |\n"
    ) if c15 else (
        "| Topic is scoped and bounded           | [PASS / FAIL] |\n"
        "|---------------------------------------|---------------|\n"
        "| Status-quo comparator is named        | [PASS / FAIL] |\n"
        "| Prior scout data available or waived  | [PASS / FAIL] |\n"
        "| Incumbent identified                  | [PASS / FAIL] |\n"
    )
    cp = "\nInvariant A checkpoint -- ORDER ERROR: No Stage 1 artifact write may occur until this gate clears.\n" if two_layer else ""
    return (
        "---\n"
        "STAGE 0 -- GATE S\n\n"
        "ROLE B executes gate_s_cleared check.\n\n"
        "| Gate condition                        | Status        |\n"
        "|---------------------------------------|---------------|\n"
        + rows +
        "\nAll rows must be PASS to proceed.\n"
        + cp +
        "\nIf all PASS:\n"
        "  EXIT SIGNAL: gate_open\n"
        "  ROLE B hands off to ROLE A.\n"
        "---\n"
    )

def stage1(two_layer=False):
    cp = "\nInvariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before gate_open is confirmed.\n" if two_layer else ""
    return (
        "---\n"
        "STAGE 1 -- HYPOTHESIS\n\n"
        "ROLE A locks the hypothesis.\n\n"
        "hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]\n"
        "null_hypothesis: [one declarative sentence stating what failure looks like]\n"
        "counter_hypothesis: [one declarative sentence stating the strongest opposing claim]\n"
        + cp +
        "\nWrite artifact: {topic}-hypothesis-{date}.md\n"
        "  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic\n\n"
        "EXIT SIGNAL: hypothesis_locked\n"
        "---\n"
    )

def stage2(two_layer=False, c15=False, c16=False):
    inc = "[incumbent]" if c15 else "[incumbent_name]"
    col = "(Stage 2 template -- incumbent from CAMPAIGN OPEN)" if c15 else "(Stage 2 template)"
    ctx = "Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.\n\n" if c15 else ""
    if two_layer:
        inv_d = (
            "Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 2 template exactly"
            + (", referencing the incumbent from CAMPAIGN OPEN" if c15 else "") + ":\n"
            "  \"Does [evidence item] support the displacement of "
            + ("[incumbent from CAMPAIGN OPEN]" if c15 else "[incumbent_name]")
            + " by {topic}?\"\n\n"
        )
    else:
        inv_d = ""
    b_check = "\nInvariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 2 nulls.\n" if two_layer else ""
    a_check = "\nInvariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before websearch stage gate clears.\n" if two_layer else ""
    disp = (
        f"\nDisplacement read: Stage 2 evidence NET [SUPPORTS / DOES NOT SUPPORT / IS INCONCLUSIVE ON] displacement of {inc} by {{topic}}. "
        "Primary supporting dimension: [dimension]. Primary open challenge: [dimension or \"none identified\"].\n"
    ) if c16 else ""
    dr_note = ", Displacement read" if c16 else ""
    return (
        "---\n"
        "STAGE 2 -- WEB SEARCH\n\n"
        "ROLE A drives web search evidence gathering.\n\n"
        "Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]\n\n"
        f"INCUMBENT CHECK TABLE -- Stage 2\n{ctx}{inv_d}"
        f"| # | Evidence item             | Invariant D question {col:<45} | Answer       | Null? |\n"
        "|---|---------------------------|----------------------------------------------|--------------|-------|\n"
        f"| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of {inc} by {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of {inc} by {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of {inc} by {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of {inc} by {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of {inc} by {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n\n"
        "Running null tally closing Stage 2: [sum of Null? column]\n"
        + b_check + disp + a_check +
        "\nWrite artifact: {topic}-websearch-{date}.md\n"
        f"  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally{dr_note}, date, topic\n\n"
        "EXIT SIGNAL: websearch_complete\n"
        "---\n"
    )

def stage3(two_layer=False, c15=False, c16=False):
    inc = "[incumbent]" if c15 else "[incumbent_name]"
    col = "(Stage 3 template -- incumbent from CAMPAIGN OPEN)" if c15 else "(Stage 3 template)"
    ctx = "Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.\n\n" if c15 else ""
    if two_layer:
        inv_d = (
            "Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 3 template exactly"
            + (", referencing the incumbent from CAMPAIGN OPEN" if c15 else "") + ":\n"
            "  \"Does [practitioner account] reveal a viable transition path from "
            + ("[incumbent from CAMPAIGN OPEN]" if c15 else "[incumbent_name]")
            + " to {topic}?\"\n\n"
        )
    else:
        inv_d = ""
    b_check = "\nInvariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 3 nulls.\n" if two_layer else ""
    a_check = "\nInvariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before interview stage gate clears.\n" if two_layer else ""
    disp = (
        f"\nDisplacement read: Stage 3 practitioner accounts NET [SUPPORT / DO NOT SUPPORT / ARE INCONCLUSIVE ON] viable transition away from {inc} toward {{topic}}. "
        "Transition confidence signal: [HIGH / MEDIUM / LOW]. Dominant blocker if any: [blocker or \"none identified\"].\n"
    ) if c16 else ""
    dr_note = ", Displacement read" if c16 else ""
    return (
        "---\n"
        "STAGE 3 -- INTERVIEW\n\n"
        "ROLE A drives practitioner interview simulation.\n\n"
        "Running null tally entering Stage 3: [carry forward closing tally from Stage 2]\n\n"
        f"INCUMBENT CHECK TABLE -- Stage 3\n{ctx}{inv_d}"
        f"| # | Practitioner account       | Invariant D question {col:<45} | Answer       | Null? |\n"
        "|---|----------------------------|----------------------------------------------|--------------|-------|\n"
        f"| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from {inc} to {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from {inc} to {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from {inc} to {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from {inc} to {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from {inc} to {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n\n"
        "Running null tally closing Stage 3: [opening tally + Stage 3 nulls]\n"
        + b_check + disp + a_check +
        "\nWrite artifact: {topic}-interview-{date}.md\n"
        f"  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally{dr_note}, date, topic\n\n"
        "EXIT SIGNAL: interview_complete\n"
        "---\n"
    )

def stage4(two_layer=False, c15=False, c16=False):
    inc = "[incumbent]" if c15 else "[incumbent_name]"
    col = "(Stage 4 template -- incumbent from CAMPAIGN OPEN)" if c15 else "(Stage 4 template)"
    ctx = "Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.\n\n" if c15 else ""
    if two_layer:
        inv_d = (
            "Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 4 template exactly"
            + (", referencing the incumbent from CAMPAIGN OPEN" if c15 else "") + ":\n"
            "  \"Does [prototype result] make a credible case for displacing "
            + ("[incumbent from CAMPAIGN OPEN]" if c15 else "[incumbent_name]")
            + " with {topic}?\"\n\n"
        )
    else:
        inv_d = ""
    b_check = "\nInvariant B checkpoint -- INTEGRITY FAILURE: Match must be true. If false, halt and recount.\n" if two_layer else ""
    a_check = "\nInvariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before prototype stage gate clears.\n" if two_layer else ""
    disp = (
        f"\nDisplacement read: Stage 4 prototype results NET [MAKE / DO NOT MAKE / PARTIALLY MAKE] a credible displacement case against {inc}. "
        "Cumulative displacement signal across S2+S3+S4: [STRONG / MODERATE / WEAK / CONTRADICTORY]. Deciding factor: [factor].\n"
    ) if c16 else ""
    dr_note = ", Displacement read" if c16 else ""
    return (
        "---\n"
        "STAGE 4 -- PROTOTYPE\n\n"
        "ROLE A drives prototype result evaluation.\n\n"
        "Running null tally entering Stage 4: [carry forward closing tally from Stage 3]\n\n"
        f"INCUMBENT CHECK TABLE -- Stage 4\n{ctx}{inv_d}"
        f"| # | Prototype result           | Invariant D question {col:<45} | Answer       | Null? |\n"
        "|---|----------------------------|----------------------------------------------|--------------|-------|\n"
        f"| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing {inc} with {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing {inc} with {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n"
        f"| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing {inc} with {{topic}}?  | [Y/N/PARTIAL]| [0/1] |\n\n"
        "Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]\n\n"
        "NULL TALLY CROSS-CHECK:\n"
        "  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]\n"
        + b_check + disp + a_check +
        "\nWrite artifact: {topic}-prototype-{date}.md\n"
        f"  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check{dr_note}, date, topic\n\n"
        "EXIT SIGNAL: prototype_complete\n"
        "---\n"
    )

def stage5(two_layer=False, c15=False, c16=False, c17=False):
    dual_cp = "\nInvariant C checkpoint -- DUAL-LOCK ERROR: Both values must be locked before any synthesis prose is written.\n" if two_layer else ""
    e_cp = "\nInvariant E checkpoint -- FAIL: All 11 fields must be present with [derived from: X] annotations.\n" if two_layer else ""
    a_cp = "\nInvariant A checkpoint -- ORDER ERROR: Both artifact writes below must not occur before dual-lock is confirmed.\n" if two_layer else ""
    inc_src = "campaign open" if c15 else "incumbent anchor"
    use_decl = c17

    if c17:
        body_ref = "[value from declarations]"
        synth_decl = (
            "SYNTHESIS DECLARATIONS\n"
            "Do not embed these values in prose sentences. Each on its own line, extractable by label match.\n\n"
            "Invariant F checkpoint -- SYNTHESIS FORMAT ERROR: Values below must appear as labeled key-value pairs, not only in prose.\n\n"
            "  hypothesis_verdict: [value from dual-lock above]\n"
            "  confidence_composite: [value from dual-lock above]\n"
            "  key_risk: [one sentence naming the primary remaining risk]\n"
            "  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]\n"
            "  next_signal: [name the next Signal skill recommended]\n\n"
        )
        if c15 and c16:
            synth_prose = (
                "SYNTHESIS BODY\n\n"
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by the name declared in CAMPAIGN OPEN. "
                "Must address counter-hypothesis verdict. Must reference the cumulative Displacement read from Stage 4. "
                "The prose contextualizes and supports the SYNTHESIS DECLARATIONS values -- it does not replace them.]\n\n"
            )
        else:
            synth_prose = (
                "SYNTHESIS BODY\n\n"
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name and address counter-hypothesis verdict. "
                "The prose contextualizes the SYNTHESIS DECLARATIONS values -- it does not replace them.]\n\n"
            )
    else:
        body_ref = "[value from synthesis body]"
        synth_decl = ""
        if c15 and c16:
            prose_body = (
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by the name declared in CAMPAIGN OPEN, "
                "address counter-hypothesis verdict, and state key_risk explicitly. "
                "Must reference the cumulative Displacement read from Stage 4.]"
            )
        elif c15:
            prose_body = (
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by the name declared in CAMPAIGN OPEN, "
                "address counter-hypothesis verdict, and state key_risk explicitly.]"
            )
        elif c16:
            prose_body = (
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name, address counter-hypothesis verdict, "
                "and state key_risk explicitly. May reference the per-stage Displacement reads from S2, S3, S4 to support the cumulative argument.]"
            )
        else:
            prose_body = (
                "[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name, "
                "address counter-hypothesis verdict, and state key_risk explicitly.]"
            )
        synth_prose = (
            "SYNTHESIS BODY\n\n"
            f"{prose_body}\n\n"
            "  key_risk: [one sentence naming the primary remaining risk]\n"
            "  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]\n"
            "  next_signal: [name the next Signal skill recommended]\n\n"
        )

    hv_val = body_ref if c17 else "[value from dual-lock]"
    cc_val = body_ref if c17 else "[value from dual-lock]"
    kr_val = body_ref if c17 else "[value from synthesis body]"
    iv_val = body_ref if c17 else "[value from synthesis body]"
    ns_val = body_ref if c17 else "[value from synthesis body]"
    inc_val = "[value from campaign open]" if c15 else f"[value from {inc_src}]"
    inc_anno = "[derived from: campaign open]" if c15 else f"[derived from: {inc_src}]"

    synth_art = "counter-hypothesis resolution table, SYNTHESIS DECLARATIONS, synthesis body" if c17 else "counter-hypothesis resolution table, dual-lock values, synthesis body"
    if c16:
        synth_art += ", all three Displacement reads"

    return (
        "---\n"
        "STAGE 5 -- SYNTHESIS\n\n"
        "COUNTER-HYPOTHESIS RESOLUTION TABLE\n\n"
        "| Counter-hypothesis text              | Evidence against             | Verdict                                        |\n"
        "|--------------------------------------|------------------------------|------------------------------------------------|\n"
        "| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |\n\n"
        "ATOMIC DUAL-LOCK\n"
        + dual_cp +
        "\n  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]\n"
        "  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]\n\n"
        "  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]\n\n"
        + synth_decl
        + synth_prose
        + "HANDOFF TABLE\n"
        + e_cp + "\n"
        "| Field                | Value                                    | Annotation                      |\n"
        "|----------------------|------------------------------------------|---------------------------------|\n"
        "| topic                | {topic}                                  | [derived from: campaign open]   |\n"
        "| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |\n"
        f"| hypothesis_verdict   | {hv_val:<40} | [derived from: dual-lock]       |\n"
        f"| confidence_composite | {cc_val:<40} | [derived from: dual-lock]       |\n"
        f"| key_risk             | {kr_val:<40} | [derived from: synthesis body]  |\n"
        "| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |\n"
        f"| incumbent_name       | {inc_val:<40} | {inc_anno}|\n"
        f"| incumbent_verdict    | {iv_val:<40} | [derived from: synthesis body]  |\n"
        "| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |\n"
        "| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |\n"
        f"| next_signal          | {ns_val:<40} | [derived from: synthesis body]  |\n\n"
        + a_cp +
        f"\nWrite artifact: {{topic}}-synthesis-{{date}}.md\n"
        f"  Contents: {synth_art}, date, topic\n\n"
        "Write artifact: {topic}-handoff-{date}.md\n"
        "  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic\n\n"
        "EXIT SIGNAL: synthesis_complete\n"
        "---\n"
    )

# -----------------------------------------------------------------------
# SKILL HEADER
# -----------------------------------------------------------------------
def skill_header():
    return (
        "You are running the prove-topic Signal skill.\n\n"
        "Topic: {topic}\n"
        "Date: {date}\n"
        "Status-quo comparator: {status_quo_comparator}\n\n"
    )

# -----------------------------------------------------------------------
# ASSEMBLE VARIATIONS
# -----------------------------------------------------------------------
def variation(
    vnum, axis_title, axis_desc, hypothesis,
    camp, anchor, inv, roles, ce, schema, exits,
    s0, s1, s2, s3, s4, s5
):
    body = skill_header() + camp + anchor + inv + roles + ce + schema + exits + s0 + s1 + s2 + s3 + s4 + s5
    return (
        f"## {vnum} -- Axis: {axis_title}\n\n"
        f"**Variation axis**: {axis_desc}\n\n"
        f"**Hypothesis**: {hypothesis}\n\n"
        "---\n\n"
        "```\n"
        + body +
        "```\n"
    )

# V-01: C-14 only
v01 = variation(
    "V-01", "Two-Layer Enforcement Architecture (C-14)",
    "C-14 only -- two-layer enforcement (canonical failure labels in SESSION INVARIANTS block, verbatim echo at every inline checkpoint)",
    ("Registering canonical failure labels once in the SESSION INVARIANTS block and requiring every inline checkpoint to echo the exact registered label "
     "creates bidirectional self-incrimination: any drift between the registered label and the inline echo is detectable from either direction simultaneously, "
     "making enforcement failures visible without requiring external audit."),
    campaign_open_basic(), incumbent_anchor_basic(), session_invariants_registry(c15=False, c17=False),
    role_table(c15=False), ce_verdict_table(), handoff_schema(c15=False, fail_note=True), exit_signals(),
    stage0(two_layer=True, c15=False), stage1(two_layer=True),
    stage2(two_layer=True, c15=False, c16=False), stage3(two_layer=True, c15=False, c16=False),
    stage4(two_layer=True, c15=False, c16=False), stage5(two_layer=True, c15=False, c16=False, c17=False),
)

# V-02: C-15 only
v02 = variation(
    "V-02", "CAMPAIGN OPEN Pre-Registration (C-15)",
    "C-15 only -- CAMPAIGN OPEN block appears BEFORE SESSION INVARIANTS and explicitly declares `incumbent` and `incumbent_strength` so all Invariant D checks bind to a persistent named displacement context",
    ("Declaring `incumbent` and `incumbent_strength` in CAMPAIGN OPEN before SESSION INVARIANTS are established forces Invariant D to bind to a persistent named entity rather than "
     "re-establishing context per stage, eliminating the risk of incumbent drift across stages and making the entire session's displacement framing traceable to a single declared anchor."),
    campaign_open_with_incumbent(), incumbent_anchor_c15(), session_invariants_c15_basic(),
    role_table(c15=True), ce_verdict_table(), handoff_schema(c15=True, fail_note=False), exit_signals(),
    stage0(two_layer=False, c15=True), stage1(two_layer=False),
    stage2(two_layer=False, c15=True, c16=False), stage3(two_layer=False, c15=True, c16=False),
    stage4(two_layer=False, c15=True, c16=False), stage5(two_layer=False, c15=True, c16=False, c17=False),
)

# V-03: C-16 only
v03 = variation(
    "V-03", "Per-Stage Displacement Read Fields (C-16)",
    "C-16 only -- each of Stages 2, 3, and 4 has a dedicated \"Displacement read:\" synthesis field appearing after the INCUMBENT CHECK TABLE rows, summarizing the stage's net displacement verdict",
    ("Adding a \"Displacement read:\" field after each INCUMBENT CHECK TABLE transforms the table from a compliance checkbox into an active displacement test -- "
     "each stage is forced to commit to a directional verdict before advancing, making the cumulative displacement argument visible and auditable at each transition "
     "point rather than only at Stage 5 synthesis."),
    campaign_open_basic(), incumbent_anchor_basic(), session_invariants_basic(),
    role_table(c15=False), ce_verdict_table(), handoff_schema(c15=False, fail_note=False), exit_signals(),
    stage0(two_layer=False, c15=False), stage1(two_layer=False),
    stage2(two_layer=False, c15=False, c16=True), stage3(two_layer=False, c15=False, c16=True),
    stage4(two_layer=False, c15=False, c16=True), stage5(two_layer=False, c15=False, c16=True, c17=False),
)

# V-04: C-14 + C-17
v04 = variation(
    "V-04", "Two-Layer Enforcement + SYNTHESIS DECLARATIONS Prohibition (C-14 + C-17)",
    "C-14 + C-17 combined -- canonical failure labels registered in SESSION INVARIANTS and echoed inline at every checkpoint; Stage 5 opens with SYNTHESIS DECLARATIONS section whose header explicitly prohibits embedding values in prose",
    ("Combining two-layer enforcement (bidirectional label matching) with a SYNTHESIS DECLARATIONS prohibition creates end-to-end structural integrity: "
     "enforcement failures are detectable at any checkpoint via label drift, while synthesis values are guaranteed to be machine-extractable rather than "
     "narrative-buried, making the skill's output reliable for downstream automation regardless of model verbosity tendencies."),
    campaign_open_basic(), incumbent_anchor_basic(), session_invariants_registry(c15=False, c17=True),
    role_table(c15=False), ce_verdict_table(), handoff_schema(c15=False, fail_note=True), exit_signals(),
    stage0(two_layer=True, c15=False), stage1(two_layer=True),
    stage2(two_layer=True, c15=False, c16=False), stage3(two_layer=True, c15=False, c16=False),
    stage4(two_layer=True, c15=False, c16=False), stage5(two_layer=True, c15=False, c16=False, c17=True),
)

# V-05: C-14 + C-15 + C-16 + C-17
v05 = variation(
    "V-05", "Full Integration (C-14 + C-15 + C-16 + C-17)",
    ("C-14 + C-15 + C-16 + C-17 all present -- CAMPAIGN OPEN pre-registers incumbent before SESSION INVARIANTS; SESSION INVARIANTS registers canonical failure labels; "
     "inline checkpoints echo exact labels; Stages 2/3/4 each have \"Displacement read:\" synthesis fields; Stage 5 opens with SYNTHESIS DECLARATIONS section and explicit prohibition header"),
    ("The four mechanisms address four distinct failure modes simultaneously -- incumbent drift (C-15), enforcement label inconsistency (C-14), displacement evidence opacity (C-16), "
     "and synthesis value narrative burial (C-17) -- and their combination is multiplicative rather than additive: a session running all four cannot exhibit any of the four failure modes "
     "without triggering at least two independent detection mechanisms."),
    campaign_open_with_incumbent(), incumbent_anchor_c15(), session_invariants_registry(c15=True, c17=True),
    role_table(c15=True), ce_verdict_table(), handoff_schema(c15=True, fail_note=True), exit_signals(),
    stage0(two_layer=True, c15=True), stage1(two_layer=True),
    stage2(two_layer=True, c15=True, c16=True), stage3(two_layer=True, c15=True, c16=True),
    stage4(two_layer=True, c15=True, c16=True), stage5(two_layer=True, c15=True, c16=True, c17=True),
)

# -----------------------------------------------------------------------
# FRONTMATTER
# -----------------------------------------------------------------------
frontmatter = """\
---
skill: quest-variate
skill_target: prove-topic
round: R3
date: 2026-03-16
rubric: prove-topic-rubric-v3-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [two_layer_enforcement, campaign_open_preregistration, per_stage_displacement_read]
  combined: [V-04 (two_layer + synthesis_declarations), V-05 (all_four_new)]
round_targets: >
  v3 adds C-14/C-15/C-16/C-17 from R2 excellence signals.
  C-14 targets bidirectional enforcement: canonical labels in SESSION INVARIANTS + verbatim echo inline.
  C-15 targets CAMPAIGN OPEN block before SESSION INVARIANTS to give invariant D a persistent named context.
  C-16 targets per-stage displacement synthesis fields that make INCUMBENT CHECK TABLE feel like evidence.
  C-17 targets SYNTHESIS DECLARATIONS prohibition header that pre-empts narrative burial of synthesis fields.
  All five R3 variations maintain all 5 essentials and all 3 recommended criteria from v2.
r2_scores:
  V-01: [tbd]
  V-02: [tbd]
  V-03: [tbd]
  V-04: [tbd]
  V-05: [tbd]
---

"""

content = frontmatter + v01 + "\n---\n\n" + v02 + "\n---\n\n" + v03 + "\n---\n\n" + v04 + "\n---\n\n" + v05

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)

size = os.path.getsize(OUT)
print(f"Written: {OUT}")
print(f"Size: {size} bytes / {size//1024} KB")
print(f"Lines: {content.count(chr(10))}")
