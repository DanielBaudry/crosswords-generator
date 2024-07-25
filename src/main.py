
# Usage example
from src.usecases.usecase import GenerateWordGridUseCase


def main():
    # Create a 5x5 word grid use case
    use_case = GenerateWordGridUseCase(5, 5)

    # List of words to add to the grid
    words = ["hello", "world", "python", "programming", "challenge"]

    # Generate the word grid
    use_case.generate_word_grid(words)

    # Print the word grid
    for row in use_case.get_grid():
        print(row)


if __name__ == "__main__":
    main()
