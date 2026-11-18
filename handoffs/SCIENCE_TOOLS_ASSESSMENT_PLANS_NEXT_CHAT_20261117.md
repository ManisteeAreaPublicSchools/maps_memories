# SCIENCE TOOLS — COMPLETE NEXT-CHAT HANDOFF: Assessment Plans

**Date:** November 17, 2026 (America/Detroit)  
**Status:** Science Tools eight-course shell installed; navigation cleanup packaged in this transfer; Assessment Plans **not yet implemented**.  
**Authority:** `maps_memories` contains shared standards/handoffs; `SCIENCE_Tools` is the owner-local executable source; CPM Tools remains the proven model for existing math implementations.  
**Delivery:** One GitHub Transfer / Curriculum Transfer v3 ZIP, Local Only; user commits/pushes manually in GitHub Desktop or GitHub Sync.

## Ready-to-paste instruction for the next chat

> Continue MAPS Science Tools with **Assessment Plans**. First read the entire `maps_memories/handoffs/SCIENCE_TOOLS_ASSESSMENT_PLANS_NEXT_CHAT_20261117.md`, `maps_memories/standards/SCIENCE_TOOLS_FOUNDATION.md`, and `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md` from the connected Google Drive mirror. Inspect the **current installed** `SCIENCE_Tools` and `CPM_Tools` sources before making changes. Start with an audit of the working CPM Assessment Plans system and propose a shared Science Assessment Plans model. Do not reuse legacy Physics Tools or import private student records. Deliver changes only as a verified Local Only GitHub Transfer ZIP, no GitHub writes.

## 1. Why Science Tools is being built

The user is establishing a district-wide, portable, local-first suite of teacher-facing tools for MAPS. The experience should feel familiar to existing CPM Tools: open the **Science Tools.app from the Mac Dock**, get the same high-level landing page and two-column course-card navigation, with distinctive **spiced mustard** coloring rather than CPM navy. Clicking a course opens a grid of ten tools. Tools currently navigate to honest placeholders; never call them functional before they really work. User has repeatedly asked not to overbuild a speculative interface or salvage obsolete Physics Tools.

### Locked UI structure

Header: spiced mustard primary (#D39832), deep-teal ink (#163D42), warm cream (#F7EEDB), secondary terracotta (#AE5238). Use the existing custom Science Dock icon, no generic/lame emoji icon. This is a **CPM-style header and two-column card grid**, not the prior sidebar/dashboard prototype.

- Header navigation: **Science Tools** and **Current Course** buttons, persistent on all views. Current Course is enabled when a course is selected, disabled on course-list home.
- The lower redundant `Science Tools / Physics` breadcrumb and underline have been intentionally removed, as have duplicate in-panel Back-to-Course and All-Science-Courses buttons. Do **not** re-add another in-page course selector; rely on top header controls.
- The page retains normal titles (`Physics`, `Assessment Plans`, etc.) and course context in subtitles.
- The course grid renders all eight from `SCIENCE_Tools/config/courses.json`: 6th Grade Science, 7th Grade Science, 8th Grade Science, Physical Science, Biology, Chemistry, Anatomy/Physiology, Physics.
- The course workspace is one shared `SCIENCE_Tools/app/app.js` implementation, not eight forks.

### All ten approved Science course tools (exact labels and basic jobs)

| Tool | Initial purpose |
|---|---|
| Planner | Course calendar, instructional days, pacing and unit sequence. |
| **Assessment Plans** | Learning goals, supporting skills, planned evidence and chapter/unit assessment design. **Next target.** |
| Lesson Builder | Notes, examples, You Try Its, labs, simulations, student and teacher guides. |
| Visuals & Printables | Graphs, diagrams, visuals, printable materials and media resources. |
| Assessments | Practice, Quick Checks, Checkpoints, Tests, Custom; paper-first. |
| Question Banks | Reusable vetted science items linked to learning goals. |
| Mastery & Evidence | Portfolio, accepted evidence, student progress, reports. |
| Launches & More | Course launches, structured investigations and explorations. |
| Library | Approved and teacher-created materials, save/reopen. |
| Course Setup | Course configuration, delivery sources, future data integrations. |

## 2. Actual installed local file architecture

Paths relative to `~/GitHub`:

- `SCIENCE_Tools/Science Tools.app` — Mac Dock application. Stable local server: `127.0.0.1:8786`.
- `SCIENCE_Tools/Start Science Tools.command` — manual fallback.
- `SCIENCE_Tools/app/index.html` — CPM-style header shell.
- `SCIENCE_Tools/app/app.js` — **single** course/tool navigation implementation.
- `SCIENCE_Tools/app/server.py` — Python stdlib-only localhost server; only whitelisted public UI assets and `/api/courses`/`/api/health`, no private file routes. Do not broaden file access casually.
- `SCIENCE_Tools/config/courses.json` — eight-course registry.
- `SCIENCE_Tools/assets/science-ui.css` — identical bundled fallback CSS.
- `maps_memories/shared_ui/science/science-ui.css` — **authoritative CSS** served live when local mirror is present; changes affect all eight Science courses.
- `SCIENCE_Tools/tests/test_science_tools.py` — local smoke/invariant tests.
- `maps_memories/standards/SCIENCE_TOOLS_FOUNDATION.md` — source of architectural decisions.
- `maps_memories/standards/MAPS_COURSE_ARTIFACT_NAMING.md` — approved course-first naming convention.

GitHub Sync includes the district `maps_memories` repository and succeeded for all five repositories after its remote was changed to SSH. **Never commit, push, pull, or synchronize automatically** in assistant workflow. Drive mirror for the local workspace lets the assistant read actual local source; public GitHub can temporarily lag uncommitted transfers, so reconcile rather than overwrite newer mirrored content.

### Source and publishing principles

- **One component change affects all Science courses.** Shared UI source lives in district `maps_memories` and bundles/offline fallbacks in the app. Avoid eight parallel solutions.
- `maps_memories` should contain **code and standards only**, no real student roster, guardian emails, IEP/504, accommodations, grades, teacher review or Portfolio evidence.
- The executable `SCIENCE_Tools` source remains a local teacher tool, with code-only mirrored diagnostics where approved. No private student state should enter public GitHub or transfer payload.
- The original `_physics_teacher_tools` and `~Curriculum/__Physics` are **legacy**, to be preserved but not used to seed Science Tools. No migration or destructive cleanup.

## 3. Google Drive structure (fresh Physics, not moved)

User made `~Curriculum/__MAPS_Courses`. A previous accidental move of `~Curriculum/__Physics` was **reversed and verified**; its original contents were preserved. A **new empty** `~Curriculum/__MAPS_Courses/Physics` was created, containing a newly created `lessons_google_drive` folder. This is the **new** Physics destination for future course materials. The separate old `~Curriculum/__Physics` must stay untouched.

`__MAPS_Courses` can later include other courses; Algebra 1 and AP Calculus have **not** been migrated and their current delivery destinations must not be broken. Physics public/original interactives may eventually be delivered to `~/GitHub/physics/lessons` by explicit design, but don't import the previous Physics Tools code or unapproved old resources automatically.

### MAPS Student Data — future only

`~Curriculum/__MAPS_Student_Data` (user's district-managed school Google Drive) is a planned single administrative source; **not integrated yet**:

| Information | Who maintains |
|---|---|
| Student & Guardian Directory, one grades 6–12 sheet keyed by PowerSchool ID | District data administrator |
| PowerSchool rosters (courses/sections/periods/teacher) | District data administrator |
| NWEA exports by year/testing window | Curriculum director |
| PowerSchool export template specs | Teacher/user |
| Student Services quick-reference and detailed accommodations/IEP/504 information | Special education teacher consultant with established restricted sharing |

Teacher tools should eventually read authorized snapshots; never create parallel manual sources or allow general access to protected student information. Student data is excluded from all GitHub/Curriculum Transfer payloads. The user may later transfer Drive ownership to a district Shared Drive; that is not a prerequisite to work.

## 4. File naming — new explicit rule

Student and teacher lesson files must be named **course first, lesson second, resource type third** to remain recognizable inside Notability. Examples: `Alg1_3.1.2_Lesson_Student.pdf`, `Phy_5.2.2_Lab_Student.pdf`, `Phy_5.2.2_Simulation.html`. Further course-prefix assignments must be approved before use. Preserve original numbering (e.g. `5.2.2`). Do not globally rename existing lessons. Implement a shared naming helper when builders actually emit files; don't maintain eight different formatting functions.

**Stable Google Drive file links:** Replacing a Drive file by the Google Drive API can preserve its file ID/URL, but overwriting a locally synced file **does not guarantee** that. An authenticated in-place-update integration is desirable later but is **explicitly low priority now**; do not delay Assessment Plans for this.

## 5. Assessment Plans: scope for the next chat (do not build blindly)

The user asked to work on Assessment Plans next, using the working CPM Tools experience rather than reinventing the wheel. The next chat should **first inspect**:

1. Current `CPM_Tools/assessment_plans.js`, `assessment_plans.css`, `app/server.py`, and any shared assessment plan backend/contracts in the live Drive mirror.
2. Current `CPM_Tools/PROJECT_START_HERE.md` and `docs/SHARED_SYSTEM_CONTRACT.md` for the successful one-engine/seven-course strategy and implementation boundary. CPM Assessment Plans are an architectural reference, not blindly copied or declared functional in Science Tools.
3. The actual Physics curriculum learning goals, 107-day pacing work, resource catalog and simulations/video labs from the Physics Build project's authoritative sources. Do not invent missing goals, sequence or schedules; ask for verification if the source is unresolved.
4. Science shared UI source and course registry listed above; do not fork the ten-tool grid.

### Suggested Assessment Plans acceptance goals for discussion

- One generic assessment-plan engine usable by all eight Science courses, with **course-specific data** separate from UI/logic.
- Appropriate unit/chapter naming for science; explicit learning goals and supporting skills connected to multiple evidence opportunities.
- Assessment categories compatible with approved paper-first workflow: Practice, Quick Check, Checkpoint, Test, Custom. Student evidence is scanned duplex and teacher reviewed; **do not** replace this with mandatory Canvas quizzes or bubble sheets.
- Distinguish reusable assessment-plan metadata (potentially public) from real student assessment results and confidential records (private).
- Scaffold first for Physics with user-approved 107-day plan, then other courses once source materials and standards are verified.
- Honest status indicators: a card may open a planning tool only after it is implemented and tested; no dead-link success claims.
- Do not import old Physics Tools curriculum, source files or legacy assessment state without explicit authorization.
- Use shared CSS, accessible control sizes, consistent top header navigation, printable teacher views as needed.
- Preserve official section numbering in names and exported files.

### Suggested execution sequence

1. Audit CPM Assessment Plans and identify reusable interface/logic, missing science fields, data model, and dependencies.
2. Show the user a compact comparison and the proposed Science Assessment Plans structure; settle needed distinctions (learning goals vs skills; unit vs chapter; evidence map).
3. Implement one course-agnostic functional slice and Physics config only after sources are verified.
4. Run all existing Science shell tests plus Assessment Plans focused tests, browser render QA on desktop/mobile, state roundtrip/save/reopen if enabled, and privacy/transfer safety checks.
5. Deliver one Local Only GitHub Transfer ZIP with exact expected prior SHA for replacements and all durable standards/handoffs updated. Never send separate PM files as parallel deliverables.

## 6. GitHub Transfer / Curriculum Transfer contract

Current schema `curriculum_transfer/3`:

- ZIP root contains `TRANSFER_MANIFEST.json` and `payload/<approved_root_alias>/<relative_path>`.
- `create` for new files; `replace` only with **exact** existing SHA256; no unapproved destinations and no private student content.
- Approved root aliases currently include `science_tools` → `SCIENCE_Tools`, `maps_memories` → `maps_memories`, and `memories` → `memories` (plus others).
- **Local Only** application, no assistant GitHub writes. User reviews and commits/pushes separately with GitHub Desktop or GitHub Sync.
- Do not assume a synced local Drive overwrite preserves a Google Drive share URL.
- Verify a patch against the current installed Drive mirror; published GitHub may lag an unapplied/uncommitted local transfer.

## 7. What this handoff transfer changed / did not change

Changed:

- Removed secondary in-page breadcrumbs and decorative mustard underline from the course/tool pages and home.
- Removed duplicate in-panel back/all-course buttons from empty tool placeholder pages; top header remains navigable.
- Removed dead breadcrumb/accent CSS from authoritative `maps_memories` theme and identical local Science Tools fallback.
- Added a documented, course-first lesson naming contract for Notability.
- Updated Science Tools and MAPS foundation readmes, added handoff, expanded regression test.

Not changed:

- No Course/Assessment Plans backend logic, student data integration, teacher saved records, legacy Physics materials, Google Drive lesson files, application launcher or icon, course registry, assessment evidence, or old academic repository files.
- No Google Drive files/folders created or moved in this patch.
- No Google Drive API in-place file updater; leave for later.
- No GitHub write, commit, push or pull.

## 8. How the teacher confirms the result

Apply this one ZIP with Curriculum Transfer — Local Only. Open or refresh the existing Science Tools Dock app at `http://127.0.0.1:8786/`, select Physics (also spot-check another course), then open Assessment Plans. The **mustard appbar still contains Science Tools / Current Course buttons**. The body contains only the course or tool title, not the redundant `Science Tools / Physics` breadcrumb or underline. Header buttons navigate home/course. Assessment Plans remains an honest placeholder until built.

### Immediate next request

**Start Science Tools Assessment Plans, using the existing CPM Assessment Plans as a reference, with one reusable engine across eight Science courses.** Begin with an audit and discuss the actual plan design; no premature import of old Physics materials.
