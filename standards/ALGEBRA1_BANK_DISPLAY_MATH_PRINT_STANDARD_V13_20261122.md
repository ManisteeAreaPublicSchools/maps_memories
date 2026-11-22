# Algebra 1 Bank Math, Graph, and Printing Standard — V13 (2026-11-22)

**Applies to CPM Tools Algebra 1 bank consumers: Practice, Assessment, Lesson Builder, Assessment Builder, and future Portfolio/print workflows.** This is a display and rendering contract, not a teacher approval decision.

- Render all legitimate TeX through local offline MathJax using `/builder/assets/vendor/tex-mml-svg.js`. Preserve the math delimiters. Never treat currency, words, units, sentences, or text answers as one algebra expression.
- For instance, **`$9 per part; $4 fee` is prose**, whereas `\(49-5(9)=4\)` is mathematics. Keep spaces readable in collapsed and expanded answers.
- Use stacked MathJax fractions `\frac{a}{b}` and keep their negative signs visible. Use real two-row/two-column HTML tables with headings and borders for question tables.
- Display a two-equation linear system as two aligned lines with a single brace, not an unreadable paragraph. The bank renderer performs this view-only conversion for `.bk-system` paragraphs with two math expressions.
- For coordinate graphs with two lines, place **A** and **B** labels near the lines and close to the visible plane edge. Colors are allowed onscreen and in Notability; printed Assessment questions must also be distinguishable in grayscale, e.g., A solid and B dashed. Do not rely solely on a detached color legend.
- The original CPM textbook (`CH01.json` through `CH04.json`) is immutable. Teacher-review draft bank JSON may add presentation labels without changing the mathematical line geometry, equation, solution, source identity, or approval status.
- Practice is lesson-indexed and uses earlier lesson Direct Skills for spirals. Four authentic Review & Preview candidates are selected separately. Assessment is indexed by **section learning goal**. Test MC and optional Extensions are separate pools. One substantial product or system can be one task; several short micro-calculations can form one multipart family.
- All new or edited draft questions remain blocked from automated Assessment Builder or Portfolio use until teacher review.

**V13 validation:** all 45 Chapter 1–4 selector combinations passed browser smoke tests; 48 Chapter 4 graph variants have line-adjacent labels; print CSS differentiates line B with dashes; 48 source-draft solution strings received math-only formatting corrections. No canonical question or answer value was changed. See `CPM_Tools/banks/algebra1/BANK_CH1_TO_CH4_DISPLAY_SYNTAX_QA_V13_20261122.json`.
