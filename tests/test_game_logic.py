import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

# Tests for check_guess - validates the high/low hint fix
def test_winning_guess():
    """If the secret is 50 and guess is 50, it should be a win with correct message."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    """If secret is 50 and guess is 60, hint should say 'Go LOWER!' (the bug fix)."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"  # This was "📈 Go HIGHER!" before the fix
    assert "LOWER" in message  # Ensure it's the corrected message

def test_guess_too_low():
    """If secret is 50 and guess is 40, hint should say 'Go HIGHER!' (the bug fix)."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"  # This was "📉 Go LOWER!" before the fix
    assert "HIGHER" in message  # Ensure it's the corrected message

def test_guess_too_high_extreme():
    """Edge case: guess 200 when secret is 50 should still say 'Go LOWER!'."""
    outcome, message = check_guess(200, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

# Tests for parse_guess
def test_parse_valid_integer():
    """Parse a valid integer input."""
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_valid_float():
    """Parse a float and convert to integer."""
    ok, value, error = parse_guess("42.7")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_invalid_input():
    """Parse invalid input should return error."""
    ok, value, error = parse_guess("not a number")
    assert ok is False
    assert value is None
    assert error is not None

def test_parse_empty_input():
    """Empty input should return error."""
    ok, value, error = parse_guess("")
    assert ok is False
    assert error == "Enter a guess."

def test_parse_none_input():
    """None input should return error."""
    ok, value, error = parse_guess(None)
    assert ok is False
    assert error == "Enter a guess."

# Tests for update_score
def test_update_score_win():
    """Winning on first attempt gives max points: 100 - 10*(1+1) = 80."""
    score = update_score(0, "Win", 1)
    assert score == 80

def test_update_score_win_late():
    """Winning on later attempt gives fewer points, but at least 10."""
    score = update_score(0, "Win", 8)
    assert score == 10  # 100 - 10*(8+1) = 10 (minimum)

def test_update_score_too_high_even_attempt():
    """Too High on even attempt adds 5 points."""
    score = update_score(50, "Too High", 2)
    assert score == 55

def test_update_score_too_high_odd_attempt():
    """Too High on odd attempt subtracts 5 points."""
    score = update_score(50, "Too High", 1)
    assert score == 45

def test_update_score_too_low():
    """Too Low always subtracts 5 points."""
    score = update_score(50, "Too Low", 1)
    assert score == 45
    score = update_score(50, "Too Low", 2)
    assert score == 45

# Tests for get_range_for_difficulty
def test_range_easy():
    """Easy difficulty has range 1-20."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    """Normal difficulty has range 1-100."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    """Hard difficulty has range 1-50."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_range_invalid():
    """Invalid difficulty defaults to Normal range 1-100."""
    low, high = get_range_for_difficulty("Impossible")
    assert low == 1
    assert high == 100
