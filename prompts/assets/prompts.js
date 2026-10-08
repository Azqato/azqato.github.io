/* Azqato's Prompts on azqato.com (item 22): the prompt block's Expand and
   Copy buttons, and the list search. Behavior as on the old site
   (github.com/Azqato/prompts, js/script.js). Nothing is stored. */
(function () {
  "use strict";

  // Word for word from the old site. Copy puts this sentence and the prompt's
  // page on the clipboard, never the prompt text: the agent fetches the page.
  var COPY_POINTER =
    'Review the full prompt on this website, provide a summary of what it does ' +
    'and then ask if I would like to run it: ';

  /* Expand / Hide. The whole bar toggles except the Copy button; the label
     names the action, not the state. Collapsed on every load. */
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

  /* Copy. A failure is said out loud: otherwise the reader pastes whatever
     was on the clipboard before. */
  var copy = document.querySelector(".copy-btn");
  if (copy) {
    var label = copy.getAttribute("aria-label");
    var flash = function (text, cls, aria) {
      copy.textContent = text;
      copy.classList.add(cls);
      copy.setAttribute("aria-label", aria);
      setTimeout(function () {
        copy.textContent = "Copy";
        copy.classList.remove(cls);
        copy.setAttribute("aria-label", label);
      }, 2000);
    };
    copy.addEventListener("click", function () {
      var text = COPY_POINTER + copy.getAttribute("data-url");
      if (!navigator.clipboard || !navigator.clipboard.writeText) {
        flash("Copy failed", "copy-failed", "Copy failed. Copy the page address instead");
        return;
      }
      navigator.clipboard.writeText(text).then(function () {
        flash("Copied!", "copied", "Copied!");
      }, function () {
        flash("Copy failed", "copy-failed", "Copy failed. Copy the page address instead");
      });
    });
  }

  /* Search: title and description, every word in any order, ignoring case.
     Enter opens the first match; Escape clears. */
  var box = document.getElementById("prompt-search");
  var empty = document.getElementById("pr-empty");
  if (box) {
    var items = [].slice.call(document.querySelectorAll(".pr-list li"));
    var apply = function () {
      var q = box.value.trim();
      var words = q.toLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      items.forEach(function (li) {
        var hay = li.textContent.toLowerCase();
        var hit = words.every(function (w) { return hay.indexOf(w) !== -1; });
        li.hidden = !hit;
        if (hit) shown++;
      });
      empty.textContent = shown ? "" : "No prompts match “" + q + "”.";
    };
    box.addEventListener("input", apply);
    box.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var first = items.filter(function (li) { return !li.hidden; })[0];
        if (first) window.location.href = first.querySelector("a").href;
      } else if (e.key === "Escape" && box.value) {
        box.value = "";
        apply();
      }
    });
    apply();
  }
})();
