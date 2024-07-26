from src.domain.grid import Grid


def test_generate_grid_with_custom_size():
    # Given
    width = 9
    height = 9
    grid = Grid(width, height)

    # When
    generated_grid = grid.generate_grid()

    # Then
    expected_output = [
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
    ]
    assert generated_grid == expected_output


def test_write_word():
    # Given
    grid = Grid(5, 5)
    word = "hello"
    position = (2, 2)
    direction = "horizontal"
    reverse = False

    # When
    grid.write_word(word, position, direction, reverse)

    # Then
    expected_output = [
        ["", "", "", "", ""],
        ["", "", "h", "e", ""],
        ["", "", "l", "l", ""],
        ["", "", "o", "", ""],
        ["", "", "", "", ""],
    ]
    assert grid.grid == expected_output
