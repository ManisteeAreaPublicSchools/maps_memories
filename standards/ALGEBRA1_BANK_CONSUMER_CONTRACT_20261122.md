# Algebra 1 Banks — consumer / assembly standard (2026-11-22, V6)

**Authority:** `CPM_Tools/banks/data/ALG1_BANK_CONSUMER_CONTRACT_V1.json`. The original `CH01.json`–`CH04.json` files remain authoritative for original question text, teacher review history, and textbook provenance. New files are a reversible review/selection layer, not an approval process. Use the user's approved bank CSS; do not invent another interface design.

## Which goal or lesson governs each bank

- **Assessment Bank:** Chapter → exact **section-level Learning Goal**, e.g., 3.1 exponent properties, 3.2 complete polynomial products, 3.3 equivalent equations. Direct Skills/core is a separate collapsible category from **Test-only Multiple Choice** and optional **application Extensions**. Chapter 3 has 12 core families per goal (36). This is a quality-guided starting count, **not** a required quota. Each Chapter 3 authored family has twelve numerical variants. Chapter 1/2 use earlier curated canonical candidates and available swaps; Chapter 4 current authority is the V11 teacher-review rebuild below.
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
- Historical V6 note superseded by Chapter 4 V11 below. Several Chapter 1 lessons still have fewer than four indexed original CPM R&P problems.
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


## V9 (2026-11-22) — question-quality / application / parallel candidate rule

- A family is an **evidence task**, not one micro-exercise. Group ten-second exponent calculations into short a–e parts where appropriate; one complete polynomial product or well-formed model can count as a full task. Do not inflate rigor by appending “explain” to the same calculation.
- The **Assessment Bank** is selected by the exact **section-level** Learning Goal. Practice is selected by **individual CPM lesson**. MC and optional application Extensions remain independent pools, not part of a numerical Direct Skills quota.
- Lesson assembly may choose **four authentic textbook Review & Preview** questions plus appropriate short spirals from **earlier Direct Skills**, particularly the preceding lesson. Never treat fabricated “Earlier:” variants as original textbook homework. Preserve original source attribution, with optional clearly labeled shorter display wording if faithful.
- **Do not assume 12 variants exist**: check actual `variants.length` in the live curated data. Never repeat a number swap to fill a quota. V9 gives 11 new draft options to 11 Chapter 4 source families while retaining their original version as V01.
- For context-based questions, verify geometry is physically feasible, money/counts are nonnegative and appropriate, pronouns and comparison directions agree with the arithmetic, and every numerical substitution preserves the evidence job. A “how much larger” area question must have a genuinely larger first area on the stated domain.
- New/rewritten source-display candidates require explicit individual teacher review and have `assessment_eligible=false`; never infer approval from an older source-family approval flag. Canonical Chapter JSON and original CPM teacher feedback are authoritative.
- In Chapter 3, the selected active 3.2 assessment scope is authoritative. Staged 3.2.4 quartic-product families outside that list are **not** automatically eligible for the short check just because their `bank=assessment` property exists.
- Runtime uses existing offline MathJax `/builder/assets/vendor/tex-mml-svg.js`, with stacked fractions and compact same-line multipart labels. The bank UI and loader paths did not change in V9.
- Review the V9 machine-readable QA report at `CPM_Tools/banks/algebra1/BANK_V9_CONTENT_AUDIT_20261122.json` and the shared human-readable `ALGEBRA1_BANK_QA_V9_20261122.md` when developing future bank consumers.


## V10 (2026-11-22) — Chapter 1–4 quality completion and source-aware consumption

- Chapter 4 now has **12 variant candidates for each of its 60 unique curated source families** (82 bank view records because some Direct Skills appear in both Practice and Assessment). V01 is the original source candidate. Newly authored V02–V12 variants are **PENDING_TEACHER_REVIEW** and remain ineligible for automatic student use. Do not treat candidate count as approval.
- Chapter 1 and Chapter 3 currently have 12 variants per displayed authored/curated family. **Chapter 2 intentionally has some quality-limited source pools** of 3, 4, 5, or 7 variants; retain their actual counts and do not pad with duplicate tasks. This is not a missing dropdown or bad data.
- All authored/curated Multiple Choice answer fields now provide **one letter A/B/C/D** for a bank consumer. The original response (e.g., `B. 11`, `Choice B — \(x^3\)`) is preserved on that same variant as `source_answer_before_v10`; the corresponding correct option is recorded as `correct_choice_text` or `correct_choice_math`. This is a reversible display/metadata normalization, not teacher approval.
- Chapter 3's `ALG1-CH03-V5-32-MULTIPLE_CHOICE-08` has a repaired offline MathJax `\text{side}` label in all 12 versions. Its correct missing-side option was separately checked against the displayed area and given side in all twelve versions.
- For Chapter 4, newly generated MC choices are unique, each keyed to a correct constructed expression, with key positions rotated. Generated system solutions were checked using SymPy; diagram-based versions include their own vector coordinate graph. These are authored drafts requiring teacher review.
- Preserve **section-level learning goals for Assessment** and **lesson-level Direct Skills for Practice**, with optional MC (test-only), Extensions (application), and original CPM Review & Preview (a separately sourced four-problem lesson component). Do not reuse authentic textbook Review & Preview as automatic spirals.
- Six Chapter 1 lesson source gaps remain: 1.1.1, 1.1.3, 1.2.1, 1.2.2, 1.2.4, 1.2.5 have fewer than four indexed authentic CPM originals. Use appropriate real earlier-source problems when assembling a lesson, rather than inventing CPM text.
- Full mathematical answer verification of every historic source variant and actual classroom timing is **not** claimed. Prefer the V10 QA ledger for source checks, variant counts, and unresolved teacher-signoff tasks. Keep modified/created candidate approval flags unchanged until explicit review.
- Package is **Curriculum Transfer — Local Only**. Do not use a plugin or script to commit, push, pull, sync, or replace a user repository. The teacher installs using their existing transfer helper.


## V11 — Chapter 4 substantive rebuild (2026-11-22)

- Earlier V10 Chapter 4 was **not finished** in pedagogical terms despite having 12 numeric swaps. V11 replaces the active Chapter 4 staged display and archives the prior 82 V10 staged display records at `CPM_Tools/banks/algebra1/archive/ALG1_CH04_CURATED_V10.json`. The source `CPM_Tools/banks/data/CH04.json` and teacher feedback/approval data remain unchanged.
- Practice Bank: Chapter → eight exact 4.x.x lessons; 68 new direct-skill task families (eight families per lesson except 4.3.1 with twelve). Each has twelve parallel variants; a complete system may stand alone and short evidence can be grouped. The next lesson's spiral is drawn from an earlier lesson's **Direct Skills**, never mistaken for original textbook R&P.
- Assessment Bank: Chapter → **three exact section Learning Focus statements**; 12 new core families for each of 4.1, 4.2, 4.3; **20 Test-only MC** and **17 Extensions** in separate collapsed sections. These are original teacher-review drafts. MC answer letters are checked against unique correct options; do not auto-certify.
- CPM Review & Preview: use **four actual original CPM questions per lesson**, taken from `CH04.json`'s `spiral` entries. All eight Chapter 4 lessons have at least four indexed originals. The R&P source remains separate and is not rewritten or autogenerated.
- Offline math renderer remains `/builder/assets/vendor/tex-mml-svg.js` with stacked fractions, graphs and proper tables. The shared `banks/bank_v2.js` renderer serializes live MathJax typesetting after variant switches.
- Consumer warning: new family IDs start `ALG1-CH04-Q11-`; all have `PENDING_TEACHER_REVIEW` and `assessment_eligible=false`. No generator or builder should automatically use them in production without an explicit teacher approval operation that is not part of this transfer.
- Review QA at `CPM_Tools/banks/algebra1/BANK_CH04_V11_QUALITY_AUDIT_20261122.json`. Automated checks do not substitute for independent hand-checking all variations or classroom timing. Chapter 1–3 content objects were left unchanged.
