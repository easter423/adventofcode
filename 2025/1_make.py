import math
import sys
from decimal import *

input = sys.stdin.readline
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
II = lambda: int(input())
IR = lambda: input().rstrip()
LIR = lambda: list(input().rstrip())
LIRS = lambda: list(input().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100
from random import randint

f = open("1201lg.in", "w")
for _ in range(10_000_000):
    if randint(0, 1):
        f.write("L")
    else:
        f.write("R")
    f.write(str(randint(1, 999)))
    f.write("\n")
f.close()
