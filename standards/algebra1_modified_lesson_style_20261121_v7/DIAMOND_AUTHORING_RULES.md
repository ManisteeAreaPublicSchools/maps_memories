# Diamond problem construction and verification

**Canonical reference:** `memories/Tools/graph_tool.py`, function `make_diamond(top, left, right, bottom, filename=...)`, resolved through `Tools/MANIFEST.json`. The current graph tool capability inventory confirms it supports blanks in any of four cells.

- **Top = product** of side numbers. **Bottom = sum** of side numbers. Left/right are the unknown pair in a standard warm-up diamond.
- For classic blanks: pass strings `top='-48', left='', right='', bottom='2'` to the graph tool. The correct two values are `8` and `-6` in either order, because 8(-6)=-48 and 8+(-6)=2.
- For other variants, do **not** force both sides blank when another meaningful unknown is appropriate. The tool accepts blanks in any position. A problem must remain solvable and answer-unique up to interchanging left and right when order is unimportant.
- Validate the mathematical data before image generation; check the renderer arguments match the actual givens and blanks; preserve the original PNG as a student-facing image without answer leakage.
- Ensure relative paths are registered in the actual lesson/Builder resource resolver and work offline. Never re-create a rough diamond with custom SVG, a Unicode glyph or CSS borders.
- Solution popup should check both `a*b=top` and `a+b=bottom` and show the pair, with any zero/sign cases correctly handled.
- Compare each produced PNG with a trusted current-bank asset for the canonical graphical structure (diagonal internal dividing lines and conventional top/bottom placement).

## November 21 verification

A read-only audit of `fluency_instances.json` found **306/306** diamonds with correct sum/product answers, consistent blanks and canonical Graph Tool metadata. Each item uses a unique PNG basename. The Drive assets folder contains **306 actual PNG image files**, including the visually checked sample `diamond_m48_p2.png`. The bank's own QA summary also reports 306 real Graph Tool PNGs generated. This audit **did not** inspect all 306 PNGs visually or run the current canonical generator source because that exact source was unavailable through the connector; further end-to-end PNG checks should run when authoring the Builder integration.
