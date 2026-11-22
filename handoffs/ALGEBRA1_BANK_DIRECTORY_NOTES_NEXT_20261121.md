# Algebra 1 Bank Directory — Next: Learning Focus / Notes

## Installed navigation intent
- `/banks/section.html` is the new lightweight Bank Directory (no chapter selector or review export on the directory).
- `/banks/assessment.html` preserves the **complete existing** Assessment/Question Bank with its chapter data and review/extraction controls. Only the title/navigation label changed; embedded chapter JSON and external JS paths remain identical. It contains the same current assessment and reference content.
- `/banks/algebra1/warmups/index.html` remains the existing Warm-Up Bank, unchanged.
- `/banks/component.html?bank=notes` is the next-bank setup page; other planned component routes display honest setup placeholders. These placeholders do not claim content exists and contain no lesson data.
- Old bookmarked `/banks/section.html?chapter=X` and `?plan=...` routes redirect to `/banks/assessment.html` retaining the entire query/hash. No current lesson Builder files modified.
- `/banks/index.html` already points at `/banks/section.html`, so it now reaches the directory.

## Bank categories on the directory
1. Assessment & Reference: direct skill evidence, assessment extensions, summative MC, CPM Review & Preview reference.
2. Warm-Ups: Q1/Q2 and source-lesson Q3/Q4 + linked Q5/Q6, teacher-reviewed.
3. Learning Focus / Notes.
4. EX / YTI.
5. Launch.
6. Smarty Pants (optional).
7. Practice Sets & Activities.
8. Reflections / Exit Tickets.

## Next build: Learning Focus / Notes
- Review the **approved** Notability student style and `maps_memories` style contract before building production content.
- Current lesson I Can only; vocabulary and Methods & Meanings directly relevant to that lesson.
- Support teacher editing, source provenance, versions, and AI change requests.
- Do not borrow the Assessment Bank's question list as Notes or mix the review/question content.
- No speculative content is added by this directory transfer.

## Transfer safety
- The source was taken from the connected `CPM_Tools/banks/section.html` mirror on 2026-11-21, SHA256 1436594492c42eb7fc98c09791d4ca5577d436aae40d00257de2cbc72c7514ea.
- Exact-source hash guard for replacing the old directory target; new `assessment.html` is a byte-for-byte content-preserving copy apart from two visible title/header changes.
- `bank.js`, `bank.css`, embedded chapter data, warm-up bank, teacher-review stores, and the Builder are not changed.
- This is Curriculum Transfer — Local Only, with no automatic GitHub writes.
