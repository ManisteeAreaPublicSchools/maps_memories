# Algebra 1 Chapter 3 Launch / Explore Component Bank — 2026-11-22 V2

## Status and source authority

- The Chapter 3 Launch Bank is a **teacher-review draft**, not automatically approved, published, or connected to Lesson Builder.
- Nine CPM lessons (3.1.1–3.3.3); **three original, independent Launch choices per lesson**; each choice has a 15–20-minute timing budget.
- Exact lesson titles and I Can statements are copied from the approved lesson-goal mapping used by the EX/YTI V4 bank. The bank is accessed through **Banks → Launch / Explore**, with Chapter → Lesson → exact I Can → three choices.
- Primary inspiration: authentic **CPM eBooks / Core Connections Algebra 1 Chapter 3** lesson opener, Launch and Explore problem structures. Each record names the CPM lesson problem numbers that informed its design; the prompts themselves are newly authored, not verbatim CPM reproductions.
- Secondary inspiration: *CCA_PG_Ch3.pdf* (Parent Guide with Extra Practice, pp. 15–23) and *math_curriculum_craft_guide.md*, especially predict → investigate → test → generalize architectures. Parent guides are inspiration, not bank content to be copied.

## Instructional job

1. Launch is a **pre-example discovery investigation**, not direct-skill practice, a worksheet of isolated calculations, a long extension, or a repeated EX/YTI with blanks.
2. **Select one** of the three lesson choices for a lesson. Each stands alone; do not concatenate all three into a 45–60 minute block.
3. **Do not prescribe one four-step sequence for every Launch.** Select the task architecture that best fits the mathematical discovery: Notice & Discover, Build & Explore, Predict & Test, Compare & Debate, or Challenge & Create. A genuinely unique investigation may use a sixth structure. Keep the student actions and discussion authentic, not just renamed headings. All phases total 15–20 minutes; classroom timing requires teacher trial.
4. Each choice provides a short teacher facilitation guide, source problem references, mathematical conclusions, and bridge to EX/YTI. These notes remain collapsed on screen and are **hidden from student printing**.
5. Give students an investigative task with genuine choices or evidence to develop: physical algebra tiles/equation mats, area models and generic rectangles, equivalent-expression sorting, disagreement/error analysis, or classification. **Within one lesson, prefer three substantively different student experiences** rather than three numerical variants or the same process with different labels.
6. Keep student reading concise. Preserve the teacher's approved V7 style (blue left accents, MathJax, open workspace without needless lines) and local offline MathJax path `/builder/assets/vendor/tex-mml-svg.js`.
7. Student algebra correctness is mandatory: full polynomial product as the result of a model, equal legal moves for equation mats, zero and negative exponent domain restrictions, and equations whose indicated solutions check.
8. Numeric and visual source records must preserve the distinction between original CPM source cards and newly authored Launch options. Do not overwrite canonical question banks or original CPM source cards.
9. When Lesson Builder later selects a launch, use stable `ALG1-LAUNCH-<lesson>-<option>` IDs, the complete option snapshot, and student-issuance provenance, consistent with the bank-first/avoid-repeats contract.
10. The same Chapter → Lesson → I Can → three choices shell may be reused for Smarty Pants next, but Smarty Pants will require a different, deeper transfer/application task design.

## Installed paths

- `CPM_Tools/banks/algebra1/launches/index.html` (teacher screen)
- `CPM_Tools/banks/algebra1/launches/app.js` (navigation, cards, MathJax, selection and printing)
- `CPM_Tools/banks/algebra1/launches/launch.css` (V7-compatible display and one-selection print)
- `CPM_Tools/banks/algebra1/launches/chapter3.json` (27 teacher-review draft records)
- `CPM_Tools/banks/algebra1/launches/QA_CH03_LAUNCH_V1_20261122.json` (historical V1 QA ledger)
- Existing `CPM_Tools/banks/algebra1/components/*.css`, EX/YTI, Notes, Practice, Warm-Up, Assessment all remain untouched.

## Boundaries

- No automatic 12 numerical swaps: Launch choices are **different explorations**, not copies with altered coefficients.
- No automatic approval; teacher review required before use.
- No direct integration with the Lesson Builder, Portfolio, student-specific assignments, or history has been added by this transfer.
- This package uses only Curriculum Transfer / Local Only and never changes GitHub directly.


## V2: five flexible Launch structures

This structure set is a **toolbox, not a mandatory fixed rotation**. Choose the structure that creates the best pre-example discovery, based first on the actual CPM lesson opener/explore card and parent guide. A unique good investigation can preserve its original sequencing.

| Structure | Signature student action | Typical phases |
|---|---|---|
| Notice & Discover | Observe repeated mathematical evidence, then formulate a rule. | Notice a pattern → Investigate & record → State a general rule → Connect to the example |
| Build & Explore | Construct or manipulate a meaningful representation and record the full mathematics. | Build the model → Move, change & test → Record the mathematics → Connect the model |
| Predict & Test | Commit to a prediction, check it with evidence, and refine the claim. | Predict → Test with evidence → Revise & explain → Conclude |
| Compare & Debate | Defend alternatives with evidence and agree on a mathematical conclusion. | Choose a position → Investigate both claims → Debate the evidence → Agree on a conclusion |
| Challenge & Create | Design a mathematical example or model, trade it, and improve it after testing. | Accept design challenge → Create a first version → Trade, test & improve → Show final design |

- Every option remains a **single 18–20-minute investigation**, with the 15–20-minute target and no classroom-time certification.
- Each lesson contains three different structures in V2, selected for instructional fit rather than enforcing a global order.
- Some prompts use original data from V1, but the V2 options change student actions (creation, peer defense, model-building, prediction and revision), not merely headings.
- Product and generic-rectangle Launches still lead to **complete products**, not partial-product worksheets. Equation mats preserve equal moves. Exponent launches build rules from patterns. Arguments may legitimately conclude that an apparently suspicious answer is correct.
- The teacher page displays an **Approach** label so the teacher can choose the format appropriate to their class. Student printing does not include teacher solutions.
- All stable `ALG1-LAUNCH-<lesson>-<option>` IDs remain unchanged and all options remain PENDING_TEACHER_REVIEW.
- V2 QA ledger is `maps_memories/standards/ALGEBRA1_CH03_LAUNCH_QA_V2_20261122.json`. This is documentation only; runtime QA ledger V1 is intentionally not overwritten.

## V3 instructional quality pass: evidence, variety, and student reading

The existing five Launch structures remain optional choices, with three distinct approaches per Chapter 3 lesson. All 27 activities have been revised to avoid duplicated instructions, preserve a 15–20-minute investigation target, and make the mathematical evidence or student decision explicit.

1. Prefer **one clear instruction for one action**. Do not restate a Build or Predict instruction in a later phase to fill time. A second prompt should add testing, comparison, revision, or representation.
2. Each phase should produce something students can point to: a matched card set, complete rectangle product, valid equation-mat move, revised claim, or equivalent formula. Student tasks may be brief on the page and substantial in activity.
3. In Compare & Debate, provide **two genuinely competing mathematical claims** (or two viable methods with an explicit criterion). A correct result and a request to verify it are not competing positions.
4. When an activity asks students to critique an incomplete calculation, show the **actual candidate**; do not invent a "six-cell shortcut" without showing which cells were omitted.
5. Design/creation visuals must not leak a fully completed example that solves the challenge. Present constraints, blank models, or starter materials instead.
6. For algebra-tile rectangle feasibility, state the modeling restrictions before claiming a pile cannot form a rectangle (nonnegative whole unit side lengths, no gaps, all pieces used).
7. Numerical checks and specific point substitutions are evidence and error detectors, but they alone do not prove two forms equivalent for every input. Use the model or legal algebraic steps as the general justification.
8. Preserve the complete mathematical object as the intended goal: full polynomial product, complete solution set, balanced equation, or full area. Launch is pre-example investigation, not an algebra drill or scaffolded partial-products worksheet.
9. Every stable option ID, original CPM inspiration reference, exact I Can, timing total, teacher-review flag, and snapshot/provenance contract stays unchanged. Existing EX/YTI, bank CSS, app JS, question banks, CPM source cards, and previously issued student copies remain intact.

**Chapter 3 corrections in this pass:** 3.2.1C and 3.2.2C no longer show the solution of their own creation challenges; 3.2.2B limits the non-fit tile discussion to nonnegative whole-number dimensions; 3.2.3B supplies two competing complete-product claims with a correct teacher verdict; 3.2.4B shows the omitted-row six-cell answer; several lessons emphasize model-based reasoning beyond numerical spot checks.

**QA:** 27/27 options retain an 18–20 minute phase budget, 53 independent symbolic mathematical checks pass, all nine lesson selectors and all 27 student print selections work, all 27 print as one letter-size page, no browser JavaScript or MathJax errors were observed. These results are programmatic, not classroom-timing certification. QA ledger: `maps_memories/standards/ALGEBRA1_CH03_LAUNCH_QA_V3_20261122.json`.

## V4 classroom-quality pass: teacher choice, student agency, and valid evidence

This pass preserves the 27 stable Launch IDs and the three-different-structures-per-lesson contract. Ten options received targeted revisions and all 27 teacher guides received lesson-specific accessibility language. No renderer, CSS, server route, EX/YTI, canonical textbook, or other bank data changed.

- **Real design, no answer leakage.** A challenge asking students to invent equivalent expressions or rectangle factors must show constraints and blank materials, not the finished expression(s). Use the teacher guide to retain an example solution.
- **Evidence of learning.** Students should provide a complete model, full product, legal equation move, proof of uniqueness, or independently checked conclusion. A numerical counterexample can refute a universal statement; agreement at a few input values cannot establish a universal identity.
- **Proof vs. checking.** Do not describe one substituted solution as a proof that an equation has a unique solution. Solve generally or show valid equivalent steps. Number-line points for absolute value must not be premade answer markers.
- **Appropriate transfer.** Do not require inverse factoring of fourth-degree polynomials in a Chapter 3 multiplication launch when the learning goal is using a generic rectangle. Prefer an added-strip comparison, an error to analyze, or a decision about complete products.
- **Mathematically honest directions.** Say distributing is useful when it is, but do not assert that one solving method is required if another equivalent method works. Explain tile-rectangle impossibility only under the stated whole-number dimension and all-tiles-used restrictions.
- **Time and accessibility.** The 18-20 minute allocation belongs to discovery, manipulation, comparing and defending a mathematical conclusion, not additional routine practice or unnecessary prose. Every teacher guide now gives a lesson-specific starting representation and expects a complete mathematical result.
- **Bank boundaries.** Launch investigations are teacher-review drafts and pre-example activities, not automatically eligible Practice or Assessment questions. Source references are inspiration/provenance, not verbatim CPM copies. Keep stable IDs when revising; store the selected snapshot when an activity is issued.

V4 corrected exemplar cases: 3.1.1B card challenge; 3.1.2B four matching groups; 3.2.4C genuine two-rectangle design with same first factor and constant-step second factor; 3.3.1A blank number line; 3.3.2A sign-error analysis; 3.3.2C isolating x; 3.3.3B distribution when helpful rather than mandatory.

Validation: 9/9 lessons, 27/27 options, 27/27 one-page letter-size student printouts, 27/27 expanded teacher guides without MathJax errors, 21 independent math assertions and no browser JavaScript errors. This is programmatic QA and not classroom-timing or teacher-approval certification. Full audit: `maps_memories/standards/ALGEBRA1_CH03_LAUNCH_QA_V4_20261122.json`.
