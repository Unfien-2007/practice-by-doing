# Week 5: Web Scraper

**Difficulty:** Intermediate

## Learning Goals
- Make HTTP requests using the `requests` library
- Parse HTML with `BeautifulSoup`
- Extract structured data from web pages
- Write scraped data to a CSV file

## Project Description
Scrape the top stories from Hacker News (`news.ycombinator.com`) and save the
results (title, URL, score, author) to a CSV file.

## Concepts Covered
- `requests.get()` and HTTP status codes
- HTML parsing with `BeautifulSoup`
- CSS selectors and tag navigation
- Writing CSV files with the `csv` module
- Basic data cleaning

## Setup
```bash
pip install requests beautifulsoup4
```

## How to Run
```bash
python main.py
# Creates hn_stories.csv in the same directory
```

## Sample Output
```
Fetching Hacker News front page...
Scraped 30 stories.
Saved to hn_stories.csv

Top 5 stories:
  1. [450 pts] Show HN: I built a … – https://…
  2. [312 pts] Ask HN: What are …   – https://…
  ...
```

## Challenges
1. Scrape multiple pages (add pagination support).
2. Filter stories by minimum score threshold.
3. Track new stories by comparing with a previous run's CSV.
