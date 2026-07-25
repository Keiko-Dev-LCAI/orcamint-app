# OrcaMint — Change Notes

## 2026-07-04 — Fix: blank page below "Download Android App" bar (mobile web)

**Symptom:** On mobile web, the page showed only the cyan "Download Android App"
button + install instructions at the top and the support chat bubble; everything
below was blank black space. Main app content (Discover/hero/NFT grid/wallet UI)
did not render.

**Root cause:** `body` uses `display:flex` (row) to lay out the fixed sidebar +
`#main`. The Android APK download bar (`.keiko-android-install`) had been appended
as a direct child of `<body>`, so it became a flex-row *sibling* of `#main`. Its
long instruction text gave it a wide flex-basis, which squeezed `#main` down to
0px width — collapsing all app content to an invisible sliver. (Sibling apps that
also have this download bar are unaffected because their `body` is not `display:flex`.)

**Fix:** Moved the `.keiko-android-install` block out of body-level and inside
`#main`, placed right after `<footer id="site-footer">`. `#main` is a flex column,
so the bar now sits as a full-width bar at the bottom of the main column and no
longer steals horizontal space. No CSS or JS logic changed.

**Verification (headless Chrome, 390px mobile viewport):**
- Before: `#main` width = 0px, hero not visible → blank page (reproduced the bug).
- After: `#main` width = 390px, hero visible, Discover section active, NFT grid
  populated, download bar full-width inside `#main`. No new console errors.

**Files changed:** `index.html` (block relocated; comment added explaining why).
