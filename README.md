# Bangladesh Digital Infrastructure — interactive deck

Story-driven HTML presentation (2G KrishiBill + TrailGuard prototypes).

## Live (after GitHub Pages deploy)

`https://moin-mostakim.github.io/bd-digital-infrastructure/`

## Local

```bash
./open-local.sh
# or: python3 -m http.server 8765
```

## Update content

Edit `../Bangladesh_Digital_Infrastructure.html`, then:

```bash
cp ../Bangladesh_Digital_Infrastructure.html index.html
git add index.html && git commit -m "Update deck" && git push
```

GitHub Actions publishes **main** to Pages automatically.

## Vercel (Git)

1. [Import repo](https://vercel.com/new) → `moin-mostakim/bd-digital-infrastructure`
2. Framework: **Other**, root: `.`, build: empty, output: `.`
3. Deploy — every `git push` redeploys.

Or CLI (after `vercel login`):

```bash
./scripts/prepare-vercel-output.sh
npx vercel deploy --prebuilt --prod
```
