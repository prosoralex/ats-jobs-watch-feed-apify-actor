// Run the "Greenhouse Jobs Scraper: Lever & Ashby Job Feed" Apify Actor and print its results.
// Setup: npm install  &&  export APIFY_TOKEN=your_apify_token  &&  node example.mjs
// This repository only documents the Actor; its source code runs on Apify's infrastructure.
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).');
    process.exit(1);
}

const client = new ApifyClient({ token });

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
console.log(`Run finished with status: ${run.status}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
