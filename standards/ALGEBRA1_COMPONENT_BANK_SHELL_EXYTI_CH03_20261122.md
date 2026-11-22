# Algebra 1 lesson-component bank shell - Chapter 3 EX/YTI pilot

Date: 2026-11-22. Status: **installed after Local Only transfer; Chapter 3 content is teacher-review draft**.

## Teacher-approved component selector pattern

The Lesson Bank directory links to `CPM_Tools/banks/algebra1/ex_yti/index.html`.

- Top selectors: **Chapter -> exact CPM Lesson**.
- Show the exact lesson-level Learning Focus / I Can from the active Notes Bank.
- Provide **three options** for that lesson. Each option is an instructional Example / matching You Try It pair, not an assessment family.
- The EX is a fully worked and readable example. The YTI matches the method with different values, asks students to do the full mathematical job, and has a hidden teacher answer/solution.
- Select one option for print; the other two are alternatives, not additional mandatory student work. Do not fill printed pages with unnecessary ruled workspaces.
- Preserve lesson-level mapping and stable pair IDs, and mark new content `PENDING_TEACHER_REVIEW`. Do not infer that a new example has been approved for assessments.
- Chapter 3 currently supplies exactly nine lessons x three options = **27 pairs**. Other chapters are not populated in this component bank.

## Reuse for Launch and Smarty Pants

Use the same **Chapter -> Lesson -> exact I Can -> three choices** teacher-facing shell. Share its V7-derived styling from `banks/algebra1/components/` and user-review interactions, but keep each component's actual content and time expectations distinct. Launch needs discovery/investigation; Smarty Pants needs an optional substantive lesson-specific challenge. Do not turn either into three extra direct-skill worksheets.

## Exact content and reference authority

- Core I Can: `CPM_Tools/banks/data/ALG1_LESSON_GOALS_V1.json` (same lesson records displayed by Notes Bank), with Chapter 3 titles and lesson IDs.
- EX/YTI source data: `CPM_Tools/banks/algebra1/ex_yti/chapter3.json`, schema `cpm-algebra1-ex-yti-component-bank/1.0`.
- Parent guide inspiration: `CCA_PG_Ch3.pdf`, *Core Connections Algebra*, Parent Guide with Extra Practice pp.15-23. Exponent laws 3.1.1-3.1.2; equation mats 3.2.1; generic rectangles/multiplication 3.2.2-3.2.4; distributive/absolute-value equations 3.3.1; rearranging formulas 3.3.2. Original example/YTI arithmetic is newly authored; publisher examples/problems were not pasted into student cards.
- V7 style authorities: `maps_memories/standards/algebra1_modified_lesson_style_20261121_v7/css/01-tokens.css`, `02-lesson.css`, and `03-print.css`, copied unmodified into local `banks/algebra1/components/`; `component-bank.css` adds only the selector/review shell.
- Offline MathJax: `/builder/assets/vendor/tex-mml-svg.js`. Use stacked fractions, actual mathematical notation, and proper parenthesized products.
- Future bank consumers must preserve `id`, `lesson_id`, chosen option, mathematical data, teacher approval and printable snapshot when assembling student work. Teacher selection is local review state; automatic Lesson Builder integration is not yet implemented.

## Bank-first and student tracking

All student exercises should be selected from an appropriate approved source bank, rather than invented by a consumer while assembling lessons. The EX/YTI pairs are stored in the **Example/YTI component bank** for explicit teacher review and subsequent selection. Warm-ups, spirals, assessment questions and authentic CPM Review & Preview keep their own source-bank distinctions under `ALGEBRA1_BANK_FIRST_SELECTION_AND_EXPOSURE_V1_20261122.md`. Student assignment history will eventually record exact family/pair IDs, version IDs and delivered snapshots so revisions do not rewrite past evidence.

## Implementation and QA boundaries

The Chapter 3 bank has stable IDs, 27 matched pairs and a future-compatible three-option renderer; the app server has a fixed explicit route whitelist. The old `/banks/component.html?bank=ex-yti` link redirects to the new route; the existing Notes Bank remains unchanged. The bank is instructional content, not automatic Quick Check/Test selection. The current implementation does **not** write into the Lesson Builder or track individual student exposure yet. Do not mark it production/assessment-approved until reviewed by the teacher.
