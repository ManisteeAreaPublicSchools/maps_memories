# MAPS course artifact naming standard

**Status:** Approved working rule (2026-11-17)  
**Authority:** `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md`  
**Purpose:** Make files recognizable in Notability, Google Drive, Finder, downloads, teacher libraries, and agendas.

## Rule — course first, lesson second

Name every student-facing and teacher-facing course lesson file with its **course prefix before its lesson/section identifier**, then its resource type. The name should remain meaningful when viewed outside a folder, especially after a student sends a PDF to Notability.

Recommended portable pattern:

`<CoursePrefix>_<LessonOrSection>_<ResourceType>[_Audience].<extension>`

Examples:

- `Alg1_3.1.2_Lesson_Student.pdf`
- `Alg1_3.1.2_Lesson_Teacher.pdf`
- `Phy_5.2.2_Lab_Student.pdf`
- `Phy_5.2.2_Lab_Teacher.pdf`
- `Phy_5.2.2_Simulation.html`
- `Phy_5.2.2_Notes_Student.pdf`

**Approved prefixes:** `Alg1` for Algebra 1, `APCalc` for AP Calculus AB, and `Phy` for Physics. Assign other course prefixes deliberately in the course registry rather than inventing competing abbreviations. For material spanning multiple lessons or weeks, use the recognized unit/date or sequence ID after the course prefix (e.g. `Phy_Week06_Review_Student.pdf`).

### Practical requirements

1. Course and lesson must be recognizable in the filename without relying on folder context. Avoid generic names such as `lesson.pdf`, `student.pdf`, or `worksheet_final2.pdf`.
2. Use stable, simple characters (`A-Z`, `a-z`, `0-9`, underscores, periods, hyphens). Prefer underscores between major parts. Preserve official lesson numbering such as `3.1.2`.
3. Make the type human-readable (`Lesson`, `Lab`, `Notes`, `Review`, `Assessment`, `Simulation`, `VideoLab`, etc.).
4. Distinguish student and teacher versions with `_Student` and `_Teacher` where both exist. Do not place private teacher material in public GitHub pages.
5. Revisions should preserve the intentional course/lesson/type identity and, where practical, the stable file name; don't append `final_v3_new` to student-facing files. Use revision metadata or version history separately.
6. Apply the pattern to newly generated work. Legacy materials are not renamed automatically except for the teacher-authorized Algebra 1 Chapter 3 renames of November 19, 2026.
7. Future tools and builders should enforce this convention through a **shared naming helper**, not through eight duplicated course-specific functions.
8. A known Drive share URL is not guaranteed by overwriting a synced local file; preserving an existing Drive file ID requires a separately verified in-place Drive API update. This is a **later, lower-priority** enhancement and not a prerequisite for course shell/Assessment Plans work.

This standard contains no student information.

## Shared Math naming helper (November 19, 2026)

The authoritative helper is `maps_memories/shared_ui/math/course_artifact_naming.py`; the offline CPM Tools fallback is `CPM_Tools/app/course_artifact_naming.py`. Use `artifact_name(course, lesson, resource, audience, extension)` for all new exports and verify companion PDF/HTML paths together. The approved Calculus prefix is `APCalc`. The Planner catalogs store existing Drive file IDs, not guessed filenames.

## Enforced release rule (2026-11-23) — recognizable Notability filenames

For **all newly packaged Algebra 1, AP Calculus AB, and Physics lessons**, the
actual student/teacher PDF names must include the approved course prefix, an
identifiable lesson/date or section, a resource type, and the Student/Teacher
suffix. Examples:

- `Alg1_20261123_BouncyBallLab_Student.pdf`
- `APCalc_Ch03_TestReview_20261123_Student.pdf`
- `APCalc_Ch03_AntiderivativesIntro_20261125_Student.pdf`
- `Phy_5.3.M_Modeling_Student.pdf`

Use corresponding `_Teacher.pdf` names for teacher copies. The same convention
applies to standalone student/teacher HTML companions; `index.html` is retained
as the conventional navigational landing page. Keep names stable across
revisions. No spaces or automatically appended version numbers.

**Enforcement:** `memories/Tools/curriculum_transfer/apply_curriculum_transfers.py`
preflights newly created or replaced lesson PDFs under the three approved
`*_lessons_drive` aliases, rejects ambiguous filenames before applying any
files, and also rejects generic `student.html`/`teacher.html`/`lesson.html`
companions. This guard does not scan or rename historical files or affect
unrelated repository PDF transfers, data, or assets. New builders should call
`lesson_pair(...)` / `validate_lesson_deliverable_name(...)` from the canonical
`maps_memories/shared_ui/math/course_artifact_naming.py` (and the identical
CPM Tools offline copy). The rule applies to the transferred **actual bytes'
filename**, not just the Planner dropdown label or visible HTML heading.

**Planner registration is separate and mandatory.** Every lesson delivery
must include verified Drive PDF IDs either in the course catalog or in
`planner_registration.json`. Since newly synced files do not have known Drive
IDs before Google Drive processes them, verify those IDs after syncing and
register them before claiming that the lesson automatically appears in the
Planner. A generic filename is never an acceptable workaround.
