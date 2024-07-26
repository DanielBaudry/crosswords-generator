import pytest
from unittest.mock import ANY
from typing import List
from src.domain.word_grid import LetterPosition, WordGrid
from src.usecases.generate_word_grid_use_case import GenerateWordGridUseCase


def test_generate_word_grid_with_valid_input(generate_word_grid_use_case):
    words = ["apple", "banana", "cherry"]
    num_rows = 6
    num_cols = 10
    generate_word_grid_use_case.generate_word_grid(words, num_rows, num_cols)
    grid = generate_word_grid_use_case.word_grid.get_grid()
    assert len(grid) == num_rows
    assert len(grid[0]) == num_cols
    # Add an assert to check the expected output grid
    expected_grid = [
        ["a", "p", "p", "l", "e", ANY, ANY, ANY, ANY, ANY],
        ["b", "a", "n", "a", "n", "a", ANY, ANY, ANY, ANY],
        ["c", "h", "e", "r", "r", "y", ANY, ANY, ANY, ANY],
        [ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY],
        [ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY],
        [ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY, ANY]
    ]
    assert grid == expected_grid


def test_generate_word_grid_with_invalid_input(generate_word_grid_use_case):
    words = ["apple", "banana", "cherry"]
    num_rows = 2
    num_cols = 5
    with pytest.raises(ValueError):
        generate_word_grid_use_case.generate_word_grid(
            words, num_rows, num_cols)


@pytest.fixture
def generate_word_grid_use_case():
    return GenerateWordGridUseCase(10, 10)