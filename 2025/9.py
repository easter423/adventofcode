import math
from decimal import *

f = open("1205.in", "r")
MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split("-")))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split(""))
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

ans = 0
IN = []
while True:
    try:
        a, b = LI()
        IN.append((a, "a"))
        IN.append((b, "c"))
    except:
        break

while True:
    try:
        c = II()
        IN.append((c, "b"))
    except:
        break

IN.sort()
now = 0
for i, mode in IN:
    if mode == "a":
        now += 1
    elif mode == "b":
        if now:
            ans += 1
    else:
        now -= 1
print(ans)
