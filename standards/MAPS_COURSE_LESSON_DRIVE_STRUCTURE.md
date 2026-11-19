# MAPS Course Lesson Drive Structure — authoritative three-course rule

**Approved:** November 18, 2026. **Installer destination corrected:** November 19, 2026. **Applies to:** Physics, Algebra 1, AP Calculus and all future lesson transfers. **Shorthand:** `memories` means the `maps_memories` project repository when discussing curriculum rules.

## One clean course tree

Canonical Google Drive root: `My Drive/~Curriculum/__MAPS_Courses/`.

```text
__MAPS_Courses/
  Physics/
    00_START_HERE_Physics_Lessons.html    # optional lesson index
    ch_01/
      lesson_1_1_1/
        student.pdf
        student.html                    # optional browser/print companion
        assets/lesson_packet.css        # self-contained rendering
        teacher/teacher.pdf             # may be student-visible
    ch_05/
      lesson_5_2_1/
      lesson_5_2_2/
        student.pdf
        student.html
        assets/lesson_packet.css
        teacher/teacher.pdf
        teacher/teacher.html
    ch_12/
  Algebra 1/
    ch_01/
      lesson_1_1_1/
        student.pdf
        teacher/teacher.pdf
  AP Calculus/
    ch_01/
      lesson_1_1_1/
        student.pdf
        teacher/teacher.pdf
```

- `ch_NN` uses two-digit chapter/unit numbering, e.g. `ch_03`, `ch_12`; inside it, `lesson_X_Y_Z` preserves the exact instructional number (do not renumber publisher units). Different teacher-approved items may be in a named chapter folder when not a standard lesson.
- **No** `lessons_google_drive` wrapper, `ch05_lessons` wrapper, parallel course tree, or loose unorganized student PDFs at course root. Course index `00_START_HERE_*.html` is permitted at the root and must link to this exact hierarchy.
- The existing Physics course tree is the canonical example. The teacher may manually move or discard old lesson copies; future packages only target the new tree. Do **not** silently migrate, delete, or preserve obsolete copies.
- Leave the public GitHub repo as the home for independently authored interactive simulations; students launch them from a link in the Drive PDF when published. The lesson document itself belongs in Google Drive, not GitHub Pages.

## Teacher-guide philosophy

**A teacher-authored answer key is a learning resource, not a security mechanism.** Teacher guides, worked solutions, and preparation notes may be visible to students. If a student studies and understands them, that is learning; design new evidence-based assessment tasks rather than relying on secrecy. The teacher controls sharing of lesson materials.

**Separate real protections:** never put student names linked to grades, IEP/504 details, accommodations, guardian information, scanner outputs, credentials, or other personal records in class-visible course trees. Purchased publisher Think Sheets, paid question banks, and publisher-provided answer keys retain license/access restrictions; the above philosophy does not grant permission to republish licensed third-party source files.

## Transfer and route contract

`~/GitHub/memories/Tools/curriculum_transfer/apply_curriculum_transfers.py` is the executing transfer script. The authoritative approved-roots seed is `~/GitHub/memories/Tools/curriculum_transfer/approved_roots.json`; the launcher's startup routine copies that seed to `~/GitHub/_curriculum_transfers/approved_roots.json`. These must agree with the script's fixed **Local Only** Drive whitelist:

| Existing transfer root alias | Google Drive target under My Drive |
| --- | --- |
| `physics_lessons_drive` | `~Curriculum/__MAPS_Courses/Physics` |
| `algebra1_lessons_drive` | `~Curriculum/__MAPS_Courses/Algebra 1` |
| `apcalc_lessons_drive` | `~Curriculum/__MAPS_Courses/AP Calculus` |

This is a **routing update**, not a migration. Do not embed the old `lessons_google_drive` or `chXX_lessons` path inside a manifest's relative `path`. Example new transfer file: `root=physics_lessons_drive, path=ch_05/lesson_5_2_2/student.pdf`. The installer rejects old wrapper paths instead of silently creating duplicate folders.

### Safe sequencing

The corrected transfer updates the executing script and the authoritative registry seed (both in `memories/Tools/curriculum_transfer/`). The launcher uses the old code/config to apply the update, and on the **next launch** refreshes the generated `_curriculum_transfers/approved_roots.json` from the updated seed. The package deliberately does not replace that generated runtime copy by hash. No student lesson files are changed by this bootstrap. Subsequent lesson transfers use the new routes. Do not combine first-time routing changes and Drive student-file operations in the same initial bootstrap transfer. Existing lesson files that the teacher manually moved into this folder are unaffected.

## Pre-build and QA policy

1. Look at the prior one or two complete actual lessons before writing, not just the pacing catalog. Identify the genuinely new reasoning or evidence type, avoiding adjacent duplicate simulation/lab experiences.
2. Use selected publisher lesson descriptions, purchased sources privately, existing materials and teacher-approved pacing. Teacher overview page first (timing total, materials, print/distribute, safety/tech). Student materials after warm-up follow the real experience.
3. Reuse `maps_memories/shared_ui/science/lesson_packet.css` as candidate source; copy into each standalone lesson's `assets/` folder. Render and inspect PDF pages; keep them light for Notability.
4. Audit paths and links against `__MAPS_Courses/<Course>/ch_NN/lesson_id/` and ensure PDF can be opened by intended class users. Do not equate owner access with student access. Check relative CSS references, PDF links and public simulation URLs.
5. Deliver exactly one verified Curriculum Transfer — Local Only ZIP. No automatic Git writes, commits, pushes or sync.

## Known initial state, November 18, 2026

- `__MAPS_Courses/Physics` already contains `ch_01`...`ch_12` and `ch_05/lesson_5_2_2/`. It holds the rebuilt live Vernier/cart lesson. Google Drive ownership metadata for this course folder showed owner-only access; adjust sharing to class-readable before assigning student URLs.
- New `__MAPS_Courses/Algebra 1` and `__MAPS_Courses/AP Calculus` course folders were created and verified as siblings; no older lessons were moved automatically.
- `00_START_HERE_Physics_Lessons.html` is a legacy index with some `ch_05/ch05_lessons/...` links. These links must be rebuilt to point to the direct `ch_05/lesson_...` tree before relying on that index. Avoid treating its existing stale links as current routing policy.
- Former sources under `~Curriculum/__Physics/lessons_google_drive` and the legacy Algebra/AP Calc `lessons_google_drive` directories are optional migration inputs, **not** active write destinations.
