# Algebra 1 Bank Quality Pass V9 — 2026-11-22

## Scope and source authority
- Inspect the current **installed V8** question-bank UI and curated question data for Chapters 1–4. V8 installation was verified in the local-only transaction log.
- Preserve canonical `CPM_Tools/banks/data/CH01.json` through `CH04.json`, original CPM Review & Preview source, question IDs, previous teacher approvals, and review history. **None is replaced in this package.**
- New or edited displays are **PENDING_TEACHER_REVIEW**, with `assessment_eligible=false`; no automatic Builder or Portfolio eligibility.
- Section-level assessment learning goals, lesson-level practice Direct Skills, and four authentic CPM R&P problems per lesson remain distinct.

## Corrections completed
1. **Chapter 3 / 3.2 garden:** 12 variants previously placed an `x × x` reserved square inside a smaller garden, generating negative remaining area. The revised rectangular gardens have dimensions `(x+a) × (x+b)`, positive `a,b`, and explicitly assume `x>0`; the square fits and every remaining-area expression is positive. Independently checked symbolically.
2. **Chapter 3 / 3.2 comparison:** 12 variants called Board A larger even where it was smaller. All versions now have Board A wider and correct positive area differences, symbolically checked.
3. **Chapter 3 / 3.1 missing-side extension:** Replaced the one-operation `x⁷/x⁶` style with an applied area/width monomial task using coefficients and exponents. All 12 versions have positive dimensions and computed answers.
4. **Chapter 4 / 4.1 multiple choice:** Clarified that the $28 total **includes** a separate $6 delivery fee. This makes the $5.50/unit answer unambiguous. Original wording remains in the canonical source and as `source_original_student_html` on the curated display variant.
5. **Chapter 4 / parallel forms:** Added 11 draft numerical versions to **11 canonical Direct Skills IDs**, chosen across contextual checking, equal-values solving, substitution, two elimination methods, strategy choice, and a modeled system. The original version remains at position 1. Generated system answers are nonzero integers within `−5` to `5`; word-problem counts are whole-number and nonnegative. Correct solutions were verified by substitution and SymPy.
6. **Chapter 4 / extension:** Added a separate 12-version real-world **notebook and marker pricing** family that requires students to form and solve a two-equation system. The original scaled-equation extension is preserved unchanged and retains its review requirements.

## Coverage and QA
- Total family records: **583** (the Practice and Assessment views may reference the same source family separately). Total candidate records: **5949**.
- V9 changed or authored **280 candidate records**; all remain drafts, not auto-approved.
- Chapter 4 still has **60** one-version family records across its bank views. These are **not** presented as completed 12-swap pools.
- Original CPM Review & Preview indexed totals: Chapter 1 = 25, Chapter 2 = 50, Chapter 3 = 54, Chapter 4 = 66.
- Verified all 45 chapter/goal and chapter/lesson selections with the existing browser UI. Verified Chapter 4 numerical swaps, the new application extension, corrected multiple-choice display, and MathJax in the browser. No JavaScript page errors.
- Exact within-family HTML prompt duplication checks pass. This is **not** certification of every legacy answer key or the intended two-minute classroom time.

## Remaining priorities, without hiding source gaps
- **Ch. 1:** six lessons have fewer than four indexed *authentic* R&P problems: 1.1.1, 1.1.3, 1.2.1, 1.2.2, 1.2.4, 1.2.5. The lesson builder should choose appropriate source problems from other prior lessons if needed, never invent a fake CPM original.
- **Ch. 2:** several legacy families have fewer than 12 approved numerical variants. Do not pad the pool with repeated math.
- **Ch. 3:** staged 3.2.4 quartic-product families outside the active assessment-goal scope are not approved alternatives for a two-minute 3.2 check. Keep them excluded until independently reviewed.
- **Ch. 4:** finish the remaining one-version families, and independently review difficulty/answer keys of MC and contextual extension items. The new variants supply options but do not certify source keys.
- For future QA, sample student-facing printed questions, inspect diagrams, verify exact CPM source attribution, independently solve answer keys, and test approximately two-minute effort in class.

## Integration/consumer rule
The installed `ALGEBRA1_BANK_CONSUMER_CONTRACT_20261122.md` is updated. No changes to automatic Lesson Builder, Assessment Builder, or Portfolio selection behavior are claimed in V9.
