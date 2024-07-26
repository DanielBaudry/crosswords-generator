class Grid:
    def __init__(self, width, height):
        self.grid = [[""] * width for _ in range(height)]

    def generate_grid(self):
        return self.grid

    def write_word(self, word, position, direction, reverse):
        if direction == "horizontal":
            start_row, start_col = position
            if reverse:
                start_col = max(start_col - len(word), 0)
            else:
                start_col = min(start_col + len(word), len(self.grid[0]) - len(word))

            if start_col + len(word) > len(self.grid[0]):
                raise ValueError(f"Word '{word}' is too long to fit in the grid at position {position} with horizontal direction and non-reverse way.")

        elif direction == "vertical":
            start_row, start_col = position
            if reverse:
                start_row = max(start_row - len(word), 0)
            else:
                start_row = min(start_row + len(word), len(self.grid))

            if start_row + len(word) > len(self.grid):
                raise ValueError(f"Word '{word}' is too long to fit in the grid at position {position} with vertical direction and non-reverse way.")

        else:
            raise ValueError("Invalid direction. Direction must be 'horizontal' or 'vertical'.")