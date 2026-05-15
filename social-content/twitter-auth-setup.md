# Twitter/X Auth Setup Notes

Manas shared Twitter/X developer credentials in Telegram on 2026-05-15. Do not store or transcribe those secrets in project files, memory, or chat logs.

Security recommendation: rotate/regenerate the exposed keys in the X Developer Portal because they were shared through chat/screenshot.

## Current status

X/Twitter posting is configured via `xurl`:

- App name: `manas-x`
- Default user: `manas_builds`
- Verified by: `xurl whoami`
- Account: Manas Gaikwad (`@manas_builds`)

Do not read or expose `~/.xurl`; it contains auth material.

## Operational notes

- Use `xurl auth status` to verify auth without exposing secrets.
- Use `xurl whoami` as a cheap reachability check.
- Use `xurl post "..."` for posting after Manas approves final copy, unless he explicitly authorizes automated posting for a specific scheduled job.
- For media, upload first with `xurl media upload <file>`, then post with `--media-id`.

## Required X app settings

- User authentication: enabled
- App permissions: Read and write
- Type of App: Web app, Automated App or Bot
- Callback / redirect URI: http://localhost:8080/callback
- Website URL: any valid owned/project URL, if required by X
