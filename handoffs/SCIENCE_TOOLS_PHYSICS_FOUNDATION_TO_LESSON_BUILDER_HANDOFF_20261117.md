# Science Tools / Physics — End-of-Night Foundation Handoff

**Date:** November 17, 2026 (America/Detroit)  
**Next session:** First Science Tools Lesson Builder lesson and CSS standard discussion.  
**Status:** Assessment Plans foundation reviewed, approval mechanism installed by transfer; teacher decisions pending. User has already installed the Pass 4 ZIP. This Pass 5 package is a patch layered on Pass 4.

## Current authoritative starting point

1. One **SCIENCE_Tools** app hosts eight courses through shared modules, not eight cloned apps. Physics has seeded plans; other courses remain unconfigured (do not invent them).
2. Physics source map is fixed at **107 core instructional periods**, composed of **82 publisher-based lessons + 25 dedicated 54-minute reading/consolidation periods** across **25 sections** and **nine chapters** in teaching order **1,2,3,4,5,6,10,12,9**. Chapter tests (nine) and Monday reviews are **outside** those 107; no invented school-calendar dates.
3. **29 teacher-facing draft I-can goals** organize **144 supporting skills**. This is intentional: supporting skills do not become separate Portfolio grades. The broad goals are not mechanically duplicated to inflate counts.
4. Pass 4 prepared 50 *unscheduled* evidence options, nine *existing test-period* coverage blueprints, original-task/lab alternatives, and purchased Question Bank **candidate numbers only**, all pending separate item/diagram/answer review.
5. Pass 5 includes a source/scope chapter-by-chapter teacher-review checklist (`maps_memories/curriculum/physics/PHYSICS_TEACHER_GOAL_REVIEW_PASS5_20261117.md`), and three explicit Science Tools review actions: **Approve goal**, **Needs revision**, **Return to draft**. No goals auto-approved; only teacher-approved, current-fingerprint goals appear in the read-only approved-goals endpoint. Nothing is written into future banks or Portfolio yet.
6. The teacher already applied Pass 4. Before continuing development, verify the installed Pass 5 transfer log and reopen Physics → Assessment Plans.

## Next morning — begin Lesson Builder, not Question Banks

- **First decision:** identify which Physics lesson we are making next and inspect the existing **5.1.1 pilot** as the classroom-tested reference. Do not assume that chapter 5 is the next chronological lesson; use the teacher's chosen next lesson and the original publisher lesson ID.
- **Second decision:** compare 5.1.1 and previous Physics packet observations to choose a **reusable, approved lesson CSS design**, then save design choices to `maps_memories` as a canonical Science lesson style. Do not invent a new CSS family from scratch or treat this evening's Assessment Plans CSS as final Lesson Builder styling.
- Remember classroom packet expectations: publisher lesson flow **Notes → Lab → Thinking Sheet** where source requires; early conceptual understanding rather than excessive calculation; important vocabulary with visible definitions for highlighting; generous blank work/drawing space; correctly formatted multiple-choice, mathematical expressions and meaningful, nonmisleading diagrams; working links to simulations and video labs.
- Output must work as a lightweight PDF for Notability. Reduce overly large/vector-heavy PDFs; verify links and page rendering. Students open Google Drive lesson link from the agenda, use Drive's **Send a copy to Notability** flow; avoid workflows that require manually rebuilding Canvas lessons.
- Lesson Builder is a **shared eight-course engine** with independent course catalogs and original source/lesson IDs; do not clone `_physics_teacher_tools`. Initial scope is the next Physics lesson, its editable assembly/styling profile, preview/print, and safe output handling. Publisher/licensed source documents remain private.
- When implementing new code, read up-to-date `SCIENCE_Tools` from connected Google Drive mirror first, use only **GitHub Transfer ZIP (`curriculum_transfer/3`, Local Only)** as the finished artifact, and never commit or push to GitHub automatically.
- Keep approval decisions, saved teacher notes, rosters and student evidence outside public repo paths. Future bank/Portfolio consumers must use `GET /api/assessment-plans/{course}/approved-goals` only, never read draft curriculum as approved material. No live bank/Portfolio integration exists yet.

## Future tasks deliberately deferred

1. Teacher goes chapter by chapter approving or flagging each goal in Assessment Plans; this is a real teacher decision, not a checkmark ChatGPT can assert.
2. After the Lesson Builder foundation and classroom trial, design actual question-bank families from approved goals and validated publisher figures/keys. No banks tonight.
3. Only when needed, wire Question Banks and Portfolio as separate consumers of the filtered goal feed. Approval never automatically becomes a grade.

## Source references and prior decisions

- `SCIENCE_Tools/data/physics_assessment_plans.json` — Pass 4 unchanged canonical map/evidence.
- `maps_memories/curriculum/physics/PHYSICS_LG_ALIGNMENT_PASS1_PASS2_20261117.md` — exact publisher outcome crosswalk, 29 goals.
- `maps_memories/curriculum/physics/PHYSICS_SUPPORTING_SKILLS_PASS3_20261117.md` — sampled textbook/purchased source validation and 144 skills.
- `maps_memories/curriculum/physics/PHYSICS_ASSESSMENT_EVIDENCE_PASS4_20261117.md` — evidence and purchased-bank text-screened candidate audit.
- `maps_memories/curriculum/physics/PHYSICS_TEACHER_GOAL_REVIEW_PASS5_20261117.md` — chapter checklist and explicit approval contract.
- `maps_memories/standards/SCIENCE_TOOLS_FOUNDATION.md` and `maps_memories/shared_ui/science/science-ui.css` — app foundation theme; Science mustard, teal, cream and terracotta.
