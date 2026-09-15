/* 天元官网 · 全局交互（无依赖） */
(function(){
  'use strict';
  var $  = function(s,c){return (c||document).querySelector(s);};
  var $$ = function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));};
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* 1. 导航吸顶缩小 */
  var nav = $('.nav');
  function onScroll(){
    var y = window.scrollY || document.documentElement.scrollTop;
    if(nav) nav.classList.toggle('sm', y > 60);
    var tp = $('.totop'); if(tp) tp.classList.toggle('on', y > 420);
  }
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* 2. 移动端抽屉（含关闭与层级返回） */
  var ham = $('.hamburger'), drawer = $('.drawer'), dclose = $('.drawer-close');
  function openDrawer(){ drawer.classList.add('on'); ham.classList.add('on');
    document.body.style.overflow='hidden'; }
  function closeDrawer(){ drawer.classList.remove('on'); ham.classList.remove('on');
    document.body.style.overflow=''; $$('.sub-m',drawer).forEach(function(s){s.style.display='none';}); }
  if(ham) ham.addEventListener('click', function(){
    drawer.classList.contains('on') ? closeDrawer() : openDrawer(); });
  if(dclose) dclose.addEventListener('click', closeDrawer);
  // 二级展开 + 返回
  $$('.drawer .has-sub > a').forEach(function(a){
    a.addEventListener('click', function(e){
      e.preventDefault();
      var sub = a.nextElementSibling;
      if(sub && sub.classList.contains('sub-m')){
        $$('.sub-m',drawer).forEach(function(s){ if(s!==sub) s.style.display='none'; });
        sub.style.display = sub.style.display==='block' ? 'none' : 'block';
        var btn = $('.drawer-back',drawer); if(btn) btn.style.display='block';
      }
    });
  });
  var back = $('.drawer-back', drawer||document);
  if(back) back.addEventListener('click', function(){
    $$('.sub-m',drawer).forEach(function(s){s.style.display='none';});
    back.style.display='none';
  });

  /* 3. 滚动进场动画 */
  var rvs = $$('.rv');
  if(REDUCED || !('IntersectionObserver' in window)){
    rvs.forEach(function(e){ e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, {threshold:.12, rootMargin:'0px 0px -40px 0px'});
    rvs.forEach(function(e){ io.observe(e); });
  }

  /* 4. 标签页 */
  $$('.tabs').forEach(function(bar){
    var scope = bar.closest('section') || document;
    $$('.tab', bar).forEach(function(t){
      t.addEventListener('click', function(){
        $$('.tab', bar).forEach(function(x){x.classList.remove('on');});
        t.classList.add('on');
        $$('.pane', scope).forEach(function(p){
          p.classList.toggle('on', p.dataset.p === t.dataset.t);
        });
      });
    });
  });

  /* 5. FAQ 折叠 */
  $$('.faq-q').forEach(function(q){
    q.addEventListener('click', function(){ q.parentElement.classList.toggle('on'); });
  });

  /* 6. 筛选器（多选 + 已选条件 + 清除全部） */
  var fbars = $$('.filter-bar');
  fbars.forEach(function(bar){
    var group = bar.dataset.group;
    var selBox = $('[data-selected="'+group+'"]');
    /* URL 参数预选（如 products.html?f=fusion，从详情页回链时自动筛选该层产品） */
    try{
      var fp = new URLSearchParams(location.search).get('f');
      if(fp){ $$('.chip[data-k="'+fp+'"]', bar).forEach(function(c){ c.classList.add('on'); }); }
    }catch(e){}
    function render(){
      if(!selBox) return;
      var on = $$('.chip.on', bar);
      var html = '<span>已选条件：</span>';
      if(!on.length) html += '<span class="sc" style="background:#fff;border-color:var(--line)">全部</span>';
      on.forEach(function(c){
        html += '<span class="sc">'+c.textContent+' <b data-k="'+c.dataset.k+'" style="cursor:pointer;color:var(--alert)">×</b></span>';
      });
      html += '<button class="clear-all" type="button">清除全部</button>';
      selBox.innerHTML = html;
      $$('.sc b', selBox).forEach(function(b){
        b.addEventListener('click', function(){
          var c = $('.chip[data-k="'+b.dataset.k+'"]', bar);
          if(c){ c.classList.remove('on'); render(); }
        });
      });
      $('.clear-all', selBox).addEventListener('click', function(){
        $$('.chip', bar).forEach(function(c){c.classList.remove('on');}); render();
      });
      applyFilter(group);
    }
    $$('.chip', bar).forEach(function(c){
      c.addEventListener('click', function(){ c.classList.toggle('on'); render(); });
    });
    render();
  });

  /* 筛选结果过滤（卡片 data-f 含标签，空格分隔） */
  function applyFilter(group){
    var cards = $$('[data-fl="'+group+'"]');
    if(!cards.length) return;
    var bar = $('.filter-bar[data-group="'+group+'"]');
    var keys = $$('.chip.on', bar).map(function(c){return c.dataset.k;});
    var shown = 0;
    cards.forEach(function(cd){
      var tags = (cd.dataset.f||'').split(/\s+/);
      var ok = !keys.length || keys.some(function(k){return tags.indexOf(k)>=0;});
      cd.style.display = ok ? '' : 'none';
      if(ok) shown++;
    });
    var empty = $('[data-empty="'+group+'"]');
    if(empty) empty.style.display = shown ? 'none' : '';
  }

  /* 7. 表单实时验证 */
  $$('form[data-validate]').forEach(function(f){
    var rules = {'tel':/^1[3-9]\d{9}$/, 'email':/^[^\s@]+@[^\s@]+\.[^\s@]+$/};
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var bad = false, first = null;
      $$('[data-rule]', f).forEach(function(el){
        var row = el.closest('.frow'); var v = el.value.trim();
        var r = el.dataset.rule; var ok = true;
        if(r === 'req') ok = v.length > 0;
        else if(rules[r]) ok = rules[r].test(v);
        if(!ok){ row.classList.add('bad'); bad = true; if(!first) first = el; }
        else row.classList.remove('bad');
      });
      if(bad){ if(first) first.focus(); return; }
      var ok2 = $('.form-ok', f);
      if(ok2){ ok2.style.display='block'; ok2.scrollIntoView({behavior: REDUCED?'auto':'smooth', block:'center'}); }
      f.reset();
    });
    $$('[data-rule]', f).forEach(function(el){
      el.addEventListener('input', function(){ el.closest('.frow').classList.remove('bad'); });
    });
  });

  /* 8. Cookie 同意（localStorage 记忆） */
  var ck = $('.cookie');
  if(ck){
    try{ if(!localStorage.getItem('ty_cookie')) ck.classList.add('on'); }catch(e){ ck.classList.add('on'); }
    $('.ck-a', ck).addEventListener('click', function(){
      try{ localStorage.setItem('ty_cookie','all'); }catch(e){} ck.classList.remove('on'); });
    $('.ck-n', ck).addEventListener('click', function(){
      try{ localStorage.setItem('ty_cookie','min'); }catch(e){} ck.classList.remove('on'); });
  }

  /* 9. 返回顶部 */
  var tp = $('.totop');
  if(tp) tp.addEventListener('click', function(){
    window.scrollTo({top:0, behavior: REDUCED?'auto':'smooth'}); });

  /* 10. 数字滚动 */
  $$('[data-count]').forEach(function(el){
    var end = parseInt(el.dataset.count, 10); if(isNaN(end)) return;
    if(REDUCED){ el.textContent = end; return; }
    var s = 0, step = Math.max(1, Math.ceil(end/26));
    var t = setInterval(function(){
      s += step; if(s >= end){ s = end; clearInterval(t); }
      el.textContent = s;
    }, 40);
  });

  /* 11. 搜索历史（localStorage，最近10条，30天过期） */
  var box = $('#searchInput');
  if(box){
    var KEY = 'ty_hist';
    function load(){
      try{
        var d = JSON.parse(localStorage.getItem(KEY) || '[]');
        var now = Date.now();
        return d.filter(function(x){ return now - x.t < 30*24*3600*1000; });
      }catch(e){ return []; }
    }
    function save(k){
      var d = load().filter(function(x){ return x.k !== k; });
      d.unshift({k:k, t:Date.now()}); d = d.slice(0,10);
      try{ localStorage.setItem(KEY, JSON.stringify(d)); }catch(e){}
      renderHist();
    }
    function renderHist(){
      var hb = $('#histBox'); if(!hb) return;
      var d = load(); if(!d.length){ hb.style.display='none'; return; }
      hb.style.display='';
      $('#histList').innerHTML = d.map(function(x){
        return '<button class="chip" data-k="'+x.k.replace(/"/g,'')+'">'+x.k+'</button>'; }).join('');
      $$('#histList .chip').forEach(function(b){
        b.addEventListener('click', function(){ box.value = b.dataset.k; doSearch(); });
      });
    }
    var clr = $('#clearHist');
    if(clr) clr.addEventListener('click', function(){
      try{ localStorage.removeItem(KEY); }catch(e){} renderHist(); });
    function doSearch(){
      var k = box.value.trim(); if(!k) return;
      save(k);
      var res = $('#resBox'); if(!res) return;
      var hits = (window.SITE_INDEX||[]).filter(function(i){
        return (i.t+i.d+i.k).toLowerCase().indexOf(k.toLowerCase()) >= 0; });
      $('#resCount').textContent = hits.length;
      $('#resWord').textContent = k;
      $('#resList').innerHTML = hits.length ? hits.map(function(i){
        return '<a href="'+i.u+'"><div class="nc"><h3>'+hl(i.t,k)+'</h3><p>'+hl(i.d,k)+
               '</p></div><div class="nt"><span>'+i.k+'</span></div></a>'; }).join('')
        : '';
      res.style.display='';
      $('#emptyBox').style.display = hits.length ? 'none' : '';
    }
    function hl(s,k){
      if(!k) return s;
      return String(s).replace(new RegExp('('+k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi'),
        '<mark style="background:#CCECFB;color:#0F3D75;padding:0 2px">$1</mark>');
    }
    $('#searchBtn').addEventListener('click', doSearch);
    box.addEventListener('keydown', function(e){ if(e.key==='Enter') doSearch(); });
    renderHist();
    if(location.hash.indexOf('q=') > -1){
      box.value = decodeURIComponent(location.hash.split('q=')[1]); doSearch();
    }
    // 排序
    var sortSel = $('#sortSel');
    if(sortSel) sortSel.addEventListener('change', doSearch);
  }

  /* 12. 首屏 Banner 图片轮播（自动播放 + 圆点切换 + 悬停暂停） */
  $$('.bcarousel').forEach(function(car){
    var slides = $$('.bslide', car);
    if(slides.length < 2) return;
    var dotsWrap = car.parentElement.querySelector('.bdots');
    var dots = dotsWrap ? $$('.bdot', dotsWrap) : [];
    var idx = 0, timer = null;
    function show(n){
      idx = (n + slides.length) % slides.length;
      slides.forEach(function(s,i){ s.classList.toggle('on', i === idx); });
      dots.forEach(function(d,i){ d.classList.toggle('on', i === idx); });
    }
    function next(){ show(idx + 1); }
    function play(){ if(REDUCED) return; stop(); timer = setInterval(next, 4500); }
    function stop(){ if(timer){ clearInterval(timer); timer = null; } }
    dots.forEach(function(d,i){
      d.addEventListener('click', function(){ show(i); play(); });
    });
    car.addEventListener('mouseenter', stop);
    car.addEventListener('mouseleave', play);
    show(0); play();
  });

  /* 13. 轮播图片点击放大（Lightbox，点击图片或背景/关闭按钮恢复） */
  var lbImgs = $$('.bcarousel .bslide img');
  if(lbImgs.length){
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role','dialog');
    lb.setAttribute('aria-modal','true');
    lb.innerHTML = '<button class="lb-close" type="button" aria-label="关闭">&times;</button>'+
                   '<img class="lb-img" alt="">';
    var lbImg = $('.lb-img', lb), lbClose = $('.lb-close', lb), lbAdded = false;
    function openLb(src, alt){
      if(!lbAdded){ document.body.appendChild(lb); lbAdded = true; }
      lbImg.src = src; lbImg.alt = alt || '';
      lb.classList.add('on'); document.body.style.overflow = 'hidden';
    }
    function closeLb(){ lb.classList.remove('on'); document.body.style.overflow = ''; }
    lbImgs.forEach(function(img){
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function(){ openLb(img.currentSrc || img.src, img.alt); });
    });
    lbClose.addEventListener('click', closeLb);
    lb.addEventListener('click', function(e){ if(e.target === lb || e.target === lbImg) closeLb(); });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape' && lb.classList.contains('on')) closeLb(); });
  }
})();
