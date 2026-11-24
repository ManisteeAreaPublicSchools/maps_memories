# Portfolio LG grading - Pass 5 real-evidence calibration

**Date:** November 23, 2026  
**Status:** READY FOR TEACHER COLOR/ATTRIBUTION DECISIONS; **NOT APPROVED FOR AUTOMATIC GRADE ENGINE**  
**Authority:** the central `ALGEBRA1_PORTFOLIO_GRADING_PHILOSOPHY_V1_20261123.md` v1.3; this file documents source findings and teacher sign-offs, **not a second policy**.  
**Privacy:** This document deliberately excludes student IDs, names, personal responses, scans, scan-page references, saved grades, and uniquely linkable student sequences. All original evidence remains in private Portfolio data.

## 1. What this pass actually did

- Re-opened both private approved-review JSON files and checked the source question text, graded responses, uncertainty flags, student-work transcript classifications, and the source's evidence inclusion flags.
- **Rendered and visually inspected the original November week Quick Check pages** from the private evidence PDF, rather than assuming its structure from the JSON question IDs. These scans are **not included in this transfer**.
- Compared task groups and real response categories across November 13 and the week-of-November-16 packet; used aggregate counts only for export.
- Rechecked the teacher's four synthetic grade anchors and the Pass 3/4 policy fixtures; added explicit structure/date/blank/mixed-work guard cases. This is a **contract check**, not a working Python grade-engine test.
- Made **no current-LG red/yellow/green event**, no automatic letter recommendation for an actual student, and no change to any saved grade.

## 2. Important source-specific findings

| Source | Verified actual observation | Why it changes the grading design |
|---|---|---|
| Original two-page Quick Check, filed under week of Nov 16 | Printed footer is **November 20, 2026**; review JSON's `source.date` is **November 16, 2026**. | Week label and printed date are different metadata; **actual administered date has not been established**. A new record must not silently use the wrong date for trends. |
| Front of that original Quick Check | Question **1** and Question **2** each ask for a full binomial product using a generic rectangle. | Candidate two distinct complete LG 3.2 tasks; do not merge by scan page or automatically grade the whole LG from them. |
| Back of that original Quick Check | **Five short exponent questions (3-7) under one `Exponent Properties` section**. | Candidate **one holistic LG 3.1 task**, rather than five unrelated evidence votes. The teacher must confirm the intended grouping. |
| Nov 13 approved review | 69 student sets, with Q1a-c and Q2a-b identified separately in prompt text. | Candidate two complete LG 3.1 prompts per student; actual authored-paper grouping should be confirmed before historical promotion. |
| Both approved reviews | Their current exponent/rectangle question rows have `count_as_evidence=false`. | The scores were reviewed, but **no current section LG evidence inclusion has been certified**. Retroactive mapping requires teacher approval. |
| Practice and Find Someone Who in the week-of-Nov-16 combined run | Different PDF sources and independence conditions from the formal Quick Check. | Keep as instructional context, not automatic current-LG grades. |

**Observation vs inference:** The printed Nov 20 footer is verified from the original PDF. It does **not** establish when students completed the paper. The grouping is a strong, visually grounded *candidate*; it is not verified bank `family_id` metadata or teacher-approved evidence attribution.

## 3. Actual-response audit, aggregates only

These are **descriptive archived question-credit checks**, not thresholds for R/Y/G and not percentages to average into grades.

| Source question grouping | Number of student sets | All parts >=4.5/5 with no review flags (raw-score descriptor only) |
|---|---:|---:|
| Nov 13 exponent Q1 (a-c), candidate whole task | 69 | 42 |
| Nov 13 zero/negative exponent Q2 (a-b), candidate whole task | 69 | 28 |
| Week-of-Nov-16 front Q1 + Q2 rectangle questions, combined descriptive group | 65 | 39 |
| Week-of-Nov-16 back Q3-Q7 exponent questions, candidate one complete task | 65 | 9 |

The 39 front entries represent students with high unflagged credit on **both separate products**, not automatic high proficiency on the entire LG 3.2. The 9 back entries represent high scores across all five parts; neither figure decides a final task color without inspecting the complete reasoning.

| Whole-worksheet issue | Zero-credit entries | Explicitly blank | Readable attempts receiving 0/5 |
|---|---:|---:|---:|
| Week-of-Nov-16 back Q6, zero exponent | 29 | 3 | 26 |
| Week-of-Nov-16 back Q7, negative exponent | 21 | 7 | 14 |

**The distinction is decisive:** an automatically mapped 0/5 would wrongly describe at least 10 explicitly blank *parts* as demonstrated misunderstanding. A part being blank does **not** automatically make a whole multipart task unscorable either; the remaining parts must be reviewed holistically.

Of 46 overlapping student sets with full comparable archived exponent-question credit in both runs, 9 increased by at least one mean-credit point, 14 decreased by at least one, and 23 were within one. This is **raw score movement**, not a certified LG grade trajectory, and the later packet's actual administration date must still be confirmed.

## 4. Real-source response patterns -> candidate task-color calibration

The source response patterns below are **generalized from actual reviewed student work**. The wording describes the *kind of mathematical reasoning* seen; it does **not** reproduce anyone's exact answer, name, sequence, or unique scan/page. These are candidate policies the teacher can approve or revise; no individual student's color is assigned.

| Case | Observed type of work | Suggested complete-task judgment | Why / confidence |
|---|---|---|---|
| P5-R01 | Exponent properties are applied coherently throughout the authored multipart task. | **Green** | Convincing *task-level* evidence; does not certify the full LG without sufficient breadth. |
| P5-R02 | Several exponent transformations are correct; a later part clearly confuses exponent operations or negative-power meaning. | **Yellow** (review) | Significant partial understanding across the task; not a rule that 'one wrong part = yellow'. |
| P5-R03 | Multiple attempted parts demonstrate the same fundamental exponent misconception without a workable method. | **Red** (review) | There is readable evidence of current misunderstanding, independent of numeric credit. |
| P5-R04 | Some completed parts are correct and another is blank. | **Yellow OR no judgment** (decision C) | If the completed portion is substantial, yellow is plausible; if too narrow to assess the authored task, null is safer. Not red because of a blank. |
| P5-R05 | Both separate generic rectangles are correct and independently explained through partial products and final expression. | **Green per complete rectangle task** | Evidence limited to binomial multiplication; don't promote directly to LG-wide A-. |
| P5-R06 | Rectangle structure and distribution are correct, but the final total contains an isolated arithmetic/sign slip. | **Green OR yellow** (decision D) | The decisive factor is whether understanding remains convincing; no score cutoff. |
| P5-R07 | Rectangle model omits an entire product or repeatedly mishandles distribution. | **Red OR yellow** (decision D) | Distinguish lack of method from a partial, repairable method. |
| P5-R08 | Every part of the assessed complete task is genuinely blank or unreadable. | **No judgment (null)** | Keep missing/unscorable state separately; cannot infer red or F. |
| P5-R09 | One later Quick Check appears weaker than earlier convincing independent work on the same goal. | **Flag contradiction; do not auto-drop grade** | Check scope, timing, errors, and independence before interpreting trend. |
| P5-R10 | Correct collaborative multiplication work, with no verified independent demonstration. | **Practice context only** | Useful instructionally, not a qualifying LG color by default. |
| P5-R11 | Five short exponent prompts sit on one authored Quick Check side. | **ONE candidate holistic LG 3.1 color** | A page is not five automatically independent attempts; confirm teacher grouping. |

### Proposed teacher-friendly default answers

For the **next** formal, teacher-approved task, my provisional defaults are: coherent complete understanding = Green; meaningful but uneven understanding = Yellow; readable broad misunderstanding = Red; wholly absent/unusable work = null. For a largely successful rectangle with one minor arithmetic slip, **Yellow is a conservative provisional suggestion**, though Green may better reflect a convincing method. For one correct part and one blank, use **Yellow only when enough mathematical thinking is visible to judge**; otherwise null. These are *not* approved numerical score bands.

## 5. Letter-grade calibration and comparison to the existing records

1. **Four teacher-anchored synthetic histories remain unchanged:** Red -> Yellow -> Green = **C+**; Green -> Green -> Green = **A-**; Yellow -> Green -> Green = **B+**; Red -> no evidence -> Yellow = **D+**. They describe qualitative judgment given comparable eligible independent tasks and sufficient taught coverage; no simplistic three-color lookup.
2. **No current-student grade comparison can be certified** from historical scoring alone: source question-credit approval is not the same as current-LG evidence approval; saved dropdown grades lack definitive teacher-vs-algorithm provenance. Showing purportedly precise replacement grade differences would repeat the old mistake.
3. **Existing A- on two narrow rectangles is a review prompt, not an automatic downgrade.** Future results may demonstrate the full taught goal. Preserve saved data.
4. **A before chapter-test evidence remains outside automatically generated recommendations.** Teacher-approved prior saved A remains unchanged until teacher action.
5. **Mixed newer evidence requires a traceable explanation and review,** not automatic weighted averages or per-skill repetition quotas.
6. **Two potential notions of 'newer':** source packet is filed under Nov 16 but printed Nov 20. Before any time-aware engine uses dates, correct event-date provenance in the source mapping; otherwise a trend might be computed in the wrong order.

## 6. Exactly six teacher decisions before implementation

| Key | Specific decision | Proposed default; pending explicit teacher sign-off |
|---|---|---|
| **A** | Should the Nov 20 printed formal Quick Check be represented as **two LG 3.2 rectangle items on the front + one LG 3.1 exponent item covering Q3-Q7 on the back**? | **Yes**. These are complete task opportunities, not five skill repetitions. |
| **B** | Should the Nov 13 Q1a-c and Q2a-b each be considered one authored current LG 3.1 task, subject to source verification? | **Yes, conditionally**; verify the original paper structure first. |
| **C** | How should one correct part and one blank part be judged? | **Yellow if meaningful partial understanding is visible; otherwise no judgment.** No automatic red for blanks. |
| **D** | How should a lone arithmetic/sign slip be judged when the overall model is convincing? | **Yellow by default with review**, or Green when independent reasoning is still convincing; persistent core misconception -> Red or Yellow by extent. |
| **E** | May approved historical Quick Check parts be mapped retrospectively into current section-LG colored events? Does teacher verify the independence of the work and original task grouping? | **Allow only after one-time explicit teacher-approved source-to-LG crosswalk.** Do not change old flags silently. |
| **F** | How do the missing original 'three rules', D/D-/F descriptors, and legacy saved-grade provenance affect deployment? | **Keep these unapproved; no automatic D/D-/F or rewriting legacy grades.** Identify original rules verbatim or explicitly omit them before engine launch. |

**Decision recording:** Teacher may respond with `A yes, B yes, C ..., D ..., E ..., F ...` or ask to review only disputed cases C/D. A response is not stored automatically in the running Portfolio; later policy update can record the teacher's signed-off interpretation. The six decisions are **not yet approvals**.

## 7. Release decision

**Pass 5 calibration audit complete. Engine deployment is still BLOCKED.** This pass provides original-paper confirmation, real-response category counts, teacher-friendly proposed colors, and precise review questions. It does not manufacture teacher labels or pretend the stored source is a calibrated R/Y/G reference set.

Once the teacher confirms the six decisions (or explicitly defers only nonessential questions), the next coordinated implementation should: (1) create the private per-LG JSON event record; (2) require approved source-to-LG mapping and preserve original evidence; (3) show non-destructive, explainable grade suggestions from qualitative history; (4) record teacher override provenance; (5) regression-test synthetic anchors and safety cases; (6) keep the existing Portfolio interface and manual send/export steps. Do not patch old numeric-grade thresholds.

**No private student data or source PDFs included. No application changes, grades, approved records, report exports, or messaging changed.**
