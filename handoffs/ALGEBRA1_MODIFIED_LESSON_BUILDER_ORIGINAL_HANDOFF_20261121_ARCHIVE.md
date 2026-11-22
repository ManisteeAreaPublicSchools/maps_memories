# ALGEBRA 1 MODIFIED LESSON BUILDER — COMPLETE NEXT-CHAT HANDOFF

**Date:** November 21, 2026 (America/Detroit)  
**Project:** Textbook Extraction / CPM Tools / Curriculum Build / Algebra 1  
**Conversation name:** Modified lesson builder  
**Handoff purpose:** Preserve detailed decisions across a long conversation. Next chat must resume: (1) critique and revise the standalone lesson HTML/CSS prototype; (2) continue resource cataloging while a ~20 GB Google Drive `Resources` sync completes (especially the 30-year `pods` archive); (3) finish the Q5/Q6 warm-up bank thoughtfully; (4) build the yearlong prepopulated, editable Modified Lesson Builder around the existing CPM Tools Assembly engine.

> **READ THIS FIRST IN THE NEXT CHAT.** This package is a HANDOFF, **not an installable Curriculum Transfer**. Do **not** put this ZIP in the Curriculum Transfer inbox. The original prototype ZIP is bundled as a reference so the next chat can edit exactly the same starting point. Do not install/rewrite CPM Tools just because this handoff has been uploaded. The teacher's next input will most likely be screenshots and criticism of the CSS prototype.

## 0. Resume immediately: concise action plan

1. Read this handoff **fully**, then inspect `prototype/Algebra1_Full_Lesson_CSS_Critique_Prototype_20261121.zip` (it contains precisely `lesson.html` and `css/01-tokens.css`, `css/02-lesson.css`, `css/03-print.css`). This is a **standalone prototype**, not a production file. Do not assume it is final/approved. The teacher is about to inspect this version for the first time.
2. When the teacher sends changes, revise **the same prototype**, iterating its CSS and HTML while preserving the current component roster, optional variants, MathJax, print layout, and paper-page boundaries unless the teacher explicitly changes them. Repackage as **one ordinary standalone ZIP**, not a GitHub Transfer, during CSS critique. Render and visually inspect screen and print layouts.
3. Continue the independent **resource catalog** as the Google Drive sync advances. Recheck the actual `Resources` tree, especially `pods`; do not call unrelated PODs folders the archive. Catalog *problem structures with verified source/page, skills, time, visual requirements,* and fit for warm-ups/Smarty Pants/Monday/sub lessons. Never overclaim an image-only PDF has been read without rendering/visual inspection.
4. After sufficiently cataloged and approved, finish a **targeted rebuild** of warm-up Q5/Q6 using the corrected **four extension families per LESSON total** (NOT four per source spiral). Keep Q1–Q4 stable. Q5 is normally application or conceptual from Q3/previous lesson; Q6 is a best-fit deeper extension from Q4/Portfolio priority. Do not mass-generate superficially different variations.
5. Then implement the Modified Lesson Builder in CPM Tools using the existing Assembly engine and approved styles, with a complete prepopulated year, editable choices and AI-request packaging. Use the authoritative mirrored code and local-only transfer hashes; never auto-commit or push.

**Important:** This is a long-standing teacher workflow. Do not repeat prior questions already answered, invent a new parallel builder, insist on a new upload when a Drive mirror already contains the files, or change course scope inadvertently. The teacher specifically wants strong continuity and hates repeatedly rebuilding the same decisions.

## 1. Governing product idea and philosophy

- Goal: **AI authors the year's Algebra 1 lesson content ahead of time**, and the application prepopulates the teacher's planner. The teacher then edits, switches versions, reorders/omits components, and makes an **AI Request** only for changes, not daily generation from scratch.
- Most operations should be deterministic/plug-and-play. The AI-generated pieces are especially (a) the actual Learning Focus/Notes when a new design is approved, (b) 2–3 curated Launch options from CPM Launch/Explore source cards, and (c) request-driven edits. Other content should normally be chosen from verified banks and prepared options.
- **Curriculum content is separate from question instances, planner recipes, and published artifacts.** An accepted learning goal and a family are reusable; finished question versions must be tracked to prevent accidental repeats.
- Build initially for **Algebra 1 only**, within CPM_Tools. Eventually reuse the architecture for Physics and include Calculus when appropriate, but do not place Algebra 1 warm-up bank files in generic shared locations.
- Teacher has already backed up the installed CPM Tools and can revert; nevertheless **preserve the existing Builder and teacher work** and make additive/targeted patches. Teacher controls GitHub Desktop and all Git operations.
- Use the approved `maps_memories` contracts/CSS standards as the eventual authoritative common reference. During critique, change prototype CSS first; do not silently update shared production CSS.
- Student output should be simple, printable, comfortable for writing, **MathJax-correct**, and suitable for both offline HTML and paper/PDF; teacher-facing answers and controls must never contaminate the student copy.

## 2. The 10 menu components — current agreed structure

The user explicitly prefers this plain numbered list, with one selected practice format in a lesson. Current names and roles:

1. **Warm-ups** — regular day: Q1 solving; Q2 diamond/factoring; Q3 previous completed lesson I Can; Q4 Portfolio-priority previously taught I Can; **Q5** optional application/conceptual from Q3; **Q6** optional best-fit deeper extension from Q4. Monday and substitute variants below.
2. **Learning Focus / Notes** — approved *lesson-specific* I Can statements, relevant vocabulary, and only the actual lesson's **Methods & Meanings**. Teacher plans to provide a **new visual format**; do not guess final notes design before seeing it. Store eventual format/CSS/conventions in `maps_memories`.
3. **EX / YTI** — worked example + closely matched 'You Try It' for this lesson, in approved CSS, MathJax, with separate teacher solution. **Do not conflate with Smarty Pants.**
4. **Launch** — **2–3 selectable options** derived from the CPM lesson Launch/Explore cards, usually a 15–30 minute investigation. May use all/part of the source activity, adapt meaningfully; make an AI Request possible.
5. **Smarty Pants Section (Optional)** — the new name for *Current-Lesson Extensions*. Relates to **today's** lesson, not previous-lesson warm-ups. Usually **3–4 connected application questions OR one coherent multipart mini-performance task**; perhaps provide two choices. Optional/challenge. User likes applications, conceptual depth, and meaningful transfer.
6. **Projection Sets** — one delivery format for the **same lesson practice set** used by all items 6–9; no separate bank.
7. **Rounds** — another layout/interaction format for exactly that practice set.
8. **Find Someone Who** — collaborative movement/discussion version of that set, with appropriate writing space and answer verification.
9. **Stations / Task Cards / Whiteboards** — interchangeable display/print formats for that **same underlying set**, not independently regenerated questions.
10. **Reflection** — a short **NON-mathematical exit ticket**: student confidence, how the activity went, what needs clarification, what helped learning, rating/scale. Rotate choices. It is not an additional math assessment problem.

**Default lesson order LOCKED by teacher:** `Warm-up → Learning Focus / Notes → EX/YTI → Launch → Smarty Pants → one selected Practice Activity (Projection Sets / Rounds / Find Someone Who / Stations / Task Cards / Whiteboards) → Reflection`.

The teacher can still reorder, omit, duplicate, substitute, change versions, or generate an AI Request. On an earlier isolated lesson, he preferred Launch before Example for discovery; that is an allowable per-lesson override and does **not** displace the subsequently approved default order.

## 3. Warm-ups: precise current decisions

### Q1 and Q2, side-by-side student choices

- **Q1:** left = linear equation; right = quadratic equation when quadratic solving has been introduced. Student chooses **one** to solve. At the start of the course only taught choices are available; track when alternate first becomes allowable; once introduced, do not require teacher to manually select quadratic every day. Teacher wants linear progressions through the year and mathematical variety.
- **Q2:** left = diamond; right = factoring when taught. Student chooses one. **Diamond diagrams must come from the approved Grapher / District Graph Tool**, not a crude Unicode diamond or a poorly drawn substitute. Proper conventional diamond: product on top, sum on bottom, two unknown side values. Separate factoring when introduced. Q1 and Q2 ideally have a shared workspace beneath choice pair rather than duplicate giant spaces for work students won't do.
- Original user-designed linear solving progression starts with `ax+b=c`, `c=ax+b`, `b+ax=c`, `c=b+ax`, then distributive structures and eventually variables on both sides. Explicit forms listed by teacher:

```
ax+b=c
c=ax+b
b+ax=c
c=b+ax
a(x+c)=d
d=a(x+c)
a(bx+c)=d
d=a(bx+c)
a(x+b)+c=d
d=a(x+b)+c
a(bx+c)+d=e
e=a(bx+c)+d
a(x+b)+cx=d
d=a(x+b)+cx
a(bx+c)+dx=e
e=a(bx+c)+dx
a+b(x+c)=d
d=a+b(x+c)
a+b(cx+d)=e
e=a+b(cx+d)
ax+b(x+c)=d
d=ax+b(x+c)
ax+b(cx+d)=e
e=ax+b(cx+d)
```

  Then similar families with variable terms on both sides. **Course entry is two-step equations, not advanced equations.** Eventually introduce positive and negative rational solutions, ending later with fractional coefficients. For initial integer stages: nonzero integer **solutions from -11 to 11** (all options represented, not predominantly 1/2/3); coefficients also generally -11..11; favor distinct coefficients/constants where practical to avoid ambiguous verbal references such as “divide by 4” when several 4s appear. Later stages may use fractions by design. Do not print `1x`, `-1x`, `x^1`, leading `+2x²`, or placeholder syntax.
- Q1 quadratic families include monic factorable, nonmonic factorable with GCF, **primitive/non-GCF nonmonic** (separate new family), quadratic formula. Worked solutions must match actual taught strategies. Factoring should use the **generic rectangle/area model**, not AC method, which teacher explicitly says he does not teach/know. If a GCF can be removed, show that path as its own family; not every nonmonic quadratic should happen to divide cleanly.
- **Answer and solution formatting:** Teacher's exemplar has left column math lines and right column short blue instructional comments **aligned to the operation on the SAME line**. `Distribute` comment sits next to the original expression, with the resulting expression underneath; next `Combine like terms` next to the line where combining begins. **Do not combine distributing and combining in a single algebra step**. Correct operation wording and signs, show individual algebra operations, double-check every step. For quadratic formula show identify `a,b,c`, discriminant, substitute, simplify, separate plus/minus, result. Verify final roots, coefficients. For diamonds, solution simply shows product and sum check; for factoring, stage-by-stage generic rectangle with check.
- Bank teacher review should show question and worked answer **permanently in right column**; **Check answer & solution** popup button belongs in the **assembled warm-up student HTML** (teacher notes/answers separately for PDF), not a redundant bank-review button. An unnecessary “Warm-up HTML popup preview” was ordered removed. The review screen uses `Good` by default, only click **Needs Work** if something is actually wrong. **Next version** (or Swap numbers, Switch sides as appropriate) changes prepared instance without automatically marking question used. The teacher should not have to individually mark every family reviewed.

### Q3/Q4/Portfolio

- Q3 = a spiral family for **previous actually completed instructional lesson's I Can**. **Continuing a lesson** reuses that instructional position; it must not advance curriculum merely because calendar day changes. New question instance for continuation day (warm-up-only replan option).
- Q4 = class-level **Portfolio-derived weak I Can** from previously taught material. Teacher previously requested “pick this automatically”—no daily dropdown. Portfolio ranks weak evidence; do not expose student-level data in warm-up interface. **Q4 selects a fresh question from the distinct Q3/Q4 WARM-UP SPIRAL BANK**, NOT the assessment bank question that originally supplied evidence. The approved assessment bank is a *skill, family, and authoring reference*, not the actual Q4 instance. Portfolio selection is **planned, not connected** as of this handoff.
- Q3/Q4 bank built for **102 Algebra 1 lessons**, **2 spiral families per lesson** = 204 families, each 8 prepared variants = 1,632 question instances. Previous assistant reported a major lesson-alignment pass on 60 lessons and specific fixes for completing square, quadratic formula, statistics, algebra tiles, residuals, etc.; these are historical build claims, not a substitute for validating current mirror.
- Review URLs in local CPM Tools look like `http://127.0.0.1:57220/banks/algebra1/warmups/index.html#q3`; tabs `Q1 Solve`, `Q2 Diamond/Factor`, `Q3/Q4 Spirals`, and `Q5/Q6 Extensions`.
- Prior serious bug: custom Flask/CPM server had an explicit whitelist and did not serve newly created `spirals.js`, `spirals.css`, `spiral_families.json` until registered in `CPM_Tools/app/server.py`. Blank tab and `Loading...` screens resulted. If new CSS/JS/JSON fails to load, check the **server route/whitelist** and hard reload/restart, not only JS visibility. An earlier transfer also failed from **SHA256 mismatch on `server.py`**, so check exact authoritative bytes before packaging a replacement.

### Q5/Q6, correct latest decision (IMPORTANT)

- Teacher wants **deeper thinking**, not larger arithmetic: application/transfer most common, conceptual thinking next, different representation when suitable, function notation evaluate/solve when taught, less frequent errors/method comparisons/missing info. The concepts **must connect to the actual Q3 and Q4 math**.
- **Q5**: most often **application OR conceptual extension of Q3** (last lesson), perhaps rotating. **Q6**: a **mix of the best-fitting kinds of reasoning** linked to Q4 (Portfolio-priority spiral), not a forced category. Optional challenge for students ready for more; not mandatory for everyone.
- **LATEST TEACHER CORRECTION: ONLY FOUR EXTENSION FAMILIES TOTAL PER LESSON**, not four for each of two spiral families. Previous assistant built 816 families (204×4) and called them “eight per lesson” — the teacher corrected this. Target design is **four meaningful lesson-level extension options**, with sensible compatibility/linkage to whichever spiral is selected for Q5/Q6, not eight artificially generated tasks. The categories are:
  1. **Application** (interpret/model in meaningful setting; may use function notation).
  2. **Conceptual** (explain, predict, investigate, generalize).
  3. **Transfer** (apply the mathematical structure to a substantively different concept/condition, not the same area multiplication with a new story).
  4. **Puzzle / Reasoning** (missing information, visual detective, error, method comparison, other investigative structure).
- **Observed failures in last generated Q5/Q6 bank:** In 3.2.3, `Transfer` and `Application` both essentially ask for polynomial rectangle area; teacher said too similar, meaningless labels. A prompt literally printed **`x={x}`** instead of a numerical substitution, even while a worked solution used x=6; must scan all template tokens and test every generated instance. Multiple near-identical tasks across source spirals / lessons are a problem even when textual prompts differ; compare reasoning type, mathematics, representations, and actions, not only string uniqueness. Avoid mass generation before source catalog informs meaningful structures.
- Current *built* Q5/Q6 bank last transfer claimed **816 extension families** and 6,528 distinct eight-version prompts, but this is **historical implementation, not approved new target**. Current user preference supersedes it. The existing bank is a baseline/reference; do not accidentally treat the count as a requirement. Q1–Q4 should remain unaffected when building revised Q5/Q6.
- Quiz review itself should show original Q3/Q4 question, answer, **four genuinely different candidate extension options per lesson** and all worked solutions; the teacher can flag Needs Work. Different numerical versions should be coordinated with source when mathematically linked, and instance IDs + category metadata preserved where possible.
- Monday and substitute days: optional Q5/Q6 can be **puzzle-style**; they need not each depend tightly on a Q3/Q4 source. Do not force six warm-up questions on Monday.

### Monday modeling, continuing, substitute warm-ups

- **MONDAYS KEEP Q1 SOLVE + Q2 DIAMOND/FACTOR.** Important correction: do **not** replace the first two with notation questions.
- Monday **Q3 is ONE multipart (a,b,c...) function notation/modeling prompt**, e.g. `p(t)` rabbit population with t=years, identify what notation represents, **evaluate** `p(3)`, **solve** `p(t)=30`, interpret output vs input. Rotate the representation: **table, graph, equation, mixed**. The progression runs throughout year with increasingly rich linear, quadratic, exponential models as taught; don't introduce future techniques too early.
- Monday Q4 can be an **optional short puzzle/conceptual prompt** instead of a full regular six-question set. Monday main lesson often a modeling/performance task. `Q1/Q2` retained as standard.
- **Continuing lesson**: teacher wants option to regenerate **only warm-up**, keep same instructional position and rest of lesson recipe, choose fresh instances. This is a calendar day but not a new completed curriculum lesson.
- **Substitute day**: independent accessible warm-up/practice/puzzles, possibly no six-question structure, separate saved day type. No automatic pacing advancement.

## 4. Shared 12-question PRACTICE SET for formats 6–9 (important recent correction)

**ONE 12-question set per lesson, not a separate bank for each activity.** Exact same selected questions can be rendered as Projection Sets, Rounds, Find Someone Who, Stations, Task Cards, or Whiteboards; change in a shared selected question propagates through all formats.

- **Questions 1–8:** current-lesson skills plus purposeful **spirals** placed FIRST, so students do the important work even if class doesn't finish the set. Flexible balance (e.g. more new skill when instruction is recent, more spiral during review). Selection/difficulty needs explicit pedagogical plan. Do not use multiple choice (teacher's stated preference for these format sets).
- **Questions 9–12:** the **four best CPM Review & Preview problems** for that lesson as selected by the assistant, *unless* problems are very wordy, confusing, too repetitive, have little spiral coverage, or clash with timing. Replace selectively with approved bank family instances/new quality-authored alternatives. The teacher is concerned CPM R&P may not spiral widely enough. **Do not assume all R&P are good or discard all R&P wholesale.** We will develop a replacement/selection policy after seeing examples.
- Source rights: CPM textbook/cards are canonical to see and adapt; keep appropriately licensed/purchased teacher material inside local synced student/teacher lesson destinations as already arranged; don't copy source into publicly indexed artifacts by default.
- Changing a question in the lesson practice set changes all activity-format views; sharing the set is *selection*, not necessarily delivering six formats in one printed student packet. Most lessons choose **one** practice activity.
- Record actual published question instances *once* as used, not once per rendered format or preview. Alternate numbers allowed, but no accidental repetition across regular, Monday, substitute, continuation, later lesson, or performance-task build.

## 5. Notes / EX-YTI / Launch / Smarty Pants / Reflection quality requirements

**Learning Focus / Notes:** The teacher says a **new visual format** is coming. For now prototype is explicitly provisional. Must show approved lesson I Can (accept/edit), clearly formatted vocabulary (student-highlightable definitions), only applicable CPM Methods & Meanings, a few concise precise notes and visuals. No generic filler or overloading the section. Shared styling in `maps_memories` once approved. The prototype is meant for CSS critique, **not** approval of this template's content.

**EX / YTI:** Separate from extensions. Teacher wanted paired worked EX and YTI with consistent visual styles; do not use distributive-property generic examples as the sole emphasis of 3.2.3 (specific lesson emphasis was 2×3 rectangle for trinomial×binomial, introduce trinomial×trinomial). MathJax; full lined/workspace appropriate to student; quick teacher answer/solution popup in HTML and teacher answer key for print.

**Launch:** 2–3 distinct substantive choices from CPM lesson Launch/Explore, 15–30 min. One may retain strong existing CPM task, another use alternate representation/model, another shorter scaffold/route. Must respect available methods and no future prerequisites. User picks an option in planner; AI request available to rewrite/adapt. Not generic “discussion” or cosmetic variants.

**Smarty Pants (Optional):** Current lesson's application/mini performance extension, typically 3–4 connected questions or one multipart coherent real-world modeling task. Very different role from Q5/Q6 warm-up extensions, which go with earlier/weak spiral skills. Name and optional status important.

**Reflection:** Not math questions. Prompt examples: rate understanding 1–5, confidence on doing independently, what helped, what remains confusing, what support would help. Printed brief response/scale. Rotate choices, do not use as another scored assessment.

## 6. Yearlong Modified Lesson Builder: architecture and pending work

- **Separate Builder**, alongside normal CPM Tools Builder. Do not disturb existing Builder or student/teacher saved lessons. Pilot exists historically but was not the final intended system.
- At lesson selection, show **approved I Can** (teacher accepts/modifies). Prepopulate the lesson planner with chosen Warm-up, Notes, EX/YTI, Launch, Smarty Pants, practice set and default activity format, Reflection. Teacher controls order and alternatives before Assembly; choose options and **AI Request** for edits.
- Prebuild **all Algebra 1 lessons for the year** (official CPM course has 102 lessons), respecting teacher pacing and Monday modeling/continuations/substitute/performance-task days. Track source lesson vs *instructional position* separately from calendar day.
- Reuse approved **CPM Tools V3 left control panel + live student preview on right**, not a new unrelated form-driven UI. Document-level controls above item controls; move up/down, use/hide, edit, alternate instance selector, +/– margins and space adjustments where relevant, manual breaks, normal/roomy/compact, save draft/publish/open student page stable controls.
- Publishing uses existing **Assembly / paginated print engine** and local lesson file routing, HTML/PDF, stable naming; teacher drafts/answers and student print output cleanly separated. Route to correct Algebra 1 synced folder, not generic global folder. Use latest `maps_memories` course artifact naming and lesson-drive structure contracts if available.
- **Question-use log** is essential: JSON database/log with stable family ID, instance ID/content fingerprint, course, I Can, lesson/day type, date/publish artifact, source vs published instance, positions Q1–Q6 and Practice 1–12, and perhaps parent-child (Q3/Q5, Q4/Q6). A preview, Next Version click, or unsaved draft must **not** consume a question. On publish, transactionally register; republishing/rebuilding same artifact must replace/update record, not append duplicate. New Monday/substitute/performance-task/continuation artifact must be recorded and protected. Detect both exact and disguised duplicates (values/context/visual stimulus) against history; if pool exhausted, generate approved fresh variant / issue visible warning rather than silently recycle.
- **Portfolio Q4:** use aggregate/skill weakness only, not individual student records; read latest observed weak skill, restrict to *previously taught*, select fresh instance from the *warm-up bank*. Exact backend API and matching date requirements still to be implemented.
- **AI Request path:** package source lesson I Can, relevant CPM cards/Methods & Meanings, current prepared component, approved CSS, prior teacher review flags, requested edits, and target filenames/routing; return changes through local transfer and preserve teacher decisions. Avoid giant rebuilding requests for what can be deterministic.
- Before any production patch, compare current **running local source** vs Drive mirror, inspect precise integration points, and obtain correct `expected_existing_sha256`. Prior mismatch failures occurred. A backup exists, but don't rely on backup as excuse for risky patches.
- Later port architecture to Physics and adaptable math courses including AP Calculus; for Calculus, do not assume Q1/Q2 Algebra fluency structure applies without separate course rules.

## 7. Standalone CSS critique prototype — EXACT CURRENT STARTING ARTIFACT

Included in this handoff ZIP as:

`prototype/Algebra1_Full_Lesson_CSS_Critique_Prototype_20261121.zip`

Inside the prototype ZIP (verified actual ZIP entries):

```
lesson.html
css/01-tokens.css
css/02-lesson.css
css/03-print.css
```

This ordinary ZIP was delivered immediately before user requested handoff. The teacher **has not yet reviewed** it. It is a **fictional lesson 3.2.3** and includes warm-ups (two paper pages, Monday and substitute variants), provisional notes/learning focus and vocabulary, worked EX/YTI, three Launch options, optional Smarty Pants, a 12-question set rendered as multiple practice formats, Reflection, and teacher/student modes. Buttons include student/teacher, day type (regular/Monday/sub), font size, spacing, practice format selection, and HTML solution popups. Paper page boundaries are visible. MathJax 3 SVG runtime is **embedded inside the one HTML file for offline use**, making HTML large (~2.2 MB). Stylesheets are separate to promote easy design tweaks. The prototype HTML is not production-ready Bank/Builder; it was specifically made for visual critique of typography/layout, workspace, diagram size, CSS tokens, print.

**Current prototype CSS tokens** (`css/01-tokens.css`, starting point, not approved):

```
--navy:#163d5e; --heading:#19486a; --ink:#20394d;
--line:#cbdbe5; --surface:#f3f7fa; --soft:#eaf3f8;
--body-font:'Aptos','Segoe UI',Arial,Helvetica,sans-serif;
--body-size:17px; --page-width:8.5in;
--page-min-height:10.95in; --page-pad:0.57in;
--page-gap:26px; --section-title-size:20px;
--work-line:37px; --card-padding:17px;
```

`css/02-lesson.css` owns visual components; `css/03-print.css` owns Letter-size printing, explicit page breaks, hidden controls, selected practice format, workspace. Actual user critique may change all of these. **Don't insist this CSS is approved**. Existing references consulted: Algebra shared `base.css` from `tnezki.github.io/algebra/css/base.css`, actual `banks/algebra1/warmups/style.css`, existing CSS tokens from class materials. The notes look is especially pending teacher's replacement format.

Prototype direct use: unzip and open `lesson.html` in browser without a server. Do not try to use Curriculum Transfer with this ordinary zip. The prior assistant reported interaction and MathJax QA; no claim of production quality until teacher feedback. Test any revisions in Chrome-compatible browser and **print to PDF screenshots**, checking each page with content bounds, page count, student workspaces, and no clipped MathJax. Do not use image-gen to replace editable HTML/CSS structure.

**Usability consideration:** Actual CSS may be more efficient if prototype scope first focuses on typography, note cards, EX/YTI, warm-up print, generic rectangle and diamond. Keep rest available for critique. Avoid visual overload and giant gratuitous title boxes.

## 8. Source and file access / safe transfers (important)

- Teacher's local GitHub workspace is mirrored to **Google Drive**. Search **connected Drive mirror** before requesting uploads. GitHub is **not** the source for all apps: **CPM_Tools is a local installed app** accessible through Drive. Teacher keeps GitHub Desktop control. Search both current Drive files and relevant `memories`/`maps_memories` contracts as appropriate; verify production version with metadata/hash.
- Current local runtime seen in browser: `http://127.0.0.1:57220/` (browser address is not remotely accessible by assistant; use Drive mirror). Actual folder example `CPM_Tools/banks/algebra1/warmups/index.html`.
- Current known **Drive file IDs** recorded in this chat for bank lookup (reverify; IDs are pointers, not evidence of install state):

```
CPM_Tools/banks/algebra1/warmups/index.html          1C4_eq8gQui4QG9CpxphxnOn_3F3A-ujV
CPM_Tools/banks/algebra1/warmups/app.js              1aAujUMHLje0hlOHBQfxUwXao3QuSkaIn
CPM_Tools/banks/algebra1/warmups/style.css           1Drwr8pW80dfoHU8TlJfCSKyrJ4SDDtyK
CPM_Tools/banks/algebra1/warmups/spirals.js          1xPTAD0ihUKYCcJ4pypBrzFIqbpIm34Vt
CPM_Tools/banks/algebra1/warmups/spirals.css         1guBW_1f9tAiX7Pfp5f0TDy5lMRn2Fzfb
CPM_Tools/banks/algebra1/warmups/spiral_families.json 12m0pAw4QHVMCfQSUEFpAFX-GXeTNFBhQ
CPM_Tools/app/server.py                             1iu4UsY7atJanV18JA5VdtIVn-SMbs7xL
```

- Some source records/downloads were staged in the conversation work container; next chat **cannot assume previous sandbox paths will mount automatically** unless attached or verified. This handoff contains the actual CSS ZIP to remove that dependency.
- Production repo patch deliverable policy: **ONE verified GitHub/Curriculum Transfer ZIP** (Local Only), approved root `cpm_tools` for CPM_Tools files as shown in actual current manifests, `maps_memories` root for shared conventions if explicitly desired. Do not separately present standalone PM/CSS/HTML as extra production deliverables unless teacher explicitly asks. **Exception for CSS critique**: teacher explicitly asked for a **regular ZIP (not Transfer)** containing one HTML and CSS folder. This HANDOFF ZIP is also a non-transfer documentation package.
- Transfer contract current schema 3 uses `TRANSFER_MANIFEST.json` and `payload/<root>/<relative paths>`, with exact `expected_existing_sha256` for replacements. Reads only `_curriculum_transfers/downloads/`. Local Only apply+verify; no commit/push/pull. User path of launcher in their machine: `/Users/tnezki/GitHub/memories/Tools/curriculum_transfer/Apply Curriculum Transfers - Local Only.command`. Only package paths supported by `approved_roots.json` (included under `reference/`); verify live approved roots in current runtime. Student-specific Portfolio info must never be in a transfer.
- `LOCKED_BUILDER_UI_CONTRACT.txt` and `QUESTION_FRESHNESS_CONTRACT.txt` included under reference; read before modifying Builder/banks. Source of UI reference: `memories/_tool_mirrors/CPM_Tools/` (mirror). Actual local installed files take precedence when verifying hash.
- MathJax must be correct for algebra and fractions. Relevant note: previous assistant had to repair a missing script on server routes; test server whitelist. Graph Tool for diamonds, generic rectangles for factoring.
- Existing approved learning goals / assessment banks: teacher provided `https://tnezki.github.io/algebra/pacing/algebra1_learning_goals_grading_reference.html#principles`. Approved assessment banks are **APPROVED** (teacher said explicitly), but Q4 student questions are selected from new warm-up bank, not direct duplicates of assessment items. Chapter 1–4 bank files and lesson goals/ToC are mirrored in Drive. Preserve teacher review history. Course catalog 102 lessons.

## 9. Resource catalog — current status and exact Drive locations

### Sync status and source priority

Teacher is syncing **nearly 20 GB** into connected Drive under the breadcrumb:

`Google Drive → My Drive → ~Curriculum → All Classes Resources → Resources`

At latest check this `Resources` root had **seven visible top-level folders**; more syncing. Especially **`pods`**, holding **~30 years of classroom warm-up ideas**, had **NOT** appeared under this particular root as of Nov 21. Other Drive folders named `PODs`/`POD's` that were located were unrelated. **Do not misidentify them**. Once `pods` appears, treat as **highest-priority authentic classroom source**, de-duplicate its strategies against catalog; older user-tested prompts may be far better than generic AI-generated items.

**Known exact folder IDs:**

```
Resources root:            1-6gMilnwZQHF38Cu7vFWjfghPMGdvw6N
Inquire Sources:           16oUeJ2qZKQL07MACCbvw9dLLI0NjUJ6W
scanned at mhs:            1TDaxiiG1qbwrGBo30iujvrTsKmhKBJeC
exeter:                    0B6fznOHK0RHAV1pZei1rMlpDLVk
```

Other visible top-level folders in screenshot: `algebra 2 Textbooks`, `common core stuff`, `Course 3 Textbook`, `exeter`, `Inquire Sources`, `Inquiry Structures`, `kuta`, `kuta (1)`, `pods` (screenshot showed pods empty/sync status). Connected Drive tool results sometimes showed only 7 root items and not yet synced `pods`. User believes last large folder not fully transferred. Continue checking without conflating screenshot with synced data availability.

### Identified scanned / readable resource files

```
Exeter Mathematics 1 (Math1All.pdf)       0B6fznOHK0RHAeEs5OWp4blVGYUU
Exeter Mathematics 2 (Math2All.pdf)       0B6fznOHK0RHAS3BiZDNhNnB0amc
Exeter Mathematics 3 (Math3All.pdf)       0B6fznOHK0RHAMERMTEVMNEFXNE0
math warm ups.pdf                         1Na41Ji239QU7Q5SK1GoKoc4Pmy6976gJ
logic fun.pdf                             1ZZbnf447JpsUDWg7LeJo8rtHTJntGn3j
problem of the week.pdf                   1ug5AjqbGvIlJRKyQiA2pebyNT_7r4aRP
more problem of the week.pdf              1imECjPTOuZ-Goy7PIPRWA29MNP30P2JS
math for smarty pants.pdf                 1ukflycTdI2khiwHc4AxSegSeFUten7Y2
A Visual Approach to Algebra.pdf          1YJgVeAeBIYB1VJcKRjiK7rvVjg-G9Vtc
algebra writing activities.pdf            1hh-EumlwPVC5-uDRAuDAHUc4056zg2w6
what's wrong with this picture-geometry.pdf 1eRHhxcYO9ncrbCso-L33hEArFToNUwO1
I hate math book.pdf                      1hWVppUBHH3nP7YHSBrC2pyI6sN4M3Cuu
```

- `math warm ups.pdf` ~93 pages; `logic fun.pdf` ~44 pages; `problem of the week.pdf` ~78 pages; `math for smarty pants.pdf` ~128 pages; `A Visual Approach to Algebra.pdf` ~160 pages. Many scanned PDFs are **image-only**: Drive fetch may return title/bytes but **no actual text**. **Render pages visually** per PDF workflow; don't hallucinate problem content from filename or trust an automatic title alone. Resource sources are inspiration/templates; create ORIGINAL, mathematically precise student questions and source catalog metadata, not mass-copy entire copyrighted books into public questions.

### First-pass verified ideas with recorded references

These are **candidate thinking structures** from prior survey (specific numbers/pages below are useful revisit pointers; check visually before enshrining lesson-specific question):

| Source / page or number | Mathematical structure | Possible role |
|---|---|---|
| Exeter Math 1 #13 & #18 | Number tricks; why an outcome follows | expressions, functions, conceptual transfer |
| Exeter Math 1 #20 | Determine if claimed result is impossible | equations, properties, reasoning |
| Exeter Math 1 #7 & #11 | Compare valid procedures | distributive method, rectangles |
| Exeter Math 1 #5 | Detect missing information in a model | equations, modeling |
| Exeter Math 2 opening #1–3 | Change a condition and test invariant/conjecture | areas/quadratic patterns |
| Exeter Math 2 #8–10 | Build a function from situation | Monday function notation |
| Math Warm-Ups PDF p. 32 (WU #22) | Missing information / changing quantities | Q5/Q6 transfer, systems |
| Math Warm-Ups p.19 (WU #11) | Number path, conditions, tricky repeated patterns | puzzle/spiral |
| Math Warm-Ups p.9 (WU #1) | Create a valid situation for quantities | modeling |
| A Visual Approach to Algebra p.16 | Match graph to situation + justify | function representation |
| Same p.26 | Compare rate-of-change behaviors | linear/nonlinear/exponential |
| Math for Smarty Pants p.16 | Repeated number process, investigate pattern | conceptual |
| Same p.65 | Predict a hidden outcome from numbered-card procedure | puzzle |
| Problem of the Week pp.11–12 | Count paths systematically | sequences and algebraic structure |
| Same pp.12–13 | Pascal triangle links to expansion | later polynomial reasoning (not early prerequisite) |
| More Problem of the Week p.56 | Equivalent arrangements / counting | conceptual |
| Same p.75 | Express total quantity from related measures | application/rates/functions |
| Algebra Writing Activities p.8 | Counterexample to a claim | integer operations/inequalities |
| Same p.13 | Compare two equation methods; identity vs contradiction | solving |
| Same p.18 | Interpret slope and units in context | Monday modeling/graphs |
| Same p.24 | Pick graphing/substitution/elimination and justify | systems (after methods taught) |
| Same p.36 | numerical fractions and rational expressions | later, not early Algebra 1 |
| What's Wrong with This Picture? p.8 | Find wrong mathematical claim / panel | visual error analysis |
| Same p.30 | diagrams: areas/perimeters inconsistent | area models |
| I Hate Mathematics Book p.21 | sampling and representativeness | statistics |
| Same p.31 | handshake-counting table and rule | growing patterns/functions |
| Same p.43 | equal areas vs volumes | Monday or Smarty Pants |
| Same p.79 | unexpected physical puzzle, challenge assumptions | substitute day |

**Catalog next step:** Build a *structured inventory* (not yet modifying repository) fields: source file ID/path + PDF page/actual problem; lesson/I Can tags; four-family type; 3–8 minute warm-up vs Smarty Pants vs Monday vs sub; needed graph/diagram; original question format; variation axes; teachability/progression; originality and copyright treatment; solution proof; ready/review/defer status. Record strong source links and quality, not just titles. Priorities: Algebra Writing Activities, Exeter, visual algebra, Math Warm-Ups; puzzle sources sparingly for routine Q5/Q6, more freely for Monday/sub.

**Quality insight from past passes:** A short “change one condition,” “predict before computing,” “cannot happen,” “missing information,” “match the graph,” or “write a counterexample” often has more conceptual value than a long word problem that is just identical multiplication. Don't force every lesson into arbitrary four templates if a genuinely meaningful task is unavailable; flag for authoring.

## 10. Historical implementation chronology / known quality failures

This context helps prevent regression. Most significant steps in past conversation:

1. Initial Modified Lesson Builder pilot attempted. Teacher backed up CPM Tools; assistant originally delayed due to uncertainty of current source. Pilot created Q1/Q2 Q3/Q4 and some classroom selection UI, but user later steered toward **prebuilt bank + deterministic assembly**, not on-demand generation.
2. Teacher asked for a list by solving, diamond/factoring, spirals, extensions, all with MathJax and number-swappable families. Some assistant changes placed new bank incorrectly; teacher insisted bank **belongs under Algebra 1 Banks Tool**, not generic/shared external hierarchy.
3. Teacher corrected ugly printed solutions, meaningless directions, leading `+` signs, `1x` and `-1x` etc., and taught method mismatches. Solutions need exact layout, clear alignments, all integer solution values, valid algebra, generic rectangles.
4. Early server transfers had failed SHA-256 of `CPM_Tools/app/server.py`. Later new Q3 tab initially appeared blank because server whitelist didn't register JS/CSS/JSON; repair was a targeted server whitelist transfer. Avoid declaring browser QA passed if actual localhost route blocked.
5. Q3/Q4 bank: 102 lessons, 204 spiral families, 8 versions each; lesson-specific quality audits and MathJax fixes done. Teacher reviewed and said questions seem workable.
6. Q5/Q6 extension bank first 2 choices per spiral, then 4 per spiral = 816 families/6528 questions. Despite uniqueness claims, teacher screens showed **nearly identical mathematical tasks** and an unresolved literal `x={x}` bug. Teacher corrected target to **4 extension families TOTAL per LESSON** and wanted to find better sources, particularly 30-year `pods` archive.
7. Several resource catalog passes found Exeter, scanned puzzle and warm-up collections. No production bank changes during final catalog passes; still source exploration.
8. Teacher clarified Monday Q1/Q2 must stay, Q3 can be function notation parts a/b/c with different representations; optional puzzle Q4. Teacher clarified practice 12 set and finalized component order and “Smarty Pants” term.
9. Last assistant created **regular non-transfer CSS critique ZIP** with single `lesson.html` and `css/` directory, full pretend lesson. Teacher paused before opening to request this detailed handoff. **First task is to receive his critique and make CSS changes**, not to restart work from step 1.

**Recent transfer filenames (HISTORICAL; do not blindly reinstall):**

```
Algebra1_Warmup_Q3_Q4_Server_Whitelist_Repair_20261121_GITHUB_TRANSFER.zip
Algebra1_Warmup_Q3_Q4_Spiral_Quality_Pass_20261121_GITHUB_TRANSFER.zip
Algebra1_Warmup_Q5_Q6_Linked_Extensions_20261121_GITHUB_TRANSFER.zip
Algebra1_Warmup_Q5_Q6_Four_Family_Rebuild_20261121_GITHUB_TRANSFER.zip
```

Actual teacher screenshots showed Q5/Q6 tab functioning after transfers. **Install status of every individual ZIP has not been independently reconfirmed here**; re-fetch current mirror before packaging another patch.

## 11. Quality/QA gate for next work

1. **Correct lesson alignment:** I Can from official lesson, actual learned methods only, no premature discriminant/standard deviation/notation, MathJax and worksheet correctness.
2. **Distinct student thinking:** Each Q5/Q6 option genuinely different. Review actions, representation, mathematical reasoning; a unique string with altered numbers is insufficient.
3. **Template integrity:** Scan all instances for `{x}`, unresolved `{{..}}`, `1x`, `-1x`, `0x`, `x^1`, unwanted leading `+`, malformed LaTeX, math errors. Check worked solution notes align with operations, factoring models use generic rectangle, not AC.
4. **History and freshness:** Do not count previews as use; log publication, prevent reuse across lesson types and practice formats; check before output.
5. **CSS prototype:** visual page-by-page QA screen + print, no clipping, correct 2 warm-up pages, adequate workspace, teacher/student controls, math renders offline, multiple practice format views use the same 12-question set. Avoid filler directions.
6. **Production transfers only:** verified current expected hashes, valid approved root, whitelist changes if necessary, clean save/publish paths, no unexpected changes to other Algebra 1/Physics/Calculus tools, never GitHub write.
7. **Report truthfully:** if browser test unable to run, say so. No claim of “passed” without execution.

## 12. Open decisions — do NOT preempt user

- **Learning Focus / Notes** final visual format is still forthcoming from teacher (he specifically has a new design).
- Exact teacher-controls UX for Modified Lesson Builder beyond established left/right contract, daily lesson editor, AI-request component editing workflow to be agreed in pilot.
- Q5/Q6 four-family exact mapping when Q3/Q4 refer to different lessons; need design to connect student task to selected spiral while maintaining four distinct options **per lesson**, not eight per lesson.
- The 12-question practice selection algorithm: current/spiral split in first 8 by lesson; criteria for replacing CPM Review & Preview problems 9–12; avoid MC; teachable variation strategy.
- Full `pods` archive is not synced; resource mapping provisional.
- Optional Monday Q4 type and Monday main performance-task connection can be refined after resource review.
- Production CSS token naming / `maps_memories` location after teacher's critique; don't prematurely publish shared CSS.
- Full year prepopulation sequencing and teacher authorization to apply packages are future phases.

## 13. Suggested first reply in next chat

> “I read the complete Modified Lesson Builder handoff and have the exact CSS prototype ZIP. We can critique the standalone HTML/CSS first without touching CPM Tools. I’m preserving the latest decisions: Monday Q1/Q2 plus multipart function-notation Q3; Q5/Q6 four extension families per lesson total; one 12-question practice set across all activity formats; and the agreed default sequence. Show me what you want changed in the prototype.”

Then **do actual edits** when the teacher provides screenshots/comments. Do not make them re-explain anything already documented here. While waiting for `pods` sync, continue cataloging user-provided resources when asked. The next result is another regular standalone critique ZIP; **production code edits require one verified Local Only GitHub Transfer ZIP**.

---

**End of handoff.** The original standalone prototype ZIP and current contract references are bundled in this handoff archive to make next-chat recovery independent of old sandbox links. This handoff describes user decisions as of November 21, 2026; newer teacher instructions always override it.
