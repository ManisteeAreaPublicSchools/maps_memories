# MAPS Mathematics Planner — CPM Tools Integration

**Approved working contract:** 2026-11-19. **Owner:** CPM Tools (Algebra 1 and AP Calculus AB). **Reference:** Physics Planner in `SCIENCE_Tools`, 2026-11-19 layout.

## Course location

Both course workspaces live inside CPM Tools: `CPM Tools > Algebra 1 > Planner` and `CPM Tools > AP Calculus AB > Planner`. AP Calculus AB is the eighth course selector entry, but **only the Planner** is connected there. Do not add Calculus to the seven native CPM question-bank/assessment packages or alter the existing separate Calculus teacher application's other tools. The older separate Algebra/AP Calc planners are archival sources, not runtime dependencies, except the one-time Algebra calendar import.

## Calendar, history and links

* 2026–27 course calendar has 215 weekday dates/43 weeks with verified MAPS school-closure and half-day labels. Future instruction entries are **empty**; official date/closure labels persist.
* Algebra migrates dated entries up to and including **November 19, 2026** from `_algebra_teacher_tools/planner/planner_state.json` on the new Planner's **first open**. An existing new-state JSON is never overwritten by old data. Legacy course section names and the five existing resource slots are retained as visible text/custom links, with the original row 1 old slot mapped to PDF row 3 and remaining four slots to rows 4–7.
* Calculus starts with a completely blank instructional history. Never import old Calculus Planner contents; existing Calculus teacher app remains intact.
* New local states live outside installed tools at `CPM_Tools_Library/planner/algebra1.json` and `CPM_Tools_Library/planner/apcalc.json`.
* `Save + Update Student Agenda` writes the appropriate static public student page locally, plus a separately housed teacher-only preview under `teacher_shared/<course>/planner/index.html`. It does not make a Git commit or publish. Open GitHub Sync for manual GitHub Desktop publishing.
* Existing public URLs stay `https://tnezki.github.io/algebra/agenda/index.html` and `https://tnezki.github.io/apcalc/agenda/index.html`.

## UI contract

* Current-week teacher overview above all 43 expanded chronological weeks; red checked selector rail for chosen current week, gray unchecked selectors for other weeks; gold current week, charcoal/gray other weeks.
* Exactly four toolbar actions: **Save + Update Student Agenda**, **Current Week**, **Student Page**, **GitHub Sync**. GitHub Sync opens **only when its own button is clicked**; saving never opens an app, tab, or external link. A successful save shows a prominent red modal reminder to sync and publish manually, with an acknowledgement button.
* Student row 1 is five weekday/date headers. Row 2 is lesson short title. Row 3 is selected student PDF or a custom item. Rows 4–7 are optional text/links and remain visible even when empty. Teacher row 8 contains public-safe teacher guide links only inside the teacher view.
* Single-line 44px teacher cells and 40px student agenda cells. All weeks visible; no accordions.
* Registered Algebra lesson PDF links use verified, stable Google Drive file IDs, not guessed filename URLs. Calculus catalog starts empty and accepts custom links until verified lessons are registered.

## CSS, naming, authority

* Canonical `maps_memories/shared_ui/math/math_planner.css` and `maps_memories/shared_ui/math/math_planner.js` with byte-identical offline fallbacks at `CPM_Tools/planner/math_planner.css` and `.js`.
* Canonical backend `maps_memories/shared_ui/math/math_planner_backend.py` and shared naming helper `maps_memories/shared_ui/math/course_artifact_naming.py`, with byte-identical offline fallbacks under `CPM_Tools/app/`.
* Canonical filename rule remains `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md`: `Alg1_3.2.3_Lesson_Student.pdf`, `APCalc_4.2_Lesson_Student.pdf`; extensions, types and audience suffix remain meaningful and portable.
* Teacher-approved one-time Drive rename retained the existing Drive IDs for all 7 Algebra Chapter 3 lesson folders and 29 lesson files. Two 3.1.1 HTML companion links originally pointed to old PDF filenames. Repair those links as a separate, explicitly authorized Drive-content change; never attempt to rewrite CloudStorage files on Planner GET. A macOS file-provider permission denial must never prevent the Planner from opening.

## QA

Local migration tests must verify 59 Algebra historical weekdays retained; all future instructional fields empty; zero Calculus lesson history; exactly 215 dates, 43 weeks, seven public rows and eight teacher rows per week; correct current-week duplication at top; no teacher guide row in public HTML; stable Drive file IDs; same-origin/revision-validated saving. Apply transfer in **Curriculum Transfer — Local Only**; no automated Git operations.

## November 19 follow-up: sync control, permissions, links, student width

* GET `/api/math-planner/<course>` is read-only with respect to Google Drive. The former `repair_legacy_html_links()` startup write was removed because Drive for Desktop may raise `PermissionError: [Errno 1] Operation not permitted`. A read must never fail due to a write outside the application's owned state.
* Teacher toolbar includes the separate **GitHub Sync** direct link (`http://127.0.0.1:8771/`); Save **never** opens this service. Following a successful save, a red, dismissible alert dialog says the agenda is saved locally but requires manual sync/publishing.
* Student resource links and teacher-only resource links come from the canonical data file `maps_memories/shared_ui/math/resource_links.json`, mirrored at `CPM_Tools/planner/resource_links.json`. This restores every resource and teacher link in the prior Algebra 1 and AP Calculus planner navigation. The teacher Planner displays both groups; generated public student agendas display only the student links.
* Local agenda HTML uses a responsive five-day table, with no unnecessary 850px minimum width on desktop, single-line 40px student rows, and a small-screen horizontal scroller only when space is genuinely insufficient.
* The existing `CPM_Tools_Library/planner` state files are **not** reset or overwritten. Preserve Algebra history and all new edits. Do not import the old AP Calculus state.
* After applying the transfer, **restart CPM Tools** to load the updated backend and frontend. Review both course planners, test local save, and publish via GitHub Desktop only when ready.


## November 19 — Legacy linked lessons shown in selectors

Legacy Algebra calendars can contain working `row3.url` entries without a corresponding
`lesson_choice`. CPM Tools reconciles these **in memory on Planner load**: a
Google Drive file ID matching a registered student PDF selects its catalog
lesson; unmatched links become a labeled Custom choice with the original URL
untouched. An explicit choice is never overridden. Merely opening the Planner
does not write anything. Save persists these selections through the normal
revision-checked workflow. No lesson is invented for future dates.

Physics and Math Planners both expose a separate GitHub Sync toolbar link.
Save updates local pages only; on success a red reminder asks the teacher to
sync manually. Neither Planner invokes GitHub Sync or runs Git commands on save.
