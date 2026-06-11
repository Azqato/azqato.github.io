# Product Tenets: Azqato Portfolio

These are the guiding principles for every decision made on this project. When two options conflict, the tenet higher on this list takes priority.

---

## 1. Speed Is a Feature; Everything Else Is Optional

A page that loads in under a second with five project cards is more valuable than a page that loads in three seconds with ten. Every addition (a library, a font, a third-party widget) must pay for itself in load time. If it can't, it doesn't ship.

*This tenet wins when debating whether to add a dependency, a new CDN resource, or a feature that requires external data.*

---

## 2. No Dependencies by Default

The default answer to "should we use a library for this?" is no. Vanilla HTML, CSS, and JavaScript can handle everything this portfolio needs. Dependencies rot, have security vulnerabilities, and create maintenance burden. The burden of proof is on adding a dependency, not on avoiding one.

*This tenet will conflict with Tenet 5 (low maintenance). When a library would genuinely reduce ongoing manual work, prefer the no-dependency solution unless the maintenance cost is severe and sustained.*

---

## 3. The Owner Must Be Able to Maintain This in Five Minutes

Adding a project, updating an affiliate link, or changing the theme should never require reading documentation. If the codebase reaches the point where the owner has to look something up to make a routine edit, it has grown too complex. Simplicity for the maintainer is a hard constraint, not a preference.

*This tenet loses to Tenet 1 only if a performance problem is severe and the fix genuinely simplifies maintenance (e.g., extracting a shared stylesheet that eliminates manual copy-paste).*

---

## 4. Transparency Before Conversion

The affiliate and support features exist to fund the work, but they must never obscure what the portfolio is. The affiliate disclosure appears above the fold. Links are clearly labeled. Nothing is disguised as editorial content. A visitor should never feel tricked.

*This tenet governs every decision on the Support page: disclosure placement, button copy, and card descriptions.*

---

## 5. Look Like a Developer Built It

The portfolio must look at home on GitHub. This means dark backgrounds, monospaced typography influences, accent colors that signal "interactive", and no stock photo hero images. The aesthetic itself communicates technical competence before the visitor reads a word.

*This tenet loses to Tenet 1 and Tenet 2 if achieving a specific visual requires a framework or a blocking resource. The aesthetic goal is achieved through CSS, not through tools.*
