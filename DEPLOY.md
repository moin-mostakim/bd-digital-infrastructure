# Deploy to Vercel (moinmostakim account)

## One-time login

```bash
cd Depplearning/lectures/bd-digital-deck
npx vercel login
```

Use the GitHub/email linked to **moinmostakim** on [vercel.com](https://vercel.com).

## Production URL

After editing `../Bangladesh_Digital_Infrastructure.html`, sync and deploy:

```bash
cp ../Bangladesh_Digital_Infrastructure.html index.html
./scripts/prepare-vercel-output.sh
npx vercel deploy --prebuilt --prod
```

**Important:** Use `--prebuilt` after `prepare-vercel-output.sh`. A plain `vercel deploy` can build a broken route table and return **404**.

## Temporary link (no login, ~60 minutes)

```bash
cp ../Bangladesh_Digital_Infrastructure.html index.html
./scripts/prepare-vercel-output.sh
npx vercel deploy --prebuilt --temporary --yes
```

Open the `https://….tmp.now` URL from the CLI output. **Do not claim** until you want it on your account; after claim, run `vercel login` and use `--prebuilt --prod`.

Vercel will prompt for a project name (e.g. `bd-digital-infrastructure`).  
Your site will be at something like:

`https://bd-digital-infrastructure.vercel.app`

(or under your team subdomain).

## Claim a temporary deploy

If you used an anonymous `--temporary` link, open the **claim URL** from the CLI output while logged in to move it to your account.
