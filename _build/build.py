# -*- coding: utf-8 -*-
"""天元官网生成器：完整企业官网（航天蓝浅色配色体系）
内容来源：天元 DISOps 官网截图文字 + 《产品详情V1.2》+《引擎V1.2》+《企业官网页面结构清单》
改站方式：直接改本脚本后重新运行 python3 build.py
"""
import os, re, json

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================ 配色（航天蓝色卡，不得引入色卡外颜色）
CSS = """/* ==========================================================
   天元官网 · 航天蓝配色体系（全局样式）
   色值全部取自《航天蓝配色_色卡.html》，不得引入色卡外颜色
   ========================================================== */
:root{
  --primary:#0F3D75;            /* 酞青蓝 主色 */
  --primary-l10:#275083; --primary-l20:#3F6491; --primary-l30:#57779E;
  --primary-l40:#6F8BAC; --primary-l50:#879EBA; --primary-l60:#9FB1C8;
  --primary-l70:#B7C5D6; --primary-l80:#CFD8E3; --primary-l90:#E7ECF1; --primary-l95:#F3F5F8;
  --primary-d10:#0E3769; --primary-d20:#0C315E; --primary-d40:#092546; --primary-d60:#06182F;
  --pl:#1B5A9E;                 /* 航天蓝 主色浅 */
  --pl-l20:#497BB1; --pl-l80:#D1DEEC; --pl-l90:#E8EEF5;
  --pl-d20:#16487E; --pl-d40:#10365F;
  --accent:#00A0E9;             /* 天蓝 辅助色 */
  --accent-l80:#CCECFB; --accent-l90:#E6F6FD; --accent-d20:#0080BA; --accent-d40:#00608C;
  --surface:#EEF4FA;            /* 浅底 */
  --surface-d10:#D6DCE1; --surface-d20:#BEC3C8; --surface-d30:#A7ABAF;
  --ink:#1A1A1A; --ink-l30:#5F5F5F; --ink-l60:#A3A3A3; --ink-l80:#D1D1D1;
  --mute:#5C6670; --mute-l30:#8D949B; --mute-d20:#4A525A;
  --alert:#C8102E; --alert-l90:#FAE7EA; --alert-d20:#A00D25;   /* 中国红 仅警示用 */
  --ok:#00608C;                                               /* 状态正向：天蓝深 */
  --white:#FFFFFF;
  --line:var(--surface-d20); --line-soft:var(--surface-d10);
  --nav-h:68px; --radius:8px;
  --shadow:0 4px 18px rgba(15,61,117,.10);
  --shadow-lg:0 10px 30px rgba(15,61,117,.14);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{animation-duration:.01ms!important;transition-duration:.01ms!important}
}
body{font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif;
  color:var(--ink);background:var(--white);line-height:1.75;font-size:15px;
  -webkit-font-smoothing:antialiased;padding-top:var(--nav-h)}
img{max-width:100%;display:block}
a{color:var(--primary);text-decoration:none}
a:hover{color:var(--pl)}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.section{padding:72px 0}
.section.alt{background:var(--surface)}
.sec-head{text-align:center;max-width:820px;margin:0 auto 44px}
.sec-head .kicker{display:inline-block;color:var(--accent-d20);background:var(--accent-l90);
  border:1px solid var(--accent-l80);font-size:12.5px;font-weight:700;letter-spacing:2px;
  padding:4px 14px;border-radius:999px;margin-bottom:14px}
.sec-head h2{font-size:30px;color:var(--primary);letter-spacing:1px}
.sec-head p{color:var(--mute);margin-top:12px}
h1,h2,h3,h4{font-weight:700}

/* ---------------- 导航 ---------------- */
.nav{position:fixed;top:0;left:0;right:0;height:var(--nav-h);z-index:1000;
  background:rgba(255,255,255,.96);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line-soft);transition:box-shadow .3s}
.nav.scrolled{box-shadow:var(--shadow)}
.nav-in{max-width:1200px;margin:0 auto;padding:0 24px;height:100%;
  display:flex;align-items:center;gap:28px}
.logo{display:flex;align-items:center;gap:10px;flex:none}
.logo-m{width:36px;height:36px;border-radius:8px;flex:none;
  background:linear-gradient(135deg,var(--primary-d40),var(--primary) 55%,var(--pl));
  position:relative}
.logo-m::after{content:"";position:absolute;inset:7px;border:2px solid var(--white);
  border-radius:50%;border-right-color:transparent;border-bottom-color:transparent;
  transform:rotate(45deg)}
.logo-t{font-size:19px;font-weight:800;color:var(--primary);line-height:1.15;letter-spacing:1px}
.logo-s{font-size:10px;color:var(--mute);letter-spacing:2.5px;line-height:1}
.menu{display:flex;list-style:none;gap:4px;flex:1;justify-content:center}
.menu>li{position:relative}
.menu>li>a{display:block;padding:8px 16px;font-size:15px;color:var(--ink);
  border-radius:6px;font-weight:500}
.menu>li>a:hover{color:var(--primary);background:var(--pl-l90)}
.menu>li.on>a{color:var(--white);background:var(--primary);font-weight:700}
.nav-right{display:flex;align-items:center;gap:12px;flex:none}
.icon-btn{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;
  border-radius:8px;border:1px solid var(--line);color:var(--mute);font-size:16px}
.icon-btn:hover{border-color:var(--pl);color:var(--pl)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;cursor:pointer;
  border-radius:6px;font-size:15px;font-weight:700;padding:10px 22px;border:2px solid transparent;
  transition:all .25s;line-height:1.4}
.btn-p{background:var(--primary);color:var(--white)}
.btn-p:hover{background:var(--pl);color:var(--white)}
.btn-o{background:transparent;color:var(--primary);border-color:var(--primary)}
.btn-o:hover{background:var(--primary);color:var(--white)}
.btn-a{background:var(--accent);color:var(--ink)}
.btn-a:hover{background:var(--accent-d20);color:var(--white)}
.btn-lg{padding:14px 34px;font-size:16px}
.btn-w{width:100%}
.hamburger{display:none;width:40px;height:40px;border:1px solid var(--line);border-radius:8px;
  background:none;cursor:pointer;flex-direction:column;align-items:center;justify-content:center;gap:5px}
.hamburger i{width:18px;height:2px;background:var(--primary);display:block}

/* 移动端抽屉 */
.drawer{position:fixed;top:0;bottom:0;right:-320px;width:300px;z-index:1200;
  background:var(--white);box-shadow:var(--shadow-lg);transition:right .3s;
  display:flex;flex-direction:column}
.drawer.open{right:0}
.drawer-mask{position:fixed;inset:0;background:rgba(6,24,47,.45);z-index:1100;display:none}
.drawer-mask.show{display:block}
.drawer-h{display:flex;justify-content:space-between;align-items:center;
  padding:16px 18px;border-bottom:1px solid var(--line-soft)}
.drawer-close{border:none;background:none;font-size:26px;color:var(--mute);cursor:pointer;line-height:1}
.drawer ul{list-style:none;overflow-y:auto;flex:1;padding:8px 0}
.drawer ul a{display:block;padding:12px 20px;color:var(--ink);font-size:15px}
.drawer ul a.on{color:var(--primary);font-weight:700;background:var(--pl-l90)}
.drawer .sub-m a{padding-left:36px;font-size:14px;color:var(--mute)}
.drawer-f{padding:14px 18px;border-top:1px solid var(--line-soft)}
.drawer-back{width:100%;padding:8px;border:1px solid var(--line);border-radius:6px;
  background:var(--surface);color:var(--mute);cursor:pointer;margin-bottom:10px}

/* ---------------- Banner ---------------- */
.banner{background:linear-gradient(120deg,var(--primary-d60) 0%,var(--primary-d20) 38%,var(--primary) 78%,var(--pl) 100%);
  color:var(--white);position:relative;overflow:hidden}
.banner::before{content:"";position:absolute;right:-140px;top:-140px;width:460px;height:460px;
  border-radius:50%;border:60px solid rgba(255,255,255,.05)}
.banner::after{content:"";position:absolute;left:-80px;bottom:-180px;width:360px;height:360px;
  border-radius:50%;border:44px solid rgba(0,160,233,.12)}
.banner-in{position:relative;z-index:1;padding:88px 24px;max-width:980px;margin:0 auto;text-align:center}
.banner .badge{display:inline-block;background:var(--accent);color:var(--ink);font-size:12.5px;
  font-weight:700;padding:5px 16px;border-radius:3px;letter-spacing:2px;margin-bottom:22px}
.banner h1{font-size:44px;letter-spacing:2px;line-height:1.3}
.banner h1 em{font-style:normal;color:var(--accent-l80)}
.banner .lead{color:var(--primary-l70);margin-top:20px;font-size:16.5px;max-width:860px;
  margin-left:auto;margin-right:auto}
.banner .lead b{color:var(--white)}
.banner .btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px}
.banner .btn-o{color:var(--white);border-color:var(--primary-l60)}
.banner .btn-o:hover{background:rgba(255,255,255,.12)}
.page-banner .banner-in{padding:64px 24px}
.page-banner h1{font-size:34px}
.page-banner .lead{font-size:15.5px}

/* ---------------- 卡片 ---------------- */
.grid{display:grid;gap:22px}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g2{grid-template-columns:repeat(2,1fr)}
.card{background:var(--white);border:1px solid var(--line-soft);border-radius:var(--radius);
  padding:26px 24px;transition:all .3s}
.section.alt .card{box-shadow:var(--shadow)}
.card:hover{border-color:var(--pl-l20);box-shadow:var(--shadow-lg);transform:translateY(-3px)}
.card h3{font-size:18px;color:var(--primary);margin-bottom:10px}
.card p{color:var(--mute);font-size:14.5px}
.ico{width:46px;height:46px;border-radius:10px;display:flex;align-items:center;justify-content:center;
  font-size:22px;margin-bottom:16px;background:var(--pl-l90);color:var(--primary)}
.ico.accent{background:var(--accent-l90);color:var(--accent-d40)}
.ico.deep{background:var(--primary);color:var(--white)}
.card .num{font-size:13px;color:var(--accent-d20);font-weight:800;letter-spacing:1px;margin-bottom:6px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tag{display:inline-block;font-size:12.5px;padding:3px 12px;border-radius:999px;
  border:1px solid var(--pl-l20);color:var(--pl-d20);background:var(--pl-l90)}
.tag.a{border-color:var(--accent-l80);color:var(--accent-d40);background:var(--accent-l90)}
.more{display:inline-block;margin-top:14px;font-size:14px;font-weight:700;color:var(--accent-d20)}
.more:hover{color:var(--accent)}
.placeholder-note{display:inline-block;font-size:12px;color:var(--alert);
  background:var(--alert-l90);border:1px dashed var(--alert);border-radius:4px;
  padding:2px 10px;margin-left:8px;font-weight:400;vertical-align:middle}

/* 感通算用四卡 */
.gtsw .card{border-top:4px solid var(--pl)}
.gtsw .card:nth-child(2){border-top-color:var(--accent)}
.gtsw .card:nth-child(3){border-top-color:var(--primary)}
.gtsw .card:nth-child(4){border-top-color:var(--primary-l40)}
.gtsw .zi{font-size:34px;font-weight:800;color:var(--primary-l80);line-height:1;
  margin-bottom:10px;font-family:KaiTi,STKaiti,serif}

/* 数据统计带 */
.stats{background:linear-gradient(120deg,var(--primary-d20),var(--primary));color:var(--white)}
.stats .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:52px 24px}
.stat{text-align:center}
.stat b{display:block;font-size:34px;color:var(--white);letter-spacing:1px}
.stat b small{font-size:18px}
.stat span{font-size:13.5px;color:var(--primary-l60)}

/* Logo 墙 */
.logo-wall{display:grid;grid-template-columns:repeat(7,1fr);gap:14px}
.logo-tile{background:var(--white);border:1px solid var(--line-soft);border-radius:8px;
  height:74px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:3px;padding:8px;filter:grayscale(1);opacity:.82;transition:all .3s;text-align:center}
.logo-tile:hover{filter:grayscale(0);opacity:1;border-color:var(--pl-l20);box-shadow:var(--shadow)}
.logo-tile b{font-size:13.5px;color:var(--primary);letter-spacing:.5px}
.logo-tile span{font-size:10.5px;color:var(--mute);line-height:1.3;max-width:100%;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

/* 新闻列表 */
.news-list{display:flex;flex-direction:column;gap:16px}
.news-item{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;
  background:var(--white);border:1px solid var(--line-soft);border-radius:var(--radius);
  padding:20px 24px;transition:all .3s}
.news-item:hover{border-color:var(--pl-l20);box-shadow:var(--shadow)}
.news-item h3{font-size:16.5px;color:var(--primary);margin-bottom:6px}
.news-item p{font-size:13.5px;color:var(--mute)}
.news-item time{flex:none;font-size:13px;color:var(--mute-l30);padding-top:3px}

/* CTA 带 */
.cta-band{background:linear-gradient(120deg,var(--primary),var(--pl));color:var(--white);
  border-radius:14px;padding:52px 48px;display:flex;justify-content:space-between;
  align-items:center;gap:32px;flex-wrap:wrap}
.cta-band h2{font-size:26px;letter-spacing:1px}
.cta-band p{color:var(--primary-l70);margin-top:8px}
.cta-band .btn-a{color:var(--ink)}
.cta-band .btn-o{color:var(--white);border-color:var(--primary-l60)}

/* ---------------- 表格 ---------------- */
.table-wrap{overflow-x:auto;border:1px solid var(--line-soft);border-radius:var(--radius)}
table.t{width:100%;border-collapse:collapse;background:var(--white);min-width:560px}
table.t th{background:var(--primary);color:var(--white);font-size:14px;padding:12px 16px;
  text-align:left;letter-spacing:1px;white-space:nowrap}
table.t td{padding:12px 16px;border-top:1px solid var(--line-soft);font-size:14px;
  color:var(--ink);vertical-align:top}
table.t tr:nth-child(even) td{background:var(--primary-l95)}
table.t td:first-child{font-weight:700;color:var(--primary);white-space:nowrap}
table.t td .val{color:var(--accent-d20);font-weight:700}

/* ---------------- 产品页筛选 ---------------- */
.filters{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:40px}
.fbtn{border:1px solid var(--line);background:var(--white);color:var(--mute);
  border-radius:999px;padding:7px 22px;font-size:14px;cursor:pointer;transition:all .25s}
.fbtn:hover{border-color:var(--pl);color:var(--pl)}
.fbtn.on{background:var(--primary);border-color:var(--primary);color:var(--white);font-weight:700}

/* 产品卡 */
.pcard{position:relative;overflow:hidden}
.pcard .layer{position:absolute;top:0;right:0;font-size:11.5px;background:var(--pl-l90);
  color:var(--pl-d20);padding:3px 12px;border-radius:0 0 0 8px;letter-spacing:1px}
.pcard .layer.a{background:var(--accent-l90);color:var(--accent-d40)}

/* 架构图（文字版） */
.arch{display:flex;flex-direction:column;gap:10px}
.arch-row{display:grid;gap:10px;align-items:stretch}
.arch-box{border-radius:8px;padding:14px 18px;font-size:14px;border:1.5px solid}
.arch-box b{display:block;font-size:15px;margin-bottom:4px}
.arch-app{background:var(--accent-l90);border-color:var(--accent-l80);color:var(--accent-d40)}
.arch-eng{background:var(--pl-l90);border-color:var(--pl-l80);color:var(--pl-d40)}
.arch-base{background:var(--primary-l95);border-color:var(--primary-l80);color:var(--primary)}
.arch-market{background:var(--white);border-color:var(--accent);color:var(--accent-d40)}
.arch-sec{background:var(--white);border:1.5px dashed var(--alert);color:var(--alert-d20);
  text-align:center;font-weight:700}
.arch-band{text-align:center;font-size:12.5px;font-weight:700;letter-spacing:2px;
  color:var(--accent-d40);padding:2px 0 0}

/* 方案块 */
.sol-block{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--line-soft);
  border-radius:var(--radius);overflow:hidden;background:var(--white);margin-bottom:28px}
.sol-block>.txt{padding:34px 36px}
.sol-block>.pic{background:linear-gradient(135deg,var(--primary-l95),var(--pl-l90));
  display:flex;align-items:center;justify-content:center;min-height:280px;position:relative}
.sol-block>.pic .formula{text-align:center;padding:28px}
.sol-block>.pic .formula b{display:block;font-size:17px;color:var(--primary);letter-spacing:1px}
.sol-block>.pic .formula i{display:block;font-size:13px;color:var(--mute);font-style:normal;margin-top:8px}
.sol-block h3{font-size:22px;color:var(--primary)}
.sol-block .sub{color:var(--accent-d20);font-size:14px;font-weight:700;margin:6px 0 16px}
.sol-block h4{font-size:14px;color:var(--accent-d40);letter-spacing:1px;margin:16px 0 6px}
.sol-block p{font-size:14px;color:var(--mute)}
.sol-block.rev{direction:rtl}
.sol-block.rev>*{direction:ltr}
.label-line{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.label-line .tag{margin-top:0}

/* 案例卡 */
.case-card .metric{font-size:22px;color:var(--accent-d20);font-weight:800;margin:8px 0 4px}
.case-card .metric small{display:block;font-size:12px;color:var(--mute);font-weight:400}

/* 时间轴 */
.timeline{position:relative;max-width:860px;margin:0 auto;padding-left:26px}
.timeline::before{content:"";position:absolute;left:7px;top:6px;bottom:6px;width:2px;
  background:var(--pl-l80)}
.tl-item{position:relative;padding:0 0 30px 22px}
.tl-item::before{content:"";position:absolute;left:-26px;top:7px;width:12px;height:12px;
  border-radius:50%;background:var(--accent);border:3px solid var(--white);
  box-shadow:0 0 0 2px var(--accent-l80)}
.tl-item time{font-size:14px;font-weight:800;color:var(--accent-d40);letter-spacing:1px}
.tl-item h4{font-size:16px;color:var(--primary);margin:4px 0}
.tl-item p{font-size:14px;color:var(--mute)}

/* 表单 */
.form{max-width:640px;margin:0 auto}
.form .row{margin-bottom:18px}
.form label{display:block;font-size:14px;font-weight:700;color:var(--primary);margin-bottom:8px}
.form label .req{color:var(--alert)}
.form input,.form textarea{width:100%;border:1px solid var(--surface-d20);border-radius:6px;
  padding:11px 14px;font-size:15px;font-family:inherit;color:var(--ink);background:var(--white);
  transition:border .25s}
.form input:focus,.form textarea:focus{outline:none;border-color:var(--accent)}
.form .err{display:none;font-size:12.5px;color:var(--alert);margin-top:5px}
.form .row.bad input{border-color:var(--alert)}
.form .row.bad .err{display:block}
.form-ok{display:none;background:var(--accent-l90);border:1px solid var(--accent-l80);
  color:var(--accent-d40);border-radius:6px;padding:12px 16px;font-size:14px;margin-top:14px}

/* FAQ */
.faq{max-width:860px;margin:0 auto}
.faq-item{border:1px solid var(--line-soft);border-radius:8px;margin-bottom:12px;
  background:var(--white);overflow:hidden}
.faq-q{width:100%;display:flex;justify-content:space-between;align-items:center;gap:14px;
  padding:16px 20px;background:none;border:none;cursor:pointer;font-size:15.5px;
  font-weight:700;color:var(--primary);text-align:left;font-family:inherit}
.faq-q .arr{transition:transform .3s;color:var(--accent-d20);font-size:13px}
.faq-item.open .faq-q .arr{transform:rotate(180deg)}
.faq-a{display:none;padding:0 20px 16px;font-size:14px;color:var(--mute)}
.faq-item.open .faq-a{display:block}

/* 详情页锚点小节 */
.anchor-sec{padding:34px 0;border-bottom:1px solid var(--line-soft)}
.anchor-sec:first-of-type{border-top:1px solid var(--line-soft)}
.anchor-sec h3{font-size:21px;color:var(--primary);margin-bottom:6px}
.anchor-sec h3 .hash{color:var(--accent);font-size:15px;margin-right:8px}
.anchor-sec .sub{color:var(--mute);font-size:14px;margin-bottom:18px}

/* 侧栏目录 */
.side-toc{position:fixed;right:18px;bottom:90px;z-index:900;background:var(--white);
  border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow-lg);
  padding:12px 14px;font-size:13px;display:flex;flex-direction:column;gap:2px}
.side-toc b{font-size:12px;color:var(--mute);letter-spacing:1px;margin-bottom:4px}
.side-toc a{padding:4px 8px;border-radius:5px;color:var(--ink)}
.side-toc a:hover{background:var(--pl-l90);color:var(--primary)}
.float-cta{position:fixed;right:18px;bottom:20px;z-index:900}

/* 搜索页 */
.search-box{display:flex;gap:10px;max-width:720px;margin:0 auto 34px}
.search-box input{flex:1;border:2px solid var(--line);border-radius:8px;padding:12px 16px;
  font-size:15px}
.search-box input:focus{outline:none;border-color:var(--accent)}
.sr{border-bottom:1px solid var(--line-soft);padding:18px 4px}
.sr h3{font-size:16.5px}
.sr .from{font-size:12.5px;color:var(--mute-l30);margin-top:4px}
.sr p{font-size:14px;color:var(--mute);margin-top:6px}
mark{background:var(--accent-l80);color:var(--ink);padding:0 2px;border-radius:2px}
.history{max-width:720px;margin:0 auto 20px;font-size:13px;color:var(--mute);
  display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.history .tag{cursor:pointer}
.empty-state{text-align:center;padding:60px 20px;color:var(--mute)}
.empty-state b{display:block;font-size:18px;color:var(--primary);margin-bottom:8px}

/* 错误页 */
.err-page{min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center;
  background:var(--surface)}
.err-page .code{font-size:88px;font-weight:800;color:var(--pl-l80);line-height:1}
.err-page h1{font-size:26px;color:var(--primary);margin:16px 0 10px}
.err-page p{color:var(--mute)}
.err-page .btns{display:flex;gap:14px;justify-content:center;margin-top:28px;flex-wrap:wrap}

/* Cookie 弹窗 */
.cookie-bar{position:fixed;left:16px;right:16px;bottom:16px;z-index:1500;background:var(--white);
  border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow-lg);
  padding:18px 22px;display:none;gap:16px;align-items:center;flex-wrap:wrap}
.cookie-bar.show{display:flex}
.cookie-bar p{flex:1;font-size:13.5px;color:var(--mute);min-width:260px}
.cookie-bar .btn{padding:8px 18px;font-size:13.5px}

/* ---------------- 页脚 ---------------- */
footer{background:var(--primary-d40);color:var(--primary-l60);margin-top:72px}
.foot-in{max-width:1200px;margin:0 auto;padding:52px 24px 30px;display:grid;
  grid-template-columns:2fr 1fr 1fr 1.4fr;gap:36px}
.foot-in h4{color:var(--white);font-size:14.5px;letter-spacing:1px;margin-bottom:14px}
.foot-in p,.foot-in li{font-size:13.5px;line-height:2}
.foot-in ul{list-style:none}
.foot-in a{color:var(--primary-l60)}
.foot-in a:hover{color:var(--white)}
.foot-brand .logo-t{color:var(--white)}
.foot-brand .logo-s{color:var(--primary-l40)}
.foot-bottom{border-top:1px solid rgba(255,255,255,.12)}
.foot-bottom-in{max-width:1200px;margin:0 auto;padding:16px 24px;display:flex;
  justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:12.5px}
.foot-bottom a{color:var(--primary-l40)}

/* ---------------- 响应式 ---------------- */
@media (max-width:1024px){
  .g4{grid-template-columns:repeat(2,1fr)}
  .logo-wall{grid-template-columns:repeat(4,1fr)}
  .stats .wrap{grid-template-columns:repeat(2,1fr)}
  .foot-in{grid-template-columns:1fr 1fr}
}
@media (max-width:860px){
  .menu,.nav-right .icon-btn,.nav-right .btn{display:none}
  .hamburger{display:flex}
  .g3{grid-template-columns:1fr}
  .g2{grid-template-columns:1fr}
  .sol-block{grid-template-columns:1fr}
  .sol-block>.pic{min-height:180px;order:-1}
  .banner h1{font-size:32px}
  .banner .btns .btn{width:100%}
  .side-toc{display:none}
  .cta-band{padding:36px 26px}
  .section{padding:52px 0}
}
@media (max-width:560px){
  .g4{grid-template-columns:1fr}
  .logo-wall{grid-template-columns:repeat(2,1fr)}
  .foot-in{grid-template-columns:1fr}
  .banner-in{padding:64px 18px}
}
"""

JS = """/* 天元官网全局脚本 */
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
    var phoneOk=/^1[3-9]\\d{9}$/.test(pv)||/^(0\\d{2,3}-?)?\\d{7,8}$/.test(pv);
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
    try{return esc(text).replace(new RegExp(kw.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&'),'gi'),function(m){return '<mark>'+m+'</mark>';});}
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
"""

# ============================================================ 公共模板
NAV_ITEMS = [
    ("index.html", "首页"),
    ("products.html", "产品与能力"),
    ("solutions.html", "解决方案"),
    ("cases.html", "客户案例"),
    ("about.html", "关于我们"),
    ("news.html", "新闻动态"),
    ("contact.html", "联系我们"),
]

ORG = "中国航天科技集团 · 卫星应用创新研究院"
ICP = "京ICP备XXXXXXXX号"  # 占位，上线前替换为实际备案号

def head(title, desc, active):
    menu = ""
    for url, name in NAV_ITEMS:
        menu += '<li%s><a href="%s">%s</a></li>' % (
            ' class="on"' if url == active else "", url, name)
    drawer = ""
    for url, name in NAV_ITEMS:
        drawer += '<li><a href="%s"%s>%s</a></li>' % (
            url, ' class="on"' if url == active else "", name)
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s | 天元 TIANYUAN</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s | 天元 TIANYUAN">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body>
<nav class="nav">
  <div class="nav-in">
    <a class="logo" href="index.html" aria-label="天元首页">
      <div class="logo-m"></div>
      <div><div class="logo-t">天元</div><div class="logo-s">TIANYUAN · DISOps</div></div>
    </a>
    <ul class="menu">%s</ul>
    <div class="nav-right">
      <a class="icon-btn" href="search.html" title="站内搜索" aria-label="站内搜索">&#128269;</a>
      <a class="btn btn-p" href="contact.html">申请演示</a>
      <button class="hamburger" aria-label="打开菜单"><i></i><i></i><i></i></button>
    </div>
  </div>
</nav>
<div class="drawer-mask"></div>
<aside class="drawer" aria-label="移动端导航菜单">
  <div class="drawer-h"><b>天元 · 导航菜单</b><button class="drawer-close" aria-label="关闭菜单">&times;</button></div>
  <ul>%s</ul>
  <div class="drawer-f">
    <button class="drawer-back" type="button">&#8249; 返回顶部导航</button>
    <a class="btn btn-p btn-w" href="contact.html">申请演示</a>
  </div>
</aside>
""" % (title, desc, title, desc, menu, drawer)

FOOT = """
<footer>
  <div class="foot-in">
    <div class="foot-brand">
      <div class="logo" style="margin-bottom:12px">
        <div class="logo-m"></div>
        <div><div class="logo-t">天元</div><div class="logo-s">TIANYUAN · DISOps</div></div>
      </div>
      <p>面向数智技术场景化闭环的一站式信息服务平台，解决数智应用“最后一公里”问题，构建“数据-认知-决策-行动”价值闭环。</p>
      <p style="margin-top:10px">%s</p>
    </div>
    <div>
      <h4>快速导航</h4>
      <ul>
        <li><a href="products.html">产品与能力</a></li>
        <li><a href="solutions.html">解决方案</a></li>
        <li><a href="cases.html">客户案例</a></li>
        <li><a href="news.html">新闻动态</a></li>
      </ul>
    </div>
    <div>
      <h4>关于我们</h4>
      <ul>
        <li><a href="about.html">研究院简介</a></li>
        <li><a href="about.html#history">发展历程</a></li>
        <li><a href="careers.html">加入我们</a></li>
        <li><a href="contact.html">联系我们</a></li>
      </ul>
    </div>
    <div>
      <h4>联系方式</h4>
      <ul>
        <li>电话：010-XXXX XXXX <span style="opacity:.6">（占位）</span></li>
        <li>邮箱：contact@example.com <span style="opacity:.6">（占位）</span></li>
        <li>地址：北京市海淀区 <span style="opacity:.6">（占位）</span></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <div class="foot-bottom-in">
      <span>© <span id="yr">2026</span> %s</span>
      <span>
        <a href="legal.html#privacy">隐私政策</a> ·
        <a href="legal.html#terms">服务条款</a> ·
        <a href="legal.html#cookie">Cookie 声明</a> ·
        <a href="sitemap.html">网站地图</a> ·
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">%s</a>
      </span>
    </div>
  </div>
</footer>
<div class="cookie-bar" id="cookie-bar" role="dialog" aria-label="Cookie 使用提示">
  <p>本站使用必要 Cookie 保障站点正常运行，并使用本地存储记录您的偏好（如搜索历史、Cookie 选择），不做服务端个人数据记录。您可以选择“仅必要”。</p>
  <button class="btn btn-p" id="cookie-accept">仅必要</button>
  <a class="btn btn-o" href="legal.html#cookie">了解更多</a>
</div>
<script src="assets/main.js"></script>
</body>
</html>
""" % (ORG, ORG, ICP)

def page(fname, title, desc, active, body, extra_head=""):
    html = head(title, desc, active).replace("</head>", extra_head + "\n</head>")
    html += body + FOOT
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("written", fname)

# ============================================================ 首页
INDEX_BODY = """
<header class="banner">
  <div class="banner-in">
    <span class="badge">感通算用 · 一体化综合信息服务</span>
    <h1>让数智技术<br>真正<em>落地行业</em></h1>
    <p class="lead">天元（DISOps）是面向数智技术场景化闭环的<b>一站式信息服务平台</b>，旨在解决数智应用“最后一公里”问题，快速构建和持续优化<b>“数据-认知-决策-行动”价值闭环</b>的数智系统，助力行业应用智能升级。</p>
    <div class="btns">
      <a class="btn btn-a btn-lg" href="products.html">了解平台能力</a>
      <a class="btn btn-o btn-lg" href="contact.html">预约演示</a>
    </div>
  </div>
</header>

<section class="section" id="gtsw">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">感 · 通 · 算 · 用</span>
      <h2>“感通算用”智能技术应用框架</h2>
      <p>融合感知、认知、具身等智能技术，实现“认知-行动”场景化智能闭环，解决AI技术行业应用的最后一公里问题，实现卫星应用向天空地融合信息服务延伸与拓展。</p>
    </div>
    <div class="grid g4 gtsw">
      <div class="card">
        <div class="zi">感</div>
        <h3>物理感知与观测</h3>
        <p>物理世界的“感知系统”，将观测结果识别为结构化信息，解决物理世界“存在什么／发生了什么？”的问题。</p>
      </div>
      <div class="card">
        <div class="zi">通</div>
        <h3>信息传输与贯通</h3>
        <p>信息及服务流程的“路由枢纽”，解决天空地信息传输、感知-认知-具身应用的流程贯通问题。</p>
      </div>
      <div class="card">
        <div class="zi">算</div>
        <h3>认知计算与决策</h3>
        <p>认知-行动的“智能中枢”，理解业务语义与用户意图，预测、模拟发展态势，规划、编排行动方案，解决“意味着什么／应该怎么办？”的问题。</p>
      </div>
      <div class="card">
        <div class="zi">用</div>
        <h3>具身应用与赋能</h3>
        <p>知行合一的“具身助手”，驱动具身系统、装备自主执行任务，解决研判、决策在物理空间行动闭环的问题。</p>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">服务模式</span>
      <h2>三个转变，交付可进化的智能价值</h2>
      <p>从模型供给到解决方案服务，从单点能力到智能协同，从标品交付到价值交付。</p>
    </div>
    <div class="grid g3">
      <div class="card">
        <div class="ico">&#128260;</div>
        <h3>从模型供给到解决方案服务</h3>
        <p>提供纳管和编排领域数据、算法、工具的数智系统解决方案构建能力，实现从“模型即服务”到“解决方案即服务”的转变。</p>
      </div>
      <div class="card">
        <div class="ico accent">&#129309;</div>
        <h3>从单点能力到智能协同</h3>
        <p>提供感知、认知、具身等智能技术融合与协同应用，快速适配用户场景、持续优化智能系统。</p>
      </div>
      <div class="card">
        <div class="ico deep">&#127919;</div>
        <h3>从标品交付到价值交付</h3>
        <p>所见即所得的场景化运行效果，实现从“交付工具和标品”到“交付价值”和“可持续进化的智能能力”的转变，行业客户为结果买单，场景智能框架保障确定性价值交付。</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="engines">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">核心引擎</span>
      <h2>三大引擎，贯通天基信息到行动闭环</h2>
      <p>数智时代的AI应用，已从模型为中心转向场景为中心。天元突破传统AI技术的特征工程、模型工程局限，从场景理解需求、由需求形成方案。</p>
    </div>
    <div class="grid g3">
      <div class="card">
        <div class="num">01</div>
        <h3>空天地数据融合引擎</h3>
        <p>以空天地一体化数据源为核心，快速获取、治理与融合卫星遥感、无人机、物联网等多源数据，并通过星地链路、5G/专网、边缘组网自适应切换保障传输，让天基数据直达业务。</p>
        <div class="tags"><span class="tag">天元·灵观</span><span class="tag">天元·灵数</span><span class="tag">空天地一体化网络</span></div>
        <a class="more" href="product-detail.html#fusion">了解详情 →</a>
      </div>
      <div class="card">
        <div class="num">02</div>
        <h3>认知计算与决策引擎</h3>
        <p>以本体建模读懂业务，以模型工厂和智能体工厂持续生产模型与智能体，并由认知计算引擎统一调度数据、模型、智能体与 Skill，形成从数据到决策的流程闭环。</p>
        <div class="tags"><span class="tag">天元·灵语</span><span class="tag">天元·灵炼</span><span class="tag">天元·灵智</span><span class="tag">认知计算引擎</span></div>
        <a class="more" href="product-detail.html#brain">了解详情 →</a>
      </div>
      <div class="card">
        <div class="num">03</div>
        <h3>具身智能行动执行引擎</h3>
        <p>面向无人机、无人车、机器狗等多类具身设备，实现统一调度与链路自适应下发，结合视觉增强完成厘米级精准作业，打通从决策到行动的最后一公里。</p>
        <div class="tags"><span class="tag">天元·灵动</span></div>
        <a class="more" href="product-detail.html#action">了解详情 →</a>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap">
    <div class="stat"><b>120<small>万+</small></b><span>闭源数据条目（安防摄像头、振动光纤、预警事件等）</span></div>
    <div class="stat"><b>20<small>余颗</small></b><span>在轨通信卫星 · 44 个地面站</span></div>
    <div class="stat"><b>1600<small>+</small></b><span>全球在轨对地观测卫星数据</span></div>
    <div class="stat"><b>30<small>余个</small></b><span>行业算法与控制组件</span></div>
    <div class="stat"><b>1000<small>+</small></b><span>船舶开源情报数据</span></div>
    <div class="stat"><b>5000<small>+</small></b><span>航空开源情报数据</span></div>
    <div class="stat"><b>1<small>套</small></b><span>多元数据融合资源库</span></div>
    <div class="stat"><b>1<small>个</small></b><span>数智服务工具箱</span></div>
  </div>
</section>

<section class="section alt" id="industries">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">行业应用</span>
      <h2>行业解决方案</h2>
      <p>基于平台核心能力，赋能多行业数智系统构建与智能升级。</p>
    </div>
    <div class="grid g4">
      <div class="card">
        <div class="ico">&#128225;</div>
        <h3>开源情报分析</h3>
        <p>认知计算＋多源数据，实现智能问数与态势空间呈现，从“翻报告”升级为“看图说话”。</p>
        <a class="more" href="solutions.html#intel">查看详情 →</a>
      </div>
      <div class="card">
        <div class="ico accent">&#127754;</div>
        <h3>海洋石油污染</h3>
        <p>信息融合与溯源分析，输出嫌疑船舶排序及证据链，服务执法取证与海洋环保。</p>
        <a class="more" href="solutions.html#oil">查看详情 →</a>
      </div>
      <div class="card">
        <div class="ico">&#9888;&#65039;</div>
        <h3>应急信息服务</h3>
        <p>自然语言交互自动拉取灾前灾后影像，支撑建筑物损毁、水体淹没范围对比分析。</p>
        <a class="more" href="solutions.html#emergency">查看详情 →</a>
      </div>
      <div class="card">
        <div class="ico deep">&#128737;&#65039;</div>
        <h3>智慧边防应用</h3>
        <p>大小模型协同＋无人装备，实现“数据、语义、决策、行动”场景智能业务闭环。</p>
        <a class="more" href="solutions.html#border">查看详情 →</a>
      </div>
    </div>
    <div class="sec-head" style="margin-top:44px;margin-bottom:20px">
      <h2 style="font-size:20px">更多行业场景</h2>
    </div>
    <div class="tags" style="justify-content:center">
      <span class="tag">新能源 · 智慧能源管理</span>
      <span class="tag">低空经济 · 低空态势感知</span>
      <span class="tag">海洋应用 · 智慧海洋监测</span>
      <span class="tag">林草生态 · 生态保护监测</span>
      <span class="tag">电网 · 智慧电网</span>
      <span class="tag">应急 · 智慧应急</span>
    </div>
  </div>
</section>

<section class="section" id="partners">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">合作生态</span>
      <h2>合作伙伴</h2>
      <p>与科研院所、高校及行业领军企业共建数智生态。</p>
    </div>
    <div class="logo-wall">
      <div class="logo-tile"><b>海康威视</b><span>杭州海康威视数字技术股份有限公司</span></div>
      <div class="logo-tile"><b>宇视科技</b><span>浙江宇视科技有限公司</span></div>
      <div class="logo-tile"><b>云深处科技</b><span>杭州云深处科技有限公司</span></div>
      <div class="logo-tile"><b>宇树科技</b><span>杭州宇树科技有限公司</span></div>
      <div class="logo-tile"><b>大疆创新</b><span>深圳市大疆创新科技有限公司</span></div>
      <div class="logo-tile"><b>浙江大学</b><span>Zhejiang University</span></div>
      <div class="logo-tile"><b>北京航空航天大学</b><span>Beihang University</span></div>
      <div class="logo-tile"><b>西安交通大学</b><span>Xi'an Jiaotong University</span></div>
      <div class="logo-tile"><b>北京理工大学</b><span>Beijing Institute of Technology</span></div>
      <div class="logo-tile"><b>北京邮电大学</b><span>Beijing University of Posts and Telecommunications</span></div>
      <div class="logo-tile"><b>中国空间技术研究院</b><span>航天五院</span></div>
      <div class="logo-tile"><b>航天空气动力技术研究院</b><span>航天十一院</span></div>
      <div class="logo-tile"><b>航天系统科学与工程研究院</b><span>体系院</span></div>
      <div class="logo-tile"><b>中国四维</b><span>中国四维测绘技术有限公司</span></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">新闻动态</span>
      <h2>最新动态</h2>
    </div>
    <div class="news-list">
      <a class="news-item" href="news.html">
        <div>
          <h3>天元平台完成 30 余个行业算法与控制组件纳管<span class="placeholder-note">示例内容</span></h3>
          <p>面向海洋、应急、边海防等典型场景，支撑行业数智系统的快速装配与持续优化……</p>
        </div>
        <time>2026-09-10</time>
      </a>
      <a class="news-item" href="news.html">
        <div>
          <h3>研究院与多家生态伙伴深化数智能力合作<span class="placeholder-note">示例内容</span></h3>
          <p>联合科研院所与高校，研发专用AI模型、遥感模型、智能体应用等组件……</p>
        </div>
        <time>2026-08-28</time>
      </a>
      <a class="news-item" href="news.html">
        <div>
          <h3>天元·灵语本体建模能力持续升级<span class="placeholder-note">示例内容</span></h3>
          <p>自动本体建模、Skill级业务操作，支持200+ AI动作，业务人员无需编程即可调用AI能力……</p>
        </div>
        <time>2026-08-15</time>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>联系我们，开启数智转型之旅</h2>
        <p>专业团队为您提供定制化数智系统解决方案</p>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn btn-a btn-lg" href="contact.html">立即咨询</a>
        <a class="btn btn-o btn-lg" href="solutions.html">查看解决方案</a>
      </div>
    </div>
  </div>
</section>
"""

# ============================================================ 产品总览
PRODUCTS = [
    # (名称, 层级分类, 一句话, 锚点)
    ("天元·智算底座", "base", "国产化、高性能的算力与数据存储支持，算力池化与统一资源管理，确保底层稳固。", "infra"),
    ("天元·灵观", "fusion", "天基数据获取，便捷获取卫星数据，AI简化任务需求，星地协同智能指挥，覆盖高、低轨卫星及44个全球地面站。", "fusion"),
    ("天元·灵数", "fusion", "数据治理与融合，智能数据治理，多源数据融合（卫星遥感、无人机、物联网），50+自动化管道。", "fusion"),
    ("空天地一体化网络", "fusion", "通信全流程保障，星地链路、5G/专网、边缘组网等多种通信方式自适应切换。", "fusion"),
    ("天元·灵语", "brain", "本体建模，自动本体建模，Skill级业务操作，支持200+ AI动作，业务人员无需编程即可调用AI能力。", "brain"),
    ("天元·灵炼", "brain", "模型工厂，数据在线AI标注，大模型后训练，增量训练与联邦学习，模型迭代周期从“月级”缩短至“周级”。", "brain"),
    ("天元·灵智", "brain", "智能体工厂，提供智能体开发、编排与运行能力，支持多智能体任务编排与自我进化。", "brain"),
    ("认知计算引擎", "brain", "智能体编排框架，自动调度数据、模型、智能体与Skill，实现信息服务的流程闭环。", "brain"),
    ("天元·灵动", "action", "具身智能调度，覆盖无人机、无人车、机器狗等多类具身设备，统一调度与精准作业。", "action"),
    ("天元·灵集", "market", "数智能力集散与流通平台，包含数智资产广场、智能体及技能广场。", "market"),
    ("天元·信息服务助手", "market", "行业信息服务的统一入口，提供通用智能问答、记忆、多轮对话等问答能力，可通过认知计算引擎在线体验与交互数智市集各类资产。", "market"),
    ("全栈安全合规", "sec", "身份与访问控制、数据安全与隐私、AI安全治理、行为审计与溯源，横向贯穿所有层级。", "security"),
]
CATS = [("all", "全部"), ("base", "智算底座"), ("fusion", "数据融合"), ("brain", "认知决策"), ("action", "行动执行"), ("market", "数智市集"), ("sec", "安全合规")]

PRODUCTS_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">产品与能力</span>
    <h1>一站式场景化数智平台</h1>
    <p class="lead">1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用，构建从空天地数据融合到认知决策、再到行动执行的全链路闭环智能系统。</p>
    <div class="btns"><a class="btn btn-a btn-lg" href="contact.html">申请演示</a></div>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="filters">
""" + "".join(
    '<button class="fbtn%s" data-f="%s">%s</button>' % (" on" if k == "all" else "", k, n)
    for k, n in CATS) + """
    </div>
    <div class="grid g3">
""" + "".join(
    '<div class="card pcard" data-cat="%s"><span class="layer%s">%s</span>'
    '<h3>%s</h3><p>%s</p>'
    '<a class="more" href="product-detail.html#%s">查看详情 →</a></div>'
    % (c, " a" if c in ("brain", "market") else "", dict(CATS)[c], name, desc, anchor)
    for name, c, desc, anchor in PRODUCTS) + """
    </div>
    <p style="text-align:center;color:var(--mute);font-size:13px;margin-top:28px">
      行业场景化解决方案（应急、海洋、边防、开源情报等）请见
      <a href="solutions.html">解决方案</a> 页面。
    </p>
  </div>
</section>
"""

# ============================================================ 产品详情
DETAIL_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">产品详情</span>
    <h1>天元平台</h1>
    <p class="lead">融合人工智能与智能体技术，实现从空天地数据融合到认知决策、再到行动执行的全链路闭环智能系统，为客户提供“感、通、算、用”一体化的数智化解决方案。</p>
    <div class="btns">
      <a class="btn btn-a btn-lg" href="contact.html">试用 / 咨询</a>
      <a class="btn btn-o btn-lg" href="solutions.html">查看行业方案</a>
    </div>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">差异化优势</span>
      <h2>与通用云平台不同，天元的四个核心差异</h2>
    </div>
    <div class="grid g4">
      <div class="card"><div class="ico">&#128752;</div><h3>空天地一体化数据源</h3><p>覆盖高、低轨卫星及44个全球地面站，实现天基数据直达业务。</p></div>
      <div class="card"><div class="ico accent">&#128279;</div><h3>全链路闭环</h3><p>从数据获取、治理、认知决策到终端执行，无需拼接多家供应商。</p></div>
      <div class="card"><div class="ico deep">&#127758;</div><h3>国产化全栈适配</h3><p>从算力底座到AI模型，满足自主可控要求。</p></div>
      <div class="card"><div class="ico">&#129302;</div><h3>智能体驱动</h3><p>多智能体任务编排与自我进化，让系统越用越聪明。</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">体系架构</span>
      <h2>1 个底座 + 3 大核心引擎 + 1 个数智市集 + 1 个安全体系 + N 个行业应用</h2>
    </div>
    <div class="arch">
      <div class="arch-row" style="grid-template-columns:repeat(5,1fr)">
        <div class="arch-box arch-app"><b>应急减灾</b>灾害应急响应</div>
        <div class="arch-box arch-app"><b>边防管控</b>预警发现与研判处置</div>
        <div class="arch-box arch-app"><b>海洋应用</b>污染溯源与态势监测</div>
        <div class="arch-box arch-app"><b>开源情报</b>智能问数与态势呈现</div>
        <div class="arch-box arch-app"><b>更多行业</b>能源 · 低空 · 林草 · 电网</div>
      </div>
      <div class="arch-row" style="grid-template-columns:1fr">
        <div class="arch-box arch-market"><b>数智市集 · 天元·灵集</b>数智资产广场 / 智能体及技能广场 / 天元·信息服务助手</div>
      </div>
      <div class="arch-row" style="grid-template-columns:1fr">
        <div class="arch-band">三大核心引擎</div>
      </div>
      <div class="arch-row" style="grid-template-columns:1fr 1fr 1fr">
        <div class="arch-box arch-eng"><b>空天地数据融合引擎</b>天元·灵观 / 天元·灵数 / 空天地一体化网络</div>
        <div class="arch-box arch-eng"><b>认知计算与决策引擎</b>天元·灵语 / 天元·灵炼 / 天元·灵智 / 认知计算引擎</div>
        <div class="arch-box arch-eng"><b>具身智能行动执行引擎</b>天元·灵动</div>
      </div>
      <div class="arch-row" style="grid-template-columns:1fr">
        <div class="arch-box arch-base"><b>基础设施层 · 天元·智算底座</b>智算集群 / 高速互联 / 边云协同，国产化全栈适配</div>
      </div>
      <div class="arch-row" style="grid-template-columns:1fr">
        <div class="arch-box arch-sec">全栈安全合规体系 —— 身份与访问控制 · 数据安全与隐私 · AI安全治理 · 行为审计与溯源（横向贯穿所有层级）</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">核心功能</span><h2>分层能力详解</h2></div>

    <div class="anchor-sec" id="infra">
      <h3><span class="hash">◆</span>基础设施层：边云协同与智算底座</h3>
      <p class="sub">核心价值：提供国产化、高性能的算力与数据存储支持，确保底层稳固。</p>
      <div class="table-wrap"><table class="t">
        <tr><th>模块</th><th>内容要点</th><th>客户价值</th></tr>
        <tr><td>智算集群</td><td>支持国产全栈适配，提供算力池化与统一资源管理</td><td><span class="val">算力资源利用率提升30%+</span>，支持弹性扩容</td></tr>
        <tr><td>高速互联</td><td>RDMA高速互联网络，分布式并行存储</td><td>训练效率提升50%，存储吞吐达TB级</td></tr>
        <tr><td>边云协同</td><td>支持云端训练与边缘端推理的无缝协同</td><td>边缘推理延迟≤50ms，带宽成本降低40%</td></tr>
      </table></div>
      <p style="font-size:12.5px;color:var(--mute);margin-top:8px">注：客户价值指标来自《产品详情V1.2》设计口径，正式对外发布前建议由产品部门复核基准与来源。</p>
    </div>

    <div class="anchor-sec" id="fusion">
      <h3><span class="hash">◆</span>数据融合层：空天地数据融合</h3>
      <p class="sub">核心价值：解决“数据从哪来”的问题，实现多源异构数据的快速获取、治理与融合。</p>
      <div class="table-wrap"><table class="t">
        <tr><th>模块</th><th>内容要点</th><th>客户价值</th></tr>
        <tr><td>天元·灵观</td><td>天基数据获取。便捷获取卫星数据，AI简化任务需求，星地协同智能指挥。覆盖高、低轨卫星及44个全球地面站</td><td>卫星数据获取周期从“天级”缩短至“小时级”</td></tr>
        <tr><td>天元·灵数</td><td>数据治理与融合。智能数据治理，多源数据融合（卫星遥感、无人机、物联网），沉淀20+数据集，拥有50+自动化管道</td><td>数据治理人工干预减少60%，多源数据融合效率提升3倍</td></tr>
      </table></div>
      <h4 style="margin-top:18px;color:var(--primary)">空天地一体化网络</h4>
      <p style="font-size:14px;color:var(--mute);margin-top:6px">通信全流程保障，确保数据传输的高带宽与低延迟。支持星地链路、5G/专网、边缘组网等多种通信方式自适应切换。</p>
    </div>

    <div class="anchor-sec" id="brain">
      <h3><span class="hash">◆</span>认知决策层：认知计算与智能决策</h3>
      <p class="sub">核心价值：解决“数据怎么用”的问题，通过AI让机器读懂业务，进行深度研判，并持续生产可复用的本体、模型与智能体。</p>
      <div class="table-wrap"><table class="t">
        <tr><th>模块</th><th>内容要点</th><th>客户价值</th></tr>
        <tr><td>天元·灵语</td><td>本体建模。自动本体建模，Skill级业务操作，支持200+ AI动作；构建行业知识建模、时空本体建模、图谱推理与因果分析</td><td>业务人员无需编程即可调用AI能力</td></tr>
        <tr><td>天元·灵炼</td><td>模型工厂。数据在线AI标注，大模型后训练，完成7项应用模型，支持增量训练与联邦学习</td><td>模型迭代周期从“月级”缩短至“周级”</td></tr>
        <tr><td>天元·灵智</td><td>智能体工厂。提供智能体开发、编排与运行能力，支持多智能体任务编排与自我进化</td><td>智能体开发效率提升，业务场景快速落地</td></tr>
        <tr><td>认知计算引擎</td><td>智能体编排框架。能够自动调度数据、模型、智能体与Skill，实现信息服务的流程闭环</td><td>为上层应用提供统一的能力调度与编排支撑，实现端到端流程闭环</td></tr>
      </table></div>
    </div>

    <div class="anchor-sec" id="action">
      <h3><span class="hash">◆</span>行动执行层：具身智能 AI 调度</h3>
      <p class="sub">核心价值：解决“指令怎么执行”的问题，实现无人设备的智能化调度与管控。</p>
      <div class="table-wrap"><table class="t">
        <tr><th>模块</th><th>内容要点</th><th>客户价值</th></tr>
        <tr><td>天元·灵动</td><td>具身智能调度。覆盖无人机、无人车、机器狗等多类具身设备；统一调度，链路自适应下发；具备视觉增强，支持小、中、大覆盖半径（作业面积5m²–100km²）的精准作业</td><td>多设备协同效率提升50%，调度响应≤1s；作业精度提升至厘米级，人力成本降低70%</td></tr>
      </table></div>
    </div>

    <div class="anchor-sec" id="market">
      <h3><span class="hash">◆</span>数智市集：天元·灵集</h3>
      <p class="sub">核心价值：作为数智能力的集散与流通平台，连接能力供给与业务消费。</p>
      <div class="grid g3" style="margin-top:8px">
        <div class="card"><h3>数智资产广场</h3><p>汇聚数据集、本体、算法、模型等数字资产，支持上架、检索与复用。</p></div>
        <div class="card"><h3>智能体及技能广场</h3><p>汇聚智能体、Skill、Workflow等，支持按需调用。</p></div>
        <div class="card"><h3>天元·信息服务助手</h3><p>行业信息服务的统一入口，提供通用智能问答、记忆、多轮对话等问答能力，可通过认知计算引擎在线对数智市集中的各类资产进行体验与交互。</p></div>
      </div>
    </div>

    <div class="anchor-sec" id="security">
      <h3><span class="hash">◆</span>安全支撑体系：全栈安全合规</h3>
      <p class="sub">核心价值：横向贯穿所有层级，提供全流程安全保障。</p>
      <div class="grid g4" style="margin-top:8px">
        <div class="card"><h3>身份与访问控制</h3><p>统一身份，分级授权。</p></div>
        <div class="card"><h3>数据安全与隐私</h3><p>加密脱敏，数据不出域，密级流转。</p></div>
        <div class="card"><h3>AI安全治理</h3><p>抗注入，模型可信赖，对抗防护。</p></div>
        <div class="card"><h3>行为审计与溯源</h3><p>全链路审计，操作可追溯。</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">应用场景</span><h2>典型场景</h2></div>
    <div class="grid g3">
      <div class="card"><h3>边防预警与研判处置</h3><p>多元信息融合的态势感知、预警发现、研判处置，无人装备协同闭环。</p><a class="more" href="solutions.html#border">查看方案 →</a></div>
      <div class="card"><h3>海洋污染溯源分析</h3><p>油膜识别与起始点反演，输出嫌疑船舶排序及证据链。</p><a class="more" href="solutions.html#oil">查看方案 →</a></div>
      <div class="card"><h3>灾害应急对比分析</h3><p>自然语言拉取灾前灾后影像，建筑物损毁、水体淹没范围对比。</p><a class="more" href="solutions.html#emergency">查看方案 →</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">相关资源</span><h2>文档下载</h2></div>
    <div class="grid g3">
      <div class="card"><h3>📄 平台白皮书</h3><p>PDF · 约 8MB<span class="placeholder-note">待提供</span></p></div>
      <div class="card"><h3>📄 产品规格书</h3><p>PDF · 约 3MB<span class="placeholder-note">待提供</span></p></div>
      <div class="card"><h3>📄 API 文档</h3><p>在线文档<span class="placeholder-note">待提供</span></p></div>
    </div>
  </div>
</section>

<div class="side-toc" aria-label="页面目录">
  <b>本页目录</b>
  <a href="#infra">智算底座</a>
  <a href="#fusion">数据融合</a>
  <a href="#brain">认知决策</a>
  <a href="#action">行动执行</a>
  <a href="#market">数智市集</a>
  <a href="#security">安全体系</a>
</div>
<div class="float-cta"><a class="btn btn-p" href="contact.html">快速咨询</a></div>

<section class="section alt">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>获取完整产品资料</h2><p>留下联系方式，我们的团队将在 1 个工作日内与您联系</p></div>
      <a class="btn btn-a btn-lg" href="contact.html">咨询 / 试用</a>
    </div>
  </div>
</section>
"""

# ============================================================ 解决方案
def sol_block(anchor, title, formula, formula_note, scene, solution, promote, tags, rev=False):
    cls = "sol-block rev" if rev else "sol-block"
    return """
<div class="%s" id="%s">
  <div class="txt">
    <h3>%s</h3>
    <div class="sub">%s</div>
    <h4>业务场景（痛点）</h4>
    <p>%s</p>
    <h4>解决方案</h4>
    <p>%s</p>
    <h4>应用推广（适用客户）</h4>
    <p>%s</p>
    <div class="label-line">%s</div>
  </div>
  <div class="pic">
    <div class="formula">
      <b>%s</b>
      <i>%s</i>
      <div class="tags" style="justify-content:center;margin-top:18px"><span class="tag">基于天元核心能力</span></div>
    </div>
  </div>
</div>""" % (cls, anchor, title, formula, scene, solution, promote, tags, formula_note, "")

SOLUTIONS_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">解决方案</span>
    <h1>行业解决方案</h1>
    <p class="lead">基于平台核心能力，赋能多行业数智系统构建与智能升级。</p>
  </div>
</header>

<section class="section">
  <div class="wrap">
""" + sol_block(
    "intel", "开源情报分析",
    "认知计算 ＋ 多源数据 ＝ 智能问数与态势空间呈现",
    "碎片化信息聚合为一张态势图",
    "开源情报来源多、规模大，应用门槛高、周期长。",
    "“认知计算＋多源数据”快速形成数据应用能力，汇聚船舶AIS、灾害通报、飞机航线等多源开源情报数据，通过认知计算引擎理解自然语言的意图，实现开源情报的智能检索与空间可视化，自动关联时空坐标，将碎片化信息聚合为一张态势图。",
    "基于开源情报的态势研判与呈现，从“翻报告”“跨系统人工查询”升级为“看图说话”。在国防安全、海事监管、应急救援等领域，可快速部署于现有情报流程中，作为情报分析的重要手段。",
    '<span class="tag">国防安全</span><span class="tag">海事监管</span><span class="tag">应急救援</span>') + sol_block(
    "oil", "海洋石油污染",
    "认知计算 ＋ 多源数据 ＋ 专用算法 ＝ 信息融合与溯源分析",
    "输出嫌疑船舶排序及证据链",
    "跨部门、跨系统的人工调查、数据查询与比对，效率低、周期长、信息融合不充分。",
    "“认知计算＋多源数据＋专用算法”快速实现多源数据处理与信息融合分析流程，以认知智能技术引擎为中枢，融合天基历史遥感影像、气象海流数据、船舶AIS轨迹等多源信息，内置油膜识别、油膜起始点反演、船舶特征分析等专用算法，输出嫌疑船舶排序及证据链。",
    "面向海洋环保监管部门、海事调查机构、海警巡查及石油企业，多元信息融合、可追溯，可作为执法取证、海洋环保等场景的信息服务工具。",
    '<span class="tag">海洋环保监管</span><span class="tag">海事调查</span><span class="tag">海警巡查</span><span class="tag">石油企业</span>', rev=True) + sol_block(
    "emergency", "应急信息服务",
    "认知计算 ＋ 多源数据 ＋ 专用算法 ＋ 多模态大模型 ＝ 信息融合与场景分析",
    "灾前灾后影像对比 · 要素级变化检测",
    "天基信息服务对使用者专业要求高，跨系统数据获取难、周期长。",
    "实现流程化信息融合、场景化分析能力，汇聚互联网灾情情报、开源或闭源天基历史与实时影像，集成变化检测等算法。以自然语言交互方式，可自动拉取灾前灾后影像，进行建筑物损毁、水体淹没范围等要素的对比分析。",
    "面向应急管理与救援、地方政府防灾减灾等非专业人员，简化天基信息应用，与现有应急指挥系统对接，可作为灾害应急响应信息服务能力补充。",
    '<span class="tag">应急管理</span><span class="tag">应急救援</span><span class="tag">地方防灾减灾</span>') + sol_block(
    "border", "智慧边防应用",
    "认知计算 ＋ 多源数据 ＋ 大小模型协同 ＋ 无人装备 ＝ 语义理解与智能决策",
    "“数据、语义、决策、行动”场景智能业务闭环",
    "跨系统、异构数据无法协同发挥价值；预警提前发现能力弱，虚警误报率高、存在漏报风险；管理、操作复杂，缺少多元信息融合的态势感知、预警发现、研判处置手段。",
    "天空地多源数据跨域整合，形成行业数据底座，涵盖枪球机摄像头、振动光纤、高压脉冲、无人设备、数字地图等数据。构建边防专用数据集，研发大小模型协同的语义理解框架，增强场景化预警发现能力。基于认知计算实现智能问数、报告生成、预警处置，实现“数据、语义、决策、行动”场景智能的业务闭环。",
    "面向边防管理部门、出入境检查机构及边境安全相关单位，预警响应速度大幅提升，人力投入显著降低，适用于陆地边境、海岸线、口岸等多种场景的智能化升级。",
    '<span class="tag">边防管理</span><span class="tag">出入境检查</span><span class="tag">边境安全</span>', rev=True) + """
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">更多行业场景</span>
      <h2>持续拓展中</h2>
      <p>以下场景能力建设中，欢迎与我们探讨合作方向。</p>
    </div>
    <div class="grid g3">
      <div class="card"><h3>新能源 · 智慧能源管理</h3><p>能源资产监测与智能调度。</p></div>
      <div class="card"><h3>低空经济 · 低空态势感知</h3><p>低空飞行活动监测与管理。</p></div>
      <div class="card"><h3>海洋应用 · 智慧海洋监测</h3><p>海洋环境与活动持续观测。</p></div>
      <div class="card"><h3>林草生态 · 生态保护监测</h3><p>林草资源与生态变化监测。</p></div>
      <div class="card"><h3>电网 · 智慧电网</h3><p>电网设施巡检与风险预警。</p></div>
      <div class="card"><h3>应急 · 智慧应急</h3><p>灾害预警与应急响应支撑。</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>预约行业顾问，获取定制方案</h2><p>告诉我们您所在行业与场景痛点，我们为您匹配对应解决方案</p></div>
      <a class="btn btn-a btn-lg" href="contact.html">获取定制方案</a>
    </div>
  </div>
</section>
"""

# ============================================================ 案例
CASES = [
    # (标题, 行业cat, 简介, 成果, 状态tag)
    ("智慧边防应用 · 陆地边境场景", "border", "天空地多源数据跨域整合形成行业数据底座，大小模型协同语义理解，实现预警发现、智能问数、报告生成与无人装备协同处置的业务闭环。",
     "预警响应速度大幅提升 · 人力投入显著降低", "实战应用"),
    ("海洋石油污染溯源分析", "ocean", "融合天基历史遥感影像、气象海流数据、船舶AIS轨迹等多源信息，内置油膜识别、起始点反演等专用算法，输出嫌疑船舶排序及证据链。",
     "嫌疑船舶排序与证据链输出 · 多元信息可追溯", "试点应用"),
    ("应急信息服务对接演练", "emergency", "以自然语言交互自动拉取灾前灾后影像，进行建筑物损毁、水体淹没范围等要素对比分析，与现有应急指挥系统对接。",
     "天基信息应用门槛显著降低 · 影像获取从跨系统查询到一句话直达", "试点应用"),
    ("开源情报态势研判", "intel", "汇聚船舶AIS、灾害通报、飞机航线等多源开源情报数据，智能检索与空间可视化，碎片化信息聚合为一张态势图。",
     "“翻报告”升级为“看图说话”", "内部应用"),
]
CASE_CATS = [("all", "全部"), ("border", "边防"), ("ocean", "海洋"), ("emergency", "应急"), ("intel", "情报")]

CASES_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">客户案例</span>
    <h1>场景驱动 · 价值交付</h1>
    <p class="lead">行业客户为结果买单，场景智能框架保障确定性价值交付。</p>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="filters">
""" + "".join(
    '<button class="fbtn%s" data-f="%s">%s</button>' % (" on" if k == "all" else "", k, n)
    for k, n in CASE_CATS) + """
    </div>
    <div class="grid g2">
""" + "".join(
    '<div class="card case-card" data-cat="%s"><h3>%s</h3>'
    '<div class="tags" style="margin-top:8px"><span class="tag">%s</span></div>'
    '<p style="margin-top:12px">%s</p>'
    '<div class="metric">%s<small>成果口径来自应用推广材料，量化基准待项目方核定</small></div>'
    '<a class="more" href="%s">查看详情 →</a></div>'
    % (c, t, status, desc, metric,
       "case-detail.html" if c == "border" else "cases.html")
    for t, c, desc, metric, status in CASES) + """
    </div>
    <p style="text-align:center;color:var(--mute);font-size:13px;margin-top:28px">
      案例成果目前以定性描述为主。按官网规范，正式发布前需补充量化指标、对比基准与数据来源，并取得客户授权。
    </p>
  </div>
</section>
"""

CASE_DETAIL_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">客户案例 · 边防行业</span>
    <h1>智慧边防应用 · 陆地边境场景</h1>
    <p class="lead">核心成果：预警响应速度大幅提升 · 人力投入显著降低（定性口径，来自应用推广材料）</p>
  </div>
</header>

<section class="section">
  <div class="wrap" style="max-width:920px">
    <div class="anchor-sec">
      <h3><span class="hash">◆</span>客户背景</h3>
      <p class="sub">客户信息已按合规要求脱敏。</p>
      <p style="font-size:14.5px;color:var(--mute)">面向边防管理部门、出入境检查机构及边境安全相关单位，管辖陆地边境线，技防设备种类多、厂商分散，亟需多元信息融合的智能化管控手段。</p>
    </div>
    <div class="anchor-sec">
      <h3><span class="hash">◆</span>项目挑战</h3>
      <div class="grid g3" style="margin-top:10px">
        <div class="card"><h3>数据烟囱</h3><p>跨系统、异构数据无法协同发挥价值。</p></div>
        <div class="card"><h3>预警能力弱</h3><p>预警提前发现能力弱，虚警误报率高、存在漏报风险。</p></div>
        <div class="card"><h3>处置手段少</h3><p>管理、操作复杂，缺少多元信息融合的态势感知、预警发现、研判处置手段。</p></div>
      </div>
    </div>
    <div class="anchor-sec">
      <h3><span class="hash">◆</span>解决方案</h3>
      <p class="sub">认知计算 ＋ 多源数据 ＋ 大小模型协同 ＋ 无人装备</p>
      <ul style="font-size:14.5px;color:var(--mute);padding-left:20px;line-height:2.1">
        <li><b>行业数据底座：</b>天空地多源数据跨域整合，涵盖枪球机摄像头、振动光纤、高压脉冲、无人设备、数字地图等数据；</li>
        <li><b>语义理解框架：</b>构建边防专用数据集，研发大小模型协同的语义理解框架，增强场景化预警发现能力；</li>
        <li><b>认知计算应用：</b>基于认知计算实现智能问数、报告生成、预警处置；</li>
        <li><b>行动闭环：</b>无人装备统一调度，实现“数据、语义、决策、行动”场景智能的业务闭环。</li>
      </ul>
    </div>
    <div class="anchor-sec">
      <h3><span class="hash">◆</span>应用成果</h3>
      <p style="font-size:14.5px;color:var(--mute)">
        预警响应速度大幅提升，人力投入显著降低；适用于陆地边境、海岸线、口岸等多种场景的智能化升级。
        <span class="placeholder-note">量化指标、对比基准与数据来源待项目方核定后补充</span>
      </p>
    </div>
    <div class="anchor-sec">
      <h3><span class="hash">◆</span>客户评价</h3>
      <p style="font-size:14.5px;color:var(--mute)">待客户授权后补充（官网规范：评价需真实可追溯，注明来源及授权）。</p>
    </div>
    <div class="anchor-sec" style="border-bottom:none">
      <h3><span class="hash">◆</span>相关推荐</h3>
      <div class="grid g2" style="margin-top:10px">
        <div class="card"><h3>海洋石油污染溯源分析</h3><p>多源信息融合，输出嫌疑船舶排序及证据链。</p><a class="more" href="solutions.html#oil">查看方案 →</a></div>
        <div class="card"><h3>应急信息服务</h3><p>自然语言交互，灾前灾后影像要素对比分析。</p><a class="more" href="solutions.html#emergency">查看方案 →</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>获取同类方案</h2><p>留下联系方式，获取边防／边境安全场景完整方案资料</p></div>
      <a class="btn btn-a btn-lg" href="contact.html">联系我们</a>
    </div>
  </div>
</section>
"""

# ============================================================ 关于我们
ABOUT_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">关于我们</span>
    <h1>让数智技术真正落地行业</h1>
    <p class="lead">中国航天科技集团卫星应用创新研究院，打造“感通算用”一体化综合信息服务平台——天元（DISOps）。</p>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="grid g2" style="align-items:center;gap:44px">
      <div>
        <h2 style="font-size:26px;color:var(--primary);margin-bottom:16px">面向行业智能升级的一站式信息服务平台</h2>
        <p style="color:var(--mute)">研究院依托“感、通、算、用”智能技术应用框架，融合感知、认知、具身等智能技术，实现“认知-行动”场景化智能闭环，解决AI技术行业应用的最后一公里问题，实现卫星应用向天空地融合信息服务延伸与拓展。</p>
        <p style="color:var(--mute);margin-top:12px">天元（DISOps）借鉴国内外优秀AI平台经验，构建感知、认知、具身等智能技术融合的场景智能框架，实现“数据-认知-决策-行动”应用闭环。</p>
      </div>
      <div class="grid g2">
        <div class="card" style="text-align:center"><div class="metric" style="font-size:34px;color:var(--accent-d20);font-weight:800">120万+</div><p>闭源数据条目</p></div>
        <div class="card" style="text-align:center"><div style="font-size:34px;color:var(--accent-d20);font-weight:800">30余个</div><p>行业算法与控制组件</p></div>
        <div class="card" style="text-align:center"><div style="font-size:34px;color:var(--accent-d20);font-weight:800">14家</div><p>生态合作伙伴</p></div>
        <div class="card" style="text-align:center"><div style="font-size:34px;color:var(--accent-d20);font-weight:800">5家</div><p>数据共建单位</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section alt" id="history">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">发展历程</span>
      <h2>关键里程碑</h2>
    </div>
    <div class="timeline">
      <div class="tl-item"><time>时间待补充</time><h4>数据资源基底初步形成<span class="placeholder-note">占位示例</span></h4><p>汇聚120万条以上闭源数据、航天特色数据与开源情报数据，形成空天地一体的数据资源基底。</p></div>
      <div class="tl-item"><time>时间待补充</time><h4>行业组件与工具链就绪<span class="placeholder-note">占位示例</span></h4><p>纳管30余个行业算法与控制组件，完成数据管道、天基服务、业务语义建模、大模型等专业工具纳管。</p></div>
      <div class="tl-item"><time>时间待补充</time><h4>行业场景闭环落地<span class="placeholder-note">占位示例</span></h4><p>在边防、海洋、应急、开源情报等典型场景形成“数据-认知-决策-行动”业务闭环并开展应用推广。</p></div>
    </div>
    <p style="text-align:center;color:var(--mute);font-size:13px;margin-top:12px">发展历程节点为占位示例，请由院办核定实际时间与事件后替换。</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">聚合共建</span>
      <h2>聚合集团公司内外数智成果</h2>
    </div>
    <div class="grid g2" style="align-items:start">
      <div class="card">
        <h3>数据共建单位</h3>
        <div class="table-wrap" style="margin-top:12px"><table class="t" style="min-width:420px">
          <tr><th>合作单位</th><th>数智成果</th></tr>
          <tr><td>航天十一院</td><td>钢铁战士雷达＋可见光视频回传与周界报警</td></tr>
          <tr><td>体系院</td><td>典型场景开源遥感影像数据</td></tr>
          <tr><td>中国四维</td><td>新疆典型区域13-17级遥感底图数据</td></tr>
          <tr><td>可克达拉市市政法委</td><td>技防设备、报警预警等闭源数据</td></tr>
          <tr><td>中国卫通鑫诺公司</td><td>船舶卫星回传GPS数据</td></tr>
        </table></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:22px">
        <div class="card">
          <h3>组件联合研发</h3>
          <p>联合体系院、航天五院钱学森实验室、北航、北京理工、北京邮电、中南大学、西交大，研发专用AI模型、遥感模型、智能体应用等组件30余个。</p>
        </div>
        <div class="card">
          <h3>专业服务聚合</h3>
          <p>联合航天五院、体系院、哈工大、云深处、大疆，聚合数据治理、业务语义建模、模型训推、天基信息服务、无人装备管理等专业服务。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="kicker">企业文化</span>
      <h2>使命 · 愿景 · 价值观</h2>
    </div>
    <div class="grid g3">
      <div class="card"><div class="ico">&#9879;</div><h3>使命</h3><p>让数智技术真正落地行业，解决AI应用“最后一公里”。</p></div>
      <div class="card"><div class="ico accent">&#128241;</div><h3>愿景</h3><p>成为空天地一体化信息服务的引领者。</p></div>
      <div class="card"><div class="ico deep">&#128161;</div><h3>价值观</h3><p>场景驱动 · 开放协同 · 自主可控 · 价值交付。</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">合作伙伴</span><h2>生态共建</h2></div>
    <div class="logo-wall">
      <div class="logo-tile"><b>海康威视</b><span>杭州海康威视数字技术股份有限公司</span></div>
      <div class="logo-tile"><b>宇视科技</b><span>浙江宇视科技有限公司</span></div>
      <div class="logo-tile"><b>云深处科技</b><span>杭州云深处科技有限公司</span></div>
      <div class="logo-tile"><b>宇树科技</b><span>杭州宇树科技有限公司</span></div>
      <div class="logo-tile"><b>大疆创新</b><span>深圳市大疆创新科技有限公司</span></div>
      <div class="logo-tile"><b>浙江大学</b><span>Zhejiang University</span></div>
      <div class="logo-tile"><b>北京航空航天大学</b><span>Beihang University</span></div>
      <div class="logo-tile"><b>西安交通大学</b><span>Xi'an Jiaotong University</span></div>
      <div class="logo-tile"><b>北京理工大学</b><span>Beijing Institute of Technology</span></div>
      <div class="logo-tile"><b>北京邮电大学</b><span>Beijing University of Posts and Telecommunications</span></div>
      <div class="logo-tile"><b>中国空间技术研究院</b><span>航天五院</span></div>
      <div class="logo-tile"><b>航天空气动力技术研究院</b><span>航天十一院</span></div>
      <div class="logo-tile"><b>航天系统科学与工程研究院</b><span>体系院</span></div>
      <div class="logo-tile"><b>中国四维</b><span>中国四维测绘技术有限公司</span></div>
    </div>
    <p style="text-align:center;margin-top:36px"><a class="btn btn-p btn-lg" href="careers.html">加入我们</a></p>
  </div>
</section>
"""

# ============================================================ 联系我们
CONTACT_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">联系我们</span>
    <h1>联系我们，开启数智转型之旅</h1>
    <p class="lead">专业团队为您提供定制化数智系统解决方案。</p>
  </div>
</header>

<section class="section">
  <div class="wrap" style="max-width:1000px">
    <div class="grid g3" style="margin-bottom:52px">
      <div class="card" style="text-align:center"><div class="ico">&#128222;</div><h3>电话</h3><p><a href="tel:01000000000">010-XXXX XXXX</a><br><span style="font-size:12px;color:var(--alert)">占位，上线前替换</span></p></div>
      <div class="card" style="text-align:center"><div class="ico accent">&#9993;</div><h3>邮箱</h3><p><a href="mailto:contact@example.com">contact@example.com</a><br><span style="font-size:12px;color:var(--alert)">占位，上线前替换</span></p></div>
      <div class="card" style="text-align:center"><div class="ico deep">&#128205;</div><h3>地址</h3><p>北京市海淀区（占位）<br><span style="font-size:12px;color:var(--alert)">占位，上线前替换</span></p></div>
    </div>

    <div class="sec-head"><span class="kicker">在线咨询</span><h2>留下您的需求</h2><p>工作日 9:00-18:00，我们将在 1 个工作日内回复。</p></div>
    <form class="form" id="contact-form" novalidate>
      <div class="row">
        <label for="f-name">姓名 <span class="req">*</span></label>
        <input id="f-name" name="name" type="text" autocomplete="name" placeholder="您的称呼" required>
        <div class="err">请填写姓名</div>
      </div>
      <div class="row">
        <label for="f-phone">电话 <span class="req">*</span></label>
        <input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="手机或座机号码" required>
        <div class="err">请填写正确的电话号码（11位手机号或座机号）</div>
      </div>
      <div class="row">
        <label for="f-msg">需求描述 <span style="font-weight:400;color:var(--mute)">（选填）</span></label>
        <textarea id="f-msg" name="message" rows="5" placeholder="您所在行业、想解决的问题…"></textarea>
      </div>
      <button class="btn btn-p btn-lg btn-w" type="submit">提交咨询</button>
      <div class="form-ok" id="form-ok">✓ 提交成功！我们的团队将在 1 个工作日内与您联系。</div>
      <p style="font-size:12.5px;color:var(--mute);margin-top:14px">提交即表示您同意我们的<a href="legal.html#privacy">隐私政策</a>。本演示站表单暂不做服务端提交，接入正式后端后生效。</p>
    </form>
  </div>
</section>

<section class="section alt">
  <div class="wrap" style="max-width:1000px">
    <div class="sec-head"><span class="kicker">常见问题</span><h2>FAQ</h2></div>
    <div class="faq">
      <div class="faq-item"><button class="faq-q" type="button">天元（DISOps）是什么？<span class="arr">&#9660;</span></button>
        <div class="faq-a">天元（DISOps）是面向数智技术场景化闭环的一站式信息服务平台，旨在解决数智应用“最后一公里”问题，快速构建和持续优化“数据-认知-决策-行动”价值闭环的数智系统，助力行业应用智能升级。</div></div>
      <div class="faq-item"><button class="faq-q" type="button">平台的数据从哪里来？<span class="arr">&#9660;</span></button>
        <div class="faq-a">平台汇聚三类数据：安防摄像头、振动光纤、预警事件等120万条以上闭源数据；20余个在轨通信卫星、44个地面站、1600+全球在轨对地观测卫星数据等航天特色数据；以及1000+船舶、5000+航空等类型的开源情报数据，初步形成空天地一体的数据资源基底。</div></div>
      <div class="faq-item"><button class="faq-q" type="button">支持哪些部署方式？<span class="arr">&#9660;</span></button>
        <div class="faq-a">平台支持国产化全栈适配，从算力底座到AI模型满足自主可控要求，支持云端训练与边缘端推理的无缝协同；具体部署模式（公有云／私有化／混合）可在咨询时按需沟通。</div></div>
      <div class="faq-item"><button class="faq-q" type="button">如何与你们开展合作？<span class="arr">&#9660;</span></button>
        <div class="faq-a">支持数据共建、组件联合研发、专业服务聚合等多种合作模式，已有海康威视、大疆、云深处等企业及多所高校、科研院所参与共建。可通过本页表单或邮箱与我们联系。</div></div>
      <div class="faq-item"><button class="faq-q" type="button">如何申请产品演示？<span class="arr">&#9660;</span></button>
        <div class="faq-a">提交本页“在线咨询”表单（仅需姓名和电话），或发送邮件说明您关注的行业场景，我们将安排对应解决方案团队与您对接演示。</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:1000px">
    <div class="sec-head"><span class="kicker">留言反馈</span><h2>其他事宜</h2></div>
    <div class="card">
      <p style="font-size:14.5px">合作意向书、媒体问询函等非销售类事宜，请发送邮件至 <b>feedback@example.com</b>（占位），支持附件（PDF/DOC/JPG，≤10MB）。销售咨询请使用上方在线表单，以便我们快速分派对应团队。</p>
      <p style="font-size:12.5px;color:var(--mute);margin-top:10px">办公地点地图待正式地址确定后嵌入（懒加载静态图＋点击跳转，保障首屏性能）。</p>
    </div>
  </div>
</section>
"""

# ============================================================ 新闻
NEWS_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">新闻动态</span>
    <h1>新闻与行业资讯</h1>
    <p class="lead">了解天元平台进展与数智行业洞察。</p>
  </div>
</header>

<section class="section">
  <div class="wrap" style="max-width:920px">
    <div class="card" style="margin-bottom:34px;display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap">
      <p style="font-size:14px;color:var(--mute)">订阅动态：邮件订阅入口即将上线，支持随时退订；也可关注公众号获取更新。</p>
      <button class="btn btn-o" type="button" disabled style="opacity:.55">订阅入口（建设中）</button>
    </div>
    <div class="news-list">
      <a class="news-item" href="news.html">
        <div><h3>天元平台完成 30 余个行业算法与控制组件纳管<span class="placeholder-note">示例内容</span></h3>
        <p>面向海洋、应急、边海防等典型场景，纳管30余个行业算法与控制组件，支撑行业数智系统的快速装配与持续优化。<span class="tag" style="margin-left:8px">产品进展</span></p></div>
        <time>2026-09-10</time>
      </a>
      <a class="news-item" href="news.html">
        <div><h3>研究院与多家生态伙伴深化数智能力合作<span class="placeholder-note">示例内容</span></h3>
        <p>联合科研院所与高校，研发专用AI模型、遥感模型、智能体应用等组件30余个；聚合数据治理、业务语义建模、模型训推等专业服务。<span class="tag" style="margin-left:8px">生态合作</span></p></div>
        <time>2026-08-28</time>
      </a>
      <a class="news-item" href="news.html">
        <div><h3>天元·灵语本体建模能力持续升级<span class="placeholder-note">示例内容</span></h3>
        <p>自动本体建模，Skill级业务操作，支持200+ AI动作，业务人员无需编程即可调用AI能力。<span class="tag" style="margin-left:8px">产品进展</span></p></div>
        <time>2026-08-15</time>
      </a>
      <a class="news-item" href="news.html">
        <div><h3>“感通算用”一体化综合信息服务能力发布<span class="placeholder-note">示例内容</span></h3>
        <p>天元（DISOps）面向数智技术场景化闭环，构建“数据-认知-决策-行动”价值闭环的数智系统。<span class="tag" style="margin-left:8px">平台发布</span></p></div>
        <time>2026-07-30</time>
      </a>
    </div>
    <p style="text-align:center;color:var(--mute);font-size:13px;margin-top:28px">
      以上为示例内容，正式上线前请替换为经审核的真实新闻稿；新闻详情页待首批稿件就绪后开放。
    </p>
  </div>
</section>
"""

# ============================================================ 招聘
CAREERS_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">加入我们</span>
    <h1>与天元一起，把数智技术落到行业最前线</h1>
    <p class="lead">在真实行业场景中，做“最后一公里”的攻坚者。</p>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">为什么选择我们</span><h2>具体的回报与成长</h2></div>
    <div class="grid g4">
      <div class="card"><div class="ico">&#128176;</div><h3>薪酬保障</h3><p>14薪＋年度调薪<span class="placeholder-note">占位，需人力核定</span></p></div>
      <div class="card"><div class="ico accent">&#9200;</div><h3>弹性工作</h3><p>弹性工作制<span class="placeholder-note">占位，需人力核定</span></p></div>
      <div class="card"><div class="ico deep">&#127973;</div><h3>年度体检</h3><p>每年全面体检<span class="placeholder-note">占位，需人力核定</span></p></div>
      <div class="card"><div class="ico">&#128640;</div><h3>航天平台</h3><p>航天科研体系，接触空天地一体化真实场景与数据。</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">开放岗位</span><h2>热招职位</h2></div>
    <div class="table-wrap"><table class="t">
      <tr><th>职位</th><th>地点</th><th>类型</th><th>申请</th></tr>
      <tr><td>大模型算法工程师<span class="placeholder-note">占位</span></td><td>北京</td><td>全职</td><td><a href="mailto:hr@example.com?subject=应聘-大模型算法工程师">邮箱直投 →</a></td></tr>
      <tr><td>遥感应用工程师<span class="placeholder-note">占位</span></td><td>北京</td><td>全职</td><td><a href="mailto:hr@example.com?subject=应聘-遥感应用工程师">邮箱直投 →</a></td></tr>
      <tr><td>智能体开发工程师<span class="placeholder-note">占位</span></td><td>北京 / 乌鲁木齐</td><td>全职</td><td><a href="mailto:hr@example.com?subject=应聘-智能体开发工程师">邮箱直投 →</a></td></tr>
      <tr><td>前端工程师<span class="placeholder-note">占位</span></td><td>北京</td><td>全职</td><td><a href="mailto:hr@example.com?subject=应聘-前端工程师">邮箱直投 →</a></td></tr>
    </table></div>
    <p style="font-size:13px;color:var(--mute);margin-top:16px">
      岗位为占位示例，需人力资源部门核定后替换。投递通道：邮箱直投（hr@example.com，占位）＋招聘平台双通道；简历投递后显示确认：“简历已收到，将在3-5个工作日内回复”。
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:920px">
    <div class="sec-head"><span class="kicker">团队风采</span><h2>在天元工作</h2></div>
    <div class="card">
      <p style="font-size:14.5px;color:var(--mute)">员工故事与工作场景展示待补充：需获员工授权，照片统一色调与构图，避免过度美化。可先用团队合照＋一句话工作感受的形式呈现。</p>
    </div>
  </div>
</section>
"""

# ============================================================ 搜索页
SEARCH_INDEX = [
    {"title": "首页", "url": "index.html", "type": "页面", "from": "天元官网", "desc": "让数智技术真正落地行业。天元（DISOps）一站式信息服务平台，构建数据-认知-决策-行动价值闭环。", "tags": "平台 感通算用"},
    {"title": "产品与能力", "url": "products.html", "type": "页面", "from": "天元官网", "desc": "1个底座+3大核心引擎+1个数智市集+1个安全体系+N个行业应用：智算底座、灵观、灵数、空天地一体化网络、灵语、灵炼、灵智、认知计算引擎、灵动、灵集、天元·信息服务助手。", "tags": "产品 引擎 组件 数智市集"},
    {"title": "天元平台产品详情", "url": "product-detail.html", "type": "页面", "from": "天元官网", "desc": "空天地一体化数据、全链路闭环、国产化全栈适配、智能体驱动；三大核心引擎与数智市集分层能力详解与客户价值。", "tags": "产品详情 架构 灵观 灵数 灵语 灵炼 灵智 灵动 灵集"},
    {"title": "开源情报分析解决方案", "url": "solutions.html#intel", "type": "解决方案", "from": "解决方案", "desc": "认知计算+多源数据=智能问数与态势空间呈现，碎片化信息聚合为一张态势图。", "tags": "情报 AIS 态势"},
    {"title": "海洋石油污染解决方案", "url": "solutions.html#oil", "type": "解决方案", "from": "解决方案", "desc": "油膜识别、起始点反演、船舶特征分析，输出嫌疑船舶排序及证据链。", "tags": "海洋 油膜 溯源"},
    {"title": "应急信息服务解决方案", "url": "solutions.html#emergency", "type": "解决方案", "from": "解决方案", "desc": "自然语言交互拉取灾前灾后影像，建筑物损毁、水体淹没范围对比分析。", "tags": "应急 灾害 影像"},
    {"title": "智慧边防应用解决方案", "url": "solutions.html#border", "type": "解决方案", "from": "解决方案", "desc": "大小模型协同+无人装备，数据、语义、决策、行动场景智能业务闭环。", "tags": "边防 预警 无人装备"},
    {"title": "客户案例总览", "url": "cases.html", "type": "页面", "from": "天元官网", "desc": "智慧边防、海洋石油污染溯源、应急信息服务对接、开源情报态势研判。", "tags": "案例 实战应用"},
    {"title": "智慧边防应用案例", "url": "case-detail.html", "type": "案例", "from": "客户案例", "desc": "陆地边境场景：行业数据底座、大小模型协同语义理解、智能问数、无人装备协同处置。", "tags": "边防 案例 预警"},
    {"title": "关于我们", "url": "about.html", "type": "页面", "from": "天元官网", "desc": "中国航天科技集团卫星应用创新研究院，聚合集团内外数据、组件、工具等数智成果。", "tags": "研究院 关于 合作"},
    {"title": "联系我们", "url": "contact.html", "type": "页面", "from": "天元官网", "desc": "在线咨询表单、常见问题FAQ、留言反馈。", "tags": "联系 咨询 演示"},
    {"title": "新闻动态", "url": "news.html", "type": "页面", "from": "天元官网", "desc": "天元平台进展与数智行业洞察。", "tags": "新闻 动态"},
    {"title": "加入我们", "url": "careers.html", "type": "页面", "from": "天元官网", "desc": "热招岗位：大模型算法工程师、遥感应用工程师、智能体开发工程师、前端工程师。", "tags": "招聘 岗位"},
    {"title": "隐私政策", "url": "legal.html#privacy", "type": "合规", "from": "法律信息", "desc": "数据收集、使用、存储、删除说明。", "tags": "隐私 合规"},
    {"title": "服务条款", "url": "legal.html#terms", "type": "合规", "from": "法律信息", "desc": "用户使用规范与免责声明。", "tags": "条款 合规"},
]

SEARCH_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">站内搜索</span>
    <h1>搜索全站内容</h1>
    <p class="lead">支持按标题、摘要、标签检索，关键词高亮显示。</p>
  </div>
</header>

<section class="section">
  <div class="wrap" style="max-width:860px">
    <form class="search-box" id="search-form">
      <input id="search-input" type="search" placeholder="输入关键词，如：边防 / 灵语 / 数据" autofocus aria-label="搜索关键词">
      <button class="btn btn-p" type="submit">搜 索</button>
    </form>
    <div class="history" id="search-history"></div>
    <div id="search-results"></div>
    <p style="font-size:12.5px;color:var(--mute);margin-top:24px">
      搜索历史仅保存在您的浏览器本地（最近10条，30天自动清除，可一键清除），不做服务端记录。
    </p>
  </div>
</section>
"""

# ============================================================ 合规页
LEGAL_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">法律信息</span>
    <h1>隐私政策 · 服务条款 · Cookie 声明</h1>
    <p class="lead">本页内容为通用模板框架，正式上线前请交由法务部门审定并定期审计更新。</p>
  </div>
</header>

<section class="section">
  <div class="wrap" style="max-width:920px">
    <div class="anchor-sec" id="privacy">
      <h3><span class="hash">◆</span>隐私政策</h3>
      <ul style="font-size:14.5px;color:var(--mute);padding-left:20px;line-height:2.1">
        <li><b>数据收集：</b>本站仅在您主动提交咨询表单时收集姓名、电话及选填的需求描述；搜索历史与偏好记录仅存储于您浏览器的本地存储中。</li>
        <li><b>数据使用：</b>收集的信息仅用于回复您的咨询及后续商务沟通，不用于其他目的，不向无关第三方出售或共享。</li>
        <li><b>数据存储：</b>数据存储于境内合规服务器，采取加密与访问控制措施。</li>
        <li><b>数据删除：</b>您可随时通过公示的联系邮箱申请查询、更正或删除您的个人信息。</li>
      </ul>
    </div>
    <div class="anchor-sec" id="terms">
      <h3><span class="hash">◆</span>服务条款</h3>
      <ul style="font-size:14.5px;color:var(--mute);padding-left:20px;line-height:2.1">
        <li><b>使用规范：</b>本站内容仅供信息参考，未经授权不得复制、转载或用于商业用途。</li>
        <li><b>信息准确性：</b>平台尽力保证信息准确，但产品能力、数据指标等以双方商务合同约定为准。</li>
        <li><b>免责声明：</b>对因不可抗力或非本站原因导致的服务中断、数据损失，本站不承担责任。</li>
      </ul>
    </div>
    <div class="anchor-sec" style="border-bottom:none" id="cookie">
      <h3><span class="hash">◆</span>Cookie 声明</h3>
      <ul style="font-size:14.5px;color:var(--mute);padding-left:20px;line-height:2.1">
        <li><b>必要 Cookie：</b>保障站点正常运行所必需。</li>
        <li><b>本地存储：</b>记录您的 Cookie 选择与搜索历史（最近10条，30天自动清除），支持一键清除。</li>
        <li><b>管理方式：</b>首次访问时弹窗告知，您可选择“仅必要”；选择结果记录在本地，不重复打扰；可通过清除浏览器数据重置选择。</li>
      </ul>
    </div>
  </div>
</section>
"""

# ============================================================ 404 / 500
BODY_404 = """
<div class="err-page">
  <div>
    <div class="code">404</div>
    <h1>页面走丢了</h1>
    <p>您访问的页面不存在或已被移动，别着急，从这里继续：</p>
    <div class="btns">
      <a class="btn btn-p btn-lg" href="index.html">返回首页</a>
      <a class="btn btn-o btn-lg" href="search.html">站内搜索</a>
    </div>
    <p style="margin-top:26px;font-size:13.5px">热门页面：
      <a href="products.html">产品与能力</a> ·
      <a href="solutions.html">解决方案</a> ·
      <a href="cases.html">客户案例</a> ·
      <a href="contact.html">联系我们</a></p>
  </div>
</div>
"""

BODY_500 = """
<div class="err-page">
  <div>
    <div class="code">500</div>
    <h1>系统维护中</h1>
    <p>系统正在紧急维护中，预计稍后恢复，请耐心等待。</p>
    <div class="btns">
      <a class="btn btn-p btn-lg" href="index.html">返回首页</a>
      <a class="btn btn-o btn-lg" href="contact.html">联系我们</a>
    </div>
    <p style="margin-top:26px;font-size:13.5px">如需紧急支持，请发送邮件至 contact@example.com（占位）。</p>
  </div>
</div>
"""

# ============================================================ 站点地图
SITEMAP_BODY = """
<header class="banner page-banner">
  <div class="banner-in">
    <span class="badge">网站地图</span>
    <h1>全站页面索引</h1>
  </div>
</header>

<section class="section">
  <div class="wrap">
    <div class="grid g3">
      <div class="card">
        <h3>主要页面</h3>
        <ul style="padding-left:18px;color:var(--mute);font-size:14px;line-height:2.2">
          <li><a href="index.html">首页</a></li>
          <li><a href="products.html">产品与能力</a></li>
          <li><a href="product-detail.html">天元平台产品详情</a></li>
          <li><a href="solutions.html">解决方案</a></li>
          <li><a href="cases.html">客户案例</a></li>
          <li><a href="case-detail.html">智慧边防应用案例</a></li>
        </ul>
      </div>
      <div class="card">
        <h3>企业与资讯</h3>
        <ul style="padding-left:18px;color:var(--mute);font-size:14px;line-height:2.2">
          <li><a href="about.html">关于我们</a></li>
          <li><a href="news.html">新闻动态</a></li>
          <li><a href="careers.html">加入我们</a></li>
          <li><a href="contact.html">联系我们</a></li>
          <li><a href="search.html">站内搜索</a></li>
        </ul>
      </div>
      <div class="card">
        <h3>解决方案锚点</h3>
        <ul style="padding-left:18px;color:var(--mute);font-size:14px;line-height:2.2">
          <li><a href="solutions.html#intel">开源情报分析</a></li>
          <li><a href="solutions.html#oil">海洋石油污染</a></li>
          <li><a href="solutions.html#emergency">应急信息服务</a></li>
          <li><a href="solutions.html#border">智慧边防应用</a></li>
        </ul>
        <h3 style="margin-top:14px">合规</h3>
        <ul style="padding-left:18px;color:var(--mute);font-size:14px;line-height:2.2">
          <li><a href="legal.html#privacy">隐私政策</a></li>
          <li><a href="legal.html#terms">服务条款</a></li>
          <li><a href="legal.html#cookie">Cookie 声明</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

# ============================================================ 生成
if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "theme.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(OUT, "assets", "main.js"), "w", encoding="utf-8") as f:
        f.write(JS)
    print("written assets/theme.css, assets/main.js")

    page("index.html", "首页 | 让数智技术真正落地行业",
         "天元（DISOps）是面向数智技术场景化闭环的一站式信息服务平台，构建“数据-认知-决策-行动”价值闭环。", "index.html", INDEX_BODY)
    page("products.html", "产品与能力",
         "1个底座+3大核心引擎+1个数智市集+1个安全体系+N个行业应用：智算底座、数据融合、认知决策、行动执行、数智市集、安全合规。", "products.html", PRODUCTS_BODY)
    page("product-detail.html", "天元平台产品详情",
         "基于空天地一体化数据，实现从数据融合到认知决策、再到行动执行的全链路闭环智能系统。", "products.html", DETAIL_BODY)
    page("solutions.html", "行业解决方案",
         "开源情报分析、海洋石油污染、应急信息服务、智慧边防应用等行业解决方案。", "solutions.html", SOLUTIONS_BODY)
    page("cases.html", "客户案例",
         "智慧边防、海洋石油污染溯源、应急信息服务、开源情报态势研判等应用案例。", "cases.html", CASES_BODY)
    page("case-detail.html", "智慧边防应用案例 | 客户案例",
         "陆地边境场景智慧边防应用：行业数据底座、大小模型协同、无人装备协同处置。", "cases.html", CASE_DETAIL_BODY)
    page("about.html", "关于我们",
         "中国航天科技集团卫星应用创新研究院，打造“感通算用”一体化综合信息服务平台。", "about.html", ABOUT_BODY)
    page("contact.html", "联系我们",
         "在线咨询、常见问题、留言反馈——专业团队为您提供定制化数智系统解决方案。", "contact.html", CONTACT_BODY)
    page("news.html", "新闻动态",
         "天元平台进展与数智行业洞察。", "news.html", NEWS_BODY)
    page("careers.html", "加入我们",
         "热招岗位：大模型算法工程师、遥感应用工程师、智能体开发工程师、前端工程师。", "about.html", CAREERS_BODY)
    page("search.html", "站内搜索",
         "支持按标题、摘要、标签检索全站内容。", "index.html", SEARCH_BODY,
         extra_head="<script>window.TY_SEARCH_INDEX=" + json.dumps(SEARCH_INDEX, ensure_ascii=False) + ";</script>")
    page("legal.html", "法律信息",
         "隐私政策、服务条款与Cookie声明。", "index.html", LEGAL_BODY)
    page("404.html", "页面未找到", "页面走丢了，返回首页或站内搜索。", "index.html", BODY_404)
    page("500.html", "系统维护中", "系统正在紧急维护中，预计稍后恢复。", "index.html", BODY_500)
    page("sitemap.html", "网站地图", "天元官网全站页面索引。", "index.html", SITEMAP_BODY)
    print("ALL DONE")
