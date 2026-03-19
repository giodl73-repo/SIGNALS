#!/usr/bin/env python
"""
quest-run.py -- Find the golden prompt for every Signal skill.

Runs the quest loop in parallel across all skills:
  trace artifacts -> rubric -> variate -> score -> converge -> golden prompt

Each skill writes independently to simulations/quest/golden/{skill}-golden-{date}.md
A final merge pass updates signal.skills.yaml with all golden prompts.

Usage:
    python quest-run.py                          # all skills without a golden
    python quest-run.py --skill scout-competitors # single skill
    python quest-run.py --namespace scout        # all skills in a namespace
    python quest-run.py --dry-run                # show what would run, don't run
    python quest-run.py --max-workers 4          # limit parallelism (default: 8)
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import date
from pathlib import Path
from typing import Optional

import anthropic
import yaml

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent
SKILLS_YAML = REPO_ROOT / "signal.skills.yaml"
QUEST_DIR = REPO_ROOT / "simulations" / "quest"
TRACE_DIR = REPO_ROOT / "simulations" / "trace" / "skill"
SPEC_DIR = REPO_ROOT / "simulations" / "draft" / "specs"
TODAY = date.today().isoformat()

MODEL = "claude-opus-4-6"
MAX_ROUNDS = 5                    # circuit breaker -- never loop forever
CONVERGENCE_PLATEAU_ROUNDS = 2   # rounds with no new patterns = quest plateaued

# ── Anthropic client ──────────────────────────────────────────────────────────

client = anthropic.AsyncAnthropic()

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_skills() -> list[dict]:
    """Load all skill definitions from signal.skills.yaml."""
    with open(SKILLS_YAML) as f:
        data = yaml.safe_load(f)
    return data.get("skills", [])


def save_skills(skills: list[dict]) -> None:
    """Write skills back to signal.skills.yaml."""
    with open(SKILLS_YAML) as f:
        data = yaml.safe_load(f)
    data["skills"] = skills
    with open(SKILLS_YAML, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def find_trace_artifacts(skill_id: str) -> list[Path]:
    """Find all trace artifacts for a skill."""
    namespace = skill_id.split("-")[0]
    skill_name = skill_id.split("-", 1)[1] if "-" in skill_id else skill_id
    # Search both the trace/skill dir and namespace-specific trace dirs
    patterns = [
        f"*-{skill_name}-*.md",
        f"*-{skill_id}-*.md",
        f"plugin-{skill_id}-*.md",
        f"plugin-{skill_name}-*.md",
    ]
    found = []
    for pattern in patterns:
        found.extend(TRACE_DIR.glob(pattern))
    return list(set(found))


def find_spec_content(skill_id: str) -> Optional[str]:
    """Load the spec content for a skill."""
    namespace = skill_id.split("-")[0]
    spec_file = SPEC_DIR / f"signal-{namespace}-{TODAY}.md"
    # Also check yesterday's date in case session spans midnight
    if not spec_file.exists():
        for f in SPEC_DIR.glob(f"signal-{namespace}-*.md"):
            spec_file = f
            break
    if spec_file.exists():
        return spec_file.read_text()
    return None


def golden_path(skill_id: str) -> Path:
    """Return the path where the golden prompt should be written."""
    return QUEST_DIR / "golden" / f"{skill_id}-golden-{TODAY}.md"


def rubric_path(skill_id: str, version: int = 1) -> Path:
    """Return the rubric path for a skill."""
    suffix = f"-v{version}" if version > 1 else ""
    return QUEST_DIR / "rubrics" / f"{skill_id}-rubric{suffix}-{TODAY}.md"


def scorecard_path(skill_id: str, round_num: int) -> Path:
    """Return the scorecard path for a skill/round."""
    return QUEST_DIR / "scorecards" / f"{skill_id}-scorecard-R{round_num}-{TODAY}.md"


def variations_path(skill_id: str, round_num: int) -> Path:
    """Return the variations path for a skill/round."""
    return QUEST_DIR / "variations" / f"{skill_id}-variations-R{round_num}-{TODAY}.md"


async def call_claude(system: str, user: str, max_tokens: int = 4096) -> str:
    """Single Claude API call with adaptive thinking."""
    response = await client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        thinking={"type": "adaptive"},
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return next(
        (b.text for b in response.content if b.type == "text"),
        ""
    )


# ── Quest loop steps ──────────────────────────────────────────────────────────

async def run_rubric(skill: dict, trace_content: str) -> str:
    """Generate initial rubric for a skill."""
    system = """You are running /quest:rubric. Define what good output looks like
for a Signal skill. Produce a scoring rubric with ranked criteria (C-01, C-02...)
each with: text, weight (essential/recommended/aspirational), category
(correctness/depth/format/coverage/behavior), and a clear pass condition.

Start with 3-5 essential criteria. These must ALL pass for the output to be useful.
Add 2-3 recommended criteria (output is better with these).
Add 1-2 aspirational criteria (raise the bar once essential/recommended are stable).

Output the rubric as a Markdown document with standard frontmatter."""

    user = f"""Skill: {skill['id']}
Namespace: {skill['namespace']}
Description: {skill['description']}

Trace artifact (hand-compiled expected output -- this is the ground truth):
{trace_content[:3000] if trace_content else 'No trace artifact found -- generate criteria from the skill description.'}

Generate the initial rubric for this skill."""

    content = await call_claude(system, user)
    path = rubric_path(skill["id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return content


async def run_variate(skill: dict, rubric_content: str, round_num: int,
                       prior_findings: str = "") -> str:
    """Generate N prompt variations for a skill."""
    system = """You are running /quest:variate. Generate 5 distinct prompt variations
of a skill body. Each variation is a COMPLETE, RUNNABLE skill body -- not a diff.
Test different axes: role sequence, output format, lifecycle emphasis, phrasing register.
Single-axis variation first, combinations later.

Label each variation V-01 through V-05 with its axis and hypothesis.
Output as a Markdown document."""

    user = f"""Skill: {skill['id']}
Round: {round_num}
Description: {skill['description']}

Rubric (what good output looks like):
{rubric_content[:2000]}

{'Prior round findings (target these gaps):' if prior_findings else ''}
{prior_findings[:1000] if prior_findings else ''}

Generate 5 prompt variations for this skill."""

    content = await call_claude(system, user)
    path = variations_path(skill["id"], round_num)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return content


async def run_score(skill: dict, variations: str, rubric: str,
                     round_num: int, trace_content: str) -> tuple[str, int, list[str], bool]:
    """Score variations against rubric. Returns (content, top_score, excellence_signals, converged)."""
    system = """You are running /quest:score. Score N skill body variations against a rubric.

For each variation (V-01 through V-05):
- Evaluate each rubric criterion: PASS / PARTIAL / FAIL with evidence
- Compute composite score: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
- Identify excellence signals: what did the top-scoring variation do that others didn't?

Output:
1. Per-variation scoring table
2. Leaderboard (ranked by composite score)
3. Excellence signals (ES-01, ES-02...) -- patterns from top outputs
4. Failure patterns -- criteria that fail in ALL variations (skill design issue vs. rubric issue)
5. CONVERGENCE CHECK: Did all essential criteria pass in V-01 through V-05? YES/NO
6. NEW PATTERNS FOUND: Are there excellence signals worth adding to the rubric? YES/NO

End with a JSON block like this (exactly):
```json
{"top_score": 85, "all_essential_pass": true, "new_patterns": ["pattern 1", "pattern 2"]}
```
If no new patterns, use: `{"top_score": 85, "all_essential_pass": true, "new_patterns": []}`"""

    user = f"""Skill: {skill['id']}
Round: {round_num}

Rubric:
{rubric[:2000]}

Variations to score:
{variations[:3000]}

Trace artifact (ground truth):
{trace_content[:1000] if trace_content else 'Not available.'}

Score all variations and check for dual convergence."""

    content = await call_claude(system, user, max_tokens=6000)

    # Parse the JSON block from the response
    top_score = 0
    excellence_signals = []
    all_essential_pass = False
    try:
        import re
        json_match = re.search(r'```json\s*({[^`]+})\s*```', content, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group(1))
            top_score = parsed.get("top_score", 0)
            all_essential_pass = parsed.get("all_essential_pass", False)
            excellence_signals = parsed.get("new_patterns", [])
    except Exception:
        pass

    converged = all_essential_pass and len(excellence_signals) == 0

    path = scorecard_path(skill["id"], round_num)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return content, top_score, excellence_signals, converged


async def evolve_rubric(skill: dict, rubric: str, excellence_signals: list[str],
                         version: int) -> str:
    """Update rubric with new excellence patterns."""
    system = """You are updating a quest rubric based on excellence signals found in scoring.
Each excellence signal is a pattern that made a high-scoring output better.
Convert each pattern into a new rubric criterion (C-NN) with weight 'aspirational'.
Bump the rubric version number. Output the complete updated rubric."""

    user = f"""Skill: {skill['id']}
Current rubric (v{version - 1}):
{rubric[:2000]}

New excellence patterns to add as criteria:
{chr(10).join(f'- {s}' for s in excellence_signals)}

Generate the updated rubric (v{version})."""

    content = await call_claude(system, user)
    path = rubric_path(skill["id"], version)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return content


async def write_golden(skill: dict, variations: str, rubric: str,
                        scorecard: str, rounds: int, top_score: int) -> str:
    """Extract and write the golden prompt."""
    system = """You are finalizing a quest run. Extract the golden prompt -- the
variation that achieved dual convergence (highest score, all essential criteria pass,
no new excellence patterns).

Write the golden prompt document with:
1. Frontmatter (skill, topic, date, rounds, rubric_final, score, status: GOLDEN)
2. The exact prompt body of the winning variation
3. 'What made it golden' -- the key patterns that distinguish it from the baseline
4. Final rubric summary

This document will be read by craft generate to bake the prompt into the SKILL.md."""

    user = f"""Skill: {skill['id']}
Rounds: {rounds}
Top score: {top_score}

Final scorecard:
{scorecard[:2000]}

Variations (find the winner):
{variations[:2000]}

Final rubric:
{rubric[:1500]}

Write the golden prompt document."""

    content = await call_claude(system, user, max_tokens=4096)
    path = golden_path(skill["id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return content


# ── Main quest loop per skill ─────────────────────────────────────────────────

async def quest_skill(skill: dict, semaphore: asyncio.Semaphore) -> dict:
    """Run the full quest loop for one skill. Returns updated skill dict."""
    async with semaphore:
        skill_id = skill["id"]
        print(f"[{skill_id}] Starting quest loop")

        # Step 1: find trace artifacts
        trace_files = find_trace_artifacts(skill_id)
        trace_content = ""
        if trace_files:
            trace_content = trace_files[0].read_text()
            print(f"[{skill_id}] Found trace: {trace_files[0].name}")
        else:
            print(f"[{skill_id}] No trace artifact -- will generate rubric from spec")

        # Step 2: generate initial rubric
        try:
            rubric = await run_rubric(skill, trace_content)
            print(f"[{skill_id}] Rubric generated (v1)")
        except Exception as e:
            print(f"[{skill_id}] FAILED rubric: {e}")
            return skill

        # Step 3: quest loop
        rubric_version = 1
        plateau_count = 0
        last_scorecard = ""
        last_variations = ""
        last_score = 0
        prior_findings = ""

        for round_num in range(1, MAX_ROUNDS + 1):
            print(f"[{skill_id}] Round {round_num}")

            try:
                # Generate variations
                variations = await run_variate(skill, rubric, round_num, prior_findings)

                # Score variations
                scorecard, top_score, excellence_signals, converged = await run_score(
                    skill, variations, rubric, round_num, trace_content
                )

                last_scorecard = scorecard
                last_variations = variations
                last_score = top_score
                prior_findings = "\n".join(
                    f"- {s}" for s in excellence_signals
                ) if excellence_signals else ""

                print(f"[{skill_id}] R{round_num}: score={top_score}, "
                      f"signals={len(excellence_signals)}, converged={converged}")

                if converged:
                    plateau_count += 1
                    if plateau_count >= CONVERGENCE_PLATEAU_ROUNDS:
                        print(f"[{skill_id}] DUAL CONVERGENCE at round {round_num}")
                        break
                else:
                    plateau_count = 0
                    if excellence_signals:
                        # Evolve rubric with new patterns
                        rubric_version += 1
                        rubric = await evolve_rubric(
                            skill, rubric, excellence_signals, rubric_version
                        )
                        print(f"[{skill_id}] Rubric evolved to v{rubric_version}")

            except Exception as e:
                print(f"[{skill_id}] FAILED round {round_num}: {e}")
                break

        # Step 4: write golden prompt
        try:
            golden = await write_golden(
                skill, last_variations, rubric, last_scorecard,
                round_num, last_score
            )
            golden_file = golden_path(skill_id)
            skill["golden"] = str(golden_file.relative_to(REPO_ROOT)).replace("\\", "/")
            skill["rubric"] = str(rubric_path(skill_id, rubric_version).relative_to(REPO_ROOT)).replace("\\", "/")
            skill["quest_status"] = f"GOLDEN (Round {round_num}, score {last_score})"
            print(f"[{skill_id}] Golden prompt written: {golden_file.name}")
        except Exception as e:
            print(f"[{skill_id}] FAILED writing golden: {e}")

        return skill


# ── Entry point ───────────────────────────────────────────────────────────────

async def main():
    parser = argparse.ArgumentParser(description="Find golden prompts for Signal skills")
    parser.add_argument("--skill", help="Run for a single skill ID")
    parser.add_argument("--namespace", help="Run for all skills in a namespace")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would run without running")
    parser.add_argument("--max-workers", type=int, default=8,
                        help="Max parallel workers (default: 8)")
    parser.add_argument("--force", action="store_true",
                        help="Re-run even if golden already exists")
    args = parser.parse_args()

    # Ensure quest output dirs exist
    for subdir in ["golden", "rubrics", "scorecards", "variations", "reports"]:
        (QUEST_DIR / subdir).mkdir(parents=True, exist_ok=True)

    # Load skills
    skills = load_skills()

    # Filter to target skills
    target = []
    for skill in skills:
        if skill.get("namespace") == "meta":
            continue  # skip internal meta-skills
        if args.skill and skill["id"] != args.skill:
            continue
        if args.namespace and skill["namespace"] != args.namespace:
            continue
        if not args.force and skill.get("quest_status", "").startswith("GOLDEN"):
            print(f"[{skill['id']}] Already golden -- skipping (use --force to re-run)")
            continue
        target.append(skill)

    if not target:
        print("No skills to process.")
        return

    print(f"\nSkills to process: {len(target)}")
    for s in target:
        print(f"  {s['id']} ({s['namespace']})")

    if args.dry_run:
        print("\n[dry-run] Would run the quest loop for the above skills.")
        return

    # Run in parallel
    semaphore = asyncio.Semaphore(args.max_workers)
    tasks = [quest_skill(skill, semaphore) for skill in target]
    updated_skills = await asyncio.gather(*tasks, return_exceptions=False)

    # Merge results back into the full skills list
    updated_map = {s["id"]: s for s in updated_skills if isinstance(s, dict)}
    final_skills = []
    for skill in skills:
        if skill["id"] in updated_map:
            final_skills.append(updated_map[skill["id"]])
        else:
            final_skills.append(skill)

    # Save updated signal.skills.yaml
    save_skills(final_skills)

    # Summary
    golden_count = sum(1 for s in updated_skills
                       if isinstance(s, dict) and s.get("quest_status", "").startswith("GOLDEN"))
    print(f"\nDone. {golden_count}/{len(target)} skills reached dual convergence.")
    print(f"Results in: {QUEST_DIR}")
    print(f"signal.skills.yaml updated with golden prompt paths.")
    print(f"\nNext step: python quest-run.py | craft generate --stage program")


if __name__ == "__main__":
    asyncio.run(main())
