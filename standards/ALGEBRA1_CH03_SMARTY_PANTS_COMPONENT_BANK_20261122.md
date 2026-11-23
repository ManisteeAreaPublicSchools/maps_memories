# Algebra 1 — Smarty Pants Lesson-Component Bank (Chapter 3 V1)

Date: 2026-11-22. Status: **teacher-review draft**.

## Authoritative UI and location

- Local module: `CPM_Tools/banks/algebra1/smarty_pants/` with `index.html`, `app.js`, `smarty.css`, `chapter3.json`, and QA JSON.
- Bank directory: `CPM_Tools/banks/section.html` → Smarty Pants. Legacy `?bank=smarty-pants` requests redirect.
- Select **Chapter → CPM lesson**. Display the **exact lesson-level I Can** from the Notes Bank and three independent optional challenges. Choose one and print only that challenge.
- Retain the approved V7 shared CSS in `banks/algebra1/components/` and the offline MathJax asset `/builder/assets/vendor/tex-mml-svg.js`. Do not duplicate CSS or substitute rendering packages.
- Student print hides the teacher guide, all unselected choices, and UI controls. One letter-size page per selected challenge. No blank ruled work areas or decorative teaching commentary.

## Instructional purpose

- Smarty Pants is **optional enrichment after students have learned the skill**. It is **not** a 15–20 minute pre-example Launch, not routine Direct Skills, not an automatic assessment item, and not simply difficult arithmetic.
- Nine Chapter 3 lessons have three original options apiece (27 total), each aligned with that lesson's I Can. Typical estimated effort 10–18 minutes; some designs require longer discussion or may extend further.
- Thinking moves vary: critique a claim, reverse-engineer a representation, compare mathematical models, add or test a constraint, invent an example, or build a generalizable rule. Do not force all three options into the same structure.
- A substantial challenge can be a single linked task with 2–3 related student prompts. Demand comes from mathematical decisions, not unnecessary 'explain' appendages.
- Explicitly separate universally true claims from checks at one input; require honest conditions (nonzero denominator, positive dimensions, realistic values). Do not hide needed diagrams or data.

## Sources and intellectual property

1. CPM Algebra 1 Chapter 3 authentic lesson/Launch cards and `CCA_PG_Ch3.pdf` guided the grade-level topics and instructional progression. Questions are newly authored; no proprietary problem text is copied.
2. Google Drive `~Curriculum/All Classes Resources/Resources/math_curriculum_craft_guide.md` **v6 Pass 6** guided original architecture designs (A8 dispute, A9 reverse/reconstruct, A19 contrast, A20 constraints/locality, A21 estimate, A22 student-posed, A23 method comparison, A25 matching representations, A33 rival models). Never repeat the guide's sample contexts or numbers or make every problem an 'A vs B' comparison.
3. District PD-day `tnezki/memories/district_tools/tiered_task_tool/TIERED_TASK_GENERATION_CONTRACT.md` **v0.4** is available as a cognitive-complexity and evidence-quality reference. DOK measures type of thinking rather than number size, computation count or verbs. A 10-minute bank challenge is not automatically labeled DOK 4. This transfer **does not install, modify or integrate** that district tool.
4. All problems are original variants stored with stable IDs `ALG1-SMARTY-<lesson>-A/B/C`. They are not copied from the Assessment Bank and are not added to the canonical CPM chapter-question files.

## Bank-first assembly and tracking

- Future Lesson Builder/Smarty Pants selection must use the **stored approved bank item**; do not generate an untracked new challenge at assembly time.
- Save item ID, lesson ID, version or content revision, teacher approval flag, and a delivered student snapshot so later bank edits do not rewrite issued student work. Respect student exposure history to avoid repeats when suitable alternatives exist.
- Do not automatically assign Smarty Pants to every student. Select it deliberately for students ready for enrichment. Teacher approval is still required for each new item.
- Keep original CPM Review & Preview distinct (lesson builder selects four authentic originals) and keep Quick Check/Checkpoint/Test Assessment Bank separate. The Chapter 3 Smarty Pants Bank does **not** create or imply integration with Portfolio or other builders.

## QA and preservation

- 9 lessons / 27 options / 81 question prompts, 45 independent mathematical assertions, 27 one-page print checks, no MathJax or JavaScript browser errors, all teacher answers excluded from student PDF.
- See `QA_CH03_SMARTY_V1_20261122.json` for boundaries and verification evidence.
- Existing Launch V5, EX/YTI V4, all other banks, canonical textbook questions, approval history, and current V7 CSS are unchanged.

## V2 instructional-quality pass — 2026-11-22

- **11 of 27** Chapter 3 Smarty Pants options have refined student prompts, teacher mathematical evidence, facilitation guidance, or time estimates. Original lesson IDs, option IDs, 3-option lesson structure, thinking moves, and pending-review statuses remain unchanged. The other 16 options are unchanged.
- **Exponent-property alignment:** zero/negative-exponent enrichment should NOT assume students can solve a reciprocal equation for every real input before studying that algebra. Prefer sign-pattern investigations and construction of equivalent expressions using zero/negative powers. A universal rule requires property reasoning; comparing a=1 and a=2 can reveal why a successful test is insufficient proof.
- **Equation mats:** directions must distinguish an illegal one-sided removal from legal equal-side moves. For contrasting solution paths, change the order of two valid moves on a correct starting mat and check the unique solution in the original equation.
- **Area models:** a change in dimensions should invite students to construct/annotate added strips and corner regions, not only repeat full expansion. Missing-cell critiques must identify the specific omitted product; single-value tests do not prove identities.
- **Student-designed challenges:** forbid superficial duplicates (e.g. exchanging p and q in commutative factors). When appropriate, compare all allowable integer designs to justify a maximum, not merely produce two examples.
- **Applications:** domain restrictions filter mathematically valid solutions and must not reveal the requested roots in the student prompt. Formula-rearrangement applications can compare two fee models and verify using the isolated variable, with realistic dollars and item counts.
- **Solutions:** the teacher guide must match the exact revised student task, show a valid exemplar and restrictions, and name where other solutions are acceptable. Avoid unnecessary scaffold space or repeated explanation instructions.
- **Verification:** 33 targeted independent math assertions, 9 lesson selectors, 27 choice renders and 27 one-page print checks passed. No MathJax or JavaScript errors observed, and teacher solutions were excluded from print. QA file: `maps_memories/standards/ALGEBRA1_CH03_SMARTY_PANTS_QA_V2_20261122.json`.
- **Preservation:** existing V7 CSS, offline MathJax, Launch V5, EX/YTI V4, Direct Skills, Assessment, Notes, original CPM sources, and review/approval records unchanged. Smarty Pants remains an optional lesson-level enrichment source; teacher approval and tracked issuance are still required before automatic consumption.
