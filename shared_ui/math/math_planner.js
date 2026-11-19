(() => {
  'use strict';
  const CUSTOM = '__custom__';
  const CLOSED = new Set(['Break','P.D.','No School','Snow Day','Holiday']);
  const DAY_TYPES=['Regular Day','Break','P.D.','Half Day','1/2 Day','No School','Snow Day','Holiday',
    'Assembly Schedule','Testing','Sub Assignment','Early Release'];
  const OTHER = '__other_day__';
  const dayTypeLabel = control => control==='1/2 Day'?'Half Day':control;
  const STUDENT_URL = 'https://tnezki.github.io/algebra/agenda/index.html';
  const GITHUB_SYNC_URL = 'http://127.0.0.1:8771/';
  let root=null, data=null, lessons=[], lookup=new Map(), activeSlug='', epoch=0;
  const escapeHTML = s => String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const goodURL = v => {
    const s=String(v||'').trim();
    if(!s)return '';
    if(/^\/(?!\/)/.test(s))return s;
    if(/^https?:\/\/[^\s/?#@]+/i.test(s))return s;
    return '';
  };
  const dayParts = day => {
    const choice=day.lesson_choice||'';
    const lesson=lookup.get(choice);
    const custom=choice===CUSTOM?(day.lesson_custom||{}):null;
    if(CLOSED.has(day.control))return {title:dayTypeLabel(day.control),choice,
      row3:{label:'',url:''},teacher:'',closed:true,
      extras:Array.from({length:4},()=>({label:'',url:''}))};
    const lessonTitle=custom ? (custom.short_name||custom.label||'') : lesson ? lesson.short_name : (day.title||'');
    const special=day.control&&day.control!=='Regular Day'?dayTypeLabel(day.control):'';
    const title=special?(special+(lessonTitle?' · '+lessonTitle:'')):lessonTitle;
    const row3=custom?{label:custom.label||'',url:custom.url||''}:lesson?{label:lesson.agenda_label||lesson.label,url:lesson.student_url}:{label:'',url:''};
    return {title,choice,row3:(!custom&&!lesson?(day.row3||row3):row3),teacher:custom?.teacher_url||lesson?.teacher_url||day.teacher_url||'',extras:day.extra_rows||Array.from({length:4},()=>({label:'',url:''}))};
  };
  function status(message,level='info'){
    if(!root)return;
    const e=root.querySelector('#scp-status');if(!e)return;
    e.textContent=message;e.dataset.level=level;e.hidden=!message;
  }
  function weeks(){
    const map=new Map();
    for(let i=0;i<data.state.days.length;i++){
      const day=data.state.days[i],wk=Number(day.week_index);
      if(!map.has(wk))map.set(wk,[]);
      map.get(wk).push({day,index:i});
    }
    return map;
  }
  function anchor(item){
    const label=String(item?.label||'').trim(),url=goodURL(item?.url||'');
    if(!label)return '<span class="scp-empty-cell">&nbsp;</span>';
    return url?`<a class="scp-cell-link" href="${escapeHTML(url)}" target="_blank" rel="noopener" title="${escapeHTML(label)}">${escapeHTML(label)}</a>`:`<span class="scp-cell-text" title="${escapeHTML(label)}">${escapeHTML(label)}</span>`;
  }
  function weekTable(which,edit,showTeacher=edit){
    const days=weeks().get(which)||[];
    if(!days.length)return '<div class="scp-shell-empty">No dates are available for this week.</div>';
    const style=which===data.state.current_week_index?'scp-current-week':'scp-other-week';
    let h='<div class="scp-table-scroller '+style+'"><table aria-label="'+(edit?'Teacher Planner':'Student weekly preview')+'"><tbody><tr>';
    for(const {day,index} of days){
      const label=dayTypeLabel(day.control||'Regular Day');
      const marker=day.control&&day.control!=='Regular Day'?`<span class="scp-day-marker">${escapeHTML(label)}</span>`:'';
      const others=day.control?.startsWith('Other: ');
      const choice=others?OTHER:day.control||'Regular Day';
      const selection=DAY_TYPES.map(item=>`<option value="${escapeHTML(item)}"${choice===item?' selected':''}>${escapeHTML(dayTypeLabel(item))}</option>`).join('');
      const selector=edit?`<select class="scp-control" data-index="${index}" aria-label="Day type for ${escapeHTML(day.date)}">${selection}<option value="${OTHER}"${others?' selected':''}>Other…</option></select>`:'';
      h+=`<th class="${marker?'scp-special-day':''}">${escapeHTML(day.dow)}<small>${escapeHTML(day.display_date)}</small>${marker}${selector}</th>`;
    }
    h+='</tr>';
    const views=days.map(({day})=>dayParts(day));
    h+='<tr class="scp-row-title">';
    for(const view of views)h+=`<td>${anchor({label:view.title,url:''})}</td>`;
    h+='</tr><tr class="scp-row-lesson">';
    for(let j=0;j<days.length;j++){
      const {day,index}=days[j],v=views[j];
      if(!edit)h+=`<td class="scp-lesson-cell">${anchor(v.row3)}</td>`;
      else{
        if(v.closed){h+=`<td class="scp-lesson-cell"><span class="scp-closed-placeholder">No lessons scheduled</span></td>`;continue}
        const customName=String(day.lesson_custom?.label||'').trim();
        const customOption=customName?'Custom: '+customName:'Custom…';
        const opts=[`<option value="${CUSTOM}"${v.choice===CUSTOM?' selected':''}>${escapeHTML(customOption)}</option>`];
        for(const l of lessons)opts.push(`<option value="${escapeHTML(l.id)}"${v.choice===l.id?' selected':''}>${escapeHTML(l.agenda_label||l.label)}</option>`);
        opts.push(`<option value=""${!v.choice?' selected':''}>— Blank —</option>`);
        const open=v.row3.url?`<a class="scp-cell-open" href="${escapeHTML(v.row3.url)}" target="_blank" rel="noopener" title="Open student PDF">↗</a>`:'<span class="scp-cell-open" aria-hidden="true"></span>';
        h+=`<td class="scp-lesson-cell"><div class="scp-edit-cell"><select class="scp-choice" data-index="${index}" aria-label="Lesson on ${escapeHTML(day.date)}">${opts.join('')}</select>${open}${v.choice===CUSTOM?`<button class="scp-custom-edit" data-index="${index}" type="button" title="Edit custom lesson">Edit</button>`:''}</div></td>`;
      }
    }
    h+='</tr>';
    for(let row=0;row<4;row++){
      h+='<tr>';
      for(let j=0;j<days.length;j++){
        const {day,index}=days[j],item=views[j].extras[row]||{label:'',url:''};
        if(!edit)h+=`<td>${anchor(item)}</td>`;
        else h+=`<td><div class="scp-edit-cell"><button class="scp-optional-edit" type="button" data-index="${index}" data-row="${row}" title="Edit optional row ${row+4} for ${escapeHTML(day.date)}">${item.label?escapeHTML(item.label):'&nbsp;'}</button>${item.url?`<a class="scp-cell-open" href="${escapeHTML(item.url)}" target="_blank" rel="noopener" title="Open optional link">↗</a>`:''}</div></td>`;
      }
      h+='</tr>';
    }
    if(showTeacher){
      h+='<tr>';
      for(const v of views)h+=`<td class="scp-teacher-cell">${anchor({label:v.teacher?'Teacher Guide':'',url:v.teacher})}</td>`;
      h+='</tr>';
    }
    return h+'</tbody></table></div>';
  }
  // Reconcile legacy row-3 PDF URLs with the new lesson selector, without
  // rewriting the local calendar during GET or changing valid existing URLs.
  // Older calendars stored the PDF in row3 but had no lesson_choice, so the
  // student preview could link correctly while the editor read "— Blank —".
  function lessonLinkKey(url){
    const value=String(url||'').trim();
    const file=value.match(/^https?:\/\/drive\.google\.com\/file\/d\/([A-Za-z0-9_-]+)/i);
    return file?'google-drive-file:'+file[1]:value.replace(/\?.*$/,'').replace(/#.*$/,'');
  }
  function restoreLinkedLessonSelections(){
    if(!data?.state?.days || !Array.isArray(lessons))return;
    const byLink=new Map();
    for(const lesson of lessons){
      if(lesson.student_url)byLink.set(lessonLinkKey(lesson.student_url),lesson);
    }
    for(const day of data.state.days){
      // Never change lessons explicitly chosen by the teacher; never fill a
      // future day. The blank-choice problem only involves saved legacy links.
      if(day.lesson_choice || !day.row3?.url)continue;
      const url=goodURL(day.row3.url);
      if(!url)continue;
      const found=byLink.get(lessonLinkKey(url));
      if(found){
        day.lesson_choice=found.id;
      }else{
        const label=String(day.row3.label||day.title||'Linked Lesson').trim().slice(0,160);
        day.lesson_choice=CUSTOM;
        day.lesson_custom={
          label:label||'Linked Lesson',
          short_name:String(day.title||label||'Linked Lesson').trim().slice(0,160),
          url,
          teacher_url:goodURL(day.teacher_url||'')
        };
      }
    }
  }
  function resourcePanel(){
    const links=data?.resources||{};
    const group=(label,items,teacher=false)=>{
      if(!Array.isArray(items)||!items.length)return '';
      return `<div class="scp-resource-group${teacher?' scp-teacher-resources':''}">
        <h3>${escapeHTML(label)}</h3><nav aria-label="${escapeHTML(label)}">${items.map(({label,url})=>
          `<a href="${escapeHTML(url)}" target="_blank" rel="noopener">${escapeHTML(label)}</a>`).join('')}</nav>
        </div>`;
    };
    return `<section class="scp-resource-panel" aria-label="Course links">
       ${group('Resources',links.student)}${group('Teacher Resources',links.teacher,true)}
       </section>`;
  }
  function showSyncReminder(){
    const overlay=root?.querySelector('#scp-sync-overlay');
    if(!overlay)return;
    overlay.hidden=false;
    overlay.querySelector('#scp-sync-dismiss')?.focus();
  }
  function hideSyncReminder(){
    const overlay=root?.querySelector('#scp-sync-overlay');
    if(!overlay)return;
    overlay.hidden=true;
    root?.querySelector('#scp-save')?.focus();
  }
  function render(preserveScroll=true){
    if(!root||!data)return;
    const priorScroll=preserveScroll&&typeof window.scrollY==='number'?window.scrollY:null;
    const state=data.state, weekList=[...weeks().entries()].sort((a,b)=>a[0]-b[0]);
    const weekHTML=weekList.map(([weekId,days])=>{
      const selected=weekId===state.current_week_index;
      const heading=escapeHTML(days[0].day.display_date);
      // Restore the older Algebra/AP Calculus Planner's red current-week rail.
      // This is the week-selector and a persistent visual reminder, not a new
      // top-toolbar action. Its checked state is also exposed to screen readers.
      const rail=`<div class="scp-current-rail"><button class="scp-current-picker" type="button"
          data-week="${weekId}" aria-pressed="${selected?'true':'false'}"
          aria-label="${selected?'Current week: ':'Set current week to '}${heading}"
          title="${selected?'This is the current week':'Make this the current week'}">
          <span class="scp-check-box" aria-hidden="true"><span class="scp-check-mark">✓</span></span>
          <span>${selected?'Current':'Set Current'}</span></button></div>`;
      return `<section class="scp-week-group${selected?' scp-week-group-current':''}" id="scp-week-${weekId}" aria-label="Week of ${heading}">
        <div class="scp-week-layout">${rail}<div class="scp-week-main">
          <div class="scp-week-heading"><h3>Week of ${heading}${selected?' · CURRENT WEEK':''}</h3></div>
          ${weekTable(weekId,true)}
        </div></div></section>`;
    }).join('');
    root.innerHTML=`<div class="scp-toolbar" aria-label="Planner controls">
      <button type="button" class="scp-action scp-save" id="scp-save">Save + Update Student Agenda</button>
      <button type="button" class="scp-action" id="scp-jump">Current Week</button>
      <a class="scp-action" href="${escapeHTML(data.public_url||STUDENT_URL)}" target="_blank" rel="noopener">Student Page ↗</a>
      <a class="scp-action scp-sync-action" href="${GITHUB_SYNC_URL}" target="_blank" rel="noopener">GitHub Sync ↗</a>
      </div>
      ${resourcePanel()}
      <p class="scp-url">Student page after GitHub Desktop publishes: <code>${escapeHTML(data.public_url||STUDENT_URL)}</code></p>
      <div class="scp-status" id="scp-status" role="status" hidden></div>
      <h2 id="scp-overview">Current Week · Teacher Overview</h2>
      <p class="scp-helper">Quick view of this week's lessons and linked teacher guides. The editable version appears again in the full-year calendar.</p>
      <div class="scp-teacher-overview">${weekTable(state.current_week_index,false,true)}</div>
      <h2 id="scp-editor-title">Planner Editor · Entire School Year</h2>
      <p class="scp-helper">Every week stays open for planning. The current week is mustard; all other weeks are gray. Day-type menus label Breaks, P.D., Half Days, and other schedules. Row 3 selects a student PDF; rows 4–7 are optional; the last row shows the teacher guide.</p>
      <div class="scp-week-list">${weekHTML}</div>
      <button class="scp-return-top" id="scp-return-top" type="button" title="Back to top of Planner">↑ Top</button>
      <p class="scp-catalog-meta">${lessons.length} registered lesson PDFs · ${state.days.length} calendar dates · Local-only teacher editing · No automatic GitHub activity</p>
      <div class="scp-sync-overlay" id="scp-sync-overlay" hidden>
        <div class="scp-sync-dialog" role="alertdialog" aria-modal="true"
             aria-labelledby="scp-sync-title" aria-describedby="scp-sync-description">
          <div class="scp-sync-title" id="scp-sync-title">Saved locally — GitHub Sync needed</div>
          <p id="scp-sync-description">The student agenda was updated on this computer, but students will not see it until you sync and publish the changes.</p>
          <p>Use the separate <strong>GitHub Sync</strong> button when you are ready. Saving does not open that app or publish anything automatically.</p>
          <button type="button" id="scp-sync-dismiss" class="scp-sync-dismiss">OK — I’ll sync manually</button>
        </div>
      </div>`;
    root.querySelector('#scp-save').addEventListener('click',save);
    root.querySelector('#scp-sync-dismiss').addEventListener('click',hideSyncReminder);
    root.querySelector('#scp-sync-overlay').addEventListener('keydown',ev=>{if(ev.key==='Escape'){ev.preventDefault();hideSyncReminder()}});
    root.querySelector('#scp-return-top').addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
    root.querySelector('#scp-jump').addEventListener('click',()=>{
      root?.querySelector('#scp-week-'+state.current_week_index)?.scrollIntoView({behavior:'instant',block:'start'});
    });
    root.querySelectorAll('button.scp-current-picker').forEach(el=>el.addEventListener('click',ev=>{
      state.current_week_index=Number(ev.currentTarget.dataset.week);
      render(true);
      status('Current week selected. Save to update the student page.','info');
    }));
    root.querySelectorAll('select.scp-control').forEach(el=>el.addEventListener('change',changeDayType));
    root.querySelectorAll('select.scp-choice').forEach(el=>el.addEventListener('change',choose));
    root.querySelectorAll('button.scp-custom-edit').forEach(el=>el.addEventListener('click',ev=>editCustom(Number(ev.currentTarget.dataset.index),true)));
    root.querySelectorAll('button.scp-optional-edit').forEach(el=>el.addEventListener('click',editOptional));
    if(priorScroll!==null&&typeof window.scrollTo==='function')window.scrollTo(0,priorScroll);
  }
  function changeDayType(ev){
    const idx=Number(ev.target.dataset.index),day=data.state.days[idx],next=ev.target.value;
    if(next===OTHER){
      const old=day.control?.startsWith('Other: ')?day.control.slice(7):'';
      const supplied=window.prompt('Special day label (for example, Field Trip):',old);
      if(supplied===null){render();return}
      const label=supplied.trim();
      if(!label||label.length>65){render();status('Please enter a day label of 1–65 characters.','bad');return}
      day.control='Other: '+label;
    }else day.control=next;
    render();status('School-day type updated. Save to publish the updated student page.','info');
  }
  function choose(ev){
    const idx=Number(ev.target.dataset.index),day=data.state.days[idx],choice=ev.target.value;
    if(choice===CUSTOM){
      if(!editCustom(idx,false)){render();return}
    }else{day.lesson_choice=choice;day.lesson_custom={};day.row3={label:'',url:''};if(choice)day.title=''}
    render();status('Lesson selected. Save to publish the updated student page.','info');
  }
  function editCustom(idx,editing){
    const day=data.state.days[idx],old=day.lesson_custom||{};
    let label=window.prompt('Custom lesson label:',old.label||'');if(label===null)return false;
    label=label.trim();if(!label){status('A custom lesson needs a label.','bad');return false}
    let url=window.prompt('Student link (blank for no link):',old.url||'');if(url===null)return false;
    if(url.trim()&&!goodURL(url)){status('Please enter an http(s) URL or local link.','bad');return false}
    let short=window.prompt('Short name for row 2:',old.short_name||label);if(short===null)return false;
    let teacher=window.prompt('Teacher guide PDF link (blank if none):',old.teacher_url||'');if(teacher===null)return false;
    if(teacher.trim()&&!goodURL(teacher)){status('Teacher guide requires a valid URL.','bad');return false}
    day.lesson_choice=CUSTOM;day.lesson_custom={label,short_name:short.trim()||label,url:goodURL(url),teacher_url:goodURL(teacher)};
    if(editing){render();status('Custom lesson updated. Save when ready.','info')}
    return true;
  }
  function editOptional(ev){
    const idx=Number(ev.currentTarget.dataset.index),row=Number(ev.currentTarget.dataset.row);
    const day=data.state.days[idx];const old=day.extra_rows?.[row]||{label:'',url:''};
    const label=window.prompt(`Row ${row+4}: text (blank to clear):`,old.label||'');if(label===null)return;
    let url='';
    if(label.trim()){
      const raw=window.prompt('Link (optional):',old.url||'');if(raw===null)return;
      url=goodURL(raw);if(raw.trim()&&!url){status('Invalid link: use http(s) or a local application path.','bad');return}
    }
    day.extra_rows[row]={label:label.trim(),url};render();status('Optional row updated. Save when ready.','info');
  }
  async function save(){
    if(!data||!root)return;
    const button=root.querySelector('#scp-save');button.disabled=true;
    status('Saving the Planner and refreshing the student agenda…','info');
    const changes=data.state.days.map(d=>({date:d.date,control:d.control||'Regular Day',title:d.title||'',row3:d.row3||{label:'',url:''},lesson_choice:d.lesson_choice||'',lesson_custom:d.lesson_custom||{},extra_rows:d.extra_rows,teacher_url:d.teacher_url||'',teacher_label:d.teacher_label||''}));
    try{
      const resp=await fetch('/api/math-planner/'+encodeURIComponent(activeSlug)+'/publish',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({revision:data.state.revision,current_week_index:data.state.current_week_index,days:changes})});
      const payload=await resp.json();if(!resp.ok||!payload.ok)throw new Error(payload.error||`HTTP ${resp.status}`);
      data.state=payload.state;data.resources=payload.resources||data.resources;render();
      status('Saved locally. GitHub Sync is needed to publish the updated student agenda.','good');
      showSyncReminder();
    }catch(e){button.disabled=false;status(`Save failed: ${e.message}`,'bad')}

  }
  async function mount(el,course){
    epoch++;const localEpoch=epoch;
    root=el;data=null;activeSlug=course.id;
    root.innerHTML='<div class="scp-shell-empty" role="status">Loading '+escapeHTML(course.title||course.name||'Math')+' Planner…</div>';
    try{
      const resp=await fetch('/api/math-planner/'+encodeURIComponent(course.id),{cache:'no-store'});
      const payload=await resp.json();if(!resp.ok||!payload.ok)throw new Error(payload.error||`HTTP ${resp.status}`);
      if(localEpoch!==epoch||root!==el)return;
      if(payload.available===false){el.innerHTML='<div class="scp-shell-empty">'+escapeHTML(payload.message||'No course calendar is loaded yet.')+'</div>';return}
      data=payload;lessons=payload.lessons||[];lookup=new Map(lessons.map(x=>[x.id,x]));
      restoreLinkedLessonSelections();
      render(false);status('Math Planner loaded. Your calendar and course links are ready. Saving updates the student agenda locally; GitHub Sync is always manual.','good');
    }catch(e){if(localEpoch===epoch&&root===el)el.innerHTML='<div class="scp-shell-empty" role="alert">Planner could not load: '+escapeHTML(e.message)+'. Restart CPM Tools if it was just updated.</div>'}
  }
  function deactivate(){epoch++;root=null;data=null;lessons=[];lookup=new Map();activeSlug=''}
  window.MAPSMathPlanner={mount,deactivate};
})();
