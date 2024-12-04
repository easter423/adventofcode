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
f=open("1204.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

a=[]
while True:
    IN=IR()
    if not IN:
        break
    a.append(IN)

r,c=len(a),len(a[0])
print(r,c)

ans=0

dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]
xmas='XMAS'

def fn(x,y):
    global ans
    q,w,e,r=a[x-1][y-1],a[x+1][y+1],a[x+1][y-1],a[x-1][y+1]
    t=0
    if (q,w) in [('M','S'), ('S','M')]:
        t+=1
    if (e,r) in [('M','S'), ('S','M')]:
        t+=1
    if t==2:
        ans+=1

for i in range(1,r-1):
    for j in range(1,c-1):
        if a[i][j]=='A':
            fn(i,j)
print(ans)
f.close()