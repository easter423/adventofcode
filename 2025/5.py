import math
from decimal import *

f = open("1203.in", "r")
MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split(","))
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100


ans = 0
while True:
    try:
        IN = list(map(int, IR()))
        if not IN:
            break
        x, y = 0, 0
        for i in IN:
            if x < y:
                x = y
                y = i
            else:
                if y < i:
                    y = i
        ans += 10 * x + y
    except:
        break
print(ans)
