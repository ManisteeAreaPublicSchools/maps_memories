# SCIENCE TOOLS — Assessment Plans running-server repair

Date: 2026-11-17 (America/Detroit)
Stage: Post-install repair for the first Physics Assessment Plans implementation.

## What failed and why

The teacher applied `MAPS_Science_Assessment_Plans_Physics_Phase1_20261117_GITHUB_TRANSFER.zip` at 21:23:16, with 12 validated operations and successful post-apply verification. The teacher's browser subsequently showed the Assessment Plans heading and an empty body. The HTTP server process had started before the transfer and still held the earlier in-memory `ALLOWED_ASSETS`/route table. The old Python process could serve newly replaced `index.html` and `app.js` from disk, but it could not serve the newly introduced `/app/assessment_plans.js` or `/api/assessment-plans/physics` endpoint. The old Mac launcher saw a matching app identity and therefore merely opened the browser without restarting that server.

## Focused repair

- `SCIENCE_Tools/Start Science Tools.command`: check the explicit Assessment Plans capability in `/api/health`, not only the existing app marker. If it is missing, identify the localhost listening PID via `lsof`, verify the exact installed `SCIENCE_Tools/app/server.py` path using `ps`, terminate only that verified old process, then start the updated Python server. Fail closed instead of killing any unexpected service. Reuse the healthy server on ordinary app launches. No Git operations.
- `SCIENCE_Tools/app/app.js`: when the Assessment Plans client module is absent, render a visible error with Dock-app restart guidance. Never silently leave an empty tool root.
- `SCIENCE_Tools/tests/test_science_tools.py`: add regression checks that require both the capability-aware launcher and the visible fallback.
- `SCIENCE_Tools/README.md`: document required one-time relaunch after the Local Only transfer.

Other components, curriculum goals, 107-day plan, question banks, student data, reports, icon, style, and saved teacher notes are unchanged. Do not apply the original Phase 1 ZIP again; this is a small follow-up transfer.

## Expected user verification

After applying this ZIP with Curriculum Transfer — Local Only, click Science Tools in the Mac Dock **once**. The launcher stops the earlier verified same-app server and starts the version supporting `shared-engine-v1`. Open or reload Physics > Assessment Plans; Chapter 1, 107 core periods, nine chapters, 25 sections, draft goals, resources and evidence should appear. Browse Chapter 2 and confirm printing and local note save as desired. Refresh alone cannot add new Python routes to a stale process.

## QA

- 16 automated Science Tools tests passing, including existing privacy, source totals and save/reopen tests.
- Node/V8 simulated stale and loaded client states passing.
- Bash syntax and JavaScript syntax passing.
- Chromium UI screenshot attempted but the execution environment returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` for both local and fully intercepted test URLs. Actual teacher Mac browser verification is still required.
- Transfer schema: `curriculum_transfer/3`, Local Only. Manifest replacements specify exact SHA256 for currently mirrored installed files.

This handoff supplements `SCIENCE_TOOLS_ASSESSMENT_PLANS_PHASE1_20261117.md`. One shared engine remains the authority for all eight science courses. Physics learning goals remain drafts pending teacher review. No GitHub writes were performed.
