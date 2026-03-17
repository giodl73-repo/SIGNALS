---
supplement_for: typesetter
framework: beamer
---

# Wave Manager - Beamer Presentation Patterns

**Last Updated**: 2026-01-29
**Technology**: Beamer (LaTeX presentations)

---

## Overview

Patterns and best practices for creating professional Beamer presentations. Covers slide structure, content density, table formatting, visual design, and common anti-patterns.

---

## Technology Stack

- **Presentation Class**: Beamer (LaTeX)
- **Packages**: booktabs, colortbl, array, tikz, listings
- **Graphics**: TikZ for diagrams
- **Themes**: Customized default theme with color overrides
- **Aspect Ratio**: 4:3 (default) or 16:9

---

## Document Structure

```
sources/wave-system-presentation/
├── main.tex                 # Main presentation file
├── slides/                  # Individual slide files
│   ├── 01-title.tex
│   ├── 02-what-is-wave-system.tex
│   ├── 03-wave-lifecycle.tex
│   └── ...
└── ../common/               # Shared definitions
    ├── colors.tex
    └── macros.tex
```

---

## Slide Structure Patterns

### Basic Frame Structure

```latex
\begin{frame}{Slide Title}

% Content goes here
% Use vertical spacing: \vspace{0.3cm}
% Keep it focused on ONE concept

\end{frame}
```

### Frame with Blocks

```latex
\begin{frame}{Concept Name}

\begin{block}{Definition}
A \emph{concise definition} of the concept in one or two sentences.
\end{block}

\vspace{0.5cm}

% Additional content below

\end{frame}
```

### Multi-Frame Pattern

For related content, use multiple sequential frames:

```latex
\begin{frame}{Topic: Part 1}
% First aspect
\end{frame}

\begin{frame}{Topic: Part 2}
% Second aspect
\end{frame}
```

**Rule**: One topic per slide. If explaining multiple aspects, use multiple slides.

---

## Content Density Rules

### The 3-5 Rule for Bullets

✅ **Good: 3-5 items maximum**

```latex
\begin{itemize}
    \item First key point
    \item Second key point
    \item Third key point
\end{itemize}
```

❌ **Bad: 7+ items (text wall)**

```latex
\begin{itemize}
    \item Point 1
    \item Point 2
    \item Point 3
    \item Point 4
    \item Point 5
    \item Point 6
    \item Point 7  % Audience loses focus
    \item Point 8  % Definitely too many
\end{itemize}
```

### The 6-Word Rule

Keep bullet points concise (ideally 6 words or fewer):

```latex
% GOOD - Concise, scannable
\item Role-based parallel execution

% BAD - Full sentence
\item The Wave System enables role-based parallel execution of enhancements across multiple specialized agents
```

### Vertical Spacing

Use consistent spacing between content blocks:

```latex
\vspace{0.3cm}  % Small gap (between related items)
\vspace{0.5cm}  % Medium gap (between sections)
```

---

## Table Formatting for Slides

### Font Sizing for Tables

Always specify font size for tables (less horizontal space than documents):

```latex
\small  % Most common for slides
\begin{tabular}{lp{7.5cm}}
...
\end{tabular}

% Or for denser content:
\footnotesize
\begin{tabular}{lp{2cm}p{2cm}p{2cm}}
...
\end{tabular}
```

### Two-Column Tables (Most Common)

```latex
\small
\noindent
\begin{tabular}{lp{7.5cm}}
\toprule
\textbf{Feature} & \textbf{Description} \\
\midrule
\rowcolor{msgray!8}
Role-Based & Specialists work in parallel \\
Multi-Agent & Expert feedback before implementation \\
\rowcolor{msgray!8}
Automated & Skills manage workflow \\
\bottomrule
\end{tabular}
```

**Pattern**: Left column = label (narrow), right column = description (wide with p{width})

### Multi-Column Tables

For metric comparisons, use 3-4 columns max:

```latex
\footnotesize
\begin{tabular}{lp{2cm}p{2cm}p{2.5cm}}
\toprule
\textbf{Metric} & \textbf{Baseline} & \textbf{Target} & \textbf{Actual} \\
\midrule
App switching & 10-30s & <5s & \improvement{2s} \checkmark \\
Landing page & App Manager & Portal & \improvement{Portal} \checkmark \\
\bottomrule
\end{tabular}
```

**Note**: Use `\noindent` before tables to align with left margin.

### Table Column Width Guidelines

For standard 4:3 slides:
- 2 columns: `{lp{7.5cm}}` or `{lp{8cm}}`
- 3 columns: `{lp{3cm}p{3cm}p{3cm}}`
- 4 columns: `{lp{2cm}p{2cm}p{2cm}p{2cm}}`

**Rule**: Total width should not exceed ~10.5cm for 4:3, ~13cm for 16:9.

---

## Visual Design Patterns

### Color Theme Setup

```latex
% In preamble
\input{../common/colors}

\setbeamercolor{structure}{fg=primaryblue}
\setbeamercolor{frametitle}{bg=primaryblue,fg=white}
\setbeamercolor{title}{fg=primaryblue}
\setbeamercolor{block title}{bg=primaryblue,fg=white}
\setbeamercolor{block body}{bg=lightgray}
\setbeamercolor{alerted text}{fg=warningorange}
```

### Emphasis and Highlighting

```latex
% Custom commands (from wave-system-presentation)
\renewcommand{\emph}[1]{{\color{primaryblue}\textbf{#1}}}

% In content:
A \emph{structured development framework} that organizes projects.

% For improvements/success:
\newcommand{\improvement}[1]{{\color{successgreen}#1}}

\improvement{93\% improvement} in app switching time
```

### Alert Text

```latex
% For warnings or important notes
\alert{Critical requirement}

% Or use alertblock
\begin{alertblock}{What Could Improve}
\begin{itemize}
    \item Item requiring attention
\end{itemize}
\end{alertblock}
```

### Block Environments

Three types of blocks:

```latex
% Standard block (blue)
\begin{block}{What Went Well}
\begin{itemize}
    \item Positive outcome
\end{itemize}
\end{block}

% Alert block (orange/red)
\begin{alertblock}{What Could Improve}
\begin{itemize}
    \item Area needing attention
\end{itemize}
\end{alertblock}

% Example block (green) - if theme supports
\begin{exampleblock}{Example}
\begin{itemize}
    \item Concrete example
\end{itemize}
\end{exampleblock}
```

---

## Code Listings on Slides

### Basic Code Block

```latex
\begin{frame}[fragile]{Code Example}  % Note: [fragile] required!

\begin{lstlisting}[language=Python]
def calculate_efficiency(wave):
    return wave.score / 300
\end{lstlisting}

\end{frame}
```

**Critical**: Always use `[fragile]` frame option for code listings.

### Inline Code

```latex
The \texttt{/start-wave} skill initializes planning.
```

---

## Section Organization

### Section Dividers

```latex
% In main.tex
\section{Introduction}
\input{slides/02-what-is-wave-system}

\section{Skills and Tools}
\input{slides/04-skills-overview}
```

**Benefit**: Creates automatic navigation/outline in PDF.

### Title Slide Pattern

```latex
% slides/01-title.tex
\begin{frame}
\titlepage
\end{frame}
```

### Q&A Slide

```latex
\begin{frame}{Questions?}

\begin{center}
\Huge
Thank you!

\vspace{1cm}

\Large
Questions \& Discussion
\end{center}

\end{frame}
```

---

## Beamer-Specific Features

### Incremental Reveals

```latex
\begin{frame}{Progressive Disclosure}

First point shown immediately.

\pause

Second point appears on click.

\pause

Third point appears on another click.

\end{frame}
```

**Caution**: Use `\pause` sparingly. Too many clicks frustrate audiences.

### Frame Options

```latex
% For code or verbatim content
\begin{frame}[fragile]{Code Example}
...
\end{frame}

% Allow frame to break across slides (avoid if possible)
\begin{frame}[allowframebreaks]{Long Content}
...
\end{frame}

% Plain frame (no header/footer)
\begin{frame}[plain]
...
\end{frame}
```

---

## Anti-Patterns to Avoid

❌ **Don't create text walls**
- More than 5 bullets = too many
- Full sentences in bullets = audience reads instead of listening

❌ **Don't use tiny fonts**
```latex
% BAD
\tiny  % Unreadable from >5 feet
```

❌ **Don't overflow slide boundaries**
- Content extending beyond visible area
- Tables wider than slide width

❌ **Don't use complex animations**
- Multiple `\pause` commands per slide
- Fancy transitions (distracting)

❌ **Don't put full paragraphs on slides**
```latex
% BAD
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam...

% GOOD
\begin{itemize}
    \item Key point 1
    \item Key point 2
    \item Key point 3
\end{itemize}
```

❌ **Don't use tables for simple lists**
```latex
% BAD - Overkill
\begin{tabular}{ll}
Feature 1 & Description \\
Feature 2 & Description \\
\end{tabular}

% GOOD - Use itemize
\begin{itemize}
    \item Feature 1: Description
    \item Feature 2: Description
\end{itemize}
```

❌ **Don't forget font sizing on tables**
```latex
% BAD - Default font too large
\begin{tabular}{lll}

% GOOD - Appropriately sized
\small
\begin{tabular}{lll}
```

❌ **Don't use \noindent with tables in Beamer frames**
```latex
% BAD - Causes LaTeX errors in Beamer
\noindent
\begin{tabular}{lp{7cm}}

% GOOD - Beamer doesn't indent tables by default
\begin{tabular}{lp{7cm}}
```

**Note**: Unlike article class, Beamer frames don't indent tables. The `\noindent` command is unnecessary and can cause alignment errors.

---

## Custom Commands Pattern

Define reusable commands in preamble:

```latex
% Skills
\newcommand{\skill}[1]{\texttt{/#1}}

% Usage:
The \skill{start-wave} command initializes planning.

% Metrics
\newcommand{\metric}[3]{%
  \textbf{#1:} #2 \textrightarrow{} #3%
}

% Usage:
\metric{Timeline}{24 days}{12 days}

% Status
\newcommand{\improvement}[1]{%
  {\color{successgreen}#1}%
}

% Usage:
Efficiency: \improvement{271/300}
```

---

## Preamble Setup Pattern

```latex
\documentclass{beamer}

% ============================================================================
% Theme
% ============================================================================
\usetheme{default}
\usecolortheme{default}

% ============================================================================
% Packages
% ============================================================================
\usepackage{graphicx}
\usepackage{array}
\usepackage{booktabs}
\usepackage{colortbl}
\usepackage{tikz}

% Booktabs configuration to prevent overfull warnings
\setlength{\aboverulesep}{0pt}
\setlength{\belowrulesep}{0pt}

% Include common colors
\input{../common/colors}

% ============================================================================
% Color Theme Setup
% ============================================================================
\setbeamercolor{structure}{fg=primaryblue}
\setbeamercolor{frametitle}{bg=primaryblue,fg=white}
\setbeamercolor{title}{fg=primaryblue}

% ============================================================================
% Custom Commands
% ============================================================================
\renewcommand{\emph}[1]{{\color{primaryblue}\textbf{#1}}}
\newcommand{\improvement}[1]{{\color{successgreen}#1}}
\newcommand{\skill}[1]{\texttt{/#1}}

% ============================================================================
% Presentation Metadata
% ============================================================================
\title{Presentation Title}
\subtitle{Optional Subtitle}
\author{Author Name}
\date{\today}

\begin{document}
...
\end{document}
```

---

## Content Organization Best Practices

### One Concept Per Slide Rule

Each slide should convey ONE main idea:

**Good Structure:**
```
Slide 1: What is the Wave System? (Definition)
Slide 2: Core Concepts (4 concepts in table)
Slide 3: Disciplines vs Roles (Distinction)
```

**Bad Structure:**
```
Slide 1: Everything about Wave System
  - Definition
  - Core concepts
  - Disciplines
  - Roles
  - Benefits
  - Results
```

### Content Hierarchy

Within a slide, follow this hierarchy:

1. **Frame Title** - The main point (5-8 words)
2. **Block or Opening Text** - Context (1-2 sentences)
3. **Main Content** - Table or itemize (3-5 items)
4. **Supporting Detail** - Additional context if needed

### Progressive Disclosure Pattern

For complex topics, break across multiple slides:

```latex
\begin{frame}{Topic: Overview}
% High-level introduction
\end{frame}

\begin{frame}{Topic: Details}
% Specific details
\end{frame}

\begin{frame}{Topic: Example}
% Concrete example
\end{frame}
```

---

## Testing Your Presentation

### Readability Test

Present to someone 10 feet away:
- Can they read all text clearly?
- Is font size appropriate?
- Are tables legible?

If not: Increase font size or reduce content.

### 6-Second Rule

Can someone understand the slide's main point in 6 seconds?
- If no: Simplify content
- If yes: Good density

### Compilation Check

```bash
# Build presentation
cd sources/wave-system-presentation
make clean && make pdf

# Check for overfull warnings (tables too wide)
pdflatex main.tex 2>&1 | grep "Overfull"

# Fix overfull boxes by:
# 1. Reducing font size (\small → \footnotesize)
# 2. Shortening text content
# 3. Adjusting column widths
```

---

## Common Beamer Issues

### Issue 1: Table Too Wide for Slide

**Symptom**: Overfull hbox warnings, table extends beyond slide edge.

**Solutions**:
```latex
% Option 1: Reduce font size
\footnotesize  % Instead of \small

% Option 2: Adjust column widths
\begin{tabular}{lp{6cm}}  % Reduce from 7.5cm

% Option 3: Shorten text content
% "Implementation" → "Impl"
% "Enhancement" → "Enh"
```

### Issue 2: Fragile Frame Error

**Symptom**:
```
! Paragraph ended before \end was complete.
```

**Solution**: Add `[fragile]` to frames with code:
```latex
\begin{frame}[fragile]{Code Example}  % Add [fragile]
\begin{lstlisting}
...
\end{lstlisting}
\end{frame}
```

### Issue 3: Too Much Content on Slide

**Symptom**: Content spills off bottom of slide.

**Solution**: Split into multiple slides:
```latex
% Before (overflowing)
\begin{frame}{All Results}
\begin{itemize}
    \item Result 1
    \item Result 2
    ... 10 more items
\end{itemize}
\end{frame}

% After (split)
\begin{frame}{Results: Part 1}
\begin{itemize}
    \item Result 1-5
\end{itemize}
\end{frame}

\begin{frame}{Results: Part 2}
\begin{itemize}
    \item Result 6-10
\end{itemize}
\end{frame}
```

---

## Quick Reference

### Perfect Slide Template

```latex
\begin{frame}{Clear, Concise Title}

\begin{block}{Optional Context}
Brief explanation in 1-2 sentences.
\end{block}

\vspace{0.5cm}

\small
\noindent
\begin{tabular}{lp{7.5cm}}
\toprule
\textbf{Item} & \textbf{Description} \\
\midrule
\rowcolor{msgray!8}
Item 1 & Brief description \\
Item 2 & Brief description \\
\rowcolor{msgray!8}
Item 3 & Brief description \\
\bottomrule
\end{tabular}

\end{frame}
```

### Common Font Sizes

- `\normalsize` - Default (rarely used on slides)
- `\small` - Most tables (recommended)
- `\footnotesize` - Dense tables with 4+ columns
- `\scriptsize` - Very dense content (use sparingly)
- `\tiny` - Avoid (unreadable)

### Required Packages

```latex
\usepackage{graphicx}    % Images
\usepackage{array}       % Table formatting
\usepackage{booktabs}    % Professional rules
\usepackage{colortbl}    % Row coloring
\usepackage{tikz}        % Diagrams
\usepackage{listings}    % Code blocks
```

---

**Key Learnings:**
1. One concept per slide - split complex topics
2. Use 3-5 bullets max - avoid text walls
3. Tables are better than bullets for structured data
4. Always use `\small` or `\footnotesize` for tables
5. Do NOT use `\noindent` with Beamer tables (causes errors)
6. Add `[fragile]` to frames with code listings
7. Test readability from 10 feet away
8. Split overflowing content into multiple slides
9. Convert bullet-heavy slides to tables for scanability
10. Keep sub-bullets minimal - prefer flat tables

---

## Content Transformation Patterns

### Pattern: Bullets to Tables

When a slide has 6+ bullets or nested sub-bullets, convert to table format:

**Before (Violates 3-5 rule):**
```latex
\begin{itemize}
    \item \textbf{Frontend}: React, TypeScript
    \item \textbf{Backend}: FastAPI, Python
    \item \textbf{Skills}: Claude automation
    \item \textbf{QA}: Testing, validation
    \item \textbf{Writer}: Documentation
    \item \textbf{DevOps}: Deployment
\end{itemize}
```

**After (Better scanability):**
```latex
\footnotesize
\begin{tabular}{lp{7.5cm}}
\toprule
\textbf{Role} & \textbf{Technology} \\
\midrule
\rowcolor{msgray!8}
Frontend & React, TypeScript \\
Backend & FastAPI, Python \\
\rowcolor{msgray!8}
Skills & Claude automation \\
\bottomrule
\end{tabular}
```

### Pattern: Nested Lists to Tables

When bullets have sub-bullets with counts/metrics, use table:

**Before (Dense nested structure):**
```latex
\begin{itemize}
    \item \textbf{Review}:
    \begin{itemize}
        \item 30-50 recs first
        \item 10-20 recs later
        \item 60\% fewer bugs
    \end{itemize}
    \item \textbf{Parallel}:
    \begin{itemize}
        \item 40-60\% faster
        \item 3-6 roles
    \end{itemize}
\end{itemize}
```

**After (Scannable metrics):**
```latex
\footnotesize
\begin{tabular}{lp{8cm}}
\toprule
\textbf{Category} & \textbf{Metrics} \\
\midrule
\rowcolor{msgray!8}
Review & 30-50 recs (first); 60\% fewer bugs \\
Parallel & 40-60\% faster; 3-6 roles \\
\bottomrule
\end{tabular}
```

---

**Last Updated**: 2026-01-29
**Version**: 1.1
**Status**: Active
