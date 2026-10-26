"""
Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/reddit-community-pain-point-trend-miner ($0.50 / 1,000 posts)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~reddit-community-pain-point-trend-miner/run-sync-get-dataset-items"

payload = {
    "subreddits": [
        "saas",
        "entrepreneur",
        "seo"
    ],
    "intentFilter": "buyer-intent"
}

if __name__ == "__main__":
    print(f"Running Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
