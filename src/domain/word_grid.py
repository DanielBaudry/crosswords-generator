import random
import string
from typing import List, Tuple

class LetterPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class WordGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[str]] = [['' for _ in range(width)] for _ in range(height)]

    def add_word(self, word: str, position: LetterPosition, direction: str) -> None:
        if direction == 'horizontal':
            if position.x + len(word) > self.width:
                raise ValueError("Word does not fit in the grid horizontally.")
            for i, char in enumerate(word):
                self.grid[position.y][position.x + i] = char
        elif direction == 'vertical':
            if position.y + len(word) > self.height:
                raise ValueError("Word does not fit in the grid vertically.")
            for i, char in enumerate(word):
                self.grid[position.y + i][position.x] = char
        else:
            raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

    def generate_random_letters(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '':
                    self.grid[i][j] = random.choice(string.ascii_lowercase)

    def get_grid(self) -> List[List[str]]:
        return self.grid