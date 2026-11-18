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

**Approved example prefixes:** `Alg1` for Algebra 1 and `Phy` for Physics. Assign other course prefixes deliberately in the course registry rather than inventing competing abbreviations. For material spanning multiple lessons or weeks, use the recognized unit/date or sequence ID after the course prefix (e.g. `Phy_Week06_Review_Student.pdf`).

### Practical requirements

1. Course and lesson must be recognizable in the filename without relying on folder context. Avoid generic names such as `lesson.pdf`, `student.pdf`, or `worksheet_final2.pdf`.
2. Use stable, simple characters (`A-Z`, `a-z`, `0-9`, underscores, periods, hyphens). Prefer underscores between major parts. Preserve official lesson numbering such as `3.1.2`.
3. Make the type human-readable (`Lesson`, `Lab`, `Notes`, `Review`, `Assessment`, `Simulation`, `VideoLab`, etc.).
4. Distinguish student and teacher versions with `_Student` and `_Teacher` where both exist. Do not place private teacher material in public GitHub pages.
5. Revisions should preserve the intentional course/lesson/type identity and, where practical, the stable file name; don't append `final_v3_new` to student-facing files. Use revision metadata or version history separately.
6. Apply the pattern to newly generated work. **Do not rename or move legacy materials automatically.**
7. Future tools and builders should enforce this convention through a **shared naming helper**, not through eight duplicated course-specific functions.
8. A known Drive share URL is not guaranteed by overwriting a synced local file; preserving an existing Drive file ID requires a separately verified in-place Drive API update. This is a **later, lower-priority** enhancement and not a prerequisite for course shell/Assessment Plans work.

This standard contains no student information.
