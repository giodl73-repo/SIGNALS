# Adoption Blocker Analysis: demo-videos

**Topic:** demo-videos
**Feature:** Automated demo video series showing Signal skills in action, targeting Microsoft Principal PMs
**Date:** 2026-04-03
**Depth:** standard
**Spec:** docs/superpowers/specs/2026-04-03-demo-video-pipeline-design.md

---

## Question

What would BLOCK adoption of this demo video series? What prevents a Principal PM from watching, installing Signal, and using it for real work?

---

## Blocker Categories

**Organizational blockers** -- policy, process, approval chains, change management
**Technical blockers** -- integration gaps, skill gaps, infrastructure requirements
**Behavioral blockers** -- habit lock-in, workflow disruption, learning curve, trust

---

## Blocker Registry

| ID | Blocker | Category | Severity | Affected Personas | Root Cause | Mitigation |
|----|---------|----------|----------|------------------|------------|------------|
| B-01 | No Claude Code license or access | Technical | P1 | All PMs | Signal requires Claude Code which requires Anthropic subscription; Microsoft employees may not have approval to use non-Microsoft AI tools | Provide install path that works with approved tooling; document the procurement/approval steps explicitly; explore Azure-hosted Claude option |
| B-02 | Videos show terminal CLI -- PMs do not live in terminals | Behavioral | P1 | Principal PMs, Partner PMs, VPs | Target audience works in PowerPoint, Teams, Outlook, Word, and browser. Terminal-first UX signals "this is for developers, not me" | Open Demo 0 with a familiar context (Teams message, email link) before transitioning to terminal; add callout text explaining this is a PM tool that happens to run in terminal |
| B-03 | 5-7 minute videos are too long for exec attention | Behavioral | P1 | VPs, Partner PMs | Senior leaders triage by scanning, not watching. A 7-minute video competes with 30-second TikTok attention habits and packed calendars | Produce 60-second highlight cuts for each demo; lead with the "money moment" in the first 15 seconds; make the 5-7 min version the "full walkthrough" linked from the short version |
| B-04 | ElevenLabs API key in config.env is a secret management risk | Technical | P2 | Pipeline maintainers | config.env holds ElevenLabs API key; if committed to git or shared repo, key leaks; if not committed, new contributors cannot render | Add config.env to .gitignore; document key setup in CONTRIBUTING.md; consider Azure AI Speech as zero-config-for-MSFT alternative |
| B-05 | VHS tape files execute real commands against real services | Technical | P2 | Pipeline maintainers, demo authors | Tape files run `/discover-hypothesis`, `/discover-competitors` etc. which call Claude API. Each render costs API tokens, takes minutes, and produces non-deterministic output | Pre-record terminal sessions or use VHS replay mode; cache API responses for deterministic renders; separate "live capture" from "render" steps |
| B-06 | OneDrive link sharing requires Microsoft tenant access | Organizational | P2 | External collaborators, open-source contributors | Videos shared as OneDrive links are inaccessible to anyone outside the Microsoft tenant or without guest access | Host videos on YouTube (unlisted) or GitHub Releases in parallel; OneDrive for internal, public URL for external |
| B-07 | No clear call-to-action after watching | Behavioral | P2 | All PMs | PM watches video, is impressed, then has no frictionless next step. The gap between "watched a video" and "installed and ran first skill" is where most adoption dies | End every video with a 10-second CTA screen: exact URL, exact command, expected time to first result (90 seconds per Demo 0) |
| B-08 | PM cannot tell if output is real or staged | Behavioral | P2 | Skeptical PMs, Partner PMs | "Authentic output" is a design principle but viewer has no way to verify. Polished narration + perfect flow looks rehearsed, triggering "too good to be true" skepticism | Show real timestamps, real errors that get corrected, real thinking time. Include one moment per demo where the PM pushes back and the tool adjusts. Imperfection builds trust |
| B-09 | Signal requires MSYS2/Git Bash on Windows | Technical | P2 | PMs on locked-down corp machines | Many Microsoft PMs run corporate Windows with restricted admin rights; installing MSYS2 or Git Bash may require IT ticket and 1-2 week wait | Document WSL path as alternative; test with default Windows Terminal + Git for Windows (already standard on MSFT machines); minimize exotic dependencies |
| B-10 | No manager or skip-level endorsement | Organizational | P2 | All PMs | Individual PMs rarely adopt workflow tools without signal from leadership that it is endorsed or at least tolerated. "Random GitHub tool" does not clear the bar | Secure one VP-level quote or testimonial; show the tool in a real ROB or shiproom context; route Demo 0 through a known leader's distribution list |
| B-11 | Videos do not address the inertia question | Behavioral | P2 | Pragmatic PMs | Signal's own philosophy says inertia is competitor zero, but the demos do not show what the PM is doing TODAY for the same task and why that is worse | Add a "before" segment (15-30s) to each demo: "Here is how this decision gets made today: 3 meetings, 2 weeks, one opinion. Here is the alternative." |
| B-12 | AI voiceover sounds robotic or uncanny | Behavioral | P3 | All viewers | ElevenLabs quality varies by voice selection and text style. Uncanny narration undermines the "professional" positioning and makes viewers click away | A/B test 3 voice options with 5 internal viewers before committing; use conversational phrasing, not script-reading cadence; allow Azure AI Speech as fallback |
| B-13 | Demo topics may not resonate with viewer's domain | Behavioral | P3 | PMs outside the demo's feature area | If demos use an API-copilot example and the viewer works on Teams or Office, they mentally translate rather than see themselves | Use a horizontal feature topic that every PM recognizes (e.g., "should we add dark mode" or "should we ship this accessibility feature") rather than a niche API scenario |
| B-14 | No subtitle/accessibility support out of the box | Organizational | P3 | Accessibility-conscious PMs, hearing-impaired viewers | The spec mentions .srt generation but does not confirm subtitles are burned in or sidecar; Microsoft accessibility standards are strict | Burn in subtitles by default (not sidecar-only); verify color contrast meets WCAG AA against terminal background; test with screen reader metadata |
| B-15 | Render pipeline requires Go, FFmpeg, curl, jq | Technical | P3 | Contributors who want to modify demos | Four separate tool installs (VHS via Go, FFmpeg, curl, jq) creates a "yak shaving" barrier for anyone who wants to tweak a demo | Provide a Dockerfile or devcontainer.json that has all deps; or a one-line `choco install` script; keep contributor path separate from viewer path |
| B-16 | No analytics on video engagement | Organizational | P3 | Demo pipeline team | OneDrive does not provide view counts, drop-off points, or engagement data. Without metrics, you cannot iterate on what works | Host on a platform with analytics (YouTube unlisted, Loom, or Vidyard); or add aka.ms redirect links that track click-through |
| B-17 | Speed-ramped terminal output may be unreadable | Behavioral | P3 | All viewers | 2-4x speed during AI generation means text scrolls faster than anyone can read. Viewers who want to follow the actual output feel lost | Add overlay text summarizing what is happening during sped-up sections ("Generating competitive analysis -- 12 competitors found"); pause on key output frames for 3-5 seconds |

---

## Kill Blocker

- **Blocker:** B-02 -- Videos show terminal CLI; PMs do not live in terminals
- **Why fatal:** The target audience is Microsoft Principal PMs whose daily tools are PowerPoint, Teams, Word, and Outlook. A terminal-only demo triggers immediate pattern matching: "developer tool, not for me." This single visual cue causes the majority of the target audience to self-select out within the first 10 seconds, before any content lands. It does not matter how good the narration is or how powerful the skills are -- if the viewer categorizes the tool as "not for people like me," they close the tab. The install video (Demo 0) compounds this: it opens in a terminal and never leaves.
- **Resolution:** Demo 0 must open in a context the PM recognizes -- a Teams message, an email, a calendar invite for a "feature review" meeting. Transition to terminal with explicit framing: "This runs in your terminal, but you are doing PM work -- investigation, decision, validation." Use the narration to continuously anchor the viewer in PM language, not developer language. Consider overlay UI that shows the PM workflow (investigate > decide > validate) as a visual layer on top of the terminal.

---

## Mitigation Plan

Ordered by severity:

1. **[B-01]** -- owner: Platform team -- deadline: Before Demo 0 ships -- success metric: A documented, tested install path that works on a standard Microsoft corporate Windows machine without IT ticket, confirmed by 3 PMs outside the team
2. **[B-02]** -- owner: Demo authors -- deadline: Demo 0 script finalization -- success metric: 5 of 5 PM test viewers correctly identify the tool as "for PMs" after watching Demo 0, measured by one-question survey
3. **[B-03]** -- owner: Demo authors -- deadline: Before distribution -- success metric: 60-second highlight cut exists for every demo; average watch-through rate on highlight cuts exceeds 70%
4. **[B-05]** -- owner: Pipeline team -- deadline: Pipeline v1 -- success metric: Render produces identical output on two consecutive runs (deterministic); render cost per demo under $0.50
5. **[B-07]** -- owner: Demo authors -- deadline: Each demo final cut -- success metric: Every video ends with CTA; link-to-install conversion rate tracked and exceeds 10%
6. **[B-08]** -- owner: Demo authors -- deadline: Demo 1-5 script review -- success metric: Each demo contains at least one visible correction/pushback moment; 3 of 5 test viewers say "this looks real" unprompted
7. **[B-09]** -- owner: Platform team -- deadline: Before Demo 0 ships -- success metric: Install tested on 3 corporate-locked Windows machines; zero IT tickets required
8. **[B-10]** -- owner: Adoption lead -- deadline: 30 days post-launch -- success metric: One VP-level endorsement or forward; Demo 0 shared by at least one leader with 50+ report chain
9. **[B-11]** -- owner: Demo authors -- deadline: Demo 1-5 script finalization -- success metric: Every demo opens with a "before" segment; test viewers can articulate the time savings after watching
10. **[B-04]** -- owner: Pipeline team -- deadline: Pipeline v1 -- success metric: config.env in .gitignore; setup docs pass "fresh machine" test
11. **[B-06]** -- owner: Distribution lead -- deadline: Before external sharing -- success metric: Videos accessible via public URL with no Microsoft login
12. **[B-12]** -- owner: Demo authors -- deadline: Before first narration recording -- success metric: Voice selection validated by 5 internal listeners; no "robotic" feedback
13. **[B-13]** -- owner: Demo authors -- deadline: Topic selection phase -- success metric: Demo topic recognized as relevant by 4 of 5 PMs from different product areas
14. **[B-14]** -- owner: Pipeline team -- deadline: Pipeline v1 -- success metric: Burned-in subtitles pass WCAG AA contrast; tested with one accessibility reviewer
15. **[B-15]** -- owner: Pipeline team -- deadline: Pipeline v1 -- success metric: Dockerfile or devcontainer.json tested; new contributor renders a demo in under 10 minutes
16. **[B-16]** -- owner: Distribution lead -- deadline: 30 days post-launch -- success metric: View count and drop-off data available for every video
17. **[B-17]** -- owner: Demo authors -- deadline: Each demo final cut -- success metric: Overlay summaries present during every speed-ramped section; test viewers report they can follow the flow

---

## Summary

17 blockers identified across 3 categories: 3 P1 (must resolve before launch), 8 P2 (address in first 30 days), 6 P3 (60-90 day roadmap).

The kill blocker is the terminal-first visual framing (B-02). Principal PMs self-select out of developer-looking tools within seconds. The mitigation is not to hide the terminal but to frame it explicitly as a PM workspace from the first frame of every video.

The three P1 blockers form a chain: the viewer must (1) recognize the tool as "for PMs" (B-02), (2) watch long enough to see value (B-03), and (3) be able to actually install it on their machine (B-01). If any link breaks, the entire funnel collapses.
