# Algebra 1 Portfolio | Learning Goal Grading Philosophy

**Version:** 1.2 / Pass 4 authentic-task calibration - 2026-11-23  
**Status:** CENTRAL WORKING STANDARD / PASS 4 TASK-LEVEL PILOT, NOT CERTIFIED FOR AUTOMATIC GRADING; unresolved teacher decisions flagged  
**Canonical location:** `maps_memories/standards/portfolio_grading/ALGEBRA1_PORTFOLIO_GRADING_PHILOSOPHY_V1_20261123.md`  
**Scope:** Algebra 1 CPM **section** Learning Goals, formative assessment evidence, trend grades, teacher review, and the future Portfolio recommendation engine.  
**Application status:** POLICY ONLY. CPM Tools does not yet consume this file. Passes 3-4 checked existing private records (in aggregate and by de-identified task patterns) without changing grades, teacher approvals, or software. See PASS3_VALIDATION_FINDINGS_20261123.md and PASS4_TASK_COLOR_CALIBRATION_20261123.md for limits and teacher decisions.

## 1. Authority and boundaries

1. **CPM section goals** are the reporting units. Maintain one evolving letter grade and one independent five-square growth display per taught CPM section Learning Goal (`ALG1-S3.1`, `ALG1-S3.2`, etc.). The canonical statement and ID remain in `CPM_Tools/data/algebra1_assessment_plans.json`; do not duplicate or invent new goals here.
2. **Learning Goal evidence, not skill quotas.** Assessment questions are selected by section Learning Goal. Supporting skills organize instruction and personalized **practice**, but the grade engine must not require an arbitrary number of performances of each skill.
3. **An assessment task is one evidence item.** A complete bank family/variant counts as one assessed task, even if its question has parts a–e. Preserve part scores, exact source, original scanned work, and feedback in the evidence archive. Do not count each brief subpart as an independent attempt toward a quota.
4. **Teacher judgment is final.** Python may compute a *working recommendation* for an existing goal dropdown, but no recommendation is automatically a teacher-approved grade. An explicitly teacher-entered/approved grade takes precedence. Save, publish, email, and export are separate reviewed actions.
5. **Safety and privacy.** Original student scans, roster IDs, recorded question work, comments, grades and evidence histories remain only in private `CPM_Tools_Portfolio_Data`, never in `maps_memories`, a GitHub Transfer ZIP, or public student pages. No changes to scanned originals, applied approvals, or existing teacher grades are allowed as a side effect of adopting this document.

### Source precedence for this policy

- Newer *explicit teacher decisions in the 2026-11-23 Portfolio grading discussion* govern the pedagogical model where they contradict November 8–16 historical interpretations.
- The November 8 chapter-assessment philosophy and November 9 grading reference remain sources for the approved section-goal structure and meaning of letter-grade trends.
- `CPM_Tools/memories/portfolio/PORTFOLIO_WORKFLOW.json` remains the active **operational** contract until a later controlled migration. This document does not claim to override the running application.
- Current bank/question approval statuses, exact original problem text, and teacher-reviewed source inclusion remain their own authorities. A new philosophy does **not** automatically certify a draft question or a historical evidence link.
- If a grading rule conflicts or lacks teacher-confirmed meaning, **do not silently resolve it in code**: flag it for teacher review and keep existing student records unchanged.

## 2. Assessment collection beginning after Thanksgiving break 2026

The intended new classroom rhythm is **about four Quick Checks each school week**. This is a schedule for collecting useful observations, **not** four mandatory attempts for each Learning Goal, a minimum number of green judgments, or a deadline for acquiring a grade.

- **Quick Check:** Front assesses the current section Learning Goal; back assesses a previously taught Learning Goal that needs additional evidence. Both sides together target about eight minutes under the bank's current design contract. A student may receive different judgments for different Learning Goals on the same sheet; do not combine them into a fictitious chapter grade.
- **Checkpoint:** Select complete core tasks and optional eligible extensions for the taught Learning Goal(s). Its breadth and independence can yield stronger evidence than a shorter Quick Check; no checkpoint is required each week.
- **Chapter test:** Purposeful comprehensive evidence for the relevant Learning Goals. A full **A** recommendation is reserved until strong, independent chapter-test evidence confirms proficiency at the taught expected depth. Test participation alone does not earn A. Do not require an unrelated transfer/extension task as a prerequisite.
- **Assessment Builder:** The old AP1/AP2 selector is intentionally **not yet migrated** to the new section-goal Assessment Bank. This is planned integration, not a reason to change the grading model back to AP1/AP2.
- **Bank eligibility:** Use teacher-reviewed, assessment-eligible bank variants only when the new builders are connected. Unapproved draft questions must not silently become graded evidence.

**Time window:** A student's evolving LG grade considers *all relevant approved historical evidence* for that goal. Current-week email/report assessment-history lists may still show only the Monday–Sunday week's verified assessments. The weekly reporting filter must never erase earlier evidence from the grade calculation.

## 3. Minimal private Learning Goal evidence record (design contract; not yet implemented)

Use a logically separate record per section goal, for example `ALG1-S3.2.json` in the **private** Portfolio data store. The grid can be seen as `student | item 1 | item 2 | item 3 ...`. Each `item` is an assessed *complete question family/task* associated with a dated assessment, not a supporting skill or a fabricated number of attempts.

Retain sufficient metadata behind each colored cell to explain and audit it:

- `student_key` (private PowerSchool roster identifier), `section_goal_id` (canonical ID), `assessment_run_id`, `assessment_type`, `assessment_date`, `task_id`, `family_id`, `variant_id` (when available), and any relevant source-page references.
- `judgment`: `red`, `yellow`, `green`, or **no judgment** (null/absent) if not scorable. Maintain distinct `absent`, `not_submitted`, `unreadable`, `pending_teacher_review`, and `not_assessed` states; do not convert any of them into a red or a zero.
- `teacher_approved_to_count`, `review_source_revision`, `independent_work` where known, task breadth/depth, and optional feedback. Preserve a student's prior events; never replace the historical row when a new task arrives.
- Grade view fields: `working_recommendation`, `recommendation_reason`, `confidence_or_review_flag`, `saved_grade`, `saved_grade_origin` (teacher vs accepted recommendation vs legacy/unknown), and `saved_grade_reviewed_at` when verifiable. Never infer legacy provenance without proof.

**Single task, one color.** Multipart tasks receive one holistic red/yellow/green judgment for the Learning Goal, while part-by-part grading remains available behind it. One task may only contribute to another Learning Goal when its actual question content and approved mapping explicitly support that additional goal; never duplicate evidence by assumption.

### Working meaning of colors — provisional descriptors needing teacher validation

| Evidence judgment | Practical meaning for that task | Exclusion |
|---|---|---|
| **Green** | Convincing independent demonstration of the *goal portion* assessed by the complete task. | Not automatically an A, a completed whole LG, or five growth squares. |
| **Yellow** | Partial or inconsistent understanding on the assessed task, with evidence of a workable idea. | Not an arbitrary percentage range, automatic C, or proof of a missing prerequisite skill. |
| **Red** | Readable, reviewed student work demonstrates a substantial current misunderstanding of the assessed task. | Never use for blank scans, absences, incomplete files, or uncertain transcriptions. |
| **No judgment** | Insufficient usable evidence to judge the task. | Never impute a red, F, failure, or absent opportunity. |

These descriptions are **candidate operational definitions**, not yet a validated student-by-student scoring rubric. Pass 4 examined authentic task patterns and created teacher calibration questions; the color choices are not yet teacher-approved. See PASS4_TASK_COLOR_CALIBRATION_20261123.md.

## 4. Principles for estimating a current letter grade

A **holistic and explainable recommendation**, not a mathematical average, a green-count threshold, or a skill-by-skill evidence quota:

1. **Current demonstrated understanding.** Consider what the most convincing *recent independent* work shows about the currently taught scope of the section Learning Goal.
2. **Trajectory and consistency.** An improving red → yellow → green history matters; a later convincing demonstration can supersede earlier difficulty without requiring a fixed number of repeat greens. One new mistake should not automatically wipe out prior mastery. An abrupt contradiction should be surfaced for teacher review.
3. **Strength/breadth of the observation.** Compare what tasks actually cover, whether they were independent, and whether they are introductory Quick Checks, broader Checkpoints, or chapter-test evidence. Do not assign a mechanical multiplier by assessment name or give four weekly checks four equal 'votes.'
4. **Completeness and uncertainty.** A recommendation may be *Too Soon to Grade* when evidence is genuinely insufficient; a single strong task can still be meaningful. Never demand a fixed minimum number of attempts; when the coverage is narrow, communicate lower confidence or request review rather than fabricate certainty.
5. **Teacher authority and traceability.** Every calculated recommendation should explain its rationale in plain language and cite the source assessment/task IDs internally. Teacher corrections persist and are not overwritten by future suggestions.

No `average_credit / 5 -> percentage -> letter`, no automatic grade from five progress squares, and no 'each skill must be attempted N times' rule.

### Grade language and provisional ceiling

| Label | Meaning / policy |
|---|---|
| **A** | Strong independent proficiency at taught expected depth, corroborated by appropriate **chapter-test evidence**. Reserved until after the test. A test occurring is not sufficient by itself. |
| **A−** | Exceptionally strong performance on assessed material, trending toward A; **highest pre-test/provisional recommendation**. |
| **B+** | Solid B-level understanding, **trending toward A**. |
| **B** | B-level understanding after final evidence supports a stable plain-letter designation, or an explicit teacher decision. |
| **B−** | B-level understanding, **trending toward C**. |
| **C+** | C-level understanding, **trending toward B**. |
| **C** | Developing understanding with meaningful gaps, after final evidence supports a stable plain-letter designation or teacher decision. |
| **C−** | C-level understanding, **trending toward D**. |
| **D+** | Limited demonstrated understanding, **trending upward toward C**; confirmed by the fourth calibration example below. |
| **D, D−, F** | Existing UI choices, but no sufficiently verified general recommendation thresholds in the reviewed policy. **Do not invent cutoffs**. Keep in teacher review / pending calibration. |
| **A+** | **Not used** for section Learning Goal grades. |
| **Too Soon to Grade** | There is not enough reliable, relevant approved evidence to make a defensible letter-grade recommendation. It is not failure. |

**Before chapter-test confirmation**, generated interim grades should communicate direction with plus/minus symbols rather than default to plain A/B/C/D. Existing teacher decisions remain untouched. **After final test evidence**, stable plain letters may be appropriate where supported; plus/minus can still communicate an observed direction. Do not map percent bands to these grades.

## 5. Four teacher-supplied calibration cases (not universal formula lookups)

Assume each task is relevant and its red/yellow/green judgment is reviewed. These are *starting expected outputs* for Pass 3 regression tests, not automatic mappings for every possible task depth.

| Case | Chronological approved task judgments | Expected interim recommendation | Teacher's rationale |
|---|---|---|---|
| Student 1 | Red → Yellow → Green | **C+** | Encouraging improvement; current proficiency needs further corroboration before B. |
| Student 2 | Green → Green → Green | **A−** | Consistently strong, but reserve A until convincing chapter-test evidence. |
| Student 3 | Yellow → Green → Green | **B+** | Solid understanding with evidence of upward movement toward A. |
| Student 4 | Red → No usable judgment → Yellow | **D+** | Limited demonstrated understanding, but partial progress and upward direction. |

The fourth case has a **missing evidence cell**, not an explicit red. Examples do not authorize counting colors or placing all students into exact letter bins without reviewing assessment scope and evidence quality.

## 6. Working grade, saved grade, disclosure, and growth bars

- Python displays a **non-destructive recommendation** in the existing Portfolio grade workflow. Distinguish the recommended grade from an explicitly teacher-approved/saved grade in provenance; a saved teacher choice always wins.
- **Recalculation does not mutate saved grades, prior delivered reports, or evidence histories.** If provenance of an existing saved grade is ambiguous, preserve the value and flag it for teacher review; do not treat it as a confirmed teacher judgment or silently replace it.
- Checking a Learning Goal's **Email / Export** control chooses whether that goal's *approved/disclosable* grade may be included. A checkbox does not create evidence or approve a calculated grade. If no shareable grade exists, email may say `Too Soon to Grade`, and PowerSchool export leaves that goal blank. Sharing requires the existing explicit teacher review and send/export steps; nothing auto-posts to PowerSchool.
- The existing **five-square growth bars** remain separate visual judgments. Their current single-assessment two-bar cap and teacher-save constraints are **legacy operational rules until independently redesigned**; the bars are not the source of the letter grade. Source-specific assessment credit is not LG mastery.
- The **question-level score (0–5 half-points)** remains part of original assessment feedback, not the LG grade scale. A proposed colored judgment must derive from reviewed *meaningful work*, not blindly from that number.
- Approved question scores and `count_as_evidence`/included I Can judgments are separate decisions: do not count an excluded or unverified question simply because it has a non-null score.

## 7. Conflict register — what supersedes what

| Prior location / rule | Disposition for NEW LG grading | Existing runtime impact |
|---|---|---|
| `app/portfolio_approved_review.py`: November 16 fixed Q1a–Q2b exponent / rectangle-score formula and particular-question gates for A−/B+ | **SUPERSEDED** as a general LG recommendation method. Use evolving approved LG-task evidence, not a single named assessment. | Current Python is **not modified** in Pass 2. Replace in one coordinated later implementation. |
| `PORTFOLIO_WORKFLOW.json: report.approved_assessment_section_proposals.never_auto_assign_letter_grades=true` versus the Nov 23 automatic recommendation code | **CLARIFIED**: no automatic *approval/recording/publication* of a grade; read-only Python working recommendations are allowed once validated. | Operational contract continues to enforce its current behavior; no edits in Pass 2. Future migration must reconcile the key explicitly and test safeguards. |
| November 8/9 A allowable after sufficient final exposure (not necessarily a chapter test) | **SUPERSEDED by the teacher's newer 2026-11-23 A rule**: A follows convincing chapter-test confirmation; A− is interim ceiling. | Existing recorded A grades are preserved pending review. |
| Skill-specific repetition rules, legacy 'two convincing observations' gates, numeric minimum-questions heuristics | **SUPERSEDED for NEW LG letter grades.** No fixed per-skill or per-goal attempt quota. | Historical ladder and practice records remain unchanged; only grading logic migrates later. |
| Five-square half-bar proposal based on November 16 credit (one assessment max two bars), older four-bar version | **NOT the letter-grade source**. Resolve bar display separately from LG grading and prevent mixing these formulas. | Retain currently enforced operational bars pending a separate review. |
| Plain A/B/C/D as automatic interim recommendations | **SUPERSEDED**: trend-bearing +/- provisional grade language; no automatic A before test. | Do not rewrite saved teacher grades. |
| Legacy grade recommendation without reliable evidence inclusion / provenance | **SUPERSEDED**: teacher approval and evidence provenance are prerequisites for a recommendation to count toward an official grade. | Do not delete imported results or mutate teacher review decisions. |
| Current-week-only history in weekly reports | **RETAIN for reporting only**. Evolving grade uses cross-week relevant evidence. | No report filter changes in Pass 2. |
| Existing five-square bars, linked skills, long-term Essential Standards/ladders | **RETAIN as separate displays/instructional references**. | Do not auto-infer a long-term ladder rung from a goal grade. |
| Original scanned responses, teacher correction history, contacts, published URLs and delivery safeguards | **RETAIN without changes**. | No data migrations or publishing in Pass 2. |

## 8. Unresolved items — do not silently fill

1. **Teacher's original 'three rules': NOT LOCATED VERBATIM.** The teacher stated they want to use *some* of their three rules. No verified source in the reviewed documents or available conversation history contains their exact original wording. Do **not** write three invented rules, mark them approved, or implement an approximation. Recover the exact text in the review stage; add only the applicable parts by explicit teacher approval.
2. **Red / yellow / green thresholds:** The plain-language descriptions in §3 are provisional; real student work is needed to calibrate their consistent application. No numerical score-to-color cutoffs are authorized by this document.
3. **Lower-end rubric:** D+ is anchored by a specific teacher example, but D, D− and F automatic recommendation criteria are not confirmed. Missing/blank/unreadable work is not automatically red, zero or F.
4. **Evidence strength without quotas:** Rules for mixed/contradictory demonstrations, task depth, incomplete test participation, and highly uneven coverage must be checked against real marked assessments in Pass 3; never invent a fixed points/weights formula to close gaps.
5. **Grade provenance migration:** Existing saved dropdown values may combine teacher actions with previously accepted Python proposals; preserve first, inspect before attributing origin.
6. **Growth-bar interpretation:** The five-square reporting rubric and legacy single-assessment cap are out of scope for grading-policy consolidation; review separately, leaving them operational.

## 9. Pass 3 validated boundaries and next release gate (2026-11-23)

**Pass 3 status: CONDITIONAL / NO ENGINE RELEASE.** Existing private Chapter 3 data were audited in aggregate against this policy. The saved dropdown grades contain substantial evidence-scope and provenance uncertainty. Review approval of question credit is *not* the same as approval of a current section Learning Goal evidence judgment. Therefore no retrospectively inferred red/yellow/green events or letter grades can be certified or installed as part of Pass 3.

Confirmed/strengthened safeguards:

1. **Current LG evidence inclusion is explicit.** An older `LG 02-ican`/`LG 03-ican` inclusion flag, or an approved 0-5 credit field, does not automatically authorize `ALG1-S3.1` or `ALG1-S3.2` judgment. Crosswalk and holistic task-color decisions need explicit teacher-reviewed attribution to the present section goal. When inclusion is unverified, preserve source work as archived/instructional context, not grade-bearing evidence.
2. **Differentiate source categories inside a combined run.** A returned review can contain formal Quick Check questions, individual practice, and Find Someone Who collaboration. `assessment_run_id` alone is not a sufficient source identifier. Preserve actual source file, assessment type, task grouping, and verified independence; collaborative/workshop items can guide practice without automatically proving independent proficiency.
3. **Count meaningful *tasks*, not subparts or raw question records.** A five-part exponent problem is one holistic task when authored as one family; its part credit remains supporting context. Two rectangle products are two tasks but may still cover a narrow slice of a larger section goal. No requirement for a fixed number of times a skill must be shown.
4. **Evidence changes require explanation, not automatic grade jumps.** A clearly stronger later independent task may supersede an earlier weak result; a surprisingly weak later task after earlier strength triggers inconsistency review rather than an instant collapse. The same task color can support different grades when task breadth, coverage of taught material, independence, and earlier observations differ.
5. **Grade and provenance are separate.** Existing dropdown values are saved grades with UNKNOWN teacher/algorithm origin unless metadata proves otherwise. Do not treat those values as a gold-standard teacher label or overwrite them when a new rule differs. The four teacher-specified sample histories in Section 5 remain *synthetic calibration anchors*, not actual identified students.
6. **A rule and low-end uncertainty.** No automatic pre-test A recommendation. A saved A without identified test evidence is *flagged* for teacher review, never deleted or demoted automatically. D+ is supported by the specific teacher anchor; D, D-, F require teacher-approved descriptors before automated recommendation. Blank/unreadable/unscored means no judgment, not red.
7. **Report window is not grading window.** Current-week history may be limited to Monday-Sunday. Current evolving LG grade must consider earlier *eligible* evidence across weeks, without importing all historical AP1/I Can events by assumption.

**Required before engine deployment:** (a) teacher review and approval of holistic task-color descriptions on authentic examples, (b) a one-time reviewed current-LG attribution of eligible November assessment tasks, (c) verified original 'three rules' or an explicit decision to omit them, (d) explicit grade-origin storage and teacher override precedence, (e) teacher judgment on unresolved lower grades and the independent five-bar display, and (f) regression verification of the synthetic contract cases plus a private, teacher-reviewed student comparison. Do not infer percentages/credit thresholds or silently recalculate saved grades to bypass this gate.

The privacy-safe, aggregate source comparison and future contract cases are in `PASS3_VALIDATION_FINDINGS_20261123.md` and `LG_GRADE_REGRESSION_CASES_V1.json`. These are **policy tests**, not a working Python grade estimator or certified real-student predictions.

## 9A. Pass 4 task-color calibration and source grouping (2026-11-23)

**Status: teacher decisions pending; no retroactive grade-bearing LG events created.** Pass 4 examined the approved November 13 and November 16 source-question records without embedding any individual student response or identifying information in repository files. Its source-specific calibration matrix and review prompts are in `PASS4_TASK_COLOR_CALIBRATION_20261123.md`.

1. **Zero question credit is not a red color.** A numerical 0/5 may correspond to a readable misunderstanding or a blank answer. For example, both are present among November's zero- and negative-exponent records. A blank or unscorable question part is not independently evidence of a misunderstanding. A holistic multipart task may still have some scorable work; teacher review determines whether a color is supportable for the *whole task* or the task is unscorable.
2. **Historical task grouping needs verification.** The November 13 source groups Q1a-Q1c and Q2a-Q2b under two separate original prompts; they are candidate whole tasks. November 16 QC1/QC2 and QC3-QC7 have separate stored question IDs but no verified bank family/variant metadata establishing the intended authored grouping. Do **not** merge all exponent parts into one event or count every brief part as its own independent demonstration by guesswork. Treat grouping as pending teacher/source confirmation.
3. **Source role matters.** November 13 and November 16 Quick Check prompts are plausible current-goal assessment candidates, but all corresponding current-goal `count_as_evidence` flags are false in the reviewed historical records. The multiplication worksheet and Find Someone Who are instructional context until explicitly reviewed for formal LG inclusion and independence. M15 is older linear content, not automatic LG 3.3 evidence.
4. **Color describes demonstrated mathematics on one meaningful task.** A complete, independent correct product may justify green *for that task* even when the section goal is broader. A sign slip with otherwise sound distribution and a systematic misunderstanding of distribution may deserve different judgments even if recorded question credit is similar. No automatic numeric-to-color cutoff is approved.
5. **Grade confidence follows breadth, not frequency.** Multiple narrow greens do not require or authorize an A-minus. Conversely, a later convincing broad independent task may substantially improve a recommendation without fulfilling an arbitrary repetition quota. Mixed results, changes in task difficulty, and uncertain source independence trigger teacher review.
6. **Future collection:** About four Quick Checks per week may add separate observations for current and earlier LGs. Each event uses a source-approved authored task identity. The same assessment scan may yield multiple LG-specific evidence items without becoming a grade-per-day or skill-per-day scheme.

**Release gate:** Before a Python replacement consumes these new records, obtain teacher approval for a small set of actual private student-work colors, historical task grouping and crosswalk, the original 'three rules' if found, and the unknown lower-grade language. None of the synthetic illustrations in the calibration file are an approval to relabel existing private work. Keep all saved grades, historical bars, and delivery safeguards untouched.

## 10. Source inventory (consulted for this Pass 2 standard)

- Explicit teacher decisions in the 2026-11-23 Portfolio discussion (four examples, one-color-per-complete-task, 4 Quick Checks per week after Thanksgiving, no skill quotas, A held for chapter test, retain existing interface).
- `CPM_Tools/docs/ALGEBRA1_CHAPTER_ASSESSMENT_PHILOSOPHY_20261108.md` (section goals and trend grades).
- `algebra1_learning_goals_grading_reference.html` (November 9 grade descriptions and independent five-square bars).
- `CPM_Tools/docs/PORTFOLIO_QUESTION_REVIEW_20261116.md` (0–5 question credit, teacher inclusion/approval and private evidence archive).
- `CPM_Tools/docs/PORTFOLIO_LG31_APPROVED_EVIDENCE_BARS_20261116.md` (single-run LG 3.1 bar proposals; not grade semantics).
- `CPM_Tools/docs/PORTFOLIO_AUTHORITATIVE_WEEKLY_DELIVERY_20261116.md` (current-week reporting and teacher review).
- `CPM_Tools/memories/portfolio/PORTFOLIO_WORKFLOW.json` (runtime operational, not yet reconciled).
- `CPM_Tools/app/portfolio_approved_review.py` and `CPM_Tools/app/portfolio_weekly_grid.py` (current Nov 23 working recommendation behavior).
- `CPM_Tools/banks/data/ALG1_CH03_ASSESSMENT_SCOPE_V3.json`, `ALG1_ASSEMBLY_RULES_V1.json`, and `ALG1_BANK_CONSUMER_CONTRACT_V1.json` (future goal-based bank/assessment organization; authored variants still subject to approval).

**Pass 4 calibration recorded; policy only.** Keep archived sources and Pass 3 findings intact. This file remains the sole central grading philosophy; it does not independently activate a runtime rule.
