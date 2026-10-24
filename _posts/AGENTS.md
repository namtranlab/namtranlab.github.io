# Statistics 110 study-note guidance

## Scope

These instructions apply only to work on the Statistics 110 study note and its figures:

- Study note: `_posts/2026-10-01-statistic_101_study_notes.md` (device path `/Users/namtran/Tmp/namtranlab.github.io/_posts/2026-10-01-statistic_101_study_notes.md`)
- Images: `assets/img/statistic-101/` (device path `/Users/namtran/Tmp/namtranlab.github.io/assets/img/statistic-101/`)
- Supporting textbook: `/Users/namtran/Tmp/Introduction_to_Probability.pdf` (Blitzstein and Hwang, *Introduction to Probability*)

They do not apply to other posts or unrelated repository work. Paths are relative to the repository root. This file sits in `_posts/` and has no date prefix, so Jekyll does not publish it. Read this file in full before making any study-note change.

## Authoritative content and preservation

- Read the current repository note before making changes. The user edits it manually, so the repository version takes precedence over earlier chat drafts.
- Find the last completed lecture in the note and continue the numbering from it.
- Preserve completed lectures. Modify a completed lecture only when the user explicitly asks.
- Append new lectures to the same Markdown file.
- Name entries `Lecture N - Topic` (for example, `Lecture 11 - Topic`) in the section heading, chapter title, and table of contents.
- Add each new lecture to the front-matter `toc` list without changing existing entries.
- Check write access before starting edits.
- Do not commit, push, or publish unless the user asks.

## Sources and scope

- Use the requested video or transcript to set each lecture's scope. Use the corresponding textbook sections to verify and clarify the material.
- If no video or transcript is supplied, say so and state which sources were used to set the scope.
- Prior chat with relevant history: `01a0f62a-0506-7fb1-8f77-16545d689aad`. It does not override the current repository note or the user's current instructions.
- Label supplementary examples, explanations, and material where appropriate. Do not present textbook topics outside the lecture as part of its scope without a label.

## Layout and markup

- Match the existing Distill/Jekyll layout, collapsible panels, CSS classes, math syntax, and writing style. Use the current note as the concrete template.
- Reuse the existing `toggleLecture` behavior and chapter markup. Give each new lecture unique IDs that follow the existing pattern: `lecture-N-toggle`, `lecture-N-body`, and `lecture-N-arrow`. Keep `onclick` targets, `aria-controls`, `aria-expanded`, and open-state classes consistent.
- Follow the note's current `$$...$$` conventions for inline and display math, and use `markdown="1"` on HTML blocks that contain Markdown.
- Reuse existing classes (`note-abstract`, `notation-panel`, `example-block`, `ex-pill` variants, `result-box`, `warning-box`, `misconception-block`, `glossary-entry`, `gcat` variants, `ref-tags`). Do not add new CSS unless the user asks.

## Content and writing style

- Explain concepts directly. Avoid phrases such as "the lecture says", "the lecturer explains", or similar commentary.
- Develop examples fully: state the assumptions, explain each step, give the result, and explain the core idea.
- Each lecture must include, using the existing headings and presentation:
  - an abstract
  - notation at a glance
  - learning objectives
  - numbered topic sections (`Part 1 — ...`, `Part 2 — ...`)
  - worked examples
  - misconceptions
  - original practice questions, with answers in a separate part
  - a quick revision table
  - a term glossary
  - reference tags
- Do not include Course/Source/Length/Basis metadata blocks, lecture roadmaps, study advice, general problem-solving checklists, or self-check checklists.

## Figures

- Save useful figures under `assets/img/statistic-101/` with descriptive names prefixed `lecture-N-` (for example, `lecture-11-textbook-fig-4-7-poisson.png`). Never overwrite existing assets.
- Embed figures with `/assets/img/statistic-101/...` paths and give appropriate attribution (for example, the textbook figure number, or "Original figure" for generated diagrams).
- Check that embedded paths resolve and that diagrams, labels, and math agree with the text.

## Verification

- Review the diff to confirm that completed lectures are unchanged and that edits are limited to the new lecture, its `toc` entry, and new figures.
- Check lecture numbering, ID uniqueness, HTML wrapper balance, math delimiters, practice answers, and figure references.
