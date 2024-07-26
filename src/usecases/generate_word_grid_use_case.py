import random
from typing import List
from src.domain.word_grid import LetterPosition, WordGrid


class GenerateWordGridUseCase:
    def __init__(self, width: int, height: int):
        self.word_grid = WordGrid(width, height)
        
    def generate_word_grid(self, words: List[str], num_rows: int, num_cols: int) -> None:
        if any(len(word) > num_cols for word in words):
            raise ValueError("The number of columns is shorter than the longest word in the list.")

        self.word_grid = WordGrid(num_cols, num_rows)

        for _ in range(1000):  # Limit the number of attempts to add words
            position = LetterPosition(
                random.randint(0, self.word_grid.width - 1),
                random.randint(0, self.word_grid.height - 1)
            )
            direction = random.choice(["horizontal", "vertical"])

            if self._can_add_word(word, position, direction):
                if direction == "horizontal":
                    self._add_word_horizontally(word, position)
                else:
                    self._add_word_vertically(word, position)
                break

        self._generate_random_letters()


    def _can_add_word(self, word: str, position: LetterPosition, direction: str) -> bool:
        if direction == "horizontal":
            if position.x + len(word) > self.word_grid.width:
                return False
            for i in range(len(word)):
                if not self.word_grid.is_empty_cell(position.x + i, position.y):
                    return False
        else:
            if position.y + len(word) > self.word_grid.height:
                return False
            for i in range(len(word)):
                if not self.word_grid.is_empty_cell(position.x, position.y + i):
                    return False
        return True


    def _add_word_horizontally(self, word: str, position: LetterPosition) -> None:
        for i in range(len(word)):
            self.word_grid.set_cell(position.x + i, position.y, word[i])


    def _add_word_vertically(self, word: str, position: LetterPosition) -> None:
        for i in range(len(word)):
            self.word_grid.set_cell(position.x, position.y + i, word[i])
