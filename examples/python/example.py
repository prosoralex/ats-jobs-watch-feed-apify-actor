"""
Run the "Greenhouse Jobs Scraper: Lever & Ashby Job Feed" Apify Actor and print its results.

Setup:
    pip install -r requirements.txt
    export APIFY_TOKEN=your_apify_token   # Apify Console > Settings > API & Integrations

This repository only documents the Actor; its source code runs on Apify's infrastructure.
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "leadsbrary/ats-jobs-watch-feed"

RUN_INPUT = {
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


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).")
    client = ApifyClient(token)
    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
