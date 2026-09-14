# -*- coding: utf-8 -*-
import io, sys
sys.path.insert(0, '.')
from common import page
def w(n,s): io.open("../"+n,"w",encoding="utf-8").write(s); print("  ->",n)

# 解决方案页已迁移至 build_sol.py（基于《产品详情V1》五大场景）

# ============ 案例总览 ============
cso = """
<div class="banner pad"><div class="banner-in">
  <h1>客户案例</h1>
  <p class="lead">我们做过什么 —— 来自真实项目的可验证成果。</p>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> / 客户案例</div></div>

<section class="sec">
  <div class="wrap">
    <div class="filter-bar rv" data-group="case">
      <span class="lb">按行业筛选</span>
      <button class="chip" data-k="emergency" type="button">应急管理</button>
      <button class="chip" data-k="resource" type="button">自然资源</button>
      <button class="chip" data-k="agri" type="button">智慧农业</button>
      <button class="chip" data-k="logistics" type="button">交通物流</button>
      <button class="chip" data-k="city" type="button">城市治理</button>
    </div>
    <div class="selected" data-selected="case"></div>
    <div class="grid3">
      <a class="pcard rv" data-fl="case" data-f="emergency" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#0F3D75,#1B5A9E)">
          <span class="ph-tag">应急救援</span>【客户名称待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【项目简述占位。成果数据须注明对比基准。】</p>
          <div style="margin-top:12px;font-size:20px;font-weight:700;color:#0F3D75">
            【成果数据】<span style="font-size:12px;color:#5C6670;font-weight:400">待补充</span></div>
          <span class="more">查看详情 &#8594;</span></div></a>
      <a class="pcard rv" data-fl="case" data-f="resource" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#1B5A9E,#3F6491)">
          <span class="ph-tag">自然资源</span>【客户名称待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【项目简述占位。成果数据须注明对比基准。】</p>
          <div style="margin-top:12px;font-size:20px;font-weight:700;color:#0F3D75">
            【成果数据】<span style="font-size:12px;color:#5C6670;font-weight:400">待补充</span></div>
          <span class="more">查看详情 &#8594;</span></div></a>
      <a class="pcard rv" data-fl="case" data-f="agri" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#0C315E,#16487E)">
          <span class="ph-tag">智慧农业</span>【客户名称待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【项目简述占位。成果数据须注明对比基准。】</p>
          <div style="margin-top:12px;font-size:20px;font-weight:700;color:#0F3D75">
            【成果数据】<span style="font-size:12px;color:#5C6670;font-weight:400">待补充</span></div>
          <span class="more">查看详情 &#8594;</span></div></a>
      <a class="pcard rv" data-fl="case" data-f="logistics" href="case-detail.html">
        <div class="ph" style="background:linear-gradient(135deg,#092546,#1B5A9E)">
          <span class="ph-tag">交通物流</span>【客户名称待补充】</div>
        <div class="pb"><h3>【案例标题占位 · 待补充】</h3>
          <p>【项目简述占位。成果数据须注明对比基准。】</p>
          <div style="margin-top:12px;font-size:20px;font-weight:700;color:#0F3D75">
            【成果数据】<span style="font-size:12px;color:#5C6670;font-weight:400">待补充</span></div>
          <span class="more">查看详情 &#8594;</span></div></a>
    </div>
    <div class="nlist rv" data-empty="case" style="display:none;margin-top:20px">
      <div style="padding:34px 24px;text-align:center;color:#5C6670">
        暂无该行业案例，请联系销售获取最新方案。
        <a href="contact.html" style="color:#00608C;text-decoration:underline">联系我们 &#8594;</a>
      </div></div>
    <div class="note rv"><b>合规要求：</b>客户名称、Logo 与成果数据须经客户书面授权后方可公开展示；
      成果数据需注明对比基准（如“效率提升 X% vs 传统方案”）与数据来源。</div>
  </div>
</section>
"""
w("cases.html", page("客户案例 | 天元平台",
  "天元平台在应急管理、自然资源、智慧农业、交通物流、城市治理等领域的项目案例。", "cases", cso))

# ============ 案例详情 ============
cd = """
<div class="banner pad"><div class="banner-in">
  <span style="display:inline-block;background:#00A0E9;color:#1A1A1A;font-size:12px;font-weight:700;
    padding:4px 12px;border-radius:3px;margin-bottom:12px">【行业标签待补充】</span>
  <h1>【案例标题占位 · 待补充】</h1>
  <p class="lead">【客户名称待补充】 · 【项目时间待补充】</p>
  <div class="spec">
    <div><span>【待补】</span><small>核心成果一</small></div>
    <div><span>【待补】</span><small>核心成果二</small></div>
    <div><span>【待补】</span><small>核心成果三</small></div>
  </div>
</div></div>
<div class="wrap"><div class="crumb"><a href="index.html">首页</a> /
  <a href="cases.html">客户案例</a> / 【案例标题】</div></div>

<section class="sec">
  <div class="wrap">
    <div class="grid2">
      <div class="card rv" style="border-left:3px solid #0F3D75"><h3>客户背景</h3>
        <p>【客户简介与业务规模占位。1–2 段即可，须经客户确认后发布。】</p></div>
      <div class="card rv" style="border-left:3px solid #00A0E9"><h3>核心成果</h3>
        <p>【成果数据占位。须注明对比基准与数据来源，例如：效率提升 X%，
          对比基准为传统人工巡检方式，数据来源为【客户名称】【年份】项目验收报告。】</p></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">CHALLENGES</div><h2>项目挑战</h2></div>
    <div class="grid4 rv">
      <div class="card"><div class="ico">01</div><h3>【痛点一】</h3><p>【简述占位】</p></div>
      <div class="card"><div class="ico">02</div><h3>【痛点二】</h3><p>【简述占位】</p></div>
      <div class="card"><div class="ico">03</div><h3>【痛点三】</h3><p>【简述占位】</p></div>
      <div class="card"><div class="ico">04</div><h3>【痛点四】</h3><p>【简述占位】</p></div>
    </div>
    <div class="sec-h left rv" style="margin-top:44px"><div class="k">SOLUTION</div><h2>解决方案</h2>
      <p>方案与上述挑战一一对应，形成逻辑闭环。</p></div>
    <div class="rv" style="background:#fff;border:1px solid #BEC3C8;border-radius:8px;padding:30px;
      text-align:center;color:#5C6670;font-size:13.5px">
      【方案架构图占位 · 支持点击放大，移动端可横向滑动，并补充文字说明与 alt 文本】
    </div>
    <div class="grid3 rv" style="margin-top:22px">
      <div class="card"><h4>关键功能一</h4><p>【对应挑战一的解决方式】</p></div>
      <div class="card"><h4>关键功能二</h4><p>【对应挑战二的解决方式】</p></div>
      <div class="card"><h4>关键功能三</h4><p>【对应挑战三的解决方式】</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">PROCESS</div><h2>实施过程</h2></div>
    <div class="tl rv">
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间节点 1】</div><b>需求对接</b>【说明占位】</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间节点 2】</div><b>方案设计</b>【说明占位】</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间节点 3】</div><b>部署实施</b>【说明占位】</div></div>
      <div class="tl-i"><div class="tl-c"><div class="tl-y">【时间节点 4】</div><b>验收交付</b>【说明占位】</div></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h left rv"><div class="k">RESULTS</div><h2>成果数据</h2></div>
    <div class="grid3 rv">
      <div class="card" style="text-align:center"><div style="font-size:34px;font-weight:700;color:#0F3D75">【待补】</div>
        <p style="margin-top:6px">【指标一 · 须注明基准与来源】</p></div>
      <div class="card" style="text-align:center"><div style="font-size:34px;font-weight:700;color:#1B5A9E">【待补】</div>
        <p style="margin-top:6px">【指标二 · 须注明基准与来源】</p></div>
      <div class="card" style="text-align:center"><div style="font-size:34px;font-weight:700;color:#00608C">【待补】</div>
        <p style="margin-top:6px">【指标三 · 须注明基准与来源】</p></div>
    </div>
    <div class="grid2 rv" style="margin-top:22px">
      <div class="card" style="border-left:3px solid #1B5A9E"><h3>客户评价</h3>
        <p style="font-size:15px;line-height:1.95">“【评价引语占位】”</p>
        <p style="margin-top:12px;font-size:13px;color:#5C6670">—— 【评价人姓名 / 职位】</p>
        <p style="margin-top:8px;font-size:12.5px;color:#C8102E">
          评价须真实可追溯并获客户授权，避免过度美化。</p></div>
      <div class="card"><h3>相关推荐</h3>
        <ul style="margin-top:10px">
          <li style="padding:8px 0;border-bottom:1px solid #D6DCE1">
            <a href="case-detail.html" style="color:#00608C">同行业案例【待补充】 &#8594;</a></li>
          <li style="padding:8px 0;border-bottom:1px solid #D6DCE1">
            <a href="solutions.html" style="color:#00608C">相关解决方案【待补充】 &#8594;</a></li>
          <li style="padding:8px 0">
            <a href="product-detail.html" style="color:#00608C">天元平台产品详情 &#8594;</a></li>
        </ul></div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2>获取同类方案</h2>
    <p>如果你的业务面临相似挑战，欢迎联系我们获取针对性建议。</p>
    <a class="btn btn-p btn-lg" href="contact.html">获取同类方案</a></div>
</section>
"""
w("case-detail.html", page("案例详情 | 天元平台",
  "天元平台项目案例详情：客户背景、项目挑战、解决方案、实施过程与成果数据。", "cases", cd))

print("第二批完成")
