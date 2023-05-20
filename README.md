# Software Testing Exercises and Pocket Beast Game

- **Unit**: Introduction to Software Engineering (`ISAD1000` / `ISEN1000`) — Exercise 2
- **Study Period**: 2023 Trimester 1A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 95 (High Distinction)

## Exercise context

Exercise 2 combined project planning, requirements analysis, test design and a small object-oriented game. The submitted report covers PERT scheduling and dependencies, functional/non-functional requirements, unit-testing techniques and the Pocket Beast implementation. The repository contains the accompanying planning spreadsheets and Python code.

For the testing question, the brief required equivalence-partition, boundary-value and white-box tests, followed by a conversion to Python's `unittest` framework. It also required Git version control.

## Contents

| Directory | Delivered work |
|---|---|
| `Q1/` | Four spreadsheet files supporting the planning/PERT calculations and scheduling answers |
| `Q3/` | Three small target programs, standalone assertion scripts and a combined `unittest` class |
| `Q4/` | The two-player Pocket Beast game |

## Testing exercises

- `CalculatePercentage.py` and `testCalculatePercentage.py` exercise percentage calculation and invalid input partitions.
- `ReactorCoreWarning.py` and its test file exercise the warning categories at ten values around the temperature thresholds.
- `GuessingGame.py` and its test file exercise lower, higher and correct guesses. The tests use `io.StringIO` as simulated input and captured output.
- `testFrameworks.py` expresses those groups as three methods of `unittest.TestCase`.

The standalone test files contain ordinary functions with assertions and are executed as scripts; `testFrameworks.py` provides the separate `unittest.TestCase` suite.

## Pocket Beast

`Q4/pocket_beast_game.py` models players, their beasts and health, rival references and a round-based loop. Each player chooses whether to defend or attack; attacks use the sum of two six-sided dice to adjust the opponent's health.

## Run

Use Python 3; the code uses standard-library modules only.

From the project directory, run the combined framework suite:

```bash
cd Q3
python3 -m unittest testFrameworks.py
```

Run the original standalone assertion scripts separately:

```bash
python3 testCalculatePercentage.py
python3 testReactorCoreWarning.py
python3 testGuessingGame.py
```

For the game, from the project directory:

```bash
cd Q4
python3 pocket_beast_game.py
```

The game prompts both players for beast names and action choices. The four `Q1/*.xlsx` files can be opened separately to inspect the planning calculations.
