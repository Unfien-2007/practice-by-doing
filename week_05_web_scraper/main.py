"""
Week 5 – Web Scraper
---------------------
Scrapes the Hacker News front page and saves story data to a CSV file.

Requirements:
    pip install requests beautifulsoup4
"""

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
OUTPUT_FILE = Path(__file__).parent / "hn_stories.csv"
CSV_HEADERS = ["rank", "title", "url", "score", "author"]


def fetch_page(url: str) -> str:
    """Fetch the raw HTML for *url* and return it as a string."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_stories(html: str) -> list[dict]:
    """
    Parse the Hacker News front-page HTML and return a list of story dicts.

    Each dict contains: rank, title, url, score, author.
    """
    soup = BeautifulSoup(html, "html.parser")
    stories: list[dict] = []

    title_rows = soup.select("tr.athing")
    for row in title_rows:
        rank_tag = row.select_one("span.rank")
        title_tag = row.select_one("span.titleline > a")
        if not rank_tag or not title_tag:
            continue

        rank = rank_tag.get_text(strip=True).rstrip(".")
        title = title_tag.get_text(strip=True)
        url = title_tag.get("href", "")

        # The subtext row is the next sibling
        subtext = row.find_next_sibling("tr")
        score = "0"
        author = ""
        if subtext:
            score_tag = subtext.select_one("span.score")
            author_tag = subtext.select_one("a.hnuser")
            if score_tag:
                score = score_tag.get_text(strip=True).split()[0]
            if author_tag:
                author = author_tag.get_text(strip=True)

        stories.append(
            {"rank": rank, "title": title, "url": url, "score": score, "author": author}
        )

    return stories


def save_to_csv(stories: list[dict], path: Path = OUTPUT_FILE) -> None:
    """Write *stories* to a CSV file at *path*."""
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(stories)


def main() -> None:
    print("Fetching Hacker News front page...")
    html = fetch_page(HN_URL)
    stories = parse_stories(html)
    save_to_csv(stories)

    print(f"Scraped {len(stories)} stories.")
    print(f"Saved to {OUTPUT_FILE}\n")

    print("Top 5 stories:")
    for story in stories[:5]:
        print(f"  {story['rank']}. [{story['score']} pts] {story['title']}")
        print(f"     {story['url']}")


if __name__ == "__main__":
    main()
