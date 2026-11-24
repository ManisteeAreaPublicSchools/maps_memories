# MAPS Planner lesson registration contract — verified shared index

**Approved for:** Algebra 1 and AP Calculus AB in CPM Tools, Physics in Science Tools. Updated November 24, 2026.

The source of truth for additional Planner lessons and optional support PDFs is the **single** indexed file:

`maps_memories/shared_ui/agenda/course_sources.json` (`maps-course-sources/1`).

The existing static catalogs in CPM Tools and Science Tools remain valid; their entries have priority. The shared index supplies only additional verified lessons and supports. Existing teacher-approved local records from the earlier pilot are preserved as a backward-compatible fallback. No Planner can edit or delete a calendar by reloading the index.

## Required new lesson workflow

1. Build the student PDF, teacher guide and optional support PDFs in the existing approved course/chapter/lesson folders using descriptive course-first filenames (`Alg1`, `APCalc`, `Phy`). Never use generic `student.pdf` or `teacher.pdf`.
2. Place the final files in the usual Google Drive synchronization workflow. **After Google Drive has assigned file IDs**, verify the real file metadata via the connected Google Drive service. Do not infer IDs from filenames or assume a replaced PDF retains its old ID.
3. Append the lesson and any support entries to `course_sources.json`, preserving its older records and stable IDs. The resulting file must be part of the normal **Curriculum Transfer — Local Only GitHub Transfer ZIP**. For an unassigned Drive ID, do not pretend a lesson is registered: clearly mark the registration pending until the ID can be verified and include the source-index update in a follow-up ZIP.
4. Open the Planner or click **Refresh Lesson List**. The button reloads the *local verified index*, not Google Drive. It does not overwrite unsaved calendar edits, sync Git, or regenerate student pages.
5. Select the newly registered lesson in the dropdown, Save + Update Student Agenda, then publish manually through GitHub Desktop.

The previously attempted `planner_registration.json` file-per-lesson and Google Cloud Desktop OAuth approaches are **retired**. The Planners no longer scan protected Google Drive Desktop folders, and do not require teachers to set up Cloud projects, clients, tokens, or read-only OAuth permissions. Do not reintroduce those requirements when creating lessons.

## Schema details

Course keys: `algebra1`, `apcalc`, `physics`. Each contains a `lessons` array and a `supports` array. A lesson object needs stable `id`, `label`, `student_filename`, and a verified `student_url`; `short_name`, `agenda_label`, `teacher_filename`, and verified `teacher_url` may accompany it. The actual filename must match the existing naming standard: `<Prefix>_<identifying information>_Student.pdf`; teacher file suffix `_Teacher.pdf`. Support objects need stable `id`, `label`, `url`, and optionally `filename`; support filenames should be descriptive and course-prefixed. The source index is metadata, not a copy of student PDFs.

All URLs are exact `https://drive.google.com/file/d/<verified-ID>/view` links. A teacher guide URL must **never** be written into the public student agenda; it is used only in the teacher view. Merge entries by both ID and student Drive URL, never replacing an existing catalog entry. Validate that the index is complete JSON and that all previously verified entries are retained before delivery.

## Failure behavior

If the index is unreadable or missing, the original course catalog still loads, saved calendars are not deleted, and student pages previously published stay intact. Previously selected additional lesson IDs are retained in saved state until the index is restored. Save may require restoring an unresolved source first; do not substitute an invented link. There is no remote authentication setup screen or scan-success message for inaccessible folders.
