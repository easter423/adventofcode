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
f=open("1212.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

board=[]
while True:
    a=LIR()
    if not a:
        break
    board.append(a)
h,w=len(board),len(board[0])

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def fun(x, y, c):
    global cnt
    for border in [(x,y,1),(x+1,y,1),(x,y,0),(x,y+1,0)]:
        if border in ns:
            continue
        elif border in s:
            s.remove(border)
            ns.add(border)
        else:
            s.add(border)
    cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=h or ny>=w or visited[nx][ny] or board[nx][ny]!=c:
            continue
        visited[nx][ny]=True
        fun(nx,ny,c)

ans=0
visited=[[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if visited[i][j]:
            continue
        s=set([])
        ns=set([])
        cnt=0
        visited[i][j]=True
        fun(i,j, board[i][j])
        ans+=cnt*len(s)
print(ans)

f.close()