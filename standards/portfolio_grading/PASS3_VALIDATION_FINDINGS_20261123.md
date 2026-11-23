# Portfolio Learning Goal grading - Pass 3 evidence-validation findings

**Date:** 2026-11-23  
**Status:** REAL-DATA AUDIT COMPLETE; AUTOMATIC-GRADE VALIDATION BLOCKED BY MISSING LG-LEVEL APPROVAL  
**Audience:** Teacher and future authorized local implementation only. No student-specific data here.  
**Authority:** `ALGEBRA1_PORTFOLIO_GRADING_PHILOSOPHY_V1_20261123.md` (Pass 3 audited v1.1). This audit is explanatory, not a second grading policy.

## Scope and provenance

Read the current mirrored private student-state snapshot (revision 13), private weekly draft (revision 22), and two teacher-approved question-review JSONs: November 13 Quick Check 3.1 and November 16 combined evidence run (quickcheck, multiplication practice, Find Someone Who). Approved means reviewed question records exist; it does not mean current section-goal grade inclusion has been authorized. No original scans, student names, IDs, responses, grade rows or export templates are included in this transfer.

The stored review data describe **question credit (0-5)**, `count_as_evidence`, `needs_review` and original source/question descriptions. They do **not** contain teacher-reviewed holistic red/yellow/green **current section LG** judgments. Therefore no definitive red/yellow/green grading histories or revised letter grades are produced in this pass.

## Verified aggregate results

| Measure | Observed count | Interpretation |
|---|---:|---|
| Active saved grid rows | 78 | Current private weekly draft; not necessarily 78 assessment participants. |
| Saved LG 3.1 letter grades | 78 | Saved grade origin (teacher vs accepted algorithm) is not reliably recorded. |
| Saved LG 3.2 letter grades | 62 | Another 16 have no saved grade. |
| Saved LG 3.3 grades | 0 | No usable LG 3.3 grade in this draft. |
| Nov 13 approved question records | 552 across 69 students | 8 question records per student; exponent parts Q1a-c/Q2a-b and separate linear tasks Q3/Q4a/Q4b. |
| Nov 16 approved question records | 1,978 across 76 students | Three different source PDFs combined under one run; 65 students in the 7-question Quick Check component. |
| Nov 13 `count_as_evidence = true` | 196 | **Only Q3/Q4** old linear relationship I Can evidence; **zero** current exponent Q1/Q2 parts counted. |
| Nov 16 `count_as_evidence = true` | 47 | **Only M15**, an older line-equation task; **zero** QC1-QC7 questions counted. |
| Nov 16 QC rectangles (LG 3.2 candidate) | 65 students, both scored | Only 57 have neither QC1 nor QC2 flagged `needs_review`; the other 8 require review. |
| Nov 16 QC exponent cluster (LG 3.1 candidate) | 51 students fully scored | All 51 have no `needs_review` flag on QC3-QC7; missing/unscored work is not red. |
| Fully scored Nov 13 AND Nov 16 exponent questions | 46 students | Raw score comparison only, not two certified LG-color observations. |
| Of those 46, later mean raw credit >= 1 lower | 14 | Contradiction/possible content difficulty; not an automatic downgrade. |
| Of those 46, later mean raw credit >= 1 higher | 9 | Growth evidence to investigate; not an automatic upgrade. |
| Of those 46, absolute mean credit change < 1 | 23 | Similar raw performance; does not guarantee same depth. |
| Saved LG 3.2 A-minus | 39 | All 39 had high credit across just two short rectangles (36 had 5/5 on both). Breadth is insufficient to *certify* full LG A-minus from these alone. |
| Saved LG 3.1 plain A | 4 | No Chapter 3 test appears in the two examined approved runs; preserve saved values but flag for optional teacher review under newest A rule. |

**Important mapping finding:** The 196 and 47 counted records are old I Can codes, *not* evidence approvals for `ALG1-S3.1`, `ALG1-S3.2`, or `ALG1-S3.3`. An all-approved review ZIP is not a blanket authorization to convert every scored question into a Learning Goal grade. Do not automatically map the scored exponent/rectangle questions just because their content plausibly fits the new LG.

## What the examples establish and what they do not

- **Score quality is not goal coverage.** Near-perfect scores on QC1/QC2 can show strong introductory rectangle multiplication but cannot by themselves prove explanation and full polynomial multiplication expected by the overall LG 3.2 statement. Newer taught scope and Checkpoint/Test tasks matter.
- **Later work can disagree.** Among 29 saved LG 3.2 A-minus students with a Find Someone Who trinomial-by-binomial response, 8 had recorded credit <=2/5 for that task. Find Someone Who participation is not verified independent/formal grade evidence, so this is a *scope / practice-target signal*, **not** an authorized grade downgrade.
- **Nov 13 + Nov 16 evidence matters.** Raw exponent scores changed in both directions, making a one-assessment algorithm unreliable. Numerical scores and date order provide context, but neither source has approved current-LG color judgments yet.
- **Saved grades are not a teacher-calibration gold standard.** The system has previously written/accepted working grades and there is no verified origin metadata on the saved grade cells. Never measure rule accuracy by exact agreement with those saved values; obtain teacher-verified examples for certification.

## Candidate decision checks from authentic source patterns (not assigned to any student)

1. **Perfect introductory rectangle work, no broader independent product:** preserve saved grade; a new high LG 3.2 grade is REVIEW / NARROW-COVERAGE until a more representative assessment is available. No forced demotion.
2. **Strong exponent work Nov 13, weak Nov 16:** CONTRADICTORY; request teacher review of the later question differences, independence and source, instead of mechanically lowering grade.
3. **Earlier struggle followed by compelling independent later demonstration:** flag GROWTH and allow a positive trend without requiring an additional fixed number of successful performances.
4. **Missing or unreadable November questions:** NO JUDGMENT for those tasks. Preserve earlier relevant evidence. Do not infer red, missed opportunity, zero, or F.
5. **Collaborative Find Someone Who completion:** contextual practice/feedback only unless specifically reviewed for independent LG evidence.
6. **Approved older line-equation I Can records:** do not label as LG 3.2 multiplication or LG 3.3 equations solely from code name; verify task content + current goal scope + teacher approval.
7. **A already saved without verified chapter test:** preserve recorded value; flag provenance/possible new-policy difference, not retroactive correction.

## Pass 3 policy calibration fixtures

`LG_GRADE_REGRESSION_CASES_V1.json` contains the four teacher-specified **synthetic** grade patterns (C+, A-, B+, D+) and no-judgment / eligibility / teacher-override / pre-test-A safeguards. These are future engine acceptance cases only. They do not grant the algorithm permission to infer colors directly from raw half-bar credit or to assume all Green judgments cover an entire LG.

## Release gate and next action

**Not ready to replace the Python grade estimator.** This is an evidence-linkage blocker, not a reason to patch more score thresholds.

1. Teacher reviews a small number of authentic full tasks spanning exponent, rectangle, stronger polynomial products and missing/ambiguous work; approves the **single holistic red/yellow/green judgement per complete task** and current section-goal mapping for retrospective evidence where appropriate.
2. Locate and quote the original teacher 'three rules' verbatim, or explicitly leave them out. Do not invent their content.
3. Approve lower-end language (D/D-/F), grade-provenance tracking, and any separate bar-display rubric. All existing grades remain unchanged until explicit teacher action.
4. After teacher approval, build the entire LG evidence-to-recommendation engine as **one coordinated replacement** of the old grading rules, with strict immutable-source and teacher-override tests. Do not alter the Assessment Builder until its own migration workstream.

**No Portfolio code, grade, evidence or emails were changed by Pass 3.**
