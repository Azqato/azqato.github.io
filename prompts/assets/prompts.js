/* Azqato's Prompts on azqato.com (item 22): the old site's behavior
   (github.com/Azqato/prompts, js/script.js) on real pages: the sidebar's
   search and phone menu, and the prompt block's Expand and Copy. Nothing is
   stored, as before. */
(function () {
  "use strict";

  // Word for word from the old site. Copy puts this sentence and the prompt's
  // page on the clipboard, never the prompt text: the agent fetches the page.
  var COPY_POINTER =
    'Review the full prompt on this website, provide a summary of what it does ' +
    'and then ask if I would like to run it: ';

  /* ---------- Phone menu (below 1024px) ---------- */
  var sidebar = document.querySelector(".pr-site .sidebar");
  var menuBtn = document.getElementById("pr-nav-toggle");
  function setMenuOpen(open) {
    if (!sidebar || !menuBtn) return;
    sidebar.classList.toggle("nav-open", open);
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      setMenuOpen(!sidebar.classList.contains("nav-open"));
    });
  }

  /* ---------- Search ----------
     Title and description, every word in any order, ignoring case. Filters
     the sidebar links and, on the home page, the cards. Home stays listed.
     Enter opens the first match; Escape clears, or closes the menu. */
  var box = document.getElementById("prompt-search");
  var navLinks = [].slice.call(document.querySelectorAll(".sidebar-nav a[data-slug]"));
  var cards = [].slice.call(document.querySelectorAll(".prompt-list-item"));
  var text = {};
  cards.forEach(function (c) { text[c.getAttribute("data-slug")] = c.textContent.toLowerCase(); });
  navLinks.forEach(function (a) {
    var s = a.getAttribute("data-slug");
    if (!text[s]) text[s] = a.textContent.toLowerCase();
  });
  // On a prompt page there are no cards, so each sidebar link carries its
  // description in data-desc for the search.
  navLinks.forEach(function (a) {
    var d = a.getAttribute("data-desc");
    if (d) text[a.getAttribute("data-slug")] += " " + d.toLowerCase();
  });

  function applySearch() {
    if (!box) return;
    var q = box.value.trim();
    var words = q.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    function hit(slug) {
      return words.every(function (w) { return text[slug].indexOf(w) !== -1; });
    }
    navLinks.forEach(function (a) {
      var ok = hit(a.getAttribute("data-slug"));
      a.hidden = !ok;
      if (ok) shown++;
    });
    cards.forEach(function (c) { c.hidden = !hit(c.getAttribute("data-slug")); });
    var msg = shown ? "" : "No prompts match “" + q + "”.";
    ["search-empty", "home-empty"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = msg;
    });
  }
  if (box) {
    box.addEventListener("input", applySearch);
    box.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var first = navLinks.filter(function (a) { return !a.hidden; })[0];
        if (first) window.location.href = first.href;
      } else if (e.key === "Escape") {
        if (box.value) { box.value = ""; applySearch(); }
        else { setMenuOpen(false); if (menuBtn) menuBtn.focus(); }
      }
    });
    applySearch();
  }

  /* ---------- Expand / Hide ----------
     The whole bar toggles except Copy; the label names the action, not the
     state. Collapsed on every load. */
  var wrapper = document.querySelector(".code-block-wrapper");
  var header = document.querySelector(".code-block-header");
  var toggle = document.querySelector(".code-toggle");
  if (wrapper && header && toggle) {
    header.addEventListener("click", function (e) {
      if (e.target.closest(".copy-btn")) return;
      var collapsed = wrapper.classList.toggle("collapsed");
      toggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
      toggle.textContent = collapsed ? "Expand" : "Hide";
    });
  }

  /* ---------- Copy ----------
     A failure is said out loud: otherwise the reader pastes whatever was on
     the clipboard before. */
  var copy = document.querySelector(".copy-btn");
  if (copy) {
    var label = copy.getAttribute("aria-label");
    var flash = function (t, cls, aria) {
      copy.textContent = t;
      copy.classList.add(cls);
      copy.setAttribute("aria-label", aria);
      setTimeout(function () {
        copy.textContent = "Copy";
        copy.classList.remove(cls);
        copy.setAttribute("aria-label", label);
      }, 2000);
    };
    copy.addEventListener("click", function () {
      var t = COPY_POINTER + copy.getAttribute("data-url");
      if (!navigator.clipboard || !navigator.clipboard.writeText) {
        flash("Copy failed", "copy-failed", "Copy failed. Copy the page address instead");
        return;
      }
      navigator.clipboard.writeText(t).then(function () {
        flash("Copied!", "copied", "Copied!");
      }, function () {
        flash("Copy failed", "copy-failed", "Copy failed. Copy the page address instead");
      });
    });
  }
})();
