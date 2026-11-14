# Problem 2: Missionaries and Cannibals Problem

## 1. Problem Statement
Three (or $M$) missionaries and three (or $C$) cannibals must cross a river using a boat that can hold at most two people.

### Constraints:
1. The boat can carry a maximum of 2 people and a minimum of 1 person per trip.
2. At no point on either river bank can the cannibals outnumber the missionaries (if any missionaries are present), otherwise the cannibals will overpower and eat the missionaries.
3. The boat cannot cross by itself; at least one person must row the boat.

---

## 2. State Space Representation
- **State:** `(M_left, C_left, Boat_position)`
  - `M_left`: Number of missionaries on the left bank ($0 \le M_{left} \le M$)
  - `C_left`: Number of cannibals on the left bank ($0 \le C_{left} \le C$)
  - `Boat_position`: `0` if the boat is on the left bank, `1` if on the right bank.
- **Right Bank People:**
  - $M_{right} = M - M_{left}$
  - $C_{right} = C - C_{left}$
- **Initial State:** `(M, C, 0)` (all people and boat on left bank)
- **Goal State:** `(0, 0, 1)` (all people and boat on right bank)

### Valid State Condition:
For any state, both banks must satisfy:
- Left bank: If $M_{left} > 0$, then $M_{left} \ge C_{left}$
- Right bank: If $M_{right} > 0$, then $M_{right} \ge C_{right}$

---

## 3. Implementations

### Script 1: Interactive Game (`Missionaries & Cannibals.py`)
- CLI-based game enabling a user to manually select how many missionaries and cannibals cross the river in each turn.
- Validates constraints after each move and provides feedback on whether the move was valid or if cannibals overpowered the missionaries.
- Tracks and displays total step count upon reaching the goal state.

### Script 2: Recursive Backtracking Solver (`Missionaries & Cannibals_check.py`)
- Automated depth-first search (DFS) with backtracking.
- Explores all 5 legal boat transfer combinations: `[(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]`.
- Uses a `visited` set of states to prevent infinite recursive loops.
- Prints the exact sequence of states and steps from initial to goal state.

---

## 4. How to Run

### Interactive Game:
```bash
python "Missionaries & Cannibals.py"
```

### Automated Solver:
```bash
python "Missionaries & Cannibals_check.py"
```

**Example Input:**
```text
Enter missionaries: 3
Enter cannibals: 3
```

**Example Output:**
```text
Solution possible
Step 0 : Left bank: 3 M, 3 C | Right bank: 0 M, 0 C | Boat: Left
Step 1 : Left bank: 3 M, 1 C | Right bank: 0 M, 2 C | Boat: Right
Step 2 : Left bank: 3 M, 2 C | Right bank: 0 M, 1 C | Boat: Left
...
Step 11 : Left bank: 0 M, 0 C | Right bank: 3 M, 3 C | Boat: Right
Total steps: 11
```

