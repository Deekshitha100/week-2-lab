# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a console-based Hangman game in Python. Students will practice string handling, loops, conditionals, and user interaction while implementing game logic.

## 📝 Tasks

### 🛠️Set up word selection and state tracking

#### Description
Define a list of possible secret words and randomly choose one at the start of each game. Initialize data structures to track which letters have been guessed and remaining attempts.

#### Requirements
Completed program should:

- Contain a predefined list (e.g. Python list) of words.
- Randomly select a word using the `random` module.
- Set up variables for guessed letters, current display (e.g. `_ a _ _`), and remaining guesses.

### 🛠️Implement the main game loop

#### Description
Create a loop that repeatedly prompts the player for a letter, updates game state, and displays progress until the game ends.

#### Requirements
Completed program should:

- Prompt the user for a single letter guess and handle invalid input gracefully.
- Update the display to reveal matching letters in the word.
- Maintain a list of incorrect guesses and decrement remaining attempts when a wrong letter is chosen.
- Redisplay current progress and remaining guesses after each turn.

### 🛠️Handle win/lose conditions and replay option

#### Description
Determine when the player has guessed the word or run out of attempts, show an appropriate message, and optionally offer to play again.

#### Requirements
Completed program should:

- Display a congratulatory message when the word is fully revealed.
- Show a failure message with the word when attempts reach zero.
- Optionally ask the player if they want to start a new game.
