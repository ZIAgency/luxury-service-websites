/* ═══════════════════════════════════════════
   IRIS PRIVÉ — the vision atelier
   nav · reveal · counters · parallax · forms
   ═══════════════════════════════════════════ */
(function () {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Navigation state ── */
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Mobile menu ── */
  const burger = document.getElementById('burger');
  burger.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  document.querySelectorAll('.links a').forEach(a =>
    a.addEventListener('click', () => document.body.classList.remove('menu-open'))
  );

  /* ── Scroll reveal ── */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); revealObserver.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  /* ── Animated counters (ease-out cubic) ── */
  function animateCount(el) {
    const target = parseFloat(el.dataset.count);
    const dur = 1700;
    const start = performance.now();
    const fmt = n => (el.dataset.decimal ? n.toFixed(1) : Math.round(n).toLocaleString()) + (el.dataset.suffix || '');
    (function tick(now) {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    })(start);
  }
  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { animateCount(e.target); countObserver.unobserve(e.target); }
    });
  }, { threshold: 0.6 });
  document.querySelectorAll('[data-count]').forEach(el => countObserver.observe(el));

  /* ── Iris parallax — the rotor follows the cursor, softly ── */
  const rotor = document.querySelector('.iris-stage');
  if (rotor && !reduceMotion && window.matchMedia('(pointer:fine)').matches) {
    window.addEventListener('mousemove', (e) => {
      const dx = (e.clientX / window.innerWidth - 0.5) * 18;
      const dy = (e.clientY / window.innerHeight - 0.5) * 12;
      rotor.style.transform = `translate(calc(-50% + ${dx}px), calc(-52% + ${dy}px))`;
    }, { passive: true });
  }

  /* ── Floating labels — fields carry their own state ── */
  document.querySelectorAll('.field').forEach(f => {
    const ctrl = f.querySelector('input,textarea,select');
    if (!ctrl) return;
    const sync = () => f.classList.toggle('filled', !!ctrl.value);
    ctrl.addEventListener('input', sync);
    ctrl.addEventListener('change', sync);
    sync();
  });

  /* ── Contact form ── */
  const contactForm = document.getElementById('contactForm');
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let ok = true;
    contactForm.querySelectorAll('[required]').forEach(f => {
      const bad = f.type === 'email'
        ? !/^\S+@\S+\.\S+$/.test(f.value)
        : !f.value.trim();
      f.closest('.field').classList.toggle('error', bad);
      if (bad) ok = false;
    });
    if (!ok) return;
    contactForm.querySelector('fieldset').hidden = true;
    contactForm.querySelector('.form-success').hidden = false;
  });
  contactForm.querySelectorAll('input,select,textarea').forEach(f =>
    f.addEventListener('input', () => f.closest('.field').classList.remove('error'))
  );

  /* ── Booking wizard ── */
  const form = document.getElementById('bookForm');
  const panes = [...form.querySelectorAll('.pane')];
  const steps = [...document.querySelectorAll('#wizSteps li')];
  let cur = 0;
  let booked = false;

  const dateInput = document.getElementById('bk-date');
  dateInput.min = new Date().toISOString().split('T')[0];

  function show(i) {
    panes.forEach((p, x) => p.classList.toggle('is-active', x === i));
    steps.forEach((s, x) => {
      s.classList.toggle('is-current', x === i);
      s.classList.toggle('is-done', x < i);
    });
  }

  function validatePane(pane) {
    let ok = true;
    pane.querySelectorAll('[required]').forEach(f => {
      let bad;
      if (f.type === 'radio') {
        bad = !pane.querySelector(`input[name="${f.name}"]:checked`);
        pane.querySelector('.choice-grid')?.classList.toggle('error', bad);
      } else if (f.id === 'bk-time') {
        bad = !f.value;
        document.getElementById('timeGrid').classList.toggle('error', bad);
      } else {
        bad = !f.value.trim();
        f.closest('.field')?.classList.toggle('error', bad);
      }
      if (bad) ok = false;
    });
    return ok;
  }

  form.addEventListener('click', (e) => {
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

  document.querySelectorAll('#timeGrid .chip').forEach(chip => {
    chip.addEventListener('click', () => {
      document.querySelectorAll('#timeGrid .chip').forEach(c => c.classList.remove('sel'));
      chip.classList.add('sel');
      document.getElementById('bk-time').value = chip.dataset.v;
      document.getElementById('timeGrid').classList.remove('error');
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (booked || !validatePane(panes[2])) return;
    booked = true;
    const svc = form.querySelector('input[name="svc"]:checked').value;
    const when = dateInput.value
      ? new Date(dateInput.value + 'T12:00:00').toLocaleDateString('fr-FR',
          { weekday: 'long', month: 'long', day: 'numeric' }) + ' · ' + document.getElementById('bk-time').value
      : '—';
    document.getElementById('recap-name').textContent = document.getElementById('bk-name').value.split(' ')[0];
    document.getElementById('recap-svc').textContent = svc;
    document.getElementById('recap-when').textContent = when;
    cur = 3;
    show(3);
  });

  form.querySelectorAll('input,textarea').forEach(f =>
    f.addEventListener('input', () => f.closest('.field')?.classList.remove('error'))
  );

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
