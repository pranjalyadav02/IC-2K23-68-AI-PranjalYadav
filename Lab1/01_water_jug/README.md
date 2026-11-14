# Problem 1: Water Jug Problem

## 1. Problem Statement
Given two jugs with capacities $X$ and $Y$ liters respectively, and an infinite supply of water, determine whether it is possible to measure exactly $Z$ (or `target`) liters of water using the two jugs.

The permissible operations are:
1. Completely fill either jug.
2. Completely empty either jug.
3. Pour water from one jug into another until the other jug is full or the first jug is empty.

---

## 2. State Space Representation
- **State:** Represented as an ordered pair `(a, b)`, where:
  - `a`: Amount of water currently in Jug 1 ($0 \le a \le X$)
  - `b`: Amount of water currently in Jug 2 ($0 \le b \le Y$)
- **Initial State:** `(0, 0)` (both jugs empty)
- **Goal State:** Any state `(a, b)` such that `a + b == target` or `a == target` or `b == target`.

---

## 3. Implementations

### Approach A: State Simulation (`water_jug.py`)
- Simulates the pour-and-fill process step-by-step using a `while` loop.
- Keeps track of visited states `(a, b)` in a hash set to detect and avoid infinite cycles.
- Transition rules:
  1. If Jug 1 is empty, fill Jug 1 (`a = x`).
  2. If Jug 2 is full, empty Jug 2 (`b = 0`).
  3. Otherwise, pour water from Jug 1 into Jug 2 until Jug 2 is full or Jug 1 is empty:
     $$\text{transfer} = \min(a, y - b)$$
- Counts total steps taken to reach the target amount.

### Approach B: Mathematical / Diophantine Equation (`Water_Jug- Using Gcd.py`)
- Based on Bézout's Identity: Any measurable volume $Z$ must satisfy:
  $$Z \le X + Y \quad \text{and} \quad Z \pmod{\gcd(X, Y)} = 0$$
- This gives an $O(\log(\min(X, Y)))$ mathematical check for solvability.

---

## 4. How to Run

### Interactive Simulation:
```bash
python "water_jug.py"
```

**Example Input:**
```text
Enter Capacity of the First Jug: 3
Enter Capacity of the Second Jug: 5
Enter Target: 4
```

**Example Output:**
```text
True
Total Step count = 6
```

### GCD Solvability Check:
```bash
python "Water_Jug- Using Gcd.py"
```

**Example Input:**
```text
Enter Capacity of Jug 1: 3
Enter Capacity of Jug 2: 5
Enter Target: 4
```

**Example Output:**
```text
True
```

