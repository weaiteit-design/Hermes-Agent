# Release QA

Release candidate verified on 2026-08-05 against the public preview.

## Automated checks

- JavaScript syntax: pass (`node --check assets/app.js`)
- Asset references: 72 checked, 0 missing
- Desktop viewport: 1440 × 1000, HTTP 200, 0 horizontal overflow, 0 broken images, 0 console errors
- Mobile viewport: 390 × 844, HTTP 200, 0 horizontal overflow, 0 broken images, 0 console errors
- Hero: 16 cards; pinned at viewport top from start through end; exact horizontal travel reached on desktop and mobile
- Creative heading: exact split text `creative visuals`; visible on desktop and mobile
- Scroll progress element: absent
- Orbit paths: hidden
- Chrome planets: 0 detected overlaps on desktop and mobile
- Dome transitions: start, black hold and white return captured for all three transitions

## Visual checks

Targeted screenshots were captured at hero start/mid/end, chrome brand system, creative visuals, and each transition phase for desktop and mobile. No release-blocking clipping, overflow or blank-content failures were found.
