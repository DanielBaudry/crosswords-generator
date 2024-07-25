import random
import string

class WordGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['' for _ in range(width)] for _ in range(height)]

    def add_word(self, word, position, direction):
        if direction == 'horizontal':
            if position[0] + len(word) > self.width:
                raise ValueError("Word does not fit in the grid horizontally.")
            for i, char in enumerate(word):
                self.grid[position[1]][position[0] + i] = char
        elif direction == 'vertical':
            if position[1] + len(word) > self.height:
                raise ValueError("Word does not fit in the grid vertically.")
            for i, char in enumerate(word):
                self.grid[position[1] + i][position[0]] = char
        else:
            raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

    def generate_random_letters(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '':
                    self.grid[i][j] = random.choice(string.ascii_lowercase)

    def get_grid(self):
        return self.grid