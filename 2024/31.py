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
f=open("1216.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
sys.setrecursionlimit(10**6)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def fun(x,y,face):
    nx=x+dx[face]
    ny=y+dy[face]
    if 0<=nx<bx and 0<=ny<by and board[nx][ny]!='#':
        if visited[nx][ny][face]>visited[x][y][face]+1:
            visited[nx][ny][face]=visited[x][y][face]+1
            fun(nx,ny,face)
    fl=(face-1)%4
    fr=(face+1)%4
    fb=(face+2)%4
    f1,f2,f3=False,False,False
    if visited[x][y][fl]>visited[x][y][face]+1000:
        visited[x][y][fl]=visited[x][y][face]+1000
        f1=True
    if visited[x][y][fr]>visited[x][y][face]+1000:
        visited[x][y][fr]=visited[x][y][face]+1000
        f2=True
    if visited[x][y][fb]>visited[x][y][face]+1000:
        visited[x][y][fb]=visited[x][y][face]+1000
        f3=True
    if f1:
        fun(x,y,fl)
    if f2:
        fun(x,y,fr)
    if f3:
        fun(x,y,fb)
    
board=[]
sx,sy=-1,-1
ex,ey=-1,-1
while True:
    IN=LIR()
    if not IN:
        break
    if sy==-1:
        sx+=1
        if 'S' in IN:
            sy=IN.index('S')
    if ey==-1:
        ex+=1
        if 'E' in IN:
            ey=IN.index('E')
    board.append(IN)
bx,by=len(board), len(board[0])
face=1
visited=[[[INF]*4 for _ in range(by)] for _ in range(bx)]
visited[sx][sy][1]=0

fun(sx,sy,1)

print(min(visited[ex][ey]))
f.close()