# Software Testing Exercises and Pocket Beast Game

- **Unit**: Introduction to Software Engineering (`ISAD1000` / `ISEN1000`) — Exercise 2
- **Study Period**: 2023 Trimester 1A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 95 (High Distinction)

<table>
  <thead>
    <tr>
      <th colspan="6">Curtin University &bull; Bachelor of Information Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr align="center" style="font-weight: bold; background-color: #f6f8fa;">
      <td>2022 T3A</td>
      <td>2023 T1A</td>
      <td>2023 T2A</td>
      <td>2023 T3A</td>
      <td>2024 T1A</td>
      <td>2024 T2A</td>
    </tr>
    <tr>
      <td valign="top">
        <abbr title="Fundamentals of Programming (92 HD)"><b>COMP1005</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP1005-Vampire-Ecosystem-Simulation">Vampire Eco</a><br>        &bull; <a href="https://github.com/honneground/COMP1005-Vehicle-Emissions-Analyzer">Emissions</a><br>      </td>
      <td valign="top" style="background-color: #f1f8ff; border: 2px solid #0969da;">
        <abbr title="Data Structures and Algorithms (89 HD)"><b>COMP1002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP1002-StudyHelp-Academic-Network">StudyHelp</a><br>        &bull; <a href="https://github.com/honneground/COMP1002-Advanced-Data-Structures-and-Visualizer">Visualizer</a><br>        <abbr title="Unix and C Programming (90 HD)"><b>COMP1000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP1000-Terminal-Maze-Survival-Game">Maze Survival</a><br>        &bull; <a href="https://github.com/honneground/COMP1000-Terminal-Maze-Darkness-Game">Maze Darkness</a><br>        &bull; <a href="https://github.com/honneground/COMP1000-Bookstore-Transaction-Simulator">Bookstore</a><br>        <abbr title="Introduction to Software Engineering (95 HD)"><b>ISAD1000</b></abbr><br>
        &bull; <b>&#128073; Pocket Beast</b><br>      </td>
      <td valign="top">
        <abbr title="Unix Systems Programming (88 HD)"><b>COMP2002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP2002-Parallel-Directory-File-Calculator">Dir Calculator</a><br>        <abbr title="Operating Systems (80 HD)"><b>COMP2006</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP2006-Customer-Queue-Concurrency-Simulation">Queue Sim</a><br>      </td>
      <td valign="top">
        <abbr title="Database Systems (80 HD)"><b>ISYS2014</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISYS2014-Relational-Database-Management-System">FootyStats DB</a><br>        <abbr title="Quantitative Techniques for Business (87 HD)"><b>ECOM2001</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ECOM2001-Econometric-Statistical-Analysis-R">Econometric R</a><br>      </td>
      <td valign="top">
        <abbr title="Financial Decision Making (93 HD)"><b>ACCT1002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ACCT1002-Financial-Decision-Calculators">Finance Tools</a><br>        <abbr title="Human Computer Interface (71 D)"><b>ICTE3002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ICTE3002-Lumen-Interaction-Design">Lumen UI</a><br>        <abbr title="Engineering Management and Professional Practice (79 D)"><b>MGMT3000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/MGMT3000-Phone-Router-Repurposing-Design">Phone Router</a><br>      </td>
      <td valign="top">
        <abbr title="Capstone Computing Project 1 (94 HD)"><b>ISAD3000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISAD3000-CurtinSG-App-Design">CurtinSG UI</a><br>        <abbr title="Capstone Computing Project 2 (95 HD)"><b>ISAD3001</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISAD3001-CurtinSG-Student-App">CurtinSG App</a><br>        <abbr title="Advanced Computer Communications (88 HD)"><b>CNCO3002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/CNCO3002-Multi-Service-Socket-Server">Socket Server</a><br>      </td>
    </tr>
  </tbody>
</table>


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

---

## Portfolio note

This Git repository was created retrospectively from the original project code, with assistance from OpenAI Codex and Antigravity in curating the repository and writing this README for publication. The initial commit timestamp is backdated to the original coursework submission date, followed by the final release commit.


