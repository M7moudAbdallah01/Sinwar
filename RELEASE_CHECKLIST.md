# SINWAR v1.0.0 Release Checklist

## Before Release

- [ ] Run `python3 cli.py`
- [ ] Test Crypto menu
- [ ] Test Network menu
- [ ] Test Web Security menu
- [ ] Test Encoding menu
- [ ] Test Password Manager
- [ ] Verify `requirements.txt`
- [ ] Verify `.gitignore`
- [ ] Confirm `passwords.json` is not tracked
- [ ] Review README
- [ ] Review CHANGELOG
- [ ] Add/update LICENSE
- [ ] Remove secrets and personal data
- [ ] Commit and push to `main`

## Git

```bash
git status
git add .
git commit -m "Release v1.0.0"
git push origin main
```

## GitHub Release

Create a new GitHub Release:

- Tag: `v1.0.0`
- Target: `main`
- Title: `SINWAR v1.0.0`
- Description: copy `RELEASE_NOTES_v1.0.0.md`

Then publish the release.

## After Release

Verify:

- [ ] Release appears under GitHub Releases
- [ ] Tag exists
- [ ] README installation commands work
- [ ] Repository has no accidentally committed secrets
