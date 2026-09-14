# -*- coding: utf-8 -*-
"""天元官网 · 共享组件（导航 / 页脚 / 抽屉 / Cookie）"""

NAV = [
    ("index",     "首页",        "index.html", []),
    ("products",  "产品与能力",  "products.html", [
        ("分层能力一览", "products.html#layers"),
        ("基础设施层 · 智算底座", "products.html#infra"),
        ("数据融合层 · 空天地数据融合引擎", "products.html#fusion"),
        ("认知决策层 · 认知计算与决策引擎", "products.html#cognition"),
        ("行动执行层 · 具身智能行动执行引擎", "products.html#embodied"),
        ("数智市集 · 天元·灵集", "products.html#market"),
        ("安全合规 · 全栈安全合规", "products.html#security"),
    ]),
    ("solutions", "解决方案",    "solutions.html", [
        ("应急管理", "solutions.html#emergency"),
        ("自然资源监测", "solutions.html#resource"),
        ("智慧农业", "solutions.html#agri"),
        ("交通物流", "solutions.html#logistics"),
    ]),
    ("cases",     "客户案例",    "cases.html", [
        ("案例总览", "cases.html"),
        ("标杆案例", "case-detail.html"),
    ]),
    ("about",     "关于我们",    "about.html", [
        ("研究院简介", "about.html#intro"),
        ("发展历程", "about.html#history"),
        ("资质荣誉", "about.html#honor"),
    ]),
    ("contact",   "联系我们",    "contact.html", []),
]


def head(title, desc, extra=""):
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="assets/theme.css">
%s
</head>
<body>
""" % (title, desc, title, desc, extra)


def topbar():
    return """<div class="topbar">
  <div class="topbar-in">
    <span class="org">中国航天科技集团卫星应用创新研究院</span>
    <div class="topbar-right">
      <a href="search.html">站内搜索</a>
      <a href="careers.html">加入我们</a>
      <a href="news.html">新闻动态</a>
      <a href="#" class="lang" title="语言切换">中文 / EN</a>
    </div>
  </div>
</div>
"""


def navbar(active):
    items = []
    for key, label, url, subs in NAV:
        on = " on" if key == active else ""
        if subs:
            sub = '<div class="sub">' + "".join(
                '<a href="%s">%s</a>' % (u, t) for t, u in subs) + '</div>'
            items.append('<li class="%s"><a href="%s">%s</a>%s</li>' % (on.strip(), url, label, sub))
        else:
            items.append('<li class="%s"><a href="%s">%s</a></li>' % (on.strip(), url, label))
    return """<nav class="nav">
  <div class="nav-in">
    <a class="logo" href="index.html">
      <div class="logo-m"></div>
      <div><div class="logo-t">天元</div><div class="logo-s">TIANYUAN</div></div>
    </a>
    <ul class="menu">%s</ul>
    <div class="nav-right">
      <a class="icon-btn" href="search.html" title="搜索" aria-label="搜索">&#128269;</a>
      <a class="btn btn-p" href="contact.html">申请演示</a>
      <button class="hamburger" aria-label="打开菜单"><i></i><i></i><i></i></button>
    </div>
  </div>
</nav>
""" % "".join(items)


def drawer(active):
    li = []
    for key, label, url, subs in NAV:
        on = " on" if key == active else ""
        if subs:
            m = "".join('<a href="%s">%s</a>' % (u, t) for t, u in subs)
            li.append('<li class="has-sub"><a href="%s" class="%s">%s &#8250;</a>'
                      '<div class="sub-m" style="display:none">%s</div></li>'
                      % (url, on.strip(), label, m))
        else:
            li.append('<li><a href="%s" class="%s">%s</a></li>' % (url, on.strip(), label))
    return """<div class="drawer">
  <div class="drawer-h"><b>导航菜单</b><button class="drawer-close" aria-label="关闭菜单">&times;</button></div>
  <ul>%s</ul>
  <div class="drawer-f">
    <button class="drawer-back" type="button">&#8249; 返回上一级</button>
    <a class="btn btn-p btn-w" href="contact.html">申请演示</a>
  </div>
</div>
""" % "".join(li)


def footer():
    return """<footer class="ft">
  <div class="wrap">
    <div class="ft-g">
      <div>
        <h5>天元平台</h5>
        <p class="ab">“感通算用”一体化综合信息服务平台<br>
        依托天地一体化资源，面向行业智能升级<br>
        提供一站式信息服务。<br>
        中国航天科技集团卫星应用创新研究院</p>
        <p class="ab" style="margin-top:10px">地址：【待补充】<br>邮编：【待补充】</p>
      </div>
      <div>
        <h5>产品与能力</h5>
        <ul>
          <li><a href="products.html">天元平台总览</a></li>
          <li><a href="products.html#fusion">空天地数据融合引擎</a></li>
          <li><a href="products.html#cognition">认知计算与决策引擎</a></li>
          <li><a href="products.html#embodied">具身智能行动执行引擎</a></li>
          <li><a href="products.html#market">天元 · 灵集（数智市集）</a></li>
          <li><a href="products.html#security">全栈安全合规</a></li>
        </ul>
      </div>
      <div>
        <h5>关于我们</h5>
        <ul>
          <li><a href="about.html">研究院简介</a></li>
          <li><a href="about.html#history">发展历程</a></li>
          <li><a href="about.html#honor">资质荣誉</a></li>
          <li><a href="careers.html">加入我们</a></li>
          <li><a href="news.html">新闻动态</a></li>
        </ul>
      </div>
      <div>
        <h5>联系与帮助</h5>
        <p class="ct">
          商务合作：<a href="tel:【待补充】">【待补充】</a><br>
          技术支持：<a href="mailto:【待补充】">【待补充】</a><br>
          媒体问询：<a href="mailto:【待补充】">【待补充】</a><br>
          工作时间：工作日 9:00–17:30
        </p>
        <p class="ct" style="margin-top:10px">
          <a href="search.html">站内搜索</a> ·
          <a href="sitemap.html">网站地图</a>
        </p>
      </div>
    </div>
    <div class="ft-b">
      <div class="links">
        <a href="contact.html">联系我们</a>
        <a href="legal.html">隐私政策</a>
        <a href="legal.html#terms">服务条款</a>
        <a href="legal.html#cookie">Cookie 声明</a>
        <a href="sitemap.html">网站地图</a>
        <a href="404.html">404 页示例</a>
      </div>
      <div class="icp">
        中国航天科技集团卫星应用创新研究院　版权所有<br>
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">【ICP备案号待补充】</a>
        　|　本页面为结构与配色演示稿，正式发布前请替换全部占位内容并完成合规审核。
      </div>
    </div>
  </div>
</footer>
"""


def cookie():
    return """<div class="cookie">
  <div class="cookie-in">
    <div>我们使用 Cookie 以保障网站正常运行并改善浏览体验。继续使用即表示您同意我们的
      <a href="legal.html#cookie">Cookie 声明</a>与<a href="legal.html">隐私政策</a>。</div>
    <div class="cookie-btns">
      <button class="ck-n" type="button">仅必要 Cookie</button>
      <button class="ck-a" type="button">全部接受</button>
    </div>
  </div>
</div>
"""


def scripts(extra=""):
    return """<button class="totop" aria-label="返回顶部">&#8593;</button>
<script src="assets/main.js"></script>
%s
</body>
</html>
""" % extra


def page(title, desc, active, body, extra_head="", extra_js=""):
    return (head(title, desc, extra_head) + topbar() + navbar(active) + drawer(active)
            + body + footer() + cookie() + scripts(extra_js))
