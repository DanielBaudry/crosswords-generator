# crosswords-generator

AI assisted code
We want to generate code that follows the SOLID principles, is tested and built with clean architecture.

## Input

- (mandatory) A list of words in the system
Example:
[
    "cookie",
    "pasta",
    "dog",
    "giraffe",
]
- (optional) Width of the generated grid
- (optional) Length of the generated grid


## Output

The system should generate a grid containing the list of words and completed by random letters :
Example:
[
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
]

## Rules

1. The system will generate a grid containing all the given words
2. If all the words does not fit in the generated grid, an exception will be raised
3. Word can be placed horizontally
4. Word can be placed vertically
5. Word can be placed diagonally
6. Word can be placed in both ways
7. Remaining empty cell in grid will be filled with random letters
8. The system should try to placed words, by crossing one letter from each.
Example: pasta and giraffe, both have an "a" letter, so the can cross with it



