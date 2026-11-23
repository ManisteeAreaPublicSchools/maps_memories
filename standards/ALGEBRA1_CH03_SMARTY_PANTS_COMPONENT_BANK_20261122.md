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

## Smarty Pants V3: Engagement and meaningful mathematical decisions (2026-11-22)

- Retain exactly three distinct lesson-specific optional challenges and stable IDs. Student work should require mathematical decisions, a model, a verified claim, or a design with constraints, not merely a larger calculation or an added "explain" sentence.
- Ten Chapter 3 options were revised: exponent impostor keys and invalid product-vs-sum law, negative/zero exponent card deck, equation-mat construction with an exact target solution, competing equal-perimeter area models, missing-area corner with a rival model, equal-area polynomial-product rival representations, a changed-dimension strip meeting a prescribed area, absolute-value solution-count redesign, and a triangular display with integral and height constraints.
- Preserve the discovery-versus-enrichment distinction: Smarty Pants is *after* lesson instruction and may call on completed EX/YTI skills. Challenge designs should be original and permit independent completion when partners are unavailable.
- Student prompts must supply required visuals and constraints but must not reveal conclusions. Teacher guides contain one correct exemplar, the reasoning that certifies it, other valid possibilities, and access notes that preserve rigor.
- Avoid turning a single numerical check into proof of an identity; use counterexamples to disprove false claims and structure/rules to establish universal identities. A numerical area check supports, but never replaces, algebraic comparison.
- V3 QA: 27 options and guides audited, all 27 single-page printouts passed, no MathJax/JS errors, all status and IDs unchanged. QA record: `maps_memories/standards/ALGEBRA1_CH03_SMARTY_PANTS_QA_V3_20261122.json`.

## Smarty Pants V4: Final independent classroom-readability and math checks (2026-11-22)

- Five additional targeted edits after V3: clarity on why the exponent machine's label fails; less 3-by-3 rectangle overwork (one full model plus coefficient table); accurate signed-number-line versus nonnegative physical measuring-strip distinction; genuine pricing-plan break-even transfer; and explicit lost-root reasoning when canceling a variable.
- Keep real tasks within the optional 10-18-minute envelope. Do not require students to fully redraw multiple nine-cell generic rectangles just to demonstrate a coefficient pattern. Record time as a planning estimate, never a classroom-measured fact.
- Teacher solutions must match each numbered student task exactly. For open-ended designs, state what makes any different student solution valid. Explain domain restrictions and distinguish algebraic answers from physically allowed outputs.
- V4 independent audit checked all 27 teacher guides and student cards, all nine exact lesson I Can targets, 27 one-page selected-challenge printouts, print exclusion of teacher solutions, no MathJax or JavaScript errors, and 42 targeted symbolic/numerical checks across V3/V4 revisions.
- The bank remains `PENDING_TEACHER_REVIEW`: not assessment-approved, not auto-assigned, and student exposure tracking remains a future builder task. Preserve canonical question banks, earlier version IDs, and student-assignment snapshots once connected.
- V4 QA: `maps_memories/standards/ALGEBRA1_CH03_SMARTY_PANTS_QA_V4_20261122.json`.

## Smarty Pants V5: Final student-facing quality gate (November 22, 2026)

- This was deliberately ONE final quality pass after V4, not a batch of new revisions. Chapter 3 remains nine exact lesson-level I Can goals x three selectable optional challenges (27 IDs); all remain `PENDING_TEACHER_REVIEW`.
- Eight targeted challenges were revised for authentic student decisions and clearer evidence, not difficulty inflation: neutral claims for exponent posters, unambiguous third-designer role and one-unit dimension changes, an area-equivalence challenge that does **not** require previously untaught trinomial factoring, competing complete products that do not leak the correct answer, an answer-neutral three-by-three rectangle, precise domain language, and cancellation reasoning that students discover for themselves.
- When a challenge asks students to evaluate a disputed result, NEVER reveal whether it is right or wrong in the heading or directions. Give actual rival claims or models, ask for mathematical evidence, then put the verdict in the teacher guide.
- A required generic rectangle is a mathematically meaningful visual: include blank student cells with accurate row/column labels, and verify the area products independently. Do not prefill answers. The bank renderer may use an optional `visual.label` to give the correct caption; preexisting visuals retain their historical label.
- Use complete products, equivalent coefficients, and structural arguments that are within the lesson. Students may notice a factorization, but should **not** be required to factor quadratic trinomials when the lesson is about generic-rectangle multiplication.
- For context restrictions, distinguish the solutions of the equation from the physically allowed subset. Clarify changes to width/height versus a border around every edge.
- Keep Smarty Pants optional, original, and post-EX/YTI: design, transfer, audit, or justify rather than simply add more routine calculations. Preserve IDs, source statuses, maths, and teacher hints in the teacher-only disclosure; future builders must select from the bank rather than independently regenerate it.
- V5 QA record: `maps_memories/standards/ALGEBRA1_CH03_SMARTY_PANTS_QA_V5_20261122.json`. Browser verified all 27 teacher guides and all 27 single-page selected student prints with MathJax, no visible teacher key or JavaScript errors. Targeted symbolic/numerical checks: 37 passed. Classroom engagement and timing still require teacher observation.
- This bank is a working reference for future chapters, not a blanket teacher approval. Next requested workstream: Practice Bank.
