"""
Question 3 D Convert Basic Test Code Implementation from A, B and C to Unit Testing Frameworks Implementation (unittest modules)
"""
import unittest
import CalculatePercentage
import ReactorCoreWarning
import GuessingGame
import sys
import io

class TestUtils(unittest.TestCase):

    def test_calculate_percentage(self):
        num1 = [1,2,1,0,-1]
        num2 = [2,1,-1,1,0]
        expRst = [50,-1,-1,-1,-1]
        msg = ["num2 > num1","num1 > num2","num1 ≤ 0","num2 ≤ 0","num1 ≤ 0, num2 ≤ 0"]    
        for i in range(len(msg)):
            self.assertTrue(abs(expRst[i] - CalculatePercentage.calculate_percentage(num1[i], num2[i]) < 0.000001), msg[i])

    def test_reactor_core_warning(self):
        inTemperatures = [299,300,649,650,799,800,949,950,1099,1100]
        expRst = ["Danger! Core temp too low","Warning! Core temp low. Decreased efficiency.","Warning! Core temp low. Decreased efficiency.","Reactor core operating at standard temperatures","Reactor core operating at standard temperatures","Reactor core operating at increased temperatures","Reactor core operating at increased temperatures","Warning! Core temp High. Deploy control rods.","Warning! Core temp High. Deploy control rods.","Danger! Core temp too high"]
        msg = ["too low / low lower boundary","too low / low upper boundary","low / standard lower boundary","low / standard upper boundary","standard / increased lower boundary","standard / increased upper boundary","increased / high lower boundary","increased / high upper boundary","high / dangerous lower boundary","high / dangerous upper boundary"]
        for i in range(len(msg)):
            self.assertEqual(expRst[i], ReactorCoreWarning.reactor_core_warning(inTemperatures[i]), msg[i])

    def test_guessingGame(self):
        input_strings = ["41\n42", "43\n42", "42"]
        test_descriptions = ["lower", "higher", "exact"]
        expected_output = ["Guess a number between 1 and 100: Too low\nGuess again: You got it!",
                        "Guess a number between 1 and 100: Too high\nGuess again: You got it!",
                        "Guess a number between 1 and 100: You got it!"]
        for i in range(len(test_descriptions)):
            sys.stdout = io.StringIO()
            sys.stdin = io.StringIO(str(input_strings[i]))
            GuessingGame.guessing_game()
            self.assertEqual(expected_output[i], sys.stdout.getvalue().strip(), test_descriptions[i])