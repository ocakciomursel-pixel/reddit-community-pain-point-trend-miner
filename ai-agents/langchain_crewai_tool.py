"""
Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/reddit-community-pain-point-trend-miner ($0.50 / 1,000 posts)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~reddit-community-pain-point-trend-miner/run-sync-get-dataset-items"

def run_reddit_community_pain_point_trend_miner(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes Reddit Subreddit, Buyer Intent & Pain-Point Lead Miner on Apify Cloud ($0.50/1k posts).
    Mine Reddit subreddits for high-intent buyer posts ("looking for a tool", "alternative to", "how to automate"), software complaints, and emerging SaaS product opportunities.
    """
    default_payload = {
    "subreddits": [
        "saas",
        "entrepreneur",
        "seo"
    ],
    "intentFilter": "buyer-intent"
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
