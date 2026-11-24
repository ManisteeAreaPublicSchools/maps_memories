"""MAPS Planner authenticated Drive source discovery and approved local overlays.

Never reads the protected Google Drive Desktop mount. OAuth uses the official
installed/desktop client type, PKCE and drive.metadata.readonly. This module has
no Drive write endpoint and never changes calendar state or static course catalogs.
All course apps share the same local authorization and approved source indexes.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import secrets
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = Path.home() / '.config' / 'MAPS_Planner_Drive'
BOOTSTRAP = Path(__file__).resolve().parents[2] / 'maps_memories' / 'shared_ui' / 'agenda' / 'verified_drive_sources_20261124.json'
CLIENT = BASE / 'oauth_desktop_client.json'
TOKEN = BASE / 'oauth_token.json'
SCOPE = 'https://www.googleapis.com/auth/drive.metadata.readonly'
GOOGLE_AUTH = 'https://accounts.google.com/o/oauth2/v2/auth'
GOOGLE_TOKEN = 'https://oauth2.googleapis.com/token'
DRIVE_FILES = 'https://www.googleapis.com/drive/v3/files'
FOLDER_MIME = 'application/vnd.google-apps.folder'
COURSES = {
    'algebra1': ('Algebra 1', 'Alg1', '1twlWt1R6H8TaMqRla7xgACDWW3-Uul2G'),
    'apcalc': ('AP Calculus', 'APCalc', '1jpXzhRdPTXU7bNQq_ex-tJfa0qf6Z2Vq'),
    'physics': ('Physics', 'Phy', '1YsdDzCvi34ykTNk24e8GIVy6_bPt2beM'),
}
MAX_FOLDERS = 500
MAX_FILES = 2200
MAX_SCAN_AGE = 20 * 60
SUPPORT_WORDS = ('worksheet', 'taskcard', 'task_card', 'station', 'practice',
                 'reviewpreview', 'review_preview', 'warmup', 'warm_up', 'handout',
                 'support', 'exit_ticket', 'extension', 'projection', 'rounds',
                 'homework', 'notessheet', 'formula', 'answersheet')
_LOCK = threading.RLock()
_PENDING = {}
_SCANS = {}
_DRIVE_ID = re.compile(r'^[A-Za-z0-9_-]{12,160}$')


class SourceError(RuntimeError):
    pass


def _protected_write(path, value):
    BASE.mkdir(mode=0o700, parents=True, exist_ok=True)
    try:
        os.chmod(BASE, 0o700)
    except OSError:
        pass
    data = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    tmp = path.with_name(path.name + '.' + secrets.token_hex(6) + '.tmp')
    descriptor = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
        os.chmod(path, 0o600)
    finally:
        if tmp.exists():
            tmp.unlink()


def _read_json(path, fallback=None):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        return fallback
    except (OSError, ValueError) as exc:
        raise SourceError('Saved Drive configuration is unreadable: ' + path.name) from exc


def _client():
    raw = _read_json(CLIENT)
    if not isinstance(raw, dict):
        return None
    cfg = raw.get('installed')
    if not isinstance(cfg, dict) or not str(cfg.get('client_id', '')).endswith('.apps.googleusercontent.com'):
        raise SourceError('Invalid installed OAuth client configuration')
    return cfg


def configure_client(raw):
    if not isinstance(raw, dict) or set(raw.keys()) != {'installed'}:
        raise SourceError('Use a Google OAuth client JSON with application type Desktop app.')
    cfg = raw['installed']
    if not isinstance(cfg, dict):
        raise SourceError('Invalid Desktop OAuth client.')
    client_id = cfg.get('client_id')
    secret = cfg.get('client_secret', '')
    if not isinstance(client_id, str) or not re.fullmatch(r'[A-Za-z0-9_.-]{10,200}\.apps\.googleusercontent\.com', client_id):
        raise SourceError('The Google Desktop app client ID is invalid.')
    if not isinstance(secret, str) or len(secret) > 300:
        raise SourceError('Invalid OAuth client secret.')
    with _LOCK:
        old = _client()
        _protected_write(CLIENT, {'installed': {'client_id': client_id, 'client_secret': secret}})
        if old and old['client_id'] != client_id and TOKEN.exists():
            TOKEN.unlink()
    return status()


def _token():
    token = _read_json(TOKEN)
    if not isinstance(token, dict):
        return None
    if token.get('client_id') != (_client() or {}).get('client_id'):
        return None
    if token.get('scope') != SCOPE:
        return None
    return token


def status(course=None):
    if course is not None and course not in COURSES:
        raise SourceError('Unknown Planner course.')
    client = _client()
    token = _token() if client else None
    response = {'ok': True, 'configured': bool(client),
                'connected': bool(token and (token.get('refresh_token') or token.get('access_token'))),
                'scope': 'Drive file names and IDs (read only)',
                'method': 'google_drive_api',
                'message': ('Connected. Update Sources will read Drive file metadata.' if token else
                            'Import a Google Desktop OAuth client JSON, then connect your account.' if not client else
                            'OAuth client installed. Choose Connect Google Drive to authorize read-only access.')}
    if course:
        saved = _read_approved(course)
        response['approved_lessons'] = len(saved['lessons'])
        response['approved_supports'] = len(saved['supports'])
    return response


def _send_json(url, data=None, bearer=None, timeout=12):
    body = None if data is None else urlencode(data).encode('utf-8')
    headers = {'Accept': 'application/json', 'User-Agent': 'MAPS-Planner-DriveSources/1'}
    if body is not None:
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    if bearer:
        headers['Authorization'] = 'Bearer ' + bearer
    try:
        with urlopen(Request(url, data=body, headers=headers), timeout=timeout) as response:
            raw = response.read(3_000_000)
        result = json.loads(raw.decode('utf-8'))
        if not isinstance(result, dict):
            raise ValueError('Expected JSON object')
        return result
    except HTTPError as exc:
        try:
            details = json.loads(exc.read(10_000).decode('utf-8'))
            error = details.get('error', {})
            message = error.get('message', '') if isinstance(error, dict) else str(error)
            if not message:
                message = str(details.get('error_description') or '')
        except (ValueError, UnicodeError):
            message = ''
        raise SourceError('Google Drive returned HTTP ' + str(exc.code) + (': ' + message[:190] if message else '')) from exc
    except (URLError, TimeoutError, ValueError, UnicodeError) as exc:
        raise SourceError('Google Drive could not be reached or returned invalid data: ' + str(exc)[:160]) from exc


def oauth_start(port):
    cfg = _client()
    if not cfg:
        raise SourceError('Import the Google Desktop OAuth client JSON first.')
    if not isinstance(port, int) or not 1024 <= port <= 65535:
        raise SourceError('Invalid Planner port')
    state = secrets.token_urlsafe(32)
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('ascii')).digest()).decode('ascii').rstrip('=')
    redirect_uri = 'http://127.0.0.1:' + str(port) + '/api/drive-sources/oauth/callback'
    with _LOCK:
        for key in list(_PENDING):
            if time.time() - _PENDING[key]['created'] > 600:
                del _PENDING[key]
        _PENDING[state] = {'verifier': verifier, 'redirect_uri': redirect_uri, 'created': time.time()}
    return GOOGLE_AUTH + '?' + urlencode({
        'client_id': cfg['client_id'], 'redirect_uri': redirect_uri,
        'response_type': 'code', 'scope': SCOPE, 'access_type': 'offline',
        'prompt': 'consent', 'code_challenge': challenge,
        'code_challenge_method': 'S256', 'state': state,
    })


def oauth_finish(state, code, error=''):
    with _LOCK:
        pending = _PENDING.pop(state, None)
    if not pending or time.time() - pending['created'] > 600:
        raise SourceError('This Google sign-in has expired. Start Connect Google Drive again.')
    if error:
        raise SourceError('Google sign-in was cancelled or declined: ' + error[:80])
    if not code or len(code) > 4096:
        raise SourceError('Google did not return an authorization code.')
    cfg = _client()
    if not cfg:
        raise SourceError('Missing Desktop OAuth client configuration.')
    request = {'code': code, 'client_id': cfg['client_id'],
               'client_secret': cfg.get('client_secret', ''), 'code_verifier': pending['verifier'],
               'redirect_uri': pending['redirect_uri'], 'grant_type': 'authorization_code'}
    result = _send_json(GOOGLE_TOKEN, request)
    scope = result.get('scope', '')
    if SCOPE not in scope.split(' '):
        raise SourceError('Google did not grant the required read-only metadata scope.')
    if not result.get('access_token'):
        raise SourceError('Google did not return an access token.')
    old = _token()
    refresh = result.get('refresh_token') or (old or {}).get('refresh_token')
    if not refresh:
        raise SourceError('Google did not provide an offline refresh token. Reconnect with consent.')
    _protected_write(TOKEN, {'client_id': cfg['client_id'],
                             'access_token': result['access_token'],
                             'refresh_token': refresh, 'scope': SCOPE,
                             'expires_at': int(time.time()) + int(result.get('expires_in', 3600)) - 90})
    return True


def _access_token():
    with _LOCK:
        token = _token()
        if not token:
            raise SourceError('Google Drive is not connected. Use Connect Google Drive first.')
        if token.get('access_token') and token.get('expires_at', 0) > time.time() + 15:
            return token['access_token']
        cfg = _client()
        if not token.get('refresh_token'):
            raise SourceError('Google session expired. Reconnect Google Drive.')
        new = _send_json(GOOGLE_TOKEN, {
            'client_id': cfg['client_id'], 'client_secret': cfg.get('client_secret', ''),
            'grant_type': 'refresh_token', 'refresh_token': token['refresh_token']
        })
        if not new.get('access_token'):
            raise SourceError('Google Drive token refresh failed. Reconnect Google Drive.')
        token.update(access_token=new['access_token'],
                     expires_at=int(time.time()) + int(new.get('expires_in', 3600)) - 90)
        _protected_write(TOKEN, token)
        return new['access_token']


def _list_children(folder_id, api=None):
    if not _DRIVE_ID.fullmatch(folder_id):
        raise SourceError('Invalid Drive folder ID')
    if api is None:
        api = _send_json
    items = []
    page_token = ''
    for _ in range(15):
        args = {'q': "'" + folder_id + "' in parents and trashed = false",
                'fields': 'nextPageToken,files(id,name,mimeType,parents)',
                'pageSize': '500', 'orderBy': 'name', 'supportsAllDrives': 'true',
                'includeItemsFromAllDrives': 'true'}
        if page_token:
            args['pageToken'] = page_token
        response = api(DRIVE_FILES + '?' + urlencode(args), bearer=_access_token())
        if not isinstance(response.get('files'), list):
            raise SourceError('Google Drive folder listing is incomplete.')
        for item in response['files']:
            if (isinstance(item, dict) and _DRIVE_ID.fullmatch(str(item.get('id', '')))
                    and isinstance(item.get('name'), str)):
                items.append(item)
        page_token = response.get('nextPageToken', '')
        if not page_token:
            return items
        if len(items) > MAX_FILES:
            raise SourceError('Source scan safety limit reached. No changes made.')
    raise SourceError('Google Drive listing exceeded the page limit. No changes made.')


def _category(name, parent_is_teacher):
    lower = name.casefold().replace('-', '_').replace(' ', '')
    if parent_is_teacher or lower.endswith('_teacher.pdf'):
        return 'teacher'
    stem = lower[:-4]
    is_support = any(word in stem for word in SUPPORT_WORDS)
    main = any(word in stem for word in ('lesson', 'lab', 'performance', 'testreview', 'reading', 'simulation', 'modeling'))
    return 'support' if is_support and not main else 'lesson'


def _row(course, info, chapter, folder, category):
    _, prefix, _ = COURSES[course]
    name = info['name']
    suffix = '_Teacher.pdf' if category == 'teacher' else '_Student.pdf'
    clean = name.startswith(prefix + '_') and name.lower().endswith(suffix.casefold())
    return {'file_id': info['id'], 'name': name, 'category': category,
            'chapter': chapter, 'folder': folder['name'], 'folder_id': folder['id'],
            'url': 'https://drive.google.com/file/d/' + info['id'] + '/view',
            'naming_ok': clean}


def _drive_scan(course, list_children=None):
    if course not in COURSES:
        raise SourceError('Unknown Planner course.')
    list_children = list_children or _list_children
    root_id = COURSES[course][2]
    folder_count = 0
    file_count = 0
    items = []
    chapters = list_children(root_id)
    found_chapters = False
    for chapter in chapters:
        if chapter.get('mimeType') != FOLDER_MIME or not re.fullmatch(r'ch_\d{2}', chapter['name']):
            continue
        found_chapters = True
        for lesson_folder in list_children(chapter['id']):
            if lesson_folder.get('mimeType') != FOLDER_MIME:
                continue
            folder_count += 1
            if folder_count > MAX_FOLDERS:
                raise SourceError('Too many lesson folders. No changes made.')
            def collect(folder_id, parent_is_teacher=False, depth=0):
                nonlocal folder_count, file_count
                if depth > 2:
                    return
                for file in list_children(folder_id):
                    if file.get('mimeType') == FOLDER_MIME:
                        if file.get('name', '').casefold() in ('teacher', 'support', 'supports', 'worksheets',
                            'task_cards', 'stations', 'resources', 'handouts', 'printables', 'practice'):
                            folder_count += 1
                            if folder_count > MAX_FOLDERS:
                                raise SourceError('Too many subfolders. No changes made.')
                            collect(file['id'], parent_is_teacher or file['name'].casefold() == 'teacher', depth+1)
                        continue
                    if file.get('mimeType') != 'application/pdf' and not file['name'].lower().endswith('.pdf'):
                        continue
                    file_count += 1
                    if file_count > MAX_FILES:
                        raise SourceError('Too many PDFs. No changes made.')
                    kind = _category(file['name'], parent_is_teacher)
                    items.append(_row(course, file, chapter['name'], lesson_folder, kind))
            collect(lesson_folder['id'])
    if not found_chapters:
        raise SourceError('No ch_XX folders were returned by Drive. Check that this Google account has access to the course folder.')
    if not items:
        raise SourceError('Google Drive returned no PDF files from the course lesson folders. No catalog changes were made.')
    return items


def _approved_path(course):
    if course not in COURSES:
        raise SourceError('Unknown course')
    return BASE / ('approved_' + course + '.json')


def _read_approved(course):
    raw = _read_json(_approved_path(course), {'schema': 'maps-drive-approved-sources/1',
                                            'course': course, 'lessons': [], 'supports': []})
    if not isinstance(raw, dict) or raw.get('schema') != 'maps-drive-approved-sources/1' or raw.get('course') != course:
        raise SourceError('Approved source index is invalid. The existing Planner catalog remains safe.')
    if not isinstance(raw.get('lessons'), list) or not isinstance(raw.get('supports'), list):
        raise SourceError('Approved source list is invalid.')
    return raw


def _bootstrap(course):
    """One-time teacher-verified Drive IDs, not a replacement for live OAuth."""
    try:
        raw = _read_json(BOOTSTRAP, {})
        if not isinstance(raw, dict) or raw.get('schema') != 'maps-drive-verified-bootstrap/1':
            return {'lessons': [], 'supports': []}
        course_data = raw.get('courses', {}).get(course, {})
        if not isinstance(course_data, dict):return {'lessons': [], 'supports': []}
        return {'lessons': course_data.get('lessons', []), 'supports': course_data.get('supports', [])}
    except (SourceError, OSError, ValueError, TypeError):
        return {'lessons': [], 'supports': []}


def _existing_ids(existing):
    return {url.rsplit('/file/d/',1)[-1].split('/',1)[0]
            for item in existing if isinstance(item, dict)
            for url in [str(item.get('student_url', ''))] if '/file/d/' in url}


def scan_sources(course, existing, scanner=None):
    """Complete scan or fail atomically. Never claim success on partial data."""
    if course not in COURSES:
        raise SourceError('Unknown course')
    if not status()['connected']:
        raise SourceError('Google Drive is not connected. Import your Desktop OAuth JSON and sign in.')
    items = (scanner or _drive_scan)(course)
    if not isinstance(items, list):
        raise SourceError('Google Drive did not return a complete source list.')
    registered = _existing_ids(existing)
    overlay = _read_approved(course)
    registered.update(_existing_ids(approved_lessons(course)))
    registered.update(s['file_id'] for s in approved_supports(course))
    for item in items:
        item['registered'] = item['file_id'] in registered
    counts = {key:sum(x['category']==key for x in items) for key in ('lesson', 'teacher', 'support')}
    counts['new'] = sum(x['category'] in ('lesson','support') and not x['registered'] for x in items)
    counts['invalid_names'] = sum(not x['naming_ok'] for x in items)
    token = secrets.token_urlsafe(24)
    with _LOCK:
        _SCANS[course] = {'token': token, 'created': time.time(),
                          'items': items, 'registered_ids': registered}
    return {'ok': True, 'available': True, 'course': course, 'method': 'google_drive_api',
            'scan_token': token, 'items': items, 'counts': counts, 'errors': [],
            'message': 'Google Drive scan completed. Review new files before adding them to the Planner.',
            'scanned_at': datetime.now(timezone.utc).isoformat(), 'can_approve': True}


def _label(row):
    _, prefix, _ = COURSES[row['course']]
    name = row['name'][:-4]
    name = re.sub(r'_(?:Student|Teacher)$', '', name, flags=re.I)
    if name.startswith(prefix+'_'):
        name = name[len(prefix)+1:]
    return re.sub(r'_+', ' ', name).strip()[:105] or 'Lesson'


def _id_for_drive(file_id):
    return 'drv_' + hashlib.sha256(file_id.encode('ascii')).hexdigest()[:24]


def approve_sources(course, scan_token, file_ids, existing):
    if course not in COURSES:
        raise SourceError('Unknown course')
    if not isinstance(file_ids, list) or len(file_ids) > MAX_FILES or any(not isinstance(i,str) for i in file_ids):
        raise SourceError('Invalid source selection.')
    with _LOCK:
        snapshot = _SCANS.get(course)
        if (not snapshot or not secrets.compare_digest(str(scan_token), snapshot['token'])
                or time.time() - snapshot['created'] > MAX_SCAN_AGE):
            raise SourceError('The source review expired. Click Update Sources again.')
        available = {i['file_id']: i for i in snapshot['items']}
        selected = set(file_ids)
        if len(selected) != len(file_ids) or any(i not in available for i in selected):
            raise SourceError('Source selection does not match the verified Drive scan.')
        saved = _read_approved(course)
        known = _existing_ids(existing) | _existing_ids(approved_lessons(course))
        known_supports = {s['file_id'] for s in approved_supports(course)}
        teacher_by_folder = {}
        for item in snapshot['items']:
            if item['category'] == 'teacher':
                teacher_by_folder.setdefault(item['folder_id'], []).append(item)
        new_lessons, new_supports = [], []
        for file_id in sorted(selected):
            item = available[file_id]
            if item['category'] == 'teacher':
                continue  # Never publish teacher-only material as a lesson.
            if not item['naming_ok']:
                raise SourceError('Rename the file before approval: ' + item['name'])
            if item['category'] == 'lesson' and file_id not in known:
                teacher_choices = teacher_by_folder.get(item['folder_id'], [])
                teacher = next((t for t in teacher_choices if t['naming_ok']), None)
                lbl = _label({**item, 'course': course})
                new_lessons.append({'id': _id_for_drive(file_id), 'label': lbl,
                                    'short_name': lbl, 'agenda_label': lbl,
                                    'student_url': item['url'],
                                    'teacher_url': teacher['url'] if teacher else '',
                                    'student_filename': item['name'],
                                    'teacher_filename': teacher['name'] if teacher else ''})
                known.add(file_id)
            if item['category'] == 'support' and file_id not in known_supports:
                lbl = _label({**item, 'course': course})
                new_supports.append({'id': _id_for_drive(file_id), 'label': lbl,
                                     'url': item['url'], 'file_id': file_id,
                                     'filename': item['name'], 'folder': item['folder']})
                known_supports.add(file_id)
        saved['lessons'].extend(new_lessons)
        saved['supports'].extend(new_supports)
        saved['updated_at'] = datetime.now(timezone.utc).isoformat()
        if new_lessons or new_supports:
            _protected_write(_approved_path(course), saved)
        _SCANS.pop(course, None)
        return {'ok': True, 'added_lessons': len(new_lessons),
                'added_supports': len(new_supports),
                'message': 'Sources added locally. Choose a lesson in the Planner; Save updates the student page.'}


def approved_lessons(course):
    try:
        saved = list(_read_approved(course)['lessons'])
    except SourceError:
        saved = []
    return list(_bootstrap(course)['lessons']) + saved


def approved_supports(course):
    try:
        saved = list(_read_approved(course)['supports'])
    except SourceError:
        saved = []
    return list(_bootstrap(course)['supports']) + saved


def merge_lessons(course, existing):
    """Existing catalog wins. New approved IDs are additive and offline-ready."""
    result = list(existing)
    seen_id = {x.get('id') for x in existing}
    seen_url = {x.get('student_url') for x in existing}
    for lesson in approved_lessons(course):
        if lesson.get('id') in seen_id or lesson.get('student_url') in seen_url:
            continue
        url = lesson.get('student_url', '')
        if not re.fullmatch(r'https://drive\.google\.com/file/d/[A-Za-z0-9_-]{12,160}/view',url):
            continue
        result.append(lesson)
        seen_id.add(lesson['id'])
        seen_url.add(url)
    return result
