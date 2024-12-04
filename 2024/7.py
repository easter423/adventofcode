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

def fn(x,y,k,cnt):
    global ans
    if cnt==4:
        ans+=1
        return
    x+=dx[k]
    y+=dy[k]
    if 0<=x<r and 0<=y<c:
        if a[x][y]==xmas[cnt]:
            fn(x,y,k,cnt+1)

for i in range(r):
    for j in range(c):
        if a[i][j]=='X':
            for k in range(8):
                fn(i,j,k,1)
print(ans)
f.close()