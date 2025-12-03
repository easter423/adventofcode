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
        now = [0] * 12
        for i in IN:
            for j in range(11):
                if now[j] < now[j + 1]:
                    for k in range(j, 11):
                        now[k] = now[k + 1]
                    now[11] = i
                    break
            else:
                if now[11] < i:
                    now[11] = i
        for idx, i in enumerate(now):
            ans += i * (10 ** (11 - idx))
    except:
        break
print(ans)
