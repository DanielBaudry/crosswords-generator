from typing import List, Tuple

from src.domain.word_grid import LetterPosition, WordGrid


# GenerateWordGridUseCase
class GenerateWordGridUseCase:
    def __init__(self, width: int, height: int):
        self.word_grid = WordGrid(width, height)

    def generate_word_grid(self, words: List[str]) -> None:
        # Calculate the grid size based on the number of words
        num_words = len(words)
        num_rows = (num_words + 4) // 5  # Assuming each word takes 5 cells horizontally
        num_cols = 5  # Assuming each word takes 5 cells vertically

        # Resize the word grid
        self.word_grid = WordGrid(num_cols, num_rows)

        # Add words to the grid
        position = LetterPosition(0, 0)
        for word in words:
            if position.x + len(word) > self.word_grid.width:
                position.x = 0
                position.y += 1
            self._add_word_horizontally(word, position)
            position.x += len(word) + 1  # Add a space after each word

        # Generate random letters for empty cells
        self._generate_random_letters()

    def _add_word_horizontally(self, word: str, position: LetterPosition) -> None:
        self.word_grid.add_word(word, position, "horizontal")

    def _generate_random_letters(self) -> None:
        self.word_grid.generate_random_letters()

    def get_grid(self) -> List[List[str]]:
        return self.word_grid.get_grid()
