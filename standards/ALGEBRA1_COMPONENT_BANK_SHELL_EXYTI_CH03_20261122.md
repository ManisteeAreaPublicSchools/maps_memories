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

## November 22 lesson-scope coverage revision (V2)

- A teacher selects **one** of the three EX/YTI alternatives for the lesson. Therefore each selected pair must independently model and practice the **essential lesson-level I Can**, rather than divide the important skills across the three choices.
- For 3.1.1, every option has three short labeled parts: product, quotient, and power-of-a-power. For 3.1.2, each option reviews zero and negative exponents plus quotient, product, and powered expressions using **five concise parts**. Each YTI parallels all parts with different expressions.
- For 3.3.1, every option includes both a distributed equation and a two-case absolute-value equation, consistent with its I Can.
- Do **not** apply a multipart quota to substantial polynomial products or other complete tasks. Those can remain a single EX followed by a single full-product YTI.
- Preserve matching a/b/c labels between the EX and YTI and avoid redundant numeric list markers in the worked steps. Print should show the chosen pair and its I Can on one letter page where possible.
- Source statuses remain teacher-review drafts; this is an instructional coverage pass, not a change to bank approval, assignment tracking, or automatic Builder integration.

## EX/YTI visual and mathematical QA revision (V3)

- Every worked example explicitly states the student's mathematical job; the matching YTI repeats it with fresh values. In formula problems, the required variable to isolate is always identified.
- For an EX/YTI choice that names algebra tiles (3.2.1), model the **initial equality** with signed x-tiles/unit tiles. Explain the equal move sequence and check the balance. A YTI does not get a prefilled answer diagram.
- For an EX/YTI choice that names a generic rectangle (3.2.2 through 3.2.4), include the correct 2-by-2, 2-by-3, or 3-by-3 generic rectangle in the EX for **every** choice. Show the whole product in standard form, then ask for the whole YTI product, not merely cell entries.
- Where a short multipart exponent example practices separate laws, avoid repetitive outcomes that provide unnecessary duplicate evidence; retain product, quotient, power, zero and negative exponent coverage as appropriate.
- For end-of-unit equation summary, include representative one-solution / no-solution / infinitely-many-solution classification and require justification rather than larger arithmetic.
- Rendering authority remains the shared offline MathJax and the existing V7 style. New tile models are intentionally compact and print-safe; print uses texture/border differences as well as color.
- Teacher-review status is unchanged, and these examples must **not** be silently approved for assessments or independently re-generated by consumer tools. Preserve pair IDs so future tracking/assembly stays stable.
- QA record: `CPM_Tools/banks/algebra1/ex_yti/QA_CH03_V3_20261122.json`.

## Final EX/YTI quality pass (V4, November 22, 2026)

- Chapter 3 remains nine lessons, each with three selectable EX/YTI pairs (27 stable pair IDs); all remain pending teacher review. The screen uses Chapter -> Lesson -> exact lesson I Can -> three teacher choices.
- In lesson 3.1.1, each chosen pair includes product, quotient, and power-of-a-power properties; quotient examples explicitly assume nonzero variables. In lesson 3.1.2, each pair includes zero and negative exponents and rule combinations. Do not promote isolated ten-second calculations into a complete example when the learning goal covers more.
- Algebra-tile examples must model the *starting equation*, with signed x and unit tiles matching the source expression. Keep models compact and readable rather than filling a panel with unnecessary unit tiles. Student YTI problems do not expose a solved model.
- Generic rectangles in the EX are mathematically exact; the corresponding YTI asks for the entire product in standard form rather than only a cell/partial product. A substantial complete product may stand alone.
- Formula rearrangements identify the target variable and all needed assumptions, and should cover both isolating with addition/subtraction and isolating through multiplication/division. Avoid unsupported division by a zero parameter.
- A matched YTI must change the mathematical evidence, not simply duplicate the exact example's answer. Examples covering classification of equations include one, no, and infinitely many solutions.
- Every example and YTI mathematical expression is eligible for independent symbolic checks; all 54 question/answer sides and all 57 generic rectangle cells passed the V4 audit. The 27 selected-pair print previews each fit on one letter page and exclude teacher answers. Preserve the existing offline MathJax route and approved V7 CSS.
- The EX/YTI component bank is an instructional-content source, not an assessment family bank. It must remain separate from Direct Skills, Extensions, and original CPM Review & Preview. Student issuance history must reference stable pair IDs and snapshots when integrated into assembly.
- The PD-day Tiered Task Tool remains a documented design reference for future extension writing; it is not installed or automatically integrated by this transfer.
- V4 QA record: `CPM_Tools/banks/algebra1/ex_yti/QA_CH03_V4_20261122.json`. The separate Chapter 3 Launch bank is next.
