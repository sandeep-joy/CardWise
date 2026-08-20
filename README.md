# CardWise for GitHub Pages

Before uploading, edit `data/rules.json` and replace `YOUR-GITHUB-USERNAME` in `config.github_actions_url` with your GitHub username. If your repository is not named `cardwise`, change that part too.

The source-health panel has two distinct actions:

- **Reload last GitHub check** downloads the newest published `data/source_health.json` and displays its `checked_at` timestamp.
- **Run fresh check on GitHub** opens this repository's Actions workflow. Sign in to GitHub, choose **Run workflow**, wait for it to finish and for Pages to publish, then return to CardWise and reload the last check.

GitHub Pages is a public static host. It cannot safely call GitHub's authenticated workflow API without exposing a credential. CardWise therefore contains no GitHub token, password or personal access token.

## Publish

Upload everything in this folder to the repository root, including `.github`. In **Settings → Pages**, publish from `main` and `/ (root)`. The workflow has explicit `contents: write` permission; if repository policy blocks it, enable read/write workflow permissions under **Settings → Actions → General**.

The PWA continues to cache the app shell and rules for offline use. The health JSON is intentionally network-first so the reload button can obtain the newest published result.
