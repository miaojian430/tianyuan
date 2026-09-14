# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# ============ 关于我们 ============
ab = """
<div class="banner pad"><div class="banner-in">
  <h1>关于我们</h1>
  <p class="lead">以国为重、以人为本、以质取胜、以新图强。<br>
    研究怎么在卫星应用产业里真正挣到钱 —— 研究的是技术，更是价值。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 关于我们</div></div>

<section class="sec" id="intro">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">INTRODUCTION</div><h2>研究院简介</h2></div>
    <div class="grid2 rv">
      <div class="card" style="border-left:3px solid #0F3D75">
        <h3>我们的定位</h3>
        <p style="line-height:2">中国航天科技集团卫星应用创新研究院于 2025 年 5 月揭牌成立，
          依托中国卫通组建运行、委托中国卫通管理，是集团公司级非法人实体化研发机构。</p>
        <p style="line-height:2;margin-top:12px">集团赋予三项定位：卫星应用技术的系统总体；
          卫星应用领域技术创新和产品创新的主体力量；卫星应用技术成果转化和项目孵化的重要平台。</p>
      </div>
      <div class="card" style="border-left:3px solid #00A0E9">
        <h3>核心数据</h3>
        <div class="grid2" style="gap:14px;margin-top:8px">
          <div style="background:#EEF4FA;border-radius:6px;padding:16px;text-align:center">
            <div style="font-size:26px;font-weight:700;color:#0F3D75">5</div>
            <div style="font-size:12.5px;color:#5C6670">个研究所</div></div>
          <div style="background:#EEF4FA;border-radius:6px;padding:16px;text-align:center">
            <div style="font-size:26px;font-weight:700;color:#1B5A9E">【待补】</div>
            <div style="font-size:12.5px;color:#5C6670">人员规模</div></div>
          <div style="background:#EEF4FA;border-radius:6px;padding:16px;text-align:center">
            <div style="font-size:26px;font-weight:700;color:#00608C">【待补】</div>
            <div style="font-size:12.5px;color:#5C6670">服务客户数</div></div>
          <div style="background:#EEF4FA;border-radius:6px;padding:16px;text-align:center">
            <div style="font-size:26px;font-weight:700;color:#0F3D75">【待补】</div>
            <div style="font-size:12.5px;color:#5C6670">知识产权</div></div>
        </div>
        <p style="margin-top:12px;font-size:12.5px;color:#C8102E">
          【量化数据须由院办提供官方口径后填入，此处不预设】</p>
      </div>
    </div>
    <div class="grid3 rv" style="margin-top:22px">
      <div class="card"><div class="ico">总</div><h3>系统总体</h3>
        <p>负责系统设计、系统构建与系统分解，把复杂需求拆解为可执行、可交付、可算清账的任务包。</p></div>
      <div class="card"><div class="ico">创</div><h3>创新主体</h3>
        <p>突破自主可控系统研制等关键核心技术。买来的技术随时会被断供，集成来的能力随时会被替代。</p></div>
      <div class="card"><div class="ico">转</div><h3>转化平台</h3>
        <p>推动技术走出实验室、变成产品与收入。停在论文和样机阶段，等于没干。</p></div>
    </div>
  </div>
</section>

<section class="sec alt" id="history">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">MILESTONES</div><h2>发展历程</h2>
      <p>仅展示时间轴，与上方简介内容不重复。移动端自动切换为纵向。</p></div>
    <div class="tl rv">
      <div class="tl-i"><div class="tl-c"><div class="tl-y">2025 年 5 月</div>
        <b>研究院揭牌成立</b>中国航天科技集团卫星应用创新研究院正式揭牌。</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">2025 年</div>
        <b>理事会与技术委员会</b>召开第一次会议，明确“感通算用”一体服务主线。【配图待补充】</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间待补】</div>
        <b>【里程碑事件待补充】</b>【说明待补充。请按实际节点补充，勿臆造。】</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间待补】</div>
        <b>【里程碑事件待补充】</b>【说明待补充。】</div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CULTURE</div><h2>企业文化与价值观</h2></div>
    <div class="grid4 rv">
      <div class="card" style="text-align:center;border-top:3px solid #0F3D75"><h3>以国为重</h3>
        <p>服务国家战略，把国家利益放在首位。</p></div>
      <div class="card" style="text-align:center;border-top:3px solid #1B5A9E"><h3>以人为本</h3>
        <p>人才是航天的发动机，航天是人才的推进器。</p></div>
      <div class="card" style="text-align:center;border-top:3px solid #00A0E9"><h3>以质取胜</h3>
        <p>质量是政治、是生命、是效益。</p></div>
      <div class="card" style="text-align:center;border-top:3px solid #57779E"><h3>以新图强</h3>
        <p>以创新谋发展，研究能挣钱的技术。</p></div>
    </div>
    <div class="info rv"><b>编写要求：</b>价值观须配具体行为描述，避免空洞口号。
      上述四条为航天企业文化既有表述，具体阐释请由院办审定。</div>
  </div>
</section>

<section class="sec alt" id="honor">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">HONORS</div><h2>资质与合作伙伴</h2>
      <p>证书墙与伙伴 Logo 统一灰度处理，hover 恢复彩色。</p></div>
    <div class="logos rv">
      <div class="logo-b">【资质证书 1】</div><div class="logo-b">【资质证书 2】</div>
      <div class="logo-b">【资质证书 3】</div><div class="logo-b">【资质证书 4】</div>
      <div class="logo-b">【合作伙伴 1】</div><div class="logo-b">【合作伙伴 2】</div>
      <div class="logo-b">【合作伙伴 3】</div><div class="logo-b">【合作伙伴 4】</div>
      <div class="logo-b">【合作伙伴 5】</div><div class="logo-b">【合作伙伴 6】</div>
      <div class="logo-b">【合作伙伴 7】</div><div class="logo-b">【合作伙伴 8】</div>
    </div>
    <div class="note rv"><b>待补充：</b>资质证书涉及经营范围与合规表述，
      合作伙伴名录涉及品牌授权，均须经品牌、法规部门审定后发布。</div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>与我们一起，把卫星应用真正用起来</h2>
    <p>我们正在寻找认同这份事业的同行者。</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-p btn-lg" href="careers.html">加入我们</a>
      <a class="btn btn-o btn-lg" href="contact.html">商务合作</a></div></div>
</section>
"""
w("about.html", page("关于我们 | 中国航天科技集团卫星应用创新研究院",
  "研究院简介、发展历程、企业文化与资质荣誉。", "about", ab))

# ============ 新闻动态 ============
nw = """
<div class="banner pad"><div class="banner-in">
  <h1>新闻动态</h1>
  <p class="lead">记录平台进展、技术成果与生态合作。内容持续更新中。</p>
  <div style="display:flex;gap:10px;margin-top:24px;flex-wrap:wrap">
    <input type="email" placeholder="订阅邮箱（功能待开通）" autocomplete="email"
      style="min-height:46px;padding:11px 16px;border-radius:4px;border:1px solid rgba(255,255,255,.4);
      background:rgba(255,255,255,.12);color:#fff;font-size:14px;min-width:260px;font-family:inherit">
    <a class="btn btn-p" href="contact.html">订阅动态</a>
  </div>
  <p style="font-size:12.5px;color:#BBCEE2;margin-top:10px">
    订阅需提供成功反馈与退订入口，符合个人信息保护相关要求。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 新闻动态</div></div>

<section class="sec">
  <div class="wrap">
    <div class="filter-bar rv" data-group="news">
      <span class="lb">按类型筛选</span>
      <button class="chip" data-k="top" type="button">要闻</button>
      <button class="chip" data-k="tech" type="button">技术</button>
      <button class="chip" data-k="eco" type="button">生态</button>
      <button class="chip" data-k="media" type="button">媒体聚焦</button>
    </div>
    <div class="selected" data-selected="news"></div>
    <div class="nlist rv">
      <a href="#n1" data-fl="news" data-f="top"><div class="nd"><b>【日】</b><small>【年月】</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位。正式发布前请替换为已审定的公开稿件，勿使用未经核实的信息。】</p></div>
        <div class="nt"><span>要闻</span></div></a>
      <a href="#n1" data-fl="news" data-f="tech"><div class="nd"><b>【日】</b><small>【年月】</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充】</p></div>
        <div class="nt"><span>技术</span></div></a>
      <a href="#n1" data-fl="news" data-f="eco"><div class="nd"><b>【日】</b><small>【年月】</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充】</p></div>
        <div class="nt"><span>生态</span></div></a>
      <a href="#n1" data-fl="news" data-f="media"><div class="nd"><b>【日】</b><small>【年月】</small></div>
        <div class="nc"><h3>【新闻标题占位 · 待补充】</h3>
          <p>【新闻摘要占位 · 待补充】</p></div>
        <div class="nt"><span>媒体聚焦</span></div></a>
    </div>
    <div class="nlist rv" data-empty="news" style="display:none;margin-top:20px">
      <div style="padding:34px 24px;text-align:center;color:#5C6670">
        暂无该分类内容，请查看<a href="news.html" style="color:#00608C;text-decoration:underline">全部动态</a>。</div></div>

    <div class="note rv" id="n1"><b>待补充：</b>新闻详情页需独立页面并配置 Open Graph 与
      Twitter Card 结构化数据；分类栏目若内容不足，建议暂不单独设置，避免空栏目。</div>
  </div>
</section>
"""
w("news.html", page("新闻动态 | 天元平台",
  "天元平台与卫星应用创新研究院的最新动态、技术进展与生态合作资讯。", "about", nw))

# ============ 加入我们 ============
cr = """
<div class="banner pad"><div class="banner-in">
  <h1>加入我们</h1>
  <p class="lead">人才是航天的发动机，航天是人才的推进器。</p>
  <a class="btn btn-p btn-lg" href="#jobs" style="margin-top:22px">查看在招岗位</a>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 加入我们</div></div>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">WHY US</div><h2>为什么选择我们</h2>
      <p>具体、可验证的待遇与成长支持，不使用“有竞争力薪资”等空泛表述。</p></div>
    <div class="grid4 rv">
      <div class="card"><div class="ico">薪</div><h3>薪酬保障</h3><p>【具体薪酬结构待补充，如“14 薪 + 年度调薪”】</p></div>
      <div class="card"><div class="ico">保</div><h3>社会保障</h3><p>【社保公积金缴纳基数与比例待补充】</p></div>
      <div class="card"><div class="ico">健</div><h3>健康关怀</h3><p>【年度体检等具体安排待补充】</p></div>
      <div class="card"><div class="ico">时</div><h3>工作制度</h3><p>【工时与休假制度待补充，如“弹性工作制”】</p></div>
    </div>
    <div class="note rv"><b>编写要求：</b>福利待遇必须具体、可验证。
      上述条目均需由人力资源部门提供正式口径后填入。</div>
  </div>
</section>

<section class="sec alt" id="jobs">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">OPENINGS</div><h2>开放岗位</h2></div>
    <div class="filter-bar rv" data-group="job">
      <span class="lb">按类型筛选</span>
      <button class="chip" data-k="rd" type="button">研发</button>
      <button class="chip" data-k="algo" type="button">算法</button>
      <button class="chip" data-k="sys" type="button">系统总体</button>
      <button class="chip" data-k="mkt" type="button">市场与生态</button>
    </div>
    <div class="selected" data-selected="job"></div>
    <div class="nlist rv">
      <div data-fl="job" data-f="rd" style="padding:20px 24px;border-bottom:1px solid #D6DCE1">
        <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
          <div><h3 style="font-size:16px;color:#0F3D75;font-weight:700">【岗位名称待补充】</h3>
            <p style="font-size:13px;color:#5C6670">研发 · 【地点待补充】 · 全职</p></div>
          <a class="btn btn-s" href="mailto:【招聘邮箱待补充】">申请岗位</a></div></div>
      <div data-fl="job" data-f="algo" style="padding:20px 24px;border-bottom:1px solid #D6DCE1">
        <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
          <div><h3 style="font-size:16px;color:#0F3D75;font-weight:700">【岗位名称待补充】</h3>
            <p style="font-size:13px;color:#5C6670">算法 · 【地点待补充】 · 全职</p></div>
          <a class="btn btn-s" href="mailto:【招聘邮箱待补充】">申请岗位</a></div></div>
      <div data-fl="job" data-f="sys" style="padding:20px 24px;border-bottom:1px solid #D6DCE1">
        <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
          <div><h3 style="font-size:16px;color:#0F3D75;font-weight:700">【岗位名称待补充】</h3>
            <p style="font-size:13px;color:#5C6670">系统总体 · 【地点待补充】 · 全职</p></div>
          <a class="btn btn-s" href="mailto:【招聘邮箱待补充】">申请岗位</a></div></div>
      <div data-fl="job" data-f="mkt" style="padding:20px 24px">
        <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
          <div><h3 style="font-size:16px;color:#0F3D75;font-weight:700">【岗位名称待补充】</h3>
            <p style="font-size:13px;color:#5C6670">市场与生态 · 【地点待补充】 · 全职</p></div>
          <a class="btn btn-s" href="mailto:【招聘邮箱待补充】">申请岗位</a></div></div>
    </div>
    <div class="nlist rv" data-empty="job" style="display:none;margin-top:20px">
      <div style="padding:34px 24px;text-align:center;color:#5C6670">
        暂无该类型岗位，欢迎投递<a href="mailto:【招聘邮箱待补充】" style="color:#00608C;text-decoration:underline">通用简历</a>。</div></div>
    <div class="info rv"><b>投递要求：</b>支持邮箱直投与招聘平台跳转双通道；
      投递后须自动确认反馈（如“简历已收到，将在 3–5 个工作日内回复”）。</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">OUR PEOPLE</div><h2>员工故事</h2></div>
    <div class="grid2 rv">
      <div class="card"><div class="ico">员</div><h3>【员工姓名 / 岗位待补充】</h3>
        <p>【真实访谈内容占位。须获员工本人授权，避免过度美化。】</p></div>
      <div class="card"><div class="ico">员</div><h3>【员工姓名 / 岗位待补充】</h3>
        <p>【真实访谈内容占位。须获员工本人授权，避免过度美化。】</p></div>
    </div>
  </div>
</section>
"""
w("careers.html", page("加入我们 | 天元平台",
  "卫星应用创新研究院人才招聘：在招岗位、福利待遇与员工故事。", "about", cr))

print("第三批完成")
