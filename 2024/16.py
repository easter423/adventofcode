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
f=open("1208.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

d=defaultdict(list)
row=0
antinode=set([])
while True:
    IN=IR()
    if not IN:
        break
    C=len(IN)
    for col, c in enumerate(IN):
        if c!='.':
            d[c].append((row,col))
            antinode.add((row,col))
    row+=1
R=row
for c in d:
    l=len(d[c])
    for i in range(l-1):
        for j in range(i+1,l):
            x1,y1=d[c][i][0], d[c][i][1]
            x2,y2=d[c][j][0], d[c][j][1]
            ax,ay=x1,y1
            bx,by=x2,y2
            ax,ay,bx,by=2*ax-bx,2*ay-by,ax,ay
            while 0<=ax<R and 0<=ay<C:
                if (ax,ay) not in antinode:
                    antinode.add((ax,ay))
                ax,ay,bx,by=2*ax-bx,2*ay-by,ax,ay
            ax,ay=x1,y1
            bx,by=x2,y2
            ax,ay,bx,by=bx,by,2*bx-ax,2*by-ay
            while 0<=bx<R and 0<=by<C:
                if (bx,by) not in antinode:
                    antinode.add((bx,by))
                ax,ay,bx,by=bx,by,2*bx-ax,2*by-ay
print(len(antinode))
f.close()