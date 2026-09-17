/* ═══════════════════════════════════════════
   STILLWATER — interactions
   nav · reveal · contact · booking wizard
   ═══════════════════════════════════════════ */
(function () {
  'use strict';

  /* ── Nav ── */
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 30);
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

  /* ── Reveal ── */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* ── Contact form ── */
  const contactForm = document.getElementById('contactForm');
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let ok = true;
    contactForm.querySelectorAll('[required]').forEach(f => {
      const bad = f.type === 'email' ? !/^\S+@\S+\.\S+$/.test(f.value) : !f.value.trim();
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
  const topic = document.getElementById('cf-topic');
  topic.addEventListener('change', () => topic.classList.toggle('filled', !!topic.value));

  /* ── Booking wizard ── */
  const form = document.getElementById('bookForm');
  const panes = [...form.querySelectorAll('.pane')];
  const steps = [...document.querySelectorAll('.l-step')];
  let cur = 0, booked = false;

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
        bad = !pane.querySelector('input[name="svc"]:checked');
        pane.querySelector('.need-grid')?.classList.toggle('error', bad);
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

  document.querySelectorAll('#timeGrid .hour').forEach(h => {
    h.addEventListener('click', () => {
      document.querySelectorAll('#timeGrid .hour').forEach(x => x.classList.remove('sel'));
      h.classList.add('sel');
      document.getElementById('bk-time').value = h.dataset.v;
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
