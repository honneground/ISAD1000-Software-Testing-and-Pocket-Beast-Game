"""
Question 3 C White Box Basic Test Code Implementation
"""
import GuessingGame
import sys
import io

def test_guessingGame():

    input_strings = ["41\n42", "43\n42", "42"]
    test_descriptions = ["lower", "higher", "exact"]
    expected_output = ["Guess a number between 1 and 100: Too low\nGuess again: You got it!",
                       "Guess a number between 1 and 100: Too high\nGuess again: You got it!",
                       "Guess a number between 1 and 100: You got it!"]
    for i in range(len(input_strings)):
        sys.stdout = io.StringIO()
        sys.stdin = io.StringIO(str(input_strings[i]))
        GuessingGame.guessing_game()
        assert expected_output[i] == sys.stdout.getvalue().strip(), test_descriptions[i]

if __name__ == "__main__":
    test_guessingGame()