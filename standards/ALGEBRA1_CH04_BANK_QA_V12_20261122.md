# Algebra 1 Chapter 4 — V12 focused quality pass (November 22, 2026)

**Status: teacher-review draft.** V12 builds on the installed V11 Chapter 4 substantive rebuild. It is not automatic assessment or Portfolio approval.

## Question-quality corrections

- **Graph integrity:** Recomputed the clipping endpoints for all 48 new Chapter 4 graph variants. The V11 generator could place both endpoints at a corner and render a line as a single dot. Four such instances were found; all 48 graph segments now have nonzero, correctly placed line strokes.
- **Elimination scaling:** Replaced 60 versions across five Practice/Assessment families so that labels and student instructions really require scaling one or both equations before eliminating x. The old variants sometimes required no scaling at all.
- **Real question variety:** Replaced an overlapping 'two orders, two prices' family in Chapter 4.3 (24 versions across Practice and Assessment) with a rectangle/garden problem using perimeter and dimension-difference constraints plus a follow-up changed-design check.
- **Task length:** Adjusted 24 versions of 'Choose methods for two systems' so students choose an efficient method for each but solve only the first system, rather than having two full systems consume one short-task slot.
- **Meaning and notation:** Corrected the ambiguous 'nearest feasible total' instruction in an extension (12 versions), cleaned signed coefficients in 12 Test MC substitution-choice versions, and removed `+-` from 12 extension answers.

## Audits and evidence

- 141 Chapter 4 bank family IDs and 1,692 variant IDs **preserved**. No artificial new family quota or number-swap pool was added.
- **240 of 240 Chapter 4 Test MC variants** passed an independent check that their displayed question has exactly one correct option, matching the key.
- **396 printed linear-system solution pairs** checked independently by substitution; no mismatches found. Other item types (contexts, graph interpretation, construction tasks) are not counted as if the same test applied.
- **48 of 48 embedded line graphs** passed geometry checks following repair.
- Browser checked 14 chapter/lesson/goal navigation and swap cases including Chapters 1–3 regression, with no page errors and offline MathJax working.
- No exact prompt duplicates within a 12-variant family. Canonical textbook `CH04.json`, original CPM Review & Preview, all teacher review history, and Chapter 1–3 bank content were not changed.

## Continuing rules for other curriculum tools

Practice is **lesson-indexed**. A future lesson selects spiral Direct Skills from earlier lessons, while its four authentic CPM Review & Preview choices are a separate step. Assessment is **section-learning-goal-indexed**; Multiple Choice is for Tests, and optional Extensions can be used in Quick Checks, Checkpoints, or Tests. Count a coherent multipart task as one family, and let a complete system solution or substantial algebraic product stand alone. No new or edited draft should be promoted without teacher review.

**Remaining teacher judgment:** Verify student-facing reading load, actual classroom timing, the suitability of difficulty and transfer tasks, and final release/approval. V12 does not claim universal certification of 1,692 variants.
