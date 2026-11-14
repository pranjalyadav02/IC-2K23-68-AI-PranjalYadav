def solve(m, c, ml, cl, boat, path, visited):
    if ml == 0 and cl == 0:
        print("Solution possible")
        step = 0
        for state in path:
            left_m = state[0]
            left_c = state[1]
            right_m = m - left_m
            right_c = c - left_c
            if state[2] == 0:
                boat_side = "Left"
            else:
                boat_side = "Right"
            print("Step", step, ": Left bank:", left_m, "M,", left_c,
                  "C | Right bank:", right_m, "M,", right_c,
                  "C | Boat:", boat_side)
            step += 1
        print("Total steps:", step - 1)
        return True

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for x, y in moves:
        if boat == 0:
            nm = ml - x
            nc = cl - y
            nb = 1
        else:
            nm = ml + x
            nc = cl + y
            nb = 0
        rm = m - nm
        rc = c - nc
        if nm < 0 or nc < 0 or rm < 0 or rc < 0:
            continue
        if nm > 0 and nc > nm:
            continue
        if rm > 0 and rc > rm:
            continue
        new = (nm, nc, nb)
        if new not in visited:
            visited.add(new)
            path.append(new)
            if solve(m, c, nm, nc, nb, path, visited):
                return True
            path.pop()

    return False


m = int(input("Enter missionaries: "))
c = int(input("Enter cannibals: "))
if m < 0 or c < 0 or (m > 0 and c > m):
    print("No solution possible")
else:
    visited = {(m, c, 0)}
    if not solve(m, c, m, c, 0, [(m, c, 0)], visited):
        print("No solution possible")
