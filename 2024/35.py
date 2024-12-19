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
f=open("1218.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split(',')))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split(','))
INF = math.inf

sz=71
board=[[True]*sz for _ in range(sz)]
dist=[[INF]*sz for _ in range(sz)]
for _ in range(1024):
    a,b=LI()
    board[a][b]=False
dist[0][0]=0
q=deque([(0,0,0)])
dx=[0,1,0,-1]
dy=[1,0,-1,0]
while q:
    x,y,now=q.popleft()
    if now>dist[x][y]:
        continue
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<sz and 0<=ny<sz and board[nx][ny]:
            if dist[nx][ny]>dist[x][y]+1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny,dist[nx][ny]))
print(dist[sz-1][sz-1])

f.close()