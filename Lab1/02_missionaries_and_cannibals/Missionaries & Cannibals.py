m = int(input("Enter missionaries: "))
c = int(input("Enter cannibals: "))
tm = m
tc = c
steps = 0
boat = 0
while (m > 0 or c > 0) and m>=c:
    print("\n------------------------")
    print("Left Bank :", m, "M,", c, "C")
    print("Right Bank:", tm-m, "M,", tc-c, "C")
    if boat == 0:
        print("Boat is on LEFT side")
    else:
        print("Boat is on RIGHT side")
    print("\nEnter people to move:")
    mm = int(input("Missionaries: "))
    cc = int(input("Cannibals: "))
    if mm < 0 or cc < 0:
        print("Invalid input!")
        continue
    elif mm + cc == 0 or mm + cc > 2:
        print("Boat can carry only 1 or 2 people!")
        continue
    elif boat == 0 and (mm > m or cc > c):
        print("Not enough people on this bank!")
        continue
    elif boat == 1 and (mm > tm-m or cc > tc-c):
        print("Not enough people on this bank!")
        continue
    if boat == 0:
        nm = m - mm
        nc = c - cc
    else:
        nm = m + mm
        nc = c + cc
    rm = tm - nm
    rc = tc - nc
    if (nm > 0 and nc > nm) or (rm > 0 and rc > rm):
        print("Invalid move! Cannibals will eat missionaries.")
        continue
    m = nm
    c = nc
    if boat == 0:
        boat = 1
        print("Boat moved LEFT to RIGHT")
    else:
        boat = 0
        print("Boat moved RIGHT to LEFT")
    steps += 1
    print("Step:", steps)
    print("Left Bank :", m, "M,", c, "C")
    print("Right Bank:", rm, "M,", rc, "C")
    if m == 0 and c == 0:
        print("\nSUCCESS! Everyone crossed safely!")
        break
else:
    print("Cannibals cannot be more than Missionaries")
print("\nTotal Steps Taken:", steps)
