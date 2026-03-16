"""Tests for Week 3 – Number Guessing Game."""

from week_03_guessing_game.main import calculate_score, pick_secret, play_round


def test_pick_secret_in_range():
    for _ in range(50):
        n = pick_secret(1, 100)
        assert 1 <= n <= 100


def test_calculate_score_first_guess():
    assert calculate_score(1, 7) == 100


def test_calculate_score_all_attempts():
    assert calculate_score(7, 7) == 0


def test_calculate_score_middle():
    score = calculate_score(4, 7)
    assert 0 < score < 100


def test_play_round_win(monkeypatch):
    secret = 42
    monkeypatch.setattr("builtins.input", lambda _: "42")
    result = play_round(secret, max_attempts=7)
    assert result["won"] is True
    assert result["attempts"] == 1
    assert result["score"] == 100


def test_play_round_lose(monkeypatch):
    secret = 42
    # Always guess wrong
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = play_round(secret, max_attempts=3)
    assert result["won"] is False
    assert result["score"] == 0
