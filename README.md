# Greenhouse Jobs Scraper: Lever & Ashby Job Feed — Apify Actor usage guide

[![Run on Apify](https://img.shields.io/badge/Apify-Run%20this%20Actor-24C1E0)](https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara)
[![Try Apify free](https://img.shields.io/badge/Apify-Try%20it%20free-24C1E0)](https://console.apify.com/sign-up?fpr=aupara)

Greenhouse jobs scraper for Lever and Ashby too: get jobs by company name, domain or careers URL with title, location, remote flag, salary and apply link as JSON, CSV or Excel. Watch mode returns new, changed and closed jobs. From $1/1,000 results.

> **This repository does not contain the Actor's source code.** The Actor is closed-source and
> runs on Apify's infrastructure. This repo is documentation plus ready-to-run client examples
> (curl, Python, JavaScript) that call the hosted Actor with **your own** Apify API token.

**Run it on Apify →** [https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara](https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara)

## What it does

This Greenhouse jobs scraper also reads **Lever** and **Ashby** career boards. Give it company names, domains, career-page URLs or board tokens. It finds each company's job board and returns every open posting in one normalized format: title, department, locations, remote flag, salary (when published), description and direct apply URL.

In **watch mode** it remembers the previous run and returns only the **new, changed and closed** postings, so a daily schedule stays small and cheap.

It reads the public job-board APIs that Greenhouse, Lever and Ashby publish for third parties. No login, no browser and no proxy is involved.

## Use cases

- Hiring-signal lead lists: which target accounts are hiring for role X (e.g. 'data engineer', 'RevOps') right now
- Daily scheduled 'new jobs since last run' feed to Slack, Google Sheets or a webhook
- Job-board / newsletter aggregation with direct apply URLs and normalized salary and remote fields
- Detect closed postings (a role was filled or frozen) for competitive intelligence or to clean up job-board listings
- Give AI agents structured, fresh job data per company


## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `companies` | array | yes | Board URLs (boards.greenhouse.io/stripe, jobs.lever.co/palantir, jobs.ashbyhq.com/linear), bare board tokens, company domains (stripe.com), careers page URLs or company names. The ATS and token are detected automatically. |
| `ats` | string | no | Force one ATS for bare tokens and names, or let the Actor detect it. |
| `mode` | string | no | 'all' returns every open posting. 'watch' returns only NEW, CHANGED and CLOSED postings since the previous run with the same watch name (the first watch run returns everything as NEW). |
| `watchStateName` | string | no | Each name keeps its own snapshot, so several schedules run independently. Only a-z, 0-9 and '-'. |
| `titleKeywords` | array | no | Keep only jobs whose title contains any of these words (case-insensitive). |
| `locationKeywords` | array | no | Keep only jobs whose location text contains any of these words (case-insensitive). |
| `remoteOnly` | boolean | no | Keep only jobs flagged as remote. |
| `includeDescription` | boolean | no | Include plain-text and HTML job descriptions. Turn off for lighter rows. |
| `maxJobsPerCompany` | integer | no | Cap per company (0 = no cap). |
| `maxResults` | integer | no | Stop after this many rows in total (also protects your spending). |

The full input form (with defaults and validation) is on the [Actor page](https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara).


## Output (sample item)

Sample trimmed for readability (long texts and lists are shortened) — a real run returns the complete data.

```json
{
  "jobId": "greenhouse:stripe:8172508",
  "ats": "greenhouse",
  "boardToken": "stripe",
  "companyInput": "stripe",
  "companyName": "Stripe",
  "title": "Abuse Investigator",
  "department": "8611 Security Analytics",
  "locations": [
    "Dublin"
  ],
  "country": null,
  "isRemote": false,
  "workplaceType": null,
  "employmentType": null,
  "seniority": null,
  "salaryMin": null,
  "salaryMax": null,
  "salaryCurrency": null,
  "salaryPeriod": null,
  "salaryText": null,
  "descriptionText": null,
  "descriptionHtml": null,
  "jobUrl": "https://stripe.com/jobs/search?gh_jid=8172508",
  "applyUrl": "https://stripe.com/jobs/search?gh_jid=8172508#app",
  "publishedAt": "2026-09-03T17:32:53.000Z",
  "updatedAt": "2026-09-25T20:45:00.000Z",
  "changeType": null,
  "changedFields": null,
  "firstSeenAt": null,
  "closedAt": null,
  "scrapedAt": "2026-10-04T10:20:49.237Z"
}
```

## Pricing

Pay only for results: about **$1.50 per 1,000 results** on the Apify Free plan, down to **$1.00 per 1,000** on paid Apify plans.

Apify platform usage (compute) is billed by Apify on top of the per-result price — about **$0.01 per 1,000 results** in our measured test runs (estimate, varies with input). Tip: keep only the output formats and options you need to reduce it.

Prices can change — the [Actor page](https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara) always shows the current pricing.

## Quick start

You need an Apify account and an API token (Apify Console → **Settings → API & Integrations**).
Never commit your token: export it as the `APIFY_TOKEN` environment variable.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~ats-jobs-watch-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "companies": [
    "stripe",
    "jobs.lever.co/palantir"
  ],
  "ats": "auto",
  "mode": "all",
  "watchStateName": "default",
  "titleKeywords": [],
  "locationKeywords": [],
  "remoteOnly": false,
  "includeDescription": true,
  "maxJobsPerCompany": 0,
  "maxResults": 3
}
JSON
```

### Python (`apify-client`)

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "companies": [
        "stripe",
        "jobs.lever.co/palantir"
    ],
    "ats": "auto",
    "mode": "all",
    "watchStateName": "default",
    "titleKeywords": [],
    "locationKeywords": [],
    "remoteOnly": False,
    "includeDescription": True,
    "maxJobsPerCompany": 0,
    "maxResults": 3
}

run = client.actor("leadsbrary/ats-jobs-watch-feed").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const runInput = {
  "companies": [
    "stripe",
    "jobs.lever.co/palantir"
  ],
  "ats": "auto",
  "mode": "all",
  "watchStateName": "default",
  "titleKeywords": [],
  "locationKeywords": [],
  "remoteOnly": false,
  "includeDescription": true,
  "maxJobsPerCompany": 0,
  "maxResults": 3
};

const run = await client.actor('leadsbrary/ats-jobs-watch-feed').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Runnable versions live in [`examples/`](./examples).

## Troubleshooting

- **401 / "User was not found or authentication token is not valid"** — check that `APIFY_TOKEN` is set and copied completely.
- **The run finished but the dataset is empty** — widen your search input or check the run log on the Apify Console.
- **Run stops early** — you may have reached the maximum cost per run you set in Apify; raise it in the run options.
- **Need something else?** Open an issue in this repository or use the Issues tab on the Actor page.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get $5 of free platform usage every month, enough to try most Actors without paying upfront.
Browse the full [Apify Store](https://apify.com/store?fpr=aupara) or [all Actors from this developer](https://apify.com/leadsbrary?fpr=aupara).

## Links

- Actor page: [https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara](https://apify.com/leadsbrary/ats-jobs-watch-feed?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API reference: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## Keywords

greenhouse jobs scraper, lever jobs api, ashby jobs scraper, ats job feed, career page scraper, greenhouse job board api, lever jobs scraper, new job alerts, hiring signals, company job postings, job change monitor, career site jobs api

#greenhouse #lever #ashby #jobs #jobscraper #ats #careerpages #hiringsignals #recruiting #leadgeneration #jobalerts

## License

The example code in this repository is released under the MIT License — see [LICENSE](./LICENSE).
It does not cover the Actor itself, which remains closed-source and is operated by its developer on Apify.
