"""Tests for text preprocessing."""
import pytest

from src.data.text_preprocessing import text_preprocessing


@pytest.mark.parametrize(
    "test_input,expected", [
        (" ветер ()@@", "ветер"),
        ("«mouse»©", "mouse"),
        ("как здорово! очень, очень рада за вас! 😊👍",
         "как здорово! очень, очень рада за вас!")
    ]
)
def test_text_preprocessing(test_input, expected) -> None:
    """Test for text preprocessing function.
    @param test_input: input test raw string
    @param expected: expected clean string
    """
    assert text_preprocessing(test_input) == expected