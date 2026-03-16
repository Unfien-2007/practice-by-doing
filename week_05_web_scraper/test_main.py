"""Tests for Week 5 – Web Scraper (no network calls)."""

import csv
import textwrap
from pathlib import Path

import pytest
from week_05_web_scraper.main import parse_stories, save_to_csv


SAMPLE_HTML = textwrap.dedent("""\
    <html><body>
    <table>
      <tr class="athing" id="1">
        <td class="title">
          <span class="rank">1.</span>
          <span class="titleline"><a href="https://example.com">Example Story</a></span>
        </td>
      </tr>
      <tr>
        <td class="subtext">
          <span class="score">100 points</span>
          by <a class="hnuser">alice</a>
        </td>
      </tr>
      <tr class="athing" id="2">
        <td class="title">
          <span class="rank">2.</span>
          <span class="titleline"><a href="https://other.com">Other Story</a></span>
        </td>
      </tr>
      <tr>
        <td class="subtext">
          <span class="score">50 points</span>
          by <a class="hnuser">bob</a>
        </td>
      </tr>
    </table>
    </body></html>
""")


def test_parse_stories_count():
    stories = parse_stories(SAMPLE_HTML)
    assert len(stories) == 2


def test_parse_stories_fields():
    stories = parse_stories(SAMPLE_HTML)
    first = stories[0]
    assert first["rank"] == "1"
    assert first["title"] == "Example Story"
    assert first["url"] == "https://example.com"
    assert first["score"] == "100"
    assert first["author"] == "alice"


def test_save_to_csv(tmp_path):
    stories = [
        {"rank": "1", "title": "T", "url": "http://t.com", "score": "10", "author": "u"}
    ]
    out = tmp_path / "test.csv"
    save_to_csv(stories, path=out)
    assert out.exists()
    rows = list(csv.DictReader(out.open(encoding="utf-8")))
    assert len(rows) == 1
    assert rows[0]["title"] == "T"
