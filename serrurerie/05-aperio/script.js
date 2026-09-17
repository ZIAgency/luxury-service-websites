/* ═══════════════════════════════════════════
   APERIO SYSTEMS — interactions
   nav · access-log feed · reveal · counters · contact · wizard
   ═══════════════════════════════════════════ */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Navigation state ── */
  var nav = document.getElementById('nav');
  var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 40); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Mobile menu ── */
  var burger = document.getElementById('burger');
  burger.addEventListener('click', function () {
    var open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  document.querySelectorAll('.links a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
  });

  /* ── Scroll reveal ── */
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); revealObserver.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(function (el) { revealObserver.observe(el); });

  /* ── Animated counters (ease-out cubic) ── */
  function animateCount(el) {
    var target = parseFloat(el.dataset.count);
    var dur = 1700;
    var start = performance.now();
    var fmt = function (n) {
      return (el.dataset.decimal ? n.toFixed(Number(el.dataset.decimal)) : Math.round(n).toLocaleString()) + (el.dataset.suffix || '');
    };
    (function tick(now) {
      var p = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    })(start);
  }
  var countObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { animateCount(e.target); countObserver.unobserve(e.target); }
    });
  }, { threshold: 0.6 });
  document.querySelectorAll('[data-count]').forEach(function (el) { countObserver.observe(el); });

  /* ── Access log: live feed of simulated entries ── */
  var logFeed = document.getElementById('logFeed');
  var logClock = document.getElementById('logClock');
  var users = ['R. VANCE', 'M. OKAFOR', 'S. IKE', 'INVITÉ · 4H', 'MÉNAGE · 2H', 'T. ABARA', 'LIVRAISON · 30M'];
  var methods = ['bio', 'app', 'pin'];
  var methodNames = { bio: 'BIO', app: 'APP', pin: 'PIN' };
  var doors = ['PORTAIL', 'HALL', 'SALLE', 'PARKING', 'COURRIER'];
  var creds = 37;

  function pad(n) { return String(n).padStart(2, '0'); }

  function stamp() {
    var d = new Date();
    return pad(d.getHours()) + ':' + pad(d.getMinutes()) + ':' + pad(d.getSeconds());
  }

  function pushLog() {
    if (!logFeed) return;
    var allowed = Math.random() > 0.12;
    var li = document.createElement('li');
    var m = methods[Math.floor(Math.random() * methods.length)];
    li.innerHTML =
      '<span class="l-t">' + stamp().slice(0, 5) + ':' + pad(new Date().getSeconds()) + '</span>' +
      '<span class="l-u">' + users[Math.floor(Math.random() * users.length)] + '</span>' +
      '<span class="l-m ' + m + '">' + methodNames[m] + '</span>' +
      '<span class="l-d">' + doors[Math.floor(Math.random() * doors.length)] + '</span>' +
      '<span class="' + (allowed ? 'l-ok">✓' : 'l-no">✕') + '</span>';
    logFeed.insertBefore(li, logFeed.firstChild);
    while (logFeed.children.length > 5) logFeed.removeChild(logFeed.lastChild);
    if (allowed) {
      creds += 1;
      var credEl = document.getElementById('mCreds');
      if (credEl) credEl.innerHTML = creds + ' <i>clés</i>';
    }
  }

  if (logFeed && !reducedMotion) {
    setInterval(pushLog, 4200);
  }

  /* ── Dashboard clock + unlock-time jitter ── */
  function tickDash() {
    if (logClock) logClock.textContent = stamp();
    if (!reducedMotion) {
      var u = document.getElementById('mUnlock');
      if (u) u.innerHTML = (0.38 + Math.random() * 0.07).toFixed(2) + ' <i>s</i>';
    }
  }
  tickDash();
  setInterval(tickDash, 4000);

  /* ── Floating-label sync ── */
  function syncFilled(f) {
    f.classList.toggle('filled', !!String(f.value).trim());
  }
  document.querySelectorAll('.field input, .field select, .field textarea').forEach(function (f) {
    syncFilled(f);
    f.addEventListener('input', function () { syncFilled(f); });
    f.addEventListener('change', function () { syncFilled(f); });
  });

  /* ── Contact form ── */
  var contactForm = document.getElementById('contactForm');
  contactForm.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true;
    contactForm.querySelectorAll('[required]').forEach(function (f) {
      var bad = f.type === 'email'
        ? !/^\S+@\S+\.\S+$/.test(f.value)
        : !f.value.trim();
      f.closest('.field').classList.toggle('error', bad);
      if (bad) ok = false;
    });
    if (!ok) return;
    contactForm.querySelector('fieldset').hidden = true;
    contactForm.querySelector('.form-success').hidden = false;
  });
  contactForm.querySelectorAll('input,select,textarea').forEach(function (f) {
    f.addEventListener('input', function () { f.closest('.field').classList.remove('error'); });
  });

  /* ── Booking wizard ── */
  var form = document.getElementById('bookForm');
  var panes = Array.prototype.slice.call(form.querySelectorAll('.pane'));
  var steps = Array.prototype.slice.call(document.querySelectorAll('#wizSteps li'));
  var cur = 0;
  var booked = false;

  var dateInput = document.getElementById('bk-date');
  dateInput.min = new Date().toISOString().split('T')[0];

  function show(i) {
    panes.forEach(function (p, x) { p.classList.toggle('is-active', x === i); });
    steps.forEach(function (s, x) {
      s.classList.toggle('is-current', x === i);
      s.classList.toggle('is-done', x < i);
    });
  }

  function validatePane(pane) {
    var ok = true;
    pane.querySelectorAll('[required]').forEach(function (f) {
      var bad;
      if (f.type === 'radio') {
        bad = !pane.querySelector('input[name="' + f.name + '"]:checked');
        var grid = pane.querySelector('.choice-grid');
        if (grid) grid.classList.toggle('error', bad);
      } else if (f.id === 'bk-time') {
        bad = !f.value;
        document.getElementById('timeGrid').classList.toggle('error', bad);
      } else {
        bad = !f.value.trim();
        var field = f.closest('.field');
        if (field) field.classList.toggle('error', bad);
      }
      if (bad) ok = false;
    });
    return ok;
  }

  form.addEventListener('click', function (e) {
    if (e.target.closest('.js-next')) {
      if (!validatePane(panes[cur])) return;
      cur = Math.min(cur + 1, panes.length - 1);
      show(cur);
    }
    if (e.target.closest('.js-prev')) {
      cur = Math.max(cur - 1, 0);
      show(cur);
    }
  });

  document.querySelectorAll('#timeGrid .chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      document.querySelectorAll('#timeGrid .chip').forEach(function (c) { c.classList.remove('sel'); });
      chip.classList.add('sel');
      document.getElementById('bk-time').value = chip.dataset.v;
      document.getElementById('timeGrid').classList.remove('error');
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (booked || !validatePane(panes[2])) return;
    booked = true;
    var svc = form.querySelector('input[name="svc"]:checked').value;
    var when = dateInput.value
      ? new Date(dateInput.value + 'T12:00:00').toLocaleDateString('fr-FR',
          { weekday: 'long', month: 'long', day: 'numeric' }) + ' · ' + document.getElementById('bk-time').value
      : '—';
    document.getElementById('recap-name').textContent = document.getElementById('bk-name').value.split(' ')[0];
    document.getElementById('recap-svc').textContent = svc;
    document.getElementById('recap-when').textContent = when;
    cur = 3;
    show(3);
  });

  form.querySelectorAll('input,textarea').forEach(function (f) {
    f.addEventListener('input', function () {
      var field = f.closest('.field');
      if (field) field.classList.remove('error');
    });
  });

  /* ── Year ── */
  document.getElementById('year').textContent = new Date().getFullYear();
})();


/* ── Durcissement anti-abus ─────────────────────────────────
   1. Honeypot : un champ caché rempli = robot → soumission ignorée
   2. Piège temporel : soumission < 3 s après le chargement = robot
   3. Limites de saisie + autocomplete posées proprement
   NB : la protection réelle contre le flood/injection se joue côté
   serveur lorsqu'un backend recevra ces formulaires. */
(function () {
  'use strict';
  var PAGE_LOADED = performance.now();

  function looksLikeBot(form) {
    var hp = form.querySelector('.hp-field input');
    if (hp && hp.value !== '') return true;
    if (performance.now() - PAGE_LOADED < 3000) return true;
    return false;
  }

  // Phase de capture sur document : s'exécute AVANT les handlers des formulaires.
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!(form instanceof HTMLFormElement) || form.dataset.hardened) return;
    form.dataset.hardened = '1';
    if (looksLikeBot(form)) {
      e.preventDefault();
      e.stopImmediatePropagation();
    }
  }, true);

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('form input, form textarea').forEach(function (f) {
      if (f.closest('.hp-field')) return;
      if (!f.maxLength || f.maxLength === -1) {
        if (f.tagName === 'TEXTAREA') f.maxLength = 1500;
        else if (f.type === 'email') f.maxLength = 120;
        else if (f.type === 'tel') f.maxLength = 30;
        else f.maxLength = 100;
      }
      if (!f.autocomplete || f.autocomplete === 'off') {
        var id = (f.id || '') + ' ' + (f.name || '');
        if (/adresse|address/i.test(id)) f.autocomplete = 'street-address';
        else if (f.type === 'email') f.autocomplete = 'email';
        else if (f.type === 'tel') f.autocomplete = 'tel';
        else if (f.type === 'date') f.autocomplete = 'off';
        else if (f.tagName !== 'TEXTAREA' && /nom|name/i.test(id)) f.autocomplete = 'name';
      }
    });
  });
})();
