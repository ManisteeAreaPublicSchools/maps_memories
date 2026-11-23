"""Read-only, verified Drive-lesson registration discovery for MAPS Planners.

The Google Drive Desktop mirror exposes PDF *names*, not a portable public
Drive file ID. Never fabricate student URLs from filenames or local paths.
A lesson folder can opt in with ``planner_registration.json`` containing the
verified student/teacher Drive IDs, obtained when the files were uploaded.

This module is installed identically in CPM Tools, Science Tools, and the
maps_memories canonical shared_ui/agenda source. No network, OAuth, git, or
Drive write operations are performed during Planner load or save.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

_SCHEMAS = {'maps-planner-lesson-registration/1', 'maps-lesson-registration/1'}
_COURSES = {'algebra1': 'Algebra 1', 'apcalc': 'AP Calculus', 'physics': 'Physics'}
_ID = re.compile(r'^[A-Za-z0-9._-]{1,35}$')
_DRIVE_ID = re.compile(r'^[A-Za-z0-9_-]{12,200}$')
_DRIVE_URL = re.compile(r'^https://drive\.google\.com/file/d/([A-Za-z0-9_-]{12,200})/view(?:[/?#].*)?$', re.I)
_MAPPINGS = {'algebra1': 'Alg1', 'apcalc': 'APCalc', 'physics': 'Phy'}


def _safe_string(value, maximum=120):
    return value.strip() if isinstance(value, str) and 0 < len(value.strip()) <= maximum else ''


def _drive_url(value):
    """Accept a verified-looking Drive PDF ID/URL, never an inferred filename."""
    if not isinstance(value, str):
        return ''
    value = value.strip()
    found = _DRIVE_URL.fullmatch(value)
    if found:
        return f'https://drive.google.com/file/d/{found.group(1)}/view'
    if _DRIVE_ID.fullmatch(value):
        return f'https://drive.google.com/file/d/{value}/view'
    return ''


def candidate_course_dirs(workspace: Path, course: str):
    """Read-only locations used by the MAPS Google Drive for Desktop mirror."""
    if course not in _COURSES:
        return []
    relative = Path('~Curriculum') / '__MAPS_Courses' / _COURSES[course]
    paths = []
    # Allows a district-managed explicit sync folder without binding a user ID.
    explicit = os.environ.get('MAPS_LESSON_DRIVE_ROOT', '').strip()
    if explicit:
        base = Path(explicit).expanduser()
        paths.extend([base / _COURSES[course], base / relative])
    paths.extend([Path(workspace) / relative,
                  Path.home() / 'My Drive' / relative,
                  Path.home() / 'Google Drive' / 'My Drive' / relative])
    cloud = Path.home() / 'Library' / 'CloudStorage'
    try:
        paths.extend(sorted(cloud.glob('GoogleDrive-*/My Drive'))[:8])
    except OSError:
        pass
    # The CloudStorage loop added My Drive directories, not course roots.
    paths = [p / relative if p.name == 'My Drive' else p for p in paths]
    seen, result = set(), []
    for path in paths:
        norm = str(path)
        if norm not in seen:
            seen.add(norm)
            try:
                if path.is_dir():
                    result.append(path)
            except OSError:
                continue
    return result


def _registration_items(raw):
    if not isinstance(raw, dict) or raw.get('schema') not in _SCHEMAS:
        return []
    if isinstance(raw.get('lessons'), list):
        return raw['lessons'][:20]
    return [raw]


def _parse_row(raw, course, folder):
    if not isinstance(raw, dict):
        return None
    if raw.get('course_id', raw.get('course', course)) != course:
        return None
    name = _safe_string(raw.get('id', ''), 35)
    if not _ID.fullmatch(name):
        return None
    student_url = _drive_url(raw.get('student_pdf_id', '') or raw.get('student_url', ''))
    teacher_url = _drive_url(raw.get('teacher_pdf_id', '') or raw.get('teacher_url', ''))
    if not student_url:
        return None
    # Fail closed if the companion PDF was not actually copied into the folder.
    student_filename = _safe_string(raw.get('student_filename', ''), 150)
    prefix = _MAPPINGS[course] + '_'
    if (not student_filename or Path(student_filename).name != student_filename
            or not student_filename.startswith(prefix)
            or not student_filename.endswith('_Student.pdf')
            or not (folder / student_filename).is_file()):
        return None
    teacher_filename = _safe_string(raw.get('teacher_filename', ''), 150)
    if teacher_url:
        if (not teacher_filename or Path(teacher_filename).name != teacher_filename
                or not teacher_filename.startswith(prefix)
                or not teacher_filename.endswith('_Teacher.pdf')
                or not (folder / 'teacher' / teacher_filename).is_file()):
            return None
    label = _safe_string(raw.get('label', ''), 110) or name + ' Lesson'
    short = _safe_string(raw.get('short_name', ''), 110) or label
    agenda = _safe_string(raw.get('agenda_label', ''), 110) or label
    return {'id': name, 'label': label, 'short_name': short,
            'agenda_label': agenda, 'student_url': student_url,
            'teacher_url': teacher_url, 'folder': folder.as_posix(),
            'legacy_student_urls': []}


def discover(workspace: Path, course: str, existing: list[dict]) -> list[dict]:
    """Merge new verified registrations, preserving manually approved entries.

    A local PDF alone does not identify its Google Drive URL. Missing/invalid
    sidecars are ignored rather than breaking a working Planner.
    """
    if course not in _COURSES:
        return list(existing)
    merged = list(existing)
    seen_ids = {r.get('id') for r in existing}
    seen_urls = {_drive_url(r.get('student_url', '')) for r in existing}
    for course_dir in candidate_course_dirs(Path(workspace), course):
        try:
            chapters = sorted(p for p in course_dir.glob('ch_[0-9][0-9]') if p.is_dir())[:30]
        except OSError:
            continue
        for chapter in chapters:
            try:
                lesson_dirs = sorted(p for p in chapter.iterdir() if p.is_dir())[:180]
            except OSError:
                continue
            for folder in lesson_dirs:
                manifest = folder / 'planner_registration.json'
                try:
                    if not manifest.is_file() or manifest.stat().st_size > 60_000:
                        continue
                    raw = json.loads(manifest.read_text(encoding='utf-8'))
                    for item in _registration_items(raw):
                        row = _parse_row(item, course, folder)
                        if row is None:
                            continue
                        if row['id'] in seen_ids or row['student_url'] in seen_urls:
                            continue
                        # No arbitrary schema fields from sidecars are propagated.
                        merged.append(row)
                        seen_ids.add(row['id'])
                        seen_urls.add(row['student_url'])
                except (OSError, ValueError, TypeError, UnicodeError):
                    # Cloud-backed filenames can temporarily be inaccessible.
                    continue
    return merged
