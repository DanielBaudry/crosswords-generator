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

