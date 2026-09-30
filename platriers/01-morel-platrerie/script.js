/* Morel Plâtrerie · navigation, préremplissage et formulaire de démonstration */
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

  // Situations : préremplit le type de travaux puis descend au formulaire
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
        document.getElementById("name").focus({ preventScroll: true });
      }, 600);
    })
  );

  // Apparition douce des blocs
  const targets = document.querySelectorAll(".serv, .step-list li, .job, .review, .sit");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    targets.forEach((t) => { t.classList.add("reveal"); io.observe(t); });
  }

  // Formulaire de devis (démonstration : rien n'est envoyé)
  const form = document.getElementById("quoteForm");
  const loadedAt = Date.now();
  const rules = {
    work: (v) => v !== "",
    name: (v) => v.trim().length >= 2,
    zip: (v) => /^\d{5}$/.test(v.trim()),
    phone: (v) => v.replace(/[\s.\-]/g, "").replace(/^\+33/, "0").match(/^0\d{9}$/) !== null,
    email: (v) => v.trim() === "" || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()),
  };

  const check = (id) => {
    const el = document.getElementById(id);
    const ok = rules[id](el.value);
    el.closest(".field").classList.toggle("invalid", !ok);
    el.setAttribute("aria-invalid", String(!ok));
    return ok;
  };
  Object.keys(rules).forEach((id) =>
    document.getElementById(id).addEventListener("blur", () => {
      if (document.getElementById(id).value !== "") check(id);
    })
  );

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    // Robots : champ piège rempli ou envoi en moins de 3 secondes
    if (form.website.value !== "" || Date.now() - loadedAt < 3000) return;
    const results = Object.keys(rules).map(check);
    if (results.includes(false)) {
      form.querySelector(".invalid input, .invalid select").focus();
      return;
    }
    const when = form.querySelector('input[name="when"]:checked').value.toLowerCase();
    const first = document.getElementById("name").value.trim().split(/\s+/)[0];
    document.getElementById("successMsg").textContent =
      `Merci ${first}. Nous vous rappelons ${when === "midi" ? "entre 12 h et 14 h" : when === "matin" ? "le matin" : "l'après-midi"} pour fixer la visite de votre chantier.`;
    document.getElementById("success").hidden = false;
  });
})();
