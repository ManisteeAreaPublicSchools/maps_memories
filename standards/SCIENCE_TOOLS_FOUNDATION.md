# MAPS Science Tools — shared shell authority (2026-11-17)

## Locked direction

- Dock app: `~/GitHub/SCIENCE_Tools/Science Tools.app`, local-only server `127.0.0.1:8786`.
- Familiar CPM Tools **layout**, not reused Physics Tools code.
- Eight courses: 6th Grade Science, 7th Grade Science, 8th Grade Science,
  Physical Science, Biology, Chemistry, Anatomy/Physiology, and Physics.
- All eight share one ten-tool shell: Planner, Assessment Plans, Lesson Builder,
  Visuals & Printables, Assessments, Question Banks, Mastery & Evidence,
  Launches & More, Library, Course Setup.
- The **tools are navigation shells only** until integrated. Nothing in a shell
  claims to perform editing, grading, data loading, or distribution yet.
- Shared CSS authority: `maps_memories/shared_ui/science/science-ui.css`.
  Spiced mustard `#D39832` is prominent; deep teal `#163D42` provides contrast.
  Server serves the canonical CSS live, with an identical bundled fallback.
- One toolbox implementation for every course: `SCIENCE_Tools/app/app.js`.
  Course names are data in `SCIENCE_Tools/config/courses.json`.
- Custom Science Dock icon is retained; no emoji placeholder icon.
- No former Physics Tools code/materials reused. The original Drive
  `~Curriculum/__Physics` is preserved unchanged. A separate fresh home exists
  at `~Curriculum/__MAPS_Courses/Physics/lessons_google_drive`.
- Do not connect student directories, student records, IEP/504, or Portfolio
  until access/data design is explicitly approved.

## Source, transfer and mirroring

- `maps_memories` holds district-wide, public code/design standards and a code-only
  mirrored copy of `SCIENCE_Tools`. No student information may enter this repo.
- All installed app files are maintained in `SCIENCE_Tools`. Transfers should
  refresh the local code-only mirror, not launch Git operations.
- Curriculum Transfer 3; Local Only; single GitHub Transfer ZIP.
- Teacher manually reviews and syncs repository modifications via GitHub Sync
  or GitHub Desktop. Browser tests are separate from teacher Mac verification.
- Applying one shared CSS change updates every course after refresh.

## Next integration decision

Review course navigation and mustard theme before building real tools.
Preserve common navigation contracts; add functionality as shared engines,
not as eight per-course copies.

## 2026-11-17 navigation and naming refinement (installed via Local Only transfer)

- The top mustard header is the **only** Science Tools / Current Course
  navigation. The in-body `Science Tools / Physics` breadcrumb and underline,
  and redundant in-panel back/all-course controls have been removed for every
  course and ten-tool view. Page titles remain for context.
- Artifact filenames are **course first, lesson second, resource type third**.
  See `standards/MAPS_COURSE_ARTIFACT_NAMING.md`: e.g.
  `Alg1_3.1.2_Lesson_Student.pdf` and `Phy_5.2.2_Lab_Student.pdf`.
  This ensures files remain recognizable in Notability.
- Stable Google Drive file IDs/URLs are desirable but **not a current
  development priority**. Local synced-file replacement does not guarantee
  identity preservation; discuss a verified Drive API update later.
- Next work: **Assessment Plans**, starting with analysis of CPM Tools' current
  Assessment Plans functionality and a shared Science course model. Do not
  migrate old Physics Tools material or enable student data access.
- Detailed next-chat handoff: `handoffs/SCIENCE_TOOLS_ASSESSMENT_PLANS_NEXT_CHAT_20261117.md`.


## 2026-11-17 — Assessment Plans phase 1 (one shared engine)

- CPM Tools' working Algebra 1 Assessment Plans was audited as the interaction
  reference: chapter selector, section goals, collapsed skills/source lessons,
  print chapter/all, separate teacher note overrides, and explicit curriculum
  approval states. Its Algebra-specific API and curriculum assumptions were
  **not copied** into Science.
- Science now has one generic `SCIENCE_Tools/app/assessment_plans.js` client,
  `SCIENCE_Tools/app/assessment_plans.py` data/notes backend, and one shared
  `SCIENCE_Tools/assets/assessment_plans.css`; `app/app.js` remains the single
  navigation renderer and top mustard header remains the only course navigation.
- Current Physics authoritative teaching sequence is the teacher-uploaded
  `SCIENCE_Tools/data/source/Physics_107_Day_Course_Plan_20261117.md`, structured
  as `SCIENCE_Tools/data/physics_assessment_plans.json`. Order:
  1,2,3,4,5,6,10,12,9; chapters 7/8/11 omitted. 107 core periods =
  82 publisher periods + 25 dedicated full-period readings. Nine chapter test
  periods and Monday pretest reviews remain separate from the 107 core periods.
- All 25 proposed section goals/skills and their evidence suggestions are
  **draft, not teacher approved**. The 107-day source verifies curriculum
  topics, labs, simulations, and schedule; it does not approve newly authored
  goal language or particular assessments. No grading/Portfolio/bank activation.
- The seven other science courses use the same engine, with an honest
  `curriculum not loaded` state until official source material is verified.
- Only chapter title and planning notes are editable/saved. Local teacher
  overrides live at `~/GitHub/SCIENCE_Tools_Library/assessment_plans/<course>.json`,
  outside GitHub Transfer/public static data. Saves require exact course IDs,
  supported chapter IDs, expected revisions, same-origin JSON, and a size limit.
  The canonical curriculum JSON is immutable through the tool.
- The existing six source shell files/styles are preserved except the minimum
  shared navigation/backend/HTML/test changes required by this integration.
  No shared theme CSS, Dock icon, source chapters, Google Drive resources, or
  private student state was altered.
- New durable work record: `handoffs/SCIENCE_TOOLS_ASSESSMENT_PLANS_PHASE1_20261117.md`.
  Next: teacher review of 25 proposed Physics learning goals and evidence map,
  then explicit approvals and additional course-source adapters. Do not mark
  draft proposals as official during future builds.
