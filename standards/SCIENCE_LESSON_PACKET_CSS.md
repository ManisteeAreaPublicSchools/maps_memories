# MAPS Science Lesson Packet CSS — reusable candidate v1.2

**Date:** November 18, 2026 · **Status:** Proposed for teacher review, not yet frozen.

## Canonical file and distribution

- `maps_memories/shared_ui/science/lesson_packet.css` is the canonical editable source for student/teacher lesson packet styling across Science courses.
- For an independently viewable or printable student/teacher HTML lesson, place an exact copy at the lesson's lesson-local `assets/lesson_packet.css` and reference it relatively. Do not require the browser to access a sibling repo, the public app server, or a CDN.
- Public independently authored simulations use a self-contained mobile-first HTML document. No purchased files/assets are copied to public repos.
- The chapter/lesson ID is preserved exactly, e.g. `5.2.2`; CSS classes are generic (`.sheet`, `.draw-box`, `.vocab`, `.table`, `.answer`) not page IDs or course-specific CSS overrides.

## Visual language from the existing 5.1.1 / 5.2.1 pilots

- Navy `#17324d` headings, warm white paper, rust `#b65429` rule/kicker, teal `#236d62` vocabulary/learning focus. Broad identity aligns with Science Tools without replacing familiar physics packet proportions.
- 8.5×11 in letter pages; first student page uses a generous warm-up with sketch, data-evaluation, or written reasoning space appropriate to the prior lesson; later content is in publisher-prescribed activity sequence.
- Paper-first (Google Drive → Send a copy to Notability), no fake Share button. Linked activities have a visible clickable button and a real absolute PDF URL.
- Student-facing vocabulary includes **definitions**, not just words. Conceptual question before calculation; no repetitive superficial explain/justify variants.
- Page sections break cleanly at the boundary. Tables have generous cells and correct units/signs. Multiple choice uses vertical options and clear circles.
- Teacher companion opens with a one-page overview: time-by-activity table totaling the lesson, materials and printing/distribution bulleted lists, prep/safety/links and fallbacks. Detailed answer pages follow in the same order as the student packet.
- PDF should remain lightweight: text and limited vector geometry (no large duplicated bitmap backgrounds). Check page dimensions, links, clipping, Notability performance and actual iPad launch.

## Source-specific lesson composition

- Do not force one order on all lessons. Lesson 5.2.2 was subsequently rebuilt to use live exploding carts, a short prior-lesson CER, and Vernier before/after velocity measurements. The older simulation-led packet is superseded; retain the sim as backup/reference, not the main activity.
- The publisher's `Mom5_RedCartVsBlueCart.pdf` guided scope but is not copied/reprinted. Student prompts are original.
- 54-minute *current live-lab* model: **5 min warm-up + 7 min CER + 9 min capture + 18 min Vernier velocity readings + 11 min momentum comparison + 4 min exit = 54 min**. Teacher should adjust after the classroom trial.

## Review before approval

Check page-by-page writing space, visual density, formula legibility and printed hyperlinks on student iPads. Once reviewed, write version 1 approved to this record and keep future packet builds tied to the same canonical style, rather than diverging page-specific patches.

## Mandatory previous-lesson check

Before any new packet, follow `maps_memories/standards/SCIENCE_LESSON_PREBUILD_REVIEW.md`. Open and inspect the actual preceding lesson(s) to design a nonduplicative warm-up and coherent progression. For 5.2.2, the warm-up now tests a claim using a prior sample data trial rather than repeating 5.2.1's push-apart sketch.

## Live experiment / video analysis pattern (v1.2)

Use distinct `.cer-grid`, `.cer-block`, `.experiment-focus`, `.compact-table`, `.check-row`, `.lab-alert` and `.answer-lines` components for actual measured-data lessons. Teacher overview comes first; student activities follow the lesson, not a rigid universal sequence. Prefer conceptual warm-up > short evidence summary from the prior lesson > live experiment > new measurement/data reduction > conclusion. Explicitly separate simulated example values from authentic classroom measurements; never prefill real lab data. Keep calculator and equation demand limited to the learning objective.

## Distribution / teacher-key philosophy (November 18, 2026)

Place lesson-local stylesheets inside the canonical `__MAPS_Courses/<Course>/ch_NN/lesson_id/assets/` directory. Student and teacher PDFs/HTML can live together in that one lesson directory. Teacher-authored guides and solutions may be shared with students; do not build workflows dependent on hiding solutions. Preserve licensing restrictions on purchased publisher assets and maintain strict privacy for student records, grades, interventions, and credentials.
