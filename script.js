// Accordion
document.querySelectorAll('.accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const item = trigger.closest('.accordion-item');
    const body = item.querySelector('.accordion-body');
    const icon = trigger.querySelector('.accordion-icon');
    const isOpen = body.classList.contains('open');

    // Close all open items
    document.querySelectorAll('.accordion-body.open').forEach(openBody => {
      openBody.classList.remove('open');
      const openTrigger = openBody.closest('.accordion-item').querySelector('.accordion-trigger');
      openTrigger.setAttribute('aria-expanded', 'false');
      const openIcon = openTrigger.querySelector('.accordion-icon');
      if (openIcon) openIcon.textContent = '+';
    });

    // Toggle the clicked item
    if (!isOpen) {
      body.classList.add('open');
      trigger.setAttribute('aria-expanded', 'true');
      if (icon) icon.textContent = '-';
    }
  });
});

// IntersectionObserver for sidebar On This Page links (all pages)
const metricLinks = document.querySelectorAll('.metric-links a');
if (metricLinks.length > 0) {
  const sectionIds = Array.from(metricLinks).map(a => a.getAttribute('href').slice(1));
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        metricLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, {
    rootMargin: '-15% 0px -65% 0px',
    threshold: 0
  });

  sections.forEach(section => observer.observe(section));
}
