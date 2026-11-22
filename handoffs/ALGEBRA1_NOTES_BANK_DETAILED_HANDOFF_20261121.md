# ALGEBRA 1 — LEARNING FOCUS / NOTES BANK
## Complete next-chat handoff — November 21, 2026 (America/Detroit)

**Project:** Textbook Extraction → Curriculum Build → CPM Tools (Algebra 1 pilot)  
**Next task:** Build the **Learning Focus / Notes content bank**, using the now-accepted Algebra 1 Bank Directory, the teacher-approved parts of the Modified Lesson style, the official lesson learning goals, and verified CPM lesson resources.  
**Current task status:** This document is a **handoff**. It creates **no new Notes bank content, no new application route, and no code changes**. The user explicitly says the Bank Directory setup now seems fine; do **not** continue troubleshooting that screen unless a fresh defect is reported.

> **New-chat instruction:** Read this entire handoff and, for provenance, `ALGEBRA1_MODIFIED_LESSON_BUILDER_ORIGINAL_HANDOFF_20261121_ARCHIVE.md` in the same handoff folder. Then inspect the latest actual files in the connected Google Drive mirror and the stored V7 student style. Begin **building the Learning Focus / Notes bank**. Do not ask the teacher to repeat settled design decisions; do not reopen the Bank Directory or rebuild the warm-up bank.

## 0. Quick state and what is already done

The teacher reviewed the lesson-bank landing page and asked that it become a **simple directory of banks**, rather than a chapter-selecting question-review screen. The new directory was installed, followed by a targeted server route repair after `/banks/assessment.html` initially returned `{"error":"Not found."}`. The latest teacher message explicitly says **"the setup seems fine now."** Treat that as the current status.

**Installed transfer evidence, November 21:**

- `Algebra1_Bank_Directory_Navigation_20261121_GITHUB_TRANSFER.zip`: successful Local Only run **21:10:03**, 4 operations: replaced `CPM_Tools/banks/section.html`; created `CPM_Tools/banks/assessment.html`, `CPM_Tools/banks/component.html`, and `maps_memories/handoffs/ALGEBRA1_BANK_DIRECTORY_NOTES_NEXT_20261121.md`. Post-apply verification **PASS**.
- `Algebra1_Bank_Directory_Route_Repair_20261121_GITHUB_TRANSFER.zip`: successful Local Only run **21:14:48**, replaced `CPM_Tools/app/server.py` to permit the new route. Post-apply verification **PASS**. Both transfers ran **LOCAL ONLY; no Git actions**.
- The original `/banks/section.html` had full chapter/section/lesson selectors and review/export functions. Those functions were **preserved in** `/banks/assessment.html`; the directory now routes to that existing bank instead of duplicating its logic.
- The Warm-Up Bank remains at `/banks/algebra1/warmups/index.html`; new directory links are a navigation change, not a content-bank rewrite.

**Current bank-directory routes** (confirmed by reading its HTML):

| Navigation tile | Target route | Current status |
|---|---|---|
| Assessment & Reference | `/banks/assessment.html` | Existing content moved to its dedicated route; tested by user after route fix only insofar as they say setup seems fine |
| Warm-Ups | `/banks/algebra1/warmups/index.html` | Existing working bank |
| Learning Focus / Notes | `/banks/component.html?bank=notes` | **Setup placeholder only: NEXT BANK** |
| EX / YTI | `/banks/component.html?bank=ex-yti` | Planned placeholder |
| Launch | `/banks/component.html?bank=launch` | Planned placeholder |
| Smarty Pants | `/banks/component.html?bank=smarty-pants` | Planned placeholder |
| Practice Sets & Activities | `/banks/component.html?bank=practice` | Planned placeholder |
| Reflections / Exit Tickets | `/banks/component.html?bank=reflection` | Planned placeholder |

The generic `component.html` currently describes planned banks and says no lesson content is populated. **Replacing that placeholder with a real Notes bank** is the next implementation task, but first inspect current routing, data, and style integration. The other planned placeholders should continue to work until their own banks exist. The directory has **no chapter selector or export button**: that is deliberate.

## 1. Governing source and instruction priority

This handoff was built after multiple source checks. If two historical documents conflict, **newer teacher decisions override older prototypes and earlier handoffs**. The priority is:

1. Teacher's direct recent instructions, especially Notability print behavior, source-bank distinction, and simple directory.
2. Actual **latest installed** `CPM_Tools` files in the connected Google Drive mirror (verify each file, not historical GitHub assumptions).
3. Current `maps_memories` style/architecture handoffs, especially the approved V7 **style reference** and the bank-directory notes handoff.
4. Official CPM source lesson, learning goals, Methods & Meanings, and previously approved teacher curriculum.
5. The **original November 21 handoff**, retained separately as historical context. It describes the start-of-day CSS prototype, not the final approved visual style; its old four-total Q5/Q6 proposal was subsequently superseded.

**Important:** A separate existing resource titled `Algebra_Notes_HTML_Structure_Reference.md` describes a different Unit 1 Algebra Notes PM framework (v6.16, 9pt text, elaborate opening sequence). It can be consulted *as a reference* if useful, but must **not** silently replace the later Modified Lesson / Notability style, or impose WTC, vocabulary sorting, large blank pages, and other structures the teacher has not approved for this Notes bank.

## 2. What the whole system is for

Build a **prepopulated year of Algebra 1 lesson components** so the teacher can select/modify/approve before students see them. The bank supplies lesson-authored, reusable instructional content; the **assembler** combines selected components into saved lesson recipes and paginated Notability/offline student documents. Avoid creating parallel builders, rebuilding a lesson every day, or storing the same content redundantly in every layout.

- Algebra 1 has **102 source CPM lessons** under the current approved pacing/learning-goal plan. The user also references 30 section learning goals and 12 chapter entries (including statistics moved into Chapter 12). Do not confuse relocated planning categories with original lesson identifiers; verify the actual curriculum catalog before mass-generation.
- The installed normal Builder, Assembly/page engine, existing Library, assessment/question bank, warm-up bank, student lesson files, and teacher review state must remain intact. A separate *Modified Lesson Builder* is an eventual component assembler; it is **not** this Notes-bank deliverable.
- The teacher controls all Git activity with GitHub Desktop. Curriculum Transfer applies only local file changes with verified source hashes; no commit/push/pull/PR by the assistant.
- The student's pages are used extensively in **Notability**. This affects header size, writing space, text/highlighting ability, and PDF performance, not just aesthetics.

### Proposed separation into **eight bank roles** (directory already reflects these)

1. **Assessment & Reference** — teacher-approved direct skill/evidence questions and extensions, summative multiple choice, and CPM Review & Preview (R&P) **as reference**. The assessment bank is not the Notes source file or the automatic warm-up Q4 question bank.
2. **Warm-Ups** — Q1/Q2 fluency choice pool; source-lesson Q3/Q4 spiral families and linked optional Q5/Q6. A source lesson contributes review opportunities **to future lessons**.
3. **Learning Focus / Notes** — **our next build**. Today's verified lesson I Can, immediately relevant vocabulary and definitions, Methods & Meanings content, concise explanation/representation. Teacher-editable.
4. **EX / YTI** — current lesson worked example + closely matched You Try It; alternatives, number swaps, staged solution. Separate from Notes and Smarty Pants, though Notes may refer to the relevant concept.
5. **Launch** — 2–3 distinct teacher-selectable CPM Launch/Explore-based 15–30-minute investigations.
6. **Smarty Pants** — optional **today's-lesson** application, interesting investigation, design/model/decision challenge. Not a repackaged earlier-skill Q5/Q6.
7. **Practice Sets & Activities** — one lesson-specific **12-question** set shared by Projection Sets, Rounds, Find Someone Who, Stations/Task Cards/Whiteboards, not independent sets for each format. Projection Set prints **two questions per page**.
8. **Reflections** — genuine **3-minute** self-assessment/reflection; simple two-per-page black-and-white printed format, 1–4 confidence scale, choose just one of four broad prompts, **not another math question**.

Default lesson order already agreed: **Warm-Up → Learning Focus / Notes → EX/YTI → Launch → Smarty Pants → one selected Practice format → Reflection**. The teacher can omit/reorder for a particular lesson, especially Launch-before-EX when discovery warrants it. This **does not** mean the Notes bank should store or render those other components.

## 3. Exact mission for the Learning Focus / Notes bank

**One reusable, editable, lesson-specific content record (plus optional alternative notes/versions) per actual CPM source lesson**, not a giant generic topic note for a whole chapter. At minimum, the pilot should support:

- **Learning Focus / I Can:** Use the verified **lesson-level** I Can; show the actual target before or alongside the content. Preserve teacher-approved exact language; teachers can accept/modify and record a new approved revision. Avoid substituting a broad section I Can for a specific lesson I Can.
- **Relevant vocabulary:** Only terms needed for the **current lesson**. Definitions should be accurate, concise, student-readable and **text-highlightable**, not baked into an image. The teacher said vocabulary definitions should be visible so students can highlight them.
- **Methods & Meanings:** Include/accurately adapt **only the CPM Methods & Meanings or Math Notes that actually support this lesson**. Verify provenance in the real lesson/source cards; do not indiscriminately append all section/chapter notes or invent a CPM quotation.
- **Concise instructional notes:** Key meaning, representation, conventions, a purposeful illustration/example *only when useful*; no generic filler, long motivational introductions, decorative essays, unrelated prerequisite lectures, or formula dumps.
- **Mathematical models and figures:** Prefer canonical existing diagrams or generate with the approved district Graph Tool where appropriate. Generic rectangles must label factors and terms correctly; MathJax used for equations and symbols; graph axes/units/labels preserved. Never hand-draw a fake diamond in CSS or substitute a misleading diagram for an actual source image.
- **Student and teacher separation:** Student view contains instructional content and writable/annotatable space; teacher view may contain author notes, guidance, content provenance, and revision metadata. Never leak answer-only controls, edit instructions, or mockup commentary into student/printed pages.
- **Editable at all levels:** Teacher can edit text/definitions/blocks, omit a block, rearrange, choose an alternate, or ask for an AI revision of a selected block. Changes must be stored as a revision, not silently overwrite approved shared content. Support marking a specific block as needing improvement with a teacher note.
- **AI modification request:** Capture existing lesson/goal, selected Notes record/block, relevant CPM source references, approved CSS style reference, what the teacher wants changed, and selected lesson's current text. AI Request should return a targeted reviewable change; it must not regenerate the whole lesson or mutate assessment/warm-up banks.

**Do not decide the final content-length formula in advance.** Some lessons need a compact notes page, some require representations or Methods & Meanings. Use actual source and learning goals; make page length a result of purposeful content, not an artificial requirement to fill a page. No need to create excessive writing space at expense of instruction or to remove useful borders/shading in the name of minimalism.

### Strong proposed record schema — blueprint, not yet installed

The implementation can revise this after inspecting existing data contracts. This shows the semantics needed, not mandatory literal JSON field names:

```
notes_record_id             stable unique ID; never derive identity from display order
course_id / source_lesson   algebra1 + canonical CPM lesson number
curriculum_goal_id          approved learning-goal/section reference
lesson_i_can                exact verified lesson-level I Can + source/provenance
style_ref                   maps_memories/standards/algebra1_modified_lesson_style_20261121_v7
blocks[]                    ordered, typed content blocks, each stable block_id:
   focus | vocabulary | method_meaning | explanation | representation
   student_html_or_structured_content; MathJax and figure refs
   source_ref (file/card/page and source kind)
   teacher_only_commentary (never printed in student view)
version / revision_history  timestamp, author/AI-request provenance, change summary
review_status               draft | needs_work | teacher_approved
teacher_feedback            block-specific comments and requested change notes
flags                       skill tags, prerequisites, figures, print/style checks
```

Separately maintain a **lesson assembler recipe** (future work) pointing to selected `notes_record_id` + revision, not a duplicate of every Notes HTML block. The Notes bank's teacher approval should be **content approval**, and previewing/number-swapping in unrelated banks should not affect Notes status.

### Example target for the pilot (content to verify; not a ready lesson)

**Lesson 3.2.3** has already been used as a visual example. The latest lesson-level focus in the existing warm-up source bank is: **“I can multiply a trinomial by a binomial using a generic rectangle and combine like terms.”** Teacher explicitly wanted **trinomial × binomial using a 3-by-2 generic rectangle** as the model, with trinomial × trinomial introduced later. Do **not** let the older broad label “binomials and the distributive property” displace the teacher's more recent instructional focus.

For that pilot Notes record: confirm its exact approved target and applicable Methods & Meanings in canonical CPM source/plan; include only useful vocabulary such as `generic rectangle`, `partial product`, and `like terms` **if those are actually needed/approved in source context**; show one accurate labeled 3×2 representation when it helps. Do not manufacture a full lesson from this example alone. The teacher previously rejected repeated distributive-property exercises and overly cramped EX/YTI; EX/YTI is separate and should not take over Notes.

## 4. Visual standard: what was approved, what was not

**Canonical style reference already retained in:**

`maps_memories/standards/algebra1_modified_lesson_style_20261121_v7/`

It contains `README.md`, `DIAMOND_AUTHORING_RULES.md`, `lesson_reference.html`, `css/01-tokens.css`, `css/02-lesson.css`, `css/03-print.css`, `css/04-assembler.css`, a Graph Tool sample diamond asset and verification metadata. It was added by the reference-only `Algebra1_Style_Reference_Diamond_QA_20261121_GITHUB_TRANSFER.zip`. **It does not mean the production Builder adopted that CSS, or the example notes content was approved.** Inspect the actual style files before implementing.

**Teacher-approved style direction:**

- Compact headings such as `3.2.3 Learning Focus / Notes`, **not** enormous “Core Connections Algebra 1 · Design Prototype”/page badge/student packet banner.
- Blue-gray/bluish palette, **selective light-blue shading**, thicker **blue left rule** for important sections; purposeful borders/sections to organize and highlight math, not indiscriminately bare pages.
- User specifically **preferred the original, more structured Learning Focus / Notes mockup** over the subsequently stripped/sparse Notes page. Keep useful visual hierarchy; don't interpret “no fluff” as “no borders, no shading.”
- Preserve maximum usable **open Notability writing space**, but no obligatory lined paper, gigantic empty boxes, redundant work zones, or instructional fluff. Place content and blank space intentionally.
- No **Name** or **Date / Period** fields on regular student lesson pages; class work occurs in Notability. A separately printed exit ticket may carry a small name field (not relevant to Notes).
- Student-facing content only; remove prototype commentary, answer-key annotations, assembler choice buttons, and meta-labels. Options and teacher controls belong in the assembler/bank review interface.
- Text and math must be readable and **MathJax equations sized with surrounding prose**; avoid huge black display equations unless emphasis is genuinely needed. Use logical headings/definition blocks and figure sizing.
- **One or two columns only when content has enough space**; avoid cramped parallel columns. Earlier EX/YTI was switched to stacked layout when parallel columns cramped the math. For Notes, preserve readability.
- Test **print/PDF and interactive HTML**; page breaks, clipping, note panels and math typesetting. PDF should behave sensibly in Notability, avoiding unnecessary vector complexity/oversized files where possible.

**Explicitly NOT teacher-approved:** all 3.2.3 prototype question choices, provisional Methods & Meanings/Notes wording, the rest of the lesson activities, and universal fixed Notes page length. The original CSS prototype was the first draft; the V7 style is a *partially approved reference*. Do not claim it is an approved curriculum template in full.

### Historical example of how the teacher gives CSS feedback

1. Oversized branded titles waste page space; use small lesson-numbered headings.
2. Remove name/date fields on student pages.
3. Keep borders, shading and thick left blue border on useful teaching sections; do **not** strip every box.
4. Equations need to match adjacent text size.
5. Number/question on one line; compact I Can band above the question where it applies; solution popups are controls in interactive HTML, not PDF promises.
6. Don't force a two-column activity that compresses diagrams or writing room.
7. No generic I Can text on Q1/Q2 solve/diamond/factoring choices (specific to warm-up; not a rule to omit Learning Focus I Can).
8. Student content is real lesson material, not comments like “Original mockup” or “I can statement here.”

## 5. Content sources and exact places to start

**Do not ask the teacher to upload files already in the connected Google Drive mirror.** The mirror is the local CPM_Tools source for this task, not merely a backup of a GitHub repository. Before coding, re-read the current live file bytes/metadata and source IDs.

### Essential installed source locations

| Asset or contract | Where to inspect / purpose |
|---|---|
| Bank Directory | `CPM_Tools/banks/section.html` — new directory, live route |
| Assessment bank | `CPM_Tools/banks/assessment.html` — old chapter/lesson bank preserved |
| Component placeholder | `CPM_Tools/banks/component.html?bank=notes` — Notes setup; do not break other component placeholders |
| Warm-Up Bank | `CPM_Tools/banks/algebra1/warmups/` — unchanged source-bank architecture; not Notes |
| Server routes | `CPM_Tools/app/server.py` — explicit path whitelist; earlier new routes gave `Not found` until repaired |
| Approved lesson goals | `CPM_Tools/data/algebra1_assessment_plans.json` and canonical Algebra 1 lesson/pacing catalog; confirm exact current file in Drive |
| Original extracted CPM lesson/cards | CPM Tools local textbook/card Library and mirrored original source HTML, especially lesson/teacher Methods & Meanings; verify actual source lesson and provenance |
| Styled reference | `maps_memories/standards/algebra1_modified_lesson_style_20261121_v7/` — inspect actual CSS and HTML before authoring |
| Directory handoff | `maps_memories/handoffs/ALGEBRA1_BANK_DIRECTORY_NOTES_NEXT_20261121.md` |
| Component architecture handoff | `maps_memories/handoffs/ALGEBRA1_LESSON_COMPONENT_BANKS_NEXT_CHAT_20261121_v1.md` |
| Warm-up QA handoff | `memories/_question_structure/handoffs/Algebra1_Warmup_Followup_Passes_20261121_v2.md` |
| Other resource research | `memories/_question_structure/catalogs/` holds POD, broad resource, deeper question-structure, and extension/Smarty Pants catalogs |

**Verified current Drive pointers as of November 21** (file IDs not guaranteed forever, re-search if moved):

- Bank directory `CPM_Tools/banks/section.html` → Drive `11XsoNoxbUG-GlWvQsoEQxyFJdzQyGQf6`.
- Notes component placeholder `CPM_Tools/banks/component.html` → Drive `1nSXAQmZG2Qrai_X9Tmdxees7iD2ZRTEi`.
- Dedicated Assessment page `CPM_Tools/banks/assessment.html` → Drive `1AucLgCeoHZ0VY7SlCp3as2Zuw68T7-Wz` (large file; use metadata/raw fetch rather than forcing a full inline text response).
- Warm-up review `/banks/algebra1/warmups/index.html` → Drive `1C4_eq8gQui4QG9CpxphxnOn_3F3A-ujV`; data `spiral_families.json` → `12m0pAw4QHVMCfQSUEFpAFX-GXeTNFBhQ`.
- V7 style directory → Drive folder `1m9fCb31hIGCPAUfWgs_IHwro2x081Cic`.
- Original wider resource root `~Curriculum → All Classes Resources → Resources` → Drive folder `1-6gMilnwZQHF38Cu7vFWjfghPMGdvw6N`; `pods` later appeared and was cataloged under `1Z9Y3wvzX9wbs4rjhNeaLbPlB119U8Y4Q`. Broad resource catalogs already exist; **resource cataloging is not the next task**.

**Relevant pacing reference:** `Algebra 1 — Learning Goals, Grading Reference, and Pacing` was previously found at Drive file ID `1T6bHxg4HMuj382ymn3vB2HbI33LtojOb`; the teacher also used `https://tnezki.github.io/algebra/pacing/algebra1_learning_goals_grading_reference.html#principles` as a learning-goal reference. Reverify against the actual installed lesson data rather than treating a web copy as primary.

### Source fidelity rules

1. Identify the exact original CPM lesson; confirm title, I Can, Methods & Meanings, diagrams and teacher intent.
2. Associate every Notes block with a verifiable source reference (CPM card/lesson, Methods & Meanings, teacher-approved plan, or original teacher-authored content). Mark source adaptations and AI-written explanatory text accurately; do not describe original text as CPM when not verified.
3. Preserve provenance for licensed/purchased teacher material; keep within authorized local/synced lesson workflows; don't republish whole copyrighted textbooks publicly.
4. Separate a content finding from a source guess. Missing details should remain flagged for verification, not filled with invented “likely” Math Notes.
5. Use educational judgment: select what supports **today's** student thinking. Other interesting material belongs in Launch, Smarty Pants, or future Notes, not automatically appended.

## 6. Warm-up architecture and QA — keep it stable, don't rebuild

The **original** November 21 handoff contained an interim proposal for four extension options **per lesson total**. This was explicitly revised later after discussion. **Latest authoritative implementation to preserve:**

- 102 source lessons × 2 source spiral families = **204 Q3/Q4 spiral families**.
- Each source spiral family offers **four different optional extension approaches** (Application, Conceptual/error, Connection/representation, Deeper reasoning) = **816 extension families**. These are **not** 816 mandatory student exercises.
- Each source spiral family has **8** prepared variants.
- Each extension family now has **4 active numbered versions and 4 archived/recoverable versions**. The teacher said they were content with four numbered extension versions for warm-ups.
- Q1 = linear/quadratic solving choice (when taught), Q2 = diamond/factor choice; four individual solution popups on first page when both pairs are available, **no I Can statements** on these fluency choices.
- The source lesson stores spirals for later lessons. For destination lesson 3.2.3, Q3/Q5 come from previously completed 3.2.2. Q4/Q6 come from a previously taught skill; for prebuilt lessons Q4 uses a **balanced random earlier source**; later Portfolio may replace Q4 and Q6 as a matched pair. This future assembly logic is **not yet connected**.
- Q5/Q6 optional student extension of Q3/Q4; should be meaningful, not just harder arithmetic, linked to parent skill. **Smarty Pants** instead applies *today's* learning.
- Teacher approvals, review notes, source/instance IDs, parent links, and publication-question history are important; don't erase or reinterpret them.
- Last follow-up bank pass reported 76 remaining similar A/B template cases, with exact active duplicate check and MathJax check passing. They are **not automatically teacher-approved** and the assistant did not re-solve every legacy instance by hand. This is known QA debt, **not a Notes-bank blocker**.

Monday: retain Q1/Q2 and use a multipart Q3 function-notation/modeling question with table/graph/equation representation, and optional short Q4 puzzle. Continuing a lesson must not advance the instructional position; substitute days use independent suitable activities. Not relevant to Notes authoring except that the future assembler must keep these exceptions.

## 7. What to build first in the next chat — executable work plan

**Do not begin with a broad design interview**; user has asked to start the Notes bank. Proceed with verified sources and a pilot, making reasoned defaults where the data is complete.

### Pass A — Verify content and integration sources

- Fetch latest installed `CPM_Tools/banks/section.html`, `component.html`, `app/server.py`, local lesson catalog and approved I Can references from connected Drive. Check actual route whitelist and current file hashes; earlier “Not found” errors came from the server path whitelist.
- Inspect V7 CSS reference and its offline `lesson_reference.html`, especially the originally favored structured Learning Focus/Notes design. Review teacher screenshots/feedback in the handoff and, if needed, in available conversation attachments.
- Inspect the canonical CPM lesson 3.2.3 cards + teacher Methods & Meanings and approved lesson-goal record. Do not simply derive notes from the already generated warm-up review text.
- Check that source lesson number mapping is stable. For all 102, identify sources and missing records; retain a source/coverage report.

### Pass B — Build a functional, integrated Notes bank pilot

- Create a **Notes-bank route** accessible via the existing `Learning Focus / Notes` directory card; preserve all other card routes. Candidate implementation directory is `CPM_Tools/banks/algebra1/notes/`, but verify current route and server conventions before fixing final path. Do not install at a guessed route if the server won't serve it.
- Teacher-facing chapter/section/lesson selector, a clear per-lesson learning target, ordered notes block previews, source citations/provenance, approval/needs-work status, and editing controls. Avoid overly elaborate meta UI; treat Notes as its own content bank, not an assessment question list.
- Versioned storage; an **AI change request** action that captures block+goal+source+style+teacher request, using existing CPM Tools request patterns where available. Do not promise a live backend integration unless actually implemented and tested; a valid downloadable AI Request package can be an initial step.
- Demonstrate a **real, verified lesson 3.2.3 Notes record**, not placeholders. Optionally include a second lesson with different mathematical structures after sources are inspected, to show format flexibility.
- Student preview uses canonical blue style and actual MathJax; teacher editing controls/notes don't appear in student mode. Full offline PDF/Notability preview without oversized banners/name fields.

### Pass C — QA and scale preparation

- Check mathematical content and relevance, readable text, vocabulary definitions, accurate diagrams, and Methods & Meanings provenance.
- Test navigation, source links, review flag and revision persistence, content editing, and AI-request payload contents. Ensure all new CSS/JS/JSON assets are allowed by `server.py`; test through the real local route or explicitly report limitation if localhost cannot be reached.
- Render student HTML/PDF pages and check page breaks, MathJax relative size, un-clipped representations and print isolation. Do not invent full 102 authored Notes if only pilot sources were actually verified.
- Prepare a **102-lesson inventory/skeleton** if the catalog supports it, with `draft`, `source-needed`, and `teacher-approved` statuses. Fill only what is confirmed; then build out the full collection in subsequent passes.
- Package the completed pilot and source/QA reports into **one GitHub Transfer ZIP (Curriculum Transfer — Local Only)** using the newest approved root aliases and exact replacement hashes. Teacher installs, verifies, and uses GitHub Desktop manually.

### Teacher acceptance test for the first Notes bank

1. Bank Directory opens → click **Learning Focus / Notes** → real Notes review/editor (not generic placeholder).
2. Choose **3.2.3** → see approved current lesson I Can and *only* relevant vocabulary, Methods & Meanings and concise mathematical explanations.
3. Notes look like the **approved style direction**: compact header, blue left accents and selected blue shading, readable MathJax, highlightable words, open workspace, no unnecessary name/date fields or mockup labels.
4. Teacher can change a word/definition or flag a block, keep revision history and prepare a targeted AI change request, without destroying the approved original.
5. Student preview/print isolates teacher data, renders and paginates correctly; the installed normal Builder, assessment bank, and warm-up bank remain intact.
6. All source citations and any remaining unverified content are clearly flagged, not silently presented as approved.

## 8. Production transfer and file safety

**Single ZIP only.** The user’s Curriculum Build delivery rule: one authoritative `...GITHUB_TRANSFER.zip` link; do not present standalone PM/CSS/HTML/notes files separately unless explicitly requested.

The live `approved_roots.json` previously verified includes `cpm_tools` → `CPM_Tools/`, `maps_memories` → `maps_memories/`, and `memories` → `memories/`. Inspect the current file before the new patch.

Schema 3 transfer format:

```
TRANSFER_MANIFEST.json
payload/<approved-root-alias>/<relative path>
```

Create operations only for genuinely new files; **replace** requires the SHA256 of the exact existing installed file. Never overwrite from a historical ZIP without re-reading live mirror. A package is accepted by **Curriculum Transfer — Local Only**. The teacher initiates the launcher and alone chooses later GitHub Desktop commits/pushes. No remote GitHub writes or student-personal data in the transfer. Avoid a second, confusing standalone deliverable.

Existing installed Builder/Bank may have been modified after this handoff was written; always reverify source and hashes. Root `maps_memories` stores stable contracts/handoffs/style, not active CPM_Tools application code. New Notes bank is authored under the `cpm_tools` approved root once the source is inspected.

## 9. Risks and things NOT to repeat

- Do **not** continue debugging the Assessment route/Bank Directory; two transfers passed and user explicitly accepts setup now. A new report of failure is a separate issue.
- Do **not** regenerate the completed Warm-Up Bank or move its 816 families into Notes. The installed bank is teacher review work, not automatically approved student content.
- Do **not** copy giant assessment MC catalogs, CPM Review & Preview banks, or all chapter Methods & Meanings into a lesson's Notes.
- Do **not** create Notes by simply changing the example question numbers; Notes need lesson-aligned meaning, terms, models, and teaching ideas.
- Do **not** reintroduce giant headings, name/date fields, irrelevant decorative borders, stripped-down unstructured notes, two-column cramped layouts, or fake worksheet ruled lines.
- Do **not** put editable bank/source metadata inside the student-facing document. Teacher controls belong outside the printed packet.
- Do **not** assume an HTML view or JS request works because the source file exists: the prior localhost 404 resulted from `server.py` whitelist. Test actual routes.
- Do **not** conflate the separate, older Unit 1 Notes framework with the Modified Lesson Notes bank without deliberate teacher approval.
- Do **not** claim all 102 Notes are complete, or all mathematical content teacher-approved, if only a pilot was built.
- Do **not** perform GitHub writes/commits/pushes or expose private student data.

## 10. Source documents reviewed to prepare THIS handoff (provenance)

This handoff was reconciled in **multiple reading passes**, not drafted from a conversation summary alone:

1. **Original primary:** `Algebra1_Modified_Lesson_Builder_Complete_Handoff_20261121(1).zip` → `READ_FIRST_HANDOFF.md`, 46,282 bytes, covering 10 components, original CSS, Q1–Q6, the yearlong Builder, source locations, and transfer constraints. A byte-for-byte copy of its handoff Markdown is included alongside this handoff as an **archive**, not as newer instructions.
2. **Original bundle contracts:** `CURRICULUM_TRANSFER_CONTRACT.txt` (schema 3), `LOCKED_BUILDER_UI_CONTRACT.txt`, `QUESTION_FRESHNESS_CONTRACT.txt`, and approved root configuration inside the primary handoff ZIP.
3. **Style transfer:** `Algebra1_Style_Reference_Diamond_QA_20261121_GITHUB_TRANSFER.zip` + installed `maps_memories/standards/algebra1_modified_lesson_style_20261121_v7/README.md`; records concrete accepted style and its limitations.
4. **Warm-up follow-up:** `Algebra1_Warmup_Bank_Followup_Quality_20261121_GITHUB_TRANSFER.zip` → component architecture and follow-up QA handoffs; newer than the original handoff's extension count.
5. **Bank Directory / Notes handoff:** installed `maps_memories/handoffs/ALGEBRA1_BANK_DIRECTORY_NOTES_NEXT_20261121.md`; direct read of live `banks/section.html` and `banks/component.html` from connected Drive.
6. **Transfer logs:** `20261121-211003_Algebra1_Bank_Directory_Navigation...log` and `20261121-211448_Algebra1_Bank_Directory_Route_Repair...log`, both reporting post-apply PASS; user's final "setup seems fine".
7. **Additional separate reference:** `Algebra_Notes_HTML_Structure_Reference.md` (older Base Notes/PM framework; not automatically controlling this project).

The handoff explicitly separates **verified installed state**, **teacher-approved design direction**, **planned functionality**, and **unverified content**. Where historical records disagree, Section 1 provides the governing precedence.

## 11. Suggested exact next-chat user prompt

> Read the complete `ALGEBRA1_NOTES_BANK_DETAILED_HANDOFF_20261121.md` and its archived original handoff in the attached GitHub Transfer ZIP. Use the latest CPM_Tools mirror and the stored V7 style. Start building the **Learning Focus / Notes bank** using a verified Lesson 3.2.3 pilot. Leave the accepted Bank Directory, Assessment Bank, Warm-Ups, existing Builder, and all review history alone. Deliver one Local Only GitHub Transfer ZIP.

**Handoff complete. Next work is the Notes bank, not another handoff or directory redesign.**
