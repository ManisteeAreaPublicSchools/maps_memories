"""MAPS shared local Math Planner for Algebra 1 and AP Calculus in CPM Tools."""
from __future__ import annotations
import json,html,os,threading,copy,re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
from course_artifact_naming import validate_artifact_name
from lesson_discovery import discover as discover_drive_lessons

LOCK=threading.RLock()
SCHEMA='maps-math-planner/1'
CUTOFF='2026-11-19'
CLOSED={'Break','P.D.','No School','Snow Day','Holiday'}
URLS={'algebra1':'https://tnezki.github.io/algebra/agenda/index.html','apcalc':'https://tnezki.github.io/apcalc/agenda/index.html'}
NAMES={'algebra1':'Algebra 1','apcalc':'AP Calculus AB'}

def paths(course,root):
    if course not in URLS: raise ValueError('Unknown course')
    return {'state':root/'CPM_Tools_Library/planner'/f'{course}.json','legacy':root/'_algebra_teacher_tools/planner/planner_state.json' if course=='algebra1' else None,'calendar':root/'CPM_Tools/planner/calendar_2026_2027.json','catalog':root/'CPM_Tools/planner'/('algebra1_lesson_catalog.json' if course=='algebra1' else 'apcalc_lesson_catalog.json'),'student':root/('algebra' if course=='algebra1' else 'apcalc')/'agenda/index.html','teacher':root/'teacher_shared'/('algebra' if course=='algebra1' else 'calc')/'planner/index.html','resources':root/'CPM_Tools/planner/resource_links.json'}

def atomic(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(text,encoding='utf-8');os.replace(tmp,path)

def empty():return {'label':'','url':''}

def valid_url(s):
    if not s:return ''
    if not isinstance(s,str) or len(s)>4000:raise ValueError('Invalid URL')
    s=s.strip();p=urlparse(s)
    if p.scheme in {'http','https'} and p.netloc and not p.username and not p.password:return s
    if s.startswith('/') and not s.startswith('//') and '\\' not in s and '\n' not in s:return s
    raise ValueError('Links must be http(s) or an absolute local path')

def text(s,n=160):
    if not isinstance(s,str) or len(s)>n:raise ValueError('Invalid planner text')
    return s.strip()

def item(d):
    if not isinstance(d,dict):d={}
    return {'label':text(d.get('label','')),'url':valid_url(d.get('url',''))}

def init(course,p):
    base=json.loads(p['calendar'].read_text())
    dates=base['days'];assert len(dates)==215
    ds=[]
    for src in dates:
        ds.append({**src,'title':'','row3':empty(),'lesson_choice':'','lesson_custom':{},'extra_rows':[empty() for _ in range(4)],'teacher_url':'','teacher_label':'Teacher Guide'})
    imported=0
    if course=='algebra1' and p['legacy'].is_file():
        legacy=json.loads(p['legacy'].read_text())
        originals={x['date']:x for x in legacy['days']}
        for d in ds:
            if d['date']>CUTOFF:continue
            old=originals.get(d['date'])
            if not old:continue
            d['title']=str(old.get('section') or '')[:160]
            prev=old.get('control') or 'Regular Day'
            if prev!='Regular Day' or d['control']=='Regular Day':d['control']=prev
            slots=old.get('student_slots') or []
            customs=old.get('custom_slots') or []
            previous=[]
            for idx in range(5):
                name=str(slots[idx] or '') if idx<len(slots) else ''
                custom=customs[idx] if idx<len(customs) and isinstance(customs[idx],dict) else {}
                if name=='Custom Item':previous.append(item({'label':str(custom.get('label') or 'Custom Item')[:160],'url':str(custom.get('url') or '')}))
                else:previous.append(item({'label':name[:160]}))
            d['row3']=previous[0];d['extra_rows']=previous[1:]
            imported+=1
    return {'schema':SCHEMA,'course_id':course,'school_year':'2026-2027','revision':0,'current_week_index':base['current_week_index'],'days':ds,'migration':{'source':'Legacy Algebra calendar' if course=='algebra1' else 'Blank slate','past_preserved_through':CUTOFF if course=='algebra1' else '','imported_days':imported,'future_lesson_entries_preserved':0}}

def load(course,root):
    p=paths(course,root)
    with LOCK:
        if not p['state'].is_file():atomic(p['state'],json.dumps(init(course,p),indent=2)+'\n')
        state=json.loads(p['state'].read_text())
        if state.get('schema')!=SCHEMA or state.get('course_id')!=course or len(state.get('days',[]))!=215:raise ValueError('Invalid Math Planner state')
        return state

def catalog(course,root):
    p=paths(course,root)['catalog'];data=json.loads(p.read_text())['lessons']
    for entry in data:
        for k in ('student_filename','teacher_filename'):
            if entry.get(k) and not validate_artifact_name(entry[k],course):raise ValueError('Invalid course filename: '+entry[k])
        for k in ('student_url','teacher_url'):valid_url(entry.get(k,''))
    return discover_drive_lessons(root,course,data)

def resource_links(course,root,state):
    """Read restored course links without mutating Google Drive or teacher files.

    Only the local CPM Tools data file is read. Paths and file permissions in a
    Google Drive for Desktop mount must never determine whether a Planner loads.
    """
    raw=json.loads(paths(course,root)['resources'].read_text(encoding='utf-8'))
    if raw.get('schema')!='maps-math-planner-resource-links/1':
        raise ValueError('Unsupported resource link catalog')
    entry=raw.get(course)
    if not isinstance(entry,dict):raise ValueError('Missing course resources')
    # Legacy teacher library selector followed the currently taught unit.
    # Derive it from the current week's work, then previous weeks if blank.
    week=state.get('current_week_index',0)
    unit=1
    for day in reversed(state['days']):
        if day.get('week_index',999)>week:continue
        title=day.get('title') or day.get('lesson_choice') or ''
        match=re.match(r'\s*(\d+)\.',str(title))
        if match and int(match.group(1))>0:
            unit=int(match.group(1));break
    def collect(kind):
        result=[]
        for row in entry.get(kind,[]):
            if not isinstance(row,dict):raise ValueError('Invalid resource link')
            label=text(row.get('label',''),80)
            url=valid_url(row.get('url',''))
            if not label or not url:raise ValueError('Incomplete resource link')
            if row.get('current_unit'):
                url=re.sub(r'/unit\d+/',f'/unit{unit}/',url)
            result.append({'label':label,'url':url})
        return result
    return {'student':collect('student'),'teacher':collect('teacher')}


def get_payload(course,root):
    # Read-only GET. Never repair or rewrite mirrored Drive lesson HTML here.
    state=load(course,root)
    return {'ok':True,'state':state,'lessons':catalog(course,root),
            'resources':resource_links(course,root,state),
            'course_title':NAMES[course],'public_url':URLS[course]}

def display(d,index):
    choice=d.get('lesson_choice','');lesson=index.get(choice);custom=d.get('lesson_custom') if choice=='__custom__' else None
    title=d.get('title','');pdf=d.get('row3') or empty();teacher=d.get('teacher_url','');teacher_label=d.get('teacher_label','Teacher Guide')
    if custom:
        title=custom.get('short_name') or custom.get('label') or title;pdf={'label':custom.get('label',''),'url':custom.get('url','')};teacher=custom.get('teacher_url','')
    elif lesson:
        title=lesson.get('short_name') or lesson.get('label') or title;pdf={'label':lesson.get('agenda_label') or lesson['label'],'url':lesson['student_url']};teacher=lesson.get('teacher_url','')
    control=d.get('control','Regular Day')
    if control in CLOSED:return {'title':control,'pdf':empty(),'extras':[empty() for _ in range(4)],'teacher':empty()}
    if control!='Regular Day':title=control+(' · '+title if title else '')
    return {'title':title,'pdf':pdf,'extras':d.get('extra_rows') or [empty() for _ in range(4)],'teacher':{'label':teacher_label if teacher else '', 'url':teacher}}

def anchor(v):
    label=html.escape(str(v.get('label') or ''));url=html.escape(str(v.get('url') or ''),quote=True)
    if not label:return '&nbsp;'
    if url:return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
    return f'<span>{label}</span>'

CSS='''*{box-sizing:border-box}
body{background:#f4f6fa;color:#17314c;font:15px/1.4 Arial,sans-serif;margin:0}
main{width:min(1500px,calc(100% - 28px));max-width:100%;margin:22px auto}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
h2{color:#173f6d;margin:20px 0 10px;font-size:clamp(18px,1.75vw,23px)}
html{scroll-behavior:smooth}
#year-current-week{scroll-margin-top:12px}
.floating-top{position:fixed;right:20px;bottom:20px;z-index:30;display:inline-flex;align-items:center;justify-content:center;min-height:43px;padding:9px 17px;border:2px solid #173f6d;border-radius:999px;background:#fff1bd;color:#173f6d;text-decoration:none;font-size:14px;font-weight:850;box-shadow:0 4px 14px #173f6d33}
.floating-top:hover,.floating-top:focus-visible{background:#e2bc4f;text-decoration:underline}
.link-panel{margin:14px 0 20px;padding:13px 16px;background:#fff9e8;border:1px solid #e8d39d;border-radius:11px}
.link-panel h2{font-size:13px;margin:4px 0 9px;letter-spacing:.04em;text-transform:uppercase;color:#77571d}
.link-panel nav{display:flex;flex-wrap:wrap;gap:8px 9px}
.link-panel a{display:inline-block;padding:7px 12px;background:white;border:1px solid #d9c58d;border-radius:100px;text-decoration:none;color:#173f6d;font-size:13px;font-weight:720}
.link-panel a:hover,.link-panel a:focus-visible{background:#fff0c7;text-decoration:underline}
.link-panel .teacher-links{margin-top:14px;border-top:1px solid #ecd9b2;padding-top:11px}
.scroller{overflow-x:auto;max-width:100%;border:1px solid #cbd2d9;border-radius:7px}
table{table-layout:fixed;border-collapse:collapse;min-width:0;width:100%}
th,td{width:20%;text-align:center;border-right:1px solid #cbd2d9;border-bottom:1px solid #cbd2d9}
th{background:#e2bc4f;padding:8px 7px;text-align:left;color:#173f6d;font-size:clamp(11px,1vw,15px);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
th small{margin-left:6px;font-size:.9em}
td{height:40px;background:#fff9e8}tr:nth-child(odd):not(:first-child) td{background:#fff0c7}
td a,td span{display:block;height:40px;line-height:40px;padding:0 5px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;color:#173f6d;font-weight:750;font-size:clamp(10px,.86vw,14px)}
a:hover{text-decoration:underline}
.week:not(.current) th{background:#434b55;color:white;border-top:5px solid #222}
.week:not(.current) td{background:#fff}.week:not(.current) tr:nth-child(odd):not(:first-child) td{background:#f3f4f6}
.week{margin:13px 0}.week h3{font-size:14px;margin:6px 0;color:#374151}
.current{margin:10px 0 20px}
.all{background:#173f6d;color:#fff;font-weight:850;padding:9px 12px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:12px;margin:24px 0 12px;border-radius:6px}
.all>strong{grid-column:2;font-size:1rem;letter-spacing:.025em}
.all-nav{grid-column:3;display:flex;align-items:center;justify-content:flex-end;flex-wrap:wrap;gap:8px}
.all-nav a{display:inline-flex;align-items:center;justify-content:center;min-height:35px;padding:6px 12px;background:#fff;color:#173f6d;border-radius:8px;border:1px solid #d3b66e;text-decoration:none;font-size:.85rem;font-weight:850}
.all-nav a:hover,.all-nav a:focus-visible{background:#fff0c7;text-decoration:underline}
@media(max-width:700px){.all{grid-template-columns:1fr;justify-items:center}.all>strong,.all-nav{grid-column:1}.all-nav{justify-content:center}}
.special{display:inline-block;font-size:10px;background:#fff7e2;color:#694c17;padding:2px 4px;margin-left:3px;border-radius:3px}
@media(max-width:700px){main{width:calc(100% - 14px);margin:9px auto}.scroller table{min-width:650px}.link-panel{padding:10px}.link-panel a{font-size:12px}th{font-size:12px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{.all-nav,.floating-top{display:none!important}.scroller{overflow:visible}main{width:100%}.week{break-inside:avoid}table{min-width:0!important}}'''


def _shared_agenda_css() -> str:
    """Shared MAPS agenda CSS copied locally with an offline fallback."""
    stylesheet=Path(__file__).resolve().parents[1]/'planner'/'student_agenda.css'
    try:return '\n'+stylesheet.read_text(encoding='utf-8')
    except OSError:return ''  # Existing inline CSS remains available offline.


def table(days,index,teacher=False):
    parts=['<div class="scroller"><table><tbody><tr>']
    for d in days:
        status=d['control'];flag='<small class="special">'+html.escape(status)+'</small>' if status!='Regular Day' else ''
        parts.append(f'<th>{html.escape(d["dow"])} <small>{html.escape(d["display_date"])}</small>{flag}</th>')
    parts.append('</tr>')
    info=[display(d,index) for d in days]
    for key in ('title','pdf',0,1,2,3,'teacher'):
        if key=='teacher' and not teacher:continue
        parts.append('<tr>')
        for v in info:
            row={'label':v['title'],'url':''} if key=='title' else v['pdf'] if key=='pdf' else v['teacher'] if key=='teacher' else v['extras'][key]
            parts.append('<td>'+anchor(row)+'</td>')
        parts.append('</tr>')
    parts.append('</tbody></table></div>')
    return ''.join(parts)

def resource_panel(groups,teacher=False):
    parts=['<section class="link-panel agenda-resource-row" aria-label="Course resources">']
    for label,rows,klass in [('Resources',groups.get('student',[]),''),
                            ('Teacher Resources',groups.get('teacher',[]) if teacher else [],'teacher-links')]:
        if not rows:continue
        parts.extend([f'<div class="{klass}"><h2>{html.escape(label)}</h2><nav>'])
        for row in rows:
            parts.append('<a href="'+html.escape(row['url'],quote=True)+'" target="_blank" rel="noopener">'+html.escape(row['label'])+'</a>')
        parts.append('</nav></div>')
    parts.append('</section>')
    return ''.join(parts)


def agenda(course,state,lessons,teacher=False,resources=None):
    byweek={};idx={d['id']:d for d in lessons}
    for d in state['days']:byweek.setdefault(d['week_index'],[]).append(d)
    current=state['current_week_index'];title=NAMES[course]+(' Teacher Agenda' if teacher else ' Student Agenda')
    # Keep a screen-reader heading; omit the oversized visual banner and the
    # duplicate Current Week heading. Current Week navigation belongs only in ALL WEEKS; Top stays floating.
    p=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+_shared_agenda_css()+'</style></head><body><main class="agenda-shell" id="page-top"><h1 class="sr-only">'+html.escape(title)+'</h1>',
       '<header class="agenda-topbar"><span class="agenda-topbar__title">'+html.escape(NAMES[course])+(' · Teacher Agenda' if teacher else ' · Student Agenda')+' 2026–27</span></header>',
       resource_panel(resources or {},teacher),'<div class="current">',table(byweek[current],idx,teacher),'</div><div class="all"><span aria-hidden="true"></span><strong>ALL WEEKS</strong><nav class="all-nav" aria-label="Agenda navigation"><a href="#year-current-week">Current Week</a></nav></div>']
    for n,ds in sorted(byweek.items()):
        current_anchor=' id="year-current-week"' if n==current else ''
        p.extend(['<section'+current_anchor+' class="week'+(' current' if n==current else '')+'"><h3>Week of '+html.escape(ds[0]['display_date'])+(' · CURRENT WEEK' if n==current else '')+'</h3>',table(ds,idx,teacher),'</section>'])
    return ''.join(p)+'<a class="floating-top" href="#page-top" aria-label="Back to top of agenda" title="Back to top">↑ Top</a></main></body></html>'

def save_and_publish(course,root,body):
    if not isinstance(body,dict):raise ValueError('Invalid request')
    with LOCK:
        previous=load(course,root)
        if previous['revision']!=body.get('revision'):raise ValueError('Planner was saved in another tab. Reload and try again.')
        proposed=body.get('days')
        if not isinstance(proposed,list) or len(proposed)!=215:raise ValueError('Expected 215 calendar dates')
        names={d['id'] for d in catalog(course,root)}
        result=[]
        for old,raw in zip(previous['days'],proposed):
            if not isinstance(raw,dict) or old['date']!=raw.get('date'):raise ValueError('School dates cannot change')
            new=copy.deepcopy(old);new['control']=text(raw.get('control','Regular Day'),65);new['title']=text(raw.get('title',''))
            choice=text(raw.get('lesson_choice',''),120)
            if choice not in names|{'','__custom__'}:raise ValueError('Unknown lesson selection')
            new['lesson_choice']=choice
            custom=raw.get('lesson_custom') or {}
            if choice=='__custom__':
                if not isinstance(custom,dict):raise ValueError('Invalid custom lesson')
                new['lesson_custom']={k:valid_url(custom.get(k,'')) if k in ('url','teacher_url') else text(custom.get(k,'')) for k in ('label','short_name','url','teacher_url')}
                if not new['lesson_custom']['label']:raise ValueError('Custom lesson label required')
            else:new['lesson_custom']={}
            new['row3']=item(raw.get('row3'));rows=raw.get('extra_rows')
            if not isinstance(rows,list) or len(rows)!=4:raise ValueError('Four optional rows required')
            new['extra_rows']=[item(x) for x in rows];new['teacher_url']=valid_url(raw.get('teacher_url',''));new['teacher_label']=text(raw.get('teacher_label',''))
            result.append(new)
        week=body.get('current_week_index')
        if not isinstance(week,int) or not 0<=week<43:raise ValueError('Invalid current week')
        fresh=copy.deepcopy(previous);fresh['days']=result;fresh['current_week_index']=week;fresh['revision']+=1;fresh['last_saved_at']=datetime.now(ZoneInfo('America/Detroit')).isoformat()
        p=paths(course,root);lessonlist=catalog(course,root)
        resources=resource_links(course,root,fresh)
        student=agenda(course,fresh,lessonlist,False,resources);teacher=agenda(course,fresh,lessonlist,True,resources)
        atomic(p['state'],json.dumps(fresh,indent=2,ensure_ascii=False)+'\n')
        atomic(p['student'],student);atomic(p['teacher'],teacher)
        return {'ok':True,'state':fresh,'resources':resources,'public_url':URLS[course]}
