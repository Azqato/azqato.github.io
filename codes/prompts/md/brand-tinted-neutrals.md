---
title: Brand-Tinted Neutrals
description: Replace an interface's pure greys with a scale tinted by the brand color, so every background, surface, border and text color carries a quiet trace of the brand.
meta: Claude Code Prompt
---

Gives an interface a brand feel without adding brand color anywhere new. It takes the brand's base color and builds one scale of shades from near-white to near-black, all faintly tinted with it, then uses those shades for every neutral in the interface: backgrounds, cards, borders, dividers and text. Light text becomes a very light tint of the brand, and a dark background becomes a very dark one. Few people notice the change, but the interface feels like it belongs to the brand.

It works well where status colors could otherwise drown out the brand, such as trading or finance interfaces, where gains and losses are colored green and red. The tint is kept low, so gains, losses, warnings and links stay as clear as before and the brand color itself keeps its job as the accent.

Claude reads the project first, finds where colors are defined and lists every grey in use. It proposes the scale, with a swatch page and a contrast table for both themes, and changes nothing until you approve. It then swaps the greys for the new tokens, checks every text and border pair for contrast, compares screenshots before and after, and ends with the files changed and the checks it ran.

## Prompt

```
Replace the pure greys in this interface with a neutral scale tinted by the brand's base color, so every background, surface, border and text color carries a quiet trace of the brand. Propose the scale first, get my approval, then apply it.

Read first
- Read the project's own instructions, README and design docs before acting, and follow any color, theme or accessibility rules they set.
- Find where colors are defined: CSS custom properties, a theme or tokens file, a Tailwind or framework config, a design-system package, or values written inline.
- Find the brand's base color in those sources. If there is more than one candidate, or none, stop and ask me which to use.
- Work out which themes the interface has (light, dark, or both) and how the theme is chosen.

Audit (change nothing yet)
- With a script, list every neutral color in use, meaning any grey, white or black, including near-greys with very low saturation: its value, where it is defined, how many places use it, and its role (page background, surface, raised surface, border, divider, primary text, secondary text, muted text, disabled).
- Note colors written inline rather than through a token. Each is a finding, since it will not follow the new scale.
- List the status and accent colors (success, danger, warning, info, links, the brand accent) separately. These are not neutrals and are not changed.

Build the scale
- Generate 10 to 12 steps from near-white to near-black, in a perceptual color space (OKLCH, or CIELAB if OKLCH is not available), all with the brand color's hue.
- Keep the tint low: chroma about 0.005 to 0.02 in OKLCH, or the equivalent. Use the lowest chroma at the lightest and darkest steps and a little more in the middle steps, so white and black read as tinted white and tinted black, never as pale or deep brand color.
- The lightest step must still read as white and the darkest as black. If the result looks colored rather than tinted, lower the chroma.
- Map each role from the audit to one step in each theme, for example: page background, surface and raised surface; border and divider; primary, secondary and muted text.
- Check every text and background pair, and every border against its background, with the WCAG formula, in both themes: text at least 4.5:1, large text and control borders at least 3:1. Where a pair fails, choose a different step rather than lowering the bar.
- Check that the status colors still read clearly against the new backgrounds and pass 4.5:1 where they are used as text. Report any that change from passing to failing.

Proposal (then stop)
- Build a swatch page: the scale with each step's value, the role-to-step table for each theme, a sample of the main interface (a card, a table row, body text, a button, positive and negative values) in both themes, and the contrast table with pass or fail for every pair.
- Render it in headless Microsoft Edge (or Chrome if Edge is not installed) and look at the screenshots, not the code.
- Show me the swatch page, the old-to-new mapping, and the inline colors you found. Do not change the interface until I approve.

Apply, after approval
- Define the scale once, as tokens in the project's existing color system, named by step (for example --neutral-50 to --neutral-950) with role tokens on top (for example --color-surface, --color-text-muted).
- Point every neutral the audit found at the role tokens. Replace inline greys with tokens too.
- Do not change status colors, the brand accent, images, logos or charts' data colors.
- Keep the existing theme switching exactly as it works today.
- Ask before installing any new dependency.

Verify
- Screenshot the main screens before and after, in both themes and at phone width, and compare them. The change should be felt, not seen: if a screen now looks blue (or whatever the brand color is) rather than neutral, lower the chroma and repeat.
- Rerun the contrast check against the applied colors on the real pages, not only the swatch page.
- Search the code again for pure greys and inline colors that were missed.
- Run the project's tests, lint and build.

Report, in this order
1. The base color and the scale: each step's value and chroma.
2. The role-to-step table for each theme.
3. The contrast table: every pair, its ratio, pass or fail.
4. Files changed, and the inline colors replaced.
5. Before and after screenshots, and the checks run with whether each passed.
6. Anything left as a grey, and why.

Do not commit anything.
```
