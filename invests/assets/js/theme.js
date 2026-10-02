/*
 * Light and dark themes (D10). Adapted from Template Interface's
 * assets/js/theme-toggle.js (commit ed840da): loaded in the head, without
 * defer, so the theme is set on <html data-theme> before the first paint.
 * Changed for this site: a visitor with no saved choice gets their system
 * theme (the template defaults to dark), and the choice is saved under this
 * site's own key, in the visitor's browser only.
 *
 * Any <button class="theme-toggle"> becomes the toggle. It shows the theme it
 * switches to (a sun while dark, a moon while light) and its accessible name
 * states the action.
 */
(function () {
  "use strict";

  var KEY = "azqato-invests-theme";
  var root = document.documentElement;

  function stored() {
    try {
      var v = window.localStorage.getItem(KEY);
      return v === "light" || v === "dark" ? v : null;
    } catch (e) {
      return null;
    }
  }

  function system() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function save(mode) {
    try { window.localStorage.setItem(KEY, mode); } catch (e) { /* storage blocked: the choice lasts this page only */ }
  }

  root.setAttribute("data-theme", stored() || system());

  function sync(button) {
    var dark = root.getAttribute("data-theme") === "dark";
    var icon = button.querySelector(".theme-toggle-icon");
    if (icon) icon.textContent = dark ? "☀️" : "🌙";
    button.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }

  function bind() {
    var buttons = document.querySelectorAll(".theme-toggle");
    buttons.forEach(function (button) {
      sync(button);
      button.addEventListener("click", function () {
        var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        save(next);
        buttons.forEach(sync);
        document.dispatchEvent(new CustomEvent("site-theme", { detail: next }));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
