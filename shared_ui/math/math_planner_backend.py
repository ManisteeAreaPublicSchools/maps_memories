"""MAPS shared local Math Planner for Algebra 1 and AP Calculus in CPM Tools."""
from __future__ import annotations
import json,html,os,threading,copy
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
from course_artifact_naming import validate_artifact_name

LOCK=threading.RLock()
SCHEMA='maps-math-planner/1'
CUTOFF='2026-11-19'
CLOSED={'Break','P.D.','No School','Snow Day','Holiday'}
URLS={'algebra1':'https://tnezki.github.io/algebra/agenda/index.html','apcalc':'https://tnezki.github.io/apcalc/agenda/index.html'}
NAMES={'algebra1':'Algebra 1','apcalc':'AP Calculus AB'}

def paths(course,root):
    if course not in URLS: raise ValueError('Unknown course')
    return {'state':root/'CPM_Tools_Library/planner'/f'{course}.json','legacy':root/'_algebra_teacher_tools/planner/planner_state.json' if course=='algebra1' else None,'calendar':root/'CPM_Tools/planner/calendar_2026_2027.json','catalog':root/'CPM_Tools/planner'/('algebra1_lesson_catalog.json' if course=='algebra1' else 'apcalc_lesson_catalog.json'),'student':root/('algebra' if course=='algebra1' else 'apcalc')/'agenda/index.html','teacher':root/'teacher_shared'/('algebra' if course=='algebra1' else 'calc')/'planner/index.html'}

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
    return data

def repair_legacy_html_links():
    """One-time correction for renamed 3.1.1 PDF companions in synced Drive folder.
    Does not rename/move Drive files or affect the public agenda.
    """
    home=Path.home();bases=[];cloud=home/'Library/CloudStorage'
    if cloud.is_dir():
        for provider in cloud.glob('GoogleDrive-*'):bases.extend([provider/'My Drive',provider/'MyDrive'])
    bases.extend([home/'Google Drive/My Drive',home/'Google Drive/MyDrive'])
    relative=Path('~Curriculum/__MAPS_Courses/Algebra 1/ch_03/lesson_3_1_1')
    pairs=(('Alg1_3.1.1_Lesson_Student.html','Algebra1_Lesson_3.1.1_Student_Notability.pdf','Alg1_3.1.1_Lesson_Student.pdf'),('Alg1_3.1.1_Lesson_Teacher.html','Algebra1_Lesson_3.1.1_Teacher_Guide.pdf','Alg1_3.1.1_Lesson_Teacher.pdf'))
    for base in bases:
        folder=base/relative
        if not folder.is_dir():continue
        for filename,old,new in pairs:
            f=folder/filename
            if f.is_file():
                contents=f.read_text(encoding='utf-8')
                if old in contents:
                    # In-place update keeps existing relative path; avoid creating renamed copies.
                    f.write_text(contents.replace(old,new),encoding='utf-8')
        return

def get_payload(course,root):
    if course=='algebra1':repair_legacy_html_links()
    return {'ok':True,'state':load(course,root),'lessons':catalog(course,root),'course_title':NAMES[course],'public_url':URLS[course]}

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

CSS='''*{box-sizing:border-box}body{background:#f4f6fa;color:#17314c;font:15px/1.4 Arial,sans-serif;margin:0}main{width:min(1500px,calc(100% - 28px));margin:22px auto}h1{background:#173f6d;color:#fff;padding:17px;border-radius:10px;font-size:24px}h2{color:#173f6d}.caption{color:#65748a}.scroller{overflow-x:auto;border:1px solid #cbd2d9;border-radius:7px}table{table-layout:fixed;border-collapse:collapse;min-width:850px;width:100%}th,td{width:20%;text-align:center;border-right:1px solid #cbd2d9;border-bottom:1px solid #cbd2d9}th{text-align:left;background:#e2bc4f;padding:10px 8px;color:#173f6d}th small{margin-left:6px}td{height:40px;background:#fff9e8}tr:nth-child(odd):not(:first-child) td{background:#fff0c7}td a,td span{display:block;height:40px;line-height:40px;padding:0 8px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;color:#173f6d;font-weight:750}a:hover{text-decoration:underline}.week:not(.current) th{background:#434b55;color:white;border-top:5px solid #222}.week:not(.current) td{background:#fff}.week:not(.current) tr:nth-child(odd):not(:first-child) td{background:#f3f4f6}.week{margin:13px 0}.week h3{font-size:14px;margin:6px 0;color:#374151}.current{margin:10px 0 20px}.all{background:#173f6d;color:#fff;font-weight:850;padding:12px;text-align:center;margin:24px 0 12px}.special{display:block;font-size:11px;background:#fff7e2;color:#694c17;padding:3px;margin-top:3px}@media print{.scroller{overflow:visible}main{width:100%}.week{break-inside:avoid}table{min-width:0}}'''

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

def agenda(course,state,lessons,teacher=False):
    byweek={};idx={d['id']:d for d in lessons}
    for d in state['days']:byweek.setdefault(d['week_index'],[]).append(d)
    current=state['current_week_index'];title=NAMES[course]+(' Teacher Agenda' if teacher else ' Student Agenda')
    p=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+'</style></head><body><main><h1>'+html.escape(title)+'</h1><p class="caption">2026–27 school year · Updated locally by the Math Planner · Published manually with GitHub Desktop.</p><h2>Current Week</h2><div class="current">',table(byweek[current],idx,teacher),'</div><div class="all">ALL WEEKS</div>']
    for n,ds in sorted(byweek.items()):
        p.extend(['<section class="week'+(' current' if n==current else '')+'"><h3>Week of '+html.escape(ds[0]['display_date'])+(' · CURRENT WEEK' if n==current else '')+'</h3>',table(ds,idx,teacher),'</section>'])
    return ''.join(p)+'</main></body></html>'

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
        student=agenda(course,fresh,lessonlist,False);teacher=agenda(course,fresh,lessonlist,True)
        atomic(p['state'],json.dumps(fresh,indent=2,ensure_ascii=False)+'\n')
        atomic(p['student'],student);atomic(p['teacher'],teacher)
        return {'ok':True,'state':fresh,'public_url':URLS[course]}
