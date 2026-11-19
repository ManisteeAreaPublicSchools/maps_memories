# MAPS Physics Planner — Seven-Row Lesson Agenda Contract

Status: implemented in local Physics Tools Planner; 2026-11-19. This is the existing Physics Tools Planner (`~/GitHub/_physics_teacher_tools/planner`), not the new Science Tools Planner placeholder.

## Toolbar

Only four actions in the Planner tool strip: **Save + Update Student Agenda**, **Current Week**, **Student Page**, **GitHub Sync**. Student Page opens the local preview (`/physics/agenda/index.html`) and displays the eventual public URL `https://tnezki.github.io/physics/agenda/index.html` in the Planner. GitHub Sync is a link to the separate teacher-controlled local app; the transfer process never invokes Git itself.

## Fixed weekly grid

Every Monday–Friday column has these seven rows on the **student page**, including blank rows:

1. Weekday/date (header).
2. Short lesson name, auto-filled when a known lesson is selected; preexisting labels remain for historical dates until reselected.
3. Lesson selector in the teacher Planner; student page displays its actual linked PDF. Options: **Custom… first**, then registered lessons (newest first), followed by a blank choice. A custom lesson can include its own PDF link and optional guide.
4–7. Four visible optional rows; initially empty. In the teacher editor, click the empty cell to add or clear text and an optional URL. Empty rows are not collapsed.

An **eighth row** exists in the teacher editor and co-teacher agenda, with a direct link to the selected lesson's teacher guide PDF. This row is **not generated** on the public student agenda. The teacher-authored guide may be publicly readable; the student page omission is for uncluttered UX, not secrecy.

## Direct Drive link requirements

Canonical course layout: `Google Drive / My Drive / ~Curriculum / __MAPS_Courses / Physics / ch_## / lesson_#_#_# / student.pdf (or named student PDF)` and `teacher/teacher.pdf` (or equivalent named guide). No extra `lessons_google_drive` or `ch05_lessons` layers for new lessons.

Actual PDF links use the **file ID** in `https://drive.google.com/file/d/<ID>/view`. A local filename or chapter path does not determine a Drive file ID. The local `_physics_teacher_tools/planner/lesson_catalog.json` maps verified lesson identifiers to PDF file URLs and short titles. **Every future lesson transfer must update this catalog** after verifying the Drive file IDs and should not invent or guess a new URL. Until registered, the lesson is not selectable automatically; use Custom for a one-off.

Use the catalog entry's `short_name` for row 2, `label` for the row 3 option, `student_url` for students and `teacher_url` only for the teacher row. Historical manually linked lessons can be recognized by verified file ID even when the old link contains `?usp=sharing` or a mistyped lesson label.

The Drive folder's sharing controls still determine whether students can open the PDF. Do not claim a link is student-accessible without a real student access test. Teacher-written answer guides may be shared; private student/guardian/grade/accommodation data and restricted publisher assets remain protected.

## State and publishing

The live local calendar stays at `_physics_teacher_tools/planner/planner_state.json` and is **never packaged** or overwritten by a Planner feature transfer. New choices are stored additively in per-day `lesson_choice`, `lesson_custom`, and four `extra_rows` without deleting historical fields. Original manual current-week selection survives. Save regenerates `physics/agenda/index.html` and `teacher_shared/physics/index.html` locally. No Git action takes place from the transfer; the teacher decides when to publish with GitHub Desktop.

QA gates: verify 7 student rows including blanks; 8 teacher rows; short-name selection; actual PDF links; zero teacher PDF URLs in student HTML; all 5 weekdays and all weeks; custom edit; existing planner state validates; no file/URL inference without a catalog; old running server restart.
