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
f=open("1201.in","r")
MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

x=50
ans=0
while True:
    try:
        a=IR()
        b=int(a[1:])
        if a[0]=='L':
            x-=b
        else:
            x+=b
        x%=100
        if x==0:
            ans+=1
    except:
        break
print(ans)