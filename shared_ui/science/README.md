# MAPS Science Tools — shared course theme

`science-ui.css` is the authoritative stylesheet for all eight Science Tools
course workspaces and their shared ten-tool grid. Deep teal is the supporting
contrast color; spiced mustard `#D39832` is the dominant accent and header.

The local Science Tools server serves this repository file directly per request,
so editing it once updates all Science course views on refresh. The app ships an
identical bundled fallback for offline use without the district repository.

The common toolbox and navigation code lives in `SCIENCE_Tools/app/app.js` and
is rendered for every course from `SCIENCE_Tools/config/courses.json`; no
course-specific HTML/CSS copies are permitted.

Do not store student data, credentials, IEP/504 information, private teacher
evidence, or runtime logs in this public GitHub repository.
