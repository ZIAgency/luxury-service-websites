/* Aqua Lumière · navigation, préremplissage et formulaire de démonstration */
(() => {
  "use strict";

  const nav = document.getElementById("nav");
  const burger = document.getElementById("burger");
  const links = document.getElementById("navLinks");

  // Ombre de la barre de navigation au défilement
  const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Menu mobile
  burger.addEventListener("click", () => {
    const open = burger.getAttribute("aria-expanded") === "true";
    burger.setAttribute("aria-expanded", String(!open));
    burger.setAttribute("aria-label", open ? "Ouvrir le menu" : "Fermer le menu");
    links.classList.toggle("open", !open);
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      burger.setAttribute("aria-expanded", "false");
      links.classList.remove("open");
    })
  );

  // Situations : préremplit le motif puis descend au formulaire
  const work = document.getElementById("work");
  document.querySelectorAll("[data-prefill]").forEach((btn) =>
    btn.addEventListener("click", () => {
      work.value = btn.dataset.prefill;
      work.closest(".field").classList.remove("invalid");
      document.getElementById("devis").scrollIntoView({ behavior: "smooth" });
      window.setTimeout(() => {
        work.classList.remove("flash");
        void work.offsetWidth;
        work.classList.add("flash");
        const next = document.querySelector("#quoteForm [data-rule]:not(#work)");
        if (next) next.focus({ preventScroll: true });
      }, 600);
    })
  );

  // Apparition douce des blocs
  const targets = document.querySelectorAll(".serv, .step-list li, .job, .review, .sit");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.15 });
    targets.forEach((t) => { t.classList.add("reveal"); io.observe(t); });
  }

  // Formulaire (démonstration : rien n'est envoyé)
  const form = document.getElementById("quoteForm");
  const loadedAt = Date.now();
  const date = form.querySelector('input[type="date"]');
  if (date) date.min = new Date().toISOString().slice(0, 10);
  const tests = {
    req: (v) => v.trim() !== "",
    name: (v) => v.trim().length >= 2,
    zip: (v) => /^\d{5}$/.test(v.trim()),
    phone: (v) => /^0\d{9}$/.test(v.replace(/[\s.\-]/g, "").replace(/^\+33/, "0")),
    email: (v) => v.trim() === "" || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()),
  };
  const fields = [...form.querySelectorAll("[data-rule]")];
  const check = (el) => {
    const ok = tests[el.dataset.rule](el.value);
    el.closest(".field").classList.toggle("invalid", !ok);
    el.setAttribute("aria-invalid", String(!ok));
    return ok;
  };
  fields.forEach((el) => el.addEventListener("blur", () => { if (el.value !== "") check(el); }));

  const WHEN = { "Matin": "le matin", "Midi": "entre 12 h et 14 h", "Après-midi": "l'après-midi" };
  form.addEventListener("submit", (ev) => {
    ev.preventDefault();
    // Robots : champ piège rempli ou envoi en moins de 3 secondes
    if (document.getElementById("website").value !== "" || Date.now() - loadedAt < 3000) return;
    const bad = fields.filter((el) => !check(el));
    if (bad.length) { bad[0].focus(); return; }
    const first = document.getElementById("name").value.trim().split(/\s+/)[0];
    const picked = form.querySelector('input[name="when"]:checked');
    const when = picked ? WHEN[picked.value] : "";
    document.getElementById("successMsg").textContent =
      "Merci {first}. Nous vous rappelons {when} pour fixer la visite de votre projet.".replace("{first}", first).replace("{when}", when);
    document.getElementById("success").hidden = false;
  });
})();
