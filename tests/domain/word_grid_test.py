import pytest
from src.domain.word_grid import WordGrid, LetterPosition


def test_init():
    # Given
    width = 5
    height = 5

    # When
    grid = WordGrid(width, height)

    # Then
    assert grid.width == width
    assert grid.height == height
    assert len(grid.grid) == height
    assert len(grid.grid[0]) == width


def test_add_word_horizontal():
    # Given
    grid = WordGrid(5, 5)
    word = "hello"
    position = LetterPosition(0, 0)
    direction = "horizontal"

    # When
    grid.add_word(word, position, direction)

    # Then
    expected_grid = [
        ['h', 'e', 'l', 'l', 'o'],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ]
    assert grid.grid == expected_grid


def test_add_word_vertical():
    # Given
    grid = WordGrid(5, 5)
    word = "world"
    position = LetterPosition(0, 0)
    direction = "vertical"

    # When
    grid.add_word(word, position, direction)

    # Then
    expected_grid = [
        ['w', '', '', '', ''],
        ['o', '', '', '', ''],
        ['r', '', '', '', ''],
        ['l', '', '', '', ''],
        ['d', '', '', '', '']
    ]
    assert grid.grid == expected_grid


def test_add_word_invalid_direction():
    # Given
    grid = WordGrid(5, 5)
    word = "test"
    position = LetterPosition(0, 0)
    direction = "diagonal"

    # When
    with pytest.raises(ValueError):
        grid.add_word(word, position, direction)

    # Then
    # The ValueError is raised, so no assertions are needed
