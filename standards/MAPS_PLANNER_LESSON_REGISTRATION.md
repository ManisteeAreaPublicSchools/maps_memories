# MAPS Planner lesson registration contract

**Approved for:** Algebra 1 in CPM Tools, AP Calculus AB in CPM Tools, Physics in Science Tools.

## Why it exists

The Drive for Desktop mirrored folders display lesson files and filenames but do not guarantee access to the Google Drive file IDs required to form working student PDF links. Never guess a Drive file ID or publish a `file://` link. A newly uploaded lesson requires *verified* file IDs, either in the course's installed catalog (delivered with the lesson transfer) or in a small read-only registration manifest inside its Google Drive lesson folder.

## Automatic discovery

On every Planner read, the current installed catalog is retained and the Planner checks the local Drive mirror at `My Drive/~Curriculum/__MAPS_Courses/<Course>/ch_NN/<lesson-folder>/planner_registration.json`. A folder without this manifest is not added merely because a PDF exists. The optional environment variable `MAPS_LESSON_DRIVE_ROOT` may point at the `__MAPS_Courses` directory when the default Drive-for-Desktop macOS location differs. Existing catalog entries win on conflicts. Missing Drive for Desktop, offline folders, malformed manifests, and File Provider permission errors are skipped without preventing the Planner from opening; no metadata files or lesson PDFs are modified by the Planner.

The required format is:

```json
{
  "schema": "maps-planner-lesson-registration/1",
  "course_id": "algebra1",
  "id": "3.2.4",
  "label": "3.2.4 Lesson",
  "short_name": "Multiplying Polynomials",
  "agenda_label": "3.2.4 Lesson PDF",
  "student_filename": "Alg1_3.2.4_Lesson_Student.pdf",
  "student_pdf_id": "<verified Drive file ID>",
  "teacher_filename": "Alg1_3.2.4_Lesson_Teacher.pdf",
  "teacher_pdf_id": "<verified Drive file ID>"
}
```

Use `course_id` values `algebra1`, `apcalc`, or `physics`. Approved name prefixes are `Alg1`, `APCalc`, and `Phy`. The student PDF must exist directly inside the lesson folder; a teacher PDF, if registered, must exist under `teacher/`. The filename patterns must end with `_Student.pdf` and `_Teacher.pdf`. A registration may omit teacher metadata if none exists. The schema also accepts `student_url` and `teacher_url` in verified `https://drive.google.com/file/d/<id>/view` form instead of `*_pdf_id` fields.

## Lesson-builder responsibility

1. Produce student and teacher files under the canonical lesson folder using the course-first filename standard from `MAPS_COURSE_ARTIFACT_NAMING.md`.
2. Obtain actual Drive file IDs **after** upload/sync; the connected Drive file metadata is an acceptable source. Do not assume a newly created file retained an old ID after transfer.
3. Register those IDs with the lesson transfer: update the installed course catalog or include `planner_registration.json` alongside the synced Drive lesson files. Both methods are supported; using both is harmless because the installed catalog takes precedence.
4. A Planner reread (reopen/refresh) merges new valid manifests into its dropdown. Selecting and saving remains teacher-controlled and never auto-publishes.
5. Do not modify the local-only dated Planner state, import old calendars, or automatically push GitHub during a lesson release.

**Existing data:** Previously registered entries, including 2026-11-23 Algebra 1 Bouncy Ball and 5.2.R Physics Reading, remain in their installed catalogs. The new manifest reader supports future course lessons across all three Planners. A PDF placed on Drive *without* verified-link registration remains intentionally unavailable as a registered student-facing lesson; the teacher may still use Custom with a verified Drive URL.
