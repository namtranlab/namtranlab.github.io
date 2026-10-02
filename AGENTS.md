# Statistics 110 study-note guidance

## Scope

These instructions apply only to work on `_posts/2026-10-01-statistic_101_study_notes.md` and its supporting figures in `assets/img/statistic-101/`. They do not apply to other posts or unrelated repository work.

## Authoritative content and preservation

- Read the current repository note before making changes. The user edits it manually; the repository version is authoritative over previous chat drafts.
- Preserve completed lectures. Modify a completed lecture only when the user explicitly requests it.
- Append new lectures to the same Markdown file. Name entries `Lecture 3 - Topic`, `Lecture 4 - Topic`, and so on, continuing the existing numbering.
- Update the front-matter table of contents for each appended lecture without changing existing entries.
- Verify write access before starting study-note edits.
- Do not commit, push, or publish unless requested.

## Sources and scope

- Use the requested video or transcript to establish each lecture's scope. Use the corresponding textbook sections to verify and clarify the material.
- Supporting textbook: `/Users/namtran/Downloads/Joseph K. Blitzstein, Jessica Hwang-Introduction to Probability.pdf`.
- Relevant prior chat, if history is needed: `01a0f62a-0506-7fb1-8f77-16545d689aad`. Its history does not override the current repository note or current user instructions.
- Label supplementary examples, explanations, or material where appropriate; do not silently present additional textbook topics as part of the lecture's scope.

## Layout and writing

- Match the existing Distill/Jekyll layout, collapsible panels, CSS classes, math syntax, and writing style. Use the current note as the concrete template.
- Reuse the existing `toggleLecture` behavior and chapter markup. Give every new lecture unique IDs following the existing pattern: `lecture-N-toggle`, `lecture-N-body`, and `lecture-N-arrow`. Keep onclick targets, aria-controls, aria-expanded, and open-state classes consistent.
- Match the current `$$...$$` inline and display math conventions and `markdown="1"` wrappers for Markdown inside HTML blocks.
- Explain concepts directly. Avoid phrases such as “the lecture says” or “the lecturer explains.”
- Develop examples fully: state the assumptions, explain each step, show the result, and explain the core idea.
- Include notation, learning objectives, numbered topic sections, worked examples, misconceptions, practice questions with answers, a quick revision table, and a glossary, using the existing headings and presentation conventions.
- Do not add Course/Source/Length/Basis metadata blocks, lecture roadmaps, study advice, general problem-solving checklists, or self-check checklists.

## Figures

- Save useful figures under `assets/img/statistic-101/` with descriptive filenames that avoid overwriting existing assets.
- Embed them using `/assets/img/statistic-101/...` paths, with appropriate attribution.
- Check that embedded paths resolve and that diagrams, labels, and mathematical content agree with the notes.

## Verification

- Review the diff to confirm that completed lecture content is unchanged and edits are limited to the requested additions and necessary table-of-contents updates.
- Check new lecture numbering, ID uniqueness, HTML wrapper balance, math delimiters, practice answers, and figure references.
