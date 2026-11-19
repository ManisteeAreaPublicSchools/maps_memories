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
* Exactly three toolbar actions: **Save + Update Student Agenda**, **Current Week**, **Student Page**. GitHub Sync opens on successful save but is not an additional toolbar control.
* Student row 1 is five weekday/date headers. Row 2 is lesson short title. Row 3 is selected student PDF or a custom item. Rows 4–7 are optional text/links and remain visible even when empty. Teacher row 8 contains public-safe teacher guide links only inside the teacher view.
* Single-line 44px teacher cells and 40px student agenda cells. All weeks visible; no accordions.
* Registered Algebra lesson PDF links use verified, stable Google Drive file IDs, not guessed filename URLs. Calculus catalog starts empty and accepts custom links until verified lessons are registered.

## CSS, naming, authority

* Canonical `maps_memories/shared_ui/math/math_planner.css` and `maps_memories/shared_ui/math/math_planner.js` with byte-identical offline fallbacks at `CPM_Tools/planner/math_planner.css` and `.js`.
* Canonical backend `maps_memories/shared_ui/math/math_planner_backend.py` and shared naming helper `maps_memories/shared_ui/math/course_artifact_naming.py`, with byte-identical offline fallbacks under `CPM_Tools/app/`.
* Canonical filename rule remains `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md`: `Alg1_3.2.3_Lesson_Student.pdf`, `APCalc_4.2_Lesson_Student.pdf`; extensions, types and audience suffix remain meaningful and portable.
* Teacher-approved one-time Drive rename retained the existing Drive IDs for all 7 Algebra Chapter 3 lesson folders and 29 lesson files. Two 3.1.1 HTML companion links originally pointed to old PDF filenames; the local Math Planner repairs those references when the lesson folder is accessible through Google Drive for Desktop.

## QA

Local migration tests must verify 59 Algebra historical weekdays retained; all future instructional fields empty; zero Calculus lesson history; exactly 215 dates, 43 weeks, seven public rows and eight teacher rows per week; correct current-week duplication at top; no teacher guide row in public HTML; stable Drive file IDs; same-origin/revision-validated saving. Apply transfer in **Curriculum Transfer — Local Only**; no automated Git operations.
