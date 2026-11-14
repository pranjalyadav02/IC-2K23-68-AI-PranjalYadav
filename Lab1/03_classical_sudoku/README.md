# Problem 3: Classical Sudoku

## 1. Problem Statement
Sudoku is a logic-based constraint satisfaction problem. A $9 \times 9$ grid must be filled with numbers from 1 to 9 such that:
1. Each row contains all digits from 1 to 9 without repetition.
2. Each column contains all digits from 1 to 9 without repetition.
3. Each of the nine $3 \times 3$ sub-grids contains all digits from 1 to 9 without repetition.

---

## 2. Problem Formulation (Constraint Satisfaction Problem)
- **Variables:** 81 cells in the $9 \times 9$ matrix: $X_{r, c}$ where $r, c \in \{0, 1, \dots, 8\}$.
- **Domain:** $D = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$ for empty cells.
- **Constraints:**
  - Row constraint: $\forall r, \text{AllDifferent}(X_{r, 0}, X_{r, 1}, \dots, X_{r, 8})$
  - Column constraint: $\forall c, \text{AllDifferent}(X_{0, c}, X_{1, c}, \dots, X_{8, c})$
  - Box constraint: $\forall \text{block } B, \text{AllDifferent}(X_{i, j} \in B)$

---

## 3. Implementation Details (`classical_sudoku.py`)

### Backtracking Generation & Solving:
- Uses a recursive backtracking function `generate(board)` to create a complete, valid $9 \times 9$ Sudoku solution.
- Randomly removes 40 cells to create a playable puzzle instance while preserving original clues.

### Graphical User Interface (Tkinter):
- Interactive $9 \times 9$ grid displaying original numbers in black (disabled) and player entries in blue.
- Controls:
  - **Submit:** Validates move against Sudoku rules, updates the grid, increments the move counter, and checks for completion.
  - **Erase:** Clears a user-entered number (original puzzle numbers cannot be erased).
  - **New Game:** Generates and loads a freshly randomized puzzle.
  - **Step Counter & Status Bar:** Tracks number of player attempts and shows feedback.

---

## 4. How to Run

### Requirements:
Python 3.x with `tkinter` (included with standard Python on Windows and macOS).

### Execution:
```bash
python "classical_sudoku.py"
```
A desktop GUI window titled **Sudoku Game** will open. Enter the row (1-9), column (1-9), and digit (1-9) in the input fields and click **Submit**.

