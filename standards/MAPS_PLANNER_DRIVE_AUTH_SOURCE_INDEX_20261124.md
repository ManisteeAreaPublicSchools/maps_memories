# MAPS Planner lesson sources — simplified architecture (2026-11-24)

**Current decision:** The three working Planners read one verified local source index.
The earlier Google OAuth scanning proposal has been withdrawn. **Do not require
teachers to create Google Cloud projects, authorize the local Planners, or maintain
per-lesson planner_registration.json files.** Old OAuth endpoints are removed.

## One authoritative source index

- `maps_memories/shared_ui/agenda/course_sources.json`
- Schema: `maps-course-sources/1` with `courses.algebra1`, `courses.apcalc`, `courses.physics`.
- Each course stores `lessons` and `supports` arrays. Valid lesson IDs and actual
  Google Drive file URLs are mandatory. The student URL must be a confirmed PDF ID,
  *not* a path inferred from the filename. Match the teacher guide in the same folder.
- Existing CPM Tools/Science Tools catalogs take precedence. Additional verified
  entries merge by unique lesson ID and student Drive URL. Older teacher-approved
  entries, if any, remain readable as a legacy fallback; no saved calendars reset.
- Canonical reader: `maps_memories/shared_ui/agenda/drive_source_connector.py`.
  Course apps use tiny adapters to load it, not independently maintained copies.
- The dated `verified_drive_sources_20261124.json` is a **legacy fallback only**,
  used if `course_sources.json` is not installed. Future transfers modify only
  `course_sources.json`.

## New lesson creation requirement — one transfer per lesson

1. Build the student lesson, teacher guide, and optional supports using descriptive
   course-specific names, e.g. `Phy_5.3.M3_Modeling_Student.pdf` or
   `APCalc_Ch03_AntiderivativesIntro_20261125_Student.pdf`.
2. Upload to the established `~Curriculum/__MAPS_Courses/<Course>/ch_NN/<lesson>/`
   folders via the user's usual transfer workflow.
3. **After Google Drive has assigned the real file IDs**, use the connected Drive
   tool to verify the student PDF, optional teacher PDF and support PDF IDs.
4. Update the same canonical `course_sources.json`, preserving all existing
   entries and stable IDs, as part of the lesson's GitHub Transfer ZIP. If Drive
   IDs are not available before delivery, do not invent links or pretend the
   dropdown is ready; clearly mark the registration as incomplete and complete
   registration in the next transfer after Drive verifies the files.
5. Never create placeholder student links, never replace saved calendar state,
   and never automatically push/commit/sync GitHub.

## Day-to-day teacher experience

- Opening the Planner loads all registered lessons from the canonical index,
  the older catalog and previously approved sources.
- **Refresh Lesson List** rereads the *local verified index* without overwriting
  any unsaved Planner edits. It is not a Google Drive scan and never connects online.
- Selecting a lesson and clicking **Save + Update Student Agenda** updates the
  local agenda; the teacher manually publishes with GitHub Desktop.
- Support PDFs can be selected in the optional agenda rows; teacher-guide URLs
  stay in the teacher-only row and out of the public agenda.
- If the index is temporarily missing/unreadable, the original course catalog
  and saved calendar still work. There are no authentication screens.

## Integrity checks before every lesson transfer

- Each new lesson/student and teacher PDF uses approved descriptive naming.
- Each Drive URL corresponds to a verified actual file ID and the correct course.
- New index entries are additive and deduplicated; old entries are preserved.
- Test new source selection, student page generation, and optional supports.
- Use schema-3 Curriculum Transfer — Local Only ZIP with exact existing hashes.
- Test the actual installer transaction before delivery; never write to GitHub.
