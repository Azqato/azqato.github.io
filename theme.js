/*
 * Light and dark themes for the whole site (build pass item 5, 2026-10-02).
 * One script for azqato.com's pages and Azqato Invests, moved here from
 * invests/assets/js/theme.js (itself adapted from Template Interface's
 * theme-toggle.js, commit ed840da). Loaded in the head, without defer, so the
 * theme is set on <html data-theme> before the first paint.
 *
 * A visitor with no saved choice gets their system theme. The choice is saved
 * under one key for the whole site, in the visitor's browser only; a choice
 * saved under Invests' old key still counts.
 *
 * A page whose <html> carries data-theme-lock="dark" (music.html: the
 * visualizer is drawn for a dark room) stays dark and has no button.
 *
 * Any <button class="theme-toggle"> becomes the toggle. It shows the theme it
 * switches to (a sun while dark, a moon while light) and its accessible name
 * states the action.
 */
(function () {
  "use strict";

  var KEY = "azqato-theme";
  var OLD_KEY = "azqato-invests-theme";
  var root = document.documentElement;
  var lock = root.getAttribute("data-theme-lock");

  function read(key) {
    try {
      var v = window.localStorage.getItem(key);
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

  root.setAttribute("data-theme", lock || read(KEY) || read(OLD_KEY) || system());

  function sync(button) {
    var dark = root.getAttribute("data-theme") === "dark";
    var icon = button.querySelector(".theme-toggle-icon");
    if (icon) icon.textContent = dark ? "☀️" : "🌙";
    button.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }

  function bind() {
    var buttons = document.querySelectorAll(".theme-toggle");
    buttons.forEach(function (button) {
      if (lock) { button.hidden = true; return; }
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
