(function () {
  var anchorLinks = document.querySelectorAll('.anchor-link');

  if (anchorLinks.length > 0) {
    var sectionIds = Array.from(anchorLinks).map(function (link) {
      return link.getAttribute('href').slice(1);
    });

    var sections = sectionIds
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);

    if (sections.length > 0) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              anchorLinks.forEach(function (link) {
                link.classList.remove('is-active');
              });
              var id = entry.target.id;
              var active = document.querySelector('.anchor-link[href="#' + id + '"]');
              if (active) active.classList.add('is-active');
            }
          });
        },
        { rootMargin: '-15% 0px -80% 0px', threshold: 0 }
      );

      sections.forEach(function (section) {
        observer.observe(section);
      });
    }
  }

  var toggle = document.querySelector('.nav-toggle');
  var mobileNav = document.getElementById('mobile-nav');

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      mobileNav.hidden = expanded;
    });
  }
})();
