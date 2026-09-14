# -*- coding: utf-8 -*-
"""客户案例模块（依据《客户案例模块 PRD》重构，2026-09-14）
- cases.html：案例列表页（3 列卡片，≤960px 2 列 / ≤640px 1 列），点击卡片弹出详情弹窗；
  首个案例为“智慧边防”，另含“更多行业案例即将上线”占位卡
- 弹窗：遮罩半透明 + 背景模糊，面板 max-width 880px / 圆角 18px / 从底部滑入，
  ✕ / 遮罩 / ESC 三种关闭方式，内容按模块顺序：封面 / 客户原声 / 面临挑战 /
  四大核心能力 / 两大关键突破 / 底部 CTA
- case-detail.html：智慧边防独立详情页（军绿主题），无 JS 兜底与“标杆案例”导航目标
- 列表页配色与主平台一致（#0F3D75 / #00A0E9 系）；详情页（弹窗 + 独立页）以军绿为主色
- 案例数据集中在 CASES 列表，新增案例在此追加即可
"""
import io, sys, json
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ================= 案例数据（配置化） =================
CASES = [
{
 "id":"smart-border",
 "media":{"type":"placeholder","note":"边防场景视频 / 图片占位"},
 "badge":"实战案例",
 "tags":["智慧边防"],
 "title":"智慧边防，从“看得见”到“看得准”",
 "desc":"构建防控态势一图展示、同屏联动一图预警、全域态势一图指挥、技防量化一图规划四大核心能力，"
        "实现 AI 赋能存量设备与新型装备智能调度两大关键突破，误报降低 80%，有效报警率 95% 以上。",
 "stats":[{"v":"400m","l":"白天发现距离"},{"v":"↓80%","l":"误报降低"},{"v":"95%+","l":"有效报警率"}],
 "detail":{
   "subtitle":"天元平台赋能边境管控智能化实践",
   "coverTags":["#智慧边防","#AI预警","#无人装备协同","#无电无网覆盖"],
   "quote":"报警响了，却看不清是人是兽是风。",
   "quoteBy":"—— 某边防团执勤人员",
   "challenges":[
     ["看不远","老旧枪机白天仅能识别 100–200 米，夜间几乎失效"],
     ["辨不准","移动旗帜、树枝等频繁误报，有效报警率低"],
     ["覆盖难","无电无网区域存在感知盲区，数据回传困难"],
     ["协同弱","装备各自为战，缺乏统一调度与联动"]],
   "arch4":{"img":None,"h":300,"label":"四大核心能力架构图"},
   "capabilities":[
     ["防控态势一图展示","人防、物防、技防力量一张图汇聚，设备一键巡检"],
     ["同屏联动一图预警","智能预警 + 持续定位 + 轨迹回溯，推送一线护边员"],
     ["全域态势一图指挥","智能情报助手，问答式查询，辅助生成分析报告"],
     ["技防量化一图规划","GIS + 遥感三维建模，可视化评估覆盖盲区与补点效能"]],
   "arch2":{"img":None,"h":260,"label":"两大关键突破架构图"},
   "breakthroughs":[
     {"title":"突破一 · AI 赋能存量设备",
      "desc":"老旧枪机不变焦条件下，白天发现距离由 100–200 米提升至 400 米，"
             "夜间无辅助照明条件下提升至 200 米。",
      "stats":["400m","200m","↓80%"]},
     {"title":"突破二 · 新型装备智能调度",
      "desc":"卫星链路补盲无电无网区域，机器狗联动抵近侦察，破解复杂地形管控难题。",
      "stats":["95%+","卫星链路补盲","机器狗联动侦察"]}],
   "cta":"目前已在新疆生产建设兵团开展应用实践"
 }
}
]

# 军绿调色板（详情页主色）：深 / 主 / 中 / 浅背景 / 边线 / 挑战橙
MIL = "#3E4A2B", "#5A6B3F", "#2F3B22", "#F1F3E6", "#C4CDA8", "#D9632C"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;")
            .replace(">","&gt;").replace('"',"&quot;"))

# ---------- 列表页卡片（主平台蓝） ----------
def list_card(c):
    stats = "".join('<div class="cs-stat"><b>%s</b><small>%s</small></div>'
                    % (esc(s["v"]), esc(s["l"])) for s in c["stats"])
    badge = ('<span class="cs-badge"><i class="dot"></i>%s</span>'
             % esc(c["badge"])) if c.get("badge") else ""
    tags = "".join('<span class="cs-tag">%s</span>' % esc(t) for t in c["tags"])
    return """
      <a class="cs-card rv" href="case-detail.html" data-case="%s">
        <div class="cs-cover">
          <div class="cs-cover-ph"><b>&#9654;</b><small>%s</small></div>%s
        </div>
        <div class="cs-pb">
          <div class="cs-tags">%s</div>
          <h3>%s</h3>
          <p>%s</p>
          <div class="cs-stats">%s</div>
          <span class="cs-go">查看详情 &#8594;</span>
        </div>
      </a>""" % (esc(c["id"]), esc(c["media"].get("note","")), badge, tags,
                 esc(c["title"]), esc(c["desc"]), stats)

cards_html = "".join(list_card(c) for c in CASES)

cso = """
<div class="banner pad"><div class="banner-in">
  <h1>客户案例</h1>
  <p class="lead">一站式全链路数字化信息服务平台 · 赋能行业智能化转型</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 客户案例</div></div>

<section class="sec">
  <div class="wrap">
    <div class="cs-grid">
      __CARDS__
      <div class="cs-card cs-more rv" aria-disabled="true">
        <div class="cs-cover cs-cover-more"><span class="cs-plus">+</span></div>
        <div class="cs-pb"><h3>更多行业案例即将上线</h3>
          <p>应急管理 · 自然资源 · 智慧农业 · 交通物流 · 城市治理……</p></div>
      </div>
    </div>
    <div class="note rv"><b>合规要求：</b>客户名称、影像与成果数据须经客户书面授权后方可公开展示；
      成果数据需注明对比基准（如“发现距离提升至 400m vs 原枪机 100–200m”）与数据来源。</div>
  </div>
</section>

<!-- ===== 案例详情弹窗（军绿主题，内容由 window.CASES 渲染） ===== -->
<div class="cmd" id="caseModal" aria-hidden="true">
  <div class="cmd-mask" data-close="1"></div>
  <div class="cmd-panel" role="dialog" aria-modal="true" aria-labelledby="cmTitle">
    <button class="cmd-x" type="button" data-close="1" aria-label="关闭案例详情">&#10005;</button>
    <div class="cmd-scroll" id="cmScroll"></div>
  </div>
</div>
""".replace("__CARDS__", cards_html)

CASES_CSS = """
<style>
/* ===== 案例列表卡片（与主平台配色一致） ===== */
.cs-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.cs-card{display:flex;flex-direction:column;background:#fff;border:1px solid #B4C7E7;
  border-radius:14px;overflow:hidden;text-decoration:none;color:inherit;
  box-shadow:0 2px 8px rgba(15,61,117,.06);transition:transform .2s,box-shadow .2s,border-color .2s}
.cs-card:hover{transform:translateY(-5px);box-shadow:0 16px 40px rgba(10,60,140,.12);
  border-color:#00A0E9}
.cs-cover{position:relative;height:170px;background:linear-gradient(135deg,#0C315E,#1B5A9E);overflow:hidden}
.cs-cover::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to top,rgba(9,37,70,.62),transparent 55%);pointer-events:none}
.cs-cover-ph{position:absolute;inset:0;display:flex;flex-direction:column;gap:8px;
  align-items:center;justify-content:center;color:rgba(255,255,255,.75)}
.cs-cover-ph b{display:flex;align-items:center;justify-content:center;width:44px;height:44px;
  border-radius:50%;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.35);
  font-size:16px}
.cs-cover-ph small{font-size:11.5px}
.cs-cover video,.cs-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cs-badge{position:absolute;top:10px;left:10px;z-index:2;display:inline-flex;align-items:center;gap:7px;
  background:rgba(15,61,117,.82);color:#fff;font-size:12px;font-weight:700;
  padding:4px 10px;border-radius:4px;backdrop-filter:blur(2px)}
.cs-badge .dot{width:7px;height:7px;border-radius:50%;background:#6FE3FF;
  animation:cs-pulse 2s infinite}
@keyframes cs-pulse{0%{box-shadow:0 0 0 0 rgba(111,227,255,.55)}
  70%{box-shadow:0 0 0 7px rgba(111,227,255,0)}100%{box-shadow:0 0 0 0 rgba(111,227,255,0)}}
.cs-pb{padding:16px 18px 18px;display:flex;flex-direction:column;flex:1}
.cs-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.cs-tag{background:#DCE9F5;color:#0F3D75;font-size:11px;font-weight:700;
  padding:2px 8px;border-radius:4px}
.cs-pb h3{font-size:17.5px;color:#0F3D75;margin:0 0 8px;line-height:1.5}
.cs-pb p{font-size:13px;color:#33414E;line-height:1.8;margin:0;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.cs-stats{display:flex;gap:18px;flex-wrap:wrap;margin:14px 0 12px;
  padding-top:12px;border-top:1px dashed #D6DEE9}
.cs-stat b{display:block;font-size:20px;font-weight:700;color:#0F3D75}
.cs-stat small{display:block;font-size:11.5px;color:#5C6670;margin-top:2px}
.cs-go{margin-top:auto;font-size:13px;font-weight:700;color:#00608C}
.cs-card:hover .cs-go{color:#00A0E9}
/* 占位卡 */
.cs-more{border-style:dashed;background:#FBFCFE;cursor:default}
.cs-more:hover{transform:none;box-shadow:0 2px 8px rgba(15,61,117,.06);border-color:#B4C7E7}
.cs-cover-more{background:#F0F5FB;display:flex;align-items:center;justify-content:center}
.cs-cover-more::after{display:none}
.cs-plus{display:flex;align-items:center;justify-content:center;width:52px;height:52px;
  border-radius:50%;background:#fff;border:1px dashed #9FB6CF;color:#0F3D75;
  font-size:26px;font-weight:400;line-height:1}
.cs-more .cs-pb h3{color:#5C6670}
.cs-more .cs-pb p{display:block;color:#8894A0}
/* ===== 案例详情弹窗（军绿主题） ===== */
.cmd{position:fixed;inset:0;z-index:1200;display:none}
.cmd.open{display:flex;align-items:center;justify-content:center;padding:22px}
.cmd-mask{position:absolute;inset:0;background:rgba(10,22,40,.55);
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.cmd-panel{position:relative;width:100%;max-width:880px;max-height:92vh;
  background:#F1F3E6;border-radius:18px;overflow:hidden;display:flex;flex-direction:column;
  transform:translateY(48px);opacity:0;transition:transform .35s ease,opacity .35s ease;
  box-shadow:0 24px 70px rgba(15,25,8,.35)}
.cmd.open .cmd-panel{transform:none;opacity:1}
.cmd-x{position:absolute;top:12px;right:12px;z-index:5;width:38px;height:38px;border-radius:50%;
  border:0;background:rgba(255,255,255,.16);color:#fff;font-size:15px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:background .2s}
.cmd-x:hover{background:rgba(255,255,255,.32)}
.cmd-scroll{overflow-y:auto;overscroll-behavior:contain}
/* 封面：军绿渐变 + 底部遮罩 */
.cm-cover{position:relative;min-height:280px;display:flex;flex-direction:column;
  justify-content:flex-end;padding:26px 30px;background:linear-gradient(135deg,#232D18,#3E4A2B 55%,#55663A)}
.cm-cover video,.cm-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cm-cover .cm-shade{position:absolute;inset:0;
  background:linear-gradient(to top,rgba(18,24,10,.88),rgba(18,24,10,.25) 60%,transparent)}
.cm-cover .cm-in{position:relative}
.cm-ctags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.cm-ctags span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);
  color:#EAF0DC;font-size:12px;padding:3px 10px;border-radius:4px}
.cm-cover h2{color:#fff;font-size:26px;line-height:1.45;margin:0 0 8px}
.cm-sub{color:#C9D6A8;font-size:14px;margin:0}
/* 正文（浅军绿底） */
.cm-body{padding:24px 30px 30px}
.cm-h{display:flex;align-items:center;gap:8px;margin:26px 0 14px;font-size:17px;
  color:#2F3B22;font-weight:700}
.cm-h:first-child{margin-top:0}
.cm-h::before{content:"";width:4px;height:18px;border-radius:2px;background:#5A6B3F}
/* 客户原声 */
.cm-quote{background:#fff;border-radius:10px;padding:16px 18px;border-left:4px solid #5A6B3F}
.cm-quote p{margin:0;font-size:15px;line-height:1.95;color:#2E3A20}
.cm-quote small{display:block;margin-top:8px;font-size:12.5px;color:#7C8894}
/* 挑战 2×2：橙色竖线 */
.cm-grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.cm-chal{background:#fff;border-radius:10px;padding:14px 16px;border-left:4px solid #D9632C}
.cm-chal b{display:block;font-size:14.5px;color:#2F3B22;margin-bottom:5px}
.cm-chal p{margin:0;font-size:13px;line-height:1.8;color:#5C6670}
/* 架构图占位：可替换为真实图片 */
.cm-arch{background:#F7F9EE;border:1.5px dashed #9DAA84;border-radius:10px;
  display:flex;flex-direction:column;gap:8px;align-items:center;justify-content:center;
  color:#7C8894;overflow:hidden}
.cm-arch img{width:100%;height:100%;object-fit:cover;border:0}
.cm-arch b{font-size:14px;color:#5A6B3F}
.cm-arch small{font-size:11.5px}
/* 能力列表 */
.cm-cap b{display:block;font-size:14.5px;color:#2F3B22;margin-bottom:5px}
.cm-cap p{margin:0;font-size:13px;line-height:1.8;color:#5C6670}
/* 突破卡：白底 + 军绿顶条 */
.cm-brk{background:#fff;border-radius:10px;overflow:hidden;border:1px solid #DDE2CB}
.cm-brk-h{background:#3E4A2B;color:#fff;font-size:14.5px;font-weight:700;padding:10px 16px}
.cm-brk-b{padding:14px 16px}
.cm-brk-b p{margin:0 0 12px;font-size:13px;line-height:1.85;color:#33414E}
.cm-brk-stats{display:flex;flex-wrap:wrap;gap:6px}
.cm-brk-stats span{font-size:11.5px;color:#3E4A2B;background:#EDF0E0;
  border:1px solid #C4CDA8;border-radius:4px;padding:2px 8px;font-weight:700}
/* 底部 CTA：深军绿 */
.cm-cta{margin-top:26px;background:#2F3B22;border-radius:12px;padding:20px 24px;
  display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.cm-cta p{margin:0;color:#EAF0DC;font-size:14px;line-height:1.8}
.cm-cta .btn-wt{display:inline-block;background:#fff;color:#2F3B22;font-size:14px;font-weight:700;
  padding:11px 22px;border-radius:6px;text-decoration:none;white-space:nowrap;transition:background .2s}
.cm-cta .btn-wt:hover{background:#DDE8C4}
/* 响应式 */
@media(max-width:960px){.cs-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.cm-grid2{grid-template-columns:1fr}
  .cm-cover{min-height:240px;padding:20px}
  .cm-cover h2{font-size:21px}
  .cm-body{padding:20px 18px 22px}}
@media(max-width:640px){.cs-grid{grid-template-columns:1fr}
  .cmd.open{padding:0;align-items:flex-end}
  .cmd-panel{max-height:94vh;border-radius:18px 18px 0 0}}
@media(prefers-reduced-motion:reduce){.cmd-panel{transition:none}
  .cs-badge .dot{animation:none}
  .cs-card,.cs-card:hover{transition:none}}
</style>
"""

CASES_JS = """
<script>
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CASES = window.CASES || [];
  var modal = document.getElementById('caseModal');
  if(!modal) return;
  var scroll = document.getElementById('cmScroll');
  var xBtn = modal.querySelector('.cmd-x');
  var lastFocus = null;

  function esc(s){return String(s).replace(/[&<>"]/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function byId(id){for(var i=0;i<CASES.length;i++){if(CASES[i].id===id)return CASES[i];}return null;}

  function archHtml(a){
    var inner = a.img
      ? '<img src="'+esc(a.img)+'" alt="'+esc(a.label)+'">'
      : '<b>'+esc(a.label)+'</b><small>架构图占位 · 支持替换为真实图片</small>';
    return '<div class="cm-arch" style="height:'+a.h+'px">'+inner+'</div>';
  }
  function render(c){
    var d = c.detail || {};
    var m = c.media || {};
    var media = '';
    if(m.video){media='<video src="'+esc(m.video)+'" autoplay muted loop playsinline></video>';}
    else if(m.img){media='<img src="'+esc(m.img)+'" alt="'+esc(c.title)+'">';}
    var ctags = (d.coverTags||[]).map(function(t){return '<span>'+esc(t)+'</span>';}).join('');
    var chal = (d.challenges||[]).map(function(x){
      return '<div class="cm-chal"><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var caps = (d.capabilities||[]).map(function(x){
      return '<div class="cm-cap cm-chal" style="border-left-color:#5A6B3F"><b>'+esc(x[0])+
             '</b><p>'+esc(x[1])+'</p></div>';}).join('');
    var brks = (d.breakthroughs||[]).map(function(x){
      var st=(x.stats||[]).map(function(s){return '<span>'+esc(s)+'</span>';}).join('');
      return '<div class="cm-brk"><div class="cm-brk-h">'+esc(x.title)+
             '</div><div class="cm-brk-b"><p>'+esc(x.desc)+'</p>'+
             '<div class="cm-brk-stats">'+st+'</div></div></div>';}).join('');
    var arch4 = d.arch4 ? archHtml(d.arch4) : '';
    var arch2 = d.arch2 ? archHtml(d.arch2) : '';
    scroll.innerHTML =
      '<div class="cm-cover">'+media+'<div class="cm-shade"></div><div class="cm-in">'+
        '<div class="cm-ctags">'+ctags+'</div>'+
        '<h2 id="cmTitle">'+esc(c.title)+'</h2>'+
        '<p class="cm-sub">'+esc(d.subtitle||'')+'</p>'+
      '</div></div>'+
      '<div class="cm-body">'+
        '<div class="cm-h">客户原声</div>'+
        '<div class="cm-quote"><p>“'+esc(d.quote||'')+'”</p><small>'+esc(d.quoteBy||'')+'</small></div>'+
        '<div class="cm-h">面临挑战</div><div class="cm-grid2">'+chal+'</div>'+
        '<div class="cm-h">四大核心能力</div>'+arch4+
        '<div class="cm-grid2" style="margin-top:12px">'+caps+'</div>'+
        '<div class="cm-h">两大关键突破</div>'+arch2+
        '<div class="cm-grid2" style="margin-top:12px">'+brks+'</div>'+
        '<div class="cm-cta"><p>'+esc(d.cta||'')+'</p>'+
          '<a class="btn-wt" href="contact.html">联系我们获取方案 &#8594;</a></div>'+
      '</div>';
    scroll.scrollTop = 0;
  }

  function setHash(id){
    try{ history.replaceState(null,'', id ? '#case='+id : location.pathname+location.search); }
    catch(e){}
  }
  function open(id){
    var c = byId(id);
    if(!c) return;
    render(c);
    modal.classList.add('open');
    modal.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
    lastFocus = document.activeElement;
    xBtn.focus();
    setHash(id);
  }
  function close(){
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
    if(lastFocus && lastFocus.focus) lastFocus.focus();
    setHash(null);
  }

  /* 卡片点击 → 弹窗；无 JS 时由链接兜底跳转独立详情页 */
  Array.prototype.forEach.call(document.querySelectorAll('[data-case]'), function(el){
    el.addEventListener('click', function(e){
      e.preventDefault();
      open(el.getAttribute('data-case'));
    });
  });

  /* 关闭：✕ / 遮罩 */
  Array.prototype.forEach.call(modal.querySelectorAll('[data-close]'), function(el){
    el.addEventListener('click', close);
  });
  /* 关闭：ESC */
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && modal.classList.contains('open')) close();
  });

  /* 入口与 hash 联动：#case=smart-border */
  function fromHash(){
    var m = /^#case=([\\w-]+)$/.exec(location.hash);
    if(m) open(m[1]);
  }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
</script>
"""

cases_json = json.dumps(CASES, ensure_ascii=False)
cases_head = "<script>window.CASES=%s;</script>%s" % (cases_json, CASES_CSS)

w("cases.html", page("客户案例 | 天元平台",
  "天元平台客户案例：智慧边防等行业的智能化实践成果，点击卡片查看案例详情。",
  "cases", cso, extra_head=cases_head, extra_js=CASES_JS))

# ================= 案例独立详情页（军绿主题，智慧边防） =================
D = CASES[0]
d = D["detail"]

def arch_block(a):
    inner = ('<img src="%s" alt="%s">' % (esc(a["img"]), esc(a["label"]))) if a["img"] else \
            ('<b>%s</b><small>架构图占位 · 支持替换为真实图片</small>' % esc(a["label"]))
    return ('<div class="cm-arch" style="height:%dpx">%s</div>' % (a["h"], inner))

chal_html = "".join('<div class="cm-chal"><b>%s</b><p>%s</p></div>'
                    % (esc(x[0]), esc(x[1])) for x in d["challenges"])
caps_html = "".join('<div class="cm-cap cm-chal" style="border-left-color:#5A6B3F"><b>%s</b><p>%s</p></div>'
                    % (esc(x[0]), esc(x[1])) for x in d["capabilities"])
brks_html = "".join(
    '<div class="cm-brk"><div class="cm-brk-h">%s</div><div class="cm-brk-b"><p>%s</p>'
    '<div class="cm-brk-stats">%s</div></div></div>'
    % (esc(b["title"]), esc(b["desc"]),
       "".join('<span>%s</span>' % esc(s) for s in b["stats"]))
    for b in d["breakthroughs"])
spec_html = "".join('<div><span>%s</span><small>%s</small></div>'
                    % (esc(s["v"]), esc(s["l"])) for s in D["stats"])
ctags_html = "".join('<span>%s</span>' % esc(t) for t in d["coverTags"])

cd = """
<div class="banner pad" style="background:linear-gradient(135deg,#232D18,#3E4A2B 55%,#55663A)">
<div class="banner-in">
  <div class="cm-ctags" style="margin-bottom:14px">__CTAGS__</div>
  <h1>__TITLE__</h1>
  <p class="lead">__SUBTITLE__</p>
  <div class="spec">__SPEC__</div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> /
  <a href="cases.html">客户案例</a> / 智慧边防</div></div>

<section class="sec">
  <div class="wrap">
    <div class="cm-body" style="padding:0;max-width:920px;margin:0 auto">
      <div class="cm-h">客户原声</div>
      <div class="cm-quote"><p>“__QUOTE__”</p><small>__QUOTEBY__</small></div>
      <div class="cm-h">面临挑战</div>
      <div class="cm-grid2">__CHAL__</div>
      <div class="cm-h">四大核心能力</div>
      __ARCH4__
      <div class="cm-grid2" style="margin-top:12px">__CAPS__</div>
      <div class="cm-h">两大关键突破</div>
      __ARCH2__
      <div class="cm-grid2" style="margin-top:12px">__BRKS__</div>
      <div class="cm-cta"><p>__CTA__</p>
        <a class="btn-wt" href="contact.html">联系我们获取方案 &#8594;</a></div>
    </div>
    <div class="note rv" style="margin-top:26px"><b>合规要求：</b>成果数据须注明对比基准与数据来源，
      客户名称与影像资料须经客户书面授权后方可公开展示；评价须真实可追溯。</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k" style="color:#5A6B3F">MORE</div>
      <h2 style="color:#2F3B22">相关推荐</h2></div>
    <div class="grid3 rv">
      <a class="card" href="cases.html"><div class="ico">例</div><h3>更多客户案例</h3>
        <p>返回案例列表，查看各行业实践成果。</p></a>
      <a class="card" href="solutions.html"><div class="ico">解</div><h3>行业解决方案</h3>
        <p>按行业查找业务痛点与对应方案。</p></a>
      <a class="card" href="products.html"><div class="ico">天</div><h3>天元平台产品与能力</h3>
        <p>从数据获取到行动执行的全链路能力。</p></a>
    </div>
  </div>
</section>
"""
cd = (cd.replace("__CTAGS__", ctags_html).replace("__TITLE__", esc(D["title"]))
        .replace("__SUBTITLE__", esc(d["subtitle"])).replace("__SPEC__", spec_html)
        .replace("__QUOTE__", esc(d["quote"])).replace("__QUOTEBY__", esc(d["quoteBy"]))
        .replace("__CHAL__", chal_html).replace("__ARCH4__", arch_block(d["arch4"]))
        .replace("__CAPS__", caps_html).replace("__ARCH2__", arch_block(d["arch2"]))
        .replace("__BRKS__", brks_html).replace("__CTA__", esc(d["cta"])))

cd_css = CASES_CSS.replace("<style>", "<style>\n/* 独立详情页：复用弹窗军绿组件样式 */")

w("case-detail.html", page("智慧边防案例 | 天元平台",
  "天元平台智慧边防实践：从“看得见”到“看得准”，误报降低 80%，有效报警率 95% 以上。",
  "cases", cd, extra_head=cd_css))

print("第二批完成（客户案例 PRD 版）")
