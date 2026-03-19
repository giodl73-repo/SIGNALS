#!/usr/bin/env python
# Appends V-02 through V-05 to flow-lifecycle-variate-R18-2026-03-15.md
# Each variation is a complete prompt body with only targeted changes from V-01.

import re

TARGET = r"C:/src/sim/simulations/quest/golden/flow-lifecycle-variate-R18-2026-03-15.md"

# ── helpers ──────────────────────────────────────────────────────────────────

def read_v01():
    """Extract the raw prompt body from V-01 (everything after the hypothesis line up to the ---/--- separator)."""
    with open(TARGET, "r", encoding="utf-8") as f:
        text = f.read()
    # V-01 prompt body starts at "You are running **flow-lifecycle**" and ends just before "---\n---"
    # Find the first occurrence of that marker after the V-01 header
    start_marker = "You are running **flow-lifecycle** for topic: {Topic}."
    end_marker = "---\n---\n"
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    return text[start:end]

# ── transformations ───────────────────────────────────────────────────────────

C54_OLD = "CHAIN STATUS: [CLOSED / OPEN]"

C54_BLOCK = """\
**DERIVATION CLAIM:**
> For CHAIN STATUS: CLOSED to be asserted, each direction declared PRESENT in DIRECTION
> INVENTORY must evaluate to NO CONFLICT through its Violation Check. The enumeration below
> lists every PRESENT direction, its Violation Check evaluation result, and derives CLOSED
> from the complete per-direction record. Absent derivation claim is a fail even when
> per-direction Violation Checks are well-formed and CHAIN STATUS: CLOSED is declared.
> A derivation claim omitting any PRESENT direction is a fail. NOT-APPLICABLE directions exempt.

- B-NN->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Phase-exit-sequence: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Phase: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]

Derivation: All four PRESENT directions evaluate to NO CONFLICT per Violation Checks above.
CHAIN STATUS: CLOSED is logically derived from this complete per-direction evaluation record.
A single CONFLICT in any direction above produces CHAIN STATUS: OPEN regardless of other declarations.

CHAIN STATUS: [CLOSED / OPEN]"""


C55_OLD = ("An IM-ID with NONE in `Phase Refs:` cited by any PHASE ENTRY CONTRACT "
           "`IM Reference:` is an inconsistency. |")

C55_NEW = ("An IM-ID with NONE in `Phase Refs:` cited by any PHASE ENTRY CONTRACT "
           "`IM Reference:` is an inconsistency. "
           "Consistency maintained by `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY "
           "-- that labeled instruction triggers the `Phase Refs:` back-annotation workflow step; "
           "correct execution of the Return instruction prevents the IM-ID/Phase Refs inconsistency "
           "pattern from arising. |")


C56_BOTTLENECK_OLD = "NONE only if no declared bottleneck was causal. Namespace: B-ID (see architecture above).]"
C56_BOTTLENECK_NEW = "NONE only if no declared bottleneck was causal. Namespace: B-ID (see EXCEPTION BLOCK ARCHITECTURE above).]"

C56_ROLE_OLD = "R-ID fails. Namespace: R-ID (see architecture above).]"
C56_ROLE_NEW = "R-ID fails. Namespace: R-ID (see EXCEPTION BLOCK ARCHITECTURE above).]"


def apply_c54(body):
    # Replace the FIRST occurrence of the bare CHAIN STATUS line (in CHAIN STATUS section,
    # after the DIRECTION INVENTORY table). We want to find it in the CHAIN STATUS section
    # specifically -- it appears after the direction inventory table.
    # The line appears as a standalone line: "CHAIN STATUS: [CLOSED / OPEN]"
    # We replace the first occurrence that is NOT inside the DIRECTION INVENTORY table
    # (the table rows contain "CHAIN STATUS" only as part of longer strings).
    # The standalone line appears after the table, so replace the last occurrence in the
    # CHAIN STATUS section (which is the standalone declaration line).
    idx = body.rfind("\nCHAIN STATUS: [CLOSED / OPEN]\n")
    if idx == -1:
        raise ValueError("Could not find standalone CHAIN STATUS line")
    before = body[:idx+1]  # keep the newline before
    after = body[idx+1+len("CHAIN STATUS: [CLOSED / OPEN]\n"):]
    return before + C54_BLOCK + "\n" + after


def apply_c55(body):
    if C55_OLD not in body:
        raise ValueError("C55 target string not found")
    return body.replace(C55_OLD, C55_NEW, 1)


def apply_c56(body):
    if C56_BOTTLENECK_OLD not in body:
        raise ValueError("C56 Bottleneck target string not found")
    if C56_ROLE_OLD not in body:
        raise ValueError("C56 Role target string not found")
    body = body.replace(C56_BOTTLENECK_OLD, C56_BOTTLENECK_NEW, 1)
    body = body.replace(C56_ROLE_OLD, C56_ROLE_NEW, 1)
    return body


# ── variation builders ────────────────────────────────────────────────────────

def build_variation(number, axis_short, axis_long, hypothesis, body):
    header = f"""## V-{number:02d} -- Axis: {axis_long}

**Variation axis**: {axis_short}
**Hypothesis**: {hypothesis}

---

"""
    # body already ends with "---\n---\n"
    return header + body


def main():
    v01_body = read_v01()

    # ── V-02: C-54 only ───────────────────────────────────────────────────────
    v02_body = apply_c54(v01_body)
    v02 = build_variation(
        2,
        "Output format -- adds the DERIVATION CLAIM block immediately before the `CHAIN STATUS: [CLOSED / OPEN]` declaration. All other content is byte-for-byte identical to V-01. C-54 now passes; C-55 and C-56 still fail.",
        "Output Format (CHAIN STATUS Derivation Claim, C-54 Target)",
        "43/48 = 8.958 under v18. C-54 passes (explicit DERIVATION CLAIM block enumerates all four PRESENT directions with Violation Check evaluation results and derives CLOSED from the complete record). C-55 fails (Baseline->Phase Violation Check still lacks Return instruction cross-reference). C-56 fails (Bottleneck Ref and Role Ref hints still use abbreviated \"see architecture above\").",
        v02_body
    )

    # ── V-03: C-55 only ───────────────────────────────────────────────────────
    v03_body = apply_c55(v01_body)
    v03 = build_variation(
        3,
        "Lifecycle emphasis -- appends the Return instruction cross-reference sentence to the Baseline->Phase Violation Check cell in DIRECTION INVENTORY. All other content is byte-for-byte identical to V-01. C-55 now passes; C-54 and C-56 still fail.",
        "Lifecycle Emphasis (Phase->Baseline Violation Check Cross-Reference, C-55 Target)",
        "43/48 = 8.958 under v18. C-55 passes (Baseline->Phase Violation Check now explicitly cites `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY as the authoring mechanism that maintains consistency). C-54 fails (no DERIVATION CLAIM block). C-56 fails (two of three hints use abbreviated back-reference).",
        v03_body
    )

    # ── V-04: C-56 only ───────────────────────────────────────────────────────
    v04_body = apply_c56(v01_body)
    v04 = build_variation(
        4,
        "Phrasing register -- changes `Bottleneck Ref:` and `Role Ref:` hint suffix from \"see architecture above\" to \"see EXCEPTION BLOCK ARCHITECTURE above\". `IM Ref:` hint already had the full name (C-53 pass, unchanged). All other content is byte-for-byte identical to V-01. C-56 now passes; C-54 and C-55 still fail.",
        "Phrasing Register (All-Hints Architecture Back-Reference, C-56 Target)",
        "43/48 = 8.958 under v18. C-56 passes (all three citation hints -- Role Ref, Bottleneck Ref, IM Ref -- now carry explicit inline back-reference to \"EXCEPTION BLOCK ARCHITECTURE\" by full name). C-54 fails (no DERIVATION CLAIM block). C-55 fails (no Return instruction citation in Baseline->Phase Violation Check).",
        v04_body
    )

    # ── V-05: C-54 + C-55 + C-56 ─────────────────────────────────────────────
    v05_body = apply_c54(v01_body)
    v05_body = apply_c55(v05_body)
    v05_body = apply_c56(v05_body)
    v05 = build_variation(
        5,
        "Combination -- applies all three structural changes (C-54 DERIVATION CLAIM + C-55 Return instruction cross-reference + C-56 all-hints full-name back-reference) simultaneously. Everything else is byte-for-byte identical to V-01. All three new v18 criteria pass.",
        "Combination: Output Format + Lifecycle Emphasis + Phrasing Register (C-54 + C-55 + C-56)",
        "48/48 = 10.000 under v18. C-54 passes (DERIVATION CLAIM block present, enumerates all four PRESENT directions). C-55 passes (Baseline->Phase Violation Check cites `Return instruction:` in PHASE GATE CONTRACT SUMMARY). C-56 passes (all three EX block citation hints carry full \"EXCEPTION BLOCK ARCHITECTURE\" back-reference). All prior criteria through C-53 continue to pass unchanged.",
        v05_body
    )

    # ── append all four to the file ───────────────────────────────────────────
    with open(TARGET, "a", encoding="utf-8") as f:
        f.write(v02)
        f.write(v03)
        f.write(v04)
        f.write(v05)

    print("Done. Appended V-02 through V-05.")

    # ── quick sanity check ────────────────────────────────────────────────────
    with open(TARGET, "r", encoding="utf-8") as f:
        full = f.read()

    checks = [
        ("V-01 present", "V-01 -- Axis: Role Sequence" in full),
        ("V-02 present", "V-02 -- Axis: Output Format" in full),
        ("V-03 present", "V-03 -- Axis: Lifecycle Emphasis" in full),
        ("V-04 present", "V-04 -- Axis: Phrasing Register" in full),
        ("V-05 present", "V-05 -- Combination:" in full),
        ("V-02 has DERIVATION CLAIM", full.count("**DERIVATION CLAIM:**") >= 1),
        ("V-03 has Return instruction cross-ref", "Consistency maintained by `Return instruction:`" in full),
        ("V-04 has EXCEPTION BLOCK ARCHITECTURE in Bottleneck Ref hint", "Namespace: B-ID (see EXCEPTION BLOCK ARCHITECTURE above)." in full),
        ("V-04 has EXCEPTION BLOCK ARCHITECTURE in Role Ref hint", "Namespace: R-ID (see EXCEPTION BLOCK ARCHITECTURE above)." in full),
        ("V-05 has all three", full.count("**DERIVATION CLAIM:**") >= 2),
    ]

    all_pass = True
    for label, result in checks:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {label}")

    if all_pass:
        print("All sanity checks passed.")
    else:
        print("WARNING: some checks failed -- review output.")


if __name__ == "__main__":
    main()
