# MAPS Planner authenticated Google Drive discovery (2026-11-24)

## Status and purpose

The Physics, Algebra 1 and AP Calculus Planners use the same read-only Google Drive metadata connector. It replaces the unreliable Google Drive Desktop folder inventory used by Update Sources, without changing existing calendar data or canonical lesson catalogs.

The Google Drive Desktop mirror may report macOS `PermissionError` for subdirectories and cannot supply Drive file IDs reliably. That method is no longer called by the Update Sources HTTP route. Existing `planner_registration.json` discovery remains as a compatible fallback for previously working lessons.

## Authorization and security

- One-time setup in each Planner: click Update Sources, import the downloaded Google Cloud **Desktop app** OAuth client JSON, click Connect Google Drive, sign in, return to the Planner, click Update Sources again.
- Google Drive API must be enabled for the Google Cloud OAuth project. District administrators may require approval of the app and restricted scopes.
- The only requested scope is `https://www.googleapis.com/auth/drive.metadata.readonly`. OAuth 2.0 desktop loopback redirect and S256 PKCE are used. No Drive modification/download scopes.
- OAuth credentials and refresh token are stored on the local Mac in `~/.config/MAPS_Planner_Drive/`, with private file permissions. Never package credentials, tokens, or teacher data into transfers or Git repositories.
- Connector uses fixed course-folder IDs under `~Curriculum/__MAPS_Courses/`: Algebra 1, AP Calculus, Physics. It only lists chapter folders `ch_NN` and lesson folders, plus their vetted `teacher`, `supports`, `stations`, and other support directories. Only PDFs enter the source review.
- A successful list response yields actual Drive file IDs. The app builds Drive view links from those IDs; it does **not** infer IDs from local filenames. This proves file existence under the authorized Google account; student access permissions are not automatically verified.
- Source scan failures (403, inaccessible folder, expired credentials, malformed data) have `ok:false` and show a red failure state. A partial scan cannot be approved and does not change catalogs.

## Approval and Planner integration

- Update Sources scans Drive and previews student lessons/labs/tasks, teacher guides and support PDFs. The teacher selects properly named student/support files and clicks **Add Selected to Planner**.
- The server approves only file IDs observed in its fresh, authenticated scan, with a one-time expiring scan token. It ignores teacher-only additions and automatically pairs a matching teacher guide in the same lesson folder.
- Approved sources are stored outside the repo in `~/.config/MAPS_Planner_Drive/approved_<course>.json`. Existing canonical catalog entries always win. New sources are additive, unique by Google Drive ID, and available offline on the Mac after approval.
- Source discovery never schedules lessons, changes the calendar, regenerates the student agenda, or invokes git. The teacher explicitly chooses a dropdown lesson and clicks **Save + Update Student Agenda**, then syncs/publishes manually.
- Support PDFs become optional-row choices. Teacher guides stay teacher-only in the Planner and are excluded from student page output.
- The single canonical shared connector is `maps_memories/shared_ui/agenda/drive_source_connector.py`. CPM Tools and Science Tools bundle byte-identical local copies as offline fallbacks. Update all three from the canonical source when revising the connector.

## Current preverified snapshot

`maps_memories/shared_ui/agenda/verified_drive_sources_20261124.json` carries four verified student/teacher pairs from connected Google Drive: Physics 5.3.M, 5.3.M2, 5.3.M3, and AP Calculus chapter 3 antiderivatives intro. Those are immediately visible in the dropdown after installation, even before OAuth setup. The snapshot is finite and timestamped; all later updates require live authenticated scans. It is never overwritten by a failed scan and is deduplicated against canonical and approved entries.

## Required QA before release

- Syntax checks for Python and JS.
- OAuth PKCE setup / refresh / expiry tests, limited to Drive metadata scope.
- Mocked folder walk verifies student/teacher/support classification and real-ID pairing.
- Failed scan cannot write approved index or report success; duplicate/replayed approval is rejected.
- Import/approve should preserve unsaved Planner calendar in browser and never run Git Sync.
- Schema-3 Local Only ZIP with exact original file SHA-256 preconditions. Verify installer applies and rollbacks in a sandbox workspace.
