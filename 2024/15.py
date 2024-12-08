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
    row+=1
R=row
ans=0
for c in d:
    l=len(d[c])
    for i in range(l-1):
        for j in range(i+1,l):
            x1,y1=2*d[c][i][0]-d[c][j][0],2*d[c][i][1]-d[c][j][1]
            x2,y2=2*d[c][j][0]-d[c][i][0],2*d[c][j][1]-d[c][i][1]
            if 0<=x1<R and 0<=y1<C and (not (x1,y1) in antinode):
                antinode.add((x1,y1))
                #print(x1,y1)
                ans+=1
            if 0<=x2<R and 0<=y2<C and (not (x2,y2) in antinode):
                antinode.add((x2,y2))
                #print(x2,y2)
                ans+=1
print(ans)
f.close()