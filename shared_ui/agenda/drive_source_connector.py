"""MAPS Planner verified lesson source index (offline, no OAuth or file scanning).

One authoritative index at maps_memories/shared_ui/agenda/course_sources.json.
The source index is updated as part of a lesson-building transfer AFTER ChatGPT
verifies the real Google Drive file IDs. All three Planners read it on request.
Never reads protected Mac Drive folders, performs Google authentication, or writes.
The pre-OAuth local approved files are read as legacy fallbacks only, preserving
previous teacher approvals without requiring a migration or calendar reset.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / 'course_sources.json'
LEGACY = ROOT / 'verified_drive_sources_20261124.json'
LEGACY_APPROVAL_DIR = Path.home() / '.config' / 'MAPS_Planner_Drive'
COURSES = {'algebra1': 'Alg1', 'apcalc': 'APCalc', 'physics': 'Phy'}
DRIVE_URL = re.compile(r'^https://drive\.google\.com/file/d/([A-Za-z0-9_-]{12,160})/view(?:[?#][^\s]*)?$')
LESSON_ID = re.compile(r'^[A-Za-z0-9_.-]{1,120}$')


def _read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError):
        return None


def _source_data(course):
    if course not in COURSES:
        return {'lessons': [], 'supports': []}
    # The stable index replaces the dated bootstrap. The bootstrap remains a
    # fallback only when migrating an older installation without an index yet.
    if INDEX.is_file():
        raw = _read_json(INDEX)
        good = isinstance(raw, dict) and raw.get('schema') == 'maps-course-sources/1'
    else:
        raw = _read_json(LEGACY)
        good = isinstance(raw, dict) and raw.get('schema') == 'maps-drive-verified-bootstrap/1'
    data = raw.get('courses', {}).get(course, {}) if good and isinstance(raw.get('courses'), dict) else {}
    if not isinstance(data, dict):
        data = {}
    return {'lessons': data.get('lessons', []) if isinstance(data.get('lessons'), list) else [],
            'supports': data.get('supports', []) if isinstance(data.get('supports'), list) else []}


def _legacy_approved(course):
    # Read old approved records if an OAuth pilot was actually used. Keep them
    # available offline; neither credentials nor tokens are read or written.
    raw = _read_json(LEGACY_APPROVAL_DIR / ('approved_' + course + '.json'))
    if not isinstance(raw, dict) or raw.get('schema') != 'maps-drive-approved-sources/1' or raw.get('course') != course:
        return {'lessons': [], 'supports': []}
    return {'lessons': raw.get('lessons', []) if isinstance(raw.get('lessons'), list) else [],
            'supports': raw.get('supports', []) if isinstance(raw.get('supports'), list) else []}


def _clean_lesson(course, item):
    if not isinstance(item, dict) or course not in COURSES:
        return None
    ident = item.get('id')
    url = item.get('student_url')
    if not isinstance(ident, str) or not LESSON_ID.fullmatch(ident) or not isinstance(url, str) or not DRIVE_URL.fullmatch(url):
        return None
    name = item.get('student_filename', '')
    if name and (not isinstance(name, str) or not name.startswith(COURSES[course] + '_') or not name.endswith('_Student.pdf')):
        return None
    label = item.get('label')
    if not isinstance(label, str) or not label.strip() or len(label) > 110:
        return None
    result = {'id': ident, 'label': label.strip(),
              'short_name': str(item.get('short_name') or label).strip()[:110],
              'agenda_label': str(item.get('agenda_label') or label).strip()[:110],
              'student_url': url, 'teacher_url': '', 'legacy_student_urls': []}
    teacher = item.get('teacher_url') or ''
    if isinstance(teacher, str) and DRIVE_URL.fullmatch(teacher):
        result['teacher_url'] = teacher
    if name:
        result['student_filename'] = name
    teacher_name = item.get('teacher_filename', '')
    if isinstance(teacher_name, str) and teacher_name.startswith(COURSES[course] + '_') and teacher_name.endswith('_Teacher.pdf'):
        result['teacher_filename'] = teacher_name
    return result


def approved_lessons(course):
    if course not in COURSES:
        return []
    rows = _source_data(course)['lessons'] + _legacy_approved(course)['lessons']
    result, ids, urls = [], set(), set()
    for item in rows:
        clean = _clean_lesson(course, item)
        if clean and clean['id'] not in ids and clean['student_url'] not in urls:
            result.append(clean)
            ids.add(clean['id'])
            urls.add(clean['student_url'])
    return result


def approved_supports(course):
    if course not in COURSES:
        return []
    rows = _source_data(course)['supports'] + _legacy_approved(course)['supports']
    result, ids, urls = [], set(), set()
    for item in rows:
        if not isinstance(item, dict):
            continue
        url, label, ident = item.get('url'), item.get('label'), item.get('id')
        if not isinstance(url, str) or not DRIVE_URL.fullmatch(url):
            continue
        if not isinstance(label, str) or not label.strip() or len(label) > 110:
            continue
        if not isinstance(ident, str) or not LESSON_ID.fullmatch(ident):
            continue
        filename = item.get('filename', '')
        if filename and (not isinstance(filename, str) or not filename.startswith(COURSES[course] + '_') or not filename.lower().endswith('.pdf') or filename.endswith('_Teacher.pdf')):
            continue
        if ident in ids or url in urls:
            continue
        result.append({'id': ident, 'label': label.strip(), 'url': url,
                       'file_id': DRIVE_URL.fullmatch(url).group(1),
                       'filename': filename if isinstance(filename, str) else ''})
        ids.add(ident)
        urls.add(url)
    return result


def merge_lessons(course, existing):
    """Existing teacher catalog always wins; verified entries are additive."""
    result = list(existing)
    ids = {x.get('id') for x in result if isinstance(x, dict)}
    urls = {x.get('student_url') for x in result if isinstance(x, dict)}
    for item in approved_lessons(course):
        if item['id'] not in ids and item['student_url'] not in urls:
            result.append(item)
            ids.add(item['id'])
            urls.add(item['student_url'])
    return result
