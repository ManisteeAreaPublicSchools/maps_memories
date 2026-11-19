# MAPS Science — Lesson Pre-Build Review (required)

**Status:** Required workflow; 2026-11-18. Applies to each Science lesson packet, even before Lesson Builder exists.

## Before drafting any new lesson

1. **Open actual previous lessons.** Locate the immediately preceding student PDF/HTML and teacher key in the connected Drive mirror; look back two lessons when warm-ups or concepts may repeat. Do not rely only on a resource catalog or memory summary. Read the warm-up, notes, investigation, practice, and exit prompt.
2. **Log yesterday’s evidence.** Identify exactly which question or phenomenon students just studied, terms and representations already introduced, unresolved misconceptions, and what data they generated. Avoid inventing that students collected data when the prior lesson used a simulated/example trial.
3. **Design a genuinely different warm-up.** It should retrieve useful prior knowledge *and* add a new reasoning demand (e.g., evaluate a claim from data, design a control, interpret a representation, explain conflicting evidence). Do not repeat the same push-apart sketch or merely change masses, character names or numbers. Repetition is acceptable only when explicitly planned and labeled as review.
4. **Check source and pacing.** Read the lesson's publisher day plan, purchased Think Sheet/lab/guide and existing teacher-approved course catalog. Keep the 54-minute target and source lesson ID; don't add extra activities without trimming.
5. **Prepare teacher first page.** Every teacher guide opens with lesson summary, goal, pacing table with minute totals and student page references, bulleted materials, bulleted printing/distribution requirements, tech/equipment preflight and safety/backup steps. Teacher answer pages follow in student order and are keyed exactly.
6. **Use canonical course distribution (approved November 18).** Put each lesson directly in `~Curriculum/__MAPS_Courses/<Course>/ch_NN/lesson_id/` with `student.pdf`, `student.html`, optional `assets/`, and `teacher/teacher.pdf` or teacher HTML. No `lessons_google_drive` or `chXX_lessons` wrapper levels. Teacher-authored guides and answer keys **may be student-visible**; don't use secrecy as the assessment design. Never put identifiable student/grade/accommodation data or licensed third-party source files in a publicly shared lesson folder. Check the new course folder's sharing before posting to the agenda.
7. **Verify before delivering.** Render PDFs; visually check the warm-up and teacher overview, page count and clipping. Check calculation keys, simulation link annotations, file hashes, transfer destinations, and actual installer plan against the intended installed state. Mark iPad/Notability checks as pending unless completed on device.

## Physics 5.2.2 review example

- **5.2.1 (yesterday):** Two people on rolling boards push apart; students sketched directions and used mass/speed/momentum to reason about a system at rest before release. It also introduced a two-cart spring model, mass-ratio trials, and equal-opposite momentum.
- **5.2.2 (today):** Instead of another push-apart prediction, students read a prior **sample** mass/velocity result and evaluate a claim about what happens when *only red mass* changes. They choose a controlled variable and a measurement before opening the simulation.
- Teacher overview page precedes the six matching answer pages.


## Physics 5.2.2: progression and video-analysis simplification (November 18)

- Read the actual preceding student packet, not just its title. After 5.2.1's simulated explosion and mass ratios, 5.2.2 must produce a **new evidence type**: real cart motion measured by students in Vernier Video Analysis.
- A short CER from yesterday's model can follow the warm-up, provided the CER explicitly says whether its numbers are from the student's own saved data or an illustrative model example.
- Students already know Vernier; focus on exactly four readings: each cart's velocity before and after release. No software tutorial, detailed graph-analysis exercise, acceleration computation, or repetitive simulation trials.
- Keep before/after velocity measurement and the corresponding signed momentum products together. The live video and mass data are primary; the independently authored simulation is backup only.
- Teacher overview must lead the key and include timing, equipment, printing, live video-sharing and a genuine clip fallback. Teacher-authored guides can be public by teacher choice; student records and copyrighted publisher key/source material are different and remain protected.

## Canonical MAPS lesson root (November 18, 2026)

Use `maps_memories/standards/MAPS_COURSE_LESSON_DRIVE_STRUCTURE.md` as the authority for Physics, Algebra 1, and AP Calculus. The live destination is directly under `__MAPS_Courses/<Course>`; the old `__Physics/lessons_google_drive` and former course-specific `lessons_google_drive` roots are no longer current transfer targets. Check a prior lesson's actual parent before each build; if it uses obsolete nesting, normalize to the new direct chapter layout.
