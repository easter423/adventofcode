import sys, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import Fraction
from decimal import *
from heapq import heapify, heappop, heappush, heappushpop
from datetime import datetime
from functools import cache
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

f=open("1201.in","r")
a,b=[],[]
for i in range(1000):
    x,y=map(int,f.readline().rstrip().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
ans=0
for i in range(1000):
    ans+=abs(a[i]-b[i])
print(ans)