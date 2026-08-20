# CardWise — GitHub Pages

## Deploy
Upload all files and folders in this package to a GitHub repository.

Then:
Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → /(root) → Save.

Your URL will look like:
https://sandeep-joy.github.io/CardWise/

## Enable daily source check
Settings → Actions → General → Workflow permissions → Read and write permissions → Save.

Then:
Actions → Check official card sources → Run workflow.

The workflow runs daily and checks only allowlisted HTTPS public pages from Chase, Discover, U.S. Bank, Robinhood, and Costco.

No bank login, Plaid, card number, or transaction history is used.
