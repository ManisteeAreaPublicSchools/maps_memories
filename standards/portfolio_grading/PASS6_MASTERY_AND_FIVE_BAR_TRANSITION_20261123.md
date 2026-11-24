# Portfolio | Weekly mastery calibration and five-square transition (Pass 6)

**Date:** 2026-11-23  
**Status:** Working teacher-confirmed calibration anchors and *proposed* transitional bar policy; **NO STUDENT OR SOFTWARE CHANGES**.  
**Authoritative philosophy:** `ALGEBRA1_PORTFOLIO_GRADING_PHILOSOPHY_V1_20261123.md` v1.4.  
**Scenario data:** `LG_WEEKLY_CALIBRATION_CASES_V1.json` (80 synthetic, identity-free examples; no student work).

## Teacher-confirmed calibration corrections

Two different Week 10 evidence histories were graded B+ in the previous preview. The teacher explicitly corrected both to **A-**:

- **Mostly proficient:** `G..Y..G..G` (green Weeks 1, 7 and 10; yellow Week 4) => **A-**. One earlier yellow does not cancel strong, spaced, and most-recent proficiency.
- **Recovered after setback:** `.G..G...RG` (green Weeks 2 and 5, red Week 9, green Week 10) => **A-**. Recovery on the latest independent check can restore a strong provisional grade. Do not demand one more successful check as a mechanical condition.

The previously approved late-setback comparison also remains:

- `G...G...G...G..R` at Week 16: **B** (one late red, previous greens retained; investigate the reason).
- `G...G...G...G..Y` at Week 16: **B+** (latest partial demonstration with strong earlier history).
- `G...G...G...G..G` at Week 16: **A-** (latest work again convincing).

The teacher accepted the displayed working examples except the two updated B+ -> A- cases, while prior anchor examples remain in `LG_GRADE_REGRESSION_CASES_V1.json`. No numeric score cutoff, green quota, or weighted-average rule is thereby approved. The particular circumstances of task depth and independence still matter.

## Mastery definition (central guiding statement)

**Mastery is demonstrated when a student consistently shows independent proficiency with a Learning Goal over an extended period, across multiple appropriately spaced assessment opportunities. A single successful assessment, chapter test, or short period of concentrated preparation does not establish durable mastery. Previously demonstrated goals remain eligible for reassessment through the semester.**

**A- versus A:** A- represents convincingly strong *current* proficiency and can be earned before durable retention has been confirmed; it is not reserved until the end of the semester. A is reserved for the end-of-semester judgment, supported by sustained independent proficiency across time **and** appropriate test confirmation. A test alone cannot instantly promote a student from developing to durable mastery. Later personalized test questions on prior goals are legitimate retention evidence, not a one-shot shortcut.

## Weekly evidence record and display (future, not installed)

1. About four regular Quick Checks/week, Tuesday through Friday. Each has a current LG and a previously taught LG. All students may receive a common rotation; advanced personalization is a separate future tool.
2. **One overall LG judgment per Quick Check per student**: all relevant multi-part questions for that LG (including two rectangles together, or five exponent prompts together) inform **one** red/yellow/green judgment, or no judgment. Do not produce one color per subpart.
3. When an LG is assessed twice within a week, retain original independent observations behind the scene and, if the weekly history is eventually published, show **one** reviewed weekly color for that LG. Never silently select the best/worst observation or average them into a color.
4. The possible future weekly row has **one bubble for every elapsed instructional week**. A filled red/yellow/green bubble is the week's holistic evidence. An outlined empty bubble means no assessment of that goal that week. All LGs show the same number of elapsed-week slots; the rightmost bubble is the latest week. Older filled colors are immutable historical evidence, including green.
5. Old source questions may be reused in new checks only when bank eligibility and teacher review permit. Historical November QCs may be considered for retroactive conversion **after** source/independence and goal mapping approval; the older numerical question scores alone are not approval.

## Five-square report: recommended transition through this semester

**Keep the existing five-square bar visible on all current student reports. Do not replace it with 18-20 weekly bubbles in the middle of the reporting cycle.** Preserve every saved five-square value, existing saved grade, printed report design, email behavior and manual teacher-edit controls. The ZIP in this pass changes policy files only, not running Portfolio logic.

Recommended low-risk sequence:

1. **Now through semester close:** Continue the approved legacy five-square display, including its current operational cap and manual-edit behavior. Do not reinterpret 1-5 squares as a green-count, number of weeks, color percent, or the provisional letter grade. The teacher may use approved evidence and existing controls to make deliberate growth updates; avoid auto-increasing squares from one check or backfilling bars from old question credit.
2. **Prepare a private shadow timeline:** design (but do not activate without a separate implementation approval) a per-LG append-only record of assessment-date, week, source, teacher-reviewed color, eligible/independent status, full question references, and grade recommendation provenance. Preserve existing five-square values separately. This generates data for future circle reports without changing today's student view.
3. **Compare privately:** inspect whether the five-square display, weekly evidence, and letter grade tell coherent stories. The three measures may diverge and must not be forced into a one-to-one conversion. Track examples of genuine growth, sustained proficiency, setbacks, and limited opportunities for recently introduced goals.
4. **Post-semester / January decision:** choose whether weekly circles replace bars or become a collapsible history beneath them, after teacher preview and QA. No automatic publication, regrading, PowerSchool export or emailing. Do not reset/erase established five-square history during transition.

**Discussion still open:** Should a filled five-square milestone be nondecreasing? Should students later see bars + bubbles or bubbles alone? There is no approved new five-square formula; leave the operational legacy intact pending that decision.

## Release gate

Policy/fixtures only. No active grade algorithm, no retrofit of individual historical students, no auto-color conversion, no retrospective bar values, and no change to student reports. The lower D/D-/F boundaries, original verbatim 'three rules', historical source authorization, and actual task-color teacher calibration remain separate required release gates. An A- scenario is not a certification of individual student mastery.
