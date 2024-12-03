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
f=open("1203.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

ans=0
while True:
    try:
        flag=0
        x,y=0,0
        IN=IR()
        if not IN:
            break
        for c in IN:
            if c=='m':
                flag=1
                x,y=0,0
            elif c=='u' and flag==1:
                flag=2
            elif c=='l' and flag==2:
                flag=3
            elif c=='(' and flag==3:
                flag=4
            elif c.isdigit() and flag==4:
                x=int(c)
                flag=5
            elif c.isdigit() and flag==5:
                x*=10
                x+=int(c)
            elif c==',' and flag==5:
                flag=6
            elif c.isdigit() and flag==6:
                y=int(c)
                flag=7
            elif c.isdigit() and flag==7:
                y*=10
                y+=int(c)
            elif c==')' and flag==7:
                flag=0
                ans+=x*y
                x,y=0,0
            else:
                flag=0
                x,y=0,0
    except:
        break
print(ans)
f.close()