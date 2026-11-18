# MAPS Science Tools — Assessment Plans Phase 1 / Next Review

**Date:** November 17, 2026 (America/Detroit)  
**Status:** Phase 1 implementation packaged for Local Only transfer; teacher Mac QA and learning-goal review remain.  
**Authority:** `maps_memories/standards/SCIENCE_TOOLS_FOUNDATION.md`, `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md`, teacher-provided Physics 107-day source, and live `SCIENCE_Tools` source. No GitHub writes by assistant.

## Handoff instruction for next session

Inspect `SCIENCE_Tools` and connected Drive mirror after the teacher applies this transfer. Open **Physics > Assessment Plans** and verify the Mac Dock app can load, browse, print, save and reopen teacher chapter notes. Then review the 25 Physics section learning-goal drafts, supporting skills, and evidence suggestions with the teacher. Do not approve or connect them to grade/Portfolio/question-bank generation without explicit approval. Preserve one shared engine for all eight science courses. Do not use obsolete Physics Tools or private student information. All future repository file changes return one Local Only curriculum_transfer/3 ZIP.

## Scope installed in Phase 1

- **One shared engine:** `SCIENCE_Tools/app/assessment_plans.js`, `app/assessment_plans.py`, `assets/assessment_plans.css` and two explicit endpoints under `/api/assessment-plans/<approved_course_slug>`.
- Existing `app/app.js` and mustard topbar route to Assessment Plans for all eight courses; no duplicate course navigation, theme forks or eight component copies.
- **Physics:** `data/source/Physics_107_Day_Course_Plan_20261117.md` (unaltered teacher upload) and `data/physics_assessment_plans.json` (structured reading-only curriculum map). The uploaded plan explicitly contains 107 core periods across 9 publisher-numbered chapters; 82 publisher lessons and 25 dedicated 54-minute readings; 9 test periods and Monday reviews outside that count. Teaching order: 1, 2, 3, 4, 5, 6, 10, 12, 9; omit 7, 8, 11.
- **Goals:** Exactly 25 proposed section goals plus supporting skills, derived from section descriptions, all `DRAFT_TEACHER_REVIEW`. Evidence suggestions (quick checks, some checkpoints, lab/CER custom evidence, and a separate chapter test slot) remain proposed/unscheduled. No source suggests they have been administered, graded, or approved.
- **Other 7 courses:** shared functional module and explicit `curriculum not loaded` message, not invented science units.
- **Teacher-only edit:** Chapter title and teacher notes, saved in `SCIENCE_Tools_Library/assessment_plans/<course>.json`, a local sibling of app source (not public GitHub or any transfer ZIP). Exact chapter and course allowlist, atomic replace, revision conflict, same-origin JSON POST; canonical goals are immutable.
- **Print:** one chapter or all chapters in continuous teacher-friendly view. Controls use one Science theme and preserve correct chapter numbering. Teacher Mac/Notability print appearance still needs live review.

## Source audit distinctions

CPM Tools Assessment Plans (`assessment_plans.js`, `assessment_plans.css`, Algebra 1 `data/algebra1_assessment_plans.json`, and `app/server.py`) provided the reference for chapter picker, collapsed skills/source lessons, print all, approval boundaries, teacher notes. CPM still has Algebra-specific routes and data fields; this Science module avoids copying those directly and does not imply its Assessment Builder/Portfolio systems are migrated.

## QA completed before transfer

- Source totals verified 9 / 25 / 107 / 82 / 25 and planned nine separate tests; all source-supported publisher-day entries retained, including combined lesson days and resource/pacing notes.
- Python `unittest` suite: 15 tests pass against a simulated local installation, including 8 course routes, draft statuses, course isolation, no public library file routes, source immutability, save/reopen and revision conflict checks.
- Python bytecode compile and JS syntax checks pass.
- Headless Chromium screenshot attempt could not complete in this execution environment. **Do not report visual browser QA as passed** until real desktop/mobile render checks succeed. Teacher Mac spot-check remains required.
- No live Mac filesystem or actual teacher notes were changed; tests use disposable temporary storage. No student data imported.

## Next review sequence

1. Apply ZIP with Curriculum Transfer — **Local Only**. Reload existing Science Tools Dock app (if launcher keeps old process running, stop/reopen to pick up the new API).
2. Physics > Assessment Plans: confirm original section numbers, source lesson descriptions, labs/simulations, and precise period counts; chapter 9 must appear last.
3. Print Chapter 2 and Print All. Confirm two-column skills/resources, readable page breaks, and notes in print; review on the teacher's Mac.
4. Save title/notes for Chapter 2, restart and reopen; verify persistence. Do not place private student information in notes.
5. Review draft Learning Goal statements and supporting skills one chapter at a time. Only after explicit user decisions should new review/approval controls be designed, and only later integrate Question Banks, Assessments, and Mastery & Evidence.
6. When other science course sources are available, add *data adapters only*, reusing the shared engine without second tool implementations.

**One transfer ZIP is the single deliverable.** No independent PM files or parallel installers. No Git operations performed.
