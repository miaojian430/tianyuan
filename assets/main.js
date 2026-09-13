/* 天元官网全局脚本 */
(function(){
'use strict';
/* 导航滚动阴影 */
var nav=document.querySelector('.nav');
window.addEventListener('scroll',function(){
  if(nav) nav.classList.toggle('scrolled',window.scrollY>8);
},{passive:true});

/* 移动端抽屉 */
var drawer=document.querySelector('.drawer');
var mask=document.querySelector('.drawer-mask');
function openDrawer(){if(drawer){drawer.classList.add('open');if(mask)mask.classList.add('show');}}
function closeDrawer(){
  if(drawer){drawer.classList.remove('open');
    var subs=drawer.querySelectorAll('.sub-m');for(var i=0;i<subs.length;i++)subs[i].style.display='none';}
  if(mask)mask.classList.remove('show');
}
var hb=document.querySelector('.hamburger');if(hb)hb.addEventListener('click',openDrawer);
var dc=document.querySelector('.drawer-close');if(dc)dc.addEventListener('click',closeDrawer);
if(mask)mask.addEventListener('click',closeDrawer);
/* 抽屉内二级菜单 + 返回上级 */
var hasSubs=document.querySelectorAll('.drawer .has-sub>a');
for(var i=0;i<hasSubs.length;i++)(function(a){
  a.addEventListener('click',function(e){
    e.preventDefault();
    var m=a.parentNode.querySelector('.sub-m');
    if(m)m.style.display=(m.style.display==='none'||!m.style.display)?'block':'none';
  });
})(hasSubs[i]);
var back=document.querySelector('.drawer-back');
if(back)back.addEventListener('click',function(){
  var subs=document.querySelectorAll('.drawer .sub-m');
  for(var j=0;j<subs.length;j++)subs[j].style.display='none';
});

/* 产品筛选 */
var fbtns=document.querySelectorAll('.fbtn');
for(var k=0;k<fbtns.length;k++)(function(btn){
  btn.addEventListener('click',function(){
    for(var m=0;m<fbtns.length;m++)fbtns[m].classList.remove('on');
    btn.classList.add('on');
    var cat=btn.getAttribute('data-f');
    var cards=document.querySelectorAll('[data-cat]');
    for(var n=0;n<cards.length;n++){
      cards[n].style.display=(cat==='all'||cards[n].getAttribute('data-cat')===cat)?'':'none';
    }
  });
})(fbtns[k]);

/* FAQ 折叠 */
var faqQs=document.querySelectorAll('.faq-q');
for(var f=0;f<faqQs.length;f++)(function(q){
  q.addEventListener('click',function(){q.parentNode.classList.toggle('open');});
})(faqQs[f]);

/* 联系表单校验 */
var form=document.getElementById('contact-form');
if(form){
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var ok=true;
    var name=document.getElementById('f-name'), phone=document.getElementById('f-phone');
    function mark(input,bad){var row=input.closest('.row');if(row)row.classList.toggle('bad',bad);}
    mark(name,!name.value.trim()); if(!name.value.trim())ok=false;
    var pv=phone.value.trim();
    var phoneOk=/^1[3-9]\d{9}$/.test(pv)||/^(0\d{2,3}-?)?\d{7,8}$/.test(pv);
    mark(phone,!phoneOk); if(!phoneOk)ok=false;
    if(ok){form.style.display='none';
      var done=document.getElementById('form-ok');if(done)done.style.display='block';}
  });
}

/* Cookie 提示（偏好记录于本地，不做服务端记录） */
var cookieBar=document.getElementById('cookie-bar');
try{
  if(cookieBar&&!localStorage.getItem('ty-cookie-consent'))cookieBar.classList.add('show');
}catch(err){}
var cbtn=document.getElementById('cookie-accept');
if(cbtn)cbtn.addEventListener('click',function(){
  try{localStorage.setItem('ty-cookie-consent','essential');}catch(err){}
  cookieBar.classList.remove('show');
});

/* 页脚年份 */
var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();

/* 搜索页逻辑 */
var searchForm=document.getElementById('search-form');
if(searchForm&&window.TY_SEARCH_INDEX){
  var input=document.getElementById('search-input');
  var results=document.getElementById('search-results');
  var historyBox=document.getElementById('search-history');
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  function hi(text,kw){
    if(!kw)return esc(text);
    try{return esc(text).replace(new RegExp(kw.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi'),function(m){return '<mark>'+m+'</mark>';});}
    catch(err){return esc(text);}
  }
  function renderHistory(){
    if(!historyBox)return;
    var h=[];try{h=JSON.parse(localStorage.getItem('ty-search-history')||'[]');}catch(err){}
    if(!h.length){historyBox.style.display='none';return;}
    historyBox.style.display='flex';
    var html='<span>最近搜索：</span>';
    for(var i=0;i<h.length;i++)html+='<span class="tag" data-h="'+esc(h[i])+'">'+esc(h[i])+'</span>';
    html+='<span class="tag" id="clear-history" style="cursor:pointer;border-color:var(--surface-d20);color:var(--mute)">清除记录</span>';
    historyBox.innerHTML=html;
    var tags=historyBox.querySelectorAll('[data-h]');
    for(var t=0;t<tags.length;t++)(function(el){
      el.addEventListener('click',function(){input.value=el.getAttribute('data-h');doSearch();});
    })(tags[t]);
    var ch=document.getElementById('clear-history');
    if(ch)ch.addEventListener('click',function(){
      try{localStorage.removeItem('ty-search-history');}catch(err){}
      renderHistory();
    });
  }
  function saveHistory(kw){
    try{
      var h=JSON.parse(localStorage.getItem('ty-search-history')||'[]');
      h=h.filter(function(x){return x!==kw;});h.unshift(kw);h=h.slice(0,10);
      localStorage.setItem('ty-search-history',JSON.stringify(h));
    }catch(err){}
  }
  function doSearch(){
    var kw=(input.value||'').trim();
    if(kw)saveHistory(kw);
    renderHistory();
    var html='';
    if(!kw){
      html='<div class="empty-state"><b>请输入关键词</b><p>支持按标题、摘要、标签检索全站内容</p></div>';
    }else{
      var hits=[];
      for(var i=0;i<window.TY_SEARCH_INDEX.length;i++){
        var it=window.TY_SEARCH_INDEX[i];
        if((it.title+it.desc+it.tags).toLowerCase().indexOf(kw.toLowerCase())>-1)hits.push(it);
      }
      if(hits.length){
        for(var j=0;j<hits.length;j++){
          var r=hits[j];
          html+='<div class="sr"><h3><a href="'+r.url+'">'+hi(r.title,kw)+'</a></h3>'
            +'<div class="from">'+r.type+' · '+esc(r.from)+'</div>'
            +'<p>'+hi(r.desc,kw)+'</p></div>';
        }
        html='<p style="font-size:13px;color:var(--mute);margin-bottom:8px">共找到 '+hits.length+' 条结果</p>'+html;
      }else{
        html='<div class="empty-state"><b>未找到与“'+esc(kw)+'”相关的内容</b>'
          +'<p>试试这些热门内容：</p></div>'
          +hotList();
      }
    }
    results.innerHTML=html;
  }
  function hotList(){
    var hot=[['产品与能力','products.html'],['行业解决方案','solutions.html#intel'],
      ['智慧边防应用','solutions.html#border'],['联系我们','contact.html']];
    var s='';
    for(var i=0;i<hot.length;i++)s+='<p style="margin:4px 0"><a href="'+hot[i][1]+'">'+hot[i][0]+' →</a></p>';
    return s+'</div>';
  }
  searchForm.addEventListener('submit',function(e){e.preventDefault();doSearch();});
  renderHistory();
  doSearch();
}
})();
