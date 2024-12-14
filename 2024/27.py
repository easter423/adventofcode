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
f=open("1214.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

board=[[0]*103 for _ in range(101)]
z1,z2,z3,z4=0,0,0,0
while True:
    IN=LIRS()
    if not IN:
        break
    x,y=IN[0].split(',')
    x=int(x[2:])
    y=int(y)
    ax,ay=IN[1].split(',')
    ax=int(ax[2:])
    ay=int(ay)
    x+=ax*100
    x%=101
    y+=ay*100
    y%=103
    print(x,y)
    if x<50 and y<51:
        z1+=1
    elif x>50 and y<51:
        z2+=1
    elif x<50 and y>51:
        z3+=1
    elif x>50 and y>51:
        z4+=1
print(z1*z2*z3*z4)
f.close()