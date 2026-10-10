class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False
        else:
            a = 0
            b = 0
            v = set()
            while (a, b) not in v:
                v.add((a, b))
                if a + b == target:
                    return True

                if a == 0:
                    a = x

                elif b == y:
                    b = 0

                else:
                    water = min(a, y - b)
                    a -= water
                    b += water
        return False

x=int(input("Enter Capacity of the First Jug: "))
y=int(input("Enter Capacity of the Second Jug: "))
target=int(input("Enter Target: "))
a=Solution()
print(a.canMeasureWater(x,y,target))


