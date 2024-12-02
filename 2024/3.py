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
f=open("1202.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

cnt=0
while True:
    try:
        IN=LI()
        x=IN[0]
        if IN[0]<IN[1]:
            flag=True
        elif IN[0]>IN[1]:
            flag=False
        else:
            continue
        for i in IN[1:]:
            if 1<=abs(x-i)<=3 and (i!=x) and flag^(x>i):
                x=i
                continue
            else:
                break
        else:
            cnt+=1
    except:
        break
print(cnt)
f.close()