/* Azqato's Prompts on azqato.com (item 22): the old site's behavior
   (github.com/Azqato/prompts, js/script.js) on real pages: the home page's
   search, and the prompt block's Expand and Copy. Nothing is
   stored, as before. */
(function () {
  "use strict";

  // Word for word from the old site. Copy puts this sentence and the prompt's
  // page on the clipboard, never the prompt text: the agent fetches the page.
  var COPY_POINTER =
    'Review the full prompt on this website, provide a summary of what it does ' +
    'and then ask if I would like to run it: ';

  /* ---------- Search ----------
     On the Prompts home page: title and description, every word in any
     order, ignoring case. Enter opens the first match; Escape clears. (The
     old sidebar is gone: the Codes Contents sidebar lists every prompt.) */
  var box = document.getElementById("prompt-search");
  var cards = [].slice.call(document.querySelectorAll(".prompt-list-item"));

  function applySearch() {
    var q = box.value.trim();
    var words = q.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    cards.forEach(function (c) {
      var t = c.textContent.toLowerCase();
      var ok = words.every(function (w) { return t.indexOf(w) !== -1; });
      c.hidden = !ok;
      if (ok) shown++;
    });
    var msg = document.getElementById("home-empty");
    if (msg) msg.textContent = shown ? "" : "No prompts match “" + q + "”.";
  }
  if (box) {
    box.addEventListener("input", applySearch);
    box.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var first = cards.filter(function (c) { return !c.hidden; })[0];
        if (first) window.location.href = first.href;
      } else if (e.key === "Escape" && box.value) {
        box.value = "";
        applySearch();
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
