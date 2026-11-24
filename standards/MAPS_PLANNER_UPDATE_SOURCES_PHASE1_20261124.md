# MAPS Update Sources pilot — review-only safety gate (2026-11-24)

Courses: Algebra 1 and AP Calculus in CPM Tools, Physics in Science Tools.

## Purpose

The existing Planner dropdowns depend on verified Drive IDs in catalogs or `planner_registration.json` files. Google Drive Desktop's mirrored filenames do not expose reliable Google Drive file IDs. A source inventory must never fabricate a student URL from a local path or a filename.

## Pilot behavior

A teacher-initiated **Update Sources** button performs a strictly read-only scan of `~Curriculum/__MAPS_Courses/<Course>/ch_NN/<folder>/` through the locally installed Google Drive Desktop mirror. It classifies student lesson/lab/task PDFs, teacher PDFs and support PDFs; it previews catalog matches, unlinked files and naming issues. The result is an in-memory report only, discarded on reload. Scans never write lesson packages, calendars, catalogs, teacher guides, or GitHub repositories.

The old Planner catalog + verified-sidecar discovery system stays authoritative until a later release proves authenticated Drive API metadata access. Files without actual verified Drive IDs are reported as **Needs verified Drive link** and are NOT added to dropdowns. Errors and unavailable Drive File Provider folders are explicitly reported and never interpreted as deleted lessons. Existing selections, 43 weeks, publication, and student resource links are unchanged.

## Next gated step (not in pilot)

After user acceptance of inventory/classification and reliable Drive API authentication, introduce explicit preview-and-approve registration with Drive file IDs fetched over authenticated metadata-only API. Preserve the old catalog as rollback and never auto-schedule or publish lessons. Teacher guides never appear in student-facing rows. Support materials will be separately selectable in optional rows after verified-link approval.

## QA acceptance

Check that all three Update Sources actions produce a course-specific preview; no status change occurs on calendar state, lesson catalog, or student agenda; existing URLs remain; offline/missing File Provider returns a readable warning; teacher materials are never published to the student agenda. No Git command is performed.
