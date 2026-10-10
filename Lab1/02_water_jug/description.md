# Water and Jug Problem

## Approach: Simulation and Hash Set

I solved the Water and Jug Problem by simulating the jug operations using a `while` loop and `if-elif-else` conditions.

Initially, both jugs are empty. I fill the first jug when it is empty, empty the second jug when it is full, and otherwise pour water from the first jug into the second jug.

I use a hash set to store previously visited states `(a, b)` to prevent infinite loops. At each step, I check whether the total amount of water in both jugs equals the target. If it does, I return `True`. If a state repeats without reaching the target, I return `False`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(x \times y)$, since there are at most $(x + 1) \times (y + 1)$ possible jug states.
- **Space Complexity:** $\mathcal{O}(x \times y)$, because the hash set stores visited states.

---

## Result

- **Test Cases:** All 32 test cases passed.(On Leetcode)
- **Runtime:** 0 ms (beats 100.00%).
- **Memory Usage:** 12.42 MB (beats 25.29%).
