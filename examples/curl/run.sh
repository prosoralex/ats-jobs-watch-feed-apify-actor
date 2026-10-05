#!/usr/bin/env bash
# Run the "Greenhouse Jobs Scraper: Lever & Ashby Job Feed" Apify Actor synchronously and print the dataset items.
# Usage: export APIFY_TOKEN=your_apify_token && ./run.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first (Apify Console > Settings > API & Integrations)}"

curl -sS -X POST "https://api.apify.com/v2/acts/leadsbrary~ats-jobs-watch-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
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
