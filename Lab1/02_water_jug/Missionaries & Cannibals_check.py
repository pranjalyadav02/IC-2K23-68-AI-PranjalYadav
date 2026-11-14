def solve(m, c, ml, cl, boat, path, visited):
    if ml == 0 and cl == 0:
        print("Solution possible")
        for step, (left_m, left_c, boat) in enumerate(path):
            print(
                f"Step {step}: Left bank: {left_m} M, {left_c} C | "
                f"Right bank: {m - left_m} M, {c - left_c} C"
            )
        print("Total steps:", len(path) - 1)
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
