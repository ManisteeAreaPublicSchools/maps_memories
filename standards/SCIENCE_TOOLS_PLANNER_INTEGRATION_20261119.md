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

## November 19 activation repair

The gray-week and one-time future-placeholder cleanup update changes Python code. The running HTTP process does not automatically reload that module. The prior ZIP did not change the Science Tools launcher and server health marker, so the Dock app could reuse the old server after successful installation. This patch changes the Planner health marker to shared-engine-v2-special-days-gray-weeks in the server and launcher. Reopen the Science Tools Dock app after applying: it detects the old Planner version, verifies process ownership and restarts only its own process on port 8786. Hard-refresh the Planner page and click Save + Update Student Agenda to regenerate physics/agenda/index.html. GitHub Desktop is still required to publish the public student page. A source transfer does not directly edit private SCIENCE_Tools_Library/planner/physics.json; the one-time cleanup runs on the first Planner GET with the updated server.


## November 19: Chronological current-week display + official MAPS calendar

- **Canonical source**: Manistee Area Public Schools, *MAPS Calendar 2026–27*,
  https://s29981.pcdn.co/wp-content/uploads/2026/03/MAPS-Calendar-26-27.pdf.
  This district calendar was previously supplied by the teacher; verified from
  the official one-page PDF. Never substitute a generic U.S. holiday schedule.
- **Student and teacher page layout**: Display every week **exactly once**, in
  calendar order. The **current week stays between adjacent previous/following
  weeks**, prominently mustard/gold with cream rows; all other weeks stay
  charcoal/gray. Include a jump-to-current-week link. Do not detach the current
  week to a separate top section, which previously made it disappear from the
  chronological list. Each week retains exactly seven visible student rows;
  optional teacher view has one additional teacher-guide row.
- **Verified district day types**: Sep 4 Labor Day weekend (Break); Sep 7 Labor
  Day (Holiday); Sep 21 P.D.; Oct 15–16 Half Day; Nov 25 Half Day; Nov 26–27
  Thanksgiving Break; Dec 21–Jan 3 Winter Break (students return Jan 4); Jan
  18 P.D.; Feb 19–22 Winter Break (return Feb 23); Mar 15 P.D.; Mar 26–Apr 4
  Spring Break (return Apr 5); May 31 Memorial Day (Holiday). The original PDF
  also lists Oct 14 conferences and Jan 15 semester end; these are *not* full-day
  closures and are therefore not silently converted to a no-school day.
- **One-time source-driven local migration**: On the first Planner read after
  this update, apply district day labels to existing
  `SCIENCE_Tools_Library/planner/physics.json` only for dates still tagged
  `Regular Day`. Preserve teacher-set non-regular labels, current week, dates,
  lessons, optional rows, and the previous future-placeholder cleanup. Track
  `district_calendar_version=1`, source URL, and update counts. Never replace
  or ship the private planner state in a transfer, and never reapply this to
  erase a teacher's future changes. All-day closures suppress student lessons
  only in the *view* (choices remain saved). Half days may still show lessons.
- **Publishing**: Teacher must click **Save + Update Student Agenda** to update
  `physics/agenda/index.html` locally and then publish using GitHub Desktop.
  The Python server must reload after installing a Planner code change.

## November 19 final UX correction — current student week first; teacher all weeks expanded

This rule supersedes the earlier chronological-current-week paragraph above:

- **Student page:** Put the selected current week **at the very top, first and once only**,
  with mustard header and cream rows. Below it, label **Other Weeks** and render
  remaining past/future weeks in date order, charcoal date headers and alternating
  white/light-gray rows. No collapsing, and no duplicate copy of the current week.
- **Teacher Planner editor:** Render *every* dated week, fully expanded in chronological
  order. Do not restrict the editor to a single selected week or use accordions,
  `details`, or a week-selection dropdown. Make current week mustard/cream in context;
  all surrounding weeks stay gray. Add a small per-week **Set as Current Week** action
  for noncurrent weeks; keep the top toolbar at exactly four controls. The existing
  **Current Week** toolbar control scrolls to the current editable week.
- **Row contract:** Date + six student body rows (including four always-visible
  optional blanks); one extra teacher-guide row in the editor only. Retain the
  original Drive lesson links, staff-created special-day labels, calendar dates,
  and manual `current_week_index` without a data migration.
- After applying, reopen Science Tools from the Dock (health marker v4 restarts
  only its own outdated server), refresh the Planner, and use Save + Update
  Student Agenda to rewrite `physics/agenda/index.html` locally. GitHub publishing
  remains manual.


## Confirmed user decisions — 2026-11-19 final Planner layout contract

The following supersedes earlier ambiguous November 19 layout descriptions:

1. **Teacher Science Tools Planner:** a separate current-week overview at the top
   includes row 8 (Teacher Guide), followed by every week of the school year
   expanded, editable, and chronological. The current week appears **again** in
   that full-year editor. No week-selector dropdown and no accordions. Current
   week mustard/cream; surrounding weeks charcoal/light gray. The toolbar
   Current Week button jumps to the full-year current week. A separate floating
   **Top** button returns to the start; it is not an extra top-toolbar action.
2. **Published Physics student agenda:** match the existing public Algebra agenda
   (https://tnezki.github.io/algebra/agenda/index.html) in compact layout and
   navy/gold/gray styling. It begins with the current week's seven rows, then
   an **ALL WEEKS** divider and the chronological full-year calendar (including
   a second current-week occurrence, colored gold). Do not show teacher-guide
   row or teacher-guide URL in this public student HTML. Keep all seven rows,
   including optional blanks, instead of losing the fixed row contract.
3. **Four top toolbar actions:** Save + Update Student Agenda; Current Week;
   **Student Page** pointing at the actual public
   https://tnezki.github.io/physics/agenda/index.html ; and GitHub Sync
   pointing at http://127.0.0.1:8771/ . The GitHub Sync button only opens the
   service if already running; never start it, and never commit or push.
4. Preserve local-only state (`SCIENCE_Tools_Library/planner/physics.json`),
   215 school dates, teacher-selected week, lesson links, calendar exceptions,
   and eight-tool single-engine separation. Saving regenerates the physics
   GitHub repository's agenda/index.html; publishing remains manual.
5. Every future Planner release must explicitly test the teacher overview's
   guide link, all 43 editable weeks, the actual public Student Page hyperlink,
   the four buttons, current week twice (top + ALL WEEKS), gray/gold CSS,
   and absence of guide URLs from the public student HTML.
