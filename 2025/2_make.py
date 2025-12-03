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

f = open("1202lg.in", "w")
for _ in range(1_000_000):
    x = randint(1, 10)
    y = randint(1, 10)
    a = randint(1, int("9" * x))
    b = randint(1, int("9" * y))
    f.write(str(a))
    f.write("-")
    f.write(str(a + b))
    f.write(",")
f.close()
