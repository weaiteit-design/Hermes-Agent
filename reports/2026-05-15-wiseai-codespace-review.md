# WiseAI Codespace Review — 2026-05-15

## Repositories inspected

- Mobile app: `/root/Hermes-Agent/external-repos/Delta-`
  - GitHub: `weaiteit-design/Delta-`
  - Branch: `main`
  - Status during review: clean
- Landing page: `/root/Hermes-Agent/external-repos/wiseai-landing`
  - GitHub: `weaiteit-design/wiseai-landing`
  - Branch: `landing-page`
  - Status during review: clean

## Summary

WiseAI is split across a mobile app repo and a landing page repo.

- Landing page is close to production.
- Mobile app is not launch-ready yet. It is in a partial web-to-Expo migration state.

## Mobile app findings

Path: `/root/Hermes-Agent/external-repos/Delta-`

### Current state

The repo has Expo/React Native files, but still includes web/Vite leftovers:

- `index.html`
- `index.tsx`
- `vite.config.ts`
- `vite-env.d.ts`

Several components still use browser/web React patterns:

- `<div>`
- `<button>`
- `<input>`
- `className`
- `onClick`
- browser-only APIs

This means the app is not yet a clean native Expo app.

### Verification commands run

```bash
npx tsc --noEmit
npx expo config --type public
npx expo-doctor
npm audit --omit=dev --audit-level=moderate
```

### Results

`npx tsc --noEmit` failed with issues including:

- `lucide-react` imports while the app has `lucide-react-native`
- `Dashboard` prop mismatch for `onSignOut`
- missing service methods:
  - `fetchNewsForInterests`
  - `findToolsForUseCase`
- Vite config included in typechecking without Vite dependencies
- strict null/type issues in `deltaService.ts`

`npx expo-doctor` failed 2 checks:

- Invalid config property: `android.edgeToEdgeLayoutEnabled`
- Missing assets:
  - `assets/icon.png`
  - `assets/splash-icon.png`
  - `assets/adaptive-icon.png`
- Dependency mismatches:
  - `react-native` expected `0.76.9`, found `0.76.5`
  - `@expo/vector-icons` expected `~14.0.4`, found `14.1.0`

`npm audit --omit=dev --audit-level=moderate` reported vulnerabilities, including one critical through `protobufjs`.

### Security note

A tracked `.env` exists in the mobile repo, and API-related values were found in tracked files. Treat these as exposed and rotate relevant keys before production.

## Landing page findings

Path: `/root/Hermes-Agent/external-repos/wiseai-landing`

### Current state

The landing page is a Next.js app with:

- homepage
- waitlist form
- privacy page
- terms page
- OG image and baseline metadata

### Verification commands run

```bash
npx tsc --noEmit --incremental false
npm run lint
NEXT_PUBLIC_SUPABASE_URL=https://example.supabase.co NEXT_PUBLIC_SUPABASE_ANON_KEY=dummy npm run build
npm audit --omit=dev --audit-level=moderate
```

### Results

TypeScript passed:

```bash
npx tsc --noEmit --incremental false
```

Production build passed when Supabase env vars were supplied:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://example.supabase.co NEXT_PUBLIC_SUPABASE_ANON_KEY=dummy npm run build
```

Generated routes:

- `/`
- `/privacy`
- `/terms`
- `/api/waitlist`

Lint failed with 15 errors:

- unescaped apostrophes in:
  - `src/app/privacy/page.tsx`
  - `src/app/terms/page.tsx`
  - `src/components/Features.tsx`
- React hook lint issue in:
  - `src/components/WaitlistForm.tsx`

Security audit failed:

- Next.js high severity advisories
- PostCSS moderate advisory
- likely fix: update Next from `16.1.6` to a patched version such as `16.2.6`

## Recommendation

### Phase 1: Ship landing page first

This is the fastest win.

Tasks:

1. Fix lint errors.
2. Update Next.js / PostCSS dependency chain.
3. Make Supabase env handling safer.
4. Add security headers.
5. Change fake “Now Available” copy to waitlist messaging if app is not live.
6. Add `robots.txt`, `sitemap.xml`, manifest, and structured data.
7. Add waitlist hardening:
   - honeypot
   - UTM length/type validation
   - server-backed throttling or CAPTCHA
   - verify Supabase RLS and unique index on `waitlist.email`

### Phase 2: Refactor mobile app properly

Tasks:

1. Decide architecture:
   - Expo Router with `/app`, or
   - classic `App.tsx` entry
2. Remove Vite/web leftovers.
3. Port UI to React Native primitives.
4. Replace `lucide-react` with `lucide-react-native`.
5. Add missing service methods.
6. Fix Expo assets/config.
7. Add EAS config, iOS build number, Android version code.
8. Add account deletion flow.
9. Clean secrets and rotate exposed keys.

## Short verdict

- Landing page: close, fixable quickly.
- Mobile app: needs focused migration/refactor before app store submission.
