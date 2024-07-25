import pytest

from src.domain.word_grid import LetterPosition
from src.usecases.generate_word_grid_use_case import GenerateWordGridUseCase


def given_generate_word_grid_use_case(width, height):
    return GenerateWordGridUseCase(width, height)


def when_generate_word_grid(use_case, words):
    use_case.generate_word_grid(words)


def then_word_grid_has_expected_dimensions(grid, expected_rows, expected_cols):
    assert len(grid) == expected_rows
    assert len(grid[0]) == expected_cols


def then_words_are_added_to_grid_correctly(grid, expected_grid):
    assert grid == expected_grid


def test_generate_word_grid():
    # Given
    use_case = given_generate_word_grid_use_case(5, 5)
    words = ["hello", "world", "python", "programming", "challenge"]

    # When
    when_generate_word_grid(use_case, words)

    # Then
    then_word_grid_has_expected_dimensions(use_case.get_grid(), 5, 5)
    expected_grid = [
        ["hello", "worl", "pytho", "progr", "challe"],
        ["d", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ]
    then_words_are_added_to_grid_correctly(use_case.get_grid(), expected_grid)