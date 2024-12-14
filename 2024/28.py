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
import time
input = sys.stdin.readline
f=open("1214.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

INS=[]
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
    INS.append([x,y,ax,ay])
# 912 1015 ~
# 947 1048 ~
times=7916
while True:
    try:
        board=[[0]*101 for _ in range(103)]
        for i in INS:
            x,y,ax,ay=i
            x+=ax*times
            x%=101
            y+=ay*times
            y%=103
            board[y][x]+=1
        print(f'=============== {times} ===============')
        for i in board:
            print(*i,sep='')
        print()
        times+=103
        time.sleep(0.2)
    except:
        break
f.close()