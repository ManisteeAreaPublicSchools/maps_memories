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
