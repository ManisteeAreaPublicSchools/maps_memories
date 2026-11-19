# Science Tools Planner — Integrated Seven-Row Course Agenda

**Canonical implementation:** `SCIENCE_Tools/` shared Science Tools application, course route `/courses/physics/tools/planner`.

**Status (2026-11-19):** Physics connected, other seven Science courses display "Calendar has not been loaded" until real course data is supplied. The earlier `_physics_teacher_tools` Planner is retired, not part of the runtime dependency graph. No clones for each course.

## Toolbar — only four controls

1. **Save + Update Student Agenda** — saves the independently stored Physics calendar and regenerates `~/GitHub/physics/agenda/index.html` locally (never pushes to GitHub).
2. **Current Week** — jumps editor to the teacher-selected current week.
3. **Student Page** — opens local preview at `/planner/physics/student-page`. Once manually published through GitHub Desktop, the URL remains `https://tnezki.github.io/physics/agenda/index.html`.
4. **GitHub Sync** — opens the separate sync app at `http://127.0.0.1:8771/`; Science Tools itself does not commit, pull, or push.

## Daily 7 + 1 row contract

1. Weekday / date header.
2. Short lesson name, derived automatically from the selected lesson.
3. Student PDF selection: Custom first; then registered lesson numbers, each linked to the actual Google Drive PDF file ID; blank choice last.
4.–7. Four visible optional rows, blank until teacher enters text or link. They are *never collapsed* in the student page.
8. Teacher guide link, present only in the teacher editor (and optional local teacher preview), never in the generated public student page.

The Student Page is a static `physics/agenda/index.html` and contains seven rows per week. Public teacher-made answer guides are acceptable as learning resources, but student-specific data, private contact information, credentials, and restricted publisher materials must not be published.

## Source and state rules

- Teacher calendar: `~/GitHub/SCIENCE_Tools_Library/planner/physics.json` (local-only sibling outside both the Science Tools installed code and the public Physics repository).
- First Planner open: import live `~/GitHub/_physics_teacher_tools/planner/planner_state.json` **if it exists**; otherwise import the last verified 215-day, 2026–2027 course-calendar snapshot from `SCIENCE_Tools/data/physics_planner_import_seed.json`. The snapshot contains planning dates and lesson references only, no student records. Never overwrite an already imported Science Tools calendar with an old legacy file.
- Preserve school-year dates, weekday labels, manually selected current week, and special-day labels. Old extra curriculum-resource rows are intentionally not republished; all four optional student rows begin blank in the new format.
- Canonical link catalog: `SCIENCE_Tools/data/physics_lesson_catalog.json`, built from verified PDFs under `Google Drive / My Drive / ~Curriculum / __MAPS_Courses / Physics/ch_##/lesson_.../`. Include actual Drive student and teacher PDF IDs; **never** invent a link from the filename alone.
- Every new lesson build may update the catalog when verified Drive IDs are available. Until then, the teacher selects Custom.
- Save validates same-origin JSON, rejects unknown lessons and unsafe links, uses revision conflict protection, and makes atomic local writes. It never writes back into `_physics_teacher_tools`.
- Non-Physics courses must not receive fabricated dates, lesson catalogs, or teacher data.

## Decommission checklist

1. Apply the GitHub Transfer ZIP through Curriculum Transfer — Local Only.
2. Close and reopen the **Science Tools** Dock app. The launcher checks the new Planner health marker and restarts an outdated Science Tools process if it can safely identify it.
3. Open **Physics → Planner**, verify the current week and saved lesson selections, then click **Save + Update Student Agenda**.
4. Open **Student Page** locally and verify PDF links / seven rows. Review the public `physics/agenda/index.html` locally. Publish through GitHub Desktop when ready.
5. Only then delete the old `_physics_teacher_tools` application if desired. The new Planner works without that app. It never depends on the old server or its data after the first import.

## QA before future releases

- Verify the original Physics Assessment Plans remain available, 107-day foundation and 29 goals unchanged.
- Verify all eight Science courses still route through one shared engine and seven show honest empty calendar states.
- Verify student rows 1–7 are present including blank rows; teacher row 8 excluded from published student HTML.
- Verify course calendar, current week, and actual Google Drive URLs survive save/reopen.
- Confirm **only four top-toolbar actions**; teacher editor may include week navigation and edit controls.
- Confirm zero Git operations during apply, save, and preview.


## November 19 afternoon adjustment: schedule days and old-agenda cleanup

- The 2026-11-16 through 2026-11-20 current week and all earlier entries are retained.
- On the first load after this release, remove *only* legacy prefilled future
  unit/section labels and their obsolete day numbers starting November 23, 2026.
  Preserve full dated calendar, weekday, existing typed day status (Break, P.D.,
  Half Day, etc.), and any teacher-chosen lesson dropdown / custom rows.
- This is a versioned ONE-TIME migration, not a nightly or every-save operation.
  Store `future_legacy_cleanup_version=1` in the local private state. Never
  erase future lessons added after the one-time cleanup.
- Keep the seven visible rows and teacher-only eighth row exactly; day types
  are edited in the date header of the teacher planner, not in an additional row.
- Clearly mark Break, P.D., Half Day, No School, Snow Day, Holiday,
  Assembly Schedule, Testing, Sub Assignment, Early Release and custom statuses.
  All-day closures display a status in row 2 and suppress lesson display.
  A half-day retains its lesson links, with a conspicuous status marker.
- Do not infer the district's holiday/P.D. calendar from a national calendar.
  Teacher assigns closures explicitly. Preserve pre-existing closure markers.
- Every non-current week (past **and** future) uses the old gray style:
  dark charcoal date header, alternating white and pale-gray rows, gray teacher
  row. Current week uses warm mustard/cream and deep-teal contrast.
- Student preview and published agenda use identical fixed-seven-row semantics.
  Saving regenerates the public Physics agenda HTML locally; GitHub Desktop
  remains the only publisher.
