# Algebra 1 Banks — consumer / assembly standard (2026-11-22, V6)

**Authority:** `CPM_Tools/banks/data/ALG1_BANK_CONSUMER_CONTRACT_V1.json`. The original `CH01.json`–`CH04.json` files remain authoritative for original question text, teacher review history, and textbook provenance. New files are a reversible review/selection layer, not an approval process. Use the user's approved bank CSS; do not invent another interface design.

## Which goal or lesson governs each bank

- **Assessment Bank:** Chapter → exact **section-level Learning Goal**, e.g., 3.1 exponent properties, 3.2 complete polynomial products, 3.3 equivalent equations. Direct Skills/core is a separate collapsible category from **Test-only Multiple Choice** and optional **application Extensions**. Chapter 3 has 12 core families per goal (36). This is a quality-guided starting count, **not** a required quota. Each Chapter 3 authored family has twelve numerical variants. Chapter 1/2/4 currently use existing curated canonical candidates and have variable counts and available swaps.
- **Practice Bank:** Chapter → exact CPM **lesson**. The Direct Skills bank supplies new lesson questions and **spirals from earlier Direct Skills**. Do **not** automatically use authentic CPM Review & Preview as the lesson's custom spiral set. Count an entire **family variant as one task**, even if it has multiple a–e parts. A ten-second isolated exponent fact is not one full practice task. A substantial single binomial/trinomial product or application CAN be one task; do not automatically force all practice into two or more subparts.
- **CPM Review & Preview:** actual original textbook problems, separate, source-ID-preserved, **four chosen per assembled lesson**. The browser features up to four shorter indexed originals per lesson for review, while exposing the rest. These are *suggestions*, not automatic selection or proof of skill alignment. When fewer than four are available (some Chapter 1 lessons), choose the rest from other appropriate original CPM material; never fabricate a textbook problem. For some original problems whose mathematics fits a lesson, a separately labeled teacher-adapted, shorter wording may be useful; show the complete original beside it. In this transfer, 3-6 and 3-7 have optional concise intro displays; the stored source text remains unchanged.

## Design of meaningful tasks

- 2-minute **assessment target** applies to the complete task, not each subpart; time is unverified in class. Five exponent properties = five independent quick parts (product, quotient, power of a power, zero, negative); other sets can have two or three parts. Do not construct one overwhelming algebra puzzle or use an added 'explain' as artificial rigor.
- Product questions ask for the **full polynomial in standard form**. A single binomial × binomial or trinomial × binomial product can be a valid check. Do not ask for individual partial products. Preserve the gradual lesson progression (e.g., generic rectangles before broader trinomial products).
- Equations should require genuinely distributed expressions and/or variables on both sides as specified by the target. For Chapter 3 numerical equation solutions, intended integers are -11 through +11 excluding zero. Algebraic formula answers remain formulas.
- Extensions apply skills in a context, transfer representation, compare, reverse conditions, or critique a real mathematical error. Making arithmetic larger or appending a generic justification is not an extension. Build structures inspired by `math_curriculum_craft_guide.md`, but do not copy publisher questions verbatim into new authored families.

## Interfaces and references for future consumers

- `banks/data/ALG1_CH03_ASSESSMENT_SCOPE_V3.json`: selected Chapter 3 section family IDs.
- `banks/data/ALG1_CH03_FAMILY_SETS_V2.json`: authored Chapter 3 Practice / Assessment family and full variant HTML, answers, IDs. New authored families remain `PENDING_TEACHER_REVIEW` / `assessment_eligible=false`.
- `banks/data/ALG1_CH01_CH02_CH04_CURATED_V6.json`: reversible Chapter 1/2/4 family review index; variants retain the **canonical source family ID and variant ID**. Some extremely short source tasks are displayed as clearly labeled two-part composites. Original CH files are never rewritten.
- `banks/data/CH01.json`–`CH04.json`: canonical textbook question families; authentic Review & Preview provenance and source images. Four authentic R&P selections must be tracked **separately** from the custom practice task slots.
- `banks/data/ALG1_BANK_CONSUMER_CONTRACT_V1.json`: machine-readable selection rules. Downstream builders MUST preserve family ID, variant ID, lesson/section goal, intended use, provenance, approval state, and selected original CPM problem ID.

## Limits and QA still to complete

- This transfer improves MathJax, whole-product task sizing, section/lesson routing, original CPM source selection, and Chapter 1/2/4 discoverability; **it is not a completed independent mathematical or classroom-timing certification of all four chapters.**
- In Chapter 4 most source families still have one original variant and need a deliberate parallel-number-swap generation and answer-verification pass. Several Chapter 1 lessons have fewer than four indexed original CPM R&P problems.
- The chapter source files and approval/review state are unchanged. `Assessment Builder`, `Lesson Builder`, and `Portfolio` are not automatically wired to the new bank selection and must not promote unapproved drafts.

## V7 visual mathematics and tables — required renderer policy

- Both `CPM_Tools/banks/assessment.html` and `CPM_Tools/banks/practice.html` load the **bundled offline MathJax runtime** at `/builder/assets/vendor/tex-mml-svg.js` through the local `CPM_Tools/app/server.py` whitelist. Do not load a CDN-only MathJax or invent another vendor path. The banks share `banks/bank_v2.js` and `banks/bank_v2.css` as the student/teacher browser renderer.
- For all *new* authored math containing a fraction, write MathJax source explicitly: `\(m=-\frac{2}{3}\)` or `\\(\frac{x+1}{4}\)`. Use `\frac{numerator}{denominator}` (and a leading negative sign), not text such as `-2/3` or `x/4`. Include math delimiters, do not put a stray TeX macro into plain HTML.
- Legacy source-family overlays sometimes contain typed numerical fractions such as `-2/3`. The shared renderer normalizes numeric fractions in ordinary student prompt text, teacher answers and solutions at **display time**; it does not change canonical question source, numeric values, variant IDs or approval status. Verify the fractions visually. Variable fractions and complex algebra should be authored as explicit MathJax instead of relying on this numeric-only fallback.
- When source questions contain tables, preserve their actual `<table><tr><th><td>` structures and render row/column gridlines with `.bk-math-table` CSS; do not collapse x/y rows into run-together text. Table A/B comparison questions display two readable small tables.
- MathJax must run when a bank group is opened, a numerical variant is swapped, an original source is expanded, **and when an Answer / solution pane is opened**. Validate zero `mjx-merror` errors and inspect at least one negative fraction and table in the browser before transferring.
- Preserve teacher-approved style, original textbook source identity, chapter/section/lesson mapping and all review status. Formatting fixes are not permission to rewrite canonical CPM source content.


## V8 (2026-11-22) — original CPM multipart and typesetting QA

- The four textbook Review & Preview questions chosen for a lesson remain authentic sources, independent from lesson-bank Direct Skills spirals. Display changes must **not** silently overwrite canonical CPM source records.
- In browser and print, original CPM letter labels **a., b., c.** must share the same line as the beginning of each part. Supported source markup includes `.ch3-rp-part-letter` / `.ch3-rp-part-content` and chapter-specific numbered lists containing wrapped paragraphs.
- Render mathematical fractions, especially slopes and negative values, with the already-installed offline MathJax resource `/builder/assets/vendor/tex-mml-svg.js`. If a fraction is initially stored as `-2/3`, display it as `-\frac{2}{3}`. Respect existing `\frac` and TeX delimiters.
- Preserve existing chapter bank and historical teacher feedback. Replaced V8 numeric candidates are teacher-review drafts. Their mathematical expansion was independently recomputed with SymPy and repeat-prompt audits were rerun.
- Future bank-quality passes should check duplicate prompts *across families in one lesson*, not only different numerical versions inside one family.
