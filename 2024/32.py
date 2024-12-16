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

bdx=[1,0,-1,0]
bdy=[0,-1,0,1]

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
    
def funbw(x,y,face):
    nx=x+bdx[face]
    ny=y+bdy[face]
    if 0<=nx<bx and 0<=ny<by and board[nx][ny]!='#' and marked[nx][ny][face]==False and visited[nx][ny][face]==visited[x][y][face]-1:
        marked[nx][ny][face]=True
        funbw(nx,ny,face)
    fl=(face-1)%4
    fr=(face+1)%4
    fb=(face+2)%4
    f1,f2,f3=False,False,False
    if marked[x][y][fl]==False and visited[x][y][fl]==visited[x][y][face]-1000:
        marked[x][y][fl]=True
        f1=True
    if marked[x][y][fr]==False and visited[x][y][fr]==visited[x][y][face]-1000:
        marked[x][y][fr]=True
        f2=True
    if marked[x][y][fb]==False and visited[x][y][fb]==visited[x][y][face]-1000:
        marked[x][y][fb]=True
        f3=True
    if f1:
        funbw(x,y,fl)
    if f2:
        funbw(x,y,fr)
    if f3:
        funbw(x,y,fb)
    
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

ans=min(visited[ex][ey])
marked=[[[False]*4 for _ in range(by)] for _ in range(bx)]
for i in range(4):
    if visited[ex][ey][i]==ans:
        marked[ex][ey][i]=True
for i in range(4):
    if visited[ex][ey][i]==ans:
        funbw(ex,ey,i)

ans=0
for i in range(bx):
    for j in range(by):
        if True in marked[i][j]:
            ans+=1
print(ans)

f.close()