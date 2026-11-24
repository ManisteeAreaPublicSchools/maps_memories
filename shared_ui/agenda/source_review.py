"""MAPS Planner Update Sources, stage 1: safe, read-only Drive mirror inventory.

No network, no Drive file-ID inference, no writes to calendars or catalogs.
The inventory is deliberately separate from lesson_discovery/catalog selection.
"""
from __future__ import annotations
import re
from datetime import datetime, timezone
from pathlib import Path
from lesson_discovery import candidate_course_dirs

COURSES = {'algebra1': 'Alg1', 'apcalc': 'APCalc', 'physics': 'Phy'}
SUPPORT_WORDS = ('worksheet', 'taskcard', 'station', 'practice', 'reviewpreview',
                 'review_preview', 'warmup', 'handout', 'support', 'exit_ticket',
                 'extension', 'projection', 'rounds', 'notes', 'homework')
LEARNING_WORDS = ('lesson', 'lab', 'performancetask', 'performance_task', 'assessment',
                  'simulation', 'videolab', 'reading', 'review', 'test', 'modeling')
MAX_FOLDERS = 900
MAX_FILES = 4500


def _inventory_folder(folder: Path, lesson_chapter: str, pdfs: list, notes: list,
                      counters: dict, prefix: str, course: str, catalog: list):
    try:
        children = sorted(folder.iterdir(), key=lambda p:p.name.casefold())
    except (OSError, PermissionError) as exc:
        notes.append('Cannot list ' + folder.name + ': ' + type(exc).__name__)
        return
    counters['folders'] += 1
    if counters['folders'] > MAX_FOLDERS:
        notes.append('Folder safety limit reached; scan incomplete.')
        return
    for item in children:
        if counters['files'] >= MAX_FILES:
            notes.append('File safety limit reached; scan incomplete.')
            return
        # Enumerate names and directory metadata only, never hydrate PDF bytes.
        try:
            symlink = item.is_symlink()
            directory = item.is_dir() if not symlink else False
        except (OSError, PermissionError):
            notes.append('Cannot inspect a cloud file in ' + folder.name)
            continue
        if symlink:
            continue  # Never follow a symlink outside the approved course tree.
        if directory:
            if item.name.lower() in ('teacher','support','supports','worksheets','task_cards',
                                     'stations','handouts','resources','printables','practice'):
                _inventory_folder(item, lesson_chapter, pdfs, notes, counters,
                                  prefix, course, catalog)
            continue
        if item.suffix.lower() != '.pdf':
            continue
        counters['files'] += 1
        name = item.name
        is_teacher = item.parent.name.lower() == 'teacher' or name.lower().endswith('_teacher.pdf')
        lower = name.lower().replace('-', '_')
        clean = name.startswith(prefix+'_') and (
            lower.endswith('_teacher.pdf') if is_teacher else lower.endswith('_student.pdf'))
        stem = name[:-4]
        if stem.startswith(prefix+'_'):
            stem = stem[len(prefix)+1:]
        stem = re.sub(r'_(student|teacher)$', '', stem, flags=re.I)
        term = stem.lower().replace(' ','').replace('-', '')
        support = any(word in term for word in SUPPORT_WORDS)
        learning = any(word in term for word in LEARNING_WORDS)
        kind = 'teacher' if is_teacher else ('support' if support and not any(
            word in term for word in ('testreview','reading','lesson','lab','performancetask'))
            else 'lesson')
        # Existing registration is trusted only when supplied by the existing
        # course catalog. File ID/URL is never generated from a filename.
        linked = None
        if kind != 'teacher':
            for entry in catalog:
                if entry.get('student_filename') == name and re.match(r'^https://drive\.google\.com/file/d/[A-Za-z0-9_-]+/view',str(entry.get('student_url',''))):
                    linked = entry
                    break
                if not entry.get('student_filename') and entry.get('folder'):
                    existing_folder = str(entry['folder']).rstrip('/').split('/')[-1]
                    if existing_folder == folder.name and not is_teacher and kind == 'lesson' and re.match(r'^https://drive\.google\.com/file/d/[A-Za-z0-9_-]+/view',str(entry.get('student_url',''))):
                        linked = entry
                        break
        pdfs.append({'chapter':lesson_chapter, 'folder':folder.parent.name if is_teacher else folder.name,
                     'name':name, 'category':kind, 'naming_ok':bool(clean),
                     'registered':bool(linked),
                     'registered_label':str(linked.get('label',''))[:110] if linked else '',
                     'url':str(linked.get('student_url','')) if linked else '',
                     'link_status':'registered' if linked else 'needs_drive_id'})


def scan_sources(workspace: Path, course: str, catalog: list) -> dict:
    """Read-only preview. Reject unsupported course and fail closed on errors."""
    if course not in COURSES:
        raise ValueError('Unknown course')
    prefix = COURSES[course]
    roots = candidate_course_dirs(workspace, course)
    pdfs, errors = [], []
    counts={'folders':0,'files':0}
    if not roots:
        return {'ok':True, 'course':course,'available':False,
                'message':'Google Drive Desktop course folder is not accessible. Check Drive is running and the course folder is available in Finder.',
                'items':[], 'counts':{'lesson':0,'teacher':0,'support':0,'unlinked':0,'invalid_names':0},
                'errors':[], 'method':'local_drive_mirror_preview',
                'can_approve':False,'needs_authenticated_drive_api':True}
    for root in roots[:3]:
        try:
            chapters=sorted((p for p in root.iterdir()
                             if p.is_dir() and re.fullmatch(r'ch_\d{2}',p.name)),
                            key=lambda p:p.name)
        except (OSError, PermissionError) as exc:
            errors.append('Cannot list course folder: ' + type(exc).__name__)
            continue
        for chapter in chapters[:40]:
            try:
                lesson_dirs=sorted((p for p in chapter.iterdir() if p.is_dir()),
                                   key=lambda p:p.name)
            except (OSError,PermissionError) as exc:
                errors.append('Cannot list ' + chapter.name + ': ' + type(exc).__name__)
                continue
            for folder in lesson_dirs[:200]:
                _inventory_folder(folder,chapter.name,pdfs,errors,counts,
                                  prefix,course,catalog)
                if counts['folders']>=MAX_FOLDERS or counts['files']>=MAX_FILES:
                    break
    # Multiple mounted views of the same folder must not duplicate results.
    seen=set(); unique=[]
    for row in pdfs:
        key=(row['chapter'],row['folder'],row['name'],row['category'])
        if key not in seen:
            seen.add(key);unique.append(row)
    summary={k:sum(x['category']==k for x in unique) for k in ('lesson','teacher','support')}
    summary['unlinked']=sum(x['link_status']=='needs_drive_id' and x['category']!='teacher' for x in unique)
    summary['invalid_names']=sum(not x['naming_ok'] for x in unique)
    return {'ok':True,'course':course,'available':True,
            'message':'Read-only preview. Files without existing verified catalog links need Drive API authentication before they can be approved.',
            'items':unique,'counts':summary,'errors':errors[:15],
            'method':'local_drive_mirror_preview',
            'can_approve':False,'needs_authenticated_drive_api':True,
            'scanned_at':datetime.now(timezone.utc).isoformat()}
